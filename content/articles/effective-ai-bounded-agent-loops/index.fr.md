---
title: "Boucles d’agents IA bornées : contrôles, nouvelles tentatives et règles d’arrêt"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Définissez une boucle d’objectif d’IA avec un état observable, des contrôles, des limites de nouvelles tentatives, des conditions d’arrêt et un transfert clair à une personne."
genre: ["Intelligence artificielle", "Ingénierie logicielle", "Productivité"]
tags: ["boucles d’objectif d’IA", "boucle de nouvelle tentative d’agent", "règles d’arrêt de l’automatisation IA", "surveillance des agents", "transfert humain pour l’IA", "flux de travail IA borné"]
cover: "/img/cover/effective-ai-bounded-agent-loops.webp"
coverAlt: "Une petite boucle d’agent passe d’une modification à un test, à une décision de nouvelle tentative puis à un transfert humain"
coverCaption: ""
---

[Retour au cours pratique sur les flux de travail avec l’IA](/effective-ai-course-start/)

**Une boucle d’objectif répète le travail jusqu’à ce qu’un résultat défini réussisse un contrôle ou qu’une règle d’arrêt se déclenche.** Une boucle utile lit l’état actuel, effectue une action limitée, vérifie le résultat et consigne ce qui s’est passé. Une consigne ouverte comme « continuez d’essayer » ne définit aucune règle d’achèvement fiable.

**Objectif d’apprentissage :** vous exécuterez une boucle de laboratoire bornée avec un contrôle connu pour échouer et consignerez la décision d’arrêt.

## Points clés

- **Objectif :** un résultat décrit en termes observables.
- **État :** les fichiers, résultats, erreurs et révision du code source actuels.
- **Contrôle :** un test ou une revue lié à l’objectif.
- **Budget de nouvelles tentatives :** le nombre maximal d’essais autorisés pour un échec.
- **Règle d’arrêt :** une condition qui impose de terminer ou de demander une décision humaine.

## Avant de commencer

**Prérequis :** le [dossier de tâche](/articles/effective-ai-task-packets/), le [rapport de vérification](/articles/effective-ai-output-verification/) et la [leçon sur la délégation](/articles/effective-ai-agent-delegation/). Prévoyez 45 minutes. La difficulté est intermédiaire. Utilisez une nouvelle copie du laboratoire synthétique afin de connaître à l’avance le premier contrôle qui échouera.

## Rédiger le contrat de boucle

**Pour la demande de filtre par statut**, définissez le contrat avant toute nouvelle tentative :

```text
Objectif : prendre en charge --status open|done sans modifier la sortie par défaut.
Source : docs/requirements.md, révision 1.
Fichiers autorisés : task_report.py et tests ciblés.
Vérifications : tests unitaires, comptes 4/2/2, valeur invalide avec un code de sortie non nul.
Budget de nouvelles tentatives : deux modifications au maximum après le premier essai.
Arrêt immédiat : conflit avec la source, modification inattendue d’un fichier, exposition d’un secret,
ou échec initial sans rapport avec cette demande.
Transmission : signaler le diff final, les commandes, les résultats, les essais et le problème non résolu.
```

**Le budget est une règle de la tâche**, pas une valeur par défaut du produit. Deux nouvelles tentatives suffisent pour diagnostiquer une petite tâche de laboratoire sans masquer des échecs répétés. Une tâche de production exige son propre choix en matière de risque et de revue.

## Utiliser un tableau d’état

| Étape | État à consigner | Décision |
|---|---|---|
| **Lire** | Révision du code source et résultat initial | Arrêter si l’état de départ diffère |
| **Agir** | Fichiers modifiés et action effectuée | Rejeter les changements hors périmètre |
| **Contrôler** | Test exact et résultat manuel | Accepter ou diagnostiquer |
| **Réessayer** | Cause de l’échec et nouvelle hypothèse | Continuer uniquement dans la limite du budget |
| **Transférer** | État final et prochain responsable | Arrêter après réussite ou blocage |

**Consignez chaque tentative, pas seulement le dernier message.** Un test qui réussit après trois modifications non consignées n’explique pas les changements. Tenez un journal bref de l’échec, de l’hypothèse révisée et des nouveaux éléments de preuve.

## Examiner un échec

**Exemple de première tentative :** l’agent ajoute le filtrage et les tests. `open` affiche 2, mais `--status invalid` affiche 0 et se termine normalement. L’exigence demande un code de sortie non nul pour une valeur invalide. Marquez le contrôle comme échoué.

**Diagnostic :** inspectez la validation des arguments. L’agent a traité une valeur inconnue comme un résultat vide au lieu de la signaler comme erreur. Demandez une correction limitée qui valide les valeurs acceptées avant le comptage. Relancez le cas invalide et tous les contrôles précédents.

```text
Essai 1 : le statut invalide a réussi, donc l’acceptation a échoué.
Cause trouvée : aucune validation des valeurs acceptées.
Demande pour l’essai 2 : rejeter les valeurs non prises en charge et conserver les comptes 4/2/2.
Preuves requises : exécution complète des tests et code de sortie de la commande invalide.
```

**Résultat attendu à la deuxième tentative :** une erreur claire et un code de sortie non nul pour `invalid`, sans changement des comptes valides. Si la deuxième tentative échoue encore, ne faites la dernière tentative qu’après avoir identifié une nouvelle cause. Répéter la même demande ne constitue pas un diagnostic.

## Gérer les résultats ambigus

