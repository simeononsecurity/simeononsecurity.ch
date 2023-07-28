---
title: "Marque automatisée pour les systèmes Windows - Contrôlez facilement le bureau, l'écran de verrouillage, etc"
date: 2020-08-14
---


De nombreuses organisations ont besoin ou souhaitent contrôler l'image de marque d'un système Windows.
Cela inclut le fond d'écran, l'avatar de l'utilisateur, l'écran de verrouillage de Windows et parfois le logo OEM.
Dans Windows 10, Windows Server 2016 et Windows Server 2019, ce n'est pas particulièrement facile.
Mais, avec l'aide du script lié, nous pouvons partiellement l'automatiser et rendre le processus beaucoup plus facile.

## Télécharger les fichiers nécessaires

**Téléchargez les fichiers nécessaires à partir du site [GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)

## Comment configurer les fichiers d'image de marque

- X] Remplacez toutes les images par vos images de marque.
  - X] Le logo OEM doit être au format 95x95 ou 120x20 et au format ".bmp".
  - X] Générer l'image de l'utilisateur avec les variantes 32x32, 40x40, 48x48, 192x192.
  - X] Générer ou copier l'image de l'utilisateur pour l'image de l'invité.

## Comment exécuter le script
```
.\sos-copybranding.ps1
```

## Ce script utilise l'outil suivant :

- [Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
