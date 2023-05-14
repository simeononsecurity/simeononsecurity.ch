---
title: "Automatitzeu el compliment de .NET STIG amb PowerShell Script"
date: 2020-08-20
---
 el .NET Framework STIG

Aplicar el .NET STIG definitivament no és senzill. Per a molts administradors, pot trigar hores a implementar-se completament en un sol sistema. Aquest script aplica els canvis de registre necessaris i modifica el fitxer machine.config per implementar FIPS i altres controls segons sigui necessari.

## Notes:

Aquest script no pot ni aconseguirà mai que l'estigma .NET compleixi al 100%. Ara mateix, tal com està, ha de completar aproximadament el 75% de les comprovacions i torna enrere i completa les comprovacions aplicables a totes les versions anteriors de .NET.

La intervenció manual és necessària per a qualsevol aplicació .NET o lloc IIS.

## Requisits:
- [X] Windows 7, Windows Server 2008 o posterior
- [X] Prova al teu entorn abans d'executar-te en sistemes de producció.

## STIGS/SRG aplicats:

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip)

## Fonts:

-[Add from one XML data to another existing XML file](http://www.maxtblog.com/2012/11/add-from-one-xml-data-to-another-existing-xml-file/)
-[Caspol.exe (Code Access Security Policy Tool)](https://docs.microsoft.com/en-us/dotnet/framework/tools/caspol-exe-code-access-security-policy-tool)
-[Microsoft .NET Framework Documentation](https://docs.microsoft.com/en-us/dotnet/framework/)
-[PowerShell $PSScriptRoot](https://riptutorial.com/powershell/example/27231/-psscriptroot)
-[PowerShell: Run command from script's directory](https://stackoverflow.com/questions/4724290/powershell-run-command-from-scripts-directory)
-[Powershell XML importnode from different file](https://stackoverflow.com/questions/9944885/powershell-xml-importnode-from-different-file)

## Baixeu els fitxers necessaris

Podeu descarregar els fitxers necessaris des del[GitHub Repository](https://raw.githubusercontent.com/simeononsecurity/.NET-STIG-Script/)

## Com executar l'script

**L'script es pot llançar des de la descàrrega de GitHub extreta així:**

## Com executar l'script
### Instal·lació manual:
Si es descarrega manualment, l'script s'ha de llançar des d'un powershell administratiu al directori que conté tots els fitxers del[GitHub Repository](https://github.com/simeononsecurity/.NET-STIG-Script)
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
