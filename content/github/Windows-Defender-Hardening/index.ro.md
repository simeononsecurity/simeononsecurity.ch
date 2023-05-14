---
title: "Îmbunătățirea securității Windows 10 cu Defender Hardening Script"
date: 2020-11-15
toc: true
draft: false
description: "Aflați cum să îmbunătățiți securitatea Windows 10 cu un script PowerShell care întărește Windows Defender Antivirus, implementând toate cerințele Windows Defender Antivirus STIG V2R1."
tags: ["Windows Defender", "Windows 10", "Securitate Windows 10", "Script PowerShell", "întărire", "Defender Hardening", "Automatizare de securitate", "Conformitate", "Acces controlat la foldere", "Sistem de prevenire a intruziunilor", "Controlul aplicației", "Reducerea suprafeței de atac", "Exploat Protections", "Protecții furnizate în cloud", "Protecții de rețea", "Windows Defender STIG Script", "Windows Defender STIG", "Windows Defender Antivirus STIG V2R1", "WDAC", "ASR"]
---


## Ce face acest script?
- Activează protecțiile furnizate în cloud
- Activează accesul controlat la foldere
- Activează protecția rețelei
- Activează sistemul de prevenire a intruziunilor
-[Enables Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
-[Enables Windows Defender Attack Surface Reduction Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Enables Windows Defender Exploit Protections](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide#powershell)
- Implementează toate cerințele enumerate în[Windows Defender Antivirus STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)

## Cerințe:
- [x] Windows 10 Enterprise (**Preferabil**) sau Windows 10 Professional
  - Windows 10 Home nu permite configurații GPO sau[ASR](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) 
Deși majoritatea acestor configurații se vor aplica în continuare.
  - Windows 10 Edițiile „N” nu sunt testate.

## Descărcați fișierele necesare:

Descărcați fișierele necesare din[GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)

## Cum se rulează scriptul:

**Scriptul poate fi lansat din descărcarea GitHub extrasă astfel:**
```
.\sos-windowsdefenderhardening.ps1
```
