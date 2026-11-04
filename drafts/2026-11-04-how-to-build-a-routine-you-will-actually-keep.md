# How to build a routine you will actually keep

- **status:** NEEDS-REVIEW
- **drafted by:** gemini/gemini-3.8-flash
- **verified by:** groq/openai/gpt-oss-120b (openai-oss)
- **gate:** PASS
- **citations stripped:** 0 (none)
- **generated:** 2026-11-04

## Safety gate
```json
{
  "verdict": "PASS",
  "blockers": [],
  "flags": [],
  "notes": [
    {
      "rule": "general-advice",
      "match": "you need to",
      "context": "in, gesturing with one hand] Let's talk about the idea that you need to hack your dopamine to build a routine. You'll see people on",
      "reason": "Second-person advice - normal for this channel."
    }
  ],
  "citations": {
    "venues_named": [
      "science"
    ],
    "venues_unverifiable": [],
    "dois_found": 1,
    "verified": [
      "10.1002/ejsp.674"
    ],
    "unverified": [],
    "author_year_verified": [],
    "author_year_unverified": []
  }
}
```

## Verifier
```json
{
  "errors": [
    {
      "claim": "You\u2019ve likely heard that it takes twenty-one days to form a habit. That number is a folk legend. It comes from a plastic surgeon's observations in the nineteen-fifties about patients getting used to their new faces.",
      "problem": "The origin of the 21\u2011day myth is misattributed; it is usually traced to Dr. Maxwell Maltz\u2019s 1960 book *Psycho\u2011Cybernetics*, not a 1950s plastic surgeon. The statement is likely false.",
      "severity": "high"
    },
    {
      "claim": "Most routines fail because they rely on motivation instead of reducing friction.",
      "problem": "Overgeneralization with no supporting evidence; routine failure is multifactorial.",
      "severity": "medium"
    },
    {
      "claim": "Research generally suggests that emotional states are poor predictors of consistent behavioral output.",
      "problem": "Broad claim without citation; the literature shows mixed results, not a universal rule.",
      "severity": "medium"
    },
    {
      "claim": "Big goals feel impressive to talk about. Small goals actually get finished.",
      "problem": "Absolute statement lacking empirical backing; while smaller goals can be effective, the claim ignores contexts where large goals succeed.",
      "severity": "low"
    },
    {
      "claim": "You don't need a protocol. You just need to lower the friction.",
      "problem": "Overly simplistic advice; habit formation often benefits from structured protocols as well as friction reduction.",
      "severity": "low"
    },
    {
      "claim": "SOURCES: - Habits are formed over variable lengths of time, not a fixed twenty-one days :: 10.1002/ejsp.674",
      "problem": "The DOI appears fabricated or mismatched; no verifiable article with that identifier supports the claim.",
      "severity": "high"
    }
  ],
  "unverifiable": [
    "It comes from a plastic surgeon's observations in the nineteen\u2011fifties about patients getting used to their new faces.",
    "The DOI 10.1002/ejsp.674 corresponds to a source that cannot be confirmed."
  ],
  "overclaims": [
    "Most routines fail because they rely on motivation instead of reducing friction.",
    "Research generally suggests that emotional states are poor predictors of consistent behavioral output.",
    "Big goals feel impressive to talk about. Small goals actually get finished.",
    "You don't need a protocol. You just need to lower the friction."
  ],
  "advice_risk": "low",
  "confidence": "medium",
  "verdict": "revise"
}
```

## Draft

TITLES:
1. Why Your Routines Fail
2. The Myth of Motivation
3. Friction Over Force
4. The 66-Day Myth
5. Building a Routine That Sticks

DESCRIPTION:
Most routines fail because they rely on motivation instead of reducing friction. We'll look at the actual data on habit formation and why smaller changes usually win.

THE NUMBER:
66

SCRIPT:
[VISUAL: Close up of narrator sitting at a plain wooden desk, looking directly at the camera]
0:00 You’ve probably tried to overhaul your entire life on a Sunday night and quit by Wednesday. Why does that keep happening?

0:15 The problem isn't your discipline. The problem is you're treating habit formation like a moral test instead of a design problem. 

0:30 Chapter one: The motivation trap. 
[VISUAL: Text graphic on screen: Motivation is an unreliable state]
We wait to feel like doing things. That’s backwards. Action usually precedes the feeling of wanting to do the thing. If you wait for motivation, you’ll be waiting forever. Research generally suggests that emotional states are poor predictors of consistent behavioral output. 

1:45 Chapter two: Friction is everything.
[VISUAL: Narrator holding up a TV remote, then putting it in a drawer]
If you want to read more, put the book on your pillow. If you want to stop scrolling, put your phone in another room. We tend to take the path of least resistance. Instead of fighting that, use it. Lower the activation energy required to start the behavior you want, and raise it for the behavior you don't. 

3:15 Chapter three: The scale of the goal.
[VISUAL: Split screen showing a massive workout plan vs. a single push-up]
Big goals feel impressive to talk about. Small goals actually get finished. When people try to build a routine, they usually start too big. They plan an hour at the gym when they haven't exercised in five years. A smaller target executed daily beats a massive target abandoned on day four. 

4:45 Chapter four: The timeline.
[VISUAL: Graphic of a wavy line trending upward]
You’ve likely heard that it takes twenty-one days to form a habit. That number is a folk legend. It comes from a plastic surgeon's observations in the nineteen-fifties about patients getting used to their new faces. Actual data on habit formation shows a wide spread. Some behaviors take much longer to become automatic. 

6:00 Bro-science corner.
[VISUAL: Narrator leaning in, gesturing with one hand]
Let's talk about the idea that you need to hack your dopamine to build a routine. You'll see people online talking about cold plunges and zero-sugar diets as tools for baseline optimization. The evidence here is pretty thin. Most of these claims rely on acute physiological spikes that don't translate to long-term behavioral change. You don't need a protocol. You just need to lower the friction.

7:15 [VISUAL: Cut to black, then text displaying sources on screen one by one]
Receipts. 
The study tracking habit formation times found significant variation across participants, ranging from a couple of months to over eight months for a behavior to reach automaticity. 

9:00 What is the smallest possible version of the habit you're trying to build right now, and what is currently stopping you from doing it today? Leave it in the comments.

SOURCES:
- Habits are formed over variable lengths of time, not a fixed twenty-one days :: 10.1002/ejsp.674
