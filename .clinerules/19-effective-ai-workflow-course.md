# Practical AI Workflow Course

The beginner course hub is `content/effective-ai-course-start/index.en.md`. Its
13 numbered lessons live under `content/articles/effective-ai-*/index.en.md`.
Keep this course separate from the advanced AI Collaboration Implementation
Course in rule 17. Do not add certification domain weights or a quiz bank.

## Shared Practice Lab

`static/downloads/effective-ai-course-lab/` is the maintained starter source.
Rebuild `static/downloads/effective-ai-course-lab.zip` after every lab source
change. Keep a single `effective-ai-course-lab/` directory at the archive root.
Exclude `__pycache__` and `.pyc` files. Extract the ZIP into a new directory,
compare its files with the source, run the baseline program, and run its tests.
The untouched baseline prints `Total tasks: 4` and passes two tests.

The lesson 5 feature exercise adds `--status open|done` after the JSON path.
Its checks include counts 4, 2, and 2, invalid status with a nonzero exit,
and unchanged default output. Keep its complete study-route answer key in
lesson 5. Python 3.10 or later supports its `str | None` annotation.

The capstone is a distinct feature in a fresh extraction. It adds
`--format text|json`. Default text output stays `Total tasks: 4`. JSON output
contains `total` and `by_status` counts. Check empty input, missing status,
and an invalid format. Run its complete answer key and tests in a fresh
extraction. Keep its specification in `docs/capstone-requirements.md`.

## Lesson State

Keep the lab state explicit at the start of each lesson. The coding, context,
and verification lessons use the edited copy. The delegation and bounded-loop
examples use a fresh starter copy. The capstone starts from a fresh copy.
Name resets before comparing expected file lists or test counts.

The setup lesson creates a local baseline commit. The repository-context lesson
creates `AGENTS.md` and an optional `CLAUDE.md` pointer, then asks the learner to
make a human guidance commit. Require a clean `git status --short` before the
feature edit. Coding-agent task packets exclude agent commits. Store the Python
test command proven on the learner's platform in `AGENTS.md`, using `py -3` on
Windows when `python3` fails.

## Tracks and Evidence

The connected track requires an observed coding-agent edit, MCP tool read, and
native worker or separate worker session. The study track labels unavailable
tool actions as not run, applies a proposed patch manually, and checks it with
local tests. Supply complete reference files for the manual route. Do not turn
a browser source read into a claim of MCP execution.

Every lesson names an outcome, artifact, expected result, failure diagnosis,
two short self-check questions, and course navigation. Keep expected examples
separate from output observed in the learner's environment. Keep each worker
report short so the main session receives the finding and evidence path
without the full worker transcript. The bounded-loop lesson uses a fresh
starter and a learner-created failing contract test, followed by observed
checks and a fixed action budget.

## Media and Render Checks

The hub and all 13 lessons have individual covers under `assets/img/cover/`.
Run `tools/check_content_media.py --require-cover --generated` on the 14 pages.
Inspect the covers and render the pages to a normal temporary destination.
Check generated page paths, internal links, cover URLs, and structured data
before the scoped commit. Keep render output and caches out of the commit.
