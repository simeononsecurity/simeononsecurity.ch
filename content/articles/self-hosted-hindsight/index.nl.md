---
title: "Zelfgehoste Hindsight: lokaal agentgeheugen en privé modelroutering"
date: 2026-11-08
lastmod: 2026-11-12
toc: true
draft: false
description: "Een casestudy van zelfgehoste Hindsight, waargenomen lokale Qwen-routes en GPU-werk per aanvraag zonder gehost inferentieabonnement op de onderzochte paden."
genre: ["Lokale AI", "Zelfgehoste AI", "AI-agenten", "AI-infrastructuur", "Privacy"]
tags: ["Hindsight", "zelfgehoste Hindsight", "agentgeheugen", "lokale AI", "lokale LLM", "Qwen3.5", "LiteLLM", "privé-VPN", "modelgateway", "embeddings", "reranking", "GPU-planning", "privé-inferentie", "Docker", "geheugenbanken", "kennispagina's", "lokale modelroutering"]
cover: "/img/cover/self-hosted-hindsight-local-model-routing.webp"
coverAlt: "Een abstracte privégeheugendienst routeert werk naar lokale CPU- en GPU-modelservers"
coverCaption: "Geheugenopslag, ophalen en de onderzochte modelroutes draaien op eigen hardware"
---

**Onze Hindsight-geheugendienst draait op hardware die we zelf beheren.** De geheugenengine, database, embeddingmodel en reranker draaien in één zelfgehoste installatie. Hindsight verstuurt generatieverzoeken naar een privégateway. De onderzochte gedeelde Qwen-backend en de geteste route voor het vernieuwen van pagina's gebruiken lokale modelservers zonder gehost inferentieabonnement.

Dit beschrijft één werkende installatie. **Zelfgehost betekent niet offline.** De VPN gebruikt een externe coördinatiedienst, en software-images en modelgewichten moeten worden gedownload. De claim hier gaat over geheugenverwerking en modelinferentie, niet over elke netwerkverbinding van onze apparaten of andere agenttools.

<!--more-->

## Belangrijkste punten

- **Hindsight beheert de geheugenworkflow.** Een Docker-container levert de API, workers en het control plane, met bankgegevens op een persistent volume.
- **Kleine ophaalmodellen blijven lokaal.** Embeddings en reranking draaien binnen het Hindsight-proces op de CPU.
- **Qwen genereert tekst.** Retain, Reflect en consolidatie vragen de privéalias Qwen3.5-4B aan, met redeneren uitgeschakeld en begrensde uitvoer. De onderzochte backend serveert lokaal.
- **Lange paginavernieuwingen krijgen een GPU.** Een aparte modelalias reserveert één kaart voor een achtergrondverzoek en geeft de kaart daarna weer vrij.
- **De gateway verbergt de fysieke plaatsing.** Hindsight kiest een modelalias. Privéroutingdiensten kiezen een serveerendpoint.

## Bepaal de grens voordat je modellen kiest

