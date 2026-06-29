---
title: "CompTIA SecAI+ (CY0-001): Securing AI Systems"
date: 2025-01-01
toc: true
draft: false
description: "Master securing AI systems for the CompTIA SecAI+ CY0-001 exam. Learn AI threat-modeling frameworks, model and gateway controls, access controls, data protection, monitoring and auditing, and defenses against adversarial attacks like prompt injection and model poisoning."
genre: ["CompTIA SecAI+ Course", "Securing AI Systems", "Adversarial Machine Learning", "LLM Security", "AI Threats", "MITRE ATLAS", "OWASP", "AI Security", "CY0-001", "Cybersecurity"]
tags: ["CompTIA SecAI+", "CY0-001", "OWASP LLM Top 10", "OWASP ML Security Top 10", "MITRE ATLAS", "MIT AI Risk Repository", "prompt injection", "jailbreaking", "model poisoning", "data poisoning", "backdoor attack", "trojan attack", "model inversion", "model theft", "membership inference", "model skewing", "transfer learning attack", "output integrity attack", "insecure output handling", "excessive agency", "overreliance", "model guardrails", "prompt firewall", "AI supply chain", "least privilege"]
cover: "/img/cover/comptia-secai-plus-securing-ai-systems.webp"
coverAlt: "An illustration of a secure AI system with layers of protection around an AI model, featuring visual elements like encryption, access control, and monitoring systems, set against a dark background."
coverCaption: "Defend AI Systems Against Adversarial Attacks for the CY0-001 Exam"
---

#### [Click Here to Return To the CompTIA SecAI+ Course Page](/secai-plus-start/)

**Securing AI Systems** is **40%** of the **CompTIA SecAI+ (CY0-001)** exam, making it the most heavily weighted domain by far. This domain covers how you threat-model, control, and monitor AI systems, then how you investigate attacks and pick compensating controls. *Spend the bulk of your study time here. Master the threat names and the single control that stops each one.*

AI systems expand the attack surface. The model, the training data, the prompts, the outputs, the agents that act on those outputs, and the supply chain that delivered the model are all targets. You defend each layer with controls built for AI, not just the network controls you already know. This domain has six objectives, and most exam questions are scenarios that ask you to pick the right control or name the attack you are seeing.

## AI Threat-Modeling Resources

You do not invent AI risk from scratch. You map your defenses to published frameworks and repositories so you cover known threats systematically.

| Resource | What it provides |
|----------|------------------|
| **OWASP LLM Top 10** | The most critical security risks for LLM applications, such as prompt injection and insecure output handling |
| **OWASP ML Security Top 10** | The top risks for machine learning systems, such as data poisoning and model theft |
| **MITRE ATLAS** | Real adversary tactics and techniques used against AI systems |
| **MIT AI Risk Repository** | A large, searchable catalog of documented AI risks and harms |
| **CVE AI Working Group** | An effort to standardize how AI vulnerabilities are catalogued as CVEs |
| **Threat-modeling frameworks** | Structured methods such as STRIDE applied to AI data flows and components |

*MITRE ATLAS mirrors ATT&CK but for AI, so the tactics-and-techniques mindset you already have transfers directly. Reach for ATLAS when a scenario asks how a real adversary would attack a model.*

When you threat-model an AI system, map the data flows the same way you would for any application. Identify the trust boundaries around the model, the training data, the prompt interface, the output consumers, and the agent actions, then ask what an attacker could do at each boundary.

## Model and Gateway Controls

You harden the model itself, then put a gateway in front of it that inspects and limits every request.

**Model controls** govern the model's own behavior:

- **Model evaluation** tests the model against benchmarks and adversarial inputs to confirm it behaves safely before and after deployment.
- **Model guardrails** keep inputs and outputs within safe boundaries by blocking disallowed topics, formats, or actions.
- **Prompt templates** wrap user input in a fixed, parameterized structure so raw user text cannot redefine the model's instructions.

**Gateway controls** sit in front of the model and police traffic:

| Control | What it limits |
|---------|----------------|
| **Prompt firewall** | Inspects and filters prompts before they reach the model |
| **Rate limit** | How many requests a client may send in a time window |
| **Token limit** | The number of tokens allowed per request or response |
| **Input quota** | The data size and quantity a client may submit |
| **Modality limit** | Which input types such as text, image, or audio are accepted |
| **Endpoint access control** | Which clients may reach the AI service endpoint at all |

After you deploy guardrails, you must prove they work. **Guardrail testing and validation** deliberately probes the model with malicious and edge-case prompts to confirm the guardrails block what they should and allow legitimate use through.

*A guardrail you never tested is a guardrail you cannot trust. Red-team your own prompt firewall before an attacker does.*

## Access Control for AI

You restrict who and what can reach each part of the system. The objective lists four distinct surfaces, and each needs its own policy.

- **Model access** restricts who may query, fine-tune, export, or download a model.
- **Data access** restricts who may read or change the training data and the data a model retrieves at runtime.
- **Agent access** restricts what actions an autonomous agent may perform and which systems it may touch.
- **Network/API access** authenticates and authorizes every call to the AI application interface and segments the network around it.

*Apply least privilege to all four surfaces. An agent that only needs to read a calendar should never hold write access to production systems.*

## Data Security Controls

You protect data in all three states and reduce how much sensitive data the model ever sees.

| State | Control |
|-------|---------|
| **In transit** | Encryption while data moves across a network, such as TLS |
| **At rest** | Encryption for stored training data, embeddings, and logs |
| **In use** | Encryption or confidential computing while data is processed in memory |

You also de-risk the data itself before it ever reaches the model:

- **Data anonymization** strips identifiers so records cannot be linked back to a person.
- **Data classification labels** tag data by sensitivity so controls apply automatically.
- **Data redaction** permanently removes sensitive content from a record.
- **Data masking** hides sensitive values with substitute characters while preserving format.
- **Data minimization** collects and retains only the data that is strictly needed.

*Minimization is the cheapest control. Sensitive data you never collected cannot leak, cannot be inferred, and cannot be stolen.*

## Monitoring and Auditing

You watch the system continuously, protect the evidence it produces, and audit its quality.

- **Prompt monitoring** inspects both the query a user sends and the response the model returns for abuse or policy violations.
- **Log monitoring** reviews system and access logs for anomalies and attack patterns.
- **Log sanitization** strips sensitive data such as prompts or secrets from logs before storage.
- **Log protection** secures logs against tampering and unauthorized access so they hold up as evidence.
- A **response confidence level** reflects how certain the model is about an answer, which helps catch low-confidence outputs that may be wrong.
- **Rate monitoring** watches request volume per client to spot abuse, scraping, and denial-of-service attempts.

**AI cost monitoring** tracks spend so an attack or a runaway agent does not quietly run up a huge bill. You track four cost drivers:

| Cost driver | What you measure |
|-------------|------------------|
| **Prompts** | Volume and size of incoming queries |
| **Storage** | Cost of holding embeddings, vectors, and logs |
| **Response** | Tokens generated back to clients |
| **Processing** | Compute consumed during inference |

You also audit the model for quality and compliance:

- **Hallucinations** are confident but false outputs that you flag and correct.
- **Accuracy** measures how often outputs are correct against ground truth.
- **Bias and fairness** auditing reviews outputs for unfair or discriminatory behavior.
- **Access** auditing reviews who queried the model and what data they reached.

*Cost monitoring is a security control, not just a finance one. A sudden spend spike is often the first visible sign of a model denial-of-service attack or a leaked API key.*

## Adversarial Attacks

This is the heart of the domain. You must recognize each attack and the layer it targets. Group them by what the attacker is trying to do.

**Attacks on the model and its training:**

