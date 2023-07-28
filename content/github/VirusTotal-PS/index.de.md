---
title: "Effiziente Virenscans mit VirusTotal PowerShell-Modulen"
date: 2020-11-24
toc: true
draft: false
description: "Führen Sie mit den VirusTotal PowerShell-Modulen effiziente Virenscans durch, indem Sie die Interaktion mit der VirusTotal-API automatisieren und Ihren Sicherheits-Workflow rationalisieren."
tags: ["PowerShell-Module", "PowerShell", "Automatisierung", "VirusTotal", "Viren-Scans", "Domänen-Scans", "API-Schlüssel", "VirusTotal API", "VirusTotal-Entwickler-Seite", "Systemverwaltung", "Sicherheits-Workflow", "Effiziente Virenscans", "Herunterladen und Installieren", "GitHub-Repository", "API-Verwendungsbeispiele"]
---
 Sammlung von PowerShell-Modulen für die Interaktion mit der VirusTotal-API

**Hinweise:**
- Sie benötigen Ihren VirusTotal-API-Schlüssel, den Sie in Ihrem [Shodan Account](https://www.virustotal.com/gui/)
- Beispiele für die in den Modulen verwendeten APIs finden Sie auf der Website [VirusTotal Developers Page](https://developers.virustotal.com/reference#getting-started)

## Herunterladen und Installieren
- Laden Sie die Module von der Website [GitHub Repository](https://github.com/simeononsecurity/VirusTotal-PS)
- Installieren Sie alle Module
```ps
Get-ChildItem -Recurse *.ps1 | Import-Module
```