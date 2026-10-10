---
title: "Privacy van lokale AI: wat op je computer blijft en wat niet"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Breng prompts, modelbestanden, tools, logs, netwerkblootstelling en stroomkosten in kaart voordat je kiest voor lokale inferentie of een gehoste AI-dienst."
genre: ["Lokale AI", "Privacy", "Zelfgehoste AI", "Cybersecurity", "AI-economie"]
tags: ["privacy lokale AI", "lokale inferentie", "cloud AI", "AI-dataprivacy", "zelfgehoste AI", "LLM-privacy", "GPU-eigendomskosten", "AI-stroomkosten", "RTX 5070", "Claude Haiku 5.5", "Ollama-privacy", "llama.cpp", "AI-beveiliging", "offline AI", "lokale taalmodellen", "promptprivacy", "AI-dreigingsmodel", "GPU-rendabiliteit", "AI-datagrens", "private AI"]
cover: "/img/cover/local-ai-vs-chatgpt-comparison-illustration.webp"
coverAlt: "Een lokaal AI-werkstation verbonden met een cloudservice via zichtbare datapaden"
coverCaption: "Illustratie van lokale en gehoste AI-datapaden"
---

**Lokale AI geeft je een kleinere datagrens.** Een prompt die door een lokale runtime wordt verwerkt, blijft op je apparaat wanneer het model, de tools, de logs en het netwerkpad lokaal blijven. Een lokale GPU maakt van een computer geen afgesloten systeem.

Modelruntimes, toolplugins, browserextensies, externe toegang, blootgestelde API's en modeldownloads bepalen nog steeds je risico. Kosten tellen ook mee. Elektriciteit kan goedkoper zijn dan een gehoste tokenprijs, terwijl hardwarebezit het volledige omslagpunt ver naar de toekomst verschuift.

Deze gids brengt eerst de privacygrens in kaart. Daarna controleert hij de kosten met actuele leveranciersprijzen, een expliciete stroomaanname en de gerapporteerde cijfers uit de meegeleverde video.

<!--more-->

Deze kostenvergelijking tussen lokaal en gehost geeft context voor de onderstaande formules. Kopieer de doorvoercijfers niet zonder hetzelfde modelfile en dezelfde runtime op je hardware te testen.

{{< youtube id="DmkuFpoMYmc" enable="true" title="Is lokale AI de moeite waard? We vergeleken de kosten met Claude Haiku 5.5" description="Een kostenvergelijking van lokale en gehoste AI." >}}

De video meldt een runtime van 2 minuten en 31 seconden. Ik heb de titel en runtime via de kijkpagina gecontroleerd. Ik heb de hardwaretest niet herhaald, dus de gerapporteerde snelheden blijven metingen van de bron.

## Het korte antwoord

- **Kies lokale inferentie voor een gecontroleerd datapad.** Houd de modelserver op het apparaat, bind hem aan loopback en beperk toegang tot tools.
- **Kies gehoste inferentie voor incidenteel werk.** Vermijd hardware-uitgaven wanneer je werklast klein is of je gewenste model niet op je systeem past.
- **Behandel lokale kosten als twee getallen.** Splits elektriciteit per actief uur van hardwarebezit.
- **Behandel privacy als een systeemeigenschap.** Een privémodel verliest zijn voordeel wanneer een plugin bestanden uploadt of een lokale API op elke netwerkinterface luistert.

Lokale inferentie helpt wanneer gevoelige tekst binnen een werkstation of geïsoleerd netwerk moet blijven. Het helpt ook bij offline gebruik, een vaste modelversie of voorspelbare toegang zonder leveranciersquotum.

Deze voordelen bewijzen geen betere antwoorden. Een gehost model past misschien beter bij een taak, werkt sneller of vraagt minder onderhoud. Meet de werklast voordat je hardware koopt.

## Breng het datapad in kaart

Breng elk onderdeel van een verzoek in kaart. De modelnaam alleen laat niet zien waar gegevens heen gaan.

| Onderdeel | Privacyvraag | Te verzamelen bewijs |
|---|---|---|
| **Lokale modelserver** | Blijft de prompt op de host? | Procesconfiguratie, luisteradres en uitgaand verkeer |
| **Cloudmodel** | Welke tekst, bestanden en toolresultaten verlaten de host? | API-endpoint, voorwaarden van de leverancier, requestlogs en accountinstellingen |
| **Cloudmodus in een lokale app** | Draait het gekozen model op het apparaat? | Model-ID, leverancierslabel en netwerkverbinding |
| **Toolplugin** | Ontvangt het model bestanden, shell-uitvoer of browserinhoud? | Toollijst, rechten en vastgelegde requestgegevens |
| **Modeldownload** | Welke code en gewichten komen op de host? | Bronrepository, licentie, release-checksum en downloadpad |
| **Lokale logs** | Waar blijven prompts en toolresultaten bewaard? | Runtimelogs, shellgeschiedenis, crashrapporten en back-upbereik |

**Een lokaal model haalt één leverancier uit het promptpad.** Je moet de rest van het pad nog steeds controleren.

## Lokaal betekent niet standaard privé

[Het privacybeleid van Ollama](https://ollama.com/privacy) stelt dat Ollama prompts of gegevens niet ziet wanneer een model lokaal draait. Het beleid scheidt lokaal gebruik ook van cloudmodellen. Een cloudmodel vormt nog steeds een servicegrens, ook wanneer dezelfde toepassing beide modi start.

[De serverdocumentatie van llama.cpp](https://github.com/ggml-org/llama.cpp/tree/master/tools/server) toont een lokale server die standaard op `127.0.0.1:8080` luistert. De Dockervoorbeelden tonen ook `--host 0.0.0.0`, wat de dienst op alle interfaces blootstelt. Een breder bindadres verandert de toegangsgrens.

Controleer het luisteradres voordat je gevoelige tekst verstuurt:

```bash
lsof -nP -iTCP -sTCP:LISTEN | rg 'ollama|llama|8080|11434'
```

`127.0.0.1` of `localhost` beperkt toegang normaal gesproken tot dezelfde host. Een LAN-adres of `0.0.0.0` vraagt om een firewallregel en een authenticatieplan. Stel een modelendpoint niet bloot aan een netwerk voordat je beide hebt getest.

Controleer ook de naam van het gekozen model. De cloud-documentatie van Ollama beschrijft cloudmodellen als een afzonderlijk servicepad. Een lokale interface bewijst geen lokale uitvoering.

De [FAQ van Ollama](https://docs.ollama.com/faq) beschrijft een modus die alleen lokaal werkt. Stel `disable_ollama_cloud` in `~/.ollama/server.json` in, of stel `OLLAMA_NO_CLOUD=1` in voordat je de dienst herstart. Dit verwijdert Ollama-cloudmodellen en webzoekopdrachten uit de gekozen runtime. Het beperkt andere toepassingen, browsertools, plugins of netwerktoegang op de host niet.

```json
{
  "disable_ollama_cloud": true
}
```

Controleer de instelling na de herstart. Een lokale runtime verkleint één pad. Hij maakt geen private host.

## Bereken de gehoste kosten

Tokenprijzen splitsen input en output. [Anthropic vermeldt Claude Haiku 5.5 voor $0,10 per miljoen inputtokens en $0,50 per miljoen outputtokens voor prompts tot 100.000 tokens](https://www.anthropic.com/claude/haiku). Prompts boven 100.000 tokens gebruiken de hogere vermelde tarieven.

[De tokenhandleiding van OpenAI](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens) legt uit waarom een woordtelling niet gelijk is aan een tokentelling. De handleiding scheidt ook input-, output-, gecachte input- en redeneertokens. Gebruik de gebruiksvelden van je leverancier in plaats van een schatting op basis van woorden.

Gebruik voor een eenvoudige vergelijking één miljoen gegenereerde tokens en één miljoen inputtokens als afzonderlijke werklasten. Een codeeragent verstuurt vaak herhaalde context en produceert een kleiner antwoord, dus één gecombineerd tokengetal verbergt de kostenmix.

## Bereken lokaal stroomverbruik

[NVIDIA's lanceringsaankondiging van de RTX 5070](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/) vermeldde een startprijs van $549. [De NVIDIA-pagina voor de RTX 5070-familie](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/) vermeldt 12 GB geheugen en 250 W totaal grafisch vermogen voor het Founders Edition-referentieontwerp. De productpagina van NVIDIA vermeldt nog steeds $549 en toonde de kaart tijdens deze controle als niet op voorraad.

Het GPU-vermogenscijfer is niet het vermogen van het hele systeem. Gebruik een energiemeter voor je pc. Het voorbeeld hieronder neemt **400 W totaal systeemverbruik** aan, inclusief GPU, processor, geheugen, opslag, ventilatoren en verliezen van de voeding. Dit is een aanname voor de berekening, geen meting.

[De prognose van de U.S. Energy Information Administration](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os) gebruikte 18,2 cent per kilowattuur als gemiddelde residentiële elektriciteitsprijs voor 2026. Je stroomtarief verandert de uitkomst.

Gebruik deze formule voor gegenereerde output:

```text
local cost per 1M output tokens =
(whole_system_watts / 1,000)
× (1,000,000 / output_tokens_per_second / 3,600)
× electricity_price_per_kWh
```

Bij 400 W en $0,182 per kilowattuur kost het systeem $0,0728 per actief uur.

| Outputsnelheid | Tijd voor 1M tokens | Stroomkosten voor 1M tokens |
|---:|---:|---:|
| **20 tokens per seconde** | 13 uur 53 minuten | **$1,01** |
| **50 tokens per seconde** | 5 uur 33 minuten | **$0,40** |
| **94 tokens per seconde** | 2 uur 57 minuten | **$0,22** |

Bij 50 outputtokens per seconde kost lokale stroom minder dan Haiku 5.5's outputprijs van $0,50. Bij 20 outputtokens per seconde kost lokale stroom meer. De drempel voor outputsnelheid ligt onder deze aannames rond 40 tokens per seconde.

De inputberekening gebruikt dezelfde formule. Bij 2.650 inputtokens per seconde duurt één miljoen inputtokens ongeveer 6 minuten en 17 seconden en kost het ongeveer $0,008 aan stroom. Bij 1.000 inputtokens per seconde kost hetzelfde werk ongeveer $0,020.

Het meegeleverde transcript meldt 94 outputtokens per seconde en 2.650 inputtokens per seconde voor het RTX 5070-voorbeeld. De berekening hierboven komt onder de aanname van 400 W met die cijfers overeen. Het transcript bevat geen onafhankelijk labrapport, hash van het modelfile, runtime-build, prompt of meting met een energiemeter. Behandel deze snelheden als referentieresultaat, niet als aankoopgarantie.

## Hardware verandert het omslagpunt

Stroombesparing betaalt hardware niet vanzelf terug. Vergelijk de volledige aankoop met het verschil tussen gehoste outputkosten en lokale variabele kosten.

Bij 50 outputtokens per seconde:

```text
$0.50 hosted output price - $0.40 local power = $0.10 saved per 1M tokens
$549 GPU price / $0.10 = about 5.5 billion output tokens
```

Bij 94 outputtokens per seconde stijgt de afgeronde besparing naar ongeveer $0,28 per miljoen tokens. Een GPU van $549 terugverdienen vraagt dan ongeveer 2 miljard outputtokens. Beide cijfers sluiten systeemgeheugen, opslag, moederbord, voeding, koeling, onderhoud en restwaarde uit.

De lanceringsprijs is geen universele aankoopofferte. De huidige NVIDIA-pagina toonde de officiële prijs zonder voorraad. Een aanbieding van $819 vraagt aparte controle voordat je die in een omslagpuntmodel zet. Gebruik je echte factuur en je gemeten vermogen aan de muur.

**Bestaande hardware verandert de beslissing.** Als je werkstation al genoeg geheugen en een geschikte GPU heeft, zijn de hardwarekosten voor de volgende taak al gemaakt. Vergelijk stroom, tijd, kwaliteit, privacy en onderhoud. Als je een volledig systeem moet kopen, vergelijk dan het volledige systeem met gehost gebruik.

Lees voor details over modelgeschiktheid de [gids voor lokale AI-modellen en GPU-context](/articles/local-ai-model-gpu-context-guide/) en de [gids voor 16 GB VRAM-dimensionering](/articles/is-16gb-vram-enough-local-llm/). Lees voor een gerapporteerde lokale codeeragentconfiguratie de [Strata- en OpenCode-gids](/articles/strata-opencode-local-coding-agent-16gb/).

## Wat lokale privacy je geeft

- **Een korter datapad:** de prompt hoeft geen modelleverancier te bereiken wanneer inferentie lokaal blijft.
- **Offline gebruik:** een gedownload model en lokale runtime hebben geen actieve leveranciersverbinding nodig voor tekstgeneratie.
- **Versiebeheer:** je kiest het modelfile en de runtimeversie in plaats van een automatische leverancierswijziging te ontvangen.
- **Gebruikcontrole:** lokale inferentie vermijdt een cloudmeter per verzoek nadat hardwarebezit en stroom zijn meegerekend.
- **Controle over netwerkbeleid:** je firewall en hostcontroles bepalen wie het modelendpoint bereikt.

Deze voordelen tellen vooral voor broncode, klantgegevens, niet-uitgebrachte ontwerpen, privénotities en werk in een losgekoppelde omgeving. Lokale inferentie vraagt nog steeds om schijfversleuteling, hostupdates, accountscheiding en beperkte tools.

## Wat lokale privacy je niet geeft

- **Een kwaliteitsgarantie:** kleinere of gekwantiseerde modellen moeten worden getest aan de hand van je echte acceptatiecriteria.
- **Een toeleveringsgarantie:** modelfiles, runtimes, plugins en containerimages vragen om betrouwbare bronnen en integriteitscontroles.
- **Een schone host:** malware, browserextensies, back-ups, crashreporters en beheer op afstand zien nog steeds hostgegevens.
- **Een veilig netwerkendpoint:** een server die aan elke interface is gebonden, maakt een nieuwe dienst die je moet verdedigen.
- **Een gratis systeem:** elektriciteit, opslag, koeling, hardware-slijtage en onderhoud hebben nog steeds kosten.

De [Strata-gids voor lokale codeeragents](/articles/strata-opencode-local-coding-agent-16gb/) laat zien waarom systeemgeheugen, context, tooltoegang en runtime-instellingen bij de evaluatie horen. GPU-geheugen alleen bepaalt de privacy- of prestatiegrens niet.

## Kies de juiste grens

| Situatie | Beste eerste keuze | Reden |
|---|---|---|
| **Gevoelige documenten en een bestaande geschikte pc** | Lokale inferentie | Houd prompts binnen een beheerde host en vermijd nieuwe hardware-uitgaven |
| **Incidenteel algemeen schrijven** | Gehoste API of chatdienst | Betaal voor de kleine werklast en vermijd onderhoud |
| **Een frontiermodel of gespecialiseerde cloudtool** | Gehoste dienst | Het vereiste model of de vereiste tool is niet op de lokale host beschikbaar |
| **Groot terugkerend volume met een gecontroleerd lokaal model** | Lokaal of hybride | Vergelijk stroom, kwaliteit, supporttijd en leveranciersprijzen |
| **Gemengde werklasten** | Hybride routing | Houd gevoelige taken lokaal en stuur goedgekeurde algemene taken naar een gehost model |

**Hybride routing vraagt om een expliciete classificatieregel.** Markeer gegevens als alleen lokaal, goedgekeurd voor gehoste verwerking of verboden tot beoordeling. Vertrouw niet op een modelnaam of toepassingspictogram om de regel af te dwingen.

## Controleer voordat je vertrouwt

1. **Benoem het modelpad.** Noteer model-ID, runtime, versie en downloadbron.
2. **Controleer het bindadres.** Bevestig dat de server op loopback luistert, tenzij een breder pad een gedocumenteerde reden heeft.
3. **Noteer elke tool.** Controleer toegang tot bestanden, shell, browser, netwerk en plugins.
4. **Controleer persistentie.** Vind promptlogs, tooluitvoer, crashrapporten, back-ups en gedeelde modelmappen.
5. **Test netwerkgedrag.** Observeer verbindingen tijdens een gevoelige test met een representatieve prompt.
6. **Meet het systeem.** Noteer vermogen aan de muur, output- en inputsnelheid, contextlengte en nieuwe pogingen.
7. **Test geaccepteerd werk.** Vergelijk voltooide taken en reviewinspanning, niet alleen tokens per seconde.

De [gids voor lokale AI versus ChatGPT](/articles/local-ai-vs-chatgpt-how-close-are-we/) behandelt afwegingen rond modelmogelijkheden. Gebruik deze privacychecklist naast de kwaliteitstest.

## Referenties

- [Video, Is lokale AI de moeite waard? We vergeleken de kosten met Claude Haiku 5.5](https://www.youtube.com/watch?v=DmkuFpoMYmc)
- [Lanceringsaankondiging NVIDIA Blackwell GeForce RTX 50 Series](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/)
- [Specificaties NVIDIA GeForce RTX 5070-familie](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/)
- [Productpagina NVIDIA GeForce RTX 5070](https://marketplace.nvidia.com/en-us/consumer/graphics-cards/geforce-rtx-5070/)
- [U.S. Energy Information Administration, Short-Term Energy Outlook van oktober 2026](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os)
- [Anthropic Claude Haiku 5.5](https://www.anthropic.com/claude/haiku)
- [Prijzen van het Anthropic Claude-platform](https://platform.claude.com/docs/en/about-claude/pricing)
- [OpenAI, Tokens begrijpen en tellen](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens)
- [Privacybeleid van Ollama](https://ollama.com/privacy)
- [Serverdocumentatie van llama.cpp](https://github.com/ggml-org/llama.cpp/tree/master/tools/server)
