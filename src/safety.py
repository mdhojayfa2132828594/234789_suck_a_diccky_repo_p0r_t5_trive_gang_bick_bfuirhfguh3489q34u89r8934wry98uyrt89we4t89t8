"""
Deterministic safety gate. No AI here on purpose.

An LLM cannot tell a real DOI from one it just generated - they look identical
to the model. So every check in this file is a lookup or a regex, not an opinion.

Returns: PASS | FLAG | BLOCK
"""

import re, json, urllib.request, urllib.parse, urllib.error

# ---------------------------------------------------------------- patterns

DOSING = re.compile(
    r"\b\d+(?:\.\d+)?\s?(?:mg|mcg|µg|g|kg|ml|iu|iu\/|units?|grams?|milligrams?|"
    r"micrograms?|tablespoons?|teaspoons?|capsules?|scoops?|pills?)\b", re.I)

# NOTE: must require a UNIT/DOSE noun after the quantity, otherwise it fires on
# harmless coaching phrases like "take a chest-up cue" or "take a breath".
DOSING_ADVICE = re.compile(
    r"\b(?:take|dose|dosage|supplement with|ingest|consume|administer)\s+"
    r"(?:\d+(?:\.\d+)?|one|two|three|four|five|half|a|an)\s+"
    r"(?:mg|mcg|\u00b5g|g|kg|ml|iu|units?|grams?|milligrams?|micrograms?|"
    r"scoops?|pills?|capsules?|tablets?|drops?|servings?|doses?)\b", re.I)

ABSOLUTE = re.compile(
    r"\b(?:cure[sd]?|cures|guaranteed?|100\s?%|"
    r"magic bullet|miracle|eliminates?|eradicates?|reverses?|"
    r"doctor[- ]approved|clinically proven|scientifically proven)\b", re.I)

DISEASE_CLAIM = re.compile(
    r"\b(?:treat[sd]?|treating|heals?|healing|prevents?|preventing)\s+"
    r"(?:cancer|diabetes|alzheimer'?s?|dementia|covid|hiv|aids|arthritis|"
    r"depression|anxiety|autism|epilepsy|parkinson'?s?|multiple sclerosis)\b", re.I)

# Generic second person. In an ADVICE channel this is the whole format, so it
# is a NOTE, not a flag - flagging it guarantees 100% human review and kills
# the automation.
INDIVIDUAL = re.compile(r"\b(?:you should|you need to|if your)\b", re.I)

# Genuine medical personalisation. This is the one that actually matters.
MEDICAL_PERSONAL = re.compile(
    r"\b(?:consult|ask|talk to|see|check with)\s+(?:your|a)\s+"
    r"(?:doctor|physician|clinician|gp|healthcare provider|medical team)|"
    r"\bseek (?:medical|professional) (?:advice|attention|care)|"
    r"\bif you (?:have|are|'re|'ve)\s+(?:been\s+)?"
    r"(?:diagnosed|pregnant|taking|on\s+medication|suffering|"
    r"experiencing|live with|a\s+history|any\s+(?:medical|health|heart|"
    r"kidney|liver))|"
    r"\bfor your (?:condition|specific situation)", re.I)

# Rhetorical intensifiers - worth seeing, not worth blocking on.
INTENSIFIER = re.compile(
    r"\b(?:instantly|instant|immediately|effortlessly|instantaneous)\b", re.I)

PHARMA = re.compile(
    r"\b(?:ozempic|semaglutide|wegovy|mounjaro|tirzepatide|zepbound|"
    r"viagra|sildenafil|cialis|tadalafil|adderall|ritalin|modafinil|"
    r"steroids?|testosterone (?:injection|therapy|replacement)|sarm[s]?|"
    r"clenbuterol|dianabol|anavar|trenbolone|hgh|human growth hormone)\b", re.I)

PREGNANCY = re.compile(
    r"\b(?:pregnan(?:t|cy)|fertility|conception|breastfeeding|"
    r"contraception|birth control|menopause|contraceptive)\b", re.I)

SENSITIVE = re.compile(
    r"\b(?:suicide|self[- ]harm|kill (?:yourself|myself)|eating disorder|"
    r"anorexia|bulimia|purge|binge(?:ing)?|domestic abuse|"
    r"sexual assault|self[- ]mutilation)\b", re.I)

