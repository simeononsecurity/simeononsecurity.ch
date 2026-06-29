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

Intelligence is gathered from distinct sources, each with its own discipline.

| Discipline | Source |
|------------|--------|
| **HUMINT** | Human sources and people |
| **SIGINT** | Intercepted communications and signals |
| **MASINT** | Technical sensor measurements and signatures |
| **OSINT** | Publicly available open sources |
| **IMINT** | Photographs and other imagery |

## Analysis Models

You structure analysis with proven models so findings are consistent and shareable.

- The **Diamond Model** links adversary, capability, infrastructure, and victim for a single intrusion.
- The **intelligence life cycle** repeats planning, collection, processing, analysis, and dissemination.
- **MITRE ATT&CK for ICS** catalogs adversary tactics and techniques against industrial control systems.
- The **ICS Cyber Kill Chain** describes the two stages of an attack against industrial control systems, the intrusion stage and the attack development and execution stage.

*MITRE ATT&CK for ICS is the OT-specific companion to the enterprise ATT&CK matrix. Learn it as your shared language for describing OT attacker behavior.*

## Landmark OT Threats

The exam splits real incidents into two groups. **Direct** threats were built to attack OT and ICS. **Indirect** threats hit IT or supply chains but still disrupted physical operations.

These **direct** incidents targeted control systems on purpose.

| Direct Threat | What It Did |
|---------------|-------------|
| **Stuxnet** | Physically damaged Iranian centrifuges by manipulating PLCs |
| **TRISIS (Triton)** | Targeted a safety instrumented system to disable safety functions |
| **BlackEnergy 2/3** | Contributed to power outages in Ukraine |
| **Industroyer** | Manipulated electric grid substation equipment directly |
| **FrostyGoop** | Targeted OT controllers over the Modbus protocol |

*TRISIS stands out as the first known malware to target a safety instrumented system. Attacking the last safety barrier turns a cyber event into a potential physical disaster.*

These **indirect** incidents disrupted operations without directly compromising the control logic.

| Indirect Threat | What It Did |
|-----------------|-------------|
| **Colonial Pipeline** | A ransomware incident on IT that forced a precautionary pipeline shutdown |
| **SolarWinds** | A supply chain compromise of a widely used management platform |
| **Maersk (NotPetya)** | Wiper malware that crippled global shipping and logistics |
| **AcidRain** | Wiper malware that bricked satellite modems and disrupted communications |
| **2024 CrowdStrike outage** | A faulty software update that caused widespread operational disruption |
| **Collins Aerospace / RTX** | A supply chain incident affecting aviation systems |

*The lesson of the indirect cases is that you do not need malware on a PLC to halt a process. An IT outage, a vendor compromise, or a precautionary shutdown can stop operations just as effectively.*

## Threat Actors

You profile the adversary to anticipate their behavior and motivation.

| Actor | Motivation |
|-------|------------|
| **Nation-state / APT** | Strategic disruption, sabotage, and espionage with deep resources |
| **Hacktivist** | Political or social causes |
| **Cybercriminal** | Financial gain through extortion and ransomware |
| **Insider (intentional)** | Deliberate misuse of authorized access |
| **Insider (unintentional)** | Accidental harm from error or negligence |

An **advanced persistent threat (APT)** is a stealthy, long-term, well-resourced intruder, usually a nation-state, that pursues **espionage** or sabotage over months or years.

## Threat Vectors

OT attackers reach their target through vectors you must recognize and close.

- **Remote access** abuse through third-party or internal connections.
- **Removable media** carrying malware on USB drives into air-gapped OT.
- **Social engineering** including **phishing** email and **vishing** voice calls.
- **Account compromise** using stolen or weak credentials.
- **Supply chain** tampering, including malicious **firmware**.
- **Lateral movement** between systems after initial access.
- An **IT-to-OT pivot** crossing from the IT network into the OT network, the classic path into a plant.
- **Unauthorized devices** connected to the OT network without approval.
- **Misconfigurations** that leave services exposed.
- **Vulnerability exploitation** against unpatched OT systems.
- **On-path attacks** that intercept and alter traffic between two systems.
- **QR code** lures that redirect a victim to a malicious destination.
- **Cell-based attacks** such as **SIM swapping** and a **rogue base station** that impersonates a cellular tower.

## Indicators and Intelligence Sharing

You exchange intelligence in standard formats and through trusted channels. An **indicator of compromise (IOC)** is an observable artifact that suggests a breach.

Common IOCs include the following.

- **File hashes** of known malicious files.
- **IP addresses** and **malicious domains** used by attackers.
- **Usernames** and **email addresses** tied to an actor.
- **Registry modifications**, **abnormal processes**, and **unusual log entries**.
- **Suspicious sessions** and connections that deviate from the baseline.

You describe an actor's broader behavior with their **tactics, techniques, and procedures (TTPs)**, which are harder to change than a single IOC. You share all of this through standard tooling.

| Tool | Role |
|------|------|
| **YARA** | A rule format for identifying and classifying malware |
| **STIX** | A standard format for sharing structured threat intelligence |
| **Threat intelligence platform** | Software that aggregates, enriches, and operationalizes intelligence |
| **ISAC** | An Information Sharing and Analysis Center for a sector |
| **Threat intelligence feed** | A stream of current threat data and indicators |

You draw from many sources. **Third-party private feeds**, **OEM** vendor advisories, **volunteer** and **bug bounty** reporting, and even **social media** all feed analysis. **ISACs** and **government** advisories provide trusted, sector-specific intelligence.

## Next Steps

With the adversary understood, continue to [OT Cybersecurity Architecture, Design, and Engineering](/secot-plus/ot-cybersecurity-architecture-design-engineering/) to build defenses against these threats. Return anytime to the [CompTIA SecOT+ Course](/secot-plus-start/).
