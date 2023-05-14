---
title: "স্বয়ংক্রিয় কনফিগারেশন পরিবর্তনগুলির সাথে উইন্ডোজ 10 স্থাপনাগুলি অপ্টিমাইজ করুন, শক্ত করুন এবং সুরক্ষিত করুন"
date: 2020-07-22
---
 হার্ডেন, এবং ডিব্লোট উইন্ডোজ 10 স্থাপনা**

** থেকে প্রয়োজনীয় সমস্ত ফাইল ডাউনলোড করুন[GitHub Repository](https://github.com/smiltech/Windows-Optimize-Harden-Debloat)

**আমরা নিম্নলিখিত বিষয়ে সাহায্য চাইছি[.Net issue](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/3) 

## ভূমিকা:
Windows 10 হল একটি আক্রমণাত্মক এবং অনিরাপদ অপারেটিং সিস্টেম।
সংগঠনগুলো পছন্দ করে[PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) অপারেটিং সিস্টেমকে লকডাউন, শক্ত এবং সুরক্ষিত করার জন্য কনফিগারেশন পরিবর্তনের সুপারিশ করেছে। এই পরিবর্তনগুলি টেলিমেট্রি ব্লক করা, ম্যাক্রো, ব্লোটওয়্যার অপসারণ এবং একটি সিস্টেমে অনেক ডিজিটাল এবং শারীরিক আক্রমণ প্রতিরোধ সহ বিস্তৃত প্রশমনকে কভার করে। এই স্ক্রিপ্টটি সেই সংস্থাগুলির দ্বারা প্রস্তাবিত কনফিগারেশনগুলিকে স্বয়ংক্রিয় করার লক্ষ্য রাখে।

## মন্তব্য:
- এই স্ক্রিপ্টটি প্রাথমিকভাবে **ব্যক্তিগত ব্যবহার** পরিবেশে অপারেশনের জন্য ডিজাইন করা হয়েছে। এটি মনে রেখে, নির্দিষ্ট এন্টারপ্রাইজ কনফিগারেশন সেটিংস প্রয়োগ করা হয় না। এই স্ক্রিপ্টটি একটি সিস্টেমকে 100% সম্মতিতে আনার জন্য ডিজাইন করা হয়নি। বরং এটিকে বেশিরভাগ সম্পূর্ণ করার জন্য একটি ধাপের পাথর হিসাবে ব্যবহার করা উচিত, যদি সব না হয়, ব্র্যান্ডিং এবং ব্যানারের মতো অতীতের সমস্যাগুলি এড়িয়ে যাওয়ার সময় স্ক্রিপ্ট করা যেতে পারে এমন কনফিগারেশন পরিবর্তনগুলি যেখানে ব্যক্তিগত ব্যবহারের কঠোর পরিবেশেও প্রয়োগ করা উচিত নয়৷
- এই স্ক্রিপ্টটি এমনভাবে ডিজাইন করা হয়েছে যাতে অপ্টিমাইজেশানগুলি, অন্য কিছু স্ক্রিপ্টের মতন, মূল উইন্ডোর কার্যকারিতা ভাঙবে না।
 - Windows Update, Windows Defender, Windows Store, এবং Cortona-এর মতো বৈশিষ্ট্যগুলিকে সীমাবদ্ধ করা হয়েছে, কিন্তু বেশিরভাগ অন্যান্য Windows 10 গোপনীয়তা স্ক্রিপ্টের মতো অকার্যকর অবস্থায় নেই৷
- আপনি যদি শুধুমাত্র বাণিজ্যিক পরিবেশে লক্ষ্য করে একটি ন্যূনতম স্ক্রিপ্ট চান, দয়া করে এটি দেখুন[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## প্রয়োজনীয়তা:
- [X] Windows 10 Enterprise (**Preferred**) অথবা Windows 10 Professional
  - Windows 10 হোম GPO কনফিগারেশনের জন্য অনুমতি দেয় না।
  - Windows 10 "N" সংস্করণগুলি পরীক্ষা করা হয় না।
-[X] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) একটি অত্যন্ত সুরক্ষিত Windows 10 ডিভাইসের জন্য
-[X] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - বর্তমানে Windows 10 **v1909**, **v2004**, বা **20H2**।
  - চালান[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) সর্বশেষ বড় রিলিজ আপডেট এবং যাচাই করতে।
- [এক্স] এই স্ক্রিপ্ট বাস্তবায়নের আগে বিটলকারকে অবশ্যই স্থগিত বা বন্ধ করতে হবে, এটি পুনরায় বুট করার পরে আবার সক্রিয় করা যেতে পারে।
  - এই স্ক্রিপ্টের ফলো-আপ রান বিটলকার নিষ্ক্রিয় না করে চালানো যেতে পারে।
- [এক্স] হার্ডওয়্যারের প্রয়োজনীয়তা
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
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
-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## থেকে অতিরিক্ত কনফিগারেশন বিবেচনা করা হয়েছিল:
-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[CERT - IE Scripting Engine Memory Corruption](https://kb.cert.org/vuls/id/573168/)
-[Dirteam - SSL Hardening](https://dirteam.com/sander/2019/07/30/howto-disable-weak-protocols-cipher-suites-and-hashing-algorithms-on-web-application-proxies-ad-fs-servers-and-windows-servers-running-azure-ad-connect/)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Reduce attack surfaces with attack surface reduction rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Specture and Meltdown Mitigations](https://support.microsoft.com/en-us/help/4072698/windows-server-speculative-execution-side-channel-vulnerabilities)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)
-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
-[NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)
-[UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)
-[Whonix - Disable TCP Timestamps](https://www.whonix.org/wiki/Disable_TCP_and_ICMP_Timestamps)

## STIGS/SRGs প্রয়োগ করা হয়েছে:
-[Adobe Reader Pro DC Classic V1R3](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)
-[Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Classic_V1R3_STIG.zip)
-[Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)
-[Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)
-[Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)
-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **কাজ চলছে**
-[Microsoft Office 2013 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MicrosoftOffice2013_V1R5_Overview.zip)
-[Microsoft Office 2016 V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/pdf/U_Microsoft_Office_2016_V1R2_Overview.pdf)
-[Microsoft Office 2019/Office 365 Pro Plus V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Office_365_ProPlus_V1R2_STIG.zip)
-[Microsoft OneDrive STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_OneDrive_V2R1_STIG.zip)
-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)
-[Windows 10 V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)
-[Windows Defender Antivirus V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)
-[Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

## কিভাবে স্ক্রিপ্ট চালাতে হয়
### ম্যানুয়াল ইন্সটল:
যদি ম্যানুয়ালি ডাউনলোড করা হয়, স্ক্রিপ্টটি অবশ্যই একটি প্রশাসনিক পাওয়ারশেল থেকে লঞ্চ করতে হবে যেটির মধ্যে থাকা সমস্ত ফাইল রয়েছে[GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-optimize-windows.ps1
```
### Automated Install:
The script may be launched from the extracted GitHub download like this:
```powershell
iex ((New-Object System.Net.WebClient).DownloadString('https://simeononsecurity.ch/scripts/windowsoptimizeandharden.ps1'))
```<img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/w10automatic.gif" alt="Windows-Optimize-Harden-Debloat স্বয়ংক্রিয় ইনস্টলের উদাহরণ">