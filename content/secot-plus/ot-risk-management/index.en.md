---
title: "CompTIA SecOT+ (SOT-001): OT Risk Management"
date: 2025-01-01
toc: true
draft: false
description: "Master OT risk management for the CompTIA SecOT+ SOT-001 exam. Learn risk fundamentals, frameworks like ISA/IEC 62443 and NERC CIP, qualitative and quantitative assessments, risk treatments, governance artifacts, third-party risk, and change management."
genre: ["CompTIA SecOT+ Course", "OT Risk Management", "ISA/IEC 62443", "NERC CIP", "Risk Assessment", "Governance", "Supply Chain Risk", "Operational Technology", "SOT-001", "Cybersecurity"]
tags: ["CompTIA SecOT+", "SOT-001", "risk appetite", "risk register", "ISA/IEC 62443", "NERC CIP", "NIST framework", "qualitative risk assessment", "quantitative risk assessment", "residual risk", "risk treatment", "supply chain risk", "third-party risk", "RACI", "change management", "rollback plan"]
cover: "/img/cover/comptia-secot-plus-ot-risk-management-illustration.webp"
coverAlt: "A control room scene with engineers analyzing risk management data on screens, featuring turbine controls and safety monitoring systems, all set against a dark background."
coverCaption: "Assess and Treat Risk in OT Environments for the SOT-001 Exam"
---

#### [Click Here to Return To the CompTIA SecOT+ Course Page](/secot-plus-start/)

**OT Risk Management** is **17%** of the **CompTIA SecOT+ (SOT-001)** exam. This domain teaches you how to find risk in an OT environment, decide how much risk the business will tolerate, and choose treatments that do not break the process. *In OT, a control that interrupts production or safety can be worse than the risk it addresses, so risk decisions must include the engineers who run the plant.*

Risk in OT carries physical and safety weight that IT risk does not. A breach can stop a turbine, contaminate a batch, or endanger workers, so impact ratings reach far beyond data loss.

## Governance, Risk, and Compliance Foundations

**Governance, risk, and compliance (GRC)** is the framework that directs OT security and keeps it aligned with the business. Good GRC balances two forces that often pull against each other.

- **Security** wants tighter controls, more monitoring, and frequent change.
- **Operations** wants uptime, safety, and stability above all else.

*The exam wants you to balance security against operations. The right answer protects the process without stopping it.*

You should know the **business drivers** that justify an OT security program, because they frame why a control matters.

| Driver | Why It Matters |
|--------|----------------|
| **National security** | Critical infrastructure failure can harm a nation, not just a company |
| **Regulatory compliance** | Laws and standards require specific controls |
| **Non-compliance** | Fines, sanctions, and lost licenses follow a failure to comply |
| **Reliability** | Customers and the public depend on continuous service |
| **Legal exposure** | Lawsuits and liability follow incidents and negligence |

A breach also creates **business impact** you must be able to categorize.

- **Financial** impact includes lost revenue, fines, and recovery cost.
- **Reputational** impact erodes customer and public trust.
- **Quality** impact ruins product batches and damages output.
- **Operational** impact stops or slows production.
- **Safety** impact is the most serious, including **loss of life** and **environmental** harm.

Two recovery disciplines round out the foundation. **Business continuity** keeps essential functions running during a disruption, and **disaster recovery** restores systems and data after one.

## Risk Fundamentals

You build every assessment from a few core ideas.

| Term | Meaning |
|------|---------|
| **Risk appetite** | The amount of risk the organization will accept to meet objectives |
| **Likelihood** | The probability that a risk event occurs |
| **Impact** | The consequence or severity if the event occurs |
| **Inherited risk** | Risk passed in from a connected system, vendor, or partner |
| **Residual risk** | The risk that remains after controls are applied |
| **Risk level** | A combined rating of likelihood and impact used to prioritize |

## Frameworks and Standards

OT security maps to published standards. The exam expects you to match each one to its scope.

| Framework | Scope |
|-----------|-------|
| **ISA/IEC 62443** | The core series for securing industrial automation and control systems |
| **NIST framework** | Broad guidance for managing cybersecurity risk |
| **NERC CIP** | Critical Infrastructure Protection standards for the North American electric grid |
| **NIS2 Directive** | European Union rules raising security requirements for essential services |
| **Cyber Resilience Act (CRA)** | European Union rules for security of products with digital elements |

*ISA/IEC 62443 is the standard you will see most on this exam. Know that it introduces the zones and conduits model and the security levels used to rate OT segments.*

## Building the Risk Program

