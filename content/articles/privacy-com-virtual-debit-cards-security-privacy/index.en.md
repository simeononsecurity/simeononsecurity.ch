---
title: "Privacy.com Virtual Cards: How Payment Privacy Works"
date: 2023-09-03
lastmod: 2026-10-02
toc: true
draft: false
description: "What is stored on a payment card, why the magnetic stripe is the weakest part of it, what a merchant sees when you pay with a virtual number, and how Privacy.com's card types and limits work in practice."
genre: ["Payment Security", "Digital Privacy", "Virtual Cards", "Financial Privacy", "Fraud Prevention", "Consumer Security"]
tags: ["privacy.com", "virtual cards", "virtual debit cards", "single use cards", "merchant locked cards", "category locked cards", "tokenization", "network token", "pan", "cvv", "card skimming", "magnetic stripe", "track 1", "track 2", "payment card security", "credit card fraud", "subscription management", "spend limits", "pci dss", "soc 2", "card not present fraud", "financial privacy", "payment privacy", "virtual card number", "masked card", "card controls"]
cover: "/img/cover/privacy_virtual_cards.webp"
coverAlt: "A digital illustration showing a shielded virtual card protecting a lock symbol, representing the security and privacy offered by virtual debit cards."
coverCaption: "Protect, Control, and Secure Your Online Transactions."
ref: ["/magnetic-stripe-decoder", "/articles/personal-security-checklist-prioritized-2026", "/personal-security-course/personal-finance"]
---

**A virtual card does one specific thing: it changes what the merchant receives, not what your bank knows.** This is the entire mechanism, and understanding it explains both the protection you get and the protection you do not.

Most coverage treats virtual cards as a general privacy tool and skips the technical detail. This article covers what is stored on a card, why the magnetic stripe is the weak point, and how Privacy.com's card types behave in practice.

*The practical payoff is narrow and real: a stolen number becomes useless to a thief, because it only works at the merchant it was issued for.*

## The Short Answer

| Question | Short Answer |
|---|---|
| **What does a virtual card change?** | The number the merchant stores. Your real card details never reach them |
| **Is the transaction private?** | No. Your bank, the network, and the issuer still see it |
| **What stops a breach hurting you?** | A merchant-locked or single-use number, which fails anywhere else |
| **What is the weakest part of a physical card?** | The magnetic stripe, which stores the full track data unencrypted |
| **Does it build credit?** | No. These are not credit accounts and no credit pull occurs |
| **Who qualifies for Privacy.com?** | US citizens or legal residents, 18+, with a US bank or credit union checking account |

## What Is on a Payment Card

**Three things authorise a card-not-present transaction: the primary account number, the expiry date, and the verification value.**

| Element | Length | Where It Comes From |
|---|---|---|
| **Primary Account Number (PAN)** | Up to 19 digits | The issuer, with leading digits identifying the scheme and bank |
| **Expiry** | Four digits as MM/YY | The issuer |
| **CVV or CVC** | Three or four digits | Derived from the PAN, expiry, and a key only the issuer holds |
| **Cardholder name** | Up to 26 characters | Appears only on Track 1 of the magnetic stripe |

**The PAN is not a random string.** The first digit identifies the scheme, the next several identify the issuing bank, and the remainder identifies the account. The structure means a card number is checked for plausibility without contacting anyone, and why the Luhn check digit catches a single transposed digit.

**The CVV is what proves someone physically held the card** when it was issued. It is not stored on the magnetic stripe, which is exactly why a skimmer copying the stripe never obtains it.

*Inspect all of this yourself with the **[Magnetic Stripe Decoder and Encoder](/magnetic-stripe-decoder/)**, which parses Track 1 and Track 2, decodes the service code digits, and re-encodes the result. It runs entirely in your browser, which matters because this is the full contents of a payment card.*

{{< figure src="payment-card-data-anatomy-pan-cvv-tracks.webp" alt="Diagram showing the elements of a payment card including the primary account number, expiry date, CVV, and the three magnetic stripe tracks with what each one carries" >}}

## Why the Magnetic Stripe Is the Weak Point

**The stripe stores account data in plaintext, and any compatible reader reads it.**

A magnetic stripe holds up to three tracks. Track 1 carries the PAN, the cardholder name, the expiry, and a three-digit service code, and it is the only track holding alphabetic text. Track 2 carries the PAN, expiry, and service code in a denser numeric encoding, and **Track 2 is what almost every point-of-sale terminal reads.** Track 3 is effectively unused by the major networks and is often not present on the card at all.

