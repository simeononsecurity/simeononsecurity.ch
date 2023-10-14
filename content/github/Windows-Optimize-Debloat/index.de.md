---
title: "Optimieren Sie Ihren Windows-PC mit Windows-Optimize-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Verbessern Sie die Leistung und den Datenschutz Ihres Windows-Betriebssystems mit Windows-Optimize-Debloat, einem umfassenden Skript, das bei der Entfernung von Bloatware und der Optimierung der Systemeinstellungen hilft."
tags: ["Windows-Optimieren-Entbluten", "Windows-Optimierung", "Debloating Windows", "Windows beschleunigen", "Optimieren der Windows-Leistung", "Windows-Leistungssteigerung", "Windows-System-Optimierung", "Microsoft", "Datenschutz", "Bloatware-Entfernung", "Windows 10", "Fenster 11", "Windows Defender", "Windows Update", "Cortona", "Gruppenrichtlinien-Objekte", "Telemetrie", "Windows Store", "Windows 10 Professional", "Windows 10 Startseite"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Für diejenigen, die ihre Windows 10- und 11-Installationen minimieren möchten.

**Hinweis:** Dieses Skript sollte auf den meisten, wenn nicht allen Systemen problemlos funktionieren. Während [@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Führen Sie dieses Skript nicht aus, wenn Sie nicht verstehen, was es tut.

## Einführung:
Windows 10 und 11 sind von Haus aus ein invasives und unsicheres Betriebssystem.
Organisationen wie [Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) und andere haben Konfigurationsänderungen empfohlen, um das Windows 10-Betriebssystem zu optimieren und zu entschlacken. Diese Änderungen umfassen das Blockieren von Telemetrie, das Löschen von Protokollen und das Entfernen von Bloatware, um nur einige zu nennen. Dieses Skript zielt darauf ab, die von diesen Organisationen empfohlenen Konfigurationen zu automatisieren.

## Hinweise:
- Dieses Skript ist für den Einsatz in Umgebungen mit vorwiegend **Personal Use** konzipiert.
- Dieses Skript ist so konzipiert, dass die Optimierungen, im Gegensatz zu anderen Skripten, die Kernfunktionen von Windows nicht beeinträchtigen.
 - Funktionen wie Windows Update, Windows Defender, der Windows Store und Cortona wurden eingeschränkt, sind aber nicht in einem funktionsuntüchtigen Zustand wie die meisten anderen Windows 10 Privacy-Skripte.
- Wenn Sie ein minimiertes Skript suchen, das nur auf kommerzielle Umgebungen ausgerichtet ist, lesen Sie bitte dieses [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Anforderungen:
- [X] Windows 10/11 Enterprise, Windows 10 Professional oder Windows 10 Home
  - Windows Home lässt keine GPO-Konfigurationen zu.
    - Das Skript funktioniert trotzdem, aber nicht alle Einstellungen werden übernommen.
  - Windows "N" Editionen sind nicht getestet.
  - Führen Sie das [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) zur Aktualisierung und Überprüfung der letzten Hauptversion.

## Microsoft-Konto oder Xbox-Dienste reparieren:
Dies liegt daran, dass wir die Anmeldung bei Microsoft-Konten blockieren. Microsofts Telemetrie und Identitätszuordnung ist verpönt.
Wenn Sie diese Dienste dennoch nutzen möchten, finden Sie die Lösung in den folgenden Problemtickets:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## Eine Liste der Skripte und Werkzeuge, die diese Sammlung verwendet:
- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Zusätzliche Konfigurationen wurden berücksichtigt von:
- [BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
- [MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
- [Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
- [Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
- [Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
- [Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
- [Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
- [UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
- [Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
- [The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
- [TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
- [W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)

## So führen Sie das Skript aus:
### Automatisierte Installation:
Das Skript kann wie folgt aus dem extrahierten GitHub-Download gestartet werden:
```powershell
iwr -useb 'https://simeononsecurity.com/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### Manuelle Installation:
Wenn das Skript manuell heruntergeladen wird, muss es von einer administrativen Powershell in dem Verzeichnis gestartet werden, das alle Dateien aus dem [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

Das Skript "sos-optimize-windows.ps1" enthält mehrere Parameter, mit denen der Optimierungsprozess angepasst werden kann. Jeder Parameter ist ein boolescher Wert, der standardmäßig auf true gesetzt wird, wenn er nicht angegeben wird.

- **$cleargpos**: Löscht die Einstellungen von Gruppenrichtlinienobjekten.
- **$installupdates**: Installiert Updates auf dem System.
- **$removebloatware**: Entfernt unnötige Programme und Funktionen aus dem System.
- **$disabletelemetry**: Deaktiviert die Datenerfassung und Telemetrie.
- **$Privatsphäre**: Nimmt Änderungen zur Verbesserung der Privatsphäre vor.
- **$Bildbereinigung**: Entfernt nicht benötigte Dateien aus dem System.
- **$Festplattenkomprimierung**: Komprimiert die Systemfestplatte.
- **$updatemanagement**: Ändert die Art und Weise, wie Updates auf dem System verwaltet und verbessert werden.
- **$sosbrowsers**: Optimiert die Webbrowser des Systems.

Ein Beispiel für den Aufruf des Skripts mit bestimmten Parametern wäre:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

