---
title: "Gestion de la fenêtre de contexte IA : garder les agents de programmation concentrés"
description: "Maîtrisez le contexte actif d’une tâche d’IA avec des fichiers choisis, des transmissions concises et de petites réponses des travailleurs, tout en conservant décisions et preuves."
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
genre: ["Intelligence artificielle", "Génie logiciel"]
tags: ["gestion du contexte IA", "contexte d’agent de programmation", "transmission IA", "compaction du contexte", "orchestration d’agents", "budget de tokens"]
cover: "/img/cover/effective-ai-context-window-management.webp"
coverAlt: "Une note de transmission concise près de fichiers de projet sélectionnés et d’une transcription de chat beaucoup plus longue, écartée"
coverCaption: ""
---

[Retour au cours pratique de flux de travail avec l’IA](/effective-ai-course-start/)

**La fenêtre de contexte contient le texte et les autres éléments qu’un modèle traite pendant le tour en cours.** Les instructions, définitions d’outils, extraits de fichiers, sorties d’outils et historique de conversation occupent de l’espace. Cette leçon montre comment garder la prochaine tâche ciblée et transmettre un état fiable.

**Objectif d’apprentissage :** préparer une transmission concise et la tester dans une nouvelle session.

## Points essentiels

- **Tokens :** unités utilisées par un modèle pour traiter ses entrées et ses sorties.
- **Contexte actif :** éléments disponibles pendant un tour, dans les limites du produit.
- **Sources durables :** fichiers ou dossiers de projet conservés hors du chat.
- **Compaction :** résume ou supprime une partie de l’ancien contexte et peut omettre un détail nécessaire.
- **Transmission :** indique à une nouvelle session les sources actuelles et le travail vérifié.

## Avant de commencer

**Prérequis :** le laboratoire modifié de la [première tâche avec un agent de programmation](/articles/effective-ai-coding-agent-first-task/), son exigence approuvée et la [leçon sur les paquets de tâches](/articles/effective-ai-task-packets/). Si vous avez suivi le parcours d’étude, utilisez votre laboratoire modifié manuellement. Prévoyez 35 minutes. Le niveau est intermédiaire. Gardez les notes de cours hors du dossier du laboratoire extrait afin que `git status` ne montre que les changements de code.

## Choisir le contexte selon la tâche

**Pour modifier le filtre d’état,** l’agent a besoin de `task_report.py`, `docs/requirements.md`, des tests pertinents et d’un petit échantillon de `tasks.json`. Il n’a pas besoin de tous les anciens chats, de toute la documentation du site ni de l’historique Git complet. Consultez d’abord une carte, puis chargez seulement les fichiers nécessaires à la prochaine décision.

| Tâche | Contexte utile | Contexte superflu |
|---|---|---|
| **Définir le comportement** | Exigence approuvée et échantillon de données | Anciennes conversations exploratoires |
| **Modifier le programme** | Programme et tests ciblés | Répertoires de projets sans rapport |
| **Examiner le résultat** | Différence, sortie des tests, exigence | Transcription complète de l’agent |
| **Reprendre plus tard** | Note de transmission et chemins des sources | Chat de plusieurs heures collé en entier |

**C’est un choix de récupération, pas une consigne pour cacher les preuves.** En cas d’échec d’un test, incluez sa sortie exacte et le fichier concerné. Retirez les journaux sans rapport, pas les détails utiles au diagnostic.

**Comptez la charge fixe avant d’ajouter des travailleurs.** Les instructions de l’agent et les schémas d’outils disponibles peuvent occuper du contexte avant la lecture d’un fichier de tâche. Un deuxième travailleur répète une partie de cette charge et ajoute un rapport à examiner par l’agent principal. Pour modifier deux fichiers, utilisez un agent. Pour rechercher indépendamment dans de nombreuses sources, un rapport bref peut réduire le contexte de la session principale, même si le coût total en tokens augmente.

## Préparer une transmission concise

**Une transmission est un court compte rendu destiné à la session suivante.** Elle distingue le travail terminé du travail proposé. Enregistrez cet exemple sous `course-notes/handoff.md`, hors du laboratoire, puis remplacez les observations fictives par les vôtres.

```text
Objectif : ajouter --status open|done au rapport des tâches du cours.
Source : docs/requirements.md, révision 1.
Espace de travail : dossier effective-ai-course-lab extrait.
État actuel : le filtre d’état figure dans task_report.py et dans les tests.
Vérifié : note le résultat observé des tests et les décomptes manuels 4, 2 et 2.
Décision : tasks.json est resté inchangé.
En attente : examen indépendant du diff et de la source.
Prochaine vérification : relance les tests et le cas d’état invalide.
Arrête si : l’exigence ou la valeur de référence diffère de ce relevé.
```

**Cet exemple ne décrit pas votre travail réel.** Notez les résultats observés des tests et les fichiers modifiés. Si la révision de la source change, actualisez la transmission après avoir relu cette source.

## Tester une nouvelle session

