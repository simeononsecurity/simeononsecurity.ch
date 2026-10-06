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
| `13-image-webp-conversion-pipeline.md` | Repo-wide PNG/JPG to WebP conversion pipeline |
| `14-xml-feed-and-sitemap-validation.md` | Validating Hugo's RSS/sitemap/news/image-sitemap XML outputs and known fixed bugs |
| `15-hugo-internal-template-overrides-and-relative-urls.md` | `_internal/` template override pitfall, `relativeURLs` depth-relative path bug, ad-placement `.IsPage` bug |
| `16-client-side-tools.md` | Client-side tool rules, derived-value recalculation, tool verification, ISO 7811-2 stripe encoding |

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

## Agent Bootstrap Files

The repository exposes the same rule system through tool-specific entry points so agents find it
regardless of which tool starts the session:

- `AGENTS.md` is the canonical repository-root bootstrap file.
- `CLAUDE.md`, `CODEX.md`, and `GEMINI.md` point back to `AGENTS.md`.
- `.github/copilot-instructions.md` points to `AGENTS.md` and `.clinerules/`.
- `.cursor/rules/00-project-clinerules.mdc` loads `AGENTS.md` and `.clinerules/` for Cursor.

Keep `./.clinerules/` as the single source of truth. When adding another agent integration, add a
small bootstrap file that points to `AGENTS.md` and the relevant `.clinerules/` files instead of
copying the project rules into another directory.

## Conditional Hugo Builds

Do not run a full Hugo build after every content or documentation change. A full
build takes several minutes and tests the site-wide rendering pipeline, not the
basic validity of one Markdown page.

Use targeted checks for ordinary changes such as:

- adding or editing one article, guide, writeup, course page, or reference list
- changing front matter on an isolated page
- adding verified external links
- updating a question bank and its generator validation
- editing a clinerule or other documentation file

Run a Hugo build when the change can affect how many pages render or how Hugo
processes shared resources. This includes:

- layouts, templates, partials, shortcodes, theme overrides, or shared CSS and JS
- Hugo configuration, output formats, menus, taxonomies, permalinks, or language config
- site-wide assets, image-processing code, cover references, or resource pipelines
- XML feeds, sitemaps, robots output, schema, metadata, or canonical URL behavior
- a new content type or a course treatment that adds many pages and exercises shared templates
- a user-reported rendering problem that needs confirmation in generated HTML

For a single content page, inspect the source, verify internal and external links,
check front matter, run the relevant script or unit tests, and build only that page
or section if a local render is useful. Reserve the full multilingual build for
site-wide changes or a release check. If a full build is required, run it in the
background and inspect the generated output, not only the exit status.

## Repository Skills and Routing

Store shared repository skills in `.agents/skills/<name>/SKILL.md`. `AGENTS.md`
contains the task-to-skill routing table; tool-specific bootstrap files point to
that table. Agents without native discovery read the selected skill file directly.
Do not maintain separate copies for each coding tool.

Keep policy, schemas, and exceptions in the numbered clinerules. Skills describe
the workflow and identify which rules to read. When a rule changes, check its
dependent skills for stale commands or conflicting instructions. A historical
tool name is not a required dependency when an available equivalent verifies the
same evidence. Do not infer authorization to publish, push, or purge caches from
loading a skill.

Validate each skill's front matter and references. Run new executable helpers on
valid and failing fixtures and on the selected real files. Skill and documentation
changes alone do not require a Hugo build. Check every routing link after moving
or renaming a skill.

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
