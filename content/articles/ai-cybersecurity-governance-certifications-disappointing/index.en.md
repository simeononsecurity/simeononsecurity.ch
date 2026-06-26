---
title: "AI Cybersecurity and Governance Certifications Are Not Keeping Up with the Problem"
draft: false
toc: true
date: 2026-06-26
description: "A professional opinion on the gap between AI governance certifications and actual AI security practice. We passed several of them and came away disappointed. The frameworks are early and governance-focused. The attack surface grew faster."
tags: ["AI security", "AI governance", "AI certifications", "NIST AI RMF", "NIST AI 600-1", "ISO 42001", "IAPP AIGP", "prompt injection", "AI cybersecurity", "LLM security", "OWASP LLM Top 10", "MITRE ATLAS", "AI risk management", "AI compliance", "machine learning security", "model supply chain", "adversarial AI", "AI agents", "MCP security", "AI red teaming", "AI governance certifications", "agentic AI", "Google SAIF"]
---

We sat the exams. We passed. We came away with certificates and a level of disappointment I want to be specific about.

This is not a complaint about the people who built these programs. They are working with incomplete material. AI security as a discipline is young. The attack research is moving faster than the defensive tooling. The governance frameworks arrived before the engineering guidance.

The problem is the gap between what the certifications teach and what you need to know to actually secure AI systems in production.

## Three Layers That Are Frequently Confused

Before explaining what is missing, it helps to separate what currently exists.

The first layer is governance. Documents like NIST AI Risk Management Framework (AI RMF 1.0, 2023), ISO/IEC 42001:2023, and the EU AI Act operate at the organizational and process level. They describe how to manage AI risk, structure oversight, and document accountability. They are intentionally governance-focused rather than control-prescriptive. That is by design.

The second layer is threat taxonomy. MITRE ATLAS documents adversarial tactics against AI systems in the same format as ATT&CK. The OWASP Top 10 for Large Language Model Applications enumerates the attack classes most relevant to deployed LLMs. These documents name the attacks and describe how they work. They do not prescribe defenses.

The third layer is technical guidance. This includes Google's Secure AI Framework (SAIF), Microsoft's AI Security SDL, OWASP AI Exchange, NIST AI 600-1 (the Generative AI Profile), and vendor-specific security documentation from Anthropic, OpenAI, Meta, and others. These provide engineering-level guidance on secure deployment, evaluation practices, and runtime controls.

Most AI governance certifications cover the first layer thoroughly. They reference the second layer at a summary level. They rarely touch the third.

## What the Certifications Cover

The AI governance and security certifications currently available, including the IAPP AI Governance Professional (AIGP), ISACA's AI Fundamentals Certificate, ISO 42001 certifications, and CompTIA AI+, cover a consistent set of topics.

You learn the NIST AI RMF and how to map its four functions, Govern, Map, Measure, and Manage, to your organization's AI deployment. You learn the EU AI Act's risk tier classifications and what conformity assessment looks like for high-risk systems. You learn about bias, fairness, transparency, and accountability as governance principles. You learn how to write AI governance policies and conduct impact assessments.

These are real skills. Organizations need people who understand governance frameworks. They need people who read the NIST AI RMF and know what it is asking them to build.

What the certifications do not teach with the same depth:

- How attackers currently compromise AI systems in production
- What defense-in-depth for prompt injection looks like operationally and why no single control eliminates it
- How to verify the integrity of models before deployment
- What AI-specific red teaming involves and how to scope it
- How to evaluate model behavior against adversarial inputs before launch
- What AI observability looks like at inference time
- How AI incident response differs from standard IR playbooks
- What securing AI agents with tool access and external integrations requires

## The NIST AI RMF Is Governance, Not Engineering

The NIST AI RMF is a well-constructed document. NIST designed it to be technology-neutral, sector-agnostic, and applicable across different AI development approaches. This produces a framework that applies broadly.

It also means the framework does not prescribe technical controls for specific attack classes. If your organization adopts the AI RMF fully and maps all its functions to your AI deployment, you will have documented risk processes. You will not necessarily have a defense against prompt injection on your deployed language model.

NIST acknowledges this. NIST AI 600-1, the Generative AI Profile released in 2024, extends the AI RMF specifically for generative AI and large language models. It covers risks including prompt injection, data poisoning, and information hazards at a level of specificity the base AI RMF does not reach. If your certification covered the base AI RMF without AI 600-1, you missed the document most relevant to currently deployed systems.

