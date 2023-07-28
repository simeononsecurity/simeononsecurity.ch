---
title: "Maîtriser l'administration d'Active Directory avec PowerShell : Guide d'installation et d'utilisation"
date: 2023-07-25
toc: true
draft: false
description: "Découvrez comment installer et utiliser efficacement le module Active Directory pour PowerShell afin de rationaliser vos tâches d'administration de Windows Active Directory."
genre: ["Technologie", "Fenêtres", "PowerShell", "Active Directory", "Administration", "Scripting", "IT", "Automatisation", "Serveur Windows", "Microsoft"]
tags: ["Module Active Directory pour PowerShell", "module d'importation active directory dans PowerShell", "Module Active Directory pour Windows PowerShell", "active directory PowerShell install", "installer active directory PowerShell", "PowerShell install active directory module Windows 10", "installer active directory module PowerShell Windows 10", "obtenir le module PowerShell de l'annuaire actif", "Administration de l'AD", "Windows Active Directory", "Les cmdlets PowerShell", "récupérer des informations sur l'AD", "créer des objets AD", "modifier des objets AD", "gérer la sécurité AD", "Gestion des utilisateurs AD", "Gestion des groupes AD", "AD OU management", "Scripting PowerShell", "Administration du serveur Windows", "Microsoft PowerShell", "Automatiser les tâches AD", "Installation du module PowerShell", "Guide d'administration AD", "Gestion de l'Active Directory", "Gestion de la sécurité AD", "Automatisation PowerShell", "Commandes PowerShell pour Active Directory", "Référence des cmdlets PowerShell"]
cover: "/img/cover/An_image_depicting_a_network_of_interconnected.png"
coverAlt: "Image représentant un réseau de serveurs interconnectés et d'icônes d'utilisateurs, symbolisant la gestion et l'automatisation d'Active Directory."
coverCaption: "Débloquer la puissance de l'administration d'Active Directory avec PowerShell."
---

## Introduction

Dans le paysage numérique actuel, la gestion et la maintenance des comptes d'utilisateurs, des groupes de sécurité et d'autres ressources dans un environnement Windows Active Directory (AD) nécessitent des processus efficaces et rationalisés. PowerShell, un puissant langage de script développé par Microsoft, offre le **module Active Directory** pour faciliter les tâches d'administration AD. Ce module fournit un large éventail de cmdlets qui permettent aux administrateurs d'automatiser diverses opérations et de gérer AD de manière efficace. Dans cet article, nous allons explorer l'installation et l'utilisation du module Active Directory pour PowerShell.

## Installation du module Active Directory pour PowerShell

Pour commencer à utiliser le module Active Directory pour PowerShell, vous devez vous assurer qu'il est installé sur votre système. La procédure d'installation peut varier en fonction de votre système d'exploitation. Voici les étapes de l'installation du module sur **Windows 10**, **Windows 11** et **Windows Server** :

### Windows 10 et Windows 11 - PowerShell
1. Ouvrez **Windows PowerShell** avec des privilèges administratifs.
2. Exécutez la commande suivante pour installer le module :

```powershell
Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0 -Online
```

1. Attendez la fin de l'installation. Une fois l'installation terminée, vous pouvez commencer à utiliser le module Active Directory.

### Windows Server
1. Ouvrez **Windows PowerShell** avec des privilèges administratifs.
2. Exécutez la commande suivante pour installer le module :

```powershell
Install-WindowsFeature -Name "RSAT-AD-PowerShell" -IncludeAllSubFeature
```

3. Attendez la fin de l'installation. Une fois l'installation terminée, vous pouvez commencer à utiliser le module Active Directory.

### Systèmes hors ligne

Les systèmes hors ligne sont un peu plus compliqués. Il existe plusieurs méthodes, mais celle que nous recommandons est l'utilisation du script suivant :
- [Offine-PS-ActiveDirectory-Install](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install)

