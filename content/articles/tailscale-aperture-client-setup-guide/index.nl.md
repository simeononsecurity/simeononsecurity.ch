---
title: "Tailscale Aperture: AI-clients configureren voor inferentie en MCP in 2026"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Leid modelverzoeken en MCP-tools via Tailscale Aperture. Stel Codex, Claude Code, Claude Desktop, OpenCode en Hermes in op een ander apparaat of een andere gateway."
genre: ["Kunstmatige intelligentie", "Ontwikkelaarstools", "Netwerken"]
tags: ["Tailscale Aperture", "Aperture instellen", "AI-proxy", "LLM-gateway", "MCP-gateway", "Codex Aperture", "Claude Code Aperture", "Claude Desktop Aperture", "OpenCode Aperture", "Hermes Agent Aperture", "Codex MCP", "Claude MCP", "OpenCode MCP", "Hermes MCP", "AI-inferentieproxy", "Responses API", "Anthropic Messages API", "Externe MCP", "Streamable HTTP", "Tailscale", "Zelfgehoste AI", "Codeeragenten", "AI-clientconfiguratie"]
cover: "/img/cover/tailscale-aperture-agent-setup.webp"
coverAlt: "Aperture verbindt clientpanelen met model- en MCP-toolservices via aparte blauwe inferentie- en groene toolroutes"
coverCaption: ""
---

## Inleiding

Tailscale Aperture geeft AI-clients één gateway die met de tailnet is verbonden voor modelinferentie en Model Context Protocol (MCP)-tools. Elke client moet een route gebruiken die bij het API-protocol past. MCP-tools gebruiken een apart endpoint. Aperture-grants bepalen welke modellen en connectors elke Tailscale-identiteit mag gebruiken.

Deze gids laat zien hoe je Codex, Claude Code, Claude Desktop, OpenCode en Hermes instelt op macOS, Linux en Windows. De gids behandelt CLI- en desktopinstellingen, laat zien hoe je model-ID's voor je eigen identiteit opvraagt en bevat een geanonimiseerde prompt die je kunt hergebruiken bij het instellen van een ander apparaat of een andere Aperture-instantie.

**Route kiezen:** Endpointpaden hangen af van je gateway en elk API-protocol. Een Responses-route zoals `/codex` verwerkt geen Anthropic Messages- of MCP-verkeer. Controleer de hostnaam van de gateway en de inferentieroute van elke client. Vraag model-ID's op via je eigen Aperture-toegang voordat je clientinstellingen wijzigt.

## Belangrijkste punten

- **Modelverkeer** heeft de API-route nodig die bij het clientprotocol hoort.
- **MCP-verkeer** gebruikt het aparte endpoint `/v1/mcp`.
- **Gatewaymachtigingen** moeten je Tailscale-identiteit toegang geven tot elk model en elke connector.
- **Clientconfiguratie** bewijst alleen dat instellingen zijn opgeslagen. Controleer een echt verzoek en een MCP-toolaanroep.

## Hoe de routes samenhangen

| Doel | Clientverzoek | Aperture-route | Dienst van de route |
|---|---|---|---|
| Codex en Responses-compatibele modellen | OpenAI Responses API | Meestal `/v1`. Een aangepast pad zoals `/codex` is deploymentspecifiek. | Modelinferentie |
| Claude-modelinferentie | Anthropic Messages API | Basis-URL van de gateway. Aperture verwerkt `/v1/messages` | Claude-compatibele inferentie |
| MCP-tools | Streamable HTTP MCP | `/v1/mcp` | Tools en bronnen van ingestelde connectors |

{{< figure src="aperture-client-routes.webp" alt="Codex en Hermes gebruiken een Responses-route, Claude gebruikt Anthropic Messages en MCP-clients gebruiken de aparte route /v1/mcp naar Aperture-connectors" caption="Modelinferentie en MCP-verkeer gebruiken aparte Aperture-endpoints" >}}

