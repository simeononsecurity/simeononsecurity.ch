---
title: "Zwiększanie bezpieczeństwa systemu Windows 10 za pomocą skryptu Defender Hardening Script"
date: 2020-11-15
toc: true
draft: false
description: "Dowiedz się, jak zwiększyć bezpieczeństwo systemu Windows 10 za pomocą skryptu PowerShell, który utwardza Windows Defender Antivirus, implementując wszystkie wymagania Windows Defender Antivirus STIG V2R1."
tags: ["Windows Defender", "Windows 10", "Bezpieczeństwo systemu Windows 10", "Skrypt PowerShell", "Hartowanie", "Utwardzenie Defendera", "Automatyka zabezpieczeniowa", "Zgodność", "Kontrolowany dostęp do folderów", "System zapobiegania włamaniom", "Kontrola stosowania", "Redukcja powierzchni ataku", "Zabezpieczenia przed exploitami", "Zabezpieczenia dostarczane w chmurze", "Zabezpieczenia sieci", "Windows Defender STIG Script", "Windows Defender STIG", "Windows Defender Antivirus STIG V2R1", "WDAC", "ASR"]
---


## Co robi ten skrypt?
- Włącza zabezpieczenia dostarczane w chmurze
- Włącza kontrolowany dostęp do folderów
- Włącza ochronę sieci
- Włącza system zapobiegania włamaniom
-[Enables Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
-[Enables Windows Defender Attack Surface Reduction Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Enables Windows Defender Exploit Protections](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide#powershell)
- Wprowadza wszystkie wymagania wymienione w[Windows Defender Antivirus STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)

## Wymagania:
- [x] Windows 10 Enterprise (**Preferowany**) lub Windows 10 Professional.
  - Windows 10 Home nie pozwala na konfiguracje GPO lub[ASR](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) 
Choć większość z tych konfiguracji nadal będzie miała zastosowanie.
  - Windows 10 "N" Editions nie jest testowany.

## Pobierz wymagane pliki:

Pobierz wymagane pliki ze strony.[GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)

## Jak uruchomić skrypt:

**Skrypt może być lauched z wyodrębnionego GitHub downloadu w ten sposób:**.
```
.\sos-windowsdefenderhardening.ps1
```
