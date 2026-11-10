---
title: "2x RTX 5060 Ti versus GB10: lokale AI-benchmark met vijf modellen bij 256K context"
date: 2026-10-10
lastmod: 2026-11-07
toc: true
draft: false
description: "Vergelijking van vijf modellen op RTX 5060 Ti en GB10, plus een benchmark op dezelfde host van Qwen3.8 Flash-Next Strata tot 256K context."
genre: ["Kunstmatige intelligentie", "Lokale AI", "GPU-hardware", "Benchmarking", "Computerhardware"]
tags: ["RTX 5060 Ti", "GB10", "DGX Spark", "Qwen3.8", "Qwen3.8 Flash-Next", "GSQ-RCO", "Qwen4Exp", "Strata", "Qwen3.5", "Qwen3.6", "GPT-OSS", "Nemotron", "lokale LLM", "lokale inferentie", "unified memory", "VRAM", "GPU-benchmark", "lange context", "PCIe-overhead", "AI-hardware", "NVIDIA Blackwell", "LLM-prestaties", "GPU-geheugen"]
cover: "/img/cover/nvidia-rtx-5060-ti-vs-gb10-memory-performance-comparison.webp"
coverAlt: "Illustratie met links twee NVIDIA RTX 5060 Ti-videokaarten en rechts een NVIDIA GB10-systeem, beide uitgelicht tegen een donkere achtergrond met levendige kleuren."
coverCaption: "Prestaties van lokale modellen hangen af van geheugenarchitectuur, modelkeuze en contextlengte."
---

**Twee RTX 5060 Ti-kaarten met elk 16 GB leveren samen 32 GB VRAM.** Een NVIDIA GB10-systeem heeft 128 GB coherent unified memory. De nieuwe benchmark met vijf modellen geeft een evenwichtiger beeld dan de eerdere test met alleen Qwen.

Het systeem met twee kaarten genereert bij de instelling van 256K voor vier van de vijf modellen sneller. De GB10 presteert duidelijk beter op Qwen3.8 27B en houdt meer geheugen over voor modellen, context en runtime-toewijzingen. De beste keuze hangt af van model en belasting.

Een afzonderlijke run op dezelfde host vergeleek Qwen3.8-Flash-Next IQ2_XS op Strata met dense Qwen3.8 27B Q4_K_M op Ollama. De mediane generatiesnelheid na opwarming was 92,8 tokens per seconde voor Flash-Next bij een prompt van 260.446 tokens. Dense Qwen3.8 haalde 0,939 tokens per seconde bij een prompt van 260.444 tokens.

De NVIDIA GB10 gebruikt 128 GB coherent unified memory. NVIDIA vermeldt 128 GB LPDDR5x unified memory en een chip-TDP van 140 W. De RTX 5060 Ti heeft per kaart 16 GB GDDR7, een 128-bit geheugeninterface en een totaal grafisch vermogen van 180 W. [Specificaties NVIDIA RTX 5060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/) en [specificaties NVIDIA GB10](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) beschrijven het hardwareverschil.

**De twee systemen bieden geheugen niet op dezelfde manier aan.** Twee kaarten vormen twee aparte pools van 16 GB. De GB10 plaatst model, contextgegevens, runtimebuffers en besturingssysteemtoewijzingen in één gedeelde adresruimte.

## Geheugen vergelijken

| Systeem | Geheugen | Geheugenmodel | Vermogenscijfer |
|---|---:|---|---:|
| **2x RTX 5060 Ti 16 GB** | 32 GB totaal | Twee aparte GPU-geheugenpools | 360 W totaal voor GPU's |
| **GB10-systeem** | 128 GB | Coherent unified system memory | 140 W GB10 TDP |

De GB10 wint niet elke doorvoertest omdat LPDDR5x dezelfde bandbreedte als discrete GPU's biedt. Het voordeel zit in capaciteit en plaatsing. CPU en GPU delen één adresruimte, zodat de werkset niet binnen twee geïsoleerde pools van 16 GB hoeft te passen.

