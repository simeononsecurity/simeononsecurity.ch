---
title: "Повышение безопасности Windows 10 с помощью сценария усиления защиты защитника"
date: 2020-11-15
toc: true
draft: false
description: "Узнайте, как повысить безопасность Windows 10 с помощью сценария PowerShell, который усиливает защиту антивирусной программы Защитник Windows, реализуя все требования антивирусной программы Защитник Windows STIG V2R1."
tags: ["Защитник Windows", "Windows 10", "Безопасность Windows 10", "Сценарий PowerShell", "Закалка", "Укрепление защитника", "Автоматизация безопасности", "Согласие", "Контролируемый доступ к папкам", "Система предотвращения вторжений", "Управление приложениями", "Снижение поверхности атаки", "Защита от эксплойтов", "Облачная защита", "Защита сети", "Скрипт STIG Защитника Windows", "Защитник Windows СТИГ", "STIG V2R1", "ВДАК", "ASR"]
---

## Что делает этот скрипт?
- Включает облачную защиту
- Включает контролируемый доступ к папкам
- Включает сетевую защиту
- Включает систему предотвращения вторжений
-[Enables Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
-[Enables Windows Defender Attack Surface Reduction Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Enables Windows Defender Exploit Protections](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide#powershell)
- Реализует все требования, перечисленные в[Windows Defender Antivirus STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)

## Требования:
- [x] Windows 10 Корпоративная (**Предпочтительно**) или Windows 10 Профессиональная
  - Windows 10 Домашняя не позволяет настраивать объекты групповой политики или[ASR](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) 
Хотя большинство из этих конфигураций по-прежнему будут применяться.
  - Выпуски Windows 10 "N" не тестировались.

## Загрузите необходимые файлы:

Скачайте необходимые файлы с[GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)

## Как запустить скрипт:

**Скрипт можно запустить из извлеченной загрузки GitHub следующим образом:**
```
.\sos-windowsdefenderhardening.ps1
```
