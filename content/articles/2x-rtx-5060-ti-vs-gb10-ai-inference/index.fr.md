---
title: "2x RTX 5060 Ti contre GB10 : benchmark d'IA locale sur cinq modèles à 256K"
date: 2026-10-10
lastmod: 2026-11-07
toc: true
draft: false
description: "Comparaison entre RTX 5060 Ti et GB10 sur cinq modèles, avec un benchmark Qwen3.8 Flash-Next sur Strata, exécuté sur le même hôte jusqu'à 256K de contexte."
genre: ["Intelligence artificielle", "IA locale", "Matériel GPU", "Benchmarks", "Matériel informatique"]
tags: ["RTX 5060 Ti", "GB10", "DGX Spark", "Qwen3.8", "Qwen3.8 Flash-Next", "GSQ-RCO", "Qwen4Exp", "Strata", "Qwen3.5", "Qwen3.6", "GPT-OSS", "Nemotron", "LLM local", "inférence locale", "mémoire unifiée", "VRAM", "benchmark GPU", "contexte long", "surcoût PCIe", "matériel IA", "NVIDIA Blackwell", "performances LLM", "mémoire GPU"]
cover: "/img/cover/nvidia-rtx-5060-ti-vs-gb10-memory-performance-comparison.webp"
coverAlt: "Illustration de deux cartes graphiques NVIDIA RTX 5060 Ti à gauche et d'un système NVIDIA GB10 à droite, mis en valeur par des couleurs vives sur un fond sombre."
coverCaption: "Les performances d'un modèle local dépendent de l'architecture mémoire, du choix du modèle et de la longueur du contexte."
---

**Deux cartes RTX 5060 Ti de 16 Go fournissent 32 Go de VRAM au total.** Un système NVIDIA GB10 dispose de 128 Go de mémoire unifiée cohérente. Le nouveau benchmark de cinq modèles donne un résultat plus équilibré que l'ancien test limité à Qwen.

À 256K, le système à deux cartes génère plus rapidement pour quatre des cinq modèles. Le GB10 est nettement devant avec Qwen3.8 27B et conserve davantage de mémoire pour les modèles, le contexte et les allocations du runtime. Le meilleur choix dépend du modèle et de la charge de travail.

Un autre test sur le même hôte a comparé Qwen3.8-Flash-Next IQ2_XS sur Strata à Qwen3.8 27B Q4_K_M dense sur Ollama. Après échauffement, la médiane de génération de Flash-Next était de 92.8 jetons par seconde avec un prompt de 260,446 jetons. Qwen3.8 dense a atteint 0.939 jeton par seconde avec un prompt de 260,444 jetons.

Le NVIDIA GB10 utilise 128 Go de mémoire unifiée cohérente. NVIDIA indique 128 Go de mémoire unifiée LPDDR5x et un TDP de puce de 140 W pour la plateforme GB10. Chaque RTX 5060 Ti dispose de 16 Go de GDDR7, d'une interface mémoire de 128 bits et d'une puissance graphique totale de 180 W. Les [spécifications NVIDIA RTX 5060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/) et les [spécifications NVIDIA GB10](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) décrivent cette différence matérielle.

**Les deux systèmes n'exposent pas la mémoire de la même façon.** Deux cartes forment deux pools distincts de 16 Go. Le GB10 place le modèle, les données de contexte, les buffers du runtime et les allocations du système d'exploitation dans un même espace d'adressage partagé.

## Comparaison de la mémoire

| Système | Mémoire | Modèle mémoire | Puissance annoncée |
|---|---:|---|---:|
| **2x RTX 5060 Ti 16 Go** | 32 Go au total | Deux pools de mémoire GPU distincts | 360 W au total pour les GPU |
| **Système GB10** | 128 Go | Mémoire système unifiée cohérente | TDP du GB10 : 140 W |

Le GB10 ne gagne pas tous les tests de débit, car la LPDDR5x n'égale pas la bande passante des GPU discrets. Son avantage tient à la capacité et au placement. Le CPU et le GPU partagent le même espace d'adressage, le jeu de travail n'a donc pas à tenir dans deux appareils isolés de 16 Go.

Le système à deux cartes doit répartir le modèle sur les deux cartes, et le runtime doit transférer des données entre elles. Le trafic PCIe ajoute de la latence et consomme de la bande passante. Selon les spécifications de NVIDIA, la RTX 5060 Ti ne prend pas non plus en charge NVLink.

## Benchmark de cinq modèles

Le test mis à jour a utilisé la même matrice de requêtes sur les deux systèmes. Il a couvert cinq modèles Ollama avec des contextes de 4K, 16K, 32K, 64K, 128K et 256K. Chaque requête a généré 128 jetons avec une température de 0.

Les tags des modèles testés étaient :

- **Qwen3.8 27B:** `qwen3.8:27b`
- **GPT-OSS 20B:** `gpt-oss:20b`
- **Qwen3.6 35B-A3B:** `qwen3.6:35b`
- **Qwen3.5 35B-A3B:** `qwen3.5:35b-a3b-q4_K_M`
- **Nemotron 3.5 Lightning 30B-A3B:** `nemotron-3.5-lightning:30b-a3b-q4_K_M`

Le système à deux cartes utilisait deux RTX 5060 Ti de 16 Go. Le système GB10 utilisait 128 Go de mémoire unifiée. Les tests utilisaient Ollama, version 0.34.2 sur le système à deux cartes et version 0.40.2 sur le GB10.

### Vitesse de génération

La vitesse de génération mesure les jetons produits après le traitement du prompt. Cette mesure compte surtout dans une conversation interactive.

Système avec deux RTX 5060 Ti :

| Contexte | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 91.518 | 162.027 | 117.547 | 156.104 | 55.654 |
| 16K | 87.176 | 161.377 | 112.903 | 140.596 | 51.656 |
| 32K | 82.372 | 157.055 | 106.455 | 144.833 | 47.369 |
| 64K | 74.661 | 135.106 | 95.979 | 125.008 | 38.863 |
| 128K | 62.767 | 130.924 | 79.572 | 115.352 | 26.399 |
| 256K | 67.853 | 106.221 | 58.947 | 67.159 | 1.079 |

GB10 :

| Contexte | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 62.199 | 98.648 | 72.405 | 100.906 | 32.985 |
| 16K | 56.764 | 94.366 | 69.782 | 95.448 | 32.939 |
| 32K | 53.257 | 98.175 | 64.055 | 95.025 | 29.772 |
| 64K | 49.201 | 96.132 | 58.428 | 84.528 | 25.625 |
| 128K | 40.637 | 80.238 | 48.108 | 74.579 | 22.294 |
| 256K | 43.688 | 68.043 | 36.649 | 62.115 | 22.371 |

À 256K, le système à deux cartes générait plus vite avec GPT-OSS, Nemotron, Qwen3.5 et Qwen3.6. Le GB10 était largement devant avec Qwen3.8 : le débit du système à deux cartes est tombé à 1.079 jeton par seconde, tandis que le GB10 atteignait 22.371 jetons par seconde.

Le résultat de Qwen3.6 est serré : le système à deux cartes a atteint 67.159 jetons par seconde et le GB10 62.115. Ce résultat ne permet pas d'affirmer que la mémoire unifiée ou deux GPU discrets gagnent toujours.

### Vitesse de traitement du prompt

Le traitement du prompt mesure la vitesse à laquelle le runtime lit le contexte d'entrée avant la génération. Il compte pour les longs documents et les rechargements répétés du contexte.

Système avec deux RTX 5060 Ti :

| Contexte | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 4745.9 | 2409.0 | 2701.7 | 464.3 | 783.9 |
| 16K | 7617.0 | 3031.8 | 4175.3 | 2654.0 | 840.1 |
| 32K | 8099.5 | 3074.2 | 4335.8 | 2623.2 | 811.2 |
| 64K | 6809.5 | 2893.0 | 4129.9 | 2400.4 | 727.8 |
| 128K | 5089.9 | 2362.7 | 3084.0 | 1723.6 | 546.1 |
| 256K | 5838.3 | 1813.2 | 2229.1 | 1011.0 | 251.3 |

GB10 :

