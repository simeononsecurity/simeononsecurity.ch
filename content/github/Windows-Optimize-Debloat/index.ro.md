---
title: "Optimizați-vă computerul Windows cu Windows-Optimize-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Îmbunătățiți performanța și confidențialitatea sistemului dvs. de operare Windows cu Windows-Optimize-Debloat, un script cuprinzător care ajută la eliminarea bloatware-ului și la optimizarea setărilor sistemului."
tags: ["Windows-Optimizare-Debloat", "Optimizare Windows", "Deblocare Windows", "Accelerează Windows", "Optimizați performanța Windows", "Creșterea performanței Windows", "Optimizarea sistemului Windows", "Microsoft", "Confidențialitate", "Eliminarea bloatware-ului", "Windows 10", "Windows 11", "Windows Defender", "Windows Update", "Cortona", "Obiecte de politică de grup", "Telemetrie", "Magazin Windows", "Windows 10 Professional", "Windows 10 Home"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Pentru cei care doresc să-și minimizeze instalările Windows 10 și 11.*

**Notă:** Acest script ar trebui să funcționeze pentru majoritatea, dacă nu pentru toate, sistemele fără probleme. In timp ce[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Nu rulați acest script dacă nu înțelegeți ce face.

## Introducere:
Windows 10 și 11 sunt sisteme de operare invazive și nesigure din cutie.
Organizații ca[Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) iar alții au recomandat modificări de configurare pentru a optimiza și debloca sistemul de operare Windows 10. Aceste modificări includ blocarea telemetriei, ștergerea jurnalelor și eliminarea bloatware-ului, pentru a numi câteva. Acest script are scopul de a automatiza configurațiile recomandate de acele organizații.

## Note:
- Acest script este conceput pentru funcționarea în principal în medii de **Uz personal**.
- Acest script este proiectat în așa fel încât optimizările, spre deosebire de alte scripturi, să nu distrugă funcționalitatea de bază a Windows.
 - Funcții precum Windows Update, Windows Defender, Windows Store și Cortona au fost restricționate, dar nu sunt într-o stare nefuncțională ca majoritatea celorlalte scripturi de confidențialitate Windows 10.
- Dacă căutați un script minimizat țintit doar pentru medii comerciale, vă rugăm să vedeți acest lucru[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Cerințe:
- [X] Windows 10/11 Enterprise, Windows 10 Professional sau Windows 10 Home
  - Windows Home nu permite configurarea GPO.
    - Scriptul va funcționa în continuare, dar nu se vor aplica toate setările.
  - Edițiile Windows „N” nu sunt testate.
  - Rulați[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) pentru a actualiza și a verifica cea mai recentă versiune majoră.

## Remedierea contului Microsoft sau a serviciilor Xbox:
Acest lucru se datorează faptului că blocăm conectarea la conturile Microsoft. Asocierea de telemetrie și identitate a Microsoft este descurajată.
Cu toate acestea, dacă încă doriți să utilizați aceste servicii, consultați următoarele bilete de emisiune pentru rezolvare:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## O listă de scripturi și instrumente pe care le utilizează această colecție:
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Au fost luate în considerare configurații suplimentare din:
-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)

## Cum se rulează scriptul:
### Instalare automată:
Scriptul poate fi lansat din descărcarea GitHub extrasă astfel:
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### Manual Install:
If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

The script "sos-optimize-windows.ps1" includes several parameters that allow for customization of the optimization process. Each parameter is a boolean value that defaults to true if not specified.

- **$cleargpos**: Clears Group Policy Objects settings.
- **$installupdates**: Installs updates to the system.
- **$removebloatware**: Removes unnecessary programs and features from the system.
- **$disabletelemetry**: Disables data collection and telemetry.
- **$privacy**: Makes changes to improve privacy.
- **$imagecleanup**: Cleans up unneeded files from the system.
- **$diskcompression**: Compresses the system disk.
- **$updatemanagement**: Changes the way updates are managed and improved on the system.
- **$sosbrowsers**: Optimizes the system's web browsers.

An example of how to launch the script with specific parameters would be:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

