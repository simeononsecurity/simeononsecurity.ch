---
title: "PowerShell দিয়ে অ্যাক্টিভ ডিরেক্টরি প্রশাসন"
date: 2023-07-25
toc: true
draft: false
description: আপনার উইন্ডোজ অ্যাক্টিভ ডিরেক্টরি প্রশাসন কাজগুলো সহজ করার জন্য PowerShell এর জন্য অ্যাক্টিভ ডিরেক্টরি মডিউল কীভাবে কার্যকরভাবে ইনস্টল এবং ব্যবহার করবেন তা আবিষ্কার করুন।
genre:
- প্রযুক্তি
- উইন্ডোজ
- PowerShell
- অ্যাক্টিভ ডিরেক্টরি
- প্রশাসন
- স্ক্রিপ্টিং
- আইটি
- স্বয়ংক্রিয়করণ
- উইন্ডোজ সার্ভার
- মাইক্রোসফট
tags:
- PowerShell এর জন্য অ্যাক্টিভ ডিরেক্টরি মডিউল
- PowerShell এ অ্যাক্টিভ ডিরেক্টরি মডিউল ইম্পোর্ট করুন
- উইন্ডোজ PowerShell এর জন্য অ্যাক্টিভ ডিরেক্টরি মডিউল
- অ্যাক্টিভ ডিরেক্টরি PowerShell ইনস্টল
- অ্যাক্টিভ ডিরেক্টরি PowerShell ইনস্টল করুন
- PowerShell এ উইন্ডোজ 10 এ অ্যাক্টিভ ডিরেক্টরি মডিউল ইনস্টল করুন
- উইন্ডোজ 10 এ অ্যাক্টিভ ডিরেক্টরি PowerShell মডিউল ইনস্টল করুন
- অ্যাক্টিভ ডিরেক্টরি PowerShell মডিউল পান
- AD প্রশাসন
- উইন্ডোজ অ্যাক্টিভ ডিরেক্টরি
- PowerShell cmdlet
- AD তথ্য পুনরুদ্ধার করুন
- AD অবজেক্ট তৈরি করুন
- AD অবজেক্ট পরিবর্তন করুন
- AD নিরাপত্তা পরিচালনা করুন
- AD ব্যবহারকারী ব্যবস্থাপনা
- AD গ্রুপ ব্যবস্থাপনা
- AD OU ব্যবস্থাপনা
- PowerShell স্ক্রিপ্টিং
- উইন্ডোজ সার্ভার প্রশাসন
- মাইক্রোসফট PowerShell
- AD কাজ স্বয়ংক্রিয় করুন
- PowerShell মডিউল ইনস্টলেশন
- AD প্রশাসন গাইড
- অ্যাক্টিভ ডিরেক্টরি ব্যবস্থাপনা
- AD নিরাপত্তা ব্যবস্থাপনা
- PowerShell স্বয়ংক্রিয়করণ
- অ্যাক্টিভ ডিরেক্টরি PowerShell কমান্ড
- PowerShell cmdlet রেফারেন্স
cover: /img/cover/active-directory-module-powershell-installation-usage-guide.webp
coverAlt: একটি কম্পিউটার স্ক্রিনের চিত্র যেখানে একটি PowerShell কনসোল রঙিন cmdlet সহ দেখানো হয়েছে, চারপাশে ব্যবহারকারী অ্যাকাউন্ট এবং গ্রুপের বিমূর্ত প্রতিনিধিত্ব, একটি গা dark ় পটভূমির বিরুদ্ধে।
coverCaption: PowerShell দিয়ে অ্যাক্টিভ ডিরেক্টরি প্রশাসনের শক্তি উন্মুক্ত করুন।
lastmod: 2026-10-08
---

## পরিচিতি

