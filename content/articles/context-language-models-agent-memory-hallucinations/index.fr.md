---
title: "Les Context Language Models de Meta : une meilleure mémoire pour les agents, pas la fin des hallucinations"
date: 2026-10-06
lastmod: 2026-11-13
toc: true
draft: false
description: "Comment les Context Language Models modifient la mémoire des agents, ce que démontrent les benchmarks et comment les coûts du cache, les capacités du modèle et les notes non fiables influent sur la fiabilité."
genre: ["Intelligence artificielle", "Agents IA", "IA locale", "Sécurité de l’IA"]
tags: ["modèles de langage contextuels", "CLM", "Meta AI", "hallucinations de l’IA", "mémoire des agents", "gestion du contexte", "compression du contexte", "fenêtre de contexte", "Suffix Cache Reuse", "cache KV", "SGLang", "llama.cpp", "mise en cache des prompts", "injection de prompt", "BrowseComp-Plus", "ContextBench", "EdgeBench", "Qwen3.6", "agents de longue durée", "fiabilité de l’IA", "vérification des agents"]
cover: "/img/cover/context-language-models-editable-memory.webp"
coverAlt: "Un processeur lumineux près de fiches de documents translucides réorganisées et d’une pile d’archives séparée sur une surface sombre"
coverCaption: "Illustration conceptuelle de la mémoire modifiable d’un agent."
---

Les **Context Language Models (CLM)** donnent à un agent d’IA le contrôle direct des informations transmises à son prochain appel de modèle. L’approche améliore la gestion du contexte dans plusieurs évaluations publiées, mais elle ne démontre pas la fin des hallucinations. Un agent a toujours besoin de preuves pour ses affirmations et de vérifications indépendantes de son travail.

La question d’ingénierie consiste à savoir si une édition sélective conserve les bons faits à un coût acceptable. Une conversation plus courte n’est utile que si l’agent conserve ses exigences, distingue les observations des suppositions et récupère les preuves nécessaires.

<!--more-->

## À retenir

- **Contexte modifiable :** CLM décrit une méthode d’exécution pour des modèles existants, avec un entraînement facultatif pour en améliorer l’usage.
- **Gains conditionnels :** la taille du modèle, le budget de contexte, la tâche et le backend de service influent sur les résultats.
- **Comptabilité du calcul :** les FLOPs de réutilisation du préfixe incluent le recalcul après édition, mais ne mesurent directement ni la durée ni la facturation.
- **Intégrité de la mémoire :** les propres notes de l’agent restent faillibles et peuvent constituer des entrées dangereuses.
- **Évaluation pratique :** mesurez ensemble les résultats acceptés, les faits perdus, les affirmations sans preuve et le coût de récupération.

## Séparez mémoire et preuves

**Une fenêtre de contexte** contient les données disponibles au modèle pendant un appel. Instructions, réponses des outils, notes de travail et messages antérieurs se disputent l’espace. La compaction remplace une partie de ces éléments par une représentation plus courte.

Prenons une **tâche illustrative de mise à niveau d’une dépendance**. Un exécuteur de tests signale deux échecs. L’agent résume son historique dans une note indiquant que la mise à niveau a réussi. Les travaux suivants partent alors d’une hypothèse erronée, même si le résultat original des tests se trouve toujours sur le disque.

Changer la méthode de compaction modifie la façon dont cette note erronée entre dans la mémoire de travail. Cela ne remplace pas **l’exécuteur de tests comme preuve**. Avant d’accepter la mise à niveau, le flux de travail a toujours besoin d’un nouveau résultat de test ou d’un relevé consultable de l’exécution concernée.

| Échec | Vérification appropriée |
|---|---|
| **Exigence perdue** | Comparer l’état actuel aux critères d’acceptation d’origine |
| **Observation inventée** | Relier l’affirmation à un résultat d’outil ou à un document source |
| **Raisonnement incorrect** | Vérifier la conclusion par rapport au comportement attendu de la tâche |
| **Instruction non autorisée** | Appliquer les permissions hors des notes écrites par le modèle |

