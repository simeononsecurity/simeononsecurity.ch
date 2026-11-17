---
title: "2x RTX 5060 Ti contro GB10: benchmark AI locale di cinque modelli con contesto 256K"
date: 2026-10-10
lastmod: 2026-11-07
toc: true
draft: false
description: "Confronto tra RTX 5060 Ti e GB10 su cinque modelli, più un benchmark Qwen3.8 Flash-Next su Strata eseguito sullo stesso host fino a un contesto di 256K."
genre: ["Intelligenza artificiale", "AI locale", "Hardware GPU", "Benchmark", "Hardware per computer"]
tags: ["RTX 5060 Ti", "GB10", "DGX Spark", "Qwen3.8", "Qwen3.8 Flash-Next", "GSQ-RCO", "Qwen4Exp", "Strata", "Qwen3.5", "Qwen3.6", "GPT-OSS", "Nemotron", "LLM locale", "inferenza locale", "memoria unificata", "VRAM", "benchmark GPU", "contesto lungo", "overhead PCIe", "hardware AI", "NVIDIA Blackwell", "prestazioni LLM", "memoria GPU"]
cover: "/img/cover/nvidia-rtx-5060-ti-vs-gb10-memory-performance-comparison.webp"
coverAlt: "Illustrazione con due schede grafiche NVIDIA RTX 5060 Ti a sinistra e un sistema NVIDIA GB10 a destra, evidenziati con colori vivaci su uno sfondo scuro."
coverCaption: "Le prestazioni dei modelli locali dipendono dall'architettura della memoria, dal modello scelto e dalla lunghezza del contesto."
---

**Due schede RTX 5060 Ti da 16 GB offrono complessivamente 32 GB di VRAM.** Un sistema NVIDIA GB10 offre 128 GB di memoria unificata coerente. Il nuovo benchmark su cinque modelli presenta un quadro più equilibrato rispetto al precedente test limitato a Qwen.

Con l'impostazione 256K, il sistema a doppia scheda genera più velocemente su quattro dei cinque modelli. Il GB10 prevale nettamente su Qwen3.8 27B e conserva più memoria per i modelli, il contesto e le allocazioni del runtime. La scelta migliore dipende dal modello e dal carico di lavoro.

Un test separato sullo stesso host ha confrontato Qwen3.8-Flash-Next IQ2_XS su Strata con Qwen3.8 27B Q4_K_M denso su Ollama. La mediana di generazione dopo il riscaldamento è stata di 92.8 token al secondo per Flash-Next, con un prompt di 260,446 token. Qwen3.8 denso ha raggiunto 0.939 token al secondo con un prompt di 260,444 token.

NVIDIA GB10 usa 128 GB di memoria unificata coerente. NVIDIA indica per la piattaforma GB10 128 GB di memoria unificata LPDDR5x e un TDP del chip di 140 W. Ogni RTX 5060 Ti usa 16 GB di GDDR7, un'interfaccia di memoria a 128 bit e una potenza grafica totale dichiarata di 180 W. Le [specifiche NVIDIA RTX 5060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/) e le [specifiche NVIDIA GB10](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) descrivono questa differenza hardware.

**I due sistemi non espongono la memoria nello stesso modo.** Due schede creano due pool separati da 16 GB. Il GB10 colloca il modello, i dati del contesto, i buffer del runtime e le allocazioni del sistema operativo in un unico spazio di indirizzamento condiviso.

## Confronto della memoria

| Sistema | Memoria | Modello di memoria | Potenza dichiarata |
|---|---:|---|---:|
| **2x RTX 5060 Ti 16 GB** | 32 GB complessivi | Due pool di memoria GPU separati | 360 W GPU complessivi |
| **Sistema GB10** | 128 GB | Memoria di sistema unificata coerente | TDP GB10 140 W |

Il GB10 non vince ogni test di throughput, perché la memoria LPDDR5x non eguaglia la banda delle GPU discrete. Il vantaggio deriva da capacità e collocazione. CPU e GPU condividono lo stesso spazio di indirizzamento, quindi il set di lavoro non deve entrare in due dispositivi isolati da 16 GB.