## Importation du module Active Directory dans PowerShell

Avant de pouvoir utiliser le module Active Directory dans PowerShell, vous devez l'importer dans votre session actuelle. Suivez les étapes suivantes pour importer le module :

1. Lancez **Windows PowerShell** avec les droits d'administrateur.
2. Exécutez la commande suivante pour importer le module :

```powershell
Import-Module ActiveDirectory
```

3. Le module Active Directory est importé et vous pouvez maintenant accéder à ses cmdlets et à ses fonctions.

## Utilisation du module Active Directory pour PowerShell

Une fois le module Active Directory importé, vous pouvez tirer parti de son riche ensemble de cmdlets pour effectuer diverses tâches administratives. Explorons quelques cmdlets couramment utilisées et leurs fonctionnalités :

### Récupération des informations Active Directory

Pour gérer efficacement un environnement Active Directory (AD), il est essentiel de récupérer des informations sur divers objets AD, tels que les utilisateurs, les groupes et les unités d'organisation (OU). PowerShell fournit des cmdlets puissants qui simplifient le processus de récupération.

- [**Get-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps) Cette cmdlet vous permet de récupérer des informations détaillées sur les utilisateurs AD. Vous pouvez obtenir des attributs tels que le nom d'utilisateur, le nom d'affichage, l'adresse électronique, etc. Par exemple, pour récupérer tous les utilisateurs dont le nom commence par "johndoe", vous pouvez exécuter la commande suivante :

  ```powershell
  Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
  ```

  Cette commande renvoie une liste d'objets d'utilisateurs correspondant au filtre spécifié.

- [**Get-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps) La cmdlet Get-ADGroup permet d'obtenir des informations sur les groupes AD. Elle permet d'accéder à des détails tels que le nom du groupe, ses membres, sa description, etc. Par exemple, pour récupérer tous les groupes de sécurité dans l'environnement AD, vous pouvez exécuter la commande suivante :

  ```powershell
  Get-ADGroup -Filter 'GroupCategory -eq "Security"'
  ```

  Vous obtiendrez une liste des groupes de sécurité dans l'Active Directory.

- [**Get-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit?view=windowsserver2022-ps) La cmdlet Get-ADOrganizationalUnit est utilisée pour récupérer des informations sur les OU AD. Elle vous permet d'accéder à des propriétés telles que le nom de l'OU, la description, l'OU parent, etc. Pour récupérer tous les OU du domaine, vous pouvez utiliser la commande suivante :

  ```powershell
  Get-ADOrganizationalUnit -Filter *
  ```

  L'exécution de cette commande permet d'afficher une liste de tous les OU de l'Active Directory.

En utilisant ces puissantes cmdlets, vous pouvez facilement récupérer des informations spécifiques sur les utilisateurs, les groupes et les OU d'AD, ce qui permet une administration et une gestion efficaces de votre environnement Active Directory.

{{< inarticle-dark >}}


Ces cmdlets vous permettent de récupérer des attributs spécifiques, de filtrer les résultats et d'effectuer des requêtes avancées pour obtenir les informations souhaitées.

### Création et gestion des objets Active Directory

Lorsque vous travaillez avec Active Directory (AD), le module Active Directory de PowerShell offre de puissantes cmdlets pour créer et gérer des objets AD. Nous allons explorer quelques cmdlets essentielles pour créer des utilisateurs, des groupes et des unités d'organisation (OU) AD.

- [**New-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps) Cette cmdlet vous permet de créer un nouvel utilisateur AD. Vous pouvez spécifier des attributs tels que le nom d'utilisateur, le mot de passe, l'adresse électronique, etc. Par exemple, pour créer un nouvel utilisateur avec le nom d'utilisateur "john.doe" et le nom d'affichage "John Doe", vous pouvez utiliser la commande suivante :

  ```powershell
  New-ADUser -SamAccountName "john.doe" -Name "John Doe"
  ```

  Cette commande crée un nouvel utilisateur dans l'Active Directory.

