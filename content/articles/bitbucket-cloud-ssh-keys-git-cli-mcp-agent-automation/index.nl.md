---
title: "Bitbucket Cloud SSH-sleutels: alleen-lezen Git-toegang voor AI-agents"
date: 2026-10-11
lastmod: 2026-11-09
toc: true
draft: false
description: "Stel Bitbucket Cloud SSH-sleutels, Git CLI-toegang, REST API-tokens, 1Password en MCP-tools in voor alleen-lezen workflows met AI-agents."
genre: ["Cloudbeveiliging", "Ontwikkelaarstools", "Systeembeheer"]
tags: ["Bitbucket Cloud", "Bitbucket SSH-sleutels", "repositorytoegangssleutels", "projecttoegangssleutels", "werkruimtetoegangssleutels", "Git CLI", "Bitbucket CLI", "1Password CLI", "1Password SSH Agent", "MCP", "Model Context Protocol", "REST API", "API-tokentoestemmingen", "agentmachtigingen", "alleen-lezen automatisering", "SSH-hostsleutels"]
cover: "/img/cover/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation.webp"
coverAlt: "Een terminalworkflow die Bitbucket Cloud Git-toegang, beperkte SSH-sleutels, 1Password, REST API-lezingen en MCP-tools verbindt"
coverCaption: ""
---

**Een begrensde agentworkflow scheidt repository-lezingen, API-lezingen, geheimbeheer en externe schrijfacties.** Gebruik Git via Secure Shell (SSH) voor toegang tot broncode, een alleen-lezen Bitbucket-toegangssleutel voor geautomatiseerde checkout, de REST API voor metadata en een Model Context Protocol (MCP)-server voor goedgekeurde tools. Bewaar privésleutels en API-tokens in 1Password. Laat schrijfacties pas na menselijke goedkeuring toe.

<!--more-->

## Belangrijkste punten

- **Alleen-lezen als standaard:** Gebruik een repository- of projecttoegangssleutel voor checkout door agents. Geen van beide geeft push-toegang.
- **Persoonlijke identiteit:** Gebruik een persoonlijke SSH-sleutel voor interactief werk dat aan een gebruikersaccount is gekoppeld.
- **Beheer van geheimen:** Gebruik de 1Password SSH Agent zodat Git een ondertekeningsbewerking kan uitvoeren zonder de privésleutel te lezen.
- **Betekenis van CLI:** Gebruik `git`, `curl` en een kleine gecontroleerde API-wrapper als praktische Bitbucket-opdrachtregeltools.
- **MCP-grens:** Stel beperkte leestools beschikbaar. Schakel schrijftools uit of plaats ze achter een afzonderlijk goedkeuringsproces.
- **Schrijfgate:** Laat een agent een wijziging inspecteren, vergelijken en voorbereiden. Vereis menselijke goedkeuring voor een push, pull request, merge of instellingenwijziging.

## Voordat je begint

**Vereisten:** toegang tot Bitbucket Cloud, Git, een OpenSSH-client, 1Password 8, 1Password CLI, een aangemelde CLI of goedgekeurd serviceaccount, en een MCP-host met goedkeuringsbeheer voor servers. Reken op 45 minuten. Moeilijkheidsgraad: gemiddeld.

Gebruik voor de eerste proef een testrepository. Vervang elke tijdelijke aanduiding in de voorbeelden. De opdrachten hieronder zijn niet-geteste voorbeelden. Ze verwijzen niet naar een actief Bitbucket-account of een echte repository.

**Versiestatus:** dit artikel is ontwerpadvies, geen draaiboek dat aan specifieke versies is gebonden. Controleer de geïnstalleerde versies van Git, OpenSSH, 1Password CLI, Teamwork Graph CLI, MCP-host en MCP-server voordat je test. Configureer de 1Password SSH Agent voor het huidige besturingssysteem voordat je `ssh-add -l` gebruikt.

