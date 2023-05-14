---
title: "Windows 10 System-Wide Ad Blocker Script dla lepszej prywatności i bezpieczeństwa"
date: 2021-04-02
toc: true
draft: false
description: "Blokuj reklamy, trackery i telemetrię w systemie Windows 10 za pomocą tego potężnego skryptu PowerShell, który wykorzystuje plik hosts i zaporę systemu Windows do blokowania reklam w całym systemie."
tags: ["Windows 10", "ad-blocker", "blokowanie telemetrii", "Skrypt PowerShell", "systemowe blokowanie reklam", "prywatność", "bezpieczeństwo", "EasyList", "Łatwa prywatność", "Lista filtrów NoCoin", "Filtr DNS AdGuard", "Listy YoYo", "Peter Lowe's ad tracking malware servers", "Zapora systemu Windows", "listy domen", "zablokować trackery Windows", "tropiciele bloków", "blokować reklamy", "śledzenie bloków"]
---

## Opis:
Ten skrypt blokuje domeny związane z Telemetry poprzez plik hosts oraz powiązane IP poprzez Windows Firewall.

**Notes:**
- Dodanie tych domen może uszkodzić pewne oprogramowanie, takie jak iTunes czy Skype
- Zgłoszono, że wpisy związane z Akamai powodują problemy z Widevine DRM

### Użyte listy:
-[EasyList](https://easylist.to/easylist/easylist.txt) / [JustDomains - EasyList](https://justdomains.github.io/blocklists/lists/easylist-justdomains.txt)
-[Easy Privacy](https://easylist.to/easylist/easyprivacy.txt) / [JustDomains - EasyPrivacy](https://justdomains.github.io/blocklists/lists/easyprivacy-justdomains.txt)
-[NoCoin Filter List](https://github.com/hoshsadiq/adblock-nocoin-list/) / [JustDomains - NoCoin Filter List](https://justdomains.github.io/blocklists/lists/nocoin-justdomains.txt)
-[AdGuard DNS filter](https://github.com/AdguardTeam/AdguardSDNSFilter) / [JustDomains - AdGuard Simplified Domain Names Filter](https://justdomains.github.io/blocklists/lists/adguarddns-justdomains.txt)
-[YoYo Lists](https://pgl.yoyo.org/adservers/serverlist.php)
-[Peter Lowe’s ad/tracking/malware servers](https://pgl.yoyo.org/adservers/policy.php)

### Przykład:

Uruchom automatycznie najnowszą wersję skryptu:
```powershell
iwr -useb 'https://raw.githubusercontent.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/main/sos-system-wide-windows-ad-block.ps1' | iex
```
