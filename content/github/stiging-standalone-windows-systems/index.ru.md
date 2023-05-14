---
title: "Автоматизация соответствия Windows 10 STIG с помощью сценария Powershell"
date: 2020-08-26
---

** Загрузите все необходимые файлы с[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

** Нам нужна помощь в следующем[.Net issue](https://github.com/simeononsecurity/W10-Optimize-and-Harden/issues/3) 

## Введение:

Windows 10 — небезопасная операционная система «из коробки», и для ее защиты требуется множество изменений.[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) согласие.
Такие организации, как[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) рекомендовали и требовали изменения конфигурации для блокировки, усиления и защиты операционной системы и обеспечения соответствия требованиям правительства. Эти изменения охватывают широкий спектр мер по смягчению последствий, включая блокировку телеметрии, макросов, удаление вредоносных программ и предотвращение многих физических атак на систему.

Автономные системы являются одними из самых сложных и раздражающих систем для обеспечения безопасности. Если они не автоматизированы, они требуют ручных изменений каждого STIG/SRG. Всего более 1000 изменений конфигурации при типичном развертывании и в среднем 5 минут на каждое изменение, что соответствует 3,5 дням работы. Этот скрипт призван значительно ускорить этот процесс.

## Примечания:

- Этот сценарий предназначен для работы в средах **Enterprise** и предполагает, что у вас есть аппаратная поддержка для всех требований.
  - Для персональных систем см. это[GitHub Repository](https://github.com/simeononsecurity/W10-Optimize-and-Harden)
- Этот сценарий не предназначен для доведения системы до 100% соответствия, его следует использовать в качестве трамплина для выполнения большинства, если не всех, изменений конфигурации, которые можно выполнить в сценарии.
  - За вычетом системной документации эта коллекция должна привести вас к 95% соответствию всем применяемым STIGS/SRG.

## Требования:
- [X] Windows 10 Enterprise **требуется** для STIG.
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) для высокозащищенного устройства Windows 10
-[x] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - В настоящее время Windows 10 **v1909** или **v2004**.
  - Запустить[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) для обновления и проверки последней основной версии.
- [X] Требования к оборудованию
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)
  
## Рекомендуемый материал для чтения:
  -[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  -[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  -[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  -[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  -[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  -[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Список скриптов и инструментов, которые использует эта коллекция:

-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)

-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)

## Дополнительные конфигурации рассматривались из:

-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)

-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)

## Применены STIGS/SRG:
 
-[Windows 10 V1R23](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_10_V1R23_STIG.zip)

-[Windows Defender Antivirus V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_Defender_Antivirus_V1R9_STIG.zip)

-[Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

-[Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)

-[Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)

-[Microsoft Office 2019/Office 365 Pro Plus V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Office_365_ProPlus_V1R2_STIG.zip)

-[Microsoft Office 2016 V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/pdf/U_Microsoft_Office_2016_V1R2_Overview.pdf)

-[Microsoft Office 2013 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MicrosoftOffice2013_V1R5_Overview.zip)

-[Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)

-[Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **Работа в процессе**

-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Как запустить скрипт

**Скрипт можно запустить из извлеченной загрузки GitHub следующим образом:**
```
.\secure-standalone.ps1
```
Сценарий, который мы будем использовать, должен быть запущен из каталога, содержащего все остальные файлы из каталога.[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
