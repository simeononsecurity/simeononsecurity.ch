---
title: "Оптимизируйте и укрепите свою систему Windows с помощью сценария Windows-Optimize-Harden-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Это подробное руководство содержит пошаговые инструкции по оптимизации, усилению защиты и разгрузке системы Windows для повышения производительности, безопасности и конфиденциальности."
tags: ["Оптимизация Windows", "Укрепление Windows", "Раздувание Windows", "Безопасность Windows", "Производительность Windows", "Конфиденциальность Windows", "обновления Windows", "Объекты групповой политики", "Adobe Acrobat Reader", "Fire Fox", "Гугл Хром", "Интернет-проводник", "Край Майкрософт Хром", "Дот-нет 4", "Microsoft Office", "Один диск", "Oracle Java JRE 8", "Брандмауэр Windows", "Защитник Windows", "Блокировщик приложений"]
---
 Введение:

Windows 10 и Windows 11 являются инвазивными и небезопасными операционными системами из коробки.
Такие организации, как[PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) имеют рекомендованные изменения конфигурации для блокировки, усиления защиты и защиты операционной системы. Эти изменения охватывают широкий спектр мер по смягчению последствий, включая блокировку телеметрии, макросов, удаление вредоносных программ и предотвращение многих цифровых и физических атак на систему. Этот сценарий предназначен для автоматизации конфигураций, рекомендованных этими организациями.

## Примечания, предупреждения и рекомендации:

**ПРЕДУПРЕЖДЕНИЕ:**

Этот скрипт должен без проблем работать на большинстве, если не на всех, системах. Пока[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues)

- Этот сценарий предназначен для работы преимущественно в средах **личного использования**. С учетом этого некоторые параметры конфигурации предприятия не реализованы. Этот скрипт не предназначен для доведения системы до 100% соответствия. Скорее, его следует использовать в качестве трамплина для завершения большинства, если не всех, изменений конфигурации, которые можно запрограммировать, пропуская прошлые проблемы, такие как брендинг и баннеры, которые не следует реализовывать даже в жесткой среде личного использования.
- Этот скрипт разработан таким образом, что оптимизации, в отличие от некоторых других скриптов, не нарушают основные функции Windows.
- Такие функции, как Центр обновления Windows, Защитник Windows, Магазин Windows и Cortona, были ограничены, но не находятся в дисфункциональном состоянии, как большинство других сценариев конфиденциальности Windows 10.
- Если вы ищете свернутый сценарий, предназначенный только для коммерческих сред, см.[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)


**Не запускайте этот скрипт, если не понимаете, что он делает. Вы несете ответственность за просмотр и тестирование скрипта перед его запуском.**

**НАПРИМЕР, СЛЕДУЮЩЕЕ СЛЕДУЮЩЕЕ ПОЛУЧИТСЯ, ЕСЛИ ВЫ ЗАПУСТИТЕ ЭТО БЕЗ ПРОФИЛАКТИЧЕСКИХ ШАГОВ:**

- Использование учетной записи администратора по умолчанию с именем «Администратор» отключено и переименовано в соответствии с DoD STIG.

  - Не применяется к созданной учетной записи по умолчанию, но применяется к использованию учетной записи администратора по умолчанию, часто используемой в версиях Enterprise, IOT и Windows Server.

  - Создайте новую учетную запись в разделе «Управление компьютером» и установите ее в качестве администратора, если хотите. Затем скопируйте содержимое папки предыдущих пользователей в новую после первого входа в систему нового пользователя, чтобы обойти эту проблему перед запуском скрипта.

- Вход с использованием учетной записи Microsoft отключен для DoD STIG.

  - При попытке обеспечить безопасность и конфиденциальность не рекомендуется входить в свою локальную учетную запись через учетную запись Microsoft. Это обеспечивается этим репо.

  - Создайте новую учетную запись в разделе «Управление компьютером» и установите ее в качестве администратора, если хотите. Затем скопируйте содержимое папки предыдущих пользователей в новую после первого входа в систему нового пользователя, чтобы обойти эту проблему перед запуском скрипта.

