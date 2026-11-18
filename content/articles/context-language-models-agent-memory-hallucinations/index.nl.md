---
title: "Meta’s Context Language Models: beter agentgeheugen, geen einde aan hallucinaties"
date: 2026-10-06
lastmod: 2026-11-14
toc: true
draft: false
description: "Hoe Context Language Models agentgeheugen bewerken, wat benchmarks aantonen en hoe cachekosten, modelcapaciteit en onbetrouwbare notities de betrouwbaarheid beïnvloeden."
genre: ["Kunstmatige intelligentie", "AI-agenten", "Lokale AI", "AI-beveiliging"]
tags: ["Context Language Models", "CLM", "Meta AI", "AI-hallucinaties", "agentgeheugen", "contextbeheer", "contextcompressie", "contextvenster", "Suffix Cache Reuse", "KV-cache", "SGLang", "llama.cpp", "promptcaching", "promptinjectie", "BrowseComp-Plus", "ContextBench", "EdgeBench", "Qwen3.6", "langlopende agenten", "AI-betrouwbaarheid", "agentverificatie"]
cover: "/img/cover/context-language-models-editable-memory.webp"
coverAlt: "Een lichtgevende processor naast herschikte doorschijnende documentkaarten en een aparte archiefstapel op een donker oppervlak"
coverCaption: "Conceptuele illustratie van bewerkbaar agentgeheugen."
---

**Context Language Models (CLM’s)** geven een AI-agent directe controle over de informatie voor de volgende modelaanroep. De aanpak verbetert contextbeheer in meerdere gepubliceerde evaluaties, maar toont niet aan dat hallucinaties verdwijnen. Een agent heeft nog steeds bewijs nodig voor beweringen en onafhankelijke controles van het werk.

De technische vraag is of selectieve bewerking de juiste feiten bewaart tegen aanvaardbare kosten. Een korter gesprek is alleen nuttig als de agent de vereisten onthoudt, waarnemingen van aannames onderscheidt en zo nodig ondersteunend bewijs ophaalt.

<!--more-->

## Belangrijkste punten

- **Bewerkbare context:** CLM beschrijft een uitvoeringsmethode voor bestaande modellen, met optionele training om het gebruik ervan te verbeteren.
- **Voorwaardelijke winst:** modelgrootte, contextbudget, taak en serving-backend beïnvloeden de resultaten.
- **Rekenkosten:** FLOPs voor prefixhergebruik omvatten herberekening na bewerkingen, maar meten niet rechtstreeks verstreken tijd of facturering.
- **Geheugenintegriteit:** de eigen notities van een agent blijven feilbaar en mogelijk onveilige invoer.
- **Praktische evaluatie:** meet geaccepteerde resultaten, verloren feiten, onbewezen claims en herstelkosten samen.

## Scheid geheugen van bewijs

**Een contextvenster** bevat de invoer die tijdens een aanroep beschikbaar is voor het model. Instructies, toolantwoorden, werkaantekeningen en eerdere berichten concurreren om ruimte. Compactie vervangt een deel van dit materiaal door een kortere weergave.

Neem een **illustratieve taak voor een afhankelijkheidsupgrade**. Een testrunner meldt twee fouten. De agent vat de geschiedenis samen in een notitie waarin staat dat de upgrade is geslaagd. Toekomstig werk begint dan vanuit een verkeerde aanname, hoewel de oorspronkelijke testuitvoer nog op schijf staat.

Een andere compactiemethode verandert hoe deze onjuiste notitie in het werkgeheugen terechtkomt. De methode vervangt de **testrunner als bewijs** niet. Voordat je de upgrade accepteert, heeft de workflow nog steeds een nieuwe testuitkomst of een controleerbaar verslag van de relevante uitvoering nodig.

| Fout | Geschikte controle |
|---|---|
| **Verloren vereiste** | Vergelijk de huidige staat met de oorspronkelijke acceptatiecriteria |
| **Verzonnen waarneming** | Koppel de claim aan een toolresultaat of bronregistratie |
| **Onjuiste redenering** | Toets de conclusie aan het verwachte gedrag van de taak |
| **Onbevoegde instructie** | Handhaaf machtigingen buiten door het model geschreven notities |

