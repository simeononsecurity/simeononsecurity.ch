---
title: "Module 2: Mission Preparation and Infrastructure"
date: 2026-09-12
toc: true
draft: false
description: "Everything required before an attack: scope and rules of engagement, deconfliction, hardening the attack platform, standing up redirectors, and validating the infrastructure before go."
genre: ["Red Team", "Offensive Security", "Infrastructure"]
tags: ["red team", "mission preparation", "rules of engagement", "scope", "deconfliction", "redirectors", "attack platform", "red team infrastructure", "C2 infrastructure", "red team course"]
cover: "/img/cover/red-team-mission-preparation-infrastructure.webp"
coverAlt: "An illustration of a high-tech workstation with multiple screens showing network maps and security documents, surrounded by visual elements like firewalls and encrypted data streams, all against a dark background."
coverCaption: "Module 2: ready the paperwork and the platform before the first packet."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**Mission preparation is everything you must line up before you attack.** Scope, authorization, redirectors, connectivity, and a locked-down platform. Skip it and you are either unable to operate, or operating outside your authorization.

*This module takes about 15 minutes. It decides whether the operation happens at all.*

> **Why it matters:** Authorization keeps you legal, and a broken redirector means a beacon which never checks in. The platform holds the customer's secrets, so compromise hands an adversary the crown jewels.

______

## Key Terms

| Term | Plain meaning |
|------|---------------|
| **Scope** | the targets and actions you are authorized to hit |
| **Out-of-scope** | the targets and actions you must never touch |
| **Rules of engagement (ROE)** | the signed authority to operate, with goals and boundaries |
| **Deconfliction** | the customer asking whether suspicious activity was you |
| **Redirector** | an outside server which hides your true origin |
| **Attack platform** | your workstation, which holds the customer's secrets |
| **SSL/TLS certificate** | the encrypted identity for your redirector domain |

______

## Scope and Out-of-Scope

**Scope** is the set of targets and actions you are authorized to attack. **Out-of-scope** is the explicit list you are prohibited from touching.

Both matter, and the out-of-scope list is the one keeping you out of legal trouble. Know both cold before the first packet leaves your platform. A target not in scope stays off-limits, even when it is trivially exploitable.

______

## Rules of Engagement

Red teaming requires written approval from the network owner. All parties sign a **Rules of Engagement (ROE)** document. A good ROE spells out:

- what the customer expects from the red team
- the goals and objectives of the assessment
- the allowed actions and boundaries
- the deconfliction channels

The ROE is your authority to operate, and your protection if something is questioned later. Read it. Do not skim it.

______

## Deconfliction

**Deconfliction** is when the customer asks whether suspicious activity was you. It matters in both directions.

For the red team, a slow or dishonest answer costs tools and credibility. For the customer, a fast honest answer lets them separate your activity from a genuine breach quickly. Real malicious activity hides behind the assumption a strange signal is the red team, so fast deconfliction keeps the assumption from becoming cover for an actual intruder. If the customer has little red team experience, they often need the concept explained first.

______

## Hardening the Attack Platform

The red team holds sensitive material in one place: hashes, customer files, and plaintext passwords. If your platform is compromised, you hand an adversary the customer's crown jewels.

Lock it down with a default-deny policy which allows only your redirectors and the customer's address space:

```text
iptables -A INPUT -s <redirector-ip> -j ACCEPT
iptables -A INPUT -s <customer-cidr> -j ACCEPT
iptables -A INPUT -j DROP
```

Plus:

- Blackhole or disable any unneeded ports and services.
- Change every default password to a unique new one.

> **Operator takeaway:** your attack platform is the richest target in the engagement. Lock it down before you fill it with the customer's secrets.

______

## Redirectors

A **redirector** is a system outside your network which reaches the customer without exposing your true address, usually a virtual private server from a hosting provider.

Why they matter:

- You interact with the customer over the open internet, the way a real attacker does.
- It sidesteps local ISP policy on your own connection.
- It emulates ordinary user traffic, a client browsing over HTTPS.

