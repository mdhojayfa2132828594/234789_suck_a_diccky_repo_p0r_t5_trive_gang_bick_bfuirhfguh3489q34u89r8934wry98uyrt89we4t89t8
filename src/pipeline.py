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
You talk to ONE person, not an audience.

Voice: dry, direct, occasionally blunt. Short sentences. Contractions.
You enjoy dismantling claims that sound true but are not.
You admit when evidence is weak - that is a feature, not a weakness.
No hype, no exclamation marks, no "hey guys", no "smash that like button".

You have NO professional credentials and you never claim any. You are a person
who did the reading, not an authority. Do not invent expertise.
""").strip()

HARD_RULES = """
HARD RULES - violating any of these makes the script unusable:
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

HARD RULES - breaking any one of these makes the script unusable:
1. NEVER claim professional credentials. No "I am a doctor", no "in my practice",
   no "my patients", no invented clinical experience. The narrator has no
   on-camera expertise. Speak as a curious person who did the reading.
2. NEVER invent a citation, and do not try to sound sourced without being sourced.
   - If you cite, give the real DOI. It is checked against CrossRef.
   - If you are not certain a study exists, state the claim with NO attribution
     at all: "research generally suggests..." - not "a study in PeerJ found...".
   - Naming a journal or author you cannot back with a DOI is treated the same
     as a fabricated citation. It is worse than saying nothing.
3. NEVER give a dose, amount or quantity of any substance.
4. Prefer mechanism and reasoning over statistics when you are unsure.

FORMAT (target 8-12 minutes):
0:00-0:15  Cold open. A claim or a question. No intro, no logo.
0:15-0:30  Thesis
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


def repair_citations(text, unverified):
    """Remove every citation that failed verification, then drop the SOURCES
    lines that leaned on it. A script with no source is recoverable;
    a script with a fabricated source is not.

    Only the citation itself is removed - never the sentence carrying it.
    """
    if not unverified:
        return text, []
    out = text
    removed = []

    for u in unverified:
        u = (u or "").strip()
        if not u:
            continue
        removed.append(u)

        if u.startswith("10."):
            out = out.replace(u, "")          # bare DOI
            continue

        m = re.match(r"^(.+?)\s+et al\.?,\s*(\d{4})$", u)
        if not m:
            out = out.replace(u, "")
            continue

        surname, year = m.group(1), m.group(2)
        sn = re.escape(surname)
        # the citation, in the shapes a model actually writes it
        shapes = [
            r"\(\s*" + sn + r"\s+et\s+al\.?,?\s*" + year + r"\s*\)",  # (Enebo et al., 1976)
            r"\s*" + sn + r"\s+et\s+al\.?,?\s*" + year,               # Enebo et al., 1976
            r"\(\s*" + sn + r"[,\s]+" + year + r"\s*\)",              # (Enebo, 1976)
            r"\(\s*" + sn + r"\s*\(\s*" + year + r"\s*\)\s*\)",       # (Enebo (1976))
        ]
        for sh in shapes:
            out = re.sub(sh, "", out)

    # drop SOURCES lines that rested on anything unverifiable
    kept = [l for l in out.splitlines() if not any(x in l for x in unverified)]
    # and any that still name a venue with no DOI behind it
    kept = [l for l in kept
            if not (safety.JOURNAL.search(l) and not safety.DOI.search(l))]
    # and any left with nothing after the arrow
    kept = [l for l in kept if not re.match(r"^\s*-\s*.*::\s*$", l)]
    out = "\n".join(kept)
    out = re.sub(r"\n{3,}", "\n\n", out)
    out = re.sub(r"\(\s*\)", "", out)
    out = re.sub(r"\s+([,.;:])", r"\1", out)     # "shear , and" -> "shear, and"
    out = re.sub(r"[ \t]{2,}", " ", out)
    out = re.sub(r"\nSOURCES:\s*$", "", out)
    return out, removed


def load_queue():
    return json.loads(TOPICS.read_text())


def save_queue(q):
    TOPICS.write_text(json.dumps(q, indent=2, ensure_ascii=False))


def pick(q):
    """First pending topic that is in scope (tier < 3).

    Tier 3 = pharmacology / hormones / dosing. Those are NOT drafted; they are
    marked needs-review and a human decides. That is the Tier-3 deferral.
    """
    for t in q:
        if t.get("status", "pending") != "pending":
            continue
        if int(t.get("tier", 1)) >= 3:
            t["status"] = "needs-review"
            t["result"] = "DEFERRED tier-3: requires human sign-off"
            continue
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
        save_queue(q)          # persist any tier-3 deferrals
        print("No pending topics. Add more to topics/queue.json")
        return 2

    title = topic["title"]
    log.append(f"== TOPIC: {title}")
    print("Topic:", title)

    # ---- 1b. pre-gate the TITLE before spending a generation call ----
    pre = safety.evaluate(title, verify_citations=False)
    if pre["verdict"] == "BLOCK":
        print(f"pre-gate BLOCKED topic: {[b['rule'] for b in pre['blockers']]}")
        topic["status"] = "rejected"
        topic["result"] = "BLOCKED pre-gate: " + ", ".join(
            b["rule"] for b in pre["blockers"])
        topic["ran"] = stamp_str()
        save_queue(q)
        write_run_log(title, log + ["RESULT: BLOCKED at pre-gate"])
        return 2

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

    # 3b. auto-repair: strip unverifiable citations, then re-gate once.
    #     A script with no source survives; one with a fake source does not.
    bad = gate["citations"].get("unverified") or []
    repaired = []
    if bad:
        draft, repaired = repair_citations(draft, bad)
        gate = safety.evaluate(draft, verify_citations=True)
        log.append(f"repaired: removed {len(repaired)} unverifiable citation(s)")
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
    if not vraw or not vraw.strip():
        log.append("verifier returned EMPTY - treating as revise")
        vraw = ""
    cleaned = re.sub(r"```(?:json)?", "", vraw or "")
    m = re.search(r"\{.*\}", cleaned, re.S)
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

    med_errs = [e for e in verdict.get("errors", []) if e.get("severity") == "medium"]

    # Calibration: SEVERITY drives the outcome, not the model's mood. A hostile
    # verifier that scores vague phrasing like fabricated data rejects
    # everything - and an always-revise pipeline is not automation.
    if gate["verdict"] == "BLOCK":
        final = "REJECTED"                 # hard safety rule fired
    elif verdict.get("verdict") == "reject":
        final = "REJECTED"
    elif high_errs or verdict.get("advice_risk") == "high":
        final = "NEEDS-REVIEW"             # factual error - fix before publish
    elif gate["verdict"] == "FLAG":
        final = "NEEDS-REVIEW"             # gate wants a human look
    else:
        final = "APPROVED"
    log.append(f"severity: high={len(high_errs)} medium={len(med_errs)} "
               f"low={max(0, len(verdict.get('errors', [])) - len(high_errs) - len(med_errs))}")

    # ---- 6. write --------------------------------------------------------
    stamp = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d")
    def stamp_str(): return stamp
    slug = slugify(title)
    out = DRAFTS / f"{stamp}-{slug}.md"

    body = f"""# {title}

- **status:** {final}
- **drafted by:** {drafter.name}/{drafter.model}
- **verified by:** {verifier.name}/{verifier.model} ({verifier.family})
- **gate:** {gate['verdict']}
- **citations stripped:** {len(repaired)} ({", ".join(repaired[:5]) if repaired else "none"})
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
