---
title: "Configuration du cours de flux de travail IA : terminal, Git et laboratoire pratique"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Préparez un espace sûr pour pratiquer avec l’IA, apprenez les termes du terminal et de Git utilisés dans le cours, puis lancez le laboratoire de démarrage."
genre: ["Intelligence artificielle", "Génie logiciel", "Éducation"]
tags: ["configuration du cours IA", "bases du terminal", "bases de Git", "prérequis des agents de programmation", "laboratoire de pratique IA", "cours IA pour débutants"]
cover: "/img/cover/effective-ai-course-setup.webp"
coverAlt: "Un espace de pratique pour débutants avec des symboles de terminal, Python et Git, un dossier de laboratoire coché et une archive de réinitialisation"
coverCaption: ""
---

[Retour au cours pratique sur les flux de travail IA](/effective-ai-course-start/)

**Préparez un espace de pratique sûr avant d’utiliser un agent.** Les leçons 1 et 2 fonctionnent dans un navigateur sans ce laboratoire. Revenez ici avant la leçon 3 si vous voulez suivre le cours complet. Les leçons pratiques de programmation utilisent Git, Python 3.10 ou une version ultérieure et un agent de programmation. Le parcours d’étude remplace les actions d’agent indisponibles par des tâches manuelles signalées.

**Objectif d’apprentissage :** vous exécuterez le laboratoire de démarrage, enregistrerez une base locale et expliquerez comment réinitialiser une copie jetable.

## Points clés

- **Parcours navigateur :** faites les exercices de discussion, de planification, de vérification des sources et de révision dans ChatGPT ou Claude.
- **Parcours local :** utilisez un terminal et le laboratoire Python fourni pour les exercices de programmation.
- **Parcours de réinitialisation :** extrayez une nouvelle copie du laboratoire si un exercice se passe mal.
- **Règle de sécurité :** gardez les fichiers privés, les dossiers clients et les identifiants en dehors du laboratoire.

## Choisissez votre parcours

| Parcours | Prérequis | Exercices |
|---|---|---|
| **Introduction dans le navigateur** | Navigateur récent et compte ChatGPT ou Claude | Leçons 1 et 2, ainsi que le dossier de tâches de discussion de la leçon 1 |
| **Pratique locale** | Git, Python 3.10 ou version ultérieure, terminal, un agent de programmation | Fichiers, différences, tests et modifications par l’agent |
| **Cours d’étude** | Navigateur, Python 3.10 ou version ultérieure en local et Git | Vérifications complètes du laboratoire; les étapes d’agent et MCP indisponibles sont marquées comme non exécutées |

**Chaque produit définit ses propres offres et limites.** Consultez [ChatGPT Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) et [Claude Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) avant de compter sur une fonctionnalité. Le parcours d’étude ne prouve pas votre maîtrise pratique d’un agent de programmation indisponible. Notez cette distinction dans votre bilan de cours.

**Suivez un parcours par défaut :** utilisez ChatGPT dans un navigateur pour les exercices de discussion, puis un agent de programmation disponible avec le laboratoire local. Claude offre un parcours équivalent pour la discussion. Codex CLI, Claude Code CLI et OpenCode restent des choix pour l’étape de programmation. Vous n’avez pas besoin de créer des comptes chez tous les fournisseurs.

**Consignez cinq vérifications avant d’ouvrir un agent de programmation.** Cette liste distingue une vérification du laboratoire local d’une affirmation sur un compte ou un espace de travail hébergé.

| Vérification | À consigner |
|---|---|
| **Espace de travail** | Dossier exact du laboratoire extrait que l’agent lira |
| **Exécution** | Ordinateur local ou espace distant sélectionné |
| **Fournisseur** | Compte ou fournisseur du modèle utilisé pour cette tâche |
| **Autorisations** | Écritures de fichiers et commandes shell permises ou soumises à approbation |
| **Base** | Nombre observé et deux tests réussis avant les modifications |

**Gardez la racine de pratique limitée.** Un espace hébergé a besoin de sa propre copie du laboratoire synthétique. Une exécution locale ne prouve pas que la copie distante ou le compte possède les mêmes fichiers et autorisations.

## Apprenez les termes locaux

| Terme | Sens simple |
|---|---|
| **Terminal** | Application où vous saisissez des commandes |
| **Shell** | Logiciel qui interprète ces commandes |
| **CLI** | Interface en ligne de commande d’un programme |
| **Répertoire de travail** | Dossier utilisé par défaut par une commande |
| **Dépôt** | Projet suivi par Git |
| **Commit** | Instantané Git enregistré |
| **Branche** | Ligne nommée de modifications Git |
| **Différence** | Affichage des lignes ajoutées ou supprimées |
| **Vérification** | Vérification répétable du comportement attendu |
| **Code de sortie** | Nombre signalant la réussite ou l’échec d’une commande |

**GitHub n’est pas nécessaire pour le laboratoire de démarrage.** Git fonctionne sur votre ordinateur. GitHub est un service d’hébergement distinct. Un commit local enregistre un instantané sans envoyer vos fichiers.

## Préparez le laboratoire

**Téléchargez le [laboratoire de démarrage du cours](/downloads/effective-ai-course-lab.zip)** et extrayez-le dans un nouveau dossier que vous contrôlez. Ouvrez un terminal dans ce dossier. Sous macOS ou Linux, ouvrez Terminal et utilisez `cd` pour entrer dans le dossier extrait. Sous Windows, utilisez PowerShell ou Windows Terminal et `cd`. Sous Windows, la commande Python est souvent `py -3` plutôt que `python3`.

