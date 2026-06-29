---
title: "CEH v13: Scanning Networks"
date: 2025-01-01
toc: true
draft: false
description: "Master scanning networks for the EC-Council Certified Ethical Hacker (CEH v13) exam. Learn host discovery, Nmap port scanning, TCP scan types, OS fingerprinting, and banner grabbing."
genre: ["EC-Council CEH Course", "Ethical Hacking", "Penetration Testing", "Offensive Security", "Cybersecurity", "Network Security", "Security Testing", "Hacking Techniques", "CEH Certification", "Information Security"]
tags: ["CEH", "CEH v13", "ethical hacking", "EC-Council", "penetration testing", "scanning networks", "offensive security", "cybersecurity", "hacking", "security testing"]
cover: "/img/cover/ceh-v13-network-scanning-host-discovery-port-scanning.webp"
coverAlt: "An illustration of a digital network showing nodes and connections, with glowing lines representing active scanning processes, set against a dark background."
coverCaption: "Master Scanning Networks for the CEH v13 Exam"
---

#### [Click Here to Return To the Certified Ethical Hacker (CEH v13) Course Page](/ceh-start/)

**Scanning Networks** moves from passive recon to active discovery in the **EC-Council CEH v13** course. This module covers how you find live hosts, open ports, running services, and operating systems. *Active scanning touches the target directly, so confirm your scope before you run it.*

Scanning answers three questions: what hosts are alive, what ports are open, and what software listens behind them. The answers shape your attack plan.

## Host Discovery

Before port scanning, you find which hosts respond.

```bash
# Ping sweep a subnet without port scanning
nmap -sn 192.168.1.0/24
```

A **ping sweep** uses ICMP, ARP, or TCP probes to map live hosts. On a local network ARP discovery is the most reliable.

## TCP Scan Types

Different scans trade stealth for accuracy. They rely on how TCP responds to crafted flags.

| Scan | Nmap flag | How it works |
|------|-----------|--------------|
| **TCP Connect** | `-sT` | Full three-way handshake, loud |
| **SYN (half-open)** | `-sS` | Sends SYN, never finishes, stealthier |
| **FIN** | `-sF` | Sends FIN to slip past simple filters |
| **XMAS** | `-sX` | Sets FIN, PSH, URG flags |
| **NULL** | `-sN` | Sends no flags |
| **UDP** | `-sU` | Probes UDP services like DNS and SNMP |

A closed TCP port replies with RST. An open port ignores FIN, XMAS, and NULL probes, which lets you infer its state.

## Service and OS Detection

You identify what runs behind each open port.

```bash
# Version detection, OS fingerprint, default scripts
nmap -sV -O -sC 192.168.1.10
```

**Banner grabbing** reads the service banner to learn software and version. **OS fingerprinting** compares TCP/IP stack behavior to a database to guess the operating system. Learn the full tool in depth with the on-site [Nmap guide and reference](/nmap/).

## Scan Tooling and Output

| Tool | Use |
|------|-----|
| **Nmap** | The core scanner for ports, services, and scripts |
| **Zenmap** | Nmap with a graphical interface |
| **Hping3** | Crafts custom packets for firewall testing |
| **Masscan** | Scans large ranges at high speed |

Save results with `-oA` so you feed them into the next phase. *Slow your timing with `-T2` when stealth matters more than speed.*

## Next Steps

Pull detailed data from discovered services in [Enumeration](/ceh/enumeration/). Revisit information gathering in [Footprinting and Reconnaissance](/ceh/footprinting-and-reconnaissance/). Return to the [Certified Ethical Hacker (CEH v13) Course](/ceh-start/).
