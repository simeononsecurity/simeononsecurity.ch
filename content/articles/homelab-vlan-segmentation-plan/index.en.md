---
title: "Plan and Test VLAN Segmentation for a Homelab"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Build a homelab VLAN plan for trusted devices, servers, IoT, and guests. Map allowed traffic, configure the network in stages, and test isolation."
genre: ["Homelab", "Network Security", "Networking"]
tags: ["homelab VLAN", "VLAN segmentation", "IoT network", "guest network", "homelab firewall", "inter VLAN routing", "802.1Q", "network isolation", "VLAN test", "pfSense VLAN", "access port", "trunk port", "firewall rules", "homelab security", "network plan", "subnet", "DHCP", "DNS", "managed switch", "wireless SSID"]
cover: "/img/cover/homelab-vlan-segmentation-plan.webp"
coverAlt: "A homelab router and switch separating laptops, servers, IoT devices, and guests into protected network zones."
coverCaption: "Plan VLAN boundaries, then test every allowed and denied path."
---

A homelab often puts laptops, servers, cameras, and guest devices on one network. **VLAN segmentation** places those groups on separate networks. A firewall then controls traffic between them. This guide helps you write the plan, make one change at a time, and test the result.

## Key Takeaways

- **Group by trust:** Put management devices, servers, IoT devices, and guests in separate networks when their access needs differ.
- **Write allowed paths:** Record the source, destination, service, and reason for each cross-network connection.
- **Configure both layers:** Switch and access point VLAN settings place devices. Firewall rules control routed traffic.
- **Test both outcomes:** Check an allowed connection and a denied connection from each relevant network.

## Before You Begin

You need a router or firewall with VLAN interfaces, a managed switch for wired VLANs, and an access point with VLAN-backed wireless networks if you separate wireless clients. Keep a device on the current management network while you change the configuration. Save the router, switch, and access point settings first. The steps below use an **illustrative plan**, so adapt the addresses and ports to your equipment.

If you need the basic terms first, read [subnets and VLANs](/articles/networking-basics-what-are-subnets-and-vlans/). The site's [network segmentation guide](/articles/how-to-perform-network-segmentation-for-improved-security/) covers the broader security concept. CISA describes separate home networks for guests and Internet of Things devices in its [Federal Mobile Workplace Security guidance](https://www.cisa.gov/sites/default/files/2024-08/Federal-Mobile-Workplace-Security_508_2024-08-14.pdf).

> **Warning:** A VLAN change on the port carrying your management connection might lock you out. Keep physical access and a known recovery path until every network passes its tests.

## Inventory Devices and Flows

List each device, its current address, its owner, and the services it needs. Give every device a reason to reach another network. For example, a laptop might administer a server, while a camera might reach only a recorder and DNS server. A guest phone needs internet access but no server access.

| Device group | Example devices | Required access |
|---|---|---|
| **Management** | Admin laptop, switch and access point management | Router, switch, access point, server administration |
| **Servers** | Hypervisor, NAS, backup target | Updates, DNS, approved application traffic |
| **IoT** | Cameras, smart plugs, media devices | DNS, time service, specific controller or recorder |
| **Guests** | Visitor phones and laptops | Internet, DNS, no private subnets |

Write down exceptions before adding rules. Local discovery features such as casting often depend on multicast traffic that does not cross a routed boundary by default. Do not open all traffic between VLANs to repair one discovery problem. Identify the protocol and add the smallest supported exception.

## Assign VLANs and Addresses

Give each group a VLAN ID and a separate IP subnet. This **illustrative plan** uses documentation addresses and assumes the router supplies DHCP and DNS. Do not copy the table into a live network without checking for address conflicts.

| Network | VLAN ID | Subnet | Example gateway |
|---|---:|---|---|
| **Management** | 10 | `192.0.2.0/27` | `192.0.2.1` |
| **Servers** | 20 | `198.51.100.0/27` | `198.51.100.1` |
| **IoT** | 30 | `203.0.113.0/27` | `203.0.113.1` |
| **Guests** | 40 | `192.0.2.32/27` | `192.0.2.33` |

These reserved documentation ranges illustrate the layout only. Use private addresses from [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) for your actual lab, with a nonoverlapping subnet per VLAN. Record each real gateway, DHCP pool, DNS address, and device reservation in your plan.

