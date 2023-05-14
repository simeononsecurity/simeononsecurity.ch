---
title: "Optimieren Sie Ihren Windows-PC mit Windows-Optimize-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Verbessern Sie die Leistung und den Datenschutz Ihres Windows-Betriebssystems mit Windows-Optimize-Debloat, einem umfassenden Skript, das dabei hilft, Bloatware zu entfernen und Systemeinstellungen zu optimieren."
tags: ["Windows-Optimize-Debloat", "Windows-Optimierung", "Windows entblößen", "Beschleunigen Sie Windows", "Optimieren Sie die Windows-Leistung", "Windows-Leistungssteigerung", "Windows-Systemoptimierung", "Microsoft", "Privatsphäre", "Bloatware-Entfernung", "Windows 10", "Windows 11", "Windows Defender", "Windows Update", "Cortona", "Gruppenrichtlinienobjekte", "Telemetrie", "Windows Store", "Windows 10 Professional", "Windows 10 Home"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Für diejenigen, die ihre Windows 10- und 11-Installationen minimieren möchten.*

**Hinweis:** Dieses Skript sollte auf den meisten, wenn nicht allen, Systemen ohne Probleme funktionieren. Während[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Führen Sie dieses Skript nicht aus, wenn Sie nicht verstehen, was es tut.

## Einführung:
Windows 10 und 11 sind standardmäßig invasive und unsichere Betriebssysteme.
Organisationen mögen[Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) und andere haben Konfigurationsänderungen empfohlen, um das Betriebssystem Windows 10 zu optimieren und zu entlasten. Zu diesen Änderungen gehören unter anderem das Blockieren von Telemetriedaten, das Löschen von Protokollen und das Entfernen von Bloatware. Dieses Skript zielt darauf ab, die von diesen Organisationen empfohlenen Konfigurationen zu automatisieren.

## Anmerkungen:
– Dieses Skript ist hauptsächlich für den Einsatz in Umgebungen zur **persönlichen Nutzung** konzipiert.
– Dieses Skript ist so konzipiert, dass die Optimierungen im Gegensatz zu einigen anderen Skripten die Kernfunktionen von Windows nicht beeinträchtigen.
 – Funktionen wie Windows Update, Windows Defender, der Windows Store und Cortona wurden eingeschränkt, befinden sich jedoch nicht in einem gestörten Zustand wie die meisten anderen Windows 10-Datenschutzskripte.
- Wenn Sie ein minimiertes Skript suchen, das nur für kommerzielle Umgebungen gedacht ist, sehen Sie sich bitte dieses an[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Anforderungen:
- [X] Windows 10/11 Enterprise, Windows 10 Professional oder Windows 10 Home
  - Windows Home erlaubt keine GPO-Konfigurationen.
    - Das Skript funktioniert weiterhin, es werden jedoch nicht alle Einstellungen angewendet.
  - Windows „N“-Editionen werden nicht getestet.
  - Führen Sie das aus[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) um die neueste Hauptversion zu aktualisieren und zu überprüfen.

## Microsoft-Konto oder Xbox-Dienste reparieren:
Dies liegt daran, dass wir die Anmeldung bei Microsoft-Konten blockieren. Die Telemetrie- und Identitätszuordnung von Microsoft ist verpönt.
Wenn Sie diese Dienste dennoch nutzen möchten, sehen Sie sich die folgenden Problemtickets zur Lösung an:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## Eine Liste der Skripte und Tools, die diese Sammlung verwendet:
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Zusätzliche Konfigurationen wurden berücksichtigt von:
-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)

## So führen Sie das Skript aus:
### Automatisierte Installation:
Das Skript kann wie folgt über den extrahierten GitHub-Download gestartet werden:
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### Manual Install:
If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

The script "sos-optimize-windows.ps1" includes several parameters that allow for customization of the optimization process. Each parameter is a boolean value that defaults to true if not specified.

- **$cleargpos**: Clears Group Policy Objects settings.
- **$installupdates**: Installs updates to the system.
- **$removebloatware**: Removes unnecessary programs and features from the system.
- **$disabletelemetry**: Disables data collection and telemetry.
- **$privacy**: Makes changes to improve privacy.
- **$imagecleanup**: Cleans up unneeded files from the system.
- **$diskcompression**: Compresses the system disk.
- **$updatemanagement**: Changes the way updates are managed and improved on the system.
- **$sosbrowsers**: Optimizes the system's web browsers.

An example of how to launch the script with specific parameters would be:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

