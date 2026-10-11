---
title: "How to Triage CVEs and Threat Reports"
draft: false
toc: true
date: 2023-06-27
lastmod: 2026-10-10
description: "Triage vulnerabilities through vendor advisories, CVE, NVD, KEV, affected assets, exploit evidence, controls, and confidence-rated threat reporting."
tags: ["CVE triage", "CISA KEV", "vulnerability prioritization", "threat intelligence", "vendor security advisory"]
cover: "/img/cover/An_illustration_of_a_shield_with_a_magnifying_glass_symboli.webp"
coverAlt: "A security analyst comparing a vendor advisory, CVE record, asset data, and threat evidence"
coverCaption: "Prioritize a vulnerability from asset and threat context."
---

[Return to the Cybersecurity Career Playbook](/cyber-security-career-playbook-start/)

A **CVE record** gives a common identifier and description for a publicly disclosed vulnerability. It does not prove your asset is affected, exposed, or exploitable. NVD adds analysis where available. The vendor advisory should guide affected versions and remediation.

## Use a Source Order

1. **Vendor advisory:** Affected products, versions, configurations, fixes, and workarounds
2. **CVE record:** Common identifier and reference trail
3. **NVD:** CVSS and product metadata where analysis exists
4. **CISA KEV:** Evidence of exploitation in the wild for listed entries
5. **Asset record:** Installed version, configuration, exposure, business function, and owner
6. **Internal evidence:** Scanner result, telemetry, compensating controls, and test status

CVSS describes technical severity. It does not equal business risk or fix priority by itself. KEV is one prioritization input. Federal deadlines in BOD 22-01 apply to the covered federal agencies.

## Build a Triage Record

Record:

- CVE and source dates
- Vendor and product
- Affected version and configuration rule
- Asset owner and business service
- Exposure and reachable path
- Exploitation evidence
- CVSS version and score, where useful
- Existing controls
- Remediation or mitigation
- Test, change, and rollback
- Verification and residual risk owner

Do not scan or exploit a system without authorization.

## Handle Threat Actors Carefully

Threat reports differ in source quality and confidence. Separate observed behavior, analytic judgment, and attribution. ATT&CK describes adversary behavior. It does not prove a named actor performed an event.

Record source, publication date, collection window, confidence language, alternative explanation, and relevance to your environment.

## Daily Exercise

Choose one public CVE affecting software in a disposable lab or an invented asset record. Complete the triage fields without exploitation.

**Pass condition:** The record links the vendor advisory, states whether the fictional asset meets the affected condition, uses KEV and CVSS within scope, names an owner, and defines verification. Unknown facts remain explicit.

## References

- [CVE Program](https://www.cve.org/)
- [NIST National Vulnerability Database](https://nvd.nist.gov/)
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [MITRE ATT&CK](https://attack.mitre.org/)

Use the result in a vulnerability, risk, or threat-intelligence portfolio entry with no live organization data.
