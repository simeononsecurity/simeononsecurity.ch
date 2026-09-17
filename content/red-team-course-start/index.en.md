---
title: "Red Team Course"
date: 2026-09-12
toc: true
draft: false
description: "A hands-on red team course covering methodology, command and control, reconnaissance, initial access, persistence, privilege escalation, Active Directory and Kerberos abuse, lateral movement, and reporting."
genre: ["Red Team", "Offensive Security", "Adversary Emulation", "Penetration Testing", "Command and Control", "Active Directory Attacks", "Ethical Hacking", "Cybersecurity"]
tags: ["red team", "red teaming", "red team operations", "adversary emulation", "offensive security", "penetration testing", "command and control", "Cobalt Strike", "persistence", "privilege escalation", "kerberoasting", "Active Directory", "lateral movement", "OSINT", "initial access", "phishing", "C2", "red team course", "ethical hacking"]
cover: "/img/cover/red-team-cybersecurity-methodology-illustration.webp"
coverAlt: "A digital illustration showing a cybersecurity command center with diverse professionals analyzing data on multiple screens, depicting a red team operation in a dark environment with vibrant accents."
coverCaption: "Operate like a red team, from the first recon query to the mission objective."
---

**This course walks the full adversary lifecycle end to end: methodology, command and control, reconnaissance, initial access, persistence, privilege escalation, Active Directory attacks, lateral movement, and reporting.** Each module pairs a technique with the tool or command executing it, drawn from lab-tested notes.

*Run every technique in an environment you are authorized to test. Nothing here belongs on a system you do not own or have permission to attack.*

______

## What You'll Learn

Red team work is a cycle, not a line. The course follows a six-phase methodology, then breaks post-exploitation into the techniques filling each phase.

| Phase | What happens |
|-------|--------------|
| **1. Mission Preparation** | Rules of engagement, platforms, and redirectors are ready before any touch |
| **2. Open-Source Intelligence** | Collect from public sources without tripping a single alert |
| **3. Active Reconnaissance** | Fingerprint the network, scan, and enumerate the attack surface |
| **4. Target Exploitation** | Turn recon into access with the simplest workable route |
| **5. Post Exploitation** | Hold access, escalate, expand, and fortify toward the domain controller |
| **6. Mission Objective** | Reach the point the whole operation existed to deliver |

*Expect to loop. New access restarts recon, and recon feeds a new attack plan.*

______

## Course Modules

| # | Module | Focus |
|---|--------|-------|
| 1 | [Red Team Methodology](/red-team-course/red-team-methodology/) | The six-phase operating model |
| 2 | [Mission Preparation and Infrastructure](/red-team-course/mission-preparation-and-infrastructure/) | ROE, platforms, and redirectors |
| 3 | [Networking and Active Directory](/red-team-course/foundations-networking-and-active-directory/) | Protocols and the domain model |
| 4 | [Windows Internals and Authentication](/red-team-course/foundations-windows-internals-and-authentication/) | Processes, tokens, and how Windows authenticates |
| 5 | [Command and Control Operations](/red-team-course/command-and-control-operations/) | Cobalt Strike setup and the C2 workflow |
| 6 | [Beacon Execution and BOFs](/red-team-course/beacon-execution-and-beacon-object-files/) | Running payloads and extending the beacon |
| 7 | [Malleable C2 and Communication Evasion](/red-team-course/malleable-c2-and-communication-evasion/) | Disguising traffic and C2 configuration |
| 8 | [Open-Source Intelligence](/red-team-course/open-source-intelligence/) | Search engines, Whois, Shodan, and SpiderFoot |
| 9 | [Active Reconnaissance and Scanning](/red-team-course/active-reconnaissance-and-scanning/) | Nmap and web application enumeration |
| 10 | [Initial Access: Phishing and Delivery](/red-team-course/initial-access-phishing-and-delivery/) | Payloads, phishing, and the first shell |
| 11 | [Situational Awareness and Host Operations](/red-team-course/situational-awareness-and-host-operations/) | Triage, filesystem, and discovery |
| 12 | [User Persistence](/red-team-course/user-persistence/) | Run keys, hiding files, and staying resident |
| 13 | [Local Privilege Escalation](/red-team-course/local-privilege-escalation/) | SharpUp, DLL hijacking, and misconfigurations |
| 14 | [Privileged Persistence and Process Migration](/red-team-course/privileged-persistence-and-process-migration/) | Services, sc.exe, and token reuse |
| 15 | [Persistence Cleanup and Defense Evasion](/red-team-course/persistence-cleanup-and-defense-evasion/) | Removing artifacts and blending in |
| 16 | [Domain Privilege Escalation and Kerberos Abuse](/red-team-course/domain-privilege-escalation-and-kerberos-abuse/) | Kerberoasting, tickets, and credential theft |
| 17 | [Lateral Movement and Expanding Access](/red-team-course/lateral-movement-and-expanding-access/) | SMB, services, and remote execution |
| 18 | [Cross-Domain Pivoting and LDAP Enumeration](/red-team-course/cross-domain-pivoting-and-ldap-enumeration/) | Trusts and ldapsearch |
| 19 | [Fortifying Access and Operator Discipline](/red-team-course/fortifying-access-and-operator-discipline/) | Digging in deep and staying resident |
| 20 | [Mission Objectives and Reporting](/red-team-course/mission-objectives-and-reporting/) | Discovery, exfiltration, and the writeup |

______

## Before You Start

You need a target environment you are allowed to attack. A local Windows domain in a hypervisor covers most of the course, and the rest only needs a browser and a scanning tool.

- A Windows domain lab with a domain controller and at least two workstations
- A Linux attack host running the tools referenced in each module
- A signed rules-of-engagement document spelling out your scope

**No version of this course is safe without an authorized target.** Build the lab first, then start at Module 1.

______

## Next Steps

Start at the beginning and work the modules in order, since each builds on the one before it.

**[→ Module 1: Red Team Methodology](/red-team-course/red-team-methodology/)**

For related offensive material, see the [CompTIA PenTest+ Course](/pentest-plus-start/) and the [Certified Ethical Hacker Course](/ceh-start/).
