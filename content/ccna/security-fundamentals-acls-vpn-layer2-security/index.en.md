---
title: "Cisco CCNA (200-301): Security Fundamentals"
date: 2025-01-01
toc: true
draft: false
description: "Master security fundamentals for the Cisco CCNA 200-301 exam. Learn security concepts, device access control, VPNs, access control lists, Layer 2 security, AAA, and wireless security."
genre: ["Cisco CCNA Course", "Networking", "Network Security", "Access Control Lists", "VPN", "Layer 2 Security", "Cisco Certification", "Wireless Security", "AAA", "IT Networking"]
tags: ["Cisco CCNA", "200-301", "security fundamentals", "ACLs", "VPN", "IPsec", "DHCP snooping", "dynamic ARP inspection", "port security", "AAA", "WPA2", "WPA3", "device access control", "MFA"]
cover: "/img/cover/cisco-ccna-security-fundamentals-network-illustration.webp"
coverAlt: "An illustration of a secure network environment featuring routers, switches, and visual data flow lines. The background is dark navy with vibrant blue, green, and purple accents representing cybersecurity elements."
coverCaption: "Master Security Fundamentals for the CCNA 200-301 Exam"
---

#### [Click Here to Return To the Cisco CCNA Course Page](/ccna-start/)

**Security Fundamentals** is **15%** of the **Cisco CCNA (200-301)** exam. This module covers how you protect devices, traffic, and access. *Security questions blend with configuration tasks, so know both the theory and the commands.*

This domain mixes concepts with hands-on configuration. You define the threats, then lock down devices, filter traffic, and secure both wired and wireless access.

## Core Security Concepts

You separate four related terms.

| Term | Meaning |
|------|---------|
| **Threat** | A potential cause of harm |
| **Vulnerability** | A weakness that can be exploited |
| **Exploit** | The method used against a vulnerability |
| **Mitigation** | A control that reduces the risk |

**Security program elements** include user awareness, training, and physical access control. People are the most common entry point, so training matters as much as technology.

## Device Access Control

You protect device access with strong local credentials and a clear **password policy**. Cover management, complexity, and alternatives such as **MFA**, certificates, and biometrics.

```text
! Secure privileged access and console
Router(config)# enable secret StrongSecret123
Router(config)# username admin secret AdminPass456
Router(config)# service password-encryption
```

To build credentials that resist cracking, read [how to create strong passwords](/articles/how-to-create-strong-passwords/).

## AAA and VPNs

**AAA** separates three functions:

- **Authentication** confirms who you are.
- **Authorization** decides what you can do.
- **Accounting** records what you did.

A **RADIUS** or **TACACS+** server centralizes AAA across many devices. **VPNs** protect traffic across untrusted networks. **IPsec** secures both remote access and site-to-site tunnels with encryption and integrity.

## Access Control Lists

**ACLs** filter traffic by source, destination, protocol, and port. Standard ACLs match source only, while extended ACLs match much more.

```text
! Extended ACL allowing web traffic, denying the rest
Router(config)# access-list 110 permit tcp any host 10.1.1.10 eq 80
Router(config)# interface g0/0
Router(config-if)# ip access-group 110 in
```

Order matters, because the router reads top to bottom and stops at the first match. An implicit `deny any` sits at the end of every ACL.

## Layer 2 Security

Switches need their own protections against local attacks.

| Feature | Protects against |
|---------|------------------|
| **Port security** | MAC flooding and rogue devices |
| **DHCP snooping** | Rogue DHCP servers |
| **Dynamic ARP inspection** | ARP poisoning |

```text
! Limit a port to one learned MAC
Switch(config-if)# switchport port-security
Switch(config-if)# switchport port-security maximum 1
Switch(config-if)# switchport port-security violation shutdown
```

## Wireless Security

Wireless protocols improved over time. **WPA** is legacy, **WPA2** uses AES with CCMP, and **WPA3** adds stronger key exchange with SAE. In the WLC GUI you create a WLAN and apply **WPA2 PSK** for a pre-shared key network.

## Next Steps

Finish the blueprint with [Automation and Programmability](/ccna/automation-programmability-apis-ansible-sdwan/), built on the services from [IP Services](/ccna/ip-services-nat-dhcp-qos-snmp/). Strengthen your fundamentals with the [CompTIA Security+ Course](/security-plus-start/) and return to the [Cisco CCNA Course](/ccna-start/).
