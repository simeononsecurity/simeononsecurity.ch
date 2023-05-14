---
title: "Verbessern der Windows 10-Sicherheit mit Defender Hardening Script"
date: 2020-11-15
toc: true
draft: false
description: "Erfahren Sie, wie Sie die Sicherheit von Windows 10 mit einem PowerShell-Skript verbessern, das Windows Defender Antivirus härtet und alle Anforderungen von Windows Defender Antivirus STIG V2R1 implementiert."
tags: ["Windows Defender", "Windows 10", "Windows 10-Sicherheit", "PowerShell-Skript", "Härten", "Verteidiger-Härtung", "Sicherheitsautomatisierung", "Einhaltung", "Kontrollierter Ordnerzugriff", "Angrifferkennungssystem", "Anwendungssteuerung", "Reduzierung der Angriffsfläche", "Exploit-Schutz", "Cloud-basierter Schutz", "Netzwerkschutz", "Windows Defender STIG-Skript", "Windows Defender STIG", "Windows Defender Antivirus STIG V2R1", "WDAC", "ASR"]
---


## Was macht dieses Skript?
- Ermöglicht cloudbasierte Schutzmaßnahmen
- Ermöglicht kontrollierten Ordnerzugriff
- Aktiviert Netzwerkschutz
- Aktiviert das Intrusion Prevention System
-[Enables Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
-[Enables Windows Defender Attack Surface Reduction Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Enables Windows Defender Exploit Protections](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide#powershell)
- Setzt alle in aufgeführten Anforderungen um[Windows Defender Antivirus STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)

## Anforderungen:
- [x] Windows 10 Enterprise (**Bevorzugt**) oder Windows 10 Professional
  - Windows 10 Home erlaubt keine GPO-Konfigurationen oder[ASR](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) 
Die meisten dieser Konfigurationen gelten jedoch weiterhin.
  - Windows 10 „N“-Editionen werden nicht getestet.

## Laden Sie die erforderlichen Dateien herunter:

Laden Sie die erforderlichen Dateien herunter[GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)

## So führen Sie das Skript aus:

**Das Skript kann wie folgt aus dem extrahierten GitHub-Download gestartet werden:**
```
.\sos-windowsdefenderhardening.ps1
```