আজকের দিনে উইন্ডোজ অ্যাক্টিভ ডিরেক্টরি (AD) পরিবেশে ব্যবহারকারী অ্যাকাউন্ট, নিরাপত্তা গ্রুপ এবং অন্যান্য সম্পদ পরিচালনা ও রক্ষণাবেক্ষণ করার জন্য দক্ষ এবং সরলীকৃত প্রক্রিয়া প্রয়োজন। মাইক্রোসফট দ্বারা উন্নত একটি শক্তিশালী স্ক্রিপ্টিং ভাষা PowerShell, AD প্রশাসন কাজগুলো সহজ করার জন্য **অ্যাক্টিভ ডিরেক্টরি মডিউল** প্রদান করে। এই মডিউলটি অনেক cmdlet সরবরাহ করে যা প্রশাসকদের বিভিন্ন অপারেশন স্বয়ংক্রিয় করতে এবং AD কার্যকরভাবে পরিচালনা করতে সক্ষম করে। এই নিবন্ধে, আমরা PowerShell এর জন্য অ্যাক্টিভ ডিরেক্টরি মডিউল ইনস্টলেশন এবং ব্যবহারের বিষয়ে আলোচনা করব।

## PowerShell এর জন্য অ্যাক্টিভ ডিরেক্টরি মডিউল ইনস্টলেশন

PowerShell এর জন্য অ্যাক্টিভ ডিরেক্টরি মডিউল ব্যবহার শুরু করার জন্য, আপনাকে নিশ্চিত করতে হবে যে এটি আপনার সিস্টেমে ইনস্টল করা আছে। ইনস্টলেশন প্রক্রিয়া আপনার অপারেটিং সিস্টেমের উপর নির্ভর করে পরিবর্তিত হতে পারে। এখানে **উইন্ডোজ 10**, **উইন্ডোজ 11**, এবং **উইন্ডোজ সার্ভার** এ মডিউল ইনস্টল করার ধাপগুলো দেওয়া হলো:

### উইন্ডোজ 10 এবং উইন্ডোজ 11 - PowerShell
1. প্রশাসনিক অধিকার সহ **উইন্ডোজ PowerShell** খুলুন।
2. মডিউল ইনস্টল করতে নিম্নলিখিত কমান্ডটি চালান:

```powershell
Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0 -Online
```

1. ইনস্টলেশন সম্পন্ন হওয়া পর্যন্ত অপেক্ষা করুন। শেষ হলে, আপনি অ্যাক্টিভ ডিরেক্টরি মডিউল ব্যবহার শুরু করতে পারবেন।

### উইন্ডোজ সার্ভার 
1. প্রশাসনিক অধিকার সহ **উইন্ডোজ PowerShell** খুলুন।
2. মডিউল ইনস্টল করতে নিম্নলিখিত কমান্ডটি চালান:

```powershell
Install-WindowsFeature -Name "RSAT-AD-PowerShell" -IncludeAllSubFeature
```

3. ইনস্টলেশন সম্পন্ন হওয়া পর্যন্ত অপেক্ষা করুন। শেষ হলে, আপনি অ্যাক্টিভ ডিরেক্টরি মডিউল ব্যবহার শুরু করতে পারবেন।

### অফলাইন সিস্টেম

অফলাইন সিস্টেমগুলো একটু জটিল। কিছু পদ্ধতি আছে, তবে আমরা যে পদ্ধতিটি সুপারিশ করি তা হলো নিম্নলিখিত স্ক্রিপ্ট ব্যবহার করা:
- [Offine-PS-ActiveDirectory-Install](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install)

## PowerShell এ অ্যাক্টিভ ডিরেক্টরি মডিউল ইম্পোর্ট করা

PowerShell এ অ্যাক্টিভ ডিরেক্টরি মডিউল ব্যবহার করার আগে, আপনাকে এটি আপনার বর্তমান সেশনে ইম্পোর্ট করতে হবে। মডিউল ইম্পোর্ট করার জন্য নিচের ধাপগুলো অনুসরণ করুন:

1. প্রশাসনিক অধিকার সহ **উইন্ডোজ PowerShell** চালু করুন।
2. মডিউল ইম্পোর্ট করতে নিম্নলিখিত কমান্ডটি চালান:

```powershell
Import-Module ActiveDirectory
```

3. অ্যাক্টিভ ডিরেক্টরি মডিউল ইম্পোর্ট হয়ে যাবে, এবং এখন আপনি এর cmdlet এবং ফাংশনগুলো অ্যাক্সেস করতে পারবেন।

## PowerShell এর জন্য অ্যাক্টিভ ডিরেক্টরি মডিউল ব্যবহার

অ্যাক্টিভ ডিরেক্টরি মডিউল ইম্পোর্ট করার পর, আপনি এর সমৃদ্ধ cmdlet সেট ব্যবহার করে বিভিন্ন প্রশাসনিক কাজ করতে পারবেন। এখানে কিছু সাধারণ ব্যবহৃত cmdlet এবং তাদের কার্যকারিতা দেখানো হলো:

### অ্যাক্টিভ ডিরেক্টরি তথ্য পুনরুদ্ধার

একটি কার্যকর অ্যাক্টিভ ডিরেক্টরি (AD) পরিবেশ পরিচালনার জন্য, আপনাকে বিভিন্ন AD অবজেক্ট যেমন ব্যবহারকারী, গ্রুপ, এবং অর্গানাইজেশনাল ইউনিট (OU) সম্পর্কে তথ্য পুনরুদ্ধার করতে হবে। PowerShell শক্তিশালী cmdlet সরবরাহ করে যা পুনরুদ্ধার প্রক্রিয়াকে সহজ করে।

- [**Get-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps): এই cmdlet আপনাকে AD ব্যবহারকারীদের বিস্তারিত তথ্য পুনরুদ্ধার করতে দেয়। আপনি ব্যবহারকারীর নাম, প্রদর্শন নাম, ইমেইল ঠিকানা এবং আরও অনেক বৈশিষ্ট্য পেতে পারেন। উদাহরণস্বরূপ, "johndoe" দিয়ে শুরু হওয়া সমস্ত ব্যবহারকারী পুনরুদ্ধার করতে নিম্নলিখিত কমান্ডটি চালাতে পারেন:

  ```powershell
  Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
  ```

  এই কমান্ডটি নির্দিষ্ট ফিল্টারের সাথে মেলে এমন ব্যবহারকারী অবজেক্টের একটি তালিকা প্রদান করবে।

- [**Get-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps): Get-ADGroup cmdlet দিয়ে আপনি AD গ্রুপ সম্পর্কে তথ্য পেতে পারেন। এটি গ্রুপের নাম, সদস্য, বিবরণ এবং আরও অনেক কিছু সম্পর্কে তথ্য দেয়। উদাহরণস্বরূপ, AD পরিবেশের সমস্ত নিরাপত্তা গ্রুপ পুনরুদ্ধার করতে নিম্নলিখিত কমান্ডটি চালান:

  ```powershell
  Get-ADGroup -Filter 'GroupCategory -eq "Security"'
  ```

  এটি অ্যাক্টিভ ডিরেক্টরির নিরাপত্তা গ্রুপগুলোর একটি তালিকা প্রদান করবে।

- [**Get-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit?view=windowsserver2022-ps): Get-ADOrganizationalUnit cmdlet AD OU সম্পর্কে তথ্য পুনরুদ্ধার করতে ব্যবহৃত হয়। এটি OU নাম, বিবরণ, প্যারেন্ট OU এবং আরও অনেক বৈশিষ্ট্য অ্যাক্সেস করতে দেয়। ডোমেইনের সমস্ত OU পুনরুদ্ধার করতে নিম্নলিখিত কমান্ডটি ব্যবহার করুন:

  ```powershell
  Get-ADOrganizationalUnit -Filter *
  ```

  এই কমান্ডটি চালালে অ্যাক্টিভ ডিরেক্টরির সমস্ত OU এর একটি তালিকা প্রদর্শিত হবে।

এই শক্তিশালী cmdlet গুলো ব্যবহার করে, আপনি AD ব্যবহারকারী, গ্রুপ এবং OU সম্পর্কে নির্দিষ্ট তথ্য সহজেই পুনরুদ্ধার করতে পারবেন, যা আপনার অ্যাক্টিভ ডিরেক্টরি পরিবেশের দক্ষ প্রশাসন এবং ব্যবস্থাপনা সক্ষম করে।


এই cmdlet গুলো আপনাকে নির্দিষ্ট বৈশিষ্ট্য পুনরুদ্ধার করতে, ফলাফল ফিল্টার করতে এবং কাঙ্ক্ষিত তথ্য পেতে উন্নত অনুসন্ধান করতে দেয়।

### অ্যাক্টিভ ডিরেক্টরি অবজেক্ট তৈরি এবং পরিচালনা

