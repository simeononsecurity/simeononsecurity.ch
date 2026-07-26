---
title: "CompTIA SecurityX (CAS-005): Security Engineering"
date: 2025-01-01
toc: true
draft: false
description: "Master security engineering for the CompTIA SecurityX CAS-005 exam. Learn IAM troubleshooting, endpoint hardening, hardware roots of trust, OT/ICS security, enterprise automation, and advanced cryptography including post-quantum algorithms."
genre: ["CompTIA SecurityX Course", "Security Engineering", "Cryptography", "Hardware Security", "Endpoint Security", "OT Security", "Automation", "CASP+", "Enterprise Security", "Cybersecurity"]
tags: ["CompTIA SecurityX", "CASP+", "CAS-005", "security engineering", "IAM", "SAML", "Kerberos", "PAM", "EDR", "XDR", "SELinux", "TPM", "HSM", "Secure Boot", "measured boot", "OT", "ICS", "SCADA", "embedded systems", "post-quantum cryptography", "ML-KEM", "homomorphic encryption", "forward secrecy", "PBKDF2", "SOAR", "SCAP", "OVAL", "XCCDF", "tokenization", "code signing"]
cover: "/img/cover/comptia-securityx-cas-005-security-engineering.webp"
coverAlt: "A digital illustration showing interconnected servers and endpoints in a futuristic security environment, with glowing circuits and cryptographic elements against a dark background."
coverCaption: "Master Security Engineering for the CAS-005 Exam"
---

#### [Click Here to Return To the CompTIA SecurityX Course Page](/casp-plus-start/)

**Security Engineering** is **31%** of the **CompTIA SecurityX (CAS-005)** exam — the single heaviest domain. This module covers how you implement, configure, and troubleshoot the controls an architect designed. *Build deep hands-on familiarity with cryptography, hardware roots of trust, and IAM troubleshooting, because this domain rewards depth over breadth.*

Engineering is where designs meet reality. You configure identity systems, harden endpoints, root trust in hardware, secure industrial systems, automate at scale, and match the right cryptographic primitive to each job. Expect performance-based questions here — CompTIA will ask you to read output, diagnose failures, and recommend fixes.

## Troubleshooting IAM Components

You diagnose identity failures across a wide variety of protocols. Understanding the common failure mode for each is more useful on the exam than memorizing every field.

| Component | Role | Most common failure |
|-----------|------|---------------------|
| **SAML 2.0** | Web SSO via signed XML assertions | Clock skew between IdP and SP; misconfigured ACS URL |
| **OpenID Connect** | OAuth-based authentication layer | Invalid redirect URI; mismatched nonce |
| **OAuth 2.0** | Delegated authorization | Scope misconfiguration; token leakage via referrer head |
| **MFA / TOTP** | Second factor using time-based codes | Clock drift beyond the leeway window |
| **Kerberos** | Ticket-based authentication on Windows/AD | Clock skew over 5 minutes breaks TGT requests |
| **PAM** | Privileged access management and credential vaulting | Vault misconfiguration; broken session brokering |
| **802.1X** | Port-based network access control | RADIUS certificate mismatch; supplicant configuration error |
| **LDAP / AD** | Directory services | Replication failure; improper ACLs on OUs |

*Kerberos and SAML both break when system clocks drift. On the exam, when MFA or SSO is failing, check time synchronization before anything else.*

### Privileged Access Management in Depth

**PAM** platforms protect administrative accounts through:

- **Credential vaulting** — stores privileged passwords and rotates them automatically.
- **Just-in-time (JIT) access** — grants elevated rights only for the duration of an approved task, then revokes them.
- **Session recording** — captures full privileged sessions for audit and forensic review.
- **Dual control** — requires a second approver before releasing a high-value credential.

PAM is the architectural answer when the threat model includes insider threat and credential theft.

## Endpoint and Server Security

You harden the hosts where attackers land after initial access.

