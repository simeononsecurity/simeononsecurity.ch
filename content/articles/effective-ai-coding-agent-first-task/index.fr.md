---
title: "Réalisez votre première tâche de dépôt avec un agent de programmation"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Choisissez une interface d’agent de programmation, ouvrez un dépôt d’exemple, examinez une modification proposée et lancez les vérifications avant de la conserver."
genre: ["Intelligence artificielle", "Génie logiciel"]
tags: ["tutoriel Codex CLI", "application Codex", "Claude Code CLI", "tutoriel OpenCode", "flux de travail d’agent de programmation", "outils de programmation IA"]
cover: "/img/cover/effective-ai-coding-agent-first-task.webp"
coverAlt: "Un dépôt de code avec des vues distinctes de l’agent dans le terminal et sur le bureau, à côté d’un fichier diff révisé"
coverCaption: ""
---

[Retour au cours sur le flux de travail pratique avec l’IA](/effective-ai-course-start/)

**Un agent de programmation lit les fichiers, propose des modifications et exécute des outils dans un espace de travail.** Cette leçon vous guide dans une petite tâche sur un dépôt. Choisissez Codex dans l’application de bureau ChatGPT ou en CLI, Claude Code CLI ou OpenCode TUI. Examinez ensuite une modification avant de l’accepter.

**Objectif d’apprentissage :** vous exécuterez ou appliquerez manuellement une modification limitée, puis vérifierez son diff et son comportement.

## Points essentiels

- **Codex dans l’application de bureau ChatGPT** fournit un espace visuel pour les tâches et leur révision.
- **Codex CLI** lance une session Codex depuis votre terminal.
- **Claude Code CLI** lance le flux de programmation de Claude dans votre terminal.
- **OpenCode TUI** propose un flux de programmation en terminal avec des fournisseurs et des permissions configurables.
- **Un diff et le résultat d’un test** comptent davantage que le message d’achèvement de l’assistant.

## Avant de commencer

**Prérequis :** terminez la [configuration du cours](/articles/effective-ai-course-setup/), y compris le test de référence et l’instantané Git local. Terminez [le contexte du dépôt](/articles/effective-ai-agents-md-context/) et [les paquets de tâches](/articles/effective-ai-task-packets/) avant cette leçon. Utilisez un agent de programmation auquel vous êtes autorisé à accéder. Prévoyez 45 minutes. Le niveau va de débutant à intermédiaire.

**Utilisez le [laboratoire de départ du cours](/downloads/effective-ai-course-lab.zip)** dans un dossier jetable. L’archive contient un petit programme de rapport de tâches, des données d’exemple et des tests. N’utilisez pas un dépôt de production pour votre première modification. Votre tâche consiste à ajouter un filtre `--status` tout en conservant le décompte total actuel.

## Parcours sans agent de programmation

**Demandez à un assistant conversationnel de proposer la même modification** si aucun agent de programmation n’est disponible. Collez uniquement `docs/requirements.md`, `task_report.py` et le fichier de test ciblé du laboratoire synthétique. Demandez un diff unifié et une brève explication. Un diff unifié marque les anciennes lignes avec `-` et les nouvelles avec `+`. Ouvrez le fichier indiqué dans un éditeur de texte, remplacez les anciennes lignes par la proposition et enregistrez le fichier. Exécutez ensuite toutes les commandes de la section Examiner le résultat. Ne modifiez pas `tasks.json`. Notez que l’étape avec l’agent de programmation n’a pas été exécutée. Le projet final comprend une fonction JSON distincte. Comparez donc votre solution de filtre avec l’exigence et les vérifications de la leçon 5.

## Choisir une interface

**Choisissez d’abord une surface de révision.** Codex dans l’application de bureau ChatGPT convient à un projet visuel et à l’examen de diffs. Une interface en terminal convient au travail dans le dossier du laboratoire extrait. Comparez les options de terminal entre elles :

