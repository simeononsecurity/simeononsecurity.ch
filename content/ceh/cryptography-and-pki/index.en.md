---
title: "CEH v13: Cryptography and PKI"
date: 2025-01-01
toc: true
draft: false
description: "Master cryptography and PKI for the EC-Council Certified Ethical Hacker (CEH v13) exam. Learn symmetric and asymmetric encryption, PKI components, crypto attacks, the TLS handshake, and key management."
lastmod: 2026-10-10
genre: ["EC-Council CEH Course", "Ethical Hacking", "Penetration Testing", "Offensive Security", "Cybersecurity", "Network Security", "Security Testing", "Hacking Techniques", "CEH Certification", "Information Security"]
tags: ["CEH", "CEH v13", "ethical hacking", "EC-Council", "penetration testing", "cryptography and pki", "offensive security", "cybersecurity", "hacking", "security testing"]
cover: "/img/cover/ceh-v13-cryptography-pki-illustration.webp"
coverAlt: "An abstract illustration showing intertwined symmetric and asymmetric cryptography keys, with elements symbolizing hashing and digital signatures, set against a dark background."
coverCaption: "Master Cryptography and PKI for the CEH v13 Exam"
---

#### [Click Here to Return To the Certified Ethical Hacker (CEH v13) Course Page](/ceh-start/)

**Cryptography and PKI** closes the **EC-Council CEH v13** course. This module covers encryption types, public key infrastructure, cryptographic attacks, the TLS handshake, and key management. *Use cracking tools only against hashes and traffic you are authorized to test, because weak crypto exposes real secrets.*

Cryptography protects confidentiality and integrity, but a weak algorithm or poor key handling undoes that protection. You learn how it works and where it breaks.

## Symmetric and Asymmetric Encryption

You divide encryption by how keys are used.

| Type | Key | Examples | Use case |
|------|-----|----------|----------|
| **Symmetric** | One shared key | AES, ChaCha20 | Bulk data encryption |
| **Public-key cryptography** | Public and private pair | RSA, elliptic-curve schemes | Key agreement or transport, signatures |

Many protocols combine public-key operations with symmetric encryption. In modern TLS, ephemeral (EC)DHE key agreement commonly derives a shared secret, then symmetric keys protect application traffic. RSA key transport exists in older TLS designs, but it is not the general model for current sessions.

## Hashing and Digital Signatures

A **cryptographic hash** maps input to a fixed-length digest. Preimage resistance makes recovery of an arbitrary input computationally difficult. An attacker still tries likely inputs, so an unkeyed hash alone is unsuitable for password storage.

- **SHA-256** and **SHA-3** are current secure hashes.
- **MD5** and **SHA-1** have practical collision attacks and are unsuitable for digital signatures or other collision-sensitive security uses. They still appear as nonsecurity checksums, where an attacker-resistant digest is not required.

A **digital signature** uses a private signing key to sign a message or its digest under a defined algorithm. The verifier uses the public key to check the signature. A valid signature supports message integrity and control of the signing key. It establishes a named signer's identity only when the verifier also trusts the key-to-identity binding, such as a validated certificate. ECDSA and EdDSA do not work by encrypting a hash.

You can generate and compare hashes with the [hash calculator](/hash-calculator/) or follow the [Linux hashing guide](/guides/how-to-get-hashes-of-files-on-linux/) and the [Windows hashing guide](/guides/how-to-get-hashes-of-files-in-windows/).

## Public Key Infrastructure

**PKI** ties a public key to a verified identity through trusted authorities.

| Component | Role |
|-----------|------|
| **CA** | Certificate authority that issues and signs certificates |
| **Digital certificate** | Binds a public key to an identity |
| **CRL / OCSP** | Reports revoked certificates |
| **RA** | Registration authority that verifies requests |

When trust in a key breaks, the CA revokes the certificate and publishes it through a CRL or OCSP.

## Cryptographic Attacks

Attackers target weak algorithms, short keys, and flawed implementations.

| Attack | Target |
|--------|--------|
| **Brute force** | Short or weak keys |
| **Birthday** | Hash collisions |
| **Padding oracle** | CBC-mode decryption flaws |
| **Side-channel** | Timing and power leakage |

You crack captured password hashes in a lab with **Hashcat** or **John the Ripper**.

```bash
# Crack NTLM hashes with a wordlist
hashcat -m 1000 -a 0 hashes.txt rockyou.txt
```

## TLS and Key Management

The **TLS handshake** authenticates the server, agrees on a cipher, and derives session keys. Weak cipher suites and old protocol versions expose traffic to downgrade attacks.

- Disable **SSLv3**, **TLS 1.0**, and **TLS 1.1**.
- Enforce **forward secrecy** with ephemeral key exchange.
- Rotate keys and store them in a hardware security module.

Strong key management matters more than the algorithm, since a leaked key defeats any cipher. To build strong secrets, review [how to create strong passwords](/articles/how-to-create-strong-passwords/).

## Next Steps

You have now covered all 20 CEH v13 modules. Review the previous module on [Cloud Computing Threats](/ceh/cloud-computing-threats/), practice hashing with the [hash calculator](/hash-calculator/), and test your readiness with the [EC-Council CEH Practice Test](/ceh-practice-test/). Explore more learning paths in [Courses and Playbooks](/courses-and-playbooks/) and return to the [Certified Ethical Hacker (CEH v13) Course](/ceh-start/).
