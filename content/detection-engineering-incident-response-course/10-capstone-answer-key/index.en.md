---
title: "Detection Engineering Capstone Answer Key"
date: 2026-10-11
lastmod: 2026-10-11
toc: true
draft: false
description: "Compare a completed detection and incident response package with the reference evidence, rule, recovery plan, and executive update."
genre: ["Cybersecurity", "Detection Engineering", "Incident Response", "Security Lab"]
tags: ["detection engineering capstone answer key", "incident response capstone answer", "SOC portfolio review", "incident report reference", "detection rule answer"]
cover: "/img/cover/detection-incident-response-capstone-answer-key.webp"
coverAlt: "An analyst comparing a detection and incident response package with a reference timeline, rule, and recovery plan"
coverCaption: "Compare the finished package with the evidence-based reference."
---

[Return to the Detection Engineering and Incident Response Capstone](/detection-engineering-incident-response-course/08-capstone/)

**Open this reference after you finish and score your capstone.** Record each difference as a correction, unsupported claim, or remaining evidence gap.

## Incident Decision

Declare a high-severity incident with high confidence in endpoint compromise and identity misuse. Treat the link between both paths as medium confidence until added provider or network evidence supports one actor or sequence.

## Evidence Record

These SHA-256 values cover the exact supplied files as published for this course. Recalculate them from your downloads before and after analysis. All times below are UTC. Identity-provider, mail-access, proxy, and script-content records are absent.

| File | Lines | SHA-256 |
|---|---:|---|
| `auth-events.jsonl` | 8 | `fa4bbaf8693287f884d5592f5d401ed66fb0087daada87ed4db6454d0d6de5cb` |
| `endpoint-events.jsonl` | 8 | `a3d053605d71798663ef947bb0f4424b0dfe2f0bbb6aa641c5820b5d5d9cdef1` |
| `dns-events.csv` | 7, including header | `14ddb700e39a3dd46d428d5c0dcda01550baf04e74028fba7744813d551615a9` |

## Core Timeline

| Time UTC | ID | Supported interpretation |
|---|---|---|
| **13:58:02** | E-2001 | Outlook writes a macro-enabled document |
| **13:59:28** | E-2002 | Word opens the document |
| **14:00:16** | E-2003 | Word starts encoded PowerShell |
| **14:00:24** | D-3002 | The host resolves the suspicious test domain |
| **14:00:31** | E-2004 | PowerShell writes `sync-update.ps1` |
| **14:01:10** | E-2005 | A scheduled task creates persistence |
| **14:02:49** | E-2006 | PowerShell connects to the DNS answer on TCP 443 |
| **14:04:09** | A-1004 | Legacy-protocol sign-in succeeds after failures |
| **14:06:41** | A-1005 | A mailbox rule hides invoice mail |
| **14:07:33** | A-1006 | A mail-reading OAuth grant is approved |

The endpoint and identity chains overlap. Shared timing and identity support correlation, while the available sources do not prove a single actor or causal sequence.

## Scope

As of `2026-06-18T15:00:00Z`, confirmed scope includes Morgan's identity and `HR-LT-044`. Likely scope includes mail reachable through the delegated grant. Exclude `FIN-LT-021` after comparing its approved inventory chain. Unknowns include message access, script content, destination content, initial document delivery detail, and other activity tied to the indicators.

## Detection Package

The strongest first rule detects Office starting encoded PowerShell. A second analytic should correlate the same host with a dropped script, scheduled task, DNS request, or outbound connection within a short window. Identity analytics should cover failed-to-successful legacy access, suspicious mailbox rule creation, and risky delegated consent.

Use this Sigma-style rule as the submitted draft. Its `test` status means no production validation is claimed. The backend field mapping and actual match results still need a local translator or SIEM test.

