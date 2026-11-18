---
title: "Délégation d’agents IA : répartir le travail et vérifier les résultats"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Déterminez quand un second agent IA est utile, attribuez à chaque agent une tâche délimitée, évitez les conflits de modification et intégrez les preuves dans la session principale."
genre: ["Intelligence artificielle", "Génie logiciel"]
tags: ["délégation d’agents IA", "sous-agents", "agents travailleurs", "contexte de l’orchestrateur", "arbres de travail IA", "tâches IA parallèles"]
cover: "/img/cover/effective-ai-agent-delegation.webp"
coverAlt: "Un agent principal répartit des tâches distinctes de recherche et de revue des tests, puis rassemble de courts rapports de preuves"
coverCaption: ""
---

[Retour au cours pratique sur les flux de travail IA](/effective-ai-course-start/)

**Déléguez lorsqu’une question indépendante justifie une session séparée.** Un agent travailleur examine les sources, révise les tests ou prépare une modification limitée dans son propre contexte. L’agent principal vérifie et intègre le résultat. Cette leçon compare des documentations pendant que votre session principale conserve la petite tâche du laboratoire.

**Objectif pédagogique :** vous confierez une revue indépendante à un agent et vérifierez son bref rapport de preuves.

## Points clés

- **Orchestrateur :** l’agent principal qui coordonne la tâche et la revue finale.
- **Travailleur :** un agent séparé chargé d’un résultat délimité.
- **Travail indépendant :** une sous-tâche dont la réponse ne dépend pas du résultat inachevé d’un autre agent.
- **Responsabilité :** un fichier ou une question attribué à un seul agent.
- **Intégration :** comparaison du résultat de l’agent avec les sources actuelles par l’agent principal.

## Avant de commencer

**Prérequis :** vos comptes rendus de [transfert de contexte](/articles/effective-ai-context-window-management/) et de [vérification des résultats](/articles/effective-ai-output-verification/). Prévoyez 40 minutes. Difficulté intermédiaire. La voie connectée nécessite un produit prenant en charge les agents travailleurs. La voie d’étude utilise une conversation distincte et une intégration manuelle.

**Repartez d’un démarrage propre pour cette leçon.** Enregistrez le diff du filtre modifié et le relevé de tests hors du laboratoire. Extrayez le ZIP d’origine dans un nouveau dossier jetable. Exécutez la commande de démarrage et ses deux tests de référence. Reprenez la base Git de la leçon de configuration du cours et recréez les consignes courtes `AGENTS.md` et le fichier facultatif `CLAUDE.md` de la leçon sur le contexte du dépôt. Faites vous-même un commit de ces fichiers, puis vérifiez que `git status --short` est propre. Gardez la copie modifiée du filtre comme référence, mais faites cet exercice avec le démarrage propre.

## Décider de déléguer ou non

**Utilisez un seul agent** pour une petite modification séquentielle. La délégation entraîne des coûts de configuration, de jetons et de revue. Faites appel à un travailleur quand une question indépendante en lecture seule remplirait autrement la conversation principale de nombreux fichiers ou pages de sources.

| Tâche du laboratoire | Déléguer ? | Raison |
|---|---|---|
| **Ajouter un filtre à deux valeurs** | En général non | Un petit fichier et des tests ciblés |
| **Trouver des cas manquants dans deux tests de référence** | En général non | La session principale lira plus vite un fichier court |
| **Comparer les documents actuels de trois produits** | Oui, en lecture seule | La lecture des sources reste dans le contexte du travailleur |
| **Modifier deux fois la même fonction** | Non | Les modifications simultanées créent des conflits |

**Le travailleur doit recevoir moins de contexte que l’orchestrateur,** pas une copie de toute la conversation. Fournissez-lui l’objectif, le chemin source, la limite de la tâche et le format de réponse. Gardez un bref rapport de preuves dans la session principale. Examinez vous-même les fichiers cités avant d’agir.

## Lancer un travailleur en lecture seule

**Gardez la tâche principale réduite.** Dans la session principale, lisez l’`AGENTS.md` local et notez le fichier contenant la commande de test. Confiez la question de recherche distincte ci-dessous à un travailleur. Il n’a pas besoin de tout le laboratoire ni de la conversation précédente.

