---
title: "Maximizați auditarea Windows cu Windows Audit Policy Script"
date: 2021-05-10
toc: true
draft: false
description: "Aflați cum să maximizați auditul Windows prin implementarea scriptului Windows Audit Policy pentru a îmbunătăți securitatea și monitorizarea."
tags: ["Politica de audit Windows", "Auditul Windows", "securitate", "monitorizare", "auditpol", "Comenzi Windows", "Securitatea Windows", "configurația de audit", "politici de securitate", "jurnalele de evenimente", "monitorizarea sistemului", "Server Windows", "cele mai bune practici de securitate", "securitate cibernetică", "analiza jurnalului", "conformitatea securității", "răspunsul la incidente", "instrumente de monitorizare a securității", "acces privilegiat", "Administrare Windows", "scripting", "administrarea sistemului", "securitatea informațiilor", "auditul de conformitate", "Întărirea ferestrelor", "controale de securitate", "automatizarea securității", "gestionarea jurnalelor", "Setări de securitate Windows"]
---

## Windows-Audit-Policy

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml)

Maximizați auditul Windows

## Materiale de lectură recomandate:
  - [auditpol](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol)
  - [auditpol clear](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-clear)
  - [auditpol backup](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-backup)
  - [auditpol restore](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-restore)
  - [auditpol list](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-list)

## Cum se execută scriptul
### Instalare manuală:
În cazul în care este descărcat manual, scriptul trebuie lansat din directorul care conține toate celelalte fișiere de la [GitHub Repository](https://github.com/simeononsecurity/Windows-Audit-Policy)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-auditpolicy.ps1
```
