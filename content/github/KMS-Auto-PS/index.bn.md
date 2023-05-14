---
title: "GLVK স্ক্রিপ্ট সহ উইন্ডোজ কেএমএস অ্যাক্টিভেশন স্বয়ংক্রিয় করুন"
date: 2020-12-18
toc: true
draft: false
description: "SimeonOnSecurity-এর GLVK অটো ইন্সটল স্ক্রিপ্ট ব্যবহার করে Windows 10 KMS অ্যাক্টিভেশন প্রক্রিয়া সহজ করুন এবং Microsoft-এর প্রস্তাবিত রিডিং থেকে KMS এবং GLVK ক্লায়েন্ট কী সম্পর্কে আরও জানুন।"
tags: ["উইন্ডোজ অ্যাক্টিভেশন", "KMS ক্লায়েন্ট কী", "জিএলভিকে", "উইন্ডোজ আপডেট", "কমপ্লায়েন্স", "পাওয়ারশেল স্ক্রিপ্ট", "কী ব্যবস্থাপনা পরিষেবা", "ভলিউম লাইসেন্সিং", "এন্টারপ্রাইজ অ্যাক্টিভেশন", "কী ম্যানেজমেন্ট সার্ভার", "অটোমেশন", "মাইক্রোসফট পণ্য", "অপারেটিং সিস্টেম", "সফটওয়্যার", "এন্টারপ্রাইজ পরিবেশ", "প্রশাসনিক পাওয়ারশেল", "GitHub সংগ্রহস্থল", "স্ক্রিপ্টিং", "সাইবার নিরাপত্তা", "সিমেনঅনসিকিউরিটি"]
---

KMS অ্যাক্টিভেশনের জন্য GLVK অটো ইন্সটল স্ক্রিপ্ট

## প্রস্তাবিত পড়া:
-[Microsoft - KMS Client Keys (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## কিভাবে স্ক্রিপ্ট চালাবেন:
### ম্যানুয়াল ইন্সটল:
যদি ম্যানুয়ালি ডাউনলোড করা হয়, স্ক্রিপ্টটি অবশ্যই একটি প্রশাসনিক পাওয়ারশেল থেকে লঞ্চ করতে হবে যেটির মধ্যে থাকা সমস্ত ফাইল রয়েছে[GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```ps
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```
