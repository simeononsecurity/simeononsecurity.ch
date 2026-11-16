---
title: "Konfiguracja serwera MCP: uprawnienia, testy narzędzi i bezpieczne usuwanie"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Połącz tylko do odczytu jeden serwer dokumentacji MCP, sprawdź jego narzędzia, wykonaj rzeczywisty odczyt i usuń połączenie."
genre: ["Sztuczna inteligencja", "Narzędzia dla programistów"]
tags: ["Konfiguracja serwera MCP", "Protokół kontekstu modeli (MCP)", "Uprawnienia MCP", "MCP w Codex", "MCP w Claude Code", "MCP w OpenCode"]
cover: "/img/cover/effective-ai-mcp-server-setup.webp"
coverAlt: "Klient AI połączony z serwerem dokumentacji tylko do odczytu, z widocznym narzędziem i granicą dostępu"
coverCaption: ""
---

[Wróć do kursu Praktyczny przepływ pracy z AI](/effective-ai-course-start/)

**Użyj serwera MCP, gdy zadanie wymaga powtarzalnego narzędzia lub aktualnych informacji spoza projektu.** Model Context Protocol, czyli MCP, określa wymianę informacji o narzędziach, zasobach i promptach między klientem a serwerem. Wpis serwera sam nie dowodzi, że narzędzie działa. Ta lekcja sprawdza jedno połączenie z dokumentacją tylko do odczytu.

**Cel nauki:** odróżnisz konfigurację od rzeczywistego odczytu MCP i zapiszesz sposób bezpiecznego usunięcia połączenia.

## Najważniejsze informacje

- **Host MCP:** aplikacja AI koordynująca użytkowników, modele, uprawnienia i klientów.
- **Klient MCP:** część protokołu komunikująca się z jednym serwerem.
- **Serwer MCP:** program lub usługa zdalna udostępniająca narzędzia, zasoby lub prompty.
- **Wykrycie narzędzia:** dowód, że w kliencie pojawia się nazwana funkcja.
- **Uruchomienie narzędzia:** dowód rzeczywistego wywołania i zwróconej treści.
- **Zakres uprawnień:** dostęp przyznany przez hosta, serwer, konto i użytkownika.

## Zanim zaczniesz

