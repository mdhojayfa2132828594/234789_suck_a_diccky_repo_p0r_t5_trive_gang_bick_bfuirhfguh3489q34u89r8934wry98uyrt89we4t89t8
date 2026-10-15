# Status — what the pipeline actually does today

Date: 2026-10-13

This is an honest record of the first real runs. Not a sales page.

---

## What is live

| Piece | State |
|---|---|
| GitHub Actions daily run | ✅ working, cron 06:00 UTC, dispatchable |
| Secrets | ✅ 6 stored, encrypted client-side, never in the repo |
| Multi-provider router | ✅ Gemini → Groq → OpenRouter, model-level fallback |
| Deterministic safety gate | ✅ 9 blockers, 3 flags, 2 note categories |
| Adversarial verifier | ✅ different model family than the drafter |
| Drafts committed to repo | ✅ yes, with full gate + verifier JSON attached |
| Publishing | ❌ NOT built. Nothing publishes without a human. |

---

## The headline finding

**The drafter fabricates citations. Constantly. The verification stack catches it.**

Across five real topics, every single script contained fabricated sources:

| Fabricated thing | Caught by |
|---|---|
| `10.1111/j.1469-7580.2004.00350.x` | gate — CrossRef 404 |
| `10.1016/j.clinbiomech.2004.09.009` | verifier |
| `10.1519/JSC.0b013e3181a90af6` | verifier |
| "Enebo et al., 1976" | gate — author-year CrossRef check |
| Gundersen 2016, DOI `10.1242/jeb.148535` | verifier — right author, wrong paper |
| "a PeerJ study" (no DOI) | gate — venue named, no resolvable DOI |

**Every unverifiable citation in these runs was fake.** Not one was real-but-unresolvable.
Check for yourself: `curl https://api.crossref.org/works/10.1111/j.1469-7580.2004.00350.x` → 404.

## The second finding

The drafter also makes real factual errors, not just fake citations:

- *"Quarter squats bypass the stretch-shortening cycle entirely"* — false.
- *"Missing your post-workout window spikes cortisol and eats your muscle"* — false.
- *"Static stretching does nothing to prevent injuries"* — overstated, evidence is mixed.
- *"Your lats attach your arms to your spine and pelvis"* — inserts on the humerus, not the pelvis.

## The third finding

When I banned invented DOIs, the model **switched to inventing journal names**
("a study in the Journal of Biomechanics"). It complied with the letter of the rule
and defeated its purpose. Both holes are now closed.

## What changed after the repair pass

Unverifiable citations are now **stripped automatically** and the script is re-gated.
A script with no source survives; one with a fake source does not.

| Metric | Before | After |
|---|---|---|
| Gate PASS | 2 of 5 | **5 of 6** |
| Fake citations surviving into drafts | 1–5 per script | **0** |

## Current pass rate

6 of 6 topics come out `NEEDS-REVIEW`, not because of citations any more — those are
now handled — but because the verifier finds **1–2 genuine high-severity factual
errors in every script**. That is the real remaining bottleneck, and it is a property
of the drafter, not of the pipeline.

Zero scripts have reached `APPROVED`. That is honest, not a failure: the system is
catching real errors. Anyone claiming an LLM writes publishable factual scripts
today without this kind of checking is not checking.

## Channel framing (corrected)

**This is not a medical channel.** It is general life advice. Consequences:

- The "final-year medical student" persona was **removed** — it made the model
  invent clinical authority, which the `fabricated-credential` blocker then caught.
  The two were fighting each other.
- The scripted "I'm not your doctor" line was **removed**.
- Medical blockers (dosing, pharma, disease claims) stay on. Even a non-medical
  channel should not tell people what to ingest.
- GLP-1 / pharmacology stays **Tier 3 — deferred**. It needs a human-written
  script. The pipeline will not draft it.

---

## What the gate catches (deterministic — cannot be talked out of it)

**BLOCKS**
- `dosing-numbers`, `dosing-advice` — any quantity+unit
- `fabricated-credential` — "I am a doctor", "in my practice", "my patients"
- `pharma-product` — named drugs, incl. GLP-1s and androgens
- `disease-claim` — "treats/cures/prevents <disease>"
- `pregnancy`, `sensitive-topic`

**FLAGS** (human must look)
- `unverified-citation` — DOI or author-year that fails CrossRef
- `named-venue-no-doi` — journal named, no resolvable DOI
- `absolute-language` — cures, guaranteed, clinically proven
- `medical-personalization` — reads as advice to a specific patient

**NOTES** (recorded, do not block)
- `general-advice` — "you should". This is an advice channel; flagging it
  guaranteed 100% human review and killed the automation.
- `intensifier` — "instantly", "immediately"

---

## Bugs found and fixed during this build

1. Groq 403 — Cloudflare rejects Python's default User-Agent. Fixed with a browser UA.
2. Gemini 2.5 retired for new accounts → now `gemini-3.8-flash`, with model-level fallback.
3. `gpt-oss-120b` is a reasoning model: returns null `content`, real output in `reasoning`.
4. Dosing regex fired on "Take a chest-up cue" → required a unit noun after the quantity.
5. `individual-advice` fired 8×/script on harmless coaching → split into NOTE vs real
   medical personalisation.
6. Verifier's own mood (not severity) drove the verdict → recalibrated on severity.

## Known gaps

- Publishing is not built. YouTube upload code exists in no workflow.
- Comment → video loop is not built.
- TTS and thumbnails not wired up, though the Gemini key supports both.
- OpenRouter could not be verified from the dev sandbox (DNS blocked). It is in the
  fallback chain and untested as a primary.
- The 7-day OAuth refresh-token trap still applies while the consent screen is in
  Testing status. Publish the app to clear it.