Het systeem met twee kaarten heeft een plaatsingsprobleem. Het model moet over beide kaarten worden verdeeld. De runtime moet gegevens ertussen verplaatsen. PCIe-verkeer voegt latentie toe en verbruikt bandbreedte. Volgens de NVIDIA-specificaties ondersteunt de RTX 5060 Ti ook geen NVLink.

## Benchmark met vijf modellen

De bijgewerkte run gebruikte op beide systemen dezelfde aanvraagmatrix. De test omvatte vijf Ollama-modellen met contextinstellingen van 4K, 16K, 32K, 64K, 128K en 256K. Elke aanvraag genereerde 128 tokens met temperatuur 0.

De gebruikte modeltags waren:

- **Qwen3.8 27B:** `qwen3.8:27b`
- **GPT-OSS 20B:** `gpt-oss:20b`
- **Qwen3.6 35B-A3B:** `qwen3.6:35b`
- **Qwen3.5 35B-A3B:** `qwen3.5:35b-a3b-q4_K_M`
- **Nemotron 3.5 Lightning 30B-A3B:** `nemotron-3.5-lightning:30b-a3b-q4_K_M`

Het systeem met twee kaarten gebruikte twee RTX 5060 Ti-kaarten van 16 GB. De GB10 gebruikte 128 GB unified memory. De runs gebruikten Ollama, versie 0.34.2 op het systeem met twee kaarten en versie 0.40.2 op de GB10.

### Generatiesnelheid

Generatiesnelheid meet de tokens die na promptverwerking worden geproduceerd. Deze maat is vooral belangrijk in een interactief gesprek.

Systeem met twee RTX 5060 Ti-kaarten:

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

Bij 256K genereerde het systeem met twee kaarten sneller voor GPT-OSS, Nemotron, Qwen3.5 en Qwen3.6. De GB10 was veel sneller op Qwen3.8: die zakte op het systeem met twee kaarten naar 1,079 tokens per seconde, terwijl de GB10 22,371 haalde.

Het resultaat voor Qwen3.6 ligt dicht bij elkaar. Het systeem met twee kaarten haalde 67,159 tokens per seconde en de GB10 62,115. De resultaten ondersteunen niet de algemene claim dat unified memory altijd wint of dat twee discrete GPU's altijd winnen.

### Promptverwerkingssnelheid

Promptverwerking meet hoe snel de runtime de invoercontext leest voordat generatie begint. Dit is belangrijk bij lange documenten en herhaald laden van context.

Systeem met twee RTX 5060 Ti-kaarten:

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

Bij 256K verwerkte het systeem met twee kaarten prompts voor GPT-OSS en Qwen3.5 sneller. De GB10 was sneller voor Nemotron, Qwen3.6 en Qwen3.8. Modelarchitectuur en runtimegedrag zijn minstens zo belangrijk als de geheugeninterface.

## Aanvullende benchmarks voor Qwen3.8 Flash-Next

Drie extra runs maten Qwen3.8 Flash-Next GGUF-pakketten op het systeem met twee RTX 5060 Ti-kaarten bij contextinstellingen van 4K en 16K. De exacte Hugging Face-modelreferentie en kwantisatie staan in elke rij.

| Exact model | Kwantisatie | Generatie 4K | Generatie 16K |
|---|---:|---:|---:|
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS) | IQ2_XS | 31.77 tok/s | 28.20 tok/s |
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ3_S) | IQ3_S | 24.54 tok/s | 22.60 tok/s |
| [`hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M`](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF/tree/main) | Q4_K_M | 17.91 tok/s | 17.02 tok/s |

Het IQ2_XS-pakket had in deze reeks de hoogste doorvoer. Bij 4K was dat 31,77 tokens per seconde, tegenover 24,54 voor IQ3_S en 17,91 voor Q4_K_M. Bij 16K bleef de volgorde gelijk: 28,20, 22,60 en 17,02 tokens per seconde.