অ্যাক্টিভ ডিরেক্টরি (AD) নিয়ে কাজ করার সময়, PowerShell এর অ্যাক্টিভ ডিরেক্টরি মডিউল AD অবজেক্ট তৈরি এবং পরিচালনার জন্য শক্তিশালী cmdlet সরবরাহ করে। এখানে AD ব্যবহারকারী, গ্রুপ এবং অর্গানাইজেশনাল ইউনিট (OU) তৈরি করার জন্য কিছু গুরুত্বপূর্ণ cmdlet দেখানো হলো।

- [**New-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps): এই cmdlet দিয়ে আপনি একটি নতুন AD ব্যবহারকারী তৈরি করতে পারেন। আপনি ব্যবহারকারীর নাম, পাসওয়ার্ড, ইমেইল ঠিকানা এবং আরও অনেক বৈশিষ্ট্য নির্দিষ্ট করতে পারেন। উদাহরণস্বরূপ, "john.doe" ব্যবহারকারীর নাম এবং "John Doe" প্রদর্শন নাম সহ একটি নতুন ব্যবহারকারী তৈরি করতে নিম্নলিখিত কমান্ডটি ব্যবহার করুন:

  ```powershell
  New-ADUser -SamAccountName "john.doe" -Name "John Doe"
  ```

  এই কমান্ডটি অ্যাক্টিভ ডিরেক্টরিতে একটি নতুন ব্যবহারকারী তৈরি করবে।

- [**New-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adgroup?view=windowsserver2022-ps): New-ADGroup cmdlet দিয়ে আপনি একটি নতুন AD গ্রুপ তৈরি করতে পারেন। আপনি গ্রুপের নাম, বিবরণ, গ্রুপ স্কোপ এবং আরও অনেক বৈশিষ্ট্য নির্ধারণ করতে পারেন। উদাহরণস্বরূপ, "Marketing" নামের একটি নতুন গ্রুপ এবং একটি বিবরণ তৈরি করতে নিম্নলিখিত কমান্ডটি চালান:

  ```powershell
  New-ADGroup -Name "Marketing" -Description "Marketing Team"
  ```

  এই কমান্ডটি অ্যাক্টিভ ডিরেক্টরিতে একটি নতুন গ্রুপ তৈরি করবে।

- [**New-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adorganizationalunit?view=windowsserver2022-ps): New-ADOrganizationalUnit cmdlet ব্যবহার করে আপনি একটি নতুন AD OU তৈরি করতে পারেন। আপনি OU নাম, প্যারেন্ট OU এবং আরও অনেক গুণাবলী নির্দিষ্ট করতে পারেন। উদাহরণস্বরূপ, "Departments" OU এর অধীনে "Sales" নামে একটি নতুন OU তৈরি করতে, আপনি নিম্নলিখিত কমান্ডটি চালাতে পারেন:

  ```powershell
  New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"
  ```

  এই কমান্ডটি Active Directory হায়ারার্কিতে একটি নতুন OU তৈরি করবে।

এই cmdlet গুলো ব্যবহার করে, আপনি সহজেই নতুন AD ব্যবহারকারী, গ্রুপ এবং OU তৈরি করতে পারেন আপনার কাঙ্ক্ষিত গুণাবলী ও কনফিগারেশন সহ, যা আপনার Active Directory পরিবেশের কার্যকর ব্যবস্থাপনা সক্ষম করে।


### Active Directory অবজেক্ট পরিবর্তন করা

বিদ্যমান Active Directory (AD) অবজেক্টের গুণাবলী ও বৈশিষ্ট্য পরিবর্তনের ক্ষেত্রে, PowerShell এর Active Directory মডিউল বেশ কিছু উপযোগী cmdlet প্রদান করে। এখানে AD ব্যবহারকারী, গ্রুপ এবং অর্গানাইজেশনাল ইউনিট (OU) পরিবর্তনের জন্য এই cmdlet গুলোর একটি পর্যালোচনা দেওয়া হলো।

- [**Set-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-aduser?view=windowsserver2022-ps): Set-ADUser cmdlet আপনাকে একটি AD ব্যবহারকারীর গুণাবলী পরিবর্তন করতে দেয়। আপনি ডিসপ্লে নাম, ইমেইল ঠিকানা, টেলিফোন নম্বর এবং আরও অনেক বৈশিষ্ট্য আপডেট করতে পারেন। উদাহরণস্বরূপ, "john.doe" ইউজারনেমের ব্যবহারকারীর টেলিফোন নম্বর পরিবর্তন করতে, আপনি নিম্নলিখিত কমান্ডটি ব্যবহার করতে পারেন:

  ```powershell
  Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
  ```

  এই কমান্ডটি নির্দিষ্ট ব্যবহারকারীর টেলিফোন নম্বর Active Directory-তে পরিবর্তন করবে।