The service code is worth understanding, because it describes the card's permitted use. Digit one covers interchange rules, digit two covers authorization handling, and digit three covers the range of services. A card coded `201` permits international interchange, needs no special authorization path, and carries no service restrictions.

The history explains why the stripe lasted so long. In 1969 an IBM engineer named Forrest Parry tried to attach magnetic tape to a plastic card and failed to get it to adhere without damaging it. His wife suggested using a clothes iron, and the heat bonded the tape to the card. The improvisation became the standard for over half a century.

Two developments are ending it:

| Milestone | Status |
|---|---|
| **Mastercard announced the stripe's removal** | By 2033, no Mastercard credit or debit cards will carry one |
| **Europe** | Stripes began disappearing from Mastercard cards in 2024 |
| **United States** | Banks to stop issuing them starting 2027 |

*The stripe was replaced by chip and contactless payment because copying one requires no skill beyond owning a reader. Our **[magnetic stripe tool](/magnetic-stripe-decoder/)** shows how little data is needed to reconstruct a working track.*

{{< figure src="magnetic-stripe-track-layout-track1-track2.webp" alt="Diagram of a magnetic stripe showing the physical position of tracks one, two and three, with the field layout of each track including sentinels, PAN, name, expiry and service code" >}}

## How to Read Track Data

**A magnetic-stripe string is a sequence of fields, not a second card number.** The reader finds the start sentinel, separates fields, reads the expiry and service code, then checks the end sentinel and LRC.

| Track | Start | Main fields | End | Character set |
|---|---|---|---|---|
| **Track 1** | `%` | Format code, PAN, name, expiry, service code, discretionary data | `?` plus LRC | Six-bit ALPHA, so it carries letters |
| **Track 2** | `;` | PAN, expiry, service code, discretionary data | `?` plus LRC | Four-bit BCD, so it carries digits and a small punctuation set |

The optional sentinels identify the physical record boundaries. A decoder often omits them when it displays the fields, but a physical encoder needs the complete record format expected by the reader.

### Track 1 Example

This is a synthetic example. It uses the standard test PAN from the tool and fake name, expiry, service code, and discretionary data. It is not a Privacy.com card and it is not valid payment data.

```text
%B4111111111111111^TEST/USER^2912501000000000?
```

Read it from left to right:

| Segment | Value | Meaning |
|---|---|---|
| **Start sentinel** | `%` | Track 1 record begins |
| **Format code** | `B` | Financial-card format B |
| **PAN** | `4111111111111111` | Synthetic primary account number |
| **Field separator** | `^` | PAN ends and name begins |
| **Name** | `TEST/USER` | Surname, separator, first name |
| **Field separator** | `^` | Name ends and transaction fields begin |
| **Expiry** | `2912` | December 2029 in YYMM form |
| **Service code** | `501` | National interchange, normal processing, no restrictions |
| **Discretionary data** | `0000000` | Issuer-defined filler in this example |
| **End sentinel** | `?` | Track 1 data ends before the LRC |

The real encoded record also carries an LRC character after the end sentinel when the reader expects it. The visible text form is useful for studying structure. The bit-level representation also carries odd parity for each character.

### Track 2 Example

Track 2 removes the name and format code. The same synthetic values become:

```text
;4111111111111111=291250100000000?
```

| Segment | Value | Meaning |
|---|---|---|
| **Start sentinel** | `;` | Track 2 record begins |
| **PAN** | `4111111111111111` | Synthetic primary account number |
| **Separator** | `=` | PAN ends and transaction fields begin |
| **Expiry** | `2912` | December 2029 in YYMM form |
| **Service code** | `501` | Same synthetic service code as Track 1 |
| **Discretionary data** | `0000000` | Issuer-defined filler in this example |
| **End sentinel** | `?` | Track 2 data ends before the LRC |

**Track 2 is shorter because it has no cardholder name.** Many terminals read Track 2 for ordinary swipe transactions, while Track 1 provides the name field when a reader requests it.

### Service-Code Digits

**The three service-code digits describe terminal and authorization behavior.** They do not contain the CVV, and changing them on a real card without issuer authorization produces a malformed or misleading payment credential.

| Digit | Example values | What it describes |
|---|---|---|
| **First** | `1`, `2`, `5`, `6`, `7`, `9` | Interchange rules and whether chip use is preferred |
| **Second** | `0`, `2`, `4` | Normal processing or online issuer contact |
| **Third** | `0` through `7` | PIN, cash, goods-and-services, and other restrictions |

For example, `201` means international interchange with chip use where feasible, normal authorization processing, and no service restrictions. The decoder exposes each digit separately so you do not have to memorize the table.

### LRC and Parity

