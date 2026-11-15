---
title: "Hermes-modellen lokaal testen: welke GPU- en modelcombinaties ik zou kiezen"
date: 2026-10-24
lastmod: 2026-11-15
toc: true
draft: false
description: "Mijn modeladviezen voor Hermes zijn gebaseerd op tests met lange context, tools, streaming en beeldherkenning op RTX 5060 Ti-, RTX 2000E Ada-, RTX 3060 Ti- en RTX 3070-systemen."
genre: ["Kunstmatige intelligentie", "Lokale AI", "Hardwareonderdelen"]
tags: ["Hermes Agent", "lokale taalmodellen", "benchmarks voor taalmodellen", "GPU-inferentie", "RTX 3060 Ti", "RTX 3070", "RTX 2000E Ada", "RTX 5060 Ti", "modelkwalificatie", "toolaanroepen", "lange context", "llama.cpp", "Ollama", "Qwen3.5", "Qwen3.6", "Qwen3.8"]
cover: "/img/cover/hermes-local-model-gpu-benchmarks.webp"
coverAlt: "Geïllustreerde videokaarten met twee ventilatoren en een laag profiel naast de titel Hermes Model Benchmarks op een donkerblauwe achtergrond"
coverCaption: ""
---

Voor Hermes-taken met een lange context zou ik beginnen met Qwen3.5 35B op twee RTX 5060 Ti-kaarten van 16 GB. De geteste route behield 239.153 invoertokens via LiteLLM en slaagde afzonderlijk voor tool-, streaming-, vision-, wachtrij- en annuleringscontroles. Qwen3.6 is mijn alternatief met één kaart. Op systemen met een RTX 3060 Ti of RTX 3070 zou ik beginnen met Qwen3.5 2B of 4B.

Die keuzes komen voort uit tests met modellen via de inferentieroutes die de agent gebruikt. Ik controleerde het behoud van lange invoer, toolrondes, gestreamde antwoorden, beeldvragen en het vrijgeven van modellen. Ook testte ik de modi en geheugeninstellingen achter de routes, omdat een model dat laadt weinig zegt over zijn nut tijdens een lange agentaanvraag.

Hermes vereist minstens 64.000 contexttokens voor agentgebruik met tools. Ik gebruikte 65.536 werkelijk verwerkte invoertokens als drempel voor kwalificatie bij lange context. Het aantal invoertokens zegt meer dan de contextgrootte die de server adverteert. ([Documentatie van Hermes Agent-providers](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md))

## Welke GPU's in elk systeem zaten

De letters bij de systemen verwijzen in de resultaten steeds naar deze hardwarecombinaties.

| Systeem | GPU's voor deze benchmark | Mijn startkeuze voor het model |
|---|---|---|
| A | 2 × GeForce RTX 5060 Ti, elk 16 GB | Qwen3.5 35B op beide kaarten of Qwen3.6 op één kaart |
| B | 1 × RTX 2000E Ada, 16 GB | Qwen3.5 9B als verwerking van lange invoer enkele minuten mag duren |
| C | 1 × RTX 2000E Ada, 16 GB | Gemma 3 4B voor de geteste route met lange invoer; Qwen3.5 0.8B zonder denken voor beperkte terughaaltaken |
| D | 1 × RTX 2000E Ada, 16 GB | Qwen3.5 9B, Gemma 4 12B-IT of GPT-OSS 20B voor de geteste werklasten met grotere modellen |
| E | 9 × GeForce RTX 3060 Ti, elk 8 GB | Qwen3.5 2B of 4B |
| F | 8 × GeForce RTX 3060 Ti, elk 8 GB | Qwen3.5 2B of 4B |
| G | 3 × GeForce RTX 3070 | Qwen3.5 2B of 4B |

Het aantal geïnstalleerde kaarten betekent niet dat elke aanvraag alle GPU's gebruikte. De tests met Qwen3.5 35B en Flash Next gebruikten beide kaarten in systeem A. Qwen3.6 gebruikte één kaart. Bij de geslaagde vision-herhaling van Qwen3.5 4B op systeem E werd één geselecteerde kaart uit een pool van acht gebruikt, terwijl een negende kaart buiten het AI-werk bleef.

Beschouw de onderstaande tijden als resultaten van de geteste combinatie van model, runtime en systeem. Deze runs vergelijken bruikbare configuraties. Ze isoleren de GPU-architectuur niet als oorzaak van een snelheidsverschil.

## Twee RTX 5060 Ti-kaarten maken Qwen3.5 35B mijn keuze voor lange context

Qwen3.5 35B behield in deze tests de meeste invoer. De directe Ollama-reeks behield 248.279 invoertokens binnen een runtimecontext van 262.144 tokens. Een aparte gestreamde gateway-aanvraag behield 239.153 invoertokens, gaf de openingsmarkering terug en eindigde normaal na 31 uitvoertokens in 148,12 seconden.

Het gateway-resultaat is relevant voor Hermes, omdat de aanvraag via de broker en LiteLLM liep. Afzonderlijke aanvragen voltooiden een toolronde, herkenden een rode afbeelding en gaven twee juiste antwoorden toen ze tegelijk werden ingediend. De broker zette die twee aanvragen in de wachtrij. Toen de stream werd gesloten, gaf de broker de aanvraag vrij en werd het model binnen 60,31 seconden uit het geheugen gehaald.

| Aanvraag met Qwen3.5 35B | Invoertokens | Uitvoertokens | Duur | Resultaat |
|---|---:|---:|---:|---|
| Directe Ollama, eerste opeenvolgende stap | 69,429 | 31 | 38.783 s | Exacte openingsmarkering |
| Directe Ollama, voortzetting met gedeelde prefix | 124,179 | 31 | 28.472 s | Exacte openingsmarkering |
| Directe Ollama, voortzetting met gedeelde prefix | 182,579 | 31 | 38.974 s | Exacte openingsmarkering |
| Directe Ollama, voortzetting met gedeelde prefix | 248,279 | 31 | 54.215 s | Exacte openingsmarkering |
| Gestreamde brokeraanvraag | 69,427 | 29 | 38.872 s | Exacte openingsmarkering |
| Gestreamde LiteLLM-aanvraag | 239,153 | 31 | 148.12 s | Exacte openingsmarkering, clean unload |

De opeenvolgende directe aanvragen hergebruikten een steeds langere prefix. Hun tijden beschrijven voortzettingen met een warme cache. De meting van 54,215 seconden is geen onafhankelijke koude meting voor een nieuwe prompt van 248K.

In de grootste directe fase meldde het model ongeveer 27,3 miljard bytes resident geheugen over beide GPU's. De pieken per kaart bereikten 14.964 en 12.386 MiB.

De piektemperaturen bereikten 62 en 63 °C; de run registreerde geen OOM- of Xid-fout. Binnen de ingestelde context bleven 13.865 tokens over voor voortzetting. Het korte antwoord met de markering gebruikte daarvan 31 tokens.

Ik zou deze route kiezen wanneer behoud van een grote werkset belangrijker is dan het kortste eerste antwoord. De tool- en visioncontroles tonen bruikbaar agentgedrag, terwijl de lange-invoertest het behoud ervan aantoont. Het gaat om afzonderlijke werklasten.

## Qwen3.6 is de optie met één kaart

Qwen3.6-35B-A3B UD-Q4_K_XL behield 131.000 invoertokens op één RTX 5060 Ti. De andere kaart bleef tijdens de test ongebruikt. Dit geeft het systeem een bruikbaar alternatief wanneer je niet beide kaarten aan één model wilt toewijzen.

