---
title: "Cisco CCNA (200-301): Automation and Programmability"
date: 2025-01-01
toc: true
draft: false
description: "Learn CCNA v1.1 automation, network AI, REST authentication, Ansible, Terraform, and JSON through a worked change review."
lastmod: 2026-10-10
genre: ["Cisco CCNA Course", "Networking", "Network Automation", "Programmability", "SDN", "REST APIs", "Cisco Certification", "Infrastructure as Code", "DevNet", "IT Networking"]
tags: ["Cisco CCNA", "200-301 v1.1", "network automation", "network AI", "machine learning", "REST API authentication", "Ansible", "Terraform", "JSON", "cloud managed networking"]
cover: "/img/cover/cisco-ccna-automation-programmability-networking.webp"
coverAlt: "An illustration depicting a network diagram with interconnected nodes and abstract representations of APIs and configuration management tools, set against a dark background with vibrant colors."
coverCaption: "Master Automation and Programmability for the CCNA 200-301 Exam"
---

[Click Here to Return To the Cisco CCNA Course Page](/ccna-start/)

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

**Cisco Catalyst Center** provides centralized campus management through policy and automation. Cloud-managed platforms such as Cisco Meraki offer a remote management plane. A device still forwards traffic according to its local capabilities and configuration when management connectivity changes. Compare the reach, credentials, and failure path of each management option before choosing one.

## AI and Machine Learning in Operations

**Predictive AI** learns patterns from past telemetry and flags unusual behavior or likely capacity problems. **Generative AI** produces summaries or candidate commands from a prompt. A network operator checks the source telemetry, device model, current configuration, and proposed diff before acting. A model's answer is not a live state check. Record the operator's approval and the post-change verification separately.

**Practice:** A monitoring tool flags a rise in interface errors. Predictive analysis identifies the pattern. A generative tool suggests changing duplex. First compare `show interfaces` output at both ends, then confirm negotiated speed and duplex. Change only after you identify the cause. Save the before and after counters.

## REST APIs

A **REST API** lets software configure and query devices over HTTP. It maps **CRUD** operations to HTTP verbs.

| CRUD | HTTP verb |
|------|-----------|
| Create | POST |
| Read | GET |
| Update | PUT or PATCH |
| Delete | DELETE |

A response code of 200 often means the request succeeded, while 401 means the request lacks valid authentication and 404 means the resource was not found. A 201 response often follows resource creation. The body often uses **JSON**. An API might use a bearer token, API key, or another authentication method. Send credentials through the service's documented secure method over HTTPS. Do not place tokens in URLs, examples, or version control. A successful HTTP response does not prove the requested network state changed. Read the resource back and verify the device.

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

Cisco v1.1 names Ansible and Terraform. Know the difference between applying device configuration and describing managed infrastructure.

| Tool | Model | Agent |
|------|-------|-------|
| **Ansible** | Runs tasks from playbooks, often over SSH or network APIs | Usually no agent on a network device |
| **Terraform** | Describes desired resources through providers and plans changes before applying them | Uses provider APIs and a state file |

**Ansible** is popular for network work because it is agentless and uses readable YAML playbooks. To learn it hands-on, read the [Ansible for beginners guide](/articles/ansible-for-beginners/).

## Worked Change Review

A team wants a new VLAN in a lab. Its proposed automation change declares VLAN 20, named `GUEST`, on two switches.

1. Record the intended devices, VLAN ID, name, and maintenance window.
2. Review the Ansible task or Terraform plan. Confirm both devices are in scope. Check for unrelated deletions.
3. Require a reviewer to approve the proposed change. Keep the plan or playbook revision with the approval.
4. Apply the change only in your lab. Run `show vlan brief` on both switches and compare the result with the intended state.
5. Record any mismatch, rollback action, and final state. A successful playbook run without device verification is incomplete evidence.

**Self-check:** Explain which part of the example is a desired-state description, which part is an API or device operation, and which observed output proves the VLAN exists. Passing work names all three and keeps credentials out of the saved record. Review the [Cisco v1.1 release notes](https://learningcontent.cisco.com/documents/marketing/exam-topics/CCNA_1_1_release_notes.pdf) to distinguish current objectives from older Puppet and Chef examples.

## Next Steps

You have now covered all six CCNA domains. Reinforce the foundations in [Network Fundamentals](/ccna/network-fundamentals-osi-tcp-ip-switching/), practice automation with the [Ansible for beginners guide](/articles/ansible-for-beginners/), and test your readiness with the [Cisco CCNA Practice Test](/ccna-practice-test/). Explore more learning paths in [Courses and Playbooks](/courses-and-playbooks/) and return to the [Cisco CCNA Course](/ccna-start/).
