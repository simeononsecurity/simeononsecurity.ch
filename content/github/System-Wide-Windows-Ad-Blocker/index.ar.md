---
title: "Windows 10 System-Wide Ad Blocker Script for Better Privacy and Security"
date: 2021-04-02
toc: true
draft: false
description: "Block ads, trackers, and telemetry on Windows 10 using this powerful PowerShell script that utilizes the hosts file and Windows Firewall for system-wide ad-blocking."
tags: ["Windows 10", "ad-blocker", "telemetry blocking", "PowerShell script", "system-wide ad-blocking", "privacy", "security", "EasyList", "Easy Privacy", "NoCoin Filter List", "AdGuard DNS filter", "YoYo Lists", "Peter Lowe's ad/tracking/malware servers", "Windows Firewall", "domain lists", "block Windows trackers", "block trackers", "block ads", "block tracking"]
---
```powershell
iwr -useb 'https://raw.githubusercontent.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/main/sos-system-wide-windows-ad-block.ps1' | iex
```

 ## وصف: هذا البرنامج الخاص بالعقار.  ** ملحوظة: ** - دورا دورا في إضافة هذه المجالات إلى تعطيل برامج معينة مثل iTunes أو Skype - تم باسم الإدخالات المتعلقة بـ Akamai تسبب مشاكل مع Widevine DRM  ### نسخ التقارير: - [EasyList] (https://easylist.to/easylist/easylist.txt) / [JustDomains - EasyList] (https://justdomains.github.io/blocklists/lists/easylist-justdomains.txt) - [Easy Privacy] (https://easylist.to/easylist/easyprivacy.txt) / [JustDomains - EasyPrivacy] (https://justdomains.github.io/blocklists/lists/easyprivacy-justdomains.txt) - [قائمة تصفية NoCoin] (https://github.com/hoshsadiq/adblock-nocoin-list/) / [JustDomains - قائمة تصفية NoCoin] (https://justdomains.github.io/blocklists/lists/nocoin-justdomains .رسالة قصيرة) - [مرشح AdGuard DNS] (https://github.com/AdguardTeam/AdguardSDNSFilter) / [JustDomains - AdGuard Simplified Domain Names Filter] (https://justdomains.github.io/blocklists/lists/adguarddns-justdomains.txt) - [قوائم يو] (https://pgl.yoyo.org/adservers/serverlist.php) - [خوادم الإعلانات / نقاط البرامج / البرامج لبيتر لوي] (https://pgl.yoyo.org/adservers/policy.php)  ### مثال:  قم بإصدار أحدث من البرنامج تلقائيًا: