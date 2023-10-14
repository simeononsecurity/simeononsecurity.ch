---
title: "Verbetering van Windows- en serversystemen: Custom Branding Setup Guide"
date: 2020-08-13
toc: true
draft: false
description: "Learn how to set up custom branding on Windows 10 and Server 2016/2019/2022 systems to personalize your user experience."
tags: ["Windows branding", "Server branding", "custom branding", "systeemaanpassing", "branding setup", "Windows 10", "Server 2016", "Server 2019", "Server 2022", "gebruikerservaring", "gids voor systeemaanpassing", "personalisatie", "systeembranding", "Aanpassing van Windows", "Aanpassing van de server", "OEM-logo", "gebruikersafbeelding", "gastbeeld", "branding script", "Microsoft Toolkit voor beveiligingsnaleving", "Windows branding instellen", "Server branding setup", "custom branding gids", "gepersonaliseerde branding", "handleiding systeemaanpassing", "Windows systeemaanpassing", "Aanpassing van het serversysteem", "merkbeelden", "beste praktijken voor branding", "Windows aanpassingstips", "Serveraanpassingstechnieken"]
---

**Setup branding op Windows 10 en Server 2016/2019/2022 Systemen**

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml)

## Hoe de branding bestanden in te stellen
- X] Vervang alle afbeeldingen door uw merkafbeeldingen
  - X] OEM logo moet 95x95 of 120x20 zijn en in ".bmp" formaat.
  - X] Genereer de User Image samen met 32x32, 40x40, 48x48, 192x192 varianten.
  - X] Genereer of kopieer de gebruikersafbeelding voor de gastafbeelding.
  
## Dit script gebruikt het volgende gereedschap:
- [Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Hoe het script uit te voeren
### Handmatig installeren:
Indien handmatig gedownload, moet het script worden gestart vanuit een administratieve powershell in de directory die alle bestanden van de [GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-copybranding.ps1
```
### Geautomatiseerde installatie:
Het script kan vanaf de uitgepakte GitHub-download als volgt worden gestart:
```powershell
iwr -useb 'https://simeononsecurity.com/scripts/sosbranding.ps1'|iex
```

