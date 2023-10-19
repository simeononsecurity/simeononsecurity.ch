---
title: "Automatiser la conformité à la STIG de .NET avec un script PowerShell"
date: 2020-08-20
---
 le cadre .NET STIG

L'application de la STIG du cadre .NET n'est certainement pas simple. Pour de nombreux administrateurs, la mise en œuvre complète sur un seul système peut prendre des heures. Ce script applique les changements de registre nécessaires et modifie le fichier machine.config pour implémenter le FIPS et d'autres contrôles selon les besoins.

## Notes :

Ce script ne peut pas et ne pourra jamais faire en sorte que le stig .NET soit conforme à 100 %. Pour l'instant, tel qu'il est, il est en mesure d'effectuer environ 75 % des vérifications et de revenir en arrière pour effectuer les vérifications applicables à toutes les versions .NET antérieures.

Une intervention manuelle est nécessaire pour toute application .NET ou site IIS.

## Exigences :
- [X] Windows 7, Windows Server 2008 ou plus récent
- [X] Tester dans votre environnement avant de l'exécuter sur des systèmes de production.

## STIGS/SRGs appliqués :

- [Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip)

## Sources :

- [Add from one XML data to another existing XML file](http://www.maxtblog.com/2012/11/add-from-one-xml-data-to-another-existing-xml-file/)
- [Caspol.exe (Code Access Security Policy Tool)](https://docs.microsoft.com/en-us/dotnet/framework/tools/caspol-exe-code-access-security-policy-tool)
- [Microsoft .NET Framework Documentation](https://docs.microsoft.com/en-us/dotnet/framework/)
- [PowerShell $PSScriptRoot](https://riptutorial.com/powershell/example/27231/-psscriptroot)
- [PowerShell: Run command from script's directory](https://stackoverflow.com/questions/4724290/powershell-run-command-from-scripts-directory)
- [Powershell XML importnode from different file](https://stackoverflow.com/questions/9944885/powershell-xml-importnode-from-different-file)

## Télécharger les fichiers nécessaires

Vous pouvez télécharger les fichiers nécessaires à partir du site [GitHub Repository](https://raw.githubusercontent.com/simeononsecurity/.NET-STIG-Script/)

## Comment exécuter le script

**Le script peut être lancé à partir du téléchargement GitHub extrait comme ceci:**

## Comment exécuter le script
### Installation manuelle :
S'il est téléchargé manuellement, le script doit être lancé à partir d'un powerhell d'administration dans le répertoire contenant tous les fichiers de l'archive GitHub. [GitHub Repository](https://github.com/simeononsecurity/.NET-STIG-Script)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-.net-4-stig.ps1
```
### Installation automatisée :
Utilisez cette ligne pour télécharger automatiquement, décompresser tous les fichiers de support et exécuter la dernière version du script.
```
iwr -useb 'https://simeononsecurity.com/scripts/sosdotnet.ps1'|iex
```
