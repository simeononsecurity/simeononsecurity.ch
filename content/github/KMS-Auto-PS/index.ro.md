---
title: "Automatizați activarea Windows KMS cu GLVK Script"
date: 2020-12-18
toc: true
draft: false
description: "Simplificați procesul de activare KMS pentru Windows 10 utilizând Scriptul de instalare automată GLVK de la SimeonOnSecurity și aflați mai multe despre cheile client KMS și GLVK din citirea recomandată de Microsoft."
tags: ["Activare Windows", "Chei de client KMS", "GLVK", "Actualizări Windows", "Conformitate", "Script Powershell", "Serviciul de gestionare a cheilor", "Licențiere în volum", "Activarea întreprinderii", "Server de gestionare a cheilor", "Automatizare", "Produse Microsoft", "Sistem de operare", "Software", "Medii de întreprindere", "Powershell administrativ", "Depozitul GitHub", "Scripting", "Securitate cibernetică", "SimeonOnSecurity"]
---

Scriptul de instalare automată GLVK pentru activarea KMS

## Lectură recomandată:
-[Microsoft - KMS Client Keys (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## Cum se rulează scriptul:
### Instalare manuală:
Dacă este descărcat manual, scriptul trebuie lansat dintr-un powershell administrativ din directorul care conține toate fișierele din[GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```ps
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```
