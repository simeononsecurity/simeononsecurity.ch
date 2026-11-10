---
title: "Standalone-Windows-STIG-Script : créez un PC conforme"
date: 2023-02-02
toc: true
draft: false
description: "Guide étape par étape pour utiliser Standalone-Windows-STIG-Script sur des systèmes Windows conformes, avec paramètres et étapes de vérification."
tags: ["Script STIG", "Sécurité Windows", "Système Windows conforme", "Renforcement du système", "Windows STIG", "Windows sécurisé", "Conformité Windows", "Installation manuelle", "Mises à jour Windows", "Adobe Reader", "Firefox", "Chrome", "Internet Explorer 11", ".NET Framework", "Office", "OneDrive", "Java", "Windows Defender", "Pare-feu Windows", "Mesures d’atténuation", "Nessus PID", "VMware Horizon", "Renforcement facultatif"]
cover: "/img/cover/create-compliant-windows-desktop-systems-with-standalone-windows-stig-script.webp"
coverAlt: "Illustration d’un écran d’ordinateur présentant une interface de conformité de sécurité, des barres de progression dynamiques et des flux de données sur un fond bleu marine sombre avec des accents vifs."
coverCaption: ""
lastmod: 2026-11-09
---

Les systèmes Windows sont largement utilisés dans les entreprises, les organisations et même les foyers. Avec le nombre croissant de cyberattaques, il est crucial de s'assurer que ces systèmes sont sécurisés et conformes aux normes de l'industrie. Le script Standalone-Windows-STIG est un outil utile qui vous permet d'atteindre cet objectif. Dans cet article, nous verrons ce qu'est le Standalone-Windows-STIG-Script, comment il fonctionne et comment vous pouvez l'utiliser pour créer un système Windows sécurisé et conforme.

## Qu'est-ce que Standalone-Windows-STIG-Script ?

**Standalone-Windows-STIG-Script** est un script développé par Simeononsecurity qui est conçu pour automatiser le processus de sécurisation d'un système Windows et de mise en conformité avec le Guide d'implémentation technique de la sécurité (STIG). Le script est open-source et disponible sur **GitHub**.

## Comment cela fonctionne-t-il ?

Le script Standalone-Windows-STIG met en œuvre les directives fournies dans le STIG pour sécuriser un système Windows. Le script peut être exécuté sur un système Windows, et il effectuera les changements nécessaires au système pour assurer la conformité avec la STIG. Le script couvre un large éventail de mesures de sécurité, y compris, mais sans s'y limiter, les éléments suivants :

- Politiques de compte
- Politiques d'audit
- Options de sécurité
- Paramètres du pare-feu
- Paramètres des services

## Avantages de l'utilisation de Standalone-Windows-STIG-Script :

- **Automatisation** : Le script automatise le processus de sécurisation d'un système Windows, ce qui permet de gagner du temps et d'éliminer le risque d'erreur humaine.

- **Conformité** : Le script met en œuvre les directives fournies dans la STIG, garantissant que le système Windows est conforme aux normes de l'industrie.

- **Tranquillité d'esprit** : En utilisant le script Standalone-Windows-STIG, vous pouvez avoir l'esprit tranquille en sachant que votre système Windows est sécurisé et conforme aux normes de l'industrie.

_________________________________________________________________________________________________________________________

## Comment utiliser le script Standalone-Windows-STIG :

1. L'utilisation du script Standalone-Windows-STIG est relativement simple. Voici les étapes à suivre pour utiliser le script :

2. **Téléchargez le script** : Le script est disponible sur GitHub à l'adresse https://github.com/simeononsecurity/Standalone-Windows-STIG-Script. Téléchargez le script et enregistrez-le sur votre système Windows.

3. **Ouvrez une invite de commande élevée** : Cliquez avec le bouton droit de la souris sur le bouton Démarrer de Windows et sélectionnez "Windows PowerShell (Admin)".

4. **Exécutez le script** : Naviguez jusqu'à l'emplacement où vous avez enregistré le script et exécutez le script en entrant la commande suivante :

```powershell
powershell.exe -ExecutionPolicy Bypass -File Standalone-Windows-STIG-Script.ps1
```

5. Examinez les modifications : Après l'exécution du script, examinez les modifications apportées au système pour vous assurer que tout est configuré correctement.

## Conclusion :

En conclusion, le script Standalone-Windows-STIG est un outil utile qui peut vous aider à sécuriser votre système Windows et à vous conformer aux normes de l'industrie. En utilisant le script, vous pouvez automatiser le processus de sécurisation de votre système Windows, en vous assurant qu'il est conforme à la STIG et en vous procurant la tranquillité d'esprit de savoir que votre système est sécurisé. Donc, si vous voulez créer un système Windows conforme et sécurisé, envisagez d'utiliser le script Standalone-Windows-STIG.