**Providerroots:** Aperture voegt de clientverzoekpaden toe aan de basis-URL van de provider. Stel `baseurl` van de provider in op de API-root. Voeg geen `/v1` toe aan een upstream-basis-URL als het inkomende pad al `/v1` bevat. Zie de [Aperture-configuratiereferentie](https://tailscale.com/docs/aperture/configuration) voor URL-opbouw, modelregistratie en grants.

## De gateway voorbereiden

**Vraag voordat je iets wijzigt** een Aperture-beheerder om deze waarden:

- **Gatewayhostnaam:** Gebruik `http://` voor de meeste clients die met de tailnet zijn verbonden. Claude Desktop-inferentie vereist `https://` met een vertrouwd certificaat.
- **Inferentieroutes:** OpenAI Responses en Anthropic Messages gebruiken verschillende aanvraagindelingen.
- **Model-ID's:** Vraag met het endpoint hieronder op welke modellen beschikbaar zijn voor je Tailscale-identiteit. Gebruik de exacte ID's die voor die identiteit worden geretourneerd.
- **Authenticatie:** Controleer of de client een tijdelijke API-sleutel of gebruikersgegevens verstuurt.
- **MCP-endpoint:** Meestal `http://<APERTURE_HOST>/v1/mcp` voor tailnet-clients. Claude Desktop-inferentie vereist HTTPS met een vertrouwd certificaat.
- **Toegangsmachtigingen:** Controleer model- en connectormachtigingen voor je Tailscale-identiteit.

**Netwerktoegang:** Het clientapparaat moet de gateway via de tailnet bereiken. Een hostnaam alleen geeft geen toegang tot modellen of tools. Aperture weigert toegang zonder een passende grant voor het model of de connector.

### Modellen vinden die voor je gebruiker beschikbaar zijn

**Vraag de modellijst op** vanaf een apparaat dat met dezelfde tailnet is verbonden. Aperture gebruikt de Tailscale-identiteit van het apparaat en retourneert modellen die aan die gebruiker zijn toegekend, zoals beschreven in de [gids voor modelgrants](https://tailscale.com/docs/aperture/how-to/grant-model-access):

```sh
# macOS of Linux
curl -fsS http://<APERTURE_HOST>/v1/models
```

```powershell
# Windows PowerShell, gebruik curl.exe om de oude curl-alias te omzeilen
curl.exe -fsS http://<APERTURE_HOST>/v1/models
```

**De uitkomst lezen:** Gebruik elke geretourneerde `id` als model-ID. Controleer `metadata.provider.id` om de Aperture-provider te herkennen. Kies een model dat het API-formaat van de client ondersteunt. Claude Desktop vereist bijvoorbeeld een Anthropic Messages-model. De [modellenlijst](https://tailscale.com/docs/aperture/reference/chat) van Aperture toont ook identifiers die beschikbaar zijn voor de aangemelde gebruiker.

**Ontbrekende modellen:** Verschijnt een verwacht model niet, vraag dan een Aperture-beheerder de providerconfiguratie en je modelgrant te controleren. Via het endpoint kunnen gebruikers zichzelf geen toegang geven.

**URL-schema:** Tailscale raadt `http://` aan voor de meeste clients op dezelfde tailnet. WireGuard versleutelt dat verkeer. Claude Desktop vereist `https://` en een certificaat dat het besturingssysteem vertrouwt. Gebruik het schema dat hieronder per client staat.

### Een inferentieprovider toevoegen

**OpenAI Responses:** Voeg de upstreamprovider toe aan Aperture en schakel het API-formaat in dat de client gebruikt. Voeg voor een OpenAI-provider bijvoorbeeld dit fragment toe:

```json
{
  "providers": {
    "openai": {
      "baseurl": "https://api.openai.com",
      "apikey": "<UPSTREAM_PROVIDER_KEY>",
      "models": ["<MODEL_ID>"],
      "compatibility": {
        "openai_chat": true,
        "openai_responses": true
      }
    }
  }
}
```

**Anthropic Messages:** Gebruik de Anthropic API-root, de autorisatie-indeling `x-api-key` en de compatibiliteit `anthropic_messages`. De model-ID moet ook in de lijst `models` van de provider staan. Voeg bijvoorbeeld dit fragment toe:

```json
{
  "providers": {
    "anthropic": {
      "baseurl": "https://api.anthropic.com",
      "apikey": "<UPSTREAM_PROVIDER_KEY>",
      "authorization": "x-api-key",
      "models": ["<CLAUDE_MODEL_ID>"],
      "compatibility": {
        "anthropic_messages": true
      }
    }
  }
}
```

**Configuratiewijzigingen:** Vervang elke placeholder door je upstreamwaarden. Voeg de fragmenten toe aan de bestaande Aperture-configuratie. Behoud de rest van het huidige bestand. Schakel compatibiliteitsvlaggen in voor de API's die je provider ondersteunt.

**Toegangsmachtigingen:** Aperture beheert gebruikerstoegang tot elk model en elke connector. Geef elke beoogde Tailscale-gebruiker alleen de benodigde rechten. Dit voorbeeld geeft één gebruiker toegang tot één providermodel en één connector:

```json
{
  "grants": [
    {
      "src": ["<TAILSCALE_USER>"],
      "app": {
        "tailscale.com/cap/aperture": [
          {"role": "user", "models": "openai/<MODEL_ID>"},
          {"connectors": ["teamtools/**"]}
        ]
      }
    }
  ]
}
```

**Modelgrant:** Gebruik de provider-ID en model-ID in het grantpatroon. De [gids voor connectorconfiguratie](https://tailscale.com/docs/aperture/connectors/get-started) toont de huidige instelling `connectors.servers`. De oudere configuratie op hoofdniveau `mcp.servers` is verouderd.

### Een MCP-connector toevoegen

**MCP-connector:** Aperture maakt verbinding met upstream-MCP-servers en biedt tools aan via `/v1/mcp`:

```json
{
  "connectors": {
    "servers": {
      "teamtools": {
        "protocol": "mcp",
        "url": "<UPSTREAM_MCP_ENDPOINT>"
      }
    }
  }
}
```

**Connector-URL:** Gebruik het volledige MCP-endpoint van de upstreamserver. Geef je Tailscale-gebruiker daarna toegang tot `teamtools/**` of tot een beperkter toolpatroon. De [referentie voor de MCP-proxy](https://tailscale.com/docs/aperture/mcp-server) legt het ene clientendpoint en het gedrag van connectors uit.

## Codex CLI en desktop

**Gedeelde instellingen:** Codex CLI en de desktopapp gebruiken dezelfde configuratie. Bewerk op macOS en Linux `~/.codex/config.toml`. Bewerk op Windows `%USERPROFILE%\.codex\config.toml` (shells die de homemap uitbreiden accepteren ook `~/.codex/config.toml`). Het [overzicht van de Codex-app](https://openai.com/index/introducing-the-codex-app/) vermeldt dat de desktopapp de Codex CLI-configuratie gebruikt. Codex-gebruikersinstellingen staan in `~/.codex/config.toml`. De documentatie over [configuratiebasis](https://learn.chatgpt.com/docs/config-file/config-basic) beschrijft provider- en MCP-velden op gebruikersniveau. Voeg de provider aan dit bestand toe, start de app opnieuw en controleer of provider en model in de interface verschijnen.

```toml
model = "<MODEL_ID>"
model_provider = "aperture"

[model_providers.aperture]
name = "Aperture Proxy"
base_url = "http://<APERTURE_HOST>/v1"
wire_api = "responses"
requires_openai_auth = true
supports_websockets = false
```

**Optionele velden:** Deze twee waarden passen bij één Codex-providerinstelling. Behoud ze alleen als je gateway en Codex-configuratie ze vereisen. De huidige [Tailscale-gids voor Codex Aperture](https://tailscale.com/docs/aperture/how-to/use-codex) laat ze weg, gebruikt `wire_api = "responses"` en vermeldt dat Aperture upstreamgegevens invoegt. Gebruik de exacte Responses-URL van je gatewaybeheerder. `/codex` is deploymentspecifiek. De door Tailscale gedocumenteerde standaardroute is `/v1`.

**MCP-configuratie:** Voeg de server aan dezelfde gebruikersconfiguratie toe:

```toml
[mcp_servers.aperture]
url = "http://<APERTURE_HOST>/v1/mcp"
enabled = true
```

**Codex controleren:** Voer `codex mcp list` uit, start een nieuwe sessie en bekijk `/mcp`. De serverlijst bewijst registratie. Een vermelde tool en een geslaagde aanroep bewijzen ontdekking en uitvoering. De [Codex-configuratiereferentie](https://learn.chatgpt.com/docs/config-file/config-reference) beschrijft provider- en MCP-instellingen op gebruikersniveau.

## Claude Code CLI

**Protocol:** Claude Code gebruikt Anthropic Messages. Stel het globale Claude Code-instellingenbestand in op de Anthropic-compatibele Aperture-gateway. Gebruik `~/.claude/settings.json` op macOS en Linux of `%USERPROFILE%\.claude\settings.json` op Windows. Gebruik in PowerShell het overeenkomstige pad `$HOME\.claude\settings.json`. De route moet `/v1/messages` bedienen. Codex Responses gebruikt een ander protocol en een andere route. Tailscale raadt HTTP aan voor Claude Code op de tailnet, omdat WireGuard de verbinding versleutelt.

```json
{
  "apiKeyHelper": "echo '-'",
  "env": {
    "ANTHROPIC_BASE_URL": "http://<APERTURE_HOST>"
  }
}
```

**Clientauthenticatie:** De Aperture-clientgids gebruikt een placeholder in `apiKeyHelper`, omdat Aperture de upstreamreferentie invoegt. Voor het doorgeven van een Claude-abonnement moet de Anthropic-provider van Aperture de Claude-inloggegevens van de gebruiker doorsturen. Laat `ANTHROPIC_API_KEY` en `ANTHROPIC_AUTH_TOKEN` in dat geval oningesteld. Deze variabelen vervangen de abonnementsreferentie. Volg de actuele [Claude Code Aperture-instructies](https://tailscale.com/docs/aperture/how-to/use-claude-code) voor jouw Claude Code-versie en Anthropic's [gatewaygids](https://code.claude.com/docs/en/llm-gateway-connect) voor authenticatieopties.

**MCP via HTTP:** Voeg het endpoint toe met:

```sh
claude mcp add --transport http --scope user aperture http://<APERTURE_HOST>/v1/mcp
claude mcp list
```

**Claude Code controleren:** Start een sessie en voer `/mcp` uit om de verbinding te controleren. Anthropic raadt HTTP aan voor externe MCP-servers in de [MCP-documentatie](https://code.claude.com/docs/en/mcp).

## Claude Desktop-GUI

**Aparte instellingen:** Claude Desktop heeft een scherm voor inferentie via derden. Deze instelling leidt modelverzoeken van Claude Desktop via Aperture. MCP-configuratie is een aparte stap.

1. Kies in Claude Desktop voor macOS of Windows **Help > Problemen oplossen > Ontwikkelaarsmodus inschakelen**. Gebruik in de Linux-bèta hetzelfde menu als het beschikbaar is. Start de app opnieuw als daarom wordt gevraagd. Ontbreekt het menu, werk Claude Desktop dan bij en raadpleeg de releaseopmerkingen voor je platform.
2. Kies **Ontwikkelaar > Inferentie via derden configureren**.
3. Stel **Verbindingstype** in op **Gateway** en **Referentietype** op **Statische API-sleutel**.
4. Voer `https://<APERTURE_HOST>` in als **Basis-URL van de gateway**. Gebruik de volledige hostnaam die door een vertrouwd TLS-certificaat wordt gedekt.
5. Voer een niet-lege placeholder zoals `aperture` in als gatewaysleutel. Aperture negeert de placeholder en authenticeert via de tailnet.
6. Laat aangepaste inferentieheaders leeg.
7. Voeg een ingeschakeld model toe met een exacte ID die `GET /v1/models` voor je Tailscale-identiteit retourneert. Filter op een Anthropic Messages-model. Voer de model-ID, weergavenaam en optionele tier-alias handmatig in. Claude Desktop zoekt op dit scherm geen modellen op.
8. Kies **Wijzigingen opslaan** en daarna **Wijzigingen toepassen**. Sluit Claude Desktop af en open het opnieuw.

**Protocol controleren:** De [Aperture-gids voor Claude Desktop](https://tailscale.com/docs/aperture/how-to/use-claude-desktop) vermeldt dat Claude Desktop Anthropic Messages gebruikt via `/v1/messages`. Voer de Codex-route `/codex` niet in en kies geen OpenAI-compatibel verbindingstype.

### Claude Desktop met MCP verbinden

**Privé-MCP-toegang:** Voer een lokale stdio-bridge uit op dezelfde computer als Claude Desktop. Voeg dit toe aan de lokale MCP-configuratie van Claude Desktop:

```json
{
  "mcpServers": {
    "aperture": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "http://<APERTURE_HOST>/v1/mcp"]
    }
  }
}
```

**Werking van de bridge:** Het lokale proces bereikt Aperture via de Tailscale-verbinding van de computer. Gebruik het configuratiepad voor je besturingssysteem: macOS, `~/Library/Application Support/Claude/claude_desktop_config.json`; Windows, `%APPDATA%\Claude\claude_desktop_config.json`; Linux-bèta, open **Instellingen > Ontwikkelaar > Configuratie bewerken** en gebruik het pad dat Claude Desktop opent. Het Linux-pad kan per pakket verschillen. Start Claude Desktop opnieuw, controleer de connectorlijst en voer één onschadelijke toolaanroep uit. Het project [`mcp-remote`](https://github.com/punkpeye/mcp-remote) documenteert deze lokale-naar-externe bridge.

**Externe connectors:** De stroom Instellingen > Connectors van Anthropic vereist een externe server die de Anthropic-service kan bereiken. Een hostnaam die alleen binnen de tailnet werkt, is privé voor je apparaten. Gebruik dus de lokale bridge voor het privé-endpoint. Stel authenticatie en machtigingen in voordat je een publieke MCP-service als cloudconnector toevoegt. Zie Anthropic's [gids voor externe MCP-connectors](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp).

## OpenCode CLI en desktop

**Gedeelde instellingen:** OpenCode CLI en desktop lezen dezelfde OpenCode-configuratie. De huidige OpenCode V2-documentatie gebruikt de map `providers` voor aangepaste providers en zet MCP-servers onder `mcp.servers`. Dit voorbeeld gebruikt het OpenAI-compatibele chatendpoint op `/v1`. Controleer of je Aperture-provider OpenAI Chat Completions ondersteunt voordat je deze modelroute gebruikt.

**Globale configuratie:** Bewerk op macOS en Linux `~/.config/opencode/opencode.json`. Gebruik op Windows `%USERPROFILE%\.config\opencode\opencode.json`. Voeg een OpenAI-compatibele provider toe en vervang `<MODEL_ID>` door de exacte Aperture-model-ID. OpenCode accepteert ook `opencode.jsonc` in dezelfde map voor opmerkingen. De [configuratiereferentie](https://opencode.ai/docs/config/) beschrijft de voorrang tussen globale en projectinstellingen.

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "model": "aperture/<MODEL_ID>",
  "providers": {
    "aperture": {
      "env": ["APERTURE_API_KEY"],
      "package": "@opencode/ai/providers/openai-compatible",
      "settings": {
        "baseURL": "http://<APERTURE_HOST>/v1"
      },
      "models": {
        "<MODEL_ID>": { "modelID": "<MODEL_ID>" }
      }
    }
  },
  "mcp": {
    "servers": {
      "aperture": {
        "type": "remote",
        "url": "http://<APERTURE_HOST>/v1/mcp",
        "oauth": false
      }
    }
  }
}
```

**Clientauthenticatie:** `oauth: false` slaat de standaard-OAuth-stroom van OpenCode over. Aperture herkent de aanroeper via Tailscale. OpenCode vereist ook een provider-authenticatievermelding, dus stel `APERTURE_API_KEY=-` in de lokale omgeving in. De desktopapp moet de variabele ook ontvangen. Neemt de app je shellomgeving niet over, voer dan `/connect` uit en typ `-` voor Aperture. Zet de upstreamprovidersleutel niet in dit bestand. De [providergids](https://opencode.ai/docs/providers/) en [MCP-gids](https://opencode.ai/docs/mcp-servers/) van OpenCode beschrijven de huidige indeling. Voer `opencode mcp list` uit om de server te controleren en gebruik `/mcps` in de app om de status te bekijken.

## Hermes CLI en desktop

**Gedeelde instellingen:** Hermes Agent bewaart benoemde providers en MCP-servers in `~/.hermes/config.yaml` op macOS en Linux. Native Windows-installaties gebruiken `%LOCALAPPDATA%\hermes\config.yaml`. Voer `hermes config path` uit om het actieve bestand te bevestigen. `HERMES_HOME` kan de standaardlocatie vervangen. Lokale Hermes Desktop gebruikt dezelfde Hermes-home en hetzelfde profiel als de CLI. Als Desktop verbinding maakt met een externe Hermes-gateway, stel Aperture dan in op de machine waar Hermes draait en controleer of de server de tailnet bereikt. Zie de [Hermes Desktop-gids](https://hermes-agent.nousresearch.com/docs/user-guide/desktop) voor lokale en externe installatie.

**Responses-provider:** Voeg een benoemde provider toe. De waarde `api` moet overeenkomen met het Responses-endpoint van je Aperture-instantie:

```yaml
providers:
  aperture:
    api: "http://<APERTURE_HOST>/v1"
    transport: codex_responses
    default_model: "<MODEL_ID>"
    # Voeg key_env alleen toe als je Aperture-instelling een clientsleutel vereist.
    # key_env: APERTURE_API_KEY

model:
  provider: "custom:aperture"
  default: "<MODEL_ID>"
```

**Protocol kiezen:** Stel voor OpenAI Chat Completions `transport: chat_completions` in. Kies voor Anthropic Messages `transport: anthropic_messages` en gebruik de Anthropic Messages-gateway-URL. De actuele [providergids](https://hermes-agent.nousresearch.com/docs/integrations/providers) beschrijft de velden `api`, `transport` en `default_model` voor benoemde Hermes-providers.

**MCP-configuratie:** Voeg Aperture MCP toe aan hetzelfde YAML-bestand:

```yaml
mcp_servers:
  aperture:
    url: "http://<APERTURE_HOST>/v1/mcp"
    enabled: true
```

**Hermes controleren:** Voer `hermes mcp` uit en inspecteer elke verbinding in de interactieve serverkiezer. Lokale Desktop gebruikt hetzelfde configuratieprofiel. Hermes documenteert [externe HTTP-MCP-servers](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) en de volledige [referentie voor MCP-configuratie](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference).

## Beide paden controleren

**Voer aparte controles uit** voor modelinferentie en MCP:

1. Controleer of het apparaat Tailscale-connectiviteit heeft en de gateway kan bereiken. Controleer voor Claude Desktop of de gateway een vertrouwd TLS-certificaat aanbiedt.
2. Stuur via elke ingestelde client een korte prompt. Controleer of een bijbehorend verzoek in de Aperture-sessielijst verschijnt.
3. Controleer of de gekozen model-ID hoort bij een model dat aan je Tailscale-identiteit is toegekend.
4. Open het MCP-statusscherm of de lijstopdracht van elke client. Controleer of de Aperture-server verbinding maakt en de verwachte tools toont.
5. Roep een alleen-lezen-tool aan. Vergelijk de geretourneerde inhoud met de upstreambron.
6. Bekijk de Aperture-logs als een model- of toolaanroep mislukt. Een opgeslagen configuratie bewijst niet dat een verzoek is geslaagd.

| Probleem | Controle |
|---|---|
| Modelverzoek retourneert 404 of 405 | Controleer of het clientendpoint de juiste route en het juiste protocol gebruikt. Gebruik `/codex` niet opnieuw voor Anthropic Messages of MCP. |
| Model niet beschikbaar | Vraag `/v1/models` op als de beoogde Tailscale-gebruiker. Controleer of de exacte ID verschijnt en het API-formaat bij de client past. Vraag een beheerder ontbrekende providers of grants te controleren. |
| Verzoek niet geautoriseerd | Controleer of de client een placeholder, bearer-token of doorgifte van een abonnement nodig heeft. Kopieer nooit een upstreamprovidersleutel naar een openbaar projectbestand. |
| MCP-server staat in de lijst, maar er verschijnen geen tools | Controleer `/v1/mcp`, de status van de connector, de connectorgrants en het netwerkpad van de client naar Aperture. |
| Claude Desktop kan geen verbinding maken met een privé-MCP-URL | Voer een lokale bridge zoals `mcp-remote` uit of gebruik een goedgekeurde publieke connector met passende authenticatie. |

## De configuratie op een ander apparaat herhalen

**Nieuw apparaat:** Installeer dezelfde client en verbind het apparaat eerst met de tailnet. Vraag `/v1/models` op vanaf het nieuwe apparaat om modellen te vinden die aan de Tailscale-identiteit zijn toegekend. Neem de configuratiestructuur over, maar bewaar aanmeldgegevens lokaal. Vervang `<APERTURE_HOST>`, `<MODEL_ID>` en `<UPSTREAM_MCP_ENDPOINT>` door waarden van de doelinstantie Aperture. Gebruik een apart endpoint voor elk API-protocol en configureer daarna het pad `/v1/mcp` voor toolverkeer. Controleer tot slot één modelverzoek en één MCP-toolaanroep.

**Meerdere gateways:** Gebruik een aparte configuratie voor elke Aperture-instantie. Een apparaat heeft een Responses-endpoint nodig voor Codex en Hermes, een Anthropic Messages-endpoint voor Claude en het MCP-aggregatie-endpoint voor tools. Bewaar API-aanmeldgegevens in de lokale geheimenopslag van elke client of in een omgevingsvariabele. Kopieer API-sleutels niet naar gedeelde bestanden zoals `config.toml`, `opencode.json`, `config.yaml` of een openbare repository.

## Herbruikbare Aperture-prompt

**Kopieer deze geanonimiseerde prompt** naar je codeerassistent. Vervang de placeholders door je gatewaygegevens. De assistent moet Aperture als jouw Tailscale-identiteit opvragen voordat er model-ID's worden gekozen.

```text
Configureer mijn bestaande Tailscale Aperture-gateway en de AI-clients die op dit apparaat zijn geïnstalleerd.

Clients binnen scope: Codex CLI en desktop, Claude Code, Claude Desktop, OpenCode CLI en desktop, Hermes CLI en desktop.

Stel eerst vast of dit apparaat macOS, Linux of Windows gebruikt, bepaal welke shell actief is (zoals zsh, bash of PowerShell) en gebruik overal de paden en opdrachtsyntaxis van dat platform. Controleer eerst de huidige gateway, Tailscale-verbinding, clientversies en bestaande clientinstellingen. Lees de actuele officiële documentatie. Behoud instellingen die niet met deze taak te maken hebben en maak van elk bestand een back-up voordat je het wijzigt. Raad geen hostnamen, model-ID's, API-routes of inloggegevens. Bewaar upstreamprovidersleutels in Aperture, niet in clientbestanden of deze repository.

Ontdek de modellen die vanaf dit Tailscale-apparaat beschikbaar zijn:
1. Vraag `http://<APERTURE_HOST>/v1/models` op als de Tailscale-identiteit van mijn clients. Gebruik de gedocumenteerde aangepaste URL voor de modellijst van deze gateway als die afwijkt.
2. Lees van elk model `id` en `metadata.provider.id`. Deze lijst toont modellen die aan mijn identiteit zijn toegekend. Vervang de lijst niet door die van een beheerder en verzin geen ID's.
3. Koppel API-compatibiliteit van elk model aan de juiste client. Codex gebruikt OpenAI Responses. Claude-clients gebruiken Anthropic Messages. OpenCode en Hermes hebben een ingestelde, compatibele provider en transport nodig.
4. Hergebruik waar mogelijk het bestaande standaardmodel van een client. Als een client een standaardmodel nodig heeft en ik geen voorkeur heb, toon dan compatibele modellen en vraag me te kiezen. Claude Desktop vereist handmatige invoer van de exacte model-ID.
5. Levert het endpoint geen geschikt model, controleer dan de provider- en grantinstellingen alleen als ik beheerderstoegang heb. Zo niet, vermeld dan welke modeltoegang een beheerder moet toevoegen. Geef jezelf geen toegang.

Zoek de Aperture-implementatie en de bron van de configuratie. Ga niet uit van een bestandspad en vervang niet de volledige configuratie. OpenAI Responses vereist `openai_responses`. Anthropic-clients vereisen `anthropic_messages`. MCP-connectors horen in de huidige configuratie `connectors.servers` en clients verbinden via `/v1/mcp`.

Maak voordat je een gedeelde gateway wijzigt een minimale diff voor providers, connectors en grants. Pas die alleen toe als ik beheerder ben en dit verzoek gatewaywijzigingen toestaat. Ontbreekt die bevoegdheid, meld dan de exacte wijzigingen voor de eigenaar van de instantie. Maak grants niet aan en verruim ze niet zonder expliciete toestemming van de eigenaar. Behoud alle bestaande gatewayinstellingen.

Configureer elke geïnstalleerde client met het huidige officiële formaat en de locatie voor het besturingssysteem:
- Codex CLI en desktop delen `~/.codex/config.toml` op macOS/Linux en `%USERPROFILE%\.codex\config.toml` op Windows. Stel de Aperture-provider, een compatibel model, `wire_api = "responses"` en MCP onder `mcp_servers` in.
- Claude Code gebruikt `ANTHROPIC_BASE_URL` en externe MCP via HTTP. Gebruik `~/.claude/settings.json` op macOS/Linux en `%USERPROFILE%\.claude\settings.json` op Windows.
- Claude Desktop gebruikt Ontwikkelaarsmodus, Inferentie via derden configureren, Gateway, Statische API-sleutel, een HTTPS-gateway-URL met een vertrouwd certificaat en een voor mijn gebruiker gevonden model-ID. Gebruik een lokale `mcp-remote`-bridge voor privé-MCP op de tailnet. Zoek de MCP-configuratie via Instellingen > Ontwikkelaar > Configuratie bewerken als dat beschikbaar is. Gebruik anders het gedocumenteerde pad voor het vastgestelde besturingssysteem.
- OpenCode gebruikt het huidige V2-schema `providers` en `mcp.servers`. De globale configuratie staat op `~/.config/opencode/opencode.json` op macOS/Linux en `%USERPROFILE%\.config\opencode\opencode.json` op Windows. Stel `oauth: false` in voor Aperture-MCP. Gebruik waar nodig lokaal een tijdelijke API-sleutel.
- Hermes gebruikt een benoemde provider, een transport dat bij de model-API past en `mcp_servers`. Gebruik `~/.hermes/config.yaml` op macOS/Linux. Controleer op Windows `hermes config path`, meestal `%LOCALAPPDATA%\hermes\config.yaml`. Controleer of Hermes Desktop het lokale Hermes-profiel deelt.

Gebruik HTTP voor tailnetverkeer als de client dat ondersteunt. Claude Desktop-inferentie vereist HTTPS met een vertrouwd certificaat. Gebruik `/v1`, tenzij deze gateway een andere route documenteert.

Start ingestelde clients opnieuw. Controleer in Aperture één modelverzoek per client en één onschadelijke, alleen-lezen-MCP-toolaanroep. Rapporteer modellen voor mijn identiteit, gewijzigde clients en bestanden, verificatieresultaten en eventuele resterende beheerderactie. Installeer geen software, maak de gateway niet openbaar, commit niets en publiceer niets.
```

## Conclusie

Een werkende Aperture-instelling vereist drie zaken: een bereikbare gateway, een modelroute die bij het clientprotocol past en grants voor de benodigde modellen en MCP-connectors. Dezelfde configuratiepatronen werken op macOS, Linux en Windows, maar elke client slaat instellingen op een eigen, systeemspecifieke plek op.

Vraag model-ID's op als de Tailscale-identiteit die ze gaat gebruiken. Configureer modelinferentie en `/v1/mcp` apart en controleer daarna één echt verzoek en één alleen-lezen-toolaanroep. Gebruik bij overstappen naar een ander apparaat of een andere Aperture-instantie de structuur uit deze gids, controleer de routes en grants van die instantie en bewaar inloggegevens in de lokale geheimenopslag.

## Volgende stappen

**MCP oefenen:** Lees [MCP-server instellen: machtigingen, tooltests en veilig verwijderen](/articles/effective-ai-mcp-server-setup/) voor het verschil tussen een opgeslagen server en een geverifieerde toolaanroep. Bekijk voor de bredere zelfgehoste architectuur [Hybride AI-agentenfleet: Tailscale, LiteLLM en Hermes](/articles/hybrid-agentic-ai-fleet-tailscale-litellm-hermes/).
