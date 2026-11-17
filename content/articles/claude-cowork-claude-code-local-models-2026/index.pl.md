---
title: "Claude Cowork i Claude Code z lokalnymi modelami: przewodnik konfiguracji na 2026 rok"
date: 2026-09-22
lastmod: 2026-11-09
toc: true
draft: false
description: "Skonfiguruj Ollama z Claude Desktop i Claude Code przez interfejs API zgodny z Anthropic. Poznaj wybór modeli i funkcje dostępne wyłącznie w chmurze w 2026 roku."
genre: ["Lokalna AI", "Narzędzia AI do programowania", "Samodzielnie hostowana AI", "Narzędzia dla programistów", "Prywatność", "Modele open source", "Automatyzacja", "Sprzęt AI"]
tags: ["claude cowork", "claude code", "lokalne modele claude desktop", "ollama claude code", "anthropic base url", "anthropic_auth_token", "lokalny model claude code", "uruchom claude offline", "lokalny agent programistyczny AI", "ollama launch claude", "claude desktop ollama", "lokalne programowanie z llm", "prywatne programowanie AI", "programowanie AI offline", "lokalny agent AI", "qwen3.8", "model glm w chmurze", "modele z obsługą narzędzi", "konfiguracja claude code", "bezpłatny claude code", "claude bez klucza API", "okno kontekstu lokalnego modelu", "llama.cpp", "ollama cloud", "prywatność programowania AI", "AI bez dostępu do sieci", "narzędzia AI dla devops"]
cover: "/img/cover/claude-cowork-setup-guide-local-models-2026.webp"
coverAlt: "Nowoczesne stanowisko pracy z komputerem wyświetlającym interfejs programistyczny, tabletem i inteligentnymi głośnikami na ciemnoniebieskim tle z kolorowymi akcentami świetlnymi."
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**Narzędzia agentowe Claude działają teraz z modelami na własnym sprzęcie, bez klucza API, abonamentu i przesyłania danych poza komputer.** Ollama udostępnia interfejs API zgodny z Anthropic. Claude Code i Claude Desktop łączą się z nim za pomocą kilku poleceń.

*W wielu poradnikach brakuje jednego ważnego szczegółu. Opisują Claude Cowork, a następnie podają kroki konfigurujące narzędzie wiersza poleceń. To dwie różne integracje, a tylko jedna z nich udostępnia Cowork.*

Ten przewodnik osobno opisuje obie ścieżki, zmienną środowiskową pomijaną w popularnych poradnikach, dobór modeli dla każdej z nich we wrześniu 2026 roku oraz funkcje, które pozostaną dostępne wyłącznie w chmurze niezależnie od konfiguracji.

**Po lekturze:** wybierzesz potrzebną integrację, połączysz ją przez udokumentowaną ścieżkę Ollama i sprawdzisz endpoint jednym testem wywołania narzędzia. Lokalna inferencja utrzymuje żądania modelu na komputerze tylko wtedy, gdy wybierzesz model lokalny i zrezygnujesz z funkcji opartych na chmurze.

## Krótka odpowiedź

**Ollama łączy się z Claude na dwa różne sposoby. Wybór niewłaściwego jest najczęstszym powodem, dla którego po konfiguracji działa terminal, ale nie Cowork.**

| Integracja | Co otrzymujesz | Ścieżka konfiguracji | Platforma |
|---|---|---|---|
| **Claude Desktop** | Cowork, subagenci, wyszukiwanie w sieci, tryb automatyczny | Aplikacja Ollama, następnie **Apps** i **Connect Claude** | **Tylko macOS** |
| **Claude Code** | Agent programistyczny CLI z wywołaniami narzędzi i edycją plików | `ollama launch claude` lub zmienne środowiskowe | macOS, Linux, Windows |

**Jeśli potrzebujesz Cowork, użyj integracji Claude Desktop.** To graficzna konfiguracja w aplikacji Ollama, dostępna tylko w macOS. Obsługa Windows jest wymieniona jako planowana.

