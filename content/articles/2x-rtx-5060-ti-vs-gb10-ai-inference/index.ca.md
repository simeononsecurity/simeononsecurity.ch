---
title: "2x RTX 5060 Ti contra GB10: benchmark local d’IA amb cinc models i context 256K"
date: 2026-10-10
lastmod: 2026-11-08
toc: true
draft: false
description: "Comparació de cinc models entre RTX 5060 Ti i GB10, més un benchmark Qwen3.8 Flash-Next Strata al mateix host fins a 256K de context."
genre: ["Intel·ligència artificial", "IA local", "Maquinari GPU", "Benchmarking", "Maquinari d’ordinador"]
tags: ["RTX 5060 Ti", "GB10", "DGX Spark", "Qwen3.8", "Qwen3.8 Flash-Next", "GSQ-RCO", "Qwen4Exp", "Strata", "Qwen3.5", "Qwen3.6", "GPT-OSS", "Nemotron", "LLM local", "inferència local", "memòria unificada", "VRAM", "benchmark GPU", "context llarg", "sobrecàrrega PCIe", "maquinari d’IA", "NVIDIA Blackwell", "rendiment LLM", "memòria GPU"]
cover: "/img/cover/nvidia-rtx-5060-ti-vs-gb10-memory-performance-comparison.webp"
coverAlt: "Il·lustració amb dues targetes gràfiques NVIDIA RTX 5060 Ti a l’esquerra i un sistema NVIDIA GB10 a la dreta, totes dues parts destacades sobre un fons fosc amb colors vius."
coverCaption: "El rendiment dels models locals depèn de l’arquitectura de memòria, el model i la longitud del context."
---

**Dues RTX 5060 Ti de 16 GB ofereixen 32 GB de VRAM agregada.** Un sistema NVIDIA GB10 ofereix 128 GB de memòria unificada coherent. El nou benchmark de cinc models mostra un resultat més equilibrat que la prova anterior, que només incloïa Qwen.

El sistema amb dues targetes genera més de pressa en quatre dels cinc models a la configuració de 256K. El GB10 destaca clarament amb Qwen3.8 27B i conserva més memòria per als models, el context i les assignacions del runtime. La millor opció depèn del model i de la càrrega de treball.

Una prova separada al mateix host va comparar Qwen3.8-Flash-Next IQ2_XS amb Strata i Qwen3.8 27B Q4_K_M dens amb Ollama. La mediana de generació després de l’escalfament va ser de 92.8 tokens per segon per a Flash-Next, amb un prompt de 260,446 tokens. Qwen3.8 dens va arribar a 0.939 tokens per segon amb un prompt de 260,444 tokens.

NVIDIA GB10 utilitza 128 GB de memòria unificada coherent. NVIDIA indica 128 GB de memòria unificada LPDDR5x i un TDP del xip de 140 W per a la plataforma GB10. Cada RTX 5060 Ti té 16 GB de GDDR7, una interfície de memòria de 128 bits i una potència gràfica total de 180 W. Les [especificacions de NVIDIA RTX 5060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/) i les [especificacions de NVIDIA GB10](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) descriuen aquesta diferència de maquinari.

**Els dos sistemes exposen la memòria de manera diferent.** Dues targetes formen dos pools separats de 16 GB. El GB10 manté el model, les dades de context, els buffers del runtime i les assignacions del sistema operatiu en un únic espai d’adreces compartit.

## Comparació de memòria

| Sistema | Memòria | Model de memòria | Xifra de potència indicada |
|---|---:|---|---:|
| **2x RTX 5060 Ti 16 GB** | 32 GB agregats | Dos pools separats de memòria GPU | 360 W totals per a les GPU |
| **Sistema GB10** | 128 GB | Memòria de sistema unificada coherent | TDP de 140 W del GB10 |

El GB10 no guanya totes les proves de rendiment perquè la memòria LPDDR5x iguali l’amplada de banda d’una GPU discreta. El seu avantatge prové de la capacitat i de la col·locació. CPU i GPU comparteixen el mateix espai d’adreces, de manera que el conjunt de treball no ha de cabre en dos dispositius aïllats de 16 GB.