Il sistema a doppia scheda deve gestire il posizionamento: il modello va suddiviso tra le due schede e il runtime deve trasferire dati da una all'altra. Il traffico PCIe aggiunge latenza e consuma banda. Secondo le specifiche NVIDIA, RTX 5060 Ti non supporta NVLink.

## Benchmark su cinque modelli

La prova aggiornata ha usato la stessa matrice di richieste su entrambi i sistemi. Ha coperto cinque modelli Ollama con contesti da 4K, 16K, 32K, 64K, 128K e 256K. Ogni richiesta ha generato 128 token con temperatura 0.

I tag dei modelli testati erano:

- **Qwen3.8 27B:** `qwen3.8:27b`
- **GPT-OSS 20B:** `gpt-oss:20b`
- **Qwen3.6 35B-A3B:** `qwen3.6:35b`
- **Qwen3.5 35B-A3B:** `qwen3.5:35b-a3b-q4_K_M`
- **Nemotron 3.5 Lightning 30B-A3B:** `nemotron-3.5-lightning:30b-a3b-q4_K_M`

Il sistema a doppia scheda usava due RTX 5060 Ti da 16 GB. Il GB10 usava 128 GB di memoria unificata. I test hanno usato Ollama, versione 0.34.2 sul sistema a doppia scheda e 0.40.2 sul GB10.

### Velocità di generazione

La velocità di generazione misura i token prodotti dopo l'elaborazione del prompt. Questo dato è il più importante durante una conversazione interattiva.

Sistema con due RTX 5060 Ti:

| Contesto | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 91.518 | 162.027 | 117.547 | 156.104 | 55.654 |
| 16K | 87.176 | 161.377 | 112.903 | 140.596 | 51.656 |
| 32K | 82.372 | 157.055 | 106.455 | 144.833 | 47.369 |
| 64K | 74.661 | 135.106 | 95.979 | 125.008 | 38.863 |
| 128K | 62.767 | 130.924 | 79.572 | 115.352 | 26.399 |
| 256K | 67.853 | 106.221 | 58.947 | 67.159 | 1.079 |

GB10:

| Contesto | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 62.199 | 98.648 | 72.405 | 100.906 | 32.985 |
| 16K | 56.764 | 94.366 | 69.782 | 95.448 | 32.939 |
| 32K | 53.257 | 98.175 | 64.055 | 95.025 | 29.772 |
| 64K | 49.201 | 96.132 | 58.428 | 84.528 | 25.625 |
| 128K | 40.637 | 80.238 | 48.108 | 74.579 | 22.294 |
| 256K | 43.688 | 68.043 | 36.649 | 62.115 | 22.371 |

A 256K, il sistema a doppia scheda ha generato più velocemente con GPT-OSS, Nemotron, Qwen3.5 e Qwen3.6. Il GB10 ha superato nettamente il sistema a doppia scheda con Qwen3.8: quest'ultimo è sceso a 1.079 token al secondo, mentre il GB10 ne ha prodotti 22.371 al secondo.

Il risultato di Qwen3.6 è vicino: il sistema a doppia scheda ha raggiunto 67.159 token al secondo e il GB10 62.115. Il dato non sostiene l'affermazione generale che la memoria unificata vinca sempre o che vincano sempre due GPU discrete.

### Velocità di elaborazione del prompt

L'elaborazione del prompt misura la velocità con cui il runtime legge il contesto in ingresso prima della generazione. È importante per i documenti lunghi e i ricaricamenti ripetuti del contesto.

Sistema con due RTX 5060 Ti:

| Contesto | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 4745.9 | 2409.0 | 2701.7 | 464.3 | 783.9 |
| 16K | 7617.0 | 3031.8 | 4175.3 | 2654.0 | 840.1 |
| 32K | 8099.5 | 3074.2 | 4335.8 | 2623.2 | 811.2 |
| 64K | 6809.5 | 2893.0 | 4129.9 | 2400.4 | 727.8 |
| 128K | 5089.9 | 2362.7 | 3084.0 | 1723.6 | 546.1 |
| 256K | 5838.3 | 1813.2 | 2229.1 | 1011.0 | 251.3 |

GB10:

