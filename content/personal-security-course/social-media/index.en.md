---
title: "Module 5: Social Media Privacy"
date: 2026-09-30
lastmod: 2026-09-30
toc: true
draft: false
description: "Social profiles aggregate into a detailed dossier. This module covers the two assumptions behind every post, upload discipline, permission and integration review, and when leaving is the honest answer."
genre: ["Personal Security", "Social Media", "Privacy", "OPSEC", "Data Protection"]
tags: ["social media privacy", "privacy settings", "doxxing", "osint", "geolocation privacy", "metadata removal", "third party apps", "account security", "oversharing", "image cloaking", "social media permissions", "digital footprint", "personal security course"]
cover: "/img/cover/social-media-privacy-settings-review.webp"
coverAlt: "A person at a desk focused on a laptop displaying abstract icons symbolizing personal data. The dark background contrasts with vibrant colors from the screen and desk items related to privacy."
coverCaption: "Module 5: the profile is the dossier"
---

#### [← Return to the Personal Security Course](/personal-security-course-start/)

**A social profile is a dossier you assemble for someone else.** Individually, a birthday, a hometown, a pet's name, and a photograph of your street are trivial. Aggregated, they answer the security questions protecting your accounts and locate your home.

This module covers the two assumptions behind every post, upload discipline, permission and integration review, and when leaving a platform is the honest answer.

*Budget about 25 minutes. Most of the value comes from a settings review and a single privacy decision.*

## What You Will Learn

- **Apply** the two assumptions which should govern every post
- **Explain** how scattered details aggregate into an identity profile
- **Configure** privacy, tagging, and permission settings
- **Remove** location and metadata before uploading media
- **Audit** third-party applications with profile access
- **Produce** a social media record listing your platforms, exposure level, and review date

| Term | Meaning |
|---|---|
| **Digital footprint** | The accumulated public record of your online activity |
| **OSINT** | Intelligence gathered from public sources, which is what an attacker performs on you |
| **Geotag** | Location data embedded in a post or an image file |
| **Image cloaking** | Imperceptible alterations which degrade facial recognition against your photos |
| **Third-party integration** | An external application granted access to your profile data |

## The Two Assumptions

**Assume everything is public and permanent, then decide whether to post.**

| Assumption | Why It Holds |
|---|---|
| **Public** | Platform settings change, connections reshare, and screenshots exist. Private content is frequently visible to someone |
| **Permanent** | Archives, caches, and third-party mirrors retain what you delete |

**Deletion is a request, not a guarantee.** Assume anything you post has been copied at least once.

*This is not a reason to avoid social media. It is a reason to ask whether a specific post would embarrass or endanger you if it were the first result for your name.*

## Securing the Account

**Social accounts are valuable takeover targets** because they are trusted by your contacts. A compromised account sends convincing messages to people who have no reason to doubt them.

Apply Module 1 to these accounts and add two steps specific to social platforms:

- **Enable login alerts** so an unfamiliar session produces a notification
- **Review active sessions** and sign out anything you do not recognize

*An account takeover enables social engineering against everyone who trusts you, which is why a compromised profile is a risk to your contacts as much as to you.*

## What Your Profile Reveals

**Attackers do not break in. They look you up.** A profile answers questions which would otherwise require effort.

| Detail | What It Enables |
|---|---|
| **Full name and birthday** | Identity verification and impersonation |
| **Hometown, school, first pet** | Answers to common security questions |
| **Employer and role** | Targeted business email compromise |
| **Direct email or phone** | Phishing and SIM swap attempts |
| **Daily routine and locations** | Physical risk, and empty property cues |
| **Family names and relationships** | Impersonation of people you trust |

**Security questions are the sharpest edge here.** Your mother's maiden name is often public record, your first car is often in a photograph, and your school is on your profile. Module 1's answer applies: **store invented answers in your vault** rather than true ones.

*Our **[Prioritized Security Checklist](/articles/personal-security-checklist-prioritized-2026/)** places this under Tier 3 in effort but notes it feeds directly into Tier 1 account recovery.*

## Upload Discipline

**Two details leak from every upload, and both are removable.**

### Location

Publishing a location while still there announces your presence. Publishing it while travelling announces your absence.

- **Post location-tagged content after you leave**, not during
- **Disable automatic geotagging** in the camera app and the platform
- **Check backgrounds** in photographs, which reveal street signs, house numbers, and landmarks
- **Review check-ins and tagged locations**, including ones your contacts added

*The absence signal matters more than the presence signal. A tagged holiday photograph tells a reader which property is currently unoccupied.*

### Metadata

Images carry data beyond the visible pixels, including GPS coordinates, timestamps, and device identifiers. Platforms strip some of this and not all of it.

**Check before uploading** with the local **[EXIF Viewer](/exif-viewer/)**, which reads metadata without transmitting the file. Our **[URL Parser](/url-parser/)** does the equivalent for links, exposing tracking parameters appended to a shared address.

## Permissions and Integrations

**Two review tasks belong in any social media audit.**

| Target | What to Check |
|---|---|
| **App permissions** | Contacts, call log, location, photos, and microphone. Revoke what the app does not need |
| **Third-party integrations** | Everything connected through social sign-in, which you granted once and never revisited |

**Prefer a dedicated account per service over social sign-in.** A social login links your profiles into one graph and makes a single provider compromise reach every connected service.

Our threat model guide covers when this level of separation is justified: **[How to Form Your Own Personal Threat Model](/articles/how-to-form-your-own-personal-threat-model-safeguard-online-security/)**.

## When Leaving Is the Answer

**Some platforms cannot be configured into safety**, because the business model depends on the aggregation you are trying to prevent.

| Situation | Reasonable Response |
|---|---|
| **You post infrequently and mostly read** | Reduce to a lurking account with minimal profile detail |
| **Your profile is required for work** | Separate work and personal identities, and keep the personal one minimal |
| **You face harassment, stalking, or a public role** | Consider leaving, or maintaining a pseudonymous presence with no real details |
| **The platform sells behavioral advertising** | Assume your activity is the product regardless of settings |

**A pseudonymous account is a legitimate middle path** for readers who want the content without the profile. Use a different name, no real contact details, and a separate browser container so no two identities share storage.

*Advanced readers concerned about facial recognition against existing photographs should explore image cloaking tools. The technique degrades recognition rather than preventing it, and it does not remove photographs which are already published.*

{{< figure src="social-media-profile-aggregation-osint-dossier.webp" alt="Diagram showing scattered social media details such as birthday, school, employer, and routine aggregating into a single identity dossier used for impersonation and account recovery attacks" >}}

## The Social Media Record

```text
SOCIAL MEDIA RECORD
Platforms in use:
  - ______________________  profile detail: minimal / full
  - ______________________  profile detail: minimal / full

Settings reviewed:
  Profile visibility:     public / friends / custom
  Tagging approval:       on / off
  Location & geotagging:  off / on
  Facial recognition:     off / on / unavailable

Permissions audited:
  Apps with profile access: ______  revoked: ______
  Social sign-ins in use:   ______________________

Details removed from profile:
  birthday / hometown / school / employer / phone / email
```

## Next Steps

1. **Continue to Module 6** and secure the network your devices connect through: **[Home Network Security](/personal-security-course/networks/)**
2. **Check what your next upload exposes** with the **[EXIF Viewer](/exif-viewer/)**
3. **Review connected applications** and revoke anything you no longer use
4. **Remove security-question answers from your profile** and store invented ones in your vault
5. **Read the human aspect module** to see how public details feed social engineering: **[The Human Aspect](/personal-security-course/human-aspect/)**