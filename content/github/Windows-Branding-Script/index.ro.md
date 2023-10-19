---
title: "Îmbunătățirea sistemelor Windows și a sistemelor server: Ghid de configurare a mărcii personalizate"
date: 2020-08-13
toc: true
draft: false
description: "Learn how to set up custom branding on Windows 10 and Server 2016/2019/2022 systems to personalize your user experience."
tags: ["Marca Windows", "Marca serverului", "branding personalizat", "personalizarea sistemului", "configurația de branding", "Windows 10", "Server 2016", "Server 2019", "Server 2022", "experiența utilizatorului", "ghid de personalizare a sistemului", "personalizare", "branding de sistem", "Personalizarea Windows", "Personalizarea serverului", "logo-ul OEM", "imaginea utilizatorului", "imagine invitată", "script de branding", "Kitul de instrumente de conformitate a securității Microsoft", "Configurarea mărcii Windows", "Configurarea mărcii serverului", "ghid de branding personalizat", "branding personalizat", "tutorial de personalizare a sistemului", "Personalizarea sistemului Windows", "Personalizarea sistemului de servere", "imagini de branding", "cele mai bune practici de branding", "Sfaturi pentru personalizarea Windows", "Tehnici de personalizare a serverului"]
---

**Configurarea mărcii pe sistemele Windows 10 și Server 2016/2019/2022**

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml)

## Cum se configurează fișierele de branding
- [X] Înlocuiți toate imaginile cu imaginile de branding
  - [X] Logo-ul OEM trebuie să fie fie de 95x95 sau 120x20 și în format ".bmp".
  - [X] Generați imaginea utilizatorului împreună cu variantele 32x32, 40x40, 48x48, 192x192.
  - X] Generați sau copiați imaginea utilizatorului pentru imaginea invitatului.
  
## Acest script utilizează următorul instrument:
- [Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Cum se execută scriptul
### Instalare manuală:
Dacă este descărcat manual, scriptul trebuie lansat dintr-un powershell administrativ în directorul care conține toate fișierele din fișierul [GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-copybranding.ps1
```
### Automated Install:
Scriptul poate fi lansat din descărcarea extrasă de pe GitHub astfel:
```powershell
iwr -useb 'https://simeononsecurity.com/scripts/sosbranding.ps1'|iex
```

