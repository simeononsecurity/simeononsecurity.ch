---
title: "Tailscale Aperture: configurează clienții AI pentru inferență și MCP în 2026"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Direcționează cererile modelelor și instrumentele MCP prin Tailscale Aperture. Configurează Codex, Claude Code, Claude Desktop, OpenCode și Hermes pe alt dispozitiv sau gateway."
genre: ["Inteligență artificială", "Instrumente pentru dezvoltatori", "Rețele"]
tags: ["Tailscale Aperture", "Configurare Aperture", "Proxy AI", "Gateway LLM", "Gateway MCP", "Codex Aperture", "Claude Code Aperture", "Claude Desktop Aperture", "OpenCode Aperture", "Hermes Agent Aperture", "Codex MCP", "Claude MCP", "OpenCode MCP", "Hermes MCP", "Proxy de inferență AI", "API Responses", "API Anthropic Messages", "MCP la distanță", "HTTP Streamable", "Tailscale", "AI găzduit local", "Agenți de programare", "Configurarea clienților AI"]
cover: "/img/cover/tailscale-aperture-agent-setup.webp"
coverAlt: "Aperture conectează panourile clienților la servicii de modele și instrumente MCP prin rute separate, albastră pentru inferență și verde pentru instrumente"
coverCaption: ""
---

## Introducere

Tailscale Aperture oferă clienților AI un gateway conectat la tailnet pentru inferența modelelor și instrumentele Model Context Protocol (MCP). Fiecare client trebuie să folosească o rută potrivită protocolului său API. Instrumentele MCP folosesc un endpoint separat, iar granturile Aperture controlează modelele și conectorii pe care îi poate accesa fiecare identitate Tailscale.

Acest ghid explică configurarea Codex, Claude Code, Claude Desktop, OpenCode și Hermes pe macOS, Linux și Windows. Acoperă setările CLI și desktop, arată cum să găsești ID-urile modelelor disponibile pentru identitatea ta și include un prompt anonimizat pe care îl poți reutiliza când configurezi alt dispozitiv sau altă instanță Aperture.

**Alegerea rutei:** Căile endpointurilor depind de gateway și de fiecare protocol API. O rută Responses precum `/codex` nu deservește traficul Anthropic Messages sau MCP. Confirmă numele gazdei gatewayului și ruta de inferență a fiecărui client. Găsește ID-urile modelelor prin propriul acces Aperture înainte să modifici setările clientului.

## Idei principale

- **Traficul modelelor** are nevoie de ruta API potrivită protocolului clientului.
- **Traficul MCP** folosește endpointul separat `/v1/mcp`.
- **Permisiunile gatewayului** trebuie să permită identității tale Tailscale să folosească fiecare model și conector.
- **Configurarea clientului** dovedește doar că setările au fost salvate. Verifică o cerere reală și un apel către un instrument MCP.

## Cum se potrivesc rutele

| Scop | Cererea clientului | Ruta Aperture | Serviciul oferit de rută |
|---|---|---|---|
| Codex și modele compatibile Responses | API OpenAI Responses | De obicei `/v1`. O cale personalizată precum `/codex` depinde de implementare. | Inferența modelelor |
| Inferența modelelor Claude | API Anthropic Messages | URL-ul de bază al gatewayului. Aperture gestionează `/v1/messages` | Inferență compatibilă cu Claude |
| Instrumente MCP | MCP HTTP Streamable | `/v1/mcp` | Instrumente și resurse de la conectorii configurați |

{{< figure src="aperture-client-routes.webp" alt="Codex și Hermes folosesc o rută Responses, Claude folosește Anthropic Messages, iar clienții MCP folosesc ruta separată /v1/mcp pentru a ajunge la conectorii Aperture" caption="Inferența modelelor și traficul MCP folosesc endpointuri Aperture separate" >}}

