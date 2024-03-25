---
title: "উইন্ডোজ-অপ্টিমাইজ-হার্ডেন-ডেব্লোট স্ক্রিপ্টের সাথে আপনার উইন্ডোজ সিস্টেম অপ্টিমাইজ করুন এবং শক্ত করুন"
date: 2020-12-29
toc: true
draft: false
description: "এই বিস্তৃত নির্দেশিকাটি উন্নত কর্মক্ষমতা, নিরাপত্তা এবং গোপনীয়তার জন্য কীভাবে আপনার উইন্ডোজ সিস্টেমকে অপ্টিমাইজ, শক্ত এবং ডিব্লোট করতে হয় সে সম্পর্কে ধাপে ধাপে নির্দেশনা প্রদান করে।"
tags: ["উইন্ডোজ অপ্টিমাইজেশান", "উইন্ডোজ শক্ত করা", "Windows debloating", "উইন্ডোজ নিরাপত্তা", "উইন্ডোজ কর্মক্ষমতা", "উইন্ডোজ গোপনীয়তা", "উইন্ডোজ আপডেট", "গ্রুপ পলিসি অবজেক্ট", "অ্যাডোব অ্যাক্রোব্যাট রিডার", "ফায়ারফক্স", "গুগল ক্রম", "ইন্টারনেট এক্সপ্লোরার", "মাইক্রোসফট ক্রোমিয়াম এজ", "ডট নেট 4", "মাইক্রোসফট অফিস", "ওয়ানড্রাইভ", "ওরাকল জাভা JRE 8", "উইন্ডোজ ফায়ারওয়াল", "উইন্ডোজ ডিফেন্ডার", "আবেদনকারী"]
---
 ভূমিকা:

Windows 10 এবং Windows 11 আক্রমণাত্মক এবং অনিরাপদ অপারেটিং সিস্টেম বাক্সের বাইরে।
সংগঠনগুলো পছন্দ করে[PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://www.defense.gov/), and the [National Security Agency](https://www.nsa.gov/) অপারেটিং সিস্টেমকে লকডাউন, শক্ত এবং সুরক্ষিত করতে কনফিগারেশন পরিবর্তনের সুপারিশ করেছে। এই পরিবর্তনগুলি টেলিমেট্রি ব্লক করা, ম্যাক্রো, ব্লোটওয়্যার অপসারণ এবং একটি সিস্টেমে অনেক ডিজিটাল এবং শারীরিক আক্রমণ প্রতিরোধ সহ বিস্তৃত প্রশমনকে কভার করে। এই স্ক্রিপ্টটি সেই সংস্থাগুলির দ্বারা প্রস্তাবিত কনফিগারেশনগুলিকে স্বয়ংক্রিয় করার লক্ষ্য রাখে।

## নোট, সতর্কতা, এবং বিবেচনা:

**সতর্কতা:**

এই স্ক্রিপ্টটি বেশিরভাগ ক্ষেত্রে কাজ করা উচিত, যদি সব না হয়, সমস্যা ছাড়াই সিস্টেমের জন্য। যখন[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues)

- এই স্ক্রিপ্টটি প্রাথমিকভাবে **ব্যক্তিগত ব্যবহার** পরিবেশে অপারেশনের জন্য ডিজাইন করা হয়েছে। এটি মনে রেখে, নির্দিষ্ট এন্টারপ্রাইজ কনফিগারেশন সেটিংস প্রয়োগ করা হয় না। এই স্ক্রিপ্টটি একটি সিস্টেমকে 100% সম্মতিতে আনার জন্য ডিজাইন করা হয়নি। বরং এটিকে বেশিরভাগ সম্পূর্ণ করার জন্য একটি ধাপের পাথর হিসাবে ব্যবহার করা উচিত, যদি সব না হয়, ব্র্যান্ডিং এবং ব্যানারের মতো অতীতের সমস্যাগুলি এড়িয়ে যাওয়ার সময় স্ক্রিপ্ট করা যেতে পারে এমন কনফিগারেশন পরিবর্তনগুলি যেখানে ব্যক্তিগত ব্যবহারের কঠোর পরিবেশেও প্রয়োগ করা উচিত নয়৷
- এই স্ক্রিপ্টটি এমনভাবে ডিজাইন করা হয়েছে যাতে অপ্টিমাইজেশানগুলি, অন্য কিছু স্ক্রিপ্টের মতন, মূল উইন্ডোর কার্যকারিতা ভাঙবে না।
- Windows Update, Windows Defender, Windows Store, এবং Cortona-এর মতো বৈশিষ্ট্যগুলিকে সীমাবদ্ধ করা হয়েছে, কিন্তু বেশিরভাগ অন্যান্য Windows 10 গোপনীয়তা স্ক্রিপ্টের মতো অকার্যকর অবস্থায় নেই৷
- আপনি যদি শুধুমাত্র বাণিজ্যিক পরিবেশে লক্ষ্য করে একটি ন্যূনতম স্ক্রিপ্ট চান, দয়া করে এটি দেখুন[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)


**এই স্ক্রিপ্টটি চালাবেন না যদি আপনি বুঝতে না পারেন এটি কী করে। এটি চালানোর আগে স্ক্রিপ্টটি পর্যালোচনা এবং পরীক্ষা করা আপনার দায়িত্ব৷**

**উদাহরণস্বরূপ, আপনি যদি প্রতিরোধমূলক পদক্ষেপ না নিয়ে এটি চালান তবে নিচের কাজগুলি ভেঙে যাবে:**

- "প্রশাসক" নামের ডিফল্ট অ্যাডমিনিস্ট্রেটর অ্যাকাউন্ট ব্যবহার করা নিষ্ক্রিয় করা হয়েছে এবং DoD STIG অনুসারে নামকরণ করা হয়েছে

  - তৈরি করা ডিফল্ট অ্যাকাউন্টের ক্ষেত্রে প্রযোজ্য নয় তবে প্রায়শই এন্টারপ্রাইজ, আইওটি এবং উইন্ডোজ সার্ভার সংস্করণে পাওয়া ডিফল্ট অ্যাডমিনিস্ট্রেটর অ্যাকাউন্ট ব্যবহার করার ক্ষেত্রে প্রযোজ্য হয়

  - কম্পিউটার ম্যানেজমেন্টের অধীনে একটি নতুন অ্যাকাউন্ট তৈরি করুন এবং আপনি চাইলে প্রশাসক হিসাবে সেট করুন। তারপরে স্ক্রিপ্টটি চালানোর আগে এটিকে ঘিরে কাজ করার জন্য প্রথমবার নতুন ব্যবহারকারী সাইন ইন করার পরে পূর্ববর্তী ব্যবহারকারীদের ফোল্ডারের বিষয়বস্তু নতুনটিতে অনুলিপি করুন।

- একটি মাইক্রোসফ্ট অ্যাকাউন্ট ব্যবহার করে সাইন ইন করা প্রতি DoD STIG অক্ষম করা হয়েছে৷

  - নিরাপদ এবং ব্যক্তিগত হওয়ার চেষ্টা করার সময়, একটি Microsoft অ্যাকাউন্টের মাধ্যমে আপনার স্থানীয় অ্যাকাউন্টে সাইন ইন করার পরামর্শ দেওয়া হয় না। এটি এই রেপো দ্বারা প্রয়োগ করা হয়।

  - কম্পিউটার ম্যানেজমেন্টের অধীনে একটি নতুন অ্যাকাউন্ট তৈরি করুন এবং আপনি চাইলে প্রশাসক হিসাবে সেট করুন। তারপরে স্ক্রিপ্টটি চালানোর আগে এটিকে ঘিরে কাজ করার জন্য প্রথমবার নতুন ব্যবহারকারী সাইন ইন করার পরে পূর্ববর্তী ব্যবহারকারীদের ফোল্ডারের বিষয়বস্তু নতুনটিতে অনুলিপি করুন।

- DoD STIG প্রতি অ্যাকাউন্ট পিন অক্ষম করা হয়েছে

  - শুধুমাত্র পাসওয়ার্ডের জায়গায় ব্যবহার করা হলে পিনগুলি অনিরাপদ হয় এবং কয়েক ঘন্টা বা সম্ভাব্য এমনকি সেকেন্ড বা মিনিটের মধ্যে সহজেই বাইপাস করা যায়

  - অ্যাকাউন্ট থেকে পিনটি সরান এবং/অথবা স্ক্রিপ্ট চালানোর পরে পাসওয়ার্ড ব্যবহার করে সাইন ইন করুন।

- বিটলকার ডিফল্ট পরিবর্তন করা হয়েছে এবং DoD STIG এর কারণে শক্ত হয়েছে।

  - কীভাবে বিটলকার প্রয়োগ করা হয়, যখন এই পরিবর্তনগুলি ঘটে এবং আপনি যদি ইতিমধ্যেই বিটলকার সক্ষম করে থাকেন তবে এটি বিটলকার বাস্তবায়নকে ভেঙে দেবে।

  - বিটলকার অক্ষম করুন, স্ক্রিপ্টটি চালান, তারপর এই সমস্যাটির সমাধান করতে বিটলকারকে পুনরায় সক্রিয় করুন৷

## প্রয়োজনীয়তা:

- [x] Windows 10/11 এন্টারপ্রাইজ (**পছন্দের**) বা পেশাদার
  - Windows 10/11 হোম সংস্করণগুলি GPO কনফিগারেশন সমর্থন করে না এবং পরীক্ষা করা হয় না।
  - উইন্ডো "এন" সংস্করণগুলি পরীক্ষা করা হয় না।
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) একটি অত্যন্ত সুরক্ষিত Windows 10 ডিভাইসের জন্য
-[x] System is [fully up to date and supported](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - চালান[Windows Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) সর্বশেষ বড় রিলিজ আপডেট এবং যাচাই করতে।
- [x] এই স্ক্রিপ্টটি প্রয়োগ করার আগে বিটলকারকে অবশ্যই সাসপেন্ড বা বন্ধ করতে হবে, এটি পুনরায় বুট করার পরে আবার সক্রিয় করা যেতে পারে।
  - এই স্ক্রিপ্টের ফলো-আপ রান বিটলকার নিষ্ক্রিয় না করে চালানো যেতে পারে।
- [x] হার্ডওয়্যারের প্রয়োজনীয়তা
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections)
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)

