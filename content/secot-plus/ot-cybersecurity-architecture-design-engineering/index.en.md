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

**OT Cybersecurity Architecture, Design, and Engineering** is **18%** of the **CompTIA SecOT+ (SOT-001)** exam. This domain teaches you to build OT systems that resist attack and keep running through one. You apply layered controls, harden fragile devices, and segment the network so a compromise on one side cannot reach the process on the other. *Architecture is where you prevent the IT to OT pivot you studied in threat intelligence.*

Good OT architecture assumes a breach will happen. The goal is to contain it, keep the process safe, and keep operators in control.

## Design Principles

You start from sound principles.

| Principle | Meaning |
|-----------|---------|
| **Least privilege** | Grant only the access needed to function |
| **Defense in depth** | Layer controls so no single failure is fatal |
| **Compartmentalization** | Isolate parts so a compromise cannot spread freely |
| **Redundancy** | Duplicate components that take over on failure |
| **High availability** | Keep systems running with minimal downtime |
| **Operational resilience** | Endure and recover from disruption |

*Deterministic behavior matters in OT. The system must respond predictably in time, so any control you add cannot introduce latency that breaks the process.*

## Physical Access Control

Physical security is a frontline OT control because touching a device often defeats network defenses.

- An **access control vestibule** allows only one person through at a time.
- **Biometric access** grants entry based on fingerprints or other body traits.
- A **bollard** blocks vehicles from restricted areas.
- A **port blocker** prevents use of an unused hardware port.
- The **main distribution frame** and **intermediate distribution frame** are wiring points you must protect.

## Device Hardening

You harden each device against tampering and unauthorized code.

| Control | Protection |
|---------|-----------|
| **Secure Boot** | Allows only trusted, signed code to run at startup |
| **Trusted Platform Module** | Stores keys and verifies system integrity |
| **Tamper detection** | Reveals or responds to physical interference |
| **Drive encryption** | Protects stored data |
| **Code signing** | Proves software origin with a verified signature |
| **Default password change** | Replaces factory credentials before deployment |

A **PLC operating mode** such as run, program, or remote also controls how a PLC behaves, and leaving it in remote-program can let an attacker push logic changes.

## Network Segmentation

Segmentation is the heart of OT defense. You divide the network into zones and tightly control what crosses between them.

- **Network segmentation** divides the network into zones to limit spread.
- A **VLAN** logically separates traffic on shared hardware.
- The **industrial demilitarized zone (IDMZ)** is a buffer network between the OT and IT networks.
- **Zones and conduits** is the ISA/IEC 62443 model that groups assets into zones linked by controlled conduits.
- A **data diode** allows data to flow in only one direction.
- A **unidirectional gateway** enforces one-way transfer in hardware.

*The IDMZ is the single most important architectural control in OT. No IT system should ever talk directly to an OT device. Traffic terminates in the IDMZ and is brokered across.*

## Detection and Management

You add monitoring and controlled administration paths.

- An **OT-aware intrusion detection system** understands industrial protocols and behavior.
- A **host-based firewall** and **host-based intrusion detection system** protect individual hosts.
- **Endpoint detection and response** monitors endpoints and responds to threats.
- **Out-of-band management** uses a separate network from production traffic.
- A **jump box** is a hardened, controlled gateway for remote administration.

## Identity and Access Management

You control who can do what with strong identity controls.

| Control | Function |
|---------|----------|
| **Role-based access control** | Access based on assigned role |
| **Attribute-based access control** | Access based on user, resource, and context attributes |
| **Mandatory access control** | Access enforced by system rules users cannot change |
| **Multifactor authentication** | Requires two or more independent factors |
| **Privileged access management** | Secures and monitors elevated accounts |

**RADIUS** and **TACACS+** centralize authentication and accounting, and a **public key infrastructure** manages the certificates that bind identity to keys.

## Next Steps

With the architecture designed, continue to [OT Security Operations](/secot-plus/ot-security-operations/) to run and monitor it day to day. Return anytime to the [CompTIA SecOT+ Course](/secot-plus-start/).
