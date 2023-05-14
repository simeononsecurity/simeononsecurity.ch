---
title: "Automatizza la conformità .NET STIG con PowerShell Script"
date: 2020-08-20
---
 .NET Framework STIG

L'applicazione di .NET STIG non è assolutamente semplice. Per molti amministratori possono essere necessarie ore per l'implementazione completa su un singolo sistema. Questo script applica le modifiche al registro richieste e modifica il file machine.config per implementare FIPS e altri controlli come richiesto.

## Appunti:

Questo script non può e non otterrà mai la conformità .NET stig al 100%. In questo momento, così com'è, completa circa il 75% dei controlli e torna indietro e completa i controlli applicabili su tutte le versioni precedenti di .NET.

L'intervento manuale è richiesto per qualsiasi applicazione .NET o sito IIS.

## Requisiti:
- [X] Windows 7, Windows Server 2008 o versioni successive
- [X] Test nel proprio ambiente prima dell'esecuzione sui sistemi di produzione.

## STIGS/SRG applicati:

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip)

## Fonti:

-[Add from one XML data to another existing XML file](http://www.maxtblog.com/2012/11/add-from-one-xml-data-to-another-existing-xml-file/)
-[Caspol.exe (Code Access Security Policy Tool)](https://docs.microsoft.com/en-us/dotnet/framework/tools/caspol-exe-code-access-security-policy-tool)
-[Microsoft .NET Framework Documentation](https://docs.microsoft.com/en-us/dotnet/framework/)
-[PowerShell $PSScriptRoot](https://riptutorial.com/powershell/example/27231/-psscriptroot)
-[PowerShell: Run command from script's directory](https://stackoverflow.com/questions/4724290/powershell-run-command-from-scripts-directory)
-[Powershell XML importnode from different file](https://stackoverflow.com/questions/9944885/powershell-xml-importnode-from-different-file)

## Scarica i file richiesti

È possibile scaricare i file richiesti dal file[GitHub Repository](https://raw.githubusercontent.com/simeononsecurity/.NET-STIG-Script/)

## Come eseguire lo script

**Lo script può essere avviato dal download GitHub estratto in questo modo:**

## Come eseguire lo script
### Installazione manuale:
Se scaricato manualmente, lo script deve essere avviato da un PowerShell amministrativo nella directory contenente tutti i file dal file[GitHub Repository](https://github.com/simeononsecurity/.NET-STIG-Script)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-.net-4-stig.ps1
```
### Automated Install:
Use this one-liner to automatically download, unzip all supporting files, and run the latest version of the script.
```
iwr -useb 'https://simeononsecurity.ch/scripts/sosdotnet.ps1'|iex
```
