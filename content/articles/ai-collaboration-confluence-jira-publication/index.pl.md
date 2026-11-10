---
title: "Proces publikacji AI w GitHub, Confluence i Jira"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Opublikuj stałą propozycję retencji w Confluence, GitHub i Jira, sprawdzając wersje i przygotowując się na częściową publikację."
genre: ["Sztuczna inteligencja", "Współpraca zespołowa", "Inżynieria oprogramowania"]
tags: ["kurs współpracy AI", "Confluence Cloud", "Jira Cloud", "publikacja między systemami", "kontrola wersji", "rejestr publikacji", "częściowa publikacja"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustracja przedstawiająca specjalistów przeglądających wspólny projekt w przestrzeni roboczej cyberbezpieczeństwa"
coverCaption: ""
---

[Wróć do kursu współpracy AI](/ai-collaboration-course-start/)

**Współtwórca zamraża PROP-042, zanim właściciele go zatwierdzą.** Osoba publikująca w Confluence aktualizuje wymagania, opiekun repozytorium GitHub scala implementację, a zespół operacyjny publikuje runbook. Jira rejestruje każdy krok. Wykonaj te działania po sprawdzeniu uprawnień, ponieważ te trzy systemy nie tworzą jednej transakcji atomowej. Rejestr publikacji ujawni niepełne wdrożenie.

## Najważniejsze wnioski

- **Zatwierdzona intencja** różni się od dostarczonego działania.
- **Stałe rewizje propozycji** wiążą decyzje z konkretną wersją.
- **Rejestry publikacji** ujawniają częściowe wykonanie.
- **Ponowne odczyty źródeł** chronią przed zmianą podstawy.

## Zanim zaczniesz

**Wymagania:** [konfiguracja miejsca pracy](/articles/ai-collaboration-confluence-jira-setup/), uprawnienia do publikacji, właściciele oraz opiekun repozytorium. **Szacowany czas:** dwie godziny. **Poziom trudności:** zaawansowana koordynacja.

**Podstawowy interfejs:** odczyt w przeglądarce, opcjonalne przygotowanie szkicu w zatwierdzonym czacie i publikacja przez człowieka. Nie zakładamy subskrypcji konektora. Przed dodaniem integracji sprawdź dostępność w dzierżawie, zakresy uprawnień, obsługę danych przez dostawcę i mapowanie tożsamości. Nigdy nie udostępniaj współtwórcy danych logowania właściciela.

**Wynik dla czytelnika:** przygotujesz stałą propozycję, rejestr publikacji dla każdego systemu, dowody z odczytu zwrotnego i decyzję o odzyskiwaniu po pierwszym nieukończonym kroku. Ćwiczenie sprawdza procedurę i obsługę dowodów, a nie zachowanie retencji w środowisku produkcyjnym.

## Zapisz aktualne źródła

1. **Przeczytaj MAP-01**, a następnie otwórz REQ-17 i RUN-04 na podstawie przypisanych identyfikatorów stron.
2. **Otwórz menu strony i historię strony (Page History)**, a następnie zapisz numery wersji, stan, treść, właściciela i wyjątki.
3. **Odczytaj element w Jira** i dołącz zamrożony eksport propozycji lub commit GitHub. Sam klucz nie utrwala dowodów przeglądu.
4. **Odczytaj zatwierdzoną POL-01** i chronioną bazową konfigurację.
5. **Przekaż czatowi wyłącznie potrzebne syntetyczne fragmenty**, oznacz je jako migawki i wyłącz działania umożliwiające zapis.

```text
Task: PROP-042, propose only
Authority: Confluence REQ-17 for intent, GitHub for behavior
Read: mapped current pages, versions, scope, exceptions
Proposal: synthetic export retention from 7 to 30 days
Output: requirement wording, config diff, runbook, ledger
Evidence: source ID and captured revision for each factual claim
Unknowns: missing access and absent runtime observations
Stop: conflict, changed base, or denied access
```

**Pakiety offline pozostają migawkami.** Przed zapisem osoba publikująca ponownie odczytuje aktualne dane. Odmowa dostępu blokuje publikację. Stary eksport nie zastępuje bieżącego upoważnienia.

## Zamroź propozycję

```json
{
  "proposal_id": "PROP-042",
  "proposal_revision": 1,
  "requirement_base_version": 1,
  "runbook_base_version": 1,
  "policy_version": 1,
  "from_days": 7,
  "to_days": 30,
  "status": "awaiting-owner-review",
  "publication_order": ["requirement", "implementation", "runbook", "delivery"]
}
```

**Zastąp przykładowe wersje stron rzeczywistymi zapisanymi wersjami.** Dołącz stały plik JSON i proponowane brzmienie do Jira. Każdy właściciel zapisuje rolę, decyzję, rewizję propozycji, wersje źródeł i czas przeglądu. Każda istotna zmiana powoduje powrót pakietu do Review.

**Zespół produktowy ocenia intencję i zakres. Zespół operacyjny ocenia czyszczenie i odzyskiwanie.** Opiekun repozytorium sprawdza diff. Reakcje na zmienne wiadomości czatu nie są zatwierdzeniami powiązanymi z konkretną rewizją.

## Opublikuj i odczytaj ponownie

1. **Przenieś Jira do stanu Publishing**, gdy osoba publikująca sprawdzi oba przeglądy właścicieli i potwierdzi, że podstawy źródłowe się nie zmieniły.
2. **Opublikuj REQ-17** z okresem trzydziestu dni i polem dostawy oczekującej. Zapisz wynikową wersję, zakres i wyjątki.
3. **Otwórz PR implementacji w GitHub**, odwołując się do zatwierdzonej wersji strony. Zmień konfigurację na trzydzieści dni i dołącz niewiążącą migawkę wymagania.
4. **Scal po przeglądzie repozytorium** i odczytaj ponownie **`main`**. Zapisz działanie wynikające z commita oddzielnie od działania w środowisku wykonawczym.
5. **Opublikuj RUN-04**, odczytaj go ponownie według identyfikatora i zapisz wynikową wersję. Osoba publikująca aktualizuje w wymaganiu odniesienia do dostawy.
6. **Zakończ Jira** dopiero wtedy, gdy wszystkie wpisy są zgodne i dołączono dowody ostatniego odczytu zwrotnego.

**Używaj lokalnego walidatora wyłącznie do sprawdzania spójności migawek.** Skopiuj wymaganie Confluence sprzed zmiany do bazowego schematu JSON laboratorium, zapisz migawkę i zmień kandydata na trzydzieści dni. Zwiększ lokalną rewizję migawki, a rzeczywiste wersje Confluence zachowaj oddzielnie w Jira. Przepływ pracy, w którym GitHub jest źródłem głównym, nie waliduje aktywnej zawartości Confluence. Zielony status nie potwierdza autorytatywności zewnętrznego źródła.

**W tym ćwiczeniu nie wdrażaj usuwania danych.** Rzeczywista usługa wymaga dowodu wdrożenia, kontrolowanych danych testowych, mechanizmu wstrzymania i testów granic działania środowiska. Scalony commit potwierdza stan repozytorium, a nie zachowanie retencji w produkcji.

## Śledź częściową publikację

| Krok | Stan początkowy | Dowód wykonania |
|---|---|---|
| **REQ-17** | Pending | Wynikowa wersja strony |
| **Konfiguracja** | Pending | Scalony commit i przegląd |
| **RUN-04** | Pending | Wynikowa wersja strony |
| **Zamknięcie Jira** | Pending | Ostateczny odczyt zwrotny i zmiana stanu |

**Zapisz każdy wynik przed podjęciem następnej próby.** PROP-042 łączy zdarzenia w poszczególnych systemach. Jeden ukończony wiersz nie oznacza ukończenia całej zmiany.

**Przykład niepowodzenia:** Confluence publikuje trzydzieści dni, ale GitHub odmawia scalenia. Ustaw Jira na Blocked, a wymaganie oznacz jako oczekujące na dostawę. Zespół produktowy wybiera dokończenie wdrożenia lub sprawdzone przywrócenie siedmiu dni. Nie zmieniaj awaryjnej kopii README w źródło prawdy dla wymagania.

## Obsługuj równoczesne edycje

**Podstawowy przepływ w przeglądarce:** wyznacz jedną osobę publikującą na czas pilotażu. Otwórz historię strony bezpośrednio przed edycją i po publikacji. Jeśli inna osoba zmieni źródło, zatrzymaj pracę, porównaj i uzgodnij zmiany, a następnie ponów zatwierdzenie. Sekwencyjna publikacja to procedura, a nie gwarancja jednej transakcji atomowej.

**Rozszerzenie API:** dokumentacja Confluence v2 opisuje **`GET /wiki/api/v2/pages/{id}?body-format=storage`** i **`PUT /wiki/api/v2/pages/{id}`** z obiektem wersji. Sprawdzona integracja wydawnicza porównuje bieżącą wersję z zatwierdzoną podstawą, przesyła następną wersję i odczytuje ją ponownie. Nie odświeżaj automatycznie nieudanej wersji, aby ponowić próbę ze starą treścią.

**Sam sukces API nie wystarcza.** Sprawdź wynikową treść, identyfikator źródła, zakres i wersję. Ten kurs nie dostarcza klienta API z uprawnieniami do zapisu. Podstawowym wykonalnym procesem dla osób nieprogramujących jest publikacja w przeglądarce przez człowieka.

## Sprawdź przypadki negatywne

| Wstrzyknięcie | Oczekiwane rozumowanie |
|---|---|
| **Zmiana źródła po zatwierdzeniu** | Zatrzymaj pracę i ponów zatwierdzenie dla nowej wersji |
| **Odebranie osobie publikującej dostępu do edycji** | Odmów aktualizacji i pozostaw wpis oczekujący |
| **Ustawienie w Jira okresu sześćdziesięciu dni** | Zatrzymaj się w razie konfliktu i zachowaj Confluence jako źródło prawdy |
| **Niepowodzenie publikacji runbooka** | Pozostaw dostawę nieukończoną i przypisz odzyskiwanie |

**Zapisz rzeczywiste wyniki piaskownicy** wraz z rolą aktora i rewizjami przed i po zmianie. Nie dołączaj treści chronionych stron do dowodów dla użytkownika, któremu odmówiono dostępu. Oczekiwane wyniki nie są wynikami zmierzonymi.

## Przygotuj pakiet do przeglądu

**Zamroź treść, a nie tylko etykietę propozycji.** PROP-042 pojawia się w każdym systemie, ale sama etykieta nie określa treści, którą sprawdził właściciel. Umieść w jednym stałym pakiecie dokładne brzmienie wymagania, diff implementacji, treść runbooka, wersje źródeł i kolejność publikacji.

```text
Package: PROP-042 revision 1, illustrative
Intent: synthetic export retention changes from 7 to 30 days
Exclusions: production data, backups, legal holds
Requirement amendment: fixed proposed REQ-17 wording
Implementation: fixed candidate diff and protected base reference
Runbook amendment: fixed RUN-04 wording and recovery limits
Review: product and operations decisions for this package
Delivery: requirement -> implementation -> runbook -> closure
Stop: changed source, missing review, denied write, failed read-back
```

**Pakiet powinien być czytelny dla obu właścicieli.** Zespół produktowy potrzebuje intencji i wyłączeń. Zespół operacyjny potrzebuje zmiany operacyjnej i granic odzyskiwania. Oba zespoły muszą rozumieć okres, w którym zatwierdzona intencja różni się od dostarczonej konfiguracji. Sam diff kodu nie wystarczy właścicielowi, który nie zna plików repozytorium.

**Przykładowa zawartość wypełnionego pakietu:**

```text
REQ-17 proposed v5: "Synthetic export files are retained for 30 days from creation. This pilot excludes production data, backups, and legal holds. Delivery remains pending until the GitHub configuration and RUN-04 read-backs match this approved wording."

GitHub config.json, proposed change against base-001:
-  "retention_days": 7
+  "retention_days": 30

RUN-04 proposed v3: "Retention days: 30. Synthetic exports only. No deletion job runs in this lab. If publication fails, keep delivery pending, read back each source, and obtain owner approval before restoring the seven-day configuration or completing the thirty-day publication."
```

Powyższe ciągi znaków to przykładowa treść propozycji, a nie rekordy z aktywnej dzierżawy. Przed przeglądem dołącz rzeczywisty commit bazowy i wersje stron. Stały pakiet ma zawierać pełną proponowaną treść, a nie streszczenie wymagające od właściciela uzupełnienia szczegółów.

**Oddziel migawkę offline od publikacji na żywo.** Kontrola spójności potwierdza zgodność zarejestrowanych danych. Bezpośrednio przed pierwszym zapisem osoba publikująca ponownie sprawdza przypisane strony, a opiekun repozytorium ponownie sprawdza chronioną podstawę. Jeśli którekolwiek źródło się zmieniło, stary pakiet wraca do Review.

## Przejdź przez rejestr

**Przykładowy przebieg stanu:** tabela zawiera wersje szkoleniowe, a nie zaobserwowane wartości. Po każdym zapisie w piaskownicy wpisz rzeczywiste wynikowe wersje i commity.

| Krok | Stan po poprawnym odczycie zwrotnym | Pozostałe zadania |
|---|---|---|
| **Zakończony przegląd właścicieli** | Zatwierdzony pakiet, wszystkie opublikowane wartości wynoszą siedem | Wszystkie kroki publikacji |
| **Opublikowano REQ-17** | Intencja wynosi trzydzieści, dostawa oczekuje | Konfiguracja i runbook |
| **Odczytano scalony commit GitHub** | Intencja i konfiguracja wynoszą trzydzieści, runbook siedem | Runbook i uzgodnienie końcowe |
| **Opublikowano RUN-04** | Wszystkie właściwe wpisy wynoszą trzydzieści | Niezależny odczyt końcowy |
| **Zamknięto dostawę** | Kompletny rejestr z dowodami | Zapisane luki środowiska wykonawczego nadal istnieją |

**Oczekująca dostawa to ważny stan.** Zapobiega opisywaniu starej implementacji jako zgodnej z nową intencją, gdy publikacja jest niepełna. W tym okresie czytelnicy potrzebują obu wartości, a nie jednego podsumowania stwierdzającego, że retencja wynosi trzydzieści dni.

**Zapisuj nieudane próby jako oddzielne zdarzenia.** Jeśli zapis runbooka się nie powiedzie, zachowaj wyniki publikacji wymagania i konfiguracji. Zapisz próbę dotyczącą runbooka, błąd, niezmienioną wersję, przypisaną rolę i następne działanie. Nie cofaj ukończonych wierszy do Pending i nie usuwaj zaobserwowanej sekwencji.

**Przykład odrzucenia z powodu nieaktualnej wersji:** osoba publikująca odczytuje REQ-17 v4, inny upoważniony edytor publikuje v5, a następnie pierwsza osoba próbuje zastosować PROP-042 r1 do v4. Platforma zgłasza konflikt wersji albo odczyt przed zapisem wykrywa v5. Zapisz aktora `publisher`, początkową wersję `v4`, próbę `PROP-042 r1`, wykryty konflikt lub zmianę wersji bieżącej, końcową `v5` bez zmian w tej próbie i przypisanego właściciela `product owner`. Pozostaw Jira w stanie Review. Odczytaj ponownie v5, uzgodnij brzmienie i poproś o przegląd nowego, stałego pakietu przed kolejnym zapisem. Podczas testu na żywo użyj rzeczywistej odpowiedzi platformy i historii strony. Ten wpis jest przykładem szkoleniowym.

**Zakończony przykład szkoleniowy, wyłącznie wartości syntetyczne:**

| System | Początkowe źródło | Stały przegląd | Zapis i odczyt zwrotny | Stan końcowy |
|---|---|---|---|---|
| Confluence REQ-17 | v4, siedem dni | PROP-042 r1, Product zatwierdził zmianę v4 na v5 | Osoba publikująca zapisała v5, reviewer otworzył ją ponownie | Trzydzieści dni, kopie zapasowe i blokady prawne wyłączone |
| Konfiguracja GitHub | Commit `base-001` na `main`, siedem dni | PROP-042 r1, Operations zatwierdził diff kandydata | PR scalono jako `merge-002`, niezależny klon odczytał wartość trzydzieści | Trzydzieści dni w chronionym źródle |
| Confluence RUN-04 | v2, siedem dni | PROP-042 r1, Operations zatwierdził zmianę v2 na v3 | Osoba publikująca zapisała v3, reviewer otworzył ją ponownie | Operacyjny krok trzydziestu dni z wycofaniem |
| Jira PROP-042 | In Review | Obie decyzje właścicieli powiązane z r1 | Właściciel dostawy dołączył dowody i zmienił stan na Done | Zamknięcie po trzech odczytach zwrotnych |

Powyższe etykiety są przykładowe, a nie stanowią dowodów z dzierżawy. Rejestr powinien zawierać odwołania do natywnych wersji stron i identyfikatorów commitów. Przed ustawieniem Jira na Done dołącz zamrożoną propozycję, przeglądy obu ról, zapis podstaw źródłowych, każdy odczyt zwrotny publikacji, wynik testu negatywnego i nierozwiązane ograniczenia środowiska wykonawczego. Jeśli brakuje jednego elementu, pozostaw dostawę otwartą lub zablokowaną.

**Bramka pakietu:** oznacz każdą z pięciu kontroli jako Supported lub Blocked: rewizje źródeł są aktualne, obaj właściciele zatwierdzili tę samą stałą rewizję, wszystkie wymagane publikacje zgadzają się z odczytem zwrotnym, ograniczenia środowiska wykonawczego są jawne, a stan odzyskiwania jest uzgodniony. Done wymaga pięciu kontroli w stanie Supported i braku nieupoważnionych zapisów.

## Obsłuż niepewny zapis

**Po przekroczeniu limitu czasu wynik pozostaje nieznany.** Nie oznacza to ani sukcesu, ani porażki. W podstawowym procesie przeglądarkowym ponownie otwórz przypisane źródło i sprawdź aktualną treść oraz historię, zanim zdecydujesz o ponowieniu próby.

1. **Wstrzymaj następny krok:** pozostaw dostawę nieukończoną.
2. **Odczytaj miejsce docelowe:** porównaj aktualne brzmienie, wersję i zakres ze stałym pakietem.
3. **Zapisz obserwację:** ukończono, bez zmian, konflikt lub brak dostępu.
4. **Wybierz następne działanie:** kontynuuj od zweryfikowanego zakończenia, ponów upoważniony krok bez zmian albo eskaluj konflikt.
5. **Zachowaj niepewność:** zapisz nieudaną lub nieznaną próbę wraz z późniejszym odczytem zwrotnym.

**Nie odtwarzaj całej sekwencji bez sprawdzenia.** Powtórzenie ukończonego kroku tworzy dodatkowe wersje i może nadpisać niezwiązane zmiany. Wznów pracę od zweryfikowanego stanu. Gdy nie masz dostępu do źródła, wybierz Hold zamiast zgadywać na podstawie starego rejestru.

## Porównaj decyzje dotyczące odzyskiwania

| Sytuacja | Decyzja do przeglądu | Powód |
|---|---|---|
| **Zmiana wymagania, odmowa scalenia** | Dokończenie lub kompensacja wymagania | Intencja różni się od działania |
| **Zmiana konfiguracji, odmowa publikacji runbooka** | Dokończenie runbooka lub cofnięcie konfiguracji | Instrukcje operacyjne są nieaktualne |
| **Inny właściciel zmienia zakres** | Powrót do Review | Stałe zatwierdzenie dotyczy innej treści |
| **Nieznany wynik zapisu** | Najpierw odczyt miejsca docelowego | Ponowna próba zależy od zaobserwowanego stanu |
| **Osoba publikująca traci dostęp** | Wstrzymanie i prośba o administrację z uprawnieniami | Stare upoważnienie nie zezwala na nowe zapisy |

**Wybieraj na podstawie aktualnego stanu i decyzji właściciela.** Dokończenie wymaga aktualnych zatwierdzeń i wykonalnych kontroli. Kompensacja wymaga sprawdzenia przywrócenia z uwzględnieniem późniejszych zmian. Zmiana odzyskiwania jest kolejną publikacją, a nie uprzywilejowanym wyjątkiem od procedury.

## Sprawdź zakończenie publikacji

**Przygotuj pakiet, który może uzgodnić niezależny reviewer.** Powinien znaleźć dokładną sprawdzoną propozycję, jej podstawy źródłowe, przeglądy obu ról, każdy wynik zapisu, wartości końcowe i pozostałe ograniczenia środowiska wykonawczego. Poproś go o wskazanie pierwszego nieukończonego kroku po przerwaniu.

**Oczekiwane rozumowanie:** następne działanie wynika z aktualnych źródeł i rejestru, a nie z pewności poprzedniego asystenta. Przenieś końcowe odwołania do mapowanych źródeł do testów pobierania, w których wyszukiwanie musi zachować to samo rozróżnienie źródeł prawdy.

## Rozwiązywanie problemów i odzyskiwanie

**Zmieniona wersja:** porównaj historię i ponów przegląd. **Kontrola migawki przechodzi, ale wiki się różni:** ponownie pobierz aktualne źródła Confluence. **Za wcześnie ustawiono Done:** otwórz ponownie dozwolonym procesem i zapisz brakujące kroki.

**Odzyskiwanie:** porównaj historię stron i wykonaj przywrócenie lub zmianę kompensacyjną zatwierdzoną przez właściciela. Zapisz wynikową wersję i nie zakładaj, że przywrócenie resetuje numerację. Jeśli zespół produktowy wybierze wycofanie, cofnij konfigurację przez chroniony PR. Gwarancja cofania nie obejmuje usuniętych plików.

## Ćwiczenie i samoocena

**Przerwij po publikacji REQ-17** i przekaż innemu publikującemu tylko mapę oraz rejestr.

**Oczekiwane rozumowanie:** ta osoba pobiera aktualne źródła, potwierdza stałe zatwierdzenie i wznawia tylko upoważniony oczekujący krok. Brak dowodów przenosi pracę z powrotem do Review.

## Główne źródła

- **Historia i przywracanie:** [dokumentacja techniczna Confluence](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Wersjonowane operacje API:** [strony Confluence REST API v2](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/).
- **Kontrole przepływu pracy:** [zaawansowane przepływy pracy Jira](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).
- **Bezpieczeństwo integracji:** [najlepsze praktyki bezpieczeństwa MCP](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices).

## Następne kroki

**Po sprawdzonej rundzie publikacji przejdź do [Pobierania według mapy](/articles/ai-collaboration-map-first-retrieval/).**
