---
title: "Konfiguracja kursu o przepływie pracy z AI: terminal, Git i laboratorium ćwiczeniowe"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Przygotuj bezpieczne miejsce do ćwiczeń z AI, poznaj używane w kursie pojęcia dotyczące terminala i Git oraz uruchom laboratorium startowe."
genre: ["Sztuczna inteligencja", "Inżynieria oprogramowania", "Edukacja"]
tags: ["konfiguracja kursu AI", "podstawy terminala", "podstawy Git", "wymagania dla agentów programistycznych", "laboratorium ćwiczeń AI", "kurs AI dla początkujących"]
cover: "/img/cover/effective-ai-course-setup.webp"
coverAlt: "Miejsce do ćwiczeń dla początkujących z symbolami terminala, Pythona i Git, zaznaczonym folderem laboratorium i archiwum do resetowania"
coverCaption: ""
---

[Wróć do praktycznego kursu przepływu pracy z AI](/effective-ai-course-start/)

**Przygotuj bezpieczne miejsce do ćwiczeń, zanim użyjesz agenta.** Lekcje 1 i 2 działają w przeglądarce bez tego laboratorium. Wróć tu przed lekcją 3, jeśli chcesz ukończyć cały kurs. Praktyczne lekcje programowania wymagają Git, Pythona 3.10 lub nowszego oraz jednego agenta programistycznego. W ścieżce do samodzielnej nauki oznaczone zadania ręczne zastępują niedostępne działania agenta.

**Cel nauki:** uruchomisz laboratorium startowe, zapiszesz lokalny stan bazowy i wyjaśnisz, jak zresetować tymczasową kopię.

## Najważniejsze informacje

- **Ścieżka przeglądarkowa:** wykonaj ćwiczenia z czatu, planowania, sprawdzania źródeł i przeglądu w ChatGPT lub Claude.
- **Ścieżka lokalna:** użyj terminala i dostarczonego laboratorium Python do ćwiczeń programistycznych.
- **Ścieżka resetu:** rozpakuj nową kopię laboratorium, gdy ćwiczenie się nie powiedzie.
- **Zasada bezpieczeństwa:** prywatne pliki, dane klientów i dane logowania trzymaj poza laboratorium.

## Wybierz ścieżkę

| Ścieżka | Wymagania | Ćwiczenia |
|---|---|---|
| **Wprowadzenie w przeglądarce** | Aktualna przeglądarka i konto ChatGPT lub Claude | Lekcje 1 i 2 oraz pakiet zadań czatu z lekcji 1 |
| **Ćwiczenia lokalne** | Git, Python 3.10 lub nowszy, terminal i jeden agent programistyczny | Pliki, różnice, testy i zmiany agenta |
| **Kurs do samodzielnej nauki** | Przeglądarka, lokalny Python 3.10 lub nowszy i Git | Pełne kontrole laboratorium; niedostępne kroki agenta i MCP oznacz jako niewykonane |

**Każdy produkt sam określa plany i ograniczenia.** Przed poleganiem na funkcji sprawdź [ChatGPT Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) i [Claude Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects). Ścieżka do samodzielnej nauki nie potwierdza praktycznej umiejętności obsługi niedostępnego agenta programistycznego. Zapisz tę różnicę w notatkach końcowych.

**Korzystaj z jednej podstawowej ścieżki:** ChatGPT w przeglądarce do ćwiczeń czatu, a potem dostępny agent programistyczny z lokalnym laboratorium. Claude to równoważna opcja do czatu. Do programowania możesz wybrać Codex CLI, Claude Code CLI lub OpenCode. Nie potrzebujesz kont u wszystkich dostawców.

**Zapisz pięć kontroli wstępnych przed uruchomieniem agenta programistycznego.** Dzięki nim odróżnisz kontrolę lokalnego laboratorium od twierdzenia o koncie lub hostowanym środowisku pracy.

