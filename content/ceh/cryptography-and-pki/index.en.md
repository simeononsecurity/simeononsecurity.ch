title: "CEH v13: Cryptography and PKI"
date: 2025-01-01
toc: true
draft: false
description: "Master cryptography and PKI for the EC-Council Certified Ethical Hacker (CEH v13) exam. Learn symmetric and asymmetric encryption, PKI components, crypto attacks, the TLS handshake, and key management."
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
| **Asymmetric** | Public and private pair | RSA, ECC | Key exchange, signatures |

Most systems combine both. Asymmetric crypto exchanges a key, then fast symmetric crypto encrypts the data.

## Hashing and Digital Signatures

A **hash** produces a fixed-length fingerprint of data. It is one-way, so you cannot reverse it to the original input.

- **SHA-256** and **SHA-3** are current secure hashes.
- **MD5** and **SHA-1** are broken and must not be used.

A **digital signature** hashes a message, then encrypts the hash with a private key. The receiver verifies it with the public key, which proves integrity and authenticity.

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
