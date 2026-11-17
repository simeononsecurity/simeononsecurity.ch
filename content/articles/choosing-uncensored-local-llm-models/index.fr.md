---
title: "Comment choisir un modèle d’IA local sans censure"
date: 2026-11-15
lastmod: 2026-11-15
toc: true
draft: false
description: "Comparez les variantes locales selon les réponses complètes, les capacités préservées, l’usage du contexte, la quantification et la VRAM requise."
genre: ["IA locale", "IA auto-hébergée", "Sécurité de l’IA", "Matériel GPU"]
tags: ["IA locale sans censure", "ablitération", "LLM local", "VRAM", "longueur du contexte", "quantification", "Ollama", "Qwen3.8", "Gemma 4"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Un poste de travail local pour l’IA avec une carte graphique et des écrans affichant des visualisations de modèles et d’inférence"
coverCaption: ""
ref: ["/articles/local-ai-model-gpu-context-guide", "/articles/qwen38-27b-vast-ai-gpu-benchmark"]
---

**Choix du modèle :** évaluez chaque variante selon les réponses utiles qu’elle termine, la qualité qu’elle préserve et la mémoire nécessaire à votre charge de travail. Un faible nombre de refus ou une fiche de modèle populaire ne démontrent pas ces résultats.

Le terme **sans censure** ne correspond à aucune échelle de performance standard. Les éditeurs de modèles l’emploient pour désigner différentes modifications des poids, différents ajustements fins et modèles de conversation. Comparez chaque candidat à son modèle d’origine et testez les tâches que vous comptez lui confier.

{{< youtube id="j-VqPVjztJE" enable="true" title="J’ai testé tous les modèles d’IA locaux sans censure (de 8 Go à 32 Go de VRAM)" description="Comparaison de variantes de modèles locaux, de réponses terminées, de paramètres de contexte et de capacités mémoire GPU." >}}

## Ce que le terme indique

Un **modèle ablitéré** a subi une modification de ses poids visant certains comportements de refus. L’article de 2024 sur la direction du refus a présenté une méthode appliquée à 13 modèles de conversation ouverts. Des outils plus récents proposent d’autres approches. Heretic 2, par exemple, documente à la fois l’ablation de rang arbitraire et l’ablation directionnelle. Le libellé d’une fiche de modèle n’indique pas quel comportement a changé ni les effets de la modification.

Séparez ces quatre propriétés lorsque vous comparez des modèles :

| Propriété | Points à vérifier |
|---|---|
| **Comportement de refus** | Quelles demandes entraînent un refus, une réponse partielle ou une réponse complète ? |
| **Capacités préservées** | Comment les tâches factuelles, de raisonnement, de programmation et de mise en forme se comparent-elles au modèle d’origine ? |
| **Réponse terminée** | À quelle fréquence la génération se termine-t-elle avant la limite de jetons ou de temps ? |
| **Compatibilité avec l’environnement d’exécution** | Le fichier quantifié exact fonctionne-t-il avec assez de mémoire pour le contexte nécessaire ? |

Un modèle modifié reste probabiliste. **Évaluez séparément la qualité :** exactitude, fiabilité et usage sûr. Gardez un modèle normalement aligné à disposition pour les tâches où ses protections comptent.

## Pourquoi le nombre de refus classe mal les modèles

**Un score de refus** mesure un résultat sur un jeu de requêtes. Il révèle peu de choses sur l’exactitude factuelle, la longueur des réponses ou la capacité du modèle à produire une réponse finale avant d’épuiser son budget de génération.

**La comparaison de Qwen3.8-27B menée par Sapwell en septembre 2026** a testé le modèle de base et huit variantes avec le même environnement de service. Sa suite de 13 tâches mesurait les connaissances, les mathématiques, la programmation et la véracité. Un jeu HarmBench distinct contenait 400 demandes nuisibles, et un juge LLM a évalué les réponses complètes. Ces résultats concernent une famille de modèles, un GPU et un protocole d’évaluation.

| Variante Qwen3.8-27B de l’étude | Refus explicites sur 400 | Réponses dont le raisonnement n’a pas abouti |
|---|---:|---:|
| **Modèle de base** | 381 | 0 % |
| **OrcaRouter** | 2 | 38 % |
| **Trohrbaugh** | 122 | 15 % |

Le nombre élevé de refus du modèle de base allait de pair avec moins de sorties inachevées. Le nombre faible de refus d’OrcaRouter allait de pair avec un taux plus élevé de réponses inachevées. Trohrbaugh a conservé davantage de refus et produit moins de réponses inachevées. **Choisissez selon votre tâche et les compromis acceptables.**

**Une étude de 23 variantes Gemma 4 E4B** a constaté des pertes importantes sur certaines mesures de capacité pour la variante la plus téléchargée. Une modification plus limitée est restée proche du modèle de base lors du test. La popularité et le nombre de téléchargements décrivent l’adoption. Ils ne mesurent pas la qualité.

Ne rassemblez pas ces mesures en un seul score. **Séparez les indicateurs :** refus, achèvement, exactitude et latence. Notez aussi le jeu de requêtes, la révision du modèle, le modèle de conversation, l’environnement d’exécution, le contexte et la limite de sortie. Toute modification de ces paramètres change le sens de la comparaison.

## Analysez les réponses vides avant de remplacer un modèle

**Les jetons de raisonnement** sont comptabilisés dans la limite de sortie avant l’apparition du texte visible. Si cette limite est atteinte pendant le raisonnement interne, certains environnements renvoient une réponse vide ou tronquée. Ce résultat diffère d’un refus ou d’une réponse complète mais incorrecte.

**Le benchmark Qwen3.6-27B de Sapwell** a montré l’effet de ce problème sur les scores principaux. Les scores bruts en mathématiques variaient beaucoup, car certaines exécutions n’atteignaient jamais la réponse finale. Parmi les réponses terminées, les valeurs d’exactitude mesurées étaient beaucoup plus proches. Le benchmark séparait la capacité à répondre de l’épuisement du budget de raisonnement.

**Si une réponse est vide, vérifiez le motif d’arrêt de l’environnement et ses journaux.** Notez la longueur de la requête, l’allocation du contexte, la limite de jetons en sortie, la durée et la présence éventuelle d’un marqueur de réponse finale. Recommencez ensuite avec une limite de sortie plus élevée si la mémoire disponible le permet.

| Résultat | Catégorie probable à examiner |
|---|---|
| **Texte de refus** | Le modèle a décliné la demande. |
| **Sortie vide à la limite de jetons** | Le budget de sortie a été épuisé avant la réponse finale. |
| **Sortie tronquée** | La limite de génération a interrompu une réponse incomplète. |
| **Erreur de l’environnement** | Le serveur, le fichier du modèle ou l’allocation mémoire a échoué. |
| **Réponse complète mais erronée** | Le modèle a renvoyé du texte, mais a échoué au contrôle d’exactitude. |

**Sortie vide :** vérifiez le résultat de l’environnement avant de qualifier chaque cas de défaut du modèle. Une fenêtre de contexte plus grande ne corrige pas automatiquement une petite limite de sortie, un modèle de conversation mal formé ou un délai d’expiration de l’application.

## Réservez de la VRAM aux poids et au contexte

Le fichier du modèle n’est qu’un des éléments qui utilisent la mémoire. L’environnement a aussi besoin d’espace pour le **cache KV**, qui conserve l’état d’attention de la requête et de la réponse actives, ainsi que pour les tampons de calcul et les autres processus chargés. Augmenter la longueur du contexte augmente l’usage mémoire.

**La documentation actuelle d’Ollama** indique des fenêtres de contexte par défaut de 4K sous 24 Gio de VRAM, de 32K entre 24 et 48 Gio, et de 256K à partir de 48 Gio. Ces valeurs décrivent le comportement par défaut de l’environnement. Vérifiez le contexte alloué et le placement du processeur avec `ollama ps`.

**Exemple Linux :** cette commande définit une valeur par défaut de 16K pour les nouvelles sessions du serveur Ollama :

```bash
OLLAMA_CONTEXT_LENGTH=16384 ollama serve
```

**Vérifiez le contexte alloué** par rapport aux tailles habituelles des entrées et des réponses avec le modèle chargé :

```bash
ollama ps
```

Les colonnes `CONTEXT` et `PROCESSOR` indiquent l’allocation et si le modèle tourne sur le GPU ou est partiellement déporté. **Allocation du contexte :** une limite affichée ne garantit pas que toute la fenêtre tiendra dans la VRAM.

### Options initiales selon la mémoire GPU

**Candidats de départ :** ces familles de modèles sont apparues dans des comparaisons de variantes en 2026. Les tailles de fichiers proviennent de dépôts quantifiés précis. Vérifiez le fichier exact, la prise en charge par l’environnement et la mémoire mesurée avant de conclure qu’un candidat convient.

| Mémoire GPU | Candidat de départ | Principale contrainte |
|---|---|---|
| **8 Go** | Gemma 4 E4B, par exemple la variante `coder3101` | Réduit la taille du fichier de poids. Gardez de la mémoire pour le contexte et les tampons de l’environnement. |
| **12 Go** | Gemma 4 12B, par exemple le fichier GGUF Q4 de 7,4 Go de `TrevorJS` | Offre davantage de capacités au modèle, mais moins de place pour un long contexte qu’une variante plus petite. |
| **16 Go** | Un modèle plus petit ou un fichier Q3 de Qwen3.8-27B | Le dépôt Qwen indique 13,72 Go pour Q3_K_S. Son éditeur qualifie ce fichier de faible qualité. La marge pour le contexte sera limitée. |
| **24 Go** | Qwen3.8-27B Q4_K_S ou Q4_K_M | Le dépôt actuel indique des fichiers de 16,71 Go et 17,77 Go. Réservez de la place au cache et aux tampons. |
| **32 Go** | Qwen3.8-27B Q6_K | Le dépôt actuel indique un fichier de 23,46 Go. Un fichier plus grand laisse moins de mémoire au contexte qu’une quantification plus petite. |

*Utilisez ces options comme point de départ. Les dépôts et les versions changent, et la taille du fichier ne prédit pas à elle seule l’allocation mémoire de l’environnement ni la qualité des réponses.*

Les libellés de quantification GGUF résument un choix d’encodage. **Différences entre dépôts :** des fichiers ayant la même profondeur de bits nominale n’offrent pas forcément la même qualité. Un dépôt Qwen qualifie Q3_K_S de faible qualité et Q4_K_M de choix par défaut. Avant le téléchargement, vérifiez la taille exacte du fichier, la fiche du modèle, le format de requête et les résultats des tests.

**Pour dimensionner le cache et vérifier l’adéquation à un GPU local,** consultez le [guide des modèles locaux, du GPU et du contexte](/articles/local-ai-model-gpu-context-guide/). Ses recommandations portent sur la programmation. Cette page traite du comportement de refus modifié et de l’évaluation.

## Examinez le modèle de conversation et la source du modèle

Un **modèle de conversation** encadre les messages avec les jetons et instructions attendus par le modèle. Un paquet de modèle peut fournir un modèle personnalisé ou une consigne système. Ces changements modifient le comportement mesuré même si les poids sous-jacents restent identiques.

**Effet du modèle de conversation :** Sapwell a trouvé une variante Qwen3.8 dont le paquet contenait un personnalité demandant au modèle de ne jamais refuser ni avertir. Son affirmation d’un faible taux de refus dépendait de ce modèle. Sa comparaison a uniformisé les modèles de conversation pour faire ressortir les différences entre les poids. Ce contrôle ne prouve pas que le modèle fourni soit malveillant ou inutilisable.

**Avant l’installation :** vérifiez l’éditeur, le modèle de base, la licence, le processus de conversion, le quantificateur, le modèle de conversation et l’historique des révisions. Comparez-le au modèle d’origine avec le même modèle de conversation et le même environnement. Si la fiche du modèle ne décrit ni la méthode ni le protocole de test, indiquez que la provenance est inconnue.

## Lancez une petite évaluation pour votre charge de travail

**Créez un jeu de requêtes reproductible** à partir de tâches ordinaires qui vous appartiennent ou que vous êtes autorisé à tester. Incluez le travail que le modèle effectuera, des questions factuelles dont vous connaissez les réponses et des demandes de mise en forme avec des critères de réussite clairs. Ajoutez quelques cas limites sans danger pour que le comportement de refus entre aussi dans la décision.

**Gardez les paramètres de test constants** pour le modèle d’origine et sa variante modifiée. Ne changez pas la consigne système, le modèle de conversation, la quantification, la version de l’environnement, le contexte, la limite de sortie ni les paramètres d’échantillonnage. Enregistrez la révision du modèle ou l’empreinte du fichier avec les résultats.

Suivez séparément chaque résultat :

- **Achèvement :** réponse finale, refus, sortie vide, troncature ou erreur de l’environnement.
- **Exactitude :** réussite ou échec selon une réponse attendue ou un barème.
- **Utilité :** capacité de la réponse à satisfaire les exigences de la tâche.
- **Latence :** temps jusqu’au premier jeton et durée totale de génération.
- **Mémoire :** contexte alloué, placement sur le GPU et pic de VRAM.
- **Comportement de sécurité :** refus ou poursuite appropriés pour chaque cas limite.

Répétez le jeu après avoir modifié une seule variable. Si la réponse se termine après l’augmentation de la limite de sortie, le premier échec venait du budget. Si elle reste incomplète, examinez le modèle de conversation, le mode de raisonnement, l’environnement et la révision du modèle. **Conservez la variante uniquement si elle améliore la tâche visée sans perte inacceptable d’exactitude ou de sécurité.**

## Isolez le déploiement

**Confidentialité :** l’inférence locale dépend de toute votre pile. Vérifiez l’interface, les journaux, les extensions, la télémétrie et les chemins réseau. Traitez les poids non fiables et les modèles personnalisés comme du code et de la configuration de tiers.

**Accès public :** n’exposez jamais directement le point de terminaison du modèle sur l’Internet public. Isolez l’accès aux outils et utilisez les variantes modifiées uniquement pour des tâches autorisées. Pour l’accès à distance, placez le point de terminaison derrière une passerelle privée dotée d’une authentification, de limites de requêtes et d’une isolation réseau. L’article original sur la direction du refus mentionne les conséquences de sécurité des modifications qui suppriment les refus.

## Décision

**Règle de décision :** choisissez le modèle qui obtient les meilleurs résultats vérifiés sur votre propre jeu de tâches. Utilisez le nombre de refus comme un indicateur, puis vérifiez l’achèvement des réponses, l’exactitude, le comportement du modèle de conversation et la marge de VRAM. Commencez avec un fichier adapté à votre GPU, réglez le contexte selon votre charge et comparez-le au modèle d’origine avec les mêmes paramètres.

**Pour dimensionner le GPU,** comparez ces résultats au [benchmark de location de GPU pour Qwen 27B](/articles/qwen38-27b-vast-ai-gpu-benchmark/). Louez ou empruntez le matériel avant de l’acheter si vous n’êtes pas sûr du fichier de modèle ou du contexte cible.

## Références

- [Benchmark d’ablitération de Qwen3.8-27B](https://nathan.sapwell.net/posts/qwen38-27b-abliteration/), Nathan Sapwell, 6 septembre 2026.
- [Benchmark d’ablitération de Qwen3.6-27B](https://nathan.sapwell.net/posts/qwen36-27b-abliteration/), Nathan Sapwell, 2026-05-17.
- [Benchmark des variantes Gemma 4 E4B](https://nathan.sapwell.net/posts/gemma4-e4b-abliteration/), Nathan Sapwell, 1er août 2026.
- [Benchmark des variantes Gemma 4 12B](https://nathan.sapwell.net/posts/gemma4-12b-abliteration/), Nathan Sapwell, 28 août 2026.
- [Le refus dans les modèles de langage est médié par une direction unique](https://arxiv.org/abs/2406.11717), Arditi et al., 2024.
- [Documentation du projet Heretic](https://github.com/p-e-w/heretic/).
- [Fiche officielle du modèle Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B).
- [Documentation d’Ollama sur la longueur du contexte](https://docs.ollama.com/context-length).
- [Fiche du modèle Gemma 4 E4B `coder3101`](https://huggingface.co/coder3101/gemma-4-E4B-it-heretic).
- [Fichiers GGUF Gemma 4 12B de TrevorJS](https://huggingface.co/TrevorJS/gemma-4-12B-it-uncensored-GGUF).
- [Fichiers GGUF OrcaRouter Qwen3.8-27B](https://huggingface.co/bartowski/orcarouter_Qwen3.8-27B-Uncensored-GGUF).
- [Format GGUF et types de quantification](https://huggingface.co/docs/hub/en/gguf), documentation Hugging Face.
- [Source vidéo : J’ai testé tous les modèles d’IA locaux sans censure (de 8 Go à 32 Go de VRAM)](https://www.youtube.com/watch?v=j-VqPVjztJE).
