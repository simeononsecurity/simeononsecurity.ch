---
title: "Benchmarks de modèles locaux avec Hermes : les combinaisons de GPU et de modèles que je choisirais"
date: 2026-10-24
lastmod: 2026-11-15
toc: true
draft: false
description: "Mes recommandations de modèles Hermes reposent sur des tests de contexte long, d'outils, de diffusion en continu et de vision sur des systèmes RTX 5060 Ti, RTX 2000E Ada, RTX 3060 Ti et RTX 3070."
genre: ["Intelligence artificielle", "IA locale", "Matériel informatique"]
tags: ["Agent Hermes", "modèles de langage locaux", "benchmarks de LLM", "inférence GPU", "RTX 3060 Ti", "RTX 3070", "RTX 2000E Ada", "RTX 5060 Ti", "qualification de modèle", "appel d'outils", "contexte long", "llama.cpp", "Ollama", "Qwen3.5", "Qwen3.6", "Qwen3.8"]
cover: "/img/cover/hermes-local-model-gpu-benchmarks.webp"
coverAlt: "Illustration de cartes graphiques à deux ventilateurs et à profil bas près du titre Hermes Model Benchmarks sur fond bleu foncé"
coverCaption: ""
---

Pour les tâches Hermes avec un long contexte, je commencerais par Qwen3.5 35B sur deux cartes RTX 5060 Ti de 16 Go. La configuration testée a conservé 239 153 jetons d'entrée via LiteLLM et réussi les contrôles distincts des outils, du flux continu, de la vision, des requêtes en file d'attente et de l'annulation. Qwen3.6 est mon option sur une seule carte. Sur les systèmes RTX 3060 Ti et RTX 3070, je commencerais par Qwen3.5 2B ou 4B.

Ces choix viennent de l'exécution des modèles sur les chemins d'inférence utilisés par l'agent. J'ai testé la conservation des entrées longues, les échanges avec les outils, les réponses en continu, les questions sur des images et la libération du modèle. J'ai aussi testé les modes et les réglages mémoire associés aux configurations, car réussir à charger un modèle dit peu de choses sur son utilité pendant une longue requête d'agent.

Hermes exige au moins 64 000 jetons de contexte pour utiliser des outils avec un agent. J'ai fixé le seuil de qualification du contexte long à 65 536 jetons d'entrée réels. Le nombre de jetons d'entrée compte davantage que la taille de contexte annoncée par le serveur. ([Documentation des fournisseurs Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md))

## Quels GPU équipent chaque système

Les lettres des systèmes désignent les combinaisons matérielles utilisées dans les résultats.

| Système | GPU utilisés pour ce benchmark | Modèle que je choisirais en premier |
|---|---|---|
| A | 2 × GeForce RTX 5060 Ti, 16 Go chacune | Qwen3.5 35B sur les deux cartes, ou Qwen3.6 sur une seule carte |
| B | 1 × RTX 2000E Ada, 16 Go | Qwen3.5 9B si plusieurs minutes de traitement d'une longue entrée conviennent à la tâche |
| C | 1 × RTX 2000E Ada, 16 Go | Gemma 3 4B pour le chemin d'entrée longue testé, Qwen3.5 0.8B sans réflexion pour les tâches de rappel ciblées |
| D | 1 × RTX 2000E Ada, 16 Go | Qwen3.5 9B, Gemma 4 12B-IT ou GPT-OSS 20B pour les charges testées avec de plus grands modèles |
| E | 9 × GeForce RTX 3060 Ti, 8 Go chacune | Qwen3.5 2B ou 4B |
| F | 8 × GeForce RTX 3060 Ti, 8 Go chacune | Qwen3.5 2B ou 4B |
| G | 3 × GeForce RTX 3070 | Qwen3.5 2B ou 4B |

Le nombre de cartes installées ne signifie pas que chaque requête utilisait tous les GPU. Les essais Qwen3.5 35B et Flash Next utilisaient les deux cartes du système A. Qwen3.6 n'en utilisait qu'une. Le nouvel essai réussi de vision avec Qwen3.5 4B sur le système E utilisait une carte choisie parmi huit, tandis qu'une neuvième carte restait exclue des tâches d'IA.

Considérez les durées ci-dessous comme des résultats combinant le modèle, l'environnement d'exécution et le système testés. Ces essais comparent des configurations utilisables. Ils ne permettent pas d'isoler l'architecture du GPU comme cause des écarts de vitesse.

## Deux RTX 5060 Ti font de Qwen3.5 35B mon choix pour le contexte long

Qwen3.5 35B a produit le plus grand résultat d'entrée conservée de ces tests. La progression directe dans Ollama a conservé 248 279 jetons d'entrée dans un contexte d'exécution de 262 144 jetons. Une requête distincte en flux continu via la passerelle a conservé 239 153 jetons d'entrée, renvoyé le marqueur initial et terminé normalement après 31 jetons de sortie en 148,12 secondes.

Le résultat de la passerelle compte pour Hermes, car la requête passait par le courtier et LiteLLM. Des requêtes distinctes ont terminé un échange avec un outil, reconnu une image rouge et renvoyé deux réponses correctes lorsqu'elles ont été soumises ensemble. Le courtier a mis ces deux requêtes en file d'attente. La fermeture d'une requête en flux continu a libéré le courtier et déchargé le modèle en 60,31 secondes.

| Requête Qwen3.5 35B | Jetons d'entrée | Jetons de sortie | Durée | Résultat |
|---|---:|---:|---:|---|
| Ollama direct, première étape progressive | 69,429 | 31 | 38.783 s | Marqueur initial exact |
| Ollama direct, continuation avec préfixe partagé | 124,179 | 31 | 28.472 s | Marqueur initial exact |
| Ollama direct, continuation avec préfixe partagé | 182,579 | 31 | 38.974 s | Marqueur initial exact |
| Ollama direct, continuation avec préfixe partagé | 248,279 | 31 | 54.215 s | Marqueur initial exact |
| Requête en flux continu par le courtier | 69,427 | 29 | 38.872 s | Marqueur initial exact |
| Requête en flux continu LiteLLM | 239,153 | 31 | 148.12 s | Marqueur initial exact, déchargement propre |

Les requêtes directes progressives réutilisaient un préfixe de plus en plus long. Leurs durées décrivent le comportement de continuation à chaud. Le résultat de 54,215 secondes n'est pas une mesure indépendante à froid du traitement d'une nouvelle invite de 248K.

À l'étape directe la plus longue, le modèle signalait environ 27,3 milliards d'octets résidents sur les deux GPU. Les pics mémoire par carte atteignaient 14 964 et 12 386 MiB.

Les températures maximales ont atteint 62 et 63 C, sans erreur OOM ni Xid enregistrée. L'entrée laissait 13 865 jetons dans le contexte configuré pour la suite. La courte réponse marqueur en utilisait 31.

J'utiliserais cette configuration lorsque la conservation d'un grand ensemble de travail compte davantage qu'une réponse initiale rapide. Les contrôles des outils et de la vision établissent des comportements utiles pour un agent, tandis que le test d'entrée longue établit la conservation du contexte. Ce sont des charges distinctes.

## Qwen3.6 est l'option sur une seule carte

Qwen3.6-35B-A3B UD-Q4_K_XL a conservé 131 000 jetons d'entrée sur une seule RTX 5060 Ti. L'autre carte est restée inactive pendant le test. Le système dispose ainsi d'une option utile lorsqu'on ne souhaite pas consacrer les deux cartes à un seul modèle.

| Requête Qwen3.6 via la passerelle | Jetons d'entrée | Jetons de sortie | Durée | Résultat |
|---|---:|---:|---:|---|
| Requête longue initiale | 66,007 |  | 167.82 s | Marqueur initial conservé |
| Requête plus longue | 90,000 | 11 | 159.92 s | Marqueur initial conservé, aucune entrée mise en cache |
| Requête plus longue | 119,999 | 11 | 250.61 s | Marqueur initial conservé, aucune entrée mise en cache |
| Près de la limite d'exécution | 131,000 | 11 | 287.09 s | Marqueur initial conservé, aucune entrée mise en cache |

La requête de 131 000 jetons approchait la limite d'exécution de 131 072 jetons. Pour un agent, je garderais davantage d'espace pour la réponse et les messages d'outils suivants. Une conservation proche de la limite renseigne sur le traitement des entrées, mais ne constitue pas un budget d'entrée par défaut raisonnable.

L'utilisation des outils a réussi avec la réflexion désactivée. La réflexion par défaut a consommé le budget d'essai de 512 jetons avant d'émettre l'appel d'outil. Le test pilote réussi a aussi passé les requêtes rapides, en flux continu et de vision. Son contrôle initial de contexte de 65 845 jetons a pris 139,57 secondes.

## Qwen3.8 27B gagne la comparaison à réponse égale sur 66K

Pour la même charge marqueur de 66 007 jetons sur le système A, Qwen3.8 27B a renvoyé la réponse le plus vite. Je garderais cette configuration pour les requêtes proches de la taille d'entrée testée, à côté de Qwen3.5 35B pour les ensembles de travail plus grands.

| Configuration du système A | Jetons d'entrée | Durée | Résultat |
|---|---:|---:|---|
| Qwen3.8 27B | 66,007 | 54.64 s | Marqueur initial conservé |
| Qwen3.6-35B-A3B UD-Q4_K_XL | 66,007 | 167.82 s | Marqueur initial conservé |
| Qwen3.8-Flash-Next UD-IQ4_XS | 66,007 | 164.58 s | Marqueur initial conservé |
| Alias de compatibilité Flash Next IQ4 | 66,007 | 213.25 s | Marqueur conservé |

Qwen3.8 27B a pris environ un tiers du temps des requêtes comparables Qwen3.6 et Flash Next. Il s'agit d'observations sur des requêtes complètes avec les environnements testés, et non d'une comparaison limitée au matériel.

Les réponses rapides, le flux continu et l'utilisation d'outils ont aussi réussi. Le mode sans réflexion a terminé la séquence complète de couleurs et l'échange avec l'outil, tandis que l'essai avec réflexion n'a renvoyé qu'une partie de la séquence dans le budget de 512 jetons.

Flash Next reste un choix par défaut moins intéressant sur ce système en raison de la pression mémoire. Son essai pilote de 65 847 jetons a réussi en 201,41 secondes avec un contexte d'exécution de 98 304. Deux profils antérieurs à 131 072 jetons ont atteint leur limite mémoire avant d'être prêts.

La configuration ultérieure a atteint sa limite cgroup de 54 GiB. Pour un travail sans surveillance, je choisirais une configuration offrant davantage de marge mémoire.

La route nommée `flash-iq2` servait le backend de compatibilité Flash Next IQ4. Son nom ne désigne pas un résultat IQ2.

## La RTX 2000E Ada traite les longues entrées, mais le modèle change le délai

Gemma 3 4B est ma configuration testée préférée pour les longues entrées sur le système C. Deux chemins ont conservé plus de 84K jetons d'entrée en environ 88 secondes. Les configurations avec des modèles plus grands ont aussi réussi des contrôles de conservation utiles, mais leurs requêtes ont pris plusieurs minutes.

| Système | Modèle et chemin | Jetons d'entrée | Durée | Résultat |
|---|---|---:|---:|---|
| B | Qwen3.5 9B, passerelle | 72,265 | 263 s | Les deux marqueurs ont été conservés, le contrôle ultérieur de reprise du minage a réussi |
| C | Gemma 3 4B, passerelle | 84,044 | 88.05 s | Marqueur initial conservé |
| C | Gemma 3 4B, Aperture | 84,045 | 87.68 s | Marqueur initial conservé |
| C | Gemma 4 12B-IT, passerelle | 67,254 | 263.07 s | Marqueur initial conservé |
| C | Gemma 4 12B-IT, Aperture sans flux continu | 67,255 | 274.24 s | Marqueur initial conservé |
| C | Gemma 4 12B-IT, flux continu Aperture | 67,255 | 282.16 s | Marqueur initial conservé |
| C | Qwen3.5 9B, passerelle | 75,648 | 319.36 s | Marqueur initial conservé, modèle déchargé |
| C | GPT-OSS 20B, passerelle | 84,099 | 315.83 s | Marqueur initial conservé, modèle déchargé |
| D | Qwen3.5 9B, Aperture | 81,051 | 324.07 s | Conservation réussie sur l'artefact installé |
| D | Gemma 4 12B-IT, Aperture | 72,057 | 300.67 s | Conservation réussie sur l'artefact installé |
| D | GPT-OSS 20B, Aperture | 72,104 | 245.94 s | Conservation réussie sur l'artefact installé |

Le flux continu n'a pas supprimé le long délai de préremplissage de Gemma 4 sur le système C. Le premier contenu diffusé est arrivé après 277,49 secondes, soit après la réponse complète de 274,24 secondes sans flux continu. Une première tentative sans flux a expiré avant la relance réussie. Je réserverais cette configuration aux tâches qui tolèrent plusieurs minutes de traitement initial.

Gemma 3 4B montre aussi pourquoi je limiterais la qualification à chaque système testé. Le système D a manqué le marqueur initial lors de deux essais de rappel à 65K, y compris une répétition à température zéro avec 67 252 jetons d'entrée. La requête déterministe s'est terminée normalement en 62,07 secondes avec le GPU entièrement occupé.

Une fin rapide et une réponse API normale ne garantissaient pas une réponse correcte. J'utiliserais le chemin réussi du système C et écarterais celui du système D de la sélection Hermes.

## Le mode de réflexion détermine l'utilité de Qwen3.5 0.8B

Qwen3.5 0.8B est devenu un candidat utile au rappel ciblé sur le système C après désactivation de la réflexion. Le petit modèle Q8_0 a conservé 75 649 jetons d'entrée via la passerelle en 65,92 secondes. Ce résultat concerne l'artefact Q8_0 testé et le chemin sans réflexion, pas les anciennes configurations à contexte de 16K présentées ailleurs dans le tableau.

| Requête Qwen3.5 0.8B sur le système C | Jetons d'entrée | Jetons de sortie | Durée | Résultat |
|---|---:|---:|---:|---|
| Réflexion par défaut, diagnostic court | 9,050 | 3,391 | 66.56 s | Marqueur initial exact |
| Réflexion désactivée, diagnostic comparable | 9,055 | 21 | 7.65 s | Marqueur initial exact, aucun texte de raisonnement |
| Réflexion par défaut, essai long |  |  | délai dépassé à 600 s | Aucune réponse terminée |
| Réflexion désactivée, Ollama natif | 75,656 | 22 | 69.80 s | Marqueur initial exact |
| Point de terminaison compatible OpenAI sans réflexion | 75,646 | 12 | 69.09 s | Marqueur initial exact |
| Courtier avec mode sans réflexion imposé | 75,647 | 13 | 66.83 s | Marqueur initial exact |
| LiteLLM du système A vers le système C | 75,649 | 15 | 65.92 s | Marqueur initial exact |

Le diagnostic comparable est passé de 66,56 à 7,65 secondes, soit environ 8,7 fois plus vite, tandis que la sortie générée est passée de 3 391 à 21 jetons. C'est pourquoi je définirais explicitement le mode de raisonnement pour les tâches simples d'extraction et de routage. Le raisonnement par défaut consacrait l'essentiel du travail à une sortie inutile pour la tâche.

Une courte sonde compatible OpenAI a manqué son marqueur avant la réussite de la nouvelle tentative à température zéro. Les contrôles de chemin réussis utilisaient le mode sans réflexion et une fin naturelle, sans limite de sortie. Trois autres passerelles ont réussi les requêtes courtes avec marqueur en 4,22, 4,37 et 3,85 secondes. Ces contrôles vérifient le routage, tandis que la requête de 75 649 jetons vérifie la conservation des longues entrées via la passerelle.

Je testerais cette configuration pour le rappel et l'extraction à portée limitée. Pour un raisonnement d'agent ouvert, je choisirais un modèle plus grand. Récupérer un marqueur synthétique est une tâche plus limitée que planifier, coder ou coordonner plusieurs outils.

## Les systèmes RTX 3060 Ti et RTX 3070 conviennent mieux à Qwen3.5 2B et 4B

Qwen3.5 2B et 4B sont mes choix de départ pratiques pour les cartes de 8 Go. Les requêtes de contexte texte sur les systèmes E, F et G ont réussi avec 65 579 jetons d'entrée et des durées de 30,343 à 93,753 secondes. Les chemins 4B testés ont aussi réussi les contrôles d'outils, de flux continu et d'image.

La nouvelle exécution de contexte visuel 4B sur le système E a conservé les deux marqueurs et l'ordre des couleurs de l'image avec 65 637 jetons d'entrée en 44,88 secondes. Les requêtes avec ordre des couleurs direct et inversé ont aussi réussi. La répétition utilisait une carte saine après une erreur de liaison Xid 79 sur une autre carte et le redémarrage du système.

| Système | Contexte texte Qwen3.5 2B | Contexte texte Qwen3.5 4B | Contexte vision Qwen3.5 4B |
|---|---|---|---|
| E, parc de RTX 3060 Ti | 65,579 jetons, 30.343 s | 65,579 jetons, 53.787 s | 65,637 jetons, 44.88 s |
| F, parc de RTX 3060 Ti | 65,579 jetons, 61.282 s | 65,579 jetons, 93.753 s | 65,635 jetons, 84.749 s |
| G, parc de RTX 3070 | 65,579 jetons, 76.731 s | 65,579 jetons, 90.807 s | 65,635 jetons, 87.496 s |

Chacun de ces systèmes a enregistré 29 contrôles réussis. L'écart de durée entre les deux systèmes RTX 3060 Ti montre aussi pourquoi je sélectionnerais un profil système testé au lieu de classer les cartes à partir de ces durées de requête.

Les sept systèmes ont repris le minage après la période d'inférence. Le contrôle distinct de reprise après arrêt du système B a réussi avec de nouvelles parts acceptées. La carte défaillante du système E a ensuite repris le minage après un redémarrage et un renforcement de la liaison PCIe, tout en restant exclue du parc IA. Le rétablissement du minage en fin de période est un résultat distinct du retour automatique après chaque requête d'inférence.

## Charger un modèle ne suffit pas à le qualifier

J'écarterais DeepSeek Coder V2 16B des choix Hermes testés à 65K. Son essai avec cache f16 a conservé 50 477 jetons d'entrée, mais l'essai visant 65K a atteint la protection VRAM. Les options de cache Q4 et Q8 ont chargé les poids sur les GPU, puis atteint les limites de mémoire hôte ou un débit médiocre sur les longues invites.

| Profil de cache DeepSeek Coder V2 | Contexte d'exécution | Résultat observé | Mon évaluation |
|---|---:|---|---|
| f16 | 81,920 | Rappel de 50 477 jetons réussi, requête trop grande rejetée | Résultat utile à contexte plus court |
| f16 | 73,728 | Préremplissage cible 65K arrêté à 15 802 MiB d'utilisation GPU | Ne convient pas à 65K |
| Q4_0 | 98,304 | Le préremplissage long est tombé à 96.72 jetons/s avant l'arrêt contrôlé | Peu adapté à cette charge |
| Q8_0 | 77,824 | Le préremplissage long est tombé à 120.12 jetons/s avant l'arrêt contrôlé | Peu adapté à cette charge |
| Q4_0 / Q8_0, profils plus grands | 163,840 / 98,304 | Les protections de mémoire hôte ont arrêté les essais | La capacité dépend de tout le système |

La leçon pratique consiste à tester la requête que vous comptez envoyer. La présence du modèle en mémoire GPU, une réponse courte et un grand contexte configuré ne prouvent pas que les longues entrées sont conservées avec une latence utile.

Granite 4.2 8B et GPT-OSS 20B se sont améliorés après des ajustements ciblés au chemin sur le système A. Le chemin Q6_K de Granite a conservé 66 082 jetons d'entrée en 88,636 secondes sans entrée mise en cache. GPT-OSS a terminé son échange avec l'outil après la correction du courtier, en 9,854 secondes pour l'appel et 9,849 secondes pour le suivi. Je distinguerais ces contrôles de chemins réussis des essais antérieurs incomplets.

## Résultats complets des benchmarks

Le tableau contient 295 contrôles répartis sur 59 combinaisons de modèles et de systèmes. La matrice recense 273 réussites, un échec de rappel et sept résultats incomplets, incohérents ou incompatibles. Quatorze contrôles sortent du périmètre de qualification à 65K. Chaque ligne conserve son résultat mesuré.

Mes recommandations concernent les chemins et charges qui ont réussi. Une ligne en échec ou incomplète ne qualifie pas le comportement correspondant.

Les réussites à contexte court et en intégration s'appliquent à leurs propres charges. Une réussite à contexte de 16K ou 32K ne qualifie pas un chemin pour la charge Hermes à 65 536 jetons d'entrée. Les noms des modèles sont ici des noms de chemin. Le nom `flash-iq2` correspondait au backend de compatibilité IQ4.

La ligne de contexte Qwen3.5 35B du système A correspond à la dernière étape de préfixe partagé présentée ci-dessus. Les durées d'utilisation d'outil avec un signe plus indiquent séparément l'appel et le suivi.