**Ouvrez un nouveau chat ou une nouvelle session d’agent de programmation** dans le laboratoire. Dans un chat, collez la transmission et le fichier `AGENTS.md` du laboratoire synthétique, puis nommez les fichiers à examiner. Dans un agent de programmation, ouvrez le dossier du laboratoire et collez la transmission en autorisant la lecture des fichiers indiqués. Demandez :

```text
À partir de cette passation et des fichiers actuels du dépôt, indique les valeurs d’état approuvées, le décompte de référence et la prochaine vérification. Ne modifie rien.
Si la passation contredit une source actuelle, signale le conflit.
```

**Raisonnement attendu :** la nouvelle session trouve `open` et `done` dans `docs/requirements.md`, relève le compte initial de 4 et nomme les tests et vérifications manuelles. Si elle répète l’ancienne valeur `pending`, relisez l’exigence et corrigez la transmission.

## Garder l’orchestrateur léger

**L’orchestrateur est l’agent principal qui coordonne les travailleurs.** Donnez à chacun une question précise et des fichiers d’entrée nommés. Demandez une réponse courte : constat, chemin de preuve, niveau de confiance et point non résolu. Gardez les journaux détaillés dans un fichier ou dans la session du travailleur. Ne transmettez à l’agent principal que ce dont il a besoin pour décider de la suite.

**Exemple :** demandez à un travailleur en lecture seule d’examiner les tests et de répondre « cas manquant, fichier et ligne, vérification suggérée ». Ne lui demandez pas de coller tous les tests dans le chat principal. L’agent principal vérifie ensuite le constat dans le dépôt avant de modifier quoi que ce soit. La [leçon sur la délégation](/articles/effective-ai-agent-delegation/) ajoute une tâche indépendante quand son périmètre justifie le coût.

**Dans de nombreux produits, les sessions des travailleurs ont leur propre contexte,** mais l’héritage et l’isolation varient. Consultez les règles actuelles du produit avant de supposer qu’un travailleur voit les mêmes instructions, fichiers ou outils que l’agent principal. Les guides de [sous-agents Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents) et de [sous-agents Claude Code](https://code.claude.com/docs/en/sub-agents) décrivent le fonctionnement de chaque produit.

## Utiliser la compaction avec prudence

**La compaction raccourcit l’historique actif.** Codex, Claude Code et OpenCode diffèrent dans le moment et la méthode de compaction. Traitez un résumé compacté comme une aide à la reprise, pas comme le dossier complet du projet. Conservez exigences et décisions dans des fichiers, puis vérifiez-les après la compaction. Consultez les recommandations actuelles sur les [bonnes pratiques Codex](https://learn.chatgpt.com/docs/learn/best-practices), les [commandes Claude Code](https://code.claude.com/docs/en/commands) et la [compaction OpenCode 2](https://opencode.ai/v2/docs/compaction). OpenCode 1 et OpenCode 2 utilisent des schémas différents. Vérifiez `opencode --version` avant de copier des réglages.

**Si l’assistant oublie une contrainte,** arrêtez la modification, rouvrez la source et reformulez le paquet de tâches. Une nouvelle session avec une transmission brève et vérifiée demande souvent moins d’attention que la correction répétée d’un long chat confus.

## S’exercer et vérifier

**Votre livrable :** une transmission de moins de 180 mots, enregistrée hors du laboratoire. Marquez chaque ligne comme source, résultat observé, décision ou action en attente. Fournissez-la à une nouvelle session et notez si elle nomme les deux valeurs d’état acceptées et la prochaine vérification.

**Vérification finale :** la nouvelle session nomme `open`, `done`, le compte initial de 4 et une étape de test sans s’appuyer sur l’ancien chat. Corrigez les omissions, puis recommencez avec une autre nouvelle session.

## Vérifier sa compréhension

1. **Question :** que faut-il inclure dans une transmission destinée à une nouvelle session ? **Réponse :** l’objectif, la source faisant autorité, l’état actuel, le résultat vérifié et l’action suivante.

2. **Question :** pourquoi garder le rapport d’un travailleur court ? **Réponse :** un rapport concis avec des preuves fournit à l’orchestrateur le résultat utile sans reprendre toute la transcription.

## Dépannage

- **Le résumé omet une décision :** ajoutez une ligne brève avec la décision et la révision de sa source.
- **La réponse du travailleur est énorme :** demandez un tableau de preuves limité et des références de fichiers.
- **La transmission est obsolète :** relisez les sources actuelles avant la prochaine modification.
- **Le contexte reste trop chargé :** divisez la tâche en sessions plus petites avec des livrables distincts.

## Étapes suivantes

**Poursuivez avec [Configurer un serveur MCP](/articles/effective-ai-mcp-server-setup/)**. Vous ajouterez un outil externe en lecture seule et limiterez sa sortie.

**Navigation du cours :** [Précédent : première tâche de programmation](/articles/effective-ai-coding-agent-first-task/), [Plan du cours](/effective-ai-course-start/).