| Qwen3.6-gatewayaanvraag | Invoertokens | Uitvoertokens | Duur | Resultaat |
|---|---:|---:|---:|---|
| Eerste lange aanvraag | 66,007 |  | 167.82 s | Openingsmarkering behouden |
| Langere aanvraag | 90,000 | 11 | 159.92 s | Openingsmarkering behouden, zero cached input |
| Langere aanvraag | 119,999 | 11 | 250.61 s | Openingsmarkering behouden, zero cached input |
| Bijna aan de runtimegrens | 131,000 | 11 | 287.09 s | Openingsmarkering behouden, zero cached input |

De aanvraag met 131.000 tokens naderde de runtimegrens van 131.072 tokens. Voor een agent zou ik meer ruimte overlaten voor het antwoord en latere toolberichten. Een meting vlak bij de limiet levert nuttig bewijs over invoerverwerking, maar is geen verstandig standaardbudget.

Toolgebruik slaagde toen denken was uitgeschakeld. De standaardmodus voor denken verbruikte de testlimiet van 512 tokens voordat de toolaanroep werd gedaan. De geslaagde pilot slaagde ook voor snelle, gestreamde en vision-aanvragen. De eerste contextcontrole met 65.845 tokens duurde 139,57 seconden.

## Qwen3.8 27B wint de vergelijking met gelijke invoer van 66K

Bij dezelfde markeringstest met 66.007 tokens op systeem A gaf Qwen3.8 27B het snelste antwoord. Ik zou deze route beschikbaar houden voor aanvragen rond die geteste invoergrootte, naast Qwen3.5 35B voor de grotere werkset.

| Route op systeem A | Invoertokens | Duur | Resultaat |
|---|---:|---:|---|
| Qwen3.8 27B | 66,007 | 54.64 s | Openingsmarkering behouden |
| Qwen3.6-35B-A3B UD-Q4_K_XL | 66,007 | 167.82 s | Openingsmarkering behouden |
| Qwen3.8-Flash-Next UD-IQ4_XS | 66,007 | 164.58 s | Openingsmarkering behouden |
| Flash Next IQ4 compatibility alias | 66,007 | 213.25 s | Markering behouden |

Qwen3.8 27B had ongeveer een derde nodig van de looptijd van de overeenkomstige Qwen3.6- en Flash Next-aanvragen. Dit zijn metingen van volledige aanvragen met de geteste runtimes, geen vergelijking van alleen de hardware.

Ook snelle antwoorden, streaming en toolgebruik slaagden. De modus zonder denken voltooide de volledige kleurreeks en toolronde. De test met denken gaf binnen de limiet van 512 tokens slechts een deel van de kleurreeks terug.

Flash Next is op dit systeem minder geschikt als standaardkeuze vanwege de geheugendruk. De pilot met 65.847 tokens slaagde in 201,41 seconden bij een runtimecontext van 98.304 tokens. Twee eerdere profielen met een context van 131.072 tokens bereikten hun geheugenlimiet voordat ze klaar waren.

De latere route bereikte de cgroup-limiet van 54 GiB. Voor werk zonder toezicht zou ik een route met meer geheugerruimte kiezen.

De route met de naam `flash-iq2` gebruikte de Flash Next IQ4-compatibiliteitsbackend. De naam betekent niet dat het resultaat IQ2 gebruikte.

## De RTX 2000E Ada verwerkt lange invoer, maar de modelkeuze bepaalt de wachttijd

Gemma 3 4B is mijn voorkeur voor lange invoer op systeem C. Twee routes behielden meer dan 84K invoertokens in ongeveer 88 seconden. De grotere modellen slaagden ook voor nuttige controles van invoerbehoud, maar hun aanvragen duurden enkele minuten.

| Systeem | Model en route | Invoertokens | Duur | Resultaat |
|---|---|---:|---:|---|
| B | Qwen3.5 9B, gateway | 72,265 | 263 s | Beide markeringen behouden; latere herstelcontrole voor mining geslaagd |
| C | Gemma 3 4B, gateway | 84,044 | 88.05 s | Openingsmarkering behouden |
| C | Gemma 3 4B, Aperture | 84,045 | 87.68 s | Openingsmarkering behouden |
| C | Gemma 4 12B-IT, gateway | 67,254 | 263.07 s | Openingsmarkering behouden |
| C | Gemma 4 12B-IT, Aperture zonder streaming | 67,255 | 274.24 s | Openingsmarkering behouden |
| C | Gemma 4 12B-IT, Aperture met streaming | 67,255 | 282.16 s | Openingsmarkering behouden |
| C | Qwen3.5 9B, gateway | 75,648 | 319.36 s | Openingsmarkering behouden, model uit het geheugen verwijderd |
| C | GPT-OSS 20B, gateway | 84,099 | 315.83 s | Openingsmarkering behouden, model uit het geheugen verwijderd |
| D | Qwen3.5 9B, Aperture | 81,051 | 324.07 s | Behoudstest geslaagd op het geïnstalleerde artefact |
| D | Gemma 4 12B-IT, Aperture | 72,057 | 300.67 s | Behoudstest geslaagd op het geïnstalleerde artefact |
| D | GPT-OSS 20B, Aperture | 72,104 | 245.94 s | Behoudstest geslaagd op het geïnstalleerde artefact |

Streaming verkortte het lange voorverwerken van Gemma 4 op systeem C niet. De eerste gestreamde inhoud kwam na 277,49 seconden, later dan het volledige niet-gestreamde antwoord van 274,24 seconden. Een eerdere niet-gestreamde poging liep vast op de time-out voordat de geslaagde herhaling lukte. Ik zou deze route alleen gebruiken wanneer enkele minuten wachttijd bij de eerste verwerking bij de taak passen.

Gemma 3 4B laat ook zien waarom kwalificatie per getest systeem moet gebeuren. Systeem D miste de openingsmarkering in twee terughaaltests met 65K, waaronder een herhaling bij temperatuur nul met 67.252 invoertokens. De deterministische aanvraag eindigde normaal in 62,07 seconden terwijl het model volledig op de GPU stond.

Een snelle voltooiing en een normaal API-antwoord betekenden niet dat het antwoord juist was. Ik zou de geslaagde route op systeem C gebruiken en de falende route op systeem D buiten de Hermes-selectie houden.

## De denkmodus bepaalt of Qwen3.5 0.8B bruikbaar is

Qwen3.5 0.8B werd op systeem C een bruikbare kandidaat voor beperkte terughaalvragen nadat denken was uitgeschakeld. Het kleine Q8_0-model behield via de gateway 75.649 invoertokens in 65,92 seconden. Dit resultaat geldt voor het geteste Q8_0-artefact en de route zonder denken, niet voor de oudere configuraties met een context van 16K elders in de tabel.

