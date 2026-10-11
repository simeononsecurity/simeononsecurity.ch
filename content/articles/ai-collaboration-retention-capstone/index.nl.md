---
title: "Capstone AI-samenwerking: GitHub, Confluence en Jira"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Lever een synthetische bewaartermijnwijziging via GitHub-first- en Confluence/Jira-workflows, met foutbewijs en onafhankelijke beoordeling."
genre: ["Kunstmatige intelligentie", "Teamsamenwerking", "Software-engineering"]
tags: ["AI-samenwerkingscursus", "bewaarvoorstel", "GitHub-review", "Confluence Jira-workflow", "foutmatrix", "onafhankelijke acceptatie"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustratie van professionals die gedeeld projectwerk beoordelen in een cybersecurity-werkruimte"
coverCaption: ""
---

[Terug naar de cursus AI-samenwerking](/ai-collaboration-course-start/)

**Lever PROP-042 twee keer**, via GitHub-first en via GitHub met Confluence/Jira. Jij draagt bij, afzonderlijke eigenaren beoordelen en geautoriseerde publiceerders passen de wijziging toe. Gebruik geïsoleerde synthetische sandboxes na de eerdere lessen. De capstone toetst de volledige procedure, inclusief afwijzing, herstel en onafhankelijke overdracht, niet de prozakwaliteit van de assistent.

## Belangrijkste punten

- **Eén gedeelde wijziging** vergelijkt beide autoriteitsmodellen.
- **Negatieve tests** zijn even belangrijk als geslaagde levering.
- **Bewijspakketten** ondersteunen onafhankelijke beoordeling.
- **Afronding van het lab** geeft geen toestemming voor productie-uitrol.

## Voordat je begint

**Vereisten:** eerdere [cursusmodules](/ai-collaboration-course-start/), goedgekeurde sandbox-toegang en afzonderlijke beoordelaars. **Planningsruimte:** acht tot twaalf uur over meerdere sessies, plus onafhankelijke beoordeling. De werkelijke tijd hangt af van accountinstellingen en herstelwerk. **Moeilijkheid:** gevorderd.

**Vereiste artefacten:** charter, kaart, beleid, adapters, baseline, manifest, vastgezet voorstel, eigenaarbeoordelingen, logboek, herstelrecord en overdracht. Ontbrekende plangebonden machtigingen blokkeren de voltooiing. Ze worden geen veronderstelde goedkeuringen.

**Maak vóór het testen één bewijsdirectory per spoor.** Een beoordelaar moet de actor, bronrevisies, geplande actie, waargenomen resultaat en eindstatus herkennen zonder op een chatsamenvatting te vertrouwen.

## Twee baselines vastleggen

1. **Maak geïsoleerde runs** met de namen GitHub-first en Mixed. Houd revisies en beoordelingen gescheiden.
2. **Herstel de zevendaagse baseline** via de goedgekeurde procedure van elk spoor en leg de resulterende revisies vast.
3. **Controleer weigeringscontroles** met accounts voor bijdragers en uitgesloten gebruikers.
4. **Leg de huidige context vast** en bevestig dat adapter en beleid overeenkomen.
5. **Verklaar de scope:** synthetische exportretentie van dertig dagen, exclusief echte gegevens, back-ups en wettelijke bewaarplichten.

**PROP-042 is een correlatielabel, geen herbruikbare goedkeuring.** Elke run heeft een eigen bevroren revisie en bronbewijs nodig. Neem run-ID's op in rapporten.

## Leveren met GitHub-first

**Open de Issue en kandidaat-PR** met de GitHub-lessen. Wijzig vereiste, configuratie, voorstel en runbook samen. Leg de beschermde basis vast, voer vertrouwde controles uit en verkrijg product- en operationsbeoordelingen op de definitieve commit.

```text
Run: GitHub-first
Change: synthetic retention 7 -> 30 days
Requirement: REQ-17 revision 2
Configuration: retention_days 30
Runbook: Retention days: 30
Proposal: base revision 1, from 7, to 30
Manifest: protected pre-change source hashes
Review: product and operations at final proposal revision
Publication: merged commit and read-back
Limit: no running deletion service exercised
```

**Vul de echte verwijzingen vanuit de sandbox in.** Het overzicht toont de verwachte koppeling, geen voltooid bewijs. De maintainer mergt pas na beoordeling en leest daarna onafhankelijk **`main`**. Sluit de Issue nadat je de definitieve records hebt gekoppeld.

## Het Mixed-spoor leveren

**Lees Confluence-versies en zet het Jira-voorstel vast.** Verkrijg beide eigenaarbeoordelingen. Publiceer de vereiste met levering in behandeling, merge de configuratie, publiceer het runbook en lees alle systemen terug voordat je Done gebruikt.

**Registreer elke publicatie** met paginaversie, commit of overgangsbewijs. Vereistekopieën in de repository blijven snapshots. De lokale checker bewijst niet welke Confluence-inhoud nu gezaghebbend is.

| Vergelijking | GitHub-first | Gemengde werkplek |
|---|---|---|
| **Vereiste** | Review van beschermde repository | Door Confluence-eigenaar beoordeelde publicatie |
| **Coördinatie** | Issue/PR | Vastgezet Jira-voorstel |
| **Publicatie-eenheid** | Repository-merge | Afzonderlijke paginawrites en merge |
| **Actualiteit** | Beschermde commit | Paginaversies plus commit |
| **Herstel** | Beoordeelde revert/compensatie | Door logboek gestuurde compensatie |

**Kies een workflow op basis van eigenaarschap.** GitHub-first vermindert coördinatie tussen systemen. Het Mixed-spoor behoudt de werkplekken en voegt publicatie- en toegangscontroles toe.

## De foutmatrix uitvoeren

| Geval | Injectie | Vereist waargenomen bewijs |
|---|---|---|
| **Goedgekeurde wijziging** | Dien een beoordeeld voorstel van dertig dagen in | Consistente read-back en review |
| **Verouderde context** | Wijzig de bron na vastlegging | Afwijzing, afstemming, hergoedkeuring |
| **Onbevoegde write** | Bijdrager publiceert | Weigering en ongewijzigde revisie |
| **Conflict** | Jira zegt zestig, Confluence zeven | Blokkade en afstemming door eigenaar |
| **Gedeeltelijke publicatie** | Onderbreek na één write | Openstaand logboek en herstel |
| **Toegangsweigering** | Verwijder taak-leestoegang | Geen beschermde tekst of publicatie |
| **Herstel** | Goedgekeurde afronding/backout | Nieuwe beoordeelde revisies |
| **Overdracht** | Nieuwe sessie krijgt alleen kaart en logboek | Nieuwe read en juiste volgende actie |

**Een conflict tussen systemen hoort bij Mixed.** Test in GitHub-first een Issue-beschrijving die strijdt met het goedgekeurde bestand. Voer de andere toepasselijke gevallen in beide sporen uit. Een lokale validatorfout vervangt geen live bewijs van machtigingen.

| Geval en bewijsbestand | GitHub-first-run | Mixed-run |
|---|---|---|
| **Goedgekeurde wijziging** `01-approved-change.md` | Beoordeelde PR en read-back | Beoordeelde pagina's, merge en logboek |
| **Verouderde context** `02-stale-context.md` | Beschermde basis na vastlegging wijzigen | Autoriteitspagina na vastlegging wijzigen |
| **Onbevoegde write** `03-unauthorized-write.md` | Direct-pushweigering voor bijdrager | Weigering van paginawijziging en overgang |
| **Conflict** `04-conflict.md` | Issue wijkt af van goedgekeurd bestand | Jira-tekst wijkt af van Confluence |
| **Gedeeltelijke publicatie** `05-partial-publication.md` | Stop vóór merge of read-back | Stop na één paginawrite |
| **Toegangsweigering** `06-access-denial.md` | Beschermde repositorybron achterhouden | Gebruiker uitsluiten van beperkte pagina |
| **Herstel** `07-recovery.md` | Beoordeelde revert of voltooiing | Door logboek gestuurde compensatie |
| **Overdracht** `08-handoff.md` | Nieuwe sessie leest beschermde bestanden | Nieuwe sessie leest gemapte pagina's en logboek |

**Maak elk bestand vóór de test.** Leg verwacht resultaat, waargenomen resultaat, actorrol, begin- en eindrevisies, native-bewijsverwijzing en beoordelaarsbesluit vast. Een browserrouteprompt bewijst geen direct-pushweigering. Houd beide spoordirectories gescheiden.

**Houd verwacht en waargenomen resultaat apart.** Noteer per geval run-ID, actorrol, beginrevisies, geplande actie, verwachting, observatie, resulterende revisies en beoordelaarsbesluit. Verwijder wachtwoorden en account-ID's uit gedeelde rapporten.

## Voltooiing beoordelen

**Slagen vereist waargenomen bewijs voor elke toepasselijke rij** en onafhankelijke acceptatie. Beoordelaars controleren machtigingen, bronactualiteit, rolreview, gedeeltelijke publicatie en overdrachtsreconstructie, naast consistentielogs.

**Faalt onmiddellijk** bij onbevoegde publicatie, geweigerde tekst die het model bereikt of stil overschrijven van een gewijzigde basis. Houd het werk geblokkeerd totdat gecorrigeerde controles een herhalingstest doorstaan. Middel zulke fouten niet weg in een gunstige score.

**Meet voltooide en geblokkeerde gevallen, afgewezen verouderde voorstellen, geweigerde writes, herstelacties en beoordelingstijd.** Voorgestelde uitkomsten blijven verwacht totdat ze zijn waargenomen. De tien geleverde unit-tests dekken consistentie, geen live tenantbeveiliging.

## De twee runs plannen

**Gebruik geen goedkeuring opnieuw tussen sporen.** De gevraagde waarde is gelijk, maar bronlocaties, vastgelegde revisies, machtigingen en publicatievolgorde verschillen. Geef iedere run een eigen bewijsdirectory en reviewpakket.

```text
capstone-evidence/
  github-first/
    charter-and-map
    captured-sources
    fixed-proposal
    role-reviews
    consistency-results
    permission-results
    publication-readback
    recovery-and-handoff
  mixed/
    same evidence categories, independently captured
```

**Deze namen zijn een organisatievoorbeeld**, geen aangeleverde archiefbestanden. Bewaar echt bewijs privé in de goedgekeurde sandbox. Gedeelde cursusinzendingen gebruiken rollabels en geredigeerde verwijzingen. Beoordelaars behouden toegang tot native records.

**Wijs vóór het uitvoeren van fouten een testwaarnemer aan.** De bijdrager voert de actie uit. De waarnemer noteert beginstatus, uitkomst en eindstatus. Een beoordelaar bepaalt later of het bewijs de claim ondersteunt. Meld rol-overlap in plaats van onafhankelijke acceptatie te suggereren.

## Fouten geïsoleerd uitvoeren

**Reset tussen gevallen naar een geverifieerde, beoordeelde toestand.** Als je bronafwijking, toegangsintrekking en een runbook-mismatch tegelijk injecteert, blijft onduidelijk welke controle het voorstel heeft geweigerd. Eén fout per run geeft de beoordelaar een traceerbare reden.

1. **Leg de beginstatus vast:** bronrevisies, configuratie, leveringsstatus en actorrol.
2. **Pas één synthetische injectie toe:** wijzig één relevante voorwaarde via een geautoriseerde testroute.
3. **Probeer de begrensde actie:** validatie, lezen, publicatie of overdracht.
4. **Registreer de observatie:** echte uitvoer en resulterende bronstatus.
5. **Herstel via review:** bewaar foutbewijs voordat je controles terugzet.
6. **Herhaal het positieve geval:** bevestig dat de gecorrigeerde workflow toegestaan werk blijft leveren.

**Een geplande fout blijft een foutobservatie.** Noem een onbevoegde publicatie geen geslaagde test omdat je de controle wilde onderzoeken. De test legde een defect bloot. De publicatiegrens faalde en vereist herstel.

## Een gemengd resultaat interpreteren

**Illustratief bewijspakket:** lokale consistentie slaagt, product en operations beoordelen het vaste pakket, publicatie van de vereiste slaagt en wijzigingstoegang tot het runbook wordt geweigerd. De configuratie is nog niet gemerged. Jira blijft Blocked.

| Claim | Oordeel | Reden |
|---|---|---|
| **Kandidaatrecords komen overeen** | Ondersteund door lokale controle | Aangeleverde records doorstonden vergelijkingen |
| **Eigenaren accepteerden intentie en operations** | Vereist native vaste reviews | Rollabels alleen zijn onvoldoende |
| **Dertig dagen levering voltooid** | Niet ondersteund | Vereiste publicatiestappen blijven open |
| **Machtigingsgrens werkt voor elke rol** | Niet ondersteund | Eén geweigerde actie heeft beperkte reikwijdte |
| **Hersteleigenaar moet handelen** | Ondersteund als volgende stap | Gedeeltelijke levering vereist een beoordeeld besluit |

**Verwachte redenering:** houd de run onvoltooid, controleer actuele bronnen en vraag het juiste eigenaarbesluit. Rond niet af door machtigingen te verzwakken of de snapshotcontrole als live publicatiebewijs te beschrijven.

## Review met een onafhankelijke lezer

**Vraag de beoordelaar gebeurtenissen te reconstrueren**, niet alleen je conclusie te lezen. Die moet goedgekeurde baseline, vastgezet voorstel, eigenaarsbesluiten, resulterende revisies, mislukte pogingen, herstel en resterende hiaten vinden zonder jouw vertelling.

```text
Reviewer questions:
Which source governs retention intent in this track?
Which exact package did each owner review?
Did any source change after review?
What was published, and what remains pending?
Which denied action was observed under which role?
Did protected text reach an excluded user's context?
Which repair was reviewed and read back?
Does the fresh handoff reconstruct current state independently?
```

**Scoor iedere vereiste afzonderlijk.** Gebruik Supported, Failed, Blocked of Not run met een bewijsverwijzing. Consistentie, goedkeuring, machtigingen, herstel en overdracht zijn aparte vereisten. Een verzameling groene lokale tests compenseert geen mislukte live-publicatiegrens.

```text
Run ID and track:
Reviewer role and review date:
Case 01 approved change: status ___ evidence ___ gap ___
Case 02 stale context: status ___ evidence ___ gap ___
Case 03 unauthorized write: status ___ evidence ___ gap ___
Case 04 conflict: status ___ evidence ___ gap ___
Case 05 partial publication: status ___ evidence ___ gap ___
Case 06 access denial: status ___ evidence ___ gap ___
Case 07 recovery: status ___ evidence ___ gap ___
Case 08 handoff: status ___ evidence ___ gap ___
Overall decision: Supported / Failed / Blocked / Not run
Next accountable role and action:
```

**Supported betekent dat de beoordelaar waargenomen bewijs vond voor elk toepasselijk geval.** Noteer Failed voor een waargenomen controlefout, Blocked voor ontbrekende toegang of controle en Not run voor een niet-uitgevoerd geval. Bewaar iedere native verwijzing in het genoemde bewijsbestand.

**Slagingspoort van de cursus:** voltooi GitHub-first en Mixed. In beide sporen moeten alle acht toepasselijke gevallen Supported zijn. Een Failed-grens of ontbrekende native read-back blokkeert het spoor. Een ontbrekend betaald plan of testidentiteit levert Blocked op, geen veronderstelde pass. Eén voltooid spoor levert een gedocumenteerd gedeeltelijk resultaat, geen cursusvoltooiing.

**Geredegeerd modelpakket, alleen illustratief:**

```text
Track: github-first | Run: G-01 | Reviewer: separate pilot role
Base: protected commit base-001 | Fixed proposal: PROP-042 r1
Approvals: product review ref P-01, operations review ref O-01
Consistency: local check pass, saved output ref C-01
Permission: contributor direct push denied, native event ref D-01
Publication: merged commit merge-002, fresh clone confirms thirty
Exception: backups and legal holds remain excluded
Recovery: interruption case R-01 read back and resolved through review
Handoff: second reader found current base, exception, and next action
Runtime limit: no production deletion or deployment claim
Decision: Supported for synthetic GitHub-first track only
```

Vervang iedere illustratieve verwijzing door een waargenomen sandbox-artefact. Herhaal het volledige pakket voor Mixed met eigen bronversies en reviews. De beoordelaar moet een gekopieerde GitHub-goedkeuring in het Mixed-pakket afwijzen.

## Een begrensd besluit schrijven

**Een nuttig slotbesluit benoemt de volgende pilot**, geen onbeperkte uitrol. Kies bijvoorbeeld een andere synthetische exportinstelling met dezelfde rollen en directe lookup-route, terwijl echte gegevens en automatische publicatie buiten scope blijven.

| Besliselement | Vereist detail |
|---|---|
| **Scope** | Eén volgende wijziging en expliciete uitsluitingen |
| **Bewijs** | Ondersteunde gevallen en onopgeloste fouten |
| **Controles** | Platformafgedwongen en procedurele vereisten afzonderlijk |
| **Eigenaren** | Verantwoordelijke rol voor elk resterend gat |
| **Runtime-gat** | Niet-getest verwijder- of deploymentgedrag |
| **Stopvoorwaarden** | Ontbrekende toegang, gewijzigde autoriteit, onbevoegde publicatie |

**Voltooiingscontrole:** beide runpakketten overleven onafhankelijke reconstructie, toepasselijke foutgevallen hebben waargenomen bewijs en onopgeloste controles blijven zichtbaar. Als alleen GitHub klaar is, rapporteer gedeeltelijke cursusvoltooiing in plaats van aan te nemen dat Mixed hetzelfde werkt.

## Probleemoplossing en backout

**Alleen happy-path-bewijs:** herhaal weigering- en onderbrekingstests. **Overlappende rollen:** meld ze en herhaal met afzonderlijke gebruikers. **Ontbrekende plancontroles:** stop en verkrijg een goedgekeurde sandbox.

**Backout:** herstel de baseline via beoordeelde PR's en Confluence-wijzigingen, trek tijdelijke integraties in, archiveer Jira-bewijs en voer goedgekeurde synthetische opschoning uit na bewijsretentie. Bewaar de herstelgeschiedenis.

## Het uitrolbesluit maken

```text
Decision: another synthetic pilot, blocked, or rejected
Evidence: both run packages and failure matrix
Unenforced requirements: procedural controls listed explicitly
Provider review: input scope and retention handling
Owner coverage: product, operations, policy, repository, delivery
Production gaps: runtime tests, secrets, deployment, access review
Next action: one bounded follow-up with accountable role
Review date: assigned by pilot owners
```

**Verwachte redenering:** synthetisch succes ondersteunt nog één begrensde pilot. Productie vereist afzonderlijke goedkeuring voor echte gegevens, deployment, verwerking door de provider en runtimegedrag. Een geslaagd assistentantwoord is geen deploymentautorisatie.

## Primaire referenties

- **Repositorycontroles:** [Beschermde branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Werkplektoegang:** [Confluence-machtigingen](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Leveringscontroles:** [Jira-machtigingsschema's](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).

## Volgende stappen

**Ga terug naar de [cursushub](/ai-collaboration-course-start/)** om ontbrekende controles te bekijken. Vergelijk je implementatie met [het frameworkartikel](/articles/one-source-many-tools-ai-collaboration-framework/) voordat je een volgende pilot kiest.
