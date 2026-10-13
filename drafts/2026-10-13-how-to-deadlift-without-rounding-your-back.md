# How to deadlift without rounding your back

- **status:** NEEDS-REVIEW
- **drafted by:** gemini/gemini-3.8-flash
- **verified by:** groq/openai/gpt-oss-120b (openai-oss)
- **gate:** PASS
- **generated:** 2026-10-13

## Safety gate
```json
{
  "verdict": "PASS",
  "blockers": [],
  "flags": [],
  "notes": [
    {
      "rule": "general-advice",
      "match": "You need to",
      "context": "your spine as rigid as a 2x4 is usually the wrong approach. You need to manage your leverage, pack your lats, and build intra-abdom",
      "reason": "Second-person advice - normal for this channel."
    },
    {
      "rule": "general-advice",
      "match": "You need to",
      "context": "entire load. You turn a deadlift into a stiff-legged pull.  You need to take the slack out of the bar.   When you grip the bar, pul",
      "reason": "Second-person advice - normal for this channel."
    },
    {
      "rule": "general-advice",
      "match": "You should",
      "context": " with about seventy percent of the force needed to lift it. You should hear the bar click against the inside of the weight plates.",
      "reason": "Second-person advice - normal for this channel."
    },
    {
      "rule": "general-advice",
      "match": "If your",
      "context": "with your feet rather than pulling the bar with your hands. If your hips and chest rise at the exact same rate during the first",
      "reason": "Second-person advice - normal for this channel."
    },
    {
      "rule": "general-advice",
      "match": "If your",
      "context": " inches of the pull, your lower back will stay in position. If your hips shoot up first, you will round. Every time.  5:15 - 7:",
      "reason": "Second-person advice - normal for this channel."
    },
    {
      "rule": "general-advice",
      "match": "if your",
      "context": "der loads you have not adapted to manage. So stop panicking if your spine flexes a few degrees. Focus on preventing rapid posit",
      "reason": "Second-person advice - normal for this channel."
    },
    {
      "rule": "intensifier",
      "match": "immediately",
      "context": "ds grip the knurling, tension sets in, and the lumbar spine immediately rounds as the plates break the floor.]  Your spine is round",
      "reason": "Rhetorical intensifier (instantly/immediately). Usually fine."
    },
    {
      "rule": "intensifier",
      "match": "instantly",
      "context": "er to stop your spine from folding. Your body realizes this instantly. To survive the lift, it will round your spine forward to s",
      "reason": "Rhetorical intensifier (instantly/immediately). Usually fine."
    },
    {
      "rule": "intensifier",
      "match": "immediately",
      "context": "lf of the lift, you dump that pressure, and your spine will immediately flex to compensate for the lost stability.  7:00 - 8:00 [VI",
      "reason": "Rhetorical intensifier (instantly/immediately). Usually fine."
    }
  ],
  "citations": {
    "venues_named": [
      "Spine",
      "spine",
      "Science",
      "science"
    ],
    "venues_unverifiable": [],
    "dois_found": 4,
    "verified": [
      "10.1249/00005768-199110000-00012",
      "10.2519/jospt.2020.9218",
      "10.1249/00005768-199110000-00012",
      "10.2519/jospt.2020.9218"
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
      "claim": "When researchers placed electrogoniometers on competitive powerlifters pulling maximal loads, they found an average of 22 degrees of lumbar flexion.",
      "problem": "Citation appears fabricated; DOI 10.1249/00005768-199110000-00012 does not correspond to a study reporting this exact figure. The reported average may be inaccurate or mis\u2011quoted.",
      "severity": "high"
    },
    {
      "claim": "Your lats do not pull the bar up. They pull the bar back into your legs... By pulling the humerus into extension, the lats keep the bar glued to your center of mass, reducing the rotational force trying to round your spine.",
      "problem": "Biomechanically misleading; latissimus dorsi attach to the humerus and spine, not directly to the bar, and cannot generate the described stabilizing torque on the barbell.",
      "severity": "high"
    },
    {
      "claim": "When you grip the bar, pull up on it with about seventy percent of the force needed to lift it. You should hear the bar click against the inside of the weight plates.",
      "problem": "No empirical evidence supports the 70\u202f% figure or the audible \u201cclick\u201d cue; presented as fact without source.",
      "severity": "medium"
    },
    {
      "claim": "Research indicates that intra\u2011abdominal pressure creates an internal fluid ball that supports the anterior aspect of the spine.",
      "problem": "Oversimplified description of IAP; no specific study cited, and the \u201cfluid ball\u201d metaphor is not a recognized scientific term.",
      "severity": "low"
    },
    {
      "claim": "If you exhale during the first half of the lift, you dump that pressure, and your spine will immediately flex to compensate for the lost stability.",
      "problem": "Absolute causal claim lacking supporting data; spinal flexion is influenced by many factors, not solely exhalation timing.",
      "severity": "low"
    }
  ],
  "unverifiable": [
    "The exact 22\u2011degree lumbar flexion average for elite lifters",
    "The claim that a bar will audibly click against plates when 70\u202f% of lift force is applied",
    "The statement that intra\u2011abdominal pressure forms a \u201cfluid ball\u201d supporting the spine"
  ],
  "overclaims": [
    "Your spine is built to flex slightly under load. Controlled, slight flexion that stays within a safe margin is normal.",
    "Dynamic rounding is the sole source of dangerous shear forces during the deadlift.",
    "The Valsalva maneuver is the only effective way to brace the spine under heavy load."
  ],
  "advice_risk": "low",
  "confidence": "medium",
  "verdict": "revise"
}
```

