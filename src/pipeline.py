"""
Channel pipeline - v1.

Stages:
  1. pick topic          from topics/queue.json
  2. draft script        Gemini (long generation)
  3. deterministic gate  safety.py  - no AI, cannot hallucinate
  4. adversarial verify  Groq (DIFFERENT model family than the drafter)
  5. consensus           merge verdicts -> approved / needs-review / rejected
  6. write draft         drafts/*.md + state/run-log.md   (nothing publishes)

Exit codes: 0 ok · 2 no topics · 3 all providers failed
"""

import json, os, re, sys, time, pathlib, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from llm_router import build_providers, Router   # noqa: E402
import safety                                     # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOPICS = ROOT / "topics" / "queue.json"
DRAFTS = ROOT / "drafts"
STATE = ROOT / "state"

PERSONA = os.environ.get("PERSONA", """
You are the host of a YouTube self-improvement channel.
You are a final-year medical student who works in a hospital and reads research
for fun. You talk to ONE person, not an audience.

Voice: dry, direct, occasionally blunt. Short sentences. Contractions.
You enjoy dismantling bad health claims. You admit when evidence is weak.
No hype, no exclamation marks, no "hey guys", no "smash that like button".
""").strip()

HARD_RULES = """
HARD RULES - violating any of these makes the script unusable:
- "I'm not your doctor" appears once, early, naturally - never as a legal disclaimer.
- No dosing. Never state a quantity of any substance.
- No diagnosis. No advice for an individual's specific body or symptom.
- Never name a pharmaceutical or supplement as a recommendation.
- No "magic bullet", "cure", "instantly", "guaranteed", "100%".
- Every factual claim gets a source. Put sources in a SOURCES block at the end,
  one per line, formatted: - <claim> :: <source title or DOI>
- If the evidence is genuinely weak, say so in the script. That is a feature.
"""

DRAFT_PROMPT = """Write a YouTube script.

TOPIC: {topic}

FORMAT (target 8-12 minutes):
0:00-0:15  Cold open. A claim or a question. No intro, no logo.
0:15-0:30  Thesis + "I'm not your doctor"
0:30-7:00  3-5 chapters, one idea each. Mark visuals as [VISUAL: ...]
~7:00      "Bro-science corner" - one claim dismantled
8:00-9:00  Receipts - sources on screen
9:00-9:30  One open question to drive comments

OUTPUT EXACTLY:

TITLES:
1. ...
2. ...
3. ...
4. ...
5. ...

DESCRIPTION:
<2 sentences>

THE NUMBER:
<one concrete figure used in this episode>

SCRIPT:
<full script with [VISUAL: ...] markers and timestamps>

SOURCES:
- <claim> :: <source>
- <claim> :: <source>
"""

VERIFY_PROMPT = """You are a HOSTILE fact-checker. Your job is to find errors,
not to approve. Assume the draft is overconfident and that some citations may
be fabricated.

Return ONLY this JSON:

{{
  "errors": [
    {{"claim": "<exact text>", "problem": "<what is wrong>", "severity": "high|medium|low"}}
  ],
  "unverifiable": ["<claims you cannot confirm>"],
  "overclaims": ["<absolute or exaggerated statements>"],
  "advice_risk": "<none|low|high - does this read as advice for a specific person?>",
  "confidence": "high|medium|low",
  "verdict": "pass|revise|reject"
}}

Be strict. If you find nothing wrong, say so - but you are penalised for
approving content that later turns out to be wrong.

DRAFT:
{draft}
"""


def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:60]


def load_queue():
    return json.loads(TOPICS.read_text())


def save_queue(q):
    TOPICS.write_text(json.dumps(q, indent=2, ensure_ascii=False))


def pick(q):
    for t in q:
        if t.get("status", "pending") == "pending":
            return t
    return None


def main():
    DRAFTS.mkdir(exist_ok=True)
    STATE.mkdir(exist_ok=True)
    log = []

    providers = build_providers()
    if not providers:
        print("FATAL: no LLM API keys in environment")
        return 3
    router = Router(providers, log=log)

    q = load_queue()
    topic = pick(q)
    if not topic:
        print("No pending topics. Add more to topics/queue.json")
        return 2

    title = topic["title"]
    log.append(f"== TOPIC: {title}")
    print("Topic:", title)

    # ---- 2. draft -------------------------------------------------------
    draft, drafter = router.call(
        task="draft",
        prompt=DRAFT_PROMPT.format(topic=title),
        system=PERSONA + "\n\n" + HARD_RULES,
        prefer="gemini",
        max_tokens=6000,
        temperature=0.75,
    )

    # ---- 3. deterministic gate ------------------------------------------
    gate = safety.evaluate(draft, verify_citations=True)
    log.append(f"gate: {gate['verdict']} "
               f"(blockers={len(gate['blockers'])}, flags={len(gate['flags'])})")

    # ---- 4. adversarial verify (different family) ------------------------
    vraw, verifier = router.call(
        task="verify",
        prompt=VERIFY_PROMPT.format(draft=draft[:14000]),
        system="You are a strict, hostile scientific fact-checker. Output JSON only.",
        prefer="groq",
        avoid_family=drafter.family,
        max_tokens=2500,
        temperature=0.2,
    )
    m = re.search(r"\{.*\}", vraw, re.S)
    try:
        verdict = json.loads(m.group(0)) if m else {"verdict": "revise",
                                                    "errors": [], "confidence": "low"}
    except Exception:
        verdict = {"verdict": "revise", "errors": [], "confidence": "low",
                   "parse_note": "verifier returned non-JSON"}

    log.append(f"verifier ({verifier.family}): {verdict.get('verdict')} "
               f"confidence={verdict.get('confidence')}")

    # ---- 5. consensus ----------------------------------------------------
    high_errs = [e for e in verdict.get("errors", []) if e.get("severity") == "high"]

    if gate["verdict"] == "BLOCK":
        final = "REJECTED"
    elif high_errs or verdict.get("advice_risk") == "high":
        final = "REJECTED"
    elif gate["verdict"] == "FLAG" or verdict.get("verdict") != "pass":
        final = "NEEDS-REVIEW"
    else:
        final = "APPROVED"

    # ---- 6. write --------------------------------------------------------
    stamp = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    slug = slugify(title)
    out = DRAFTS / f"{stamp}-{slug}.md"

    body = f"""# {title}

- **status:** {final}
- **drafted by:** {drafter.name}/{drafter.model}
- **verified by:** {verifier.name}/{verifier.model} ({verifier.family})
- **gate:** {gate['verdict']}
- **generated:** {stamp}

## Safety gate
```json
{json.dumps(gate, indent=2)[:4000]}
```

## Verifier
```json
{json.dumps(verdict, indent=2)[:4000]}
```

## Draft

{draft}
"""
    out.write_text(body)

    topic["status"] = {"APPROVED": "done", "REJECTED": "rejected",
                       "NEEDS-REVIEW": "review"}.get(final, "review")
    topic["result"] = final
    topic["draft"] = out.name
    topic["ran"] = stamp
    save_queue(q)

    (STATE / "run-log.md").open("a").write(
        f"\n## {stamp} — {title}\n\n"
        f"- result: **{final}**\n"
        f"- gate: {gate['verdict']} · blockers {len(gate['blockers'])} "
        f"flags {len(gate['flags'])}\n"
        f"- verifier: {verdict.get('verdict')} (confidence {verdict.get('confidence')})\n"
        f"- draft: `drafts/{out.name}`\n"
    )

    print("\n".join(log))
    print("\nRESULT:", final)
    print("draft ->", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
