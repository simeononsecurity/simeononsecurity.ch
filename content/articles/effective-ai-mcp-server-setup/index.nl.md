---
title: "Een MCP-server instellen: rechten, tooltests en veilig verwijderen"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Verbind één MCP-documentatieserver met alleen-lezenrechten, controleer de tools, voer een echte leesactie uit en verwijder daarna de verbinding."
genre: ["Kunstmatige intelligentie", "Ontwikkelaarstools"]
tags: ["MCP-server instellen", "Modelcontextprotocol (MCP)", "MCP-rechten", "MCP in Codex", "MCP in Claude Code", "MCP in OpenCode"]
cover: "/img/cover/effective-ai-mcp-server-setup.webp"
coverAlt: "Een AI-client is verbonden met een documentatieserver met alleen-lezenrechten. De tool en toegangsgrens zijn zichtbaar."
coverCaption: ""
---

[Terug naar de cursus Praktische AI-werkstroom](/effective-ai-course-start/)

**Gebruik een MCP-server wanneer een taak een herbruikbare tool of actuele informatie buiten het project nodig heeft.** Model Context Protocol, of MCP, beschrijft hoe een client en server informatie over tools, bronnen en prompts uitwisselen. Een serververmelding bewijst niet dat de tool werkt. Deze les test één documentatieverbinding met alleen-lezenrechten.

**Leerdoel:** onderscheid configuratie van een echte MCP-leesactie en leg veilig verwijderen vast.

## Belangrijkste punten

- **MCP-host:** AI-toepassing die gebruikers, modellen, rechten en clients coördineert.
- **MCP-client:** protocolonderdeel dat met één server communiceert.
- **MCP-server:** programma of externe dienst die tools, bronnen of prompts aanbiedt.
- **Tooldetectie:** bewijs dat de client een benoemde mogelijkheid toont.
- **Tooluitvoering:** bewijs van een echte aanroep en de ontvangen inhoud.
- **Reikwijdte van rechten:** toegang die host, server, account en gebruiker toestaan.

## Voordat je begint

