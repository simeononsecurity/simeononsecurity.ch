---
title: "Ottimizza il tuo PC Windows con Windows-Optimize-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Migliora le prestazioni e la privacy del tuo sistema operativo Windows con Windows-Optimize-Debloat, uno script completo che aiuta a rimuovere il bloatware e ottimizzare le impostazioni di sistema."
tags: ["Windows-Ottimizza-Debloat", "Ottimizzazione Windows", "Debloare Windows", "Velocizza Windows", "Ottimizza le prestazioni di Windows", "Aumento delle prestazioni di Windows", "Ottimizzazione del sistema Windows", "Microsoft", "Riservatezza", "Rimozione del bloatware", "Windows 10", "Finestre 11", "Difensore di Windows", "aggiornamento Windows", "Cortone", "Oggetti Criteri di gruppo", "Telemetria", "Windows Store", "Windows 10 professionale", "Windows 10 Casa"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Per coloro che cercano di ridurre al minimo le installazioni di Windows 10 e 11.*

**Nota:** questo script dovrebbe funzionare senza problemi per la maggior parte dei sistemi, se non per tutti. Mentre[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Non eseguire questo script se non capisci cosa fa.

## Introduzione:
Windows 10 e 11 sono sistemi operativi invasivi e non sicuri pronti all'uso.
Organizzazioni come[Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) e altri hanno raccomandato modifiche alla configurazione per ottimizzare e sbloccare il sistema operativo Windows 10. Queste modifiche includono il blocco della telemetria, l'eliminazione dei registri e la rimozione del bloatware per citarne alcuni. Questo script ha lo scopo di automatizzare le configurazioni consigliate da tali organizzazioni.

## Appunti:
- Questo script è progettato per funzionare principalmente in ambienti di **uso personale**.
- Questo script è progettato in modo tale che le ottimizzazioni, a differenza di altri script, non interrompano le funzionalità di base di Windows.
 - Funzionalità come Windows Update, Windows Defender, Windows Store e Cortona sono state limitate, ma non sono in uno stato disfunzionale come la maggior parte degli altri script Privacy di Windows 10.
- Se cerchi uno script ridotto a icona destinato solo ad ambienti commerciali, consulta questo[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Requisiti:
- [X] Windows 10/11 Enterprise, Windows 10 Professional o Windows 10 Home
  - Windows Home non consente configurazioni GPO.
    - Lo script continuerà a funzionare ma non tutte le impostazioni verranno applicate.
  - Le edizioni "N" di Windows non sono testate.
  - Corri il[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) per aggiornare e verificare l'ultima major release.

## Correzione dell'account Microsoft o dei servizi Xbox:
Questo perché blocchiamo l'accesso agli account Microsoft. La telemetria e l'associazione di identità di Microsoft sono disapprovate.
Tuttavia, se desideri ancora utilizzare questi servizi, consulta i seguenti ticket di emissione per la risoluzione:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## Un elenco di script e strumenti utilizzati da questa raccolta:
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Ulteriori configurazioni sono state prese in considerazione da:
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

## Come eseguire lo script:
### Installazione automatica:
Lo script può essere avviato dal download GitHub estratto in questo modo:
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