## ISO 42001 and the Management System Comparison

ISO 42001:2023 is an AI management system standard. It provides a structure for governing AI development and deployment at the organizational level. Security professionals will recognize the parallel to ISO 27001 for information security.

ISO 27001 is widely adopted. Certified organizations still get breached. Certification documents that a management system exists, follows a defined process, and gets reviewed. It does not certify that the systems governed by that process resist the attacks being used against them.

ISO 42001 provides organizational discipline. Achieving certification tells stakeholders that your AI processes are documented, reviewed, and subject to governance. It does not tell them your deployed models produce consistent outputs under adversarial conditions, your agents operate within defined trust boundaries, or your fine-tuned models were built from verified training data.

That is the same gap ISO 27001 has. In traditional cybersecurity we learned to live with it. We should not pretend AI governance certifications close it when they share the same structural limitation.

## The EU AI Act Creates Outcome Requirements Without Engineering Specifications

The EU AI Act sorts AI systems by risk level: unacceptable (prohibited), high risk (conformity assessment required), limited risk (transparency obligations), and minimal risk (no specific requirements).

High-risk systems, including those used in critical infrastructure, biometric identification, employment screening, education, and law enforcement, face technical documentation requirements, human oversight obligations, and robustness requirements. The Act explicitly requires that high-risk AI systems be robust against attempts to alter behavior through adversarial manipulation.

That requirement is in the text. The Act intentionally specifies outcomes rather than prescribing technical controls. The technical methods for demonstrating adversarial robustness across all deployment contexts do not yet have consensus answers for every system type and use case.

Certifications built around the EU AI Act prepare you to classify AI systems, write technical documentation, and structure oversight protocols. They prepare you for audit. The engineering work that produces a system compliant with the Act's robustness requirements sits in a different discipline than the certifications currently cover.

## What Is Actually Attacking AI Systems

MITRE ATLAS and OWASP LLM Top 10 document the operational threat landscape. These are the resources that enumerate attacks at a useful level of detail. Governance frameworks reference threats at a higher abstraction. The following comes from those security-specific sources.

Prompt injection works by providing input to a language model that overrides or manipulates system instructions. Direct injection targets the model's input directly. Indirect injection embeds malicious instructions in content the model retrieves, processes, or summarizes. Your RAG pipeline reads an attacker-controlled document and acts on instructions hidden in it. Your browsing agent visits an attacker-controlled page and follows its embedded directives. Your customer support bot summarizes a support article containing instructions to ignore its safety guidelines.

There is no universally effective mitigation for prompt injection as of 2026. Defense-in-depth reduces risk: input filtering, output validation, privilege-limited tool scopes, sandboxed execution environments, and human approval gates on consequential actions. None of these eliminate the attack class. NIST, OWASP, Anthropic, OpenAI, Google, and Microsoft all recommend layered controls rather than single solutions.

Training data poisoning introduces malicious examples into training data to degrade model behavior, introduce backdoors, or implant trigger-based behaviors. The signal for successful poisoning is often absent until the model encounters specific trigger inputs. If your organization fine-tunes models on user-generated content, retrieved documents, or third-party datasets without verifying their provenance, you face this risk.

Model supply chain compromise is the threat most organizations treat as an afterthought. Model repositories often distribute executable code alongside model weights, and unsafe serialization formats like pickle have repeatedly created supply chain risks. Packages accompanying model downloads may install dependencies with their own vulnerabilities. Many organizations download and appear to apply significantly less supply-chain scrutiny to models from public repositories than they apply to software dependencies. The attack surface is comparable to npm but the security culture around it is much earlier.

Model extraction allows attackers to reconstruct functionally similar models through repeated inference queries against your API. This represents both intellectual property loss and a means of studying your model offline to develop more targeted attacks.

Membership inference allows attackers to determine with varying confidence whether specific data records were in your training set, depending on model architecture and training regime. This creates privacy risk for organizations that trained on personal information.

Adversarial inputs manipulate model outputs through crafted perturbations. The technique is most studied in image classification but applies to text, audio, and multimodal systems. If your AI makes decisions about fraud detection, creditworthiness, medical imaging, or physical access, adversarial robustness is a security property you need to test against, not just document.

