---
title: "Detection Engineering and Incident Response Quiz"
date: 2026-10-10
lastmod: 2026-10-11
toc: true
draft: false
description: "Test telemetry, ATT&CK mapping, detection logic, triage, scoping, containment, recovery, and evidence handling."
genre: ["Cybersecurity", "Detection Engineering", "Incident Response"]
tags: ["detection engineering quiz", "incident response quiz", "MITRE ATT&CK quiz", "SOC assessment"]
cover: "/img/cover/detection-incident-response-quiz.webp"
coverAlt: "An analyst reviewing detection and incident response questions beside an evidence timeline"
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

## Progression Gate

| Score | Required next action |
|---|---|
| **9 to 10** | Start the capstone after recording missed-item corrections |
| **7 to 8** | Revisit each missed lesson, correct every missed reason, and retake the quiz from a clean copy. Start the capstone only after the retest reaches 9 out of 10 |
| **0 to 6** | Repeat Lessons 1 through 6 with the sample timeline, correct every missed reason, and retake the quiz. Reach 9 out of 10 before the capstone |

> **Expected Result:** each choice has an evidence-based reason before you view the key.

## Verify Your Work

- [ ] All ten questions have answers and reasons
- [ ] The first attempt is complete before the key opens
- [ ] Missed items link to a specific lesson
- [ ] The score is recorded without secrets or real incident data

Open the [Quiz Answer Key](/detection-engineering-incident-response-course/09-quiz-answer-key/) after you finish every answer. Start the [Capstone](/detection-engineering-incident-response-course/08-capstone/) only after your score reaches 9 out of 10.