**Jeśli chcesz agenta w terminalu, użyj Claude Code.** Wystarczy jedno polecenie.

*Obie opcje są bezpłatne. Kosztują tylko sprzęt i energia elektryczna.*

## Dwie integracje, nie jedna

Źródłem nieporozumień są nazwy. **Claude Cowork to funkcja w Claude Desktop**, a nie osobna aplikacja ani synonim Claude Code.

Dokumentacja Ollama opisuje je na osobnych stronach i w osobnych sekcjach. Claude Desktop znajduje się w sekcji **Assistants**, obok OpenClaw i Hermes. Claude Code widnieje w sekcji **Coding**, obok OpenCode, Cline i Codex CLI.

Różnica ma znaczenie, bo konfiguracje są całkowicie odmienne:

- **Claude Desktop** konfigurujesz w interfejsie aplikacji Ollama. Nie zmieniasz profilu powłoki.
- **Claude Code** konfigurujesz przez zmienne środowiskowe lub pojedyncze polecenie uruchamiające.

Poradnik polecający eksport `ANTHROPIC_BASE_URL`, a następnie uruchomienie `claude`, konfiguruje narzędzie wiersza poleceń. Jeśli po tych krokach oczekujesz interfejsu Cowork, **nic się nie zepsuło. Skonfigurowano inny produkt.**

## Konfiguracja Claude Desktop i Cowork

Ta ścieżka korzysta z aplikacji Ollama, a nie z terminala.

### Wymagania wstępne

- **Zainstalowana aplikacja Ollama** w systemie macOS. Obsługa Windows jest wymieniona jako planowana.
- **Wcześniej pobrany model**, jeśli chcesz działać lokalnie. W przypadku modelu chmurowego zaloguj się do Ollama i włącz modele chmurowe. Niektóre z nich wymagają płatnego planu.
- **Zainstalowany Claude.** Jeśli go brakuje, Ollama zaproponuje pobranie podczas konfiguracji.

### Kroki

1. Otwórz Ollama i wybierz **Apps**.
2. Wybierz **Connect Claude**.
3. Wykonaj instrukcje konfiguracji. Jeśli pojawi się prośba, zainstaluj Claude i uruchom go ponownie.

To cała procedura. Aby później zmienić model, otwórz **Ollama Settings**, przejdź do **Apps**, wybierz modele i naciśnij **Restart Claude**.

### Dostępne funkcje

Dokumentacja Ollama wymienia cztery funkcje obsługiwane przez tę integrację:

- **Cowork**, do wykonywania trudnych zadań
- **Subagenci**, do podziału większych zadań między agentów
- **Web search**, domyślnie udostępniane przez Ollama
- **Auto mode**, w którym agent sam decyduje, kiedy zapytać o zgodę przed wprowadzeniem zmian

*Cowork znajduje się na tej liście. Ta integracja go obsługuje, a integracja wiersza poleceń nie.*

### Rozłączanie

Rozłączenie przywraca poprzednią konfigurację Claude, więc zmiana nie jest destrukcyjna.

- W interfejsie otwórz **Apps**, rozłącz Claude, a następnie uruchom go ponownie, gdy pojawi się prośba.
- W terminalu uruchom `ollama launch claude-desktop --restore`.
- **Zamknięcie Ollama przy połączonym Claude również przywraca jego zwykłą konfigurację.** Jeśli chcesz zachować konfigurację lokalną, pozostaw Ollama uruchomioną.

{{< figure src="claude-desktop-ollama-integration-flow.webp" alt="Diagram pokazujący aplikację Ollama łączącą się z Claude Desktop przez panel Apps, wybór modeli w ustawieniach Ollama i ścieżkę przywracania poprzedniej konfiguracji" >}}

## Konfiguracja Claude Code z CLI

To ścieżka opisywana przez większość poradników i właściwy wybór do pracy w terminalu.

### Metoda jednego polecenia

```bash
ollama launch claude
```