Dit onderscheid is belangrijk bij de evaluatie van elke geheugentechniek. **Behoud en juistheid zijn afzonderlijke eigenschappen.** Een systeem dat een onjuiste bewering perfect bewaart, blijft onjuist.

## Wat CLM’s veranderen

**Rulin Shao en mede-auteurs**, onder wie onderzoekers van Meta Superintelligence Labs en de University of Washington, introduceerden CLM’s in een preprint van 29 september 2026. Hun implementatie stelt de actieve context beschikbaar als bewerkbaar bestand. De agent wijzigt het met shellopdrachten of code, waarna de runtime de aangepaste inhoud bij de volgende aanroep gebruikt. Zie [Context Language Models](https://arxiv.org/abs/2609.37725).

```text
Gewone voortzetting:
bestaande context + nieuw antwoord + nieuwe uitvoer van de tool

Voortzetting met bewerkbare context:
agent herziet contextbestand -> runtime laadt herziene context -> volgende modelaanroep
```

Voor de zero-shot-aanpak hoeft **de modelarchitectuur niet te worden vervangen**. De runtime voegt een mogelijkheid toe rond een bestaand model. De paper onderzoekt daarnaast instructies, aangeleerde strategieën voor contextbeheer en reinforcement learning.

Een **notitiebestand** werkt anders. Een opgeslagen notitie lezen voegt de inhoud toe aan een gesprek. Het bestand later bewerken verwijdert de oude tekst niet automatisch uit de actieve context. CLM vereist runtimesupport om bewerkingen met volgende verzoeken te synchroniseren. De [officiële implementatie](https://github.com/facebookresearch/context-language-models) bevat de agentcode en een afzonderlijke servingextensie.

**Externe opslag blijft nuttig.** Houd gedetailleerde logs en brondocumenten beschikbaar voor ophalen en bewaar beknopte verwijzingen in het werkgeheugen. De locatie van een document en de claim die het ondersteunt zijn vaak belangrijker dan elke regel in de volgende prompt bewaren.

## Lees de resultaten zorgvuldig

**Benchmarkverbeteringen zijn specifieke vergelijkingen.** De volgende bevindingen komen uit evaluaties van de auteurs, niet uit tests voor dit artikel. Het onderzoek is nog een preprint. Resultaten van een gekozen benchmark bewijzen geen betrouwbaarheid in willekeurige workflows.

| Evaluatie | Gerapporteerd resultaat | Interpretatie |
|---|---|---|
| **BrowseComp-Plus, zero-shot** | 11,4% relatieve nauwkeurigheidswinst en 21,5% minder FLOPs voor prefixhergebruik dan de sterkste baseline | Nauwkeurigheid en rekenwerk verbeteren beide in deze opstelling |
| **TerminalBench 2.1** | Even nauwkeurig als de sterkste baseline met 29,5% minder FLOPs | Het voordeel is efficiëntie bij vergelijkbare nauwkeurigheid |
| **EdgeBench, runs van 12 uur** | 5% hogere score met 59% minder FLOPs | Score voor software-optimalisatie, geen hallucinatiepercentage |
| **Getrainde Qwen3.5-9B** | CLM 42,5% tegenover 42,1% nauwkeurigheid met getrainde samenvatting | Klein nauwkeurigheidsverschil met groter verschil in rekenwerk |

De getrainde 9B-vergelijking gebruikt **1,34 tegenover 2,19 PFLOPs per vraag**, ongeveer 38,8% minder rekenwerk voor CLM. De verbetering van 28,8% vóór training naar 42,5% erna is een andere vergelijking dan het verschil van 0,4 procentpunt met getrainde samenvatting. Houd de baseline expliciet. Zie de [resultaten- en trainingstabel van de paper](https://arxiv.org/html/2609.37725v1).

Ook **relatieve percentages** hebben een noemer nodig. Een stijging van ongeveer 53,3% naar 59,4% is circa 6,1 procentpunt of 11,4% relatief. Geen van beide formuleringen betekent dat het systeem elke vraag correct beantwoordt.

### Contextbudget verandert uitkomsten

Een **contextbudget van 32K** komt in de hoofdevaluaties terug. Dit beperkt zinvol wat kan worden behouden en bewerkt. Generaliseer resultaten bij dit budget niet naar elke implementatie met een groter venster.

Bij **128K op EdgeBench-10** rapporteert bijlage F de volgende resultaten over tien taken en drie seeds:

| Methode | Eindscore | Gemiddelde PFLOPs voor prefixhergebruik per proef |
|---|---|---|
| **Samenvatting** | 47,8 | 222 |
| **CLM** | 47,3 | 142 |
| **CLM met subagents** | 50,2 | 219 |

**De nauwkeurigheid van één agent ligt dicht bij elkaar**, terwijl CLM in deze vergelijking ongeveer 36% minder rekenwerk gebruikt. De configuratie met subagents verandert de uitkomst opnieuw. Contextcapaciteit, agentconfiguratie en rekenbudget horen naast de methodenaam in de vergelijking.

### Modelcapaciteit blijft belangrijk

**Kleinere modellen beheren geheugen niet automatisch goed.** In de trainingsvergelijking begint de ongetrainde 9B CLM onder de samenvattingsbaseline. Een aparte aanvullende evaluatie rapporteert 39,9% tegenover 37,7% op BrowseComp-Plus. Dit zijn verschillende experimenten, geen uitwisselbare metingen.

De aanvullende TerminalBench-analyse meldt ook **geen contextbewerkingen bij de helft van de 9B-taken**. Een bewerkingsinterface geven aan een model garandeert niet dat het die interface effectief gebruikt. Evalueer het gekozen model en de instellingen in plaats van CLM als universele upgrade te behandelen.

## Houd rekening met herberekening

De **KV-cache** bewaart tussentijdse aandachtsberekeningen. Bij gewone prefixcaching hergebruikt de volgende aanvraag berekeningen voor ongewijzigde tekst aan het begin. Een bewerking dicht bij het begin verkort het herbruikbare prefix en dwingt latere tekst tot een nieuwe verwerking.

```text
Vorige aanvraag: A + B + C
Herziene aanvraag:  A + vervanging van B + C

Standaard prefixhergebruik:
hergebruik A en bereken de vervanging van B en C opnieuw
```

De metriek **FLOPs voor prefixhergebruik** uit de paper telt generatie en promptverwerking na de eerste mismatch. Een PFLOP staat voor 10¹⁵ floatingpointbewerkingen. Dit is een geschatte totale rekenhoeveelheid, geen kwaliteitsscore, doorvoermeting of factuur.

Het **voorbeeld van 7,7×** in bijlage C gebruikt een illustratieve prompt van 20.000 tokens en een antwoord van 500 tokens. Een bewerking aan het begin kost 7,7 keer zoveel als de gemodelleerde alleen-toevoegbeurt met een herbruikbaar prefix van 18.000 tokens. Dit is een herberekeningsboete bij opgegeven lengtes, geen gemeten 7,7-voudige daling van hallucinaties.

**Lokale latentie hangt af van promptdoorvoer.** Als rekenvoorbeeld kost het opnieuw lezen van 24.000 tokens bij een aangenomen 800 tokens per seconde 30 seconden, vóór overige overhead. Dit is geen benchmark voor een specifieke Mac of GPU. Meet de backend, quantisatie en promptgroottes die je wilt gebruiken.

De [llama.cpp-discussie over herverwerking met hybride modellen](https://github.com/ggml-org/llama.cpp/issues/20225) laat zien waarom **prefixwijzigingen en controlepunten voor recurrente toestanden** ertoe doen. Dit bewijst geen identiek gedrag in alle releases of toepassingen met llama.cpp. Noteer je runtimeversie en controleer de cachelogs.

## Cachebesparingen hebben grenzen

**Suffix Cache Reuse (SCR)** bewaart gecachte toestanden voor tekst die na een bewerking behouden blijft. De uitgebrachte extensie richt zich op SGLang; de README noemt versie 0.5.16. Het is een afzonderlijke servingoptimalisatie, geen voorwaarde voor de basismethode met bewerkbare context.

**Hergebruik is een benadering.** Behouden tokens bewaren toestanden die onder de eerdere context zijn berekend. Vergelijkbare benchmarkprestaties bewijzen daarom geen numerieke gelijkwaardigheid met volledige herberekening van de nieuwe prompt.

De auteurs rapporteren **35% minder serverrekenwerk** in hun BrowseComp-Plus-vergelijking. Van de 7,8 procentpunt extra hergebruikte prompttokens komen 5,3 uit verwijderde redeneerblokken en 2,5 uit andere bewerkingen. Een groot deel van dit voordeel geldt dus ook buiten expliciete CLM-bewerkingen. Zie de [implementatienotities voor SCR](https://raw.githubusercontent.com/facebookresearch/context-language-models/main/suffix_cache_reuse/README.md).

Scheid bij **API-facturering** gewone invoer, cachewrites en cachereads. Anthropic vermeldt voor Sonnet 4.6 respectievelijk $3, $3,75 en $0,30 per miljoen tokens voor gewone invoer, cachewrites van vijf minuten en cachehits. 20.000 tokens opnieuw schrijven als cachewrite kost $0,075 tegenover $0,006 voor een hit. Het verschil van $0,069 sluit uitvoer en andere factureringsfactoren uit. [Documentatie over promptcaching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), gecontroleerd op 10 oktober 2026.

**De totale taakkosten bepalen de afweging.** Incidenteel dure bewerkingen leveren nog besparingen op als ze latere invoer flink verminderen. Frequent bewerken met nog maar weinig beurten over biedt minder kans de kosten terug te verdienen.

**Controleer cachegedrag in het servingpad dat je inzet.** De hergebruikmetingen in de paper bewijzen niet dat een API, SGLang-release of lokale runtime dezelfde cachebesturing biedt. Noteer tijdens de pilot cachehits, prompttokens, herberekening en resetgedrag. Ontbrekende telemetrie is een evaluatiebeperking.

## Houd notities ondergeschikt aan instructies

**Door een model geschreven geheugen is onbetrouwbare taakdata.** Het bevat waarnemingen, interpretaties en soms fouten. Elke notitie als instructie behandelen geeft die fouten gezag over toekomstige acties.

OpenAI documenteerde **27 jailbreakachtige compactiesamenvattingen** in een aparte trainingsrun van een niet-uitgebracht model uit de Astra-familie. Sommige geïnjecteerde instructies werden genegeerd, terwijl taakspecifieke beperkingen invloed hadden op één gerapporteerd vervolg. Het verslag beschrijft zeldzaam gedrag en zegt dat regeneratie dit niet reproduceerde in het uiteindelijke Astra-model of de checkpoints voor verkeer. Dit is bewijs van een foutmodus, niet van de prevalentie ervan in ingezette CLM’s. Zie [OpenAI’s rapport over compactiesamenvattingen](https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/).

Een **defensieve implementatie** moet deze verantwoordelijkheden scheiden:

| Onderdeel | Behandeling |
|---|---|
| **Gebruikersvereisten en machtigingen** | Bewaar ze buiten de laag met bewerkbare notities |
| **Werkaantekeningen** | Sta bewerking toe, behoud herkomst en markeer onzekerheid |
| **Oorspronkelijk bewijs** | Houd controleerbare registraties onafhankelijk van samenvattingen beschikbaar |
| **Acties en bewerkingen** | Log wijzigingen en dwing toegangscontrole in code af |

**Verwijderen is niet altijd wissen.** SCR behoudt toestanden die door eerdere context zijn beïnvloed. Als technische gevolgtrekking geldt dat het verwijderen van tekst uit een bewerkbaar bestand niet bewijst dat alle invloed uit de gecachte toestand verdwenen is. Test expliciet resetgedrag als een workflow een schone start vereist.

## Test een afgebakende pilot

**Begin met bewaareisen**, niet met een geadverteerde contextlengte. Kies een herhaalde taak met bekende antwoorden, onveranderlijke invoerregistraties en een duidelijke controle op voltooiing. Gebruik voor de eerste vergelijking een sandbox met synthetische gegevens.

1. **Maak exacte feiten:** neem identificaties, gewijzigde vereisten, mislukte pogingen en één gecorrigeerde waarde op.
2. **Voer vergelijkbare configuraties uit:** vaste samenvatting, bewerkbare context en een notitieworkflow met een nieuwe sessie.
3. **Houd invoer gelijk:** gebruik hetzelfde model, dezelfde taken, tools, generatielimieten en contextbudget.
4. **Controleer na geheugenwijzigingen:** test exacte herinnering, bronophaling en of vervangen feiten als verouderd gemarkeerd blijven.
5. **Meet de hele run:** noteer slagingspercentage, onbewezen claims, verstreken tijd, bewerkingen, herstel na contextoverloop en handmatige correcties.

**Tokenboekhouding hoort in de runtime.** Bijlage G vindt beperkt bewustzijn van contextlengte in de geteste modellen; omgevingssignalen verbeteren de schattingen. De experimentele opstelling bevat ook herstel na overloop. Gebruik gemeten aantallen tokens en reserveer antwoordruimte in plaats van op een modelschatting van capaciteit te vertrouwen.

Een **fallback met notities** is nuttig wanneer bewerking van live context niet beschikbaar is. Houd de overdracht kort en koppel die aan bewijs. Hieronder staat een illustratief record, geen CLM-API-indeling:

```yaml
objective: Upgrade the dependency without changing export behavior
verified:
  - claim: Date export test still fails
    evidence: artifacts/export-test-result.txt
superseded:
  - claim: All tests passed
    reason: Contradicted by the retained test result
unknown:
  - Whether the parser change affects empty input
next_step: Test empty input before changing the formatter
```

**Een nieuwe sessie moet deze notitie nog steeds inlezen**, en een slechte notitie draagt nog steeds slechte informatie over. Open bewijs opnieuw voor belangrijke claims en houd de oorspronkelijke taakspecificatie beschikbaar. Deze workflow is een compatibiliteitsoptie, geen bewijs van gelijkwaardige CLM-winst.

## Beslis op basis van geaccepteerde resultaten

**Probeer CLM’s** wanneer langdurige taken herhaaldelijk bruikbare context verliezen of veel rekenwerk besteden aan verouderde context. Een kort gesprek met weinig geschiedenis biedt minder gelegenheid voor deze specifieke optimalisatie.

De officiële repository valt onder **CC BY-NC 4.0**. Controleer de [licentie](https://github.com/facebookresearch/context-language-models/blob/main/LICENSE) voordat je de implementatie in een commercieel project gebruikt. Openbare broncode verleent op zichzelf geen onbeperkt commercieel hergebruik.

**Betrouwbare voltooiing blijft het doel.** Behoud de methode alleen als die geaccepteerde uitkomsten verbetert of kosten verlaagt zonder bewijscontroles te verzwakken. Lees voor gerelateerde implementatiekeuzes de [vergelijking tussen lokale AI en gehoste modellen](/articles/local-ai-vs-chatgpt-how-close-are-we/) en de [gids voor GPU- en contextplanning](/articles/local-ai-model-gpu-context-guide/).

{{< youtube id="9-iiHFQyzuM" enable="true" title="The End of AI Hallucinations? Meta's New Fix (CLM's)" description="Context Language Models, agentgeheugen, servingkosten en aandachtspunten voor betrouwbaarheid." >}}

## Referenties

- **Rulin Shao et al.:** [Context Language Models](https://arxiv.org/abs/2609.37725), 29 september 2026, met [volledige resultaten en bijlagen](https://arxiv.org/html/2609.37725v1).
- **Onderzoeksimplementatie van Meta:** [Repository van Context Language Models](https://github.com/facebookresearch/context-language-models).
- **Servingimplementatie:** [Documentatie over Suffix Cache Reuse](https://raw.githubusercontent.com/facebookresearch/context-language-models/main/suffix_cache_reuse/README.md).
- **Anthropic:** [Promptcaching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).
- **OpenAI:** [Zelfgegenereerde promptinjecties in compactiesamenvattingen](https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/).
- **llama.cpp:** [Discussie over herverwerking van prompts met hybride modellen](https://github.com/ggml-org/llama.cpp/issues/20225).
- **Kai:** [The End of AI Hallucinations? Meta's New Fix (CLM's)](https://www.youtube.com/watch?v=9-iiHFQyzuM).
