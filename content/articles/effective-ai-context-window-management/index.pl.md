---
title: "Zarządzanie oknem kontekstu AI: skup agentów programistycznych"
description: "Kontroluj aktywny kontekst zadania AI za pomocą wybranych plików, zwięzłych przekazań i krótkich raportów pracowników, zachowując decyzje i dowody."
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
genre: ["Sztuczna inteligencja", "Inżynieria oprogramowania"]
tags: ["zarządzanie oknem kontekstu AI", "kontekst agenta programistycznego", "przekazanie AI", "kompaktowanie kontekstu", "orkiestracja agentów", "budżet tokenów"]
cover: "/img/cover/effective-ai-context-window-management.webp"
coverAlt: "Zwięzła notatka przekazania obok wybranych plików projektu i znacznie dłuższej, odrzuconej transkrypcji czatu"
coverCaption: ""
---

[Wróć do praktycznego kursu pracy z AI](/effective-ai-course-start/)

**Okno kontekstu obejmuje tekst i inne materiały przetwarzane przez model w bieżącej turze.** Miejsce zajmują prompty, instrukcje, definicje narzędzi, fragmenty plików, wyniki narzędzi i historia rozmowy. Ta lekcja pokazuje, jak skupić kolejne zadanie i zostawić rzetelne przekazanie pracy.

**Cel nauki:** przygotuj zwięzłe przekazanie pracy i sprawdź je w nowej sesji.

## Najważniejsze informacje

- **Tokeny** to jednostki używane przez model do przetwarzania wejścia i wyjścia.
- **Aktywny kontekst** to materiały dostępne w jednej turze, z uwzględnieniem limitów produktu.
- **Trwałe źródła** znajdują się poza czatem, w plikach lub zapisach projektu.
- **Kompaktowanie** streszcza lub usuwa starszy kontekst i może pominąć potrzebny szczegół.
- **Przekazanie pracy** wskazuje nowej sesji aktualne źródła i zweryfikowane działania.

## Zanim zaczniesz

**Wymagania wstępne:** edytowane laboratorium z [pierwszego zadania z agentem programistycznym](/articles/effective-ai-coding-agent-first-task/), zatwierdzone wymaganie i [lekcja o pakietach zadań](/articles/effective-ai-task-packets/). Jeśli korzystasz ze ścieżki nauki, użyj laboratorium edytowanego ręcznie. Zarezerwuj 35 minut. Poziom trudności jest średni. Zapisz notatki z kursu poza rozpakowanym katalogiem laboratorium, aby `git status` pokazywał tylko zmiany w kodzie.

## Dobierz kontekst do zadania

**Do zmiany filtra statusu** agent potrzebuje `task_report.py`, `docs/requirements.md`, właściwych testów i małej próbki `tasks.json`. Nie potrzebuje wszystkich starych czatów, całej dokumentacji witryny ani pełnej historii Git. Najpierw sprawdź mapę projektu, a potem wczytaj tylko pliki potrzebne do kolejnej decyzji.

| Zadanie | Przydatny kontekst | Nadmiarowy kontekst |
|---|---|---|
| **Określenie zachowania** | Zatwierdzone wymaganie i jedna próbka danych | Stare rozmowy rozpoznawcze |
| **Edycja programu** | Program i ukierunkowane testy | Niezwiązane katalogi projektów |
| **Przegląd wyniku** | Diff, wynik testów i wymaganie | Pełny zapis pracy agenta |
| **Późniejszy powrót** | Notatka przekazania i ścieżki źródeł | Wklejony czat z kilku godzin |

**To wybór materiałów do pobrania, a nie zasada ukrywania dowodów.** Jeśli test się nie powiedzie, dołącz dokładny wynik i wskaż plik. Usuwaj nieistotne logi, ale zachowaj szczegóły potrzebne do diagnozy.

**Uwzględnij stały narzut, zanim dodasz kolejnych pracowników.** Instrukcje agenta i schematy dostępnych narzędzi mogą zajmować kontekst jeszcze przed odczytaniem pliku zadania. Drugi pracownik powtarza część tego narzutu i tworzy raport, który główny agent musi sprawdzić. Do edycji dwóch plików wystarczy jeden agent. Przy niezależnym przeszukiwaniu wielu źródeł krótki raport pracownika może ograniczyć kontekst głównej sesji, choć całkowite zużycie tokenów wzrośnie.

## Przygotuj zwięzłe przekazanie

**Przekazanie pracy to krótki zapis dla kolejnej sesji.** Oddziela pracę wykonaną od proponowanej. Zapisz ten przykład poza laboratorium w `course-notes/handoff.md` i zastąp przykładowe obserwacje własnymi.

```text
Cel: dodać --status open|done do raportu zadań kursu.
Źródło: docs/requirements.md, wersja 1.
Obszar roboczy: rozpakowany folder effective-ai-course-lab.
Aktualny stan: filtr statusu znajduje się w task_report.py i testach.
Zweryfikowano: zapisz zaobserwowany wynik testów i ręczne liczby 4, 2 i 2.
Decyzja: tasks.json pozostał bez zmian.
Oczekuje: niezależny przegląd diffu i źródła.
Następne sprawdzenie: ponownie uruchom testy i przypadek nieprawidłowego statusu.
Zatrzymaj się, jeśli: wymaganie lub wartość bazowa różni się od powyższego zapisu.
```

**Przykład nie twierdzi, że wykonałeś te działania.** Zapisz zaobserwowane wyniki testów i zmienione pliki. Jeśli zmieni się wersja źródła, zaktualizuj przekazanie po ponownym odczytaniu źródła.

