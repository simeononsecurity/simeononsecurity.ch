---
title: "Pakiety zadań AI: lepsze polecenia i kryteria akceptacji"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Zamień niejasne polecenia dla AI w pakiety zadań z określonym wynikiem, źródłem, zakresem plików, kontrolami i warunkiem zatrzymania."
genre: ["Sztuczna inteligencja", "Produktywność", "Inżynieria oprogramowania"]
tags: ["pisanie poleceń AI", "pakiet zadań", "polecenie dla agenta programistycznego", "kryteria akceptacji", "przepływ pracy AI", "instrukcje dla agentów AI"]
cover: "/img/cover/effective-ai-task-packets.webp"
coverAlt: "Niejasne polecenie przepisane jako krótki pakiet zadań ze źródłem, zakresem, kontrolą i warunkiem zatrzymania"
coverCaption: ""
---

[Powrót do kursu praktycznych przepływów pracy z AI](/effective-ai-course-start/)

**Dobre polecenie opisuje pracę i sposób oceny wyniku.** Więcej słów nie uzupełni brakującego zakresu. Ta lekcja zmienia niejasne polecenie w pakiet zadań do laboratorium kursu.

**Cel nauki:** napiszesz ograniczony pakiet zadań ze źródłem, zakresem plików, kontrolami i warunkiem zatrzymania.

## Najważniejsze informacje

- **Wynik** określa oczekiwany artefakt lub zachowanie.
- **Zakres** określa dozwolone pliki i wykluczone działania.
- **Źródło** wskazuje zatwierdzone wymaganie.
- **Kryteria akceptacji** pozwalają zaobserwować sukces.
- **Warunki zatrzymania** zapobiegają zgadywaniu i nieautoryzowanej dalszej pracy.

## Zanim zaczniesz

**Wymagania wstępne:** rozpakowane laboratorium, zawarty w nim plik `docs/requirements.md` oraz [lekcja o kontekście repozytorium](/articles/effective-ai-agents-md-context/). Zarezerwuj 30 minut. Poziom jest początkujący. Ćwiczenie kończy się przygotowaniem pisemnego pakietu. Na razie nie musisz edytować kodu.

## Porównaj dwa polecenia

**Niejasne polecenie:** „Ulepsz skrypt zadań”. Agent może przepisać wynik, dodać zależności, edytować przykładowe dane lub pominąć testy. Polecenie nie określa żadnej z tych decyzji.

**Ograniczone polecenie:** „Dodaj opcjonalny filtr statusu do `task_report.py` zgodnie z rewizją 1 pliku `docs/requirements.md`. Zachowaj domyślny wynik. Dodaj testy. Nie zmieniaj przykładowych danych. Zatrzymaj się przed commitem”. Agent nadal wybiera szczegóły implementacji, a zadanie określa warunki sukcesu.

| Część pakietu | Przykład z laboratorium | Kontrola |
|---|---|---|
| **Wynik** | Dodaj `--status` do raportu | Działają obie dozwolone wartości |
| **Źródło** | `docs/requirements.md`, rewizja 1 | Kod odpowiada zatwierdzonym wartościom |
| **Zakres** | Tylko program i testy | Diff nie zawiera innych plików |
| **Ograniczenia** | Zachowaj domyślny wynik i przykładowe dane | Wynik bazowy nadal wynosi `Total tasks: 4` |
| **Dowody** | Polecenie testowe i ręczne uruchomienia | Wyniki odpowiadają oczekiwanym liczbom |
| **Zatrzymanie** | Bez commitów i pushy | Historia Git i zdalne repozytorium pozostają bez zmian |

## Użyj szablonu wielokrotnego użytku

**Skopiuj ten szablon** do małego zadania programistycznego lub badawczego. Usuń nieistotne pola zamiast wypełniać je nieprecyzyjnym tekstem.

```text
Outcome:
Authoritative source and revision:
Relevant files or records:
Allowed changes:
Excluded changes and actions:
Examples of desired behavior:
Completion checks:
Stop or ask when:
Report back with:
```

**W laboratorium** wypełniony pakiet wygląda tak:

```text
Outcome: Add an optional --status filter to task_report.py.
Source: docs/requirements.md, revision 1.
Relevant files: task_report.py, tasks.json, tests/.
Allowed changes: task_report.py and focused tests.
Excluded: tasks.json, new dependencies, commits, pushes.
Examples: no filter prints Total tasks: 4. Open and done each print 2.
Checks: run unit tests and four manual commands: no filter, open, done, and invalid.
The invalid value must exit nonzero with a clear error.
Stop or ask: source conflict, missing file, unrelated failing baseline.
Report: changed files, commands, observed outputs, unresolved issues.
```

**W systemie Windows** użyj `py -3` w poleceniach pakietu, jeśli twoje środowisko korzysta z programu uruchamiającego Pythona.

**Pakiet nie określa każdej linijki kodu.** Pozwala agentowi wybrać niewielką implementację, a wynik pozostaje sprawdzalny.

## Ostrożnie dodawaj przykłady

**Dokładny przykład ogranicza niejasności.** Przykłady `open` i `done` określają wynik dla dostarczonego pliku z czterema zadaniami. Nie ustanawiają ogólnej reguły dla wszystkich plików. W innym pliku liczby zależą od jego rekordów.

**Oddzielaj wynik oczekiwany od zaobserwowanego.** Przed uruchomieniem programu `Total tasks: 2` jest oczekiwanym wynikiem dla każdego statusu. Po uruchomieniu wynik terminala jest obserwacją. Jeśli wartości się różnią, sprawdź dane i implementację przed zgłoszeniem sukcesu.

## Ustal warunek zatrzymania

**Załóż, że brakuje pliku z wymaganiami.** Pakiet wskazuje go jako zatwierdzone źródło. Zatrzymaj się i poproś o wymaganie zamiast wywodzić dozwolone wartości ze starego czatu lub przykładowego zgłoszenia.

**Załóż, że testy bazowe nie przechodzą przed edycją.** Zapisz błąd i zapytaj, czy najpierw naprawić stan początkowy. Późniejsze przejście testów nie wyjaśni, czy zmianę spowodował filtr, czy stan początkowy.

**Załóż, że agent chce utworzyć commit.** Pakiet wyklucza commity. Poproś go o zatrzymanie się po diffie i testach. Ty zdecydujesz, czy późniejszy commit pasuje do procesu projektu.

## Sprawdź pakiet

**Przyznaj jeden punkt za każdą odpowiedź:** Czy wynik jest konkretny? Czy wskazano nadrzędne źródło? Czy zakres plików jest jasny? Czy podano co najmniej dwie obserwowalne kontrole? Czy jest warunek zatrzymania? Wynik poniżej pięciu oznacza, że przed delegowaniem trzeba poprawić pakiet.

**Twój rezultat:** zapisz końcowy pakiet zadań i jednozdaniowe wyjaśnienie warunku zatrzymania. Przekaż go agentowi programistycznemu podczas następnej lekcji praktycznej albo samodzielnie podaj oczekiwane wyniki na ścieżce nauki.

## Sprawdź zrozumienie

1. **Pytanie:** Co sprawia, że pakiet zadań można zweryfikować? **Odpowiedź:** Źródło, dozwolone pliki, obserwowalne kontrole i warunek zatrzymania.
2. **Pytanie:** Co agent powinien zrobić, gdy w źródle brakuje wymaganego szczegółu? **Odpowiedź:** Zatrzymać się i zgłosić brak zamiast go wymyślać.

## Rozwiązywanie problemów

- **Agent zmienia zbyt wiele:** wymień pliki i wykluczone działania w pakiecie.
- **Agent zadaje wiele pytań:** podaj brakujące źródło lub konkretny przykład.
- **Agent zbyt wcześnie zgłasza sukces:** poproś o zaobserwowane wyniki poleceń i sprawdź pliki.
- **Pakiet staje się zbyt długi:** zastąp skopiowaną treść źródła ścieżką i rewizją.

## Następne kroki

**Przejdź do lekcji [Twoje pierwsze zadanie z agentem programistycznym](/articles/effective-ai-coding-agent-first-task/)**. Użyj pakietu, aby przeprowadzić niewielką zmianę w laboratorium.

**Nawigacja kursu:** [Wstecz: Kontekst repozytorium](/articles/effective-ai-agents-md-context/), [Plan kursu](/effective-ai-course-start/).
