---
title: "Quel modèle d'IA local devriez-vous exécuter ? Guide GPU, contexte et programmation pour octobre 2026"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Guide pratique d'octobre 2026 pour choisir des modèles d'IA locaux destinés aux agents de programmation. Comparez la mémoire GPU, la croissance du cache KV, la taille du contexte, la qualité de la quantification, le traitement des prompts, les niveaux de raisonnement et les coûts de location cloud."
genre: ["IA locale", "Matériel IA", "IA auto-hébergée", "Benchmark GPU", "Outils pour développeurs", "Économie de l'IA"]
tags: ["modèles IA locaux", "agents de programmation", "guide GPU", "VRAM", "cache KV", "fenêtre de contexte", "Qwen 27B", "mixture of experts", "quantification", "llama.cpp", "Ollama", "décodage spéculatif", "prédiction multi-token", "LLM local", "location GPU", "station de travail IA", "programmation par agent", "traitement des prompts", "vitesse d'inférence"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Une station de travail présentant des modèles d'IA locaux, l'utilisation de la mémoire GPU et les fenêtres de contexte d'un agent de programmation"
coverCaption: ""
ref: ["/articles/32gb-vram-qwen-27b-hardware-guide", "/articles/qwen38-27b-vast-ai-gpu-benchmark", "/articles/local-ai-2026-build-your-rig-now"]
---

**Le meilleur modèle local pour programmer est celui qui garde assez de votre projet en mémoire et le lit assez vite pour rester utile.** La taille du modèle compte toujours. Pourtant, un modèle qui ne tient qu'après un transfert vers la RAM système paraît souvent moins efficace qu'un modèle plus petit avec une fenêtre de contexte stable.

*Choisissez ensemble le modèle et le budget mémoire. Ne choisissez pas un modèle dans un classement avant de le forcer sur un matériel inadapté.*

Ce guide porte sur les agents de programmation, pas sur les prompts courts d'autocomplétion. Un agent lit des fichiers, des sorties d'outils, des erreurs de compilation et des résultats de tests avant d'écrire une correction. Ces entrées consomment du contexte et modifient le choix du matériel.

## La vidéo sert de référence

La vidéo suivante compare des modèles locaux sur plusieurs niveaux de mémoire GPU. Elle apporte des observations pratiques sur le choix des modèles et des résultats matériels rapportés. Cet article suit une approche distincte en organisant la décision autour du comportement mémoire, du contexte de l'agent, du traitement des prompts et du coût total de possession.

{{< youtube id="C9M6iUFtVB4" enable="true" title="J'ai testé chaque modèle d'IA local pour que vous n'ayez pas à le faire" description="Comparaison pratique de modèles d'IA locaux sur plusieurs niveaux de mémoire GPU, avec une attention portée aux charges de programmation et aux limites matérielles." >}}

## Pourquoi les classements échouent

Un classement de modèles associe généralement le nombre de paramètres à une quantité de mémoire GPU. Ce raccourci aide pour une première estimation. Il devient insuffisant dès qu'un agent de programmation lit un vrai dépôt.

Les poids du modèle constituent la première allocation. Le **cache KV** est l'allocation qui augmente. Il stocke les clés et les valeurs d'attention du contexte actif afin que le moteur n'ait pas à recalculer tout le prompt après chaque token généré.

| Consommateur mémoire | Ce qu'il contient | Pourquoi c'est important |
|---|---|---|
| **Poids du modèle** | Les paramètres quantifiés | Besoin de chargement initial |
| **Cache KV** | Notes du contexte actif | Augmente avec le prompt et la conversation |
| **Buffers d'exécution** | Espace temporaire pour les calculs | Varie selon le backend et la taille des lots |
| **Instructions de l'agent** | Prompts système et définitions des outils | Utilise du contexte avant l'arrivée des fichiers du projet |

**Le fait qu'un fichier de modèle tienne sur la carte ne prouve pas qu'il convient à un agent.** Le moteur a besoin de place pour le cache, les buffers temporaires, les définitions d'outils et la réponse suivante.

## Le contexte est le vrai budget

Les agents de programmation consacrent du contexte à bien plus que les fichiers source. Le budget comprend aussi les instructions système, les schémas d'outils, les listes de répertoires, les sorties shell, les messages du compilateur, les résultats de tests et les tours précédents de la conversation.

Trois connexions MCP avec des définitions d'outils verbeuses consomment souvent plusieurs milliers de tokens avant que l'agent ouvre un fichier du projet. Un petit contexte par défaut laisse alors peu de place au code. L'agent répond toujours, mais il perd l'ensemble de travail nécessaire aux réparations en plusieurs étapes.

La [FAQ du moteur Ollama](https://docs.ollama.com/faq) indique un contexte par défaut de 4 096 tokens. Le réglage `OLLAMA_CONTEXT_LENGTH` modifie cette valeur, tandis que `OLLAMA_NUM_PARALLEL` fait évoluer la mémoire nécessaire avec le nombre de requêtes simultanées. Notez ces deux valeurs avant de comparer un benchmark local à un résultat obtenu avec une seule requête.

```bash
OLLAMA_CONTEXT_LENGTH=32768 OLLAMA_NUM_PARALLEL=1 ollama serve
```

Cet exemple fixe un contexte par défaut de 32K pour une requête active. Il ne réserve pas 32K tokens aux fichiers du projet. Les instructions, les définitions d'outils, l'entrée et la sortie se partagent toujours la fenêtre.

### Une fiche de contexte simple

Avant de comparer les GPU, notez ces valeurs :

- **Taille du projet :** fichiers et nombre approximatif de lignes source dans une tâche normale.
- **Surcharge des outils :** prompt système, schémas MCP, outils shell et instructions de l'éditeur.
- **Charge d'erreur :** longueur habituelle des sorties du compilateur et des tests.
- **Contexte cible :** prompt le plus long que vous voulez conserver sans troncature.
- **Réserve de réponse :** espace réservé au patch prévu et à son explication.

Utilisez le résultat comme spécification de charge de travail. Un développeur qui modifie un fichier à la fois n'a pas le même besoin mémoire qu'un développeur qui demande à un agent de suivre une API dans un monorepo.

## Le cache KV change le classement

Deux modèles ayant un nombre de paramètres similaire ont souvent des coûts de contexte différents. Un modèle dense dont chaque couche contribue au cache croissant demande souvent plus de mémoire qu'un modèle utilisant une architecture d'attention hybride.

Un modèle de programmation 27B évoqué dans le matériel de référence utilise un nombre limité de couches à attention complète, tandis que les autres couches utilisent un résumé de taille fixe. Le coût rapporté du cache pour un contexte de 128K reste inférieur à 9 Go. Un modèle de taille comparable avec une attention entièrement croissante à chaque couche demande, selon le rapport, plus de 21 Go pour la même longueur de contexte.

Ces chiffres décrivent des architectures de modèles et des réglages d'exécution précis. Utilisez-les pour examiner l'architecture, pas comme une formule mémoire universelle.

| Comportement du modèle | Effet sur le contexte | Conséquence matérielle |
|---|---|---|
| **Attention complète à chaque couche** | Forte croissance du cache | Davantage de mémoire pour les longs prompts |
| **Attention hybride ou glissante** | Croissance plus faible du cache dans certaines couches | Plus de marge de contexte à taille de modèle égale |
| **Mixture of experts** | Moins de paramètres actifs par token | Moins de calcul par token, mais tous les poids doivent être stockés |
| **Extension pour long contexte** | Fenêtre de travail plus grande | Plus de mémoire pour le cache et de travail de traitement du prompt |

**Lisez l'architecture du modèle avant d'acheter de la mémoire.** Le nombre de paramètres masque à lui seul le coût d'une longue session de programmation.

## Choisissez selon le niveau de mémoire GPU

### Quatre à huit Go

Les petits modèles denses restent le choix pratique. Ils tiennent sur la carte, répondent vite et conviennent à l'autocomplétion, aux explications courtes et aux modifications ciblées de fichiers.

Un modèle plus grand avec déport vers le CPU peut produire du texte, mais le temps de réponse devient souvent le facteur limitant. Un agent de programmation effectue des lectures de fichiers et des appels d'outils répétés. Une configuration à quatre tokens par seconde transforme chaque réparation en longue attente, même lorsque le modèle fonctionne techniquement.

Les modèles mixture of experts offrent une autre voie. Une petite partie active réduit la pression de calcul, tandis que l'ensemble des poids réside en partie dans la mémoire système. Cette approche demande beaucoup de RAM et des chemins de transfert rapides.

| Charge de travail | Orientation conseillée |
|---|---|
| **Autocomplétion** | Petit modèle dense avec un prompt court |
| **Modifications d'un seul fichier** | Petit modèle instruct avec prise en charge des outils |
| **Agent sur tout un dépôt** | Louer un GPU plus grand ou augmenter d'abord la mémoire système |
| **Code privé sous NDA** | Utiliser un modèle local, en acceptant un périmètre plus petit ou des exécutions plus lentes |

**À ce niveau, achetez de la RAM système avant de viser un grand modèle.** Un petit modèle stable vaut mieux qu'un grand modèle qui passe l'essentiel de son temps à déplacer des données sur le bus.

### Douze à seize Go

Cette tranche ouvre l'accès à un modèle de programmation 27B, mais le choix de la quantification devient central. Une version standard en 4 bits proche de 17 Go ne tient pas sur une carte de 16 Go une fois les frais du moteur pris en compte.

Une version en 3 bits proche de 13 Go laisse plus de place au contexte. Une carte de 12 Go pousse vers une version en 2 bits ou vers un modèle mixture of experts plus petit. La qualité dépend du quantificateur et du processus de calibration. Deux fichiers ayant la même profondeur de bits donnent donc souvent des résultats différents en programmation.

Vérifiez ces éléments avant de télécharger un modèle quantifié :

- **Auteur du quantificateur et notes de version**
- **Données de calibration et résultats d'évaluation**
- **Compatibilité du tokenizer**
- **Tests d'appel d'outils**
- **Longueur de contexte avec la quantification choisie**
- **Prise en charge par Ollama, llama.cpp ou l'interface choisie**

**Ne considérez pas « 2 bits » ou « 3 bits » comme une description complète de la qualité.** La méthode de compactage et les données de calibration comptent.

### Vingt-quatre à trente-deux Go

C'est la plage la plus flexible pour un modèle de programmation 27B. Une carte de 24 Go accueille souvent une version en 4 bits avec un contexte utile, mais une fenêtre complète de 128K peut dépasser la mémoire restante. Une carte de 32 Go donne au moteur plus de place pour le cache et les allocations temporaires.

Cette plage facilite aussi la justification de l'achat. Un GPU traite la charge sans la complexité d'un partage entre deux cartes. Le système consomme moins qu'une configuration multi-GPU et le support logiciel est plus facile à tester.

| Capacité | Position pratique |
|---|---|
| **24 Go** | Modèle 4 bits solide, avec des limites de contexte à mesurer |
| **32 Go** | Modèle 27B en 4 ou 6 bits, avec davantage de marge de contexte |
| **48 Go** | Précision supérieure ou cache plus grand, sans changer de modèle principal |

**La plage de 24 à 32 Go est la zone d'achat raisonnable pour une programmation privée fréquente.** Elle évite les pires effets du déport sans imposer du matériel de centre de données dans un boîtier de bureau.

### Quarante-huit Go et plus

Plus de mémoire ne signifie pas automatiquement un nouveau modèle. Le même modèle 27B peut fonctionner en précision 8 bits sur une carte de 48 Go, avec un cache plus grand et moins de compromis. Le gain porte sur la régularité, l'espace de contexte et la qualité des sorties, pas sur un nouveau niveau de raisonnement.

À 128 Go, la décision change. Un modèle mixture of experts bien plus grand devient possible, mais le traitement du prompt devient une vraie contrainte. Un modèle génère parfois rapidement tout en mettant longtemps à lire un dépôt volumineux ou un nouveau résultat d'outil.

**Mesurez séparément la vitesse de préremplissage et la vitesse de décodage pour les grands modèles.** Une réponse rapide après une lecture lente du prompt reste lente dans un flux de travail avec agent.

## La vitesse de décodage ne représente que la moitié du test

**La vitesse de décodage** mesure les tokens générés par seconde. Elle répond à la question : « À quelle vitesse le modèle écrit-il ? » **La vitesse de préremplissage** mesure le traitement du prompt. Elle répond à la question : « À quelle vitesse le modèle lit-il ? »

Un agent passe une grande partie de son temps à lire. Chaque appel d'outil ajoute du texte. Un long fichier source, une trace d'erreur ou un journal de test entre dans le prompt avant le début de la réponse suivante.

| Mesure | Expérience utilisateur |
|---|---|
| **Tokens décodés par seconde** | Vitesse d'apparition de la réponse après le traitement |
| **Tokens de prompt par seconde** | Temps d'attente avant le début de la réponse |
| **Temps avant le premier token** | Délai combiné du traitement du prompt et de la préparation |
| **Rétention du contexte** | Quantité d'état du projet disponible pendant la tâche |

**Évaluez vos propres tailles de prompt.** Un prompt synthétique court masque le coût le plus important pendant le travail sur un dépôt.

## Commencez par les réglages du moteur

Les mises à niveau matérielles ne sont pas la première étape de performance. Testez les réglages du moteur avant d'ouvrir une page d'achat.

### Prédiction multi-token

Certaines combinaisons de modèles et de backends prédisent plusieurs tokens futurs, puis les vérifient en une seule passe. La fonction apparaît souvent sous la forme d'un indicateur d'exécution ou d'une configuration de modèle brouillon compatible.

Les tests rapportés dans le matériel de référence montrent de forts gains sur certaines cartes haut de gamme. Les résultats varient selon le fichier de modèle, le backend, le pilote et la carte. Les chemins Apple Metal peuvent perdre la fonction requise pendant la conversion.

### Niveau de raisonnement

Un modèle livré avec un raisonnement maximal passe plus de temps sur le travail interne avant de renvoyer un résultat. Un raisonnement moyen offre souvent un meilleur équilibre pour la réparation de code, surtout lorsque la tâche contient déjà un message d'erreur clair et cible un fichier précis.

Utilisez une matrice de test simple :

1. Exécutez la même correction de bug avec un raisonnement faible, moyen et élevé.
2. Notez le temps avant le premier token, le temps total, la réussite du patch et le résultat des tests.
3. Répétez avec un prompt court et un prompt de taille comparable à un dépôt.
4. Gardez le réglage qui termine la tâche le mieux, pas celui qui affiche le meilleur débit de tokens.

**Un raisonnement moyen avec un chemin multi-token compatible est un bon point de départ.** Vérifiez la qualité sur votre propre code avant d'en faire le réglage par défaut.

## Matériel local ou GPU loué ?

Le calcul loué gagne pour un usage occasionnel. Vous payez les sessions actives au lieu d'acheter, refroidir, mettre à jour et alimenter une carte toute l'année.

Le matériel possédé gagne lorsque la charge est fréquente, privée ou hors ligne. Il supprime aussi le temps d'attente et fournit un environnement stable pour les tests répétables.

| Situation | Premier choix préférable |
|---|---|
| **Quelques sessions par mois** | Louer un GPU ou utiliser une API |
| **Programmation privée quotidienne** | Acheter un système compatible de 24 à 32 Go |
| **Dépôt volumineux avec rechargements fréquents** | Louer d'abord et mesurer la vitesse de préremplissage |
| **Aucun code ne sort des locaux** | Posséder le plus petit système qui atteint la cible de contexte |
| **Expérimentation avec un nouveau modèle** | Louer avant d'acheter le matériel |

Calculez le seuil de rentabilité avec les heures actives, pas avec les heures du calendrier. Incluez l'électricité, le stockage, le refroidissement, la maintenance et le temps nécessaire pour garder le moteur fonctionnel.

**Un GPU haut de gamme acheté pour des expérimentations occasionnelles est une dépense de loisir.** Un système de 24 à 32 Go utilisé chaque jour pour un travail privé présente un meilleur argument économique.

## Une meilleure liste d'achat

Suivez cet ordre lorsque vous comparez un modèle et un GPU :

1. **Définissez la tâche.** Autocomplétion, correction d'un fichier, agent de dépôt ou analyse avec long contexte.
2. **Mesurez le prompt.** Comptez les instructions système, les schémas d'outils, les fichiers et les sorties de tests habituels.
3. **Examinez le cache.** Cherchez les notes d'architecture et les mesures de mémoire liées au contexte.
4. **Choisissez une quantification.** Vérifiez les résultats de qualité du fichier précis, pas seulement sa profondeur de bits.
5. **Testez le préremplissage et le décodage.** Utilisez des prompts issus de votre dépôt.
6. **Réglez le raisonnement.** Comparez le temps de tâche terminée avec plusieurs niveaux de raisonnement.
7. **Testez la confidentialité et la maintenance.** Confirmez où part le code source et qui maintient le backend.
8. **Comparez le coût de location.** Utilisez les heures actives prévues et incluez l'énergie dans l'estimation du système possédé.

## Recommandation finale

**Sous 12 Go, utilisez un modèle plus petit ou un modèle mixture of experts avec assez de RAM système.** Ne forcez pas un modèle dense 27B sur une configuration qui passe l'essentiel de son temps à déporter les données.

**De 12 à 16 Go, concentrez-vous sur la qualité de la quantification et une cible de contexte contrôlée.** Une version 2 ou 3 bits bien testée avec prise en charge des outils est plus utile qu'un fichier 4 bits qui ne tient jamais correctement.

**De 24 à 32 Go, un modèle de programmation 27B devient le choix pratique par défaut pour un travail privé quotidien.** Mesurez l'usage du contexte et la vitesse du prompt avant de supposer que toute la fenêtre annoncée est disponible.

**À partir de 48 Go, consacrez la mémoire supplémentaire à la précision, à l'espace du cache et à la stabilité des sessions avant de passer à un modèle plus grand.** Une fois la machine passée à 128 Go, la vitesse de lecture des prompts et l'économie de la location méritent plus d'attention que la capacité brute.

Le nom du modèle n'est que le point de départ. La question utile porte sur la quantité de contexte du projet qui reste après la part du modèle, du moteur, des outils et du cache.

## Lectures associées

- [32 Go de VRAM pour Qwen 27B : le guide matériel de l'IA locale](/articles/32gb-vram-qwen-27b-hardware-guide/), consacré aux options matérielles pour une charge 27B.
- [Benchmarks GPU de Llama 3.1 8B et Qwen3.8 27B sur Vast.ai](/articles/qwen38-27b-vast-ai-gpu-benchmark/), résultats mesurés sur GPU loué et limites du long contexte.
- [IA locale en 2026 : un modèle 27B dépasse Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/), qualité du modèle, quantification et économie du matériel local.
