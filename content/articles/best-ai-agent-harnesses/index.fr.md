---
title: "Meilleurs harnesses d'agents IA en 2026 : choisir selon le flux de travail"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Comparez Deep Agents, Claude Agent SDK, OpenAI Agents SDK, Pydantic AI, Pi et LangGraph selon l'exécution des outils, la mémoire, la reprise et l'effort d'intégration."
genre: ["Intelligence artificielle", "Développement logiciel", "Sécurité de l'IA"]
tags: ["harnesses d'agents IA", "meilleurs frameworks d'agents", "Deep Agents", "Claude Agent SDK", "OpenAI Agents SDK", "Pydantic AI", "agent de codage Pi", "LangGraph", "runtime d'agent", "appels d'outils", "mémoire d'agent", "gestion du contexte", "exécution durable", "permissions d'agent", "sécurité des agents IA", "agents IA locaux", "évaluation d'agents", "humain dans la boucle", "comparaison de SDK d'agents", "agents de production"]
cover: "/img/cover/ai-agent-execution-components.webp"
coverAlt: "Composants métalliques modulaires reliés à un processeur central lumineux par des chemins turquoise et orange sur une surface de travail sombre"
coverCaption: "Illustration conceptuelle des composants autour d'un modèle d'IA."
---

**Deep Agents est mon premier choix pour un agent généraliste avec des modèles configurables et une gestion intégrée du contexte.** Claude Agent SDK convient bien à l'intégration du comportement d'exécution de Claude Code. OpenAI Agents SDK et Pydantic AI méritent un essai pour des agents propres à une application, tandis que Pi privilégie un noyau extensible réduit et LangGraph privilégie un contrôle explicite du flux de travail.

**Le meilleur choix dépend du travail que vous voulez accepter.** Un assistant de recherche, un éditeur de dépôt et un service qui traite les demandes des clients ont besoin d'outils et de règles de reprise différents. Ces recommandations sont des jugements éditoriaux fondés sur la documentation officielle vérifiée le **10 octobre 2026**, et non des résultats d'un benchmark de performance pratique.

<!--more-->

## Points essentiels

- **Choisissez d'abord l'abstraction :** agent assemblé, SDK d'application ou runtime de workflow.
- **Vérifiez les limites d'exécution :** l'approbation des outils, l'isolation du système de fichiers et la politique réseau résolvent des problèmes différents.
- **Testez la reprise :** l'historique de conversation seul n'empêche pas les actions externes en double.
- **Mesurez le travail accepté :** incluez les échecs, le temps de revue et l'infrastructure dans votre comparaison des coûts.
- **Gardez le modèle explicite :** changer le modèle et le logiciel de l'agent teste le système complet, pas seulement le logiciel.

## Ce que fournit un harness

Un **harness d'agent est le logiciel qui entoure un appel de modèle.** Il prépare le contexte, expose les outils, exécute les actions approuvées, renvoie les résultats et décide quand continuer ou s'arrêter. Selon l'implémentation, il gère aussi la mémoire, la délégation, les permissions et la reprise.

Un **modèle** propose l'action suivante. Un **outil** réalise une opération. Un **runtime** exécute et conserve le workflow. Ces responsabilités se chevauchent dans les produits assemblés, mais les séparer vous aide à repérer les capacités manquantes.

| Composant | Question à poser |
|---|---|
| **Gestion du contexte** | Quelles exigences survivent à une longue exécution ? |
| **Exécution des outils** | Qui valide les arguments et limite l'autorité ? |
| **Stockage de l'état** | Que reste-t-il après un redémarrage du processus ? |
| **Vérification** | Quelles preuves établissent la fin du travail ? |

Considérez un **agent de support illustratif** chargé d'inspecter une commande et de préparer une demande de remplacement. La lecture de la commande, la proposition d'un remplacement et son envoi doivent avoir des autorisations séparées. Une explication convaincante ne prouve pas l'autorisation d'envoyer la demande, et une transcription enregistrée ne prouve pas que l'envoi a déjà eu lieu.

