---
title: "STIG স্ক্রিপ্টের সাথে উইন্ডোজ সার্ভার STIG সম্মতি স্বয়ংক্রিয় করা"
date: 2020-09-09
---

** থেকে প্রয়োজনীয় সমস্ত ফাইল ডাউনলোড করুন[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**দ্রষ্টব্য:** এই স্ক্রিপ্টটি বেশিরভাগ ক্ষেত্রে কাজ করা উচিত, যদি সব না হয়, সমস্যা ছাড়াই সিস্টেমের জন্য। যখন[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) এই স্ক্রিপ্টটি চালাবেন না যদি আপনি বুঝতে না পারেন এটি কী করে। এটি চালানোর আগে স্ক্রিপ্টটি পর্যালোচনা এবং পরীক্ষা করা আপনার দায়িত্ব।

## উত্তরযোগ্য:
আমরা এখন এই স্ক্রিপ্টের জন্য একটি প্লেবুক সংগ্রহ অফার করি৷ অনুগ্রহ করে নিম্নলিখিতগুলি দেখুন:
-[Github Repo](https://github.com/simeononsecurity/Windows_STIG_Ansible)
-[Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## ভূমিকা:

Windows 10 বাক্সের বাইরে অনিরাপদ অপারেটিং সিস্টেম এবং বীমা করার জন্য অনেক পরিবর্তন প্রয়োজন[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) সম্মতি
সংগঠনগুলো পছন্দ করে[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://www.defense.gov/), and the [National Security Agency](https://www.nsa.gov/) অপারেটিং সিস্টেমকে লকডাউন, কঠোর এবং সুরক্ষিত করতে এবং সরকারী সম্মতি নিশ্চিত করতে কনফিগারেশন পরিবর্তনের সুপারিশ করেছে এবং প্রয়োজনীয়। এই পরিবর্তনগুলি টেলিমেট্রি ব্লক করা, ম্যাক্রো, ব্লোটওয়্যার অপসারণ এবং একটি সিস্টেমে অনেক শারীরিক আক্রমণ প্রতিরোধ সহ বিস্তৃত প্রশমনকে কভার করে।

স্বতন্ত্র সিস্টেমগুলি সুরক্ষিত করা সবচেয়ে কঠিন এবং বিরক্তিকর সিস্টেমগুলির মধ্যে কয়েকটি। স্বয়ংক্রিয় না হলে, তাদের প্রতিটি STIG/SRG-এর ম্যানুয়াল পরিবর্তন প্রয়োজন। একটি সাধারণ স্থাপনায় মোট 1000 টির বেশি কনফিগারেশন পরিবর্তন এবং প্রতি পরিবর্তনে গড়ে 5 মিনিট যা 3.5 দিনের কাজের সমান। এই স্ক্রিপ্টটি সেই প্রক্রিয়াটিকে উল্লেখযোগ্যভাবে গতিশীল করার লক্ষ্য রাখে।

## মন্তব্য:

- এই স্ক্রিপ্টটি **এন্টারপ্রাইজ** পরিবেশে অপারেশনের জন্য ডিজাইন করা হয়েছে এবং ধরে নিচ্ছে যে আপনার কাছে সমস্ত প্রয়োজনীয়তার জন্য হার্ডওয়্যার সমর্থন রয়েছে৷
  - ব্যক্তিগত সিস্টেমের জন্য এটি দেখুন[GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)
- এই স্ক্রিপ্টটি একটি সিস্টেমকে 100% কমপ্লায়েন্সে আনার জন্য ডিজাইন করা হয়নি, বরং এটিকে বেশিরভাগ সম্পূর্ণ করার জন্য একটি স্টেপিং স্টোন হিসাবে ব্যবহার করা উচিত, যদি সব না হয়, স্ক্রিপ্ট করা যেতে পারে এমন কনফিগারেশন পরিবর্তন করে।
  - মাইনাস সিস্টেম ডকুমেন্টেশন, এই সংগ্রহটি আপনাকে প্রযোজ্য সমস্ত STIGS/SRG-তে প্রায় 95% কমপ্লায়েন্স নিয়ে আসবে।

## প্রয়োজনীয়তা:
- [X] Windows 10 এন্টারপ্রাইজ প্রতি STIG-এর প্রয়োজন।
-[X] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) একটি অত্যন্ত সুরক্ষিত Windows 10 ডিভাইসের জন্য
-[X] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
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
-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
-[NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)

## STIGS/SRGs প্রয়োগ করা হয়েছে:
-[Adobe Acrobat Pro DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
-[Adobe Acrobat Reader DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
-[Firefox V5R2](https://public.cyber.mil/stigs/downloads/)
-[Google Chrome V2R4](https://public.cyber.mil/stigs/downloads/)
-[Internet Explorer 11 V1R19](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Edge V1R2](https://public.cyber.mil/stigs/downloads/)
-[Microsoft .Net Framework 4 V1R9](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2013 V2R1](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2016 V2R1](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2019/Office 365 Pro Plus V2R3](https://public.cyber.mil/stigs/downloads/)
-[Microsoft OneDrive STIG V2R1](https://public.cyber.mil/stigs/downloads/)
-[Oracle JRE 8 V1R5](https://public.cyber.mil/stigs/downloads/)
-[Windows 10 V2R2](https://public.cyber.mil/stigs/downloads/)
-[Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)

## স্থানীয় গ্রুপ নীতিতে নীতিগুলি সম্পাদনা করা
- এখান থেকে ADMX নীতির সংজ্ঞা আমদানি করুন[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) আপনি যে সিস্টেমটি পরিবর্তন করার চেষ্টা করছেন তাতে *C:\windows\Policy Definitions* এ প্রবেশ করুন।
- খুলুন```gpedit.msc``` on on the system you're trying to modify. 


## How to run the script:
### Automated Install:
The script may be launched from the extracted GitHub download like this:
```powershell
iex ((New-Object System.Net.WebClient).DownloadString('https://simeononsecurity.com/scripts/standalonewindows.ps1'))
```

### Manual Install:
If manually downloaded, the script must be launched from the directory containing all the other files from the [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

All of the parameters in the "secure-standalone.ps1" script are optional, with a default value of $true. This means that if no value is specified for a parameter when the script is run, it will be treated as if it were set to $true.

The script takes the following parameters, all of which are optional and default to $true if not specified:

- **cleargpos**: (Boolean) Clear GPOs not being used
- **installupdates**: (Boolean) Install updates and reboot if necessary
- **adobe**: (Boolean) STIG Adobe Reader
- **firefox**: (Boolean) STIG Firefox
- **chrome**: (Boolean) STIG Chrome
- **IE11**: (Boolean) STIG Internet Explorer 11
- **edge**: (Boolean) STIG Edge
- **dotnet**: (Boolean) STIG .NET Framework
- **office**: (Boolean) STIG Office
- **onedrive**: (Boolean) STIG OneDrive
- **java**: (Boolean) STIG Java
- **windows**: (Boolean) STIG Windows
- **defender**: (Boolean) STIG Windows Defender
- **firewall**: (Boolean) STIG Windows Firewall
- **mitigations**: (Boolean) STIG Mitigations
- **nessusPID**: (Boolean) Resolve Unquoted Strings in Path
- **horizon**: (Boolean) STIG VMware Horizon
- **sosoptional**: (Boolean) Optional STIG/Hardening items

An example of how to run the script with all default parameters would be:

```powershell
.\secure-standalone.ps1
```
If you want to specify a different value for one or more of the parameters, you can include them in the command along with their desired value. For example, if you wanted to run the script and set the $firefox parameter to $false, the command would be:

```powershell
.\secure-standalone.ps1 -firefox $false
```

You can also specify multiple parameters in the command like this:

```powershell
.\secure-standalone.ps1 -firefox $false -chrome $false
```

মনে রাখবেন যে এই উদাহরণে, ফায়ারফক্স এবং ক্রোম উভয় প্যারামিটার $false এ সেট করা আছে।



