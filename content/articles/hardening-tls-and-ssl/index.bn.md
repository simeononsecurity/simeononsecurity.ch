---
title: "SSL এবং TLS 1.1 ও তার আগের সংস্করণ বন্ধ করে কম্পিউটারের নিরাপত্তা জোরদার করুন"
date: 2023-02-08
lastmod: 2026-11-13
toc: true
draft: false
description: "TLS 1.2 বা নতুন সংস্করণ চালু রেখে SSL ও পুরোনো TLS সংস্করণ বন্ধ করুন। এতে Windows Schannel, .NET এবং Linux পরিষেবা আলোচিত হয়েছে।"
tags: ['কম্পিউটার নিরাপত্তা জোরদার', 'SSL এবং TLS বন্ধ করা', 'ডেটা নিরাপত্তা', 'POODLE', 'BEAST', 'Heartbleed', 'Windows রেজিস্ট্রি এডিটর', 'Linux OpenSSL কনফিগারেশন', 'Apache', 'Nginx']
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.webp"
coverAlt: "ডেটা নিরাপত্তার প্রতীক তালাযুক্ত একটি কম্পিউটার"
coverCaption: ""
---

## ভূমিকা:

কম্পিউটার আমাদের দৈনন্দিন জীবনের গুরুত্বপূর্ণ অংশ হয়ে উঠেছে, তাই ডেটা সুরক্ষার প্রয়োজনও বেড়েছে। চলাচলের সময় ডেটা সুরক্ষায় SSL (Secure Socket Layer) এবং TLS (Transport Layer Security) ব্যাপকভাবে ব্যবহৃত হয়। প্রযুক্তির অগ্রগতির সঙ্গে পুরোনো সংস্করণগুলো সাইবার আক্রমণের ঝুঁকিতে পড়েছে। এই নিবন্ধে SSL এবং TLS 1.0 ও 1.1 বন্ধ রেখে TLS 1.2 বা TLS 1.3 চালু রাখার উপায় ব্যাখ্যা করা হয়েছে।

*TLS 1.2 অপ্রচলিত প্রোটোকল নয়। বর্তমান ন্যূনতম মান হলো TLS 1.2 বা নতুন সংস্করণ। [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)-এ TLS 1.3 সংজ্ঞায়িত হয়েছে, আর [RFC 8996](https://www.rfc-editor.org/rfc/rfc8996) আনুষ্ঠানিকভাবে TLS 1.0 ও TLS 1.1 অপ্রচলিত ঘোষণা করে।*

### SSL এবং TLS 1.1 ও তার আগের সংস্করণ বন্ধ করবেন কেন?

SSL এবং TLS-এর পুরোনো সংস্করণ POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) এবং Heartbleed-এর মতো হুমকির ঝুঁকিতে রয়েছে। এসব আক্রমণে সংবেদনশীল তথ্য প্রকাশ পেতে পারে, তাই পুরোনো প্রোটোকল বন্ধ করা জরুরি। Heartbleed নিজে কোনো প্রোটোকল সংস্করণ ছিল না, এটি দুর্বল OpenSSL বাস্তবায়নকে প্রভাবিত করেছিল। লাইব্রেরি প্যাচ করুন এবং উন্মুক্ত হয়ে থাকতে পারে এমন পরিচয়পত্র বদলান।

Microsoft-এর বর্তমান [Schannel রেজিস্ট্রি নির্দেশিকা](https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings)-তে সমর্থিত Windows সংস্করণের প্রোটোকল সেটিংস রয়েছে। Group Policy বা সমর্থিত ব্যবস্থাপনা সরঞ্জাম থাকলে সেগুলো ব্যবহারের পরামর্শ দেয় Microsoft। ভালো নিয়ন্ত্রণ না থাকলেই সরাসরি রেজিস্ট্রি সম্পাদনা করুন।

### Windows-এ SSL এবং TLS 1.1 ও তার আগের সংস্করণ বন্ধ করা:

Windows-এ রেজিস্ট্রি এডিটর দিয়ে SSL এবং TLS 1.1 ও তার আগের সংস্করণ বন্ধ করা যায়। নিচের PowerShell স্ক্রিপ্টটি Schannel-এর ক্লায়েন্ট ও সার্ভার সেটিংস বদলায়। এটি .NET-কে অপারেটিং সিস্টেমের TLS ডিফল্ট এবং শক্তিশালী ক্রিপ্টোগ্রাফি ব্যবহার করতেও সেট করে।