- [**New-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adgroup?view=windowsserver2022-ps) La cmdlet New-ADGroup vous permet de créer un nouveau groupe AD. Vous pouvez définir des propriétés telles que le nom du groupe, la description, la portée du groupe, etc. Pour créer un nouveau groupe nommé "Marketing" avec une description, vous pouvez exécuter la commande suivante :

  ```powershell
  New-ADGroup -Name "Marketing" -Description "Marketing Team"
  ```

  Cette commande crée un nouveau groupe dans l'Active Directory.

- [**New-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adorganizationalunit?view=windowsserver2022-ps) La cmdlet New-ADOrganizationalUnit permet de créer une nouvelle OU AD. Vous pouvez spécifier des propriétés telles que le nom de l'OU, l'OU parent, etc. Par exemple, pour créer une nouvelle OU nommée "Sales" sous l'OU "Departments", vous pouvez exécuter la commande suivante :

  ```powershell
  New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"
  ```

  Cette commande crée une nouvelle OU dans la hiérarchie Active Directory.

Grâce à ces cmdlets, vous pouvez facilement créer de nouveaux utilisateurs, groupes et OU AD avec les propriétés et configurations souhaitées, ce qui permet une gestion efficace de votre environnement Active Directory.

{{< inarticle-dark >}}


### Modifier les objets Active Directory

Lorsqu'il s'agit de modifier les propriétés et les attributs d'objets Active Directory (AD) existants, le module Active Directory de PowerShell fournit plusieurs cmdlets utiles. Explorons ces cmdlets pour modifier les utilisateurs, les groupes et les unités d'organisation (OU) d'Active Directory.

- [**Set-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-aduser?view=windowsserver2022-ps) La cmdlet Set-ADUser vous permet de modifier les propriétés d'un utilisateur AD. Vous pouvez mettre à jour des attributs tels que le nom d'affichage, l'adresse électronique, le numéro de téléphone, etc. Par exemple, pour modifier le numéro de téléphone d'un utilisateur dont le nom d'utilisateur est "john.doe", vous pouvez utiliser la commande suivante :

  ```powershell
  Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
  ```

  Cette commande modifie le numéro de téléphone de l'utilisateur spécifié dans l'Active Directory.

- [**Set-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adgroup?view=windowsserver2022-ps) La cmdlet Set-ADGroup permet de modifier les propriétés d'un groupe AD. Vous pouvez mettre à jour des attributs tels que la description du groupe, les membres, la portée du groupe, etc. Pour modifier la description d'un groupe nommé "Marketing" en "Équipe marketing", vous pouvez exécuter la commande suivante :

  ```powershell
  Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
  ```

  Cette commande met à jour la description du groupe spécifié dans l'Active Directory.

- [**Set-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adorganizationalunit?view=windowsserver2022-ps) La cmdlet Set-ADOrganizationalUnit vous permet de modifier les propriétés d'une OU AD. Vous pouvez modifier des attributs tels que le nom de l'OU, sa description, etc. Par exemple, pour modifier la description d'une OU nommée "Sales" en "Sales Department", vous pouvez exécuter la commande suivante :

  ```powershell
  Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"
  ```

  Cette commande met à jour la description de l'OU spécifiée dans la hiérarchie Active Directory.

En utilisant ces cmdlets, vous pouvez facilement modifier les propriétés et les attributs des objets AD, en effectuant les mises à jour et les ajustements nécessaires pour répondre aux besoins de votre organisation.

{{< inarticle-dark >}}


### Gestion de la sécurité d'Active Directory

Outre la gestion et l'administration des objets Active Directory (AD), le module Active Directory de PowerShell fournit des cmdlets spécialement conçues pour gérer les aspects de sécurité d'AD. Ces cmdlets permettent aux administrateurs de gérer efficacement l'accès des utilisateurs, l'appartenance à des groupes et les tâches liées aux mots de passe dans l'environnement AD.

