---
title: "Cisco CCNA (200-301): IP Services"
date: 2025-01-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Configure and verify CCNA v1.1 NAT and DHCP in a two-router lab, then assess time synchronization, logging, SSH, and QoS with bounded evidence."
genre: ["Cisco CCNA Course", "Networking", "IP Services", "NAT", "DHCP", "QoS", "Cisco Certification", "Network Operations", "Network Management", "IT Networking"]
tags: ["Cisco CCNA", "200-301", "IP services", "NAT", "PAT", "NTP", "DHCP", "DNS", "SNMP", "syslog", "QoS", "per-hop behavior", "SSH", "TFTP", "FTP", "remote access"]
cover: "/img/cover/cisco-ccna-ip-services-network-management.webp"
coverAlt: "A digital illustration of a futuristic control panel with glowing buttons, set against a dark cityscape filled with servers and routers, symbolizing network management and IP services."
coverCaption: "Master IP Services for the CCNA 200-301 Exam"
---

[Click Here to Return To the Cisco CCNA Course Page](/ccna-start/)

**IP Services** is **10%** of the **Cisco CCNA (200-301)** exam. This module covers the services that make a network usable and manageable. *These features show up constantly in real networks even though the domain weight is small.*

These services translate addresses, keep time, hand out configuration, and report what the network is doing. You configure and verify each one.

## Network Address Translation

**NAT** maps private addresses to public ones so internal hosts reach the internet. **Static NAT** maps one inside address to one outside address, a **pool** maps many to many, and **PAT** (overload) maps many private hosts to one public address with port numbers.

```text
! Lab 4 supplies the full PAT configuration and verification.
R1# show ip nat translations
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
! Disposable lab only. Replace the placeholder with a unique secret.
R1(config)# hostname R1
R1(config)# ip domain-name example.test
R1(config)# username labadmin secret <unique-lab-secret>
R1(config)# crypto key generate rsa modulus 2048
R1(config)# ip ssh version 2
R1(config)# line vty 0 4
R1(config-line)# login local
R1(config-line)# transport input ssh
```

## Quality of Service

**Per-hop behavior (PHB)** decides how each device treats a packet. The steps are **classification**, **marking**, **queuing**, congestion management, **policing**, and **shaping**. Policing drops or remarks traffic over a limit, while shaping buffers it to smooth bursts. This keeps voice and video usable when links fill.

## Lab 4: Translate and Assign Addresses

Continue the [course topology](/ccna-start/) with OSPF working. Save `ccna-routing-clean.pkt` before adding services. On R1, `g0/0.10` and `g0/0.20` are inside interfaces, and `g0/1` faces the R2 outside test network. A standard ACL selects which sources receive translation. Cisco's [NAT configuration example](https://www.cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/13772-12.html) shows the same inside, outside, selection, and overload parts.

```text
R1(config)# access-list 1 permit 10.10.0.0 0.0.255.255
R1(config)# interface g0/0.10
R1(config-subif)# ip nat inside
R1(config)# interface g0/0.20
R1(config-subif)# ip nat inside
R1(config)# interface g0/1
R1(config-if)# ip nat outside
R1(config)# ip nat inside source list 1 interface g0/1 overload
```

From PC-A, ping SRV1 at `198.51.100.10`, then inspect `show ip nat translations` and `show ip nat statistics` on R1. The inside local source should be `10.10.10.10`. The inside global source should use R1's `192.0.2.1` outside interface. A simulation may expire ICMP entries quickly; generate fresh traffic before calling the table empty. Do not send this test to the real internet. Compare the result with the pre-NAT routing checkpoint.

Next, reserve `.1` through `.20` and give VLAN 10 a DHCP pool. In Packet Tracer, switch PC-A from static to DHCP after recording its first address. It should receive a free address from the VLAN 10 pool and keep gateway `.1`.

```text
R1(config)# ip dhcp excluded-address 10.10.10.1 10.10.10.20
R1(config)# ip dhcp pool VLAN10
R1(dhcp-config)# network 10.10.10.0 255.255.255.0
R1(dhcp-config)# default-router 10.10.10.1
R1(dhcp-config)# dns-server 198.51.100.10
R1# show ip dhcp binding
```

A missing lease suggests the PC did not switch to DHCP, the VLAN or trunk is wrong, or the pool and gateway do not match. Do not blame DNS for a missing lease. Add a separate VLAN 20 pool only after this first case works. Record the lease, mask, gateway, and renewal result. Restore the intended static address before the next lesson, or update its worksheet with the assigned address.

For an NTP and syslog review, label SRV1 as a fictional management server. If your Packet Tracer server offers those services, enable them in its Services tab, point R1 to `198.51.100.10` with `ntp server` and `logging`, and inspect `show ntp associations` and the server's log. If the simulator omits a feature, mark `not run` and describe the evidence a real device would need. Use SNMPv3 where supported in a real authorized environment. Do not expose a community string or management credential in this course record.

For QoS, consider a 10 Mb/s link receiving 12 Mb/s of traffic. Policing at 10 Mb/s drops or remarks excess at the enforcement point. Shaping at 10 Mb/s buffers bursts and adds delay within queue limits. Record the tradeoff and which measurement, such as drops, queue depth, or latency, would test the policy. This is a reasoning task, not a Packet Tracer performance measurement.

Your checkpoint is a complete NAT configuration, translated-source observation, DHCP lease, one injected failure and repair, and a services evidence table with `observed`, `simulated`, or `not run`. Pass when you can explain the source translation and verify the new lease and gateway without treating a successful command as proof of end-to-end service.

## Next Steps

Secure these services in [Security Fundamentals](/ccna/security-fundamentals-acls-vpn-layer2-security/) and automate them in [Automation and Programmability](/ccna/automation-programmability-apis-ansible-sdwan/). Review routing in [IP Connectivity](/ccna/ip-connectivity-routing-ospf-static-routes/) and return to the [Cisco CCNA Course](/ccna-start/).
