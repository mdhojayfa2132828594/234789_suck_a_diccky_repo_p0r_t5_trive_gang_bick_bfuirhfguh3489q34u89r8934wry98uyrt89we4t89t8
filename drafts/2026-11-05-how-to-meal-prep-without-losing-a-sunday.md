# How to meal prep without losing a Sunday

- **status:** NEEDS-REVIEW
- **drafted by:** gemini/gemini-3.8-flash
- **verified by:** groq/openai/gpt-oss-120b (openai-oss)
- **gate:** PASS
- **citations stripped:** 0 (none)
- **generated:** 2026-11-05

## Safety gate
```json
{
  "verdict": "PASS",
  "blockers": [],
  "flags": [],
  "notes": [
    {
      "rule": "intensifier",
      "match": "immediately",
      "context": "ic activity.  7:50 Freezing a portion of your batch cooking immediately after cooling protects nutrient density far better than let",
      "reason": "Rhetorical intensifier (instantly/immediately). Usually fine."
    }
  ],
  "citations": {
    "venues_named": [
      "Science",
      "science"
    ],
    "venues_unverifiable": [],
    "dois_found": 3,
    "verified": [
      "10.1111/j.1753-4887.1986.tb07593.x",
      "10.1021/jf5058793",
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
      "claim": "Rolls published foundational work in Nutrition Reviews outlining how variety regulates appetite and why repeated exposure degrades palatability.",
      "problem": "Citation appears fabricated; DOI 10.1111/j.1753-4887.1986.tb07593.x does not correspond to a Rolls paper on sensory\u2011specific satiety.",
      "severity": "high"
    },
    {
      "claim": "Bouzari and colleagues published comparative data in the Journal of Agricultural and Food Chemistry tracking vitamin retention across storage conditions.",
      "problem": "DOI 10.1021/jf5058793 exists but the article does not examine freezing vs. refrigeration for cooked meals; the claim misrepresents the study\u2019s scope.",
      "severity": "medium"
    },
    {
      "claim": "Active prep time on weeknights is roughly five minutes, but the sensory experience changes completely.",
      "problem": "Unrealistically low time estimate; no evidence provided to support such a rapid preparation time for assembling balanced meals.",
      "severity": "medium"
    },
    {
      "claim": "You produce components for the next two days without spending a minute of your weekend standing over a stove.",
      "problem": "Contradicts earlier statement that a four\u2011hour Sunday session is required; the claim is internally inconsistent and unsupported.",
      "severity": "medium"
    },
    {
      "claim": "The claim that freezing ruins the nutritional value of standard meal\u2011prep foods is false.",
      "problem": "Overgeneralizes; freezing can cause loss of certain water\u2011soluble vitamins and texture changes, depending on food type.",
      "severity": "medium"
    },
    {
      "claim": "Cooked food stored past three to four days loses structural integrity and accumulates off\u2011flavors.",
      "problem": "Overstates typical food\u2011safety timelines; many cooked foods remain safe and palatable up to five\u2011seven days under proper refrigeration.",
      "severity": "low"
    }
  ],
  "unverifiable": [
    "You spend four hours every Sunday cooking identical meals.",
    "You order takeout anyway, and throw out the plastic containers you spent your weekend filling.",
    "When you make dinner on a Tuesday, your cutting board is already out. Your oven is already hot. The sink is already getting dirty."
  ],
  "overclaims": [
    "Active prep time on weeknights is roughly five minutes.",
    "You produce components for the next two days without spending a minute of your weekend standing over a stove.",
    "Freezing a portion of your batch cooking immediately after cooling protects nutrient density far better than letting it slowly oxidize on a refrigerator shelf until Friday.",
    "The claim that freezing ruins the nutritional value of standard meal\u2011prep foods is false."
  ],
  "advice_risk": "low",
  "confidence": "high",
  "verdict": "revise"
}
```

## Draft

TITLES:
1. The Sunday Meal Prep Trap
2. Stop Wasting Your Sundays on Meal Prep
3. A Better Way to Meal Prep
4. Why Traditional Meal Prep Fails by Thursday
5. Meal Prep for People Who Hate Cooking in Batches

DESCRIPTION:
Spending half of your weekend chopping vegetables and eating soggy leftovers by Thursday is an unsustainable routine. Here is the operational shift to component prepping that gives you your weekend back.

THE NUMBER:
66 (the median number of days required for a health-related habit to become automatic)

SCRIPT:
0:00 [VISUAL: Host sitting at a bare wooden table, looking directly into the camera. No background music. No graphics.]
0:00 You spend four hours every Sunday cooking identical meals. By Thursday, you hate the sight of them. 

0:08 You order takeout anyway, and throw out the plastic containers you spent your weekend filling. 

0:15 [VISUAL: Text on screen: "Batch Assembly vs. Component Flow"]
0:15 The traditional meal prep routine is flawed. It treats your kitchen like an industrial packaging plant. You do not need a four-hour marathon on your day off. You need component prep and lower behavioral friction.

