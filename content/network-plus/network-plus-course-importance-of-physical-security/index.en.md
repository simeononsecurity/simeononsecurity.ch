---
title: "CompTIA Network+ N10-009: Physical Security"
date: 2023-07-22
lastmod: 2026-10-21
toc: true
draft: false
description: "Learn Network Skills for CompTIA Network+ N10-009 through doors, racks, consoles, ports, a controlled fault, saved evidence, and recovery proof."
genre: ["CompTIA Network+", "N10-009", "Networking", "Certification Course"]
tags: ["CompTIA Network+", "N10-009", "Physical Security", "network lab", "network troubleshooting", "exam prep"]
cover: "/img/cover/A_symbolic_illustration_showing_a_lock_protect.webp"
coverAlt: "A symbolic illustration showing a lock protecting network infrastructure."
coverCaption: "Protect your network with robust physical security measures."
---

[Click Here to Return To the Network Plus Course Page](/network-plus-start)

**Physical security** is a crucial aspect of any organization's overall security strategy. While cybersecurity focuses on protecting data and information in digital environments, physical security deals with safeguarding the tangible assets and infrastructure of a business. This article delves into the significance of physical security, best practices for its implementation, and specific measures to secure network devices, such as switchports and VLANs.

______

## Understanding the Significance of Physical Security

Physical security forms the foundational layer of a comprehensive security framework. It encompasses measures to protect a company's facilities, personnel, equipment, and resources from unauthorized access, damage, theft, or compromise. Neglecting physical security can lead to severe consequences, including data breaches, unauthorized data access, and infrastructure damage.

**A breach in physical security** can open up vulnerabilities that cybercriminals can exploit. For instance, an unauthorized individual gaining access to the server room might be able to directly tamper with network equipment, plant malware, or steal sensitive data.

______

## Implementing Best Practices for Physical Security

To ensure robust physical security, organizations must adopt best practices that encompass a range of preventive and protective measures. Some essential practices include:

### 1. Access Control and Monitoring

**Access control** is the foundation of physical security. Restricting access to sensitive areas through key cards, biometric authentication, or other access control systems helps prevent unauthorized entry. Additionally, monitoring access attempts and maintaining logs can aid in detecting potential security breaches.

### 2. Surveillance Systems

Deploying surveillance cameras in and around the premises can serve as a deterrent for potential intruders and provide valuable evidence in the event of security incidents. Modern surveillance systems can also integrate with AI and analytics for more effective monitoring.

### 3. Security Guards and Personnel Training

Trained security personnel play a vital role in maintaining physical security. Their presence alone can deter criminals. Regular training for employees on security protocols and procedures helps in fostering a security-conscious culture within the organization.

### 4. Perimeter Security

Securing the physical boundaries of the organization, such as fences, gates, and barriers, prevents unauthorized access to the premises. Adding additional layers of security to sensitive areas within the building is also recommended.

### 5. Alarms and Incident Response

Install **intrusion detection systems** and alarms to promptly notify security personnel of any security breaches. Coupled with a robust incident response plan, these systems can help contain security incidents before they escalate.

______

## Securing Switchports and Disabling Unneeded Services

In network security, securing switchports is an essential measure to prevent unauthorized access to a network. Switchports are points of entry into a network where network devices are connected. Hackers can exploit unsecured switchports to gain unauthorized access to the network.

To secure switchports:

1. **Implement Port Security**: Limit the number of MAC addresses allowed on each switchport to prevent unauthorized devices from connecting.

2. **Disable Unused Ports**: Shut down any switchports not currently in use to reduce potential points of entry.

3. **Enable BPDU Guard**: BPDU Guard prevents the unauthorized creation of switch loops, which could be used for malicious purposes.

______

## Changing Default Passwords and Enforcing Password Complexity

One common mistake that often leads to security breaches is leaving **default passwords** unchanged on network devices. Manufacturers set default credentials, and attackers can easily find these credentials online, gaining access to the device.

To enhance password security:

1. **Change Default Passwords**: Immediately change default passwords on all network devices, including routers, switches, and access points.

