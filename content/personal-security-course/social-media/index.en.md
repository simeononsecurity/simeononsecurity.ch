---
title: "Module 5: Social Media Privacy"
date: 2026-09-30
lastmod: 2026-10-10
toc: true
draft: false
description: "Audit profile exposure, tags, sessions, integrations, media metadata, exports, and deletion controls on each social platform you use with repeatable tests."
genre: ["Personal Security", "Social Media", "Privacy", "OPSEC", "Data Protection"]
tags: ["social media privacy", "privacy settings", "doxxing", "osint", "geolocation privacy", "metadata removal", "third party apps", "account security", "oversharing", "image cloaking", "social media permissions", "digital footprint", "personal security course"]
cover: "/img/cover/social-media-privacy-settings-review.webp"
coverAlt: "A person at a desk focused on a laptop displaying abstract icons symbolizing personal data. The dark background contrasts with vibrant colors from the screen and desk items related to privacy."
coverCaption: "Module 5: the profile is the dossier"
---

[← Return to the Personal Security Course](/personal-security-course-start/)

**A social profile is a dossier you assemble for someone else.** Individually, a birthday, a hometown, a pet's name, and a photograph of your street are trivial. Aggregated, they answer the security questions protecting your accounts and locate your home.

This module covers the two assumptions behind every post, upload discipline, permission and integration review, and when leaving a platform is the honest answer.

*Budget about 25 minutes. Review settings, outside profile view, sessions, tags, integrations, and export controls.*

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
| **OSINT** | Intelligence collected from publicly available sources for research, defense, journalism, or abuse |
| **Geotag** | Location data embedded in a post or an image file |
| **Image cloaking** | Experimental image changes intended to affect some recognition or model-training systems |
| **Third-party integration** | An external application granted access to your profile data |

## The Two Assumptions

**Assume everything is public and permanent, then decide whether to post.**

| Assumption | Why It Holds |
|---|---|
| **Public** | Platform settings change, connections reshare, and screenshots exist. Private content is frequently visible to someone |
| **Persistent** | Recipients, archives, caches, or mirrors might retain copies outside the deletion scope |

**Deletion does not erase copies held by recipients, archives, search indexes, or systems outside the platform's deletion scope.** Post from the expected audience and retention risk.

*This is not a reason to avoid social media. It is a reason to ask whether a specific post would embarrass or endanger you if it were the first result for your name.*

## Securing the Account

**Social accounts are valuable takeover targets** because they are trusted by your contacts. A compromised account sends convincing messages to people who have no reason to doubt them.

Apply Module 1 to these accounts and add two steps specific to social platforms:

- **Enable login alerts** so an unfamiliar session produces a notification
- **Review active sessions** and sign out anything you do not recognize

*An account takeover enables social engineering against everyone who trusts you, which is why a compromised profile is a risk to your contacts as much as to you.*

## What Your Profile Reveals

**Public profile details reduce the research needed for impersonation or targeted contact.** Account intrusion and data leaks create separate exposure paths.

| Detail | What It Enables |
|---|---|
| **Full name and birthday** | Identity verification and impersonation |
| **Hometown, school, first pet** | Answers to common security questions |
| **Employer and role** | Targeted business email compromise |
| **Direct email or phone** | Phishing and SIM swap attempts |
| **Daily routine and locations** | Physical risk, and empty property cues |
| **Family names and relationships** | Impersonation of people you trust |

**Truthful security-question answers might appear in public records, posts, photographs, or profiles.** Where the provider permits arbitrary answers, store unique generated responses in your vault rather than reusing biographical facts.

*Our **[Prioritized Security Checklist](/articles/personal-security-checklist-prioritized-2026/)** places this under Tier 3 in effort but notes it feeds directly into Tier 1 account recovery.*

## Upload Discipline

**Uploads expose visible context and might carry metadata.** Capture settings, file format, and platform processing decide which fields exist or survive.

### Location

Publishing a location while still there announces your presence. Publishing it while travelling announces your absence.

- **Post location-tagged content after you leave**, not during
- **Disable automatic geotagging** in the camera app and the platform
- **Check backgrounds** in photographs, which reveal street signs, house numbers, and landmarks
- **Review check-ins and tagged locations**, including ones your contacts added

