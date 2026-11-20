---
title: "Tailscale Aperture: configurare i client IA per inferenza e MCP nel 2026"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Instrada le richieste dei modelli e gli strumenti MCP tramite Tailscale Aperture. Configura Codex, Claude Code, Claude Desktop, OpenCode e Hermes su un altro dispositivo o gateway."
genre: ["Intelligenza artificiale", "Strumenti per sviluppatori", "Reti"]
tags: ["Tailscale Aperture", "Configurazione Aperture", "Proxy IA", "Gateway LLM", "Gateway MCP", "Codex Aperture", "Claude Code Aperture", "Claude Desktop Aperture", "OpenCode Aperture", "Hermes Agent Aperture", "Codex MCP", "Claude MCP", "OpenCode MCP", "Hermes MCP", "Proxy di inferenza IA", "API Responses", "API Anthropic Messages", "MCP remoto", "HTTP Streamable", "Tailscale", "IA self-hosted", "Agenti di programmazione", "Configurazione client IA"]
cover: "/img/cover/tailscale-aperture-agent-setup.webp"
coverAlt: "Aperture collega i pannelli dei client ai servizi di modelli e strumenti MCP tramite percorsi separati, blu per l'inferenza e verde per gli strumenti"
coverCaption: ""
---

## Introduzione

Tailscale Aperture offre ai client IA un gateway collegato alla tailnet per l'inferenza dei modelli e gli strumenti Model Context Protocol (MCP). Ogni client deve usare un percorso compatibile con il proprio protocollo API. Gli strumenti MCP usano un endpoint separato e le autorizzazioni Aperture controllano quali modelli e connettori ogni identità Tailscale può usare.

Questa guida spiega come configurare Codex, Claude Code, Claude Desktop, OpenCode e Hermes su macOS, Linux e Windows. Copre le impostazioni della CLI e delle app desktop, mostra come individuare gli ID dei modelli disponibili per la propria identità e include un prompt anonimizzato riutilizzabile quando si configura un altro dispositivo o un'altra istanza Aperture.

**Scelta del percorso:** I percorsi degli endpoint dipendono dal gateway e da ciascun protocollo API. Un percorso Responses come `/codex` non gestisce traffico Anthropic Messages o MCP. Conferma il nome host del gateway e il percorso di inferenza di ciascun client. Individua gli ID dei modelli tramite il tuo accesso Aperture prima di modificare le impostazioni del client.

## Punti chiave

- **Il traffico dei modelli** richiede il percorso API previsto dal protocollo del client.
- **Il traffico MCP** usa l'endpoint separato `/v1/mcp`.
- **Le autorizzazioni del gateway** devono consentire alla tua identità Tailscale di usare ogni modello e connettore.
- **La configurazione del client** prova solo che le impostazioni sono state salvate. Verifica una richiesta reale e una chiamata a uno strumento MCP.

## Come funzionano i percorsi

| Scopo | Richiesta del client | Percorso Aperture | Servizio offerto |
|---|---|---|---|
| Codex e modelli compatibili con Responses | API OpenAI Responses | Di solito `/v1`. Un percorso personalizzato come `/codex` dipende dal deployment. | Inferenza dei modelli |
| Inferenza dei modelli Claude | API Anthropic Messages | URL base del gateway. Aperture gestisce `/v1/messages` | Inferenza compatibile con Claude |
| Strumenti MCP | MCP HTTP Streamable | `/v1/mcp` | Strumenti e risorse dei connettori configurati |

{{< figure src="aperture-client-routes.webp" alt="Codex e Hermes usano un percorso Responses, Claude usa Anthropic Messages e i client MCP usano il percorso separato /v1/mcp per raggiungere i connettori Aperture" caption="L'inferenza dei modelli e il traffico MCP usano endpoint Aperture separati" >}}

**Radici dei provider:** Aperture aggiunge i percorsi delle richieste del client all'URL base del provider. Imposta `baseurl` del provider sulla radice della sua API. Non aggiungere `/v1` a un URL base upstream quando il percorso in ingresso include già `/v1`. Consulta il [riferimento di configurazione Aperture](https://tailscale.com/docs/aperture/configuration) per la costruzione degli URL, la registrazione dei modelli e le autorizzazioni.

## Prepara il gateway

**Prima di modificare la configurazione,** chiedi all'amministratore Aperture questi valori:

- **Nome host del gateway:** Usa `http://` con la maggior parte dei client collegati alla tailnet. L'inferenza Claude Desktop richiede `https://` con un certificato attendibile.
- **Percorsi di inferenza:** OpenAI Responses e Anthropic Messages usano formati di richiesta diversi.
- **ID dei modelli:** Individua i modelli disponibili per la tua identità Tailscale con l'endpoint qui sotto. Usa gli ID esatti restituiti per quell'identità.
- **Autenticazione:** Verifica se il client invia una chiave API segnaposto o una credenziale utente.
- **Endpoint MCP:** Di solito `http://<APERTURE_HOST>/v1/mcp` per i client della tailnet. L'inferenza Claude Desktop richiede HTTPS con un certificato attendibile.
- **Autorizzazioni di accesso:** Verifica i permessi sui modelli e sui connettori per la tua identità Tailscale.

**Accesso di rete:** Il dispositivo client deve raggiungere il gateway tramite la tailnet. Il nome host da solo non concede accesso ai modelli o agli strumenti. Aperture nega l'accesso se un'autorizzazione corrispondente non consente il modello o il connettore.

### Trova i modelli disponibili per il tuo utente

**Interroga l'elenco dei modelli** da un dispositivo collegato alla stessa tailnet. Aperture usa l'identità Tailscale del dispositivo e restituisce i modelli concessi a quell'utente, come descritto nella [guida alle autorizzazioni dei modelli](https://tailscale.com/docs/aperture/how-to/grant-model-access):

```sh
# macOS o Linux
curl -fsS http://<APERTURE_HOST>/v1/models
```

```powershell
# Windows PowerShell, usa curl.exe per evitare il vecchio alias curl
curl.exe -fsS http://<APERTURE_HOST>/v1/models
```

