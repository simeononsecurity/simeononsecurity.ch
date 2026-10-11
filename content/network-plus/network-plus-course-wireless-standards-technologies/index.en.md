---
title: "CompTIA Network+ N10-009: Wireless Standards"
date: 2023-07-11
toc: true
draft: false
description: "Compare wireless standards, bands, channels, PHY rates, RSSI, noise, SNR, antennas, roaming, BSSID, ESSID, and access point models."
lastmod: 2026-10-10
genre: ["CompTIA Network+", "N10-009", "Networking", "Certification Course"]
tags: ["CompTIA Network+", "N10-009", "Wireless Standards", "network lab", "network troubleshooting", "exam prep"]
cover: "/img/cover/A_cartoon_illustration_showcasing_different_wi.webp"
coverAlt: "A cartoon illustration showcasing different wireless network devices and signals."
coverCaption: "Unleash the Power of Wireless Networks"
---

[Click Here to Return To the Network Plus Course Page](/network-plus-start)

Wireless networks play a crucial role in our interconnected world, allowing seamless communication and internet access. As part of the **CompTIA Network+ Certification Exam**, it's essential to understand various wireless standards and technologies. In this article, we will explore the **802.11 standards**, frequencies, range, channel bonding, antenna types, encryption standards, and SSID configurations commonly used in wireless networks.

______

## Exploring Different 802.11 Standards

The 802.11 standards, commonly known as Wi-Fi, define the specifications for wireless local area networks (WLANs). 
Let's delve into some of the most prevalent 802.11 standards:

| Standard  | Introduction Year | Frequency Range | Maximum Data Rate |
|-----------|-------------------|-----------------|-------------------|
| 802.11a   | 1999              | 5GHz            | 54 Mbps           |
| 802.11b   | 1999              | 2.4GHz          | 11 Mbps           |
| 802.11g   | 2003              | 2.4GHz          | 54 Mbps           |
| 802.11n   | 2009              | 2.4GHz/5GHz     | Up to 600 Mbps    |
| 802.11ac  | 2014              | 5GHz            | Up to 6.77 Gbps   |
| 802.11ax (Wi-Fi 6) | 2019        | 2.4GHz/5GHz     | Up to 9.6 Gbps    |
| 802.11ax (Wi-Fi 6E) | 2021       | 6GHz            | Up to 9.6 Gbps across supported bands |

These rates are theoretical PHY ceilings. Real throughput depends on channel width, signal quality, client capability, interference, and network load. Wi-Fi 6E extends 802.11ax into the 6 GHz band. It is not a new 802.11 amendment. Check local rules and device support before enabling 6 GHz.

______

## Frequencies, Range, and Channel Bonding in Wireless Networks

Wireless networks utilize different frequencies, each with its unique characteristics. Let's explore the common frequencies and their impact on range and channel bonding.

### Frequencies and Range

- **2.4GHz**: This frequency is widely used and provides better coverage over longer distances. However, it is more susceptible to interference from other devices, such as microwaves and cordless phones.

- **5GHz**: The 5GHz frequency offers higher data rates and reduced interference compared to 2.4GHz. However, it has a shorter range due to higher attenuation of signals at this frequency.

- **6 GHz**: Wi-Fi 6E uses additional spectrum and channels where local rules allow it. Devices need 6 GHz support. Compared with 2.4 GHz, 6 GHz usually has less reach through walls at the same power and deployment conditions. Plan access point placement from a site survey.

### Channels

Wireless networks are divided into channels, and the available channels may vary depending on the regulatory domain.

**Regulatory Impacts**: Different countries have specific regulations regarding wireless frequency usage. For instance, in the United States, the Federal Communications Commission (FCC) regulates wireless communication under Part 15 of their rules and regulations.

**Channel Bonding**: Channel bonding allows the aggregation of multiple channels to increase the overall bandwidth available for data transmission. It improves network performance by enabling higher data rates.

______

## Overview of Antenna Types, Encryption Standards, and SSID Configurations

Wireless networks rely on various components, including antennas, encryption standards, and SSID configurations. Let's explore each of these components in detail.

### Antenna Types

Wireless networks utilize different types of antennas to transmit and receive signals. The two common types are:

- **Omni**: Omni-directional antennas radiate signals in all directions, making them suitable for providing coverage over a wide area.

