---
title: "AI-agenten delegeren: taken verdelen en resultaten beoordelen"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Bepaal wanneer een tweede AI-agent helpt, geef elke werker een afgebakende taak, voorkom bewerkingsconflicten en voeg bewijs samen in de hoofdsessie."
genre: ["Kunstmatige intelligentie", "Software-engineering"]
tags: ["AI-agentdelegatie", "subagenten", "werker-agenten", "context van de orkestrator", "AI-werkmappen", "parallelle AI-taken"]
cover: "/img/cover/effective-ai-agent-delegation.webp"
coverAlt: "Een hoofdagent wijst afzonderlijke onderzoeks- en testbeoordelingstaken toe en combineert daarna korte bewijsrapporten"
coverCaption: ""
---

[Terug naar de praktische AI-werkstroomcursus](/effective-ai-course-start/)

**Delegeer wanneer een onafhankelijke vraag genoeg werk oplevert voor een aparte sessie.** Een werker-agent onderzoekt bronnen, beoordeelt tests of maakt binnen de eigen context een afgebakende wijziging. De hoofdagent controleert en integreert het resultaat. Deze les vergelijkt documentatie terwijl je hoofdsessie de kleine labtaak behoudt.

**Leerdoel:** je wijst een onafhankelijke beoordeling toe aan een werker en controleert diens korte bewijsrapport.

## Belangrijkste punten

- **Orkestrator:** de hoofdagent die de taak en eindbeoordeling coördineert.
- **Werker:** een aparte agent met één afgebakend resultaat.
- **Onafhankelijk werk:** een subtaak waarvan het antwoord niet afhangt van het onvoltooide resultaat van een andere werker.
- **Eigenaarschap:** een benoemd bestand of een vraag die aan één werker is toegewezen.
- **Integratie:** de hoofdagent vergelijkt de uitvoer van de werker met actuele bronnen.

## Voordat je begint

**Vereisten:** je registraties voor [contextoverdracht](/articles/effective-ai-context-window-management/) en [uitvoercontrole](/articles/effective-ai-output-verification/). Reserveer 40 minuten. Gemiddelde moeilijkheid. De verbonden route vereist een product met werkerondersteuning. De studieroute gebruikt een aparte chat en handmatige integratie.

**Begin voor deze les met een schone starter.** Bewaar de diff van het bewerkte filter en het testverslag buiten het lab. Pak de oorspronkelijke ZIP uit in een nieuwe tijdelijke map. Voer het startercommando en de twee basistests uit. Herhaal de Git-basislijn uit de cursusinstellingsles en maak de korte `AGENTS.md`- en optionele `CLAUDE.md`-instructies uit de les over repositorycontext opnieuw. Commit deze instructiebestanden zelf en controleer daarna dat `git status --short` schoon is. Bewaar de aangepaste filterkopie als referentie, maar voer de werkeropdracht uit op de schone starter.

## Bepaal of je moet delegeren

**Gebruik één agent** voor een kleine opeenvolgende bewerking. Delegeren kost voorbereiding, tokens en beoordeling. Gebruik een werker als een onafhankelijke vraag die alleen lezen vereist anders veel bestanden of bronpagina's in de hoofdchat zou brengen.

| Labtaak | Delegeren? | Reden |
|---|---|---|
| **Een filter met twee waarden toevoegen** | Meestal niet | Eén klein bestand en gerichte tests |
| **Ontbrekende gevallen vinden in twee basistests** | Meestal niet | De hoofdsessie leest één kort bestand sneller |
| **Actuele documentatie van drie producten vergelijken** | Ja, alleen lezen | Bronnen blijven in de context van de werker |
| **Dezelfde functie tweemaal bewerken** | Nee | Gelijktijdige bewerkingen veroorzaken conflicten |

**De werker hoort minder context te krijgen dan de orkestrator,** niet een kopie van het hele gesprek. Geef het doel, het bronpad, de taakgrens en het antwoordformaat. Bewaar een kort bewijsrapport in de hoofdsessie. Controleer geciteerde bestanden zelf voordat je handelt.

## Start één werker die alleen leest

**Houd de hoofdtaak klein.** Lees in je hoofdsessie de lokale `AGENTS.md` en noteer welk bestand het testcommando bevat. Wijs de aparte onderzoeksvraag hieronder toe aan één werker. De werker heeft niet het hele lab of de eerdere chat nodig.

