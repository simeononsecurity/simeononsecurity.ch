---
title: "Odzyskiwanie po rozjechaniu kontekstu agenta AI i przekazywanie pracy"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Wykrywaj nieaktualne źródła i adaptery polityk, wznawiaj przerwaną publikację oraz weryfikuj niezależne przekazania między agentami."
genre: ["Sztuczna inteligencja", "Współpraca zespołowa", "Inżynieria oprogramowania"]
tags: ["kurs współpracy AI", "rozbieżność źródeł", "odzyskiwanie publikacji", "przekazanie agentowi", "weryfikacja aktualnych źródeł", "kompensacja"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustracja przedstawiająca specjalistów wspólnie przeglądających pracę projektową w środowisku cyberbezpieczeństwa"
coverCaption: ""
---
[Powrót do kursu współpracy AI](/ai-collaboration-course-start/)

**Sprawdzaj rozbieżności przed zadaniami i po przerwaniu publikacji.** Porównaj wersje źródeł, wersje adapterów i stan dostarczenia w repozytorium lub piaskownicy roboczej. Zrób to po ukończeniu jednego etapu. Dzięki temu stare podsumowania nie staną się aktualnym źródłem prawdy, a historia odzyskiwania pozostanie możliwa do przejrzenia.

## Najważniejsze informacje

- **Rozbieżność źródła** różni się od rozbieżności adaptera.
- **Częściowa publikacja** wymaga osobnego rejestru dla każdego systemu.
- **Odzyskiwanie** zachowuje historię wraz ze sprawdzonymi zmianami.
- **Przekazanie** wymaga, aby odbiorca samodzielnie odczytał aktualne źródła.

## Zanim zaczniesz

**Wymagania wstępne:** [praca z GitHubem w przeglądarce](/articles/ai-collaboration-github-browser-workflow/) lub [mieszany przepływ publikacji](/articles/ai-collaboration-confluence-jira-publication/). **Szacowany czas:** 60 do 90 minut. **Poziom trudności:** zaawansowana weryfikacja.

**Bezpieczeństwo:** używaj wyłącznie danych syntetycznych. Wstrzymaj automatyczną publikację przed testami odzyskiwania. Nie dostarczono działającej usługi usuwania.

**Efekt dla czytelnika:** przygotuj inwentaryzację stanu, decyzję właściciela, sprawdzoną naprawę oraz przekazanie, które inny recenzent odtworzy na podstawie aktualnych źródeł. Ukończenie ćwiczenia nie oznacza zgody na publikację.

## Klasyfikowanie rozbieżności

| Rozbieżność | Sygnał | Osoba odpowiedzialna za naprawę |
|---|---|---|
| **Wymaganie** | Źródło różni się od manifestu | Właściciel produktu |
| **Polityka** | Adapter różni się od POL-01 | Właściciel polityki |
| **Implementacja** | Konfiguracja przeczy założeniom | Opiekun |
| **Runbook** | Instrukcje przeczą zatwierdzonemu działaniu | Właściciel operacji |
| **Dostęp** | Odczyt wcześniej dostępnego źródła został odrzucony | Administrator, zadanie zatrzymane |
| **Dostarczenie** | Oznaczone jako gotowe bez kompletnego rejestru | Właściciel dostarczenia |

**Najnowszy tekst nie zawsze jest zatwierdzonym źródłem prawdy.** Niedawna nieautoryzowana edycja wymaga zbadania, a nie automatycznego przyjęcia. Przed skopiowaniem wartości ustal status i właściciela.

## Wykonanie kontroli wstępnej

```text
Read MAP-01 and capture its revision.
Read POL-01 and compare active adapter versions.
Read REQ-17 and RUN-04 from mapped homes.
Read config.json at protected main.
Read frozen proposal and current role reviews.
Compare current sources with reviewed bases.
List mismatches, denied reads, and pending publications.
Stop consequential writes until owners resolve each mismatch.
```

**Autor wkładu wykonuje kontrolę wstępną przed przygotowaniem projektu. Wydawca powtarza ją przed wprowadzeniem zmian.** Dołącz porównanie wersji do projektu. Cotygodniowe kontrole uzupełniają odczyt aktualnych źródeł, ale go nie zastępują.

**Przykład rozbieżności adaptera:** POL-01 osiąga wersję 2, a CLAUDE.md nadal wskazuje wersję 1. Zatrzymaj się, przeczytaj sprawdzoną zmianę polityki, zaktualizuj adapter przez chroniony PR i rozpocznij nową sesję. Sama zmiana numeru wersji bez wczytania polityki nie odświeża kontekstu.

**Wprowadzenie rozbieżności źródła w laboratorium offline:** rozpakuj nową kopię dostarczonego archiwum ZIP w pustym katalogu tymczasowym. Z jego katalogu głównego skopiuj `baseline/` do `candidate/`, uruchom `python3 check.py capture --base baseline > candidate/context.json`, a następnie `python3 check.py validate --base baseline --candidate candidate`. Zapisz początkowy wynik `PASS`. Otwórz `baseline/requirement.json` w edytorze tekstu i zmień wyłącznie `"retention_days": 7` na `"retention_days": 8`. Uruchom ponownie to samo polecenie validate. Oczekiwany status zakończenia jest niezerowy, a komunikat brzmi `STALE_CONTEXT: capture the trusted base again`. Zapisz oba wyniki i ścieżkę zmienionego źródła. Po zachowaniu prywatnych dowodów usuń tymczasowe rozpakowane pliki, a następnie rozpakuj nową kopię, aby zresetować środowisko. Nie wprowadzaj zmiany ośmiu dni do opublikowanego repozytorium i nie traktuj ponownego przechwycenia jako zgody właściciela.

**Wprowadzenie rozbieżności adaptera w tymczasowym repozytorium:** na nowej gałęzi projektu skopiuj zatwierdzony tekst adaptera POL-01 w wersji 1 do CLAUDE.md i oznacz go jako wersję 1. W osobnym, sprawdzanym projekcie polityki opisz zmianę do wersji 2 z konkretnym nowym warunkiem zatrzymania. Pozostaw adapter w wersji 1. Poproś recenzenta o porównanie obu zapisów i oznaczenie adaptera jako nieaktualnego przed scaleniem lub uruchomieniem agenta. Zresetuj test przez zamknięcie projektów albo aktualizację adaptera w sprawdzonym PR. Następnie otwórz nową sesję i zweryfikuj obie wersje oraz nowy warunek zatrzymania. Zachowaj stare i poprawione diffy. To test dokumentacji, a nie symulowana odmowa platformy.

## Odzyskiwanie przerwanej publikacji

1. **Wstrzymaj publikację PROP-042** i wyznacz osobę odpowiedzialną za odzyskiwanie.
2. **Odczytaj faktyczny stan** we wszystkich zaangażowanych systemach. Rozróżnij zakończone, nieudane i nierozpoczęte działania.
3. **Poproś zespół produktu o wybór:** kontynuacja, sprawdzone wycofanie albo wstrzymanie.
4. **Przygotuj projekt odzyskiwania** na podstawie aktualnych wersji, zachowując zakres i wyjątki, chyba że zostały osobno sprawdzone.
5. **Wykonuj po jednej sprawdzonej czynności**, zapisując i ponownie odczytując każdy wynik.
6. **Zweryfikuj stan końcowy** i pozostałe ograniczenia przed wznowieniem zwykłej pracy.

```yaml
recovery_id: RECOVERY-042
proposal_id: PROP-042
mode: awaiting-owner-choice
illustrative_state:
  requirement: thirty-days-published
  implementation: seven-days-on-main
  runbook: seven-days
  delivery: blocked
choices:
  forward: finish approved implementation and runbook
  backout: restore baseline through reviewed changes
  hold: wait for evidence or access
```

**Zastąp przykładowe stany zaobserwowanymi rewizjami i wartościami.** Wcześniejszy wpis w rejestrze ani twierdzenie asystenta nie stanowią dowodu ponownego odczytu.

| Wybór | Kiedy użyć | Ograniczenie |
|---|---|---|
| **Kontynuacja** | Zgoda pozostaje aktualna, a źródła są zgodne | Wymaga świeżej weryfikacji |
| **Wycofanie** | Właściciel cofa zmianę lub implementacja zawodzi | Nie odzyskuje usuniętych danych |
| **Wstrzymanie** | Brakuje dowodów lub dostępu | Dostarczenie pozostaje nieukończone |

**Wybierz wstrzymanie, gdy brakuje dowodów.** Syntetyczne ćwiczenia nie uzasadniają ślepego nadpisywania. Wskaż kolejną rolę i brakujące dowody.

**Odzyskiwanie w GitHubie** używa sprawdzonego revertu lub kompensacji. **Odzyskiwanie w Confluence** porównuje historię i stosuje sprawdzone przywrócenie lub kompensację. **Odzyskiwanie w Jira** zachowuje historię projektu, jednocześnie ponownie otwierając lub blokując dostarczenie. Odczytaj wynikowe rewizje zamiast zakładać, że numeracja historii zaczyna się od nowa.

## Weryfikacja niezależnego przekazania

```text
Handoff: HANDOFF-042
Task: PROP-042
Map and policy: attach current approved revisions
Evidence: requirement, runbook, configuration references
Ledger: completed, failed, pending
Decision: owner choice and fixed proposal revision
Limits: no runtime deletion test or production data
Next role: accountable role
Next action: one bounded step
Stop: changed base, access denial, conflicting authority
```

**Otwórz inne narzędzie lub czystą sesję** z mapą i przekazaniem, bez poprzedniej rozmowy. Wymagaj świeżych odczytów źródeł, nowego manifestu i wskazania nierozstrzygniętej czynności. Ręczne dowody z przeglądarki pozostają ważne, jeśli oznaczysz je jako zrzut stanu i sprawdzisz ponownie przed zapisem.

**Negatywny test przekazania:** odbierz dostęp do REQ-17. Oczekuj jawnej blokady zamiast zgadywania lub uprzywilejowanego fragmentu. Przywróć wyłącznie zatwierdzony dostęp przez administratora i ponów weryfikację.

## Najpierw diagnoza

**Zacznij od inwentaryzacji stanu.** „Asystenci się nie zgadzają” opisuje objaw w odpowiedzi, a nie źródłowy problem. Przed zleceniem naprawy któremukolwiek asystentowi odczytaj niezależnie przypisane wymaganie, konfigurację, runbook, politykę i zapis dostarczenia.

| Obserwacja | Diagnoza | Pierwsze działanie |
|---|---|---|
| **Oba źródła zgodne, stara odpowiedź różna** | Nieaktualny kontekst odpowiedzi | Odtwórz stan na podstawie świeżych odczytów |
| **Wymaganie trzydzieści, konfiguracja siedem** | Niezgodność dostarczenia lub implementacji | Sprawdź zatwierdzony pakiet i rejestr |
| **Adapter jeden, polityka dwa** | Niezgodność wersji instrukcji | Przeczytaj zmianę polityki i napraw adapter |
| **Źródło było dostępne, teraz odmowa** | Zmiana dostępu | Zatrzymaj zadanie i poproś o uprawniony przegląd |
| **Rejestr kompletny, runbook siedem** | Zamknięcie bez prawidłowego odczytu zwrotnego | Otwórz lub zablokuj dostarczenie i zbadaj sprawę |

**Nie uznawaj każdej rozbieżności za problem modelu.** Odświeżenie sesji naprawia nieaktualny kontekst rozmowy. Nie publikuje runbooka, nie przywraca brakujących uprawnień ani nie rozstrzyga sprzecznych decyzji właścicieli. Zanim wybierzesz działanie w narzędziu, wskaż osobę odpowiedzialną za naprawę.

## Przykład kompensacji

**Przykładowe przerwanie:** REQ-17 zawiera zatwierdzoną intencję trzydziestu dni, a dostarczenie pozostaje w toku. Konfiguracja i runbook nadal wskazują siedem. Opiekun zgłasza nierozwiązany błąd implementacji. Zespół produktu wybiera przywrócenie zamiast kontynuacji.

1. **Zapisz bieżące wersje:** wymaganie trzydzieści, konfiguracja siedem, runbook siedem, dostarczenie zablokowane.
2. **Wstrzymaj oczekujący projekt:** zachowaj recenzje i dowody nieudanej publikacji.
3. **Przygotuj kompensującą zmianę wymagania:** przywróć siedem, zachowując późniejsze wykluczenia i notatki.
4. **Uzyskaj ocenę właściciela:** wskaż bieżącą wersję źródła i dokładne brzmienie przywrócenia.
5. **Opublikuj zatwierdzoną ścieżką:** odczytaj nową wersję wymagania.
6. **Uzgodnij rejestr:** wszystkie obowiązujące opublikowane wartości wynoszą siedem, a pierwotna zmiana nie została dostarczona.

**Kompensacja nie usuwa historii.** Zachowaj osobno próbę zmiany na trzydzieści dni, jej niepowodzenie i późniejsze przywrócenie. Źródło końcowe wskazuje siedem, a historia dostarczenia wyjaśnia, dlaczego zatwierdzony projekt nie został ukończony.

```text
Recovery decision: illustrative compensation
Original proposal: PROP-042 revision 1
Observed mismatch: requirement 30, configuration/runbook 7
Owner decision: restore approved baseline intent
Review object: fixed compensation against current requirement version
Result: capture resulting revision and seven-day read-back
Original delivery: withdrawn or blocked with explanation
Limit: no runtime deletion or data restoration performed
```

**Jawnie zachowaj wyjątek dodany przez innego autora.** Ślepe wklejenie treści starej strony może usunąć prawidłową zmianę wprowadzoną po drodze. Porównaj aktualny i zamierzony tekst, a następnie sprawdź minimalną zmianę kompensującą względem aktualnej wersji.

## Test świeżego przekazania

**Użyj czystej sesji i innego recenzenta.** Przekaż mapę, ustalony pakiet, rejestr i decyzję odzyskiwania. Nie pokazuj poprzedniego czatu. Poproś odbiorcę o wskazanie bieżącej intencji, konfiguracji, instrukcji operacyjnych i następnego dozwolonego działania.

```text
Read the mapped current sources independently.
Distinguish approved intent, committed configuration, and delivery state.
Compare them with the reviewed package and ledger.
List missing reads and changed bases.
Recommend one bounded next action with its accountable role.
Do not treat this handoff as approval or publication permission.
```

**Oczekiwane rozumowanie:** odbiorca weryfikuje wynik kompensacji przed opisaniem przywrócenia stanu bazowego. Jeśli jedynie powtórzy „siedem dni” z przekazania, wymóg niezależnego odczytu nie został sprawdzony. Poproś o dowody ze źródeł zamiast kolejnego podsumowania.

**Ukończona inwentaryzacja szkoleniowa, syntetyczne przerwanie:**

| Zapis | Zaobserwowany stan | Zachowane dowody | Następny właściciel |
|---|---|---|---|
| REQ-17 | v5 mówi o trzydziestu dniach, kopie zapasowe wyłączone | Historia strony i świeży odczyt | Produkt |
| Chroniona konfiguracja | `main` na `base-001` wskazuje siedem dni | Odczyt commita i odmowa scalania | Opiekun repozytorium |
| RUN-04 | v2 nadal wskazuje siedem dni | Świeży odczyt strony | Operacje |
| PROP-042 | r1 zatwierdzona, dostarczenie zablokowane | Ustalone recenzje i rejestr | Właściciel dostarczenia |

Przekaż tę inwentaryzację drugiej osobie bez starego czatu. Przekazanie zalicza się tylko wtedy, gdy odbiorca samodzielnie znajdzie wszystkie cztery stany, wskaże wyłączenie kopii zapasowych, rozpozna `base-001` jako aktualną chronioną rewizję i zaproponuje krok odzyskiwania zatwierdzony przez właściciela. Oznacz jako niezaliczone błędną rewizję, brak wyjątku lub nieuzasadnione wznowienie. Zapisz odwołania do źródeł i poprawki odbiorcy przed kolejnym zapisem.

## Decyzja o wznowieniu

| Wynik kontroli wstępnej | Decyzja o wznowieniu |
|---|---|
| **Źródła zgodne z ustaloną zgodą** | Wykonaj dozwolony oczekujący krok |
| **Źródło zmienione poza sprawdzonym zakresem** | Zatrzymaj się i porównaj, uzyskaj nową ocenę |
| **Brak dostępu do odczytu** | Wstrzymaj zadanie z wyznaczonym recenzentem dostępu |
| **Zmieniła się polityka** | Napraw adaptery i ponownie oceń uprawnienie do zadania |
| **Nieznany wynik zapisu** | Odczytaj cel przed ponowieniem próby |

**Ustal konkretne kryteria akceptacji odzyskiwania.** Wymagaj zgodnego odczytu zwrotnego, aktualnego obiektu recenzji, uzgodnionego rejestru i świeżego przekazania. Nie zamykaj odzyskiwania, bo asystent twierdzi, że problem rozwiązano.

**Kontrola ukończenia:** dostarcz zaobserwowaną inwentaryzację stanu, decyzję właściciela, sprawdzoną naprawę, końcowy odczyt zwrotny i niezależną rekonstrukcję. Jeśli dostęp uniemożliwia odczyt, udokumentuj blokadę. Zastosuj ten standard dowodów w projekcie końcowym.

## Rozwiązywanie problemów i wycofywanie zmian

**Konflikty podczas revertu:** przygotuj zmianę kompensującą względem bieżącego stanu. **Przywrócenie usuwa wyjątki:** przed zapisem porównaj całą istotną sekcję. **Odpowiedź kontroluje stara pamięć:** rozpocznij ponownie na podstawie zatwierdzonych źródeł i usuń nieaktualny kontekst wersji roboczej.

**Wycofanie odzyskiwania:** zatrzymaj się na ostatnim zweryfikowanym stanie i dodaj wpis do rejestru. Nie usuwaj natywnych zdarzeń audytowych ani nie wymuszaj resetu chronionej historii. Nierozstrzygnięte kwestie uprawnień przekaż do zespołu produktu.

## Ćwiczenie i samoocena

**Wprowadź nieaktualne dowody, przestarzały adapter polityki i częściową publikację.** Przekaż zapisy innemu recenzentowi bez objaśnień i poproś o wskazanie osoby odpowiedzialnej za naprawę.

**Oczekiwane rozumowanie:** zespół produktu odpowiada za uzgodnienie wymagań, właściciel polityki za dostosowanie adaptera, a koordynator odzyskiwania za uzgodnienie pracy zaangażowanych właścicieli. „Odśwież kontekst” nie jest pełną naprawą wszystkich tych przypadków.

## Główne źródła

- **Kontrole odzyskiwania w repozytorium:** [Chronione gałęzie](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Historia stron:** [Dokumentacja Confluence](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Inspekcja instrukcji:** [Pamięć Claude Code](https://code.claude.com/docs/en/memory).

## Następne kroki

**Ukończ [Retention Capstone](/articles/ai-collaboration-retention-capstone/)** z użyciem obu ścieżek i drugiego czytelnika. Pokaż świeże odczyty źródeł, rozbieżności wersji, decyzję właściciela, sprawdzone odzyskiwanie, odczyt zwrotny i niezależną rekonstrukcję.
