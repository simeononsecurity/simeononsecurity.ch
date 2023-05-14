---
title: "Windows 10 Script de blocare a reclamelor la nivel de sistem pentru o mai bună confidențialitate și securitate"
date: 2021-04-02
toc: true
draft: false
description: "Blocați reclamele, instrumentele de urmărire și telemetria pe Windows 10 folosind acest script PowerShell puternic care utilizează fișierul hosts și Windows Firewall pentru blocarea reclamelor la nivel de sistem."
tags: ["Windows 10", "blocant de anunțuri", "blocarea telemetriei", "Script PowerShell", "blocarea reclamelor la nivelul întregului sistem", "intimitate", "Securitate", "EasyList", "Confidențialitate ușoară", "Lista de filtre NoCoin", "Filtrul DNS AdGuard", "Liste YoYo", "Serverele malware de urmărire a reclamelor lui Peter Lowe", "Windows Firewall", "liste de domenii", "blocați dispozitivele de urmărire Windows", "blocuri de urmărire", "blocați reclamele", "urmărirea blocurilor"]
---

## Descriere:
Acest script blochează domeniile legate de telemetrie prin fișierul hosts și IP-urile aferente prin Windows Firewall.

**Note:**
- Adăugarea acestor domenii poate distruge anumite programe precum iTunes sau Skype
- S-a raportat că intrările legate de Akamai cauzează probleme cu Widevine DRM

### Liste utilizate:
-[EasyList](https://easylist.to/easylist/easylist.txt) / [JustDomains - EasyList](https://justdomains.github.io/blocklists/lists/easylist-justdomains.txt)
-[Easy Privacy](https://easylist.to/easylist/easyprivacy.txt) / [JustDomains - EasyPrivacy](https://justdomains.github.io/blocklists/lists/easyprivacy-justdomains.txt)
-[NoCoin Filter List](https://github.com/hoshsadiq/adblock-nocoin-list/) / [JustDomains - NoCoin Filter List](https://justdomains.github.io/blocklists/lists/nocoin-justdomains.txt)
-[AdGuard DNS filter](https://github.com/AdguardTeam/AdguardSDNSFilter) / [JustDomains - AdGuard Simplified Domain Names Filter](https://justdomains.github.io/blocklists/lists/adguarddns-justdomains.txt)
-[YoYo Lists](https://pgl.yoyo.org/adservers/serverlist.php)
-[Peter Lowe’s ad/tracking/malware servers](https://pgl.yoyo.org/adservers/policy.php)

### Exemplu:

Rulați cea mai recentă versiune a scriptului automat:
```powershell
iwr -useb 'https://raw.githubusercontent.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/main/sos-system-wide-windows-ad-block.ps1' | iex
```
