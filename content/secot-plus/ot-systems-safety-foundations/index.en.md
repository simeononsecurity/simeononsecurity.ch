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

**OT Systems and Safety Foundations** is **14%** of the **CompTIA SecOT+ (SOT-001)** exam. This domain establishes the language and safety mindset you need before you secure anything. In operational technology, a mistake can injure people or shut down critical infrastructure, so safety always comes before security. *Learn the components, the systems, and the protocols cold, because every later domain builds on this vocabulary.*

OT differs from IT in one fundamental way. IT protects data, while OT protects a physical process. Availability and safety outrank confidentiality, and a device may run for twenty years without a reboot.

## Safety First

You never touch OT equipment without controlling its hazards first.

| Practice | Purpose |
|----------|---------|
| **Lockout/tagout** | De-energizes and locks equipment so it cannot start during maintenance |
| **Job safety analysis** | Breaks a task into steps to identify and control hazards before work begins |
| **Personal protective equipment** | Protects workers with helmets, gloves, goggles, and similar gear |
| **Safety briefing** | Reviews hazards and controls before work starts |
| **Safety outbrief** | Reviews what happened and any safety issues after work ends |

*Safety is not a checkbox. A control change that looks trivial on a screen can move a real valve or motor, so you plan for the physical result every time.*

## OT Components

These are the building blocks of any control system.

- A **sensor** measures a physical property and reports it to the control system.
- An **actuator** converts a control signal into physical motion or action.
- A **controller** processes inputs and issues commands to actuators.
- A **programmable logic controller (PLC)** is a ruggedized industrial computer that automates machinery and processes.
- A **human-machine interface (HMI)** lets operators monitor and control a process.
- A **variable frequency drive** controls motor speed by varying supplied power frequency.
- An **intelligent electronic device** is a microprocessor controller used in power systems for protection and control.
- A **remote terminal unit** collects data and relays it to a SCADA system over distance.

## OT Systems

Components combine into larger systems.

| System | Role |
|--------|------|
| **SCADA** | Monitors and controls geographically distributed assets |
| **Distributed control system (DCS)** | Spreads controllers across a plant for continuous processes |
| **Safety instrumented system (SIS)** | Brings a process to a safe state when limits are exceeded |
| **Historian** | Records time-series process data |
| **Engineering workstation** | Configures and programs control system devices |
| **Manufacturing execution system** | Tracks and manages production on the plant floor |

*The safety instrumented system is special. It exists only to make the process safe, so it stays independent of the control system and is the last line of defense against a dangerous condition.*

## Control Logic and Programming

PLCs run logic you must recognize.

- **Ladder logic** is a graphical language that resembles relay control diagrams.
- A **function block diagram** connects function blocks with signal lines.
- **Structured text** is a high-level textual language similar to Pascal.
- A **process variable** is the measured value a controller tries to regulate.
- A **set point** is the target value the controller works to maintain.
- A **watchdog timer** resets or alarms a system that stops responding.

## OT Protocols

OT protocols were built for reliability and real-time behavior, not security. Most carry no authentication or encryption by default.

| Protocol | Use |
|----------|-----|
| **Modbus** | Simple serial or TCP protocol for industrial devices |
| **DNP3** | SCADA communications in utilities |
| **Profibus** | Fieldbus connecting controllers and field devices |
| **Profinet** | Industrial Ethernet for automation |
| **EtherCAT** | Real-time Ethernet fieldbus |
| **OPC UA** | Secure cross-platform industrial data exchange |
| **BACnet** | Building automation and control networks |

*OPC UA is the outlier because it was designed with security in mind. Legacy protocols like Modbus trust any device that can reach them, which is why segmentation matters so much in OT.*

## IT/OT Convergence

**IT/OT convergence** integrates information technology and operational technology networks and practices. It brings efficiency and visibility, but it also exposes fragile OT devices to IT-borne threats. Many OT devices run a **real-time operating system** for predictable timing or an **embedded operating system** with fixed functions, and they often cannot be patched on an IT schedule.

## Next Steps

With the foundations set, continue to [OT Risk Management](/secot-plus/ot-risk-management/) to learn how to assess and treat risk in these environments. Return anytime to the [CompTIA SecOT+ Course](/secot-plus-start/).
