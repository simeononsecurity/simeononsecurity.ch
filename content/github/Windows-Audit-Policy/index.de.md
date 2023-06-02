---
title: "Maximierung der Windows-Überwachung mit dem Skript für die Windows-Überprüfungsrichtlinie"
date: 2021-05-10
toc: true
draft: false
description: "Erfahren Sie, wie Sie die Windows-Überwachung durch die Implementierung des Skripts für die Windows-Überwachungsrichtlinie optimieren können, um die Sicherheit und Überwachung zu verbessern."
tags: ["Windows Audit Policy", "Windows-Überprüfung", "Sicherheit", "Überwachung", "auditpol", "Windows-Befehle", "Windows-Sicherheit", "Konfigurationsaudit", "Sicherheitspolitik", "Ereignisprotokolle", "Systemüberwachung", "Windows-Server", "bewährte Sicherheitsverfahren", "Cybersicherheit", "Protokollanalyse", "Einhaltung der Sicherheitsvorschriften", "Vorfallreaktion", "Werkzeuge zur Sicherheitsüberwachung", "privilegierter Zugang", "Windows-Verwaltung", "Skripting", "Systemverwaltung", "Informationssicherheit", "Ordnungsmäßigkeitsprüfung", "Windows-Härtung", "Sicherheitskontrollen", "Sicherheitsautomatisierung", "Protokollverwaltung", "Windows-Sicherheitseinstellungen"]
---

## Windows-Audit-Policy

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml)

Windows-Überwachung ausreizen

## Empfohlenes Lesematerial:
  - [auditpol](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol)
  - [auditpol clear](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-clear)
  - [auditpol backup](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-backup)
  - [auditpol restore](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-restore)
  - [auditpol list](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-list)

## So führen Sie das Skript aus
### Manuelle Installation:
Wenn das Skript manuell heruntergeladen wird, muss es aus dem Verzeichnis gestartet werden, das alle anderen Dateien aus dem [GitHub Repository](https://github.com/simeononsecurity/Windows-Audit-Policy)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-auditpolicy.ps1
```
