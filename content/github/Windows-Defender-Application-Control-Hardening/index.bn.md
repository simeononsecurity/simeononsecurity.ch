---
title: "উইন্ডোজ ডিফেন্ডার অ্যাপ্লিকেশন কন্ট্রোল WDAC-এর সাথে উইন্ডোজ শক্ত করার সম্পূর্ণ নির্দেশিকা"
date: 2020-12-16
toc: true
draft: false
description: "আপনার উইন্ডোজ অপারেটিং সিস্টেমকে স্ক্রিপ্ট এবং টুল দিয়ে শক্ত করতে কীভাবে উইন্ডোজ ডিফেন্ডার অ্যাপ্লিকেশন কন্ট্রোল WDAC ব্যবহার করবেন তা শিখুন।"
tags: ["উইন্ডোজ ডিফেন্ডার অ্যাপ্লিকেশন কন্ট্রোল WDAC হার্ডেনিং", "শক্তির উৎস", "পাওয়ারশেল স্ক্রিপ্ট", "অটোমেশন", "কমপ্লায়েন্স", "ব্লু-টিম", "উইন্ডোজ ডিফেন্ডার STIG স্ক্রিপ্ট", "উইন্ডোজ ডিফেন্ডার হার্ডেনিং", "উইন্ডোজ ডিফেন্ডার STIG", "ডিফেন্ডার STIG", "উইন্ডোজ ডিফেন্ডার শোষণ সুরক্ষা WDEP", "উইন্ডোজ ডিফেন্ডার অ্যাটাক সারফেস রিডাকশন এএসআর", "উইন্ডোজ সার্ভার 2016 2019", "উইন্ডোজ সার্ভার কোর", "Microsoft WDAC-Toolkit", "CI নীতি রিফ্রেশ করুন", "Microsoft প্রস্তাবিত ব্লক নিয়ম", "মাইক্রোসফ্ট সুপারিশকৃত ড্রাইভার ব্লক নিয়ম", "XML নীতি", "BIN নীতি", "সম্মিলিত নীতি", "Microsoft Intune"]
---

**উইন্ডোজ ডিফেন্ডার অ্যাপ্লিকেশন কন্ট্রোল ডব্লিউডিএসি সহ হার্ড উইন্ডোজ**

