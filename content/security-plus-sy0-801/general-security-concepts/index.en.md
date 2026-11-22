---
title: "CompTIA Security+ SY0-801: General Security Concepts"
date: 2025-01-01
toc: true
draft: false
description: "Study General Security Concepts for CompTIA Security+ SY0-801. Learn to choose security controls, plan safe changes, and match cryptographic protections to a threat."
genre: ["CompTIA Security+ Course", "SY0-801", "Cybersecurity"]
tags: ["CompTIA Security+", "SY0-801", "security controls", "change management", "cryptography", "PKI", "digital signatures", "defense in depth"]
cover: "/img/cover/comptia-security-plus-sy0-801-general-security-concepts.webp"
coverAlt: "A gold padlock and key inside concentric rings above a branching decision path."
coverCaption: "Domain 1: General Security Concepts"
---

#### [Click Here to Return To the CompTIA Security+ Course Page](/security-plus-sy0-801-start/)

**General Security Concepts accounts for 16% of CompTIA Security+ (SY0-801). You will learn to choose the control that addresses a specific failure, plan security changes without breaking dependent services, and decide what cryptography must protect.**

*When two options would help, choose the one that meets the stated requirement without introducing a new failure.*

## Security Concepts and Controls (1.1)

### What needs protecting?

| Goal | What it protects | Example |
|------|------------------|---------|
| **Confidentiality** | Information from unauthorized disclosure | A claims reviewer can read only assigned cases |
| **Integrity** | Information from unauthorized or unintended changes | An import service rejects a rate table that differs from the approved version |
| **Availability** | Access for authorized users when needed | A standby service takes over during an outage |

**Authentication, authorization, and accounting (AAA)** answer three questions: Who are you? What may you do? What did you do? A hardware security key helps verify identity. A case assignment determines access. An audit record captures who viewed or changed the case. Stronger authentication does not fix an authorization rule that is too broad.

**Non-repudiation** supplies evidence that can help establish who signed or approved something later. An individual signing key and a protected timestamped record can support that claim. A shared account or shared signing secret weakens attribution because several people could have performed the same action.

**Defense in depth** layers controls so one failure does not expose the asset. For a claims portal, combine strong sign-in, case-level permissions, and independently retained audit records. **Least privilege** grants only the access needed for the task. **Zero Trust** means network location alone does not confer trust. Check the identity, device, and policy conditions before granting access to the requested resource, then reevaluate when appropriate.

### How the control works

| Category | What implements it | Example |
|----------|--------------------|---------|
| **Technical or logical** | Hardware or software enforcement | An application checks a case assignment |
| **Managerial or administrative** | Policy, oversight, or a management decision | A rule requires documented access approval |
| **Physical or environmental** | Protection of a physical space or equipment | A locked enclosure protects network gear |
| **Operational** | A recurring process performed by people | Staff reconcile visitor badges at closing |

| Type | What it does | Example |
|------|-------------|---------|
| **Preventive** | Blocks an unwanted action | A service rejects access outside the assigned role |
| **Deterring** | Discourages an action | A visible monitoring notice |
| **Detective** | Identifies an event or condition | An alert reports a restricted record was opened |
| **Corrective** | Restores or fixes a known problem | Restore a verified clean configuration |
| **Compensating** | Covers a control gap when the preferred control cannot be used | Supervise and separately log work on an old controller that cannot identify individual administrators |
| **Directive** | Instructs people to take a required action | A written procedure requires incident reporting |

Category and type describe different things. A locked cabinet is physical by category and preventive by purpose. A camera can deter when visible and detect when someone reviews its footage. Classify it by the function the scenario asks about.

**Decision:** If a claims reviewer must still download assigned material, blocking all downloads is too broad. Alerting on exports is useful but does not prevent cross-team access. Enforce case authorization at each download request and keep the alert as a separate layer.

## Change Management (1.2)

### Plan for the whole service

A **change owner** coordinates the work and confirms the outcome. **Stakeholders** include the teams that use or depend on the service, not just the people who maintain it. A **change advisory board (CAB)** or designated approver reviews the impact, test evidence, and recovery plan before the authorized change window.

| Change record | What to capture |
|---------------|-----------------|
| **Impact analysis** | Affected users, dependencies, permitted and blocked traffic, and business impact |
| **Test results** | What passed and what staging could not reproduce |
| **Maintenance window** | Expected downtime, notices, restart order, and restrictions on overlapping work |
| **Backout plan** | How to restore a known-good state, when to start, and how to verify recovery |
| **Fail-forward plan** | An approved corrective change when rollback is unsafe or cannot preserve newer data |
| **Evidence and documentation** | Approved version, post-change checks, and updates to diagrams, policies, or operating procedures |

A **standard operating procedure (SOP)** makes repeatable tasks consistent. It does not remove the need to review an unusual dependency. An allow list permits specified items. A deny list blocks specified items. A new allow list must include legitimate clients and scheduled service traffic. A new deny list may miss unlisted sources. Check for legacy systems, application or service restarts, and activities that must pause during the change.

### Choose when to stop

