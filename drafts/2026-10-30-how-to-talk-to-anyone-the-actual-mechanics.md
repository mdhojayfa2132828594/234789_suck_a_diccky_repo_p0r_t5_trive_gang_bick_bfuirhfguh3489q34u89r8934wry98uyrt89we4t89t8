# How to talk to anyone: the actual mechanics

- **status:** NEEDS-REVIEW
- **drafted by:** gemini/gemini-3.8-flash
- **verified by:** groq/openai/gpt-oss-120b (openai-oss)
- **gate:** PASS
- **citations stripped:** 1 (10.1037/psap0000157)
- **generated:** 2026-10-30

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
    "dois_found": 1,
    "verified": [
      "10.1037/h0026102"
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
      "claim": "Everyone hates small talk because it's boring.",
      "problem": "Absolute claim with no empirical support; ignores cultural and individual variation.",
      "severity": "high"
    },
    {
      "claim": "If you skip it, you just seem aggressive.",
      "problem": "Overgeneralization; no citation showing that omitting small talk universally signals aggression.",
      "severity": "medium"
    },
    {
      "claim": "People who ask more follow-up questions are consistently rated as more engaging.",
      "problem": "Unsupported superlative; the cited literature is absent and the statement exaggerates findings.",
      "severity": "medium"
    },
    {
      "claim": "The main reason people suck at talking to strangers is that they're thinking about themselves.",
      "problem": "Broad, unsubstantiated causal claim; no data provided to back it up.",
      "severity": "high"
    },
    {
      "claim": "When your internal monologue is running that loud, you aren't having a conversation. You're just waiting for your turn to perform.",
      "problem": "Subjective assertion presented as fact; lacks scientific evidence.",
      "severity": "medium"
    },
    {
      "claim": "Today's target: The idea that 93 percent of communication is nonverbal.",
      "problem": "Misinterpretation of Mehrabian's 7\u201138\u201155 rule, which applies only to specific affective communication, not to all interactions.",
      "severity": "high"
    },
    {
      "claim": "The evidence is garbage, but it sounds scientific, so people repeat it.",
      "problem": "Pejorative language and blanket dismissal of a body of research without nuanced critique; not an accurate representation of the literature.",
      "severity": "medium"
    },
    {
      "claim": "Most social advice is just weird manipulation tactics that make you look like a lizard person.",
      "problem": "Hyperbolic, unverified claim; no data supporting the prevalence or effect described.",
      "severity": "medium"
    },
    {
      "claim": "Research generally suggests that people use these superficial exchanges to check for safety before they commit cognitive effort to a real conversation.",
      "problem": "Vague attribution to 'research' without any citation; the mechanism is speculative.",
      "severity": "medium"
    }
  ],
  "unverifiable": [
    "Everyone hates small talk because it's boring.",
    "If you skip it, you just seem aggressive.",
    "People who ask more follow-up questions are consistently rated as more engaging.",
    "The main reason people suck at talking to strangers is that they're thinking about themselves.",
    "When your internal monologue is running that loud, you aren't having a conversation.",
    "Most social advice is just weird manipulation tactics that make you look like a lizard person.",
    "Research generally suggests that people use these superficial exchanges to check for safety before they commit cognitive effort to a real conversation."
  ],
  "overclaims": [
    "Everyone hates small talk because it's boring.",
    "If you skip it, you just seem aggressive.",
    "People who ask more follow-up questions are consistently rated as more engaging.",
    "The main reason people suck at talking to strangers is that they're thinking about themselves.",
    "When your internal monologue is running that loud, you aren't having a conversation.",
    "Today's target: The idea that 93 percent of communication is nonverbal.",
    "Most social advice is just weird manipulation tactics that make you look like a lizard person."
  ],
  "advice_risk": "low",
  "confidence": "high",
  "verdict": "revise"
}
```

## Draft

TITLES:
1. The "How to Talk to Anyone" Delusion
2. Why Small Talk Actually Sucks
3. The Mechanics of a Real Conversation
4. Asking Better Questions
5. The End of Charisma

DESCRIPTION:
Most advice on talking to people relies on fake charm and memorized tricks that don't work. Here is a look at what actually drives human interaction based on what researchers have managed to measure.

THE NUMBER:
3

SCRIPT:
[VISUAL: Close-up on the host sitting at a plain wooden desk, looking straight at the camera.]
0:00 You’ve probably read articles telling you to mirror body language or use someone's name three times in a sentence to make them like you. 

[VISUAL: The host leans back slightly, expression flat.]
0:15 Most social advice is just weird manipulation tactics that make you look like a lizard person. Let's look at what actually happens when two people talk.

[VISUAL: Text overlay on screen: Chapter 1: The Small Talk Trap]
0:30 Everyone hates small talk because it's boring. But it's actually a low-risk sorting mechanism. 

[VISUAL: Cut to a graphic showing two stick figures waving at each other.]
0:45 Research generally suggests that people use these superficial exchanges to check for safety before they commit cognitive effort to a real conversation. If you skip it, you just seem aggressive.

[VISUAL: Text overlay on screen: Chapter 2: The Question Ratio]
1:30 You don't need to be fascinating. You just need to be interested, which is annoying because it requires actual attention.

[VISUAL: Host holds up a small notebook.]
2:15 Studies on conversation dynamics have looked at how question-asking correlates with likability. People who ask more follow-up questions are consistently rated as more engaging. Not because they said something clever, but because they let the other person keep talking.

[VISUAL: Text overlay on screen: Chapter 3: Cognitive Load]
4:00 The main reason people suck at talking to strangers is that they're thinking about themselves. 

[VISUAL: Host taps the side of their head.]
4:45 You're worried about how your voice sounds, whether your shirt looks fine, and what you're going to say next. That leaves zero brain power to actually process what the other person is saying. 

[VISUAL: Cut to B-roll of static on an old television screen.]
5:30 When your internal monologue is running that loud, you aren't having a conversation. You're just waiting for your turn to perform.

[VISUAL: Host leans forward, elbows on the desk.]
7:15 Today's target: The idea that 93 percent of communication is nonverbal. You've heard this quoted everywhere. Albert Mehrabian's old studies on tone and body language. 

[VISUAL: Host shakes head slowly.]
7:30 Except Mehrabian was looking at a very specific, narrow context where people were expressing feelings of liking or disliking with single words. It had nothing to do with normal conversation. Yet entire seminar industries were built on applying it to business meetings and dates. The evidence is garbage, but it sounds scientific, so people repeat it.

[VISUAL: Text overlay on screen: Receipts]
8:00 Let's look at the actual receipts. 

[VISUAL: Full screen graphic of source texts with DOIs visible.]

[VISUAL: Host returns to frame.]
8:45 I am not an expert. I just read the papers so you don't have to.

[VISUAL: Host looks directly down the lens.]
9:00 Here is my question for you: what is the one social rule you refuse to follow because you think it's completely stupid? Leave it in the comments.

SOURCES:
- Nonverbal communication percentages are frequently misapplied from narrow context studies:: 10.1037/h0026102
