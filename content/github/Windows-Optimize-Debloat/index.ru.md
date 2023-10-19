---
title: "Оптимизация компьютера под управлением Windows с помощью программы Windows-Optimize-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Повышение производительности и конфиденциальности операционной системы Windows с помощью Windows-Optimize-Debloat - комплексного скрипта, позволяющего удалить раздутое ПО и оптимизировать системные настройки."
tags: ["Windows-Optimize-Debloat", "Оптимизация Windows", "Деблокирующие окна", "Ускорение работы Windows", "Оптимизация производительности Windows", "Повышение производительности Windows", "Оптимизация системы Windows", "Microsoft", "Конфиденциальность", "Удаление вредоносного ПО", "Windows 10", "Windows 11", "Защитник Windows", "Обновление Windows", "Cortona", "Объекты групповой политики", "Телеметрия", "Windows Store", "Windows 10 Professional", "Windows 10 Home"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Для тех, кто стремится минимизировать установку Windows 10 и 11.

**Примечание:** Этот сценарий должен работать в большинстве, если не во всех, системах без проблем. Хотя [@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Не запускайте этот скрипт, если вы не понимаете, что он делает.

## Введение:
Windows 10 и 11 - это инвазивные и небезопасные операционные системы из коробки.
Такие организации, как [Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) и другие специалисты рекомендовали внести изменения в конфигурацию, чтобы оптимизировать и разгрузить операционную систему Windows 10. Эти изменения включают в себя блокировку телеметрии, удаление журналов, удаление раздутого ПО и т. д. Данный сценарий предназначен для автоматизации конфигураций, рекомендованных этими организациями.

## Примечания:
- Данный сценарий предназначен для работы в основном в средах **Personal Use**.
- Сценарий разработан таким образом, что оптимизация, в отличие от некоторых других сценариев, не нарушает основную функциональность windows.
 - Такие функции, как Windows Update, Windows Defender, Windows Store и Cortona, были ограничены, но не находятся в нерабочем состоянии, как большинство других сценариев конфиденциальности Windows 10.
- Если вам нужен минимизированный скрипт, предназначенный только для коммерческих сред, обратитесь к этому примеру [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Требования:
- [X] Windows 10/11 Enterprise, Windows 10 Professional или Windows 10 Home.
  - Windows Home не позволяет настраивать GPO.
    - Сценарий будет работать, но не все параметры будут применены.
  - Издания Windows "N" не тестировались.
  - Запустите сценарий [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) для обновления и проверки последнего мажорного релиза.

## Исправление учетной записи Microsoft или служб Xbox:
Это связано с тем, что мы блокируем вход в учетные записи Microsoft. Телеметрия и ассоциация идентификационных данных Microsoft не одобряются.
Однако если вы все еще хотите использовать эти службы, обратитесь к следующим проблемным билетам:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## Список скриптов и инструментов, используемых в данной коллекции:
- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Были рассмотрены дополнительные конфигурации из:
- [BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
- [MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
- [Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
- [Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
- [Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
- [Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
- [Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
- [UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
- [Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
- [The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
- [TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
- [W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)

## Как запустить скрипт:
### Автоматическая установка:
Скрипт может быть запущен из распакованной загрузки с GitHub следующим образом:
```powershell
iwr -useb 'https://simeononsecurity.com/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### Установка вручную:
При ручной загрузке скрипт должен быть запущен из административного powershell в директории, содержащей все файлы из файла [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

Сценарий "sos-optimize-windows.ps1" включает в себя несколько параметров, позволяющих настраивать процесс оптимизации. Каждый параметр представляет собой булево значение, которое по умолчанию равно true, если не указано.

- **$cleargpos**: Очищает параметры объектов групповой политики.
- **$installupdates**: Устанавливает обновления в систему.
- **$removebloatware**: Удаляет из системы ненужные программы и функции.
- **$disabletelemetry**: Отключение сбора данных и телеметрии.
- **$privacy**: Внесение изменений для улучшения конфиденциальности.
- **$imagecleanup**: Очистка системы от ненужных файлов.
- **$diskcompression**: Сжатие системного диска.
- **$updatemanagement**: Изменяет способ управления и улучшения обновлений в системе.
- **$sosbrowsers**: Оптимизирует работу веб-браузеров системы.

Примером запуска скрипта с определенными параметрами может быть:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

