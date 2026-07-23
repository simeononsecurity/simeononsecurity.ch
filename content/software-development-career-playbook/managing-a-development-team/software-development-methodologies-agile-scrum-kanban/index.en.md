---
title: "Software Development Methodologies: Agile, Scrum, and Kanban Explained"
draft: false
toc: true
date: 2026-07-22
description: "Understand the core software development methodologies — Agile, Scrum, and Kanban — when to use each one, and what actually works versus what becomes process theater."
tags: ["agile software development", "scrum methodology", "kanban for developers", "agile vs scrum vs kanban", "software development process", "sprint planning", "agile team practices", "managing a development team", "software development methodologies"]
coverAlt: "A digital illustration of a modern workspace showing a Kanban board with colorful cards and a Scrum team engaged in a daily standup, all set against a dark background."
coverCaption: ""
cover: "/img/cover/agile-scrum-kanban-software-development-methodologies.webp"
---

#### [Click Here to Return To the Software Development Career Playbook](/software-development-career-playbook-start/)

**Most software teams claim to be "agile" while practicing something closer to chaotic iteration with standups.** Understanding what Agile, Scrum, and Kanban actually prescribe — and what makes each one work or fail — helps you run a team that ships consistently rather than a team that attends meetings about shipping. *The goal of any methodology is reducing uncertainty and improving delivery. If your process adds overhead without reducing uncertainty, it is waste.*

## Agile: the Philosophy

**Agile** is not a methodology. It is a set of values and principles codified in the 2001 Agile Manifesto:

- Individuals and interactions **over** processes and tools.
- Working software **over** comprehensive documentation.
- Customer collaboration **over** contract negotiation.
- Responding to change **over** following a plan.

Agile prescribes none of the specific ceremonies (sprints, standups, retrospectives). Those come from frameworks like Scrum and Kanban that implement agile principles.

## Scrum

**Scrum** is the most widely used agile framework. It structures work into fixed-length iterations called **sprints** (usually 2 weeks), with defined ceremonies and roles.

### Scrum Roles

| Role | Responsibility |
|---|---|
| **Product Owner (PO)** | Defines and prioritizes the backlog; represents customer and business value |
| **Scrum Master** | Facilitates Scrum ceremonies; removes process blockers for the team |
| **Development Team** | Cross-functional engineers who deliver the sprint goal |

### Scrum Ceremonies

| Ceremony | Purpose | Typical Duration |
|---|---|---|
| **Sprint Planning** | Team selects stories from backlog and commits to a sprint goal | 2–4 hours per 2-week sprint |
| **Daily Standup** | Synchronize on progress and blockers | 15 minutes |
| **Sprint Review** | Demo completed work to stakeholders | 1 hour |
| **Sprint Retrospective** | Inspect and adapt team process | 1 hour |
| **Backlog Refinement** | Groom, estimate, and clarify upcoming stories | 1 hour ongoing |

### What Makes Scrum Work

- A well-maintained backlog with clear acceptance criteria before sprint planning.
- A PO who is available to answer questions during the sprint, not just at sprint boundaries.
- A team empowered to push back on scope mid-sprint rather than silently overcommit.
- Retrospective actions that are actually implemented.

### What Kills Scrum

- Sprint commitments treated as contracts rather than forecasts.
- Architectural work that cannot fit in a sprint but is forced to anyway.
- A Scrum Master who is also a developer on the same team (the roles conflict).
- Retrospectives where the same problems surface every sprint with no resolution.

## Kanban

**Kanban** visualizes work as a flow of items through defined stages. Unlike Scrum, there are no sprints, no fixed-length iterations, and no roles.

The core Kanban practices:

1. **Visualize the workflow**: a board with columns representing stages (To Do, In Progress, In Review, Done).
2. **Limit work in progress (WIP)**: a WIP limit on each column prevents bottlenecks from being hidden. "No more than 3 tickets In Progress at once."
3. **Manage flow**: measure and improve the time from start to completion (cycle time, lead time).
4. **Make policies explicit**: define when a ticket moves from one stage to the next (definition of done).
5. **Implement feedback loops**: daily standup, weekly flow meeting.

### When Kanban Works Better Than Scrum

- Operational and support teams where incoming work is unpredictable and cannot be planned 2 weeks ahead.
- Engineering teams with continuous delivery where work flows constantly rather than in batches.
- Small teams where Scrum ceremony overhead exceeds its value.

*Interruption-heavy work (production incidents, security team, platform-on-call) belongs on a Kanban board, not a sprint.*

## SAFe, LeSS, and Scaled Agile Frameworks

Large organizations often layer additional coordination frameworks on top of Scrum or Kanban:

- **SAFe (Scaled Agile Framework)**: defines program increments (PIs) and Agile Release Trains (ARTs) to coordinate dozens of teams. Often criticized for recreating waterfall planning with agile vocabulary.
- **LeSS (Large-Scale Scrum)**: minimal coordination layer for multiple Scrum teams working on a single product.
- **Spotify Model**: squad, tribe, chapter, guild structure. Widely referenced but often misapplied; it was never a prescriptive framework.

*Most teams are better served by disciplined Scrum or Kanban than by scaling frameworks. Adopt scaling frameworks only when you have proven your fundamental process works first.*

## Choosing Your Methodology

| Team Type | Recommendation |
|---|---|
| Product team, planned roadmap | Scrum |
| Platform / ops / support team | Kanban |
| Early-stage startup | Lightweight Kanban or shape-up |
| Large multi-team program | Scrum + SAFe program increment |

## Next Steps

- [Building and Leading a Development Team](/software-development-career-playbook/managing-a-development-team/building-and-leading-a-development-team/)
- [DevOps and Platform Engineering for Developers](/software-development-career-playbook/managing-a-development-team/devops-and-platform-engineering-for-developers/)
- [Software Development Career Playbook Home](/software-development-career-playbook-start/)
