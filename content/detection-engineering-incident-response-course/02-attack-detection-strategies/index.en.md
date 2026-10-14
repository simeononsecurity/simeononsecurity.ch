---
title: "Detection Engineering Lesson 2: ATT&CK Detection Strategies"
date: 2026-10-10
lastmod: 2026-10-14
toc: true
draft: false
description: "Use current MITRE ATT&CK Detection Strategies and Analytics to describe behavior, telemetry needs, and platform logic without treating a mapping as proof."
genre: ["Cybersecurity", "Detection Engineering", "Threat-Informed Defense"]
tags: ["MITRE ATT&CK v20", "detection strategies", "ATT&CK analytics", "technique mapping", "detection coverage", "SOC course"]
cover: "/img/cover/attack-detection-strategies-course.webp"
coverAlt: "A behavior chain mapped to ATT&CK detection strategies and platform analytics."
coverCaption: "Use ATT&CK to organize detection logic and evidence needs."
---

[Return to the Detection Engineering and Incident Response Course](/detection-engineering-incident-response-course-start/)

**ATT&CK describes adversary behavior and defensive knowledge.** A technique label does not prove intent, attribution, or compromise.

## Use Current Objects

ATT&CK v18 replaced technique-level detection text with **Detection Strategies** and platform-specific **Analytics**. The [MITRE version history](https://attack.mitre.org/resources/versions/) lists **ATT&CK v20.0** as current on October 14, 2026. Use the current technique page and follow its Detection Strategy, Analytic, and Data Component links. Record the version with your mapping.

| Object | Purpose | Analyst use |
|---|---|---|
| **Technique** | Describes adversary behavior | Name the behavior under review |
| **Detection Strategy** | Groups a high-level detection approach | State the behavior chain and needed evidence |
| **Analytic** | Gives platform-specific logic | Adapt conditions to available telemetry |
| **Data Component** | Names an observable event property | Check whether collection supports the logic |

Legacy **Data Sources** were deprecated in v18. Keep older mappings for historical work, then review current Data Components and Analytics before creating new coverage claims.

## Map the Scenario

Start with facts from the sample data. Use a confidence label for each mapping.

| Evidence | Candidate behavior | Confidence |
|---|---|---|
| **`A-1004`** successful legacy-protocol sign-in after failures | Valid Accounts, T1078 | High for credential use, low for actor identity |
| **`E-2003`** Word launches encoded PowerShell | PowerShell, T1059.001 | High |
| **`E-2005`** scheduled task starts a script | Scheduled Task/Job: Scheduled Task, T1053.005 | High |
| **`E-2006` plus `D-3002`** process connects after name resolution | Outbound network communication to a resolved destination | High for connection, unknown for application protocol or command purpose |
| **`A-1005`** hidden mailbox rule | Email Collection or account manipulation behavior | Medium, review exact ATT&CK object and provider audit detail |

**Do not force every event into ATT&CK.** Business context, incident impact, and response authority sit outside a technique map.

## Write a Strategy Card

Create a card for the Word-to-PowerShell behavior.

```text
Behavior: Office process starts PowerShell with encoded content
Question: Did a document trigger script execution outside approved automation?
Required observations: parent process, child process, command line, user, host, time
Correlation: same host and user within 60 seconds
Exclusions: signed enterprise add-ins with documented child-process behavior
Escalation: decoded content, file creation, persistence, or outbound connection
Missing evidence: script block logs and file origin metadata
ATT&CK references: technique T1059.001 plus relevant Detection Strategy and Analytic
```

The card starts with behavior and evidence. ATT&CK supplies vocabulary and related logic. **Your environment supplies thresholds, exclusions, and response actions.**

## Practice Steps

1. Pick `E-2003`, `E-2005`, and `A-1004`.
2. Find the current ATT&CK technique page for each behavior.
3. Follow its Detection Strategy and Analytic links.
4. Record the required Data Components.
5. Compare the requirements with the course telemetry inventory.
6. Mark each supported field, missing field, and ambiguous field.
7. Write one strategy card.

> **Expected Result:** the card names a behavior, required observations, a correlation window, exclusions, escalation evidence, and collection gaps.

## Troubleshooting

| Problem | Fix |
|---|---|
| **Search results show old detection text** | Check the version history and open the current ATT&CK site rather than an archived version |
| **Several techniques fit** | Keep multiple candidates until evidence supports a narrower statement |
| **An Analytic names unavailable fields** | Record the gap and adapt the logic without claiming full coverage |
| **A rule matches one command string only** | Reframe the strategy around behavior and add platform-specific indicators later |

## Verify Your Work

- [ ] Every mapping points to source evidence
- [ ] Confidence is explicit
- [ ] Current Detection Strategies and Analytics replace deprecated Data Source planning
- [ ] Missing telemetry appears in the card
- [ ] No mapping is presented as proof of malicious intent

**Primary references, checked 2026-10-14:** [ATT&CK version history](https://attack.mitre.org/resources/versions/), [Detection Strategies](https://attack.mitre.org/detectionstrategies/), [Analytics](https://attack.mitre.org/analytics/), and [ATT&CK v18 defensive changes](https://attack.mitre.org/resources/updates/updates-october-2025/).

## Next Steps

Continue to [Lesson 3: Detection Hypotheses and Rules](/detection-engineering-incident-response-course/03-detection-hypotheses-rules/). Turn the strategy card into testable logic.
