---
title: "Tailscale Aperture: konfiguracja klientów AI do inferencji i MCP w 2026 roku"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Kieruj żądania modeli i narzędzia MCP przez Tailscale Aperture. Skonfiguruj Codex, Claude Code, Claude Desktop, OpenCode i Hermes na innym urządzeniu lub bramie."
genre: ["Sztuczna inteligencja", "Narzędzia dla programistów", "Sieci"]
tags: ["Tailscale Aperture", "Konfiguracja Aperture", "Proxy AI", "Brama LLM", "Brama MCP", "Codex Aperture", "Claude Code Aperture", "Claude Desktop Aperture", "OpenCode Aperture", "Hermes Agent Aperture", "Codex MCP", "Claude MCP", "OpenCode MCP", "Hermes MCP", "Proxy inferencji AI", "API Responses", "API Anthropic Messages", "Zdalne MCP", "Streamable HTTP", "Tailscale", "Samodzielnie hostowana AI", "Agenci programistyczni", "Konfiguracja klientów AI"]
cover: "/img/cover/tailscale-aperture-agent-setup.webp"
coverAlt: "Aperture łączy panele klientów z usługami modeli i narzędzi MCP przez oddzielne niebieskie trasy inferencji i zielone trasy narzędzi"
coverCaption: ""
---

## Wprowadzenie

Tailscale Aperture zapewnia klientom AI jedną bramę połączoną z tailnetem do inferencji modeli i narzędzi Model Context Protocol (MCP). Każdy klient musi używać trasy zgodnej z jego protokołem API. Narzędzia MCP korzystają z oddzielnego endpointu, a uprawnienia Aperture określają, do których modeli i konektorów ma dostęp każda tożsamość Tailscale.

Ten poradnik pokazuje konfigurację Codex, Claude Code, Claude Desktop, OpenCode i Hermes w systemach macOS, Linux i Windows. Opisuje ustawienia CLI i aplikacji desktopowych, sprawdzanie identyfikatorów modeli dostępnych dla własnej tożsamości oraz zawiera zanonimizowaną instrukcję do wykorzystania przy konfiguracji innego urządzenia lub instancji Aperture.

**Wybór trasy:** Ścieżki endpointów zależą od bramy i protokołu API. Trasa Responses, taka jak `/codex`, nie obsługuje ruchu Anthropic Messages ani MCP. Potwierdź nazwę hosta bramy i trasę inferencji każdego klienta. Przed zmianą ustawień sprawdź identyfikatory modeli przez własny dostęp do Aperture.

## Najważniejsze informacje

- **Ruch modeli** wymaga trasy API odpowiedniej dla protokołu klienta.
- **Ruch MCP** korzysta z oddzielnego endpointu `/v1/mcp`.
- **Uprawnienia bramy** muszą zezwalać Twojej tożsamości Tailscale na użycie każdego modelu i konektora.
- **Konfiguracja klienta** potwierdza tylko zapis ustawień. Sprawdź rzeczywiste żądanie i wywołanie narzędzia MCP.

## Jak działają trasy

| Zastosowanie | Żądanie klienta | Trasa Aperture | Obsługa trasy |
|---|---|---|---|
| Codex i modele zgodne z Responses | API OpenAI Responses | Zwykle `/v1`. Własna ścieżka, np. `/codex`, zależy od wdrożenia. | Inferencja modeli |
| Inferencja modeli Claude | API Anthropic Messages | Bazowy URL bramy. Aperture obsługuje `/v1/messages` | Inferencja zgodna z Claude |
| Narzędzia MCP | Streamable HTTP MCP | `/v1/mcp` | Narzędzia i zasoby skonfigurowanych konektorów |

{{< figure src="aperture-client-routes.webp" alt="Codex i Hermes korzystają z trasy Responses, Claude z Anthropic Messages, a klienci MCP z oddzielnej trasy /v1/mcp do konektorów Aperture" caption="Inferencja modeli i ruch MCP używają oddzielnych endpointów Aperture" >}}

