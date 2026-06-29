---
title: "CompTIA SecOT+ (SOT-001): OT Cybersecurity Architecture, Design, and Engineering"
date: 2025-01-01
toc: true
draft: false
description: "Master OT cybersecurity architecture, design, and engineering for the CompTIA SecOT+ SOT-001 exam. Learn design principles, physical access controls, device hardening, network segmentation, the industrial DMZ, zones and conduits, data diodes, and identity management."
genre: ["CompTIA SecOT+ Course", "OT Architecture", "Network Segmentation", "Industrial DMZ", "Zones and Conduits", "Device Hardening", "Defense in Depth", "Operational Technology", "SOT-001", "Cybersecurity"]
tags: ["CompTIA SecOT+", "SOT-001", "defense in depth", "least privilege", "industrial DMZ", "zones and conduits", "data diode", "unidirectional gateway", "network segmentation", "VLAN", "Secure Boot", "TPM", "jump box", "RBAC", "ABAC", "multifactor authentication", "privileged access management"]
cover: "/img/cover/comptia-secot-cybersecurity-architecture-design.webp"
coverAlt: "An illustration of a cybersecurity architecture for operational technology, featuring elements like firewalls, biometric access controls, and segmented networks, set against a dark background with vibrant colors."
coverCaption: "Design Resilient, Segmented OT Architecture for the SOT-001 Exam"
---

#### [Click Here to Return To the CompTIA SecOT+ Course Page](/secot-plus-start/)

**OT Cybersecurity Architecture, Design, and Engineering** is **18%** of the **CompTIA SecOT+ (SOT-001)** exam. This domain teaches you to build OT systems that resist attack and keep running through one. You apply layered controls, harden fragile devices, and segment the network so a compromise on one side cannot reach the process on the other. *Architecture is where you prevent the IT-to-OT pivot you studied in threat intelligence, so give this heavily weighted domain deep, hands-on attention.*

Good OT architecture assumes a breach will happen. The goal is to contain it, keep the process safe, and keep operators in control.

## Design Principles

You start from sound principles that shape every later decision.

| Principle | Meaning |
|-----------|---------|
| **Least privilege** | Grant only the access needed to function |
| **Least functionality** | Run only the services and features the system requires |
| **Defense in depth** | Layer controls so no single failure is fatal |
| **Compartmentalization** | Isolate parts so a compromise cannot spread freely |
| **Criticality** | Protect the most important assets the most |
| **Simplicity** | Prefer simple designs that are easier to secure and maintain |
| **Interoperability** | Ensure components work together and stay compatible |

**Operational resilience** is the ability to endure and recover from disruption. It is built from four properties you should know.

- **Endurance** keeps the process running under stress.
- **Redundancy** duplicates components that take over on failure.
- **High availability** keeps systems running with minimal downtime.
- **Recoverability** restores service quickly after a failure.

A secure design must also stay observable and predictable. **Auditability** lets you prove what happened, **observability** lets you see system state, and **deterministic** behavior guarantees the system responds within a fixed time.

*Deterministic behavior matters in OT. The system must respond predictably in time, so any control you add cannot introduce latency that breaks the process. Performance is a security requirement here, not just a convenience.*

## Physical Access Control

Physical security is a frontline OT control because touching a device often defeats network defenses. You layer perimeter, room, and cabinet controls.

| Control | Purpose |
|---------|---------|
| **Access control system** | Badges, fobs, readers, biometrics, and turnstiles that gate entry |
| **Access control vestibule** | Allows only one person through at a time to stop tailgating |
| **Room and cabinet security** | Locked rooms, locked cabinets, and cable locks on equipment |
| **MDF and IDF protection** | Securing the main and intermediate distribution frames where wiring lands |
| **Surveillance** | Video, motion sensors, and a spectrum analyzer to detect rogue wireless |
| **Fences and bollards** | Perimeter barriers that stop people and vehicles |

A **walkdown** is a physical inspection of the facility to confirm the environment matches the documented design and to spot unauthorized devices or connections.

## Hardware Hardening

You harden each device against tampering and unauthorized code before and after deployment.

| Control | Protection |
|---------|-----------|
| **Secure Boot** | Allows only trusted, signed code to run at startup |
| **Root of trust / TPM** | A Trusted Platform Module stores keys and verifies system integrity |
| **Tamper detection** | Reveals or responds to physical interference |
| **Drive encryption** | Protects data stored on the device |
| **Firmware updates** | Apply tested vendor firmware to close known flaws |
| **Port lockers and blockers** | Physically block unused USB and network ports |

