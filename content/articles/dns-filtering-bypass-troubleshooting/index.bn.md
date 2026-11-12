---
title: "DNS ফিল্টার কেন পাশ কাটানো হচ্ছে: রিজলভার পথ পরীক্ষা করুন"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "কোনো ডিভাইস বা ব্রাউজার কেন DNS ফিল্টার এড়িয়ে যাচ্ছে তা খুঁজে বের করুন। সরাসরি ও স্বাভাবিক query তুলনা করুন, log দেখুন, তারপর encrypted DNS, VPN, IPv6 ও router সেটিং পরীক্ষা করুন।"
genre: ["হোম নেটওয়ার্ক", "DNS", "গোপনীয়তা"]
tags: ["DNS filtering bypass", "Pi-hole bypass", "DNS query log", "browser secure DNS", "DNS over HTTPS", "Android Private DNS", "iCloud Private Relay", "VPN DNS", "IPv6 DNS", "router DHCP DNS", "Resolve-DnsName", "DNS সমস্যা সমাধান", "DNS filter test", "NextDNS সমস্যা সমাধান", "AdGuard DNS সমস্যা সমাধান"]
cover: "/img/cover/dns-filtering-bypass-troubleshooting.webp"
coverAlt: "ল্যাপটপের নীল DNS পথটি filter পেরিয়ে block চিহ্নে থেমে যায়, আর কমলা browser পথটি অন্য resolver-এ পৌঁছায়।"
coverCaption: "Filter rule বদলানোর আগে query-র পথ অনুসরণ করুন।"
---

আপনি filtering resolver সেট করেছেন, তবু একটি ডিভাইস এমন domain-এ পৌঁছায় যা আপনার policy block করে। কারণ হতে পারে rule, ডিভাইসে Domain Name System (DNS) বরাদ্দ, browser-এর encrypted resolver, অথবা VPN। **সেটিং বদলানোর আগে পথ পরীক্ষা করুন।** Filter-এ সরাসরি query এবং ডিভাইসের স্বাভাবিক query ভিন্ন প্রশ্নের উত্তর দেয়।

<!--more-->

## মূল বিষয়

- **আগে rule দেখুন:** Filter যেন নিরাপদ test domain পায় এবং block করে তা নিশ্চিত করুন।
- **প্রতিটি স্তর অনুসরণ করুন:** Router, operating system, browser, VPN এবং mobile setting DNS routing বদলাতে পারে।
- **নতুন query ব্যবহার করুন:** নতুন hostname ও সময়কে filter-এর query log-এর সঙ্গে মেলান।
- **সীমা স্পষ্ট করুন:** দেখা একটি query একটি পথ প্রমাণ করে, সব app বা device-এর আচরণ নয়।

## শুরু করার আগে

প্রায় ২০ মিনিট রাখুন। Filtering resolver-এর query log-এ প্রবেশাধিকার, সমস্যাযুক্ত একটি device এবং router-এর DNS setting-এর নথি দরকার। উদাহরণে Windows laptop ও **Pi-hole** ব্যবহার করা হয়েছে, তবে client-ভিত্তিক query log দেয় এমন যেকোনো resolver-এর সঙ্গে এই তুলনা চলে। আগে filter-এর নির্দিষ্ট address খুঁজে নিন। Public report-এ private client address, query log বা policy rule দেবেন না।

আপনার policy-তে আগে থেকেই block হওয়া একটি **নিরাপদ test domain** বেছে নিন। বিকল্পভাবে, test profile-এ আপনার নিয়ন্ত্রণাধীন domain-এর জন্য অস্থায়ী exact deny rule যোগ করতে পারেন। Rule লিখে রাখুন এবং test শেষে সরিয়ে ফেলুন। সক্রিয় malware domain দিয়ে probe করবেন না। Blocked page উপকারী লক্ষণ, কিন্তু resolver log পথ সম্পর্কে বেশি শক্ত প্রমাণ দেয়।

