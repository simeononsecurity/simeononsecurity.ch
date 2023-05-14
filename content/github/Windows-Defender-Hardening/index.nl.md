---
title: "Windows 10 Beveiliging verbeteren met Defender Hardening Script"
date: 2020-11-15
toc: true
draft: false
description: "Leer hoe u de beveiliging van Windows 10 kunt verbeteren met een PowerShell-script dat Windows Defender Antivirus verhardt en alle vereisten van de Windows Defender Antivirus STIG V2R1 implementeert."
tags: ["Windows Defender", "Windows 10", "Windows 10 Beveiliging", "PowerShell Script", "Hardening", "Defender Hardening", "Veiligheid Automatisering", "Naleving", "Gecontroleerde toegang tot mappen", "Inbraakpreventie systeem", "Toepassingscontrole", "Vermindering van het aanvalsoppervlak", "Bescherming tegen uitbuiting", "Cloud-geleverde bescherming", "Netwerkbescherming", "Windows Defender STIG Script", "Windows Defender STIG", "Windows Defender Antivirus STIG V2R1", "WDAC", "ASR"]
---


## Wat doet dit script?
- Schakelt Cloud-delivered Protections in
- Gecontroleerde maptoegang inschakelen
- Schakelt netwerkbeveiliging in
- Schakelt Intrusion Prevention System in
-[Enables Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
-[Enables Windows Defender Attack Surface Reduction Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Enables Windows Defender Exploit Protections](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide#powershell)
- Voert alle in de[Windows Defender Antivirus STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)

## Vereisten:
- x] Windows 10 Enterprise (**Bij voorkeur**) of Windows 10 Professional.
  - Windows 10 Home staat geen GPO-configuraties of[ASR](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) 
Hoewel de meeste van deze configuraties nog steeds van toepassing zijn.
  - Windows 10 "N" Editions zijn niet getest.

## Download de benodigde bestanden:

Download de vereiste bestanden van de[GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)

## Hoe voer je het script uit:

**Het script kan worden gelanceerd vanaf de uitgepakte GitHub-download als volgt:**
```
.\sos-windowsdefenderhardening.ps1
```
