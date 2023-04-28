---
title: "Windows 10 System-Wide Ad Blocker Script for Better Privacy and Security"
date: 2021-04-02
toc: true
draft: false
description: "Block ads, trackers, and telemetry on Windows 10 using this powerful PowerShell script that utilizes the hosts file and Windows Firewall for system-wide ad-blocking."
tags: ["Windows 10", "ad-blocker", "telemetry blocking", "PowerShell script", "system-wide ad-blocking", "privacy", "security", "EasyList", "Easy Privacy", "NoCoin Filter List", "AdGuard DNS filter", "YoYo Lists", "Peter Lowe's ad/tracking/malware servers", "Windows Firewall", "domain lists", "block Windows trackers", "block trackers", "block ads", "block tracking"]
---
```powershell
iwr -useb 'https://raw.githubusercontent.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/main/sos-system-wide-windows-ad-block.ps1' | iex
```

 ##Beschreibung: Dieses Skript blockiert telemetriebezogene Domänen über die Hosts-Datei und zugehörige IPs über die Windows-Firewall.  **Anmerkungen:** - Das Hinzufügen dieser Domänen kann bestimmte Software wie iTunes oder Skype verursachen – Es wurde berichtet, dass Einträge im Zusammenhang mit Akamai-Problemen mit Widevine DRM-Verursacher  ### Verwendete Hören Sie: - [EasyList](https://easylist.to/easylist/easylist.txt) / [JustDomains - EasyList](https://justdomains.github.io/blocklists/lists/easylist-justdomains.txt) - [Easy Privacy](https://easylist.to/easylist/easyprivacy.txt) / [JustDomains - EasyPrivacy](https://justdomains.github.io/blocklists/lists/easyprivacy-justdomains.txt) - [NoCoin-Filterliste](https://github.com/hoshsadiq/adblock-nocoin-list/) / [JustDomains - NoCoin-Filterliste](https://justdomains.github.io/blocklists/lists/nocoin-justdomains .txt) - [AdGuard DNS-Filter](https://github.com/AdguardTeam/AdguardSDNSFilter) / [JustDomains - Vereinfachter AdGuard-Domainnamenfilter](https://justdomains.github.io/blocklists/lists/adguarddns-justdomains.txt) - [YoYo-Listen](https://pgl.yoyo.org/adservers/serverlist.php) - [Anzeigen-/Tracking-/Malware-Server von Peter Lowe] (https://pgl.yoyo.org/adservers/policy.php)  ### Beispiel:  Führen Sie die neueste Version des Skripts automatisch aus: