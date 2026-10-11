---
title: "Module 1: Authentication and Credentials"
date: 2026-09-30
lastmod: 2026-10-10
toc: true
draft: false
description: "Learn how passwords, passkeys, MFA, vaults, and account recovery work. Build and test a safer authentication plan without exposing secrets, with clear evidence."
genre: ["Personal Security", "Authentication", "Password Management", "Account Security"]
tags: ["authentication", "credentials", "password manager", "passkeys", "hardware security key", "FIDO2", "2FA", "multi-factor authentication", "credential stuffing", "phishing", "backup codes", "recovery", "password hygiene", "offline password manager", "personal security course"]
cover: "/img/cover/authentication-and-credentials-digital-vault-security.webp"
coverAlt: "An illustration of a digital vault with glowing elements representing various security credentials, set against a dark background. Abstract shapes symbolize credential stuffing and phishing attacks."
coverCaption: "Module 1: credentials are the first thing an attacker tries"
---

[← Return to the Personal Security Course](/personal-security-course-start/)

**Authentication controls access to accounts and recovery paths.** A valid credential might let an attacker bypass controls on your own browser, disk, or network. Provider risk checks, session policy, authorization, and later verification still shape access.

This module covers how credentials fail, how to choose a vault, which second factors genuinely resist phishing, and why recovery configuration belongs in the same sitting as setup.

*Budget about 45 minutes. Start with the vault, high-value account factors, sessions, and recovery.*

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
| **Origin binding** | A credential cryptographically tied to one domain, which resists credential phishing on a lookalike site |
| **Recovery key** | A single-use code which restores access when the second factor is lost |
| **Vault** | The encrypted store holding your credentials |

## Why Credentials Fail

**Three common account attacks demand different countermeasures.**

| Attack | Mechanism | What Stops It |
|---|---|---|
| **Credential stuffing** | Replaying leaked pairs across services | Unique passwords per account |
| **Phishing** | A lookalike site collecting the password and the code | Origin-bound credentials |
| **Session theft** | Malware or another attacker obtains a valid session token | Session protection, revocation, reauthentication, and endpoint controls |

**A valid stolen session token might provide access without a fresh password or factor prompt.** Provider controls, token scope, expiration, reauthentication, and revocation decide the result.

*Password reuse lets an attacker test one leaked pair against other services. Unique credentials limit the number of accounts exposed by one password leak.*

## Choosing a Vault

A password manager supports unique credentials. Choose its architecture, recovery design, platform support, and sharing model from your needs.

| | Cloud-Synced | Offline File-Based |
|---|---|---|
| **Examples** | Bitwarden, 1Password | KeePassXC, KeePassDX |
| **Sync** | Automatic across devices | Manual, or via your own storage |
| **Recovery** | Vendor-supported | Entirely your responsibility |
| **Trust** | The vendor's encryption and availability | Your own backup discipline |
| **Weakness** | Vendor outage or failure in the service or client design | Losing every copy of the file or key blocks recovery |
| **Common fit** | People who want managed multi-device sync | People willing to own synchronization and backups |

**Choose the design you will maintain and recover.** Compare vendor trust, local backup skill, device support, sharing needs, offline access, and recovery before choosing cloud sync or an offline file.

*Whichever you pick, the vault is now a single high-value target. The concentration is the trade, and it is a good one because you control the countermeasures.*

Our comparison of the two architectures: **[Best Password Managers 2026: Bitwarden vs KeePassXC](/articles/bitwarden-and-keepassxc-vs-the-rest/)**.

## The Master Password

**Your vault password protects a concentrated credential store.** Give its recovery and endpoint security the same care as the vault itself.

Two rules follow:

- **Prefer length over complexity.** A password manager generated value avoids reuse. A multiword passphrase suits a secret you need to enter from memory. Guides to **[Creating Strong Passwords](/articles/how-to-create-strong-passwords/)** cover the arithmetic.
- **Choose a controlled recovery copy.** A sealed paper copy in a locked place helps some households avoid permanent lockout. A person facing theft or coercion might reject this option. Record the choice and storage location without writing the secret in this course record.

If your manager supports the feature, **enable a second factor on the vault account**. The factor protects access to the provider account. Local vault access behavior depends on the product design.

## Second Factors Ranked

**Second factors are not interchangeable.** They resist different attacks, and the ranking is entirely about what they stop.

| Factor | Stops Stuffing | Phishing Resistant | Stops Session Theft |
|---|---|---|---|
| **SMS code** | Yes | No, codes remain phishable and relayable | No |
| **Email code** | Yes | No, codes remain phishable and relayable | No |
| **Authenticator app** | Yes | No, codes remain phishable and relayable | No |
| **Push approval** | Yes | Depends on the protocol and verification flow | No |
| **Passkey** | Yes | **Yes, when implemented with verifier binding** | No |
| **Hardware key (FIDO2)** | Yes | **Yes, when implemented with verifier binding** | No |

**Passkeys and FIDO2 security keys provide common consumer phishing-resistant options.** NIST also recognizes other cryptographic methods. Verifier binding prevents a lookalike origin from receiving a valid reusable authentication output. These factors do not by themselves invalidate a session token stolen after login.

Three failure modes worth naming:

- **SIM swap** moves your number to an attacker's device and threatens accounts which accept SMS to the number. Set available carrier account and transfer protections, covered in Module 7.
- **Prompt bombing** floods you with push requests until you approve one. Number matching helps. A passkey flow which replaces approval prompts removes this path from the selected login flow.
- **Real-time relay** puts an attacker between you and the real site, forwarding a code live. Verifier-bound cryptographic authentication resists this path.

