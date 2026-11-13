---
title: "Dossiers de tâches IA : meilleures consignes et critères d’acceptation"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Transformez les demandes vagues adressées à une IA en dossiers de tâches avec un résultat, une source, un périmètre de fichiers, des vérifications et une condition d’arrêt définis."
genre: ["Intelligence artificielle", "Productivité", "Ingénierie logicielle"]
tags: ["rédaction de consignes IA", "dossier de tâche", "consigne pour agent de programmation", "critères d’acceptation", "flux de travail IA", "instructions pour agents IA"]
cover: "/img/cover/effective-ai-task-packets.webp"
coverAlt: "Une demande vague reformulée en un court dossier de tâche avec source, périmètre, vérification et condition d’arrêt"
coverCaption: ""
---

[Retour au cours sur les flux de travail pratiques avec l’IA](/effective-ai-course-start/)

**Une bonne consigne décrit le travail et la façon de l’évaluer.** Ajouter des mots ne compense pas un périmètre manquant. Cette leçon transforme une demande vague en dossier de tâche destiné au laboratoire du cours.

**Objectif d’apprentissage :** vous rédigerez un dossier de tâche délimité avec une source, un périmètre de fichiers, des vérifications et une condition d’arrêt.

## Points essentiels

- **Résultat** désigne l’artefact ou le comportement attendu.
- **Périmètre** désigne les fichiers autorisés et les actions exclues.
- **Source** identifie l’exigence approuvée.
- **Critères d’acceptation** rendent la réussite observable.
- **Conditions d’arrêt** empêchent les suppositions et les tâches suivantes non autorisées.

## Avant de commencer

**Prérequis :** le laboratoire extrait, son fichier `docs/requirements.md` et la [leçon sur le contexte du dépôt](/articles/effective-ai-agents-md-context/). Prévoyez 30 minutes. Le niveau est débutant. Cet exercice se termine par un dossier écrit. Vous n’avez pas encore à modifier le code.

## Comparer deux demandes

**Demande vague :** « Améliore le script de tâches. » Un agent pourrait réécrire les résultats, ajouter des dépendances, modifier les données d’exemple ou omettre les tests. La demande ne précise aucun de ces choix.

**Demande délimitée :** « Ajoute un filtre d’état facultatif à `task_report.py` selon la révision 1 de `docs/requirements.md`. Conserve le résultat par défaut. Ajoute des tests. Ne modifie aucune donnée d’exemple. Arrête-toi avant le commit. » L’agent choisit encore les détails d’implémentation, tandis que la tâche définit la réussite.

| Partie du dossier | Exemple du laboratoire | Vérification |
|---|---|---|
| **Résultat** | Ajouter `--status` au rapport | Les deux valeurs acceptées fonctionnent |
| **Source** | `docs/requirements.md`, révision 1 | Le code respecte les valeurs approuvées |
| **Périmètre** | Programme et tests uniquement | Le diff ne contient aucun autre fichier |
| **Contraintes** | Conserver le résultat par défaut et les données d’exemple | Le résultat de référence reste `Total tasks: 4` |
| **Preuves** | Commande de test et exécutions manuelles | Les résultats correspondent aux nombres attendus |
| **Arrêt** | Ne pas faire de commit ni de push | L’historique Git et le dépôt distant restent intacts |

## Utiliser un modèle réutilisable

**Copiez ce modèle** pour une petite tâche de programmation ou de recherche. Supprimez les champs sans rapport avec la tâche au lieu de les remplir avec des formulations vagues.

```text
Outcome:
Authoritative source and revision:
Relevant files or records:
Allowed changes:
Excluded changes and actions:
Examples of desired behavior:
Completion checks:
Stop or ask when:
Report back with:
```

**Pour le laboratoire,** le dossier rempli ressemble à ceci :

```text
Outcome: Add an optional --status filter to task_report.py.
Source: docs/requirements.md, revision 1.
Relevant files: task_report.py, tasks.json, tests/.
Allowed changes: task_report.py and focused tests.
Excluded: tasks.json, new dependencies, commits, pushes.
Examples: no filter prints Total tasks: 4. Open and done each print 2.
Checks: run unit tests and four manual commands: no filter, open, done, and invalid.
The invalid value must exit nonzero with a clear error.
Stop or ask: source conflict, missing file, unrelated failing baseline.
Report: changed files, commands, observed outputs, unresolved issues.
```

**Sous Windows,** utilisez `py -3` dans toute commande du dossier si votre environnement utilise le lanceur Python.

**Le dossier ne prescrit pas chaque ligne de code.** Il laisse à l’agent le choix d’une petite implémentation, tout en rendant le résultat vérifiable.

## Ajouter des exemples avec soin

**Un exemple exact réduit l’ambiguïté.** Les exemples `open` et `done` précisent le résultat attendu pour le fichier fourni, qui contient quatre tâches. Ils ne définissent pas une règle générale pour tous les fichiers. Pour un autre fichier, les nombres dépendent de ses enregistrements.

**Distinguez l’attendu de l’observé.** Avant d’exécuter le programme, `Total tasks: 2` est le résultat attendu pour chaque état. Après l’exécution, la sortie du terminal devient une observation. Si les valeurs diffèrent, examinez les données et l’implémentation avant d’annoncer la réussite.

## Définir une condition d’arrêt

**Supposons que le fichier des exigences manque.** Le dossier le nomme comme source approuvée. Arrêtez-vous et demandez les exigences au lieu de déduire les valeurs acceptées d’une ancienne conversation ou d’un ticket d’exemple.

**Supposons que les tests de référence échouent avant la modification.** Consignez l’échec et demandez s’il faut d’abord corriger l’état initial. Une exécution réussie ultérieure ne permet pas de distinguer l’effet du filtre de celui de l’état de départ.

**Supposons que l’agent veuille faire un commit.** Le dossier exclut les commits. Demandez-lui de s’arrêter après le diff et les tests. Vous déciderez si un commit ultérieur convient au flux de travail du projet.

## Vérifier le dossier

**Attribuez un point à chaque réponse :** le résultat est-il concret ? La source de référence est-elle nommée ? Le périmètre des fichiers est-il clair ? Au moins deux vérifications observables sont-elles indiquées ? Une condition d’arrêt est-elle présente ? Un score inférieur à cinq signifie que le dossier doit être révisé avant la délégation.

**Votre livrable :** enregistrez votre dossier final et une explication d’une ligne sur une condition d’arrêt. Transmettez-le à un agent de programmation dans la prochaine leçon pratique ou répondez aux résultats attendus sur le parcours d’étude.

## Vérifier votre compréhension

1. **Question :** Qu’est-ce qui rend un dossier de tâche vérifiable ? **Réponse :** Une source, les fichiers autorisés, des vérifications observables et une condition d’arrêt.
2. **Question :** Que doit faire un agent si la source omet un détail nécessaire ? **Réponse :** S’arrêter et signaler le détail manquant au lieu de l’inventer.

## Dépannage

- **L’agent modifie trop de choses :** nommez les fichiers et les actions exclues dans le dossier.
- **L’agent pose trop de questions :** fournissez la source manquante ou un exemple concret.
- **L’agent annonce trop tôt la réussite :** demandez les sorties observées des commandes et inspectez les fichiers.
- **Le dossier devient trop long :** remplacez les extraits copiés de la source par son chemin et sa révision.

## Étapes suivantes

**Poursuivez avec [Votre première tâche avec un agent de programmation](/articles/effective-ai-coding-agent-first-task/)**. Utilisez le dossier pour guider une petite modification du laboratoire.

**Navigation du cours :** [Précédent : Contexte du dépôt](/articles/effective-ai-agents-md-context/), [Plan du cours](/effective-ai-course-start/).
