---
title: "Projets ChatGPT et Claude : configurer un contexte d’IA réutilisable"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Configurez des projets ChatGPT et Claude avec des consignes ciblées, des fichiers de référence à jour et un test simple du contexte réutilisé."
genre: ["Intelligence artificielle", "Productivité"]
tags: ["Projets ChatGPT", "Projets Claude", "consignes de projet IA", "contexte IA", "configuration de projet ChatGPT", "connaissances de projet Claude"]
cover: "/img/cover/effective-ai-chat-projects.webp"
coverAlt: "Deux espaces de projet IA organisés avec un brief, des fichiers de référence et des conversations séparées"
coverCaption: ""
---

[Retour au cours sur les workflows pratiques avec l’IA](/effective-ai-course-start/)

**Créez un projet lorsque plusieurs conversations partagent le même objectif.** Regroupez les consignes stables et les fichiers de référence approuvés. Gardez chaque conversation centrée sur une tâche. Cette leçon propose un atelier communautaire fictif pour vous entraîner sans données privées.

**Objectif pédagogique :** vous créerez un projet avec deux sources contrôlées et vérifierez leurs faits dans une nouvelle conversation.

## À retenir

- **Les consignes du projet** définissent un comportement réutilisable pour des conversations liées.
- **Les sources du projet** contiennent les références que vous voulez faire consulter par l’assistant.
- **L’historique de conversation** conserve la trace d’un échange, mais ne remplace pas une source approuvée.
- **Un test dans une nouvelle conversation** montre si la configuration fournit assez de contexte.

## Avant de commencer

**Prérequis :** un compte ChatGPT ou Claude, ainsi que le dossier d’exercice de la [leçon 1](/articles/effective-ai-workflow-foundations/). Prévoyez 35 minutes. Le niveau est débutant. Utilisez des noms, dates et lieux fictifs pendant toute l’exercice.

**Créez deux petits fichiers** sur votre ordinateur. Ouvrez un éditeur de texte brut, collez chaque bloc ci-dessous dans son propre fichier et enregistrez-le sous le nom `.md` indiqué. Les fichiers Markdown sont du texte brut. `workshop-brief.md` indique le public et le style. `approved-schedule.md` contient le programme officiel fictif.

```text
workshop-brief.md, révision 1
Public : personnes inscrites à un atelier d’initiation.
Style : phrases courtes, ton amical et factuel.
N’invente pas de prix, de fonctions d’accessibilité ni de détails sur le stationnement.
```

```text
approved-schedule.md, révision 1
Marqueur de source : WS-2026-11-12-R1
Événement : Introduction à la sécurité numérique
Date : 2026-11-12
Début : 7 p.m.
Lieu : Community Room A
```

## Configurer ChatGPT

1. **Ouvrez « Projects »** dans la barre latérale de ChatGPT et créez un projet nommé `Workshop Practice`.
2. **Ajoutez les deux fichiers** comme sources du projet.
3. **Ouvrez les paramètres du projet** et ajoutez les consignes ci-dessous.
4. **Examinez les réglages de mémoire et de partage** de votre compte et de votre espace de travail avant d’ajouter des données réelles.

```text
Utilise approved-schedule.md pour les faits concernant l’événement.
Utilise workshop-brief.md pour le public et le style.
Si un fait demandé manque, demande la source ou indique qu’il est inconnu.
Rédige uniquement des brouillons. Ne les envoie pas et ne les publie pas.
Liste les changements factuels après chaque brouillon révisé.
```

**Les projets ChatGPT regroupent les conversations, fichiers et consignes liés.** Les paramètres du projet et les fonctionnalités disponibles dépendent de l’offre et de l’espace de travail. Si le processus de création propose une mémoire limitée au projet, choisissez-la pour tester une isolation propre. Avec la mémoire par défaut, une conversation peut s’appuyer sur des informations qui ne figurent pas dans les fichiers téléversés. Le marqueur unique ci-dessous vous aide à tester le fichier sans prendre une réponse issue de la mémoire pour une preuve de lecture. Consultez le [guide officiel des projets ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) pour vérifier les options de mémoire actuelles.

## Configurer Claude

1. **Ouvrez « Projects »** dans Claude et créez un projet avec le même nom d’exercice.
2. **Ajoutez les deux fichiers** aux connaissances du projet.
3. **Définissez les cinq mêmes lignes** comme consignes du projet.
4. **Démarrez une nouvelle conversation dans le projet** pour tester la configuration.

