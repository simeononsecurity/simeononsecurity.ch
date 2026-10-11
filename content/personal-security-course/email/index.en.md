---
title: "Module 3: Email Security"
date: 2026-09-30
lastmod: 2026-10-10
toc: true
draft: false
description: "Secure email recovery, sessions, forwarding, aliases, remote content, OAuth access, and domain authentication through a provider-aware audit."
genre: ["Personal Security", "Email Security", "Privacy", "Account Recovery", "Data Protection"]
tags: ["email security", "email privacy", "tracking pixels", "remote content", "email aliasing", "subaddressing", "custom domain", "anonymous forwarding", "encrypted email", "secure mail provider", "remailer", "openpgp", "self-hosted mail", "spf dkim dmarc", "personal security course"]
cover: "/img/cover/email-security-strategies-protection-access.webp"
coverAlt: "An illustration showing a secure email environment with a central inbox surrounded by visual elements representing email security strategies like aliasing and subaddressing, on a dark background."
coverCaption: "Module 3: the account which unlocks the others"
---

[← Return to the Personal Security Course](/personal-security-course-start/)

**Your email account is a recovery path for many other accounts.** Password resets, fallback links, and takeover alerts often arrive there. Some services use separate recovery methods, so list each important account's real path instead of assuming email controls all of them.

This module covers address strategy, the tracking mechanisms built into mail itself, provider selection, and an honest assessment of self-hosting.

*Budget about 25 minutes. The address strategy decision is the one which compounds over years.*

## What You Will Learn

- **Explain** why mailbox compromise grants access to unrelated accounts
- **Distinguish** aliasing, subaddressing, and separate accounts as three different strategies
- **Disable** automatic remote content loading to reduce one mail tracking channel
- **Evaluate** a provider on encryption, jurisdiction, and recovery policy rather than marketing
- **Audit** third-party applications with mailbox access
- **Produce** an email record listing your address strategy, provider, and connected applications

| Term | Meaning |
|---|---|
| **Alias** | An additional address handled under provider-specific delivery, reply, and disable rules |
| **Subaddress** | A variant of your real address using a `+` suffix, which reveals the original |
| **Catch-all** | A domain configuration accepting mail to any address at the domain |
| **Tracking pixel** | A remote image request used to infer an open when the client fetches the resource |
| **Third-party access** | An application granted OAuth or IMAP permission to read your mailbox |

## Why the Mailbox Is the Master Key

**Many services route recovery through email.** Check each Tier 1 account because provider recovery methods differ.

| Attack | What It Achieves |
|---|---|
| **Mailbox takeover** | Password resets for accounts which use this address for recovery |
| **Read-only mailbox access** | Silent reconnaissance, including which services you use |
| **Mail rule insertion** | Automatic forwarding or deletion of security notifications |
| **Recovery address change** | A persistence path until the account owner or provider removes the change |

**Check your mail rules and forwarding settings today.** A malicious rule might forward or delete security alerts and remain after a password change.

*Mailbox compromise threatens accounts which accept the mailbox for recovery. Map those dependencies and secure the mailbox first.*

## Address Strategy

**One address for every service creates a shared identifier.** Three strategies change the correlation and recovery trade-offs.

| Strategy | Hides Your Real Address | Tracks Who Leaked It | Cost |
|---|---|---|---|
| **Separate accounts** | Yes, for the service | Partially | Multiple inboxes to check |
| **Aliasing** | Often, depending on reply behavior | Helps identify the address used | A provider or your own domain |
| **Subaddressing** (`you+service@`) | Usually no | Helps identify the address used | None |

**Unique aliases compartmentalize address reuse.** Subaddressing is easier where supported, but a recipient sees the base address. Alias acceptance, reply behavior, cost, and recovery differ by service.

A retired alias receiving mail is **a useful review signal**. The sender might have an old record, a forwarded message, or a leaked address. Inspect the message before labeling the sender fraudulent.

*A personal domain provides address portability. Alias and catch-all support, limits, and fees depend on the registrar and mail provider. A catch-all also receives mistyped addresses and more unwanted mail.*

## Remote Content and Tracking Pixels

**A remote image request might expose a fetch time, network address, or client detail.** Proxying, caching, privacy relays, and manual loading change which party sees which data. A fetch supports an open inference rather than proof a person read the message.

**Disable automatic remote content loading where the client supports the setting.** This reduces direct tracking requests. Some providers proxy images, and links, forms, and reply behavior still reveal activity.

Two related practices:

- **View mail as plaintext where practical.** HTML mail carries the same tracking plus additional parser attack surface.
- **Do not treat email as confidential.** Transport encryption protects the message in transit, not the copy sitting in a provider's mailbox or in a mis-sent thread.

## Provider Selection

Evaluate against these rather than marketing claims:

| Criterion | Why It Matters |
|---|---|
| **Encryption at rest** | Whether the provider holds keys to your mailbox |
| **Jurisdiction** | Which legal orders the provider responds to |
| **Recovery policy** | Whether support will restore access, and under what proof |
| **Data retention** | How long deleted mail persists in backups |
| **Third-party access control** | Whether you control which apps read your mailbox |