## মন্তব্য:
- উইন্ডোজ সার্ভার 2016/2019 বা সংস্করণ 1903 এর আগে যেকোন কিছু শুধুমাত্র একবারে একটি একক উত্তরাধিকার নীতি সমর্থন করে।
- উইন্ডোজ সার্ভার কোর সংস্করণ WDAC সমর্থন করে তবে অ্যাপলকারের উপর নির্ভর করে এমন কিছু উপাদান কাজ করবে না
- অনুগ্রহ করে পড়ুন[Recommended Reading](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening#recommended-reading) বাস্তবায়ন বা এমনকি পরীক্ষার আগে।

## এই সংগ্রহটি ব্যবহার করে স্ক্রিপ্ট এবং সরঞ্জামগুলির একটি তালিকা:

-[MicrosoftDocs - WDAC-Toolkit](https://github.com/MicrosoftDocs/WDAC-Toolkit)
-[Microsoft - Refresh CI Policy ](https://www.microsoft.com/en-us/download/details.aspx?id=102925)

## থেকে অতিরিক্ত কনফিগারেশন বিবেচনা করা হয়েছিল:

-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)

## ব্যাখ্যাঃ

### XML বনাম BIN:

- সহজ কথায়, **"XML"** নীতিগুলি একটি মেশিনে স্থানীয়ভাবে আবেদন করার জন্য এবং **"BIN"** ফাইলগুলি যেকোন একটি দিয়ে প্রয়োগ করার জন্য[Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) or [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) আপনি যখন স্থানীয় স্থাপনায় XML, BIN, বা CIP নীতিগুলি ব্যবহার করতে পারেন, সাধারণভাবে বলতে গেলে আপনাকে XML-এ লেগে থাকা উচিত যেখানে সম্ভব এবং বিশেষ করে অডিট বা সমস্যা সমাধানের সময়।

### নীতি বর্ণনা:

- **ডিফল্ট নীতি:**
  - "ডিফল্ট" নীতিগুলি শুধুমাত্র WDAC-Toolkit-এ উপলব্ধ ডিফল্ট বৈশিষ্ট্যগুলি ব্যবহার করে৷
- **প্রস্তাবিত নীতি:**
  - "প্রস্তাবিত" নীতিগুলি ডিফল্ট বৈশিষ্ট্যগুলির পাশাপাশি Microsoft-এর প্রস্তাবিত বৈশিষ্ট্যগুলি ব্যবহার করে৷[blocks](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules) and [driver block](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules) নিয়ম
- **অডিট নীতি:**
  - "অডিট" নীতিগুলি, নিয়মগুলির ব্যতিক্রমগুলি লগ করুন৷ এটি আপনার পরিবেশে পরীক্ষার জন্য, যাতে আপনি আপনার পরিবেশের প্রয়োজনের সাথে মানানসই নীতিগুলি পরিবর্তন করতে পারেন।
- **প্রবর্তিত নীতি:**
  - "প্রবর্তিত" নীতিগুলি নিয়মগুলির কোনও ব্যতিক্রমের অনুমতি দেবে না, অ্যাপ্লিকেশন, ড্রাইভার, dll, ইত্যাদি মেনে না চললে ব্লক করা হবে৷

### উপলব্ধ নীতি:

- **XML:**
  - **শুধুমাত্র নিরীক্ষা:**
    - `WDAC_V1_Default_Audit_{version}.xml`
    - `WDAC_V1_Recommended_Audit_{version}.xml`
  - **জোরপূর্বক:**
    - `WDAC_V1_Default_Enforced_{version}.xml`
    - `WDAC_V1_Recommended_Enforced_{version}.xml`
- **বিন:**
  - **শুধুমাত্র নিরীক্ষা:**
    - `WDAC_V1_Default_Audit_{version}.bin`
    - `WDAC_V1_Recommended_Audit_{version}.bin`
  - **জোরপূর্বক:**
    - `WDAC_V1_Default_Enforced_{version}.bin`
    - `WDAC_V1_Recommended_Enforced_{version}.bin`
- **সিআইপি:**
  - **শুধুমাত্র নিরীক্ষা:**
    - `WDAC_V1_Default_Audit\{uid}.cip`
    - `WDAC_V1_Recommended_Audit\{uid}.cip`
  - **জোরপূর্বক:**
    - `WDAC_V1_Default_Enforced\{uid}.cip`
    - `WDAC_V1_Recommended_Enforced\{uid}.cip`

আপনি স্থানীয়ভাবে যে নীতিটি চান তা ব্যবহার করতে স্ক্রিপ্টে নিম্নলিখিত লাইনটি আপডেট করুন:

```powershell
$PolicyPath = "C:\temp\Windows Defender\CIP\WDAC_V1_Recommended_Enforced\*.cip"
#https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script
ForEach ($Policy in (Get-ChildItem -Recurse $PolicyPath).Fullname) {
  $PolicyBinary = "$Policy"
  $DestinationFolder = $env:windir+"\System32\CodeIntegrity\CIPolicies\Active\"
  $RefreshPolicyTool = "./Files/EXECUTABLES/RefreshPolicy(AMD64).exe"
  Copy-Item -Path $PolicyBinary -Destination $DestinationFolder -Force
  & $RefreshPolicyTool
}
```

Alternatively, you may use [Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) or [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) to enforce the WDAC policies.

## Auditing:

You can view the WDAC event logs in event viewer under:

`Applications and Services Logs\Microsoft\Windows\CodeIntegrity\Operational`

## Recommended Reading:

- [Argonsys - Deploying Windows 10 Application Control Policy](https://argonsys.com/microsoft-cloud/library/deploying-windows-10-application-control-policy/)
- [Microsoft - Audit Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/audit-windows-defender-application-control-policies)
- [Microsoft - Create a WDAC policy for fixed-workload devices using a reference computer](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [Microsoft - Deploy Windows Defender Application Control policies by using Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy)
- [Microsoft - Deploy Windows Defender Application Control policies by using Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune)
- [Microsoft - Deploy WDAC policies using script](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [Microsoft - Enforce Windows Defencer Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/enforce-windows-defender-application-control-policies)
- [Microsoft - Guidance on Creating WDAC Deny Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [Microsoft - Use multiple Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)

## How to run the script:

### Manual Install:

If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening/archive/main.zip)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-wdachardening.ps1
```
