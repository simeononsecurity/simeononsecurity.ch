---
title: "Detection Engineering and Incident Response Course"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Build and test detections with synthetic identity, endpoint, and DNS evidence. Investigate an incident and report your findings."
genre: ["Cybersecurity", "Detection Engineering", "Incident Response", "Security Operations"]
tags: ["detection engineering course", "incident response course", "MITRE ATT&CK", "Sigma rules", "security analytics", "alert triage", "incident investigation", "threat detection", "SOC training", "cybersecurity lab"]
cover: "/img/cover/detection-engineering-incident-response-course.webp"
coverAlt: "Security analysts linking identity, endpoint, and DNS events across an investigation timeline."
coverCaption: "Build detections and turn alerts into supported incident decisions."
---

**This course joins detection engineering with incident response.** You will define observable behavior, write testable logic, investigate synthetic evidence, choose response actions, and record improvements.

The course uses a fictional compromise across identity, endpoint, and DNS logs. Every conclusion must point to evidence. Every response step must state an owner, approval boundary, and verification check.

## Audience

This course serves junior security analysts, system administrators moving into security operations, and detection engineers who need a repeatable investigation method.

**You should know basic command-line navigation and JSON.** Prior SIEM, EDR, or forensic experience is optional.

## Outcomes

By the end, you will produce:

- A **telemetry inventory** with fields, retention needs, and trust limits
- An **ATT&CK-informed detection hypothesis** tied to current Detection Strategies and Analytics
- A **portable rule specification** with test cases and tuning notes
- A **full incident timeline** built from three synthetic log sources
- A **scope statement** separating confirmed impact, likely impact, and unknowns
- A **response plan** with containment, recovery, and improvement checks

## Course Order

| # | Lesson | Skill and output |
|---|---|---|
| **1** | [Telemetry and Evidence](/detection-engineering-incident-response-course/01-telemetry-evidence/) | Normalize events and record source limits |
| **2** | [ATT&CK Detection Strategies](/detection-engineering-incident-response-course/02-attack-detection-strategies/) | Map behavior without treating ATT&CK as proof |
| **3** | [Detection Hypotheses and Rules](/detection-engineering-incident-response-course/03-detection-hypotheses-rules/) | Write logic, tests, and tuning criteria |
| **4** | [Triage and Scoping](/detection-engineering-incident-response-course/04-triage-scoping/) | Decide severity and find related activity |
| **5** | [Full Investigation Lab](/detection-engineering-incident-response-course/05-investigation-lab/) | Build a supported timeline from sample data |
| **6** | [Containment and Recovery](/detection-engineering-incident-response-course/06-containment-recovery/) | Plan safe response and verify restoration |
| **7** | [Quiz and Answer Key](/detection-engineering-incident-response-course/07-quiz-answer-key/) | Check concepts and evidence handling |
| **8** | [Capstone and Answer Key](/detection-engineering-incident-response-course/08-capstone-answer-key/) | Deliver a detection and incident package |

Work in order. **Lessons 3 through 6 reuse the same event story**, so skipped steps leave evidence gaps.

## Prerequisites

- **Python 3** for optional JSON parsing
- **`jq`** for command-line JSON filters, or a text editor with JSON support
- **A clean working folder** for evidence copies and analyst notes
- **Forty-five to sixty minutes per lesson** and ninety minutes for the capstone

Download the [data README](/downloads/detection-engineering-incident-response-course/README.md), [authentication events](/downloads/detection-engineering-incident-response-course/auth-events.jsonl), [endpoint events](/downloads/detection-engineering-incident-response-course/endpoint-events.jsonl), and [DNS events](/downloads/detection-engineering-incident-response-course/dns-events.csv). Save all four files in one folder. Do not alter the source files.

## Working Method

1. Record the question before searching.
2. Preserve source timestamps and time zones.
3. Separate observations from analyst conclusions.
4. Mark missing evidence as unknown.
5. Test alternate explanations.
6. Verify each containment and recovery action.

> **Expected Result:** your final report lets another analyst reproduce the timeline and reach the same supported findings.

## Current Framework Note

**MITRE ATT&CK v19.2 is current as of October 10, 2026.** ATT&CK deprecated Data Sources in v18. Use current **Detection Strategies**, platform-specific **Analytics**, and Data Components when planning detections. Legacy Data Source pages remain available for reference.

Incident response guidance also changed. **NIST SP 800-61 Rev. 3**, published in April 2025, places response inside the broader Cybersecurity Framework 2.0 risk cycle. Preparation, detection, response, recovery, and improvement operate as connected activities.

**Primary references, checked 2026-10-10:** [MITRE ATT&CK version history](https://attack.mitre.org/resources/versions/), [MITRE ATT&CK Detection Strategies](https://attack.mitre.org/detectionstrategies/), [MITRE ATT&CK Analytics](https://attack.mitre.org/analytics/), and [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

## Troubleshooting

- **The data files open in a browser:** save the raw files into one working folder.
- **A lesson result differs:** compare timestamps, event IDs, and stated assumptions.
- **A tool is missing:** use a text editor and preserve the same evidence fields.

## Verify Readiness

- [ ] All three event files and the README are present
- [ ] Source files have recorded hashes
- [ ] UTC is the timeline standard
- [ ] Analyst notes use a separate file

> **Expected Result:** the working folder contains preserved evidence, stable hashes, and an empty analyst timeline ready for Lesson 1.

## Start Here

Begin with [Lesson 1: Telemetry and Evidence](/detection-engineering-incident-response-course/01-telemetry-evidence/). Create the evidence inventory before writing a rule or naming an incident.