Voer dezelfde exacte modelreferenties uit met Ollama:

```bash
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S
ollama run hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M
```

Deze eerdere aanvullende resultaten komen van twee GPU's. Ze staan los van de bovenstaande vergelijkbare aanvraagmatrix voor RTX 5060 Ti versus GB10. Het aangeleverde record bevat de exacte modelreferenties, kwantisaties, gevraagde contextinstellingen en generatiesnelheid. Het bevat geen opgeloste manifest-digests, verwerkte prompttokens, uitvoerlengte, warme toestand, apparaatverdeling, CPU, systeem-RAM, koeling of meetdatum.

## Strata versus dense Ollama bij 256K

**Een tweede benchmark van 14 oktober 2026 vergeleek twee model- en runtime-stacks op dezelfde host met twee RTX 5060 Ti-kaarten.** De dense basislijn gebruikte [`qwen3.8:27b`](https://ollama.com/library/qwen3.8:27b), een Qwen35-model van 27,3 miljard parameters in Q4_K_M. De Flash-stack gebruikte [Qwen3.8-Flash-Next IQ2_XS](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS), een mixture-of-experts-model van Qwen4Exp in een native Strata unified pack.

Dit vergelijkt complete stacks. Modelarchitectuur, kwantisatie, verpakking, expert-routing en inferentie-engine veranderden tegelijk. De IQ3_S- en Q4_K_M-Flashvarianten vielen buiten deze test.

### Testsysteem en methode

| Component | Vastgelegde configuratie |
|---|---|
| **GPU's** | 2x NVIDIA GeForce RTX 5060 Ti, elk 16 GiB, compute capability 12.0 |
| **GPU-verbinding** | PCIe 4.0 x4 per kaart, PHB-topologie, geen NVLink |
| **CPU** | AMD Ryzen 9 5900XT, 32 threads |
| **Hostgeheugen** | 62 GiB RAM en 15 GiB swap |
| **NVIDIA-driver** | 595.99.02 |

De harness genereerde synthetische genummerde records. Elke rij had de vorm `Record 00001: alpha beta gamma delta epsilon zeta eta theta iota kappa.` De instructie vereiste eerst `BENCHMARK_OK`, daarna een beknopte technische synthese tot de uitvoerlimiet. De zes prompts bevatten 180, 720, 1.500, 3.100, 6.200 en 12.400 records.

Elke run gebruikte temperatuur 0, seed 42 en maximaal 128 uitvoertokens. Voor elke context volgden vijf gemeten aanvragen op één opwarmrun. De Ollama-tests gebruikten `/api/generate`. De Strata-tests gebruikten `/v1/chat/completions`. Alle gemeten aanvragen werden zonder API-fouten voltooid.

De decode-instellingen waren niet gelijk. Strata stelde `reasoning_effort` expliciet in op `none` en schakelde denken uit via het chattemplate. De dense Ollama-aanvraag stuurde geen `think: false` en dense uitvoer verscheen in denk- en antwoordvelden tijdens een vervolgaanvraag. Beschouw de generatieresultaten als specifiek voor deze decode-instellingen.

| Contextinstelling | Dense prompttokens | Flash-prompttokens |
|---:|---:|---:|
| **4K** | 3,824 | 3,826 |
| **16K** | 15,164 | 15,166 |
| **32K** | 31,544 | 31,546 |
| **64K** | 65,144 | 65,146 |
| **128K** | 130,244 | 130,246 |
| **256K** | 260,444 | 260,446 |

De headers van beide modellen vermeldden een maximale context van 262.144 tokens. De prompts verschilden bij elk controlepunt met twee tokens.

### Mediane generatiesnelheid na opwarming

Elke mediaan omvat vijf gemeten aanvragen na één opwarmrun. Bij elke dense aanvraag bleven alle prompttokens behalve vier behouden. Bij elke Flash-aanvraag bleven alle prompttokens behalve zeven behouden. De tabel meet warme decode-doorvoer met prefixcache. Dit is geen meting van koude end-to-endlatentie.

| Context | Flash IQ2_XS op Strata | Dense Q4_K_M op Ollama | Voorsprong Flash |
|---:|---:|---:|---:|
| **4K** | 98.4 tok/s | 65.0 tok/s | 1.51x |
| **16K** | 96.8 tok/s | 60.6 tok/s | 1.60x |
| **32K** | 95.3 tok/s | 64.4 tok/s | 1.48x |
| **64K** | 89.6 tok/s | 51.2 tok/s | 1.75x |
| **128K** | 92.9 tok/s | 31.5 tok/s | 2.95x |
| **256K** | 92.8 tok/s | 0.939 tok/s | 98.9x |

De Flash-stack bleef tussen 64K en 256K rond 90 tokens per seconde. Dense Qwen3.8 vertraagde sterk na 64K en haalde bij 256K 0,939 tokens per seconde. De Flash-uitvoer bij 256K eindigde normaal na 67 tokens. De dense run bereikte de uitvoerlimiet van 128 tokens.

### Promptverwerking van de eerste aanvraag

| Context | Eerste Flash-aanvraag | Eerste dense aanvraag |
|---:|---:|---:|
| **4K** | 1,134 tok/s | 832 tok/s |
| **16K** | 2,013 tok/s | 856 tok/s |
| **32K** | 2,386 tok/s | 799 tok/s |
| **64K** | 2,509 tok/s | 690 tok/s |
| **128K** | 2,538 tok/s | 489 tok/s |
| **256K** | 2,399 tok/s | 214 tok/s |

De eerste dense aanvraag verwerkte de volledige prompt bij elk controlepunt. Strata rapporteerde 16.384 hergebruikte prefix-tokens bij 64K, 49.152 bij 128K en 114.688 bij 256K. Beschouw de Flash-snelheden van 64K tot 256K als doorvoer voor de voortzetting van de eerste aanvraag, niet als volledig ongecachede prefill.

Bij 256K verwerkte Strata de eerste aanvraag in 60,8 seconden. Ollama had ongeveer 1.215,4 seconden nodig. Door het prefixhergebruik is een directe vergelijking van koude prefill bij dit controlepunt niet mogelijk.

### Plaatsing in de runtime verklaart het verschil bij lange context

Ollama 0.34.2 gebruikte llama-server 0.4.1-dev met CUDA-laadoffload, het ChatML-template en MTP-speculative decoding met een maximale draftbreedte van vier. Batch- en microbatchgroottes waren 1.024 bij 32K en 512 van 64K tot 256K. Bij 32K en 64K bleven alle 66 dense lagen op de GPU's. Bij 128K bleven 63 van 66 lagen op de GPU's en ging 1.404 MiB naar CPU-mapped geheugen. Bij 256K bleven 42 van 66 lagen op de GPU's en ging 6.002 MiB naar CPU-mapped geheugen. De MTP-acceptatiegraad bij 256K was ongeveer 69,4 procent.

Strata 0.1.44.1 met CUDA 13.0.3 hield de 48 lagen verdeeld over beide GPU's. De configuratie van 4K en 16K plaatste lagen 0 t/m 23 op de eerste GPU en lagen 24 t/m 47 op de tweede. Deze run gebruikte automatisch 700 MiB VRAM-reserve en 16.047 aanwezige expert-slots.

De configuratie van 32K tot 256K plaatste lagen 0 t/m 24 op de eerste GPU en lagen 25 t/m 47 op de tweede. Deze run gebruikte automatische prefill, een minimale speculative probability van 0,5, INT8 KV-opslag, 32.768 aanwezige KV-cellen per QSA-laag, 832 MiB VRAM-reserve, een expertcache met 15.318 slots en 21.024 MiB, en MTP-speculative decoding met een maximale draftbreedte van vier.

De digest van de native Strata- en PLE-blob was `sha256:1473e0664c2017095f9164b6d617d7a71893452c1180c83002c4f28fc8c2b0da`. De run hing ook af van een expertprofiel en een MTP-draftpack zonder gepubliceerde onveranderlijke digests.

De Strata-run gebruikte de standaardinstelling om de staart van de route over te slaan. Deze instelling verandert de modeluitvoer enigszins en maakt het resultaat specifiek voor de vastgelegde runtimeconfiguratie. Flash-antwoorden bevatten `BENCHMARK_OK`-markeringen. Dense aanvragen hadden nul API-fouten, maar de primaire harness legde de markering niet vast. De ruwe rijen noteerden nul antwoordtekens. Een vervolgaanvraag vond uitvoer in antwoord- en denkvelden en bevestigde `BENCHMARK_OK` in het antwoord.

De 4K- en 16K-configuratie registreerde één aanvraag met 409 MiB vrij en adviseerde 832 MiB reserve. De configuratie voor lange context registreerde één aanvraag met 481 MiB vrij en adviseerde 896 MiB reserve. Beide waarden lagen onder de drempel van 512 MiB voor driverpaging in de engine. Geen aanvraag faalde, maar deze lage geheugentoestanden beïnvloeden de reproduceerbaarheid.

**Behandel het cijfer van 98,9x als een resultaat van de volledige stack bij lange context, niet als bewijs van een voordeel van 98,9x voor alleen de engine.** De test isoleert de host, niet het model, de kwantisatie of de runtime.

## Werkelijke promptlengte is belangrijk

De gevraagde context is niet hetzelfde als het aantal verwerkte prompttokens. Bij de instelling van 256K verwerkten Qwen3.5-, Qwen3.6-, Nemotron- en Qwen3.8-runs op beide systemen ongeveer 171.359 tot 171.365 prompttokens.

GPT-OSS verwerkte bij de instelling van 256K op beide systemen 65.538 prompttokens. De rij voor 256K vertegenwoordigt daarom niet dezelfde invoerlengte als de andere modellen.

Het resultaat van Qwen3.8 bij 256K laat het verschil het duidelijkst zien. Het systeem met twee kaarten verwerkte 171.359 prompttokens met 251,3 tokens per seconde en genereerde met 1,079 tokens per seconde. De GB10 verwerkte hetzelfde aantal prompttokens met 535,1 tokens per seconde en genereerde met 22,371 tokens per seconde.

**Een contextinstelling bevestigt de gevraagde limiet.** Het werkelijke aantal prompttokens bewijst dat de runtime de belasting heeft voltooid.

## Waarom totale VRAM nog steeds telt

### 1. Het model ziet geen enkele kaart van 32 GB

Twee GPU's voegen hun geheugen niet samen tot één lokale adresruimte. Een modelparallelle runtime verdeelt lagen of tensors over apparaten. Elke GPU moet ruimte houden voor toegewezen gewichten, tijdelijke buffers en een deel van de contextstatus.

De bruikbare capaciteit is kleiner dan de eenvoudige optelsom. De exacte overhead hangt af van modelindeling, kwantisatie, inferentiebackend, tensorsprerdeling en contextlengte.

### 2. Contextgeheugen groeit tijdens generatie

Modelgewichten zijn maar één deel van het geheugenbudget. De key-value-cache, of KV-cache, bewaart attentiongegevens voor eerdere tokens. Langere context vereist meer cachegeheugen. Een test met 4K voorspelt geen inzet met 128K of 256K.

De nieuwe resultaten tonen per model verschillende foutpunten. Qwen3.8 stort bij 256K vrijwel in qua generatiesnelheid op het systeem met twee kaarten. De andere vier modellen behouden op beide systemen bruikbare snelheid. Geheugencapaciteit blijft belangrijk omdat die bepaalt welke combinatie van model en context past naast de runtime-toewijzingen.

### 3. PCIe-overdracht kost prestaties

Wanneer de runtime activaties of tensors tussen GPU's verplaatst, loopt de overdracht via de hostinterconnect. Dat veroorzaakt synchronisatie en voegt latentie toe aan elke stap. De impact hangt af van tensorplaatsing, modelarchitectuur, kwantisatie en contextlengte.

Dit maakt een systeem met twee GPU's niet nutteloos. Het betekent dat runtimeconfiguratie en model het resultaat bepalen. Een benchmark die alleen promptverwerking bij 4K rapporteert, mist deze kosten.

### 4. Energie-efficiëntie is een voordeel op systeemniveau

De GB10 gebruikt minder gerapporteerd chip- of GPU-vermogen en biedt meer geheugencapaciteit. Twee RTX 5060 Ti-kaarten hebben samen 360 W GPU-vermogen, zonder de rest van het systeem. NVIDIA vermeldt een TDP van 140 W voor de GB10.

**De GB10 ruilt piekdoorvoer op meerdere modellen in voor capaciteit, een gedeelde werkset en lager gerapporteerd GPU-vermogen.** Het systeem met twee kaarten levert in deze test meer doorvoer op meerdere nieuwere MoE-modellen.

## Het 5060ti-x2-systeem kost veel minder

Een complete workstation met twee RTX 5060 Ti 16 GB-kaarten stond op 10 oktober 2026 te koop voor **$3.479**. De configuratie bevat een Intel Ultra 7 265K, Z890-moederbord, 32 GB DDR5, 1 TB opslag, een voeding van 1.000 W en beide GPU's. [Bekijk de complete workstation met twee GPU's](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white).

