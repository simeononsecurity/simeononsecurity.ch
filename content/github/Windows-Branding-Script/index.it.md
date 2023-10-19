---
title: "Miglioramento dei sistemi Windows e Server: Guida all'impostazione del marchio personalizzato"
date: 2020-08-13
toc: true
draft: false
description: "Learn how to set up custom branding on Windows 10 and Server 2016/2019/2022 systems to personalize your user experience."
tags: ["Marchio Windows", "Marchio del server", "marchio personalizzato", "personalizzazione del sistema", "impostazione del marchio", "Windows 10", "Server 2016", "Server 2019", "Server 2022", "esperienza dell'utente", "Guida alla personalizzazione del sistema", "personalizzazione", "marchio del sistema", "Personalizzazione di Windows", "Personalizzazione del server", "Logo OEM", "immagine utente", "immagine ospite", "script di branding", "Toolkit di conformità alla sicurezza Microsoft", "Impostazione del marchio Windows", "Impostazione del marchio del server", "Guida al marchio personalizzato", "marchio personalizzato", "esercitazione sulla personalizzazione del sistema", "Personalizzazione del sistema Windows", "Personalizzazione del sistema server", "immagini di branding", "Le migliori pratiche di branding", "Suggerimenti per la personalizzazione di Windows", "Tecniche di personalizzazione del server"]
---

**Impostazione del marchio su sistemi Windows 10 e Server 2016/2019/2022**

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml)

## Come impostare i file di branding
- [X] Sostituire tutte le immagini con le immagini del proprio branding.
  - [X] Il logo OEM deve essere 95x95 o 120x20 e in formato ".bmp".
  - [X] Generare l'immagine utente con le varianti 32x32, 40x40, 48x48, 192x192.
  - [X] Generare o copiare l'immagine utente per l'immagine guest.
  
## Questo script utilizza il seguente strumento:
- [Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Come eseguire lo script
### Installazione manuale:
Se scaricato manualmente, lo script deve essere lanciato da una powershell amministrativa nella directory contenente tutti i file del file [GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-copybranding.ps1
```
### Installazione automatica:
Lo script può essere lanciato dal download estratto da GitHub in questo modo:
```powershell
iwr -useb 'https://simeononsecurity.com/scripts/sosbranding.ps1'|iex
```

