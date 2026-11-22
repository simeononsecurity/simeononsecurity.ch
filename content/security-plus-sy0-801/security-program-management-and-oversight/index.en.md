---
title: "CompTIA Security+ SY0-801: Security Program Management and Oversight"
date: 2025-01-01
toc: true
draft: false
description: "Study Security+ SY0-801 Domain 5 through decisions about policies, risk treatment, suppliers, compliance, audits, and security awareness."
genre: ["CompTIA Security+ Course", "Security Governance", "Risk Management", "Compliance"]
tags: ["CompTIA Security+", "SY0-801", "governance", "risk register", "third-party risk", "privacy", "security audits", "security awareness"]
cover: "/img/cover/comptia-security-plus-sy0-801-security-program-management-and-oversight.webp"
coverAlt: "A violet checklist and balance scale stand beside a shield and evidence tiles."
coverCaption: "Security Program Management and Oversight, SY0-801 Domain 5"
---

#### [Click Here to Return To the CompTIA Security+ Course Page](/security-plus-sy0-801-start/)

**Security Program Management and Oversight accounts for 14% of CompTIA Security+ SY0-801.** You assign owners, choose a risk response, check whether controls work, and teach staff how to act when something goes wrong.

*For scenario questions, identify the obligation, the decision owner, and the evidence before you pick a control.*

## 5.1 Governance Artifacts

A **policy** states a mandatory direction. A **standard** sets a measurable requirement. A **procedure** describes how to meet it. A **guideline** recommends an approach without mandating it.

| Artifact | Workplace use |
|---|---|
| **Policy** | Set rules for acceptable use, personal devices, clean desks, privacy, data classification, or vulnerability disclosure |
| **Standard** | Specify approved encryption settings and required verification records |
| **Procedure or runbook** | Give operators the steps to enroll a laptop and verify encryption |
| **Guideline** | Offer recommended configurations, reference designs, or advisory material |
| **Business continuity plan (BCP)** | Keep essential work running through alternate facilities, suppliers, or manual workflows |
| **Disaster recovery plan (DRP)** | Restore systems and data in priority order after a disruption |

A distributor loses its packing floor during a flood. The **order system** is still online, so restoring it solves nothing. The continuity plan shifts priority orders to another warehouse. If the order system later fails, the recovery plan covers its restoration.

*Match the document to the gap. A requirement belongs in a standard, not in a runbook built around one vendor.*

## 5.2 Risk Management

**Risk assessment** estimates likelihood and impact. Review both existing controls and what remains after they are applied. A **risk register** tracks each risk, owner, rating, treatment, due date, and residual exposure.

| Risk measure | Decision it informs |
|---|---|
| **Risk appetite** | Broad level of risk leadership accepts in pursuit of its goals |
| **Risk tolerance** | Threshold for a particular objective or category of exposure |
| **Inherent risk** | Exposure before the assessed controls |
| **Residual risk** | Exposure still present after controls |
| **Business impact analysis (BIA)** | Processes to restore first, based on outage impact over time and dependencies |

**Risk treatment** follows the assessment. Accept an exposure within authority. Mitigate it with a control. Transfer part of its financial impact through insurance or contract. Avoid it by stopping the activity. Insurance does not restore a service or remove the duty to protect its data.

**Quantitative example:** A service estimates a **single loss expectancy (SLE)** of $180,000 and an **annualized rate of occurrence (ARO)** of 0.2. Multiplying these gives an **annualized loss expectancy (ALE)** of $36,000. A proposed $12,000 annual control reduces the estimated loss per event to $80,000 without changing frequency. Its residual ALE is $16,000, for $20,000 a year in avoided loss before control costs. The estimate favors the control by $8,000 per year, before other costs and benefits.

Use a **qualitative assessment** when good frequency or cost estimates are unavailable. Define shared scoring criteria, identify the data gaps, and revisit the rating when evidence improves. If a necessary temporary exception remains within tolerance, record the controls, owner approval, expiry, and conditions for review.

*Compare mitigation cost to expected loss reduction, not to the remaining loss.*

## 5.3 Third-Party Risk

A **request for information (RFI)** surveys vendor capabilities. A **request for proposal (RFP)** asks vendors how they would solve a defined problem. A **request for quotation (RFQ)** asks for comparable prices for well-defined needs. An **expression of interest** identifies willing suppliers before a fuller selection process.

| Agreement or target | Purpose |
|---|---|
| **Non-disclosure agreement (NDA)** | Protect exchanged confidential information |
| **Master services agreement (MSA)** | Set the standing legal and commercial terms |
| **Statement of work (SOW)** | Define deliverables, schedule, and acceptance for a project |
| **Service-level agreement (SLA)** | Set agreed service commitments, measurement, and remedies |
| **Service-level objective (SLO)** | Set a specific service target, with no contractual remedy unless incorporated into the agreement |
| **Memorandum of understanding (MOU)** | Record shared intent and responsibilities, with enforceability dependent on its terms |

In **due diligence**, check vendor control evidence, data access, subcontractors, jurisdiction, and potential conflicts of interest. Align costs, staffing, and audit rights with the service's importance. Use a **vendor registry** to track ownership, contracts, and assurance dates. Monitor service metrics and reassess material changes rather than relying on the previous year's attestation.