| Contexte | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 3295.5 | 576.0 | 2067.9 | 628.8 | 756.9 |
| 16K | 4675.5 | 3006.7 | 2691.2 | 2556.3 | 812.6 |
| 32K | 4571.4 | 3077.9 | 2691.7 | 2563.9 | 794.1 |
| 64K | 3704.7 | 3066.9 | 2585.3 | 2444.9 | 714.0 |
| 128K | 2857.0 | 2802.9 | 2360.4 | 2229.9 | 655.5 |
| 256K | 3243.4 | 2325.4 | 1938.5 | 1817.6 | 535.1 |

À 256K, le système à deux cartes traitait plus vite les prompts de GPT-OSS et Qwen3.5. Le GB10 était devant pour Nemotron, Qwen3.6 et Qwen3.8. L'architecture du modèle et le comportement du runtime comptent autant que l'interface mémoire.

## Benchmarks complémentaires de Qwen3.8 Flash-Next

Trois essais supplémentaires ont mesuré des paquets GGUF Qwen3.8 Flash-Next sur le système à deux RTX 5060 Ti, avec des contextes de 4K et 16K. Chaque ligne indique la référence exacte du modèle sur Hugging Face et sa quantification.

| Modèle exact | Quantification | Génération 4K | Génération 16K |
|---|---:|---:|---:|
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS) | IQ2_XS | 31.77 tok/s | 28.20 tok/s |
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ3_S) | IQ3_S | 24.54 tok/s | 22.60 tok/s |
| [`hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M`](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF/tree/main) | Q4_K_M | 17.91 tok/s | 17.02 tok/s |

Le paquet IQ2_XS a atteint le débit le plus élevé du groupe : 31.77 jetons par seconde à 4K, contre 24.54 pour IQ3_S et 17.91 pour Q4_K_M. À 16K, le classement reste le même : 28.20, 22.60 et 17.02 jetons par seconde.

Exécutez les mêmes références exactes de modèles avec Ollama :

```bash
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S
ollama run hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M
```

Ces résultats complémentaires précédents proviennent d'un système à deux GPU. Ils sont distincts de la matrice de requêtes comparant RTX 5060 Ti et GB10 ci-dessus. Le relevé fourni indique les références exactes des modèles, les quantifications, les contextes demandés et la vitesse de génération. Il ne précise pas les empreintes de manifest résolues, le nombre de jetons du prompt traité, la longueur de sortie, l'état de chauffe, la répartition entre appareils, le CPU, la RAM, le refroidissement ni la date de mesure.

## Strata contre Ollama dense à 256K

