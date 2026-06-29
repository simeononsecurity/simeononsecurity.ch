---
title: "ISC2 CISSP: Identity and Access Management (IAM)"
date: 2025-01-01
toc: true
draft: false
description: "Master Identity and Access Management for the ISC2 CISSP exam. Learn physical and logical access control, authentication strategy, federation, authorization models, and the identity lifecycle."
genre: ["ISC2 CISSP Course", "Identity Management", "Access Control", "Authentication", "Federation", "ISC2 Certification", "Information Security", "RBAC", "MFA", "Cybersecurity"]
tags: ["ISC2 CISSP", "CISSP", "identity and access management", "IAM", "authentication", "MFA", "SSO", "federation", "RBAC", "MAC", "DAC", "ABAC", "provisioning", "access control"]
cover: "/img/cover/isc2-cissp-identity-access-management-illustration.webp"
coverAlt: "An illustration showing interconnected devices and systems representing identity and access management, with user authentication interfaces and multi-factor authentication symbols on a dark background."
coverCaption: "Master Identity and Access Management for the CISSP Exam"
---

#### [Click Here to Return To the ISC2 CISSP Course Page](/cissp-start/)

**Identity and Access Management** is **13%** of the **ISC2 CISSP** exam. This module covers how you prove who someone is and control what they can reach across the full identity lifecycle. *Access control models are a frequent exam topic, so know each one's differences and who sets the permissions.*

Access control answers three questions for every request: who are you, what are you allowed to do, and is this attempt accountable. Get identity wrong and every other control fails, because an attacker with valid credentials walks through your defenses unchallenged.

## Identity and Access Concepts

You separate four distinct steps. The exam tests whether you can tell them apart.

| Step | Question answered | Example |
|------|-------------------|---------|
| **Identification** | Who do you claim to be? | Entering a username |
| **Authentication** | Can you prove it? | Entering a password and an OTP |
| **Authorization** | What are you allowed to do? | Read a file but not delete it |
| **Accountability** | Who did what? | Audit logs tie actions to a user |

You control both **physical access** to facilities, devices, and media, and **logical access** to systems, applications, and data. Strong identity covers people, devices, and services alike.

## Authentication Strategy

You authenticate using one or more **factors**. Combining factors from different categories gives **multi-factor authentication (MFA)**.

| Factor | Category | Examples |
|--------|----------|----------|
| **Something you know** | Knowledge | Password, PIN, security question |
| **Something you have** | Possession | Hardware token, smartphone, smart card |
| **Something you are** | Inherence | Fingerprint, face, iris |
| **Somewhere you are** | Location | GPS, network location |

True **MFA** combines categories. A password plus a PIN is *not* MFA because both are knowledge factors. A password plus a hardware token is MFA.

**Passwordless** authentication removes the weakest factor, the password, and uses possession and inherence instead. **FIDO2** and **passkeys** use public-key cryptography so no shared secret can be phished or stolen from a server. For traditional passwords, follow strong practices covered in [how to create strong passwords](/articles/how-to-create-strong-passwords/).

Biometric systems are rated by two error types. The **False Acceptance Rate (FAR)** measures impostors let in. The **False Rejection Rate (FRR)** measures valid users turned away. The **Crossover Error Rate (CER)**, where FAR equals FRR, measures overall accuracy, and a lower CER is better.

## Federated Identity

**Federation** lets one set of credentials work across organizations and services.

- **Single Sign-On (SSO)** lets a user authenticate once and reach many systems without logging in again.
- **Federated Identity Management (FIM)** extends that trust across organizational boundaries.

| Protocol | Use |
|----------|-----|
| **SAML** | XML-based federation for enterprise web SSO |
| **OAuth 2.0** | Delegated authorization, granting apps limited access |
| **OpenID Connect** | Authentication layer built on OAuth 2.0 |
| **Kerberos** | Ticket-based authentication on internal networks |

*SSO is a convenience and a risk: one compromised credential reaches everything, so you pair it with strong MFA.*

## Authorization Mechanisms

**Authorization models** decide who sets permissions and how the system enforces them. This is the most tested concept in the domain.

| Model | Who decides access | Best for |
|-------|--------------------|----------|
| **DAC** (Discretionary) | The data owner | Flexible business environments |
| **MAC** (Mandatory) | The system, via labels and clearances | Military and classified data |
| **RBAC** (Role-Based) | Roles assigned to job functions | Most enterprises |
| **Rule-Based** | Global rules, like firewall ACLs | Network and time-based access |
| **ABAC** (Attribute-Based) | Attributes of user, resource, and context | Dynamic, fine-grained access |
| **Risk-Based** | Real-time risk score | Adaptive authentication |

**DAC** lets owners share their own resources, which is flexible but prone to mistakes. **MAC** enforces labels the user cannot override, which is rigid but strong. **RBAC** scales well because you manage roles, not individuals. **ABAC** is the most granular, evaluating attributes like department, device, time, and location at request time.

## Identity and Access Provisioning Lifecycle

You manage identity from hire to retire so access always matches the current role.

1. **Provisioning** grants access when a user joins, ideally automated from an HR system.
2. **Role transitions** adjust access when a user changes jobs. *Access creep* happens when you add new access but never remove the old, so you review at each move.
3. **Deprovisioning** removes all access the moment a user leaves. A forgotten account is a standing door for an attacker.
4. **Access reviews** periodically recertify that each user still needs their access.

Watch for **privilege escalation**, where a user gains rights beyond their role. *Vertical* escalation moves from a normal user to admin. *Horizontal* escalation moves to another user's access at the same level. Least privilege and regular reviews shrink this risk.

## Authentication Systems

You implement authentication across three environments and keep them consistent.

- **On-premises** systems use directory services like Active Directory with Kerberos and LDAP.
- **Cloud** systems use identity providers like Entra ID, Okta, or Google with SAML and OIDC.
- **Hybrid** systems sync identities between on-prem and cloud so users get one consistent identity everywhere.

A centralized identity provider with MFA and conditional access reduces the attack surface across all three.

## Next Steps

With identity controlled, continue to [Security Assessment and Testing](/cissp/security-assessment-and-testing/) to verify access controls work, then [Security Operations](/cissp/security-operations/) to run them day to day. Review the network controls in [Communication and Network Security](/cissp/communication-and-network-security/) and return to the [ISC2 CISSP Course](/cissp-start/).
