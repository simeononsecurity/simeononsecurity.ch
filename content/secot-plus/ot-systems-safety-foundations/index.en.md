---
title: "CompTIA SecOT+ (SOT-001): OT Systems and Safety Foundations"
date: 2025-01-01
toc: true
draft: false
description: "Master OT systems and safety foundations for the CompTIA SecOT+ SOT-001 exam. Learn safety procedures, OT components like PLCs and HMIs, control systems such as SCADA and DCS, control logic, and industrial protocols including Modbus and DNP3."
genre: ["CompTIA SecOT+ Course", "OT Systems", "Safety Foundations", "Industrial Control Systems", "SCADA", "PLC", "Industrial Protocols", "Operational Technology", "SOT-001", "Cybersecurity"]
tags: ["CompTIA SecOT+", "SOT-001", "lockout tagout", "job safety analysis", "PLC", "HMI", "SCADA", "DCS", "safety instrumented system", "historian", "ladder logic", "Modbus", "DNP3", "Profibus", "OPC UA", "IT/OT convergence", "remote terminal unit"]
cover: "/img/cover/comptia-secot-ot-systems-safety-foundations.webp"
coverAlt: "An illustration of a control room with a large human-machine interface displaying data. Surrounding elements represent sensors, actuators, and PLCs, all set against a dark background with vibrant colors."
coverCaption: "Build a Safety-First Foundation in OT Systems for the SOT-001 Exam"
---

#### [Click Here to Return To the CompTIA SecOT+ Course Page](/secot-plus-start/)

**OT Systems and Safety Foundations** is **14%** of the **CompTIA SecOT+ (SOT-001)** exam. This domain establishes the language and safety mindset you need before you secure anything. In operational technology, a mistake can injure people or shut down critical infrastructure, so safety always comes before security. *Learn the components, the systems, the control logic, and the protocols cold, because every later domain builds on this vocabulary.*

**Operational technology (OT)** is hardware and software that monitors and controls physical processes, devices, and infrastructure. OT differs from IT in one fundamental way. IT protects data, while OT protects a physical process. Availability and safety outrank confidentiality, and a single device may run for twenty years without a reboot.

## Safety First

You never touch OT equipment without controlling its hazards first. A control change that looks trivial on a screen can move a real valve or motor, so you plan for the physical result every time.

| Practice | Purpose |
|----------|---------|
| **Lockout/tagout (LOTO)** | De-energizes and locks equipment with a physical lock and a warning tag so it cannot start during maintenance |
| **Job safety analysis (JSA)** | Breaks a task into steps to identify and control hazards before work begins |
| **Personal protective equipment (PPE)** | Protects workers with helmets, gloves, goggles, hearing protection, and similar gear |
| **Safety briefing** | Reviews hazards and controls in a meeting before work starts |
| **Safety outbrief** | Reviews what happened and any safety issues in a meeting after work ends |

*Safety is not a checkbox. It is the first thing the exam expects you to consider before any maintenance or security task.*

You must also recognize the **hazards** present in industrial spaces and the **industrial ratings** that tell you whether a device or tool is safe to use in a given area.

- **Electrical** hazards include shock, arc flash, and electrocution from energized conductors.
- **Pressure** hazards come from compressed gas, steam, and hydraulic systems that can rupture.
- **Heights** introduce fall hazards on towers, tanks, and elevated platforms.
- **Temperature** hazards include burns from hot surfaces and frostbite from cryogenic lines.
- **Fire** and explosion hazards exist where fuel, dust, or vapor can ignite.
- **Chemical** hazards include corrosive, toxic, and reactive substances.
- **Water** hazards include drowning, slips, and electrical danger near wet areas.

*Industrial ratings such as hazardous-area and ingress-protection markings tell you if equipment can operate safely in an explosive, wet, or dusty zone. Never bring an unrated device into a rated area.*

## OT Components and Field Devices

These are the building blocks of any control system. The exam expects you to identify each one by what it does.