**Ces étapes décrivent les projets Claude classiques.** Anthropic déploie une bêta Projects distincte auprès de certains utilisateurs Pro et Max de Claude Code. Dans cette bêta, un projet correspond à une conversation avec des fils cloud parallèles. Consultez [Qu’est-ce que Projects ?](https://support.claude.com/en/articles/9517075-what-are-projects) et suivez l’interface de votre compte. Les consignes des projets classiques s’appliquent à toutes les conversations, et les connaissances du projet fournissent des références partagées. Utilisez les fichiers téléversés comme faits contrôlés. Le comportement de la mémoire varie selon le compte et les paramètres. Ne considérez donc pas les détails d’une autre conversation comme le programme approuvé. Consultez le [guide de configuration des projets Claude](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) pour connaître les commandes actuelles.

| Mode de projet | Ressources partagées à vérifier | Nouveau test |
|---|---|---|
| **Projet ChatGPT** | Fichiers téléversés, consignes et mode de mémoire choisi | Une nouvelle conversation du projet cite le marqueur du programme |
| **Projet Claude classique** | Connaissances et consignes du projet partagées entre les conversations | Une nouvelle conversation du projet cite le marqueur du programme |
| **Bêta Claude Projects** | Sources et contexte dans le projet et ses fils cloud | Un nouveau fil du projet cite le marqueur du programme |

**Un projet regroupe le contexte, mais ne valide pas une source.** Le marqueur indique si un fichier nommé est arrivé dans la conversation. Comparez tout de même la date, l’heure et la salle au fichier.

## Tester une nouvelle conversation

**Ouvrez une nouvelle conversation de projet ChatGPT ou une nouvelle conversation d’un projet Claude classique.** Dans la bêta Claude Projects, démarrez un nouveau fil du projet. Demandez une courte annonce. N’incluez pas le programme dans votre prompt afin que les sources du projet fournissent les renseignements.

```text
Rédige un courriel de 100 mots pour le prochain atelier.
Indique le fichier source et son marqueur exact pour l’heure et le lieu.
Liste les informations manquantes après le brouillon.
N’envoie pas le message.
```

| Résultat | Signification | Étape suivante |
|---|---|---|
| **L’heure, le lieu et le marqueur correspondent** | Le fichier est accessible à cette conversation | Vérifiez vous-même les faits dans le fichier |
| **Un fait est inventé** | Les consignes ou l’utilisation de la source ont échoué | Supprimez le fait et précisez la demande |
| **La source est absente** | La référence n’est pas arrivée dans cette conversation | Vérifiez l’appartenance au projet et le téléversement du fichier |
| **Une ancienne révision apparaît** | Le projet contient des renseignements périmés | Remplacez la source et recommencez le test |

**Ne déduisez pas la fiabilité d’une seule bonne réponse.** La mémoire par défaut du projet peut fournir une heure familière sans lire le fichier téléversé. Exigez le marqueur exact `WS-2026-11-12-R1`, puis répétez le test avec ce brouillon contradictoire :

```text
Révise cette phrase selon le calendrier approuvé du projet :
« Le cours Introduction à la sécurité numérique commence à 6 p.m. à Community Room A. »
Indique le changement factuel, le fichier source et son marqueur. N’envoie pas le message.
```

**Réponse attendue :** la phrase indique 19 h et nomme `approved-schedule.md` avec le marqueur `WS-2026-11-12-R1`. Notez tout échec observé. Un test réussi n’a pas besoin d’un échec inventé.

**Exemple de compte rendu du test :** nouvelle conversation, première demande, heure : 19 h, lieu : Community Room A, source : `approved-schedule.md`, marqueur : `WS-2026-11-12-R1`, réussi. Prompt contradictoire, correction de 18 h à 19 h, réussi. Il s’agit d’un exemple. Remplacez-le par vos observations.

## Entretenir le projet

**Gardez les consignes du projet courtes.** Placez-y les règles stables. Ajoutez les détails propres à chaque tâche dans son prompt. Remplacez les anciens fichiers et indiquez leurs révisions. Séparez les travaux sans lien dans un autre projet afin d’éviter les conflits entre sources.

**Avant de partager un projet,** examinez ses fichiers, conversations, consignes et liste d’accès. Un projet est un espace de travail, pas un système d’approbation. Même un fichier nommé « approved » exige un vrai responsable et un registre de révision pour les tâches importantes.

## Pratiquer et vérifier

**Votre livrable :** un projet contenant deux fichiers sources synthétiques, cinq lignes de consignes et un bref compte rendu du test. Notez l’heure et le lieu observés, le nom de la source, son marqueur et tout fait inventé. Supprimez le projet d’exercice lorsque vous avez terminé, si vous n’en avez plus besoin.

**Raisonnement attendu :** une nouvelle conversation utilise les sources du projet pour les faits stables, tandis que votre prompt définit le résultat immédiat. Vérifiez la réponse dans le fichier. Si une source manque ou si une mauvaise révision apparaît, revenez à la configuration du projet.

## Vérifier votre compréhension

1. **Question :** une nouvelle conversation d’un projet ChatGPT garantit-elle l’isolation avec tous les réglages de mémoire ? **Réponse :** non. Vérifiez le mode de mémoire du projet et testez-le avec un marqueur de source unique.

2. **Question :** que faire si le projet répète un ancien programme ? **Réponse :** examinez la source jointe et la portée de la mémoire, puis remplacez les ressources périmées.

## Dépannage

- **Commandes du projet introuvables :** vérifiez votre offre actuelle et les paramètres de l’espace de travail dans le guide du fournisseur.
- **Réponses contradictoires :** supprimez les fichiers sources en double ou périmés, puis démarrez une nouvelle conversation.
- **Partage inattendu :** examinez les membres du projet et retirez les sources sensibles avant de continuer.
- **Écarts de style répétés :** raccourcissez les consignes et fournissez un exemple court dans le prompt de la tâche.

## Pour continuer

**Passez à [Contexte de dépôt avec AGENTS.md](/articles/effective-ai-agents-md-context/)**. La leçon suivante passe d’un projet de conversation à un dépôt de code local.

**Navigation du cours :** [Précédent : Fondements du workflow](/articles/effective-ai-workflow-foundations/), [Plan du cours](/effective-ai-course-start/).