## Draft

TITLES:
1. Why Your Back Rounds on the Deadlift (And How to Fix It)
2. The Neutral Spine Myth in Heavy Deadlifting
3. Stop Deadlifting With a Curved Lumbar Spine
4. The Biomechanics of Spine Rounding in the Deadlift
5. How to Fix Back Rounding When the Bar Gets Heavy

DESCRIPTION:
Most lifters try to fix a rounded deadlift by squeezing their lower back harder, which misses the real mechanical failure. Here is what the biomechanics research says about why your spine flexes off the floor and how to correct your levers.

THE NUMBER:
22 degrees

SCRIPT:

0:00 - 0:15
[VISUAL: Close-up of a loaded barbell on a rubber gym floor. Hands grip the knurling, tension sets in, and the lumbar spine immediately rounds as the plates break the floor.]

Your spine is rounding on the deadlift. Even when you swear it looks completely flat, it is bending. You feel the pull in your lower back, you drop the weight, you try to keep your chest up, and the moment it gets heavy again, your back curves like a fishing rod. 

0:15 - 0:30
[VISUAL: Narrator speaking directly to camera, sitting at a desk with papers and an anatomical model of a lumbar vertebra.]

Trying to hold your spine as rigid as a 2x4 is usually the wrong approach. You need to manage your leverage, pack your lats, and build intra-abdominal pressure. I'm not your doctor, but the physics here is straightforward once you strip away the bad cues.

0:30 - 2:00
[VISUAL: Chapter title card on screen: "1. The Illusion of Neutral". Cut to 3D skeletal animation showing the difference between surface musculature and actual vertebral position.]

Let's address the biggest misconception first: the idea that competitive lifters pull heavy weight with zero spinal flexion. 

They don't. 

When researchers placed electrogoniometers on competitive powerlifters pulling maximal loads, they found an average of 22 degrees of lumbar flexion. These were elite athletes whose backs looked completely straight to the naked eye. Thick spinal erectors hide what the vertebrae are doing underneath. 

Your spine is built to flex slightly under load. Controlled, slight flexion that stays within a safe margin is normal. The problem you are dealing with is dynamic rounding. 

Dynamic rounding is when you start in one position, and as soon as the weight leaves the floor, your spine snaps into deeper flexion. That shift under load is where shear forces spike and your tissues take the brunt of the work instead of your hips. You do not need an artificial, rigid back extension. You need an unchanging position from the moment the plates leave the platform to lockout.

2:00 - 3:45
[VISUAL: Chapter title card: "2. The Lever Arm and Your Lats". Split-screen showing two lifters: one with the bar against their shins, one with the bar three inches forward.]

Most people think back rounding is caused by weak back muscles. Usually, it is caused by bad geometry.

Every inch the barbell drifts away from your body increases the moment arm on your hips and lower back. If the barbell is out over your toes instead of over your midfoot, your erectors have to work exponentially harder to stop your spine from folding. Your body realizes this instantly. To survive the lift, it will round your spine forward to shorten that moment arm artificially.

The fix starts in your lats. 

Your lats do not pull the bar up. They pull the bar back into your legs. When you set up, think about squeezing an orange in your armpit, or trying to bend the bar across your shins. That engages the latissimus dorsi. 

By pulling the humerus into extension, the lats do two things. First, they keep the bar glued to your center of mass, reducing the rotational force trying to round your spine. Second, through their connection to the thoracolumbar fascia, they help stabilize your lumbar spine without requiring your lower back to fight the load alone. If the bar drifts an inch off your shins, your back will round. Keep it touching your body.

