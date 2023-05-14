---
title: "Windows 10 Script de bloqueig d'anuncis a tot el sistema per a una millor privadesa i seguretat"
date: 2021-04-02
toc: true
draft: false
description: "Bloquegeu anuncis, rastrejadors i telemetria a Windows 10 mitjançant aquest potent script de PowerShell que utilitza el fitxer hosts i el tallafoc de Windows per bloquejar anuncis a tot el sistema."
tags: ["Windows 10", "bloquejador d'anuncis", "bloqueig de telemetria", "Script de PowerShell", "bloqueig d'anuncis a tot el sistema", "privadesa", "seguretat", "EasyList", "Privadesa fàcil", "Llista de filtres NoCoin", "Filtre DNS AdGuard", "Llistes YoYo", "Servidors de programari maliciós de seguiment d'anuncis de Peter Lowe", "Firewall de Windows", "llistes de dominis", "bloquejar els seguidors de Windows", "rastrejadors de blocs", "bloquejar anuncis", "seguiment de blocs"]
---

## Descripció:
Aquest script bloqueja els dominis relacionats amb la telemetria mitjançant el fitxer hosts i les IP relacionades mitjançant el tallafoc de Windows.

**Notes:**
- Afegir aquests dominis pot trencar cert programari com iTunes o Skype
- S'ha informat que les entrades relacionades amb Akamai causen problemes amb Widevine DRM

### Llistes utilitzades:
-[EasyList](https://easylist.to/easylist/easylist.txt) / [JustDomains - EasyList](https://justdomains.github.io/blocklists/lists/easylist-justdomains.txt)
-[Easy Privacy](https://easylist.to/easylist/easyprivacy.txt) / [JustDomains - EasyPrivacy](https://justdomains.github.io/blocklists/lists/easyprivacy-justdomains.txt)
-[NoCoin Filter List](https://github.com/hoshsadiq/adblock-nocoin-list/) / [JustDomains - NoCoin Filter List](https://justdomains.github.io/blocklists/lists/nocoin-justdomains.txt)
-[AdGuard DNS filter](https://github.com/AdguardTeam/AdguardSDNSFilter) / [JustDomains - AdGuard Simplified Domain Names Filter](https://justdomains.github.io/blocklists/lists/adguarddns-justdomains.txt)
-[YoYo Lists](https://pgl.yoyo.org/adservers/serverlist.php)
-[Peter Lowe’s ad/tracking/malware servers](https://pgl.yoyo.org/adservers/policy.php)

### Exemple:

Executeu la darrera versió de l'script automàticament:
```powershell
iwr -useb 'https://raw.githubusercontent.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/main/sos-system-wide-windows-ad-block.ps1' | iex
```
