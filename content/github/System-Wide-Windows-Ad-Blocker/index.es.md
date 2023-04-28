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

 ## Descripción: Este script bloquea los dominios relacionados con la telemetría a través del archivo de hosts y las direcciones IP relacionadas a través del Firewall de Windows.  **Notas:** - Agregar ciertos dominios puede dañar programas como iTunes o Skype - Se ha informado que las entradas relacionadas con Akamai causan problemas con Widevine DRM  ### Listas usadas: - [EasyList](https://easylist.to/easylist/easylist.txt) / [JustDomains - EasyList](https://justdomains.github.io/blocklists/lists/easylist-justdomains.txt) - [Privacidad fácil](https://easylist.to/easylist/easyprivacy.txt) / [JustDomains - EasyPrivacy](https://justdomains.github.io/blocklists/lists/easyprivacy-justdomains.txt) - [Lista de filtros NoCoin](https://github.com/hoshsadiq/adblock-nocoin-list/) / [JustDomains - Lista de filtros NoCoin](https://justdomains.github.io/blocklists/lists/nocoin -solo dominios .TXT) - [Filtro de DNS de AdGuard](https://github.com/AdguardTeam/AdguardSDNSFilter) / [JustDomains - Filtro de nombres de dominio simplificado de AdGuard](https://justdomains.github.io/blocklists/lists/adguarddns -solodominios.txt) - [Listas de YoYo](https://pgl.yoyo.org/adservers/serverlist.php) - [Servidores de publicidad/seguimiento/malware de Peter Lowe](https://pgl.yoyo.org/adservers/policy.php)  ### Ejemplo:  Ejecute la última versión del script automáticamente: