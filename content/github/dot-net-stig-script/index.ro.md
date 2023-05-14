---
title: "Automatizați conformitatea .NET STIG cu Scriptul PowerShell"
date: 2020-08-20
---
 .NET Framework STIG

Aplicarea .NET STIG cu siguranță nu este simplă. Pentru mulți administratori, implementarea completă pe un singur sistem poate dura ore. Acest script aplică modificările de registry necesare și modifică fișierul machine.config pentru a implementa FIPS și alte controale după cum este necesar.

## Note:

Acest script nu poate și nu va aduce vreodată stigul .NET la conformitate 100%. În acest moment, așa cum este, urmează să finalizeze aproximativ 75% din verificări și se întoarce și completează verificările aplicabile pentru toate versiunile anterioare .NET.

Este necesară intervenția manuală pentru orice aplicație .NET sau site IIS.

## Cerințe:
- [X] Windows 7, Windows Server 2008 sau mai nou
- [X] Testarea în mediul dumneavoastră înainte de a rula pe sistemele de producție.

## STIGS/SRG aplicate:

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip)

## Surse:

-[Add from one XML data to another existing XML file](http://www.maxtblog.com/2012/11/add-from-one-xml-data-to-another-existing-xml-file/)
-[Caspol.exe (Code Access Security Policy Tool)](https://docs.microsoft.com/en-us/dotnet/framework/tools/caspol-exe-code-access-security-policy-tool)
-[Microsoft .NET Framework Documentation](https://docs.microsoft.com/en-us/dotnet/framework/)
-[PowerShell $PSScriptRoot](https://riptutorial.com/powershell/example/27231/-psscriptroot)
-[PowerShell: Run command from script's directory](https://stackoverflow.com/questions/4724290/powershell-run-command-from-scripts-directory)
-[Powershell XML importnode from different file](https://stackoverflow.com/questions/9944885/powershell-xml-importnode-from-different-file)

## Descărcați fișierele necesare

Puteți descărca fișierele necesare din[GitHub Repository](https://raw.githubusercontent.com/simeononsecurity/.NET-STIG-Script/)

## Cum se rulează scriptul

**Scriptul poate fi lansat din descărcarea GitHub extrasă astfel:**

## Cum se rulează scriptul
### Instalare manuală:
Dacă este descărcat manual, scriptul trebuie lansat dintr-un powershell administrativ din directorul care conține toate fișierele din[GitHub Repository](https://github.com/simeononsecurity/.NET-STIG-Script)
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
