---
title: "Script do bloqueador de anúncios em todo o sistema do Windows 10 para melhor privacidade e segurança"
date: 2021-04-02
toc: true
draft: false
description: "Bloqueie anúncios, rastreadores e telemetria no Windows 10 usando este poderoso script do PowerShell que utiliza o arquivo hosts e o Firewall do Windows para bloqueio de anúncios em todo o sistema."
tags: ["Windows 10", "bloqueador de anúncios", "bloqueio de telemetria", "script do PowerShell", "bloqueio de anúncios em todo o sistema", "privacidade", "segurança", "EasyList", "Privacidade fácil", "Lista de filtros NoCoin", "Filtro de DNS do AdGuard", "Listas de ioiô", "Servidores de malware de rastreamento de anúncios de Peter Lowe", "Firewall do Windows", "listas de domínio", "bloquear rastreadores do Windows", "bloquear rastreadores", "bloquear anúncios", "rastreamento de bloqueio"]
---

## Descrição:
Este script bloqueia domínios relacionados à telemetria por meio do arquivo hosts e IPs relacionados por meio do Firewall do Windows.

**Notas:**
- Adicionar esses domínios pode quebrar certos softwares como iTunes ou Skype
- Foi relatado que entradas relacionadas à Akamai causam problemas com Widevine DRM

### Listas usadas:
-[EasyList](https://easylist.to/easylist/easylist.txt) / [JustDomains - EasyList](https://justdomains.github.io/blocklists/lists/easylist-justdomains.txt)
-[Easy Privacy](https://easylist.to/easylist/easyprivacy.txt) / [JustDomains - EasyPrivacy](https://justdomains.github.io/blocklists/lists/easyprivacy-justdomains.txt)
-[NoCoin Filter List](https://github.com/hoshsadiq/adblock-nocoin-list/) / [JustDomains - NoCoin Filter List](https://justdomains.github.io/blocklists/lists/nocoin-justdomains.txt)
-[AdGuard DNS filter](https://github.com/AdguardTeam/AdguardSDNSFilter) / [JustDomains - AdGuard Simplified Domain Names Filter](https://justdomains.github.io/blocklists/lists/adguarddns-justdomains.txt)
-[YoYo Lists](https://pgl.yoyo.org/adservers/serverlist.php)
-[Peter Lowe’s ad/tracking/malware servers](https://pgl.yoyo.org/adservers/policy.php)

### Exemplo:

Execute a versão mais recente do script automaticamente:
```powershell
iwr -useb 'https://raw.githubusercontent.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/main/sos-system-wide-windows-ad-block.ps1' | iex
```