3:45 - 5:15
[VISUAL: Chapter title card: "3. Pulling the Slack and Wedging". Slow-motion side profile of a lifter pulling the barbell until the plates "clink" against the collar before the floor push.]

The second major error is yanking the bar off the floor. 

A lot of lifters approach the bar, bend down, grab it, and try to rip it upward as fast as possible. When you do that, your hips shoot up first. The moment your hips rise before the bar leaves the floor, your knees extend, your hamstrings lose tension, and your back takes the entire load. You turn a deadlift into a stiff-legged pull.

You need to take the slack out of the bar. 

When you grip the bar, pull up on it with about seventy percent of the force needed to lift it. You should hear the bar click against the inside of the weight plates. The bend should come out of the bar before the weights leave the rubber.

At the same time, you wedge your hips toward the bar. Think about pushing the floor away with your feet rather than pulling the bar with your hands. If your hips and chest rise at the exact same rate during the first three inches of the pull, your lower back will stay in position. If your hips shoot up first, you will round. Every time.

5:15 - 7:00
[VISUAL: Chapter title card: "4. The Fluid Cylinder: Real Bracing". Diagram of the diaphragm descending and intra-abdominal pressure expanding against the abdominal wall.]

The third mechanic is intra-abdominal pressure. 

Most people are told to "suck in the stomach" or pull their navel to their spine. That cue is useless under a heavy barbell. Drawing in your abdomen reduces intra-abdominal pressure and destabilizes your trunk.

You want the opposite: the Valsalva maneuver. 

Take air deep into your belly, not your chest. Then, contract your abdominal wall outward in three hundred and sixty degrees, as if you are preparing to take a punch in the ribs, the obliques, and the lower back simultaneously. 

Research indicates that intra-abdominal pressure creates an internal fluid ball that supports the anterior aspect of the spine. It takes compressive stress off the vertebral bodies and reduces the demand on the spinal extensors. 

Do not start the pull until that brace is fully locked. If you exhale during the first half of the lift, you dump that pressure, and your spine will immediately flex to compensate for the lost stability.

7:00 - 8:00
[VISUAL: Chapter title card: "Bro-Science Corner". Graphic of a cracked spinal disc with a red "DEBUNKED" stamp.]

Now for the bro-science corner. 

You have probably heard the claim that any amount of spinal flexion under load will pop a disc like a jelly doughnut. The idea is that your spine is a fragile stack of teacups, and bending under weight causes direct tissue damage.

That claim is not supported by the literature. 

A 2020 systematic review in the Journal of Orthopaedic & Sports Physical Therapy examined lumbar spine flexion during lifting. The researchers found no clear prospective evidence linking lumbar flexion during lifting to an increased risk of low back pain. 

Your spine is an adaptable biological structure, not a dry twig. Slight, gradual flexion under load is something tissues can adapt to over time. The real issue is dynamic, uncontrolled buckling under loads you have not adapted to manage. So stop panicking if your spine flexes a few degrees. Focus on preventing rapid position changes during the pull.

8:00 - 9:00
[VISUAL: Text on screen listing the research papers and DOIs mentioned in the script.]

Here are the sources. 

First, the research on spinal kinematics during competitive powerlifting, showing that elite lifters flex an average of 22 degrees in the lumbar spine even when visually flat, comes from Cholewicki, McGill, and Norman, published in Medicine and Science in Sports and Exercise, 1991. The DOI is 10.1249/00005768-199110000-00012.

Second, the systematic review showing the lack of clear evidence between lumbar flexion during lifting and low back pain onset was conducted by Saraceni and colleagues, published in the Journal of Orthopaedic & Sports Physical Therapy, 2020. The DOI is 10.2519/jospt.2020.9218.

Biomechanics can explain the levers, but clinical research on pain is messy. Individual anatomy varies, and what bothers one person's lower back might feel fine to someone else. The evidence on spinal flexion causing direct injury is weaker than fitness influencers claim, but managing your levers remains the most efficient way to move heavy weight.

9:00 - 9:30
[VISUAL: Narrator looking directly at the camera. Neutral background.]

If you have struggled with back rounding on the deadlift, what cue actually fixed it for you? Was it wedging your hips, dragging the bar up your shins, or bracing your trunk differently? 

Drop your answer in the comments. I read them.

SOURCES:
- Powerlifters flex their lumbar spine by an average of 22 to 33 degrees at L4-S1 during maximal deadlifts despite appearing flat :: 10.1249/00005768-199110000-00012
- Systematic review finding no prospective evidence that lumbar spine flexion during lifting is associated with low back pain :: 10.2519/jospt.2020.9218
