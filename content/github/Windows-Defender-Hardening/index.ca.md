---
title: "Millora de la seguretat de Windows 10 amb Defender Hardening Script"
date: 2020-11-15
toc: true
draft: false
description: "Apreneu a millorar la seguretat de Windows 10 amb un script de PowerShell que endurisca l'antivirus Windows Defender, implementant tots els requisits de l'antivirus Windows Defender STIG V2R1."
tags: ["Windows Defender", "Windows 10", "Seguretat de Windows 10", "Script de PowerShell", "Enduriment", "Enduriment del defensor", "Automatització de seguretat", "Compliment", "Accés controlat a la carpeta", "Sistema de prevenció d'intrusions", "Control d'aplicacions", "Reducció de superfície d'atac", "Proteccions d'explotació", "Proteccions al núvol", "Proteccions de xarxa", "Windows Defender STIG Script", "Windows Defender STIG", "Windows Defender Antivirus STIG V2R1", "WDAC", "ASR"]
---


## Què fa aquest guió?
- Habilita les proteccions lliurades al núvol
- Habilita l'accés controlat a les carpetes
- Activa les proteccions de xarxa
- Habilita el sistema de prevenció d'intrusions
-[Enables Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
-[Enables Windows Defender Attack Surface Reduction Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Enables Windows Defender Exploit Protections](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide#powershell)
- Implementa tots els requisits enumerats a la[Windows Defender Antivirus STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)

## Requisits:
- [x] Windows 10 Enterprise (**Preferit**) o Windows 10 Professional
  - Windows 10 Home no permet configuracions GPO o[ASR](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) 
Tot i que la majoria d'aquestes configuracions encara s'aplicaran.
  - Les edicions "N" de Windows 10 no estan provades.

## Baixeu els fitxers necessaris:

Baixeu els fitxers necessaris des del[GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)

## Com executar l'script:

**L'script es pot llançar des de la descàrrega de GitHub extreta així:**
```
.\sos-windowsdefenderhardening.ps1
```
