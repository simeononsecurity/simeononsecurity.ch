---
title: "Полное руководство по защите Windows с помощью Windows Defender Application Control WDAC"
date: 2020-12-16
toc: true
draft: false
description: "Узнайте, как использовать Windows Defender Application Control WDAC для защиты операционной системы Windows с помощью сценариев и инструментов."
tags: ["Защита приложений WDAC в Защитнике Windows", "PowerShell", "Сценарий PowerShell", "Автоматизация", "Согласие", "Синяя команда", "Скрипт STIG Защитника Windows", "Усиление Защитника Windows", "Защитник Windows СТИГ", "Защитник СТИГ", "Защита от эксплойтов Защитника Windows WDEP", "ASR для уменьшения поверхности атаки Защитника Windows", "Виндовс сервер 2016 2019", "Ядро сервера Windows", "Набор инструментов Microsoft WDAC", "Обновить политику CI", "Рекомендуемые Microsoft правила блокировки", "Рекомендуемые Microsoft правила блокировки драйверов", "XML-политики", "Политики БИН", "Групповая политика", "Майкрософт Интуне"]
---

**Защитите Windows с помощью управления приложениями в Защитнике Windows WDAC**

## Примечания:
- Windows Server 2016/2019 или что-либо до версии 1903 одновременно поддерживают только одну устаревшую политику.
- Редакция Windows Server Core поддерживает WDAC, но некоторые компоненты, зависящие от AppLocker, не будут работать.
- Пожалуйста, прочтите[Recommended Reading](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening#recommended-reading) перед внедрением или даже тестированием.

## Список скриптов и инструментов, которые использует эта коллекция:

-[MicrosoftDocs - WDAC-Toolkit](https://github.com/MicrosoftDocs/WDAC-Toolkit)
-[Microsoft - Refresh CI Policy ](https://www.microsoft.com/en-us/download/details.aspx?id=102925)

## Дополнительные конфигурации рассматривались из:

-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)

## Объяснение:

### XML против BIN:

- Проще говоря, политики **"XML"** предназначены для локального применения к машине, а файлы **"BIN"** — для принудительного применения их с помощью[Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) or [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) Хотя вы можете использовать политики XML, BIN или CIP в локальном развертывании, вообще говоря, вы должны придерживаться XML, где это возможно, особенно при аудите или устранении неполадок.

### Описание политик:

- **Политики по умолчанию:**
  - Политики «По умолчанию» используют только функции по умолчанию, доступные в WDAC-Toolkit.
- **Рекомендуемые правила:**
  - Политики «Рекомендуемые» используют функции по умолчанию, а также рекомендованные Microsoft[blocks](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules) and [driver block](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules) правила.
- **Политика аудита:**
  - Политики «Аудит», просто регистрируйте исключения из правил. Это предназначено для тестирования в вашей среде, чтобы вы могли изменять политики по своему усмотрению в соответствии с потребностями вашей среды.
- **Принудительные политики:**
  - Политики «Принудительно» не допустят каких-либо исключений из правил, приложения, драйверы, dll и т. д. будут заблокированы, если они не соответствуют.

### Доступные политики:

- **XML:**
  - **Только аудит:**
    - `WDAC_V1_Default_Audit_{версия}.xml`
    - `WDAC_V1_Recommended_Audit_{версия}.xml`
  - **Принудительно:**
    - `WDAC_V1_Default_Enforced_{версия}.xml`
    - `WDAC_V1_Recommended_Enforced_{версия}.xml`
- **БИН:**
  - **Только аудит:**
    - `WDAC_V1_Default_Audit_{версия}.bin`
    - `WDAC_V1_Recommended_Audit_{версия}.bin`
  - **Принудительно:**
    - `WDAC_V1_Default_Enforced_{версия}.bin`
    - `WDAC_V1_Recommended_Enforced_{версия}.bin`
- **СИП:**
  - **Только аудит:**
    - `WDAC_V1_Default_Audit\{uid}.cip`
    - `WDAC_V1_Recommended_Audit\{uid}.cip`
  - **Принудительно:**
    - `WDAC_V1_Default_Enforced\{uid}.cip`
    - `WDAC_V1_Recommended_Enforced\{uid}.cip`

Обновите следующую строку в сценарии, чтобы использовать нужную политику локально:

```powershell
$PolicyPath = "C:\temp\Windows Defender\CIP\WDAC_V1_Recommended_Enforced\*.cip"
#https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script
ForEach ($Policy in (Get-ChildItem -Recurse $PolicyPath).Fullname) {
  $PolicyBinary = "$Policy"
  $DestinationFolder = $env:windir+"\System32\CodeIntegrity\CIPolicies\Active\"
  $RefreshPolicyTool = "./Files/EXECUTABLES/RefreshPolicy(AMD64).exe"
  Copy-Item -Path $PolicyBinary -Destination $DestinationFolder -Force
  & $RefreshPolicyTool
}
```

Alternatively, you may use [Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) or [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) to enforce the WDAC policies.

## Auditing:

You can view the WDAC event logs in event viewer under:

`Applications and Services Logs\Microsoft\Windows\CodeIntegrity\Operational`

## Recommended Reading:

- [Argonsys - Deploying Windows 10 Application Control Policy](https://argonsys.com/microsoft-cloud/library/deploying-windows-10-application-control-policy/)
- [Microsoft - Audit Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/audit-windows-defender-application-control-policies)
- [Microsoft - Create a WDAC policy for fixed-workload devices using a reference computer](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [Microsoft - Deploy Windows Defender Application Control policies by using Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy)
- [Microsoft - Deploy Windows Defender Application Control policies by using Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune)
- [Microsoft - Deploy WDAC policies using script](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [Microsoft - Enforce Windows Defencer Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/enforce-windows-defender-application-control-policies)
- [Microsoft - Guidance on Creating WDAC Deny Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [Microsoft - Use multiple Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)

## How to run the script:

### Manual Install:

If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening/archive/main.zip)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-wdachardening.ps1
```
