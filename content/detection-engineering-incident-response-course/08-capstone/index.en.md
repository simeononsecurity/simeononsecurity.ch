---
title: "Detection Engineering and Incident Response Capstone"
date: 2026-10-10
lastmod: 2026-10-11
toc: true
draft: false
description: "Deliver a complete detection and incident package from the synthetic course data, then score the result with a defined rubric."
genre: ["Cybersecurity", "Detection Engineering", "Incident Response", "Security Lab"]
tags: ["detection engineering capstone", "incident response capstone", "SOC portfolio", "incident report", "detection rule"]
cover: "/img/cover/detection-incident-response-capstone.webp"
coverAlt: "A completed detection rule, incident timeline, scope statement, and response plan in one review package"
coverCaption: "Deliver one reproducible detection and incident package."
---

[Return to the Detection Engineering and Incident Response Course](/detection-engineering-incident-response-course-start/)

**The capstone joins engineering and response into one review package.** Finish and score your submission before reading the reference answer.

## Scenario

Your security operations lead asks for a detection and incident package based on the three course data files. The package must support analyst review, management decisions, and follow-up engineering work.

## Required Deliverables

1. **Evidence record:** filenames, hashes, counts, time zone, and source limits
2. **Detection strategy card:** behavior, evidence, correlation, exclusions, escalation, and ATT&CK references
3. **Rule draft:** Sigma-style YAML with status `test`
4. **Test matrix:** two positive, two negative, and one boundary case
5. **Timeline:** at least ten source-linked entries
6. **Scope statement:** confirmed, likely, excluded, unknown, and as-of time
7. **Response plan:** five action cards in order
8. **Recovery gates:** identity, endpoint, mail, monitoring, and business
9. **Improvement backlog:** six owned and testable items
10. **Executive update:** five sentences or fewer

## Constraints

- Do not execute the encoded command.
- Do not change source evidence.
- Do not claim message export without message-access records.
- Do not include `FIN-LT-021` in confirmed scope without new evidence.
- Label ATT&CK mappings as behavior mappings rather than proof.

> **Expected Result:** another analyst reproduces your findings from the same files and understands every remaining uncertainty.

## Scoring Rubric

| Area | Points | Full-credit evidence |
|---|---:|---|
| **Evidence handling** | 15 | Stable hashes, counts, UTC, preserved sources, stated limits |
| **Detection design** | 20 | Behavior hypothesis, current ATT&CK objects, rule, tests, runbook |
| **Investigation** | 25 | Reproducible timeline, alternatives, supported findings |
| **Scope** | 15 | Confirmed, likely, excluded, unknown, as-of time |
| **Response** | 15 | Ordered cards, authority, rollback, success checks |
| **Communication** | 10 | Short, factual update with impact and unknowns |

**Passing score:** 80 points with no evidence-integrity failure.

## Troubleshooting

- **Your timeline differs:** compare UTC parsing and correlation IDs.
- **Your scope is broader:** identify direct evidence for each added entity.
- **Your rule matches inventory work:** tighten parent process and encoded flag logic.
- **Your response starts with deletion:** move preservation and authority checks first.

## Verify Completion

- [ ] All ten deliverables exist
- [ ] Source hashes stayed stable
- [ ] Findings cite event IDs
- [ ] The first score is recorded before the answer key opens
- [ ] The final score reaches 80 points with no evidence-integrity failure

Open the [Capstone Answer Key](/detection-engineering-incident-response-course/10-capstone-answer-key/) after you finish and score the full package.
