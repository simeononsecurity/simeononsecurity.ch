---
title: "উইন্ডোজ কমান্ড প্রম্পট এবং পাওয়ারশেল হার্ডেনিং"
date: 2020-11-18
toc: true
draft: false
description: "আমাদের ব্যাপক হার্ডেনিং স্ক্রিপ্ট এবং ডকুমেন্টেশন সহ, সিস্টেমের নিরাপত্তা এবং সম্মতি বৃদ্ধি করে উইন্ডোজ কমান্ড প্রম্পট এবং পাওয়ারশেলকে সুরক্ষিত করুন।"
tags: ["শক্তির উৎস", "শক্ত করা", "উইন্ডোজ কমান্ড প্রম্পট", "নিরাপত্তা", "কমপ্লায়েন্স", "অটোমেশন", "সীমাবদ্ধ ভাষা মোড", "পাওয়ারশেল লগিং", "পাওয়ারশেল স্ক্রিপ্ট", "WSMAN", "পিএস রিমোটিং", "এন্টারপ্রাইজ নিরাপত্তা", "নীল দল", "সাইবার নিরাপত্তা", "সেরা অনুশীলন", "কমান্ড প্রম্পট অক্ষম করুন", "PowerShell v2 অক্ষম করুন", "GitHub সংগ্রহস্থল", "উইন্ডোজ ডিফেন্ডার", "মাইক্রোসফট"]
---
 এবং উইন্ডোজ কমান্ড প্রম্পট এবং পাওয়ারশেল শক্ত করার জন্য ডকুমেন্টেশন

## এই স্ক্রিপ্ট কি করে?
- কমান্ড প্রম্পট নিষ্ক্রিয় করে
- পাওয়ারশেল v2 অক্ষম করে
- WSMAN এবং PRemoting অক্ষম করে
- পাওয়ারশেল সীমাবদ্ধ ভাষা মোড সক্ষম করে
- পাওয়ারশেল লগিং সক্ষম করে

## প্রস্তাবিত পঠন:
-[PowerShell Best Practices](https://www.digitalshadows.com/blog-and-research/powershell-security-best-practices/)
-[PowerShell Constrained Language Mode](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)
-[Securing PowerShell in the Enterprise](https://www.cyber.gov.au/acsc/view-all-content/publications/securing-powershell-enterprise)
-[Windows Defender Hardening](https://github.com/simeononsecurity/Windows-Defender-Hardening)

## প্রয়োজনীয় ফাইল ডাউনলোড করুন:

থেকে প্রয়োজনীয় ফাইল ডাউনলোড করুন[GitHub Repository](https://github.com/simeononsecurity/Windows-Terminal-Hardening)

## কিভাবে স্ক্রিপ্ট চালাবেন:

**নিষ্কৃত গিটহাব ডাউনলোড থেকে স্ক্রিপ্টটি এভাবে চালু করা যেতে পারে:**
```
.\sos-windowsterminalhardening.ps1
```
