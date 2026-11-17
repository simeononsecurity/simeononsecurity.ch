---
title: "Comment vérifier les résultats, les sources, les tests et les coûts de l’IA"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Constituez un dossier d’acceptation pour un résultat d’IA en vérifiant les sources, le périmètre des fichiers, les preuves de test, la confidentialité et l’utilisation."
genre: ["Intelligence artificielle", "Génie logiciel"]
tags: ["vérifier les résultats d’IA", "vérification des faits par l’IA", "revue d’agent de programmation", "preuves de test IA", "suivi des coûts IA", "revue humaine"]
cover: "/img/cover/effective-ai-output-verification.webp"
coverAlt: "Une fiche de revue comparant une affirmation de l’IA à un fichier source, un diff de code, une sortie de test et un total d’utilisation"
coverCaption: ""
---

[Retour au cours Pratique des flux de travail avec l’IA](/effective-ai-course-start/)

**N’acceptez un résultat d’IA qu’après avoir vérifié les preuves adaptées à la tâche.** Une explication soignée, un outil configuré et une bannière de tests réussis répondent à des questions différentes. Cette leçon crée un seul dossier de revue pour le laboratoire de l’atelier.

**Objectif d’apprentissage :** vous produirez un dossier d’acceptation couvrant les sources, le périmètre des fichiers, les tests, la confidentialité et l’utilisation.

## Points clés

- **Vérification des sources :** comparez une affirmation factuelle à une source faisant autorité et à jour.
- **Vérification du périmètre :** inspectez les fichiers ou systèmes modifiés.
- **Vérification du comportement :** exécutez les tests et les cas manuels pertinents.
- **Vérification de la confidentialité :** inspectez les données transmises à l’outil ou au fournisseur.
- **Vérification de l’utilisation :** consignez les jetons, les appels d’outils et le tarif utilisé pour calculer le coût.

## Avant de commencer

**Prérequis :** le laboratoire du cours, `docs/requirements.md`, un instantané Git local et la [leçon MCP](/articles/effective-ai-mcp-server-setup/) ou son équivalent dans le navigateur. Prévoyez 40 minutes. La difficulté est intermédiaire. Utilisez le laboratoire modifié lors de la première tâche avec un agent de programmation. Si vous avez sauté la modification, utilisez une nouvelle extraction et indiquez que les contrôles de fonctionnalité ne sont pas implémentés. La base intacte réussit toujours ses deux tests d’origine.

## Vérifier une affirmation factuelle

**Affirmation :** « Les valeurs d’état approuvées sont `open` et `pending`. » Ouvrez `docs/requirements.md`, révision 1. Le document indique `open` et `done`. L’affirmation est fausse. Un ton assuré ne change pas l’exigence.

