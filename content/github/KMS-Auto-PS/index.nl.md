---
title: "Windows KMS-activering automatiseren met GLVK-script"
date: 2020-12-18
toc: true
draft: false
description: "Vereenvoudig het Windows 10 KMS activatieproces met behulp van het GLVK Auto Install Script van SimeonOnSecurity, en leer meer over KMS en GLVK-clientsleutels uit de aanbevolen lectuur van Microsoft."
tags: ["Windows Activering", "KMS-clientsleutels", "GLVK", "Windows Updates", "Naleving", "Powershell Script", "Dienst voor sleutelbeheer", "Volumelicenties", "Activering van de onderneming", "Sleutelbeheerserver", "Automatisering", "Microsoft-producten", "Besturingssysteem", "Software", "Bedrijfsomgevingen", "Administratieve Powershell", "GitHub archief", "Scripting", "Cyberbeveiliging", "SimeonOnSecurity"]
---

GLVK Automatisch installatiescript voor KMS-activering

## Aanbevolen lectuur:
-[Microsoft - KMS Client Keys (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## Hoe voer je het script uit:
### Handmatig installeren:
Indien handmatig gedownload, moet het script gestart worden vanuit een administratieve powershell in de directory die alle bestanden van de[GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```ps
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```