A mature program is more than a single assessment. You manage it with structure and documentation.

- A **risk register** lists identified risks with owner, status, and treatment.
- A **maturity assessment** evaluates how developed the program's capabilities are.
- A **benchmark** compares your program against peers and standards.
- A **roadmap** sequences improvement initiatives over time.
- A **RACI model** assigns who is Responsible, Accountable, Consulted, and Informed.
- **Stakeholder management** keeps operators, engineers, and executives engaged in risk decisions.
- **Metrics** track program performance with measurable indicators.
- **Training and awareness** prepare staff to recognize and avoid OT threats.
- **Criticality** ranks assets so the most important systems get the most protection.

You also document the program so it is repeatable and defensible. **Policies** state intent, **processes** describe how work flows, **standards** set required configurations, and **standard operating procedures (SOPs)** give step-by-step instructions for routine tasks.

## Agreements and Procurement

OT depends heavily on vendors and integrators, so you manage their risk through contracts. **Procurement** is where many of these terms are set, so security requirements belong in the purchase.

| Agreement | Purpose |
|-----------|---------|
| **Master service agreement (MSA)** | Sets general terms for future work |
| **Service-level agreement (SLA)** | Defines the expected level of service and its metrics, for internal or external parties |
| **Memorandum of understanding (MOU)** | Describes shared intent without binding the parties |
| **Statement of work (SOW)** | Defines specific deliverables, tasks, and timelines |

## Risk Assessment Methods

You assess risk with the right tool for the question. First you define the **scope** and map the **threat surface**, the sum of all points an attacker could reach. Then you weigh the **risk variables** of likelihood and impact.

| Method | Description |
|--------|-------------|
| **Qualitative risk assessment** | Uses descriptive ratings such as high, medium, and low |
| **Quantitative risk assessment** | Uses numeric values such as monetary loss |
| **Scenario-based assessment** | Walks through a specific attack story to find gaps |
| **Failure mode and criticality analysis** | Examines how parts can fail and how severe each failure is |
| **Supply chain assessment** | Reviews hardware and software sourcing for risk |
| **Third-party assessment** | Evaluates the security of vendors and integrators |
| **Architecture review** | Assesses system design to find weaknesses |
| **Penetration test** | Runs an authorized simulated attack to find exploitable weaknesses |
| **Adversarial emulation** | Mimics a specific threat actor's tactics and techniques |

*Be cautious with active testing in live OT. A scan that is harmless on IT can crash a fragile PLC, so penetration testing in OT is often done on test systems or with great care.*

## Controls and Catalogs

Once you understand a risk, you select controls to address it.

- A **controls catalog** is a published library of controls you can choose from.
- **Control acceptance criteria** define what a control must achieve to be approved.
- **Control maturity indicators** show how well a control is implemented and managed.
- A **controls calendar** schedules recurring control activities such as reviews and tests.

## Risk Treatment and Disposition

After assessment, you choose a **disposition** for each risk.

- **Risk mitigation** reduces a risk's likelihood or impact.
- **Risk transfer** shifts a risk to another party such as an insurer.
- **Risk avoidance** eliminates the activity that causes the risk.
- **Risk acceptance** acknowledges and tolerates a risk within appetite.

The chosen action is the **risk treatment**, and what remains afterward is the **residual risk**. *You can never reach zero risk in OT. The goal is to drive residual risk down to within the organization's appetite.*

## Auditing, Reporting, and Escalation

You verify that controls work and keep leadership informed.

- An **internal audit** is performed by the organization's own staff.
- An **external audit** is performed by an independent third party.
- **Reporting** communicates risk status to stakeholders in clear, prioritized terms.
- **Escalation** raises a risk that exceeds appetite or authority to the right decision-maker.

## Change Management

**Change management** is the controlled process of identifying, evaluating, approving, and communicating changes. In OT it protects a live process, so it follows a careful sequence.

1. **Identification** captures the proposed change and its reason.
2. **Determination** confirms the change is applicable and that a fix is available.
3. **Testing and rollback** validate the change and prepare a way to revert it.
4. **Communication** informs stakeholders, department heads, and the system, process, and asset owners.
5. **Approval** authorizes the change before it touches production.

Every change to an OT system needs a **rollback plan**, a prepared procedure to revert a change that fails, so a bad update does not strand the process.

## Next Steps

With risk under control, continue to [OT Threat Intelligence](/secot-plus/ot-threat-intelligence/) to study the adversaries you defend against. Return anytime to the [CompTIA SecOT+ Course](/secot-plus-start/).