| Contesto | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 3295.5 | 576.0 | 2067.9 | 628.8 | 756.9 |
| 16K | 4675.5 | 3006.7 | 2691.2 | 2556.3 | 812.6 |
| 32K | 4571.4 | 3077.9 | 2691.7 | 2563.9 | 794.1 |
| 64K | 3704.7 | 3066.9 | 2585.3 | 2444.9 | 714.0 |
| 128K | 2857.0 | 2802.9 | 2360.4 | 2229.9 | 655.5 |
| 256K | 3243.4 | 2325.4 | 1938.5 | 1817.6 | 535.1 |

A 256K, il sistema a doppia scheda ha elaborato più velocemente i prompt di GPT-OSS e Qwen3.5. Il GB10 ha prevalso su Nemotron, Qwen3.6 e Qwen3.8. L'architettura del modello e il comportamento del runtime contano quanto l'interfaccia di memoria.

## Benchmark aggiuntivi Qwen3.8 Flash-Next

Tre prove aggiuntive hanno misurato pacchetti Qwen3.8 Flash-Next GGUF sul sistema con due RTX 5060 Ti, usando contesti 4K e 16K. Ogni riga riporta il riferimento esatto del modello su Hugging Face e la quantizzazione.

| Modello esatto | Quantizzazione | Generazione 4K | Generazione 16K |
|---|---:|---:|---:|
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS) | IQ2_XS | 31.77 tok/s | 28.20 tok/s |
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ3_S) | IQ3_S | 24.54 tok/s | 22.60 tok/s |
| [`hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M`](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF/tree/main) | Q4_K_M | 17.91 tok/s | 17.02 tok/s |

Il pacchetto IQ2_XS ha ottenuto il throughput più alto del gruppo: 31.77 token al secondo a 4K, contro 24.54 per IQ3_S e 17.91 per Q4_K_M. A 16K l'ordine è rimasto lo stesso: 28.20, 22.60 e 17.02 token al secondo.

Esegui in Ollama gli stessi riferimenti esatti dei modelli:

```bash
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S
ollama run hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M
```

Questi risultati supplementari precedenti provengono da un sistema con due GPU e sono separati dalla matrice di richieste abbinata tra RTX 5060 Ti e GB10 riportata sopra. Il registro fornito indica i riferimenti esatti dei modelli, le quantizzazioni, i contesti richiesti e la velocità di generazione. Non include digest risolti dei manifest, conteggio dei token di prompt elaborati, lunghezza dell'output, stato di riscaldamento, suddivisione tra dispositivi, CPU, RAM, raffreddamento e data della misurazione.

## Strata contro Ollama denso a 256K

**Un secondo benchmark del 14 ottobre 2026 ha confrontato due stack di modelli e runtime sullo stesso host con due RTX 5060 Ti.** La baseline densa usava [`qwen3.8:27b`](https://ollama.com/library/qwen3.8:27b), un modello Qwen35 da 27.3 miliardi di parametri in Q4_K_M. Lo stack Flash usava [Qwen3.8-Flash-Next IQ2_XS](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS), un modello Qwen4Exp mixture-of-experts in un pacchetto nativo unificato Strata.

È un confronto tra stack completi. Architettura del modello, quantizzazione, confezionamento, routing degli esperti e motore di inferenza sono cambiati insieme. Le varianti Flash IQ3_S e Q4_K_M non rientrano in questa prova.

### Sistema di test e metodo

| Componente | Configurazione registrata |
|---|---|
| **GPU** | 2x NVIDIA GeForce RTX 5060 Ti, 16 GiB ciascuna, compute capability 12.0 |
| **Collegamento GPU** | PCIe 4.0 x4 per scheda, topologia PHB, senza NVLink |
| **CPU** | AMD Ryzen 9 5900XT, 32 thread |
| **Memoria host** | 62 GiB RAM e 15 GiB swap |
| **Driver NVIDIA** | 595.99.02 |

L'harness ha generato record numerati sintetici. Ogni riga seguiva il formato `Record 00001: alpha beta gamma delta epsilon zeta eta theta iota kappa.` L'istruzione richiedeva prima `BENCHMARK_OK`, seguito da una sintesi tecnica concisa fino al limite di output. I sei prompt contenevano 180, 720, 1,500, 3,100, 6,200 e 12,400 record.

Ogni prova usava temperatura 0, seed 42 e una lunghezza massima di output di 128 token. Per ogni contesto, a un riscaldamento seguivano cinque richieste misurate. I test Ollama usavano `/api/generate`; quelli Strata `/v1/chat/completions`. Tutte le richieste misurate sono state completate senza errori API.

I controlli di decodifica non erano abbinati. Strata impostava esplicitamente `reasoning_effort` su `none` e disattivava il thinking tramite il template chat. La richiesta densa a Ollama non inviava `think: false`; una verifica successiva ha trovato l'output denso nei campi thinking e response. Considera il risultato di generazione specifico di queste modalità di decodifica.

| Impostazione contesto | Token prompt denso | Token prompt Flash |
|---:|---:|---:|
| **4K** | 3,824 | 3,826 |
| **16K** | 15,164 | 15,166 |
| **32K** | 31,544 | 31,546 |
| **64K** | 65,144 | 65,146 |
| **128K** | 130,244 | 130,246 |
| **256K** | 260,444 | 260,446 |

Le intestazioni di entrambi i modelli dichiaravano un contesto massimo di 262,144 token. I prompt abbinati differivano di due token a ogni punto di controllo.

### Mediana della velocità di generazione dopo il riscaldamento

Ogni mediana copre cinque richieste misurate dopo un riscaldamento. Ogni richiesta densa misurata riutilizzava tutti i token del prompt tranne quattro; ogni richiesta Flash tutti tranne sette. La tabella misura il throughput di decodifica a caldo con prefisso in cache, non la latenza end-to-end a freddo.

| Contesto | Flash IQ2_XS su Strata | Denso Q4_K_M su Ollama | Vantaggio Flash |
|---:|---:|---:|---:|
| **4K** | 98.4 tok/s | 65.0 tok/s | 1.51x |
| **16K** | 96.8 tok/s | 60.6 tok/s | 1.60x |
| **32K** | 95.3 tok/s | 64.4 tok/s | 1.48x |
| **64K** | 89.6 tok/s | 51.2 tok/s | 1.75x |
| **128K** | 92.9 tok/s | 31.5 tok/s | 2.95x |
| **256K** | 92.8 tok/s | 0.939 tok/s | 98.9x |

Lo stack Flash è rimasto vicino a 90 token al secondo da 64K a 256K. Qwen3.8 denso ha rallentato nettamente dopo 64K e a 256K ha raggiunto 0.939 token al secondo. La risposta Flash a 256K si è conclusa normalmente dopo 67 token. La prova densa ha raggiunto il limite di output di 128 token.

### Elaborazione del prompt nella prima richiesta

| Contesto | Prima richiesta Flash | Prima richiesta densa |
|---:|---:|---:|
| **4K** | 1,134 tok/s | 832 tok/s |
| **16K** | 2,013 tok/s | 856 tok/s |
| **32K** | 2,386 tok/s | 799 tok/s |
| **64K** | 2,509 tok/s | 690 tok/s |
| **128K** | 2,538 tok/s | 489 tok/s |
| **256K** | 2,399 tok/s | 214 tok/s |

La prima richiesta densa ha elaborato l'intero prompt a ogni punto di controllo. Strata ha segnalato il riutilizzo di 16,384 token di prefisso a 64K, 49,152 a 128K e 114,688 a 256K. Considera le velocità Flash da 64K a 256K come throughput di continuazione della prima richiesta, non come prefill completo senza cache.

A 256K, Strata ha elaborato la prima richiesta in 60.8 secondi. Ollama ha impiegato circa 1,215.4 secondi. Il riutilizzo del prefisso impedisce un confronto diretto del prefill a freddo in questo punto.

### Il posizionamento del runtime spiega la differenza con contesti lunghi

Ollama 0.34.2 usava llama-server 0.4.1-dev con offload dei layer CUDA, template ChatML e decodifica speculativa MTP con ampiezza massima della bozza pari a quattro. Batch e microbatch erano di 1,024 a 32K e 512 da 64K a 256K. A 32K e 64K tutti i 66 layer densi restavano sulle GPU. A 128K, 63 layer su 66 restavano sulle GPU e 1,404 MiB passavano alla memoria mappata sulla CPU. A 256K, 42 layer su 66 restavano sulle GPU e 6,002 MiB passavano alla memoria mappata sulla CPU. Il tasso di accettazione MTP a 256K era circa 69.4 percento.

Strata 0.1.44.1 con CUDA 13.0.3 manteneva i suoi 48 layer divisi tra le due GPU. La configurazione 4K e 16K collocava i layer da 0 a 23 sulla prima GPU e da 24 a 47 sulla seconda. Questa prova usava una riserva VRAM automatica di 700 MiB e 16,047 slot esperti residenti.

La configurazione da 32K a 256K collocava i layer da 0 a 24 sulla prima GPU e da 25 a 47 sulla seconda. Questa prova usava prefill automatico, probabilità minima speculativa 0.5, archiviazione KV INT8, 32,768 celle KV residenti per layer QSA, una riserva VRAM di 832 MiB, una cache esperti con 15,318 slot e 21,024 MiB, e decodifica speculativa MTP con ampiezza massima della bozza pari a quattro.

Il digest del blob nativo Strata e PLE era `sha256:1473e0664c2017095f9164b6d617d7a71893452c1180c83002c4f28fc8c2b0da`. La prova dipendeva anche da un profilo esperti e da un pacchetto di bozza MTP senza digest immutabili pubblicati.

La prova Strata usava la modalità predefinita di skip della coda del routing. Questa impostazione modifica leggermente l'output del modello e rende il risultato specifico della configurazione registrata del runtime. Le risposte Flash contenevano i marcatori `BENCHMARK_OK`. Le richieste dense non hanno restituito errori API, ma l'harness principale non ha acquisito il marcatore. Le righe grezze indicavano zero caratteri di risposta. Una verifica successiva ha trovato output nei campi response e thinking e ha confermato `BENCHMARK_OK` nella risposta.

La configurazione 4K e 16K ha registrato una richiesta con 409 MiB liberi e ha raccomandato una riserva di 832 MiB. La configurazione a contesto lungo ha registrato una richiesta con 481 MiB liberi e ha raccomandato una riserva di 896 MiB. Entrambi i valori erano sotto la soglia di paging del driver di 512 MiB. Nessuna richiesta è fallita, ma questi livelli ridotti di memoria libera influiscono sulla ripetibilità.

**Interpreta il valore 98.9x come risultato a contesto lungo dell'intero stack, non come prova di un vantaggio di 98.9x del solo motore.** Il test isola l'host, ma non il modello, la quantizzazione o il runtime.

## La lunghezza effettiva del prompt conta

Il contesto richiesto non coincide con il numero di token del prompt elaborati. Con l'impostazione 256K, i test Qwen3.5, Qwen3.6, Nemotron e Qwen3.8 hanno elaborato circa 171,359-171,365 token effettivi del prompt su entrambi i sistemi.

GPT-OSS ha elaborato 65,538 token effettivi del prompt con l'impostazione 256K su entrambi i sistemi. La sua riga 256K non rappresenta quindi la stessa lunghezza di input degli altri modelli.

Il risultato Qwen3.8 a 256K mostra la differenza più netta. Il sistema a doppia scheda ha elaborato 171,359 token di prompt a 251.3 token al secondo e ha generato a 1.079 token al secondo. Il GB10 ha elaborato lo stesso numero di token di prompt a 535.1 token al secondo e ha generato a 22.371 token al secondo.

**L'impostazione del contesto indica il limite richiesto.** Il conteggio effettivo dei token del prompt mostra il carico completato dal runtime.

## Perché la VRAM aggregata conta ancora

### 1. Il modello non vede un'unica scheda da 32 GB

Due GPU non uniscono la memoria in un unico spazio di indirizzamento locale. Un runtime model-parallel divide layer o tensori tra i dispositivi. Ogni dispositivo deve comunque contenere i pesi assegnati, i buffer temporanei e una parte dello stato del contesto.

La capacità utilizzabile è inferiore a quella suggerita dalla somma semplice. L'overhead preciso dipende dal formato del modello, dalla quantizzazione, dal backend di inferenza, dalla suddivisione dei tensori e dalla lunghezza del contesto.

### 2. La memoria del contesto cresce durante la generazione

I pesi del modello sono solo una parte del budget di memoria. La cache key-value, o cache KV, memorizza i dati di attention dei token precedenti. Contesti più lunghi richiedono più memoria per la cache. Un test 4K non predice un deployment 128K o 256K.

I nuovi risultati mostrano punti di cedimento diversi per ciascun modello. A 256K Qwen3.8 subisce un forte crollo della generazione sul sistema a doppia scheda. Gli altri quattro modelli mantengono una velocità di generazione utile su entrambi i sistemi. La capacità di memoria resta importante perché determina quali combinazioni di modello e contesto entrano lasciando spazio alle allocazioni del runtime.

### 3. I trasferimenti PCIe aggiungono un costo

Quando il runtime trasferisce attivazioni o tensori tra GPU, il trasferimento attraversa l'interconnessione dell'host. Questo crea punti di sincronizzazione e aggiunge latenza a ogni passaggio. La penalità dipende dal posizionamento dei tensori, dall'architettura del modello, dalla quantizzazione e dalla lunghezza del contesto.

Questo non rende inutile un sistema con due GPU. Significa che il risultato dipende dalla configurazione del runtime e dal modello. Un benchmark che riporta solo l'elaborazione del prompt a 4K non mostra questo costo.

### 4. L'efficienza energetica resta un vantaggio a livello di sistema

Il GB10 ha una potenza dichiarata del chip o della GPU inferiore e offre più memoria. Le due RTX 5060 Ti hanno una potenza GPU combinata dichiarata di 360 W, senza considerare il resto del sistema. NVIDIA indica un TDP di 140 W per GB10.

**Il GB10 sacrifica il throughput massimo su vari modelli in cambio di capacità, un set di lavoro condiviso e una potenza GPU dichiarata inferiore.** Il sistema a doppia scheda offre un throughput misurato maggiore su diversi modelli MoE più recenti.

## Il sistema 5060ti-x2 costa molto meno

Una workstation completa con due RTX 5060 Ti da 16 GB era in vendita a **$3,479** il 10 ottobre 2026. La configurazione include Intel Ultra 7 265K, scheda madre Z890, 32 GB DDR5, 1 TB di storage, alimentatore da 1,000 W ed entrambe le GPU. [Visualizza l'offerta della workstation completa con due GPU](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white).

Il marketplace statunitense NVIDIA indica il DGX Spark da 128 GB a **$6,950**. L'offerta include 128 GB di memoria unificata coerente e 4 TB di storage NVMe, ma il sistema risulta esaurito. [Controlla l'offerta DGX Spark corrente di NVIDIA](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/).

La piattaforma per sviluppatori AMD Ryzen AI Halo offre un altro riferimento. Questo sistema Strix Halo è quotato a **$3,999.99** da Micro Center, con 128 GB di memoria unificata LPDDR5x e 2 TB di storage. Strix Halo spesso rientra nella stessa categoria pratica di sistemi GB10 per l'AI locale, anche se i test indipendenti misurano spesso prestazioni e maturità software superiori per GB10. [Controlla l'offerta Linux corrente di Micro Center](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false) e [leggi la recensione Strix Halo contro GB10](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4).

