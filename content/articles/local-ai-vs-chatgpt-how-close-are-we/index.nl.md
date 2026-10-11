---
title: "Lokale AI versus ChatGPT: hoe dichtbij zijn we echt?"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Vergelijk lokale AI met ChatGPT en Claude aan de hand van benchmarkscores, geheugenschattingen, servicesnelheid en agentverificatie. Met scenario's voor RTX 5090, DGX Spark en Mac Studio."
genre: ["Lokale AI", "Kunstmatige intelligentie", "AI-hardware", "Ontwikkelaarstools"]
tags: ["lokale AI versus ChatGPT", "lokale AI versus Claude", "lokale LLM", "AI-agents", "open gewichten", "Qwen3.8 27B", "GLM-5.3", "GPT-6 Astra", "Claude Opus 5.5", "RTX 5090", "DGX Spark", "Mac Studio", "kwantisatie", "KV-cache", "unified memory", "VRAM", "Artificial Analysis", "agentverificatie", "lokale inferentie", "hybride AI", "codeeragents", "AI-benchmarks"]
cover: "/img/cover/local-ai-vs-chatgpt-comparison-illustration.webp"
coverAlt: "Een desktopwerkstation verbonden via een lichtgevend pad met een abstracte wolk van netwerkpunten op een donkere achtergrond"
coverCaption: "Conceptuele illustratie van lokale en gehoste AI."
---

**Lokale AI** is praktisch voor afgebakend werk met duidelijke controles. Om werk van ChatGPT of Claude te vervangen, moeten modelcapaciteit, bruikbaar geheugen en een agent die de uitvoer inspecteert en controleert samen passen.

Een model dat op je werkstation past heeft geschikte hulpmiddelen en genoeg snelheid nodig voor herhaalde pogingen. Dit artikel scheidt benchmarkresultaten, geheugenschattingen en bewijs van voltooide taken, zodat je elk onderdeel afzonderlijk beoordeelt.

<!--more-->

## Belangrijkste punten

- **Capaciteit:** referentiescores beschrijven specifieke evaluatie-instellingen, niet jouw lokale gekwantiseerde build.
- **Geheugen:** plan gewichten, contextcache en runtime-overhead samen.
- **Snelheid:** het opnieuw afspelen van een agentgesprek meet serverprestaties, niet correctheid.
- **Verificatie:** een agent heeft controles nodig die bij het gevraagde resultaat passen.
- **Keuze:** vergelijk herhaalde taken, hersteltijd en totale kosten voordat je hardware koopt.

## Scores in context lezen

