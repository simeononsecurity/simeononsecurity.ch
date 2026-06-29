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

The **Incident Command System (ICS)** provides a standardized command structure, and **ICS4ICS** adapts it specifically for industrial control system incidents.

## Coordination and Communication

OT incidents pull in many teams at once, so coordination is a skill the exam tests directly. Safety comes first, which can mean calling for physical response before cyber response.

- **Cybersecurity and physical response** may both be needed, including **emergency services** and an **emergency shutdown (ESD)**.
- **Crisis management** leads the broad organizational response and messaging.
- **Facilities** teams handle the building, power, and physical environment.
- **IT and OT coordination** aligns two teams that think differently about uptime and safety.
- **Escalation and notification** raise the incident to the right leaders and authorities on time.

You also reach outside the organization for help through **mutual aid**.

- **Internal** teams and other sites can lend staff and resources.
- **ISACs** share sector intelligence and coordinate a common response.
- **Incident response retainers (IRRs)** pre-arrange outside expert support.

## Plans, Playbooks, and Exercises

You prepare the documents and skills response depends on long before an incident.

| Document | Role |
|----------|------|
| **Incident response plan (IRP)** | Documents the overall response approach |
| **Playbook** | Guides response to a specific type of incident |
| **Runbook** | Gives detailed step-by-step operational procedures |
| **Decision matrix** | Guides choices such as declaration, shutdown, or payment |

You focus the plan on **high-value assets** and the **attack surface** that protect the process. Then you practice.

- A **tabletop exercise (TTX)** walks through a scenario in discussion.
- A **purple-team exercise** has offensive and defensive teams work together.
- A **simulation** is a realistic practice run of response.

## Decisions, Triage, and Forensics

When an incident is declared, you make hard calls and gather evidence at the same time. A **flyaway kit** with **PPE** and **tooling** lets a team respond on site.

Decision matrices guide three critical choices.

- **Declaration** decides when an event becomes a formal incident.
- **Shutdown** decides whether to bring the process to a safe stop.
- **Payment** decides on any ransom, with an **OFAC** check because paying a sanctioned entity is illegal.

*An OFAC consideration matters before any ransom payment. The decision matrix should route that choice to legal and leadership, never to a single responder.*

You then **triage** and **scope** the incident, and you protect evidence with a **chain of custody** that preserves its integrity. Advanced collection in OT goes beyond a normal disk image.

- **Historian data**, a **sequence of events**, and **operator logs** reconstruct what happened to the process.
- **Memory**, **disk**, **registry**, and **user logs** capture the host side of the attack.

Finally, **root cause analysis (RCA)** determines the underlying cause so the same incident cannot recur.

## OT-Specific Incident Effects

OT attacks produce primary impacts you must recognize and name. The exam pairs each loss with its manipulation twin.

| Effect | What Happens |
|--------|--------------|
| **Loss of view** | Operators can no longer see the process state |
| **Loss of control** | Operators can no longer control the process |
| **Loss of safety** | Safety functions stop protecting the process |
| **Manipulation of view** | The attacker falsifies what operators see |
| **Manipulation of control** | The attacker alters commands sent to the process |
| **Manipulation of safety** | The attacker tampers with safety functions |

*Manipulation of view is especially dangerous. Stuxnet showed operators normal readings while the centrifuges tore themselves apart. Trust your independent instrumentation, not just the HMI.*

## Investigative Data Sets

You pull evidence from three data sets, each telling part of the story.

- **System documentation** reveals a **deviation from baseline**, **anomalous behavior**, or a **deviation from design**.
- **Network data** includes **flow**, **firewall**, **ICS protocol**, **pcap**, **IDS**, **deception**, **ISP**, and **syslog** records.
- **Host data** includes **disk**, **OS events**, **application logs**, **security logs**, **sudo**, and **systemd** records.

## Containment Through Recovery

You stop the spread, remove the threat, and restore safe operation in order.

**Containment** limits the damage.

- **Isolate** and **quarantine** the affected systems.
- **Disconnect IT from OT** to stop a pivot.
- **Block malicious traffic** and **suspend compromised accounts**.

**Eradication** removes the threat.

- **Remove malicious components and malware** from affected systems.
- **Reset credentials** that may have been exposed.

**Recovery** brings the process back safely.

- **Restoration** returns systems to a known good state.
- A **bare metal restore** rebuilds a system from the ground up.
- A **hot swap** replaces failed hardware with minimal downtime.
- **Process validation** confirms the process runs correctly before going live.
- A **redesign** fixes the underlying weakness so it cannot be exploited again.

After the incident, you close the loop.

- A **hot wash** or **debrief** reviews the response while details are fresh.
- A **postmortem** and **lessons learned** drive lasting improvement.
- **Mandatory reporting** satisfies **regulatory**, **insurance**, **emergency notification**, and **contractual** duties.

## Next Steps

You have completed all six SecOT+ domains. Review any that need reinforcement, starting with [OT Systems and Safety Foundations](/secot-plus/ot-systems-safety-foundations/), then test your readiness with the [CompTIA SecOT+ Practice Test](/secot-plus-practice-test/). Return anytime to the [CompTIA SecOT+ Course](/secot-plus-start/).
