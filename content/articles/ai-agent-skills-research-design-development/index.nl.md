---
title: "9 AI-agentvaardigheidsprojecten voor onderzoek, ontwerp en ontwikkeling"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Vergelijk negen agentvaardigheidsprojecten op workflow, hostondersteuning, afhankelijkheden en kosten. Leer hoe je de benodigde vaardigheden installeert, inspecteert en test."
genre: ["Kunstmatige intelligentie", "Ontwikkelaarstools", "Softwareontwikkeling"]
tags: ["AI-agentvaardigheden", "Codex-vaardigheden", "Claude Code-vaardigheden", "last30days", "Impeccable", "gstack", "Superpowers", "Claude Video", "Humanizer", "NVIDIA SkillSpector", "HyperFrames", "Remotion", "SKILL.md", "agentworkflows", "vaardigheidsinstallatie", "vaardigheidsbeveiliging", "AI-onderzoek", "frontendontwerp", "videogeneratie", "ontwikkelworkflows", "agentaanpassing"]
cover: "/img/cover/agent-skill-workflow-library.webp"
coverAlt: "Ivoren instructiekaarten in een bakje naast een vergrootglas, kleurstalen en een kleine filmrol op een donker bureau"
coverCaption: "Conceptuele illustratie van een taakgerichte bibliotheek met agentvaardigheden."
---

**Installeer een agentvaardigheid om een herhaalbare taak te verbeteren.** Onderzoek naar recente discussies, beoordeling van interfaceontwerp en het renderen van een video gebruiken verschillende procedures en afhankelijkheden. Een nuttige vaardigheid levert de ontbrekende instructies, referentiematerialen of scripts voor een van deze taken.

**Negen projecten verdienen aandacht:** last30days, Humanizer, Impeccable, Superpowers, gstack, Claude Video, Remotion, HyperFrames en NVIDIA SkillSpector. Sommige zijn instructiebundels, sommige bevatten uitvoerbare tools en sommige zijn frameworks met aanvullende vaardigheden. Deze gids vergelijkt hun gedocumenteerde rollen en geeft een praktische manier om ze te kiezen, installeren en beoordelen.

**Momentopname van de documentatie: 10 oktober 2026.** De aanbevelingen zijn gebaseerd op projectdocumentatie en broninspectie, niet op een vergelijkende benchmark van uitvoerkwaliteit. Een gratis installatie bewijst niet dat inferentie, rendering, datatoegang of commercieel gebruik gratis is.

<!--more-->

## Belangrijkste punten

- **Begin met een terugkerende taak:** kies een vaardigheid met een duidelijk resultaat en een acceptatiecontrole.
- **Scheid vaardigheden van runtimes:** instructies installeren installeert niet elk vereist uitvoerbaar bestand.
- **Controleer de host:** een werkende Claude Code-integratie bewijst geen identiek gedrag in Codex of Cowork.
- **Inspecteer rechten en afhankelijkheden:** pakketcommando's, hooks, externe diensten en inloggegevens vragen elk om aparte aandacht.
- **Pas aan na het testen:** houd het projectbeleid leidend en bewaar upstreamversies.

## Kies op basis van het resultaat

| Vereiste uitvoer | Te beoordelen project | Eerste controle |
|---|---|---|
| **Actuele discussiesamenvatting** | last30days | Welke bronnen leverden bruikbaar bewijs? |
| **Bewerkte tekst** | Humanizer | Zijn betekenis en bronvermelding behouden? |
| **Verbeterde interface** | Impeccable | Werkt de aangepaste interactie? |
| **Geplande en geteste wijziging** | Superpowers | Past het proces bij de taakcomplexiteit? |
| **Review- en QA-workflow** | gstack | Welke functies werken op jouw agenthost? |
| **Video-observaties** | Claude Video / Watch | Worden claims door beelden of audio ondersteund? |
| **React-videocompositie** | Remotion-vaardigheden | Komt de geëxporteerde video overeen met de preview? |
| **HTML-videocompositie** | HyperFrames-vaardigheden | Blijft de animatie deterministisch bij zoeken? |
| **Inspectierapport voor een vaardigheid** | SkillSpector | Was de analyse compleet en wat werd gemarkeerd? |

**Een vaardigheid verschilt van een agentharnas.** Een vaardigheid geeft taakgerichte richtlijnen en soms scripts. Het harnas bepaalt hoe de agent instructies laadt, tools aanroept en rechten afdwingt. Onze [vergelijking van agentharnassen](/articles/best-ai-agent-harnesses/) behandelt deze omliggende systemen.

**Een vaardigheidsmap is ook geen plugininstallatie.** Plugins registreren soms hooks of extra tools die een handmatige mapkopie niet bevat. Lees de instructies voor jouw host en installatiemethode voordat je gelijkwaardig gedrag aanneemt.

## Onderzoek en schrijven

### last30days

**Gebruik last30days voor onderzoek naar recente discussies.** Het [project](https://github.com/mvanhorn/last30days-skill) combineert bronnen zoals Reddit, Hacker News, YouTube, X en het web. De beschikbare dekking hangt af van de gekozen bronnen, geïnstalleerde tools, authenticatie en providertoegang. De preflightmodus beschrijft geplande toegang en schrijfacties zonder onderzoek te starten.

**Vraag om een bewijsspoor.** Een bruikbaar resultaat bevat datums, links, terugkerende klachten en meningsverschillen. Een onbeschikbare bron hoort als dekkingsgat te verschijnen. Engagementcijfers beschrijven activiteit in verzamelde posts, geen representatieve enquête onder alle gebruikers.

**Voorbeeldtaak:** onderzoek terugkerende installatieproblemen bij een recent uitgebrachte bibliotheek. Groepeer meldingen per versie en besturingssysteem en controleer voorgestelde oplossingen daarna tegen de issuetracker of documentatie van de bibliotheek. Behandel een populaire workaround niet als een door upstream ondersteunde oplossing.

### Humanizer

**Gebruik Humanizer als bewerkingsstap.** De [vaardigheid](https://github.com/blader/humanizer) richt zich op herhaalde contrasten, geënsceneerde introducties, overdreven claims en andere schrijfgewoonten. Ze accepteert stemvoorbeelden en probeert de onderliggende betekenis te behouden.

**Lever de beperkingen samen met het concept aan.** Benoem het publiek, de feiten die moeten blijven staan en de citaten die gekoppeld moeten blijven. Vergelijk na het bewerken de feitelijke claims met het origineel. Een beter ritme is nuttig, maar valideert geen statistiek zonder onderbouwing.

| Schrijfcontrole | Geslaagd resultaat |
|---|---|
| **Betekenis** | Dezelfde claims, kwalificaties en reikwijdte |
| **Bronnen** | Bronvermelding blijft dicht bij overgenomen bevindingen |
| **Stem** | Past bij de beoogde lezer en aangeleverde voorbeelden |
| **Originaliteit** | Voegt eigen redenering toe in plaats van gekopieerde tekst te verhullen |

**Gebruik deze projecten in verschillende fasen.** last30days verzamelt materiaal voor onderzoek. Humanizer bewerkt formuleringen. Geen van beide vervangt bronverificatie of zelfstandig auteurschap.

## Interface- en ontwikkelwerk

### Impeccable

**Gebruik Impeccable voor gericht ontwerpwerk.** De [website](https://impeccable.style/) en [repository](https://github.com/pbakaus/impeccable) documenteren een ontwerpworkflow voor kritiek, typografie, lay-out, duidelijkheid, beweging en afwerking. Begin met een concreet gebruikersprobleem in plaats van om een vaag indrukwekkendere pagina te vragen.

**Voorbeeldbrief:** maak een pagina met abonnementsinstellingen beter scanbaar zonder annulering te verbergen of toetsenbordnavigatie te wijzigen. Vraag eerst om kritiek en implementeer daarna de gekozen wijzigingen. Controleer vervolgens mobiele lay-out, focusvolgorde, contrast en voltooiing van de oorspronkelijke taak.

**De installatiemodus doet ertoe.** De huidige Codex-instructies onderscheiden de vaardigheid van een projectspecifieke ontwerp-hook. Vertrouwen in een hook vereist een eigen goedkeuring in Codex. Een gekopieerde vaardigheidsmap bewijst niet dat een actieve hook bestaat.

### Superpowers

**Gebruik Superpowers voor een gestructureerd ontwikkelproces.** De [repository](https://github.com/obra/superpowers) bundelt workflows voor brainstormen, plannen, testen, debuggen en reviewen. Ze documenteert ook hostspecifieke plugininstallatie, waaronder Codex.

**Stem het proces af op de opdracht.** Een functie over dataopslag, UI en tests heeft baat bij een expliciet plan. Voor een spellingcorrectie is veel minder proces nodig. Definieer de toegestane reikwijdte zodat een algemene ontwikkelworkflow niet uitbreidt naar aangrenzend werk.

**Projectinstructies blijven gelden.** De voorkeursmethode voor testen, de worktree-aanpak en het delegatiepatroon van een vaardigheid moeten passen bij de repository en het verzoek. Een methode installeren geeft geen toestemming voor elke beschreven actie.

### gstack

**Gebruik gstack voor een bredere engineeringworkflow met uitvoerbare tools.** De [documentatie](https://github.com/garrytan/gstack) bevat planning, review, browser-QA, onderzoek en releasegerichte vaardigheden. De installatie bouwt ondersteunende tools in plaats van alleen tekst te kopiëren.

**Codex-ondersteuning is nog experimenteel.** Het project onderscheidt door hooks afgedwongen veiligheidsfuncties in Claude Code van adviserend gedrag in Codex. Ga er niet van uit dat een gelijknamig commando op elke host dezelfde afdwinging biedt.

**Mijn keuzeregel:** probeer Superpowers als een herhaalbaar ontwikkelproces ontbreekt. Probeer gstack als de specifieke review- of browsertools een actuele behoefte oplossen. Als beide zijn geïnstalleerd, kies dan per taak één hoofdworkflow en geef de andere een afgebakende bijdrage.

| Ontwikkelprobleem | Nuttige evaluatietaak |
|---|---|
| **Onduidelijke scope** | Een begrensd plan met acceptatiecriteria maken |
| **Kwetsbare implementatie** | Een voorbereide regressie herstellen en bestaand gedrag behouden |
| **Defecte interactie** | Een browserfout reproduceren en bewijs bewaren |
| **Conflicterende workflows** | Bevestigen dat alleen het gekozen proces de taak aanstuurt |

## Videobewijs en productie

### Claude Video / Watch

**Gebruik Claude Video om bewijs uit een video te verzamelen.** Ondanks de naam van de repository ondersteunt de [Watch-vaardigheid](https://github.com/bradautomates/claude-video) lokale agents, waaronder Codex. De lokale route gebruikt downloads, gesamplede frames en ondertiteling of transcriptie. Een aparte Gemini-route stuurt de video voor analyse naar het model wanneer die is geconfigureerd.

**Controleer de huidige hostondersteuning.** De README vermeldt Claude Chat en Cowork als niet ondersteund. Lokale uitvoering vereist mediatools zoals FFmpeg en yt-dlp, terwijl afzonderlijke websites toegangsbeperkingen houden.

**Houd visuele en auditieve claims gescheiden.** Een transcript ondersteunt gesproken woorden. Frames ondersteunen zichtbare details op gesamplede momenten. Geen van beide bewijst een onzichtbare gebeurtenis tussen de samples. Vraag om tijdstempels en onopgeloste observaties in plaats van zonder voorbehoud te beweren dat je de hele opname hebt begrepen.

### Remotion

**Gebruik Remotion voor videocomposities in React.** De [frameworkrepository](https://github.com/remotion-dev/remotion) verwijst naar een aparte [agentvaardighedencollectie](https://www.remotion.dev/docs/ai/skills). De collectie behandelt projectcreatie, markup, kaarten, ondertitels, Studio en rendering. De collectie installeren maakt geen videoproject en installeert niet alle projectafhankelijkheden.

**Controleer de licentie los van de download van de vaardigheid.** De [prijspagina](https://www.remotion.dev/docs/license/pricing) van Remotion vermeldt een gratis licentie voor individuen en bedrijven tot drie personen, plus bedrijfslicenties voor grotere teams en bepaalde samenwerkingen. Controleer de huidige voorwaarden voor jouw gebruik.

### HyperFrames

**Gebruik HyperFrames voor HTML-videocompositie.** De [repository](https://github.com/heygen-com/hyperframes) beschrijft het renderen van HTML, CSS, media en doorzoekbare animatie naar MP4. De gepubliceerde vaardigheden begeleiden compositie, preview, validatie en rendering.

**Begin met de gedocumenteerde kernset.** De huidige installatie-instructies onderscheiden kernvaardigheden van de grotere gepubliceerde collectie en repository-interne vaardigheden. Elke map zonder selectie installeren voegt irrelevante instructies toe en maakt onderhoud lastiger.

| Videoworkflow | Belangrijke acceptatiecontrole |
|---|---|
| **Watch** | Observaties met tijdstempels komen overeen met het geïnspecteerde medium |
| **Remotion** | De eindexport behoudt timing, lettertypen, audio en lay-out |
| **HyperFrames** | Naar een frame zoeken toont de bedoelde visuele toestand |

**Kies met een gecontroleerd voorbeeld.** Geef Remotion en HyperFrames dezelfde opdracht, assets, duur en uitvoerafmetingen. Animeer bijvoorbeeld een onderhoudsprocedure in drie stappen met bijschriften en één diagram. Vergelijk geëxporteerde bestanden, bewerkingswerk en renderfouten. Eén aantrekkelijke demo bewijst geen algemene winnaar.

## Inspecteren met SkillSpector

```bash
skillspector scan ./downloaded-skill --no-llm --format json --output report.json
```

**NVIDIA SkillSpector is een scanner, geen video- of schrijfvaardigheid.** Het [project](https://github.com/NVIDIA/SkillSpector) documenteert statische controles en optionele modelondersteunde analyse voor agentvaardigheidspakketten. Het commando hierboven veronderstelt dat de CLI al is geïnstalleerd en een lokale map scant zonder de doelvaardigheid uit te voeren.

**Lees bevindingen en dekking samen.** Inspecteer gemarkeerde bestanden en omliggende code en noteer welke controles zijn voltooid. Een onvolledige scan mag geen schoon oordeel worden. Een treffer op een trefwoord vraagt ook om context. Een gedocumenteerd openbaar maptoken van een provider verschilt van code die niet-gerelateerde inloggegevens verzamelt.

**Statisch betekent niet volledig offline.** Volgens het project gaan namen en versies van afhankelijkheden met **`--no-llm`** nog naar OSV voor kwetsbaarheidscontrole. Modelanalyse stuurt daarnaast geschikte bestandsinhoud naar de geconfigureerde provider. Kies de modus die bij het te beoordelen materiaal past.

**Gebruik het rapport als bewijs voor een beslissing.** Leg uit of elke bevinding voor de taak nodig is, welke gegevens de machine verlaten en welke macht de runtime verleent. Een lage score bewijst geen veiligheid en reputatie lost een onverklaarde bevinding niet op.

## Installeer het juiste pakket

**Bepaal eerst de canonieke distributie van de vaardigheid.** Het Remotion-framework en de vaardigheden staan in verschillende repositories. Claude Video biedt een vaardigheid met de naam Watch. SkillSpector wordt als CLI geïnstalleerd, met een aparte agentintegratie. Daarom is een project klonen niet altijd genoeg.

**De voorbeeldcommando's hieronder komen uit de huidige installatiedocumentatie van de projecten.** Voer alleen het commando voor het gekozen project uit. De pakketstarter downloadt en voert installatiecode uit. Inspecteer daarom eerst het upstreamproject en kies de installatiescope.

```bash
# Humanizer: user-wide Codex installation
npx skills add blader/humanizer --global --agent codex

# last30days: user-wide Codex installation
npx skills add mvanhorn/last30days-skill -g -a codex

# Remotion: official skill collection, not the framework repository
npx skills add remotion-dev/skills
```

**Het derde commando opent de installatieworkflow.** Kies de bedoelde agent en scope in plaats van aan te nemen dat de standaardwaarden overeenkomen met de expliciet beperkte commando's hierboven. Plugininstallers en zelfstandige mapinstallaties hebben ook verschillende updateprocessen.

**Behoud bestaande installaties.** Controleer vóór vervanging de versie, lokale wijzigingen en beheerder van een vaardigheid. Bewaar geen concurrerende kopieën in gebruikers-, project- en pluginlocaties, tenzij de host documenteert hoe deze worden opgelost.

| Installatiestatus | Wat dit vaststelt |
|---|---|
| **Bestanden aanwezig** | Instructies en verwezen assets bestaan |
| **Host vindt vaardigheid** | De agent herkent naam en beschrijving |
| **Afhankelijkheden gereed** | Vereiste uitvoerbare bestanden en pakketten zijn beschikbaar |
| **Taak geverifieerd** | Een representatief resultaat doorstaat onafhankelijke controles |

**Controleer elke fase in volgorde.** Een geslaagde mapkopie bewijst geen werkende browser, download, transcriptie of render. Houd optionele providersetup apart van de basisinstallatie en sla geen inloggegevens op in vaardigheidsbestanden.

**Noteer host en revisie voor elke proef.** Vermeld of de vaardigheid via Claude Code, Codex, Cowork of een andere host werkt. Bewaar de upstreamcommit of pakketversie samen met het acceptatieresultaat. Vergelijkbare namen bewijzen geen identieke ontdekking, hooks, rechten of tooltoegang.

## Testen vóór aanpassen

**Gebruik één opgeslagen taak als baseline.** Voer die zonder de nieuwe vaardigheid uit en daarna met de vaardigheid, waarbij model, invoer, tools en acceptatiecriteria zo gelijk mogelijk blijven. Noteer mislukkingen en menselijke correcties samen met het eindresultaat.

```yaml
# Illustrative evaluation record, not a skill configuration schema
job: "review a settings page"
input: "same source revision and test data"
variants:
  - "agent without the selected skill"
  - "same agent with the selected skill"
acceptance:
  - "required actions remain visible"
  - "keyboard navigation works"
  - "mobile layout remains usable"
record:
  - "skill source and revision"
  - "model and enabled tools"
  - "completed checks and retained evidence"
  - "elapsed time and manual corrections"
  - "external service usage"
```

**Pas de terugkerende fout aan, niet het hele pakket.** Als onderzoekssamenvattingen tegenstrijdig bewijs verliezen, voeg dan de eis toe om afwijkende bronnen te behouden. Als een ontwerpaanpassing bestaande kleuren verandert, verwijs dan naar de designtokens. Als videocaptions overlopen, voeg dan een controle van de uitvoerresolutie toe.

**Houd lokale toevoegingen traceerbaar.** Noteer de upstreamrevisie, je wijzigingen en de taak die ze motiveerde. Voer opnieuw een proef uit wanneer nieuwe triggers, scripts of afhankelijkheden het eerdere proces wijzigen.

**Let op overlappende instructies.** Ontwikkelsuites, designvaardigheden en teksteditors hebben allemaal voorkeuren. Repositoryregels en het huidige verzoek bepalen de uitkomst. Een stijlvaardigheid mag geen toegankelijkheidslabels, citaten of technische termen verwijderen om de formulering te variëren.

## Bouw een nuttige bibliotheek

**Begin met het werk dat je het vaakst herhaalt.** Een schrijver kan last30days en Humanizer testen. Een frontendontwikkelaar kan beginnen met Impeccable en één ontwikkelworkflow. Een videomaker kiest een productieframework en voegt Watch toe wanneer bronvideoanalyse onderdeel van het werk is.

**Begroot exploitatie en installatie apart.** Tel modelaanroepen, optionele zoekproviders, transcriptie, mediageneratie, renderinfrastructuur en toepasselijke licenties mee. Een gratis repository beantwoordt slechts een deel van de kostenvraag.

**Voor de eerste proef:** bereid goedgekeurde modeltoegang, een wegwerpbaar project of voorbeeld en schriftelijke acceptatiecriteria voor. Basisskills voor instructies zijn toegankelijk voor beginners. Browsertools, media-afhankelijkheden en cloudrendering vragen meer voorbereiding. Reserveer een uur voor een beperkte proef en herhaal die daarna met representatieve invoer voordat je de workflow standaard maakt.

**Behoud vaardigheden met bewezen waarde.** Houd de vaardigheden die gemiste stappen of reviewwerk verminderen en verwijder duplicaten die conflicterend gedrag veroorzaken. Controleer hostcompatibiliteit en afhankelijkheden opnieuw wanneer je agentomgeving verandert.

{{< youtube id="3fdb_giOrLo" enable="true" title="9 Free AI Agent Skills You NEED to Install Now" >}}

## Referenties

- [last30days: onderzoeksvaardigheid en installatie](https://github.com/mvanhorn/last30days-skill)
- [Humanizer: schrijfvaardigheid](https://github.com/blader/humanizer)
- [Impeccable: ontwerpworkflow](https://impeccable.style/)
- [Impeccable: repository en hostspecifieke installatie](https://github.com/pbakaus/impeccable)
- [Superpowers: ontwikkelvaardigheden](https://github.com/obra/superpowers)
- [gstack: engineeringtools en hostondersteuning](https://github.com/garrytan/gstack)
- [Claude Video: Watch-vaardigheid en runtimevereisten](https://github.com/bradautomates/claude-video)
- [Remotion: React-videoframework](https://github.com/remotion-dev/remotion)
- [Remotion: agentvaardigheden](https://www.remotion.dev/docs/ai/skills)
- [Remotion: licenties en prijzen](https://www.remotion.dev/docs/license/pricing)
- [HyperFrames: framework en vaardigheidsdistributie](https://github.com/heygen-com/hyperframes)
- [NVIDIA SkillSpector: scannergedrag en gegevensverwerking](https://github.com/NVIDIA/SkillSpector)
- [Futurepedia: 9 Free AI Agent Skills You NEED to Install Now](https://www.youtube.com/watch?v=3fdb_giOrLo)
