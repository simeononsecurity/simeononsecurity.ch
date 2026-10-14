---
title: "Detection Engineering Lesson 1: Telemetry and Evidence"
date: 2026-10-10
lastmod: 2026-10-14
toc: true
draft: false
description: "Inventory identity, endpoint, and DNS telemetry. Normalize timestamps, preserve source events, and document evidence limits before analysis."
genre: ["Cybersecurity", "Detection Engineering", "Incident Response"]
tags: ["security telemetry", "event normalization", "log evidence", "detection engineering", "incident timeline", "SOC course"]
cover: "/img/cover/detection-engineering-telemetry-evidence.webp"
coverAlt: "Three log streams feeding a normalized security event timeline with preserved source records."
coverCaption: "Know what each event proves before use."
---

[Return to the Detection Engineering and Incident Response Course](/detection-engineering-incident-response-course-start/)

**A detection is only as strong as its telemetry contract.** The contract states which system produced an event, which fields exist, how time is recorded, and where collection gaps appear.

## Build an Inventory

Create one row per source before opening the investigation files.

| Source | Key fields | Useful question | Limit |
|---|---|---|---|
| **Identity** | User, source IP, device, result, authentication protocol, MFA state | Did a principal authenticate from a new context? | A successful sign-in does not prove who used the credential |
| **Endpoint** | Host, user, process, parent, command line, hash | What executed, and which process launched the child? | Missing events do not prove missing execution |
| **DNS** | Host, user, query, response, answer | Which names did an endpoint resolve? | A lookup does not prove a later connection |

Record retention, clock source, ingestion delay, field transformations, and access owner. **Do not merge similarly named fields until their meanings match.** A device name reported by an identity provider might describe registration state rather than the endpoint which sent traffic.

## Preserve Evidence

1. Copy the sample files into a read-only source folder.
2. Create a separate folder for filters, timelines, and notes.
3. Record a SHA-256 hash for each source file.
4. Use UTC for every derived timeline entry.
5. Keep raw values beside normalized values.

```bash
shasum -a 256 auth-events.jsonl endpoint-events.jsonl dns-events.csv
```

On Linux, use `sha256sum` with the same three filenames. On Windows PowerShell, run:

```powershell
Get-FileHash -Algorithm SHA256 -Path 'auth-events.jsonl','endpoint-events.jsonl','dns-events.csv' |
  Select-Object Path, Hash
```

PowerShell's [Get-FileHash](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash?view=powershell-7.5) computes the same SHA-256 digest from the file bytes. Keep the output with your source inventory.

Expected output:

```text
<64 hexadecimal characters>  auth-events.jsonl
<64 hexadecimal characters>  endpoint-events.jsonl
<64 hexadecimal characters>  dns-events.csv
```

The exact hashes depend on the downloaded bytes. **The verification target is stable hashes across your work session.** Recalculate after the lab and compare the values.

## Normalize a Timeline

List the JSON events in chronological order without changing the source.

```bash
jq -sr 'sort_by(.timestamp)[] | [.timestamp, (.host // .device), .user, .event_type, .correlation_id] | @tsv' \
  auth-events.jsonl endpoint-events.jsonl
```

**Without `jq`, use a text editor.** Open each JSONL file as lines of separate JSON objects. For every line, copy `timestamp`, `host` or `device`, `user`, `event_type`, and `correlation_id` into a new table. Use `-` for an absent field. Sort the new table by the UTC timestamp text, then inspect the DNS CSV and add selected rows. The first five JSON events in the merged order are `A-1001`, `E-2001`, `E-2002`, `E-2003`, and `E-2004`. If your order differs, check the `Z` suffix and sort the copied rows again. Leave the source files unchanged.

Inspect the CSV separately, then place selected DNS rows in your analyst timeline. Keep the original correlation ID in every derived row.

Use these columns:

```text
timestamp_utc | source | asset | principal | action | result | correlation_id | analyst_note
```

**Observation:** `A-1004` records a successful sign-in from `203.0.113.77`.

**Conclusion:** the sign-in is suspicious because earlier failures, a new country, an unknown device, and a legacy protocol surround the event.

The conclusion depends on several observations. Keep the distinction visible.

## Practice Steps

1. Download the [sample data README](/downloads/detection-engineering-incident-response-course/README.md) and its three linked files.
2. Record file hashes.
3. Build the source inventory table.
4. Add the first five events to a normalized timeline.
5. Mark each row as observation, conclusion, or open question.
6. Write one collection gap for each source.

> **Expected Result:** you have a source inventory, stable hashes, five ordered events, and three documented limits.

## Troubleshooting

| Problem | Fix |
|---|---|
| **`jq` reports invalid JSON** | Process the JSONL files one object per line or use `jq -s` as shown |
| **Events sort incorrectly** | Keep ISO 8601 UTC timestamps with the trailing `Z` |
| **A field is absent** | Use `unknown` in notes instead of copying a value from another source |
| **Hashes changed** | Restore the source copies and move analyst notes to a separate file |

## Verify Your Work

- [ ] Source files stayed unchanged
- [ ] Every derived row retains a correlation ID
- [ ] All timestamps use UTC
- [ ] Every conclusion points to at least one observation
- [ ] Every source has a stated collection limit

**Primary reference, checked 2026-10-10:** [CISA logging and monitoring guidance](https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/use-logging-on-business-systems).

## Next Steps

Continue to [Lesson 2: ATT&CK Detection Strategies](/detection-engineering-incident-response-course/02-attack-detection-strategies/). You will connect observed behavior to current ATT&CK defensive objects.
