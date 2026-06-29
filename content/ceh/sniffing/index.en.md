---
title: "CEH v13: Sniffing"
date: 2025-01-01
toc: true
draft: false
description: "Master sniffing for the EC-Council Certified Ethical Hacker (CEH v13) exam. Learn passive and active sniffing, ARP poisoning, MAC flooding, Wireshark, tcpdump, and sniffing countermeasures."
genre: ["EC-Council CEH Course", "Ethical Hacking", "Penetration Testing", "Offensive Security", "Cybersecurity", "Network Security", "Security Testing", "Hacking Techniques", "CEH Certification", "Information Security"]
tags: ["CEH", "CEH v13", "ethical hacking", "EC-Council", "penetration testing", "sniffing", "offensive security", "cybersecurity", "hacking", "security testing"]
cover: "/img/cover/ceh-v13-sniffing-network-traffic-analysis.webp"
coverAlt: "A digital artwork of a modern workspace with a laptop displaying vibrant network traffic analysis, surrounded by glowing lines representing data flow and network connections."
coverCaption: "Master Sniffing for the CEH v13 Exam"
---

#### [Click Here to Return To the Certified Ethical Hacker (CEH v13) Course Page](/ceh-start/)

**Sniffing** captures and analyzes network traffic in the **EC-Council CEH v13** course. This module covers passive and active sniffing, switch-based attacks, and the tools that read packets off the wire. *Capture traffic only on networks you are authorized to test.*

A sniffer reads packets as they cross the network. On unencrypted protocols this exposes credentials, session tokens, and sensitive data in plaintext.

## Passive vs. Active Sniffing

The network design decides which approach works.

| Type | Where it works | Method |
|------|----------------|--------|
| **Passive** | Hubs, mirrored ports | Listens without altering traffic |
| **Active** | Switched networks | Forces traffic to your host |

Switches send traffic only to the right port, so an attacker uses active techniques to redirect it.

## Active Sniffing Attacks

You manipulate Layer 2 to intercept traffic.

- **ARP poisoning** sends forged ARP replies so victims send traffic through you. This is a man-in-the-middle position.
- **MAC flooding** overloads the switch CAM table so it fails open and broadcasts like a hub.
- **DHCP starvation** exhausts the DHCP pool, then a rogue server hands out malicious settings.

```bash
# Capture traffic on an interface and filter for HTTP
sudo tcpdump -i eth0 -A 'tcp port 80'
```

## Analysis Tools

| Tool | Use |
|------|-----|
| **Wireshark** | Deep graphical packet analysis |
| **tcpdump** | Command-line capture and filtering |
| **Ettercap** | Man-in-the-middle and ARP poisoning |
| **dsniff** | Extracts credentials from traffic |

You apply display filters in Wireshark like `http.request` or `tcp.port == 443` to focus on relevant packets.

## Countermeasures

You defend against sniffing with encryption and switch hardening.

- **Encrypt** traffic with TLS, SSH, and VPNs so captured data stays unreadable.
- **Dynamic ARP Inspection (DAI)** blocks forged ARP replies.
- **Port security** limits MAC addresses per port to stop flooding.

*Encryption is the strongest defense, because a sniffer that captures ciphertext gains nothing.*

## Next Steps

Move from technical capture to human attacks in [Social Engineering](/ceh/social-engineering/). Revisit malicious code in [Malware Threats](/ceh/malware-threats/). Return to the [Certified Ethical Hacker (CEH v13) Course](/ceh-start/).