La ligne de concurrence indique les durées des deux requêtes en file d'attente. La ligne d'annulation indique le délai de libération après fermeture du flux par le client. Les progressions supplémentaires de contexte et les comparaisons de chemin Qwen3.5 0.8B figurent dans leurs propres tableaux ci-dessus.

### Système A

| Étiquette de route du modèle | Contrôle | Résultat | Jetons d'entrée | Durée de requête |
|---|---|---|---:|---:|
| bonsai-2-27b | context | Réussi | 65,621 | 88.746 s |
| bonsai-2-27b | quick | Réussi | 57 | 6.429 s |
| bonsai-2-27b | stream | Réussi |  | 9.371 s |
| bonsai-2-27b | tools | Réussi |  | 10.478 s |
| deepseek-coder-v2:16b | context | Incompatible | 50,477 |  |
| deepseek-coder-v2:16b | quick | Réussi | 77 | 43.239 s |
| flash-iq2 | context | Réussi | 66,007 | 213.25 s |
| flash-iq2 | quick | Réussi |  | 56.03 s |
| flash-iq2 | stream | Réussi |  | 1.35 s |
| flash-iq2 | tools | Réussi |  | 16.55 s |
| gemma-4-12b-it | context | Réussi | 65,590 | 51.225 s |
| gemma-4-12b-it | quick | Réussi | 21 | 5.166 s |
| gemma-4-12b-it | stream | Réussi |  | 4.653 s |
| gemma-4-12b-it | tools | Réussi |  | 18.72 s |
| gemma-4-12b-it | vision | Réussi | 115 | 7.222 s |
| gemma-4-12b-it | vision_context | Réussi | 65,685 | 56.06 s |
| gemma-4-12b-it | vision_reverse | Réussi | 115 | 7.467 s |
| gemma-4-e4b-it | context | Réussi | 65,590 | 21.889 s |
| gemma-4-e4b-it | quick | Réussi | 21 | 17.919 s |
| gemma-4-e4b-it | stream | Réussi |  | 4.25 s |
| gemma-4-e4b-it | tools | Réussi |  | 8.734 s |
| gpt-oss-20b | context | Réussi | 65,637 | 159.155 s |
| gpt-oss-20b | quick | Réussi | 73 | 10.548 s |
| gpt-oss-20b | stream | Réussi |  | 20.594 s |
| gpt-oss-20b | tools | Réussi |  | 9.854 + 9.849 s |
| granite-4.2-3b | context | Réussi | 65,589 | 70.968 s |
| granite-4.2-3b | quick | Réussi | 20 | 4.009 s |
| granite-4.2-3b | stream | Réussi |  | 5.365 s |
| granite-4.2-3b | tools | Réussi |  | 6.086 s |
| granite-4.2-8b | context | Réussi | 66,082 | 88.636 s |
| granite-4.2-8b | quick | Réussi | 20 | 5.857 s |
| granite-4.2-8b | stream | Réussi |  | 11.826 s |
| granite-4.2-8b | tools | Réussi |  | 11.852 s |
| qwen27b | context | Réussi | 66,007 | 54.64 s |
| qwen27b | quick | Réussi | 57 | 31.5 s |
| qwen27b | stream | Réussi |  | 0.92 s |
| qwen27b | tools | Réussi |  | 4.25 s |
| qwen3-embedding-0.6b | context | Réussi | 32,767 | 7.736 s |
| qwen3-embedding-0.6b | quick | Réussi | 14 | 2.125 s |
| qwen3.5-0.8b | context | Réussi | 16,429 | 10.5 s |
| qwen3.5-0.8b | quick | Réussi | 17 | 14.316 s |
| qwen3.5-0.8b | stream | Réussi |  | 2.125 s |
| qwen3.5-0.8b | tools | Réussi |  | 4.416 s |
| qwen3.5-2b | context | Réussi | 65,581 | 11.175 s |
| qwen3.5-2b | quick | Réussi | 17 | 4.519 s |
| qwen3.5-2b | stream | Réussi |  | 3.736 s |
| qwen3.5-2b | tools | Réussi |  | 5.046 s |
| qwen3.5-4b | context | Réussi | 65,579 | 36.451 s |
| qwen3.5-4b | quick | Réussi | 15 | 19.935 s |
| qwen3.5-4b | stream | Réussi |  | 17.496 s |
| qwen3.5-4b | tools | Réussi |  | 7.308 s |
| qwen3.5-4b | vision | Réussi | 70 | 7.848 s |
| qwen3.5-4b | vision_context | Réussi | 65,635 | 28.24 s |
| qwen3.5-4b | vision_reverse | Réussi | 70 | 4.386 s |
| qwen3.5-9b | context | Réussi | 65,581 | 34.139 s |
| qwen3.5-9b | quick | Réussi | 17 | 3.88 s |
| qwen3.5-9b | stream | Réussi |  | 3.378 s |
| qwen3.5-9b | tools | Réussi |  | 10.204 s |
| qwen3.5-9b | vision | Réussi | 72 | 4.441 s |
| qwen3.5-9b | vision_context | Réussi | 65,637 | 33.745 s |
| qwen3.5-9b | vision_reverse | Réussi | 72 | 3.97 s |
| qwen3.5:35b-a3b-q4_K_M | cancellation | Réussi |  | 60.31 s |
| qwen3.5:35b-a3b-q4_K_M | concurrency | Réussi |  | 26.23 / 25.33 s |
| qwen3.5:35b-a3b-q4_K_M | context | Réussi | 248,279 | 54.215 s |
| qwen3.5:35b-a3b-q4_K_M | gateway | Réussi | 239,153 | 148.12 s |
| qwen3.5:35b-a3b-q4_K_M | quick | Réussi | 79 | 10.08 s |
| qwen3.5:35b-a3b-q4_K_M | stream | Réussi | 69,429 | 38.783 s |
| qwen3.5:35b-a3b-q4_K_M | tools | Réussi |  | 15.22 + 14.83 s |
| qwen3.5:35b-a3b-q4_K_M | vision | Réussi |  | 18.39 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | context | Réussi | 65,845 | 139.57 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | quick | Réussi | 15 | 3.97 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | stream | Réussi |  | 0.45 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | tools | Réussi | 293 | 5.48 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | vision | Réussi | 38 | 0.59 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | context | Réussi | 65,847 | 201.41 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | quick | Réussi | 17 | 54.62 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | stream | Réussi |  | 1.2 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | tools | Réussi |  | 22.18 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | vision | Réussi |  | 3.86 s |

### Système B

