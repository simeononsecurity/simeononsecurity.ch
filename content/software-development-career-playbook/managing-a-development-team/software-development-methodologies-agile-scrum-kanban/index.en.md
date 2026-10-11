---
title: "Software Development Methodologies"
draft: false
toc: true
date: 2026-07-22
lastmod: 2026-10-10
description: "Compare Agile values, the 2020 Scrum Guide, and Kanban flow practices through a filled work board, explicit policies, metrics, and a review action."
tags: ["agile software development", "scrum methodology", "kanban for developers", "agile vs scrum vs kanban", "software development process", "sprint planning", "agile team practices", "managing a development team", "software development methodologies"]
coverAlt: "A digital illustration of a modern workspace showing a Kanban board with colorful cards and a Scrum team engaged in a daily standup, all set against a dark background."
coverCaption: ""
cover: "/img/cover/agile-scrum-kanban-software-development-methodologies.webp"
---

[Return to the Software Development Career Playbook](/software-development-career-playbook-start/)

Agile values, Scrum, and Kanban offer different ways to inspect work and adapt. Use the current source for each approach. Select practices which fit the work, risks, and team rather than treating a framework name as proof of good delivery.

## Agile: the Philosophy

**Agile** is not a methodology. It is a set of values and principles codified in the 2001 Agile Manifesto:

- Individuals and interactions **over** processes and tools.
- Working software **over** comprehensive documentation.
- Customer collaboration **over** contract negotiation.
- Responding to change **over** following a plan.

Agile prescribes none of the specific ceremonies (sprints, standups, retrospectives). Those come from frameworks like Scrum and Kanban that implement agile principles.

## Scrum

**Scrum** structures work into fixed-length sprints of one month or less. The 2020 Scrum Guide defines accountabilities and events.

### Scrum Roles

| Role | Responsibility |
|---|---|
| **Product Owner (PO)** | Defines and prioritizes the backlog, represents customer and business value |
| **Scrum Master** | Establishes Scrum, supports effectiveness, and helps remove impediments |
| **Developers** | Create a usable increment and adapt the plan toward the Sprint Goal |

### Scrum Ceremonies

| Scrum Event | Purpose | Timebox From the Scrum Guide |
|---|---|---|
| **Sprint Planning** | Initiate the Sprint by laying out why, what, and how | Maximum eight hours for a one-month Sprint |
| **Daily Scrum** | Inspect progress toward the Sprint Goal and adapt the Sprint Backlog | 15 minutes |
| **Sprint Review** | Inspect the outcome and determine future adaptations | Maximum four hours for a one-month Sprint |
| **Sprint Retrospective** | Plan ways to increase quality and effectiveness | Maximum three hours for a one-month Sprint |

Product Backlog refinement is ongoing work. The Scrum Guide does not define it as a Scrum event or prescribe a fixed duration.

### What Makes Scrum Work

- A well-maintained backlog with clear acceptance criteria before sprint planning.
- A PO who is available to answer questions during the sprint, not just at sprint boundaries.
- A team empowered to push back on scope mid-sprint rather than silently overcommit.
- Retrospective actions that are actually implemented.

### What Kills Scrum

- Sprint commitments treated as contracts rather than forecasts.
- Architectural work that cannot fit in a sprint but is forced to anyway.
- One person holding Scrum Master and Developer accountabilities without enough capacity or clear conflict handling.
- Retrospectives where the same problems surface every sprint with no resolution.

## Kanban

**Kanban** visualizes work as a flow of items through defined stages. Unlike Scrum, there are no sprints, no fixed-length iterations, and no roles.

The core Kanban practices:

1. **Visualize the workflow**: a board with columns representing stages (To Do, In Progress, In Review, Done).
2. **Limit work in progress (WIP)**: a WIP limit on each column prevents bottlenecks from being hidden. "No more than 3 tickets In Progress at once."
3. **Manage flow**: measure and improve the time from start to completion (cycle time, lead time).
4. **Make policies explicit**: define when a ticket moves from one stage to the next (definition of done).
5. **Implement feedback loops**: choose review cadences which help the team inspect flow and change policy.

### When Kanban Works Better Than Scrum

- Operational and support teams where incoming work changes faster than a chosen planning interval.
- Engineering teams with continuous delivery where work flows constantly rather than in batches.
- Small teams where Scrum ceremony overhead exceeds its value.

Kanban often fits interruption-heavy work because work-in-progress limits and flow policies expose overload. A team should test this fit against its own service commitments.

## SAFe, LeSS, and Scaled Agile Frameworks

Large organizations often layer additional coordination frameworks on top of Scrum or Kanban:

- **SAFe (Scaled Agile Framework)**: defines program increments (PIs) and Agile Release Trains (ARTs) to coordinate dozens of teams. Often criticized for recreating waterfall planning with agile vocabulary.
- **LeSS (Large-Scale Scrum)**: minimal coordination layer for multiple Scrum teams working on a single product.
- **Spotify Model**: squad, tribe, chapter, guild structure. Widely referenced but often misapplied, it was never a prescriptive framework.

Before adding a scaling framework, define the coordination problem, expected benefit, cost, and review date.

## Choosing Your Methodology

| Team Type | Recommendation |
|---|---|
| Stable product goal with iterative delivery | Evaluate Scrum |
| Unpredictable intake or service work | Evaluate Kanban |
| Small team with changing priorities | Test a lightweight visual flow |
| Multiple dependent teams | Define the dependency before selecting coordination practices |

## Next Steps

- [Building and Leading a Development Team](/software-development-career-playbook/managing-a-development-team/building-and-leading-a-development-team/)
- [DevOps and Platform Engineering for Developers](/software-development-career-playbook/managing-a-development-team/devops-and-platform-engineering-for-developers/)
- [Software Development Career Playbook Home](/software-development-career-playbook-start/)

## Practice and Verify

**Artifact: Flow experiment.** Create a small board with backlog, active, review, and done states. Set an explicit work-in-progress limit, product goal, short delivery goal, and definition of done. Run one week, measure cycle time without individual ranking, and record one retrospective action.

> **Expected result:** The board shows work movement, blocked items, a respected WIP limit, and one owned improvement action.

```text
REDACTED COMPLETED EXAMPLE
WIP limit: 2. Items finished: 3. Blocked item: dependency access. Retro action: request access before commitment.
```

**Pass checklist**

- [ ] The artifact uses dated, role-specific evidence
- [ ] Claims, ownership, team credit, and unknown values are truthful
- [ ] Privacy, secrets, licenses, accessibility, cost, and safety received review where relevant
- [ ] A reviewer or repeatable check produced feedback
- [ ] The record names a timed next action and checkpoint

**Primary references, checked 2026-10-10:** [Scrum Guide 2020](https://scrumguides.org/scrum-guide.html), [Kanban Guide](https://kanbanguides.org/english/), and [Manifesto for Agile Software Development](https://agilemanifesto.org/).
