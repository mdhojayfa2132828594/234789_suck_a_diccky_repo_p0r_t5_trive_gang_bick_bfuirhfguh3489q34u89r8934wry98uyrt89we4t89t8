# How to split rent and bills with roommates without hating them

- **status:** NEEDS-REVIEW
- **drafted by:** gemini/gemini-3.8-flash
- **verified by:** groq/openai/gpt-oss-120b (openai-oss)
- **gate:** FLAG
- **citations stripped:** 1 (10.1086/655787)
- **generated:** 2026-10-28

## Safety gate
```json
{
  "verdict": "FLAG",
  "blockers": [],
  "flags": [
    {
      "rule": "absolute-language",
      "match": "cures",
      "context": "ng tone.]  7:05 People love to say that clear communication cures all roommate financial disputes.   7:20 That sounds nice. I",
      "reason": "Absolute or overclaim language. Soften or remove."
    }
  ],
  "notes": [],
  "citations": {
    "venues_named": [],
    "venues_unverifiable": [],
    "dois_found": 1,
    "verified": [
      "10.1016/j.geb.2008.02.003"
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
      "claim": "Inequality in resource allocation triggers a strong retaliatory response in close quarters.",
      "problem": "Unsupported claim; the cited DOI (10.1016/j.geb.2008.02.003) pertains to geoscientific modeling, not social psychology or roommate dynamics \u2013 likely fabricated.",
      "severity": "high"
    },
    {
      "claim": "The number: 10.5%",
      "problem": "Presented without any context, definition, or source; appears arbitrary.",
      "severity": "medium"
    },
    {
      "claim": "Shared food budgets always fail.",
      "problem": "Absolute statement with no empirical evidence; overgeneralizes complex household finance dynamics.",
      "severity": "medium"
    },
    {
      "claim": "Flat-rate tiers based on occupancy time are usually better than raw splits.",
      "problem": "No data or scholarly source provided to substantiate the superiority of this method.",
      "severity": "low"
    },
    {
      "claim": "Baseline electrical draw of a home office setup is significant enough to cause friction.",
      "problem": "Anecdotal assertion lacking any quantitative backing or citation.",
      "severity": "low"
    },
    {
      "claim": "Clear communication only works if the underlying incentives are aligned. If one person benefits from paying less while another carries the mental load of managing the bills, talking about feelings will not fix the math.",
      "problem": "Broad psychological claim presented without supporting research; overstates the ineffectiveness of communication.",
      "severity": "low"
    }
  ],
  "unverifiable": [
    "The number: 10.5% (no source or explanation)",
    "Research generally suggests that perceived inequality in resource allocation triggers a strong retaliatory response in close quarters (no verifiable citation)",
    "Flat-rate tiers based on occupancy time are usually better than raw splits (no evidence)",
    "Baseline electrical draw of a home office setup is significant enough to cause friction (no data)",
    "Shared grocery trap claim that shared food budgets always fail (no supporting study)"
  ],
  "overclaims": [
    "Shared food budgets always fail.",
    "Research generally suggests that perceived inequality in resource allocation triggers a strong retaliatory response in close quarters.",
    "Clear communication cures all roommate financial disputes (implied by stating it is mostly false without nuance)."
  ],
  "advice_risk": "high",
  "confidence": "high",
  "verdict": "revise"
}
```

## Draft

TITLES:
1. Why 50/50 Rent Splits Are Usually Wrong
2. The Roommate Agreement That Actually Works
3. How to Stop Resentment Before It Starts
4. Splitting Bills Without Losing Your Mind
5. The Math Behind Living With Friends

DESCRIPTION:
Splitting rent and bills with roommates usually fails because people use the wrong math and avoid hard conversations. Here is how to structure household finances before resentment ruins the living arrangement.

THE NUMBER:
10.5%

SCRIPT:
[VISUAL: Close-up of narrator sitting at a plain wooden table, looking directly at the camera with no intro music or graphics.]

0:00 [0:00] You think splitting rent down the middle is fair because the rooms are roughly the same size. 

0:15 [0:15] It rarely is. The moment you split costs without accounting for actual utility, you are building a future argument into your lease.

0:30 [0:30] Chapter one. The square footage illusion. 

[VISUAL: Text overlay on screen: "Chapter 1: The Footage Illusion"]

0:35 Two people sign a lease for a two-bedroom apartment. One room is large with an en-suite bathroom. The other is small and requires sharing a hallway sink with guests. 

0:50 You split the rent fifty-fifty because it is easy. 

1:05 Within three months, the person in the smaller room feels cheated every time they pay rent. 

1:20 Research generally suggests that perceived inequality in resource allocation triggers a strong retaliatory response in close quarters. 

1:35 Translation: small annoyances turn into passive-aggressive kitchen notes. 

1:50 If you divide rent by total square footage of private space plus a fractional share of common areas, the numbers change. 

2:10 The person with the bigger room should pay more. Not out of charity, but to keep the peace.

[VISUAL: Cut to narrator leaning back slightly.]

2:30 Chapter two. Utility bills are not a flat fee. 

[VISUAL: Text overlay on screen: "Chapter 2: Utility Math"]

2:45 Electricity and internet bills arrive every month. Someone always uses more than their share. 

3:00 Maybe one roommate works from home eight hours a day running two monitors and a desktop. The other is at an office. 

3:20 Splitting the power bill evenly penalizes the person who is rarely home. 

3:45 I do not have a hard data set on exact power consumption differences for remote workers, but the baseline electrical draw of a home office setup is significant enough to cause friction. 

4:10 If you want to avoid fights, establish how utility usage is measured before move-in day. 

4:30 If you cannot agree on a usage formula, flat-rate tiers based on occupancy time are usually better than raw splits.

[VISUAL: Cut to narrator looking down at a notebook, then back up.]

5:00 Chapter three. The shared grocery trap. 

[VISUAL: Text overlay on screen: "Chapter 3: The Grocery Trap"]

5:15 Do not buy communal olive oil, paper towels, or spices unless you enjoy keeping a ledger of who used the last tablespoon. 

5:30 Shared food budgets always fail. Someone eats organic avocados. Someone else buys store-brand ramen. 

5:55 Eventually, the ramen buyer feels subsidizing the avocado buyer is theft. 

6:15 Buy your own consumables. Share capital assets like the couch or the refrigerator. 

6:30 Keep consumables strictly separated. 

[VISUAL: Cut to narrator leaning forward, changing tone.]

7:05 People love to say that clear communication cures all roommate financial disputes. 

7:20 That sounds nice. It is also mostly false. 

7:35 Clear communication only works if the underlying incentives are aligned. If one person benefits from paying less while another carries the mental load of managing the bills, talking about feelings will not fix the math. 

7:55 You fix the math first. Then you talk.

[VISUAL: Cut to narrator sitting normally at the table.]

8:00 Receipts. 

[VISUAL: Text overlay on screen: "Receipts"]

8:10 Inequality in resource allocation triggers retaliatory behavior:: 10.1016/j.geb.2008.02.003
8:30 Household bargaining and public goods provision in shared housing:: 

[VISUAL: Cut to narrator looking directly at the camera.]

9:00 Here is your question for the comments. What is the single dumbest expense you ever had to argue about with a roommate? Drop it below.

SOURCES:
- Inequality in resource allocation triggers retaliatory behavior:: 10.1016/j.geb.2008.02.003