| Étiquette de route du modèle | Contrôle | Résultat | Jetons d'entrée | Durée de requête |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Réussi | 65,590 | 299.163 s |
| gemma-4-12b-it | quick | Réussi | 21 | 15.261 s |
| gemma-4-12b-it | stream | Réussi |  | 148.792 s |
| gemma-4-12b-it | tools | Réussi |  | 34.124 s |
| gemma-4-12b-it | vision | Réussi | 120 | 61.455 s |
| gemma-4-12b-it | vision_context | Réussi | 65,690 | 295.581 s |
| gemma-4-12b-it | vision_reverse | Réussi | 120 | 32.511 s |
| gemma3-4b | context | Réussi | 65,584 | 67.382 s |
| gemma3-4b | quick | Réussi | 15 | 6.329 s |
| gemma3-4b | stream | Réussi |  | 24.138 s |
| gemma3-4b | vision | Réussi | 306 | 7.018 s |
| gemma3-4b | vision_context | Réussi | 65,876 | 70.912 s |
| gemma3-4b | vision_reverse | Réussi | 306 | 5.762 s |
| gpt-oss-20b | context | Réussi | 65,637 | 206.767 s |
| gpt-oss-20b | quick | Réussi | 72 | 16.583 s |
| gpt-oss-20b | stream | Réussi |  | 32.075 s |
| gpt-oss-20b | tools | Réussi |  | 28.102 s |
| nomic-embed-text | context | Incomplet | 2,048 |  |
| nomic-embed-text | quick | Réussi |  | 7.117 s |
| qwen3-14b | context | Incomplet |  | 1800.09 s |
| qwen3-14b | quick | Réussi | 15 | 37.199 s |
| qwen3-14b | stream | Réussi |  | 35.471 s |
| qwen3-14b | tools | Réussi |  | 87.554 s |
| qwen3-8b | context | Hors périmètre sous 65K, exclu |  |  |
| qwen3-8b | quick | Hors périmètre sous 65K, réussite | 15 | 21.059 s |
| qwen3-8b | stream | Hors périmètre sous 65K, exclu |  |  |
| qwen3-8b | tools | Hors périmètre sous 65K, exclu |  |  |
| qwen3.5-9b | context | Réussi | 65,579 | 282.796 s |
| qwen3.5-9b | litellm_long_route | Réussi | 72,265 | 263 s |
| qwen3.5-9b | post_external_stop_mining | Réussi |  |  |
| qwen3.5-9b | quick | Réussi | 15 | 25.881 s |
| qwen3.5-9b | stream | Réussi |  | 143.44 s |
| qwen3.5-9b | tools | Réussi |  | 31.812 s |
| qwen3.5-9b | vision | Réussi | 75 | 32.015 s |
| qwen3.5-9b | vision_context | Réussi | 65,640 | 396.288 s |
| qwen3.5-9b | vision_reverse | Réussi | 75 | 28.626 s |

### Système C

| Étiquette de route du modèle | Contrôle | Résultat | Jetons d'entrée | Durée de requête |
|---|---|---|---:|---:|
| gemma-4-12b-it | aperture_context | Réussi | 67,255 | 274.24 s |
| gemma-4-12b-it | aperture_short | Réussi | 35 | 39.32 s |
| gemma-4-12b-it | aperture_stream_context | Réussi | 67,255 | 282.16 s |
| gemma-4-12b-it | context | Réussi | 65,670 | 313.661 s |
| gemma-4-12b-it | gateway_context | Réussi | 67,254 | 263.07 s |
| gemma-4-12b-it | gateway_short | Réussi | 27 | 20.98 s |
| gemma-4-12b-it | quick | Réussi | 21 | 16.447 s |
| gemma-4-12b-it | stream | Réussi |  | 15.175 s |
| gemma-4-12b-it | tools | Réussi |  | 37.821 s |
| gemma-4-12b-it | vision | Réussi | 120 | 58.52 s |
| gemma-4-12b-it | vision_context | Réussi | 65,690 | 308.759 s |
| gemma-4-12b-it | vision_reverse | Réussi | 120 | 31.25 s |
| gemma3-4b | aperture_context | Réussi | 84,045 | 87.68 s |
| gemma3-4b | aperture_after_system_d_route_change | Réussi | 24 | 5.42 s |
| gemma3-4b | aperture_short | Réussi | 22 | 5.45 s |
| gemma3-4b | aperture_stream | Réussi |  | 3.72 s |
| gemma3-4b | context | Réussi | 65,664 | 67.543 s |
| gemma3-4b | gateway_context | Réussi | 84,044 | 88.05 s |
| gemma3-4b | gateway_short_via_system_a | Réussi |  | 3.16 s |
| gemma3-4b | gateway_short_via_system_e | Réussi |  |  |
| gemma3-4b | gateway_short_via_system_f | Réussi |  | 4.15 s |
| gemma3-4b | gateway_short_via_system_g | Réussi |  | 6.06 s |
| gemma3-4b | quick | Réussi | 15 | 5.163 s |
| gemma3-4b | stream | Réussi |  | 24.691 s |
| gemma3-4b | vision | Réussi | 306 | 7.318 s |
| gemma3-4b | vision_context | Réussi | 65,876 | 72.476 s |
| gemma3-4b | vision_reverse | Réussi | 306 | 5.831 s |
| gpt-oss-20b | context | Réussi | 65,716 | 216.594 s |
| gpt-oss-20b | gateway_context | Réussi | 84,099 | 315.83 s |
| gpt-oss-20b | gateway_short | Incohérent |  |  |
| gpt-oss-20b | quick | Réussi | 72 | 21.603 s |
| gpt-oss-20b | stream | Réussi |  | 31.957 s |
| gpt-oss-20b | tools | Réussi |  | 26.096 s |
| nomic-embed-text | context | Hors périmètre sous 65K, incomplet | 2,048 |  |
| nomic-embed-text | quick | Hors périmètre sous 65K, réussite |  | 4.178 s |
| qwen3-14b | context | Hors périmètre sous 65K, incomplet |  | 1800.06 s |
| qwen3-14b | quick | Hors périmètre sous 65K, réussite | 15 | 35.809 s |
| qwen3-14b | stream | Hors périmètre sous 65K, réussite |  | 35.43 s |
| qwen3-14b | tools | Hors périmètre sous 65K, réussite |  | 87.723 s |
| qwen3-8b | context | Hors périmètre sous 65K, exclu |  |  |
| qwen3-8b | quick | Hors périmètre sous 65K, réussite | 15 | 21.293 s |
| qwen3-8b | stream | Hors périmètre sous 65K, incomplet |  | 900.01 s |
| qwen3-8b | tools | Hors périmètre sous 65K, exclu |  |  |
| qwen3.5-9b | context | Réussi | 65,662 | 287.984 s |
| qwen3.5-9b | gateway_context | Réussi | 75,648 | 319.36 s |
| qwen3.5-9b | gateway_short | Réussi | 21 | 72.14 s |
| qwen3.5-9b | quick | Réussi | 15 | 24.635 s |
| qwen3.5-9b | stream | Réussi |  | 143.157 s |
| qwen3.5-9b | tools | Réussi |  | 30.395 s |
| qwen3.5-9b | vision | Réussi | 75 | 27.756 s |
| qwen3.5-9b | vision_context | Réussi | 65,640 | 398.797 s |
| qwen3.5-9b | vision_reverse | Réussi | 75 | 28.645 s |

### Système D