*A live travel post might suggest absence from a usual location. Delay location posts when this inference creates a safety or property risk.*

### Metadata

Image files might contain metadata beyond visible pixels, including GPS coordinates, timestamps, software details, or device fields. File format, capture settings, editing, and platform processing decide what survives.

**Check before uploading** with the local **[EXIF Viewer](/exif-viewer/)**, which reads metadata without transmitting the file. Our **[URL Parser](/url-parser/)** does the equivalent for links, exposing tracking parameters appended to a shared address.

## Permissions and Integrations

**Two review tasks belong in any social media audit.**

| Target | What to Check |
|---|---|
| **App permissions** | Contacts, call log, location, photos, and microphone. Revoke what the app does not need |
| **Third-party integrations** | External services connected through social sign-in or an app grant |

**Compare dedicated accounts with social sign-in.** A dedicated account reduces provider correlation and concentration. Social sign-in might give stronger authentication and simpler recovery. Record which risk matters for each service.

Our threat model guide covers when this level of separation is justified: **[How to Form Your Own Personal Threat Model](/articles/how-to-form-your-own-personal-threat-model-safeguard-online-security/)**.

## When Leaving Is the Answer

**Some platform designs conflict with a learner's threat model.** Settings reduce selected exposure. They do not remove business-model, retention, network, or social-graph risks.

| Situation | Reasonable Response |
|---|---|
| **You post infrequently and mostly read** | Reduce to a lurking account with minimal profile detail |
| **Your profile is required for work** | Separate work and personal identities, and keep the personal one minimal |
| **You face harassment, stalking, or a public role** | Consider leaving, or maintaining a pseudonymous presence with no real details |
| **The platform uses behavioral advertising** | Review which activity supports ad selection, measurement, and data sharing under current terms |

**A pseudonymous account separates selected profile details.** A different name and browser profile reduce direct links. Network addresses, device fingerprints, recovery contacts, payments, writing style, and shared contacts still create correlation paths.

*Image cloaking is experimental. Platform recompression and model changes might reduce effectiveness. Treat the method as a research technique, not a safety control.*

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

## Practice and Verify

Choose one platform. Record the date because menu names and defaults change.

1. Review profile visibility, audience defaults, tag approval, location sharing, active sessions, and connected apps.
2. View the profile from a signed-out window or a consenting second account.
3. Remove one unnecessary public field and revoke one stale session or integration.
4. Upload a harmless test image after checking its metadata locally.
5. Download the platform's account export or confirm where the export control lives.
6. Locate deactivation and deletion controls without submitting the final deletion request.

> **Expected Result:** the outside view matches the intended audience, tags need approval where supported, no unknown session stays active, and the learner has a dated export and deletion route.

If a setting is absent, search the platform's official help center for your region and app version. If harassment or stalking is involved, preserve evidence, avoid sudden changes which increase danger, and use the platform safety center or a local specialist service.

```text
REDACTED EXAMPLE
Platform:              social network A
Outside profile view:  name and avatar only
Tag approval:          enabled
Sessions revoked:      old tablet
Connected app removed: quiz app
Export requested:      2026-10-10
Deletion route:        recorded, not submitted
```

**Pass checklist**

- [ ] A second view confirmed actual exposure
- [ ] Tag, session, and integration settings received review
- [ ] Media inspection used the original file, before upload
- [ ] Export and deletion paths are documented
- [ ] Any pseudonym plan lists remaining correlation paths

**Primary references, checked 2026-10-10:** [Apple location metadata controls](https://support.apple.com/guide/personal-safety/manage-location-metadata-in-photos-ips0d7a5df82/1.0/web/1.0) and the selected platform's official privacy and safety center.

## Next Steps

1. **Continue to Module 6** and secure the network your devices connect through: **[Home Network Security](/personal-security-course/networks/)**
2. **Check what your next upload exposes** with the **[EXIF Viewer](/exif-viewer/)**
3. **Review connected applications** and revoke anything you no longer use
4. **Remove security-question answers from your profile** and store invented ones in your vault
5. **Read the human aspect module** to see how public details feed social engineering: **[The Human Aspect](/personal-security-course/human-aspect/)**
