---
title: "Hindsight auto-hébergé : mémoire locale pour agents et routage privé des modèles"
date: 2026-11-08
lastmod: 2026-11-12
toc: true
draft: false
description: "Étude de cas sur Hindsight auto-hébergé, les routes Qwen locales observées et le travail GPU par requête sans abonnement à un modèle hébergé sur les routes inspectées."
genre: ["IA locale", "IA auto-hébergée", "Agents IA", "Infrastructure IA", "Vie privée"]
tags: ["Hindsight", "Hindsight auto-hébergé", "mémoire des agents", "IA locale", "LLM local", "Qwen3.5", "LiteLLM", "VPN privé", "passerelle de modèles", "embeddings", "reranking", "planification GPU", "inférence privée", "Docker", "banques mémoire", "pages de connaissances", "routage local des modèles"]
cover: "/img/cover/self-hosted-hindsight-local-model-routing.webp"
coverAlt: "Un service mémoire privé achemine les tâches vers des serveurs locaux de modèles sur CPU et GPU"
coverCaption: "La mémoire, la récupération et les routes de modèles inspectées fonctionnent sur du matériel que nous possédons"
---

**Notre service mémoire Hindsight fonctionne sur du matériel que nous contrôlons.** Le moteur mémoire, la base de données, le modèle d’embeddings et le reranker fonctionnent dans un même déploiement auto-hébergé. Hindsight envoie les requêtes de génération vers une passerelle privée. Le backend Qwen partagé que nous avons inspecté et la route de mise à jour des pages testée utilisent des serveurs locaux, sans abonnement à une inférence hébergée.

Voici la description d’un déploiement opérationnel. **Auto-hébergé ne signifie pas hors ligne.** Le VPN utilise un service externe de coordination, et les images logicielles ainsi que les poids des modèles doivent être téléchargés. Cette affirmation porte sur le traitement de la mémoire et l’inférence du modèle, pas sur chaque connexion réseau de nos appareils ou des autres outils d’agents.

<!--more-->

## À retenir

- **Hindsight gère le flux mémoire.** Un conteneur Docker fournit l’API, les travailleurs et le plan de contrôle. Un volume persistant conserve les données des banques.
- **Les petits modèles de récupération restent locaux.** Les embeddings et le reranking s’exécutent dans le processus Hindsight sur le CPU.
- **Qwen génère le texte.** Retain, Reflect et Consolidation appellent l’alias privé Qwen3.5-4B avec le raisonnement désactivé et une sortie limitée. Le backend inspecté sert le modèle localement.
- **La mise à jour lente des pages reçoit un GPU.** Un alias de modèle distinct emprunte une carte pour une requête en arrière-plan, puis la libère une fois la requête terminée.
- **La passerelle masque l’emplacement physique.** Hindsight choisit un alias de modèle. Les services de routage privés choisissent un point de service.

## Définir les limites avant de choisir les modèles

