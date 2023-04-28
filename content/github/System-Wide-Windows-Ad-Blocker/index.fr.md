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

 ## Description: Ce script bloque les domaines liés à la télémétrie via le fichier hosts et les adresses IP associées via le pare-feu Windows.  **Remarques :** - L'ajout de ces domaines peut casser certains logiciels comme iTunes ou Skype - Des entrées liées à Akamai ont été signalées comme causant des problèmes avec Widevine DRM  ### Listes utilisées : - [EasyList](https://easylist.to/easylist/easylist.txt) / [JustDomains - EasyList](https://justdomains.github.io/blocklists/lists/easylist-justdomains.txt) - [Confidentialité facile](https://easylist.to/easylist/easyprivacy.txt) / [JustDomains - EasyPrivacy](https://justdomains.github.io/blocklists/lists/easyprivacy-justdomains.txt) - [Liste des filtres NoCoin](https://github.com/hoshsadiq/adblock-nocoin-list/) / [JustDomains - Liste des filtres NoCoin](https://justdomains.github.io/blocklists/lists/nocoin -justdomains .SMS) - [Filtre DNS AdGuard](https://github.com/AdguardTeam/AdguardSDNSFilter) / [JustDomains - Filtre de noms de domaine simplifié AdGuard](https://justdomains.github.io/blocklists/lists/adguarddns-justdomains. SMS) - [Listes YoYo] (https://pgl.yoyo.org/adservers/serverlist.php) - [Serveurs publicitaires/de suivi/malwares de Peter Lowe](https://pgl.yoyo.org/adservers/policy.php)  ### Exemple :  Exécutez automatiquement la dernière version du script :