Data leakage through AI systems is a category that deserves direct attention. RAG pipelines expose documents from your knowledge base, sometimes to users who should not have access to them. Prompt leakage from system instructions reveals operational details you intended to keep confidential. Multi-tenant AI deployments create isolation requirements that traditional application security engineers sometimes underestimate. These are operational risks that appear in deployed systems regularly.

## AI Agents Change the Attack Surface Entirely

Most AI security certifications were written when AI systems primarily meant chatbots and classifiers. Enterprise AI in 2026 increasingly means agents.

Agents differ from chatbots in one operationally important way: they take actions. An agent with tool access to your email system, internal databases, file systems, browser, and code execution environments is not a chatbot with more features. It is an autonomous process with significant access to real systems, operating based on language model outputs.

OWASP now maintains a separate Agentic AI Top 10 because the threat model for agents differs enough from LLM chat applications to require separate documentation.

Prompt injection in an agent context does not produce an unwanted text response. It produces an unwanted action. An indirect injection in a retrieved document instructs the agent to delete files, exfiltrate data, or send emails. The consequence is not an inappropriate answer. It is an unauthorized action taken against systems the agent has access to.

The attack surface for agents includes:

- Tool invocation limits: whether the agent is restricted to a minimal set of tools appropriate for each task
- Credential scope: whether the credentials the agent holds are limited to what each task requires
- Action reversibility: whether consequential actions require human approval before execution
- Output filtering: whether the agent's outputs are validated before they trigger downstream actions
- Sandboxing: whether the agent's execution environment prevents unintended access to connected systems

Most AI governance certifications do not cover agent security design at this level of specificity.

## Model Context Protocol Creates a New Enterprise Attack Surface

Model Context Protocol (MCP) has become a widely adopted standard for connecting AI agents to external tools, data sources, and services. MCP servers expose capabilities that agents discover and use. The integration is fast and flexible. The security implications are not always receiving equivalent attention.

MCP-specific risks include:

- Malicious MCP servers that misrepresent their capabilities to an agent and execute unintended actions
- Tool poisoning where a legitimate MCP server returns attacker-controlled data embeds instructions in what should be data outputs
- Overprivileged tools where MCP integrations hold permissions beyond what the task requires
- Trust boundary confusion where agents receive instructions from attached MCP tools that appear equivalent to user instructions

Organizations deploying agents with MCP integrations need a framework for evaluating MCP server trust, auditing tool permissions, and validating that tool responses are treated as data rather than instructions.

## Evaluation Is the Operational Practice Certifications Skip

AI red teaming and evaluation suites are replacing static security assessments as the primary methods for understanding AI model risk before and after deployment.

Red teaming for AI involves:

- Structured adversarial testing of model behavior against known attack techniques
- Jailbreak benchmarking against established prompt attack datasets
- Adversarial robustness testing that measures output drift under perturbed inputs
- Behavioral regression testing between model versions
- Safety benchmark evaluation against published evaluation suites

NIST, Anthropic, OpenAI, Microsoft, Google, and CISA all recommend AI-specific red teaming before deployment for high-risk systems. This is becoming standard expectation, not optional practice.

None of the current AI governance certifications adequately prepare practitioners to scope, execute, or interpret a red teaming exercise against a deployed model or agent system. They describe what red teaming is. They do not teach you to do it.

## AI Observability Is a Separate Discipline

Traditional security logging does not transfer directly to AI systems. Monitoring an LLM or agent in production requires different data collection and different analysis.

AI observability infrastructure covers:

- Prompt and output telemetry for anomaly detection and policy violation identification
- Tool invocation logs for agents, including what tools were called with what arguments
- Retrieval quality monitoring for RAG pipelines
- Jailbreak attempt detection and classification
- Output consistency monitoring to detect model drift between versions
- Hallucination rate tracking for applications where factual accuracy matters
- Latency patterns that may indicate prompt injection attempts inflating context size

This is an emerging discipline. Most organizations deploying AI in 2026 have significantly less observability into their AI components than into their traditional infrastructure. Most governance certifications do not describe what adequate observability looks like for AI systems.

## AI Incident Response Is Not Like Regular IR

When a traditional system gets compromised, your IR playbook covers containment, forensics, and recovery. AI incidents introduce questions the standard playbook does not address.

Questions you need playbooks for before you need them:

- How do you determine whether a model was poisoned during fine-tuning
- How do you assess whether a RAG retrieval was abused to return attacker-controlled content
- How do you identify whether an agent executed unauthorized actions and what their scope was
- How do you verify whether a model update from a third-party provider changed behavior in security-relevant ways
- How do you establish what a model's behavior was before an incident to compare to post-incident behavior