| Sistema completo | Prezzo indicato il 10 ottobre 2026 | Differenza di prezzo |
|---|---:|---:|
| **Workstation 5060ti-x2** | $3,479 | Riferimento |
| **AMD Ryzen AI Halo, Strix Halo** | $3,999.99 | $520.99 in più |
| **128 GB GB10 DGX Spark** | $6,950 | $3,471 in più |

Il GB10 offre un pool di memoria unificata più ampio e una potenza GPU dichiarata inferiore. Il sistema AMD offre la stessa classe di memoria da 128 GB per circa $4,000. La workstation 5060ti-x2 costa ancora circa **il 50% del prezzo indicato per GB10**, prima di tasse e spedizione.

Sono prezzi pubblicati da rivenditori diversi, non un confronto con un paniere di acquisto controllato. Il sistema 5060ti-x2 ha anche meno memoria di sistema e storage. Le offerte attuali per RTX 5060 Ti da 16 GB si aggirano sui **$789-$830 ciascuna**, molto oltre il prezzo di lancio di $429. Il vantaggio economico del sistema a doppia scheda persiste quindi durante l'attuale aumento dei prezzi GPU. [Controlla i prezzi attuali di RTX 5060 Ti](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/).

## Cosa significa per i carichi di lavoro AI locali