| স্তর | প্রশ্ন |
|---|---|
| **Filter** | সরাসরি query কি নির্দিষ্ট resolver-এ পৌঁছে এবং rule-এর সঙ্গে মেলে? |
| **Device** | Network কোন DNS server বরাদ্দ করছে? |
| **Browser বা app** | Client কি device resolver ব্যবহার করে, নাকি আলাদা পথ? |
| **VPN বা relay** | সক্রিয় tunnel কি query-র গন্তব্য বদলায়? |

## Filter কাজ করছে তা প্রমাণ করুন

Resolver-এর query log খুলুন। বেছে নেওয়া blocked domain-টি সরাসরি filter-এ query করুন। Windows-এ PowerShell ব্যবহার করুন, এবং prompt এলে filter address ও test domain লিখুন:

```powershell
$filterAddress = Read-Host "Filtering DNS server address"
$testDomain = Read-Host "Harmless domain blocked by your test rule"
Resolve-DnsName -Name $testDomain -Server $filterAddress -Type A -DnsOnly
```

Microsoft-এর [**`Resolve-DnsName`** reference](https://learn.microsoft.com/en-us/powershell/module/dnsclient/resolve-dnsname) অনুযায়ী **`-Server`** নির্দিষ্ট resolver-এ query পাঠায়। Filter log-এ query খুঁজে response এবং মেলা rule পরীক্ষা করুন। Pi-hole-এর [query ও logging documentation](https://docs.pi-hole.net/main/pihole-command/) স্থানীয় query tool ব্যাখ্যা করে। সরাসরি query অনুমোদিত হলে bypass খোঁজার আগে rule বা client group assignment ঠিক করুন। Query filter-এ না পৌঁছালে address, service এবং network path পরীক্ষা করুন।

**এই direct test প্রমাণ করে না যে laptop স্বাভাবিকভাবে filter ব্যবহার করে।** **`-Server`** option এই query-র জন্য default resolver-কে override করে। এই পার্থক্য সাধারণ false positive ঠেকায়।

## Device path অনুসরণ করুন

আগের DNS cache entry এড়াতে নতুন hostname ব্যবহার করুন। নিচের উদাহরণে একটি query সরাসরি filter-এ এবং অন্যটি laptop-এর স্বাভাবিক resolver selection দিয়ে পাঠানো হয়। আলাদা নাম থাকায় কোন log entry কোন পথের তা বোঝা যায়। **NXDOMAIN** response মানে DNS server জানাচ্ছে hostname নেই। Random নামটি ব্যবহৃত না হলে এটি স্বাভাবিক। এখানে গুরুত্বপূর্ণ হলো query filter log-এ দেখা যাচ্ছে কি না।

```powershell
$stamp = [guid]::NewGuid().ToString("N")
Resolve-DnsName -Name "direct-${stamp}.example.com" -Server $filterAddress -Type A -DnsOnly
Resolve-DnsName -Name "default-${stamp}.example.com" -Type A -DnsOnly
```

Filter log-এ দুইটি হুবহু নাম খুঁজে সময় এবং দেখানো client লিখে রাখুন। **`direct-`** দেখা গেলেও **`default-`** না এলে laptop-এ বরাদ্দ DNS server পরীক্ষা করুন। Windows-এর **`Get-DnsClientServerAddress`** interface অনুযায়ী DNS server address দেখায়। বিচ্ছিন্ন adapter নয়, সক্রিয় Wi-Fi বা Ethernet adapter দেখুন। [Microsoft DNS client reference](https://learn.microsoft.com/en-us/powershell/module/dnsclient/get-dnsclientserveraddress) এই read-only command বর্ণনা করে।

প্রথম test-এ error দৃশ্যমান রাখুন। Error বা timeout আলাদা troubleshooting চায় এবং log entry না থাকার সমতুল্য নয়।

```powershell
Get-DnsClientServerAddress | Select-Object InterfaceAlias, AddressFamily, ServerAddresses
```

IPv4 ও IPv6 row তুলনা করুন। **DHCP** DNS server-এর মতো network setting বরাদ্দ করে। **IPv6** হলো Internet Protocol address-এর নতুন পরিবার, যা ১২৮-bit address ব্যবহার করে। IPv4 lease filter নির্দেশ করতে পারে, অথচ IPv6 router advertisement অন্য DNS server দিতে পারে। Router-এর **DHCP** ও **IPv6 DNS** advertisement পরীক্ষা করুন, এরপর সংশোধনের পর device-এর network lease renew করুন। Pi-hole-এর [post-install guide](https://docs.pi-hole.net/main/post-install/) ব্যাখ্যা করে DHCP কীভাবে client-কে Pi-hole দেয়। [Router example](https://docs.pi-hole.net/routers/fritzbox/) IPv6 DNS advertisement নিয়ে আলোচনা করে।

Log-এ **router** client হিসেবে দেখা গেলে, router হয়তো device-এর হয়ে query forward করছে। তখন filter log প্রমাণ করে router filter-এ পৌঁছেছে, কোন device query শুরু করেছে তা নয়। Client পরিচয় অনুপস্থিত তথ্য বলে ধরার আগে router-এর forwarding design নিশ্চিত করুন।

## Browser DNS পরীক্ষা করুন

Command-line query device resolver path পরীক্ষা করে। Browser এর বদলে **DNS over HTTPS (DoH)** ব্যবহার করতে পারে। Browser-এ একই blocked test domain খুলুন এবং filter log-এ মিল থাকা query দেখুন। Cached result তুলনায় সমস্যা করলে browser DNS cache clear করুন অথবা test rule-এ থাকা নতুন hostname ব্যবহার করুন।

কম্পিউটারে **Chrome**-এ **Settings > Privacy and security > Security > Use secure DNS** খুলুন। [Google Chrome help](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) বলে, automatic mode বর্তমান provider ব্যবহার করে এবং ব্যর্থ হলে unencrypted lookup-এ ফিরে যায়। নির্বাচিত custom provider একইভাবে fallback করে না। Setting বদলানোর আগে mode ও provider লিখে রাখুন।

**Firefox**-এ **Settings > Privacy & Security > DNS over HTTPS** খুলুন। [Mozilla protection-level guide](https://support.mozilla.org/en-US/kb/dns-over-https) Default, Increased, Max, Custom ও Off mode আলাদা করে। [DoH overview](https://support.mozilla.org/en-US/kb/firefox-dns-over-https) ব্যাখ্যা করে কখন browser resolver স্থানীয় DNS filter bypass করে। একটি নিয়ন্ত্রিত setting বদলের পর test করুন, তারপর পছন্দের privacy setting ফিরিয়ে দিন।

**Browser query অনুপস্থিত হলেই bypass বলবেন না।** Browser cache data পুনর্ব্যবহার করতে পারে, আগে জানা address-এ পৌঁছাতে পারে, অথবা proxy ব্যবহার করতে পারে। Query কোথায় গেছে সিদ্ধান্তের আগে নতুন নাম, মিলযুক্ত সময়সীমা ও browser resolver setting তুলনা করুন।

## Mobile এবং VPN path পরীক্ষা করুন

**Android**-এ **Settings > Network & internet > Private DNS** পরীক্ষা করুন। Provider hostname router-এর বিজ্ঞাপিত DNS থেকে আলাদা private DNS service বেছে নেয়। Google-এর [Android network settings](https://support.google.com/android/answer/9654714?hl=en) Off, Automatic এবং provider-hostname বিকল্প ব্যাখ্যা করে। নিয়ন্ত্রিত স্থানীয় ফলের জন্য Wi-Fi-তে mobile data বন্ধ রেখে test করুন, তারপর স্বাভাবিক setting ফিরিয়ে দিন।

**Apple device**-এ নেটওয়ার্কে **iCloud Private Relay** চালু কি না এবং Safari প্রত্যাশিত পথ ব্যবহার করছে কি না দেখুন। Apple জানায় [Private Relay Safari browsing এবং DNS তথ্য সুরক্ষিত রাখে](https://support.apple.com/en-gb/102602)। এর [network controls](https://support.apple.com/en-ie/102022) Private Relay-এর সঙ্গে filtering সংঘাতে এলে network অনুযায়ী কী ঘটে তা ব্যাখ্যা করে। Safari-র ফল device-এর সব app-এর জন্য ধরে নেবেন না।

**VPN** নিজস্ব DNS resolver দিতে পারে বা tunnel দিয়ে query পাঠাতে পারে। VPN যুক্ত কি না, DNS setting এবং split-tunnel policy লিখে রাখুন। Security policy অনুমতি দিলেই VPN চালু ও বন্ধ অবস্থায় একই test তুলনা করুন। ফল বদলালে path আলাদা বোঝায়। শুধু এই ফল leak বা filter defect প্রমাণ করে না।

## ফলাফল ব্যাখ্যা করুন

| প্রমাণ | পরবর্তী সম্ভাব্য পরীক্ষা |
|---|---|
| **Direct query filter log-এ নেই** | Filter address, DNS service, logging বা network reachability |
| **Direct query অনুমোদিত** | Exact deny rule, group policy বা rule priority |
| **Direct আছে, default নেই** | DHCP, device static DNS, IPv6 DNS বা VPN resolver |
| **Default আছে, browser নেই** | Browser DoH, browser cache, proxy বা relay |
| **দুইটি log হয়েছে ও block, কিন্তু site খোলে** | অন্য hostname, cached content, direct address বা app path |

Logging বন্ধ, router client-এর হয়ে forward করছে, বা test cached data ব্যবহার করছে হলে **log না থাকা অস্পষ্ট**। Firewall rule বদলানোর আগে নতুন hostname দিয়ে আবার test করুন এবং query time দেখুন। External resolver-এ সাধারণ DNS block করলেই encrypted browser বা VPN আপনার filter ব্যবহার করতে বাধ্য হয় না। Pi-hole-এর [OPNsense guide](https://docs.pi-hole.net/routers/opnsense/) external DNS block-কে ঐচ্ছিক network control হিসেবে দেখায়। Device policy এবং browser configuration আলাদা control হিসেবেই থাকে।

## ঠিক করে আবার পরীক্ষা করুন

একবারে একটি layer বদলান। DHCP বা IPv6 DNS advertisement ঠিক করুন, অনিচ্ছাকৃত static resolver সরান, browser-এ প্রত্যাশিত DNS provider বাছুন, অথবা VPN-এর DNS policy সমন্বয় করুন। একটি test ব্যর্থ হয়েছে বলে সব device-এ encryption DNS বা relay protection নীরবে দুর্বল করবেন না। Source device, interface, filter address, queried name, time, response, log client, browser mode, VPN state এবং করা পরিবর্তন লিখে রাখুন।

প্রতিটি পরিবর্তনের পর **direct**, **default** এবং **browser** test আবার চালান। প্রতিবার নতুন hostname ব্যবহার করুন। Device-এ একাধিক network profile থাকলে আলাদা করে পরীক্ষা করুন। [DNS resolver comparison](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) service বাছতে সাহায্য করে। [Browser leak test](/articles/privacy-browser-leak-test-dns-webrtc/) অন্য প্রশ্নের উত্তর দেয়: browser ও VPN configuration থেকে কোন network তথ্য বাইরে যায়। **নির্ভরযোগ্য filter ফলের জন্য যাচাইকৃত rule ও যাচাইকৃত client path দরকার।**

## পরবর্তী পদক্ষেপ

প্রতিটি নিয়ন্ত্রিত পরিবর্তনের পর direct, default ও browser test পুনরাবৃত্তি করুন। Filtering service বাছার সময় [DNS resolver comparison](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) দেখুন।
