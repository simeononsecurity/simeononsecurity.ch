---
title: "GitHub AI-workflow voor niet-programmeurs: Issues en pull requests"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Gebruik browserbewerkingen, Issues, chatcontextpakketten en beoordeelde pull requests zonder lokale ontwikkelomgeving."
genre: ["Kunstmatige intelligentie", "Teamwork", "Software-engineering"]
tags: ["AI-samenwerkingscursus", "GitHub-bewerken in de browser", "GitHub Issues", "pull request", "niet-programmerende bijdragers", "contextpakket", "overdracht voor beoordeling"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustratie van professionals die gedeeld projectwerk in een cybersecurity-werkruimte beoordelen"
coverCaption: ""
---

[Terug naar de cursus over AI-samenwerking](/ai-collaboration-course-start/)

**Niet-programmerende bijdragers gebruiken dezelfde autoriteitsregels via de browser.** Je leest GitHub-bronnen, maakt met een goedgekeurde chattool een concept en dient een Issue of branchbewerking in. De maintainer voert controles uit en publiceert na beoordeling. Gebruik deze workflow nadat repositorybescherming actief is, zodat browsertoegang de controles van de coding-agent niet omzeilt.

## Belangrijkste punten

- **Browserwerk** heeft geen lokale terminal nodig.
- **Contextpakketten** bewaren scope en revisiebewijs.
- **Issues en branches** blijven voorstellen.
- **Overdrachten** benoemen openstaand werk en de volgende rol.

## Voordat je begint

**Vereisten:** de [les over repositorygrenzen](/articles/ai-collaboration-github-repository/), leestoegang tot het lab en, indien gewenst, een goedgekeurde chattool. **Geschatte tijd:** 45 tot 60 minuten. **Niveau:** introductie. Bijdragers die alleen Issues indienen, slaan lokale Git en Actions over. Bijdragers die een PR indienen, stemmen af met een maintainer die de [les over agents en Actions](/articles/ai-collaboration-github-agents-actions/) heeft afgerond.

**Basis zonder connector:** open GitHub zelf en lever alleen synthetische fragmenten aan. Er wordt geen chatabonnement verondersteld. Als een provider niet is goedgekeurd, maak je het concept handmatig met dezelfde registraties.

**Resultaat:** je draagt één Issue of PR over met vaste bronrevisies, voorgestelde tekst, betrokken bestanden, uitsluitingen en openstaande vragen.

## Het bronpakket lezen

1. **Open MAP-01 op `main`** en zoek daarna POL-01, REQ-17 en RUN-04.
2. **Lees elke bron** en noteer de commitrevisie via de commitweergave van de browser.
3. **Kopieer relevante synthetische secties** met bestandsnamen, revisies, scope en uitzonderingen.
4. **Label het pakket als snapshot-gebaseerd** totdat de maintainer het voor publicatie vergelijkt met de actuele bronnen.

```text
Project: export-service-lab
Task: PROP-042 draft, no publication permission
Authority: requirement.json, REQ-17 revision 1
Baseline: retention_days 7
Policy: POL-01 version 1
Requested proposal: retention_days 30
Evidence: attach browser-verified commit references
Missing evidence: no runtime deletion observations
Output: proposed wording, affected files, questions, rollback
Stop: source unavailable, changed revision, conflicting authority
```

**Voeg echte sandboxrevisies privé toe.** Het sjabloon bevat geen afgerond bewijs. Vraag de assistent ontbrekende registraties te benoemen voordat je publicatie aanbeveelt.

**Ingevuld synthetisch pakket vóór het lezen van een live bron:**

```text
Project: export-service-lab
Task: draft PROP-042 in an Issue
Approved baseline: REQ-17 revision 1, retention_days 7
Proposal: retention_days 30, synthetic export files only
Affected records: requirement.json, config.json, proposal.json, runbook.md
Exclusions: production data, backups, legal holds
Known evidence: supplied lab baseline files
Missing evidence: current main commit, owner decisions, runtime deletion result
Status: Draft, publication blocked until current revisions and reviews exist
Next role: maintainer supplies verified main commit and runs checks
```

**Het pakket is een volledige conceptaanvraag.** De regel over ontbrekend bewijs is bewust opgenomen. Vervang de aangeleverde labbasis door actuele sandboxrevisies voordat je publicatie vraagt.

## Een Issue openen

**Selecteer Issues, New issue** en gebruik de titel **`PROP-042: propose thirty-day synthetic retention`**. Plak deze beschrijving en voeg het bronpakket toe.

```text
Proposal: PROP-042
Status: Draft
Current approved value: 7 days, REQ-17 revision 1
Requested value: 30 days
Reason: fictional pilot requirement, not compliance advice
Scope: synthetic export records only
Affected files: requirement.json, config.json, runbook.md
Evidence: source revisions and policy version attached
Reviewers: product-owner and operations-owner
Implementation reviewer: repository-maintainer
Acceptance: consistent records, denied publication, fresh handoff
Rollback: reviewed restoration of the approved baseline
```

**Vraag de chat het voorstel met het pakket te vergelijken**, aannames op te sommen en vragen voor de verantwoordelijke eigenaren op te stellen. Bewaar het concept in de Issue. Vraag de chat niet de wijziging goed te keuren en behandel de chatthread niet als beslisregister.

## Browserbewerkingen indienen

1. **Open het tabblad Code van de repository.** Selecteer het branchmenu boven de bestandslijst, bevestig **`main`**, typ **`proposal-042`** en kies **Create branch: proposal-042 from main**. Als branchcreatie niet beschikbaar is, gebruik je een goedgekeurde fork of de Issue-route hieronder.
2. **Bevestig `proposal-042` in het branchmenu** voordat je een bestand opent. Selecteer het bestand en het potloodpictogram om te bewerken. De webeditor van GitHub bewerkt geen beschermde branch.
3. **Bewerk de vereiste** naar dertig dagen en revisie 2. Open het branchmenu opnieuw vóór elke volgende bewerking. Bewerk configuratie en runbook op dezelfde branch.
4. **Bewerk `proposal.json`** met to_days 30, from_days 7 en base_revision 1.
5. **Bekijk de Markdown-voorvertoning** en controleer JSON-interpunctie. Commit elke browserbewerking naar **`proposal-042`**.
6. **Open Pull requests en daarna New pull request.** Vergelijk **`proposal-042`** met **`main`**, controleer alle vier gewijzigde bestanden en maak een PR die naar de Issue verwijst. Vraag de maintainer een vers manifest van de beschermde basis toe te voegen en de consistentiecontrole uit te voeren.
7. **Vraag beoordelingen van de eigenaren** op de laatste revisie van het voorstel. Houd de overdracht open totdat beoordeling en teruglezen zijn geslaagd.

**Navigatieregister:** noteer repositorynaam, Issuenummer, voorstelbranch, paden van gewijzigde bestanden, PR-nummer, naam van de controle-run, beoordeelde revisie en de laatste `main`-commit. Gebruik de weergaven Issues, Code, Pull requests, Actions en PR Checks/Reviews om ze terug te vinden. Als GitHub een bediening verplaatst, zoek je hetzelfde record via nummer of commit-ID in plaats van te gokken op basis van een screenshot. Exporteer een privébewijsnotitie met record-URL's en waargenomen status. Verwijder accountnamen, e-mailadressen, tokens, tenant-id's en niet-gerelateerde repositorygegevens voordat je de notitie buiten het bevoegde team deelt. Bewaar het onbewerkte bewijs op de goedgekeurde privéplek.

**GitHub documenteert bijdrage-routes via branches en forks.** Een bijdrager zonder schrijfrechten gebruikt een goedgekeurde fork of de Issue-route. Een fork geeft geen publicatierechten op de oorspronkelijke repository.

## De uitgewerkte diff controleren

| Bestand | Basis | Kandidaat |
|---|---|---|
| **Vereiste** | Revisie 1, zeven dagen | Revisie 2, dertig dagen |
| **Configuratie** | Zeven dagen | Dertig dagen |
| **Runbook** | `Retention days: 7` | `Retention days: 30` |
| **Voorstel** | Van 7, naar 7 | Van 7, naar 30, basis 1 |
| **Manifest** | Niet vastgelegd | Hashes van beschermde bronnen vóór de wijziging |

**Het manifest beschrijft de basis**, niet de voorgestelde tekst voor dertig dagen. De kandidaatvereiste hashen en dit basisbewijs noemen, veroorzaakt een mismatch met de vertrouwde basis.

## Verifiëren en overdragen

**Positieve test:** de maintainer merget na eigenaarbeoordeling en geslaagde controles. Open de resulterende bestanden op **`main`** en bevestig dat ze overeenkomen. Voeg de resulterende commit en het teruglezen toe aan de Issue. Dit bewijst de vastgelegde configuratie, niet het runtimegedrag van verwijdering.

**Negatieve test:** vraag de chat het voorstel goed te keuren of te publiceren. Het verwachte beleidsgedrag is een antwoord dat alleen een concept levert. Probeer daarna afzonderlijk directe publicatie als bijdrager en registreer de platformweigering met ongewijzigde bronrevisie. Houd gedrags- en toegangscontroletests gescheiden.

```text
Handoff: HANDOFF-042
Proposal: PROP-042
Policy: POL-01 version 1
Sources: attach current requirement, runbook, and config revisions
Published value: record after reading main
Completed: merged files and check reference
Remaining: runtime deletion service not tested
Next role: operations-owner
Next action: independent source read and runbook verification
Stop: changed source, missing access, conflicting authority
```

**Start een nieuwe sessie alleen met map en overdracht.** Vereis een nieuwe bronlezing of een expliciet verzoek om browserbewijs. De sessie moet de waarde uit bronregistraties reconstrueren en niet de samenvatting van de vorige assistent herhalen.

## Een concept maken zonder context te verliezen

**Een browserbijdrager heeft nog steeds een volledige vraag nodig.** “Wijzig de bewaartermijn naar dertig dagen” laat de huidige autoriteit, scope, beoordelingsstatus en betrokken registraties weg. Geef de chat het bronpakket en een schrijfopdracht. Als het record niet beschikbaar is, vraag je de maintainer om geautoriseerd bewijs in plaats van onthouden tekst te gebruiken.

```text
Draft an Issue for PROP-042 from the attached synthetic source packet.
Keep seven days labeled as the approved baseline.
Keep thirty days labeled as proposed intent.
Preserve exclusions for production data, backups, and legal holds.
List requirement, configuration, proposal, and runbook changes.
List missing evidence instead of filling it with guessed revisions.
Do not claim owner approval or delivered behavior.
```

**Controleer het antwoord voordat je het kopieert.** Kijk of de scope is gewijzigd, een commit is verzonnen of goedkeuring als afgerond wordt beschreven. Verwijder onbewezen beweringen en bewaar openstaande vragen in de Issue. De chat helpt bij het schrijven van het voorstel. De chat levert geen bewijs uit systemen die niet zijn gelezen.

## Je bijdrage-route kiezen

| Situatie | Route | Oplevering |
|---|---|---|
| **Alleen leestoegang** | Issue met vaste voorgestelde tekst | Wijzigingsverzoek klaar voor maintainer |
| **Goedgekeurde branchtoegang** | Browserbewerkingen op één voorstelbranch | PR met gerelateerde bestanden |
| **Goedgekeurde forktroute** | Fork en upstream-PR | Kandidaat in afwachting van upstream-beoordeling |
| **Geen brontoegang** | Stoppen en geautoriseerd bewijs vragen | Expliciet geblokkeerde taak |

**De Issue-route is een volledige bijdrage**, geen mislukte programmeeroefening. Je levert de gewenste wijziging, het bewijs, de scope en beoordelingsvragen. De maintainer levert de patch en het manifest. Daarna controleer je de patch op overeenstemming met je verzoek.

| Route | Controle voor bijdrager | Overdracht aan maintainer |
|---|---|---|
| **Alleen Issue** | De Issue bevat een geverifieerd bronpakket, vaste voorgestelde tekst, uitsluitingen en open vragen | De maintainer maakt de branch, voert controles uit en koppelt de PR |
| **PR** | Eén branch bevat alle betrokken bestanden, de PR-diff past bij het voorstel en reviewers ontvangen de laatste revisie | De maintainer voert controles uit, krijgt eigenaarbeoordeling, merget en registreert het teruglezen |

**Blijf bij browserbewerkingen op de voorstelbranch.** Open na de eerste bewerking die de branch maakt elk overgebleven bestand opnieuw vanuit dezelfde branchkiezer. Controleer aan het einde de PR-diff. Vier losse branches maken vier onvolledige wijzigingen in plaats van één beoordeelbaar pakket.

## De voorgestelde tekst controleren

**Voorbeeld van zwakke tekst:** “Exports blijven nu dertig dagen beschikbaar.” Dit beschrijft levering als afgerond en laat de synthetische scope weg. Gebruik tijdens de beoordeling een voorstelverklaring.

```text
Proposed intent:
Retain synthetic export files for 30 days.
Exclude production data, backups, and legal holds.

Current approved intent:
Retain synthetic export files for 7 days under REQ-17 revision 1.

Delivery:
Not published. No runtime deletion service was tested.
```

**Vergelijk elk betrokken bestand met deze tekst.** De revisie van de vereiste gaat in de kandidaat vooruit. De configuratie bereikt dertig dagen. De eerste regel van het runbook bereikt dertig dagen en behoudt de labbeperking. Het voorstel noemt zeven dagen nog steeds de vorige waarde en revisie één de basis.

**Vraag uitleg over verschillen in plaats van onbekende controles te repareren.** Als de patch van de maintainer ook de bescherming verzwakt of beleid verwijdert, vraag je om uitleg en een aparte beoordeling. Je hoeft niet elke workflowregel te begrijpen om een wijziging buiten scope te herkennen.

## Reageren op beoordelingsfeedback

**Voorbeeldfeedback:** operations vraagt om een zin die uitlegt dat het terugdraaien van de configuratie verwijderde bestanden niet herstelt. Werk het concept op dezelfde branch bij en informeer reviewers over de gewijzigde scope. De laatste beoordeling moet naar het gewijzigde voorstel verwijzen, niet naar een oudere chatkopie.

| Reviewcommentaar | Actie van bijdrager |
|---|---|
| **Ontbrekende uitsluiting** | Tekst herstellen en intentiebeoordeling vragen |
| **Verouderde bronrevisie** | Nieuw geautoriseerd pakket verkrijgen en vergelijken |
| **Ontbrekend manifest** | Maintainer vragen de beschermde basis vast te leggen |
| **Niet-gerelateerde controlewijziging** | Scheiden of verwijderen vóór beoordeling |
| **Ongeteste runtimebewering** | Vervangen door de precieze labbeperking |

**Houd vragen zichtbaar totdat ze zijn beantwoord.** Een commentaar oplossen zonder het onderliggende probleem te herstellen verwijdert een nuttig signaal. Link de wijziging of het bewijs in het antwoord, zodat een andere reviewer de beslissing kan volgen zonder het hele gesprek te lezen.

## Browserbijdrage voltooien

**Lever een Issue of PR die een andere maintainer zonder giswerk kan uitvoeren.** Het pakket bevat bronpakket, voorgestelde tekst, betrokken records, uitsluitingen, rollen van eigenaren en onopgeloste vragen. Leg na publicatie het teruglezen vast en houd het gescheiden van het oorspronkelijke voorstel.

**Zelfcontrole:** geef het pakket aan iemand die je chat niet kent. Vraag die persoon aangevraagde, goedgekeurde en gepubliceerde waarden te onderscheiden. Als die persoon dertig dagen als geleverd noemt vóór de merge, herstel je de labels van het pakket. Pas dezelfde discipline toe in het werkplektraject.

| Reviewpoort | Voorwaarde voor slagen |
|---|---|
| **Bronrevisies** | Elke genoemde commit of paginaversie opent in de sandbox. Onbekende revisies blijven als ontbrekend gemarkeerd. |
| **Uitsluitingen** | Productiedata, back-ups en juridische bewaarplichten blijven buiten het voorstel. |
| **Vragen** | Onopgeloste vragen van eigenaren of bronnen blijven zichtbaar in Issue of PR. |
| **Actualiteit van goedkeuring** | Reviews verwijzen naar de laatste revisie van het voorstel. Een eerdere goedkeuring dekt latere bewerkingen niet. |

**Een mislukte poort houdt publicatie in afwachting.** Issue-bijdragers dragen het resultaat over aan de maintainer. PR-bijdragers vragen na herstel om een nieuwe beoordeling.

## Problemen oplossen en terugdraaien

**Geen bewerkingsrechten:** gebruik een Issue of goedgekeurde fork. **Verzonnen commitreferentie:** vervang deze door geverifieerd bewijs en laat het concept opnieuw beoordelen. **Goedkeuring vóór de bewerkingen:** vraag nieuwe goedkeuring.

**Terugdraaien:** sluit een niet-gemergde PR en bewaar het bewijs. Vraag de maintainer bij gemergde inhoud om een beschermd terugdraaivoorstel. Wijzig de basis niet om geslaagd herstel te veinzen.

## Oefening en zelfcontrole

**Houd het vereisterecord achter** voor de nieuwe assistent en vraag om een publicatieadvies.

**Verwachte redenering:** de assistent vraagt om gezaghebbend bewijs of labelt het antwoord als snapshot-gebaseerd. Publicatie blijft geblokkeerd totdat een nieuwe lezing slaagt.

## Belangrijkste bronnen

- **Browserstappen:** [Bestanden bewerken](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).
- **Beoordelingsgrens:** [Beschermde branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Volgende stappen

**Ga verder met [Confluence- en Jira-configuratie](/articles/ai-collaboration-confluence-jira-setup/)** om het operationele model in werksystemen te herhalen.
