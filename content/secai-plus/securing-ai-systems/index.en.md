---
title: "CompTIA SecAI+ (CY0-001): Securing AI Systems"
date: 2025-01-01
toc: true
draft: false
description: "Master securing AI systems for the CompTIA SecAI+ CY0-001 exam. Learn AI security frameworks, access controls, data protection, runtime guardrails, monitoring, and defenses against adversarial attacks like prompt injection and model poisoning."
genre: ["CompTIA SecAI+ Course", "Securing AI Systems", "Adversarial Machine Learning", "LLM Security", "AI Threats", "MITRE ATLAS", "OWASP", "AI Security", "CY0-001", "Cybersecurity"]
tags: ["CompTIA SecAI+", "CY0-001", "OWASP LLM Top 10", "MITRE ATLAS", "prompt injection", "jailbreaking", "model poisoning", "data poisoning", "backdoor attack", "model inversion", "model theft", "membership inference", "model guardrails", "prompt firewall", "AI supply chain", "excessive agency"]
cover: "/img/cover/comptia-secai-plus-securing-ai-systems.webp"
coverAlt: "An illustration of a secure AI system with layers of protection around an AI model, featuring visual elements like encryption, access control, and monitoring systems, set against a dark background."
coverCaption: "Defend AI Systems Against Adversarial Attacks for the CY0-001 Exam"
---

#### [Click Here to Return To the CompTIA SecAI+ Course Page](/secai-plus-start/)

**Securing AI Systems** is **40%** of the **CompTIA SecAI+ (CY0-001)** exam, making it the most heavily weighted domain by far. This module covers how you protect models, their data, and the applications around them from a new class of adversarial attacks. *Spend the bulk of your study time here. Master the threat names and the control that stops each one.*

AI systems expand the attack surface. The model, the training data, the prompts, the outputs, and the agents that act on those outputs are all targets. You defend each layer with controls built for AI, not just the network controls you already know.

## AI Security Frameworks

You do not invent AI risk from scratch. You map your defenses to published frameworks.

| Framework | What it provides |
|-----------|------------------|
| **OWASP LLM Top 10** | The most critical security risks for LLM applications |
| **OWASP ML Security Top 10** | The top risks for machine learning systems |
| **MITRE ATLAS** | Adversary tactics and techniques against AI systems |
| **MIT AI Risk Repository** | A catalog of documented AI risks |
| **CVE AI Working Group** | An effort to standardize how AI vulnerabilities are catalogued |

*MITRE ATLAS mirrors ATT&CK but for AI, so the tactics-and-techniques mindset you already have transfers directly.*

## Access Control for AI

You restrict who and what can reach each part of the system. The objective lists five distinct surfaces:

- **Endpoint access control** restricts which clients can reach an AI service endpoint.
- **Model access control** restricts who may query, modify, or download a model.
- **Data access control** restricts who may read or change the data a model uses.
- **Agent access control** restricts what actions an autonomous agent may perform.
- **API access control** authenticates and restricts calls to an AI application interface.

## Data Protection

You protect data in all three states and reduce how much sensitive data the model ever sees.

| State | Control |
|-------|---------|
| **In transit** | Encryption while data moves across a network |
| **At rest** | Encryption for stored data |
| **In use** | Encryption while data is being processed |

You also de-risk the data itself:

- **Anonymization** removes identifiers so data cannot be linked to a person.
- **Redaction** permanently removes sensitive content.
- **Masking** hides sensitive values with substitute characters while preserving format.
- **Minimization** collects and keeps only the data that is strictly needed.
- A **data classification label** tags data by its sensitivity level.

## Runtime Guardrails

You wrap the live model in controls that bound what it accepts and produces:

- **Model guardrails** keep outputs within safe boundaries.
- A **prompt firewall** inspects and filters prompts before they reach the model.
- **Rate limiting** caps how many requests a client may send in a time window.
- A **token limit** caps the tokens allowed per request or response.
- An **input quota** limits the size or quantity of data a client may submit.
- A **modality limit** restricts which input types such as text, image, or audio are accepted.

## Monitoring and Cost Control

You watch the system continuously and protect the evidence it produces:

- **Prompt monitoring** inspects queries and responses for abuse or policy violations.
- **Log sanitization** strips sensitive data from logs before storage.
- **Log protection** secures logs against tampering and unauthorized access.
- A **response confidence level** reflects how certain the model is about an answer, which helps catch a **hallucination**, a confident but false output.
- **AI cost monitoring** tracks spend on prompts, storage, processing, and responses so a model denial-of-service attack does not run up a huge bill unnoticed.
- **Bias and fairness auditing** reviews outputs for unfair or discriminatory behavior.

## Adversarial Attacks

This is the heart of the domain. You must recognize each attack and the layer it targets.

| Attack | What the attacker does |
|--------|------------------------|
| **Prompt injection** | Crafts input that overrides the model's intended instructions |
| **Jailbreaking** | Bypasses safety guardrails to elicit prohibited output |
| **Data poisoning** | Corrupts training data to bias or sabotage the model |
| **Model poisoning** | Tampers with model parameters or training to corrupt behavior |
| **Backdoor attack** | Hides a trigger that produces attacker-chosen behavior |
| **Trojan attack** | Embeds malicious behavior inside an otherwise normal model |
| **Model inversion** | Reconstructs sensitive training data from model outputs |
| **Model theft** | Extracts or copies a proprietary model through repeated queries |
| **Membership inference** | Determines whether a specific record was in the training data |
| **AI supply chain attack** | Compromises third-party models, datasets, or libraries |

## Application-Layer Risks

The application around the model adds its own risks:

- **Insecure output handling** trusts model output without validation, enabling downstream attacks such as cross-site scripting or command injection.
- **Excessive agency** grants an agent more autonomy or permissions than it needs.
- **Model denial of service** overloads a model with costly requests to exhaust resources.

*Treat every model output as untrusted input to the next system. That single habit closes a large share of LLM application vulnerabilities.*

## Next Steps

With AI systems defended, continue to [AI-assisted Security](/secai-plus/ai-assisted-security/) to turn AI into a defensive tool, then [AI Governance, Risk, and Compliance](/secai-plus/ai-governance-risk-compliance/) to manage it responsibly. Review the foundations in [Basic AI Concepts](/secai-plus/basic-ai-concepts/) and return to the [CompTIA SecAI+ Course](/secai-plus-start/).