| Attack | What the attacker does |
|--------|------------------------|
| **Data poisoning** | Corrupts training data to bias or sabotage the model |
| **Model poisoning** | Tampers with model parameters or the training process to corrupt behavior |
| **Backdoor attack** | Hides a trigger that makes the model produce attacker-chosen behavior |
| **Trojan attack** | Embeds malicious behavior inside an otherwise normal-looking model |
| **Transfer learning attack** | Poisons a pretrained base model so the flaw carries into every model fine-tuned from it |
| **Model skewing** | Slowly shifts a model's behavior over time by feeding it biased feedback data |
| **AI supply chain attack** | Compromises third-party models, datasets, or libraries before you ever use them |

**Attacks through prompts and inputs:**

| Attack | What the attacker does |
|--------|------------------------|
| **Prompt injection** | Crafts input that overrides the model's intended instructions |
| **Jailbreaking** | Bypasses safety guardrails to elicit prohibited output |
| **Input manipulation** | Perturbs an input just enough to force a wrong classification |
| **Introducing biases** | Steers the model toward skewed or unfair outputs |
| **Circumventing AI guardrails** | Finds wording or encoding that evades the safety filters |
| **Manipulating application integrations** | Abuses a model's connected tools and plug-ins to act on other systems |

**Attacks that steal or break the model:**

| Attack | What the attacker does |
|--------|------------------------|
| **Model inversion** | Reconstructs sensitive training data from model outputs |
| **Model theft** | Extracts or clones a proprietary model through repeated queries |
| **Membership inference** | Determines whether a specific record was in the training data |
| **Output integrity attack** | Tampers with model output in transit so consumers act on falsified results |
| **Model denial of service (DoS)** | Floods the model with costly requests to exhaust compute and budget |
| **Sensitive information disclosure** | Coaxes the model into revealing secrets, PII, or system prompts |

*Model inversion and membership inference both leak training data, but they differ. Inversion rebuilds the data, while membership inference only confirms whether one record was used. Encryption and differential privacy defend both.*

## Application-Layer Risks

The application and agents around the model add their own risks, drawn from the OWASP LLM Top 10.

- **Insecure output handling** trusts model output without validation, enabling downstream attacks such as cross-site scripting or command injection.
- **Insecure plug-in design** exposes a model's plug-ins with weak input validation or excessive permissions.
- **Excessive agency** grants an agent more autonomy, permissions, or tool access than its task requires.
- **Overreliance** is when people trust AI output without verification and act on hallucinations or errors.

*Treat every model output as untrusted input to the next system. That single habit closes a large share of LLM application vulnerabilities, including insecure output handling and integration abuse.*

## Compensating Controls

When you analyze the evidence of an attack, you choose compensating controls that directly counter what you observed. Match the control to the attack.

| Control | Attacks it counters |
|---------|---------------------|
| **Prompt firewall** | Prompt injection, jailbreaking, circumventing guardrails |
| **Model guardrails** | Jailbreaking, sensitive information disclosure, biased outputs |
| **Prompt templates** | Prompt injection and instruction override |
| **Access controls** | Model theft, unauthorized data access, agent abuse |
| **Least privilege** | Excessive agency, manipulating application integrations |
| **Data integrity controls** | Data poisoning, model skewing, supply chain tampering |
| **Encryption** | Model inversion, membership inference, output integrity attacks |
| **Rate limiting** | Model denial of service, model theft, membership inference |

*Exam scenarios give you symptoms and ask for the fix. Read the evidence, name the attack, then pick the control from this table that stops it. The single best answer is the one aimed at the specific technique described.*

## Next Steps

With AI systems defended, continue to [AI-assisted Security](/secai-plus/ai-assisted-security/) to turn AI into a defensive tool, then [AI Governance, Risk, and Compliance](/secai-plus/ai-governance-risk-compliance/) to manage it responsibly. Review the foundations in [Basic AI Concepts](/secai-plus/basic-ai-concepts/) and return to the [CompTIA SecAI+ Course](/secai-plus-start/).