**Hindsight est le moteur mémoire, pas le serveur de modèles.** L’image Docker complète inclut des modèles locaux d’embeddings et de reranking, mais la génération de langage nécessite un endpoint. Le [guide d’installation de Hindsight](https://hindsight.vectorize.io/developer/installation) explique cette séparation et présente les serveurs locaux llama.cpp, Ollama et vLLM comme solutions de remplacement aux fournisseurs hébergés.

**L’API mémoire reste sur le réseau privé.** Le plan de contrôle web fonctionne sur une interface locale. Un volume persistant conserve la base de données intégrée, afin qu’une recréation du conteneur ne supprime pas les banques. L’authentification protège l’API, et des banques distinctes organisent le contexte des projets.

**La passerelle de génération fournit des noms de modèles stables.** Hindsight envoie des requêtes compatibles avec OpenAI via le VPN et la passerelle privée. La passerelle les transmet à des endpoints locaux. La route Qwen inspectée atteint un déploiement LiteLLM associé à un serveur CPU local. La [documentation du routeur LiteLLM](https://docs.litellm.ai/docs/routing) décrit ce modèle d’alias. Un autre routeur compatible OpenAI peut remplir le même rôle.

{{< figure src="hindsight-private-request-path.webp" alt="Schéma montrant des agents, un service Hindsight privé, des modèles locaux de récupération, une passerelle privée et des serveurs Qwen locaux" caption="Le schéma omet les noms d’hôtes, les adresses, les clés d’accès et les noms des machines physiques" >}}

[Ouvrir le schéma complet du parcours d’une requête](hindsight-private-request-path.webp).

**Une API interne existe aussi.** Hindsight appelle une passerelle privée au format compatible OpenAI. Les routes de modèles inspectées servent l’inférence localement. Nous n’avons pas audité toutes les règles de secours de la passerelle. Examinez sa politique avant de considérer le traitement local comme une garantie pour chaque requête.

## Affecter chaque tâche mémoire au bon calcul

Les opérations Hindsight ont des fonctions différentes. **Retain** extrait des faits des nouveaux éléments. **Recall** trouve les souvenirs pertinents. **Reflect** recherche et rédige une réponse synthétique. **Consolidation** fusionne des faits associés. La **mise à jour des pages de connaissances** reconstruit un résumé évolutif à partir de la banque.

| Opération | Emplacement du modèle | Raison |
| --- | --- | --- |
| **Retain** | Qwen3.5-4B via la passerelle privée | Extraction structurée locale avec un budget de sortie limité |
| **Recall** | Embeddings et reranking locaux sur CPU | La recherche n’a pas besoin d’appeler l’API de génération |
| **Reflect** | Qwen3.5-4B via la passerelle privée | La synthèse nécessite une génération après la récupération mémoire |
| **Consolidation** | Qwen3.5-4B via la passerelle privée | Les petits lots limitent les longues réponses structurées |
| **Mise à jour d’une page de connaissances** | Route Qwen locale dédiée sur GPU | La grande synthèse en arrière-plan dépassait la durée maximale de la route CPU |

*Gardez les petites tâches de récupération sur CPU et réservez l’inférence GPU aux travaux longs que vous avez mesurés.*

Le conteneur Hindsight charge **BAAI/bge-small-en-v1.5** pour les embeddings et **hindsight-ai/hs-rerank-1** pour le reranking. Les journaux de démarrage confirment que les deux fonctionnent localement sur CPU. La [référence des modèles Hindsight](https://hindsight.vectorize.io/developer/models) décrit les options locales et la route facultative du modèle de décision.

Nous avons conservé le modèle d’embeddings actuel, car changer d’espace d’embeddings impose de reconstruire les vecteurs stockés. Le reranker fonctionne déjà localement. Un service de reranking hébergé créerait donc une nouvelle frontière de données sans résoudre le délai de génération observé. Un essai local de **hs-decide-1-flash** a produit une réponse Reflect correcte, mais le résultat a terminé près de la limite de temps du test. Les données synthétiques de Consolidation n’ont pas exercé la route de décision. Le modèle de décision est donc absent du routage de production.

## Réserver un GPU au travail lent en arrière-plan

**Le nom de modèle habituel et celui de la mise à jour diffèrent.** Retain, Reflect et Consolidation utilisent l’alias Qwen partagé. La mise à jour des pages en arrière-plan utilise un alias GPU propre au nœud et limite à un le nombre d’appels simultanés au modèle de langage. Une tâche de maintenance longue ne mobilise ainsi qu’un GPU à la fois.

**Une réservation liée à la requête limite l’usage du GPU.** Le pool GPU démarre un travailleur de modèle à l’arrivée d’une requête. Son contrôleur réserve une carte, traite la requête, arrête le travailleur, puis libère la réservation. Le schéma omet l’inventaire des machines physiques.

{{< figure src="hindsight-gpu-lease-cycle.webp" alt="Schéma d’un GPU réservé pour une mise à jour de page en arrière-plan, puis libéré quand la requête se termine" caption="Un bail lié à la requête réserve un GPU pour mettre à jour une page" >}}

[Ouvrir le schéma complet du cycle de réservation GPU](hindsight-gpu-lease-cycle.webp).

Cette séparation découle d’un échec mesuré. **Une mise à jour de page prioritaire CPU a atteint une limite d’une heure.** Après avoir routé les mises à jour en arrière-plan vers le pool GPU local, cinq pages précédemment en échec ont terminé en environ deux à six minutes lors d’une récupération. Ces chiffres décrivent ces pages et ces paramètres. Ils ne constituent pas un benchmark général du débit Qwen.

## Corriger les valeurs par défaut et les délais

**Les anciennes limites de sortie de Hindsight ne convenaient pas à notre routeur local.** Le routeur accepte au maximum 8 192 jetons de sortie et applique une limite de 256 jetons si la requête n’en indique aucune. Une ancienne limite Retain de 64 000 jetons a provoqué une erreur HTTP 400. Des lots Consolidation de huit faits ont atteint la limite de sortie, et Reflect avait besoin d’une limite explicite pour éviter le fallback de 256 jetons du routeur.

**Nous avons défini explicitement les limites de chaque tâche.** Le raisonnement Qwen est désactivé pour ces opérations mémoire. Hindsight autorise désormais quatre appels LLM simultanés au total, dont au plus un appel de mise à jour de page en arrière-plan. Le délai global LLM est de 1 800 secondes avec une nouvelle tentative du modèle.

| Charge | Limite de sortie ou de lot | Limites d’appel et d’opération |
| --- | --- | --- |
| **Retain** | 8 192 jetons de sortie | Délai d’appel général de 1 800 secondes |
| **Reflect** | 4 096 jetons de sortie | 900 secondes par appel, 3 600 secondes par opération |
| **Consolidation** | 4 096 jetons, quatre faits par appel | 900 secondes par appel, 14 400 secondes par opération |
| **Mise à jour de page** | Un appel de modèle simultané | 900 secondes par appel, route GPU dédiée |

*Ces valeurs décrivent notre déploiement de novembre 2026 et son routeur local.*

**Le délai d’un appel et la durée maximale d’une opération limitent des étapes différentes.** Certains appels Qwen valides dépassaient l’ancien délai de 300 secondes par appel. Les délais d’opération plus longs autorisent plusieurs appels, tandis que la limite de 900 secondes par appel borne toujours chaque tentative.

Lors de la récupération, plusieurs tâches Retain ont terminé avec **1 042 à 2 076 jetons de sortie**. Deux exécutions Consolidation ont terminé **41 sur 41** et **30 sur 30** éléments. Plus tard, l’expiration du délai d’une mise à jour de page a conduit à la route GPU distincte décrite plus haut. Ces résultats ne démontrent pas une fiabilité à long terme.

## Les compromis de cette conception

**Ne pas payer de modèle hébergé ne signifie pas que le coût est nul.** Le déploiement consomme du matériel détenu, de l’électricité, du stockage, du temps de maintenance et du temps GPU pendant les mises à jour. Chaque choix d’emplacement échange de la capacité contre de la latence ou de la simplicité opérationnelle.

| Choix | Avantage | Compromis |
| --- | --- | --- |
| **Génération d’abord sur CPU** | Laisse le GPU disponible | Une mise à jour testée a atteint sa limite d’une heure |
| **Mise à jour de page sur GPU** | Cinq pages ont terminé en deux à six minutes environ lors d’une exécution | Utilise la capacité GPU et dépend de la route dédiée |
| **Base intégrée** | Garde le déploiement compact | Réduit le domaine de panne et exige des sauvegardes testées |

*Utilisez une route GPU de mise à jour lorsque la latence CPU mesurée dépasse votre fenêtre de maintenance.*

Le [guide d’installation de Hindsight](https://hindsight.vectorize.io/developer/installation) recommande un PostgreSQL séparé pour les déploiements de production plus importants. **Notre base intégrée nécessite une procédure de sauvegarde et de récupération testée** à mesure que la banque grandit.

**L’inférence privée dépend du parcours.** Vérifiez le fournisseur Hindsight choisi, le mappage des modèles du gateway, les règles de secours, le processus de modèle local, la rétention des journaux et le trafic sortant. Les identifiants de trace Hindsight aident à corréler les requêtes, et Docker fait tourner les journaux du conteneur. Aucun de ces éléments ne prouve qu’une requête en aval est restée locale. Un audit du gateway fournit la preuve complète qui manque.

## Recommandation

**Commencez par des modèles locaux de récupération et des limites de génération explicites.** Placez Hindsight, les modèles d’embeddings et le reranker sur du matériel détenu. Faites passer la génération par un gateway privé compatible OpenAI au moyen d’un VPN. Mesurez chaque opération avant d’attribuer CPU ou GPU, et réservez la route GPU aux tâches de fond dont la latence CPU dépasse votre fenêtre de maintenance.

*Examinez chaque règle de secours du gateway et testez la récupération des banques avant de considérer le déploiement comme privé et résilient.* Le [guide des limites de confidentialité de l’IA locale](/articles/local-ai-privacy-boundary/) fournit une première liste de contrôle.

## Conclusion

**Ce déploiement conserve la mémoire Hindsight et les routes d’inférence inspectées sur du matériel détenu, sans abonnement à un modèle hébergé.** La récupération CPU, les appels Qwen bornés et la route GPU de mise à jour à un appel traitent des charges différentes. Les récupérations ont terminé Retain, Consolidation et les mises à jour de pages avec ces paramètres. Les prochaines vérifications sont l’audit de toutes les règles de secours du gateway, le test des sauvegardes et une observation de fiabilité plus longue.
