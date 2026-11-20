# Approved Capstone Requirement

Revision: 1
Owner: fictional workshop coordinator

Start from a fresh course lab extraction. This task is separate from the `--status` filter in `requirements.md`.

Add an optional `--format` argument after the JSON file path. Accept `text` and `json`. The default and `--format text` print the original `Total tasks: 4` line for the supplied data.

`--format json` prints one valid JSON object to standard output. It has a `total` number and a `by_status` object with one count for each status present in the input. For the supplied data, the result has `total` 4, `open` 2, and `done` 2. An empty list returns `total` 0 and an empty `by_status` object. Do not add prose before or after the JSON object.

Reject an unsupported format with a nonzero exit and a clear error. Reject a task without a string `status` with a nonzero exit and a clear error. Keep `tasks.json` unchanged. Change only `task_report.py` and focused tests. Test default text, explicit text, JSON values, empty input, missing status, and invalid format. Do not commit or publish the feature edit during the agent task.
