---
title: "Автоматизация соответствия Windows Server STIG с помощью сценариев STIG"
date: 2020-09-09
---

** Загрузите все необходимые файлы с[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**Примечание.** Этот скрипт должен без проблем работать на большинстве, если не на всех, системах. Пока[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Не запускайте этот сценарий, если вы не понимаете, что он делает. Вы несете ответственность за просмотр и тестирование сценария перед его запуском.

## Доступно:
Теперь мы предлагаем сборник пьес для этого скрипта. См. следующее:
-[Github Repo](https://github.com/simeononsecurity/Windows_STIG_Ansible)
-[Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## Введение:

Windows 10 — небезопасная операционная система «из коробки», и для ее защиты требуется множество изменений.[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) согласие.
Такие организации, как[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://www.defense.gov/), and the [National Security Agency](https://www.nsa.gov/) рекомендовали и требовали изменения конфигурации для блокировки, усиления и защиты операционной системы и обеспечения соответствия требованиям правительства. Эти изменения охватывают широкий спектр мер по смягчению последствий, включая блокировку телеметрии, макросов, удаление вредоносных программ и предотвращение многих физических атак на систему.

Автономные системы являются одними из самых сложных и раздражающих систем для обеспечения безопасности. Если они не автоматизированы, они требуют ручных изменений каждого STIG/SRG. Всего более 1000 изменений конфигурации при типичном развертывании и в среднем 5 минут на каждое изменение, что соответствует 3,5 дням работы. Этот скрипт призван значительно ускорить этот процесс.

## Примечания:

- Этот сценарий предназначен для работы в средах **Enterprise** и предполагает, что у вас есть аппаратная поддержка для всех требований.
  - Для персональных систем см. это[GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)
- Этот сценарий не предназначен для доведения системы до 100% соответствия, его следует использовать в качестве трамплина для выполнения большинства, если не всех, изменений конфигурации, которые можно выполнить в сценарии.
  - За вычетом системной документации эта коллекция должна привести вас к 95% соответствию всем применяемым STIGS/SRG.

## Требования:
- [X] Для STIG требуется Windows 10 Enterprise.
-[X] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) для высокозащищенного устройства Windows 10
-[X] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Запустить[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) для обновления и проверки последней основной версии.
- [X] Bitlocker должен быть приостановлен или выключен перед реализацией этого скрипта, его можно снова включить после перезагрузки.
  - Последующие запуски этого скрипта можно запускать без отключения битлокера.
- [X] Требования к оборудованию
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

## Список скриптов и инструментов, которые использует эта коллекция:
-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Дополнительные конфигурации рассматривались из:
-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
-[NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)

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
-[Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)

## Редактирование политик в Local Group Policy постфактум:
- Импортируйте определения политики ADMX из этого[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) в *C:\windows\PolicyDefinitions* в системе, которую вы пытаетесь изменить.
- Открыть```gpedit.msc``` on on the system you're trying to modify. 


## How to run the script:
### Automated Install:
The script may be launched from the extracted GitHub download like this:
```powershell
iex ((New-Object System.Net.WebClient).DownloadString('https://simeononsecurity.com/scripts/standalonewindows.ps1'))
```

### Manual Install:
If manually downloaded, the script must be launched from the directory containing all the other files from the [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

All of the parameters in the "secure-standalone.ps1" script are optional, with a default value of $true. This means that if no value is specified for a parameter when the script is run, it will be treated as if it were set to $true.

The script takes the following parameters, all of which are optional and default to $true if not specified:

- **cleargpos**: (Boolean) Clear GPOs not being used
- **installupdates**: (Boolean) Install updates and reboot if necessary
- **adobe**: (Boolean) STIG Adobe Reader
- **firefox**: (Boolean) STIG Firefox
- **chrome**: (Boolean) STIG Chrome
- **IE11**: (Boolean) STIG Internet Explorer 11
- **edge**: (Boolean) STIG Edge
- **dotnet**: (Boolean) STIG .NET Framework
- **office**: (Boolean) STIG Office
- **onedrive**: (Boolean) STIG OneDrive
- **java**: (Boolean) STIG Java
- **windows**: (Boolean) STIG Windows
- **defender**: (Boolean) STIG Windows Defender
- **firewall**: (Boolean) STIG Windows Firewall
- **mitigations**: (Boolean) STIG Mitigations
- **nessusPID**: (Boolean) Resolve Unquoted Strings in Path
- **horizon**: (Boolean) STIG VMware Horizon
- **sosoptional**: (Boolean) Optional STIG/Hardening items

An example of how to run the script with all default parameters would be:

```powershell
.\secure-standalone.ps1
```
If you want to specify a different value for one or more of the parameters, you can include them in the command along with their desired value. For example, if you wanted to run the script and set the $firefox parameter to $false, the command would be:

```powershell
.\secure-standalone.ps1 -firefox $false
```

You can also specify multiple parameters in the command like this:

```powershell
.\secure-standalone.ps1 -firefox $false -chrome $false
```

Обратите внимание, что в этом примере для параметров Firefox и Chrome задано значение $false.



