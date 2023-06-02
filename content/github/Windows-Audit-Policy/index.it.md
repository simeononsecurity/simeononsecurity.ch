---
title: "Massimizzate l'audit di Windows con lo script Criteri di audit di Windows"
date: 2021-05-10
toc: true
draft: false
description: "Scoprite come massimizzare l'auditing di Windows implementando lo script Criteri di controllo di Windows per migliorare la sicurezza e il monitoraggio."
tags: ["Criteri di audit di Windows", "Audit di Windows", "sicurezza", "monitoring", "auditpol", "Comandi di Windows", "Sicurezza di Windows", "configurazione di audit", "politiche di sicurezza", "log degli eventi", "monitoraggio del sistema", "Server Windows", "migliori pratiche di sicurezza", "sicurezza informatica", "analisi dei log", "conformità alla sicurezza", "risposta agli incidenti", "strumenti di monitoraggio della sicurezza", "accesso privilegiato", "Amministrazione di Windows", "scripting", "amministrazione del sistema", "sicurezza delle informazioni", "audit di conformità", "Indurimento delle finestre", "controlli di sicurezza", "automazione della sicurezza", "gestione dei log", "Impostazioni di sicurezza di Windows"]
---

## Windows-Audit-Policy

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml)

Massimizzare l'audit di Windows

## Materiale di lettura consigliato:
  - [auditpol](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol)
  - [auditpol clear](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-clear)
  - [auditpol backup](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-backup)
  - [auditpol restore](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-restore)
  - [auditpol list](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-list)

## Come eseguire lo script
### Installazione manuale:
Se scaricato manualmente, lo script deve essere lanciato dalla directory contenente tutti gli altri file del file [GitHub Repository](https://github.com/simeononsecurity/Windows-Audit-Policy)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-auditpolicy.ps1
```
