---
title: "Remplacement de la carte SD de Nebra Helium Miner : Guide étape par étape"
draft: false
toc: true
date: 2022-02-13
description: "Apprenez comment remplacer ou re-flasher la carte SD Nebra Indoor et Outdoor, première et deuxième génération, EMMC Key et résoudre les problèmes de synchronisation d'Helium Miner avec ce guide."
genre: ["Technologie", "Crypto-monnaie", "Matériel", "Hélium Mining", "Dépannage", "Remplacement de la carte SD", "Problèmes de synchronisation", "Raspberry Pi", "Balena Etcher", "Nebra Helium Miner"]
tags: ["Nebra Helium Miner", "Remplacement de la carte SD", "Problèmes de synchronisation", "Hélium Mining", "Dépannage", "Raspberry Pi", "Balena Etcher", "Guide du matériel", "Mise à jour de la carte SD", "Résolution des problèmes de synchronisation", "Guide étape par étape", "Helium Miner Sync Fix", "Nebra Indoor Miner", "Nebra Outdoor Miner", "Raspberry Pi Compute Module 3", "Image Balena Raspberry Pi CM3", "Dépannage des mineurs d'hélium", "Nebra Mining Equipment", "Logiciel Balena Etcher", "Remplacement de la clé EMMC sur le Nebra Miner", "Réparation de la carte SD pour Helium Miner", "Correction des problèmes de synchronisation d'Helium Miner", "Remplacement de la carte SD de Nebra Miner", "Guide de dépannage du Nebra Helium Miner", "Conseils pour l'extraction de l'hélium", "Mise à niveau de la carte SD Nebra Helium Miner", "Comment réimager la carte SD de Nebra Miner ?", "Résolution des problèmes de synchronisation de Nebra Helium Miner"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_holding_a_Nebra_Helium_M.png"
coverAlt: "Illustration de bande dessinée d'une personne tenant un Nebra Helium Miner avec un panneau ouvert révélant l'emplacement de la carte SD et les étapes du guide apparaissant sous la forme d'un guide flottant au-dessus de l'appareil."
coverCaption: "Résolvez les problèmes de synchronisation et mettez à niveau votre Helium Miner en toute simplicité."
---

**Remplacement et réimagerie de la clé EMMC / carte SD de Nebra Indoor et Outdoor**

Ce guide complet vous guidera à travers le processus de remplacement ou de réimagerie de la clé EMMC / carte SD de Nebra Indoor et Outdoor. En suivant ces étapes, vous pouvez résoudre les problèmes de synchronisation avec votre Helium Miner et assurer un fonctionnement sans heurts. Le guide fournit une explication détaillée des outils et logiciels dont vous aurez besoin, ainsi que les étapes nécessaires pour acquérir le fichier config.json, flasher la nouvelle carte SD en utilisant Balena Raspberry Pi CM3 Image, et transférer le fichier de configuration original vers la nouvelle carte SD.

## Introduction

Les Nebra Helium Miners, tant les modèles d'intérieur que d'extérieur, dépendent de la clé EMMC/Carte SD pour leur fonctionnement. Au fil du temps, il peut s'avérer nécessaire de remplacer ou de re-flasher cette carte pour résoudre les problèmes de synchronisation et maintenir des performances optimales. Ce guide vous fournira les connaissances et les instructions nécessaires pour mener à bien cette tâche.

Pour remplacer avec succès la carte SD du Nebra Helium Miner, vous aurez besoin d'outils et de logiciels spécifiques. Les outils comprennent un tournevis à tête Phillips ou un tournevis à tête Phillips. [Allen Key Set](https://amzn.to/34SlnOS) (depending on the model), a [Micro SD Card Reader](https://amzn.to/3Jl3U0w), a [64GB A2 micro SD card](https://amzn.to/3oJtTqs) (or larger), and a [Micro USB 2.0 Cable](https://amzn.to/3LxXYmA). The essential software needed for this process includes [Balena Etcher](https://www.balena.io/etcher/), Balena Raspberry Pi Image, and [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) Avec ces ressources en main, vous serez prêt à procéder au remplacement de la carte SD ou à son rebasage.

## Outils requis :
- Un tournevis cruciforme ou [plastic pry bar](https://amzn.to/3rLXVfc) for the Nebra Indoor Miner or [allen key set](https://amzn.to/34SlnOS) pour Nebra Outdoor Miner
- Des ongles solides, une pince à épiler ou une pince à bec effilé pour retirer l'ancienne carte SD.
- [A Micro SD Card Reader](https://amzn.to/3Jl3U0w)
- [A 64gb (or larger) A2 micro sd card](https://amzn.to/3oJtTqs)
- [A Micro USB 2.0 Cable](https://amzn.to/3LxXYmA)
## Logiciels requis :
- [Balena Etcher](https://www.balena.io/etcher/)
- [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)
- Dernière image Nebra pour votre appareil spécifique :
*Si vous ne savez pas quel appareil vous possédez, veuillez consulter le site Web de Nebra. [nebra documentatio](https://support.nebra.com/support/home) Si elle est plus ancienne, on peut supposer que vous avez un appareil de première génération.
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)

## A l'intérieur des Nebra Helium Miners :
### Contenu du Nebra Indoor Miner :
{{< figure src="Indoor-internal-lights.png" alt="Nebra Indoor Miner" >}}
### Contenu du Nebra Outdoor Miner :
{{< figure src="Inside-Interfaces.jpg" alt="Nebra Outdoor Miner" >}}
 - 1.) 9-16V @ 15W DC 6.5MMx2.0MM Barrel Jack
 - 2.) Connecteur Ethernet
 - 3.) Indicateur LED
 - 4.) Bouton d'interface
 - 5.) Connecteur du module 4G / LTE
 - 6.) Fente pour carte Sim

