---
title: "DNS filter ਨੂੰ ਕਿਉਂ ਬਾਈਪਾਸ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ: resolver ਦਾ ਰਸਤਾ ਜਾਂਚੋ"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "ਪਤਾ ਕਰੋ ਕਿ ਕੋਈ device ਜਾਂ browser ਤੁਹਾਡੇ DNS filter ਨੂੰ ਕਿਉਂ ਛੱਡ ਰਿਹਾ ਹੈ। ਸਿੱਧੀਆਂ ਅਤੇ ਆਮ queries ਦੀ ਤੁਲਨਾ ਕਰੋ, logs ਵੇਖੋ, ਫਿਰ encrypted DNS, VPN, IPv6 ਅਤੇ router settings ਜਾਂਚੋ।"
genre: ["ਘਰੇਲੂ ਨੈੱਟਵਰਕ", "DNS", "ਪਰਦੇਦਾਰੀ"]
tags: ["DNS filter bypass", "Pi-hole bypass", "DNS query log", "browser secure DNS", "DNS over HTTPS", "Android Private DNS", "iCloud Private Relay", "VPN DNS", "IPv6 DNS", "router DHCP DNS", "Resolve-DnsName", "DNS ਸਮੱਸਿਆ ਹੱਲ", "DNS filter ਜਾਂਚ", "NextDNS ਸਮੱਸਿਆ ਹੱਲ", "AdGuard DNS ਸਮੱਸਿਆ ਹੱਲ"]
cover: "/img/cover/dns-filtering-bypass-troubleshooting.webp"
coverAlt: "ਲੈਪਟਾਪ ਦਾ ਨੀਲਾ DNS ਰਸਤਾ filter ਵਿੱਚੋਂ ਲੰਘ ਕੇ ਰੋਕ ਦੇ ਨਿਸ਼ਾਨ ਕੋਲ ਰੁਕਦਾ ਹੈ, ਜਦਕਿ browser ਦਾ ਸੰਤਰੀ ਰਸਤਾ ਹੋਰ resolver ਤੱਕ ਪਹੁੰਚਦਾ ਹੈ।"
coverCaption: "Filter rule ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ query ਦਾ ਰਸਤਾ ਪਤਾ ਕਰੋ।"
---

ਤੁਸੀਂ filtering resolver ਸੈੱਟ ਕੀਤਾ ਹੈ, ਫਿਰ ਵੀ ਇੱਕ device ਉਸ domain ਤੱਕ ਪਹੁੰਚਦਾ ਹੈ ਜਿਸ ਨੂੰ ਤੁਹਾਡੀ policy ਰੋਕਦੀ ਹੈ। ਕਾਰਨ rule, device ਨੂੰ ਦਿੱਤਾ Domain Name System (DNS), browser ਦਾ encrypted resolver ਜਾਂ VPN ਹੋ ਸਕਦਾ ਹੈ। **Settings ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ ਰਸਤਾ ਜਾਂਚੋ।** Filter ਵੱਲ ਸਿੱਧੀ query ਅਤੇ device ਦੀ ਆਮ query ਵੱਖਰੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਦਿੰਦੀਆਂ ਹਨ।

<!--more-->

## ਮੁੱਖ ਗੱਲਾਂ

- **ਪਹਿਲਾਂ rule ਜਾਂਚੋ:** ਪੱਕਾ ਕਰੋ ਕਿ filter ਇੱਕ ਸੁਰੱਖਿਅਤ test domain ਲੈਂਦਾ ਅਤੇ ਰੋਕਦਾ ਹੈ।
- **ਹਰ ਪਰਤ ਦਾ ਪਤਾ ਲਗਾਓ:** Router, operating system, browser, VPN ਅਤੇ mobile settings DNS routing ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦੀਆਂ ਹਨ।
- **ਨਵੀਆਂ queries ਵਰਤੋ:** ਨਵੇਂ hostname ਅਤੇ ਸਮੇਂ ਨੂੰ filter ਦੇ query log ਨਾਲ ਮਿਲਾਓ।
- **ਹੱਦ ਸਪਸ਼ਟ ਕਰੋ:** ਵੇਖੀ ਗਈ ਇੱਕ query ਇੱਕ ਰਸਤੇ ਦਾ ਸਬੂਤ ਹੈ, ਹਰ app ਜਾਂ device ਦੇ ਵਰਤਾਰੇ ਦਾ ਨਹੀਂ।

## ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

ਲਗਭਗ 20 ਮਿੰਟ ਰੱਖੋ। ਤੁਹਾਨੂੰ filtering resolver ਦੇ query log ਤੱਕ ਪਹੁੰਚ, ਸਮੱਸਿਆ ਵਾਲਾ ਇੱਕ device ਅਤੇ router ਦੀ DNS settings ਦਾ ਰਿਕਾਰਡ ਚਾਹੀਦਾ ਹੈ। ਉਦਾਹਰਨਾਂ Windows laptop ਅਤੇ **Pi-hole** ਵਰਤਦੀਆਂ ਹਨ, ਪਰ client ਅਨੁਸਾਰ query logs ਦੇਣ ਵਾਲੇ ਕਿਸੇ ਵੀ resolver ਨਾਲ ਇਹ ਤੁਲਨਾ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ। ਪਹਿਲਾਂ filter ਦਾ ਸਹੀ address ਪਛਾਣੋ। ਜਨਤਕ ਰਿਪੋਰਟ ਵਿੱਚ private client addresses, query logs ਜਾਂ policy rules ਨਾ ਪਾਓ।

ਇੱਕ **ਨੁਕਸਾਨ-ਰਹਿਤ test domain** ਚੁਣੋ ਜਿਸ ਨੂੰ ਤੁਹਾਡੀ policy ਪਹਿਲਾਂ ਹੀ block ਕਰਦੀ ਹੈ। ਦੂਜਾ ਤਰੀਕਾ ਇਹ ਹੈ ਕਿ test profile ਵਿੱਚ ਤੁਹਾਡੇ ਕਾਬੂ ਵਾਲੇ domain ਲਈ ਕੁਝ ਸਮੇਂ ਵਾਸਤੇ exact deny rule ਜੋੜੋ। Rule ਲਿਖ ਲਵੋ ਅਤੇ test ਮਗਰੋਂ ਹਟਾ ਦਿਓ। ਚੱਲ ਰਹੇ malware domain ਨੂੰ probe ਵਜੋਂ ਨਾ ਵਰਤੋ। Blocked page ਇੱਕ ਕੰਮ ਦਾ ਲੱਛਣ ਹੈ, ਪਰ resolver log ਰਸਤੇ ਬਾਰੇ ਵਧੇਰੇ ਮਜ਼ਬੂਤ ਸਬੂਤ ਦਿੰਦਾ ਹੈ।

| ਪਰਤ | ਸਵਾਲ |
|---|---|
| **Filter** | ਕੀ ਸਿੱਧੀ query ਮਨਚਾਹੇ resolver ਤੱਕ ਪਹੁੰਚਦੀ ਅਤੇ rule ਨਾਲ ਮਿਲਦੀ ਹੈ? |
| **Device** | Network ਕਿਹੜੇ DNS servers ਦਿੰਦਾ ਹੈ? |
| **Browser ਜਾਂ app** | ਕੀ ਇਹ client device resolver ਵਰਤਦਾ ਹੈ ਜਾਂ ਵੱਖਰਾ ਰਸਤਾ? |
| **VPN ਜਾਂ relay** | ਕੀ ਚੱਲਦਾ tunnel queries ਦੀ ਮੰਜ਼ਿਲ ਬਦਲਦਾ ਹੈ? |

## Filter ਦੇ ਕੰਮ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ

Resolver ਦਾ query log ਖੋਲ੍ਹੋ। ਚੁਣੇ ਹੋਏ blocked domain ਨੂੰ ਸਿੱਧਾ filter ਉੱਤੇ query ਕਰੋ। Windows ਵਿੱਚ PowerShell ਵਰਤੋ ਅਤੇ ਪੁੱਛਣ ਉੱਤੇ filter address ਅਤੇ test domain ਦਿਓ:

