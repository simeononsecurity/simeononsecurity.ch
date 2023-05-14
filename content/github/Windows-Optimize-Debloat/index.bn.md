---
title: "Windows-Optimize-Debloat দিয়ে আপনার Windows PC অপ্টিমাইজ করুন"
date: 2020-12-29
toc: true
draft: false
description: "Windows-Optimize-Debloat-এর মাধ্যমে আপনার Windows অপারেটিং সিস্টেমের কর্মক্ষমতা এবং গোপনীয়তা উন্নত করুন, একটি ব্যাপক স্ক্রিপ্ট যা bloatware অপসারণ করতে এবং সিস্টেম সেটিংস অপ্টিমাইজ করতে সাহায্য করে।"
tags: ["উইন্ডোজ-অপ্টিমাইজ-ডিব্লোট", "উইন্ডোজ অপ্টিমাইজেশান", "উইন্ডোজ ডিব্লোটিং", "উইন্ডোজের গতি বাড়ান", "উইন্ডোজ পারফরম্যান্স অপ্টিমাইজ করুন", "উইন্ডোজ পারফরম্যান্স বুস্ট", "উইন্ডোজ সিস্টেম অপ্টিমাইজেশান", "মাইক্রোসফট", "গোপনীয়তা", "Bloatware অপসারণ", "উইন্ডোজ 10", "উইন্ডোজ 11", "উইন্ডোজ ডিফেন্ডার", "উইন্ডোজ আপডেট", "কর্টোনা", "গ্রুপ পলিসি অবজেক্ট", "টেলিমেট্রি", "উইন্ডোজ স্টোর", "উইন্ডোজ 10 প্রফেশনাল", "উইন্ডোজ 10 হোম"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*যারা তাদের উইন্ডোজ 10 এবং 11 ইন্সটল মিনিমাইজ করতে চায় তাদের জন্য।*

**দ্রষ্টব্য:** এই স্ক্রিপ্টটি বেশিরভাগ ক্ষেত্রে কাজ করা উচিত, যদি সব না হয়, সমস্যা ছাড়াই সিস্টেমের জন্য। যখন[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) এই স্ক্রিপ্টটি চালাবেন না যদি আপনি বুঝতে না পারেন এটি কী করে।

## ভূমিকা:
Windows 10 এবং 11 হল আক্রমণাত্মক এবং অনিরাপদ অপারেটিং সিস্টেম বাক্সের বাইরে।
সংগঠনগুলো পছন্দ করে[Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) এবং অন্যরা Windows 10 অপারেটিং সিস্টেম অপ্টিমাইজ এবং ডিব্লোট করার জন্য কনফিগারেশন পরিবর্তনের সুপারিশ করেছে৷ এই পরিবর্তনগুলির মধ্যে রয়েছে টেলিমেট্রি ব্লক করা, লগ মুছে ফেলা এবং কয়েকটি নাম দেওয়ার জন্য ব্লোটওয়্যার অপসারণ করা। এই স্ক্রিপ্টটি সেই সংস্থাগুলির দ্বারা প্রস্তাবিত কনফিগারেশনগুলিকে স্বয়ংক্রিয় করার লক্ষ্য রাখে।

## মন্তব্য:
- এই স্ক্রিপ্টটি প্রাথমিকভাবে **ব্যক্তিগত ব্যবহার** পরিবেশে অপারেশনের জন্য ডিজাইন করা হয়েছে।
- এই স্ক্রিপ্টটি এমনভাবে ডিজাইন করা হয়েছে যে অপ্টিমাইজেশানগুলি, অন্য কিছু স্ক্রিপ্টের মতন, মূল উইন্ডোর কার্যকারিতা ভাঙ্গবে না।
 - Windows Update, Windows Defender, Windows Store, এবং Cortona-এর মতো বৈশিষ্ট্যগুলিকে সীমাবদ্ধ করা হয়েছে, কিন্তু বেশিরভাগ অন্যান্য Windows 10 গোপনীয়তা স্ক্রিপ্টের মতো অকার্যকর অবস্থায় নেই৷
- আপনি যদি শুধুমাত্র বাণিজ্যিক পরিবেশে লক্ষ্য করে একটি মিনিমাইজড স্ক্রিপ্ট চান, তাহলে অনুগ্রহ করে এটি দেখুন[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## প্রয়োজনীয়তা:
- [X] Windows 10/11 Enterprise, Windows 10 Professional, অথবা Windows 10 Home
  - উইন্ডোজ হোম GPO কনফিগারেশনের জন্য অনুমতি দেয় না।
    - স্ক্রিপ্ট এখনও কাজ করবে কিন্তু সব সেটিংস প্রযোজ্য হবে না।
  - উইন্ডোজ "এন" সংস্করণগুলি পরীক্ষা করা হয় না।
  - চালান[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) সর্বশেষ বড় রিলিজ আপডেট এবং যাচাই করতে।

## মাইক্রোসফ্ট অ্যাকাউন্ট বা এক্সবক্স পরিষেবাগুলি ঠিক করা:
কারণ আমরা মাইক্রোসফট অ্যাকাউন্টে সাইন ইন করা ব্লক করি। মাইক্রোসফ্টের টেলিমেট্রি এবং আইডেন্টিটি অ্যাসোসিয়েশন ভ্রুকুটি করা হয়েছে।
যাইহোক, আপনি যদি এখনও এই পরিষেবাগুলি ব্যবহার করতে চান তাহলে রেজোলিউশনের জন্য নিম্নলিখিত ইস্যু টিকিটগুলি দেখুন:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## এই সংগ্রহটি ব্যবহার করে স্ক্রিপ্ট এবং সরঞ্জামগুলির একটি তালিকা:
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## থেকে অতিরিক্ত কনফিগারেশন বিবেচনা করা হয়েছিল:
-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)

## কিভাবে স্ক্রিপ্ট চালাবেন:
### স্বয়ংক্রিয় ইনস্টল:
স্ক্রিপ্টটি বের করা গিটহাব ডাউনলোড থেকে এইভাবে চালু করা যেতে পারে:
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### Manual Install:
If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

The script "sos-optimize-windows.ps1" includes several parameters that allow for customization of the optimization process. Each parameter is a boolean value that defaults to true if not specified.

- **$cleargpos**: Clears Group Policy Objects settings.
- **$installupdates**: Installs updates to the system.
- **$removebloatware**: Removes unnecessary programs and features from the system.
- **$disabletelemetry**: Disables data collection and telemetry.
- **$privacy**: Makes changes to improve privacy.
- **$imagecleanup**: Cleans up unneeded files from the system.
- **$diskcompression**: Compresses the system disk.
- **$updatemanagement**: Changes the way updates are managed and improved on the system.
- **$sosbrowsers**: Optimizes the system's web browsers.

An example of how to launch the script with specific parameters would be:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

