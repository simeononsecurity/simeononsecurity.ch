---
title: "VirusTotal PowerShell মডিউল সহ দক্ষ ভাইরাস স্ক্যান"
date: 2020-11-24
toc: true
draft: false
description: "VirusTotal API এর সাথে মিথস্ক্রিয়া স্বয়ংক্রিয় করে এবং আপনার নিরাপত্তা কর্মপ্রবাহকে স্ট্রিমলাইন করে VirusTotal PowerShell মডিউলগুলির সাথে দক্ষ ভাইরাস স্ক্যানগুলি সম্পাদন করুন৷"
tags: ["পাওয়ারশেল মডিউল", "শক্তির উৎস", "অটোমেশন", "ভাইরাস টোটাল", "ভাইরাস স্ক্যান", "ডোমেইন স্ক্যান", "API কী", "VirusTotal API", "ভাইরাসটোটাল ডেভেলপার পেজ", "সিস্টেম অ্যাডমিনিস্ট্রেশন", "নিরাপত্তা কর্মপ্রবাহ", "দক্ষ ভাইরাস স্ক্যান", "ডাউনলোড এবং ইন্সটল", "GitHub সংগ্রহস্থল", "API ব্যবহারের উদাহরণ"]
---
 VirusTotal API এর সাথে ইন্টারঅ্যাক্ট করার জন্য PowerShell মডিউলের সংগ্রহ

**মন্তব্য:**
- আপনার VirusTotal API কী প্রয়োজন হবে, যা আপনার এ পাওয়া যাবে[Shodan Account](https://www.virustotal.com/gui/)
- মডিউলগুলিতে ব্যবহৃত API-এর উদাহরণ পাওয়া যেতে পারে[VirusTotal Developers Page](https://developers.virustotal.com/reference#getting-started)

## ডাউনলোড এবং ইন্সটল
- থেকে মডিউল ডাউনলোড করুন[GitHub Repository](https://github.com/simeononsecurity/VirusTotal-PS)
- সমস্ত মডিউল ইনস্টল করুন
```ps
Get-ChildItem -Recurse *.ps1 | Import-Module
```