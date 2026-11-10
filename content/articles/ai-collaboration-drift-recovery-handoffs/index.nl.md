---
title: "AI-agenten: herstel van drift en overdrachtsworkflow"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Detecteer verouderde bronnen en beleidsadapters, herstel onderbroken publicaties en controleer onafhankelijke overdrachten tussen agents."
genre: ["Kunstmatige intelligentie", "Teamwerk", "Software-engineering"]
tags: ["AI-samenwerkingscursus", "bronafwijking", "publicatieherstel", "agentoverdracht", "actuele bronverificatie", "compensatie"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustratie van professionals die gezamenlijk projectwerk beoordelen in een cybersecuritywerkruimte"
coverCaption: ""
---
[Terug naar de AI-samenwerkingscursus](/ai-collaboration-course-start/)

**Controleer afwijkingen vóór taken en na een onderbroken publicatie.** Vergelijk bronversies, adapterversies en de afleverstatus in de repository of werkomgevingssandbox. Doe dit na afronding van één traject. Zo voorkom je dat oude samenvattingen als actuele autoriteit gelden en behoud je een controleerbare herstelgeschiedenis.

## Belangrijkste punten

- **Bronafwijking** verschilt van adapterafwijking.
- **Gedeeltelijke publicatie** vereist een register per systeem.
- **Herstel** behoudt de geschiedenis met beoordeelde wijzigingen.
- **Overdrachten** vereisen dat iemand anders de actuele bronnen zelf leest.

## Voordat u begint

**Vereisten:** de [GitHub-browserworkflow](/articles/ai-collaboration-github-browser-workflow/) of de [gemengde publicatieworkflow](/articles/ai-collaboration-confluence-jira-publication/). **Geschatte tijd:** 60 tot 90 minuten. **Niveau:** geavanceerde beoordeling.

**Veiligheid:** gebruik alleen synthetische gegevens. Pauzeer automatische publicatie vóór hersteltests. Er wordt geen actieve verwijderingsservice geleverd.

**Resultaat voor de lezer:** rond af met een statusinventaris, een besluit van de eigenaar, een beoordeelde reparatie en een overdracht die een andere beoordelaar aan de hand van actuele bronnen kan reconstrueren. Een afgeronde oefening is geen publicatietoestemming.

## Classificeer afwijkingen

| Afwijking | Signaal | Verantwoordelijke voor herstel |
|---|---|---|
| **Vereiste** | Bron verschilt van manifest | Producteigenaar |
| **Beleid** | Adapter verschilt van POL-01 | Beleidseigenaar |
| **Implementatie** | Configuratie spreekt de bedoeling tegen | Beheerder |
| **Runbook** | Instructies spreken goedgekeurd gedrag tegen | Operations-eigenaar |
| **Toegang** | Eerder leesbare bron is geweigerd | Beheerder, taak gestopt |
| **Aflevering** | Afgerond zonder volledig register | Aflevereigenaar |

**De nieuwste tekst is niet automatisch de goedgekeurde autoriteit.** Een recente ongeautoriseerde bewerking vereist onderzoek, geen automatische overname. Stel eerst de status en eigenaar vast voordat je waarden kopieert.

## Voer de preflight uit

```text
Read MAP-01 and capture its revision.
Read POL-01 and compare active adapter versions.
Read REQ-17 and RUN-04 from mapped homes.
Read config.json at protected main.
Read frozen proposal and current role reviews.
Compare current sources with reviewed bases.
List mismatches, denied reads, and pending publications.
Stop consequential writes until owners resolve each mismatch.
```

**De bijdrager voert de preflight uit vóór het opstellen van een voorstel. De uitgever herhaalt die vóór het schrijven.** Bewaar de versievergelijking bij het voorstel. Wekelijkse controles vullen deze bronlezingen aan, maar vervangen ze niet.

**Voorbeeld van adapterafwijking:** POL-01 wordt versie 2, terwijl CLAUDE.md nog versie 1 vermeldt. Stop, lees de beoordeelde beleidswijziging, werk de adapter bij via een beschermde PR en start een nieuwe sessie. Alleen het versienummer aanpassen zonder het beleid te laden herstelt de context niet.

**Breng bronafwijking aan in het offline lab:** pak een nieuwe kopie van het meegeleverde ZIP-bestand uit in een lege tijdelijke map. Kopieer vanuit de hoofdmap `baseline/` naar `candidate/`, voer `python3 check.py capture --base baseline > candidate/context.json` uit en daarna `python3 check.py validate --base baseline --candidate candidate`. Noteer de eerste `PASS`. Open `baseline/requirement.json` in een teksteditor en wijzig alleen `"retention_days": 7` in `"retention_days": 8`. Voer dezelfde validate-opdracht opnieuw uit. De verwachte afsluitstatus is niet nul en de melding luidt `STALE_CONTEXT: capture the trusted base again`. Noteer beide uitvoerresultaten en het gewijzigde bronpad. Verwijder deze tijdelijke uitpakmap nadat je privébewijs hebt bewaard en pak daarna een nieuwe kopie uit om te resetten. Pas de wijziging van acht dagen niet toe op de gepubliceerde repository en beschouw opnieuw vastleggen niet als goedkeuring van de eigenaar.

**Breng adapterafwijking aan in de tijdelijke repository:** maak op een nieuwe voorstelbranch een kopie van de goedgekeurde POL-01-adaptertekst versie 1 in CLAUDE.md en label die als versie 1. Schrijf in een afzonderlijk beoordeeld beleidsvoorstel een wijziging naar versie 2 met een specifieke nieuwe stopvoorwaarde. Laat de adapter op versie 1 staan. Vraag een beoordelaar de twee records te vergelijken en de adapter als verouderd aan te merken vóór een merge of agentuitvoering. Reset door de testvoorstellen te sluiten of de adapter via een beoordeelde PR bij te werken. Open daarna een nieuwe sessie en controleer beide versies en de nieuwe stopvoorwaarde. Bewaar de oude en gecorrigeerde diffs. Dit is een documentatietest, geen nagebootste platformweigering.

## Herstel een onderbroken publicatie

1. **Pauzeer publicatie van PROP-042** en wijs een herstelverantwoordelijke aan.
2. **Lees de werkelijke status** in alle betrokken systemen. Maak onderscheid tussen afgerond, mislukt en niet geprobeerd.
3. **Vraag Product om een keuze:** verder afronden, een beoordeelde terugdraaiing uitvoeren of wachten.
4. **Maak een herstelvoorstel** op basis van actuele versies, met ongewijzigde scope en uitzonderingen tenzij die expliciet zijn beoordeeld.
5. **Voer telkens één beoordeelde stap uit** en leg het resultaat vast en lees het terug.
6. **Controleer de eindstatus** en resterende beperkingen voordat normaal werk hervat.

```yaml
recovery_id: RECOVERY-042
proposal_id: PROP-042
mode: awaiting-owner-choice
illustrative_state:
  requirement: thirty-days-published
  implementation: seven-days-on-main
  runbook: seven-days
  delivery: blocked
choices:
  forward: finish approved implementation and runbook
  backout: restore baseline through reviewed changes
  hold: wait for evidence or access
```

**Vervang voorbeeldstatussen door waargenomen revisies en waarden.** Een eerdere registerregel of bewering van een assistent is geen bewijs van teruglezing.

| Keuze | Gebruik wanneer | Beperking |
|---|---|---|
| **Verdergaan** | Goedkeuring blijft geldig en bronnen komen overeen | Vereist nieuwe verificatie |
| **Terugdraaien** | Eigenaar trekt de wijziging in of implementatie mislukt | Herstelt geen verwijderde gegevens |
| **Wachten** | Bewijs of toegang ontbreekt | Aflevering blijft onvolledig |

**Kies voor wachten als bewijs ontbreekt.** Synthetische oefeningen geven geen operationele reden voor blind overschrijven. Benoem de volgende rol en het ontbrekende bewijs.

**GitHub-herstel** gebruikt een beoordeelde revert of compensatie. **Confluence-herstel** vergelijkt de geschiedenis en gebruikt beoordeeld herstel of compensatie. **Jira-herstel** bewaart de voorstelgeschiedenis en heropent of blokkeert de aflevering. Lees de resulterende revisies in plaats van aan te nemen dat de nummering van de geschiedenis opnieuw begint.

## Controleer een onafhankelijke overdracht

```text
Handoff: HANDOFF-042
Task: PROP-042
Map and policy: attach current approved revisions
Evidence: requirement, runbook, configuration references
Ledger: completed, failed, pending
Decision: owner choice and fixed proposal revision
Limits: no runtime deletion test or production data
Next role: accountable role
Next action: one bounded step
Stop: changed base, access denial, conflicting authority
```

**Open een andere tool of een schone sessie** met de kaart en overdracht, niet met het vorige gesprek. Vereis nieuwe bronlezingen, een nieuw manifest en een benoemde openstaande actie. Handmatig browserbewijs blijft geldig als je het als momentopname labelt en vóór het schrijven opnieuw controleert.

**Negatieve overdracht:** trek toegang tot REQ-17 in. Verwacht een expliciete blokkade, geen gegokte waarde of bevoorrecht fragment. Herstel alleen goedgekeurde toegang via beheer en herhaal de verificatie.

## Stel eerst een diagnose

**Begin met een statusinventaris.** ‘De assistenten zijn het oneens’ beschrijft een symptoom in het antwoord, niet het onderliggende bronprobleem. Lees de toegewezen vereiste, configuratie, het runbook, beleid en afleverrecord elk afzonderlijk voordat je een van beide assistenten om herstel vraagt.

| Waarneming | Diagnose | Eerste actie |
|---|---|---|
| **Beide bronnen komen overeen, oud antwoord wijkt af** | Verouderde antwoordcontext | Reconstrueer op basis van nieuwe lezingen |
| **Vereiste dertig, configuratie zeven** | Aflever- of implementatieverschil | Controleer het goedgekeurde pakket en register |
| **Adapter één, beleid twee** | Verschil in instructieversie | Lees beleidswijziging en herstel adapter |
| **Bron eerder leesbaar, nu geweigerd** | Toegang gewijzigd | Stop taak en vraag bevoegde beoordeling |
| **Register volledig, runbook zeven** | Afsluiting zonder geldige teruglezing | Heropen of blokkeer aflevering en onderzoek |

**Behandel niet elk verschil als een modelprobleem.** Een sessie vernieuwen verhelpt verouderde gesprekscontext. Het publiceert geen runbook, herstelt geen ontbrekende machtiging en verzoent geen tegenstrijdige besluiten van eigenaren. Benoem de herstelverantwoordelijke voordat je een toolactie kiest.

## Doorloop compensatie

**Voorbeeld van onderbreking:** REQ-17 bevat goedgekeurde intentie voor dertig dagen, maar de aflevering staat nog open. De configuratie en het runbook bevatten nog zeven dagen. De beheerder meldt een onopgeloste implementatiefout. Product kiest voor herstel in plaats van verdergaan.

1. **Leg actuele versies vast:** vereiste dertig, configuratie zeven, runbook zeven, aflevering geblokkeerd.
2. **Pauzeer het openstaande voorstel:** bewaar de beoordelingen en het bewijs van mislukte publicatie.
3. **Maak een compenserende wijziging van de vereiste:** herstel zeven en behoud tussentijdse uitzonderingen en opmerkingen.
4. **Vraag beoordeling door de eigenaar:** benoem de actuele bronversie en de exacte hersteltekst.
5. **Publiceer via de toegestane route:** lees de nieuwe vereisteversie terug.
6. **Werk het register bij:** alle toepasselijke gepubliceerde waarden zijn zeven; de oorspronkelijke wijziging is niet geleverd.

**Compensatie verwijdert de geschiedenis niet.** Bewaar de poging met dertig dagen, de mislukking en het latere herstel als afzonderlijke records. De eindbron vermeldt zeven, terwijl de aflevergeschiedenis uitlegt waarom het goedgekeurde voorstel niet is afgerond.

```text
Recovery decision: illustrative compensation
Original proposal: PROP-042 revision 1
Observed mismatch: requirement 30, configuration/runbook 7
Owner decision: restore approved baseline intent
Review object: fixed compensation against current requirement version
Result: capture resulting revision and seven-day read-back
Original delivery: withdrawn or blocked with explanation
Limit: no runtime deletion or data restoration performed
```

**Behoud een uitzondering expliciet als een andere schrijver die heeft toegevoegd.** Een oude paginaversie blind terugzetten kan een geldige tussentijdse wijziging verwijderen. Vergelijk de actuele en beoogde tekst en beoordeel daarna een minimale compenserende wijziging tegen de actuele versie.

## Test een nieuwe overdracht

**Gebruik een schone sessie en een andere beoordelaar.** Geef de kaart, het vastgezette pakket, het register en het herstelbesluit. Houd het vorige gesprek achterwege. Vraag de ontvanger de actuele bedoeling, configuratie, werkinstructies en volgende toegestane actie te benoemen.

```text
Read the mapped current sources independently.
Distinguish approved intent, committed configuration, and delivery state.
Compare them with the reviewed package and ledger.
List missing reads and changed bases.
Recommend one bounded next action with its accountable role.
Do not treat this handoff as approval or publication permission.
```

**Verwachte redenering:** de ontvanger controleert het resultaat van de compensatie voordat die de uitgangssituatie als hersteld beschrijft. Als de ontvanger alleen ‘zeven dagen’ uit de overdracht herhaalt, is de eis van onafhankelijk lezen nog niet getest. Vraag om bronbewijs in plaats van nog een samenvatting.

**Voltooide lesinventaris, synthetische onderbreking:**

| Record | Waargenomen status | Te bewaren bewijs | Volgende eigenaar |
|---|---|---|---|
| REQ-17 | v5 vermeldt dertig dagen, back-ups uitgesloten | Paginasgeschiedenis en nieuwe lezing | Product |
| Beschermde configuratie | `main` op `base-001` vermeldt zeven dagen | Commit-teruglezing en geweigerde mergegebeurtenis | Repositorybeheerder |
| RUN-04 | v2 vermeldt nog steeds zeven dagen | Nieuwe paginalezing | Operations |
| PROP-042 | r1 goedgekeurd, aflevering geblokkeerd | Vastgezette beoordelingen en register | Aflevereigenaar |

Geef deze inventaris aan een tweede lezer zonder het oude gesprek. De overdracht slaagt alleen als de lezer de vier statussen zelfstandig vindt, de uitsluiting van back-ups benoemt, `base-001` als actuele beschermde revisie aanwijst en een herstelstap met beoordeling door de eigenaar voorstelt. Markeer als mislukt bij een onjuiste revisie, ontbrekende uitzondering of niet-onderbouwde hervatting. Noteer de bronverwijzingen en eventuele correctie van de lezer voordat er opnieuw wordt geschreven.

## Bepaal of u hervat

| Preflight-resultaat | Besluit over hervatten |
|---|---|
| **Bronnen komen overeen met vaste goedkeuring** | Voer de toegestane openstaande stap uit |
| **Bron buiten beoordeelde scope gewijzigd** | Stop voor vergelijking en nieuwe beoordeling |
| **Leesrechten ontbreken** | Wacht met een aangewezen toegangsbeoordelaar |
| **Beleid gewijzigd** | Herstel adapters en beoordeel taaktoestemming opnieuw |
| **Schrijfresultaat onbekend** | Lees bestemming voordat je opnieuw probeert |

**Houd acceptatie van herstel concreet.** Vereis een overeenkomende teruglezing, een actueel beoordelingsobject, een afgestemd register en een nieuwe overdracht. Sluit herstel niet af omdat de assistent zegt dat het probleem is opgelost.

**Afrondingscontrole:** lever een waargenomen statusinventaris, besluit van de eigenaar, beoordeelde reparatie, definitieve teruglezing en onafhankelijke reconstructie. Als toegang een lezing verhindert, documenteer dan de blokkade. Neem deze bewijsnorm mee naar de capstone.

## Problemen oplossen en terugdraaien

**Conflicten bij terugdraaien:** maak een compenserende wijziging op basis van de actuele status. **Herstel verliest uitzonderingen:** vergelijk vóór het schrijven de volledige relevante sectie. **Oude herinnering bepaalt het antwoord:** start opnieuw met goedgekeurde bronnen en verwijder verouderde conceptcontext.

**Herstel terugdraaien:** stop bij de laatst geverifieerde status en voeg een nieuwe registerregel toe. Wis geen oorspronkelijke auditgebeurtenissen en reset geen beschermde geschiedenis met dwang. Escaleer onopgeloste bevoegdheidskwesties naar Product.

## Oefening en zelfcontrole

**Voer een oefening uit met verouderd bewijs, een achterhaalde beleidsadapter en een gedeeltelijke publicatie.** Geef een andere beoordelaar de records zonder toelichting en vraag wie het herstel uitvoert.

**Verwachte redenering:** Product is verantwoordelijk voor afstemming van vereisten, de beleidseigenaar voor adapteruitlijning en de afleverherstelcoördinator voor afstemming tussen betrokken eigenaren. ‘Vernieuw de context’ is geen volledige oplossing voor al deze situaties.

## Primaire bronnen

- **Herstel van repositories:** [Beschermde branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Paginageschiedenis:** [Confluence-documentatie](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Inspectie van instructies:** [Claude Code-geheugen](https://code.claude.com/docs/en/memory).

## Vervolgstappen

**Voltooi de [Retention Capstone](/articles/ai-collaboration-retention-capstone/)** met beide trajecten en een tweede lezer. Toon actuele bronlezingen, versieafwijkingen, de beslissingseigenaar, het beoordeelde herstel, de teruglezing en onafhankelijke reconstructie.
