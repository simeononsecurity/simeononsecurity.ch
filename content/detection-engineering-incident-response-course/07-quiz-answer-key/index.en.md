---
title: "Detection Engineering and Incident Response Quiz"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Test telemetry, ATT&CK mapping, detection logic, triage, scoping, containment, recovery, and evidence handling with a complete answer key."
genre: ["Cybersecurity", "Detection Engineering", "Incident Response"]
tags: ["detection engineering quiz", "incident response quiz", "MITRE ATT&CK quiz", "SOC assessment", "answer key"]
cover: "/img/cover/detection-incident-response-quiz.webp"
coverAlt: "An analyst reviewing detection and incident response questions beside an evidence timeline."
coverCaption: "Check each decision against evidence."
---

[Return to the Detection Engineering and Incident Response Course](/detection-engineering-incident-response-course-start/)

**Answer every question before opening the key.** Write a one-sentence reason for each choice.

## Questions

1. Which statement best describes a telemetry contract?
   A. A list of ATT&CK techniques
   B. A record of source, fields, time, retention, transformations, and limits
   C. A vendor alert severity table
   D. A list of blocked indicators

2. Which ATT&CK object gives platform-specific detection logic in current ATT&CK?
   A. Analytic
   B. Group
   C. Campaign
   D. Mitigation

3. What changed in ATT&CK v18?
   A. Techniques were removed
   B. Data Sources became mandatory
   C. Detection Strategies and Analytics replaced technique detection text, and Data Sources were deprecated
   D. ATT&CK stopped publishing defensive content

4. Which test is a negative case for the course rule?
   A. Word starts PowerShell with `-EncodedCommand`
   B. Excel starts `pwsh.exe` with `-enc`
   C. Software Center starts an approved inventory script
   D. PowerPoint starts encoded PowerShell

5. Why does a successful suspicious sign-in fail to prove actor identity?
   A. Sign-in logs never include users
   B. The event records credential use, while person or process attribution needs more evidence
   C. Every successful sign-in is benign
   D. IP addresses identify people

6. Which finding belongs in confirmed scope?
   A. Mail content was exported, with no message-access records
   B. `HR-LT-044` launched encoded PowerShell, based on `E-2003`
   C. One actor controlled both compromise paths, based only on close timing
   D. Every host using PowerShell is compromised

7. What belongs in an action card?
   A. Purpose, owner, approval, evidence first, risk, rollback, and success check
   B. Only the command to run
   C. A technique ID and severity
   D. A screenshot without source details

8. Which response step addresses delegated access left after a password reset?
   A. Reimage the endpoint only
   B. Revoke OAuth grants and active sessions
   C. Close the alert
   D. Change the DNS server

9. Why is `FIN-LT-021` excluded from confirmed scope?
   A. Finance devices are trusted
   B. Its event chain matches approved inventory context and lacks links to the suspicious indicators
   C. PowerShell is always safe
   D. The event occurred later

10. What proves recovery?
    A. The endpoint starts
    B. The user receives a new password
    C. Security gates pass, monitoring works, and the business owner accepts restored function
    D. The incident ticket has a closing date

## Answer Key

1. **B.** A telemetry contract defines meaning and limits before analysis.
2. **A.** An Analytic holds platform-specific detection logic under a Detection Strategy.
3. **C.** ATT&CK v18 introduced the current defensive object model and deprecated Data Sources.
4. **C.** Approved inventory work should not match the Office-parent encoded-command rule.
5. **B.** The source proves use of an authentication path, not the human behind it.
6. **B.** The event directly records the host behavior.
7. **A.** The card makes authority, evidence risk, rollback, and verification visible.
8. **B.** Password reset alone does not remove sessions or delegated application grants.
9. **B.** Parent, script, destination, user, and approval context support a separate benign workflow.
10. **C.** Recovery needs technical and business validation.

## Score and Review

| Score | Next action |
|---|---|
| **9 to 10** | Start the capstone |
| **7 to 8** | Revisit the missed lesson and correct your reason |
| **0 to 6** | Repeat Lessons 1 through 6 with the sample timeline |

> **Expected Result:** each correct choice has an evidence-based reason, not a memorized label.

## Troubleshooting

- **Two answers seem plausible:** choose the one supported by direct evidence and bounded claims.
- **A framework term is unclear:** return to the official source linked in the related lesson.
- **Your reason differs from the key:** identify which fact changes the decision.

## Verify Your Work

- [ ] All ten questions have answers and reasons
- [ ] Missed items link to a specific lesson
- [ ] Revised answers explain the evidence change
- [ ] Score is recorded without secrets or real incident data

## Next Steps

Complete the [Detection Engineering and Incident Response Capstone](/detection-engineering-incident-response-course/08-capstone-answer-key/).