| Aanvraag met Qwen3.5 0.8B op systeem C | Invoertokens | Uitvoertokens | Duur | Resultaat |
|---|---:|---:|---:|---|
| Standaard denkmodus, korte diagnose | 9,050 | 3,391 | 66.56 s | Exacte openingsmarkering |
| Denken uitgeschakeld, vergelijkbare diagnose | 9,055 | 21 | 7.65 s | Exacte openingsmarkering, no reasoning text |
| Standaard denkmodus, lange poging |  |  | Time-out na 600 s | Geen voltooid antwoord |
| Denken uitgeschakeld, native Ollama | 75,656 | 22 | 69.80 s | Exacte openingsmarkering |
| OpenAI-compatibel eindpunt zonder denken | 75,646 | 12 | 69.09 s | Exacte openingsmarkering |
| Broker dwingt modus zonder denken af | 75,647 | 13 | 66.83 s | Exacte openingsmarkering |
| LiteLLM via systeem A naar systeem C | 75,649 | 15 | 65.92 s | Exacte openingsmarkering |

De duur van de vergelijkbare diagnosetest daalde van 66,56 naar 7,65 seconden, ongeveer 8,7 keer sneller, terwijl de uitvoer kromp van 3.391 naar 21 tokens. Daarom zou ik de redeneermodus expliciet instellen voor eenvoudige extractie- en routeringstaken. Standaardredenering besteedde het meeste werk aan uitvoer die de taak niet nodig had.

Een korte OpenAI-compatibele test miste de markering voordat de herhaling bij temperatuur nul slaagde. De geslaagde routetests gebruikten de modus zonder denken en een natuurlijke voltooiing zonder uitvoerlimiet. Drie andere gateways slaagden voor korte markeringstests in 4,22, 4,37 en 3,85 seconden. Die controles bevestigen de routering; de aanvraag met 75.649 tokens toont behoud van lange invoer via de gateway.

Ik zou deze route uitproberen voor beperkte terughaal- en extractietaken. Voor open agentredeneringen zou ik een groter model kiezen. Eén synthetische markering terugvinden is een beperktere taak dan plannen, programmeren of verschillende tools coördineren.

## De RTX 3060 Ti- en RTX 3070-systemen zijn geschikt voor Qwen3.5 2B en 4B

Qwen3.5 2B en 4B zijn mijn praktische startkeuzes voor kaarten met 8 GB. Hun teksttests met context op systemen E, F en G slaagden met 65.579 invoertokens en duurden 30,343 tot 93,753 seconden. De geteste 4B-routes slaagden ook voor tool-, streaming- en beeldcontroles.

Bij de vision-herhaling met context op systeem E behield de 4B-route beide markeringen en de volgorde van de beeldkleuren bij 65.637 invoertokens in 44,88 seconden. Aanvragen met de kleuren in voorwaartse en omgekeerde volgorde slaagden ook. De herhaling gebruikte één gezonde kaart nadat een andere kaart een Xid 79-linkfout gaf en het systeem opnieuw was opgestart.

| Systeem | Qwen3.5 2B-tekstcontext | Qwen3.5 4B-tekstcontext | Qwen3.5 4B-visioncontext |
|---|---|---|---|
| E, RTX 3060 Ti pool | 65,579 tokens, 30.343 s | 65,579 tokens, 53.787 s | 65,637 tokens, 44.88 s |
| F, RTX 3060 Ti pool | 65,579 tokens, 61.282 s | 65,579 tokens, 93.753 s | 65,635 tokens, 84.749 s |
| G, RTX 3070 pool | 65,579 tokens, 76.731 s | 65,579 tokens, 90.807 s | 65,635 tokens, 87.496 s |

Elk van deze systemen registreerde 29 geslaagde controles. Het tijdsverschil tussen de twee RTX 3060 Ti-systemen laat ook zien waarom ik een getest systeemprofiel zou kiezen in plaats van kaarten op basis van deze aanvraagtijden te rangschikken.

Alle zeven systemen gingen na het inferentiesegment terug naar mining. De afzonderlijke herstelcontrole na stop op systeem B slaagde met nieuwe geaccepteerde shares. De defecte kaart in systeem E ging later na een herstart en PCIe-linkversterking terug naar mining, terwijl de uitsluiting uit de AI-pool actief bleef. Mining herstellen aan het einde van het testvenster is iets anders dan automatisch terugschakelen na één inferentieaanvraag.

## Een model laden is geen kwalificatie

Ik zou DeepSeek Coder V2 16B uitsluiten van de geteste Hermes-keuzes voor 65K. De run met f16-cache behield 50.477 invoertokens, maar de run met het doel van 65K bereikte de VRAM-bewaking. Alternatieven met Q4- en Q8-cache laadden de gewichten op de GPU's, maar liepen daarna tegen hostgeheugenlimieten of een lage verwerkingssnelheid voor lange prompts aan.

| DeepSeek Coder V2-cacheprofiel | Runtimecontext | Waargenomen resultaat | Mijn beoordeling |
|---|---:|---|---|
| f16 | 81,920 | Terughaaltest met 50.477 tokens geslaagd; te grote aanvraag afgewezen | Bruikbaar resultaat met kortere context |
| f16 | 73,728 | Prefill voor 65K-doel stopte bij 15.802 MiB GPU-gebruik | Voldoet niet aan 65K-kwalificatie |
| Q4_0 | 98,304 | Lange prefill daalde tot 96,72 tokens/s voordat de run gecontroleerd stopte | Minder geschikt voor deze werklast |
| Q8_0 | 77,824 | Lange prefill daalde tot 120,12 tokens/s voordat de run gecontroleerd stopte | Minder geschikt voor deze werklast |
| Q4_0 / Q8_0, larger profiles | 163,840 / 98,304 | Hostgeheugenbewaking stopte de tests | Geheugenpassing moet voor het hele systeem worden beoordeeld |

De praktische les is om de aanvraag te testen die je wilt versturen. GPU-residentie, een kort antwoord en een grote ingestelde context bewijzen niet dat lange invoer met bruikbare vertraging behouden blijft.

Granite 4.2 8B en GPT-OSS 20B verbeterden na vervolgwerk per route op systeem A. De Q6_K-route van Granite behield 66.082 invoertokens in 88,636 seconden met nul tokens uit de cache. GPT-OSS voltooide de toolronde na de brokerreparatie, met 9,854 seconden voor de aanroep en 9,849 seconden voor het vervolg. Ik houd deze geslaagde routecontroles apart van eerdere onvolledige pogingen.

## Volledige benchmarkresultaten

De tabel bevat 295 controles voor 59 combinaties van modellen en systemen. De matrix bevat 273 geslaagde controles, één mislukte terughaaltest en zeven onvolledige, inconsistente of incompatibele resultaten. Veertien controles vallen buiten de kwalificatiescope van 65K. Elke rij toont het gemeten resultaat.

Mijn aanbevelingen gelden voor de geslaagde routes en werklasten. Een mislukte of onvolledige rij kwalificeert het betreffende gedrag niet.

Geslaagde tests met een korte context en embeddings gelden voor hun eigen werklasten. Een geslaagde context van 16K of 32K kwalificeert een route niet voor de Hermes-werklast met 65.536 invoertokens. Modelnamen zijn hier routelabels. Het label `flash-iq2` verwijst naar de IQ4-compatibiliteitsbackend.

De rij voor Qwen3.5 35B-context op systeem A is de laatste gedeelde-prefixstap uit de reeks hierboven. Tooltijden met een plusteken tonen de aanroep en het vervolg afzonderlijk.

De rij voor gelijktijdigheid vermeldt de tijden van de twee aanvragen in de wachtrij. De annuleringsrij toont hoe lang het duurde om vrij te geven nadat de client de stream had gesloten. Aanvullende contextreeksen en routevergelijkingen voor Qwen3.5 0.8B staan in hun eigen tabellen hierboven.

### Systeem A

