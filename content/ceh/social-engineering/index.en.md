---
title: "CEH v13: Social Engineering"
date: 2025-01-01
toc: true
draft: false
description: "Master social engineering for the EC-Council Certified Ethical Hacker (CEH v13) exam. Learn phishing, vishing, smishing, pretexting, impersonation, GoPhish, and awareness defenses."
genre: ["EC-Council CEH Course", "Ethical Hacking", "Penetration Testing", "Offensive Security", "Cybersecurity", "Network Security", "Security Testing", "Hacking Techniques", "CEH Certification", "Information Security"]
tags: ["CEH", "CEH v13", "ethical hacking", "EC-Council", "penetration testing", "social engineering", "offensive security", "cybersecurity", "hacking", "security testing"]
cover: "/img/cover/ceh-v13-social-engineering-attacks.webp"
coverAlt: "An illustration showing a hacker at a computer with visual symbols of phishing emails and phone calls, surrounded by silhouettes of individuals representing social engineering vulnerabilities."
coverCaption: "Master Social Engineering for the CEH v13 Exam"
---

#### [Click Here to Return To the Certified Ethical Hacker (CEH v13) Course Page](/ceh-start/)

**Social Engineering** targets people rather than systems in the **EC-Council CEH v13** course. This module covers the psychology of manipulation, common attack vectors, and the awareness defenses that reduce human risk. *All social engineering testing requires explicit written scope and rules of engagement.*

People are the easiest path past strong technical controls. Social engineering exploits trust, fear, urgency, and the wish to be helpful.

## Why It Works

Attackers exploit predictable human triggers.

- **Authority** makes people obey a perceived boss or official.
- **Urgency** rushes a victim past careful thought.
- **Scarcity** pressures action before an offer ends.
- **Trust and familiarity** lower a target's guard.

## Attack Vectors

| Vector | Channel |
|--------|---------|
| **Phishing** | Mass deceptive email |
| **Spear phishing** | Targeted email to one person |
| **Whaling** | Targets executives |
| **Vishing** | Voice calls |
| **Smishing** | SMS text messages |
| **Pretexting** | A fabricated backstory |

Physical techniques include **tailgating** (following someone through a door), **baiting** (a dropped malicious USB), and **impersonation** of staff or vendors.

## Phishing Simulations

You test user awareness with controlled campaigns. A framework like **GoPhish** sends tracked emails and measures who clicks, who submits credentials, and who reports the message.

```text
1. Build a template that mimics a real sender
2. Import a scoped target list
3. Launch and track opens, clicks, and submissions
4. Report metrics and deliver targeted training
```

*A campaign measures behavior, so design it to teach, not to shame.*

## Defenses

You lower human-factor risk with layered controls.

- **Security awareness training** teaches staff to spot and report attacks.
- **Email filtering** and **DMARC** block spoofed senders.
- **MFA** limits damage when credentials are phished, building on [strong password practices](/articles/how-to-create-strong-passwords/).
- **Verification procedures** confirm requests for money or access through a second channel.

## Next Steps

Move into network disruption attacks in [Denial-of-Service](/ceh/denial-of-service/). Revisit traffic interception in [Sniffing](/ceh/sniffing/). Return to the [Certified Ethical Hacker (CEH v13) Course](/ceh-start/).
