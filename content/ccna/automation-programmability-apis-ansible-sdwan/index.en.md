---
title: "Cisco CCNA (200-301): Automation and Programmability"
date: 2025-01-01
toc: true
draft: false
description: "Master automation and programmability for the Cisco CCNA 200-301 exam. Learn how automation impacts networks, controller-based architectures, REST APIs, configuration management, and JSON."
genre: ["Cisco CCNA Course", "Networking", "Network Automation", "Programmability", "SDN", "REST APIs", "Cisco Certification", "Infrastructure as Code", "DevNet", "IT Networking"]
tags: ["Cisco CCNA", "200-301", "automation", "programmability", "controller-based networking", "SDN", "overlay", "underlay", "fabric", "REST API", "CRUD", "Puppet", "Chef", "Ansible", "JSON", "Cisco DNA Center"]
cover: "/img/cover/cisco-ccna-automation-programmability-networking.webp"
coverAlt: "An illustration depicting a network diagram with interconnected nodes and abstract representations of APIs and configuration management tools, set against a dark background with vibrant colors."
coverCaption: "Master Automation and Programmability for the CCNA 200-301 Exam"
---

#### [Click Here to Return To the Cisco CCNA Course Page](/ccna-start/)

**Automation and Programmability** is **10%** of the **Cisco CCNA (200-301)** exam. This module covers how software-defined networking and automation change network management. *Modern networking careers increasingly expect these skills, so do not skip them.*

Automation reduces manual errors and speeds up changes across many devices. You learn how controllers, APIs, and configuration tools reshape the work.

## How Automation Changes Networks

Manual, box-by-box configuration is slow and easy to get wrong. **Automation** applies consistent changes at scale, enforces standards, and rolls back faster. The trade is an upfront investment in tooling and skills.

| Approach | Configuration | Scale |
|----------|---------------|-------|
| **Traditional** | Per-device CLI | Slow, error-prone |
| **Controller-based** | Central policy | Fast, consistent |

## Controller-Based and Software-Defined Networking

**Controller-based networking** splits the **control plane** from the **data plane**. The controller makes the decisions, and the devices forward traffic.

| Term | Meaning |
|------|---------|
| **Underlay** | Physical network of devices and links |
| **Overlay** | Virtual network built on top, such as VXLAN |
| **Fabric** | The combined underlay and overlay system |
| **Northbound API** | Controller to applications |
| **Southbound API** | Controller to network devices |

**Cisco DNA Center** manages a campus from one place, replacing per-device CLI with policy and automation.

## REST APIs

A **REST API** lets software configure and query devices over HTTP. It maps **CRUD** operations to HTTP verbs.

| CRUD | HTTP verb |
|------|-----------|
| Create | POST |
| Read | GET |
| Update | PUT or PATCH |
| Delete | DELETE |

A response code of 200 means success, while 401 means unauthorized and 404 means not found. Data is usually encoded in **JSON** or XML.

## JSON Data

**JSON** stores data as key-value pairs and arrays. You must recognize valid structure on the exam.

```javascript
{
  "device": "R1",
  "interfaces": ["g0/0", "g0/1"],
  "enabled": true,
  "ospf": { "process": 1, "area": 0 }
}
```

Keys are strings in quotes, values can be strings, numbers, booleans, arrays, or objects, and commas separate items.

## Configuration Management Tools

Three tools automate configuration at scale. Know their basic model.

| Tool | Model | Agent |
|------|-------|-------|
| **Ansible** | Push, procedural | Agentless (SSH) |
| **Puppet** | Pull, declarative | Agent-based |
| **Chef** | Pull, declarative | Agent-based |

**Ansible** is popular for network work because it is agentless and uses readable YAML playbooks. To learn it hands-on, read the [Ansible for beginners guide](/articles/ansible-for-beginners/).

## Next Steps

You have now covered all six CCNA domains. Reinforce the foundations in [Network Fundamentals](/ccna/network-fundamentals-osi-tcp-ip-switching/), practice automation with the [Ansible for beginners guide](/articles/ansible-for-beginners/), and test your readiness with the [Cisco CCNA Practice Test](/ccna-practice-test/). Explore more learning paths in [Courses and Playbooks](/courses-and-playbooks/) and return to the [Cisco CCNA Course](/ccna-start/).