**Portée :** ce guide compare des logiciels et des runtimes intégrables. Pour les interfaces de développeur quotidiennes, consultez la [comparaison des agents de codage CLI](/articles/cli-coding-agents-comparison/) ou la [comparaison des agents de codage GUI](/articles/gui-coding-agents-comparison/). Une comparaison de SDK ne doit pas devenir discrètement un classement d'outils de terminal face aux extensions d'éditeur.

## La sélection pratique

| Besoin de départ | Première option à évaluer | Responsabilité principale qui vous revient |
|---|---|---|
| **Agent généraliste** | Deep Agents | Configurer le backend, les permissions et le modèle |
| **Claude Code dans une application** | Claude Agent SDK | Exploiter et isoler le processus d'exécution |
| **Workflow d'outils applicatifs** | OpenAI Agents SDK | Définir les outils, les approbations et l'acceptation |
| **Application Python typée** | Pydantic AI et son package Harness | Choisir les capacités et l'espace de travail |
| **Noyau de codage minimal intégrable** | Pi SDK | Assembler les extensions et la politique d'exécution |
| **Workflow durable explicite** | LangGraph | Concevoir l'état du graphe et la reprise |

**Ces options sont des points de départ différents.** Deep Agents utilise déjà LangGraph, donc le choisir n'est pas nécessairement une décision exclusive. Pydantic AI sépare aussi son framework d'agent principal des capacités assemblées du harness. Comparez la quantité de code applicatif que vous devez posséder au lieu de traiter chaque ligne comme une bibliothèque interchangeable.

**Commencez par la plus petite couche qui passe le test d'acceptation.** Utilisez un framework applicatif typé pour des appels d'outils bornés, un agent assemblé pour un travail ouvert sur des fichiers ou de la recherche, et un graphe explicite lorsque la reprise et les transitions exigent des états nommés. Ajoutez mémoire, accès shell ou sous-agents seulement après qu'un test a montré pourquoi la couche simple échoue.

## Deep Agents : capacités assemblées

**Choisissez d'abord Deep Agents pour un agent qui travaille sur des fichiers, des outils et de longues conversations.** Sa [présentation officielle](https://docs.langchain.com/oss/python/deepagents/overview) documente les backends de système de fichiers, le déchargement du contexte, les résumés, les sous-agents et l'approbation humaine. Il s'appuie sur LangChain et le runtime LangGraph, avec des intégrations pour plusieurs fournisseurs de modèles.

**La configuration détermine toujours le comportement.** La documentation actuelle indique que la planification des tâches est opt-in à partir de la version 0.7. Ne supposez pas qu'un tutoriel d'une ancienne version décrit les valeurs par défaut actuelles. Notez la version du package et le middleware activé dans votre évaluation.

**Inspectez soigneusement la portée des permissions.** Les règles documentées du système de fichiers couvrent les outils de fichiers intégrés, pas les commandes shell arbitraires via les backends sandbox. Refuser un outil de fichier ne suffit pas si un autre chemin d'exécution atteint le même fichier. Testez ensemble le backend et la limite shell.

**Ma recommandation :** mettez-le sur votre liste pour un service d'analyse de documents ou de dépôt lorsque vous voulez des capacités assemblées et le choix du fournisseur. Préférez un point de départ plus petit lorsque le travail consiste en deux appels API étroitement définis et une réponse validée. Des outils supplémentaires ajoutent du comportement à évaluer.

## Claude : exécution intégrée

