---
title: "Guide complet : Hachures de fichiers sous Windows à l'aide de PowerShell"
draft: false
toc: true
date: 2023-05-25
description: "Apprenez à obtenir des hachages de fichiers sous Windows à l'aide de PowerShell, notamment SHA256, MD5 et SHA1, à l'aide d'instructions et d'exemples étape par étape."
tags: ["hachages de fichiers", "PowerShell", "Hachure SHA256", "Hachure MD5", "Hachure SHA1", "intégrité des fichiers", "authentification des données", "vérification des fichiers", "algorithmes de hachage", "Système d'exploitation Windows", "langage de script", "shell de ligne de commande", "la sécurité des données", "criminalistique numérique", "cybersécurité", "calcul du hachage", "falsification de fichiers", "l'intégrité des données", "authenticité du dossier", "Sécurité Windows", "identification du fichier", "cyberdéfense", "sécurité des fichiers", "protection des données", "vérification des données", "validation des fichiers", "Windows PowerShell", "génération de hachages", "algorithmes de hachage", "fonctions de hachage"]
cover: "/img/cover/A_cartoon_illustration_showing_a_file_with_a_lock_symbol.png"
coverAlt: "Illustration de bande dessinée montrant un fichier avec un symbole de cadenas et une loupe, représentant la vérification et la sécurité du hachage des fichiers."
coverCaption: ""
---

**Comment obtenir des hachages de fichiers sous Windows à l'aide de PowerShell**.

Dans le domaine de la sécurité informatique, l'obtention des hachages de fichiers est une étape cruciale pour garantir l'intégrité des données et vérifier l'authenticité des fichiers. Les hachages sont des identifiants uniques générés pour les fichiers, permettant aux utilisateurs de détecter les tentatives de falsification et de valider l'intégrité des données. Dans ce guide complet, nous allons explorer le processus d'obtention des hachages **SHA256**, **MD5** et **SHA1** des fichiers sous Windows à l'aide du puissant langage de script **PowerShell**. Suivez les instructions étape par étape et plongez dans des exemples spécifiques. C'est parti !

______

## Obtention de hachages sous Windows à l'aide de PowerShell

PowerShell, un langage de script polyvalent et un shell de ligne de commande pour Windows, propose la cmdlet **Get-FileHash**, qui permet aux utilisateurs de calculer le hachage d'un fichier sans effort.

### Obtention du hachage SHA256

Pour obtenir le hachage **SHA256** d'un fichier à l'aide de PowerShell, suivez ces étapes simples :

1. Lancez PowerShell en ouvrant le **menu Démarrer**, en recherchant **PowerShell** et en sélectionnant **Windows PowerShell**.
2. Naviguez jusqu'au répertoire où se trouve le fichier. Utilisez l'option `cd` suivie du chemin d'accès au répertoire.
3. Exécutez la commande suivante pour obtenir le hachage SHA256 du fichier :
```powershell
   Get-FileHash -Algorithm SHA256 -Path "file_path"
```
### Obtention des hachages MD5 et SHA1
Vous pouvez également obtenir les hachages `MD5` et `SHA1` Les hashs d'un fichier à l'aide de PowerShell. Utilisez les commandes suivantes :

- Pour obtenir les `MD5 hash`
  
```powershell
Get-FileHash -Algorithm MD5 -Path "file_path"
```

- Pour obtenir la `SHA1 hash`

```powershell
Get-FileHash -Algorithm SHA1 -Path "file_path"
```

N'oubliez pas de remplacer "file_path" par le chemin d'accès à votre fichier dans les deux commandes.

## Exemples
Nous allons nous pencher sur des exemples spécifiques pour illustrer le processus d'obtention de hachages à l'aide de PowerShell sous Windows.

{{< youtube id="UrHhsF1q3rU" >}}

### Exemple 1 : Obtention du hachage SHA256
Imaginez que vous ayez un fichier nommé `document.pdf` situé dans le répertoire `C:\Files` Pour obtenir la `SHA256 hash` de ce fichier à l'aide de PowerShell, exécutez la commande suivante :

```powershell
Get-FileHash -Algorithm SHA256 -Path "C:\Files\document.pdf"
```

La sortie affichera la valeur de hachage SHA256 du fichier.

### Exemple 2 : Obtention du hachage MD5

Supposons que vous possédiez un fichier nommé `image.jpg` stockés dans le répertoire `C:\Photos` Pour obtenir la `MD5 hash` de ce fichier à l'aide de PowerShell, exécutez la commande suivante :

```powershell
Get-FileHash -Algorithm MD5 -Path "C:\Photos\image.jpg"
```

Le terminal affiche la valeur de hachage MD5 du fichier.

### Exemple 3 : Obtention du hachage SHA1

Prenons l'exemple d'un fichier nommé `data.txt` situé dans le répertoire `C:\Documents` Pour obtenir la `SHA1 hash` de ce fichier à l'aide de PowerShell, exécutez la commande suivante :

```powershell
Get-FileHash -Algorithm SHA1 -Path "C:\Documents\data.txt"
```

La sortie affichera la valeur de hachage SHA1 du fichier.