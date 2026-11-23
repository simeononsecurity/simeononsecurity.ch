---
title: "Eén bron, veel tools: een AI-samenwerkingskader voor gemengde teams"
date: 2026-10-01
lastmod: 2026-11-23
toc: true
draft: false
description: "Bouw een gedeeld AI-samenwerkingssysteem met broneigenaarschap, versiebeheer van context, duurzame wijzigingsbeoordeling en keuzes tussen projectkaarten en RAG."
genre: ["Kunstmatige intelligentie", "Kennisbeheer", "Softwareontwikkeling", "Teamsamenwerking"]
tags: ["AI-samenwerkingskader", "gemengde teams", "bron van waarheid", "AI-agenten", "AGENTS.md", "CLAUDE.md", "Cline-regels", "Claude Code", "Codex", "ChatGPT", "Copilot", "Cowork", "generatie met opgehaalde informatie", "RAG", "Model Context Protocol", "projectkaart", "contextmanifest", "kennisbeheer", "documentatiedrift", "menselijke goedkeuring", "besluitenregister", "agentoverdracht", "beleidsversiebeheer", "Git-worktrees", "pull-requestcontroles"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Een illustratie van professionals die samenwerken aan cybersecurity"
coverCaption: ""
---

**Twee mensen stellen twee AI-tools dezelfde vraag:** hoe lang moet een dienst exports bewaren? In dit voorbeeld zegt de IDE-agent van een ontwikkelaar zeven dagen op basis van een README. De chatassistent van een operationeel verantwoordelijke zegt dertig dagen op basis van een wikipagina. Beide antwoorden klinken overtuigend. Elke tool las een andere versie van de waarheid.

**Het probleem is eigenaarschap**, niet de kwaliteit van de prompt. De wiki-eis veranderde vorige week, maar niemand werkte de README bij. De ontwikkelaar vraagt de agent de bewaartaak aan te passen. De agent volgt het oudere document en levert een nette patch op die het verkeerde gedrag herstelt. Beoordelaars zien niet welke versie van de eis het antwoord onderbouwde.

**Geef elk feit één thuis.** Laat elke tool die bron lezen en laat een persoon elke blijvende wijziging beoordelen. **Repository, wiki en tracker houden elk hun eigen doel.** Wijs ze expliciet gezag en eigenaren toe, en spreek af hoe informatie tussen systemen wordt verplaatst.

**Deze gids biedt een model dat je deze week kunt toepassen**, met of zonder retrieval-augmented generation. Begin met een projectkaart, versiebeheer voor instructies, bewijsregistraties en beoordeelde voorstellen. Voeg zoekinfrastructuur pas toe als het informatieprobleem daar om vraagt.

**Je eerste oplevering is een bronnenregister**, geen connector. Leg per feitstype de gezaghebbende bron, eigenaar, actuele revisie en goedkeurder van wijzigingen vast.

## Belangrijkste punten

- **Wijs gezag toe per informatietype**, in plaats van alles in één toepassing onder te brengen.
- **Behandel geheugen en retrieval-indexen als caches**, nooit als zelfstandige beleidsbronnen.
- **Koppel bronversies aan voorstellen**, zodat beoordelaars zien welke feiten een wijziging onderbouwen.
- **Dwing goedkeuring buiten prompts af**, via toegangsbeheer en verplichte beoordelingscontroles.
- **Deel de werkwijze tussen tools**, en pas de uitvoering aan elke interface aan.

## Voordat je begint

**Vereisten:** kies een proefproject met repository, wiki of documentensysteem, tracker en eigenaren die wijzigingen willen beoordelen. **Zonder wiki gebruik je een documentensysteem met versiebeheer.** Het eigenaarschapsmodel blijft gelijk.

**Geschatte tijd:** reserveer twee tot vier uur voor de eerste kaart en sjablonen, plus een proefweek. **Moeilijkheid:** gemiddeld. Afspreken welke bron gezag heeft is lastig, niet een nieuwe AI-tool installeren.

**Reikwijdte:** dit is een voorgesteld werkmodel voor teams. De goedkeuringsregels en naamgevingsconventies zijn aanbevelingen, geen standaardgedrag dat Claude Code, Codex, Cline, Cowork, Copilot of ChatGPT garandeert. De inhoudsopgave hierboven linkt naar elke implementatiestap.

## Verschillende tools, gescheiden context

**Programmeurs en niet-programmeurs delen een project**, maar gebruiken andere interfaces. Een ontwikkelaar gebruikt een IDE- of terminalagent. Een producteigenaar gebruikt een chatproject. Operations werkt vanuit een wiki en tracker. Kies de interface op basis van de taak, niet op basis van toegang tot gezaghebbende feiten.

**Context is het materiaal dat voor het huidige antwoord beschikbaar is.** **Controleer per sessie repositorybestanden**, geüploade documenten, chatgeschiedenis, opgeslagen geheugen, connectorresultaten en opgehaalde fragmenten. Sessies met verschillend bewijs hoeven het niet eens te zijn, zelfs bij dezelfde vraag.

| Probleem | Wat je ziet |
|---|---|
| **Documentatiedrift** | Een README herhaalt een verouderde eis |
| **Promotie van samenvattingen** | Een sessiesamenvatting wordt bewijs zonder de oorspronkelijke bron |
| **Overlappende wijzigingen** | Twee agents vervangen dezelfde pagina vanuit verschillende basisversies |
| **Verloren besluiten** | Een vergaderafspraak bereikt het besluitenregister niet |
| **Ontbrekende herkomst** | Een aannemelijk antwoord noemt geen paginaversie of commit |

**Het voorbeeld met de bewaartermijn maakt het onderscheid duidelijk.** De wiki beschrijft het goedgekeurde gewenste gedrag. **De code beschrijft wat is geïmplementeerd.** Geen van beide hoort de ander stilzwijgend te herschrijven. Leg het verschil vast en vraag de eigenaar of de implementatie of eis moet veranderen.

> **Belangrijk punt:** overeenstemming over gezag gaat vooraf aan overeenstemming over een AI-tool. Begin met deze gedeelde begrippen.

### Zijbalk: vijf gedeelde begrippen

| Begrip | Betekenis in dit kader |
|---|---|
| **Bron** | Het gezaghebbende record voor een informatietype |
| **Cache** | Een afgeleid exemplaar voor snelheid of gemak |
| **Voorstel** | Een voorgestelde wijziging die op goedkeuring wacht |
| **Projectkaart** | Een index van bronlocaties, identificatoren en eigenaren |
| **Manifest** | Een registratie van het exacte bewijs voor een antwoord of voorstel |

## Geef feiten één thuis

**Eén bron betekent één autoriteit per feit**, niet **één database voor de hele organisatie**. Stel deze verdeling tijdens de proef vast en vervang voorbeeldrollen door de echte eigenaren van je team.

| Informatietype | Bronsysteem | Eigenaar | Wie schrijft | Hoe agents lezen |
|---|---|---|---|---|
| **Code, tests, configuratie, schema's** | Repository | Technisch beheerder | Bijdragers via beoordeelde pull requests | Bestanden op een vastgelegde commit |
| **Geleverde documentatie en ADR's** | Repository | Technisch eigenaar | Bijdragers via dezelfde pull request | Bestanden met versiebeheer |
| **Vereisten** | Wiki | Producteigenaar | Eigenaar of goedgekeurde uitgever | Pagina-ID en revisie |
| **Runbooks** | Wiki | Operationeel eigenaar | Goedgekeurde uitgever | Pagina-ID en revisie |
| **Beleid** | Wiki | Beleidseigenaar | Goedgekeurde uitgever na beoordeling | Canonieke pagina plus lokale adapter |
| **Besluiten tussen teams** | Wiki-besluitenregister | Benoemde besluiteigenaar | Eigenaar na goedkeuring | Besluit-ID en status |
| **Taken en bevindingen** | Tracker | Taakeigenaar | Mensen of toegestane voorstelinvoer | Issue-ID en revisie |
| **Chats, samenvattingen, embeddings** | Alleen cache | Sessie- of indexbeheerder | Tools en deelnemers | Alleen verwijzing, gevolgd door broncontrole |

**Een architectuurbesluitrecord (ADR)** hoort bij de code als het de repositoryarchitectuur bepaalt. Een besluit tussen teams hoort in het gedeelde register. Koppel de twee records wanneer een besluit beide werkgebieden raakt. Houd de goedkeuringsstatus niet bij in twee onafhankelijke kopieën.

**Lokale beleidskopieën blijven ondergeschikt** aan de canonieke beleidspagina. Repositorytests en schema's zijn bronnen binnen hun eigen werkgebied. **De locatie bepaalt het gezag niet; de kaart doet dat.**

**Een cache gaat nooit boven een bron.** Als een samenvatting zeven dagen noemt en de goedgekeurde eis dertig, gebruik de eis voor het gewenste gedrag. Bewaar de tegenstrijdige samenvatting als bewijs van drift, niet als concurrerende regel. Leg daarna het wijzigingspad vast.

## Cache omlaag, voorstel omhoog

**Agents halen bewijs op in de sessiecontext** en stellen vervolgens wijzigingen voor. Ze keuren duurzame feiten niet zelf goed. Een taakbranch aanpassen of concept indienen is iets anders dan beleid publiceren, code samenvoegen of een besluit accepteren.

```text
Bron -> geautoriseerde leesactie -> sessiecontext
Sessiecontext -> voorstel + basisversie -> beoordeling door eigenaar
Goedkeuring door eigenaar -> gecontroleerde publicatie -> wijzigingslog
Gewijzigde basisversie -> voorstel afstemmen -> opnieuw beoordelen
```

**Leg de basisversie vast** voordat je beoordeling vraagt. Een beoordelaar heeft de vorige waarde, voorgestelde waarde, reden, bewijs en betrokken systemen nodig. Goedkeuring moet naar één revisie van het voorstel verwijzen, niet naar een veranderende chat.

```yaml
proposal_id: PROP-042
target: wiki:REQ-17
base_version: 8
change: "Bewaar exports dertig dagen in plaats van zeven."
evidence:
  - "besluit:DEC-12 goedgekeurd"
affected_records:
  - "repo:export-service retention configuration"
  - "wiki:RUN-04 cleanup procedure"
owner_role: product-owner
status: awaiting-review
```

**De identificatoren hierboven zijn voorbeelden.** Sla voor elke goedgekeurde logische wijziging één rij op met voorstel-ID, doelrecords, oude en nieuwe versies, goedkeurder, tijdstip en verwijzing naar samenvoeging of publicatie. Koppel systeemauditgebeurtenissen aan die rij in plaats van de oorspronkelijke historie te vervangen.

**Mensen nemen het besluit.** Een bevoegde uitgever of beperkte automatisering voert **de goedgekeurde revisie** door. Beperk schrijfrechten. Instructies alleen scheiden opstellen en publiceren niet. Hetzelfde onderscheid geldt voor informatie ophalen.

## Gedeelde context zonder RAG

**Een projectkaart is de eerste retrieval-index.** Beheer één pagina per project met bron-ID's, repositorylocaties, tracker-ID's, gezagsgebieden en eigenaren. Lees eerst de kaart en haal het relevante record daarna op via zijn ID. Gebruik zoeken als de ID onbekend is.

### Zijbalk: voorbeeld van een projectkaart

```yaml
project: export-service
map_id: MAP-01
policy:
  source_id: POL-01
  approved_version: 3
  owner_role: policy-owner
sources:
  requirements: {page_id: REQ-17, owner_role: product-owner}
  runbook: {page_id: RUN-04, owner_role: operations-owner}
  decisions: {register_id: DEC-REGISTER, owner_role: project-lead}
repository:
  key: export-service
  setup: README.md
  terms: CONTEXT.md
  decisions: docs/adr/
tracker:
  project_key: EXP
  active_task: EXP-42
```

**Directe connectors beperken handmatig kopiëren.** Model Context Protocol (MCP) is een integratieprotocol waarmee AI-toepassingen tools en context gebruiken. Gebruik goedgekeurde wiki-, tracker- en repositoryconnectors waar beschikbaar. Gericht ophalen beperkt irrelevante resultaten, maar vervangt autorisatie- en actualiteitscontroles niet. Volg de MCP-beveiligingsrichtlijnen in de referenties bij het kiezen van connectorrechten.

**Exact ophalen vraagt weinig inrichting.** Het geeft citeerbaar bewijs zonder vectordatabase. De beperkingen zijn duidelijk: iemand onderhoudt de kaart, brede vragen vereisen extra zoeken en grote pagina's vullen de sessie. Haal de relevante sectie met omliggende voorwaarden op in plaats van een heel handboek te plakken.

**Offline werk gebruikt expliciete momentopnamen.** Noteer de geëxporteerde revisie en markeer antwoorden als gebaseerd op een momentopname. Publiceer niets voordat een bevoegd persoon of connector de actuele bron controleerde. Maak hetzelfde beleid daarna zichtbaar in elke interface.

## Eén beleid, verschillende adapters

**Houd één gedeeld beleid aan** en verspreid korte adapters per tool. Zet de goedgekeurde beleidsversie op regel één van elke adapter of gekopieerde instructieset. Vermeld de bron-ID en voeg een beoordeelde lokale momentopname toe voor sessies zonder connector.

**Laadgedrag verschilt per tool.** Codex documenteert gelaagde ontdekking van `AGENTS.md`. Claude Code documenteert `CLAUDE.md`, imports en projectgeheugen. Cline documenteert `.clinerules/` en regelinstellingen. Gebruik de officiële instructiedocumentatie in de referenties. Controleer in je geïnstalleerde versie welke instructies zijn geladen; neem niet aan dat bestandsnamen overal hetzelfde werken.

### Zijbalk: voorbeeldkop voor AGENTS.md

```markdown
Beleidsversie: v3 | Bron: wiki:POL-01 | Status: goedgekeurd

# Projectinstructies

Lees vóór een taak de projectkaart MAP-01.
Laad docs/policy-snapshot.md en noteer de bronrevisie.
Behandel chatgeheugen en zoekfragmenten als caches.
Koppel bronrevisies aan elk feitelijk voorstel.
Gebruik één taakbranch en één worktree per programmeertaak.
Publiceer geen beleid, keur geen besluiten goed en voeg je eigen PR niet samen.
Stop bij onopgeloste bronconflicten of overlappende schrijfacties.
Verplichte controles: tests, documentatiebeoordeling en beleidsactualiteit.
Eigenaren: engineeringbeheerder, producteigenaar en beleidseigenaar.
```

**Chatprojectinstructies krijgen dezelfde kop en werkwijze.** Een niet-programmeur ontvangt de beleidssnapshot en projectkaart via goedgekeurde uploads of connectors. Als de interface geen live toegang heeft, levert iemand de versie-export aan en registreert de beperking.

**Een versielabel is een bewering, geen bewijs van identieke inhoud.** Genereer adapters uit de goedgekeurde snapshot of vergelijk hun beleidsdelen met een opgeslagen digest. Beoordeel uitzonderingen per adapter. Controleer tijdens de proef op uitgeschakelde regels, geneste overschrijvingen en persoonlijke instructies. Leg daarna vast welk bewijs elke taak gebruikte.

## Een contextmanifest registreren

**Een contextmanifest beschrijft het bewijs achter een antwoord.** Noteer pagina-ID's en revisies, issue-ID's en hun revisie of bijwerktijd, en volledige repositorycommit-ID's. Vermeld het ophaaltijdstip en relevante secties. Markeer ontbrekende records in plaats van een herinnerde samenvatting in te vullen.

```yaml
task: EXP-42
policy: {page_id: POL-01, version: 3}
wiki:
  - {page_id: REQ-17, version: 8, section: export-retention}
tracker:
  - {issue_key: EXP-42, revision: 5}
repository:
  commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  files: [README.md, config/retention.yaml]
limits:
  - "Runbook niet opgehaald. Geen wijziging aan runbook voorgesteld."
```

**De commitwaarde is synthetisch.** Vervang deze in een echt manifest door de gecontroleerde commit. Voeg het ophaaltijdstip toe tijdens het lezen. Een record dat vóór de inspectie is gemaakt, is een checklist, geen bewijs.

**Citaten helpen controleren**, maar garanderen geen vertrouwen. Verwijs voor elke belangrijke bewering naar het ondersteunende record en de sectie. Als bronnen elkaar tegenspreken, houd ze allebei in het manifest en meld het onopgeloste verschil. Kies niet de nieuwste tijdstempel zonder werkgebied en goedkeuringsstatus te controleren. Deze bewijsdiscipline geldt ook voor semantisch ophalen.

## Gedeelde context met RAG

**Retrieval-augmented generation (RAG)** levert opgehaald materiaal aan een model dat een antwoord opstelt. **Een semantische index vindt relevante passages**, ook als de vraag andere woorden gebruikt. Microsoft's RAG-overzicht behandelt grounding, retrievalbeperkingen en toegangsbeheer. Zie de officiële bron bij de referenties.

**Gebruik RAG om grotere verzamelingen te doorzoeken**, zoals oude documentatie, vergadernotities en transcripties. Label documentklassen en goedkeuringsstatussen. Een transcript uit de oorspronkelijke opname is bewijs van wat deelnemers zeiden, maar geen autoriteit voor goedgekeurde vereisten. Maak een gesprek via indexering geen beleid.

| Indexregel | Vereist gedrag |
|---|---|
| **Bronnen innemen, geen caches** | Sluit gegenereerde samenvattingen en onbeheerde lokale kopieën uit |
| **Herkomst behouden** | Bewaar per fragment bron-ID, revisie, sectie en documentstatus |
| **Bij wijzigingen vernieuwen** | Indexeer wijzigingen opnieuw en maak oude fragmenten ongeldig |
| **Toegangswijzigingen respecteren** | Werk rechten bij en verwijder ingetrokken of verwijderde inhoud |
| **Citaten teruggeven** | Toon bronverwijzingen naast opgehaalde tekst |
| **Live record controleren** | Haal actuele gegevens op vóór een ingrijpend voorstel |

**Een opgehaald fragment is in dit kader een verwijzing.** De tekst helpt het bewijs te vinden. De live bron bevestigt actuele formulering, goedkeuring, uitzonderingen en toegang. Markeer de momentopname en stop de ingrijpende actie als live ophalen mislukt. Dit is een bestuursregel, geen uitspraak over elke RAG-implementatie.

**Verouderde embeddings en ontbrekende context vormen aparte risico's.** Een oud fragment mist een revisie. Een actueel fragment misleidt nog steeds als een uitzondering in de volgende sectie staat. Behoud koppen en haal omliggende voorwaarden op voordat je een eis beoordeelt.

**Toegangslekken verdienen een eigen test.** Dwing autorisatie af voordat fragmenten naar het model gaan, niet pas na het antwoord. Controleer gevoelige inhoud vóór indexering of externe embedding-aanroepen. Houd rekening met kopieën in logs, modelverzoeken en retrievaltraces. Een lokaal model maakt een externe connector niet lokaal. Deze controles bepalen of RAG in de proef past.

## Kies een kaart, RAG of beide

**Stem retrieval af op de vraag.** Een bekende eis-ID pleit voor directe toegang. Een open vraag over verspreid historisch materiaal pleit voor zoeken. Begin met de kaart, tenzij ontdekken al een aantoonbaar probleem is.

### Zijbalk: RAG of niet?

```text
Noemen taken meestal een project, pagina, issue of bestand?
  Ja -> Is directe retrieval voldoende voor de proef?
           Ja -> ALLEEN KAART
           Nee -> HYBRIDE: kaart voor bekende ID’s, RAG om te ontdekken
  Nee -> Is bewijs verspreid over een grote verzameling?
           Nee -> ALLEEN KAART, plus ingebouwde zoekfunctie
           Ja -> Is het werk verkennend en alleen-lezen?
                    Ja -> ALLEEN RAG voor ontdekking
                    Nee -> HYBRIDE met live-broncontroles

Elke optie behoudt eigenaren, autorisatie en herkomst.
Ontdekking met RAG controleert bronnen nog vóór duurzame acties.
```

**RAG-only beschrijft de retrievalinterface**, geen vrijstelling van beheer. Gebruik die voor een afgebakende verkennende verzameling waar directe broncontrole beschikbaar blijft. Ze past slecht bij wijzigingen op bekende ID's die precieze versiecontroles vereisen.

**Het hybride model scheidt ontdekken van verifiëren.** De kaart behandelt bekende zoekopdrachten. RAG vindt onbekende records. RAG antwoordt op “waar”; de bron antwoordt op “wat”. Haal voor het bewaartermijnvoorbeeld `REQ-17` rechtstreeks op. Zoek voor “welke oudere exportbesluiten verklaren deze limiet?” in het register en haal elk relevant besluit op. Pas nu de repositorykant toe.

## Informatie in de repository

**Repositorykennis verandert met de implementatie.** Houd de structuur compact, zodat een agent en beoordelaar weten waar ze moeten zoeken.

| Bestand of map | Verantwoordelijkheid |
|---|---|
| **`CONTEXT.md`** | Projecttermen en links naar gezaghebbende records |
| **`docs/adr/`** | Geaccepteerde architectuurbesluiten voor de repository |
| **`docs/design/`** | Goedgekeurde beschrijvingen van systeemgedrag |
| **`docs/plans/`** | Implementatievoorstellen met expliciete status |
| **`AGENTS.md`** | Beoordelingscontroles, grenzen en eigenaarsrollen |
| **`README.md`** | Installatie en startpunten, geen dubbele vereisten |

**Pas de regel voor dezelfde pull request toe:** wijzig code en relevante repositorydocumentatie tegelijk. Is een kennisbankupdate niet nodig, eis dan een schriftelijke uitzondering in de PR-beschrijving of op de afgesproken plek voor committrailers.

```text
KB-Update: none (reden: interne refactor behoudt gedocumenteerd gedrag)
```

**De pipeline dwingt de verklaring af.** Een verplichte controle weigert gedragswijzigingen zonder documentatieaanpassing of uitzondering. Een menselijke documentatie-eigenaar beoordeelt de uitzondering. Een controle op gewijzigde paden vindt mogelijke wijzigingen, maar bewijst geen semantische volledigheid. Verplicht controle en beoordeling via branchbescherming of een vergelijkbare samenvoegingscontrole.

**Een controle die niet in de pipeline staat, is geen controle.** “Documentatiebeoordeling” noemen in een instructiebestand is alleen advies. Test de afdwinging met een bewust onvolledige PR en bevestig dat samenvoegen geblokkeerd blijft.

**Gebruik één taak, één branch en één worktree.** Git-worktrees bieden aparte werkmappen met eigen uitgecheckte status. Ze beperken lokale bewerkingsconflicten, maar verhinderen niet dat twee branches hetzelfde bestand aanpassen of twee agents één wikipagina bijwerken.

**Commit nooit rechtstreeks naar de standaardbranch**, of die nu `main`, `master` of anders heet. Meld verschillen tussen eis en code in de tracker. Voeg de tegenstrijdige records toe en laat de eigenaren het bedoelde gedrag bepalen voordat een van beide wordt aangepast. Pas vergelijkbare controles buiten Git toe.

## Informatie buiten de repository

**De wiki heeft een documentatiestandaard nodig.** Elke gezaghebbende pagina vermeldt doel, status, eigenaar, revisie, controledatum en gerelateerde bron-ID's. Zet voorstellen in een conceptgedeelte met een duidelijk niet-gezaghebbend label. Meng voorgestelde tekst niet met een goedgekeurde eisenpagina.

**Veilige updates volgen een vaste reeks:**

1. **Lees opnieuw** de huidige pagina en de omliggende voorwaarden.
2. **Vergelijk** de versie met de basisversie van het voorstel.
3. **Verwerk** tussentijdse wijzigingen en vraag opnieuw goedkeuring voor aangepaste tekst.
4. **Schrijf** de goedgekeurde revisie met een voorwaarde voor de verwachte versie.
5. **Controleer** de opgeslagen pagina en voeg de verwijzing naar het wijzigingslog toe.

**Opnieuw lezen voorkomt races niet.** Gebruik waar beschikbaar het voorwaardelijke updatemechanisme. Ontbreekt dat, laat één eigenaar publiceren en controleer het resultaat. Stop als iemand anders de basis tijdens de beoordeling wijzigt.

**De regel voor verwijderen geldt voor agentworkflows.** Agents stellen archiveren of verwijderen voor. Bevoegde mensen voeren bewaarbeleid en verwijderprocedures uit. Lees dit niet als toestemming om gevoelige informatie onbeperkt te bewaren.

**Trackerbevindingen bevatten bewijs**, niet alleen conclusies. Noteer wat je zag, het exacte commando of de inspectiemethode, de gecontroleerde commit, verwacht en werkelijk gedrag en acceptatiecriteria. Verwijder geheimen en gevoelige uitvoer voordat je bewijs toevoegt. Markeer voorgestelde opdrachten als niet uitgevoerd tot iemand ze uitvoert.

```text
Bevinding: implementatie van bewaartermijn wijkt af van goedgekeurde eis
Bewijs: REQ-17 v8 en gecontroleerde config/retention.yaml
Inspectiecommando: git show HEAD:config/retention.yaml
Commit: volledige gecontroleerde commit-ID staat in het manifest
Acceptatie: goedgekeurde duur komt overeen met code, tests en runbook
Status: wacht op beoordeling door product- en engineeringeigenaar
```

**Het voorbeeld is een sjabloon voor een bevinding**, geen gemeten resultaat. Vul het met echte inspectiegegevens. Koppel de wiki-update en het trackerbewijs via de voorstel-ID.

**Het besluitenregister scheidt regels van redeneringen.** Leg vraag, opties, aanbeveling, afwegingen, eigenaar, goedkeuringsstatus en verwijzing naar de resulterende regel vast. Agents stellen voor. Mensen beslissen. Goedgekeurde regels gaan in beleid en procedurele vaardigheden. De onderbouwing blijft in het register.

**Leg duurzame feiten uit vergaderingen en chats vast.** Dien een voorstel met bronbewijs in en vraag goedkeuring. Markeer de afspraak als voorlopig tot publicatie. Koppel daarna goedgekeurd gedrag tussen repository en wiki.

## Verbind de twee systemen

**Synchronisatie na samenvoegen brengt implementatiewijzigingen naar buiten.** Maak een wiki-updatetaak met verwijzingen naar de samengevoegde commit, goedgekeurde eis en betrokken runbook. Een agent stelt de update op. De wiki-eigenaar controleert de actuele pagina en keurt publicatie goed. Laat de synchronisatietaak open tot de opgeslagen revisie is gecontroleerd.

**Beleidsactualiteit is een aparte controle.** Vergelijk elke repositoryadapter en chatkopie van instructies met de canonieke goedgekeurde versie. Beleid `v3` staat op `POL-01`. Elke `AGENTS.md` noemt `v3` op regel één. De controle markeert `v2`, ontbrekende labels en inhoudsverschillen, zelfs als labels overeenkomen.

| Controle | Bewijs van voltooiing |
|---|---|
| **Beleidsactualiteit** | Canonieke versie en vergelijking van adapterdigest |
| **Vereisten afstemmen** | Revisie van de eis vergeleken met code en tests |
| **Synchronisatie na samenvoegen** | Samengevoegde commit gekoppeld aan gepubliceerde wikirevisie |
| **Conflicten oplossen** | Door eigenaar goedgekeurd besluit gekoppeld aan beide records |

**Stem af op een schema of pull request.** Een wekelijkse controle past bij een proef. Een gedragswijzigende PR vereist vóór samenvoegen een eisencontrole. Kies de frequentie op basis van de kosten van drift en noteer de laatste geslaagde controle.

**De wijziging naar dertig dagen heeft meerdere controlepunten:** product keurt de eis goed, engineering werkt configuratie en tests bij, beoordelaars voegen de PR samen en operations publiceert de runbookupdate. Eén rij in het wijzigingslog koppelt de resulterende records. Een mislukte wikisynchronisatie blijft zichtbaar en verdwijnt niet achter een geslaagde merge. Gedeelde overdrachten houden de reeks tussen tools intact.

## Eén werkwijze, elke tool

**Verpak herhaalde stappen als vaardigheden of prompts** met een versie-ID voor de procedure. Deel het contract, niet de aanname dat elke tool hetzelfde bestandsformaat gebruikt. Elke adapter gebruikt de ondersteunde laad- of aanroepmethode.

| Procedure | Vereiste uitvoer |
|---|---|
| **Taak starten** | Eigenaar, werkgebied, beleidsversie, bronmanifest, schrijfreservering |
| **Documentatielint** | Ontbrekende metadata, dubbel gezag, kapotte bronverwijzingen |
| **Kenniscontrole** | Verschillen tussen eis en code met ondersteunende revisies |
| **Overdracht** | Actueel bewijs, voorstellen, voltooide controles, open vragen |

**Niet-programmeurs werken zonder Git.** Ze halen toegestane bronnen op in chatprojecten, vullen hetzelfde voorstelsjabloon in en dienen het bij de eigenaar in via een conceptpagina of trackertaak. Een repositorycheckout is niet nodig om een eiscorrectie aan te vragen.

**Programmeurs gebruiken repositorybestanden en PR-controles.** Ze koppelen het goedgekeurde voorstel in de PR, noteren gecontroleerde commits en voeren de verplichte controles uit. Beide groepen dragen dezelfde bewijsstructuur over.

```yaml
handoff:
  task: EXP-42
  policy_version: 3
  manifest: "Attached source IDs, revisions, and inspected commit"
  completed: [requirement-review]
  proposals: [PROP-042]
  pending: [implementation-review, runbook-publication]
  reservations: ["RUN-04 publication assigned to operations-owner"]
  unresolved: []
  next_owner_role: engineering-maintainer
```

**Een overdracht is nog steeds een cache.** **De volgende persoon leest bronnen opnieuw vóór actie** en registreert nieuwe revisies. Vertrouw niet op “voltooid” zonder de gekoppelde goedkeuring of test te controleren. Pas vóór elke schrijfactie de waarborgen hieronder toe.

## Waarborgen vóór elke schrijfactie

**Controleer gegevens voordat ze het bronsysteem verlaten.** Bekijk classificatie, connectorrechten, toegestane bestemmingen, verwerking door de modelprovider en logging. Verstuur alleen de minimaal relevante inhoud. Plaats afgeschermde records niet in onbevoegde chatprojecten of embeddingdiensten.

**Opgehaalde tekst is bewijs, geen instructiekanaal.** Een wikipagina of toolantwoord dat een agent vraagt beleid te negeren, verandert het gezag niet. Beoordeel instructies uit inhoud apart van het goedgekeurde werkbeleid. Beperk retrievalconnectors tot leesrechten en scheid publicatierechten van sessietoegang.

**Wijs elke pagina of elk bestand **één actieve eigenaar** toe.** Leg de reservering met werkgebied en vervaltijd vast in de tracker. Lees opnieuw vóór schrijven en gebruik versiecontroles. Aparte worktrees helpen lokale isolatie; reserveringen en voorwaardelijke schrijfacties beschermen gedeelde records.

| Reden om te stoppen en te vragen | Vereiste reactie |
|---|---|
| **Bronnen spreken elkaar tegen zonder eigenaar** | Pauzeer en vraag wie gezag heeft |
| **Een andere taak reserveert het doel** | Spreek eigenaarschap af vóór bewerking |
| **Basisversie is gewijzigd** | Verwerk de wijziging en vraag opnieuw goedkeuring |
| **Een belangrijke bewering mist bewijs** | Markeer die als onbevestigd en vraag een bron |
| **Gegevensverwerking is onduidelijk** | Houd de inhoud in het bronsysteem |
| **Live toegang tot de bron werkt niet** | Noteer snapshotbeperkingen en pauzeer duurzame actie |

**Prompts zijn geen beveiligingscontroles.** Test toegangsweigering, beschermde branches, afwijzing van een verouderde basis en schrijfeigenaarschap buiten het model. Een keurige demonstratie volstaat niet als het account onbeperkt mag publiceren. Gebruik deze tests om te bepalen of de proef klaar is.

## Eerst een proef

**Start het kader als concept.** Test één project met een programmeur, niet-programmeur en benoemde broneigenaren. Stel dezelfde vraag met bekende ID via twee tools en voer daarna bewust een oefening met tegenstrijdige bronnen uit. **Beoordeel manifesten en voorstellen, niet de vloeiendheid van de tekst.**

**Verwachte redenering:** beide deelnemers vinden de actuele goedgekeurde eis en beschrijven apart de geïnspecteerde implementatie. Vergelijk eerst de manifestregels als ze verschillen. Dit is een voorgestelde oefening, geen gemeten benchmark.

| Maatstaf | Definitie |
|---|---|
| **Citeerpercentage** | Door bronnen gesteunde belangrijke beweringen gedeeld door feitelijke beweringen in steekproefuitvoer |
| **Wekelijkse driftbevindingen** | Bevestigde verschillen in gezag of versie, gegroepeerd per brontype |
| **Doorlooptijd van voorstellen** | Mediane tijd van beoordelingsklaar voorstel tot vastgelegd besluit |
| **Herwerk door verouderde context** | Heropende taken door verouderd of onbevestigd bewijs |

**Meet eerst een uitgangsniveau.** Meer driftbevindingen in week één kunnen betere detectie betekenen, geen slechtere documentatie. Volg herhaling en oplostijd naast het ruwe aantal. Beoordeel gevoelig bewijs zonder het naar analytics-exporten te kopiëren.

**Lever tijdens de uitrol een voorbeeldrepository op.** Voeg synthetische kaart, beleidsadapters, manifesten, voorstelsjablonen, documentatie-uitzonderingen en uitvoerbare controles toe. Gebruik nepwiki- en trackerrecords zonder productiegegevens. Demonstreer geweigerde publicatie, afwijzing van een gewijzigde basis, beleidsversiedrift en een geslaagde overdracht.

**Een sjabloonrepository hoort bij de uitrol**, maar wordt niet met dit artikel meegeleverd. Promoveer het werkmodel nadat leidinggevenden en broneigenaren de proefresultaten hebben beoordeeld. Bewaar uitzonderingen en onopgeloste fouten in het besluitenregister. Los vóór promotie de voorspelbare problemen hieronder op.

## Problemen met gedeelde context oplossen

| Symptoom | Eerste herstelactie |
|---|---|
| **Twee tools geven verschillende antwoorden** | Vergelijk bron-ID's, revisies, werkgebied en goedkeuringsstatus |
| **Instructies lijken actueel, gedrag wijkt af** | Controleer geladen adapters, regelinstellingen en lokale overschrijvingen |
| **RAG vindt oude vereisten** | Controleer indexvernieuwing en haal de live pagina op |
| **Een wiki-edit wist een andere wijziging** | Eis voorwaardelijke schrijfacties of geserialiseerde publicatie |
| **Documentatiecontroles slagen met oude tekst** | Voeg eigenaarbeoordeling en vereistenafstemming toe |
| **Besluiten blijven in chat** | Wijs voorstelinvoer en registereigenaarschap toe |

**Herstel het bewijspad voordat je de prompt herschrijft.** Voer daarna de mislukte proef opnieuw uit en registreer het resultaat. Gebruik de checklist om het herstelde proces wekelijks te herhalen.

## Tien stappen voor deze week

1. **Kies één proefproject** en de deelnemende mensen en tools.
2. **Wijs elk informatietype een bron en eigenaar toe.**
3. **Publiceer een projectkaart** met bron-ID's en gezagsgebieden.
4. **Stel gedeeld beleid op** en laat een eigenaar het beoordelen.
5. **Geef elke instructieadapter een versie** op regel één en controleer dat die laadt.
6. **Eis een contextmanifest** voor belangrijke feitelijke antwoorden en voorstellen.
7. **Maak een voorstelinvoerpad** met basisversies en benoemde goedkeurders.
8. **Dwing schrijfrechten en de documentatieregel voor dezelfde PR af.**
9. **Test drift, conflicten en overdracht** met synthetische records.
10. **Beoordeel proefmaatstaven** en keur de volgende uitrolfase goed.

**Geef elk feit één thuis, laat elke tool vanuit die bron lezen en laat een persoon elke duurzame wijziging beoordelen.**

## Referenties en vervolgstappen

**Officiële documentatie ondersteunt de technische onderdelen**, niet de organisatorische regels van dit kader. Controleer tijdens de proef het gedrag van geïnstalleerde tools en connectorrechten.

- **Codex-instructies:** [Aangepaste instructies met AGENTS.md](https://developers.openai.com/codex/guides/agents-md), over het vinden en controleren van instructies.
- **Claude Code-instructies:** [Hoe Claude je project onthoudt](https://code.claude.com/docs/en/memory), over projectinstructies en geheugen.
- **Cline-instructies:** [Regels](https://docs.cline.bot/customization/cline-rules), over werkruimteregels en activeringsinstellingen.
- **Retrievalontwerp:** [RAG met Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview), over grounding, retrievalbeperkingen en beveiliging.
- **Connectorbeveiliging:** [MCP-beveiligingsrichtlijnen](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices), over autorisatie en connectorrisico's.
- **Worktree-isolatie:** [Git-worktreedocumentatie](https://git-scm.com/docs/git-worktree), over afzonderlijke werkmappen en gedeelde repositorystatus.

**Lees voor lokale inferentieplanning** de [Gids voor lokale AI-GPU-context](/articles/local-ai-model-gpu-context-guide/). Hardwarecapaciteit en beheer van gedeelde bronnen lossen verschillende problemen op. Een groter contextvenster herstelt geen tegenstrijdig gezag.

{{< centerbutton href="/articles/local-ai-model-gpu-context-guide/" >}}
  Lees de gids voor lokale AI-context
{{< /centerbutton >}}