**Installez [Python 3.10 ou version ultérieure](https://www.python.org/downloads/) et [Git](https://git-scm.com/downloads) si nécessaire.** Vérifiez les outils installés avant de lancer le laboratoire. Les deux premières commandes affichent les versions. `cd` change le répertoire de travail. `ls` liste les fichiers. Remplacez le chemin d’exemple par celui de votre dossier extrait.

```bash
python3 --version
git --version
cd /path/to/effective-ai-course-lab
ls
```

**Dans Windows PowerShell,** utilisez `py -3 --version`, `git --version`, `cd C:\path\to\effective-ai-course-lab` et `Get-ChildItem`. La liste doit comprendre `task_report.py`, `tasks.json`, `tests` et `docs`. Si une commande de version échoue, terminez l’installation avant de continuer.

```bash
pwd
python3 task_report.py tasks.json
python3 -m unittest discover -s tests -v
```

**Dans Windows PowerShell,** remplacez `pwd` par `Get-Location` si vous préférez, et `python3` par `py -3` si Python utilise le lanceur. La première commande affiche le chemin, qui doit se terminer par le dossier du laboratoire extrait. Vérifiez aussi les noms de fichiers. Un fichier nommé `AGENTS.md.txt` ne remplace pas `AGENTS.md`. Dans l’Explorateur Windows, activez les extensions de noms de fichiers pour voir le nom complet.

**Résultat attendu :** le rapport indique `Total tasks: 4`. La commande de test nomme deux tests et se termine par `OK`. Un shell renvoie le code zéro après une réussite. Un autre nombre ou une trace d’erreur signifie qu’il faut vérifier le dossier et l’installation de Python.

**Lisez une commande morceau par morceau.** Dans `python3 task_report.py tasks.json`, `python3` lance Python, `task_report.py` est le programme et `tasks.json` désigne les données d’entrée. Le nombre affiché est une sortie, pas une commande. Après un échec, macOS et Linux affichent l’état avec `echo $?`. PowerShell expose le dernier état d’un programme natif par `$LASTEXITCODE`.

**Prévoyez environ dix minutes pour le premier lancement** après l’installation de Python : extrayez le laboratoire, exécutez le rapport et comparez son total aux quatre entrées de `tasks.json`. Ouvrez le fichier JSON dans un éditeur de texte et comptez vous-même les entrées.

## Pratiquez Git sans risque

**Initialisez Git uniquement dans le dossier du laboratoire extrait.** Ces commandes enregistrent un instantané local. `git status` indique les fichiers modifiés. `git diff` affiche les lignes changées après la modification d’un fichier suivi.

```bash
git init
git add .
git commit -m "État initial du laboratoire du cours"
git status --short
```

**État attendu :** aucun nom de fichier n’apparaît après le commit. Si Git demande un nom et une adresse e-mail, configurez une identité réservée au laboratoire depuis ce dossier, puis relancez le commit. Remplacez les valeurs d’exemple par des valeurs privées. Ne collez pas de sortie d’identité ou d’identifiants dans un chat public.

```bash
git config --local user.name "Élève du cours"
git config --local user.email "learner@example.invalid"
git commit -m "État initial du laboratoire du cours"
git status --short
```

**Aucune commande Git n’est nécessaire pour réinitialiser le laboratoire.** Enregistrez vos notes hors du laboratoire, supprimez la copie extraite et extrayez de nouveau le ZIP d’origine. Utilisez cette méthode si une modification laisse le programme dans un état inconnu.

## Protégez votre espace de pratique

**Utilisez des exemples synthétiques.** Ne téléversez pas de documents privés dans un projet de cours. Ne mettez pas de clés API dans des prompts, fichiers source, captures d’écran ou commits. L’accès d’un agent aux fichiers et commandes dépend de ses autorisations et du dossier ouvert. Vérifiez ces deux éléments avant de le laisser agir.

**Vérifiez le partage avant tout téléversement.** Les fichiers du projet peuvent être accessibles aux membres. Pour le travail réel, suivez les règles de votre organisation. Le cours utilise des données fictives; le laboratoire ne demande donc pas d’autorisation particulière.

## Entraînez-vous et vérifiez

**Votre livrable :** consignez le parcours choisi, les cinq champs du contrôle préalable, le nombre indiqué par le rapport, le résultat des tests et la méthode de réinitialisation. Utilisez une nouvelle copie du laboratoire pour confirmer que vous savez le réinitialiser.

**Raisonnement attendu :** vous savez quel dossier les commandes affectent, distinguez Git local de l’hébergement et disposez d’une méthode de récupération avant qu’un agent ne modifie des fichiers.

## Vérifiez vos connaissances

1. **Question :** Une introduction uniquement dans un navigateur termine-t-elle le parcours du laboratoire local ? **Réponse :** Non. Le parcours complet exige une base locale Python et Git.

2. **Question :** Que faut-il enregistrer avant de modifier le laboratoire jetable ? **Réponse :** Le résultat réussi des tests de départ et un point de réinitialisation propre.

## Dépannage

- **Commande Python introuvable :** installez Python 3 depuis son distributeur officiel, puis rouvrez le terminal.
- **Fichier introuvable :** vérifiez le répertoire de travail et listez les fichiers du dossier extrait.
- **Tests impossibles à lancer :** utilisez exactement la commande du README du laboratoire extrait.
- **Git demande une identité pour le commit :** configurez Git localement et gardez les valeurs choisies hors des notes de cours.

## Étapes suivantes

**Continuez avec [le flux de travail IA fiable](/articles/effective-ai-workflow-foundations/)**. Le premier exercice utilise le même atelier synthétique avant que tout outil reçoive des fichiers réels.

**Navigation du cours :** [Plan du cours](/effective-ai-course-start/).
