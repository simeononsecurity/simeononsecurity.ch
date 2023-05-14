---
title: "পাওয়ারশেল স্ক্রিপ্টের সাথে .NET STIG কমপ্লায়েন্স স্বয়ংক্রিয় করুন"
date: 2020-08-20
---
 .NET ফ্রেমওয়ার্ক STIG

.NET STIG প্রয়োগ করা অবশ্যই সোজা নয়। অনেক প্রশাসকের জন্য এটি একটি একক সিস্টেমে সম্পূর্ণরূপে প্রয়োগ করতে কয়েক ঘন্টা সময় নিতে পারে। এই স্ক্রিপ্টটি প্রয়োজনীয় রেজিস্ট্রি পরিবর্তনগুলি প্রয়োগ করে এবং প্রয়োজন অনুসারে FIPS এবং অন্যান্য নিয়ন্ত্রণগুলি বাস্তবায়ন করতে machine.config ফাইলটি পরিবর্তন করে।

## মন্তব্য:

এই স্ক্রিপ্টটি .NET স্টিগ 100% কমপ্লায়েন্স পেতে পারে না এবং পাবে না। এই মুহূর্তে, এটি প্রায় 75% চেক সম্পূর্ণ করতে দাঁড়িয়েছে এবং ফিরে গিয়ে সমস্ত পূর্ববর্তী .NET সংস্করণগুলিতে প্রযোজ্য চেকগুলি সম্পূর্ণ করে৷

যেকোনো .NET অ্যাপ্লিকেশন বা IIS সাইটের জন্য ম্যানুয়াল হস্তক্ষেপ প্রয়োজন।

## প্রয়োজনীয়তা:
- [X] Windows 7, Windows Server 2008 বা নতুন
- [এক্স] উত্পাদন সিস্টেমে চালানোর আগে আপনার পরিবেশে পরীক্ষা করা।

## STIGS/SRGs প্রয়োগ করা হয়েছে:

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip)

## সূত্র:

-[Add from one XML data to another existing XML file](http://www.maxtblog.com/2012/11/add-from-one-xml-data-to-another-existing-xml-file/)
-[Caspol.exe (Code Access Security Policy Tool)](https://docs.microsoft.com/en-us/dotnet/framework/tools/caspol-exe-code-access-security-policy-tool)
-[Microsoft .NET Framework Documentation](https://docs.microsoft.com/en-us/dotnet/framework/)
-[PowerShell $PSScriptRoot](https://riptutorial.com/powershell/example/27231/-psscriptroot)
-[PowerShell: Run command from script's directory](https://stackoverflow.com/questions/4724290/powershell-run-command-from-scripts-directory)
-[Powershell XML importnode from different file](https://stackoverflow.com/questions/9944885/powershell-xml-importnode-from-different-file)

## প্রয়োজনীয় ফাইল ডাউনলোড করুন

আপনি থেকে প্রয়োজনীয় ফাইল ডাউনলোড করতে পারেন[GitHub Repository](https://raw.githubusercontent.com/simeononsecurity/.NET-STIG-Script/)

## কিভাবে স্ক্রিপ্ট চালাতে হয়

**নিষ্কৃত গিটহাব ডাউনলোড থেকে স্ক্রিপ্টটি এভাবে চালু করা যেতে পারে:**

## কিভাবে স্ক্রিপ্ট চালাতে হয়
### ম্যানুয়াল ইন্সটল:
যদি ম্যানুয়ালি ডাউনলোড করা হয়, স্ক্রিপ্টটি অবশ্যই একটি প্রশাসনিক পাওয়ারশেল থেকে লঞ্চ করতে হবে যেটির মধ্যে থাকা সমস্ত ফাইল রয়েছে[GitHub Repository](https://github.com/simeononsecurity/.NET-STIG-Script)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-.net-4-stig.ps1
```
### Automated Install:
Use this one-liner to automatically download, unzip all supporting files, and run the latest version of the script.
```
iwr -useb 'https://simeononsecurity.ch/scripts/sosdotnet.ps1'|iex
```
