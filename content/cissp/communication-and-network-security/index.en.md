---
title: "ISC2 CISSP: Communication and Network Security"
date: 2025-01-01
toc: true
draft: false
description: "Master Communication and Network Security for the ISC2 CISSP exam. Learn secure network architecture, segmentation, wireless and cellular networks, modern network concepts, and secure channels."
genre: ["ISC2 CISSP Course", "Network Security", "Secure Architecture", "Segmentation", "Wireless Security", "ISC2 Certification", "Information Security", "Zero Trust", "SDN", "Cybersecurity"]
tags: ["ISC2 CISSP", "CISSP", "network security", "OSI model", "TCP/IP", "IPSec", "TLS", "segmentation", "VLAN", "microsegmentation", "wireless", "5G", "SDN", "VPC", "CDN", "secure channels"]
cover: "/img/cover/isc2-cissp-communication-network-security-architecture.webp"
coverAlt: "A digital illustration of a secure network architecture, featuring layered OSI and TCP/IP models, wireless networks like Wi-Fi and 5G, and components like NAC, all against a dark background with vibrant accents."
coverCaption: "Master Communication and Network Security for the CISSP Exam"
---

#### [Click Here to Return To the ISC2 CISSP Course Page](/cissp-start/)

**Communication and Network Security** is **13%** of the **ISC2 CISSP** exam. This module covers how you design networks that resist attack and move data through channels nobody else can read. *Apply security principles to networking rather than memorizing vendor commands, since the CISSP tests concepts, not configuration syntax.*

Networks carry every byte your organization values. A flat, trusting network lets one compromised host reach everything. A segmented, encrypted, monitored network contains the damage. This domain teaches you to design the second kind.

## The OSI and TCP/IP Models

You must know the **OSI model** layers cold because the exam describes attacks and controls by layer.

| Layer | Name | Examples | Threats |
|-------|------|----------|---------|
| 7 | Application | HTTP, DNS, SMTP | Injection, malware |
| 6 | Presentation | TLS, encoding, encryption | Weak ciphers |
| 5 | Session | RPC, session setup | Session hijacking |
| 4 | Transport | TCP, UDP | SYN floods, port scans |
| 3 | Network | IP, ICMP, routing | Spoofing, routing attacks |
| 2 | Data Link | Ethernet, MAC, ARP | ARP poisoning, MAC flooding |
| 1 | Physical | Cables, radio, hubs | Wiretapping, jamming |

The **TCP/IP model** collapses these into four layers: Application, Transport, Internet, and Link. A common memory aid for OSI top to bottom is "All People Seem To Need Data Processing."

**IPv4** uses 32-bit addresses and is nearly exhausted. **IPv6** uses 128-bit addresses, builds in IPSec support, and removes the need for NAT. Both run on the same network layer.

## Secure Protocols

You replace clear-text protocols with encrypted equivalents at every layer.

| Insecure | Secure replacement | Protects |
|----------|--------------------|----------|
| HTTP | HTTPS (TLS) | Web traffic |
| Telnet | SSH | Remote shell |
| FTP | SFTP or FTPS | File transfer |
| SNMPv1/v2 | SNMPv3 | Network management |

- **IPSec** secures IP traffic with two modes. *Transport mode* encrypts the payload only. *Tunnel mode* encrypts the whole packet and is used for site-to-site VPNs. It uses **AH** for integrity and **ESP** for confidentiality and integrity.
- **SSH** gives an encrypted remote shell and tunnels other protocols.
- **SSL/TLS** secures application traffic. *SSL is deprecated, so use TLS 1.2 or 1.3.*

```bash
# Test which TLS versions and ciphers a server accepts
nmap --script ssl-enum-ciphers -p 443 example.com

# Open an encrypted shell to a server with key-based authentication
ssh -i ~/.ssh/id_ed25519 admin@server.example.com
```

## Network Segmentation

**Segmentation** divides a network so a breach in one zone does not spread. It is one of the strongest controls you can apply.

- **Physical segmentation** uses separate hardware for separate networks. It is the strongest and most expensive option.
- **Logical segmentation** uses **VLANs** to separate traffic on shared hardware and **VPNs** to extend a trusted network over an untrusted one.
- **Micro-segmentation** isolates individual workloads with their own policies. It is the foundation of **zero trust** networking, where no host trusts another by default.
- A **DMZ** (screened subnet) holds public-facing servers between two firewalls so the internet never reaches the internal network directly.

You connect segmentation back to [Security Architecture and Engineering](/cissp/security-architecture-and-engineering/), where defense in depth and zero trust are defined.

## Wireless and Cellular Networks

Wireless removes the physical boundary, so you secure the air itself.

| Technology | Range | Security notes |
|-----------|-------|----------------|
| **Wi-Fi** | Building | Use WPA3, disable WPS, separate guest SSIDs |
| **Bluetooth** | Personal | Disable discovery, beware bluejacking and bluesnarfing |
| **Zigbee** | Home/IoT | Low-power mesh, weak default keys on many devices |
| **Satellite** | Global | High latency, encrypt the link |
| **4G/5G** | Wide area | 5G adds stronger encryption and network slicing |

**WPA3** is the current Wi-Fi standard and fixes the offline-dictionary weakness of WPA2 with **SAE**. Always isolate IoT and guest devices on separate networks so a cheap smart bulb cannot reach your servers.

## Modern Network Concepts

- **Software-Defined Networking (SDN)** separates the control plane from the data plane, so you manage the network through software and apply policy centrally.
- **Virtual Private Cloud (VPC)** is an isolated network inside a cloud provider where you control subnets, routing, and security groups.
- **Content Delivery Network (CDN)** caches content near users to cut latency and absorb DDoS traffic.

You judge network performance with four metrics:

| Metric | Meaning |
|--------|---------|
| **Bandwidth** | Maximum data rate of a link |
| **Latency** | Delay for data to travel end to end |
| **Jitter** | Variation in latency, harmful to voice and video |
| **Throughput** | Actual data delivered, always at or below bandwidth |

## Network Components and Secure Channels

You secure the devices that move traffic.

- **Network Access Control (NAC)** checks a device's identity and health before it joins the network and quarantines noncompliant devices.
- **Endpoint security** protects the hosts at the edge with EDR, host firewalls, and patching.
- **Transmission media** matters: fiber resists tapping and electromagnetic interference better than copper.

You protect communication channels by content type:

- **Voice** over IP needs encryption such as SRTP and protection against toll fraud.
- **Video and collaboration** tools need encryption, access controls, and meeting-link hygiene.
- **Remote access** uses VPNs, MFA, and posture checks so a home device cannot become an entry point.

## Next Steps

With the network secured, continue to [Identity and Access Management](/cissp/identity-and-access-management/) to control who reaches these systems, then [Security Assessment and Testing](/cissp/security-assessment-and-testing/) to verify the controls hold. Compare real-world gear in [Fortinet vs Cisco network security](/articles/fortinet-vs-cisco-network-security-comparison/) and return to the [ISC2 CISSP Course](/cissp-start/).
