---
title: "Capstone współpracy AI: GitHub, Confluence i Jira"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Dostarcz syntetyczną zmianę retencji przez przepływy GitHub-first oraz Confluence/Jira, z dowodami awarii i niezależnym przeglądem."
genre: ["Sztuczna inteligencja", "Współpraca zespołowa", "Inżynieria oprogramowania"]
tags: ["kurs współpracy AI", "propozycja retencji", "przegląd GitHub", "przepływ Confluence Jira", "macierz awarii", "niezależna akceptacja"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustracja profesjonalistów przeglądających wspólną pracę projektową w środowisku cyberbezpieczeństwa"
coverCaption: ""
---

[Wróć do kursu współpracy AI](/ai-collaboration-course-start/)

**Dostarcz PROP-042 dwa razy**, przez GitHub-first oraz przez GitHub z Confluence/Jira. Wnosisz zmianę, oddzielni właściciele ją przeglądają, a uprawnieni publikujący ją stosują. Po poprzednich lekcjach użyj izolowanych syntetycznych sandboxów. Capstone sprawdza pełną procedurę, w tym odrzucenie, odzyskanie i niezależne przekazanie, a nie jakość tekstu asystenta.

## Najważniejsze wnioski

- **Jedna wspólna zmiana** porównuje oba modele władzy.
- **Testy negatywne** są równie ważne jak udane dostarczenie.
- **Pakiety dowodowe** wspierają niezależny przegląd.
- **Ukończenie laboratorium** nie zezwala na wdrożenie produkcyjne.

## Zanim zaczniesz

**Wymagania wstępne:** wcześniejsze [moduły kursu](/ai-collaboration-course-start/), zatwierdzony dostęp do sandboxa i oddzielni recenzenci. **Planowany czas:** osiem do dwunastu godzin w wielu sesjach oraz niezależny przegląd. Rzeczywisty czas zależy od konfiguracji konta i prac naprawczych. **Poziom:** zaawansowany.

**Wymagane artefakty:** karta, mapa, polityka, adaptery, baza, manifest, ustalona propozycja, przeglądy właścicieli, rejestr, zapis odzyskiwania i przekazanie. Brak uprawnień zależnych od planu blokuje ukończenie. Nie traktuj ich jako domyślnie zaliczonych.

**Przed testami przygotuj po jednym katalogu dowodowym dla każdego toru.** Recenzent powinien rozpoznać aktora, rewizje źródeł, wykonaną czynność, zaobserwowany wynik i stan końcowy bez polegania na podsumowaniu czatu.

## Ustal dwie bazy

1. **Utwórz izolowane uruchomienia** o nazwach GitHub-first i Mixed. Oddziel rewizje i przeglądy.
2. **Przywróć bazę siedmiodniową** przez zatwierdzoną procedurę każdego toru i zapisz wynikowe rewizje.
3. **Sprawdź kontrole odmowy** za pomocą kont contributor i excluded-user.
4. **Zapisz bieżący kontekst** i potwierdź zgodność adaptera z polityką.
5. **Zdefiniuj zakres:** syntetyczna retencja eksportu przez trzydzieści dni, bez prawdziwych danych, kopii zapasowych i blokad prawnych.

**PROP-042 jest etykietą korelacyjną, a nie ponownie używalną zgodą.** Każde uruchomienie potrzebuje własnej zamrożonej rewizji i dowodów źródłowych. Raporty muszą zawierać identyfikatory uruchomień.

## Dostarcz GitHub-first

**Otwórz Issue i kandydacki PR** zgodnie z lekcjami GitHub. Zmień razem wymaganie, konfigurację, propozycję i runbook. Zapisz chronioną bazę, uruchom zaufane kontrole i uzyskaj przeglądy produktu oraz operacji przy końcowym commicie.

```text
Run: GitHub-first
Change: synthetic retention 7 -> 30 days
Requirement: REQ-17 revision 2
Configuration: retention_days 30
Runbook: Retention days: 30
Proposal: base revision 1, from 7, to 30
Manifest: protected pre-change source hashes
Review: product and operations at final proposal revision
Publication: merged commit and read-back
Limit: no running deletion service exercised
```

**Wstaw rzeczywiste odwołania z sandboxa.** Szkic pokazuje oczekiwane mapowanie, nie gotowe dowody. Maintainer scala dopiero po przeglądzie, a potem niezależnie odczytuje **`main`**. Zamknij Issue po dodaniu linków do końcowych zapisów.

## Dostarcz tor Mixed

**Przeczytaj wersje Confluence i zamroź propozycję Jira.** Uzyskaj oba przeglądy właścicieli. Opublikuj wymaganie ze stanem delivery pending, scal konfigurację, opublikuj runbook i przed stanem Done odczytaj wszystkie systemy.

**Zapisuj każdą publikację** wraz z wersją strony, commitem lub dowodem przejścia. Kopie wymagań w repozytorium pozostają migawkami. Lokalny checker nie potwierdza bieżącej władzy Confluence.

| Porównanie | GitHub-first | Miejsce pracy Mixed |
|---|---|---|
| **Wymaganie** | Przegląd chronionego repozytorium | Publikacja sprawdzona przez właściciela Confluence |
| **Koordynacja** | Issue/PR | Ustalona propozycja Jira |
| **Jednostka publikacji** | Scalenie repozytorium | Oddzielne zapisy stron i scalenie |
| **Aktualność** | Chroniony commit | Wersje stron plus commit |
| **Odzyskiwanie** | Sprawdzony revert/kompensacja | Kompensacja prowadzona rejestrem |

**Wybierz przepływ według potrzeb właścicielskich.** GitHub-first ogranicza koordynację między systemami. Tor Mixed zachowuje miejsce pracy i dodaje kontrole publikacji oraz dostępu.

## Uruchom macierz awarii

| Przypadek | Wstrzyknięcie | Wymagany zaobserwowany dowód |
|---|---|---|
| **Zatwierdzona zmiana** | Prześlij sprawdzoną propozycję trzydziestodniową | Spójny odczyt i przegląd |
| **Nieaktualny kontekst** | Zmień źródło po zapisie | Odrzucenie, uzgodnienie, ponowna zgoda |
| **Nieuprawniony zapis** | Contributor publikuje | Odmowa i niezmieniona rewizja |
| **Konflikt** | Jira mówi sześćdziesiąt, Confluence siedem | Blokada i uzgodnienie właścicieli |
| **Częściowa publikacja** | Przerwij po jednym zapisie | Oczekujący rejestr i odzyskanie |
| **Odmowa dostępu** | Usuń dostęp do odczytu zadania | Brak chronionego tekstu lub publikacji |
| **Odzyskanie** | Zatwierdzone ukończenie/cofnięcie | Nowe sprawdzone rewizje |
| **Przekazanie** | Nowa sesja dostaje tylko mapę/rejestr | Świeży odczyt i poprawne następne działanie |

**Konflikt między systemami należy do Mixed.** W GitHub-first sprawdź opis Issue sprzeczny z zatwierdzonym plikiem. Pozostałe właściwe przypadki uruchom w obu torach. Lokalna awaria walidatora nie zastępuje dowodu uprawnień na żywo.

| Przypadek i plik dowodowy | Uruchomienie GitHub-first | Uruchomienie Mixed |
|---|---|---|
| **Zatwierdzona zmiana** `01-approved-change.md` | Sprawdzony PR i odczyt | Sprawdzone strony, scalenie i rejestr |
| **Nieaktualny kontekst** `02-stale-context.md` | Zmień chronioną bazę po zapisie | Zmień stronę władzy po zapisie |
| **Nieuprawniony zapis** `03-unauthorized-write.md` | Odmowa bezpośredniego pushu contributora | Odmowa edycji strony i przejścia contributora |
| **Konflikt** `04-conflict.md` | Issue nie zgadza się z zatwierdzonym plikiem | Tekst Jira nie zgadza się z Confluence |
| **Częściowa publikacja** `05-partial-publication.md` | Zatrzymaj się przed scaleniem lub odczytem | Zatrzymaj się po jednym zapisie strony |
| **Odmowa dostępu** `06-access-denial.md` | Ukryj chronione źródło repozytorium | Wyklucz użytkownika z ograniczonej strony |
| **Odzyskanie** `07-recovery.md` | Sprawdzony revert lub ukończenie | Kompensacja prowadzona rejestrem |
| **Przekazanie** `08-handoff.md` | Nowa sesja odczytuje chronione pliki | Nowa sesja odczytuje mapowane strony i rejestr |

**Utwórz każdy plik przed jego testem.** Zapisz oczekiwany wynik, zaobserwowany wynik, rolę aktora, początkowe i końcowe rewizje, natywne odwołanie dowodowe oraz decyzję recenzenta. Monit przeglądarkowej trasy nie jest odmową bezpośredniego pushu. Oddziel katalogi obu torów.

**Oddziel wyniki oczekiwane od zaobserwowanych.** Dla każdego przypadku zapisz identyfikator uruchomienia, rolę aktora, początkowe rewizje, próbę działania, oczekiwanie, obserwację, wynikowe rewizje i decyzję recenzenta. Redaguj dane logowania i identyfikatory kont we wspólnych raportach.

## Oceń ukończenie

**Zaliczenie wymaga zaobserwowanych dowodów dla każdego właściwego wiersza** i niezależnej akceptacji. Recenzenci sprawdzają uprawnienia, aktualność źródeł, przegląd ról, częściową publikację, odtworzenie przekazania i logi spójności.

**Natychmiast oznacz Fail** przy nieuprawnionej publikacji, dotarciu odrzuconego tekstu do modelu lub cichym nadpisaniu zmienionej bazy. Pozostaw pracę jako Blocked, dopóki poprawione kontrole nie przejdą ponownego testu. Nie uśredniaj tych awarii do korzystnego wyniku.

**Mierz przypadki ukończone/zablokowane, odrzucone nieaktualne propozycje, odmowy zapisów, odzyskania i czas recenzenta.** Proponowane wyniki pozostają oczekiwane do chwili obserwacji. Dostarczone dziesięć testów jednostkowych obejmuje spójność, nie bezpieczeństwo dzierżawy na żywo.

## Zaplanuj dwa uruchomienia

**Nie używaj tej samej zgody w obu torach.** Żądana wartość jest taka sama, lecz miejsca źródeł, zapisane rewizje, uprawnienia i sekwencja publikacji są różne. Każdemu uruchomieniu nadaj własny katalog dowodowy i pakiet recenzji.

```text
capstone-evidence/
  github-first/
    charter-and-map
    captured-sources
    fixed-proposal
    role-reviews
    consistency-results
    permission-results
    publication-readback
    recovery-and-handoff
  mixed/
    same evidence categories, independently captured
```

**Te nazwy są przykładem organizacji**, a nie dostarczonymi plikami archiwum. Rzeczywiste dowody przechowuj prywatnie w zatwierdzonym sandboxie. Wspólne zgłoszenia kursowe powinny używać etykiet ról i zredagowanych odwołań, a recenzenci zachowują dostęp do natywnych zapisów.

**Wyznacz obserwatora testów przed uruchomieniem awarii.** Contributor wykonuje próbę działania. Obserwator zapisuje stan początkowy, wynik i stan końcowy. Recenzent później ustala, czy dowody wspierają twierdzenie. Ujawnij nakładanie ról zamiast sugerować niezależną akceptację.

## Uruchamiaj awarie osobno

**Między przypadkami wracaj do zweryfikowanego, sprawdzonego stanu.** Jednoczesne wstrzyknięcie dryfu źródła, odebrania dostępu i niezgodności runbooka zaciera informację, która kontrola odrzuciła propozycję. Jedna awaria na uruchomienie daje recenzentowi możliwy do prześledzenia powód.

1. **Zapisz stan początkowy:** rewizje źródeł, konfigurację, stan dostarczenia i rolę aktora.
2. **Zastosuj jedno syntetyczne wstrzyknięcie:** zmień jeden warunek przez uprawnioną ścieżkę testową.
3. **Wykonaj ograniczoną czynność:** walidację, odczyt, publikację lub przekazanie.
4. **Zapisz obserwację:** rzeczywisty wynik i wynikowy stan źródła.
5. **Napraw przez przegląd:** zachowaj dowód awarii przed przywróceniem kontroli.
6. **Powtórz przypadek pozytywny:** potwierdź, że poprawiony przepływ nadal dostarcza dozwoloną pracę.

**Planowana awaria nadal jest obserwacją awarii.** Nie nazywaj nieuprawnionej publikacji udanym testem tylko dlatego, że planowałeś ją zbadać. Test ujawnił defekt, lecz granica publikacji zawiodła i wymaga naprawy.

**Karta wstrzyknięcia i resetu dla każdego przypadku:** przed kolejnym wierszem użyj nowej syntetycznej propozycji albo przywróć sprawdzoną bazę. Obserwator zapisuje warunek wstępny i potwierdza reset. Nigdy nie usuwaj nieudanej próby z rejestru.

| Przypadek | Wstrzyknięcie i sprawdzenie GitHub-first | Wstrzyknięcie i sprawdzenie Mixed | Reset przed następnym przypadkiem |
|---|---|---|---|
| Zatwierdzona zmiana | Wyślij ustalony PR, uzyskaj oba przeglądy, scal i ponownie otwórz `main` | Opublikuj REQ-17, scal sprawdzony diff, opublikuj RUN-04, a potem ponownie otwórz wszystkie zapisy | Zapisz końcowe rewizje jako następną bazę |
| Nieaktualny kontekst | Zapisz manifest, a następnie zmień chronioną bazę testową przez osobny sprawdzony PR przed walidacją starej propozycji | Zapisz wersje stron, a następnie zleć uprawnionemu edytorowi zmianę strony testowej przed odczytem przed zapisem | Zatrzymaj się, porównaj wersje, pobierz świeże źródła i sprawdź nowy ustalony pakiet |
| Nieuprawniony zapis | Contributor próbuje nieszkodliwego bezpośredniego pushu do chronionego `main` i zapisuje odmowę serwera | Contributor próbuje edycji REQ-17 i przejścia Approved | Ponownie otwórz chroniony commit, wersję strony i stan Jira, które powinny pozostać bez zmian |
| Konflikt | Wstaw sześćdziesiąt dni do roboczego Issue, gdy zatwierdzony plik mówi siedem | Wstaw sześćdziesiąt dni do roboczego Jira, gdy REQ-17 mówi siedem | Właściciel produktu uzgadnia szkic i zapisuje decyzję przed przeglądem |
| Częściowa publikacja | Zatrzymaj się po zgodzie, ale przed scaleniem lub końcowym odczytem, pozostawiając Issue otwarte | Zatrzymaj się po odczycie REQ-17, gdy konfiguracja i RUN-04 nadal mówią siedem | Pozostaw dostarczenie oczekujące, a następnie uzyskaj sprawdzoną decyzję o ukończeniu lub kompensacji |
| Odmowa dostępu | Użyj tożsamości testowej wykluczonej z prywatnego źródła i spróbuj odczytu | Użyj wykluczonej tożsamości na osobnej ograniczonej stronie syntetycznej | Przywróć tylko zatwierdzony dostęp testowy i sprawdź, że zwykły czytelnik nadal działa |
| Odzyskanie | Przerwij zatwierdzoną zmianę testową, a następnie zaproponuj sprawdzone ukończenie lub revert | Użyj rejestru częściowej publikacji do zaproponowania sprawdzonego ukończenia lub kompensacji | Odczytaj każdą wynikową źródłową wartość i uzgodnij rejestr |
| Przekazanie | Wyślij MAP-01 i rejestr świeżemu recenzentowi bez starego czatu | Wyślij mapowane identyfikatory stron i rejestr świeżemu recenzentowi bez starego czatu | Recenzent otwiera bieżące źródła i zapisuje następny uprawniony krok |

Dla każdego przypadku odmowy zapisz odpowiedź platformy i drugi odczyt chronionego rekordu. Dla przypadku wykluczonego użytkownika sprawdź także zwrócony kontekst zadania, aby zapisany fragment nie udawał bezpiecznej odmowy. Jeśli plan nie udostępnia kontroli lub brakuje zatwierdzonej tożsamości testowej, zapisz Blocked zamiast symulować zaliczenie.

## Zinterpretuj wynik Mixed

**Przykładowy pakiet dowodowy:** lokalna spójność przechodzi, produkt i operacje sprawdzają ustalony pakiet, publikacja wymagania kończy się sukcesem, a dostęp do edycji runbooka zostaje odrzucony. Konfiguracja nie została jeszcze scalona. Jira pozostaje Blocked.

| Twierdzenie | Werdykt | Powód |
|---|---|---|
| **Kandydackie zapisy są zgodne** | Potwierdzone lokalnym sprawdzeniem | Dostarczone zapisy przeszły porównania |
| **Właściciele zaakceptowali intencję i operacje** | Wymaga natywnych, ustalonych przeglądów | Same etykiety ról nie wystarczają |
| **Dostarczenie trzydziestodniowe ukończone** | Niepotwierdzone | Wymagane kroki publikacji pozostają oczekujące |
| **Granica uprawnień działa dla każdej roli** | Niepotwierdzone | Jedna odmowa ma ograniczony zakres |
| **Właściciel odzyskania powinien działać** | Potwierdzone jako następny krok | Częściowe dostarczenie wymaga sprawdzonej decyzji |

**Oczekiwane rozumowanie:** pozostaw uruchomienie nieukończone, sprawdź bieżące źródła i poproś o decyzję właściwego właściciela. Nie kończ przez osłabienie uprawnień ani przez opisanie sprawdzenia migawki jako dowodu publikacji na żywo.

**Wypełniony pakiet dydaktyczny toru Mixed, syntetyczny i niebędący dowodem tenant:**

```text
Run: MIXED-042-example
Captured base: REQ-17 v4 = 7 days, RUN-04 v2 = 7 days,
  GitHub main base-001 config.json = {"retention_days": 7}, Jira PROP-042 r1 = In Review
Fixed proposal: REQ-17 v5 wording says synthetic exports 30 days,
  excluding production data, backups, and legal holds.
  GitHub config.json changes retention_days from 7 to 30.
  RUN-04 v3 wording says 30 days, no deletion service runs in this lab,
  and incomplete publication stays pending.
Review: product owner approved the exact requirement wording at PROP-042 r1.
  Operations owner approved the exact config diff and runbook wording at r1.
Publication: publisher reopened REQ-17 v5 and read 30 days.
  Maintainer reopened main at merge-002 and read retention_days 30.
  Publisher reopened RUN-04 v3 and read 30 days.
Denied action: contributor tried an edit to restricted REQ-17 from v5.
  Platform denied the edit, the publisher reread v5 unchanged, and the
  observer saved the native denial. No edit was applied and v5 stayed unchanged.
Recovery: after a separate simulated failed RUN-04 attempt, Jira stayed
  Blocked. Operations approved a retry against the current version.
  Publisher reread v3 after the authorized retry before Jira moved to Done.
Handoff: a new reviewer received MAP-01 and the ledger, reopened the three
  sources and Jira, and named the current 30-day state and remaining runtime gap.
Limit: source publication is shown. Actual deletion timing is Not run.
```

Zastąp każdą ilustracyjną wersję, aktora, odmowę i odczyt natywnymi zapisami przed oznaczeniem wiersza na żywo jako Supported. Jeśli plan lub rola nie pozwala na test, oznacz wiersz jako Blocked i pozostaw kurs obu torów nieukończony.

## Sprawdź z niezależnym czytelnikiem

**Poproś recenzenta o odtworzenie zdarzeń**, a nie tylko o przeczytanie wniosku. Bez twojej narracji powinien znaleźć zatwierdzoną bazę, ustaloną propozycję, decyzje właścicieli, wynikowe rewizje, nieudane próby, naprawę i pozostałe luki.

```text
Reviewer questions:
Which source governs retention intent in this track?
Which exact package did each owner review?
Did any source change after review?
What was published, and what remains pending?
Which denied action was observed under which role?
Did protected text reach an excluded user's context?
Which repair was reviewed and read back?
Does the fresh handoff reconstruct current state independently?
```

**Oceniaj każde wymaganie osobno.** Użyj Supported, Failed, Blocked lub Not run wraz z odwołaniem dowodowym. Spójność, zgoda, uprawnienia, odzyskanie i przekazanie są osobnymi wymaganiami. Zbiór zielonych testów lokalnych nie równoważy nieudanej granicy publikacji na żywo.

```text
Run ID and track:
Reviewer role and review date:
Case 01 approved change: status ___ evidence ___ gap ___
Case 02 stale context: status ___ evidence ___ gap ___
Case 03 unauthorized write: status ___ evidence ___ gap ___
Case 04 conflict: status ___ evidence ___ gap ___
Case 05 partial publication: status ___ evidence ___ gap ___
Case 06 access denial: status ___ evidence ___ gap ___
Case 07 recovery: status ___ evidence ___ gap ___
Case 08 handoff: status ___ evidence ___ gap ___
Overall decision: Supported / Failed / Blocked / Not run
Next accountable role and action:
```

**Supported oznacza, że recenzent znalazł zaobserwowane dowody dla każdego właściwego przypadku.** Zapisz Failed przy zaobserwowanej awarii kontroli, Blocked przy brakującym dostępie lub kontroli, a Not run przy niepodjętym przypadku. Natywne odwołanie każdego przypadku zachowaj w nazwanym pliku dowodowym.

**Bramka zaliczenia kursu:** ukończ oba tory, GitHub-first i Mixed. W każdym torze wszystkie osiem właściwych przypadków musi mieć dowody Supported. Nieudana granica lub brak natywnego odczytu blokuje tor. Brak płatnego planu lub tożsamości testowej daje Blocked, nie zgadywane zaliczenie. Jeden ukończony tor daje udokumentowany wynik częściowy, nie ukończenie kursu.

**Zredagowany pakiet modelowy, tylko ilustracja:**

```text
Track: github-first | Run: G-01 | Reviewer: separate pilot role
Base: protected commit base-001 | Fixed proposal: PROP-042 r1
Approvals: product review ref P-01, operations review ref O-01
Consistency: local check pass, saved output ref C-01
Permission: contributor direct push denied, native event ref D-01
Publication: merged commit merge-002, fresh clone confirms thirty
Exception: backups and legal holds remain excluded
Recovery: interruption case R-01 read back and resolved through review
Handoff: second reader found current base, exception, and next action
Runtime limit: no production deletion or deployment claim
Decision: Supported for synthetic GitHub-first track only
```

Zastąp każde ilustracyjne odwołanie zaobserwowanym artefaktem sandboxa. Powtórz pełny pakiet dla toru Mixed z jego własnymi wersjami źródeł i przeglądami. Recenzent powinien odrzucić skopiowaną zgodę GitHub w pakiecie Mixed.

## Napisz ograniczoną decyzję

**Dobra decyzja końcowa wskazuje następny pilot**, a nie nieograniczone wdrożenie. Na przykład wybierz inne ustawienie syntetycznego eksportu z tymi samymi rolami i bezpośrednią ścieżką odczytu, pozostawiając prawdziwe dane i automatyczną publikację poza zakresem.

| Element decyzji | Wymagany szczegół |
|---|---|
| **Zakres** | Jedna następna zmiana i jej wyraźne wykluczenia |
| **Dowody** | Przypadki Supported i nierozwiązane awarie |
| **Kontrole** | Wymagania wymuszane przez platformę i proceduralne osobno |
| **Właściciele** | Odpowiedzialna rola za każdą pozostałą lukę |
| **Luka wykonawcza** | Niesprawdzone zachowanie usuwania/wdrożenia |
| **Warunki zatrzymania** | Brak dostępu, zmieniona władza, nieuprawniona publikacja |

**Kontrola ukończenia:** oba pakiety przechodzą niezależne odtworzenie, właściwe przypadki awarii mają zaobserwowane dowody, a nierozwiązane kontrole pozostają widoczne. Jeśli ukończony jest tylko tor GitHub, zgłoś częściowe ukończenie kursu. Nie zakładaj, że Mixed zachowa się tak samo.

## Rozwiązywanie problemów i wycofanie

**Tylko dowody ścieżki szczęśliwej:** ponów testy odmowy i przerwania. **Nakładające się role:** ujawnij je i powtórz z oddzielnymi użytkownikami. **Brak kontroli planu:** zatrzymaj się i uzyskaj zatwierdzony sandbox.

**Wycofanie:** przywróć bazę przez sprawdzone PR-y i edycje Confluence, odwołaj tymczasowe integracje, zarchiwizuj dowody Jira i wykonaj zatwierdzone przez właściciela syntetyczne czyszczenie po retencji dowodów. Zachowaj historię odzyskiwania.

## Utwórz decyzję wdrożeniową

```text
Decision: another synthetic pilot, blocked, or rejected
Evidence: both run packages and failure matrix
Unenforced requirements: procedural controls listed explicitly
Provider review: input scope and retention handling
Owner coverage: product, operations, policy, repository, delivery
Production gaps: runtime tests, secrets, deployment, access review
Next action: one bounded follow-up with accountable role
Review date: assigned by pilot owners
```

**Oczekiwane rozumowanie:** sukces syntetyczny wspiera kolejny ograniczony pilot. Produkcja wymaga osobnej zgody na prawdziwe dane, wdrożenie, obsługę dostawcy i zachowanie wykonawcze. Udana odpowiedź asystenta nie jest zgodą na wdrożenie.

## Główne odwołania

- **Kontrole repozytorium:** [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Dostęp do miejsca pracy:** [Confluence permissions](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Kontrole dostarczania:** [Jira permission schemes](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).

## Następne kroki

**Wróć do [centrum kursu](/ai-collaboration-course-start/)**, aby przejrzeć brakujące kontrole. Przed wyborem kolejnego pilota porównaj implementację z [artykułem o frameworku](/articles/one-source-many-tools-ai-collaboration-framework/).