DOI = re.compile(r"\b10\.\d{4,9}/[^\s\"'<>)\]]+", re.I)

# Author-year citations. DOIs are not the only thing a model invents - it also
# invents "Enebo et al., 1976". These get checked the same way.
AUTHOR_YEAR = re.compile(
    r"\b([A-Z][A-Za-z\-\u00e9']{2,})\s+"
    r"(?:and\s+([A-Z][A-Za-z\-\u00e9']{2,})\s+)?"
    r"(?:et\s+al\.?\s*,?\s*)?"
    r"\(?((?:19|20)\d{2})\)?")

# Naming a journal is the model's favourite way to fake authority once you ban
# DOIs - "a 2019 PeerJ study found..." sounds sourced but cannot be checked.
# If a venue is named, a resolvable DOI must accompany it.
JOURNAL = re.compile(
    r"\b(?:PeerJ|Nature|Science|Cell|JAMA|Lancet|BMJ|PLoS\s?ONE|PNAS|"
    r"Journal of Biomechanics|Clinical Biomechanics|Spine|"
    r"Journal of Applied Physiology|Journal of Physiology|"
    r"Journal of Strength and Conditioning Research|"
    r"Medicine & Science in Sports and Exercise|"
    r"European Journal of Applied Physiology|Sports Medicine|"
    r"Journal of Sport and Health Science|Gait & Posture)\b", re.I)

# Fabricated first-person authority. The single fastest way to destroy a
# channel is to have the narrator claim credentials they do not have.
CREDENTIAL_CLAIM = re.compile(
    r"\b(?:I (?:am|'m) (?:a|an) (?:doctor|physician|surgeon|physio(?:therapist)?|"
    r"physical therapist|nutritionist|dietitian|researcher|scientist|"
    r"orthop(?:a)?edic|clinician|MD|PT)|"
    r"I\s+(?:work|spend|practis\w*|practic\w*)\b[^.\n]{0,40}?\s(?:in|as|at)\b|"
    r"(?:my|our) (?:patients|clients|practice|clinic|lab|caseload)|"
    r"I (?:have|'ve) (?:treated|seen|diagnosed|operated)|"
    r"in my (?:clinical|medical|professional) (?:practice|experience|career))", re.I)


# ---------------------------------------------------------------- citation check

