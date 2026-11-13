---
title: "Ograniczone pętle agentów AI: kontrole, ponowienia i reguły zatrzymania"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Zdefiniuj pętlę celu AI z obserwowalnym stanem, kontrolami, limitami ponowień, warunkami zatrzymania i jasnym przekazaniem zadania człowiekowi."
genre: ["Sztuczna inteligencja", "Inżynieria oprogramowania", "Produktywność"]
tags: ["pętle celów AI", "pętla ponowień agenta", "reguły zatrzymania automatyzacji AI", "monitorowanie agentów", "przekazanie AI człowiekowi", "ograniczony przepływ pracy AI"]
cover: "/img/cover/effective-ai-bounded-agent-loops.webp"
coverAlt: "Mała pętla agenta prowadzi od jednej edycji przez test i decyzję o ponowieniu do przekazania zadania człowiekowi"
coverCaption: ""
---

[Wróć do praktycznego kursu przepływów pracy AI](/effective-ai-course-start/)

**Pętla celu powtarza pracę, aż określony wynik przejdzie kontrolę lub zadziała reguła zatrzymania.** Przydatna pętla odczytuje bieżący stan, wykonuje ograniczoną czynność, sprawdza wynik i zapisuje przebieg. Otwarta instrukcja „próbuj dalej” nie określa wiarygodnych zasad zakończenia.

**Cel nauki:** uruchomisz ograniczoną pętlę laboratoryjną ze znaną nieudaną kontrolą i zapiszesz decyzję o zatrzymaniu.

## Najważniejsze wnioski

- **Cel:** wynik opisany w obserwowalny sposób.
- **Stan:** bieżące pliki, wyniki, błędy i rewizja źródła.
- **Kontrola:** test lub przegląd powiązany z celem.
- **Budżet ponowień:** maksymalna liczba prób dla jednego błędu.
- **Reguła zatrzymania:** warunek wymagający zakończenia lub decyzji człowieka.

## Zanim zaczniesz

**Wymagania wstępne:** [pakiet zadania](/articles/effective-ai-task-packets/), [rejestr weryfikacji](/articles/effective-ai-output-verification/) i [lekcja o delegowaniu](/articles/effective-ai-agent-delegation/). Zarezerwuj 45 minut. Poziom trudności jest średni. Użyj świeżej kopii syntetycznego laboratorium, aby z góry znać pierwszą nieudaną kontrolę.

## Zapisz kontrakt pętli

**Dla prośby o filtrowanie według statusu** ustal kontrakt przed każdą ponowną próbą:

```text
Cel: obsługiwać --status open|done bez zmiany domyślnego wyniku.
Źródło: docs/requirements.md, rewizja 1.
Dozwolone pliki: task_report.py i ukierunkowane testy.
Kontrole: testy jednostkowe, liczby 4/2/2, nieprawidłowa wartość zwraca kod wyjścia różny od zera.
Limit ponowień: najwyżej dwie edycje po pierwszej próbie.
Zatrzymaj natychmiast: konflikt źródeł, nieoczekiwana zmiana pliku, ujawnienie sekretu,
lub niepowodzenie testu bazowego niezwiązane z tym żądaniem.
Przekazanie: zgłoś końcowy diff, polecenia, wyniki, próby i nierozwiązany problem.
```

**Budżet to zasada dla zadania**, a nie ustawienie domyślne produktu. Dwa ponowienia wystarczą, by zdiagnozować małe zadanie laboratoryjne bez ukrywania powtarzających się błędów. Zadanie produkcyjne wymaga osobnej decyzji dotyczącej ryzyka i przeglądu.

## Użyj tabeli stanu

| Krok | Stan do zapisania | Decyzja |
|---|---|---|
| **Odczyt** | Rewizja źródła i wynik bazowy | Zatrzymaj się, jeśli stan początkowy jest inny |
| **Działanie** | Zmienione pliki i wykonana czynność | Odrzuć zmiany poza zakresem |
| **Kontrola** | Dokładny test i wynik ręczny | Zaakceptuj lub zdiagnozuj |
| **Ponowienie** | Przyczyna błędu i nowa hipoteza | Kontynuuj tylko w ramach budżetu |
| **Przekazanie** | Stan końcowy i następna osoba odpowiedzialna | Zatrzymaj się po zaliczeniu lub zablokowaniu |

