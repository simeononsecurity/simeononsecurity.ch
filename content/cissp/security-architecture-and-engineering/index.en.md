---
title: "ISC2 CISSP: Security Architecture and Engineering"
date: 2025-01-01
toc: true
draft: false
description: "Master Security Architecture and Engineering for the ISC2 CISSP exam. Learn secure design principles, security models, cryptographic solutions, cryptanalytic attacks, and physical security."
genre: ["ISC2 CISSP Course", "Security Architecture", "Security Engineering", "Cryptography", "Physical Security", "ISC2 Certification", "Information Security", "Security Models", "Zero Trust", "Cybersecurity"]
tags: ["ISC2 CISSP", "CISSP", "security architecture", "secure design", "Bell-LaPadula", "Biba", "TPM", "cryptography", "PKI", "cryptanalytic attacks", "physical security", "defense in depth", "zero trust"]
cover: "/img/cover/isc2-cissp-security-architecture-engineering.webp"
coverAlt: "An illustration of a secure data center featuring server racks, security cameras, and digital locks, layered with vibrant colors representing different security measures and technologies."
coverCaption: "Master Security Architecture and Engineering for the CISSP Exam"
---

#### [Click Here to Return To the ISC2 CISSP Course Page](/cissp-start/)

**Security Architecture and Engineering** is **13%** of the **ISC2 CISSP** exam. This module covers how you design systems that stay secure by default, the formal models that prove a design works, and the cryptography that protects data everywhere. *Cryptography questions appear across the whole exam, so build a solid mental model here and the rest of the test gets easier.*

A secure system is engineered, not bolted on. You decide the trust boundaries, the controls, and the failure behavior before the first line of code or the first server rack. This domain rewards understanding why a control exists more than memorizing the control itself.

## Secure Design Principles

**Secure design principles** are the rules you apply to every architecture decision. They keep a system safe even when one control fails.

- **Threat modeling** maps what you are protecting, who wants it, and how they could get it before you build. **STRIDE** and **PASTA** are common methods.
- **Least privilege** gives each user, process, and service only the access it needs to do its job, and nothing more.
- **Defense in depth** stacks independent controls so a single failure does not breach the system. A firewall, network segmentation, host hardening, and encryption all guard the same asset.
- **Secure defaults** ship a system locked down. The user opts in to risk rather than opting out of it.
- **Fail securely** means a crash or error denies access rather than granting it. A failed authentication check defaults to "deny."
- **Zero trust** removes implicit trust based on network location. You verify every request with identity, device posture, and context. The model summary is *never trust, always verify*.
- **Privacy by design** builds data protection into the system from the start, including data minimization and purpose limitation.

The difference between **fail-secure** and **fail-safe** is an exam favorite. *Fail-secure* protects data and denies access on failure. *Fail-safe* protects people and may unlock doors during a fire. You choose based on whether life safety or asset protection comes first.

## Security Models

**Security models** are formal rules that define how a system enforces a security policy. The exam tests whether you know which property each model protects.

| Model | Protects | Core rules |
|-------|----------|-----------|
| **Bell-LaPadula** | Confidentiality | No read up, no write down (the "no read up, no write down" rule) |
| **Biba** | Integrity | No read down, no write up |
| **Clark-Wilson** | Integrity | Enforces well-formed transactions and separation of duties |
| **Brewer-Nash (Chinese Wall)** | Conflict of interest | Access changes dynamically to prevent conflicts |

Remember **Bell-LaPadula** with "no write down" (the *Star Property*) protects secrets from leaking to lower levels. **Biba** flips it: "no write up" stops low-integrity data from corrupting trusted data. The **Star Model** notation (the * property) shows up in both, so read the question to see whether it asks about confidentiality or integrity.

## Security Capabilities of Information Systems

Hardware and firmware enforce security the operating system alone cannot.

- **Memory protection** isolates one process from another so a crash or exploit in one cannot read or write another's memory. Techniques include **ASLR** and the **NX bit**.
- **Trusted Platform Module (TPM)** is a hardware chip that stores cryptographic keys, measures boot integrity, and supports full-disk encryption like **BitLocker**.
- **Hardware Security Module (HSM)** is a dedicated appliance for generating, storing, and using keys at scale.
- **Trusted execution environments** run sensitive code in an isolated processor region.

## Cryptographic Solutions

You select **cryptographic solutions** based on what you protect and the data state. Cryptography provides confidentiality, integrity, authentication, and non-repudiation.

