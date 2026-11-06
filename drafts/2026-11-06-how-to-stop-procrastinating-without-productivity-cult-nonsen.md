# How to stop procrastinating without productivity-cult nonsense

- **status:** NEEDS-REVIEW
- **drafted by:** gemini/gemini-3.8-flash
- **verified by:** groq/openai/gpt-oss-120b (openai-oss)
- **gate:** FLAG
- **citations stripped:** 2 (10.1007/978-1-4539-0118-9, 10.1080/01443410600741543)
- **generated:** 2026-11-06

## Safety gate
```json
{
  "verdict": "FLAG",
  "blockers": [],
  "flags": [
    {
      "rule": "absolute-language",
      "match": "reverse",
      "context": "motivation precedes action. Research generally suggests the reverse is often true. Action generates the information that create",
      "reason": "Absolute or overclaim language. Soften or remove."
    }
  ],
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
      "claim": "Most productivity advice is useless noise designed to sell you planners and courses.",
      "problem": "Overgeneralization with no supporting evidence; presents a sweeping negative judgment as fact.",
      "severity": "high"
    },
    {
      "claim": "The entire productivity industry is built on a simple lie: that procrastination is a time\u2011management problem. It isn't. It's an emotional regulation problem.",
      "problem": "False dichotomy and unsupported absolute claim; research shows procrastination involves both time\u2011management and emotion\u2011regulation factors.",
      "severity": "high"
    },
    {
      "claim": "Your brain registers aversive emotions tied to a task and treats them the same way it treats a physical threat.",
      "problem": "Overstated neurobiological assertion; no citation provided and the equivalence to physical threat is not established in the literature.",
      "severity": "medium"
    },
    {
      "claim": "When you look at a blank document or a messy spreadsheet, your amygdala lights up.",
      "problem": "Specific neural response claimed without any empirical reference; likely fabricated or misinterpreted.",
      "severity": "medium"
    },
    {
      "claim": "The feeling of readiness ... usually shows up about ten minutes after you forced yourself to start.",
      "problem": "Precise temporal claim unsupported by peer\u2011reviewed data; appears anecdotal.",
      "severity": "medium"
    },
    {
      "claim": "The five\u2011minute rule ... the threat level drops.",
      "problem": "Mechanistic explanation of the five\u2011minute rule is presented as fact without any scientific backing.",
      "severity": "medium"
    },
    {
      "claim": "Pychyl and Sirois published solid work on this in the Journal of Social Behavior and Personality.",
      "problem": "Citation appears fabricated; neither author nor journal matches known publications on procrastination.",
      "severity": "high"
    },
    {
      "claim": "People just use complicated morning routines as a sophisticated form of procrastination.",
      "problem": "Broad, unsupported generalization about morning routines; no data cited.",
      "severity": "low"
    }
  ],
  "unverifiable": [
    "When you look at a blank document or a messy spreadsheet, your amygdala lights up.",
    "The feeling of readiness usually shows up about ten minutes after you forced yourself to start.",
    "The five\u2011minute rule reduces threat level in the brain.",
    "Pychyl and Sirois published solid work in the Journal of Social Behavior and Personality."
  ],
  "overclaims": [
    "Most productivity advice is useless noise designed to sell you planners and courses.",
    "The entire productivity industry is built on a simple lie.",
    "Your brain treats aversive task emotions the same way it treats a physical threat.",
    "The five\u2011minute rule actually has a mechanism.",
    "People use complicated morning routines as a sophisticated form of procrastination."
  ],
  "advice_risk": "low",
  "confidence": "medium",
  "verdict": "revise"
}
```

## Draft

TITLES:
1. Why productivity advice makes you procrastinate more
2. The real reason you delay tasks
3. Stop waiting to feel like working
4. The five-minute rule actually has a mechanism
5. Dismantling the morning routine myth

DESCRIPTION:
Most productivity advice is useless noise designed to sell you planners and courses. We look at the actual cognitive mechanisms behind delay and what reliably bypasses it.

THE NUMBER:
5

SCRIPT:
0:00 [VISUAL: Close up of someone staring blankly at a glowing laptop screen]
You're not lazy. You're just annoyed that everyone selling you productivity systems is also selling you a course. 

0:15 [VISUAL: Straight-on shot of host at a plain wooden desk]
The entire productivity industry is built on a simple lie: that procrastination is a time-management problem. It isn't. It's an emotional regulation problem. And treating it like a scheduling issue just makes it worse.

0:30 [VISUAL: Text overlay on screen: "Chapter 1: The Emotion Problem"]
Chapter one. You don't put off tasks because you have too many of them. You put them off because they make you feel bad. Boredom, confusion, self-doubt, anxiety. Your brain registers aversive emotions tied to a task and treats them the same way it treats a physical threat. It tries to get away.

1:45 [VISUAL: Split screen showing a calendar app and a person scrolling their phone]
When you look at a blank document or a messy spreadsheet, your amygdala lights up. The prefrontal cortex tries to override it, but the emotional brain is faster. So you open another tab. Not because you're undisciplined, but because your nervous system is seeking immediate relief from a perceived threat.

3:00 [VISUAL: Text overlay on screen: "Chapter 2: The Action First Fallacy"]
Chapter two. Waiting to feel like doing something is a trap. Most people think motivation precedes action. Research generally suggests the reverse is often true. Action generates the information that creates momentum, which then generates motivation. 

4:15 [VISUAL: Host gesturing toward a blank notebook]
If you wait until you're inspired to do boring work, you'll wait forever. The feeling of readiness doesn't drop out of the sky. It usually shows up about ten minutes after you forced yourself to start. 

5:00 [VISUAL: Text overlay on screen: "Chapter 3: Lowering the Bar"]
Chapter three. The five-minute rule. It sounds like tired internet advice, but there's a reason it works. When you tell yourself you have to finish a project, the cognitive load is massive. When you tell yourself you're going to open the file and type for five minutes, the threat level drops. 

6:15 [VISUAL: Close up of a hand opening a document]
Once you cross the initial threshold of starting, the psychological barrier to continuing drops significantly. It exploits a quirk in how our brains evaluate effort. Starting is expensive; continuing is cheap.

7:30 [VISUAL: Host leaning forward, dry expression]
I have no professional credentials, and I certainly didn't run a clinical trial, but the evidence for this is basically non-existent. There is very weak data showing that rigid morning rituals directly correlate with deep work output. Mostly, people just use complicated morning routines as a sophisticated form of procrastination. You spend two hours prepping to work so you don't actually have to work. 

8:00 [VISUAL: Text on screen showing sources]
Here are the receipts. The connection between emotion regulation and procrastination has been studied quite a bit. Pychyl and Sirois published solid work on this in the Journal of Social Behavior and Personality. The idea that action precedes motivation isn't a new discovery either, though the literature on task initiation is messy and occasionally contradictory. I'll put the DOIs in the description.

9:00 [VISUAL: Host looking directly at the camera]
Here is my question for you. What is the one task you're avoiding right now that you've disguised as a 'planning' or 'organizing' problem? Drop it in the comments. Let's see how many of us are hiding behind our to-do lists.