## প্রস্তাবিত পড়ার উপাদান:

-[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
-[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
-[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
-[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
-[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
-[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## সংযোজন, উল্লেখযোগ্য পরিবর্তন, এবং বাগ ফিক্স:

**এই স্ক্রিপ্ট আপনার সিস্টেমে সেটিংস যোগ করে, অপসারণ করে এবং পরিবর্তন করে। এটি চালানোর আগে স্ক্রিপ্ট পর্যালোচনা করুন.**

### ব্রাউজার:

- গোপনীয়তা এবং সুরক্ষায় সহায়তা করার জন্য ব্রাউজারগুলিতে অতিরিক্ত এক্সটেনশন ইনস্টল করা থাকবে।
  - দেখা[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/11) অতিরিক্ত তথ্যের জন্য।
- ব্রাউজারগুলির জন্য বাস্তবায়িত DoD STIGs এর কারণে, এক্সটেনশন পরিচালনা এবং অন্যান্য এন্টারপ্রাইজ সেটিংস সেট করা হয়েছে৷ এই বিকল্পগুলি কীভাবে দেখতে হয় তার নির্দেশাবলীর জন্য, আপনাকে নীচের GPO নির্দেশাবলী দেখতে হবে।

### পাওয়ারশেল মডিউল:

- পাওয়ারশেলকে উইন্ডোজ আপডেটগুলি স্বয়ংক্রিয় করতে সহায়তা করতে[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) আপনার সিস্টেমে মডিউল যোগ করা হবে।

### মাইক্রোসফ্ট অ্যাকাউন্ট, স্টোর বা এক্সবক্স পরিষেবাগুলি ঠিক করা:

কারণ আমরা মাইক্রোসফট অ্যাকাউন্টে সাইন ইন করা ব্লক করি। মাইক্রোসফ্টের টেলিমেট্রি এবং আইডেন্টিটি অ্যাসোসিয়েশন ভ্রুকুটি করা হয়েছে।
যাইহোক, আপনি যদি এখনও এই পরিষেবাগুলি ব্যবহার করতে চান তাহলে রেজোলিউশনের জন্য নিম্নলিখিত ইস্যু টিকিটগুলি দেখুন:

- https://github.com/simeononsecurity/Windows-Optimize-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

### স্থানীয় গ্রুপ নীতিতে নীতিগুলি সম্পাদনা করা

আপনি যদি একটি সেটিং পরিবর্তন বা পরিবর্তন করতে চান, তাহলে সেগুলি সম্ভবত GPO এর মাধ্যমে কনফিগার করা যায়:

- এখান থেকে ADMX নীতির সংজ্ঞা আমদানি করুন[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) আপনি যে সিস্টেমটি পরিবর্তন করার চেষ্টা করছেন তাতে _C:\windows\PolicyDefinitions_-এ।

- আপনি যে সিস্টেমটি পরিবর্তন করার চেষ্টা করছেন তাতে `gpedit.msc` খুলুন।

## এই সংগ্রহটি ব্যবহার করে স্ক্রিপ্ট এবং সরঞ্জামগুলির একটি তালিকা:

### প্রথম পার্টি:

-[.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
-[FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[JAVA-STIG-Script](https://github.com/simeononsecurity/JAVA-STIG-Script)
-[Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[Windows-Optimize-Debloat](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

### তৃতীয় পক্ষ:

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
-[Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)

## STIGS/SRGs প্রয়োগ করা হয়েছে:

-[Adobe Acrobat Pro DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
-[Adobe Acrobat Reader DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
-[Firefox V5R2](https://public.cyber.mil/stigs/downloads/)
-[Google Chrome V2R4](https://public.cyber.mil/stigs/downloads/)
-[Internet Explorer 11 V1R19](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Edge V1R2](https://public.cyber.mil/stigs/downloads/)
-[Microsoft .Net Framework 4 V1R9](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2013 V2R1](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2016 V2R1](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2019/Office 365 Pro Plus V2R3](https://public.cyber.mil/stigs/downloads/)
-[Microsoft OneDrive STIG V2R1](https://public.cyber.mil/stigs/downloads/)
-[Oracle JRE 8 V1R5](https://public.cyber.mil/stigs/downloads/)
-[Windows 10 V2R2](https://public.cyber.mil/stigs/downloads/)
-[Windows Defender Antivirus V2R2](https://public.cyber.mil/stigs/downloads/)
-[Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)

## থেকে অতিরিক্ত কনফিগারেশন বিবেচনা করা হয়েছিল:

-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[CERT - IE Scripting Engine Memory Corruption](https://kb.cert.org/vuls/id/573168/)
-[Dirteam - SSL Hardening](https://dirteam.com/sander/2019/07/30/howto-disable-weak-protocols-cipher-suites-and-hashing-algorithms-on-web-application-proxies-ad-fs-servers-and-windows-servers-running-azure-ad-connect/)
-[MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Reduce attack surfaces with attack surface reduction rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Specture and Meltdown Mitigations](https://support.microsoft.com/en-us/help/4072698/windows-server-speculative-execution-side-channel-vulnerabilities)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)
-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
-[NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)
-[UnderGroundWires - Privacy.S\*\*Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[VectorBCO - windows-path-enumerate](https://github.com/VectorBCO/windows-path-enumerate)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)
-[Whonix - Disable TCP Timestamps](https://www.whonix.org/wiki/Disable_TCP_and_ICMP_Timestamps)

## কিভাবে স্ক্রিপ্ট চালাবেন:
### GUI - নির্দেশিত ইনস্টল:

সর্বশেষ রিলিজ ডাউনলোড করুন[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat-GUI/releases/)আপনি যে বিকল্পগুলি চান তা চয়ন করুন এবং কার্যকর করুন। <img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/WOHD-GUI.gif" alt="Windows-Optimize-Harden-Debloat GUI-ভিত্তিক নির্দেশিত ইনস্টলের উদাহরণ"> ### স্বয়ংক্রিয় ইনস্টল: স্বয়ংক্রিয়ভাবে ডাউনলোড করতে, সমস্ত সমর্থনকারী ফাইল আনজিপ করতে এবং স্ক্রিপ্টের সর্বশেষ সংস্করণ চালাতে এই ওয়ান-লাইনারটি ব্যবহার করুন।```powershell
iwr -useb 'https://simeononsecurity.com/scripts/windowsoptimizeandharden.ps1'|iex
```

<img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/w10automatic.gif" alt="Example of 
Windows-Optimize-Harden-Debloat automatic install">

### Manual Install:

If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

The script "sos-optimize-windows.ps1" includes several parameters that allow for customization of the optimization process. Each parameter is a boolean value that defaults to true if not specified.

- **cleargpos**: Clears Group Policy Objects settings.
- **installupdates**: Installs updates to the system.
- **adobe**: Implements the Adobe Acrobat Reader STIGs.
- **firefox**: Implements the FireFox STIG.
- **chrome**: Implements the Google Chrome STIG.
- **IE11**: Implements the Internet Explorer 11 STIG.
- **edge**: Implements the Microsoft Chromium Edge STIG.
- **dotnet**: Implements the Dot Net 4 STIG.
- **office**: Implements the Microsoft Office Related STIGs.
- **onedrive**: Implements the Onedrive STIGs.
- **java**: Implements the Oracle Java JRE 8 STIG.
- **windows**: Implements the Windows Desktop STIGs.
- **defender**: Implements the Windows Defender STIG.
- **firewall**: Implements the Windows Firewall STIG.
- **mitigations**: Implements General Best Practice Mitigations.
- **defenderhardening**: Implements and Hardens Windows Defender Beyond STIG Requirements.
- **pshardening**: Implements PowerShell Hardening and Logging.
- **sslhardening**: Implements SSL Hardening.
- **smbhardening**: Hardens SMB Client and Server Settings.
- **applockerhardening**: Installs and Configures Applocker (In Audit Only Mode).
- **bitlockerhardening**: Harden Bitlocker Implementation.
- **removebloatware**: Removes unnecessary programs and features from the system.
- **disabletelemetry**: Disables data collection and telemetry.
- **privacy**: Makes changes to improve privacy.
- **imagecleanup**: Cleans up unneeded files from the system.
- **nessusPID**: Resolves Unquoted System Strings in Path.
- **sysmon**: Installs and configures sysmon to improve auditing capabilities.
- **diskcompression**: Compresses the system disk.
- **emet**: Implements STIG Requirements and Hardening for EMET on Windows 7 Systems.
- **updatemanagement**: Changes the way updates are managed and improved on the system.
- **deviceguard**: Enables Device Guard Hardening.
- **sosbrowsers**: Optimizes the system's web browsers.

An example of how to launch the script with specific parameters would be:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```
