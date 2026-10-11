---
title: "Module 12: Physical Security"
date: 2026-09-30
lastmod: 2026-10-10
toc: true
draft: false
description: "Plan for device theft, travel, emergency access, observation, recovery, and media disposal with jurisdiction-aware biometric choices using repeatable checks."
genre: ["Personal Security", "Physical Security", "OPSEC", "Privacy", "Device Seizure"]
tags: ["physical security", "device seizure", "shoulder surfing", "skimmer", "cctv", "biometrics", "kensington lock", "document disposal", "public records", "biometric coercion", "privacy screen", "personal security course"]
cover: "/img/cover/physical-security-workspace-tech-measures.webp"
coverAlt: "A digital illustration of a secure workspace featuring a laptop with a cable lock, a privacy screen, and a shredder filled with shredded documents. Surrounding elements include biometric devices."
coverCaption: "Module 12: the layer no software reaches"
---

[← Return to the Personal Security Course](/personal-security-course-start/)

**Physical access changes the risk.** An unlocked device exposes active sessions. Full-disk encryption still protects powered-off storage when keys and recovery material stay unavailable. A stolen phone also threatens factors and recovery paths stored on the device.

This final module covers device control, document disposal, observation, and the biometric question which depends on your legal situation rather than your preferences.

*Budget about 25 minutes. The device and biometric decisions are the ones with lasting consequences.*

## What You Will Learn

- **Assess** the difference between theft risk and seizure risk
- **Apply** physical controls proportionate to where you carry devices
- **Dispose** of documents and media without leaving recoverable data
- **Recognize** observation techniques including shoulder surfing and card skimming
- **Evaluate** biometrics against a PIN for your own legal circumstances
- **Produce** a physical security record and a completed course summary

| Term | Meaning |
|---|---|
| **Seizure** | Lawful or unlawful taking of a device by another party |
| **Shoulder surfing** | Reading a screen or keypad from a position you did not notice |
| **Skimmer** | A device attached to a card reader to capture card data |
| **Coercion** | Compelling a device unlock rather than defeating encryption |
| **Perimeter** | The physical boundary around a space containing assets |

## Theft and Seizure Are Different Problems

**They overlap, and they drive opposite design decisions.**

| | Theft | Seizure |
|---|---|---|
| **Who acts** | A thief or another person taking the device | A government authority or another party acting under claimed legal power |
| **Primary loss** | The hardware and the data on it | The data and its contents |
| **Control focus** | Custody, powered-off encryption, account recovery, and supported remote lock or wipe | Data minimization, power state, encryption, legal advice, and account recovery |
| **What helps** | Not leaving devices visible, cable locks | Device power state, and knowing your rights |

**Shutting down rather than suspending changes the attack surface.** A suspended device might retain keys in memory. A powered-off encrypted device normally requires an authentication factor or recovery path, subject to platform design, firmware, hardware, credential strength, and implementation flaws.

*Data minimization reduces the amount exposed during theft, seizure, or account compromise. Record what belongs on each travel or daily-use device.*

## Devices in the Physical World

- **Use cable locks** where a device is left in a semi-public place, such as an office or a library
- **Keep devices out of sight** in vehicles, and treat a charging cable on a seat as a signal something is under it
- **Carry a privacy screen** where side viewing matters, then test its viewing angles under normal lighting
- **Enroll remote lock or wipe** and confirm the device appears in the vendor console. Test on a spare device or follow a documented vendor test. Do not wipe a primary device as a drill
- **Do not charge from unknown USB ports**, as Module 7 covered. Prefer your own adapter

**A short idle lock timeout reduces unattended unlocked time.** Full shutdown and encryption address powered-off storage. Physical custody and account recovery address theft.

## Documents and Disposal

**Physical documents carry data which no encryption protects.**

| Item | Disposal Approach |
|---|---|
| **Financial statements** | Shred, cross-cut rather than strip-cut |
| **Identity documents** | Shred, and treat replacement as the better option where available |
| **Medical records** | Shred because they might contain health and identifying data |
| **Old storage media** | Use an approved clear, purge, cryptographic erase, or destroy method suited to the media and data. Reuse is valid after verified sanitization |
| **Delivery labels** | Remove or obscure before discarding packaging |

**Watermark documents you share** with the recipient and date when suitable. A watermark might identify the intended copy after a leak, though removal, cropping, retyping, screenshots, and shared copies limit attribution.

*Cross-cut shredding matters. Strip-cut shredders produce strips which are straightforward to reassemble.*

## Observation, and the Biometric Question

**Being observed is subtle, and the countermeasures are simple.**

- **Shield the keypad** when entering a PIN, and clean the screen afterwards on touch devices where smudges reveal digits
- **Inspect card readers and ATMs** for attached skimming hardware, and prefer readers which look untouched
- **Notice who is positioned to see your screen**, and reposition rather than assuming nobody is looking

**The biometric decision depends on your legal exposure, not your convenience.**

| Method | Strength | Consideration |
|---|---|---|
| **Biometric** | Convenient, and difficult to guess | In some jurisdictions, compelling a finger or face carries different protections than compelling a passphrase |
| **PIN or passphrase** | Knowledge you hold | Slower, and vulnerable to observation |

**Seek current local legal guidance for compelled access, border searches, and seizure.** Rules differ by jurisdiction and facts. Learn the vendor's temporary biometric-disable action, and choose a PIN, passphrase, biometric, or combination from both safety and legal needs.

