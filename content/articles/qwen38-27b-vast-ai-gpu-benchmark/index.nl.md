---
title: "GPU-benchmarks van Llama 3.1 8B en Qwen3.8 27B op Vast.ai"
date: 2026-10-02
lastmod: 2026-10-10
toc: true
draft: false
description: "Gemeten Ollama-benchmarks van Llama 3.1 8B en Qwen3.8 27B op belangrijke Vast.ai-GPU's. Vergelijk decodeersnelheid, lange context, huurkosten, self-hosting, API-tegoed en abonnementen."
genre: ["Lokale AI", "GPU-benchmarking", "Self-hosted AI", "Cloud computing", "Kunstmatige intelligentie", "AI-economie"]
tags: ["Llama 3.1 8B", "llama3.1:8b", "Qwen3.8 27B", "Qwen3.8:27b", "Vast.ai", "GPU-benchmark", "Ollama", "H100", "RTX PRO 5000", "RTX 6000 Ada", "RTX PRO 6000 Max-Q", "A100", "CMP 170HX", "lokale LLM", "lange context", "GPU-huur", "self-hosted AI", "abliterated modellen", "ongecensureerde modellen", "API-tegoed", "AI-abonnement", "Q4_K_M", "tokens per seconde"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Hightech werkplek met een grafische kaart en schermen met lokale AI-benchmarkresultaten"
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**De H100 SXM was de snelste kaart in beide Ollama-tests, maar niet de beste waarde.** De RTX PRO 5000 en RTX 6000 Ada boden een betere verhouding tussen snelheid en huurprijs. De CMP 170HX had het laagste uurtarief van de voltooide Qwen3.8 27B-runs.

*Deze resultaten meten één model, één Ollama-wrapper, één standaardkwantisering en één serveerpatroon. Gebruik ze voor deze werklast, niet als algemene GPU-ranglijst.*

Dit artikel vergelijkt **Llama 3.1:8b**, een Ollama Q4_K_M-build met 8,03 miljard parameters, met **Qwen3.8:27b**, een Ollama Q4_K_M-build met ongeveer 27,3 miljard parameters. Beide modellen zijn getest op GPU-instanties van Vast.ai. De tests richtten zich op decodeerdoorvoer bij echte promptlengtes tot de ondersteunde contextlimiet.

## Kort antwoord

**Huur een RTX PRO 5000 of RTX 6000 Ada voor regelmatig werk door één gebruiker.** De RTX PRO 5000 leidde bij korte en middelgrote contexten. De RTX 6000 Ada kostte minder en bleef sneller dan de A100-kaarten. Huur een H100 SXM wanneer reactiesnelheid belangrijker is dan het uurtarief of wanneer lange prompts deel van het werk zijn.

| Doel | Advies | Reden |
|---|---|---|
| **Laagste testkosten** | CMP 170HX | $0.420 per uur en genoeg VRAM voor de geteste Q4_K_M-modellen |
| **Beste waarde onder $1.25/uur** | RTX PRO 5000 of RTX 6000 Ada | Sterke decodeersnelheid zonder H100-huurprijs |
| **Snelste antwoorden** | H100 SXM | Hoogste decodeersnelheid in beide tests |
| **Qwen met lange context** | H100 SXM of RTX PRO 6000 Max-Q | Beide voltooiden de Qwen-run van ongeveer 131k tokens met veel VRAM over |
| **Populaire 8B-baseline** | Llama 3.1:8b | Praktische 8B-vergelijking met 128K-contextlimiet |
| **Kleine terugkerende werklast** | API-tegoed of chatabonnement | Geen kosten voor een inactieve GPU, onderhoud of deployment |
| **Privé en frequent werk** | Eigen GPU-werkstation | Hardwarekosten zijn beter te verantwoorden bij blijvend gebruik |
| **Abliterated of ongecensureerde tests** | Eerst huren, pas na blijvend gebruik kopen | Gedrag, licentie en operationeel risico vragen eerst om een aparte test |

## Wat is getest

**De benchmark gebruikte Ollama met de standaard Q4_K_M-build.** Er is geen speciale kwantisering, speculative decoding, aangepaste sampler of andere serving-stack gebruikt. Het doel was een eenvoudige, lokaal reproduceerbare vergelijking van GPU-instanties.

Vast.ai beschrijft zijn dienst als een GPU-cloudmarktplaats tussen rekenproviders en gebruikers. De documentatie noemt on-demand, gereserveerde, onderbreekbare en serverless opties, met filters voor GPU-model, geheugen, prijs en beschikbaarheid. De uurtarieven hieronder kwamen uit de gekozen instanties tijdens deze sessie, niet uit een vaste prijslijst.

De gemeten uitvoer was **decodeerdoorvoer**, uitgedrukt in gegenereerde tokens per seconde. Prefill-doorvoer staat apart, omdat die promptverwerking meet en niet de snelheid waarmee het antwoord verschijnt. Een lange prompt vraagt vaak veel verwerkingstijd, ook wanneer de decodeersnelheid hoog blijft.

Er waren twee geldige proeven per context. De mediaan van het decodeerresultaat is vastgelegd. De voltooide niveaus waren gebaseerd op echte `prompt_eval_count`-waarden:

- **Ongeveer 16,4k prompttokens**
- **Ongeveer 32,8k prompttokens**
- **Ongeveer 65,5k prompttokens**
- **Ongeveer 131k prompttokens**

De gevraagde run van 256k tokens werd niet voltooid. De A100-kaarten van 40 GB en meerdere kleinere kaarten waren nog bezig of bereikten de doelcontext niet.

> **Benchmarklimiet:** de cijfers beschrijven twee Ollama Q4_K_M-werklasten met één serveerpatroon. Ze voorspellen geen trainingssnelheid, multi-user-doorvoer, beeldgeneratie, vLLM-prestaties of resultaten van een ander model.

## Nieuwe Llama 3.1 8B-run

**Llama 3.1:8b is een praktische baseline voor dezelfde GPU-pool.** Ollama vermeldt ongeveer 120 miljoen downloads, wat het een bruikbare populariteitsbaseline maakt. De [officiële Ollama-modelpagina](https://ollama.com/library/llama3.1:8b) vermeldt een Q4_K_M-build van 4,9 GB, 8,03B parameters en 128K context.

De run gebruikte een modelspecifieke benchmarkrunner met een promptgenerator die op de Ollama-tokenizer was afgestemd. De labels gebruiken echte promptaantallen:

- **Ongeveer 32.676 echte prompttokens** voor het 32k-doel
- **Ongeveer 65.342 echte prompttokens** voor het 64k-doel
- **Ongeveer 130.671 echte prompttokens** voor het 128k-doel

256k is expliciet niet ondersteund, omdat de modelcontext 128K is. De runner hield retries en statusregels bij, zodat time-outs zichtbaar blijven.

### Resultaten Llama 3.1 8B

| GPU | ~32k decode tok/s | ~64k decode tok/s | ~128k decode tok/s |
|---|---:|---:|---:|
| **H100 SXM** | **163.5** | **124.0** | **82.4** |
| **H100 SXM** | **158.6** | **121.2** | **80.6** |
| **RTX PRO 5000** | 110.1 | 79.8 | 49.9 |
| **CMP 170HX 64GB** | 91.9 | 71.0 | 50.1 |
| **RTX 6000 Ada** | 88.3 | 53.9 | 29.3 |
| **RTX PRO 6000 Max-Q** | 66.7 | 53.0 | 40.3 |
| **RTX PRO 6000 S** | 60.3 | 42.5 | 33.9 |
| **A100 SXM4 40GB** | 2.0 | 40.6 | 38.5 |
| **A100 PCIe 40GB** | 1.2 | 20.3 | 20.3 |
| **2x RTX 5060 Ti** | 1.3 | 26.8 | Timeout |

De twee H100-regels kwamen uit afzonderlijke geldige instanties van dezelfde GPU-klasse. Beide liepen duidelijk voor op de andere kaarten. Hun 32k-resultaten waren 44% tot 48% sneller dan de RTX PRO 5000. Bij 128k was de voorsprong ongeveer 61% tot 65%.

De 32k-resultaten van de A100 en RTX 5060 Ti zijn te laag voor een vergelijkbare GPU-run. De RTX 5060 Ti-host time-outte ook tijdens de tweede 128k-proef. Behandel deze host als ongeschikt voor een geldige GPU-vergelijking, niet als een echte ranglijstscore.

| Contextdoel | Status |
|---|---|
| **32k** | Voltooid op alle 10 hosts |
| **64k** | Voltooid op alle 10 hosts |
| **128k** | Voltooid op 9 hosts. De 2x RTX 5060 Ti-host time-outte tijdens de tweede proef |
| **256k** | Niet ondersteund op alle hosts omdat Llama 3.1 8B maximaal 128K context heeft |

## De twee modellen vergelijken

**Het kleinere Llama-model was op elke vergelijkbare GPU sneller, maar modelgrootte en kwaliteit zijn niet uitwisselbaar.** Llama 3.1 8B is een populaire baseline met lagere geheugenvraag. Qwen3.8 27B vraagt meer geheugen en heeft een ander capaciteitsprofiel. Gebruik de cijfers voor hardwarekeuze, niet voor een universeel oordeel.

| Gebruik | Beste benchmarkreferentie | Waarom |
|---|---|---|
| **Snelle 8B-assistent** | Llama 3.1:8b | Hogere decodeersnelheid en lagere geheugenvraag |
| **Lokale 27B-dimensionering** | Qwen3.8:27b | Representatiever voor een groter single-GPU-werkload |
| **128K-contextplafond** | Llama 3.1:8b | De expliciete limiet maakt 256k ongeldig |
| **VRAM-marge testen** | Qwen3.8:27b | Het grotere model toont geheugen- en contextlimieten eerder |
| **Baseline tussen providers** | Llama 3.1:8b | Populariteit en grootte maken reproductie eenvoudiger |

De eerdere Qwen-run corrigeerde de echte promptaantallen naar ongeveer **32.770**, **65.538** en **131.074** tokens. Deze labels vervangen de gevraagde `num_ctx`-waarden bij Qwen-vergelijkingen.

## Ongeveer 16k tokens

**De H100 SXM leidde de korte-context-run met 134,4 decodeertokens per seconde.** De RTX PRO 5000 volgde met 113,9 tokens per seconde en kostte minder dan de helft per uur.

| Rang | GPU | VRAM | Decode tok/s | Prefill tok/s | Huurprijs |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **134.4** | 89,974 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **113.9** | 68,726 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **89.1** | 95,856 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **84.1** | 72,235 | $1.507/hr |
| 5 | **A100 SXM4** | 40 GB | **60.6** | 53,048 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **51.5** | 51,122 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **49.3** | 52,773 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | **38.4** | 38,886 | $0.565/hr |

Op deze lengte haalde de RTX PRO 5000 ongeveer 84,7% van de H100-snelheid tegen 37,3% van het uurtarief. De RTX 6000 Ada haalde 66,3% van de snelheid tegen 30,2% van de prijs.

## Ongeveer 32,8k tokens

**De rangorde bleef stabiel bij middelgrote context.** De H100 SXM daalde naar 120,0 tokens per seconde. De RTX PRO 5000 haalde 105,0 en de RTX 6000 Ada 75,7.

| Rang | GPU | VRAM | Decode tok/s | Prefill tok/s | Huurprijs |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **120.0** | 139,748 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **105.0** | 103,707 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **75.7** | 141,678 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **66.9** | 120,537 | $1.507/hr |
| 5 | **RTX PRO 6000 S** | 95.6 GB | **65.9** | 109,280 | $1.756/hr |
| 6 | **A100 SXM4** | 40 GB | **51.1** | 81,929 | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | **46.2** | 77,984 | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | **36.1** | 73,377 | $0.565/hr |

De RTX PRO 5000 bleef de aantrekkelijkste huurkaart. Hij was 12,5% langzamer dan de H100 en kostte 62,7% minder per uur.

## Ongeveer 65,5k tokens

**Langere prompts toonden een groter verschil tussen kaarten met veel geheugen en kaarten met minder marge.** De H100 bleef eerste met 112,0 tokens per seconde. De RTX PRO 6000 Max-Q haalde de RTX 6000 Ada in.

| Rang | GPU | VRAM | Decode tok/s | Prefill tok/s | Huurprijs |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **112.0** | 195,252 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **96.9** | 148,897 | $1.005/hr |
| 3 | **RTX PRO 6000 Max-Q** | 95.6 GB | **75.7** | 156,443 | $1.507/hr |
| 4 | **RTX 6000 Ada** | 48 GB | **70.8** | 208,400 | $0.813/hr |
| 5 | **A100 SXM4** | 40 GB | **49.3** | 147,699 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **45.9** | 118,657 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **37.0** | 124,927 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | N/A | N/A | $0.565/hr |

De RTX PRO 5000 bleef de beste balans. De RTX 6000 Ada was langzamer, maar de lagere huurprijs past bij een budget waarbij beschikbaarheid belangrijker is dan topsnelheid.

## Ongeveer 131k tokens

**De H100 was de enige kaart boven 100 decodeertokens per seconde bij deze context.** De RTX PRO 6000 Max-Q voltooide de run met 73,4 tokens per seconde, gevolgd door de RTX 6000 Ada met 61,7.

| Rang | GPU | VRAM | Decode tok/s | Prefill tok/s | Huurprijs |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **108.2** | 242,093 | $2.693/hr |
| 2 | **RTX PRO 6000 Max-Q** | 95.6 GB | **73.4** | 197,208 | $1.507/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **61.7** | 278,283 | $0.813/hr |
| 4 | **RTX PRO 6000 S** | 95.6 GB | **39.4** | 124,653 | $1.756/hr |
| 5 | **RTX PRO 5000** | 47.8 GB | N/A | N/A | $1.005/hr |
| 6 | **A100 SXM4** | 40 GB | N/A | N/A | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | N/A | N/A | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | N/A | N/A | $0.565/hr |

De RTX PRO 6000 Max-Q werd het praktische alternatief voor de H100 bij lange prompts. Hij haalde 67,8% van de decodeersnelheid tegen 56,0% van het uurtarief. De RTX 6000 Ada kostte minder, maar 48 GB VRAM laat minder ruimte voor lange prompts, grotere batches of een andere modelconfiguratie.

## Totale decodeervergelijking

| GPU | ~16k | ~32,8k | ~65,5k | ~131k |
|---|---:|---:|---:|---:|
| **H100 SXM** | **134.4** | **120.0** | **112.0** | **108.2** |
| **RTX PRO 5000** | 113.9 | 105.0 | 96.9 | N/A |
| **RTX 6000 Ada** | 89.1 | 75.7 | 70.8 | 61.7 |
| **RTX PRO 6000 Max-Q** | 84.1 | 66.9 | 75.7 | 73.4 |
| **RTX PRO 6000 S** | 49.3 | 65.9 | 37.0 | 39.4 |
| **A100 SXM4** | 60.6 | 51.1 | 49.3 | N/A |
| **CMP 170HX** | 51.5 | 46.2 | 45.9 | N/A |
| **A100 PCIe** | 38.4 | 36.1 | N/A | N/A |

**De H100 leidde bij elke voltooide contextlengte.** Het voordeel daalde van 20,5 tokens per seconde boven de RTX PRO 5000 bij ongeveer 16k naar 12,0 bij ongeveer 32,8k. De waarde hangt af van de keuze tussen de snelste eerste reactie en de laagste kosten voor een lange sessie.

## Kosten per miljoen decodeertokens

**Alleen het uurtarief verbergt de nuttige vergelijking.** Deel het uurtarief door de decodeerdoorvoer om de huurkosten voor één miljoen gegenereerde tokens te schatten. Dit negeert promptverwerking, inactiviteit, opslag, dataverkeer, belasting, kortingen en mislukte runs.

| GPU | Tarief korte context | Geschatte kosten per 1M decodeertokens |
|---|---:|---:|
| **CMP 170HX** | $0.420/hr | $2.27 |
| **RTX PRO 5000** | $1.005/hr | $2.45 |
| **RTX 6000 Ada** | $0.813/hr | $2.53 |
| **A100 SXM4** | $0.680/hr | $3.12 |
| **A100 PCIe** | $0.565/hr | $4.09 |
| **RTX PRO 6000 Max-Q** | $1.507/hr | $4.98 |
| **H100 SXM** | $2.693/hr | $5.57 |
| **RTX PRO 6000 S** | $1.756/hr | $9.89 |

**De CMP 170HX won deze beperkte rekensom.** De RTX PRO 5000 en RTX 6000 Ada volgden dicht daarna en boden beide meer doorvoer. Bij interactief gebruik telt extra wachttijd vaak zwaarder dan de laagste tokenprijs.

## Huren, tegoed kopen, abonneren of hardware kopen?

**De juiste optie hangt af van gebruik en controle.** GPU-huur is een variabele compute-factuur. API-tegoed is een variabele modelfactuur. Een chatabonnement is een vast toegangstarief met gebruikslimieten. Eigen hardware is een kapitaalaankoop met daarna stroom, koeling, onderhoud en afschrijving.

| Maandbudget en werklast | Advies | Waarom | Belangrijkste compromis |
|---|---|---|---|
| **Onder $10** | Koop API-tegoed of gebruik een gratis lokaal model | Test de workflow zonder kosten voor een inactieve GPU | Minder controle over hosting en limieten |
| **$10 tot $30** | API-tegoed voor incidenteel werk, chatabonnement voor dagelijks interactief gebruik | Abonnement past bij chat, tegoed bij scripts en gemeten calls | Geen van beide geeft standaard een privé 27B-endpoint |
| **$30 tot $100** | Huur RTX 6000 Ada of RTX PRO 5000 alleen tijdens actieve sessies | Dekt korte onderzoekssessies zonder eigenaarslasten | Setup, opslag, monitoring en correct afsluiten blijven nodig |
| **$100 tot $250** | Huur een snelle kaart voor gepland werk of test een eigen werkstation | Maandelijks gebruik wordt zichtbaar | Beschikbaarheid en tarieven veranderen |
| **$250 tot $600** | Vergelijk een maand RTX PRO 5000 met lokale GPU | Beslispunt voor frequent privé-infereren | Hardware voegt stroom, warmte, support en restwaarderisico toe |
| **Boven $600** | Koop alleen bij hoge benutting of huur H100 voor pieken | Een gemengde strategie voorkomt eigendom van piekhardware | Kapitaal zit vast in één configuratie |

Deze bedragen zijn beslisrichtlijnen, geen offertes. Een H100 van $2.693 per uur kost ongeveer $64.63 per continue dag en $1,941.00 per 30 dagen. Een RTX PRO 5000 van $1.005 per uur kost ongeveer $24.12 per dag en $723.60 per 30 dagen. Een kaart die alleen tijdens actieve sessies draait heeft een ander totaal.

### Wanneer API-tegoed wint

**API-tegoed wint bij onregelmatig gebruik, automatisering en wanneer een specifiek lokaal model niet vereist is.** Het voorkomt GPU-provisioning, modeldownloads, driverproblemen en inactiviteit. Je kunt meerdere gehoste modellen vergelijken voordat je hardware koopt.

API-prijzen verschillen per model en provider. De modelcatalogus van OpenRouter vergelijkt context, providers en tokenprijzen. Gebruik de actuele calculator van de provider voordat je een API-factuur met deze benchmark vergelijkt. Een lokale GPU heeft geen kosten per token, maar de huur loopt door terwijl de instantie wacht.

### Wanneer een abonnement wint

**Een abonnement past bij iemand die elke dag een gehoste assistent gebruikt.** De individuele Claude-plannen onderscheiden bijvoorbeeld Free, Pro en Max met verschillende limieten en functies. Een abonnement is geen API-toegang. Het biedt vaak een interface en gebundelde tools, terwijl API-tegoed programmatische controle geeft.

Kies een abonnement voor interactief schrijven, onderzoek, coderen of bestandscontrole. Kies API-tegoed wanneer een script, applicatie of agent een meetbaar endpoint nodig heeft.

### Wanneer Vast.ai wint

**Vast.ai wint wanneer je een open model, private runtimecontrole of korte hoge doorvoer nodig hebt.** Selecteer de GPU, start de instantie, draai Ollama, test een model en stop de instantie daarna. Dit past bij Qwen3.8 27B, abliterated varianten en modelbestanden die niet op een laptop passen.

De prijs brengt operationeel werk mee. Controleer GPU-gebruik, bewaak VRAM, bescherm de blootgestelde service, bewaar benodigde modelbestanden en stop de instantie na de run. Een laag uurtarief verhelpt geen vergeten instantie.

### Wanneer een GPU kopen wint

**Hardware kopen wint bij blijvend gebruik, stabiele modelvereisten en behoefte aan lokale controle.** Je verwijdert beschikbaarheidsrisico en krijgt een vaste omgeving. Je kunt privégegevens verwerken zonder prompts naar een gehoste provider te sturen.

De aankoopprijs is slechts één deel. Voeg host, voeding, opslag, koeling, stroom, vervanging en configuratietijd toe. Een dure kaart staat ook stil wanneer API-tegoed of een abonnement goedkoper is.

NVIDIA noemt voor de RTX 4090 24 GB geheugen, 450 W totaal grafisch vermogen en 850 W aanbevolen systeemvermogen. Dit is een nuttig lokaal referentiepunt, maar 24 GB ligt onder de geteste 27B Q4_K_M-configuraties. Controleer werkelijk geheugengebruik en ga niet alleen van parameteraantal uit.

## Abliterated en ongecensureerde modellen

**Abliterated en ongecensureerde varianten veranderen de koopbeslissing.** Ze trekken aan door minder weigeringen of beperkingen. Kosten zijn zwakker veiligheidsgedrag, onzekere herkomst, inconsistente promptopmaak, meer controlewerk en mogelijke licentie- of gebruiksbeperkingen.

Huur voor deze modellen eerst. Een dag RTX PRO 5000 tegen het opgegeven tarief kost ongeveer $24.12 vóór andere kosten. Dat is genoeg om modelgeschiktheid, GPU-gebruik, antwoordkwaliteit en operationeel risico te testen.

**Stel een ongecensureerd model niet rechtstreeks bloot aan het openbare internet.** Zet authenticatie, snelheidslimieten, logcontroles en netwerkisolatie ervoor. Stuur geen persoonlijke, vertrouwelijke of gereguleerde gegevens naar een niet-beoordeelde modelbron.

Als het model dagelijks wordt gebruikt, vergelijk dan de maandhuur met de volledige kosten van een eigen werkstation. Bij incidenteel gebruik blijft huren eenvoudiger te stoppen en te vervangen.

## Benchmarkvoorbehouden

**Ontbrekende resultaten zijn onderdeel van het resultaat.** `N/A` betekent dat de run geen geldige meting opleverde. Het betekent niet dat de GPU zo langzaam is als de score van een andere kaart suggereert.

- **De tweede H100-instantie leverde geen geldige set op**, omdat de modeldownload te laat klaar was.
- **De 2x RTX 5060 Ti-instantie is uitgesloten**, omdat Ollama het model op de CPU laadde.
- **De Qwen3.8 27B-prompt van 256k tokens is niet voltooid.** Het hoogste geldige niveau was ongeveer 131k echte prompttokens. Llama 3.1 8B ondersteunt 256k niet en heeft een limiet van 128K.
- **Het gevraagde `num_ctx` is niet als ranglijstlabel gebruikt.** De eindtabellen gebruiken echte `prompt_eval_count`-waarden.
- **Twee geldige proeven per context zijn samengevat met de decodeermediaan.** Dit beperkt het effect van één trage run, maar vervangt geen grotere testset.
- **De wrapper was bewust eenvoudig.** Een afgesteld vLLM- of llama.cpp-deployment geeft een andere rangorde.

## Eindadvies

**Begin met een RTX 6000 Ada of RTX PRO 5000 op huurbasis.** De RTX 6000 Ada is de budgetkeuze wanneer $0.813 per uur beschikbaar is. De RTX PRO 5000 is de snellere keuze onder H100-prijs. Gebruik H100 SXM voor lange prompts, veeleisende interactieve latency of een korte benchmark waarbij tijd belangrijker is dan huurkosten. Voor een 8B-model is CMP 170HX het testen waard wanneer een laag uurtarief belangrijker is dan topsnelheid.

**Koop geen GPU na één geslaagde test.** Huur een maand voor echte werklasten, noteer actieve uren, promptlengtes, gelijktijdigheid en modelwissels en vergelijk de huur met de volledige eigenaarskosten. Koop wanneer de werklast de kaart vaak gebruikt en stabiel genoeg is.

Voor incidenteel werk zijn API-tegoed of een chatabonnement eenvoudiger. Voor privé-inferentie, open modellen of abliterated tests biedt Vast.ai een route met minder verplichting dan direct een werkstation kopen. Gebruik Llama 3.1 8B als laag-geheugenbaseline en Qwen3.8 27B wanneer het grotere model het echte doel is.

## Volgende stappen

Herhaal de vergelijking met eigen promptlengtes en een schatting van actieve uren. Controleer GPU-gebruik, noteer modelrevisie en runtimeversie, stop de instantie na elke run en vergelijk de maandhuur met de volledige eigenaarskosten voordat je hardware koopt.

## Bronnen

1. [Vast.ai GPU-cloudmarktplaats](https://vast.ai/)
2. [Vast.ai-documentatie: marktplaats, instanties, prijzen en huurtypen](https://docs.vast.ai/)
3. [Ollama Qwen3-modellenbibliotheek](https://ollama.com/library/qwen3)
4. [Ollama Llama 3.1 8B-modelpagina](https://ollama.com/library/llama3.1:8b)
5. [OpenRouter-modelcatalogus en prijsvergelijking](https://openrouter.ai/models)
6. [Claude-prijzen en individuele abonnementen](https://www.anthropic.com/pricing)
7. [NVIDIA GeForce RTX 4090-specificaties](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/)
8. [Lokale AI in 2026: Qwen3.8 27B en hardware voor self-hosted modellen](/articles/local-ai-2026-build-your-rig-now/)
9. [Ollama-modeltests op Raspberry Pi-hardware](/articles/ai-models-raspberry-pi-4-5/)
