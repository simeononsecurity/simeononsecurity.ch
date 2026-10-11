---
title: "Detection Engineering Lesson 3: Detection Hypotheses and Rules"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Turn a behavior hypothesis into portable detection logic, positive and negative tests, tuning criteria, and an operational runbook."
genre: ["Cybersecurity", "Detection Engineering", "Security Operations"]
tags: ["detection hypothesis", "Sigma rule", "rule testing", "false positive tuning", "security analytics", "SOC runbook"]
cover: "/img/cover/detection-hypotheses-rules.webp"
coverAlt: "A detection hypothesis moving through rule logic, test events, and analyst triage."
coverCaption: "Test behavior before sending alerts to analysts."
---

[Return to the Detection Engineering and Incident Response Course](/detection-engineering-incident-response-course-start/)

**A detection hypothesis predicts observable behavior.** A rule implements one part of the hypothesis in a specific data model.

## Define the Hypothesis

Use this sentence:

```text
When an Office process starts an encoded PowerShell command, the event deserves review because document-driven script execution is uncommon in the course environment and appears before persistence or outbound traffic in the scenario.
```

Record five items:

- **Behavior:** Office parent starts PowerShell
- **Observable fields:** parent image, child image, command line, user, host, timestamp
- **Population:** managed Windows endpoints with process creation telemetry
- **Expected benign cases:** approved document automation and enterprise add-ins
- **Escalation evidence:** dropped script, scheduled task, suspicious DNS, or outbound connection

## Write Portable Logic

The example follows the official Sigma rule structure. Adapt field mappings before deployment.

```yaml
title: Office Process Starts Encoded PowerShell
id: 908e82a9-4f44-4f20-8da1-9e8af49fdb81
status: test
description: Detects an Office process starting PowerShell with an encoded command.
date: 2026-10-10
logsource:
  category: process_creation
  product: windows
detection:
  parent_office:
    ParentImage|endswith:
      - '\\WINWORD.EXE'
      - '\\EXCEL.EXE'
      - '\\POWERPNT.EXE'
  child_powershell:
    Image|endswith:
      - '\\powershell.exe'
      - '\\pwsh.exe'
  encoded_flag:
    CommandLine|contains:
      - '-EncodedCommand'
      - '-enc '
  condition: parent_office and child_powershell and encoded_flag
falsepositives:
  - Approved document automation after environment review
level: high
```

**Status `test` matters.** The rule has not earned production status until telemetry mapping, replay tests, volume review, and analyst handling pass.

## Build Test Cases

| Test | Event shape | Expected |
|---|---|---|
| **Positive 1** | Word starts PowerShell with `-EncodedCommand` | Match |
| **Positive 2** | Excel starts `pwsh.exe` with `-enc` | Match |
| **Negative 1** | Software Center starts an approved PowerShell file | No match |
| **Negative 2** | Word starts a PDF viewer | No match |
| **Boundary** | Word starts PowerShell without an encoded flag | No match, then review whether separate logic covers the behavior |

Run the positive and negative cases against your SIEM translator or local rule test tool. Record the backend query and field mapping. **A valid YAML file does not prove correct detection behavior.**

## Define Operations

Every alert needs a short runbook:

1. Confirm host, user, parent, child, and command line.
2. Decode content in an isolated analysis workflow without execution.
3. Search for child processes, file writes, persistence, and outbound connections.
4. Compare the parent document hash and origin with approved software records.
5. Escalate when related persistence, identity misuse, or network activity appears.
6. Close as expected only when an owner and approved behavior record support the decision.

> **Expected Result:** another analyst knows which evidence to collect, which alternate explanations to test, and when to declare an incident.

## Troubleshooting

| Problem | Fix |
|---|---|
| **No positive events match** | Compare backend field names and case handling with the normalized schema |
| **Approved scripts match** | Narrow the parent-child relationship or add a documented filter with an owner and review date |
| **The query is too expensive** | Filter on indexed parent and child fields before command-line terms |
| **Alert volume rises after an update** | Compare new parent paths, process names, and management software versions before broad suppression |

## Verify Your Work

- [ ] Hypothesis names behavior, population, and reason for review
- [ ] Rule status stays `test`
- [ ] Two positive and two negative tests exist
- [ ] Field mappings are recorded
- [ ] Runbook includes escalation and closure evidence
- [ ] Every suppression has an owner and review date

**Primary reference, checked 2026-10-10:** [Sigma rule structure and logsource guidance](https://sigmahq.io/docs/basics/rules.html).

## Next Steps

Continue to [Lesson 4: Triage and Scoping](/detection-engineering-incident-response-course/04-triage-scoping/). Use the alert as a starting point for an evidence search.
