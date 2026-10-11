---
title: "Cisco CCNA 200-301 v1.1 Course and Lab Guide"
date: 2025-01-01
toc: true
draft: false
description: "Build a six-stage Packet Tracer lab for CCNA 200-301 v1.1. Verify subnetting, VLANs, OSPF, NAT, access controls, and automation evidence."
lastmod: 2026-10-10
genre: ["Cisco CCNA Course", "Networking Certification", "Network Fundamentals", "Routing and Switching", "Network Security", "Cisco Certification", "IP Connectivity", "Network Automation", "Wireless Networking", "IT Networking"]
tags: ["Cisco CCNA", "200-301", "networking", "routing", "switching", "OSPF", "VLANs", "spanning tree", "subnetting", "IPv4", "IPv6", "NAT", "DHCP", "DNS", "ACLs", "network security", "wireless", "automation", "Ansible", "SDN", "Cisco certification"]
cover: "/img/cover/cisco-ccna-200-301-exam-preparation-illustration.webp"
coverAlt: "An illustration of a modern training environment for Cisco CCNA exam preparation, featuring a laptop with a network diagram, routers, and switches, all set against a dark background with vibrant colors."
coverCaption: "Build and verify a CCNA 200-301 practice network"
---
Cisco lists CCNA 200-301 v1.1 through February 2, 2027, with v2.0 starting February 3, 2027. This course follows the six v1.1 domains. Check the [official v1.1 topics](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf) and [current CCNA page](https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccna.html) before booking. The lessons explain the topics and build one isolated simulated network. Lab results show specific skills; they do not guarantee exam or workplace readiness.

You need basic IP addressing and command-line familiarity. If subnet masks, gateways, or a switch port are new terms, work through [Network+ fundamentals](/network-plus-start/) first. Set aside six sessions of 60 to 90 minutes plus a final fault exercise. Work only in a simulator or equipment you own and have permission to configure.

## Set up Cisco Packet Tracer

1. Enroll in Cisco Networking Academy's free [Getting Started with Cisco Packet Tracer](https://www.netacad.com/courses/getting-started-cisco-packet-tracer/1000) course. Download Packet Tracer through that authorized route. Do not download device images or `.pkt` projects from unofficial mirrors.
2. Start a blank project. In the device palette, place two routers with two Gigabit Ethernet ports, two switches with Fast Ethernet access ports and Gigabit uplinks, two PCs, and one server. The common Packet Tracer router and switch models work for the basic lab. Interface names differ by model, so replace the sample names with the actual names shown in your project.
3. Use the connection tool to wire the ports in the table. Save `ccna-base.pkt`. Keep a separate copy after every module so you can reverse a broken configuration.

| Cable | End A | End B |
|-------|-------|-------|
| 1 | PC-A FastEthernet0 | S1 FastEthernet0/1 |
| 2 | PC-B FastEthernet0 | S2 FastEthernet0/1 |
| 3 | S1 GigabitEthernet0/2 | S2 GigabitEthernet0/1 |
| 4 | S1 GigabitEthernet0/1 | R1 GigabitEthernet0/0 |
| 5 | R1 GigabitEthernet0/1 | R2 GigabitEthernet0/0 |
| 6 | R2 GigabitEthernet0/1 | SRV1 FastEthernet0 |

Use this fictional address plan. `192.0.2.0/24`, `198.51.100.0/24`, and `2001:db8::/32` are documentation ranges, not live internet targets.

| Segment | Network | Gateway or node |
|---------|---------|-----------------|
| VLAN 10, PC-A | `10.10.10.0/24` | R1 `.1`, PC-A `.10` |
| VLAN 20, PC-B | `10.10.20.0/24` | R1 `.1`, PC-B `.10` |
| R1 to R2 | `192.0.2.0/30` | R1 `.1`, R2 `.2` |
| R2 to SRV1 | `198.51.100.0/24` | R2 `.1`, SRV1 `.10` |

Do not configure every feature at once. The Network Access lesson creates VLANs and trunks. IP Connectivity creates R1 subinterfaces, the R1 to R2 link, routes, and OSPF. IP Services adds controlled NAT and services. Keep a screenshot or text record of intended state, command output, a failure injection, the repair, and the final state at every stage.

| Order | Domain | Weight | Checkpoint |
|-------|--------|--------|------------|
| 1 | [Network Fundamentals](/ccna/network-fundamentals-osi-tcp-ip-switching/) | 20% | Address worksheet and frame-path prediction |
| 2 | [Network Access](/ccna/network-access-vlans-spanning-tree-wireless/) | 20% | VLAN and trunk verification |
| 3 | [IP Connectivity](/ccna/ip-connectivity-routing-ospf-static-routes/) | 25% | Route choice and OSPF neighbor evidence |
| 4 | [IP Services](/ccna/ip-services-nat-dhcp-qos-snmp/) | 10% | NAT, DHCP, NTP, and logging record |
| 5 | [Security Fundamentals](/ccna/security-fundamentals-acls-vpn-layer2-security/) | 15% | ACL allow and deny tests |
| 6 | [Automation and Programmability](/ccna/automation-programmability-apis-ansible-sdwan/) | 10% | Read-only JSON and reviewed change plan |

Packet Tracer models a subset of production features. When a device lacks a feature, study its syntax and use a supplied output example. Label the task `simulated` or `not run`. Never claim a simulator proves live wireless controller, VPN, API, or automation behavior.

## Final practical assessment

Save a clean copy. Ask another person to insert one fault, or insert the following yourself and hide the answer until diagnosis: change S2's trunk native VLAN, shut R1's link to R2, or place a deny ACL before an intended permit. For each fault, record the baseline, symptom, affected path, two candidate causes, the command or packet test, the observed result, one correction, and the restored result. Then restore the clean project.

Pass when PC-A reaches its default gateway, PC-B reaches its default gateway, an allowed PC reaches SRV1, a denied flow fails for the intended ACL reason, and the evidence points to the actual fault rather than a guess. Explain what your simulator did not verify. Review the [Cisco CCNA practice test](/ccna-practice-test/) and the [official exam topics](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf) for theory gaps.

For an exam date on or after February 3, 2027, use Cisco's [v2.0 topics](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301_CCNA_v2.0_Exam_Topics_PDF.pdf) and rebuild your study checklist for that blueprint. Browse the [course index](/courses-and-playbooks/) for related paths.
