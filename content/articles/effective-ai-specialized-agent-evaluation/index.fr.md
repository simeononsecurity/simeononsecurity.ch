---
title: "OpenClaw et Hermes Agent : une évaluation pratique"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Évaluez des agents d’IA spécialisés et persistants à l’aide d’un inventaire des accès, d’un examen des déclencheurs, d’un relevé des flux de données et d’une décision de pilote."
genre: ["Intelligence artificielle", "Génie logiciel", "Productivité"]
tags: ["agents d’IA spécialisés", "OpenClaw", "Hermes Agent", "agents de travail", "évaluation des agents d’IA", "agents d’IA persistants"]
cover: "/img/cover/effective-ai-specialized-agent-evaluation.webp"
coverAlt: "Fiche répertoriant les outils, la mémoire stockée, les déclencheurs, les journaux et la décision d’examen d’un agent"
coverCaption: ""
---

[Retour au cours pratique sur les flux de travail avec l’IA](/effective-ai-course-start/)

**Choisissez un agent spécialisé selon la tâche et les accès nécessaires.** Un agent de travail qui examine un fichier diffère d’un système persistant qui reçoit des messages, stocke une mémoire et exécute des actions planifiées. Cette leçon facultative prend OpenClaw et Hermes Agent comme exemples, puis propose une fiche d’évaluation à remplir avant l’installation.

**Objectif pédagogique :** vous comparerez les accès et déclencheurs d’un agent, puis consignerez une décision pour un pilote limité.

## Points clés

- **Agent de travail à rôle défini :** agent chargé d’une question ou d’un livrable précis.
- **Agent persistant :** service ou session qui conserve un état ou répond à des déclencheurs ultérieurs.
- **Déclencheur :** événement, message ou planification qui démarre le travail.
- **Inventaire des accès :** liste des outils, comptes, fichiers et droits d’écriture accordés à l’agent.
- **Décision de pilote :** rejeter, lancer un test limité ou approuver un usage défini.

## Avant de commencer

**Prérequis :** [délégation](/articles/effective-ai-agent-delegation/), [boucles à objectifs délimités](/articles/effective-ai-bounded-agent-loops/) et un cas d’usage fictif. Prévoyez 35 minutes. Le niveau est intermédiaire. Cette leçon ne nécessite pas l’installation d’un agent persistant.

**Cas d’usage :** une personne qui coordonne un atelier souhaite qu’un assistant lise un planning et prépare un brouillon de rappel. La demande n’autorise pas l’envoi du rappel. Votre évaluation doit préserver cette limite.

## Comparer les rôles

| Approche | Type de tâche courant | Première question |
|---|---|---|
| **Un chat** | Rédiger un rappel | Le planning est-il disponible ? |
| **Agent en lecture seule** | Vérifier indépendamment les données du planning | Quelle source doit-il lire ? |
| **Agent de programmation** | Mettre à jour un programme local de rapports | Quels fichiers et tests s’appliquent ? |
| **Plateforme persistante** | Réagir aux messages ou aux plannings au fil du temps | Quels déclencheurs, outils et états stockés existent ? |

