---
title: "Créer un inventaire Active Directory en lecture seule avec PowerShell"
date: 2026-10-10
lastmod: 2026-11-08
toc: true
draft: false
description: "Inventoriez les unités d’organisation, les utilisateurs et les ordinateurs Active Directory avec des requêtes PowerShell ciblées. Exportez des fichiers CSV vérifiables sans modifier les objets de l’annuaire."
genre: ["Active Directory", "PowerShell", "Administration système"]
tags: ["Inventaire Active Directory", "Inventaire AD PowerShell", "Get-ADUser", "Get-ADComputer", "Get-ADOrganizationalUnit", "Get-ADDomain", "SearchBase", "AD en lecture seule", "Export d’utilisateurs AD", "Export d’ordinateurs AD", "Export d’OU AD", "Export-Csv", "RSAT", "Audit d’annuaire", "Rapports AD", "Inventaire d’OU", "Windows Server", "Script PowerShell", "Module AD", "Hygiène d’annuaire"]
cover: "/img/cover/active-directory-powershell-read-only-inventory.webp"
coverAlt: "Arborescence Active Directory dont les enregistrements d’utilisateurs, d’ordinateurs et d’unités d’organisation alimentent trois fichiers de vérification."
coverCaption: "Limitez la portée de la requête, puis exportez uniquement les champs nécessaires à la vérification."
---
Un nettoyage d’Active Directory commence par une liste fiable des objets existants. Cet **inventaire en lecture seule** rassemble les unités d’organisation, les utilisateurs et les ordinateurs d’un périmètre choisi. Il exporte trois fichiers CSV (valeurs séparées par des virgules) à vérifier, sans modifier les objets de l’annuaire. Protégez tout de même ces fichiers, car les noms et les détails des appareils révèlent une partie de votre environnement.

<!--more-->

## Points essentiels

- **Choisissez un périmètre :** interrogez une unité d’organisation avant d’étendre la recherche à tout le domaine.
- **Utilisez des commandes de lecture :** `Get-ADOrganizationalUnit`, `Get-ADUser` et `Get-ADComputer` récupèrent des objets.
- **Sélectionnez les champs :** exportez uniquement les propriétés nécessaires à la tâche.
- **Vérifiez le résultat :** comparez le nombre d’objets et quelques lignes avant de vous fier au rapport.

## Avant de commencer

