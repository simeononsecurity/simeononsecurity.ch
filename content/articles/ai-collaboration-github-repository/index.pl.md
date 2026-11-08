---
title: "Współpraca AI w GitHubie: granice repozytorium i przeglądu"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Zbuduj mapę źródeł, własność plików i chronioną granicę publikacji dla sprawdzanych zmian wnoszonych przez AI."
genre: ["Sztuczna inteligencja", "Współpraca zespołowa", "Inżynieria oprogramowania"]
tags: ["kurs współpracy AI", "repozytorium GitHub", "ochrona gałęzi", "CODEOWNERS", "mapa źródeł", "przegląd pull requestów", "kontrola publikacji"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustracja przedstawiająca specjalistów wspólnie przeglądających pracę projektową w środowisku cyberbezpieczeństwa"
coverCaption: ""
---
[Powrót do kursu współpracy AI](/ai-collaboration-course-start/)

**Po zatwierdzeniu karty projektu opiekun tworzy granicę publikacji opartą na GitHubie.** Wymagania, konfiguracja, polityka i runbook znajdują się w jednym tymczasowym repozytorium. Współpracownicy proponują zmiany przez Issues i pull requesty. Ustalasz, gdzie znajdują się zatwierdzone fakty, i blokujesz nieprzejrzane zmiany przed podłączeniem agentów.

## Najważniejsze informacje

- **Chroniona gałąź `main`** stanowi granicę publikacji.
- **Issues** zbierają propozycje, ale nie zatwierdzają polityki.
- **CODEOWNERS** przypisuje uprawnionych recenzentów plików.
- **Oddzielne konta** pozwalają wykazać kontrolę przeglądu i odmowy.

## Zanim zaczniesz

**Wymagania wstępne:** [podstawa pilotażu](/articles/ai-collaboration-pilot-foundation/), rozpakowane laboratorium, administrator repozytorium oraz oddzielni recenzenci produktu i operacji. **Szacowany czas:** 60 minut. **Poziom trudności:** umiarkowany.

**Granice planu:** GitHub dokumentuje chronione gałęzie dla publicznych repozytoriów w planie Free oraz prywatnych repozytoriów w planach Pro, Team lub Enterprise. W publicznych repozytoriach używaj wyłącznie treści syntetycznych. Przed poleganiem na egzekwowaniu zasad sprawdź widoczność i plan w dokumentacji ochrony gałęzi.

**Wynik:** chroniona gałąź publikacyjna, właściciele plików, mapa źródeł i test odmowy zapisany jako dowód.

## Utwórz repozytorium

1. **Utwórz `export-service-lab`** z plikiem README i domyślną gałęzią **`main`**.
2. **Skopiuj rozpakowane laboratorium** do katalogu głównego repozytorium, zachowując **`check.py`**, **`test_check.py`** i **`baseline/`**. Skopiuj pliki z `baseline/` do katalogu głównego jako rekordy początkowe.
3. **Utwórz `docs/project-map.md`** na podstawie rejestru z podstawy pilotażu. Dodaj **`docs/policy.md`** z zatwierdzonym POL-01.
4. **Utwórz `docs/decisions/DEC-12.md`** z zatwierdzeniem karty, rolami, decyzją dotyczącą bazy i statusem.
5. **Zatwierdź konfigurację początkową** jako administrator. Zapisz ten początkowy wyjątek. Włącz ochronę przed kolejnymi zmianami.

**Lokalna konfiguracja w Git Bash, Terminalu macOS lub powłoce Linuksa:** zaloguj się do GitHuba w przeglądarce, otwórz nowe repozytorium, wybierz **Code** i skopiuj adres HTTPS do klonowania. W tymczasowym katalogu roboczym uruchom poniższe polecenia. Zastąp dwie przykładowe ścieżki adresem URL i ścieżką pobranego ZIP-a laboratorium. Nie umieszczaj tokenu w adresie URL.

```bash
git --version
git clone "https://github.com/OWNER/export-service-lab.git"
cd export-service-lab
unzip -n "/absolute/path/to/ai-collaboration-lab.zip"
cp baseline/config.json baseline/policy.json baseline/proposal.json baseline/requirement.json baseline/runbook.md .
mkdir -p docs/decisions
git status --short
```

Polecenie clone powinno utworzyć katalog repozytorium. Jeśli `unzip` nie jest dostępne, rozpakuj ZIP menedżerem plików i skopiuj zawartość do tego checkoutu, pozostawiając README repozytorium. `git status --short` powinno pokazać skopiowane rekordy, checker, testy i `baseline/` jako nowe pliki. Zapisz `docs/project-map.md`, `docs/policy.md` i `docs/decisions/DEC-12.md` z pakietu pilotażowego za pomocą edytora tekstu. Następnie uruchom:

```bash
git add README.md baseline check.py test_check.py config.json policy.json proposal.json requirement.json runbook.md docs
git commit -m "Add synthetic collaboration baseline"
git push origin main
git status --short
git remote -v
```

Git powinien zgłosić nowy identyfikator commita, a potem udany push do `main`. Końcowy krótki status powinien być pusty. Otwórz repozytorium GitHub w nowym widoku przeglądarki i potwierdź, że pliki oraz identyfikator commita są widoczne na `main`. Zapisz adres URL commita jako dowód konfiguracji początkowej. Jeśli Git poprosi o tożsamość autora, skorzystaj z instrukcji konfiguracji w centrum kursu. Jeśli uwierzytelnienie nie działa, użyj obsługiwanego przez GitHub sposobu zarządzania poświadczeniami, a następnie ponów ten sam push. Jeśli gałąź lub zdalne repozytorium są nieprawidłowe, zatrzymaj się i sprawdź `git branch --show-current` oraz `git remote -v` przed kolejnym zapisem. Jeśli push zostanie odrzucony, bo ochrona została już włączona, utwórz gałąź propozycji i PR zamiast omijać regułę. Dostępna jest też poniższa ścieżka wyłącznie przez przeglądarkę z pomocą opiekuna.

| Rekord | Lokalizacja | Właściciel |
|---|---|---|
| **POL-01** | `policy.json`, `docs/policy.md` | Właściciel polityki |
| **REQ-17** | `requirement.json` | Właściciel produktu |
| **RUN-04** | `runbook.md` | Właściciel operacji |
| **Zachowanie** | `config.json` | Opiekun repozytorium |
| **Decyzje** | `docs/decisions/` | Lider projektu |

**Mapa wskazuje lokalizacje zamiast kopiować wartości.** README powinno skupiać się na konfiguracji i mapie. Powtórzone wymagania dotyczące retencji powodują rozbieżności nawet w jednym repozytorium.

## Przypisz właścicieli plików

**Lokalnie wygeneruj `.github/CODEOWNERS`** z prawdziwymi uchwytami kont w piaskownicy. Wpisuj uchwyty bez początkowego znaku **`@`**. Tożsamości kont przechowuj w prywatnym laboratorium, a nie w publicznych dowodach ćwiczenia.

```bash
python3 - <<'PY'
from pathlib import Path
roles = ['product', 'operations', 'maintainer', 'policy']
handles = {r: input(r + ' GitHub handle: ').strip().lstrip('@') for r in roles}
if any(not h or not all(c.isalnum() or c == '-' for c in h) for h in handles.values()):
    raise SystemExit('Invalid handle')
paths = {'requirement.json': 'product', 'runbook.md': 'operations',
         'config.json': 'maintainer', 'policy.json': 'policy',
         'docs/policy.md': 'policy', 'AGENTS.md': 'policy',
         'CLAUDE.md': 'policy', '.clinerules/': 'policy',
         '.github/': 'maintainer', 'check.py': 'maintainer',
         'test_check.py': 'maintainer', 'baseline/': 'maintainer'}
Path('.github').mkdir(exist_ok=True)
Path('.github/CODEOWNERS').write_text(''.join(
    '/' + path + ' @' + handles[role] + '\n' for path, role in paths.items()))
PY
```

**Właściciele muszą mieć uprawnienia zapisu**, aby GitHub ich rozpoznawał. Sprawdź w przeglądarce, czy plik CODEOWNERS nie zawiera błędów. Chroń pliki własności i definicje przepływów pracy tak samo jak zwykłą treść.

**Wpisanie kilku nazw w jednym wierszu nie wymaga akceptacji wszystkich właścicieli.** GitHub przyjmuje jedną zgodę uprawnionego właściciela dla pasującej ścieżki. Przypisz różnych właścicieli do ścieżek wymagania i runbooka. Pilotaż wymaga też poświadczeń właściciela produktu i operacji powiązanych z końcową propozycją.

## Chroń publikację

1. **Otwórz Ustawienia, Gałęzie** i dodaj regułę ochrony gałęzi dla **`main`**. W tym ćwiczeniu konsekwentnie używaj ochrony gałęzi, nie mieszaj jej z rulesetami.
2. **Wymagaj pull requesta,** dwóch zatwierdzających recenzji i przeglądu właścicieli kodu.
3. **Odrzucaj nieaktualne zatwierdzenia** po nowych commitach i wymagaj rozwiązania wątków rozmowy.
4. **Włącz opcję „Nie zezwalaj na omijanie powyższych ustawień”.** Wyłącz wymuszony push i usuwanie gałęzi.
5. **Dodaj kontrolę spójności** po jej pierwszym uruchomieniu w następnym module. Wymagaj aktualności gałęzi przed scaleniem.

**Dwa zatwierdzenia wymuszają liczbę, a nie przynależność do ról biznesowych.** CODEOWNERS dodaje pokrycie właścicieli zależne od ścieżki. Opiekun sprawdza też poświadczenia dwóch ról. Zapisz tę kontrolę proceduralną wprost, zamiast opisywać ją jako automatyczne wymuszenie dwóch ról.

**Administratorzy nadal zarządzają konfiguracją.** Zrób zrzut reguły przed testami i po nich. Nie przyznawaj agentowi uprawnień administratora ani nie używaj uprzywilejowanego tokenu do demonstracji odmowy współpracownikowi.

## Zweryfikuj granicę

| Próba | Oczekiwany wynik |
|---|---|
| **Współpracownik wysyła gałąź** | Propozycja dozwolona |
| **Współpracownik publikuje bezpośrednio** | Chroniona publikacja odrzucona |
| **Jedna osoba zatwierdza** | Scalanie zablokowane przez próg recenzji |
| **Po recenzji pojawia się nowy commit** | Wymagana jest świeża akceptacja |
| **Wrażliwy plik nie ma przypisanego właściciela** | Napraw przed publikacją |

**Użyj sesji przeglądarki współpracownika, aby sprawdzić ścieżkę.** Edytor internetowy GitHuba nie edytuje chronionej gałęzi **`main`**. Prośba o utworzenie gałęzi pokazuje obsługiwaną ścieżkę w przeglądarce. Nie dowodzi, że serwer odrzucił bezpośredni push. Aby uzyskać dowód odmowy platformy, poproś współpracownika z zatwierdzonym lokalnym dostępem Git o próbę nieszkodliwego bezpośredniego pushu do chronionej gałęzi **`main`** i zachowaj odpowiedź serwera. Oznacz test odmowy jako Zablokowany, jeśli lokalny dostęp jest niedostępny.

**Po odmowie odczytaj `main`** i potwierdź, że rewizja się nie zmieniła. Zapisz rolę wykonawcy, próbę, wynik i rewizję źródła. Obietnica asystenta, że nie opublikuje zmian, jest dowodem zachowania, a nie testem uprawnień platformy.

**Do testu bezpośredniego pushu użyj własnego uwierzytelnionego klonu współpracownika.** Token opiekuna sprawdzałby niewłaściwą tożsamość. Ten przykładowy komunikat pokazuje rodzaj odpowiedzi serwera, który należy zachować. Dokładne sformułowanie zależy od reguł repozytorium.

```text
Actor role: contributor
Attempt: harmless synthetic direct push to main
Remote result: rejected, protected branch update denied
Initial main commit: [record sandbox commit]
Final main commit: [record same commit after read-back]
Decision: platform denial supported only if both records are observed
```

**Jeśli lokalne uwierzytelnianie Git jest niedostępne, oznacz odmowę po stronie serwera jako Zablokowaną.** Zachowaj monit przeglądarki o utworzenie gałęzi jako dowód ścieżki, a następnie poproś opiekuna o zorganizowanie oddzielnego testu współpracownika. Nie oceniaj monitu o ścieżce jako odrzuconego bezpośredniego pushu.

## Zbuduj użyteczną mapę źródeł

**Mapa źródeł to dokument nawigacyjny**, a nie drugi dokument wymagań. Osoba przechodząca z czatu musi znaleźć aktualny zamiar, wdrożone zachowanie i instrukcje operacyjne bez wybierania między konkurencyjnymi podsumowaniami.

```text
Project: export-service-lab
Track: GitHub-first
Approved boundary: protected main

REQ-17 -> requirement.json
  Authority: retention intent for synthetic export files
  Owner: product-owner
  Revision: record revision plus protected commit

RUN-04 -> runbook.md
  Authority: operating instructions for the synthetic lab
  Owner: operations-owner
  Revision: protected commit

Behavior -> config.json
  Authority: committed retention configuration
  Owner: repository-maintainer
  Revision: protected commit

Proposals -> Issues and proposal branches
  Authority: requested changes only
```

**Nie wpisuj aktualnej wartości retencji do każdego wiersza mapy.** Mapa zawierająca „siedem dni” staje się kolejną wartością do synchronizowania po PROP-042. Umieszczaj w niej stabilne identyfikatory i lokalizacje, a wartość odczytuj z autorytatywnego rekordu.

**Chroń zmiany mapy jako zmiany routingu.** Przekierowanie REQ-17 do pliku roboczego zmienia wybór źródła, nawet jeśli zatwierdzone wymaganie pozostaje nietknięte. Przy każdej zmianie mapy sprawdź cel, właściciela i zakres autorytetu.

## Oddziel bazę od kandydata

**Katalog główny repozytorium zawiera aktywne rekordy laboratorium.** Pobrany katalog **`baseline/`** jest zestawem ćwiczeniowym. Nie jest automatycznie chronioną bazą dla każdego kolejnego PR. Gdy sprawdzona praca trafi na **`main`**, chronione rekordy w katalogu głównym stają się bazą następnej propozycji.

| Lokalizacja | Cel | Edytować w PROP-042? |
|---|---|---|
| **Wymaganie/konfiguracja/runbook w katalogu głównym** | Aktywne rekordy proponowane w gałęzi | Tak, przez sprawdzone zmiany |
| **`baseline/`** | Pierwotny zestaw ćwiczeniowy offline | Nie |
| **Odłączony zaufany worktree** | Zarejestrowane chronione rekordy z katalogu głównego | Nie |
| **`context.json`** | Dowód przechwycenia bajtów bazy | Wygeneruj ponownie po uzgodnieniu |

**Oddziel zmiany kontroli od zmian retencji.** Najpierw skonfiguruj checker i reguły przeglądu. Następnie zaproponuj zmianę z siedmiu na trzydzieści dni. Połączenie przepisywania polityki, przepływu pracy i wartości utrudnia recenzentowi odróżnienie naprawionych kontroli od ich obejścia.

## Przejrzyj całą zmianę

**Przed zaakceptowaniem opisu PR otwórz kartę Files changed.** Opis wyjaśnia zamiar autora. Diff pokazuje przesłaną zmianę. W PROP-042 sprawdź rewizję wymagania, wyłączenia zakresu, konfigurację, runbook, bazę propozycji i dowody z manifestu.

1. **Recenzja produktu:** potwierdź zamiar trzydziestu dni i niezmienione wyłączenia.
2. **Recenzja operacji:** potwierdź, że runbook odpowiada proponowanej konfiguracji i zachowuje ograniczenie środowiska wykonawczego.
3. **Recenzja opiekuna:** sprawdź JSON, przechwycenie źródła, wyniki kontroli i niepowiązane edycje.
4. **Recenzja kontroli:** osobno sprawdź wszelkie zmiany mapy, polityki, CODEOWNERS lub przepływu pracy.

**Zielony check nie wyjaśnia niepowiązanego usunięcia.** Jeśli gałąź usuwa dokument polityki przy zmianie retencji, poproś o osobną propozycję lub konkretną recenzję właściciela. Ograniczony zakres ułatwia zrozumienie obiektu przeglądu.

## Zdiagnozuj test odmowy

**Dla każdego wiersza dowodów użyj jednej próby działania.** „Współpracownikowi się nie udało” jest niejednoznaczne. Użytkownik może nie mieć zwykłego dostępu do zapisu, napotkać ograniczenie przeglądarki albo trafić na zamierzoną regułę gałęzi. Te obserwacje wyznaczają różne granice.

| Obserwacja | Interpretacja | Dalsze działanie |
|---|---|---|
| **Nie można utworzyć żadnej gałęzi** | Brak dostępu do współtworzenia | Użyj zatwierdzonej ścieżki Issue lub forka |
| **Można utworzyć gałąź, nie można publikować do main** | Sprawdzona ścieżka publikacji jest ograniczona | Zapisz niezmienioną rewizję main |
| **Scalanie blokuje jedna recenzja** | Próg recenzji działa dla sprawdzonego PR | Dodaj dowód dotyczący roli |
| **Administrator publikuje mimo reguły** | Sprawdzona tożsamość omija granicę | Sprawdź ustawienia omijania i uprawnienia |

**Wspólny dowód kursu zapisuj z rolą i działaniem, bez ujawniania danych konta.** Oryginalne rekordy wykonawców zachowaj prywatnie do dyspozycji recenzenta. Zestaw konfigurację reguły, próbę operacji, odmowę i wynikową chronioną rewizję.

## Kontrola ukończenia repozytorium

**Dostarcz repozytorium, po którym inny współpracownik porusza się samodzielnie.** README wskazuje mapę, mapa prowadzi do autorytatywnych rekordów, przypisanie właścicieli obejmuje wrażliwe ścieżki, a ochrona dotyczy **`main`**. Zachowaj jedną dozwoloną propozycję i jedną odrzuconą próbę publikacji.

**Nie deklaruj egzekwowania wyłącznie na podstawie ustawień.** Ustawienia pokazują zamierzoną konfigurację. Próba w piaskownicy pokazuje obserwowane zachowanie dla konkretnej roli i ścieżki. Uwzględnij oba dowody w lekcji o agentach i GitHub Actions.

## Rozwiązywanie problemów i wycofywanie

**Brak żądania właściciela:** potwierdź dostęp do zapisu i przypisanie ścieżki gałęzi bazowej. **Brak ochrony:** sprawdź plan i widoczność. **Scalanie nadal możliwe:** sprawdź cel reguły, konfigurację omijania i liczbę recenzji.

**Wycofanie:** zamknij niescalone propozycje i wyłącz automatyzację laboratorium. Scalony materiał laboratoryjny wycofaj przez kolejny sprawdzony PR. Zachowaj dowody przed usunięciem tymczasowego repozytorium. Nie osłabiaj ochrony, aby zaliczyć nieudany test.

## Ćwiczenie i samoocena

**Jako współpracownik zaproponuj edycję `docs/policy.md`.** Zastanów się, czy sama akceptacja opiekuna potwierdza zgodę właściciela polityki.

**Oczekiwane rozumowanie:** sama liczba recenzji nie potwierdza uprawnień. Ścieżka wymaga pokrycia przez właściciela polityki i aktualnej oceny ról. Wymagania dotyczące ról, które nie są egzekwowane automatycznie, wymień jako kontrole proceduralne.

## Główne źródła

- **Kontrola planu i przeglądu:** [Chronione gałęzie](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Uprawnienia właścicieli:** [Właściciele kodu](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
- **Współtworzenie przez przeglądarkę:** [Edycja plików](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).

## Następne kroki

**Kontynuuj z modułem [Adaptery agentów i GitHub Actions](/articles/ai-collaboration-github-agents-actions/)**, aby połączyć dowody ze źródeł z wykonywalnymi kontrolami.
