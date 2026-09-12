---
title: "Why Tailscale Uses a Relay: Direct Connections, DERP, and Peer Relays"
date: 2026-09-11
lastmod: 2026-09-11
toc: true
draft: false
description: "Find out why Tailscale uses a relay, read status and netcheck output, and decide whether a DERP or peer-relay connection needs troubleshooting."
genre: ["Networking", "Network Security", "Self-Hosted"]
tags: ["Tailscale", "Tailscale relay", "DERP", "Tailscale Peer Relay", "direct connection", "WireGuard", "NAT traversal", "hard NAT", "CGNAT", "UDP", "tailscale status", "tailscale ping", "tailscale netcheck", "MappingVariesByDestIP", "VPN performance", "remote access", "tailnet", "homelab networking", "relay latency", "end-to-end encryption"]
cover: "/img/cover/why-tailscale-uses-a-relay.webp"
coverAlt: "Two laptops on separate islands exchange locked packets through a central relay while a direct path is interrupted."
coverCaption: ""
---

**Tailscale uses a relay** when devices have not established a direct connection. A brief DERP connection during startup is normal. Persistent relaying often reflects network address translation (NAT) or firewall conditions affecting the route between the devices. Direct, DERP, and peer-relay connections all retain WireGuard end-to-end encryption. [Tailscale connection types](https://tailscale.com/docs/reference/connection-types).

## Key Takeaways

- **Recognize the path:** distinguish direct, DERP, and peer-relay connections.
- **Collect evidence:** run peer-specific probes and network checks on both ends.
- **Analyze the pattern:** compare device pairs and network conditions.
- **Choose a change:** justify it with a measured workload and a retest.

## Before You Begin

**Prerequisites:** two enrolled, online devices and a terminal with the Tailscale command-line interface, or **CLI**, available. You need administrative access only if the investigation leads to configuration changes.

**Estimated effort:** five minutes for basic checks, then 15–20 minutes for the comparison exercise. **Difficulty:** beginner for observation and intermediate for network changes. Define the problem first, such as a slow backup or delayed terminal response.

## Direct, DERP, and Peer Relay

A **tailnet** is your Tailscale network. Its devices attempt direct UDP connectivity, with relays available when the direct path fails. Tailscale periodically rechecks its connection options. [Connection establishment](https://tailscale.com/docs/reference/connection-types).

| Path | Traffic route | Typical implication |
|---|---|---|
| **Direct** | Between the two devices | Usually the preferred performance path |
| **DERP relay** | Through Tailscale relay infrastructure | Adds an intermediary when direct access fails |
| **Peer relay** | Through a configured device in your tailnet | An alternative relay under your administration |

**DERP performance** depends partly on the extra route and shared service capacity. Tailscale documents throughput limits intended to share DERP resources fairly. There is no universal relay speed suitable for predicting your file-transfer time. [Tailscale performance troubleshooting](https://tailscale.com/docs/reference/troubleshooting/poor-performance-tailnet).

## Understand Connection Negotiation

**NAT traversal** is the process of establishing a usable path across address-translating devices. Tailscale begins communication through DERP while negotiating a direct path. If direct connectivity fails, an available configured peer relay provides another option. Tailscale rechecks its options over time. [Connection establishment](https://tailscale.com/docs/reference/connection-types).

**Hard NAT** describes mapping behavior making traversal difficult. The conditions at both ends matter. Two devices behind different routers do not necessarily behave alike, even if both networks use private addresses. [Device connectivity](https://tailscale.com/docs/reference/device-connectivity).

For **a roaming laptop**, the path to your home server might change after moving from home Wi-Fi to a hotel network. Record the network used during the observation. Yesterday's direct connection is not evidence about today's route.

## Check Your Current Connection

Replace **`home-server`** with your peer's Tailscale name or address:

```bash
tailscale ping home-server
tailscale status
tailscale netcheck
```

**`tailscale ping`** probes connectivity to the named peer. **`tailscale status`** lists peers and connection details. **`tailscale netcheck`** reports conditions on the device running the command. The [Tailscale CLI reference](https://tailscale.com/docs/reference/tailscale-cli) documents these commands.

| Output indicator | Read it as |
|---|---|
| **`direct`** | Traffic to this peer uses a direct path |
| **`relay`** | Traffic to this peer uses DERP |
| **`peer-relay`** | Traffic uses a configured peer relay |
| **An initial DERP pong** | Inspect subsequent results before deciding the path stayed relayed |

These labels come from the [connection-type documentation](https://tailscale.com/docs/reference/connection-types). **Generate traffic first**, then inspect the peer you care about. The commands above are examples, not captured results from a benchmark.

## Interpret a Path Change

This **illustrative sequence** omits addresses and timings so you focus on the connection transition:

```text
First response:    via DERP
Later response:    via a direct endpoint
Status afterward: direct
```

**Interpretation:** negotiation succeeded during this observation. The first response alone would have produced the wrong diagnosis. If later responses and status remain relayed, record a persistent relay for this device pair and test period.

**Probe scope:** a successful Tailscale ping establishes peer connectivity for its probe. It does not prove your dashboard, file service, or SSH daemon accepts application traffic. Test the failing application separately before declaring the problem solved.

## What Netcheck Tells You

Run **`tailscale netcheck` on both devices**. Compare these fields against the [device-connectivity reference](https://tailscale.com/docs/reference/device-connectivity):

| Field | Useful interpretation |
|---|---|
| **`UDP`** | Whether the probe observed outbound UDP connectivity |
| **`MappingVariesByDestIP`** | Changing external mappings suggest difficult NAT traversal |
| **`IPv6`** | Whether this device has usable IPv6 connectivity |
| **`PortMapping`** | Whether a supported port-mapping mechanism is available |

**One field is not a verdict.** An available mapping mechanism does not prove a particular peer path works. Likewise, a relay label does not identify which router caused it. Compare both endpoints and the actual ping results.

**Carrier NAT** is relevant when upstream translation is outside your control, as discussed in our [T-Mobile port-forwarding explainer](/articles/t-mobile-home-internet-port-forwarding/). Avoid assuming every connection behind carrier NAT has identical traversal behavior.

## Compare Three Device Pairs

Use a **third enrolled device**, if available, to improve the evidence. The following is a hypothetical pattern, not a measured result:

| Device pair | Observed path |
|---|---|
| **Laptop to home server** | DERP |
| **Laptop to another server** | Direct |
| **Home server to another server** | DERP |

**Working hypothesis:** prioritize the home server's network for investigation because both observed paths involving it stayed relayed. This is a lead, not proof. Each pair negotiates independently, and the comparison server has its own network conditions.

**Next observation:** collect netcheck output on all three devices and repeat the laptop-to-home test from another network you control. If the path changes, record exactly which network changed. Avoid attributing the result to a particular firewall setting until you test it.

**Review exercise:** laptop-to-home is direct, but a file transfer remains slow. A relay explanation no longer matches this observation. Check the underlying upload connection, server load, storage, and application behavior before changing relay settings.

## Choose a Targeted Change

Start with a **comparison test** on another network you control. If the same peer becomes direct, you have useful evidence about the original network path. Review its UDP restrictions and NAT arrangement before changing unrelated DNS or application settings.

**Change one variable**, rerun the checks, and measure the same workload. Record transfer direction, file size, elapsed time, and connection type. This separates an improved path from an unrelated change in server or storage load.

**Firewall changes** should follow the platform-specific guidance and the evidence you collected. Opening an application port to the public Internet does not itself improve Tailscale's transport path. Keep changes limited to the required traffic and network you administer. [Tailscale firewall guidance](https://tailscale.com/docs/integrations/firewalls).

| Finding | Change worth evaluating |
|---|---|
| **UDP probe fails** | Review outbound UDP restrictions on this network |
| **Mapping changes across destinations** | Review NAT behavior on equipment you control |
| **Direct path, slow application** | Investigate the host, underlying connection, and workload |
| **Working relay, acceptable experience** | Keep the arrangement and document the baseline |

*Prefer a measured improvement over changing settings solely to remove a relay label.*

## Evaluate a Peer Relay

A **peer relay** requires a suitable host, reachable UDP port, and an access policy permitting its use. Both the relay and participating clients require Tailscale 1.86 or later. Review supported host platforms before allocating a device. [Peer-relay requirements](https://tailscale.com/docs/features/peer-relay).

**Placement determines usefulness.** A device behind the same inaccessible network boundary needs a reachable relay port before it helps other peers. Choosing a host geographically near the endpoints is insufficient without connectivity to it.

**Maintenance tradeoff:** someone must keep the relay online, updated, and adequately provisioned. For occasional administration with acceptable latency, compare this burden with the measured benefit. For repeated large transfers, measure the workload through the proposed relay before adopting it.

## Check Shared Traffic Effects

**Aggregated traffic** deserves attention when a subnet router or exit node carries several workloads through DERP. Tailscale documents situations where heavy relayed traffic delays latency-sensitive traffic sharing the connection. [Hard-NAT troubleshooting](https://tailscale.com/docs/reference/troubleshooting/network-configuration/hard-nat-issues).

**Comparison exercise:** observe your interactive session before, during, and after a large backup. Keep the endpoint pair fixed and record the path each time. Delays appearing during the transfer justify investigating shared load, but do not establish its exact cause.

**Choose the next test** from the observation. Check link saturation and host load, then evaluate a direct path or separating latency-sensitive services if the topology supports it. Avoid treating a DNS symptom as automatic evidence of a DNS configuration error.

## Is a Relay an Exit Node?

An **exit node** routes a client's general Internet traffic through a selected tailnet device. A relay carries traffic between Tailscale peers. Selecting an exit node does not guarantee a direct path to it. [Exit-node documentation](https://tailscale.com/docs/features/exit-nodes).

## Create a Diagnostic Record

Save a **small before-and-after record** for the actual problem:

```text
Date and Tailscale versions:
Source and destination devices:
Networks used by each device:
Initial and settled connection paths:
Netcheck observations from both ends:
Workload, direction, and elapsed time:
Single change tested:
Retest result:
Decision to keep or revert:
```

**Completion criterion:** the record links a specific symptom to observations, a hypothesis, and a measured retest. “Relay disappeared” is incomplete if the application is still slow. “The backup meets its time requirement through DERP” is a valid result if the requirement is explicit.

## Next Steps

Record the path to your important peer and test the workload before changing network settings. For the separate question of who operates your coordination infrastructure, read [Tailscale vs Headscale](/articles/tailscale-vs-headscale-comparison-guide/).
