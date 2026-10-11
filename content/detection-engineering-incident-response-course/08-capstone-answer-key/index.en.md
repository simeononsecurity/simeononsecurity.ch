---
title: "Detection Engineering and Incident Response Capstone"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Deliver a complete detection and incident package from the synthetic course data, then compare it with a detailed answer key and scoring rubric."
genre: ["Cybersecurity", "Detection Engineering", "Incident Response", "Security Lab"]
tags: ["detection engineering capstone", "incident response capstone", "SOC portfolio", "incident report", "detection rule", "answer key"]
cover: "/img/cover/detection-incident-response-capstone.webp"
coverAlt: "A completed detection rule, incident timeline, scope statement, and response plan in one review package."
coverCaption: "Deliver one reproducible detection and incident package."
---

[Return to the Detection Engineering and Incident Response Course](/detection-engineering-incident-response-course-start/)

**The capstone joins engineering and response into one review package.** Finish your submission before reading the reference answer.

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

## Reference Answer

### Incident Decision

Declare a high-severity incident with high confidence in endpoint compromise and identity misuse. Treat the link between both paths as medium confidence until added provider or network evidence supports one actor or sequence.

### Core Timeline

| Time UTC | ID | Supported interpretation |
|---|---|---|
| **13:58:02** | E-2001 | Outlook writes a macro-enabled document |
| **13:59:28** | E-2002 | Word opens the document |
| **14:00:16** | E-2003 | Word starts encoded PowerShell |
| **14:00:24** | D-3002 | The host resolves the suspicious test domain |
| **14:00:31** | E-2004 | PowerShell writes `sync-update.ps1` |
| **14:01:10** | E-2005 | A scheduled task creates persistence |
| **14:04:09** | A-1004 | Legacy-protocol sign-in succeeds after failures |
| **14:06:41** | A-1005 | A mailbox rule hides invoice mail |
| **14:07:33** | A-1006 | A mail-reading OAuth grant is approved |
| **14:02:49** | E-2006 | PowerShell connects to the DNS answer on TCP 443 |

Sort the finished timeline by timestamp. The table above groups the linked endpoint and identity facts for review, so `E-2006` appears last despite its earlier time. A strong submission flags and corrects this presentation issue in its chronological artifact.

### Scope

Confirmed scope includes Morgan's identity and `HR-LT-044`. Likely scope includes mail reachable through the delegated grant. Exclude `FIN-LT-021` after comparing its approved inventory chain. Unknowns include message access, script content, destination content, initial document delivery detail, and other activity tied to the indicators.

### Detection Package

The strongest first rule detects Office starting encoded PowerShell. A second analytic should correlate the same host with a dropped script, scheduled task, DNS request, or outbound connection within a short window. Identity analytics should cover failed-to-successful legacy access, suspicious mailbox rule creation, and risky delegated consent.

### Response Priorities

Preserve evidence, isolate the endpoint, restrict the identity, revoke sessions and grants, remove the preserved mailbox rule, collect artifacts, recover credentials, rebuild from trusted media, pass recovery gates, and monitor recurrence.

### Executive Update

```text
Security declared an incident involving one employee identity and one managed
Windows endpoint. Evidence shows suspicious cloud access, delegated mail access,
document-driven script execution, persistence, and outbound communication.
Containment and evidence preservation are in progress. Mail access volume and
the script's full behavior remain under investigation, with the next update due
after identity and endpoint collection finishes.
```

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
- [ ] Answer key comparison records corrections
- [ ] Final score meets the threshold

Return to the [course hub](/detection-engineering-incident-response-course-start/) and retain the package as a synthetic portfolio sample.
