---
title: "উত্তরযোগ্য STIG প্লেবুকগুলির সাথে উইন্ডোজ সম্মতি স্বয়ংক্রিয় করুন৷"
date: 2022-04-26
toc: true
draft: false
description: "Windows সিস্টেমের জন্য Ansible STIG Playbooks-এর সাথে আপনার নিরাপত্তা সম্মতি স্ট্রীমলাইন করুন।"
tags: ["অটোমেশন", "উইন্ডোজ কমপ্লায়েন্স", "উত্তরযোগ্য STIG প্লেবুক", "উইন্ডোজ হার্ডেনিং", "STIG স্ক্রিপ্ট", "STIG সম্মতি", "উত্তরযোগ্য গ্যালাক্সি", "শক্তির উৎস", "পাওয়ারশেল স্ক্রিপ্ট", "উইন্ডোজ সার্ভার", "উইন্ডোজ ডিফেন্ডার", ".নেট", "ফায়ারফক্স", "ওরাকল জেআরই 8", "অ্যাডোব রিডার ডিসি", "ইন্টারনেট সংযোগ", "অফলাইন সামঞ্জস্য", "নিরাপত্তা কঠোরকরণ", "উইন্ডোজ নিরাপত্তা"]
---


SimeonOnSecurity-এর STIG স্ক্রিপ্টের জন্য উত্তরযোগ্য প্লেবুক

## মন্তব্য:

- বর্তমানে ইন্টারনেট সংযোগ প্রয়োজন। (অফলাইন সামঞ্জস্য WIP)

## ব্যবহার:

## স্থাপন:

-[Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

```bash
ansible-galaxy collection install simeononsecurity.windows_stigs
```

## এর উপর ভিত্তি করে:

-[simeononsecurity/STIG-Compliant-Domain-Prep](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep)
-[simeononsecurity/Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[simeononsecurity/Standalone-Windows-Server-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-Server-STIG-Script)
-[simeononsecurity/Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[simeononsecurity/.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[simeononsecurity/FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[simeononsecurity/Oracle-JRE-8-STIG-Script](https://github.com/simeononsecurity/Oracle-JRE-8-STIG-Script)
-[simeononsecurity/Adobe-Reader-DC-STIG-Script](https://github.com/simeononsecurity/Adobe-Reader-DC-STIG-Script)
