---
title: "1Password SSH Agent and CLI: Read-Only AI Agent Access"
date: 2026-10-11
lastmod: 2026-10-28
toc: true
draft: false
description: "Zaprojektuj workflow tylko do odczytu z użyciem 1Password CLI, SSH Agent oraz MCP. Wykorzystaj syntetyczne polecenia, zawężone uprawnienia i zatwierdzenie przez człowieka przed testami na żywo."
genre: ["Administracja systemami", "Bezpieczeństwo chmury", "Automatyzacja"]
tags: ["1Password CLI", "klucze SSH", "1Password SSH Agent", "MCP", "Model Context Protocol", "administracja agentami", "administracja systemami", "Bitbucket Cloud", "Git over SSH", "odniesienia do sekretów", "konta usługowe", "minimalne uprawnienia", "uwierzytelnianie kluczem publicznym", "zarządzanie sekretami", "bezpieczeństwo wiersza poleceń", "bezpieczeństwo automatyzacji"]
cover: "/img/cover/1password-cli-ssh-keys-mcp-agent-administration.webp"
coverAlt: "Abstrakcyjny diagram agenta korzystającego z odniesienia do sekretu, agenta SSH oraz narzędzi MCP, bez pokazywania kluczy prywatnych."
coverCaption: ""
---

**Agent wiersza poleceń potrzebuje przydatnego dostępu, nie kopii każdego poświadczenia.** Ten przewodnik przedstawia ograniczony projekt dla 1Password CLI, 1Password SSH Agent, dostępu do Bitbucket Git oraz Model Context Protocol (MCP). Pierwszy przepływ pracy używa syntetycznych nazw, akcji tylko do odczytu i zatwierdzenia przez człowieka na granicy SSH.

<!--more-->

Kluczowa różnica jest prosta. **Interaktywny SSH używa zgody za pośrednictwem 1Password SSH Agent. Automatyzacja bez nadzoru wymaga osobnej tożsamości, wąskiego zakresu dostępu i innego cyklu życia klucza.** Nie traktuj połączenia MCP jako pozwolenia na uruchomienie żadnego z tych przepływów pracy.

## Kluczowe wnioski

- **Ochrona klucza prywatnego:** 1Password SSH Agent wykonuje uwierzytelnianie SSH, utrzymując klucze prywatne wewnątrz aplikacji 1Password.
- **Obsługa klucza publicznego:** Publikuj wyłącznie klucz publiczny w Bitbucket lub na zdalnym koncie. Zachowaj połowę prywatną w elemencie SSH Key.
- **Interaktywna zgoda:** Osoba zatwierdza klienta lub sesję terminala, zanim SSH Agent użyje klucza.
- **Separacja bez nadzoru:** Zadanie zaplanowane wymaga dedykowanego konta usługi i wąskiego zakresu sejfów. Zatwierdzenie przez interaktywnego SSH Agent nie spełnia tego wymogu.
- **Granice MCP:** MCP łączy agenta z narzędziami i zasobami. Klient, serwer, system operacyjny oraz polityka 1Password nadal kontrolują dostęp.

## Przed rozpoczęciem

**Wymagania wstępne:** Zainstaluj 1Password 8 i 1Password CLI 2.20.0 lub nowszy. Zaloguj się za pomocą wspieranego konta 1Password. Używaj klienta OpenSSH. Utwórz testowe repozytorium Bitbucket lub inny cel inny niż produkcyjny. Zachowaj drugą ścieżkę administracyjną do cofnięcia zmian.

**Czas:** 30 do 45 minut na przegląd projektu i syntetyczny przebieg.

**Poziom trudności:** Średni. Wymagana jest podstawowa wiedza na temat Git, SSH, powłoki (shell) i kontroli dostępu.

Ten przewodnik obejmuje projektowanie i planowanie. Powiązany artykuł o Bitbucket obejmuje specyficzne dla Bitbucket granice dostępu. Ten przewodnik nie testuje konta na żywo, nie tworzy prawdziwego klucza, nie łączy się z prawdziwym hostem ani nie rejestruje prawdziwego serwera MCP. Wszystkie identyfikatory poniżej są syntetyczne. **Zastępuj placeholdery wyłącznie we własnym kontrolowanym środowisku.**