## Sprawdź nową sesję

**Uruchom w laboratorium nowy czat lub sesję agenta programistycznego.** W czacie wklej przekazanie i plik `AGENTS.md` z syntetycznego laboratorium, a także wskaż pliki do sprawdzenia. W agencie programistycznym otwórz katalog laboratorium i wklej przekazanie, zapewniając dostęp do odczytu wskazanych plików. Zapytaj:

```text
Na podstawie tego przekazania i aktualnych plików repozytorium podaj zatwierdzone wartości statusu, liczbę bazową i następne sprawdzenie. Niczego nie edytuj.
Jeśli przekazanie jest sprzeczne z aktualnym źródłem, zgłoś konflikt.
```

**Oczekiwane rozumowanie:** nowa sesja znajduje `open` i `done` w `docs/requirements.md`, podaje wartość początkową 4 oraz wymienia testy i kontrole ręczne. Jeśli powtórzy starszą wartość `pending`, ponownie odczytaj wymaganie i popraw przekazanie.

## Zachowaj małego koordynatora

**Koordynator to główny agent, który kieruje pracownikami.** Przydziel każdemu pracownikowi wąskie pytanie i nazwane pliki wejściowe. Poproś o krótki wynik: ustalenie, ścieżkę dowodu, pewność i nierozwiązany problem. Szczegółowe logi zachowaj w pliku albo sesji pracownika. Przekaż głównemu agentowi tylko informacje potrzebne do kolejnej decyzji.

**Przykład:** poproś pracownika z dostępem tylko do odczytu o sprawdzenie testów i odpowiedź „brakujący przypadek, plik i wiersz, sugerowana kontrola”. Nie proś o wklejenie wszystkich testów do głównego czatu. Główny agent sprawdza ustalenie w repozytorium przed edycją. [Lekcja o delegowaniu](/articles/effective-ai-agent-delegation/) dodaje niezależne zadanie pracownika, gdy jego zakres uzasadnia koszt.

**W wielu produktach sesje pracowników mają własny kontekst,** ale dziedziczenie i izolacja działają różnie. Sprawdź aktualne zasady produktu, zanim założysz, że pracownik widzi te same instrukcje, pliki i narzędzia co główny agent. Przewodniki po [subagentach Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents) i [subagentach Claude Code](https://code.claude.com/docs/en/sub-agents) opisują działanie tych produktów.

## Ostrożnie stosuj kompaktowanie

**Kompaktowanie skraca aktywną historię.** Codex, Claude Code i OpenCode różnią się czasem i sposobem kompaktowania. Traktuj skompaktowane podsumowanie jako pomoc w kontynuacji, a nie pełny zapis projektu. Zapisuj wymagania i decyzje w plikach, a po kompaktowaniu sprawdź je ponownie. Zapoznaj się z aktualnymi wskazówkami dotyczącymi [dobrych praktyk Codex](https://learn.chatgpt.com/docs/learn/best-practices), [poleceń Claude Code](https://code.claude.com/docs/en/commands) i [kompaktowania OpenCode 2](https://opencode.ai/v2/docs/compaction). OpenCode 1 i OpenCode 2 używają różnych schematów. Przed kopiowaniem ustawień sprawdź `opencode --version`.

**Jeśli asystent zgubi ograniczenie,** zatrzymaj edycję, ponownie otwórz źródło i przedstaw pakiet zadania od nowa. Nowa sesja z krótkim, zweryfikowanym przekazaniem często wymaga mniej uwagi niż wielokrotne poprawianie długiego, zagubionego czatu.

## Ćwicz i sprawdź

**Twój artefakt:** przekazanie krótsze niż 180 słów, zapisane poza laboratorium. Oznacz każdy wiersz jako źródło, zaobserwowany wynik, decyzję albo oczekujące działanie. Przekaż je nowej sesji i zanotuj, czy wskazała obie dozwolone wartości statusu i następne sprawdzenie.

**Kontrola końcowa:** nowa sesja podaje `open`, `done`, wartość początkową 4 i krok testowy bez korzystania ze starego czatu. Uzupełnij braki i powtórz test w kolejnej nowej sesji.

## Sprawdź swoją wiedzę

1. **Pytanie:** co należy umieścić w przekazaniu dla nowej sesji? **Odpowiedź:** cel, autorytatywne źródło, aktualny stan, sprawdzony wynik i następne działanie.

2. **Pytanie:** dlaczego raport pracownika powinien być krótki? **Odpowiedź:** zwięzły raport z dowodami przekazuje koordynatorowi potrzebny wynik bez powtarzania całej transkrypcji pracownika.

## Rozwiązywanie problemów

- **Podsumowanie pomija decyzję:** dodaj krótki wiersz z decyzją i wersją źródła.
- **Odpowiedź pracownika jest ogromna:** poproś o ograniczoną tabelę dowodów i odwołania do plików.
- **Przekazanie jest nieaktualne:** przed kolejną edycją ponownie przeczytaj aktualne pliki źródłowe.
- **Brakuje miejsca na kontekst:** podziel zadanie na mniejsze sesje z osobnymi artefaktami.

## Następne kroki

**Przejdź do [konfiguracji serwera MCP](/articles/effective-ai-mcp-server-setup/)**. Dodasz zewnętrzne narzędzie tylko do odczytu i ograniczysz jego wyjście.

**Nawigacja kursu:** [Wstecz: pierwsze zadanie programistyczne](/articles/effective-ai-coding-agent-first-task/), [Plan kursu](/effective-ai-course-start/).
