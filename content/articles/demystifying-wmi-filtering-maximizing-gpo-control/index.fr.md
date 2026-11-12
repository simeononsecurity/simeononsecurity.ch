---
title: "Comprendre le filtrage WMI"
date: 2023-07-25
lastmod: 2026-11-12
toc: true
draft: false
description: "Découvrez le filtrage WMI et son utilisation pour mieux cibler les objets de stratégie de groupe (GPO), avec des exemples pratiques et des bonnes pratiques."
genre: ["Gestion Windows", "Stratégie de groupe", "Administration système", "Gestion réseau", "Infrastructure informatique", "Gestion des stratégies", "Gouvernance informatique", "Automatisation informatique", "Active Directory", "Conformité de sécurité"]
tags: ["filtrage WMI", "GPO", "objets de stratégie de groupe", "filtres WMI", "ciblage des stratégies", "requêtes WMI", "Windows Management Instrumentation", "contrôle des GPO", "console de gestion des stratégies de groupe", "langage de requête WMI", "application des stratégies", "WQL", "affiner les stratégies", "gestion des stratégies", "ressources système", "exemples de ciblage des stratégies", "administration système", "gestion réseau", "gestion de l’infrastructure informatique", "automatisation informatique", "gestion Active Directory", "conformité de sécurité", "techniques de contrôle des stratégies", "bonnes pratiques de gestion des stratégies", "filtrage des stratégies", "stratégies de contrôle des GPO", "sécurité des GPO", "avantages du filtrage WMI", "mise en œuvre du filtrage WMI", "bonnes pratiques du filtrage WMI"]
cover: "/img/cover/An_illustration_of_a_magnifying_glass_focusing.webp"
coverAlt: "Illustration d’une loupe dirigée vers une icône de filtre, symbole du ciblage des GPO par le filtrage WMI."
coverCaption: "Utilisez le filtrage WMI pour cibler efficacement les stratégies de groupe !"
---

## Introduction