| Control | What it does | Stops |
|---------|-------------|-------|
| **EDR** | Records endpoint telemetry; responds to threats autonomously or with analyst guidance | Post-exploitation activity |
| **XDR** | Extends EDR across endpoints, network, cloud, and email into one correlated view | Cross-vector attacks |
| **MDR** | Managed EDR/XDR operated by a third party on your behalf | Gap when internal SOC capacity is limited |
| **Application control** | Allowlists approved executables; blocks everything else | Malware, living-off-the-land binaries |
| **HIPS/HIDS** | Monitors host activity for attack signatures or anomalies | Known exploit patterns |
| **MDM** | Enforces policy on mobile devices: encryption, PIN, remote wipe | Lost or stolen device data exposure |
| **SELinux** | Applies mandatory access control labels on Linux | Process breakout, privilege escalation |

*EDR, XDR, and MDR are frequently tested as a progression. EDR is the tool. XDR extends visibility. MDR is EDR operated by a service provider.*

### Linux Host Hardening

On Linux, you apply defense-in-depth at the kernel and process level:

- **SELinux** enforces MAC policies so a compromised nginx process cannot read `/etc/shadow`.
- **AppArmor** provides a simpler MAC alternative using path-based profiles.
- **seccomp** restricts which system calls a process may make, shrinking the kernel attack surface.
- **auditd** logs security-relevant events to a tamper-resistant log stream.

## Threat-Actor TTPs

You identify attacker behavior by mapping it to MITRE ATT&CK, the framework covered in [Governance, Risk, and Compliance](/casp-plus/governance-risk-compliance/).

| TTP Category | What attackers do | Key indicators |
|-------------|------------------|---------------|
| **Initial access** | Phishing, exploit public-facing app, valid accounts | Unusual login times, new source IPs |
| **Execution** | PowerShell, cmd, scripting engines, WMI | Encoded commands, unusual parent processes |
| **Persistence** | Scheduled tasks, registry run keys, new services | Unexpected scheduled tasks, new admin accounts |
| **Privilege escalation** | Token manipulation, UAC bypass, sudo abuse | Processes running in unexpected security contexts |
| **Credential dumping** | LSASS memory dump, SAM database, DCSync | Mimikatz signatures, unusual LSASS access |
| **Lateral movement** | Pass-the-hash, PsExec, RDP, SMB shares | Unusual inter-host connections, SMB traffic |
| **Defense evasion** | Log clearing, timestomping, process injection | Missing log entries, process hollow detection |
| **Exfiltration** | DNS tunneling, HTTPS to unusual destinations | Large outbound transfers, long DNS queries |

*Credential dumping and lateral movement are the two TTPs most central to ransomware and APT intrusions. Know how to detect them in SIEM data.*

## Network Infrastructure Security

You troubleshoot and harden the protocols that keep traffic authentic and confidential.

| Technology | Protects | Troubleshooting tip |
|-----------|----------|---------------------|
| **DNSSEC** | DNS integrity; prevents record spoofing | Check signature validation with `dig +dnssec` |
| **SPF** | Authorizes sending IPs for a domain | Too many DNS lookups (>10) cause permerror |
| **DKIM** | Signs email messages cryptographically | Key rotation must sync with DNS TTL |
| **DMARC** | Instructs receivers on SPF/DKIM failures | Start with `p=none` to observe, then enforce |
| **TLS 1.3** | Traffic confidentiality and integrity | Watch for weak cipher suites and expired certificates |
| **HSTS** | Forces HTTPS; prevents downgrade | Preload list requires minimum 1-year max-age |

```bash
# Check a domain's email authentication records during troubleshooting
dig +short TXT example.com | grep "v=spf"
dig +short TXT _dmarc.example.com
dig +short TXT selector1._domainkey.example.com
```

### Network Attack Techniques

You recognize attacks against infrastructure protocols:

