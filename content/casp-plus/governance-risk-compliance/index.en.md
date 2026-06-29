---
title: "CompTIA SecurityX (CAS-005): Governance, Risk, and Compliance"
date: 2025-01-01
toc: true
draft: false
description: "Master governance, risk, and compliance for the CompTIA SecurityX CAS-005 exam. Learn security program documentation, risk management, third-party risk, compliance frameworks, threat modeling, and AI security."
genre: ["CompTIA SecurityX Course", "Governance Risk Compliance", "Risk Management", "Compliance", "Threat Modeling", "Security Governance", "CASP+", "Enterprise Security", "AI Security", "Cybersecurity"]
tags: ["CompTIA SecurityX", "CASP+", "CAS-005", "governance", "risk management", "compliance", "COBIT", "ITIL", "PCI DSS", "ISO 27001", "SOC 2", "NIST CSF", "GDPR", "MITRE ATT&CK", "threat modeling", "AI security", "supply chain risk"]
cover: "/img/cover/comptia-securityx-governance-risk-compliance.webp"
coverAlt: "An illustration showing a cybersecurity governance framework with interconnected elements representing policies, risk management, compliance, and threat modeling on a dark background."
coverCaption: "Master Governance, Risk, and Compliance for the CAS-005 Exam"
---

#### [Click Here to Return To the CompTIA SecurityX Course Page](/casp-plus-start/)

**Governance, Risk, and Compliance** is **20%** of the **CompTIA SecurityX (CAS-005)** exam. This module covers how you set direction, measure risk, and prove compliance across a large enterprise. *SecurityX tests you as an architect who advises leadership, so think in terms of business risk, not single controls.*

Governance sets the rules. Risk management decides where to spend. Compliance proves you met your obligations. Together they turn security from a technical hobby into a business function leadership trusts and funds.

## Governance Components

You document the security program in a clear hierarchy so everyone knows what is required.

| Document | Binding? | Purpose |
|----------|----------|---------|
| **Policy** | Mandatory | High-level intent set by leadership |
| **Standard** | Mandatory | Specific, measurable requirements |
| **Procedure** | Mandatory | Step-by-step instructions |
| **Guideline** | Optional | Recommended best practice |

You align the program to a **governance framework** so it maps to recognized practice:

- **COBIT** governs and manages enterprise IT, linking IT goals to business goals.
- **ITIL** structures IT service management around the service lifecycle.

## Change and Configuration Management

You control changes so an "improvement" does not become an outage or a vulnerability. You track every asset through its **life cycle**: procurement, deployment, maintenance, and decommissioning.

A **Configuration Management Database (CMDB)** records each asset and its relationships, so you know what you have and what depends on it. Accurate **inventory** is the foundation of every other control. You cannot protect what you do not know exists.

## Risk Management Activities

You manage risk in a repeatable cycle: identify, assess, respond, and monitor. You measure impact two ways:

| Method | Uses | Strength |
|--------|------|----------|
| **Quantitative** | Dollar values (SLE, ARO, ALE) | Objective, supports cost-benefit math |
| **Qualitative** | Ratings like high/medium/low | Fast, captures hard-to-price risks |

The core quantitative formulas appear on the exam:

```text
SLE = Asset Value x Exposure Factor
ALE = SLE x ARO
```

*SLE* is the loss from one event. *ARO* is how often it happens per year. *ALE* is the expected annual loss, which you compare against the cost of a control. You then choose a **risk response**: mitigate, transfer, accept, or avoid. You prioritize the risks with the highest ALE and the lowest cost to fix.

## Third-Party Risk

Your security is only as strong as your weakest vendor. You assess risk across the whole chain:

- **Supply chain risk** covers tampering, counterfeits, and compromised software updates.
- **Vendor risk** covers a supplier's own security posture, validated with SOC 2 reports and questionnaires.
- **Subprocessor risk** covers the vendors your vendors use, often the hidden weak link.

You require a **software bill of materials (SBOM)** so you know every component in the software you buy.

## Compliance and Privacy

Compliance frameworks shape your security strategy because noncompliance carries fines and lost business.

| Framework | Applies to |
|-----------|-----------|
| **PCI DSS** | Payment card data |
| **ISO/IEC 27000 series** | Information security management systems |
| **SOC 2** | Service provider controls |
| **NIST CSF** | Risk-based cybersecurity framework |
| **CIS Controls** | Prioritized defensive actions |
| **Cloud Security Alliance** | Cloud-specific controls |

Privacy regulations add legal duties tied to personal data:

| Regulation | Region/Scope |
|-----------|--------------|
| **GDPR** | European Union |
| **CCPA** | California |
| **LGPD** | Brazil |
| **COPPA** | US children under 13 |

## Threat Modeling

You model threats to focus defense where attackers actually operate. Each framework structures the problem differently.

| Framework | Focus |
|-----------|-------|
| **MITRE ATT&CK** | Real adversary tactics and techniques |
| **CAPEC** | Catalog of attack patterns |
| **Cyber Kill Chain** | Stages of an intrusion |
| **Diamond Model** | Adversary, capability, infrastructure, victim |
| **STRIDE** | Spoofing, Tampering, Repudiation, Info disclosure, DoS, Elevation |
| **OWASP** | Web application risks |

## AI Security Challenges

SecurityX adds AI threats because attackers and defenders both use machine learning. You explain the main risks:

- **Prompt injection** manipulates an AI's instructions through crafted input.
- **Training data poisoning** corrupts a model by tampering with its training set.
- **Model theft** steals a proprietary model through repeated queries or extraction.
- **Model inversion** reconstructs sensitive training data from a model's outputs.
- **Deep fakes** generate convincing fake media for fraud and disinformation.

For a deeper look at how AI is reshaping defense, read [the state of AI in cybersecurity](/articles/state-of-ai-cybersecurity-2026/) and the critique of [AI governance certifications](/articles/ai-cybersecurity-governance-certifications-disappointing/).

## Next Steps

With governance and risk set, continue to [Security Architecture](/casp-plus/security-architecture/) to design resilient systems, then [Security Engineering](/casp-plus/security-engineering/) to build them. Return to the [CompTIA SecurityX Course](/casp-plus-start/) and review [tips for passing CompTIA exams](/articles/tips-and-tricks-for-passing-comptia-exams/).