**Un second benchmark du 14 octobre 2026 a comparé deux ensembles modèle-runtime sur le même hôte doté de deux RTX 5060 Ti.** La référence dense utilisait [`qwen3.8:27b`](https://ollama.com/library/qwen3.8:27b), un modèle Qwen35 de 27.3 milliards de paramètres en Q4_K_M. Le stack Flash utilisait [Qwen3.8-Flash-Next IQ2_XS](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS), un modèle Qwen4Exp mixture-of-experts dans un paquet natif unifié Strata.

Il s'agit d'une comparaison de stacks complets. L'architecture du modèle, la quantification, le paquet, le routage des experts et le moteur d'inférence changent ensemble. Les variantes Flash IQ3_S et Q4_K_M ne font pas partie de cette série.

### Système et méthode de test

| Composant | Configuration enregistrée |
|---|---|
| **GPU** | 2x NVIDIA GeForce RTX 5060 Ti, 16 GiB chacune, compute capability 12.0 |
| **Liaison GPU** | PCIe 4.0 x4 par carte, topologie PHB, sans NVLink |
| **CPU** | AMD Ryzen 9 5900XT, 32 threads |
| **Mémoire de l'hôte** | 62 GiB de RAM et 15 GiB de swap |
| **Pilote NVIDIA** | 595.99.02 |

Le banc d'essai a généré des enregistrements synthétiques numérotés. Chaque ligne suivait le format `Record 00001: alpha beta gamma delta epsilon zeta eta theta iota kappa.` La consigne demandait d'abord `BENCHMARK_OK`, puis une synthèse technique concise jusqu'à la limite de sortie. Les six prompts contenaient 180, 720, 1,500, 3,100, 6,200 et 12,400 enregistrements.

Chaque essai utilisait une température de 0, le seed 42 et une sortie maximale de 128 jetons. Pour chaque contexte, une phase d'échauffement précédait cinq requêtes mesurées. Les tests Ollama utilisaient `/api/generate`, ceux de Strata `/v1/chat/completions`. Toutes les requêtes mesurées se sont terminées sans erreur d'API.

Les paramètres de décodage n'étaient pas identiques. Strata définissait explicitement `reasoning_effort` sur `none` et désactivait le raisonnement via son modèle de conversation. La requête Ollama dense n'envoyait pas `think: false`; une vérification ultérieure a trouvé la sortie dense dans les champs de raisonnement et de réponse. Le résultat de génération est propre à ces modes de décodage.

| Contexte demandé | Jetons du prompt dense | Jetons du prompt Flash |
|---:|---:|---:|
| **4K** | 3,824 | 3,826 |
| **16K** | 15,164 | 15,166 |
| **32K** | 31,544 | 31,546 |
| **64K** | 65,144 | 65,146 |
| **128K** | 130,244 | 130,246 |
| **256K** | 260,444 | 260,446 |

Les en-têtes des deux modèles déclaraient un contexte maximal de 262,144 jetons. Les prompts appariés différaient de deux jetons à chaque point de mesure.

### Médiane de la vitesse de génération après échauffement

Chaque médiane couvre cinq requêtes mesurées après un échauffement. Chaque requête dense réutilisait tous les jetons du prompt sauf quatre. Chaque requête Flash en réutilisait tous sauf sept. Le tableau mesure le débit de décodage à chaud avec préfixe en cache, pas la latence de bout en bout à froid.

| Contexte | Flash IQ2_XS sur Strata | Dense Q4_K_M sur Ollama | Avantage Flash |
|---:|---:|---:|---:|
| **4K** | 98.4 tok/s | 65.0 tok/s | 1.51x |
| **16K** | 96.8 tok/s | 60.6 tok/s | 1.60x |
| **32K** | 95.3 tok/s | 64.4 tok/s | 1.48x |
| **64K** | 89.6 tok/s | 51.2 tok/s | 1.75x |
| **128K** | 92.9 tok/s | 31.5 tok/s | 2.95x |
| **256K** | 92.8 tok/s | 0.939 tok/s | 98.9x |

Le stack Flash est resté près de 90 jetons par seconde de 64K à 256K. Qwen3.8 dense a fortement ralenti après 64K et a atteint 0.939 jeton par seconde à 256K. La réponse Flash à 256K s'est terminée normalement après 67 jetons. Le test dense a atteint sa limite de sortie de 128 jetons.

### Traitement du prompt de la première requête

| Contexte | Première requête Flash | Première requête dense |
|---:|---:|---:|
| **4K** | 1,134 tok/s | 832 tok/s |
| **16K** | 2,013 tok/s | 856 tok/s |
| **32K** | 2,386 tok/s | 799 tok/s |
| **64K** | 2,509 tok/s | 690 tok/s |
| **128K** | 2,538 tok/s | 489 tok/s |
| **256K** | 2,399 tok/s | 214 tok/s |

La première requête dense a traité le prompt complet à chaque point de mesure. Strata a signalé la réutilisation de 16,384 jetons de préfixe à 64K, 49,152 à 128K et 114,688 à 256K. De 64K à 256K, les débits Flash correspondent à la continuation de la première requête et non à un prefill complet sans cache.

À 256K, Strata a traité la première requête en 60.8 secondes. Ollama a pris environ 1,215.4 secondes. La réutilisation du préfixe empêche une comparaison directe du prefill à froid à ce point.

### Le placement du runtime explique l'écart avec un long contexte

Ollama 0.34.2 utilisait llama-server 0.4.1-dev avec déchargement de couches CUDA, le modèle ChatML et le décodage spéculatif MTP avec une largeur de brouillon maximale de quatre. Les tailles de batch et microbatch étaient de 1,024 à 32K et de 512 entre 64K et 256K. Les 66 couches denses restaient sur les GPU à 32K et 64K. À 128K, 63 couches sur 66 restaient sur les GPU et 1,404 MiB passaient en mémoire mappée sur CPU. À 256K, 42 couches sur 66 restaient sur les GPU et 6,002 MiB passaient en mémoire mappée sur CPU. Le taux d'acceptation MTP à 256K était d'environ 69.4 %.

Strata 0.1.44.1 avec CUDA 13.0.3 répartissait ses 48 couches entre les deux GPU. Pour les contextes 4K et 16K, les couches 0 à 23 étaient sur le premier GPU et les couches 24 à 47 sur le second. Cette passe utilisait une réserve VRAM automatique de 700 MiB et 16,047 emplacements d'experts résidents.

La configuration de 32K à 256K plaçait les couches 0 à 24 sur le premier GPU et 25 à 47 sur le second. Cette passe utilisait le prefill automatique, une probabilité spéculative minimale de 0.5, le stockage KV INT8, 32,768 cellules KV résidentes par couche QSA, une réserve VRAM de 832 MiB, un cache d'experts de 15,318 emplacements et 21,024 MiB, ainsi que le décodage spéculatif MTP avec une largeur de brouillon maximale de quatre.

L'empreinte du blob natif Strata et PLE était `sha256:1473e0664c2017095f9164b6d617d7a71893452c1180c83002c4f28fc8c2b0da`. Le test dépendait aussi d'un profil d'experts et d'un paquet de brouillons MTP sans empreintes immuables publiées.

Le test Strata utilisait le mode par défaut de saut de fin de routage. Ce paramètre modifie légèrement la sortie du modèle et rend le résultat propre à la configuration de runtime enregistrée. Les réponses Flash contenaient le marqueur `BENCHMARK_OK`. Les requêtes denses n'ont généré aucune erreur API, mais le banc d'essai principal n'a pas capturé le marqueur. Les lignes brutes indiquaient zéro caractère de réponse. Une vérification ultérieure a trouvé une sortie dans les champs response et thinking, puis confirmé `BENCHMARK_OK` dans la réponse.

La configuration 4K et 16K a enregistré une requête avec 409 MiB libres et recommandé une réserve de 832 MiB. La configuration à long contexte a enregistré une requête avec 481 MiB libres et recommandé une réserve de 896 MiB. Ces deux valeurs étaient sous le seuil de pagination du pilote de 512 MiB. Aucune requête n'a échoué, mais ce faible niveau de mémoire affecte la répétabilité.

**Le chiffre de 98.9x correspond à un résultat de long contexte pour le stack complet, pas à la preuve d'un avantage de 98.9x pour le seul moteur.** Le test isole l'hôte, mais pas le modèle, la quantification ni le runtime.

## La longueur réelle du prompt compte

Le contexte demandé ne correspond pas au nombre de jetons de prompt traités. Avec le réglage 256K, les tests Qwen3.5, Qwen3.6, Nemotron et Qwen3.8 ont traité environ 171,359 à 171,365 jetons réels sur les deux systèmes.

À 256K, GPT-OSS a traité 65,538 jetons de prompt réels sur les deux systèmes. Sa ligne 256K ne représente donc pas la même longueur d'entrée que celle des autres modèles.

Le résultat Qwen3.8 à 256K montre l'écart le plus net. Le système à deux cartes a traité 171,359 jetons de prompt à 251.3 jetons par seconde et généré à 1.079 jeton par seconde. Le GB10 a traité le même nombre de jetons à 535.1 jetons par seconde et généré à 22.371 jetons par seconde.

**Le réglage du contexte indique la limite demandée.** Le nombre réel de jetons du prompt indique la charge traitée par le runtime.

## Pourquoi la VRAM totale compte encore

### 1. Le modèle ne voit pas une seule carte de 32 Go

Deux GPU ne fusionnent pas leur mémoire dans un seul espace d'adressage local. Un runtime model-parallel répartit les couches ou les tenseurs entre les appareils. Chaque appareil doit encore accueillir les poids attribués, les buffers temporaires et une partie de l'état du contexte.

La capacité utilisable est inférieure à la simple somme. Le surcoût exact dépend du format du modèle, de la quantification, du backend d'inférence, du découpage des tenseurs et de la longueur du contexte.

### 2. La mémoire du contexte augmente pendant la génération

Les poids du modèle ne sont qu'une partie du budget mémoire. Le cache clé-valeur (KV cache) stocke les données d'attention des jetons précédents. Les contextes plus longs nécessitent davantage de mémoire cache. Un test 4K ne prédit pas le comportement à 128K ou 256K.

Les nouveaux résultats montrent des limites différentes selon le modèle. À 256K, la vitesse de génération de Qwen3.8 s'effondre sur le système à deux cartes. Les quatre autres modèles conservent une vitesse utilisable sur les deux systèmes. La capacité mémoire reste essentielle, car elle détermine quelles combinaisons de modèle et de contexte tiennent avec les allocations du runtime.

### 3. Les transferts PCIe ajoutent un coût

Lorsque le runtime déplace des activations ou des tenseurs entre GPU, le transfert passe par l'interconnexion de l'hôte. Cela crée des points de synchronisation et ajoute de la latence à chaque étape. Le coût dépend du placement des tenseurs, de l'architecture du modèle, de la quantification et de la longueur du contexte.

Cela ne rend pas un système à deux GPU inutile. Le résultat dépend de la configuration du runtime et du modèle. Un benchmark qui ne rapporte que le traitement du prompt à 4K ignore ce coût.

### 4. L'efficacité énergétique reste un avantage système

Le GB10 offre plus de mémoire avec une puissance déclarée du GPU ou de la puce inférieure. Deux RTX 5060 Ti représentent 360 W de puissance GPU cumulée, sans compter le reste du système. NVIDIA indique un TDP de 140 W pour le GB10.

**Le GB10 échange le débit maximal sur plusieurs modèles contre plus de capacité, un jeu de travail partagé et une puissance GPU déclarée plus faible.** Le système à deux cartes offre un débit mesuré supérieur sur plusieurs modèles MoE plus récents.

## Le système 5060ti-x2 coûte beaucoup moins cher

Une station complète équipée de deux RTX 5060 Ti 16 Go était affichée à **$3,479** le 10 octobre 2026. La configuration comprend un Intel Ultra 7 265K, une carte mère Z890, 32 Go de DDR5, 1 To de stockage, une alimentation de 1,000 W et les deux GPU. [Voir l'offre complète de la station à deux GPU](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white).

La boutique américaine de NVIDIA affiche le DGX Spark 128 Go à **$6,950**. L'offre comprend 128 Go de mémoire unifiée cohérente et 4 To de stockage NVMe, mais le système est indiqué en rupture de stock. [Consulter l'offre DGX Spark actuelle de NVIDIA](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/).

La plateforme AMD Ryzen AI Halo Developer Platform offre un autre point de comparaison. Micro Center affiche ce système Strix Halo à **$3,999.99**, avec 128 Go de mémoire unifiée LPDDR5x et 2 To de stockage. Strix Halo se situe souvent dans la même catégorie pratique que les systèmes GB10 pour l'IA locale, même si des tests indépendants mesurent souvent un avantage du GB10 en débit et en maturité logicielle. [Consulter l'offre Linux actuelle de Micro Center](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false) et [lire la comparaison Strix Halo contre GB10](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4).