Run one redirector for active operations, and keep two or more as low-and-slow backups for emergencies only.

______

## Standing Up a Redirector

The steps which matter:

1. Register the server and TLS certificate, and point a domain at it.
2. Categorize the domain and server through a filtering vendor. New, uncategorized domains are blocked by many firewalls.
3. Test the redirector before a live operation. Browse to it on port 443 and confirm the command and control listener answers.

Port 443 HTTPS routes back to your attack machine. The redirector makes beacon traffic originate from somewhere other than your own space, and HTTPS is the cover letting it look like a workstation browsing a website.

> **Operator takeaway:** the redirector and the listener must be correct before anything works. A broken link means your beacon never checks in.

______

## What Each Piece Is For

| Piece | Purpose |
|-------|---------|
| **Attack platform** | holds and protects the customer's secrets |
| **Redirector** | presents your traffic from an outside address |
| **Domain + TLS** | gives the redirector a browsable, trusted identity |
| **SMTP server** | sends the phishing campaign |
| **C2 listener** | receives the beacon callbacks |

______

## Phishing SMTP Server

Phishing needs a sending path. A standalone SMTP server you control lets a campaign deliver mail without routing through a third party you do not own.

{{< youtube id="mRUGEygkDEQ" >}}

Watch the setup: [SMTP server build for phishing](https://www.youtube.com/watch?v=mRUGEygkDEQ)

______

## Prepare Your Own Mission

Draft a prep checklist for a sample engagement. For each item, write what you would do and where:

1. Who signs, and what does the ROE list?
2. What is in scope, and what is explicitly out?
3. How do you harden the attack platform?
4. How many redirectors, and why?
5. How do you verify the redirector before go?

A complete checklist names the signers, the scope lists, the hardening steps, the redirector count, and the verification step. If any is missing, the operation is not ready.

______

## Why Infrastructure Choices Matter

Infrastructure separates operator traffic from the customer network and gives defenders useful indicators for detection. Disposable domains and unmanaged hosting were common in older operations, but they create ownership and abuse problems. A current lab uses registered assets, short-lived certificates, access logging, and an explicit teardown record. **Do not route test traffic through infrastructure outside the written scope.**

______

## Common Mistakes

- Skipping the out-of-scope list and touching a target never authorized.
- Standing up a redirector with an uncategorized domain, so firewalls block it.
- Reusing default passwords on the attack platform.
- Failing to test the redirector to listener path before go.

______

## Self-Check

1. What does the Rules of Engagement give you?
2. Why does fast deconfliction matter in both directions?
3. Name two hardening steps for the attack platform.
4. Why does a redirector hide your true origin?
5. Why categorize the redirector domain before go?

______

## Answer Key

**Self-Check**

1. **Authority to operate and protection.** The ROE grants written permission and lists goals and boundaries.
2. **It separates your activity from a real intruder.** Fast honest answers stop a genuine breach from hiding as the red team, and protect your credibility.
3. **Default-deny firewall rules and unique passwords.** Block everything except redirectors and the customer's addresses, and replace every default credential.
4. **It presents your traffic from an outside address.** The beacon appears to come from a disposable server, not your own space.
5. **New domains are blocked by many firewalls.** Categorization lets the traffic through where an uncategorized domain dies.

**Exercise**

1. **The network owner signs the ROE, listing goals, scope, and deconfliction channels.**
2. **In scope are the named customer systems. Out of scope is everything else, off-limits no matter how easy.**
3. **Default-deny iptables, no extra services, fresh passwords.**
4. **One active redirector plus two low-and-slow backups.**
5. **Browse the redirector on port 443 and confirm the C2 listener answers.**

______

## Next Steps

Infrastructure is ready. Next, the technical baseline for reading the target: networking and Active Directory.

**[→ Module 3: Networking and Active Directory Foundations](/red-team-course/foundations-networking-and-active-directory/)**

Or return to the hub: **[Red Team Course](/red-team-course-start/)**