- [**Set-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adgroup?view=windowsserver2022-ps): Set-ADGroup cmdlet ব্যবহার করে আপনি একটি AD গ্রুপের গুণাবলী পরিবর্তন করতে পারেন। আপনি গ্রুপের বর্ণনা, সদস্যপদ, গ্রুপ স্কোপ এবং আরও অনেক বৈশিষ্ট্য আপডেট করতে পারেন। উদাহরণস্বরূপ, "Marketing" নামের একটি গ্রুপের বর্ণনা "Marketing Team" এ পরিবর্তন করতে, আপনি নিম্নলিখিত কমান্ডটি চালাতে পারেন:

  ```powershell
  Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
  ```

  এই কমান্ডটি নির্দিষ্ট গ্রুপের বর্ণনা Active Directory-তে আপডেট করবে।

- [**Set-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adorganizationalunit?view=windowsserver2022-ps): Set-ADOrganizationalUnit cmdlet আপনাকে একটি AD OU এর গুণাবলী পরিবর্তন করতে দেয়। আপনি OU নাম, বর্ণনা এবং আরও অনেক বৈশিষ্ট্য পরিবর্তন করতে পারেন। উদাহরণস্বরূপ, "Sales" নামের একটি OU এর বর্ণনা "Sales Department" এ পরিবর্তন করতে, আপনি নিম্নলিখিত কমান্ডটি চালাতে পারেন:

  ```powershell
  Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"
  ```

  এই কমান্ডটি নির্দিষ্ট OU এর বর্ণনা Active Directory হায়ারার্কিতে আপডেট করবে।

এই cmdlet গুলো ব্যবহার করে, আপনি সহজেই AD অবজেক্টের গুণাবলী ও বৈশিষ্ট্য পরিবর্তন করতে পারেন, প্রয়োজনীয় আপডেট ও সমন্বয় করে আপনার প্রতিষ্ঠানের চাহিদা পূরণ করতে পারেন।


### Active Directory নিরাপত্তা পরিচালনা

Active Directory (AD) অবজেক্ট ব্যবস্থাপনা ও প্রশাসনের পাশাপাশি, PowerShell এর Active Directory মডিউল নিরাপত্তা-সম্পর্কিত দিকগুলো পরিচালনার জন্য বিশেষ cmdlet প্রদান করে। এই cmdlet গুলো প্রশাসকদের AD পরিবেশে ব্যবহারকারীর প্রবেশাধিকার, গ্রুপ সদস্যপদ এবং পাসওয়ার্ড সম্পর্কিত কাজগুলো দক্ষতার সাথে পরিচালনা করতে সাহায্য করে।

নিম্নলিখিত কিছু সাধারণ নিরাপত্তা-সম্পর্কিত cmdlet রয়েছে:

- [**Add-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2022-ps): এই cmdlet আপনাকে একটি AD গ্রুপে সদস্য যোগ করতে দেয়। AD গ্রুপ এবং যোগ করতে চান এমন ব্যবহারকারী অ্যাকাউন্ট বা গ্রুপ নির্দিষ্ট করে, আপনি সহজেই প্রবেশাধিকার নিয়ন্ত্রণ করতে পারেন। উদাহরণস্বরূপ, "JohnDoe" নামে একটি ব্যবহারকারীকে "Managers" গ্রুপে যোগ করতে, আপনি নিম্নলিখিত কমান্ডটি ব্যবহার করতে পারেন:

  ```powershell
  Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
  ```

- [**Remove-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/remove-adgroupmember?view=windowsserver2022-ps): এই cmdlet ব্যবহার করে আপনি একটি AD গ্রুপ থেকে সদস্য অপসারণ করতে পারেন। AD গ্রুপ এবং অপসারণ করতে চান এমন ব্যবহারকারী অ্যাকাউন্ট বা গ্রুপ নির্দিষ্ট করে, আপনি গ্রুপ সদস্যপদ কার্যকরভাবে পরিচালনা করতে পারেন। উদাহরণস্বরূপ, "JaneSmith" নামে একটি ব্যবহারকারীকে "Developers" গ্রুপ থেকে অপসারণ করতে, আপনি নিম্নলিখিত কমান্ডটি ব্যবহার করতে পারেন:

  ```powershell
  Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
  ```

