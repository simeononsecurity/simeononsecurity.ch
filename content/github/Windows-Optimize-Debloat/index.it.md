---
title: "Ottimizzare il PC Windows con Windows-Optimize-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Migliorate le prestazioni e la privacy del vostro sistema operativo Windows con Windows-Optimize-Debloat, uno script completo che aiuta a rimuovere il bloatware e a ottimizzare le impostazioni del sistema."
tags: ["Windows-Optimize-Debloat", "Ottimizzazione di Windows", "Finestre debloating", "Velocizzare Windows", "Ottimizzare le prestazioni di Windows", "Aumento delle prestazioni di Windows", "Ottimizzazione del sistema Windows", "Microsoft", "Privacy", "Rimozione del bloatware", "Windows 10", "Windows 11", "Windows Defender", "Aggiornamento di Windows", "Cortona", "Oggetti dei Criteri di gruppo", "Telemetria", "Windows Store", "Windows 10 Professional", "Windows 10 Home"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Per coloro che desiderano ridurre al minimo le installazioni di Windows 10 e 11.*.

**Nota:** Questo script dovrebbe funzionare senza problemi per la maggior parte dei sistemi, se non per tutti. Mentre [@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Non eseguite questo script se non capite cosa fa.

## Introduzione:
Windows 10 e 11 sono sistemi operativi invasivi e insicuri.
Organizzazioni come [Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) e altri hanno consigliato di apportare modifiche alla configurazione per ottimizzare e ridurre il sistema operativo Windows 10. Queste modifiche includono il blocco della telemetria, l'eliminazione dei registri e la rimozione del bloatware, per citarne alcune. Questo script mira ad automatizzare le configurazioni consigliate da queste organizzazioni.

## Note:
- Questo script è stato progettato per operare in ambienti prevalentemente di **uso personale**.
- Questo script è progettato in modo tale che le ottimizzazioni, a differenza di altri script, non interrompano le funzionalità fondamentali di Windows.
 - Funzionalità come Windows Update, Windows Defender, Windows Store e Cortona sono state limitate, ma non sono in uno stato di disfunzione come la maggior parte degli altri script Windows 10 Privacy.
- Se cercate uno script ridotto al minimo e destinato solo ad ambienti commerciali, consultate questo [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Requisiti:
- [X] Windows 10/11 Enterprise, Windows 10 Professional o Windows 10 Home
  - Windows Home non consente le configurazioni GPO.
    - Lo script funzionerà comunque, ma non tutte le impostazioni saranno applicate.
  - Le edizioni "N" di Windows non sono state testate.
  - Eseguire il file [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) per aggiornare e verificare l'ultima versione principale.

## Correzione dell'account Microsoft o dei servizi Xbox:
Questo perché blocchiamo l'accesso agli account Microsoft. La telemetria e l'associazione di identità di Microsoft non sono viste di buon occhio.
Tuttavia, se si desidera utilizzare questi servizi, consultare i seguenti ticket per la risoluzione del problema:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## Un elenco degli script e degli strumenti utilizzati da questa raccolta:
- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Sono state prese in considerazione configurazioni aggiuntive da:
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

## Come eseguire lo script:
### Installazione automatica:
Lo script può essere lanciato dal download estratto da GitHub in questo modo:
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### Installazione manuale:
Se scaricato manualmente, lo script deve essere lanciato da una powershell amministrativa nella directory contenente tutti i file del file [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

Lo script "sos-optimize-windows.ps1" include diversi parametri che consentono di personalizzare il processo di ottimizzazione. Ciascun parametro è un valore booleano che, se non specificato, viene impostato come vero.

- **$cleargpos**: Cancella le impostazioni degli oggetti dei Criteri di gruppo.
- **$installupdates**: Installa gli aggiornamenti nel sistema.
- **$removebloatware**: Rimuove i programmi e le funzioni non necessarie dal sistema.
- **$disabletelemetry**: Disattiva la raccolta dati e la telemetria.
- **$privacy**: Apporta modifiche per migliorare la privacy.
- **$imagecleanup**: Ripulisce il sistema dai file non necessari.
- **$diskcompression**: Comprime il disco di sistema.
- **$gestione degli aggiornamenti**: Modifica il modo in cui gli aggiornamenti vengono gestiti e migliorati nel sistema.
- **$sosbrowsers**: Ottimizza i browser web del sistema.

Un esempio di come lanciare lo script con parametri specifici potrebbe essere:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

