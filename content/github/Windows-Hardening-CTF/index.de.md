---
title: "Windows Hardening CTF: Verstärken Sie die Sicherheit Ihres Windows-Geräts für Capture the Flag-Events"
date: 2020-10-19
toc: true
draft: false
description: "Entdecken Sie ein leistungsfähiges Skript, das die Sicherheit von Windows durch die Implementierung verschiedener Härtungsmaßnahmen erhöht, um Kompromisse zu verhindern."
tags: ["Windows-Härtung", "Windows-Sicherheit", "Skript", "Windows-Gerät", "Eingabeaufforderung", "LLMNR", "PowerShell", "SMB", "TCP-Zeitstempel", "AppLocker", "Windows-Protokollierung", "DEP", "EMET-Konfigurationen", "Eingeschränkter PowerShell-Sprachmodus", "SMB-Verschlüsselung", "Abhilfemaßnahmen für Spectre und Meltdown", "Windows Defender", "Windows Firewall", "PSWindowsUpdate", "Windows-Updates", "Härtungsskript", "Empfohlene NSA-Richtlinien", "Windows-Protokollierung und Sicherheitskontrollen", "Windows Defender Anwendungssteuerung", "Verfahren zur Reduzierung der Angriffsfläche von Windows Defender", "Windows Defender Cloud-basierte Schutzmaßnahmen", "Windows Defender Exploit-Schutz", "PSWindowsUpdate-Installation", "Verbesserung der Sicherheit von Windows-Geräten", "Maßnahmen zur Härtung von Windows", "Stärkung der Windows-Sicherheit"]
---

**Windows-Hardening-CTF**
Ein Windows-Hardening-Skript, das es schwieriger und lästiger macht, ein Windows-Gerät zu kompromittieren.

## Was macht dieses Skript?
- Deaktiviert die Eingabeaufforderung
- Deaktiviert LLMNR
- Deaktiviert PowerShell v2
- Deaktiviert SMB-Komprimierung
- Deaktiviert SMB v1
- Deaktiviert SMB v2
- Deaktiviert TCP-Zeitstempel
- Deaktiviert WSMAN und PSRemoting
- Aktiviert AppLocker mit den empfohlenen NSA-Richtlinien
- Aktiviert Best Practice Windows Logging und Sicherheitskontrollen
- Aktiviert DEP
- Aktiviert EMET-Konfigurationen (gilt nur für Systeme mit installiertem EMET)
- Aktiviert den PowerShell-Sprachmodus (Constrined Language Mode)
- Ermöglicht PowerShell-Protokollierung
- Aktiviert SMB-Verschlüsselung
- Aktiviert Spectre- und Meltdown-Abschwächungen
- Ermöglicht Windows Defender-Anwendungskontrolle
- Ermöglicht Windows Defender-Verfahren zur Reduzierung der Angriffsfläche
- Ermöglicht Windows Defender Cloud-basierte Schutzmaßnahmen
- Ermöglicht Windows Defender Exploit-Schutz
- Aktiviert Windows Firewall und Protokollierung
- Installiert PSWindowsUpdate und installiert alle verfügbaren Windows-Updates

## Laden Sie die erforderlichen Dateien herunter:

Laden Sie die erforderlichen Dateien von der [GitHub Repository](https://github.com/simeononsecurity/Windows-Hardening-CTF)

## So führen Sie das Skript aus:

**Das Skript kann aus dem extrahierten GitHub-Download wie folgt gestartet werden:**
```
.\sos-windows-hardening-ctf.ps1
```