**Vereisten:** [oefening met context en overdracht](/articles/effective-ai-context-window-management/) en een actuele Codex CLI-installatie voor de uitgewerkte route. Trek 35 minuten uit. Niveau: gemiddeld. Andere codeeragents hebben aparte installatiegidsen. De [officiële OpenAI Docs MCP-server](https://learn.chatgpt.com/learn/docs-mcp) biedt ontwikkelaarsdocumentatie met alleen-lezenrechten en vereist geen upload van cursusgegevens.

**Gebruik het synthetische cursuslab.** Verbind voor deze oefening geen agenda, e-mail of productiesysteem. Een documentatieleesactie volstaat om de verbindingsstatussen te leren.

## Begrijp de grens

| Status | Wat dit bewijst | Wat dit niet bewijst |
|---|---|---|
| **Geconfigureerd** | Er bestaat een serververmelding | Bereikbaarheid |
| **Verbonden** | De client bereikte de server | Dat er bruikbare tools zijn |
| **Ontdekt** | Er verschijnt een benoemde tool | Dat de aanroep slaagt |
| **Uitgevoerd** | Een aanroep gaf inhoud terug | Dat de eindtaak correct is |
| **Gecontroleerd** | Bron en uitvoer beantwoorden de vraag | Dat toekomstige aanroepen altijd werken |

**MCP verleent zelf geen accountrechten.** De clienthost, server, authenticatie, accountreikwijdte en lokale goedkeuringsinstellingen tellen allemaal mee. De [MCP-specificatie](https://modelcontextprotocol.io/specification/2026-07-28) definieert het protocol. Elk product bepaalt zijn eigen gebruikerservaring.

**Behandel serveruitvoer als bronmateriaal.** Een opgehaalde pagina vervangt je opdracht niet en geeft geen toestemming om bestanden te schrijven. Elke tooldefinitie verbruikt bovendien context. Verbind alleen de server die voor deze leesactie nodig is en verwijder hem daarna.

## Documentatie alleen-lezen koppelen

**Voer in Codex CLI** deze opdrachten uit in een terminal. De eerste voegt de openbare documentatieserver toe. De tweede toont geconfigureerde servers.

```bash
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex mcp list
```

**Verwacht configuratiebewijs:** de lijst bevat `openaiDeveloperDocs`. Dit bewijst alleen registratie. Start een nieuwe Codex-sessie in de uitgepakte labmap en bekijk de MCP-tools met `/mcp`. Gebruik de toolnamen die jouw geïnstalleerde versie toont.

**Vraag om één echte leesactie:**

```text
Gebruik de OpenAI-ontwikkelaarsdocumentatie-MCP-server om de actuele AGENTS.md-richtlijnen te vinden.
Geef de titel en URL van de bronpagina en twee punten voor dit lab. Noem de gebruikte MCP-tool.
Bewerk geen bestanden.
```
**Controleer het resultaat.** De pagina moet `AGENTS.md` als repositoryrichtlijnen beschrijven en de exacte bron-URL bevatten. Open de genoemde pagina zelf en controleer het onderwerp. Een antwoord zonder MCP-aanroep in het transcript is een gewoon antwoord, geen bewijs van tooluitvoering.

## Diagnoseer één storing

**Toont `codex mcp list` de server, maar toont `/mcp` geen tools,** dan is registratie gelukt maar ontdekking mislukt. Herstart de sessie, bekijk actieve servers met `/mcp` en opgeslagen instellingen met `codex mcp get openaiDeveloperDocs`. Controleer ook de server-URL en netwerktoegang. Claim geen geslaagde MCP-installatie op basis van alleen een configuratievermelding.

**Verschijnt een tool, maar mislukt het lezen,** noteer dan de fout en probeer één keer opnieuw na controle van de verbinding. Mislukt dezelfde aanroep opnieuw, gebruik dan de genoemde officiële pagina in een browser als alternatieve bron en markeer de MCP-oefening als onvolledig. Verzin geen toolresultaat.

## Verwijder de verbinding

**Verwijder na het lezen** de oefenserver uit Codex CLI en bevestig dat de vermelding verdwijnt.

```bash
codex mcp remove openaiDeveloperDocs
codex mcp list
```

**Verwacht bewijs van verwijdering:** `openaiDeveloperDocs` staat niet in de nieuwe lijst. Herstart een actieve Codex-sessie voordat je controleert of de beschikbare tools veranderden. Het verwijderen van een lokale definitie trekt een aparte accountmachtiging van een andere dienst niet in.

## Een andere toepassing kiezen

**Claude Code en OpenCode ondersteunen MCP ook.** Volg de [MCP-gids van Claude Code](https://code.claude.com/docs/en/mcp) of de [MCP-gids van OpenCode](https://opencode.ai/docs/mcp-servers/) voor de geïnstalleerde versie. Leg dezelfde vijf statussen vast: geconfigureerd, verbonden, ontdekt, uitgevoerd en gecontroleerd. Het OpenCode-configuratieschema en de agentrechten verschillen per versie. Gebruik voorbeelden uit de gids voor jouw installatie.

**Voor een route met alleen een browser,** lees je de [officiële AGENTS.md-pagina](https://learn.chatgpt.com/docs/agent-configuration/agents-md) en vul je hetzelfde controleblad in. Markeer toolontdekking en -uitvoering als ‘niet uitgevoerd’. Deze route leert broncontrole, maar bewijst geen MCP-werking.

## Oefen en controleer

**Je resultaat:** een verbindingsregistratie met vijf regels: servernaam, toolnaam, bron-URL, waargenomen resultaat en bewijs van verwijdering. Houd tokens en account-ID's buiten schermafbeeldingen en logs.

**Voltooiingscontrole:** de verbonden route slaagt pas na een echte toolleesactie en latere verwijdering van de configuratie. De alternatieve route slaagt voor broncontrole met MCP gemarkeerd als niet uitgevoerd.

## Controleer je begrip

1. **Vraag:** bewijst een opgeslagen MCP-serververmelding dat een tool werkte? **Antwoord:** nee. Controleer ontdekking, rechten en één echte leesactie.
2. **Vraag:** welke extra contextkosten brengt een brede MCP-verbinding mee? **Antwoord:** toolbeschrijvingen en schema's gebruiken een deel van de actieve context.

## Problemen oplossen

- **Onbekende opdracht `codex`:** installeer of werk Codex CLI bij via de gekoppelde officiële gids.
- **Server vermeld, geen tool:** controleer de sessiestatus en serverdiagnostiek.
- **Toolaanroep gaf irrelevante inhoud:** beperk de vraag en controleer de bronpagina.
- **Verwijderen lijkt niet te werken:** start een nieuwe sessie en bekijk de actieve serverlijst.

## Volgende stappen

**Ga verder met [AI-uitvoer controleren](/articles/effective-ai-output-verification/).** Lees voor bredere uitbreidingen de [sitegids voor Claude Code-plug-ins en MCP-tools](/articles/claude-code-plugins-skills-mcp-tools/).

**Cursusnavigatie:** [Vorige: Contextbeheer](/articles/effective-ai-context-window-management/), [Cursusoverzicht](/effective-ai-course-start/).