**The LRC is a check character, not another field to invent.** The encoder XORs the data value of each character from the start sentinel through the end sentinel. It converts the result back into the track's printable character range and reports the encoded odd-parity bits separately.

Track 1 uses a six-bit ALPHA character set. Its data value is the ASCII code minus `0x20`. Track 2 uses a four-bit BCD character set. Its data value is the low nibble of the ASCII code. Applying the Track 1 mapping to Track 2 produces the wrong LRC.

The decoder's **Include calculated LRC** option adds the printable LRC character to the output. Its breakdown also shows the LRC bit pattern with odd parity. Use this to learn how a reader checks the record, not to bypass an issuer's controls.

## Writing Synthetic Cards for Testing

**Use the decoder to write test strings, not live payment cards.** The tool accepts fields, rebuilds Track 1 and Track 2, adds optional sentinels, and calculates the LRC. It runs locally in the browser.

1. Open the **[Magnetic Stripe Decoder and Encoder](/magnetic-stripe-decoder/)**.
2. Select **Load Test Card**. This fills the tool with the synthetic PAN `4111111111111111`, the name `TEST/USER`, expiry `2912`, service code `201`, and test discretionary data.
3. Enable **Include start and end sentinels** to display the physical record boundaries.
4. Enable **Include calculated LRC** to append the calculated check character.
5. Enable **Split discretionary data into PVKI, PVV and CVV** only to see how a nine-digit synthetic field is displayed. Those labels are issuer conventions, not a universal Track 1 or Track 2 layout.
6. Change the name, expiry, service code, or synthetic discretionary data. The output updates as you type.
7. Compare the decoded fields with the generated strings. Clear the fields when finished.

For a synthetic Track 1 exercise, use:

```text
PAN: 4111111111111111
Surname: TEST
First name: USER
Expiry: 12/29
Service code: 201
Discretionary data: 000000000
```

For a synthetic Track 2 exercise, use the same PAN, expiry, service code, and a numeric discretionary field. The generated Track 2 string omits the name because Track 2 has no name field.

**Do not copy a live Privacy.com PAN, expiry, CVV, or discretionary value into a writable card.** Privacy.com describes its product as virtual card numbers created through its website or app. Its official page does not present the service as a magnetic-stripe-writing system, while a virtual card number is not proof of an issuer-authorized physical stripe record. A writable test card containing a live credential creates a duplicate payment instrument and violates issuer terms or payment rules.

The safe boundary is simple: use the tool's built-in synthetic sample, use a lab card with dummy values, and use an issuer-approved physical card when you need to pay in person. Do not attempt to turn a Privacy.com virtual card into a physical swipe card.

## What a Virtual Card Changes

**A virtual card is a second number standing in front of the first one.**

When you pay with a virtual card, the merchant receives a number, an expiry, and a CVV belonging to the virtual card. Your real PAN never reaches them. Practically, the change shows up after a breach:

| Scenario | With Your Real Card | With a Merchant-Locked Virtual Card |
|---|---|---|
| **Merchant database leaked** | The number is valid everywhere it is accepted | The number fails at every other merchant |
| **Subscription you cancelled** | Charging continues until you dispute it | You close the card and the charge fails |
| **Trial converting silently** | Unwanted charge on your statement | The limit or closure stops it |
| **Card details sold on a forum** | Usable for card-not-present fraud | Usable at one merchant only, if at all |

**What it does not change** matters as much. Your bank still sees the transaction. The card network still processes it. The issuer still holds your identity, because anti-money-laundering rules require verification. **A virtual card reduces merchant-side exposure. It is not a way to spend anonymously.**

*The distinction trips people up constantly. If your threat model includes the issuer or the network, a virtual card changes nothing about it.*

{{< figure src="virtual-card-merchant-shielding-flow.webp" alt="Diagram showing a virtual card number going to the merchant while the real card number stays between the cardholder and the issuing bank" >}}

## The Three Kinds of Card-Shaped Thing

The terminology is used inconsistently, and the difference matters when you are choosing what to hand a merchant.

| Type | Card Number | Physical Version | Typical Use |
|---|---|---|---|
| **Digital card** | Same as your physical card | Yes | Adding your existing card to a mobile wallet |
| **Virtual card** | Different from any physical card | No | Online purchases, subscriptions, one-off merchants |
| **Digital-first card** | Different, with an optional linked physical card | Optional | Fintech accounts where the physical card carries no printed details |

**A mobile wallet uses a fourth mechanism entirely.** When you add a card to a wallet, the wallet stores a device-specific token rather than your PAN, and the merchant receives the token. This is called tokenization, and it is why paying with a phone is safer than handing over the plastic even without a virtual card.

