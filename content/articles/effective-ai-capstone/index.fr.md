---
title: "Projet final de workflow IA : créer et vérifier un rapport JSON"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Créez un rapport JSON avec le contexte du projet, une demande d’agent au périmètre défini, des tests indépendants, une vérification des sources et un transfert vers une nouvelle session."
genre: ["Intelligence artificielle", "Génie logiciel", "Éducation"]
tags: ["projet final de workflow IA", "projet d’agent de programmation", "vérification de tâche IA", "AGENTS.md", "exercice MCP", "transfert d’agent"]
cover: "/img/cover/effective-ai-capstone.webp"
coverAlt: "Tâche logicielle d’atelier terminée avec les fichiers source, les résultats des tests, la vérification de l’agent et le compte rendu de transfert"
coverCaption: ""
---

[Retour au cours sur le workflow IA pratique](/effective-ai-course-start/)

**Créez un nouveau format de sortie et prouvez son comportement.** Vous avez ajouté un filtre d’état plus tôt. Ce projet final démarre dans un nouveau labo et ajoute un rapport JSON qu’un autre programme pourra lire. Cette nouvelle exigence vérifie si vous savez transférer votre workflow vers une autre fonctionnalité.

**Objectif pédagogique :** vous livrerez un rapport JSON vérifié, un relevé des preuves issues des sources et des outils, et un transfert compréhensible par une nouvelle session.

## Points essentiels

- **Une exigence distincte** définit la fonctionnalité du projet final.
- **La modification d’un agent de programmation** reste limitée aux fichiers nommés.
- **Des vérifications indépendantes** déterminent l’acceptation.
- **Un transfert vers une nouvelle session** permet de reconstituer le résultat.

## Avant de commencer

**Prérequis :** terminez les leçons 0 à 10, notamment le contexte du dépôt, la première tâche de programmation, MCP ou son équivalent dans un navigateur, la délégation et les boucles bornées. La leçon 11 est facultative. Prévoyez 90 à 120 minutes. La difficulté est intermédiaire.

**Utilisez une nouvelle extraction** du [labo de démarrage](/downloads/effective-ai-course-lab.zip). Exécutez `python3 task_report.py tasks.json` et les deux tests de référence avant toute modification. Sous Windows, utilisez `py -3` si votre configuration utilise le lanceur Python. Créez une base Git locale comme lors de la configuration du cours. Le filtre d’état de la leçon 5 est volontairement absent.

**Lisez `docs/capstone-requirements.md`, révision 1.** Le fichier exige `--format text|json`. La sortie texte par défaut reste `Total tasks: 4`. La sortie JSON contient un total numérique et un décompte pour chaque état présent dans les données. Vous testerez une liste vide, un état absent et un format non pris en charge. N’utilisez pas `docs/requirements.md` comme référence pour cette nouvelle fonctionnalité.

**Choisissez votre parcours.** Le parcours connecté utilise une modification observée d’un agent de programmation, un véritable appel MCP en lecture seule et un worker natif ou une session worker séparée. Le parcours d’étude utilise un assistant de chat pour proposer le code, une source de navigateur à la place de MCP et des chats distincts comme workers simulés. Indiquez « non exécuté » pour les étapes d’outils indisponibles. Les deux parcours exigent des tests locaux et une revue des fichiers. Le corrigé ci-dessous contient les fichiers complets pour rétablir un essai. Enregistrez votre première tentative dans des notes avant de copier le corrigé dans une nouvelle extraction.

## Point 1 : Consigne du projet

**Ouvrez le projet d’atelier synthétique ChatGPT ou Claude.** Demandez un rappel de deux phrases. Vérifiez son heure de 19 h dans `approved-schedule.md`. Le calendrier définit le rappel. L’exigence du projet final définit le programme.

**Preuve :** notez le nom du projet, la révision de la source, l’heure observée dans le brouillon et toute correction. N’envoyez pas le message.

## Point 2 : Contexte du dépôt

**Ouvrez le nouveau labo.** Créez un `AGENTS.md` concis qui renvoie à `docs/capstone-requirements.md`, `task_report.py`, aux tests et à la commande de test validée pendant la configuration. Avec Claude Code, importez le fichier partagé depuis `CLAUDE.md`. Faites un commit humain de configuration pour ces fichiers d’instructions, puis vérifiez que `git status --short` ne renvoie aucun changement. L’agent de programmation ne doit pas committer la modification fonctionnelle.

**Preuve :** enregistrez la carte du dépôt et l’état propre des instructions. Indiquez les clés JSON et le comportement face aux entrées invalides de la révision 1. Si un ancien chat décrit le filtre d’état, considérez-le comme le contexte d’une autre tâche.

## Point 3 : Ressource externe