**Hindsight is de geheugenengine, niet de modelserver.** De volledige Docker-image bevat lokale embedding- en rerankingmodellen, maar voor taalmodelgeneratie is een endpoint nodig. De [installatiehandleiding van Hindsight](https://hindsight.vectorize.io/developer/installation) beschrijft deze scheiding en noemt lokale llama.cpp-, Ollama- en vLLM-servers als alternatieven voor gehoste aanbieders.

**De geheugen-API blijft op het privénetwerk.** Het webcontrol plane blijft op een lokale interface. Een persistent volume bevat de ingebedde database, zodat het opnieuw aanmaken van een container de banken niet verwijdert. Authenticatie beschermt de API en afzonderlijke banken ordenen projectcontext.

**De generatiegateway levert stabiele modelnamen.** Hindsight verstuurt OpenAI-compatibele verzoeken via de privégateway over een VPN. De gateway stuurt verzoeken door naar lokale serveerendpoints. De onderzochte Qwen-route bereikt een LiteLLM-installatie die aan een lokale CPU-server is gekoppeld. [De routerdocumentatie van LiteLLM](https://docs.litellm.ai/docs/routing) beschrijft dit patroon met modelaliassen. Een gelijkwaardige OpenAI-compatibele router vervult dezelfde rol.

{{< figure src="hindsight-private-request-path.webp" alt="Diagram met agents, een privé-Hindsight-dienst, lokale ophaalmodellen, een privégateway en lokale Qwen-servers" caption="Het diagram laat hostnamen, adressen, toegangssleutels en fysieke hostlabels weg" >}}

[Open het diagram van het volledige verzoekpad](hindsight-private-request-path.webp).

**Er bestaat nog steeds een interne API.** Hindsight roept een privégateway aan met het OpenAI-compatibele formaat. De onderzochte modelroutes voeren inferentie lokaal uit. We hebben niet elke terugvalregel van de gateway gecontroleerd. Beoordeel daarom het gatewaybeleid voordat je lokale verwerking als garantie voor elk verzoek beschouwt.

## Wijs elke geheugentaak toe aan de juiste rekenkracht

De bewerkingen van Hindsight doen verschillend werk. **Retain** haalt feiten uit nieuw materiaal. **Recall** vindt relevante herinneringen. **Reflect** zoekt en schrijft een samengesteld antwoord. **Consolidation** voegt verwante feiten samen. Een achtergrondtaak **knowledge-page refresh** bouwt een actuele samenvatting van de bank opnieuw op.

| Bewerking | Modelplaatsing | Reden |
| --- | --- | --- |
| **Retain** | Qwen3.5-4B via de privégateway | Lokale gestructureerde extractie met een begrensd uitvoerbudget |
| **Recall** | Lokale CPU-embedding en reranking | Zoeken vereist geen generatie-API-aanroep |
| **Reflect** | Qwen3.5-4B via de privégateway | Synthese vereist generatie na het ophalen van herinneringen |
| **Consolidation** | Qwen3.5-4B via de privégateway | Kleine batches beperken lange gestructureerde antwoorden |
| **Knowledge-page refresh** | Aparte lokale GPU-Qwen-route | Grote achtergrondsynthetisering overschreed de tijdslimiet van de CPU-route |

*Houd kleine ophaaltaken op de CPU en reserveer GPU-inferentie voor gemeten langlopende taken.*

De Hindsight-container laadt **BAAI/bge-small-en-v1.5** voor embeddings en **hindsight-ai/hs-rerank-1** voor reranking. Opstartlogboeken bevestigen dat beide lokaal op de CPU draaien. De [modelreferentie van Hindsight](https://hindsight.vectorize.io/developer/models) beschrijft lokale modelopties en het optionele pad voor een beslismodel.

We behielden het bestaande embeddingmodel omdat een wijziging van de embeddingruimte vereist dat opgeslagen vectoren opnieuw worden opgebouwd. De reranker draait al lokaal, dus een gehoste rerankingdienst zou een nieuwe grens voor gegevensverwerking toevoegen zonder de waargenomen generatietime-out op te lossen. Een lokale proef met **hs-decide-1-flash** leverde één correct Reflect-antwoord op, maar de test liep bijna tegen de tijdslimiet aan. De synthetische consolidatiegegevens oefenden het beslispad niet. Daarom maakt het beslismodel geen deel uit van de productieroutering.

## Geef traag achtergrondwerk een GPU

**De gewone modelnaam verschilt van de modelnaam voor vernieuwen.** Retain, Reflect en consolidatie gebruiken de gedeelde Qwen-alias. Het vernieuwen van achtergrondpagina's gebruikt een knooppuntspecifieke GPU-alias met één gelijktijdige taalmodelaanroep. Zo blijft een lange onderhoudstaak beperkt tot één GPU tegelijk.

**Een reservering per verzoek beperkt het GPU-gebruik.** De GPU-pool start een modelworker zodra een verzoek binnenkomt. De controller reserveert één kaart, verwerkt het verzoek, stopt de worker en geeft de reservering vrij. Het diagram laat de fysieke hostinventaris weg.

{{< figure src="hindsight-gpu-lease-cycle.webp" alt="Diagram waarop één GPU wordt gereserveerd voor het vernieuwen van een achtergrondpagina en na voltooiing van het verzoek wordt vrijgegeven" caption="Een lease per verzoek reserveert één GPU voor het vernieuwen van een pagina" >}}

[Open het diagram van de volledige GPU-leasecyclus](hindsight-gpu-lease-cycle.webp).

Deze scheiding kwam voort uit een gemeten mislukking. **Eén paginavernieuwing met prioriteit voor de CPU bereikte de limiet van één uur.** Nadat we achtergrondvernieuwingen naar de lokale GPU-pool hadden gerouteerd, werden vijf eerder mislukte pagina's in één herstelrun in ongeveer twee tot zes minuten voltooid. Deze cijfers beschrijven die pagina's en instellingen. Ze vormen geen algemene Qwen-doorvoerbenchmark.

## Herstel standaardwaarden en time-outs

**De eerdere uitvoerlimieten van Hindsight pasten niet bij onze lokale router.** De router accepteert maximaal 8.192 uitvoertokens en hanteert een limiet van 256 tokens wanneer een verzoek er geen opgeeft. Een eerdere Retain-limiet van 64.000 tokens leidde tot HTTP 400. Consolidatiebatches met acht feiten stopten omdat de uitvoerlengte was bereikt, en Reflect had een expliciete limiet nodig om de terugval van 256 tokens van de router te vermijden.

**We maakten de limieten voor elke taak expliciet.** Qwen-redeneren staat uit voor deze geheugenbewerkingen. Hindsight staat nu in totaal vier gelijktijdige LLM-aanroepen toe, met maximaal één aanroep voor het vernieuwen van achtergrondpagina's. De globale LLM-time-out is 1.800 seconden, met één nieuwe poging voor het model.

| Werklast | Uitvoer- of batchlimiet | Limieten voor aanroepen en bewerkingen |
| --- | --- | --- |
| **Retain** | 8.192 uitvoertokens | Globale time-out van 1.800 seconden per aanroep |
| **Reflect** | 4.096 uitvoertokens | 900 seconden per aanroep, 3.600 seconden totale bewerkingstijd |
| **Consolidation** | 4.096 uitvoertokens, vier feiten per aanroep | 900 seconden per aanroep, 14.400 seconden totale bewerkingstijd |
| **Page refresh** | Eén gelijktijdige modelaanroep | 900 seconden per aanroep, aparte GPU-route |

*Deze waarden beschrijven onze lokale router en installatie van november 2026.*

**Een time-out voor een aanroep en een totale bewerkingstijd begrenzen verschillende fasen.** Sommige geldige Qwen-aanroepen overschreden de eerdere time-out van 300 seconden. De langere totale bewerkingstijden laten werk met meerdere aanroepen toe, terwijl de limieten van 900 seconden per aanroep elke poging begrenzen.

In de herstelrun werden meerdere Retain-taken voltooid met **1.042 tot 2.076 uitvoertokens**. Twee consolidatieruns voltooiden respectievelijk **41 van 41** en **30 van 30** items. Een latere overschrijding van de tijdslimiet voor het vernieuwen van pagina's leidde tot de hierboven beschreven aparte GPU-route. Deze herstelresultaten bewijzen geen betrouwbaarheid op lange termijn.

## Welke compromissen brengt het ontwerp mee?

**Geen rekening voor gehoste modellen betekent niet dat er geen kosten zijn.** De installatie gebruikt eigen hardware, elektriciteit, opslag, onderhoudstijd en GPU-tijd tijdens het vernieuwen van pagina's. Elke plaatsingskeuze ruilt capaciteit in tegen latentie of operationele eenvoud.

| Keuze | Voordeel | Compromis |
| --- | --- | --- |
| **Generatie met prioriteit voor de CPU** | Houdt GPU-capaciteit beschikbaar | Een geteste paginavernieuwing bereikte de limiet van één uur |
| **Paginavernieuwing op de GPU** | Vijf pagina's waren in één run in ongeveer twee tot zes minuten klaar | Gebruikt GPU-capaciteit en is afhankelijk van de aparte route |
| **Ingebedde database** | Houdt de installatie compact | Beperkt het storingsdomein en vereist geteste back-ups |

*Gebruik een GPU-route voor vernieuwen nadat gemeten CPU-latentie je onderhoudsvenster overschrijdt.*

De [installatiehandleiding van Hindsight](https://hindsight.vectorize.io/developer/installation) adviseert voor grotere productie-installaties een aparte PostgreSQL-database. **Onze ingebedde database vereist een geteste back-up- en herstelprocedure** naarmate de bank groeit.

**Privé-inferentie geldt voor een pad.** Controleer de geselecteerde Hindsight-provider, de modelkoppeling van de gateway, terugvalregels, het lokale modelproces, logbewaring en uitgaand netwerkverkeer. De trace-ID's van Hindsight helpen verzoeken te koppelen en Docker roteert de containerlogboeken. Geen van beide bewijst dat een vervolgverzoek lokaal bleef. Een gateway-audit levert het ontbrekende end-to-endbewijs.

## Aanbeveling

**Begin met lokale ophaalmodellen en expliciete generatielimieten.** Plaats Hindsight en de embedding- en rerankingmodellen op eigen hardware. Routeer generatie via een privé OpenAI-compatibele gateway over een VPN. Meet elke bewerking voordat je CPU- of GPU-capaciteit toewijst en reserveer de GPU-route voor achtergrondtaken waarvan de CPU-latentie je onderhoudsvenster overschrijdt.

*Controleer elke terugvalregel van de gateway en test bankherstel voordat je de installatie privé en veerkrachtig noemt.* De [gids over de privacygrens van lokale AI](/articles/local-ai-privacy-boundary/) biedt een beginchecklist.

## Conclusie

**Deze installatie houdt Hindsight-geheugen en de onderzochte inferentiepaden op eigen hardware zonder gehost inferentieabonnement.** CPU-ophalen, begrensde Qwen-aanroepen en een GPU-route met één aanroep voor paginavernieuwing bedienen verschillende werklasten. De herstelruns voltooiden Retain-, consolidatie- en paginavernieuwingstaken onder deze instellingen. Een volledige audit van gateway-terugvalregels, een back-uptest en langere betrouwbaarheidsobservatie zijn de volgende controles.