**Zapisuj próby, a nie tylko ostatnią wiadomość.** Test, który przechodzi po trzech nieujawnionych edycjach, nie wyjaśnia, co się zmieniło. Prowadź krótki rejestr błędu, poprawionej hipotezy i nowych dowodów.

## Przeanalizuj błąd

**Przykład pierwszej próby:** agent dodaje filtrowanie i testy. `open` zwraca 2, ale `--status invalid` zwraca 0 i kończy się powodzeniem. Wymaganie mówi, że nieprawidłowa wartość ma zwrócić niezerowy kod wyjścia. Oznacz kontrolę jako niezaliczoną.

**Diagnoza:** sprawdź walidację argumentów. Agent potraktował nieznaną wartość jak pusty wynik zamiast zgłosić błąd. Poproś o ograniczoną poprawkę, która sprawdzi dozwolone wartości przed zliczaniem. Ponownie uruchom przypadek nieprawidłowy i wszystkie wcześniejsze kontrole.

```text
Próba 1: nieprawidłowy status zwrócił sukces, więc kryterium akceptacji nie zostało spełnione.
Znaleziona przyczyna: brak sprawdzania dozwolonych wartości.
Żądanie próby 2: odrzucaj nieobsługiwane wartości i zachowaj liczby 4/2/2.
Wymagane dowody: pełny przebieg testów i kod wyjścia nieprawidłowego polecenia.
```

**Oczekiwany wynik drugiej próby:** jasny błąd i niezerowy kod wyjścia dla `invalid`, przy niezmienionych prawidłowych licznikach. Jeśli druga próba również się nie powiedzie, wykorzystaj ostatnią dopiero po wskazaniu nowej przyczyny. Powtórzenie tej samej prośby nie jest diagnozą.

## Obsłuż niejednoznaczne wyniki

**Proces, który kończy się bez wyniku, nie oznacza sukcesu.** Jeśli narzędzie przekroczy limit czasu po możliwym zapisie, sprawdź pliki i stan Git przed ponownym uruchomieniem. Jeśli połączona usługa zgłasza nieznany wynik, odczytaj jej bieżący stan przed powtórzeniem zewnętrznej czynności. Poza laboratorium zduplikowane wysyłki, publikacje lub zapisy są realnym ryzykiem.

**Zatrzymaj się i poproś o przegląd człowieka**, gdy wymaganie jest sprzeczne z innym zatwierdzonym źródłem, uprawnienie blokuje działanie, budżet ponowień się wyczerpał lub żądana czynność przekracza granicę publikacji. Przekazanie powinno określać dokładny stan i decyzję, która pozostała do podjęcia.

## Oddziel pętle od monitorów

**Pętla edycji** działa w ramach ograniczonego zadania i sprawdza wynik po każdej czynności. **Zaplanowany monitor** uruchamia się później, aby sprawdzić warunek. Monitor wymaga własnej częstotliwości, progu zmiany, reguły powiadamiania i warunku zatrzymania. Nie zamieniaj pętli edycji w laboratorium w zadanie cykliczne. Następna lekcja ocenia systemy trwałe przed ich uruchomieniem.

## Uruchom kontrolowaną pętlę

**Zacznij od niezmienionego laboratorium.** Dwa testy bazowe przechodzą. W świeżo rozpakowanej kopii utwórz `tests/test_loop_contract.py` z poniższą kontrolą. Ten plik określa pożądaną funkcję, której brakuje w wersji startowej. Nie należy do utrzymywanego archiwum ZIP wersji startowej.

```python
"""One controlled failing check for the status-filter exercise."""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class LoopContractTests(unittest.TestCase):
    def test_open_status_count(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"),
             str(ROOT / "tasks.json"), "--status", "open"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "Total tasks: 2")


if __name__ == "__main__":
    unittest.main()
```

**Uruchom `python3 -m unittest discover -s tests -v`.** Dwa oryginalne testy powinny przejść, a nowy test kontraktowy powinien się nie powieść, ponieważ wersja startowa nie obsługuje `--status`. Zapisz rzeczywisty błąd. Jeśli zainicjowano Git zgodnie z lekcją 0, zapisz także `git status --short`. W przeciwnym razie porównaj zmienione pliki z nietkniętą kopią. W Windows użyj `py -3`, jeśli konfiguracja korzysta z launchera.