El sistema amb dues targetes té un problema de col·locació. El model s’ha de repartir entre les dues targetes. El runtime ha de transferir dades entre elles. El trànsit PCIe augmenta la latència i consumeix amplada de banda. Segons les especificacions de NVIDIA, la RTX 5060 Ti tampoc admet NVLink.

## Benchmark de cinc models

La prova actualitzada va utilitzar la mateixa matriu de sol·licituds als dos sistemes. Va cobrir cinc models d’Ollama amb configuracions de context de 4K, 16K, 32K, 64K, 128K i 256K. Cada sol·licitud va generar 128 tokens amb temperatura 0.

Les etiquetes dels models provats van ser:

- **Qwen3.8 27B:** `qwen3.8:27b`
- **GPT-OSS 20B:** `gpt-oss:20b`
- **Qwen3.6 35B-A3B:** `qwen3.6:35b`
- **Qwen3.5 35B-A3B:** `qwen3.5:35b-a3b-q4_K_M`
- **Nemotron 3.5 Lightning 30B-A3B:** `nemotron-3.5-lightning:30b-a3b-q4_K_M`

El sistema amb dues targetes va utilitzar dues RTX 5060 Ti de 16 GB. El sistema GB10 va utilitzar 128 GB de memòria unificada. Les proves van utilitzar Ollama, versió 0.34.2 al sistema amb dues targetes i 0.40.2 al GB10.

### Velocitat de generació

La velocitat de generació mesura la rapidesa amb què el model produeix tokens després de processar el prompt. Aquesta mètrica importa sobretot en una conversa interactiva.

Sistema amb dues RTX 5060 Ti:

| Context | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 91.518 | 162.027 | 117.547 | 156.104 | 55.654 |
| 16K | 87.176 | 161.377 | 112.903 | 140.596 | 51.656 |
| 32K | 82.372 | 157.055 | 106.455 | 144.833 | 47.369 |
| 64K | 74.661 | 135.106 | 95.979 | 125.008 | 38.863 |
| 128K | 62.767 | 130.924 | 79.572 | 115.352 | 26.399 |
| 256K | 67.853 | 106.221 | 58.947 | 67.159 | 1.079 |

GB10:

| Context | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 62.199 | 98.648 | 72.405 | 100.906 | 32.985 |
| 16K | 56.764 | 94.366 | 69.782 | 95.448 | 32.939 |
| 32K | 53.257 | 98.175 | 64.055 | 95.025 | 29.772 |
| 64K | 49.201 | 96.132 | 58.428 | 84.528 | 25.625 |
| 128K | 40.637 | 80.238 | 48.108 | 74.579 | 22.294 |
| 256K | 43.688 | 68.043 | 36.649 | 62.115 | 22.371 |

A 256K, el sistema amb dues targetes va generar més de pressa amb GPT-OSS, Nemotron, Qwen3.5 i Qwen3.6. El GB10 va generar més de pressa amb Qwen3.8. La velocitat de Qwen3.8 va baixar a 1.079 tokens per segon al sistema amb dues targetes, mentre que el GB10 va produir 22.371 tokens per segon.

El resultat de Qwen3.6 és ajustat. El sistema amb dues targetes va arribar a 67.159 tokens per segon i el GB10 a 62.115. El resultat no avala una afirmació general que la memòria unificada sempre guanyi ni que dues GPU discretes sempre guanyin.

### Velocitat de processament del prompt

El processament del prompt mesura la rapidesa amb què el runtime llegeix el context d’entrada abans de generar. És important per als documents llargs i per a les recàrregues repetides de context.

Sistema amb dues RTX 5060 Ti:

| Context | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 4745.9 | 2409.0 | 2701.7 | 464.3 | 783.9 |
| 16K | 7617.0 | 3031.8 | 4175.3 | 2654.0 | 840.1 |
| 32K | 8099.5 | 3074.2 | 4335.8 | 2623.2 | 811.2 |
| 64K | 6809.5 | 2893.0 | 4129.9 | 2400.4 | 727.8 |
| 128K | 5089.9 | 2362.7 | 3084.0 | 1723.6 | 546.1 |
| 256K | 5838.3 | 1813.2 | 2229.1 | 1011.0 | 251.3 |