- A **sensor** measures a physical property such as temperature, pressure, or flow and reports it to the control system.
- An **actuator** converts a control signal into physical motion or action, such as opening a valve.
- A **controller** processes inputs and issues commands to actuators.
- A **programmable logic controller (PLC)** is a ruggedized industrial computer that automates machinery and processes.
- A **human-machine interface (HMI)** lets operators monitor and control a process from a screen.
- A **variable frequency drive (VFD)** controls motor speed by varying the frequency of the supplied power.
- A **relay** is an electrically operated switch that opens or closes a circuit.
- An **intelligent electronic device (IED)** is a microprocessor controller used in power systems for protection and control.
- A **remote terminal unit (RTU)** collects field data and relays it to a SCADA system over distance.
- An **engineering workstation** configures, programs, and maintains control system devices.
- An **operator workstation** is the station an operator uses to run and watch the process.
- A **historian** records time-series process data for trending and analysis.
- A **transient or portable device** is a laptop, tablet, or USB tool that connects to OT only temporarily and is a common infection path.

## Industrial Control Systems

Components combine into larger **industrial control systems (ICS)** that run a plant, a utility, or a pipeline.

| System | Role |
|--------|------|
| **SCADA** | Supervisory control and data acquisition that monitors and controls geographically distributed assets |
| **Distributed control system (DCS)** | Spreads controllers across a plant to run continuous processes locally |
| **Localized control network** | A control network confined to a single area, line, or machine |
| **Safety instrumented system (SIS)** | Brings a process to a safe state when limits are exceeded |
| **Manufacturing execution system (MES)** | Tracks and manages production on the plant floor and bridges to business systems |
| **Stand-alone system** | A control system that runs in isolation without network connectivity |

*The safety instrumented system is special. It exists only to make the process safe, so it stays independent of the basic control system and is the last line of defense against a dangerous condition.*

OT secures the systems that run **critical infrastructure**. These sectors include energy, water and wastewater, oil and gas, manufacturing, transportation, chemical, and food and agriculture. A failure in any of them can affect public safety and national security, which is why the exam ties OT security to consequences beyond a single company.

The **IT and OT roles** differ in what they protect and how they prioritize. The table below frames the contrast the exam tests.

| Dimension | IT | OT |
|-----------|----|----|
| **Top priority** | Confidentiality of data | Safety and availability of the process |
| **Uptime** | Reboots and patches are routine | Systems run for years and rarely stop |
| **Lifespan** | Three to five years | Fifteen to thirty years |
| **Patching** | Frequent and scheduled | Rare, tested, and often deferred |

## Control Logic and Programming

PLCs run logic you must recognize on sight. The exam names four IEC 61131-3 languages plus the runtime values a controller tracks.

- **Ladder logic** is a graphical language that resembles relay control diagrams and reads like rungs on a ladder.
- A **function block diagram** connects reusable function blocks with signal lines.
- **Structured text** is a high-level textual language similar to Pascal.
- A **sequential function chart** breaks a process into ordered steps and transitions.

The runtime values below are what the logic reads and writes while the process runs.

| Term | Meaning |
|------|---------|
| **Process variable** | The measured value the controller tries to regulate |
| **Set point** | The target value the controller works to maintain |
| **Current value** | The live reading of a process variable right now |
| **Input/output (I/O)** | The wired or networked points that read sensors and drive actuators |
| **Tag** | A named reference to a memory location or data point in the controller |
| **Timer** | A logic element that counts time to delay or sequence an action |
| **Watchdog** | A timer that resets or alarms a system that stops responding |

## OT Protocols

OT protocols were built for reliability and real-time behavior, not security. Most carry no authentication or encryption by default, so any device that can reach them is trusted. The exam groups protocols by their transport.

**Serial protocols** run over older point-to-point and multidrop wiring.