```yaml
title: Office Process Starts Encoded PowerShell
id: 908e82a9-4f44-4f20-8da1-9e8af49fdb81
status: test
description: Detects an Office process starting PowerShell with an encoded command.
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

The strategy card names Office-to-PowerShell execution, process parent and command-line fields, a 60-second host/user correlation window, approved automation as an exclusion candidate, and persistence or outbound activity as escalation evidence. Map the PowerShell behavior to T1059.001 and the scheduled-task evidence separately to T1053.005. Neither mapping proves malicious intent.

The encoded-flag rule has a deliberate blind spot. Alternate PowerShell syntax, transformed or concatenated commands, another script host, or encoded content without `-EncodedCommand` need separate analytics. Record those evasion cases and their test results before claiming broad PowerShell coverage.

| Case | Input shape | Expected rule result | Observed result |
|---|---|---|---|
| Positive 1 | Word starts PowerShell with `-EncodedCommand` | Match | Offline checker: match |
| Positive 2 | Excel starts `pwsh.exe` with `-enc` | Match | Offline checker: match |
| Negative 1 | Software Center starts an approved PowerShell file | No match | Offline checker: no match |
| Negative 2 | Word starts a PDF viewer | No match | Offline checker: no match |
| Boundary | Word starts PowerShell without an encoded flag | No match, review separate analytic | Offline checker: no match |

The supplied [offline checker](/downloads/detection-engineering-incident-response-course/check_rule_cases.py) and [five cases](/downloads/detection-engineering-incident-response-course/rule-test-events.jsonl) produced `5/5 passed`, exit code 0, and zero matches among the two negative cases. For full offline credit, run the checker yourself, attach its output, and map its three predicates to the Sigma selections. Mark the backend query `not run, no SIEM translator available`. For a SIEM-backed submission, also attach the translated query, field mapping, observed results, and false-positive count. The offline checker does not execute the YAML or prove production behavior.

## Response Priorities

Preserve evidence, isolate the endpoint, restrict the identity, revoke sessions and grants, remove the preserved mailbox rule, collect artifacts, recover credentials, rebuild from trusted media, pass recovery gates, and monitor recurrence.

The incident commander collects volatile endpoint evidence before isolation when active harm is controlled. If active exfiltration continues, contain first and record the evidence tradeoff. Use these five action-card exemplars:

| Action and owner | Evidence and approval before change | Success check | Rollback or recovery |
|---|---|---|---|
| Isolate `HR-LT-044`, endpoint lead | Incident commander approval, endpoint and volatile data decision | Host loses unapproved network paths | Restore approved connectivity after trusted rebuild |
| Restrict Morgan's identity, identity lead | Export sign-in and session records, approve business interruption | Old sessions fail and new access uses approved MFA | Temporary scoped access through incident authority |
| Revoke OAuth grant, identity lead | Preserve consent and application IDs | Grant absent and old token path fails | Reauthorize a reviewed app if business owner confirms need |
| Remove mailbox rule, mail lead | Export rule definition and message trace | Rule absent and new mail follows normal routing | Restore only a verified business rule |
| Rebuild endpoint, endpoint lead | Preserve document, script, task, hashes, and chain of custody | Trusted image boots, old task absent, detections healthy | Keep device isolated and restore approved backup |

Each action card needs a timestamp and approval ID in the learner's submitted package.

| Recovery gate | Evidence required before closure |
|---|---|
| Identity | Credential and factor recovery, session revocation, consent review |
| Endpoint | Trusted rebuild, patches, healthy agent, no old task or script |
| Mail | Rule review and message trace preserved |
| Monitoring | Behavior detections active with owner, expiry, and test result |
| Business | Service owner accepts restored function and residual risk |

| Improvement item | Owner | Validation |
|---|---|---|
| Limit legacy authentication | Identity engineering | Test a blocked legacy sign-in and approved modern sign-in |
| Alert on risky delegated consent | Identity engineering | Replay a synthetic consent event into the alert path |
| Keep process parent and command line | Endpoint engineering | Verify both fields arrive from a managed test host |
| Detect unsanctioned scheduled tasks | Detection engineering | Positive and approved-task negative replay |
| Correlate DNS and endpoint connections | Network engineering | Resolve and connect in an isolated test, verify host join |
| Tune Office-to-PowerShell rule | SOC detection owner | Run five-case matrix and record alert volume |

## Executive Update

```text
Security declared an incident involving one employee identity and one managed
Windows endpoint. Evidence shows suspicious cloud access, delegated mail access,
document-driven script execution, persistence, and outbound communication.
Containment and evidence preservation are in progress. Mail access volume and
the script's full behavior remain under investigation, with the next update due
after identity and endpoint collection finishes.
```

## Review Gate

Use the rubric on the [capstone prompt](/detection-engineering-incident-response-course/08-capstone/). Pass with **80 out of 100 or higher** and no evidence-integrity failure.

## Verify Your Review

- [ ] Each correction points to evidence or a stated limitation
- [ ] Unsupported attribution and impact claims are removed
- [ ] The score reaches 80 out of 100
- [ ] No evidence-integrity failure remains

Return to the [Detection Engineering and Incident Response Course](/detection-engineering-incident-response-course-start/) after you record corrections and the final score.
