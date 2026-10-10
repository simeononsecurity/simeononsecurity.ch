---
title: "GitHub Copilot CLI contre VS Code : comparaison des flux de travail en 2026"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Comparez l’agent de terminal Copilot avec son expérience dans VS Code, notamment le contexte de l’éditeur, les différences visuelles, le mode Agent, l’intégration CLI et les règles du compte."
genre: ["Outils pour développeurs", "Intelligence artificielle", "Développement logiciel"]
tags: ["GitHub Copilot CLI contre VS Code", "Copilot CLI", "GitHub Copilot", "VS Code", "mode Agent", "CLI contre GUI", "contexte de l’éditeur", "suggestions intégrées", "différence visuelle", "sessions Copilot", "agent de terminal", "flux GitHub", "revue de code", "intégration IDE", "outils MCP", "autorisations de l’agent", "AI Credits", "outils de développement", "assistant de programmation", "automatisation"]
cover: "/img/cover/github-copilot-cli-vs-vscode.webp"
coverAlt: "Invite de terminal reliée à une sélection de l’éditeur et à une différence visuelle dans un espace de programmation bleu et vert"
coverCaption: ""
---

**GitHub Copilot CLI et Copilot dans VS Code proposent des points d’entrée différents pour programmer.** Le CLI commence avec le shell et une invite de tâche. VS Code réunit contexte de l’éditeur, suggestions, chat et flux d’agent. Évaluez les deux avec les mêmes règles de compte et de dépôt.

**Le choix n’est pas exclusif.** GitHub documente une connexion entre Copilot CLI et VS Code. Une tâche menée dans le terminal profite de la sélection de l’éditeur et de la revue visuelle lorsque vous reliez explicitement les deux.

## Points clés

- **Utilisez Copilot CLI pour les tâches pilotées par le terminal** et les appels programmatiques pris en charge.
- **Utilisez Copilot dans VS Code pour le travail centré sur l’éditeur**, avec l’assistance intégrée et le mode Agent.
- **Reliez le CLI à VS Code** lorsque les invites du terminal doivent recevoir le contexte et les diffs de l’éditeur.
- **Vérifiez les réglages du compte, du modèle et des règles**, même dans une seule famille de produits.

**Périmètre et date :** La documentation officielle a été vérifiée le 10 octobre 2026. Cette comparaison porte sur le CLI autonome `copilot` et Copilot dans VS Code, pas sur l’ancienne extension `gh copilot` ni sur un agent cloud associé à une issue GitHub. Il faut un dépôt testable et un accès Copilot autorisé. Prévoyez une heure pour l’essai.

## Trois façons de travailler

| Flux | Interaction principale | Tâche d’essai adaptée |
|---|---|---|
| **CLI autonome** | Invite du terminal et sortie de commande | Expliquer et corriger un échec de test reproduit |
| **Intégration VS Code** | Sélection de l’éditeur, chat, suggestions et diffs | Modifier une fonction sélectionnée et ses tests |
| **CLI relié à VS Code** | Tâche du terminal avec contexte et revue de l’éditeur | Enquêter depuis le shell et examiner le patch visuellement |

**Le mode hybride reste une session CLI.** L’exécuter dans un terminal intégré ne le transforme pas automatiquement en conversation native du mode Agent de l’éditeur. Vérifiez la session et la connexion actives au lieu de vous fier à la fenêtre qui contient l’invite.

## Ce que fournit le CLI

```bash
copilot
```

**La commande autonome actuelle démarre l’agent de terminal.** La [présentation de Copilot CLI](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-cli) de GitHub décrit l’usage interactif et programmatique, ainsi que la planification et les autorisations d’outils. Évaluez-le lorsque la sortie du terminal constitue la preuve principale.

**Une bonne première tâche possède un échec concret.** Donnez la commande en échec, le comportement attendu et une restriction contre les refactorisations sans rapport. Demandez la reproduction avant de modifier des fichiers. Vérifiez que l’explication finale correspond à la sortie observée.

**L’automatisation exige des limites explicites.** Utilisez les [guides d’utilisation du CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli) pour l’appel et les options actuelles. Définissez les outils autorisés, les délais et la gestion de sortie avant les tâches sans surveillance. Ne transformez pas une politique interactive d’autorisation en permission générale pour un pipeline.

**Le sandboxing change le périmètre de l’essai.** GitHub documente le sandbox local pour les restrictions du système de fichiers, du réseau et du système, ainsi que des sandboxes cloud. Une invite de répertoire approuvé et un indicateur d’autorisation ne remplacent pas ces limites. Testez le sandbox, le réseau et l’écriture avec une fixture inoffensive avant un changement réel.

## Ce qu’ajoute VS Code

**L’expérience Copilot dans l’IDE comprend suggestions, chat et tâches d’agent.** La [présentation de l’IDE](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-in-ides) sépare ces fonctions. L’assistance intégrée convient lorsque vous restez l’éditeur principal. Le mode Agent convient à un résultat limité touchant plusieurs fichiers.

