---
name: sos-build-browser-tool
description: "Create or fix browser-side utilities in the SimeonOnSecurity Hugo site, including reactive integrity calculations and meaningful verification of the shipped JavaScript."
---

## Read first

Read `.clinerules/08-clinerules-maintenance.md`, rule 16, and relevant parts of rules 09 and 15. Inspect the existing tool layout and its hyphen/underscore duplicates before editing. Read shared prose rules for user-facing text.

## Workflow

Use the existing content-page/layout pair and add a new tool to the tools index when requested. Preserve the existing UI conventions and use a unique CSS prefix.

Keep user inputs in the browser. Rule 16's named exceptions do not grant a new tool permission to transmit data. Do not add remote processing or tracking payloads containing user input to simplify implementation.

Recompute every derived value when any contributing input changes. Empty inputs clear stale results. Automatic recalculation, timers, and initialization pass the no-tracking path; only explicit activation records the normal event.

Validate the shipped code, not a rewritten copy. Syntax-check extracted or rendered JavaScript and compare results with independent reference vectors or standard implementations. Exercise input/change events through a realistic DOM or browser. Supply required Web Crypto in a test environment. Verify clearing, errors, debounce behavior, and silent automatic analytics. Investigate whether a failed expectation or test environment is wrong before changing implementation.

Apply a fix to both resolving layout variants where duplicates exist. Check network behavior and inspect the relevant rendered UI. Use targeted checks for isolated tool changes; use `sos-hugo-validation` for shared changes under rule 08.

## Finish

Report the user-visible change and reference/interaction checks. Keep all examples synthetic and inspect sample fragments for residual personal data. Update rule 16's inventory for a new integrity tool. Commit only within the user's requested scope.
