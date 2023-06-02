---
title: "Améliorer les systèmes Windows et les serveurs : Guide d'installation du marquage personnalisé"
date: 2020-08-13
toc: true
draft: false
description: "Learn how to set up custom branding on Windows 10 and Server 2016/2019/2022 systems to personalize your user experience."
tags: ["Marquage Windows", "Marque du serveur", "marquage personnalisé", "personnalisation du système", "configuration de l'image de marque", "Windows 10", "Serveur 2016", "Serveur 2019", "Serveur 2022", "expérience utilisateur", "guide de personnalisation du système", "personnalisation", "l'image de marque du système", "Personnalisation de Windows", "Personnalisation du serveur", "Logo OEM", "image de l'utilisateur", "guest image", "script d'image de marque", "Microsoft Security Compliance Toolkit (en anglais)", "Configuration de la marque Windows", "Configuration de la marque du serveur", "guide personnalisé de l'image de marque", "marquage personnalisé", "tutoriel de personnalisation du système", "Personnalisation du système Windows", "Personnalisation du système de serveur", "images de marque", "meilleures pratiques en matière d'image de marque", "Conseils de personnalisation de Windows", "Techniques de personnalisation du serveur"]
---

**Mise en place de la marque sur les systèmes Windows 10 et Server 2016/2019/2022**.

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml)

## Comment configurer les fichiers d'image de marque
- X] Remplacez toutes les images par vos images de marque.
  - X] Le logo OEM doit être au format 95x95 ou 120x20 et au format ".bmp".
  - X] Générer l'image de l'utilisateur avec les variantes 32x32, 40x40, 48x48, 192x192.
  - X] Générer ou copier l'image de l'utilisateur pour l'image de l'invité.
  
## Ce script utilise l'outil suivant :
- [Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Comment exécuter le script
### Installation manuelle :
S'il est téléchargé manuellement, le script doit être lancé à partir d'un power-shell d'administration dans le répertoire contenant tous les fichiers du fichier [GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-copybranding.ps1
```
### Installation automatisée :
Le script peut être lancé à partir du téléchargement GitHub extrait comme suit :
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/sosbranding.ps1'|iex
```