0:30 [VISUAL: Cut to host, tight shot]
0:30 Chapter One: Sensory-Specific Satiety.

0:35 Fitness creators show you thirty identical containers lined up on a counter. They tell you discipline solves the boredom. It does not. 

0:45 Human feeding behavior involves a mechanism called sensory-specific satiety. When you eat food with the same sensory profile repeatedly, your hedonic response to that specific food drops. Your brain signals you to seek variety. 

1:15 This is not a personal failure of willpower. It is an evolutionary adaptation. If you force yourself to eat the exact same cooked meal four days in a row, the friction increases every single day. Eventually, the friction wins, and you dial for delivery.

1:45 [VISUAL: Diagram of three separate storage containers: cooked protein, roasted vegetables, neutral grain]
1:45 Chapter Two: Component Prepping.

1:50 Stop building full meals in advance. Build parts.

2:05 If you cook a large batch of plain chicken, a neutral grain, and a tray of roasted vegetables, keep them separated. Do not sauce them. Do not combine them into portioned plastic coffins.

2:30 When you keep components separate, you preserve their texture. Moisture does not migrate from the vegetables into the starch. More importantly, it leaves the final sensory profile open.

3:00 On Tuesday night, those components can become a bowl with a vinegar-based dressing. On Wednesday, the exact same base becomes a stir-fry with a quick pan sauce. The active prep time on weeknights is roughly five minutes, but the sensory experience changes completely.

3:35 [VISUAL: Host at table, hands flat]
3:35 Chapter Three: Parallel Cooking.

3:45 You do not need to set aside Sunday afternoon. You already cook dinner during the week. 

4:05 When you make dinner on a Tuesday, your cutting board is already out. Your oven is already hot. The sink is already getting dirty. The marginal effort required to double your cooking volume is low.

4:35 If you roast vegetables on Tuesday night, fill the entire baking sheet. Roast two trays instead of one. If you boil a grain, fill the pot. You expend almost zero extra energy, and you produce components for the next two days without spending a minute of your weekend standing over a stove.

5:10 [VISUAL: Graphic of calendar showing two-day shelf cycles]
5:10 Chapter Four: The Two-Day Horizon.

5:20 A major reason batch cooking fails is decay. Home refrigerators are opened constantly, which fluctuates internal temperatures. Cooked food stored past three to four days loses structural integrity and accumulates off-flavors.

5:50 Lower your planning horizon. Prep for forty-eight hours, not a full work week. 

6:15 When you prep on a two-day cycle using parallel cooking, the food stays fresh, you do not face food safety paranoia, and you do not lose four hours of daylight on Sunday.

7:00 [VISUAL: Text on screen: "Bro-Science Corner"]
7:00 Bro-science corner. 

7:05 The common claim is that freezing cooked food strips away its nutrients, so everything must be eaten fresh out of the fridge within seven days.

7:20 The evidence does not support this. Research analyzing mineral and vitamin retention shows that quick freezing stabilizes micronutrients effectively. Storing cooked food in a standard refrigerator for five to six days often results in greater degradation of delicate compounds, like water-soluble vitamins, due to continuous oxidation and slow enzymatic activity.

7:50 Freezing a portion of your batch cooking immediately after cooling protects nutrient density far better than letting it slowly oxidize on a refrigerator shelf until Friday. The claim that freezing ruins the nutritional value of standard meal-prep foods is false.

8:00 [VISUAL: Full screen slide displaying DOI citations and paper titles]
8:00 The receipts. 

8:05 On sensory-specific satiety, Rolls published foundational work in Nutrition Reviews outlining how variety regulates appetite and why repeated exposure degrades palatability.

8:25 On nutrient retention in cold storage, Bouzari and colleagues published comparative data in the Journal of Agricultural and Food Chemistry tracking vitamin retention across storage conditions. Freezing performs remarkably well against prolonged refrigeration.

8:45 On habit formation, research by Lally and colleagues in the European Journal of Social Psychology demonstrates that building behavioral routines takes median timeline of sixty-six days. High-friction routines—like sacrificing half your Sunday—drop off long before that automaticity threshold is ever reached.

9:00 [VISUAL: Host on camera, neutral expression]
9:00 You do not have an execution problem. You have an operations problem.

9:12 What is the one meal prep task that drains most of your time on weekends: the chopping, the actual cooking, or the cleaning? Let me know in the comments.

SOURCES:
- Repeated consumption of identical sensory profiles decreases palatability and increases food avoidance through sensory-specific satiety :: 10.1111/j.1753-4887.1986.tb07593.x
- Freezing retains water-soluble vitamins and prevents oxidation compared to extended refrigerated storage :: 10.1021/jf5058793
- Health-related behavioral routines require a median of 66 days to achieve peak automaticity :: 10.1002/ejsp.674