| Système complet | Prix affiché le 10 octobre 2026 | Écart de prix |
|---|---:|---:|
| **Station 5060ti-x2** | $3,479 | Référence |
| **AMD Ryzen AI Halo, Strix Halo** | $3,999.99 | $520.99 de plus |
| **128 GB GB10 DGX Spark** | $6,950 | $3,471 de plus |

Le GB10 offre un pool de mémoire unifiée plus grand et une puissance GPU déclarée plus faible. Le système AMD fournit la même capacité de 128 Go pour environ $4,000. Avant taxes et livraison, la station 5060ti-x2 coûte environ **50 % du prix affiché du GB10**.

Il s'agit de prix affichés par différents vendeurs, pas d'un panier de vente au détail contrôlé. Le système 5060ti-x2 dispose aussi de moins de mémoire système et de stockage. Les RTX 5060 Ti 16 Go sont actuellement affichées autour de **$789 à $830 l'unité**, bien au-dessus du prix de lancement conseillé de $429. L'avantage tarifaire du système à deux cartes subsiste donc pendant la hausse actuelle des prix GPU. [Vérifier les prix actuels des RTX 5060 Ti](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/).

## Conséquences pour les charges d'IA locales

Une configuration de deux cartes de 16 Go exécute plusieurs modèles quantifiés de 27B à 35B avec un long contexte. Le benchmark ne désigne pas un vainqueur unique pour chaque modèle.