def _crossref_ok(query_or_doi, timeout=25):
    """Resolve a DOI, or title-search CrossRef. Returns bool."""
    try:
        if query_or_doi.lower().startswith("10."):
            url = "https://api.crossref.org/works/" + urllib.parse.quote(query_or_doi)
        else:
            url = ("https://api.crossref.org/works?rows=1&select=title&query="
                   + urllib.parse.quote(query_or_doi[:160]))
        req = urllib.request.Request(url, headers={"User-Agent": "channel-ops/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode("utf-8", "ignore"))
        if "message" not in data:
            return False
        m = data["message"]
        if isinstance(m, dict) and m.get("title"):
            return True
        if isinstance(m, dict) and m.get("items"):
            return len(m["items"]) > 0
        return False
    except Exception:
        return False


def _author_year_ok(surname, year, timeout=25):
    """Bibliographic search: does ANY real paper match surname+year?"""
    try:
        url = ("https://api.crossref.org/works?rows=1&query.author="
               + urllib.parse.quote(surname)
               + f"&filter=from-pub-date:{year}-01-01,until-pub-date:{year}-12-31")
        req = urllib.request.Request(url, headers={"User-Agent": "channel-ops/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode("utf-8", "ignore"))
        return bool((data.get("message") or {}).get("items"))
    except Exception:
        return False


def check_citations(text, do_verify=True):
    """Pull DOIs and author-year citations, verify both against CrossRef."""
    dois = list(dict.fromkeys(DOI.findall(text)))
    unverified, verified = [], []
    for d in dois:
        d = d.rstrip(".,;)")
        (verified if (do_verify and _crossref_ok(d)) else unverified).append(d)

    seen, ay_unverified, ay_verified = set(), [], []
    for surname, coauthor, year in AUTHOR_YEAR.findall(text):
        if len(surname) < 4:
            continue
        key = (surname.lower(), year)
        if key in seen:
            continue
        seen.add(key)
        label = f"{surname} et al., {year}"
        if not do_verify:
            continue
        (ay_verified if _author_year_ok(surname, year) else ay_unverified).append(label)

    venues = list(dict.fromkeys(JOURNAL.findall(text)))
    venue_unverified = []
    if venues and not verified:
        venue_unverified = venues   # named a journal but supplied no resolvable DOI

    unverified = unverified + ay_unverified
    return {"venues_named": venues,
            "venues_unverifiable": venue_unverified,"dois_found": len(dois), "verified": verified, "unverified": unverified,
            "author_year_verified": ay_verified,
            "author_year_unverified": ay_unverified}


# ---------------------------------------------------------------- the gate

BLOCKERS = [
    ("dosing-numbers", DOSING,
     "Contains a quantity+unit that could be read as a dose."),
    ("dosing-advice", DOSING_ADVICE,
     "Tells the viewer to take/ingest something."),
    ("pharma-product", PHARMA,
     "Names a pharmaceutical or performance-enhancing substance."),
    ("disease-claim", DISEASE_CLAIM,
     "Claims to treat, heal or prevent a named disease."),
    ("fabricated-credential", CREDENTIAL_CLAIM,
     "Narrator claims professional credentials. Never invent authority - "
     "the channel has no on-camera expert."),
    ("pregnancy", PREGNANCY,
     "Pregnancy/fertility/contraception content needs a qualified reviewer."),
    ("sensitive-topic", SENSITIVE,
     "Self-harm / eating disorder / abuse content must never be auto-produced."),
]

FLAGS = [
    ("absolute-language", ABSOLUTE,
     "Absolute or overclaim language. Soften or remove."),
    ("medical-personalization", MEDICAL_PERSONAL,
     "Reads as advice to a specific patient. Make it explicitly general."),
]

# Informational only. Recorded so you can see them, but they do NOT change the
# verdict and do NOT force human review.
NOTES = [
    ("general-advice", INDIVIDUAL,
     "Second-person advice - normal for this channel."),
    ("intensifier", INTENSIFIER,
     "Rhetorical intensifier (instantly/immediately). Usually fine."),
]


def evaluate(text, verify_citations=True):
    hits_block, hits_flag, hits_note = [], [], []
    for name, rx, msg in BLOCKERS:
        for m in rx.finditer(text):
            s = max(0, m.start() - 60)
            hits_block.append({"rule": name, "match": m.group(0),
                               "context": text[s:m.end() + 60].replace("\n", " "),
                               "reason": msg})
    for name, rx, msg in FLAGS:
        for m in rx.finditer(text):
            s = max(0, m.start() - 60)
            hits_flag.append({"rule": name, "match": m.group(0),
                              "context": text[s:m.end() + 60].replace("\n", " "),
                              "reason": msg})

    for name, rx, msg in NOTES:
        for m in rx.finditer(text):
            s_ = max(0, m.start() - 60)
            hits_note.append({"rule": name, "match": m.group(0),
                              "context": text[s_:m.end() + 60].replace("\n", " "),
                              "reason": msg})

    cites = check_citations(text, do_verify=verify_citations)
    if cites.get("venues_unverifiable"):
        hits_flag.append({"rule": "named-venue-no-doi",
                          "match": ", ".join(cites["venues_unverifiable"][:3]),
                          "context": "Journal named but no resolvable DOI supplied",
                          "reason": "Cite with a real DOI, or state the claim "
                                    "without naming a journal."})
    if cites["unverified"]:
        hits_flag.append({"rule": "unverified-citation",
                          "match": ", ".join(cites["unverified"][:3]),
                          "context": "citation could not be resolved against CrossRef",
                          "reason": "Drop it or replace with a resolvable source."})

    verdict = "BLOCK" if hits_block else ("FLAG" if hits_flag else "PASS")
    return {
        "verdict": verdict,
        "blockers": hits_block,
        "flags": hits_flag,
        "notes": hits_note,
        "citations": cites,
    }
