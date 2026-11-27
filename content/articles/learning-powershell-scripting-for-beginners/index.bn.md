---
title: "PowerShell স্ক্রিপ্টিং"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-27
description: "কমান্ডলেট, লুপ, ফাংশনসহ ধাপে ধাপে সাজানো এই শিক্ষানবিশ নির্দেশিকা থেকে PowerShell স্ক্রিপ্টিংয়ের ভিত্তি শিখুন এবং কাজ স্বয়ংক্রিয় করুন।"
genre: ["প্রযুক্তি", "প্রোগ্রামিং", "স্বয়ংক্রিয়করণ", "Windows", "স্ক্রিপ্টিং", "আইটি", "প্রশাসনিক কাজ", "কম্পিউটার ব্যবস্থাপনা", "সফটওয়্যার উন্নয়ন", "কোডিং"]
tags: ["PowerShell স্ক্রিপ্টিং", "PowerShell স্বয়ংক্রিয়করণ", "Windows স্ক্রিপ্টিং", "PowerShell কমান্ডলেট", "PowerShell মডিউল", "PowerShell লুপ", "PowerShell শর্তাধীন বিবৃতি", "PowerShell ফাংশন", "PowerShell-এর উত্তম পদ্ধতি", "PowerShell ডিবাগিং", "PowerShell পরীক্ষা", "PowerShell ভেরিয়েবল", "PowerShell ISE", "PowerShell Remoting", "Microsoft প্রযুক্তি", "আইটি স্বয়ংক্রিয়করণ", "কম্পিউটার ব্যবস্থাপনা", "শিক্ষানবিশদের কোডিং", "প্রশাসনিক কাজ", "PowerShell স্ক্রিপ্টের ধারণা", "স্বয়ংক্রিয় ব্যাকআপ", "ফাইল ব্যবস্থাপনা", "সিস্টেমের তথ্য", "ব্যবহারকারী ব্যবস্থাপনা", "সফটওয়্যার ইনস্টলেশন", "নেটওয়ার্ক কনফিগারেশন", "নিরাপত্তা স্বয়ংক্রিয়করণ", "কাজের সময়সূচি", "রেজিস্ট্রি পরিবর্তন", "দূরবর্তী প্রশাসন"]
cover: "/img/cover/A_cartoon_character_holding_a_script_and_standing.webp"
coverAlt: "PowerShell প্রম্পট দেখানো কম্পিউটারের সামনে স্ক্রিপ্ট হাতে একটি কার্টুন চরিত্র, যা শিক্ষানবিশদের জন্য PowerShell স্ক্রিপ্টিংয়ের সহজতা বোঝায়"
coverCaption: ""
---
**শিক্ষানবিশদের জন্য PowerShell স্ক্রিপ্টিং**

PowerShell হলো Microsoft-এর তৈরি একটি কমান্ড-লাইন শেল ও স্ক্রিপ্টিং ভাষা। Windows অপারেটিং সিস্টেম এবং অন্যান্য Microsoft প্রযুক্তির নানা দিক পরিচালনা ও স্বয়ংক্রিয় করার জন্য এতে প্রচুর কমান্ড ও সুবিধা রয়েছে। এই নিবন্ধে PowerShell স্ক্রিপ্টিংয়ের ভিত্তি তুলে ধরা হয়েছে এবং শুরু করার ধাপগুলো দেখানো হয়েছে।

## PowerShell পরিচিতি

**PowerShell** হলো একটি কমান্ড-লাইন শেল, যা Windows অপারেটিং সিস্টেম এবং অন্যান্য Microsoft প্রযুক্তি স্বয়ংক্রিয় ও পরিচালনা করতে সহায়তা করে। ফাইল ও ডিরেক্টরি ব্যবস্থাপনা, নেটওয়ার্ক কনফিগারেশন এবং সিস্টেম ব্যবস্থাপনার মতো প্রশাসনিক কাজ করার জন্য এতে বিস্তৃত কমান্ড ও সুবিধা রয়েছে। PowerShell-এর স্ক্রিপ্টিং ভাষা দিয়ে জটিল স্ক্রিপ্ট তৈরি করা এবং পুনরাবৃত্ত কাজ স্বয়ংক্রিয় করা যায়।

## PowerShell দিয়ে শুরু করা

### PowerShell ইনস্টল করা