**Houd inloggegevens buiten shells, logs, URL’s, Git-remotes en bronbestanden.** Gebruik tijdelijke aanduidingen zoals `<workspace>`, `<repository>`, `<api-token>` en `<socket-path>`. Plak geen echte privésleutel in een terminaltranscript.

## Kies de toegangsgrens

Bitbucket Cloud ondersteunt toegangssleutels op repository-, project- en werkruimteniveau. De scope bepaalt de impact van een gekopieerde sleutel. De [officiële vergelijking van toegangssleutels](https://support.atlassian.com/bitbucket-cloud/kb/difference-between-repository-project-and-workspace-access-keys/) beschrijft het verschil in machtigingen.

| Toegangstype | Scope | Schrijfrechten | Geschikt voor |
|---|---|---:|---|
| **Repository-toegangssleutel** | Eén repository | Nee | Standaard checkout door een agent |
| **Projecttoegangssleutel** | Repositories in één project | Nee | Alleen-lezen-taken voor een kleine groep repositories |
| **Werkruimtetoegangssleutel** | Repositories in één werkruimte | Ja | Gecontroleerde serviceautomatisering met een afzonderlijk schrijfplan |
| **Persoonlijke SSH-sleutel** | Repositories die voor één gebruiker toegankelijk zijn | Volgt het gebruikersaccount | Interactief beheer |
| **API-token** | Gebruikersgebonden API-scopes en accountbereik | Afhankelijk van scopes | REST API-lezingen of een tijdelijke schrijftaak |

**Begin met de kleinste bruikbare grens.** Kies een repositorytoegangssleutel als één repository volstaat. Kies een projectsleutel als meerdere repositories binnen één project vallen en alleen-lezen-toegang past. Behandel een werkruimtetoegangssleutel als een identiteit met schrijfrechten, niet als een handige standaard.

Maak de kleinst mogelijke sleutel aan en registreer deze via de bijbehorende Bitbucket-instellingen:

1. Open Repository settings, Access keys en Add key voor één repository. Plak de publieke sleutel en houd de sleutel alleen-lezen.
2. Open Project settings, Access keys en Add key wanneer meerdere repositories een alleen-lezen-identiteit op projectniveau nodig hebben.
3. Gebruik een werkruimtetoegangssleutel alleen in een gedeelde werkruimte met een goedgekeurd schrijfontwerp. Persoonlijke werkruimten bieden niet dezelfde optie op werkruimteniveau.
4. Noteer het sleutel-label, de scope, de fingerprint van de publieke sleutel, de eigenaar en de rotatiedatum. Bewaar de privésleutel in 1Password.

Voer na registratie één exacte test voor alleen-lezen-verbinding uit:

```bash
git ls-remote git@bitbucket.org:<workspace>/<repository>.git HEAD
```

**Verwachte uitvoer:** één commitverwijzing voor `HEAD`. Niet-getest voorbeeld. Een geslaagd resultaat bewijst dat één toegestane SSH-identiteit de genoemde repository heeft bereikt. Het bewijst niet dat de geregistreerde sleutel is geselecteerd of dat schrijfrechten bestaan. Voer de test opnieuw uit nadat je de configuratie met één sleutel per repository hebt ingesteld.

Zie [1Password CLI en SSH Agent: beveilig SSH-sleutels voor AI-agents](/articles/1password-cli-ssh-keys-mcp-agent-administration/) voor het beheer van privésleutels en toestemming via de 1Password SSH Agent.

## Wat “Bitbucket CLI” precies betekent

De term **Bitbucket CLI** verwijst vaak naar drie verschillende interfaces. Houd ze uit elkaar.

- **Git CLI:** `git clone` en `git fetch` verplaatsen repositorygegevens via SSH of HTTPS. `git diff` vergelijkt lokale bestanden of revisies.
- **REST-client:** `curl` of een gecontroleerde wrapper roept de Bitbucket Cloud Representational State Transfer (REST) API aan. Een API is een programmeerbare interface voor gegevensverzoeken of acties. De [Bitbucket Cloud REST API-referentie](https://developer.atlassian.com/cloud/bitbucket/rest/) vermeldt repository-, broncode-, branch-, pull-request-, pipeline- en statusresources.
- **Atlassian CLI:** `acli` is de officiële opdrachtregelinterface van Atlassian. De [introductie](https://developer.atlassian.com/cloud/acli/guides/introduction/) beschrijft het product, terwijl de [opdrachtreferentie](https://developer.atlassian.com/cloud/acli/reference/commands/) de onderdelen `admin`, `jira`, `feedback` en `rovodev` noemt. De referentie documenteert geen Bitbucket Cloud-opdrachten.

**De officiële opdrachtreferentie van Atlassian voor `acli` documenteert geen Bitbucket Cloud-opdrachten.** Verzin geen opdracht zoals `acli bitbucket clone`. Gebruik Git voor Git-bewerkingen en de REST API voor Bitbucket Cloud-gegevens.

### Optionele Teamwork Graph CLI

**Atlassian publiceert ook de Teamwork Graph CLI, of `twg`.** Het [overzicht](https://developer.atlassian.com/cloud/twg-cli/) en de [opdrachtcatalogus](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/commands/commands-catalog/) documenteren Bitbucket-opdrachtfamilies. De installatieopdracht is:

```bash
twg setup
```

De installatieopdracht wijzigt de lokale authenticatiestatus. Volg de prompts van de geïnstalleerde versie voor optionele Bitbucket-tokenconfiguratie. De Bitbucket-tokenroute van de CLI staat los van Atlassian OAuth. Koppel exacte opdrachtsyntaxis aan de geïnstalleerde versie en de actuele opdrachtcatalogus. Gebruik een apart profiel, een beperkt token, gecontroleerde geïnstalleerde skills en menselijke goedkeuring voor wijzigingsopdrachten.

**Verwacht resultaat, niet getest:** het geïsoleerde profiel ontvangt Bitbucket-authenticatie-instellingen. Noteer de vorige profielstatus voordat je `setup` uitvoert. Verwijder de opgeslagen referentie bij rollback via de gedocumenteerde uitlog- of configuratieverwijderingsprocedure van de geïnstalleerde versie.

Als een project van derden zichzelf een Bitbucket CLI noemt, controleer dan de broncode, releaseprocedure, checksums, updatepad, authenticatiestroom, gevraagde scopes, netwerkbestemmingen, logverwerking en schrijfopdrachten. Een bekende binaire naam bewijst geen ondersteuning door de leverancier of veilige machtigingen.

## Houd SSH-sleutels onder beheer van 1Password

De [1Password SSH Agent](https://www.1password.dev/ssh/agent) biedt SSH-sleutels die in 1Password zijn opgeslagen aan Git- en SSH-clients. De client voert een goedgekeurde ondertekeningsaanvraag uit. De privésleutel blijft in de 1Password-app en 1Password vraagt toestemming voordat een goedgekeurde client een sleutel gebruikt.

De [1Password CLI-referentie](https://www.1password.dev/cli/reference) heeft een andere rol. Gebruik `op` voor gecontroleerde toegang tot items, API-tokens, serviceaccounts en automatiseringsinstellingen. Gebruik de SSH Agent voor SSH-ondertekening. Exporteer geen privésleutel naar een tijdelijk bestand alleen om een agentworkflow eenvoudiger te maken.

Controleer de lokale CLI- en agentstatus met alleen-lezen-opdrachten:

```bash
op --version
ssh-add -l
```

**Verwachte uitvoer:** een 1Password CLI-versie en een of meer fingerprints van publieke sleutels uit de actieve agent. Niet-getest voorbeeld. Een lege uitvoer van `ssh-add -l` betekent dat via de geselecteerde agentsocket geen sleutel beschikbaar is.

Maak voor een nieuwe sleutel een Ed25519 SSH Key-item aan in 1Password of importeer een sleutel die met een vertrouwd lokaal proces is gegenereerd. Gebruik een label met doel, scope en rotatiedatum. Voeg alleen de publieke sleutel toe aan Bitbucket Cloud. De [Linux-gids voor repository-toegangssleutels](https://support.atlassian.com/bitbucket-cloud/docs/set-up-repository-access-keys-on-linux/) beschrijft de repository-instellingen en de beperking tot alleen-lezen.

## Controleer eerst de Bitbucket-hostsleutel

SSH-gebruikersauthenticatie bewijst de serveridentiteit niet. De client moet de Bitbucket Cloud-hostsleutel controleren voordat een authenticatieverzoek wordt verzonden. De [Atlassian-gids voor SSH en tweestapsverificatie](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification/) vermeldt de openbare hostsleutels en toont het officiële endpoint om known-hosts-vermeldingen op te halen.

Haal de openbare host-sleutelgegevens op ter vergelijking:

```bash
curl --fail --silent --show-error https://bitbucket.org/site/ssh
```

**Verwachte uitvoer:** OpenSSH `known_hosts`-regels voor `bitbucket.org`. Niet-getest voorbeeld. Vergelijk de geretourneerde sleutel of fingerprint met een onafhankelijke, vertrouwde kopie voordat je de regel toevoegt aan `~/.ssh/known_hosts`.

Schakel strikte hostcontrole in nadat de goedgekeurde vermelding bestaat:

```sshconfig
Host bitbucket.org
    StrictHostKeyChecking yes
    UserKnownHostsFile ~/.ssh/known_hosts
```

**Accepteer geen gewijzigde hostsleutel tijdens een agentrun.** Stop de run, controleer de actuele Bitbucket Cloud-hostsleutelregistratie en bekijk de lokale `known_hosts`-vermelding. Automatische acceptatie verwijdert een beveiligingsgrens rond de sleutel.

## Selecteer één sleutel per repository

Op één apparaat staan vaak meerdere Bitbucket-sleutels. Een brede SSH-agent biedt tijdens één verbinding meerdere identiteiten aan. Een server of beleid met een laag maximumaantal authenticatiepogingen kan de juiste sleutel afwijzen nadat eerdere sleutels zijn mislukt.

De [Atlassian-gids voor meerdere repository-toegangssleutels](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) gebruikt `core.sshCommand` in een Git-configuratiebestand van de repository en `includeIf` in de globale Git-configuratie. Gebruik hetzelfde patroon met één sleutel per repository.

Draagbaar voorbeeld met bestanden:

```ini
# .gitconfig inside one local repository
[core]
    sshCommand = ssh -o IdentitiesOnly=yes -i ~/.ssh/<repository-automation-key>
```

```ini
# ~/.gitconfig
[includeIf "gitdir:~/src/<repository>/"]
    path = ~/src/<repository>/.gitconfig
```

Het bovenstaande blok is een uitzondering voor een privésleutel in een bestand, bedoeld voor een specifieke automatiseringsidentiteit. Het configureert de 1Password SSH Agent niet. Configureer voor de 1Password SSH Agent de platformspecifieke waarde van `IdentityAgent` of `SSH_AUTH_SOCK` uit de [1Password-installatiegids](https://www.1password.dev/ssh/get-started). Sommige OpenSSH-configuraties gebruiken een `.pub`-bestand als identiteitsselector voor een agent. Controleer platformondersteuning voordat je dit gebruikt. Een configuratie met een bestand vereist het bijbehorende pad naar de privésleutel. Geef nooit een `.pub`-bestand door aan een opdracht die privésleutelmateriaal verwacht en exporteer geen persoonlijke privésleutel.

Gebruik expliciete repositoryconfiguratie wanneer een lokale kloon één sleutel nodig heeft. Gebruik `includeIf` wanneer een map meerdere klonen met dezelfde toegangsgrens bevat. De [gids voor meerdere sleutels](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) toont beide instellingen in de Bitbucket-workflow.

Kloon met Git via SSH:

```bash
git clone git@bitbucket.org:<workspace>/<repository>.git <local-directory>
```

**Verwachte uitvoer:** Git maakt `<local-directory>` aan en haalt de repository op via `bitbucket.org`. Niet-getest voorbeeld. Met een repositorytoegangssleutel kun je alleen klonen en ophalen.

## Gebruik API-tokens voor beperkte REST-lezingen

Gebruik SSH voor Git-transport. Gebruik de REST API voor metadata of bewerkingen buiten Git-transport. De [gids met API-tokenmachtigingen](https://support.atlassian.com/bitbucket-cloud/docs/api-token-permissions/) vermeldt repositoryscopes zoals Read, Write, Admin en Delete. Repository Read komt overeen met `read:repository:bitbucket` en omvat geen toegang tot pull requests.

Gebruik bij voorkeur een Bitbucket-repository- of projecttoegangstoken voor leesautomatisering wanneer het doelendpoint dit ondersteunt. Een gebruikersgebonden API-token behoudt het bredere bereik van het gebruikersaccount. Gebruik een werkruimtetoegangstoken alleen wanneer de taakregistratie die bredere grens noemt. Bekijk de [Bitbucket-gids voor toegangstokens](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/) voordat je een tokentype kiest.

Begin voor leesacties door agents met `read:repository:bitbucket`. Voeg `read:pullrequest:bitbucket` alleen toe als de agent pull-requestgegevens nodig heeft. Voeg werkruimte- of pipelinescopes alleen toe wanneer de taakregistratie endpoint en resultaat noemt. Schrijf- en beheerdersscopes vereisen een afzonderlijk goedkeuringsproces.

Maak elk API-token aan voor één doel, stel een vervaldatum in, noteer die in het rotatieregister en vervang het token vóór de vervaldatum. De [gids van Atlassian voor het maken van API-tokens](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/) vereist een naam, vervaldatum, appselectie en scopes. Het token wordt na aanmaak één keer getoond.

Bewaar de waarde in 1Password of een beheerd runtimegeheim. Zet de waarde niet in een remote-URL. Geef een bearer-token alleen via een omgevingsvariabele door aan het proces dat één leesactie uitvoert:

```bash
op run --env-file=/path/to/agent.env -- \
sh -c 'curl --fail --silent --show-error \
  --request GET \
  --url "https://api.bitbucket.org/2.0/repositories/<workspace>/<repository>" \
  --header "Authorization: Bearer ${BITBUCKET_API_TOKEN}" \
  --header "Accept: application/json"'
```

Houd `/path/to/agent.env` buiten de repository. Bewaar een verwijzing zoals `BITBUCKET_API_TOKEN=op://synthetic-vault/synthetic-api-token/credential` in het bestand. `op run` lost de verwijzing op en stelt de waarde gedurende het subprocess beschikbaar aan het curl-subproces. Het voorkomt niet dat het onderliggende proces de omgevingswaarde leest of logt. Vervang de tijdelijke aanduiding niet door een letterlijk token.

**Verwachte uitvoer:** JSON-metadata voor de geselecteerde repository. Niet-getest voorbeeld. De tijdelijke aanduiding mag nooit een echt token worden in een gecommit bestand of log.

Laat voor langere automatisering 1Password een geheim via de ondersteunde CLI- of serviceaccountstroom in de procesomgeving injecteren. Houd de levensduur van het token kort genoeg voor de taak. Trek een token in wanneer de taak voortijdig eindigt of de eigenaar van de host verandert.

## Geef MCP een beperkt leesoppervlak

Gebruik de actuele [MCP-specificatie](https://modelcontextprotocol.io/specification/2026-07-28) en de [autorisatieregels](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) bij het beoordelen van een nieuwe server. HTTP-servers hebben token-audiencecontroles nodig en moeten 401- en 403-reacties duidelijk afhandelen.

De MCP-host vraagt toestemming van de gebruiker. De client onderhoudt een verbinding met één server. De server biedt tools, resources of prompts aan. Behandel elke server als niet-vertrouwde code totdat de bron, het transport, het account en de machtigingen zijn beoordeeld.

De specificatie-URL 2025-06-18 in de volgende alinea verwijst naar een historische versie. Gebruik voor nieuwe beoordelingen de actuele specificatie 2026-07-28.

De [MCP-specificatie](https://modelcontextprotocol.io/specification/2025-06-18) definieert de communicatie tussen een MCP-host, client en server. Een server biedt tools, resources of prompts via het protocol aan. MCP standaardiseert de verbindingsindeling. De host, serverimplementatie, het account, de tokenscope en het goedkeuringsbeleid bepalen nog steeds waartoe een aanroep toegang krijgt.

Gebruik een MCP-server als beperkte adapter voor Git en de Bitbucket Cloud REST API.

Bescherm deze adapter tegen token-doorgifte, server-side request forgery (SSRF) en verwarring over privileges (confused deputy). Met SSRF kan een server verzoeken naar onbedoelde bestemmingen sturen. Dit privilegeprobleem ontstaat wanneer een server namens een aanroeper ruimere rechten gebruikt. Bescherm de adapter ook tegen kwaadaardige lokale servers, onveilige OAuth-omleidingen en te grote brondataresultaten. Beperk toegestane Bitbucket-origins en repository-ID’s. Voer lokale servers uit in een sandbox met een eigen besturingssysteemgebruiker. Redigeer geheimen uit toolresultaten en logs.

Deze sectie beschrijft een ontwerp, geen geteste MCP-configuratie. Er zijn hier geen client, server, transport, versie of fixture vastgelegd. Valideer één alleen-lezen-server in een afzonderlijk testprofiel voordat je een agent met een productierepository verbindt.

Voorbeelden van leestools:

| Tool | Begrensd resultaat |
|---|---|
| **`get_repository_metadata`** | Retourneert metadata van één repository |
| **`read_source_file`** | Leest één pad op één revisie |
| **`list_branches`** | Geeft branches van één repository weer |
| **`get_pull_request`** | Retourneert één pull request nadat het token pull-request-leesscope heeft |
| **`get_build_status`** | Retourneert statusgegevens voor één commit |

Deze namen beschrijven een ontwerp. Het zijn geen Atlassian-opdrachten. Voorkom dat de server willekeurige URL’s, willekeurige shell-opdrachten, ruwe tokens, verzoeken om privésleutelexport of onbeperkte repository-ID’s accepteert.

Stel machtigingen op vier lagen in:

1. **Bitbucket Cloud:** repository- of projectleessleutel voor Git, plus de kleinste API-tokenscopes voor REST-lezingen.
2. **1Password:** één kluis of serviceaccount voor de taak, zonder mogelijkheid om privésleutels te exporteren.
3. **MCP-server:** een allowlist van leestools, vaste Bitbucket Cloud-endpoints, invoervalidatie, time-outs en geredigeerde logs.
4. **MCP-host:** gebruikersgoedkeuring voor de server en elke schrijfactie, met schrijftools uitgeschakeld in het standaardprofiel.

*Een MCP-toollijst bewijst dat tools zijn gevonden. De lijst bewijst geen autorisatie, juiste scope, veilige invoerverwerking of correcte resultaten.*

## Faseer de agentworkflow

Houd de workflow expliciet. Elke fase levert bewijs voor de volgende fase.

| Fase | Actie van de agent | Machtiging | Menselijke controle |
|---|---|---|---|
| **Voorbereiden** | Configuratie, host-sleutelrecord, sleutel-label, tokenscope en vervaldatum lezen | Lokale leestoegang | Installatierecord goedkeuren |
| **Inspecteren** | Via Git over SSH klonen of ophalen en REST-metadata opvragen | Repository lezen en API lezen | Geen na installatie |
| **Analyseren** | Bestanden, branches, pull requests en buildstatus via goedgekeurde tools lezen | Alleen-lezen-MCP-tools | Geen voor begrensde leesacties |
| **Wijziging voorbereiden** | Een patch, branchplan of concept-pull-request maken in een lokale werkruimte | Alleen lokaal schrijven | Diff en doel controleren |
| **Schrijven goedkeuren** | De exacte externe actie, scope en terugdraaistap presenteren | Nog geen externe schrijfactie | Menselijke goedkeuring |
| **Schrijfactie uitvoeren** | Een branch pushen, een pull request maken of een schrijfendpoint aanroepen | Kortlevende schrijfidentiteit | Elke actie bevestigen |
| **Verifiëren** | De resulterende commit, pull request of status lezen | Opnieuw alleen-lezen | Verwacht resultaat bevestigen |

Het standaardagentprofiel hoort na **Analyseren** of **Wijziging voorbereiden** te stoppen. Een afzonderlijk schrijfprofiel gebruikt een ander token of een andere sleutel, een korte vervaldatum, een vast doel en een goedkeuringsprompt. Een repositorytoegangssleutel kan de schrijfstap niet uitvoeren, wat een nuttige technische grens vormt.

## Terugdraaien en verwijderen

Begin rollback met het intrekken van toegang en ruim daarna de lokale configuratie op:

1. Verwijder de repository-, project- of werkruimtetoegangssleutel op de bijbehorende Bitbucket-instellingenpagina.
2. Trek het repository-, project-, werkruimte- of gebruikerstoken in op de bijbehorende Bitbucket-beveiligingspagina.
3. Verwijder de opgeslagen Teamwork Graph-referentie via de gedocumenteerde [authenticatieprocedure](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/getting-started/how-authentication-works/) voor de geïnstalleerde CLI-versie. Bewaar de vorige referentie alleen in de goedgekeurde geheimenbeheerder. Controleer dat het geïsoleerde profiel de testreferentie niet meer vermeldt.
4. Verwijder na de test het repositorybestand `.gitconfig` en de bijbehorende `includeIf`-regel. Laat overige Git-configuratie ongemoeid.
5. Verwijder alleen de gecontroleerde Bitbucket-hostsleutelregel die voor de test is toegevoegd. Behoud andere goedgekeurde hostsleutels.
6. Verwijder het externe `agent.env`-bestand en tijdelijke uitvoer. Haal de MCP-serververmelding uit de hostconfiguratie en start de host daarna opnieuw.

Registreer elke verwijdering, de uitvoerder en het tijdstip. Roteer een sleutel of token als een waarde in een onverwacht log, procesrecord of transcript terechtkwam.

## Een lus voor externe leesacties en lokale referentie-updates

Gebruik een kleine lus voor terugkerende repository-inspectie:

```bash
LOCAL_REPO="<local-directory>"
git -C "$LOCAL_REPO" fetch --no-tags
git -C "$LOCAL_REPO" status --short --branch
git -C "$LOCAL_REPO" log -1 --format='%H %ad %s' --date=iso-strict
```

`HEAD` betekent de huidige uitgecheckte verwijzing van de repository. Een geslaagd resultaat bewijst dat één toegestane SSH-identiteit de genoemde repository heeft bereikt. Het bewijst niet welke sleutel is geselecteerd of dat push-toegang bestaat.

**Verwachte uitvoer:** een fetch-resultaat, branchstatus en één commitregel. Niet-getest voorbeeld. `fetch` schrijft niets naar de remote, maar werkt lokale verwijzingen en `FETCH_HEAD` bij. De lus pusht niets en wijzigt geen branches.

De MCP-server hoort dezelfde leesgrens via benoemde bewerkingen aan te bieden. Een lokale shell-wrapper of MCP-tool moet een schrijfwerkwoord afwijzen voordat er een verzoek wordt verzonden. Log de toolnaam, repositorytijdelijke aanduiding, revisie, resultaatklasse en duur. Redigeer tokens, cookies, privépaden en bestandsinhoud, tenzij de taak één bestand expliciet vereist.

## Problemen oplossen

### `Permission denied (publickey)`

Controleer de actieve agentsocket, de geselecteerde publieke sleutel, de toegangssleutelvermelding van de repository en `IdentitiesOnly`. Een repositorysleutel moet bestaan op de doelrepository of het project. Een persoonlijke sleutel vereist accountmachtiging. Een werkruimtesleutel heeft een andere grens voor schrijfrechten.

### De verkeerde repositorysleutel wordt aangeboden

Gebruik één sleutel per repository met `core.sshCommand`, of groepeer klonen onder een map die via `includeIf` wordt beheerd. Bekijk agentsleutels met `ssh-add -l`. Als veel 1Password-sleutels beschikbaar zijn, gebruik dan een expliciete identiteitsselector of een 1Password SSH-bookmark. De [1Password Agent-gids](https://www.1password.dev/ssh/agent) beschrijft aandachtspunten rond het aantal sleutels en bookmarks.

### SSH meldt een gewijzigde hostsleutel

Stop de agent. Verwijder `known_hosts` niet als eerste reactie. Vergelijk de actuele Bitbucket Cloud-hostsleutelregistratie via een onafhankelijk kanaal met de lokale vermelding. Verwijder of vervang een vermelding pas nadat de vergelijking is geslaagd.

### De API retourneert `401` of `403`

Controleer de tokenvervaldatum, het tokentype, de endpointscope en de account- of werkruimtegrens. Een repositoryleesscope omvat geen pull requests. Een schrijfendpoint vereist een schrijfscope en een goedgekeurd schrijfprofiel. Verruim scopes niet voordat het mislukte endpoint bekend is.

### De API retourneert repositorygegevens maar geen pull requests

Voeg de kleinste pull-request-leesscope toe aan een nieuw of geroteerd token. Hergebruik geen breed gebruikerstoken voor een alleen-lezen-MCP-server.

### De MCP-server toont tools, maar een aanroep mislukt

Houd serverregistratie, verbinding, toolontdekking, uitvoering en resultaatverificatie uit elkaar. Bekijk het serverlog zonder het token bloot te leggen. Controleer endpoint en invoerstructuur. Probeer één keer opnieuw na controle van de verbinding. Markeer de bewerking als onvolledig wanneer de tweede aanroep ook mislukt.

### Een Bitbucket CLI van derden vraagt om brede toegang

Stop de installatie. Vergelijk de gevraagde toegang met de taakregistratie. Controleer broncode, releasesignaturen of checksums, netwerkbestemmingen, geheimenopslag en schrijfgedrag. De officiële Atlassian CLI-opdrachtreferentie bewijst geen ondersteuning voor een Bitbucket-binary van derden.

## Volgende stappen

Maak een beknopt toegangsrecord met de repository- of projectscope, sleutel-label, verificatiedatum van de hostsleutel, API-scopes, tokentermijn, 1Password-eigenaar, MCP-toollijst, logbeleid en goedkeurder van schrijfacties.

Voer één alleen-lezen-kloon, één REST-metadata-aanvraag en één MCP-toollezing uit met tijdelijke aanduidingen in het transcript. Vergelijk de resultaten. Houd het agentprofiel alleen-lezen totdat het record en de logs zijn gecontroleerd.

Maak eerst een lokale diff wanneer er een schrijftaak binnenkomt. Presenteer de doelbranch, gewijzigde paden, aangevraagde API-methode, tokenscope en rollbackstap. Gebruik pas een afzonderlijke, kortlevende schrijfidentiteit nadat iemand de exacte actie heeft goedgekeurd.