**Pour les affirmations sur un produit,** utilisez sa documentation officielle actuelle et notez le titre de la page et la date de vérification. Une affirmation sur un menu, un forfait, une commande ou une limite de contexte devient obsolète plus vite qu’un principe général de flux de travail. La [documentation Codex](https://learn.chatgpt.com/docs/codex/cli), la [documentation Claude Code](https://code.claude.com/docs/en/overview) et la [documentation OpenCode](https://opencode.ai/docs/) décrivent leurs interfaces actuelles.

| Affirmation | Source | Décision |
|---|---|---|
| **`open` et `pending`** | Exigence du laboratoire, révision 1 | Rejeter, remplacer `pending` par `done` |
| **Le total sans filtre est 4** | Programme de base et quatre entrées JSON | Vérifier en exécutant le programme |
| **Une lecture MCP a eu lieu** | Transcription des outils de la session | Accepter uniquement si un appel d’outil est visible |

## Inspecter la modification

**Pour une tâche de programmation,** utilisez Git pour lister les fichiers modifiés et lire le diff réel. Un nouveau fichier non suivi apparaît dans l’état même s’il n’apparaît pas dans un diff ordinaire. Inspectez les deux.

```bash
git status --short
git diff -- task_report.py tests
```

**Périmètre attendu :** après la tâche de filtrage, seuls `task_report.py` et les tests ciblés changent. Toute modification de `tasks.json`, `docs/requirements.md` ou d’un fichier de configuration caché exige une explication et une revue distincte. Si vous n’avez pas effectué de modification, attendez-vous à ne voir aucun changement.

## Tester le comportement

**Exécutez les mêmes contrôles de base et de fonctionnalité** dans le dossier extrait du laboratoire. Le rapport de fin de l’agent doit donner les résultats observés de ces contrôles.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**Dans la copie modifiée,** les tests couvrent les nouveaux cas, les totaux sont 4, 2 et 2, et la valeur invalide provoque une erreur claire avec une sortie non nulle. Dans une nouvelle copie de départ, seuls les deux tests de base réussissent et le total vaut 4. Consignez séparément cet état de départ.

**L’échec d’un test de fonctionnalité doit être diagnostiqué.** Si `open` affiche 4, vérifiez que l’argument de filtrage parvient à la fonction de comptage et que le programme compare le champ `status` de la tâche. Ne présentez pas un test en échec comme réussi au motif que l’agent dit avoir terminé l’implémentation.

## Vérifier la confidentialité et l’accès

**Consignez les fichiers reçus par l’agent.** Le laboratoire contient des données synthétiques et aucun secret. Un vrai projet peut inclure des identifiants, des données client ou des documents privés. Avant de partager une sortie, inspectez les prompts, les journaux, les captures et les diffs à la recherche de ces valeurs.

**Un test local ne prouve que le comportement local.** Il ne prouve ni les autorisations d’un compte cloud, ni le périmètre d’un serveur MCP, ni le comportement d’un service déployé. Testez chaque limite dans l’environnement concerné.

## Consigner l’utilisation et les coûts

**Les jetons mesurent le volume d’entrée et de sortie du modèle.** Les tableaux de bord varient selon le produit, utilisez donc les chiffres d’utilisation affichés par votre fournisseur. Consignez séparément les appels d’outils et les frais d’image ou d’environnement hébergé, le cas échéant. Consultez les tarifs actuels avant de calculer une facture réelle.

**Ouvrez la vue d’utilisation du compte qui a exécuté la tâche.** Notez les jetons d’entrée et de sortie affichés, le modèle, la période de facturation et toute catégorie d’entrée mise en cache. Pour ChatGPT ou Claude, une limite ou une allocation d’abonnement n’équivaut pas au coût API d’une tâche. Pour une exécution OpenCode via API ou fournisseur, consultez l’utilisation ou la facturation de ce fournisseur et son tarif actuel. Si le produit n’affiche pas les jetons par tâche, écrivez « non disponible » et ne déduisez pas de coût de la longueur de la conversation.

**Calcul illustratif, sans rapport avec les tarifs d’un fournisseur :** 30 000 jetons d’entrée à 1 $ par million coûtent 0,03 $. 5 000 jetons de sortie à 5 $ par million coûtent 0,025 $. Dans cet exemple, le coût combiné du modèle est 0,055 $, hors frais d’outil ou d’hébergement.

```text
coût d’entrée = jetons d’entrée / 1 000 000 × tarif d’entrée
coût de sortie = jetons de sortie / 1 000 000 × tarif de sortie
total = coût d’entrée + coût de sortie + frais d’outils distincts
```

**Une tâche confiée à un agent consomme aussi des jetons.** La délégation déplace les détails hors de la conversation principale, mais le travail n’est pas gratuit. Comparez le coût à la valeur de la vérification indépendante.

**Gardez les catégories de frais séparées.** Les entrées mises en cache, les nouvelles entrées, les sorties, les appels d’outils et l’exécution hébergée peuvent avoir des tarifs différents. Cet exemple n’utilise que les tarifs des nouvelles entrées et des sorties. Il ne dit rien sur un abonnement ni des frais d’outil.

## Tenir un dossier d’acceptation

| Champ | Exemple rempli après la modification |
|---|---|
| **Source** | `docs/requirements.md`, révision 1, lu |
| **Fichiers modifiés** | `task_report.py` et `tests/test_task_report.py` dans `git status --short` |
| **Tests** | Tests de base et nouveaux tests de filtrage réussis, consignez le nombre observé |
| **Sortie manuelle** | `Total tasks: 4`, `2` et `2` observés, valeur invalide rejetée |
| **État de la fonctionnalité** | `--status open` et `--status done` implémentés |
| **Confidentialité** | Fichiers synthétiques uniquement |
| **Utilisation** | Consignez les chiffres de votre fournisseur, s’ils sont disponibles |
| **Décision** | Acceptez uniquement si les contrôles de source, diff, tests et confidentialité réussissent |

**Votre livrable :** copiez ce dossier et remplissez-le après votre propre exécution. Remplacez « observé » uniquement par une sortie que vous avez vue. Choisissez Accepter si tous les contrôles requis réussissent, Réviser si une correction reste limitée, et Arrêter si la source, le périmètre ou l’accès n’est pas clair.

## Vérifier votre compréhension

1. **Question :** la réussite de la base de départ prouve-t-elle que la fonctionnalité demandée existe ? **Réponse :** Non. Testez le nouveau comportement d’acceptation après la modification.

2. **Question :** que doit contenir un dossier d’acceptation ? **Réponse :** les preuves des sources, les fichiers modifiés, les contrôles de comportement, le périmètre d’accès et l’utilisation observée.

## Dépannage

- **Aucune source pour une affirmation :** indiquez qu’elle n’est pas vérifiée et trouvez une source faisant autorité.
- **Les tests réussissent mais la sortie diffère :** ajoutez un cas manuel et inspectez les données.
- **Utilisation absente :** notez « non disponible » au lieu d’estimer un coût réel.
- **Le diff contient des données privées :** cessez de partager la sortie et supprimez ces données du dossier d’exercice.

## Étapes suivantes

**Continuez avec [Délégation d’agents](/articles/effective-ai-agent-delegation/)**. Pour les détails sur les coûts et la confidentialité, consultez le [routage des fournisseurs](/articles/openrouter-provider-routing-quality-cost/) et la [limite de confidentialité de l’IA locale](/articles/local-ai-privacy-boundary/).

**Navigation du cours :** [Précédent : Configuration MCP](/articles/effective-ai-mcp-server-setup/), [Plan du cours](/effective-ai-course-start/).