**Leggi il risultato:** Usa ogni `id` restituito come ID del modello. Controlla `metadata.provider.id` per identificare il provider Aperture. Scegli un modello che supporti il formato API del client. Per esempio, Claude Desktop richiede un modello Anthropic Messages. Anche la [directory dei modelli](https://tailscale.com/docs/aperture/reference/chat) Aperture elenca gli identificatori disponibili per l'utente autenticato.

**Modelli mancanti:** Se un modello atteso non compare, chiedi all'amministratore Aperture di verificare la configurazione del provider e la tua autorizzazione. L'endpoint non consente agli utenti di concedersi l'accesso.

**Schema URL:** Tailscale consiglia `http://` per la maggior parte dei client collegati alla stessa tailnet. WireGuard cifra questo traffico. Claude Desktop richiede `https://` e un certificato attendibile per il sistema operativo. Usa lo schema indicato per ciascun client qui sotto.

### Aggiungi un provider di inferenza

**OpenAI Responses:** Aggiungi il provider upstream ad Aperture e abilita il formato API usato dal client. Per un provider OpenAI, aggiungi un frammento come questo:

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

**Anthropic Messages:** Usa la radice API Anthropic, il formato di autorizzazione `x-api-key` e la compatibilità `anthropic_messages`. L'ID del modello deve essere anche nell'elenco `models` del provider. Aggiungi un frammento come questo:

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

**Modifiche alla configurazione:** Sostituisci ogni segnaposto con i valori upstream. Aggiungi i frammenti alla configurazione Aperture esistente. Conserva il resto del file attuale. Attiva i flag di compatibilità per le API supportate dal provider.

**Autorizzazioni di accesso:** Aperture controlla l'accesso di ogni utente a ciascun modello o connettore. Concedi a ogni utente Tailscale previsto solo i permessi necessari. Questo esempio concede a un utente l'accesso a un modello provider e a un connettore:

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

**Autorizzazione del modello:** Usa l'ID provider e l'ID modello nel pattern dell'autorizzazione. La [guida alla configurazione dei connettori](https://tailscale.com/docs/aperture/connectors/get-started) mostra la configurazione attuale `connectors.servers`. La vecchia configurazione di primo livello `mcp.servers` è deprecata.

### Aggiungi un connettore MCP

**Connettore MCP:** Aperture si collega ai server MCP upstream ed espone gli strumenti in `/v1/mcp`:

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

**URL del connettore:** Usa l'endpoint MCP completo del server upstream. Poi autorizza il tuo utente Tailscale ad accedere a `teamtools/**` o a un pattern più ristretto. Il [riferimento al proxy MCP](https://tailscale.com/docs/aperture/mcp-server) spiega l'endpoint unico per i client e il comportamento dei connettori.

## Codex CLI e app desktop

**Impostazioni condivise:** Codex CLI e l'app desktop usano la stessa configurazione. Su macOS e Linux, modifica `~/.codex/config.toml`. Su Windows, modifica `%USERPROFILE%\.codex\config.toml` (anche `~/.codex/config.toml` nei terminali che espandono la home). La [presentazione dell'app Codex](https://openai.com/index/introducing-the-codex-app/) dice che l'app desktop riprende la configurazione di Codex CLI. Le impostazioni utente di Codex si trovano in `~/.codex/config.toml`. La documentazione sulle [basi della configurazione](https://learn.chatgpt.com/docs/config-file/config-basic) descrive i campi provider e MCP a livello utente. Aggiungi il provider a questo file, riavvia l'app e controlla che provider e modello compaiano nell'interfaccia.

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

**Campi facoltativi:** Questi due valori corrispondono a una configurazione provider Codex. Mantienili solo se richiesti dal gateway e dalla configurazione Codex. L'attuale [guida Tailscale a Codex Aperture](https://tailscale.com/docs/aperture/how-to/use-codex) li omette, usa `wire_api = "responses"` e dice che Aperture inserisce le credenziali upstream. Usa l'URL Responses esatto indicato dall'amministratore del gateway. `/codex` è un percorso specifico del deployment. Il percorso predefinito documentato da Tailscale è `/v1`.

**Configurazione MCP:** Aggiungi il server alla stessa configurazione utente:

```toml
[mcp_servers.aperture]
url = "http://<APERTURE_HOST>/v1/mcp"
enabled = true
```

**Verifica Codex:** Esegui `codex mcp list`, avvia una nuova sessione e controlla `/mcp`. L'elenco dei server prova la registrazione. Uno strumento elencato e una chiamata riuscita provano il rilevamento e l'esecuzione. Il [riferimento alla configurazione Codex](https://learn.chatgpt.com/docs/config-file/config-reference) descrive le impostazioni utente di provider e MCP.

## Claude Code CLI

**Protocollo:** Claude Code usa Anthropic Messages. Imposta il file globale delle impostazioni Claude Code sul gateway Aperture compatibile con Anthropic. Usa `~/.claude/settings.json` su macOS e Linux, oppure `%USERPROFILE%\.claude\settings.json` su Windows. In PowerShell, usa il percorso equivalente `$HOME\.claude\settings.json`. Il percorso deve servire `/v1/messages`. Codex Responses usa un protocollo e un percorso diversi. Tailscale consiglia HTTP per Claude Code sulla tailnet perché WireGuard cifra la connessione.

```json
{
  "apiKeyHelper": "echo '-'",
  "env": {
    "ANTHROPIC_BASE_URL": "http://<APERTURE_HOST>"
  }
}
```

**Autenticazione client:** La guida Aperture usa un segnaposto in `apiKeyHelper` perché Aperture inserisce la credenziale upstream. Per inoltrare l'abbonamento Claude, il provider Anthropic Aperture deve inoltrare la credenziale Claude dell'utente. In questo caso, lascia non impostate `ANTHROPIC_API_KEY` e `ANTHROPIC_AUTH_TOKEN`. Queste variabili sostituiscono la credenziale dell'abbonamento. Segui le istruzioni aggiornate di [Claude Code su Aperture](https://tailscale.com/docs/aperture/how-to/use-claude-code) per la tua versione di Claude Code e la [guida ai gateway Anthropic](https://code.claude.com/docs/en/llm-gateway-connect) per le opzioni di autenticazione.

**MCP su HTTP:** Aggiungi l'endpoint con:

```sh
claude mcp add --transport http --scope user aperture http://<APERTURE_HOST>/v1/mcp
claude mcp list
```

**Verifica Claude Code:** Avvia una sessione ed esegui `/mcp` per confermare la connessione. Nella [documentazione MCP](https://code.claude.com/docs/en/mcp), Anthropic consiglia HTTP per i server MCP remoti.

## Interfaccia grafica Claude Desktop

**Impostazioni separate:** Claude Desktop ha una schermata di inferenza di terze parti. Questa impostazione instrada le richieste dei modelli Claude Desktop tramite Aperture. La configurazione MCP richiede un passaggio separato.

1. In Claude Desktop per macOS o Windows, scegli **Aiuto > Risoluzione dei problemi > Abilita modalità sviluppatore**. Nella beta Linux, usa lo stesso menu se disponibile. Riavvia l'app se richiesto. Se il menu manca, aggiorna Claude Desktop e consulta le note di rilascio specifiche della piattaforma.
2. Scegli **Sviluppatore > Configura inferenza di terze parti**.
3. Imposta **Tipo di connessione** su **Gateway** e **Tipo credenziale** su **Chiave API statica**.
4. Inserisci `https://<APERTURE_HOST>` come **URL base gateway**. Usa il nome host completo coperto da un certificato TLS attendibile.
5. Inserisci una chiave segnaposto non vuota, ad esempio `aperture`. Aperture ignora il segnaposto e autentica tramite la tailnet.
6. Lascia vuote le intestazioni di inferenza personalizzate.
7. Aggiungi un modello abilitato con un ID esatto restituito da `GET /v1/models` per la tua identità Tailscale. Filtra i modelli Anthropic Messages. Inserisci manualmente il suo ID, il nome visualizzato e un alias di livello facoltativo. Claude Desktop non rileva i modelli in questa schermata.
8. Seleziona **Salva modifiche**, poi **Applica modifiche**. Chiudi Claude Desktop e riaprilo.

**Verifica del protocollo:** La [guida Aperture per Claude Desktop](https://tailscale.com/docs/aperture/how-to/use-claude-desktop) dice che Claude Desktop usa Anthropic Messages su `/v1/messages`. Non inserire il percorso Codex `/codex` e non scegliere un tipo di connessione compatibile con OpenAI.

### Collega Claude Desktop a MCP

**Accesso MCP privato:** Esegui un bridge locale di tipo stdio sullo stesso computer di Claude Desktop. Aggiungi questo alla configurazione MCP locale di Claude Desktop:

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

**Funzionamento del bridge:** Il processo locale raggiunge Aperture tramite la connessione Tailscale del computer. Usa il percorso di configurazione del sistema operativo: macOS, `~/Library/Application Support/Claude/claude_desktop_config.json`; Windows, `%APPDATA%\Claude\claude_desktop_config.json`; beta Linux, apri **Impostazioni > Sviluppatore > Modifica configurazione** e usa il percorso aperto da Claude Desktop. Il percorso Linux varia a seconda del pacchetto. Riavvia Claude Desktop, controlla l'elenco dei connettori e prova una chiamata innocua a uno strumento. Il [progetto `mcp-remote`](https://github.com/punkpeye/mcp-remote) documenta questo bridge locale-remoto.

**Connettori remoti:** Il flusso Impostazioni > Connettori di Anthropic richiede un server remoto raggiungibile dal servizio Anthropic. Un nome host disponibile solo nella tailnet è privato ai tuoi dispositivi, quindi usa il bridge locale per l'endpoint privato. Se esponi un servizio MCP pubblico, configurane l'autenticazione e i permessi prima di aggiungerlo come connettore cloud. Consulta la [guida ai connettori MCP remoti](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) Anthropic.

## OpenCode CLI e app desktop

**Impostazioni condivise:** OpenCode CLI e app desktop leggono la stessa configurazione OpenCode. La documentazione OpenCode V2 attuale usa la mappa `providers` per i provider personalizzati e inserisce i server MCP in `mcp.servers`. Questo esempio usa l'endpoint chat compatibile con OpenAI su `/v1`. Verifica che il provider Aperture supporti OpenAI Chat Completions prima di usare questo percorso modello.

**Configurazione globale:** Su macOS e Linux, modifica `~/.config/opencode/opencode.json`. Su Windows usa `%USERPROFILE%\.config\opencode\opencode.json`. Aggiungi un provider compatibile con OpenAI e sostituisci `<MODEL_ID>` con l'ID esatto del modello Aperture. OpenCode accetta anche `opencode.jsonc` nella stessa cartella per i commenti. Il [riferimento alla configurazione](https://opencode.ai/docs/config/) spiega la precedenza tra le impostazioni globali e quelle del progetto.

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

**Autenticazione client:** `oauth: false` salta il flusso OAuth predefinito di OpenCode. Aperture identifica il chiamante tramite Tailscale. OpenCode richiede anche un'entrata di autenticazione del provider, quindi imposta `APERTURE_API_KEY=-` nell'ambiente locale. Anche l'app desktop deve ricevere la variabile. Se non eredita l'ambiente della shell, esegui `/connect` nell'app e inserisci `-` per Aperture. Non inserire la chiave del provider upstream in questo file. La [guida ai provider](https://opencode.ai/docs/providers/) e la [guida MCP](https://opencode.ai/docs/mcp-servers/) di OpenCode descrivono il formato attuale. Esegui `opencode mcp list` per controllare il server, poi usa `/mcps` nell'app per verificarne lo stato.

## Hermes CLI e app desktop

**Impostazioni condivise:** Hermes Agent salva i provider denominati e i server MCP in `~/.hermes/config.yaml` su macOS e Linux. Le installazioni native Windows usano `%LOCALAPPDATA%\hermes\config.yaml`. Esegui `hermes config path` per verificare il file attivo sul tuo sistema. `HERMES_HOME` può sostituire il percorso predefinito. Hermes Desktop locale usa la stessa home Hermes e lo stesso profilo della CLI. Se Desktop si collega a un gateway Hermes remoto, configura Aperture sul computer che esegue Hermes e verifica che il server raggiunga la tailnet. Consulta la [guida Hermes Desktop](https://hermes-agent.nousresearch.com/docs/user-guide/desktop) per la configurazione locale e remota.

**Provider Responses:** Aggiungi un provider denominato. Il valore `api` deve corrispondere all'endpoint Responses della tua istanza Aperture:

```yaml
providers:
  aperture:
    api: "http://<APERTURE_HOST>/v1"
    transport: codex_responses
    default_model: "<MODEL_ID>"
    # Aggiungi key_env solo se la configurazione Aperture richiede una chiave client.
    # key_env: APERTURE_API_KEY

model:
  provider: "custom:aperture"
  default: "<MODEL_ID>"
```

**Scelta del protocollo:** Per OpenAI Chat Completions, imposta `transport: chat_completions`. Per Anthropic Messages, scegli `transport: anthropic_messages` e usa l'URL del gateway Anthropic Messages. La guida attuale ai [provider](https://hermes-agent.nousresearch.com/docs/integrations/providers) descrive i campi `api`, `transport` e `default_model` dei provider denominati Hermes.

**Configurazione MCP:** Aggiungi Aperture MCP allo stesso file YAML:

```yaml
mcp_servers:
  aperture:
    url: "http://<APERTURE_HOST>/v1/mcp"
    enabled: true
```

**Verifica Hermes:** Esegui `hermes mcp` e controlla ogni connessione nel selettore interattivo dei server. Desktop locale espone lo stesso profilo. Hermes documenta i [server MCP HTTP remoti](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) e il [riferimento completo alla configurazione MCP](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference).

## Verifica entrambi i percorsi

**Esegui controlli separati** per l'inferenza dei modelli e MCP:

1. Conferma che il dispositivo sia connesso a Tailscale e raggiunga il gateway. Per Claude Desktop, verifica che il gateway presenti un certificato TLS attendibile.
2. Invia un prompt breve tramite ciascun client configurato. Verifica che una richiesta corrispondente compaia nell'elenco delle sessioni Aperture.
3. Conferma che l'ID del modello selezionato corrisponda a un modello concesso alla tua identità Tailscale.
4. Apri la schermata di stato MCP di ogni client o esegui il comando elenco. Verifica che il server Aperture si connetta ed esponga gli strumenti previsti.
5. Chiama uno strumento in sola lettura. Confronta il contenuto restituito con la fonte upstream.
6. Controlla i log Aperture se la chiamata al modello o allo strumento fallisce. Una configurazione salvata non prova che la richiesta sia riuscita.

| Sintomo | Controllo |
|---|---|
| La richiesta del modello restituisce 404 o 405 | Verifica che l'endpoint client usi il percorso e il protocollo corretti. Non riutilizzare `/codex` per Anthropic Messages o MCP. |
| Modello non disponibile | Interroga `/v1/models` come l'utente Tailscale previsto. Controlla che compaia l'ID esatto e che il formato API corrisponda al client. Chiedi a un amministratore di controllare provider o autorizzazioni mancanti. |
| Richiesta non autorizzata | Verifica se il client richiede un segnaposto, un token bearer o l'inoltro dell'abbonamento. Non copiare mai una chiave provider upstream in un file di progetto pubblico. |
| Il server MCP è elencato ma non compaiono strumenti | Controlla `/v1/mcp`, lo stato del connettore, le autorizzazioni del connettore e il percorso di rete del client verso Aperture. |
| Claude Desktop non si connette a un URL MCP privato | Esegui un bridge locale come `mcp-remote` o usa un connettore pubblico approvato con autenticazione adeguata. |

## Ricrea la configurazione su un altro dispositivo

**Nuovo dispositivo:** Installa lo stesso client e collega prima il dispositivo alla tailnet. Interroga `/v1/models` dal nuovo dispositivo per individuare i modelli concessi alla sua identità Tailscale. Copia la struttura della configurazione e conserva localmente le credenziali. Sostituisci `<APERTURE_HOST>`, `<MODEL_ID>` e `<UPSTREAM_MCP_ENDPOINT>` con i valori dell'istanza Aperture di destinazione. Mantieni un endpoint separato per ogni protocollo API, poi configura il percorso `/v1/mcp` per gli strumenti. Infine verifica una richiesta modello e una chiamata a uno strumento MCP.

**Più gateway:** Usa una configurazione separata per ogni istanza Aperture. Un dispositivo necessita di un endpoint Responses per Codex e Hermes, di un endpoint Anthropic Messages per Claude e dell'endpoint MCP aggregato per gli strumenti. Salva le credenziali API nel secret store locale di ciascun client o in una variabile d'ambiente. Non copiare le chiavi API in file condivisi `config.toml`, `opencode.json`, `config.yaml` o in un repository pubblico.

## Prompt Aperture riutilizzabile

**Copia questo prompt anonimizzato** nel tuo assistente di programmazione. Sostituisci i segnaposto con i dettagli del gateway. L'assistente deve interrogare Aperture con la tua identità Tailscale prima di scegliere gli ID dei modelli.

```text
Configura il mio gateway Tailscale Aperture esistente e i client IA installati su questo dispositivo.

Client inclusi: Codex CLI e desktop, Claude Code, Claude Desktop, OpenCode CLI e desktop, Hermes CLI e desktop.

Per prima cosa rileva se questo dispositivo usa macOS, Linux o Windows, identifica la shell attiva (per esempio zsh, bash o PowerShell) e usa sempre i percorsi e la sintassi dei comandi di quella piattaforma. Esamina prima il gateway attuale, la connessione Tailscale, le versioni dei client e le impostazioni esistenti. Consulta la documentazione ufficiale aggiornata. Conserva le configurazioni non correlate e crea un backup di ogni file prima di modificarlo. Non indovinare nomi host, ID dei modelli, percorsi API o credenziali. Conserva le chiavi dei provider upstream in Aperture, non nei file dei client o in questo repository.

Individua i modelli disponibili da questo dispositivo connesso a Tailscale:
1. Interroga `http://<APERTURE_HOST>/v1/models` usando l'identità Tailscale dei miei client. Se differisce, usa l'URL personalizzato documentato per l'elenco modelli del gateway.
2. Leggi `id` e `metadata.provider.id` di ogni modello. Questo elenco riflette i modelli concessi alla mia identità. Non sostituirlo con l'elenco dell'amministratore e non inventare ID.
3. Abbina la compatibilità API di ciascun modello al relativo client. Codex usa OpenAI Responses. I client Claude usano Anthropic Messages. OpenCode e Hermes richiedono un provider e un trasporto compatibili configurati.
4. Quando possibile, riutilizza il modello predefinito esistente del client. Se un client ne richiede uno e non ho preferenze, mostrarmi i modelli compatibili e chiedimi di scegliere. Claude Desktop richiede l'inserimento manuale dell'ID esatto.
5. Se l'endpoint non restituisce un modello adatto, controlla provider e autorizzazioni solo se dispongo dei permessi amministrativi. Altrimenti indica quale accesso modello deve aggiungere un amministratore. Non concederti accesso.

Individua il deployment Aperture e la fonte della sua configurazione. Non presumere un percorso file e non sostituire tutta la configurazione. OpenAI Responses richiede `openai_responses`. I client Anthropic richiedono `anthropic_messages`. I connettori MCP appartengono alla configurazione attuale `connectors.servers` e i client si collegano tramite `/v1/mcp`.

Prima di modificare un gateway condiviso, prepara il diff minimo per provider, connettori e autorizzazioni. Applica le modifiche solo se ho autorità amministrativa e questa richiesta autorizza le modifiche al gateway. Se non ho tale autorità, indica le modifiche esatte da proporre al proprietario dell'istanza. Non creare né ampliare autorizzazioni senza l'autorizzazione esplicita del proprietario. Conserva tutte le impostazioni esistenti del gateway.

Configura ogni client installato secondo il formato ufficiale attuale e il percorso specifico del sistema operativo:
- Codex CLI e desktop condividono `~/.codex/config.toml` su macOS/Linux e `%USERPROFILE%\.codex\config.toml` su Windows. Imposta il provider Aperture, un modello compatibile, `wire_api = "responses"` e MCP in `mcp_servers`.
- Claude Code usa `ANTHROPIC_BASE_URL` e MCP remoto tramite HTTP. Usa `~/.claude/settings.json` su macOS/Linux e `%USERPROFILE%\.claude\settings.json` su Windows.
- Claude Desktop usa Modalità sviluppatore, Configura inferenza di terze parti, Gateway, Chiave API statica, un URL gateway HTTPS con certificato attendibile e un ID modello individuato per il mio utente. Usa un bridge locale `mcp-remote` per MCP privato sulla tailnet. Trova la configurazione MCP in Impostazioni > Sviluppatore > Modifica configurazione, se disponibile. Altrimenti usa il percorso documentato per il sistema rilevato.
- OpenCode usa lo schema V2 attuale `providers` e `mcp.servers`. La configurazione globale è `~/.config/opencode/opencode.json` su macOS/Linux e `%USERPROFILE%\.config\opencode\opencode.json` su Windows. Imposta `oauth: false` per MCP Aperture. Usa una chiave API segnaposto locale quando richiesta.
- Hermes usa un provider denominato, un trasporto corrispondente all'API del modello e `mcp_servers`. Usa `~/.hermes/config.yaml` su macOS/Linux. Su Windows, controlla `hermes config path`, di solito `%LOCALAPPDATA%\hermes\config.yaml`. Verifica se Hermes Desktop condivide il profilo Hermes locale.

Usa HTTP per il traffico tailnet quando il client lo supporta. L'inferenza Claude Desktop richiede HTTPS con un certificato attendibile. Usa `/v1` salvo che il gateway documenti un percorso diverso.

Riavvia i client configurati. Verifica in Aperture una richiesta modello per client e una chiamata innocua in sola lettura a uno strumento MCP. Riporta i modelli individuati per la mia identità, i client e i file modificati, i risultati della verifica e le eventuali azioni amministrative restanti. Non installare software, non esporre pubblicamente il gateway, non eseguire commit e non pubblicare.
```

## Conclusione

Una configurazione Aperture funzionante dipende da tre elementi: un gateway raggiungibile, un percorso modello compatibile con il protocollo del client e le autorizzazioni per i modelli e i connettori MCP necessari. Gli stessi schemi di configurazione funzionano su macOS, Linux e Windows, ma ciascun client salva le impostazioni in un percorso specifico del sistema operativo.

Individua gli ID dei modelli usando l'identità Tailscale che li utilizzerà. Configura separatamente l'inferenza dei modelli e `/v1/mcp`, poi verifica una richiesta reale e una chiamata a uno strumento in sola lettura. Quando passi a un altro dispositivo o a un'altra istanza Aperture, riutilizza la struttura di questa guida, conferma percorsi e autorizzazioni di quell'istanza e conserva le credenziali nel secret store locale.

## Prossimi passi

**Esercitazione MCP:** Per distinguere un server salvato da una chiamata a uno strumento verificata, leggi [Configurazione di server MCP: autorizzazioni, test degli strumenti e rimozione sicura](/articles/effective-ai-mcp-server-setup/). Per l'architettura self-hosted più ampia, consulta [Flotta ibrida di agenti IA: Tailscale, LiteLLM e Hermes](/articles/hybrid-agentic-ai-fleet-tailscale-litellm-hermes/).
