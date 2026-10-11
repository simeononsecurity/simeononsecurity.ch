---
title: "Module 7: Mobile Device Security"
date: 2026-09-30
lastmod: 2026-10-10
toc: true
draft: false
description: "Audit phone permissions, backups, carrier protections, linked devices, and emergency access on current iOS and Android without unsafe resets."
genre: ["Personal Security", "Mobile Security", "Privacy", "Android", "iOS"]
tags: ["mobile security", "phone privacy", "sim swap", "carrier pin", "app permissions", "stalkerware", "juice jacking", "mobile firewall", "custom keyboard privacy", "android privacy", "ios privacy", "custom rom", "location tracking", "personal security course"]
cover: "/img/cover/mobile-device-security-app-permissions-sim-pin.webp"
coverAlt: "A smartphone surrounded by icons of security features like app permissions, SIM PINs, and data streams, set against a dark background with vibrant colors."
coverCaption: "Module 7: the phone travels with you"
---

[← Return to the Personal Security Course](/personal-security-course-start/)

**A phone is a sensor platform which travels with you.** Depending on settings and use, apps and services derive location, access cameras or microphones, hold authenticated sessions, and receive second-factor codes. Losing control threatens accounts connected to exposed sessions and recovery paths.

This module covers carrier controls, permissions, app inventory, stalkerware safety, privileged services, and input methods.

*Budget about 30 minutes. Review carrier controls and app permissions first.*

## What You Will Learn

- **Explain** why the phone number is a security asset rather than a mere identifier
- **Configure** carrier-level protections against SIM swap
- **Audit** app permissions and background activity
- **Recognize** the indicators of stalkerware and the correct response
- **Evaluate** third-party keyboards, launchers, and input methods
- **Produce** a mobile record listing encryption status, carrier PIN, and audited permissions

| Term | Meaning |
|---|---|
| **SIM swap** | Moving your number to another SIM, which redirects calls and messages |
| **Carrier PIN** | A provider-specific account control used during selected support or transfer actions |
| **Juice jacking** | Data theft through a charging cable which also carries data |
| **Stalkerware** | Monitoring software or account access used for covert, persistent surveillance of another person |
| **Sandboxing** | Isolating an app so it cannot read other apps' data |

## Why the Phone Deserves Its Own Module

**Three properties make a phone a different risk category from a laptop.**

| Property | Consequence |
|---|---|
| **Location signals** | Apps, services, networks, and sensors might record or infer movement when access and collection are active |
| **Always-present sensors** | Camera, microphone, accelerometer, and Bluetooth radios |
| **Second-factor delivery** | SMS and push approvals might expose accounts which rely on this phone |

**Second-factor delivery creates account dependencies.** A phone might receive SMS codes, push approvals, email, or synced passkeys for selected accounts. Map which accounts depend on the device or number.

*Module 1 recommends phishing-resistant authentication where supported. A passkey might remain on or sync through the phone. A separate hardware key adds another authenticator and recovery option.*

## The Carrier Layer

**Your phone number is an asset which many services trust as proof of identity.** The trust is the vulnerability.

### Set a Carrier PIN

**Start by reviewing the controls your carrier offers.**

A carrier account PIN or number-transfer PIN adds a check to selected support and transfer workflows. Names, coverage, expiration, and reset paths differ by provider. Support-process failure still creates risk, so confirm the exact rules with your carrier.

| Attack | Effect Without a PIN | Effect With a PIN |
|---|---|---|
| **SIM swap** | Attacker receives your calls and SMS | Adds provider-specific verification |
| **Number porting** | Your number moves to another carrier | Adds transfer controls where supported |
| **Account recovery** | SMS-based recovery might route to the attacker | Carrier controls do not protect separately stored recovery codes |

Two supporting steps:

- **Request a port lock or number lock** where the provider offers one. Confirm covered transfer paths and reset rules
- **Reduce your number's exposure**, since it is both a tracking identifier and a link between datasets

**A separate recovery number has trade-offs.** Some services reject virtual numbers. Providers recycle numbers after closure, and inactivity rules differ. Prefer a phishing-resistant factor or saved recovery code where the account offers one.

*This connects directly to Module 1. SMS security depends on the provider workflow, device access, phishing resistance, message handling, and carrier account controls.*

## Permissions and App Inventory

**Every installed app is code with granted capabilities.** Review the list after major updates and when an app changes purpose.

### Start With the Inventory

- **Uninstall what you do not use.** An unused app might retain permissions, local data, background privileges, or vulnerable code
- **Prefer official app stores**, where applications are reviewed and cryptographically signed, though review is not a guarantee
- **Compare a website with a dedicated app** for occasional use. Browsers scope site permissions and storage, while installed apps receive platform permissions and background rights. Both retain selected state

### Then Audit Permissions

| Permission | Grant Only When | Warning Sign |
|---|---|---|
| **Location** | Navigation or a genuine local need | A shopping or social app requesting precise location at all times |
| **Microphone** | Voice features you use | Any app without a voice function |
| **Camera** | Photography or scanning | An app requesting camera without a stated use |
| **Contacts** | Messaging or calling apps | A game or utility reading your address book |
| **Files and photos** | Editing apps | An app requesting your entire library for one image |

**Set location to approximate rather than precise** where the platform offers the choice. A weather app does not need your street address.

Two further steps reduce background collection:

- **Restrict background activity** per app, which limits both battery drain and data collection
- **Disable connectivity you do not need.** Modern phones rotate or limit some radio identifiers, yet active radios still expand discovery and connection paths

*A restart clears selected in-memory state and interrupts some temporary activity. A restart does not remove installed malware or repair a compromised account.*

## Stalkerware