- [**Set-ADUserPassword**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adaccountpassword?view=windowsserver2022-ps): এই cmdlet আপনাকে একটি AD ব্যবহারকারীর পাসওয়ার্ড সেট করতে দেয়। ব্যবহারকারী অ্যাকাউন্ট নির্দিষ্ট করে এবং একটি নতুন পাসওয়ার্ড প্রদান করে, আপনি পাসওয়ার্ড নীতি প্রয়োগ করতে এবং নিরাপদ ব্যবহারকারী প্রমাণীকরণ নিশ্চিত করতে পারেন। এখানে "AmyJohnson" নামে একটি ব্যবহারকারীর জন্য নতুন পাসওয়ার্ড সেট করার উদাহরণ দেওয়া হলো:

  ```powershell
  Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
  ```

এই নিরাপত্তা-সম্পর্কিত cmdlet গুলো ব্যবহার করে, প্রশাসকরা Active Directory পরিবেশে ব্যবহারকারীর প্রবেশাধিকার, গ্রুপ সদস্যপদ এবং পাসওয়ার্ড নীতি কার্যকরভাবে পরিচালনা করতে পারেন।

## PowerShell এর জন্য উদাহরণ Active Directory মডিউল স্ক্রিপ্ট
```powershell
# Import Active Directory module
Import-Module ActiveDirectory

# Retrieve Active Directory information
Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
Get-ADGroup -Filter 'GroupCategory -eq "Security"'
Get-ADOrganizationalUnit -Filter *

# Create a new Active Directory user
New-ADUser -SamAccountName "john.doe" -Name "John Doe"

# Create a new Active Directory group
New-ADGroup -Name "Marketing" -Description "Marketing Team"

# Create a new Active Directory organizational unit
New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"

# Modify Active Directory objects
Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"

# Manage Active Directory security
Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
```

## উপসংহার

সংক্ষেপে, **PowerShell এর জন্য Active Directory মডিউল** একটি শক্তিশালী টুল যা Windows Active Directory এর কার্যকর ও সুবিধাজনক ব্যবস্থাপনা সক্ষম করে। মডিউল ইনস্টল ও ইমপোর্ট করার মাধ্যমে, আপনি একটি বিস্তৃত **cmdlet** সেটে প্রবেশাধিকার পান যা বিভিন্ন AD-সম্পর্কিত কাজ সহজ করে।

Active Directory মডিউল ব্যবহার করে, আপনি AD অবজেক্ট সম্পর্কে তথ্য সংগ্রহ, নতুন অবজেক্ট তৈরি, গুণাবলী পরিবর্তন এবং নিরাপত্তা পরিচালনার মতো অনেক অপারেশন করতে পারেন। এই মডিউল প্রশাসকদের প্রশাসনিক কাজগুলো স্বয়ংক্রিয় করতে, ওয়ার্কফ্লো সহজ করতে এবং Active Directory পরিবেশের সুষ্ঠু কার্যকারিতা নিশ্চিত করতে সাহায্য করে।

**PowerShell** এবং **Active Directory মডিউল** ব্যবহার করে, আপনি আপনার AD প্রশাসন দক্ষতা বৃদ্ধি করতে এবং AD ব্যবস্থাপনা প্রক্রিয়াগুলোর কার্যকারিতা উন্নত করতে পারেন। আপনি হোন সিস্টেম প্রশাসক, IT পেশাজীবী বা Active Directory ম্যানেজার, Active Directory মডিউল আপনাকে আপনার AD অবকাঠামো কার্যকরভাবে পরিচালনার জন্য প্রয়োজনীয় সরঞ্জাম প্রদান করে।

**PowerShell** এবং **Active Directory মডিউল** এর শক্তি গ্রহণ করুন আপনার AD প্রশাসন কাজগুলো সহজ করতে, উৎপাদনশীলতা বাড়াতে এবং একটি নিরাপদ ও সুসংগঠিত Active Directory পরিবেশ বজায় রাখতে।

## রেফারেন্সসমূহ

- [Install-WindowsFeature cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature)
- [Import-Module cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module)
- [Active Directory cmdlets in PowerShell - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/activedirectory)
