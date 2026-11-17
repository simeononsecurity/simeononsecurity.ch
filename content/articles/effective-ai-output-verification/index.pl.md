---
title: "Jak weryfikować wyniki AI, źródła, testy i koszty"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Przygotuj zapis akceptacji wyniku AI, sprawdzając źródła, zakres plików, dowody z testów, prywatność i wykorzystanie."
genre: ["Sztuczna inteligencja", "Inżynieria oprogramowania"]
tags: ["weryfikacja wyników AI", "sprawdzanie faktów przez AI", "przegląd agenta programistycznego", "dowody testów AI", "śledzenie kosztów AI", "przegląd człowieka"]
cover: "/img/cover/effective-ai-output-verification.webp"
coverAlt: "Arkusz kontroli porównuje twierdzenie AI z plikiem źródłowym, diffem kodu, wynikami testów i sumą wykorzystania"
coverCaption: ""
---

[Wróć do kursu Praktyczny przepływ pracy z AI](/effective-ai-course-start/)

**Zaakceptuj wynik AI dopiero po sprawdzeniu dowodów odpowiednich do zadania.** Dopracowane wyjaśnienie, skonfigurowane narzędzie i zielony komunikat o testach odpowiadają na różne pytania. Ta lekcja tworzy jeden zapis przeglądu dla warsztatowego laboratorium.

**Cel nauki:** przygotujesz zapis akceptacji źródeł, zakresu plików, testów, prywatności i wykorzystania.

## Najważniejsze wnioski

- **Kontrola źródeł:** porównaj twierdzenie faktyczne z aktualnym, wiarygodnym źródłem.
- **Kontrola zakresu:** sprawdź, które pliki lub systemy uległy zmianie.
- **Kontrola działania:** uruchom testy i odpowiednie przypadki ręczne.
- **Kontrola prywatności:** sprawdź, jakie materiały trafiły do narzędzia lub dostawcy.
- **Kontrola wykorzystania:** zapisz tokeny, wywołania narzędzi i stawkę użytą do obliczenia kosztu.

## Zanim zaczniesz

**Wymagania:** laboratorium kursu, `docs/requirements.md`, lokalny snapshot Git oraz [lekcja MCP](/articles/effective-ai-mcp-server-setup/) albo jej odpowiednik w przeglądarce. Zarezerwuj 40 minut. Poziom trudności jest średni. Użyj laboratorium zmienionego w pierwszym zadaniu z agentem programistycznym. Jeśli pominąłeś edycję, użyj świeżego rozpakowania i oznacz kontrole funkcji jako niezaimplementowane. Nienaruszona wersja bazowa nadal przechodzi dwa pierwotne testy.

## Sprawdź twierdzenie faktyczne

**Twierdzenie:** „Zatwierdzone wartości statusu to `open` i `pending`”. Otwórz `docs/requirements.md`, rewizja 1. Dokument podaje `open` i `done`. Twierdzenie jest błędne. Pewny ton nie zmienia wymagania.

