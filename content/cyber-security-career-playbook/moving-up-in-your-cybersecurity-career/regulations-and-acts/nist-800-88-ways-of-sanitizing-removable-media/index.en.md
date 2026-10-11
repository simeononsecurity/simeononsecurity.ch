---
title: "NIST SP 800-88 Rev. 2 Media Sanitization"
date: 2023-02-11
lastmod: 2026-10-10
toc: true
draft: false
description: "Choose Clear, Purge, or Destroy under NIST SP 800-88 Rev. 2, then verify, validate, and document disposition."
tags: ["cybersecurity career", "federal security", "security guidance"]
cover: "/img/cover/An_image_of_a_person_holding_a_USB_flash_drive_with_a_shreder.webp"
coverAlt: "A USB storage device near a media shredder."
coverCaption: "Plan media sanitization by device type"
---

**NIST SP 800-88 Revision 2 is the current media sanitization guideline.** NIST published the final revision in September 2025. It supersedes Revision 1. The objective is to make access to target data infeasible for a given level of effort. Pick a method from the [current publication](https://csrc.nist.gov/pubs/sp/800/88/r2/final) for the media, data sensitivity, destination, and organizational policy.

[Return to the Cybersecurity Career Playbook](/cyber-security-career-playbook-start/).

## Clear, Purge, and Destroy

| Method | Purpose | Decision point |
|---|---|---|
| Clear | Protect against simple recovery through approved logical techniques | Does the method address the selected medium and its accessible storage? |
| Purge | Apply a method with greater resistance to recovery, including suitable device commands or cryptographic erase | Does the device support the method, and can you validate it? |
| Destroy | Make media unusable through an approved physical process | Does the destruction method fit the device and data classification? |

Do not treat Purge as a fixed number of overwrite passes. Flash translation layers, spare blocks, and device firmware change what a host can reach. Do not assume that dropping an encryption key works unless the device encrypted all target data with suitable keys and the key sanitization process meets the policy.

## Follow a Decision Record

1. Inventory the device by asset ID, model, serial, type, capacity, and owner.
2. Identify data sensitivity, retention duties, reuse or disposal destination, and any special rules.
3. Select an approved method suited to the device. Record the tool, firmware, settings, and operator.
4. Perform the method under a controlled procedure. Keep custody and error logs.
5. Verify that the technique completed as intended, then validate that the result meets the selected protection level.
6. Record the decision and disposition in a certificate or equivalent traceable record.

NIST separates verification of execution from validation of the overall sanitization result. A tool reporting success is evidence for a check, not the entire decision. If a device is damaged or the method fails, quarantine it and follow the approved alternate route.

## Practice Without Erasing a Device

Use three fictional records: a reusable HDD with low-sensitivity lab data, an SSD leaving the organization with sensitive data, and an unreadable USB drive. For each, choose a candidate method and list the missing facts that would change your choice. Submit a completed decision record and a failure route. Have another learner identify the method from your recorded facts. The [historical DoD 5220.22-M page](/cyber-security-career-playbook/moving-up-in-your-cybersecurity-career/regulations-and-acts/dod-5220.22-m-data-sanitization-summarized/) explains why a legacy label does not replace this decision.