**Access ports** carry one device network without a VLAN tag. **Trunk ports** carry selected tagged VLANs between the router, switch, and access point. Match the port's VLAN ID and native or untagged setting at both ends. Netgate's [VLAN switch guide](https://docs.netgate.com/pfsense/en/latest/recipes/switch-vlan-configuration.html) explains tagged trunk ports, untagged access ports, and port VLAN IDs. Avoid using the default VLAN 1 for management when your hardware permits a separate VLAN, as described in Netgate's [VLAN security guidance](https://docs.netgate.com/pfsense/en/latest/vlan/security.html).

## Build a Traffic Matrix

A VLAN by itself separates broadcast domains. **Inter-VLAN routing** at the router or layer-3 switch still needs firewall policy. Use the device inventory to record the connections you intend to allow. The following entries are examples, not a universal rule set.

| Source | Destination | Service | Decision |
|---|---|---|---|
| **Management** | Server admin interface | TCP 443 | Allow for approved admin devices |
| **IoT** | Camera recorder | Recorder's documented port | Allow only if needed |
| **IoT** | Management subnet | Any | Deny |
| **Guests** | Private subnets | Any | Deny |
| **Guests** | DNS and internet | DNS, web traffic | Allow through approved resolver and gateway |

Include the router's own services in the plan. A rule that blocks IoT access to other VLANs might still leave the router's administrative interface reachable. Restrict management services to the management network. If you use pfSense, its [rule methodology](https://docs.netgate.com/pfsense/en/latest/firewall/rule-methodology.html) explains that interface rules filter traffic entering that interface and that allowed connections create state for return traffic.

## Configure One Network at a Time

1. Create one VLAN interface on the router. Assign its gateway address and DHCP scope. Confirm the router's DNS service or an approved resolver is reachable from that VLAN. Netgate's [VLAN configuration guide](https://docs.netgate.com/pfsense/en/latest/vlan/configuration.html) lists these separate interface and service steps for pfSense.
2. Add the VLAN to the router-to-switch trunk. Add the same VLAN to the relevant switch-to-access-point trunk if wireless clients need the network.
3. Assign one test access port or wireless SSID to the VLAN. Move a noncritical test device onto that port or SSID.
4. Add the intended allow rules, then deny unwanted access to other private networks and the router's management services. Check your firewall's rule order and its default behavior.
5. Confirm the test device receives an address, gateway, and DNS server from the intended subnet. Then run the connection checks below before moving more devices.

Do not move the last management device until its replacement path works. Save the working configuration after each network passes. Roll back the last change if DHCP, DNS, or management access fails.

## Test Isolation and Access

Use a service you control and know is listening on the destination. From a Windows test device, replace the example address and port with a real server and run:

```powershell
Test-NetConnection -ComputerName 198.51.100.10 -Port 443
```

The **`TcpTestSucceeded`** field reports whether a TCP connection completed. Microsoft's [Test-NetConnection reference](https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection) documents the `-ComputerName` and `-Port` parameters. A failed connection alone does not prove a firewall rule worked. The service might be down, or the host firewall might reject traffic. Check the destination service and the network firewall log before drawing a conclusion.

Test from each relevant source VLAN. Record an allowed connection to the intended service, a denied connection to an internal service outside the matrix, and working DNS and internet access where planned. On pfSense, **Status > System Logs > Firewall** shows logged pass or block actions. Netgate's [firewall log guide](https://docs.netgate.com/pfsense/en/latest/monitoring/logs/firewall.html) explains the view. Compare the log's source, destination, port, and rule to your test. If the test unexpectedly succeeds, inspect broad allow rules and existing state entries.

> **Expected Result:** Each device receives an address from its planned subnet. Allowed services work. Denied attempts match a firewall block or a documented equivalent control.

## Troubleshooting

- **No address:** Check the access port or SSID VLAN, trunk tags, DHCP scope, and gateway interface.
- **Address works, DNS fails:** Check the resolver address, router service binding, and firewall rule for DNS traffic.
- **One device reaches another VLAN unexpectedly:** Check router rules, broad allow rules, and whether both devices still share an untagged network.
- **A denied test times out without a firewall log:** Confirm the destination service is listening. Then inspect routing and logging settings. Netgate's [firewall troubleshooting guide](https://docs.netgate.com/pfsense/en/latest/troubleshooting/firewall.html) describes the log and state checks.
- **Casting or discovery stops:** Identify the discovery protocol and controller path before adding a narrow exception.

## Next Steps

Keep the device inventory and traffic matrix with your network diagram. Review the rules when you add a server or IoT device. Repeat one allowed and one denied connection test after each relevant network change. For the broader design principles, return to [network segmentation](/articles/how-to-perform-network-segmentation-for-improved-security/).
