---
title: "CEH v13: Hacking Web Applications"
date: 2025-01-01
toc: true
draft: false
description: "Master hacking web applications for the EC-Council Certified Ethical Hacker (CEH v13) exam. Learn the OWASP Top 10, Burp Suite, broken access control, injection, LFI/RFI, XXE, and secure coding defenses."
genre: ["EC-Council CEH Course", "Ethical Hacking", "Penetration Testing", "Offensive Security", "Cybersecurity", "Network Security", "Security Testing", "Hacking Techniques", "CEH Certification", "Information Security"]
tags: ["CEH", "CEH v13", "ethical hacking", "EC-Council", "penetration testing", "hacking web applications", "offensive security", "cybersecurity", "hacking", "security testing"]
cover: "/img/cover/ceh-v13-hacking-web-applications-owasp-top-10.webp"
coverAlt: "An illustration of a computer screen showing code and web elements under attack, with visual effects like glowing cracks and arrows indicating vulnerabilities, set against a dark navy background."
coverCaption: "Master Hacking Web Applications for the CEH v13 Exam"
---

#### [Click Here to Return To the Certified Ethical Hacker (CEH v13) Course Page](/ceh-start/)

**Hacking Web Applications** targets the application layer in the **EC-Council CEH v13** course. This module covers the OWASP Top 10, request interception, and the secure coding practices that close these flaws. *Test web applications only against in-scope targets you are authorized to assess.*

The web server hosts the platform. The application is the custom code on top, and that is where most exploitable bugs live.

## The OWASP Top 10

The **OWASP Top 10** ranks the most critical web application risks.

| Risk | Example |
|------|---------|
| **Broken access control** | Reaching another user's data |
| **Injection** | SQL, command, and LDAP injection |
| **Cryptographic failures** | Weak or missing encryption |
| **Security misconfiguration** | Default settings, open admin |
| **Insecure design** | Flaws built into the logic |

## Intercepting Requests with Burp Suite

You sit between the browser and the server to read and modify traffic. **Burp Suite** is the standard proxy for this.

```text
1. Set the browser proxy to Burp (127.0.0.1:8080)
2. Capture a request in the Proxy tab
3. Send it to Repeater to modify and replay
4. Use Intruder to fuzz parameters
```

This reveals hidden parameters and lets you tamper with values the application trusts.

## Common Application Attacks

- **Broken access control** and **insecure direct object references (IDOR)** expose data by changing an ID in the request.
- **Command injection** runs OS commands through unsanitized input.
- **File inclusion** (LFI/RFI) loads local or remote files into the application.
- **XML external entity (XXE)** abuses XML parsers to read files or reach internal systems.

## Defenses

You remediate at the code level.

- **Validate and sanitize** all input on the server side.
- **Use parameterized queries** to stop injection.
- **Enforce access control** checks on every request.
- **Apply least privilege** to the application's database account.

## Next Steps

Go deep on the most famous injection flaw in [SQL Injection](/ceh/sql-injection/). Revisit the platform layer in [Hacking Web Servers](/ceh/hacking-web-servers/). Return to the [Certified Ethical Hacker (CEH v13) Course](/ceh-start/).