| Routelabel van het model | Controle | Resultaat | Invoertokens | Aanvraagtijd |
|---|---|---|---:|---:|
| bonsai-2-27b | context | Geslaagd | 65,621 | 88.746 s |
| bonsai-2-27b | quick | Geslaagd | 57 | 6.429 s |
| bonsai-2-27b | stream | Geslaagd |  | 9.371 s |
| bonsai-2-27b | tools | Geslaagd |  | 10.478 s |
| deepseek-coder-v2:16b | context | Incompatibel | 50,477 |  |
| deepseek-coder-v2:16b | quick | Geslaagd | 77 | 43.239 s |
| flash-iq2 | context | Geslaagd | 66,007 | 213.25 s |
| flash-iq2 | quick | Geslaagd |  | 56.03 s |
| flash-iq2 | stream | Geslaagd |  | 1.35 s |
| flash-iq2 | tools | Geslaagd |  | 16.55 s |
| gemma-4-12b-it | context | Geslaagd | 65,590 | 51.225 s |
| gemma-4-12b-it | quick | Geslaagd | 21 | 5.166 s |
| gemma-4-12b-it | stream | Geslaagd |  | 4.653 s |
| gemma-4-12b-it | tools | Geslaagd |  | 18.72 s |
| gemma-4-12b-it | vision | Geslaagd | 115 | 7.222 s |
| gemma-4-12b-it | vision_context | Geslaagd | 65,685 | 56.06 s |
| gemma-4-12b-it | vision_reverse | Geslaagd | 115 | 7.467 s |
| gemma-4-e4b-it | context | Geslaagd | 65,590 | 21.889 s |
| gemma-4-e4b-it | quick | Geslaagd | 21 | 17.919 s |
| gemma-4-e4b-it | stream | Geslaagd |  | 4.25 s |
| gemma-4-e4b-it | tools | Geslaagd |  | 8.734 s |
| gpt-oss-20b | context | Geslaagd | 65,637 | 159.155 s |
| gpt-oss-20b | quick | Geslaagd | 73 | 10.548 s |
| gpt-oss-20b | stream | Geslaagd |  | 20.594 s |
| gpt-oss-20b | tools | Geslaagd |  | 9.854 + 9.849 s |
| granite-4.2-3b | context | Geslaagd | 65,589 | 70.968 s |
| granite-4.2-3b | quick | Geslaagd | 20 | 4.009 s |
| granite-4.2-3b | stream | Geslaagd |  | 5.365 s |
| granite-4.2-3b | tools | Geslaagd |  | 6.086 s |
| granite-4.2-8b | context | Geslaagd | 66,082 | 88.636 s |
| granite-4.2-8b | quick | Geslaagd | 20 | 5.857 s |
| granite-4.2-8b | stream | Geslaagd |  | 11.826 s |
| granite-4.2-8b | tools | Geslaagd |  | 11.852 s |
| qwen27b | context | Geslaagd | 66,007 | 54.64 s |
| qwen27b | quick | Geslaagd | 57 | 31.5 s |
| qwen27b | stream | Geslaagd |  | 0.92 s |
| qwen27b | tools | Geslaagd |  | 4.25 s |
| qwen3-embedding-0.6b | context | Geslaagd | 32,767 | 7.736 s |
| qwen3-embedding-0.6b | quick | Geslaagd | 14 | 2.125 s |
| qwen3.5-0.8b | context | Geslaagd | 16,429 | 10.5 s |
| qwen3.5-0.8b | quick | Geslaagd | 17 | 14.316 s |
| qwen3.5-0.8b | stream | Geslaagd |  | 2.125 s |
| qwen3.5-0.8b | tools | Geslaagd |  | 4.416 s |
| qwen3.5-2b | context | Geslaagd | 65,581 | 11.175 s |
| qwen3.5-2b | quick | Geslaagd | 17 | 4.519 s |
| qwen3.5-2b | stream | Geslaagd |  | 3.736 s |
| qwen3.5-2b | tools | Geslaagd |  | 5.046 s |
| qwen3.5-4b | context | Geslaagd | 65,579 | 36.451 s |
| qwen3.5-4b | quick | Geslaagd | 15 | 19.935 s |
| qwen3.5-4b | stream | Geslaagd |  | 17.496 s |
| qwen3.5-4b | tools | Geslaagd |  | 7.308 s |
| qwen3.5-4b | vision | Geslaagd | 70 | 7.848 s |
| qwen3.5-4b | vision_context | Geslaagd | 65,635 | 28.24 s |
| qwen3.5-4b | vision_reverse | Geslaagd | 70 | 4.386 s |
| qwen3.5-9b | context | Geslaagd | 65,581 | 34.139 s |
| qwen3.5-9b | quick | Geslaagd | 17 | 3.88 s |
| qwen3.5-9b | stream | Geslaagd |  | 3.378 s |
| qwen3.5-9b | tools | Geslaagd |  | 10.204 s |
| qwen3.5-9b | vision | Geslaagd | 72 | 4.441 s |
| qwen3.5-9b | vision_context | Geslaagd | 65,637 | 33.745 s |
| qwen3.5-9b | vision_reverse | Geslaagd | 72 | 3.97 s |
| qwen3.5:35b-a3b-q4_K_M | cancellation | Geslaagd |  | 60.31 s |
| qwen3.5:35b-a3b-q4_K_M | concurrency | Geslaagd |  | 26.23 / 25.33 s |
| qwen3.5:35b-a3b-q4_K_M | context | Geslaagd | 248,279 | 54.215 s |
| qwen3.5:35b-a3b-q4_K_M | gateway | Geslaagd | 239,153 | 148.12 s |
| qwen3.5:35b-a3b-q4_K_M | quick | Geslaagd | 79 | 10.08 s |
| qwen3.5:35b-a3b-q4_K_M | stream | Geslaagd | 69,429 | 38.783 s |
| qwen3.5:35b-a3b-q4_K_M | tools | Geslaagd |  | 15.22 + 14.83 s |
| qwen3.5:35b-a3b-q4_K_M | vision | Geslaagd |  | 18.39 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | context | Geslaagd | 65,845 | 139.57 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | quick | Geslaagd | 15 | 3.97 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | stream | Geslaagd |  | 0.45 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | tools | Geslaagd | 293 | 5.48 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | vision | Geslaagd | 38 | 0.59 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | context | Geslaagd | 65,847 | 201.41 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | quick | Geslaagd | 17 | 54.62 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | stream | Geslaagd |  | 1.2 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | tools | Geslaagd |  | 22.18 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | vision | Geslaagd |  | 3.86 s |

### Systeem B

