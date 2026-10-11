---
title: "Cisco CCNA (200-301): Network Access"
date: 2025-01-01
toc: true
draft: false
description: "Practice CCNA v1.1 VLANs, trunks, Rapid PVST+ guards, EtherChannel, and device management access."
lastmod: 2026-10-10
genre: ["Cisco CCNA Course", "Networking", "Switching", "VLANs", "Spanning Tree", "Wireless", "Cisco Certification", "Network Access", "EtherChannel", "IT Networking"]
tags: ["Cisco CCNA", "200-301", "VLANs", "trunking", "802.1Q", "EtherChannel", "LACP", "spanning tree", "Rapid PVST+", "PortFast", "CDP", "LLDP", "wireless", "WLC", "access points", "network access"]
cover: "/img/cover/cisco-ccna-network-access-vlan-etherchannel-wireless.webp"
coverAlt: "An illustration depicting a network topology with interconnected switches, VLAN configurations, EtherChannel connections, and wireless access points, all on a dark background."
coverCaption: "Master Network Access for the CCNA 200-301 Exam"
---

#### [Click Here to Return To the Cisco CCNA Course Page](/ccna-start/)

**Network Access** is **20%** of the **Cisco CCNA (200-301)** exam. This module covers VLANs, trunking, EtherChannel, spanning tree, and wireless access. *These are the configuration skills interviewers love to test on a live switch.*

This domain ties the most hands-on configuration to the exam. You build VLANs, connect switches with trunks, bundle links, and keep the topology loop-free.

## VLANs and Access Ports

A **VLAN** splits one physical switch into separate broadcast domains. You assign an access port to a single data VLAN and often a voice VLAN for IP phones.

```text
! Create a VLAN and assign an access port
Switch(config)# vlan 10
Switch(config-vlan)# name SALES
Switch(config)# interface g0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
```

The **default VLAN** is VLAN 1, and best practice moves user traffic off it. Verify your work with `show vlan brief`.

## Trunking and Discovery

A **trunk** carries many VLANs between switches using **802.1Q** tagging. The **native VLAN** rides untagged, so match it on both ends.

```text
! Configure an 802.1Q trunk
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk native vlan 99
```

**Layer 2 discovery protocols** map neighbors. **CDP** is Cisco-proprietary, and **LLDP** is the open standard.

| Protocol | Scope |
|----------|-------|
| **CDP** | Cisco devices only |
| **LLDP** | Vendor-neutral (IEEE 802.1AB) |

## EtherChannel

**EtherChannel** bundles links into one logical connection for more bandwidth and redundancy. **LACP** negotiates the bundle and is the standard option.

```text
! Bundle two ports with LACP
Switch(config-if-range)# channel-group 1 mode active
```

## Spanning Tree

**Rapid PVST+** prevents Layer 2 loops by blocking redundant paths. Know these roles and states:

| Term | Meaning |
|------|---------|
| **Root bridge** | Switch with the lowest bridge ID |
| **Root port** | Best path toward the root bridge |
| **Designated port** | Forwarding port on each segment |
| **PortFast** | Moves an edge port to forwarding quickly. Use only where a switch is not expected. |

Cisco v1.1 also asks you to identify four safeguards:

| Feature | Purpose | Placement check |
|---|---|---|
| Root guard | Keeps a downstream switch from becoming the root | Designated ports toward downstream switches |
| Loop guard | Reduces loop risk when expected BPDUs stop arriving | Root or alternate ports where supported |
| BPDU guard | Disables an edge port when it receives a BPDU | PortFast edge ports |
| BPDU filter | Suppresses BPDUs under configured conditions | Use only after reviewing the loop risk |

Do not apply a guard by name alone. Draw the intended root and port roles first, then verify the resulting state with `show spanning-tree`.

The switch with the lowest **bridge ID** (priority plus MAC) becomes the root. Set priority manually so the right switch wins.

## Wireless Access

**Cisco wireless architectures** often use a **WLC** to manage lightweight access points. Management access depends on the platform and policy. Cisco v1.1 includes console, SSH, HTTPS, TACACS+/RADIUS, legacy Telnet and HTTP, and cloud-managed access. Prefer encrypted administrative paths. A cloud-managed device uses a remote management service, but you still need to verify its local connectivity and the management account's scope. In a controller GUI, review the WLAN, security mode, and QoS profile before applying a change.

## Lab: Verify the Access Path

Use two lab switches and one test host. Keep the lab separate from a production network.

1. Create VLAN 10 on both switches. Assign the host-facing port to VLAN 10. Configure the interswitch link as a trunk.
2. Record `show vlan brief` and `show interfaces trunk` from both switches. The host VLAN must appear on both ends.
3. Identify the Rapid PVST+ root with `show spanning-tree`. Mark the root port and designated ports in a diagram.
4. Place BPDU guard on a host-only PortFast port in the lab. Connect a second lab switch to that port and observe the protection response. Restore the host port after documenting the event.
5. Compare local HTTPS or SSH management with any available cloud management option. Record which identity grants access and which path stops working when management connectivity is removed.

**Pass condition:** Your diagram matches the observed root and port roles. Both switches carry VLAN 10, the guarded lab port reacts to an unexpected BPDU, and your evidence identifies the tested management path. If the simulator lacks a guard or cloud feature, mark that row untested and use Cisco's [v1.1 exam topics](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf) for a separate concept check.

## Next Steps

Route between your VLANs in [IP Connectivity](/ccna/ip-connectivity-routing-ospf-static-routes/), then secure access in [Security Fundamentals](/ccna/security-fundamentals-acls-vpn-layer2-security/). Review the foundations in [Network Fundamentals](/ccna/network-fundamentals-osi-tcp-ip-switching/) and return to the [Cisco CCNA Course](/ccna-start/).
