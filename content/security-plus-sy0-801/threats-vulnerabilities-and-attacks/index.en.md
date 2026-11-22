---
title: "CompTIA Security+ (SY0-801): Threats, Vulnerabilities, and Attacks"
date: 2025-01-01
toc: true
draft: false
description: "Study the SY0-801 threats domain. Compare threat actors and attack surfaces, interpret incident evidence, and choose controls for conventional and AI risks."
genre: ["CompTIA Security+ Course", "Threat Analysis", "Cybersecurity"]
tags: ["CompTIA Security+", "SY0-801", "threat actors", "attack vectors", "vulnerability analysis", "incident triage", "AI security"]
cover: "/img/cover/comptia-security-plus-sy0-801-threats-vulnerabilities-and-attacks.webp"
coverAlt: "A red magnifying lens highlights an interrupted signal in a network of connected nodes."
coverCaption: ""
---

#### [Click Here to Return To the CompTIA Security+ Course Page](/security-plus-sy0-801-start/)

**Threats, Vulnerabilities, and Attacks account for 24% of the CompTIA Security+ (SY0-801) exam. Learn to trace a suspected incident from its possible entry point to the affected asset, then choose a response supported by the evidence.**

*When two answers sound reasonable, identify which one addresses the exposed asset, the observed behavior, or the decision named in the question.*

## Threats and Vulnerabilities (2.1)

A **threat** is a potential cause of harm. A **vulnerability** is a weakness. An **attack** is an attempt to cause harm or gain unauthorized access. **Risk** captures the likelihood and impact of harm in context. An alert about a vulnerability is evidence of exposure, not proof of an attack.

| Element | Example from a remote service |
|---|---|
| **Threat** | Unauthorized access through a third-party support connection |
| **Vulnerability** | A support account retains write access after its contract ends |
| **Exposure** | The account still reaches a service holding customer records |
| **Potential impact** | Unauthorized changes or disclosure of customer records |
| **Evidence of activity** | A completed session with recorded changes during the exposure window |

**Prioritize in context.** Two devices with the same vulnerability rating do not necessarily pose equal risk. Compare reachability, the privileges at stake and the consequence of failure. An isolated lab display and a broadly reachable clinical data relay warrant different schedules. Fix the relay first if the operational owner approves a safe window and rollback plan. If a patch must wait, reduce its reachability and give the temporary control an expiry date.

A **Common Vulnerabilities and Exposures (CVE)** identifier names a publicly disclosed weakness. The **Common Vulnerability Scoring System (CVSS)** describes technical severity under specific assumptions. Use the identifier to connect scanner results with a vendor advisory, then check the deployed version, network path, and business impact. Neither the identifier nor the score confirms local exploitability or a successful attack.

A **threat feed** supplies indicators or reports. Compare external reporting with vendor advisories and internal observations. Gather evidence, assess relevance, share time-bounded findings, and revisit them as conditions change. A reported domain seen in local logs is a lead. An approved service using shared infrastructure is an alternative explanation.

## Threat Actors and Motives (2.2)

Treat an actor label as a working hypothesis. A request for payment provides stronger evidence of a financial motive than an unfamiliar address provides about who controls it.

| Actor or activity | Evidence worth checking |
|---|---|
| **Opportunistic attacker** | Broad probing with little apparent interest in the victim's business |
| **Organized crime** | Data theft followed by an extortion demand or repeated fraud |
| **State-backed actor** | Sustained collection around strategic priorities, with corroborated attribution needed |
| **Hacktivist** | Public claims and demands tied to a political or social cause |
| **Intentional insider** | Authorized access used outside the employee's role or duties |
| **Unintentional insider** | An error, such as a mistaken share, without evidence of malicious intent |

Motives include **financial gain, espionage, sabotage, revenge, ideology,** and **disruption**. Distinguish motive from means. Theft followed by a payment demand supports extortion even when no files were encrypted. Selective, quiet collection suggests espionage, but does not by itself identify a state sponsor. Compare access, resources, persistence, and observed behavior before making an attribution. An unskilled attacker seeking notoriety, a competitor seeking intellectual property, and a terrorist seeking fear or disruption require different hypotheses. An authorized researcher acting within a defined reporting program is different from an attacker who claims an ethical motive.

## Threat Vectors and Sources (2.3)

A **vector** is the path a threat takes. An identity compromise has several possible entry points: a message, a browser extension, a remote access provider, or a physical handoff. Choose a control at the relevant trust boundary.

