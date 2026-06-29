---
title: "Cisco CCNA Course: Complete Study Guide for the 200-301 Exam"
date: 2025-01-01
toc: true
draft: false
description: "A comprehensive Cisco CCNA (200-301) study course covering network fundamentals, network access, IP connectivity, IP services, security fundamentals, and automation and programmability."
genre: ["Cisco CCNA Course", "Networking Certification", "Network Fundamentals", "Routing and Switching", "Network Security", "Cisco Certification", "IP Connectivity", "Network Automation", "Wireless Networking", "IT Networking"]
tags: ["Cisco CCNA", "200-301", "networking", "routing", "switching", "OSPF", "VLANs", "spanning tree", "subnetting", "IPv4", "IPv6", "NAT", "DHCP", "DNS", "ACLs", "network security", "wireless", "automation", "Ansible", "SDN", "Cisco certification"]
cover: "/img/cover/cisco-ccna-200-301-exam-preparation-illustration.webp"
coverAlt: "An illustration of a modern training environment for Cisco CCNA exam preparation, featuring a laptop with a network diagram, routers, and switches, all set against a dark background with vibrant colors."
coverCaption: "Master the Cisco CCNA and Build Your Networking Career"
---

The **Cisco CCNA (200-301)** is the industry-standard associate-level networking certification. It validates your ability to install, configure, and troubleshoot networks across routing, switching, IP services, security, and automation. This course covers every exam domain so you build hands-on skills and pass the exam with confidence. *The CCNA exam runs 120 minutes and uses performance-based, multiple choice, and drag-and-drop questions.*

| Domain | Title | Exam Weight |
|--------|-------|-------------|
| 1.0 | Network Fundamentals | 20% |
| 2.0 | Network Access | 20% |
| 3.0 | IP Connectivity | 25% |
| 4.0 | IP Services | 10% |
| 5.0 | Security Fundamentals | 15% |
| 6.0 | Automation and Programmability | 10% |

## Resources

