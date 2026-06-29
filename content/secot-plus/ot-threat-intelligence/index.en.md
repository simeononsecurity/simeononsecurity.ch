---
title: "CompTIA SecOT+ (SOT-001): OT Threat Intelligence"
date: 2025-01-01
toc: true
draft: false
description: "Master OT threat intelligence for the CompTIA SecOT+ SOT-001 exam. Learn intelligence disciplines, analysis models like the Diamond Model and MITRE ATT&CK for ICS, landmark OT malware including Stuxnet and TRISIS, threat actors, attack techniques, and intelligence sharing."
genre: ["CompTIA SecOT+ Course", "OT Threat Intelligence", "MITRE ATT&CK for ICS", "ICS Malware", "Stuxnet", "Threat Actors", "Cyber Kill Chain", "Operational Technology", "SOT-001", "Cybersecurity"]
tags: ["CompTIA SecOT+", "SOT-001", "threat intelligence", "MITRE ATT&CK for ICS", "ICS Cyber Kill Chain", "Diamond Model", "Stuxnet", "TRISIS", "Industroyer", "BlackEnergy", "FrostyGoop", "Colonial Pipeline", "advanced persistent threat", "indicator of compromise", "STIX", "ISAC", "IT to OT pivot"]
cover: "/img/cover/comptia-secot-plus-ot-threat-intelligence.webp"
coverAlt: "A dark control room with glowing screens showing threat intelligence data. A cybersecurity analyst is focused on the screens, surrounded by colorful graphs and icons representing various attack techniques."
coverCaption: "Understand the Adversaries Targeting OT for the SOT-001 Exam"
---

#### [Click Here to Return To the CompTIA SecOT+ Course Page](/secot-plus-start/)

**OT Threat Intelligence** is **14%** of the **CompTIA SecOT+ (SOT-001)** exam. This domain teaches you who attacks OT, how they operate, and how you turn raw information into intelligence that drives defense. *Real OT attacks are rare but consequential, so you study the landmark cases closely because they define the techniques you must detect.*

Threat intelligence is the difference between guarding everything equally and guarding what an actual adversary is likely to target. You map your defenses to known behavior, not to imagination.

## Intelligence Disciplines

Intelligence is gathered from distinct sources.

| Discipline | Source |
|------------|--------|
| **HUMINT** | Human sources and people |
| **SIGINT** | Intercepted communications and signals |
| **OSINT** | Publicly available sources |
| **IMINT** | Photographs and other imagery |
| **MASINT** | Technical sensor measurements and signatures |

## Analysis Models

You structure analysis with proven models.

- The **Diamond Model** links adversary, capability, infrastructure, and victim.
- The **intelligence life cycle** repeats planning, collection, analysis, and dissemination.
- **MITRE ATT&CK for ICS** catalogs adversary tactics and techniques against industrial control systems.
- The **ICS Cyber Kill Chain** describes the stages of an attack against industrial control systems.

*MITRE ATT&CK for ICS is the OT-specific companion to the enterprise ATT&CK matrix. Learn it as your shared language for describing OT attacker behavior.*

## Landmark OT Threats

These real incidents shaped the field and appear throughout the exam.

| Threat | What it did |
|--------|-------------|
| **Stuxnet** | Physically damaged Iranian centrifuges by manipulating PLCs |
| **TRISIS** | Targeted a safety instrumented system to disable safety functions |
| **BlackEnergy** | Contributed to power outages in Ukraine |
| **Industroyer** | Manipulated electric grid substation equipment |
| **FrostyGoop** | Targeted OT controllers over the Modbus protocol |
| **Colonial Pipeline** | A ransomware incident that disrupted fuel distribution |

*TRISIS stands out as the first known malware to target a safety instrumented system. Attacking the last safety barrier turns a cyber event into a potential physical disaster.*

## Threat Actors

You profile the adversary to anticipate their behavior.

- A **nation-state actor** is a well-resourced attacker working for a government.
- An **advanced persistent threat** is a stealthy, long-term, capable intruder.
- A **hacktivist** is motivated by political or social causes.
- A **cybercriminal** is motivated primarily by financial gain.
- An **insider threat** comes from people inside the organization who misuse access.

## Attack Techniques

OT attackers use techniques you must recognize.

- A **removable media threat** carries malware on USB drives and portable storage, a common way into air-gapped OT.
- **Phishing** and **vishing** use deceptive messages or voice calls to steal access.
- **Lateral movement** is moving between systems after initial access.
- An **IT to OT pivot** is crossing from the IT network into the OT network, the classic path into a plant.
- A **rogue base station** is a fake cellular tower used to intercept communications.

## Sharing and Consuming Intelligence

You exchange intelligence in standard formats and through trusted channels.

| Tool | Role |
|------|------|
| **Indicator of compromise** | An observable artifact that suggests a breach |
| **YARA** | A rule format for identifying and classifying malware |
| **STIX** | A standard format for sharing threat intelligence |
| **ISAC** | An Information Sharing and Analysis Center for a sector |
| **Threat intelligence feed** | A stream of current threat data and indicators |

You also describe an actor's **tactics, techniques, and procedures** to characterize their behavior, and you use **bug bounty** programs and **OEM threat feeds** to gather more.

## Next Steps

With the adversary understood, continue to [OT Cybersecurity Architecture, Design, and Engineering](/secot-plus/ot-cybersecurity-architecture-design-engineering/) to build defenses against these threats. Return anytime to the [CompTIA SecOT+ Course](/secot-plus-start/).
