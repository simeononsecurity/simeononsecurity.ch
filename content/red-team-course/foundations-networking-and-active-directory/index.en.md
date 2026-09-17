---
title: "Module 3: Networking and Active Directory Foundations"
date: 2026-09-12
toc: true
draft: false
description: "The networking and Active Directory concepts every red team technique builds on: HTTP and HTTPS, TCP and UDP, the domain controller, users, groups, and group nesting."
genre: ["Red Team", "Offensive Security", "Networking", "Active Directory"]
tags: ["red team", "networking", "TCP", "UDP", "HTTP", "HTTPS", "Active Directory", "domain controller", "group nesting", "foundations", "red team course"]
cover: "/img/cover/networking-active-directory-foundations-illustration.webp"
coverAlt: "An illustration showing a central Domain Controller connected to various nodes representing users and groups, with visual elements symbolizing networking protocols like HTTP, HTTPS, TCP, and UDP."
coverCaption: "Module 3: the ground every later technique stands on."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**Before any tool comes out, you need the networking and Active Directory concepts every later technique leans on.** HTTP and HTTPS, TCP and UDP, and the structure of a Windows domain decide how your traffic looks on the wire and how you plan an escalation.

*This module is foundational reading for the whole course, about 12 minutes. Do not skip it.*

______

## Key Terms

| Term | Plain meaning |
|------|---------------|
| **HTTP / HTTPS** | unencrypted vs encrypted web traffic |
| **TCP** | reliable transport with a handshake |
| **UDP** | fast transport with no delivery guarantee |
| **Active Directory (AD)** | the domain's central directory of users and hosts |
| **Domain Controller (DC)** | the server holding the domain's hashes |
| **Group nesting** | a group inside another group |

______

## Why Foundations First

A red team levels these concepts to a shared baseline before tooling appears. When you stare at a callback and decide how it should look on the wire, or read a group membership to plan an escalation, you are using exactly this material.

Skip it and the later techniques have no context. Every persistence trick, every Kerberos abuse, and every lateral movement you learn later sits on top of these few ideas.

______

## HTTP vs HTTPS

`HTTP` and `HTTPS` are web protocols running over TCP. **HTTP is unencrypted, HTTPS is encrypted.**

On plain HTTP, anyone listening on the wire reads every byte between client and server. On an open wireless hotspot, a listener sees each page you load in the clear. On HTTPS, a listener sees only ciphertext.

The red team angle shows up immediately. Normal web traffic is plaintext, and most remote access tools wrap their commands in encryption. Encrypted data riding over an HTTP channel is a tell, because plaintext pages should not contain ciphertext. A defender who sees ciphertext where cleartext pages belong has reason to look closer.

> **Operator takeaway:** match the wrapper to the protocol. Encrypted payloads over HTTP look wrong. Encrypted payloads over HTTPS look like normal browsing.

Use HTTPS when you control the choice. Your C2 blends better when its encryption matches the protocol carrying it. This is why your listener selection later favors HTTPS for a client network, and why an HTTP beacon on an internet-facing host reads as noise.

______

## TCP vs UDP

**TCP is connection-oriented.** A client opens a session with a three-way handshake (`SYN`, `SYN-ACK`, `ACK`) and confirms data arrived intact with checksums.

**UDP is connectionless.** One host sends to another without confirming the port is open or every packet landed.

| Protocol | Trait | Used for |
|----------|-------|----------|
| **TCP** | reliable handshake, delivery checks | web pages, banking, downloads |
| **UDP** | fast, no delivery guarantee | streaming, voice, real time |

Streaming and real-time services choose UDP because speed matters more than perfect delivery. Live audio and call video trade lost packets for lower latency.

The TCP handshake matters to an attacker because defenders watch it. A burst of `SYN` packets from one host is the classic signature of a port scan. During active reconnaissance you watch for exactly this tell, both when you run a scan and when you shape your own traffic to avoid tripping it.

______

## Active Directory and the Domain Controller

**Active Directory (AD)** is the directory service for Windows domain networks. It registers users, computers, printers, and other principals in one central database.