**W przypadku twierdzeń o produktach** korzystaj z aktualnej oficjalnej dokumentacji i zapisz tytuł strony oraz datę przeglądu. Informacja o menu, planie, poleceniu lub limicie kontekstu dezaktualizuje się szybciej niż ogólna zasada przepływu pracy. [Dokumentacja Codex](https://learn.chatgpt.com/docs/codex/cli), [dokumentacja Claude Code](https://code.claude.com/docs/en/overview) i [dokumentacja OpenCode](https://opencode.ai/docs/) opisują obecne interfejsy.

| Twierdzenie | Źródło | Decyzja |
|---|---|---|
| **`open` i `pending`** | Wymaganie laboratorium, rewizja 1 | Odrzuć, zastąp `pending` przez `done` |
| **Liczba bez filtra wynosi 4** | Program bazowy i cztery wpisy JSON | Sprawdź, uruchamiając program |
| **Wykonano odczyt MCP** | Transkrypcja narzędzi sesji | Zaakceptuj tylko, gdy widać wywołanie narzędzia |

## Sprawdź zmianę

**W zadaniu programistycznym** użyj Git, aby wyświetlić zmienione pliki i przeczytać rzeczywisty diff. Nowy plik nieśledzony pojawia się w statusie, choć nie w zwykłym diffie, więc sprawdź oba widoki.

```bash
git status --short
git diff -- task_report.py tests
```

**Oczekiwany zakres:** po zadaniu filtrowania zmieniają się tylko `task_report.py` i ukierunkowane testy. Zmiana w `tasks.json`, `docs/requirements.md` lub ukrytym pliku konfiguracyjnym wymaga wyjaśnienia i osobnego przeglądu. Jeśli nie wykonałeś edycji, nie oczekuj zmian.

## Przetestuj działanie

**Uruchom te same kontrole bazowe i funkcjonalne** z rozpakowanego katalogu laboratorium. Raport agenta o zakończeniu zadania powinien podawać zaobserwowane wyniki tych kontroli.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**W zmienionej kopii** testy obejmują nowe przypadki, wyniki to 4, 2 i 2, a błędna wartość kończy działanie czytelnym błędem i niezerowym kodem wyjścia. W nowej kopii startowej przechodzą tylko dwa testy bazowe, a suma wynosi 4. Zapisz ten stan początkowy oddzielnie.

**Nieudany test funkcji wymaga diagnozy.** Jeśli `open` pokazuje 4, sprawdź, czy argument filtra dociera do funkcji zliczającej i czy program porównuje pole `status` zadania. Nie uznawaj nieudanego testu za zaliczony tylko dlatego, że agent twierdzi, że skończył implementację.

## Sprawdź prywatność i dostęp

**Zapisz, jakie pliki otrzymał agent.** Laboratorium zawiera dane syntetyczne i nie ma w nim tajemnic. Rzeczywisty projekt może zawierać dane logowania, informacje o klientach lub prywatne dokumenty. Zanim udostępnisz wynik, sprawdź prompty, logi, zrzuty ekranu i diffy pod kątem takich wartości.

**Lokalny test potwierdza tylko lokalne działanie.** Nie potwierdza uprawnień konta w chmurze, zakresu serwera MCP ani zachowania wdrożonej usługi. Sprawdź każdą granicę w odpowiednim środowisku.

## Zapisz wykorzystanie i koszty

**Tokeny mierzą objętość wejścia i wyjścia modelu.** Panele produktów różnią się, dlatego korzystaj z danych o wykorzystaniu pokazywanych przez dostawcę. W razie potrzeby oddzielnie zapisuj wywołania narzędzi oraz opłaty za obrazy lub środowiska hostowane. Przed obliczeniem rzeczywistego rachunku sprawdź aktualne stawki.

**Otwórz widok wykorzystania konta, które wykonało zadanie.** Zapisz podane tokeny wejściowe i wyjściowe, model, okres rozliczeniowy i ewentualną kategorię wejścia z pamięci podręcznej. W abonamentach ChatGPT lub Claude limit albo przydział nie jest tym samym co opłata API za zadanie. W przypadku uruchomienia OpenCode przez API lub dostawcę sprawdź użycie lub rozliczenie u tego dostawcy oraz aktualny cennik. Jeśli produkt nie pokazuje tokenów dla zadania, wpisz „niedostępne” i nie wyliczaj opłaty z długości rozmowy.

**Przykładowe obliczenie, nie cennik dostawcy:** 30 000 tokenów wejściowych po 1 USD za milion kosztuje 0,03 USD. 5 000 tokenów wyjściowych po 5 USD za milion kosztuje 0,025 USD. Łączna opłata za model w tym przykładzie wynosi 0,055 USD, przed opłatami za narzędzia lub hosting.

```text
koszt wejścia = tokeny wejściowe / 1 000 000 × stawka wejściowa
koszt wyjścia = tokeny wyjściowe / 1 000 000 × stawka wyjściowa
razem = koszt wejścia + koszt wyjścia + oddzielne opłaty za narzędzia
```

**Zadanie pracownika również zużywa tokeny.** Delegowanie przenosi szczegółowy wynik poza główną rozmowę, ale nie sprawia, że praca jest darmowa. Porównaj koszt z wartością niezależnej kontroli.

**Oddziel kategorie opłat.** Wejście z pamięci podręcznej, nowe wejście, wyjście, wywołania narzędzi i wykonanie hostowane mogą mieć różne stawki. Ten przykład używa tylko stawek dla nowego wejścia i wyjścia. Nie mówi nic o opłacie za abonament ani narzędzie.

## Prowadź zapis akceptacji

| Pole | Przykład po edycji |
|---|---|
| **Źródło** | `docs/requirements.md`, rewizja 1, przeczytano |
| **Zmienione pliki** | `task_report.py` i `tests/test_task_report.py` w `git status --short` |
| **Testy** | Testy bazowe i nowe testy filtra zaliczone, zapisz zaobserwowaną liczbę |
| **Ręczny wynik** | Zaobserwowano `Total tasks: 4`, `2` i `2`, błędną wartość odrzucono |
| **Stan funkcji** | Zaimplementowano `--status open` i `--status done` |
| **Prywatność** | Tylko pliki syntetyczne |
| **Wykorzystanie** | Zapisz dane dostawcy, jeśli są dostępne |
| **Decyzja** | Zaakceptuj dopiero po przejściu kontroli źródła, diffu, testów i prywatności |

**Twój artefakt:** skopiuj ten zapis i wypełnij go po własnym uruchomieniu. Zastąp „zaobserwowano” tylko wynikiem, który widziałeś. Wybierz Akceptuj, gdy wszystkie wymagane kontrole przejdą, Popraw, gdy poprawka ma ograniczony zakres, i Zatrzymaj, gdy źródło, zakres lub dostęp są niejasne.

## Sprawdź swoją wiedzę

1. **Pytanie:** czy zaliczona baza startowa dowodzi, że istnieje wymagana funkcja? **Odpowiedź:** Nie. Po edycji przetestuj nowe zachowanie akceptacji.

2. **Pytanie:** co należy do zapisu akceptacji? **Odpowiedź:** dowody źródłowe, zmienione pliki, kontrole działania, zakres dostępu i zaobserwowane wykorzystanie.

## Rozwiązywanie problemów

- **Brak źródła dla twierdzenia:** oznacz je jako niezweryfikowane i znajdź wiarygodny zapis.
- **Testy przechodzą, ale wynik się różni:** dodaj ręczny przypadek i sprawdź dane.
- **Brak danych o wykorzystaniu:** wpisz „niedostępne” zamiast szacować rzeczywisty koszt.
- **Diff zawiera prywatne dane:** przestań udostępniać wynik i usuń te dane z zapisu ćwiczenia.

## Następne kroki

**Przejdź do [delegowania agentów](/articles/effective-ai-agent-delegation/)**. Szczegóły kosztów i prywatności znajdziesz w artykule o [kierowaniu do dostawców](/articles/openrouter-provider-routing-quality-cost/) oraz [granicy prywatności lokalnej AI](/articles/local-ai-privacy-boundary/).

**Nawigacja kursu:** [Wstecz: konfiguracja MCP](/articles/effective-ai-mcp-server-setup/), [Plan kursu](/effective-ai-course-start/).