| Kontrola | Zapisz |
|---|---|
| **Środowisko pracy** | Dokładny folder rozpakowanego laboratorium, który agent odczyta |
| **Wykonanie** | Komputer lokalny lub wybrane środowisko zdalne |
| **Dostawca** | Konto lub dostawca modelu używany w tym zadaniu |
| **Uprawnienia** | Czy zapis plików i polecenia powłoki są dozwolone, czy wymagają zgody |
| **Stan bazowy** | Zaobserwowana liczba i dwa zaliczone testy przed edycją |

**Ogranicz katalog główny ćwiczeń.** Hostowane środowisko potrzebuje własnej kopii syntetycznego laboratorium. Lokalny przebieg nie dowodzi, że kopia zdalna lub konto mają te same pliki i uprawnienia.

## Poznaj lokalne pojęcia

| Pojęcie | Proste znaczenie |
|---|---|
| **Terminal** | Aplikacja do wpisywania poleceń |
| **Powłoka** | Oprogramowanie interpretujące polecenia |
| **CLI** | Interfejs wiersza poleceń programu |
| **Katalog roboczy** | Folder używany domyślnie przez polecenie |
| **Repozytorium** | Projekt śledzony przez Git |
| **Commit** | Zapisana migawka Git |
| **Gałąź** | Nazwana linia zmian Git |
| **Diff** | Widok dodanych lub usuniętych wierszy |
| **Sprawdzenie** | Powtarzalne sprawdzenie oczekiwanego działania |
| **Kod wyjścia** | Liczba informująca o sukcesie lub porażce polecenia |

**Do laboratorium startowego nie potrzebujesz GitHub.** Git działa na twoim komputerze. GitHub to osobna usługa hostingu. Lokalny commit zapisuje migawkę bez wysyłania plików.

## Przygotuj laboratorium

**Pobierz [laboratorium startowe kursu](/downloads/effective-ai-course-lab.zip)** i rozpakuj je do nowego folderu, który kontrolujesz. Otwórz terminal w tym folderze. W macOS lub Linux otwórz Terminal i użyj `cd`, aby przejść do rozpakowanego katalogu. W Windows użyj PowerShell lub Windows Terminal oraz `cd`. W Windows polecenie Python to często `py -3` zamiast `python3`.