NVIDIA's Amerikaanse marktplaats vermeldt de 128 GB DGX Spark voor **$6.950**. De aanbieding bevat 128 GB coherent unified memory en 4 TB NVMe-opslag, maar toont het systeem als niet op voorraad. [Bekijk de actuele DGX Spark-aanbieding van NVIDIA](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/).

Het AMD Ryzen AI Halo Developer Platform is een ander vergelijkingspunt. Dit Strix Halo-systeem staat bij Micro Center te koop voor **$3.999,99** met 128 GB LPDDR5x unified memory en 2 TB opslag. Strix Halo valt vaak in dezelfde praktische klasse voor lokale AI als GB10-systemen, al meten onafhankelijke tests GB10 vaak hoger op doorvoer en volwassenheid van software. [Bekijk de actuele Micro Center Linux-aanbieding](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false) en [lees de vergelijking Strix Halo versus GB10](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4).

| Compleet systeem | Aanbiedingsprijs op 10 oktober 2026 | Prijsverschil |
|---|---:|---:|
| **5060ti-x2-workstation** | $3.479 | Basislijn |
| **AMD Ryzen AI Halo, Strix Halo** | $3.999,99 | $520,99 meer |
| **128 GB GB10 DGX Spark** | $6.950 | $3.471 meer |