**Le mode Agent modifie les fichiers et exécute les commandes par itérations.** Le [guide du mode Agent](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/use-copilot-agents/use-agent-mode?tool=vscode) décrit la sélection d’Agent dans le chat, la revue des changements et l’extension par MCP. La disponibilité et l’approbation des commandes dépendent aussi de la configuration et de l’administration.

**Évaluez volontairement le transfert de contexte.** Sélectionnez une fonction et demandez une explication de sa gestion des erreurs. Demandez ensuite une petite modification avec un test indépendant. Notez si vous devez fournir des fichiers voisins ou corriger une hypothèse de l’agent.

{{< figure src="copilot-terminal-editor-bridge.webp" alt="Invite de terminal reliée à une sélection de l’éditeur et à une différence de code côte à côte dans un espace de dépôt" caption="Une session CLI connectée combine l’entrée du terminal avec la revue de l’éditeur" >}}

## Relier les deux interfaces

```text
/ide
```

**Utilisez `/ide` dans une session interactive Copilot CLI** pour inspecter ou modifier la connexion VS Code. Le [guide de connexion](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/connecting-vs-code) documente la correspondance d’un espace approuvé, le partage de la sélection et l’affichage des changements proposés en diffs.

**La connexion automatique dépend de la correspondance de l’espace de travail.** Un CLI local ne se connecte pas à un Codespace distant parce que le nom du dépôt correspond. Exécutez le CLI dans l’environnement correspondant. Une autorisation large de modification contourne aussi l’approbation des diffs. Vérifiez les permissions si les invites attendues disparaissent.

**Les transcriptions CLI apparaissent dans la vue Sessions de VS Code**, avec une reprise via Resume in Terminal. Le flux du terminal est conservé. La conversation ne devient pas pour autant une session native interchangeable de l’agent de l’éditeur.

| Avant la connexion | Vérifier |
|---|---|
| **Espace de travail** | Le dossier voulu est ouvert et approuvé |
| **Lieu d’exécution** | Le CLI et l’intégration de l’éditeur visent le même environnement |
| **Sélection** | Le code sélectionné correspond à la demande actuelle |
| **Permissions** | La revue des changements proposés reste active si nécessaire |
| **Session** | La conversation voulue se poursuit |

## Modèles, facturation et règles

**Utilisez le même modèle sélectionné pour les deux essais quand il existe.** Si les choix diffèrent, notez la différence. Un modèle, un contexte ou un ensemble d’outils différent modifie l’expérience au-delà de l’opposition graphique-terminal.

**Vérifiez la comptabilisation actuelle dans votre compte.** La documentation du mode Agent de GitHub mentionne AI Credits. N’appliquez pas d’anciennes estimations de requêtes premium sans vérifier la facturation. Une invite CLI et une tâche d’éditeur ne représentent pas automatiquement la même unité de travail.

**L’accès de l’organisation est requis.** Si une fonction manque, vérifiez les règles avant de réinstaller l’extension. Notez les outils et intégrations approuvés pour les deux surfaces. Une connexion fournisseur n’autorise pas automatiquement la modification de tous les dépôts ou le contact de tous les services externes.

## Effectuer un essai en parallèle

**Préparez deux copies de la même révision de départ.** Gardez les mêmes instructions et tests d’acceptation. Lancez le premier essai dans le CLI autonome et le second dans le mode Agent de VS Code. Ajoutez un troisième essai avec le CLI connecté si l’interaction mixte correspond à votre travail.

| Mesure | Pourquoi l’enregistrer |
|---|---|
| **Contexte fourni** | Révèle le travail manuel de préparation |
| **Exactitude** | Sépare le code plausible de la correction vérifiée |
| **Étapes d’approbation** | Montre la charge de supervision sous la même règle |
| **Temps de revue** | Mesure l’effort de compréhension du patch complet |
| **Réparations manuelles** | Capture le travail restant après l’agent |
| **Utilisation** | Relie le coût aux résultats acceptés |

**Gardez la récupération dans l’essai.** Refusez une approche proposée et expliquez pourquoi. Observez si l’essai suivant conserve le travail utile et respecte la correction. Cela révèle mieux l’usage quotidien qu’une démonstration unique sans interruption.

## Dépannage et prochaines étapes

**Si le CLI se connecte à la mauvaise fenêtre**, inspectez `/ide` et sélectionnez l’espace voulu. Si l’approbation visuelle disparaît, vérifiez les permissions générales de modification. Si le mode Agent est absent, inspectez l’état de l’extension et les règles de l’organisation.

**Choisissez le CLI autonome** lorsque le contexte du shell et l’appel répétable dominent. **Choisissez VS Code** lorsque le contexte par sélection, le travail intégré et la revue graphique dominent. **Utilisez le CLI connecté** lorsque l’entrée du terminal et l’inspection de l’éditeur fonctionnent bien ensemble.

**Pour comparer les fournisseurs**, lisez la [comparaison principale CLI](/articles/cli-coding-agents-comparison/) ou la [comparaison principale GUI](/articles/gui-coding-agents-comparison/). Gardez ces évaluations séparées de cet essai d’interfaces d’une même famille.
