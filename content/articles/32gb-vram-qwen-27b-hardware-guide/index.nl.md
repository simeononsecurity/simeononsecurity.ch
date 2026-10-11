---
title: "32 GB VRAM voor Qwen 27B: hardwaregids voor lokale AI in oktober 2026"
date: 2026-10-03
lastmod: 2026-10-10
toc: true
draft: false
description: "Praktische gids voor oktober 2026 om een Qwen 27B-model te draaien met 32 GB bruikbaar acceleratorgeheugen. Vergelijk losse GPU's, systemen met twee kaarten, unified memory, gebruikte datacenterkaarten, gehuurde rekenkracht, softwareondersteuning en limieten bij volledige context."
genre: ["Lokale AI", "AI-hardware", "GPU-benchmarking", "Zelf gehoste AI", "Computerhardware", "AI-economie"]
tags: ["32GB VRAM", "Qwen 27B", "Qwen3.8 27B", "lokale AI", "GPU-koopgids", "VRAM", "llama.cpp", "RTX 5090", "RTX 5060 Ti", "Radeon AI PRO R9700", "Intel Arc Pro B70", "Tesla V100", "AMD Instinct MI50", "GPU huren", "lange context", "KV cache", "multi GPU", "tensor split", "CUDA", "ROCm", "Metal", "unified memory", "lokale LLM", "AI-workstation"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Een moderne workstation met een grafische kaart en schermen met prestatiegegevens van een lokaal AI-model"
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/qwen38-27b-vast-ai-gpu-benchmark", "/articles/dgx-spark-64gb-memory-crisis-2027"]
---

**32 GB op het productlabel betekent niet 32 GB beschikbaar voor een Qwen 27B-werklast.** Het besturingssysteem, de runtime, KV-cache, modelindeling, driverstack en kaartopstelling veranderen het resultaat. Een goedkope kaart met voldoende capaciteit kan alsnog verliezen op promptverwerking of insteltijd.

*Vergelijk voor oktober 2026 bruikbaar geheugen en uitgevoerd werk per dollar, niet alleen het VRAM-getal.*

Deze gids beschrijft praktische manieren om een Qwen 27B-model met 6-bitkwaliteit en een groot contextvenster te draaien. Gepubliceerde specificaties staan los van gemelde testresultaten. De tokens-per-seconde-score van één persoon is geen vaste eigenschap van een GPU.

## Waarom 32 GB het doel is

De geheugenbehoefte begint bij de gewichten. Een dicht 27B-model leest tijdens generatie de volledige parameterset. Bij 6-bitquantisatie nemen de gewichten ongeveer **20,5 GB** in, voordat runtime-allocaties en contextgeheugen meetellen.

Een context van 128K tokens vraagt nog een grote allocatie. De exacte KV-cachegrootte hangt af van modelarchitectuur, cacheprecisie, batchinstellingen en backend. Een praktische schatting van ongeveer **8 GB** brengt gewichten en cache samen op circa **28,5 GB**, vóór het aandeel van besturingssysteem en inferentieruntime.

| Configuratie | Ondersteuning |
|---|---|
| **24GB discrete GPU** | 4-bitgewichten met kleinere context, of gedeeltelijke offload |
| **32GB discrete GPU** | 6-bitgewichten met een bruikbaar 128K-contextdoel |
| **Twee 16GB-GPU's** | Gesplitst model met minder ruimte voor runtime-overhead |
| **64GB unified memory** | Grotere context en modellen, binnen de GPU-geheugenlimiet |

**32 GB is een meetpunt voor dimensionering, geen garantie.** Een model kan laden en toch te weinig ruimte overlaten voor een lange prompt, grotere batch, multimodale invoer of een tweede proces.

## De video is een bruikbare praktijkreferentie

De volgende video vergelijkt de belangrijkste manieren om 32 GB voor lokale AI te bereiken. De video helpt bij gemelde prijzen, instelwerk en runtime-resultaten. Dit artikel maakt een afzonderlijke vergelijking op basis van hardwarespecificaties, modelgeheugen, softwareondersteuning en totale eigendomskosten.

{{< youtube id="uavLRbbfM94" enable="true" title="Every Ways to Get 32GB VRAM for Local AI at Full Context" description="Praktijkvergelijking van single-GPU, multi-GPU, unified-memory, gebruikte accelerator- en huurtrajecten voor lokale AI-werklasten van 32 GB." >}}

## Bruikbaar geheugen weegt zwaarder dan geheugen op de doos

### Apple unified memory

Apple silicon gebruikt één gedeelde pool voor CPU en GPU. Apple verkoopt Mac mini-configuraties met 32 GB unified memory, maar de volledige pool is geen toegewezen grafisch geheugen. macOS, de toepassing en de inferentieruntime hebben ook ruimte nodig.

Sommige llama.cpp-sessies melden ongeveer **22.906 MB beschikbaar** op een 32GB-systeem. Dat is ongeveer **21,3 GiB**, met weinig ruimte voor een 6-bit 27B-model plus grote KV-cache. De precieze grens hangt af van besturingssysteem, modelrunner, geheugendruk en startopties.

Apple silicon blijft aantrekkelijk voor stille systemen. llama.cpp behandelt Metal als volwaardig backend. Apple vermijdt ook driver- en stroomproblemen van veel gebruikte datacenterkaarten. De ruil is lagere doorvoer dan bij een krachtige discrete GPU en minder voorspelbare geheugenruimte.

### Twee kaarten van 16 GB

Twee 16GB-kaarten leveren 32 GB fysiek VRAM, maar de runtime heeft per apparaat buffers en communicatieruimte nodig. De ene kaart kan 13,4 GB gebruik melden en de andere 14,4 GB. De resterende capaciteit is geen nette reserve van 4 GB voor context.

Ook de splitsmethode telt. **Layer splitting** wijst verschillende modellagen aan verschillende kaarten toe. Dit vergroot de capaciteit, maar de kaarten doorlopen het model om de beurt. **Tensor splitting** verdeelt werk van dezelfde laag over beide kaarten. De communicatie neemt toe, maar beide apparaten dragen directer bij.

| Splitsmethode | Belangrijkste voordeel | Belangrijkste kosten |
|---|---|---|
| **Layer split** | Eenvoudige capaciteitsuitbreiding | Eén kaart wacht vaak terwijl de andere werkt |
| **Tensor split** | Betere parallelle berekening bij sommige werklasten | Meer tuning en interconnectverkeer |
| **CPU plus GPU offload** | Modellen boven totale VRAM passen toch | Grote snelheidsstraf wanneer de CPU vaak lagen verwerkt |

**Een plan met twee kaarten heeft vóór aankoop een getest backend nodig.** PCIe-generatie, slotafstand, stroomvoorziening, driverondersteuning en exacte quantisatie beïnvloeden het resultaat.

## Opties met één kaart

### RTX 5090

NVIDIA vermeldt voor de RTX 5090 **32 GB GDDR7** en **1.792 GB/s geheugenbandbreedte**. De kaart heeft brede CUDA-ondersteuning, volwassen gereedschap en veel geteste frontends. De huidige CUDA-GPU-tabel vermeldt compute capability 12.0.

De prijs is het probleem. Een nieuwe 5090 biedt een eenvoudige route naar 32 GB, maar de aankoopprijs concurreert met maanden gehuurde acceleratortijd. De kaart verbruikt bovendien tot **575 W totaal grafisch vermogen**, dus het systeem heeft een zware voeding en goede koeling nodig.

### Radeon AI PRO R9700

De R9700 is een AMD-optie in de 32GB-klasse met hoge geheugenbandbreedte en vaak een lagere instapprijs dan de 5090. De waarde hangt sterk van de runtime af. Een standaard llama.cpp-pad levert een bruikbaar resultaat. Een sneller community-backend haalt op dezelfde kaart in sommige gemelde tests veel meer.

Dit toont waarom een GPU-vergelijking twee snelheidkolommen nodig heeft. **Decodesnelheid** meet gegenereerde tokens. **Prefillsnelheid** meet hoe snel het backend de prompt leest vóór de eerste gegenereerde token. Een codebase van 50.000 tokens toont een zwak prefill-pad, ook als decode er goed uitziet.

### Intel Arc Pro B70

De Arc Pro B70 richt zich met 32 GB geheugen op professionele werklasten. De kaart is interessant voor capaciteit per dollar, maar het softwarepad vraagt meer controle dan CUDA-hardware. Standaard GGUF-ondersteuning, aangepaste builds, draft-tokeninstellingen en backendvolwassenheid beïnvloeden het resultaat.

**Een lagere aankoopprijs vergoedt geen uren zoeken naar een werkende build.** Voor een hobbybouwer hoort dit werk bij het project. Voor een workstation voor dagelijks gebruik hebben driver- en applicatieondersteuning echte waarde.

## Gebruikte datacenterkaarten

### Tesla V100

Gebruikte Tesla V100-kaarten met 32 GB krijgen aandacht omdat de kaartprijs laag lijkt. Het complete systeem kost meer. Een passieve datacenterkaart vraagt luchtstroom, een geschikte behuizing of shroud, stroomadapters en een host met genoeg PCIe-ruimte.

De softwareleeftijd is een tweede probleem. De huidige CUDA-GPU-tabel richt zich op nieuwere architecturen en vermeldt V100 niet in de huidige architectuurtabel. Controleer vóór aankoop de CUDA-versie, driverbranch, backend en communityfork.

**Begroot een werkend V100-systeem, geen losse kaart.** Een kaart van ongeveer 680 dollar kan na koeling, adapters en hostplatform een project van ongeveer 1.000 dollar worden. Gebruikte prijzen stijgen ook wanneer een populaire lokale AI-werklast kopers naar dezelfde afgeschreven accelerator stuurt.

### AMD Instinct MI50

De MI50 biedt een aantrekkelijke gebruikte prijs per gigabyte, maar de huidige softwareondersteuning vormt een serieuze beperking. Een kaart die een oudere ROCm-stack of communityfork vereist, is niet gelijk aan een actuele consumentenkaart met brede applicatieondersteuning.

Het gemelde verschil in promptverwerking telt zwaarder dan de stickerprijs. Een vergelijking mat ongeveer **128 tokens per seconde** op een MI50 tegenover ongeveer **2.652 tokens per seconde** op een nieuwere 32GB-kaart. Een codebase van 50.000 tokens duurt vóór generatie minuten op het trage pad en seconden op het snelle pad.

**MI50 past bij een smalle toepassing.** De kaart past bij een bouwer die capaciteit boven interactiesnelheid zet en driveronderhoud accepteert. Voor snelle codebaseanalyse is de kaart zwak wanneer prefill telt.

## Software hoort bij de GPU

llama.cpp ondersteunt CUDA, HIP, Metal, Vulkan, SYCL en andere backends. Het ondersteunt ook hybride CPU-GPU-inferentie en multi-GPU. Deze functies leveren niet dezelfde prestaties bij elke leverancier of modelindeling.

Dezelfde fysieke kaart toont vaak grote verschillen tussen:

- **Een standaard applicatiebuild** met voorzichtige instellingen.
- **Een afgestemde llama.cpp-build** met backend-specifieke kernels.
- **Een communityfork** met speculatieve of multi-tokenvoorspelling.
- **Een aangepast modelindeling** voor één acceleratorpad.

Gemelde resultaten in de vergelijking bevatten ongeveer **27 tokens per seconde** voor een standaard 32GB AMD-pad, ongeveer **46 tokens per seconde** met multi-tokenvoorspelling en veel hogere resultaten op een gespecialiseerd backend. Het resultaat toont softwaremarge. Het belooft geen gelijke uitkomst bij een nieuwe installatie.

**Leg voor elke benchmark backend, commit, modelbestand, quantisatie, contextlengte, promptlengte, batchgrootte en energiestatus vast.** Zonder die velden is tokens per seconde een reclamegetal.

## Huren in plaats van kopen

Een snelle GPU huren verandert de berekening. Een gemelde huurprijs van ongeveer **0,69 dollar per uur** voor een RTX 5090 maakt een aankoop van 4.400 dollar gelijk aan ongeveer **6.377 huururen**, vóór elektriciteit, hosthardware, onderhoud en restwaarde.

Dat is bijna negen maanden continu huren of ongeveer twee jaar bij acht uur per dag. Een desktop met twee kaarten van ongeveer 1.560 dollar staat gelijk aan circa 2.261 uur tegen hetzelfde tarief. De gehuurde 5090 vermijdt ook lokale hitte, geluid, driverinstelling en kaartdefecten.

| Gebruikspatroon | Beste eerste test |
|---|---|
| **Enkele uren per week** | Gehost model of gehuurde GPU |
| **Kort project** | Huur een kaart in de 5090-klasse en meet de echte werklast |
| **Dagelijks interactief gebruik** | Koop pas na testen van backend en context |
| **Agents die 's nachts draaien** | Eigen hardware is eenvoudiger te verantwoorden |
| **Privégegevens met vaste belasting** | Eigen hardware met netwerkisolatie |

**Huur eerst wanneer model, backend of contextlengte nog onzeker zijn.** Een weekend meten kost minder dan een verkeerde workstationaankoop.

## Koopadviezen

### Twee RTX 5060 Ti-kaarten van 16 GB

Twee 16GB-kaarten bieden een praktische CUDA-route voor kopers die 32 GB nodig hebben en gangbare tutorials, drivers en frontends willen. Gebruik tensor splitting pas na controle van modelindeling en backend. Layer splitting is eenvoudiger, maar laat vaak prestaties liggen.

Deze route vraagt ook een moederbord met twee bruikbare slots, voldoende vermogen en luchtstroom tussen de kaarten. Twee kaarten vormen geen kleine workstationbouw zodra platformkosten meetellen.

### Eén kaart van 32 GB

Kies één 32GB-kaart wanneer betrouwbaarheid, garantie en eenvoudige inzet zwaarder wegen dan de laagste geheugenprijs. De R9700 en RTX 5090 vertegenwoordigen verschillende versies van deze keuze. AMD legt de nadruk op capaciteit en prijs. NVIDIA legt de nadruk op softwarebreedte en volwassen CUDA-ondersteuning.

### Een gebruikte V100 of MI50

Kies gebruikte datacenterhardware alleen wanneer het project driverstests, koelwerk en backendonderhoud omvat. De kaartprijs is de eerste begrotingsregel, niet de laatste.

### Apple silicon

Kies een Apple silicon-systeem met 32 GB wanneer stilte, laag idle-verbruik en een compact bureaublad belangrijker zijn dan maximale doorvoer. Controleer de geheugentoewijzing van de exacte runner vóór je aanneemt dat 32 GB voor het model beschikbaar is.

### Cloudhuur

Kies huur wanneer de werklast af en toe voorkomt, het model vaak verandert of een snelle promptreactie belangrijker is dan lokaal eigendom. Zet de instantie na de test uit. Inactieve tijd haalt het prijsvoordeel snel weg.

## Een beter vergelijkingsblad

Leg vóór aankoop deze waarden voor elke kandidaat vast:

- **Bruikbaar modelgeheugen** na runtime-overhead.
- **Gewichtindeling** en verwachte modelgrootte.
- **KV-cachegrootte** bij de doelcontext.
- **Prefillsnelheid** voor een representatieve prompt.
- **Decodesnelheid** nadat de context vol is.
- **Benodigde backend- en driverversie** voor het resultaat.
- **Idle- en geladen vermogen** tegen je lokale stroomtarief.
- **Hostkosten**, koeling, adapters, opslag en garantie.
- **Huur-equivalent** voor het verwachte aantal uren.

De nuttigste test gebruikt een prompt uit je echte werklast. Gebruik voor coding een representatieve codebase. Gebruik voor onderzoek een lang document met de normale retrieval- of plakworkflow. Meet tijd tot eerste token, promptverwerking, generatiesnelheid, geheugen, uitvoerkwaliteit en vermogen.

## Eindadvies

**Koop twee RTX 5060 Ti-kaarten van 16 GB voor de CUDA-build van 32 GB met de minste frictie.** Gebruik tensor split pas nadat een kleine test het backend bevestigt.

**Koop één 32GB-kaart voor een nettere workstation.** Kies de kaart met het sterkste softwarepad voor je runner, niet de kaart met het laagste bedrag per gigabyte.

**Gebruik V100 of MI50 alleen wanneer je het onderhoudsproject accepteert.** Een goedkope accelerator met zwakke prefill is geen koopje voor lange codeprompts.

**Huur een GPU in de 5090-klasse bij onregelmatig gebruik.** De huurtest geeft echte gegevens over geheugen, snelheid en context vóór een grote aankoop.

De vraag over 32 GB is dus niet "Welke kaart heeft de goedkoopste gigabyte?" De vraag is "Welk systeem laat genoeg bruikbaar geheugen over, leest mijn werklast snel, werkt met mijn software en verdient de aankoopprijs terug door regelmatig gebruik?"

## Referenties

- [Every Ways to Get 32GB VRAM for Local AI at Full Context](https://www.youtube.com/watch?v=uavLRbbfM94), videoreferentie voor de besproken praktijkvergelijking.
- [NVIDIA GeForce RTX 5090 specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/), officiële gegevens over VRAM, bandbreedte, vermogen en CUDA-capaciteit.
- [NVIDIA CUDA GPU Compute Capability](https://developer.nvidia.com/cuda/gpus), actuele tabel met architecturen en compute-capability.
- [Apple Mac mini technical specifications](https://www.apple.com/mac-mini/specs/), officiële unified-memoryconfiguraties en bandbreedte.
- [llama.cpp](https://github.com/ggml-org/llama.cpp), ondersteunde inferentiebackends en multi-GPU-documentatie.
- [Qwen3.5 27B model card](https://huggingface.co/Qwen/Qwen3.5-27B), officiële Qwen-referentie voor de actuele 27B-familie en lange context.
- [Local AI in 2026: A 27B Model Beats Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/), verwante analyse van lokale modellen en hardware.
- [Llama 3.1 8B and Qwen3.8 27B GPU Benchmarks on Vast.ai](/articles/qwen38-27b-vast-ai-gpu-benchmark/), verwante analyse van benchmarks op gehuurde GPU's.
- [The 64GB DGX Spark Is a Warning Sign for Local AI Hardware Prices](/articles/dgx-spark-64gb-memory-crisis-2027/), verwante analyse van geheugencapaciteit en aanbod.

## Volgende stappen

Gebruik het blad met een representatieve prompt vóór aankoop. Vergelijk tijd tot eerste token, promptverwerking, decode, geheugen, vermogen en totale platformkosten. Huur bij een kort project eerst en bewaar het meetresultaat bij je aankoopbesluit.
