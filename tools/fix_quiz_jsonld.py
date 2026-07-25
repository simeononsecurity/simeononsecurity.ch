#!/usr/bin/env python3
"""
fix_quiz_jsonld.py
------------------
Replace the broken FAQPage JSON-LD blocks in all quiz section layouts with a call
to the new quiz_jsonld.html partial.

The old code used:
    resources.Get "static/quiz-dicts/XXXDICT.json"
which looks in assets/, NOT static/. The dict files are in static/, so the block
rendered an empty mainEntity array on every quiz page.

The new partial (layouts/partials/quiz_jsonld.html) uses os.ReadFile, which is
project-relative and correctly reads from static/.

For ccna_quiz.html and cybersecurity_quiz.html which never had a FAQPage block,
the partial call is inserted after the breadcrumbs partial.
"""
import re
import os

LAYOUT_DIR = os.path.join(os.path.dirname(__file__), "..", "layouts", "section")

# layout filename → quiz dict name (matches static/quiz-dicts/NAME.json)
LAYOUT_TO_DICT = {
    "a_plus_quiz.html":        "aplusdict",
    "casp_plus_quiz.html":     "caspplusdict",
    "ccna_quiz.html":           "ccnadict",
    "ceh_quiz.html":            "cehdict",
    "cissp_quiz.html":          "cisspdict",
    "cybersecurity_quiz.html":  "quizdict",
    "cysa_plus_quiz.html":      "cysaplusdict",
    "linux_plus_quiz.html":     "linuxplusdict",
    "network_plus_quiz.html":   "netplusdict",
    "pentest_plus_quiz.html":   "pentestplusdict",
    "secai_plus_quiz.html":     "secaiplusdict",
    "secot_plus_quiz.html":     "secotplusdict",
    "security_plus_quiz.html":  "secplusdict",
}

# Matches the whole broken FAQPage <script> block (may span ~18 lines)
FAQ_BLOCK_RE = re.compile(
    r'[ \t]*<script type="application/ld\+json">\s*\{[\s\S]*?"@type":\s*"FAQPage"[\s\S]*?</script>[ \t]*\n?',
    re.MULTILINE,
)

def partial_call(dict_name: str) -> str:
    return f'  {{{{ partial "quiz_jsonld.html" (dict "Page" . "dictName" "{dict_name}") }}}}\n'

changed = []
for fname, dict_name in LAYOUT_TO_DICT.items():
    fpath = os.path.join(LAYOUT_DIR, fname)
    if not os.path.exists(fpath):
        print(f"  SKIP (not found): {fname}")
        continue

    with open(fpath, encoding="utf-8") as fh:
        content = fh.read()

    if FAQ_BLOCK_RE.search(content):
        new_content = FAQ_BLOCK_RE.sub(partial_call(dict_name), content, count=1)
        action = "replaced FAQPage block"
    elif '{{ partialCached "breadcrumbs.html"' in content:
        # No existing FAQPage block — insert after breadcrumbs line
        new_content = content.replace(
            '{{ partialCached "breadcrumbs.html" . .Page}}',
            '{{ partialCached "breadcrumbs.html" . .Page}}\n' + partial_call(dict_name),
            1,
        )
        action = "added partial after breadcrumbs (was missing FAQPage)"
    else:
        print(f"  WARNING — no injection point found: {fname}")
        continue

    if new_content == content:
        print(f"  UNCHANGED (regex did not match): {fname}")
        continue

    with open(fpath, "w", encoding="utf-8") as fh:
        fh.write(new_content)
    print(f"  OK [{action}]: {fname}")
    changed.append(fname)

print(f"\nDone — modified {len(changed)}/{len(LAYOUT_TO_DICT)} quiz layouts.")