- **BGP hijacking** redirects internet traffic by announcing more specific prefixes. Mitigation: RPKI route origin validation.
- **ARP poisoning** poisons the Layer 2 cache to intercept traffic on a local segment. Mitigation: dynamic ARP inspection on switches.
- **DNS spoofing** injects false DNS records. Mitigation: DNSSEC validation.
- **SSL stripping** downgrades HTTPS to HTTP. Mitigation: HSTS with preloading.

## Hardware Security Technologies

You root trust in hardware because software-only attestation can be subverted by software.

| Technology | Role | Key detail |
|-----------|------|------------|
| **TPM 2.0** | Stores keys and boot measurements on the motherboard | Cannot be extracted; tied to the physical board |
| **HSM** | Hardware appliance for high-volume cryptographic operations | FIPS 140-2/3 validated; used for CA key storage |
| **vTPM** | Software-emulated TPM for virtual machines | Provides measured boot in virtualized environments |
| **Secure Boot** | Firmware validates bootloader signatures before executing | Blocks bootkit malware |
| **Measured Boot** | Records each boot stage hash into TPM PCR registers | Enables remote attestation of boot integrity |
| **Self-encrypting drive (SED)** | Encrypts data at drive firmware level using AES | Decrypt key protected by authentication credential |

*TPM PCR registers lock boot measurements. If the boot software changes, the PCR value changes and the stored key becomes unavailable. This is the mechanism behind BitLocker's pre-boot integrity check.*

### Hardware Root of Trust

The chain of trust starts at hardware and extends to firmware, bootloader, OS, and application:

1. Firmware (UEFI) verifies the bootloader signature (Secure Boot).
2. Bootloader measures itself and components into TPM PCR registers (Measured Boot).
3. OS verifies its own components against the TPM measurements.
4. Remote attestation allows a remote verifier to confirm the chain is intact.

A broken link at any stage breaks the chain. This is why a compromised BIOS is so catastrophic.

## Specialized and Legacy Systems

You secure systems that cannot run conventional endpoint agents.

### OT, SCADA, and ICS Security

Operational technology controls physical processes in manufacturing, utilities, and transportation. These systems were designed for availability and determinism, not security.

| OT Component | Role | Security challenge |
|-------------|------|-------------------|
| **PLC** | Executes control logic for machinery | No authentication; proprietary protocols |
| **HMI** | Operator interface to SCADA | Often Windows XP-era, unpatched |
| **Historian** | Logs process data | Bridges OT and IT networks |
| **RTU** | Remote terminal unit in field devices | Low bandwidth, no encryption |

The **Purdue Model** (ICS reference architecture) organizes OT into five levels: field devices, control, supervisory, manufacturing operations, and enterprise IT. You enforce network segmentation between levels and monitor passively with OT-aware sensors. For a critical look at fundamental weaknesses in this space, read [why OT/ICS/PLC cybersecurity is fundamentally broken](/articles/ot-ics-plc-cybersecurity-fundamentally-broken/).

### IoT and Embedded Systems

- **IoT devices** ship with weak defaults, minimal update mechanisms, and no EDR. Segment them on a dedicated VLAN and monitor traffic behavior.
- **SoC and embedded systems** have constrained resources. Secure the network perimeter around them and apply firmware signing.

## Automation to Secure the Enterprise

Manual processes cannot scale. You automate repeatable security tasks.

| Tool / Framework | Use case |
|-----------------|---------|
| **PowerShell** | Windows automation, AD management, incident response scripts |
| **Bash / Python** | Log analysis, API calls, orchestration |
| **IaC (Terraform, Ansible)** | Version-controlled, repeatable infrastructure deployments |
| **SOAR** | Orchestrates playbooks; reduces analyst time per alert |
| **SCAP** | Framework for expressing security configurations and compliance checks |
| **OVAL** | Machine-readable vulnerability and configuration definitions |
| **XCCDF** | Checklist format for expressing security guidance |

For a hands-on introduction to infrastructure automation, see [Ansible for Beginners](/articles/ansible-for-beginners/).

### SOAR in the Security Operations Workflow

