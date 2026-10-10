---
title: "10 Claude Code-plug-ins, skills en MCP-tools: praktische gids"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Kies Claude Code-extensies voor planning, code review, kennisbeheer, ontwerp en automatisering. Vergelijk tien tools, afhankelijkheden en praktische controles."
genre: ["Kunstmatige intelligentie", "Ontwikkelaarstools", "Softwareontwikkeling"]
tags: ["Claude Code-plug-ins", "Claude Code-skills", "MCP-tools", "Graphify", "grill-me", "grill-with-docs", "grill-me-codex", "Claudex Loop", "Codex-plug-in", "code review", "claude-obsidian", "Obsidian", "CLAUDE.md", "Karpathy-richtlijnen", "Impeccable", "Higgsfield", "NotebookLM", "notebooklm-py", "n8n MCP", "AI-ontwikkelworkflow", "agentinstructies", "kennisgrafieken"]
cover: "/img/cover/claude-code-plugins-workflow-management-tools.webp"
coverAlt: "Blauwe en paarse toolpictogrammen, mappen en abstracte grafiekpanelen verbonden met een geometrisch middelpunt op een donkere achtergrond"
coverCaption: "Conceptuele illustratie van een workflow. Grafiekvormen staan niet voor gemeten resultaten."
---

**Kies een Claude Code-extensie rond één concreet probleem in je workflow.** Onduidelijke vereisten vragen om een planningsgesprek. Gemiste fouten vragen om review en tests. Herhaald onderzoek vraagt om traceerbare bronnen. Meer tools installeren helpt alleen wanneer hun verantwoordelijkheden duidelijk zijn.

Deze gids vergelijkt **tien projecten** voor deze taken, met installatievoorbeelden en een uitgewerkte evaluatie. De analyse gebruikt actuele projectdocumentatie en de aangeleverde Chase AI-video. Aanbevelingen zijn redactionele beoordelingen. Ze zijn geen prestatiemetingen of bewijs van tien keer hogere productiviteit.

<!--more-->

## Belangrijkste punten

- **Kies op basis van de uitvoer:** een gereviewd plan, een codemap en een gegenereerde afbeelding vragen om verschillende tools.
- **Scheid installatielagen:** instructies, uitvoerbare programma's, plug-ins en serviceverbindingen hebben verschillende afhankelijkheden.
- **Controleer actuele namen:** Graphify en grill-me-codex hebben nu verschillende canonieke repositorylocaties.
- **Ga verder dan overeenstemming:** twee modellen die een plan accepteren bewijzen niet dat de implementatie klopt.
- **Meet geaccepteerd werk:** neem installatie, servicegebruik, mislukte pogingen en menselijke correcties mee.

## Voor je begint

**Vereisten:** een werkende Claude Code-installatie, een wegwerpbaar project of branch en toestemming voor de gekozen externe diensten. CLI-voorbeelden gaan uit van een terminal en de genoemde pakketbeheerder. Cloudintegraties vereisen eigen accounts en authenticatie.

**Geschatte tijd:** 15 minuten lezen, daarna 30 tot 60 minuten voor één afgebakende proef. **Moeilijkheid:** gemiddeld voor CLI-installatie en service-integratie. Instructieskills lezen vraagt minder voorbereiding.

**Documentatie gecontroleerd op 10 oktober 2026.** Commando's en toegangsregels volgen de gekoppelde bronnen. Controleer je geïnstalleerde versie opnieuw voordat je een oudere tutorial volgt. Dit artikel behandelt extensies vanuit Claude Code en noemt relevante verschillen tussen hosts.

**Controleer na installatie laag voor laag.** Controleer bestanden, hostdetectie, uitvoerbare afhankelijkheden, inloggegevens en één representatieve taak afzonderlijk. Een geslaagde installer bewijst niet dat een browser, MCP-server, mediatool of extern account werkt. Gebruik synthetische gegevens voor de eerste test en noteer de upstream-revisie.

## Ken het type extensie

| Type | Rol | Voorbeeld |
|---|---|---|
| **Instructiebestand** | Stelt blijvende projectverwachtingen vast | CLAUDE.md |
| **Skill** | Levert een procedure voor een gekozen taak | grill-me |
| **Plug-in** | Bundelt geregistreerde commando's en integraties | Codex-plug-in |
| **CLI** | Voert commando's uit vanuit een terminal | Graphify |
| **MCP-server** | Stelt aanroepbare tools beschikbaar aan een agentclient | n8n-instantie-integratie |

Het **Model Context Protocol (MCP)** verbindt een agentapplicatie met tools en gegevens die een server beschikbaar stelt. Een command-line-interface, of **CLI**, voert uitvoerbare commando's uit. Een skill leert een agent vaak hoe één van beide interfaces te gebruiken, maar aanwezigheid bewijst geen werkende verbinding.

**Begin met de ontbrekende mogelijkheid.** Heeft je agent al repositoryzoeking, dan moet een nieuwe zoekprocedure een zichtbaar voordeel geven. Ontbreekt toegang tot een automatiseringsplatform, dan levert een tekstbestand met instructies geen geauthenticeerde toegang. De [gids voor agent-runtimes](/articles/best-ai-agent-harnesses/) beschrijft de software rond modelaanroepen en tooluitvoering.

## Kies je eerste tool

| Probleem | Tool | Eerste acceptatiecontrole |
|---|---|---|
| **Onduidelijke vereisten** | grill-me / grill-with-docs | Expliciete beslissingen en acceptatiecriteria |
| **Herhaalde scopeverschuiving** | Karpathy-geïnspireerde CLAUDE.md | Elke wijziging dient de gevraagde verandering |
| **Riskant implementatieplan** | Claudex Loop | Reviewbevindingen opgelost met bewijs |
| **Niet-gereviewde codewijzigingen** | OpenAI Codex-plug-in | Bevindingen gekoppeld aan code en foutgevallen |
| **Onbekende repository** | Graphify | Relaties stemmen overeen met bronbestanden |
| **Verspreide projectkennis** | claude-obsidian | Claims behouden links naar originele bewijzen |
| **Herhaalde bronanalyse** | notebooklm-py | Antwoorden verwijzen naar bedoelde bronnen |
| **Onduidelijke interface** | Impeccable | Gebruikers voltooien de bedoelde interactie |
| **Ontbrekende visuele assets** | Higgsfield | Uitvoer past bij de goedgekeurde briefing |
| **Herhaalbare serviceworkflow** | n8n MCP | Testuitvoering levert het verwachte resultaat |

**Aanbevolen startpunt:** kies één rij en bewaar een basistaak vóór installatie. Voeg een tweede tool alleen toe wanneer die een afzonderlijke, meetbare bijdrage levert.

## Verduidelijk het werk

### grill-me en grill-with-docs

