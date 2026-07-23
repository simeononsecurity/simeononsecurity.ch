---
title: "IT Policies and Change Management: ITSM, ITIL, and CAB Explained"
draft: false
toc: true
date: 2026-07-22
description: "Learn how to build IT policies and run effective change management processes using ITSM, ITIL 4, and Change Advisory Board (CAB) practices that reduce risk and downtime."
tags: ["it change management", "ITIL change management", "CAB change advisory board", "ITSM practices", "it policies for teams", "change management process it", "managing an it team", "it career playbook"]
coverAlt: "A diverse team of IT professionals collaborates around a digital interface showing a flowchart of the change management process stages on a deep navy background."
coverCaption: ""
cover: "/img/cover/it-change-management-process-itil-cab.webp"
---

#### [Click Here to Return To the IT Career Playbook](/it-career-playbook-start/)

**Most IT outages are caused by changes, not hardware failures.** A formal change management process does not slow work down. It catches the changes most likely to cause problems before they hit production. *Skipping change control feels fast until the first unplanned outage costs you twelve hours of recovery time and an incident report.*

Building lightweight but effective IT policies and change processes is one of the most impactful things an IT manager can do.

## What IT Policies Cover

IT policies set the rules of the road for how technology is used, managed, and protected inside the organization. Every IT team needs at least these foundational policies:

| Policy | What It Governs |
|---|---|
| **Acceptable Use Policy (AUP)** | How employees may use company devices and networks |
| **Access Control Policy** | Who gets access to what, and how access is provisioned and revoked |
| **Change Management Policy** | How changes to systems are requested, reviewed, approved, and documented |
| **Incident Response Policy** | How security or service incidents are detected, escalated, and resolved |
| **Data Classification Policy** | How data is labeled and handled based on sensitivity |
| **Backup and Recovery Policy** | Frequency, retention, and testing requirements for backups |
| **Vendor Management Policy** | How third-party vendors are evaluated, contracted, and monitored |

Policies must be living documents. Review them at least annually and whenever a regulation, audit finding, or major incident exposes a gap.

## ITSM: the Operational Model

**IT Service Management (ITSM)** is the discipline of managing IT as a set of services delivered to users and the business. ITSM practices define how your team handles requests, incidents, problems, and changes consistently and measurably.

The most widely-used ITSM framework is **ITIL 4**, which organizes practice into a service value system connecting business demand to value delivery. Core ITSM processes that every IT manager must own:

- **Service request management** — handling routine user requests (password resets, software installs, access provisioning).
- **Incident management** — restoring service as fast as possible after an unplanned disruption.
- **Problem management** — finding and eliminating root causes so the same incident does not recur.
- **Change enablement** — managing risk when modifying IT systems.
- **Knowledge management** — capturing solutions and runbooks so the team does not solve the same problem twice.

## Change Management Process

A standard change management process moves every change through five stages:

1. **Request** — a team member submits a change request (CR) describing what will change, why, and what the rollback plan is.
2. **Review** — technical peers review the change for completeness and risk.
3. **Approval** — a Change Advisory Board (CAB) or change manager approves, defers, or rejects the change.
4. **Implementation** — the change is executed in the approved maintenance window.
5. **Post-implementation review** — the change is documented as successful, failed, or partially successful.

## Change Types

Not every change needs full CAB review. Classify changes by risk to determine the approval path.

| Type | Definition | Approval Path |
|---|---|---|
| **Standard** | Pre-approved, low-risk, routine (patch Tuesday, scheduled reboots) | Pre-authorized, no CAB needed |
| **Normal** | Planned change with moderate risk | CAB review before implementing |
| **Emergency** | Urgent change to restore service or fix a critical vulnerability | Expedited approval, documented retroactively |

*Reserve emergency changes for actual emergencies. Overuse of the emergency path bypasses the controls that prevent outages.*

## Change Advisory Board (CAB)

The **CAB** is typically a weekly or bi-weekly meeting where proposed normal changes are reviewed before approval. CAB participants include IT leadership, the change manager, and representatives from impacted teams.

A lightweight CAB for smaller organizations can be an async Slack channel or a shared spreadsheet with a 48-hour approval window. The goal is peer review and a second set of eyes, not bureaucracy.

## Measuring Change Management Effectiveness

Track these metrics to gauge the health of your change process:

- **Change success rate** — percentage of changes implemented without unplanned impact.
- **Emergency change rate** — high rates indicate poor planning or inadequate standard change catalog.
- **MTTR (Mean Time to Restore)** — average time to full service restoration after an incident.
- **Change-related incident rate** — percentage of incidents caused by changes, target below 15%.

## Next Steps

- [Building and Managing an IT Team](/it-career-playbook/managing-an-it-team/building-and-managing-an-it-team/)
- [Outsourcing vs. In-House IT](/it-career-playbook/managing-an-it-team/outsourcing-vs-inhouse-it/)
- [IT Career Playbook Home](/it-career-playbook-start/)
