---
title: "Maximaliseer Windows Auditing met Windows Audit Policy Script"
date: 2021-05-10
toc: true
draft: false
description: "Leer hoe u Windows auditing kunt maximaliseren door het Windows Audit Policy script te implementeren om de beveiliging en monitoring te verbeteren."
tags: ["Windows controlebeleid", "Windows auditing", "beveiliging", "controle", "auditpol", "Windows commando's", "Windows beveiliging", "auditconfiguratie", "veiligheidsbeleid", "gebeurtenislogboeken", "systeemcontrole", "Windows server", "beste beveiligingspraktijken", "cyberbeveiliging", "logboekanalyse", "naleving van de veiligheidsvoorschriften", "reactie op incidenten", "tools voor veiligheidscontrole", "geprivilegieerde toegang", "Windows administratie", "scripting", "systeembeheer", "informatiebeveiliging", "nalevingscontrole", "Ramen verharden", "veiligheidscontroles", "veiligheidsautomatisering", "logboekbeheer", "Windows beveiligingsinstellingen"]
---

## Windows-Audit-Policy

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml)

Maximaliseren van Windows Auditing

## Aanbevolen leesmateriaal:
  - [auditpol](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol)
  - [auditpol clear](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-clear)
  - [auditpol backup](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-backup)
  - [auditpol restore](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-restore)
  - [auditpol list](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-list)

## Hoe het script uit te voeren
### Handmatig installeren:
Indien handmatig gedownload, moet het script gestart worden vanuit de map die alle andere bestanden van de [GitHub Repository](https://github.com/simeononsecurity/Windows-Audit-Policy)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-auditpolicy.ps1
```