These require preparation before the incident. They require logs and telemetry you have to set up in advance. They require AI-specific runbooks that dedicate space to forensics on model behavior, not just network traffic and endpoint logs.

## The Certification Update Problem

One structural reason certifications lag behind current practice: AI security changes faster than certification update cycles allow.

Security+, CISSP, and ISO 27001 cover domains that evolve over years. The core attack surfaces of networks, endpoints, and applications are relatively stable. AI attack techniques evolve across months. Prompt injection techniques, adversarial attack methods, and agentic attack surfaces in 2026 look different from what existed when the first AI certifications launched in 2023 and 2024.

Certification bodies update materials on schedules. The OWASP LLM Top 10 published a significant revision within its first year. MCP did not exist as an enterprise concern when many current AI certifications were designed. Agentic AI security frameworks post-date most current certification curricula.

This is a structural problem, not a failure of intent. You need to read primary sources on an ongoing basis rather than treat a certification as a fixed body of knowledge.

## What Needs to Be in AI Security Certification Content

For certification curricula to reflect current AI security practice, they need to cover:

- Prompt injection defense-in-depth: input filtering, output validation, tool scoping, sandboxing, and human approval gates, along with the documented limitations of each
- Model supply chain verification: unsafe serialization risks, SBOM requirements, provenance documentation, and signed artifact verification
- AI agent security architecture: trust boundaries, minimal privilege tool access, action reversibility, and monitoring requirements
- MCP and external integration security: trust evaluation for tool servers, tool permission auditing, and data vs. instruction separation
- Evaluation and red teaming: how to scope an adversarial evaluation, what benchmarks and evaluation datasets exist, and how to interpret results
- AI observability: what logs and telemetry AI systems require, and how to use them for incident detection and response
- AI-specific incident response: pre-planning for AI incident scenarios, evidence collection for model behavior questions, and recovery considerations unique to AI systems
- Data leakage prevention: RAG isolation, prompt confidentiality, multi-tenant access controls, and output filtering

## What You Should Do Right Now

If you are responsible for AI systems in your organization:

Read the OWASP Top 10 for Large Language Model Applications and the OWASP Agentic AI Top 10. They are free. They are more operationally specific than any current paid certification curricula.

Review MITRE ATLAS before your next threat modeling session on any AI component. Know what adversary tactics apply to your architecture before you finalize your deployment design.

Read NIST AI 600-1. It extends the base AI RMF specifically for generative AI and is significantly more relevant to LLM and agent deployments than the base framework alone.

Review Google SAIF, Microsoft's AI SDL, and OWASP AI Exchange for engineering-level guidance that governance frameworks do not provide.

Verify the provenance of every model your organization deploys. Check model cards. Scan serialization formats for known exploit classes before loading weights.

Map every AI agent in your environment against the access it holds. An agent with read and write access to your internal knowledge base, email, and file system is a prompt injection amplifier. Minimize its credentials to what each task requires.

Require AI-specific red teaming before deploying any model or agent into a high-consequence context. Treat it as mandatory, not optional.

Build AI-specific incident response runbooks now, before you need them.

Treat your governance certification as documentation of your process layer. It is not documentation of your security posture.

## References

- NIST AI Risk Management Framework (AI RMF 1.0), 2023
- NIST AI 600-1: Generative AI Profile, 2024
- NIST SP 1270: Towards a Standard for Identifying and Managing Bias in Artificial Intelligence
- ISO/IEC 42001:2023 Artificial Intelligence Management Systems
- EU AI Act, Regulation (EU) 2024/1689
- OWASP Top 10 for Large Language Model Applications, 2025
- OWASP Agentic AI Top 10
- OWASP AI Exchange
- MITRE ATLAS: Adversarial Threat Landscape for AI Systems
- Google Secure AI Framework (SAIF)
- Microsoft AI Security SDL documentation
- CISA Guidance on AI Cybersecurity, 2024
- Barreno et al., Can Machine Learning Be Secure?, 2006
- Biggio et al., Poisoning Attacks Against Support Vector Machines, 2012
- Goodfellow et al., Explaining and Harnessing Adversarial Examples, ICLR 2015
- IAPP AI Governance Professional (AIGP) program documentation
- ISACA AI Fundamentals Certificate program documentation