## Comment remplacer la carte SD
### Étape 1 : Acquérir éventuellement le fichier config.json à partir de la clé EMMC :
- Télécharger et installer [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) Vous en aurez besoin pour démarrer le module de calcul en tant que système de fichiers USB.
- Identifiez et ajustez les cavaliers sur la carte fille CM3 pour le mode de programmation
 - {{< figure src="daughterboardBreakdown.png" alt="Nebra Daughterboard Overview" >}}
   - 5.) Port micro USB utilisé pour l'imagerie
   - 7.) JP4 Cavalier USB - Utilisé pour basculer entre le fonctionnement normal et le mode flash, assurez-vous qu'il est en position 1-2 pour le fonctionnement normal et 2-3 pour la programmation.
   - 8.) JP3 Cavalier d'alimentation - Permet au module d'être alimenté par le connecteur Micro USB. Ne le connectez que lorsque vous programmez à partir d'un PC et assurez-vous que la carte mère n'est pas connectée.
 - Déplacez le cavalier JP4 en position 2+3.
 - Branchez un câble USB et faites passer le [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) utilitaire
 - Ouvrez votre explorateur de fichiers et vous verrez un lecteur appelé "resin-boot". Récupérez le fichier "config.json" dans le répertoire, vous pourriez en avoir besoin plus tard et il devrait être sauvegardé.
 - Débranchez le câble usb et réinitialisez le cavalier JP4 en position 1+2.
### Etape 2 : Flashez la nouvelle carte sd avec l'image Balena Raspberry Pi CM3 :
- Télécharger et extraire l'image appropriée
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)
- Utilisation [Balena Etcher](https://www.balena.io/etcher/) sélectionnez le fichier .img récemment extrait et votre nouvelle carte microsd comme périphérique cible
- Sélectionnez Flash
### Etape 3 : Installer la nouvelle carte SD et réassembler le Nebra Miner :
 - Installez la carte SD dans l'emplacement où se trouvait la clé EMMC.
 - Réassembler le Nebra Miner
 - Lors de la première mise sous tension du Nebra Miner nouvellement flashé, branchez-le sur ethernet pendant 20-30 minutes avant d'établir à nouveau des connexions wifi.
### Etape 4 : Profit ?




