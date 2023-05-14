---
title: "Windows 10-systeemwijde advertentieblokkeringsscript voor betere privacy en beveiliging"
date: 2021-04-02
toc: true
draft: false
description: "Blokkeer advertenties, trackers en telemetrie op Windows 10 met dit krachtige PowerShell-script dat gebruikmaakt van het hosts-bestand en de Windows Firewall voor systeembrede advertentieblokkering."
tags: ["Windows 10", "ad-blocker", "telemetrie blokkering", "PowerShell script", "systeemwijde advertentieblokkering", "privacy", "beveiliging", "EasyList", "Eenvoudige privacy", "NoCoin Filterlijst", "AdGuard DNS filter", "YoYo lijsten", "Peter Lowe's ad tracking malware servers", "Windows Firewall", "domeinenlijsten", "Windows trackers blokkeren", "bloktrackers", "advertenties blokkeren", "blok volgen"]
---

## Beschrijving:
Dit script blokkeert Telemetry-gerelateerde domeinen via het hosts-bestand en gerelateerde IP's via Windows Firewall.

**Noten:**
- Het toevoegen van deze domeinen kan bepaalde software zoals iTunes of Skype verstoren
- Entries gerelateerd aan Akamai veroorzaken problemen met Widevine DRM.

### Gebruikte lijsten:
-[EasyList](https://easylist.to/easylist/easylist.txt) / [JustDomains - EasyList](https://justdomains.github.io/blocklists/lists/easylist-justdomains.txt)
-[Easy Privacy](https://easylist.to/easylist/easyprivacy.txt) / [JustDomains - EasyPrivacy](https://justdomains.github.io/blocklists/lists/easyprivacy-justdomains.txt)
-[NoCoin Filter List](https://github.com/hoshsadiq/adblock-nocoin-list/) / [JustDomains - NoCoin Filter List](https://justdomains.github.io/blocklists/lists/nocoin-justdomains.txt)
-[AdGuard DNS filter](https://github.com/AdguardTeam/AdguardSDNSFilter) / [JustDomains - AdGuard Simplified Domain Names Filter](https://justdomains.github.io/blocklists/lists/adguarddns-justdomains.txt)
-[YoYo Lists](https://pgl.yoyo.org/adservers/serverlist.php)
-[Peter Lowe’s ad/tracking/malware servers](https://pgl.yoyo.org/adservers/policy.php)

### Voorbeeld:

Voer de laatste versie van het script automatisch uit:
```powershell
iwr -useb 'https://raw.githubusercontent.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/main/sos-system-wide-windows-ad-block.ps1' | iex
```
