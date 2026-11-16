---
title: "Configuration d’un serveur MCP : autorisations, tests des outils et suppression sécurisée"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Connectez un serveur documentaire MCP en lecture seule, inspectez ses outils, effectuez une vraie lecture, puis supprimez la connexion."
genre: ["Intelligence artificielle", "Outils de développement"]
tags: ["Configuration du serveur MCP", "Protocole de contexte des modèles (MCP)", "Autorisations MCP", "MCP Codex", "MCP Claude Code", "MCP OpenCode"]
cover: "/img/cover/effective-ai-mcp-server-setup.webp"
coverAlt: "Un client d’IA relié à un serveur documentaire en lecture seule, avec un outil et une limite d’accès visibles"
coverCaption: ""
---

[Retour au cours Pratique des flux de travail IA](/effective-ai-course-start/)

**Utilisez un serveur MCP lorsqu’une tâche requiert un outil réutilisable ou des informations à jour hors du projet.** Le Model Context Protocol, ou MCP, définit l’échange d’informations sur les outils, ressources et prompts entre un client et un serveur. Une entrée serveur ne prouve pas que l’outil fonctionne. Cette leçon teste une connexion documentaire en lecture seule.

**Objectif d’apprentissage :** distinguer la configuration d’une véritable lecture MCP et consigner la suppression sécurisée.

## Points clés

- **Hôte MCP :** application d’IA qui coordonne utilisateurs, modèles, autorisations et clients.
- **Client MCP :** composant du protocole qui communique avec un serveur.
- **Serveur MCP :** programme ou service distant qui fournit des outils, ressources ou prompts.
- **Découverte d’outil :** preuve qu’une capacité nommée apparaît dans le client.
- **Exécution d’outil :** preuve d’un appel réel et de son contenu retourné.
- **Portée des autorisations :** accès accordé par l’hôte, le serveur, le compte et l’utilisateur.

## Avant de commencer

