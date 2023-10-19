---
title: "Verbesserung von Windows- und Serversystemen: Leitfaden für die Einrichtung des benutzerdefinierten Brandings"
date: 2020-08-13
toc: true
draft: false
description: "Learn how to set up custom branding on Windows 10 and Server 2016/2019/2022 systems to personalize your user experience."
tags: ["Windows-Branding", "Server-Branding", "kundenspezifisches Branding", "Systemanpassung", "Branding-Setup", "Windows 10", "Server 2016", "Server 2019", "Server 2022", "Benutzererfahrung", "Anleitung zur Systemanpassung", "Personalisierung", "System-Branding", "Windows-Anpassung", "Server-Anpassung", "OEM-Logo", "Benutzerbild", "Gastbild", "Branding-Skript", "Microsoft Security Compliance Toolkit", "Einrichtung des Windows-Brandings", "Einrichtung des Server-Brandings", "Leitfaden für individuelles Branding", "personalisiertes Branding", "Anleitung zur Systemanpassung", "Anpassung des Windows-Systems", "Anpassung des Serversystems", "Branding-Bilder", "bewährte Praktiken der Markenführung", "Tipps zur Anpassung von Windows", "Techniken zur Serveranpassung"]
---

**Setup Branding auf Windows 10 und Server 2016/2019/2022 Systemen**

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml)

## So richten Sie die Branding-Dateien ein
- X] Ersetzen Sie alle Bilder durch Ihre Branding-Bilder
  - X] Das OEM-Logo muss entweder 95x95 oder 120x20 groß sein und im Format ".bmp" vorliegen.
  - X] Generieren Sie das Benutzerbild zusammen mit den Varianten 32x32, 40x40, 48x48, 192x192.
  - X] Erzeugen oder kopieren Sie das Benutzerbild für das Gastbild.
  
## Dieses Skript verwendet das folgende Tool:
- [Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## So führen Sie das Skript aus
### Manuelle Installation:
Wenn das Skript manuell heruntergeladen wird, muss es von einer administrativen Powershell aus in dem Verzeichnis gestartet werden, das alle Dateien aus der [GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-copybranding.ps1
```
### Automatisierte Installation:
Das Skript kann aus dem extrahierten GitHub-Download wie folgt gestartet werden:
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/sosbranding.ps1'|iex
```

