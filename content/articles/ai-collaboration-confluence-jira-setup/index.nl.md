---
title: "Confluence en Jira AI instellen: machtigingen en bevoegdheden"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Configureer gezaghebbende Confluence-pagina’s en Jira-machtigingen voor bedrijfsbeheerde samenwerking tussen teams na beoordeling."
genre: ["Kunstmatige intelligentie", "Teamwerk", "Softwareontwikkeling"]
tags: ["AI-samenwerkingscursus", "Confluence Cloud", "Jira Cloud", "gezaghebbende pagina’s", "Jira-machtigingenschema", "workflowovergang", "toegangstests"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustratie van professionals die gedeeld projectwerk beoordelen in een cybersecuritywerkruimte"
coverCaption: ""
---

[Terug naar de AI-samenwerkingscursus](/ai-collaboration-course-start/)

**De beheerder stelt eerst de bevoegdheden op de werkplek vast en koppelt daarna chattools.** Product- en operationele eigenaren publiceren eisen en draaiboeken in Confluence Cloud. Jira Cloud coördineert de uitvoering. GitHub beheert de implementatie. Je bouwt pas na de basis aparte testomgevingen, omdat een onjuiste machtiging informatie blootlegt, ongeacht het gedrag van een model.

## Belangrijkste punten

- **Confluence** beheert de goedgekeurde formulering van eisen.
- **Jira** beheert de uitvoeringsstatus, niet het bewaarbeleid.
- **GitHub** beheert configuratie en gedeeld beleid.
- **Toegangstests** vereisen geschikte abonnementen en afzonderlijke gebruikers.

## Voordat je begint

**Vereisten:** de [basis](/articles/ai-collaboration-pilot-foundation/), de labrepository, beheer van Confluence-ruimtes, Jira-beheer en afzonderlijke gebruikers voor bijdrager, eigenaar en uitgever. **Geschatte tijd:** 90 tot 120 minuten. **Moeilijkheid:** geavanceerd beheer.

**Abonnementseis:** Confluence Free ondersteunt geen inhoudsbeperkingen. Jira Free biedt geen instelbare machtigingenschema’s, ruimterollen of beveiligingsschema’s voor werkitems. Gebruik voor dit traject geschikte testomgevingen met Standard of hoger. Controleer vóór het testen het abonnement en de bevoegdheden aan de hand van de bronnen.

**Navigatie:** de huidige Jira-documentatie gebruikt “ruimte” en “werkitem”. Sommige tenants gebruiken nog “project” en “issue”. Kies een bedrijfsbeheerde configuratie. Dit stappenplan behandelt geen machtigingen in teambeheerde omgevingen. Rovo, Marketplace-apps, goedkeuringen in Jira Service Management en een betaalde chatconnector zijn niet nodig.

**Resultaat:** je eindigt met een machtigingenmatrix, benoemde gezaghebbende pagina’s, een Jira-workflow voor alleen het lab en bewijs van geweigerde toegang met afzonderlijke gebruikers. Noteer het tenantabonnement en de aannames over rollen bij de testresultaten.

**Controleer dit voordat je records maakt:**

| Controle | Beschikbaar | Ontbreekt |
|---|---|---|
| Paginabeperkingen en ruimtebeheer in Confluence | Maak aparte goedgekeurde en uitgesloten pagina’s | Markeer tests voor bewerken en geweigerde leestoegang als Geblokkeerd |
| Machtigingenschema en workflow-editor voor bedrijfsbeheerde Jira | Kopieer een schema en workflow voor alleen het lab | Markeer overgangstests als Geblokkeerd |
| Afzonderlijke gebruikers voor bijdrager, eigenaar, uitgever en uitgesloten gebruiker | Voer positieve en negatieve tests per rol uit | Markeer niet-geteste rollen als Geblokkeerd |
| Repositorybeheerder en beveiligde branch | Koppel de beoordeelde implementatieroute | Voltooi eerst het GitHub-traject voordat je gemengd publiceert |

Gebruik vanaf oktober 2026 de knop **Share** of de beperkingsinstelling voor toegang tot een pagina, het gebied met machtigingen onder **Space settings** in Confluence voor bredere rechten en **Settings > Work items > Permission schemes** in Jira voor het labschema. De workflow-editor voor bedrijfsbeheerde Jira bepaalt de overgangen. UI-labels en abonnementsfuncties verschillen per tenant. Noteer vóór deze stappen het werkelijke pad en abonnement bij je bewijs. Zie [machtigingen op Confluence-paginaniveau](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/) en [Jira-machtigingenschema’s](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/).

## Gezaghebbende pagina’s maken

1. **Maak een Confluence-ruimte** met de naam **`Export Service Lab`**. Schakel anonieme toegang en openbaar delen uit via de beschikbare site- en ruimte-instellingen.
2. **Maak gepubliceerde pagina’s**, geen live documenten, met de namen **`REQ-17 Export Retention`**, **`RUN-04 Export Cleanup`** en **`Decision Register`**.
3. **Publiceer de eerste eis** hieronder als producteigenaar. Noteer de werkelijke pagina-ID en versie in de repositorykaart.
4. **Publiceer RUN-04** als operationeel eigenaar, met een bewaartermijn van zeven dagen en de uitleg dat in dit lab geen verwijdertaak draait.
5. **Open Share** op elke gezaghebbende pagina. Stel de algemene toegang in op alleen-lezen voor geschikte ruimtedeelnemers en geef aangewezen eigenaren en uitgevers afzonderlijk bewerkingsrechten. Sla op en controleer dit met de bijdrager.

```text
Source ID: REQ-17
Owner role: product-owner
Status: Approved baseline
Scope: synthetic export files only
Retention: 7 days
Delivery state: baseline lab configuration
Exceptions: production data, backups, and legal holds excluded
Approval evidence: DEC-12 baseline review
Implementation reference: attach protected GitHub baseline commit
```

**Pas beperkingen toe op elke gezaghebbende pagina.** Ga er niet van uit dat een bewerkingsbeperking op een bovenliggende pagina ook de onderliggende pagina’s beschermt. Overerving van lees- en bewerkingsrechten werkt verschillend en ruimtemachtigingen blijven gelden. Een koppeling geeft op zichzelf geen toegang. Controleer alle lidmaatschappen als een gebruiker met vermeend alleen-lezen toegang toch kan bewerken.

**Gebruik deze begininhoud voor de andere twee pagina’s.** Vervang tijdelijke beoordelingsvelden door werkelijk bewijs uit de testomgeving voordat je een record goedkeurt.

```text
Source ID: RUN-04
Owner role: operations-owner
Status: Approved baseline
Scope: synthetic export files only
Configured retention: 7 days
Procedure: compare REQ-17 with config.json before a reviewed change
Runtime limit: this lab has no deletion job and produces no deletion evidence
Recovery: restore the prior approved configuration through review
Recovery limit: restoring configuration does not restore deleted files
Review evidence: add actual reviewer, page version, and decision reference
```

```text
Page: Decision Register
Entry ID: DEC-12
Decision: use seven days as the synthetic baseline
Scope: export-service-lab only
Requirement: REQ-17 page version, record after publication
Runbook: RUN-04 page version, record after publication
Policy: POL-01 protected GitHub revision, record after review
Product review: pending until the named owner records a decision
Operations review: pending until the named owner records a decision
Status: draft example, replace with observed review evidence
```

## De kaart bijwerken

```yaml
track: mixed-workplace
policy: {source_id: POL-01, home: GitHub, version: 1}
requirements: {source_id: REQ-17, home: Confluence, owner_role: product-owner}
runbook: {source_id: RUN-04, home: Confluence, owner_role: operations-owner}
decisions: {source_id: DEC-12, home: Confluence, owner_role: project-lead}
implementation: {home: GitHub, file: config.json}
delivery: {home: Jira, proposal_id: PROP-042}
snapshot_rule: repository requirement copies are not authoritative
```

**Voeg de werkelijke privé-locaties van de testomgeving en pagina-ID’s** toe aan de kaart. De sjabloon benoemt bevoegdheden zonder te doen alsof er live adressen in staan. Verwijder README-tekst die de gekopieerde JSON aanwijst als bron voor eisen in het gemengde traject.

**Bewaar POL-01 in GitHub** voor beide trajecten. Confluence verwijst naar de beoordeelde revisie. Als je tijdens een taak de beleidsbron verplaatst, is opnieuw een beoordeelde overdracht van bevoegdheden nodig.

## Jira-machtigingen instellen

1. **Maak een bedrijfsbeheerde labruimte** en kopieer een machtigingenschema naar een afzonderlijk labschema. Wijzig geen gedeeld productieschema.
2. **Open Settings, Work items, Permission Schemes**, selecteer het labschema en pas de rechten aan.
3. **Geef bijdragers rechten om te bekijken, maken en reageren.** Beperk beheerdersrechten. Controleer bewerkingsrechten en de machtiging **Transition work items** afzonderlijk.
4. **Koppel het schema** aan de labruimte en controleer dat geen productieruimte het deelt.
5. **Maak PROP-042** als werkitem. Noteer de gegenereerde sleutel op de kaart en houd PROP-042 als logisch voorstel-ID in de beschrijving.

**Plak deze concepttekst in PROP-042.** Het Jira-item volgt de uitvoering. De tekst vervangt de goedgekeurde formulering in Confluence niet.

```text
Proposal ID: PROP-042
Status: Draft
Current approved value: 7 days, REQ-17 page version to record
Proposed value: 30 days for synthetic export files
Exclusions: production data, backups, legal holds
Affected records: REQ-17, RUN-04, config.json, proposal.json
Fixed proposal attachment: pending
Product-owner review: pending
Operations-owner review: pending
Publication ledger: pending
Stop on changed source version, missing review, or denied access
```

| Rol | Confluence | Jira | GitHub |
|---|---|---|---|
| **Bijdrager** | Goedgekeurde pagina’s lezen | Concepten maken en erop reageren | Voorstelbranch of issue |
| **Producteigenaar** | Eis beoordelen | Beoordeling van de eis vastleggen | Bewijs in de PR beoordelen |
| **Operationeel eigenaar** | Draaiboek beoordelen | Operationele beoordeling vastleggen | Operationele impact beoordelen |
| **Uitgever** | Goedgekeurde pagina’s bewerken | Publicatiestatus vastleggen | Geen automatische bevoegdheid om samen te voegen |
| **Beheerder** | Eis lezen | Implementatie vastleggen | Beveiligde PR beoordelen en samenvoegen |

**Rechten uit verschillende groepen worden opgeteld.** Verwijder onbedoeld brede rechten in het lab. Ga er niet van uit dat een beperkte toekenning een brede toekenning opheft. Plaats connectoridentiteiten niet in beheerdersgroepen.

## Uitvoeringsstatussen instellen

**Kopieer een bedrijfsbeheerde workflow** naar een workflow voor alleen het lab. Voeg de statussen Concept, Beoordeling, Goedgekeurd, Publicatie, Gereed en Geblokkeerd toe. Voeg overgangen toe voor indienen, goedkeuren, publiceren, voltooien, blokkeren en terugkeren naar beoordeling. Koppel de workflow alleen aan het labwerkitemtype.

1. **Selecteer de overgang naar Goedgekeurd** in de workflow-editor.
2. **Voeg een voorwaarde of beperking toe** zodat alleen de aangewezen eigenaar/uitgeverrol of -groep de overgang activeert. Gebruik de gedocumenteerde voorwaarden en publiceer de workflowconceptversie als beheerder.
3. **Controleer handmatig beide beoordelingen van eigenaren** vóór de overgang. Elke beoordeling verwijst naar de vastgezette voorstel- en bronversies.
4. **Beperk Gereed** tot de verantwoordelijke uitvoeringsrol. Verwijder alternatieve of globale overgangen die deze grens omzeilen.

**Een beperkte overgang is geen goedkeuring door twee personen.** De beperking bepaalt wie de overgang uitvoert. In deze pilot blijft de controle op bewijs van beide rollen een procedurele stap. Leg deze beperking expliciet vast.

**Voorbeeld van een overgangsrecord:** Sta voor **Beoordeling naar Goedgekeurd** alleen de aangewezen groep van eigenaren en uitgevers toe. Vóór de overgang opent de uitvoerder de vaste bijlage van PROP-042 en controleert hij of er een besluit van de producteigenaar en de operationele eigenaar bestaat voor dezelfde voorstelrevisie. Ontbreekt een besluit of verwijst het naar een oudere revisie, laat het item dan op Beoordeling staan en noteer het ontbrekende bewijs. De workflowbeperking bepaalt wie de overgang uitvoert. De bewijscontrole is een afzonderlijke menselijke stap.

## Toegang weigeren controleren

**Als bijdrager**, lees REQ-17, probeer de pagina te bewerken, maak het Jira-concept en probeer de overgang naar Goedgekeurd. Verwacht dat de eis leesbaar is, bewerken wordt geweigerd, het voorstel wel wordt aangemaakt en goedkeuring wordt geweigerd. Vergelijk de bronversies vóór en na de geweigerde acties.

**Als uitgesloten gebruiker**, open een afzonderlijk beperkte synthetische pagina. Verwacht geen toegang tot de inhoud. Test onderliggende pagina’s afzonderlijk. Plak beschermde tekst niet als omweg in de chat van de uitgesloten gebruiker.

## De repositorykaart aanpassen

**Houd bron-ID’s stabiel als de bronlocatie verandert.** REQ-17 blijft staan voor de goedgekeurde bewaareis, maar in het gemengde traject is de bron een Confluence-pagina. Een momentopname in de repository helpt bij controles en beoordelingen. Deze vervangt de gezaghebbende pagina niet.

| Record | Gezaghebbende bron | Behandeling in repository |
|---|---|---|
| **REQ-17** | Gekoppelde Confluence-pagina met de eis | Momentopname met bewijs van paginarevisie |
| **RUN-04** | Gekoppelde Confluence-pagina met het draaiboek | Vastgelegd bedieningsfragment voor consistentie |
| **POL-01** | Beveiligd GitHub-beleid | Gedeelde agentinstructies verwijzen ernaar |
| **Configuratie** | Beveiligd GitHub-record | Voorgesteld implementatieverschil |
| **Uitvoering** | Jira-werkitem | Koppeling voor samenhang, geen beleidskopie |

**Voeg herkomstgegevens toe aan momentopnamen.** Noteer het bron-ID, de paginaverwijzing, pagina-versie, vastlegtijd en rol van de vastlegger in het privévoorstelpakket. Neem interne pagina-ID’s niet op in openbare cursusinzendingen. Als de uitgever een andere actuele versie aantreft, stem die af voordat je de momentopname gebruikt.

**Verander de bron niet om bij de tool te passen.** De bewerkbare Jira-beschrijving is handig voor discussie, maar blijft een uitvoeringsrecord. Een zin over dertig dagen in Jira vervangt geen eis van zeven dagen in Confluence.

## Toegangstests ontwerpen

**Scheid lezen, voorstellen maken en publiceren.** Een bijdrager heeft voldoende toegang nodig om de synthetische eis te begrijpen en een voorstel in te dienen. Bewerkingsrechten op de gezaghebbende pagina of toestemming om het eigen voorstel goed te keuren zijn niet nodig.

```text
Test record: PERM-REQ-EDIT
Role: contributor
Source: REQ-17
Precondition: source is readable, published revision captured
Attempt: edit the authoritative requirement
Expected: edit denied, published revision unchanged
Observed: fill from the sandbox
Evidence: native result and independent revision read-back
Reviewer: administrator or independent permission reviewer
```

**Gebruik een apart record voor geweigerde leestoegang.** De leesbare eis voor de bijdrager test de scheiding van publicatierechten. Een ontoegankelijke pagina voor een uitgesloten gebruiker test vertrouwelijkheid. Door beide in één rij te combineren, zie je niet welke grens is getest.

**Controleer ook toegestane toegang.** Eigenaren en uitgevers moeten hun toegewezen route kunnen gebruiken. Als iedereen wordt geweigerd, is de testomgeving wel beperkt maar onbruikbaar. Bewaar een geslaagde bewerking door een bevoegde gebruiker op een wegwerppagina. Wijzig de goedgekeurde eis niet terwijl je machtigingen onderzoekt.

## Jira-beoordeling oefenen

**Gebruik de statusnamen als ontwerp voor deze pilot.** Concept bevat een aanvraag. Beoordeling bevat een vastgezet pakket. Goedgekeurd betekent dat de eigenaren hun beoordeling hebben afgerond. Publicatie betekent dat de uitvoering nog loopt. Gereed vereist een controle achteraf. Geblokkeerd betekent dat bewijs of toegang ontbreekt, of dat een conflict onopgelost is.

| Overgang | Vereist pakket | Verantwoordelijke controle |
|---|---|---|
| **Concept naar Beoordeling** | Vast voorstel en bronversies | Bijdrager bevestigt volledigheid |
| **Beoordeling naar Goedgekeurd** | Besluiten van product- en operationele eigenaar | Bevoegde uitvoerder controleert beide rollen |
| **Goedgekeurd naar Publicatie** | Vergelijking met actuele bronnen | Uitgever bevestigt dat de basis ongewijzigd is |
| **Publicatie naar Gereed** | Volledig registratiespoor per systeem | Uitvoeringseigenaar controleert de teruglezing |
| **Elke ondersteunde stap naar Geblokkeerd** | Fout en openstaande actie | Hersteleigenaar toegewezen |

**Oefen met een onvolledig synthetisch pakket.** Dien alleen een productbeoordeling in en vraag de bevoegde uitvoerder de overgang te beoordelen. Verwacht dat het werk op Beoordeling blijft staan totdat de operationele beoordeling is aangevraagd. Zo test je de procedurele beoordeling los van de platformweigering voor de bijdrager.

**Test alternatieve routes bewust.** Controleer in de workflowweergave van je testomgeving elke route naar Goedgekeurd en Gereed. Een beperkte benoemde overgang volstaat niet als een andere route dezelfde beoordelingsgrens overslaat. Noteer welke routes en uitvoerder je hebt gecontroleerd. Claim geen volledige dekking na één klik.

## Onverwachte toegang onderzoeken

**Begin bij de effectieve identiteit.** Controleer of de browsersessie bij de bedoelde testrol hoort. Inspecteer daarna groepslidmaatschap, ruimtemachtigingen, paginatoegang en workflowkoppeling met de beheertools van het product. Wijzig niet meerdere instellingen tegelijk, want dan verliest een weigering diagnostische waarde.

1. **Controleer de identiteit:** gebruik afzonderlijke sessies voor bijdrager, uitgever en uitgesloten gebruiker.
2. **Zoek de toekenning:** stel vast welk lidmaatschap of welke instelling de actie toestaat.
3. **Pas de labinstelling aan:** behoud legitieme toegang voor eigenaren.
4. **Herhaal dezelfde poging:** leg na weigering de ongewijzigde bronversie vast.
5. **Herhaal de positieve test:** bevestig dat bevoegde publicatie nog werkt.

**Controlelijst voor bewijs:** noteer de Confluence-paginaboom en gekoppelde pagina-ID’s, het Jira-labschema, de labworkflow, de groepslidmaatschappen van iedere testrol, een toegestane lezing van de eis, een geweigerde bewerking met ongewijzigde versie, een toegestane conceptaanmaak, een geweigerde overgang naar Goedgekeurd met ongewijzigde status, een geweigerde lezing door de uitgesloten gebruiker en de eigenaar van de opschoning. Noteer per rij de actorrol, begin- en eindversie of -status, het native resultaat en de onafhankelijke beoordelaar. Noteer het navigatiepad dat je in de tenant hebt gezien, want labels en beschikbare instellingen verschillen per abonnement.

**Voltooiingscontrole:** lever de gekoppelde gezaghebbende pagina’s, de labworkflow, de bedoelde rollenmatrix en de waargenomen machtigingsrecords op. Ontbreekt een vereiste functie in het abonnement, markeer de betreffende rij dan als Geblokkeerd. De publicatieles veronderstelt dat deze tests zijn geslaagd, niet alleen dat er schermafbeeldingen van instellingen bestaan.

## Problemen oplossen en terugdraaien

**De bijdrager kan nog bewerken:** controleer paginatoegang, ruimtemachtigingen en lidmaatschappen. **De overgang slaagt nog steeds:** controleer de workflowkoppeling en omleidingsroutes. **Instellingen ontbreken:** controleer of het om een bedrijfsbeheerde configuratie gaat, welke editie is ingeschakeld en of je beheerder bent.

**Terugdraaien:** verwijder connectorrechten en archiveer concepten. Koppel labschema’s en -workflows pas los nadat je bewijs hebt bewaard. Herstel de goedgekeurde paginainhoud via de beoordeelde geschiedenis of een corrigerende bewerking. Verwijder geen auditbewijs.

## Oefening en zelfcontrole

**Jira vermeldt dertig dagen terwijl REQ-17 zeven dagen vermeldt.** Bepaal welke implementatie-invoer en welke eigenaar de tegenstrijdigheid moet oplossen.

**Verwachte redenering:** Confluence bepaalt de bedoeling. Jira bevat een voorstel- of uitvoeringsfout. Stop de publicatie en vraag de producteigenaar om afstemming, in plaats van de nieuwste tijdstempel te kiezen.

## Primaire bronnen

- **Beperkingen en abonnement:** [Confluence-machtigingen](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Deelinstellingen:** [Toegang tot specifieke inhoud](https://support.atlassian.com/confluence-cloud/docs/add-or-remove-page-restrictions/).
- **Schema beheren:** [Jira-machtigingenschema’s](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).
- **Overgangsvoorwaarden:** [Geavanceerde workflows](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).

## Volgende stappen

**Ga verder met [Publicatie tussen systemen](/articles/ai-collaboration-confluence-jira-publication/)** nadat de toegangstests zijn geslaagd.
