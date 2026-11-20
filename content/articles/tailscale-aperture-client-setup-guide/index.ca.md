---
title: "Tailscale Aperture: configura clients d'IA per a inferència i MCP el 2026"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Encamina les sol·licituds dels models i les eines MCP a través de Tailscale Aperture. Configura Codex, Claude Code, Claude Desktop, OpenCode i Hermes en un altre dispositiu o passarel·la."
genre: ["Intel·ligència artificial", "Eines per a desenvolupadors", "Xarxes"]
tags: ["Tailscale Aperture", "Configuració d'Aperture", "Proxy d'IA", "Passarel·la LLM", "Passarel·la MCP", "Codex Aperture", "Claude Code Aperture", "Claude Desktop Aperture", "OpenCode Aperture", "Hermes Agent Aperture", "Codex MCP", "Claude MCP", "OpenCode MCP", "Hermes MCP", "Proxy d'inferència d'IA", "API Responses", "API Anthropic Messages", "MCP remot", "HTTP Streamable", "Tailscale", "IA allotjada localment", "Agents de programació", "Configuració de clients d'IA"]
cover: "/img/cover/tailscale-aperture-agent-setup.webp"
coverAlt: "Aperture connecta els panells dels clients amb serveis de models i eines MCP mitjançant rutes separades, blava per a la inferència i verda per a les eines"
coverCaption: ""
---

## Introducció

Tailscale Aperture proporciona als clients d'IA una passarel·la connectada a la tailnet per a la inferència de models i les eines del Model Context Protocol (MCP). Cada client ha d'utilitzar una ruta que coincideixi amb el seu protocol d'API. Les eines MCP fan servir un endpoint separat, i les concessions d'Aperture controlen quins models i connectors pot utilitzar cada identitat de Tailscale.

Aquesta guia explica com configurar Codex, Claude Code, Claude Desktop, OpenCode i Hermes a macOS, Linux i Windows. Inclou la configuració de línia d'ordres i d'escriptori, mostra com consultar els identificadors dels models disponibles per a la teva identitat i incorpora una instrucció anonimitzada que pots reutilitzar per configurar un altre dispositiu o una altra instància d'Aperture.

**Tria de la ruta:** Els camins dels endpoints depenen de la passarel·la i de cada protocol d'API. Una ruta Responses com ara `/codex` no serveix el trànsit d'Anthropic Messages ni de MCP. Confirma el nom d'amfitrió de la passarel·la i la ruta d'inferència de cada client. Consulta els identificadors dels models amb el teu accés propi a Aperture abans de modificar la configuració dels clients.

## Punts clau

- **El trànsit de models** necessita la ruta d'API del protocol del client.
- **El trànsit MCP** utilitza l'endpoint separat `/v1/mcp`.
- **Els permisos de la passarel·la** han de permetre que la teva identitat de Tailscale utilitzi cada model i connector.
- **La configuració del client** només prova que s'han desat els ajustos. Comprova una sol·licitud real i una crida a una eina MCP.

## Com encaixen les rutes

| Finalitat | Sol·licitud del client | Ruta d'Aperture | Servei de la ruta |
|---|---|---|---|
| Codex i models compatibles amb Responses | API OpenAI Responses | Normalment `/v1`. Un camí personalitzat com `/codex` depèn del desplegament. | Inferència de models |
| Inferència de models Claude | API Anthropic Messages | URL base de la passarel·la. Aperture gestiona `/v1/messages` | Inferència compatible amb Claude |
| Eines MCP | MCP HTTP Streamable | `/v1/mcp` | Eines i recursos dels connectors configurats |

{{< figure src="aperture-client-routes.webp" alt="Codex i Hermes utilitzen una ruta Responses, Claude utilitza Anthropic Messages i els clients MCP utilitzen la ruta separada /v1/mcp per arribar als connectors d'Aperture" caption="La inferència de models i el trànsit MCP utilitzen endpoints d'Aperture separats" >}}