Polecenie ustawia wymagane zmienne środowiskowe, kieruje Claude Code do lokalnej instancji Ollama i uruchamia program. Wybierz model z listy i naciśnij Enter. Aby wskazać model od razu, dodaj flagę:

```bash
ollama launch claude --model qwen3.5
```

*Wrapper ustawia środowisko za Ciebie. Przeczytaj też następną sekcję, bo znajomość tych ustawień ułatwi późniejsze diagnozowanie problemów.*

### Ręczne ustawianie zmiennych środowiskowych

```bash
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434

claude --model qwen3.5
```

**Drugą linię pomijają popularne poradniki.** Ustawienie pustego ciągu w `ANTHROPIC_API_KEY` zapobiega zakłóceniom połączenia lokalnego przez prawdziwy klucz zapisany już w środowisku. Gdy opublikowany poradnik pomija tę linię, czytelnicy z wcześniej wyeksportowanym kluczem napotykają mylący błąd.

Aby nie zmieniać profilu powłoki, przekaż wszystko bezpośrednio w poleceniu:

```bash
ANTHROPIC_AUTH_TOKEN=ollama ANTHROPIC_BASE_URL=http://localhost:11434 ANTHROPIC_API_KEY="" claude --model kimi-k2.7-code:cloud
```

Dwa szczegóły z oficjalnej dokumentacji:

- **`ANTHROPIC_AUTH_TOKEN` zawiera token bearer**, dlatego w trybie lokalnym ma dosłowną wartość `ollama`.
- **Pliki ustawień Claude mają pierwszeństwo przed zmiennymi powłoki.** Jeśli po wyeksportowaniu nowych wartości połączenie działa nieprawidłowo, sprawdź te ustawienia, a następnie uruchom `/status` w Claude Code, aby zobaczyć używany endpoint.

### Bezpośrednie połączenie z Ollama Cloud

W tej ścieżce nie trzeba instalować Ollama. Ustaw klucz API i wskaż Claude Code hostowany endpoint Ollama:

```bash
ANTHROPIC_BASE_URL=https://ollama.com \
ANTHROPIC_AUTH_TOKEN="$OLLAMA_API_KEY" \
ANTHROPIC_API_KEY="" \
claude --model glm-5.3-flash
```

**Ta ścieżka ma jedno ograniczenie.** Dokumentacja Ollama informuje, że hostowane wyszukiwanie w sieci i zaawansowane sterowanie narzędziami nie są w pełni obsługiwane. Podstawowy czat, edycja plików i wywoływanie narzędzi działają z kompatybilnymi modelami.

## Wybór modelu na wrzesień 2026

Oferta modeli znacznie zmieniła się w 2026 roku, więc zalecenia z wiosny warto sprawdzić ponownie.

| Model | Typ | Kontekst | Dlaczego warto wybrać |
|---|---|---|---|
| **Qwen3.8 27B** | Lokalny, 18 GB | 256K | Obecnie najlepszy wszechstronny model lokalny z wizją, wywoływaniem narzędzi i sterowaniem trybem myślenia |
| **Qwen3 Coder Next** | Lokalny, MoE 80B łącznie / 3B aktywne | 256K | Zaprojektowany dla stale działających agentów programistycznych, ma szybki tryb bez myślenia |
| **Qwen3.6 35B A3B** | Lokalny, MoE 35B / 3B aktywne | 262K | Apache 2.0 i wydajność przy ograniczonej pamięci |
| **kimi-k2.7-code:cloud** | Chmurowy | Duży | Chmurowy model do programowania bez wymagań dotyczących lokalnego sprzętu |
| **glm-5.3-flash** | Chmurowy | Duży | Model wskazany w pierwszej kolejności w dokumentacji samego Ollama |

**Jeśli masz odpowiednią ilość pamięci, zacznij od Qwen3.8 27B.** Działa lokalnie z kontekstem 256K, natywną obsługą obrazu, wywoływaniem narzędzi i trybem myślenia przełączanym dla każdego żądania. Karta z co najmniej 24 GB pamięci zapewnia wygodne codzienne użytkowanie.

**Jeśli nie masz takiej pamięci, zacznij od modelu chmurowego.** Połączenie Claude Code z hostowanym modelem nic nie kosztuje na próbę i eliminuje kwestię sprzętu, ale kod opuszcza komputer.

### Uwaga dotycząca modeli trójwartościowych

W naszym **[przewodniku po lokalnej AI](/articles/local-ai-2026-build-your-rig-now/)** opisujemy, jak trójwartościowy Bonsai 2 27B uruchamia pełny model 27B w **5,53 GiB**. Kuszące, by użyć go również tutaj.

**Ten model nie działa w tym przepływie pracy.** Jego trójwartościowe kernele znajdują się w forku llama.cpp od Prism ML, a standardowy Ollama nie odczytuje tych plików. Polecenie `ollama launch claude --model Ternary-Bonsai-2-27B` zakończy się błędem przed rozpoczęciem inferencji. Do Claude Code użyj standardowego pakietu Qwen3.8 27B. Pakiety trójwartościowe zostaw dla środowiska uruchomieniowego, które je obsługuje.

*Wygoda i maksymalna wydajność wymagają tu różnych rozwiązań. Zintegrowane narzędzia oczekują standardowego pliku GGUF.*

## Ustaw kontekst 64K, zanim obwinisz model

Dokumentacja Ollama podaje jedną bezpośrednią wskazówkę dotyczącą pracy z repozytorium: wybierz model i **ustaw okno kontekstu o rozmiarze co najmniej 64K**. Dla większych repozytoriów zwiększ tę wartość.

Claude Code umieszcza w oknie kontekstu treść plików, różnice i wyniki poleceń. Przy małej wartości domyślnej zabraknie miejsca przed końcem zadania. Błąd wygląda wtedy na problem z rozumowaniem, choć przyczyną jest ustawienie.

| Kontekst | Zastosowanie |
|---|---|
| Poniżej 32K | Edycja jednego pliku i krótkie pytania |
| **64K** | Praca z kilkoma plikami w niedużym repozytorium |
| 128K | Większe repozytoria i długie wyniki poleceń |
| 256K | Pełne okno modelu Qwen3.8 27B |

*Jeśli Claude Code traci wątek w połowie zadania, sprawdź ustawienie kontekstu przed zmianą modelu.*

## Sprawdź wywoływanie narzędzi jednym poleceniem

Wywoływanie narzędzi odróżnia agenta od generatora tekstu. Warto sprawdzić, czy działa.

Po uruchomieniu Claude Code poproś go:

```text
Read the current directory and list all files
```

**Jeśli wyświetli rzeczywiste pliki, wywoływanie narzędzi działa.** Jeśli twierdzi, że odczytałby katalog, i opisuje, czego się w nim spodziewa, funkcja nie jest skonfigurowana. Rozmawiasz z modelem czatu z dołączonym promptem programistycznym. Kolejne prompty tego nie naprawią.

Sprawdź kolejno:

1. **Wybierz model z potwierdzoną obsługą narzędzi.** Nie każdy model ją zapewnia, a liczba parametrów nie pozwala rozpoznać tej różnicy.
2. **Sprawdź, czy środowisko wskazuje Ollama.** Uruchom `ollama --version` i potwierdź, że `ANTHROPIC_BASE_URL` wskazuje lokalny endpoint.
3. **Uruchom `/status` w Claude Code.** Bazowy adres lub dane uwierzytelniające w ustawieniach Claude mają pierwszeństwo przed właśnie wyeksportowanymi zmiennymi powłoki.

## Funkcje dostępne wyłącznie w chmurze

Poznaj tę granicę przed zbudowaniem przepływu pracy wokół lokalnej inferencji.

