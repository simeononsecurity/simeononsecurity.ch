---
title: "CEH v13: IoT and OT Hacking"
date: 2025-01-01
toc: true
draft: false
description: "Master IoT and OT hacking for the EC-Council Certified Ethical Hacker (CEH v13) exam. Learn IoT enumeration with Shodan, SCADA and ICS architecture, Modbus, DNP3, default credentials, and OT defenses."
genre: ["EC-Council CEH Course", "Ethical Hacking", "Penetration Testing", "Offensive Security", "Cybersecurity", "Network Security", "Security Testing", "Hacking Techniques", "CEH Certification", "Information Security"]
tags: ["CEH", "CEH v13", "ethical hacking", "EC-Council", "penetration testing", "iot and ot hacking", "offensive security", "cybersecurity", "hacking", "security testing"]
cover: "/img/cover/iot-ot-hacking-security-illustration.webp"
coverAlt: "An illustration showing various interconnected IoT devices and industrial systems like smart home gadgets and SCADA interfaces, representing vulnerabilities in cybersecurity."
coverCaption: "Master IoT and OT Hacking for the CEH v13 Exam"
---

#### [Click Here to Return To the Certified Ethical Hacker (CEH v13) Course Page](/ceh-start/)

**IoT and OT Hacking** targets connected devices and industrial systems in the **EC-Council CEH v13** course. This module covers IoT enumeration, operational technology weaknesses, industrial protocols, and the defenses that protect critical infrastructure. *Never probe live OT or industrial systems without written authorization, because a failed scan can stop a production line or endanger lives.*

IoT devices and operational technology often run legacy, unpatched software with weak defaults. The impact of an attack ranges from a hijacked camera to a disrupted power grid.

## IoT Attack Surface

Most IoT weaknesses follow the **OWASP IoT Top 10**. Devices ship with predictable credentials and expose management interfaces to the internet.

- **Default credentials** like `admin/admin` stay unchanged in the field.
- **Insecure firmware** ships without signing or update support.
- **Unencrypted communication** leaks credentials and telemetry.
- **Exposed interfaces** put web, Telnet, and UPnP services on public IPs.

You find exposed devices with **Shodan**, which indexes internet-facing services and banners.

```text
# Shodan search filters for exposed devices
port:23 default password
product:"IP camera" country:US
"Server: gSOAP"
```

Try the [Shodan IP lookup tool](/shodan_ip/) to see what an address exposes.

## OT, ICS, and SCADA

Operational technology runs physical processes. The CEH exam expects you to know the core terms.

| Term | Role |
|------|------|
| **OT** | Hardware and software that controls physical processes |
| **ICS** | Industrial control systems that run automation |
| **SCADA** | Supervisory control and data acquisition for remote sites |
| **PLC** | Programmable logic controller that drives equipment |

The **Purdue Model** layers OT networks from field devices up to enterprise IT. Attackers who cross from IT into OT can reach the control layer.

## Industrial Protocols

Industrial protocols were built for reliability, not security. Most send commands without authentication or encryption.

| Protocol | Weakness |
|----------|----------|
| **Modbus** | No authentication, plaintext commands |
| **DNP3** | Limited authentication in legacy deployments |
| **Profinet** | Exposed to spoofing and replay |

An attacker who reaches a Modbus network can read and write register values directly, which changes how equipment behaves.

*OT cybersecurity is fundamentally fragile, and you can read why in [this analysis of broken ICS and PLC security](/articles/ot-ics-plc-cybersecurity-fundamentally-broken/).*

## OT and IoT Defense

| Control | Purpose |
|---------|---------|
| **Network segmentation** | Separates OT from IT and the internet |
| **Firmware hardening** | Removes default accounts and signs updates |
| **OT monitoring** | Detects abnormal commands and traffic |
| **Strong credentials** | Replaces default passwords on every device |

Segmentation is the single most effective control, since it keeps a compromised IT host away from the control layer.

## Next Steps

Continue with [Cloud Computing Threats](/ceh/cloud-computing-threats/). Review the previous module on [Hacking Mobile Platforms](/ceh/hacking-mobile-platforms/), read more on [broken OT and ICS security](/articles/ot-ics-plc-cybersecurity-fundamentally-broken/), and test exposure with the [Shodan IP lookup](/shodan_ip/). Return to the [Certified Ethical Hacker (CEH v13) Course](/ceh-start/).
