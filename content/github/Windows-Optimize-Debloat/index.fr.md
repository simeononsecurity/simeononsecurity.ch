---
title: "Optimisez votre PC Windows avec Windows-Optimize-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Améliorez les performances et la confidentialité de votre système d'exploitation Windows avec Windows-Optimize-Debloat, un script complet qui permet de supprimer les logiciels superflus et d'optimiser les paramètres du système."
tags: ["Windows-Optimize-Debloat", "Optimisation de Windows", "Fenêtres de déblocage", "Accélérer Windows", "Optimiser les performances de Windows", "Amélioration des performances de Windows", "Optimisation du système Windows", "Microsoft", "Vie privée", "Suppression des bloatwares", "Windows 10", "Windows 11", "Windows Defender", "Windows Update", "Cortona", "Objets de stratégie de groupe", "Télémétrie", "Windows Store", "Windows 10 Professional", "Windows 10 Home"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Pour ceux qui cherchent à minimiser leurs installations de Windows 10 et 11.

**Note:** Ce script devrait fonctionner sans problème sur la plupart des systèmes, si ce n'est sur tous. Tout en [@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) N'exécutez pas ce script si vous ne comprenez pas ce qu'il fait.

## Introduction :
Windows 10 et 11 sont des systèmes d'exploitation invasifs et peu sûrs.
Des organisations comme [Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) et d'autres ont recommandé des changements de configuration pour optimiser et débloquer le système d'exploitation Windows 10. Ces changements comprennent le blocage de la télémétrie, la suppression des journaux et la suppression des bloatwares, pour n'en citer que quelques-uns. Ce script vise à automatiser les configurations recommandées par ces organisations.

## Notes :
- Ce script est conçu pour fonctionner dans des environnements principalement **à usage personnel**.
- Ce script est conçu de manière à ce que les optimisations, contrairement à d'autres scripts, ne cassent pas les fonctionnalités principales de Windows.
 - Des fonctionnalités telles que Windows Update, Windows Defender, le Windows Store et Cortona ont été restreintes, mais ne sont pas dans un état de dysfonctionnement comme la plupart des autres scripts de confidentialité de Windows 10.
- Si vous recherchez un script minimisé ciblant uniquement les environnements commerciaux, veuillez consulter ce document. [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Exigences :
- [X] Windows 10/11 Enterprise, Windows 10 Professional, ou Windows 10 Home
  - Windows Home ne permet pas les configurations GPO.
    - Le script fonctionnera toujours mais tous les paramètres ne s'appliqueront pas.
  - Les éditions "N" de Windows ne sont pas testées.
  - Exécutez le script [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) pour mettre à jour et vérifier la dernière version majeure.

## Correction du compte Microsoft ou des services Xbox :
Ceci est dû au fait que nous bloquons la connexion aux comptes Microsoft. La télémétrie et l'association d'identité de Microsoft sont mal vues.
Cependant, si vous souhaitez toujours utiliser ces services, consultez les tickets de problème suivants pour la résolution :
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## Une liste de scripts et d'outils utilisés par cette collection :
- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Des configurations supplémentaires ont été prises en compte à partir de :
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

## Comment exécuter le script :
### Installation automatisée :
Le script peut être lancé à partir du téléchargement GitHub extrait comme suit :
```powershell
iwr -useb 'https://simeononsecurity.com/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### Installation manuelle :
S'il est téléchargé manuellement, le script doit être lancé à partir d'un powerhell d'administration dans le répertoire contenant tous les fichiers du fichier [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

Le script "sos-optimize-windows.ps1" comprend plusieurs paramètres qui permettent de personnaliser le processus d'optimisation. Chaque paramètre est une valeur booléenne qui prend par défaut la valeur "true" si elle n'est pas spécifiée.

- **$cleargpos** : Efface les paramètres des objets de stratégie de groupe.
- **$installupdates** : Installe des mises à jour sur le système.
- **$removebloatware** : Supprime les programmes et fonctionnalités inutiles du système.
- **$disabletelemetry** : Désactive la collecte de données et la télémétrie.
- **$privacy** : Apporte des modifications pour améliorer la confidentialité.
- **$imagecleanup** : Nettoie les fichiers inutiles du système.
- **$diskcompression** : Compresse le disque du système.
- **$updatemanagement** : Modifie la façon dont les mises à jour sont gérées et améliorées sur le système.
- **$sosbrowsers** : Optimise les navigateurs web du système.

Voici un exemple de lancement du script avec des paramètres spécifiques :

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

