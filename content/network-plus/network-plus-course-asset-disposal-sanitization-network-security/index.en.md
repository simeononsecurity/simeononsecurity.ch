---
title: "CompTIA Network+ N10-009: Media Sanitization"
date: 2023-07-26
lastmod: 2026-10-10
toc: true
draft: false
description: "Inventory retired network media, choose Clear, Purge, or Destroy, verify results, track custody, and record final disposition under NIST guidance."
genre: ["CompTIA Network+", "N10-009", "Networking", "Certification Course"]
tags: ["CompTIA Network+", "N10-009", "Media Sanitization", "network lab", "network troubleshooting", "exam prep"]
cover: "/img/cover/A_3D_animated_illustration_showing_a_locked_pa.webp"
coverAlt: "A 3D illustration of a padlock representing secure disposal of stored network data"
coverCaption: ""
---

[Return to the Network+ course](/network-plus-start/)

**Asset disposal starts with an inventory, not a reset button.** A retired firewall, switch, or access point might hold configuration files, certificates, logs, credentials, and removable storage. Record every storage component before a device leaves your control.

This lesson uses the **final NIST SP 800-88 Rev. 2** guidance. It teaches you to choose a sanitization method, check the result, and document the handoff. Practice on an inventory worksheet or a disposable lab device. Never erase a working device for this exercise.

## Identify Data and Media

**List the device and each storage component separately.** A factory reset might remove visible settings while leaving logs, backups, keys, or data in other media. Check vendor documentation for all internal and removable storage. Include USB drives, memory cards, and failed drives.

| Inventory field | Example for a retired lab firewall |
|---|---|
| **Asset and owner** | Firewall LAB-FW-01, network operations |
| **Media** | Internal flash and removable SSD |
| **Stored data** | Configuration, logs, certificate material |
| **Sensitivity** | Internal lab information, confirm with data owner |
| **Next destination** | Internal reuse, resale, recycler, or destruction |

**Keep the asset in controlled custody** while you decide. Disconnect the device from production networks, preserve any records required for an investigation, and obtain the owner's disposition decision. Sanitization does not replace retention or legal-hold review.

## Choose Clear, Purge, or Destroy

NIST defines three **sanitization methods**. A method describes the assurance goal. The actual technique depends on the media, its supported commands, and an approved standard.

| Method | Result and typical decision |
|---|---|
| **Clear** | Protects against simple recovery through the normal user interface. Use only when the data risk and destination permit it. |
| **Purge** | Makes recovery infeasible with state-of-the-art laboratory techniques while leaving suitable media potentially reusable. Prefer an approved purge technique when the risk warrants it. |
| **Destroy** | Makes the media unusable for data storage and target-data recovery infeasible. Use for damaged media or a policy requiring destruction. |

**A format or factory reset is not automatic proof of sanitization.** Ordinary writes might miss SSD overprovisioning or inaccessible storage. NIST Rev. 2 does not prescribe repeated random overwrites as a universal answer. Follow the approved media standard and verify the specific device's implementation.

**Cryptographic erase** is a purge option only after you confirm encryption covered the target data and the relevant keys were sanitized. If you lack evidence about key coverage or device behavior, choose another approved method. Logical or cloud storage requires a provider-specific process and evidence. Physical destruction does not apply to a virtual volume.

## Work Through a Disposal Decision

**Example:** LAB-FW-01 has internal flash and a removable SSD. Its configuration includes a lab certificate and its SSD holds logs. The owner approves external recycling after required records are retained.

1. **Record both media.** Keep their identifiers linked to LAB-FW-01.
2. **Check vendor instructions.** Identify supported sanitization commands and storage areas each command covers.
3. **Choose a method per medium.** An approved purge process might suit reusable internal flash. A failed SSD might require approved destruction. Do not select either technique without the device facts.
4. **Perform the approved process** under the organization's procedure. Save command status or destruction evidence without exposing stored secrets.
5. **Verify and validate.** Inspect completion status, errors, media health, or physical remnants. An accountable reviewer decides whether the result meets the confidentiality requirement.
6. **Record custody and destination.** Hand the sanitized or destroyed components to the approved recycler with a signed transfer record.

**Stop on an unknown storage component, failed command, or uncertain result.** Keep the asset controlled and escalate to the media owner. A failed clear operation does not become a pass because a later format command finished.

## Verify, Validate, and Record

**Verification** checks what the selected technique did. For a logical operation, inspect tool completion, errors, and relevant media status. For destruction, inspect the remnants and equipment record. **Validation** is the decision to accept or reject the result against the data risk. A reviewer might reject a technically completed operation if it did not cover all stored data.

```text
Asset ID: LAB-FW-01
Media ID and type: record separately for flash and SSD
Data owner and classification: record approved values
Method and approved technique: Clear / Purge / Destroy, with procedure reference
Tool or vendor process and version: record actual details
Operator, date, and location: record privately
Verification: completion status, errors, or remnant inspection
Validation: accepted or rejected, reviewer, and reason
Custody: each transfer, recipient role, and time
Disposition: internal reuse, external reuse, recycling, or destruction
```

**NIST Appendix C supplies a sample certificate of sanitization.** Use an approved organization form with the same core fields. Keep account names, serial numbers, and custody records in your private asset system, not a public course submission.

## Practice and Check

**Exercise:** your team retires a working switch with internal flash and a damaged SSD used for logs. The switch goes to a recycler. Write one row per medium with the proposed method, required device facts, verification, validation owner, and custody record.

**Expected reasoning:** identify both media. A normal format does not establish SSD sanitization. Check the vendor's flash process and the approved media standard. Escalate the damaged SSD for approved destruction if a validated purge is unavailable. Record both outcomes before release.

**Completion check:** another learner should identify the asset, all storage components, approved method for each component, evidence of technique completion, acceptance decision, and final destination from your worksheet alone. Mark any unknown or failed component Blocked.

## Primary Reference

- [NIST SP 800-88 Rev. 2, Guidelines for Media Sanitization](https://csrc.nist.gov/pubs/sp/800/88/r2/final)

## Next Steps

Continue with [Network Hardening Techniques](/network-plus/network-plus-course-network-hardening-techniques/) and return to the [Network+ course](/network-plus-start/).


## Progressive Lab Checkpoint 25: Media Sanitization

This checkpoint extends the [shared course topology](/network-plus-start/#progressive-n10-009-lab). Work inside an isolated simulator copy. Save `25-before` before changing state.

**Goal and tasks:** Create a simulated router inventory record. Identify media, data sensitivity, reuse goal, and media-specific method. Choose Clear, Purge, or Destroy. Record custody, verification, validation, exceptions, final destination, and certificate serial and date. Formatting alone does not prove sanitization.

### Expected evidence

Save command output, packet data, counters, diagrams, or records which prove each task result. Compare observed evidence with the topology and address plan. Explain every mismatch before changing state.

### Fault injection and recovery

Remove the serial number or custody signature from a copy. Reject the package, repair the gap, and reconcile inventory.

### Deliverable and pass gate

Submit **`25-disposition-record.md`** with purpose, affected nodes, risk, rollback, before evidence, fault evidence, recovery evidence, and cleanup statement.

**Pass:** Inventory, method, verification, validation, custody, certificate, and disposition all match.

[Previous checkpoint](/network-plus/network-plus-course-network-hardening-techniques/) | [Next checkpoint](/network-plus/network-plus-course-network-software-tools-commands/)

### Primary references

- [CompTIA Network+ N10-009 exam objectives](https://comptiacdn.azureedge.net/webcontent/docs/default-source/exam-objectives/comptia-network-n10-009-exam-objectives-%284-0%29-%281%29.pdf?sfvrsn=f31cc6c4_4)
- [Topic source](https://csrc.nist.gov/pubs/sp/800/88/r2/final)