**Un processus qui s’arrête sans résultat n’a pas réussi.** Si un outil expire après une éventuelle écriture, inspectez les fichiers et l’état de Git avant de le relancer. Si un service connecté signale un résultat inconnu, lisez son état actuel avant de répéter une action externe. Hors du laboratoire, les envois, publications ou écritures en double présentent un risque réel.

**Arrêtez-vous pour demander une revue humaine** si l’exigence contredit une autre source approuvée, si une autorisation bloque l’action, si le budget de nouvelles tentatives est épuisé ou si l’action demandée dépasse une limite de publication. Le transfert indique l’état exact et la décision en attente.

## Distinguer les boucles des moniteurs

**Une boucle de modification** s’exécute dans le cadre d’une tâche limitée et vérifie le résultat après chaque action. **Un moniteur planifié** se réveille plus tard pour examiner une condition. Un moniteur a besoin de sa propre fréquence, d’un seuil de changement, d’une règle de notification et d’une condition d’arrêt. Ne transformez pas la boucle de modification du laboratoire en tâche récurrente. La leçon suivante évalue les systèmes persistants avant leur activation.

## Exécuter une boucle contrôlée

**Commencez avec le laboratoire intact.** Ses deux tests de base réussissent. Dans la nouvelle extraction, créez `tests/test_loop_contract.py` avec le contrôle ci-dessous. Ce fichier exprime une fonctionnalité souhaitée qui manque dans le projet de départ. Il ne fait pas partie de l’archive ZIP de départ maintenue.

```python
"""One controlled failing check for the status-filter exercise."""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class LoopContractTests(unittest.TestCase):
    def test_open_status_count(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"),
             str(ROOT / "tasks.json"), "--status", "open"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "Total tasks: 2")


if __name__ == "__main__":
    unittest.main()
```

**Exécutez `python3 -m unittest discover -s tests -v`.** Les deux tests d’origine devraient réussir et le nouveau test contractuel devrait échouer, car le projet de départ ne gère pas `--status`. Consignez l’échec réel. Si vous avez initialisé Git comme indiqué dans la leçon 0, consignez aussi `git status --short`. Sinon, comparez les fichiers modifiés à une extraction intacte. Sous Windows, utilisez `py -3` si votre configuration passe par le lanceur.

**Fixez un budget de trois tentatives :** la première modification et deux corrections au maximum. Donnez le contrat de boucle ci-dessus à votre agent et demandez une seule modification limitée. Après chaque tentative, inspectez les fichiers modifiés, relancez tous les tests et exécutez les commandes par défaut, `open`, `done` et valeur invalide. Consignez la cause de l’échec avant toute autre tentative. Arrêtez-vous après une réussite, un échec de référence sans rapport avec la demande, un changement hors périmètre ou le troisième échec.

**Parcours d’étude :** après avoir consigné le test rouge, appliquez la [solution complète de la leçon 5](/articles/effective-ai-coding-agent-first-task/) dans cette nouvelle copie. Relancez les mêmes contrôles et indiquez que la modification par l’agent n’a pas été exécutée. Conservez le test contractuel contrôlé. Ne l’affaiblissez pas et ne le supprimez pas pour le faire réussir.

| Tentative | État et observation | Décision |
|---|---|---|
| **Avant la modification** | Les deux tests de base réussissent et le nouveau contrôle `open` échoue | Continuer avec une modification limitée |
| **Après chaque modification** | Consigner les tests exacts, les comptes, le code de sortie invalide et les fichiers modifiés | Accepter, diagnostiquer ou arrêter |
| **À la fin du budget** | Consigner l’échec restant et le diff actuel | Transférer sans nouvelle tentative |

## S’entraîner et vérifier

**Votre livrable :** le test contrôlé qui échoue, les résultats observés avant et après, un journal des tentatives et une décision finale d’acceptation ou d’arrêt. Si la première modification réussit, consignez une tentative. N’inventez pas un deuxième échec pour remplir le journal.

**Contrôle de fin :** le contrat nomme une source, un périmètre de fichiers, des contrôles observables, une limite de nouvelles tentatives, au moins une condition d’arrêt immédiat et un transfert. Votre journal contient le véritable test rouge, les résultats des contrôles ultérieurs et soit une réussite, soit un arrêt dû au budget. Une deuxième tentative nomme une nouvelle cause et diffère de la première.

## Vérifier votre compréhension

1. **Question :** que prouve le premier test contractuel rouge ? **Réponse :** le projet de départ n’a pas le filtre de statut demandé, comme le montre un test écrit avant la modification.
2. **Question :** quand la boucle doit-elle s’arrêter même s’il reste des tentatives ? **Réponse :** en cas de changement hors périmètre, d’autorisation incertaine ou d’exigence contradictoire.

## Dépannage

- **La boucle répète le même échec :** arrêtez-vous et formulez une nouvelle hypothèse sur la cause.
- **Les contrôles s’affaiblissent :** rétablissez les critères d’acceptation d’origine.
- **Résultat externe incertain :** inspectez l’état actuel avant une nouvelle tentative.
- **Budget épuisé :** transférez le journal d’échec au lieu de le masquer.

## Étapes suivantes

Poursuivez avec l’optionnelle [Évaluation des agents spécialisés](/articles/effective-ai-specialized-agent-evaluation/) ou passez directement au [projet final du cours sur les flux de travail avec l’IA](/articles/effective-ai-capstone/). Pour comparer les environnements d’exécution, consultez le [guide des environnements d’agents](/articles/best-ai-agent-harnesses/).

**Navigation du cours :** [Précédent : délégation d’agents](/articles/effective-ai-agent-delegation/), [Plan du cours](/effective-ai-course-start/).