Il vous faut un hôte d’administration Windows avec un DNS fonctionnel et un accès réseau à un contrôleur de domaine, le module PowerShell **ActiveDirectory**, un compte autorisé à lire les objets sélectionnés et un dossier protégé pour les fichiers CSV. Sur un client Windows, le module provient des outils Active Directory des Remote Server Administration Tools (RSAT). Le [guide du module Active Directory](/articles/active-directory-module-powershell-installation-usage-guide/) explique l’installation. Microsoft fournit la [référence des cmdlets](https://learn.microsoft.com/en-us/powershell/module/activedirectory/) du module et les [options d’installation de RSAT](https://learn.microsoft.com/windows-server/remote/remote-server-administration-tools). Ce guide utilise la syntaxe Windows PowerShell et ne modifie aucun objet de l’annuaire.

Les autorisations de l’annuaire restent applicables. Dans ses [conseils sur les comptes privilégiés](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory), Microsoft explique que les listes de contrôle d’accès autorisent souvent les utilisateurs authentifiés à lire les informations générales, tout en limitant l’accès aux champs sensibles et aux modifications. Commencez avec un compte approuvé et une OU de test. N’accordez pas les droits Domain Admin pour faire réussir un inventaire.

> **Avertissement :** les fichiers CSV contiennent des noms de comptes et d’ordinateurs. Enregistrez-les dans un emplacement approuvé, limitez les accès et supprimez les copies supplémentaires après vérification. Ne publiez pas un export brut et ne le joignez pas à une issue publique.

## Choisir la base de recherche

Une **unité d’organisation (OU)** regroupe des objets de l’annuaire. Son **nom unique (DN)** indique sa position dans l’arborescence. Le paramètre `-SearchBase` limite une requête au DN choisi. Sans périmètre défini volontairement, un filtre large peut renvoyer bien plus d’objets que nécessaire.

Chargez d’abord le module et affichez le DN du domaine actuel :

```powershell
Import-Module ActiveDirectory
(Get-ADDomain).DistinguishedName
```

Microsoft documente [Get-ADDomain](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-addomain) et les informations de domaine renvoyées par cette cmdlet. Repérez l’OU à examiner avant de définir la base de recherche :

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase (Get-ADDomain).DistinguishedName |
    Select-Object Name, DistinguishedName
```

Copiez le DN exact du résultat. Dans les exemples suivants, remplacez cette valeur de documentation par le DN de votre OU :

```powershell
$SearchBase = 'OU=Lab,DC=example,DC=com'
```

`example.com` est un domaine de documentation. Ne copiez pas son DN dans une requête réelle. Si vous avez délibérément besoin d’un inventaire de tout le domaine, affectez le DN du domaine à `$SearchBase` et consignez ce périmètre plus large dans le rapport. La [référence Get-ADOrganizationalUnit](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit) de Microsoft documente `-Filter` et `-SearchBase`.

## Inventorier les OU, les utilisateurs et les ordinateurs

Commencez par compter les objets. Ce contrôle aide à repérer rapidement une base de recherche incorrecte ou un résultat vide inattendu :

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADUser -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADComputer -Filter * -SearchBase $SearchBase | Measure-Object
```

`-Filter *` récupère tous les objets correspondants dans la base de recherche. Microsoft documente [Get-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser) et [Get-ADComputer](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) comme des commandes de récupération. Un décompte nul peut être normal, mais vérifiez le DN, les autorisations et le domaine cible avant de considérer l’inventaire comme complet.

Affichez maintenant quelques lignes dans la console. Enregistrez les champs sélectionnés afin que l’aperçu et l’export CSV utilisent les mêmes colonnes :

```powershell
$UserFields = 'Name', 'SamAccountName', 'Enabled', 'DistinguishedName'
Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields -First 10
```

Pour les ordinateurs, demandez la propriété supplémentaire du système d’exploitation uniquement si votre vérification en a besoin :

```powershell
$ComputerFields = @(
    'Name', 'DNSHostName', 'OperatingSystem',
    'Enabled', 'DistinguishedName'
)
Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields -First 10
```

Le paramètre `-Properties` demande des propriétés qui ne figurent pas dans l’ensemble par défaut de la cmdlet. La [référence de la cmdlet des ordinateurs](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) de Microsoft le documente. Traitez les noms de système d’exploitation comme des données d’annuaire, et non comme une preuve de la version actuellement installée. Un objet ordinateur peut être obsolète ou son attribut peut ne pas avoir été actualisé.

## Exporter des fichiers CSV vérifiables

Choisissez un dossier de sortie approuvé avec suffisamment d’espace libre. Les commandes suivantes écrivent des **fichiers CSV locaux** et ne modifient pas les objets de l’annuaire. Exécutez-les dans ce dossier. `-NoClobber` empêche l’écrasement d’un fichier existant. Utilisez un nouveau dossier ou nom de fichier à chaque exécution.

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase |
    Select-Object Name, DistinguishedName |
    Export-Csv -Path .\ad-ous.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields |
    Export-Csv -Path .\ad-users.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields |
    Export-Csv -Path .\ad-computers.csv -NoTypeInformation -Encoding UTF8 -NoClobber
```

La [référence Export-Csv](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv?view=powershell-5.1) de Microsoft explique `-NoTypeInformation`, `-Encoding` et `-NoClobber`. Ouvrez chaque fichier CSV dans un éditeur de texte ou un tableur approuvé. Vérifiez l’en-tête, quelques lignes et le nombre d’enregistrements par rapport au décompte précédent. Une commande en échec ou un fichier de zéro octet ne prouve pas que le rapport est complet.

> **Résultat attendu :** vous disposez de trois fichiers CSV contenant les enregistrements OU, utilisateurs et ordinateurs du périmètre choisi. Le nombre de lignes et les exemples correspondent au périmètre de l’annuaire sélectionné.

## Vérifier sans modifier les objets

Utilisez l’inventaire pour répondre à des questions précises : quelle OU gère un ordinateur ? Quels comptes utilisateur sont désactivés ? Quels noms d’appareils ont besoin d’un propriétaire ? Consignez vos constats dans une note de vérification distincte. Ne déduisez pas de la valeur `Enabled` qu’un compte est encore nécessaire ou non. Ne supprimez et ne désactivez aucun objet sur la seule base d’un export.

Pour un rapport récurrent, consignez la date de la requête, le domaine, le DN de l’OU, les propriétés sélectionnées, l’opérateur et l’emplacement du CSV. Avant de comparer deux exports, vérifiez qu’ils utilisent le même périmètre et les mêmes champs. Sinon, un écart peut venir de la requête plutôt que d’un changement réel de l’annuaire.

Il s’agit d’un **inventaire**, pas d’un audit des comptes privilégiés ni d’un rapport d’activité de connexion. Microsoft précise que les propriétés et les autorisations Active Directory varient selon l’objet et l’environnement. Vérifiez un attribut de système d’exploitation ou un nom d’affichage auprès du responsable système avant d’agir. Le [guide de sécurité Active Directory](/articles/active-directory-security-best-practices/) couvre les contrôles de sécurité plus larges.

## Dépannage

- **Le module ne s’importe pas :** vérifiez que les outils Active Directory de RSAT ou les outils d’administration Windows Server sont installés sur l’hôte. Consultez le [guide de configuration du module](/articles/active-directory-module-powershell-installation-usage-guide/).
- **La requête ne renvoie aucun objet :** vérifiez le DN exact, le domaine actuel, le contenu de l’OU et les droits de lecture. Testez d’abord une petite OU connue avant d’élargir le périmètre.
- **Une propriété est vide :** vérifiez que l’attribut existe et que votre compte peut le lire. Ne complétez pas les champs manquants par des suppositions.
- **L’export indique que le fichier existe déjà :** `-NoClobber` a protégé le rapport précédent. Choisissez un nouveau nom de fichier ou dossier et relancez la commande.
- **Le nombre diffère des attentes :** vérifiez si des utilisateurs ou des ordinateurs se trouvent dans une autre OU, si le périmètre a changé et si l’annuaire a été modifié pendant la requête.

## Étapes suivantes

Conservez les fichiers CSV bruts dans un emplacement protégé pendant la période de vérification convenue. Ne partagez que les champs nécessaires au réviseur. Une fois les constats confirmés par leurs responsables, planifiez les modifications selon votre procédure habituelle d’approbation et de retour arrière. Après les changements approuvés, relancez le même inventaire sur le même périmètre pour confirmer le résultat.