Voici quelques cmdlets de sécurité couramment utilisées :

- [**Add-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2022-ps) Cette cmdlet vous permet d'ajouter des membres à un groupe AD. En spécifiant le groupe AD et les comptes d'utilisateurs ou les groupes que vous souhaitez ajouter, vous pouvez facilement gérer le contrôle d'accès. Par exemple, pour ajouter un utilisateur nommé "JohnDoe" au groupe "Managers", vous pouvez utiliser la commande suivante :

  ```powershell
  Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
  ```

- [**Remove-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/remove-adgroupmember?view=windowsserver2022-ps) Cette cmdlet permet de supprimer des membres d'un groupe AD. En spécifiant le groupe AD et les comptes d'utilisateurs ou les groupes que vous souhaitez supprimer, vous pouvez gérer efficacement les appartenances à un groupe. Par exemple, pour supprimer un utilisateur nommé "JaneSmith" du groupe "Developers", vous pouvez utiliser la commande suivante :

  ```powershell
  Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
  ```

- [**Set-ADUserPassword**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adaccountpassword?view=windowsserver2022-ps) Cette cmdlet vous permet de définir le mot de passe d'un utilisateur AD. En spécifiant le compte d'utilisateur et en fournissant un nouveau mot de passe, vous pouvez appliquer des stratégies de mot de passe et garantir une authentification sécurisée de l'utilisateur. Voici un exemple de définition d'un nouveau mot de passe pour un utilisateur nommé "AmyJohnson" :

  ```powershell
  Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
  ```

En utilisant ces cmdlets de sécurité, les administrateurs peuvent gérer efficacement l'accès des utilisateurs, l'appartenance à des groupes et les stratégies de mot de passe dans l'environnement Active Directory.

## Exemple de script de module Active Directory pour PowerShell
```powershell
# Import Active Directory module
Import-Module ActiveDirectory

# Retrieve Active Directory information
Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
Get-ADGroup -Filter 'GroupCategory -eq "Security"'
Get-ADOrganizationalUnit -Filter *

# Create a new Active Directory user
New-ADUser -SamAccountName "john.doe" -Name "John Doe"

# Create a new Active Directory group
New-ADGroup -Name "Marketing" -Description "Marketing Team"

# Create a new Active Directory organizational unit
New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"

# Modify Active Directory objects
Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"

# Manage Active Directory security
Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
```

## Conclusion

En conclusion, le module **Active Directory pour PowerShell** est un outil puissant qui permet une gestion efficace et pratique de Windows Active Directory. En installant et en important le module, vous avez accès à un ensemble complet de **cmdlets** qui simplifient diverses tâches liées à AD.

Avec le module Active Directory, vous pouvez effectuer un large éventail d'opérations telles que la récupération d'informations sur les objets AD, la création de nouveaux objets, la modification des propriétés et la gestion de la sécurité. Ce module permet aux administrateurs d'automatiser les tâches administratives, de rationaliser les flux de travail et de garantir le bon fonctionnement des environnements Active Directory.

En tirant parti de **PowerShell** et du **Module Active Directory**, vous pouvez renforcer vos capacités d'administration AD et améliorer l'efficacité des processus de gestion AD. Que vous soyez administrateur système, professionnel de l'informatique ou responsable Active Directory, le module Active Directory vous fournit les outils nécessaires pour gérer efficacement votre infrastructure AD.

Profitez de la puissance de **PowerShell** et du **module Active Directory** pour rationaliser vos tâches d'administration AD, augmenter votre productivité et maintenir un environnement Active Directory sécurisé et bien organisé.

{{< inarticle-dark >}}

## Références

- [Install-WindowsFeature cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature)
- [Import-Module cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module)
- [Active Directory cmdlets in PowerShell - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/activedirectory)