De GB10 heeft een grotere unified-memorypool en lager gerapporteerd GPU-vermogen. Het AMD-systeem biedt dezelfde klasse van 128 GB geheugen voor ongeveer $4.000. De 5060ti-x2-workstation kost ongeveer **50% van de vermelde GB10-prijs**, vóór belasting en verzending.

Dit zijn vermelde prijzen van verschillende winkels, geen gecontroleerde winkelmand. Het 5060ti-x2-systeem heeft ook minder systeemgeheugen en opslag. Actuele aanbiedingen van RTX 5060 Ti 16 GB-kaarten liggen rond **$789 tot $830 per stuk**, ruim boven de lanceringsadviesprijs van $429. Het prijsvoordeel van twee kaarten blijft dus bestaan tijdens de huidige GPU-prijspiek. [Actuele prijscontrole RTX 5060 Ti](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/).

## Betekenis voor lokale AI-belastingen

Een configuratie met twee kaarten van 16 GB kan meerdere gekwantiseerde modellen van 27B tot 35B bij lange context draaien. De benchmark wijst geen universele winnaar aan.

Kies het systeem met twee kaarten wanneer je waarde hecht aan:

- **Hogere generatiesnelheid voor GPT-OSS, Nemotron, Qwen3.5 en Qwen3.6** in deze test.
- **Hogere doorvoer bij korte context** voor de vijf modellen.
- **Lagere aanschafprijs** dan het vermelde GB10-systeem.
- **NVIDIA-softwarecompatibiliteit voor discrete GPU's** en experimenten met toekomstige modellen.

