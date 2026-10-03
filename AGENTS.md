# Agent Instructions

This repository's canonical agent instructions live in `./.clinerules/`.

Before planning, editing, running commands, or committing changes:

1. Read `./.clinerules/08-clinerules-maintenance.md`.
2. Read every rule file relevant to the task.
3. Follow the repository conventions in those rules over generic defaults.
4. Update the relevant `.clinerules/` file when a task reveals a reusable project rule.

The `.clinerules/` directory is the source of truth. This file is only the repository-wide
bootstrap entry point. Keep tool-specific instruction files pointed at the same directory.

## Repository basics

- Use absolute paths when referring to files in agent reports.
- Inspect existing code and content before editing.
- Preserve unrelated working-tree changes.
- Validate edited files before completing a task.
- Do not commit secrets, personal data, host identifiers, IP addresses, ports, or generated output.