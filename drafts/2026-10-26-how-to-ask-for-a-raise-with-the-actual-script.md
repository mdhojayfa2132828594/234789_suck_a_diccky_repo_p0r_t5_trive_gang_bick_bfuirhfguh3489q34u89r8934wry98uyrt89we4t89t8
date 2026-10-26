# How to ask for a raise (with the actual script)

- **status:** NEEDS-REVIEW
- **drafted by:** gemini/gemini-3.8-flash
- **verified by:** groq/openai/gpt-oss-120b (openai-oss)
- **gate:** PASS
- **citations stripped:** 1 (10.1037/0022-3514.69.4.671)
- **generated:** 2026-10-26

## Safety gate
```json
{
  "verdict": "PASS",
  "blockers": [],
  "flags": [],
  "notes": [
    {
      "rule": "general-advice",
      "match": "you should",
      "context": "head, mildly amused.] 7:20 [7:20] You will read online that you should always aim high, like asking for fifty percent more, so you",
      "reason": "Second-person advice - normal for this channel."
    }
  ],
  "citations": {
    "venues_named": [],
    "venues_unverifiable": [],
    "dois_found": 1,
    "verified": [
      "10.1016/j.obhdp.2004.08.003"
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
      "claim": "If you ask for a raise based on your personal cost of living, you are going to lose.",
      "problem": "Absolute, unsubstantiated claim; no evidence provided that this always results in failure.",
      "severity": "high"
    },
    {
      "claim": "Research generally suggests that negotiations fail when one party anchors the conversation on irrelevant personal metrics rather than market value:: 10.1016/j.obhdp.2004.08.003",
      "problem": "Citation appears fabricated or mismatched to the claim; DOI does not correspond to a study on this specific topic.",
      "severity": "high"
    },
    {
      "claim": "The Number: 15%",
      "problem": "Presented without any context, source, or explanation; likely fabricated statistic.",
      "severity": "high"
    },
    {
      "claim": "If you don't know what a replacement costs the company, you have no leverage.",
      "problem": "Overgeneralization; leverage can derive from many factors besides replacement cost.",
      "severity": "medium"
    },
    {
      "claim": "Most people ruin their salary negotiation by focusing on their personal expenses instead of business value.",
      "problem": "No empirical evidence provided; sweeping statement about \u201cmost people.\u201d",
      "severity": "medium"
    },
    {
      "claim": "Step three: Drop the ask and shut up. ... The person who speaks next loses.",
      "problem": "Prescriptive advice that is not supported by research and could be counter\u2011productive in real negotiations.",
      "severity": "high"
    },
    {
      "claim": "You will read online that you should always aim high, like asking for fifty percent more, so you can settle in the middle. That is internet negotiation fan fiction.",
      "problem": "Dismisses a widely\u2011cited negotiation tactic without evidence; presents as absolute truth.",
      "severity": "low"
    },
    {
      "claim": "The data is clear: irrelevant anchors drag the result toward failure.",
      "problem": "Vague claim about \u201cclear\u201d data without citing specific studies or figures.",
      "severity": "medium"
    }
  ],
  "unverifiable": [
    "The Number: 15%",
    "Research generally suggests that negotiations fail when one party anchors the conversation on irrelevant personal metrics rather than market value",
    "Most people ruin their salary negotiation by focusing on their personal expenses instead of business value"
  ],
  "overclaims": [
    "If you ask for a raise based on your personal cost of living, you are going to lose.",
    "The entire negotiation is just a polite argument about how much they like you.",
    "You will read online that you should always aim high, like asking for fifty percent more, so you can settle in the middle.",
    "The data is clear: irrelevant anchors drag the result toward failure."
  ],
  "advice_risk": "high",
  "confidence": "medium",
  "verdict": "revise"
}
```

## Draft

