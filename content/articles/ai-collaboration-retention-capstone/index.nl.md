---
title: "Capstone AI-samenwerking: GitHub, Confluence en Jira"
date: 2026-10-01
lastmod: 2026-11-13
toc: true
draft: false
description: "Lever een synthetische bewaartermijnwijziging via GitHub-first- en Confluence/Jira-workflows, met foutbewijs en onafhankelijke beoordeling."
genre: ["Kunstmatige intelligentie", "Teamsamenwerking", "Softwareontwikkeling"]
tags: ["AI-samenwerkingscursus", "bewaarvoorstel", "GitHub-beoordeling", "Confluence-Jira-werkwijze", "foutmatrix", "onafhankelijke acceptatie"]
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
Uitvoering: GitHub-first
Wijziging: synthetische bewaring 7 -> 30 dagen
Vereiste: REQ-17 revisie 2
Configuratie: retention_days 30
Runbook: bewaartermijn: 30 dagen
Voorstel: basisrevisie 1, van 7, naar 30
Manifest: beschermde bronhashes van vóór de wijziging
Beoordeling: beoordeling door product en operations van de definitieve voorstelversie
Publicatie: samengevoegde commit en herlezing ter controle
Limiet: geen actieve verwijderingsservice getest
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
    dezelfde bewijscategorieën, onafhankelijk verzameld
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

**Injectie- en resetkaart per geval:** gebruik vóór het volgende geval een nieuw synthetisch voorstel of herstel een beoordeelde basis. De observator legt de voorwaarde vast en bevestigt de reset. Wis de mislukte poging nooit uit het ledger.

| Geval | Injectie en controle: GitHub-first | Injectie en controle: Mixed | Reset vóór het volgende geval |
|---|---|---|---|
| Goedgekeurde wijziging | Dien de vastgezette PR in, haal beide beoordelingen op, merge en open `main` opnieuw | Publiceer REQ-17, merge de beoordeelde diff, publiceer RUN-04 en lees alle records opnieuw | Leg de eindversies vast als nieuwe basis |
| Verouderde context | Leg een manifest vast, wijzig daarna de testbasis met een aparte beoordeelde PR voordat je het oude voorstel valideert | Leg paginaversies vast en laat een bevoegde editor een testpagina wijzigen vóór de prewrite-read | Stop, vergelijk versies, leg nieuwe bronnen vast en laat een nieuw pakket beoordelen |
| Onbevoegde schrijfactie | Contributor probeert een onschuldige directe push naar beschermd `main` en legt de serverweigering vast | Contributor probeert REQ-17 te bewerken en naar Approved over te gaan | Lees commit, paginaversie en Jira-status opnieuw en bevestig dat ze ongewijzigd zijn |
| Conflict | Het Issue-concept zegt zestig dagen, het goedgekeurde bestand zeven | Het Jira-concept zegt zestig dagen, REQ-17 zeven | De producteigenaar stemt het concept af en legt de beslissing vast |
| Gedeeltelijke publicatie | Stop na goedkeuring maar vóór merge of teruglezen, en laat het Issue open | Stop na teruglezen van REQ-17 terwijl configuratie en RUN-04 nog zeven aangeven | Houd levering in behandeling en vraag een beoordeeld besluit over afronding of compensatie |
| Toegang geweigerd | Een uitgesloten testidentiteit probeert een synthetische bron uit een privétestrepository te lezen | De uitgesloten identiteit probeert een beperkte synthetische pagina te openen | Herstel alleen goedgekeurde testtoegang en controleer of de gewone lezer nog toegang heeft |
| Herstel | Onderbreek een goedgekeurde testwijziging en stel na beoordeling afronding of revert voor | Gebruik het ledger voor gedeeltelijke publicatie om beoordeelde afronding of compensatie voor te stellen | Lees elke bron opnieuw en stem het ledger ermee af |
| Overdracht | Stuur MAP-01 en het ledger zonder de oude chat naar een nieuwe reviewer | Stuur toegewezen pagina-ID's en het ledger zonder de oude chat naar een nieuwe reviewer | De reviewer opent de huidige bronnen en noteert de volgende toegestane stap |

Leg bij elk geweigerd geval de platformreactie en een tweede lezing van het beschermde record vast. Controleer voor de uitgesloten gebruiker providertraces, ophaallogs of auditgegevens om na te gaan of beschermde tekst de taak bereikte. Ontbreekt dit bewijs, markeer de toegangsveiligheidscontrole als Blocked. Een zichtbare weigering bewijst niet dat geen gecachet fragment is teruggegeven. Ontbreekt de controle in het plan of een goedgekeurde testidentiteit, noteer dan Blocked in plaats van een geslaagde test te simuleren.



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

**Ingevuld leerpakket voor Mixed, synthetisch en geen bewijs uit een tenant:**

```text
Uitvoering: MIXED-042-example
Vastgelegde basis: REQ-17 v4 = 7 dagen; RUN-04 v2 = 7 dagen.
GitHub main base-001 config.json = {"retention_days": 7}; Jira PROP-042 r1 = In Review.
Vast voorstel: REQ-17 v5 stelt 30 dagen bewaring van synthetische exports in. Productiegegevens, back-ups en wettelijke bewaarplichten vallen erbuiten.
GitHub config.json wijzigt retention_days van 7 naar 30. RUN-04 v3 vermeldt 30 dagen; in het lab draait geen verwijderdienst. Onvolledige publicatie blijft open.
Beoordeling: producteigenaar keurt de exacte REQ-17-tekst goed. Operations keurt de configuratiediff en runbook op r1 goed.
Publicatie: uitgever leest REQ-17 v5 en RUN-04 v3 opnieuw en bevestigt 30 dagen; beheerder leest main op merge-002 met retention_days 30.
Geweigerde actie: bijdrager mag REQ-17 v5 niet bewerken. Uitgever bevestigt dat niets is gewijzigd; waarnemer bewaart platformbewijs.
Herstel: RUN-04-poging mislukt en Jira blijft Blocked. Operations keurt een nieuwe poging goed; na herlezing van v3 wordt Jira Done.
Overdracht: nieuwe reviewer krijgt MAP-01 en logboek, leest de drie bronnen en Jira, en noteert 30 dagen en de open runtimekloof.
Beperking: alleen bronpublicatie is aangetoond. Verwijdertijd: niet uitgevoerd.
```

