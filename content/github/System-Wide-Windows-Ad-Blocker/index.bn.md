---
title: "ভালো গোপনীয়তা এবং নিরাপত্তার জন্য Windows 10 সিস্টেম-ওয়াইড অ্যাড ব্লকার স্ক্রিপ্ট"
date: 2021-04-02
toc: true
draft: false
description: "এই শক্তিশালী PowerShell স্ক্রিপ্ট ব্যবহার করে Windows 10-এ বিজ্ঞাপন, ট্র্যাকার এবং টেলিমেট্রি ব্লক করুন যা সিস্টেম-ওয়াইড অ্যাড-ব্লকিংয়ের জন্য হোস্ট ফাইল এবং উইন্ডোজ ফায়ারওয়াল ব্যবহার করে।"
tags: ["উইন্ডোজ 10", "বিজ্ঞাপন প্রতিরোধক", "টেলিমেট্রি ব্লকিং", "পাওয়ারশেল স্ক্রিপ্ট", "সিস্টেম-ব্যাপী বিজ্ঞাপন-ব্লকিং", "গোপনীয়তা", "নিরাপত্তা", "ইজিলিস্ট", "সহজ গোপনীয়তা", "NoCoin ফিল্টার তালিকা", "AdGuard DNS ফিল্টার", "YoYo তালিকা", "পিটার লো এর বিজ্ঞাপন ট্র্যাকিং ম্যালওয়্যার সার্ভার", "উইন্ডোজ ফায়ারওয়াল", "ডোমেইন তালিকা", "উইন্ডোজ ট্র্যাকার ব্লক করুন", "ব্লক ট্র্যাকার", "বিজ্ঞাপন ব্লক করুন", "ব্লক ট্র্যাকিং"]
---

## বর্ণনা:
এই স্ক্রিপ্টটি হোস্ট ফাইলের মাধ্যমে টেলিমেট্রি সম্পর্কিত ডোমেন এবং উইন্ডোজ ফায়ারওয়ালের মাধ্যমে সম্পর্কিত আইপি ব্লক করে।

**মন্তব্য:**
- এই ডোমেইনগুলি যোগ করলে আইটিউনস বা স্কাইপের মতো নির্দিষ্ট সফ্টওয়্যারগুলি ভেঙে যেতে পারে৷
- Akamai-এর সাথে সম্পর্কিত এন্ট্রিগুলি Widevine DRM-এর সাথে সমস্যা সৃষ্টি করে বলে রিপোর্ট করা হয়েছে

### ব্যবহৃত তালিকা:
-[EasyList](https://easylist.to/easylist/easylist.txt) / [JustDomains - EasyList](https://justdomains.github.io/blocklists/lists/easylist-justdomains.txt)
-[Easy Privacy](https://easylist.to/easylist/easyprivacy.txt) / [JustDomains - EasyPrivacy](https://justdomains.github.io/blocklists/lists/easyprivacy-justdomains.txt)
-[NoCoin Filter List](https://github.com/hoshsadiq/adblock-nocoin-list/) / [JustDomains - NoCoin Filter List](https://justdomains.github.io/blocklists/lists/nocoin-justdomains.txt)
-[AdGuard DNS filter](https://github.com/AdguardTeam/AdguardSDNSFilter) / [JustDomains - AdGuard Simplified Domain Names Filter](https://justdomains.github.io/blocklists/lists/adguarddns-justdomains.txt)
-[YoYo Lists](https://pgl.yoyo.org/adservers/serverlist.php)
-[Peter Lowe’s ad/tracking/malware servers](https://pgl.yoyo.org/adservers/policy.php)

### উদাহরণ:

স্ক্রিপ্টের সর্বশেষ সংস্করণটি স্বয়ংক্রিয়ভাবে চালান:
```powershell
iwr -useb 'https://raw.githubusercontent.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/main/sos-system-wide-windows-ad-block.ps1' | iex
```
