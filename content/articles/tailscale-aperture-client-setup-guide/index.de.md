---
title: "Tailscale Aperture: KI-Clients für Inferenz und MCP im Jahr 2026 konfigurieren"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Leiten Sie Modellanfragen und MCP-Werkzeuge über Tailscale Aperture. Richten Sie Codex, Claude Code, Claude Desktop, OpenCode und Hermes auf einem anderen Gerät oder Gateway ein."
genre: ["Künstliche Intelligenz", "Entwicklerwerkzeuge", "Netzwerke"]
tags: ["Tailscale Aperture", "Aperture einrichten", "KI-Proxy", "LLM-Gateway", "MCP-Gateway", "Codex Aperture", "Claude Code Aperture", "Claude Desktop Aperture", "OpenCode Aperture", "Hermes Agent Aperture", "Codex MCP", "Claude MCP", "OpenCode MCP", "Hermes MCP", "KI-Inferenzproxy", "Responses-API", "Anthropic-Messages-API", "Remote-MCP", "Streamable HTTP", "Tailscale", "selbst gehostete KI", "Programmieragenten", "KI-Clientkonfiguration"]
cover: "/img/cover/tailscale-aperture-agent-setup.webp"
coverAlt: "Aperture verbindet Client-Panels über getrennte blaue Inferenz- und grüne Werkzeugrouten mit Modell- und MCP-Werkzeugdiensten"
coverCaption: ""
---

## Einleitung

Tailscale Aperture stellt KI-Clients ein mit dem Tailnet verbundenes Gateway für Modellinferenz und Model Context Protocol (MCP)-Werkzeuge bereit. Jeder Client muss eine Route verwenden, die zu seinem API-Protokoll passt. MCP-Werkzeuge nutzen einen eigenen Endpunkt. Aperture-Berechtigungen steuern, auf welche Modelle und Konnektoren jede Tailscale-Identität zugreifen darf.

Diese Anleitung zeigt die Konfiguration von Codex, Claude Code, Claude Desktop, OpenCode und Hermes unter macOS, Linux und Windows. Sie behandelt CLI- und Desktop-Einstellungen, erklärt, wie Sie Modell-IDs für Ihre eigene Identität abrufen, und enthält eine anonymisierte Anweisung zur Wiederverwendung beim Einrichten eines weiteren Geräts oder einer anderen Aperture-Instanz.

**Routenwahl:** Die Endpunktpfade hängen vom Gateway und dem jeweiligen API-Protokoll ab. Eine Responses-Route wie `/codex` verarbeitet weder Anthropic-Messages- noch MCP-Verkehr. Prüfen Sie den Gateway-Hostnamen und die Inferenzroute jedes Clients. Rufen Sie Modell-IDs über Ihren eigenen Aperture-Zugang ab, bevor Sie Client-Einstellungen ändern.

## Wichtigste Punkte

- **Modellverkehr** benötigt die API-Route des Client-Protokolls.
- **MCP-Verkehr** nutzt den separaten Endpunkt `/v1/mcp`.
- **Gateway-Berechtigungen** müssen Ihrer Tailscale-Identität Zugriff auf jedes Modell und jeden Konnektor gewähren.
- **Die Client-Konfiguration** belegt nur, dass Einstellungen gespeichert wurden. Prüfen Sie eine echte Anfrage und einen MCP-Werkzeugaufruf.

## So passen die Routen zusammen

| Zweck | Client-Anfrage | Aperture-Route | Dienst der Route |
|---|---|---|---|
| Codex und Responses-kompatible Modelle | OpenAI Responses API | Üblicherweise `/v1`. Ein benutzerdefinierter Pfad wie `/codex` hängt von der Bereitstellung ab. | Modellinferenz |
| Claude-Modellinferenz | Anthropic Messages API | Basis-URL des Gateways. Aperture verarbeitet `/v1/messages` | Claude-kompatible Inferenz |
| MCP-Werkzeuge | Streamable HTTP MCP | `/v1/mcp` | Werkzeuge und Ressourcen konfigurierter Konnektoren |

{{< figure src="aperture-client-routes.webp" alt="Codex und Hermes verwenden eine Responses-Route, Claude Anthropic Messages, und MCP-Clients die separate Route /v1/mcp zu Aperture-Konnektoren" caption="Modellinferenz und MCP-Verkehr verwenden getrennte Aperture-Endpunkte" >}}