## Review met een onafhankelijke lezer

**Vraag de beoordelaar gebeurtenissen te reconstrueren**, niet alleen je conclusie te lezen. Die moet goedgekeurde baseline, vastgezet voorstel, eigenaarsbesluiten, resulterende revisies, mislukte pogingen, herstel en resterende hiaten vinden zonder jouw vertelling.

```text
Vragen voor onafhankelijke beoordeling:
Welke bron bepaalt de bewaartermijn in deze route?
Welk exact pakket beoordeelde elke eigenaar?
Is een bron na de beoordeling gewijzigd?
Wat is gepubliceerd en wat staat nog open?
Welke geweigerde actie is onder welke rol waargenomen?
Heeft beschermde tekst de context van een uitgesloten gebruiker bereikt?
Welke reparatie is beoordeeld en opnieuw gelezen?
Kan de nieuwe overdracht de huidige status onafhankelijk reconstrueren?
```

**Scoor iedere vereiste afzonderlijk.** Gebruik Supported, Failed, Blocked of Not run met een bewijsverwijzing. Consistentie, goedkeuring, machtigingen, herstel en overdracht zijn aparte vereisten. Een verzameling groene lokale tests compenseert geen mislukte live-publicatiegrens.

```text
Uitvoerings-ID en route:
Reviewrol en datum:
Geval 01 goedgekeurde wijziging: status ___ bewijs ___ kloof ___
Geval 02 verouderde context: status ___ bewijs ___ kloof ___
Geval 03 ongeoorloofde schrijfactie: status ___ bewijs ___ kloof ___
Geval 04 conflict: status ___ bewijs ___ kloof ___
Geval 05 gedeeltelijke publicatie: status ___ bewijs ___ kloof ___
Geval 06 toegang geweigerd: status ___ bewijs ___ kloof ___
Geval 07 herstel: status ___ bewijs ___ kloof ___
Geval 08 overdracht: status ___ bewijs ___ kloof ___
Eindoordeel: Onderbouwd / Mislukt / Geblokkeerd / Niet uitgevoerd
Volgende verantwoordelijke rol en actie:
```

**Supported betekent dat de beoordelaar waargenomen bewijs vond voor elk toepasselijk geval.** Noteer Failed voor een waargenomen controlefout, Blocked voor ontbrekende toegang of controle en Not run voor een niet-uitgevoerd geval. Bewaar iedere native verwijzing in het genoemde bewijsbestand.

**Slagingspoort van de cursus:** voltooi GitHub-first en Mixed. In beide sporen moeten alle acht toepasselijke gevallen Supported zijn. Een Failed-grens of ontbrekende native read-back blokkeert het spoor. Een ontbrekend betaald plan of testidentiteit levert Blocked op, geen veronderstelde pass. Eén voltooid spoor levert een gedocumenteerd gedeeltelijk resultaat, geen cursusvoltooiing.

**Geredegeerd modelpakket, alleen illustratief:**

```text
Route: github-first | Uitvoering: G-01 | Reviewer: onafhankelijke pilotrol
Basis: beschermde commit base-001 | Vast voorstel: PROP-042 r1
Goedkeuringen: productbeoordeling P-01, operationsbeoordeling O-01
Consistentie: lokale controle geslaagd, uitvoer C-01 opgeslagen
Toegang: directe push door bijdrager geweigerd, native gebeurtenis D-01
Publicatie: commit merge-002; nieuwe clone bevestigt 30 dagen
Uitzondering: back-ups en wettelijke bewaarplichten uitgesloten
Herstel: onderbreking R-01 opnieuw gelezen en na beoordeling opgelost
Overdracht: tweede lezer vond huidige basis, uitzondering en volgende stap
Runtimegrens: geen claim over verwijdering of productie-uitrol
Oordeel: alleen onderbouwd voor synthetische GitHub-first-route
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
Besluit: nieuwe synthetische pilot, geblokkeerd of afgewezen
Bewijs: beide uitvoeringspakketten en foutmatrix
Niet afgedwongen eisen: procedurele controles expliciet opsommen
Providerbeoordeling: invoerbereik en bewaring
Verantwoordelijkheid: product, operations, beleid, repository, levering
Productiekloven: runtimetests, geheimen, uitrol, toegangscontrole
Volgende stap: beperkte vervolgactie met verantwoordelijke rol
Beoordelingsdatum: vastgesteld door piloteigenaren
```

**Verwachte redenering:** synthetisch succes ondersteunt nog één begrensde pilot. Productie vereist afzonderlijke goedkeuring voor echte gegevens, deployment, verwerking door de provider en runtimegedrag. Een geslaagd assistentantwoord is geen deploymentautorisatie.

## Primaire referenties

- **Repositorycontroles:** [Beschermde branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Werkplektoegang:** [Confluence-machtigingen](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Leveringscontroles:** [Jira-machtigingsschema's](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).

## Volgende stappen

**Ga terug naar de [cursushub](/ai-collaboration-course-start/)** om ontbrekende controles te bekijken. Vergelijk je implementatie met [het frameworkartikel](/articles/one-source-many-tools-ai-collaboration-framework/) voordat je een volgende pilot kiest.
