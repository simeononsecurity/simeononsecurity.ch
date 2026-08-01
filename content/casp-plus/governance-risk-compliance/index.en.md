---
title: "CompTIA SecurityX (CAS-005)"
date: 2025-01-01
toc: true
draft: false
description: "Master governance, risk, and compliance for the CompTIA SecurityX CAS-005 exam. Learn security program documentation, risk management, third-party risk, compliance frameworks, privacy regulations, threat modeling, and AI security challenges."
genre: ["CompTIA SecurityX Course", "Governance Risk Compliance", "Risk Management", "Compliance", "Threat Modeling", "Security Governance", "CASP+", "Enterprise Security", "AI Security", "Cybersecurity"]
tags: ["CompTIA SecurityX", "CASP+", "CAS-005", "governance", "risk management", "compliance", "COBIT", "ITIL", "PCI DSS", "ISO 27001", "SOC 2", "NIST CSF", "CIS Controls", "GDPR", "CCPA", "MITRE ATT&CK", "STRIDE", "threat modeling", "AI security", "supply chain risk", "BIA", "ALE", "CMMC", "privacy engineering"]
cover: "/img/cover/comptia-securityx-governance-risk-compliance.webp"
coverAlt: "An illustration showing a cybersecurity governance framework with interconnected elements representing policies, risk management, compliance, and threat modeling on a dark background."
coverCaption: "Master Governance, Risk, and Compliance for the CAS-005 Exam"
---

#### [Click Here to Return To the CompTIA SecurityX Course Page](/casp-plus-start/)

**Governance, Risk, and Compliance** is **20%** of the **CompTIA SecurityX (CAS-005)** exam. This domain covers how you set direction, measure risk, and prove your program meets legal and contractual obligations across a large enterprise. *SecurityX tests you as an architect who advises leadership, so think in terms of business risk and organizational outcomes, not individual controls.*

Governance sets the rules. Risk management decides where to invest. Compliance proves you met your obligations. Together they turn security from a technical hobby into a business function leadership trusts and funds.

## Governance Components

Security programs need a documented hierarchy so every employee knows what is required and why.

| Document | Binding? | Changed by | Example |
|----------|----------|------------|---------|
| **Policy** | Mandatory | Senior leadership | Acceptable Use Policy |
| **Standard** | Mandatory | Security team | Password complexity requirement |
| **Procedure** | Mandatory | Operations | Step-by-step patch process |
| **Guideline** | Optional | Security team | Recommended browser settings |

Policies state intent. Standards make it measurable. Procedures tell people exactly what to do. Guidelines offer flexibility when a prescriptive standard would cause more harm than good.

You align the program to a recognized **governance framework** to demonstrate maturity:

- **COBIT** (Control Objectives for Information and Related Technologies) links IT goals to business goals through governance and management objectives.
- **ITIL** (IT Infrastructure Library) organizes IT service management around a service lifecycle, emphasizing continual improvement.

### Security Program Maturity

Maturity models let you measure how repeatable and optimized your program is:

| Model | Used for |
|-------|----------|
| **CMMC** | Defense industrial base contractors, DoD supply chain |
| **SSE-CMM** | Systems security engineering processes |
| **NIST CSF Tiers** | Cybersecurity risk management sophistication (1–4) |

*On the exam, recognize that a Tier 1 (Partial) organization acts ad hoc while a Tier 4 (Adaptive) organization integrates threat intelligence into real-time decisions.*

## Change and Configuration Management

Unauthorized changes create vulnerabilities. You control changes through a formal process: request, approve, test, implement, and verify.

A **Configuration Management Database (CMDB)** records every asset and its relationships. It answers: "If I patch this server, what else breaks?" An accurate **inventory** is the foundation of every other control. You cannot protect what you do not know exists.

The **asset management life cycle** follows the asset from procurement through deployment, maintenance, and secure decommissioning. End-of-life assets without a disposal plan become unpatched attack surface.

## Risk Management Activities

Risk management is a repeatable cycle: identify, assess, respond, and monitor. You measure risk two ways depending on data availability:

