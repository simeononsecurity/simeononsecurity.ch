---
title: "AI-publicatieworkflow voor GitHub, Confluence en Jira"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Publiceer een vast retentievoorstel in Confluence, GitHub en Jira met versiecontroles en herstel na gedeeltelijke publicatie."
genre: ["Kunstmatige intelligentie", "Teamwerk", "Softwareontwikkeling"]
tags: ["AI-samenwerkingscursus", "Confluence Cloud", "Jira Cloud", "publicatie tussen systemen", "versiecontrole", "publicatielogboek", "gedeeltelijke publicatie"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustratie van professionals die gezamenlijk projectwerk beoordelen in een cybersecuritywerkruimte"
coverCaption: ""
---

[Terug naar de cursus AI-samenwerking](/ai-collaboration-course-start/)

**De bijdrager bevriest PROP-042 voordat de eigenaren het goedkeuren.** Een Confluence-publiceerder werkt de vereisten bij, een GitHub-beheerder voegt de implementatie samen en Operations publiceert het draaiboek. Jira registreert elke stap. Voer dit uit nadat je de bevoegdheden hebt gecontroleerd, want de drie systemen vormen samen geen atomaire transactie. Met je publicatielogboek zie je wanneer de levering onvolledig is.

## Belangrijkste punten

- **Goedgekeurde intentie** verschilt van opgeleverd gedrag.
- **Vaste voorstelrevisies** leggen de review vast.
- **Publicatielogboeken** maken gedeeltelijke voltooiing zichtbaar.
- **Nieuwe broncontroles** beschermen tegen gewijzigde uitgangspunten.

## Voordat je begint

**Vereisten:** de [werkplekinrichting](/articles/ai-collaboration-confluence-jira-setup/), toegang om te publiceren, eigenaren en een repositorybeheerder. **Geschatte tijd:** twee uur. **Moeilijkheid:** geavanceerde coördinatie.

**Uitgangspunt voor de interface:** browsercontroles, optioneel chatconcepten opstellen met goedkeuring, en publicatie door een mens. We gaan uit van geen connectorabonnement. Controleer beschikbaarheid van de tenant, machtigingen, verwerking door de provider en identiteitskoppeling voordat je een integratie toevoegt. Deel nooit de inloggegevens van een eigenaar met een bijdrager.

**Resultaat voor de lezer:** je sluit af met een vast voorstel, een publicatielogboek per systeem, bewijs uit teruglezingen en een herstelbesluit voor de eerste onvolledige stap. De oefening bewijst de procedure en bewijsverwerking, niet het gedrag van retentie in productie.

## Actuele bronnen vastleggen

1. **Lees MAP-01** en open daarna REQ-17 en RUN-04 via de gekoppelde pagina-ID's.
2. **Open het paginamenu en de paginageschiedenis (Page History)** en leg versienummers, status, tekst, eigenaar en uitzonderingen vast.
3. **Lees het Jira-item** en voeg een vast voorstelbestand of een GitHub-commit toe. Alleen de sleutel bevriest het reviewbewijs niet.
4. **Lees POL-01 met goedkeuring** en de beveiligde configuratiebasislijn.
5. **Geef alleen de noodzakelijke synthetische fragmenten door** aan de chat, markeer ze als momentopnamen en houd schrijfbevoegde acties uitgeschakeld.

```text
Task: PROP-042, propose only
Authority: Confluence REQ-17 for intent, GitHub for behavior
Read: mapped current pages, versions, scope, exceptions
Proposal: synthetic export retention from 7 to 30 days
Output: requirement wording, config diff, runbook, ledger
Evidence: source ID and captured revision for each factual claim
Unknowns: missing access and absent runtime observations
Stop: conflict, changed base, or denied access
```

**Offline pakketten blijven momentopnamen.** De publiceerder voert opnieuw live controles uit voordat er iets wordt geschreven. Geweigerde toegang blokkeert publicatie. Een oude export vervangt geen actuele toestemming.

## Het voorstel vastzetten

```json
{
  "proposal_id": "PROP-042",
  "proposal_revision": 1,
  "requirement_base_version": 1,
  "runbook_base_version": 1,
  "policy_version": 1,
  "from_days": 7,
  "to_days": 30,
  "status": "awaiting-owner-review",
  "publication_order": ["requirement", "implementation", "runbook", "delivery"]
}
```

**Vervang voorbeeldversies van pagina's door de werkelijk vastgelegde versies.** Voeg de vaste JSON en de voorgestelde tekst toe aan Jira. Elke eigenaar registreert de rol, het besluit, de voorstelrevisie, de bronversies en het reviewtijdstip. Bij elke inhoudelijke wijziging gaat het pakket terug naar `Review`.

**Product beoordeelt intentie en reikwijdte. Operations beoordeelt opschoning en herstel.** De beheerder beoordeelt de diff. Reacties op wijzigbare chatberichten zijn geen goedkeuringen die aan een revisie zijn gekoppeld.

## Publiceren en teruglezen

1. **Zet Jira op `Publishing`** nadat de publiceerder beide reviews van de eigenaren en ongewijzigde bronbasissen heeft gecontroleerd.
2. **Publiceer REQ-17** met dertig dagen en het veld voor levering in behandeling. Registreer de resulterende versie, reikwijdte en uitzonderingen.
3. **Open de GitHub-implementatie-PR** met de goedgekeurde paginaversie als verwijzing. Wijzig de configuratie naar dertig dagen en voeg een niet-gezaghebbende momentopname van de vereiste toe.
4. **Voeg de wijziging na de repositoryreview samen** en lees **`main`** terug. Registreer vastgelegd gedrag apart van runtimegedrag.
5. **Publiceer RUN-04**, lees het terug via de ID en registreer de resulterende versie. Laat de publiceerder de verwijzingen naar de levering in de vereiste bijwerken.
6. **Rond Jira pas af** wanneer alle registraties overeenkomen en het bewijs van de laatste teruglezing is toegevoegd.

**Gebruik de lokale validator alleen voor de consistentie van momentopnamen.** Kopieer de Confluence-vereiste van vóór de wijziging naar het JSON-basisschema van het lab, leg deze vast en pas het kandidaatbestand aan naar dertig dagen. Gebruik een verhoogde lokale revisie van de momentopname en bewaar de werkelijke Confluence-versies afzonderlijk in Jira. De workflow met GitHub als eerste bron valideert geen live Confluence-gegevens. Presenteer een groene status daarom niet als verificatie van de externe bron.

**Rol in deze oefening geen verwijdergedrag uit.** Een echte dienst vereist bewijs van implementatie, gecontroleerde testgegevens, een mechanisme om verwijdering tijdelijk op te schorten en tests van runtimegrenzen. Een samenvoeging bewijst de repositorystatus, niet het retentiegedrag in productie.

## Gedeeltelijke publicatie bijhouden

| Stap | Beginstatus | Bewijs van voltooiing |
|---|---|---|
| **REQ-17** | `Pending` | Resulterende paginaversie |
| **Configuratie** | `Pending` | Samengevoegde commit en review |
| **RUN-04** | `Pending` | Resulterende paginaversie |
| **Jira afronden** | `Pending` | Laatste teruglezing en statusovergang |

**Registreer elk resultaat voordat je de volgende stap probeert.** PROP-042 koppelt de gebeurtenissen in de afzonderlijke systemen aan elkaar. Eén voltooide rij betekent nooit dat de hele wijziging klaar is.

**Uitgewerkte fout:** Confluence publiceert dertig dagen, maar GitHub weigert de samenvoeging. Houd Jira op `Blocked` en markeer de vereiste als levering in behandeling. Product kiest voor voltooiing of een beoordeelde terugzetting naar zeven dagen. Maak een noodkopie in README niet leidend voor de vereiste.

## Gelijktijdige wijzigingen afhandelen

**Browseruitgangspunt:** wijs één publiceerder aan voor de pilotperiode. Open de paginageschiedenis direct vóór en na het publiceren opnieuw. Wijzigt een andere schrijver de bron, stop dan, vergelijk en stem af, en vraag opnieuw om goedkeuring. Publicatie in volgorde is een procedure, geen garantie op een atomaire transactie.

**API-uitbreiding:** de Confluence v2-documentatie beschrijft **`GET /wiki/api/v2/pages/{id}?body-format=storage`** en **`PUT /wiki/api/v2/pages/{id}`** met een versieobject. Een beoordeelde publiceerintegratie vergelijkt de huidige versie met de goedgekeurde basis, verzendt de volgende versie en leest die terug. Vernieuw nooit automatisch een mislukte versie en probeer daarna opnieuw met een oude tekst.

**API-succes alleen is onvoldoende.** Controleer de resulterende inhoud, bron-ID, reikwijdte en versie. Deze cursus levert geen schrijfbevoegde API-client. Publicatie via de browser door een mens is de uitvoerbare basis voor niet-programmeurs.

## Negatieve gevallen testen

| Injectie | Verwachte redenering |
|---|---|
| **Bron wijzigen na goedkeuring** | Stop en vraag opnieuw goedkeuring voor de nieuwe versie |
| **Bewerktoegang van de publiceerder verwijderen** | Weiger de wijziging en houd het logboek open |
| **Jira op zestig dagen zetten** | Stop bij het conflict en behoud Confluence als gezaghebbende bron |
| **Publicatie van het draaiboek mislukt** | Houd levering onvolledig en wijs herstel toe |

**Registreer werkelijke sandboxresultaten** met de rol van de actor en revisies vóór en na de actie. Neem geen beschermde paginainhoud op in bewijs voor een gebruiker met geweigerde toegang. Verwachte resultaten zijn geen gemeten uitkomsten.

## Het reviewpakket samenstellen

**Bevries de inhoud, niet alleen het voorstelnummer.** PROP-042 verschijnt in elk systeem, maar een label geeft niet aan welke inhoud de eigenaar heeft beoordeeld. Neem de exacte vereiste tekst, implementatiediff, draaiboektekst, bronversies en publicatievolgorde op in één vast pakket.

```text
Package: PROP-042 revision 1, illustrative
Intent: synthetic export retention changes from 7 to 30 days
Exclusions: production data, backups, legal holds
Requirement amendment: fixed proposed REQ-17 wording
Implementation: fixed candidate diff and protected base reference
Runbook amendment: fixed RUN-04 wording and recovery limits
Review: product and operations decisions for this package
Delivery: requirement -> implementation -> runbook -> closure
Stop: changed source, missing review, denied write, failed read-back
```

**Houd het pakket leesbaar voor beide eigenaren.** Product heeft de intentie en uitzonderingen nodig. Operations heeft de operationele wijziging en herstelgrens nodig. Beiden moeten begrijpen in welke periode de goedgekeurde intentie en de opgeleverde configuratie verschillen. Een kale codediff volstaat niet voor een eigenaar die de repositorybestanden niet kent.

**Ingevulde pakketinhoud voor dit synthetische voorbeeld:**

```text
REQ-17 proposed v5: "Synthetic export files are retained for 30 days from creation. This pilot excludes production data, backups, and legal holds. Delivery remains pending until the GitHub configuration and RUN-04 read-backs match this approved wording."

GitHub config.json, proposed change against base-001:
-  "retention_days": 7
+  "retention_days": 30

RUN-04 proposed v3: "Retention days: 30. Synthetic exports only. No deletion job runs in this lab. If publication fails, keep delivery pending, read back each source, and obtain owner approval before restoring the seven-day configuration or completing the thirty-day publication."
```

Deze teksten zijn voorbeeldvoorstellen, geen gegevens uit een live tenant. Voeg vóór de review de daadwerkelijke basiscommit en paginaversies toe. Het vaste pakket bevat de volledige voorgestelde teksten, niet alleen een samenvatting waarvoor een eigenaar ontbrekende details moet invullen.

**Houd de offline momentopname gescheiden van live publicatie.** Een consistentiecontrole toont overeenstemming tussen vastgelegde gegevens. Direct vóór de eerste wijziging controleert de publiceerder de gekoppelde pagina's opnieuw en controleert de beheerder de beveiligde basis opnieuw. Is een van beide gewijzigd, dan stopt het oude pakket bij `Review`.

## Het logboek doorlopen

**Voorbeeld van statusverloop:** de tabel gebruikt onderwijsversies, geen waarnemingen. Vul na elke sandboxwijziging de werkelijke resulterende versies en commits in.

| Stap | Status na geslaagde teruglezing | Resterend werk |
|---|---|---|
| **Review door eigenaren afgerond** | Goedgekeurd pakket, alle gepubliceerde waarden zijn zeven | Alle publicatiestappen |
| **REQ-17 gepubliceerd** | Intentie is dertig, levering in behandeling | Configuratie en draaiboek |
| **GitHub-samenvoeging teruggelezen** | Intentie/configuratie is dertig, draaiboek is zeven | Draaiboek en eindcontrole |
| **RUN-04 gepubliceerd** | Alle toepasselijke registraties zijn dertig | Onafhankelijke laatste teruglezing |
| **Levering gesloten** | Volledig logboek met bewijs | Vastgelegde runtimehiaten blijven bestaan |

**Levering in behandeling is een betekenisvolle status.** Daarmee voorkom je dat de oude implementatie als conform de nieuwe intentie wordt beschreven terwijl de publicatie nog loopt. Lezers hebben tijdens deze periode beide waarden nodig, niet één samenvatting die beweert dat de retentie dertig dagen is.

**Voeg mislukte pogingen als aparte gebeurtenissen toe.** Mislukt het schrijven van een draaiboek, behoud dan de geslaagde resultaten voor de vereiste en configuratie. Leg de poging voor het draaiboek, de fout, de ongewijzigde versie, de toegewezen rol en de volgende actie vast. Zet voltooide rijen niet terug op In behandeling en wis de waargenomen volgorde niet.

**Voorbeeld van afwijzing wegens een verouderde versie:** de publiceerder leest REQ-17 v4, een andere gemachtigde bewerker publiceert v5 en daarna probeert de publiceerder PROP-042 r1 toe te passen op v4. Het platform meldt een versieconflict of de controle vóór schrijven detecteert v5. Registreer actor `publisher`, oorspronkelijke versie `v4`, poging `PROP-042 r1`, waargenomen conflict of gewijzigde huidige versie, de ongewijzigde eindversie `v5` en de toegewezen eigenaar `product owner`. Houd Jira in Review. Lees v5 opnieuw, stem de tekst af en vraag review voor een nieuw vast pakket voordat je opnieuw schrijft. Gebruik bij een live test de werkelijke platformreactie en paginageschiedenis. Deze rij is een onderwijsscenario.

**Voltooid onderwijsscenario, uitsluitend synthetische waarden:**

| Systeem | Initiële bron | Vaste review | Schrijven en teruglezen | Eindstatus |
|---|---|---|---|---|
| Confluence REQ-17 | v4, zeven dagen | PROP-042 r1, Product keurde v4 naar v5 goed | Publiceerder schreef v5, reviewer opende v5 opnieuw | Dertig dagen, back-ups en wettelijke bewaarplichten uitgesloten |
| GitHub-configuratie | `main`-commit `base-001`, zeven dagen | PROP-042 r1, Operations keurde de kandidaat-diff goed | PR samengevoegd als `merge-002`, onafhankelijke kloon las dertig terug | Dertig dagen in de beveiligde bron |
| Confluence RUN-04 | v2, zeven dagen | PROP-042 r1, Operations keurde v2 naar v3 goed | Publiceerder schreef v3, reviewer opende v3 opnieuw | Bedrijfsstap voor dertig dagen met terugzetprocedure |
| Jira PROP-042 | `In Review` | Beide eigenaarbesluiten gekoppeld aan r1 | Leveringseigenaar voegde bewijs toe en zette de status op `Done` | Afgesloten na alle drie teruglezingen |

De labels hierboven zijn illustratief, geen tenantbewijs. Je logboek heeft koppelingen naar de oorspronkelijke paginaversies en commit-ID's nodig. Voeg vóór je Jira op `Done` zet het vaste voorstel, de twee rolreviews, de registratie van de bronbasissen, elke publicatieteruglezing, het resultaat van de negatieve test en de resterende runtimebeperkingen toe. Ontbreekt er iets, houd de levering open of `Blocked`.

**Poort voor het pakket:** markeer elk van de vijf controles als `Supported` of `Blocked`: bronrevisies zijn actueel, beide eigenaren keurden dezelfde vaste revisie goed, alle vereiste publicaties komen overeen met de teruglezing, runtimebeperkingen blijven expliciet en de herstelstatus is afgestemd. `Done` vereist vijf controles met `Supported` en geen onbevoegde wijziging.

## Een onzekere wijziging afhandelen

**Een time-out laat de uitkomst onbekend.** Die bewijst geen succes of mislukking. Open in de browserbasis de gekoppelde bron opnieuw en bekijk de actuele inhoud en geschiedenis voordat je beslist of je opnieuw probeert.

1. **Pauzeer de volgende stap:** houd de levering onvolledig.
2. **Lees de bestemming:** vergelijk de huidige tekst, versie en reikwijdte met het vaste pakket.
3. **Leg de waarneming vast:** voltooid, ongewijzigd, conflicterend of ontoegankelijk.
4. **Kies de volgende actie:** ga door vanaf een geverifieerde voltooiing, probeer een bevoegde ongewijzigde stap opnieuw of escaleer een conflict.
5. **Bewaar de onzekerheid:** houd de mislukte of onbekende poging naast de latere teruglezing.

**Speel niet blind de hele reeks opnieuw af.** Een reeds voltooide stap herhalen maakt extra revisies en kan niet-gerelateerde wijzigingen overschrijven. Hervat vanaf de geverifieerde status. Is de bron niet toegankelijk, kies dan voor `Hold` in plaats van te gissen op basis van het oude logboek.

## Herstelbesluiten vergelijken

| Situatie | Te beoordelen besluit | Reden |
|---|---|---|
| **Vereiste gewijzigd, samenvoeging geweigerd** | Vooruitgaan of de vereiste compenseren | Intentie en gedrag verschillen |
| **Configuratie gewijzigd, draaiboek geweigerd** | Draaiboek afronden of configuratie terugdraaien | Bedieningsinstructies zijn verouderd |
| **Andere eigenaar wijzigt de reikwijdte** | Terug naar `Review` | De vaste goedkeuring beschrijft andere inhoud |
| **Uitkomst van wijziging onbekend** | Eerst de bestemming lezen | Opnieuw proberen hangt af van de waargenomen status |
| **Publiceerder verliest toegang** | Vasthouden en bevoegde administratie vragen | Oude toestemming geeft geen recht op nieuwe wijzigingen |

**Kies op basis van de actuele status en het besluit van de eigenaar.** Vooruitgaan vereist actuele goedkeuringen en werkbare controles. Compensatie vereist review van het herstel in samenhang met wijzigingen die later zijn aangebracht. Een herstelwijziging is opnieuw een publicatie, geen bevoegde uitzondering op het proces.

## Controle op publicatievoltooiing

**Lever een pakket dat een onafhankelijke reviewer kan afstemmen.** Die moet het exacte beoordeelde voorstel, de bronbasissen, beide rolreviews, elk schrijfresultaat, de eindwaarden en de resterende runtimebeperkingen kunnen vinden. Vraag de reviewer de eerste onvoltooide stap na een onderbreking aan te wijzen.

**Verwachte redenering:** de volgende actie volgt uit actuele bronnen en het logboek, niet uit het vertrouwen van de vorige assistent. Neem de uiteindelijke gekoppelde verwijzingen mee naar de ophaaltests, waar het terugvinden hetzelfde onderscheid in gezag moet behouden.

## Problemen oplossen en herstellen

**Versie gewijzigd:** vergelijk de geschiedenis en vraag opnieuw review. **Momentopnamecontrole slaagt, maar de wiki wijkt af:** haal de actuele Confluence-bronnen opnieuw op. **Jira te vroeg op `Done` gezet:** heropen dit via de toegestane workflow en registreer de ontbrekende stappen.

**Herstel:** vergelijk via de paginageschiedenis en voer een door een eigenaar beoordeelde terugzetting of compenserende wijziging uit. Registreer de resulterende versie. Ga er niet van uit dat terugzetten het versienummer reset. Zet de configuratie terug via een beveiligde PR als Product daarvoor kiest. Verwijderde bestanden vallen buiten de terugzetgarantie.

## Oefening en zelfcontrole

**Onderbreek na publicatie van REQ-17** en geef een andere publiceerder alleen de kaart en het logboek.

**Verwachte redenering:** de volgende publiceerder haalt actuele bronnen op, bevestigt de vaste goedkeuring en hervat alleen de bevoegde openstaande stap. Ontbreekt bewijs, dan gaat het werk terug naar `Review`.

## Primaire referenties

- **Geschiedenis en herstel:** [technische documentatie van Confluence](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Versiebeheerde API-bewerkingen:** [Confluence REST API v2-pagina's](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/).
- **Workflowcontroles:** [geavanceerde Jira-workflows](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).
- **Beveiliging van integraties:** [best practices voor MCP-beveiliging](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices).

## Volgende stappen

**Ga na een beoordeelde publicatieronde verder met [Op kaarten gebaseerd ophalen](/articles/ai-collaboration-map-first-retrieval/).**
