---
title: "Incident Response Lesson 5: Full Investigation Lab"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Investigate a synthetic identity and endpoint compromise from raw JSONL and CSV evidence. Build a timeline, scope statement, findings, and search plan."
genre: ["Cybersecurity", "Incident Response", "Security Lab"]
tags: ["incident response lab", "security investigation", "JSONL logs", "DNS logs", "timeline analysis", "SOC lab"]
cover: "/img/cover/full-incident-investigation-lab.webp"
coverAlt: "Identity, endpoint, and DNS evidence arranged into a complete incident timeline."
coverCaption: "Investigate the evidence and support every finding."
---

[Return to the Detection Engineering and Incident Response Course](/detection-engineering-incident-response-course-start/)

**This lab uses synthetic evidence to investigate one compromise.** Preserve the source files, record every query, and keep unsupported details marked unknown.

## Lab Goal

Deliver four artifacts:

- A **source and hash record**
- A **UTC incident timeline**
- A **scope and findings report**
- A **next-search plan**

Download [authentication events](/downloads/detection-engineering-incident-response-course/auth-events.jsonl), [endpoint events](/downloads/detection-engineering-incident-response-course/endpoint-events.jsonl), and [DNS events](/downloads/detection-engineering-incident-response-course/dns-events.csv).

## Step 1: Verify Sources

```bash
shasum -a 256 auth-events.jsonl endpoint-events.jsonl dns-events.csv
wc -l auth-events.jsonl endpoint-events.jsonl dns-events.csv
```

Expected record counts:

```text
8 auth events
8 endpoint events
7 DNS CSV lines, including the header
```

If counts differ, download the files again before analysis.

## Step 2: Find Entities

```bash
jq -r '[.timestamp, (.host // .device), .user, .event_type, (.source_ip // .destination_ip // "-")] | @tsv' \
  auth-events.jsonl endpoint-events.jsonl
```

List unique users, hosts, IP addresses, domains, hashes, application names, rule names, and task names. Mark documentation addresses and `.test` domains as synthetic indicators.

Expected high-interest entities include:

- **Identity:** `morgan.lee@example.test`
- **Host:** `HR-LT-044`
- **Source IP:** `203.0.113.77`
- **Destination IP:** `203.0.113.90`
- **Domain:** `cdn-sync.example.test`
- **Task:** `Document Sync Update`
- **Application:** `Document Sync Test`

## Step 3: Build the Timeline

Create a table with source, event ID, fact, and interpretation. Include at least these turning points:

1. `E-2001` creates the document.
2. `E-2002` opens the document from Outlook.
3. `E-2003` launches encoded PowerShell.
4. `E-2004` writes a script.
5. `E-2005` creates persistence.
6. `A-1004` records suspicious legacy-protocol access.
7. `A-1005` creates a mailbox rule.
8. `A-1006` grants application consent.
9. `D-3002` through `D-3004` resolve the suspicious domain.
10. `E-2006` connects to the matching destination.

The identity and endpoint chains overlap in time. **The evidence does not establish whether one actor controlled both paths.** Treat shared timing and user identity as correlation, then seek provider and network detail.

## Step 4: Test Alternatives

Test at least three explanations:

| Explanation | Supporting evidence | Contradicting evidence |
|---|---|---|
| **Approved document automation** | Office starts PowerShell in some business workflows | Encoded content, persistence, new destination, and unknown script lack approval records |
| **User travel** | A sign-in from another country might follow travel | Earlier US activity, unknown device, legacy protocol, mailbox rule, and consent raise risk |
| **Approved inventory task** | `FIN-LT-021` uses PowerShell | Different parent, script path, destination, user, and approved script label separate the event |

Do not label an explanation false without evidence. Record which owner or log source would resolve it.

## Step 5: State Findings

Use evidence-strength labels.

```text
Finding 1, high confidence: A document opened from Outlook started encoded
PowerShell on HR-LT-044, wrote a script, created a scheduled task, and connected
to 203.0.113.90 after resolving cdn-sync.example.test.

Finding 2, high confidence: Morgan's cloud identity completed a legacy-protocol
sign-in from 203.0.113.77 after two failures, then created a mailbox rule and
granted Mail.Read plus offline_access to Document Sync Test.

Finding 3, medium confidence: The endpoint and identity activity belong to one
incident. Shared identity and close timing support the link. Missing message,
proxy, and decoded-script evidence limit the claim.
```

## Step 6: Define Scope

Confirmed scope includes Morgan and `HR-LT-044`. Likely scope includes mailbox data available to the consented application. Exclude `FIN-LT-021` with written rationale. Keep data access volume and the script's full behavior unknown.

> **Expected Result:** your report declares an incident, supports two high-confidence findings, states one medium-confidence correlation, and lists unresolved evidence.

## Troubleshooting

| Problem | Fix |
|---|---|
| **JSON and CSV rows do not merge cleanly** | Normalize selected fields into a separate analyst table |
| **Time order looks wrong** | Sort full UTC timestamps as text and preserve the trailing `Z` |
| **Encoded content tempts execution** | Do not execute it. Record the value and use an approved isolated decoder workflow |
| **A conclusion lacks an event ID** | Rewrite it as a question or collect supporting evidence |

## Verify Your Work

- [ ] Source hashes match before and after analysis
- [ ] Timeline contains all ten turning points
- [ ] Findings separate facts from conclusions
- [ ] Alternate explanations include supporting and contradicting evidence
- [ ] Scope includes confirmed, likely, excluded, and unknown items
- [ ] Next searches name identity, endpoint, mail, and network owners

## Next Steps

Continue to [Lesson 6: Containment and Recovery](/detection-engineering-incident-response-course/06-containment-recovery/). Choose actions in an order which preserves evidence and limits harm.
