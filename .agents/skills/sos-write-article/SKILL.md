---
name: sos-write-article
description: "Write or revise articles and guides in the SimeonOnSecurity Hugo repository, including sourced comparisons and video-based articles. Use the dedicated course or writeup skill for those formats."
---

## Read first

Locate the repository root through `AGENTS.md`. Read `.clinerules/08-clinerules-maintenance.md`, then rules 03, 04, 05, 06, 09, and 11. These files remain authoritative; this skill supplies the workflow, not a second style guide. All paths below are repository-relative.

## Workflow

1. Inspect nearby articles and search existing coverage before selecting a slug. Preserve supplied technical detail and define the reader's outcome. For comparisons, state the exact products, interfaces, and evaluation date. Apply rule 03's CLI/GUI grouping boundaries.
2. Verify claims against current primary sources. Visit each new external link and read its actual topic, not only its HTTP status. Use the available browsing tools when the historical tool names in rule 06 are unavailable. Verify internal links against content files and explicit slugs. Keep an evidence record outside committed content.
3. Distinguish external measurements, personal testing, expected behavior, and recommendations. A supplied transcript is source material, not proof of its claims. Preserve failed attempts and qualify cached timings or partial tests. Do not imply hands-on testing unless it occurred.
4. Write the page bundle and front matter using rule 04. Apply rule 03's article structure and scannability checks and rule 05's prose review. For new articles, include `lastmod`; preserve the original publication date when revising.
5. For requested YouTube embeds, use the named `id` form and the per-instance privacy opt-in in rule 09. Keep a watch link, omit an unverified upload date, and confirm a rendered player exists. Do not change the global privacy setting.
6. Use `sos-content-media` when creating, replacing, or auditing images. Keep visual breaks within rule 11's limit. Generated illustrations must not supply invented evidence.
7. Validate YAML, local links, shortcode arguments, table width, prose restrictions, and image references for the selected files. Review the entire page after a correction so older tables or examples do not contradict it. Follow rule 08 for targeted versus full rendering; use `sos-hugo-validation` when inspecting generated output.

## Finish

Report the article paths, sources checked, media completed, and validation performed. Commit only when requested, with each article and its assets together. Do not push or publish merely because the article is ready.