You also manage how a device behaves and connects.

- A **PLC operating mode** such as run, program, or remote controls how a PLC accepts changes. Leaving it in remote-program can let an attacker push logic.
- A **backup strategy** captures device configuration and logic so you can restore after failure.
- **Port, protocol, and service management** disables everything the device does not need.
- **Hardware access control** restricts who can physically connect to the device.
- **Secure removable media** handling prevents USB drives from carrying malware into the device.

## Host and Application Security

Workstations and servers in OT need IT-grade host controls tuned for fragile systems.

| Control | Function |
|---------|----------|
| **Host firewall** | Filters traffic to and from a single host |
| **HIDS** | Host-based intrusion detection that watches a host for malicious activity |
| **EPP / EDR** | Endpoint protection platform and endpoint detection and response |
| **EPM** | Endpoint privilege management that limits what local accounts can elevate |
| **Patches** | Tested updates that close software vulnerabilities |
| **Code signing** | Proves software origin with a verified signature |

You also lock down the host configuration.

- **OS benchmarks** apply a hardened baseline such as a CIS benchmark.
- **Integrity verification** confirms files and software have not changed.
- **Deactivating debug interfaces** removes maintenance backdoors before production.
- **Read and write protection** prevents unauthorized changes to critical files.
- **Access control models** such as **role-based (RBAC)**, **attribute-based (ABAC)**, and **mandatory access control (MAC)** decide who can do what.

## Network Architecture and Segmentation

Segmentation is the heart of OT defense. You divide the network into zones and tightly control what crosses between them.

- **Segmentation** can be **physical** with separate hardware or **logical** with **subnetting** and **VLANs**.
- **Zones and conduits** is the ISA/IEC 62443 model that groups assets into zones linked by controlled conduits.
- The **industrial demilitarized zone (IDMZ)** is a buffer network between the OT and IT networks.
- A **data diode** allows data to flow in only one direction.
- A **unidirectional gateway** enforces one-way transfer in hardware.

*The IDMZ is the single most important architectural control in OT. No IT system should ever talk directly to an OT device. Traffic terminates in the IDMZ and is brokered across.*

You enforce and watch the boundary with these controls.

| Control | Role |
|---------|------|
| **ACLs and firewall policy** | Explicit allow and block lists that permit only required traffic |
| **NAC** | Network access control using MAC, certificate, or token-based checks |
| **Proxy** | Brokers and inspects traffic between zones |
| **OT-aware IDS/IPS** | Understands industrial protocols to detect and stop attacks |
| **Out-of-band management** | Administers devices over a separate network from production |
| **Wireless management** | Controls and monitors wireless access in the plant |

Internal monitoring keeps the segmented network honest. You aggregate **traffic, flow, and logs**, build a **baseline** of normal behavior, and apply **DNS security** with query logging and reverse lookups to spot suspicious resolution. You also choose the **encryption location** carefully, because encryption can blind the OT-aware sensors that protect the process.

## Identity and Access Management

You control who can do what with strong identity controls and disciplined account hygiene.

You should recognize the **account types** in an OT environment.

- A **service account** runs an application or process, not a person.
- A **shared account** is used by multiple people and is hard to attribute.
- An **individual account** belongs to one named user.
- A **privileged account** holds elevated rights and needs the most protection.
- A **local account** exists only on a single device.

*Change default passwords on every device and account before deployment. Default credentials are the first thing an attacker tries.*

You centralize and strengthen identity with these services and controls.

| Control | Function |
|---------|----------|
| **Directory services** | Central identity store with Group Policy for configuration |
| **PKI** | Issues device and user certificates through a registration authority |
| **RADIUS / TACACS+** | Centralize authentication, authorization, and accounting |
| **SSO** | Single sign-on across multiple systems |
| **MFA** | Multifactor authentication requiring two or more independent factors |
| **PAM** | Privileged access management to secure and monitor elevated accounts |

A **jump box** or **bastion host** is a hardened, controlled gateway that administrators must pass through to reach OT systems, so all privileged access is funneled and logged.

## Next Steps

With the architecture designed, continue to [OT Security Operations](/secot-plus/ot-security-operations/) to run and monitor it day to day. Return anytime to the [CompTIA SecOT+ Course](/secot-plus-start/).