**Verbonden route:** open het lab als project in Codex, Claude Code of een andere client met werkerondersteuning en vraag de hoofdagent het volgende leesverzoek aan één werker toe te wijzen. Controleer in het tooltranscript of een echte werker is gestart en een rapport heeft teruggestuurd. Als het product geen werker toont, gebruik dan een aparte sessie en benoem die als afzonderlijke werkersessie. De actuele handleidingen voor [Codex-subagenten](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Claude Code-subagenten](https://code.claude.com/docs/en/sub-agents) en [OpenCode-agenten](https://opencode.ai/docs/agents/) beschrijven de huidige instellingen.

**Studieroute:** open een nieuwe chat voor hetzelfde verzoek. Geef de drie officiële links of bronfragmenten. Noem dit een gesimuleerde werker. Een tweede chat is een aparte context, geen bewijs van een native subagent.

```text
Gebruik de actuele officiële documentatie Codex AGENTS.md, Claude Code memory en OpenCode rules.
Vergelijk hoe elk product repository-instructiebestanden laadt.
Bewerk geen bestanden.
Geef hoogstens drie rijen: product, instructiebestand, bron-URL en één laadgedrag.
Vermeld onzekerheid. Plak geen volledige pagina's.
```

**Bronnen:** [Codex-projectinstructies](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Claude Code-geheugengids](https://code.claude.com/docs/en/memory) en [OpenCode-regels](https://opencode.ai/docs/rules/). Het verwachte rapport noemt `AGENTS.md` voor Codex en OpenCode. Huidige Claude Code-versies laden `AGENTS.md` ook rechtstreeks als `CLAUDE.md` of `CLAUDE.local.md` geen voorrang krijgt. Dit lab gebruikt een `CLAUDE.md`-bestand met een `@AGENTS.md`-import, wat ook oudere of anders ingestelde sessies ondersteunt. Controleer de actuele pagina's en actieve versie voordat je dit voorbeeld presenteert als waargenomen uitvoer van een werker.

## Integreer de bevindingen

**Open de geciteerde bronpagina's zelf.** Als de werker beweert dat Claude Code altijd een `CLAUDE.md`-import vereist, controleer dan de memory-handleiding en corrigeer het rapport. Vergelijk het met je lokale instructiebestanden. Schrijf een korte integratienotitie:

```text
Geaccepteerd: Codex en OpenCode gebruiken AGENTS.md voor projectinstructies.
Huidige Claude Code-versies kunnen AGENTS.md rechtstreeks laden. Dit lab gebruikt
CLAUDE.md met een @AGENTS.md-import voor een stabiele gedeelde kaart.
Bewijs: noteer de drie actuele officiële URL's en de beoordelingsdatum.
Besluit: behoud een korte gedeelde kaart en een Claude-import.
```

**Deze notitie is de bruikbare werkeruitvoer.** De orkestrator heeft gecontroleerde bevindingen en bronpaden nodig, niet het onderzoekstranscript. Delegeren kost in totaal meer tokens. Houd het hoofdgesprek alleen kleiner als de aparte sessie aandacht bespaart.

## Wijs eigenaarschap van bewerkingen toe

**Als werkers bestanden bewerken,** verdeel dan eigenaarschap per bestand of gebruik aparte worktrees voor overlappend repositorywerk. Een worktree is een extra kopie van dezelfde Git-repository met eigen werkbestanden. Dat houdt gelijktijdige bewerkingen gescheiden. De hoofdagent beoordeelt en verplaatst wijzigingen met een expliciete merge, cherry-pick of patch, en voert daarna de tests opnieuw uit in de geïntegreerde boom.

| Werker | Toegewezen werk | Retourneer |
|---|---|---|
| **Implementatie** | `task_report.py` | Diff en testcommando |
| **Testauteur** | `tests/test_task_report.py` | Testgevallen en waargenomen resultaat |
| **Orkestrator** | Vereisten en eindintegratie | Gecombineerde diff en acceptatiecriteria |

**Het kleine lab heeft geen parallelle bewerkingen nodig.** Deze tabel laat een eigenaarschapsmodel voor groter werk zien. Tests in de ene worktree valideren geen implementatie die in een andere worktree geïsoleerd blijft. Als twee werkers dezelfde functie nodig hebben, werk dan na elkaar of laat één werker alleen beoordelen. Aparte worktrees voorkomen bestandsbotsingen, maar lossen tegenstrijdige vereisten niet op.

## Controleer productgedrag

**Subagenten verschillen per host.** Codex, Claude Code en OpenCode verschillen in contextoverdracht, toolrechten en resultaatbezorging. Lees voor het geïnstalleerde product de handleidingen voor [Codex-subagenten](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Claude Code-subagenten](https://code.claude.com/docs/en/sub-agents) en [OpenCode-agenten](https://opencode.ai/docs/agents/). Ga er niet van uit dat een werker alle context van de hoofdsessie deelt of een geïsoleerde worktree krijgt.

## Oefen en controleer

**Je resultaat:** één kort documentatierapport van een werker en één integratienotitie. Gebruik op de studieroute een nieuwe chat en benoem die als gesimuleerde werker. Claim niet dat een native subagent is uitgevoerd.

**Afrondingscontrole:** het rapport noemt drie officiële bronnen, blijft binnen de vraag en respecteert de lengte. De integratienotitie controleert de bronnen en noemt de instructiebestanden die het lab gebruikt.

## Controleer je begrip

1. **Vraag:** Wanneer helpt een werker meer dan één agent? **Antwoord:** Als de werker een onafhankelijke vraag of resultaat bezit en een bruikbaar bewijsrapport levert.

2. **Vraag:** Wat moet gebeuren nadat twee werkers overlappende bestanden wijzigen? **Antwoord:** Integreer de wijzigingen, bekijk de gecombineerde diff en voer de controles opnieuw uit.

## Problemen oplossen

- **De werker retourneert een lang transcript:** vraag om een kortere bewijstabel met bestandsverwijzingen.
- **Werkers zijn het oneens:** lees het gezaghebbende bestand opnieuw voordat je een antwoord kiest.
- **Twee bewerkingen overlappen:** stop één bewerking en wijs bestandseigenaarschap toe of scheid de worktrees.
- **De werker heeft andere tooltoegang:** controleer diens rechten in plaats van aan te nemen dat ze overeenkomen met de hoofdagent.

## Volgende stappen

**Ga verder met [begrensde doelcycli](/articles/effective-ai-bounded-agent-loops/).** Gebruik voor teambeheer buiten dit kleine lab de [AI-samenwerkingsimplementatiecursus](/ai-collaboration-course-start/).

**Cursusnavigatie:** [Vorige: uitvoercontrole](/articles/effective-ai-output-verification/), [Cursusoverzicht](/effective-ai-course-start/).