Larger organizations split the database across a hierarchy of parent and child domains, for example `corp.local` with `chicago.corp.local` and `detroit.corp.local` beneath it.

The central database runs on the **Domain Controller (DC)**. The DC stores password hashes, every computer in the domain, and every user and group. It is the prize, because the domain's credential material lives on it.

> **Operator takeaway:** the DC holds the hashes for the whole domain. A large share of post-exploitation work exists to push toward it.

______

## Users, Groups, and Nesting

AD grants permission through **groups**, not one account at a time. Add a user to a group and the user inherits everything the group does.

Groups also contain other groups, which is where mapping becomes messy. A user not listed in Domain Admins directly still inherits it through a chain of groups.

| Concept | Meaning | Why it matters |
|---------|---------|----------------|
| **User** | an account for a person or service | holds credentials you reuse |
| **Group** | a set of users or groups with shared rights | permission inheritance |
| **Nesting** | a group inside another group | hidden inheritance to admin rights |

Read the group names to map which principals hold which rights. Typical names tell the story: `Workstation Admins`, `Server Admins`, `Domain Admins`, `Exchange Admins`. A well-run domain separates these privileges. A poorly run domain collapses them, and the collapse is an escalation path you hunt for. This is why group enumeration gets dedicated tooling later in the course.

______

## These Concepts Feed Your Tooling

Every idea above maps to a command you run later. Keep the mapping in view:

| Concept | Tool it feeds | What you do with it |
|---------|---------------|---------------------|
| **HTTPS** | a C2 listener | choose HTTPS for a client network so beacons browse like users |
| **TCP handshake** | `nmap` | `-sS` SYN scan lights up exactly what defenders watch |
| **Domain Controller** | `netGroupListMembers` | enumerate `Domain Controllers` to locate the target host |
| **Group nesting** | `netGroupListMembers` | enumerate `Domain Admins` and chase nested members |

______

## Reason About Your Traffic and Domain

Given a callback on a workstation inside a customer domain:

1. Should the beacon ride HTTP or HTTPS, and why?
2. Where do the domain's hashes live, and which host do you aim toward?
3. You find a user absent from Domain Admins but reachable through two nested groups. What does this tell you?
4. Which transport carries your C2, and why?

Answer from memory first. The explanations are in the Answer Key at the end.

______

## Common Mistakes

- Running an encrypted payload over plain HTTP, so the ciphertext rides where cleartext belongs.
- Forgetting the TCP handshake is a detectable signature, then hammering a target with `SYN` packets.
- Confusing a local group with a domain group, or the reverse.
- Treating a group listing as flat, and missing the nested membership which grants the real privilege.

______

## Self-Check

Before moving on, answer these from memory:

1. Why does encrypted C2 over HTTP stand out, and over HTTPS does not?
2. Order the three-way handshake packets.
3. Why is the domain controller the prize?
4. What is group nesting, and why does it matter to an operator?

If any answer is thin, reread the matching section. These four ideas recur in every later module.

______

## Answer Key

**Self-Check**

1. **Plaintext should not carry ciphertext.** Encrypted C2 over HTTP is visible as an oddity, while HTTPS hides it inside normal browsing.
2. **SYN, SYN-ACK, ACK.** The three packets which open a TCP session.
3. **It holds every domain hash.** The DC stores the hashes for the whole domain, so it is the post-exploitation target.
4. **A group inside another group, which grants inherited rights.** A user outside Domain Admins still reaches admin through the chain.

**Exercise**

1. **HTTPS.** It reads as browsing and hides the payload.
2. **On the domain controller.** Aim at the DC to reach the hashes.
3. **The user inherits admin through nesting.** Absent from Domain Admins yet still admin via the groups.
4. **TCP.** A callback needs reliable, ordered delivery.

______

## Next Steps

Networking and the domain model are the ground floor. Next comes the Windows internals behind every later technique: processes, tokens, and how authentication works.

**[→ Module 4: Windows Internals and Authentication](/red-team-course/foundations-windows-internals-and-authentication/)**

Or return to the hub: **[Red Team Course](/red-team-course-start/)**
