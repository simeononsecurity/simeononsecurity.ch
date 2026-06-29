---
title: "CEH v13: System Hacking"
date: 2025-01-01
toc: true
draft: false
description: "Master system hacking for the EC-Council Certified Ethical Hacker (CEH v13) exam. Learn password cracking, Metasploit exploitation, privilege escalation, maintaining access, and clearing tracks."
genre: ["EC-Council CEH Course", "Ethical Hacking", "Penetration Testing", "Offensive Security", "Cybersecurity", "Network Security", "Security Testing", "Hacking Techniques", "CEH Certification", "Information Security"]
tags: ["CEH", "CEH v13", "ethical hacking", "EC-Council", "penetration testing", "system hacking", "offensive security", "cybersecurity", "hacking", "security testing"]
cover: "/img/cover/ceh-v13-system-hacking-access-privilege-escalation.webp"
coverAlt: "A digital illustration showing a computer terminal with flowing binary code, stylized icons representing hacking tools, layered structures for access levels, and hidden files, all on a dark background."
coverCaption: "Master System Hacking for the CEH v13 Exam"
---

#### [Click Here to Return To the Certified Ethical Hacker (CEH v13) Course Page](/ceh-start/)

**System Hacking** covers gaining and keeping access in the **EC-Council CEH v13** course. This module covers password attacks, exploitation, privilege escalation, persistence, and covering tracks. *Run these techniques only against systems named in your signed scope.*

This is where reconnaissance pays off. You turn a confirmed vulnerability or weak credential into a shell, then climb from a low-privilege account to full control.

## The System Hacking Methodology

You follow four stages once you have a target.

1. **Gaining access** through a weak password or an exploit.
2. **Escalating privileges** from a normal user to administrator or root.
3. **Maintaining access** with a backdoor or scheduled task.
4. **Clearing tracks** by cleaning logs and artifacts.

## Password Attacks

Passwords are the most common way in. You attack them several ways.

| Attack | Method |
|--------|--------|
| **Dictionary** | Tries words from a list |
| **Brute force** | Tries every combination |
| **Hybrid** | Words plus numbers and symbols |
| **Rainbow table** | Precomputed hash lookups |
| **Credential stuffing** | Reuses breached passwords |

```bash
# Crack captured hashes with a wordlist
hashcat -m 1000 hashes.txt rockyou.txt
john --format=nt hashes.txt --wordlist=rockyou.txt
```

**Salting** defeats rainbow tables by adding random data before hashing. Strong, unique passwords remain the best defense, covered in [how to create strong passwords](/articles/how-to-create-strong-passwords/). Generate and compare hashes with the on-site [hash calculator](/hash-calculator/).

## Exploitation with Metasploit

The **Metasploit Framework** packages exploits, payloads, and post-exploitation modules.

```bash
# Search, configure, and launch an exploit module
msf6 > search type:exploit name:smb
msf6 > use exploit/windows/smb/ms17_010_eternalblue
msf6 > set RHOSTS 192.168.1.10
msf6 > exploit
```

A successful exploit returns a session, often a **Meterpreter** shell with built-in post-exploitation commands.

## Privilege Escalation and Persistence

A low-privilege shell rarely ends the job. You escalate using:

- **Kernel exploits** against unpatched operating systems.
- **Misconfigured services** running as SYSTEM or root.
- **Weak file permissions** and stored credentials.

You maintain access with backdoors, new accounts, or scheduled tasks. **Clearing tracks** then removes log entries and timestamps, though defenders use forwarded logs to detect tampering. *Document every change you make so the client restores a clean state after the test.*

## Next Steps

Study the malicious code attackers plant in [Malware Threats](/ceh/malware-threats/). Revisit weakness selection in [Vulnerability Analysis](/ceh/vulnerability-analysis/). Return to the [Certified Ethical Hacker (CEH v13) Course](/ceh-start/).