Kies de GB10 wanneer je waarde hecht aan:

- **Qwen3.8 27B bij 256K**, waar de GB10 bij generatie meer dan twintig keer sneller is.
- **Eén geheugenpool van 128 GB** met meer ruimte voor gewichten, KV-cache en runtimebuffers.
- **Lager gerapporteerd GPU- of chipvermogen** dan twee discrete kaarten.
- **Minder plaatsingsbeperkingen bij meerdere apparaten** voor modellen die het systeem met twee kaarten zwaar belasten.

Dit sluit aan bij de dimensioneringsrichtlijnen in [Is 16GB VRAM genoeg voor serieus lokaal LLM-werk?](/articles/is-16gb-vram-enough-local-llm/), waarin gewichten, context en runtime-toewijzingen één budget vormen. De [32GB VRAM-gids voor Qwen 27B](/articles/32gb-vram-qwen-27b-hardware-guide/) komt voor builds met twee kaarten tot dezelfde conclusie. Totale capaciteit is geen bruikbare reserve.

Stel vóór aankoop van hardware vier vragen over elke inzet met lange context:

- **Past de gekozen kwantisatie met runtimebuffers?** Modelgewichten bepalen niet alleen de geheugeneis.
- **Past de context zonder zware KV-cache-druk?** Lange prompts veranderen het resultaat.
- **Verdeelt de runtime apparaten efficiënt?** PCIe-overdracht en tensorplaatsing beïnvloeden elk gegenereerd token.
- **Voltooit het systeem de doelcontext?** Een snel resultaat bij 4K compenseert geen mislukte belasting bij 256K.

