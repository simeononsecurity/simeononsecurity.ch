---
title: "Automatizza l'attivazione di Windows KMS con lo script GLVK"
date: 2020-12-18
toc: true
draft: false
description: "Semplifica il processo di attivazione KMS di Windows 10 utilizzando lo script di installazione automatica GLVK di SimeonOnSecurity e scopri di più sulle chiavi client KMS e GLVK dalla lettura consigliata da Microsoft."
tags: ["Attivazione Windows", "Chiavi client KMS", "GLVK", "Aggiornamenti di Windows", "Conformità", "Script PowerShell", "Servizio di gestione delle chiavi", "Contratti multilicenza", "Attivazione aziendale", "Server di gestione delle chiavi", "Automazione", "Prodotti Microsoft", "Sistema operativo", "Software", "Ambienti aziendali", "Powershell amministrativo", "Repository GitHub", "Scripting", "Sicurezza informatica", "Simeon Sulla Sicurezza"]
---

Script di installazione automatica GLVK per l'attivazione KMS

## Letture consigliate:
-[Microsoft - KMS Client Keys (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## Come eseguire lo script:
### Installazione manuale:
Se scaricato manualmente, lo script deve essere avviato da una PowerShell amministrativa nella directory contenente tutti i file dal file[GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```ps
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```