| Étiquette de route du modèle | Contrôle | Résultat | Jetons d'entrée | Durée de requête |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Réussi | 65,590 | 275.395 s |
| gemma-4-12b-it | exact_digest_aperture_65k | Réussi | 72,057 | 300.67 s |
| gemma-4-12b-it | exact_digest_broker_short | Réussi | 34 | 30.74 s |
| gemma-4-12b-it | quick | Réussi | 21 | 15.05 s |
| gemma-4-12b-it | stream | Réussi |  | 14.722 s |
| gemma-4-12b-it | tools | Réussi |  | 33.869 s |
| gemma-4-12b-it | vision | Réussi | 120 | 56.315 s |
| gemma-4-12b-it | vision_context | Réussi | 65,690 | 282.174 s |
| gemma-4-12b-it | vision_reverse | Réussi | 120 | 29.978 s |
| gemma3-4b | context | Réussi | 65,584 | 63.564 s |
| gemma3-4b | exact_digest_65k_recall | Failed | 67,252 | 62.07 s |
| gemma3-4b | quick | Réussi | 15 | 5.151 s |
| gemma3-4b | stream | Réussi |  | 22.552 s |
| gemma3-4b | vision | Réussi | 306 | 8.276 s |
| gemma3-4b | vision_context | Réussi | 65,876 | 67.575 s |
| gemma3-4b | vision_reverse | Réussi | 306 | 5.651 s |
| gpt-oss-20b | context | Réussi | 65,637 | 189.07 s |
| gpt-oss-20b | exact_digest_aperture_65k | Réussi | 72,104 | 245.94 s |
| gpt-oss-20b | exact_digest_broker_short | Réussi | 84 | 15.96 s |
| gpt-oss-20b | quick | Réussi | 72 | 15.431 s |
| gpt-oss-20b | stream | Réussi |  | 31.052 s |
| gpt-oss-20b | tools | Réussi |  | 23.65 s |
| nomic-embed-text | context | Incomplet | 2,048 |  |
| nomic-embed-text | quick | Réussi |  | 2.798 s |
| qwen3-14b | context | Incomplet | 40,939 | 872.209 s |
| qwen3-14b | quick | Réussi | 15 | 36.021 s |
| qwen3-14b | stream | Réussi |  | 33.491 s |
| qwen3-14b | tools | Réussi |  | 82.471 s |
| qwen3-8b | context | Incomplet |  | 1800.07 s |
| qwen3-8b | quick | Réussi | 15 | 19.283 s |
| qwen3-8b | stream | Réussi |  | 19.401 s |
| qwen3-8b | tools | Réussi |  | 65.054 s |
| qwen3.5-9b | context | Réussi | 65,579 | 258.048 s |
| qwen3.5-9b | exact_digest_aperture_65k | Réussi | 81,051 | 324.07 s |
| qwen3.5-9b | exact_digest_broker_short | Réussi | 29 | 94.48 s |
| qwen3.5-9b | quick | Réussi | 15 | 27.16 s |
| qwen3.5-9b | stream | Réussi |  | 28.62 s |
| qwen3.5-9b | tools | Réussi |  | 28.129 s |
| qwen3.5-9b | vision | Réussi | 75 | 25.047 s |
| qwen3.5-9b | vision_context | Réussi | 65,640 | 369.477 s |
| qwen3.5-9b | vision_reverse | Réussi | 75 | 27.602 s |

### Système E

| Étiquette de route du modèle | Contrôle | Résultat | Jetons d'entrée | Durée de requête |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Réussi | 65,590 | 49.086 s |
| gemma-4-e4b-it | quick | Réussi | 21 | 23.911 s |
| gemma-4-e4b-it | stream | Réussi |  | 28.136 s |
| gemma-4-e4b-it | tools | Réussi |  | 56.756 s |
| granite-4.0-h-tiny | context | Réussi | 65,566 |  |
| granite-4.0-h-tiny | quick | Réussi | 35 | 10.408 s |
| granite-4.0-h-tiny | stream | Réussi |  | 27.798 s |
| granite-4.0-h-tiny | tools | Réussi |  | 43.304 s |
| granite-4.2-3b | context | Réussi | 65,589 | 1014.03 s |
| granite-4.2-3b | quick | Réussi | 20 | 14.569 s |
| granite-4.2-3b | stream | Réussi |  | 6.948 s |
| granite-4.2-3b | tools | Réussi |  | 56.376 s |
| qwen3-embedding-0.6b | context | Réussi | 32,767 | 20.387 s |
| qwen3-embedding-0.6b | quick | Réussi | 14 | 9.592 s |
| qwen3.5-0.8b | context | Réussi | 16,429 | 9.128 s |
| qwen3.5-0.8b | quick | Réussi | 17 | 452.417 s |
| qwen3.5-0.8b | stream | Réussi |  | 11.163 s |
| qwen3.5-0.8b | tools | Réussi |  | 39.214 s |
| qwen3.5-2b | context | Réussi | 65,579 | 30.343 s |
| qwen3.5-2b | quick | Réussi | 15 | 12.509 s |
| qwen3.5-2b | stream | Réussi |  | 26.165 s |
| qwen3.5-2b | tools | Réussi |  | 42.056 s |
| qwen3.5-4b | context | Réussi | 65,579 | 53.787 s |
| qwen3.5-4b | quick | Réussi | 15 | 26.736 s |
| qwen3.5-4b | stream | Réussi |  | 26.02 s |
| qwen3.5-4b | tools | Réussi |  | 57.293 s |
| qwen3.5-4b | vision | Réussi | 72 | 10.09 s |
| qwen3.5-4b | vision_context | Réussi | 65,637 | 44.88 s |
| qwen3.5-4b | vision_reverse | Réussi | 72 | 9.96 s |

### Système F

| Étiquette de route du modèle | Contrôle | Résultat | Jetons d'entrée | Durée de requête |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Réussi | 65,590 | 98.443 s |
| gemma-4-e4b-it | quick | Réussi | 21 | 27.51 s |
| gemma-4-e4b-it | stream | Réussi |  | 28.042 s |
| gemma-4-e4b-it | tools | Réussi |  | 73.891 s |
| granite-4.0-h-tiny | context | Réussi | 65,599 | 19.692 s |
| granite-4.0-h-tiny | quick | Réussi | 35 | 43.818 s |
| granite-4.0-h-tiny | stream | Réussi |  | 27.296 s |
| granite-4.0-h-tiny | tools | Réussi |  | 75.377 s |
| granite-4.2-3b | context | Réussi | 65,589 | 145.179 s |
| granite-4.2-3b | quick | Réussi | 20 | 15.703 s |
| granite-4.2-3b | stream | Réussi |  | 35.482 s |
| granite-4.2-3b | tools | Réussi |  | 52.539 s |
| qwen3-embedding-0.6b | context | Réussi | 32,767 | 20.656 s |
| qwen3-embedding-0.6b | quick | Réussi | 14 | 8.122 s |
| qwen3.5-0.8b | context | Réussi | 16,429 | 13.326 s |
| qwen3.5-0.8b | quick | Réussi | 17 | 445.22 s |
| qwen3.5-0.8b | stream | Réussi |  | 13.266 s |
| qwen3.5-0.8b | tools | Réussi |  | 40.825 s |
| qwen3.5-2b | context | Réussi | 65,579 | 61.282 s |
| qwen3.5-2b | quick | Réussi | 15 | 16.738 s |
| qwen3.5-2b | stream | Réussi |  | 25.29 s |
| qwen3.5-2b | tools | Réussi |  | 47.444 s |
| qwen3.5-4b | context | Réussi | 65,579 | 93.753 s |
| qwen3.5-4b | quick | Réussi | 15 | 33.039 s |
| qwen3.5-4b | stream | Réussi |  | 25.658 s |
| qwen3.5-4b | tools | Réussi |  | 71.731 s |
| qwen3.5-4b | vision | Réussi | 70 | 43.053 s |
| qwen3.5-4b | vision_context | Réussi | 65,635 | 84.749 s |
| qwen3.5-4b | vision_reverse | Réussi | 70 | 27.518 s |