Windows-এর অধিকাংশ সংস্করণে PowerShell আগে থেকেই ইনস্টল থাকে। আপনি পুরোনো Windows সংস্করণ ব্যবহার করলে অথবা PowerShell-এর নতুন সংস্করণ দরকার হলে Microsoft-এর ওয়েবসাইট থেকে ডাউনলোড করুন। PowerShell ডাউনলোড ও ইনস্টল করতে এই ধাপগুলো অনুসরণ করুন:

1. [Microsoft PowerShell ওয়েবসাইটে](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2) যান এবং যে সংস্করণটি ইনস্টল করতে চান তা বেছে নিন।
2. ইনস্টলেশন ফাইল ডাউনলোড করে চালান।
3. ইনস্টলেশন শেষ করতে পর্দায় দেখানো নির্দেশনা অনুসরণ করুন।

### PowerShell চালু করা

PowerShell ইনস্টল করার পর এই ধাপগুলো অনুসরণ করে চালু করুন:

1. Start মেনু খুলে অনুসন্ধান বারে "PowerShell" লিখুন।
2. অনুসন্ধানের ফল থেকে "Windows PowerShell" বেছে নিন।
3. PowerShell নতুন উইন্ডোতে খুলবে।

### Visual Studio Code-এ PowerShell স্ক্রিপ্টিং

আরও উন্নত স্ক্রিপ্টিং অভিজ্ঞতার জন্য জনপ্রিয় সমন্বিত উন্নয়ন পরিবেশ (IDE) Visual Studio Code (VS Code) ব্যবহার করতে পারেন। VS Code-এ সিনট্যাক্স হাইলাইটিং, কোড সম্পূর্ণ করার সুবিধা, ডিবাগিং এবং সমন্বিত টার্মিনাল রয়েছে, তাই PowerShell স্ক্রিপ্টিংয়ের জন্য এটি ভালো পছন্দ। VS Code-এ শুরু করতে:

1. [অফিশিয়াল ওয়েবসাইট](https://code.visualstudio.com/) থেকে Visual Studio Code ইনস্টল করুন।
2. VS Code-এর এক্সটেনশনের বাজার থেকে Microsoft-এর "PowerShell" এক্সটেনশন ইনস্টল করুন।
3. VS Code-এ PowerShell স্ক্রিপ্ট ফাইল (.ps1) খুলে স্ক্রিপ্ট লেখা শুরু করুন।

### সিস্টেম প্রশাসনে PowerShell

সিস্টেম প্রশাসনের কাজে PowerShell বহুমুখী একটি টুল। এক লাইনের সাধারণ কমান্ড থেকে জটিল স্বয়ংক্রিয় কর্মপ্রবাহ পর্যন্ত, এটি এমন কাজ সহজ করে যা অন্যথায় হাতে করতে হতো। Windows, Linux এবং macOS-এ একই স্ক্রিপ্টিং প্ল্যাটফর্ম দিয়ে প্রশাসকেরা ভিন্ন পরিবেশ পরিচালনার জন্য সামঞ্জস্যপূর্ণ টুলসেট পান।

### Command Prompt থেকে Windows PowerShell-এ যাওয়া

আপনি Command Prompt-এ অভ্যস্ত হলে Windows PowerShell-এ যাওয়ার শেখার ধাপ সহজ হতে পারে। Windows PowerShell স্ক্রিপ্টিং Command Prompt-এর ধারণার ওপর ভিত্তি করে আরও উন্নত সুবিধা দেয়। বিদ্যমান জ্ঞান কাজে লাগিয়ে PowerShell-এর অতিরিক্ত বৈশিষ্ট্য ও কমান্ডলেট ধীরে ধীরে শিখুন।

### PowerShell-এর ভিত্তি

অপারেটিং সিস্টেমের সঙ্গে কাজ করার জন্য PowerShell কমান্ড-লাইন ইন্টারফেস দেয়। এর কমান্ডগুলোকে কমান্ডলেট বলা হয় এবং সেগুলো মডিউলে সাজানো থাকে। উপলভ্য মডিউলের তালিকা দেখতে Get-Module কমান্ড ব্যবহার করুন:

```powershell
Get-Module
```

কোনো মডিউলে উপলভ্য কমান্ডলেট দেখতে Get-Command ব্যবহার করুন:
```powershell
Get-Command -Module <module name>
```

কোনো কমান্ডলেট-এর সাহায্য পেতে Get-Help ব্যবহার করুন:
```powershell
Get-Help <কমান্ডলেট name>
```

PowerShell alias-ও সমর্থন করে, যা কমান্ডলেট-এর সংক্ষিপ্ত নাম। উপলভ্য alias-এর তালিকা দেখতে Get-Alias ব্যবহার করুন:
```powershell
Get-Alias
```

## স্ক্রিপ্ট ফাইল এবং এক্সিকিউশন নীতি

PowerShell স্ক্রিপ্ট ফাইলে .ps1 এক্সটেনশন থাকে। স্ক্রিপ্ট চালানোর আগে এক্সিকিউশন নীতি সেট করার দরকার হতে পারে। এই নীতি নির্ধারণ করে স্ক্রিপ্ট চালানো যাবে কি না এবং কোন ধরনের স্ক্রিপ্ট চলতে পারবে। নীতি সেট করতে Set-ExecutionPolicy কমান্ডলেট ব্যবহার করুন। উদাহরণস্বরূপ, স্ক্রিপ্ট চালানোর অনুমতি দিতে:

```powershell
Set-ExecutionPolicy RemoteSigned
```

অথবা (শুধু পরীক্ষার জন্য)

```powershell
Set-ExecutionPolicy Undefined
```

### PowerShell স্ক্রিপ্টিং

PowerShell স্ক্রিপ্টিং দিয়ে বিভিন্ন প্রশাসনিক কাজ স্বয়ংক্রিয় করা যায়। এতে ভেরিয়েবল, লুপ, শর্তাধীন বিবৃতি এবং ফাংশন সমর্থিত, যা একে স্বয়ংক্রিয়করণের কার্যকর টুল করে তোলে।

#### ভেরিয়েবল

PowerShell স্ক্রিপ্টে তথ্য সংরক্ষণে ভেরিয়েবল ব্যবহার হয়। PowerShell-এ ভেরিয়েবলের নাম ডলার চিহ্ন ($) দিয়ে শুরু হয়। ভেরিয়েবলে মান দিতে এই গঠন ব্যবহার করুন:
```powershell
$variable_name = value
```
উদাহরণ:
```powershell
$name = "John"
```
#### লুপ

লুপ নির্দিষ্ট সংখ্যক বার কোডের একটি অংশ পুনরাবৃত্তি করে। PowerShell-এ এই ধরনের লুপ রয়েছে:

- **For লুপ**: নির্দিষ্ট সংখ্যক বার কোডের অংশ পুনরাবৃত্তি করে।
- **While লুপ**: শর্ত সত্য থাকা পর্যন্ত কোডের অংশ পুনরাবৃত্তি করে।
- **Do-While লুপ**: অন্তত একবার কোড চালিয়ে শর্ত সত্য থাকা পর্যন্ত পুনরাবৃত্তি করে।
- **ForEach লুপ**: কোনো সংগ্রহের প্রতিটি উপাদানের জন্য কোডের অংশ পুনরাবৃত্তি করে।

নিচের কোডে For লুপ ব্যবহার করে 1 থেকে 5 পর্যন্ত সংখ্যা দেখানো হয়েছে:
```powershell
for($i=1; $i -le 5; $i++) {
Write-Host $i
}
```

#### শর্তাধীন বিবৃতি

শর্তাধীন বিবৃতি

নির্দিষ্ট শর্ত সত্য হলে শর্তাধীন বিবৃতি কোডের একটি অংশ চালায়। PowerShell-এ এই ধরনের বিবৃতি রয়েছে:

- **If বিবৃতি**: শর্ত সত্য হলে কোডের একটি অংশ চালায়।
- **If-Else বিবৃতি**: শর্ত সত্য হলে একটি অংশ, মিথ্যা হলে অন্য অংশ চালায়।
- **Switch বিবৃতি**: কোনো মানকে সম্ভাব্য মিলের তালিকার সঙ্গে তুলনা করে এবং প্রথম মিলটির অংশ চালায়।

উদাহরণস্বরূপ, নিচের কোড If ব্যবহার করে কোনো সংখ্যা 5-এর চেয়ে বড় কি না যাচাই করে:

```powershell
$number = 10
if ($number -gt 5) {
    Write-Host "সংখ্যাটি 5-এর চেয়ে বড়"
}
```
#### ফাংশন

ফাংশন হলো নির্দিষ্ট কাজ করা পুনর্ব্যবহারযোগ্য কোড ব্লক। ফাংশন ইনপুট প্যারামিটার নেয় এবং ফলাফল ফেরত দেয়। PowerShell-এ এই ধরনের ফাংশন রয়েছে:

- **স্ক্রিপ্ট ব্লক**: চালানো যায় এমন কোডের একটি অংশ।
- **উন্নত ফাংশন**: মেটাডেটা এবং প্যারামিটার যাচাইসহ ফাংশন।

উদাহরণস্বরূপ, নিচের কোডে দুটি সংখ্যা যোগ করার ফাংশন সংজ্ঞায়িত করা হয়েছে:
```powershell
function Add-Numbers {
    param (
        [int]$num1,
        [int]$num2
    )
    $result = $num1 + $num2
    return $result
}

$result = Add-Numbers -num1 5 -num2 10
Write-Host "ফলাফল $result"
```
### PowerShell ISE

PowerShell ISE (সমন্বিত স্ক্রিপ্টিং পরিবেশ) হলো PowerShell স্ক্রিপ্টিংয়ের গ্রাফিক্যাল ইন্টারফেস। এতে সমৃদ্ধ টেক্সট এডিটর, ডিবাগিং টুল এবং স্ক্রিপ্ট লেখা ও পরীক্ষা সহজ করার অন্যান্য সুবিধা রয়েছে। PowerShell ISE খুলতে:

1. Start মেনু খুলে অনুসন্ধান বারে "PowerShell ISE" লিখুন।
2. অনুসন্ধানের ফল থেকে "Windows PowerShell ISE" বেছে নিন।
3. PowerShell ISE নতুন উইন্ডোতে খুলবে।

### PowerShell Remoting

PowerShell Remoting দিয়ে দূরবর্তী কম্পিউটারে PowerShell কমান্ড ও স্ক্রিপ্ট চালানো যায়। স্থানীয় ও দূরবর্তী উভয় কম্পিউটারে WinRM পরিষেবা চালু থাকতে হবে। PowerShell Remoting চালু করতে:

1. প্রশাসকের অধিকারসহ PowerShell প্রম্পট খুলুন।
2. PowerShell Remoting চালু করতে এই কমান্ড চালান:
```powershell
   Enable-PSRemoting -Force
```
3. দূরবর্তী কম্পিউটারকে TrustedHosts তালিকায় যোগ করতে এই কমান্ড চালান:
```powershell
Set-Item wsman:\localhost\Client\TrustedHosts -Value <computer name> -Force
```
4. WinRM পরিষেবা পুনরায় চালু করুন।
```powershell
Restart-Service WinRM
```

দূরবর্তী কম্পিউটারে PowerShell কমান্ড চালাতে Invoke-Command কমান্ডলেট ব্যবহার করুন:
```powershell
Invoke-Command -ComputerName <computer name> -ScriptBlock { <command> }
```
### PowerShell মডিউল

PowerShell মডিউল হলো নির্দিষ্ট কাজের জন্য তৈরি কমান্ডলেট, ফাংশন ও স্ক্রিপ্টের সংগ্রহ। PowerShell মডিউলের কেন্দ্রীয় ভান্ডার PowerShell Gallery দিয়ে এগুলো ইনস্টল ও পরিচালনা করা যায়।

PowerShell Gallery থেকে মডিউল ইনস্টল করতে:
```powershell
Install-Module <module name>
```

ইনস্টল করা PowerShell মডিউলের তালিকা দেখতে Get-InstalledModule ব্যবহার করুন:
```powershell
Get-InstalledModule
```

### PowerShell স্ক্রিপ্টিংয়ের উত্তম পদ্ধতি

**PowerShell স্ক্রিপ্ট** লেখার সময় সেগুলোকে **নিরাপদ**, **নির্ভরযোগ্য** এবং **রক্ষণাবেক্ষণযোগ্য** রাখতে উত্তম পদ্ধতি অনুসরণ করুন। কয়েকটি পরামর্শ:

- **বর্ণনামূলক ভেরিয়েবলের নাম ব্যবহার করুন**: উদ্দেশ্য স্পষ্ট করে এমন নাম বেছে নিন।
- **মন্তব্য লিখুন**: কোডের উদ্দেশ্য ব্যাখ্যা করুন।
- **ত্রুটি সামলান**: ত্রুটি ও ব্যতিক্রম যথাযথভাবে সামলান। PowerShell-এর `Try...Catch...Finally` কাঠামো ব্যতিক্রম ধরে উপযুক্ত পদক্ষেপ নিতে সাহায্য করে। [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-try-catch-finally?view=powershell-7.1)
- **স্ক্রিপ্ট ভালোভাবে পরীক্ষা করুন**: প্রত্যাশামতো কাজ করছে কি না যাচাই করুন। PowerShell পরীক্ষার কাঠামো **Pester** দিয়ে ইউনিট পরীক্ষা লেখা ও চালানো যায়। [Pester ডকুমেন্টেশন](https://pester.dev/)
- **ফাংশন ও মডিউল ব্যবহার করুন**: কোড সাজিয়ে পুনর্ব্যবহার সহজ করুন। ফাংশন কোডকে ছোট পরিচালনাযোগ্য অংশে ভাগ করে, আর মডিউল কোড প্যাকেজ ও বিতরণের উপায় দেয়। [ফাংশন সম্পর্কে](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-functions?view=powershell-7.1), [মডিউল সম্পর্কে](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-modules?view=powershell-7.1)
- **কোডে মান স্থায়ীভাবে লিখবেন না**: প্যারামিটার বা ভেরিয়েবল ব্যবহার করলে স্ক্রিপ্ট নমনীয় ও পুনর্ব্যবহারযোগ্য হয়। `param` কীওয়ার্ড দিয়ে স্ক্রিপ্টে প্যারামিটার পাঠান। [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters?view=powershell-7.1)
- **বিস্তারিত আউটপুট ব্যবহার করুন**: স্ক্রিপ্টের অগ্রগতি সম্পর্কে অতিরিক্ত তথ্য দিতে `Write-Verbose` কমান্ডলেট ব্যবহার করুন। [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-verbose?view=powershell-7.1)

### PowerShell স্ক্রিপ্টিংয়ের উত্তম পদ্ধতির বিস্তারিত

#### ত্রুটি সামলান

PowerShell স্ক্রিপ্টিংয়ে ত্রুটি সামলানো জরুরি, কারণ এর ফলে স্ক্রিপ্ট ত্রুটি ও ব্যতিক্রম যথাযথভাবে সামলাতে পারে। PowerShell-এ Try-Catch বিবৃতি, Trap বিবৃতি এবং ErrorAction প্যারামিটারসহ কয়েকটি উপায় রয়েছে। Try-Catch ব্যতিক্রম ধরে ও সামলায়, Trap ত্রুটি ধরে ও সামলায়, আর ErrorAction নিয়ন্ত্রণ করে স্ক্রিপ্ট ত্রুটির প্রতিক্রিয়া কীভাবে দেবে।

Try-Catch দিয়ে ত্রুটি সামলানোর উদাহরণ:
```powershell
try {
    # যে কোডে ত্রুটি হতে পারে
}
catch {
    Write-Error "একটি ত্রুটি ঘটেছে: $_"
}
```

#### স্ক্রিপ্ট ভালোভাবে পরীক্ষা করুন

PowerShell স্ক্রিপ্ট প্রত্যাশামতো কাজ করছে কি না নিশ্চিত করতে পরীক্ষা জরুরি। Pester-এর মতো পরীক্ষা টুল ও কাঠামো পরীক্ষা লেখা ও চালাতে দেয়। এগুলো কোডের সমস্যা শনাক্ত ও আলাদা করতে এবং স্ক্রিপ্ট চাহিদা পূরণ করছে কি না যাচাই করতে সাহায্য করে।

PowerShell স্ক্রিপ্ট পরীক্ষায় Pester ব্যবহারের উদাহরণ:
```powershell
Describe "আমার PowerShell স্ক্রিপ্ট" {
    It "নির্দিষ্ট কাজ করে" {
        # যে কোডের প্রত্যাশিত ফল দেওয়ার কথা
        $result = Do-Something
        $result | Should -Be "প্রত্যাশিত ফল"
    }
}
```

#### ফাংশন ও মডিউল ব্যবহার করুন

PowerShell স্ক্রিপ্টিংয়ে কোড সাজানো ও পুনর্ব্যবহার সহজ করতে ফাংশন এবং মডিউল দরকারি। ফাংশন কোডকে পুনর্ব্যবহারযোগ্য ব্লকে সাজায়, আর মডিউল কোড প্যাকেজ করে অন্যদের সঙ্গে ভাগ করতে দেয়। এগুলো ব্যবহার করলে স্ক্রিপ্ট আরও মডিউলার, কার্যকর এবং রক্ষণাবেক্ষণযোগ্য হয়।

PowerShell ফাংশনের উদাহরণ:
```powershell
function Get-ProcessCount {
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount
Write-Host "$countটি প্রক্রিয়া চলছে।"
```

#### কোডে মান স্থায়ীভাবে লিখবেন না

PowerShell স্ক্রিপ্টে মান স্থায়ীভাবে লিখলে নমনীয়তা কমে এবং রক্ষণাবেক্ষণ কঠিন হয়। তার বদলে প্যারামিটার বা ভেরিয়েবল ব্যবহার করুন, যাতে ব্যবহারকারী চালানোর সময় মান দিতে পারেন। এতে স্ক্রিপ্ট পুনর্ব্যবহার ও পরিবর্তিত পরিস্থিতির সঙ্গে মানিয়ে নেওয়া সহজ হয়।

PowerShell প্যারামিটারের উদাহরণ:
```powershell
param (
    [string]$name
)

Write-Host "হ্যালো, $name!"
```

#### বিস্তারিত আউটপুট ব্যবহার করুন

বিস্তারিত আউটপুট স্ক্রিপ্টের অগ্রগতি সম্পর্কে অতিরিক্ত তথ্য দেয়, যা ডিবাগিং ও সমস্যা সমাধানে কাজে লাগে। Write-Verbose কমান্ডলেট কনসোলে বিস্তারিত তথ্য দেখায়, ফলে স্ক্রিপ্ট বোঝা ও ডিবাগ করা সহজ হয়।

PowerShell-এ বিস্তারিত আউটপুটের উদাহরণ:
```powershell
function Get-ProcessCount {
    Write-Verbose "প্রক্রিয়াগুলো সংগ্রহ করা হচ্ছে..."
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount -Verbose
Write-Host "$countটি প্রক্রিয়া চলছে।"
```

### শিক্ষানবিশদের জন্য PowerShell স্ক্রিপ্টের দশটি ধারণা

আপনি PowerShell স্ক্রিপ্টিংয়ে নতুন হলে শুরু করার জন্য এই দশটি ধারণা চেষ্টা করুন:

- **স্বয়ংক্রিয় ব্যাকআপ**: গুরুত্বপূর্ণ ফাইল ও ডিরেক্টরি বাহ্যিক হার্ড ড্রাইভ বা ক্লাউড স্টোরেজে কপি করার স্ক্রিপ্ট তৈরি করুন। ফাইল কপি করতে `Copy-Item` এবং ব্যাকআপ পটভূমিতে চালাতে `Start-Job` কমান্ডলেট ব্যবহার করুন। [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.1)

- **ফাইল ব্যবস্থাপনা**: ফাইলের ধরন, আকার বা অন্য মানদণ্ড অনুসারে ফাইল ও ডিরেক্টরি বিভিন্ন ফোল্ডারে সাজানোর স্ক্রিপ্ট তৈরি করুন। ফাইল আনতে `Get-ChildItem` এবং নির্দিষ্ট জায়গায় নিতে `Move-Item` ব্যবহার করুন। [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.1), [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item?view=powershell-7.1)

- **সিস্টেমের তথ্য**: CPU ও মেমরির ব্যবহার, ডিস্কের জায়গা এবং নেটওয়ার্ক সেটিংসের মতো তথ্য সংগ্রহ করে সহজে পড়ার মতো করে দেখানো স্ক্রিপ্ট তৈরি করুন। তথ্য পেতে `Get-WmiObject` এবং সাজাতে `Format-Table` বা `Out-GridView` ব্যবহার করুন। [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-7.1)

- **ব্যবহারকারী ব্যবস্থাপনা**: Windows-এ ব্যবহারকারী ও গোষ্ঠী যোগ, পরিবর্তন বা মোছার কাজ স্বয়ংক্রিয় করার স্ক্রিপ্ট তৈরি করুন। ব্যবহারকারীর জন্য `New-LocalUser`, `Set-LocalUser` এবং `Remove-LocalUser`; গোষ্ঠীর জন্য `New-LocalGroup`, `Add-LocalGroupMember` এবং `Remove-LocalGroup` ব্যবহার করুন। [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localuser?view=powershell-7.1), [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localgroup?view=powershell-7.1)

- **সফটওয়্যার ইনস্টলেশন**: একই সঙ্গে একাধিক কম্পিউটারে সফটওয়্যার ইনস্টল ও কনফিগার করার স্ক্রিপ্ট তৈরি করুন। দূরবর্তী কম্পিউটারে ইনস্টলেশন কমান্ড চালাতে `Invoke-Command` ব্যবহার করুন। [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

- **নেটওয়ার্ক কনফিগারেশন**: IP ঠিকানা, সাবনেট মাস্ক এবং ডিফল্ট গেটওয়ের মতো নেটওয়ার্ক সেটিংস স্বয়ংক্রিয় করার স্ক্রিপ্ট তৈরি করুন। সেটিংস কনফিগার করতে `Set-NetIPAddress`, `Set-NetIPInterface` এবং `Set-DnsClientServerAddress` ব্যবহার করুন। [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipaddress?view=win10-ps), [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipinterface?view=win10-ps), [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/dnsclient/set-dnsclientserveraddress?view=win10-ps)

- **নিরাপত্তা**: নিরাপত্তা সেটিংস নিরীক্ষণ ও পর্যবেক্ষণ করে পরিবর্তন শনাক্ত হলে ব্যবহারকারীকে সতর্ক করার স্ক্রিপ্ট তৈরি করুন। নিরীক্ষা নীতি পেতে `Get-AuditPolicy` এবং ইমেইল সতর্কতা পাঠাতে `Send-MailMessage` ব্যবহার করুন। [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-auditpolicy?view=powershell-7.1), [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/send-mailmessage?view=powershell-7.1)

- **কাজের সময়সূচি**: ব্যাকআপ, আপডেট এবং সিস্টেম স্ক্যানের মতো নিয়মিত কাজের সময় নির্ধারণ ও স্বয়ংক্রিয় করার স্ক্রিপ্ট তৈরি করুন। নির্ধারিত কাজ তৈরি করতে `Register-ScheduledTask` এবং চালাতে `Start-ScheduledTask` ব্যবহার করুন। [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/register-scheduledtask?view=win10-ps), [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/start-scheduledtask?view=win10-ps)

- **রেজিস্ট্রি পরিবর্তন**: নির্দিষ্ট রেজিস্ট্রি কী বা মানের তথ্য দেখা বা বদলানোর স্ক্রিপ্ট তৈরি করুন। রেজিস্ট্রির সঙ্গে কাজ করতে `Get-ItemProperty` এবং `Set-ItemProperty` ব্যবহার করুন। [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-itemproperty?view=powershell-7.1), [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-itemproperty?view=powershell-7.1)

- **দূরবর্তী প্রশাসন**: Windows কম্পিউটারে দূরবর্তী প্রশাসন চালু করে দূরবর্তী মেশিনে কমান্ড ও স্ক্রিপ্ট চালানোর ব্যবস্থা করুন। দূরবর্তী কম্পিউটারে কমান্ড চালাতে `Enter-PSSession` বা `Invoke-Command` ব্যবহার করুন। [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enter-pssession?view=powershell-7.1), [Microsoft ডকুমেন্টেশন](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

বাস্তব অভিজ্ঞতা অর্জন এবং PowerShell স্ক্রিপ্টিংয়ের জ্ঞান বাড়াতে এই ধারণাগুলো নিয়ে কাজ শুরু করুন।

## উপসংহার

Windows অপারেটিং সিস্টেম ও অন্যান্য Microsoft প্রযুক্তি পরিচালনা এবং স্বয়ংক্রিয় করার শক্তিশালী টুল হলো PowerShell। এই নিবন্ধে শিক্ষানবিশদের জন্য স্ক্রিপ্টিংয়ের ভিত্তি আলোচনা করেছি: ইনস্টল ও চালু করা, কমান্ডলেট, ভেরিয়েবল, লুপ, শর্তাধীন বিবৃতি ও ফাংশন ব্যবহার, PowerShell ISE, PowerShell Remoting এবং মডিউল। উত্তম পদ্ধতি মেনে চললে স্ক্রিপ্ট নিরাপদ, নির্ভরযোগ্য ও রক্ষণাবেক্ষণযোগ্য হয়। অনুশীলনের মাধ্যমে PowerShell-এ দক্ষ হয়ে বিভিন্ন প্রশাসনিক কাজ সহজে স্বয়ংক্রিয় করতে পারবেন।