**Arrels dels proveïdors:** Aperture afegeix els camins de les sol·licituds del client a l'URL base del proveïdor. Defineix `baseurl` del proveïdor com l'arrel de la seva API. No afegeixis `/v1` a una URL base ascendent quan el camí d'entrada ja inclou `/v1`. Consulta la [referència de configuració d'Aperture](https://tailscale.com/docs/aperture/configuration) per veure la construcció d'URL, el registre de models i les concessions.

## Prepara la passarel·la

**Abans d'editar**, demana aquests valors a un administrador d'Aperture:

- **Nom d'amfitrió de la passarel·la:** Utilitza `http://` amb la majoria de clients connectats a la tailnet. La inferència de Claude Desktop exigeix `https://` amb un certificat de confiança.
- **Rutes d'inferència:** OpenAI Responses i Anthropic Messages utilitzen formats de sol·licitud diferents.
- **Identificadors de models:** Consulta els models disponibles per a la teva identitat de Tailscale amb l'endpoint següent. Utilitza els identificadors literals retornats per a aquella identitat.
- **Autenticació:** Comprova si el client envia una clau API de substitució o unes credencials d'usuari.
- **Endpoint MCP:** Normalment `http://<APERTURE_HOST>/v1/mcp` per als clients de la tailnet. La inferència de Claude Desktop exigeix HTTPS amb un certificat de confiança.
- **Concessions d'accés:** Comprova els permisos de models i connectors de la teva identitat de Tailscale.

**Accés a la xarxa:** El dispositiu client ha d'arribar a la passarel·la a través de la tailnet. Un nom d'amfitrió no concedeix per si sol accés a models ni eines. Aperture denega l'accés si no hi ha cap concessió coincident per al model o el connector.

### Troba els models disponibles per al teu usuari

**Consulta la llista de models** des d'un dispositiu connectat a la mateixa tailnet. Aperture utilitza la identitat de Tailscale del dispositiu i retorna els models concedits a l'usuari, tal com s'explica a la [guia de concessions de models](https://tailscale.com/docs/aperture/how-to/grant-model-access):

```sh
# macOS o Linux
curl -fsS http://<APERTURE_HOST>/v1/models
```

```powershell
# Windows PowerShell, utilitza curl.exe per evitar l'àlies antic curl
curl.exe -fsS http://<APERTURE_HOST>/v1/models
```

**Llegeix el resultat:** Utilitza cada `id` retornat com a identificador del model. Comprova `metadata.provider.id` per identificar el proveïdor d'Aperture. Tria un model que admeti el format d'API del client. Per exemple, Claude Desktop necessita un model Anthropic Messages. El [directori de models](https://tailscale.com/docs/aperture/reference/chat) d'Aperture també enumera els identificadors disponibles per a l'usuari autenticat.

**Falten models:** Si no apareix un model esperat, demana a un administrador d'Aperture que revisi la configuració del proveïdor i la teva concessió de model. L'endpoint no permet que els usuaris es concedeixin accés a si mateixos.

**Esquema de la URL:** Tailscale recomana `http://` per a la majoria de clients connectats a la mateixa tailnet. WireGuard xifra aquest trànsit. Claude Desktop exigeix `https://` i un certificat de confiança per al sistema operatiu. Utilitza l'esquema indicat per a cada client més avall.

### Afegeix un proveïdor d'inferència

**OpenAI Responses:** Afegeix el proveïdor ascendent a Aperture i activa el format d'API que utilitza el client. Per a un proveïdor OpenAI, afegeix un fragment com aquest:

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

**Anthropic Messages:** Utilitza l'arrel de l'API d'Anthropic, el format d'autorització `x-api-key` i la compatibilitat `anthropic_messages`. L'identificador del model també ha d'aparèixer a la llista `models` del proveïdor. Afegeix un fragment com aquest:

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

**Canvis de configuració:** Substitueix cada marcador per les dades del proveïdor ascendent. Afegeix els fragments a la configuració d'Aperture existent. Conserva la resta del fitxer actual. Activa els indicadors de compatibilitat per a les API que admeti el proveïdor.

**Concessions d'accés:** Aperture controla l'accés de cada usuari a cada model o connector. Concedeix a cada usuari de Tailscale previst només els permisos necessaris. Aquest exemple dona a un usuari accés a un model d'un proveïdor i a un connector:

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

**Concessió de model:** Utilitza l'identificador del proveïdor i del model al patró de concessió. La [guia de configuració de connectors](https://tailscale.com/docs/aperture/connectors/get-started) mostra la configuració actual `connectors.servers`. La configuració antiga de primer nivell `mcp.servers` està obsoleta.

### Afegeix un connector MCP

**Connector MCP:** Aperture es connecta a servidors MCP ascendents i exposa les eines a `/v1/mcp`:

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

**URL del connector:** Utilitza l'endpoint MCP complet del servidor ascendent. Després concedeix al teu usuari de Tailscale accés a `teamtools/**` o a un patró d'eines més limitat. La [referència del proxy MCP](https://tailscale.com/docs/aperture/mcp-server) explica l'endpoint únic del client i el comportament dels connectors.

## Codex CLI i escriptori

**Configuració compartida:** Codex CLI i l'aplicació d'escriptori utilitzen la mateixa configuració. A macOS i Linux, edita `~/.codex/config.toml`. A Windows, edita `%USERPROFILE%\.codex\config.toml` (els intèrprets que amplien el directori personal també admeten `~/.codex/config.toml`). La [presentació de l'aplicació Codex](https://openai.com/index/introducing-the-codex-app/) diu que l'aplicació d'escriptori adopta la configuració de Codex CLI. Els ajustos d'usuari de Codex són a `~/.codex/config.toml`. La documentació de [configuració bàsica](https://learn.chatgpt.com/docs/config-file/config-basic) descriu els camps de proveïdor i MCP d'usuari. Afegeix el proveïdor a aquest fitxer, reinicia l'aplicació i confirma que el proveïdor i el model apareixen a la interfície.

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

**Camps opcionals:** Aquests dos valors coincideixen amb una configuració de proveïdor Codex. Conserva'ls només si els exigeixen la passarel·la i la configuració de Codex. La [guia actual de Tailscale per a Codex Aperture](https://tailscale.com/docs/aperture/how-to/use-codex) els omet, utilitza `wire_api = "responses"` i diu que Aperture injecta les credencials ascendents. Utilitza l'URL Responses exacte de l'administrador de la passarel·la. `/codex` és una ruta específica del desplegament. La ruta predeterminada documentada per Tailscale és `/v1`.

**Configuració MCP:** Afegeix el servidor a la mateixa configuració d'usuari:

```toml
[mcp_servers.aperture]
url = "http://<APERTURE_HOST>/v1/mcp"
enabled = true
```

**Verifica Codex:** Executa `codex mcp list`, inicia una sessió nova i inspecciona `/mcp`. La llista de servidors confirma el registre. Una eina que hi apareix i una crida correcta confirmen la detecció i l'execució. La [referència de configuració de Codex](https://learn.chatgpt.com/docs/config-file/config-reference) documenta els ajustos d'usuari per als proveïdors i MCP.

## Claude Code CLI

**Protocol:** Claude Code utilitza Anthropic Messages. Apunta el fitxer global d'ajustos de Claude Code a la passarel·la d'Aperture compatible amb Anthropic. Utilitza `~/.claude/settings.json` a macOS i Linux, o `%USERPROFILE%\.claude\settings.json` a Windows. A PowerShell, utilitza el camí equivalent `$HOME\.claude\settings.json`. La ruta ha de servir `/v1/messages`. Codex Responses utilitza un protocol i una ruta diferents. Tailscale recomana HTTP per a Claude Code a la tailnet perquè WireGuard xifra la connexió.

```json
{
  "apiKeyHelper": "echo '-'",
  "env": {
    "ANTHROPIC_BASE_URL": "http://<APERTURE_HOST>"
  }
}
```

**Autenticació del client:** La guia de client d'Aperture utilitza un marcador a `apiKeyHelper`, perquè Aperture injecta la credencial ascendent. Per transferir una subscripció de Claude, el proveïdor Anthropic d'Aperture ha de reenviar la credencial Claude de l'usuari. En aquest cas, deixa `ANTHROPIC_API_KEY` i `ANTHROPIC_AUTH_TOKEN` sense definir. Aquestes variables substitueixen la credencial de subscripció. Segueix les instruccions actuals de [Claude Code amb Aperture](https://tailscale.com/docs/aperture/how-to/use-claude-code) per a la teva versió de Claude Code i la [guia de passarel·les d'Anthropic](https://code.claude.com/docs/en/llm-gateway-connect) per a les opcions d'autenticació.

**MCP per HTTP:** Afegeix l'endpoint amb aquestes ordres:

```sh
claude mcp add --transport http --scope user aperture http://<APERTURE_HOST>/v1/mcp
claude mcp list
```

**Verifica Claude Code:** Inicia una sessió i executa `/mcp` per confirmar la connexió. Anthropic recomana HTTP per als servidors MCP remots a la seva [documentació de MCP](https://code.claude.com/docs/en/mcp).

## Interfície gràfica de Claude Desktop

**Ajustos separats:** Claude Desktop disposa d'una pantalla d'inferència de tercers. Aquest ajust encamina les sol·licituds de models de Claude Desktop a través d'Aperture. La configuració MCP és un pas separat.

1. A Claude Desktop per a macOS o Windows, selecciona **Ajuda > Resolució de problemes > Activa el mode de desenvolupador**. A la beta de Linux, utilitza el mateix menú si hi és. Reinicia l'aplicació si t'ho demana. Si no hi ha el menú, actualitza Claude Desktop i consulta les notes de versió de la plataforma.
2. Selecciona **Desenvolupador > Configura la inferència de tercers**.
3. Defineix **Tipus de connexió** com a **Passarel·la** i **Tipus de credencial** com a **Clau API estàtica**.
4. Introdueix `https://<APERTURE_HOST>` com a **URL base de la passarel·la**. Utilitza el nom d'amfitrió complet cobert per un certificat TLS de confiança.
5. Introdueix una clau de substitució no buida, com ara `aperture`. Aperture ignora el marcador i s'autentica a través de la tailnet.
6. Deixa buits els encapçalaments d'inferència personalitzats.
7. Afegeix un model activat amb un identificador exacte retornat per `GET /v1/models` per a la teva identitat de Tailscale. Filtra els models Anthropic Messages. Introdueix manualment l'identificador, el nom visible i un àlies de nivell opcional. Claude Desktop no detecta models en aquesta pantalla.
8. Selecciona **Desa els canvis** i després **Aplica els canvis**. Tanca Claude Desktop i torna'l a obrir.

**Comprovació del protocol:** La [guia d'Aperture per a Claude Desktop](https://tailscale.com/docs/aperture/how-to/use-claude-desktop) diu que Claude Desktop utilitza Anthropic Messages a `/v1/messages`. No introdueixis la ruta Codex `/codex` ni triïs un tipus de connexió compatible amb OpenAI.

### Connecta Claude Desktop a MCP

**Accés MCP privat:** Executa un pont local de tipus stdio al mateix ordinador que Claude Desktop. Afegeix això a la configuració MCP local de Claude Desktop:

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

**Funcionament del pont:** El procés local arriba a Aperture per la connexió de Tailscale de l'ordinador. Utilitza el camí de configuració del teu sistema operatiu: macOS, `~/Library/Application Support/Claude/claude_desktop_config.json`; Windows, `%APPDATA%\Claude\claude_desktop_config.json`; beta de Linux, obre **Configuració > Desenvolupador > Edita la configuració** i utilitza el camí que obre Claude Desktop. El camí de Linux varia segons el paquet. Reinicia Claude Desktop, inspecciona la llista de connectors i fes una crida inofensiva a una eina. El [projecte `mcp-remote`](https://github.com/punkpeye/mcp-remote) documenta aquest pont local-remot.

**Connectors remots:** El flux Configuració > Connectors d'Anthropic necessita un servidor remot accessible pel servei d'Anthropic. Un nom d'amfitrió només disponible a la tailnet és privat per als teus dispositius, així que utilitza el pont local per a l'endpoint privat. Si publiques un servei MCP, configura'n l'autenticació i els permisos abans d'afegir-lo com a connector al núvol. Consulta la [guia de connectors MCP remots](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) d'Anthropic.

## OpenCode CLI i escriptori

**Ajustos compartits:** OpenCode CLI i l'escriptori llegeixen la mateixa configuració d'OpenCode. La documentació actual d'OpenCode V2 utilitza el mapa `providers` per als proveïdors personalitzats i agrupa els servidors MCP a `mcp.servers`. Aquest exemple utilitza l'endpoint de xat compatible amb OpenAI a `/v1`. Comprova que el proveïdor d'Aperture admeti OpenAI Chat Completions abans d'utilitzar aquesta ruta de model.

**Configuració global:** A macOS i Linux, edita `~/.config/opencode/opencode.json`. A Windows, utilitza `%USERPROFILE%\.config\opencode\opencode.json`. Afegeix un proveïdor compatible amb OpenAI i substitueix `<MODEL_ID>` per l'identificador exacte del model d'Aperture. OpenCode també accepta `opencode.jsonc` al mateix directori per incloure comentaris. La [referència de configuració](https://opencode.ai/docs/config/) explica la prioritat entre la configuració global i la del projecte.

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

**Autenticació del client:** `oauth: false` omet el flux OAuth predeterminat d'OpenCode. Aperture identifica qui fa la crida mitjançant Tailscale. OpenCode també necessita una entrada d'autenticació del proveïdor, així que defineix `APERTURE_API_KEY=-` a l'entorn local. L'aplicació d'escriptori també ha de rebre la variable. Si no hereta l'entorn del shell, executa `/connect` a l'aplicació i introdueix `-` per a Aperture. No desis la clau del proveïdor ascendent en aquest fitxer. La [guia de proveïdors](https://opencode.ai/docs/providers/) i la [guia MCP](https://opencode.ai/docs/mcp-servers/) d'OpenCode expliquen el format actual. Executa `opencode mcp list` per comprovar el servidor i utilitza `/mcps` a l'aplicació per veure'n l'estat.

## Hermes CLI i escriptori

**Ajustos compartits:** Hermes Agent desa els proveïdors amb nom i els servidors MCP a `~/.hermes/config.yaml` a macOS i Linux. Les instal·lacions natives de Windows utilitzen `%LOCALAPPDATA%\hermes\config.yaml`. Executa `hermes config path` per confirmar el fitxer actiu al teu sistema. `HERMES_HOME` pot canviar la ubicació predeterminada. Hermes Desktop local comparteix el directori i el perfil d'Hermes amb la CLI. Si Desktop es connecta a una passarel·la Hermes remota, configura Aperture a l'ordinador on s'executa Hermes i confirma que el servidor arriba a la tailnet. Consulta la [guia Hermes Desktop](https://hermes-agent.nousresearch.com/docs/user-guide/desktop) per a la configuració local i remota.

**Proveïdor Responses:** Afegeix un proveïdor amb nom. El valor `api` ha de coincidir amb l'endpoint Responses de la teva instància d'Aperture:

```yaml
providers:
  aperture:
    api: "http://<APERTURE_HOST>/v1"
    transport: codex_responses
    default_model: "<MODEL_ID>"
    # Afegeix key_env només si la configuració d'Aperture exigeix una clau de client.
    # key_env: APERTURE_API_KEY

model:
  provider: "custom:aperture"
  default: "<MODEL_ID>"
```

**Tria del protocol:** Per a OpenAI Chat Completions, defineix `transport: chat_completions`. Per a Anthropic Messages, tria `transport: anthropic_messages` i utilitza l'URL de passarel·la d'Anthropic Messages. La [guia actual de proveïdors](https://hermes-agent.nousresearch.com/docs/integrations/providers) documenta els camps `api`, `transport` i `default_model` dels proveïdors amb nom d'Hermes.

**Configuració MCP:** Afegeix Aperture MCP al mateix fitxer YAML:

```yaml
mcp_servers:
  aperture:
    url: "http://<APERTURE_HOST>/v1/mcp"
    enabled: true
```

**Verifica Hermes:** Executa `hermes mcp` i inspecciona cada connexió al selector interactiu de servidors. Desktop local exposa el mateix perfil de configuració. Hermes documenta els [servidors MCP HTTP remots](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) i la [referència completa de configuració MCP](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference).

## Verifica les dues rutes

**Fes comprovacions separades** per a la inferència de models i MCP:

1. Confirma que el dispositiu té connectivitat Tailscale i arriba a la passarel·la. Per a Claude Desktop, confirma que la passarel·la presenta un certificat TLS de confiança.
2. Envia una instrucció breu des de cada client configurat. Confirma que apareix una sol·licitud coincident a la llista de sessions d'Aperture.
3. Confirma que l'identificador del model triat coincideix amb un model concedit a la teva identitat de Tailscale.
4. Obre la pantalla d'estat MCP de cada client o executa l'ordre de llista. Confirma que el servidor d'Aperture es connecta i exposa les eines previstes.
5. Crida una eina de només lectura. Compara el contingut retornat amb la font ascendent.
6. Revisa els registres d'Aperture si falla la crida al model o a l'eina. Una configuració desada no prova que la sol·licitud s'hagi completat.

| Símptoma | Comprovació |
|---|---|
| La sol·licitud del model retorna 404 o 405 | Confirma que l'endpoint del client utilitza la ruta i el protocol correctes. No reutilitzis `/codex` per a Anthropic Messages o MCP. |
| El model no està disponible | Consulta `/v1/models` com l'usuari de Tailscale previst. Comprova que aparegui l'identificador exacte i que el format d'API coincideixi amb el client. Demana a un administrador que revisi els proveïdors o les concessions que faltin. |
| Sol·licitud no autoritzada | Comprova si el client necessita un marcador, un token bearer o el traspàs d'una subscripció. No copiïs mai una clau de proveïdor ascendent en un fitxer públic del projecte. |
| El servidor MCP apareix, però no hi ha eines | Comprova `/v1/mcp`, l'estat del connector, les concessions del connector i la ruta de xarxa del client fins a Aperture. |
| Claude Desktop no es pot connectar a una URL MCP privada | Executa un pont local com `mcp-remote` o utilitza un connector públic aprovat amb autenticació adequada. |

## Repeteix la configuració en un altre dispositiu

**Dispositiu nou:** Instal·la el mateix client i connecta primer el dispositiu a la tailnet. Consulta `/v1/models` des del dispositiu nou per trobar els models concedits a la seva identitat de Tailscale. Copia l'estructura de configuració i conserva les credencials localment. Substitueix `<APERTURE_HOST>`, `<MODEL_ID>` i `<UPSTREAM_MCP_ENDPOINT>` pels valors de la instància d'Aperture de destinació. Mantén un endpoint separat per a cada protocol d'API i configura després el camí `/v1/mcp` per al trànsit d'eines. Finalment, comprova una sol·licitud de model i una crida a una eina MCP.

**Diverses passarel·les:** Utilitza una configuració separada per a cada instància d'Aperture. Un dispositiu necessita un endpoint Responses per a Codex i Hermes, un endpoint Anthropic Messages per a Claude i l'endpoint d'agregació MCP per a les eines. Desa les credencials API al magatzem local de secrets de cada client o en una variable d'entorn. No copiïs les claus API a fitxers compartits `config.toml`, `opencode.json`, `config.yaml` ni a un repositori públic.

## Instrucció reutilitzable per configurar Aperture

**Copia aquesta instrucció anonimitzada** al teu assistent de programació. Substitueix els marcadors per les dades de la passarel·la. L'assistent ha de consultar Aperture amb la teva identitat de Tailscale abans de triar identificadors de models.

```text
Configura la meva passarel·la Tailscale Aperture existent i els clients d'IA instal·lats en aquest dispositiu.

Clients inclosos: Codex CLI i escriptori, Claude Code, Claude Desktop, OpenCode CLI i escriptori, Hermes CLI i escriptori.

Primer detecta si aquest dispositiu executa macOS, Linux o Windows, identifica l'intèrpret d'ordres actiu (per exemple, zsh, bash o PowerShell) i utilitza sempre les rutes i la sintaxi de comandes d'aquesta plataforma. Inspecciona primer la passarel·la actual, la connexió Tailscale, les versions dels clients i la configuració existent. Llegeix la documentació oficial actual. Conserva la configuració no relacionada i fes una còpia de seguretat de cada fitxer abans de modificar-lo. No endevinis noms d'amfitrió, identificadors de models, rutes d'API ni credencials. Mantén les claus dels proveïdors ascendents a Aperture, no als fitxers dels clients ni en aquest repositori.

Descobreix els models disponibles des d'aquest dispositiu connectat a Tailscale:
1. Consulta `http://<APERTURE_HOST>/v1/models` amb la identitat de Tailscale dels meus clients. Si és diferent, utilitza l'URL personalitzat documentat per a la llista de models de la passarel·la.
2. Llegeix `id` i `metadata.provider.id` de cada model. Aquesta llista reflecteix els models concedits a la meva identitat. No la substitueixis per la llista de l'administrador ni inventis identificadors.
3. Relaciona la compatibilitat d'API de cada model amb cada client. Codex utilitza OpenAI Responses. Els clients Claude utilitzen Anthropic Messages. OpenCode i Hermes necessiten un proveïdor i un transport compatibles configurats.
4. Reutilitza el model predeterminat existent d'un client quan sigui possible. Si un client en necessita un i no tinc cap preferència, mostra'm els models compatibles i demana'm que triï. Claude Desktop exigeix introduir manualment l'identificador exacte del model.
5. Si l'endpoint no retorna cap model adequat, comprova la configuració del proveïdor i les concessions només si tinc accés d'administrador. En cas contrari, indica quin accés al model ha d'afegir un administrador. No et concedeixis accés.

Localitza el desplegament d'Aperture i la font de la seva configuració. No pressuposis una ruta de fitxer ni substitueixis tota la configuració. OpenAI Responses requereix `openai_responses`. Els clients Anthropic requereixen `anthropic_messages`. Els connectors MCP han d'anar a la configuració actual `connectors.servers`, i els clients es connecten mitjançant `/v1/mcp`.

Abans de modificar una passarel·la compartida, prepara el diff mínim de proveïdors, connectors i concessions. Aplica'l només si tinc autoritat d'administrador i aquesta sol·licitud autoritza els canvis a la passarel·la. Si no tinc aquesta autoritat, informa de les modificacions exactes proposades al propietari de la instància. No creïs ni ampliïs concessions sense l'autorització explícita del propietari. Conserva tota la configuració existent de la passarel·la.

Configura cada client instal·lat amb el format oficial actual i la ubicació específica del sistema operatiu:
- Codex CLI i escriptori comparteixen `~/.codex/config.toml` a macOS/Linux i `%USERPROFILE%\.codex\config.toml` a Windows. Defineix el proveïdor Aperture, un model compatible, `wire_api = "responses"` i MCP a `mcp_servers`.
- Claude Code utilitza `ANTHROPIC_BASE_URL` i MCP remot per HTTP. Utilitza `~/.claude/settings.json` a macOS/Linux i `%USERPROFILE%\.claude\settings.json` a Windows.
- Claude Desktop utilitza el mode de desenvolupador, Configura la inferència de tercers, Passarel·la, Clau API estàtica, una URL HTTPS de passarel·la amb certificat de confiança i un identificador de model consultat per al meu usuari. Utilitza un pont local `mcp-remote` per a MCP privat de la tailnet. Busca la configuració MCP a Configuració > Desenvolupador > Edita la configuració si està disponible. Si no, utilitza el camí documentat per al sistema detectat.
- OpenCode utilitza l'esquema V2 actual `providers` i `mcp.servers`. La configuració global és a `~/.config/opencode/opencode.json` a macOS/Linux i `%USERPROFILE%\.config\opencode\opencode.json` a Windows. Defineix `oauth: false` per a l'MCP d'Aperture. Si cal, utilitza una clau API de substitució local.
- Hermes utilitza un proveïdor amb nom, un transport que coincideixi amb l'API del model i `mcp_servers`. Utilitza `~/.hermes/config.yaml` a macOS/Linux. A Windows, comprova `hermes config path`, habitualment `%LOCALAPPDATA%\hermes\config.yaml`. Comprova si Hermes Desktop comparteix el perfil local d'Hermes.

Utilitza HTTP per al trànsit de la tailnet quan el client ho admeti. La inferència de Claude Desktop exigeix HTTPS amb un certificat de confiança. Utilitza `/v1` tret que aquesta passarel·la documenti una altra ruta.

Reinicia els clients configurats. Verifica a Aperture una sol·licitud de model per client i una crida MCP inofensiva i de només lectura. Informa dels models consultats per a la meva identitat, els clients i fitxers modificats, els resultats de verificació i qualsevol acció d'administrador pendent. No instal·lis programari, no exposis la passarel·la públicament, no facis commits ni publiquis.
```

## Conclusió

Una configuració funcional d'Aperture depèn de tres elements: una passarel·la accessible, una ruta de model que coincideixi amb el protocol del client i concessions per als models i connectors MCP necessaris. Els mateixos patrons funcionen a macOS, Linux i Windows, però cada client desa la configuració en una ubicació pròpia del sistema operatiu.

Consulta els identificadors dels models com la identitat de Tailscale que els utilitzarà. Configura la inferència de models i `/v1/mcp` per separat, i després verifica una sol·licitud real i una crida a una eina de només lectura. En passar a un altre dispositiu o instància d'Aperture, reutilitza l'estructura d'aquesta guia, confirma les rutes i les concessions d'aquella instància i conserva les credencials al magatzem local de secrets.

## Passos següents

**Pràctica amb MCP:** Per veure la diferència entre un servidor desat i una crida verificada a una eina, llegeix [Configuració de servidor MCP: permisos, proves d'eines i eliminació segura](/articles/effective-ai-mcp-server-setup/). Per a l'arquitectura autoallotjada més àmplia, consulta [Flota híbrida d'agents d'IA: Tailscale, LiteLLM i Hermes](/articles/hybrid-agentic-ai-fleet-tailscale-litellm-hermes/).