**Postawa wersyjna:** Używaj 1Password 8 i [1Password CLI 2.20.0 lub nowszego](https://www.1password.dev/ssh/manage-keys) dla tego przepływu pracy. [1Password CLI 1 jest przestarzałe](https://www.1password.dev/cli/upgrade/). [1Password 7 wycofuje się na początku 2027 roku](https://support.1password.com/add-account/). Generowanie, import i udostępnianie kluczy SSH wymagają 1Password 8. Potwierdź zainstalowane wersje Git, OpenSSH, hosta MCP i serwera MCP przed testami. Przykłady poniżej pozostają nietestowane.

**Klucz** to chroniona kolekcja elementów w 1Password. **OpenSSH** to oprogramowanie klienta i serwera SSH używane przez wiele systemów operacyjnych. **MCP**, czyli Model Context Protocol, łączy agenta z zatwierdzonymi narzędziami lub zasobami.

## Dlaczego nie odczytywać kluczy prywatnych

Para kluczy SSH składa się z klucza publicznego i klucza prywatnego. Zdalna usługa lub serwer Git przechowuje klucz publiczny. Klient udowadnia posiadanie klucza prywatnego podczas uwierzytelniania. Klucz prywatny nie musi być przesyłany do zdalnej usługi.

[1Password SSH Agent](https://www.1password.dev/ssh/agent) rozszerza ten model. Jego dokumentacja stwierdza, że klienci SSH i Git uwierzytelniają się za pośrednictwem agenta, podczas gdy klucz prywatny pozostaje w aplikacji 1Password. Klient otrzymuje wynik podpisu, a nie plik klucza prywatnego.

Ta granica zmniejsza kilka ścieżek narażenia:

- **Kontrola wersji:** Klucz prywatny nie trafia do repozytorium ani do żądania wyciągnięcia (pull request).
- **Historia powłoki:** Wartość klucza prywatnego nie pojawia się w argumencie polecenia.
- **Pliki tymczasowe:** Skrypt nie musi zapisywać klucza prywatnego do `~/.ssh/`.
- **Kontekst agenta:** Duży model językowy (LLM) nie potrzebuje tekstu klucza prywatnego, aby żądać operacji SSH.
- **Przypadkowe ponowne użycie:** Skopiowany klucz nie pozostaje w starym obszarze roboczym po zakończeniu zadania.

Ta granica nie czyni SSH nieszkodliwym. Proces z uprawnieniami do użycia gniazda agenta może wykonywać działania jako zatwierdzony klucz. Weryfikacja klucza hosta, ograniczenia zdalnego konta, uprawnienia repozytorium, polityka poleceń i izolacja procesów nadal mają znaczenie.

*Granica klucza prywatnego chroni materiał kluczowy. Granica nie zatwierdza zdalnego polecenia ani nie dowodzi, że docelowy host jest zaufany.*

## Interaktywna zgoda SSH

Skonfiguruj dedykowany klucz dla kluczy agenta. Użyj pliku konfiguracyjnego SSH Agent, aby wybrać najmniejszy zestaw kluczy i klucz specyficzny dla hosta. Nie ujawniaj każdego kwalifikującego się klucza z każdego wbudowanego klucza procesowi automatyzacji.

[Model bezpieczeństwa 1Password SSH Agent](https://www.1password.dev/ssh/agent/security) wiąże zatwierdzenie z kluczem i procesem żądającym. Prompt identyfikuje proces i klucz. Osoba następnie zatwierdza żądanie za pomocą skonfigurowanej metody uwierzytelniania.

1Password dokumentuje kilka zakresów zatwierdzania. Zatwierdzanie per klucz i per aplikacja jest domyślne. Zakres sesji terminala zawęża zatwierdzenie do karty lub sesji. Zatwierdzanie per żądanie pyta ponownie o każde żądanie. Istnieje opcja zatwierdzania wszystkich procesów, ale ta opcja daje każdemu procesowi pod bieżącym użytkownikiem systemu operacyjnego dostęp na czas sesji.

**Używaj najwęższego zakresu zatwierdzenia odpowiedniego dla zadania.** Agent administracji systemowej powinien działać w dedykowanym terminalu lub piaskownicy. Nie zatwierdzaj każdego procesu, jeśli wystarczy jedna sesja terminala.

Sesja zatwierdzenia nie jest trwałym upoważnieniem. 1Password rejestruje autoryzację na skonfigurowany okres lub do momentu zablokowania lub zamknięcia aplikacji. Gdy aplikacja jest zablokowana, agent nie przechowuje kluczy prywatnych do późniejszego użycia. Proces SSH Agenta kontynuuje działanie w tle, gdy odpowiednie ustawienie jest włączone, a 1Password jest zamknięty, ale nowe żądanie podpisu wymaga odblokowania 1Password.

Przewodnik [1Password SSH setup guide](https://www.1password.dev/ssh/get-started) pokazuje ogólny przebieg: wygenerowanie lub import klucza, publikacja klucza publicznego, włączenie SSH Agenta, konfiguracja klienta SSH, uruchomienie polecenia SSH lub Git oraz zatwierdzenie żądania. Dokładna ścieżka gniazda (socket) różni się w zależności od systemu operacyjnego. Używaj instrukcji dla bieżącej platformy zamiast kopiowania ścieżki z innej maszyny.

Aplikacja 1Password musi być odblokowana, zanim nowe żądanie podpisu zakończy się sukcesem. Proces agenta może kontynuować działanie w tle, gdy aplikacja jest zamknięta. Zablokowana aplikacja nie udostępnia materiału klucza prywatnego do podpisu.

## Klucze publiczne i Bitbucket

Przewodnik [1Password key-management guide](https://www.1password.dev/ssh/manage-keys) dokumentuje elementy SSH Key, generowanie kluczy, import kluczy, klucze publiczne, odciski palców oraz klucze prywatne. Przykład CLI używa `op item create --category ssh` do utworzenia elementu SSH Key. 1Password CLI domyślnie generuje klucz Ed25519 dla tego przykładu i maskuje klucz prywatny w swoim wyjściu.

Bitbucket Cloud używa standardowego workflow linii komend Git i OpenSSH. Jego [command-line guide](https://support.atlassian.com/bitbucket-cloud/docs/find-the-command-line/) opisuje operacje Git z lokalnego repozytorium. Jego [SSH configuration guide](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) wymienia formy zdalnych SSH i obsługiwane formaty kluczy publicznych.

**Traktuj Bitbucket jako konsumenta klucza publicznego.** Zarejestruj klucz publiczny lub odcisk palca przez zatwierdzone konto Bitbucket lub ustawienie repozytorium. Zachowaj klucz prywatny w 1Password. Klient Git prosi SSH Agenta o podpis. Klient nie odczytuje pliku klucza prywatnego.

W zakresie klucza dostępowego Bitbucket, ścieżki rejestracji i testu Git tylko do odczytu, zobacz [Bitbucket Cloud SSH Keys and Git CLI: Read-Only Access for AI Agents](/articles/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation/).

Dokumentacja Bitbucket nazywa to workflow Git CLI. Ten artykuł nie zakłada istnienia osobnego serwera MCP Bitbucket ani produktu o nazwie Bitbucket CLI. Specyficzny dla Bitbucket CLI wymaga własnej aktualnej dokumentacji i własnej przeglądu uprawnień.

## Granica między Agentem a MCP

Przy przeglądaniu nowego serwera stosuj bieżącą [specyfikację MCP](https://modelcontextprotocol.io/specification/2026-07-28).

Adres URL specyfikacji z 2025-06-18 w następnym akapicie tła to wersja historyczna. Do nowych przeglądów używaj specyfikacji z 2026-07-28.

[Standard MCP](https://modelcontextprotocol.io/specification/2025-06-18) standaryzuje połączenia między aplikacją LLM, klientem łączącym a serwerem. Serwer oferuje narzędzia, zasoby lub podpowiedzi. Specyfikacja stanowi również, że hosty muszą uzyskać zgodę użytkownika przed udostępnieniem danych lub wywołaniem narzędzi.

**Sam MCP nie przyznaje uprawnień.** Narzędzie MCP nadal działa w ramach uprawnień procesu serwera, użytkownika systemu operacyjnego, ścieżki sieciowej, konta w chmurze oraz skonfigurowanych poświadczeń. Opis narzędzia nie jest polityką autoryzacji.

[Dokumentacja 1Password Security for AI](https://www.1password.dev/security-for-ai) opisuje serwer MCP Environments oraz bezpieczne wzorce konfiguracji MCP. Ta sama strona opisuje ładowanie wartości konfiguracji MCP z 1Password w czasie wykonania. Te strony nie definiują ogólnego produktu MCP dla kluczy SSH 1Password ani uniwersalnego przepływu pracy SSH dla każdego klienta agenta.

Używaj MCP jako wąskiej powierzchni sterowania:

- **Narzędzia odczytu:** Inspekcja statusu usługi, metadanych repozytorium lub zatwierdzonych dzienników.
- **Narzędzia planowania:** Przygotowanie polecenia lub rekordu zmian bez wykonywania polecenia.
- **Narzędzia zatwierdzania:** Żądanie decyzji człowieka przed zdalnym zapisem.
- **Narzędzia zapisu:** Pozostaw nieaktywne, dopóki cel, polecenie, zakres i plan wycofania nie będą jednoznacznie określone.

Agent powinien otrzymywać odniesienia, metadane i wyniki operacji. **Agent nie powinien otrzymywać tekstu klucza prywatnego, zrzutu wszystkich elementów sejfu ani nieograniczonej powłoki.**

## Bezpieczna pierwsza polityka

Zacznij od pisemnej polityki przed włączeniem agenta. Trzymaj politykę blisko konfiguracji MCP, ale nie umieszczaj w pliku poświadczeń.

```yaml
agent_policy:
  purpose: "Read-only repository and system inspection"
  identities:
    interactive_ssh: "1Password SSH Agent with per-terminal consent"
    unattended_jobs: "Dedicated service account with one narrow vault"
  allowed:
    - "Read repository metadata through Git"
    - "Read approved service status and logs"
    - "Run one synthetic SSH connectivity check"
  approval_required:
    - "Any remote write"
    - "Any package, firewall, clock, or service change"
    - "Any new host-key acceptance"
    - "Any private-key export"
  denied:
    - "Read or print private-key fields"
    - "List every vault or every item"
    - "Write tokens or secrets to shell profiles"
    - "Run arbitrary commands from tool output"
  rollback:
    - "Revoke the service account"
    - "Remove the public key from the target"
    - "Disable the MCP server entry"
    - "Lock 1Password and end the agent session"
```

Ta polityka jest przykładem, a nie formatem konfiguracji 1Password. Przechowuj rzeczywistą politykę w warstwie sterowania używanej przez klienta agenta. Przeglądaj każde narzędzie w odniesieniu do polityki przed włączeniem danego narzędzia.

## Konta usługowe i odniesienia do sekretów

**Konto usługowe** nadaje zautomatyzowanemu procesowi własną tożsamość. [Przewodnik po skryptach CLI 1Password](https://www.1password.dev/cli/secrets-scripts) zaleca konta usługowe dla dostępu z minimalnymi uprawnieniami do wybranych sejfów. Oddziela to zadanie bezobsługowe od SSO, MFA, inwentarza sejfów i codziennego konta osoby.

**Sekretna referencja** naznacza wartość bez umieszczania jej w kodzie źródłowym. [Dokumentacja CLI 1Password](https://www.1password.dev/cli/reference) używa formy `op://vault/item/field`. Referencja jest bezpieczna do przechowywania tylko wtedy, gdy otaczający proces ma nadal wąski dostęp. Referencja nie omija polityki bezpieczeństwa.

Używaj `op read`, gdy jedna komenda potrzebuje jednej wartości. Używaj `op run`, gdy proces potomny potrzebuje kontrolowanego zestawu wartości czasu wykonania. Używaj `op item create`, gdy nowy element SSH Key musi istnieć w zatwierdzonym sejfie.

Nie myl wstrzykiwania wartości w czasie wykonania z ochroną klucza prywatnego. Token API przekazywany jako zmienna środowiskowa jest nadal widoczny dla procesu potomnego. Klucz prywatny przekazywany przez zmienną środowiskową jest gorszy, ponieważ wartość rozszerza ekspozycję na inspekcję procesu, raporty o awariach, wyjście debugowania, śledzenie powłoki oraz przypadkowe logowanie.

**Preferuj referencję w kodzie źródłowym i wartość w czasie wykonania w najmniejszym możliwym procesie.** Utrzymuj proces krótkotrwały. Wyłącz śledzenie powłoki. Nie wypisuj środowiska. Usuń pliki tymczasowe po nieudanej egzekucji.

## Bezpieczny początkowy przepływ pracy

Poniższa sekwencja oddziela rejestrację klucza publicznego, interaktywny SSH, wykrywanie MCP oraz projektowanie bezobsługowe.

### 1. Zdefiniuj cel

Zapisz klasę celu, zdalne konto, intended repository lub komendę, źródło klucza hosta, właściciela zatwierdzenia oraz akcję wycofania. Używaj syntetycznego rekordu podczas pierwszego ćwiczenia.

```text
target_class: test-repository
remote_account: git
operation: read-only connectivity check
host_key_source: approved administrator record
approval_owner: named operator
rollback: remove public key and revoke test identity
```

**Oczekiwany wynik, nietestowany:** Rekord identyfikuje jeden cel i jedną operację. Rekord nie zawiera nazwy hosta, adresu IP, tokenu, klucza prywatnego ani danych osobowych.

### 2. Utwórz lub wybierz element SSH Key

Oficjalny [przewodnik po kluczach SSH 1Password](https://www.1password.dev/ssh/manage-keys) dokumentuje wzorzec tworzenia za pomocą CLI. Poniższa komenda używa syntetycznego tytułu i nazwanego sejfu testowego.

```bash
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
```

**Oczekiwane wyjście, nietestowane:** 1Password tworzy element SSH Key w nazwanym sejfie testowym i maskuje klucz prywatny w wyjściu terminala. Komenda zmienia stan 1Password. Dokładne, czytelne wyjście zależy od wersji CLI i stanu logowania.

Zapisz zwrócony identyfikator elementu w rekordzie testowym, nie kopiując pola klucza prywatnego. Używaj identyfikatora lub dokładnego tytułu elementu do późniejszych odczytów konkretnych pól dopiero po potwierdzeniu schematu elementu.

Nie przekierowuj tego wyjścia do wspólnego dziennika. Zapisuj tylko identyfikator elementu, odcisk palca klucza publicznego i rekord zatwierdzenia, gdy lokalna procedura obsługuje bezpieczne, strukturalne wyjście.

### 3. Obsłuż klucz publiczny

Otwórz element Klucz SSH w 1Password i użyj akcji Kopiuj klucz publiczny. Używaj odwołania do konkretnego pola dopiero po potwierdzeniu etykiety pola klucza publicznego w swoim koncie. Nie wyodrębniaj całego elementu.

```bash
PUBLIC_KEY_REF="op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
op read "$PUBLIC_KEY_REF"
```

**Oczekiwany wynik, nieprzetestowany:** Jedna syntetyczna linia klucza publicznego OpenSSH lub wartość klucza publicznego z potwierdzonego pola. Nazwa pola zastępczego powyżej nie jest gwarancją etykiety pola w Twoim elemencie.

Zarejestruj klucz publiczny w zatwierdzonym koncie Bitbucket, repozytorium Bitbucket lub koncie zdalnym. Nigdy nie wklejaj odpowiadającego klucza prywatnego do Bitbucket. [Przewodnik SSH Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) zaleca również zapisanie klucza hosta Bitbucket przed pierwszym połączeniem.

W przypadku Bitbucket pobierz opublikowany rekord klucza hosta i porównaj go z niezależną, zaufaną kopią przed dodaniem linii do `~/.ssh/known_hosts`. Używaj ścisłej weryfikacji hosta po pomyślnym porównaniu. Nie akceptuj zmienionego klucza hosta podczas działania agenta.

### 4. Włącz interaktywny SSH

Włącz agenta SSH 1Password w aplikacji desktopowej. Skonfiguruj OpenSSH z użyciem wartości `IdentityAgent` lub `SSH_AUTH_SOCK` specyficznej dla platformy z [oficjalnego przewodnika konfiguracji](https://www.1password.dev/ssh/get-started). Ogranicz pierwszy test do jednego repozytorium lub jednego konta spoza środowiska produkcyjnego.

Na systemach macOS lub Linux ustaw gniazdo zgodnie z przewodnikiem konfiguracji dla danej platformy i uruchom `ssh-add -l`. Na systemie Windows użyj obsługiwanej konfiguracji nazwanej rury i zweryfikuj dostępne klucze przez interfejs agenta SSH 1Password lub udokumentowany test SSH dla Windows. Nie przedstawiaj `ssh-add -l` jako polecenia weryfikacyjnego działającego między platformami.

Wyłącznie na systemach macOS lub Linux:

```bash
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**Oczekiwany wynik, nieprzetestowany:** Na systemach macOS lub Linux `ssh-add -l` wyświetla odciski palców z aktywnego agenta. Na systemie Windows użyj udokumentowanego testu nazwanej rury lub interfejsu agenta SSH 1Password. Pomyślny odczyt Git zwraca odwołanie do commitu. Miejsce zastępcze repozytorium powyżej wymaga podmiany w kontrolowanym teście.

Polecenie używa miejsca zastępczego repozytorium. Podmień miejsce zastępcze wyłącznie w kontrolowanym teście. **Nie zatwierdzaj monitu dla celu lub procesu, którego się nie spodziewałeś.**

### 5. Dodaj MCP po działaniu ścieżki SSH

Najpierw zweryfikuj klienta SSH i cel bez MCP. Następnie dodaj jeden serwer MCP tylko do odczytu lub lokalny łącznik. Udostępnij agentowi narzędzie takie jak `read_status` lub `prepare_command`. Nie zaczynaj od ogólnego narzędzia powłoki.

Konfiguracja MCP powinna odwoływać się do wartości uruchomieniowych za pomocą mechanizmu zmiennych środowiskowych wspieranego przez klienta. [Przewodnik 1Password dotyczący bezpieczeństwa AI](https://www.1password.dev/security-for-ai) opisuje zastępowanie tokenów konfiguracji MCP w postaci jawnej zmiennymi środowiskowymi ładowanymi z 1Password. **Zachowuj odwołanie lub nazwę zmiennej w konfiguracji. Wykluczaj rozwiązaną wartość z transkryptu agenta.**

Ten opis dotyczy projektu, a nie przetestowanej konfiguracji MCP. Żaden klient, serwer, transport, wersja ani zestaw testowy nie są tu zdefiniowane. Zweryfikuj jeden serwer tylko do odczytu w osobnym profilu testowym przed podłączeniem agenta do systemu produkcyjnego.

### 6. Zarejestruj wynik

Zarejestruj klasę docelową, nazwę narzędzia, decyzję o zatwierdzeniu, odcisk klucza publicznego, wynik polecenia oraz wynik sprzątania. Pomiń wartości poufne. Oznacz każdy wynik jako zaobserwowany lub oczekiwany.

**Oczekiwany wynik, przetestowany:** Agent odczytuje status, proponuje ograniczone polecenie, otrzymuje wyraźne zatwierdzenie dla żądania SSH, kończy operację tylko do odczytu i generuje rejestr bez tekstu klucza prywatnego.

## Syntetyczna sekwencja poleceń

Poniższa sekwencja pokazuje kolejność bez użycia rzeczywistej infrastruktury. Polecenia te są wyłącznie przykładami. Nie zostały wykonane podczas przygotowywania artykułu.

```bash
op --version
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
op read "op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
# macOS or Linux only
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**Oczekiwany wynik, przetestowany:**

```text
2.x.y
SSH Key item created. Private key: redacted
ssh-ed25519 AAAA<synthetic-public-key> synthetic-key-label
256 SHA256:<synthetic-fingerprint> synthetic-agent-admin-key (ED25519)
<synthetic-commit-id>        HEAD
```

Blok wyjściowy ma charakter poglądowy. Blok nie reprezentuje uruchomienia na koncie 1Password, Bitbucket, dostawcy Git ani zdalnym hoście. Rejestr produkcyjny powinien przechowywać wyłącznie zatwierdzone metadane oraz stan sukcesu lub porażki.

## Dostęp interaktywny versus nieprzerywany

| Tryb dostępu | Tożsamość | Ścieżka klucza prywatnego | Model zatwierdzania |
|---|---|---|---|
| **Interaktywny SSH** | Konto ludzkie przez 1Password SSH Agent | Klucz prywatny pozostaje w aplikacji 1Password | Człowiek zatwierdza proces, sesję terminala lub żądanie |
| **Zaplanowany odczyt** | Dedykowane konto usługi | `op run` dostarcza wąskie wartości uruchomieniowe | Polityka zadania i zakres konta usługi |
| **Zaplanowany SSH** | Dedykowana tożsamość automatyzacji | Eksport klucza pozostaje rozwiązaniem ostatecznym | Izolacja zadania, krótki czas życia, ograniczenie hosta i rotacja |
| **Zapis agenta** | Tożsamość ludzka lub specyficzna dla zadania | Zależy od zatwierdzonej integracji | Zatwierdzenie przez człowieka przed każdą zdefiniowaną zmianą |

*Nie planuj przepływu pracy wokół prompta interaktywnego agenta SSH. Użyj osobnego projektu automatyzacji lub zachowaj krok obsługiwany przez człowieka.*

Dla zadań uruchamianych bez nadzoru utwórz konto usługi z dostępem do jednej kasy lub małego zestawu elementów. Przypisz zadaniu jeden cel. Użyj dedykowanego repozytorium lub konta serwera. Dodaj weryfikację klucza hosta. Ustaw limit czasu wykonania. Rejestruj metadane akcji bez sekretów. Po teście zrotuj lub odwołaż tożsamość.

Jeśli zadanie uruchamiane bez nadzoru naprawdę wymaga klucza prywatnego SSH, użyj dedykowanego klucza automatyzacji z wąsko zakreślonym kontem zdalnym i udokumentowaną datą zakończenia. Pobieranie klucza prywatnego za pomocą `op read` nadal eksportuje materiał kluczowy przez granicę procesu. Taki projekt ma większy zasięg skutków niż 1Password SSH Agent. Gdy docelowy system to obsługuje, preferuj tożsamość platformy, usługę wdrożeniową lub inną tożsamość obciążenia.

## Dlaczego jawne zmienne środowiskowe zwiększają ryzyko

Zmienne środowiskowe trzymają sekrety poza plikami źródłowymi, ale nie czynią ich niewidocznymi. Proces potomny odczytuje swoje środowisko. Inspekcja procesu, obsłużniki awarii, wyjście debugowania, śledzenie powłoki oraz skopiowane zapisy poleceń mogą ujawnić wartości.

1Password dokumentuje `op run` jako metodę uruchomieniową do ładowania referencji do procesu potomnego. Używaj `op run` dla wartości, których proces naprawdę potrzebuje. Utrzymuj proces potomny krótkotrwały i ogranicz jego polecenie. Nie przekazywaj klucza prywatnego przez `SSH_PRIVATE_KEY`, `KEY` ani zmienną podobnego typu, gdy SSH Agent eliminuje potrzebę eksportu.

Bezpieczniejsza kolejność to:

1. **Użyj SSH Agent** do interaktywnego SSH.
2. **Użyj rejestracji klucza publicznego** dla Bitbucket lub konta zdalnego.
3. **Użyj `op run`** dla wąsko zakreślonego procesu potomnego uruchamianego bez nadzoru.
4. **Użyj `op read`** dla jednej wartości, gdy proces potomny nie potrzebuje pełnego środowiska.
5. **Eksportuj klucz prywatny** dopiero po pisemnym wyjątku, wąskim zakresie, planie sprzątania i planie rotacji.

## Tabela decyzyjna

| Potrzeba | Preferowana ścieżka | Powód do zatrzymania lub przebudowy |
|---|---|---|
| Użytkownik uruchamia Git przez SSH | 1Password SSH Agent | Zatrzymaj, jeśli prompt wskazuje nieoczekiwany proces lub klucz |
| Rejestracja klucza repozytorium | Odczyt lub automatyczne wypełnienie klucza publicznego | Nigdy nie kopiuj klucza prywatnego do usługi repozytorium |
| Agent odczytuje status usługi | Narzędzie MCP tylko do odczytu z zakresem na poziomie systemu operacyjnego | Zatrzymaj, jeśli narzędzie udostępnia nieograniczoną powłokę |
| Agent proponuje zmianę zdalną | Narzędzie planowania, po którym następuje zatwierdzenie przez człowieka | Zatrzymaj, jeśli cel, polecenie lub procedura wycofania są niejasne |
| Zadanie odczytuje jeden token API | Konto usługi oraz `op read` lub `op run` | Zatrzymaj, jeśli token trafia do kodu źródłowego, logów lub globalnego profilu |
| Zadanie potrzebuje dostępu SSH | Tożsamość obciążenia (workload identity) lub dedykowany klucz automatyzacji | Zatrzymaj, jeśli zadanie wymaga osobistego klucza lub szerokiego konta |
| Konfiguracja MCP potrzebuje tokenu | Odwołanie do czasu wykonania ładowane przez wspierany klient | Zatrzymaj, jeśli token w postaci jawnej zostanie zapisany w konfiguracji |

## Obsługa awarii

**Nieoczekiwany prompt zgody SSH:** Odrzuć prompt. Sprawdź nazwę procesu, sesję terminala, odcisk palca klucza, cel repozytorium oraz klucz hosta. Przeglądaj konfigurację klienta SSH przed ponowieniem próby.

**Brak gniazda SSH Agent:** Upewnij się, że aplikacja desktopowa 1Password jest zainstalowana za pomocą wspieranego sposobu, że SSH Agent jest włączony oraz że klient używa gniazda specyficznego dla danej platformy. Oficjalna strona SSH Agent](https://www.1password.dev/ssh/agent) zawiera wymagania dotyczące systemów operacyjnych oraz linki do konfiguracji gniazd.

**Uwierzytelnianie kluczem publicznym nie powiodło się:** Sprawdź wybrany klucz publiczny, konto zdalne, uprawnienia do repozytorium, klucz hosta oraz konfigurację SSH. Użyj porównania odcisków palców publicznych. Nie rozwiązuj błędu przez eksportowanie niezwiązanego klucza prywatnego.

**`op read` odmawia dostępu:** Sprawdź zakres skrzynki konta usługi, identyfikator elementu, odwołanie do pola, stan logowania oraz status elementu. Ogranicz odwołanie do jednego zatwierdzonego elementu. Nie rozszerzaj przyznania dostępu do skrzynki jako pierwszej reakcji.

**`op run` ujawnia wartość:** Zatrzymaj zadanie. Zachowaj jedynie minimalny zapis incydentu. Usuń skopiowane logi i pliki tymczasowe zgodnie z procedurą retencji. Zrotuj dotknięty sekret lub klucz. Przeglądaj śledzenie powłoki, inspekcję procesów, raporty o awariach oraz retencję transkryptów MCP.

**Narzędzie MCP zachowuje się nieoczekiwanie:** Traktuj dane wyjściowe narzędzia jako niezaufane. Zatrzymaj się przed wykonaniem poleceń sugerowanych przez dane wyjściowe. Przejrzyj kod źródłowy serwera, konfigurację, uprawnienia i transport. Host MCP musi uzyskać zgodę użytkownika. Specyfikacja dostarcza również wytycznych dla implementatorów dotyczących zgody i kontroli dostępu, ale protokół nie zastępuje Twojej weryfikacji.

## Wycofanie i usuwanie

Wycofanie rozpoczyna się od usunięcia dostępu, a nie od usuwania plików.

1. **Zatrzymaj agenta lub zaplanowane zadanie.** Wyłącz wpis serwera MCP lub odłącz klienta.
2. **Zablokuj 1Password.** Zakończ interaktywną sesję autoryzacji SSH.
3. **Usuń klucz publiczny.** Usuń klucz testowy z Bitbucket, repozytorium lub konta zdalnego.
4. **Wycofaj konto usługi.** Usuń jego dostęp do sejfów i unieważnij jego token.
5. **Usuń element testowego klucza SSH** po potwierdzeniu, że żaden zatwierdzony proces nie używa tego elementu.
6. **Usuń tymczasową konfigurację.** Usuń odniesienia testowe, lokalne nadpisanie gniazd (socket) i wygenerowane dzienniki.
7. **Przejrzyj dowody.** Upewnij się, że rekord wycofania nie zawiera klucza prywatnego, tokena ani zrzutu środowiska.

*Usunięcie lokalnego pliku nie wycofuje klucza publicznego, konta usługi, tokena w pamięci podręcznej ani autoryzacji zdalnej. Usuń każde przyznanie uprawnień w jego źródle.*

## Rozwiązywanie problemów

### Agent prosi o klucz przy każdym poleceniu

Sprawdź wybrany zakres autoryzacji. Zatwierdzanie dla każdego żądania jest bardziej restrykcyjne. Sesja terminala lub aplikacji mogła się zakończyć. 1Password prosi również ponownie po zdarzeniu blokady lub zamknięcia.

### Agent widzi klucz prywatny w swoim transkrypcie

Zatrzymaj proces i zrotuj klucz. Przejrzyj odpowiedź serwera MCP, polecenie powłoki, dziennik debugowania i opakowanie narzędzia. Zamień odczyty klucza prywatnego na użycie SSH Agent dla zadań interaktywnych. Dla zadań zaplanowanych zamień osobisty klucz na dedykowaną tożsamość i udokumentowany wyjątek.

### Lista kluczy zawiera zbyt wiele tożsamości

SSH Agent 1Password ujawnia kwalifikujące się klucze z jego skonfigurowanych sejfów. Użyj skonfigurowanego agenta z ograniczonym zakresem lub konfiguracji SSH specyficznej dla hosta. [Dokumentacja agenta](https://www.1password.dev/ssh/agent) również odnotowuje limit sześciu kluczy serwera OpenSSH.

### Polecenie działa ręcznie, ale nie powiada się w zadaniu

Porównaj tożsamość, zakres sejfu, środowisko, dane klucza hosta, katalog roboczy i założenia dotyczące zatwierdzenia. Interaktywna sesja 1Password zawiera zgodę człowieka. Zaplanowane zadanie jej nie zawiera. Zaprojektuj zadanie jako osobny tryb dostępu.

### Serwer MCP jest połączony, ale zadanie nie powiada się

Połączenie nie dowodzi upoważnienia. Sprawdź wykrywanie narzędzi, dane uwierzytelniające serwera, zgodę klienta, uprawnienia systemu operacyjnego, dostęp do sieci oraz uprawnienia po stronie docelowej w osobnych krokach. Zachowaj pierwszy test tylko do odczytu.

## Kolejne kroki

Używaj bieżącej specyfikacji MCP z 2026-07-28 dla nowych zatwierdzeń. Każdy link do specyfikacji z 2025-06-18 w tym artykule stanowi historyczne tło.

Zacznij od jednego syntetycznego repozytorium i jednego narzędzia MCP tylko do odczytu. Zapisz każdy oczekiwany wynik jako „nieprzetestowany”, dopóki kontrolowane środowisko nie dostarczy dowodów. Następnie powtórz przepływ pracy z celem niedotyczącym produkcji, nazwanym operatorem, zweryfikowanym kluczem hosta oraz pisemnym zapisem procedury cofnięcia.

Przeczytaj [referencję CLI 1Password](https://www.1password.dev/cli/reference), aby poznać bieżące flagi poleceń. Przeczytaj [Ładowanie sekretów do skryptów](https://www.1password.dev/cli/secrets-scripts) przed tworzeniem automatyzacji konta usługi. Przeczytaj [specyfikację MCP](https://modelcontextprotocol.io/specification/2026-07-28) przed zatwierdzeniem narzędzi z nowego serwera.

**Zachowaj interaktywny SSH zatwierdzany przez człowieka. Zachowaj dostęp bez nadzoru osobno. Zachowaj klucze prywatne nieczytane, o ile cel obsługuje uwierzytelnianie oparte na agencie.**
