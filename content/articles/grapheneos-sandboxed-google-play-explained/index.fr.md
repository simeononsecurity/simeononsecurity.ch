---
title: "Sandboxed Google Play sur GrapheneOS expliqué"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Découvrez ce que change Sandboxed Google Play sur GrapheneOS, quand un profil distinct est utile et comment s’articulent comptes, notifications et compatibilité des applications."
genre: ["Confidentialité", "Sécurité mobile", "Open source"]
tags: ["GrapheneOS", "sandboxed Google Play", "Google Play services", "Google Play Store", "confidentialité Android", "sécurité Android", "bac à sable d’application", "compte Google", "profils GrapheneOS", "profil propriétaire", "profils utilisateur", "profil professionnel", "compatibilité des applications", "notifications push", "Firebase Cloud Messaging", "autorisations d’application", "confidentialité Pixel", "installation de Google Play", "confidentialité mobile", "GrapheneOS App Store"]
cover: "/img/cover/grapheneos-sandboxed-google-play-explained.webp"
coverAlt: "L’écran d’un smartphone affiche des applications dans des compartiments transparents distincts, dont un symbole coloré de boutique d’applications."
coverCaption: ""
---

**Sandboxed Google Play** permet d’installer les composants officiels de Google Play sur GrapheneOS comme des applications ordinaires. Ils fonctionnent sans les privilèges système que Google Play reçoit normalement sur le système d’exploitation standard. L’installation reste facultative. [Présentation des fonctionnalités de GrapheneOS](https://grapheneos.org/features#sandboxed-google-play).

## À retenir

- **Comprenez l’isolation :** distinguez les autorisations des applications de l’activité des comptes en ligne.
- **Regroupez les dépendances :** placez l’application dépendante et Play dans le même profil.
- **Testez le fonctionnement :** vérifiez les notifications en arrière-plan et les tâches essentielles.
- **Préparez un plan :** notez les profils, comptes et besoins des applications que vous avez choisis.

## Avant de commencer

**Public visé :** les utilisateurs de GrapheneOS qui décident d’installer ou non Google Play et de son emplacement. **Prérequis :** un appareil pris en charge, GrapheneOS à jour et l’accès à vos comptes essentiels. L’installation du système est expliquée dans le [guide d’installation de GrapheneOS](/guides/how-to-install-graphine-os/).

**Temps estimé :** 20 à 30 minutes pour dresser l’inventaire initial des applications et effectuer les vérifications, puis une utilisation quotidienne normale pour évaluer la fiabilité des notifications. **Difficulté :** débutant. Commencez par une application représentative avant de réorganiser votre téléphone.

## Ce que change le bac à sable

Le **bac à sable des applications** Android sépare les ressources des applications au moyen des protections du système d’exploitation. Une application ne reçoit pas un accès illimité aux fichiers privés d’une autre. Cette protection s’applique au code natif comme au code exécuté dans l’environnement Android géré. [Documentation sur le bac à sable des applications Android](https://source.android.com/docs/security/app-sandbox).

GrapheneOS ajoute une **couche de compatibilité** pour que les composants officiels de Play fonctionnent sous ces restrictions ordinaires. Les applications d’un même profil disposent encore de moyens pris en charge pour communiquer d’un commun accord. Le bac à sable limite les privilèges, mais n’empêche pas tout échange volontaire entre applications. [Conception de Sandboxed Google Play](https://grapheneos.org/features#sandboxed-google-play).

| Sujet | Signification pratique |
|---|---|
| **Fichiers privés des applications** | Installer Play ne donne pas un accès illimité aux données des autres applications |
| **Autorisations** | Examinez l’accès demandé comme pour toute autre application |
| **Fonctions liées à Google** | Une application qui choisit un service Google continue de communiquer avec lui |
| **Activité du compte** | Se connecter à un service reste une décision distincte en matière de confidentialité |

**Le bac à sable et la confidentialité du compte** répondent à des questions différentes. Le bac à sable restreint l’accès local. Il n’efface pas les informations que vous transmettez volontairement à un service en ligne. Par exemple, vous connecter à une application d’achat identifie toujours votre compte auprès de son opérateur.

## Distinguez trois décisions de confidentialité

**L’accès local, l’utilisation des services et l’identité** sont des questions distinctes. Si une application demande l’accès aux contacts et la connexion à un compte, examinez chaque demande séparément :

| Décision | Question |
|---|---|
| **Autorisation locale** | Cette fonction a-t-elle besoin de mes contacts, de mon microphone ou de ma position ? |
| **Dépendance à un service** | Quelle fonction dépend de Play services ? |
| **Identité en ligne** | À quel compte associer cette activité ? |

**Exemple concret :** un compte d’achat contient déjà votre adresse de livraison. Déplacer l’application dans un autre profil ne change pas l’adresse détenue par le commerçant. Refuser l’accès aux contacts concerne une autre question, celle des données présentes sur votre téléphone.

**Objectif de confidentialité :** notez l’exposition précise que vous souhaitez réduire. « Empêcher cette application d’accéder à mes contacts personnels » est vérifiable. « Rendre ce compte anonyme » demande d’autres décisions que le choix du profil.

## Profil propriétaire ou profil distinct ?

**Installer dans le profil propriétaire** est une option prise en charge et simple. Google Play y reste sandboxé. Un profil utilisateur ou professionnel distinct permet de choisir le groupe d’applications qui a accès à Play. [Conseils d’installation de GrapheneOS](https://grapheneos.org/usage#sandboxed-google-play-installation).

| Votre priorité | Configuration de départ | Compromis |
|---|---|---|
| **Simplicité au quotidien** | Garder les applications requises et Play dans le profil Propriétaire | Play est accessible aux applications qui coopèrent dans ce profil |
| **Séparer les applications dépendantes de Google** | Les installer ensemble dans un autre profil | Davantage de gestion des profils |
| **Éviter les services Google** | Commencer sans Play | Vérifier les dépendances de chaque application |

**Le choix du profil** compte davantage que l’installation des mêmes composants partout. La FAQ de GrapheneOS explique que l’accès à Play se limite aux profils sélectionnés. Beaucoup d’applications fonctionnent sans Play ou n’en ont besoin que pour une partie de leurs fonctions. [FAQ sur les services Google](https://grapheneos.org/faq#google-services).

*Utilisez un profil distinct lorsque l’accès sélectif à Play répond à un besoin précis que vous avez identifié.*

## Comprenez l’activité des profils

**Un profil utilisateur secondaire** possède ses propres instances d’applications et ses propres données. Passer à un autre utilisateur et terminer la session de l’utilisateur précédent sont deux actions différentes. **Terminer la session** arrête les applications du profil secondaire et remet son stockage chiffré au repos. [FAQ de GrapheneOS sur le chiffrement et les profils](https://grapheneos.org/faq#encryption).

**Le transfert des notifications** peut afficher à l’utilisateur actif les notifications d’un utilisateur qui fonctionne en arrière-plan. Il ne maintient pas une session terminée. [Fonctions des profils utilisateur GrapheneOS](https://grapheneos.org/features).

| État du profil | Condition de réception |
|---|---|
| **Actif** | Testez la réception dans ce profil |
| **Actif en arrière-plan** | Vérifiez le transfert vers l’utilisateur actif |
| **Session terminée** | Les applications de ce profil sont arrêtées |

Pour **une application de messagerie utilisée chaque jour**, déterminez s’il est essentiel de recevoir des messages pendant l’utilisation du profil Propriétaire. Une configuration qui exige de terminer souvent les sessions ne convient pas à la réception continue en arrière-plan. Faites ce choix avant de déplacer votre historique de conversations principal.

## Installation et comptes

Ouvrez le **GrapheneOS App Store** intégré, sélectionnez **Google Play services** et installez-le. Le Play Store qui en dépend sera également installé. Laissez l’App Store gérer ces composants. Exemptez Play services de l’optimisation de la batterie pour assurer la fiabilité des fonctions en arrière-plan, comme les notifications push. [Instructions officielles d’installation](https://grapheneos.org/usage#sandboxed-google-play-installation).

**La connexion à un compte Google** est facultative pour les fonctions qui ne dépendent pas d’un compte. L’installation d’applications par le Play Store exige une connexion. Les anciennes installations comprennent aussi Google Services Framework, que le projet recommande de conserver. Suivez les instructions actuelles au lieu d’une ancienne liste de trois paquets.

## Testez d’abord une application

Utilisez une **application représentative à faible risque** pour vérifier la configuration prévue. Gardez vos méthodes actuelles de récupération de compte disponibles pendant le test.

1. **Choisir un profil :** décidez où l’application doit se trouver avant d’installer ses dépendances.
2. **Installer Play :** suivez dans ce profil les étapes officielles ci-dessus.
3. **Installer l’application :** utilisez une source de distribution fiable et terminez la configuration initiale.
4. **Examiner les demandes :** accordez les autorisations correspondant à la fonction testée.
5. **Essayer une fonction :** envoyez un message, ouvrez une carte ou effectuez une autre action réversible.
6. **Consigner le résultat :** notez les versions de l’application et du système, le profil et l’opération exacte.

**Résultat attendu :** une description reproductible, par exemple « un message test est arrivé, écran verrouillé, dans le profil actif ». Évitez de noter seulement « fonctionne », car cela ne précise ni la fonction ni les conditions testées.

## Diagnostiquer l’absence de notifications

Les **notifications push** dépendent de l’implémentation de l’application. Certaines maintiennent leur propre connexion en arrière-plan. D’autres s’appuient sur Firebase Cloud Messaging de Google. Le fait qu’une application s’ouvre ne prouve pas que ses notifications arrivent après le verrouillage du téléphone. [FAQ GrapheneOS sur les notifications](https://grapheneos.org/faq#notifications).

**Vérifiez les conditions de réception** avant de modifier les autorisations de plusieurs applications :

| Symptôme | Piste à vérifier |
|---|---|
| **Les messages apparaissent seulement après l’ouverture** | Vérifiez le mode de réception en arrière-plan et les réglages de batterie |
| **La réception fonctionne seulement dans son profil** | Vérifiez l’activité du profil et le transfert des notifications |
| **Aucune réception après « Terminer la session »** | Redémarrez le profil secondaire avant de refaire le test |
| **La notification arrive sans son** | Vérifiez le canal de notification et les réglages sonores de l’application |

Les **canaux de notification** regroupent le comportement des notifications d’une application, notamment leur importance et leur son. Android donne à l’utilisateur accès aux réglages des canaux. [Documentation Android sur les canaux de notification](https://developer.android.com/develop/ui/compose/notifications/channels).

**Refaites le test en ne changeant qu’une condition à la fois :** gardez l’appareil émetteur et le type de message fixes, puis changez l’état du profil destinataire. Notez « actif », « actif en arrière-plan » ou « session terminée » pour chaque résultat. Vous pourrez distinguer un problème de cycle de vie du profil d’un problème de configuration des notifications.

## Évaluez les tâches essentielles

Avant de vous fier à une nouvelle configuration, effectuez un court **test d’acceptation personnel** :

| Tâche | Vérification sur votre appareil |
|---|---|
| **Messagerie** | Recevoir un message écran verrouillé |
| **Accès au compte** | Se connecter et valider le second facteur requis |
| **Banque ou paiements** | Tester la fonction exacte dont vous avez besoin, y compris les contrôles de l’appareil |
| **Navigation** | Obtenir la position avec les autorisations choisies |

**Le lancement d’une application** n’est que le premier contrôle. Pour diagnostiquer un problème, notez les versions de l’application et de GrapheneOS ainsi que l’opération qui a échoué. Cet article propose une méthode de décision, pas une liste de compatibilité testée.

**Décision de migration :** gardez votre ancien moyen d’accès jusqu’à la réussite de chaque opération essentielle. Une application de messagerie et une application bancaire ont des critères d’acceptation différents. La réception d’un message ne renseigne pas sur les contrôles de compte ou d’appareil d’une autre application.

**Refaites les vérifications après une mise à jour de GrapheneOS ou des applications.** Le profil, les autorisations, les canaux de notification et l’état de la session définissent toujours le test. Notez la version avec chaque résultat afin qu’un changement de notification ou de connexion ne devienne pas une conclusion injustifiée sur la confidentialité.

Pour **une connexion professionnelle**, testez toute la séquence de connexion et le second facteur requis. Pour une application de voyage, testez la fonction dont vous aurez besoin hors de chez vous. Choisissez des actions représentatives sans faire d’achats inutiles ni modifier la sécurité du compte.

## Préparez votre plan d’applications

Complétez cet **inventaire** pour vos cinq applications principales. Les lignes ci-dessous sont des pistes, pas des affirmations de compatibilité pour des produits précis :

| Catégorie d’application | Besoin à consigner | Preuve à recueillir |
|---|---|---|
| **Messagerie** | Réception en arrière-plan et profil choisi | Test écran verrouillé et profil en arrière-plan |
| **Accès professionnel** | Connexion requise et second facteur | Connexion terminée |
| **Navigation** | Autorisation de position et besoins hors ligne | Un itinéraire dans les conditions prévues |
| **Banque** | Opérations essentielles prises en charge | Résultats pour chaque fonction nécessaire |
| **Achats** | Accès au compte et aux données locales | Vérification des autorisations et usage normal du compte |

**Consignez une décision** pour chaque ligne : profil choisi, dépendance à Play, compte requis, autorisations accordées et solution de repli. Gardez les dépendances inconnues comme telles jusqu’à l’obtention de preuves. Vous éviterez ainsi d’installer des composants supplémentaires simplement parce qu’une autre application en avait besoin.

**Exercice :** une application fonctionne lorsque son profil secondaire est actif, puis cesse de recevoir des messages après la fin de la session. Commencez par redémarrer le profil et refaire le test. Accorder l’accès aux contacts ne résoudrait pas une session arrêtée.

**Critère de fin :** votre plan explique pourquoi chaque application se trouve dans son profil et quel test justifie de vous y fier. Réexaminez la ligne correspondante après une mise à jour qui modifie le comportement.

## Étapes suivantes

Si GrapheneOS n’est pas encore installé, consultez le [guide d’installation de GrapheneOS](/guides/how-to-install-graphine-os/). Choisissez ensuite une configuration de profils et testez vos applications essentielles avant d’ajouter d’autres profils ou de modifier largement les autorisations.
