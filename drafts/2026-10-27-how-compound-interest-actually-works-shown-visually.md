# How compound interest actually works, shown visually

- **status:** NEEDS-REVIEW
- **drafted by:** gemini/gemini-3.8-flash
- **verified by:** groq/openai/gpt-oss-120b (openai-oss)
- **gate:** PASS
- **citations stripped:** 2 (10.1080/00207390802206775, 10.1037/0033-295X.99.2.336)
- **generated:** 2026-10-27

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
    "dois_found": 0,
    "verified": [],
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
      "claim": "Take a penny and double it every day for a month. By day twenty, you don't have much. By day thirty, you have over five million dollars.",
      "problem": "The final amount is incorrect. Starting with $0.01 and doubling 30 times yields about $10.7\u202fmillion, not \u201cover five million dollars.\u201d This misstates the mathematics.",
      "severity": "high"
    },
    {
      "claim": "People love to say that compound interest is the most powerful force in the universe, often attributing the quote to Einstein.",
      "problem": "The phrase \u201cmost powerful force in the universe\u201d is a hyperbolic overstatement, not a factual claim. It exaggerates the significance of compound interest beyond any empirical basis.",
      "severity": "medium"
    }
  ],
  "unverifiable": [
    "Everyone says compound interest is magic.",
    "The evidence for how people actually apply this in daily life is pretty messy, by the way."
  ],
  "overclaims": [
    "compound interest is the most powerful force in the universe"
  ],
  "advice_risk": "none",
  "confidence": "high",
  "verdict": "revise"
}
```

## Draft

TITLES:
1. The Compound Interest Trap
2. Why Linear Thinking Fails Us
3. The Math Behind Snowballing
4. The Visualization Problem
5. Understanding Exponential Growth

DESCRIPTION:
Compound interest gets called the eighth wonder of the world, but most people misunderstand how it actually moves over time. We're looking at the math and the visuals without the hype.

THE NUMBER:
72

SCRIPT:
0:00 [VISUAL: Close-up of a blank white sheet of paper]
Everyone says compound interest is magic. 

0:15 [VISUAL: Narrator looking directly at the camera, arms crossed]
It isn't magic. It's just multiplication that loops back on itself, and our brains are terrible at picturing it. 

0:30 [VISUAL: Split screen showing a straight diagonal line climbing slowly, next to a flat line that suddenly curves straight up]
Chapter one: The linear trap. 
We think in straight lines. 
If you walk ten steps, you expect to be ten steps away. 
We apply this to everything. 
We think progress should look like a ramp. 
It doesn't.

1:45 [VISUAL: Animation of a single penny doubling every day on a grid]
Chapter two: The bend. 
Take a penny and double it every day for a month. 
By day twenty, you don't have much. 
By day thirty, you have over five million dollars. 
The growth spends most of its time looking like nothing is happening. 
Then the curve hits.

3:30 [VISUAL: A graph where the Y-axis is unlabeled, just showing an exponential curve]
Chapter three: The rule of seventy-two. 
There's a quick mental shortcut economists use to estimate doubling time. 
You divide seventy-two by the interest rate. 
If you have a six percent return, it takes about twelve years to double. 
The evidence for how people actually apply this in daily life is pretty messy, by the way. 
Behavioral economics research generally suggests we undervalue future rewards compared to immediate ones. 
The math is simple. 
Our execution is terrible.

5:15 [VISUAL: A hand drawing compounding circles that get visibly larger with each loop]
Chapter four: The feedback loop. 
The core mechanism is just principal plus interest earning interest. 
It sounds boring because it is. 
It requires letting time do the work while you do nothing. 
That makes people restless. 
We want to tinker. 
Tinkering usually breaks the loop.

7:00 [VISUAL: Narrator leaning forward on the desk]
People love to say that compound interest is the most powerful force in the universe, often attributing the quote to Einstein. 
There is zero historical evidence Einstein ever said that. 
It's financial mythology used to sell newsletters and index funds. 
The math works fine without the fake historical endorsement. 

8:00 [VISUAL: Text on screen listing references]
Receipts. 
I didn't invent math. 
The rule of seventy-two is a standard algebraic approximation. 
Behavioral discounting is documented widely in decision theory literature. 

9:00 [VISUAL: Narrator looking at the camera]
Here is my question for you. 
If exponential growth is so obvious on paper, why do we consistently bail out right before the curve bends upward? 
Leave your thoughts in the comments.

