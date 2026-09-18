---
title: "Red Team Course"
date: 2026-09-12
lastmod: 2026-09-17
toc: true
draft: false
description: "A structured red-team course that moves from objective and evidence design through reconnaissance, access, identity, persistence, movement, and reporting."
genre: ["Red Team", "Offensive Security", "Adversary Emulation", "Penetration Testing", "Active Directory"]
tags: ["red team", "red teaming", "adversary emulation", "offensive security", "Cobalt Strike", "Active Directory", "lateral movement", "reporting", "red team course"]
cover: "/img/cover/red-team-cybersecurity-methodology-illustration.webp"
coverAlt: "A digital illustration showing a cybersecurity command center with diverse professionals analyzing data on multiple screens, depicting a red team operation in a dark environment with vibrant accents."
coverCaption: "Build an evidence-backed red-team mission"
---

**This course follows a red-team mission from an approved question to a reviewable result.** Each module connects a technique to identity, scope, evidence, and recovery. The sequence develops from definitions and explanations into bounded actions, comparisons, decisions, and reader-created records.

*Use the material only in an environment you are authorized to test. Treat every example as a lab exercise unless the engagement rules say otherwise.*

## What You Will Learn

The course is a loop of **objective, preparation, observation, access, analysis, cleanup, backout, and reporting**. New evidence can change the objective or next action, so the modules teach records that survive a change in plan.

| Stage | Reader outcome |
|---|---|
| **Prepare** | Scope, roles, infrastructure, and stopping conditions |
| **Understand** | Network, Windows, identity, and protocol behavior |
| **Observe** | OSINT, scanning, host state, and service evidence |
| **Access** | Delivery, execution, persistence, and privilege boundaries |
| **Expand carefully** | Kerberos, movement, trusts, and LDAP scope |
| **Clean up and back out** | Remove owned artifacts, restore changes, and verify the baseline |
| **Report** | Objective, evidence, impact, remediation, and retest |

## Course Modules

| # | Module | Reader artifact |
|---|---|---|
| 1 | [Red Team Methodology](/red-team-course/red-team-methodology/) | Objective and evidence review loop |
| 2 | [Mission Preparation and Infrastructure](/red-team-course/mission-preparation-and-infrastructure/) | Readiness and responsibility register |
| 3 | [Networking and Active Directory](/red-team-course/foundations-networking-and-active-directory/) | Dependency and access map |
| 4 | [Windows Internals and Authentication](/red-team-course/foundations-windows-internals-and-authentication/) | Identity, token, and registry context record |
| 5 | [Command and Control Operations](/red-team-course/command-and-control-operations/) | Task delivery and result ledger |
| 6 | [Beacon Execution and BOFs](/red-team-course/beacon-execution-and-beacon-object-files/) | Compatibility and failure record |
| 7 | [Malleable C2 and Communication Evasion](/red-team-course/malleable-c2-and-communication-evasion/) | Controlled traffic comparison |
| 8 | [Open-Source Intelligence](/red-team-course/open-source-intelligence/) | Provenance and research brief |
| 9 | [Active Reconnaissance and Scanning](/red-team-course/active-reconnaissance-and-scanning/) | Scan manifest and response interpretation |
| 10 | [Initial Access: Phishing and Delivery](/red-team-course/initial-access-phishing-and-delivery/) | Delivery and interaction test specification |
| 11 | [Situational Awareness and Host Operations](/red-team-course/situational-awareness-and-host-operations/) | Host-state snapshot |
| 12 | [User Persistence](/red-team-course/user-persistence/) | Startup lifecycle record |
| 13 | [Local Privilege Escalation](/red-team-course/local-privilege-escalation/) | Permission-boundary evidence chain |
| 14 | [Privileged Persistence and Process Migration](/red-team-course/privileged-persistence-and-process-migration/) | Service and process lifecycle record |
| 15 | [Persistence Cleanup and Defense Evasion](/red-team-course/persistence-cleanup-and-defense-evasion/) | Restoration and backout ledger |
| 16 | [Domain Privilege Escalation and Kerberos Abuse](/red-team-course/domain-privilege-escalation-and-kerberos-abuse/) | Ticket and privilege review |
| 17 | [Lateral Movement and Expanding Access](/red-team-course/lateral-movement-and-expanding-access/) | Movement path ledger |
| 18 | [Cross-Domain Pivoting and LDAP Enumeration](/red-team-course/cross-domain-pivoting-and-ldap-enumeration/) | Trust and query decision record |
| 19 | [Fortifying Access and Operator Discipline](/red-team-course/fortifying-access-and-operator-discipline/) | Access and failover plan |
| 20 | [Mission Objectives and Reporting](/red-team-course/mission-objectives-and-reporting/) | Mission finding package |

## How To Use It

Start with [Module 1: Red Team Methodology](/red-team-course/red-team-methodology/). Read each module's terms and explanation before attempting its lab action. The worked example then shows how to apply the idea, while the comparison and self-check sections ask you to judge evidence and limits.

Keep the **reader artifact** from each module. The next module uses it as an input, so the course becomes a connected assessment record instead of twenty unrelated command lists. When a module describes an expected result, label it as expected until your authorized lab produces an observation.

## Prerequisites

Use a disposable lab with a Windows domain controller, Windows workstations, and a Linux analysis host. Keep an engagement document that names the assets, identities, time window, data handling rules, owner contacts, and stop conditions. Several commands are Windows-specific and are documented rather than executed on the macOS authoring system.

**The course does not grant permission to test a real system.** Obtain written authorization and use the smallest scope that answers the mission question.

## After Module 20

Review the [CompTIA PenTest+ Course](/pentest-plus-start/) and [Certified Ethical Hacker Course](/ceh-start/) for related study. Reuse the mission finding package when you design a new approved exercise, then update the evidence and retest fields with observed results.