**OpenClaw** est une plateforme d’agents open source dotée d’une passerelle, de canaux de messagerie, d’outils, d’une mémoire, de connexions MCP et de sous-agents. Sa [présentation](https://docs.openclaw.ai/start/why-openclaw), son [guide de connexion MCP](https://docs.openclaw.ai/tools/mcp) et son [guide des sous-agents](https://docs.openclaw.ai/tools/subagents) décrivent ces composants. Avant un pilote, vérifiez les paramètres actifs des canaux, des outils et de l’isolation.

**Hermes Agent** est l’application d’agents de Nous Research. La famille de modèles Hermes est distincte. Sa [documentation](https://hermes-agent.nousresearch.com/docs/), son [guide de délégation](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation) et son [guide de configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/) couvrent l’interface en ligne de commande, la messagerie, les outils, la mémoire et les tâches déléguées. Son [guide de mémoire](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/) décrit les stockages locaux et l’approbation des écritures. La valeur par défaut documentée pour `memory.write_approval` et `skills.write_approval` est `false`. Activez l’approbation ou désactivez le stockage concerné pour un pilote nécessitant la vérification des écritures. Vérifiez la configuration en cours avant de vous fier à l’un ou l’autre de ces contrôles.

| Point d’évaluation | OpenClaw | Hermes Agent |
|---|---|---|
| **Point d’entrée** | Passerelle et canaux connectés | Interface en ligne de commande ou de messagerie configurée |
| **Travail délégué** | Sous-agents soumis aux règles de session et d’outils propres à la plateforme | Tâches déléguées soumises aux règles d’outils propres à la plateforme |
| **État persistant** | Examiner la mémoire activée et le stockage des sessions | Examiner les paramètres de mémoire et de profil, ainsi que les écritures des compétences |
| **Travail récurrent** | Examiner les déclencheurs et planifications configurés | Examiner les [tâches cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron/) et l’état de la passerelle |
| **Premier pilote** | Une demande manuelle via un canal choisi | Une demande manuelle via l’interface en ligne de commande ou la messagerie |

Ce tableau présente des points à examiner, pas des paramètres de sécurité équivalents. Notez la version installée et la configuration active avant d’accorder l’accès à des données ou comptes réels.

**Les noms ne définissent pas un modèle d’autorisation commun.** Un « sous-agent » d’un produit peut recevoir des fichiers, des outils et un historique différents de ceux d’un agent de travail d’un autre produit. Consultez la documentation de la version installée et ses paramètres actifs au lieu de transposer des hypothèses d’un outil à l’autre.

## Remplir une fiche des accès

**Ajoutez une ligne par capacité** avant d’installer ou de connecter un système. Utilisez les paramètres réels si le produit est disponible. Écrivez « inconnu » plutôt que de deviner.

| Question | Réponse pour le pilote de l’atelier |
|---|---|
| **Tâche** | Rédiger un rappel à partir d’un planning synthétique |
| **Entrée** | Un fichier de planning approuvé |
| **Fichiers** | Lire le fichier de planning, sans droit d’écriture |
| **Outils externes** | Aucun pour le premier pilote |
| **Accès aux comptes** | Aucun compte de messagerie ou de calendrier |
| **Déclencheur** | Demande manuelle uniquement |
| **Écritures de mémoire et de compétences** | Consigner les paramètres actifs, désactiver les stockages ou exiger l’approbation des écritures pendant le pilote |
| **Journaux** | Consigner le chemin de stockage, la règle de conservation, l’instruction, la révision de la source et le brouillon |
| **Vérification** | Une personne vérifie la date, l’heure, le lieu et la liste des destinataires |
| **Retour arrière** | Supprimer le brouillon et désactiver le pilote |

**Le flux de données fait partie de la fiche.** Indiquez où les données quittent votre ordinateur, quel fournisseur les traite et où les transcriptions ou la mémoire sont conservées. Si un outil se connecte à la messagerie, précisez s’il lit, rédige ou envoie. Ces autorisations sont distinctes.

## Prendre une décision de pilote

**Rejeter :** l’agent a besoin d’un vaste droit d’écriture sur une boîte aux lettres pour une tâche limitée à la rédaction, ou ses déclencheurs et journaux sont inconnus. Aucun essai n’est nécessaire pour rejeter une option inadaptée.

**Pilote :** limitez l’entrée au planning synthétique, utilisez un déclencheur manuel, désactivez l’envoi et examinez un brouillon. Le résultat attendu est une heure correcte de 19 h et aucun message envoyé. Consignez votre propre observation si vous réalisez le pilote.

**Approuver un usage défini :** seulement après la réussite des vérifications du pilote et l’acceptation, par la personne responsable, des accès, déclencheurs, durées de conservation et étapes de vérification précis. L’autorisation de rédiger ne permet ni l’envoi ni une automatisation ultérieure.

## Diagnostiquer un échec

**Supposons qu’un brouillon de rappel indique 18 h.** Vérifiez si l’agent a lu le planning à jour ou si une mémoire stockée ou un ancien message a fourni l’heure obsolète. Remplacez l’entrée obsolète, relancez un pilote manuel et laissez l’envoi désactivé. Un deuxième brouillon correct n’efface pas le premier échec du compte rendu.

**Supposons qu’une connexion MCP apparaisse dans les paramètres, mais qu’aucun outil ne soit accessible.** Consultez les [états de connexion MCP](/articles/effective-ai-mcp-server-setup/). La présence d’une entrée de serveur enregistrée ne prouve pas qu’une lecture a réussi.

## S’exercer et vérifier

**Votre livrable :** une fiche des accès remplie et une décision : Rejeter, Pilote ou Approuver un usage défini. Indiquez un déclencheur, une limite d’autorisation, une question sur le flux des données et un moyen d’arrêter l’agent.

**Vérification finale :** une autre personne doit comprendre quelle action l’agent effectue, ce qu’il lit et stocke, quand il s’exécute, qui vérifie le résultat et comment le désactiver. Si une réponse est inconnue, choisissez Rejeter ou un pilote plus limité.

## Vérifier sa compréhension

1. **Question :** Une tâche limitée à la rédaction d’un rappel nécessite-t-elle le droit d’envoyer des courriels ? **Réponse :** Non. L’envoi reste hors du périmètre du pilote.
2. **Question :** Quels paramètres Hermes faut-il examiner avant un pilote contrôlant les écritures ? **Réponse :** Vérifiez les paramètres actifs d’écriture de la mémoire et des compétences, y compris leurs contrôles d’approbation.

## Étapes suivantes

**Poursuivez avec le [projet de synthèse du flux de travail avec l’IA](/articles/effective-ai-capstone/)**. Pour une comparaison plus large des environnements d’exécution, consultez le [guide des environnements d’agents](/articles/best-ai-agent-harnesses/).

**Navigation du cours :** [Précédent : Boucles délimitées](/articles/effective-ai-bounded-agent-loops/), [Plan du cours](/effective-ai-course-start/).
