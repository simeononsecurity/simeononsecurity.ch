---
title: "Lokale AI in 2026: een 27B-model verslaat Sonnet 4.6 terwijl het hardwarevenster sluit"
date: 2026-09-22
lastmod: 2026-11-14
toc: true
draft: false
description: "Plan een lokale AI-pc voor 2026 op basis van modelgrootte, VRAM, geheugenbandbreedte, stroomverbruik, kosten en upgrademogelijkheden."
genre: ["Lokale AI", "Zelfgehoste AI", "Open modellen", "AI-apparatuur", "Machinaal leren", "Kwantisering", "Thuislab", "Gegevensbescherming", "AI-economie", "Consumentenelektronica"]
tags: ["lokale ai", "llm lokaal draaien", "qwen3.8", "qwen3.8 27b", "bonsai 2 27b", "ternary bonsai", "prism ml", "ternaire kwantisering", "1.58-bitkwantisering", "llm-kwantisering", "claude sonnet 4.6", "sonnet 4.6 versus lokaal model", "open gewichten", "model met expertsamenvoeging", "expertsamenvoeging", "ollama", "llama.cpp", "rtx 5090", "vram", "lokale inferentie", "gpu-prijzen 2026", "dram-tekort", "geheugenprijzen", "lokale ai-pc bouwen", "thuislab-ai", "ai-abonnementskosten", "openrouter", "artificial analysis", "gpu-koopgids", "zelfgehoste llm", "privacyvriendelijke ai", "ai-apparatuur 2026"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Een hightech werkruimte met één grafische kaart en meerdere oplichtende schermen met AI-benchmarks en visualisaties, tegen een donkerblauwe achtergrond."
coverCaption: ""
ref: ["/articles/ai-models-raspberry-pi-4-5", "/articles/building-a-privacy-preserving-meshtastic-ai-assistant"]
---

**Een downloadbaar model dat op één grafische kaart voor consumenten past, scoort nu hoger dan een frontier-API-model op de samengestelde intelligentie-index.** Qwen3.8 27B is een open-gewicht vision-language-model dat in augustus 2026 verscheen. De ternaire herverpakking, Bonsai 2 27B, brengt dezelfde gewichten terug tot 5.53 GiB. Samen markeren ze het moment waarop lokale inferentie ophield een hobbyistisch compromis te zijn en een serieus alternatief voor een betaalde API werd.

*De hardwarekant van dit verhaal sluit snel. Geheugen is in twintig jaar niet zo duur geweest, en die prijzen stuwen ook de prijzen van grafische kaarten omhoog.*

Dit artikel behandelt wat de benchmarks laten zien, wat de twee modellen precies zijn, waar het open model nog verliest en waarom de komende twaalf maanden geen goed moment zijn om te wachten.

**Wat je eraan overhoudt:** kies een model en geheugenniveau op basis van je werklast. Vergelijk daarna de hardwarekosten, stroomkosten, contextlengte en gemeten doorvoer voordat je iets koopt. De benchmarkvergelijking voorspelt niet hoe goed een model jouw taak uitvoert of wat je toekomstige videokaart kost.

## Het korte antwoord

**Het intelligentieverschil tussen een lokaal 27B-model en een betaalde API vlak onder de frontier is verdwenen. De resterende voordelen van het betaalde model zijn kleiner dan het prijsverschil doet vermoeden.**

Er veranderden drie dingen tegelijk:

- **Open 27B-modellen bereikten scores vlak onder de frontier.** Qwen3.8 27B haalt een Intelligence Index van 33.7 tegenover 30.1 voor Sonnet 4.6, op dezelfde evaluatieset.
- **Ternaire kwantisering verlaagde de geheugenbehoefte met ongeveer twee derde.** Bonsai 2 27B draait het volledige 27B-model in **5.53 GiB**, genoeg voor kaarten van enkele honderden dollars.
- **De geheugentoevoer verslechterde.** De contractprijzen voor conventionele DRAM stegen begin 2026 kwartaal op kwartaal met **90 tot 95 procent**. Dat is de grootste kwartaalstijging die TrendForce heeft geregistreerd en duwde de volgende generatie GPU's door naar 2028.

*Nu kopen of bouwen is de goedkope keuze. Dit is geen verkooppraatje, maar wat de leveringsgegevens laten zien.*

## Bekijk de demonstratie met één GPU

De claim hierboven verdient een demonstratie, geen tabel. Bijan Bowen testte Bonsai 2 27B op een machine met één GPU en vroeg of dit nu het beste model voor één kaart is.

{{< youtube id="OA5cICIzD-c" enable="true" title="Bonsai 2 27B eerste test – is DIT het beste AI-model voor één GPU?" description="Een eerste blik op het draaien van het ternaire Bonsai 2-model met 27B parameters op één GPU voor consumenten, met aandacht voor snelheid, kwaliteit en alternatieven." >}}

*Let op de kwaliteit van de uitvoer, niet op het aantal tokens dat elke seconde wordt verwerkt. Snelheid is het eenvoudigste probleem om op te lossen.*

## Twee labels, dezelfde gewichten

De twee modellen die je hier moet kennen, concurreren niet met elkaar. **Het zijn dezelfde gewichten met twee verschillende precisies.**

| | Qwen3.8 27B | Ternaire Bonsai 2 27B |
|---|---|---|
| **Wat het is** | Het oorspronkelijke open-gewichtmodel van Qwen | Een ternaire herverpakking van Qwen3.8-27B door Prism ML |
| **Gewichten op schijf** | **18 GB** | **5.53 GiB** (PTQ1_0) of **6.70 GiB** (PQ2_0) |
| **Parameters** | 27B dicht | 26.90B, dezelfde architectuur |
| **Context** | 256K | 262,144 tokens |
| **Beeldverwerking** | Ja, ingebouwd | Ja, aparte CLIP-projectorverpakking |
| **Toolaanroepen** | Ja | Ja |
| **Licentie** | Apache 2.0 | Apache 2.0 |
| **Runtime** | Ollama, llama.cpp, MLX | Alleen **de llama.cpp-fork van Prism ML** |

De Ollama-bibliotheekpagina voor `qwen3.8` vermeldt het 27B-model met **18 GB**, een contextvenster van 256K, vision-ondersteuning, toolaanroepen en een aparte MLX-build voor Apple Silicon. De ternaire herverpakking op Ollama is een spiegel van de Apache-2.0-GGUF-pakketten van Prism ML, opnieuw gepubliceerd met overeenkomende checksums.

**De praktische vraag is dus niet welk model je moet kiezen.** De vraag is hoeveel geheugen je wilt besteden aan dezelfde intelligentie. De ternaire versie gebruikt ongeveer een derde van het geheugen en levert weinig in.

{{< figure src="local-ai-architecture-comparison.webp" alt="Diagram vergelijkt dezelfde 27B-modelvoetafdruk: 18 GB met standaardprecisie tegenover 5.53 GiB met ternaire gewichten, beide passend op één GPU voor consumenten" >}}

## Vergelijking van de meetresultaten

Artificial Analysis beoordeelt beide modellen met dezelfde testset. Lees de resultaten per rij in plaats van ze samen te vatten, want de modellen winnen op verschillende punten.

| Meetwaarde | Qwen3.8 27B | Claude Sonnet 4.6 | Leider |
|---|---|---|---|
| **Intelligence Index** | **33.7** | 30.1 | Open |
| **Coding Index** | **68.1** | 63.0 | Open |
| **Agentic Index** | **45.8** | 31.8 | Open |
| **GPQA Diamond** | **90.5%** | 87.5% | Open |
| **Humanity's Last Exam** | **33.9%** | 33.6% | Open |
| **AA-LCR (lange context)** | **82.0%** | 80.0% | Open |
| **GDPval-AA** | **45.4%** | 36.0% | Open |
| **CritPt (onderzoeksfysica)** | **5.4%** | 3.1% | Open |
| **Niet-hallucinatiepercentage** | **69.7%** | 51.6% | Open |
| **SciCode** | 46.6% | **50.1%** | Sonnet |
| **AA-Omniscience-nauwkeurigheid** | 15.6% | **40.9%** | Sonnet |

*Het open model leidt in negen van de elf vergelijkbare rijen, waaronder elke samengestelde index.*

### Waar modellen met vrij beschikbare gewichten winnen

De drie samengestelde indexen halen de kop. **Intelligence 33.7 tegenover 30.1, Coding 68.1 tegenover 63.0, Agentic 45.8 tegenover 31.8.** Het verschil bij agentische taken is het grootst. Het telt vooral voor wie geautomatiseerde workflows met meerdere stappen uitvoert in plaats van losse prompts.

Artificial Analysis plaatst Qwen3.8 27B voor context bij het **agentische index beter dan 86 procent van de modellen** en voor coderen beter dan 76 procent. Sonnet 4.6 staat respectievelijk op 68 en 72 procent. Voor wetenschappelijk redeneren op masterniveau haalt het open model **90.5 procent** op GPQA Diamond.

### Waar Sonnet 4.6 nog wint

Twee rijen wijzen de andere kant op, en geen van beide is onbelangrijk.

**AA-Omniscience meet of een model kennisvragen meteen correct beantwoordt. Sonnet 4.6 scoort 40.9 procent tegenover 15.6 procent.** Dat is een groot verschil in feitelijke betrouwbaarheid en het sterkste afzonderlijke argument om voor een premiummodel te betalen.

De rij over niet-hallucineren vraagt om voorzichtigheid. Qwens 69.7 procent tegenover Sonnets 51.6 procent lijkt een duidelijke overwinning, en op zichzelf is dat ook zo. De maat beschrijft echter het aandeel *onjuiste* antwoorden waarin geen verzinsels voorkomen. Een model met lagere nauwkeurigheid geeft meer onjuiste antwoorden. De percentages beschrijven dus verschillende groepen en zijn niet rechtstreeks vergelijkbaar. **Lees eerst de rij over nauwkeurigheid.**

Sonnet haalt ook 50.1 procent op SciCode tegenover 46.6 procent. Daarnaast rapporteert het resultaten op twee evaluaties die niet op de kaart van het open model staan: IFBench en Terminal-Bench Hard. Die resultaten zijn niet te vergelijken.

### Twee eerlijke kanttekeningen

**De releasedatums liggen zes maanden uit elkaar.** Sonnet 4.6 verscheen in februari 2026. Qwen3.8 27B verscheen in augustus 2026. Een frontiermodel uit februari vergelijken met een open model uit augustus is geen gelijkwaardige wedstrijd.

**Sonnet 4.6 is niet langer het frontiermodel van Anthropic.** Sonnet 5 en Opus 5 staan inmiddels hoger in het aanbod. Het open 27B-model haalde een vlaggenschip uit midden 2026 in. Het haalde niet de huidige top van de reeks in. Wie meer beweert, leest te veel in de tabel.

*Benchmarks meten prestaties op benchmarks. Alleen de score op jouw werklast telt.*

## Wat ternaire gewichten veranderen

Bonsai 2 is geen kleiner model. Het is hetzelfde model met 26.90B parameters op een veel lagere numerieke precisie. De gepubliceerde GGUF-metadata maakt de afweging duidelijk.

| Eigenschap | Waarde |
|---|---|
| **Architectuur** | `qwen35`, hybride aandacht met volledige aandacht om de vier lagen, plus state-space-lagen |
| **Parameters** | 26.90B |
| **Blokken** | 64 |
| **Embeddingbreedte** | 5120 |
| **Aandacht** | 24 querykoppen, 4 KV-koppen, key/value-lengte 256 |
| **Context** | 262,144 tokens, RoPE-basis 1e7 |
| **Gewichtsformaat** | Ternair, groepsgrootte 128. PQ2_0 met 2.13 bits per gewicht, PTQ1_0 met 1.75 |
| **Vision-toren** | CLIP, 460.73M parameters, geleverd als aparte projectorverpakking |
| **Licentie** | Apache 2.0 |

**Ternaire gewichten betekenen dat elke parameter een van drie waarden heeft in plaats van zestien.** Die compressie is het hele idee. Daardoor past een volledig 27B-model in 5.53 GiB in plaats van 18 GB.

### Gemeten doorvoer

Gemeten met `llama-bench` op een RTX 5090 met 32 GB, alle lagen naar de GPU verplaatst, flash attention ingeschakeld en het gemiddelde van drie runs:

| Verpakking | Gewichten | Prefill (pp512) | Decode (tg128) |
|---|---|---|---|
| **PQ2_0** | 6.70 GiB | **3802.74 tok/s** | **135.41 tok/s** |
| **PTQ1_0** | 5.53 GiB | 1876.31 tok/s | 131.41 tok/s |

PQ2_0 voert de prefill **2.03 keer sneller** uit dan PTQ1_0, terwijl decoderen statistisch gelijk eindigt. Daarom is PQ2_0 de logische standaard. PTQ1_0 is bedoeld voor situaties waarin de laatste 1.2 GiB verschil maakt. Via `llama-server` bleef decoderen met een context van 65K op **136.5 tok/s** bij één streamingaanvraag.

**Decodersnelheid merk je in dagelijks gebruik.** De uitvoersnelheid bedraagt 135 tokens in één seconde en ligt daarmee ruim boven leessnelheid. Latentie is geen reden om lokaal te draaien, want een gehoste API is snel genoeg. Kosten, privacy en controle zijn dat wel.

### De valkuil die niemand noemt

**De standaardversie van Ollama kan deze bestanden niet laden.** De ternaire kernels zitten in de llama.cpp-fork van Prism ML. Getest met Ollama 0.34.2, mislukt het laden met `unsupported tensor "output.weight" size overflows`. De runtime herkent de architectuur `qwen35`, maar bevat nergens in zijn bibliotheken `pq2_0` of `ptq1_0` en heeft geen Hadamard-runtime voor activaties.

Er is nog een valkuil die je beter kent voordat je er een avond aan besteedt. **De F16-verpakking van deze modelfamilie lijkt een veilige terugvaloptie, maar dat is ze niet.** De tensors zijn gewone F16 en F32. Daarom wordt het bestand geparseerd en geladen zonder foutmelding, waarna er onleesbare tekst uitkomt. De gewichten staan in een geroteerde basis die is vastgelegd in de metadata `prism.hadamard.*`. Een runtime moet de bijbehorende rotatie toepassen, anders ontstaat onzin. Met 50.1 GiB past de F16-verpakking bovendien niet volledig op een kaart met 32 GB.

*Lees de modelkaart voordat je downloadt. Een communityspiegel is geen ondersteunde build, en deze pagina zegt dat duidelijk.*

## De MoE-ontwikkeling hierachter

Dichte 27B-modellen zijn maar de helft van het verhaal. Mixture-of-experts-modellen activeren per token slechts een klein deel van hun parameters. Daardoor veranderen de kosten opnieuw.

| Modelfamilie | Totaal / actief | Context | Opmerking |
|---|---|---|---|
| **Qwen3.8 2.4T A95B** | 2.4T / 95B | 1.0M | Open-gewichtbroertje van Qwen3.8 Max |
| **Qwen3.6 35B A3B** | 35B / 3B | 262K | Apache 2.0, hybride sparse MoE |
| **Qwen3 Coder Next** | 80B / 3B | 256K | Open gewichten, ontworpen voor continu actieve codeeragents |

**Qwen3 Coder Next is het model om lokaal in de gaten te houden.** Het heeft in totaal 80B parameters, waarvan er slechts 3B per token actief zijn. Het is gericht op continu actieve agents in CLI- en IDE-omgevingen. Een model dat 3B parameters activeert, genereert op de snelheid van een 3B-model en put tegelijk uit de opgeslagen mogelijkheden van 80B. De notities van de ontwikkelaar noemen prestaties die vergelijkbaar zijn met modellen die tien tot twintig keer zoveel actieve rekenkracht gebruiken.

*Het dichte 27B-model is nu de veilige keuze. Bij sparse modellen buigt de efficiëntiecurve nog verder.*

{{< figure src="local-ai-moe-dense-tradeoff.webp" alt="Grafiek vergelijkt een dicht 27B-model dat alle parameters per token activeert met een sparse mixture-of-experts-model dat slechts 3 miljard van de 80 miljard parameters activeert" >}}

## Het hardwarevenster sluit

Dit deel van het verhaal heeft een deadline.

Lokale inferentie werd goedkoop precies toen het geheugen dat ervoor nodig is duurder werd. Die trends botsen en de gevolgen zijn al zichtbaar in winkelprijzen.

### Wat er met geheugenprijzen gebeurde

**De contractprijzen voor conventionele DRAM stegen in het eerste kwartaal van 2026 kwartaal op kwartaal met 90 tot 95 procent.** Dat is de grootste kwartaalstijging die TrendForce heeft geregistreerd. NAND-flash steeg in hetzelfde tijdvak met 55 tot 60 procent.

De druk nam niet af. Volgens TrendForce steeg DRAM in het tweede kwartaal nog eens **58 tot 63 procent** en NAND 70 tot 75 procent. Zelfs de gematigdere stijging in het derde kwartaal, 13 tot 18 procent voor DRAM en 10 tot 15 procent voor NAND, komt boven op twee recordkwartalen. Het is geen verlichting.

De oorzaak is structureel, niet cyclisch. AI-datacenters nemen geheugencapaciteit in die eerder voor telefoons, laptops en spelcomputers werd gebruikt. Geheugenmakers geven de best betalende orders voorrang. Analisten die de moduletoevoer volgen, verwachten dat het DRAM-aanbod aan modulemakers in 2027 met meer dan 70 procent daalt.

**De topman van Intel noemde een getal.** Tijdens de AI Infrastructure Summit in Santa Clara op 15 september 2026 zei Lip-Bu Tan dat geheugenprijzen al "vijf, zes en zeven keer" hoger waren dan voorheen. Hij waarschuwde dat geheugen nu 70 tot 80 procent van de materiaalkosten van een goedkope laptop vormt. Elders zei hij dat er tot 2028 geen verlichting komt.

*Onafhankelijke berichtgeving over de prijs per oppervlak van DRAM-wafers tegenover wafers met geavanceerde logica bevat een belangrijke kanttekening. Spotprijzen zijn geen contractprijzen. De DDR5-spotmarkt is dun genoeg om de vergelijking suggestief maar niet definitief te maken. De richting is duidelijk.*

{{< figure src="local-ai-memory-price-trend-2026.webp" alt="Grafiek van kwartaalstijgingen in DRAM-contractprijzen door 2026: 90 tot 95 procent in het eerste kwartaal, aflopend tot 13 tot 18 procent in het derde kwartaal" >}}

### Wat dit met videokaarten deed

Geheugen vormt een groot deel van de materiaalkosten van een grafische kaart. DRAM-prijzen werken dus rechtstreeks door in GPU-prijzen.

| Kaart | Begin 2025 | September 2026 |
|---|---|---|
| **Nvidia RTX 5090** | $1,999 | **meer dan $5,000** |
| **Asus RTX 5080** | $1,199 | $1,595 |
| **AMD RX 9070 XT** | ongeveer $830 | **meer dan $1,037** |

Die stijgingen kwamen in gecoördineerde golven door 2026, niet als losse uitschieters. Nvidia verhoogde prijzen in januari, opnieuw in mei voor de RTX 5090 en later dat jaar nog een keer. AMD volgde in augustus met minstens 10 procent prijsstijging op bepaalde Radeon-kaarten en GDDR6-geheugenkits. Het bedrijf wees rechtstreeks naar de geheugenkosten.

**De volgende generatie werd uitgesteld in plaats van uitgebracht.** De RTX 60-serie van Nvidia wordt nu in 2028 verwacht en slaat 2027 volledig over. Als oorzaak wordt de geheugenschaarste genoemd.

*De kaart die je nu koopt concurreert niet met een goedkopere kaart volgend jaar. Hij concurreert met een duurdere versie van zichzelf.*

## Waarom wachten duurder is

Het gebruikelijke hardwareadvies luidt: wacht op de volgende generatie. In een markt waar geheugen schaars is, werkt dat advies tegen je.

Drie punten maken dit duidelijk.

**Prijzen zijn al gestegen en blijven stijgen.** Een kwartaalstijging van 90 tot 95 procent voor DRAM-contracten is geen uitschieter die na één kwartaal verdwijnt. TrendForce verwacht voor het derde kwartaal verdere stijgingen, geen daling. De topman van Intel noemt 2028 als moment waarop verlichting komt.

**Er komt geen productgeneratie in 2027 om op te wachten.** Als de volgende consumentengpu's pas in 2028 verschijnen, duurt de wachttijd twee jaar. Een groot deel van een hardwarevernieuwingscyclus gaat dan op aan wachten.

**De modellen zijn nu al goed genoeg.** Dat veranderde in 2026. Twee jaar geleden leverde lokale hardware zichtbaar slechtere ervaringen op. Vandaag koop je voor hetzelfde geld een 27B-model dat elke seconde 135 tokens genereert met een contextvenster van 262K en een premium-API-model verslaat op de samengestelde intelligentie-index.

*Wachtte je tot lokale modellen goed genoeg werden? Dan is het wachten voorbij. Wacht je tot hardware goedkoper wordt? Volgens de leveringsgegevens wacht je tot 2028.*

## Wat je moet bouwen

De hardware aan de bovenstaande modellen koppelen is eenvoudig, omdat ternaire gewichten de geheugenbehoefte verlaagden.

| Niveau | Geheugen | Wat soepel draait |
|---|---|---|
| **Instap** | 8 tot 12 GB VRAM | Ternair 27B-model van 5.53 tot 6.70 GiB, met ruimte voor context |
| **Praktisch** | 16 tot 24 GB VRAM | Volledig Qwen3.8 27B-model van 18 GB, of de ternaire verpakking met lange context |
| **Comfortabel** | 32 GB VRAM | Ternair 27B-model met volledige context van 262K, of een 80B-MoE met 3B actieve parameters |
| **Gedeeld geheugen** | 64 tot 128 GB | Grotere sparse MoE-modellen op Apple Silicon of een desktop met gedeeld geheugen |

Enkele praktische aandachtspunten wegen zwaarder dan de niveautabel:

- **Koop geheugen, niet de vlaggenschipkaart.** Dankzij de ternaire verpakking van 5.53 GiB is het instapniveau echt bruikbaar. Besteed het verschil liever aan systeem-RAM en opslag dan aan een topkaart tegen prijzen van 2026.
- **Systemen met gedeeld geheugen bieden veel waar voor je geld.** Een machine met minstens 64 GB gedeeld geheugen draait grotere sparse modellen voor een fractie van de kosten van een losse kaart met dezelfde capaciteit.
- **Stroom en koeling tellen mee.** Een systeem dat urenlang inferentie draait gedraagt zich anders dan een systeem dat enkele minuten benchmarks uitvoert.
- **Draai de ternaire verpakking naast een kleiner model.** Een model met 3B parameters beantwoordt snelle vragen, terwijl het 27B-model de moeilijke vragen afhandelt.

{{< centerbutton href="https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B" >}}
Download Ternary Bonsai 2 27B
{{< /centerbutton >}}

## Waar premiummodellen hun prijs nog waard zijn

Er is een echte reden voor het premiumniveau. Die is kleiner dan marketing doet vermoeden.

**Betrouwbaarheid van feiten is het eerlijke antwoord.** De AA-Omniscience-nauwkeurigheid is 40.9 procent voor Sonnet 4.6 en 15.6 procent voor het open 27B-model. Als een fout antwoord een klant, diagnose of juridisch standpunt schaadt, weegt een verschil van 25 procentpunten zwaarder dan elke samengestelde index.

**Lange agentische ketens zijn de tweede reden.** Sonnet 4.6 haalt 53.0 procent op Terminal-Bench Hard en 75.7 procent op τ²-Bench Telecom. Die evaluaties meten langdurig toolgebruik en gedrag van agents over meerdere beurten. De kaart van het open model bevat geen vergelijkbare resultaten. Dat ontbreken is geen goed teken.

**De derde reden is beheer.** Een gehoste API brengt geen driverupdates, kwantiseringseigenaardigheden, een llama.cpp-fork die je moet volgen of een geroteerde gewichtsruimte die je goed moet instellen. Iemand anders beheert de uptime en iemand anders wordt om drie uur 's nachts opgeroepen.

### De vraag die ertoe doet

Waar staat het premiumniveau buiten het bedrijfsleven?

**Voor werk waarbij kennis cruciaal is, blijft het relevant.** Denk aan onderzoek, juridische analyse, medische vragen, financiële modellen en alles waarbij een zelfverzekerd maar fout antwoord duur is. Dit is een echte categorie en het nauwkeurigheidsverschil is een echte reden om te betalen.

**Voor generatief werk wordt de reden snel zwakker.** Teksten opstellen, samenvatten, code herstructureren, gegevens herformatteren, documenten classificeren en geautomatiseerde pijplijnen uitvoeren zijn taken waarbij je de uitvoer controleert voordat je erop vertrouwt. Het verschil in nauwkeurigheid kost weinig als een mens of testsuite het resultaat eerst controleert. Dan is het moeilijk te verdedigen om per token te betalen voor een index van 30.1, terwijl een index van 33.7 gratis draait op hardware die je al bezit.

**De keuze gaat nu over gevolgen, niet over mogelijkheden.** Twee jaar geleden was de vraag of een lokaal model het werk überhaupt goed genoeg kon uitvoeren. Nu gaat het om de kosten van een fout en hoe je die ontdekt.

*De zakelijke meerprijs koopt betrouwbaarheid, compliance en de storingsdienst van iemand anders. Anderen betalen voor een verschil dat niet meer telt zodra een testsuite het resultaat controleert.*

## Belangrijkste punten

- **Een lokaal 27B-model verslaat Claude Sonnet 4.6 nu op de samengestelde intelligentie-index**, 33.7 tegenover 30.1. Het leidt ook bij coderen, agentische taken, lange context en wetenschappelijk redeneren op masterniveau.
- **Sonnet 4.6 wint nog op feitelijke nauwkeurigheid**, 40.9 tegenover 15.6 procent op AA-Omniscience. Dat is het sterkste resterende argument voor het premiumniveau.
- **Ternaire kwantisering maakt dit praktisch.** Bonsai 2 27B draait hetzelfde model van 26.90B parameters in 5.53 GiB in plaats van 18 GB. Beide gebruiken Apache 2.0.
- **Standaard-Ollama kan de ternaire verpakkingen niet uitvoeren.** Daarvoor heb je de llama.cpp-fork van Prism ML nodig. De F16-terugvaloptie produceert ongemerkt onsamenhangende uitvoer in plaats van een foutmelding.
- **De gemeten decodersnelheid bedraagt 135 tokens in één seconde** op een RTX 5090. Dat ligt ruim boven leessnelheid.
- **Geheugenprijzen zijn de reden om nu te handelen.** DRAM-contractprijzen stegen in 2026 in één kwartaal met 90 tot 95 procent en de volgende generatie consumentengpu's is uitgesteld tot 2028.
- **De RTX 5090 steeg in minder dan twee jaar van $1,999 naar meer dan $5,000**, en elk niveau werd duurder.

## Volgende stappen

1. **Download het model en test het met je eigen werklast**: **[Ternaire Bonsai 2 27B op Ollama](https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B)**
2. **Haal de oorspronkelijke gewichten op volledige precisie op** als je genoeg geheugen hebt: **[Qwen3.8 op Ollama](https://ollama.com/library/qwen3.8)**
3. **Test het model voordat je iets bouwt** met het gratis gehoste eindpunt: **[Qwen3.8 27B gratis op OpenRouter](https://openrouter.ai/qwen/qwen3.8-27b:free)**
4. **Vergelijk met het betaalde niveau met dezelfde prompts**: **[Claude Sonnet 4.6 op OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-4.6)**
5. **Bepaal de omvang van je systeem op basis van de geheugentabel** en koop het geheugen vóór de grafische kaart.
6. **Heb je een ongebruikte Raspberry Pi?** Kijk of die een kleiner model kan draaien: **[Welke AI-modellen kunnen draaien op een Raspberry Pi 4 of 5?](/articles/ai-models-raspberry-pi-4-5/)**

## Verwante artikelen

| Artikel | Wat het behandelt |
|---|---|
| **[Welke AI-modellen kunnen draaien op een Raspberry Pi 4 of 5?](/articles/ai-models-raspberry-pi-4-5/)** | De ondergrens van lokale inferentie en wat kleine borden echt aankunnen |
| **[Een privacyvriendelijke AI-assistent voor Meshtastic bouwen](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | Een lokale assistent op off-grid hardware, waar privacy noodzakelijk is |
| **[De rol van ECC-geheugen bij het beperken van gegevenscorruptie](/articles/the-role-of-ecc-memory-in-mitigating-data-corruption/)** | Waarom geheugenkwaliteit belangrijker wordt wanneer er een groot model in draait |
| **[Wat is een homelab en heb je er een nodig?](/articles/what-is-a-homelab-and-should-you-have-one/)** | Huisvesting, stroom en koeling plannen voor hardware die heet wordt |

## Bronnen

1. [Ternaire Bonsai 2 27B - Ollama-modelspiegel](https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B)
2. [Qwen3.8 - Ollama-modellenbibliotheek](https://ollama.com/library/qwen3.8)
3. [Qwen3.8 27B (gratis) - OpenRouter-benchmarks en prijzen](https://openrouter.ai/qwen/qwen3.8-27b:free)
4. [Claude Sonnet 4.6 - OpenRouter-benchmarks en prijzen](https://openrouter.ai/anthropic/claude-sonnet-4.6)
5. [Bonsai 2 27B eerste test - is DIT het beste AI-model voor één GPU? - Bijan Bowen](https://www.youtube.com/watch?v=OA5cICIzD-c)
6. [Artificial Analysis - onafhankelijke modelevaluaties](https://artificialanalysis.ai/)
7. [TrendForce - voorspellingen voor DRAM- en NAND-contractprijzen](https://www.trendforce.com/)
8. [Geheugenchips zijn nu per oppervlak duurder dan computerchips - Tom's Hardware](https://www.tomshardware.com/pc-components/dram/dram-is-now-more-expensive-than-compute-chips-on-per-area-basis-ai-demand-drives-memory-die-value-past-leading-edge-silicon)
9. [GPU-prijsdaling verschuift naar 2028 na een DRAM-recordstijging van 95% - Tech Insider](https://tech-insider.org/gpu-relief-pushed-2028-dram-price-jump-2026/)
10. [Intel-topman Tan: geheugen zevenmaal zo duur, geen verlichting tot 2028 - shattered.io](https://shattered.io/intel-ceo-memory-shortage-no-relief-until-2028-2026/)
11. [Prism ML llama.cpp-fork - ternaire kernels](https://github.com/PrismML-Eng/llama.cpp)
12. [Ternary-Bonsai-2-27B-gguf - oorspronkelijke gewichten](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)
