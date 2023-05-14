---
title: "Optimitzeu el vostre PC amb Windows amb Windows-Optimize-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Milloreu el rendiment i la privadesa del vostre sistema operatiu Windows amb Windows-Optimize-Debloat, un script complet que ajuda a eliminar el bloatware i optimitzar la configuració del sistema."
tags: ["Windows-Optimize-Desbloat", "Optimització de Windows", "Desinflació de Windows", "Accelera Windows", "Optimitzar el rendiment de Windows", "Augment del rendiment de Windows", "Optimització del sistema Windows", "Microsoft", "Privadesa", "Eliminació de bloatware", "Windows 10", "Windows 11", "Windows Defender", "actualització de Windows", "Cortona", "Objectes de política de grup", "Telemetria", "Botiga de Windows", "Windows 10 Professional", "Windows 10 Home"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Per a aquells que busquen minimitzar les instal·lacions de Windows 10 i 11.*

**Nota:** Aquest script hauria de funcionar per a la majoria, si no tots, els sistemes sense problemes. Mentre[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) No executeu aquest script si no enteneu què fa.

## Introducció:
Windows 10 i 11 són un sistema operatiu invasiu i insegur des de la caixa.
Organitzacions com[Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) i altres han recomanat canvis de configuració per optimitzar i eliminar el sistema operatiu Windows 10. Aquests canvis inclouen el bloqueig de la telemetria, la supressió de registres i l'eliminació del programari bloat per citar-ne alguns. Aquest script pretén automatitzar les configuracions recomanades per aquestes organitzacions.

## Notes:
- Aquest script està dissenyat per funcionar principalment en entorns d'**Ús personal**.
- Aquest script està dissenyat de tal manera que les optimitzacions, a diferència d'altres scripts, no trencaran la funcionalitat bàsica de Windows.
 - S'han restringit funcions com Windows Update, Windows Defender, Windows Store i Cortona, però no es troben en un estat disfuncional com la majoria dels altres scripts de privadesa de Windows 10.
- Si cerqueu un script minimitzat dirigit només a entorns comercials, consulteu això[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Requisits:
- [X] Windows 10/11 Enterprise, Windows 10 Professional o Windows 10 Home
  - Windows Home no permet configuracions GPO.
    - L'script seguirà funcionant, però no s'aplicaran tots els paràmetres.
  - Les edicions "N" de Windows no estan provades.
  - Executar el[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) per actualitzar i verificar la darrera versió principal.

## Arreglar el compte de Microsoft o els serveis de Xbox:
Això es deu al fet que bloquegem la sessió als comptes de Microsoft. L'associació de telemetria i identitat de Microsoft està mal vista.
Tanmateix, si encara voleu utilitzar aquests serveis, consulteu els següents tiquets d'emissió per a la resolució:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## Una llista de scripts i eines que utilitza aquesta col·lecció:
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## S'han considerat configuracions addicionals de:
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

## Com executar l'script:
### Instal·lació automàtica:
L'script es pot llançar des de la descàrrega de GitHub extreta així:
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

