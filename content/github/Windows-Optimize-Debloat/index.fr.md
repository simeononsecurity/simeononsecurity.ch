---
title: "Optimisez votre PC Windows avec Windows-Optimize-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Améliorez les performances et la confidentialité de votre système d'exploitation Windows avec Windows-Optimize-Debloat, un script complet qui aide à supprimer les bloatwares et à optimiser les paramètres système."
tags: ["Windows-Optimize-Debloat", "Optimisation Windows", "Dégonfler Windows", "Accélérer Windows", "Optimiser les performances de Windows", "Amélioration des performances de Windows", "Optimisation du système Windows", "Microsoft", "Confidentialité", "Suppression des bloatwares", "Windows 10", "Windows 11", "Windows Defender", "Windows Update", "Cortone", "Objets de stratégie de groupe", "Télémétrie", "Magasin Windows", "Windows 10 Professionnel", "Windows 10 Famille"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Pour ceux qui cherchent à minimiser leurs installations Windows 10 et 11.*

**Remarque :** Ce script devrait fonctionner sans problème pour la plupart des systèmes, sinon tous. Alors que[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) N'exécutez pas ce script si vous ne comprenez pas ce qu'il fait.

## Introduction:
Windows 10 et 11 sont des systèmes d'exploitation invasifs et non sécurisés prêts à l'emploi.
Des organisations comme[Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) et d'autres ont recommandé des changements de configuration pour optimiser et dégonfler le système d'exploitation Windows 10. Ces changements incluent le blocage de la télémétrie, la suppression des journaux et la suppression des bloatwares pour n'en nommer que quelques-uns. Ce script vise à automatiser les configurations recommandées par ces organisations.

## Remarques:
- Ce script est conçu pour fonctionner principalement dans des environnements **à usage personnel**.
- Ce script est conçu de manière à ce que les optimisations, contrairement à certains autres scripts, ne cassent pas les fonctionnalités principales de Windows.
 - Des fonctionnalités telles que Windows Update, Windows Defender, le Windows Store et Cortona ont été restreintes, mais ne sont pas dans un état dysfonctionnel comme la plupart des autres scripts de confidentialité de Windows 10.
- Si vous recherchez un script réduit destiné uniquement aux environnements commerciaux, veuillez consulter ceci[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Exigences:
- [X] Windows 10/11 Entreprise, Windows 10 Professionnel ou Windows 10 Famille
  - Windows Home ne permet pas les configurations GPO.
    - Le script fonctionnera toujours mais tous les paramètres ne s'appliqueront pas.
  - Les éditions "N" de Windows ne sont pas testées.
  - Exécutez le[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) pour mettre à jour et vérifier la dernière version majeure.

## Correction du compte Microsoft ou des services Xbox :
En effet, nous bloquons la connexion aux comptes Microsoft. L'association télémétrie et identité de Microsoft est mal vue.
Toutefois, si vous souhaitez toujours utiliser ces services, consultez les tickets de problème suivants pour la résolution :
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## Une liste de scripts et d'outils utilisés par cette collection :
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Des configurations supplémentaires ont été envisagées à partir de :
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

## Comment exécuter le script :
### Installation automatisée :
Le script peut être lancé à partir du téléchargement GitHub extrait comme ceci :
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

