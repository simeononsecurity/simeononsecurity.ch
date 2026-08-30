# Clinerules Maintenance — Capture Lessons as You Work

This rule defines when and how to update the `.clinerules/` directory during any
task. The goal is a living knowledge base: every hard-won lesson, every corrected
mistake, and every clarified convention gets written down immediately so it is
available in every future session.

## When to Create or Update a Rule

Create or extend a clinerule whenever you encounter any of the following:

- **A mistake you had to correct.** If you generated something wrong and had to
  redo it (wrong colour, wrong format, wrong file path, broken command), document
  the failure mode and the fix in the relevant rule file.
- **A convention you had to look up or infer.** If you read several files to figure
  out how something works, write the answer into a rule so it does not need to be
  re-discovered next time.
- **A user correction or clarification.** Any time the user tells you to do
  something differently than you did, that correction is a rule. Capture it.
- **A new tool, script, or pipeline step.** If you add or modify a generator,
  partial, layout, or config file, document its behavior and usage in the
  appropriate rule.
- **A pattern that repeats across tasks.** If you notice you are solving the same
  sub-problem more than once, extract it into a rule.

## How to Choose the Right File

The `.clinerules/` directory uses numbered files. The current set:

| File | Topic |
|------|-------|
| `01-exam-course-treatment-structure.md` | Certification course four-piece treatment |
| `02-practice-test-question-generation.md` | Quiz JSON bank generation |
| `03-content-writing-style.md` | Prose voice and markdown formatting |
| `04-article-front-matter-and-media.md` | Article front matter, images, shortcodes |
| `05-ai-writing-avoidance.md` | Banned words and AI-writing anti-patterns |
| `06-link-verification.md` | External URL verification before publishing |
| `07-ad-cta-guidelines.md` | Ad creative CTA and brand colour standards |
| `08-clinerules-maintenance.md` | This file — rules about maintaining rules |
| `09-hugo-shortcodes-and-partials.md` | Hugo architecture, every shortcode, and all partials |
| `10-cover-image-generation.md` | Cover and inline image generation pipeline (`generate_cover_images.py`) |
| `11-inline-image-strategy.md` | When and how to break up walls of text with inline images |
| `12-writeups-format.md` | CTF/Sherlock/challenge writeup skeleton, redaction rules, and fidelity checks |

When a lesson fits an existing file, append it to that file under an appropriate
`##` heading. When a lesson is a new topic not covered by any existing file, create
a new numbered file (`09-`, `10-`, etc.) with a focused single-topic title.

Do not create one giant catch-all file. Each file should answer one question:
"What do I need to know to do X correctly on this project?"

## How to Write the Rule

Rules must be:

- **Specific, not general.** Name the file, command, field, or behavior. Do not
  write "be careful with colours." Write "the gpt-image-2 model hallucinates pink
  when the sentinel #FF00FF is present — add an explicit ZERO pink line to the
  system prompt."
- **Actionable.** Every rule should end with something you can check or do.
  Use a checklist, a command, or a concrete example.
- **Written in present tense, active voice.** Follow the same prose style as
  `03-content-writing-style.md`.
- **No filler.** Do not restate the obvious. Every sentence should add information
  that would not otherwise be recoverable from reading the code.

## When to Do This

Update rules **during the task**, not after. Before committing work, ask:

1. Did anything go wrong that a future session would repeat?
2. Did the user correct anything I did?
3. Did I figure out something non-obvious about this codebase?
4. Did I add or change any tool, script, or pipeline component?

If the answer to any of those is yes, update or create the relevant clinerule
before the final git commit, and include the `.clinerules/` file in that commit.

## Commit Convention

When a clinerule is the only change, the commit message should be:

```
docs(clinerules): <short description of what was learned>
```

When a clinerule update accompanies a code or content fix, include it in the same
commit with a note in the commit body, for example:

```
fix: <primary change>

- <what was fixed>
- docs(clinerules/07): captured pink-hallucination failure mode and fix
```
