---
title: "OT, ICS, and PLC Cybersecurity Is a Problem Industry Cannot Honestly Solve"
draft: false
toc: true
date: 2026-06-26
description: "A professional opinion on why OT, ICS, and PLC cybersecurity guidance cannot keep pace with the actual problem. The systems were never designed to be secured. Compliance with written standards is not the same as being secure."
tags: ["OT security", "ICS security", "PLC security", "IoT security", "industrial cybersecurity", "SCADA security", "NIST 800-82", "IEC 62443", "NERC CIP", "operational technology", "critical infrastructure", "analog sensors", "air gap", "legacy systems", "cybersecurity opinion", "industrial control systems", "SCADA", "Stuxnet", "control system security", "cyber-physical security", "supply chain security", "OT supply chain"]
---

I have spent enough time in industrial environments to say this plainly: most OT, ICS, and PLC cybersecurity programs are theater. They produce compliance documentation. They do not produce security. The gap between the two is where critical infrastructure gets hit.

This is not an attack on the people writing standards. NIST SP 800-82 Rev 3, IEC 62443, and NERC CIP are technically sound documents. The problem is not the guidance. The problem is what the guidance is applied to.

## The Systems Were Built to Work, Not to Be Secured

PLCs, SCADA systems, distributed control systems (DCS), and legacy industrial IoT hardware were designed for one thing: run reliably for a very long time. Availability was the only design goal worth discussing. Confidentiality, integrity, authentication, and logging were not requirements. In many cases they were not even concepts on the table when these systems were engineered.

NIST SP 800-82 Rev 3 (2023) is honest about this. It describes OT environments as having "unique performance, reliability, and safety requirements" where "security cannot interfere with system operation." Read that again. The primary security guidance document for operational technology explicitly acknowledges that security comes second. This is not a flaw in the document. It is an accurate description of the environment.

You cannot apply role-based access control to a PLC with no concept of user roles. You cannot patch firmware on hardware whose manufacturer no longer exists. Legacy serial protocols, Modbus RTU and Profibus DP among them, provide no native authentication. They transmit commands and data to whoever asks. There is no verification of who is asking.

The guidance is sound. The systems often are not capable of receiving it. These are not the same problem.

## There Are Two Completely Different Categories of OT Systems

Legacy PLCs from the 1980s through the early 2000s were designed for isolated, physical-only operation. They run proprietary operating systems. They are often managed from engineering workstations that also touch corporate networks. Their configurations are stored in formats with no integrity verification. These systems represent a significant portion of deployed infrastructure in water treatment, energy generation, manufacturing, and transportation.

Modern security-capable controllers are different. Siemens, Schneider, Rockwell, Beckhoff, and Phoenix Contact now ship platforms with secure boot, signed firmware, role-based access control, TPM-backed identity, and encrypted communications. EtherNet/IP CIP Security, PROFINET Security Class, and OPC UA with authentication exist as shipping features on current hardware.

I am not dismissing modern OT security engineering. Progress is real. The problem is that most of the deployed base is not modern. When people say "OT cybersecurity," they are usually describing someone trying to secure a 20-year-old programmable controller with a cybersecurity framework written in 2023. That is the gap I am talking about.

## What Actually Works

Physical security and network isolation are the most reliable controls available for legacy OT environments. Every major ICS security framework says the same thing. IEC 62443 organizes OT environments into security zones with defined conduits. The intent is to make lateral movement require passing through controlled boundaries rather than sliding across a flat network.

Network isolation reduces the network-based attack surface substantially. It does not eliminate all risk. Removable media, insider access, maintenance laptops, temporary engineering connections, and supply chain compromise all represent documented entry paths into systems with no network exposure. Stuxnet, which reached air-gapped Iranian centrifuge facilities via infected USB drives, is the canonical example of this. Network isolation is necessary. It is not sufficient.

Human-in-the-loop monitoring of physical process parameters remains one of the most reliable detection mechanisms available. A trained operator watching pressure, temperature, and flow in real time will notice things that no intrusion detection system will see, because the IDS cannot verify whether the digital value matches physical reality.

Controls that reduce risk in the right contexts:

- Data diodes allow telemetry out without allowing any inbound connections
- Application whitelisting on HMI workstations restricts what executes on machines with access to control systems
- Passive anomaly detection platforms from Claroty, Dragos, and Nozomi analyze traffic without touching control plane communications
- Network segmentation between OT zones slows lateral movement without requiring full air gaps
- Zero trust principles, referenced in NIST SP 800-82 Rev 3, add per-session verification requirements to some modern OT architectures