- [Tips for Passing IT Certification Exams](/articles/tips-and-tricks-for-passing-comptia-exams/)
- [Cisco CCNA Practice Test](/ccna-practice-test/)
- [Official Cisco 200-301 Exam Topics](https://learningnetwork.cisco.com/s/ccna-exam-topics)
- [Jeremy's IT Lab Free CCNA Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ)
- [Additional Learning Resources](/recommendations/learning_resources/)
- [Courses and Playbooks](/courses-and-playbooks/)

-----

## Domain 1: Network Fundamentals (20%)

### [Network Fundamentals](/ccna/network-fundamentals-osi-tcp-ip-switching/)

- Explain the role and function of **network components**, including routers, Layer 2 and Layer 3 switches, next-generation firewalls, IPS, access points, controllers, endpoints, servers, and PoE
- Describe **network topology architectures**, including two-tier, three-tier, spine-leaf, WAN, SOHO, and on-premises vs. cloud
- Compare **physical interface and cabling types**, including single-mode fiber, multimode fiber, and copper
- Identify **interface and cable issues**, including collisions, errors, duplex mismatch, and speed mismatch
- Compare **TCP to UDP** and their use cases
- Configure and verify **IPv4 addressing and subnetting**, and describe the need for private IPv4 addressing
- Configure and verify **IPv6 addressing** and describe IPv6 address types, including global unicast, unique local, link local, anycast, and multicast
- Describe **wireless principles**, including nonoverlapping Wi-Fi channels, SSID, RF, and encryption
- Explain **virtualization fundamentals**, including server virtualization, containers, and VRFs
- Describe **switching concepts**, including MAC learning and aging, frame switching, frame flooding, and the MAC address table

-----

## Domain 2: Network Access (20%)

### [Network Access](/ccna/network-access-vlans-spanning-tree-wireless/)

- Configure and verify **VLANs** spanning multiple switches, including access ports (data and voice), the default VLAN, and connectivity
- Configure and verify **interswitch connectivity**, including trunk ports, 802.1Q tagging, and the native VLAN
- Configure and verify **Layer 2 discovery protocols**, including Cisco Discovery Protocol (CDP) and LLDP
- Configure and verify **EtherChannel** using LACP at Layer 2 and Layer 3
- Interpret basic operations of **Rapid PVST+ Spanning Tree Protocol**, including root port, root bridge selection, port states, and PortFast
- Describe **Cisco wireless architectures** and AP modes
- Describe **physical infrastructure connections** of WLAN components, including AP, WLC, access/trunk ports, and LAG
- Describe **AP and WLC management access connections**, including Telnet, SSH, HTTP, HTTPS, console, and TACACS+/RADIUS
- Interpret the **wireless LAN GUI configuration** for client connectivity, including WLAN creation, security settings, and QoS profiles

*Strong VLAN and trunking skills set the foundation for [IP connectivity](/ccna/ip-connectivity-routing-ospf-static-routes/) later in the course.*

-----

## Domain 3: IP Connectivity (25%)

### [IP Connectivity and Routing](/ccna/ip-connectivity-routing-ospf-static-routes/)

- Interpret the components of the **routing table**, including routing protocol code, prefix, network mask, next hop, administrative distance, metric, and gateway of last resort
- Determine how a router makes a **forwarding decision** by default, including longest prefix match, administrative distance, and routing protocol metric
- Configure and verify **IPv4 and IPv6 static routing**, including default routes, network routes, host routes, and floating static routes
- Configure and verify **single area OSPFv2**, including neighbor adjacencies, point-to-point, broadcast (DR/BDR selection), and router ID
- Describe the purpose, functions, and concepts of **first hop redundancy protocols**

*This is the heaviest-weighted domain at 25%, so spend extra lab time configuring static routes and OSPF.*

-----

## Domain 4: IP Services (10%)

### [IP Services](/ccna/ip-services-nat-dhcp-qos-snmp/)

- Configure and verify **inside source NAT** using static entries and pools
- Configure and verify **NTP** operating in client and server mode
- Explain the role of **DHCP and DNS** within the network
- Explain the function of **SNMP** in network operations
- Describe the use of **syslog features**, including facilities and levels
- Configure and verify **DHCP client and relay**
- Explain **per-hop behavior (PHB) for QoS**, including classification, marking, queuing, congestion, policing, and shaping
- Configure network devices for **remote access using SSH**
- Describe the capabilities and function of **TFTP/FTP** in the network

-----

## Domain 5: Security Fundamentals (15%)

### [Security Fundamentals](/ccna/security-fundamentals-acls-vpn-layer2-security/)

- Define key **security concepts**, including threats, vulnerabilities, exploits, and mitigation techniques
- Describe **security program elements**, including user awareness, training, and physical access control
- Configure and verify **device access control** using local passwords
- Describe **password policy elements**, including management, complexity, and password alternatives such as MFA, certificates, and biometrics
- Describe **IPsec remote access and site-to-site VPNs**
- Configure and verify **access control lists (ACLs)**
- Configure and verify **Layer 2 security features**, including DHCP snooping, dynamic ARP inspection, and port security
- Compare **authentication, authorization, and accounting (AAA)** concepts
- Describe **wireless security protocols**, including WPA, WPA2, and WPA3
- Configure and verify a **WLAN using WPA2 PSK** within the GUI

-----

## Domain 6: Automation and Programmability (10%)

### [Automation and Programmability](/ccna/automation-programmability-apis-ansible-sdwan/)

- Explain how **automation** impacts network management
- Compare **traditional networks** with controller-based networking
- Describe **controller-based, software-defined architecture**, including overlay, underlay, and fabric, plus separation of the control plane and data plane and northbound and southbound APIs
- Compare traditional campus device management with **Cisco DNA Center** enabled device management
- Describe characteristics of **REST-based APIs**, including CRUD, HTTP verbs, and data encoding
- Recognize the capabilities of **configuration management tools**, including Puppet, Chef, and Ansible
- Recognize components of **JSON-encoded data**

-----

## A Note on CCNA v2.0

Cisco refreshed the 200-301 blueprint. The **CCNA v2.0** exam topics take effect with a first test date of **February 3, 2027**. The exam keeps the same 200-301 number and 120-minute format, but reorganizes the domains and adds AI content:

| Domain | Title | Exam Weight |
|--------|-------|-------------|
| 1.0 | Network Infrastructure and Connectivity | 25% |
| 2.0 | Switching and Network Access | 25% |
| 3.0 | IP Routing | 20% |
| 4.0 | Network Services and Security | 20% |
| 5.0 | AI, and Network Operations and Management | 10% |

*Key changes in v2.0:* added coverage of **agentic AI** in network operations, **generative AI prompts** for network tasks, OSPFv3 for IPv6, SFTP/SCP secure file transfers, and expanded Layer 2 security with storm control and RA guard. *If your exam date is before February 3, 2027, study the v1.0 topics above.*

-----

Work through all six domains, build the configurations in a lab such as Cisco Packet Tracer or GNS3, then assess your readiness with the [Cisco CCNA Practice Test](/ccna-practice-test/). For more certification courses and hands-on playbooks, visit [Courses and Playbooks](/courses-and-playbooks/).