| Method | Uses | Strength |
|--------|------|----------|
| **Quantitative** | Dollar values (SLE, ARO, ALE) | Objective, supports cost-benefit analysis |
| **Qualitative** | Ratings like high/medium/low | Fast, works when data is unavailable |

The core quantitative formulas the exam tests:

```text
SLE  = Asset Value × Exposure Factor
ALE  = SLE × ARO
```

**SLE** (Single Loss Expectancy) is the loss from one event. **ARO** (Annualized Rate of Occurrence) is how often it happens per year. **ALE** (Annualized Loss Expectancy) is the expected annual loss — you compare it against the annualized cost of a control. If a control costs less than the ALE it eliminates, it pays for itself.

### Risk Responses

After calculating ALE, you choose one of four responses:

- **Mitigate** — implement a control to reduce impact or likelihood.
- **Transfer** — shift risk to another party through insurance or contracts.
- **Accept** — document the risk and choose not to act, often because the cost to fix exceeds the ALE.
- **Avoid** — eliminate the activity that creates the risk entirely.

*Avoid is the strongest response but often the least practical. Every response except avoid leaves residual risk you must still monitor.*

### Business Impact Analysis

A **Business Impact Analysis (BIA)** identifies critical processes and quantifies what downtime costs. Key outputs:

- **RTO** (Recovery Time Objective) — maximum tolerable downtime before business impact becomes unacceptable.
- **RPO** (Recovery Point Objective) — maximum acceptable data loss measured in time.
- **MTBF** (Mean Time Between Failures) — average uptime between failures; higher is better.
- **MTTR** (Mean Time to Repair) — average time to restore service after failure; lower is better.

The BIA feeds directly into [Security Architecture](/casp-plus/security-architecture/) decisions about redundancy and recovery design.

## Third-Party Risk

Your security posture equals the security of your weakest link, which is often a vendor. You assess third-party risk across the whole chain:

- **Supply chain risk** covers tampering, counterfeits, and compromised software updates inserted before the product reaches you.
- **Vendor risk** covers a supplier's own security posture. You validate it with SOC 2 Type II reports, questionnaires, and right-to-audit clauses.
- **Subprocessor risk** covers the vendors your vendors use — often the hidden weak link in large SaaS platforms.

You require a **Software Bill of Materials (SBOM)** so you know every third-party component inside software you buy or deploy. An SBOM makes it possible to respond quickly when a new CVE hits a transitive dependency.

| Third-Party Assessment Method | What it tells you |
|-------------------------------|-------------------|
| **SOC 2 Type I** | Controls exist at a point in time |
| **SOC 2 Type II** | Controls operated effectively over a period (6–12 months) |
| **Questionnaire / SIG** | Self-reported posture — use as a starting point only |
| **Penetration test report** | Technical verification of claimed controls |
| **Right to audit** | Contractual ability to verify posture yourself |

*SOC 2 Type II is far more valuable than Type I because it proves sustained operation, not just design.*

## Compliance Frameworks and Regulations

Compliance frameworks shape your security strategy because noncompliance carries fines, lost contracts, and reputational harm.

| Framework | Scope | Key Requirement |
|-----------|-------|-----------------|
| **PCI DSS** | Payment card data | 12 requirements around card data protection |
| **ISO/IEC 27001** | Information security management | ISMS with formal risk treatment |
| **ISO/IEC 27002** | Controls guidance for 27001 | 93 controls across 4 themes |
| **SOC 2** | Service provider controls | Trust Service Criteria: security, availability, confidentiality |
| **NIST CSF** | Voluntary risk framework | Five functions: Identify, Protect, Detect, Respond, Recover |
| **CIS Controls v8** | Prioritized defensive actions | 18 controls organized by implementation group |
| **CSA CCM** | Cloud services | Cloud-specific controls mapped to ISO and NIST |

### Privacy Regulations

Privacy regulations add legal duties tied to personal data collection and processing:

| Regulation | Region | Key Requirement |
|-----------|--------|-----------------|
| **GDPR** | European Union | Lawful basis for processing; right to erasure; 72-hour breach notification |
| **CCPA / CPRA** | California | Right to know, delete, and opt out of data sale |
| **LGPD** | Brazil | Similar to GDPR; DPA, legal basis, data subject rights |
| **COPPA** | United States | Parental consent required for children under 13 |
| **HIPAA** | United States | Protected Health Information (PHI) safeguards |