**W razie potrzeby zainstaluj [Python 3.10 lub nowszy](https://www.python.org/downloads/) i [Git](https://git-scm.com/downloads).** Przed uruchomieniem laboratorium sprawdź zainstalowane narzędzia. Dwa pierwsze polecenia wypisują wersje. `cd` zmienia katalog roboczy, a `ls` wyświetla pliki. Zastąp przykładową ścieżkę rzeczywistą ścieżką do rozpakowanego folderu.

```bash
python3 --version
git --version
cd /path/to/effective-ai-course-lab
ls
```

**W Windows PowerShell** użyj `py -3 --version`, `git --version`, `cd C:\path\to\effective-ai-course-lab` i `Get-ChildItem`. Lista powinna zawierać `task_report.py`, `tasks.json`, `tests` i `docs`. Jeśli polecenie wersji zawiedzie, dokończ instalację przed kontynuowaniem.

```bash
pwd
python3 task_report.py tasks.json
python3 -m unittest discover -s tests -v
```

**W Windows PowerShell** zastąp `pwd` poleceniem `Get-Location`, jeśli wolisz, a `python3` poleceniem `py -3`, gdy Python korzysta z launchera. Pierwsze polecenie pokazuje ścieżkę zakończoną folderem laboratorium. Sprawdź również nazwy plików. `AGENTS.md.txt` nie zastępuje `AGENTS.md`. W Eksploratorze plików włącz rozszerzenia nazw, aby widzieć pełną nazwę.

**Oczekiwany wynik:** raport podaje `Total tasks: 4`. Polecenie testów wymienia dwa testy i kończy się wynikiem `OK`. Po sukcesie powłoka zwraca kod wyjścia zero. Inna liczba lub traceback oznacza, że trzeba sprawdzić folder i konfigurację Pythona.

**Czytaj polecenia na części.** W `python3 task_report.py tasks.json` program `python3` uruchamia Pythona, `task_report.py` jest programem, a `tasks.json` wskazuje dane wejściowe. Wypisana liczba to wynik, nie następne polecenie. Po błędzie macOS i Linux wyświetlają stan przez `echo $?`. PowerShell udostępnia status ostatniego natywnego programu przez `$LASTEXITCODE`.

**Po instalacji Pythona zaplanuj około dziesięciu minut na pierwsze uruchomienie:** rozpakuj laboratorium, uruchom raport i porównaj sumę z czterema wpisami w `tasks.json`. Otwórz JSON w edytorze tekstu i policz wpisy samodzielnie.

## Ćwicz bezpiecznie z Git

**Uruchom Git tylko w rozpakowanym folderze laboratorium.** Te polecenia zapisują lokalną migawkę. `git status` pokazuje zmienione pliki. `git diff` pokazuje zmienione wiersze po edycji śledzonego pliku.

```bash
git init
git add .
git commit -m "Stan bazowy laboratorium kursu"
git status --short
```

**Oczekiwany stan:** po commicie nie wyświetlają się nazwy plików. Jeśli Git pyta o imię i e-mail, ustaw w tym folderze tożsamość przeznaczoną tylko do laboratorium i ponów commit. Zastąp przykładowe wartości prywatnymi. Nie wklejaj danych tożsamości ani dostępu do publicznego czatu.

```bash
git config --local user.name "Osoba ucząca się"
git config --local user.email "learner@example.invalid"
git commit -m "Stan bazowy laboratorium kursu"
git status --short
```

**Reset nie wymaga polecenia Git.** Zapisz notatki poza laboratorium, usuń rozpakowaną kopię ćwiczeniową i ponownie rozpakuj oryginalny ZIP. Zrób tak, gdy zmiana z lekcji pozostawi program w nieznanym stanie.

## Chroń miejsce do ćwiczeń

**Używaj syntetycznych przykładów.** Nie przesyłaj prywatnych dokumentów do projektu kursu. Nie umieszczaj kluczy API w promptach, plikach źródłowych, zrzutach ekranu ani commitach. Dostęp agenta do plików i poleceń zależy od uprawnień i otwartego folderu. Sprawdź oba elementy, zanim pozwolisz mu działać.

**Przed przesłaniem sprawdź udostępnianie.** Pliki projektu mogą być dostępne dla członków projektu. W rzeczywistej pracy stosuj politykę swojej organizacji. Kurs używa fikcyjnych danych, więc samo laboratorium nie wymaga specjalnej zgody.

## Ćwicz i sprawdź

**Twój wynik:** zapisz wybraną ścieżkę, pięć pól kontroli wstępnej, liczbę z raportu, wynik testów i metodę resetu. Użyj nowej kopii laboratorium, aby potwierdzić, że umiesz je zresetować.

**Oczekiwany wniosek:** wiesz, którego folderu dotyczą polecenia, odróżniasz lokalny Git od hostingu i masz sposób odzyskiwania przed edycją plików przez agenta.

## Sprawdź zrozumienie

1. **Pytanie:** Czy wprowadzenie wyłącznie w przeglądarce kończy lokalną ścieżkę laboratorium? **Odpowiedź:** Nie. Pełna ścieżka wymaga lokalnego stanu bazowego Pythona i Git.

2. **Pytanie:** Co należy zachować przed zmianą tymczasowego laboratorium? **Odpowiedź:** Wynik zaliczonego testu startowego i czysty punkt przywracania.

## Rozwiązywanie problemów

- **Brak polecenia Python:** zainstaluj Python 3 z oficjalnego źródła i ponownie otwórz terminal.
- **Nie znaleziono pliku:** sprawdź katalog roboczy i wyświetl pliki rozpakowanego folderu.
- **Testy się nie uruchamiają:** użyj dokładnego polecenia z pliku README rozpakowanego laboratorium.
- **Git prosi o tożsamość do commitu:** skonfiguruj Git lokalnie i nie zapisuj wybranych wartości w notatkach kursu.

## Następne kroki

**Przejdź do [niezawodnego przepływu pracy z AI](/articles/effective-ai-workflow-foundations/)**. Pierwsze ćwiczenie używa tego samego syntetycznego warsztatu, zanim dowolne narzędzie otrzyma prawdziwe pliki.

**Nawigacja kursu:** [Plan kursu](/effective-ai-course-start/).
