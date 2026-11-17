---
title: "Zo kies je een ongecensureerd lokaal AI-model"
date: 2026-11-15
lastmod: 2026-11-15
toc: true
draft: false
description: "Vergelijk lokale modelvarianten op voltooide antwoorden, behouden mogelijkheden, contextgebruik, kwantisatie en passend VRAM-gebruik."
genre: ["Lokale AI", "Zelfgehoste AI", "AI-veiligheid", "GPU-apparatuur"]
tags: ["ongecensureerde lokale AI", "abliteratie", "lokale LLM", "VRAM", "contextlengte", "kwantisatie", "Ollama", "Qwen3.8", "Gemma 4"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Een lokaal AI-werkstation met een grafische kaart en monitoren met model- en inferentievisualisaties"
coverCaption: ""
ref: ["/articles/local-ai-model-gpu-context-guide", "/articles/qwen38-27b-vast-ai-gpu-benchmark"]
---

**Modelkeuze:** beoordeel elke variant op de bruikbare antwoorden die het model afrondt, de kwaliteit die behouden blijft en het geheugen dat je werklast nodig heeft. Een laag aantal weigeringen of een populair modelkaartje bewijst die resultaten niet.

Het label **ongecensureerd** heeft geen gestandaardiseerde prestatiemaatstaf. Uitgevers van modellen gebruiken het voor uiteenlopende aanpassingen van gewichten, fijn afgestelde modellen en sjablonen voor gesprekken. Vergelijk elke kandidaat met het oorspronkelijke model en test de taken die je wilt uitvoeren.

{{< youtube id="j-VqPVjztJE" enable="true" title="Ik testte elk ongecensureerd lokaal AI-model (van 8 GB tot 32 GB VRAM)" description="Een vergelijking van lokale modelvarianten, afgeronde antwoorden, contextinstellingen en GPU-geheugenniveaus." >}}

## Wat het label je vertelt

Een **geablitereerd model** heeft aanpassingen aan de gewichten gekregen om bepaald weigeringsgedrag te veranderen. Het artikel uit 2024 over de weigeringsrichting liet één methode zien bij 13 open chatmodellen. Nieuwere hulpmiddelen bieden meer benaderingen. Heretic 2 beschrijft bijvoorbeeld zowel ablatie met willekeurige rang als directionele ablatie. Het label op een modelkaart vertelt niet welk gedrag veranderde of wat de aanpassing heeft beïnvloed.

Houd deze vier eigenschappen gescheiden wanneer je modellen vergelijkt:

| Eigenschap | Wat je controleert |
|---|---|
| **Weigeringsgedrag** | Op welke verzoeken volgt een weigering, een gedeeltelijk antwoord of een volledig antwoord? |
| **Behoud van mogelijkheden** | Hoe verhouden feitelijke, redenerings-, codeer- en opmaaktaken zich tot het oorspronkelijke model? |
| **Voltooide antwoorden** | Hoe vaak eindigt de generatie vóór de token- of tijdslimiet? |
| **Geschiktheid voor de uitvoeringsomgeving** | Draait precies dit gekwantiseerde bestand met genoeg geheugen voor de context die je nodig hebt? |

Een aangepast model blijft probabilistisch. **Controleer kwaliteit op afzonderlijke punten:** nauwkeurigheid, betrouwbaarheid en veilig gebruik. Houd een normaal uitgelijnd model beschikbaar voor werk waarbij de beveiligingen van belang zijn.

## Waarom weigeringsaantallen een zwakke rangschikking vormen

**Een weigeringsscore** meet één uitkomst op één verzoekenset. De score zegt weinig over feitelijke juistheid, antwoordlengte of de vraag of het model een definitief antwoord geeft voordat het generatiebudget op is.

**Sapwells vergelijking van Qwen3.8-27B uit september 2026** testte het basismodel en acht varianten met dezelfde serverconfiguratie. De suite met 13 taken mat kennis, wiskunde, coderen en waarheidsgetrouwheid. Een aparte HarmBench-set bevatte 400 schadelijke verzoeken, en een LLM-beoordelaar bekeek de volledige antwoorden. Deze resultaten gelden voor één modelfamilie, één GPU en één evaluatieopzet.

| Qwen3.8-27B-variant in het onderzoek | Expliciete weigeringen van 400 | Antwoorden met onafgemaakte redenering |
|---|---:|---:|
| **Basismodel** | 381 | 0% |
| **OrcaRouter** | 2 | 38% |
| **Trohrbaugh** | 122 | 15% |

Het hoge weigeringsaantal van het basismodel viel samen met minder onafgemaakte antwoorden. Het lage weigeringsaantal van OrcaRouter viel samen met een hoger percentage onvoltooide antwoorden. Trohrbaugh behield meer weigeringen en gaf minder onafgemaakte antwoorden. **Stem je keuze af op je taak en de afwegingen die je accepteert.**

**Een onderzoek naar 23 Gemma 4 E4B-varianten** vond bij de meest gedownloade variant aanzienlijke verliezen op sommige mogelijkheden, terwijl een kleinere aanpassing in de tests dicht bij het basismodel bleef. Populariteit en downloads zeggen iets over gebruik. Ze meten geen kwaliteit.

Voeg deze metingen niet samen tot één score. **Houd de metingen apart:** weigering, afronding, juistheid en vertraging. Noteer ook de verzoekenset, modelversie, gespreksjabloon, uitvoeringsomgeving, context en uitvoerlimiet. Elke wijziging in die instellingen verandert de betekenis van de vergelijking.

## Onderzoek lege antwoorden voordat je een model vervangt

**Redeneertokens** tellen mee voor de uitvoerlimiet voordat er zichtbare tekst verschijnt. Als de limiet tijdens intern denken opraakt, geven sommige uitvoeringsomgevings een leeg of afgebroken antwoord terug. Dit verschilt van een weigering of een onjuist maar afgerond antwoord.

**Sapwells benchmark van Qwen3.6-27B** liet zien hoe dit de totaalscores beïnvloedt. De ruwe rekenscores liepen sterk uiteen omdat sommige uitvoeringen nooit tot een eindantwoord kwamen. Bij afgeronde antwoorden lagen de gemeten nauwkeurigheidswaarden veel dichter bij elkaar. De benchmark onderscheidde het antwoordvermogen van uitputting van het denkbudget.

**Controleer de stopreden van de uitvoeringsomgeving en de logboeken** wanneer een antwoord leeg is. Noteer de verzoeklengte, contexttoewijzing, uitvoertokenlimiet, verstreken tijd en of het model een marker voor het eindantwoord produceerde. Herhaal daarna de verzoek met een ruimere uitvoerlimiet als de apparatuur genoeg ruimte heeft.

| Resultaat | Waarschijnlijke categorie om te onderzoeken |
|---|---|
| **Weigeringstekst** | Het model wees het verzoek af. |
| **Lege uitvoer bij de tokenlimiet** | De uitvoerlimiet raakte op voordat er een eindantwoord kwam. |
| **Afgebroken uitvoer** | De generatielimiet stopte een onvolledig antwoord. |
| **Fout in de uitvoeringsomgeving** | De server, het modelbestand of de geheugentoewijzing is mislukt. |
| **Afgerond maar fout antwoord** | Het model gaf tekst terug, maar slaagde niet voor de juistheidscontrole. |

**Lege uitvoer:** controleer eerst het resultaat van de uitvoeringsomgeving voordat je elk geval een modelfout noemt. Een groter contextvenster lost een kleine uitvoerlimiet, een verkeerd geconfigureerde sjabloon of een applicatietime-out niet vanzelf op.

## Reserveer VRAM voor gewichten en context

Het modelbestand is slechts één geheugengebruiker. De uitvoeringsomgeving heeft ook ruimte nodig voor de **KV-cache**, die de aandachtsstatus van de actieve verzoek en het antwoord bewaart, plus rekenbuffers en andere geladen processen. Een langere context verhoogt het geheugengebruik.

**De actuele documentatie van Ollama** vermeldt standaardcontextvensters van 4K bij minder dan 24 GiB VRAM, 32K tussen 24 en 48 GiB en 256K bij 48 GiB of meer. Deze standaarden beschrijven uitvoeringsomgevinggedrag. Controleer de toegewezen context en processorplaatsing met `ollama ps`.

**Linux-voorbeeld:** deze opdracht stelt een standaard van 16K in voor nieuwe Ollama-serversessies:

```bash
OLLAMA_CONTEXT_LENGTH=16384 ollama serve
```

**Controleer de toegewezen context** aan de hand van normale invoer- en antwoordgroottes met het geladen model:

```bash
ollama ps
```

De kolommen `CONTEXT` en `PROCESSOR` tonen de toewijzing en of het model op de GPU draait of gedeeltelijk is uitgeladen. **Contexttoewijzing:** een vermelde limiet garandeert niet dat het volledige venster in VRAM past.

### Startpunten op basis van GPU-geheugen

**Startkandidaten:** deze modelfamilies kwamen voor in vergelijkingen van varianten uit 2026. De bestandsgroottes komen uit specifieke repositories met gekwantiseerde bestanden. Controleer het exacte bestand, de uitvoeringsomgevingsupport en het gemeten geheugengebruik voordat je aanneemt dat een kandidaat past.

| GPU-geheugen | Startkandidaat | Belangrijkste beperking |
|---|---|---|
| **8 GB** | Gemma 4 E4B, zoals de `coder3101`-variant | Houdt het gewichtsbestand klein. Laat geheugen vrij voor context en uitvoeringsomgevingbuffers. |
| **12 GB** | Gemma 4 12B, zoals het GGUF Q4-bestand van 7,4 GB van `TrevorJS` | Biedt meer modelcapaciteit, maar minder ruimte voor lange context dan een kleinere variant. |
| **16 GB** | Een kleiner model of een Qwen3.8-27B Q3-bestand | De Qwen-repository vermeldt 13,72 GB voor Q3_K_S. De uitgever bestempelt dit bestand als lage kwaliteit. De ruimte voor context is beperkt. |
| **24 GB** | Qwen3.8-27B Q4_K_S of Q4_K_M | De huidige repository vermeldt bestanden van 16,71 GB en 17,77 GB. Reserveer ruimte voor de cache en buffers. |
| **32 GB** | Qwen3.8-27B Q6_K | De huidige repository vermeldt een bestand van 23,46 GB. Een groter bestand laat minder contextgeheugen over dan een kleinere quant. |

*Gebruik dit als startpunt. Repositories en versies veranderen, en de bestandsgrootte voorspelt op zichzelf niet de uitvoeringsomgevinggeheugentoewijzing of antwoordkwaliteit.*

GGUF-kwantisatielabels vatten een coderingskeuze samen. **Verschillen tussen repositories:** bestanden met dezelfde nominale bitdiepte hoeven niet dezelfde kwaliteit te hebben. Een Qwen-repository noemt Q3_K_S lage kwaliteit en Q4_K_M de standaardkeuze. Bekijk vóór het downloaden het exacte bestand, de modelkaart, het verzoekformaat en de testresultaten.

**Voor cachegrootte en geschiktheid voor een lokale GPU** kun je de [gids voor lokale modellen, GPU's en context](/articles/local-ai-model-gpu-context-guide/) raadplegen. De aanbevelingen richten zich op programmeerwerk. Deze pagina behandelt aangepast weigeringsgedrag en evaluatie.

## Bekijk de gespreksjabloon en de herkomst van het model

Een **gespreksjabloon** verpakt berichten in de tokens en instructies die het model verwacht. Een modelpakket bevat soms een aangepaste sjabloon of systeeminstructie. Die wijzigingen beïnvloeden het gemeten gedrag, zelfs wanneer de onderliggende gewichten hetzelfde blijven.

**Effect van de sjabloon:** Sapwell vond een Qwen3.8-variant waarvan het pakket een persoonlijkheidsinstructie bevatte die het model opdroeg nooit te weigeren of te waarschuwen. De claim van weinig weigeringen hing af van de sjabloon. In zijn vergelijking waren de sjabloons gelijkgetrokken zodat de test verschillen tussen de gewichten benadrukte. Die controle bewijst niet dat de meegeleverde sjabloon kwaadwillig of onbruikbaar is.

**Controleer vóór installatie:** de uitgever, het basismodel, de licentie, het conversieproces, de kwantiseerder, de sjabloon en de revisiegeschiedenis. Vergelijk het model met het origineel onder dezelfde sjabloon en uitvoeringsomgeving. Noteer de herkomst als onbekend wanneer de modelkaart de methode of testopzet niet beschrijft.

## Voer een kleine evaluatie uit voor je werklast

**Stel een herhaalbare verzoekenset samen** met gewone taken die van jou zijn of waarvoor je toestemming hebt om ze te testen. Neem het werk op dat het model gaat doen, feitelijke vragen met bekende antwoorden en opmaakverzoeken met duidelijke slaagvoorwaarden. Voeg enkele veilige grensgevallen toe zodat weigeringsgedrag meeweegt in de keuze.

**Houd de testinstellingen gelijk** voor het oorspronkelijke model en de aangepaste variant. Verander de systeeminstructie, sjabloon, kwantisatie, versie van de uitvoeringsomgeving, context, uitvoerlimiet en steekproefinstellingen niet. Bewaar de modelversie of bestandshash bij de resultaten.

Registreer elke uitkomst afzonderlijk:

- **Afronding:** eindantwoord, weigering, lege uitvoer, afgebroken antwoord of uitvoeringsomgevingfout.
- **Juistheid:** geslaagd of mislukt volgens een verwacht antwoord of beoordelingsschema.
- **Bruikbaarheid:** of het antwoord aan de taakeisen voldoet.
- **Vertraging:** tijd tot het eerste token en totale generatietijd.
- **Geheugen:** toegewezen context, GPU-plaatsing en maximaal VRAM-gebruik.
- **Veilig gedrag:** passend weigeren of doorgaan bij elk grensgeval.

Herhaal de set nadat je één variabele hebt gewijzigd. Als het antwoord compleet wordt nadat je de uitvoerlimiet verhoogt, kwam de eerste fout door het budget. Blijven antwoorden onvolledig, controleer dan de modelsjabloon, redeneermodus, uitvoeringsomgeving en modelversie. **Behoud de variant alleen als die je doeltaak verbetert zonder onaanvaardbaar verlies aan nauwkeurigheid of veiligheid.**

## Houd de implementatie afgeschermd

**Privacy:** lokale inferentie hangt af van je volledige systeemopstelling. Controleer je gebruikersinterface, logboeken, extensies, telemetrie en netwerkpaden. Behandel niet-vertrouwde gewichten en aangepaste sjabloons als code en configuratie van derden.

**Openbare toegang:** stel het modeleindpunt nooit rechtstreeks bloot aan het openbare internet. Isoleer toegang tot hulpmiddelen en gebruik aangepaste varianten alleen voor toegestaan werk. Plaats het eindpunt voor externe toegang achter een privégateway met authenticatie, verzoeklimieten en netwerkisolatie. Het oorspronkelijke onderzoek naar de weigeringsrichting beschrijft de veiligheidsgevolgen van aanpassingen die weigeringen verwijderen.

## Conclusie

**Beslisregel:** kies het model met de sterkste geverifieerde resultaten op je eigen takenpakket. Gebruik weigeringsaantallen als één maatstaf en controleer daarna antwoordafronding, juistheid, sjabloongedrag en VRAM-ruimte. Begin met een bestand dat bij je GPU past, stel de context voor je werklast in en vergelijk het met het oorspronkelijke model onder dezelfde instellingen.

**Voor GPU-capaciteit** kun je deze resultaten vergelijken met de [Qwen 27B GPU-huurbenchmark](/articles/qwen38-27b-vast-ai-gpu-benchmark/). Huur of leen apparatuur voordat je die koopt wanneer je onzeker bent over het exacte modelbestand of de gewenste context.

## Bronnen

- [Benchmark van Qwen3.8-27B-abliteratie](https://nathan.sapwell.net/posts/qwen38-27b-abliteration/), Nathan Sapwell, 6 september 2026.
- [Benchmark van Qwen3.6-27B-abliteratie](https://nathan.sapwell.net/posts/qwen36-27b-abliteration/), Nathan Sapwell, 2026-05-17.
- [Benchmark van Gemma 4 E4B-varianten](https://nathan.sapwell.net/posts/gemma4-e4b-abliteration/), Nathan Sapwell, 1 augustus 2026.
- [Benchmark van Gemma 4 12B-varianten](https://nathan.sapwell.net/posts/gemma4-12b-abliteration/), Nathan Sapwell, 28 augustus 2026.
- [Weigering in taalmodellen wordt gestuurd door één richting](https://arxiv.org/abs/2406.11717), Arditi e.a., 2024.
- [Documentatie van het Heretic-project](https://github.com/p-e-w/heretic/).
- [Officiële modelkaart van Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B).
- [Documentatie van Ollama over contextlengte](https://docs.ollama.com/context-length).
- [Modelkaart van Gemma 4 E4B `coder3101`](https://huggingface.co/coder3101/gemma-4-E4B-it-heretic).
- [GGUF-bestanden voor Gemma 4 12B van TrevorJS](https://huggingface.co/TrevorJS/gemma-4-12B-it-uncensored-GGUF).
- [GGUF-bestanden voor OrcaRouter Qwen3.8-27B](https://huggingface.co/bartowski/orcarouter_Qwen3.8-27B-Uncensored-GGUF).
- [GGUF-formaat en kwantisatietypen](https://huggingface.co/docs/hub/en/gguf), documentatie van Hugging Face.
- [Videobron: Ik testte elk ongecensureerd lokaal AI-model (van 8 GB tot 32 GB VRAM)](https://www.youtube.com/watch?v=j-VqPVjztJE).