| Funkcja | Lokalne modele | Chmura |
|---|---|---|
| Czat i edycja plików | Tak | Tak |
| Wywoływanie narzędzi | Zależnie od modelu | Tak |
| Subagenci | Tak | Tak |
| Wyszukiwanie w sieci | Zapewnia Ollama | Tak |
| **Cowork** | Przez integrację Claude Desktop | Tak |
| Tryb automatyczny | Przez integrację Claude Desktop | Tak |
| Zaplanowane prompty | Przez `/loop` w Claude Code | Tak |

Praca lokalna ma trzy ograniczenia:

- **Rozumowanie na wielu plikach pogarsza się szybciej niż prędkość.** Lokalny model dobrze obsługuje jeden plik, zadowalająco trzy, a słabo całe repozytorium. Dostosuj rozmiar zadania.
- **Niektóre modele chmurowe wymagają płatnego planu Ollama.** Trzeba też się zalogować i włączyć modele chmurowe.
- **Bezpośrednia ścieżka chmurowa ma ograniczenia funkcji.** Hostowane wyszukiwanie w sieci i zaawansowane sterowanie narzędziami nie są w pełni obsługiwane bez lokalnej instalacji.

*Lokalna inferencja dobrze sprawdza się w ograniczonych, weryfikowalnych zadaniach, a gorzej w rozległych i niejasnych. Dopasuj plan do tego ograniczenia.*

## Automatyzacja

Dwie funkcje pozwalają wyjść poza interaktywne użycie.

### Uruchamianie bez interfejsu w skryptach i CI

Flaga `--yes` pomija interaktywne wybory i w razie potrzeby pobiera model. Wymaga `--model`, a wszystko po `--` trafia bezpośrednio do Claude Code:

```bash
ollama launch claude --model gemma4:cloud --yes -- -p "how does this repository work?"
```

**Zwróć uwagę na uprawnienia.** Claude Code przed większością działań pyta o potwierdzenie, więc tryb bez interfejsu wymaga skonfigurowanych reguł uprawnień lub odizolowanego środowiska. Nie kieruj nadzorowanego agenta na repozytorium, na którym Ci zależy.

### Zaplanowane prompty z `/loop`

W sesji Claude Code polecenie `/loop` uruchamia prompt lub polecenie ukośnikowe w określonym odstępie czasu:

```text
/loop 30m Check my open PRs and summarize their status
/loop 1h Research the latest AI news and summarize key developments
/loop 15m Check for new GitHub issues and triage by priority
```

*Polecenie działa, dopóki sesja pozostaje otwarta. Nie jest usługą działającą w tle i kończy się wraz z sesją.*

## Rozwiązywanie problemów

| Objaw | Prawdopodobna przyczyna | Rozwiązanie |
|---|---|---|
| **Odmowa połączenia** | Ollama nie działa | Uruchom `ollama serve` i sprawdź `curl http://localhost:11434/api/tags` |
| **Model opisuje działania zamiast je wykonywać** | Wybrany model nie obsługuje wywoływania narzędzi | Zmień go na model z potwierdzoną obsługą narzędzi |
| **Używany jest prawdziwy klucz API zamiast lokalnego endpointu** | `ANTHROPIC_API_KEY` jest nadal wyeksportowany | Ustaw pusty ciąg, jak pokazano wyżej |
| **Po konfiguracji brakuje Cowork** | Skonfigurowano Claude Code CLI zamiast Claude Desktop | Użyj przepływu Ollama **Apps** dla Cowork |
| **Generowanie jest wolne** | Kontekst ustawiono zbyt wysoko albo wybrano gęsty model zamiast rzadszego | Zmniejsz kontekst, a następnie wypróbuj model typu mixture of experts |
| **Wyeksportowane zmienne nie działają** | Pliki ustawień Claude mają pierwszeństwo przed zmiennymi powłoki | Sprawdź pliki ustawień, a następnie uruchom `/status` |
| **Żądania w tle kończą się błędem** | Claude Code wybiera mały model do zadań wewnętrznych | Ustaw nadpisanie małego modelu na ten sam model lokalny |

*Dwa z tych siedmiu problemów mają tę samą przyczynę. Większość błędów konfiguracji wynika ze złego endpointu albo modelu bez wywoływania narzędzi.*

