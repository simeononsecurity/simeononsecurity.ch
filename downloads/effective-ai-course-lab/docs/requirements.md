# Approved Practice Requirement

Revision: 1
Owner: fictional workshop coordinator

Keep the current output when no filter is supplied: `Total tasks: 4` for the supplied data.

Add an optional `--status` argument after the JSON file path, with two accepted values, `open` and `done`. The output format stays `Total tasks: N`. With the supplied data, each value has a count of 2. Reject any other value with a nonzero exit status and a clear error. Add tests for the two accepted values, the invalid value, and the unchanged default.

The change belongs in `task_report.py` and its tests. Do not change `tasks.json`. Do not commit or publish the change during course exercises unless a lesson explicitly asks for a local practice commit.