None of these solve the underlying design constraints. They reduce risk at the edges of systems that were never built for this.

## Analog Signals Cannot Be Authenticated

4-20mA current loops, 0-10V signals, thermocouple outputs, and RTD readings transmit as varying electrical signals. There is no mechanism in the physical signal to verify authenticity. Anyone who puts the right signal on the wire gets believed.

Stuxnet made this concrete. The attack manipulated PLC logic executing on the Siemens S7 controllers while simultaneously replaying previously recorded normal process data to operator interfaces. The operators watched screens showing normal readings while the centrifuges were being driven past their operational limits. The deception held long enough to cause physical damage that appeared as equipment failure rather than an attack.

Electromagnetic interference from power cables, variable frequency drives, lightning, and improper grounding corrupts analog measurements in normal operation. IEC 61000 exists because of this. Industrial installations use shielded cabling, proper grounding, filtering, and physical separation to manage it. Strong electromagnetic interference will corrupt readings. This is why the engineering controls exist.

Modern smart field devices convert analog measurements to digital form internally before transmitting over HART-IP, WirelessHART, EtherNet/IP CIP Security, or OPC UA. Authenticated digital communications are available at the device level on modern hardware. The analog 4-20mA wire connecting a legacy transmitter to a legacy PLC input carries no authentication and never will. For a significant portion of deployed instrumentation, this is still the wire in use.

## Sensor Validation Is a Safety Control, Not a Security Control

Process safety systems perform redundant sensor voting. A 2-of-3 arrangement with two sensors reading 230 PSI and one reading 14 PSI flags the outlier. This provides limited resilience against single-point sensor manipulation. It is a safety engineering control, not a cybersecurity control.

Standard PLCs have no cryptographic validation for their analog inputs. A signal generator injected on the loop is indistinguishable from a legitimate transmitter. The PLC reads the current and acts on it.

Safety Instrumented Systems were supposed to be the independent last line of defense. In 2017, TRITON (also known as TRISIS) targeted Schneider Electric Triconex SIS units with the specific goal of disabling that layer. The attackers reached the safety system through the engineering workstation network. The independence of the layer depended on network separation that had not been maintained.

IEC 62443-3-3, IEC 62443-4-2, and the coordination with functional safety under IEC 61511 now reflect this lesson. For years, process safety and cybersecurity were treated as separate disciplines by separate groups. TRITON demonstrated in practice what independent analysis had argued in theory: an attacker who neutralizes the safety system before triggering the hazardous condition removes the last control preventing physical consequences.

## Your Supply Chain Is the Vector You Are Probably Ignoring

Most OT security programs focus on network architecture. Most OT compromises in recent years have used entry points that network architecture does not stop.

OT supply chain risk includes:

- Firmware integrity before installation, specifically whether hardware arrives with unverified firmware from the factory or distributor
- Vendor remote access sessions, which remain persistent exposures at sites that rely on manufacturer support
- Engineering workstations that connect to both the corporate network and the OT network, often because it is operationally convenient
- The absence of software bills of materials (SBOMs) for most legacy OT deployments, making software component tracking largely impossible
- Maintenance contractors who bring laptops and USB drives into operationally isolated environments
- Signed firmware update support, which most older platforms do not have

NIST SP 800-82 Rev 3 dedicates specific sections to vendor dependencies and third-party access. If your air gap is intact internally but your equipment vendor maintains a persistent remote access portal into your engineering network, you do not have an air gap. You have a gap with a door in it that someone else controls.

## Hardening Legacy Systems Costs More Than It Should

Each PLC program is custom-written for a specific process. The logic that runs a refinery's surge control system differs entirely from the logic that runs a water treatment chlorination sequence or a turbine governor. This is not a choice. Physical processes are different.

Hardening legacy OT systems frequently costs more than anticipated because of engineering validation requirements, necessary downtime, vendor support constraints, documentation gaps, and testing cycles that exceed initial estimates. In some cases involving hardware with no vendor support, hardening costs approach or exceed the replacement cost of the system. This is not typical across all OT environments, but it is common enough to be a planning factor.

NERC CIP compliance for bulk electric system cyber assets costs individual utilities millions of dollars per year. A 2019 survey from the American Public Power Association documented compliance costs ranging widely, with smaller utilities reporting disproportionate burden relative to their scale. Many water systems and smaller utilities operate outside NERC CIP requirements entirely and face no comparable compliance obligation.

## The Systems Should Be Replaced

