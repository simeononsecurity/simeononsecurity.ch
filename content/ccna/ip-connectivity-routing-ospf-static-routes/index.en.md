---
title: "Cisco CCNA (200-301): IP Connectivity and Routing"
date: 2025-01-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Configure a two-router CCNA v1.1 lab, test longest-prefix routing, verify OSPF neighbors, and diagnose one controlled failure."
genre: ["Cisco CCNA Course", "Networking", "Routing", "OSPF", "Static Routing", "IP Connectivity", "Cisco Certification", "Routing and Switching", "Network Architecture", "IT Networking"]
tags: ["Cisco CCNA", "200-301", "IP connectivity", "routing table", "static routing", "default route", "floating static", "OSPFv2", "neighbor adjacencies", "DR", "BDR", "router ID", "first hop redundancy", "administrative distance"]
cover: "/img/cover/cisco-ccna-routing-ip-connectivity-illustration.webp"
coverAlt: "An illustration of interconnected routers on a dark background, featuring glowing data flows in blue and green and a detailed routing table overlay with various network components."
coverCaption: "Master IP Connectivity and Routing for the CCNA 200-301 Exam"
---

[Click Here to Return To the Cisco CCNA Course Page](/ccna-start/)

**IP Connectivity** is the heaviest domain on the **Cisco CCNA (200-301)** exam at **25%**. This module covers how routers choose paths and how you configure static and OSPF routing. *Spend extra lab time here, because this domain carries the most weight.*

Routing connects separate networks. You learn to read the routing table, predict the forwarding decision, and build both static and dynamic routes.

## The Routing Table

Every line in the routing table tells you how to reach a network.

| Field | Meaning |
|-------|---------|
| **Protocol code** | How the route was learned (C, S, O, D) |
| **Prefix and mask** | The destination network |
| **Next hop** | The address to forward toward |
| **Administrative distance** | Trust level of the source |
| **Metric** | Cost within a protocol |
| **Gateway of last resort** | The default route |

```text
! View the IPv4 routing table
Router# show ip route
```

## Forwarding Decisions

When several routes could match, the router applies clear rules in order:

1. **Longest prefix match** wins first, since the most specific route is preferred.
2. **Administrative distance** breaks ties between protocols.
3. **Metric** breaks ties within the same protocol.

| Source | Administrative distance |
|--------|-------------------------|
| Connected | 0 |
| Static | 1 |
| OSPF | 110 |
| RIP | 120 |

## Static Routing

You configure **static routes** by hand for predictable paths. A **default route** sends all unknown traffic toward one next hop, and a **floating static** route backs up a dynamic route with a higher administrative distance.

```text
! IPv4 static and default routes
Router(config)# ip route 10.2.2.0 255.255.255.0 192.168.1.2
Router(config)# ip route 0.0.0.0 0.0.0.0 192.168.1.1

! IPv6 static route
Router(config)# ipv6 route 2001:db8:2::/64 2001:db8:1::2
```

## Single-Area OSPFv2

**OSPFv2** is a link-state protocol that builds neighbor adjacencies and picks paths by cost. On broadcast networks, routers elect a **DR** and **BDR** to reduce flooding. An explicitly configured router ID wins. Without one, Cisco IOS selects the highest active loopback IPv4 address, then the highest active interface IPv4 address when no loopback exists. An existing OSPF process may need a restart before a changed ID takes effect.

```text
! Enable OSPF process 1 in area 0
Router(config)# router ospf 1
Router(config-router)# router-id 1.1.1.1
Router(config-router)# network 192.168.1.0 0.0.0.255 area 0
```

Verify adjacencies with `show ip ospf neighbor`. An absent or stuck neighbor has several possible causes, including interface state, subnet, area, timers, authentication, or network type. Compare both ends before changing configuration.

## First Hop Redundancy

**First hop redundancy protocols (FHRP)** give hosts a default gateway that stays available. Two or more routers share one virtual IP, so if the active router fails, the standby takes over without changing client settings. **HSRP** is the common Cisco option.

## Lab 3: Route Between VLANs and to a Server