Una configurazione con due schede da 16 GB esegue diversi modelli quantizzati da 27B a 35B con contesti lunghi. Il benchmark non indica un vincitore unico per ogni modello.

Scegli il sistema a doppia scheda se dai priorità a:

- **Maggiore velocità di generazione per GPT-OSS, Nemotron, Qwen3.5 e Qwen3.6** in questo test.
- **Maggiore throughput con contesto breve** sui cinque modelli.
- **Costo di acquisto inferiore** rispetto al sistema GB10 indicato.
- **Compatibilità software con GPU discrete NVIDIA** e possibilità di sperimentare altri modelli.

Scegli il GB10 se dai priorità a:

- **Qwen3.8 27B a 256K**, per cui GB10 genera oltre 20 volte più velocemente.
- **Un unico pool di memoria da 128 GB**, con più spazio per pesi del modello, cache KV e buffer del runtime.
- **Potenza dichiarata di GPU o chip inferiore** rispetto a due schede discrete.
- **Meno vincoli di collocazione tra più dispositivi** per i modelli che mettono sotto pressione la configurazione a doppia scheda.

Questo è coerente con le indicazioni di dimensionamento in [16 GB di VRAM bastano per lavorare seriamente con LLM locali?](/articles/is-16gb-vram-enough-local-llm/), che considera pesi, contesto e allocazioni del runtime come un unico budget. Anche la [guida ai 32 GB di VRAM per Qwen 27B](/articles/32gb-vram-qwen-27b-hardware-guide/) arriva alla stessa conclusione per i sistemi a due schede. La capacità aggregata non equivale alla memoria disponibile.