2. **Enforce Password Complexity**: Set password policies that require strong passwords with a combination of uppercase and lowercase letters, numbers, and special characters. Regularly enforce password updates to ensure ongoing security.

______

## Implementing DHCP Snooping and Changing Default VLAN

Dynamic Host Configuration Protocol (DHCP) snooping is a security feature that helps protect against unauthorized DHCP servers on a network. Unauthorized DHCP servers can distribute incorrect IP configurations or even launch attacks on devices within the network.

To implement DHCP snooping:

1. **Enable DHCP Snooping**: Enable DHCP snooping on all switches to validate DHCP messages from authorized servers and mitigate the risk of rogue DHCP servers.

2. **Change Default VLAN**: Changing the default VLAN on network devices helps prevent unauthorized access to sensitive VLANs and improves overall network security.

______

In conclusion, physical security is an integral part of a comprehensive security strategy. Neglecting physical security can expose organizations to significant risks, including data breaches and infrastructure damage. By implementing best practices, such as access control, surveillance systems, and personnel training, organizations can establish a strong foundation for physical security. Additionally, securing switchports, changing default passwords, and implementing DHCP snooping are specific measures that enhance network security. Prioritizing physical security alongside cybersecurity measures is crucial for protecting an organization's assets and ensuring business continuity.

______

## References

1. [Federal Information Security Management Act (FISMA)](https://www.cisa.gov/fisma)
2. [Payment Card Industry Data Security Standard (PCI DSS)](https://www.pcisecuritystandards.org/pci_security/)
3. [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
4. [NIST Special Publication 800-171](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-171r2.pdf)
5. [CompTIA Network+ Certification Exam](https://www.comptia.org/certifications/network)
6. [Implementing Cisco Network Security](https://www.cisco.com/c/en/us/training-events/training-certifications/exams/current-list/iins-210-260.html)
7. [Cisco Certified Network Associate (CCNA) Certification](https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/associate/ccna.html)
8. [Microsoft Technology Associate (MTA) Certification](https://www.microsoft.com/en-us/learning/mta-certification.aspx)


## Next Steps

Continue with [Patch and Firmware Management](/network-plus/network-plus-course-firmware-and-patch-management/) and return to the [Network+ course](/network-plus-start/).

## Progressive Lab Checkpoint 22: Physical Security

This checkpoint extends the [shared course topology](/network-plus-start/#progressive-n10-009-lab). Work inside an isolated simulator copy. Save `22-before` before changing state.

**Build and verify:** Create one topic-specific diagram, configuration, capture, log, ticket, or test record covering doors, racks, consoles, ports, management access, default, native and management VLANs, DHCP snooping, quarantine, and switch ports. Tie every choice to R1, R2, SW1, SW2, AP1, SRV1, or an endpoint in the shared topology. Record expected and observed results.

### Fault injection and recovery

Mark a user port trusted or leave an unused port active. Detect the exposure and correct it.

### Deliverable and pass gate

Submit **`22-network-plus-course-importance-of-physical-security.md`** with purpose, affected nodes, risk, rollback, before evidence, fault evidence, recovery evidence, and cleanup statement.

**Pass:** The artifact covers each named topic, supports the diagnosis with evidence, restores required service, and proves cleanup.

[Previous checkpoint](/network-plus/network-plus-course-plans-procedures-policies/) | [Next checkpoint](/network-plus/network-plus-course-detection-prevention-methods/)

### Reproducible route and filled sample

Use a fictional site-survey packet. Filled finding: `PS-01 | SW2 F0/10 active in public room | evidence link light and show interface | risk unauthorized access | owner NetOps | fix shutdown plus quarantine VLAN | retest link down | pass`. Packet Tracer supports the switch-port repair. Door, rack, visitor, and camera checks remain fictional records.

### Primary reference

- [CompTIA Network+ N10-009 exam objectives](https://comptiacdn.azureedge.net/webcontent/docs/default-source/exam-objectives/comptia-network-n10-009-exam-objectives-%284-0%29-%281%29.pdf?sfvrsn=f31cc6c4_4)