**De nieuwe benchmark beantwoordt deze vragen per model.** Qwen3.8 geeft bij 256K een duidelijk voordeel aan de GB10. De andere vier modellen geven in deze specifieke opstelling de voorkeur aan het systeem met twee kaarten voor generatiesnelheid. De grotere unified-memorypool biedt nog steeds meer capaciteitsruimte, ook als die niet de hoogste gemeten doorvoer oplevert.

Dezelfde hardware met twee GPU's haalde met Flash-Next IQ2_XS op Strata ook een mediane snelheid van 92,8 tokens per seconde na opwarming bij 256K. Dit afzonderlijke resultaat verandert de bevinding voor dense Qwen3.8 op de GB10 niet. Flash-Next gebruikt een andere mixture-of-experts-architectuur, kwantisatie, verpakking, runtime en decodeermodus. In deze dataset bestaat geen vergelijkbare GB10-run voor Flash-Next.

## Conclusie

**Het systeem met twee RTX 5060 Ti-kaarten genereert bij 256K sneller voor vier van de vijf geteste modellen.** Het kost ook ongeveer de helft van de vermelde prijs van het GB10-systeem. De GB10 is nog steeds de betere keuze voor Qwen3.8 27B bij 256K, voor capaciteitsruimte en voor belastingen die baat hebben bij één coherent geheugenpool.

Het eerdere resultaat met alleen Qwen leek op een eenvoudige overwinning voor de GB10. De bijgewerkte test met vijf modellen toont waarom die conclusie te breed was. Modelarchitectuur, runtimeversie, tensorplaatsing en contextgedrag beïnvloeden het resultaat.

Als je GPT-OSS, Nemotron 3.5 Lightning, Qwen3.5 of Qwen3.6 draait, behaalde het systeem met twee kaarten in deze benchmark een hogere generatiesnelheid. Draai je Qwen3.8 27B bij 256K, dan haalde de GB10 bruikbare snelheid terwijl het systeem met twee kaarten bijna stilviel.

