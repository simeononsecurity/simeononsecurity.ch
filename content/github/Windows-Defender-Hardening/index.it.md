---
title: "Miglioramento della sicurezza di Windows 10 con Defender Hardening Script"
date: 2020-11-15
toc: true
draft: false
description: "Scopri come migliorare la sicurezza di Windows 10 con uno script PowerShell che rafforza Windows Defender Antivirus, implementando tutti i requisiti di Windows Defender Antivirus STIG V2R1."
tags: ["Difensore di Windows", "Windows 10", "Sicurezza di Windows 10", "Script di PowerShell", "Indurimento", "Indurimento del difensore", "Automazione della sicurezza", "Conformità", "Accesso controllato alle cartelle", "Sistema anti-intrusione", "Controllo delle applicazioni", "Riduzione della superficie di attacco", "Protezioni dagli exploit", "Protezioni fornite dal cloud", "Protezioni di rete", "Script di Windows Defender STIG", "Windows Defender STIG", "Windows Defender Antivirus STIG V2R1", "WDAC", "RSA"]
---


## Cosa fa questo script?
- Abilita le protezioni fornite dal cloud
- Abilita l'accesso controllato alle cartelle
- Abilita le protezioni di rete
- Abilita il sistema di prevenzione delle intrusioni
-[Enables Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
-[Enables Windows Defender Attack Surface Reduction Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Enables Windows Defender Exploit Protections](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide#powershell)
- Implementa tutti i requisiti elencati nella[Windows Defender Antivirus STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)

## Requisiti:
- [x] Windows 10 Enterprise (**Preferito**) o Windows 10 Professional
  - Windows 10 Home non consente configurazioni GPO o[ASR](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) 
Sebbene la maggior parte di queste configurazioni sarà ancora valida.
  - Le edizioni "N" di Windows 10 non sono testate.

## Scarica i file richiesti:

Scarica i file richiesti dal file[GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)

## Come eseguire lo script:

**Lo script può essere avviato dal download GitHub estratto in questo modo:**
```
.\sos-windowsdefenderhardening.ps1
```