Choisissez le système à deux cartes si vous privilégiez :

- **Une génération plus rapide pour GPT-OSS, Nemotron, Qwen3.5 et Qwen3.6** dans ce test.
- **Un débit supérieur avec un contexte court** sur les cinq modèles.
- **Un coût d'achat inférieur** à celui du GB10 affiché.
- **La compatibilité logicielle avec les GPU NVIDIA discrets** et l'expérimentation avec de futurs modèles.

Choisissez le GB10 si vous privilégiez :

- **Qwen3.8 27B à 256K**, où le GB10 génère plus de 20 fois plus vite.
- **Un seul pool mémoire de 128 Go** avec plus de place pour les poids du modèle, le cache KV et les buffers du runtime.
- **Une puissance GPU ou de puce déclarée plus faible** que celle de deux cartes discrètes.
- **Moins de contraintes de placement multi-appareils** pour les modèles qui sollicitent fortement les deux cartes.

Cela correspond aux conseils de dimensionnement de [16 Go de VRAM suffisent-ils pour travailler sérieusement avec des LLM locaux ?](/articles/is-16gb-vram-enough-local-llm/), qui regroupent poids, contexte et allocations du runtime dans un même budget. Le [guide des 32 Go de VRAM pour Qwen 27B](/articles/32gb-vram-qwen-27b-hardware-guide/) aboutit à la même conclusion pour les configurations à deux cartes. La capacité totale n'est pas la marge réellement disponible.