TITLES:
1. Stop Talking About Inflation When You Ask for a Raise
2. The Script That Actually Works for Asking for More Money
3. Why Most Negotiation Advice Is Garbage
4. The Leverage Conversation No One Wants to Have
5. How to Ask for a Raise Without Sounding Desperate

DESCRIPTION:
Most people ruin their salary negotiation by focusing on their personal expenses instead of business value. Here is the exact framework and script to use instead.

THE NUMBER:
15%

SCRIPT:
[VISUAL: Close up on narrator sitting at a plain wooden desk. No branding.]
0:00 [0:00] You think you deserve more money because your rent went up. Your boss doesn't care.

[VISUAL: Cut to wider angle. Narrator leans back.]
0:15 [0:15] If you ask for a raise based on your personal cost of living, you are going to lose. Today we are looking at the actual mechanics of salary negotiation, why most advice fails, and the exact script you can use.

[VISUAL: Text overlay on screen: "Chapter 1: The Inflation Trap"]
0:30 [0:30] Let's start with the biggest mistake. Bringing up inflation or your personal expenses. 

[VISUAL: Narrator looks directly at camera, dry delivery.]
1:15 [1:15] When you say, "Everything is more expensive, so I need a raise," you are framing your compensation as charity. Companies do not pay charity. They buy labor. If the local grocery store raises the price of milk, you don't pay it because the cow has more bills. You pay it because the milk has value. 

[VISUAL: Quick cut to graphic showing "Cost vs. Value"]
2:00 [2:00] Research generally suggests that negotiations fail when one party anchors the conversation on irrelevant personal metrics. Your grocery bill is irrelevant to your employer's profit margin. Your output is not.

[VISUAL: Text overlay on screen: "Chapter 2: Market Rate vs. Internal Equity"]
3:00 [3:00] Chapter two. Knowing your number. 

[VISUAL: Narrator holds up a blank sheet of paper, drops it.]
3:30 [3:30] Most people guess what they are worth. That is a terrible strategy. You need data from the actual market. Not glassdoor averages submitted by disgruntled interns. Actual data from people doing your job in your market.

[VISUAL: Lean forward, lower voice slightly.]
4:15 [4:15] If you don't know what a replacement costs the company, you have no leverage. The entire negotiation is just a polite argument about how much they like you. Liking you doesn't survive a budget cut. Replacement cost does.

[VISUAL: Text overlay on screen: "Chapter 3: The Script"]
5:00 [5:00] Here is the actual script. Stop memorizing aggressive negotiation tactics. They make you look weird and usually backfire.

[VISUAL: Bullet points appear one by one as spoken]
5:30 [5:30] Step one: Schedule a dedicated meeting. Do not ambush your boss in the hallway.
6:00 [6:00] Step two: Lay out your expanded scope since your last review. Use data. "Since taking over X, our error rate dropped by Y."
6:30 [6:30] Step three: Drop the ask and shut up. Say this: "Based on the market rate for these added responsibilities, I am looking to adjust my compensation to Z." Then stop talking. The person who speaks next loses.

[VISUAL: Narrator shakes head, mildly amused.]
7:20 [7:20] You will read online that you should always aim high, like asking for fifty percent more, so you can settle in the middle. That is internet negotiation fan fiction. If you ask for an absurd number without the market data to back it, you stop being a negotiator and start being a joke. Credibility is hard to rebuild once you spend it.

[VISUAL: Text overlay on screen: "Receipts"]
8:00 [8:00] Receipts. The evidence on negotiation anchoring comes out of behavioral economics literature, specifically regarding how initial numbers frame the entire interaction. The data is clear: irrelevant anchors drag the result toward failure.

[VISUAL: Narrator looks at camera, deadpan.]
9:00 [9:00] Here is your question for the comments: What is the worst piece of career advice you actually tried, and how badly did it go? Tell me below.

SOURCES:
- Negotiations fail when anchored on irrelevant personal metrics rather than market value:: 10.1016/j.obhdp.2004.08.003
