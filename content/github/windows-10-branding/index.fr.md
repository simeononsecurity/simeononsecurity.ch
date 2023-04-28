---
title: "Automated Branding for Windows Systems - Easily Control Desktop, Lock Screen, and More"
date: 2020-08-14T14:37:16-05:00
toc: true
draft: false
description: "Control desktop wallpaper, users avatar, lock screen, and OEM logo with ease on Windows 10 and Server systems using a partially automated script."
tags: ["Automation", "Branding", "Windows Branding", "Customization", "Windows Customization", "Windows 10", "Windows Server 2016", "Windows Server 2019", "Powershell", "Script", "Windows System Branding", "Desktop Wallpaper", "Users Avatar", "Windows Lock Screen", "OEM Logo", "Microsoft Security Compliance Toolkit 1.0", "Organization Branding", "System Customization", "IT Automation", "Security Compliance"]
---
```
.\sos-copybranding.ps1
```

  De nombreuses organisations ont besoin ou souhaitent contrôler l'image de marque d'un système Windows. Cela inclut le fond d'écran du bureau, l'avatar de l'utilisateur, l'écran de verrouillage Windows et parfois le logo OEM. Dans Windows 10, Windows Server 2016 et Windows Server 2019, ce n'est pas particulièrement facile. Mais, à l'aide du script lié, nous pouvons l'automatiser partiellement et rendre le processus beaucoup plus facile.  ## Téléchargez les fichiers requis  **Téléchargez les fichiers requis depuis le [référentiel GitHub](https://github.com/simeononsecurity/Windows-Branding-Script)**  ## Comment configurer les fichiers de marque  - [X] Remplacez toutes les images par vos images de marque   - [X] Le logo OEM doit être au format 95x95 ou 120x20 et au format ".bmp"   - [X] Générez l'image utilisateur avec les variantes 32x32, 40x40, 48x48, 192x192.   - [X] Générer ou copier l'image de l'utilisateur pour l'image de l'invitation.  ## Commentez le script  ## Ce script utilise l'outil suivant :  - [Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)