GB10:

| Context | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 3295.5 | 576.0 | 2067.9 | 628.8 | 756.9 |
| 16K | 4675.5 | 3006.7 | 2691.2 | 2556.3 | 812.6 |
| 32K | 4571.4 | 3077.9 | 2691.7 | 2563.9 | 794.1 |
| 64K | 3704.7 | 3066.9 | 2585.3 | 2444.9 | 714.0 |
| 128K | 2857.0 | 2802.9 | 2360.4 | 2229.9 | 655.5 |
| 256K | 3243.4 | 2325.4 | 1938.5 | 1817.6 | 535.1 |

A 256K, el sistema amb dues targetes va liderar en processament de prompt per a GPT-OSS i Qwen3.5. El GB10 va liderar amb Nemotron, Qwen3.6 i Qwen3.8. L’arquitectura del model i el comportament del runtime importen tant com la interfície de memòria.

## Benchmarks addicionals de Qwen3.8 Flash-Next

Tres execucions addicionals van mesurar paquets GGUF de Qwen3.8 Flash-Next al sistema amb dues RTX 5060 Ti, amb configuracions de context de 4K i 16K. Cada fila identifica la referència exacta del model a Hugging Face i la quantització.

| Model exacte | Quantització | Generació a 4K | Generació a 16K |
|---|---:|---:|---:|
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS) | IQ2_XS | 31.77 tok/s | 28.20 tok/s |
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ3_S) | IQ3_S | 24.54 tok/s | 22.60 tok/s |
| [`hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M`](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF/tree/main) | Q4_K_M | 17.91 tok/s | 17.02 tok/s |

El paquet IQ2_XS va obtenir el throughput més alt d’aquest grup. El seu resultat a 4K va ser de 31.77 tokens per segon, davant de 24.54 per a IQ3_S i 17.91 per a Q4_K_M. A 16K es va mantenir el mateix ordre, amb 28.20, 22.60 i 17.02 tokens per segon.

Executa les mateixes referències exactes de model amb Ollama:

```bash
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S
ollama run hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M
```

Aquests resultats addicionals anteriors són observacions del sistema amb dues GPU. Són diferents de la matriu de sol·licituds comparable entre RTX 5060 Ti i GB10 que apareix més amunt. El registre identifica les referències exactes dels models, les quantitzacions, les configuracions de context sol·licitades i la velocitat de generació. No inclou els digests de manifest resolts, el recompte de tokens de prompt processats, la longitud de sortida, l’estat d’escalfament, la divisió de dispositius, CPU, RAM del sistema, refrigeració ni la data del mesurament.

## Strata contra Ollama dens a 256K

