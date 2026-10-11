---
title: "AI-samenwerking met GitHub: grenzen voor repository en review"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Bouw een GitHub-gerichte bronnenkaart, wijs bestandseigenaars toe en stel een beschermde publicatiegrens in voor gereviewde AI-bijdragen."
genre: ["Kunstmatige intelligentie", "Teamsamenwerking", "Software-engineering"]
tags: ["AI-samenwerkingscursus", "GitHub-repository", "branchbescherming", "CODEOWNERS", "bronnenkaart", "pull-requestreview", "publicatiecontroles"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustratie van professionals die gedeeld projectwerk beoordelen in een cybersecurity-werkomgeving"
coverCaption: ""
---

[Terug naar de cursus over AI-samenwerking](/ai-collaboration-course-start/)

**De maintainer bouwt na goedkeuring van het charter de GitHub-gerichte publicatiegrens.** Vereisten, configuratie, beleid en runbooks staan in één wegwerp-repository. Bijdragers stellen werk voor via Issues en pull requests. Jij bepaalt waar goedgekeurde feiten staan en blokkeert niet-gereviewde wijzigingen voordat je agents koppelt.

## Belangrijkste punten

- **Beschermde `main`** is de publicatiegrens.
- **Issues** verzamelen voorgesteld werk zonder beleid goed te keuren.
- **CODEOWNERS** wijst bevoegde bestandsreviewers toe.
- **Afzonderlijke gebruikers** tonen review- en weigeringscontroles.

## Voordat je begint

**Vereisten:** de [pilotfundering](/articles/ai-collaboration-pilot-foundation/), het uitgepakte lab, een repositorybeheerder en afzonderlijke product- en operationele reviewers. **Geschatte tijd:** 60 minuten. **Moeilijkheid:** gemiddeld.

**Planbegrenzing:** GitHub documenteert beschermde branches voor openbare repositories op Free en private repositories op Pro, Team of Enterprise. Gebruik openbare repositories alleen voor synthetische inhoud. Controleer zichtbaarheid en plan in de referentie voor beschermde branches voordat je op handhaving vertrouwt.

**Resultaat:** je eindigt met een beschermde publicatiebranch, bestandseigenaars, een bronnenkaart en een weigeringstest die als bewijs is vastgelegd.

## De repository maken

1. **Maak `export-service-lab`** met een README en de standaardbranch **`main`**.
2. **Kopieer het uitgepakte lab** naar de repositoryroot en behoud **`check.py`**, **`test_check.py`** en **`baseline/`**. Kopieer de baseline-recordbestanden naar de root als eerste records.
3. **Maak `docs/project-map.md`** met het funderingsregister. Voeg **`docs/policy.md`** toe met goedgekeurde POL-01.
4. **Maak `docs/decisions/DEC-12.md`** met chartergoedkeuring, rollen, het baselinebesluit en de status.
5. **Commit de bootstrap** als beheerder. Leg deze eerste uitzondering vast. Schakel bescherming in vóór volgende bijdragen.

**Lokale bootstraproute voor Git Bash, macOS Terminal of een Linux-shell:** meld je in de browser aan bij GitHub, open de nieuwe repository, kies **Code** en kopieer de HTTPS-clone-URL. Voer de onderstaande opdrachten uit in een wegwerpwerkdirectory. Vervang de twee tijdelijke paden door de URL en het pad naar het gedownloade lab-ZIP-bestand. Plak geen token in de URL.

```bash
git --version
git clone "https://github.com/OWNER/export-service-lab.git"
cd export-service-lab
unzip -n "/absolute/path/to/ai-collaboration-lab.zip"
cp baseline/config.json baseline/policy.json baseline/proposal.json baseline/requirement.json baseline/runbook.md .
mkdir -p docs/decisions
git status --short
```

De clone-opdracht moet de repositorydirectory benoemen. Als `unzip` niet beschikbaar is, pak je het ZIP-bestand uit met je bestandsbeheerder en kopieer je de inhoud naar deze checkout. Laat de README van de repository intact. Sla `docs/project-map.md`, `docs/policy.md` en `docs/decisions/DEC-12.md` uit het funderingspakket op met een teksteditor. Voer daarna uit:

```bash
git add README.md baseline check.py test_check.py config.json policy.json proposal.json requirement.json runbook.md docs
git commit -m "Add synthetic collaboration baseline"
git push origin main
git status --short
git remote -v
```

Git hoort een nieuwe commit-ID en daarna een geslaagde push naar `main` te tonen. De laatste korte status hoort leeg te zijn. Open de GitHub-repository in een nieuw browservenster en bevestig dat de bestanden en commit-ID op `main` verschijnen. Bewaar de commit-URL als bootstrapbewijs. Als Git om de auteursidentiteit vraagt, volg je de setup bridge op de cursus hub. Als authenticatie mislukt, gebruik je GitHubs ondersteunde credentialflow en probeer je dezelfde push opnieuw. Als de branch of remote fout is, stop je en controleer je `git branch --show-current` en `git remote -v` vóór een nieuwe schrijfactie. Als de push wordt geweigerd omdat bescherming al is ingeschakeld, open je een voorstelbranch en PR in plaats van de regel te omzeilen. De browserroute hieronder blijft beschikbaar voor een maintainer.

| Record | Locatie | Eigenaar |
|---|---|---|
| **POL-01** | `policy.json`, `docs/policy.md` | Beleidseigenaar |
| **REQ-17** | `requirement.json` | Producteigenaar |
| **RUN-04** | `runbook.md` | Operationele eigenaar |
| **Gedrag** | `config.json` | Maintainer |
| **Besluiten** | `docs/decisions/` | Projectleider |

**De kaart koppelt locaties in plaats van waarden te kopiëren.** Houd de README gericht op installatie en de kaart. Herhaalde bewaartermijnen veroorzaken drift, zelfs binnen één repository.

## Bestandseigenaars toewijzen

**Genereer `.github/CODEOWNERS`** lokaal met echte sandbox-handles. Voer handles in zonder de eerste **`@`**. Bewaar accountidentiteiten in je privé-lab, niet in openbaar oefenbewijs.

```bash
python3 - <<'PY'
from pathlib import Path
roles = ['product', 'operations', 'maintainer', 'policy']
handles = {r: input(r + ' GitHub handle: ').strip().lstrip('@') for r in roles}
if any(not h or not all(c.isalnum() or c == '-' for c in h) for h in handles.values()):
    raise SystemExit('Invalid handle')
paths = {'requirement.json': 'product', 'runbook.md': 'operations',
         'config.json': 'maintainer', 'policy.json': 'policy',
         'docs/policy.md': 'policy', 'AGENTS.md': 'policy',
         'CLAUDE.md': 'policy', '.clinerules/': 'policy',
         '.github/': 'maintainer', 'check.py': 'maintainer',
         'test_check.py': 'maintainer', 'baseline/': 'maintainer'}
Path('.github').mkdir(exist_ok=True)
Path('.github/CODEOWNERS').write_text(''.join(
    '/' + path + ' @' + handles[role] + '\n' for path, role in paths.items()))
PY
```

Eigenaren hebben schrijftoegang nodig zodat GitHub hen herkent. Controleer het CODEOWNERS-bestand in de browser op fouten. Bescherm eigendomsbestanden en workflowdefinities samen met gewone inhoud.

**Meerdere namen op één regel vereisen niet de goedkeuring van alle vermelde eigenaren.** GitHub accepteert één goedkeuring van een bevoegde eigenaar voor het overeenkomende pad. Gebruik afzonderlijke aangewezen eigenaren voor vereiste- en runbookpaden. De pilot vereist ook attestaties van de producteigenaar en operationele eigenaar die aan het uiteindelijke voorstel zijn gekoppeld.

## Publicatie beschermen

1. **Open Settings, Branches** en voeg een branch protection rule toe voor **`main`**. Gebruik in deze oefening consequent de branch-protectionroute in plaats van die met rulesets te mengen.
2. **Vereis een pull request**, twee goedkeurende reviews en review door code owners.
3. **Wijs verouderde goedkeuringen af** na nieuwe commits en vereis het oplossen van gesprekken.
4. **Schakel Do not allow bypassing the above settings in.** Houd force pushes en verwijdering uitgeschakeld.
5. **Voeg de consistentiecheck toe** na de eerste uitvoering ervan in de volgende module. Vereis dat branches bijgewerkt zijn voordat ze worden gemerged.

**Twee goedkeuringen leggen een aantal vast, geen lidmaatschap van een bedrijfsrol.** CODEOWNERS voegt padgebaseerde eigenaarsdekking toe. De maintainer controleert ook de twee rolattestaties. Leg deze procedurele controle expliciet vast in plaats van haar te beschrijven als geautomatiseerde handhaving van twee rollen.

**Beheerders beheren nog steeds de configuratie.** Leg de regel vast vóór en na de tests. Geef een agent geen beheerdersrechten en gebruik geen privileged token om weigering van een bijdrager te demonstreren.

## De grens verifiëren

| Poging | Verwacht resultaat |
|---|---|
| **Bijdrager dient een branch in** | Voorstel toegestaan |
| **Bijdrager publiceert rechtstreeks** | Beschermde publicatie geweigerd |
| **Eén reviewer keurt goed** | Merge geblokkeerd door de reviewdrempel |
| **Nieuwe commit volgt op review** | Nieuwe goedkeuring vereist |
| **Gevoelig bestand heeft geen eigenaarsdekking** | Herstellen vóór publicatie |

**Gebruik de browsersessie van de bijdrager om de route te onderzoeken.** GitHubs webeditor bewerkt geen beschermde **`main`**-branch. Een prompt om een branch te maken toont de ondersteunde browserroute. Dit bewijst niet dat de server een directe push heeft geweigerd. Laat voor platform-weigeringsbewijs een bijdrager met goedgekeurde lokale Git-toegang een onschadelijke directe push naar beschermde **`main`** proberen en bewaar het serverantwoord. Markeer de weigeringstest als Blocked wanneer lokale toegang ontbreekt.

**Lees `main` na de weigering** en bevestig dat de revisie niet is gewijzigd. Noteer de rol van de actor, de ondernomen actie, het resultaat en de bronrevisie. Een belofte van een assistent om niet te publiceren is gedragsbewijs, geen platform-permissietest.

**Gebruik de eigen geauthenticeerde lokale clone van de bijdrager voor de directe-pushtest.** Een maintainer-token zou de verkeerde identiteit testen. Deze illustratieve respons toont het type serverbewijs dat je moet bewaren. De exacte formulering verschilt per repositoryregel.

```text
Actor role: contributor
Attempt: harmless synthetic direct push to main
Remote result: rejected, protected branch update denied
Initial main commit: [record sandbox commit]
Final main commit: [record same commit after read-back]
Decision: platform denial supported only if both records are observed
```

**Als lokale Git-authenticatie niet beschikbaar is, markeer je server-side weigering als Blocked.** Bewaar de browserprompt voor de branch als routebewijs en vraag de maintainer een afzonderlijke bijdragerstest te organiseren. Beoordeel de routeprompt niet als een geweigerde directe push.

## Een bruikbare bronnenkaart bouwen

**Een bronnenkaart is een routeringsdocument**, geen tweede vereistendocument. Iemand die vanuit de chat komt, moet actuele intentie, geïmplementeerd gedrag en operationele instructies vinden zonder uit concurrerende samenvattingen te kiezen.

```text
Project: export-service-lab
Track: GitHub-first
Approved boundary: protected main

REQ-17 -> requirement.json
  Authority: retention intent for synthetic export files
  Owner: product-owner
  Revision: record revision plus protected commit

RUN-04 -> runbook.md
  Authority: operating instructions for the synthetic lab
  Owner: operations-owner
  Revision: protected commit

Behavior -> config.json
  Authority: committed retention configuration
  Owner: repository-maintainer
  Revision: protected commit

Proposals -> Issues and proposal branches
  Authority: requested changes only
```

**Zet de actuele bewaartermijn niet in elke kaartvermelding.** Een kaart met “zeven dagen” wordt na PROP-042 nog een waarde die je moet synchroniseren. Houd stabiele identificatoren en locaties in de kaart en lees de waarde uit het gezaghebbende record.

**Bescherm kaartwijzigingen als routeringswijzigingen.** REQ-17 omleiden naar een conceptbestand verandert de bronselectie, zelfs als de goedgekeurde vereiste onaangetast blijft. Review bestemming, eigenaar en gezagsbereik wanneer de kaart verandert.

## Baseline en kandidaat scheiden

**De repositoryroot bevat de actieve labrecords.** De gedownloade **`baseline/`**-directory is een onderwijsfixture. Die is niet automatisch de beschermde baseline voor elke latere PR. Zodra gereviewd werk **`main`** bereikt, bepalen de beschermde rootrecords de basis voor het volgende voorstel.

| Locatie | Doel | Bewerken tijdens PROP-042? |
|---|---|---|
| **Root requirement/config/runbook** | Voorgestelde actieve records op de branch | Ja, via gereviewde wijzigingen |
| **`baseline/`** | Oorspronkelijke offline-oefenfixture | Nee |
| **Losgekoppelde vertrouwde worktree** | Vastgelegde beschermde rootrecords | Nee |
| **`context.json`** | Bewijs van vastgelegde basisbytes | Opnieuw genereren na afstemming |

**Houd controlewijzigingen gescheiden van bewaartermijnwijzigingen.** Bootstrap eerst checker en reviewregels. Stel daarna de wijziging van zeven naar dertig dagen voor. Het combineren van een beleids-, workflow- en waardeherschrijving maakt het moeilijker om herstelde controles van omzeilde controles te onderscheiden.

## De volledige wijziging reviewen

**Open Files changed voordat je een PR-beschrijving accepteert.** De beschrijving legt de bedoeling van de auteur uit. De diff toont de ingediende wijziging. Bekijk voor PROP-042 de vereistrevisie, scope-uitsluitingen, configuratie, runbook, voorstelbasis en manifestbewijs.

1. **Productreview:** bevestig de intentie voor dertig dagen en onveranderde uitsluitingen.
2. **Operationele review:** bevestig dat het runbook overeenkomt met de voorgestelde configuratie en de runtimebeperking behoudt.
3. **Maintainerreview:** controleer JSON, bronvastlegging, checkresultaten en ongerelateerde wijzigingen.
4. **Controlereview:** bekijk elke wijziging aan kaart, beleid, CODEOWNERS of workflow afzonderlijk.

**Een groene check verklaart geen ongerelateerde verwijdering.** Als de branch het beleidsdocument verwijdert terwijl de bewaartermijn wijzigt, vraag je een afzonderlijk voorstel of een review door een specifieke eigenaar. Een beperkte scope houdt het reviewobject begrijpelijk.

## Een weigeringstest diagnosticeren

**Gebruik één ondernomen actie per bewijsregel.** “Contributor failed” is dubbelzinnig. De gebruiker heeft mogelijk geen gewone schrijfrechten, loopt tegen een browserbeperking aan of raakt de bedoelde branchregel. Die observaties stellen verschillende grenzen vast.

| Observatie | Interpretatie | Opvolging |
|---|---|---|
| **Kan geen branch maken** | Toegang voor bijdragen ontbreekt | Gebruik een goedgekeurde Issue- of forkroute |
| **Maakt branch, kan niet naar main publiceren** | Geteste publicatieroute is beperkt | Leg ongewijzigde main-revisie vast |
| **Merge geblokkeerd met één review** | Reviewaantal geldt voor geteste PR | Voeg rolgebonden bewijs toe |
| **Admin publiceert ondanks regel** | Geteste identiteit omzeilt de grens | Controleer bypassinstellingen en grants |

**Registreer rol en actie zonder accountdetails bloot te geven** in gedeeld cursusbewijs. Houd native actorrecords privé beschikbaar voor de reviewer. Leg regelconfiguratie, ondernomen bewerking, weigering en de resulterende beschermde revisie samen vast.

## Repository-voltooiingscontrole

**Lever een repository die een andere bijdrager zelfstandig kan volgen.** De README verwijst naar de kaart, de kaart verwijst naar gezaghebbende records, eigenaarsdekking omvat gevoelige paden en bescherming geldt voor **`main`**. Bewaar één toegelaten voorstel en één geweigerde publicatiepoging.

**Claim geen handhaving op basis van instellingen alleen.** Instellingen leggen de bedoelde configuratie vast. De sandboxpoging legt waargenomen gedrag vast voor een bepaalde rol en route. Neem beide mee naar de les over agents en Actions.

## Problemen oplossen en terugdraaien

**Eigenaarsverzoek ontbreekt:** bevestig schrijfrechten en dekking van het basisbranchpad. **Bescherming ontbreekt:** controleer plan en zichtbaarheid. **Merge blijft ingeschakeld:** controleer regeldoel, bypassconfiguratie en reviewaantal.

**Terugdraaien:** sluit niet-gemergde voorstellen en schakel labautomatisering uit. Draai gemergde labinhoud terug via een andere gereviewde PR. Bewaar bewijs voordat je de wegwerp-repository verwijdert. Verzwak de bescherming niet om een mislukte test af te ronden.

## Oefening en zelfcontrole

**Stel als bijdrager een wijziging aan `docs/policy.md` voor.** Bepaal of goedkeuring door de maintainer alleen goedkeuring door de beleidseigenaar vaststelt.

**Verwachte redenering:** het reviewaantal stelt op zichzelf geen bevoegdheid vast. Het pad heeft dekking door de beleidseigenaar en een actuele rolreview nodig. Noteer niet-afgedwongen rolgebonden vereisten als procedurele controles.

## Belangrijkste referenties

- **Plan- en reviewcontroles:** [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Geschiktheid van eigenaren:** [Code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
- **Bijdragen in de browser:** [Editing files](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).

## Volgende stappen

**Ga verder met [Agentadapters en Actions](/articles/ai-collaboration-github-agents-actions/)** om bronbewijs te koppelen aan uitvoerbare controles.