**SOAR** platforms automate the first response to common alert types — phishing, brute force, malware — by running predefined playbooks: isolate the endpoint, reset the credential, capture forensic data, and create a ticket. An analyst reviews the output rather than performing each step manually. The result is faster containment and consistent evidence collection.

## Advanced Cryptography

### Core Concepts

| Concept | What it does | Exam shorthand |
|---------|-------------|----------------|
| **Symmetric** | One key for encryption and decryption; fast for bulk data | AES-256, ChaCha20 |
| **Asymmetric** | Key pair; solves key distribution and digital signatures | RSA, ECDSA, Ed25519 |
| **Hashing** | One-way; produces a fixed-length digest for integrity | SHA-256, SHA-3 |
| **HMAC** | Keyed hash; adds authentication to a message digest | Used in TLS, API auth |
| **Forward secrecy** | Ephemeral keys so a stolen long-term key cannot decrypt past sessions | ECDHE in TLS 1.3 |
| **Key stretching** | Iterative hashing to slow brute force on passwords | PBKDF2, bcrypt, Argon2 |
| **Homomorphic encryption** | Compute on encrypted data without decrypting | Privacy-preserving analytics |

### Post-Quantum Cryptography

Quantum computers running Shor's algorithm can break RSA, ECC, and Diffie-Hellman. NIST finalized the first post-quantum standards in 2024:

| Algorithm | Type | Replaces |
|-----------|------|---------|
| **ML-KEM** (CRYSTALS-Kyber) | Key encapsulation / key exchange | ECDH, RSA key exchange |
| **ML-DSA** (CRYSTALS-Dilithium) | Digital signatures | ECDSA, RSA signatures |
| **SLH-DSA** (SPHINCS+) | Hash-based signatures; no lattice dependency | ECDSA (conservative backup) |

*The CAS-005 exam tests awareness of post-quantum migration, not implementation details. Know that ML-KEM and ML-DSA are the primary NIST PQC standards and that "harvest now, decrypt later" is the threat that makes migration urgent.*

### Cryptographic Use Cases

| Use case | Best approach | Why |
|---------|--------------|-----|
| **Bulk data encryption** | AES-256-GCM | Fast, authenticated encryption |
| **Key transport** | RSA-OAEP or ML-KEM | Asymmetric; keeps the key secret |
| **Digital signatures** | ECDSA or ML-DSA | Non-repudiation and integrity |
| **Password storage** | Argon2id | Memory-hard; resists GPU cracking |
| **Sensitive data in database** | Tokenization | Token has no mathematical relation to original |
| **Software distribution** | Code signing (Authenticode, GPG) | Proves source and detects tampering |
| **Long-term data confidentiality** | Post-quantum hybrid | Combine classical + PQC during migration period |

### Side-Channel Attacks

Side-channel attacks derive secrets from physical observations rather than breaking math:

- **Timing attacks** measure execution time to infer key bits.
- **Power analysis** monitors power consumption during cryptographic operations.
- **Cache-timing attacks** exploit CPU cache behavior (Spectre, Meltdown class).

Mitigations include constant-time implementations and hardware-isolated execution environments.

## Engineering Exam Tips

- Kerberos and SAML both fail on clock skew. Check NTP synchronization before deeper troubleshooting.
- TPM stores keys; HSM performs high-volume operations. Know which is appropriate for each scenario.
- Post-quantum: ML-KEM for key exchange, ML-DSA for signatures.
- Application control (allowlisting) stops living-off-the-land attacks that bypass signature-based AV.
- SELinux provides MAC; it confines processes even after compromise.
- Forward secrecy (ECDHE) prevents session decryption even if the server private key is later stolen.

## Next Steps

With controls engineered, move to [Security Operations](/casp-plus/security-operations/) to learn how to monitor, hunt, and respond to threats against these systems. Review [Security Architecture](/casp-plus/security-architecture/) for the design context behind the engineering choices. Return to the [CompTIA SecurityX Course](/casp-plus-start/) and test your readiness with the [CompTIA SecurityX Practice Test](/casp-plus-practice-test/).
