---
title: "ডিফেন্ডার হার্ডেনিং স্ক্রিপ্ট সহ উইন্ডোজ 10 সুরক্ষা উন্নত করা"
date: 2020-11-15
toc: true
draft: false
description: "উইন্ডোজ ডিফেন্ডার অ্যান্টিভাইরাস STIG V2R1-এর সমস্ত প্রয়োজনীয়তা বাস্তবায়ন করে, Windows Defender অ্যান্টিভাইরাসকে শক্ত করে এমন PowerShell স্ক্রিপ্টের সাহায্যে কীভাবে Windows 10 নিরাপত্তা বাড়ানো যায় তা শিখুন।"
tags: ["উইন্ডোজ ডিফেন্ডার", "উইন্ডোজ 10", "উইন্ডোজ 10 নিরাপত্তা", "পাওয়ারশেল স্ক্রিপ্ট", "শক্ত করা", "ডিফেন্ডার হার্ডেনিং", "নিরাপত্তা অটোমেশন", "সম্মতি", "নিয়ন্ত্রিত ফোল্ডার অ্যাক্সেস", "অনুপ্রবেশের প্রতিরোধ সিস্টেম", "অ্যাপ্লিকেশন নিয়ন্ত্রণ", "আক্রমণ সারফেস হ্রাস", "শোষণ সুরক্ষা", "ক্লাউড-ডেলিভারড সুরক্ষা", "নেটওয়ার্ক সুরক্ষা", "উইন্ডোজ ডিফেন্ডার STIG স্ক্রিপ্ট", "উইন্ডোজ ডিফেন্ডার STIG", "উইন্ডোজ ডিফেন্ডার অ্যান্টিভাইরাস STIG V2R1", "WDAC", "এএসআর"]
---


## এই স্ক্রিপ্ট কি করে?
- ক্লাউড-ডেলিভারি সুরক্ষা সক্ষম করে
- নিয়ন্ত্রিত ফোল্ডার অ্যাক্সেস সক্ষম করে
- নেটওয়ার্ক সুরক্ষা সক্ষম করে
- অনুপ্রবেশ প্রতিরোধ ব্যবস্থা সক্ষম করে
-[Enables Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
-[Enables Windows Defender Attack Surface Reduction Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Enables Windows Defender Exploit Protections](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide#powershell)
- তালিকাভুক্ত সমস্ত প্রয়োজনীয়তা বাস্তবায়ন করে৷[Windows Defender Antivirus STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)

## প্রয়োজনীয়তা:
- [x] Windows 10 Enterprise (**Preferred**) অথবা Windows 10 Professional
  - Windows 10 হোম GPO কনফিগারেশন বা জন্য অনুমতি দেয় না[ASR](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) 
যদিও এই কনফিগারেশনগুলির বেশিরভাগই এখনও প্রযোজ্য হবে।
  - Windows 10 "N" সংস্করণগুলি পরীক্ষা করা হয় না।

## প্রয়োজনীয় ফাইল ডাউনলোড করুন:

থেকে প্রয়োজনীয় ফাইল ডাউনলোড করুন[GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)

## কিভাবে স্ক্রিপ্ট চালাবেন:

**নিষ্কৃত গিটহাব ডাউনলোড থেকে স্ক্রিপ্টটি এভাবে চালু করা যেতে পারে:**
```
.\sos-windowsdefenderhardening.ps1
```