Prima di acquistare hardware per un deployment a contesto lungo, poni quattro domande:

- **La quantizzazione richiesta entra insieme ai buffer del runtime?** I soli pesi del modello non determinano il fabbisogno di memoria.
- **Il contesto entra senza mettere sotto pressione la cache KV?** I prompt lunghi cambiano il risultato.
- **Il runtime suddivide il carico tra dispositivi in modo efficiente?** I trasferimenti PCIe e il posizionamento dei tensori influiscono su ogni token generato.
- **Il sistema completa il contesto richiesto?** Un risultato rapido a 4K non compensa un carico 256K non completato.

**Il nuovo benchmark risponde a queste domande per ogni modello.** A 256K Qwen3.8 favorisce nettamente GB10. In questa configurazione specifica, gli altri quattro modelli generano più velocemente sul sistema a doppia scheda. Il pool di memoria unificata più ampio offre comunque maggiore margine di capacità, anche quando non raggiunge il throughput misurato più alto.

Lo stesso hardware a doppia GPU ha registrato anche una mediana post-riscaldamento di 92.8 token al secondo a 256K con Flash-Next IQ2_XS su Strata. Questo risultato separato non ribalta quello di Qwen3.8 denso su GB10. Flash-Next usa un'architettura mixture-of-experts, quantizzazione, pacchetto, runtime e modalità di decodifica diversi. Questo dataset non include un risultato Flash-Next su GB10 comparabile.

## Verdetto

**Il sistema con due RTX 5060 Ti genera più velocemente per quattro dei cinque modelli testati a 256K.** Costa inoltre circa la metà del sistema GB10 indicato. GB10 resta la scelta migliore per Qwen3.8 27B a 256K, per il margine di memoria e per i carichi che traggono vantaggio da un unico pool di memoria coerente.

Il precedente risultato limitato a Qwen suggeriva una semplice vittoria di GB10. Il nuovo test su cinque modelli mostra perché quella conclusione era troppo ampia. Il risultato dipende dall'architettura del modello, dalla versione del runtime, dal posizionamento dei tensori e dal comportamento con diversi contesti.

Se usi GPT-OSS, Nemotron 3.5 Lightning, Qwen3.5 o Qwen3.6, in questo benchmark il sistema a doppia scheda ha offerto una velocità di generazione maggiore. Se usi Qwen3.8 27B a 256K, GB10 ha mantenuto una velocità di generazione utile, mentre il sistema a doppia scheda si è quasi bloccato.

