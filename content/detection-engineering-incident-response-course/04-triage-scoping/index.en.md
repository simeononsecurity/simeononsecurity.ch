---
title: "Incident Response Lesson 4: Triage and Scoping"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Triage an alert, separate severity from confidence, search related identity and endpoint activity, and write a bounded incident scope statement."
genre: ["Cybersecurity", "Incident Response", "Security Operations"]
tags: ["alert triage", "incident scoping", "security investigation", "severity", "confidence", "SOC workflow"]
cover: "/img/cover/incident-triage-scoping.webp"
coverAlt: "An analyst sorting evidence into confirmed, likely, and unknown incident scope."
coverCaption: "Scope the event before choosing response actions."
---

[Return to the Detection Engineering and Incident Response Course](/detection-engineering-incident-response-course-start/)

**Triage decides what deserves immediate work.** Scoping decides which identities, assets, data, and time ranges belong in the investigation.

## Separate Two Ratings

| Rating | Question | Example |
|---|---|---|
| **Confidence** | How strongly does evidence support the finding? | High confidence for Word launching encoded PowerShell |
| **Severity** | What harm follows if the finding is true? | High severity when identity misuse and persistence appear together |

Do not increase confidence because impact looks serious. Do not lower severity because evidence collection is incomplete.

## Run Initial Triage

1. Confirm the alert fields exist in the source event.
2. Check sensor health and timestamp quality.
3. Identify the principal, host, process tree, and first observed time.
4. Search the same user across identity events.
5. Search the same host across endpoint and DNS events.
6. Look backward fifteen minutes and forward one hour.
7. Record alternate explanations.
8. Decide whether an incident declaration threshold is met.

For the course data, `E-2003` links to file creation, persistence, DNS, and a network connection on `HR-LT-044`. Identity events show suspicious access for the same user. This cross-source chain supports incident declaration.

> **Expected Result:** triage produces a declared incident for `morgan.lee@example.test` and `HR-LT-044`, with the start time set no later than `2026-06-18T13:58:02Z`.

## Build Scope Rings

Use three rings instead of one broad list.

| Ring | Meaning | Course example |
|---|---|---|
| **Confirmed** | Direct source evidence supports involvement | Morgan's identity and `HR-LT-044` |
| **Likely** | Several facts support involvement, but one key fact is missing | Mailbox data accessed by the consented application |
| **Unknown** | Evidence needed for a decision is unavailable | Message access volume, script contents, and data destination content |

`FIN-LT-021` contains PowerShell activity, yet its parent, script path, destination, and surrounding identity event fit approved inventory work. Keep the host outside confirmed scope. Record why.

## Write the Scope Statement

```text
As of 2026-06-18T15:00:00Z, confirmed scope includes the identity
morgan.lee@example.test and endpoint HR-LT-044. Evidence shows suspicious
legacy-protocol access, a mailbox rule, OAuth consent, document-driven encoded
PowerShell, a dropped script, scheduled-task persistence, DNS resolution, and an
outbound connection to 203.0.113.90. Mail access through the consented app is
likely but unconfirmed because message access logs are absent. FIN-LT-021 is not
in scope after review of its approved inventory process. Search remains open for
other activity from 203.0.113.77, the document hash, the script hash, and the
destination domain.
```

The phrase **as of** fixes the statement to a time. Scope changes when new evidence appears.

## Practice Steps

1. Start from `E-2003`.
2. Search all sources for the user, host, IP addresses, domain, hashes, and correlation IDs.
3. Build a fifteen-minute pre-alert window and a one-hour post-alert window.
4. Place each entity in confirmed, likely, unknown, or excluded status.
5. Write a one-paragraph scope statement.
6. Record three next searches and the evidence owner for each.

## Troubleshooting

| Problem | Fix |
|---|---|
| **Everything looks related** | Require a time, entity, or behavior link before adding scope |
| **One benign event ends the search** | Test whether the benign explanation covers every linked observation |
| **Scope never closes** | Set a search boundary and list uncollected sources as residual uncertainty |
| **Severity changes between analysts** | Use documented impact and response criteria, then record the chosen rationale |

## Verify Your Work

- [ ] Confidence and severity are separate
- [ ] Confirmed scope points to direct evidence
- [ ] Excluded entities retain exclusion rationale
- [ ] Unknowns name the missing evidence
- [ ] Scope statement includes an as-of time
- [ ] Next searches have owners

**Primary reference, checked 2026-10-10:** [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

## Next Steps

Continue to [Lesson 5: Full Investigation Lab](/detection-engineering-incident-response-course/05-investigation-lab/). Build the complete timeline and findings package.