```powershell
$filterAddress = Read-Host "Filtering DNS server address"
$testDomain = Read-Host "Harmless domain blocked by your test rule"
Resolve-DnsName -Name $testDomain -Server $filterAddress -Type A -DnsOnly
```

Microsoft ਦੀ [**`Resolve-DnsName`** reference](https://learn.microsoft.com/en-us/powershell/module/dnsclient/resolve-dnsname) **`-Server`** ਨੂੰ ਦੱਸੇ resolver ਵੱਲ query ਵਜੋਂ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੀ ਹੈ। Filter log ਵਿੱਚ query ਲੱਭੋ ਅਤੇ response ਤੇ ਮਿਲਦੇ rule ਨੂੰ ਜਾਂਚੋ। Pi-hole ਦੀ [queries ਅਤੇ logging ਬਾਰੇ documentation](https://docs.pi-hole.net/main/pihole-command/) ਸਥਾਨਕ query tools ਦੱਸਦੀ ਹੈ। ਜੇ ਸਿੱਧੀ query ਮਨਜ਼ੂਰ ਹੋਵੇ, ਤਾਂ bypass ਦੀ ਜਾਂਚ ਤੋਂ ਪਹਿਲਾਂ rule ਜਾਂ client group assignment ਠੀਕ ਕਰੋ। ਜੇ query filter ਤੱਕ ਨਹੀਂ ਪਹੁੰਚਦੀ, ਤਾਂ address, service ਅਤੇ network path ਜਾਂਚੋ।

**ਇਹ ਸਿੱਧੀ ਜਾਂਚ ਇਹ ਸਾਬਤ ਨਹੀਂ ਕਰਦੀ ਕਿ laptop ਆਮ ਤੌਰ ਉੱਤੇ filter ਵਰਤਦਾ ਹੈ।** **`-Server`** option ਇਸ query ਲਈ default resolver ਨੂੰ ਬਦਲ ਦਿੰਦਾ ਹੈ। ਇਹ ਫਰਕ ਆਮ false positive ਤੋਂ ਬਚਾਉਂਦਾ ਹੈ।

## Device ਦਾ ਰਸਤਾ ਪਤਾ ਕਰੋ

ਪੁਰਾਣੀ DNS cache entry ਤੋਂ ਬਚਣ ਲਈ ਨਵਾਂ hostname ਵਰਤੋ। ਅਗਲੀ ਉਦਾਹਰਨ ਇੱਕ query ਸਿੱਧੀ filter ਵੱਲ ਅਤੇ ਦੂਜੀ laptop ਦੀ ਆਮ resolver ਚੋਣ ਰਾਹੀਂ ਭੇਜਦੀ ਹੈ। ਨਾਂ ਵੱਖਰੇ ਹਨ, ਇਸ ਲਈ ਤੁਸੀਂ ਹਰ ਰਸਤੇ ਦੀ log entry ਪਛਾਣ ਸਕਦੇ ਹੋ। **NXDOMAIN** response ਦਾ ਮਤਲਬ ਹੈ DNS server ਕਹਿੰਦਾ ਹੈ ਕਿ hostname ਮੌਜੂਦ ਨਹੀਂ। ਜੇ random ਨਾਂ ਵਰਤਿਆ ਨਹੀਂ ਜਾਂਦਾ ਤਾਂ ਇਹ ਆਮ ਗੱਲ ਹੈ। ਇੱਥੇ ਅਹਿਮ ਗੱਲ ਇਹ ਹੈ ਕਿ query filter log ਵਿੱਚ ਆਉਂਦੀ ਹੈ ਜਾਂ ਨਹੀਂ।

```powershell
$stamp = [guid]::NewGuid().ToString("N")
Resolve-DnsName -Name "direct-${stamp}.example.com" -Server $filterAddress -Type A -DnsOnly
Resolve-DnsName -Name "default-${stamp}.example.com" -Type A -DnsOnly
```

Filter log ਵਿੱਚ ਦੋਵੇਂ ਸਹੀ ਨਾਂ ਲੱਭੋ ਅਤੇ ਸਮਾਂ ਤੇ ਦਿਖਾਇਆ client ਲਿਖੋ। ਜੇ **`direct-`** ਆਉਂਦਾ ਹੈ ਪਰ **`default-`** ਨਹੀਂ, ਤਾਂ laptop ਨੂੰ ਦਿੱਤੇ DNS servers ਵੇਖੋ। Windows ਦਾ **`Get-DnsClientServerAddress`** ਹਰ interface ਲਈ DNS server addresses ਦਿਖਾਉਂਦਾ ਹੈ। ਚੱਲਦਾ Wi-Fi ਜਾਂ Ethernet adapter ਜਾਂਚੋ, disconnected adapter ਨਹੀਂ। [Microsoft DNS client reference](https://learn.microsoft.com/en-us/powershell/module/dnsclient/get-dnsclientserveraddress) ਇਹ read-only command ਸਮਝਾਉਂਦੀ ਹੈ।

ਪਹਿਲੀ ਜਾਂਚ ਦੌਰਾਨ errors ਦਿਖਣ ਦਿਓ। Error ਜਾਂ timeout ਵੱਖਰੀ diagnosis ਮੰਗਦਾ ਹੈ ਅਤੇ log entry ਨਾ ਹੋਣ ਵਰਗਾ ਨਹੀਂ ਹੈ।

```powershell
Get-DnsClientServerAddress | Select-Object InterfaceAlias, AddressFamily, ServerAddresses
```

IPv4 ਅਤੇ IPv6 ਦੀਆਂ rows ਦੀ ਤੁਲਨਾ ਕਰੋ। **DHCP** DNS servers ਵਰਗੀਆਂ network settings ਦਿੰਦਾ ਹੈ। **IPv6** Internet Protocol ਦਾ ਨਵਾਂ address family ਹੈ ਅਤੇ 128-bit addresses ਵਰਤਦਾ ਹੈ। IPv4 lease filter ਦੱਸ ਸਕਦੀ ਹੈ, ਜਦਕਿ IPv6 router advertisements ਹੋਰ DNS server ਦੇ ਸਕਦੀਆਂ ਹਨ। Router ਦੀਆਂ **DHCP** ਅਤੇ **IPv6 DNS** advertisements ਜਾਂਚੋ, ਫਿਰ ਸੁਧਾਰ ਮਗਰੋਂ device ਦੀ network lease renew ਕਰੋ। Pi-hole ਦੀ [post-install guide](https://docs.pi-hole.net/main/post-install/) ਦੱਸਦੀ ਹੈ ਕਿ DHCP clients ਨੂੰ Pi-hole ਵੱਲ ਕਿਵੇਂ ਭੇਜਦਾ ਹੈ। [Router example](https://docs.pi-hole.net/routers/fritzbox/) IPv6 DNS advertisements ਬਾਰੇ ਹੈ।

ਜੇ log ਵਿੱਚ **router** client ਵਜੋਂ ਦਿਖੇ, ਤਾਂ router devices ਦੀ ਥਾਂ queries ਅੱਗੇ ਭੇਜ ਰਿਹਾ ਹੋ ਸਕਦਾ ਹੈ। Filter log ਫਿਰ ਸਿਰਫ ਇਹ ਸਾਬਤ ਕਰਦਾ ਹੈ ਕਿ router filter ਤੱਕ ਪਹੁੰਚਿਆ, ਇਹ ਨਹੀਂ ਕਿ ਕਿਹੜੇ device ਨੇ query ਸ਼ੁਰੂ ਕੀਤੀ। Client ਦੀ ਪਛਾਣ ਨੂੰ ਗੁੰਮ ਡਾਟਾ ਮੰਨਣ ਤੋਂ ਪਹਿਲਾਂ router ਦਾ forwarding design ਪੱਕਾ ਕਰੋ।

## Browser DNS ਜਾਂਚੋ

Command-line query device resolver path ਦੀ ਜਾਂਚ ਕਰਦੀ ਹੈ। Browser ਇਸ ਦੀ ਥਾਂ **DNS over HTTPS (DoH)** ਵਰਤ ਸਕਦਾ ਹੈ। Browser ਵਿੱਚ ਉਹੀ blocked test domain ਖੋਲ੍ਹੋ ਅਤੇ filter log ਵਿੱਚ ਮਿਲਦੀ query ਵੇਖੋ। ਜੇ cached results ਤੁਲਨਾ ਰੋਕਣ ਤਾਂ browser DNS cache ਸਾਫ਼ ਕਰੋ ਜਾਂ test rule ਹੇਠ ਨਵਾਂ hostname ਵਰਤੋ।

ਕੰਪਿਊਟਰ ਉੱਤੇ **Chrome** ਵਿੱਚ **Settings > Privacy and security > Security > Use secure DNS** ਖੋਲ੍ਹੋ। [Google Chrome help](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) ਦੱਸਦੀ ਹੈ ਕਿ automatic mode ਮੌਜੂਦਾ provider ਵਰਤਦਾ ਹੈ ਅਤੇ ਨਾਕਾਮੀ ਉੱਤੇ unencrypted lookup ਵੱਲ ਮੁੜਦਾ ਹੈ। ਚੁਣਿਆ custom provider ਇਸੇ ਤਰ੍ਹਾਂ ਵਾਪਸ ਨਹੀਂ ਮੁੜਦਾ। Setting ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ mode ਅਤੇ provider ਲਿਖੋ।

**Firefox** ਵਿੱਚ **Settings > Privacy & Security > DNS over HTTPS** ਖੋਲ੍ਹੋ। [Mozilla protection-level guide](https://support.mozilla.org/en-US/kb/dns-over-https) Default, Increased, Max, Custom ਅਤੇ Off modes ਵਿੱਚ ਫਰਕ ਦੱਸਦੀ ਹੈ। [DoH overview](https://support.mozilla.org/en-US/kb/firefox-dns-over-https) ਸਮਝਾਉਂਦੀ ਹੈ ਕਿ browser resolver ਕਦੋਂ ਸਥਾਨਕ DNS filter bypass ਕਰਦਾ ਹੈ। ਇੱਕ ਨਿਯੰਤਰਿਤ ਤਬਦੀਲੀ ਮਗਰੋਂ ਮੁੜ test ਕਰੋ, ਫਿਰ ਆਪਣੀ ਚਾਹੀਦੀ privacy setting ਵਾਪਸ ਲਿਆਓ।

**Browser ਦੀ ਹਰ ਗੁੰਮ query ਨੂੰ bypass ਨਾ ਕਹੋ।** Browser cache data ਮੁੜ ਵਰਤ ਸਕਦਾ ਹੈ, ਪਹਿਲਾਂ ਪਤਾ address ਤੱਕ ਜਾ ਸਕਦਾ ਹੈ ਜਾਂ proxy ਵਰਤ ਸਕਦਾ ਹੈ। Query ਕਿੱਥੇ ਗਈ ਇਹ ਫੈਸਲਾ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਨਵਾਂ ਨਾਂ, ਮਿਲਦਾ ਸਮਾਂ ਅਤੇ browser resolver setting ਦੀ ਤੁਲਨਾ ਕਰੋ।

## Mobile ਅਤੇ VPN ਰਸਤੇ ਜਾਂਚੋ

**Android** ਉੱਤੇ **Settings > Network & internet > Private DNS** ਵੇਖੋ। Provider hostname ਇੱਕ private DNS service ਚੁਣਦਾ ਹੈ ਜੋ router ਵੱਲੋਂ ਦੱਸੇ DNS ਤੋਂ ਵੱਖਰੀ ਹੈ। Google ਦੀਆਂ [Android network settings](https://support.google.com/android/answer/9654714?hl=en) Off, Automatic ਅਤੇ provider-hostname ਚੋਣਾਂ ਦੱਸਦੀਆਂ ਹਨ। ਨਿਯੰਤਰਿਤ ਸਥਾਨਕ ਨਤੀਜੇ ਲਈ Wi-Fi ਉੱਤੇ mobile data ਬੰਦ ਕਰਕੇ test ਕਰੋ, ਫਿਰ ਆਮ setting ਵਾਪਸ ਕਰੋ।

**Apple devices** ਉੱਤੇ ਜਾਂਚੋ ਕਿ network ਲਈ **iCloud Private Relay** ਚੱਲ ਰਿਹਾ ਹੈ ਅਤੇ Safari ਉਮੀਦ ਕੀਤਾ ਰਸਤਾ ਵਰਤਦਾ ਹੈ। Apple ਕਹਿੰਦਾ ਹੈ [Private Relay Safari browsing ਅਤੇ DNS ਜਾਣਕਾਰੀ ਦੀ ਰੱਖਿਆ ਕਰਦਾ ਹੈ](https://support.apple.com/en-gb/102602)। ਇਸ ਦੇ [network controls](https://support.apple.com/en-ie/102022) ਦੱਸਦੇ ਹਨ ਕਿ filtering ਅਤੇ Private Relay ਟਕਰਾਉਣ ਉੱਤੇ ਹਰ network ਲਈ ਕੀ ਹੁੰਦਾ ਹੈ। Safari ਦੇ ਨਤੀਜੇ ਨੂੰ device ਦੀਆਂ ਸਾਰੀਆਂ apps ਉੱਤੇ ਲਾਗੂ ਨਾ ਕਰੋ।

**VPN** ਆਪਣਾ DNS resolver ਦੇ ਸਕਦਾ ਹੈ ਜਾਂ queries ਨੂੰ tunnel ਰਾਹੀਂ ਭੇਜ ਸਕਦਾ ਹੈ। ਲਿਖੋ ਕਿ VPN ਜੁੜਿਆ ਹੈ ਜਾਂ ਨਹੀਂ, ਉਸ ਦੀ DNS setting ਕੀ ਹੈ ਅਤੇ split-tunnel policy ਕੀ ਹੈ। Security policy ਇਜਾਜ਼ਤ ਦੇਵੇ ਤਾਂ ਹੀ VPN ਚਾਲੂ ਅਤੇ ਬੰਦ ਕਰਕੇ ਉਹੀ test ਤੁਲਨਾ ਕਰੋ। ਨਤੀਜਾ ਬਦਲਣਾ ਵੱਖਰੇ ਰਸਤੇ ਦਾ ਸੰਕੇਤ ਹੈ। ਇਸ ਨਾਲ ਇਕੱਲੇ leak ਜਾਂ filter ਖ਼ਰਾਬੀ ਸਾਬਤ ਨਹੀਂ ਹੁੰਦੀ।

## ਨਤੀਜੇ ਸਮਝੋ

| ਸਬੂਤ | ਅਗਲੀ ਸੰਭਾਵੀ ਜਾਂਚ |
|---|---|
| **ਸਿੱਧੀ query filter log ਵਿੱਚ ਨਹੀਂ** | Filter address, DNS service, logging ਜਾਂ network ਪਹੁੰਚ |
| **ਸਿੱਧੀ query ਮਨਜ਼ੂਰ ਹੋਈ** | Exact deny rule, group policy ਜਾਂ rule priority |
| **ਸਿੱਧੀ ਦਰਜ, ਆਮ query ਗੁੰਮ** | DHCP, device static DNS, IPv6 DNS ਜਾਂ VPN resolver |
| **ਆਮ ਦਰਜ, browser query ਗੁੰਮ** | Browser DoH, browser cache, proxy ਜਾਂ relay |
| **ਦੋਵੇਂ ਦਰਜ ਅਤੇ block, ਪਰ site ਖੁੱਲ੍ਹਦੀ ਹੈ** | ਹੋਰ hostname, cached content, direct address ਜਾਂ app path |

ਜੇ logging ਬੰਦ ਹੈ, router client ਦੀ ਥਾਂ forward ਕਰਦਾ ਹੈ ਜਾਂ test cached data ਦੁਬਾਰਾ ਵਰਤਦਾ ਹੈ, ਤਾਂ **log entries ਨਾ ਹੋਣ ਦਾ ਅਰਥ ਸਪਸ਼ਟ ਨਹੀਂ ਹੁੰਦਾ**। Firewall rules ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ ਨਵੇਂ hostname ਨਾਲ ਦੁਬਾਰਾ test ਕਰੋ ਅਤੇ query time ਵੇਖੋ। ਬਾਹਰੀ resolvers ਵੱਲ ਆਮ DNS ਰੋਕਣ ਨਾਲ encrypted browser ਜਾਂ VPN ਤੁਹਾਡਾ filter ਵਰਤਣ ਲਈ ਮਜਬੂਰ ਨਹੀਂ ਹੁੰਦਾ। Pi-hole ਦੀ [OPNsense guide](https://docs.pi-hole.net/routers/opnsense/) external-DNS blocking ਨੂੰ ਚੋਣਵਾਂ network control ਦੱਸਦੀ ਹੈ। Device policy ਅਤੇ browser configuration ਵੱਖਰੇ controls ਰਹਿੰਦੇ ਹਨ।

## ਸੁਧਾਰੋ ਅਤੇ ਫਿਰ test ਕਰੋ

ਇੱਕ ਵਾਰ ਵਿੱਚ ਇੱਕ layer ਬਦਲੋ। DHCP ਜਾਂ IPv6 DNS advertisements ਠੀਕ ਕਰੋ, ਅਣਚਾਹਾ static resolver ਹਟਾਓ, browser ਵਿੱਚ ਚਾਹੀਦਾ DNS provider ਚੁਣੋ ਜਾਂ VPN ਦੀ DNS policy ਬਦਲੋ। ਇੱਕ test ਨਾਕਾਮ ਹੋਣ ਕਰਕੇ ਸਾਰੇ devices ਉੱਤੇ encrypted DNS ਜਾਂ relay protection ਚੁੱਪਚਾਪ ਕਮਜ਼ੋਰ ਨਾ ਕਰੋ। Source device, interface, filter address, queried name, time, response, log client, browser mode, VPN state ਅਤੇ ਕੀਤਾ ਬਦਲਾਅ ਲਿਖੋ।

ਹਰ ਬਦਲਾਅ ਮਗਰੋਂ **direct**, **default** ਅਤੇ **browser** tests ਦੁਬਾਰਾ ਚਲਾਓ। ਹਰ ਵਾਰ ਨਵਾਂ hostname ਵਰਤੋ। ਜੇ device ਦੇ ਕਈ network profiles ਹਨ ਤਾਂ ਹਰ ਇੱਕ ਵੱਖਰਾ ਜਾਂਚੋ। [DNS resolver comparison](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) service ਚੁਣਨ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ। [Browser leak test](/articles/privacy-browser-leak-test-dns-webrtc/) ਹੋਰ ਸਵਾਲ ਦਾ ਜਵਾਬ ਦਿੰਦਾ ਹੈ: browser ਅਤੇ VPN configuration ਵਿੱਚੋਂ ਕਿਹੜੀ network ਜਾਣਕਾਰੀ ਬਾਹਰ ਜਾਂਦੀ ਹੈ। **ਭਰੋਸੇਯੋਗ filter ਨਤੀਜੇ ਲਈ ਜਾਂਚਿਆ rule ਅਤੇ ਜਾਂਚਿਆ client path ਲੋੜੀਂਦੇ ਹਨ।**

## ਅਗਲੇ ਕਦਮ

ਹਰ ਨਿਯੰਤਰਿਤ ਤਬਦੀਲੀ ਮਗਰੋਂ direct, default ਅਤੇ browser tests ਦੁਹਰਾਓ। Filtering service ਚੁਣਦੇ ਸਮੇਂ [DNS resolver comparison](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) ਵੇਖੋ।