**Choisissez Claude Agent SDK si vous voulez l'agent Claude Code dans votre application.** Anthropic décrit une bibliothèque Python et TypeScript qui utilise la même boucle d'exécution, les mêmes outils et la même gestion du contexte que Claude Code. Le SDK exécute le binaire Claude Code dans un processus que vous exploitez. Il se distingue du client API Anthropic de base et des Managed Agents hébergés. [Présentation de l'Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview).

**L'intérêt est de réutiliser un système d'exécution existant.** Les opérations sur les fichiers, les commandes, les hooks, les permissions, les sessions et les sous-agents sont des capacités documentées. Votre intégration fournit la limite de l'application et les contrôles d'acceptation propres à la tâche.

**L'hébergement reste une décision d'ingénierie.** Les [conseils de déploiement](https://code.claude.com/docs/en/agent-sdk/secure-deployment) d'Anthropic traitent les contrôles du système de fichiers, les restrictions réseau et l'isolation. Configurez-les autour du processus au lieu de considérer une demande de permission comme une limite du système d'exploitation.

**Ma recommandation :** évaluez-le pour l'automatisation de documents ou de code centrée sur Claude avec beaucoup de travail sur les fichiers et les commandes. Choisissez une alternative flexible côté fournisseur si la comparaison de modèles locaux et de plusieurs fournisseurs hébergés est une exigence centrale du produit.

| Option assemblée | Priorité d'intégration |
|---|---|
| **Deep Agents** | Sélection du modèle, middleware et configuration du backend |
| **Claude Agent SDK** | Exécution de Claude Code dans un processus applicatif |

## OpenAI : workflows d'outils applicatifs

**Choisissez OpenAI Agents SDK pour une application organisée autour de fonctions, de tâches déléguées et de sorties explicites.** Sa [présentation](https://openai.github.io/openai-agents-python/) documente la boucle d'agent, les handoffs, les guardrails, le tracing et les capacités d'agents sandbox. Le SDK fournit une interface de construction distincte de l'application développeur Codex.

**L'approbation est un comportement configurable.** Le [guide human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/) décrit les exécutions interrompues et l'état sérialisé pour reprendre après une décision. Pour les outils shell et patch locaux, l'approbation est opt-in. Ajouter un callback d'approbation seul n'active pas l'obligation d'approbation.

**La prise en charge des modèles dépasse OpenAI.** La [documentation des fournisseurs](https://openai.github.io/openai-agents-python/models/) décrit les points d'intégration et les adaptateurs pour des fournisseurs externes. Validez les sorties structurées, les appels d'outils et le transport avec votre endpoint au lieu de supposer une parité des fonctions.

**Ma recommandation :** mettez-le sur votre liste pour un service dont les actions utiles existent déjà sous forme de fonctions applicatives bien définies. Par exemple, récupérez une commande, calculez l'éligibilité dans du code ordinaire et préparez une demande structurée. Gardez l'autorisation et les contrôles d'éligibilité dans l'application même lorsque le modèle sélectionne l'outil suivant.

## Pydantic AI : applications typées

**Choisissez Pydantic AI lorsque les types Python et les sorties validées sont centraux dans votre application.** Sa [documentation principale](https://pydantic.dev/docs/ai/overview/) couvre les outils typés, l'injection de dépendances, les sorties structurées et les intégrations d'exécution durable. La validation établit la structure requise de la sortie. Elle n'établit pas la véracité de chaque champ.

**Le package Harness séparé ajoute des capacités assemblées.** Sa [documentation](https://pydantic.dev/docs/ai/harness/) présente les piles Coder et Researcher, l'accès aux fichiers et au shell, la mémoire et les intégrations d'espace de travail. Un espace local et un sandbox isolé sont des choix d'exécution différents. Les capacités de harness pertinentes exigent un espace de travail au lieu d'en sélectionner un en silence.

**Ma recommandation :** évaluez le framework principal pour un service Python qui renvoie des enregistrements typés. Ajoutez les capacités de harness lorsque la tâche exige aussi l'exploration d'un espace de travail ou une recherche ouverte. Vous éviterez ainsi d'ajouter un accès shell à un service d'extraction borné sans besoin concret.

Pour un **agent illustratif de revue de factures**, la validation du schéma vérifie qu'un total est numérique et qu'une devise appartient à un ensemble autorisé. Une logique applicative séparée compare le total aux lignes et vérifie les preuves sources. Les deux contrôles font partie de l'essai.

| Préoccupation applicative | Test d'acceptation |
|---|---|
| **Sortie structurée** | Valider les champs et vérifier séparément leur sens |
| **Pause d'approbation** | Conserver l'action en attente et la décision exactes |
| **Changement de fournisseur** | Répéter les tests de compatibilité des appels d'outils et des sorties |

## Pi : noyau extensible réduit

**Choisissez le SDK de Pi si vous voulez contrôler directement une implémentation compacte d'agent de codage.** La [documentation du projet](https://github.com/earendil-works/pi/tree/main/packages/coding-agent) décrit l'intégration SDK et RPC avec son interface interactive. Son ensemble d'outils par défaut comprend la lecture, l'écriture, la modification et l'exécution shell, avec des extensions pour ajouter d'autres comportements.

**Le minimalisme reporte du travail sur l'intégrateur.** Pi omet volontairement les fenêtres de permission intégrées et l'orchestration de sous-agents. Sa documentation oriente les utilisateurs vers des conteneurs ou des extensions personnalisées pour les flux de confirmation. Évaluez ici le SDK intégré, et non son interface terminal face à l'éditeur graphique d'un autre fournisseur.

**Ma recommandation :** évaluez Pi pour un service de codage personnalisé si vous êtes prêt à gérer les restrictions d'exécution, la revue des extensions et la politique de reprise. Son petit noyau facilite la compréhension et la modification du comportement. Il convient moins comme point de départ lorsque votre exigence principale est un système d'approbation et d'orchestration déjà assemblé.

## LangGraph : contrôle explicite du workflow

**Choisissez LangGraph lorsque le workflow lui-même exige des états et des transitions explicites.** Sa [documentation de persistance](https://docs.langchain.com/oss/python/langgraph/persistence) distingue les checkpoints liés aux threads des stores partagés entre threads. Un checkpointer persistant prend en charge la reprise après un redémarrage du processus. Un checkpointer en mémoire ne le fait pas.

**LangGraph est une base de runtime.** Vous définissez le workflow et décidez où placer le comportement piloté par le modèle. Deep Agents utilise déjà cette base. Descendre au niveau de LangGraph a donc du sens lorsque vous avez besoin d'un contrôle plus direct des chemins d'exécution.

**Ma recommandation :** évaluez-le pour un processus avec des étapes nommées, des pauses de revue et des règles de reprise distinctes. Un workflow d'entrée de documents pourrait extraire des champs, les valider, demander une revue et publier un enregistrement approuvé. Les transitions fixes sont utiles lorsque le modèle doit choisir le contenu sans inventer le processus métier.

| Étape du workflow | Preuve de fin |
|---|---|
| **Extraire** | Enregistrement candidat lié à la source |
| **Valider** | Contrôles déterministes et exceptions |
| **Revoir** | Décision attachée au candidat précis |
| **Publier** | Reçu externe associé à l'opération |

**Les effets externes exigent leur propre conception de reprise.** Enregistrer l'état du graphe ne rend pas atomique une transaction de service distant avec le checkpoint. Utilisez un identifiant d'opération et rapprochez le résultat externe avant de réessayer une soumission.

## Tester les éléments manquants

**Une liste de fonctionnalités ne constitue qu'un point de départ.** Faites passer chaque candidat par des échecs proches de votre charge de travail. Utilisez un espace de travail jetable et des services de test contenant des données synthétiques.

| Test | Preuve à conserver |
|---|---|
| **Soumission interrompue** | Un seul effet externe après la reprise |
| **Conversation longue** | Les exigences initiales restent satisfaites |
| **Action rejetée** | Aucun effet par un outil alternatif |
| **Instruction non fiable dans un document** | Le texte du document n'acquiert pas d'autorité |
| **Arguments d'outil mal formés** | Rejet avant toute mutation applicative |
| **Budget épuisé** | Arrêt borné avec travail partiel inspectable |

**Définissez explicitement la répétition.** Pour un service de demandes de remplacement, arrêtez le worker après l'acceptation d'une demande par le service de test mais avant l'enregistrement local de la fin. Au redémarrage, le workflow doit rechercher l'identifiant d'opération au lieu de soumettre aveuglément une nouvelle fois. Il s'agit d'un test proposé, et non d'un résultat observé pour les produits cités.

**Vérifiez les preuves après une compression.** Placez une exigence importante au début de la tâche, puis fournissez assez de contenu réaliste pour déclencher la stratégie de contexte configurée. Demandez à l'agent de produire son artefact final et les références sources associées. Notre [analyse du CLM et de la mémoire d'agent](/articles/context-language-models-agent-memory-hallucinations/) explique pourquoi conserver des notes et conserver des preuves exactes sont deux sujets distincts.

**Examinez les destinations de télémétrie.** Les traces d'outils et les stores mémoire contiennent souvent des données de tâche. Notez les systèmes qui les reçoivent et leur durée de conservation. Une inférence avec un modèle local n'implique pas une journalisation, une récupération ou une exécution exclusivement locales.

## Comparer le coût par tâche acceptée

**Utilisez deux axes d'évaluation.** Une comparaison contrôlée garde le modèle, les outils, le jeu de tâches et les budgets constants lorsque les candidats le permettent. Une comparaison de déploiement utilise la configuration prévue pour chaque candidat. La première isole certains effets logiciels. La seconde répond à la question de l'installation complète qui sert le mieux votre travail.

**Ne forcez pas les configurations non prises en charge dans l'axe contrôlé.** Si deux candidats n'ont pas de modèle ou d'interface d'outils communs, présentez la comparaison comme une évaluation système. Gardez l'effort de configuration et le pilotage humain dans les résultats.

```yaml
# Illustrative trial record, not a framework configuration file
candidate: "package and pinned version"
model: "provider and exact model identifier"
workspace: "isolated test environment"
task_set: "frozen fixtures and acceptance checks"
limits:
  elapsed_minutes: 15
  model_calls: 30
  tool_calls: 60
record:
  - accepted_result
  - unsupported_claims
  - duplicate_external_actions
  - inference_cost
  - infrastructure_cost
  - human_review_minutes
  - recovery_outcome
```

**Exécutez plusieurs essais par tâche.** Gardez les tentatives infructueuses au dénominateur et rapportez les nombres bruts avec les pourcentages. Un petit essai révèle des profils d'échec, et non un classement stable du secteur.

**Calcul de coût illustratif :** supposons que la configuration A dépense 12 $ sur dix tentatives et produise huit résultats acceptés. Son coût d'inférence par tâche acceptée est de 1,50 $. La configuration B dépense 8 $ mais produit quatre résultats acceptés, soit 2,00 $ par tâche. Aucun nombre n'inclut la revue humaine ni l'infrastructure. Ces éléments appartiennent à un total enregistré séparément.

**Fixez les échecs disqualifiants avant le test.** Une soumission non autorisée ou une fuite de données entre utilisateurs ne doit pas disparaître dans une moyenne de qualité. Après avoir imposé ces exigences, comparez la justesse, la reprise, l'effort de revue et le coût.

## Faire un choix borné

**Commencez avec deux candidats et un workflow réel.** Pour un agent assemblé flexible côté fournisseur, comparez Deep Agents à une alternative plus étroite adaptée à votre application. Pour le comportement de Claude Code dans un service, essayez Claude Agent SDK. Pour une application typée, comparez Pydantic AI et OpenAI Agents SDK. Choisissez Pi si le comportement personnalisé justifie l'intégration supplémentaire, et LangGraph si le contrôle explicite du workflow est prioritaire.

**Prérequis de l'essai :** accès approuvé au modèle, fixtures synthétiques, espace de travail isolé lorsque nécessaire et critères d'acceptation écrits. Réservez un après-midi initial à la configuration et aux tests d'échec de base, puis collectez des exécutions répétées avant de décider pour la production. La difficulté va d'intermédiaire à avancée selon les actions externes et les exigences de reprise.

**Sélectionnez le plus petit système qui satisfait vos exigences.** Conservez les fixtures d'essai, les versions des packages et les rapports d'échec. Relancez-les lorsque vous changez le modèle, la stratégie de contexte, les outils ou le backend d'exécution. Ces changements modifient le système évalué.

## Références

- [LangChain: présentation de Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview)
- [Anthropic: présentation de Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)
- [Anthropic: déploiement sécurisé](https://code.claude.com/docs/en/agent-sdk/secure-deployment)
- [OpenAI: Agents SDK](https://openai.github.io/openai-agents-python/)
- [OpenAI: exécution human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/)
- [OpenAI: intégration des modèles et fournisseurs](https://openai.github.io/openai-agents-python/models/)
- [Pydantic: présentation du framework IA](https://pydantic.dev/docs/ai/overview/)
- [Pydantic: AI Harness](https://pydantic.dev/docs/ai/harness/)
- [Earendil: SDK d'agent de codage Pi et modes d'intégration](https://github.com/earendil-works/pi/tree/main/packages/coding-agent)
- [LangChain: persistance de LangGraph](https://docs.langchain.com/oss/python/langgraph/persistence)