```powershell
Function Disable-Protocol {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Protocol
    )
    $ServerPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\$Protocol\Server"
    $ClientPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\$Protocol\Client"
    New-Item -Path $ServerPath -Force
    New-Item -Path $ClientPath -Force
    Set-ItemProperty -Path $ServerPath -Force -Name Enabled -Type "DWORD" -Value 0
    Set-ItemProperty -Path $ServerPath -Force -Name DisabledByDefault -Type "DWORD" -Value 1
    Set-ItemProperty -Path $ClientPath -Force -Name Enabled -Type "DWORD" -Value 0
    Set-ItemProperty -Path $ClientPath -Force -Name DisabledByDefault -Type "DWORD" -Value 1
}
# Disable SSL v2
Disable-Protocol -Protocol "SSL 2.0"
# Disable SSL v3
Disable-Protocol -Protocol "SSL 3.0"
# Disable TLS 1.0
Disable-Protocol -Protocol "TLS 1.0"
# Disable DTLS 1.0
Disable-Protocol -Protocol "DTLS 1.0"
# Disable TLS 1.1
Disable-Protocol -Protocol "TLS 1.1"
# There is no DTLS 1.1 protocol. RFC 8996 deprecates DTLS 1.0 and retains DTLS 1.2.

function Set-NETStrongAuthentication {
    param(
        [string]$RegistryPath,
        [string]$Name,
        [string]$Type,
        [int]$Value
    )
    Set-ItemProperty -Path $RegistryPath -Force -Name $Name -Type $Type -Value $Value
}

$NETVersions = @("2.0.50727", "3.0", "4.0.30319")

foreach ($version in $NETVersions) {
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\Microsoft\.NETFramework\v$version" -Name SchUseStrongCrypto -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\Microsoft\.NETFramework\v$version" -Name SystemDefaultTlsVersions -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v$version" -Name SchUseStrongCrypto -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v$version" -Name SystemDefaultTlsVersions -Type "DWORD" -Value 0x00000001
}
```

#### Linux-এ SSL এবং TLS 1.1 ও তার আগের সংস্করণ বন্ধ করা:

Linux-এ পুরোনো প্রোটোকল বন্ধ করার পদ্ধতি অ্যাপ্লিকেশন ও লাইব্রেরির ওপর নির্ভর করে। `/etc/ssl/openssl.cnf` সম্পাদনা করলে প্রতিটি ডেমন বা অন্তর্ভুক্ত TLS লাইব্রেরির সেটিং বদলায় না। ধাপগুলো অনুসরণ করুন:

1. টার্মিনাল খুলুন এবং root হিসেবে লগ ইন করুন।
2. OpenSSL কনফিগারেশন ফাইলে যান। সাধারণত এটি /etc/ssl/openssl.cnf-এ থাকে।
3. nano বা vim-এর মতো টেক্সট এডিটরে ফাইলটি খুলুন।
4. পরিষেবার প্রোটোকল নির্দেশিকা খুঁজে ন্যূনতম সংস্করণ TLS 1.2 নির্ধারণ করুন। পুরোনো `-TLSv1.2` নির্দেশটি TLS 1.2 বন্ধ করত, তাই আধুনিক ন্যূনতম মান হিসেবে এটি ব্যবহার করবেন না।
5. ফাইল সংরক্ষণ করে টেক্সট এডিটর বন্ধ করুন।
6. পরিবর্তন কার্যকর করতে Apache বা Nginx-এর মতো OpenSSL-নির্ভর পরিষেবা পুনরায় চালু করুন।

## উপসংহার:

SSL এবং TLS 1.1 ও তার আগের সংস্করণ বন্ধ করলে আধুনিক TLS ক্লায়েন্টের সামঞ্জস্য বজায় রেখে কম্পিউটারের নিরাপত্তা বাড়ে। TLS আলোচনাকারী পরিষেবাতেই সঠিক সেটিং নির্ধারিত হয়, তাই একটি OpenSSL ফাইল সব ডেমন নিয়ন্ত্রণ করে ধরে না নিয়ে প্রতিটি অ্যাপ্লিকেশন পরীক্ষা করুন।

পুরোনো সংস্করণ বন্ধ করলে কিছু পুরোনো সিস্টেমের সঙ্গে সামঞ্জস্যে প্রভাব পড়তে পারে। সম্পূর্ণ প্রয়োগের আগে পরিবর্তনগুলো ভালোভাবে পরীক্ষা করুন এবং সিস্টেমে বিরূপ প্রভাব নেই নিশ্চিত করুন।

সংবেদনশীল তথ্য সুরক্ষিত রাখতে এবং আক্রমণের ঝুঁকি কমাতে এই নিবন্ধের ধাপগুলো অনুসরণ করুন। প্রথমে প্রতিটি পরিষেবার ব্যবহৃত প্রোটোকল শনাক্ত করুন, তারপর অস্থায়ী ব্যতিক্রম নথিভুক্ত করুন।

## বর্তমান যাচাই তালিকা

- **আলোচিত প্রোটোকল যাচাই করুন।** TLS স্ক্যানার বা অনুমোদিত অভ্যন্তরীণ পরীক্ষা দিয়ে সংযোগের উভয় পাশে ক্লায়েন্ট ও সার্ভার পরীক্ষা করুন।
- **TLS 1.2 চালু রাখুন।** কিছু পুরোনো অ্যাপ্লিকেশনের এখনও এটি দরকার, আর TLS 1.3 সমর্থন অপারেটিং সিস্টেম ও লাইব্রেরির ওপর নির্ভর করে।
- **DTLS আলাদাভাবে পর্যালোচনা করুন।** RFC 8996-এ DTLS 1.0 অবহিত করা হয়েছে। এতে DTLS 1.1 প্রোটোকল সংজ্ঞায়িত হয়নি।
- **প্রভাবিত পরিষেবা পুনরায় চালু করুন।** নতুন নীতি কার্যকর করতে Schannel ও অ্যাপ্লিকেশন সেটিংসে প্রায়ই পরিষেবা বা সিস্টেম পুনরায় চালু করতে হয়।
- **ব্যতিক্রম নথিভুক্ত করুন।** সাময়িক সামঞ্জস্য সেটিং দরকার এমন পুরোনো প্রতিটি এন্ডপয়েন্ট লিখে রাখুন এবং অপসারণের তারিখ দিন।
