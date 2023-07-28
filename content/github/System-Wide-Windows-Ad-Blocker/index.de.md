---
title: "Windows 10 Systemweites Werbeblocker-Skript für mehr Datenschutz und Sicherheit"
date: 2021-04-02
toc: true
draft: false
description: "Blockieren Sie Werbung, Tracker und Telemetrie unter Windows 10 mit diesem leistungsstarken PowerShell-Skript, das die Hosts-Datei und die Windows-Firewall zum systemweiten Blockieren von Werbung nutzt."
tags: ["Windows 10", "Werbeblocker", "Telemetrieblockierung", "PowerShell-Skript", "systemweiter Werbeblocker", "Datenschutz", "Sicherheit", "EasyList", "Einfacher Datenschutz", "NoCoin Filter List", "AdGuard DNS-Filter", "YoYo-Listen", "Peter Lowes Ad-Tracking-Malware-Server", "Windows Firewall", "Domänenlisten", "Windows-Tracker blockieren", "Block-Tracker", "Anzeigen blockieren", "Blockverfolgung"]
---

**System-Wide-Windows-Ad-Blocker**

[![VirusTotal Scan](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/actions/workflows/virustotal.yml)

Dieses Skript ist ein Windows PowerShell-Skript, das die Datei "StevenBlack/hosts" herunterlädt und auf die "hosts"-Datei des Systems anwendet, mit der bestimmte Domänen/Websites blockiert werden können, indem sie einer IP-Adresse Ihrer Wahl zugeordnet werden (in der Regel die IP-Adresse des lokalen Computers). Das Skript überprüft die Internetverbindung und die Proxy-Einstellungen und versucht, die neueste Version der "hosts"-Datei von zwei verschiedenen Quellen herunterzuladen: "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts" und "http://sbc.io/hosts/hosts". Schlägt der Download fehl, fährt das Skript mit einer lokalen Kopie der "hosts"-Datei fort. Das Skript erfordert zur Ausführung erhöhte Rechte und ändert den Registrierungsschlüssel ".NETFramework", um nur die neueste Version des .NET-Frameworks zu verwenden.

*Wir sind an allen Kommentaren und Bedenken zu diesem Repo interessiert. Bitte senden Sie eine [issue](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues) mit allen Informationen, die Sie haben.

### Verwendete Listen:
- [StevenBlack/hosts - adware + malware](https://github.com/StevenBlack/hosts)

### Beispiel:
#### Manuelle Installation:
**Das Skript kann aus dem extrahierten GitHub-Download wie folgt gestartet werden:**
```powershell
.\sos-system-wide-windows-ad-block.ps1
```
#### Automatisch installieren:
Führen Sie die neueste Version des Skripts automatisch aus:
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/soswindowsadblocker.ps1' | iex
```