## Najważniejsze wnioski

- **Claude Desktop i Claude Code to osobne integracje.** Cowork działa w Claude Desktop i konfiguruje się go na macOS w panelu Ollama **Apps**. Ścieżka CLI nie zapewnia Cowork.
- **Trasę CLI uruchamia jedno polecenie:** `ollama launch claude`. Ręczna konfiguracja wymaga trzech zmiennych. **W wielu poradnikach brakuje `ANTHROPIC_API_KEY=""`.**
- **Nie musisz instalować modelu lokalnie.** Wskaż Claude Code adres `https://ollama.com` i podaj klucz API.
- **Zanim ocenisz model, ustaw kontekst o rozmiarze co najmniej 64K.** Małe okno może przypominać błąd rozumowania.
- **Sprawdź wywoływanie narzędzi jednym żądaniem.** Jeśli model opisuje działania, zamiast je wykonać, masz generator tekstu, a nie agenta.
- **Pakiety Bonsai w wersji trójwartościowej tu nie działają.** Wymagają forka llama.cpp od Prism ML, którego standardowy Ollama nie ładuje.
- **Rozłączenie jest bezpieczne.** Zamknięcie Ollama przywraca poprzednie ustawienia Claude, a w terminalu służy do tego `ollama launch claude-desktop --restore`.

## Następne kroki

1. **Zainstaluj Ollama i pobierz model z potwierdzoną obsługą narzędzi** przed konfiguracją Claude: **[Biblioteka modeli Ollama](https://ollama.com/library)**
2. **Przeczytaj stronę Ollama o Claude Code**, aby poznać aktualne flagi i modele: **[Integracja Claude Code](https://docs.ollama.com/integrations/claude-code)**
3. **Jeśli potrzebujesz Cowork, skorzystaj ze strony Claude Desktop:** **[Integracja Claude Desktop](https://docs.ollama.com/integrations/claude-desktop)**
4. **Dobierz sprzęt przed zakupem** na podstawie kategorii pamięci w naszym przewodniku po lokalnej inferencji: **[Lokalna AI w 2026 roku: model 27B przewyższa Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)**
5. **Sprawdź możliwości mniejszego sprzętu**, jeśli chcesz stale działającego agenta na energooszczędnym urządzeniu: **[Jakie modele AI działają na Raspberry Pi 4 lub 5?](/articles/ai-models-raspberry-pi-4-5/)**

## Powiązane artykuły

| Artykuł | Co opisuje |
|---|---|
| **[Lokalna AI w 2026 roku: model 27B przewyższa Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | Benchmark lokalnej inferencji, kwantyzacja trójwartościowa i wybór sprzętu |
| **[Jakie modele AI działają na Raspberry Pi 4 lub 5?](/articles/ai-models-raspberry-pi-4-5/)** | Lokalna inferencja dla małego asystenta działającego bez przerwy |
| **[Budowa asystenta AI dla Meshtastic chroniącego prywatność](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | Lokalny model sterujący radiem bez dostępu do sieci, z naciskiem na prywatność |
| **[Najlepsze rozszerzenia VS Code do programowania z AI](/articles/best-visual-studio-code-extensions-for-ai/)** | Narzędzia edytora do współpracy z lokalnym agentem programistycznym |

## Źródła

1. [Integracja Claude Code - dokumentacja Ollama](https://docs.ollama.com/integrations/claude-code)
2. [Integracja Claude Desktop - dokumentacja Ollama](https://docs.ollama.com/integrations/claude-desktop)
3. [Biblioteka modeli Ollama](https://ollama.com/library)
4. [Qwen3.8 - biblioteka modeli Ollama](https://ollama.com/library/qwen3.8)
5. [Claude Cowork z lokalnymi modelami - PromptSpace](https://www.promptspace.in/blog/how-to-use-claude-cowork-with-local-models-2026-guide)
6. [Fork llama.cpp od Prism ML - kernele trójwartościowe](https://github.com/PrismML-Eng/llama.cpp)
