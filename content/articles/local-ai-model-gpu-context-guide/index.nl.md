---
title: "Welk lokaal AI-model moet je draaien? Een GPU-, context- en programmeergids voor oktober 2026"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Een praktische gids voor oktober 2026 voor het kiezen van lokale AI-modellen voor programmeeragents. Vergelijk GPU-geheugen, groei van de KV-cache, contextgrootte, quantisatiekwaliteit, promptverwerking, redeneerniveaus en cloudhuurkosten."
genre: ["Lokale AI", "AI-hardware", "Zelfgehoste AI", "GPU-benchmarking", "Ontwikkelaarstools", "AI-economie"]
tags: ["lokale AI-modellen", "programmeeragents", "GPU-gids", "VRAM", "KV-cache", "contextvenster", "Qwen 27B", "mixture of experts", "quantisatie", "llama.cpp", "Ollama", "speculatieve decodering", "multi-tokenvoorspelling", "lokale LLM", "GPU-huur", "AI-werkstation", "agentprogrammering", "promptverwerking", "inferentiesnelheid"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Een werkstation met lokale AI-modellen, GPU-geheugengebruik en contextvensters van programmeeragents"
coverCaption: ""
ref: ["/articles/32gb-vram-qwen-27b-hardware-guide", "/articles/qwen38-27b-vast-ai-gpu-benchmark", "/articles/local-ai-2026-build-your-rig-now"]
---

**Het beste lokale programmeermodel is het model dat genoeg van je project in het geheugen houdt en het snel genoeg leest om bruikbaar te blijven.** De modelgrootte telt nog steeds. Een model dat pas past nadat gegevens naar systeem-RAM zijn verplaatst, voelt vaak slechter dan een kleiner model met een stabiel contextvenster.

*Kies het model en het geheugenbudget samen. Kies geen model uit een tierlijst om het daarna op ongeschikte hardware te forceren.*

Deze gids gaat over programmeeragents, niet over korte autocomplete-prompts. Een agent leest bestanden, tooluitvoer, compilerfouten en testresultaten voordat hij een oplossing schrijft. Die invoer gebruikt context en verandert de hardwarekeuze.

## De video is een referentie

De volgende video vergelijkt lokale modellen over verschillende GPU-geheugenniveaus. De video is nuttig voor praktische observaties over modelkeuze en gerapporteerde hardwareresultaten. Dit artikel kiest een eigen aanpak en ordent de beslissing rond geheugengedrag, agentcontext, promptverwerking en totale eigendomskosten.

{{< youtube id="C9M6iUFtVB4" enable="true" title="Ik heb elk lokaal AI-model getest zodat jij dat niet hoeft te doen" description="Een praktische vergelijking van lokale AI-modellen over meerdere GPU-geheugenniveaus, met aandacht voor programmeerworkloads en hardwarelimieten." >}}

## Waarom tierlijsten falen

Een modeltierlijst koppelt meestal het aantal parameters aan een hoeveelheid GPU-geheugen. Die verkorte aanpak helpt bij een eerste schatting. Zodra een programmeeragent een echte repository leest, voldoet hij niet meer.

De modelgewichten vormen de eerste allocatie. De **KV-cache** is de groeiende allocatie. Die bewaart attention keys en values van de actieve context, zodat de runtime niet na elk gegenereerd token de hele prompt opnieuw hoeft te berekenen.

| Geheugenverbruiker | Wat hij bevat | Waarom het telt |
|---|---|---|
| **Modelgewichten** | De gequantiseerde parameters | Eenmalige laadvereiste |
| **KV-cache** | Informatie uit de actieve context | Groeit met prompt en gesprek |
| **Runtimebuffers** | Tijdelijke rekenruimte | Varieert per backend en batchgrootte |
| **Agentinstructies** | Systeemprompts en tooldefinities | Gebruikt context voordat projectbestanden binnenkomen |

**Dat een modelbestand op de kaart past, bewijst niet dat je een bruikbare agent hebt.** De runtime heeft ruimte nodig voor de cache, tijdelijke buffers, tooldefinities en het volgende antwoord.

## Context is het echte budget

Programmeagents gebruiken context voor meer dan bronbestanden. Het budget omvat ook systeeminstructies, toolschema's, directorylijsten, shelluitvoer, compilermeldingen, testresultaten en eerdere gespreksbeurten.

Drie MCP-verbindingen met uitgebreide tooldefinities gebruiken vaak enkele duizenden tokens voordat de agent een projectbestand opent. Een kleine standaardcontext laat weinig ruimte over voor code. De agent antwoordt nog steeds, maar verliest de werkset die nodig is voor reparaties in meerdere stappen.

De [runtime-FAQ van Ollama](https://docs.ollama.com/faq) noemt een standaardcontext van 4.096 tokens. `OLLAMA_CONTEXT_LENGTH` wijzigt de standaardwaarde. `OLLAMA_NUM_PARALLEL` schaalt het benodigde geheugen met het aantal gelijktijdige verzoeken. Noteer beide waarden voordat je een lokale benchmark vergelijkt met een resultaat voor één verzoek.

```bash
OLLAMA_CONTEXT_LENGTH=32768 OLLAMA_NUM_PARALLEL=1 ollama serve
```

Dit voorbeeld stelt een standaard van 32K in voor één actief verzoek. Het reserveert geen 32K tokens voor projectbestanden. Instructies, tooldefinities, invoer en uitvoer delen het venster nog steeds.

### Een eenvoudig contextrecord

Noteer deze waarden voordat je GPU's vergelijkt:

- **Projectgrootte:** bestanden en het geschatte aantal bronregels in een normale taak.
- **Tooloverhead:** systeemprompt, MCP-schema's, shelltools en editorinstructies.
- **Foutpayload:** normale lengte van compiler- en testuitvoer.
- **Doelcontext:** de grootste prompt die je zonder afkappen wilt behouden.
- **Antwoordruimte:** ruimte voor de geplande patch en uitleg.

Gebruik het resultaat als werklastspecificatie. Een ontwikkelaar die één bestand tegelijk bewerkt, heeft een andere geheugenbehoefte dan iemand die een agent een API door een monorepo laat volgen.

## De KV-cache verandert de rangorde

Twee modellen met ongeveer evenveel parameters hebben vaak verschillende contextkosten. Een dicht model waarin elke laag bijdraagt aan de groeiende cache heeft vaak meer geheugen nodig dan een model met een hybride attentionarchitectuur.

Een 27B-programmeermodel dat in het referentiemateriaal wordt besproken, gebruikt een beperkt aantal lagen met volledige attention. Andere lagen gebruiken een samenvatting met vaste grootte. De gerapporteerde cachekosten voor een 128K-context blijven onder 9GB. Een model van vergelijkbare grootte met volledig groeiende attention in elke laag heeft volgens het rapport bij dezelfde contextlengte meer dan 21GB nodig.

Deze cijfers beschrijven specifieke modelarchitecturen en runtime-instellingen. Gebruik ze als reden om de architectuur te bekijken, niet als universele geheugenformule.

| Modelgedrag | Contextseffect | Gevolg voor hardware |
|---|---|---|
| **Volledige attention in elke laag** | Grote cachegroei | Meer geheugen nodig voor lange prompts |
| **Hybride of sliding attention** | Lagere cachegroei in sommige lagen | Meer contextmarge bij dezelfde modelgrootte |
| **Mixture of experts** | Minder actieve parameters per token | Minder berekening per token, maar alle gewichten moeten worden opgeslagen |
| **Uitbreiding voor lange context** | Groter werkvenster | Meer cachegeheugen en meer promptverwerking |

**Lees de modelarchitectuur voordat je geheugen koopt.** Het aantal parameters verbergt op zichzelf de kosten van een lange programmeersessie.

## Kies op basis van de GPU-geheugenklasse

### Vier tot acht GB

Kleine dichte modellen blijven de praktische keuze. Ze passen op de kaart, antwoorden snel en werken goed voor autocomplete, korte uitleg en kleine bestandswijzigingen.

Een groter model met CPU-offload kan tekst produceren, maar responstijd wordt vaak de beperkende factor. Een programmeeragent leest bestanden herhaaldelijk en roept tools herhaaldelijk aan. Een configuratie van vier tokens per seconde maakt van elke reparatie een lange wachttijd, ook wanneer het model technisch draait.

Mixture-of-expertsmodellen bieden een andere route. Een klein actief deel verlaagt de rekenbelasting, terwijl de volledige gewichtenset deels in systeemgeheugen staat. Deze aanpak vraagt om veel RAM en snelle overdrachtspaden.

| Workload | Aanbevolen richting |
|---|---|
| **Autocomplete** | Klein dicht model met een korte prompt |
| **Wijzigingen in één bestand** | Klein instructmodel met toolondersteuning |
| **Agent voor de hele repository** | Huur een grotere GPU of vergroot eerst het systeemgeheugen |
| **Privécode onder een NDA** | Gebruik een lokaal model, maar accepteer een kleinere scope of tragere runs |

**Koop in deze klasse eerst systeem-RAM voordat je een groot model nastreeft.** Een stabiel klein model is beter dan een groot model dat het grootste deel van zijn tijd data over de bus verplaatst.

### Twaalf tot zestien GB

Deze klasse opent de deur naar een 27B-programmeermodel, maar de keuze van de quantisatie wordt centraal. Een standaard 4-bit build van bijna 17GB past niet op een kaart van 16GB zodra runtime-overhead meetelt.

Een 3-bit build van bijna 13GB laat meer ruimte over voor context. Een kaart van 12GB stuurt de keuze naar een 2-bit build of een kleiner mixture-of-expertsmodel. De kwaliteit hangt af van de specifieke quantizer en het calibratieproces. Twee uploads met dezelfde bitdiepte leveren daarom vaak verschillende programmeerresultaten.

Controleer het volgende voordat je een gequantiseerd model downloadt:

- **Auteur van de quantizer en releasenotities**
- **Calibratiedata en evaluatieresultaten**
- **Compatibiliteit van de tokenizer**
- **Tests voor toolaanroepen**
- **Contextlengte met de gekozen quantisatie**
- **Runtimeondersteuning in Ollama, llama.cpp of de gekozen frontend**

**Beschouw “2-bit” of “3-bit” niet als een volledige kwaliteitsbeschrijving.** De packingmethode en het calibratierecord tellen mee.

### Vierentwintig tot tweeëndertig GB

Dit is de meest flexibele reeks voor een 27B-programmeermodel. Een kaart van 24GB past vaak een 4-bit build met bruikbare context, maar een volledig venster van 128K kan de resterende geheugenruimte overschrijden. Een kaart van 32GB geeft de runtime meer ruimte voor cache en tijdelijke allocaties.

Deze reeks maakt eigendom ook eenvoudiger te rechtvaardigen. Eén GPU verwerkt de workload zonder de complexiteit van een verdeling over twee kaarten. Het systeem gebruikt minder stroom dan een multi-GPU-build en softwareondersteuning is eenvoudiger te testen.

| Capaciteit | Praktische positie |
|---|---|
| **24GB** | Sterk 4-bitmodel met contextlimieten die je moet meten |
| **32GB** | 4-bit of 6-bit 27B-model met meer contextmarge |
| **48GB** | Hogere precisie of grotere cache zonder het kernmodel te wijzigen |

**De reeks van 24GB tot 32GB is de verstandige eigendomszone voor regelmatig privé programmeerwerk.** Je vermijdt het zwakste offloadgedrag zonder dat je datacenterhardware in een desktopkast moet plaatsen.

### Achtenveertig GB en hoger

Meer geheugen betekent niet automatisch een nieuw model. Hetzelfde 27B-model kan op een kaart van 48GB met 8-bitprecisie draaien, met een grotere cache en minder compromissen. De verbetering zit in consistentie, contextmarge en uitvoerkwaliteit, niet in een nieuw redeneerniveau.

Bij 128GB verandert de beslissing. Een veel groter mixture-of-expertsmodel wordt mogelijk, maar promptverwerking wordt een serieuze zorg. Een model genereert soms snel terwijl het lang bezig is met het inlezen van een grote repository of een nieuw toolresultaat.

**Meet bij grote modellen de prefill-snelheid apart van de decode-snelheid.** Een snel antwoord na een trage promptlezing voelt in een agentworkflow nog steeds traag.

## Decodesnelheid is slechts de helft van de test

**Decodesnelheid** meet gegenereerde tokens per seconde. De vraag is: “Hoe snel schrijft het model?” **Prefill-snelheid** meet promptverwerking. De vraag is: “Hoe snel leest het model?”

Een agent besteedt veel tijd aan lezen. Elke toolaanroep voegt nieuwe tekst toe. Een lang bronbestand, stacktrace of testlog komt in de prompt voordat het volgende antwoord begint.

| Metriek | Gebruikerservaring |
|---|---|
| **Decodetokens per seconde** | Hoe snel het antwoord verschijnt na verwerking |
| **Prompttokens per seconde** | Hoe lang de agent wacht voordat het antwoord begint |
| **Tijd tot het eerste token** | Gecombineerde vertraging van promptverwerking en voorbereiding |
| **Contextbehoud** | Hoeveel projectstatus tijdens de taak beschikbaar blijft |

**Benchmark je eigen promptgroottes.** Een korte synthetische prompt verbergt de kosten die tijdens repositorywerk het belangrijkst zijn.

## Test eerst runtime-instellingen

Hardware-upgrades zijn niet de eerste stap voor betere prestaties. Test runtime-instellingen voordat je een winkelpagina opent.

### Multi-tokenvoorspelling

Sommige combinaties van model en backend voorspellen meerdere toekomstige tokens en controleren die daarna in één doorgang. De functie wordt vaak aangeboden via een runtimeflag of compatibele draftconfiguratie.

Gerappporteerde tests in het referentiemateriaal laten grote verbeteringen zien op sommige high-endkaarten. Resultaten verschillen per modelfile, backend, driver en kaart. Apple Metal-paden behouden de vereiste functie mogelijk niet tijdens de conversie.

### Redeneerniveau

Een model met maximale redeneermodus besteedt meer tijd aan intern werk voordat het een resultaat terugstuurt. Gemiddeld redeneren geeft vaak een betere balans voor codeherstel, vooral wanneer de taak al een duidelijke foutmelding en een smal bestandsdoel heeft.

Gebruik een eenvoudige testmatrix:

1. Voer dezelfde bugfix-taak uit met laag, gemiddeld en hoog redeneren.
2. Noteer tijd tot het eerste token, totale tijd, patchesucces en testresultaat.
3. Herhaal dit met een korte prompt en een prompt ter grootte van een repository.
4. Behoud de instelling die de taak het beste afrondt, niet de instelling met de hoogste tokensnelheid.

**Gemiddeld redeneren met een compatibel multi-tokenpad is een sterk startpunt.** Controleer de kwaliteit op je eigen code voordat je dit als standaard instelt.

## Lokale hardware of een gehuurde GPU?

Gehuurde rekenkracht wint bij incidenteel gebruik. Je betaalt voor actieve sessies in plaats van het hele jaar een kaart te kopen, te koelen, bij te werken en van stroom te voorzien.

Eigen hardware wint wanneer de workload frequent, privé of offline is. Je vermijdt wachtrijen en krijgt een stabiele omgeving voor herhaalbare tests.

| Situatie | Beste eerste stap |
|---|---|
| **Enkele sessies per maand** | Huur een GPU of gebruik een API |
| **Dagelijks privé programmeren** | Koop een ondersteund systeem van 24GB tot 32GB |
| **Grote repository met vaak opnieuw laden** | Huur eerst en meet de prefill-snelheid |
| **Geen code verlaat het gebouw** | Bezit het kleinste systeem dat het contextdoel haalt |
| **Experimenteren met een nieuw model** | Huur voordat je hardware koopt |

Bereken het break-evenpunt met actieve uren, niet met kalenderuren. Neem elektriciteit, opslag, koeling, onderhoud en de tijd om de runtime werkend te houden mee.

**Een high-end GPU kopen voor incidentele experimenten is een hobby-uitgave.** Een systeem van 24GB tot 32GB dat dagelijks voor privéwerk wordt gebruikt, heeft een sterkere economische onderbouwing.

## Een betere aankoopchecklist

Gebruik deze volgorde wanneer je een model en een GPU vergelijkt:

1. **Definieer de taak.** Autocomplete, reparatie van één bestand, repository-agent of analyse met lange context.
2. **Meet de prompt.** Tel normale systeeminstructies, toolschema's, bestanden en testuitvoer.
3. **Bekijk cachegedrag.** Zoek architectuurnotities en metingen van contextgeheugen.
4. **Kies een quantisatie.** Controleer kwaliteitsresultaten van de specifieke upload, niet alleen de bitdiepte.
5. **Test prefill en decode.** Gebruik prompts uit je eigen repository.
6. **Stem het redeneren af.** Vergelijk de tijd voor een afgeronde taak op verschillende niveaus.
7. **Test privacy en onderhoud.** Controleer waar broncode naartoe gaat en wie de backend onderhoudt.
8. **Vergelijk huurkosten.** Gebruik verwachte actieve uren en neem stroom mee in de schatting voor een eigen systeem.

## Eindadvies

**Onder 12GB draai je een kleiner model of een mixture-of-expertsmodel met genoeg systeem-RAM.** Forceer geen dicht 27B-model op een configuratie die het grootste deel van de tijd aan offload besteedt.

**Van 12GB tot 16GB richt je je op quantisatiekwaliteit en een beheerst contextdoel.** Een goed geteste 2-bit of 3-bit build met toolondersteuning is nuttiger dan een 4-bitbestand dat nooit netjes past.

**Van 24GB tot 32GB wordt een 27B-programmeermodel de praktische standaard voor dagelijks privéwerk.** Meet contextgebruik en promptsnelheid voordat je aanneemt dat het volledige aangekondigde venster beschikbaar is.

**Bij 48GB en hoger besteed je extra geheugen eerst aan precisie, cacheruimte en stabiele sessies voordat je naar een groter model overstapt.** Zodra je in het gebied van 128GB komt, verdienen promptleessnelheid en huureconomie meer aandacht dan ruwe capaciteit.

De modelnaam is alleen het beginpunt. De nuttige vraag is hoeveel projectcontext overblijft nadat model, runtime, tools en cache hun deel hebben genomen.

## Gerelateerde artikelen

- [32GB VRAM voor Qwen 27B: de lokale AI-hardwaregids](/articles/32gb-vram-qwen-27b-hardware-guide/), gericht op hardwarepaden voor een 27B-workload.
- [Llama 3.1 8B en Qwen3.8 27B GPU-benchmarks op Vast.ai](/articles/qwen38-27b-vast-ai-gpu-benchmark/), gemeten resultaten van gehuurde GPU's en limieten bij lange context.
- [Lokale AI in 2026: een 27B-model verslaat Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/), modelkwaliteit, quantisatie en de economie van lokale hardware.
