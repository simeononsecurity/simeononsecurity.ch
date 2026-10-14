---
title: "Local AI Course: From First Model to Secure Server"
date: 2026-10-10
lastmod: 2026-10-14
toc: true
draft: false
description: "Run your first local model, measure fit and speed, then expose a controlled API through a secure server design."
genre: ["Artificial Intelligence", "Self-Hosted", "Cybersecurity"]
tags: ["local AI course", "Ollama course", "llama.cpp", "vLLM", "local LLM server", "secure AI server", "GGUF", "GPU inference", "self-hosted AI"]
cover: "/img/cover/local-ai-first-model-secure-server.webp"
coverAlt: "Learning path from a laptop model session to a monitored and access-controlled local AI server"
coverCaption: ""
---

**This course takes you from one local prompt to a reviewed server design.** You will select a model, prove local inference, measure memory and speed, bind a service safely, test access controls, and plan updates and recovery.

The course focuses on local inference and server operations. The [Practical AI Workflow Course](/effective-ai-course-start/) covers task packets, coding agents, context handoffs, and MCP workflow basics.

## Audience and Prerequisites

This course serves first-time local AI users, homelab operators, developers, and administrators.

You need:

- **One supported computer** with 8 GB or more system memory
- **20 GB of free storage** for software, one small model, and test records
- **Terminal access** and administrator rights for installation
- **No private dataset** during the course
- **A local firewall** available before any network exposure
- **Linux or macOS shell tools** for the course commands. On Windows, use WSL 2 with Python 3, curl, and `ss`, and run the model service and labs inside the same WSL environment. The PowerShell commands below only inventory the Windows host.

Model size and context length drive memory use. Start with a small model even on a large system. Prove the process before scaling.

## Choose Your Path

| Path | Goal | Tools | Completion target |
|---|---|---|---|
| **Beginner** | Run and evaluate one local model on one computer | Ollama CLI and local API | Loopback-only service with a measured prompt |
| **Advanced** | Tune and operate a multi-user service | Ollama, llama.cpp, or vLLM, service manager, proxy, metrics | Authenticated private service with rollback evidence |

Both paths complete the same security lab and quiz. Advanced callouts add build, concurrency, GPU offload, and operations work.

## Learning Outcomes

After the course, you will:

- **Inventory hardware** and select a model size with a stated memory margin
- **Verify model provenance** using publisher, license, source, digest, and local file records
- **Run local inference** through a CLI and loopback API
- **Measure prompt processing and generation speed** without mixing the two values
- **Tune context and concurrency** against observed memory use
- **Select a serving runtime** across Ollama, llama.cpp, and vLLM from workload, hardware, model format, and concurrency needs
- **Design secure access** with loopback binding, private routing, authentication, TLS, and rate limits
- **Operate updates and rollback** with version, model, configuration, and test evidence

## Course Order

| # | Lesson | Beginner output | Advanced output |
|---|---|---|---|
| **1** | [Choose Hardware and a Model](/local-ai-secure-server-course/01-hardware-model-fit/) | Fit worksheet | Capacity envelope |
| **2** | [Run Your First Local Model](/local-ai-secure-server-course/02-first-local-model/) | CLI and API proof | Service and artifact record |
| **3** | [Measure and Tune Inference](/local-ai-secure-server-course/03-measure-tune/) | Repeatable timing record | Context and concurrency profile |
| **4** | [Design a Secure Local AI Server](/local-ai-secure-server-course/04-secure-server/) | Loopback hardening plan | Private multi-user design |
| **5** | [Run the Secure Exposure Lab](/local-ai-secure-server-course/05-secure-exposure-lab/) | Local access tests | Proxy and boundary tests |
| **6** | [Check Your Knowledge](/local-ai-secure-server-course/06-knowledge-check/) | Quiz record | Quiz plus repair notes |
| **7** | [Complete the Server Capstone](/local-ai-secure-server-course/07-capstone/) | Single-user deployment package | Multi-user operations package |

Lesson 1 selects a model from published records. Lesson 2 installs Ollama before any `ollama` command runs.

Open the [knowledge-check answer key](/local-ai-secure-server-course/08-knowledge-check-answer-key/) after your closed-book attempt. Open the [capstone answer key](/local-ai-secure-server-course/09-capstone-answer-key/) after your deployment package and decision are complete.

## Completion Standard

Complete every lesson artifact before you claim course completion.

- **Quiz gate:** Score at least 8 out of 10 on a closed-book attempt. Answer security questions 4, 6, 8, 9, and 10 correctly. Repair every miss before starting the capstone.
- **Beginner capstone gate:** Submit all nine package files. Record the model source, license, identifier, three warm trials, a loopback-only listener, local firewall policy, and a tested prior-configuration rollback. Label remote denial `not run` when no second private client exists. Name an owner for each remaining condition.
- **Advanced capstone gate:** Submit all nine package files. Record the model digest, retained artifact, fixed evaluation set, context and concurrency profile, private gateway route, per-user authorization, protected metadata retention, and gateway denial evidence. The observed evidence must cover unauthorized, oversized, listener, timeout, and overload checks. Repeat the listener, health, and denial checks after rollback. Name an owner for each remaining condition.

## Shared Practice Record

Create **`local-ai-course-record.md`**. Add one section per lesson with commands, versions, expected results, observed results, and deviations. Never label an example result as observed.

Use synthetic prompts such as:

```text
List three checks for a backup restore test. Use fewer than 80 words.
```

Avoid customer data, credentials, internal source code, and regulated records while learning the service boundary.

## Expected Result

The beginner path ends with one model reachable only on the local machine and a record of actual memory and speed. The advanced path ends with a private service design, authenticated entry point, network rules, monitoring, update plan, and rollback test.

## Troubleshooting

- **Hardware details are unclear:** Record operating system, CPU, total RAM, GPU model, VRAM, and free disk space.
- **A model does not fit:** Reduce model size, quantization size, context, or concurrency.
- **The service listens on every interface:** Stop it, restore loopback binding, then review firewall and proxy design.
- **A result lacks a source:** Link the model card, runtime documentation, or local command output.

## Verify Your Setup

```bash
python3 --version
git --version
df -h .
```

On Linux, add:

```bash
free -h
lscpu | head
```

On macOS, add:

```bash
system_profiler SPHardwareDataType
```

On Windows PowerShell, add:

```powershell
Get-ComputerInfo | Select-Object OsName, OsVersion, CsTotalPhysicalMemory
Get-CimInstance Win32_VideoController | Select-Object Name
```

Record the observed values. Do not use `Win32_VideoController.AdapterRAM` as your VRAM capacity. Microsoft defines that field as a 32-bit byte value, so it cannot represent modern GPU memory above 4 GiB reliably. For an NVIDIA GPU, use `nvidia-smi --query-gpu=name,memory.total --format=csv`. For another GPU, use the vendor's current diagnostic tool and record its reported memory. Continue with [Lesson 1: Choose Hardware and a Model](/local-ai-secure-server-course/01-hardware-model-fit/).

Source: [Microsoft Win32_VideoController reference](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-videocontroller).