**Stalkerware describes covert monitoring used in an abuse context.** Access might come from a device installation, shared cloud account, family plan, linked service, or compromised credential. The person responsible might be known or unknown.

Indicators worth noticing:

- **Battery draining faster than usual** or the device running warm while idle
- **Unfamiliar apps**, especially ones with generic or system-sounding names
- **Settings you did not change**, particularly accessibility services and device administrators
- **Someone showing knowledge of your activity** which they should not have

**Check accessibility services and device administrators directly.** Some stalkerware abuses these broad permissions. Account and cloud access might leave no unfamiliar app on the device.

> **Warning: do not remove suspected stalkerware without a safety plan. Removal or account changes might be visible to the person monitoring the device and might affect safety or evidence. Use a safer device to seek specialist advice before acting.**

> **Safety first:** if a current or former partner might monitor the phone, use a safer device to contact a domestic violence or survivor-support service. Sudden removal, a password change, or a reset might alert the person or destroy evidence. Plan account separation, evidence needs, and emergency contact before changing the device.

## Input Methods and Physical Ports

**A third-party keyboard processes text entered through the keyboard.** Password fields and secure input receive different handling across operating systems and apps, so review the platform rules before granting full access.

| Input Method | Consideration |
|---|---|
| **Stock keyboard** | Maintained by the platform vendor and covered by system updates |
| **Third-party keyboard** | Handles ordinary input under platform rules. Secure fields and network access differ by operating system and keyboard |
| **Cloud-based prediction** | Sends context to a server to improve suggestions |

**Choose a keyboard from platform permissions, network behavior, update support, accessibility, and privacy terms.** Disable cloud features which do not serve your needs.

Two physical considerations:

- **Avoid public charging ports where possible.** A USB port carries data as well as power, so prefer your own adapter or a power-only cable
- **Evaluate erase-after-failed-attempts** if the platform supports the control. The setting limits repeated guessing but adds accidental loss and denial-of-service risk

*A longer device credential, current encryption, lock state, recovery controls, and the chosen erase setting jointly affect theft risk.*

{{< figure src="mobile-device-carrier-permission-risk-layers.webp" alt="Diagram showing mobile security layers from the carrier SIM protections at the bottom through operating system encryption, app permissions, and input methods such as keyboards" >}}

## The Mobile Record

```text
MOBILE RECORD
Device:                  ______________________
OS version:              ______________________  auto-update: on / off
Device encryption:       on / off / unknown
Lock method:             PIN (length: __) / passphrase / biometric
Erase after N attempts:  enabled / disabled

Carrier:
  Provider:              ______________________
  Carrier PIN set:       yes / no
  Port freeze:           yes / no / unavailable
  Recovery number:       separate / same as primary

Permissions audited:
  Location set to approximate: yes / no
  Apps with microphone:   ______  revoked: ______
  Apps with camera:       ______  revoked: ______
  Apps with contacts:     ______  revoked: ______

Uninstalled this session: ______________________
Accessibility services reviewed: yes / no
Keyboard:                stock / third-party: __________
```

## Practice and Verify

Use the current iOS or Android settings search because device makers rename menus.

1. Confirm the operating-system version, update status, screen lock, and backup date.
2. On iPhone, review Privacy and Security, App Privacy Report, and Safety Check where available. On Android, review Privacy Dashboard, Permission Manager, and backup settings.
3. Remove one unneeded permission. Reopen the app and test its main task.
4. Review account devices, accessibility services, device administrators, keyboards, VPNs, and management profiles.
5. Ask the carrier which account PIN, transfer PIN, port lock, and recovery controls apply. Record the official support page and date.
6. Confirm emergency contacts and one recovery route from a safer second device.

> **Expected Result:** the phone stays usable, the changed app completes its main task, backup status is current, and no unknown privileged service or account device remains.

If an app breaks, restore the single permission, then choose a less precise or while-in-use option where available. If abuse or stalkerware is suspected, stop the exercise. Use a safer device and a specialist safety plan before removing software, resetting accounts, or erasing evidence.

```text
REDACTED EXAMPLE
Platform/version:      Android [version removed]
Backup date:           2026-10-09
Permission changed:    shopping app, precise to approximate
Function retest:       passed
Privileged services:   expected only
Carrier controls:      account PIN yes, transfer PIN expires
Emergency access:      trusted contact reviewed
```

**Pass checklist**

- [ ] Update, lock, backup, recovery, and account-device status are recorded
- [ ] Permission changes have a function retest
- [ ] Accessibility, administrators, keyboards, VPNs, and profiles contain no unknown entry
- [ ] Carrier behavior comes from current provider guidance
- [ ] A survivor-safety plan replaces abrupt device changes when monitoring is suspected

**Primary references, checked 2026-10-10:** [Apple Safety Check](https://support.apple.com/guide/personal-safety/ips2aad835e1/web), [Android Privacy Dashboard](https://support.google.com/android/answer/13530434), [Android backup and restore](https://support.google.com/android/answer/12461238), and [FCC SIM-swap and port-out proceeding](https://docs.fcc.gov/public/attachments/FCC-21-102A1.pdf).

## Next Steps

1. **Continue to Module 8** and secure the machine your accounts and files live on: **[Personal Computer Security](/personal-security-course/personal-computers/)**
2. **Review carrier account and transfer controls** through the provider's official support path
3. **Audit accessibility services and device administrators** for anything you did not enable
4. **Switch location permissions to approximate** for apps which do not need precision
5. **Review your keyboard** and disable cloud prediction if you keep a third-party one
6. **Read the organizational counterpart**: **[Mobile Device Security Checklist](/checklists/mobile-device-security-checklist/)**
