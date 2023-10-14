---
title: "Optimizați PC-ul Windows cu Windows-Optimize-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Îmbunătățiți performanța și confidențialitatea sistemului de operare Windows cu Windows-Optimize-Debloat, un script cuprinzător care vă ajută să eliminați bloatware și să optimizați setările sistemului."
tags: ["Windows-Optimize-Debloat", "Optimizarea Windows", "Deblocare ferestre", "Accelerați Windows", "Optimizarea performanțelor Windows", "Îmbunătățirea performanțelor Windows", "Optimizarea sistemului Windows", "Microsoft", "Confidențialitate", "Eliminarea Bloatware", "Windows 10", "Windows 11", "Windows Defender", "Windows Update", "Cortona", "Obiecte de politică de grup", "Telemetrie", "Magazin Windows", "Windows 10 Professional", "Windows 10 Home"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Pentru cei care caută să își minimizeze instalațiile Windows 10 și 11.*

**Nota:** Acest script ar trebui să funcționeze pentru majoritatea, dacă nu toate sistemele, fără probleme. În timp ce [@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Nu rulați acest script dacă nu înțelegeți ce face.

## Introducere:
Windows 10 și 11 este un sistem de operare invaziv și nesigur din start.
Organizații precum [Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) și alții au recomandat modificări de configurare pentru a optimiza și debloca sistemul de operare Windows 10. Aceste modificări includ blocarea telemetriei, ștergerea jurnalelor și eliminarea bloatware-ului, pentru a numi doar câteva dintre ele. Acest script își propune să automatizeze configurațiile recomandate de aceste organizații.

## Note:
- Acest script este conceput pentru funcționarea în medii în principal **Personal Use**.
- Acest script este conceput în așa fel încât optimizările, spre deosebire de alte scripturi, nu vor întrerupe funcționalitatea de bază a Windows.
 - Funcționalități precum Windows Update, Windows Defender, Windows Store și Cortona au fost restricționate, dar nu se află într-o stare de disfuncționalitate ca majoritatea celorlalte scripturi Windows 10 Privacy.
- Dacă sunteți în căutarea unui script minimizat destinat doar mediilor comerciale, vă rugăm să consultați acest script [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Cerințe:
- [X] Windows 10/11 Enterprise, Windows 10 Professional sau Windows 10 Home
  - Windows Home nu permite configurații GPO.
    - Scriptul va funcționa în continuare, dar nu se vor aplica toate setările.
  - Edițiile Windows "N" nu sunt testate.
  - Rulați scriptul [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) pentru a actualiza și verifica ultima versiune majoră.

## Repararea contului Microsoft sau a serviciilor Xbox:
Acest lucru se datorează faptului că blocăm semnarea în conturile microsoft. Telemetria Microsoft și asocierea identității este dezaprobată.
Cu toate acestea, dacă doriți totuși să utilizați aceste servicii, consultați următoarele bilete de problemă pentru rezolvare:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## O listă de scripturi și instrumente pe care le utilizează această colecție:
- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Au fost luate în considerare configurații suplimentare din:
- [BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
- [MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
- [Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
- [Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
- [Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
- [Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
- [Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
- [UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
- [Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
- [The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
- [TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
- [W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)

## Cum se execută scriptul:
### Automated Install:
Scriptul poate fi lansat din descărcarea extrasă de pe GitHub, astfel:
```powershell
iwr -useb 'https://simeononsecurity.com/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### Instalare manuală:
Dacă este descărcat manual, scriptul trebuie lansat dintr-un powershell administrativ în directorul care conține toate fișierele din fișierul [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

Scriptul "sos-optimize-windows.ps1" include mai mulți parametri care permit personalizarea procesului de optimizare. Fiecare parametru este o valoare booleană care, în cazul în care nu este specificată, are valoarea implicită true.

- **$cleargpos**: Șterge setările Obiectelor de politică de grup.
- **$$installupdates**: Instalează actualizări în sistem.
- **$removebloatware**: Îndepărtează programele și funcțiile inutile din sistem.
- **$disabletelemetry**: Dezactivează colectarea de date și telemetria.
- **$privacy**: Efectuează modificări pentru a îmbunătăți confidențialitatea.
- **$imagecleanup**: Curăță fișierele inutile din sistem.
- **$diskcompression**: Comprimă discul sistemului.
- **$updatemanagement**: Modifică modul în care sunt gestionate și îmbunătățite actualizările pe sistem.
- **$sosbrowsers**: Optimizează browserele web ale sistemului.

Un exemplu de lansare a scriptului cu parametrii specifici ar fi

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

