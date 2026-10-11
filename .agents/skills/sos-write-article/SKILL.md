---
name: sos-write-article
description: "Write or revise sourced SimeonOnSecurity Hugo articles and guides, including Ahrefs-led article campaigns when requested. Use the dedicated course or writeup skill for those formats."
---

## Read first

Locate the repository root through `AGENTS.md`. Read `.clinerules/08-clinerules-maintenance.md`, then rules 03, 04, 05, 06, 09, and 11. Read rule 10 for media generation and rule 18 when translations are in scope. Read `sos-hugo-validation` when rendered output needs inspection, `sos-content-media` when media work is in scope, and `sos-build-browser-tool` when the article ships a browser utility. These files remain authoritative. This skill supplies the workflow, not a second style guide. All paths below are repository-relative.

## Execution modes and preflight

Classify the request before editing:

1. New article
2. Additive revision
3. Read-only article audit
4. Ahrefs-led campaign
5. Translation bundle
6. Article supported by video
7. Article with an interactive artifact
8. Benchmark or comparison article

Before delegation or editing, record the current commit, working-tree status, target paths, requested source-language count, configured languages, media scope, reviewer set, and commit or push authorization. Preserve unrelated changes. Assign disjoint paths to parallel agents. Keep research records, worklists, manifests, and reviewer reports outside committed article content.

## Workflow

1. Inspect nearby articles and search existing coverage before selecting a slug. Define the reader's outcome and keep the new page distinct from existing coverage. For comparisons, state the exact products, interfaces, workload, and evaluation date. Apply rule 03's CLI/GUI grouping boundaries.
2. Build a claim evidence matrix outside committed content. Record each material claim, source URL, source title or H1, source date or version, verification method, and status. Classify claims as measured result, external measurement, observed behavior, expected behavior, estimate, calculation, or recommendation. Recheck time-sensitive claims near completion.
3. Verify claims against current primary sources. Visit each new external link and read its actual topic, not only its HTTP status. Use available browsing tools when historical tool names in rule 06 are unavailable. Verify internal links against content files and explicit slugs. Treat redirects to error pages, soft 404s, login walls, and automated 403 responses as verification failures until an approved alternate method confirms the target.
4. Distinguish external measurements, personal testing, expected behavior, and recommendations. A supplied transcript is source material, not proof of its claims. Preserve failed attempts and qualify cached timings or partial tests. Do not imply hands-on testing unless it occurred.
5. For commands and configuration, verify the product version, operating system, permissions, inputs, expected output, failure behavior, and destructive side effects. Mark commands as tested or untested. Do not expose secrets, personal data, host identifiers, or private infrastructure details.
6. For benchmarks, record the model, weights, quantization, runtime, context length, prompt and decode conditions, warm or cold state, system RAM, actual prompt tokens, host configuration, and measurement date. Keep workload-specific results separate from universal rankings.
7. Write the page bundle and front matter using rule 04. Apply rule 03's article structure, cognitive-level guidance, emphasis layer, paragraph limits, table guidance, and visual-break checks. Apply rule 05's prose review. For new articles, include `lastmod`. Preserve the original publication date when revising. Do not add author fields. Keep editorial workflow details out of reader-facing prose. Discuss AI normally when AI is the subject.
8. For revisions, create a preservation manifest covering headings, substantive sections, code fences, examples, images, figure references, tables, and links. Compare the complete revised page with the original. Any deletion requires an accuracy correction or explicit user instruction. Review the entire page after corrections so older examples and tables do not contradict the new text.
9. For requested YouTube embeds, use the named `id=` form and the per-instance privacy opt-in in rule 09. Keep a watch link, omit an unverified upload date, and confirm a rendered player exists. When supplied video supports an article, use the video as supporting material. Do not add a “reference video” section or frame the article as being about the video. Do not change the global privacy setting.
10. For interactive artifacts, keep the HTML and supporting files inside the relevant article bundle. Use the repository shortcode or embed pattern. Verify distinctive rendered markers, scripts, links, and user-facing fallback behavior.
11. Run the `sos-content-media` audit after finishing each article in a campaign, and whenever creating, replacing, or auditing images for a single article. Follow rules 10 and 11. Generate only missing or approved replacement media for the selected page. Inspect every generated image. Generated illustrations must not supply invented evidence. Run only one media generator process at a time across concurrent article work.
12. For a new article, run rule 10's full dry-run scan to identify pending media, then use a scoped dry run and scoped generation for the selected page. A site-wide write pass requires an explicit site-wide media request. If a site-wide run is authorized, record the worklist, success count, failure count, generated dimensions, visual inspection, and legacy warnings separately.
13. Validate YAML, front matter fields, local links, shortcode arguments, table width, prose restrictions, raw image usage, and image references for the selected files. Run targeted Hugo validation when useful. Inspect generated HTML, canonical metadata, Open Graph metadata, JSON-LD, TOC anchors, image paths, figure output, video output, and interactive embeds. A successful command exit status alone does not establish correct output.
14. Derive translation languages from `config/_default/config.toml`, not from existing filenames. Compare every translation against English for headings, tables, code, links, shortcode parameters, image paths, metadata, translated prose, and script usage. Report coverage as a count. Translation QA does not establish a new English fact-check.