| Vector | Practical defense |
|---|---|
| **Email, SMS, collaboration tools, voice, or QR codes** | Verify sensitive requests through an established contact or workflow. Do not use coordinates, numbers, or links supplied by the suspect message. |
| **Attachments and browser content** | Limit executable content, restrict extension permissions, and isolate untrusted documents from privileged sessions. |
| **Remote support and trusted service providers** | Use time-limited scopes and named sessions. Correlate vendor logs with local identity and endpoint evidence. |
| **Software and hardware supply chains** | Verify provenance and integrity, record dependencies and stage updates before wider rollout. |
| **Removable media and physical access** | Use managed media, inspect files before import, and restrict unattended access to sensitive equipment. |
| **Network and wireless access** | Limit reachable services and require authenticated access. Inventory unmanaged devices and isolate guest, sensor, and equipment networks. |

**Worked decision:** A supplier requests new payment details in a thread the accounting team recognizes. Domain authentication passed. Hold the changed payment and call the supplier's previously recorded number. Authentication provides evidence about message origin, not evidence of approval for the business instruction. A second email to the same account is not an independent check.

A **watering hole** is a compromised resource frequently visited by a target group. Watch for altered content and unexpected browser activity from familiar sites. A **living-off-the-land** signal involves abuse of a legitimate system tool. Compare the process and its parent, user, and timing with normal administrative work before blocking a tool used for operations. For low-power radio and operational technology (OT), account for physical access and operational safety before changing the network.

## Vulnerabilities and Attack Surfaces (2.4)

An **attack surface** is the set of interfaces and relationships exposed to abuse. Inventory public and internal services, cloud permissions, identities, browser extensions, mobile apps, connected devices, and supplier connections. Include equipment without a vendor patch path.

| Weakness | Control matched to the weakness |
|---|---|
| **Broken object-level authorization** | Check access to the specific record at the server. Random identifiers and encrypted transport do not authorize reads. |
| **Unsafe input handling** | Keep incoming data separate from instructions. Use parameterized database queries and context-appropriate output encoding. |
| **Excessive permissions** | Remove unneeded privileges. Give a build consumer pull-only access and isolate publishing privileges. |
| **Exposed default settings** | Replace default credentials, remove unused services, and check configuration drift against a known baseline. |
| **End-of-life equipment** | Plan replacement. Until then, segment the equipment and limit authorized maintenance through an audited access point. |
| **Hardcoded secrets or stale credentials** | Revoke exposed or unused credentials. Move active secrets to controlled storage and restrict their scope. |
| **Time-of-check to time-of-use race** | Bind the check and use to the same approved state. Revalidate when the state changes. |
| **Public repository or object storage** | Remove public access when unnecessary, verify the effective permission boundary, and review historic access. |
| **Unverified dependencies or firmware** | Use trusted sources, review dependencies, verify integrity, and deploy approved updates in stages. |

**Choose a treatment you are able to verify.** Encrypting a service connection protects data in transit. It does not fix user-to-user data exposure. Logging provides visibility but does not reduce an account's write authority. A **zero-day** weakness is newly discovered or exploited before an effective fix is available. Disable an affected feature or restrict access according to the advisory. When a software fix is not immediately available, name the temporary boundary, test its effectiveness, and set a replacement date.

## Indicators of Malicious Activity (2.5)

An **indicator of compromise (IOC)** is an observable artifact associated with possible compromise, such as a known file hash or unauthorized account change. An **indicator of attack** describes behavior consistent with an attempted or ongoing attack. One weak signal rarely answers both whether an attack occurred and what it affected.

| Evidence pattern | What it suggests | What to verify next |
|---|---|---|
| A few authentication failures per account across many users | Possible **password spraying** | Search nearby successful sessions and compare with expected login activity. |
| Unexpected MFA notices, followed by approval and unfamiliar account changes | Possible identity takeover | Correlate challenge approval, session creation and the identity behind each change. |
| Rapid file rewrites across shares from one unexpected source | Possible **ransomware** or destructive activity | Restrict the source, preserve evidence, and protect known-good recovery copies. |
| Unexpected outbound traffic from a workstation | Possible unauthorized transfer or a new approved service | Match the process, destinations, timing and volume against a known baseline. |
| Many clients fail to reach a service at once | Possible denial of service or ordinary outage | Compare service health, deployment history, network telemetry, and client errors. |
| Conflicting certificate or endpoint identity evidence | Possible impersonation, interception, or configuration error | Verify the approved endpoint identity from a separate trusted source. |