**Prérequis :** [pratique du contexte et des transmissions](/articles/effective-ai-context-window-management/) et une installation actuelle de Codex CLI pour le parcours guidé. Prévoyez 35 minutes. Niveau intermédiaire. Les autres agents de programmation ont leurs propres guides ci-dessous. Le [serveur officiel OpenAI Docs MCP](https://learn.chatgpt.com/learn/docs-mcp) fournit une documentation développeur en lecture seule et ne nécessite aucun téléversement de données du cours.

**Utilisez le laboratoire synthétique du cours.** Ne connectez ni calendrier, ni messagerie, ni système de production pour cet exercice. Une lecture documentaire suffit pour comprendre les états de connexion.

## Comprendre la limite

| État | Ce qu’il prouve | Ce qu’il ne prouve pas |
|---|---|---|
| **Configuré** | Une entrée serveur existe | L’accessibilité |
| **Connecté** | Le client a joint le serveur | L’existence d’outils utiles |
| **Découvert** | Un outil nommé apparaît | La réussite de son appel |
| **Exécuté** | Un appel a renvoyé du contenu | L’exactitude de la tâche finale |
| **Vérifié** | La source et le résultat répondent à la question | La réussite de tous les futurs appels |

**MCP n’accorde pas lui-même une autorisation de compte.** L’hôte client, le serveur, l’authentification, la portée du compte et les réglages d’approbation locale comptent tous. La [spécification MCP](https://modelcontextprotocol.io/specification/2026-07-28) définit le protocole, tandis que chaque produit contrôle son interface.

**Traitez la sortie du serveur comme une source.** Une page récupérée ne peut pas remplacer votre tâche ni autoriser une écriture de fichier. Chaque définition d’outil ajoute aussi du contexte. Ne connectez que le serveur nécessaire à cette lecture et supprimez-le ensuite.

## Accéder à la documentation en lecture seule

**Dans Codex CLI,** exécutez ces commandes dans un terminal. La première ajoute le serveur documentaire public. La seconde liste les serveurs configurés.

```bash
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex mcp list
```

**Preuve de configuration attendue :** la liste contient `openaiDeveloperDocs`. Cela prouve uniquement l’enregistrement. Démarrez une nouvelle session Codex dans le dossier du laboratoire extrait et inspectez les outils MCP avec `/mcp`. Les noms affichés par votre version installée sont ceux à employer.

**Demandez une lecture réelle :**

```text
Utilise le serveur MCP de documentation développeur OpenAI pour trouver les consignes actuelles d’AGENTS.md.
Indique le titre et l’URL de la page source, deux points pertinents pour ce laboratoire, et l’outil MCP utilisé.
Ne modifie aucun fichier.
```
**Inspectez le résultat.** La page renvoyée doit présenter `AGENTS.md` comme des consignes de dépôt et inclure l’URL exacte. Ouvrez la page citée et confirmez son sujet. Une réponse sans appel MCP dans la transcription est une réponse ordinaire, pas une preuve d’exécution.

## Diagnostiquer un échec

**Si `codex mcp list` affiche le serveur, mais que `/mcp` n’affiche aucun outil,** l’enregistrement a réussi, mais la découverte a échoué. Redémarrez la session, inspectez les serveurs actifs avec `/mcp` et la configuration enregistrée avec `codex mcp get openaiDeveloperDocs`, puis vérifiez l’URL du serveur et l’accès réseau. Ne prétendez pas que la configuration seule prouve la réussite.

**Si un outil apparaît, mais que la lecture échoue,** consignez l’erreur et réessayez une fois après avoir vérifié la connectivité. Si le même appel échoue, utilisez la page officielle citée dans un navigateur comme source de secours et marquez l’exercice MCP incomplet. N’inventez aucun résultat d’outil.

## Supprimer la connexion

**Après la lecture,** supprimez le serveur d’exercice de Codex CLI et confirmez la disparition de l’entrée.

```bash
codex mcp remove openaiDeveloperDocs
codex mcp list
```

**Preuve de suppression attendue :** `openaiDeveloperDocs` est absent de la nouvelle liste. Redémarrez toute session Codex active avant de vérifier si ses outils disponibles ont changé. Supprimer une définition locale ne révoque aucune autorisation de compte distincte utilisée par un autre service.

## Passer à une autre application

**Claude Code et OpenCode prennent aussi en charge MCP.** Suivez le [guide MCP de Claude Code](https://code.claude.com/docs/en/mcp) ou celui d’[OpenCode](https://opencode.ai/docs/mcp-servers/) correspondant à la version installée. Consignez les cinq mêmes états : configuré, connecté, découvert, exécuté et vérifié. Le schéma de configuration et les autorisations d’agent OpenCode varient selon les versions. Reprenez les exemples du guide correspondant à votre installation.

**Pour un parcours dans le navigateur uniquement,** lisez la [page officielle AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) et remplissez la même fiche de vérification. Indiquez « non exécuté » pour la découverte et l’exécution des outils. Ce parcours enseigne la vérification des sources, mais ne démontre pas le fonctionnement de MCP.

## S’exercer et vérifier

**Votre livrable :** une fiche de connexion de cinq lignes avec le nom du serveur, le nom de l’outil, l’URL source, le résultat observé et la preuve de suppression. Excluez les jetons et identifiants de compte des captures et journaux.

**Critère de réussite :** le parcours connecté réussit seulement après une vraie lecture par outil, puis la suppression de la configuration. Le parcours de secours réussit l’exercice de vérification de source avec MCP indiqué comme non exécuté.

## Vérifier votre compréhension

1. **Question :** une entrée MCP enregistrée prouve-t-elle qu’un outil a fonctionné ? **Réponse :** non. Vérifiez la découverte, l’autorisation et une vraie lecture.
2. **Question :** quel coût de contexte entraîne une connexion MCP trop large ? **Réponse :** les descriptions et schémas d’outils consomment une partie du contexte actif.

## Dépannage

- **Commande `codex` inconnue :** installez ou mettez à jour Codex CLI depuis le guide officiel lié.
- **Serveur listé, aucun outil :** inspectez l’état de session et les diagnostics du serveur.
- **Appel d’outil avec contenu sans rapport :** précisez la requête et vérifiez la page source.
- **Suppression apparemment sans effet :** démarrez une nouvelle session et inspectez la liste de serveurs active.

## Étapes suivantes

**Poursuivez avec [Vérification des sorties d’IA](/articles/effective-ai-output-verification/).** Pour les extensions plus larges, consultez le [guide du site sur les plugins et outils MCP de Claude Code](/articles/claude-code-plugins-skills-mcp-tools/).

**Navigation du cours :** [Précédent : Gestion du contexte](/articles/effective-ai-context-window-management/), [Plan du cours](/effective-ai-course-start/).