The **cryptographic lifecycle** governs a key from creation to destruction: generation, distribution, storage, use, rotation, revocation, and destruction. Weak key management defeats strong algorithms.

| Type | How it works | Example algorithms | Best for |
|------|--------------|--------------------|----------|
| **Symmetric** | One shared key encrypts and decrypts | AES, ChaCha20 | Bulk data encryption, speed |
| **Asymmetric** | Public/private key pair | RSA, ECC | Key exchange, digital signatures |
| **Elliptic curve (ECC)** | Asymmetric with smaller keys | ECDSA, ECDH | Mobile and IoT, strong security per bit |
| **Hashing** | One-way fixed-length digest | SHA-256, SHA-3 | Integrity, password storage |

**Symmetric** encryption is fast but has a key distribution problem: every pair of parties needs a shared secret. **Asymmetric** solves distribution but is slow, so real systems use a hybrid approach. **TLS** exchanges a symmetric session key using asymmetric crypto, then encrypts the session with the fast symmetric key.

**Quantum** computing threatens current asymmetric algorithms. *Post-quantum cryptography* like the NIST-selected **ML-KEM** (Kyber) resists quantum attacks, so plan migration now for long-lived secrets.

**Public Key Infrastructure (PKI)** ties a public key to a verified identity using **digital certificates** signed by a **Certificate Authority (CA)**.

```bash
# Generate a private key and a certificate signing request with OpenSSL
openssl req -newkey rsa:4096 -keyout private.key -out request.csr

# Inspect a certificate to verify issuer, subject, and validity dates
openssl x509 -in certificate.crt -text -noout
```

A relying party trusts a certificate by following the **chain of trust** up to a trusted **root CA**. Revoked certificates appear in a **Certificate Revocation List (CRL)** or are checked in real time with **OCSP**.

## Cryptanalytic Attacks

**Cryptanalytic attacks** try to break encryption or the systems around it. The exam tests recognition of each by its description.

| Attack | Method |
|--------|--------|
| **Brute force** | Try every possible key until one works |
| **Ciphertext only** | Attacker has only encrypted data and looks for patterns |
| **Known plaintext** | Attacker has matching plaintext and ciphertext pairs |
| **Chosen plaintext** | Attacker encrypts chosen data to study the output |
| **Side-channel** | Measure power, timing, or emissions to recover keys |
| **Fault injection** | Induce hardware errors to expose secrets |
| **Timing** | Measure how long operations take to infer key bits |
| **Man-in-the-middle (MITM)** | Intercept and relay traffic between two parties |
| **Pass the hash** | Reuse a captured password hash without cracking it |
| **Ransomware** | Encrypt a victim's data and demand payment for the key |

Defenses include strong key lengths against **brute force**, constant-time operations against **timing** attacks, certificate pinning against **MITM**, and offline backups against **ransomware**.

## Site and Facility Security

You apply security principles to physical design because an attacker with physical access often wins.

- **Wiring closets** and **server rooms** need locked doors, access logging, and limited entry.
- **Media storage** facilities control temperature, humidity, and access to backup tapes and drives.
- **Fire prevention** uses detection, suppression, and the right agent. Server rooms use clean-agent or gas suppression rather than water to protect equipment.
- **Power redundancy** uses UPS systems for short outages and generators for long ones.
- **HVAC** keeps equipment within safe operating ranges.

**Crime Prevention Through Environmental Design (CPTED)** uses layout, lighting, and natural surveillance to deter intruders before they reach a door.

## Information System Lifecycle

You manage systems from cradle to grave so security stays current.

1. **Requirements analysis** defines security needs alongside business needs.
2. **Design and development** build controls in from the start.
3. **Testing and acquisition** validate the controls work.
4. **Operations and maintenance** patch, monitor, and reassess.
5. **Disposal** sanitizes media and decommissions hardware securely.

Secure disposal closes the loop with [Asset Security](/cissp/asset-security/), where data remanence and destruction are covered in depth.

## Next Steps

With secure design and cryptography mastered, continue to [Communication and Network Security](/cissp/communication-and-network-security/) to apply these principles to networks, then [Identity and Access Management](/cissp/identity-and-access-management/) to control who reaches your systems. Ground this domain in [Security and Risk Management](/cissp/security-and-risk-management/) and return to the [ISC2 CISSP Course](/cissp-start/). Review [tips for passing certification exams](/articles/tips-and-tricks-for-passing-comptia-exams/) before test day.