Avant d'acheter du matériel pour un déploiement à long contexte, posez quatre questions :

- **La quantification souhaitée tient-elle avec les buffers du runtime ?** Les seuls poids du modèle ne déterminent pas le besoin mémoire.
- **Le contexte tient-il sans forte pression sur le cache KV ?** Les longs prompts changent le résultat.
- **Le runtime répartit-il efficacement la charge entre appareils ?** Les transferts PCIe et le placement des tenseurs affectent chaque jeton généré.
- **Le système termine-t-il le contexte visé ?** Un résultat rapide à 4K ne compense pas un échec à 256K.

**Le nouveau benchmark répond à ces questions modèle par modèle.** À 256K, Qwen3.8 favorise nettement le GB10. Dans cette configuration précise, les quatre autres modèles génèrent plus vite sur le système à deux cartes. Le pool de mémoire unifiée plus grand offre davantage de réserve, même s'il n'atteint pas le débit mesuré le plus élevé.

Le même matériel à deux GPU a aussi enregistré une médiane de 92.8 jetons par seconde après échauffement à 256K avec Flash-Next IQ2_XS sur Strata. Ce résultat distinct ne renverse pas le constat concernant Qwen3.8 dense sur GB10. Flash-Next utilise une architecture mixture-of-experts, une quantification, un paquet, un runtime et un mode de décodage différents. Ce jeu de données ne contient aucun résultat Flash-Next comparable sur GB10.

## Conclusion

**Le système avec deux RTX 5060 Ti génère plus vite pour quatre des cinq modèles testés à 256K.** Il coûte aussi environ la moitié du GB10 affiché. Le GB10 reste préférable pour Qwen3.8 27B à 256K, pour la marge mémoire et pour les charges qui profitent d'un pool mémoire cohérent.

L'ancien résultat limité à Qwen semblait donner une victoire nette au GB10. Le nouveau test sur cinq modèles montre pourquoi cette conclusion était trop générale. L'architecture du modèle, la version du runtime, le placement des tenseurs et le comportement du contexte influencent le résultat.

Si vous utilisez GPT-OSS, Nemotron 3.5 Lightning, Qwen3.5 ou Qwen3.6, le système à deux cartes a généré plus vite dans ce benchmark. Pour Qwen3.8 27B à 256K, le GB10 a maintenu une vitesse exploitable tandis que le système à deux cartes a presque calé.

