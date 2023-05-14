---
title: "পাওয়ারশেল স্ক্রিপ্টের সাথে Windows 10 STIG কমপ্লায়েন্স স্বয়ংক্রিয় করা"
date: 2020-08-26
---

** থেকে প্রয়োজনীয় সকল ফাইল ডাউনলোড করুন[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**আমরা নিম্নলিখিত বিষয়ে সাহায্য চাইছি[.Net issue](https://github.com/simeononsecurity/W10-Optimize-and-Harden/issues/3) 

## ভূমিকা:

Windows 10 বাক্সের বাইরে অনিরাপদ অপারেটিং সিস্টেম এবং বীমা করার জন্য অনেক পরিবর্তন প্রয়োজন[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) সম্মতি
সংগঠনগুলো পছন্দ করে[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) অপারেটিং সিস্টেমকে লকডাউন, কঠোর এবং সুরক্ষিত করতে এবং সরকারী সম্মতি নিশ্চিত করতে কনফিগারেশন পরিবর্তনের সুপারিশ করেছে এবং প্রয়োজনীয়। এই পরিবর্তনগুলি টেলিমেট্রি ব্লক করা, ম্যাক্রো, ব্লোটওয়্যার অপসারণ এবং একটি সিস্টেমে অনেক শারীরিক আক্রমণ প্রতিরোধ সহ বিস্তৃত প্রশমনকে কভার করে।

স্বতন্ত্র সিস্টেমগুলি সুরক্ষিত করা সবচেয়ে কঠিন এবং বিরক্তিকর সিস্টেমগুলির মধ্যে কয়েকটি। স্বয়ংক্রিয় না হলে, তাদের প্রতিটি STIG/SRG-এর ম্যানুয়াল পরিবর্তন প্রয়োজন। একটি সাধারণ স্থাপনায় মোট 1000 টির বেশি কনফিগারেশন পরিবর্তন এবং প্রতি পরিবর্তনে গড়ে 5 মিনিট যা 3.5 দিনের কাজের সমান। এই স্ক্রিপ্টটি সেই প্রক্রিয়াটিকে উল্লেখযোগ্যভাবে গতিশীল করার লক্ষ্য রাখে।

## মন্তব্য:

- এই স্ক্রিপ্টটি **এন্টারপ্রাইজ** পরিবেশে অপারেশনের জন্য ডিজাইন করা হয়েছে এবং ধরে নিচ্ছে যে আপনার কাছে সমস্ত প্রয়োজনীয়তার জন্য হার্ডওয়্যার সমর্থন রয়েছে৷
  - ব্যক্তিগত সিস্টেমের জন্য এটি দেখুন[GitHub Repository](https://github.com/simeononsecurity/W10-Optimize-and-Harden)
- এই স্ক্রিপ্টটি একটি সিস্টেমকে 100% কমপ্লায়েন্সে আনার জন্য ডিজাইন করা হয়নি, বরং এটিকে বেশিরভাগ সম্পূর্ণ করার জন্য একটি স্টেপিং স্টোন হিসাবে ব্যবহার করা উচিত, যদি সব না হয়, স্ক্রিপ্ট করা যেতে পারে এমন কনফিগারেশন পরিবর্তন করে।
  - মাইনাস সিস্টেম ডকুমেন্টেশন, এই সংগ্রহটি আপনাকে প্রযোজ্য সমস্ত STIGS/SRG-তে প্রায় 95% কমপ্লায়েন্স নিয়ে আসবে।

## প্রয়োজনীয়তা:
- [X] Windows 10 এন্টারপ্রাইজ প্রতি STIG এর জন্য **প্রয়োজনীয়**।
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) একটি অত্যন্ত সুরক্ষিত Windows 10 ডিভাইসের জন্য
-[x] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - বর্তমানে Windows 10 **v1909** বা **v2004**।
  - চালান[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) আপডেট করা এবং সর্বশেষ বড় রিলিজ যাচাই করা.
- [এক্স] হার্ডওয়্যারের প্রয়োজনীয়তা
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)
  
## প্রস্তাবিত পড়ার উপাদান:
  -[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  -[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  -[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  -[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  -[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  -[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## এই সংগ্রহটি ব্যবহার করে স্ক্রিপ্ট এবং সরঞ্জামগুলির একটি তালিকা:

-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)

-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)

## থেকে অতিরিক্ত কনফিগারেশন বিবেচনা করা হয়েছিল:

-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)

-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)

## STIGS/SRGs প্রয়োগ করা হয়েছে:
 
-[Windows 10 V1R23](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_10_V1R23_STIG.zip)

-[Windows Defender Antivirus V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_Defender_Antivirus_V1R9_STIG.zip)

-[Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

-[Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)

-[Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)

-[Microsoft Office 2019/Office 365 Pro Plus V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Office_365_ProPlus_V1R2_STIG.zip)

-[Microsoft Office 2016 V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/pdf/U_Microsoft_Office_2016_V1R2_Overview.pdf)

-[Microsoft Office 2013 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MicrosoftOffice2013_V1R5_Overview.zip)

-[Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)

-[Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **কাজ চলছে**

-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## কিভাবে স্ক্রিপ্ট চালাতে হয়

**নিষ্কৃত গিটহাব ডাউনলোড থেকে স্ক্রিপ্টটি এভাবে চালু করা যেতে পারে:**
```
.\secure-standalone.ps1
```
আমরা যে স্ক্রিপ্টটি ব্যবহার করব তা অবশ্যই ডাইরেক্টরি থেকে লঞ্চ করতে হবে যাতে অন্যান্য সমস্ত ফাইল রয়েছে[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
