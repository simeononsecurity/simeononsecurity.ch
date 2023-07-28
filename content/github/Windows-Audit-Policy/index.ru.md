---
title: "Максимально эффективный аудит Windows с помощью сценария политики аудита Windows"
date: 2021-05-10
toc: true
draft: false
description: "Узнайте, как максимально эффективно использовать аудит Windows путем применения сценария политики аудита Windows для повышения уровня безопасности и контроля."
tags: ["Политика аудита Windows", "Аудит Windows", "безопасность", "мониторинг", "auditpol", "Команды Windows", "Безопасность Windows", "конфигурация аудита", "политики безопасности", "журналы событий", "мониторинг системы", "Сервер Windows", "передовые методы обеспечения безопасности", "кибербезопасность", "анализ журнала", "соблюдение требований безопасности", "реагирование на инциденты", "средства мониторинга безопасности", "привилегированный доступ", "Администрирование Windows", "скриптинг", "системное администрирование", "информационная безопасность", "аудит соответствия", "Усиление защиты Windows", "средства контроля безопасности", "автоматизация системы безопасности", "управление журналом", "Параметры безопасности Windows"]
---

## Windows-Audit-Policy

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml)

Максимальное расширение возможностей аудита Windows

## Рекомендуемые материалы для чтения:
  - [auditpol](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol)
  - [auditpol clear](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-clear)
  - [auditpol backup](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-backup)
  - [auditpol restore](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-restore)
  - [auditpol list](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-list)

## Как запустить скрипт
## Ручная установка:
При ручной загрузке скрипт должен быть запущен из директории, содержащей все остальные файлы из каталога [GitHub Repository](https://github.com/simeononsecurity/Windows-Audit-Policy)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-auditpolicy.ps1
```