**Capacità di memoria e throughput sono criteri d'acquisto distinti.** GB10 offre quattro volte la memoria aggregata e un set di lavoro condiviso più semplice. Il sistema a doppia scheda offre un throughput osservato più alto sulla maggior parte dei modelli testati, a un prezzo indicato molto inferiore.

Il risultato Strata aggiunge un secondo insegnamento. Posizionamento del runtime, architettura del modello e modalità di decodifica hanno cambiato il risultato 256K sullo stesso host a doppia scheda. Flash-Next IQ2_XS ha mantenuto una mediana post-riscaldamento vicina a 93 token al secondo, mentre Qwen3.8 denso ha trasferito 24 layer e rallentato sotto un token al secondo.

## Limiti del benchmark

Il benchmark registra i tag dei modelli, i contesti richiesti, i token effettivi del prompt, la velocità di elaborazione del prompt e di generazione, le versioni di Ollama e l'obiettivo di generazione di 128 token. Non registra digest risolti dei manifest, potenza della CPU, consumo alla presa, velocità delle ventole o configurazione di raffreddamento.

Le righe GPT-OSS a 256K hanno elaborato 65,538 token effettivi del prompt su entrambi i sistemi. Le altre righe 256K ne hanno elaborati circa 171K. Considera i dati come un confronto osservato tra sistemi, non come una classifica universale di ogni coppia di RTX 5060 Ti e di ogni implementazione GB10.

Il test Strata contro il modello denso registra i conteggi esatti dei prompt, cinque richieste misurate per contesto, versioni del runtime, posizionamento dei dispositivi, impostazioni della cache e stato delle richieste. Il confronto cambia insieme architettura del modello, quantizzazione, confezionamento, runtime e modalità di decodifica. Strata ha riutilizzato anche i prefissi del prompt oltre 32K. Le richieste di generazione misurate su entrambi gli stack hanno riutilizzato quasi tutto il prompt.

Non è possibile riprodurre esattamente il test partendo da questo articolo. L'harness del benchmark, il layout del pacchetto Strata, il profilo esperti e il pacchetto draft MTP non sono pubblicati con digest immutabili. L'avviso di VRAM bassa aggiunge inoltre variabilità tra le esecuzioni. Il test isola l'host, non il motore di inferenza.

Le specifiche hardware sopra riportate provengono da NVIDIA. I dati sulle prestazioni derivano dal benchmark controllato per questo articolo.

## Riferimenti

- [Libreria di modelli Ollama Qwen3.8](https://ollama.com/library/qwen3.8)
- [Modelli ISTA-DASLab Qwen3.8 Flash-Next GSQ-RCO GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF)
- [Modelli orcarouter Qwen3.8 Flash-Next Uncensored GGUF](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF)
- [Libreria di modelli Ollama Qwen3.5](https://ollama.com/library/qwen3.5)
- [Libreria di modelli Ollama Qwen3.6](https://ollama.com/library/qwen3.6)
- [Libreria di modelli Ollama Nemotron 3.5 Lightning](https://ollama.com/library/nemotron-3.5-lightning)
- [Tag dei modelli Ollama GPT-OSS](https://ollama.com/library/gpt-oss/tags)
- [16 GB di VRAM bastano per lavorare seriamente con LLM locali?](/articles/is-16gb-vram-enough-local-llm/)
- [32 GB di VRAM per Qwen 27B](/articles/32gb-vram-qwen-27b-hardware-guide/)
- [Guida al contesto dei modelli AI locali e alle GPU](/articles/local-ai-model-gpu-context-guide/)
- [Benchmark GPU di Qwen3.8 27B su Vast.ai](/articles/qwen38-27b-vast-ai-gpu-benchmark/)
- [Offerta workstation completa con due RTX 5060 Ti da 16 GB](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white)
- [Offerta NVIDIA DGX Spark sul marketplace statunitense](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/)
- [Offerta Linux AMD Ryzen AI Halo da 128 GB](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false)
- [Recensione Tom's Hardware: Strix Halo contro GB10](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4)
- [Prezzi attuali di RTX 5060 Ti](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/)
