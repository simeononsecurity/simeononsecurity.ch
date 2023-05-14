---
title: "Оптимизируйте свой ПК с Windows с помощью Windows-Optimize-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Повысьте производительность и конфиденциальность вашей операционной системы Windows с помощью Windows-Optimize-Debloat, всеобъемлющего сценария, который помогает удалять вредоносные программы и оптимизировать системные настройки."
tags: ["Windows-Оптимизация-Раздувание", "Оптимизация Windows", "Разблокировка Windows", "Ускорить Windows", "Оптимизация производительности Windows", "Повышение производительности Windows", "Оптимизация системы Windows", "Майкрософт", "Конфиденциальность", "Удаление вирусов", "Windows 10", "Windows 11", "Защитник Windows", "Центр обновления Windows", "Кортона", "Объекты групповой политики", "Телеметрия", "Магазин Windows", "Windows 10 Профессиональная", "Windows 10 Домашняя"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Для тех, кто стремится свести к минимуму свои установки Windows 10 и 11.*

**Примечание.** Этот скрипт должен без проблем работать на большинстве, если не на всех, системах. Пока[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Не запускайте этот сценарий, если вы не понимаете, что он делает.

## Введение:
Windows 10 и 11 являются инвазивными и небезопасными операционными системами из коробки.
Такие организации, как[Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) и другие рекомендовали изменения конфигурации для оптимизации и разгрузки операционной системы Windows 10. Эти изменения включают в себя блокировку телеметрии, удаление журналов и удаление вредоносных программ, и это лишь некоторые из них. Этот сценарий предназначен для автоматизации конфигураций, рекомендованных этими организациями.

## Примечания:
- Этот сценарий предназначен для работы в основном в средах **личного использования**.
- Этот скрипт разработан таким образом, что оптимизации, в отличие от некоторых других скриптов, не нарушают основные функции Windows.
 - Такие функции, как Центр обновления Windows, Защитник Windows, Магазин Windows и Cortona, были ограничены, но не находятся в неработоспособном состоянии, как большинство других сценариев конфиденциальности Windows 10.
- Если вы ищете свернутый сценарий, предназначенный только для коммерческих сред, см.[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Требования:
- [X] Windows 10/11 Корпоративная, Windows 10 Профессиональная или Windows 10 Домашняя
  - Windows Home не позволяет настраивать объекты групповой политики.
    - Скрипт по-прежнему будет работать, но не все настройки будут применены.
  - Редакции Windows "N" не тестировались.
  - Запустить[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) для обновления и проверки последней основной версии.

## Исправление учетной записи Microsoft или служб Xbox:
Это связано с тем, что мы блокируем вход в учетные записи Microsoft. Телеметрия Microsoft и сопоставление удостоверений не одобряются.
Однако, если вы по-прежнему хотите использовать эти услуги, см. следующие тикеты для разрешения:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## Список скриптов и инструментов, которые использует эта коллекция:
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Дополнительные конфигурации рассматривались из:
-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)

## Как запустить скрипт:
### Автоматическая установка:
Скрипт можно запустить из извлеченной загрузки GitHub следующим образом:
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### Manual Install:
If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

The script "sos-optimize-windows.ps1" includes several parameters that allow for customization of the optimization process. Each parameter is a boolean value that defaults to true if not specified.

- **$cleargpos**: Clears Group Policy Objects settings.
- **$installupdates**: Installs updates to the system.
- **$removebloatware**: Removes unnecessary programs and features from the system.
- **$disabletelemetry**: Disables data collection and telemetry.
- **$privacy**: Makes changes to improve privacy.
- **$imagecleanup**: Cleans up unneeded files from the system.
- **$diskcompression**: Compresses the system disk.
- **$updatemanagement**: Changes the way updates are managed and improved on the system.
- **$sosbrowsers**: Optimizes the system's web browsers.

An example of how to launch the script with specific parameters would be:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

