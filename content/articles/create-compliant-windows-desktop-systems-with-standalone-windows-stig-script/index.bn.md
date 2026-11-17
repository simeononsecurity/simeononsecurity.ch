---
title: "Standalone-Windows-STIG-Script: একটি অনুবর্তী কম্পিউটার তৈরি করুন"
date: 2023-02-02
lastmod: 2026-11-09
toc: true
draft: false
description: "পরামিতি ও যাচাইয়ের ধাপসহ, অনুবর্তী Windows সিস্টেম তৈরিতে Standalone-Windows-STIG-Script ব্যবহারের ধাপে ধাপে নির্দেশিকা।"
tags: ["STIG স্ক্রিপ্ট", "Windows নিরাপত্তা", "অনুবর্তী Windows সিস্টেম", "সিস্টেম হার্ডেনিং", "Windows STIG", "নিরাপদ Windows", "Windows অনুবর্তিতা", "ম্যানুয়াল ইনস্টলেশন", "Windows আপডেট", "Adobe Reader", "Firefox", "Chrome", "Internet Explorer 11", ".NET Framework", "Office", "OneDrive", "Java", "Windows Defender", "Windows Firewall", "প্রশমন ব্যবস্থা", "Nessus PID", "VMware Horizon", "ঐচ্ছিক হার্ডেনিং"]
cover: "/img/cover/create-compliant-windows-desktop-systems-with-standalone-windows-stig-script.webp"
coverAlt: "গাঢ় নেভি পটভূমিতে উজ্জ্বল রঙের অগ্রগতি বার ও ডেটা প্রবাহসহ নিরাপত্তা অনুবর্তিতা ইন্টারফেস দেখানো কম্পিউটার পর্দার চিত্র।"
coverCaption: ""
---

ব্যবসা প্রতিষ্ঠান, সংস্থা, এমনকি বাড়িতেও Windows সিস্টেম বহুল ব্যবহৃত। সাইবার আক্রমণ বাড়ার সঙ্গে সঙ্গে এসব সিস্টেম নিরাপদ এবং শিল্পমানের সঙ্গে সামঞ্জস্যপূর্ণ রাখা জরুরি। Standalone-Windows-STIG-Script এ কাজে সহায়তা করে। এই নিবন্ধে স্ক্রিপ্টটি কী, কীভাবে কাজ করে এবং নিরাপদ ও অনুবর্তী Windows সিস্টেম তৈরি করতে কীভাবে ব্যবহার করবেন তা ব্যাখ্যা করা হয়েছে।

## Standalone-Windows-STIG-Script কী?

**Standalone-Windows-STIG-Script** হলো Simeononsecurity-এর তৈরি একটি স্ক্রিপ্ট। এটি Security Technical Implementation Guide (STIG) অনুযায়ী Windows সিস্টেম সুরক্ষিত করার কাজ স্বয়ংক্রিয় করে। স্ক্রিপ্টটি ওপেন সোর্স এবং **GitHub**-এ পাওয়া যায়।

## এটি কীভাবে কাজ করে?

Windows সিস্টেম সুরক্ষিত করতে Standalone-Windows-STIG-Script STIG-এর নির্দেশনা প্রয়োগ করে। Windows সিস্টেমে স্ক্রিপ্টটি চালালে STIG মেনে চলার জন্য প্রয়োজনীয় পরিবর্তনগুলো করা হয়। এতে নানা নিরাপত্তা ব্যবস্থা রয়েছে, যেমন:

- অ্যাকাউন্ট নীতি
- অডিট নীতি
- নিরাপত্তা বিকল্প
- ফায়ারওয়াল সেটিংস
- সার্ভিস সেটিংস

## Standalone-Windows-STIG-Script ব্যবহারের সুবিধা:

- **স্বয়ংক্রিয়করণ**: স্ক্রিপ্টটি Windows সিস্টেম সুরক্ষার প্রক্রিয়া স্বয়ংক্রিয় করে, এতে সময় বাঁচে এবং মানুষের ভুলের ঝুঁকি কমে।

- **অনুবর্তিতা**: স্ক্রিপ্টটি STIG-এর নির্দেশনা প্রয়োগ করে, ফলে Windows সিস্টেম শিল্পমানের সঙ্গে সামঞ্জস্যপূর্ণ হয়।

- **নিশ্চিন্ততা**: Standalone-Windows-STIG-Script ব্যবহার করলে আপনার Windows সিস্টেম নিরাপদ এবং শিল্পমানের সঙ্গে সামঞ্জস্যপূর্ণ। এ বিষয়ে নিশ্চিন্ত থাকতে পারেন।

_________________________________________________________________________________________________________________________

## Standalone-Windows-STIG-Script কীভাবে ব্যবহার করবেন:

1. Standalone-Windows-STIG-Script ব্যবহার করা তুলনামূলক সহজ। স্ক্রিপ্টটি ব্যবহারের ধাপগুলো নিচে দেওয়া হলো:

2. **স্ক্রিপ্ট ডাউনলোড করুন**: GitHub-এ https://github.com/simeononsecurity/Standalone-Windows-STIG-Script ঠিকানায় স্ক্রিপ্টটি পাওয়া যায়। ডাউনলোড করে আপনার Windows সিস্টেমে সংরক্ষণ করুন।

3. **উচ্চতর অধিকারসহ কমান্ড প্রম্পট খুলুন**: Windows Start বোতামে ডান-ক্লিক করে "Windows PowerShell (Admin)" নির্বাচন করুন।

4. **স্ক্রিপ্ট চালান**: স্ক্রিপ্টটি যেখানে সংরক্ষণ করেছেন সেখানে যান এবং নিচের কমান্ড দিয়ে চালান:

```powershell
powershell.exe -ExecutionPolicy Bypass -File Standalone-Windows-STIG-Script.ps1
```

5. পরিবর্তনগুলো পর্যালোচনা করুন: স্ক্রিপ্ট শেষ হলে সিস্টেমে করা পরিবর্তনগুলো দেখে নিন, যাতে সবকিছু সঠিকভাবে কনফিগার হয়েছে কি না নিশ্চিত হন।

## উপসংহার:

Standalone-Windows-STIG-Script একটি কার্যকর সরঞ্জাম, যা Windows সিস্টেম সুরক্ষিত করতে এবং শিল্পমান মেনে চলতে সহায়তা করে। এটি সুরক্ষার কাজ স্বয়ংক্রিয় করে এবং STIG নির্দেশনা প্রয়োগে সাহায্য করে। নিরাপদ ও অনুবর্তী Windows সিস্টেম তৈরি করতে চাইলে Standalone-Windows-STIG-Script ব্যবহারের কথা বিবেচনা করুন।