**Wymagania:** [ćwiczenie z kontekstu i przekazywania pracy](/articles/effective-ai-context-window-management/) oraz aktualna instalacja Codex CLI do opisanego ćwiczenia. Zarezerwuj 35 minut. Poziom średniozaawansowany. Inne agenty kodujące mają osobne instrukcje konfiguracji. Oficjalny [serwer OpenAI Docs MCP](https://learn.chatgpt.com/learn/docs-mcp) udostępnia dokumentację dla programistów tylko do odczytu i nie wymaga przesyłania danych kursu.

**Skorzystaj z syntetycznego laboratorium kursu.** Nie łącz kalendarza, poczty ani systemu produkcyjnego. Odczyt dokumentacji wystarczy, aby poznać stany połączenia.

## Zrozum granice

| Stan | Co potwierdza | Czego nie potwierdza |
|---|---|---|
| **Skonfigurowany** | Istnieje wpis serwera | Dostępności |
| **Połączony** | Klient dotarł do serwera | Dostępności przydatnych narzędzi |
| **Wykryty** | Widać narzędzie o określonej nazwie | Że jego wywołanie się powiedzie |
| **Uruchomiony** | Wywołanie zwróciło treść | Poprawności końcowego zadania |
| **Zweryfikowany** | Źródło i wynik odpowiadają na pytanie | Niezawodności przyszłych wywołań |

**MCP sam nie nadaje uprawnień do konta.** Liczą się też host klienta, serwer, uwierzytelnianie, zakres konta i lokalne ustawienia zatwierdzania. [Specyfikacja MCP](https://modelcontextprotocol.io/specification/2026-07-28) definiuje protokół, a każdy produkt ustala własny interfejs.

**Traktuj wynik serwera jako materiał źródłowy.** Pobrana strona nie zastępuje Twojego zadania ani nie uprawnia do zapisu plików. Definicje narzędzi zużywają też kontekst, więc podłącz tylko serwer potrzebny do tego odczytu i usuń go po ćwiczeniu.

## Połącz serwer tylko do odczytu

**W Codex CLI** wykonaj te polecenia w terminalu. Pierwsze dodaje publiczny serwer dokumentacji. Drugie wyświetla skonfigurowane serwery.

```bash
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex mcp list
```

**Oczekiwany dowód konfiguracji:** lista zawiera `openaiDeveloperDocs`. To potwierdza wyłącznie rejestrację. Uruchom nową sesję Codex w rozpakowanym katalogu laboratorium i sprawdź listę narzędzi MCP poleceniem `/mcp`. Używaj nazw narzędzi zainstalowanej wersji.

**Poproś o rzeczywisty odczyt:**

```text
Użyj serwera MCP dokumentacji dla programistów OpenAI, aby znaleźć aktualne wskazówki AGENTS.md.
Podaj tytuł i URL strony źródłowej oraz dwa punkty istotne dla tego laboratorium. Wymień użyte narzędzie MCP.
Nie edytuj plików.
```
**Sprawdź wynik.** Zwrócona strona powinna opisywać `AGENTS.md` jako wskazówki repozytorium i zawierać dokładny adres źródłowy. Otwórz cytowaną stronę i sprawdź jej temat. Odpowiedź bez wywołania MCP w transkrypcji jest zwykłą odpowiedzią, a nie dowodem wykonania narzędzia.

## Zdiagnozuj jeden problem

**Jeśli `codex mcp list` pokazuje serwer, ale `/mcp` nie pokazuje narzędzi,** rejestracja powiodła się, lecz wykrywanie nie. Uruchom sesję ponownie, sprawdź aktywne serwery przez `/mcp`, konfigurację przez `codex mcp get openaiDeveloperDocs`, a następnie URL serwera i dostęp do sieci. Nie uznawaj konfiguracji za działającą wyłącznie na podstawie wpisu.

**Jeśli narzędzie jest widoczne, ale odczyt się nie udaje,** zapisz błąd i ponów próbę raz po sprawdzeniu łączności. Jeśli kolejne wywołanie zawiedzie, użyj cytowanej oficjalnej strony w przeglądarce jako źródła zastępczego i oznacz ćwiczenie MCP jako nieukończone. Nie wymyślaj wyniku narzędzia.

## Usuń połączenie

**Po odczycie** usuń serwer testowy z Codex CLI i potwierdź, że wpis zniknął.

```bash
codex mcp remove openaiDeveloperDocs
codex mcp list
```

**Oczekiwany dowód usunięcia:** nowa lista nie zawiera `openaiDeveloperDocs`. Uruchom ponownie aktywną sesję Codex przed sprawdzeniem, czy zmieniły się jej dostępne narzędzia. Usunięcie lokalnej definicji nie odbiera oddzielnej zgody konta używanej przez inną usługę.

## Użyj innego klienta

**Claude Code i OpenCode również obsługują MCP.** Skorzystaj z [przewodnika MCP Claude Code](https://code.claude.com/docs/en/mcp) albo [przewodnika MCP OpenCode](https://opencode.ai/docs/mcp-servers/) dla zainstalowanej wersji. Zapisz te same pięć stanów: skonfigurowany, połączony, wykryty, uruchomiony i zweryfikowany. Schemat konfiguracji oraz uprawnienia agentów OpenCode różnią się między wersjami. Przepisuj przykłady z przewodnika zgodnego z instalacją.

**W wariancie wyłącznie przeglądarkowym** przeczytaj [oficjalną stronę AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) i uzupełnij ten sam rejestr weryfikacji. Oznacz wykrywanie i uruchamianie narzędzi jako „nie wykonano”. Ten wariant uczy sprawdzania źródeł, ale nie potwierdza działania MCP.

## Ćwicz i sprawdź

**Twój rezultat:** pięciowierszowy rejestr połączenia: nazwa serwera, nazwa narzędzia, adres źródła, zaobserwowany wynik i dowód usunięcia. Nie umieszczaj tokenów ani identyfikatorów konta na zrzutach ekranu i w logach.

**Warunek ukończenia:** połączona ścieżka jest zaliczona dopiero po rzeczywistym odczycie narzędziem i późniejszym usunięciu konfiguracji. Wariant zastępczy zalicza ćwiczenie ze źródłami, jeśli MCP oznaczono jako niewykonane.

## Sprawdź swoją wiedzę

1. **Pytanie:** czy zapisany wpis serwera MCP dowodzi, że narzędzie działało? **Odpowiedź:** nie. Sprawdź wykrycie, uprawnienia i rzeczywisty odczyt.
2. **Pytanie:** jaki koszt kontekstu powoduje szerokie połączenie MCP? **Odpowiedź:** opisy i schematy narzędzi zużywają część aktywnego kontekstu.

## Rozwiązywanie problemów

- **Nieznane polecenie `codex`:** zainstaluj lub zaktualizuj Codex CLI zgodnie z podłączonym oficjalnym przewodnikiem.
- **Serwer na liście, brak narzędzia:** sprawdź stan sesji i diagnostykę serwera.
- **Wywołanie zwróciło niepowiązaną treść:** zawęź zapytanie i sprawdź stronę źródłową.
- **Usunięcie nie działa:** rozpocznij nową sesję i sprawdź aktywną listę serwerów.

## Następne kroki

**Przejdź do [Weryfikacji wyników AI](/articles/effective-ai-output-verification/).** Więcej rozszerzeń opisuje [przewodnik po wtyczkach i narzędziach MCP Claude Code](/articles/claude-code-plugins-skills-mcp-tools/).

**Nawigacja kursu:** [Wstecz: Zarządzanie kontekstem](/articles/effective-ai-context-window-management/), [Plan kursu](/effective-ai-course-start/).
