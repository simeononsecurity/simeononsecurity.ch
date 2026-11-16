---
title: "Projekt końcowy przepływu pracy z AI: zbuduj i zweryfikuj raport JSON"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Utwórz raport zadań JSON z kontekstem projektu, ograniczonym zakresem polecenia dla agenta, niezależnymi testami, kontrolą źródeł i przekazaniem pracy do nowej sesji."
genre: ["Sztuczna inteligencja", "Inżynieria oprogramowania", "Edukacja"]
tags: ["projekt końcowy przepływu pracy AI", "projekt agenta programistycznego", "weryfikacja zadań AI", "AGENTS.md", "ćwiczenie MCP", "przekazanie agentowi"]
cover: "/img/cover/effective-ai-capstone.webp"
coverAlt: "Zakończone warsztatowe zadanie programistyczne z plikami źródłowymi, wynikami testów, przeglądem agenta i zapisem przekazania"
coverCaption: ""
---

[Wróć do kursu Praktyczny przepływ pracy z AI](/effective-ai-course-start/)

**Zbuduj nowy format wyjściowy i potwierdź jego działanie.** Wcześniej dodano filtr stanu. Ten projekt końcowy zaczyna się od nowego laboratorium i dodaje raport JSON przeznaczony do odczytu przez inny program. Nowe wymaganie sprawdza, czy przeniesiesz swój przepływ pracy na inną funkcję.

**Cel nauki:** dostarczysz sprawdzony raport JSON, zapis dowodów dotyczących źródeł i narzędzi oraz przekazanie, które zrozumie nowa sesja.

## Najważniejsze wnioski

- **Osobne wymaganie** określa funkcję projektu końcowego.
- **Zmiana agenta programistycznego** pozostaje w nazwanych plikach.
- **Niezależne kontrole** rozstrzygają o akceptacji.
- **Przekazanie nowej sesji** pozwala odtworzyć wynik.

## Zanim zaczniesz

**Wymagania wstępne:** ukończ lekcje od 0 do 10, w tym kontekst repozytorium, pierwsze zadanie programistyczne, MCP lub jego odpowiednik w przeglądarce, delegowanie i ograniczone pętle. Lekcja 11 jest opcjonalna. Zarezerwuj 90–120 minut. Poziom trudności: średni.

**Użyj nowego rozpakowania** [laboratorium startowego](/downloads/effective-ai-course-lab.zip). Przed każdą zmianą uruchom `python3 task_report.py tasks.json` i dwa testy bazowe. W systemie Windows użyj `py -3`, jeśli konfiguracja korzysta z programu Python Launcher. Utwórz lokalny punkt bazowy Git, tak jak w konfiguracji kursu. Filtr stanu z lekcji 5 celowo nie występuje.

**Przeczytaj `docs/capstone-requirements.md`, rewizja 1.** Wymaga `--format text|json`. Domyślny tekst nadal brzmi `Total tasks: 4`. Wyjście JSON zawiera liczbowe podsumowanie i liczbę każdego statusu w danych. Sprawdź pustą listę, brak statusu i nieobsługiwany format. Nie używaj `docs/requirements.md` jako źródła wymagań dla tej funkcji.

**Wybierz ścieżkę.** Ścieżka połączona wykorzystuje zaobserwowaną zmianę agenta programistycznego, rzeczywiste wywołanie MCP tylko do odczytu i natywnego workera albo osobną sesję workera. Ścieżka nauki wykorzystuje asystenta czatu do zaproponowania kodu, źródło w przeglądarce zamiast MCP i osobne czaty jako symulowanych workerów. Niedostępne kroki narzędzi oznacz jako „nie uruchomiono”. Obie ścieżki wymagają lokalnych testów i przeglądu plików. Klucz odpowiedzi poniżej zawiera pełne pliki do odtworzenia ćwiczenia. Zapisz pierwszą próbę w notatkach, zanim skopiujesz klucz do nowego rozpakowania.

## Punkt kontrolny 1: Opis projektu

**Otwórz syntetyczny projekt warsztatowy ChatGPT lub Claude.** Poproś o dwuzdaniowy projekt przypomnienia. Sprawdź godzinę 19:00 w `approved-schedule.md`. Harmonogram określa treść przypomnienia. Wymaganie projektu końcowego określa program.

