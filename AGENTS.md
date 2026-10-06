# Agent Instructions

This repository's canonical agent instructions live in `./.clinerules/`.

Before planning, editing, running commands, or committing changes:

1. Read `./.clinerules/08-clinerules-maintenance.md`.
2. Read every rule file relevant to the task.
3. Select any matching repository skills below and read their `SKILL.md` files.
4. Follow the repository conventions in those rules over generic defaults.
5. Update the relevant `.clinerules/` file when a task reveals a reusable project rule.

The `.clinerules/` directory is the source of truth. This file is the repository-wide
bootstrap and skill-routing entry point. Keep tool-specific instruction files pointed
at the same directory.

## Repository basics

- Use absolute paths when referring to files in agent reports.
- Inspect existing code and content before editing.
- Preserve unrelated working-tree changes.
- Validate edited files before completing a task.
- Do not commit secrets, personal data, host identifiers, IP addresses, ports, or generated output.

## Repository Skills

Skills live in `.agents/skills/` and provide repeatable workflows over the canonical
rules. Load only the skills relevant to the request. Read referenced rules before
acting; a skill does not replace `.clinerules/` or expand the user's authorization.
If the tool does not discover repository skills automatically, open the linked
`SKILL.md` directly and follow it as project instructions.

| Task | Skill |
|---|---|
| Write or revise an article, guide, comparison, or video-based article | [sos-write-article](.agents/skills/sos-write-article/SKILL.md) |
| Generate, replace, convert, or verify article covers and inline images | [sos-content-media](.agents/skills/sos-content-media/SKILL.md) |
| Build or extend a course, certification treatment, quiz bank, or course lab | [sos-build-course](.agents/skills/sos-build-course/SKILL.md) |
| Turn a supplied CTF, HackTheBox, or Sherlock solve into a writeup | [sos-write-writeup](.agents/skills/sos-write-writeup/SKILL.md) |
| Validate or debug Hugo rendering, metadata, shortcodes, feeds, or asset paths | [sos-hugo-validation](.agents/skills/sos-hugo-validation/SKILL.md) |
| Build or fix a browser utility or reactive checksum/hash calculator | [sos-build-browser-tool](.agents/skills/sos-build-browser-tool/SKILL.md) |
| Create sponsored ad artwork, variants, partials, or matching preloads | [sos-ad-creative](.agents/skills/sos-ad-creative/SKILL.md) |

Combine skills when needed. A new illustrated article normally uses article writing
and content media. Add Hugo validation when inspecting output or changing shared
rendering. A text-only correction does not require image generation or a full build.
Course and writeup skills take precedence over the generic article structure for
those formats. Do not create per-tool copies of these skills or of the routing table.

Keep temporary renders, logs, caches, and validation reports out of commits. Intended
source artwork and downloadable course artifacts follow their specific clinerules.
