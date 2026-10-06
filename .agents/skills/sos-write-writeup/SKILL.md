---
name: sos-write-writeup
description: "Turn supplied CTF, HackTheBox, Sherlock, or challenge-solving material into a SimeonOnSecurity writeup while preserving technical steps and applying the site redaction conventions."
---

## Read first

Read `.clinerules/08-clinerules-maintenance.md`, then rules 12, 03, 04, 05, and 06. Rule 12 supplies the writeup-specific structure and casual-word exceptions. Inspect a matching existing crypto or challenge writeup before drafting.

## Workflow

Inventory the supplied files, commands, findings, and final result. Preserve the complete real solve. Do not invent a test run, security incident, or prompt-injection storyline to fill gaps; identify missing evidence during drafting.

Use rule 12's compact first-person format, provided-files section, walkthrough, and result block. Split commands from output in new code blocks. Avoid formal audit metadata, tool-selection rationales, numbered meta-headings, and an added Key Takeaways recap.

Redact scored answers and identifying values using the canonical placeholders while preserving the real command and surrounding output. Check for remaining fragments, not only a full-value match. Do not expose secrets or real infrastructure details.

Verify new source links and local asset references. Use `sos-content-media` for requested covers or relevant illustrations, never to fabricate screenshots of challenge evidence. Compare the final writeup against the supplied solve step by step. Validate front matter, code fences, redaction, and targeted rendering as required by rule 08.

## Finish

Report the writeup path and verification performed. Distinguish source-derived findings from commands run during this task. Commit the source and media together only when requested.