- **Directional**: Directional antennas focus signals in a specific direction, allowing for longer-range connections in a particular direction.

### Encryption Standards

Select authentication and encryption together. For a new network, prefer WPA3 where clients support it. Use WPA2 with AES-based CCMP for clients which lack WPA3 support. WPA and TKIP are legacy choices and should not be presented as current deployment defaults.

| Mode | Typical authentication | Use case |
|---|---|---|
| WPA2-Personal | Shared passphrase (PSK) | Small network with compatible clients |
| WPA3-Personal | Simultaneous Authentication of Equals (SAE) | New personal network with WPA3 clients |
| WPA2-Enterprise | 802.1X/EAP with an authentication server | Managed users with individual credentials |
| WPA3-Enterprise | 802.1X/EAP with WPA3 protections | Managed users where devices and infrastructure support it |

Do not treat a hidden SSID or MAC filter as a replacement for these controls. The [CompTIA N10-009 objectives](https://comptiacdn.azureedge.net/webcontent/docs/default-source/exam-objectives/comptia-network-n10-009-exam-objectives-%284-0%29-%281%29.pdf?sfvrsn=f31cc6c4_4) include 6 GHz, WPA2, WPA3, and personal versus enterprise authentication.

### SSID Configurations

The Service Set Identifier (SSID) is a unique identifier that distinguishes one wireless network from another. Different SSID configurations exist to cater to specific network requirements:

- **Basic Service Set (BSS)**: A BSS represents a single access point (AP) and associated client devices.

- **Extended Service Set (ESS)**: An ESS consists of multiple APs interconnected to form a single logical network.

- **Independent Basic Service Set (Ad-hoc)**: Ad-hoc networks allow devices to establish direct connections without the need for an AP.

- **Roaming**: Roaming enables devices to seamlessly switch between APs within the same ESS without losing connectivity.

______

In conclusion, understanding wireless standards and technologies is vital for network professionals aiming to excel in the **CompTIA Network+ Certification Exam**. By exploring different 802.11 standards, frequencies, range, channel bonding, antenna types, encryption standards, and SSID configurations, individuals can build a strong foundation in wireless networking principles.

Remember to stay up to date with the latest advancements and government regulations related to wireless technologies, as they evolve rapidly. By mastering these concepts, you will be well-equipped to design, deploy, and troubleshoot wireless networks effectively.

## References

- [Federal Communications Commission (FCC)](https://www.fcc.gov/)
- [WiFi Alliance](https://www.wi-fi.org/)


## Progressive Lab Checkpoint 09: Wireless Standards

This checkpoint extends the [shared course topology](/network-plus-start/#progressive-n10-009-lab). Work inside an isolated simulator copy. Save `09-before` before changing state.

**Goal and tasks:** Place AP1 and a proposed second AP on a floor plan. Record SSID, BSSID, band, channel, width, security, antenna, and client type. Analyze six RSSI, noise, and SNR samples. Explain 802.11h, band steering, roaming, and autonomous versus lightweight APs. Separate PHY rate from measured throughput.

### Expected evidence

Save command output, packet data, counters, diagrams, or records which prove each task result. Compare observed evidence with the topology and address plan. Explain every mismatch before changing state.

### Fault injection and recovery

Put both APs on the same wide channel. Record contention risk, revise the plan, and save the corrected layout.

### Deliverable and pass gate

Submit **`09-wireless-channel-plan.md`** with purpose, affected nodes, risk, rollback, before evidence, fault evidence, recovery evidence, and cleanup statement.

**Pass:** The plan ties channel width, overlap, signal, noise, antenna, roaming, and security to measured evidence.

[Previous checkpoint](/network-plus/address-resolution-protocol-arp-neighbor-discovery-protocol-ndp/) | [Next checkpoint](/network-plus/network-plus-course-wireless-security-iot-access/)

### Primary references

- [CompTIA Network+ N10-009 exam objectives](https://comptiacdn.azureedge.net/webcontent/docs/default-source/exam-objectives/comptia-network-n10-009-exam-objectives-%284-0%29-%281%29.pdf?sfvrsn=f31cc6c4_4)
- [Topic source](https://standards.ieee.org/ieee/802.11/10548/)