*Network tokenization and virtual cards solve overlapping parts of the same problem. Tokenization protects the number in transit and at rest. A virtual card protects you from what the merchant retains afterwards.*

## Privacy.com Card Types

**Privacy.com offers four card behaviours, and they are not interchangeable.**

| Card Type | Behaviour | Best For |
|---|---|---|
| **Single-Use** | Closes automatically after one transaction | One-off purchases and unfamiliar merchants |
| **Merchant-Locked** | Locks to the first merchant to charge it and fails elsewhere | Everyday online shopping |
| **Category-Locked** | Restricted to a spending category | Containing a whole class of spend |
| **Everywhere** | A physical card with the same protection model | In-person purchases |

**Merchant locking is the mechanism carrying most of the value.** A locked card fails at any merchant other than the one it was first used with, which means a breach at the merchant yields a number useless anywhere else.

**Single-use is the stronger option where it applies.** A card closing after one charge cannot be replayed at all, and it removes the need to remember to close it later.

Two operational details worth knowing:

- **Shared cards lock to the first merchant they are used with**, so sharing one with a family member or employee still carries the merchant restriction.
- **A card is paused rather than closed.** Pausing is reversible, which is useful when you want to stop a subscription temporarily without losing the card details.

## Spend Limits and Controls

**Every card carries a spend limit, which is a separate control from merchant locking.**

| Control | What It Prevents |
|---|---|
| **Per-transaction limit** | A single charge larger than you authorised |
| **Monthly limit** | Accumulating charges over a billing period |
| **Pause** | Any charge at all, reversibly |
| **Close** | Any future charge, permanently |

**Set both a per-transaction and a monthly limit on any card tied to a subscription.** A merchant quietly raising its price hits the limit rather than your balance, and you notice it from a failed charge instead of missing a statement line.

*Our **[Personal Finance Security](/personal-security-course/personal-finance/)** module places this alongside credit freezes and card tokenization as the three controls limiting what a single compromised merchant reaches.*

## Plans and What Each Unlocks

Privacy.com runs a free tier alongside three paid plans. Prices and feature boundaries change, so confirm current terms before subscribing.

| Plan | Price | Notable Additions |
|---|---|---|
| **Personal (free)** | $0 | Virtual cards, merchant locking, spend limits, no fee on domestic transactions |
| **Plus** | $5/mo | Category cards, card notes for organising spend |
| **Pro** | $10/mo | Cashback on qualifying purchases, Everywhere physical cards |
| **Premium** | $25/mo | Everything in Pro, with the monthly card creation limit raised to 60 |

**The free tier covers the core security benefit.** Merchant locking, single-use cards, and spend limits are the mechanisms reducing exposure, and they are available without paying. The paid tiers add organisation and convenience rather than additional protection.

**Foreign transaction fees differ by tier.** The free tier charges 3% on foreign transactions with a $0.50 minimum, while the paid tiers do not.

## What Privacy.com Does Not Do

**Being clear about the limits is more useful than a feature list.**

| Limitation | Detail |
|---|---|
| **It does not make you anonymous** | Your identity is verified at signup and the issuer holds it |
| **It does not hide the transaction from your bank** | Your bank sees the funding transfer, and the network sees the charge |
| **It does not build credit** | These are not credit accounts, and no credit pull occurs |
| **It is US-only** | Requires US citizenship or legal residency and a US bank or credit union account |
| **It requires identity verification** | Know Your Customer checks are mandatory under anti-money-laundering rules |
| **It does not cover every merchant** | Some merchants block prepaid and virtual card ranges |

**The merchant-blocking point matters in practice.** Some subscription services and airlines reject card ranges they associate with virtual or prepaid cards, and no amount of configuration fixes the problem. Keep a real card available as a fallback for those cases.

*The honest summary: a virtual card is a containment control for merchant-side exposure, not an anonymity tool. If you need anonymity, this is a different problem with different tools.*

## Who Issues the Card and Why It Matters

**A virtual card is still a real card, issued by a real bank, under a real scheme licence.**

| Detail | Value |
|---|---|
| **Issuing bank** | Patriot Bank, N.A., Member FDIC |
| **Scheme licences** | Mastercard and Visa |
| **Where it is accepted** | Anywhere Mastercard and Visa are accepted |
| **Funding** | Transferred from your linked US checking account |

**This is why the protection is genuine.** The card carries the same scheme protections as any other Mastercard or Visa product, which means chargeback rights and fraud dispute processes apply normally. It is not a gift card or a closed-loop store credit.

Two certifications are worth naming because they are independently verifiable rather than marketing claims:

- **PCI-DSS compliance**, which is the payment card industry standard for handling cardholder data
- **SOC 2 Type II**, which is an audited report covering security controls over a period of time rather than a point-in-time assertion

**On the business model:** the company states it earns interchange from merchants and does not sell customer data to advertisers or third parties. This is the same revenue model as every other card issuer, which is worth understanding rather than treating as unusual.

*The practical reason to check the issuing bank is verification. Anyone claims to run a card programme, and the issuer name on the card is what you confirm against the bank named in the paperwork.*

Inspect the scheme and bank from the PAN prefix using the **[Magnetic Stripe Decoder](/magnetic-stripe-decoder/)**, which reports the major scheme range and validates the Luhn check digit.

## Using Virtual Cards Well

**The controls only help if you configure them.** Six habits carry most of the benefit.

1. **Lock every card to a merchant** unless there is a reason not to. The lock is what makes a leaked number useless.
2. **Use single-use for anything unfamiliar**, including trials and one-off purchases from smaller sites.
3. **Set both spend limits** on subscription cards, so a price increase fails rather than charges.
4. **Name each card after the merchant**, so a transaction list is readable and an unexpected charge stands out.
5. **Pause rather than close** when you plan to resume a service, and close when you will not.
6. **Keep one real card for merchants rejecting virtual ranges**, so a blocked checkout does not become an emergency.

> **Common Mistake: treating a virtual card as a substitute for noticing your statements.** Merchant locking stops one class of harm. It does not detect a compromised account at your bank, an unauthorised transfer, or a fraudulent charge on the real card behind it.

## Key Takeaways

- **A virtual card changes the number the merchant stores.** Your real PAN never reaches them, which is the whole mechanism.
- **It does not make the transaction private.** Your bank, the network, and the issuer still see it, and identity verification is mandatory.
- **Merchant locking is the highest-value feature**, because a leaked number then fails everywhere else.
- **The free tier includes the security controls.** Paid plans add organisation and convenience rather than protection.
- **The magnetic stripe stores card data in plaintext** and is being removed by 2033, with US banks stopping issuance in 2027.
- **The CVV is not on the stripe**, which is why a skimmer copying tracks still lacks what many online merchants require.
- **Some merchants reject virtual card ranges.** Keep a real card as a fallback.
- **Verify the issuing bank** rather than trusting a card programme claim, and check the PAN prefix yourself.

## Next Steps

1. **Inspect your own card's track data** and see exactly what a stripe carries: **[Magnetic Stripe Decoder and Encoder](/magnetic-stripe-decoder/)**
2. **Freeze your credit** if you have not already, which is the stronger control for new-account fraud: **[Personal Finance Security](/personal-security-course/personal-finance/)**
3. **Apply the tiering discipline** to decide how much effort this deserves for your situation: **[Prioritized Personal Security Checklist](/articles/personal-security-checklist-prioritized-2026/)**
4. **Review the Privacy.com plans and current terms** before subscribing: **[Privacy.com](https://www.privacy.com/virtual-card)**
5. **Check whether your details already appear in a breach** before assuming you are unaffected: **[Have I Been Pwned](https://haveibeenpwned.com)**
6. **Read the payment security checklist** for the organizational counterpart: **[Incident Response Checklist](/checklists/incident-response-checklist/)**

## References

1. [Privacy.com - what virtual cards are, merchant locking, and spend limits](https://www.privacy.com/virtual-card)
2. [Digital card - Wikipedia, covering digital versus virtual cards, magnetic-stripe tracks, service codes, parity, and LRC](https://en.wikipedia.org/wiki/Digital_card)
3. [ISO/IEC 7813:2006 - identification cards, financial transaction cards, tracks 1 and 2 data structure](https://webstore.iec.ch/en/publication/11605)
4. [ISO/IEC 7813 - track field layout in detail, including sentinels and service codes](https://en.wikipedia.org/wiki/ISO/IEC_7813)
5. [PCI Security Standards Council - cardholder data environment requirements](https://www.pcisecuritystandards.org/)
6. [Consumer Financial Protection Bureau - credit reports and scores](https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/)
7. [ANSI/ISO ALPHA data encoding, the Track 1 character set and parity table](http://www.hhhh.org/~joeboy/resources/magcards/trackdata_ANSI-ISO_ALPHA.html)
8. [Magnetic card ISO characters, the Track 1 and Track 2 sets side by side](https://www.pos.swiftpos.com.au/Help-SP/MagneticCardSwipeISOCharacters.html)
9. [Reading magnetic card data, a practical walkthrough with a live card scan](https://blog.j2i.net/2024/06/18/reading-magnetic-card-data/)