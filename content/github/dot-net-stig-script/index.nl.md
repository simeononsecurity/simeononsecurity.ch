---
title: ".NET STIG-naleving automatiseren met PowerShell-script"
date: 2020-08-20
---
 het .NET-kader STIG

Het toepassen van de .NET STIG is zeker niet eenvoudig. Voor veel beheerders kan het uren duren om volledig te implementeren op een enkel systeem. Dit script past de vereiste registerwijzigingen toe en wijzigt het bestand machine.config om FIPS en andere controles te implementeren zoals vereist.

## Opmerkingen:

Dit script kan en zal nooit de .NET stig tot 100% compliance brengen. Op dit moment, zoals het is, staat het op ongeveer 75% van de controles en het gaat terug en voltooit de van toepassing zijnde controles op alle vorige .NET versies.

Handmatige tussenkomst is vereist voor elke .NET-toepassing of IIS-site.

## Vereisten:
- [X] Windows 7, Windows Server 2008 of nieuwer.
- X] Testen in uw omgeving alvorens op productiesystemen te draaien.

## Toegepaste STIGS/SRG's:

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip)

## Bronnen:

-[Add from one XML data to another existing XML file](http://www.maxtblog.com/2012/11/add-from-one-xml-data-to-another-existing-xml-file/)
-[Caspol.exe (Code Access Security Policy Tool)](https://docs.microsoft.com/en-us/dotnet/framework/tools/caspol-exe-code-access-security-policy-tool)
-[Microsoft .NET Framework Documentation](https://docs.microsoft.com/en-us/dotnet/framework/)
-[PowerShell $PSScriptRoot](https://riptutorial.com/powershell/example/27231/-psscriptroot)
-[PowerShell: Run command from script's directory](https://stackoverflow.com/questions/4724290/powershell-run-command-from-scripts-directory)
-[Powershell XML importnode from different file](https://stackoverflow.com/questions/9944885/powershell-xml-importnode-from-different-file)

## Download de benodigde bestanden

U kunt de benodigde bestanden downloaden van de[GitHub Repository](https://raw.githubusercontent.com/simeononsecurity/.NET-STIG-Script/)

## Hoe voer je het script uit

**Het script kan worden gestart vanuit de uitgepakte GitHub-download als volgt:**

## Hoe het script uit te voeren
### Handmatig installeren:
Indien handmatig gedownload, moet het script worden gestart vanuit een administratieve powershell in de map met alle bestanden uit de[GitHub Repository](https://github.com/simeononsecurity/.NET-STIG-Script)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-.net-4-stig.ps1
```
### Geautomatiseerde installatie:
Gebruik deze one-liner om automatisch alle ondersteunende bestanden te downloaden, uit te pakken en de laatste versie van het script uit te voeren.
```
iwr -useb 'https://simeononsecurity.ch/scripts/sosdotnet.ps1'|iex
```
