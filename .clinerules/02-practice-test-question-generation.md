# Practice-Test Question Generation Logic

This rule defines how the `static/quiz-dicts/<examdict>.json` question banks are built. Every
exam practice test on this site is generated the same way so the banks stay large, deterministic,
and consistent. Use the SecOT+ (`secotplusdict.json`) and SecAI+ (`secaiplusdict.json`) banks and
their generator scripts as the canonical reference.

## Question Bank JSON Schema

The bank is a flat JSON array. Each question is an object with exactly these keys:

```json
{
  "question": "Which term or concept best matches this description: \"...\"?",
  "answers": { "A": "...", "B": "...", "C": "...", "D": "..." },
  "correctanswer": "A",
  "reasoning": "... This concept falls under the <Domain> domain of the <Exam> exam."
}
```

Rules:
- Always exactly four options keyed `A`, `B`, `C`, `D`.
- `correctanswer` is a single letter that must exist in `answers`.
- `reasoning` is one or two sentences that restate the correct mapping and name the domain.
- Write the file with `json.dump(bank, f, indent=2, ensure_ascii=False)`.

## Generator Pattern

Build a small, self-contained Python script at `tools/generate_<exam>_practice_test.py`:

1. **`random.seed(1337)`** at the top so the bank is reproducible across runs.
2. A `DATA` dict mapping each official **domain name** to a triple-quoted block of
   `term :: definition` lines (one concept per line). Aim for **38 to 42 concepts per domain**.
3. A `ROLE` constant naming the practitioner persona for scenario questions, for example
   `"OT cybersecurity engineer"` or `"AI security engineer"`.
4. Helper functions:
   - `parse_block(block)` splits a domain block into `(term, definition)` pairs.
   - `letter(i)` returns `"ABCD"[i]`.
   - `make_question(question, correct_text, distractors, reasoning)` shuffles the four options,
     assigns them to A through D, and computes the correct letter.
   - `build_bank(domains, role)` loops every concept and emits the three question styles below.
   - `main()` writes the JSON.

## The Three Question Styles (per concept)

Every concept produces **three** questions, drawing its three distractors from **sibling concepts
in the SAME domain** (`random.sample(other_terms, 3)` or `random.sample(other_defs, 3)`). Keeping
distractors in-domain makes them plausible and exam-realistic.

- **T1 — description to term:** "Which term or concept best matches this description: \"<definition>\"?"
  Options are the correct **term** plus three sibling **terms**.
- **T2 — term to description:** "Within the <Domain> domain, what best describes <Term>?"
  Options are the correct **definition** plus three sibling **definitions**.
- **T3 — scenario to term:** "As a <ROLE>, you encounter something described as \"<definition>\".
  Which term applies?" Options are the correct **term** plus three sibling **terms**.

With ~40 concepts per domain × 3 styles you get **~120 questions per domain**, which satisfies the
**hard minimum of 100 questions per domain**.

## Validation (run before committing the bank)

- Total count: `jq 'length' static/quiz-dicts/<examdict>.json`
- No broken correct answers (must print `0`):
  `jq '[.[]|select(.answers[.correctanswer]==null)]|length' static/quiz-dicts/<examdict>.json`
- No em dashes anywhere (must print `0`): `grep -c "—" static/quiz-dicts/<examdict>.json`
- Spot-check per-domain counts add up to the total and each domain is >= 100.

## Writing the Concept Definitions

The `term :: definition` source is what the prose and the questions share, so write definitions in
the same spartan style required for page content (see `03-content-writing-style.md`):

- Start the definition with a lowercase noun phrase ("a safety procedure that...", "software that...").
- One clause, no em dashes, no semicolons.
- Make each definition uniquely identify its term so T1/T3 have one defensible answer.
