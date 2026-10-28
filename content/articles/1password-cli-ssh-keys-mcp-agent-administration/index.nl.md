---
title: "1Password SSH Agent en CLI: Alleen-lezen AI-agent-toegang"
date: 2026-10-11
lastmod: 2026-10-28
toc: true
draft: false
description: "Ontwerp een alleen-lezen SSH-workflow met 1Password CLI, de SSH Agent en MCP. Gebruik synthetische commando's, beperkte machtigingen en menselijke goedkeuring voordat u live test."
genre: ["Systeembeheer", "Cloudbeveiliging", "Automatisering"]
tags: ["1Password CLI", "SSH-sleutels", "1Password SSH Agent", "MCP", "Model Context Protocol", "agentbeheer", "systeembeheer", "Bitbucket Cloud", "Git over SSH", "geheimverwijzingen", "serviceaccounts", "minimale machtigingen", "open sleutelauthenticatie", "geheimbeheer", "commandoregelbeveiliging", "automatiseringsveiligheid"]
cover: "/img/cover/1password-cli-ssh-keys-mcp-agent-administration.webp"
coverAlt: "Abstracte diagram van een agent die een geheimverwijzing, een SSH-agent en MCP-tools gebruikt zonder private sleutels te tonen."
coverCaption: ""
---

**Een command-line agent heeft nuttige toegang nodig, niet een kopie van elke inloggegevens.** Deze gids presenteert een begrensd ontwerp voor 1Password CLI, de 1Password SSH Agent, Bitbucket Git-toegang en Model Context Protocol (MCP). De eerste workflow gebruikt synthetische namen, alleen-lezen acties en menselijke goedkeuring op het SSH-grensgebied.

<!--more-->

Het belangrijkste onderscheid is eenvoudig. **Interactief SSH gebruikt toestemming via de 1Password SSH Agent. Onbeheerde automatisering heeft een aparte identiteit, beperkte toegang en een andere sleutellevenscyclus nodig.** Behandel een MCP-verbinding niet als toestemming om een van deze workflows uit te voeren.

## Belangrijkste punten

- **Bescherming van privésleutels:** De 1Password SSH Agent voert SSH-authenticatie uit terwijl de privésleutels binnen de 1Password-app worden bewaard.
- **Verwerking van openbare sleutels:** Publiceer alleen een openbare sleutel naar Bitbucket of een externe account. Bewaar de privé-helft in een SSH Key-item.
- **Interactieve toestemming:** Een persoon keurt een client- of terminalsessie goed voordat de SSH Agent een sleutel gebruikt.
- **Scheiding voor onbeheerde taken:** Een geplande taak heeft een toegewijde service-account en een beperkte vault-scope nodig. Een interactieve SSH Agent-goedkeuring voldoet niet aan deze behoefte.
- **MCP-grenzen:** MCP verbindt een agent met tools en bronnen. De client, server, besturingssysteem en 1Password-beleid bepalen nog steeds de toegang.

## Voordat u begint

**Vereisten:** Installeer 1Password 8 en 1Password CLI 2.20.0 of nieuwer. Meld u aan via een ondersteunde 1Password-account. Gebruik een OpenSSH-client. Maak een test-Bitbucket-repository of een andere niet-productie doel aan. Houd een tweede administratieve route beschikbaar voor terugrol.

**Tijd:** 30 tot 45 minuten voor een ontwerpbeoordeling en synthetische doorloop.

**Moeilijkheidsgraad:** Gemiddeld. U heeft basiskennis van Git, SSH, shell en toegangsbeheer nodig.

Deze gids behandelt ontwerp en planning. Het gelinkte Bitbucket-artikel behandelt Bitbucket-specifieke toegangsbeperkingen. Deze gids test geen live account, maakt geen echte sleutel, verbindt zich niet met een echte host en registreert geen echte MCP-server. Alle identificatoren hieronder zijn synthetisch. **Vervang placeholders alleen binnen uw eigen gecontroleerde omgeving.**