| Serial Protocol | Use |
|-----------------|-----|
| **RS-232 / RS-485** | Physical serial standards for point-to-point and multidrop links |
| **Modbus RTU** | Simple serial protocol for polling industrial devices |
| **Profibus** | Fieldbus connecting controllers and field devices |
| **Data Highway Plus** | Legacy Allen-Bradley peer-to-peer control network |
| **DNP3** | SCADA communications common in electric and water utilities |

**Ethernet protocols** carry control traffic over industrial Ethernet.

| Ethernet Protocol | Use |
|-------------------|-----|
| **Modbus TCP** | Modbus framed over Ethernet |
| **EtherNet/IP (CIP)** | Common Industrial Protocol over Ethernet, common in factories |
| **EtherCAT** | Real-time Ethernet fieldbus for fast motion control |
| **Profinet** | Industrial Ethernet for automation |
| **OPC DA / OPC UA** | Cross-platform industrial data exchange, with OPC UA adding security |
| **BACnet / KNX** | Building automation and control networks |

**Wireless protocols** connect remote, mobile, or hard-to-wire assets.

| Wireless Protocol | Use |
|-------------------|-----|
| **VHF** | Very high frequency radio for voice and telemetry over distance |
| **AIS** | Automatic identification system for vessel tracking |
| **VSAT** | Very small aperture terminal satellite links for remote sites |
| **M-Bus** | Meter-bus for reading utility meters |
| **802.15.4** | Low-rate wireless for sensor networks such as Zigbee |
| **802.11** | Wi-Fi for plant and field connectivity |

*OPC UA is the outlier because it was designed with security in mind. Legacy protocols like Modbus and DNP3 trust any device that can reach them, which is why segmentation matters so much in OT.*

## Legacy and Modern Infrastructure

OT environments mix decades-old gear with new cloud-connected platforms, and the exam asks you to compare the two. **Legacy infrastructure** is purpose-built and hard to change, while **modern infrastructure** is virtualized, software-defined, and often cloud-connected.

| Aspect | Legacy Infrastructure | Modern Infrastructure |
|--------|-----------------------|------------------------|
| **Operating system** | Embedded, custom, or real-time operating system (RTOS) | Commodity operating systems on virtual machines and containers |
| **Hardware** | Fixed-function, single-purpose controllers | General-purpose servers and edge compute |
| **Protocols** | Proprietary serial fieldbus with no security | Routable, sometimes encrypted protocols |
| **Physical ports** | Exposed serial and parallel ports | Managed USB and network ports |
| **Applications** | Vendor-locked, rarely updated | Modular, frequently updated software |

Modern OT borrows heavily from IT. You should know these building blocks.

- **Virtualization** runs control software on **virtual machines** managed by a **hypervisor**, with **virtual switching**, **virtual PLCs**, and **containers** replacing some physical hardware.
- **Software-defined networking (SDN)** controls network behavior in software instead of fixed hardware configuration.
- **Middleware** connects applications and systems that were never designed to talk to each other.
- **AI, ML, and generative AI** capabilities now assist with anomaly detection, optimization, and operator support.
- **Cloud** models include **public**, **private**, **hybrid**, **edge**, and **vendor-managed** deployments that extend OT beyond the plant.
- A **privatized backbone** is a dedicated private network that carries critical traffic instead of the public internet.
- **Autonomous systems** make and act on decisions with little or no human input.

*Modern features add efficiency and visibility, but every new connection is a new path for an attacker. Map the convergence before you trust it.*

## IT/OT Convergence

**IT/OT convergence** integrates information technology and operational technology networks and practices. It brings efficiency and remote visibility, but it also exposes fragile OT devices to IT-borne threats. Many OT devices run a **real-time operating system** for predictable timing or an **embedded operating system** with fixed functions, and they often cannot be patched on an IT schedule. That gap between IT expectations and OT reality is the tension you will manage for the rest of this course.

## Next Steps

With the foundations set, continue to [OT Risk Management](/secot-plus/ot-risk-management/) to learn how to assess and treat risk in these environments. Return anytime to the [CompTIA SecOT+ Course](/secot-plus-start/).
