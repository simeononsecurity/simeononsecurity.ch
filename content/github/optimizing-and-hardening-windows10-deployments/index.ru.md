---
title: "Оптимизация, защита и безопасность развертываний Windows 10 с помощью автоматических изменений конфигурации"
date: 2020-07-22
---
 Устойчивость и деблокирование развертываний Windows 10**.

**Скачайте все необходимые файлы с сайта [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

**Мы ищем помощь в следующих вопросах [.Net issue](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/3) 

## Введение:
Windows 10 - это инвазивная и небезопасная операционная система из коробки.
Такие организации, как [PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) рекомендованы изменения конфигурации для блокировки, усиления и защиты операционной системы. Эти изменения охватывают широкий спектр мер, включая блокирование телеметрии, макросов, удаление раздутого ПО и предотвращение многих цифровых и физических атак на систему. Данный скрипт предназначен для автоматизации конфигураций, рекомендуемых этими организациями.

## Примечания:
- Данный скрипт предназначен для работы преимущественно в средах **Personal Use**. При этом некоторые параметры корпоративной конфигурации не реализованы. Данный сценарий не предназначен для приведения системы к 100%-ному соответствию требованиям. Скорее, его следует использовать как ступеньку для завершения большинства, если не всех, изменений конфигурации, которые можно внести в сценарий, пропуская такие моменты, как брендинг и баннеры, где они не должны быть реализованы даже в защищенной среде персонального использования.
- Этот сценарий разработан таким образом, что оптимизация, в отличие от некоторых других сценариев, не нарушает основную функциональность windows.
 - Такие функции, как Windows Update, Windows Defender, Windows Store и Cortona, были ограничены, но не находятся в нерабочем состоянии, как большинство других скриптов конфиденциальности Windows 10.
- Если вам нужен минимизированный скрипт, предназначенный только для коммерческих сред, обратитесь к этому примеру [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Требования:
- [X] Windows 10 Enterprise (**Предпочтительно**) или Windows 10 Professional
  - Windows 10 Home не позволяет настраивать GPO.
  - Издания Windows 10 "N" не тестируются.
- [X] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) для высокозащищенного устройства с Windows 10
- [X] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - В настоящее время Windows 10 **v1909**, **v2004** или **20H2**.
  - Запустите [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) для обновления и проверки последней основной версии.
- [X] Перед выполнением этого сценария Bitlocker должен быть приостановлен или выключен, после перезагрузки он может быть включен снова.
  - Последующие запуски этого сценария могут быть выполнены без отключения битлокатора.
- [X] Требования к аппаратному обеспечению
  - [Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  - [Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  - [Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  - [Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)


## Рекомендуемые материалы для чтения:
  - [System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  - [System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  - [Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  - [Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  - [Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  - [Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Список скриптов и инструментов, используемых в данной коллекции:
- [Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Были рассмотрены дополнительные конфигурации из:
- [BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
- [CERT - IE Scripting Engine Memory Corruption](https://kb.cert.org/vuls/id/573168/)
- [Dirteam - SSL Hardening](https://dirteam.com/sander/2019/07/30/howto-disable-weak-protocols-cipher-suites-and-hashing-algorithms-on-web-application-proxies-ad-fs-servers-and-windows-servers-running-azure-ad-connect/)
- [Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
- [Microsoft - Reduce attack surfaces with attack surface reduction rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
- [Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
- [Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
- [Microsoft - Specture and Meltdown Mitigations](https://support.microsoft.com/en-us/help/4072698/windows-server-speculative-execution-side-channel-vulnerabilities)
- [Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
- [Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
- [Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
- [Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
- [Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
- [NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
- [NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)
- [NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
- [NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)
- [UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
- [Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
- [The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
- [TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
- [W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)
- [Whonix - Disable TCP Timestamps](https://www.whonix.org/wiki/Disable_TCP_and_ICMP_Timestamps)

## Применяемые СТИГи/СРГ:
- [Adobe Reader Pro DC Classic V1R3](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)
- [Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Classic_V1R3_STIG.zip)
- [Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)
- [Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)
- [Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)
- [Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **Работа в процессе выполнения**
- [Microsoft Office 2013 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MicrosoftOffice2013_V1R5_Overview.zip)
- [Microsoft Office 2016 V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/pdf/U_Microsoft_Office_2016_V1R2_Overview.pdf)
- [Microsoft Office 2019/Office 365 Pro Plus V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Office_365_ProPlus_V1R2_STIG.zip)
- [Microsoft OneDrive STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_OneDrive_V2R1_STIG.zip)
- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)
- [Windows 10 V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)
- [Windows Defender Antivirus V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)
- [Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

## Как запустить скрипт
### Установка вручную:
При ручной загрузке скрипт должен быть запущен из административного powershell в директории, содержащей все файлы из каталога [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-optimize-windows.ps1
```
### Автоматическая установка:
Скрипт может быть запущен из распакованной загрузки с GitHub следующим образом:
```powershell
iex ((New-Object System.Net.WebClient).DownloadString('https://simeononsecurity.com/scripts/windowsoptimizeandharden.ps1'))
```
<img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/w10automatic.gif" alt="Пример
Автоматическая установка Windows-Optimize-Harden-Debloat">
