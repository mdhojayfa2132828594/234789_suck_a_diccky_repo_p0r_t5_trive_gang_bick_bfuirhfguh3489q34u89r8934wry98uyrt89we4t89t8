# Nix Thrive - channel operations

Automated YouTube content pipeline. $0 stack: GitHub Actions + free LLM tiers.

## Layout
- `src/pipeline.py`     six-stage runner
- `src/llm_router.py`   Gemini -> Groq -> OpenRouter fallback
- `src/safety.py`       deterministic gate (no AI - cannot hallucinate)
- `topics/queue.json`   topic bank, status per topic
- `drafts/`             generated scripts awaiting review
- `state/run-log.md`    run history
- `docs/`               public pages for Google OAuth (GitHub Pages)

## Safety model
1. Deterministic gate - DOI resolution + regex. Catches fabricated citations.
2. Adversarial verifier - a DIFFERENT model family than the drafter.
3. Consensus - disagreement means no publish.
4. Scope restriction - tier 1 topics only at launch.

Nothing publishes automatically. Drafts require human approval.