## Ahrefs-led article campaigns

Use this section only when the user requests an article batch or Ahrefs-led selection. Do not impose a batch size, Ahrefs dependency, six-agent review, or translation campaign on an ordinary article request.

1. Read the full `.clinerules/` folder and inspect the existing article catalog before selecting work. Confirm actual Ahrefs access. Record the report, date, location, filters, ranking URL, and source project for each candidate. Treat Ahrefs traffic as an estimate. Compare candidates with existing bundles and aliases, search intent, overlap, source availability, and the reader's task. Keep this selection record outside committed articles. Never claim Ahrefs evidence from a tool listing or inaccessible report.
2. Track the user's requested count as distinct source-language article bundles. Translations do not increase the count. Include both new and materially improved articles only after their content, media, translation, review, and validation pass. Use bounded batches with a parent-side filesystem audit after each batch. Do not treat a delegated completion message as repository evidence.
3. Use `deep-research` for each selected article. Use `pages:write-page` only for an actual Pages deliverable. Use `codex-security:vulnerability-writeup` only for a vulnerability writeup, subject to the repository's dedicated writeup skill. Read each applicable skill before use. Missing tools do not count as completed research.
4. For additive improvements, preserve all existing sections, images, code blocks, examples, and useful technical information. Correct errors in place and add missing detail. Compare the full revised article with the original before counting it. Do not disclose Ahrefs, AI-assisted writing, or production automation in published prose. This does not ban AI as an article subject or accurate source attribution.
5. When translations are requested or required for a selected bundle, apply rule 18 to every configured language. Preserve code, links, shortcodes, media references, and meaning. Audit all configured languages before marking the bundle complete.
6. Use the reviewer matrix below when the user requests independent agent reviews. Re-review changed text until every requested reviewer approves the final version. Run the final reviewer pass after translation, media, and rendering changes. Respect available agent slots and keep media generation serial.

## Reviewer subagent dispatch

Treat reviewer roles as independent subagent work, not as a checklist for the parent agent to simulate. When this skill is invoked for a campaign, a substantial article, an explicit review request, or from a goal loop, spawn the requested reviewer roles as separate subagents before declaring the work complete. A goal loop does not replace reviewer dispatch.

Dispatch one focused subagent per independent reviewer role. Dispatch independent roles in parallel. Do not ask one subagent to impersonate multiple reviewers. Give each subagent the final article snapshot, evidence matrix, applicable rules, precise role, acceptance criteria, and read-only constraints. Require a verdict and findings with file or line references.

