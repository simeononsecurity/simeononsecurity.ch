---
title: "Wykonaj pierwsze zadanie w repozytorium z agentem programistycznym"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Wybierz interfejs agenta programistycznego, otwórz przykładowe repozytorium, sprawdź proponowaną zmianę i uruchom testy przed jej zachowaniem."
genre: ["Sztuczna inteligencja", "Inżynieria oprogramowania"]
tags: ["poradnik Codex CLI", "aplikacja Codex", "Claude Code CLI", "poradnik OpenCode", "przepływ pracy z agentem programistycznym", "narzędzia programistyczne AI"]
cover: "/img/cover/effective-ai-coding-agent-first-task.webp"
coverAlt: "Repozytorium kodu z oddzielnymi widokami agenta w terminalu i na pulpicie obok sprawdzonego pliku diff"
coverCaption: ""
---

[Wróć do kursu Praktyczny przepływ pracy z AI](/effective-ai-course-start/)

**Agent programistyczny czyta pliki, proponuje zmiany i uruchamia narzędzia w obszarze roboczym.** W tej lekcji wykonasz małe zadanie w repozytorium. Wybierz Codex w aplikacji ChatGPT na komputerze lub w CLI, Claude Code CLI albo OpenCode TUI. Przed zaakceptowaniem zmiany sprawdź jej treść.

**Cel nauki:** wykonasz lub ręcznie zastosujesz ograniczoną zmianę i sprawdzisz diff oraz działanie.

## Najważniejsze informacje

- **Codex w aplikacji ChatGPT na komputerze** zapewnia wizualny obszar do pracy i przeglądu zmian.
- **Codex CLI** uruchamia sesję Codex w terminalu.
- **Claude Code CLI** obsługuje przepływ pracy programistycznej Claude w terminalu.
- **OpenCode TUI** oferuje terminalowy przepływ pracy z konfigurowalnymi dostawcami i uprawnieniami.
- **Diff i wynik testu** są ważniejsze niż komunikat asystenta o zakończeniu pracy.

## Zanim zaczniesz

**Wymagania wstępne:** ukończ [konfigurację kursu](/articles/effective-ai-course-setup/), w tym test bazowy i lokalny zrzut Git. Przed tą lekcją ukończ [kontekst repozytorium](/articles/effective-ai-agents-md-context/) oraz [pakiety zadań](/articles/effective-ai-task-packets/). Użyj agenta programistycznego, do którego masz uprawniony dostęp. Zarezerwuj 45 minut. Poziom trudności: od początkującego do średniozaawansowanego.

**Skorzystaj ze [startowego laboratorium kursu](/downloads/effective-ai-course-lab.zip)** w tymczasowym folderze. Archiwum zawiera mały program raportujący zadania, przykładowe dane i testy. Nie używaj repozytorium produkcyjnego do pierwszej edycji. Dodaj filtr `--status`, zachowując dotychczasową sumę zadań.

## Ścieżka nauki bez agenta programistycznego

**Poproś asystenta czatu o zaproponowanie tej samej zmiany,** jeśli agent programistyczny jest niedostępny. Wklej tylko `docs/requirements.md`, `task_report.py` i odpowiedni plik testowy z syntetycznego laboratorium. Poproś o ujednolicony diff i krótkie wyjaśnienie. Ujednolicony diff oznacza stare wiersze znakiem `-`, a nowe znakiem `+`. Otwórz wskazany plik w edytorze tekstu, zastąp stare wiersze proponowaną zmianą i zapisz plik. Następnie uruchom wszystkie polecenia z sekcji Sprawdź wynik. Nie zmieniaj `tasks.json`. Zapisz, że krok z agentem programistycznym nie został wykonany. Projekt końcowy ma osobną funkcję JSON, dlatego porównaj filtr z wymaganiem i testami z lekcji 5.

## Wybierz interfejs

**Najpierw wybierz środowisko przeglądu.** Codex w aplikacji ChatGPT na komputerze pasuje do projektu wizualnego i przeglądu diffów. Interfejs terminalowy sprawdzi się przy pracy w rozpakowanym folderze laboratorium. Porównuj narzędzia terminalowe ze sobą:

| Narzędzie terminalowe | Sprawdzenie konta lub dostawcy | Polecenie startowe |
|---|---|---|
| **Codex CLI** | Potwierdź zalogowanie do Codex i uprawnienia lokalne | `codex` |
| **Claude Code CLI** | Potwierdź dostęp do Claude Code i uprawnienia lokalne | `claude` |
| **OpenCode TUI** | Skonfiguruj obsługiwanego dostawcę modelu i uprawnienia | `opencode` |

**Zainstaluj i zaloguj się zgodnie z aktualnym oficjalnym przewodnikiem** wybranego narzędzia. Przeczytaj [Codex CLI](https://learn.chatgpt.com/docs/codex/cli), [aplikację ChatGPT na komputerze](https://learn.chatgpt.com/docs/app), [Claude Code](https://code.claude.com/docs/en/overview) lub [OpenCode](https://opencode.ai/docs/). Polecenia, obsługiwane platformy i wymagania konta zmieniają się. Ta lekcja używa stabilnych nazw uruchomieniowych i wspólnej procedury przeglądu.

**Aby dokładniej wybrać produkt,** przeczytaj porównanie [agentów programistycznych CLI](/articles/cli-coding-agents-comparison/) lub [agentów programistycznych z interfejsem graficznym](/articles/gui-coding-agents-comparison/). Przewodniki [Codex CLI i komputer](/articles/codex-cli-vs-desktop/), [Claude Code CLI i komputer](/articles/claude-code-cli-vs-desktop/) oraz [OpenCode CLI i komputer](/articles/opencode-cli-vs-desktop/) porównują interfejsy poszczególnych produktów.

**Zacznij w folderze laboratorium.** Każdy interfejs wymaga jawnego wyboru obszaru roboczego:

1. **Codex na komputerze:** otwórz aplikację ChatGPT na komputerze, wybierz rozpakowane laboratorium jako projekt lokalny i uruchom w nim zadanie lokalne. Przed edycją sprawdź ścieżkę folderu i prośby o zatwierdzenie. Zadanie hostowane korzysta z osobnej kopii obszaru roboczego.
2. **Codex CLI:** uruchom `cd /path/to/effective-ai-course-lab`, a następnie `codex`. Sprawdź wyświetlony folder roboczy i tryb zatwierdzania.
3. **Claude Code CLI:** uruchom to samo polecenie `cd`, a potem `claude`. Sprawdź folder projektu i uprawnienia narzędzi.
4. **OpenCode TUI:** uruchom to samo polecenie `cd`, a potem `opencode`. Sprawdź wybranego dostawcę, projekt i ustawienia uprawnień.

**ChatGPT chat i Claude Projects obsługują rozmowy i współdzielone pliki referencyjne.** Codex i Claude Code działają w obszarze kodu z narzędziami do plików i poleceń. OpenCode oferuje również widoki na komputer i IDE, ale ta lekcja korzysta z terminala. Dostawca, konto i wykonywanie lokalne lub hostowane są różne. Zapisz wybrane środowisko zamiast traktować każdą sesję jako ten sam przebieg.

**Przed otwarciem laboratorium sprawdź pięć kwestii:** obsługiwany system operacyjny, uwierzytelnianie, koszt dostawcy lub konta, uprawnienia do plików i poleceń oraz to, czy zadanie działa lokalnie, czy na zdalnym hoście. Zapisz wybór. Nie zakładaj, że aplikacja na komputerze i narzędzie terminalowe korzystają z tego samego obszaru roboczego.

## Sprawdź projekt startowy

**Ponownie otwórz czysty folder laboratorium** z lekcji o kontekście repozytorium. Ta kopia zawiera zatwierdzony plik `AGENTS.md` oraz opcjonalne wskazówki `CLAUDE.md`. Przed prośbą o edycję przejrzyj pliki. Uruchom testy bazowe z tego folderu.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
```

**Oczekiwany wynik bazowy:** raport wyświetla `Total tasks: 4`. Testy pokazują dwie nazwy i kończą się wynikiem `OK`. Jeśli którykolwiek test zawiedzie, zatrzymaj się i sprawdź rozpakowane pliki. Nie przypisuj agentowi naprawy wadliwego punktu startowego.

**Korzystaj z lokalnych zrzutów Git** z konfiguracji kursu i lekcji o kontekście repozytorium. `AGENTS.md` i opcjonalny `CLAUDE.md` powinny być już zatwierdzone. Przed edycją funkcji uruchom `git status --short` i oczekuj pustej listy. Agent również nie może tworzyć commitów. Archiwum nie zawiera historii Git. Plik `.gitignore` wyklucza bajtkod Pythona generowany podczas uruchamiania testów. Jeśli rozpakujesz nową kopię, powtórz w niej konfigurację kursu i lekcję o kontekście repozytorium. Zatwierdź pliki z instrukcjami przed edycją funkcji. Najpierw zainicjuj i zatwierdź projekt startowy:

```bash
git init
git add .
git commit -m "Podstawa laboratorium kursu"
```

**Następnie dodaj `AGENTS.md` i opcjonalny `CLAUDE.md`** z zatwierdzonym źródłem i poleceniem testowym z lekcji o kontekście repozytorium. Zatwierdź te pliki, sprawdź, czy `git status --short` nie pokazuje zmian, i rozpocznij edycję funkcji. Polecenia wykonuj w rozpakowanym folderze ćwiczeniowym, a nie w katalogu głównym innego repozytorium.

## Przekaż ograniczone zadanie

**Otwórz folder laboratorium** w wybranym agencie programistycznym. Wyślij ten pakiet zadania:

```text
Dodaj do task_report.py opcjonalny argument --status.
Dozwolone wartości: open i done.
Jeśli argumentu brakuje, zachowaj dotychczasowy wynik sumy bez zmian.
Jeśli argument podano, licz tylko pasujące zadania i wypisz Total tasks: N.
Dodaj testy obu wartości, nieprawidłowej wartości i niezmienionego wyniku domyślnego.
Nie zmieniaj tasks.json ani niepowiązanych plików.
Uruchom testy i podaj dokładne polecenie oraz wynik.
Zakończ po kodzie i testach. Nie twórz commita ani nie wykonuj push.
```

**W systemie Windows** zastąp `python3` zweryfikowanym podczas konfiguracji poleceniem `py -3`, także w zapisanych instrukcjach repozytorium i pakiecie zadania.

**Jeśli nie znasz jeszcze kodu, poproś przed edycją o krótki plan.** Zezwól agentowi na edycję wyłącznie tymczasowego folderu laboratorium. Zasady uprawnień różnią się w zależności od narzędzia, więc przed zgodą na polecenia powłoki lub zapis plików sprawdź aktualne ustawienia.

## Sprawdź wynik

**Przeczytaj diff.** Sprawdź, czy wyjście bez filtra pozostaje takie samo, filtr przyjmuje tylko dwie wartości, a testy obejmują błędną wartość i niezmienione wyjście domyślne. Zaliczone testy potwierdzają zmianę tylko wtedy, gdy sprawdzają wymagane działanie.

```bash
git status --short
git diff -- task_report.py tests
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**Oczekiwane wyniki:** pierwsze trzy polecenia raportujące pokazują 4, 2 i 2. Nieprawidłowa wartość wyświetla jasny błąd, a proces kończy się kodem różnym od zera. Dokładna treść zależy od implementacji. Na macOS lub Linux uruchom `echo $?` bezpośrednio po błędnym poleceniu, aby odczytać kod wyjścia. W PowerShell sprawdź `$LASTEXITCODE`.

| Dowód | Co sprawdzić |
|---|---|
| **Lista plików** | Zmieniły się tylko program i testy |
| **Diff** | Logika filtra odpowiada zadaniu |
| **Wynik testów** | Nowe przypadki uruchomiono i zaliczono |
| **Ręczne uruchomienie** | Liczby dla wartości domyślnej, `open` i `done` zgadzają się z `tasks.json` |

**Jeśli agent podaje wynik bez uruchomienia testów,** wykonaj polecenie samodzielnie. Jeśli edycja wykracza poza pakiet zadania, poproś o ograniczoną poprawkę. Jeśli stan jest niejasny, usuń rozpakowaną kopię ćwiczeniową i ponownie rozpakuj oryginalny ZIP.

## Odpowiedzi do ścieżki nauki

**Użyj tych kompletnych plików, jeśli ręczna poprawka się nie powiedzie.** Zacznij od świeżo rozpakowanego laboratorium, zapisz pierwszy blok jako `task_report.py`, drugi jako `tests/test_task_report.py` i uruchom polecenia z sekcji Sprawdź wynik. Nie zmieniaj `tasks.json` ani `docs/requirements.md`. Zapisz pierwotną awarię przed skopiowaniem plików.

`task_report.py`:

```python
"""Wyświetla liczbę zadań z pliku JSON."""

import argparse
import json
import sys
from pathlib import Path


def count_tasks(path: Path, status: str | None = None) -> int:
    """Liczy wszystkie zadania lub zadania z dozwolonym statusem."""
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    if status not in (None, "open", "done"):
        raise ValueError("status must be open or done")
    if status is None:
        return len(tasks)
    return sum(1 for task in tasks if task["status"] == status)


def main() -> int:
    parser = argparse.ArgumentParser(description="Policz zadania warsztatu")
    parser.add_argument("path", type=Path, help="ścieżka do listy zadań JSON")
    parser.add_argument("--status", choices=("open", "done"))
    args = parser.parse_args()
    try:
        total = count_tasks(args.path, args.status)
    except (OSError, ValueError, KeyError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Total tasks: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py`:

```python
"""Testy raportu zadań warsztatu."""

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


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_counts_each_approved_status(self):
        sample = ROOT / "tasks.json"
        self.assertEqual(count_tasks(sample, "open"), 2)
        self.assertEqual(count_tasks(sample, "done"), 2)

    def test_rejects_invalid_status_in_function(self):
        with self.assertRaises(ValueError):
            count_tasks(ROOT / "tasks.json", "pending")

    def test_default_command_stays_unchanged(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"), str(ROOT / "tasks.json")],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_invalid_command_exits_nonzero(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"), str(ROOT / "tasks.json"),
             "--status", "invalid"],
            capture_output=True, text=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**Zachowaj kopię ze zmianą, która przechodzi testy filtra** na potrzeby lekcji o kontekście i weryfikacji wyniku. Jeśli użyto tego przykładu do odzyskania pracy, zachowaj nową kopię z zaliczonymi testami filtra. Trzymaj diff i zapis testów poza laboratorium. Przywróć wersję startową przed lekcją o delegowaniu albo usuń nieudaną próbę, aby zacząć od czystej kopii.

## Ćwicz i sprawdź

**Twój materiał:** diff laboratorium i czterowierszowy zapis przeglądu obejmujący zakres plików, działanie domyślne, filtrowanie oraz błędne dane. Zapisz nazwę i wersję narzędzia w prywatnych notatkach, aby odtworzyć problem dotyczący konkretnej wersji.

**Oczekiwane rozumowanie:** wybrano interfejs pasujący do sposobu pracy, ograniczono zadanie, sprawdzono rzeczywistą zmianę i wykonano kontrolę niezależną od raportu agenta.

## Sprawdź swoją wiedzę

1. **Pytanie:** Co potwierdza, że filtr stanu działa? **Odpowiedź:** Ograniczony diff, zaliczone testy i zaobserwowane wyniki dla trybu domyślnego, open, done oraz błędnej wartości.
2. **Pytanie:** Czy komunikat agenta, że uruchomił testy, jest twoim wynikiem testów? **Odpowiedź:** Nie. Uruchom polecenie lub sprawdź wynik testów.

## Rozwiązywanie problemów

- **Brakuje polecenia:** dokończ instalację z podanego przewodnika dostawcy i ponownie otwórz terminal.
- **Brak dostępu do plików:** otwórz rozpakowany folder laboratorium i sprawdź uprawnienia obszaru roboczego.
- **Zmieniły się nieoczekiwane pliki:** zatrzymaj się i sprawdź `git status --short` przed kolejną prośbą.
- **Testy przechodzą, ale działanie jest błędne:** dodaj ręczny przypadek lub test brakującego wymagania.

## Następne kroki

**Przejdź do [Okien kontekstu i przekazywania pracy](/articles/effective-ai-context-window-management/)**. Przygotujesz przydatny zapis do nowej sesji.

**Nawigacja kursu:** [Wstecz: Pakiety zadań](/articles/effective-ai-task-packets/), [Plan kursu](/effective-ai-course-start/).