| Routelabel van het model | Controle | Resultaat | Invoertokens | Aanvraagtijd |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Geslaagd | 65,590 | 299.163 s |
| gemma-4-12b-it | quick | Geslaagd | 21 | 15.261 s |
| gemma-4-12b-it | stream | Geslaagd |  | 148.792 s |
| gemma-4-12b-it | tools | Geslaagd |  | 34.124 s |
| gemma-4-12b-it | vision | Geslaagd | 120 | 61.455 s |
| gemma-4-12b-it | vision_context | Geslaagd | 65,690 | 295.581 s |
| gemma-4-12b-it | vision_reverse | Geslaagd | 120 | 32.511 s |
| gemma3-4b | context | Geslaagd | 65,584 | 67.382 s |
| gemma3-4b | quick | Geslaagd | 15 | 6.329 s |
| gemma3-4b | stream | Geslaagd |  | 24.138 s |
| gemma3-4b | vision | Geslaagd | 306 | 7.018 s |
| gemma3-4b | vision_context | Geslaagd | 65,876 | 70.912 s |
| gemma3-4b | vision_reverse | Geslaagd | 306 | 5.762 s |
| gpt-oss-20b | context | Geslaagd | 65,637 | 206.767 s |
| gpt-oss-20b | quick | Geslaagd | 72 | 16.583 s |
| gpt-oss-20b | stream | Geslaagd |  | 32.075 s |
| gpt-oss-20b | tools | Geslaagd |  | 28.102 s |
| nomic-embed-text | context | Onvolledig | 2,048 |  |
| nomic-embed-text | quick | Geslaagd |  | 7.117 s |
| qwen3-14b | context | Onvolledig |  | 1800.09 s |
| qwen3-14b | quick | Geslaagd | 15 | 37.199 s |
| qwen3-14b | stream | Geslaagd |  | 35.471 s |
| qwen3-14b | tools | Geslaagd |  | 87.554 s |
| qwen3-8b | context | Buiten 65K-scope: uitgesloten |  |  |
| qwen3-8b | quick | Buiten 65K-scope: geslaagd | 15 | 21.059 s |
| qwen3-8b | stream | Buiten 65K-scope: uitgesloten |  |  |
| qwen3-8b | tools | Buiten 65K-scope: uitgesloten |  |  |
| qwen3.5-9b | context | Geslaagd | 65,579 | 282.796 s |
| qwen3.5-9b | litellm_long_route | Geslaagd | 72,265 | 263 s |
| qwen3.5-9b | post_external_stop_mining | Geslaagd |  |  |
| qwen3.5-9b | quick | Geslaagd | 15 | 25.881 s |
| qwen3.5-9b | stream | Geslaagd |  | 143.44 s |
| qwen3.5-9b | tools | Geslaagd |  | 31.812 s |
| qwen3.5-9b | vision | Geslaagd | 75 | 32.015 s |
| qwen3.5-9b | vision_context | Geslaagd | 65,640 | 396.288 s |
| qwen3.5-9b | vision_reverse | Geslaagd | 75 | 28.626 s |

### Systeem C

| Routelabel van het model | Controle | Resultaat | Invoertokens | Aanvraagtijd |
|---|---|---|---:|---:|
| gemma-4-12b-it | aperture_context | Geslaagd | 67,255 | 274.24 s |
| gemma-4-12b-it | aperture_short | Geslaagd | 35 | 39.32 s |
| gemma-4-12b-it | aperture_stream_context | Geslaagd | 67,255 | 282.16 s |
| gemma-4-12b-it | context | Geslaagd | 65,670 | 313.661 s |
| gemma-4-12b-it | gateway_context | Geslaagd | 67,254 | 263.07 s |
| gemma-4-12b-it | gateway_short | Geslaagd | 27 | 20.98 s |
| gemma-4-12b-it | quick | Geslaagd | 21 | 16.447 s |
| gemma-4-12b-it | stream | Geslaagd |  | 15.175 s |
| gemma-4-12b-it | tools | Geslaagd |  | 37.821 s |
| gemma-4-12b-it | vision | Geslaagd | 120 | 58.52 s |
| gemma-4-12b-it | vision_context | Geslaagd | 65,690 | 308.759 s |
| gemma-4-12b-it | vision_reverse | Geslaagd | 120 | 31.25 s |
| gemma3-4b | aperture_context | Geslaagd | 84,045 | 87.68 s |
| gemma3-4b | aperture_after_system_d_route_change | Geslaagd | 24 | 5.42 s |
| gemma3-4b | aperture_short | Geslaagd | 22 | 5.45 s |
| gemma3-4b | aperture_stream | Geslaagd |  | 3.72 s |
| gemma3-4b | context | Geslaagd | 65,664 | 67.543 s |
| gemma3-4b | gateway_context | Geslaagd | 84,044 | 88.05 s |
| gemma3-4b | gateway_short_via_system_a | Geslaagd |  | 3.16 s |
| gemma3-4b | gateway_short_via_system_e | Geslaagd |  |  |
| gemma3-4b | gateway_short_via_system_f | Geslaagd |  | 4.15 s |
| gemma3-4b | gateway_short_via_system_g | Geslaagd |  | 6.06 s |
| gemma3-4b | quick | Geslaagd | 15 | 5.163 s |
| gemma3-4b | stream | Geslaagd |  | 24.691 s |
| gemma3-4b | vision | Geslaagd | 306 | 7.318 s |
| gemma3-4b | vision_context | Geslaagd | 65,876 | 72.476 s |
| gemma3-4b | vision_reverse | Geslaagd | 306 | 5.831 s |
| gpt-oss-20b | context | Geslaagd | 65,716 | 216.594 s |
| gpt-oss-20b | gateway_context | Geslaagd | 84,099 | 315.83 s |
| gpt-oss-20b | gateway_short | Inconsistent |  |  |
| gpt-oss-20b | quick | Geslaagd | 72 | 21.603 s |
| gpt-oss-20b | stream | Geslaagd |  | 31.957 s |
| gpt-oss-20b | tools | Geslaagd |  | 26.096 s |
| nomic-embed-text | context | Buiten 65K-scope: onvolledig | 2,048 |  |
| nomic-embed-text | quick | Buiten 65K-scope: geslaagd |  | 4.178 s |
| qwen3-14b | context | Buiten 65K-scope: onvolledig |  | 1800.06 s |
| qwen3-14b | quick | Buiten 65K-scope: geslaagd | 15 | 35.809 s |
| qwen3-14b | stream | Buiten 65K-scope: geslaagd |  | 35.43 s |
| qwen3-14b | tools | Buiten 65K-scope: geslaagd |  | 87.723 s |
| qwen3-8b | context | Buiten 65K-scope: uitgesloten |  |  |
| qwen3-8b | quick | Buiten 65K-scope: geslaagd | 15 | 21.293 s |
| qwen3-8b | stream | Buiten 65K-scope: onvolledig |  | 900.01 s |
| qwen3-8b | tools | Buiten 65K-scope: uitgesloten |  |  |
| qwen3.5-9b | context | Geslaagd | 65,662 | 287.984 s |
| qwen3.5-9b | gateway_context | Geslaagd | 75,648 | 319.36 s |
| qwen3.5-9b | gateway_short | Geslaagd | 21 | 72.14 s |
| qwen3.5-9b | quick | Geslaagd | 15 | 24.635 s |
| qwen3.5-9b | stream | Geslaagd |  | 143.157 s |
| qwen3.5-9b | tools | Geslaagd |  | 30.395 s |
| qwen3.5-9b | vision | Geslaagd | 75 | 27.756 s |
| qwen3.5-9b | vision_context | Geslaagd | 65,640 | 398.797 s |
| qwen3.5-9b | vision_reverse | Geslaagd | 75 | 28.645 s |

### Systeem D

