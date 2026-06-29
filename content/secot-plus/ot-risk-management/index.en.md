---
title: "CompTIA SecOT+ (SOT-001): OT Risk Management"
date: 2025-01-01
toc: true
draft: false
description: "Master OT risk management for the CompTIA SecOT+ SOT-001 exam. Learn risk fundamentals, frameworks like ISA/IEC 62443 and NERC CIP, qualitative and quantitative assessments, risk treatments, governance artifacts, third-party risk, and change management."
genre: ["CompTIA SecOT+ Course", "OT Risk Management", "ISA/IEC 62443", "NERC CIP", "Risk Assessment", "Governance", "Supply Chain Risk", "Operational Technology", "SOT-001", "Cybersecurity"]
tags: ["CompTIA SecOT+", "SOT-001", "risk appetite", "risk register", "ISA/IEC 62443", "NERC CIP", "NIST framework", "qualitative risk assessment", "quantitative risk assessment", "residual risk", "risk treatment", "supply chain risk", "third-party risk", "RACI", "change management", "rollback plan"]
cover: "/img/cover/comptia-secot-plus-ot-risk-management.webp"
coverAlt: "An illustration of a risk matrix and governance documents overlaid on an industrial facility, set against a dark background."
coverCaption: "Assess and Treat Risk in OT Environments for the SOT-001 Exam"
---

#### [Click Here to Return To the CompTIA SecOT+ Course Page](/secot-plus-start/)

**OT Risk Management** is **17%** of the **CompTIA SecOT+ (SOT-001)** exam. This domain teaches you how to find risk in an OT environment, decide how much risk the business will tolerate, and choose treatments that do not break the process. *In OT, a control that interrupts production or safety can be worse than the risk it addresses, so risk decisions must include the engineers who run the plant.*

Risk in OT carries physical and safety weight that IT risk does not. A breach can stop a turbine, contaminate a batch, or endanger workers, so impact ratings reach far beyond data loss.

## Risk Fundamentals

You build every assessment from a few core ideas.

| Term | Meaning |
|------|---------|
| **Risk appetite** | The amount of risk the organization will accept to meet objectives |
| **Likelihood** | The probability that a risk event occurs |
| **Impact** | The consequence or severity if the event occurs |
| **Inherited risk** | Risk passed in from a connected system or partner |
| **Residual risk** | The risk that remains after controls are applied |

## Frameworks and Standards

OT security maps to published standards.

- **ISA/IEC 62443** is the core series of standards for securing industrial automation and control systems.
- The **NIST framework** provides broad guidance for managing cybersecurity risk.
- **NERC CIP** sets Critical Infrastructure Protection standards for the North American electric grid.

*ISA/IEC 62443 is the standard you will see most on this exam. Know that it introduces the zones and conduits model and security levels for OT.*

## Risk Assessment Methods

You assess risk with the right tool for the question.

| Method | Description |
|--------|-------------|
| **Qualitative risk assessment** | Uses descriptive ratings such as high, medium, and low |
| **Quantitative risk assessment** | Uses numeric values such as monetary loss |
| **Architecture review** | Assesses system design to find weaknesses |
| **Penetration test** | Runs an authorized simulated attack to find exploitable weaknesses |
| **Adversarial emulation** | Mimics a specific threat actor's tactics and techniques |

*Be cautious with active testing in live OT. A scan that is harmless on IT can crash a fragile PLC, so penetration testing in OT is often done on test systems or with great care.*

## Risk Treatment

Once you understand a risk, you choose how to treat it.

- **Risk mitigation** reduces a risk's likelihood or impact.
- **Risk transfer** shifts a risk to another party such as an insurer.
- **Risk avoidance** eliminates the activity that causes the risk.
- **Risk acceptance** acknowledges and tolerates a risk within appetite.

The chosen action is the **risk treatment**, and what remains afterward is the **residual risk**.

## Governance Artifacts

You document the program so it is repeatable and defensible.

| Artifact | Purpose |
|----------|---------|
| **Security policy** | States management's high-level security intent and rules |
| **Standard operating procedure** | Gives step-by-step instructions for routine tasks |
| **RACI model** | Assigns who is Responsible, Accountable, Consulted, and Informed |
| **Risk register** | Lists identified risks with status and treatment |
| **Maturity assessment** | Evaluates how developed the program's capabilities are |

A **roadmap** then sequences improvement initiatives, and a **benchmark** compares your program against peers.

## Agreements and Third Parties

OT depends heavily on vendors and integrators, so you manage their risk through contracts.

- A **master service agreement** sets general terms for future work.
- A **service-level agreement** defines the expected level of service and its metrics.
- A **memorandum of understanding** describes shared intent without binding the parties.
- A **statement of work** defines specific deliverables, tasks, and timelines.

**Supply chain risk** and **third-party risk** enter through hardware, software, and services from outside the organization. Internal and external audits then verify that controls work.

## Change Management

**Change management** is the controlled process of identifying, testing, approving, and communicating changes. Every change to an OT system needs a **rollback plan**, a prepared procedure to revert a change that fails, so a bad update does not strand the process.

## Next Steps

With risk under control, continue to [OT Threat Intelligence](/secot-plus/ot-threat-intelligence/) to study the adversaries you defend against. Return anytime to the [CompTIA SecOT+ Course](/secot-plus-start/).
