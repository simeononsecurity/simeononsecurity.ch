---
title: "Proves locals de models Hermes: quins conjunts de GPU i model triaria"
date: 2026-10-24
lastmod: 2026-11-15
toc: true
draft: false
description: "Les meves recomanacions per a Hermes parteixen de proves de context llarg, eines, transmissió i visió en sistemes RTX 5060 Ti, RTX 2000E Ada, RTX 3060 Ti i RTX 3070."
genre: ["Intel·ligència artificial", "IA local", "Maquinari"]
tags: ["Hermes Agent", "models lingüístics locals", "proves de LLM", "inferència amb GPU", "RTX 3060 Ti", "RTX 3070", "RTX 2000E Ada", "RTX 5060 Ti", "qualificació de models", "crides a eines", "context llarg", "llama.cpp", "Ollama", "Qwen3.5", "Qwen3.6", "Qwen3.8"]
cover: "/img/cover/hermes-local-model-gpu-benchmarks.webp"
coverAlt: "Il·lustració de targetes gràfiques amb dos ventiladors i de perfil baix al costat del títol Hermes Model Benchmarks sobre fons blau fosc"
coverCaption: ""
---

Per a tasques d'Hermes amb context llarg, començaria amb Qwen3.5 35B en dues RTX 5060 Ti de 16 GB. La ruta va retenir 239.153 tokens d'entrada via LiteLLM i va superar proves separades d'eines, transmissió, visió, cua i cancel·lació. Qwen3.6 és l'alternativa amb una targeta. Als sistemes RTX 3060 Ti i RTX 3070, començaria amb Qwen3.5 2B o 4B.

Aquestes opcions provenen d'executar models per les vies d'inferència de l'agent. Vaig provar la retenció d'entrades llargues, rondes d'eines, respostes transmeses, preguntes d'imatge i alliberament del model. També vaig provar els modes i els ajustos de memòria, perquè carregar un model no demostra la seva utilitat en una petició llarga d'agent.