De **Artificial Analysis Intelligence Index** combineert meerdere evaluaties tot een referentiescore. De [modellenranglijst](https://artificialanalysis.ai/leaderboards/models) en lokale hardware-resultaten tonen de volgende items, gecontroleerd op 6 oktober 2026.

| Model en instelling | Indexscore | Implementatie in deze vergelijking |
|---|---|---|
| **Qwen3.8 27B, xhigh** | 34 | Downloadbare gewichten |
| **GLM-5.3, max** | 45 | Downloadbare gewichten |
| **GPT-6 Astra, max** | 53 | Gehoste dienst |
| **Claude Opus 5.5, max met fallback** | 58 | Gehoste dienst |

**Indexpunten** zijn geen percentages voor intelligentie of taaksucces. Een verschil van 13 punten tussen GLM en Claude bewijst geen verschil van 13% in je programmeerresultaten. Redeneerinstellingen tellen mee wanneer je hetzelfde model vergelijkt.

De [gepubliceerde evaluatiemethode](https://artificialanalysis.ai/methodology/intelligence-benchmarking) beschrijft de testopstelling. Sommige evaluaties gebruiken hulpmiddelen en agentinfrastructuur. Zie de score als resultaat binnen die voorwaarden. Pas hem niet rechtstreeks toe op een gecomprimeerde lokale kopie in een andere applicatie.

**ChatGPT en Claude zijn producten**, terwijl deze tabel geselecteerde onderliggende modellen vergelijkt. Abonnement, gekozen model, beschikbare hulpmiddelen en taakcontext voegen verschillen toe. Begin met een herhaalde taak en test de volledige opstelling.

## De volledige aanvraag begroten

**Geheugenpassing** begint met drie toewijzingen. Modelgewichten bewaren geleerde parameters. De key-value-cache, of **KV-cache**, houdt aandachtsgegevens tijdens inferentie bij. Runtimebuffers en andere software gebruiken de resterende ruimte.

```text
Required memory = resident weights + context cache + runtime allowance
Available memory = physical capacity - operating system and application reserve
```

**Kwantisatie** verlaagt de opslagprecisie van modelgewichten. Lagere precisie verlaagt het geheugengebruik, terwijl kwaliteit afhangt van model en gekwantiseerde build. Cacheprecisie is een aparte instelling. Een Q4-gewichtbestand bewijst geen vierbitscache.

Als ruwe gewichteninschatting vragen 27 miljard parameters op 16 bits ongeveer 50,3 GiB. Acht bits vraagt ongeveer 25,1 GiB en vier bits ongeveer 12,6 GiB. **Gepubliceerde bestandsgroottes** bevatten ook metadata, packing en gemengde precisie. Gebruik de exacte bestanden voor implementatieplanning.

De [Qwen3.8-27B-modelkaart](https://huggingface.co/Qwen/Qwen3.8-27B) en [GLM-5.3-modelkaart](https://huggingface.co/zai-org/GLM-5.3) beschrijven verschillende architecturen. Een **mixture-of-experts-model** activeert per token slechts een deel van de parameters, maar de overige gewichten moeten nog steeds worden opgeslagen. Offloading wijzigt plaats en latentie, niet het bestaan van de gewichten.

## Beginnen met gepubliceerde bestanden

**Downloadgrootte** is een concreter beginpunt dan parameteraantal. De gepubliceerde Qwen- en GLM-builds van Unsloth tonen hoe sterk opslag verandert met de gekozen kwantisatie.

| Gekwantiseerde build | Gepubliceerde grootte, decimale GB | Geschatte GiB |
|---|---|---|
| **Qwen3.8 27B Q4_0** | 16.1 | 15.0 |
| **Qwen3.8 27B Q8_0** | 29.0 | 27.0 |
| **GLM-5.3 UD-Q4_K_XL** | 467 | 434.9 |
| **GLM-5.3 UD-IQ2_M** | 239 | 222.6 |

**Bestandsbronnen:** [Qwen Q4_0](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/blob/main/Qwen3.8-27B-Q4_0.gguf), [Qwen Q8_0](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/blob/main/Qwen3.8-27B-Q8_0.gguf), [GLM UD-Q4_K_XL-shards](https://huggingface.co/unsloth/GLM-5.3-GGUF/tree/main/UD-Q4_K_XL) en [GLM UD-IQ2_M-shards](https://huggingface.co/unsloth/GLM-5.3-GGUF/tree/main/UD-IQ2_M). Afgeronde waarden, gecontroleerd op 6 oktober 2026. GiB-conversies delen decimale bytes door 2³⁰.

**Dit zijn gewichtsbestandsgroottes**, geen totale metingen van resident geheugen. Laden, caches, tijdelijke buffers en extra modelonderdelen beïnvloeden het actieve proces. Vergelijk een download van 29 GB niet direct met een toewijzing van 30 GiB zonder de eenheden om te rekenen.

## Context verandert de passing

De **aandachtscache van Qwen** geeft een uitgewerkt voorbeeld. De [gepubliceerde configuratie](https://huggingface.co/Qwen/Qwen3.8-27B/blob/main/config.json) noemt 64 lagen, volledige aandacht om de vier lagen, vier key-value-heads en een headdimensie van 256.

```text
Full-attention KV bytes per token:
16 layers × 4 KV heads × 256 dimensions × 2 (K and V) × 2 bytes
= 65,536 bytes

8,192 tokens  = 0.5 GiB
32,768 tokens = 2.0 GiB
```

Dit **berekende cacheonderdeel** gaat uit van 16-bits sleutels en waarden voor één reeks. Lineaire-aandachtsstatus, runtimebuffers, allocator-overhead en optionele visie- of speculatieve decodeeronderdelen ontbreken. Voor die toewijzingen blijft reserve nodig.

Voor een **illustratief planningsbudget** tel je 3–5 GiB op bij de afgeronde gewichtsformaten. Deze marge is een aanname die je vervangt door metingen van je runtime.

| Build en context | Berekende planningsreeks |
|---|---|
| **Qwen Q4_0, 8K** | 18.5–20.5 GiB |
| **Qwen Q8_0, 8K** | 30.5–32.5 GiB |
| **Qwen Q8_0, 32K** | 32.0–34.0 GiB |

Een **bruikbare toewijzing van 30 GiB** laat ruimte voor het Q4-voorbeeld, terwijl de Q8-scenario's deze onder deze aannames overschrijden. Een kleinere gemeten reserve verandert de grens. Een korte geslaagde prompt bewijst dus geen capaciteit voor een lange codesessie.

**Gelijktijdige aanvragen** voegen een dimensie toe. Ollama documenteert groei van contextgeheugen met parallelle aanvragen en aparte instellingen voor cacheprecisie. De Q8-cache gebruikt ongeveer de helft van de F16-cache, Q4 ongeveer een kwart, met modelafhankelijke kwaliteitskeuzes. Zie de [Ollama-runtime-FAQ](https://docs.ollama.com/faq).

## Hardware aan de toewijzing koppelen

Een **RTX 5090** heeft 32 GB toegewijd grafisch geheugen. Een DGX Spark met 128 GB gebruikt gedeeld geheugen. Artificial Analysis documenteert beide configuraties in de hardware-resultaten. Meer capaciteit maakt grotere toewijzingen mogelijk, maar bewijst geen servicesnelheid.

| Hardwarescenario | Praktische betekenis |
|---|---|
| **RTX 5090, 32 GB** | Qwen Q4 laat meer contextreserve dan Q8 |
| **DGX Spark, 128 GB** | Ruimte voor beide Qwen-builds, met benodigde runtime-overhead |
| **Mac Studio, 256 GB** | Grotere gewichtensets zijn kandidaten, afhankelijk van runtime en toewijzingslimieten |

**GLM UD-Q4_K_XL** overschrijdt alle drie capaciteiten vóór een cache wordt toegevoegd. De IQ2-gewichtenset van ongeveer 222,6 GiB overschrijdt ook een systeem van 128 GB. Op een Mac van 256 GB hangt haalbaarheid af van de werkelijk voor de GPU beschikbare toewijzing en resterende overhead. [Apple-specificaties](https://www.apple.com/mac-studio/specs/) beschrijven hardwareopties, geen gegarandeerde inferentietoewijzing.

Een **hypothetisch bruikbaar budget van 240 GiB** laat na deze IQ2-gewichten ongeveer 17,4 GiB over. Een budget van 192 GiB faalt met alleen de gewichten. Geen van beide bewijst een standaardwaarde van het besturingssysteem, ondersteuning voor gecomprimeerde cache, bruikbare doorvoer of aanvaardbare IQ2-kwaliteit. Eis een aangetoonde runtimeconfiguratie voordat je hardware voor deze werklast koopt.

## Snelheid is een apart resultaat

De **lokale-inferentiebenchmark van Artificial Analysis** speelt een opgenomen werklast van 168 modelbeurten opnieuw af. De [laptop- en workstationresultaten](https://artificialanalysis.ai/hardware-inference-stack/laptops-workstations/) geven deze tijden voor geteste Qwen3.8 27B-configuraties.

| Systeem | Hersteltijd van service-replay |
|---|---|
| **DGX Spark, 128 GB** | 24.2 minuten |
| **RTX 5090** | 4.9 minuten |
| **Mac Studio, 256 GB** | Geen resultaat in deze vergelijking |

Het RTX-resultaat duurt ongeveer een vijfde van de Spark-tijd. **Serviceconfiguraties tellen mee**, dus dit is geen universele hardwareverhouding. De geteste service-builds verschillen ook van de GGUF-planningsvoorbeelden hierboven.

**Replaytijd** sluit tooluitvoering uit en dwingt opgenomen antwoordlengtes af. De tijd beoordeelt niet of antwoorden de oorspronkelijke taak oplossen. Een MacBook-meting bewijst ook geen Mac Studio-prestaties.

## De agent feedback geven

Een **agent-uitvoersysteem** levert hulpmiddelen, context, een actielus en verificatie. Een model schrijft of kiest acties binnen dit systeem. Voor een CSV-export zijn projectbestanden lezen, code wijzigen, tests uitvoeren en resulterende fouten ontvangen nuttige mogelijkheden.

Neem een **illustratieve exporttaak**, geen gemeten experiment. De agent schrijft een downloadfunctie, maar gebruikt de verkeerde datumnotatie. Visuele controle ziet het probleem niet. Een test opent het geëxporteerde bestand en vergelijkt datums met de vereiste notatie. De agent ontvangt de fout, wijzigt de formatter en voert de controle opnieuw uit.

| Ontbrekend onderdeel | Waarschijnlijke fout |
|---|---|
| **Relevante context** | Bewerkt een ongerelateerd bestand |
| **Uitvoertools** | Beschrijft een oplossing zonder die toe te passen |
| **Verificatiestap** | Stopt na plausibele code |
| **Foutfeedback** | Herhaalt een mislukte aanpak |

**LangChain meldt** een verandering van 52,8% naar 66,5% op Terminal Bench 2.0 met GPT-5.2-Codex constant. Het [rapport over agentengineering](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering) beschrijft verificatieadvies, omgevingscontext, detectie van herhaalde edits en wijzigingen in redeneerbudget.

## Controles aan het werk koppelen

Een **geslaagde controle** bewijst alleen wat de controle afdekt. Een CSV-test die kolomnamen valideert laat datumnotatie, aanhalingstekens, Unicode en toegangsbeheer ongetest. Definieer het gewenste resultaat voordat je verificatie kiest.

| Taak | Nuttig bewijs van voltooiing |
|---|---|
| **Codewijziging** | Relevante tests plus inspectie van het resulterende gedrag |
| **Onderzoeksantwoord** | Opgehaalde bronnen die afzonderlijke claims ondersteunen |
| **Boeking of terugbetaling** | Correct opgeslagen resultaat en naleving van toepasselijk beleid |
| **Documentexport** | Geparseerde uitvoer die gevraagde velden en formaten volgt |

De **τ-bench-studie** beoordeelt agents die met hulpmiddelen, gebruikers en domeinregels werken. Het [onderzoeksartikel](https://arxiv.org/abs/2406.12045) controleert de uiteindelijke databasestatus tegen verwachte resultaten. Dit laat zien waarom vloeiende bevestigingstekst geen voldoende transactiecontrole is.

## Lokaal betekent niet offline

**Lokale inferentie** bepaalt waar het model draait. De omliggende applicatie bepaalt nog steeds waar documenten, zoekopdrachten, traces en toolresultaten heen gaan. Een lokaal codemodel dat met externe zoekfuncties of cloudtools werkt, blijft een netwerksysteem.

Ollama zegt dat het voor lokale uitvoering geen prompts of antwoorden ontvangt en documenteert hoe cloudfuncties worden uitgeschakeld. Dit is een **runtime-specifieke verklaring**, geen privacygarantie voor elke verbonden agent. Controleer modelendpoint en elke integratie in de [runtime-documentatie](https://docs.ollama.com/faq).

| Datapad | Wat je controleert |
|---|---|
| **Inferentie-endpoint** | Lokaal proces, externe server of automatische fallback |
| **Zoeken en ophalen** | Extern verzonden zoekopdrachten en documentfragmenten |
| **Toolverbindingen** | Bestanden en records die aan elke dienst worden blootgesteld |
| **Logboeken en traces** | Opslaglocatie, bewaarde inhoud en toegang |

Een **hybride workflow** heeft een expliciete overdrachtsregel nodig. Houd privé-documentextractie bijvoorbeeld lokaal en stuur alleen goedgekeurde samengevoegde resultaten naar gehoste analyse. Controleer exact wat naar buiten gaat. Een samenvatting bevat gevoelige informatie als namen, klantgegevens of vertrouwelijke bevindingen behouden blijven.

## Testen vóór aankoop

**Kies een herhaalde taak** met een duidelijke eindvoorwaarde. Vergelijk lokale configuratie met het gehoste product dat je gebruikt, inclusief de hulpmiddelen. Geef beide dezelfde invoer en acceptatiecriteria en herhaal de taak met representatieve voorbeelden.

1. **Leg de configuratie vast:** exact modelbestand, kwantisatie, backendversie, contextlimiet en redeneerinstelling.
2. **Definieer succes:** verwacht artefact, vereist gedrag en verboden neveneffecten.
3. **Meet voltooiing:** verstreken tijd, geslaagde controles, mislukte pogingen en handmatige reparaties.
4. **Neem eigendomskosten mee:** hardware, elektriciteit, API-kosten, onderhoud en je tijd.
5. **Classificeer fouten:** redeneerfouten, geheugenlimieten, latentie, ontbrekende context of verificatie.

**Lokale inferentie** past bij werk waarvan geteste kwaliteit en latentie aan je eisen voldoen. Een gehost model blijft nuttig wanneer extra capaciteit fouten of reviewwerk vermindert. Een hybride workflow wijst verschillende taken toe nadat is bepaald welke gegevens de machine mogen verlaten.

## Kosten per geaccepteerd resultaat tellen

**Menselijke hersteltijd** verandert vaak de economie. Een snel lokaal antwoord dat tien minuten correctie vraagt kost meer werktijd dan een trager antwoord dat de review passeert. Tel geaccepteerde resultaten naast inferentie-uitgaven.

```text
Cost per accepted task =
(hardware allocation + electricity + service fees + maintenance + review time)
÷ accepted tasks
```

**Illustratieve reviewkosten:** bij een verondersteld tarief van $30 per uur kosten acht correctieminuten $4 per taak. Honderd zulke taken gebruiken $400 aan reviewtijd. Dit zijn rekenvoorbeelden, geen gemeten faalpercentages van lokale modellen.

**Vergelijk gelijkwaardige uitkomsten.** Neem afgewezen pogingen op in tijd en kosten. Verdeel bij eigen hardware de aankoopprijs over een realistische gebruiksperiode en taakhoeveelheid. Neem bij een gehoste dienst abonnement of API-kosten en resterend reviewwerk mee.

Voor hardwaredetails lees je de [gids voor lokale modellen, GPU's en context](/articles/local-ai-model-gpu-context-guide/). Voor capaciteit en prijs lees je de [DGX Spark-geheugenvergelijking](/articles/dgx-spark-64gb-memory-crisis-2027/). Gebruik je taakresultaten om de kleinste opstelling te kiezen die aan je eisen voor kwaliteit, snelheid en gegevens voldoet.

## Referentievideo

{{< youtube id="siZ3f_06k8M" enable="true" title="Local AI vs ChatGPT: How Close Are We Really?" description="Local and hosted AI models, memory requirements, serving performance, and agent verification." >}}

## Referenties

- **AI Mechanics:** [Local AI vs ChatGPT: How Close Are We Really?](https://www.youtube.com/watch?v=siZ3f_06k8M).
- **Artificial Analysis:** [modelresultaten](https://artificialanalysis.ai/leaderboards/models), [evaluatiemethode](https://artificialanalysis.ai/methodology/intelligence-benchmarking) en [lokale-inferentieresultaten](https://artificialanalysis.ai/hardware-inference-stack/laptops-workstations/).
- **Modeluitgevers:** [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) en [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3).
- **Unsloth:** [Qwen GGUF-builds](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/tree/main) en [GLM GGUF-builds](https://huggingface.co/unsloth/GLM-5.3-GGUF/tree/main).
- **Ollama:** [runtime-, geheugen- en privacydocumentatie](https://docs.ollama.com/faq).
- **LangChain:** [agentengineeringresultaten](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering).
- **τ-bench:** [onderzoek naar tool-agent-gebruiker-evaluatie](https://arxiv.org/abs/2406.12045).
