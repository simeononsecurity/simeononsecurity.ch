---
title: "Module 1: Red Team Methodology"
date: 2026-09-12
toc: true
draft: false
description: "The six-phase red team methodology: mission preparation, OSINT, active reconnaissance, target exploitation, post exploitation, and mission objective, with the tools and judgment behind each."
genre: ["Red Team", "Offensive Security", "Methodology"]
tags: ["red team", "red team methodology", "mission preparation", "OSINT", "active reconnaissance", "target exploitation", "post exploitation", "mission objective", "adversary emulation", "red team course"]
cover: "/img/cover/red-team-methodology-six-phases-visualization.webp"
coverAlt: "An illustration of a circular flowchart representing the six phases of Red Team methodology, featuring vibrant colors against a dark background. Abstract elements suggest data streams and network connections."
coverCaption: "Module 1: the six phases every technique slots into."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**The six phases are the map for the whole course. Every technique you learn later slots into one of these phases, and operators revisit all of them throughout an operation.**

*This module takes about 15 minutes. Memorize the phases, then expect to loop.*

______

## The Six Phases

1. Mission Preparation
2. Open-Source Intelligence (OSINT)
3. Active Reconnaissance
4. Target Exploitation
5. Post Exploitation
6. Mission Objective

| Phase | What you do |
|-------|-------------|
| **Mission Preparation** | sign rules of engagement, stand up the platform and redirectors, confirm scope |
| **OSINT** | collect from public sources, generate no alerts |
| **Active Reconnaissance** | fingerprint, scan, enumerate, build the attack plan |
| **Target Exploitation** | run the plan with the simplest workable route |
| **Post Exploitation** | hold access, escalate, expand, fortify |
| **Mission Objective** | reach the point the operation existed to deliver |

*Do not treat the phases as a one-way street. New access restarts recon, and recon feeds a new plan.*

______

## Key Terms

Every phase leans on a small vocabulary. Lock these in first:

| Term | Plain meaning |
|------|---------------|
| **Rules of engagement (ROE)** | the signed document granting authority to operate and listing boundaries |
| **Scope / out-of-scope** | the targets you are allowed to touch, and the targets you must never touch |
| **Deconfliction** | the customer asking whether activity was you, and the fast honest answer |
| **Redirector** | a disposable outside host which hides your true origin |
| **Attack plan** | the prioritized list of targets and routes built by active recon |
| **Low hanging fruit** | the simplest workable vulnerability, the one you exploit first |
| **Foothold** | your initial access on a host, before persistence |
| **Domain controller (DC)** | the server holding the domain's hashes, the post-exploitation target |

______

## Mission Preparation

Before you touch anything, the paperwork and the platform are ready. Sign the **rules of engagement**. Stand up the attack platform and redirectors. Confirm the in-scope and out-of-scope lists. Most shops carry their own pre-operational checklist, so finish the organizational items to the customer's standard.

This phase is unglamorous and decides whether the operation happens at all. Getting it wrong means you either cannot operate, or you operate somewhere you were never authorized to be.

______

## Open-Source Intelligence

**OSINT** collects from public sources. Its defining trait: it never triggers an alert or a deconfliction. You read what is already public, not the customer's infrastructure.

- Google dork searches enumerate the target.
- Social profiles on LinkedIn and similar platforms map the people.
- IP lookups through **ARIN** tie public addresses to owners.

Be nosey and creative here. Good OSINT is often the difference between failing and getting in.

______

## Active Reconnaissance

Now you touch customer infrastructure, so your activity gets flagged and often triggers a deconfliction. You fingerprint the network, scan with `Nmap`, and enumerate web applications for weaknesses: **LFI/RFI**, file uploads, **SQL injection**, and **remote code execution (RCE)**.

The output is an attack plan. Log every step, because everything here lands on the target.

______

## Target Exploitation

You run the plan: attempt what active recon turned up (LFI/RFI, web shell uploads, RCE, SQL injection) and send phishing to the addresses OSINT surfaced.

**Low hanging fruit** matters. A red team is paid to take the simplest workable vulnerability and show its impact, not to find every bug. Find the easy way in, prove it matters, move on.

______

## Post Exploitation

The largest phase, broken into five parts:

- **User persistence** holds access across reboots.
- **Privilege escalation** moves from a normal user to privileged.
- **Privileged persistence** survives at the higher level.
- **Expanding access** reaches the domain controller.
- **Fortifying access** makes removal genuinely hard.

The through-line never changes: the domain controller holds the hashes, so post exploitation keeps pushing toward it.

______

## Mission Objective