| Routelabel van het model | Controle | Resultaat | Invoertokens | Aanvraagtijd |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Geslaagd | 65,590 | 275.395 s |
| gemma-4-12b-it | exact_digest_aperture_65k | Geslaagd | 72,057 | 300.67 s |
| gemma-4-12b-it | exact_digest_broker_short | Geslaagd | 34 | 30.74 s |
| gemma-4-12b-it | quick | Geslaagd | 21 | 15.05 s |
| gemma-4-12b-it | stream | Geslaagd |  | 14.722 s |
| gemma-4-12b-it | tools | Geslaagd |  | 33.869 s |
| gemma-4-12b-it | vision | Geslaagd | 120 | 56.315 s |
| gemma-4-12b-it | vision_context | Geslaagd | 65,690 | 282.174 s |
| gemma-4-12b-it | vision_reverse | Geslaagd | 120 | 29.978 s |
| gemma3-4b | context | Geslaagd | 65,584 | 63.564 s |
| gemma3-4b | exact_digest_65k_recall | Mislukt | 67,252 | 62.07 s |
| gemma3-4b | quick | Geslaagd | 15 | 5.151 s |
| gemma3-4b | stream | Geslaagd |  | 22.552 s |
| gemma3-4b | vision | Geslaagd | 306 | 8.276 s |
| gemma3-4b | vision_context | Geslaagd | 65,876 | 67.575 s |
| gemma3-4b | vision_reverse | Geslaagd | 306 | 5.651 s |
| gpt-oss-20b | context | Geslaagd | 65,637 | 189.07 s |
| gpt-oss-20b | exact_digest_aperture_65k | Geslaagd | 72,104 | 245.94 s |
| gpt-oss-20b | exact_digest_broker_short | Geslaagd | 84 | 15.96 s |
| gpt-oss-20b | quick | Geslaagd | 72 | 15.431 s |
| gpt-oss-20b | stream | Geslaagd |  | 31.052 s |
| gpt-oss-20b | tools | Geslaagd |  | 23.65 s |
| nomic-embed-text | context | Onvolledig | 2,048 |  |
| nomic-embed-text | quick | Geslaagd |  | 2.798 s |
| qwen3-14b | context | Onvolledig | 40,939 | 872.209 s |
| qwen3-14b | quick | Geslaagd | 15 | 36.021 s |
| qwen3-14b | stream | Geslaagd |  | 33.491 s |
| qwen3-14b | tools | Geslaagd |  | 82.471 s |
| qwen3-8b | context | Onvolledig |  | 1800.07 s |
| qwen3-8b | quick | Geslaagd | 15 | 19.283 s |
| qwen3-8b | stream | Geslaagd |  | 19.401 s |
| qwen3-8b | tools | Geslaagd |  | 65.054 s |
| qwen3.5-9b | context | Geslaagd | 65,579 | 258.048 s |
| qwen3.5-9b | exact_digest_aperture_65k | Geslaagd | 81,051 | 324.07 s |
| qwen3.5-9b | exact_digest_broker_short | Geslaagd | 29 | 94.48 s |
| qwen3.5-9b | quick | Geslaagd | 15 | 27.16 s |
| qwen3.5-9b | stream | Geslaagd |  | 28.62 s |
| qwen3.5-9b | tools | Geslaagd |  | 28.129 s |
| qwen3.5-9b | vision | Geslaagd | 75 | 25.047 s |
| qwen3.5-9b | vision_context | Geslaagd | 65,640 | 369.477 s |
| qwen3.5-9b | vision_reverse | Geslaagd | 75 | 27.602 s |

### Systeem E

| Routelabel van het model | Controle | Resultaat | Invoertokens | Aanvraagtijd |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Geslaagd | 65,590 | 49.086 s |
| gemma-4-e4b-it | quick | Geslaagd | 21 | 23.911 s |
| gemma-4-e4b-it | stream | Geslaagd |  | 28.136 s |
| gemma-4-e4b-it | tools | Geslaagd |  | 56.756 s |
| granite-4.0-h-tiny | context | Geslaagd | 65,566 |  |
| granite-4.0-h-tiny | quick | Geslaagd | 35 | 10.408 s |
| granite-4.0-h-tiny | stream | Geslaagd |  | 27.798 s |
| granite-4.0-h-tiny | tools | Geslaagd |  | 43.304 s |
| granite-4.2-3b | context | Geslaagd | 65,589 | 1014.03 s |
| granite-4.2-3b | quick | Geslaagd | 20 | 14.569 s |
| granite-4.2-3b | stream | Geslaagd |  | 6.948 s |
| granite-4.2-3b | tools | Geslaagd |  | 56.376 s |
| qwen3-embedding-0.6b | context | Geslaagd | 32,767 | 20.387 s |
| qwen3-embedding-0.6b | quick | Geslaagd | 14 | 9.592 s |
| qwen3.5-0.8b | context | Geslaagd | 16,429 | 9.128 s |
| qwen3.5-0.8b | quick | Geslaagd | 17 | 452.417 s |
| qwen3.5-0.8b | stream | Geslaagd |  | 11.163 s |
| qwen3.5-0.8b | tools | Geslaagd |  | 39.214 s |
| qwen3.5-2b | context | Geslaagd | 65,579 | 30.343 s |
| qwen3.5-2b | quick | Geslaagd | 15 | 12.509 s |
| qwen3.5-2b | stream | Geslaagd |  | 26.165 s |
| qwen3.5-2b | tools | Geslaagd |  | 42.056 s |
| qwen3.5-4b | context | Geslaagd | 65,579 | 53.787 s |
| qwen3.5-4b | quick | Geslaagd | 15 | 26.736 s |
| qwen3.5-4b | stream | Geslaagd |  | 26.02 s |
| qwen3.5-4b | tools | Geslaagd |  | 57.293 s |
| qwen3.5-4b | vision | Geslaagd | 72 | 10.09 s |
| qwen3.5-4b | vision_context | Geslaagd | 65,637 | 44.88 s |
| qwen3.5-4b | vision_reverse | Geslaagd | 72 | 9.96 s |

### Systeem F

| Routelabel van het model | Controle | Resultaat | Invoertokens | Aanvraagtijd |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Geslaagd | 65,590 | 98.443 s |
| gemma-4-e4b-it | quick | Geslaagd | 21 | 27.51 s |
| gemma-4-e4b-it | stream | Geslaagd |  | 28.042 s |
| gemma-4-e4b-it | tools | Geslaagd |  | 73.891 s |
| granite-4.0-h-tiny | context | Geslaagd | 65,599 | 19.692 s |
| granite-4.0-h-tiny | quick | Geslaagd | 35 | 43.818 s |
| granite-4.0-h-tiny | stream | Geslaagd |  | 27.296 s |
| granite-4.0-h-tiny | tools | Geslaagd |  | 75.377 s |
| granite-4.2-3b | context | Geslaagd | 65,589 | 145.179 s |
| granite-4.2-3b | quick | Geslaagd | 20 | 15.703 s |
| granite-4.2-3b | stream | Geslaagd |  | 35.482 s |
| granite-4.2-3b | tools | Geslaagd |  | 52.539 s |
| qwen3-embedding-0.6b | context | Geslaagd | 32,767 | 20.656 s |
| qwen3-embedding-0.6b | quick | Geslaagd | 14 | 8.122 s |
| qwen3.5-0.8b | context | Geslaagd | 16,429 | 13.326 s |
| qwen3.5-0.8b | quick | Geslaagd | 17 | 445.22 s |
| qwen3.5-0.8b | stream | Geslaagd |  | 13.266 s |
| qwen3.5-0.8b | tools | Geslaagd |  | 40.825 s |
| qwen3.5-2b | context | Geslaagd | 65,579 | 61.282 s |
| qwen3.5-2b | quick | Geslaagd | 15 | 16.738 s |
| qwen3.5-2b | stream | Geslaagd |  | 25.29 s |
| qwen3.5-2b | tools | Geslaagd |  | 47.444 s |
| qwen3.5-4b | context | Geslaagd | 65,579 | 93.753 s |
| qwen3.5-4b | quick | Geslaagd | 15 | 33.039 s |
| qwen3.5-4b | stream | Geslaagd |  | 25.658 s |
| qwen3.5-4b | tools | Geslaagd |  | 71.731 s |
| qwen3.5-4b | vision | Geslaagd | 70 | 43.053 s |
| qwen3.5-4b | vision_context | Geslaagd | 65,635 | 84.749 s |
| qwen3.5-4b | vision_reverse | Geslaagd | 70 | 27.518 s |

