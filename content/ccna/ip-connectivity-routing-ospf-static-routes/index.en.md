---
title: "Cisco CCNA (200-301): IP Connectivity and Routing"
date: 2025-01-01
toc: true
draft: false
description: "Master IP connectivity for the Cisco CCNA 200-301 exam. Learn the routing table, forwarding decisions, IPv4 and IPv6 static routing, single-area OSPFv2, and first hop redundancy protocols."
genre: ["Cisco CCNA Course", "Networking", "Routing", "OSPF", "Static Routing", "IP Connectivity", "Cisco Certification", "Routing and Switching", "Network Architecture", "IT Networking"]
tags: ["Cisco CCNA", "200-301", "IP connectivity", "routing table", "static routing", "default route", "floating static", "OSPFv2", "neighbor adjacencies", "DR", "BDR", "router ID", "first hop redundancy", "administrative distance"]
cover: "/img/cover/cisco-ccna-routing-ip-connectivity-illustration.webp"
coverAlt: "An illustration of interconnected routers on a dark background, featuring glowing data flows in blue and green and a detailed routing table overlay with various network components."
coverCaption: "Master IP Connectivity and Routing for the CCNA 200-301 Exam"
---

#### [Click Here to Return To the Cisco CCNA Course Page](/ccna-start/)

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

**OSPFv2** is a link-state protocol that builds neighbor adjacencies and picks paths by cost. On broadcast networks, routers elect a **DR** and **BDR** to reduce flooding. The **router ID** identifies each router, and the highest loopback usually wins it.

```text
! Enable OSPF process 1 in area 0
Router(config)# router ospf 1
Router(config-router)# router-id 1.1.1.1
Router(config-router)# network 192.168.1.0 0.0.0.255 area 0
```

Verify adjacencies with `show ip ospf neighbor`. A neighbor stuck in a non-full state usually means a mismatched subnet, area, or timers.

## First Hop Redundancy

**First hop redundancy protocols (FHRP)** give hosts a default gateway that stays available. Two or more routers share one virtual IP, so if the active router fails, the standby takes over without changing client settings. **HSRP** is the common Cisco option.

## Next Steps

Add network services in [IP Services](/ccna/ip-services-nat-dhcp-qos-snmp/) and protect your routers in [Security Fundamentals](/ccna/security-fundamentals-acls-vpn-layer2-security/). Review the switching base in [Network Access](/ccna/network-access-vlans-spanning-tree-wireless/) and return to the [Cisco CCNA Course](/ccna-start/).
