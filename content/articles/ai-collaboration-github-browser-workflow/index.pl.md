---
title: "Workflow AI w GitHub dla osób bez kodowania: Issues i pull requesty"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Korzystaj z edycji w przeglądarce, zgłoszeń, pakietów kontekstu czatu i sprawdzonych pull requestów bez lokalnego środowiska programistycznego."
genre: ["Sztuczna inteligencja", "Współpraca zespołowa", "Inżynieria oprogramowania"]
tags: ["kurs współpracy AI", "edycja GitHub w przeglądarce", "GitHub Issues", "pull request", "współtwórcy bez kodowania", "pakiet kontekstu", "przekazanie do przeglądu"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustracja przedstawiająca specjalistów sprawdzających wspólną pracę nad projektem w środowisku cyberbezpieczeństwa"
coverCaption: ""
---

[Powrót do kursu współpracy AI](/ai-collaboration-course-start/)

**Współtwórcy, którzy nie programują, stosują te same zasady autorytetu w przeglądarce.** Czytasz źródła w GitHub, przygotowujesz szkic zatwierdzonym narzędziem czatu i wysyłasz Issue albo edycję gałęzi. Opiekun repozytorium uruchamia kontrole i publikuje po przeglądzie. Stosuj ten workflow po włączeniu ochrony repozytorium, aby dostęp z przeglądarki nie omijał zabezpieczeń agentów programistycznych.

## Najważniejsze wnioski

- **Praca w przeglądarce** nie wymaga lokalnego terminala.
- **Pakiety kontekstu** zachowują zakres i dowody rewizji.
- **Issues i gałęzie** pozostają propozycjami.
- **Przekazanie pracy** wskazuje otwarte zadania i następną rolę.

## Zanim zaczniesz

**Wymagania wstępne:** [lekcja o granicach repozytorium](/articles/ai-collaboration-github-repository/), dostęp do odczytu w laboratorium oraz zatwierdzone narzędzie czatu, jeśli chcesz go użyć. **Szacowany czas:** 45–60 minut. **Poziom trudności:** podstawowy. Osoby tworzące tylko Issue pomijają lokalny Git i Actions. Współtwórcy wysyłający PR współpracują z opiekunem, który ukończył [lekcję o agentach i Actions](/articles/ai-collaboration-github-agents-actions/).

**Podstawowy wariant bez łącznika:** samodzielnie otwórz GitHub i udostępniaj wyłącznie syntetyczne fragmenty. Nie zakładaj dostępności funkcji czatu z subskrypcji. Jeśli dostawca nie jest zatwierdzony, przygotuj szkic ręcznie z użyciem tych samych rekordów.

**Wynik:** przekaż jedno Issue lub PR ze stałymi rewizjami źródeł, proponowanym tekstem, listą zmienionych plików, wyłączeniami i nierozstrzygniętymi pytaniami.

## Przeczytaj pakiet źródłowy

1. **Otwórz MAP-01 w gałęzi `main`**, a następnie znajdź POL-01, REQ-17 i RUN-04.
2. **Przeczytaj każde źródło** i zapisz rewizję commitu z widoku commitów w przeglądarce.
3. **Skopiuj odpowiednie syntetyczne fragmenty** wraz z nazwami plików, rewizjami, zakresem i wyjątkami.
4. **Oznacz pakiet jako migawkę**, dopóki opiekun nie porówna go z aktualnymi źródłami przed publikacją.

```text
Project: export-service-lab
Task: PROP-042 draft, no publication permission
Authority: requirement.json, REQ-17 revision 1
Baseline: retention_days 7
Policy: POL-01 version 1
Requested proposal: retention_days 30
Evidence: attach browser-verified commit references
Missing evidence: no runtime deletion observations
Output: proposed wording, affected files, questions, rollback
Stop: source unavailable, changed revision, conflicting authority
```

**Dołącz prywatnie rzeczywiste rewizje z piaskownicy.** Szablon nie zawiera gotowych dowodów. Poproś asystenta o wskazanie brakujących rekordów przed rekomendowaniem publikacji.

**Wypełniony pakiet syntetyczny przed odczytem źródła na żywo:**

```text
Project: export-service-lab
Task: draft PROP-042 in an Issue
Approved baseline: REQ-17 revision 1, retention_days 7
Proposal: retention_days 30, synthetic export files only
Affected records: requirement.json, config.json, proposal.json, runbook.md
Exclusions: production data, backups, legal holds
Known evidence: supplied lab baseline files
Missing evidence: current main commit, owner decisions, runtime deletion result
Status: Draft, publication blocked until current revisions and reviews exist
Next role: maintainer supplies verified main commit and runs checks
```

**Pakiet jest kompletnym szkicem zgłoszenia.** Brakujące dowody wskazano celowo. Przed prośbą o publikację zastąp bazę z laboratorium rewizjami z aktywnej piaskownicy.

## Otwórz Issue

**Wybierz Issues, New issue** i nadaj tytuł **`PROP-042: propose thirty-day synthetic retention`**. Wklej ten opis i dołącz pakiet źródłowy.

```text
Proposal: PROP-042
Status: Draft
Current approved value: 7 days, REQ-17 revision 1
Requested value: 30 days
Reason: fictional pilot requirement, not compliance advice
Scope: synthetic export records only
Affected files: requirement.json, config.json, runbook.md
Evidence: source revisions and policy version attached
Reviewers: product-owner and operations-owner
Implementation reviewer: repository-maintainer
Acceptance: consistent records, denied publication, fresh handoff
Rollback: reviewed restoration of the approved baseline
```

**Poproś czat o porównanie propozycji z pakietem**, listę założeń i szkic pytań do właścicieli. Zapisz szkic w Issue. Nie proś czatu o zatwierdzenie zmiany i nie traktuj wątku rozmowy jako rejestru decyzji.

## Wprowadzaj zmiany w przeglądarce

1. **Otwórz kartę Code repozytorium.** Rozwiń menu gałęzi nad listą plików, potwierdź **`main`**, wpisz **`proposal-042`** i wybierz **Create branch: proposal-042 from main**. Jeśli nie możesz utworzyć gałęzi, użyj zatwierdzonego forka albo ścieżki Issue poniżej.
2. **Przed otwarciem pliku potwierdź `proposal-042` w menu gałęzi.** Wybierz plik i ikonę ołówka. Edytor internetowy GitHub nie zmienia chronionej gałęzi.
3. **Zmień wymaganie** na trzydzieści dni i rewizję 2. Przed każdą kolejną edycją ponownie otwórz menu gałęzi. Konfigurację i instrukcję zmień na tej samej gałęzi.
4. **Edytuj `proposal.json`**, ustawiając to_days 30, from_days 7 i base_revision 1.
5. **Wyświetl podgląd Markdown** i sprawdź interpunkcję JSON. Zapisz każdą edycję z przeglądarki w gałęzi **`proposal-042`**.
6. **Otwórz Pull requests, a następnie New pull request.** Porównaj **`proposal-042`** z **`main`**, sprawdź zmiany we wszystkich czterech plikach i utwórz PR powiązany z Issue. Poproś opiekuna o dołączenie nowego manifestu z chronionej bazy i uruchomienie kontroli spójności.
7. **Poproś właścicieli o przegląd** końcowej rewizji propozycji. Nie zamykaj dostawy, dopóki przegląd i odczyt kontrolny nie zakończą się powodzeniem.

**Zapis nawigacji:** zanotuj nazwę repozytorium, numer Issue, gałąź propozycji, ścieżki zmienionych plików, numer PR, nazwę uruchomionej kontroli, rewizję poddaną przeglądowi i końcowy commit `main`. Ponownie znajdziesz te dane w widokach Issues, Code, Pull requests, Actions oraz PR Checks/Reviews. Jeśli GitHub przeniesie kontrolkę, znajdź ten sam rekord po numerze lub ID commitu, zamiast zgadywać na podstawie zrzutu ekranu. Wyeksportuj prywatną notatkę dowodową z adresami rekordów i zaobserwowanym stanem. Przed udostępnieniem jej poza upoważnionym zespołem usuń nazwy kont, adresy e-mail, tokeny, identyfikatory tenantów i niepowiązane dane repozytoriów. Nieocenzurowane dowody przechowuj wyłącznie w zatwierdzonym prywatnym miejscu.

**Dokumentacja GitHub opisuje ścieżki współtworzenia przez gałęzie i forki.** Osoba bez prawa zapisu w repozytorium używa zatwierdzonego forka albo ścieżki Issue. Fork nie daje prawa publikacji w oryginalnym repozytorium.

## Sprawdź gotowy diff

| Plik | Baza | Kandydat |
|---|---|---|
| **Wymaganie** | Rewizja 1, siedem dni | Rewizja 2, trzydzieści dni |
| **Konfiguracja** | Siedem dni | Trzydzieści dni |
| **Instrukcja** | `Retention days: 7` | `Retention days: 30` |
| **Propozycja** | From 7, to 7 | From 7, to 30, base 1 |
| **Manifest** | Nie zapisano | Skróty chronionych źródeł sprzed zmiany |

**Manifest opisuje bazę**, a nie proponowany tekst o trzydziestu dniach. Użycie skrótu wymagania-kandydata jako dowodu bazy powoduje niezgodność z zaufaną bazą.

## Weryfikacja i przekazanie

**Test pozytywny:** opiekun scala zmianę po przeglądzie właścicieli i pomyślnych kontrolach. Otwórz wynikowe pliki w **`main`** i potwierdź ich zgodność. Dołącz do Issue powstały commit i odczyt kontrolny. Potwierdza to zatwierdzoną konfigurację, a nie działanie usługi usuwania w czasie wykonywania.

**Test negatywny:** poproś czat o zatwierdzenie lub publikację propozycji. Zgodnie z polityką powinien zwrócić wyłącznie szkic. Osobno spróbuj opublikować bezpośrednio jako współtwórca i zapisz odmowę platformy wraz z niezmienioną rewizją źródła. Nie łącz testów zachowania z kontrolą dostępu.

```text
Handoff: HANDOFF-042
Proposal: PROP-042
Policy: POL-01 version 1
Sources: attach current requirement, runbook, and config revisions
Published value: record after reading main
Completed: merged files and check reference
Remaining: runtime deletion service not tested
Next role: operations-owner
Next action: independent source read and runbook verification
Stop: changed source, missing access, conflicting authority
```

**Rozpocznij nową sesję tylko z mapą i przekazaniem.** Wymagaj ponownego odczytu źródła albo wyraźnej prośby o dowody z przeglądarki. Asystent ma odtworzyć wartość z rekordów źródłowych, a nie powtarzać wcześniejsze podsumowanie.

## Przygotuj szkic bez utraty kontekstu

**Współtwórca pracujący w przeglądarce nadal potrzebuje kompletnego pytania.** „Zmień okres przechowywania na trzydzieści dni” pomija aktualne źródło, zakres, stan przeglądu i zmieniane rekordy. Przekaż czatowi pakiet źródłowy i instrukcję przygotowania szkicu. Jeśli brakuje rekordu, poproś opiekuna o zatwierdzone dowody zamiast zastępować je zapamiętanym tekstem.

```text
Draft an Issue for PROP-042 from the attached synthetic source packet.
Keep seven days labeled as the approved baseline.
Keep thirty days labeled as proposed intent.
Preserve exclusions for production data, backups, and legal holds.
List requirement, configuration, proposal, and runbook changes.
List missing evidence instead of filling it with guessed revisions.
Do not claim owner approval or delivered behavior.
```

**Przed skopiowaniem sprawdź odpowiedź.** Ustal, czy zmieniła zakres, wymyśliła commit albo opisała zgodę jako zakończoną. Usuń niepoparte twierdzenia i pozostaw otwarte pytania w Issue. Czat pomaga napisać propozycję, ale nie dostarcza dowodów z systemów, których nie przeczytał.

## Wybierz ścieżkę współtworzenia

| Sytuacja | Ścieżka | Wynik |
|---|---|---|
| **Tylko dostęp do odczytu** | Issue ze stałym proponowanym tekstem | Prośba o zmianę gotowa dla opiekuna |
| **Zatwierdzony dostęp do gałęzi** | Edycje w przeglądarce na jednej gałęzi propozycji | PR z powiązanymi zmianami plików |
| **Zatwierdzona ścieżka forka** | Fork i PR do repozytorium nadrzędnego | Kandydat oczekujący na przegląd nadrzędny |
| **Brak dostępu do źródeł** | Zatrzymaj pracę i poproś o zatwierdzone dowody | Jawnie zablokowane zadanie |

**Ścieżka Issue to pełny wkład**, a nie nieudane ćwiczenie z kodowania. Przekazujesz zamierzoną zmianę, dowody, zakres i pytania do przeglądu. Opiekun przygotowuje poprawkę i manifest. Następnie sprawdzasz, czy poprawka odpowiada Twojej prośbie.

| Ścieżka | Warunek ukończenia przez współtwórcę | Przekazanie opiekunowi |
|---|---|---|
| **Tylko Issue** | Issue zawiera zweryfikowany pakiet źródłowy, stały proponowany tekst, wyłączenia i otwarte pytania | Opiekun tworzy gałąź, uruchamia kontrole i linkuje PR |
| **PR** | Jedna gałąź zawiera wszystkie zmieniane pliki, diff PR odpowiada propozycji, a recenzenci otrzymują końcową rewizję | Opiekun uruchamia kontrole, uzyskuje przegląd właścicieli, scala zmianę i zapisuje odczyt kontrolny |

**Podczas edycji w przeglądarce pozostań na gałęzi propozycji.** Po utworzeniu gałęzi przez pierwszą edycję, otwieraj pozostałe pliki z tego samego selektora. Na koniec sprawdź diff PR. Cztery osobne gałęzie dadzą cztery niekompletne zmiany zamiast jednego pakietu do przeglądu.

## Sprawdź proponowany tekst

**Przykład nieprecyzyjnego tekstu:** „Eksporty są teraz dostępne przez trzydzieści dni”. Brzmi jak zakończone wdrożenie i pomija syntetyczny zakres. Dopóki trwa przegląd, używaj sformułowania propozycji.

```text
Proposed intent:
Retain synthetic export files for 30 days.
Exclude production data, backups, and legal holds.

Current approved intent:
Retain synthetic export files for 7 days under REQ-17 revision 1.

Delivery:
Not published. No runtime deletion service was tested.
```

**Porównaj każdy zmieniany plik z tym tekstem.** W kandydacie rewizja wymagania przechodzi na wyższy numer. Konfiguracja wskazuje trzydzieści dni. Pierwszy wiersz instrukcji również wskazuje trzydzieści, zachowując ograniczenie laboratorium. Propozycja nadal podaje siedem jako poprzednią wartość i rewizję 1 jako bazę.

**Pytaj o niezgodności, zamiast naprawiać nieznane ustawienia.** Jeśli poprawka opiekuna osłabia też ochronę albo usuwa politykę, poproś o wyjaśnienie i osobny przegląd. Nie musisz rozumieć każdej linijki workflow, aby zauważyć zmianę poza zakresem prośby.

## Odpowiedz na uwagi z przeglądu

**Przykładowa uwaga:** zespół operacyjny prosi o zdanie wyjaśniające, że przywrócenie konfiguracji nie odzyskuje usuniętych plików. Zaktualizuj szkic na tej samej gałęzi i poinformuj recenzentów o zmienionym zakresie. Końcowy przegląd musi dotyczyć poprawionej propozycji, a nie wcześniejszej kopii z czatu.

| Uwaga z przeglądu | Działanie współtwórcy |
|---|---|
| **Brak wyłączenia** | Przywróć sformułowanie i poproś o przegląd intencji |
| **Nieaktualna rewizja źródła** | Uzyskaj nowy zatwierdzony pakiet i uzgodnij zmiany |
| **Brak manifestu** | Poproś opiekuna o zapisanie chronionej bazy |
| **Niezwiązana zmiana kontroli** | Oddziel ją lub usuń przed przeglądem |
| **Nieprzetestowane twierdzenie o działaniu** | Zastąp je dokładnym ograniczeniem laboratorium |

**Pozostaw pytania widoczne do czasu uzyskania odpowiedzi.** Zamknięcie komentarza bez rozwiązania problemu usuwa ważny sygnał. Dodaj w odpowiedzi link do poprawki lub dowodu, aby kolejny recenzent mógł odtworzyć decyzję bez czytania całej rozmowy.

## Kontrola ukończenia pracy w przeglądarce

**Przekaż Issue lub PR, które inny opiekun wykona bez zgadywania.** Pakiet zawiera źródła, proponowany tekst, zmieniane rekordy, wyłączenia, role właścicieli i nierozstrzygnięte pytania. Po publikacji zapisz odczyt kontrolny oddzielnie od pierwotnej propozycji.

**Samokontrola:** przekaż pakiet osobie, która nie widziała Twojego czatu. Poproś ją o odróżnienie wartości żądanej, zatwierdzonej i opublikowanej. Jeśli uzna, że trzydzieści dni już wdrożono przed scaleniem, popraw etykiety pakietu. Taką samą dyscyplinę stosuj w ścieżce pracy zespołowej.

| Bramka przeglądu | Warunek zaliczenia |
|---|---|
| **Rewizje źródeł** | Każdy wskazany commit lub wersja strony otwiera się w piaskownicy. Nieznane rewizje pozostają Brakujące. |
| **Wyłączenia** | Dane produkcyjne, kopie zapasowe i blokady prawne pozostają poza propozycją. |
| **Pytania** | Nierozstrzygnięte pytania do właścicieli lub źródeł pozostają widoczne w Issue albo PR. |
| **Aktualność zatwierdzeń** | Przeglądy wskazują końcową rewizję propozycji. Wcześniejsza zgoda nie obejmuje późniejszych zmian. |

**Nieudana bramka wstrzymuje publikację.** Osoba tworząca samo Issue przekazuje wynik opiekunowi. Autor PR po poprawkach prosi o kolejny przegląd.

## Rozwiązywanie problemów i wycofanie

**Brak prawa do edycji:** użyj Issue lub zatwierdzonego forka. **Wymyślony commit:** zastąp go zweryfikowanym dowodem i ponownie przejrzyj szkic. **Zgoda sprzed zmian:** poproś o nową zgodę.

**Wycofanie:** zamknij niescalony PR, zachowując jego dowody. Dla scalonej treści poproś opiekuna o propozycję chronionego revertu. Nie zmieniaj bazy, aby upozorować udane odzyskiwanie.

## Ćwiczenie i samokontrola

**Nie udostępniaj nowemu asystentowi rekordu wymagania** i poproś go o rekomendację publikacji.

**Oczekiwane rozumowanie:** prosi o autorytatywny dowód albo oznacza odpowiedź jako opartą na migawce. Publikacja pozostaje zablokowana do czasu udanego, świeżego odczytu.

## Główne źródła

- **Edycja w przeglądarce:** [edytowanie plików](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).
- **Granice przeglądu:** [chronione gałęzie](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Następne kroki

**Przejdź do [Konfiguracji Confluence i Jira](/articles/ai-collaboration-confluence-jira-setup/)**, aby powtórzyć ten model pracy w systemach zespołowych.
