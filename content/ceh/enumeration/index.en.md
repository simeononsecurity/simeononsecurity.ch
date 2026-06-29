---
title: "CEH v13: Enumeration"
date: 2025-01-01
toc: true
draft: false
description: "Master enumeration for the EC-Council Certified Ethical Hacker (CEH v13) exam. Learn NetBIOS, SNMP, LDAP, SMB, and DNS enumeration with tools like enum4linux, SNMPwalk, and NBTscan."
genre: ["EC-Council CEH Course", "Ethical Hacking", "Penetration Testing", "Offensive Security", "Cybersecurity", "Network Security", "Security Testing", "Hacking Techniques", "CEH Certification", "Information Security"]
tags: ["CEH", "CEH v13", "ethical hacking", "EC-Council", "penetration testing", "enumeration", "offensive security", "cybersecurity", "hacking", "security testing"]
cover: "/img/cover/ceh-v13-enumeration-network-protocols-security.webp"
coverAlt: "An abstract illustration showing a network structure with nodes and connections, representing various network protocols like NetBIOS and LDAP on a dark background with vibrant colors."
coverCaption: "Master Enumeration for the CEH v13 Exam"
---

#### [Click Here to Return To the Certified Ethical Hacker (CEH v13) Course Page](/ceh-start/)

**Enumeration** extracts detailed information from discovered services in the **EC-Council CEH v13** course. This module covers how you pull usernames, shares, groups, and configuration data from exposed protocols. *Enumeration is active and noisy, so it only belongs inside an authorized engagement.*

Scanning tells you a port is open. Enumeration connects to that service and asks it for specifics like account names, share lists, and software versions. These details fuel the attack phase.

## Common Enumeration Targets

Each protocol leaks different data when it is misconfigured.

| Protocol | Port | What you extract |
|----------|------|------------------|
| **NetBIOS** | 137-139 | Computer names, shares |
| **SMB** | 445 | Shares, users, groups |
| **SNMP** | 161 | Device config, interfaces, routes |
| **LDAP** | 389 | Directory users and structure |
| **DNS** | 53 | Records, zone data |
| **SMTP** | 25 | Valid email accounts |

## SMB and NetBIOS Enumeration

Windows file sharing exposes a wealth of data when null sessions are allowed.

```bash
# Enumerate shares, users, and groups over SMB
enum4linux -a 192.168.1.10
nbtscan 192.168.1.0/24
```

A **null session** connects without credentials and lists users and shares on older or misconfigured systems. You map shares, then check which allow anonymous read or write.

## SNMP and LDAP Enumeration

**SNMP** with a default community string like `public` reveals routing tables, running processes, and interface details.

```bash
# Walk the SNMP tree with the public community string
snmpwalk -v2c -c public 192.168.1.1
```

**LDAP** enumeration queries the directory for users, groups, and the organizational structure, which maps targets for password attacks.

## DNS Zone Transfers

A misconfigured name server allows a **zone transfer** that dumps every record in a domain.

```bash
# Attempt a zone transfer against a name server
dig axfr example.com @ns1.example.com
```

A successful transfer hands you internal hostnames and IP addresses. *Most servers block this, but one that allows it gives you the whole map.*

## Next Steps

Turn this detail into a list of weaknesses in [Vulnerability Analysis](/ceh/vulnerability-analysis/). Revisit port discovery in [Scanning Networks](/ceh/scanning-networks/). Return to the [Certified Ethical Hacker (CEH v13) Course](/ceh-start/).