### Systeem G

| Routelabel van het model | Controle | Resultaat | Invoertokens | Aanvraagtijd |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Geslaagd | 65,590 | 92.696 s |
| gemma-4-e4b-it | quick | Geslaagd | 21 | 38.329 s |
| gemma-4-e4b-it | stream | Geslaagd |  | 43.549 s |
| gemma-4-e4b-it | tools | Geslaagd |  | 66.616 s |
| granite-4.0-h-tiny | context | Geslaagd | 65,599 | 69.777 s |
| granite-4.0-h-tiny | quick | Geslaagd | 35 | 33.17 s |
| granite-4.0-h-tiny | stream | Geslaagd |  | 31.751 s |
| granite-4.0-h-tiny | tools | Geslaagd |  | 63.338 s |
| granite-4.2-3b | context | Geslaagd | 65,589 | 100.849 s |
| granite-4.2-3b | quick | Geslaagd | 20 | 23.355 s |
| granite-4.2-3b | stream | Geslaagd |  | 28.75 s |
| granite-4.2-3b | tools | Geslaagd |  | 44.226 s |
| qwen3-embedding-0.6b | context | Geslaagd | 32,767 | 23.055 s |
| qwen3-embedding-0.6b | quick | Geslaagd | 14 | 8.924 s |
| qwen3.5-0.8b | context | Geslaagd | 16,429 | 16.74 s |
| qwen3.5-0.8b | quick | Geslaagd | 17 | 504.813 s |
| qwen3.5-0.8b | stream | Geslaagd |  | 15.095 s |
| qwen3.5-0.8b | tools | Geslaagd |  | 36.672 s |
| qwen3.5-2b | context | Geslaagd | 65,579 | 76.731 s |
| qwen3.5-2b | quick | Geslaagd | 15 | 20.949 s |
| qwen3.5-2b | stream | Geslaagd |  | 25.194 s |
| qwen3.5-2b | tools | Geslaagd |  | 37.552 s |
| qwen3.5-4b | context | Geslaagd | 65,579 | 90.807 s |
| qwen3.5-4b | quick | Geslaagd | 15 | 41.84 s |
| qwen3.5-4b | stream | Geslaagd |  | 40.812 s |
| qwen3.5-4b | tools | Geslaagd |  | 54.999 s |
| qwen3.5-4b | vision | Geslaagd | 70 | 29.619 s |
| qwen3.5-4b | vision_context | Geslaagd | 65,635 | 87.496 s |
| qwen3.5-4b | vision_reverse | Geslaagd | 70 | 26.283 s |

## Hoe ik Hermes-geschiktheid testte

Ik plaatste een synthetische markering aan het begin van een lange prompt en vroeg het model om die na de opvultekst terug te geven. Het antwoord moest de verwachte waarde bevatten. De servergemelde invoertokens bepaalden de aanvraaggrootte. Een model dat normaal antwoordde na een grote prompt faalde alsnog wanneer de openingsmarkering onjuist was.

De reeks voor Qwen3.5 35B gebruikte genummerde opvulrecords, temperatuur 0 en oplopende lengtes van 3.800, 6.800, 10.000 en 13.600 records. Die stappen leverden 69.429, 124.179, 182.579 en 248.279 prompttokens op. Het model bleef tussen de stappen geladen, waardoor prefixhergebruik mogelijk was. De afzonderlijke controles van Qwen3.6 vlak bij de limiet meldden nul tokens uit de cache.

De lange prompt voor 0.8B herhaalde `river stone lantern orchard circuit velvet compass marble` 8.400 keer tussen een openingssleutel en een laatste terughaalvraag. De native run gebruikte `think:false`, `num_ctx:131072`, `stream:false` en `keep_alive:0`. De OpenAI-compatibele route gebruikte `reasoning_effort:"none"`. De broker dwong de modus zonder denken af, zodat gatewayclients geen instelling hoefden te wijzigen.

### Tool-, vision- en vrijgavecontroles

Tooltests controleerden zowel de aanvraag als het antwoord nadat het toolresultaat terugkwam. Een eenvoudige test gebruikte `add_numbers(7, 11)` en verwachtte 18. De test met Qwen3.5 35B gebruikte `lookup_square` en verwachtte 49. GPT-OSS deed een inventarisopvraag en moest het teruggegeven resultaat verwerken.

Visioncontroles gebruikten vragen over rode en blauwe afbeeldingen, omgekeerde beeldvolgorde en lange prompts met beeldkleuren plus begin- en eindmarkeringen. De test met Qwen3.5 35B gebruikte een rode PNG van 256 × 256. De broker had een reparatie voor beeldinhoudconversie nodig voordat deze aanvraag slaagde. De lange vision-test met 4B op systeem E vereiste dat beide markeringen en de kleurvolgorde behouden bleven.

Rond de lange runs controleerde ik GPU-geheugen, modelresidentie, temperaturen, hostgeheugendruk, OOM-gebeurtenissen en GPU-fouten. De bewaking voor Qwen3.5 35B controleerde ook het vrijgeven na een gecontroleerde onderbreking. Latere controles van clientannulering en aanvragen in de wachtrij testten het brokerpad. Twee aanvragen in de wachtrij bewijzen de afhandeling onder de geteste belasting, niet het bestaan van twee onafhankelijke gelijktijdige GPU-backends.

### De prestatieresultaten lezen

De aanvraagtijden omvatten het voorverwerken van lange invoer en het teruggegeven antwoord. Het zijn geen generatietokens per seconde. Bij streaming telt de vertraging tot de eerste inhoud. Reeksen met gecachte prefixen moet je apart interpreteren.

De geslaagde vervolgtests voor grotere modellen op systemen A en C gebruikten afzonderlijke inferentievensters waarin mining uitgeschakeld was. Na de aanvragen werden de modellen uit het geheugen gehaald. Mining werd op alle zeven systemen aan het einde van het testvenster hersteld. Deze resultaten beschrijven de modelservice tijdens een inferentievenster, niet gelijktijdig minen en infereren.

## Backendprofielen in de tests

Kies het profiel dat past bij de werklast die je wilt herhalen. Kwantisering, runtimecontext, cachetype, redeneermodus en GPU-plaatsing beïnvloeden het resultaat.