Dans les objets de stratégie de groupe (GPO), le [**filtrage WMI**](https://simeononsecurity.com/github/wmi-filters/) joue un rôle essentiel. Il limite l’application des stratégies à certains ordinateurs ou utilisateurs selon les résultats de requêtes WMI (Windows Management Instrumentation). Cette fonction permet aux administrateurs d’affiner le ciblage et de n’appliquer les stratégies qu’aux systèmes souhaités. Cet article présente le filtrage WMI, son fonctionnement dans les GPO, la création de [filtres WMI](https://simeononsecurity.com/github/wmi-filters/) et des exemples pratiques.

## [Qu’est-ce que le filtrage WMI ?](https://simeononsecurity.com/github/wmi-filters/)

Le [**filtrage WMI**](https://simeononsecurity.com/github/wmi-filters/) consiste à appliquer des filtres aux GPO selon les résultats de requêtes WMI. WMI est une infrastructure de gestion intégrée à Windows. Elle permet aux administrateurs de récupérer des données de gestion et d’interagir par programmation avec les ressources du système. Le filtrage WMI permet de cibler dynamiquement les GPO selon des critères précis renvoyés par les requêtes.

Les filtres WMI utilisent le langage de requête WMI (WQL), un sous-ensemble de SQL (Structured Query Language). Ils s’appuient généralement sur les propriétés et valeurs disponibles dans un espace de noms WMI. Les administrateurs peuvent combiner des conditions, des opérateurs logiques et des espaces de noms pour construire des requêtes qui ciblent précisément des ordinateurs ou des utilisateurs.

## Comment le filtrage WMI fonctionne-t-il dans les GPO ?

{{< figure src="wmi-filtering-gpo-evaluation-flow.webp" alt="Organigramme montrant un filtre WMI associé à un objet de stratégie de groupe qui évalue une requête WQL à vrai ou faux pour décider si la GPO s’applique à un ordinateur" >}}

Dans une stratégie de groupe, le **filtrage WMI** permet d’appliquer sélectivement les GPO selon l’évaluation de **requêtes WMI**. En associant un **filtre WMI** à une GPO, l’administrateur détermine si le filtre renvoie **True** ou **False** et contrôle ainsi l’application de la GPO.

Les filtres utilisent le **langage de requête WMI (WQL)**, un sous-ensemble de SQL (Structured Query Language). WQL permet de créer des requêtes complexes fondées sur les **propriétés** et les **valeurs** disponibles dans un **espace de noms WMI**. Cela permet de cibler précisément certains ordinateurs ou utilisateurs.

Par exemple, une organisation peut vouloir appliquer une GPO uniquement aux ordinateurs exécutant Windows 10. Elle peut créer un filtre WMI qui vérifie la propriété **OperatingSystem** de la classe **Win32_OperatingSystem**. La requête WMI peut ressembler à ceci :

```sql
SELECT * FROM Win32_OperatingSystem WHERE Version LIKE "10.%"
```

Cette requête vérifie si la version du système d’exploitation commence par « 10. », ce qui indique Windows 10. Si la requête renvoie **True**, la GPO s’applique à l’ordinateur cible. Sinon, elle ne s’applique pas.

Le filtrage WMI prend aussi en charge des conditions et opérateurs logiques comme **AND**, **OR** et **NOT**. Les administrateurs peuvent combiner plusieurs propriétés et valeurs pour contrôler plus finement l’application des GPO.

Ils peuvent également utiliser différents **espaces de noms WMI** pour accéder à des ensembles précis de classes et de propriétés WMI. Ils peuvent ainsi cibler les GPO selon le matériel, les logiciels installés, la configuration réseau et d’autres critères.

Pour en savoir plus sur la création de filtres et de requêtes WMI, consultez la documentation Microsoft sur le [filtrage WMI pour la stratégie de groupe](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo).

Le filtrage WMI permet donc d’adapter l’application des GPO aux ordinateurs ou utilisateurs selon des conditions dynamiques et d’améliorer la gestion de l’environnement informatique.

## Créer des filtres WMI pour les GPO

Pour créer un filtre WMI pour une GPO, procédez comme suit :

1. Ouvrez la **console de gestion des stratégies de groupe** (GPMC) sur un ordinateur Windows joint au domaine.

2. Développez le domaine, puis sélectionnez le nœud **Filtres WMI**.

3. Cliquez avec le bouton droit sur **Filtres WMI**, puis sélectionnez **Nouveau**.

4. Donnez un nom explicite au filtre et saisissez la requête WMI dans le champ **Requête**. Utilisez la syntaxe WQL.

5. Cliquez sur **OK** pour enregistrer le filtre WMI.

Une fois créé, le filtre peut être associé à une ou plusieurs GPO. Pour l’associer à une GPO, procédez ainsi :

1. Cliquez avec le bouton droit sur la GPO souhaitée, puis sélectionnez **Propriétés**.

2. Dans la fenêtre des propriétés de la GPO, ouvrez l’onglet **Filtrage WMI**.

3. Sélectionnez le filtre WMI souhaité dans la liste.

4. Cliquez sur **OK** pour enregistrer les modifications.

L’association de filtres WMI aux GPO permet de cibler précisément l’application des stratégies selon les résultats des requêtes WMI.

## Combien de filtres WMI peut-on configurer pour une GPO ?

Pour une GPO, les administrateurs peuvent configurer **plusieurs filtres WMI** afin d’affiner le ciblage. Aucun nombre maximal précis de filtres associés à une seule GPO n’est défini, ce qui permet de construire des combinaisons complexes.

Il faut toutefois tenir compte de l’effet du nombre de filtres sur le temps de traitement des GPO. Plus il y a de filtres, plus l’évaluation et l’application des GPO peuvent prendre du temps. Pour maintenir un traitement efficace, il est conseillé de limiter leur nombre à une quantité raisonnable.

Par exemple, une organisation peut appliquer une GPO uniquement aux ordinateurs sous Windows 10 qui exécutent un logiciel donné. Elle peut créer deux filtres WMI distincts, l’un pour le **système d’exploitation** et l’autre pour **l’installation du logiciel**. La combinaison des filtres cible alors les ordinateurs concernés.

Il faut trouver un équilibre entre le nombre de filtres nécessaires au ciblage et le temps de traitement. Avant de choisir combien de filtres configurer, les administrateurs doivent évaluer la complexité de l’environnement, le nombre d’ordinateurs ou d’utilisateurs et les conséquences sur les performances.

La prise en charge de plusieurs filtres WMI permet d’optimiser le ciblage des GPO tout en conservant un traitement et une gestion efficaces de l’environnement informatique.

## Exemples pratiques de filtrage WMI dans les GPO

Le filtrage WMI dans les GPO permet d’appliquer des stratégies de façon ciblée. Voici quelques exemples :

1. **Cibler des systèmes d’exploitation précis** : pour appliquer une GPO uniquement aux ordinateurs **Windows 10**, créez un filtre qui vérifie la version du système, par exemple `"SELECT * FROM Win32_OperatingSystem WHERE Version LIKE '10.%'"`. Cela cible les ordinateurs Windows 10.

2. **Appliquer des stratégies différentes aux ordinateurs de bureau et aux portables** : si les stratégies diffèrent selon le type d’appareil, utilisez deux filtres WMI. Le premier peut reconnaître les ordinateurs de bureau à l’aide d’attributs matériels, comme `"SELECT * FROM Win32_ComputerSystem WHERE Desktop = True"`, et le second peut identifier les portables. Vous pouvez ainsi appliquer une stratégie adaptée à chaque type d’appareil.

3. **Appliquer une stratégie selon l’espace disque** : pour éviter d’appliquer des stratégies gourmandes en ressources aux ordinateurs dont l’espace disque est limité, créez un filtre qui vérifie l’espace disponible. Par exemple, la requête `"SELECT * FROM Win32_LogicalDisk WHERE FreeSpace > 10737418240"` exclut les ordinateurs disposant de moins de 10 Go d’espace libre.

Ces exemples montrent la souplesse du **filtrage WMI** dans les GPO. Les administrateurs peuvent cibler l’application des stratégies selon des critères précis.

## Conclusion

Le filtrage WMI est une fonction utile des objets de stratégie de groupe. Il permet aux administrateurs d’appliquer des stratégies de façon sélective selon les résultats des requêtes WMI. Les filtres WMI ciblent précisément les ordinateurs ou utilisateurs et rendent la gestion des stratégies plus efficace et mieux contrôlée. Cet article a présenté le filtrage WMI, son fonctionnement dans les GPO, la création de filtres et des exemples pratiques.

En intégrant le filtrage WMI à la gestion des GPO, vous améliorez la précision de l’application des stratégies et veillez à ce qu’elles s’appliquent uniquement aux cibles prévues.

## Références

- [Microsoft Docs : créer des filtres WMI pour la GPO](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/create-wmi-filters-for-the-gpo)
- [Microsoft Docs : about_WQL](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_wql?view=powershell-5.1)
- [Microsoft Docs : stratégie de groupe](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects)
- [Microsoft Docs : console de gestion des stratégies de groupe](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn265969(v=ws.11))
