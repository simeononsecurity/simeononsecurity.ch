---
title: "Script di blocco degli annunci a livello di sistema di Windows 10 per una migliore privacy e sicurezza"
date: 2021-04-02
toc: true
draft: false
description: "Blocca annunci, tracker e telemetria su Windows 10 utilizzando questo potente script di PowerShell che utilizza il file hosts e Windows Firewall per il blocco degli annunci a livello di sistema."
tags: ["Windows 10", "blocco per annunci pubblicitari", "blocco della telemetria", "Script di PowerShell", "blocco degli annunci a livello di sistema", "intimità", "sicurezza", "EasyList", "Segretezza facile", "Elenco dei filtri NoCoin", "Filtro DNS di AdGuard", "Liste YoYo", "I server del malware di tracciamento degli annunci di Peter Lowe", "firewall di Windows", "elenchi di domini", "bloccare i tracker di Windows", "tracker di blocco", "bloccare gli annunci", "tracciamento dei blocchi"]
---

## Descrizione:
Questo script blocca i domini correlati alla telemetria tramite il file hosts e gli IP correlati tramite Windows Firewall.

**Appunti:**
- L'aggiunta di questi domini potrebbe danneggiare alcuni software come iTunes o Skype
- È stato segnalato che le voci relative ad Akamai causano problemi con Widevine DRM

### Elenchi utilizzati:
-[EasyList](https://easylist.to/easylist/easylist.txt) / [JustDomains - EasyList](https://justdomains.github.io/blocklists/lists/easylist-justdomains.txt)
-[Easy Privacy](https://easylist.to/easylist/easyprivacy.txt) / [JustDomains - EasyPrivacy](https://justdomains.github.io/blocklists/lists/easyprivacy-justdomains.txt)
-[NoCoin Filter List](https://github.com/hoshsadiq/adblock-nocoin-list/) / [JustDomains - NoCoin Filter List](https://justdomains.github.io/blocklists/lists/nocoin-justdomains.txt)
-[AdGuard DNS filter](https://github.com/AdguardTeam/AdguardSDNSFilter) / [JustDomains - AdGuard Simplified Domain Names Filter](https://justdomains.github.io/blocklists/lists/adguarddns-justdomains.txt)
-[YoYo Lists](https://pgl.yoyo.org/adservers/serverlist.php)
-[Peter Lowe’s ad/tracking/malware servers](https://pgl.yoyo.org/adservers/policy.php)

### Esempio:

Esegui automaticamente l'ultima versione dello script:
```powershell
iwr -useb 'https://raw.githubusercontent.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/main/sos-system-wide-windows-ad-block.ps1' | iex
```