**Voie connectée :** dans Codex, Claude Code ou un autre client prenant en charge les agents travailleurs, ouvrez le laboratoire comme projet et demandez à l’agent principal de déléguer la demande en lecture seule ci-dessous à un agent. Vérifiez dans la trace des outils qu’un véritable agent a démarré et rendu son rapport. Si le produit n’expose pas d’agent, utilisez une session distincte et identifiez-la comme telle. Les guides actuels des [sous-agents Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents), des [sous-agents Claude Code](https://code.claude.com/docs/en/sub-agents) et des [agents OpenCode](https://opencode.ai/docs/agents/) décrivent les contrôles actuels.

**Voie d’étude :** ouvrez une nouvelle conversation pour la même demande. Donnez-lui les trois liens officiels ou des extraits des sources. Étiquetez-la comme un agent simulé. Une deuxième conversation constitue un contexte séparé, pas une preuve d’exécution d’un sous-agent natif.

```text
Utilisez les documents officiels actuels Codex AGENTS.md, Claude Code memory et OpenCode rules.
Comparez la façon dont chaque produit charge les fichiers d’instructions du dépôt.
Ne modifiez aucun fichier.
Renvoyez au plus trois lignes : produit, fichier d’instructions, URL source et un comportement de chargement.
Signalez toute incertitude. Ne collez pas les pages complètes.
```

**Sources :** [consignes de projet Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [mémoire Claude Code](https://code.claude.com/docs/en/memory) et [règles OpenCode](https://opencode.ai/docs/rules/). Le rapport attendu cite `AGENTS.md` pour Codex et OpenCode. Les versions actuelles de Claude Code chargent aussi directement `AGENTS.md` lorsqu’aucun fichier `CLAUDE.md` ou `CLAUDE.local.md` ne prend le dessus. Ce laboratoire utilise un fichier `CLAUDE.md` qui importe `@AGENTS.md`, ce qui prend également en charge les sessions plus anciennes ou configurées autrement. Vérifiez les pages actuelles et la version active avant de présenter cet exemple comme un résultat observé d’un agent.

## Intégrer les résultats

**Ouvrez vous-même les pages citées.** Si l’agent affirme que Claude Code exige toujours l’importation de `CLAUDE.md`, consultez son guide mémoire et corrigez le rapport. Comparez-le à vos fichiers d’instructions locaux. Rédigez une courte note d’intégration :

```text
Accepté : Codex et OpenCode utilisent AGENTS.md pour les consignes du projet.
Les versions actuelles de Claude Code peuvent charger AGENTS.md directement. Ce laboratoire
utilise CLAUDE.md avec un import @AGENTS.md pour conserver une carte commune stable.
Preuves : consignez les trois URL officielles actuelles et la date de revue.
Décision : conserver une carte commune courte et un import pour Claude.
```

**Cette note est le résultat utile du travailleur.** L’orchestrateur a besoin de conclusions vérifiées et des chemins des sources, pas de la transcription de recherche. La délégation consomme davantage de jetons au total ; gardez la conversation principale plus courte uniquement si la session séparée économise de l’attention.

## Attribuer la responsabilité des modifications

**Si les travailleurs modifient des fichiers,** répartissez les fichiers attribués ou utilisez des arbres de travail séparés pour les tâches qui se chevauchent dans un dépôt. Un arbre de travail est une autre copie du même dépôt Git, avec ses propres fichiers de travail. Il permet d’isoler des modifications simultanées. L’agent principal vérifie puis transfère les changements avec un merge, un cherry-pick ou un patch explicite, avant de relancer les tests dans l’arbre intégré.

| Travailleur | Travail attribué | Résultat attendu |
|---|---|---|
| **Implémentation** | `task_report.py` | Diff et commande de test |
| **Auteur des tests** | `tests/test_task_report.py` | Cas de test et résultat observé |
| **Orchestrateur** | Exigences et intégration finale | Diff combiné et critères d’acceptation |

**Le petit laboratoire n’a pas besoin de modifications parallèles.** Ce tableau enseigne une méthode de répartition pour les tâches plus importantes. Les tests d’un arbre de travail ne valident pas une implémentation encore isolée dans un autre. Si deux travailleurs ont besoin de la même fonction, travaillez en série ou demandez à l’un de réviser sans modifier. Les arbres séparés évitent les collisions de fichiers, mais ne résolvent pas les exigences contradictoires.

## Vérifier le comportement du produit

**Les sous-agents varient selon l’hôte.** Codex, Claude Code et OpenCode gèrent différemment l’héritage du contexte, les permissions des outils et la remise des résultats. Consultez les guides des [sous-agents Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents), des [sous-agents Claude Code](https://code.claude.com/docs/en/sub-agents) et des [agents OpenCode](https://opencode.ai/docs/agents/) pour le produit installé. Ne supposez pas qu’un travailleur partage tout le contexte principal ou dispose d’un arbre de travail isolé.

## S’exercer et vérifier

**Votre livrable :** un bref rapport d’agent sur la documentation et une note d’intégration. Dans la voie d’étude, utilisez une nouvelle conversation et identifiez-la comme un agent simulé. Ne prétendez pas qu’un sous-agent natif a été exécuté dans cette voie.

**Contrôle de fin :** le rapport cite trois sources officielles, reste dans le périmètre de la question et respecte la longueur demandée. La note d’intégration vérifie les sources et nomme les fichiers d’instructions utilisés dans votre laboratoire.

## Vérifier votre compréhension

1. **Question :** Quand un travailleur aide-t-il davantage qu’un agent unique ? **Réponse :** Lorsqu’il possède une question ou un livrable indépendant et remet un rapport de preuves utile.

2. **Question :** Que faire après que deux travailleurs ont modifié des fichiers qui se chevauchent ? **Réponse :** Intégrer les changements, examiner le diff combiné et relancer les vérifications.

## Dépannage

- **Le travailleur renvoie une longue transcription :** demandez un tableau de preuves plus court avec des références de fichiers.
- **Les travailleurs ne sont pas d’accord :** relisez le fichier faisant autorité avant de choisir une réponse.
- **Deux modifications se chevauchent :** arrêtez l’une et attribuez la responsabilité des fichiers ou séparez les arbres de travail.
- **Les droits d’outils du travailleur diffèrent :** examinez ses permissions au lieu de supposer qu’elles correspondent à celles du parent.

## Étapes suivantes

**Continuez avec les [boucles d’objectifs délimitées](/articles/effective-ai-bounded-agent-loops/).** Pour la gouvernance d’équipe au-delà de ce petit laboratoire, consultez le [cours de mise en œuvre de la collaboration IA](/ai-collaboration-course-start/).

**Navigation du cours :** [Précédent : vérification de sortie](/articles/effective-ai-output-verification/), [Plan du cours](/effective-ai-course-start/).