*Prioritize accounts which hold recovery paths or financial value. Email and finance accounts often belong near the top after you map your own dependencies.*

Generate and verify codes locally with the **[TOTP and HOTP Generator](/totp-generator/)**, which reads a Base32 secret or an `otpauth://` URI without sending either anywhere.

## Recovery Belongs in the Same Sitting

**Recovery planning prevents avoidable lockout.** A lost device becomes a serious problem when no saved code, second authenticator, recovery contact, or provider process exists.

Use the supported steps when you enable a factor:

1. **Save the backup codes before closing the setup screen.** Print them or write them down, and store them **separately from your vault**, since one compromise should not yield both.
2. **Register a second key or device** where the service allows it.
3. **Remove stale recovery details.** A disconnected number might be reassigned, while an obsolete address or contact might no longer be trustworthy.
4. **Confirm which recovery contact is listed**, then update it if it is wrong.

> **Warning: recovery differs by provider.** Some services use saved codes, recovery contacts, identity proofing, or support review. Confirm the real process before removing an old factor.

## What Not to Store

A vault holds credentials. It should not hold everything adjacent to them.

| Item | Why It Stays Out |
|---|---|
| **Backup codes** | Separate storage limits one compromise, while vault storage reduces loss risk. Choose from your threat model |
| **Your master password** | A sealed offline copy supports recovery. Store the copy away from the device and document who has access |
| **Full payment card details** | Vault storage adds convenience and concentration risk. A processor or virtual card gives another option |
| **Recovery email credentials** | Separation limits one compromise. A secured vault reduces forgotten-password risk |

Also review **password hints and security questions**. Biographical answers might appear in records, posts, profiles, or photographs. If a site permits arbitrary answers, **store unique generated responses in the vault** rather than reusing real facts.

Two more habits deserve a mention because they cut in opposite directions:

- **Review the browser vault before use.** Modern browser password stores often use operating-system or account protection. A dedicated manager gives clearer cross-browser controls. Endpoint malware still threatens both designs.
- **Choose where TOTP codes live.** A separate authenticator limits vault concentration. Vault-held codes reduce lockout and setup friction. Record the trade-off for each high-value account.

*The counterpoint to the second item is real: a dedicated authenticator adds friction. Take the friction if you hold anything worth protecting.*

## The Authentication Record

Produce a short record before moving on. It becomes the reference for every later module.

```text
AUTHENTICATION RECORD
Vault:               ______________________  (vendor or file location)
Vault second factor: ______________________
Master password recovery copy: none / sealed offline / trusted custodian

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

*Prioritize phishing-resistant authentication for high-impact accounts where supported. Give each lower-impact account a unique credential, then add available factors when account value, recovery dependencies, or the threat model justify them.*

{{< figure src="authentication-factor-tiers-and-recovery-path.webp" alt="Diagram showing account tiers from recovery and finance accounts down to low-value services, with phishing-resistant factors applied to the top tier and recovery paths stored separately from the vault" >}}

## Practice and Verify

Use a low-value account first. Do not paste a password, recovery code, QR code, or secret key into the record.

1. Open the provider's security page from a saved bookmark.
2. Record the current factors, recovery contacts, and active sessions.
3. Add a second factor only after saving a recovery method.
4. Sign out of a separate browser profile, then sign back in with the new factor.
5. Revoke the test session from the provider's session list.

> **Expected Result:** the new login asks for the selected factor, the recovery method appears in account settings, and the revoked session loses access after refresh.

If the factor prompt never appears, check whether the provider enrolled the factor for login or recovery only. If session revocation leaves the test session active, wait for the provider's stated delay, refresh, then use the sign-out-all-sessions control. Stop before removing the old factor when no tested recovery path exists.

```text
REDACTED EXAMPLE
Account tier:          1, primary email
Primary factor:        synced passkey
Fallback:              hardware key
Recovery copy:         sealed offline, locked location
Test login:            passed 2026-10-10
Session revocation:    passed after refresh
```

**Pass checklist**

- [ ] One unique credential or passkey protects each reviewed account
- [ ] Every Tier 1 account has a tested factor and a documented recovery path
- [ ] The record reveals no secrets
- [ ] A lost device does not remove every authenticator
- [ ] A stolen session has a documented revocation route

**Primary references, checked 2026-10-10:** [NIST SP 800-63B authentication and recovery](https://pages.nist.gov/800-63-4/sp800-63b.html) and [CISA multifactor authentication guidance](https://www.cisa.gov/secure-our-world/turn-mfa).

## Next Steps

1. **Continue to Module 2** and harden the browser your credentials now flow through: **[Web Browsing and Tracking](/personal-security-course/web-browsing/)**
2. **Compare vault architectures** if the choice is unresolved: **[Bitwarden vs KeePassXC](/articles/bitwarden-and-keepassxc-vs-the-rest/)**
3. **Generate the master passphrase locally** with the **[Password Generator](/password-generator/)**, which reports the entropy of your settings
4. **Check which accounts have already leaked**, so you prioritize correctly: **[Have I Been Pwned](https://haveibeenpwned.com)**
5. **Test a candidate password's strength** without transmitting it: **[Password Strength Checker](/password-checker/)**
6. **Read the organizational counterpart** if you also set password policy for others: **[Password Security Checklist](/checklists/password-security-checklist/)**
