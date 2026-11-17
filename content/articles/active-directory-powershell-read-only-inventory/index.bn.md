---
title: "PowerShell দিয়ে শুধু-পঠনযোগ্য Active Directory ইনভেন্টরি তৈরি করুন"
date: 2026-10-10
lastmod: 2026-11-08
toc: true
draft: false
description: "নির্দিষ্ট PowerShell কোয়েরি দিয়ে Active Directory-র OU, ব্যবহারকারী ও কম্পিউটার ইনভেন্টরি করুন। ডিরেক্টরি অবজেক্ট না বদলে পর্যালোচনাযোগ্য CSV ফাইল রপ্তানি করুন।"
genre: ["Active Directory", "PowerShell", "সিস্টেম প্রশাসন"]
tags: ["Active Directory ইনভেন্টরি", "PowerShell AD ইনভেন্টরি", "Get-ADUser", "Get-ADComputer", "Get-ADOrganizationalUnit", "Get-ADDomain", "SearchBase", "শুধু-পঠনযোগ্য AD", "AD ব্যবহারকারী রপ্তানি", "AD কম্পিউটার রপ্তানি", "AD OU রপ্তানি", "Export-Csv", "RSAT", "ডিরেক্টরি অডিট", "AD প্রতিবেদন", "OU ইনভেন্টরি", "Windows Server", "PowerShell স্ক্রিপ্ট", "AD মডিউল", "ডিরেক্টরি পরিচ্ছন্নতা"]
cover: "/img/cover/active-directory-powershell-read-only-inventory.webp"
coverAlt: "Active Directory গাছ থেকে ব্যবহারকারী, কম্পিউটার ও সাংগঠনিক ইউনিটের রেকর্ড তিনটি পর্যালোচনা ফাইলে যাচ্ছে।"
coverCaption: "কোয়েরির পরিসর সীমিত করুন, তারপর পর্যালোচনার জন্য প্রয়োজনীয় ক্ষেত্রগুলোই রপ্তানি করুন।"
---
Active Directory পরিষ্কার করার কাজ শুরু হয় বিদ্যমান অবজেক্টের নির্ভরযোগ্য তালিকা দিয়ে। এই **শুধু-পঠনযোগ্য ইনভেন্টরি** নির্বাচিত পরিসরের সাংগঠনিক ইউনিট, ব্যবহারকারী ও কম্পিউটার সংগ্রহ করে। এটি ডিরেক্টরি অবজেক্ট না বদলে পর্যালোচনার জন্য তিনটি CSV (কমা-বিভাজিত মান) ফাইল রপ্তানি করে। তবু ফাইলগুলো সুরক্ষিত রাখুন, কারণ নাম ও ডিভাইসের বিবরণ আপনার পরিবেশের অংশ প্রকাশ করে।

<!--more-->

## মূল বিষয়গুলো

- **পরিসর বেছে নিন:** পুরো ডোমেইনে যাওয়ার আগে একটি সাংগঠনিক ইউনিট কোয়েরি করুন।
- **পড়ার কমান্ড ব্যবহার করুন:** `Get-ADOrganizationalUnit`, `Get-ADUser` এবং `Get-ADComputer` অবজেক্ট সংগ্রহ করে।
- **ক্ষেত্র বেছে নিন:** কাজের জন্য প্রয়োজনীয় প্রপার্টিগুলোই রপ্তানি করুন।
- **আউটপুট যাচাই করুন:** প্রতিবেদনের ওপর নির্ভর করার আগে সংখ্যা ও কয়েকটি নমুনা সারি তুলনা করুন।

## শুরু করার আগে

