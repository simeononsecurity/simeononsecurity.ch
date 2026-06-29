---
title: "CompTIA SecOT+ (SOT-001): OT Security Operations"
date: 2025-01-01
toc: true
draft: false
description: "Master OT security operations for the CompTIA SecOT+ SOT-001 exam. Learn asset inventory and discovery, data collection with SIEM and SOAR, baselining and threat hunting, vulnerability management, patching with compensating controls, and removable media security."
genre: ["CompTIA SecOT+ Course", "OT Security Operations", "Asset Inventory", "SIEM", "Vulnerability Management", "Threat Hunting", "Patch Management", "Operational Technology", "SOT-001", "Cybersecurity"]
tags: ["CompTIA SecOT+", "SOT-001", "asset inventory", "passive discovery", "active discovery", "configuration management database", "SIEM", "SOAR", "baselining", "threat hunting", "patch management", "compensating control", "software bill of materials", "vulnerability triage", "removable media scanning", "write blocker", "sanitization kiosk"]
cover: "/img/cover/comptia-secot-ot-security-operations-control-room.webp"
coverAlt: "A high-tech control room showing professionals analyzing network traffic and asset inventories on multiple screens, with a dark navy background and vibrant blue and green accents."
coverCaption: "Run Day-to-Day OT Security Operations for the SOT-001 Exam"
---

#### [Click Here to Return To the CompTIA SecOT+ Course Page](/secot-plus-start/)

**OT Security Operations** is **22%** of the **CompTIA SecOT+ (SOT-001)** exam, making it the most heavily weighted domain. This is the daily work of keeping an OT environment secure. You discover and track assets, collect and analyze data, hunt for threats, and manage vulnerabilities in systems you often cannot simply patch. *Spend the most study time here. Visibility is the foundation, because you cannot protect an asset you do not know exists.*

OT operations differ from IT operations because uptime and safety constrain everything. You cannot reboot a turbine to apply a patch, so you lean on compensating controls and carefully scheduled downtime.

## Asset Inventory and Discovery

You cannot secure what you cannot see, so inventory comes first. You discover assets, create the inventory, validate it, and maintain it over time.

| Method | How It Works |
|--------|--------------|
| **Passive discovery** | Identifies assets by observing network traffic without probing |
| **Active discovery** | Identifies assets by querying or scanning them |
| **Manual discovery** | Identifies assets through physical inspection and records |

*Prefer passive discovery in OT. Active scanning can disrupt fragile devices, so you watch traffic rather than probe whenever possible.*

The inventory is only useful if it is rich and current.

- **Creation** builds the first complete list of assets.
- **Validation** confirms the inventory matches reality through walkdowns and cross-checks.
- **Maintenance** keeps the inventory accurate as assets change.
- **Key attributes** capture each asset's IP, MAC, model, firmware, location, and owner.
- A **software inventory** records installed software and versions on each asset.
- A **configuration management database (CMDB)** stores asset configuration and maps relationships between assets.
- A **collection management framework** documents what data is collected, from where, and how.

## Data Collection and Analysis

You gather data from three layers and analyze it for signs of trouble. The exam groups log sources by where they live.

**Control system data** comes from the process itself.

- **Process logs** record control system events and values.
- **Change logs** capture configuration and logic changes.
- **Function codes** in protocols like Modbus reveal what command was issued.
- A **historian** holds time-series process data for trending.

**Network and boundary data** comes from the wire.

- A **packet capture (pcap)** records raw network traffic for analysis.
- **Syslog** forwards and stores log messages.
- **IDS**, **firewall**, **switch**, **router**, and **edge** logs show boundary activity.

**Host and security data** comes from endpoints and identity systems.

- **AAA and access logs** record authentication and authorization.
- **EDR** and **EPP** report endpoint activity and detections.
- **OS and application logs** and **identity logs** round out host visibility.

You centralize and act on this data with two platforms. **Security information and event management (SIEM)** aggregates and correlates security logs, and **security orchestration, automation, and response (SOAR)** automates security workflows.

You then turn data into detection.

- **Baselining** establishes normal behavior so deviations stand out.
- **Threat hunting** proactively searches collected artifacts for undetected threats.
- **Tuning** refines detection by adjusting **IDS rules**, **firewall rules**, **network performance monitoring**, **EPP and EDR policy**, and **SIEM and SOAR** logic to cut false positives.

## Vulnerability Management

You find weaknesses, decide which matter, and confirm they are fixed. You identify vulnerabilities through both **external** and **internal** assessment.

You detect them with three approaches, choosing the least disruptive for the asset.

- **Passive detection** finds vulnerabilities by observing traffic and configurations.
- **Active detection** scans or probes a system directly.
- **Derived detection** infers vulnerabilities from inventory and known advisories.

You source vulnerability data from a **software bill of materials (SBOM)**, **vendor advisories**, and the **National Vulnerability Database (NVD)**.

You then triage by real exposure, not raw score alone.

| Factor | Question It Answers |
|--------|---------------------|
| **Exposure** | How reachable is the asset by a threat? |
| **Relevance** | Does the vulnerability apply to this configuration? |
| **Exploitability** | How easily can the flaw be used? |
| **Severity** | How serious is the flaw on its own? |
| **Impact** | What happens to the process if it is exploited? |

After remediation, **remediation verification** confirms the fix actually resolved the issue.

## Patching and Remediation

Patching OT is hard, so you evaluate every fix before you touch production. You first confirm the patch is viable.

- **Availability** asks whether a patch even exists.
- **Applicability** asks whether it applies to your version and configuration.
- **Viability** asks whether you can deploy it without breaking the process.
- **Dependency** asks what else must change for the patch to work.

When a patch is not viable, you reach for alternatives and disciplined process.

- A **mitigating control** reduces the impact of a vulnerability when patching is not possible.
- A **compensating control** substitutes for an impractical primary control.
- **Version management** tracks software and firmware versions.
- **Stakeholder coordination** aligns engineers, operators, and owners before a change.
- **Scheduling downtime** arranges maintenance windows to apply changes safely.
- **Testing** and **process validation** prove the change works and the process still runs correctly.
- A **rollback plan** prepares a way to revert a change that fails.

*When you cannot patch a vulnerable PLC, you wrap it in compensating controls such as tighter segmentation and monitoring. The risk is reduced even though the flaw remains.*

## Portable and Mobile Device Security

Removable media and portable tools are a major OT threat vector, so you control them tightly across their whole life cycle.

For **removable media**, you apply a chain of controls.

- **Scanning kiosks** and **anti-malware** check media for malware before use.
- **Dedicated devices** are reserved for a single purpose to limit cross-contamination.
- **Authorization**, **tracking**, and **procurement** control which media enter the environment.
- **Tamper-proofing**, **secure storage**, and a **write blocker** protect integrity and evidence.
- **Sanitization**, **destruction**, and **data loss detection** handle media at end of life.

For **mobile devices**, you manage who and what connects.

- Devices include **corporate** and **third-party** hardware, **calibration equipment**, **phones**, **tablets**, and **wearables**.
- **Device-to-network authentication** proves a device is allowed before it joins.
- **Security validation** and **posture checks** confirm a device meets requirements before it connects.
- **External connections** are controlled whether **persistent** or **temporary**, and **geolocation** can restrict where a device is allowed to operate.

## Next Steps

With operations running, continue to [OT Incident Management](/secot-plus/ot-incident-management/) to prepare for when prevention fails. Return anytime to the [CompTIA SecOT+ Course](/secot-plus-start/).
