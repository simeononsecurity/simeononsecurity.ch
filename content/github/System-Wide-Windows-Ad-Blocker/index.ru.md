---
title: "Общесистемный скрипт блокировки рекламы Windows 10 для лучшей конфиденциальности и безопасности"
date: 2021-04-02
lastmod: 2026-11-23
toc: true
draft: false
description: "Блокируйте в Windows домены из списка StevenBlack с помощью скрипта PowerShell, который сохраняет ваши записи в файле hosts."
tags: ["Windows 10", "блокировщик рекламы", "блокировка телеметрии", "Сценарий PowerShell", "общесистемная блокировка рекламы", "конфиденциальность", "безопасность"]
---

Блокируйте в Windows домены из списка StevenBlack с помощью скрипта PowerShell, который сохраняет ваши записи в файле hosts.

## Подготовка и предварительная проверка

Скачайте и распакуйте весь репозиторий. Перед запуском прочитайте [README на GitHub](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/blob/main/README.md) и проверьте скрипт. В распакованной папке откройте Windows PowerShell 5.1 или PowerShell 7 от имени администратора. Сначала проверьте DNS и нужные приложения на временной системе Windows.

Сначала проверьте, какие изменения будут внесены. Запустите вторую команду отдельно, когда будете готовы применить изменения.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1
```

## Восстановление исходного файла hosts

Сначала проверьте, что сделает команда восстановления. Запустите вторую команду отдельно, когда будете готовы восстановить файл.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore
```

Не изменяйте резервную копию до успешного восстановления. Если после применения изменений пользователь или приложение отредактировали файл hosts, восстановление остановится. Сохраните и согласуйте эти правки перед повторной попыткой.

## Список блокировки

- [StevenBlack/hosts](https://github.com/StevenBlack/hosts)
- [Сообщить о проблеме](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues)
