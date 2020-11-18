---
title: "Windows Spectre Meltdown Mitigation Script"
date: 2020-06-18
toc: true
draft: false
tags: ['CVE-2017-5715', 'CVE-2017-5753', 'CVE-2017-5754', 'CVE-2018-3639', 'CVE-2018-11091','CVE-2018-12126', 'CVE-2018-12127', 'CVE-2018-12130', 'Branch Target Injection', 'Bounds Check Bypass', 'Rogue Data Cache Load', 'Speculative Store Bypass', 'Microarchitectural Data Sampling Uncacheable Memory', 'MDSUM', 'Microarchitectural Store Buffer Data Sampling, 'MSBDS', 'Microarchitectural Fill Buffer Data Sampling', 'MFBDS', 'Microarchitectural Load Port Data Sampling', 'MLPDS', 'PowerShell', 'Automation']
---
#### https://support.microsoft.com/en-us/help/4073119/protect-against-speculative-execution-side-channel-vulnerabilities-in
**Simple script to implement protections against speculative execution side-channel vulnerabilities in Windows systems.**

Microsoft is aware of a new publicly disclosed class of vulnerabilities that are called “speculative execution side-channel attacks” and that affect many modern processors including Intel, AMD, VIA, and ARM. 

**Note:** This issue also affects other operating systems, such as Android, Chrome, iOS, and macOS. Therefore, we advise customers to seek guidance from those vendors.

We have released several updates to help mitigate these vulnerabilities. We have also taken action to secure our cloud services. See the following sections for more details.

We have not yet received any information to indicate that these vulnerabilities were used to attack customers. We are working closely with industry partners including chip makers, hardware OEMs, and application vendors to protect customers. To get all available protections, firmware (microcode) and software updates are required. This includes microcode from device OEMs and, in some cases, updates to antivirus software.

**This article addresses the following vulnerabilities:**
- CVE-2017-5715 – "Branch Target Injection"
- CVE-2017-5753 – "Bounds Check Bypass"
- CVE-2017-5754 – "Rogue Data Cache Load"
- CVE-2018-3639 – "Speculative Store Bypass"
- CVE-2018-11091 – “Microarchitectural Data Sampling Uncacheable Memory (MDSUM)”
- CVE-2018-12126 – “Microarchitectural Store Buffer Data Sampling (MSBDS)”
- CVE-2018-12127 – “Microarchitectural Fill Buffer Data Sampling (MFBDS)”
- CVE-2018-12130 – “Microarchitectural Load Port Data Sampling (MLPDS)”

UPDATED ON AUGUST 6, 2019 On August 6, 2019 Intel released details about a Windows kernel information disclosure vulnerability. This vulnerability is a variant of the Spectre Variant 1 speculative execution side channel vulnerability and has been assigned CVE-2019-1125.

UPDATED ON NOVEMBER 12, 2019 On November 12, 2019, Intel published a technical advisory around Intel® Transactional Synchronization Extensions (Intel® TSX) Transaction Asynchronous Abort vulnerability that is assigned CVE-2019-11135. Microsoft has released updates to help mitigate this vulnerability and the OS protections are enabled by default for Windows Client OS Editions.

## Recommended actions
Customers should take the following actions to help protect against the vulnerabilities:

- Apply all available Windows operating system updates, including the monthly Windows security updates.
- Apply the applicable firmware (microcode) update that is provided by the device manufacturer.
- Evaluate the risk to your environment based on the information that is provided on Microsoft Security Advisories: ADV180002, ADV180012, ADV190013 and information provided in this Knowledge Base article.
- Take action as required by using the advisories and registry key information that are provided in this Knowledge Base article.