**Rădăcinile furnizorilor:** Aperture adaugă căile cererilor clientului la URL-ul de bază al furnizorului. Setează `baseurl` al furnizorului la rădăcina API a acestuia. Nu adăuga `/v1` la un URL de bază upstream când calea de intrare include deja `/v1`. Consultă [referința de configurare Aperture](https://tailscale.com/docs/aperture/configuration) pentru formarea URL-urilor, înregistrarea modelelor și granturi.

## Pregătește gatewayul

**Înainte de editare,** cere unui administrator Aperture aceste valori:

- **Numele gazdei gatewayului:** Folosește `http://` pentru majoritatea clienților conectați la tailnet. Inferența Claude Desktop necesită `https://` și un certificat de încredere.
- **Rute de inferență:** OpenAI Responses și Anthropic Messages folosesc formate diferite de cerere.
- **ID-uri de modele:** Găsește modelele disponibile pentru identitatea ta Tailscale folosind endpointul de mai jos. Utilizează ID-urile exacte returnate pentru acea identitate.
- **Autentificare:** Verifică dacă clientul trimite o cheie API substitut sau acreditările unui utilizator.
- **Endpoint MCP:** De obicei `http://<APERTURE_HOST>/v1/mcp` pentru clienții tailnet. Inferența Claude Desktop necesită HTTPS și un certificat de încredere.
- **Granturi de acces:** Verifică permisiunile pentru modele și conectori ale identității tale Tailscale.

**Acces la rețea:** Dispozitivul client trebuie să ajungă la gateway prin tailnet. Un nume de gazdă nu acordă acces la modele sau instrumente. Aperture refuză accesul dacă un grant potrivit nu permite modelul sau conectorul.

### Găsește modelele disponibile pentru utilizatorul tău

**Interoghează lista de modele** de pe un dispozitiv conectat la aceeași tailnet. Aperture folosește identitatea Tailscale a dispozitivului și returnează modelele acordate acelui utilizator, conform [ghidului de granturi pentru modele](https://tailscale.com/docs/aperture/how-to/grant-model-access):

```sh
# macOS sau Linux
curl -fsS http://<APERTURE_HOST>/v1/models
```

```powershell
# Windows PowerShell, apelează curl.exe pentru a evita aliasul vechi curl
curl.exe -fsS http://<APERTURE_HOST>/v1/models
```

**Citește rezultatul:** Folosește fiecare `id` returnat drept ID de model. Verifică `metadata.provider.id` pentru a identifica furnizorul Aperture. Alege un model compatibil cu formatul API al clientului. De exemplu, Claude Desktop necesită un model Anthropic Messages. [Directorul de modele](https://tailscale.com/docs/aperture/reference/chat) Aperture listează și identificatorii disponibili pentru utilizatorul autentificat.

**Lipsesc modele:** Dacă nu apare un model așteptat, cere unui administrator Aperture să verifice configurația furnizorului și grantul tău pentru model. Endpointul nu le permite utilizatorilor să-și acorde singuri acces.

**Schema URL-ului:** Tailscale recomandă `http://` pentru majoritatea clienților conectați la aceeași tailnet. WireGuard criptează traficul. Claude Desktop necesită `https://` și un certificat de încredere pentru sistemul de operare. Folosește schema indicată pentru fiecare client mai jos.

### Adaugă un furnizor de inferență

**OpenAI Responses:** Adaugă furnizorul upstream în Aperture și activează formatul API folosit de client. Pentru un furnizor OpenAI, adaugă un fragment ca acesta:

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

**Anthropic Messages:** Folosește rădăcina API Anthropic, formatul de autorizare `x-api-key` și compatibilitatea `anthropic_messages`. ID-ul modelului trebuie să apară și în lista `models` a furnizorului. Adaugă un fragment ca acesta:

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

**Modificări de configurare:** Înlocuiește fiecare substituent cu valorile upstream. Adaugă fragmentele la configurația Aperture existentă. Păstrează restul fișierului actual. Activează indicatorii de compatibilitate pentru API-urile suportate de furnizor.

**Granturi de acces:** Aperture controlează accesul fiecărui utilizator la fiecare model sau conector. Acordă fiecărui utilizator Tailscale vizat doar drepturile necesare. Acest exemplu oferă unui utilizator acces la un model al furnizorului și la un conector:

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

**Grant pentru model:** Folosește ID-ul furnizorului și ID-ul modelului în modelul de grant. [Ghidul de configurare a conectorilor](https://tailscale.com/docs/aperture/connectors/get-started) arată configurația actuală `connectors.servers`. Configurația veche `mcp.servers` de la nivel superior este depreciată.

### Adaugă un conector MCP

**Conector MCP:** Aperture se conectează la servere MCP upstream și expune instrumentele la `/v1/mcp`:

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

**URL-ul conectorului:** Folosește endpointul MCP complet al serverului upstream. Apoi acordă utilizatorului tău Tailscale acces la `teamtools/**` sau la un model mai restrâns de instrumente. [Referința proxy-ului MCP](https://tailscale.com/docs/aperture/mcp-server) explică endpointul unic al clientului și comportamentul conectorilor.

## Codex CLI și desktop

**Setări comune:** Codex CLI și aplicația desktop folosesc aceeași configurație. Pe macOS și Linux, editează `~/.codex/config.toml`. Pe Windows, editează `%USERPROFILE%\.codex\config.toml` (shellurile care extind directorul home acceptă și `~/.codex/config.toml`). [Prezentarea aplicației Codex](https://openai.com/index/introducing-the-codex-app/) spune că aplicația desktop preia configurația Codex CLI. Setările de utilizator Codex sunt în `~/.codex/config.toml`. Documentația [noțiunilor de bază privind configurarea](https://learn.chatgpt.com/docs/config-file/config-basic) descrie câmpurile de furnizor și MCP la nivel de utilizator. Adaugă furnizorul în acest fișier, repornește aplicația, apoi confirmă că furnizorul și modelul apar în interfață.

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

**Câmpuri opționale:** Aceste două valori corespund unei configurări de furnizor Codex. Păstrează-le doar dacă gatewayul și configurația Codex le cer. Ghidul actual Tailscale pentru [Codex Aperture](https://tailscale.com/docs/aperture/how-to/use-codex) le omite, folosește `wire_api = "responses"` și precizează că Aperture inserează acreditările upstream. Folosește URL-ul Responses exact de la administratorul gatewayului. `/codex` este o rută specifică implementării. Ruta implicită documentată de Tailscale este `/v1`.

**Configurare MCP:** Adaugă serverul în aceeași configurație de utilizator:

```toml
[mcp_servers.aperture]
url = "http://<APERTURE_HOST>/v1/mcp"
enabled = true
```

**Verifică Codex:** Rulează `codex mcp list`, pornește o sesiune nouă și inspectează `/mcp`. Lista de servere dovedește înregistrarea. Un instrument listat și un apel reușit dovedesc descoperirea și execuția. [Referința de configurare Codex](https://learn.chatgpt.com/docs/config-file/config-reference) documentează setările de furnizor și MCP la nivel de utilizator.

## Claude Code CLI

**Protocol:** Claude Code folosește Anthropic Messages. Configurează fișierul global de setări Claude Code să indice gatewayul Aperture compatibil Anthropic. Folosește `~/.claude/settings.json` pe macOS și Linux sau `%USERPROFILE%\.claude\settings.json` pe Windows. În PowerShell, folosește calea echivalentă `$HOME\.claude\settings.json`. Ruta trebuie să deservească `/v1/messages`. Codex Responses folosește alt protocol și altă rută. Tailscale recomandă HTTP pentru Claude Code în tailnet deoarece WireGuard criptează conexiunea.

```json
{
  "apiKeyHelper": "echo '-'",
  "env": {
    "ANTHROPIC_BASE_URL": "http://<APERTURE_HOST>"
  }
}
```

**Autentificarea clientului:** Ghidul clientului Aperture folosește un substituent în `apiKeyHelper`, deoarece Aperture inserează acreditarea upstream. Pentru transmiterea abonamentului Claude, furnizorul Anthropic din Aperture trebuie să trimită mai departe acreditarea Claude a utilizatorului. În acest caz, lasă `ANTHROPIC_API_KEY` și `ANTHROPIC_AUTH_TOKEN` neconfigurate. Aceste variabile înlocuiesc acreditarea abonamentului. Urmează instrucțiunile actuale [Claude Code Aperture](https://tailscale.com/docs/aperture/how-to/use-claude-code) pentru versiunea ta Claude Code și [ghidul Anthropic pentru gatewayuri](https://code.claude.com/docs/en/llm-gateway-connect) pentru opțiunile de autentificare.

**MCP prin HTTP:** Adaugă endpointul cu:

```sh
claude mcp add --transport http --scope user aperture http://<APERTURE_HOST>/v1/mcp
claude mcp list
```

**Verifică Claude Code:** Pornește o sesiune și rulează `/mcp` pentru a confirma conexiunea. Anthropic recomandă HTTP pentru servere MCP la distanță în [documentația MCP](https://code.claude.com/docs/en/mcp).

## Interfața grafică Claude Desktop

**Setări separate:** Claude Desktop are un ecran pentru inferență de la terți. Această setare direcționează cererile modelelor Claude Desktop prin Aperture. Configurarea MCP este un pas separat.

1. În Claude Desktop pentru macOS sau Windows, selectează **Ajutor > Depanare > Activează modul pentru dezvoltatori**. În versiunea beta Linux, folosește același meniu dacă există. Repornește aplicația dacă ți se cere. Dacă meniul lipsește, actualizează Claude Desktop și consultă notele de lansare pentru platforma ta.
2. Selectează **Dezvoltator > Configurează inferența de la terți**.
3. Setează **Tipul conexiunii** la **Gateway** și **Tipul acreditării** la **Cheie API statică**.
4. Introdu `https://<APERTURE_HOST>` ca **URL de bază al gatewayului**. Folosește numele complet al gazdei acoperit de un certificat TLS de încredere.
5. Introdu o cheie substitut nenulă, cum ar fi `aperture`, pentru gateway. Aperture ignoră substituentul și autentifică prin tailnet.
6. Lasă necompletate antetele de inferență personalizate.
7. Adaugă un model activat folosind un ID exact returnat de `GET /v1/models` pentru identitatea ta Tailscale. Filtrează un model Anthropic Messages. Introdu manual ID-ul, numele afișat și un alias opțional de nivel. Claude Desktop nu descoperă modele pe acest ecran.
8. Selectează **Salvează modificările**, apoi **Aplică modificările**. Închide Claude Desktop și deschide-l din nou.

**Verificarea protocolului:** [Ghidul Aperture pentru Claude Desktop](https://tailscale.com/docs/aperture/how-to/use-claude-desktop) spune că Claude Desktop folosește Anthropic Messages la `/v1/messages`. Nu introduce ruta Codex `/codex` și nu selecta un tip de conexiune compatibil OpenAI.

### Conectează Claude Desktop la MCP

**Acces MCP privat:** Rulează un bridge local stdio pe același computer cu Claude Desktop. Adaugă această configurație MCP locală în Claude Desktop:

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

**Cum funcționează bridge-ul:** Procesul local ajunge la Aperture prin conexiunea Tailscale a computerului. Folosește calea de configurare a sistemului tău: macOS, `~/Library/Application Support/Claude/claude_desktop_config.json`; Windows, `%APPDATA%\Claude\claude_desktop_config.json`; beta Linux, deschide **Setări > Dezvoltator > Editează configurația** și folosește calea deschisă de Claude Desktop. Calea Linux variază în funcție de pachet. Repornește Claude Desktop, verifică lista conectorilor și execută un apel inofensiv la un instrument. Proiectul [`mcp-remote`](https://github.com/punkpeye/mcp-remote) documentează bridge-ul local-la-distanță.

**Conectori la distanță:** Fluxul Setări > Conectori al Anthropic are nevoie de un server la distanță accesibil serviciului Anthropic. Un nume de gazdă numai pentru tailnet este privat dispozitivelor tale, deci folosește bridge-ul local pentru endpointul privat. Dacă expui un serviciu MCP public, configurează autentificarea și permisiunile înainte de a-l adăuga drept conector cloud. Consultă [ghidul Anthropic pentru conectori MCP la distanță](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp).

## OpenCode CLI și desktop

**Setări comune:** OpenCode CLI și aplicația desktop citesc aceeași configurație OpenCode. Documentația curentă OpenCode V2 folosește harta `providers` pentru furnizori personalizați și include serverele MCP în `mcp.servers`. Acest exemplu folosește endpointul de chat compatibil OpenAI la `/v1`. Verifică suportul OpenAI Chat Completions în furnizorul Aperture înainte de a folosi această rută.

**Configurație globală:** Pe macOS și Linux, editează `~/.config/opencode/opencode.json`. Pe Windows, folosește `%USERPROFILE%\.config\opencode\opencode.json`. Adaugă un furnizor compatibil OpenAI și înlocuiește `<MODEL_ID>` cu ID-ul exact al modelului Aperture. OpenCode acceptă și `opencode.jsonc` în același director pentru comentarii. [Referința de configurare](https://opencode.ai/docs/config/) explică prioritatea dintre setările globale și cele ale proiectului.

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

**Autentificarea clientului:** `oauth: false` omite fluxul OAuth implicit OpenCode. Aperture identifică apelantul prin Tailscale. OpenCode are nevoie și de o intrare de autentificare a furnizorului, deci setează `APERTURE_API_KEY=-` în mediul local. Aplicația desktop trebuie să primească și ea variabila. Dacă nu preia mediul shellului, rulează `/connect` în aplicație și introdu `-` pentru Aperture. Nu pune cheia furnizorului upstream în acest fișier. [Ghidul furnizorilor](https://opencode.ai/docs/providers/) și [ghidul MCP](https://opencode.ai/docs/mcp-servers/) OpenCode descriu formatul actual. Rulează `opencode mcp list` pentru a verifica serverul, apoi folosește `/mcps` în aplicație pentru a-i vedea starea.

## Hermes CLI și desktop

**Setări comune:** Hermes Agent stochează furnizori denumiți și servere MCP în `~/.hermes/config.yaml` pe macOS și Linux. Instalările Windows native folosesc `%LOCALAPPDATA%\hermes\config.yaml`. Rulează `hermes config path` pentru a confirma fișierul activ. `HERMES_HOME` poate schimba locația implicită. Hermes Desktop local folosește același director Hermes și același profil ca CLI. Dacă Desktop se conectează la un gateway Hermes la distanță, configurează Aperture pe mașina care rulează Hermes și verifică dacă serverul ajunge la tailnet. Vezi [ghidul Hermes Desktop](https://hermes-agent.nousresearch.com/docs/user-guide/desktop) pentru configurarea locală și la distanță.

**Furnizor Responses:** Adaugă un furnizor denumit. Valoarea `api` trebuie să corespundă endpointului Responses al instanței tale Aperture:

```yaml
providers:
  aperture:
    api: "http://<APERTURE_HOST>/v1"
    transport: codex_responses
    default_model: "<MODEL_ID>"
    # Adaugă key_env doar dacă setarea Aperture cere o cheie pentru client.
    # key_env: APERTURE_API_KEY

model:
  provider: "custom:aperture"
  default: "<MODEL_ID>"
```

**Selectarea protocolului:** Pentru OpenAI Chat Completions, setează `transport: chat_completions`. Pentru Anthropic Messages, alege `transport: anthropic_messages` și folosește URL-ul gatewayului Anthropic Messages. Ghidul actual pentru [furnizori](https://hermes-agent.nousresearch.com/docs/integrations/providers) descrie câmpurile `api`, `transport` și `default_model` pentru furnizorii Hermes denumiți.

**Configurare MCP:** Adaugă Aperture MCP în același fișier YAML:

```yaml
mcp_servers:
  aperture:
    url: "http://<APERTURE_HOST>/v1/mcp"
    enabled: true
```

**Verifică Hermes:** Rulează `hermes mcp` și verifică fiecare conexiune în selectorul interactiv de servere. Desktop local expune același profil. Hermes documentează [servere MCP HTTP la distanță](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) și [referința completă pentru configurarea MCP](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference).

## Verifică ambele căi

**Rulează verificări separate** pentru inferența modelelor și MCP:

1. Confirmă conectivitatea Tailscale și accesul dispozitivului la gateway. Pentru Claude Desktop, confirmă că gatewayul prezintă un certificat TLS de încredere.
2. Trimite o cerere scurtă prin fiecare client configurat. Confirmă că o cerere corespunzătoare apare în lista de sesiuni Aperture.
3. Confirmă că ID-ul modelului ales corespunde unui model acordat identității tale Tailscale.
4. Deschide ecranul de stare MCP al fiecărui client sau rulează comanda de listare. Confirmă că serverul Aperture se conectează și expune instrumentele așteptate.
5. Apelează un instrument doar în citire. Compară conținutul returnat cu sursa upstream.
6. Verifică jurnalele Aperture dacă apelul modelului sau al instrumentului eșuează. Un fișier de configurare salvat nu dovedește o cerere reușită.

| Simptom | Verificare |
|---|---|
| Cererea modelului returnează 404 sau 405 | Confirmă că endpointul clientului folosește ruta și protocolul corecte. Nu reutiliza `/codex` pentru Anthropic Messages sau MCP. |
| Model indisponibil | Interoghează `/v1/models` ca utilizatorul Tailscale vizat. Verifică dacă apare ID-ul exact și dacă formatul API se potrivește clientului. Cere unui administrator să verifice furnizorii sau granturile lipsă. |
| Cerere neautorizată | Verifică dacă clientul are nevoie de un substituent, un token bearer sau transmiterea abonamentului. Nu copia o cheie de furnizor upstream într-un fișier public de proiect. |
| Serverul MCP apare, dar nu sunt afișate instrumente | Verifică `/v1/mcp`, starea conectorului, granturile conectorului și calea de rețea a clientului către Aperture. |
| Claude Desktop nu se conectează la un URL MCP privat | Rulează un bridge local precum `mcp-remote` sau folosește un conector public aprobat, cu autentificare potrivită. |

## Recreează configurația pe alt dispozitiv

**Dispozitiv nou:** Instalează același client și conectează mai întâi dispozitivul la tailnet. Interoghează `/v1/models` de pe noul dispozitiv pentru a găsi modelele acordate identității sale Tailscale. Copiază structura configurației și păstrează acreditările local. Înlocuiește `<APERTURE_HOST>`, `<MODEL_ID>` și `<UPSTREAM_MCP_ENDPOINT>` cu valorile instanței Aperture vizate. Păstrează un endpoint separat pentru fiecare protocol API, apoi configurează calea `/v1/mcp` pentru traficul instrumentelor. La final, verifică o cerere de model și un apel la un instrument MCP.

**Mai multe gatewayuri:** Folosește o configurație separată pentru fiecare instanță Aperture. Un dispozitiv are nevoie de un endpoint Responses pentru Codex și Hermes, un endpoint Anthropic Messages pentru Claude și endpointul de agregare MCP pentru instrumente. Salvează acreditările API în managerul local de secrete al fiecărui client sau într-o variabilă de mediu. Nu copia chei API în fișiere partajate precum `config.toml`, `opencode.json`, `config.yaml` sau într-un depozit public.

## Prompt reutilizabil pentru configurarea Aperture

**Copiază acest prompt anonimizat** în asistentul tău de programare. Înlocuiește substituenții cu detaliile gatewayului. Asistentul trebuie să interogheze Aperture folosind identitatea ta Tailscale înainte să aleagă ID-uri de modele.

```text
Configurează gatewayul meu Tailscale Aperture existent și clienții AI instalați pe acest dispozitiv.

Clienți incluși: Codex CLI și desktop, Claude Code, Claude Desktop, OpenCode CLI și desktop, Hermes CLI și desktop.

Mai întâi detectează dacă dispozitivul folosește macOS, Linux sau Windows, identifică shellul activ (de exemplu zsh, bash sau PowerShell) și utilizează peste tot căile și sintaxa comenzilor pentru acea platformă. Inspectează întâi gatewayul actual, conexiunea Tailscale, versiunile clienților și setările existente. Citește documentația oficială actuală. Păstrează configurațiile fără legătură și fă copii de siguranță ale fișierelor înainte de editare. Nu ghici nume de gazde, ID-uri de modele, rute API sau acreditări. Păstrează cheile furnizorilor upstream în Aperture, nu în fișierele clienților sau în acest depozit.

Descoperă modelele disponibile de pe acest dispozitiv conectat la Tailscale:
1. Interoghează `http://<APERTURE_HOST>/v1/models` folosind identitatea Tailscale a clienților mei. Dacă diferă, folosește URL-ul personalizat documentat pentru lista de modele a gatewayului.
2. Citește `id` și `metadata.provider.id` pentru fiecare model. Lista arată modelele acordate identității mele. Nu folosi lista administratorului și nu inventa ID-uri.
3. Potrivește compatibilitatea API a fiecărui model cu clientul corespunzător. Codex folosește OpenAI Responses. Clienții Claude folosesc Anthropic Messages. OpenCode și Hermes au nevoie de furnizori și transporturi compatibile configurate.
4. Reutilizează modelul implicit existent al clientului când este posibil. Dacă un client are nevoie de un model implicit și nu am o preferință, arată-mi modelele compatibile și cere-mi să aleg. Claude Desktop cere introducerea manuală a ID-ului exact al modelului.
5. Dacă endpointul nu returnează un model potrivit, verifică configurația furnizorului și granturile doar dacă am acces administrativ. Altfel, spune ce acces la model trebuie să adauge un administrator. Nu-ți acorda acces.

Localizează implementarea Aperture și sursa configurației. Nu presupune o cale de fișier și nu înlocui întreaga configurație. OpenAI Responses cere `openai_responses`. Clienții Anthropic cer `anthropic_messages`. Conectorii MCP aparțin configurației actuale `connectors.servers`, iar clienții se conectează prin `/v1/mcp`.

Înainte de modificarea unui gateway partajat, pregătește diff-ul minim pentru furnizori, conectori și granturi. Aplică-l numai dacă am autoritate administrativă și această solicitare autorizează schimbările gatewayului. Dacă nu am acea autoritate, raportează schimbările exacte propuse pentru proprietarul instanței. Nu crea și nu extinde granturi fără autorizarea explicită a proprietarului. Păstrează toate setările existente ale gatewayului.

Configurează fiecare client instalat cu formatul oficial actual și locația specifică sistemului de operare:
- Codex CLI și desktop partajează `~/.codex/config.toml` pe macOS/Linux și `%USERPROFILE%\.codex\config.toml` pe Windows. Setează furnizorul Aperture, un model compatibil, `wire_api = "responses"` și MCP în `mcp_servers`.
- Claude Code folosește `ANTHROPIC_BASE_URL` și MCP la distanță prin HTTP. Folosește `~/.claude/settings.json` pe macOS/Linux și `%USERPROFILE%\.claude\settings.json` pe Windows.
- Claude Desktop folosește Modul pentru dezvoltatori, Configurează inferența de la terți, Gateway, Cheie API statică, un URL HTTPS al gatewayului cu certificat de încredere și un ID de model găsit pentru utilizatorul meu. Folosește un bridge local `mcp-remote` pentru MCP privat pe tailnet. Caută configurația MCP în Setări > Dezvoltator > Editează configurația, dacă este disponibilă. Altfel folosește calea documentată pentru sistemul detectat.
- OpenCode folosește schema V2 actuală `providers` și `mcp.servers`. Configurația globală este `~/.config/opencode/opencode.json` pe macOS/Linux și `%USERPROFILE%\.config\opencode\opencode.json` pe Windows. Setează `oauth: false` pentru MCP Aperture. Folosește o cheie API substitut locală când este necesar.
- Hermes folosește un furnizor denumit, un transport potrivit API-ului modelului și `mcp_servers`. Folosește `~/.hermes/config.yaml` pe macOS/Linux. Pe Windows, verifică `hermes config path`, de obicei `%LOCALAPPDATA%\hermes\config.yaml`. Verifică dacă Hermes Desktop partajează profilul Hermes local.

Folosește HTTP pentru traficul tailnet când clientul acceptă. Inferența Claude Desktop cere HTTPS cu un certificat de încredere. Folosește `/v1` dacă gatewayul nu documentează altă rută.

Repornește clienții configurați. Verifică în Aperture câte o cerere de model pentru fiecare client și un apel inofensiv, doar în citire, la un instrument MCP. Raportează modelele descoperite pentru identitatea mea, clienții și fișierele modificate, rezultatele verificării și acțiunile administrative rămase. Nu instala software, nu expune public gatewayul, nu face commit și nu publica.
```

## Concluzie

O configurare funcțională Aperture depinde de trei lucruri: un gateway accesibil, o rută de model potrivită protocolului clientului și granturi pentru modelele și conectorii MCP necesari. Aceleași tipare de configurare funcționează pe macOS, Linux și Windows, dar fiecare client își salvează setările într-o locație proprie sistemului de operare.

Găsește ID-urile modelelor folosind identitatea Tailscale care le va utiliza. Configurează separat inferența modelelor și `/v1/mcp`, apoi verifică o cerere reală și un apel la un instrument doar în citire. Când treci la alt dispozitiv sau la altă instanță Aperture, reutilizează structura acestui ghid, confirmă rutele și granturile acelei instanțe și păstrează acreditările în managerul local de secrete.

## Pașii următori

**Exerciții MCP:** Pentru diferența dintre un server salvat și un apel verificat la un instrument, citește [Configurarea unui server MCP: permisiuni, testarea instrumentelor și eliminarea sigură](/articles/effective-ai-mcp-server-setup/). Pentru arhitectura mai largă auto-găzduită, consultă [Flotă hibridă de agenți AI: Tailscale, LiteLLM și Hermes](/articles/hybrid-agentic-ai-fleet-tailscale-litellm-hermes/).