*The exam may ask you to apply GDPR's right to erasure or COPPA's age verification in a scenario. Focus on what each regulation requires of the organization.*

### Audit Types

Understanding audit types helps you advise leadership on evidence preparation:

- **Attestation** — an independent auditor confirms controls work (SOC 2 reports).
- **Examination** — deep independent review of specific assertions.
- **Agreed-upon procedures (AUP)** — auditor performs procedures both parties agree on; no opinion issued.
- **Internal audit** — conducted by the organization's own audit function; less independence.

## Threat Modeling

Threat modeling focuses defense where attackers actually operate. You pick the model that fits the question being asked.

| Framework | What it answers |
|-----------|----------------|
| **MITRE ATT&CK** | What real adversary TTPs look like, mapped to detection and response |
| **CAPEC** | Common attack patterns against software and systems |
| **Cyber Kill Chain** | Stages of an intrusion from reconnaissance to actions on objectives |
| **Diamond Model** | Relationships between adversary, capability, infrastructure, and victim |
| **STRIDE** | Six threat categories against a component or data flow |
| **OWASP Top 10** | Most critical web application security risks |
| **PASTA** | Process for Attack Simulation and Threat Analysis — risk-centric, attacker-focused |

### STRIDE in Practice

**STRIDE** is the most commonly tested threat-modeling method because it maps neatly to countermeasures:

| Threat | Countermeasure |
|--------|----------------|
| **Spoofing** | Authentication |
| **Tampering** | Integrity controls, signing |
| **Repudiation** | Audit logging and non-repudiation |
| **Information Disclosure** | Encryption and access control |
| **Denial of Service** | Availability controls, rate limiting |
| **Elevation of Privilege** | Least privilege, authorization checks |

Apply STRIDE to each component in a data flow diagram. Every arrow and process bubble has a different threat profile.

## AI Security Challenges

SecurityX adds AI threats because both attackers and defenders now use machine learning. Understand the attack mechanisms so you can recommend controls.

| AI Attack | Mechanism | Mitigation |
|-----------|-----------|------------|
| **Prompt injection** | Crafted input overrides model instructions | Input sanitization, output filtering |
| **Training data poisoning** | Corrupts a model by inserting malicious training examples | Data provenance, integrity checks |
| **Model theft** | Extracts a proprietary model through repeated queries | Rate limiting, query monitoring |
| **Model inversion** | Reconstructs sensitive training data from model outputs | Differential privacy, output minimization |
| **Deep fakes** | Generates convincing fake media for fraud or disinformation | Detection tooling, multi-channel verification |
| **Adversarial examples** | Subtly altered inputs that fool a classifier | Adversarial training, ensemble methods |

For a broader look at how AI is reshaping the threat landscape and what governance frameworks struggle with, read [the state of AI in cybersecurity](/articles/state-of-ai-cybersecurity-2026/) and the critical review of [AI governance certifications](/articles/ai-cybersecurity-governance-certifications-disappointing/). The [CompTIA SecurityAI+ course](/secai-plus-start/) covers AI security in far greater depth if this is a focus area for you.

## Governance Exam Tips

- When a question asks you to choose a governance document, ask: is it binding? Policies and standards are. Guidelines are not.
- ALE math appears on the exam. Practice: Asset = $500,000, EF = 20%, ARO = 0.5. SLE = $100,000. ALE = $50,000.
- SOC 2 Type II always beats Type I when assessing a vendor's ongoing reliability.
- STRIDE maps directly to countermeasures. Memorize the six categories and what stops each one.
- GDPR's 72-hour breach notification window is a frequent distractor question.

## Next Steps

With governance, risk, and compliance established, move to [Security Architecture](/casp-plus/security-architecture/) to design resilient systems that serve the risk strategy. Then continue to [Security Engineering](/casp-plus/security-engineering/) to implement those designs. When you have covered all four domains, test your readiness with the [CompTIA SecurityX Practice Test](/casp-plus-practice-test/) and review [tips for passing CompTIA exams](/articles/tips-and-tricks-for-passing-comptia-exams/).