**Ustal budżet trzech prób:** pierwszą edycję i najwyżej dwie poprawki. Przekaż agentowi powyższy kontrakt pętli i poproś o jedną ograniczoną zmianę. Po każdej próbie sprawdź zmienione pliki, ponownie uruchom wszystkie testy i wykonaj polecenia domyślne, `open`, `done` oraz z nieprawidłową wartością. Przed kolejną próbą zapisz przyczynę błędu. Zatrzymaj się po zaliczeniu testu, niepowiązanym błędzie bazowym, zmianie poza zakresem lub trzeciej nieudanej próbie.

**Ścieżka nauki:** po zapisaniu czerwonego testu zastosuj pełne [rozwiązanie z lekcji 5](/articles/effective-ai-coding-agent-first-task/) w tej świeżej kopii. Ponownie wykonaj te same kontrole i zapisz, że edycja agenta nie została uruchomiona. Zachowaj kontrolowany test kontraktowy. Nie osłabiaj go ani nie usuwaj, aby go zaliczyć.

| Próba | Stan i obserwacja | Decyzja |
|---|---|---|
| **Przed edycją** | Dwa testy bazowe przechodzą, nowa kontrola `open` nie przechodzi | Kontynuuj jedną ograniczoną edycją |
| **Po każdej edycji** | Zapisz dokładne testy, liczniki, niezerowy kod dla nieprawidłowej wartości i zmienione pliki | Zaakceptuj, zdiagnozuj lub zatrzymaj |
| **Po wyczerpaniu budżetu** | Zapisz pozostały błąd i bieżący diff | Przekaż zadanie bez kolejnej próby |

## Ćwicz i sprawdź

**Twój artefakt:** kontrolowany test, który nie przechodzi, zaobserwowane wyniki przed i po, dziennik prób oraz końcowa decyzja o akceptacji lub zatrzymaniu. Jeśli pierwsza edycja przejdzie, zapisz jedną próbę. Nie wymyślaj drugiej awarii, aby wypełnić dziennik.

**Kontrola ukończenia:** kontrakt wskazuje źródło, zakres plików, obserwowalne kontrole, limit ponowień, co najmniej jeden natychmiastowy warunek zatrzymania oraz przekazanie zadania. Rejestr zawiera rzeczywisty czerwony test, późniejsze wyniki kontroli i albo sukces, albo zatrzymanie z powodu limitu. Druga próba wskazuje nową przyczynę i różni się od pierwszej.

## Sprawdź zrozumienie

1. **Pytanie:** co wykazuje pierwszy czerwony test kontraktowy? **Odpowiedź:** wersja startowa nie ma żądanego filtra stanu, co potwierdza test napisany przed edycją.
2. **Pytanie:** kiedy pętla musi się zatrzymać, mimo że pozostały próby? **Odpowiedź:** przy zmianie poza zakresem, niejasnym uprawnieniu lub sprzecznym wymaganiu.

## Rozwiązywanie problemów

- **Pętla powtarza ten sam błąd:** zatrzymaj się i postaw nową hipotezę co do przyczyny.
- **Kontrole słabną:** przywróć pierwotne kryteria akceptacji.
- **Niepewny wynik zewnętrzny:** sprawdź bieżący stan przed kolejną próbą.
- **Budżet się wyczerpał:** przekaż rejestr błędów zamiast ich ukrywać.

## Następne kroki

Przejdź do opcjonalnej lekcji [Ocena wyspecjalizowanych agentów](/articles/effective-ai-specialized-agent-evaluation/) albo od razu do [projektu końcowego kursu przepływów pracy AI](/articles/effective-ai-capstone/). Więcej informacji o środowiskach uruchomieniowych znajdziesz w [przewodniku po środowiskach agentów](/articles/best-ai-agent-harnesses/).

**Nawigacja kursu:** [Poprzednia: delegowanie agentów](/articles/effective-ai-agent-delegation/), [Plan kursu](/effective-ai-course-start/).