Work from **timestamp, identity, source, action, and outcome**. Separate observation from inference. For example, a failed login is an attempt. An unfamiliar successful login followed by unauthorized forwarding provides stronger evidence of misuse. When harm is ongoing, choose a reversible containment step and preserve the logs at the same time.

### Compare similar signals

A **Trojan** masquerades as legitimate software. A **worm** spreads on its own, while a **virus** infects a host file or program. A **logic bomb** activates under a specified condition. **Fileless malware** usually leaves more evidence in memory and process telemetry than in a standalone executable. **Spyware** gathers information without authorization. A **keylogger** records keystrokes, **adware** displays unwanted ads, and a **rootkit** hides or preserves unauthorized access.

Check the evidence closest to the suspected event. For **tailgating**, compare badge events with access-area observations. For **skimming** or **shoulder surfing**, check the suspected reader or entry point before assuming which credentials were exposed. A suspicious domain resolution warrants comparison with trusted DNS records before declaring **cache poisoning**. An unexpected older protocol warrants a policy and negotiation check before concluding **downgrade**.

Attempts to read unexpected files suggest **directory traversal**. An action repeated with previously accepted authentication data suggests **replay**. Review server authorization decisions when an account gains capabilities outside its role. One successful administrative action is meaningful only after you establish who performed it and what access was approved.

## Threats in AI Usage (2.6)

AI applications introduce separate boundaries at input, retrieval, storage, output, and tool use. Begin by finding where the application accepts outside data and where it performs an action.

| Risk | Defensive response |
|---|---|
| **Prompt injection** | Treat messages, retrieved pages, and attachments as untrusted data. Keep sensitive tool actions behind independent authorization. |
| **Data poisoning** | Track the provenance of training and retrieval inputs. Review changes and compare unexpected behavior against a known-good dataset or index. |
| **Sensitive data leakage** | Enforce source permissions before retrieval. Minimize inputs and review how the provider retains, processes, and shares data. |
| **Hallucination** | Verify material claims and citations against authoritative sources. A plausible answer is not evidence of accuracy. |
| **Bias or manipulated output** | Test relevant populations and edge cases. Check results against independent labels and keep review for consequential decisions. |
| **Synthetic impersonation** | Verify sensitive instructions using a known contact channel and existing approval rules. Do not decide from voice familiarity alone. |
| **Model manipulation, evasion, or jailbreaking** | Test observed outputs against expected behavior. Audit model releases and evaluate whether a control failure is in the model, input classifier, or application policy. |
| **Session hijacking or unsafe code execution** | Use protected, scoped sessions. Keep generated code and tool output untrusted, and prevent model output from running with production authority. |
| **Limited explainability** | Require evidence and a review path for consequential decisions. Record the source and human approval rather than treating the model's explanation as proof. |
| **AI supply-chain compromise** | Verify the model and dependency sources. Restrict deployment privileges and test approved releases before giving them data or tools. |

**Worked decision:** A support assistant summarizes attachments and attempts to close tickets without approval. Keep summarization read-only and require an independently authorized closure. Changing the model's instructions is useful for its normal behavior, but does not enforce the permission boundary. Better transport encryption does not stop a permitted tool from acting on untrusted input.

## Exercise: Triage a Vendor Session

A supplier's remote-support platform reports an incident. A local support identity opened a session outside its approved maintenance window. Endpoint logs show an unexpected service change on one staging server. Production uses the same supplier but its logs show no matching change. The staging server supports tomorrow's release. No payment demand or public claim has appeared.

1. Write one sentence each for the possible vector, weakness, and impact.
2. Name the evidence you would preserve and one correlation you would perform.
3. Choose one immediate control. Give a condition for widening it to production.
4. State one conclusion the evidence does not support.

**Expected reasoning:** The likely vector is the trusted support path, with out-of-window access indicating a possible authorization gap. The observed impact is an unexpected staging change. Preserve the session, identity, endpoint, and change records, then map the service change to the supplier session and approved maintenance ticket. Restrict the implicated identity or access path while you assess the release dependency. Widen containment if corroborated production evidence appears or you confirm the same exposed identity still reaches production. Do not claim production compromise or attribute the incident to a specific motive based on staging evidence alone.

## Next Steps

Continue to [Security Architecture](/security-plus-sy0-801/security-architecture/) to study how trust boundaries limit exposure. Review [General Security Concepts](/security-plus-sy0-801/general-security-concepts/) or return to the [Security+ course hub](/security-plus-sy0-801-start/). Use the [SY0-801 practice test](/security-plus-sy0-801-practice-test/) to apply these decisions to new scenarios.
