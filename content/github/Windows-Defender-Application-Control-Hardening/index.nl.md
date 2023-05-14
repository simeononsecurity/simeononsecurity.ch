---
title: "Complete gids voor het afschermen van Windows met Windows Defender Application Control WDAC"
date: 2020-12-16
toc: true
draft: false
description: "Leer hoe u Windows Defender Application Control WDAC kunt gebruiken om uw Windows-besturingssysteem te harden met scripts en tools."
tags: ["Windows Defender Application Control WDAC-verharding", "PowerShell", "PowerShell Script", "Automatisering", "Naleving", "Blue-Team", "Windows Defender STIG Script", "Windows Defender Hardening", "Windows Defender STIG", "Verdediger STIG", "Windows Defender Exploitbescherming WDEP", "Windows Defender Beperking van het aanvalsoppervlak ASR", "Windows Server 2016 2019", "Windows Server Core", "Microsoft WDAC Toolkit", "Vernieuwen CI-beleid", "Door Microsoft aanbevolen blokkeringsregels", "Door Microsoft aanbevolen regels voor het blokkeren van stuurprogramma's", "XML-beleid", "BIN-beleid", "Groepsbeleid", "Microsoft Intune"]
---

**Versterk Windows met Windows Defender Application Control WDAC**

## Opmerkingen:
- Windows Server 2016/2019 of alles vóór versie 1903 ondersteunen slechts één legacybeleid tegelijk.
- Windows Server Core editie ondersteunt WDAC, maar sommige onderdelen die afhankelijk zijn van AppLocker zullen niet werken.
- Lees de[Recommended Reading](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening#recommended-reading) alvorens te implementeren of zelfs te testen.

## Een lijst van scripts en gereedschappen die deze collectie gebruikt:

-[MicrosoftDocs - WDAC-Toolkit](https://github.com/MicrosoftDocs/WDAC-Toolkit)
-[Microsoft - Refresh CI Policy ](https://www.microsoft.com/en-us/download/details.aspx?id=102925)

## Aanvullende configuraties werden overwogen van:

-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)

## Verklaring:

### XML vs. BIN:

- Simpel gezegd zijn de **"XML"** beleidsregels om lokaal op een machine toe te passen en de **"BIN"** bestanden om ze af te dwingen met ofwel[Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) or [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) Hoewel u XML-, BIN- of CIP-beleid kunt gebruiken in een lokale implementatie, moet u het in het algemeen waar mogelijk bij XML houden, vooral bij audits en probleemoplossing.

### Beleidsbeschrijvingen:

- **Standaardbeleid:**
  - De "Standaard" policies gebruiken alleen de standaard functies die beschikbaar zijn in de WDAC-Toolkit.
- **Aanbevolen beleid:**
  - De "Aanbevolen" beleidsregels gebruiken de standaardfuncties en de aanbevolen functies van Microsoft.[blocks](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules) and [driver block](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules) regels.
- **Audit Policies:**
  - Het "Audit"-beleid logt alleen uitzonderingen op de regels. Dit is om te testen in uw omgeving, zodat u het beleid naar believen kunt aanpassen aan de behoeften van uw omgeving.
- Afgedwongen beleid:**
  - De "Enforced" policies staan geen uitzonderingen toe op de regels, applicaties, drivers, dlls, etc. worden geblokkeerd als ze niet voldoen.

### Beschikbare beleidsregels:

- XML:**
  - **Alleen controle:**
    -`WDAC_V1_Default_Audit_{version}.xml`
    -`WDAC_V1_Recommended_Audit_{version}.xml`
  - **Ontslagen:**
    -`WDAC_V1_Default_Enforced_{version}.xml`
    -`WDAC_V1_Recommended_Enforced_{version}.xml`
- **BIN:**
  - **Alleen controle:**
    -`WDAC_V1_Default_Audit_{version}.bin`
    -`WDAC_V1_Recommended_Audit_{version}.bin`
  - **Ontslagen:**
    -`WDAC_V1_Default_Enforced_{version}.bin`
    -`WDAC_V1_Recommended_Enforced_{version}.bin`
- **CIP:**
  - **Alleen controle:**
    -`WDAC_V1_Default_Audit\{uid}.cip`
    -`WDAC_V1_Recommended_Audit\{uid}.cip`
  - **Ontslagen:**
    -`WDAC_V1_Default_Enforced\{uid}.cip`
    -`WDAC_V1_Recommended_Enforced\{uid}.cip`

Pas de volgende regel in het script aan om het lokaal gewenste beleid te gebruiken:

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

U kunt ook[Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) or [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) om het WDAC-beleid te handhaven.

## Auditing:

U kunt de WDAC-gebeurtenislogboeken bekijken in gebeurtenisviewer onder:

`Applications and Services Logs\Microsoft\Windows\CodeIntegrity\Operational`

## Aanbevolen lectuur:

-[Argonsys - Deploying Windows 10 Application Control Policy](https://argonsys.com/microsoft-cloud/library/deploying-windows-10-application-control-policy/)
-[Microsoft - Audit Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/audit-windows-defender-application-control-policies)
-[Microsoft - Create a WDAC policy for fixed-workload devices using a reference computer](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
-[Microsoft - Deploy Windows Defender Application Control policies by using Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy)
-[Microsoft - Deploy Windows Defender Application Control policies by using Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune)
-[Microsoft - Deploy WDAC policies using script](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
-[Microsoft - Enforce Windows Defencer Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/enforce-windows-defender-application-control-policies)
-[Microsoft - Guidance on Creating WDAC Deny Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
-[Microsoft - Use multiple Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)

## Hoe voer je het script uit:

### Handmatig installeren:

Indien handmatig gedownload, moet het script gestart worden vanuit een administratieve powershell in de directory die alle bestanden van de[GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening/archive/main.zip)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-wdachardening.ps1
```
