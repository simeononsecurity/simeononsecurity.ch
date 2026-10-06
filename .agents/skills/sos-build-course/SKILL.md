---
name: sos-build-course
description: "Create or extend SimeonOnSecurity courses and deterministic practice-test banks. Route certification treatments separately from the AI collaboration implementation course."
---

## Read first

Read `.clinerules/08-clinerules-maintenance.md` and shared content rules 03–06 from the repository root. Choose the mode from the user's course, not from a keyword:

- Certification course or practice test: read rules 01 and 02 and inspect SecOT+ or SecAI+ as the working reference.
- AI collaboration implementation course: read rule 17. Do not add certification weights or a quiz bank to this course.
- Another non-certification course: use shared writing rules and its existing structure. Do not infer the certification four-piece treatment applies.

## Certification workflow

Verify the current official objectives, domain labels, weights, and exam code. Build the requested treatment using rule 01's domain pages, start page, quiz page/layout/bank, and both listing pages. For a scoped update, change only the affected pieces and their necessary links.

Clone a functioning quiz layout and replace every dictionary reference and analytics label. Check for old exam strings. Follow rule 02's seeded generator and in-domain distractors; preserve its schema and per-domain minimum. Check valid answer keys, four distinct options, reproducibility across two runs, domain totals, and plausible unique mappings. Passing JSON parsing alone does not prove the questions are sound.

Verify both listing edits on disk and check every hub/domain/practice-test link. Generate missing media through `sos-content-media`. Follow rule 08 for build scope; local quiz activation differs from production, so distinguish template rendering from live quiz behavior.

## Implementation course workflow

Inspect the hub, affected lessons, lab sources, and answer keys together. Preserve the shared scenario and give each lesson its own worked artifact and completion check. Correct contradictory claims across prose, tables, exercises, and solutions. Keep expected outcomes separate from observed results.

For lab edits, rebuild the archive without caches, run the source tests and tests against a fresh extraction, and execute the changed examples there. Do not claim tenant permission tests from local unit tests. Follow rule 17's exact boundaries and course-wide output checks.

## Finish

Report changed course pieces, question counts or lab checks, link/media validation, and actual render scope. Keep generated site output out of commits. Include maintained source banks and intended downloadable artifacts when requested, not temporary build files.
