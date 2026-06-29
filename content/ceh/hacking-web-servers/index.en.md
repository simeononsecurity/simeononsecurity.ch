---
title: "CEH v13: Hacking Web Servers"
date: 2025-01-01
toc: true
draft: false
description: "Master hacking web servers for the EC-Council Certified Ethical Hacker (CEH v13) exam. Learn web server enumeration, misconfigurations, directory traversal, common attacks, and hardening with Nikto and dirb."
genre: ["EC-Council CEH Course", "Ethical Hacking", "Penetration Testing", "Offensive Security", "Cybersecurity", "Network Security", "Security Testing", "Hacking Techniques", "CEH Certification", "Information Security"]
tags: ["CEH", "CEH v13", "ethical hacking", "EC-Council", "penetration testing", "hacking web servers", "offensive security", "cybersecurity", "hacking", "security testing"]
cover: "/img/cover/ceh-v13-hacking-web-servers-security.webp"
coverAlt: "An illustration of a web server rack with glowing highlights indicating vulnerabilities, set against a dark background. Abstract representations of hacking tools are also visible."
coverCaption: "Master Hacking Web Servers for the CEH v13 Exam"
---

#### [Click Here to Return To the Certified Ethical Hacker (CEH v13) Course Page](/ceh-start/)

**Hacking Web Servers** targets the server layer in the **EC-Council CEH v13** course. This module covers enumerating web server software, finding misconfigurations, and hardening the platform. *Scan and exploit web servers only inside your authorized scope.*

A web server runs the software (Apache, IIS, Nginx) that hosts the application. Flaws in that platform open the door before you ever touch the application code.

## Web Server Enumeration

You fingerprint the server and map its content.

```bash
# Scan for known web server flaws and brute-force directories
nikto -h http://target.example
dirb http://target.example /usr/share/wordlists/dirb/common.txt
```

**Nikto** checks for outdated versions and dangerous files. **dirb** and **gobuster** brute-force hidden directories and pages. Verbose error messages and default pages reveal the software and version.

## Common Web Server Attacks

| Attack | Result |
|--------|--------|
| **Directory traversal** | Reads files outside the web root |
| **Default credentials** | Logs into admin panels |
| **Defacement** | Replaces site content |
| **DNS hijacking** | Redirects visitors elsewhere |
| **Cache poisoning** | Serves malicious cached content |

Directory traversal uses sequences like `../../etc/passwd` to escape the web root and read system files.

## Exploitation and Hardening

You match a discovered version to a known exploit, often through **Metasploit modules** for Apache, IIS, or Nginx. You then report fixes:

- **Patch** the server and remove unused modules.
- **Disable** directory listing and verbose errors.
- **Deploy a WAF** to filter malicious requests.
- **Enforce HTTPS** and strong TLS settings.

Check a site's response headers with the on-site [security headers tool](/securityheaders/). *A patched server with a clean configuration removes most of these attacks at once.*

## Next Steps

Move up the stack to [Hacking Web Applications](/ceh/hacking-web-applications/). Revisit defense evasion in [Evading IDS, Firewalls, and Honeypots](/ceh/evading-ids-firewalls-honeypots/). Return to the [Certified Ethical Hacker (CEH v13) Course](/ceh-start/).
