---
title: "Module 1: Authentication and Credentials"
date: 2026-09-30
lastmod: 2026-09-30
toc: true
draft: false
description: "Why credentials fail, how to choose between a cloud and an offline vault, which second factors stop phishing, and why recovery belongs in the same sitting as setup."
genre: ["Personal Security", "Authentication", "Password Management", "Account Security"]
tags: ["authentication", "credentials", "password manager", "passkeys", "hardware security key", "FIDO2", "2FA", "multi-factor authentication", "credential stuffing", "phishing", "backup codes", "recovery", "password hygiene", "offline password manager", "personal security course"]
cover: "/img/cover/authentication-and-credentials-digital-vault-security.webp"
coverAlt: "An illustration of a digital vault with glowing elements representing various security credentials, set against a dark background. Abstract shapes symbolize credential stuffing and phishing attacks."
coverCaption: "Module 1: credentials are the first thing an attacker tries"
---

#### [← Return to the Personal Security Course](/personal-security-course-start/)

**Authentication is where every other control begins.** An attacker who holds your credentials does not need to defeat your browser hardening, your encrypted disk, or your network segmentation. They log in as you and inherit everything.

This module covers how credentials fail, how to choose a vault, which second factors genuinely resist phishing, and why recovery configuration belongs in the same sitting as setup.

*Budget about 45 minutes. The vault decision and the second-factor upgrade are the two highest-yield actions in the entire course.*

## What You Will Learn

- **Explain** how credential stuffing turns one breach into many
- **Distinguish** cloud-synced vaults from offline vaults, including the failure mode of each
- **Rank** second factors by what they resist rather than by convenience
- **Configure** recovery so a lost device does not become a permanent lockout
- **Identify** credentials which should never enter a password manager
- **Produce** an authentication record listing your vault choice, factor per account tier, and recovery location

| Term | Meaning |
|---|---|
| **Credential stuffing** | Replaying leaked username and password pairs against other services |
| **Passphrase** | A password built from several random words, long and easy to recall |
| **Entropy** | The unpredictable content of a secret, measured in bits |
| **Origin binding** | A credential cryptographically tied to one domain, which defeats lookalike sites |
| **Recovery key** | A single-use code which restores access when the second factor is lost |
| **Vault** | The encrypted store holding your credentials |

## Why Credentials Fail

**Three mechanisms account for most account compromise, and they demand different countermeasures.**

| Attack | Mechanism | What Stops It |
|---|---|---|
| **Credential stuffing** | Replaying leaked pairs across services | Unique passwords per account |
| **Phishing** | A lookalike site collecting the password and the code | Origin-bound credentials |
| **Session theft** | Malware lifts browser cookies and reuses a live session | Nothing at the authentication layer, so endpoints matter |

The third row is the one people miss. **A stolen session cookie bypasses your password and your second factor entirely**, which is why Module 8 exists and why endpoint hygiene is not optional.

*Password reuse is the multiplier. One leaked pair becomes dozens of compromised accounts, automatically and without any further effort from the attacker.*

## Choosing a Vault

You need a manager. The only real decision is the architecture.

| | Cloud-Synced | Offline File-Based |
|---|---|---|
| **Examples** | Bitwarden, 1Password | KeePassXC, KeePassDX |
| **Sync** | Automatic across devices | Manual, or via your own storage |
| **Recovery** | Vendor-supported | Entirely your responsibility |
| **Trust** | The vendor's encryption and availability | Your own backup discipline |
| **Weakness** | Vendor outage or breach of the wrapped key | Losing the file means losing everything |
| **Best for** | Most people, especially multiple devices | Users willing to own synchronization |

**Choose cloud-synced unless you have a specific reason not to.** The security gap between a well-run vendor and a self-managed file is small. The gap between either and password reuse is enormous.

*Whichever you pick, the vault is now a single high-value target. The concentration is the trade, and it is a good one because you control the countermeasures.*

Our comparison of the two architectures: **[Best Password Managers 2026: Bitwarden vs KeePassXC](/articles/bitwarden-and-keepassxc-vs-the-rest/)**.

## The Master Password

**Your vault password is now the highest-value secret you own.** Everything else sits behind it.

Two rules follow:

- **Make it long rather than complicated.** A passphrase of five or six random words carries more entropy than a short string of symbols, and you will remember it. Guides to **[Creating Strong Passwords](/articles/how-to-create-strong-passwords/)** cover the arithmetic.
- **Never store it anywhere.** Not in the vault, not in a notes app, not in a browser. If you must write it down during the first week, keep the paper somewhere you control and destroy it once memorized.

If your manager supports it, **enable a second factor on the vault account itself**. This is the one place where a second factor protects the master credential rather than an individual site.

## Second Factors Ranked

**Second factors are not interchangeable.** They resist different attacks, and the ranking is entirely about what they stop.