Continue the [course topology](/ccna-start/) after VLAN 10 and VLAN 20 trunks work. Enter the following in a disposable Packet Tracer project, adapting interface names to your model. R1 `g0/0` connects to S1's trunk. R1 `g0/1` connects to R2 `g0/0`. R2 `g0/1` connects to SRV1. Save a copy before each routing change.

```text
R1(config)# interface g0/0
R1(config-if)# no shutdown
R1(config)# interface g0/0.10
R1(config-subif)# encapsulation dot1Q 10
R1(config-subif)# ip address 10.10.10.1 255.255.255.0
R1(config)# interface g0/0.20
R1(config-subif)# encapsulation dot1Q 20
R1(config-subif)# ip address 10.10.20.1 255.255.255.0
R1(config)# interface g0/1
R1(config-if)# ip address 192.0.2.1 255.255.255.252
R1(config-if)# no shutdown
R2(config)# interface g0/0
R2(config-if)# ip address 192.0.2.2 255.255.255.252
R2(config-if)# no shutdown
R2(config)# interface g0/1
R2(config-if)# ip address 198.51.100.1 255.255.255.0
R2(config-if)# no shutdown
```

Set PC-A, PC-B, and SRV1 to the static addresses in the hub. Each should ping its gateway. A PC-A ping to SRV1 should fail until R1 learns `198.51.100.0/24` and R2 learns the return path. First practice static routes:

```text
R1(config)# ip route 198.51.100.0 255.255.255.0 192.0.2.2
R2(config)# ip route 10.10.10.0 255.255.255.0 192.0.2.1
R2(config)# ip route 10.10.20.0 255.255.255.0 192.0.2.1
```

Collect `show ip route`, `show ip interface brief`, and PC-A to SRV1 ping results. Remove those three static routes with the same commands prefixed by `no`, then enable OSPF area 0:

```text
R1(config)# router ospf 1
R1(config-router)# router-id 1.1.1.1
R1(config-router)# network 10.10.10.0 0.0.0.255 area 0
R1(config-router)# network 10.10.20.0 0.0.0.255 area 0
R1(config-router)# network 192.0.2.0 0.0.0.3 area 0
R2(config)# router ospf 1
R2(config-router)# router-id 2.2.2.2
R2(config-router)# network 192.0.2.0 0.0.0.3 area 0
R2(config-router)# network 198.51.100.0 0.0.0.255 area 0
```

`show ip ospf neighbor` should show the other router in FULL state. `show ip route ospf` on R1 should include `198.51.100.0/24`; on R2 it should include both `10.10` VLAN networks. If a command is unsupported on your simulated model, record that and use `show ip route` instead. Test PC-A and PC-B pings to SRV1.

For a controlled fault, shut R1 `g0/1`. Neighbor and remote route should disappear after convergence. Restore `no shutdown` and capture the return to FULL. Before changing anything else, compare local interface state, peer address and mask, OSPF area, and timers. Do not diagnose a mismatch only from an empty neighbor table.

On paper, choose between `198.51.100.0/24` and `198.51.100.10/32` for destination `198.51.100.10`. The `/32` wins by longest prefix. For equal prefixes from different protocols, compare administrative distance, then a protocol's metric as appropriate.

Your checkpoint is a port and address map, static-route output, OSPF neighbor and route output, successful end-to-end ping, fault symptom, repair, and final state. Pass when you explain both the forward and return paths and distinguish a router-ID choice from an adjacency failure. [Cisco's OSPF configuration guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/15-mt/iro-15-mt-book/iro-cfg.html) supports the ID selection order. Match exam scope to the [CCNA v1.1 topics](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf).

## Next Steps

Add network services in [IP Services](/ccna/ip-services-nat-dhcp-qos-snmp/) and protect your routers in [Security Fundamentals](/ccna/security-fundamentals-acls-vpn-layer2-security/). Review the switching base in [Network Access](/ccna/network-access-vlans-spanning-tree-wireless/) and return to the [Cisco CCNA Course](/ccna-start/).
