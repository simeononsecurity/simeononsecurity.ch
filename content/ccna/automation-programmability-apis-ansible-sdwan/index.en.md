---
title: "Cisco CCNA (200-301): Automation and Programmability"
date: 2025-01-01
toc: true
draft: false
description: "Read local HTTP and JSON responses, review a CCNA v1.1 network change, and practice optional Ansible check mode without touching a live device."
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

## Lab 6: Read a Local API-Like Resource and Review a Change

The Packet Tracer topology does not expose a stable management REST API. Use a local read-only HTTP exercise to learn the request, response, JSON, and authentication boundary without implying that a network device changed. Save this synthetic file as `device.json` in a disposable folder:

```json
{"device":"R1","interface":"g0/1","admin_up":true,"errors":0}
```

From that folder, start `python3 -m http.server 8765 --bind 127.0.0.1`. In a second terminal run `curl -i http://127.0.0.1:8765/device.json`. You should see HTTP `200` and the JSON body. Run `curl -i http://127.0.0.1:8765/missing.json`; expect `404`. End the server with Ctrl+C. The local file server has no authentication and no write API. Never expose it to a network or mistake it for a Cisco controller. A `401` from a real API means missing or invalid authentication; stop and check authorized access instead of placing a token in a URL.

Parse the saved JSON with `python3 -c 'import json; d=json.load(open("device.json")); print(d["device"], d["errors"])'`. Expected output is `R1 0`. State what `admin_up` means in the example and what it does not prove. A saved response is a snapshot, not live interface evidence.

For a change-plan exercise, write a desired state `VLAN 20 GUEST` and compare it with the actual `show vlan brief` output from your saved Packet Tracer project. List the proposed add, any unrelated deletion, approval owner, rollback, and post-change command. Do not apply a suggested command until the planned device and port are in scope. After an authorized simulator change, run `show vlan brief` again and keep the before and after outputs.

If Ansible is installed, practice its check mode only against your own local test file. Save this as `local-plan.yml`:

```yaml
- name: Review a local VLAN note
  hosts: localhost
  connection: local
  gather_facts: false
  tasks:
    - name: Record the proposed VLAN
      ansible.builtin.copy:
        content: "VLAN 20 GUEST\n"
        dest: "{{ playbook_dir }}/vlan-plan.txt"
        mode: "0644"
```

Run `ansible-playbook -i localhost, local-plan.yml --check --diff`. Check mode reports the proposed change without writing the file. In a disposable folder, run the same command without `--check` to create the note, then run it again. The second run should report no change. Remove the note when done. This tests local file idempotence, not network-device idempotence. If Ansible is unavailable, mark that optional check `not run` and use the written change plan for the core checkpoint. See [Ansible's check and diff mode documentation](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_checkmode.html).

Your checkpoint is two HTTP statuses, parsed JSON output, a reviewed VLAN change plan, and the observed VLAN result. Pass when you distinguish a read response, a proposed configuration, an approved write, and a device read-back. Record which optional parts were not run. The [Cisco CCNA v1.1 topics](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf) define the exam scope.

## Next Steps

You have now covered all six CCNA domains. Reinforce the foundations in [Network Fundamentals](/ccna/network-fundamentals-osi-tcp-ip-switching/), practice automation with the [Ansible for beginners guide](/articles/ansible-for-beginners/), and test your readiness with the [Cisco CCNA Practice Test](/ccna-practice-test/). Explore more learning paths in [Courses and Playbooks](/courses-and-playbooks/) and return to the [Cisco CCNA Course](/ccna-start/).