**Un segon benchmark, del 14 d’octubre de 2026, va comparar dues combinacions de model i runtime al mateix host amb dues RTX 5060 Ti.** La base densa va utilitzar [`qwen3.8:27b`](https://ollama.com/library/qwen3.8:27b), un model Qwen35 de 27.3 mil milions de paràmetres en Q4_K_M. La combinació Flash va utilitzar [Qwen3.8-Flash-Next IQ2_XS](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS), un model Qwen4Exp mixture-of-experts dins d’un paquet natiu unificat de Strata.

Aquesta és una comparació de tota la pila. L’arquitectura del model, la quantització, l’empaquetatge, l’encaminament d’experts i el motor d’inferència van canviar alhora. Les variants Flash IQ3_S i Q4_K_M no es van incloure en aquesta ronda.

### Sistema i mètode de prova

| Component | Configuració registrada |
|---|---|
| **GPU** | 2x NVIDIA GeForce RTX 5060 Ti, 16 GiB cadascuna, compute capability 12.0 |
| **Enllaç GPU** | PCIe 4.0 x4 per targeta, topologia PHB, sense NVLink |
| **CPU** | AMD Ryzen 9 5900XT, 32 fils |
| **Memòria del host** | 62 GiB RAM i 15 GiB swap |
| **Controlador NVIDIA** | 595.99.02 |

L’arnès va generar registres sintètics numerats. Cada fila seguia el format `Record 00001: alpha beta gamma delta epsilon zeta eta theta iota kappa.` La instrucció exigia primer `BENCHMARK_OK`, seguit d’una síntesi tècnica breu fins al límit de sortida. Els sis prompts contenien 180, 720, 1,500, 3,100, 6,200 i 12,400 registres.

Cada execució va usar temperatura 0, seed 42 i una longitud màxima de sortida de 128 tokens. Abans de les cinc sol·licituds mesurades per context hi va haver un escalfament. Les proves Ollama van utilitzar `/api/generate`. Les proves Strata van utilitzar `/v1/chat/completions`. Totes les sol·licituds mesurades van acabar sense errors d’API.

Els controls de descodificació no coincidien. Strata va definir explícitament `reasoning_effort` com a `none` i va desactivar thinking amb la seva plantilla de xat. La sol·licitud densa d’Ollama no va enviar `think: false`, i una prova posterior va trobar sortida als camps thinking i response. Interpreta el resultat de generació com a específic d’aquests modes de descodificació.

| Configuració de context | Tokens de prompt dens | Tokens de prompt Flash |
|---:|---:|---:|
| **4K** | 3,824 | 3,826 |
| **16K** | 15,164 | 15,166 |
| **32K** | 31,544 | 31,546 |
| **64K** | 65,144 | 65,146 |
| **128K** | 130,244 | 130,246 |
| **256K** | 260,444 | 260,446 |

Les capçaleres dels dos models indicaven un context màxim de 262,144 tokens. Els prompts emparellats diferien en dos tokens a cada punt de control.

### Mediana de velocitat de generació després de l’escalfament

Cada mediana cobreix cinc sol·licituds mesurades després d’un escalfament. Cada sol·licitud densa va reutilitzar tots els tokens del prompt anterior, excepte quatre. Cada sol·licitud Flash en va reutilitzar tots, excepte set. La taula mesura throughput de descodificació amb la memòria cau de prefixos calenta. No mesura la latència completa des d’una execució en fred.

| Context | Flash IQ2_XS a Strata | Dense Q4_K_M a Ollama | Avantatge de Flash |
|---:|---:|---:|---:|
| **4K** | 98.4 tok/s | 65.0 tok/s | 1.51x |
| **16K** | 96.8 tok/s | 60.6 tok/s | 1.60x |
| **32K** | 95.3 tok/s | 64.4 tok/s | 1.48x |
| **64K** | 89.6 tok/s | 51.2 tok/s | 1.75x |
| **128K** | 92.9 tok/s | 31.5 tok/s | 2.95x |
| **256K** | 92.8 tok/s | 0.939 tok/s | 98.9x |

La combinació Flash es va mantenir a prop de 90 tokens per segon entre 64K i 256K. Qwen3.8 dens es va alentir molt després de 64K i va arribar a 0.939 tokens per segon a 256K. La resposta Flash de 256K va acabar amb normalitat després de 67 tokens. L’execució densa va arribar al límit de sortida de 128 tokens.

### Processament del primer prompt

| Context | Primera sol·licitud Flash | Primera sol·licitud densa |
|---:|---:|---:|
| **4K** | 1,134 tok/s | 832 tok/s |
| **16K** | 2,013 tok/s | 856 tok/s |
| **32K** | 2,386 tok/s | 799 tok/s |
| **64K** | 2,509 tok/s | 690 tok/s |
| **128K** | 2,538 tok/s | 489 tok/s |
| **256K** | 2,399 tok/s | 214 tok/s |

La primera sol·licitud densa va processar el prompt complet a cada punt de control. Strata va reutilitzar 16,384 tokens de prefix a 64K, 49,152 a 128K i 114,688 a 256K. Considera les taxes Flash de 64K a 256K com a throughput de continuació de la primera sol·licitud, no com a prefill totalment sense memòria cau.

A 256K, Strata va processar la primera sol·licitud en 60.8 segons. Ollama va trigar uns 1,215.4 segons. La reutilització de prefixos impedeix una comparació directa de prefill en fred en aquest punt.

### La col·locació del runtime explica la diferència en context llarg

Ollama 0.34.2 va utilitzar llama-server 0.4.1-dev amb offload de capes CUDA, plantilla ChatML i descodificació especulativa MTP amb una amplada màxima de draft de quatre. Les mides de batch i microbatch van ser 1,024 a 32K i 512 de 64K a 256K. Les 66 capes denses van continuar a les GPU a 32K i 64K. A 128K, 63 de les 66 capes van quedar a les GPU i 1,404 MiB van passar a memòria mapejada per CPU. A 256K, 42 de les 66 capes van quedar a les GPU i 6,002 MiB van passar a memòria mapejada per CPU. La taxa d’acceptació MTP a 256K va ser d’aproximadament 69.4 per cent.

Strata 0.1.44.1 amb CUDA 13.0.3 va mantenir les seves 48 capes repartides entre les dues GPU. La configuració de 4K i 16K va col·locar les capes 0 a 23 a la primera GPU i 24 a 47 a la segona. Aquesta ronda va utilitzar una reserva VRAM automàtica de 700 MiB i 16,047 slots d’experts residents.

La configuració de 32K a 256K va col·locar les capes 0 a 24 a la primera GPU i 25 a 47 a la segona. Aquesta ronda va utilitzar prefill automàtic, una probabilitat mínima especulativa de 0.5, emmagatzematge KV INT8, 32,768 cel·les KV residents per capa QSA, una reserva VRAM de 832 MiB, una memòria cau d’experts amb 15,318 slots i 21,024 MiB, i descodificació especulativa MTP amb una amplada màxima de draft de quatre.

El digest del blob natiu i PLE de Strata era `sha256:1473e0664c2017095f9164b6d617d7a71893452c1180c83002c4f28fc8c2b0da`. L’execució també depenia d’un perfil d’experts i d’un paquet de draft MTP sense digests immutables publicats.

L’execució de Strata va utilitzar el mode predeterminat d’ometre la cua de ruta. Aquesta opció canvia lleugerament la sortida del model i fa que el resultat sigui específic de la configuració registrada del runtime. Les respostes Flash tenien marcadors `BENCHMARK_OK`. Les sol·licituds denses no van tenir errors d’API, però l’arnès principal no va capturar el marcador. Les files en brut indicaven zero caràcters de resposta. Una prova posterior va trobar sortida als camps response i thinking, i va confirmar `BENCHMARK_OK` a la resposta.

La configuració de 4K i 16K va registrar 409 MiB lliures en una sol·licitud i va recomanar una reserva de 832 MiB. La configuració de context llarg va registrar 481 MiB lliures en una sol·licitud i va recomanar una reserva de 896 MiB. Tots dos valors eren inferiors al llindar de 512 MiB de paginació del controlador del motor. Cap sol·licitud va fallar, però aquests estats de poca memòria afecten la repetibilitat.

**Interpreta el valor 98.9x com el resultat de tota la pila en context llarg, no com una prova que el motor sol sigui 98.9x més ràpid.** La prova va aïllar l’host. No va aïllar el model, la quantització ni el runtime.

## La longitud real del prompt importa

El context sol·licitat no és el mateix que el nombre de tokens de prompt processats. A la configuració de 256K, les execucions Qwen3.5, Qwen3.6, Nemotron i Qwen3.8 van processar uns 171,359 a 171,365 tokens de prompt reals en tots dos sistemes.

GPT-OSS va processar 65,538 tokens de prompt reals a la configuració de 256K en tots dos sistemes. Per tant, la seva fila de 256K no representa la mateixa longitud d’entrada que la dels altres models.

El resultat de Qwen3.8 a 256K mostra la diferència amb més claredat. El sistema amb dues targetes va processar 171,359 tokens de prompt a 251.3 tokens per segon i va generar a 1.079 tokens per segon. El GB10 va processar el mateix nombre de tokens a 535.1 tokens per segon i va generar a 22.371 tokens per segon.

**La configuració del context indica el límit sol·licitat.** El recompte real de tokens de prompt indica quina part de la càrrega va completar el runtime.

## Per què la VRAM agregada continua sent important

### 1. El model no veu una sola targeta de 32 GB

Dues GPU no uneixen la seva memòria en un únic espai d’adreces local. Un runtime model-parallel reparteix capes o tensors entre dispositius. Cada dispositiu necessita espai per als pesos assignats, els buffers temporals i la seva part de l’estat del context.

La capacitat utilitzable és inferior a la suma simple. La sobrecàrrega exacta depèn del format del model, la quantització, el backend d’inferència, la divisió de tensors i la longitud del context.

### 2. La memòria de context creix durant la generació

Els pesos del model només són una part del pressupost de memòria. La memòria cau key-value, o KV cache, desa dades d’atenció dels tokens anteriors. Els contextos més llargs necessiten més memòria cau. Una prova de 4K no prediu una implementació de 128K o 256K.

Els nous resultats mostren punts de limitació diferents per a cada model. Qwen3.8 pateix una caiguda greu de generació al sistema amb dues targetes a 256K. Els altres quatre models mantenen una velocitat de generació útil als dos sistemes. La capacitat de memòria continua sent important perquè determina quines combinacions de model i context hi caben deixant espai per a les assignacions del runtime.

### 3. Les transferències PCIe afegeixen un cost

Quan el runtime mou activacions o tensors entre GPU, la transferència passa per la interconnexió de l’host. Això crea punts de sincronització i afegeix latència a cada pas. La penalització depèn de la col·locació dels tensors, l’arquitectura del model, la quantització i la longitud del context.

Això no fa inútil un sistema amb dues GPU. La configuració del runtime i el model determinen el resultat. Un benchmark que només informa del processament de prompt a 4K no mostra aquest cost.

### 4. L’eficiència energètica és un avantatge de sistema

El GB10 utilitza menys potència indicada del xip o de la GPU i ofereix més capacitat de memòria. Dues RTX 5060 Ti sumen 360 W de potència de GPU abans de comptar la resta del sistema. NVIDIA indica un TDP de 140 W per al GB10.

**El GB10 canvia el throughput màxim en diversos models per més capacitat, un conjunt de treball compartit i menys potència GPU indicada.** En aquesta prova, el sistema amb dues targetes ofereix més throughput mesurat en diversos models MoE recents.

## El sistema 5060ti-x2 costa molt menys

Una workstation completa amb dues RTX 5060 Ti de 16 GB apareixia a **$3,479** el 10 d’octubre de 2026. La configuració inclou Intel Ultra 7 265K, placa base Z890, 32 GB DDR5, 1 TB d’emmagatzematge, una font d’alimentació de 1,000 W i les dues GPU. [Consulta la llista de la workstation completa amb dues GPU](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white).

El marketplace dels EUA de NVIDIA anuncia el DGX Spark de 128 GB a **$6,950**. La llista inclou 128 GB de memòria unificada coherent i 4 TB d’emmagatzematge NVMe, però indica que no hi ha estoc. [Consulta la llista actual del DGX Spark de NVIDIA](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/).

La AMD Ryzen AI Halo Developer Platform és un altre punt de comparació. Aquest sistema Strix Halo costa **$3,999.99** a Micro Center amb 128 GB de memòria unificada LPDDR5x i 2 TB d’emmagatzematge. Strix Halo sovint pertany a la mateixa categoria pràctica d’IA local que els sistemes GB10, tot i que les proves independents acostumen a situar GB10 per davant en throughput i maduresa del programari. [Consulta la llista Linux actual de Micro Center](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false) i [llegeix la comparació entre Strix Halo i GB10](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4).

| Sistema complet | Preu anunciat el 10 d’octubre de 2026 | Diferència de preu |
|---|---:|---:|
| **Workstation 5060ti-x2** | $3,479 | Referència |
| **AMD Ryzen AI Halo, Strix Halo** | $3,999.99 | $520.99 més |
| **DGX Spark GB10 de 128 GB** | $6,950 | $3,471 més |

El GB10 ofereix un pool més gran de memòria unificada i menys potència GPU indicada. El sistema AMD ofereix la mateixa categoria de memòria de 128 GB per uns $4,000. La workstation 5060ti-x2 costa aproximadament **el 50% del preu anunciat del GB10**, abans d’impostos i enviament.

Són preus anunciats per venedors diferents, no una cistella de compra controlada. La comparació també deixa el sistema 5060ti-x2 amb menys memòria de sistema i emmagatzematge. Les RTX 5060 Ti de 16 GB es venen actualment per uns **$789 a $830 cadascuna**, molt per sobre del preu de llançament de $429. L’avantatge de preu del sistema amb dues targetes es manté durant l’actual pujada de preus de les GPU. [Consulta els preus actuals de la RTX 5060 Ti](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/).

## Què significa per a les càrregues locals d’IA

Una configuració amb dues targetes de 16 GB executa diversos models quantitzats de 27B a 35B amb context llarg. El benchmark no determina un únic guanyador per a tots els models.

Tria el sistema amb dues targetes si valores:

- **Més velocitat de generació amb GPT-OSS, Nemotron, Qwen3.5 i Qwen3.6** en aquesta prova.
- **Més throughput amb context curt** en els cinc models.
- **Un cost de compra inferior** al del sistema GB10 anunciat.
- **Compatibilitat de programari amb GPU discretes NVIDIA** i marge per provar models nous.

Tria el GB10 si valores:

- **Qwen3.8 27B a 256K**, on el GB10 genera més de 20 vegades més de pressa.
- **Un únic pool de memòria de 128 GB** amb més espai per als pesos, el KV cache i els buffers del runtime.
- **Menys potència GPU o del xip indicada** que amb dues targetes discretes.
- **Menys limitacions de col·locació entre dispositius** per als models que exigeixen més al sistema amb dues targetes.

Això coincideix amb les recomanacions de dimensionament de [N’hi ha prou amb 16 GB de VRAM per treballar seriosament amb LLM locals?](/articles/is-16gb-vram-enough-local-llm/), que considera pesos, context i assignacions del runtime com un sol pressupost. La [guia de 32 GB de VRAM per a Qwen 27B](/articles/32gb-vram-qwen-27b-hardware-guide/) arriba a la mateixa conclusió per a sistemes amb dues targetes. La capacitat agregada no equival a espai disponible.

Per a qualsevol implementació de context llarg, fes quatre preguntes abans de comprar maquinari:

- **La quantització triada hi cap amb els buffers del runtime?** Els pesos del model sols no determinen la necessitat de memòria.
- **El context hi cap sense una pressió greu del KV cache?** Els prompts llargs canvien el resultat.
- **El runtime reparteix bé la feina entre dispositius?** Les transferències PCIe i la col·locació dels tensors afecten cada token generat.
- **El sistema completa el context objectiu?** Un resultat ràpid a 4K no compensa una càrrega de 256K que falla.

**El nou benchmark respon aquestes preguntes per a cada model.** A 256K, Qwen3.8 afavoreix clarament el GB10. En aquesta configuració concreta, els altres quatre models afavoreixen el sistema amb dues targetes en velocitat de generació. El pool més gran de memòria unificada encara ofereix més marge de capacitat, encara que no produeixi el throughput mesurat més alt.

El mateix maquinari amb dues GPU també va registrar una mediana de 92.8 tokens per segon després de l’escalfament a 256K amb Flash-Next IQ2_XS a Strata. Aquest resultat separat no canvia el resultat de Qwen3.8 dens al GB10. Flash-Next utilitza una arquitectura mixture-of-experts, quantització, paquet, runtime i mode de descodificació diferents. Aquest conjunt de dades no inclou un resultat comparable de Flash-Next al GB10.

## Veredicte

**El sistema amb dues RTX 5060 Ti és més ràpid en quatre dels cinc models provats a 256K.** També costa aproximadament la meitat del preu anunciat del GB10. El GB10 continua sent la millor opció per a Qwen3.8 27B a 256K, per tenir més marge de capacitat i per a càrregues que aprofiten un pool de memòria coherent.

El resultat anterior, limitat a Qwen, suggeria una victòria fàcil del GB10. La prova actualitzada amb cinc models mostra per què aquella conclusió era massa general. L’arquitectura del model, la versió del runtime, la col·locació dels tensors i el comportament del context afecten el resultat.

Si executes GPT-OSS, Nemotron 3.5 Lightning, Qwen3.5 o Qwen3.6, el sistema amb dues targetes va oferir més velocitat de generació en aquest benchmark. Si executes Qwen3.8 27B a 256K, el GB10 va mantenir una velocitat útil mentre el sistema amb dues targetes gairebé es va aturar.

**La capacitat de memòria i el throughput són criteris de compra diferents.** El GB10 ofereix quatre vegades la memòria agregada i un conjunt de treball compartit més senzill. El sistema amb dues targetes ofereix més throughput observat en la majoria de models provats per un preu de sistema molt més baix.

El resultat de Strata aporta una altra lliçó. La col·locació del runtime, l’arquitectura del model i el mode de descodificació van canviar el resultat a 256K al mateix host amb dues GPU. Flash-Next IQ2_XS va mantenir una mediana després de l’escalfament propera a 93 tokens per segon, mentre que Qwen3.8 dens va descarregar 24 capes i va baixar d’un token per segon.

## Límits del benchmark

El benchmark registra les etiquetes dels models, els contextos sol·licitats, els tokens de prompt reals, la velocitat de processament del prompt, la velocitat de generació, les versions d’Ollama i l’objectiu de generació de 128 tokens. No registra digests de manifest resolts, potència de la CPU, potència de la paret, velocitat dels ventiladors ni configuració de refrigeració.

Les files GPT-OSS a 256K van processar 65,538 tokens de prompt reals en tots dos sistemes. Les altres files de 256K van processar uns 171K tokens de prompt reals. Considera aquestes xifres una comparació observada entre sistemes, no una classificació universal de totes les parelles RTX 5060 Ti ni de totes les implementacions GB10.

La prova Strata contra dense registra els recomptes exactes de prompt, cinc sol·licituds mesurades per context, les versions del runtime, la col·locació dels dispositius, la configuració de la memòria cau i l’estat de les sol·licituds. La comparació canvia alhora l’arquitectura del model, la quantització, l’empaquetatge, el runtime i el mode de descodificació. Strata també va reutilitzar prefixos de prompt per sobre de 32K. Les sol·licituds de generació mesurades a les dues piles van reutilitzar gairebé tot el prompt.

Aquest article no permet reproduir exactament les proves. L’arnès del benchmark, la disposició del paquet Strata, el perfil d’experts i el paquet de draft MTP no s’han publicat amb digests immutables. L’avís de poca VRAM també afegeix risc de variació entre execucions. La prova aïlla l’host, no el motor d’inferència.

Les especificacions de maquinari anteriors provenen de NVIDIA. Les xifres de rendiment provenen de la prova controlada d’aquest article.

## Referències

- [Biblioteca de models Qwen3.8 d’Ollama](https://ollama.com/library/qwen3.8)
- [Models GGUF Qwen3.8 Flash-Next GSQ-RCO d’ISTA-DASLab](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF)
- [Models GGUF Qwen3.8 Flash-Next Uncensored d’orcarouter](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF)
- [Biblioteca de models Qwen3.5 d’Ollama](https://ollama.com/library/qwen3.5)
- [Biblioteca de models Qwen3.6 d’Ollama](https://ollama.com/library/qwen3.6)
- [Biblioteca de models Nemotron 3.5 Lightning d’Ollama](https://ollama.com/library/nemotron-3.5-lightning)
- [Etiquetes GPT-OSS d’Ollama](https://ollama.com/library/gpt-oss/tags)
- [N’hi ha prou amb 16 GB de VRAM per treballar seriosament amb LLM locals?](/articles/is-16gb-vram-enough-local-llm/)
- [32 GB de VRAM per a Qwen 27B](/articles/32gb-vram-qwen-27b-hardware-guide/)
- [Guia de context GPU per a IA local](/articles/local-ai-model-gpu-context-guide/)
- [Benchmarks GPU de Qwen3.8 27B a Vast.ai](/articles/qwen38-27b-vast-ai-gpu-benchmark/)
- [Llista de la workstation completa amb dues RTX 5060 Ti de 16 GB](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white)
- [Llista del marketplace dels EUA del NVIDIA DGX Spark](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/)
- [Llista Linux AMD Ryzen AI Halo de 128 GB](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false)
- [Anàlisi de Tom's Hardware: Strix Halo contra GB10](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4)
- [Preus actuals de la RTX 5060 Ti](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/)
