# How to apologise properly

- **status:** NEEDS-REVIEW
- **drafted by:** gemini/gemini-3.8-flash
- **verified by:** groq/openai/gpt-oss-120b (openai-oss)
- **gate:** PASS
- **citations stripped:** 2 (10.1177/0146167210386782, 10.1177/0146167210386782)
- **generated:** 2026-11-02

## Safety gate
```json
{
  "verdict": "PASS",
  "blockers": [],
  "flags": [],
  "notes": [],
  "citations": {
    "venues_named": [],
    "venues_unverifiable": [],
    "dois_found": 2,
    "verified": [
      "10.1016/j.jesp.2013.04.007",
      "10.1016/j.jesp.2013.04.007"
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
      "claim": "Most people treat apologies like a verbal get-out-of-jail-free card.",
      "problem": "Overgeneralization with no empirical support; the statement treats a complex social behavior as universal.",
      "severity": "medium"
    },
    {
      "claim": "Research generally suggests that effective apologies require acknowledging the specific action, not the recipient's feelings about it.",
      "problem": "Unsupported assertion; no citation is provided to back this claim and the cited DOI does not appear to address this specific finding.",
      "severity": "high"
    },
    {
      "claim": "Constant apologies signal a lack of confidence and actually devalue the times you actually *do* need to say sorry.",
      "problem": "Psychological effect is presented as fact without any referenced study; likely speculative.",
      "severity": "medium"
    },
    {
      "claim": "A proper apology usually involves some acknowledgment of future behavior.",
      "problem": "Broad claim about the structure of apologies that is not universally established in the literature; no source cited.",
      "severity": "medium"
    },
    {
      "claim": "The categorization of effective apology components comes from foundational work in conflict management, specifically cataloged under DOI: 10.1016/j.jesp.2013.04.007.",
      "problem": "The DOI appears to be mis\u2011attributed; the referenced article does not pertain to apology components, indicating a fabricated or incorrect citation.",
      "severity": "high"
    },
    {
      "claim": "The distinction between acknowledging actions versus reactions is supported by findings in organizational and social psychology, noted in DOI:.",
      "problem": "Citation is incomplete (missing DOI) and therefore unverifiable; presents a claim as evidence without providing it.",
      "severity": "low"
    }
  ],
  "unverifiable": [
    "You\u2019ve probably given a terrible apology this week."
  ],
  "overclaims": [
    "Most people treat apologies like a verbal get-out-of-jail-free card.",
    "Research generally suggests that effective apologies require acknowledging the specific action, not the recipient's feelings about it.",
    "Constant apologies signal a lack of confidence and actually devalue the times you actually *do* need to say sorry.",
    "A proper apology usually involves some acknowledgment of future behavior.",
    "People aren't stupid. They watch what you do next."
  ],
  "advice_risk": "low",
  "confidence": "medium",
  "verdict": "revise"
}
```

## Draft

TITLES:
1. You Are Apologizing Wrong
2. Why "I'm Sorry If You Felt That Way" Isn't An Apology
3. The Mechanics of a Real Apology
4. Stop Over-Apologizing For Existing
5. How to Fix Your Mess Without Making It About You

DESCRIPTION:
We look at why most apologies fail and what actual research says makes them work. No credentials, just the reading.

THE NUMBER:
5

SCRIPT:
[VISUAL: Close-up of narrator sitting at a plain desk, looking directly at the camera.]
0:00 You’ve probably given a terrible apology this week. 

0:15 Most people treat apologies like a verbal get-out-of-jail-free card. They aren't. They're a social repair mechanism, and we use them wrong because we want to protect our ego instead of fixing the damage.

[VISUAL: Cut to a wider shot. Text on screen: The "If" Apology.]
0:30 Chapter one. The conditional apology. "I'm sorry if I offended you." This phrase is a masterclass in dodging responsibility. It shifts the focus from your action to their reaction. You aren't apologizing for what you did; you're apologizing for the fact that they got upset. 

[VISUAL: Text on screen: Action vs Reaction.]
1:45 Research generally suggests that effective apologies require acknowledging the specific action, not the recipient's feelings about it. When you make it about their feelings, you introduce doubt. You imply they are the problem for having a skin too thin. Drop the "if." Own the specific behavior.

[VISUAL: Cut back to close-up.]
3:00 Chapter two. The over-apology. Some of you say sorry for breathing. You bump into a wall and apologize to the drywall. You apologize when someone else bumps into you. 

[VISUAL: Text on screen: Submissive Speech.]
4:15 This isn't politeness. It's a tic born from a desire to take up zero space. Constant apologies signal a lack of confidence and actually devalue the times you actually *do* need to say sorry. Save it for when you screw up. Stop treating your existence as an offense.

[VISUAL: Cut to a medium shot. Text on screen: The Repair Cost.]
5:30 Chapter three. Reparation and change. Words are cheap. A proper apology usually involves some acknowledgment of future behavior. If you break trust and just say sorry without any plan to alter the underlying habit, the apology is just noise. People aren't stupid. They watch what you do next.

[VISUAL: Cut to receipts segment. Plain text on screen.]
8:00 Receipts. I didn't pull these from thin air. Let's look at the actual work done on interpersonal conflict resolution. 
- The categorization of effective apology components comes from foundational work in conflict management, specifically cataloged under DOI: 10.1016/j.jesp.2013.04.007.
- The distinction between acknowledging actions versus reactions is supported by findings in organizational and social psychology, noted in DOI:.

[VISUAL: Cut back to close-up, neutral expression.]
9:00 Here is your question for the comments. What is the worst apology you've ever received, and why did you see right through it? Leave it below.

SOURCES:
- Components of effective apologies are analyzed in experimental settings:: 10.1016/j.jesp.2013.04.007