**Geheugencapaciteit en doorvoer zijn aparte aankoopcriteria.** De GB10 biedt vier keer zoveel totaal geheugen en een eenvoudiger gedeelde werkset. Het systeem met twee kaarten biedt voor de meeste geteste modellen een hogere gemeten doorvoer tegen een veel lagere vermelde systeemprijs.

Het Strata-resultaat leert nog iets. Runtimeplaatsing, modelarchitectuur en decodeermodus veranderden het resultaat bij 256K op dezelfde host met twee GPU's. Flash-Next IQ2_XS bleef na opwarming rond 93 tokens per seconde, terwijl dense Qwen3.8 24 lagen offloadde en onder één token per seconde zakte.

## Beperkingen van de benchmark

De benchmark registreert modeltags, gevraagde contexten, werkelijke prompttokens, promptverwerkingssnelheid, generatiesnelheid, Ollama-versies en het doel van 128 uitvoertokens. CPU-vermogen, wandvermogen, ventilatorsnelheid en koeling zijn niet vastgelegd.

De GPT-OSS-rijen bij 256K verwerkten op beide systemen 65.538 prompttokens. De andere rijen bij 256K verwerkten ongeveer 171K prompttokens. Beschouw de cijfers als een waargenomen systeemvergelijking, niet als een universele rangschikking van elk paar RTX 5060 Ti-kaarten en elke GB10-uitvoering.

De vergelijking Strata versus dense legt exacte aantallen prompttokens, vijf metingen per context, runtimeversies, apparaatplaatsing, cache-instellingen en aanvraagstatus vast. De modellen verschillen tegelijk in architectuur, kwantisatie, verpakking, runtime en decodeermodus. Strata hergebruikte ook promptprefixen boven 32K. Bij beide stacks hergebruikten gemeten generatieaanvragen bijna de volledige prompt.

Exacte reproductie op basis van dit artikel is niet mogelijk. De benchmark-harness, Strata-packindeling, het expertprofiel en het MTP-draftpack zijn niet met onveranderlijke digests gepubliceerd. De waarschuwing voor weinig VRAM vergroot ook de variatie tussen runs. De test isoleert de host, niet de inferentie-engine.

De bovenstaande hardwarespecificaties komen van NVIDIA. De prestatiecijfers komen uit de gecontroleerde benchmarkrun voor dit artikel.

## Referenties

- [Ollama Qwen3.8-modellenbibliotheek](https://ollama.com/library/qwen3.8)
- [ISTA-DASLab Qwen3.8 Flash-Next GSQ-RCO GGUF-modellen](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF)
- [orcarouter Qwen3.8 Flash-Next Uncensored GGUF-modellen](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF)
- [Ollama Qwen3.5-modellenbibliotheek](https://ollama.com/library/qwen3.5)
- [Ollama Qwen3.6-modellenbibliotheek](https://ollama.com/library/qwen3.6)
- [Ollama Nemotron 3.5 Lightning-modellenbibliotheek](https://ollama.com/library/nemotron-3.5-lightning)
- [Ollama GPT-OSS-modeltags](https://ollama.com/library/gpt-oss/tags)
- [Is 16GB VRAM genoeg voor serieus lokaal LLM-werk?](/articles/is-16gb-vram-enough-local-llm/)
- [32GB VRAM voor Qwen 27B](/articles/32gb-vram-qwen-27b-hardware-guide/)
- [Contextgids voor lokale AI-GPU's](/articles/local-ai-model-gpu-context-guide/)
- [Qwen3.8 27B GPU-benchmarks op Vast.ai](/articles/qwen38-27b-vast-ai-gpu-benchmark/)
- [Complete workstation met twee RTX 5060 Ti 16 GB-kaarten](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white)
- [NVIDIA DGX Spark-aanbieding op de Amerikaanse marktplaats](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/)
- [AMD Ryzen AI Halo Linux-aanbieding met 128 GB](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false)
- [Tom's Hardware-review: Strix Halo versus GB10](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4)
- [Actuele RTX 5060 Ti-prijzen](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/)