The point of the operation. Objectives fall into three kinds:

- **Network effects**, like taking down an external server to test failover.
- **Specific information**, like changing one record on a workstation.
- **Demonstrated impact**, like reaching a Linux server storing customer data.

Access with no objective is noise. The objective turns a foothold into a finding the customer acts on.

> **Operator takeaway:** memorize the six phases as your default order of operations, but expect to loop. New access restarts recon, and recon feeds a new attack plan.

______

## What Each Phase Looks Like

| Phase | Example activity | Example tool |
|-------|------------------|--------------|
| **OSINT** | dork the domain, check ownership | Google operators, Whois, ARIN, Shodan, SpiderFoot |
| **Active Recon** | scan and fingerprint | `Nmap`, DNS tools, web proxies |
| **Exploitation** | phish, upload a web shell, or RCE | GoPhish, Cobalt Strike listener |
| **Post Exploitation** | persist, escalate, expand, fortify | `reg_set`, `sc_create`, `netGroupListMembers`, `hashcat` |
| **Objective** | locate the target, reach it, record impact | `ldapsearch`, `eventlog_query`, `portfwd` |

______

## Quiet vs Loud

| Phase | Touch the target? | Noise level |
|-------|-------------------|-------------|
| **OSINT** | no | none |
| **Active Recon** | yes | low, but logged |
| **Target Exploitation** | yes | moderate, deliberate |
| **Post Exploitation** | yes | depends on the technique |

The curve is deliberate. You start silent and add noise only as each phase earns it, because once a defender notices, they are chasing you for the rest of the operation.

______

## When to Loop

The phases are a cycle, not a line. Loop back when:

- New access lands, and you restart recon from the new host's view.
- A route dies, and recon feeds a fresh attack plan.
- The objective shifts, and you re-aim the whole chain.

*Expect to loop. An operation which never loops stayed above the surface, and never found the thing worth finding.*

______

## Plan Your Own Operation

Draft a phase-mapped plan for a sample target, a mid-size company with a public website and employee email. For each phase, write one concrete action and the tool you would use.

1. Mission Preparation: what is signed, and what do you stand up?
2. OSINT: what three sources do you check first?
3. Active Recon: which hosts and ports do you scan?
4. Target Exploitation: what is your simplest route in?
5. Post Exploitation: what is your first persistence move?
6. Mission Objective: what would you deliver as proof of impact?

A complete plan names a concrete action per phase, picks the quietest route available, and states the objective before the foothold. If any phase is blank, the operation stalls there.

______

## Common Mistakes

- Treating the six phases as a one-way checklist instead of a loop.
- Skipping OSINT and touching the target early, burning the quiet phase.
- Chasing every finding in exploitation instead of the simplest workable one.
- Failing to log active recon, so a deconfliction has no trail.

______

## Self-Check

1. Name the six phases in order.
2. Which phase must generate no alerts, and why?
3. Name the five parts of post exploitation.
4. Name the three kinds of mission objective.
5. Why is the objective decided before the foothold?

______

## Answer Key

**Self-Check**

1. **Mission Preparation, OSINT, Active Reconnaissance, Target Exploitation, Post Exploitation, Mission Objective.** The six phases form the default order of operations for the course.
2. **OSINT.** It reads only public data, touches nothing, and so generates no alerts and no deconfliction.
3. **User persistence, privilege escalation, privileged persistence, expanding access, fortifying access.** These five parts fill the largest phase.
4. **Network effects, specific information, demonstrated impact.** The three shapes the objective takes.
5. **The objective defines success before any foothold lands.** Access with no objective is noise, so the objective is decided first to keep the operation aimed.

**Exercise**

1. **The rules of engagement, signed by the network owner.** Plus the attack platform and redirectors, stood up and tested.
2. **A domain dork, an ownership lookup, and a social-media sweep.** Three public sources which never touch the customer.
3. **Only the in-scope hosts and the common external ports, scanned slow and quiet.** For example port 443 and 80 over a short list.
4. **The simplest workable route, low hanging fruit.** One crafty phishing message or an exposed upload beats an exhaustive hunt.
5. **Hold the foothold first.** A run key or service which returns after a reboot.
6. **Impact against the stated objective.** The changed record, the reached server, or the failover result, with evidence.

______

## Next Steps

With the map in hand, you start at the first phase. Next: mission preparation, infrastructure, and the rules keeping an operation legal.

**[→ Module 2: Mission Preparation and Infrastructure](/red-team-course/mission-preparation-and-infrastructure/)**

Or return to the hub: **[Red Team Course](/red-team-course-start/)**