**Exit planning:** A records platform meets availability goals, but only exports PDFs with no usable metadata. Negotiate a structured export and exit assistance, then test importing a sample before signing. Better uptime or a wider right to audit does not make the data portable.

*Use the contract to address the specific failure: missed service, unauthorized subcontracting, or a failed exit.*

## 5.4 Security Compliance

A **compliance program** maps duties from laws, regulations, and contracts to owners, controls, evidence, and reporting deadlines. Train the staff who perform the controls, monitor exceptions, and escalate failures. Possible consequences include fines, loss of contracts, or operating restrictions.

| Duty | Practical response |
|---|---|
| **Retention** | Assign a documented retention period by record type and dispose of expired records securely |
| **Legal hold or order** | Preserve the specified material and suspend routine deletion for the covered records |
| **Privacy rights** | Verify and route requests for correction, erasure, opt-in or opt-out, or processing restrictions under the applicable rule |
| **Incident notification** | Determine which trigger starts the clock, who must receive notice, and what facts the first notice requires |

A **controller** determines why and how personal data is processed. A **processor** handles data on the controller's instructions. For example, a payroll processor routes a worker's correction request to the employer and assists with a verified correction. A legal duty to preserve specified records takes precedence over their ordinary deletion schedule. Consult the responsible legal or privacy owner when duties conflict.

For **role-based compliance training**, teach approval and reporting for the work staff perform. Procurement staff need to recognize prohibited gifts and bribery risks. Payment investigators need to know their money-laundering and terrorist-financing procedures. Log completion and test whether the required escalation occurs.

*An internal ticket or a completed training record does not prove a statutory or contractual reporting duty was met.*

## 5.5 Audits and Assessments

An **audit** evaluates evidence against defined criteria. An **assessment** evaluates a control or risk against a stated goal. Neither term alone tells you whether the engagement checks a design, measures operation over time, or tests a security outcome.

| Method or reference | What it answers |
|---|---|
| **Internal audit** | Whether controls meet criteria through an organization's independent review function |
| **External audit** | Whether evidence supports conclusions by an outside reviewer |
| **Functional test** | Whether a control produces its specified result in a defined case |
| **Behavioral test** | How a system or group responds to realistic conditions |
| **Penetration test** | Whether weaknesses create material exposure within written authorization and limits |
| **MITRE ATT&CK** | Which known adversary behaviors a defensive control is intended to detect or limit |
| **Cyber Kill Chain** | Where in an intrusion sequence an organization expects to interrupt activity |

Before the engagement, write down **scope and rules of engagement**: included systems, exclusions, methods, timing, owners, and escalation paths. With **black-box** testing the evaluator starts with minimal internal knowledge. **Gray-box** testing provides limited context. **White-box** testing supplies extensive internal information. Knowledge level does not expand authorization.

**Evidence example:** A policy requires quarterly approval of privileged accounts. A current account list shows who has access now. To check last year's operation, sample each quarter's approval records, contemporaneous account lists, and follow-up on exceptions.

*Choose evidence for the claim and time period. Report limitations instead of implying the checks covered systems outside scope.*

## 5.6 Security Awareness

Start with a **target behavior**. Staff should know what to do with a suspicious request, a missing device, or a private record in the wrong channel. Teach the reporting route during onboarding, then rehearse it in short role-based sessions and refresh it after process changes.

| Exposure | Behavior to rehearse |
|---|---|
| **Social engineering** | Decline unsolicited requests for credentials and report them through the known channel |
| **Business email compromise (BEC)** | Verify sensitive requests independently through a trusted contact path |
| **Passwords and multifactor authentication (MFA)** | Use approved credential tools, deny unexpected prompts, and report repeated requests |
| **Bring your own device (BYOD)** | Use approved work applications and report loss promptly |
| **Remote work** | Protect unattended screens and use the approved remote access route |
| **Unapproved sharing** | Stop sharing sensitive material, report the incident, and switch to a restricted location |

Use **behavior metrics** to evaluate training. Compare similar drills before and after training, measure the share reported correctly, and track median reporting time. Completion records tell you who took the course. They do not show whether employees reported the event instead of forwarding it.

*Make the secure action practical during a busy shift, then test whether staff use it.*

## Self-Check

- **Risk:** A $9,000 yearly control cuts estimated annual losses from $30,000 to $24,000. Under a savings-only rule, should you recommend it? No. The reduction is $6,000 per year, $3,000 less than the recurring cost. A contractual requirement would change the decision criteria.
- **Vendor review:** A new payroll subcontractor needs access to tax records. Is the original provider's audit report enough? No. Confirm the new scope and approval requirements, then obtain evidence specific to the subcontractor's access and handling.
- **Audit:** You have last year's retention policy and today's settings. Do those prove every scheduled purge ran? No. Sample dated job results and exception records from the period being audited.

*If you choose a different action, identify the requirement or evidence your choice satisfies better.*

## Next Steps

- **Review:** Revisit [Security Operations](/security-plus-sy0-801/security-operations/) for control implementation and investigation.
- **Practice:** Take the [SY0-801 practice test](/security-plus-sy0-801-practice-test/).
- **Return:** Use the [Security+ SY0-801 course hub](/security-plus-sy0-801-start/) to select another domain.

*Use missed questions to identify which decision or evidence you need to review.*