| Systeem en model | Getest backendprofiel |
|---|---|
| A, Qwen3.5 35B-A3B Q4_K_M | Ollama 0.34.2, f16 KV-cache, beide RTX 5060 Ti-kaarten van 16 GB, 64 GiB hostgeheugen en een runtimecontext van 262.144 voor de grote reeks. Native aanvragen gebruikten `think:false`, temperatuur 0, streaming en een keep-alive van vijf minuten tussen stappen. Gatewayaanvragen gebruikten de broker en LiteLLM. Geen limiet voor aanvraaguitvoer. |
| A, Qwen3.8 27B | llama.cpp op aanvraag via de broker en LiteLLM, runtimecontext 262.144, één inferentieslot, Q4 K/V-cache en beide RTX 5060 Ti-kaarten. De aanvraag met 66.007 tokens had geen uitvoerlimiet. |
| A, Qwen3.6-35B-A3B UD-Q4_K_XL | Strata 0.1.48, context 131.072, INT8 KV-cache, één geselecteerde GPU, geheugenlimiet van 55 GiB voor de procesgroep, runtimelimiet van 30 minuten, lazy loading en vrijgave na 60 seconden inactiviteit. Lang antwoord in de pilot: 217 uitvoertokens. Gatewayantwoord vlak bij de limiet: 11 uitvoertokens, zonder limiet voor aanvraaguitvoer. |
| A, Qwen3.8-Flash-Next UD-IQ4_XS | Strata 0.1.48, context 98.304, Q4 KV-cache, 8 GiB resident expertcache en beide RTX 5060 Ti-kaarten. Geheugenlimiet van de pilot: 52 GiB; latere route: 54 GiB. Lang antwoord in de pilot: 10 uitvoertokens. Eerdere combinaties met grotere context en cache stopten bij de geheugenlimieten. |
| A, Granite 4.2 8B | Q6_K GGUF-gewichten, gedeeld llama.cpp-werkproces, context 131.072, Q4_0 K/V-cache, `--n-predict -1`. De lange aanvraag gebruikte temperatuur 0, streaming en geen uitvoerlimiet. |
| A, DeepSeek Coder V2 16B | Q4_0 GGUF-gewichten, Ollama 0.34.2, twee RTX 5060 Ti-kaarten en 64 GiB hostgeheugen. Afzonderlijke cachetests met f16, Q4_0 en Q8_0 gebruikten de runtimecontexten uit de vergelijkingstabel. Geen limiet voor aanvraaguitvoer. |
| B, C, D, gecontroleerde Ollama-service | Ollama 0.34.2, context 131.072, parallelisme 1, één geladen model, wachtrijgrootte 128, keep-alive 0, Flash Attention en Q4_0 KV-cache. |
| B, Qwen3.5 9B-gatewaypilot | Time-out van de LiteLLM-route: 1.800 seconden; geen nieuwe pogingen en geen limiet voor context- of uitvoertokens. Beide markeringen bleven behouden bij 72.265 invoertokens. De afzonderlijke herstelcontrole voor mining slaagde. |
| C, Qwen3.5 0.8B | Q8_0-gewichten op één RTX 2000E Ada met een vermogensprofiel van 30 W. Runtimecontext 131.072. Native `think:false`, OpenAI-compatibele `reasoning_effort:"none"` en geen uitvoerlimiet. De brokeralias legde de runtimecontext vast en dwong de modus zonder denken af. |
| C, Gemma 4 12B-IT | Ollama-profiel met één GPU en runtimecontext 131.072; gestreamde en niet-gestreamde Aperture-aanvragen zonder uitvoerlimiet. De directe Aperture-run bereikte 75 °C en 30,64 W bij het ingestelde profiel van 30 W en werd daarna vrijgegeven. |
| D, Qwen3.5 9B, Gemma 4 12B-IT, GPT-OSS 20B | Exacte geïnstalleerde artefacten getest via Aperture met runtimecontext 131.072, volledige residentie op één GPU en natuurlijke voltooiing zonder limiet voor aanvraaguitvoer. |
| E, F, G, llama.cpp-chatprocessen | Build 11669, 99 GPU-lagen, parallelisme 1, Flash Attention, Q4_0 K/V-cache en `--n-predict -1`. De runtimecontext verschilde per modelfamilie. |

De opgenomen serviceprofielen beschrijven hun eigen runtimeconfiguratie. Het afzonderlijk geteste Qwen3.5 35B-profiel met f16-cache op systeem A erft niet de Q4_0-cache-instellingen van de kleinere Ollama-systemen.

### Modelvingerafdrukken voor de nieuwe runs met behouden invoer

Deze modelidentificaties onderscheiden de geteste artefacten van andere downloads of aliassen met vergelijkbare namen.

| Artefact | Kwantisering | Vastgelegde digest of SHA-256 van bestand |
|---|---|---|
| Qwen3.5 35B-A3B Ollama tag | Q4_K_M | `72aac7c28be8ff9b81c2a270eb489c88e6d822a76ec0cb7bf34d965768848567` |
| Qwen3.5 0.8B base Ollama tag | Q8_0 | `de63045f29755d4721c09d54c9b45c2dadb644f4fd7d604d4cac90d96049971c` |
| Granite 4.2 8B GGUF file | Q6_K | `5ad3d67f6fe09a448031029bead7f6a088697ca2787c0c5640bf964c59df1a21` |

Ollama-manifestdigests en SHA-256-waarden van gewichtbestanden identificeren verschillende objecten. Vergelijk de identificatie met het artefacttype in de tabel.

## Wat ik met Hermes zou gebruiken

Ik zou Qwen3.5 35B de hoofdroute voor hoge context maken op het systeem met twee RTX 5060 Ti-kaarten. De gatewaytest met 239.153 behouden tokens, aparte geslaagde tool- en vision-tests en geverifieerde vrijgave van aanvragen maken dit een betere keuze dan een model dat alleen een groot contextvenster adverteert. Ik houd Qwen3.8 27B beschikbaar voor het snellere antwoord bij 66K en Qwen3.6 wanneer één kaart belangrijk is.

Op systemen met de RTX 2000E Ada zou ik de geverifieerde Gemma 3 4B-route van systeem C kiezen voor de geteste werklast met lange invoer. De Qwen3.5 0.8B-route zonder denken zou ik uitproberen voor beperkte terughaal- en extractietaken. De grotere Gemma-, Qwen- en GPT-OSS-routes passen bij werk waarbij een eerste antwoord na vier tot vijf minuten acceptabel is. De mislukte Gemma 3-route op systeem D zou ik uitsluiten.

Voor RTX 3060 Ti- en RTX 3070-kaarten met 8 GB zou ik beginnen met Qwen3.5 2B of 4B. De tekstresultaten op 65K en de beeldcontroles voor 4B ondersteunen een bruikbare startconfiguratie zonder voor elke aanvraag de twee kaarten van 16 GB nodig te hebben. De geheugendruk van Flash Next en het onvolledige gedrag van DeepSeek Coder V2 bij 65K maken die modellen minder geschikte standaardkeuzes op de geteste profielen.

De tests ondersteunen deze keuzes van modellen en systemen voor specifieke werkwijzen. Behouden invoer, een correcte toolronde, beeldherkenning en nette vrijgave beantwoorden elk een ander deel van de Hermes-geschiktheid. Een betrouwbare configuratie moet de gedragingen ondersteunen die jouw agent gebruikt, met voldoende context voor het antwoord en toolverkeer.

## Bronnen en verwante informatie

- [Providerconfiguratie en contextvereisten van Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md)
- [Specificaties van NVIDIA GeForce RTX 3060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3060-3060ti/)
- [Specificaties van NVIDIA GeForce RTX 5060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/)
- [Overzicht van Hermes Agent](/hermes-local-ai-broker-course/01-hermes-agent-overview/)
- [Een lokale modelbackend kiezen](/hermes-local-ai-broker-course/02-choose-a-backend/)