**Versiepositie:** Gebruik 1Password 8 en [1Password CLI 2.20.0 of nieuwer](https://www.1password.dev/ssh/manage-keys) voor deze workflow. [1Password CLI 1 is verouderd](https://www.1password.dev/cli/upgrade/). [1Password 7 wordt begin 2027 uitgefaseerd](https://support.1password.com/add-account/). SSH-sleutelgeneratie, import en delen vereisen 1Password 8. Bevestig de geïnstalleerde versies van Git, OpenSSH, MCP-host en MCP-server voordat u test. De voorbeelden hieronder zijn niet getest.

Een **vault** is een beveiligde 1Password-collectie van items. **OpenSSH** is de SSH-client- en serversoftware die door veel besturingssystemen wordt gebruikt. **MCP**, of Model Context Protocol, verbindt een agent met goedgekeurde tools of bronnen.

## Waarom private sleutels onleesbaar houden

Een SSH-sleutelpaar heeft een openbare sleutel en een private sleutel. Een externe Git-service of server bewaart de openbare sleutel. De client bewijst het bezit van de private sleutel tijdens de authenticatie. De private sleutel hoeft niet naar de externe service te reizen.

De [1Password SSH Agent](https://www.1password.dev/ssh/agent) breidt dit model uit. De documentatie stelt dat SSH- en Git-clients zich via de agent authenticeren terwijl de private sleutel in de 1Password-app blijft. De client ontvangt een ondertekenresultaat, niet een bestand met de private sleutel.

Deze grens vermindert verschillende blootstellingspaden:

- **Bronbeheer:** Een private sleutel komt niet in een repository of een pull request terecht.
- **Shellgeschiedenis:** Een private-sleutelwaarde verschijnt niet in een commandoargument.
- **Tijdelijke bestanden:** Een script hoeft geen private sleutel naar `~/.ssh/` te schrijven.
- **Agentcontext:** Een groot taalmodel (LLM) heeft de tekst van de private sleutel niet nodig om een SSH-bewerking aan te vragen.
- **Onbedoeld hergebruik:** Een gekopieerde sleutel blijft niet in een oude werkruimte achter nadat een taak is beëindigd.

De grens maakt SSH niet onschadelijk. Een proces met toestemming om de agent-socket te gebruiken, kan mogelijk acties uitvoeren als de goedgekeurde sleutel. Host-sleutelverificatie, beperkingen van externe accounts, repositoryrechten, commandobeleid en procesisolatie blijven belangrijk.

*De private-sleutelgrens beschermt het sleutelmateriaal. De grens keurt een extern commando niet goed of bewijst niet dat de doelhost betrouwbaar is.*

## Interactieve SSH-toestemming

Configureer een gewijzigde vault voor agent-sleutels. Gebruik het configuratiebestand van de SSH Agent om de kleinste sleutelset en een host-specifieke sleutel te selecteren. Stel niet elke in aanmerking komende sleutel uit elke ingebouwde vault bloot aan een automatiseringsproces.

Het [1Password SSH Agent-beveiligingsmodel](https://www.1password.dev/ssh/agent/security) koppelt goedkeuring aan een sleutel en een aanvragend proces. De prompt identificeert het proces en de sleutel. De persoon keurt de aanvraag vervolgens goed via de geconfigureerde authenticatiemethode.

1Password documenteert verschillende goedkeuringsbereiken. Goedkeuring per sleutel en per applicatie is de standaard. Een terminal-sessiebereik beperkt de goedkeuring tot een tabblad of sessie. Goedkeuring per aanvraag vraagt opnieuw voor elke aanvraag. Een goedkeuringsoptie voor alle processen bestaat, maar deze optie geeft elk proces onder de huidige besturingssysteemgebruiker toegang voor de sessie.

**Gebruik de smalste goedkeuringsomvang die geschikt is voor de taak.** Een systeemadministratieagent moet in een toegewijd terminalvenster of een sandbox worden uitgevoerd. Goedkeur niet elk proces als een enkel terminalvenster voldoende is.

De goedkeuringsessie is geen permanente machtiging. 1Password registreert de autorisatie voor de geconfigureerde periode of tot de app vergrendeld of afgesloten is. Wanneer de app is vergrendeld, behoudt de agent geen privé-sleutels voor later gebruik. Het SSH Agent-proces blijft op de achtergrond actief wanneer de ondersteunde instelling is ingeschakeld terwijl 1Password is gesloten, maar een nieuw ondertekenverzoek vereist dat 1Password is ontgrendeld.

De [1Password SSH-instellingsgids](https://www.1password.dev/ssh/get-started) toont de algemene werkwijze: een sleutel genereren of importeren, de openbare sleutel publiceren, de SSH Agent inschakelen, de SSH-client configureren, een SSH- of Git-opdracht uitvoeren en het verzoek goedkeuren. Het exacte socket-pad verschilt per besturingssysteem. Gebruik de instructies voor het huidige platform in plaats van een pad te kopiëren van een andere machine.

De 1Password-app moet ontgrendeld zijn voordat een nieuw ondertekenverzoek slaagt. Het agent-proces kan op de achtergrond blijven actief terwijl de app gesloten is. Een vergrendelde app geeft geen privé-sleutelmateriaal vrij voor het ondertekenen.

## Openbare sleutels en Bitbucket

De [1Password sleutelbeheergids](https://www.1password.dev/ssh/manage-keys) documenteert SSH Key-items, sleutelgeneratie, sleutelimport, openbare sleutels, vingerafdrukken en privé-sleutels. Het CLI-voorbeeld gebruikt `op item create --category ssh` om een SSH Key-item te maken. 1Password CLI genereert in dit voorbeeld standaard een Ed25519-sleutel en maskert de privé-sleutel in de uitvoer.

Bitbucket Cloud gebruikt de normale Git- en OpenSSH-commandoregelwerkwijze. De [commandoregelgids](https://support.atlassian.com/bitbucket-cloud/docs/find-the-command-line/) beschrijft Git-operaties vanuit een lokaal repository. De [SSH-configuratiegids](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) noemt SSH-remote-vormen en ondersteunde openbare sleutelformaten.

**Behandel Bitbucket als de gebruiker van de openbare sleutel.** Registreer de openbare sleutel of vingerafdruk via de goedgekeurde Bitbucket-account- of repositoryinstelling. Bewaar de privé-sleutel in 1Password. De Git-client vraagt de SSH Agent om te ondertekenen. De client leest geen privé-sleutelbestand.

Voor de Bitbucket-toegangssleutelomvang, registratiepad en read-only Git-test, zie [Bitbucket Cloud SSH Keys and Git CLI: Read-Only Access for AI Agents](/articles/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation/).

De Bitbucket-documentatie noemt dit een Git CLI-werkwijze. Dit artikel gaat niet uit van een aparte Bitbucket MCP-server of een product genaamd Bitbucket CLI. Een Bitbucket-specifieke CLI heeft zijn eigen actuele documentatie en zijn eigen machtigingsbeoordeling nodig.

## De grens tussen de Agent en MCP

Gebruik de huidige [MCP-specificatie](https://modelcontextprotocol.io/specification/2026-07-28) bij het beoordelen van een nieuwe server.

De specificatie-URL van 2025-06-18 in de volgende achtergrondparagraaf is een historische versie. Gebruik de specificatie van 2026-07-28 voor nieuwe beoordelingen.

[MCP](https://modelcontextprotocol.io/specification/2025-06-18) standaardiseert verbindingen tussen een LLM-toepassing, een clientconnector en een server. Een server biedt tools, resources of prompts. De specificatie stelt ook dat hosts toestemming van de gebruiker moeten verkrijgen voordat ze gegevens blootleggen of tools aanroepen.

**MCP zelf verleent geen machtigingen.** Een MCP-tool wordt nog steeds uitgevoerd binnen de machtigingen van het serverproces, de besturingssysteemgebruiker, het netwerkpad, het cloudaccount en de geconfigureerde inloggegevens. Een toolbeschrijving is geen autorisatiebeleid.

De [1Password Security for AI-documentatie](https://www.1password.dev/security-for-ai) beschrijft een Environments MCP Server en veilige MCP-configuratiemodellen. Dezelfde pagina beschrijft het laden van MCP-configuratiewaarden uit 1Password op runtime. Deze pagina's definiëren geen generiek 1Password SSH-sleutel-MCP-product of een universele SSH-workflow voor elke agent-client.

Gebruik MCP als een beperkt besturingsoppervlak:

- **Lees-tools:** Inspecteer de status van services, metagegevens van repositories of goedgekeurde logs.
- **Plan-tools:** Bereid een commando of wijzigingsregistratie voor zonder het commando uit te voeren.
- **Goedkeurings-tools:** Vraag een menselijke beslissing aan vóór een remote write.
- **Schrijf-tools:** Houd uitgeschakeld totdat het doel, het commando, de reikwijdte en het terugrolplan expliciet zijn.

De agent moet referenties, metagegevens en operatieresultaten ontvangen. **De agent moet geen private-sleuteltekst, een volledige vault-dump of een onbeperkte shell ontvangen.**

## Een veilige eerste beleid

Begin met een schriftelijk beleid voordat u een agent inschakelt. Houd het beleid dicht bij de MCP-configuratie, maar plaats geen inloggegevens in het bestand.

```yaml
agent_policy:
  purpose: "Read-only repository and system inspection"
  identities:
    interactive_ssh: "1Password SSH Agent with per-terminal consent"
    unattended_jobs: "Dedicated service account with one narrow vault"
  allowed:
    - "Read repository metadata through Git"
    - "Read approved service status and logs"
    - "Run one synthetic SSH connectivity check"
  approval_required:
    - "Any remote write"
    - "Any package, firewall, clock, or service change"
    - "Any new host-key acceptance"
    - "Any private-key export"
  denied:
    - "Read or print private-key fields"
    - "List every vault or every item"
    - "Write tokens or secrets to shell profiles"
    - "Run arbitrary commands from tool output"
  rollback:
    - "Revoke the service account"
    - "Remove the public key from the target"
    - "Disable the MCP server entry"
    - "Lock 1Password and end the agent session"
```

Dit beleid is een voorbeeld, geen 1Password-configuratieformaat. Bewaar het echte beleid in het control plane dat door uw agent-client wordt gebruikt. Beoordeel elke tool aan de hand van het beleid voordat u elke tool inschakelt.

## Serviceaccounts en secret-referenties

Een **serviceaccount** geeft een geautomatiseerd proces een eigen identiteit. De [1Password CLI-scriptgids](https://www.1password.dev/cli/secrets-scripts) beveelt serviceaccounts aan voor least-privilege-toegang tot geselecteerde vaults. Dit scheidt een onbeheerd job van de SSO, MFA, vault-inventaris en dagelijkse account van een persoon.

Een **geheimreferentie** noemt een waarde zonder de waarde in de bron te plaatsen. De [1Password CLI-referentie](https://www.1password.dev/cli/reference) gebruikt de vorm `op://vault/item/field`. De referentie is alleen veilig op te slaan wanneer het omringende proces nog steeds beperkte toegang heeft. Een referentie omzeilt geen beleid.

Gebruik `op read` wanneer één commando één waarde nodig heeft. Gebruik `op run` wanneer een kindproces een gecontroleerde set runtime-waarden nodig heeft. Gebruik `op item create` wanneer een nieuw SSH Key-item moet bestaan in de goedgekeurde kluis.

Verwar runtime-injectie niet met bescherming van een privé-sleutel. Een API-token dat als omgevingsvariabele wordt doorgegeven, is nog steeds zichtbaar voor het kindproces. Een privé-sleutel die via een omgevingsvariabele wordt doorgegeven, is erger, omdat de waarde de blootstelling vergroot aan procesinspectie, crashrapporten, debugoutput, shell-tracing en onbedoelde logregistratie.

**Kies voor een referentie in de bron en een runtime-waarde in het kleinste mogelijke proces.** Houd het proces van korte duur. Schakel shell-tracing uit. Print de omgeving niet. Verwijder tijdelijke bestanden na een mislukte uitvoering.

## Veilige eerste workflow

De onderstaande volgorde scheidt de registratie van de openbare sleutel, interactieve SSH, MCP-detectie en onbemand ontwerp.

### 1. Definieer het doel

Noteer de doelklasse, het externe account, de beoogde repository of het commando, de bron van de hostsleutel, de goedkeuringsbevoegde en de rollback-actie. Gebruik een synthetisch record tijdens de eerste oefening.

```text
target_class: test-repository
remote_account: git
operation: read-only connectivity check
host_key_source: approved administrator record
approval_owner: named operator
rollback: remove public key and revoke test identity
```

**Verwacht resultaat, niet getest:** Het record identificeert één doel en één operatie. Het record bevat geen hostnaam, IP-adres, token, privé-sleutel of persoonlijke gegevens.

### 2. Maak of selecteer het SSH Key-item

De officiële [1Password SSH-sleutelgids](https://www.1password.dev/ssh/manage-keys) documenteert het CLI-creatiepatroon. Het onderstaande commando gebruikt een synthetische titel en een benoemde testkluis.

```bash
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
```

**Verwachtte output, niet getest:** 1Password maakt een SSH Key-item aan in de benoemde testkluis en maskert de privé-sleutel in de terminaloutput. Het commando wijzigt de 1Password-status. De exacte menslezbare output hangt af van de CLI-versie en de inlogstatus.

Vang het geretourneerde item-identificatienummer op in het testrecord zonder het veld voor de privé-sleutel te kopiëren. Gebruik het identificatienummer of de exacte itemtitel voor latere veldspecifieke leestaken alleen nadat het itemschema is bevestigd.

Stuur deze output niet door naar een gedeeld logboek. Vang alleen het item-identificatienummer, de vingerafdruk van de openbare sleutel en het goedkeuringsrecord op wanneer de lokale procedure veilige gestructureerde output ondersteunt.

### 3. Behandel de openbare sleutel

Open het SSH Key-item in 1Password en gebruik de actie **Copy Public Key**. Gebruik een veldspecifieke referentie pas nadat u het label van het openbare-sleutelveld in uw eigen account heeft bevestigd. Dump het volledige item niet.

```bash
PUBLIC_KEY_REF="op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
op read "$PUBLIC_KEY_REF"
```

**Verwacht resultaat, niet getest:** Eén synthetische OpenSSH openbare-sleutelregel of een openbare-sleutelwaarde uit het bevestigde veld. De placeholder-veldnaam hierboven is geen belofte over het veldlabel van uw item.

Registreer de openbare sleutel in het goedgekeurde Bitbucket-account, de Bitbucket-repository of het externe account. Plak de bijbehorende private sleutel nooit in Bitbucket. De [Bitbucket SSH-handleiding](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) adviseert ook om de Bitbucket host key te registreren vóór de eerste verbinding.

Voor Bitbucket: haal het gepubliceerde host-key-record op en vergelijk dit record met een onafhankelijke, betrouwbare kopie voordat u een regel toevoegt aan `~/.ssh/known_hosts`. Gebruik strikte host-controle nadat de vergelijking is geslaagd. Accepteer geen gewijzigde host key tijdens een agent-run.

### 4. Interactieve SSH inschakelen

Schakel de 1Password SSH Agent in de desktop-app in. Configureer OpenSSH met de platformspecifieke waarde `IdentityAgent` of `SSH_AUTH_SOCK` uit de [officiële installatiehandleiding](https://www.1password.dev/ssh/get-started). Beperk de eerste test tot één repository of één niet-productieaccount.

Op macOS of Linux: stel de socket in vanuit de platforminstallatiehandleiding en voer `ssh-add -l` uit. Op Windows: gebruik de ondersteunde named-pipe-configuratie en verifieer de beschikbare sleutels via de 1Password SSH Agent-interface of een gedocumenteerde Windows SSH-test. Presenteer `ssh-add -l` niet als een cross-platform verificatiecommando.

Alleen op macOS of Linux:

```bash
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**Verwacht resultaat, niet getest:** Op macOS of Linux toont `ssh-add -l` vingerafdrukken van de actieve agent. Op Windows: gebruik de gedocumenteerde named-pipe-test of de 1Password SSH Agent-interface. Een geslaagde Git-leesoperatie retourneert een commit-referentie. De repository-placeholder hierboven moet worden vervangen in een gecontroleerde test.

Het commando gebruikt een repository-placeholder. Vervang de placeholder alleen in een gecontroleerde test. **Keur geen prompt goed voor een doel of proces dat u niet verwachtte.**

### 5. MCP toevoegen nadat het SSH-pad werkt

Verifieer eerst de SSH-client en het doel zonder MCP. Voeg daarna één read-only MCP-server of lokale connector toe. Geef de agent een tool zoals `read_status` of `prepare_command`. Begin niet met een algemene shell-tool.

De MCP-configuratie moet runtime-waarden refereren via het door de client ondersteunde omgevingsmechanisme. De [1Password AI security guide](https://www.1password.dev/security-for-ai) beschrijft het vervangen van plaintext MCP-configuratietokens door omgevingsvariabelen die worden geladen uit 1Password. **Houd de referentie of de variabelenaam in de configuratie. Houd de opgeloste waarde buiten het transcript van de agent.**

Dit gedeelte beschrijft een ontwerp, geen geteste MCP-configuratie. Er is hier geen client, server, transport, versie of fixture vastgelegd. Valideer één read-only server in een apart testprofiel voordat een agent wordt verbonden met een productiesysteem.

### 6. Noteer het resultaat

Noteer de doelklasse, toolnaam, goedkeuringsbeslissing, open-sleutelvingerafdruk, commando-uitkomst en opschoningsresultaat. Laat geheime waarden weg. Markeer elke output als waargenomen of verwacht.

**Verwacht resultaat, niet getest:** De agent leest de status, stelt een beperkt commando voor, ontvangt expliciete goedkeuring voor het SSH-verzoek, voltooit de read-only operatie en produceert een record zonder private-sleuteltekst.

## Synthetische commandosequentie

De volgende sequentie toont de volgorde zonder gebruik van echte infrastructuur. Deze commando's zijn slechts voorbeelden. Ze zijn niet uitgevoerd tijdens de voorbereiding van het artikel.

```bash
op --version
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
op read "op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
# macOS or Linux only
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**Verwachte output, niet getest:**

```text
2.x.y
SSH Key item created. Private key: redacted
ssh-ed25519 AAAA<synthetic-public-key> synthetic-key-label
256 SHA256:<synthetic-fingerprint> synthetic-agent-admin-key (ED25519)
<synthetic-commit-id>        HEAD
```

Het outputblok is illustratief. Het blok vertegenwoordigt geen uitvoering tegen een 1Password-account, Bitbucket, Git-provider of remote host. Een productierecord moet alleen goedgekeurde metadata en een succes- of mislukkingstoestand opslaan.

## Interactieve versus onbeheerde toegang

| Toegangsmodus | Identiteit | Private-sleutelpad | Goedkeuringsmodel |
|---|---|---|---|
| **Interactief SSH** | Menselijk account via 1Password SSH Agent | Private sleutel blijft in de 1Password-app | Mens keurt een proces, terminalsessie of verzoek goed |
| **Geplande read** | Toegewijd serviceaccount | `op run` levert smalle runtime-waarden | Jobbeleid en serviceaccount-scope |
| **Gepland SSH** | Toegewijd automatiseringsidentiteit | Sleutelexport blijft een laatste-middel-ontwerp | Jobisolatie, korte levensduur, hostbeperking en rotatie |
| **Agent write** | Menselijk of taakspecifiek identiteit | Afhankelijk van de goedgekeurde integratie | Menselijke goedkeuring vóór elke gedefinieerde wijziging |

*Plan geen workflow rondom een interactieve SSH Agent-prompt. Gebruik een apart automatiseringsontwerp of houd de stap menselijk bediend.*

Voor onbemande taken, maak een serviceaccount aan met toegang tot één kluis of een kleine set items. Geef de taak één doel. Gebruik een toegewijd repository- of serveraccount. Voeg host-key-verificatie toe. Stel een uitvoeringstime-out in. Log actiemetadata zonder geheimen. Rotatie of intrek het identiteitsbewijs na de test.

Als een onbemande taak echt een SSH-prive-sleutel nodig heeft, gebruik dan een toegewijde automatiseringsleutel met een beperkt remote-account en een gedocumenteerde einddatum. Het ophalen van de prive-sleutel met `op read` exporteert nog steeds sleutelmateriaal over een procesgrens. Dit ontwerp heeft een groter blast radius dan de 1Password SSH Agent. Kies bij voorkeur voor een platformidentiteit, een deploy-service of een andere workload-identiteit wanneer het doel dit ondersteunt.

## Waarom platte-tekst-omgevingsvariabelen het risico verhogen

Omgevingsvariabelen houden geheimen buiten bronbestanden, maar maken ze niet onzichtbaar. Een kindproces leest zijn omgeving. Procesinspectie, crash-handlers, debug-uitvoer, shell-tracing en gekopieerde commandorecords kunnen waarden blootleggen.

1Password documenteert `op run` als een runtime-methode voor het laden van referenties in een kindproces. Gebruik `op run` voor waarden die een proces echt nodig heeft. Houd het kindproces van korte duur en beperk zijn commando. Geef een prive-sleutel niet door via `SSH_PRIVATE_KEY`, `KEY` of een vergelijkbare variabele wanneer de SSH Agent de noodzaak voor export wegneemt.

De veiligere volgorde is:

1. **Gebruik de SSH Agent** voor interactieve SSH.
2. **Gebruik openbare-sleutelregistratie** voor Bitbucket of het remote-account.
3. **Gebruik `op run`** voor een beperkt onbemand kindproces.
4. **Gebruik `op read`** voor één waarde wanneer een kindproces geen volledige omgeving nodig heeft.
5. **Exporteer een prive-sleutel** alleen na een schriftelijke uitzondering, een beperkte scope, een opruimplan en een rotatieplan.

## Beslisstabel

| Behoefte | Voorkeurspad | Reden om te stoppen of te ontwerpen |
|---|---|---|
| Mens voert Git uit via SSH | 1Password SSH Agent | Stop als de prompt een onverwacht proces of sleutel noemt |
| Registreren van een repository-sleutel | Lees of vul de openbare sleutel automatisch in | Kopieer nooit de private sleutel naar de repository-service |
| Agent leest service-status | Alleen-lezen MCP-tool met OS-niveau bereik | Stop als de tool een onbeperkte shell blootlegt |
| Agent stelt een wijziging op de remote voor | Plan-tool gevolgd door menselijke goedkeuring | Stop als doel, commando of rollback onduidelijk is |
| Job leest één API-token | Service account plus `op read` of `op run` | Stop als het token in broncode, logs of een profiel op globaal niveau terechtkomt |
| Job heeft SSH-toegang nodig | Workload identity of toegewijde automatiseringsleutel | Stop als de job een persoonlijke sleutel of breed account vereist |
| MCP-configuratie heeft een token nodig | Runtime-referentie geladen door de ondersteunde client | Stop als een token in platte tekst naar de configuratie wordt gecommit |

## Behandeling van fouten

**Onverwacht SSH-consentvenster:** Weiger het venster. Controleer de procesnaam, de terminalsessie, de sleutelvingerafdruk, het repository-doel en de hostsleutel. Beoordeel de SSH-clientconfiguratie voordat u opnieuw probeert.

**Geen SSH Agent-socket:** Bevestig dat de 1Password-desktopapp is geïnstalleerd via een ondersteunde methode, dat de SSH Agent is ingeschakeld en dat de client de platformspecifieke socket gebruikt. De [officiële SSH Agent-pagina](https://www.1password.dev/ssh/agent)] bevat de vereisten voor besturingssystemen en links voor socket-instellingen.

**Openbare sleutel-authenticatie mislukt:** Controleer de geselecteerde openbare sleutel, het remote-account, de repository-permissie, de hostsleutel en de SSH-configuratie. Gebruik een vergelijking van openbare vingerafdrukken. Los de fout niet op door een ongerelateerde private sleutel te exporteren.

**`op read` weigert toegang:** Controleer het bereik van de service-account kluis, de item-identificatie, de veldreferentie, de inlogstatus en de itemstatus. Beperk de referentie tot één goedgekeurd item. Verbreed de kluisverlening niet als eerste reactie.

**`op run` blootlegt een waarde:** Stop de job. Bewaar alleen het minimale incidentverslag. Verwijder gekopieerde logs en tijdelijke bestanden volgens uw retentieprocedure. Roteer de beïnvloede geheimen of sleutels. Beoordeel shell-tracing, procesinspectie, crashrapporten en de retentie van MCP-transcripties.

**MCP-tool gedraagt zich onverwacht:** Behandel tooloutput als onbetrouwbare gegevens. Stop voordat u commando's uitvoert die door de output worden voorgesteld. Onderzoek de broncode, configuratie, machtigingen en transport van de server. De MCP-host moet toestemming van de gebruiker verkrijgen. De specificatie biedt ook richtlijnen voor implementatoren inzake toestemming en toegangscontroles, maar het protocol vervangt uw eigen beoordeling niet.

## Terugrollen en verwijderen

Terugrollen begint met het intrekken van toegang, niet met het verwijderen van bestanden.

1. **Stop de agent of de geplande taak.** Schakel de MCP-serverinvoer uit of koppel de client los.
2. **Vergrendel 1Password.** Beëindig de interactieve SSH-autorisatiesessie.
3. **Verwijder de openbare sleutel.** Verwijder de testsleutel uit Bitbucket, de repository of het externe account.
4. **Intrek de serviceaccount.** Verwijder de kluis-toegang en ongeldig maak het token.
5. **Verwijder het test-SSH-sleutelitem** nadat u hebt bevestigd dat er geen goedgekeurde workflow het item gebruikt.
6. **Verwijder tijdelijke configuratie.** Verwijder testverwijzingen, lokale socket-overrides en gegenereerde logs.
7. **Beoordeel het bewijs.** Bevestig dat het terugrolrecord geen privésleutel, token of omgevingsdump bevat.

*Een verwijderd lokaal bestand trekt een openbare sleutel, serviceaccount, gecachet token of externe autorisatie niet in. Verwijder elke machtiging bij de bron.*

## Problemen oplossen

### De agent vraagt bij elk commando om een sleutel

Controleer het geselecteerde autorisatiebereik. Goedkeuring per verzoek is restrictiever. Een terminal- of applicatiesessie is mogelijk beëindigd. 1Password vraagt ook opnieuw na een vergrendel- of afsluitgebeurtenis.

### De agent ziet een privésleutel in zijn transcript

Stop de workflow en roter de sleutel. Onderzoek de MCP-serverrespons, shellcommando, debuglog en toolwrapper. Vervang het lezen van privésleutels door het gebruik van SSH Agent voor interactieve taken. Voor taken, vervang een persoonlijke sleutel door een gewijde identiteit en een gedocumenteerde uitzondering.

### Een sleutellijst bevat te veel identiteiten

De 1Password SSH Agent toont in aanmerking komende sleutels uit de geconfigurede kluis. Gebruik een gescope agent-configuratie of host-specifieke SSH-configuratie. De [agent-documentatie](https://www.1password.dev/ssh/agent)] noemt ook de limiet van zes sleutels voor de OpenSSH-server.

### Een commando werkt handmatig maar faalt in een taak

Vergelijk identiteit, kluisbereik, omgeving, host-sleutelgegevens, werkmap en goedkeuringsaannames. Een interactieve 1Password-sessie omvat menselijke toestemming. Een geplande taak niet. Ontwerp de taak als een aparte toegangsmodus.

### De MCP-server is verbonden maar de taak faalt

Een verbinding bewijst geen machtiging. Controleer tooldetectie, servergeloofsbrieven, cliënttoestemming, besturingssysteemrechten, netwerktoegang en rechten aan de doelzijde in aparte stappen. Houd de eerste test alleen-lezen.

## Volgende stappen

Gebruik de huidige MCP-specificatie van 28-07-2026 voor nieuwe goedkeuringen. Elke link naar de specificatie van 18-06-2025 in dit artikel is historische achtergrond.

Begin met één synthetische repository en één alleen-lezen MCP-tool. Noteer elk verwacht resultaat als niet getest totdat een gecontroleerde omgeving bewijs levert. Herhaal vervolgens de workflow met een niet-productiedoel, een benoemde operator, een geverifieerde hostkey en een schriftelijk terugvalrecord.

Lees de [1Password CLI-referentie](https://www.1password.dev/cli/reference) voor de huidige commandovlaggen. Lees [Laad secrets in scripts](https://www.1password.dev/cli/secrets-scripts) voordat u automatisering met service-accounts aanmaakt. Lees de [MCP-specificatie](https://modelcontextprotocol.io/specification/2026-07-28) voordat u tools van een nieuwe server goedkeurt.

**Houd interactieve SSH menselijk goedgekeurd. Houd onbeheerde toegang gescheiden. Houd private keys onleesbaar wanneer het doel agentgebaseerde authenticatie ondersteunt.**
