---
title: "DoD 5220.22-M and Current Media Sanitization"
date: 2023-02-12
lastmod: 2026-10-10
toc: true
draft: false
description: "Understand the historical DoD overwrite label and choose current media-specific sanitization guidance."
tags: ["cybersecurity career", "federal security", "security guidance"]
cover: "/img/cover/An_image_of_a_hard_drive_being_securely_erased_using_data.webp"
coverAlt: "A hard drive and a data sanitization symbol."
coverCaption: "Choose a current sanitization method"
---

**DoD 5220.22-M is a historical National Industrial Security Program Operating Manual reference, not a current universal recipe for wiping media.** The NISPOM manual was replaced by [32 CFR Part 117](https://www.ecfr.gov/current/title-32/subtitle-A/chapter-I/subchapter-D/part-117). Do not apply a generic three-pass overwrite rule to every disk, SSD, or USB drive. Use the current [NIST SP 800-88 Revision 2](https://csrc.nist.gov/pubs/sp/800/88/r2/final), organizational policy, and any governing classified-media requirements.

[Return to the Cybersecurity Career Playbook](/cyber-security-career-playbook-start/).

## Choose by Media and Destination

First identify the device, its data classification, and whether it will be reused inside the organization, transferred outside, or destroyed. NIST describes Clear, Purge, and Destroy methods. The method must fit the storage technology and required protection level. A host overwrite may miss flash cells remapped by wear leveling. A vendor's sanitize command or cryptographic erase needs device support and validation. Physical destruction also needs a method suited to the media and a controlled chain of custody.

| Media | Question before choosing a method |
|---|---|
| Magnetic hard disk | Will the full addressable area and hidden areas be covered by the selected method? |
| SSD or USB flash | Does the device support a trustworthy sanitize or cryptographic erase route? How will it be verified? |
| Optical media | Is approved physical destruction the safer route for this medium and classification? |
| Failed device | If commands cannot complete or be verified, should the device be destroyed under policy? |

## Record the Decision

A useful sanitization record names the asset ID, media type, model, serial, data sensitivity, destination, selected method, operator, tool or device command, verification result, validation decision, date, and disposition. If verification fails, quarantine the media and select another approved method. A completed command alone is not a certificate that no data is recoverable.

For practice, use fictional media records and write a decision for one HDD, one SSD, and one failed USB drive. Explain why the same overwrite command does not fit all three. Do not experiment on a real device containing needed data.

Continue with the [NIST media sanitization guide in this playbook](/cyber-security-career-playbook/moving-up-in-your-cybersecurity-career/regulations-and-acts/nist-800-88-ways-of-sanitizing-removable-media/).