- PIN-коды учетной записи отключены для DoD STIG.

  - ПИН-коды небезопасны, если используются исключительно вместо пароля, и их можно легко обойти за считанные часы или, возможно, даже секунды или минуты.

  - Удалите пин-код из учетной записи и/или войдите с помощью пароля после запуска скрипта.

- Настройки Bitlocker по умолчанию изменены и усилены из-за DoD STIG.

  - Из-за того, как реализован битлокер, когда происходят эти изменения, и если у вас уже включен битлокер, это нарушит реализацию битлокера.

  - Отключите битлокер, запустите скрипт, затем снова включите битлокер, чтобы обойти эту проблему.

## Требования:

- [x] Windows 10/11 Корпоративная (**Предпочтительно**) или Профессиональная
  - Выпуски Windows 10/11 Home не поддерживают конфигурации GPO и не тестировались.
  - Редакции Window "N" не тестировались.
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) для высокозащищенного устройства Windows 10
-[x] System is [fully up to date and supported](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Запустить[Windows Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) для обновления и проверки последней основной версии.
- [x] Bitlocker должен быть приостановлен или выключен перед реализацией этого скрипта, его можно снова включить после перезагрузки.
  - Последующие запуски этого скрипта можно запускать без отключения битлокера.
- [x] Требования к оборудованию
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections)
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)

## Рекомендуемый материал для чтения:

-[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
-[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
-[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
-[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
-[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
-[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Дополнения, заметные изменения и исправления:

**Этот скрипт добавляет, удаляет и изменяет настройки вашей системы. Пожалуйста, просмотрите скрипт перед его запуском.**

### Браузеры:

- В браузерах будут установлены дополнительные расширения для обеспечения конфиденциальности и безопасности.
  - Видеть[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/11) для получения дополнительной информации.
- Из-за того, что DoD STIG реализован для браузеров, установлено управление расширениями и другие корпоративные настройки. Для получения инструкций о том, как просмотреть эти параметры, вам необходимо ознакомиться с инструкциями GPO ниже.

### Модули Powershell:

- Чтобы помочь в автоматизации обновлений Windows PowerShell[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) Модуль будет добавлен в вашу систему.

### Исправление учетной записи Microsoft, магазина или служб Xbox:

Это связано с тем, что мы блокируем вход в учетные записи Microsoft. Телеметрия Microsoft и сопоставление удостоверений не одобряются.
Однако, если вы по-прежнему хотите использовать эти услуги, см. следующие тикеты для разрешения:

- https://github.com/simeononsecurity/Windows-Optimize-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

### Редактирование политик в Local Group Policy постфактум:

Если вам нужно изменить или изменить параметр, его, скорее всего, можно настроить через GPO:

- Импортируйте определения политики ADMX из этого[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) в _C:\windows\PolicyDefinitions_ в системе, которую вы пытаетесь изменить.

- Откройте `gpedit.msc` в системе, которую вы пытаетесь изменить.

## Список скриптов и инструментов, которые использует эта коллекция:

### Первая вечеринка:

-[.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
-[FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[JAVA-STIG-Script](https://github.com/simeononsecurity/JAVA-STIG-Script)
-[Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[Windows-Optimize-Debloat](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

### Третья сторона:

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
-[Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)

## Применены STIGS/SRG:

-[Adobe Acrobat Pro DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
-[Adobe Acrobat Reader DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
-[Firefox V5R2](https://public.cyber.mil/stigs/downloads/)
-[Google Chrome V2R4](https://public.cyber.mil/stigs/downloads/)
-[Internet Explorer 11 V1R19](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Edge V1R2](https://public.cyber.mil/stigs/downloads/)
-[Microsoft .Net Framework 4 V1R9](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2013 V2R1](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2016 V2R1](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2019/Office 365 Pro Plus V2R3](https://public.cyber.mil/stigs/downloads/)
-[Microsoft OneDrive STIG V2R1](https://public.cyber.mil/stigs/downloads/)
-[Oracle JRE 8 V1R5](https://public.cyber.mil/stigs/downloads/)
-[Windows 10 V2R2](https://public.cyber.mil/stigs/downloads/)
-[Windows Defender Antivirus V2R2](https://public.cyber.mil/stigs/downloads/)
-[Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)

## Дополнительные конфигурации рассматривались из:

-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[CERT - IE Scripting Engine Memory Corruption](https://kb.cert.org/vuls/id/573168/)
-[Dirteam - SSL Hardening](https://dirteam.com/sander/2019/07/30/howto-disable-weak-protocols-cipher-suites-and-hashing-algorithms-on-web-application-proxies-ad-fs-servers-and-windows-servers-running-azure-ad-connect/)
-[MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Reduce attack surfaces with attack surface reduction rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Specture and Meltdown Mitigations](https://support.microsoft.com/en-us/help/4072698/windows-server-speculative-execution-side-channel-vulnerabilities)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)
-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
-[NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)
-[UnderGroundWires - Privacy.S\*\*Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[VectorBCO - windows-path-enumerate](https://github.com/VectorBCO/windows-path-enumerate)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)
-[Whonix - Disable TCP Timestamps](https://www.whonix.org/wiki/Disable_TCP_and_ICMP_Timestamps)

## Как запустить скрипт:
### Графический интерфейс — пошаговая установка:

Загрузите последнюю версию[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat-GUI/releases/)выберите нужные параметры и нажмите «Выполнить». <img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/WOHD-GUI.gif" alt="Пример пошаговой установки на основе графического интерфейса Windows-Optimize-Harden-Debloat"> ### Автоматическая установка: Используйте эту однострочную строку для автоматической загрузки, распаковки всех вспомогательных файлов и запуска последней версии скрипта.```powershell
iwr -useb 'https://simeononsecurity.com/scripts/windowsoptimizeandharden.ps1'|iex
```

<img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/w10automatic.gif" alt="Example of 
Windows-Optimize-Harden-Debloat automatic install">

### Manual Install:

If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

The script "sos-optimize-windows.ps1" includes several parameters that allow for customization of the optimization process. Each parameter is a boolean value that defaults to true if not specified.

- **cleargpos**: Clears Group Policy Objects settings.
- **installupdates**: Installs updates to the system.
- **adobe**: Implements the Adobe Acrobat Reader STIGs.
- **firefox**: Implements the FireFox STIG.
- **chrome**: Implements the Google Chrome STIG.
- **IE11**: Implements the Internet Explorer 11 STIG.
- **edge**: Implements the Microsoft Chromium Edge STIG.
- **dotnet**: Implements the Dot Net 4 STIG.
- **office**: Implements the Microsoft Office Related STIGs.
- **onedrive**: Implements the Onedrive STIGs.
- **java**: Implements the Oracle Java JRE 8 STIG.
- **windows**: Implements the Windows Desktop STIGs.
- **defender**: Implements the Windows Defender STIG.
- **firewall**: Implements the Windows Firewall STIG.
- **mitigations**: Implements General Best Practice Mitigations.
- **defenderhardening**: Implements and Hardens Windows Defender Beyond STIG Requirements.
- **pshardening**: Implements PowerShell Hardening and Logging.
- **sslhardening**: Implements SSL Hardening.
- **smbhardening**: Hardens SMB Client and Server Settings.
- **applockerhardening**: Installs and Configures Applocker (In Audit Only Mode).
- **bitlockerhardening**: Harden Bitlocker Implementation.
- **removebloatware**: Removes unnecessary programs and features from the system.
- **disabletelemetry**: Disables data collection and telemetry.
- **privacy**: Makes changes to improve privacy.
- **imagecleanup**: Cleans up unneeded files from the system.
- **nessusPID**: Resolves Unquoted System Strings in Path.
- **sysmon**: Installs and configures sysmon to improve auditing capabilities.
- **diskcompression**: Compresses the system disk.
- **emet**: Implements STIG Requirements and Hardening for EMET on Windows 7 Systems.
- **updatemanagement**: Changes the way updates are managed and improved on the system.
- **deviceguard**: Enables Device Guard Hardening.
- **sosbrowsers**: Optimizes the system's web browsers.

An example of how to launch the script with specific parameters would be:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```
