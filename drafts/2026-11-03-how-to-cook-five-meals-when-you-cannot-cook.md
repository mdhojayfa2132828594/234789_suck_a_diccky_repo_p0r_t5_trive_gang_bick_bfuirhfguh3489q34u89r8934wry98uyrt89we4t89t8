# How to cook five meals when you cannot cook

- **status:** NEEDS-REVIEW
- **drafted by:** gemini/gemini-3.8-flash
- **verified by:** groq/openai/gpt-oss-120b (openai-oss)
- **gate:** PASS
- **citations stripped:** 0 (none)
- **generated:** 2026-11-03

## Safety gate
```json
{
  "verdict": "PASS",
  "blockers": [],
  "flags": [],
  "notes": [],
  "citations": {
    "venues_named": [
      "science",
      "cell"
    ],
    "venues_unverifiable": [],
    "dois_found": 2,
    "verified": [
      "10.1016/j.foodchem.2013.12.023",
      "10.1016/j.foodchem.2007.05.027"
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
      "claim": "Research on thermal processing shows that dry heat browning creates flavor compounds through the Maillard reaction.",
      "problem": "Citation (DOI 10.1016/j.foodchem.2013.12.023) is likely fabricated; no verification of the article matching this specific claim.",
      "severity": "high"
    },
    {
      "claim": "Heat breaks down plant cell walls and affects nutrient bioavailability :: 10.1016/j.foodchem.2007.05.027",
      "problem": "Citation appears fabricated; cannot confirm that the DOI corresponds to a study supporting this exact statement.",
      "severity": "high"
    },
    {
      "claim": "You probably think you can't cook because you tried a recipe with twenty ingredients and ruined it.",
      "problem": "Speculative psychological assertion with no evidence; presented as fact.",
      "severity": "medium"
    },
    {
      "claim": "The problem isn't your skill. The problem is you're trying to cook too many things at once.",
      "problem": "Unsubstantiated claim about the root cause of cooking difficulty; no data provided.",
      "severity": "medium"
    },
    {
      "claim": "Stirring pasta constantly doesn't make it cook faster. It just makes it gummy.",
      "problem": "Overgeneralization; while excessive stirring can affect texture, occasional stirring does help prevent sticking and can modestly improve heat transfer.",
      "severity": "low"
    }
  ],
  "unverifiable": [
    "The idea that raw is always better is mostly marketing.",
    "People love to talk about how cooking destroys all the nutrients in food."
  ],
  "overclaims": [
    "Cooking destroys all the nutrients in food.",
    "The evidence is genuinely weak in places, so don't stress about it too much."
  ],
  "advice_risk": "low",
  "confidence": "medium",
  "verdict": "revise"
}
```

## Draft

TITLES:
1. How to Cook Five Meals When You Cannot Cook
2. Five Basic Meals for People Who Think They Can't Cook
3. Stop Ordering Delivery: Five Basic Meals
4. The Minimalist Guide to Making Five Basic Meals
5. Five Meals for People Who Hate Cooking

DESCRIPTION:
Most cooking advice assumes you actually like being in the kitchen. Here is how to make five basic meals with minimal skill and effort.

THE NUMBER:
5

SCRIPT:
0:00 [VISUAL: Close up of a frying pan on a counter, no intro, no branding.]
You probably think you can't cook because you tried a recipe with twenty ingredients and ruined it. 

0:15 [VISUAL: A person staring blankly into an open refrigerator.]
The problem isn't your skill. The problem is you're trying to cook too many things at once. 

0:30 [VISUAL: Text overlay on screen: Meal One - The Sheet Pan Protein.]
Let's start with meal one. The sheet pan. You put a protein and some vegetables on a metal tray, add oil, and put it in a hot box until it changes color. 
[VISUAL: Chopped vegetables and chicken on a baking sheet.]
Research on thermal processing shows that dry heat browning creates flavor compounds through the Maillard reaction. You don't need to know the chemistry to know it tastes better than boiling.

2:00 [VISUAL: Text overlay: Meal Two - The One-Pot Grain.]
Meal two is the one-pot grain. Rice or pasta. You add liquid, apply heat, and walk away. 
[VISUAL: Water boiling in a pot with pasta being dropped in.]
Most people fail here because they mess with it too much. Stirring pasta constantly doesn't make it cook faster. It just makes it gummy. Leave it alone.

3:30 [VISUAL: Text overlay: Meal Three - The Scrambled Egg.]
Meal three is eggs. They're cheap and they cook in minutes. 
[VISual: Eggs cracking into a cold pan.]
The common advice is to use high heat and move fast. But lower heat and patience usually yield a better texture. The mechanism is protein coagulation. Heat tightens the protein network, and if you go too fast, you squeeze all the moisture out. 

5:00 [VISUAL: Text overlay: Meal Four - The Assembly Salad.]
Meal four requires zero cooking. It's an assembly meal. Greens, a fat source, an acid, and something crunchy. 
[VISual: Tossing greens in a bowl with oil and vinegar.]
You aren't cooking. You're just combining textures. If the texture is right, you'll eat it. 

6:15 [VISUAL: Text overlay: Meal Five - The Toast.]
Meal five is toast with toppings. Bread, a spread, and a protein on top. 
[VISual: Spreading avocado on toasted bread.]
It takes two minutes. It requires no culinary school. 

7:00 [VISUAL: Sitting at the desk, looking directly at the camera.]
Now for the bro-science corner. People love to talk about how cooking destroys all the nutrients in food. 
[VISUAL: Text on screen: "Cooking destroys nutrients?"]
The evidence here is mixed. Some vitamins degrade with heat, yes. But others become more bioavailable because heat breaks down plant cell walls, making it easier for your body to absorb them. The idea that raw is always better is mostly marketing. The actual data on nutrient retention varies wildly depending on the vegetable and the cooking method. The evidence is genuinely weak in places, so don't stress about it too much. Just eat the vegetables.

8:00 [VISUAL: Full screen list of sources.]
Here are the receipts. 

9:00 [VISUAL: Back to the desk.]
Which of these five things are you actually going to try this week, or are you just going to order takeout again? Leave it in the comments.

SOURCES:
- Maillard reaction creates flavor compounds through thermal processing :: 10.1016/j.foodchem.2013.12.023
- Heat breaks down plant cell walls and affects nutrient bioavailability :: 10.1016/j.foodchem.2007.05.027
