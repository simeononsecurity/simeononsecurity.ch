---
title: "Guia completa per endurir Windows amb Windows Defender Application Control WDAC"
date: 2020-12-16
toc: true
draft: false
description: "Apreneu a utilitzar Windows Defender Application Control WDAC per endurir el vostre sistema operatiu Windows amb scripts i eines."
tags: ["Control d'aplicacions de Windows Defender Enduriment WDAC", "PowerShell", "Script de PowerShell", "Automatització", "Compliment", "Blue-Equip", "Windows Defender STIG Script", "Enduriment de Windows Defender", "Windows Defender STIG", "Defensor STIG", "Protecció contra l'explotació de Windows Defender WDEP", "ASR de reducció de superfície d'atac de Windows Defender", "Windows Server 2016 2019", "Windows Server Core", "Microsoft WDAC-Toolkit", "Actualitza la política de CI", "Regles de bloqueig recomanades de Microsoft", "Regles de bloqueig de controladors recomanades de Microsoft", "Polítiques XML", "Polítiques BIN", "Política de grup", "Microsoft Intune"]
---

**Endurir Windows amb Windows Defender Application Control WDAC**

## Notes:
- Windows Server 2016/2019 o qualsevol altra versió anterior a la versió 1903 només admet una única política heretada alhora.
- L'edició Windows Server Core admet WDAC, però alguns components que depenen d'AppLocker no funcionaran
- Si us plau, llegiu el[Recommended Reading](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening#recommended-reading) abans d'implementar o fins i tot provar.

## Una llista de scripts i eines que utilitza aquesta col·lecció:

-[MicrosoftDocs - WDAC-Toolkit](https://github.com/MicrosoftDocs/WDAC-Toolkit)
-[Microsoft - Refresh CI Policy ](https://www.microsoft.com/en-us/download/details.aspx?id=102925)

## S'han considerat configuracions addicionals de:

-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)

## Explicació:

### XML vs. BIN:

- En poques paraules, les polítiques **"XML"** són per aplicar-les a una màquina localment i els fitxers **"BIN"** són per fer-les complir amb qualsevol dels dos[Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) or [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) Tot i que podeu utilitzar polítiques XML, BIN o CIP en un desplegament local, en general, hauríeu d'adherir-vos a XML sempre que sigui possible i, especialment, durant l'auditoria o la resolució de problemes.

### Descripcions de la política:

- **Polítiques predeterminades:**
  - Les polítiques "Per defecte" només utilitzen les funcions predeterminades disponibles al WDAC-Toolkit.
- **Polítiques recomanades:**
  - Les polítiques "Recomanades" utilitzen les funcions predeterminades així com les recomanades de Microsoft[blocks](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules) and [driver block](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules) regles.
- **Polítiques d'auditoria:**
  - Les polítiques "Auditoria", només registreu excepcions a les regles. Això és per fer proves al vostre entorn, de manera que podeu modificar les polítiques, a voluntat, per adaptar-les a les necessitats del vostre entorn.
- **Polítiques aplicades:**
  - Les polítiques "Aplicades" no permetran cap excepció a les regles, les aplicacions, controladors, dll, etc. es bloquejaran si no compleixen.

### Polítiques disponibles:

- **XML:**
  - **Només auditoria:**
    - `WDAC_V1_Default_Audit_{versió}.xml`
    - `WDAC_V1_Recommended_Audit_{versió}.xml`
  - **Aplicat:**
    - `WDAC_V1_Default_Enforced_{versió}.xml`
    - `WDAC_V1_Recommended_Enforced_{versió}.xml`
- **BIN:**
  - **Només auditoria:**
    - `WDAC_V1_Default_Audit_{versió}.bin`
    - `WDAC_V1_Recommended_Audit_{versió}.bin`
  - **Aplicat:**
    - `WDAC_V1_Default_Enforced_{versió}.bin`
    - `WDAC_V1_Recommended_Enforced_{versió}.bin`
- **CIP:**
  - **Només auditoria:**
    - `WDAC_V1_Default_Audit\{uid}.cip`
    - `WDAC_V1_Recommended_Audit\{uid}.cip`
  - **Aplicat:**
    - `WDAC_V1_Default_Enforced\{uid}.cip`
    - `WDAC_V1_Recommended_Enforced\{uid}.cip`

Actualitzeu la línia següent a l'script per utilitzar la política que voleu localment:

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
