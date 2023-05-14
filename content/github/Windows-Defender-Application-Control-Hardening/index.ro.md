---
title: "Ghid complet pentru întărirea Windows cu Windows Defender Application Control WDAC"
date: 2020-12-16
toc: true
draft: false
description: "Aflați cum să utilizați Windows Defender Application Control WDAC pentru a vă consolida sistemul de operare Windows cu scripturi și instrumente."
tags: ["Windows Defender Application Control WDAC Hardening", "PowerShell", "Script PowerShell", "Automatizare", "Conformitate", "Echipa albastră", "Windows Defender STIG Script", "Întărirea Windows Defender", "Windows Defender STIG", "Apărător STIG", "Windows Defender Exploit Protection WDEP", "Windows Defender Attack Surface Reduction ASR", "Windows Server 2016 2019", "Windows Server Core", "Microsoft WDAC-Toolkit", "Actualizează politica CI", "Reguli de blocare recomandate de Microsoft", "Reguli de blocare a driverelor recomandate de Microsoft", "Politici XML", "Politici BIN", "Politica de grup", "Microsoft Intune"]
---

**Întărește Windows cu Windows Defender Application Control WDAC**

## Note:
- Windows Server 2016/2019 sau orice înainte de versiunea 1903 acceptă doar o singură politică moștenită la un moment dat.
- Ediția Windows Server Core acceptă WDAC, dar unele componente care depind de AppLocker nu vor funcționa
- Vă rugăm să citiți[Recommended Reading](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening#recommended-reading) înainte de implementare sau chiar testare.

## O listă de scripturi și instrumente pe care le utilizează această colecție:

-[MicrosoftDocs - WDAC-Toolkit](https://github.com/MicrosoftDocs/WDAC-Toolkit)
-[Microsoft - Refresh CI Policy ](https://www.microsoft.com/en-us/download/details.aspx?id=102925)

## Au fost luate în considerare configurații suplimentare din:

-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)

## Explicație:

### XML vs. BIN:

- Mai simplu spus, politicile **"XML"** sunt pentru aplicarea la o mașină locală, iar fișierele **"BIN"** sunt pentru aplicarea lor cu fie[Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) or [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) Deși puteți utiliza politicile XML, BIN sau CIP într-o implementare locală, în general, ar trebui să rămâneți la XML acolo unde este posibil și mai ales atunci când auditați sau depanați.

### Descrieri politici:

- **Politicile implicite:**
  - Politicile „Default” folosesc numai caracteristicile implicite disponibile în WDAC-Toolkit.
- **Politicile recomandate:**
  - Politicile „Recomandate” folosesc caracteristicile implicite, precum și cele recomandate de Microsoft[blocks](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules) and [driver block](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules) reguli.
- **Politicile de audit:**
  - Politicile „Audit”, doar înregistrați excepțiile de la reguli. Acesta este pentru testare în mediul dumneavoastră, astfel încât să puteți modifica politicile, după bunul plac, pentru a se potrivi nevoilor mediului dumneavoastră.
- **Politicile aplicate:**
  - Politicile „Implementate” nu vor permite nicio excepție de la reguli, aplicațiile, driverele, dll-urile etc. vor fi blocate dacă nu se conformează.

### Politici disponibile:

- **XML:**
  - **Numai audit:**
    - `WDAC_V1_Default_Audit_{versiune}.xml`
    - `WDAC_V1_Recommended_Audit_{versiune}.xml`
  - **Implementat:**
    - `WDAC_V1_Default_Enforced_{versiune}.xml`
    - `WDAC_V1_Recommended_Enforced_{versiune}.xml`
- **COS:**
  - **Numai audit:**
    - `WDAC_V1_Default_Audit_{versiune}.bin`
    - `WDAC_V1_Recommended_Audit_{versiune}.bin`
  - **Implementat:**
    - `WDAC_V1_Default_Enforced_{versiune}.bin`
    - `WDAC_V1_Recommended_Enforced_{versiune}.bin`
- **CIP:**
  - **Numai audit:**
    - `WDAC_V1_Default_Audit\{uid}.cip`
    - `WDAC_V1_Recommended_Audit\{uid}.cip`
  - **Implementat:**
    - `WDAC_V1_Default_Enforced\{uid}.cip`
    - `WDAC_V1_Recommended_Enforced\{uid}.cip`

Actualizați următoarea linie din script pentru a utiliza politica pe care o doriți local:

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