### Système G

| Étiquette de route du modèle | Contrôle | Résultat | Jetons d'entrée | Durée de requête |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Réussi | 65,590 | 92.696 s |
| gemma-4-e4b-it | quick | Réussi | 21 | 38.329 s |
| gemma-4-e4b-it | stream | Réussi |  | 43.549 s |
| gemma-4-e4b-it | tools | Réussi |  | 66.616 s |
| granite-4.0-h-tiny | context | Réussi | 65,599 | 69.777 s |
| granite-4.0-h-tiny | quick | Réussi | 35 | 33.17 s |
| granite-4.0-h-tiny | stream | Réussi |  | 31.751 s |
| granite-4.0-h-tiny | tools | Réussi |  | 63.338 s |
| granite-4.2-3b | context | Réussi | 65,589 | 100.849 s |
| granite-4.2-3b | quick | Réussi | 20 | 23.355 s |
| granite-4.2-3b | stream | Réussi |  | 28.75 s |
| granite-4.2-3b | tools | Réussi |  | 44.226 s |
| qwen3-embedding-0.6b | context | Réussi | 32,767 | 23.055 s |
| qwen3-embedding-0.6b | quick | Réussi | 14 | 8.924 s |
| qwen3.5-0.8b | context | Réussi | 16,429 | 16.74 s |
| qwen3.5-0.8b | quick | Réussi | 17 | 504.813 s |
| qwen3.5-0.8b | stream | Réussi |  | 15.095 s |
| qwen3.5-0.8b | tools | Réussi |  | 36.672 s |
| qwen3.5-2b | context | Réussi | 65,579 | 76.731 s |
| qwen3.5-2b | quick | Réussi | 15 | 20.949 s |
| qwen3.5-2b | stream | Réussi |  | 25.194 s |
| qwen3.5-2b | tools | Réussi |  | 37.552 s |
| qwen3.5-4b | context | Réussi | 65,579 | 90.807 s |
| qwen3.5-4b | quick | Réussi | 15 | 41.84 s |
| qwen3.5-4b | stream | Réussi |  | 40.812 s |
| qwen3.5-4b | tools | Réussi |  | 54.999 s |
| qwen3.5-4b | vision | Réussi | 70 | 29.619 s |
| qwen3.5-4b | vision_context | Réussi | 65,635 | 87.496 s |
| qwen3.5-4b | vision_reverse | Réussi | 70 | 26.283 s |

## Comment j'ai testé la viabilité de Hermes

J'ai placé un marqueur synthétique près du début d'une longue invite, puis demandé ce marqueur après le texte de remplissage. La réponse devait renvoyer la valeur attendue. La taille des requêtes était déterminée par le nombre de jetons d'entrée indiqué par le serveur. Un modèle qui répondait normalement après une longue invite échouait tout de même si le marqueur initial était incorrect.

La progression Qwen3.5 35B utilisait des enregistrements numérotés comme remplissage, une température de 0 et des longueurs croissantes de 3 800, 6 800, 10 000 et 13 600 enregistrements. Ces étapes ont renvoyé 69 429, 124 179, 182 579 et 248 279 jetons d'invite. Le modèle est resté chargé entre les étapes, ce qui permettait de réutiliser le préfixe. Les contrôles distincts de Qwen3.6 près de la limite indiquaient zéro jeton en cache.

La longue invite du modèle 0.8B répétait `river stone lantern orchard circuit velvet compass marble` 8 400 fois entre une clé de réponse initiale et une question finale de rappel. L'exécution native envoyait `think:false`, `num_ctx:131072`, `stream:false` et `keep_alive:0`. Le chemin compatible OpenAI utilisait `reasoning_effort:"none"`. Le courtier imposait le mode sans réflexion pour sa route, les clients de la passerelle n'avaient donc pas à modifier la requête.

### Contrôles des outils, de la vision et de la libération

Les tests d'outils vérifiaient la requête ainsi que la réponse reçue après le retour du résultat de l'outil. Un test simple utilisait `add_numbers(7, 11)` et attendait 18. Le test Qwen3.5 35B utilisait `lookup_square` et attendait 49. GPT-OSS recherchait un article en stock et devait intégrer le résultat renvoyé.

Les tests de vision utilisaient des questions sur des images rouges et bleues, inversaient l'ordre des images et inséraient des couleurs d'image ainsi que des marqueurs de début et de fin dans de longues invites. Le test Qwen3.5 35B utilisait un PNG rouge de 256 × 256. Une correction de conversion du contenu image par le courtier était nécessaire avant la réussite de cette requête. Le long test de vision 4B du système E exigeait que les deux marqueurs et l'ordre des couleurs survivent au traitement de l'entrée.

Pendant les longues exécutions, j'ai contrôlé la mémoire GPU, la résidence du modèle, les températures, la pression sur la mémoire hôte, les événements OOM et les erreurs GPU. La protection de Qwen3.5 35B vérifiait aussi la libération après une interruption contrôlée. Les contrôles ultérieurs d'annulation par le client et de requêtes en file d'attente ont exercé le chemin du courtier. Deux requêtes en file d'attente prouvent le traitement des requêtes sous la charge testée, et non l'existence de deux backends GPU simultanés indépendants.

### Interpréter les résultats de performance

Les durées des requêtes incluent le préremplissage des longues entrées et la réponse renvoyée. Elles ne correspondent pas au débit de génération en jetons par seconde. Le délai avant le premier contenu compte pour le flux continu, et les progressions avec préfixe en cache nécessitent une interprétation distincte.

Les exécutions de suivi réussies avec les grands modèles des systèmes A et C utilisaient des périodes d'inférence dédiées, pendant lesquelles le minage était inactif. Les modèles ont été déchargés après ces requêtes. Le minage a repris sur les sept systèmes à la fin de la période de test. Ces résultats décrivent le service des modèles pendant une période d'inférence, et non le minage et l'inférence simultanés.

## Profils de backend utilisés pour les tests

Choisissez le profil associé à la charge que vous souhaitez reproduire. La quantification, le contexte d'exécution, le type de cache, le mode de raisonnement et la répartition des GPU influent tous sur le résultat.