**Dowód:** zapisz nazwę projektu, rewizję źródła, zaobserwowaną godzinę w projekcie i ewentualne poprawki. Nie wysyłaj wiadomości.

## Punkt kontrolny 2: Kontekst repozytorium

**Otwórz nowe laboratorium.** Utwórz krótkie `AGENTS.md`, które odsyła do `docs/capstone-requirements.md`, `task_report.py`, testów i polecenia testowego potwierdzonego podczas konfiguracji. Jeśli używasz Claude Code, zaimportuj wspólny plik z `CLAUDE.md`. Utwórz ludzki commit konfiguracji dla tych plików z instrukcjami, a następnie potwierdź, że `git status --short` nie zwraca zmian. Agent programistyczny nie może commitować zmiany funkcji.

**Dowód:** zachowaj mapę i czysty stan instrukcji. Zapisz klucze JSON i obsługę nieprawidłowych danych z rewizji 1. Wcześniejszą rozmowę o filtrze stanu traktuj jako kontekst innego zadania.

## Punkt kontrolny 3: Źródło zewnętrzne

**Ścieżka połączona:** użyj [serwera OpenAI Docs MCP tylko do odczytu](https://learn.chatgpt.com/learn/docs-mcp) przez obsługiwany klient. Poproś narzędzie MCP o aktualne wskazówki dla `AGENTS.md`. Zapisz nazwę narzędzia, adres URL źródła i jeden istotny punkt dla laboratorium. Potem usuń połączenie ćwiczeniowe.

**Ścieżka nauki:** otwórz w przeglądarce [oficjalną dokumentację `AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md). Zapisz tytuł, URL i istotny punkt. Oznacz odkrywanie i wykonanie MCP jako „nie uruchomiono”.

**Dowód:** skonfigurowany wpis serwera nie potwierdza jego użycia. Ścieżka połączona wymaga widocznego wywołania narzędzia i zwróconej treści źródła.

## Punkt kontrolny 4: Deleguj jeden przegląd

**Poproś workera tylko do odczytu** o sprawdzenie `docs/capstone-requirements.md`, `task_report.py` i testów bazowych. Wymagaj raportu do pięciu wierszy z brakującymi kontrolami i ścieżkami plików. Na ścieżce nauki użyj osobnego czatu i oznacz go jako symulowanego workera.

**Oczekiwany wynik:** testy początkowe sprawdzają sumę i wartość JSON, która nie jest listą. Nie sprawdzają wyjścia JSON, pustej listy, braku statusu ani nieprawidłowego formatu. Samodzielnie otwórz plik testów i zweryfikuj raport. Krótki niezależny przegląd ma tu wartość, bo kryteria akceptacji różnią się od lekcji 5.

**Dowód:** zachowaj krótki raport i jednozdaniową decyzję o integracji. Zapis rozmowy workera przechowuj poza głównym rejestrem zadania.

## Punkt kontrolny 5: Zleć zmianę

**Przekaż agentowi programistycznemu** poniższy pakiet. Na ścieżce nauki asystent czatu proponuje poprawkę, którą ręcznie stosujesz w laboratorium.

```text
Cel: dodać --format text|json po ścieżce JSON.
Źródło: docs/capstone-requirements.md, rewizja 1.
Dozwolone pliki: task_report.py i tests/test_task_report.py.
Zachować: domyślne Total tasks: 4 i niezmieniony tasks.json.
JSON: jeden obiekt z total i licznikami by_status, bez dodatkowego tekstu stdout.
Wymagane kontrole: domyślny i jawny tekst, JSON 4/2/2, pusta lista,
brak statusu, nieprawidłowy format i testy bazowe.
Zatrzymać się przy: konflikcie źródeł, niezwiązanym błędzie bazowym lub zmianie poza zakresem.
Raport: zmienione pliki, polecenia, zaobserwowane wyniki, nierozwiązany problem.
Nie commitować, nie pushować, nie publikować ani nie wysyłać wiadomości.
```

**Sprawdź plan** przed edycją. Wybór schematu ma znaczenie: `total` to liczba, nie ciąg `"4"`. `by_status` zawiera każdy status z danych, więc raport uwzględni też przyszły status. Ogranicz zmianę do rozpakowanego laboratorium.

## Punkt kontrolny 6: Testy i przegląd

**Samodzielnie wykonaj te kontrole.** W systemie Windows zamień `python3` na `py -3`. Dokładna kolejność kluczy JSON i odstępy nie mają znaczenia. Odczytaj wynik jako JSON i porównaj typy wartości.

```bash
git status --short
git diff -- task_report.py tests/test_task_report.py
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --format text
python3 task_report.py tasks.json --format json
python3 task_report.py tasks.json --format invalid
```

**Oczekiwane działanie:** testy przechodzą. Oba polecenia tekstowe wyświetlają `Total tasks: 4`. Polecenie JSON zwraca jeden obiekt z `total` 4, `by_status.open` 2 i `by_status.done` 2. Nieprawidłowy format kończy się niezerowym kodem. Testy obejmują też pustą listę i zadanie bez tekstowego `status`. Przeczytaj zaobserwowany błąd i kod wyjścia dla tych przypadków.

| Punkt kontrolny | Dowód zaliczenia | Odzyskiwanie po błędzie |
|---|---|---|
| **Opis projektu** | Przypomnienie podaje 19:00 | Odśwież źródło harmonogramu |
| **Mapa repozytorium** | Podano wymaganie i ścieżki testów | Popraw pliki instrukcji |
| **Źródło zewnętrzne** | Przeczytano źródło MCP lub opisano przeglądarkową alternatywę | Sprawdź połączenie lub URL |
| **Przegląd workera** | Brakujące testy sprawdzono w pliku | Popraw raport workera |
| **Zakres plików** | Tylko program i testy | Sprawdź każdą niepożądaną zmianę |
| **Działanie** | Sprawdzono tekst, JSON, puste dane i błędy | Zdiagnozuj przyczynę i ponów próbę |
| **Przekazanie** | Nowa sesja odtwarza stan | Dodaj brakujące źródło lub wynik |

**Do bezpiecznego resetu użyj nowego rozpakowania.** Zachowaj notatki poza laboratorium, usuń tylko kopię roboczą i ponownie rozpakuj oryginalny ZIP. Nie wykonuj szerokiego resetu Git w repozytorium z pracą do zachowania.

## Punkt kontrolny 7: Przekazanie nowej sesji

**Napisz przekazanie krótsze niż 180 słów** poza katalogiem laboratorium. Uwzględnij rewizję wymagania, zmienione pliki, dokładne polecenie testowe i wynik, wyjścia tekstowe i JSON, kontrole nieprawidłowych danych, zapis użycia i dalsze działanie. Otwórz nową sesję i poproś ją o wskazanie kluczy JSON oraz ocenę, czy funkcja przeszła.

**Oczekiwana odpowiedź:** nowa sesja wymienia `total` i `by_status`, wskazuje rewizję 1, podaje wyłącznie zaobserwowane kontrole i wskazuje brakujące sprawdzenia.

## Klucz odpowiedzi i rubryka

**Prawidłowa implementacja** znajduje się poniżej. Zapisz pierwszy blok jako `task_report.py`, a drugi jako `tests/test_task_report.py` w nowym rozpakowaniu laboratorium. Nie zmieniaj `tasks.json` ani dwóch plików wymagań. Wykonaj kontrole z punktu 6. Porównaj inne rozwiązanie z wymaganiem i obserwowanym działaniem.

`task_report.py`:

```python
"""Wyświetla tekstową sumę lub podsumowanie JSON zadań warsztatowych."""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


def load_tasks(path: Path) -> list:
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    for index, task in enumerate(tasks, start=1):
        if not isinstance(task, dict) or not isinstance(task.get("status"), str):
            raise ValueError(f"task {index} needs a string status")
    return tasks


def count_tasks(path: Path) -> int:
    return len(load_tasks(path))


def summarize_tasks(path: Path) -> dict:
    tasks = load_tasks(path)
    counts = Counter()
    for task in tasks:
        counts[task["status"]] += 1
    return {"total": len(tasks), "by_status": dict(sorted(counts.items()))}


def main() -> int:
    parser = argparse.ArgumentParser(description="Raport zadań warsztatowych")
    parser.add_argument("path", type=Path, help="ścieżka do listy zadań JSON")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    try:
        if args.format == "json":
            print(json.dumps(summarize_tasks(args.path)))
        else:
            print(f"Total tasks: {count_tasks(args.path)}")
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py`:

```python
"""Kontrole raportów tekstowych i JSON dla zadań warsztatowych."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from sys import path as module_path

ROOT = Path(__file__).resolve().parents[1]
module_path.insert(0, str(ROOT))
from task_report import count_tasks  # noqa: E402


def run_report(path: Path, *options: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / "task_report.py"), str(path), *options],
        capture_output=True, text=True, check=False,
    )


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_default_and_explicit_text(self):
        for options in ((), ("--format", "text")):
            result = run_report(ROOT / "tasks.json", *options)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_json_counts_and_types(self):
        result = run_report(ROOT / "tasks.json", "--format", "json")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout), {
            "total": 4, "by_status": {"open": 2, "done": 2},
        })

    def test_empty_list(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "empty.json"
            sample.write_text("[]", encoding="utf-8")
            result = run_report(sample, "--format", "json")
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout), {
                "total": 0, "by_status": {},
            })

    def test_missing_status(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "missing.json"
            sample.write_text('[{"id": 1}]', encoding="utf-8")
            for options in ((), ("--format", "json")):
                result = run_report(sample, *options)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("status", result.stderr)

    def test_invalid_format(self):
        result = run_report(ROOT / "tasks.json", "--format", "invalid")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**Po użyciu klucza przywróć stan:** zapisz notatki poza laboratorium, usuń tę kopię i ponownie rozpakuj oryginalne laboratorium startowe. Nowa kopia zawiera dwa testy bazowe i nie zawiera implementacji funkcji.

**Przyznaj punkt za każdy punkt kontrolny** w tabeli powyżej. Siedem punktów kończy ścieżkę połączoną, jeśli wiersz źródła zewnętrznego zawiera prawdziwe wywołanie MCP, a wiersz workera dokumentuje prawdziwą sesję. Siedem punktów kończy ścieżkę nauki, jeśli źródło jest zweryfikowaną stroną przeglądarki, a kroki narzędzi są wyraźnie oznaczone jako nieuruchomione. Brak kontroli działania, źródła lub zakresu plików blokuje ukończenie obu ścieżek.

## Sprawdź zrozumienie

1. **Które wymaganie określa tę funkcję?** `docs/capstone-requirements.md`, rewizja 1. Wcześniejsze wymaganie filtra stanu należy do lekcji 5.
2. **Co potwierdza kontrakt JSON?** Odczytaj wyjście polecenia, porównaj wartości liczbowe i liczniki wszystkich statusów, a także sprawdź puste i nieprawidłowe dane. Dopracowane podsumowanie agenta nie wystarczy.

## Rozwiązywanie problemów

- **Test bazowy nie przechodzi przed edycją:** odtwórz laboratorium z ZIP i ponów konfigurację.
- **Agent zmienia inny plik:** sprawdź diff i przywróć tylko niechcianą zmianę w laboratorium.
- **Połączenie MCP nie działa:** użyj źródła w przeglądarce i oznacz punkt jako ścieżkę nauki.
- **Worker powtarza błędną wartość:** ponownie przeczytaj wymaganie projektu i popraw raport.
- **Kończy się limit prób:** zachowaj dziennik błędów i poproś człowieka o wskazanie następnego kroku.

## Następne kroki

**Zachowaj ukończony zapis dowodów.** Aby przejść do zaawansowanej publikacji zespołowej i autorytetu między systemami, kontynuuj [Kurs wdrażania współpracy z AI](/ai-collaboration-course-start/).

**Nawigacja kursu:** [Poprzednia wymagana: ograniczone pętle](/articles/effective-ai-bounded-agent-loops/), [Opcjonalna: ocena wyspecjalizowanych agentów](/articles/effective-ai-specialized-agent-evaluation/), [Plan kursu](/effective-ai-course-start/).