Replacing legacy OT systems is the right answer. At large facilities this means tens of millions of dollars, extended transition periods, and the risk of encoding complex operational knowledge incorrectly during migration. These are real costs and real risks.

What industry guidance actually recommends, through CISA and ICS-CERT, is applying compensating controls while replacement planning proceeds. This is a rational response to the constraints. Read plainly, it acknowledges that full security is not achievable on legacy equipment, so apply the controls that fit and plan for eventual replacement.

The practical reality is that many of these systems will remain in service for decades. This is a funding and policy problem. The technical community has been clear about what needs to happen. The operational budgets and replacement schedules have not kept pace.

## Adding Network Connectivity to OT Systems Often Makes Things Worse

Many organizations have added remote access and monitoring capabilities to OT environments that were originally isolated. The operational argument is straightforward: remote visibility reduces response time, and vendor support is faster with a remote connection. The security consequence is that isolated systems with no remote attack surface now have one.

The 2021 Oldsmar water treatment incident happened through a TeamViewer remote access connection. The attacker changed sodium hydroxide dosing settings through a legitimate remote access tool that had been added for convenience. The Colonial Pipeline incident in 2021 began with an IT network compromise. The operator shut down OT pipeline operations proactively because they could not confirm the OT network was unaffected. The attack did not breach the OT network directly. The uncertainty about whether it had been breached caused the shutdown.

Adding network connectivity to legacy OT systems for operational benefit, without engineering that connectivity to appropriate standards, produces more risk than the benefit justifies in many cases. The Purdue Model, while useful as a reference architecture, is no longer treated by NIST as sufficient on its own. Modern IIoT, cloud connectivity, remote operations, and hybrid architectures require more deliberate design than zone segmentation alone provides.

## Compliance With Written Standards Is Not Security

NIST SP 800-82 Rev 3, IEC 62443, and NERC CIP describe the right controls for what these systems are. I am not dismissing them. I am pointing out what they say explicitly: not every OT system can implement every control. The frameworks use tiered security levels and compensating control provisions precisely because the systems they apply to frequently cannot meet the full requirements.

The gap between what the standards describe and what a given legacy deployment can achieve is not a documentation error. The systems do not support the controls. The guidance acknowledges this. Achieving a compliant audit result on legacy OT does not mean the environment is secure. It means you documented what compensating controls are in place, and an auditor accepted them.

NIST's risk management framework is explicit that residual risk remains after controls are applied. Risk acceptance is one of the four outcomes in the framework alongside risk transfer, risk reduction, and risk avoidance. Acknowledgment of residual risk is baked into the official guidance. When someone tells you that meeting compliance requirements makes your OT environment secure, they are saying something the frameworks they are referencing do not support.

## What You Should Do With Legacy OT

If you operate legacy OT environments:

- Treat network isolation as your primary control and audit everything that crosses the OT boundary
- Give your engineering workstations their own hardening plan. They touch both worlds and are frequently the entry point
- Control and log all removable media in OT areas
- Audit vendor remote access and close every session that is not actively in use
- Implement redundant sensor monitoring where the process design allows
- Build a replacement timeline with real cost estimates, even if replacement is years away
- Stop treating compliance audit completion as a security milestone

If you are procuring new OT systems:

- Write security requirements into the procurement specification before vendors respond
- Choose platforms with documented support for authenticated communications, signed firmware updates, and role-based access control
- Design IT/OT boundaries as explicit conduits per IEC 62443, not as a vague "keep them separate" policy
- Require SBOMs for OT software components as a contract deliverable

The industry has documented the problem well. The standards are technically accurate. The systems in the field frequently cannot receive what the standards prescribe. Acknowledging that openly is the starting point for making decisions about how to manage the risk that remains.

## References

- NIST SP 800-82 Rev 3: Guide to Operational Technology (OT) Security (2023)
- IEC 62443: Industrial Automation and Control Systems Security series
- IEC 62443-3-3: System security requirements and security levels
- IEC 62443-4-2: Technical security requirements for IACS components
- IEC 61511: Functional Safety for Safety Instrumented Systems
- NERC CIP: Critical Infrastructure Protection standards for the bulk electric system
- IEC 61000: Electromagnetic Compatibility standards
- CISA ICS-CERT Advisories and Best Practices
- MITRE ATT&CK for ICS framework
- Stuxnet technical analysis, Langner Communications, 2011
- TRITON/TRISIS technical analysis, Dragos, 2017
- Oldsmar Water Treatment incident review, CISA, 2021
- American Public Power Association NERC CIP Compliance Cost Survey, 2019
