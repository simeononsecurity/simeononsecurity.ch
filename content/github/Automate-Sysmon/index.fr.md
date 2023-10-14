---
title: "Automate-Sysmon : Simplifier le déploiement et la configuration de Sysmon"
date: 2021-05-11
toc: true
draft: false
description: "Apprenez à déployer et à configurer Sysmon pour améliorer la sécurité de votre système grâce au script Automate-Sysmon, qui simplifie le processus pour les utilisateurs novices."
tags: ["Automate Sysmon", "Comment automatiser Sysmon", "Comment automatiser la configuration de Sysmon", "Comment installer Sysmon", "Powershell", "Le scénario", "Déploiement de Sysmon", "Configuration de Sysmon", "Enregistrement Sysmon", "Détection des menaces", "Activité malveillante", "SwiftOnSecurity sysmon-config", "Microsoft Sysinternals", "Dépôt GitHub", "BHIS", "Surveillance du système", "Recherche sur la sécurité", "Création de processus", "Connexions réseau"]
---

Automate-Sysmon est un script utile qui simplifie le déploiement et la configuration de Sysmon, un puissant outil de surveillance du système de Microsoft Sysinternals. En automatisant l'installation et la configuration de Sysmon, ce script augmente les capacités de journalisation de votre système et améliore les capacités de détection des menaces.

## Qu'est-ce que Sysmon ?

Sysmon est un outil de surveillance du système qui peut être utilisé pour détecter les activités malveillantes sur un système. Il fournit des informations détaillées sur la création de processus, les connexions réseau et d'autres événements système, ce qui en fait un outil précieux pour les professionnels de la sécurité. Bien que Sysmon soit un outil puissant, il peut être difficile à mettre en place et à configurer.

## Comment Automate-Sysmon peut vous aider ?

Le script Automate-Sysmon facilite l'installation et la configuration de Sysmon, même pour ceux qui n'ont pas beaucoup d'expérience. Le script utilise le module **SwiftOnSecurity/sysmon-config**, qui fournit un ensemble de règles préconfigurées pour Sysmon. Cette configuration est basée sur des années de recherche en sécurité et est régulièrement mise à jour par la communauté.

Avec Automate-Sysmon, vous pouvez soit automatiser l'ensemble du processus à l'aide d'une seule commande, soit installer manuellement Sysmon en suivant les instructions fournies. Cette flexibilité permet aux utilisateurs de personnaliser l'installation et la configuration en fonction de leurs besoins spécifiques.

## Comment utiliser Automate-Sysmon ?

Il y a deux façons d'utiliser Automate-Sysmon :

### Installation automatisée :

Pour utiliser l'installation automatisée, il suffit d'exécuter la commande suivante dans PowerShell :
```powershell
iwr -useb 'https://simeononsecurity.com/scripts/sosautomatesysmon.ps1'|iex
```

Ceci téléchargera et exécutera automatiquement le script Automate-Sysmon.

### Installation manuelle :

Si vous préférez installer Sysmon manuellement, suivez les étapes suivantes :

1. Téléchargez le script et les autres fichiers nécessaires à partir du site [GitHub repository](https://github.com/simeononsecurity/Automate-Sysmon)
2. Lancez PowerShell avec des privilèges d'administrateur.
3. Naviguez jusqu'au répertoire contenant les fichiers téléchargés.
4. Exécutez la commande suivante pour modifier la politique d'exécution de PowerShell : ```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force```
5. Débloquez tous les fichiers de script en exécutant la commande suivante : ```Get-ChildItem -Recurse *.ps1 | Unblock-File```
6. Exécutez la commande suivante pour lancer le script Automate-Sysmon : ```.\sos-automate-sysmon.ps1```


## Conclusion

En conclusion, Automate-Sysmon est un outil essentiel pour les professionnels de la sécurité qui souhaitent augmenter leurs capacités de journalisation et améliorer les capacités de détection des menaces de leur système. Avec la possibilité d'automatiser le déploiement et la configuration de Sysmon, cet outil peut aider même les utilisateurs novices à tirer le meilleur parti de Sysmon. En utilisant le module **simeononsecurity/Automate-Sysmon**, les utilisateurs peuvent bénéficier de l'expertise de la communauté et rester au courant des dernières recherches en matière de sécurité. Alors, si vous voulez améliorer la sécurité de votre système, essayez Automate-Sysmon !