Hermes necessita almenys 64.000 tokens de context per fer servir eines com a agent. Vaig fixar 65.536 tokens d'entrada reals com a llindar de context llarg. El recompte d'entrada importa més que el context anunciat pel servidor. ([Documentació de proveïdors d'Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md))

## GPU de cada sistema

Les lletres dels sistemes identifiquen aquestes combinacions de maquinari als resultats.

| Sistema | GPU utilitzades al benchmark | Model inicial recomanat |
|---|---|---|
| A | 2 × GeForce RTX 5060 Ti, 16 GB cadascuna | Qwen3.5 35B en ambdues targetes, o Qwen3.6 en una targeta |
| B | 1 × RTX 2000E Ada, 16GB | Qwen3.5 9B si la tasca admet diversos minuts de processament d’entrada llarga |
| C | 1 × RTX 2000E Ada, 16GB | Gemma 3 4B per al camí d’entrada llarga provat; Qwen3.5 0.8B sense raonament per a tasques de record delimitades |
| D | 1 × RTX 2000E Ada, 16GB | Qwen3.5 9B, Gemma 4 12B-IT o GPT-OSS 20B per a les càrregues provades amb models més grans |
| E | 9 × GeForce RTX 3060 Ti, 8 GB cadascuna | Qwen3.5 2B o 4B |
| F | 8 × GeForce RTX 3060 Ti, 8 GB cadascuna | Qwen3.5 2B o 4B |
| G | 3 × GeForce RTX 3070 | Qwen3.5 2B o 4B |

El nombre de targetes instal·lades no vol dir que cada petició fes servir totes les GPU. Les proves Qwen3.5 35B i Flash Next van fer servir les dues targetes del sistema A. Qwen3.6 en va fer servir una. La repetició reeixida de visió Qwen3.5 4B del sistema E va utilitzar una targeta d'una piscina de vuit, mentre la novena va quedar fora de la feina d'IA.

Considera els temps com a resultats del model, runtime i sistema provats. Aquestes execucions comparen configuracions útils, però no aïllen l'arquitectura GPU com a causa de la diferència de velocitat.

## Dues RTX 5060 Ti fan que Qwen3.5 35B sigui la meva opció de context llarg

Qwen3.5 35B va retenir més entrada que els altres. La progressió directa d'Ollama va conservar 248.279 tokens dins un context runtime de 262.144. Una petició transmesa per la passarel·la va retenir 239.153 tokens, retornar el marcador inicial i acabar després de 31 tokens de sortida en 148,12 segons.

El resultat importa per a Hermes perquè la petició va passar pel broker i LiteLLM. Peticions separades van completar una ronda d'eina, reconèixer una imatge vermella i retornar dues respostes correctes quan es van enviar juntes. El broker les va posar a la cua. Tancar la transmissió va alliberar el broker i descarregar el model en 60,31 segons.

| Petició Qwen3.5 35B | Tokens d'entrada | Tokens de sortida | Durada | Resultat |
|---|---:|---:|---:|---|
| Ollama directe, primera fase progressiva | 69,429 | 31 | 38.783 s | Marcador inicial exacte |
| Ollama directe, continuació del prefix compartit | 124,179 | 31 | 28.472 s | Marcador inicial exacte |
| Ollama directe, continuació del prefix compartit | 182,579 | 31 | 38.974 s | Marcador inicial exacte |
| Ollama directe, continuació del prefix compartit | 248,279 | 31 | 54.215 s | Marcador inicial exacte |
| petició de transmissió del broker | 69,427 | 29 | 38.872 s | Marcador inicial exacte |
| petició de transmissió de LiteLLM | 239,153 | 31 | 148.12 s | Marcador inicial exacte, clean unload |

Les peticions progressives reutilitzaven un prefix cada cop més llarg. Els temps descriuen continuació amb prefix calent. Els 54,215 segons no són una mesura en fred independent d'un prompt nou de 248K.

A l'etapa directa més gran, el model va informar d'uns 27.300 milions de bytes residents entre dues GPU. Els pics per targeta van ser 14.964 i 12.386 MiB.

Les temperatures van arribar a 62 i 63 °C, sense error OOM ni Xid. Van quedar 13.865 tokens del context per continuar. La resposta del marcador en va utilitzar 31.

Triaria aquesta ruta quan conservar un conjunt gran importa més que la primera resposta més ràpida. Les proves d'eines i visió mostren conductes d'agent útils; la prova d'entrada llarga comprova la retenció. Són tasques separades.

## Qwen3.6 és l'opció d'una targeta

Qwen3.6-35B-A3B UD-Q4_K_XL va retenir 131.000 tokens en una RTX 5060 Ti. L'altra targeta va quedar inactiva. És una alternativa si no convé dedicar totes dues a un sol model.

| Petició Qwen3.6 a la passarel·la | Tokens d'entrada | Tokens de sortida | Durada | Resultat |
|---|---:|---:|---:|---|
| petició llarga inicial | 66,007 |  | 167.82 s | Marcador inicial conservat |
| petició més llarga | 90,000 | 11 | 159.92 s | Marcador inicial conservat, zero cached input |
| petició més llarga | 119,999 | 11 | 250.61 s | Marcador inicial conservat, zero cached input |
| prop del límit d’execució | 131,000 | 11 | 287.09 s | Marcador inicial conservat, zero cached input |

La petició de 131.000 tokens es va acostar al límit runtime de 131.072. Per a un agent, deixaria més espai per a la resposta i missatges d'eines posteriors. La prova prop del límit mostra tractament d'entrada, no un pressupost recomanable per defecte.

L'ús d'eines va funcionar amb el pensament desactivat. El mode per defecte va consumir els 512 tokens de prova abans de cridar l'eina. El pilot també va superar peticions ràpides, transmeses i de visió. La primera comprovació amb 65.845 tokens va trigar 139,57 segons.

## Qwen3.8 27B guanya la comparació amb 66K coincidents

Per a la mateixa càrrega de 66.007 tokens al sistema A, Qwen3.8 27B va respondre més ràpid. Mantindria aquesta ruta per a peticions de mida semblant i Qwen3.5 35B per a conjunts més grans.

| Ruta del sistema A | Tokens d'entrada | Durada | Resultat |
|---|---:|---:|---|
| Qwen3.8 27B | 66,007 | 54.64 s | Marcador inicial conservat |
| Qwen3.6-35B-A3B UD-Q4_K_XL | 66,007 | 167.82 s | Marcador inicial conservat |
| Qwen3.8-Flash-Next UD-IQ4_XS | 66,007 | 164.58 s | Marcador inicial conservat |
| Flash Next IQ4 compatibility alias | 66,007 | 213.25 s | Marcador conservat |

Qwen3.8 27B va trigar aproximadament un terç dels temps de Qwen3.6 i Flash Next. Són observacions de peticions completes amb runtimes provats, no una comparació només de maquinari.

Les respostes ràpides, la transmissió i les eines també van funcionar. El mode sense pensament va completar la seqüència de colors i la ronda d'eina; la prova amb pensament només en va retornar una part dins el límit de 512 tokens.

Flash Next és menys atractiu per defecte per la pressió de memòria. La prova de 65.847 tokens va passar en 201,41 segons amb context runtime 98.304. Dos perfils previs de context 131.072 van arribar al límit de memòria abans d'estar preparats.

La ruta posterior va arribar al límit cgroup de 54 GiB. Per a feina sense supervisió triaria més marge de memòria.

La ruta anomenada `flash-iq2` feia servir el backend de compatibilitat IQ4 de Flash Next. El nom no indica un resultat IQ2.

## La RTX 2000E Ada gestiona entrades llargues, però l'elecció del model canvia l'espera

Gemma 3 4B és la meva ruta provada preferida d'entrada llarga al sistema C. Dues vies van retenir més de 84K tokens en uns 88 segons. Els models més grans també van superar proves de retenció, però van trigar minuts.

| Sistema | Model i via | Tokens d'entrada | Durada | Resultat |
|---|---|---:|---:|---|
| B | Qwen3.5 9B, passarel·la | 72,265 | 263 s | S'han conservat els dos marcadors; prova posterior de recuperació de mineria superada |
| C | Gemma 3 4B, passarel·la | 84,044 | 88.05 s | Marcador inicial conservat |
| C | Gemma 3 4B, Aperture | 84,045 | 87.68 s | Marcador inicial conservat |
| C | Gemma 4 12B-IT, passarel·la | 67,254 | 263.07 s | Marcador inicial conservat |
| C | Gemma 4 12B-IT, Aperture sense transmissió | 67,255 | 274.24 s | Marcador inicial conservat |
| C | Gemma 4 12B-IT, transmissió d’Aperture | 67,255 | 282.16 s | Marcador inicial conservat |
| C | Qwen3.5 9B, passarel·la | 75,648 | 319.36 s | Marcador inicial conservat, model descarregat de la memòria |
| C | GPT-OSS 20B, passarel·la | 84,099 | 315.83 s | Marcador inicial conservat, model descarregat de la memòria |
| D | Qwen3.5 9B, Aperture | 81,051 | 324.07 s | Retenció superada amb l'artefacte instal·lat |
| D | Gemma 4 12B-IT, Aperture | 72,057 | 300.67 s | Retenció superada amb l'artefacte instal·lat |
| D | GPT-OSS 20B, Aperture | 72,104 | 245.94 s | Retenció superada amb l'artefacte instal·lat |

La transmissió no va eliminar l'espera de preompliment de Gemma 4 al sistema C. El primer contingut va arribar després de 277,49 segons, més tard que la resposta sense transmissió de 274,24. Una prova anterior va esgotar el temps abans de la repetició reeixida. Reservaria la ruta per a tasques que admetin minuts de processament inicial.

Gemma 3 4B mostra per què la qualificació depèn del sistema. El sistema D va perdre el marcador inicial en dues proves de record 65K, inclosa una repetició amb temperatura zero i 67.252 tokens. La petició determinista va acabar en 62,07 segons amb residència completa a GPU.

La finalització ràpida i una resposta API normal no van fer correcta la resposta. Faria servir la ruta reeixida del sistema C i exclouria la fallida del sistema D d'Hermes.

## El mode de pensament determina si Qwen3.5 0.8B és útil

Qwen3.5 0.8B va ser un candidat útil per a record acotat al sistema C després de desactivar el pensament. El model Q8_0 va retenir 75.649 tokens via passarel·la en 65,92 segons. Això correspon a l'artefacte i la ruta provats, no a les configuracions antigues de 16K.

| Petició Qwen3.5 0.8B al sistema C | Tokens d'entrada | Tokens de sortida | Durada | Resultat |
|---|---:|---:|---:|---|
| diagnòstic breu amb raonament predeterminat | 9,050 | 3,391 | 66.56 s | Marcador inicial exacte |
| raonament desactivat, diagnòstic equivalent | 9,055 | 21 | 7.65 s | Marcador inicial exacte, no reasoning text |
| intent llarg amb raonament predeterminat |  |  | Temps d'espera exhaurit als 600 s | Cap resposta completada |
| raonament desactivat, Ollama natiu | 75,656 | 22 | 69.80 s | Marcador inicial exacte |
| punt final compatible amb OpenAI sense raonament | 75,646 | 12 | 69.09 s | Marcador inicial exacte |
| Broker amb mode sense raonament imposat | 75,647 | 13 | 66.83 s | Marcador inicial exacte |
| LiteLLM del sistema A al sistema C | 75,649 | 15 | 65.92 s | Marcador inicial exacte |

El diagnòstic coincident va baixar de 66,56 a 7,65 segons, unes 8,7 vegades més ràpid, i la sortida de 3.391 a 21 tokens. Per això fixaria el mode de raonament en tasques simples d'extracció i encaminament. El mode per defecte va gastar esforç en sortida innecessària.

Una prova compatible amb OpenAI no va trobar el marcador; la repetició amb temperatura zero sí. Les rutes reeixides feien servir el mode sense pensament i acabaven sense límit de sortida. Tres passarel·les més van passar proves breus en 4,22, 4,37 i 3,85 segons. Això comprova l'encaminament; els 75.649 tokens demostren retenció d'entrada llarga.

Provaria aquesta ruta per a record i extracció acotats. Per al raonament obert triaria un model més gran. Recuperar un marcador sintètic és més limitat que planificar, programar o coordinar eines.

## Els sistemes RTX 3060 Ti i RTX 3070 afavoreixen Qwen3.5 2B i 4B

Qwen3.5 2B i 4B són opcions pràctiques per a targetes de 8 GB. Les proves de text als sistemes E, F i G van passar amb 65.579 tokens i van trigar de 30,343 a 93,753 segons. Les rutes 4B també van superar proves d'eines, transmissió i imatge.

La repetició de visió 4B del sistema E va retenir dos marcadors i l'ordre de colors amb 65.637 tokens en 44,88 segons. També van funcionar els ordres normal i invers. Es va fer servir una targeta sana després que una altra patís un error Xid 79 i el sistema es reiniciés.

| Sistema | Context textual Qwen3.5 2B | Context textual Qwen3.5 4B | Context visual Qwen3.5 4B |
|---|---|---|---|
| E, RTX 3060 Ti pool | 65,579 tokens, 30.343 s | 65,579 tokens, 53.787 s | 65,637 tokens, 44.88 s |
| F, RTX 3060 Ti pool | 65,579 tokens, 61.282 s | 65,579 tokens, 93.753 s | 65,635 tokens, 84.749 s |
| G, RTX 3070 pool | 65,579 tokens, 76.731 s | 65,579 tokens, 90.807 s | 65,635 tokens, 87.496 s |

Cada sistema va registrar 29 proves reeixides. La variació entre els dos sistemes RTX 3060 Ti mostra per què triaria un perfil provat en lloc d'ordenar les targetes per aquests temps.

Els set sistemes van tornar a minar després de la finestra d'inferència. La recuperació del sistema B va passar amb noves participacions acceptades. La targeta fallida del sistema E va tornar a minar després d'un reinici i reforçar l'enllaç PCIe, però continuà exclosa de la piscina d'IA. Això és diferent del retorn automàtic després d'una petició.

## Carregar un model no el qualifica

Exclouria DeepSeek Coder V2 16B de les opcions Hermes 65K provades. La memòria f16 va retenir 50.477 tokens, però la prova 65K va arribar al límit VRAM. Les alternatives Q4 i Q8 van carregar els pesos i després van topar amb límits de memòria de l'amfitrió o rendiment baix amb prompts llargs.

| Perfil de memòria cau DeepSeek Coder V2 | Context runtime | Resultat observat | Valoració |
|---|---:|---|---|
| f16 | 81,920 | recuperació de 50.477 tokens correcta, petició excessiva rebutjada | Resultat útil amb context més curt |
| f16 | 73,728 | emplenament previ per a 65K aturat amb 15.802 MiB d’ús de GPU | No qualificat per a 65K |
| Q4_0 | 98,304 | El preompliment llarg va baixar a 96.72 tokens/s abans de l’aturada controlada | Poc adequat per a aquesta càrrega |
| Q8_0 | 77,824 | El preompliment llarg va baixar a 120.12 tokens/s abans de l’aturada controlada | Poc adequat per a aquesta càrrega |
| Q4_0 / Q8_0, perfils més grans | 163,840 / 98,304 | Les proteccions de memòria de l’amfitrió van aturar les proves | L’ajust de memòria depèn de tot el sistema |

La lliçó pràctica és provar la petició prevista. La presència a GPU, una resposta curta i un context configurat gran no demostren retenció d'entrada llarga amb latència útil.

Granite 4.2 8B i GPT-OSS 20B van millorar després de seguiment específic de ruta al sistema A. Granite Q6_K va retenir 66.082 tokens en 88,636 segons sense entrada en memòria cau. GPT-OSS va completar la ronda després de corregir el broker: 9,854 segons per a la crida i 9,849 per al seguiment. Mantindria aquests resultats separats de les proves incompletes.

## Resultats complets del benchmark

La taula conté 295 proves en 59 combinacions de models i sistemes. Registra 273 proves superades, una prova de record fallida i set resultats incomplets, incoherents o incompatibles. Catorze proves queden fora de l'abast 65K. Cada fila mostra el resultat mesurat.

Les recomanacions s'apliquen a les rutes i càrregues superades. Una fila fallida o incompleta no qualifica el comportament corresponent.

Les proves de context curt i embeddings corresponen a les seves càrregues. Superar context 16K o 32K no qualifica per a la càrrega Hermes de 65.536 tokens. Els noms són etiquetes de ruta. `flash-iq2` feia servir el backend IQ4.

La fila de context Qwen3.5 35B del sistema A és l'última etapa de prefix compartit. Els temps d'eina amb signe més separen la crida i el seguiment.

La fila de concurrència dona els temps de dues peticions en cua. La de cancel·lació mostra l'alliberament després de tancar el client. Les progressions de context i comparacions Qwen3.5 0.8B tenen taules pròpies.

### Sistema A

| Ruta del model | Prova | Resultat | Tokens d'entrada | Durada de petició |
|---|---|---|---:|---:|
| bonsai-2-27b | context | Correcte | 65,621 | 88.746 s |
| bonsai-2-27b | quick | Correcte | 57 | 6.429 s |
| bonsai-2-27b | stream | Correcte |  | 9.371 s |
| bonsai-2-27b | tools | Correcte |  | 10.478 s |
| deepseek-coder-v2:16b | context | Incompatible | 50,477 |  |
| deepseek-coder-v2:16b | quick | Correcte | 77 | 43.239 s |
| flash-iq2 | context | Correcte | 66,007 | 213.25 s |
| flash-iq2 | quick | Correcte |  | 56.03 s |
| flash-iq2 | stream | Correcte |  | 1.35 s |
| flash-iq2 | tools | Correcte |  | 16.55 s |
| gemma-4-12b-it | context | Correcte | 65,590 | 51.225 s |
| gemma-4-12b-it | quick | Correcte | 21 | 5.166 s |
| gemma-4-12b-it | stream | Correcte |  | 4.653 s |
| gemma-4-12b-it | tools | Correcte |  | 18.72 s |
| gemma-4-12b-it | vision | Correcte | 115 | 7.222 s |
| gemma-4-12b-it | vision_context | Correcte | 65,685 | 56.06 s |
| gemma-4-12b-it | vision_reverse | Correcte | 115 | 7.467 s |
| gemma-4-e4b-it | context | Correcte | 65,590 | 21.889 s |
| gemma-4-e4b-it | quick | Correcte | 21 | 17.919 s |
| gemma-4-e4b-it | stream | Correcte |  | 4.25 s |
| gemma-4-e4b-it | tools | Correcte |  | 8.734 s |
| gpt-oss-20b | context | Correcte | 65,637 | 159.155 s |
| gpt-oss-20b | quick | Correcte | 73 | 10.548 s |
| gpt-oss-20b | stream | Correcte |  | 20.594 s |
| gpt-oss-20b | tools | Correcte |  | 9.854 + 9.849 s |
| granite-4.2-3b | context | Correcte | 65,589 | 70.968 s |
| granite-4.2-3b | quick | Correcte | 20 | 4.009 s |
| granite-4.2-3b | stream | Correcte |  | 5.365 s |
| granite-4.2-3b | tools | Correcte |  | 6.086 s |
| granite-4.2-8b | context | Correcte | 66,082 | 88.636 s |
| granite-4.2-8b | quick | Correcte | 20 | 5.857 s |
| granite-4.2-8b | stream | Correcte |  | 11.826 s |
| granite-4.2-8b | tools | Correcte |  | 11.852 s |
| qwen27b | context | Correcte | 66,007 | 54.64 s |
| qwen27b | quick | Correcte | 57 | 31.5 s |
| qwen27b | stream | Correcte |  | 0.92 s |
| qwen27b | tools | Correcte |  | 4.25 s |
| qwen3-embedding-0.6b | context | Correcte | 32,767 | 7.736 s |
| qwen3-embedding-0.6b | quick | Correcte | 14 | 2.125 s |
| qwen3.5-0.8b | context | Correcte | 16,429 | 10.5 s |
| qwen3.5-0.8b | quick | Correcte | 17 | 14.316 s |
| qwen3.5-0.8b | stream | Correcte |  | 2.125 s |
| qwen3.5-0.8b | tools | Correcte |  | 4.416 s |
| qwen3.5-2b | context | Correcte | 65,581 | 11.175 s |
| qwen3.5-2b | quick | Correcte | 17 | 4.519 s |
| qwen3.5-2b | stream | Correcte |  | 3.736 s |
| qwen3.5-2b | tools | Correcte |  | 5.046 s |
| qwen3.5-4b | context | Correcte | 65,579 | 36.451 s |
| qwen3.5-4b | quick | Correcte | 15 | 19.935 s |
| qwen3.5-4b | stream | Correcte |  | 17.496 s |
| qwen3.5-4b | tools | Correcte |  | 7.308 s |
| qwen3.5-4b | vision | Correcte | 70 | 7.848 s |
| qwen3.5-4b | vision_context | Correcte | 65,635 | 28.24 s |
| qwen3.5-4b | vision_reverse | Correcte | 70 | 4.386 s |
| qwen3.5-9b | context | Correcte | 65,581 | 34.139 s |
| qwen3.5-9b | quick | Correcte | 17 | 3.88 s |
| qwen3.5-9b | stream | Correcte |  | 3.378 s |
| qwen3.5-9b | tools | Correcte |  | 10.204 s |
| qwen3.5-9b | vision | Correcte | 72 | 4.441 s |
| qwen3.5-9b | vision_context | Correcte | 65,637 | 33.745 s |
| qwen3.5-9b | vision_reverse | Correcte | 72 | 3.97 s |
| qwen3.5:35b-a3b-q4_K_M | cancellation | Correcte |  | 60.31 s |
| qwen3.5:35b-a3b-q4_K_M | concurrency | Correcte |  | 26.23 / 25.33 s |
| qwen3.5:35b-a3b-q4_K_M | context | Correcte | 248,279 | 54.215 s |
| qwen3.5:35b-a3b-q4_K_M | gateway | Correcte | 239,153 | 148.12 s |
| qwen3.5:35b-a3b-q4_K_M | quick | Correcte | 79 | 10.08 s |
| qwen3.5:35b-a3b-q4_K_M | stream | Correcte | 69,429 | 38.783 s |
| qwen3.5:35b-a3b-q4_K_M | tools | Correcte |  | 15.22 + 14.83 s |
| qwen3.5:35b-a3b-q4_K_M | vision | Correcte |  | 18.39 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | context | Correcte | 65,845 | 139.57 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | quick | Correcte | 15 | 3.97 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | stream | Correcte |  | 0.45 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | tools | Correcte | 293 | 5.48 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | vision | Correcte | 38 | 0.59 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | context | Correcte | 65,847 | 201.41 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | quick | Correcte | 17 | 54.62 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | stream | Correcte |  | 1.2 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | tools | Correcte |  | 22.18 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | vision | Correcte |  | 3.86 s |

### Sistema B

| Ruta del model | Prova | Resultat | Tokens d'entrada | Durada de petició |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Correcte | 65,590 | 299.163 s |
| gemma-4-12b-it | quick | Correcte | 21 | 15.261 s |
| gemma-4-12b-it | stream | Correcte |  | 148.792 s |
| gemma-4-12b-it | tools | Correcte |  | 34.124 s |
| gemma-4-12b-it | vision | Correcte | 120 | 61.455 s |
| gemma-4-12b-it | vision_context | Correcte | 65,690 | 295.581 s |
| gemma-4-12b-it | vision_reverse | Correcte | 120 | 32.511 s |
| gemma3-4b | context | Correcte | 65,584 | 67.382 s |
| gemma3-4b | quick | Correcte | 15 | 6.329 s |
| gemma3-4b | stream | Correcte |  | 24.138 s |
| gemma3-4b | vision | Correcte | 306 | 7.018 s |
| gemma3-4b | vision_context | Correcte | 65,876 | 70.912 s |
| gemma3-4b | vision_reverse | Correcte | 306 | 5.762 s |
| gpt-oss-20b | context | Correcte | 65,637 | 206.767 s |
| gpt-oss-20b | quick | Correcte | 72 | 16.583 s |
| gpt-oss-20b | stream | Correcte |  | 32.075 s |
| gpt-oss-20b | tools | Correcte |  | 28.102 s |
| nomic-embed-text | context | Incomplet | 2,048 |  |
| nomic-embed-text | quick | Correcte |  | 7.117 s |
| qwen3-14b | context | Incomplet |  | 1800.09 s |
| qwen3-14b | quick | Correcte | 15 | 37.199 s |
| qwen3-14b | stream | Correcte |  | 35.471 s |
| qwen3-14b | tools | Correcte |  | 87.554 s |
| qwen3-8b | context | Exclòs de l'abast 65K |  |  |
| qwen3-8b | quick | Prova superada fora de l'abast 65K | 15 | 21.059 s |
| qwen3-8b | stream | Exclòs de l'abast 65K |  |  |
| qwen3-8b | tools | Exclòs de l'abast 65K |  |  |
| qwen3.5-9b | context | Correcte | 65,579 | 282.796 s |
| qwen3.5-9b | litellm_long_route | Correcte | 72,265 | 263 s |
| qwen3.5-9b | post_external_stop_mining | Correcte |  |  |
| qwen3.5-9b | quick | Correcte | 15 | 25.881 s |
| qwen3.5-9b | stream | Correcte |  | 143.44 s |
| qwen3.5-9b | tools | Correcte |  | 31.812 s |
| qwen3.5-9b | vision | Correcte | 75 | 32.015 s |
| qwen3.5-9b | vision_context | Correcte | 65,640 | 396.288 s |
| qwen3.5-9b | vision_reverse | Correcte | 75 | 28.626 s |

### Sistema C

| Ruta del model | Prova | Resultat | Tokens d'entrada | Durada de petició |
|---|---|---|---:|---:|
| gemma-4-12b-it | aperture_context | Correcte | 67,255 | 274.24 s |
| gemma-4-12b-it | aperture_short | Correcte | 35 | 39.32 s |
| gemma-4-12b-it | aperture_stream_context | Correcte | 67,255 | 282.16 s |
| gemma-4-12b-it | context | Correcte | 65,670 | 313.661 s |
| gemma-4-12b-it | gateway_context | Correcte | 67,254 | 263.07 s |
| gemma-4-12b-it | gateway_short | Correcte | 27 | 20.98 s |
| gemma-4-12b-it | quick | Correcte | 21 | 16.447 s |
| gemma-4-12b-it | stream | Correcte |  | 15.175 s |
| gemma-4-12b-it | tools | Correcte |  | 37.821 s |
| gemma-4-12b-it | vision | Correcte | 120 | 58.52 s |
| gemma-4-12b-it | vision_context | Correcte | 65,690 | 308.759 s |
| gemma-4-12b-it | vision_reverse | Correcte | 120 | 31.25 s |
| gemma3-4b | aperture_context | Correcte | 84,045 | 87.68 s |
| gemma3-4b | aperture_after_system_d_route_change | Correcte | 24 | 5.42 s |
| gemma3-4b | aperture_short | Correcte | 22 | 5.45 s |
| gemma3-4b | aperture_stream | Correcte |  | 3.72 s |
| gemma3-4b | context | Correcte | 65,664 | 67.543 s |
| gemma3-4b | gateway_context | Correcte | 84,044 | 88.05 s |
| gemma3-4b | gateway_short_via_system_a | Correcte |  | 3.16 s |
| gemma3-4b | gateway_short_via_system_e | Correcte |  |  |
| gemma3-4b | gateway_short_via_system_f | Correcte |  | 4.15 s |
| gemma3-4b | gateway_short_via_system_g | Correcte |  | 6.06 s |
| gemma3-4b | quick | Correcte | 15 | 5.163 s |
| gemma3-4b | stream | Correcte |  | 24.691 s |
| gemma3-4b | vision | Correcte | 306 | 7.318 s |
| gemma3-4b | vision_context | Correcte | 65,876 | 72.476 s |
| gemma3-4b | vision_reverse | Correcte | 306 | 5.831 s |
| gpt-oss-20b | context | Correcte | 65,716 | 216.594 s |
| gpt-oss-20b | gateway_context | Correcte | 84,099 | 315.83 s |
| gpt-oss-20b | gateway_short | Inconsistent |  |  |
| gpt-oss-20b | quick | Correcte | 72 | 21.603 s |
| gpt-oss-20b | stream | Correcte |  | 31.957 s |
| gpt-oss-20b | tools | Correcte |  | 26.096 s |
| nomic-embed-text | context | Incomplet fora de l'abast 65K | 2,048 |  |
| nomic-embed-text | quick | Prova superada fora de l'abast 65K |  | 4.178 s |
| qwen3-14b | context | Incomplet fora de l'abast 65K |  | 1800.06 s |
| qwen3-14b | quick | Prova superada fora de l'abast 65K | 15 | 35.809 s |
| qwen3-14b | stream | Prova superada fora de l'abast 65K |  | 35.43 s |
| qwen3-14b | tools | Prova superada fora de l'abast 65K |  | 87.723 s |
| qwen3-8b | context | Exclòs de l'abast 65K |  |  |
| qwen3-8b | quick | Prova superada fora de l'abast 65K | 15 | 21.293 s |
| qwen3-8b | stream | Incomplet fora de l'abast 65K |  | 900.01 s |
| qwen3-8b | tools | Exclòs de l'abast 65K |  |  |
| qwen3.5-9b | context | Correcte | 65,662 | 287.984 s |
| qwen3.5-9b | gateway_context | Correcte | 75,648 | 319.36 s |
| qwen3.5-9b | gateway_short | Correcte | 21 | 72.14 s |
| qwen3.5-9b | quick | Correcte | 15 | 24.635 s |
| qwen3.5-9b | stream | Correcte |  | 143.157 s |
| qwen3.5-9b | tools | Correcte |  | 30.395 s |
| qwen3.5-9b | vision | Correcte | 75 | 27.756 s |
| qwen3.5-9b | vision_context | Correcte | 65,640 | 398.797 s |
| qwen3.5-9b | vision_reverse | Correcte | 75 | 28.645 s |

### Sistema D

| Ruta del model | Prova | Resultat | Tokens d'entrada | Durada de petició |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Correcte | 65,590 | 275.395 s |
| gemma-4-12b-it | exact_digest_aperture_65k | Correcte | 72,057 | 300.67 s |
| gemma-4-12b-it | exact_digest_broker_short | Correcte | 34 | 30.74 s |
| gemma-4-12b-it | quick | Correcte | 21 | 15.05 s |
| gemma-4-12b-it | stream | Correcte |  | 14.722 s |
| gemma-4-12b-it | tools | Correcte |  | 33.869 s |
| gemma-4-12b-it | vision | Correcte | 120 | 56.315 s |
| gemma-4-12b-it | vision_context | Correcte | 65,690 | 282.174 s |
| gemma-4-12b-it | vision_reverse | Correcte | 120 | 29.978 s |
| gemma3-4b | context | Correcte | 65,584 | 63.564 s |
| gemma3-4b | exact_digest_65k_recall | Fallit | 67,252 | 62.07 s |
| gemma3-4b | quick | Correcte | 15 | 5.151 s |
| gemma3-4b | stream | Correcte |  | 22.552 s |
| gemma3-4b | vision | Correcte | 306 | 8.276 s |
| gemma3-4b | vision_context | Correcte | 65,876 | 67.575 s |
| gemma3-4b | vision_reverse | Correcte | 306 | 5.651 s |
| gpt-oss-20b | context | Correcte | 65,637 | 189.07 s |
| gpt-oss-20b | exact_digest_aperture_65k | Correcte | 72,104 | 245.94 s |
| gpt-oss-20b | exact_digest_broker_short | Correcte | 84 | 15.96 s |
| gpt-oss-20b | quick | Correcte | 72 | 15.431 s |
| gpt-oss-20b | stream | Correcte |  | 31.052 s |
| gpt-oss-20b | tools | Correcte |  | 23.65 s |
| nomic-embed-text | context | Incomplet | 2,048 |  |
| nomic-embed-text | quick | Correcte |  | 2.798 s |
| qwen3-14b | context | Incomplet | 40,939 | 872.209 s |
| qwen3-14b | quick | Correcte | 15 | 36.021 s |
| qwen3-14b | stream | Correcte |  | 33.491 s |
| qwen3-14b | tools | Correcte |  | 82.471 s |
| qwen3-8b | context | Incomplet |  | 1800.07 s |
| qwen3-8b | quick | Correcte | 15 | 19.283 s |
| qwen3-8b | stream | Correcte |  | 19.401 s |
| qwen3-8b | tools | Correcte |  | 65.054 s |
| qwen3.5-9b | context | Correcte | 65,579 | 258.048 s |
| qwen3.5-9b | exact_digest_aperture_65k | Correcte | 81,051 | 324.07 s |
| qwen3.5-9b | exact_digest_broker_short | Correcte | 29 | 94.48 s |
| qwen3.5-9b | quick | Correcte | 15 | 27.16 s |
| qwen3.5-9b | stream | Correcte |  | 28.62 s |
| qwen3.5-9b | tools | Correcte |  | 28.129 s |
| qwen3.5-9b | vision | Correcte | 75 | 25.047 s |
| qwen3.5-9b | vision_context | Correcte | 65,640 | 369.477 s |
| qwen3.5-9b | vision_reverse | Correcte | 75 | 27.602 s |

### Sistema E

| Ruta del model | Prova | Resultat | Tokens d'entrada | Durada de petició |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Correcte | 65,590 | 49.086 s |
| gemma-4-e4b-it | quick | Correcte | 21 | 23.911 s |
| gemma-4-e4b-it | stream | Correcte |  | 28.136 s |
| gemma-4-e4b-it | tools | Correcte |  | 56.756 s |
| granite-4.0-h-tiny | context | Correcte | 65,566 |  |
| granite-4.0-h-tiny | quick | Correcte | 35 | 10.408 s |
| granite-4.0-h-tiny | stream | Correcte |  | 27.798 s |
| granite-4.0-h-tiny | tools | Correcte |  | 43.304 s |
| granite-4.2-3b | context | Correcte | 65,589 | 1014.03 s |
| granite-4.2-3b | quick | Correcte | 20 | 14.569 s |
| granite-4.2-3b | stream | Correcte |  | 6.948 s |
| granite-4.2-3b | tools | Correcte |  | 56.376 s |
| qwen3-embedding-0.6b | context | Correcte | 32,767 | 20.387 s |
| qwen3-embedding-0.6b | quick | Correcte | 14 | 9.592 s |
| qwen3.5-0.8b | context | Correcte | 16,429 | 9.128 s |
| qwen3.5-0.8b | quick | Correcte | 17 | 452.417 s |
| qwen3.5-0.8b | stream | Correcte |  | 11.163 s |
| qwen3.5-0.8b | tools | Correcte |  | 39.214 s |
| qwen3.5-2b | context | Correcte | 65,579 | 30.343 s |
| qwen3.5-2b | quick | Correcte | 15 | 12.509 s |
| qwen3.5-2b | stream | Correcte |  | 26.165 s |
| qwen3.5-2b | tools | Correcte |  | 42.056 s |
| qwen3.5-4b | context | Correcte | 65,579 | 53.787 s |
| qwen3.5-4b | quick | Correcte | 15 | 26.736 s |
| qwen3.5-4b | stream | Correcte |  | 26.02 s |
| qwen3.5-4b | tools | Correcte |  | 57.293 s |
| qwen3.5-4b | vision | Correcte | 72 | 10.09 s |
| qwen3.5-4b | vision_context | Correcte | 65,637 | 44.88 s |
| qwen3.5-4b | vision_reverse | Correcte | 72 | 9.96 s |

### Sistema F

| Ruta del model | Prova | Resultat | Tokens d'entrada | Durada de petició |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Correcte | 65,590 | 98.443 s |
| gemma-4-e4b-it | quick | Correcte | 21 | 27.51 s |
| gemma-4-e4b-it | stream | Correcte |  | 28.042 s |
| gemma-4-e4b-it | tools | Correcte |  | 73.891 s |
| granite-4.0-h-tiny | context | Correcte | 65,599 | 19.692 s |
| granite-4.0-h-tiny | quick | Correcte | 35 | 43.818 s |
| granite-4.0-h-tiny | stream | Correcte |  | 27.296 s |
| granite-4.0-h-tiny | tools | Correcte |  | 75.377 s |
| granite-4.2-3b | context | Correcte | 65,589 | 145.179 s |
| granite-4.2-3b | quick | Correcte | 20 | 15.703 s |
| granite-4.2-3b | stream | Correcte |  | 35.482 s |
| granite-4.2-3b | tools | Correcte |  | 52.539 s |
| qwen3-embedding-0.6b | context | Correcte | 32,767 | 20.656 s |
| qwen3-embedding-0.6b | quick | Correcte | 14 | 8.122 s |
| qwen3.5-0.8b | context | Correcte | 16,429 | 13.326 s |
| qwen3.5-0.8b | quick | Correcte | 17 | 445.22 s |
| qwen3.5-0.8b | stream | Correcte |  | 13.266 s |
| qwen3.5-0.8b | tools | Correcte |  | 40.825 s |
| qwen3.5-2b | context | Correcte | 65,579 | 61.282 s |
| qwen3.5-2b | quick | Correcte | 15 | 16.738 s |
| qwen3.5-2b | stream | Correcte |  | 25.29 s |
| qwen3.5-2b | tools | Correcte |  | 47.444 s |
| qwen3.5-4b | context | Correcte | 65,579 | 93.753 s |
| qwen3.5-4b | quick | Correcte | 15 | 33.039 s |
| qwen3.5-4b | stream | Correcte |  | 25.658 s |
| qwen3.5-4b | tools | Correcte |  | 71.731 s |
| qwen3.5-4b | vision | Correcte | 70 | 43.053 s |
| qwen3.5-4b | vision_context | Correcte | 65,635 | 84.749 s |
| qwen3.5-4b | vision_reverse | Correcte | 70 | 27.518 s |

### Sistema G

| Ruta del model | Prova | Resultat | Tokens d'entrada | Durada de petició |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Correcte | 65,590 | 92.696 s |
| gemma-4-e4b-it | quick | Correcte | 21 | 38.329 s |
| gemma-4-e4b-it | stream | Correcte |  | 43.549 s |
| gemma-4-e4b-it | tools | Correcte |  | 66.616 s |
| granite-4.0-h-tiny | context | Correcte | 65,599 | 69.777 s |
| granite-4.0-h-tiny | quick | Correcte | 35 | 33.17 s |
| granite-4.0-h-tiny | stream | Correcte |  | 31.751 s |
| granite-4.0-h-tiny | tools | Correcte |  | 63.338 s |
| granite-4.2-3b | context | Correcte | 65,589 | 100.849 s |
| granite-4.2-3b | quick | Correcte | 20 | 23.355 s |
| granite-4.2-3b | stream | Correcte |  | 28.75 s |
| granite-4.2-3b | tools | Correcte |  | 44.226 s |
| qwen3-embedding-0.6b | context | Correcte | 32,767 | 23.055 s |
| qwen3-embedding-0.6b | quick | Correcte | 14 | 8.924 s |
| qwen3.5-0.8b | context | Correcte | 16,429 | 16.74 s |
| qwen3.5-0.8b | quick | Correcte | 17 | 504.813 s |
| qwen3.5-0.8b | stream | Correcte |  | 15.095 s |
| qwen3.5-0.8b | tools | Correcte |  | 36.672 s |
| qwen3.5-2b | context | Correcte | 65,579 | 76.731 s |
| qwen3.5-2b | quick | Correcte | 15 | 20.949 s |
| qwen3.5-2b | stream | Correcte |  | 25.194 s |
| qwen3.5-2b | tools | Correcte |  | 37.552 s |
| qwen3.5-4b | context | Correcte | 65,579 | 90.807 s |
| qwen3.5-4b | quick | Correcte | 15 | 41.84 s |
| qwen3.5-4b | stream | Correcte |  | 40.812 s |
| qwen3.5-4b | tools | Correcte |  | 54.999 s |
| qwen3.5-4b | vision | Correcte | 70 | 29.619 s |
| qwen3.5-4b | vision_context | Correcte | 65,635 | 87.496 s |
| qwen3.5-4b | vision_reverse | Correcte | 70 | 26.283 s |

## Com vaig provar la viabilitat d'Hermes

Vaig col·locar un marcador sintètic prop de l'inici d'un prompt llarg i vaig demanar que es retornés després del text de farciment. La resposta havia de coincidir amb el valor esperat. Els tokens reportats pel servidor fixaven la mida. Un model podia respondre normalment i fallar si el marcador inicial era incorrecte.

La progressió Qwen3.5 35B va fer servir registres numerats, temperatura 0 i longituds de 3.800, 6.800, 10.000 i 13.600 registres. Van retornar 69.429, 124.179, 182.579 i 248.279 tokens. El model va continuar carregat entre etapes, reutilitzant el prefix. Les proves Qwen3.6 prop del límit van reportar zero tokens en memòria cau.

El prompt llarg 0.8B repetia `river stone lantern orchard circuit velvet compass marble` 8.400 vegades entre una clau inicial i la pregunta final. L'execució nativa enviava `think:false`, `num_ctx:131072`, `stream:false` i `keep_alive:0`. La ruta OpenAI feia servir `reasoning_effort:"none"`. El broker imposava el mode sense pensament.

### Proves d'eines, visió i alliberament

Les proves d'eines comprovaven la petició i la resposta després de rebre'n el resultat. Una prova feia servir `add_numbers(7, 11)` i esperava 18. Qwen3.5 35B feia servir `lookup_square` i esperava 49. GPT-OSS consultava l'inventari i havia d'incorporar el resultat.

Les proves de visió preguntaven per imatges vermelles i blaves, ordre invers i prompts llargs amb colors i marcadors inicial i final. Qwen3.5 35B feia servir un PNG vermell de 256 × 256. El broker necessitava una correcció de conversió d'imatges perquè funcionés. La prova llarga 4B del sistema E exigia retenir marcadors i ordre dels colors.

Durant les proves vaig comprovar memòria GPU, residència del model, temperatures, pressió de memòria de l'amfitrió, errors OOM i errors GPU. El control Qwen3.5 35B comprovava l'alliberament després d'una interrupció controlada. Les proves de cancel·lació i cua exercitaven el broker. Dues peticions en cua demostren gestió sota la càrrega provada, no dos backends GPU independents simultanis.

### Com llegir els resultats de rendiment

Els temps inclouen el preompliment llarg i la resposta. No són tokens generats per segon. En transmissió importa el retard fins al primer contingut; les progressions amb prefix en memòria cau s'han d'interpretar separadament.

Les proves posteriors reeixides als sistemes A i C van usar finestres d'inferència dedicades amb mineria aturada. Els models es van descarregar després. La mineria es va restaurar als set sistemes al final de la finestra. Això descriu servei durant inferència, no mineria i inferència simultànies.

## Perfils de backend utilitzats a les proves

Tria el perfil de la càrrega que vulguis reproduir. Quantització, context runtime, tipus de memòria cau, mode de raonament i ubicació GPU afecten el resultat.

| Sistema i model | Perfil de backend provat |
|---|---|
| A, Qwen3.5 35B-A3B Q4_K_M | Ollama 0.34.2, memòria cau KV f16, dues RTX 5060 Ti de 16GB, 64 GiB de RAM de l’amfitrió i context de 262.144 per a la progressió llarga. Les peticions natives feien servir `think:false`, temperatura 0, transmissió i cinc minuts de permanència entre fases. Les peticions del gateway passaven pel broker i LiteLLM. Sense límit de sortida. |
| A, Qwen3.8 27B | llama.cpp sota demanda a través del broker i LiteLLM, context de 262.144, una ranura d’inferència, memòria cau K/V Q4 i dues RTX 5060 Ti. La petició de 66.007 tokens no tenia límit de sortida. |
| A, Qwen3.6-35B-A3B UD-Q4_K_XL | Strata 0.1.48, context de 131.072, memòria cau KV INT8, una GPU seleccionada, límit de memòria del grup de processos de 55 GiB, límit d’execució de 30 minuts, càrrega diferida i descàrrega després de 60 segons inactiu. Resposta llarga del pilot: 217 tokens de sortida. Resposta del gateway prop del límit: 11 tokens, sense límit de sortida. |
| A, Qwen3.8-Flash-Next UD-IQ4_XS | Strata 0.1.48, context de 98.304, memòria cau KV Q4, memòria cau resident d’experts de 8 GiB i dues RTX 5060 Ti. Límit de memòria del pilot de 52 GiB i de 54 GiB per a la ruta posterior. Resposta llarga del pilot: 10 tokens. Configuracions anteriors amb context i memòria cau més grans es van aturar als límits de memòria. |
| A, Granite 4.2 8B | Pesos GGUF Q6_K, procés de treball compartit de llama.cpp, context de 131.072, memòria cau K/V Q4_0 i `--n-predict -1`. La petició llarga feia servir temperatura 0 i transmissió d’ús, sense límit de sortida. |
| A, DeepSeek Coder V2 16B | Pesos GGUF Q4_0, Ollama 0.34.2, dues RTX 5060 Ti i 64 GiB de RAM de l’amfitrió. Les proves separades de memòria cau f16, Q4_0 i Q8_0 feien servir els contextos de la taula comparativa. Sense límit de sortida. |
| B, C, D, servei Ollama auditat | Ollama 0.34.2, context de 131.072, paral·lelisme 1, un model carregat, cua de mida 128, permanència 0, Flash Attention i memòria cau KV Q4_0. |
| B, prova de passarel·la Qwen3.5 9B | Temps d’espera de ruta LiteLLM de 1.800 segons, cap reintent i sense límit de context ni de tokens de sortida. Tots dos marcadors es van conservar amb 72.265 tokens d’entrada. La prova independent de recuperació de mineria va passar. |
| C, Qwen3.5 0.8B | Pesos Q8_0 en una RTX 2000E Ada amb perfil de potència de 30 W. Context de 131.072. `think:false` natiu, `reasoning_effort:"none"` compatible amb OpenAI i sense límit de sortida. L’àlies del broker fixava el context i imposava el mode sense raonament. |
| C, Gemma 4 12B-IT | Perfil Ollama d’una sola GPU, context de 131.072 i peticions Aperture amb i sense transmissió, sense límit de sortida. L’execució directa d’Aperture va arribar a 75 C i 30,64 W amb el perfil de 30 W configurat, i després va descarregar el model. |
| D, Qwen3.5 9B, Gemma 4 12B-IT, GPT-OSS 20B | Artefactes exactes instal·lats i provats mitjançant Aperture, context de 131.072, residència completa en una GPU i finalització natural sense límit de sortida. |
| E, F, G, processos de xat de llama.cpp | Build 11669, 99 capes GPU, paral·lelisme 1, Flash Attention, memòria cau K/V Q4_0 i `--n-predict -1`. El context variava segons la família del model. |

Els perfils de servei descriuen les seves configuracions. El perfil Qwen3.5 35B f16 del sistema A no hereta els ajustos Q4_0 dels sistemes Ollama més petits.

### Empremtes dels models en les noves proves de retenció

Aquests identificadors distingeixen els artefactes provats d'altres baixades o àlies amb noms semblants.

| Artefacte | Quantització | Digest registrat o SHA-256 del fitxer |
|---|---|---|
| Qwen3.5 35B-A3B Ollama tag | Q4_K_M | `72aac7c28be8ff9b81c2a270eb489c88e6d822a76ec0cb7bf34d965768848567` |
| Qwen3.5 0.8B base Ollama tag | Q8_0 | `de63045f29755d4721c09d54c9b45c2dadb644f4fd7d604d4cac90d96049971c` |
| Granite 4.2 8B GGUF file | Q6_K | `5ad3d67f6fe09a448031029bead7f6a088697ca2787c0c5640bf964c59df1a21` |

Els digests del manifest Ollama i els SHA-256 dels fitxers de pesos identifiquen objectes diferents. Relaciona l'identificador amb el tipus d'artefacte de la taula.

## Què faria servir amb Hermes

Faria de Qwen3.5 35B la ruta d'alt context principal al sistema amb dues RTX 5060 Ti. La retenció de 239.153 tokens via passarel·la, les proves separades d'eines i visió i l'alliberament verificat són més sòlids que una finestra gran anunciada. Mantindria Qwen3.8 27B per a resposta més ràpida a 66K i Qwen3.6 quan importi una sola targeta.

Als sistemes RTX 2000E Ada triaria la ruta Gemma 3 4B verificada del sistema C per a la càrrega llarga provada. Provaria Qwen3.5 0.8B sense pensament per a record i extracció acotats. Els models Gemma, Qwen i GPT-OSS més grans serveixen si s'accepten quatre o cinc minuts per a la primera resposta. Exclouria la ruta fallida del sistema D.

Per a targetes RTX 3060 Ti i RTX 3070 de 8 GB començaria amb Qwen3.5 2B o 4B. Els resultats de text 65K i les proves d'imatge 4B avalen un inici útil sense dedicar les dues targetes de 16 GB a cada petició. La pressió de memòria de Flash Next i el resultat incomplet de DeepSeek Coder V2 a 65K en fan opcions per defecte més febles.

Les proves avalen aquests models i sistemes per a fluxos concrets. Retenció d'entrada, ronda d'eina correcta, reconeixement d'imatge i alliberament net cobreixen aspectes diferents de la viabilitat d'Hermes. La configuració fiable necessita els comportaments de l'agent i prou context per a la resposta i el trànsit d'eines.

## Fonts i lectures relacionades

- [Configuració de proveïdor i requisits de context de Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md)
- [Especificacions de NVIDIA GeForce RTX 3060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3060-3060ti/)
- [Especificacions de NVIDIA GeForce RTX 5060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/)
- [Introducció a Hermes Agent](/hermes-local-ai-broker-course/01-hermes-agent-overview/)
- [Com triar un backend local de models](/hermes-local-ai-broker-course/02-choose-a-backend/)
