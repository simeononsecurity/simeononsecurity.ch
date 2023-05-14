---
title: "অফলাইনে RSAT ActiveDirectory PowerShell মডিউল ইনস্টল করুন"
date: 2020-12-16
draft: false
toc: true
description: "একটি সাধারণ PowerShell স্ক্রিপ্টের সাথে অফলাইনে RSAT ActiveDirectory PowerShell মডিউল কীভাবে ইনস্টল করবেন তা শিখুন।"
tags: ["রিমোট সার্ভার অ্যাডমিনিস্ট্রেশন টুলকিট", "PowerShell RSAT ActiveDirectory মডিউল", "উইন্ডোজ 10", "অফলাইন ইনস্টলার", "পাওয়ারশেল স্ক্রিপ্ট", "পাওয়ারশেল মডিউল", "অ্যাক্টিভ ডাইরেক্টরি", "উইন্ডোজ", "অফলাইন", "ইনস্টল করুন", "সার্ভার", "প্রশাসন", "টুলকিট", "স্ক্রিপ্টিং", "মডিউল", "উইন্ডোজ সার্ভার", "পাওয়ারশেল কোর", "উইন্ডোজ পাওয়ারশেল", "মাইক্রোসফট", "আইটি প্রশাসন"]
---

 PowerShell RSAT ActiveDirectory মডিউল অফলাইনে ইনস্টল করুন

### কিভাবে ইনস্টল করতে হবে:
1.[Download the script](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install/archive/master.zip)
2. নিষ্কাশিত ফোল্ডার থেকে, চালান```.\sos-offlinepsadinstall.ps1```

```powershell
#Require elivation for script run
#Requires -RunAsAdministrator

#Copy Files
#Install PowerShell Modules
Copy-Item -Path .\Files\ActiveDirectory -Destination "C:\Windows\System32\WindowsPowerShell\v1.0\Modules\" -Force -Recurse
#Install Required DLLs
Copy-Item -Path .\Files\WinSxS\* -Destination "C:\Windows\WinSxS\" -Force -Recurse

#Unblock New PowerShell Modules and DLLs
Get-ChildItem "C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\" -recurse | Unblock-File
Unblock-File -Path "C:\Windows\WinSxS\Microsoft.ActiveDirectory.Management.resources.dll"
Unblock-File -Path "C:\Windows\WinSxS\Microsoft.ActiveDirectory.Management.dll"

#Install PowerShell Modules and DLLs
Import-Module -Name ActiveDirectory -Force -Global
Import-Module "C:\Windows\WinSxS\Microsoft.ActiveDirectory.Management.resources.dll" -Force -Global
Import-Module "C:\Windows\WinSxS\Microsoft.ActiveDirectory.Management.dll" -Force -Global
```
