---
title: "ভালো গোপনীয়তা এবং নিরাপত্তার জন্য Windows 10 সিস্টেম-ওয়াইড অ্যাড ব্লকার স্ক্রিপ্ট"
date: 2021-04-02
lastmod: 2026-11-23
toc: true
draft: false
description: "Windows-এ StevenBlack তালিকার ডোমেন ব্লক করুন। এই PowerShell স্ক্রিপ্ট আপনার নিজস্ব hosts এন্ট্রি অক্ষত রাখে।"
tags: ["উইন্ডোজ 10", "বিজ্ঞাপন প্রতিরোধক", "টেলিমেট্রি ব্লকিং", "পাওয়ারশেল স্ক্রিপ্ট", "সিস্টেম-ব্যাপী বিজ্ঞাপন-ব্লকিং", "গোপনীয়তা", "নিরাপত্তা"]
---

Windows-এ StevenBlack তালিকার ডোমেন ব্লক করুন। এই PowerShell স্ক্রিপ্ট আপনার নিজস্ব hosts এন্ট্রি অক্ষত রাখে।

## প্রস্তুতি ও পূর্বরূপ

সম্পূর্ণ রিপোজিটরি ডাউনলোড করে আনজিপ করুন। চালানোর আগে [GitHub README](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/blob/main/README.md) ও স্ক্রিপ্টটি পড়ুন। আনজিপ করা ফোল্ডার থেকে প্রশাসক হিসেবে Windows PowerShell 5.1 বা PowerShell 7 খুলুন। আগে অস্থায়ী Windows সিস্টেমে DNS ও প্রয়োজনীয় অ্যাপ পরীক্ষা করুন।

আগে পরিবর্তনের পূর্বরূপ দেখুন। প্রয়োগ করতে প্রস্তুত হলে দ্বিতীয় কমান্ডটি আলাদাভাবে চালান।

```powershell
.\sos-system-wide-windows-ad-block.ps1 -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1
```

## মূল hosts ফাইল পুনরুদ্ধার

আগে পুনরুদ্ধারের পূর্বরূপ দেখুন। প্রস্তুত হলে দ্বিতীয় কমান্ডটি আলাদাভাবে চালান।

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore
```

পুনরুদ্ধার সফল না হওয়া পর্যন্ত ব্যাকআপ অক্ষত রাখুন। প্রয়োগের পর কেউ বা কোনো অ্যাপ hosts ফাইল সম্পাদনা করলে পুনরুদ্ধার থেমে যায়। আবার চেষ্টা করার আগে পরিবর্তনগুলো সংরক্ষণ ও সমন্বয় করুন।

## ব্লক তালিকা

- [StevenBlack/hosts](https://github.com/StevenBlack/hosts)
- [সমস্যা জানান](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues)
