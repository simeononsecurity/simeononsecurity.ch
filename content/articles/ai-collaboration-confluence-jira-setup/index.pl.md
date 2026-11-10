---
title: "Konfiguracja AI w Confluence i Jira: uprawnienia i źródła obowiązujących zasad"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Skonfiguruj wiążące strony Confluence i uprawnienia w zarządzanej przez firmę Jira do przeglądanej współpracy między zespołami."
genre: ["Sztuczna inteligencja", "Współpraca zespołowa", "Inżynieria oprogramowania"]
tags: ["kurs współpracy AI", "Confluence Cloud", "Jira Cloud", "wiążące strony", "schemat uprawnień Jira", "przejście w workflow", "testy dostępu"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustracja przedstawiająca specjalistów przeglądających wspólną pracę nad projektem w środowisku cyberbezpieczeństwa"
coverCaption: ""
---

[Powrót do kursu współpracy AI](/ai-collaboration-course-start/)

**Administrator ustala obowiązujące zasady w miejscu pracy, zanim podłączy narzędzia czatu.** Właściciele produktu i operacji publikują wymagania oraz instrukcje w Confluence Cloud. Jira Cloud koordynuje realizację. GitHub odpowiada za implementację. Dedykowane środowiska testowe tworzysz po przygotowaniu podstaw, ponieważ błędne nadanie uprawnień ujawnia informacje niezależnie od działania modelu.

## Najważniejsze wnioski

- **Confluence** przechowuje zatwierdzone brzmienie wymagań.
- **Jira** przechowuje stan realizacji, a nie politykę przechowywania danych.
- **GitHub** przechowuje konfigurację i wspólną politykę.
- **Testy uprawnień** wymagają odpowiednich planów i oddzielnych użytkowników.

## Zanim zaczniesz

**Wymagania wstępne:** [podstawy](/articles/ai-collaboration-pilot-foundation/), repozytorium laboratoryjne, administracja przestrzenią Confluence, administracja Jira oraz oddzielne konta współtwórcy, właściciela i wydawcy. **Szacowany czas:** 90–120 minut. **Poziom trudności:** zaawansowana administracja.

**Wymagany plan:** Confluence Free nie obsługuje ograniczeń dostępu do treści. Jira Free nie oferuje konfigurowalnych schematów uprawnień, ról przestrzeni ani schematów zabezpieczeń elementów pracy. W tym etapie użyj odpowiednich środowisk testowych w planie Standard lub wyższym. Przed testami sprawdź plan i uprawnienia na podstawie dokumentacji.

**Uwaga dotycząca nawigacji:** aktualna dokumentacja Jira używa nazw „space” i „work item”. Niektóre dzierżawy nadal używają „project” i „issue”. Wybierz konfigurację zarządzaną przez firmę. Ta procedura nie obejmuje zachowania uprawnień w konfiguracji zarządzanej przez zespół. Nie są wymagane Rovo, aplikacje z Marketplace, zatwierdzenia Jira Service Management ani płatny łącznik czatu.

**Wynik dla czytelnika:** przygotuj macierz uprawnień, nazwane strony będące źródłem obowiązujących zasad, workflow Jira tylko dla laboratorium i dowody odmowy dostępu z oddzielnych kont. Przy wynikach testów zapisz plan dzierżawy i założenia dotyczące ról.

**Przed utworzeniem rekordów sprawdź:**

| Kontrola | Jeśli jest dostępna | Jeśli jej brakuje |
|---|---|---|
| Ograniczenia stron i administracja przestrzenią Confluence | Utwórz oddzielne strony zatwierdzone i wykluczone | Oznacz testy edycji strony i odmowy odczytu jako Zablokowane |
| Schemat uprawnień Jira zarządzanej przez firmę i edytor workflow | Skopiuj schemat i workflow tylko dla laboratorium | Oznacz testy przejść jako Zablokowane |
| Oddzielne konta współtwórcy, właściciela, wydawcy i użytkownika wykluczonego | Wykonaj pozytywne i negatywne testy dla każdej roli | Oznacz nieprzetestowane role jako Zablokowane |
| Opiekun repozytorium i chroniona gałąź | Połącz sprawdzoną ścieżkę implementacji | Przed publikacją w modelu mieszanym ukończ ścieżkę opartą najpierw na GitHubie |

Od października 2026 r. używaj przycisku **Share** lub ustawienia ograniczeń strony do zarządzania dostępem do stron, obszaru uprawnień **Space settings** w Confluence do szerszych nadań oraz **Settings > Work items > Permission schemes** w Jira do skonfigurowania schematu laboratoryjnego. Edytor workflow dla Jira zarządzanej przez firmę kontroluje przejścia. Etykiety interfejsu i funkcje planu różnią się między dzierżawami. Przed wykonaniem tych kroków zapisz rzeczywistą ścieżkę i plan jako dowód. Zobacz [uprawnienia na poziomie strony Confluence](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/) oraz [schematy uprawnień Jira](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/).

## Utwórz strony źródłowe

1. **Utwórz przestrzeń Confluence** o nazwie **`Export Service Lab`**. Za pomocą dostępnych ustawień witryny i przestrzeni wyłącz dostęp anonimowy oraz udostępnianie publiczne.
2. **Utwórz opublikowane strony**, a nie dokumenty na żywo, o nazwach **`REQ-17 Export Retention`**, **`RUN-04 Export Cleanup`** i **`Decision Register`**.
3. Jako właściciel produktu **opublikuj poniższe początkowe wymaganie**. Zapisz rzeczywisty identyfikator i wersję strony w mapie repozytorium.
4. Jako właściciel operacyjny **opublikuj RUN-04** z siedmiodniowym okresem przechowywania i informacją, że w tym laboratorium nie działa zadanie usuwania.
5. Na każdej stronie źródłowej **otwórz Share**. Ustaw dostęp ogólny na tylko do odczytu dla uprawnionych członków przestrzeni, a wskazanym właścicielom i wydawcom nadaj osobne prawa edycji. Zapisz zmiany i sprawdź je na koncie współtwórcy.

```text
Source ID: REQ-17
Owner role: product-owner
Status: Approved baseline
Scope: synthetic export files only
Retention: 7 days
Delivery state: baseline lab configuration
Exceptions: production data, backups, and legal holds excluded
Approval evidence: DEC-12 baseline review
Implementation reference: attach protected GitHub baseline commit
```

**Ustaw ograniczenia na każdej stronie źródłowej.** Nie zakładaj, że ograniczenie edycji strony nadrzędnej chroni jej podstrony. Dziedziczenie odczytu i edycji działa inaczej, a uprawnienia przestrzeni nadal obowiązują. Sam odnośnik nie daje dostępu. Gdy użytkownik, który ma mieć tylko odczyt, nadal edytuje, sprawdź wszystkie członkostwa.

**Użyj poniższych treści początkowych na dwóch pozostałych stronach.** Zanim oznaczysz rekord jako zatwierdzony, zastąp tymczasowe pola przeglądu rzeczywistymi dowodami z piaskownicy.

```text
Source ID: RUN-04
Owner role: operations-owner
Status: Approved baseline
Scope: synthetic export files only
Configured retention: 7 days
Procedure: compare REQ-17 with config.json before a reviewed change
Runtime limit: this lab has no deletion job and produces no deletion evidence
Recovery: restore the prior approved configuration through review
Recovery limit: restoring configuration does not restore deleted files
Review evidence: add actual reviewer, page version, and decision reference
```

```text
Page: Decision Register
Entry ID: DEC-12
Decision: use seven days as the synthetic baseline
Scope: export-service-lab only
Requirement: REQ-17 page version, record after publication
Runbook: RUN-04 page version, record after publication
Policy: POL-01 protected GitHub revision, record after review
Product review: pending until the named owner records a decision
Operations review: pending until the named owner records a decision
Status: draft example, replace with observed review evidence
```

## Zaktualizuj mapę

```yaml
track: mixed-workplace
policy: {source_id: POL-01, home: GitHub, version: 1}
requirements: {source_id: REQ-17, home: Confluence, owner_role: product-owner}
runbook: {source_id: RUN-04, home: Confluence, owner_role: operations-owner}
decisions: {source_id: DEC-12, home: Confluence, owner_role: project-lead}
implementation: {home: GitHub, file: config.json}
delivery: {home: Jira, proposal_id: PROP-042}
snapshot_rule: repository requirement copies are not authoritative
```

**Dodaj do mapy rzeczywiste prywatne lokalizacje środowiska testowego i identyfikatory stron.** Szablon wskazuje źródła obowiązujących zasad, ale nie udaje, że zawiera aktywne adresy. Usuń z pliku README zapis przypisujący skopiowanemu plikowi JSON rolę źródła wymagań w ścieżce mieszanej.

**Zachowaj POL-01 w GitHub** dla obu ścieżek. Confluence zawiera odnośnik do sprawdzonej rewizji. Zmiana źródła polityki w trakcie zadania wymaga kolejnego przeglądu i przejścia źródła obowiązujących zasad.

## Ustaw uprawnienia Jira

1. **Utwórz laboratoryjną przestrzeń zarządzaną przez firmę** i skopiuj schemat uprawnień do oddzielnego schematu laboratoryjnego. Nie zmieniaj wspólnego schematu produkcyjnego.
2. **Otwórz Settings, Work items, Permission Schemes**, wybierz schemat laboratoryjny i zaktualizuj nadane uprawnienia.
3. **Nadaj współtwórcom uprawnienia przeglądania, tworzenia i komentowania.** Ogranicz uprawnienia administracyjne. Osobno sprawdź uprawnienia edycji i **Transition work items**.
4. **Przypisz schemat** do przestrzeni laboratoryjnej i sprawdź, czy nie współdzieli go żadna przestrzeń produkcyjna.
5. **Utwórz PROP-042** jako element pracy. Zapisz wygenerowany klucz na mapie, a PROP-042 pozostaw w opisie jako logiczny identyfikator propozycji.

**Wklej ten szkic do PROP-042.** Element Jira śledzi realizację. Jego treść nie zastępuje zatwierdzonego brzmienia w Confluence.

```text
Proposal ID: PROP-042
Status: Draft
Current approved value: 7 days, REQ-17 page version to record
Proposed value: 30 days for synthetic export files
Exclusions: production data, backups, legal holds
Affected records: REQ-17, RUN-04, config.json, proposal.json
Fixed proposal attachment: pending
Product-owner review: pending
Operations-owner review: pending
Publication ledger: pending
Stop on changed source version, missing review, or denied access
```

| Rola | Confluence | Jira | GitHub |
|---|---|---|---|
| **Współtwórca** | Odczyt zatwierdzonych stron | Tworzenie i komentowanie szkiców | Gałąź propozycji lub issue |
| **Właściciel produktu** | Przegląd wymagań | Zapis przeglądu wymagań | Przegląd dowodów PR |
| **Właściciel operacyjny** | Przegląd instrukcji | Zapis przeglądu operacyjnego | Przegląd wpływu operacyjnego |
| **Wydawca** | Edycja zatwierdzonych stron | Zapis stanu publikacji | Bez automatycznych uprawnień do scalania |
| **Opiekun repozytorium** | Odczyt wymagań | Zapis implementacji | Przegląd i scalanie chronionego PR |

**Uprawnienia z różnych grup sumują się.** Usuń w laboratorium niezamierzone szerokie uprawnienia, zamiast zakładać, że węższe nadanie je zastępuje. Nie dodawaj tożsamości łączników do grup administracyjnych.

## Ustaw stany realizacji

**Skopiuj workflow zarządzany przez firmę** do workflow przeznaczonego tylko dla laboratorium. Dodaj stany Szkic, Przegląd, Zatwierdzone, Publikowanie, Gotowe i Zablokowane. Dodaj przejścia zgłoszenia, zatwierdzenia, publikacji, zakończenia, blokady i powrotu do przeglądu. Powiąż go wyłącznie z typem pracy w laboratorium.

1. W edytorze workflow **wybierz przejście do stanu Zatwierdzone**.
2. **Dodaj warunek lub ograniczenie**, które pozwoli aktywować przejście wyłącznie wskazanej roli lub grupie właściciela/wydawcy. Użyj udokumentowanych ustawień warunków i opublikuj szkic workflow jako administrator.
3. **Ręcznie sprawdź oba przeglądy właścicieli** przed przejściem. Każdy przegląd wskazuje zamrożoną propozycję i wersje źródeł.
4. **Ogranicz stan Gotowe** do odpowiedzialnej roli realizującej. Usuń alternatywne lub globalne przejścia omijające tę granicę.

**Ograniczone przejście nie oznacza zatwierdzenia przez dwie osoby.** Kontroluje ono, kto wykonuje przejście. W tej pilotażowej konfiguracji sprawdzanie dowodów dwóch ról pozostaje procedurą. Zapisz to ograniczenie wprost.

**Przykładowy rekord przejścia:** w przypadku przejścia **Przegląd do Zatwierdzone** zezwól na aktywację tylko wskazanej grupie właścicieli/wydawców. Przed aktywacją osoba wykonująca przejście otwiera stały załącznik PROP-042 i sprawdza decyzję właściciela produktu oraz właściciela operacyjnego dla tej samej rewizji propozycji. Jeśli brakuje którejkolwiek decyzji albo wskazuje ona starszą rewizję, pozostaw element w stanie Przegląd i zapisz lukę. Ograniczenie workflow kontroluje osobę wykonującą przejście. Sprawdzenie dowodów to odrębny krok człowieka.

## Sprawdź odmowę dostępu

**Jako współtwórca** odczytaj REQ-17, spróbuj je edytować, utwórz szkic Jira i spróbuj przejść do stanu Zatwierdzone. Oczekiwane wyniki to odczyt wymagania, odmowa edycji, udane utworzenie propozycji i odmowa zatwierdzenia. Porównaj wersje źródła przed odmową i po niej.

**Jako użytkownik wykluczony** otwórz osobną stronę syntetyczną z ograniczeniami. Oczekiwany wynik to brak dostępu do treści. Sprawdź podstrony niezależnie. Nie wklejaj chronionej treści do czatu użytkownika wykluczonego jako obejścia.

## Dostosuj mapę repozytorium

**Zachowaj identyfikatory źródeł po zmianie ich lokalizacji.** REQ-17 nadal oznacza zatwierdzoną intencję dotyczącą przechowywania, ale w ścieżce mieszanej jego źródłem jest strona Confluence. Migawka w repozytorium wspiera kontrole i przegląd. Nie zastępuje strony będącej źródłem zasad.

| Rekord | Źródło obowiązujących zasad | Sposób użycia w repozytorium |
|---|---|---|
| **REQ-17** | Powiązana strona wymagań w Confluence | Migawka z dowodem rewizji strony |
| **RUN-04** | Powiązana strona instrukcji w Confluence | Zapisany fragment operacyjny dla zachowania spójności |
| **POL-01** | Chroniona polityka w GitHub | Wspólne instrukcje agentów zawierają odnośnik |
| **Konfiguracja** | Chroniony rekord w GitHub | Proponowana zmiana implementacji |
| **Realizacja** | Element pracy w Jira | Odnośnik korelacyjny, a nie kopia polityki |

**Dodaj pochodzenie danych do migawek.** W prywatnym pakiecie propozycji zapisz identyfikator źródła, odnośnik do strony, jej wersję, czas pobrania i rolę osoby zapisującej. Nie ujawniaj natywnych identyfikatorów stron w publicznych pracach kursowych. Jeśli wydawca znajdzie inną aktualną wersję, uzgodnij ją przed użyciem migawki.

**Nie zmieniaj nazwy źródła, aby pasowała do narzędzia.** Edytowalny opis Jira ułatwia dyskusję, ale nadal jest rekordem realizacji. Zdanie o trzydziestu dniach w Jira nie zastępuje wymogu siedmiu dni w Confluence.

## Zaprojektuj testy dostępu

**Oddziel odczyt, przygotowanie szkicu i publikowanie.** Współtwórca potrzebuje dostępu wystarczającego do zrozumienia syntetycznego wymagania i zgłoszenia propozycji. Nie potrzebuje prawa edycji strony źródłowej ani uprawnienia do zatwierdzania własnej propozycji.

```text
Test record: PERM-REQ-EDIT
Role: contributor
Source: REQ-17
Precondition: source is readable, published revision captured
Attempt: edit the authoritative requirement
Expected: edit denied, published revision unchanged
Observed: fill from the sandbox
Evidence: native result and independent revision read-back
Reviewer: administrator or independent permission reviewer
```

**Użyj oddzielnego rekordu dla odmowy odczytu.** Dostęp współtwórcy do opublikowanego wymagania testuje oddzielenie publikacji od edycji. Brak dostępu do strony użytkownika wykluczonego testuje poufność. Połączenie obu przypadków w jednym wierszu ukrywa, którą granicę sprawdzono.

**Sprawdź także dostęp dozwolony.** Właściciele i wydawcy muszą móc korzystać z przypisanej im ścieżki. Jeśli odmowa dotyczy każdego użytkownika, środowisko jest ograniczone, ale bezużyteczne. Zapisz udaną autoryzowaną edycję na tymczasowej stronie testowej, nie zmieniając zatwierdzonego wymagania podczas diagnozowania uprawnień.

## Przećwicz przegląd Jira

**Potraktuj nazwy stanów jako projekt tej konfiguracji pilotażowej.** Szkic zawiera wniosek. Przegląd zawiera zamrożony pakiet. Zatwierdzone oznacza zakończenie przeglądu właścicieli. Publikowanie oznacza realizację, która jeszcze trwa. Gotowe wymaga odczytu kontrolnego. Zablokowane oznacza brak dowodów lub dostępu albo nierozwiązany konflikt.

| Przejście | Wymagany pakiet | Odpowiedzialna kontrola |
|---|---|---|
| **Szkic do Przeglądu** | Stała propozycja i wersje źródeł | Współtwórca potwierdza kompletność |
| **Przegląd do Zatwierdzone** | Decyzje właściciela produktu i operacyjnego | Upoważniona osoba sprawdza obie role |
| **Zatwierdzone do Publikowania** | Porównanie z aktualnymi źródłami | Wydawca potwierdza niezmienione podstawy |
| **Publikowanie do Gotowe** | Uzupełniony rejestr dla każdego systemu | Właściciel realizacji sprawdza odczyt kontrolny |
| **Każdy obsługiwany krok do Zablokowane** | Błąd i oczekiwane działanie | Wyznaczony właściciel odzyskiwania |

**Przećwicz pracę z niekompletnym pakietem syntetycznym.** Prześlij wyłącznie przegląd produktu i poproś upoważnioną osobę o ocenę przejścia. Oczekiwane rozumowanie: pozostawić pracę w stanie Przegląd i poprosić o przegląd operacyjny. Testuje to proceduralny przegląd osobno od odmowy dostępu dla współtwórcy.

**Celowo sprawdź alternatywne ścieżki.** W widoku workflow środowiska testowego sprawdź każdą drogę do stanów Zatwierdzone i Gotowe. Ograniczenie nazwanego przejścia nie wystarczy, jeśli inna dostępna droga omija tę samą granicę przeglądu. Zapisz sprawdzone ścieżki i użyte konto, zamiast twierdzić, że jeden klik zapewnił pełny zakres testów.

## Diagnozuj nieoczekiwany dostęp

**Zacznij od efektywnej tożsamości.** Sprawdź, czy sesja przeglądarki należy do zamierzonej roli testowej. Następnie użyj narzędzi administracyjnych produktu, aby sprawdzić członkostwo w grupach, uprawnienia przestrzeni, dostęp do stron i przypisanie workflow. Nie zmieniaj kilku ustawień jednocześnie, ponieważ odmowa straci wartość diagnostyczną.

1. **Potwierdź tożsamość:** użyj oddzielnych sesji współtwórcy, wydawcy i użytkownika wykluczonego.
2. **Znajdź nadane uprawnienie:** ustal, które członkostwo lub ustawienie pozwala wykonać daną czynność.
3. **Zmień kontrolę laboratoryjną:** zachowaj prawidłowy dostęp właścicieli.
4. **Powtórz tę samą próbę:** po odmowie zapisz niezmienioną wersję źródła.
5. **Powtórz przypadek pozytywny:** potwierdź, że autoryzowana publikacja nadal działa.

**Końcowa lista dowodów:** zapisz drzewo stron Confluence i powiązane identyfikatory stron, przypisanie schematu laboratoryjnego Jira, przypisanie workflow laboratoryjnego, członkostwo każdej roli testowej w grupach, dozwolony odczyt wymagania, odmowę edycji wymagania z niezmienioną wersją, dozwolone utworzenie szkicu, odmowę przejścia do stanu Zatwierdzone bez zmiany stanu, odmowę odczytu dla użytkownika wykluczonego i osobę odpowiedzialną za czyszczenie. Dla każdego wiersza zapisz rolę wykonawcy, początkową i końcową wersję lub stan, wynik natywny i niezależnego recenzenta. Zapisz zaobserwowaną ścieżkę nawigacji w dzierżawie, ponieważ etykiety i funkcje różnią się zależnie od planu.

**Kontrola ukończenia:** dostarcz powiązane strony źródłowe, workflow laboratoryjny, zamierzoną macierz ról i zaobserwowane rekordy uprawnień. Jeśli plan nie udostępnia wymaganej kontroli, oznacz odpowiedni wiersz jako Zablokowany. Wniosek dotyczący publikacji zakłada, że testy zakończyły się powodzeniem, a nie tylko że istnieją zrzuty ekranu ustawień.

## Rozwiązywanie problemów i wycofanie

**Współtwórca nadal edytuje:** sprawdź dostęp do strony, uprawnienia przestrzeni i członkostwa. **Przejście nadal się udaje:** sprawdź przypisanie workflow i ścieżki obejścia. **Brakuje ustawień:** sprawdź typ zarządzania przez firmę, edycję i uprawnienia administratora.

**Wycofanie:** usuń uprawnienia łączników i zarchiwizuj szkice. Odłącz schematy i workflow laboratoryjne po zachowaniu dowodów. Przywróć zatwierdzone brzmienie strony z przeglądanej historii lub w ramach poprawki. Nie usuwaj dowodów audytu.

## Ćwiczenie i samokontrola

**Jira wskazuje trzydzieści dni, a REQ-17 siedem.** Ustal dane wejściowe implementacji i właściciela, który ma rozwiązać tę sprzeczność.

**Oczekiwane rozumowanie:** Confluence określa zamiar. Jira zawiera błąd propozycji lub realizacji. Wstrzymaj publikację i poproś właściciela produktu o uzgodnienie, zamiast wybierać najnowszy znacznik czasu.

## Główne źródła

- **Ograniczenia i plan:** [uprawnienia Confluence](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Opcje udostępniania:** [dostęp do określonych treści](https://support.atlassian.com/confluence-cloud/docs/add-or-remove-page-restrictions/).
- **Administracja schematem:** [schematy uprawnień Jira](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).
- **Warunki przejść:** [zaawansowane workflow](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).

## Następne kroki

**Po pomyślnym zakończeniu testów dostępu przejdź do [Publikacji między systemami](/articles/ai-collaboration-confluence-jira-publication/)**.
