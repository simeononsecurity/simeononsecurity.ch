---
title: "CEH v13: Denial-of-Service"
date: 2025-01-01
toc: true
draft: false
description: "Master denial-of-service for the EC-Council Certified Ethical Hacker (CEH v13) exam. Learn DoS vs DDoS, volumetric, protocol, and application attacks, amplification, botnets, and defenses."
genre: ["EC-Council CEH Course", "Ethical Hacking", "Penetration Testing", "Offensive Security", "Cybersecurity", "Network Security", "Security Testing", "Hacking Techniques", "CEH Certification", "Information Security"]
tags: ["CEH", "CEH v13", "ethical hacking", "EC-Council", "penetration testing", "denial-of-service", "offensive security", "cybersecurity", "hacking", "security testing"]
cover: "/img/cover/ceh-v13-denial-of-service-attacks-techniques-defense.webp"
coverAlt: "An illustration showing a network under cyber attack, with colorful data packets and abstract shapes representing botnets and amplification methods on a dark background."
coverCaption: "Master Denial-of-Service for the CEH v13 Exam"
---

#### [Click Here to Return To the Certified Ethical Hacker (CEH v13) Course Page](/ceh-start/)

**Denial-of-Service** attacks disrupt availability in the **EC-Council CEH v13** course. This module covers DoS and DDoS techniques, attack categories, botnets, and the defenses that absorb them. *Run flooding tools only against isolated lab systems you own, never against live targets.*

A denial-of-service attack overwhelms a system so legitimate users lose access. It targets the **availability** pillar of the CIA triad rather than stealing data.

## DoS vs. DDoS

The difference is the number of sources.

| Attack | Sources | Harder to block |
|--------|---------|-----------------|
| **DoS** | One host | No |
| **DDoS** | Many hosts (a botnet) | Yes |

A **botnet** is a network of compromised devices a **command-and-control** server directs to flood a target at once.

## Attack Categories

You group attacks by the layer they hit.

- **Volumetric** attacks flood bandwidth (UDP floods, ICMP floods).
- **Protocol** attacks exhaust connection tables (SYN floods).
- **Application-layer** attacks exhaust server resources with valid-looking requests (HTTP floods).

**Amplification and reflection** make small requests produce huge responses. An attacker spoofs the victim's IP, queries open DNS or NTP servers, and those servers blast large replies at the victim.

## Tools in the Lab

| Tool | Use |
|------|-----|
| **hping3** | Crafts custom flood packets |
| **LOIC / HOIC** | Simple flooding utilities |
| **Slowloris** | Holds many slow connections open |

```bash
# Lab-only SYN flood simulation against an isolated host
sudo hping3 -S --flood -p 80 10.0.0.5
```

## Defenses

You absorb and filter attack traffic with layered controls.

- **Rate limiting** caps requests per source.
- **Scrubbing centers** filter malicious traffic before it reaches you.
- **Anycast** spreads traffic across many data centers.
- **A CDN** absorbs volumetric load at the edge.

*Defense works best upstream, because a flood that fills your link cannot be stopped at your firewall.*

## Next Steps

Take over live sessions in [Session Hijacking](/ceh/session-hijacking/). Revisit human attacks in [Social Engineering](/ceh/social-engineering/). Return to the [Certified Ethical Hacker (CEH v13) Course](/ceh-start/).