আপনার দরকার কার্যকর DNS ও ডোমেইন কন্ট্রোলারে নেটওয়ার্ক অ্যাক্সেসসহ একটি Windows প্রশাসনিক হোস্ট, PowerShell-এর **ActiveDirectory** মডিউল, নির্বাচিত অবজেক্ট পড়ার অনুমোদিত অ্যাকাউন্ট এবং CSV আউটপুটের জন্য সুরক্ষিত ফোল্ডার। Windows ক্লায়েন্টে মডিউলটি Remote Server Administration Tools (RSAT)-এর Active Directory টুলগুলোর সঙ্গে আসে। [Active Directory মডিউল গাইড](/articles/active-directory-module-powershell-installation-usage-guide/) ইনস্টলেশন ব্যাখ্যা করে। Microsoft মডিউলের [cmdlet রেফারেন্স](https://learn.microsoft.com/en-us/powershell/module/activedirectory/) এবং [RSAT ইনস্টলেশন বিকল্প](https://learn.microsoft.com/windows-server/remote/remote-server-administration-tools) প্রকাশ করেছে। এই গাইডে Windows PowerShell সিনট্যাক্স ব্যবহার করা হয়েছে এবং ডিরেক্টরি অবজেক্ট বদলানো হয় না।

ডিরেক্টরির অনুমতিগুলো এখনও প্রযোজ্য। Microsoft-এর [বিশেষাধিকারপ্রাপ্ত অ্যাকাউন্ট নির্দেশিকা](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory) ব্যাখ্যা করে, অ্যাক্সেস কন্ট্রোল তালিকা প্রায়ই প্রমাণীকৃত ব্যবহারকারীদের সাধারণ তথ্য পড়তে দেয়, আর সংবেদনশীল ক্ষেত্র ও পরিবর্তনের অনুমতি সীমিত করে। প্রথমে অনুমোদিত অ্যাকাউন্ট ও পরীক্ষামূলক OU ব্যবহার করুন। ইনভেন্টরি সফল করতে Domain Admin অধিকার বাড়াবেন না।

> **সতর্কতা:** CSV ফাইলে অ্যাকাউন্ট ও কম্পিউটারের নাম থাকে। অনুমোদিত স্থানে সংরক্ষণ করুন, অ্যাক্সেস সীমিত করুন এবং পর্যালোচনার পর অতিরিক্ত কপি মুছুন। কাঁচা রপ্তানি প্রকাশ করবেন না বা কোনো সর্বজনীন Issue-তে যুক্ত করবেন না।

## অনুসন্ধানের ভিত্তি বেছে নিন

একটি **সাংগঠনিক ইউনিট (OU)** ডিরেক্টরি অবজেক্টগুলোকে গোষ্ঠীবদ্ধ করে। এর **distinguished name (DN)** ডিরেক্টরি গাছে অবস্থান জানায়। `-SearchBase` প্যারামিটার একটি নির্বাচিত DN-এ কোয়েরি সীমাবদ্ধ করে। ইচ্ছাকৃতভাবে পরিসর নির্ধারণ না করলে বিস্তৃত ফিল্টার আপনার পর্যালোচনার প্রয়োজনের চেয়ে অনেক বেশি অবজেক্ট ফেরত দিতে পারে।

প্রথমে মডিউলটি লোড করুন এবং বর্তমান ডোমেইনের DN দেখুন:

```powershell
Import-Module ActiveDirectory
(Get-ADDomain).DistinguishedName
```

Microsoft [Get-ADDomain](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-addomain) এবং এটি ফেরত দেওয়া ডোমেইন-তথ্য নথিভুক্ত করেছে। অনুসন্ধানের ভিত্তি নির্ধারণের আগে পর্যালোচনার OU খুঁজে নিন:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase (Get-ADDomain).DistinguishedName |
    Select-Object Name, DistinguishedName
```

ফলাফল থেকে সঠিক DN কপি করুন। পরের উদাহরণগুলোতে এই নথিভুক্ত মানটির বদলে আপনার OU-র DN দিন:

```powershell
$SearchBase = 'OU=Lab,DC=example,DC=com'
```

`example.com` নথির উদাহরণ ডোমেইন। বাস্তব কোয়েরিতে এর DN কপি করবেন না। ইচ্ছাকৃতভাবে পুরো ডোমেইন ইনভেন্টরি করতে হলে `$SearchBase`-এ ডোমেইনের DN দিন এবং প্রতিবেদনে বড় পরিসরটি লিখুন। Microsoft-এর [Get-ADOrganizationalUnit রেফারেন্স](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit) `-Filter` ও `-SearchBase` ব্যাখ্যা করে।

## OU, ব্যবহারকারী ও কম্পিউটার ইনভেন্টরি করুন

অবজেক্টের সংখ্যা দিয়ে শুরু করুন। ভুল অনুসন্ধান-ভিত্তি বা অপ্রত্যাশিতভাবে খালি ফলাফল দ্রুত ধরতে এটি সাহায্য করে:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADUser -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADComputer -Filter * -SearchBase $SearchBase | Measure-Object
```

`-Filter *` অনুসন্ধানের ভিত্তির মধ্যে মেলা সব অবজেক্ট সংগ্রহ করে। Microsoft [Get-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser) ও [Get-ADComputer](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer)-কে সংগ্রহের কমান্ড হিসেবে নথিভুক্ত করেছে। শূন্য সংখ্যা সঠিকও হতে পারে, তবে ইনভেন্টরি সম্পূর্ণ ধরে নেওয়ার আগে DN, অনুমতি ও লক্ষ্য ডোমেইন যাচাই করুন।

এখন কনসোলে কয়েকটি সারি প্রিভিউ করুন। নির্বাচিত ক্ষেত্রগুলো সংরক্ষণ করলে প্রিভিউ ও পরের CSV রপ্তানিতে একই কলাম থাকবে:

```powershell
$UserFields = 'Name', 'SamAccountName', 'Enabled', 'DistinguishedName'
Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields -First 10
```

কম্পিউটারের অতিরিক্ত অপারেটিং-সিস্টেম প্রপার্টি পর্যালোচনার জন্য দরকার হলেই চান:

```powershell
$ComputerFields = @(
    'Name', 'DNSHostName', 'OperatingSystem',
    'Enabled', 'DistinguishedName'
)
Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields -First 10
```

`-Properties` প্যারামিটার cmdlet-এর ডিফল্ট সেটের বাইরে থাকা প্রপার্টি চায়। Microsoft-এর [কম্পিউটার cmdlet রেফারেন্সে](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) এটি নথিভুক্ত আছে। অপারেটিং-সিস্টেমের নামকে ডিরেক্টরি-তথ্য হিসেবে ধরুন, বর্তমানে ইনস্টল করা সংস্করণের প্রমাণ হিসেবে নয়। কম্পিউটার অবজেক্টটি পুরোনো হতে পারে বা এর অ্যাট্রিবিউট এখনও আপডেট না-ও হতে পারে।

## পর্যালোচনাযোগ্য CSV রপ্তানি করুন

পর্যাপ্ত জায়গাসহ অনুমোদিত আউটপুট ফোল্ডার বেছে নিন। নিচের কমান্ডগুলো **স্থানীয় CSV ফাইল** লেখে এবং ডিরেক্টরি অবজেক্ট বদলায় না। ওই ফোল্ডার থেকেই চালান। `-NoClobber` বিদ্যমান ফাইলের ওপর লেখা ঠেকায়। প্রতিবার নতুন ফোল্ডার বা ফাইলের নাম ব্যবহার করুন।

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase |
    Select-Object Name, DistinguishedName |
    Export-Csv -Path .\ad-ous.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields |
    Export-Csv -Path .\ad-users.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields |
    Export-Csv -Path .\ad-computers.csv -NoTypeInformation -Encoding UTF8 -NoClobber
```

Microsoft-এর [Export-Csv রেফারেন্স](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv?view=powershell-5.1) `-NoTypeInformation`, `-Encoding` ও `-NoClobber` ব্যাখ্যা করে। প্রতিটি CSV টেক্সট এডিটর বা অনুমোদিত স্প্রেডশিটে খুলুন। হেডার, কয়েকটি সারি এবং আগের গণনার সঙ্গে রেকর্ড সংখ্যা মিলিয়ে দেখুন। কমান্ড ব্যর্থ হওয়া বা শূন্য-বাইট ফাইল তৈরি হওয়া পূর্ণ প্রতিবেদনের প্রমাণ নয়।

> **প্রত্যাশিত ফল:** নির্বাচিত ডিরেক্টরি-পরিসরের OU, ব্যবহারকারী ও কম্পিউটারের রেকর্ডসহ তিনটি CSV ফাইল পাবেন। সারির সংখ্যা ও নমুনা মান নির্বাচিত পরিসরের সঙ্গে মেলে।

## অবজেক্ট না বদলে পর্যালোচনা করুন

ইনভেন্টরি দিয়ে নির্দিষ্ট প্রশ্নের উত্তর খুঁজুন: কোন OU একটি কম্পিউটারের দায়িত্বে? কোন ব্যবহারকারী অ্যাকাউন্ট নিষ্ক্রিয়? কোন ডিভাইসের নামের সঙ্গে মালিক যুক্ত করা দরকার? আলাদা পর্যালোচনা নোটে ফল লিখুন। `Enabled` মান দেখে অ্যাকাউন্টটি এখনও দরকার কি না সিদ্ধান্ত নেবেন না। শুধু রপ্তানি দেখে কোনো অবজেক্ট মুছবেন বা নিষ্ক্রিয় করবেন না।

নিয়মিত প্রতিবেদনে কোয়েরির তারিখ, ডোমেইন, OU-র DN, নির্বাচিত প্রপার্টি, অপারেটর এবং CSV-র অবস্থান লিখুন। দুটি রপ্তানি তুলনা করলে একই পরিসর ও একই ক্ষেত্র ব্যবহার হয়েছে কি না নিশ্চিত করুন। নইলে পার্থক্য ডিরেক্টরির প্রকৃত পরিবর্তনের বদলে কোয়েরি থেকে আসতে পারে।

এটি একটি **ইনভেন্টরি**, বিশেষাধিকারপ্রাপ্ত অ্যাকাউন্ট অডিট বা লগইন-কার্যকলাপের প্রতিবেদন নয়। Microsoft জানায়, Active Directory-র প্রপার্টি ও অনুমতি অবজেক্ট এবং পরিবেশভেদে বদলায়। অপারেটিং-সিস্টেম অ্যাট্রিবিউট বা প্রদর্শিত নামের ভিত্তিতে কাজ করার আগে সিস্টেমের মালিকের সঙ্গে যাচাই করুন। আরও বিস্তৃত নিরাপত্তা নিয়ন্ত্রণ [Active Directory নিরাপত্তা গাইডে](/articles/active-directory-security-best-practices/) আছে।

## সমস্যা সমাধান

- **মডিউল ইমপোর্ট হয় না:** হোস্টে RSAT-এর Active Directory টুল বা Windows Server প্রশাসনিক টুল ইনস্টল আছে কি না নিশ্চিত করুন। [মডিউল সেটআপ গাইড](/articles/active-directory-module-powershell-installation-usage-guide/) অনুসরণ করুন।
- **কোয়েরি কোনো অবজেক্ট ফেরত দেয় না:** সঠিক DN, বর্তমান ডোমেইন, OU-র বিষয়বস্তু এবং পড়ার অনুমতি যাচাই করুন। পরিসর বড় করার আগে পরিচিত ছোট OU পরীক্ষা করুন।
- **কোনো প্রপার্টি ফাঁকা:** অ্যাট্রিবিউটটি আছে এবং আপনার অ্যাকাউন্ট সেটি পড়তে পারে কি না দেখুন। অনুমান করে অনুপস্থিত ক্ষেত্র পূরণ করবেন না।
- **রপ্তানিতে ফাইল আগে থেকেই আছে দেখায়:** `-NoClobber` আগের প্রতিবেদনটি সুরক্ষিত রেখেছে। নতুন ফাইলের নাম বা ফোল্ডার বেছে আবার চালান।
- **সংখ্যা প্রত্যাশার সঙ্গে মেলে না:** ব্যবহারকারী বা কম্পিউটার অন্য OU-তে আছে কি না, পরিসর বদলেছে কি না এবং কোয়েরি চলার সময় ডিরেক্টরি বদলেছে কি না যাচাই করুন।

## পরবর্তী পদক্ষেপ

সম্মত পর্যালোচনা সময় জুড়ে কাঁচা CSV ফাইল সুরক্ষিত স্থানে রাখুন। পর্যালোচকের দরকার এমন ক্ষেত্রই ভাগ করুন। দায়িত্বপ্রাপ্তরা ফল নিশ্চিত করার পরে স্বাভাবিক অনুমোদন ও rollback প্রক্রিয়ায় পরিবর্তন পরিকল্পনা করুন। অনুমোদিত পরিবর্তনের পরে একই পরিসরে একই ইনভেন্টরি আবার চালিয়ে ফল নিশ্চিত করুন।