Suppose a hospital replaces a pharmacy-to-billing interface. Staging checks transmission but cannot reproduce the hourly billing batch. Before rollout, name the billing owner, test whatever staging can model, and schedule a check against the first real batch. Set a rollback decision before missed data would require manual correction.

If the update writes records the old version cannot read, reverting only the application may lose new work. Test restoration and reconciliation first. If rollback cannot preserve those records, require an approved fail-forward path rather than improvising after deployment.

**Version control** gives reviewers a stable record of the exact approved configuration and a known comparison point. Compare a read-only export of the running state with that approved revision, not with whatever staging runs today. Record deviations and update the service diagram and SOP after verifying the deployment.

## Cryptographic Solutions (1.3)

### Choose the protection first

| Need | Approach | What it does not solve |
|------|----------|------------------------|
| Hide content from unauthorized readers | **Encryption** using a key | Authorization inside a system that already decrypted the data |
| Compare content with a trusted reference | **Cryptographic hashing** produces a fixed-size digest | Identity of the publisher or protection when an untrusted source supplies both file and digest |
| Verify content and signer | **Digital signature** made with a private signing key and checked with the corresponding trusted public key | Confidentiality |
| Protect password verifiers | **Password hashing** with a unique random salt and suitable work factor | Online guessing, which also needs rate controls and other safeguards |
| Reduce casual exposure in a display or sample | **Obfuscation**, such as masking part of an account number | Strong confidentiality if an unauthorized party can recover the original |

A salt makes identical passwords produce different stored verifiers and thwarts reused precomputed guesses. It does not need to be secret and does not make a fast hash slow. For a public software download, a trusted signature can establish both origin and integrity. A digest stored on the same untrusted mirror as the file cannot establish either by itself.

### Match encryption to the boundary

**Symmetric encryption** uses a shared secret and is suited to bulk data. **Asymmetric cryptography** uses a public and private key pair for operations such as signing or helping protect a data key. A hybrid design can encrypt a large archive with a fresh symmetric key and protect that key for the intended recipient. **Key exchange** lets participants establish shared key material. Authentication of the exchange matters if a client must know who is on the other end.

| Boundary | Use it when |
|----------|-------------|
| **Full disk, partition, or volume** | You need protection for an entire drive or selected storage region when it is locked or offline |
| **File** | An exported document must stay encrypted when it moves to another system |
| **Database** | You need protection at the database storage layer, such as for data files |
| **Record** | Selected rows or records need protection independent of other data in the same database |
| **Transport** | Data must stay protected while crossing a network, such as with Transport Layer Security (TLS) |

Transport encryption does not keep delivered files encrypted. Storage encryption does not enforce which staff can query a running database. Choose supported algorithms, protocols, and key lengths together according to the organization's requirements. Increasing key length does not rescue a broken algorithm or correct poor key handling.

### Trust certificates and protect keys

**Public key infrastructure (PKI)** manages certificates, keys, and trust. A **certificate authority (CA)** signs certificates that bind public keys to an identity. A client validates the name, validity period, and chain to a configured **root of trust**. A self-signed endpoint certificate needs an independent trust setup. A third-party CA can reduce trust distribution for public clients. A private CA can serve managed clients that already trust its root.

- A **certificate signing request (CSR)** carries the public key and requested identity details for CA review. It does not contain the private key.
- A **wildcard certificate** can cover matching sibling hostnames. Sharing its private key across systems broadens the impact of one compromise.
- A **certificate revocation list (CRL)** publishes a set of revoked certificates. **Online Certificate Status Protocol (OCSP)** provides status for an individual certificate. Neither replaces the rest of chain validation.
- **Key escrow** keeps recovery material with an authorized custodian. Restrict access, require approval, and log retrieval. A **hardware security module (HSM)** can perform signing with a non-exportable key, avoiding private key copies on build runners.

**Decision:** If an older TLS client trusts the root and the leaf name and dates are correct, but validation succeeds only when the client cached the issuing intermediate, supply the missing intermediate on the server. A new root or a new leaf with the same incomplete chain does not address the failure.

## Exercise: Approve a Rate Update

A utility publishes a rate table to public mirrors and imports the same table into its billing service. Customers need to verify origin and integrity, not hide the rates. Billing may begin writing records under the new rates within 30 minutes, and reverting the application does not undo those writes.

Draft a short approval note. Identify one security goal and the applicable control type. Name the cryptographic protection and where clients get the trusted key. Specify a validation check, stop condition, and recovery action.

**Check your reasoning:** A signature lets readers verify the table against a publisher key distributed through a separate trusted channel. Enforcing signature verification before import is a preventive integrity control. Validate the first billing run against approved test totals and stop before new writes if the totals disagree. If new records exist, reconcile or restore them using a tested plan rather than rolling back binaries alone.

## Next Steps

Continue to [Threats, Vulnerabilities, and Attacks](/security-plus-sy0-801/threats-vulnerabilities-and-attacks/), try the [SY0-801 practice test](/security-plus-sy0-801-practice-test/), or return to the [Security+ course start page](/security-plus-sy0-801-start/).
