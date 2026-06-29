---
title: "CompTIA SecOT+ (SOT-001): OT Incident Management"
date: 2025-01-01
toc: true
draft: false
description: "Master OT incident management for the CompTIA SecOT+ SOT-001 exam. Learn the PICERL model, ICS4ICS, response plans and playbooks, exercises, OT-specific incident effects like loss of view and control, forensics, and containment through recovery."
genre: ["CompTIA SecOT+ Course", "OT Incident Management", "Incident Response", "PICERL", "ICS4ICS", "Digital Forensics", "Disaster Recovery", "Operational Technology", "SOT-001", "Cybersecurity"]
tags: ["CompTIA SecOT+", "SOT-001", "incident response", "PICERL", "ICS4ICS", "Incident Command System", "tabletop exercise", "loss of view", "loss of control", "loss of safety", "chain of custody", "root cause analysis", "containment", "eradication", "recovery", "lessons learned", "mandatory reporting"]
cover: "/img/cover/comptia-secot-incident-management-ot-response.webp"
coverAlt: "An industrial control room scene with a central figure analyzing screens, surrounded by team members coordinating responses. Graphs and schematics are visible in vibrant colors against a dark background."
coverCaption: "Lead OT Incident Response from Detection to Recovery for the SOT-001 Exam"
---

#### [Click Here to Return To the CompTIA SecOT+ Course Page](/secot-plus-start/)

**OT Incident Management** is **15%** of the **CompTIA SecOT+ (SOT-001)** exam. This domain teaches you to respond when prevention fails. You follow a structured model, coordinate IT and OT teams, preserve evidence, and restore the process safely. *In OT, the response itself can cause harm, so every action weighs safety and physical impact, not just data recovery.*

OT incident response is different because the stakes are physical. An incident can blind operators, take away their control, or defeat a safety system, and your job is to restore safe operation as fast as possible.

## Response Model

You work from a defined model rather than improvising.

| Phase (PICERL) | Action |
|----------------|--------|
| **Prepare** | Build plans, tools, and skills before an incident |
| **Identify** | Detect and confirm that an incident is underway |
| **Contain** | Limit the spread and impact |
| **Eradicate** | Remove the threat and its artifacts |
| **Recover** | Restore systems to normal operation |
| **Lessons learned** | Review to improve future response |

The **Incident Command System** provides a standardized command structure, and **ICS4ICS** adapts it specifically for industrial control system incidents.

## Plans and Playbooks

You prepare the documents response depends on.

- An **incident response plan** documents the overall approach.
- A **playbook** guides response to a specific type of incident.
- A **runbook** gives detailed operational procedures.
- A **decision matrix** guides choices such as declaration, shutdown, or payment.
- An **incident response retainer** pre-arranges outside support.

*An OFAC consideration matters before any ransom payment, because paying a sanctioned entity is itself illegal. The decision matrix should route that choice to legal and leadership.*

## Exercises

You practice before the real event.

- A **tabletop exercise** walks through a scenario in discussion.
- A **purple-team exercise** has offensive and defensive teams work together.
- A **simulation** is a realistic practice run of response.
- A **flyaway kit** is a portable set of tools and gear for responding on site.

## OT-Specific Incident Effects

OT attacks produce effects you must recognize and name.

| Effect | What happens |
|--------|--------------|
| **Loss of view** | Operators can no longer see the process state |
| **Loss of control** | Operators can no longer control the process |
| **Loss of safety** | Safety functions are compromised |
| **Manipulation of view** | The attacker falsifies what operators see |
| **Manipulation of control** | The attacker alters commands sent to the process |

*Manipulation of view is especially dangerous. Stuxnet showed operators normal readings while the centrifuges tore themselves apart. Trust your independent instrumentation, not just the HMI.*

## Investigation and Forensics

You gather and protect evidence while you respond.

- **Chain of custody** preserves the integrity of collected evidence.
- **Triage** and **scoping** assess and bound the incident.
- **Memory capture** collects volatile memory for analysis.
- **Historian data**, a **sequence of events**, and the **operator log** reconstruct what happened.
- **Root cause analysis** determines the underlying cause, and a **deviation from baseline** points to the problem.

## Containment Through Recovery

You stop the spread and restore safe operation.

- **Containment**, **isolation**, and **quarantine** limit and separate the affected systems.
- **Eradication** removes the threat from affected systems.
- **Recovery** restores normal operation, sometimes through a **bare metal restore** or a **hot swap** of failed hardware.
- An **emergency shutdown** brings the process to a safe stopped state when needed.

After the incident, a **hot wash** debriefs while details are fresh, **lessons learned** drives improvement, and **mandatory reporting** satisfies legal and contractual notification duties.

## Next Steps

You have completed all six SecOT+ domains. Review any that need reinforcement, starting with [OT Systems and Safety Foundations](/secot-plus/ot-systems-safety-foundations/), then test your readiness with the [CompTIA SecOT+ Practice Test](/secot-plus-practice-test/). Return anytime to the [CompTIA SecOT+ Course](/secot-plus-start/).
