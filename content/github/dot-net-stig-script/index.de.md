---
title: "Automatisieren der .NET STIG-Konformität mit PowerShell-Skript"
date: 2020-08-20
---
 das .NET Framework STIG

Die Anwendung der .NET STIG ist definitiv nicht einfach. Für viele Administratoren kann es Stunden dauern, ein einzelnes System vollständig zu implementieren. Dieses Skript wendet die erforderlichen Registrierungsänderungen an und ändert die Datei machine.config, um FIPS und andere Kontrollen wie erforderlich zu implementieren.

## Hinweise:

Dieses Skript kann und wird den .NET-Stig nicht zu 100% konform machen. In seiner jetzigen Form vervollständigt es etwa 75 % der Prüfungen und geht zurück und vervollständigt die anwendbaren Prüfungen auf allen früheren .NET-Versionen.

Für jede .NET-Anwendung oder IIS-Site ist ein manuelles Eingreifen erforderlich.

## Anforderungen:
- [X] Windows 7, Windows Server 2008 oder neuer
- X] Testen Sie die Anwendung in Ihrer Umgebung, bevor Sie sie auf Produktionssystemen ausführen.

## Angewandte STIGS/SRGs:

- [Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip)

## Quellen:

- [Add from one XML data to another existing XML file](http://www.maxtblog.com/2012/11/add-from-one-xml-data-to-another-existing-xml-file/)
- [Caspol.exe (Code Access Security Policy Tool)](https://docs.microsoft.com/en-us/dotnet/framework/tools/caspol-exe-code-access-security-policy-tool)
- [Microsoft .NET Framework Documentation](https://docs.microsoft.com/en-us/dotnet/framework/)
- [PowerShell $PSScriptRoot](https://riptutorial.com/powershell/example/27231/-psscriptroot)
- [PowerShell: Run command from script's directory](https://stackoverflow.com/questions/4724290/powershell-run-command-from-scripts-directory)
- [Powershell XML importnode from different file](https://stackoverflow.com/questions/9944885/powershell-xml-importnode-from-different-file)

## Download der erforderlichen Dateien

Sie können die erforderlichen Dateien von der Website [GitHub Repository](https://raw.githubusercontent.com/simeononsecurity/.NET-STIG-Script/)

## So führen Sie das Skript aus

**Das Skript kann von dem extrahierten GitHub-Download wie folgt gestartet werden:**

## So führen Sie das Skript aus
### Manuelle Installation:
Wenn das Skript manuell heruntergeladen wurde, muss es von einer administrativen Powershell in dem Verzeichnis gestartet werden, das alle Dateien aus dem [GitHub Repository](https://github.com/simeononsecurity/.NET-STIG-Script)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-.net-4-stig.ps1
```
### Automatisierte Installation:
Verwenden Sie diesen Einzeiler, um automatisch alle unterstützenden Dateien herunterzuladen, zu entpacken und die neueste Version des Skripts auszuführen.
```
iwr -useb 'https://simeononsecurity.ch/scripts/sosdotnet.ps1'|iex
```