**La capacité mémoire et le débit sont deux critères d'achat distincts.** Le GB10 offre quatre fois plus de mémoire totale et un jeu de travail partagé plus simple. Le système à deux cartes fournit un débit observé supérieur pour la plupart des modèles testés, à un prix affiché bien inférieur.

Le résultat Strata apporte un autre enseignement. Le placement du runtime, l'architecture du modèle et le mode de décodage ont modifié le résultat à 256K sur le même hôte à deux cartes. Flash-Next IQ2_XS a conservé une médiane proche de 93 jetons par seconde après échauffement, tandis que Qwen3.8 dense a déchargé 24 couches et ralenti sous un jeton par seconde.

## Limites du benchmark

Le benchmark consigne les tags des modèles, les contextes demandés, les jetons réels des prompts, les vitesses de traitement et de génération, les versions d'Ollama et la limite de sortie de 128 jetons. Il ne consigne pas les empreintes de manifest résolues, la puissance du CPU, la consommation à la prise, la vitesse des ventilateurs ni le refroidissement.

Les lignes GPT-OSS à 256K ont traité 65,538 jetons réels de prompt sur les deux systèmes. Les autres lignes 256K en ont traité environ 171K. Considérez ces chiffres comme une comparaison observée des systèmes, pas comme un classement universel de chaque paire de RTX 5060 Ti et de chaque implémentation GB10.

Le test Strata contre dense consigne le nombre exact de jetons des prompts, cinq requêtes mesurées par contexte, les versions du runtime, le placement des appareils, les paramètres de cache et l'état des requêtes. La comparaison change simultanément l'architecture, la quantification, le paquet, le runtime et le mode de décodage. Strata a aussi réutilisé les préfixes de prompt au-delà de 32K. Les requêtes de génération mesurées dans les deux stacks ont réutilisé presque tout le prompt.

Une reproduction exacte à partir de cet article est impossible. Le banc de test, la structure du paquet Strata, le profil d'experts et le paquet de brouillons MTP ne sont pas publiés avec des empreintes immuables. L'avertissement de faible VRAM ajoute aussi un risque de variation entre exécutions. Le test isole l'hôte, pas le moteur d'inférence.

Les spécifications matérielles ci-dessus proviennent de NVIDIA. Les chiffres de performance viennent du benchmark contrôlé réalisé pour cet article.

## Références

- [Bibliothèque Ollama des modèles Qwen3.8](https://ollama.com/library/qwen3.8)
- [Modèles GGUF ISTA-DASLab Qwen3.8 Flash-Next GSQ-RCO](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF)
- [Modèles GGUF orcarouter Qwen3.8 Flash-Next Uncensored](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF)
- [Bibliothèque Ollama des modèles Qwen3.5](https://ollama.com/library/qwen3.5)
- [Bibliothèque Ollama des modèles Qwen3.6](https://ollama.com/library/qwen3.6)
- [Bibliothèque Ollama des modèles Nemotron 3.5 Lightning](https://ollama.com/library/nemotron-3.5-lightning)
- [Tags des modèles GPT-OSS dans Ollama](https://ollama.com/library/gpt-oss/tags)
- [16 Go de VRAM suffisent-ils pour travailler sérieusement avec des LLM locaux ?](/articles/is-16gb-vram-enough-local-llm/)
- [32 Go de VRAM pour Qwen 27B](/articles/32gb-vram-qwen-27b-hardware-guide/)
- [Guide du contexte GPU pour l'IA locale](/articles/local-ai-model-gpu-context-guide/)
- [Benchmarks GPU de Qwen3.8 27B sur Vast.ai](/articles/qwen38-27b-vast-ai-gpu-benchmark/)
- [Offre complète de station avec deux RTX 5060 Ti de 16 Go](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white)
- [Offre NVIDIA DGX Spark sur le marché américain](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/)
- [Offre Linux AMD Ryzen AI Halo 128 Go](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false)
- [Test Tom's Hardware : Strix Halo contre GB10](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4)
- [Prix actuels des RTX 5060 Ti](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/)
