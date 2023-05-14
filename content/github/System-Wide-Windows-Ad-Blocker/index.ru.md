---
title: "Общесистемный скрипт блокировки рекламы Windows 10 для лучшей конфиденциальности и безопасности"
date: 2021-04-02
toc: true
draft: false
description: "Блокируйте рекламу, трекеры и данные телеметрии в Windows 10 с помощью этого мощного сценария PowerShell, который использует файл hosts и брандмауэр Windows для общесистемной блокировки рекламы."
tags: ["Windows 10", "блокировщик рекламы", "блокировка телеметрии", "Сценарий PowerShell", "общесистемная блокировка рекламы", "конфиденциальность", "безопасность", "EasyList", "Легкая конфиденциальность", "Список фильтров NoCoin", "DNS-фильтр AdGuard", "YoYo списки", "Серверы вредоносного ПО для отслеживания рекламы Питера Лоу", "Брандмауэр Windows", "списки доменов", "блокировать трекеры Windows", "Блок-трекеры", "блокировать рекламу", "блокировать отслеживание"]
---

## Описание:
Этот сценарий блокирует домены, связанные с телеметрией, через файл hosts и соответствующие IP-адреса через брандмауэр Windows.

**Примечания:**
- Добавление этих доменов может привести к поломке некоторых программ, таких как iTunes или Skype.
- Сообщалось, что записи, связанные с Akamai, вызывают проблемы с Widevine DRM.

### Используемые списки:
-[EasyList](https://easylist.to/easylist/easylist.txt) / [JustDomains - EasyList](https://justdomains.github.io/blocklists/lists/easylist-justdomains.txt)
-[Easy Privacy](https://easylist.to/easylist/easyprivacy.txt) / [JustDomains - EasyPrivacy](https://justdomains.github.io/blocklists/lists/easyprivacy-justdomains.txt)
-[NoCoin Filter List](https://github.com/hoshsadiq/adblock-nocoin-list/) / [JustDomains - NoCoin Filter List](https://justdomains.github.io/blocklists/lists/nocoin-justdomains.txt)
-[AdGuard DNS filter](https://github.com/AdguardTeam/AdguardSDNSFilter) / [JustDomains - AdGuard Simplified Domain Names Filter](https://justdomains.github.io/blocklists/lists/adguarddns-justdomains.txt)
-[YoYo Lists](https://pgl.yoyo.org/adservers/serverlist.php)
-[Peter Lowe’s ad/tracking/malware servers](https://pgl.yoyo.org/adservers/policy.php)

### Пример:

Запустите последнюю версию скрипта автоматически:
```powershell
iwr -useb 'https://raw.githubusercontent.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/main/sos-system-wide-windows-ad-block.ps1' | iex
```