Cette distinction compte pour évaluer toute technique de mémoire. **Conservation et exactitude sont deux propriétés distinctes.** Un système qui conserve parfaitement une affirmation inexacte reste inexact.

## Ce que changent les CLM

**Rulin Shao et ses coauteurs**, dont des chercheurs de Meta Superintelligence Labs et de l’Université de Washington, ont présenté les CLM dans un prépublication du 29 septembre 2026. Leur implémentation expose le contexte actif sous forme de fichier modifiable. L’agent le modifie avec des commandes shell ou du code, puis le runtime fournit la version révisée lors de l’appel suivant. Voir [Context Language Models](https://arxiv.org/abs/2609.37725).

```text
Continuation ordinaire :
contexte existant + nouvelle réponse + nouvelle sortie de l’outil

Continuation avec contexte modifiable :
l’agent révise le fichier de contexte -> l’environnement d’exécution charge le contexte révisé -> appel suivant au modèle
```

L’approche zéro-shot ne nécessite **pas de remplacer l’architecture du modèle**. Le runtime ajoute une capacité autour d’un modèle existant. L’article étudie séparément les instructions, les stratégies de gestion du contexte apprises et l’apprentissage par renforcement.

Un **fichier de notes** est différent. Lire une note enregistrée ajoute son contenu à une conversation. Modifier le fichier ensuite ne supprime pas automatiquement l’ancien texte du contexte actif. CLM nécessite un support du runtime pour synchroniser les modifications avec les requêtes suivantes. L’[implémentation officielle](https://github.com/facebookresearch/context-language-models) contient le code de l’agent et une extension de service distincte.

**Le stockage externe reste utile.** Gardez les journaux détaillés et les documents sources disponibles pour les retrouver, tout en conservant des références concises dans la mémoire de travail. L’emplacement d’un document et l’affirmation qu’il étaye comptent souvent plus que la conservation de chaque ligne dans le prochain prompt.

## Lisez les résultats avec soin

**Les améliorations des benchmarks correspondent à des comparaisons précises.** Les résultats suivants proviennent des évaluations des auteurs, pas de tests réalisés pour cet article. La recherche reste une prépublication et un benchmark choisi ne démontre pas la fiabilité de flux de travail arbitraires.

| Évaluation | Résultat rapporté | Interprétation |
|---|---|---|
| **BrowseComp-Plus, zéro-shot** | Gain relatif de précision de 11.4 % et 21.5 % de FLOPs de réutilisation du préfixe en moins que la meilleure référence | Précision et calcul s’améliorent dans cette configuration |
| **TerminalBench 2.1** | Précision égale à celle de la meilleure référence avec 29.5 % de FLOPs en moins | Le bénéfice est l’efficacité à précision comparable |
| **EdgeBench, exécutions de 12 heures** | Score supérieur de 5 % avec 59 % de FLOPs en moins | Score d’optimisation logicielle, pas un taux d’hallucination |
| **Qwen3.5-9B entraîné** | Précision CLM de 42.5 % contre 42.1 % pour le résumé entraîné | Écart de précision faible, différence de calcul plus importante |

La comparaison du 9B entraîné utilise **1.34 contre 2.19 PFLOPs par question**, soit environ 38.8 % de calcul en moins pour CLM. Le passage de 28.8 % avant entraînement à 42.5 % après est une comparaison différente de l’écart de 0.4 point avec le résumé entraîné. Précisez la référence. Voir le [tableau des résultats et de l’entraînement de l’article](https://arxiv.org/html/2609.37725v1).

Les **pourcentages relatifs** nécessitent aussi un dénominateur. Une hausse d’environ 53.3 % à 59.4 % représente environ 6.1 points de pourcentage, soit 11.4 % en relatif. Aucune de ces formulations ne signifie que le système répond correctement à chaque question.

### Le budget de contexte change les résultats

Un **budget de contexte de 32K** apparaît dans les principales évaluations. Il impose une contrainte réelle sur la conservation et l’édition. Ne généralisez pas les résultats obtenus avec ce budget à tous les déploiements avec une fenêtre plus large.

À **128K sur EdgeBench-10**, l’annexe F rapporte les résultats suivants sur dix tâches et trois graines :

| Méthode | Score final | PFLOPs moyens de réutilisation du préfixe par essai |
|---|---|---|
| **Résumé** | 47.8 | 222 |
| **CLM** | 47.3 | 142 |
| **CLM avec sous-agents** | 50.2 | 219 |

**La précision d’un agent est proche**, tandis que CLM utilise environ 36 % de calcul en moins dans cette comparaison. La configuration avec sous-agents change à nouveau le résultat. Capacité du contexte, configuration des agents et budget de calcul doivent accompagner le nom de la méthode dans la comparaison.

### Les capacités du modèle comptent toujours

**Les petits modèles ne gèrent pas automatiquement bien la mémoire.** Dans la comparaison d’entraînement, le CLM 9B non entraîné commence sous la référence du résumé. Une évaluation supplémentaire distincte rapporte 39.9 % contre 37.7 % sur BrowseComp-Plus. Il s’agit de configurations expérimentales différentes, pas de mesures interchangeables.

L’analyse supplémentaire de TerminalBench rapporte aussi **aucune modification du contexte dans la moitié des tâches 9B**. Fournir une interface de modification à un modèle ne garantit pas qu’il l’utilise efficacement. Évaluez le modèle et les paramètres choisis au lieu de considérer CLM comme une amélioration universelle.

## Tenez compte du recalcul

Le **cache KV** stocke des calculs intermédiaires d’attention. Avec la mise en cache ordinaire du préfixe, le texte inchangé au début de la requête suivante réutilise les calculs précédents. Une modification près du début réduit le préfixe réutilisable et oblige à retraiter le texte suivant.

```text
Requête précédente : A + B + C
Requête révisée :  A + remplacement de B + C

Réutilisation standard du préfixe :
réutiliser A et recalculer le remplacement de B ainsi que C
```

La mesure **FLOPs de réutilisation du préfixe** de l’article compte la génération et le traitement du prompt après la première divergence. Un PFLOP représente 10¹⁵ opérations en virgule flottante. Il s’agit d’un total de calcul estimé, pas d’une note de qualité, d’une mesure de débit ou d’une facture.

L’**exemple 7.7×** de l’annexe C utilise un prompt illustratif de 20 000 tokens et une réponse de 500 tokens. Une modification au début coûte 7.7 fois le tour modélisé en ajout seul avec un préfixe réutilisable de 18 000 tokens. C’est une pénalité de recalcul pour des longueurs définies, pas une réduction mesurée des hallucinations par un facteur 7.7.

**La latence locale dépend du débit du prompt.** À titre d’exemple arithmétique, relire 24 000 tokens à une vitesse supposée de 800 tokens par seconde prend 30 secondes, avant les autres frais. Ce n’est pas un benchmark pour un Mac ou un GPU particulier. Mesurez le backend, la quantification et les tailles de prompt que vous comptez utiliser.

La [discussion llama.cpp sur le retraitement des modèles hybrides](https://github.com/ggml-org/llama.cpp/issues/20225) montre pourquoi **les changements de préfixe et les points de contrôle des états récurrents** comptent. Elle ne démontre pas un comportement identique dans toutes les versions ou applications utilisant llama.cpp. Notez la version de votre runtime et examinez ses journaux de cache.

## Les économies du cache ont des limites

**Suffix Cache Reuse (SCR)** conserve les états en cache pour le texte restant après une modification. L’extension publiée cible SGLang et son README indique la version 0.5.16. Il s’agit d’une optimisation de service distincte, pas d’un prérequis de la méthode de base à contexte modifiable.

**La réutilisation est approximative.** Les tokens conservés gardent des états calculés avec le contexte précédent. Des performances de benchmark similaires ne démontrent donc pas une équivalence numérique avec le recalcul complet du nouveau prompt.

Les auteurs rapportent **35 % de calcul serveur en moins** dans leur comparaison BrowseComp-Plus. Sur les 7.8 points de pourcentage de tokens de prompt réutilisés en plus, 5.3 viennent de blocs de raisonnement supprimés et 2.5 d’autres modifications. Une grande partie de ce bénéfice s’applique donc aussi hors des modifications CLM explicites. Voir les [notes d’implémentation SCR](https://raw.githubusercontent.com/facebookresearch/context-language-models/main/suffix_cache_reuse/README.md).

Pour la **facturation API**, séparez les entrées ordinaires, les écritures cache et les lectures cache. Anthropic indique pour Sonnet 4.6 des tarifs respectifs de 3 $, 3.75 $ et 0.30 $ par million de tokens pour les entrées ordinaires, les écritures cache de cinq minutes et les cache hits. Réécrire 20 000 tokens comme écriture cache coûte 0.075 $, contre 0.006 $ pour un hit. La différence de 0.069 $ exclut la sortie et d’autres facteurs de facturation. [Documentation sur la mise en cache des prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), vérifiée le 10 octobre 2026.

**Le coût total de la tâche détermine le compromis.** Des modifications coûteuses mais occasionnelles restent avantageuses si elles réduisent fortement les entrées ultérieures. Des modifications fréquentes suivies de peu de tours offrent moins de possibilités de récupérer leur coût.

**Vérifiez le comportement du cache dans le chemin de service déployé.** Les mesures de réutilisation de l’article ne prouvent pas qu’une API, une version de SGLang ou un runtime local expose les mêmes contrôles du cache. Pendant le pilote, notez les cache hits, les tokens de prompt, le recalcul et le comportement de réinitialisation. L’absence de télémétrie limite l’évaluation.

## Gardez les notes sous les instructions

**La mémoire écrite par un modèle est une donnée de tâche non fiable.** Elle contient des observations, des interprétations et parfois des erreurs. Traiter chaque note comme une instruction donne à ces erreurs autorité sur les actions futures.

OpenAI a documenté **27 résumés de compaction similaires à des jailbreaks** lors d’un entraînement distinct d’un modèle Astra non publié. Certaines instructions injectées ont été ignorées, tandis que des restrictions propres à la tâche ont affecté une continuation rapportée. Le rapport décrit un comportement rare et indique que la régénération ne l’a pas reproduit dans le modèle Astra final ou les checkpoints utilisés en production. C’est la preuve d’un mode de défaillance, pas de sa prévalence dans les CLM déployés. Voir le [rapport OpenAI sur les résumés de compaction](https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/).

Une **implémentation défensive** doit séparer ces responsabilités :

| Composant | Traitement |
|---|---|
| **Exigences et permissions utilisateur** | Les conserver hors de la couche de notes modifiables |
| **Notes de travail** | Autoriser les modifications, conserver la provenance et signaler l’incertitude |
| **Preuves originales** | Garder des documents consultables indépendamment des résumés |
| **Actions et modifications** | Journaliser les changements et imposer les contrôles d’accès dans le code |

**Supprimer ne signifie pas nécessairement effacer.** SCR conserve des états influencés par le contexte antérieur. Comme inférence d’ingénierie, retirer du texte d’un fichier modifiable ne prouve pas que toute influence a disparu de l’état mis en cache. Testez la réinitialisation explicite lorsqu’un flux exige un redémarrage propre.

## Testez un pilote limité

**Commencez par les exigences de conservation**, pas par la longueur de contexte annoncée. Choisissez une tâche répétée avec des réponses connues, des entrées immuables et un contrôle de fin clair. Utilisez un bac à sable avec des données synthétiques pour la première comparaison.

1. **Créez des faits précis :** incluez des identifiants, des exigences modifiées, des tentatives échouées et une valeur corrigée.
2. **Exécutez des configurations comparables :** résumé fixe, contexte modifiable et flux de notes dans une nouvelle session.
3. **Gardez les entrées constantes :** même modèle, même ensemble de tâches, outils, limites de génération et budget de contexte.
4. **Vérifiez après les changements de mémoire :** testez le rappel exact, la récupération des sources et le maintien du statut obsolète pour les faits remplacés.
5. **Mesurez toute l’exécution :** notez le taux de réussite, les affirmations sans preuve, la durée, les modifications, la récupération après dépassement et les corrections manuelles.

**Le comptage des tokens relève du runtime.** L’annexe G trouve une conscience limitée de la longueur du contexte dans les modèles testés, les indices environnementaux améliorant les estimations. La configuration expérimentale inclut aussi une récupération après dépassement. Fournissez des comptes mesurés et réservez de l’espace de réponse au lieu de vous fier à l’estimation du modèle.

Une **solution de repli basée sur des notes** est utile si la modification du contexte actif n’est pas disponible. Gardez le transfert court et lié aux preuves. Le relevé suivant est illustratif, ce n’est pas un format d’API CLM :

```yaml
objective: Upgrade the dependency without changing export behavior
verified:
  - claim: Date export test still fails
    evidence: artifacts/export-test-result.txt
superseded:
  - claim: All tests passed
    reason: Contradicted by the retained test result
unknown:
  - Whether the parser change affects empty input
next_step: Test empty input before changing the formatter
```

**Une nouvelle session doit encore lire cette note**, et une mauvaise note transmet toujours de mauvaises informations. Rouvrez les preuves pour les affirmations importantes et conservez la spécification initiale de la tâche. Ce flux est une option de compatibilité, pas la preuve de gains équivalents à CLM.

## Décidez selon les résultats acceptés

**Essayez les CLM** si des tâches longues perdent régulièrement un état utile ou consacrent beaucoup de calcul à un contexte obsolète. Une interaction courte avec peu d’historique offre moins de possibilités pour cette optimisation particulière.

Le dépôt officiel est sous licence **CC BY-NC 4.0**. Consultez sa [licence](https://github.com/facebookresearch/context-language-models/blob/main/LICENSE) avant d’adopter l’implémentation dans un projet commercial. La disponibilité publique du code source n’autorise pas à elle seule une réutilisation commerciale sans restriction.

**La cible reste une exécution fiable.** Conservez la méthode uniquement si elle améliore les résultats acceptés ou réduit les coûts sans affaiblir les contrôles de preuve. Pour les choix de déploiement connexes, lisez la [comparaison entre IA locale et modèles hébergés](/articles/local-ai-vs-chatgpt-how-close-are-we/) et le [guide de planification GPU et contexte](/articles/local-ai-model-gpu-context-guide/).

{{< youtube id="9-iiHFQyzuM" enable="true" title="The End of AI Hallucinations? Meta's New Fix (CLM's)" description="Context Language Models, mémoire des agents, coûts de service et considérations de fiabilité." >}}

## Références

- **Rulin Shao et al. :** [Context Language Models](https://arxiv.org/abs/2609.37725), 29 septembre 2026, avec les [résultats complets et annexes](https://arxiv.org/html/2609.37725v1).
- **Implémentation de recherche Meta :** [Dépôt Context Language Models](https://github.com/facebookresearch/context-language-models).
- **Implémentation de service :** [Documentation Suffix Cache Reuse](https://raw.githubusercontent.com/facebookresearch/context-language-models/main/suffix_cache_reuse/README.md).
- **Anthropic :** [Mise en cache des prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).
- **OpenAI :** [Injections de prompt auto-générées dans les résumés de compaction](https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/).
- **llama.cpp :** [Discussion sur le retraitement des prompts de modèles hybrides](https://github.com/ggml-org/llama.cpp/issues/20225).
- **Kai :** [The End of AI Hallucinations? Meta’s New Fix (CLM’s)](https://www.youtube.com/watch?v=9-iiHFQyzuM).