**De skills van Matt Pocock** zetten een onvoldoende uitgewerkt idee om in beslissingen. Het [grill-me-startpunt](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) roept de gedeelde interviewskill aan. [grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) roept interview en domeinmodellering aan. De [collectiedocumentatie](https://github.com/mattpocock/skills) beschrijft gedeelde terminologie en architectuurbesluiten naast het interview.

**Gebruik de documentatievariant** wanneer bedrijfstermen de implementatie beïnvloeden. Bepaal bij een illustratieve CSV-importer of een bestaande klant dezelfde e-mail, hetzelfde externe ID of beide betekent. Leg de keuze vast voordat je duplicaatdetectie schrijft.

**Houd het interview proportioneel.** Een nuttige sessie lost belangrijke onzekerheid op. Het interview hoort geen antwoorden te herhalen die al in de repository staan. Eindig met een plan, openstaande vragen en zichtbare voltooiingscontroles.

### Karpathy-geïnspireerde CLAUDE.md

**De door Multica onderhouden richtlijnen** vertalen Karpathy's observaties naar vier thema's: expliciete aannames, eenvoudige oplossingen, gerichte wijzigingen en verifieerbare doelen. De [repository](https://github.com/multica-ai/andrej-karpathy-skills) is een community-implementatie die op zijn observaties is geïnspireerd. Het project Karpathy's persoonlijk onderhouden plug-in noemen zou de herkomst verkeerd weergeven.

**Voeg bruikbare richtlijnen toe aan bestaand projectbeleid.** Behoud buildcommando's, contentconventies en implementatiebeperkingen. Een vervangend instructiebestand dat deze details verwijdert, creëert nieuwe fouten.

**Voorbeeld van een projectregel:** eis dat een wijziging aan de importer bestaande duplicaatafhandeling behoudt en elke bewuste wijziging met een fixture uitlegt. Instructies beschrijven verwachtingen. Tests en runtimecontroles leveren afzonderlijk bewijs.

| Planningsartefact | Doel |
|---|---|
| **Vereiste** | Benoemt de zichtbare uitkomst voor de gebruiker |
| **Begrip uit de woordenlijst** | Geeft een dubbelzinnige term één betekenis |
| **Besluitregistratie** | Bewaart de reden voor een belangrijke keuze |
| **Acceptatiecontrole** | Bepaalt hoe voltooiing wordt beoordeeld |

## Review plannen en code

### grill-me-codex, nu Claudex Loop

**Claudex Loop** is de huidige bestemming van de oorspronkelijke grill-me-codex-repository. De [documentatie](https://github.com/chaseai-yt/claudex-loop) beschrijft repositoryverkenning, vereisten, review door de andere provider, implementatie en onafhankelijke inspectie. De volledige loop vereist beide CLI's en Python 3.10 of hoger.

**Gebruik Claudex Loop voor plannen met grote gevolgen** waarvan aannames vóór implementatie moeten worden uitgedaagd. De huidige workflow ondersteunt starten vanuit Claude Code of Codex. De workflow legt bevindingen en beslissingen vast en scheidt reviewbevoegdheid van bouwbevoegdheid. De oudere videobeschrijving met vijf rondes vervangt het actuele rondebudget niet.

**Vraag bewijs bij elke tegenwerping.** Een review van de CSV-importer hoort een concreet duplicaat of retrygeval en het verwachte gedrag te noemen. Modelovereenstemming is een reviewuitkomst, geen bewijs. Bewaar openstaande bevindingen wanneer het reviewbudget op is.

### OpenAI Codex-plug-in

```text
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

**OpenAI's Codex-plug-in voor Claude Code** voegt code review en taakdelegatie toe binnen Claude Code. Dit zijn Claude Code-commando's, geen shellcommando's. De [officiële repository](https://github.com/openai/codex-plugin-cc) documenteert Node.js 18.18 of hoger en geauthenticeerde Codex-toegang via ChatGPT of een OpenAI API-sleutel.

```text
/codex:review --background
/codex:status
/codex:result
```

**Gebruik gewone review** voor actuele wijzigingen of een branchvergelijking. Gebruik **`/codex:adversarial-review`** voor een gerichte uitdaging. Delegatiecommando's zoals **`/codex:rescue`** doen ander werk dan een alleen-lezen-review. Benoem de bedoelde bevoegdheid.

**Begroot Codex-gebruik afzonderlijk.** Het project noemt ChatGPT Free als ondersteund account, maar gebruikslimieten blijven gelden. Installatie van de plug-in levert geen onbeperkte toegang.

**Keuzeregel:** gebruik een afgebakende plug-in-review voor een bestaande patch. Kies de grotere loop wanneer vereisten en planherziening een eigen vastgelegd proces nodig hebben.

## Behoud bruikbare context

### Graphify

```bash
uv tool install graphifyy
graphify install --project
graphify extract . --code-only
graphify query "show the authentication flow"
```

**Graphify** zet repositoryrelaties om in een doorzoekbare kennisgrafiek. De [canonieke repository](https://github.com/Graphify-Labs/graphify) staat nu onder Graphify-Labs. De pakketnaam is **`graphifyy`**, met twee y's aan het einde. Het uitvoerbare bestand blijft **`graphify`**.

**Code-only-extractie** gebruikt lokale abstracte syntaxanalyse om de codestructuur te lezen. Document- en media-interpretatie gebruikt een afzonderlijk modelpad. Breid claims over lokale privacy of kosten niet uit naar elke modus.

**Optionele hooks** bouwen de codegrafiek opnieuw na commits en branchwissels. Na een pull of merge gebruikt de gedocumenteerde workflow **`graphify update .`**. Documentatiewijzigingen vragen ook om een aparte verversing. Obsidian-export biedt een andere grafiekweergave.

**Gebruik Graphify voor relatievragen** en inspecteer daarna de relevante bron. Een grafiek helpt bij bestandsselectie. Grafiekstructuur bewijst geen runtimegedrag en vervangt geen tests. Meet tokensparing op je eigen vragen, inclusief grafiekbouw en onderhoud.

### claude-obsidian

**claude-obsidian** ordent bronmateriaal in gekoppelde, geciteerde Obsidian-pagina's. De [repository](https://github.com/AgriciDaniel/claude-obsidian) beschrijft opname, ophalen, kennisonderhoud, bronbehoud en registraties van steun of tegenspraak. De vault blijft uit gewone lokale bestanden bestaan.

**Gebruik claude-obsidian voor blijvende projectkennis:** ontwerpbesluiten, brondocumenten en onderzoeksnotities die losse gesprekken moeten overleven. De nuttige uitvoer is een onderhoudbaar record met herkomst, dus een traceerbare oorsprong voor elke belangrijke claim.

**Review de vault na opname.** Kies enkele claims en volg hun citaten terug naar het oorspronkelijke materiaal. Bewaar tegenstrijdig bewijs in plaats van verschil samen te voegen tot een zeker klinkende samenvatting. Lokale opslag bewijst geen lokale inferentie. Controleer host en modelconfiguratie vóór je gevoelige documenten aanbiedt.

| Contextsysteem | Eerste nuttige vraag |
|---|---|
| **Graphify** | Welke broncomponenten zijn verbonden? |
| **claude-obsidian** | Welk bewaard bewijs ondersteunt dit besluit? |
| **notebooklm-py** | Wat zeggen deze geselecteerde onderzoeksbronnen? |

### notebooklm-py

```bash
uv tool install "notebooklm-py[browser]"
notebooklm login
notebooklm auth check --test --json
notebooklm skill install
```

**notebooklm-py** levert een Python-bibliotheek, CLI en agentskill voor Google's notebookonderzoeksdienst. Het [project](https://github.com/teng-lin/notebooklm-py) beschrijft bronimport, onderbouwde vragen, gegenereerde artefacten en batchdownloads. De browser-extra ondersteunt de interactieve loginflow.

**Dit is een onofficiële integratie.** De bibliotheek gebruikt ongedocumenteerde Google-interfaces en blijft gevoelig voor breuken en rate limits. Beschrijf de bibliotheek niet als een door Google ondersteunde publieke API.

**Gebruik notebooklm-py voor een afgebakend onderzoekscorpus**, zoals release notes en migratiegidsen voor één afhankelijkheid. Controleer citaten tegen de brontekst voordat je bevindingen in een plan opneemt. Bescherm opgeslagen authenticatiestatus als accounttoegangsmateriaal.

**Onderzoek uitbesteden verandert waar het werk draait.** Het verwijdert geen orkestratietokens, servicequota, reviewwerk of verplichtingen rond gegevensverwerking. Behandel tokensparing als een te verzamelen meting, niet als een automatisch installatiekenmerk.

## Ontwerp en genereer assets

### Impeccable

```text
/impeccable critique settings
/impeccable audit settings
/impeccable polish settings
```

**Impeccable** levert ontwerptaal voor gericht interfacewerk. De [documentatie](https://github.com/pbakaus/impeccable) behandelt kritiek, layout, typografie, toegankelijkheidscontroles, beweging en visuele browseriteratie. De voorbeelden veronderstellen een geïnstalleerde skill en een project met een instellingenoppervlak.

**Begin met een interactieprobleem.** Vraag bij de importer waarom gebruikers validatiefouten missen of de keuze voor duplicaatbeheer verkeerd begrijpen. Review voorgestelde wijzigingen vóór een visuele afwerking. Aantrekkelijke ruimte lost geen onduidelijke actie op.

**Live iteratie** helpt alternatieven in de browser vergelijken. Controleer toetsenbordnavigatie, mobiele layout, foutmeldingen en contrast. Het aantal commando's verandert per release. Gebruik de lijst uit je geïnstalleerde versie in plaats van het videom aantal te onthouden.

### Higgsfield

**Higgsfields MCP-integratie** koppelt agents aan de beeld- en videogeneratiedienst. De [officiële integratiepagina](https://higgsfield.ai/mcp) noemt Claude Code en CLI-verbindingsopties. Gebruik de actuele setupflow voor je account en interface.

**Kies Higgsfield wanneer de ontbrekende oplevering media is.** Geef vóór varianten worden gegenereerd verhouding, compositie, merkregels en plaatsing op. Houd de visuele briefing gescheiden van pagina-implementatie.

**Controleer toegang en verbruik eerst.** Een integratielijst bewijst geen toegang tot elk model, onbeperkte generatie of een specifiek commercieel gebruiksrecht. Controleer accountvoorwaarden en het gekozen model vóór een productieflow.

**Review het eindbestand** op de bedoelde schermgrootte. Controleer zichtbare tekst, ongewenste symbolen, uitsnede en productconsistentie. Gegenereerde terminalschermen en diagrammen vormen geen bewijs van een geslaagde test.

| Ontwerpopdracht | Bewijs van voltooiing |
|---|---|
| **Interfaceherziening** | Vereiste acties werken op de doelviewports |
| **Afbeeldingsasset** | Afmetingen, uitsnede en inhoud passen bij de briefing |
| **Videoasset** | Timing, beweging en eindexport passen bij de briefing |

## Verbind herhaalbare workflows

### n8n MCP

**n8n's ingebouwde MCP-server** stelt workflowbewerkingen beschikbaar aan verbonden clients. De [actuele verbindingsdocumentatie](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) behandelt Cloud- en self-hosted-instanties. Workflowbouw en -bewerking zijn gedocumenteerd vanaf n8n 2.13.0. Dit artikel verwijst naar n8n's eigen server, niet naar een los communitypakket met een vergelijkbare naam.

**Gebruik instanceniveau-toegang** voor de integratie hier. Het MCP Server Trigger-knooppunt heeft een andere scope: tools uit één workflow. Controleer de [toolreferentie](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference) tegen je uitgerolde versie.

**Schakel toegang bewust in.** Bestaande workflows vragen MCP-blootstelling voor volledige toegang. Zoekvoorbeelden hebben binnen bestaande gebruikersrechten bredere zichtbaarheid. Workflowblootstelling is geen afzonderlijke clientallowlist, terwijl clientrechten de bewerkingen wel sturen.

**Controleer de uitvoermodus.** De gedocumenteerde standaard van **`execute_workflow`** voert de gepubliceerde productieversie uit. Handmatige modus voert de huidige ongepubliceerde versie uit. Controleer invoer en vervolgbewerkingen vóór uitvoering.

**Goede eerste proef:** classificeer synthetische supportvragen en schrijf resultaten naar een testbestemming. Controleer ontbrekende velden en retries. Self-hosting vraagt nog steeds rekenkracht, onderhoud en eventuele betaalde downstreamdiensten.

## Voer een gecontroleerde proef uit

**Illustratieve oefening:** voeg een CSV-importer toe aan een kleine applicatie. De importer toont rijen vooraf, meldt ongeldige e-mailvelden en voorkomt dubbele creatie. Klantrecords of live externe bestemmingen zijn niet nodig.

```yaml
# Evaluation worksheet, not a tool configuration file
task: "add CSV import preview"
inputs:
  - "valid rows"
  - "invalid email field"
  - "repeated customer identifier"
  - "same import submitted twice"
acceptance:
  - "preview creates no records"
  - "invalid rows receive useful messages"
  - "duplicate policy matches the written requirement"
  - "repeat submission creates no extra records"
record:
  - "source revision and selected skill version"
  - "model and service configuration"
  - "elapsed time and billed usage"
  - "failed checks and human corrections"
```

**Leg eerst de nulmeting vast.** Sla de beginrevisie op en laat de agent de taak met je bestaande workflow uitvoeren. Voer onafhankelijke acceptatiecontroles uit en bewaar het resultaat. Herhaal vanaf dezelfde revisie met één extensie en dezelfde vereisten.

**Stem het experiment af op het vermoede probleem.** Wordt duplicaatbeheer herhaaldelijk verkeerd begrepen, test dan een requirementskill. Mist de agent een bestaande validator, test dan repositorymapping. Missen gebruikers fouten, test dan interfacekritiek. Alle tien tools tegelijk laden verhindert toeschrijving van verbetering.

**Verwachte redenering:** een geslaagde tweede poging is nuttig bewijs, maar één run bewijst geen algemene productiviteitsvermenigvuldiger. Herhaalde runs scheiden toolwaarde van modelvariatie. Vergelijk geaccepteerde resultaten, inclusief reviewwerk en mislukte pogingen.

| Observatie | Interpretatie |
|---|---|
| **Sneller antwoord, tests mislukt** | Kortere reactietijd zonder afgeronde taak |
| **Langere run, minder correcties** | Mogelijk voordeel in totale opleverinspanning |
| **Twee reviewers zijn het eens** | Overeenstemming die onafhankelijke verificatie vereist |
| **Minder agentgebruik, nieuwe servicekosten** | Kosten verschoven tussen providers |

**Maak een blijvende besluitregistratie.** Noteer probleem, gekozen tool, waargenomen voordeel, openstaand probleem en voorwaarden voor een nieuwe proef. Behoud een tool wanneer de bijdrage deze controle doorstaat. Een grote geïnstalleerde verzameling vereist geen grote actieve workflow.

## Problemen oplossen

| Symptoom | Volgende controle |
|---|---|
| **Skill bestaat maar commando faalt** | Uitvoerbare installatie, PATH en vereiste nevenbestanden |
| **Oude tutorialnamen missen commando's** | Geïnstalleerde versie en canonieke upstreaminstructies |
| **Grafiek mist recente wijzigingen** | Grafiekversheid en aparte documentverversing |
| **Reviewer herhaalt opgeloste bezwaren** | Exacte planrevisie, bewijs en reviewbudget |
| **Notebookauthenticatie faalt** | Authdiagnose, sessiegeldigheid en upstreamproblemen |
| **n8n-verbinding mist verwachte bewerkingen** | Uitgerolde versie, blootstellingsinstellingen en rechten |
| **Ontwerp ziet er beter uit maar werkt slechter** | Oorspronkelijke acceptatiecriteria en interactiecontroles |

**Controleer installatielagen in deze volgorde:** bestanden aanwezig, hostdetectie, afhankelijkheden gereed, authenticatie werkend en representatieve taak geverifieerd. Een geslaagde installer bewijst maar een deel van de keten.

**Controleer overlappende skills vóór je nog een kopie toevoegt.** Requirementsinterviews, planningssuites, designtools en reviewpakketten hebben soms concurrerende standaarden. Kies één primaire procedure en voeg ondersteunende tools toe voor benoemde bijdragen. Behoud repositorybeleid en gevraagde scope.

## Videowalkthrough

{{< youtube id="IShdbDP4Jgg" enable="true" title="The Top 10 Claude Code Plugins to 10x Your Next Project (June '26)" >}}

**De walkthrough van Chase AI** introduceert de tien besproken projecten. [Bekijk de originele video](https://www.youtube.com/watch?v=IShdbDP4Jgg) voor demonstraties. Gebruik projectdocumentatie voor actuele installatie en werking. De videotitel is een promotionele claim, geen gemeten resultaat uit deze gids.

## Volgende stappen

**Kies één terugkerend probleem en één acceptatietest.** Test de passende extensie op een wegwerpproject en behoud daarna de kleinste combinatie die het resultaat verbetert. Voeg kennisbeheer, mediageneratie of automatisering toe wanneer het werk deze uitvoer nodig heeft.

**Lees voor verwante richtlijnen** de [vergelijking van CLI-codeagents](/articles/cli-coding-agents-comparison/) bij je agentkeuze. Gebruik de [cursus AI-samenwerking](/ai-collaboration-course-start/) voor praktisch werk rond vereisten, bewijs en reviewverantwoordelijkheden.

{{< centerbutton href="/ai-collaboration-course-start/" >}}
Lees de cursus AI-samenwerking
{{< /centerbutton >}}

## Referenties

- [Graphify: codegrafieken en installatie](https://github.com/Graphify-Labs/graphify)
- [Matt Pocock: skillcollectie](https://github.com/mattpocock/skills)
- [Claudex Loop: huidig grill-me-codex-project](https://github.com/chaseai-yt/claudex-loop)
- [OpenAI: Codex-plug-in voor Claude Code](https://github.com/openai/codex-plugin-cc)
- [claude-obsidian: brongekoppeld kennisbeheer](https://github.com/AgriciDaniel/claude-obsidian)
- [Multica: Karpathy-geïnspireerde coderichtlijnen](https://github.com/multica-ai/andrej-karpathy-skills)
- [Impeccable: ontwerpcommando's en installatie](https://github.com/pbakaus/impeccable)
- [Higgsfield: agentintegratie](https://higgsfield.ai/mcp)
- [notebooklm-py: onofficiële bibliotheek, CLI en skill](https://github.com/teng-lin/notebooklm-py)
- [n8n: officiële MCP-verbindingsgids](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)
