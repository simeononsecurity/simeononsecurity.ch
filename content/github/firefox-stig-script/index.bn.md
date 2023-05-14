---
title: "PowerShell স্ক্রিপ্টগুলির সাথে স্বয়ংক্রিয় FireFox STIG সম্মতি"
date: 2020-08-15
---

ফায়ারফক্স STIG স্ক্রিপ্ট

দ্য[Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip) STIG-এর আবেদন করা সবচেয়ে সহজ নয়।
এই স্ক্রিপ্টটি ফায়ারফক্সের বেশিরভাগ প্রয়োজনীয় নীতি বাস্তবায়ন করবে। ভবিষ্যতে, ফায়ারফক্স ADMX টেমপ্লেট এবং GPO এই স্ক্রিপ্টে প্রয়োগ করা হবে।

**কাজ চলছে**

## প্রয়োজনীয় ফাইল ডাউনলোড করুন

থেকে প্রয়োজনীয় ফাইল ডাউনলোড করুন[GitHub Repository](https://github.com/simeononsecurity/FireFox-STIG-Script)

## কিভাবে স্ক্রিপ্ট চালাতে হয়


**নিষ্কৃত গিটহাব ডাউনলোড থেকে স্ক্রিপ্টটি এভাবে চালু করা যেতে পারে:**
```
.\sos-firefoxstig.ps1
```