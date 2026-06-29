---
title: "Cisco CCNA (200-301): IP Services"
date: 2025-01-01
toc: true
draft: false
description: "Master IP services for the Cisco CCNA 200-301 exam. Learn NAT, NTP, DHCP and DNS roles, SNMP, syslog, QoS per-hop behavior, SSH, and TFTP/FTP."
genre: ["Cisco CCNA Course", "Networking", "IP Services", "NAT", "DHCP", "QoS", "Cisco Certification", "Network Operations", "Network Management", "IT Networking"]
tags: ["Cisco CCNA", "200-301", "IP services", "NAT", "PAT", "NTP", "DHCP", "DNS", "SNMP", "syslog", "QoS", "per-hop behavior", "SSH", "TFTP", "FTP", "remote access"]
cover: "/img/cover/cisco-ccna-ip-services-network-management.webp"
coverAlt: "A digital illustration of a futuristic control panel with glowing buttons, set against a dark cityscape filled with servers and routers, symbolizing network management and IP services."
coverCaption: "Master IP Services for the CCNA 200-301 Exam"
---

#### [Click Here to Return To the Cisco CCNA Course Page](/ccna-start/)

**IP Services** is **10%** of the **Cisco CCNA (200-301)** exam. This module covers the services that make a network usable and manageable. *These features show up constantly in real networks even though the domain weight is small.*

These services translate addresses, keep time, hand out configuration, and report what the network is doing. You configure and verify each one.

## Network Address Translation

**NAT** maps private addresses to public ones so internal hosts reach the internet. **Static NAT** maps one inside address to one outside address, a **pool** maps many to many, and **PAT** (overload) maps many private hosts to one public address with port numbers.

```text
! Inside source NAT with a pool
Router(config)# ip nat pool POOL1 203.0.113.10 203.0.113.20 netmask 255.255.255.0
Router(config)# ip nat inside source list 1 pool POOL1
Router(config)# interface g0/0
Router(config-if)# ip nat inside
```

Verify translations with `show ip nat translations`.

## DHCP, DNS, and NTP

| Service | Role |
|---------|------|
| **DHCP** | Assigns IP, mask, gateway, and DNS to clients |
| **DNS** | Resolves names to IP addresses |
| **NTP** | Synchronizes clocks across devices |

A **DHCP relay** (`ip helper-address`) forwards requests when the server sits on another subnet. Accurate **NTP** time matters, because logs and certificates depend on it.

```text
! Point an interface to a DHCP server on another subnet
Router(config-if)# ip helper-address 10.10.10.5

! Sync to an NTP server
Router(config)# ntp server 10.10.10.6
```

## Management and Logging

**SNMP** polls device health and sends traps for events. **Syslog** records messages by **facility** and **severity level**.

| Level | Keyword |
|-------|---------|
| 0 | Emergency |
| 3 | Error |
| 6 | Informational |
| 7 | Debugging |

Lower numbers are more severe, so a level 0 message needs immediate attention.

## Secure Remote Access

You manage devices remotely with **SSH**, which encrypts the session. Avoid Telnet, since it sends credentials in clear text. **TFTP** and **FTP** move configuration files and IOS images, with FTP supporting authentication.

```text
! Enable SSH access
Router(config)# hostname R1
R1(config)# ip domain-name example.com
R1(config)# crypto key generate rsa modulus 2048
R1(config)# line vty 0 4
R1(config-line)# transport input ssh
```

## Quality of Service

**Per-hop behavior (PHB)** decides how each device treats a packet. The steps are **classification**, **marking**, **queuing**, congestion management, **policing**, and **shaping**. Policing drops or remarks traffic over a limit, while shaping buffers it to smooth bursts. This keeps voice and video usable when links fill.

## Next Steps

Secure these services in [Security Fundamentals](/ccna/security-fundamentals-acls-vpn-layer2-security/) and automate them in [Automation and Programmability](/ccna/automation-programmability-apis-ansible-sdwan/). Review routing in [IP Connectivity](/ccna/ip-connectivity-routing-ospf-static-routes/) and return to the [Cisco CCNA Course](/ccna-start/).