**Parcours connecté :** utilisez le [serveur MCP OpenAI Docs en lecture seule](https://learn.chatgpt.com/learn/docs-mcp) avec un client compatible. Demandez à un outil MCP les consignes actuelles pour `AGENTS.md`. Notez le nom de l’outil, l’URL de la source et un point utile pour le labo. Supprimez ensuite la connexion d’exercice.

**Parcours d’étude :** ouvrez la [documentation officielle de `AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md) dans un navigateur. Notez son titre, son URL et un point pertinent. Indiquez « non exécutées » pour la découverte et l’exécution MCP.

**Preuve :** une entrée de serveur configurée ne prouve pas son exécution. Le parcours connecté exige un appel d’outil visible et le contenu de source renvoyé.

## Point 4 : Déléguer une revue

**Demandez à un worker en lecture seule** d’examiner `docs/capstone-requirements.md`, `task_report.py` et les tests de référence. Exigez un rapport de cinq lignes maximum avec les contrôles manquants et les chemins de fichiers. Dans le parcours d’étude, utilisez un chat séparé et indiquez qu’il s’agit d’un worker simulé.

**Résultat attendu :** les tests de départ couvrent le total et une valeur JSON qui n’est pas une liste. Ils ne couvrent ni la sortie JSON, ni une liste vide, ni un état absent, ni un format invalide. Ouvrez vous-même le fichier de test pour vérifier le rapport. Une courte revue indépendante est utile, car les critères d’acceptation diffèrent de ceux de la leçon 5.

**Preuve :** conservez le rapport court et votre décision d’intégration en une phrase. Gardez la transcription du worker hors du journal principal de la tâche.

## Point 5 : Demander la modification

**Transmettez le paquet suivant à un agent de programmation.** Dans le parcours d’étude, un assistant de chat propose un correctif, puis vous l’appliquez manuellement dans le labo.

```text
Objectif : ajouter --format text|json après le chemin JSON.
Source : docs/capstone-requirements.md, révision 1.
Fichiers modifiables : task_report.py et tests/test_task_report.py.
Conserver : Total tasks: 4 par défaut et tasks.json inchangé.
JSON : un objet avec total et les décomptes by_status, aucun texte supplémentaire sur stdout.
Contrôles requis : texte par défaut et explicite, JSON 4/2/2, liste vide,
état absent, format invalide et tests de référence.
Arrêter si : conflit de source, échec de référence sans rapport ou modification hors périmètre.
Rapport : fichiers modifiés, commandes, sorties observées, problème non résolu.
Ne pas committer, pousser, publier ou envoyer de message.
```

**Examinez le plan** avant les modifications. Le choix du schéma compte : `total` est un nombre, pas la chaîne `"4"`. `by_status` contient chaque état présent dans l’entrée, y compris les futurs états. Limitez la modification au labo extrait.

## Point 6 : Tester et vérifier

**Exécutez vous-même ces contrôles.** Sous Windows, remplacez `python3` par `py -3`. L’ordre exact des clés et les espaces dans le JSON n’ont pas d’importance. Analysez la sortie comme du JSON et comparez les types de valeurs.

```bash
git status --short
git diff -- task_report.py tests/test_task_report.py
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --format text
python3 task_report.py tasks.json --format json
python3 task_report.py tasks.json --format invalid
```

**Comportement attendu :** les tests réussissent. Les deux commandes texte affichent `Total tasks: 4`. La commande JSON renvoie un objet unique avec `total` à 4, `by_status.open` à 2 et `by_status.done` à 2. Un format invalide renvoie un code de sortie non nul. Les tests couvrent aussi une liste vide et une tâche sans `status` de type chaîne. Lisez la sortie d’erreur observée et le code de sortie pour ces cas.

| Étape | Preuve de réussite | Rétablissement en cas d’échec |
|---|---|---|
| **Consigne du projet** | Le rappel indique 19 h | Actualiser la source du calendrier |
| **Carte du dépôt** | Exigence et chemins des tests nommés | Corriger les fichiers d’instructions |
| **Ressource externe** | Source MCP lue ou solution navigateur indiquée | Vérifier la connexion ou l’URL |
| **Revue du worker** | Contrôles manquants vérifiés dans le fichier | Corriger le rapport du worker |
| **Périmètre des fichiers** | Programme et tests seulement | Examiner chaque changement indésirable |
| **Comportement** | Texte, JSON, vide et erreurs vérifiés | Diagnostiquer une cause, puis réessayer |
| **Transfert** | Une nouvelle session reconstitue l’état | Ajouter la source ou le résultat manquant |

**Utilisez une nouvelle extraction pour une réinitialisation sûre.** Enregistrez vos notes hors du labo, supprimez uniquement la copie jetable extraite et extrayez à nouveau le ZIP d’origine. N’utilisez pas de réinitialisation Git globale dans un dépôt qui contient du travail à conserver.

## Point 7 : Transfert vers une nouvelle session

**Rédigez un transfert de moins de 180 mots** hors du dossier du labo. Incluez la révision de l’exigence, les fichiers modifiés, la commande de test exacte et son résultat, les sorties texte et JSON, les contrôles des entrées invalides, le journal d’utilisation et la prochaine action. Ouvrez une nouvelle session et demandez-lui de nommer les clés JSON et d’indiquer si la fonctionnalité a réussi.

**Réponse attendue :** la nouvelle session nomme `total` et `by_status`, indique la révision 1, ne rapporte que les contrôles observés et signale tout contrôle manquant.

## Corrigé et barème

**Une implémentation valide** figure ci-dessous. Enregistrez le premier bloc sous `task_report.py` et le second sous `tests/test_task_report.py` dans une nouvelle extraction du labo. Ne modifiez pas `tasks.json` ni les deux fichiers d’exigences. Exécutez les contrôles de l’étape 6. Comparez toute autre solution à l’exigence et au comportement observé.

`task_report.py` :

```python
"""Affiche un total texte ou un récapitulatif JSON des tâches de l’atelier."""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


def load_tasks(path: Path) -> list:
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    for index, task in enumerate(tasks, start=1):
        if not isinstance(task, dict) or not isinstance(task.get("status"), str):
            raise ValueError(f"task {index} needs a string status")
    return tasks


def count_tasks(path: Path) -> int:
    return len(load_tasks(path))


def summarize_tasks(path: Path) -> dict:
    tasks = load_tasks(path)
    counts = Counter()
    for task in tasks:
        counts[task["status"]] += 1
    return {"total": len(tasks), "by_status": dict(sorted(counts.items()))}


def main() -> int:
    parser = argparse.ArgumentParser(description="Rapport des tâches de l’atelier")
    parser.add_argument("path", type=Path, help="chemin vers la liste de tâches JSON")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    try:
        if args.format == "json":
            print(json.dumps(summarize_tasks(args.path)))
        else:
            print(f"Total tasks: {count_tasks(args.path)}")
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py` :

```python
"""Vérifications des rapports texte et JSON des tâches de l’atelier."""

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


def run_report(path: Path, *options: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / "task_report.py"), str(path), *options],
        capture_output=True, text=True, check=False,
    )


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_default_and_explicit_text(self):
        for options in ((), ("--format", "text")):
            result = run_report(ROOT / "tasks.json", *options)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_json_counts_and_types(self):
        result = run_report(ROOT / "tasks.json", "--format", "json")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout), {
            "total": 4, "by_status": {"open": 2, "done": 2},
        })

    def test_empty_list(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "empty.json"
            sample.write_text("[]", encoding="utf-8")
            result = run_report(sample, "--format", "json")
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout), {
                "total": 0, "by_status": {},
            })

    def test_missing_status(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "missing.json"
            sample.write_text('[{"id": 1}]', encoding="utf-8")
            for options in ((), ("--format", "json")):
                result = run_report(sample, *options)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("status", result.stderr)

    def test_invalid_format(self):
        result = run_report(ROOT / "tasks.json", "--format", "invalid")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**Réinitialisez après l’utilisation du corrigé :** enregistrez vos notes hors du labo, supprimez cette copie extraite et extrayez à nouveau le labo de démarrage d’origine. La nouvelle copie contient les deux tests de référence et aucune implémentation de la fonctionnalité.

**Attribuez un point par étape** du tableau ci-dessus. Sept points terminent le parcours connecté si la source externe comprend un véritable appel MCP et si la ligne du worker documente une session réelle. Sept points terminent le parcours d’étude si la source est une page Web vérifiée et si les étapes d’outils indiquent explicitement « non exécuté ». L’absence d’une vérification du comportement, de la source ou du périmètre des fichiers bloque les deux parcours.

## Vérifiez votre compréhension

1. **Quelle exigence définit cette fonctionnalité ?** `docs/capstone-requirements.md`, révision 1. L’ancienne exigence de filtre d’état appartient à la leçon 5.
2. **Qu’est-ce qui prouve le contrat JSON ?** Analysez la sortie de commande, comparez les nombres et le décompte de chaque état, puis testez les entrées vides et invalides. Un résumé bien présenté de l’agent ne suffit pas.

## Dépannage

- **Les tests de référence échouent avant la modification :** réinitialisez le labo depuis le ZIP et recommencez la configuration.
- **L’agent modifie un autre fichier :** examinez le diff et restaurez uniquement la modification indésirable du labo.
- **La connexion MCP échoue :** utilisez la source du navigateur et marquez l’étape comme parcours d’étude.
- **Le worker répète une valeur incorrecte :** relisez l’exigence du projet final et corrigez le rapport.
- **Le budget de nouvelles tentatives est épuisé :** conservez le journal d’échec et demandez la prochaine étape à une personne chargée de la revue.

## Points suivantes

**Enregistrez votre relevé de preuves terminé.** Pour la publication avancée en équipe et l’autorité intersystèmes, poursuivez avec le [cours de mise en œuvre de la collaboration IA](/ai-collaboration-course-start/).

**Navigation du cours :** [Prérequis précédent : boucles bornées](/articles/effective-ai-bounded-agent-loops/), [Facultatif : évaluation des agents spécialisés](/articles/effective-ai-specialized-agent-evaluation/), [Plan du cours](/effective-ai-course-start/).