**Provider designs differ.** Compare key control, advertising use, retention, recovery, export, legal jurisdiction, accessibility, and third-party access. A no-advertising model removes one incentive, but does not prove security or privacy quality.

## Third-Party Access and Template Leakage

**Third-party access grants the authority shown during consent.** OAuth scopes range from profile details to broad mail read, edit, or send rights. IMAP clients often receive broad mailbox access. Review the exact grant instead of assuming one scope.

Audit this in two places:

1. **Your mail provider's connected applications list**, where old OAuth grants might remain until revoked.
2. **Your mail client's add-ins**, which run with the client's own privileges.

Two leakage channels which get far less attention:

| Channel | What It Leaks |
|---|---|
| **Auto-reply messages** | Travel dates, absence from a property, temporary contact details, and job responsibilities |
| **Mail signatures** | Job title, direct number, employer structure, and internal project names |

*An out-of-office reply exposes the absence details you include. Keep the reply to the minimum dates and contact route needed for the audience.*

## Self-Hosting: An Honest Assessment

**Running your own mail server is harder than it looks, and the difficulty is not the software.**

The technical setup is achievable. The operational burden is the problem:

- **Deliverability depends on reputation**, which requires correct SPF, DKIM, and DMARC records and a sending history which receivers trust.
- **Availability is on you.** SMTP servers often retry temporary failures, but retry windows and sender behavior vary.
- **Abuse handling is on you**, including bot attempts to relay through your server.
- **Redundancy requires planning.** One reliable MX service is valid. A second MX helps only when its filtering, authentication, and queue behavior match the design.

Two reliability items belong in any self-hosted deployment:

```text
# Check your mail authentication records before sending anything
dig +short TXT example.com              # SPF
dig +short TXT _dmarc.example.com       # DMARC policy
dig +short MX example.com               # confirm expected hosts and priorities
```

**If you are not prepared to maintain this, compare managed providers.** Review account recovery, export, encryption key control, retention, alias support, accessibility, cost, and domain portability. No provider leads on every measure.

*If you do not self-host, the portability argument returns: owning the domain means you change providers without changing your address, which is the part which matters over a decade.*

## The Email Record

```text
EMAIL RECORD
Primary provider:        ______________________
Address strategy:        separate / alias / subaddress / single
Alias provider or domain: ______________________
Retired aliases disabled: ______________________

Security settings:
  Remote content loading: OFF
  View as plaintext:      yes / no
  Recovery address:       ______________________
  Recovery phone:         current / stale / none

Third-party access (review and revoke):
  - ______________________  revoked? ______
  - ______________________  revoked? ______
```

{{< figure src="email-aliasing-versus-subaddressing-comparison.webp" alt="Diagram comparing a single email address, subaddressing, and per-service aliases, showing which strategies hide the real address and which reveal who leaked it" >}}

## Practice and Verify

Use your provider's current settings pages. Labels differ across Gmail, Outlook, Fastmail, Proton Mail, and self-hosted systems.

1. Review forwarding rules, filters, delegates, active sessions, and recovery contacts.
2. Open every connected app and read its granted OAuth scope. Revoke one unused grant.
3. Send a harmless message from a second account to a new alias or subaddress.
4. Confirm delivery, reply behavior, and the address exposed in the reply.
5. Disable automatic remote content, reopen the test message, then load images for the test message only.
6. For a personal domain, verify SPF, DKIM, and DMARC results in the received headers. Export current DNS records before editing them.

> **Expected Result:** no unknown forwarding or delegate remains, the test address works as documented, remote content waits for consent, and authentication results match the provider's setup guide.

If the alias fails, restore the prior route and check provider limits, domain verification, and reply-from support. If DMARC fails, keep policy unchanged while checking identifier alignment, not only raw SPF or DKIM pass results.

```text
REDACTED EXAMPLE
Provider:              managed provider
Alias test:            delivered and replied from alias
Remote content:        blocked by default
Unknown rules:         none
OAuth grant removed:   old calendar tool, mail scope present
SPF/DKIM/DMARC:        pass / pass / pass
Rollback:              prior DNS export stored
```

**Pass checklist**

- [ ] Recovery, sessions, forwarding, filters, and delegates received review
- [ ] Each connected app has a necessary and understood scope
- [ ] Address behavior was tested instead of assumed
- [ ] Domain authentication matches the current provider guide
- [ ] A migration rollback keeps the old mailbox available until test mail passes

**Primary references, checked 2026-10-10:** [Google account access for third-party apps](https://support.google.com/accounts/answer/14013600), [Gmail security checks](https://support.google.com/mail/answer/7036019), and [RFC 9989 DMARC](https://www.rfc-editor.org/info/rfc9989/).

## Next Steps

1. **Continue to Module 4** and apply the same privacy reasoning to conversation: **[Secure Messaging](/personal-security-course/messaging/)**
2. **Disable remote content loading** in your mail client now, which takes about thirty seconds
3. **Review connected applications** and revoke anything you no longer use
4. **Compare aliasing options** if you want a provider-managed solution rather than a domain
5. **Read the module on authentication** if recovery codes are not yet stored: **[Authentication and Credentials](/personal-security-course/authentication/)**