**Provider-Wurzeln:** Aperture hängt Client-Anfragepfade an die Basis-URL des Providers an. Setzen Sie `baseurl` des Providers auf die API-Wurzel des Providers. Fügen Sie `/v1` nicht an eine Upstream-Basis-URL an, wenn der eingehende Pfad `/v1` bereits enthält. Die [Aperture-Konfigurationsreferenz](https://tailscale.com/docs/aperture/configuration) erklärt URL-Aufbau, Modellregistrierung und Berechtigungen.

## Gateway vorbereiten

**Fragen Sie vor Änderungen** eine Aperture-Administratorin oder einen Administrator nach diesen Werten:

- **Gateway-Hostname:** Verwenden Sie `http://` für die meisten Clients im Tailnet. Claude-Desktop-Inferenz benötigt `https://` mit einem vertrauenswürdigen Zertifikat.
- **Inferenzrouten:** OpenAI Responses und Anthropic Messages verwenden verschiedene Anfrageformate.
- **Modell-IDs:** Rufen Sie die für Ihre Tailscale-Identität verfügbaren Modelle mit dem folgenden Endpunkt ab. Verwenden Sie die unveränderten IDs, die für diese Identität zurückgegeben werden.
- **Authentifizierung:** Prüfen Sie, ob der Client einen Platzhalter-API-Schlüssel oder Benutzeranmeldedaten sendet.
- **MCP-Endpunkt:** Für Tailnet-Clients meist `http://<APERTURE_HOST>/v1/mcp`. Claude-Desktop-Inferenz benötigt HTTPS mit einem vertrauenswürdigen Zertifikat.
- **Zugriffsberechtigungen:** Prüfen Sie Modell- und Konnektorberechtigungen für Ihre Tailscale-Identität.

**Netzwerkzugriff:** Das Client-Gerät muss das Gateway über das Tailnet erreichen können. Ein Hostname allein gewährt keinen Modell- oder Werkzeugzugriff. Aperture verweigert den Zugriff, wenn keine passende Berechtigung das Modell oder den Konnektor zulässt.

### Verfügbare Modelle für Ihr Benutzerkonto finden

**Rufen Sie die Modellliste ab** auf einem Gerät im selben Tailnet ab. Aperture verwendet die Tailscale-Identität des Geräts und gibt die für dieses Konto freigegebenen Modelle zurück. Weitere Informationen enthält der [Leitfaden zu Modellberechtigungen](https://tailscale.com/docs/aperture/how-to/grant-model-access):

```sh
# macOS oder Linux
curl -fsS http://<APERTURE_HOST>/v1/models
```

```powershell
# Windows PowerShell, curl.exe verwenden, damit nicht der alte curl-Alias greift
curl.exe -fsS http://<APERTURE_HOST>/v1/models
```

**Ergebnis lesen:** Verwenden Sie jede zurückgegebene `id` als Modell-ID. Prüfen Sie `metadata.provider.id`, um den Aperture-Provider zu erkennen. Wählen Sie ein Modell, das das API-Format des Clients unterstützt. Claude Desktop benötigt beispielsweise ein Anthropic-Messages-Modell. Das [Modellverzeichnis](https://tailscale.com/docs/aperture/reference/chat) von Aperture listet ebenfalls die für angemeldete Benutzer verfügbaren Kennungen.

**Modelle fehlen:** Wenn ein erwartetes Modell nicht erscheint, bitten Sie eine Aperture-Administration, Provider-Konfiguration und Modellberechtigung zu prüfen. Über den Endpunkt können Benutzer sich selbst keinen Zugriff gewähren.

**URL-Schema:** Tailscale empfiehlt `http://` für die meisten Clients im selben Tailnet. WireGuard verschlüsselt diesen Datenverkehr. Claude Desktop benötigt `https://` und ein vom Betriebssystem als vertrauenswürdig eingestuftes Zertifikat. Verwenden Sie für jeden Client unten das angegebene Schema.

### Inferenz-Provider hinzufügen

**OpenAI Responses:** Fügen Sie Aperture den Upstream-Provider hinzu und aktivieren Sie das vom Client verwendete API-Format. Für einen OpenAI-Upstream können Sie zum Beispiel diesen Abschnitt ergänzen:

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

**Anthropic Messages:** Verwenden Sie die Anthropic-API-Wurzel, das Autorisierungsformat `x-api-key` und die Kompatibilität `anthropic_messages`. Die Modell-ID muss auch in der `models`-Liste des Providers stehen. Ergänzen Sie zum Beispiel diesen Abschnitt:

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

**Konfigurationsänderungen:** Ersetzen Sie jeden Platzhalter durch Ihre Upstream-Werte. Fügen Sie die Abschnitte in die bestehende Aperture-Konfiguration ein. Behalten Sie alle übrigen Einstellungen der Datei bei. Aktivieren Sie Kompatibilitätsoptionen für die APIs, die Ihr Provider unterstützt.

**Zugriffsberechtigungen:** Aperture kontrolliert den Benutzerzugriff auf jedes Modell und jeden Konnektor. Geben Sie jeder vorgesehenen Tailscale-Identität nur die nötigen Rechte. Dieses Beispiel gewährt einem Benutzer Zugriff auf ein Provider-Modell und einen Konnektor:

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

**Modellberechtigung:** Verwenden Sie die Provider-ID und Modell-ID im Berechtigungsmuster. Der [Leitfaden zur Konnektor-Einrichtung](https://tailscale.com/docs/aperture/connectors/get-started) beschreibt die aktuelle Konfiguration `connectors.servers`. Die ältere Konfiguration auf oberster Ebene `mcp.servers` ist veraltet.

### MCP-Konnektor hinzufügen

**MCP-Konnektor:** Aperture verbindet sich mit Upstream-MCP-Servern und stellt Werkzeuge unter `/v1/mcp` bereit:

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

**Konnektor-URL:** Verwenden Sie den vollständigen MCP-Endpunkt des Upstream-Servers. Geben Sie anschließend Ihrer Tailscale-Identität Zugriff auf `teamtools/**` oder ein engeres Werkzeugmuster. Die [MCP-Proxy-Referenz](https://tailscale.com/docs/aperture/mcp-server) erläutert den einzelnen Client-Endpunkt und das Verhalten der Konnektoren.

## Codex CLI und Desktop-App

**Gemeinsame Einstellungen:** Codex CLI und Desktop-App verwenden dieselbe Konfiguration. Bearbeiten Sie unter macOS und Linux `~/.codex/config.toml`. Unter Windows bearbeiten Sie `%USERPROFILE%\.codex\config.toml` (in Shells, die das Home-Verzeichnis auflösen, funktioniert auch `~/.codex/config.toml`). Die [Codex-App-Übersicht](https://openai.com/index/introducing-the-codex-app/) sagt, dass die Desktop-App die Codex-CLI-Konfiguration übernimmt. Codex-Benutzereinstellungen liegen in `~/.codex/config.toml`. Die Dokumentation zu den [Konfigurationsgrundlagen](https://learn.chatgpt.com/docs/config-file/config-basic) beschreibt Provider- und MCP-Felder auf Benutzerebene. Fügen Sie den Provider in diese Datei ein, starten Sie die App neu und prüfen Sie, ob Provider und Modell in der Oberfläche erscheinen.

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

**Optionale Felder:** Diese beiden Werte entsprechen einer Codex-Provider-Konfiguration. Behalten Sie sie nur bei, wenn Gateway und Codex-Konfiguration sie erfordern. Der aktuelle [Tailscale-Leitfaden zu Codex Aperture](https://tailscale.com/docs/aperture/how-to/use-codex) lässt sie weg, verwendet `wire_api = "responses"` und erklärt, dass Aperture Upstream-Anmeldedaten einfügt. Verwenden Sie die genaue Responses-URL Ihrer Gateway-Administration. `/codex` ist eine deploymentspezifische Route. Tailscales dokumentierter Standardpfad ist `/v1`.

**MCP-Konfiguration:** Fügen Sie den Server derselben Benutzerkonfiguration hinzu:

```toml
[mcp_servers.aperture]
url = "http://<APERTURE_HOST>/v1/mcp"
enabled = true
```

**Codex prüfen:** Führen Sie `codex mcp list` aus, starten Sie eine neue Sitzung und prüfen Sie `/mcp`. Die Serverliste belegt die Registrierung. Ein angezeigtes Werkzeug und ein erfolgreicher Aufruf belegen Erkennung und Ausführung. Die [Codex-Konfigurationsreferenz](https://learn.chatgpt.com/docs/config-file/config-reference) dokumentiert Provider- und MCP-Benutzereinstellungen.

## Claude Code CLI

**Protokoll:** Claude Code verwendet Anthropic Messages. Richten Sie die globale Claude-Code-Einstellungsdatei auf das Anthropic-kompatible Aperture-Gateway. Verwenden Sie `~/.claude/settings.json` unter macOS und Linux oder `%USERPROFILE%\.claude\settings.json` unter Windows. In PowerShell verwenden Sie den entsprechenden Pfad `$HOME\.claude\settings.json`. Die Route muss `/v1/messages` bereitstellen. Codex Responses nutzt ein anderes Protokoll und eine andere Route. Tailscale empfiehlt HTTP für Claude Code im Tailnet, weil WireGuard die Verbindung verschlüsselt.

```json
{
  "apiKeyHelper": "echo '-'",
  "env": {
    "ANTHROPIC_BASE_URL": "http://<APERTURE_HOST>"
  }
}
```

**Client-Authentifizierung:** Der Aperture-Client-Leitfaden verwendet in `apiKeyHelper` einen Platzhalter, weil Aperture die Upstream-Anmeldedaten einfügt. Für die Weitergabe eines Claude-Abos muss der Anthropic-Provider von Aperture die Claude-Anmeldedaten des Benutzers weiterleiten. Lassen Sie in diesem Fall `ANTHROPIC_API_KEY` und `ANTHROPIC_AUTH_TOKEN` ungesetzt. Diese Variablen ersetzen die Abo-Anmeldedaten. Folgen Sie den aktuellen [Claude-Code-Aperture-Anweisungen](https://tailscale.com/docs/aperture/how-to/use-claude-code) für Ihre Claude-Code-Version sowie dem [Anthropic-Leitfaden zu Gateways](https://code.claude.com/docs/en/llm-gateway-connect) zu Authentifizierungsoptionen.

**MCP über HTTP:** Fügen Sie den Endpunkt mit diesen Befehlen hinzu:

```sh
claude mcp add --transport http --scope user aperture http://<APERTURE_HOST>/v1/mcp
claude mcp list
```

**Claude Code prüfen:** Starten Sie eine Sitzung und führen Sie `/mcp` aus, um die Verbindung zu bestätigen. Anthropic empfiehlt in seiner [MCP-Dokumentation](https://code.claude.com/docs/en/mcp) HTTP für entfernte MCP-Server.

## Grafische Oberfläche von Claude Desktop

**Getrennte Einstellungen:** Claude Desktop hat einen eigenen Bildschirm für Inferenz von Drittanbietern. Diese Einstellung leitet Claude-Desktop-Modellanfragen über Aperture. Die MCP-Konfiguration erfolgt separat.

1. Wählen Sie in Claude Desktop unter macOS oder Windows **Hilfe > Fehlerbehebung > Entwicklermodus aktivieren**. Verwenden Sie in der Linux-Beta dasselbe Menü, falls vorhanden. Starten Sie die App bei Aufforderung neu. Fehlt das Menü, aktualisieren Sie Claude Desktop und lesen Sie die plattformspezifischen Versionshinweise.
2. Wählen Sie **Entwickler > Inferenz von Drittanbietern konfigurieren**.
3. Setzen Sie **Verbindungstyp** auf **Gateway** und **Anmeldedatentyp** auf **Statischer API-Schlüssel**.
4. Geben Sie `https://<APERTURE_HOST>` als **Gateway-Basis-URL** ein. Verwenden Sie den vollständigen Hostnamen, der vom vertrauenswürdigen TLS-Zertifikat abgedeckt wird.
5. Geben Sie einen nicht leeren Platzhalter wie `aperture` als Gateway-Schlüssel ein. Aperture ignoriert den Platzhalter und authentifiziert über das Tailnet.
6. Lassen Sie benutzerdefinierte Inferenz-Header leer.
7. Fügen Sie ein aktiviertes Modell mit einer exakten ID hinzu, die `GET /v1/models` für Ihre Tailscale-Identität zurückgibt. Filtern Sie nach einem Anthropic-Messages-Modell. Geben Sie Modell-ID, Anzeigename und optionalen Tarifalias manuell ein. Claude Desktop sucht Modelle auf diesem Bildschirm nicht automatisch.
8. Wählen Sie **Änderungen speichern** und anschließend **Änderungen anwenden**. Beenden Sie Claude Desktop und öffnen Sie es erneut.

**Protokoll prüfen:** Der [Aperture-Leitfaden für Claude Desktop](https://tailscale.com/docs/aperture/how-to/use-claude-desktop) sagt, dass Claude Desktop Anthropic Messages unter `/v1/messages` verwendet. Geben Sie nicht die Codex-Route `/codex` ein und wählen Sie keinen OpenAI-kompatiblen Verbindungstyp.

### Claude Desktop mit MCP verbinden

**Privater MCP-Zugriff:** Führen Sie auf demselben Computer wie Claude Desktop eine lokale stdio-Brücke aus. Ergänzen Sie die lokale MCP-Konfiguration von Claude Desktop um:

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

**Funktionsweise der Brücke:** Der lokale Prozess erreicht Aperture über die Tailscale-Verbindung des Computers. Verwenden Sie den Konfigurationspfad Ihres Betriebssystems: macOS, `~/Library/Application Support/Claude/claude_desktop_config.json`; Windows, `%APPDATA%\Claude\claude_desktop_config.json`; Linux-Beta, öffnen Sie **Einstellungen > Entwickler > Konfiguration bearbeiten** und nutzen Sie den von Claude Desktop geöffneten Pfad. Der Linux-Pfad hängt vom Paket ab. Starten Sie Claude Desktop neu, prüfen Sie die Konnektorliste und führen Sie einen unkritischen Werkzeugaufruf aus. Das [`mcp-remote`-Projekt](https://github.com/punkpeye/mcp-remote) beschreibt diese lokale Fernbrücke.

**Remote-Konnektoren:** Der Ablauf Einstellungen > Konnektoren von Anthropic benötigt einen Remote-Server, den der Anthropic-Dienst erreichen kann. Ein nur im Tailnet verfügbarer Hostname ist für Ihre Geräte privat. Verwenden Sie für den privaten Endpunkt daher die lokale Brücke. Wenn Sie einen öffentlichen MCP-Dienst bereitstellen, konfigurieren Sie vor dem Hinzufügen als Cloud-Konnektor Authentifizierung und Berechtigungen. Siehe Anthropics [Leitfaden zu Remote-MCP-Konnektoren](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp).

## OpenCode CLI und Desktop-App

**Gemeinsame Einstellungen:** OpenCode CLI und Desktop-App lesen dieselbe OpenCode-Konfiguration. Die aktuelle OpenCode-V2-Dokumentation verwendet die Map `providers` für benutzerdefinierte Provider und speichert MCP-Server unter `mcp.servers`. Dieses Beispiel verwendet den OpenAI-kompatiblen Chat-Endpunkt unter `/v1`. Prüfen Sie, ob Ihr Aperture-Provider OpenAI Chat Completions unterstützt, bevor Sie diesen Modellpfad verwenden.

**Globale Konfiguration:** Bearbeiten Sie unter macOS und Linux `~/.config/opencode/opencode.json`. Verwenden Sie unter Windows `%USERPROFILE%\.config\opencode\opencode.json`. Fügen Sie einen OpenAI-kompatiblen Provider hinzu und ersetzen Sie `<MODEL_ID>` durch die genaue Aperture-Modell-ID. OpenCode akzeptiert im selben Verzeichnis auch `opencode.jsonc` mit Kommentaren. Die [Konfigurationsreferenz](https://opencode.ai/docs/config/) erklärt die Rangfolge zwischen globalen und Projekt-Einstellungen.

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

**Client-Authentifizierung:** `oauth: false` überspringt den standardmäßigen OAuth-Ablauf von OpenCode. Aperture erkennt den Aufrufer über Tailscale. OpenCode benötigt außerdem einen Provider-Anmeldeeintrag. Setzen Sie daher `APERTURE_API_KEY=-` in der lokalen Umgebung. Auch die Desktop-App muss die Variable erhalten. Falls sie die Shell-Umgebung nicht übernimmt, führen Sie in der App `/connect` aus und geben Sie für Aperture `-` ein. Speichern Sie den Upstream-Provider-Schlüssel nicht in dieser Datei. OpenCodes [Provider-Leitfaden](https://opencode.ai/docs/providers/) und [MCP-Leitfaden](https://opencode.ai/docs/mcp-servers/) erläutern das aktuelle Format. Prüfen Sie den Server mit `opencode mcp list` und seinen Status in der App mit `/mcps`.

## Hermes CLI und Desktop-App

**Gemeinsame Einstellungen:** Hermes Agent speichert benannte Provider und MCP-Server unter `~/.hermes/config.yaml` auf macOS und Linux. Native Windows-Installationen verwenden `%LOCALAPPDATA%\hermes\config.yaml`. Führen Sie `hermes config path` aus, um die aktive Datei zu bestätigen. `HERMES_HOME` kann den Standardspeicherort ändern. Hermes Desktop lokal verwendet dasselbe Hermes-Verzeichnis und Profil wie die CLI. Wenn Desktop eine entfernte Hermes-Gateway-Instanz nutzt, konfigurieren Sie Aperture auf dem Hermes-Rechner und prüfen Sie, ob der Server das Tailnet erreicht. Der [Hermes-Desktop-Leitfaden](https://hermes-agent.nousresearch.com/docs/user-guide/desktop) beschreibt lokale und entfernte Einrichtungen.

**Responses-Provider:** Fügen Sie einen benannten Provider hinzu. `api` muss dem Responses-Endpunkt Ihrer Aperture-Instanz entsprechen:

```yaml
providers:
  aperture:
    api: "http://<APERTURE_HOST>/v1"
    transport: codex_responses
    default_model: "<MODEL_ID>"
    # key_env nur hinzufügen, wenn Ihre Aperture-Konfiguration einen Client-Schlüssel benötigt.
    # key_env: APERTURE_API_KEY

model:
  provider: "custom:aperture"
  default: "<MODEL_ID>"
```

**Protokollauswahl:** Setzen Sie für OpenAI Chat Completions `transport: chat_completions`. Wählen Sie für Anthropic Messages `transport: anthropic_messages` und verwenden Sie die Anthropic-Messages-Gateway-URL. Hermes verwendet laut aktuellem [Provider-Leitfaden](https://hermes-agent.nousresearch.com/docs/integrations/providers) für benannte Provider die Felder `api`, `transport` und `default_model`.

**MCP-Konfiguration:** Fügen Sie Aperture MCP in derselben YAML-Datei hinzu:

```yaml
mcp_servers:
  aperture:
    url: "http://<APERTURE_HOST>/v1/mcp"
    enabled: true
```

**Hermes prüfen:** Führen Sie `hermes mcp` aus und prüfen Sie jede Verbindung in der interaktiven Serverauswahl. Hermes Desktop lokal verwendet dasselbe Profil. Hermes dokumentiert [entfernte HTTP-MCP-Server](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) und die vollständige [MCP-Konfigurationsreferenz](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference).

## Beide Pfade prüfen

**Führen Sie getrennte Prüfungen** für Modellinferenz und MCP aus:

1. Bestätigen Sie Tailscale-Konnektivität und Erreichbarkeit des Gateways. Prüfen Sie bei Claude Desktop, ob das Gateway ein vertrauenswürdiges TLS-Zertifikat bereitstellt.
2. Senden Sie über jeden konfigurierten Client eine kurze Eingabe. Prüfen Sie, ob eine passende Anfrage in der Aperture-Sitzungsliste erscheint.
3. Bestätigen Sie, dass die ausgewählte Modell-ID einem Modell entspricht, das für Ihre Tailscale-Identität freigegeben ist.
4. Öffnen Sie den MCP-Statusbildschirm oder den Listenbefehl jedes Clients. Prüfen Sie, ob der Aperture-Server verbunden ist und die erwarteten Werkzeuge bereitstellt.
5. Rufen Sie ein schreibgeschütztes Werkzeug auf. Vergleichen Sie den Inhalt mit der Upstream-Quelle.
6. Prüfen Sie bei fehlgeschlagenen Modell- oder Werkzeugaufrufen die Aperture-Protokolle. Eine gespeicherte Konfiguration beweist keine erfolgreiche Anfrage.

| Symptom | Prüfung |
|---|---|
| Modellanfrage ergibt 404 oder 405 | Prüfen Sie Route und Protokoll des Client-Endpunkts. Verwenden Sie `/codex` nicht für Anthropic Messages oder MCP. |
| Modell nicht verfügbar | Rufen Sie `/v1/models` als vorgesehene Tailscale-Identität ab. Prüfen Sie, ob die genaue ID erscheint und zum API-Format des Clients passt. Bitten Sie eine Administration, fehlende Provider-Einträge oder Berechtigungen zu prüfen. |
| Anfrage nicht autorisiert | Prüfen Sie, ob der Client einen Platzhalter, Bearer-Token oder Abo-Weitergabe benötigt. Kopieren Sie einen Upstream-Provider-Schlüssel niemals in eine öffentliche Projektdatei. |
| MCP-Server ist aufgelistet, aber es erscheinen keine Werkzeuge | Prüfen Sie `/v1/mcp`, den Zustand des Konnektors, dessen Berechtigungen und den Netzwerkpfad des Clients zu Aperture. |
| Claude Desktop erreicht keine private MCP-URL | Verwenden Sie eine lokale Brücke wie `mcp-remote` oder einen genehmigten öffentlichen Konnektor mit passender Authentifizierung. |

## Einrichtung auf einem anderen Gerät wiederholen

**Neues Gerät:** Installieren Sie denselben Client und verbinden Sie zuerst das Gerät mit dem Tailnet. Rufen Sie `/v1/models` vom neuen Gerät ab, um die für dessen Tailscale-Identität freigegebenen Modelle zu finden. Übernehmen Sie die Konfigurationsstruktur, aber speichern Sie Anmeldedaten lokal. Ersetzen Sie `<APERTURE_HOST>`, `<MODEL_ID>` und `<UPSTREAM_MCP_ENDPOINT>` durch Werte der Ziel-Aperture-Instanz. Verwenden Sie pro API-Protokoll einen eigenen Endpunkt und konfigurieren Sie für Werkzeugverkehr den Pfad `/v1/mcp`. Prüfen Sie abschließend eine Modellanfrage und einen MCP-Werkzeugaufruf.

**Mehrere Gateways:** Verwenden Sie für jede Aperture-Instanz eine eigene Konfiguration. Ein Gerät benötigt einen Responses-Endpunkt für Codex und Hermes, einen Anthropic-Messages-Endpunkt für Claude und den MCP-Aggregationsendpunkt für Werkzeuge. Speichern Sie API-Anmeldedaten im lokalen Geheimnisspeicher des Clients oder in einer Umgebungsvariable. Kopieren Sie keine API-Schlüssel in gemeinsam genutzte Dateien wie `config.toml`, `opencode.json`, `config.yaml` oder in ein öffentliches Repository.

## Wiederverwendbare Aperture-Anweisung

**Kopieren Sie diese anonymisierte Anweisung** in Ihren Programmierassistenten. Ersetzen Sie die Platzhalter durch Ihre Gateway-Daten. Der Assistent muss Aperture als Ihre Tailscale-Identität abfragen, bevor er Modell-IDs auswählt.

```text
Konfiguriere mein vorhandenes Tailscale-Aperture-Gateway und die auf diesem Gerät installierten KI-Clients.

Clients im Umfang: Codex CLI und Desktop, Claude Code, Claude Desktop, OpenCode CLI und Desktop, Hermes CLI und Desktop.

Ermittle zuerst, ob dieses Gerät macOS, Linux oder Windows nutzt, welches Shell-Programm aktiv ist (zum Beispiel zsh, bash oder PowerShell), und verwende durchgehend die Pfade und Befehlssyntax dieser Plattform. Prüfe zuerst das aktuelle Gateway, die Tailscale-Verbindung, Client-Versionen und vorhandene Client-Einstellungen. Lies die aktuelle offizielle Dokumentation. Bewahre nicht zugehörige Einstellungen und sichere jede Datei vor der Bearbeitung. Rate keine Hostnamen, Modell-IDs, API-Routen oder Anmeldedaten. Speichere Upstream-Provider-Schlüssel in Aperture, nicht in Client-Dateien oder diesem Repository.

Ermittle verfügbare Modelle von diesem mit Tailscale verbundenen Gerät aus:
1. Frage `http://<APERTURE_HOST>/v1/models` mit der Tailscale-Identität meiner Clients ab. Verwende die dokumentierte benutzerdefinierte URL der Gateway-Modellliste, falls sie abweicht.
2. Lies von jedem Modell `id` und `metadata.provider.id`. Die Liste zeigt Modelle, die für meine Identität freigegeben sind. Verwende weder die Modellliste einer Administration noch erfundene IDs.
3. Ordne jedem Client ein Modell mit passender API-Kompatibilität zu. Codex verwendet OpenAI Responses. Claude-Clients verwenden Anthropic Messages. OpenCode und Hermes benötigen einen passend konfigurierten Provider und Transport.
4. Verwende nach Möglichkeit das vorhandene Standardmodell eines Clients. Wenn ein Client einen Standard benötigt und ich keine Präferenz habe, zeige mir die kompatiblen Modelle und frage nach meiner Auswahl. Claude Desktop erfordert die manuelle Eingabe der exakten Modell-ID.
5. Wenn der Endpunkt kein geeignetes Modell liefert, prüfe Provider-Konfiguration und Berechtigungen nur, wenn ich Admin-Zugriff habe. Andernfalls nenne den Modellzugriff, den eine Administration ergänzen muss. Gewähre dir selbst keinen Zugriff.

Finde die Aperture-Bereitstellung und die Quelle ihrer Konfiguration. Nimm keinen Dateipfad an und ersetze nicht die gesamte Konfiguration. OpenAI Responses benötigt `openai_responses`. Anthropic-Clients benötigen `anthropic_messages`. MCP-Konnektoren gehören in die aktuelle `connectors.servers`-Konfiguration. Clients verbinden sich über `/v1/mcp`.

Erstelle vor Änderungen an einem gemeinsam genutzten Gateway einen minimalen Diff für Provider, Konnektoren und Berechtigungen. Wende ihn nur an, wenn ich Admin-Rechte habe und diese Anfrage Gateway-Änderungen erlaubt. Fehlen mir die Rechte, nenne dem Instanzinhaber die konkreten vorgeschlagenen Änderungen. Erstelle oder erweitere keine Berechtigung ohne ausdrückliche Zustimmung des Inhabers. Bewahre alle bestehenden Gateway-Einstellungen.

Konfiguriere jeden installierten Client im aktuellen offiziellen Format und am betriebssystemspezifischen Speicherort:
- Codex CLI und Desktop teilen `~/.codex/config.toml` unter macOS/Linux und `%USERPROFILE%\.codex\config.toml` unter Windows. Setze den Aperture-Provider, ein kompatibles Modell, `wire_api = "responses"` und MCP unter `mcp_servers`.
- Claude Code nutzt `ANTHROPIC_BASE_URL` und Remote-HTTP-MCP. Verwende `~/.claude/settings.json` unter macOS/Linux und `%USERPROFILE%\.claude\settings.json` unter Windows.
- Claude Desktop nutzt Entwicklermodus, Drittanbieter-Inferenz konfigurieren, Gateway, statischen API-Schlüssel, eine HTTPS-Gateway-URL mit vertrauenswürdigem Zertifikat und eine für mein Benutzerkonto abgerufene Modell-ID. Verwende für privates Tailnet-MCP eine lokale `mcp-remote`-Brücke. Suche die MCP-Konfiguration unter Einstellungen > Entwickler > Konfiguration bearbeiten, falls verfügbar. Verwende andernfalls den dokumentierten Pfad des erkannten Betriebssystems.
- OpenCode nutzt das aktuelle V2-Schema `providers` und `mcp.servers`. Die globale Konfiguration liegt unter `~/.config/opencode/opencode.json` auf macOS/Linux und `%USERPROFILE%\.config\opencode\opencode.json` unter Windows. Setze für Aperture-MCP `oauth: false`. Verwende bei Bedarf lokal einen Platzhalter-API-Schlüssel.
- Hermes verwendet einen benannten Provider, einen zur Modell-API passenden Transport und `mcp_servers`. Verwende `~/.hermes/config.yaml` unter macOS/Linux. Prüfe unter Windows `hermes config path`, meist `%LOCALAPPDATA%\hermes\config.yaml`. Prüfe, ob Hermes Desktop das lokale Hermes-Profil nutzt.

Verwende für Tailnet-Verkehr HTTP, sofern der Client es unterstützt. Claude-Desktop-Inferenz benötigt HTTPS mit vertrauenswürdigem Zertifikat. Verwende `/v1`, sofern dieses Gateway keine andere Route dokumentiert.

Starte konfigurierte Clients neu. Prüfe in Aperture eine Modellanfrage pro Client und einen ungefährlichen, schreibgeschützten MCP-Werkzeugaufruf. Berichte die für meine Identität abgerufenen Modelle, geänderte Clients und Dateien, Prüfergebnisse und verbleibende Admin-Schritte. Installiere keine Software, mache das Gateway nicht öffentlich, committe nichts und veröffentliche nichts.
```

## Fazit

Eine funktionierende Aperture-Einrichtung benötigt drei Dinge: ein erreichbares Gateway, eine Modellroute passend zum Client-Protokoll und Berechtigungen für die benötigten Modelle und MCP-Konnektoren. Dieselben Konfigurationsmuster funktionieren unter macOS, Linux und Windows, aber jeder Client speichert seine Einstellungen an einem eigenen betriebssystemspezifischen Ort.

Rufen Sie Modell-IDs als die Tailscale-Identität ab, die sie verwenden wird. Konfigurieren Sie Modellinferenz und `/v1/mcp` getrennt. Prüfen Sie anschließend eine echte Anfrage und einen schreibgeschützten Werkzeugaufruf. Übernehmen Sie beim Wechsel zu einem anderen Gerät oder einer anderen Aperture-Instanz die Struktur dieser Anleitung, prüfen Sie die Routen und Berechtigungen dieser Instanz und speichern Sie Anmeldedaten im lokalen Geheimnisspeicher.

## Nächste Schritte

**MCP-Praxis:** Lesen Sie [MCP-Server einrichten: Berechtigungen, Werkzeugtests und sichere Entfernung](/articles/effective-ai-mcp-server-setup/), um gespeicherte Server von verifizierten Werkzeugaufrufen zu unterscheiden. Die umfassendere selbst gehostete Architektur finden Sie unter [Hybride KI-Agentenflotte: Tailscale, LiteLLM und Hermes](/articles/hybrid-agentic-ai-fleet-tailscale-litellm-hermes/).
