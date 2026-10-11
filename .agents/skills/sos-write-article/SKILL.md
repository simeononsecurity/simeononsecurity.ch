---
name: sos-write-article
description: "Write or revise sourced SimeonOnSecurity Hugo articles and guides, including Ahrefs-led article campaigns when requested. Use the dedicated course or writeup skill for those formats."
---

## Read first

Locate the repository root through `AGENTS.md`. Read `.clinerules/08-clinerules-maintenance.md`, then rules 03, 04, 05, 06, 09, and 11. Read rule 10 for media generation and rule 18 when translations are in scope. These files remain authoritative; this skill supplies the workflow, not a second style guide. All paths below are repository-relative.

## Workflow

1. Inspect nearby articles and search existing coverage before selecting a slug. Define the reader's outcome and keep the new page distinct from existing coverage. For comparisons, state the exact products, interfaces, and evaluation date. Apply rule 03's CLI/GUI grouping boundaries.
2. Verify claims against current primary sources. Visit each new external link and read its actual topic, not only its HTTP status. Use the available browsing tools when the historical tool names in rule 06 are unavailable. Verify internal links against content files and explicit slugs. Keep an evidence record outside committed content.
3. Distinguish external measurements, personal testing, expected behavior, and recommendations. A supplied transcript is source material, not proof of its claims. Preserve failed attempts and qualify cached timings or partial tests. Do not imply hands-on testing unless it occurred.
4. Write the page bundle and front matter using rule 04. Apply rule 03's article structure and scannability checks and rule 05's prose review. For new articles, include `lastmod`; preserve the original publication date when revising. Follow rule 03's fidelity check for additive revisions. Keep editorial workflow details out of reader-facing prose. Discuss AI normally when AI is the subject.
5. For requested YouTube embeds, use the named `id` form and the per-instance privacy opt-in in rule 09. Keep a watch link, omit an unverified upload date, and confirm a rendered player exists. Do not change the global privacy setting.
6. Run the `sos-content-media` audit after finishing each article in a campaign, and whenever creating, replacing, or auditing images for a single article. Follow rules 10 and 11. Generate only missing or approved replacement media for the selected page. Inspect the images. Generated illustrations must not supply invented evidence. Run only one media generator process at a time across concurrent article work.
7. For a new article, run rule 10's full dry-run scan to identify pending media, then use a scoped dry run and scoped generation for the selected page. Do not launch a site-wide write pass as a side effect of one article.
8. Validate YAML, local links, shortcode arguments, table width, prose restrictions, and image references for the selected files. Review the entire page after a correction so older tables or examples do not contradict it. Follow rule 08 for targeted versus full rendering; use `sos-hugo-validation` when inspecting generated output.

## Ahrefs-led article campaigns

Use this section only when the user requests an article batch or Ahrefs-led selection. Do not impose a batch size, Ahrefs dependency, six-agent review, or translation campaign on an ordinary article request.

1. Read the full `.clinerules/` folder and inspect the existing article catalog before selecting work. Confirm actual Ahrefs access. Record the report, date, location, filters, and ranking URL for each candidate. Treat Ahrefs traffic as an estimate. Compare candidates with existing bundles and aliases, search intent, overlap, source availability, and the reader's task. Keep this selection record outside committed articles. Never claim Ahrefs evidence from a tool listing or inaccessible report.
2. Track the user's requested count as distinct source-language article bundles. Translations do not increase the count. Include both new and materially improved articles only after their content, media, and validation pass. Keep the worklist and evidence outside committed content.
3. Use `deep-research` for each selected article and `write-like-me:write-like-me` for the established voice when the user requests those skills and they are available. Use `pages:write-page` only for an actual Pages deliverable. Use `codex-security:vulnerability-writeup` only for a vulnerability writeup, subject to the repository's dedicated writeup skill. Read each applicable skill before use. Missing tools do not count as completed research.
4. For additive improvements, preserve all existing sections, images, code blocks, examples, and useful technical information. Correct errors in place and add missing detail. Compare the full revised article with the original before counting it. Do not disclose Ahrefs, AI-assisted writing, or production automation in published prose. This does not ban AI as an article subject or accurate source attribution.
5. When translations are requested or required for a selected bundle, apply rule 18 to every configured language. Preserve code, links, shortcodes, media references, and meaning. Audit all configured languages before marking the bundle complete.
6. When the user requests independent agent reviews, honor the requested model and reasoning effort. For a six-role review, assign a beginner reader, SEO reviewer, fact checker, instructor, mid-level reader, and expert reader. The beginner checks comprehension. SEO checks intent, metadata, links, and overlap. The fact checker verifies claims and commands. The instructor checks teaching quality. The mid-level reader checks immediate utility. The expert checks depth and tradeoffs. Give each reviewer the final article, relevant sources, and a concrete acceptance rubric. Collect specific findings and an explicit verdict. Re-review changed text until every requested reviewer signs off. Respect available agent slots and keep media generation serial. Do not claim approval from an agent that did not review the final version.

## Finish

Report the article paths, sources checked, media completed, translations, review status, and validation performed. For batches, reconcile the requested count against finished source-language bundles. Commit only when requested, with each article and its assets together. Do not push or publish merely because the article is ready.