**Adresy bazowe dostawców:** Aperture dopisuje ścieżki żądań klientów do bazowego URL dostawcy. Ustaw jego `baseurl` na główny adres API. Nie dodawaj `/v1` do bazowego adresu upstream, gdy ścieżka przychodząca już zawiera `/v1`. [Dokumentacja konfiguracji Aperture](https://tailscale.com/docs/aperture/configuration) objaśnia budowanie URL-i, rejestrację modeli i uprawnienia.

## Przygotuj bramę

**Przed edycją** poproś administratora Aperture o następujące wartości:

- **Nazwa hosta bramy:** Używaj `http://` dla większości klientów połączonych z tailnetem. Inferencja Claude Desktop wymaga `https://` i zaufanego certyfikatu.
- **Trasy inferencji:** OpenAI Responses i Anthropic Messages używają różnych formatów żądań.
- **Identyfikatory modeli:** Poniższy endpoint zwraca modele dostępne dla Twojej tożsamości Tailscale. Używaj dokładnych zwróconych identyfikatorów.
- **Uwierzytelnianie:** Sprawdź, czy klient wysyła zastępczy klucz API czy poświadczenia użytkownika.
- **Endpoint MCP:** Zwykle `http://<APERTURE_HOST>/v1/mcp` dla klientów tailnetu. Inferencja Claude Desktop wymaga HTTPS i zaufanego certyfikatu.
- **Uprawnienia:** Sprawdź uprawnienia do modeli i konektorów przypisane Twojej tożsamości Tailscale.

**Dostęp sieciowy:** Urządzenie klienta musi docierać do bramy przez tailnet. Sama nazwa hosta nie daje dostępu do modeli ani narzędzi. Aperture odrzuci żądanie bez pasującego uprawnienia do modelu lub konektora.

### Sprawdź modele dostępne dla użytkownika

**Pobierz listę modeli** na urządzeniu połączonym z tą samą tailnet. Aperture używa tożsamości Tailscale urządzenia i zwraca modele przyznane temu użytkownikowi. Opisuje to [poradnik uprawnień modeli](https://tailscale.com/docs/aperture/how-to/grant-model-access):

```sh
# macOS lub Linux
curl -fsS http://<APERTURE_HOST>/v1/models
```

```powershell
# Windows PowerShell, użyj curl.exe zamiast starego aliasu curl
curl.exe -fsS http://<APERTURE_HOST>/v1/models
```

**Odczytaj wynik:** Każde zwrócone `id` jest identyfikatorem modelu. Sprawdź `metadata.provider.id`, aby rozpoznać dostawcę Aperture. Wybierz model zgodny z formatem API klienta. Claude Desktop wymaga modelu Anthropic Messages. [Katalog modeli Aperture](https://tailscale.com/docs/aperture/reference/chat) pokazuje też identyfikatory dostępne zalogowanemu użytkownikowi.

**Brak modelu:** Jeśli oczekiwany model się nie pojawia, poproś administratora Aperture o sprawdzenie konfiguracji dostawcy i uprawnienia do modelu. Endpoint nie umożliwia użytkownikom samodzielnego przyznawania sobie dostępu.

**Schemat URL:** Tailscale zaleca `http://` dla większości klientów w tej samej tailnet. WireGuard szyfruje ten ruch. Claude Desktop wymaga `https://` i certyfikatu zaufanego przez system operacyjny. Użyj schematu podanego poniżej dla danego klienta.

### Dodaj dostawcę inferencji

**OpenAI Responses:** Dodaj dostawcę upstream do Aperture i włącz format API używany przez klienta. Dla OpenAI dodaj na przykład:

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

**Anthropic Messages:** Użyj głównego adresu API Anthropic, formatu autoryzacji `x-api-key` i zgodności `anthropic_messages`. Identyfikator modelu musi też znajdować się na liście `models` dostawcy. Dodaj na przykład:

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

**Zmiany konfiguracji:** Zastąp symbole zastępcze wartościami upstream. Dodaj fragmenty do istniejącej konfiguracji Aperture i zachowaj resztę pliku. Włącz flagi zgodności dla obsługiwanych API.

**Uprawnienia dostępu:** Aperture kontroluje dostęp do każdego modelu i konektora. Przyznaj użytkownikom Tailscale tylko potrzebne prawa. Ten przykład daje jednemu użytkownikowi dostęp do modelu i konektora:

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

**Uprawnienie modelu:** Użyj identyfikatora dostawcy i modelu we wzorcu. [Poradnik konfiguracji konektorów](https://tailscale.com/docs/aperture/connectors/get-started) pokazuje bieżące `connectors.servers`. Starsza konfiguracja najwyższego poziomu `mcp.servers` jest przestarzała.

### Dodaj konektor MCP

**Konektor MCP:** Aperture łączy się z serwerami MCP upstream i udostępnia ich narzędzia pod `/v1/mcp`:

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

**URL konektora:** Użyj pełnego endpointu MCP serwera upstream. Przyznaj użytkownikowi Tailscale dostęp do `teamtools/**` lub węższego wzorca. [Dokumentacja proxy MCP](https://tailscale.com/docs/aperture/mcp-server) objaśnia wspólny endpoint klienta i działanie konektorów.

## Codex CLI i aplikacja desktopowa

**Wspólne ustawienia:** Codex CLI i aplikacja desktopowa korzystają z tej samej konfiguracji. W macOS i Linux edytuj `~/.codex/config.toml`. W Windows edytuj `%USERPROFILE%\.codex\config.toml` (powłoki rozwijające katalog domowy obsługują też `~/.codex/config.toml`). [Opis aplikacji Codex](https://openai.com/index/introducing-the-codex-app/) mówi, że desktop korzysta z konfiguracji CLI. Ustawienia użytkownika znajdują się w `~/.codex/config.toml`. [Podstawy konfiguracji](https://learn.chatgpt.com/docs/config-file/config-basic) opisują pola dostawcy i MCP. Dodaj dostawcę do tego pliku, uruchom aplikację ponownie i sprawdź, czy dostawca i model są widoczne.

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

**Pola opcjonalne:** Te dwa ustawienia pasują do jednej konfiguracji dostawcy Codex. Zachowaj je tylko wtedy, gdy wymagają ich brama i Codex. Aktualny [poradnik Tailscale dla Codex Aperture](https://tailscale.com/docs/aperture/how-to/use-codex) ich nie zawiera, używa `wire_api = "responses"` i informuje, że Aperture wstawia poświadczenia upstream. Użyj dokładnego URL Responses od administratora bramy. `/codex` zależy od wdrożenia. Domyślną trasą Tailscale jest `/v1`.

**Konfiguracja MCP:** Dodaj serwer do tej samej konfiguracji użytkownika:

```toml
[mcp_servers.aperture]
url = "http://<APERTURE_HOST>/v1/mcp"
enabled = true
```

**Sprawdź Codex:** Uruchom `codex mcp list`, rozpocznij sesję i sprawdź `/mcp`. Lista potwierdza rejestrację. Widoczne narzędzie i udane wywołanie potwierdzają wykrycie i działanie. [Referencja konfiguracji Codex](https://learn.chatgpt.com/docs/config-file/config-reference) opisuje ustawienia dostawcy i MCP.

## Claude Code CLI

**Protokół:** Claude Code używa Anthropic Messages. Wskaż globalnym plikiem Claude Code bramę Aperture zgodną z Anthropic. Użyj `~/.claude/settings.json` w macOS i Linux lub `%USERPROFILE%\.claude\settings.json` w Windows. W PowerShell użyj `$HOME\.claude\settings.json`. Trasa musi obsługiwać `/v1/messages`. Codex Responses korzysta z innego protokołu i trasy. Tailscale zaleca HTTP dla Claude Code w tailnecie, ponieważ WireGuard szyfruje połączenie.

```json
{
  "apiKeyHelper": "echo '-'",
  "env": {
    "ANTHROPIC_BASE_URL": "http://<APERTURE_HOST>"
  }
}
```

**Uwierzytelnianie klienta:** Poradnik Aperture umieszcza symbol zastępczy w `apiKeyHelper`, bo Aperture dodaje poświadczenie upstream. Przy przekazywaniu subskrypcji Claude dostawca Anthropic w Aperture musi przekazać poświadczenie Claude użytkownika. Pozostaw wtedy `ANTHROPIC_API_KEY` i `ANTHROPIC_AUTH_TOKEN` nieustawione. Te zmienne zastępują poświadczenie subskrypcji. Zastosuj aktualne [instrukcje Claude Code Aperture](https://tailscale.com/docs/aperture/how-to/use-claude-code) oraz [poradnik Anthropic o bramach](https://code.claude.com/docs/en/llm-gateway-connect).

**MCP przez HTTP:** Dodaj endpoint:

```sh
claude mcp add --transport http --scope user aperture http://<APERTURE_HOST>/v1/mcp
claude mcp list
```

**Sprawdź Claude Code:** Uruchom sesję i wykonaj `/mcp`. Anthropic zaleca HTTP dla zdalnych serwerów MCP w [dokumentacji MCP](https://code.claude.com/docs/en/mcp).

## Graficzny interfejs Claude Desktop

**Oddzielne ustawienia:** Claude Desktop ma ekran inferencji zewnętrznej. To ustawienie kieruje żądania modeli Claude Desktop przez Aperture. Konfiguracja MCP wymaga osobnego kroku.

1. W Claude Desktop dla macOS lub Windows wybierz **Pomoc > Rozwiązywanie problemów > Włącz tryb dewelopera**. W wersji beta Linux użyj tego menu, jeśli jest dostępne. Uruchom aplikację ponownie, jeśli o to poprosi. Jeśli menu nie ma, zaktualizuj Claude Desktop i sprawdź informacje o wydaniu.
2. Wybierz **Deweloper > Konfiguruj inferencję zewnętrzną**.
3. Ustaw **Typ połączenia** na **Brama**, a **Rodzaj poświadczenia** na **Statyczny klucz API**.
4. Wpisz `https://<APERTURE_HOST>` jako **bazowy URL bramy**. Użyj pełnej nazwy hosta objętej zaufanym certyfikatem TLS.
5. Wpisz niepusty symbol zastępczy, np. `aperture`, jako klucz bramy. Aperture go ignoruje i uwierzytelnia przez tailnet.
6. Pozostaw własne nagłówki inferencji puste.
7. Dodaj włączony model z dokładnym ID zwróconym przez `GET /v1/models` dla Twojej tożsamości Tailscale. Wybierz model Anthropic Messages. Ręcznie wpisz ID, nazwę wyświetlaną i opcjonalny alias poziomu. Claude Desktop nie wyszukuje tu modeli.
8. Wybierz **Zapisz zmiany**, potem **Zastosuj zmiany**. Zamknij Claude Desktop i otwórz go ponownie.

**Sprawdzenie protokołu:** [Poradnik Aperture dla Claude Desktop](https://tailscale.com/docs/aperture/how-to/use-claude-desktop) wskazuje `/v1/messages` jako trasę Anthropic Messages. Nie wpisuj `/codex` ani nie wybieraj połączenia zgodnego z OpenAI.

### Połącz Claude Desktop z MCP

**Prywatny dostęp MCP:** Uruchom lokalny most stdio na tym samym komputerze co Claude Desktop. Dodaj go do lokalnej konfiguracji MCP:

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

**Działanie mostu:** Proces lokalny łączy się z Aperture przez Tailscale. Użyj ścieżki właściwej dla systemu: macOS, `~/Library/Application Support/Claude/claude_desktop_config.json`; Windows, `%APPDATA%\Claude\claude_desktop_config.json`; Linux beta, **Ustawienia > Deweloper > Edytuj konfigurację** i ścieżka otwarta przez Claude Desktop. Ścieżka Linux zależy od pakietu. Uruchom aplikację ponownie, sprawdź listę konektorów i wykonaj nieszkodliwe wywołanie narzędzia. Projekt [`mcp-remote`](https://github.com/punkpeye/mcp-remote) opisuje ten most.

**Zdalne konektory:** Funkcja Ustawienia > Konektory Anthropic wymaga serwera dostępnego z usługi Anthropic. Host dostępny tylko w tailnecie jest prywatny dla Twoich urządzeń. Użyj lokalnego mostu albo skonfiguruj uwierzytelnianie i uprawnienia przed wystawieniem usługi MCP publicznie. Zobacz [poradnik Anthropic o zdalnych konektorach MCP](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp).

## OpenCode CLI i aplikacja desktopowa

**Wspólne ustawienia:** OpenCode CLI i desktop odczytują tę samą konfigurację. Aktualna dokumentacja V2 umieszcza dostawców w mapie `providers`, a serwery MCP w `mcp.servers`. Przykład używa endpointu czatu zgodnego z OpenAI pod `/v1`. Przed użyciem sprawdź obsługę OpenAI Chat Completions przez dostawcę Aperture.

**Konfiguracja globalna:** W macOS i Linux edytuj `~/.config/opencode/opencode.json`. W Windows użyj `%USERPROFILE%\.config\opencode\opencode.json`. Dodaj dostawcę zgodnego z OpenAI i zastąp `<MODEL_ID>` dokładnym ID modelu Aperture. OpenCode obsługuje też `opencode.jsonc` dla komentarzy. [Referencja konfiguracji](https://opencode.ai/docs/config/) wyjaśnia pierwszeństwo ustawień globalnych i projektowych.

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

**Uwierzytelnianie klienta:** `oauth: false` pomija domyślny OAuth OpenCode. Aperture rozpoznaje wywołującego przez Tailscale. OpenCode wymaga wpisu uwierzytelniania dostawcy, więc ustaw `APERTURE_API_KEY=-` lokalnie. Aplikacja desktopowa też musi otrzymać tę zmienną. Jeśli jej nie dziedziczy, uruchom `/connect` i wpisz `-` dla Aperture. Nie zapisuj klucza dostawcy upstream w tym pliku. [Poradnik dostawców](https://opencode.ai/docs/providers/) i [poradnik MCP](https://opencode.ai/docs/mcp-servers/) opisują format. Sprawdź serwer przez `opencode mcp list`, a w aplikacji jego stan przez `/mcps`.

## Hermes CLI i aplikacja desktopowa

**Wspólne ustawienia:** Hermes Agent zapisuje nazwanych dostawców i serwery MCP w `~/.hermes/config.yaml` w macOS i Linux. Natywna instalacja Windows używa `%LOCALAPPDATA%\hermes\config.yaml`. Uruchom `hermes config path`, aby znaleźć aktywny plik. `HERMES_HOME` może zmienić domyślną lokalizację. Hermes Desktop używa lokalnego profilu Hermes. Jeśli łączy się ze zdalną bramą, skonfiguruj Aperture na komputerze z Hermes i sprawdź dostęp do tailnetu. Zobacz [poradnik Hermes Desktop](https://hermes-agent.nousresearch.com/docs/user-guide/desktop).

**Dostawca Responses:** Dodaj nazwanego dostawcę. `api` musi wskazywać endpoint Responses instancji Aperture:

```yaml
providers:
  aperture:
    api: "http://<APERTURE_HOST>/v1"
    transport: codex_responses
    default_model: "<MODEL_ID>"
    # Dodaj key_env tylko wtedy, gdy Aperture wymaga klucza klienta.
    # key_env: APERTURE_API_KEY

model:
  provider: "custom:aperture"
  default: "<MODEL_ID>"
```

**Wybór protokołu:** Dla OpenAI Chat Completions ustaw `transport: chat_completions`. Dla Anthropic Messages wybierz `transport: anthropic_messages` i użyj URL tej bramy. [Poradnik dostawców Hermes](https://hermes-agent.nousresearch.com/docs/integrations/providers) opisuje pola `api`, `transport` i `default_model`.

**Konfiguracja MCP:** Dodaj Aperture MCP do tego samego pliku YAML:

```yaml
mcp_servers:
  aperture:
    url: "http://<APERTURE_HOST>/v1/mcp"
    enabled: true
```

**Sprawdź Hermes:** Uruchom `hermes mcp` i sprawdź połączenia w interaktywnym selektorze. Lokalny Desktop udostępnia ten sam profil. Hermes opisuje [zdalne serwery HTTP MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) i [pełną konfigurację MCP](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference).

## Sprawdź obie ścieżki

**Wykonaj osobne kontrole** inferencji modeli i MCP:

1. Potwierdź połączenie Tailscale i dostęp do bramy. W Claude Desktop sprawdź, czy brama przedstawia zaufany certyfikat TLS.
2. Wyślij krótką instrukcję przez każdego klienta. Sprawdź, czy odpowiednie żądanie pojawia się na liście sesji Aperture.
3. Potwierdź, że wybrany model jest przyznany Twojej tożsamości Tailscale.
4. Otwórz ekran statusu MCP lub listę serwerów klienta. Sprawdź, czy Aperture łączy się i udostępnia oczekiwane narzędzia.
5. Wywołaj narzędzie tylko do odczytu i porównaj wynik ze źródłem upstream.
6. Przy błędzie sprawdź logi Aperture. Zapisana konfiguracja nie dowodzi udanej operacji.

| Objaw | Kontrola |
|---|---|
| Żądanie modelu zwraca 404 lub 405 | Sprawdź trasę i protokół endpointu. Nie używaj `/codex` dla Anthropic Messages ani MCP. |
| Model jest niedostępny | Odpytaj `/v1/models` jako właściwy użytkownik Tailscale. Sprawdź dokładne ID i zgodność API. Poproś administratora o kontrolę brakujących dostawców lub uprawnień. |
| Brak autoryzacji | Sprawdź, czy klient wymaga symbolu zastępczego, tokenu bearer czy przekazywania subskrypcji. Nie kopiuj klucza dostawcy upstream do publicznego pliku. |
| Serwer MCP jest na liście, ale brak narzędzi | Sprawdź `/v1/mcp`, stan i uprawnienia konektora oraz połączenie sieciowe klienta z Aperture. |
| Claude Desktop nie łączy się z prywatnym URL MCP | Użyj lokalnego mostu, np. `mcp-remote`, albo zatwierdzonego publicznego konektora z właściwym uwierzytelnianiem. |

## Odtwórz konfigurację na innym urządzeniu

**Nowe urządzenie:** Zainstaluj tego samego klienta i najpierw połącz urządzenie z tailnetem. Odpytaj `/v1/models`, aby znaleźć modele przyznane jego tożsamości Tailscale. Skopiuj strukturę konfiguracji, ale poświadczenia przechowuj lokalnie. Zastąp `<APERTURE_HOST>`, `<MODEL_ID>` i `<UPSTREAM_MCP_ENDPOINT>` wartościami docelowej instancji. Używaj osobnej trasy dla każdego protokołu API i ustaw `/v1/mcp` dla narzędzi. Na koniec sprawdź żądanie modelu i wywołanie MCP.

**Wiele bram:** Używaj osobnej konfiguracji dla każdej instancji Aperture. Urządzenie potrzebuje trasy Responses dla Codex i Hermes, Anthropic Messages dla Claude i wspólnego endpointu MCP dla narzędzi. Przechowuj klucze w lokalnym magazynie sekretów klienta lub zmiennej środowiskowej. Nie umieszczaj ich we współdzielonych plikach `config.toml`, `opencode.json`, `config.yaml` ani w publicznym repozytorium.

## Instrukcja konfiguracji Aperture do ponownego użycia

**Skopiuj tę zanonimizowaną instrukcję** do asystenta programistycznego. Zastąp symbole zastępcze danymi bramy. Asystent ma odpytwać Aperture jako Twoja tożsamość Tailscale przed wyborem modeli.

```text
Skonfiguruj moją istniejącą bramę Tailscale Aperture i klientów AI zainstalowanych na tym urządzeniu.

Klienci: Codex CLI i desktop, Claude Code, Claude Desktop, OpenCode CLI i desktop, Hermes CLI i desktop.

Najpierw wykryj system operacyjny macOS, Linux lub Windows, ustal aktywną powłokę (np. zsh, bash lub PowerShell) i używaj odpowiednich ścieżek oraz poleceń. Sprawdź aktualną bramę, połączenie Tailscale, wersje klientów i istniejące ustawienia. Przeczytaj aktualną oficjalną dokumentację. Zachowaj niezwiązane ustawienia i wykonaj kopię każdego pliku przed edycją. Nie zgaduj nazw hostów, identyfikatorów modeli, tras API ani poświadczeń. Klucze dostawców upstream trzymaj w Aperture, nie w plikach klientów ani repozytorium.

Sprawdź modele dostępne z tego urządzenia:
1. Odpytaj `http://<APERTURE_HOST>/v1/models` jako tożsamość Tailscale używaną przez moich klientów. Jeśli brama dokumentuje inny adres listy modeli, użyj go.
2. Odczytaj `id` i `metadata.provider.id` każdego modelu. Lista obejmuje modele przyznane mojej tożsamości. Nie używaj listy administratora ani zmyślonych identyfikatorów.
3. Dopasuj format API do klienta. Codex używa OpenAI Responses, klienci Claude Anthropic Messages. OpenCode i Hermes potrzebują zgodnego dostawcy i transportu.
4. W miarę możliwości zachowaj model domyślny klienta. Jeśli trzeba wybrać model, pokaż mi zgodne opcje i zapytaj o wybór. Claude Desktop wymaga ręcznego wpisania dokładnego ID.
5. Jeśli brak odpowiedniego modelu, sprawdź dostawcę i uprawnienia tylko wtedy, gdy mam dostęp administratora. W przeciwnym razie podaj administratorowi wymagany dostęp. Nie przyznawaj dostępu sobie.

Znajdź wdrożenie Aperture i źródło konfiguracji. Nie zakładaj ścieżki ani nie zastępuj całego pliku. OpenAI Responses wymaga `openai_responses`; Anthropic wymaga `anthropic_messages`. Konektory MCP są w aktualnym `connectors.servers`, a klienci łączą się przez `/v1/mcp`.

Przed zmianą współdzielonej bramy przygotuj minimalny diff dostawców, konektorów i uprawnień. Wprowadź go tylko wtedy, gdy mam uprawnienia administracyjne i to żądanie zezwala na zmianę bramy. W przeciwnym razie przekaż właścicielowi instancji dokładne propozycje. Nie twórz ani nie rozszerzaj uprawnień bez wyraźnej zgody właściciela. Zachowaj pozostałe ustawienia bramy.

Skonfiguruj zainstalowanych klientów w aktualnym oficjalnym formacie i ścieżce systemowej:
- Codex CLI i desktop współdzielą `~/.codex/config.toml` w macOS/Linux i `%USERPROFILE%\.codex\config.toml` w Windows. Ustaw dostawcę Aperture, zgodny model, `wire_api = "responses"` i MCP w `mcp_servers`.
- Claude Code używa `ANTHROPIC_BASE_URL` i zdalnego MCP przez HTTP. Użyj `~/.claude/settings.json` w macOS/Linux albo `%USERPROFILE%\.claude\settings.json` w Windows.
- Claude Desktop używa trybu deweloperskiego, ustawień inferencji zewnętrznej, typu Gateway, statycznego klucza API, adresu HTTPS z zaufanym certyfikatem i ID modelu dostępnego dla mojego użytkownika. Dla prywatnego MCP użyj lokalnego mostu `mcp-remote`. Szukaj konfiguracji w Ustawienia > Deweloper > Edytuj konfigurację lub użyj udokumentowanej ścieżki systemowej.
- OpenCode używa schematu V2 `providers` i `mcp.servers`. Globalny plik to `~/.config/opencode/opencode.json` w macOS/Linux lub `%USERPROFILE%\.config\opencode\opencode.json` w Windows. Dla MCP Aperture ustaw `oauth: false` i w razie potrzeby użyj lokalnego zastępczego klucza API.
- Hermes używa nazwanego dostawcy, transportu zgodnego z API modelu oraz `mcp_servers`. Użyj `~/.hermes/config.yaml` w macOS/Linux. W Windows sprawdź `hermes config path`, zwykle `%LOCALAPPDATA%\hermes\config.yaml`. Sprawdź, czy Hermes Desktop korzysta z lokalnego profilu Hermes.

Używaj HTTP dla ruchu tailnetu, jeśli klient to obsługuje. Inferencja Claude Desktop wymaga HTTPS i zaufanego certyfikatu. Używaj `/v1`, chyba że brama określa inną trasę.

Uruchom ponownie klientów. W Aperture sprawdź żądanie modelu dla każdego klienta i nieszkodliwe wywołanie narzędzia MCP tylko do odczytu. Podaj dostępne modele, zmienione pliki i klientów, wyniki weryfikacji oraz pozostałe działania administratora. Nie instaluj oprogramowania, nie udostępniaj bramy publicznie, nie twórz commitów i niczego nie publikuj.
```

## Podsumowanie

Poprawna konfiguracja Aperture wymaga osiągalnej bramy, trasy modelu zgodnej z protokołem klienta oraz uprawnień do potrzebnych modeli i konektorów MCP. Wzorce działają w macOS, Linux i Windows, ale każdy klient przechowuje ustawienia w innej lokalizacji.

Sprawdź identyfikatory modeli jako tożsamość Tailscale, która będzie ich używać. Skonfiguruj osobno inferencję i `/v1/mcp`, a potem przetestuj rzeczywiste żądanie i narzędzie tylko do odczytu. Przy zmianie urządzenia lub instancji Aperture wykorzystaj strukturę poradnika, potwierdź trasy i uprawnienia oraz przechowuj poświadczenia lokalnie.

## Następne kroki

**Ćwiczenia MCP:** Przeczytaj [Konfiguracja serwera MCP: uprawnienia, testy narzędzi i bezpieczne usuwanie](/articles/effective-ai-mcp-server-setup/), aby poznać różnicę między zapisanym serwerem a sprawdzonym wywołaniem narzędzia. Szerszą architekturę znajdziesz w [Hybrydowa flota agentów AI: Tailscale, LiteLLM i Hermes](/articles/hybrid-agentic-ai-fleet-tailscale-litellm-hermes/).