*Biometric traits are observable and difficult to replace after compromise. A face image is not the same as a reusable biometric template, liveness signal, or device credential. Compare the actual authentication design and recovery path.*

## Reducing Ongoing Exposure

Two items deserve attention because they persist without your involvement.

**Crowdsourced and commercial image collection records public activity.** A friend's public post might reveal your location even when you post nothing. Choose travel routes from personal safety, accessibility, legality, and time. Camera avoidance alone is not a safe route plan.

**Camera and facial-recognition deployment varies by city, operator, venue, and law.** Use current local sources to understand coverage relevant to your safety plan. Do not choose an unsafe route solely to avoid a camera.

*Our sibling project mapping ALPR camera locations illustrates how much surveillance infrastructure is publicly inferable: **[Flock Finder](/sibling-sites/)**. Knowing the density near you is a starting point for planning, not a complete solution.*

{{< figure src="physical-security-device-documents-observation.webp" alt="Diagram grouping physical security controls into devices, documents, and observation, showing encryption and remote wipe for devices, shredding and watermarking for documents, and observation countermeasures" >}}

## The Physical Record

```text
PHYSICAL SECURITY RECORD
Devices:
  Idle lock timeout:      ______________________
  Remote wipe tested:     yes / no
  Cable lock in use:      yes / no / n/a
  Privacy screen:         yes / no
  Full power-off habit:   yes / no

Documents:
  Shredder type:          cross-cut / strip-cut / none
  Documents watermarked:  yes / no
  Media destruction plan: ______________________

Observation:
  Lock method:            PIN (length __) / passphrase / biometric
  Biometrics disabled when needed: how? __________
  ATM and reader checks:  habit / sometimes / never

Exposure:
  CCTV awareness near home/work: reviewed / not reviewed
```

## Practice and Verify

Use a spare device for remote-lock or wipe drills. A primary device needs a documented recovery path before any test.

1. Set a short idle lock and confirm the screen locks after the chosen delay.
2. Confirm the device appears in the vendor's find-device console.
3. Send a harmless locate, sound, or lock action to a spare device.
4. Confirm backup and account recovery before considering any wipe test.
5. Choose one retired storage item and select clear, purge, cryptographic erase, or destruction from an approved method.
6. Write a travel and theft card with emergency contact, carrier, insurer, device serial location, and local reporting route.

> **Expected Result:** the spare device receives the selected action, the learner reaches recovery material without using the primary device, and the disposal method matches the media and data sensitivity.

If the device does not appear, check account ownership, network access, location settings, and vendor enrollment. Do not erase the device while diagnosis continues. If legal seizure, border search, or compelled access drives the threat model, obtain current advice for the relevant jurisdiction.

```text
REDACTED EXAMPLE
Idle lock:            2 minutes, verified
Find-device console:  primary and spare listed
Spare lock test:      passed
Recovery route:       trusted contact plus offline record
Retired SSD:          vendor purge method, result logged
Travel card:          stored with companion
```

**Pass checklist**

- [ ] Idle lock and find-device enrollment have observed evidence
- [ ] No primary device was wiped as a drill
- [ ] Emergency and accessibility access survive the selected lock plan
- [ ] Media disposal follows a current approved method
- [ ] Jurisdiction-specific advice is labeled and sourced locally

**Primary references, checked 2026-10-10:** [NIST SP 800-88 Rev. 2 media sanitization](https://csrc.nist.gov/pubs/sp/800/88/r2/final) and the device vendor's current find-device and recovery documentation.

## Course Summary: All Twelve Modules

**You have now covered the full sequence.** This table is the compressed version of the course.

| Module | The one action which matters most |
|---|---|
| **1. Authentication** | Move email and finance accounts to a passkey or hardware key |
| **2. Web Browsing** | Block third-party cookies and install one content blocker |
| **3. Email** | Turn off automatic remote content loading |
| **4. Messaging** | Enable contact verification and disappearing messages |
| **5. Social Media** | Remove birthday, school, and employer from your profile |
| **6. Networks** | Change the router admin password and disable WPS and UPnP |
| **7. Mobile Devices** | Set a carrier PIN and port freeze |
| **8. Personal Computers** | Confirm disk encryption and restore one file from backup |
| **9. Smart Home** | Move IoT devices to a separate network segment |
| **10. Personal Finance** | Freeze the relevant US credit files |
| **11. Human Aspect** | Save verified contact numbers and agree a signal with family |
| **12. Physical Security** | Shorten the idle lock timeout and shut devices down fully |

## Next Steps

1. **Return to the course hub** and review your completed records: **[Personal Security Course](/personal-security-course-start/)**
2. **Read the four-tier summary** for the whole course on one page: **[Prioritized Personal Security Checklist](/articles/personal-security-checklist-prioritized-2026/)**
3. **Go deeper with a community checklist** if you want several hundred items: **[Personal Security Checklist by Alicia Sykes](https://github.com/Lissy93/personal-security-checklist)**
4. **Apply the organizational checklists** if you also manage systems: **[Every Checklist](/checklists/)**
5. **Use the local tools** for anything involving a secret: **[All Client-Side Tools](/tools/)**
6. **Revisit your threat model** annually, since circumstances and adversaries change: **[How to Form Your Own Personal Threat Model](/articles/how-to-form-your-own-personal-threat-model-safeguard-online-security/)**