| Factor | Stops Stuffing | Stops Phishing | Survives Session Theft |
|---|---|---|---|
| **SMS code** | Yes | Weakly, via SIM swap | No |
| **Email code** | Yes | Weakly, since mail is often already compromised | No |
| **Authenticator app** | Yes | Weakly, via real-time relay | No |
| **Push approval** | Yes | Weakly, via prompt bombing | No |
| **Passkey** | Yes | **Yes** | Yes |
| **Hardware key (FIDO2)** | Yes | **Yes** | Yes |

**The bottom two rows are the only phishing-resistant options.** The reason is structural. A passkey or hardware key is bound to the domain requesting it, so a lookalike site receives nothing reusable. There is no code for anyone to read aloud.

Three failure modes worth naming:

- **SIM swap** moves your number to an attacker's device, defeating every SMS factor at once. Set a carrier PIN, covered in Module 7.
- **Prompt bombing** floods you with push requests until you approve one. Number matching helps, and a passkey removes the problem.
- **Real-time relay** puts an attacker between you and the real site, forwarding your code live. Only origin binding defeats it.

*Upgrade email and finance accounts first. Those two hold the recovery paths for everything else.*

Generate and verify codes locally with the **[TOTP and HOTP Generator](/totp-generator/)**, which reads a Base32 secret or an `otpauth://` URI without sending either anywhere.

## Recovery Belongs in the Same Sitting

**Most lockouts are self-inflicted.** Someone enables a second factor, loses the device, and learns the backup codes were never saved.

Do all four steps whenever you enable a factor:

1. **Save the backup codes before closing the setup screen.** Print them or write them down, and store them **separately from your vault**, since one compromise should not yield both.
2. **Register a second key or device** where the service allows it.
3. **Remove stale recovery details.** An old phone number now belongs to someone else.
4. **Confirm which recovery contact is listed**, then update it if it is wrong.

> **Warning: support teams will not restore access to a properly secured account. Losing your only factor without backup codes frequently means losing the account permanently.**

## What Not to Store

A vault holds credentials. It should not hold everything adjacent to them.

| Item | Why It Stays Out |
|---|---|
| **Backup codes** | Storing both factors together collapses them into one |
| **Your master password** | Circular, and any breach of the vault exposes everything |
| **Full payment card details** | Use a processor or virtual cards instead, covered in Module 10 |
| **Recovery email credentials** | Keeping the recovery path separate is the point |

Also worth reviewing: **password hints and security questions**. Answers about your mother's maiden name or first car are frequently public record. If a site forces questions, **store invented answers in the vault** rather than real ones.

Two more habits from the source material deserve a mention because they cut in opposite directions:

- **Do not let a browser save passwords.** Browser stores are not consistently encrypted and are a primary target for infostealer malware.
- **Do not use your password manager to generate second-factor codes.** It concentrates both factors in one store, which converts a single compromise into a complete one.

*The counterpoint to the second item is real: a dedicated authenticator adds friction. Take the friction if you hold anything worth protecting.*

## The Authentication Record

Produce a short record before moving on. It becomes the reference for every later module.

```text
AUTHENTICATION RECORD
Vault:               ______________________  (vendor or file location)
Vault second factor: ______________________
Master password:     memorized only, not stored

Account tiers (list your accounts under each):
  Tier 1 (recovery, email, finance, identity):
    - ______________________  factor: __________
    - ______________________  factor: __________
    - ______________________  factor: __________
  Tier 2 (work, social, shopping):
    - ______________________  factor: __________
  Tier 3 (low value, no payment method stored):
    - ______________________  factor: __________

Recovery:
  Backup codes stored at:  ______________________
  Second key registered:   yes / no / unavailable
  Stale details removed:   phone / none / unknown
```

*Tier 1 deserves a hardware key or passkey. Tier 3 deserves a unique password and nothing more. Applying Tier 1 effort everywhere is how people abandon the process.*

{{< figure src="authentication-factor-tiers-and-recovery-path.webp" alt="Diagram showing account tiers from recovery and finance accounts down to low-value services, with phishing-resistant factors applied to the top tier and recovery paths stored separately from the vault" >}}

## Next Steps

1. **Continue to Module 2** and harden the browser your credentials now flow through: **[Web Browsing and Tracking](/personal-security-course/web-browsing/)**
2. **Compare vault architectures** if the choice is unresolved: **[Bitwarden vs KeePassXC](/articles/bitwarden-and-keepassxc-vs-the-rest/)**
3. **Generate the master passphrase locally** with the **[Password Generator](/password-generator/)**, which reports the entropy of your settings
4. **Check which accounts have already leaked**, so you prioritize correctly: **[Have I Been Pwned](https://haveibeenpwned.com)**
5. **Test a candidate password's strength** without transmitting it: **[Password Strength Checker](/password-checker/)**
6. **Read the organizational counterpart** if you also set password policy for others: **[Password Security Checklist](/checklists/password-security-checklist/)**