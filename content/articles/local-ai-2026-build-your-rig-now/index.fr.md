---
title: "IA locale en 2026 : un modèle 27B dépasse Sonnet 4.6 alors que la fenêtre matérielle se referme"
date: 2026-09-22
lastmod: 2026-11-15
toc: true
draft: false
description: "Planifiez une configuration d’IA locale pour 2026 selon la taille du modèle, la VRAM, la bande passante mémoire, la puissance, le coût et les possibilités d’évolution."
genre: ["IA locale", "IA auto-hébergée", "Modèles à poids ouverts", "Matériel IA", "Apprentissage automatique", "Quantification", "Laboratoire à domicile", "Confidentialité", "Économie de l’IA", "Matériel grand public"]
tags: ["ia locale", "exécuter un llm en local", "qwen3.8", "qwen3.8 27b", "bonsai 2 27b", "ternary bonsai", "prism ml", "quantification ternaire", "quantification 1,58 bit", "quantification llm", "claude sonnet 4.6", "sonnet 4.6 face à un modèle local", "poids ouverts", "modèle moe", "mélange d’experts", "ollama", "llama.cpp", "rtx 5090", "vram", "inférence locale", "prix gpu 2026", "pénurie de dram", "prix de la mémoire", "assembler un pc pour l’ia", "ia pour laboratoire à domicile", "coût d’abonnement ia", "openrouter", "artificial analysis", "guide d’achat gpu", "llm auto-hébergé", "ia respectueuse de la vie privée", "matériel ia 2026"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Un espace de travail high-tech avec une carte graphique et plusieurs écrans lumineux affichant des résultats d’évaluation et des visualisations d’IA, sur fond bleu marine."
coverCaption: ""
ref: ["/articles/ai-models-raspberry-pi-4-5", "/articles/building-a-privacy-preserving-meshtastic-ai-assistant"]
---

**Un modèle téléchargeable qui tient sur une seule carte graphique grand public dépasse maintenant un modèle API de pointe dans l’indice global d’intelligence.** Qwen3.8 27B est un modèle vision-langage à poids ouverts, publié en août 2026. Sa version reconditionnée en ternaire, Bonsai 2 27B, réduit les mêmes poids à 5.53 GiB. Ensemble, ces modèles marquent le moment où l’inférence locale a cessé d’être un compromis de passionnés pour devenir une véritable option face aux API payantes.

*La fenêtre pour acheter du matériel se referme vite. La mémoire coûte plus cher qu’à aucun moment depuis vingt ans, et ces prix entraînent aussi ceux des cartes graphiques.*

Cet article présente les résultats des évaluations, les deux modèles et leurs différences, les domaines où le modèle ouvert reste en retrait, et les raisons pour lesquelles les douze prochains mois ne sont pas le bon moment pour attendre.

**Ce que vous en retirerez :** choisissez un modèle et une capacité mémoire adaptés à votre charge de travail. Avant d’acheter, comparez le coût du matériel, l’électricité, la longueur du contexte et le débit mesuré. Une comparaison des évaluations ne prédit ni la qualité du résultat sur vos tâches ni le futur prix de votre GPU.

## En bref

**L’écart d’intelligence entre un modèle local 27B et une API payante proche des modèles de pointe a disparu. Les avantages restants du modèle payant sont plus faibles que ne le laisse penser la différence de prix.**

Trois évolutions se sont produites en même temps :

- **Les modèles ouverts 27B ont atteint des scores proches des modèles de pointe.** Qwen3.8 27B obtient 33.7 à l’Intelligence Index contre 30.1 pour Sonnet 4.6, sur la même série d’évaluations.
- **La quantification ternaire réduit les besoins mémoire d’environ deux tiers.** Bonsai 2 27B exécute le modèle 27B complet en **5.53 GiB**, une capacité disponible sur des cartes à quelques centaines de dollars.
- **L’offre mémoire s’est dégradée.** Au début de 2026, les prix contractuels de la DRAM conventionnelle ont augmenté de **90 à 95 %** d’un trimestre à l’autre. TrendForce n’avait jamais relevé de hausse trimestrielle plus forte, et les GPU de nouvelle génération ont été repoussés à 2028.

*Acheter ou assembler maintenant coûte moins cher. Ce n’est pas un argument commercial, mais une conclusion tirée des données d’approvisionnement.*

## Voir la démonstration avec une carte graphique

Cette affirmation mérite une démonstration plutôt qu’un tableau. Bijan Bowen a testé Bonsai 2 27B sur une machine équipée d’une seule carte graphique pour savoir s’il s’agit aujourd’hui du meilleur modèle pour une seule carte.

{{< youtube id="OA5cICIzD-c" enable="true" title="Premier test de Bonsai 2 27B : est-ce le MEILLEUR modèle d’IA pour une seule carte graphique ?" description="Première évaluation du modèle ternaire Bonsai 2 27B sur une seule carte graphique grand public, avec un examen de la vitesse, de la qualité et des solutions de rechange." >}}

*Regardez la qualité du résultat plutôt que le nombre de jetons par seconde. La vitesse est le problème le plus simple à résoudre.*

## Deux noms, un seul modèle

Les deux modèles présentés ici ne sont pas concurrents. **Ce sont les mêmes poids avec deux niveaux de précision différents.**

| | Qwen3.8 27B | Bonsai 2 27B ternaire |
|---|---|---|
| **Description** | Modèle Qwen d’origine à poids ouverts | Reconditionnement ternaire de Qwen3.8-27B par Prism ML |
| **Poids sur le disque** | **18 GB** | **5.53 GiB** (PTQ1_0) ou **6.70 GiB** (PQ2_0) |
| **Paramètres** | 27B dense | 26.90B, même architecture |
| **Contexte** | 256K | 262,144 jetons |
| **Vision** | Oui, native | Oui, projecteur CLIP fourni séparément |
| **Appels d’outils** | Oui | Oui |
| **Licence** | Apache 2.0 | Apache 2.0 |
| **Environnement d’exécution** | Ollama, llama.cpp, MLX | **Fork llama.cpp de Prism ML uniquement** |

La page de la bibliothèque Ollama consacrée à `qwen3.8` indique que le modèle 27B occupe **18 GB**, prend en charge un contexte de 256K, la vision et les appels d’outils, et propose une version MLX distincte pour Apple Silicon. La version ternaire d’Ollama est un miroir des paquets GGUF Apache-2.0 de Prism ML, republiés avec les mêmes sommes de contrôle.

**La question pratique n’est donc pas de savoir quel modèle choisir.** Elle consiste à décider quelle quantité de mémoire consacrer à une intelligence identique. La version ternaire utilise environ un tiers de la mémoire et perd peu en échange.

{{< figure src="local-ai-architecture-comparison.webp" alt="Schéma comparant l’empreinte mémoire du même modèle 27B : 18 GB en précision standard contre 5.53 GiB avec des poids ternaires, les deux tenant sur une GPU grand public" >}}

## Comparaison des évaluations

Artificial Analysis évalue les deux modèles sur la même série de tests. Lisez les résultats ligne par ligne plutôt que de les résumer, car chaque modèle se distingue dans des domaines différents.

| Mesure | Qwen3.8 27B | Claude Sonnet 4.6 | En tête |
|---|---|---|---|
| **Intelligence Index** | **33.7** | 30.1 | Ouvert |
| **Coding Index** | **68.1** | 63.0 | Ouvert |
| **Agentic Index** | **45.8** | 31.8 | Ouvert |
| **GPQA Diamond** | **90.5%** | 87.5% | Ouvert |
| **Humanity's Last Exam** | **33.9%** | 33.6% | Ouvert |
| **AA-LCR (contexte long)** | **82.0%** | 80.0% | Ouvert |
| **GDPval-AA** | **45.4%** | 36.0% | Ouvert |
| **CritPt (physique de recherche)** | **5.4%** | 3.1% | Ouvert |
| **Taux de réponses sans hallucination** | **69.7%** | 51.6% | Ouvert |
| **SciCode** | 46.6% | **50.1%** | Sonnet |
| **Précision AA-Omniscience** | 15.6% | **40.9%** | Sonnet |

*Le modèle ouvert arrive en tête dans neuf des onze résultats comparables, y compris tous les indices globaux.*

### Les points forts du modèle ouvert

Les trois indices globaux résument le résultat. **Intelligence : 33.7 contre 30.1, Coding : 68.1 contre 63.0, Agentic : 45.8 contre 31.8.** L’écart est le plus grand sur l’indice agentique. Il importe surtout pour les personnes qui lancent des processus automatisés en plusieurs étapes plutôt que des requêtes isolées.

Pour situer les résultats en percentile, Artificial Analysis place Qwen3.8 27B **au-dessus de 86 % des modèles sur l’indice agentique** et de 76 % sur l’indice de programmation. Sonnet 4.6 atteint respectivement 68 % et 72 %. En raisonnement scientifique de niveau universitaire avancé, le modèle ouvert obtient **90.5 %** sur GPQA Diamond.

### Les domaines où Sonnet 4.6 reste devant

Deux résultats s’inversent. Aucun n’est secondaire.

**AA-Omniscience mesure si un modèle répond correctement du premier coup aux questions de connaissances. Sonnet 4.6 obtient 40.9 % contre 15.6 %.** L’écart de fiabilité factuelle est important et constitue le meilleur argument individuel pour payer un modèle haut de gamme.

Le taux de réponses sans hallucination doit être interprété avec prudence. Les 69.7 % de Qwen contre 51.6 % pour Sonnet semblent montrer une victoire nette, ce qui est vrai si on les regarde seuls. Mais cette mesure représente la part des réponses *incorrectes* qui n’inventent pas d’informations. Un modèle moins précis produit plus de réponses incorrectes. Les deux pourcentages décrivent donc des populations différentes et ne sont pas directement comparables. **Commencez par la ligne de précision.**

Sonnet atteint aussi 50.1 % sur SciCode contre 46.6 %, et indique des résultats sur deux évaluations absentes de la fiche du modèle ouvert : IFBench et Terminal-Bench Hard. Il est impossible de les comparer.

### Deux réserves à garder en tête

**Les dates de sortie sont séparées de six mois.** Sonnet 4.6 est sorti en février 2026. Qwen3.8 27B est sorti en août 2026. Comparer un modèle de pointe de février à un modèle ouvert d’août ne constitue pas un test à armes égales.

**Sonnet 4.6 n’est plus le modèle le plus avancé d’Anthropic.** Sonnet 5 et Opus 5 le dépassent désormais dans la gamme. Le modèle ouvert 27B a rattrapé un modèle phare du milieu de l’année 2026, pas le modèle le plus avancé actuel. Affirmer le contraire serait tirer trop de conclusions du tableau.

*Les évaluations mesurent des performances dans des conditions normalisées. Seul compte le résultat obtenu sur votre propre charge de travail.*

## Ce que changent les poids ternaires

Bonsai 2 n’est pas un modèle plus petit. C’est le même modèle à 26.90B paramètres, avec une précision numérique bien plus faible. Les métadonnées GGUF publiées rendent ce compromis explicite.

| Propriété | Valeur |
|---|---|
| **Architecture** | `qwen35`, attention hybride avec attention complète toutes les quatre couches et couches state-space |
| **Paramètres** | 26.90B |
| **Blocs** | 64 |
| **Largeur des embeddings** | 5120 |
| **Attention** | 24 têtes de requête, 4 têtes KV, longueur clé/valeur de 256 |
| **Contexte** | 262,144 jetons, base RoPE 1e7 |
| **Format des poids** | Ternaire, groupe de 128. PQ2_0 à 2.13 bits par poids, PTQ1_0 à 1.75 |
| **Tour de vision** | CLIP, 460.73M paramètres, fourni dans un paquet projecteur séparé |
| **Licence** | Apache 2.0 |

**Avec des poids ternaires, chaque paramètre prend l’une de trois valeurs au lieu de seize.** C’est tout l’intérêt de la compression, qui permet au modèle 27B complet de tenir dans 5.53 GiB au lieu de 18 GB.

### Débit mesuré

Mesure avec `llama-bench` sur une RTX 5090 de 32 GB, toutes les couches transférées sur la GPU, flash attention activée, moyenne de trois exécutions :

| Paquet | Poids | Préremplissage (pp512) | Décodage (tg128) |
|---|---|---|---|
| **PQ2_0** | 6.70 GiB | **3802.74 tok/s** | **135.41 tok/s** |
| **PTQ1_0** | 5.53 GiB | 1876.31 tok/s | 131.41 tok/s |

PQ2_0 effectue le préremplissage **2.03 fois plus vite** que PTQ1_0, tandis que leurs vitesses de décodage sont statistiquement équivalentes. PQ2_0 constitue donc le choix standard le plus raisonnable. PTQ1_0 convient lorsque les derniers 1.2 GiB comptent. Avec `llama-server` et un contexte de 65K, le décodage a conservé **136.5 tok/s** sur une seule requête en flux continu.

**La vitesse de décodage se ressent au quotidien.** 135 jetons générés en une seconde dépassent largement la vitesse de lecture. La latence n’est pas une raison de choisir l’inférence locale, car une API hébergée est suffisamment rapide. Les raisons sont le coût, la confidentialité et le contrôle.

### Le piège dont personne ne parle

**La version standard d’Ollama ne peut pas charger ces fichiers.** Les noyaux ternaires se trouvent dans le fork llama.cpp de Prism ML. Testé avec Ollama 0.34.2, le chargement échoue avec `unsupported tensor "output.weight" size overflows`. L’environnement reconnaît l’architecture `qwen35`, mais ses bibliothèques ne contiennent ni `pq2_0` ni `ptq1_0` et n’ont pas de moteur d’activation Hadamard.

Voici un autre piège à connaître avant d’y passer une soirée. **Le paquet F16 de cette famille ressemble à une solution de repli sûre, mais ne l’est pas.** Ses tenseurs sont en F16 et F32 standard. Le fichier est donc analysé et chargé sans erreur, puis produit du texte incohérent. Les poids se trouvent dans une base tournée, déclarée dans les métadonnées `prism.hadamard.*`. L’environnement doit appliquer la rotation correspondante, sinon il produit n’importe quoi. Avec 50.1 GiB, le paquet F16 ne tient de toute façon pas entièrement sur une carte de 32 GB.

*Lisez la fiche du modèle avant le téléchargement. Un miroir communautaire n’est pas une version prise en charge, et la page le dit clairement.*

## La vague MoE qui se prépare

Les modèles denses 27B ne représentent que la moitié du sujet. Les modèles mélange d’experts activent une petite partie de leurs paramètres par jeton, ce qui change encore le coût.

| Modèle | Total / actifs | Contexte | Remarque |
|---|---|---|---|
| **Qwen3.8 2.4T A95B** | 2.4T / 95B | 1.0M | Modèle à poids ouverts de la famille de Qwen3.8 Max |
| **Qwen3.6 35B A3B** | 35B / 3B | 262K | Apache 2.0, MoE hybride et clairsemé |
| **Qwen3 Coder Next** | 80B / 3B | 256K | Poids ouverts, conçu pour les agents de programmation toujours actifs |

**Qwen3 Coder Next est le modèle local à surveiller.** Il compte 80B paramètres au total, mais n’en active que 3B par jeton. Il est conçu pour des agents permanents dans des environnements CLI et IDE. Un modèle qui active 3B paramètres génère à la vitesse d’un modèle 3B tout en puisant dans les capacités stockées dans 80B paramètres. Les notes du projet indiquent des résultats comparables à ceux de modèles qui utilisent 10 à 20 fois plus de calcul actif.

*Le modèle dense 27B est le choix sûr aujourd’hui. La courbe d’efficacité des modèles clairsemés continue de progresser.*

{{< figure src="local-ai-moe-dense-tradeoff.webp" alt="Graphique comparant un modèle dense 27B qui active tous ses paramètres par jeton à un modèle mélange d’experts clairsemé qui n’en active que 3 milliards sur 80 milliards" >}}

## La fenêtre matérielle se referme

Cette partie de l’histoire a une échéance.

L’inférence locale est devenue abordable juste au moment où la mémoire dont elle dépend s’est renchérie. Ces deux tendances convergent, et l’effet apparaît déjà dans les prix de vente.

### L’évolution du prix de la mémoire

**Les prix contractuels de la DRAM conventionnelle ont augmenté de 90 à 95 % au premier trimestre 2026 par rapport au trimestre précédent.** C’est la plus forte progression trimestrielle enregistrée par TrendForce. La mémoire flash NAND a augmenté de 55 à 60 % pendant la même période.

La pression n’a pas diminué. Selon les données de TrendForce, la DRAM a encore augmenté de **58 à 63 %** au deuxième trimestre et la NAND de 70 à 75 %. Même le ralentissement du troisième trimestre, avec une hausse de 13 à 18 % pour la DRAM et de 10 à 15 % pour la NAND, s’ajoute à deux trimestres record. Ce n’est pas un répit.

La cause est structurelle, pas cyclique. Les centres de données IA absorbent des capacités mémoire qui servaient auparavant aux téléphones, ordinateurs portables et consoles. Les fabricants de mémoire servent d’abord les commandes à plus forte marge. Les analystes qui suivent l’offre de modules prévoient une baisse de plus de 70 % de l’approvisionnement en puces DRAM des fabricants de modules en 2027.

**Le directeur général d’Intel a donné un chiffre.** Lors de l’AI Infrastructure Summit à Santa Clara, le 15 septembre 2026, Lip-Bu Tan a déclaré que le prix de la mémoire avait déjà été multiplié par « cinq, six et sept ». Il a averti que la mémoire représentait maintenant 70 à 80 % du coût des composants d’un ordinateur portable d’entrée de gamme. Il a également déclaré qu’il n’y aurait pas de répit avant 2028.

*Les articles indépendants comparant le prix par surface des wafers DRAM à celui des wafers logiques avancés comportent une réserve importante. Les prix au comptant ne sont pas les prix contractuels et le marché au comptant de la DDR5 est trop réduit pour que la comparaison soit concluante. La tendance générale ne fait aucun doute.*

{{< figure src="local-ai-memory-price-trend-2026.webp" alt="Graphique des hausses trimestrielles des contrats DRAM en 2026 : bond de 90 à 95 % au premier trimestre, ralentissant à 13 à 18 % au troisième" >}}

### L’effet sur les cartes graphiques

La mémoire représente une part importante du coût de fabrication d’une carte graphique. Les prix de la DRAM se répercutent donc directement sur ceux des GPU.

| Carte | Début 2025 | Septembre 2026 |
|---|---|---|
| **Nvidia RTX 5090** | $1,999 | **plus de $5,000** |
| **Asus RTX 5080** | $1,199 | $1,595 |
| **AMD RX 9070 XT** | environ $830 | **plus de $1,037** |

Ces hausses sont arrivées par vagues coordonnées en 2026, pas sous forme de pics isolés. Nvidia a augmenté ses prix en janvier, de nouveau en mai pour la RTX 5090, puis encore plus tard dans l’année. AMD a suivi en août avec une hausse d’au moins 10 % sur certaines cartes Radeon et certains kits de mémoire GDDR6, directement attribuée au coût de la mémoire.

**La génération suivante a été reportée au lieu d’être commercialisée.** La série RTX 60 de Nvidia est maintenant attendue en 2028, sans lancement en 2027. La disponibilité de la mémoire est citée comme cause.

*La carte que vous achetez aujourd’hui n’est pas en concurrence avec une carte moins chère l’an prochain. Elle est en concurrence avec une version plus chère d’elle-même.*

## Pourquoi attendre coûte plus cher

Le conseil habituel pour le matériel consiste à attendre la prochaine génération. Sur un marché où la mémoire est limitée, ce conseil joue contre vous.

Trois éléments l’expliquent.

**Les prix ont déjà monté et continuent de grimper.** Une hausse de 90 à 95 % des contrats DRAM en un trimestre n’est pas une anomalie qui s’inversera au trimestre suivant. TrendForce prévoit une nouvelle hausse au troisième trimestre, pas une baisse, et le directeur général d’Intel parle de 2028 pour un retour à la normale.

**Il n’y aura aucun produit 2027 à attendre.** Si les GPU grand public de nouvelle génération ne sortent qu’en 2028, l’attente dure deux ans. Une grande partie du cycle de renouvellement du matériel se passe ainsi sans rien faire.

**Les modèles sont déjà assez bons.** C’est ce qui a changé en 2026. Il y a deux ans, le matériel local offrait une expérience nettement inférieure. Aujourd’hui, le même budget permet d’exécuter un modèle 27B à 135 jetons par seconde, avec un contexte 262K, qui dépasse une API haut de gamme dans l’indice global d’intelligence.

*Si vous attendiez que les modèles locaux deviennent assez bons, vous pouvez arrêter d’attendre. Si vous attendez que le matériel baisse, les données d’approvisionnement indiquent 2028.*

## Quelle configuration assembler

Associer le matériel aux modèles ci-dessus est simple, car les poids ternaires ont réduit la capacité requise.

| Niveau | Mémoire | Ce qu’il exécute confortablement |
|---|---|---|
| **Entrée de gamme** | 8 à 12 GB VRAM | Modèle 27B ternaire de 5.53 à 6.70 GiB avec de la marge pour le contexte |
| **Pratique** | 16 à 24 GB VRAM | Qwen3.8 27B complet de 18 GB ou version ternaire avec contexte long |
| **Confortable** | 32 GB VRAM | Modèle 27B ternaire avec contexte complet 262K, ou MoE 80B avec 3B paramètres actifs |
| **Mémoire unifiée** | 64 à 128 GB | Modèles MoE clairsemés plus grands sur Apple Silicon ou un ordinateur de bureau à mémoire unifiée |

Quelques conseils pratiques comptent plus que ce tableau :

- **Achetez de la mémoire, pas le GPU haut de gamme.** Le paquet ternaire de 5.53 GiB rend l’entrée de gamme réellement utilisable. Utilisez la différence pour la RAM système et le stockage plutôt que pour une carte de luxe au prix de 2026.
- **Les systèmes à mémoire unifiée offrent un bon rapport qualité-prix.** Une machine avec au moins 64 GB de mémoire partagée exécute de plus grands modèles clairsemés pour une fraction du coût d’une carte dédiée équivalente.
- **L’alimentation et le refroidissement comptent.** Un système qui effectue de l’inférence pendant des heures ne se comporte pas comme un système testé quelques minutes.
- **Faites tourner le paquet ternaire avec un modèle plus petit.** Un modèle 3B répond aux questions rapides, tandis que le 27B traite les questions difficiles.

{{< centerbutton href="https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B" >}}
Télécharger Ternary Bonsai 2 27B
{{< /centerbutton >}}

## Quand les modèles haut de gamme justifient encore leur prix

Le niveau haut de gamme a un véritable intérêt, mais plus limité que le marketing ne le laisse entendre.

**La réponse honnête concerne la fiabilité factuelle.** La précision AA-Omniscience atteint 40.9 % pour Sonnet 4.6 contre 15.6 % pour le modèle ouvert 27B. Si une mauvaise réponse coûte un client, entraîne un diagnostic ou compromet une position juridique, un écart de 25 points compte plus que tout indice global.

**La deuxième raison concerne les longues chaînes agentiques.** Sonnet 4.6 obtient 53.0 % sur Terminal-Bench Hard et 75.7 % sur τ²-Bench Telecom, qui mesurent l’utilisation prolongée d’outils et le comportement d’un agent sur plusieurs tours. La fiche du modèle ouvert ne donne pas de résultats comparables. Cette absence n’est pas rassurante.

**La troisième raison est opérationnelle.** Une API hébergée n’exige pas de mises à jour de pilotes, ne présente pas de particularités de quantification, ne dépend pas d’un fork llama.cpp à suivre et ne demande pas de configurer correctement une base de poids tournée. Quelqu’un d’autre gère la disponibilité et reçoit l’alerte à trois heures du matin.

### La question à se poser

Quelle est la place de l’offre haut de gamme hors des entreprises ?

**Elle reste pertinente pour les tâches qui exigent des connaissances fiables.** Recherche, analyse juridique, questions médicales, modélisation financière et toute activité où une réponse fausse mais assurée coûte cher. C’est une catégorie réelle, et l’écart de précision constitue une raison valable de payer.

**Pour la création de contenu, la justification s’amenuise vite.** Rédiger, résumer, refactoriser du code, reformater des données, classer des documents et exécuter des pipelines automatisés sont des tâches où le résultat est vérifié avant d’être accepté. L’écart de précision coûte peu quand une personne ou une suite de tests contrôle d’abord la réponse. Pour ces usages, il est difficile de justifier le paiement au jeton d’un indice de 30.1 alors qu’un indice de 33.7 tourne gratuitement sur du matériel déjà possédé.

**Le choix porte maintenant sur les conséquences, pas sur les capacités.** Il y a deux ans, la question était de savoir si un modèle local pouvait faire le travail. Aujourd’hui, il faut évaluer le coût d’une erreur et la façon de la détecter.

*Le tarif entreprise achète la fiabilité, la conformité et l’astreinte de quelqu’un d’autre. Les autres paient une différence qui n’a plus d’importance dès qu’une suite de tests vérifie le résultat.*

## Points clés

- **Un modèle local 27B dépasse Claude Sonnet 4.6 dans l’indice global d’intelligence**, 33.7 contre 30.1. Il mène aussi en programmation, tâches agentiques, contexte long et raisonnement scientifique avancé.
- **Sonnet 4.6 reste plus précis sur les faits**, 40.9 % contre 15.6 % sur AA-Omniscience. C’est le principal argument restant pour le niveau haut de gamme.
- **La quantification ternaire rend cette configuration pratique.** Bonsai 2 27B exécute le même modèle de 26.90B en 5.53 GiB au lieu de 18 GB. Les deux sont sous licence Apache 2.0.
- **Ollama standard ne peut pas exécuter les paquets ternaires.** Il faut le fork llama.cpp de Prism ML, et la version F16 de secours produit discrètement du texte incohérent au lieu d’échouer.
- **La vitesse de décodage mesurée atteint 135 jetons par seconde** sur une RTX 5090, bien au-delà de la vitesse de lecture.
- **Le prix de la mémoire justifie d’agir maintenant.** Les prix contractuels DRAM ont augmenté de 90 à 95 % en un trimestre en 2026, et les GPU grand public de nouvelle génération ont été reportés à 2028.
- **La RTX 5090 est passée de $1,999 à plus de $5,000 en moins de deux ans**, et toutes les gammes ont suivi.

## Étapes suivantes

1. **Téléchargez le modèle et testez-le avec votre charge de travail** : **[Ternary Bonsai 2 27B sur Ollama](https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B)**
2. **Récupérez les poids d’origine en pleine précision** si vous avez assez de mémoire : **[Qwen3.8 sur Ollama](https://ollama.com/library/qwen3.8)**
3. **Essayez le modèle avant d’assembler une machine** via le point d’accès hébergé gratuit : **[Qwen3.8 27B gratuit sur OpenRouter](https://openrouter.ai/qwen/qwen3.8-27b:free)**
4. **Comparez-le au niveau payant avec les mêmes prompts** : **[Claude Sonnet 4.6 sur OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-4.6)**
5. **Dimensionnez votre machine selon le niveau voulu** avec le tableau mémoire et achetez la mémoire avant la carte graphique.
6. **Si un Raspberry Pi reste inutilisé**, vérifiez s’il peut héberger un modèle plus petit : **[Quels modèles IA peuvent tourner sur un Raspberry Pi 4 ou 5 ?](/articles/ai-models-raspberry-pi-4-5/)**

## Articles associés

| Article | Contenu |
|---|---|
| **[Quels modèles IA peuvent tourner sur un Raspberry Pi 4 ou 5 ?](/articles/ai-models-raspberry-pi-4-5/)** | La limite basse de l’inférence locale et les capacités réelles des petites cartes |
| **[Créer un assistant IA respectueux de la vie privée pour Meshtastic](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | Un assistant local sur du matériel hors réseau, où la confidentialité est indispensable |
| **[Le rôle de la mémoire ECC dans la prévention de la corruption des données](/articles/the-role-of-ecc-memory-in-mitigating-data-corruption/)** | Pourquoi la qualité de la mémoire compte davantage quand elle héberge un grand modèle |
| **[Qu’est-ce qu’un laboratoire à domicile et en avez-vous besoin ?](/articles/what-is-a-homelab-and-should-you-have-one/)** | Prévoir l’espace, l’alimentation et le refroidissement d’un matériel qui chauffe |

## Références

1. [Ternary Bonsai 2 27B - miroir du modèle Ollama](https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B)
2. [Qwen3.8 - bibliothèque de modèles Ollama](https://ollama.com/library/qwen3.8)
3. [Qwen3.8 27B (gratuit) - évaluations et tarifs OpenRouter](https://openrouter.ai/qwen/qwen3.8-27b:free)
4. [Claude Sonnet 4.6 - évaluations et tarifs OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-4.6)
5. [Premier test de Bonsai 2 27B - est-ce le MEILLEUR modèle IA pour une GPU ? - Bijan Bowen](https://www.youtube.com/watch?v=OA5cICIzD-c)
6. [Artificial Analysis - évaluations indépendantes des modèles](https://artificialanalysis.ai/)
7. [TrendForce - prévisions des prix contractuels DRAM et NAND](https://www.trendforce.com/)
8. [Les puces mémoire sont désormais plus chères que les puces de calcul par surface - Tom's Hardware](https://www.tomshardware.com/pc-components/dram/dram-is-now-more-expensive-than-compute-chips-on-per-area-basis-ai-demand-drives-memory-die-value-past-leading-edge-silicon)
9. [Le répit des GPU repoussé à 2028 après la hausse record de 95 % de la DRAM - Tech Insider](https://tech-insider.org/gpu-relief-pushed-2028-dram-price-jump-2026/)
10. [Tan d’Intel : la mémoire a été multipliée par sept, pas de répit avant 2028 - shattered.io](https://shattered.io/intel-ceo-memory-shortage-no-relief-until-2028-2026/)
11. [Fork llama.cpp de Prism ML - noyaux ternaires](https://github.com/PrismML-Eng/llama.cpp)
12. [Ternary-Bonsai-2-27B-gguf - poids sources](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)
