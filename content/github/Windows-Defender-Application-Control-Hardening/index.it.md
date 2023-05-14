---
title: "Guida completa per rafforzare Windows con Windows Defender Application Control WDAC"
date: 2020-12-16
toc: true
draft: false
description: "Scopri come usare Windows Defender Application Control WDAC per rafforzare il tuo sistema operativo Windows con script e strumenti."
tags: ["Protezione avanzata WDAC per il controllo delle applicazioni di Windows Defender", "PowerShell", "Script di PowerShell", "Automazione", "Conformità", "Squadra blu", "Script di Windows Defender STIG", "Rafforzamento di Windows Defender", "Windows Defender STIG", "Difensore SIG", "Protezione dagli exploit di Windows Defender WDEP", "ASR per la riduzione della superficie di attacco di Windows Defender", "Windows Server 2016 2019", "Nucleo di Windows Server", "Toolkit Microsoft WDAC", "Aggiorna criterio CI", "Regole di blocco consigliate da Microsoft", "Regole di blocco dei driver consigliate da Microsoft", "Politiche XML", "Politiche BIN", "Politica di gruppo", "MicrosoftIntune"]
---

**Rafforzare Windows con Windows Defender Application Control WDAC**

## Appunti:
- Windows Server 2016/2019 o qualsiasi versione precedente alla 1903 supporta solo un singolo criterio legacy alla volta.
- L'edizione Windows Server Core supporta WDAC ma alcuni componenti che dipendono da AppLocker non funzioneranno
- Si prega di leggere il[Recommended Reading](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening#recommended-reading) prima di implementare o addirittura testare.

## Un elenco di script e strumenti utilizzati da questa raccolta:

-[MicrosoftDocs - WDAC-Toolkit](https://github.com/MicrosoftDocs/WDAC-Toolkit)
-[Microsoft - Refresh CI Policy ](https://www.microsoft.com/en-us/download/details.aspx?id=102925)

## Ulteriori configurazioni sono state prese in considerazione da:

-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)

## Spiegazione:

### XML rispetto a BIN:

- In poche parole, i criteri **"XML"** servono per l'applicazione a una macchina in locale e i file **"BIN"** servono per applicarli con entrambi[Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) or [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) Sebbene sia possibile utilizzare i criteri XML, BIN o CIP in una distribuzione locale, in generale è necessario attenersi a XML ove possibile e in particolare durante il controllo o la risoluzione dei problemi.

### Descrizioni dei criteri:

- **Criteri predefiniti:**
  - I criteri "predefiniti" utilizzano solo le funzionalità predefinite disponibili nel WDAC-Toolkit.
- **Norme consigliate:**
  - I criteri "Consigliati" utilizzano le funzionalità predefinite oltre a quelle consigliate da Microsoft[blocks](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules) and [driver block](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules) regole.
- **Politiche di controllo:**
  - Le politiche "Audit", registrano solo le eccezioni alle regole. Questo è per il test nel tuo ambiente, in modo che tu possa modificare le politiche, a piacimento, per soddisfare le esigenze dei tuoi ambienti.
- **Norme applicate:**
  - Le policy "Enforced" non consentiranno alcuna eccezione alle regole, applicazioni, driver, dll, ecc. saranno bloccati se non conformi.

### Politiche disponibili:

- **XML:**
  - **Solo controllo:**
    - `WDAC_V1_Default_Audit_{versione}.xml`
    - `WDAC_V1_Recommended_Audit_{versione}.xml`
  - **Forzata:**
    - `WDAC_V1_Default_Enforced_{versione}.xml`
    - `WDAC_V1_Recommended_Enforced_{versione}.xml`
- **BIDONE:**
  - **Solo controllo:**
    - `WDAC_V1_Default_Audit_{versione}.bin`
    - `WDAC_V1_Recommended_Audit_{versione}.bin`
  - **Forzata:**
    - `WDAC_V1_Default_Enforced_{versione}.bin`
    - `WDAC_V1_Recommended_Enforced_{versione}.bin`
- **PIC:**
  - **Solo controllo:**
    - `WDAC_V1_Default_Audit\{uid}.cip`
    - `WDAC_V1_Recommended_Audit\{uid}.cip`
  - **Forzata:**
    - `WDAC_V1_Default_Enforced\{uid}.cip`
    - `WDAC_V1_Recommended_Enforced\{uid}.cip`

Aggiorna la seguente riga nello script per utilizzare la policy che desideri localmente:

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
