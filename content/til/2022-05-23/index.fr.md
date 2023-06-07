---
title: "Aujourd'hui, j'ai appris à créer des emballages en chocolat"
date: 2022-05-23
toc: true
draft: false
description: "Aujourd'hui, j'en ai appris plus sur les conditionnelles et la gestion des variables d'Ansible"
genre: ["Automatisation", "Windows Package Management", "Création d'un paquet", "Package Management", "Infrastructure as Code (IaC)", "Déploiement de logiciels Windows", "Emballage du logiciel", "Windows Automation", "Dépôts de paquets", "Windows Tools"]
tags: ["automation", "Powershell", "Gestionnaire de paquets chocolatés", "Chocolatée", "Choco", "création d'un paquet", "l'automatisation des paquets", "Nuspec", "Nethor", "Windows Package Managers", "IAC", "L'infrastructure en tant que code", "Déploiement de logiciels Windows", "l'emballage des logiciels", "gestion du référentiel", "partage des paquets", "Documentation sur le chocolat", "tutoriel", "édition de paquets"]
---

**Ce que SimeonOnSecurity a appris et trouvé intéressant aujourd'hui**

Aujourd'hui, SimeonOnSecurity a découvert le processus de création de paquets pour le gestionnaire de paquets Chocolatey. Chocolatey est un gestionnaire de paquets pour Windows qui facilite l'installation, la mise à niveau et la gestion des applications et des outils. En créant des paquets, SimeonOnSecurity peut automatiser l'installation de logiciels et partager des paquets avec d'autres membres de la communauté.

SimeonOnSecurity a créé et mis à jour deux dépôts sur GitHub liés à la création de paquets Chocolatey. Le premier dépôt, simeononsecurity/Chocolatey-Nethor, est un paquet pour Nethor. Le second dépôt, simeononsecurity/chocolateypackages, est une collection de paquets créés par SimeonOnSecurity pour diverses applications et outils.

Pour créer un paquet, SimeonOnSecurity a utilisé le format de fichier Nuspec, qui fournit des métadonnées sur le paquet et son contenu. Le processus de création des paquets a également impliqué l'utilisation de fonctions telles que Install-ChocolateyInstallPackage et Install-ChocolateyPackage pour spécifier le logiciel à installer et toutes les dépendances nécessaires.

SimeonOnSecurity a également examiné plusieurs ressources d'apprentissage, notamment la documentation officielle de Chocolatey et un didacticiel de Top Bug Net, afin de mieux comprendre le processus de création et de publication des paquets Chocolatey.

Dans l'ensemble, l'expérience d'apprentissage de SimeonOnSecurity lui a permis d'acquérir une compréhension complète du processus de création de paquets pour le Chocolatey Package Manager, ce qui facilite l'automatisation des installations de logiciels et le partage de paquets avec d'autres membres de la communauté.

## Repos Créé/Mis à jour :
- [simeononsecurity/Chocolatey-Nethor](https://github.com/simeononsecurity/Chocolatey-Nethor)
- [simeononsecurity/chocolateypackages](https://github.com/simeononsecurity/chocolateypackages)

## Ressources pédagogiques :
- [Chocolatey - Create Packages](https://docs.chocolatey.org/en-us/create/create-packages#nuspec)
- [Chocolatey - Install-ChocolateyInstallPackage](https://docs.chocolatey.org/en-us/create/functions/install-chocolateyinstallpackage)
- [Chocolatey - Install-ChocolateyPackage](https://docs.chocolatey.org/en-us/create/functions/install-chocolateypackage)
- [Top Bug Net - Create and Publish Chocolatey Packages](https://www.topbug.net/blog/2012/07/02/a-simple-tutorial-create-and-publish-chocolatey-packages/)