The parent agent integrates approved changes, records every reviewer verdict, checks for conflicts, validates the resulting files, and dispatches re-reviews for every role affected by a change. If available agent slots require batching, preserve separate role reports and do not declare completion until every requested role has reviewed the final version. Reviewer subagents must not edit the article unless the task explicitly assigns them an editing role.

## Reviewer matrix

The default campaign review includes a beginner reader, SEO reviewer, fact checker, instructor, mid-level reader, and expert reader.

The beginner reader checks comprehension. The SEO reviewer checks intent, metadata, links, and overlap. The fact checker verifies claims and commands. The instructor checks teaching quality. The mid-level reader checks immediate utility. The expert checks depth and tradeoffs.

Add these reviewers for most substantial articles:

1. Source provenance reviewer. Maps material claims to sources. Checks source freshness, attribution, transcript limitations, estimates, and unsupported conclusions.
2. Reproducibility reviewer. Checks commands in a safe environment or against a controlled fixture. Verifies versions, flags, expected output, permissions, failure handling, and destructive risk.
3. Hugo output reviewer. Checks front matter, shortcodes, rendered HTML, canonical metadata, JSON-LD, TOC output, image paths, video output, and interactive artifacts.

Add these reviewers according to the article type:

4. Accessibility reviewer. Checks heading order, alt text accuracy, table readability, link labels, color dependence, and mobile scanning.
5. Security and safety reviewer. Checks insecure defaults, dangerous commands, secret leakage, missing warnings, and unsupported security promises. Use for security, operations, networking, and system administration content.
6. Media truth reviewer. Checks covers and figures for invented commands, fake terminal output, unsupported benchmarks, misleading labels, incorrect alt text, and missing attribution.
7. Translation quality reviewer. Checks language-specific fluency, technical meaning, script usage, preserved markup, and English-copy leakage. Review language groups rather than pretending one reviewer validates every language.
8. Freshness reviewer. Checks versions, deprecations, lastmod, dated metrics, changing prices, current product behavior, and future update triggers.
9. Search intent reviewer. For large campaigns, split this from on-page SEO. Check cannibalization, search intent, article boundaries, title promises, aliases, and internal-link placement.
10. Readability and skimmability reviewer. Read the article as a human reader. Reject walls of text, long paragraphs, weak section breaks, vague headings, dense tables, missing emphasis, and poor visual rhythm. Request tables, figures, videos, inline links, bold terms, italic callouts, or code blocks when each addition improves comprehension. Confirm the bold and italic layer reconstructs the article's main points during a fast scan. Apply rules 03 and 11 instead of adding decoration without reader value.
11. Bloom's taxonomy reviewer. First identify whether the article teaches, explains, guides, compares, evaluates, or asks the reader to create something. Map each major section to the intended cognitive level. For education-focused content, check progression from definition and understanding through application, analysis, evaluation, and creation when the topic requires it. Request missing explanations, worked actions, comparisons, exercises, decision criteria, or next steps. Do not force educational scaffolding into a reference page or a narrowly factual news item.

Every reviewer receives the final article snapshot, the evidence matrix, applicable rules, and a role-specific acceptance rubric. Every report returns `APPROVE` or `CHANGES REQUIRED`, findings with severity and file or line references, supporting evidence, required corrections, and re-review status. Do not claim approval from an agent that did not review the final version.

## Acceptance and finish

Before completion, classify every requested article and deliverable as verified, partial, blocked, or unverified. Do not hide failed research, media failures, translation gaps, reviewer holds, or render limitations behind a general success statement.

Check whether the task exposed a reusable failure mode, convention, user correction, tool behavior, or repeated workflow. Update the relevant `.clinerules/` file before committing when a new rule is warranted. Validate the skill and references after any skill change.

Report the article paths, source evidence, media status, translation coverage, reviewer verdicts, render checks, unresolved limitations, and validation performed. For batches, reconcile the requested count against finished source-language bundles. Commit only when requested, with each article and its assets together. Do not push or publish merely because the article is ready.