| Outil de terminal | Vérification du compte ou du fournisseur | Commande de démarrage |
|---|---|---|
| **Codex CLI** | Confirmez votre connexion à Codex et les permissions locales | `codex` |
| **Claude Code CLI** | Confirmez votre accès à Claude Code et les permissions locales | `claude` |
| **OpenCode TUI** | Configurez un fournisseur de modèles pris en charge et ses permissions | `opencode` |

**Installez l’outil et connectez-vous à l’aide de son guide officiel actuel.** Consultez [Codex CLI](https://learn.chatgpt.com/docs/codex/cli), [l’application de bureau ChatGPT](https://learn.chatgpt.com/docs/app), [Claude Code](https://code.claude.com/docs/en/overview) ou [OpenCode](https://opencode.ai/docs/). Les commandes, les plateformes prises en charge et les conditions de compte changent. Cette leçon utilise uniquement les noms de lancement stables et une méthode de révision commune.

**Pour choisir plus précisément un produit,** consultez la [comparaison des agents de programmation en CLI](/articles/cli-coding-agents-comparison/) ou la [comparaison des agents de programmation avec interface graphique](/articles/gui-coding-agents-comparison/) du site. Les guides [Codex CLI et bureau](/articles/codex-cli-vs-desktop/), [Claude Code CLI et bureau](/articles/claude-code-cli-vs-desktop/) et [OpenCode CLI et bureau](/articles/opencode-cli-vs-desktop/) comparent les interfaces de chaque produit.

**Commencez dans le dossier du laboratoire.** Chaque interface exige de choisir explicitement un espace de travail :

1. **Codex pour ordinateur :** ouvrez l’application de bureau ChatGPT, choisissez le laboratoire extrait comme projet local, puis démarrez une tâche locale dans ce projet. Vérifiez le chemin du dossier et les demandes d’autorisation avant toute modification. Une tâche hébergée utilise une copie distincte de l’espace de travail.
2. **Codex CLI :** exécutez `cd /path/to/effective-ai-course-lab`, puis `codex`. Confirmez le dossier de travail affiché et le mode d’autorisation.
3. **Claude Code CLI :** exécutez la même commande `cd`, puis `claude`. Confirmez le dossier du projet et les permissions des outils.
4. **OpenCode TUI :** exécutez la même commande `cd`, puis `opencode`. Confirmez le fournisseur choisi, le projet et les permissions configurées.

**ChatGPT et Claude Projects gèrent les conversations et les fichiers de référence partagés.** Codex et Claude Code travaillent dans un espace de code avec des outils de fichiers et de commandes. OpenCode propose aussi des interfaces de bureau et d’IDE, mais cette leçon utilise son interface de terminal. Le fournisseur, le compte et l’exécution locale ou hébergée varient. Notez donc la surface choisie au lieu de considérer toutes les sessions comme le même environnement.

**Vérifiez cinq points avant d’ouvrir le laboratoire :** le système d’exploitation pris en charge, l’authentification, le coût du fournisseur ou du compte, les permissions sur les fichiers et commandes, ainsi que l’exécution locale ou sur un hôte distant. Notez votre choix. Ne supposez pas qu’une application de bureau et un outil de terminal utilisent le même espace de travail.

## Examiner le projet de départ

**Rouvrez le dossier propre du laboratoire** de la leçon sur le contexte du dépôt. Cette copie contient votre `AGENTS.md` commité et le fichier de consignes facultatif `CLAUDE.md`. Examinez les fichiers avant de demander une modification à un agent. Exécutez les tests de référence depuis ce dossier.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
```

**Résultat de référence attendu :** le rapport affiche `Total tasks: 4`. L’exécution des tests nomme deux tests et se termine par `OK`. Si l’un des deux échoue, arrêtez-vous et examinez les fichiers extraits. N’attribuez pas à l’agent la réparation d’un point de départ défectueux.

**Utilisez les instantanés Git locaux** de la configuration du cours et de la leçon sur le contexte du dépôt. `AGENTS.md` et le fichier facultatif `CLAUDE.md` doivent déjà être commités. Exécutez `git status --short` avant la modification de la fonction et attendez-vous à ne voir aucun fichier. L’agent ne doit pas non plus créer de commit. L’archive ne contient aucun historique Git. Son fichier `.gitignore` exclut le bytecode Python généré par les tests. Si vous avez extrait une nouvelle copie, répétez la configuration du cours et la leçon sur le contexte du dépôt dans ce dossier. Commitez les fichiers de consignes avant la modification de la fonction. Initialisez et commitez d’abord le projet de départ :

```bash
git init
git add .
git commit -m "Base du laboratoire du cours"
```

**Ajoutez ensuite `AGENTS.md` et le fichier facultatif `CLAUDE.md`** avec la source approuvée et la commande de test de la leçon sur le contexte du dépôt. Commitez ces fichiers, vérifiez que `git status --short` est propre, puis commencez la modification de la fonction. Exécutez ces commandes dans votre dossier de laboratoire extrait, pas à la racine d’un autre dépôt.

## Formuler une demande limitée

**Ouvrez le dossier du laboratoire** dans l’agent de programmation choisi. Envoyez ce paquet de tâches :

```text
Ajoutez un argument facultatif --status à task_report.py.
Valeurs autorisées : open et done.
Sans cet argument, conservez la sortie actuelle du total sans changement.
Avec cet argument, comptez uniquement les tâches correspondantes et affichez Total tasks: N.
Ajoutez des tests pour les deux valeurs, une valeur invalide et la sortie par défaut inchangée.
Ne modifiez pas tasks.json ni les fichiers sans rapport avec la tâche.
Exécutez les tests et indiquez la commande exacte et le résultat.
Arrêtez après le code et les tests. Ne créez pas de commit et ne faites pas de push.
```

**Sous Windows,** remplacez `python3` par la commande `py -3` vérifiée pendant la configuration, y compris dans les consignes de dépôt enregistrées et le paquet de tâches.

**Demandez un plan bref avant la modification** si vous ne connaissez pas le code. Autorisez l’agent à modifier uniquement le dossier jetable du laboratoire. Les contrôles de permissions varient selon l’outil : examinez ses paramètres actuels avant d’autoriser les commandes shell ou l’écriture de fichiers.

## Examiner le résultat

**Lisez le diff.** Vérifiez que la sortie sans filtre reste identique, que le filtre accepte seulement deux valeurs et que les tests couvrent l’erreur et la sortie par défaut inchangée. Des tests réussis valident la modification uniquement si les tests vérifient le comportement demandé.

```bash
git status --short
git diff -- task_report.py tests
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**Résultats attendus :** les trois premières commandes de rapport affichent 4, 2 et 2. La valeur incorrecte affiche une erreur claire et le processus se termine avec un code différent de zéro. La formulation exacte de l’erreur dépend de l’implémentation. Sous macOS ou Linux, exécutez `echo $?` immédiatement après la commande incorrecte pour lire le code de sortie. Dans PowerShell, examinez `$LASTEXITCODE`.

| Élément à vérifier | Point de contrôle |
|---|---|
| **Liste des fichiers** | Seuls le programme et les tests changent |
| **Diff** | La logique du filtre correspond à la demande |
| **Sortie des tests** | Les nouveaux cas ont été exécutés et réussissent |
| **Exécution manuelle** | Les décomptes par défaut, `open` et `done` correspondent à `tasks.json` |

**Si l’agent annonce un résultat sans avoir exécuté les tests,** lancez la commande vous-même. Si la modification dépasse le paquet de tâches, demandez une correction limitée. Si l’état reste incertain, supprimez la copie extraite du laboratoire et extrayez de nouveau le ZIP d’origine.

## Réponses du parcours d’étude

**Utilisez ces fichiers complets si votre correctif manuel échoue.** Recommencez avec un laboratoire fraîchement extrait, enregistrez le premier bloc sous `task_report.py` et le second sous `tests/test_task_report.py`, puis lancez les commandes de la section Examiner le résultat. Ne modifiez pas `tasks.json` ni `docs/requirements.md`. Notez l’échec initial avant de copier les fichiers.

`task_report.py` :

```python
"""Affiche le nombre de tâches d’un fichier JSON."""

import argparse
import json
import sys
from pathlib import Path


def count_tasks(path: Path, status: str | None = None) -> int:
    """Compte toutes les tâches ou celles avec un statut autorisé."""
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    if status not in (None, "open", "done"):
        raise ValueError("status must be open or done")
    if status is None:
        return len(tasks)
    return sum(1 for task in tasks if task["status"] == status)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compter les tâches de l’atelier")
    parser.add_argument("path", type=Path, help="chemin vers la liste JSON des tâches")
    parser.add_argument("--status", choices=("open", "done"))
    args = parser.parse_args()
    try:
        total = count_tasks(args.path, args.status)
    except (OSError, ValueError, KeyError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Total tasks: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py` :

```python
"""Tests du rapport de tâches de l’atelier."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from sys import path as module_path

ROOT = Path(__file__).resolve().parents[1]
module_path.insert(0, str(ROOT))
from task_report import count_tasks  # noqa: E402


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_counts_each_approved_status(self):
        sample = ROOT / "tasks.json"
        self.assertEqual(count_tasks(sample, "open"), 2)
        self.assertEqual(count_tasks(sample, "done"), 2)

    def test_rejects_invalid_status_in_function(self):
        with self.assertRaises(ValueError):
            count_tasks(ROOT / "tasks.json", "pending")

    def test_default_command_stays_unchanged(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"), str(ROOT / "tasks.json")],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_invalid_command_exits_nonzero(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"), str(ROOT / "tasks.json"),
             "--status", "invalid"],
            capture_output=True, text=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**Conservez une copie modifiée dont les tests du filtre réussissent** pendant les leçons sur le contexte et la vérification des résultats. Si vous avez utilisé ce corrigé pour récupérer votre travail, gardez la nouvelle copie avec ses tests réussis pour ces leçons. Conservez le diff et le relevé des tests hors du laboratoire. Rétablissez le projet de départ avant la leçon sur la délégation, ou supprimez une tentative échouée pour recommencer proprement.

## S’exercer et vérifier

**Votre livrable :** un diff du laboratoire et un relevé de révision de quatre lignes portant sur les fichiers modifiés, le comportement par défaut, le comportement filtré et la saisie incorrecte. Notez le nom et la version de l’outil dans vos notes privées afin de reproduire un problème propre à une version.

**Raisonnement attendu :** vous avez choisi une interface adaptée à votre façon de travailler, délimité la tâche, examiné la modification réelle et exécuté une vérification indépendamment du compte rendu de l’agent.

## Vérifier votre compréhension

1. **Question :** Qu’est-ce qui prouve que le filtre d’état fonctionne ? **Réponse :** Un diff limité, des tests réussis et des résultats observés pour le comportement par défaut, open, done et la valeur incorrecte.
2. **Question :** Le message de l’agent affirmant avoir exécuté les tests constitue-t-il votre résultat de test ? **Réponse :** Non. Exécutez la commande ou examinez sa sortie.

## Dépannage

- **Commande introuvable :** terminez l’installation à l’aide du guide du fournisseur, puis rouvrez le terminal.
- **Accès aux fichiers refusé :** ouvrez le dossier du laboratoire extrait, puis vérifiez les permissions de l’espace de travail.
- **Fichiers inattendus modifiés :** arrêtez-vous et examinez `git status --short` avant d’envoyer une autre demande.
- **Tests réussis, comportement incorrect :** ajoutez un cas manuel ou un test couvrant l’exigence manquante.

## Étapes suivantes

**Continuez avec [Fenêtres de contexte et transferts](/articles/effective-ai-context-window-management/)**. Vous conserverez une note utile pour une nouvelle session.

**Navigation du cours :** [Précédent : Paquets de tâches](/articles/effective-ai-task-packets/), [Plan du cours](/effective-ai-course-start/).
