---
title: "Renforcez la sécurité de votre système avec les commandes PowerShell de Windows Defender"
date: 2023-07-27
toc: true
draft: false
description: "Découvrez la puissance des commandes PowerShell de Windows Defender et apprenez à renforcer la sécurité de votre système grâce au contrôle de la ligne de commande."
genre: ["Windows Defender", "Commandes PowerShell", "sécurité du système", "contrôle de la ligne de commande", "antivirus", "Systèmes d'exploitation Windows", "protection contre les logiciels malveillants", "paramètres de sécurité avancés", "automatiser les opérations de sécurité", "Windows PowerShell"]
tags: ["Technologie", "Cybersécurité", "Systèmes d'exploitation", "Fenêtres", "Outils de ligne de commande", "Sécurité du système", "PowerShell", "Antivirus", "Protection contre les logiciels malveillants", "Scripting"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.png"
coverAlt: "Illustration animée représentant un bouclier protégeant un système informatique de diverses cybermenaces."
coverCaption: "Renforcez la sécurité de votre système avec les commandes PowerShell de Windows Defender."
---

## Introduction

Windows Defender, développé par Microsoft, est une solution intégrée d'antivirus et de sécurité pour les systèmes d'exploitation Windows. Il offre une interface conviviale permettant de gérer efficacement les paramètres de sécurité. Cependant, pour les utilisateurs avancés qui préfèrent le contrôle en ligne de commande, Windows Defender fournit un ensemble de commandes PowerShell puissantes. Dans cet article, nous allons nous plonger dans le monde des **commandes PowerShell de Windows Defender** et explorer comment elles peuvent améliorer la sécurité du système et fournir un meilleur contrôle sur votre environnement Windows.

## La puissance des commandes PowerShell de Windows Defender

Les commandes PowerShell de Windows Defender permettent aux utilisateurs d'effectuer des opérations de sécurité avancées à l'aide d'une interface de ligne de commande. Ces commandes offrent un large éventail de fonctionnalités, allant d'opérations simples comme la recherche de logiciels malveillants à des tâches complexes comme la configuration de paramètres de sécurité avancés. En utilisant PowerShell, les utilisateurs peuvent automatiser les opérations de sécurité, créer des scripts personnalisés et intégrer Windows Defender dans leurs flux de travail existants de manière transparente.

## Démarrer avec Windows Defender PowerShell

Pour accéder aux commandes PowerShell de Windows Defender, vous devez ouvrir une session PowerShell avec des privilèges administratifs. Voici comment commencer :

1. Appuyez sur `Win + X` et sélectionnez **Windows PowerShell (Admin)** dans le menu.
2. Si vous y êtes invité, cliquez sur **Oui** pour permettre à l'application d'apporter des modifications à votre appareil.

Une fois la session PowerShell ouverte, vous pouvez commencer à utiliser les commandes PowerShell de Windows Defender.

## Commandes PowerShell courantes de Windows Defender

### 1. **Get-MpComputerStatus** : Vérifier l'état de Windows Defender

L'état de l'ordinateur `Get-MpComputerStatus` fournit une vue d'ensemble de l'état actuel de Windows Defender sur votre système, y compris la version du moteur antivirus, l'heure de la dernière analyse et l'état de la protection en temps réel. En exécutant cette commande, vous pouvez rapidement évaluer l'état général de Windows Defender et vous assurer qu'il fonctionne de manière optimale.

Pour vérifier l'état de Windows Defender, ouvrez une session PowerShell avec des privilèges administratifs et exécutez la commande suivante :

```powershell
Get-MpComputerStatus
```

Cette commande permet d'afficher des informations telles que

- **AntivirusEngineVersion** : Le numéro de version du moteur antivirus utilisé par Windows Defender.
- **LastFullScanTime** : La date et l'heure de la dernière analyse complète effectuée par Windows Defender.
- LastQuickScanTime** : La date et l'heure de la dernière analyse rapide effectuée par Windows Defender.
- **RealTimeProtectionEnabled** : Indique si la protection en temps réel est activée ou non : Indique si la protection en temps réel est activée ou désactivée.

Surveiller régulièrement l'état de Windows Defender à l'aide de `Get-MpComputerStatus` vous permet de rester informé du niveau de protection de votre système contre les menaces potentielles.

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

Les `Update-MpSignature` vous permet de mettre à jour manuellement les signatures antivirus utilisées par Windows Defender. Les signatures antivirus contiennent des informations cruciales sur les logiciels malveillants connus, ce qui permet à Windows Defender de détecter et de bloquer les menaces de manière efficace. En exécutant cette commande, vous vous assurez que votre système dispose des signatures les plus récentes, offrant ainsi une protection renforcée contre les menaces émergentes.

Pour mettre à jour manuellement les signatures de Windows Defender, ouvrez une session PowerShell avec des privilèges administratifs et exécutez la commande suivante :

```powershell
Update-MpSignature
```
Cette commande déclenche le processus de mise à jour, au cours duquel **Windows Defender** se connecte aux **serveurs Microsoft** pour télécharger les **signatures antivirus** les plus récentes. Une fois la mise à jour terminée, Windows Defender disposera des informations les plus récentes sur les logiciels malveillants connus, ce qui renforcera sa capacité à identifier et à éliminer les menaces.

Il est essentiel de garder les signatures de Windows Defender à jour pour maintenir le plus haut niveau de protection contre le paysage en constante évolution des **malwares** et des **menaces cybernétiques**. En mettant régulièrement à jour les signatures à l'aide de `Update-MpSignature` vous vous assurez que Windows Defender peut protéger efficacement votre système.

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

Les `Set-MpPreference` vous permet de personnaliser divers paramètres de **Windows Defender**, ce qui vous permet d'adapter son comportement à vos besoins spécifiques en matière de sécurité. Cette commande offre une grande souplesse dans la configuration d'options telles que **la protection en temps réel**, **la protection basée sur le cloud** et **les paramètres du système d'inspection du réseau**.

Par exemple, vous pouvez activer ou désactiver la protection en temps réel à l'aide de la commande `Set-MpPreference` commande. La protection en temps réel surveille activement votre système à la recherche d'activités malveillantes et fournit une réponse immédiate aux menaces. Pour activer la protection en temps réel, exécutez la commande suivante :

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

En outre, vous pouvez utiliser cette commande pour ajuster les paramètres de la protection basée sur le cloud. La protection basée sur le cloud utilise les ressources du cloud pour améliorer la détection des menaces et fournir des réponses plus rapides aux menaces émergentes. Pour activer la protection basée sur le cloud, utilisez la commande suivante :

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

En outre, le `Set-MpPreference` permet de personnaliser les paramètres du système d'inspection du réseau. Le système d'inspection du réseau analyse le trafic réseau à la recherche d'activités suspectes et de menaces potentielles. Pour ajuster les paramètres du système d'inspection du réseau, exécutez la commande suivante :

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

En affinant ces paramètres à l'aide de `Set-MpPreference` vous pouvez optimiser **Windows Defender** pour répondre à vos besoins spécifiques en matière de sécurité et garantir une protection solide contre les logiciels malveillants et autres activités malveillantes.

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

Les `Start-MpScan` est un outil puissant pour lancer des analyses de logiciels malveillants sur votre système, ce qui vous permet d'identifier et d'éliminer les fichiers malveillants de manière proactive. Cette commande permet d'effectuer différents types d'analyses, notamment des **analyses rapides**, des **analyses complètes** et des **analyses personnalisées** avec des chemins d'accès spécifiques.

Pour effectuer une **analyse rapide** à l'aide de la commande `Start-MpScan` exécutez la commande PowerShell suivante :

```powershell
Start-MpScan -ScanType QuickScan
```

Une analyse rapide se concentre sur les zones critiques de votre système où les logiciels malveillants sont généralement présents, ce qui permet une évaluation rapide des menaces potentielles.

Pour une analyse plus complète qui examine tous les fichiers et répertoires de votre système, vous pouvez lancer une **analyse complète**. Exécutez la commande suivante pour effectuer une analyse complète à l'aide de la commande `Start-MpScan`

```powershell
Start-MpScan -ScanType FullScan
```

Une analyse complète garantit une détection et une suppression complètes des logiciels malveillants de votre système, mais elle peut prendre plus de temps qu'une analyse rapide.

Outre les types d'analyse prédéfinis, l'option `Start-MpScan` vous permet d'effectuer des analyses personnalisées en spécifiant des chemins d'accès ou des fichiers spécifiques à analyser. Par exemple, vous pouvez analyser un répertoire spécifique de votre système à l'aide de la commande suivante :

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

Cette commande lance une analyse personnalisée dans le répertoire spécifié, ce qui vous permet de cibler des zones spécifiques de votre système pour la détection de logiciels malveillants.

En tirant parti de la polyvalence de la commande `Start-MpScan` vous pouvez programmer des analyses, automatiser des processus de sécurité et garantir la détection et l'atténuation régulières des logiciels malveillants sur votre système.

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

Les `Get-MpThreatCatalog` est une ressource précieuse pour obtenir des informations détaillées sur les menaces connues et leurs attributs. En exécutant cette commande, vous pouvez accéder à un catalogue complet des menaces, y compris des données sur leur gravité, les noms de fichiers associés et les actions recommandées pour les atténuer.

Pour obtenir des informations sur des menaces spécifiques à l'aide de la commande `Get-MpThreatCatalog` suivre les étapes suivantes :

1. Ouvrez une session PowerShell avec des privilèges administratifs.
2. Exécutez la commande suivante :

```powershell
   Get-MpThreatCatalog
```
Cette commande permet d'afficher une liste des menaces connues avec les détails correspondants.

La sortie de la commande `Get-MpThreatCatalog` comprend des informations essentielles telles que

- **ThreatID** : Un identifiant unique pour la menace.
- Gravité** : Indique le niveau de gravité de la menace, allant de Faible à Grave.
- **Name** : Le nom ou la description de la menace.
- Chemin d'accès** : Le chemin d'accès au fichier associé à la menace.
- Action recommandée** : Fournit des indications sur l'action recommandée pour atténuer la menace.

En exploitant les informations obtenues à partir de `Get-MpThreatCatalog` vous pouvez obtenir des informations précieuses sur les menaces potentielles et prendre des décisions éclairées concernant les actions appropriées pour les atténuer. Qu'il s'agisse d'isoler, de supprimer ou de surveiller une menace spécifique, le catalogue détaillé vous permet de répondre efficacement aux incidents de sécurité.

Pour plus d'informations sur l'utilisation de `Get-MpThreatCatalog` et l'interprétation de ses résultats, se référer à la documentation officielle de Microsoft.

Restez vigilant et utilisez régulièrement le `Get-MpThreatCatalog` pour rester informé de l'évolution des menaces et renforcer la sécurité de votre système.

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

Les `Add-MpPreference` vous permet d'ajouter des exclusions à Windows Defender, ce qui vous permet de personnaliser le comportement de l'analyse et de la protection en temps réel. En ajoutant des exclusions, vous pouvez spécifier des fichiers, des dossiers ou des processus que vous souhaitez que Windows Defender ignore lors des analyses de sécurité ou de la protection en temps réel.

Pour ajouter une exclusion en utilisant `Add-MpPreference` vous devez indiquer le chemin d'accès ou le nom du fichier, du dossier ou du processus que vous souhaitez exclure. Voici un exemple d'ajout d'une exclusion pour un dossier :

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

Cette commande permet à Windows Defender de ne pas analyser le dossier spécifié, ce qui réduit les alertes inutiles et les interruptions potentielles de votre flux de travail.

Les exclusions peuvent être utiles dans divers scénarios, comme l'exclusion d'applications de confiance, d'environnements de développement ou de fichiers spécifiques susceptibles de déclencher des faux positifs. En tirant parti de la flexibilité de `Add-MpPreference` vous pouvez adapter Windows Defender à vos besoins spécifiques en matière de sécurité et optimiser ses performances.

Protégez efficacement votre système tout en minimisant les faux positifs et les interruptions d'analyse inutiles en utilisant les puissantes capacités d'exclusion fournies par `Add-MpPreference`

## Conclusion

Les commandes PowerShell de Windows Defender fournissent un **ensemble solide d'outils** pour gérer et améliorer la sécurité de votre système Windows. En tirant parti de ces commandes, vous pouvez *automatiser les opérations de sécurité*, *configurer les paramètres avancés* et intégrer Windows Defender de manière transparente dans vos flux de travail. Que vous soyez **administrateur système** ou **utilisateur principal**, l'exploration des capacités des commandes PowerShell de Windows Defender peut améliorer de manière significative la posture de sécurité de votre système.

N'oubliez pas qu'un grand pouvoir s'accompagne d'une grande responsabilité. Lorsque vous utilisez les commandes PowerShell, faites preuve de prudence et assurez-vous de comprendre l'impact des commandes avant de les exécuter. En associant vos connaissances à la puissance des commandes PowerShell de Windows Defender, vous pouvez prendre des mesures proactives pour protéger votre système contre les menaces en constante évolution.

## Références

1. Microsoft Docs - [Windows Defender Cmdlets in Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. Microsoft Docs - [Introduction to Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