| Système et modèle | Profil de backend testé |
|---|---|
| A, Qwen3.5 35B-A3B Q4_K_M | Ollama 0.34.2, cache KV f16, les deux cartes RTX 5060 Ti de 16 Go, 64 GiB de RAM hôte, contexte d'exécution de 262 144 pour la grande progression. Les requêtes natives utilisaient `think:false`, température 0, flux continu et maintien actif de cinq minutes entre étapes. Les requêtes de passerelle utilisaient le courtier et LiteLLM. Aucune limite de sortie de requête. |
| A, Qwen3.8 27B | llama.cpp à la demande via le courtier et LiteLLM, contexte d'exécution de 262 144, un emplacement d'inférence, cache K/V Q4, les deux cartes RTX 5060 Ti. La requête de 66 007 jetons n'avait aucune limite de sortie. |
| A, Qwen3.6-35B-A3B UD-Q4_K_XL | Strata 0.1.48, contexte de 131 072, cache KV INT8, un GPU sélectionné, limite mémoire de groupe de processus de 55 GiB, limite d'exécution de 30 minutes, chargement différé, déchargement après 60 secondes d'inactivité. Réponse longue pilote : 217 jetons de sortie. Réponse de passerelle près de la limite : 11 jetons de sortie, aucune limite de sortie de requête. |
| A, Qwen3.8-Flash-Next UD-IQ4_XS | Strata 0.1.48, contexte de 98 304, cache KV Q4, cache expert résident de 8 GiB, les deux cartes RTX 5060 Ti. Limite mémoire pilote de 52 GiB, puis 54 GiB pour la route ultérieure. Réponse longue pilote : 10 jetons de sortie. Les combinaisons antérieures avec un contexte et un cache plus grands se sont arrêtées aux limites mémoire. |
| A, Granite 4.2 8B | Poids GGUF Q6_K, processus de travail mutualisé de llama.cpp, contexte de 131 072, cache K/V Q4_0, `--n-predict -1`. La longue requête utilisait une température de 0, la mesure de l’utilisation en flux continu et aucune limite de sortie. |
| A, DeepSeek Coder V2 16B | Poids GGUF Q4_0, Ollama 0.34.2, deux cartes RTX 5060 Ti, 64 GiB de RAM hôte. Les essais séparés avec caches f16, Q4_0 et Q8_0 utilisaient les contextes d'exécution indiqués dans le tableau comparatif. Aucune limite de sortie de requête. |
| B, C, D, service Ollama audité | Ollama 0.34.2, contexte de 131 072, parallélisme 1, un modèle chargé, file d'attente de taille 128, maintien actif à 0, Flash Attention, cache KV Q4_0. |
| B, pilote de passerelle Qwen3.5 9B | Délai d'expiration de route LiteLLM de 1 800 secondes, aucune nouvelle tentative, aucune limite de contexte ni de jetons de sortie. Les deux marqueurs ont été conservés avec 72 265 jetons d'entrée. Le contrôle distinct de reprise du minage a réussi. |
| C, Qwen3.5 0.8B | Poids Q8_0 sur une RTX 2000E Ada avec un profil d'alimentation de 30 W. Contexte d'exécution de 131 072. `think:false` natif, `reasoning_effort:"none"` compatible OpenAI, aucune limite de sortie. L'alias du courtier fixait le contexte d'exécution et imposait le mode sans réflexion. |
| C, Gemma 4 12B-IT | Profil Ollama à un seul GPU, contexte d'exécution de 131 072, requêtes Aperture en flux continu et sans flux continu, sans limite de sortie. L'exécution Aperture directe a culminé à 75 C et 30,64 W avec le profil configuré à 30 W, puis le modèle a été déchargé. |
| D, Qwen3.5 9B, Gemma 4 12B-IT, GPT-OSS 20B | Artefacts installés exacts testés via Aperture, contexte d'exécution de 131 072, résidence complète sur un GPU, fin naturelle sans limite de sortie de requête. |
| E, F, G, processus de conversation llama.cpp | Build 11669, 99 couches GPU, parallélisme 1, Flash Attention, cache K/V Q4_0, `--n-predict -1`. Le contexte d'exécution variait selon la famille de modèles. |

Les profils de service enregistrés décrivent leurs propres configurations d'exécution. Le profil Qwen3.5 35B avec cache f16 testé séparément sur le système A n'hérite pas des réglages de cache Q4_0 des systèmes Ollama plus petits.

### Empreintes des modèles des nouveaux essais d'entrée conservée

Ces identifiants de modèles distinguent les artefacts testés d'autres téléchargements ou alias portant des noms similaires.

| Artefact | Quantification | Empreinte enregistrée ou SHA-256 du fichier |
|---|---|---|
| Étiquette Ollama Qwen3.5 35B-A3B | Q4_K_M | `72aac7c28be8ff9b81c2a270eb489c88e6d822a76ec0cb7bf34d965768848567` |
| Étiquette Ollama Qwen3.5 0.8B de base | Q8_0 | `de63045f29755d4721c09d54c9b45c2dadb644f4fd7d604d4cac90d96049971c` |
| Fichier GGUF Granite 4.2 8B | Q6_K | `5ad3d67f6fe09a448031029bead7f6a088697ca2787c0c5640bf964c59df1a21` |

Les empreintes de manifeste Ollama et les valeurs SHA-256 des fichiers de poids désignent des objets différents. Faites correspondre l'identifiant au type d'artefact du tableau.

## Ce que je lancerais avec Hermes

Je ferais de Qwen3.5 35B la principale route à contexte élevé sur le système à deux RTX 5060 Ti. Son résultat de conservation de 239 153 jetons via la passerelle, ses réussites distinctes avec les outils et la vision, ainsi que la libération vérifiée des requêtes rendent ce choix plus solide qu'un modèle simplement annoncé avec une grande fenêtre de contexte. Je garderais Qwen3.8 27B pour les réponses plus rapides aux requêtes comparables de 66K et Qwen3.6 lorsqu'il est préférable d'utiliser une seule carte.

Sur les systèmes RTX 2000E Ada, je choisirais la route Gemma 3 4B vérifiée du système C pour la charge de réponse à longue entrée testée. J'essaierais la route Qwen3.5 0.8B sans réflexion pour le rappel et l'extraction ciblés. Les routes Gemma, Qwen et GPT-OSS plus grandes conviennent aux tâches qui tolèrent une réponse initiale testée de quatre à cinq minutes. J'exclurais de la sélection la route Gemma 3 défaillante du système D.

Pour les cartes RTX 3060 Ti et RTX 3070 de 8 Go, je commencerais par Qwen3.5 2B ou 4B. Les résultats texte à 65K et les contrôles d'image 4B étayent une configuration de départ utile sans consacrer systématiquement les deux cartes de 16 Go à chaque requête. La pression mémoire de Flash Next et le comportement incomplet à 65K de DeepSeek Coder V2 en font des choix par défaut moins intéressants dans les profils testés.

Les tests appuient ces choix de modèles et de systèmes pour des flux de travail précis. La conservation des entrées, un échange correct avec un outil, la reconnaissance d'image et la libération propre vérifient chacun une partie différente de la viabilité de Hermes. Une configuration fiable doit couvrir les comportements utilisés par votre agent et laisser assez de contexte pour la réponse et les échanges avec les outils.

## Sources et lectures complémentaires

- [Configuration fournisseur et exigences de contexte Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md)
- [Caractéristiques de la NVIDIA GeForce RTX 3060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3060-3060ti/)
- [Caractéristiques de la NVIDIA GeForce RTX 5060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/)
- [Présentation de Hermes Agent](/hermes-local-ai-broker-course/01-hermes-agent-overview/)
- [Choisir un backend de modèle local](/hermes-local-ai-broker-course/02-choose-a-backend/)
