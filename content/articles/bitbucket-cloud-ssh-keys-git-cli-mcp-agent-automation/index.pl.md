---
title: "Klucze SSH Bitbucket Cloud: dostęp Git tylko do odczytu dla agentów AI"
date: 2026-10-11
lastmod: 2026-11-13
toc: true
draft: false
description: "Skonfiguruj klucze SSH Bitbucket Cloud, dostęp Git CLI, tokeny REST API, 1Password i narzędzia MCP dla procesów agentów AI działających tylko do odczytu."
genre: ["Bezpieczeństwo chmury", "Narzędzia dla programistów", "Administracja systemami"]
tags: ["Bitbucket Cloud", "klucze SSH Bitbucket", "klucze dostępu do repozytorium", "klucze dostępu do projektu", "klucze dostępu do obszaru roboczego", "Git CLI", "Bitbucket CLI", "1Password CLI", "1Password SSH Agent", "MCP", "Model Context Protocol", "REST API", "zakresy tokenów API", "uprawnienia agentów", "automatyzacja tylko do odczytu", "klucze hosta SSH"]
cover: "/img/cover/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation.webp"
coverAlt: "Przepływ pracy w terminalu łączący dostęp Bitbucket Cloud Git, ograniczone klucze SSH, 1Password, odczyty REST API i narzędzia MCP"
coverCaption: ""
---

**Ograniczony przepływ pracy agenta oddziela odczyty repozytorium, odczyty API, obsługę sekretów i zdalne zapisy.** Używaj Git przez Secure Shell (SSH) do dostępu do źródeł, klucza dostępu Bitbucket tylko do odczytu do automatycznego pobierania, REST API do metadanych i serwera Model Context Protocol (MCP) do zatwierdzonych narzędzi. Przechowuj klucze prywatne i tokeny API w 1Password. Zdalne zapisy pozostaw za etapem zatwierdzenia przez człowieka.

<!--more-->

## Najważniejsze wnioski

- **Domyślnie tylko do odczytu:** używaj klucza dostępu do repozytorium lub projektu przy pobieraniu przez agenta. Żaden z nich nie umożliwia push.
- **Tożsamość osobista:** używaj osobistego klucza SSH do interaktywnej pracy powiązanej z kontem użytkownika.
- **Przechowywanie sekretów:** używaj 1Password SSH Agent, aby Git wykonywał zatwierdzone podpisywanie bez odczytywania klucza prywatnego.
- **Znaczenie CLI:** traktuj `git`, `curl` i mały, sprawdzony wrapper API jako praktyczne narzędzia wiersza poleceń Bitbucket.
- **Granica MCP:** udostępniaj wąskie narzędzia odczytu. Wyłącz narzędzia zapisu lub umieść je za osobnym procesem zatwierdzania.
- **Bramka zapisu:** pozwól agentowi sprawdzić, porównać i przygotować zmianę. Wymagaj zatwierdzenia przez człowieka przed push, pull requestem, scaleniem lub aktualizacją ustawień.

## Zanim zaczniesz

**Wymagania:** dostęp do Bitbucket Cloud, Git, klient OpenSSH, 1Password 8, 1Password CLI, zalogowane CLI lub zatwierdzone konto usługi oraz host MCP z mechanizmem zatwierdzania serwerów. Zarezerwuj 45 minut. Poziom trudności: średni.

Na początku użyj testowego repozytorium. Zastąp wszystkie symbole zastępcze w przykładach. Poniższe polecenia to nieprzetestowane przykłady. Nie odnoszą się do aktywnego konta ani repozytorium Bitbucket.

**Wersje:** ten artykuł zawiera wskazówki projektowe, a nie instrukcję przypisaną do konkretnych wersji. Przed testem sprawdź zainstalowane wersje Git, OpenSSH, 1Password CLI, Teamwork Graph CLI, hosta MCP i serwera MCP. Skonfiguruj 1Password SSH Agent dla bieżącego systemu operacyjnego przed użyciem `ssh-add -l`.

**Nie umieszczaj poświadczeń w powłokach, logach, adresach URL, zdalnych adresach Git ani plikach źródłowych.** Używaj symboli zastępczych, takich jak `<workspace>`, `<repository>`, `<api-token>` i `<socket-path>`. Nie wklejaj prawdziwego klucza prywatnego do transkrypcji terminala.

## Wybierz granicę dostępu

Bitbucket Cloud obsługuje klucze dostępu na poziomie repozytorium, projektu i obszaru roboczego. Zakres określa wpływ skopiowanego klucza. [Oficjalne porównanie kluczy dostępu](https://support.atlassian.com/bitbucket-cloud/kb/difference-between-repository-project-and-workspace-access-keys/) bezpośrednio opisuje różnice w uprawnieniach.

| Sposób dostępu | Zakres | Możliwość zapisu | Dobre zastosowanie |
|---|---|---:|---|
| **Klucz dostępu do repozytorium** | Jedno repozytorium | Nie | Domyślne pobieranie przez agenta |
| **Klucz dostępu do projektu** | Repozytoria w jednym projekcie | Nie | Zadania tylko do odczytu w małej grupie repozytoriów |
| **Klucz dostępu do obszaru roboczego** | Repozytoria w jednym obszarze roboczym | Tak | Kontrolowana automatyzacja usługi z osobnym planem zapisu |
| **Osobisty klucz SSH** | Repozytoria dostępne dla jednego użytkownika | Zgodnie z kontem użytkownika | Interaktywna administracja |
| **Token API** | Zakresy API użytkownika i zasięg konta | Zależnie od zakresów | Odczyty REST API lub tymczasowe zadanie zapisu |

**Zacznij od najmniejszej użytecznej granicy.** Wybierz klucz repozytorium, gdy wystarczy jedno repozytorium. Wybierz klucz projektu, gdy kilka repozytoriów należy do jednego projektu i wystarczy dostęp tylko do odczytu. Traktuj klucz obszaru roboczego jako tożsamość z prawami zapisu, a nie wygodną opcję domyślną.

Utwórz i zarejestruj klucz o najmniejszym zakresie w odpowiedniej sekcji ustawień Bitbucket:

1. Otwórz Repository settings, Access keys i Add key dla jednego repozytorium. Wklej klucz publiczny i pozostaw klucz tylko do odczytu.
2. Otwórz Project settings, Access keys i Add key, gdy kilka repozytoriów wymaga wspólnej tożsamości tylko do odczytu na poziomie projektu.
3. Używaj klucza obszaru roboczego tylko we współdzielonym obszarze roboczym z zatwierdzonym projektem zapisu. Osobiste obszary robocze nie oferują tej samej ścieżki na poziomie obszaru.
4. Zapisz etykietę klucza, zakres, odcisk klucza publicznego, właściciela i datę rotacji. Klucz prywatny przechowuj w 1Password.

Po rejestracji wykonaj dokładny test połączenia tylko do odczytu:

```bash
git ls-remote git@bitbucket.org:<workspace>/<repository>.git HEAD
```

**Oczekiwany wynik:** jedno odwołanie do commita `HEAD`. Przykład nieprzetestowany. Sukces dowodzi, że jedna dozwolona tożsamość SSH dotarła do wskazanego repozytorium. Nie dowodzi, że wybrano zarejestrowany klucz ani że istnieje dostęp do zapisu. Powtórz test po konfiguracji jednego klucza na repozytorium.

Informacje o przechowywaniu kluczy prywatnych i zgodzie 1Password SSH Agent znajdziesz w [1Password CLI i SSH Agent: bezpieczne klucze SSH dla agentów AI](/articles/1password-cli-ssh-keys-mcp-agent-administration/).

## Właściwe znaczenie „Bitbucket CLI”

Określenie **Bitbucket CLI** często łączy trzy różne interfejsy. Rozdziel je.

- **Git CLI:** `git clone` i `git fetch` przesyłają dane repozytorium przez SSH lub HTTPS. `git diff` porównuje pliki lokalne lub rewizje.
- **Klient REST:** `curl` lub sprawdzony wrapper wywołuje interfejs Bitbucket Cloud Representational State Transfer (REST) API. API to programowy interfejs do żądania danych lub działań. [Dokumentacja Bitbucket Cloud REST API](https://developer.atlassian.com/cloud/bitbucket/rest/) wymienia zasoby repozytoriów, źródeł, gałęzi, pull requestów, pipeline’ów i statusów.
- **Atlassian CLI:** `acli` to oficjalny wiersz poleceń Atlassian. [Wprowadzenie](https://developer.atlassian.com/cloud/acli/guides/introduction/) opisuje produkt, a [referencja poleceń](https://developer.atlassian.com/cloud/acli/reference/commands/) wymienia obszary `admin`, `jira`, `feedback` i `rovodev`. Referencja nie dokumentuje poleceń Bitbucket Cloud.

**Oficjalna referencja poleceń `acli` Atlassian nie dokumentuje poleceń Bitbucket Cloud.** Nie wymyślaj poleceń, takich jak `acli bitbucket clone`. Używaj Git do operacji Git, a REST API do danych Bitbucket Cloud.

### Opcjonalny Teamwork Graph CLI

**Atlassian udostępnia również Teamwork Graph CLI, czyli `twg`.** Jego [omówienie](https://developer.atlassian.com/cloud/twg-cli/) i [katalog poleceń](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/commands/commands-catalog/) opisują grupy poleceń Bitbucket. Polecenie konfiguracji to:

```bash
twg setup
```

Polecenie konfiguracji zmienia lokalny stan uwierzytelniania. Postępuj zgodnie z monitami zainstalowanej wersji dotyczącymi opcjonalnej konfiguracji tokenu Bitbucket. Ścieżka tokenu Bitbucket w CLI jest odrębna od Atlassian OAuth. Składnię poleceń dopasuj do zainstalowanej wersji i aktualnego katalogu. Używaj osobnego profilu, ograniczonego tokenu, sprawdzonych zainstalowanych umiejętności i zatwierdzenia przez człowieka dla poleceń modyfikujących.

**Oczekiwany wynik, nieprzetestowany:** odizolowany profil otrzymuje ustawienia uwierzytelniania Bitbucket. Zapisz poprzedni stan profilu przed konfiguracją. Podczas wycofywania zmian usuń zapisane poświadczenie zgodnie z udokumentowaną procedurą wylogowania lub usuwania konfiguracji dla zainstalowanej wersji.

Jeśli projekt strony trzeciej nazywa się Bitbucket CLI, sprawdź jego kod źródłowy, proces wydania, sumy kontrolne, mechanizm aktualizacji, sposób uwierzytelniania, wymagane zakresy, miejsca docelowe sieci, obsługę logów i polecenia zapisu. Znana nazwa pliku binarnego nie potwierdza wsparcia dostawcy ani bezpiecznych uprawnień.

## Zarządzaj kluczami SSH w 1Password

[1Password SSH Agent](https://www.1password.dev/ssh/agent) udostępnia klientom Git i SSH klucze SSH przechowywane w 1Password. Klient wykonuje zatwierdzone żądanie podpisu. Klucz prywatny pozostaje w aplikacji 1Password, która prosi o zgodę, zanim zatwierdzony klient użyje klucza.

[Referencja 1Password CLI](https://www.1password.dev/cli/reference) służy do czegoś innego. Używaj `op` do kontrolowanego dostępu do elementów, tokenów API, kont usług i konfiguracji automatyzacji. Do podpisywania SSH używaj SSH Agent. Nie eksportuj klucza prywatnego do pliku tymczasowego tylko po to, by uprościć przepływ agenta.

Sprawdź lokalny stan CLI i agenta za pomocą poleceń tylko do odczytu:

```bash
op --version
ssh-add -l
```

**Oczekiwany wynik:** wersja 1Password CLI i co najmniej jeden odcisk klucza publicznego z aktywnego agenta. Przykład nieprzetestowany. Pusty wynik `ssh-add -l` oznacza, że przez wybrane gniazdo agenta nie jest dostępny żaden klucz.

Aby utworzyć nowy klucz, dodaj element Ed25519 SSH Key w 1Password albo zaimportuj klucz wygenerowany zaufanym lokalnym procesem. Nadaj mu etykietę opisującą cel, zakres i datę rotacji. Do Bitbucket Cloud dodaj wyłącznie klucz publiczny. [Instrukcja klucza dostępu do repozytorium w systemie Linux](https://support.atlassian.com/bitbucket-cloud/docs/set-up-repository-access-keys-on-linux/) opisuje ustawienia repozytorium i ograniczenie do odczytu.

## Najpierw zweryfikuj klucz hosta Bitbucket

Uwierzytelnienie użytkownika SSH nie potwierdza tożsamości serwera. Klient musi zweryfikować klucz hosta Bitbucket Cloud przed wysłaniem żądania uwierzytelnienia. [Przewodnik Atlassian o SSH i weryfikacji dwuetapowej](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification/) wymienia publiczne klucze hosta i podaje oficjalny endpoint do pobierania wpisów known_hosts.

Pobierz publiczne dane klucza hosta do porównania:

```bash
curl --fail --silent --show-error https://bitbucket.org/site/ssh
```

**Oczekiwany wynik:** wiersze OpenSSH `known_hosts` dla `bitbucket.org`. Przykład nieprzetestowany. Przed dodaniem wiersza do `~/.ssh/known_hosts` porównaj zwrócony klucz lub odcisk z niezależną zaufaną kopią.

Po dodaniu zatwierdzonego wpisu włącz ścisłą kontrolę hosta:

```sshconfig
Host bitbucket.org
    StrictHostKeyChecking yes
    UserKnownHostsFile ~/.ssh/known_hosts
```

**Nie akceptuj zmienionego klucza hosta podczas pracy agenta.** Zatrzymaj działanie, zweryfikuj aktualny rejestr kluczy hosta Bitbucket Cloud i sprawdź lokalny wpis `known_hosts`. Automatyczna akceptacja usuwa granicę bezpieczeństwa klucza.

## Wybierz jeden klucz na repozytorium

Na jednym urządzeniu często znajduje się kilka kluczy Bitbucket. Szeroki agent SSH oferuje wiele tożsamości podczas jednego połączenia. Serwer lub zasada z niskim limitem prób uwierzytelnienia może odrzucić właściwy klucz po wcześniejszych nieudanych próbach.

[Przewodnik Atlassian o wielu kluczach dostępu do repozytoriów](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) używa `core.sshCommand` w pliku konfiguracji Git repozytorium oraz `includeIf` w globalnej konfiguracji Git. Zastosuj ten sam wzorzec, używając jednego klucza na repozytorium.

Przenośny przykład oparty na plikach:

```ini
# .gitconfig wewnątrz jednego lokalnego repozytorium
[core]
    sshCommand = ssh -o IdentitiesOnly=yes -i ~/.ssh/<repository-automation-key>
```

```ini
# ~/.gitconfig
[includeIf "gitdir:~/src/<repository>/"]
    path = ~/src/<repository>/.gitconfig
```

Powyższy blok jest wyjątkiem dla klucza prywatnego zapisanego w pliku, przeznaczonym dla dedykowanej tożsamości automatyzacji. Nie konfiguruje on 1Password SSH Agent. W przypadku 1Password SSH Agent ustaw platformową wartość `IdentityAgent` lub `SSH_AUTH_SOCK` z [instrukcji konfiguracji 1Password](https://www.1password.dev/ssh/get-started). Niektóre konfiguracje OpenSSH używają pliku `.pub` jako selektora tożsamości agenta. Przed użyciem sprawdź obsługę platformy. Konfiguracja oparta na pliku wymaga odpowiadającej mu ścieżki do klucza prywatnego. Nigdy nie przekazuj pliku `.pub` do polecenia oczekującego materiału klucza prywatnego i nie eksportuj osobistego klucza prywatnego.

Użyj jawnej konfiguracji repozytorium, gdy lokalny klon wymaga jednego klucza. Użyj `includeIf`, gdy katalog zawiera kilka klonów korzystających z tej samej granicy dostępu. [Przewodnik o wielu kluczach](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) pokazuje oba ustawienia w przepływie Bitbucket.

Klonuj przez Git z użyciem SSH:

```bash
git clone git@bitbucket.org:<workspace>/<repository>.git <local-directory>
```

**Oczekiwany wynik:** Git tworzy `<local-directory>` i pobiera repozytorium przez `bitbucket.org`. Przykład nieprzetestowany. Klucz dostępu do repozytorium umożliwia tylko klonowanie i pobieranie.

## Używaj tokenów API do ograniczonych odczytów REST

Do transportu Git używaj SSH. REST API służy do metadanych i operacji spoza transportu Git. [Przewodnik uprawnień tokenów API](https://support.atlassian.com/bitbucket-cloud/docs/api-token-permissions/) wymienia zakresy repozytorium, takie jak Read, Write, Admin i Delete. Repository Read odpowiada `read:repository:bitbucket` i nie obejmuje dostępu do pull requestów.

Do automatyzacji odczytu preferuj token dostępu Bitbucket na poziomie repozytorium lub projektu, jeśli dany endpoint go obsługuje. Token API użytkownika zachowuje szerszy zasięg konta. Token obszaru roboczego stosuj tylko wtedy, gdy zadanie wymaga szerszej granicy. Przed wyborem typu tokenu sprawdź [przewodnik po tokenach dostępu Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/).

Dla odczytu przez agenta zacznij od `read:repository:bitbucket`. Dodaj `read:pullrequest:bitbucket` tylko wtedy, gdy agent potrzebuje danych pull requestów. Zakresy obszaru roboczego lub pipeline dodaj dopiero wtedy, gdy zadanie określa endpoint i wynik. Zakresy zapisu i administracji wymagają odrębnej ścieżki zatwierdzania.

Utwórz każdy token API do jednego celu, ustaw datę wygaśnięcia, zapisz ją w rejestrze rotacji i wymień token przed tą datą. [Instrukcja Atlassian dotycząca tworzenia tokenu API](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/) wymaga nazwy, daty wygaśnięcia, wyboru aplikacji i zakresów. Token jest wyświetlany tylko raz po utworzeniu.

Przechowuj wartość w 1Password lub zarządzanym sekrecie środowiska wykonawczego. Nie umieszczaj jej w zdalnym adresie URL. Przekazuj token bearer przez zmienną środowiskową tylko do procesu wykonującego pojedynczy odczyt:

```bash
op run --env-file=/path/to/agent.env -- \
sh -c 'curl --fail --silent --show-error \
  --request GET \
  --url "https://api.bitbucket.org/2.0/repositories/<workspace>/<repository>" \
  --header "Authorization: Bearer ${BITBUCKET_API_TOKEN}" \
  --header "Accept: application/json"'
```

Trzymaj `/path/to/agent.env` poza repozytorium. Zapisz w pliku odwołanie, na przykład `BITBUCKET_API_TOKEN=op://synthetic-vault/synthetic-api-token/credential`. `op run` rozwiązuje odwołanie i udostępnia wartość procesowi curl na czas podprocesu. Nie uniemożliwia to procesowi odczytu ani logowania wartości środowiskowej. Nie zastępuj symbolu zastępczego rzeczywistym tokenem.

**Oczekiwany wynik:** metadane JSON wybranego repozytorium. Przykład nieprzetestowany. Symbol zastępczy nigdy nie może stać się prawdziwym tokenem w zatwierdzonym pliku ani logu.

W przypadku dłuższej automatyzacji pozwól 1Password wstrzyknąć sekret do środowiska procesu za pomocą obsługiwanej CLI lub przepływu konta usługi. Dopasuj czas życia tokenu do zadania. Unieważnij token, gdy zadanie zakończy się wcześniej lub zmieni się właściciel hosta.

## Ogranicz powierzchnię odczytu MCP

Podczas przeglądu nowego serwera korzystaj z aktualnej [specyfikacji MCP](https://modelcontextprotocol.io/specification/2026-07-28) i jej [zasad autoryzacji](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization). Serwery HTTP muszą sprawdzać odbiorcę tokenu i jasno obsługiwać odpowiedzi 401 oraz 403.

Host MCP uzyskuje zgodę użytkownika. Klient utrzymuje połączenie z jednym serwerem. Serwer udostępnia narzędzia, zasoby lub prompt’y. Traktuj każdy serwer jako niezaufany kod, dopóki nie sprawdzisz jego źródła, transportu, konta i uprawnień.

Adres specyfikacji 2025-06-18 w następnym akapicie dotyczy wersji historycznej. Przy nowych przeglądach używaj aktualnej specyfikacji 2026-07-28.

[Specyfikacja MCP](https://modelcontextprotocol.io/specification/2025-06-18) definiuje komunikację między hostem, klientem i serwerem MCP. Serwer udostępnia narzędzia, zasoby lub prompt’y w ramach protokołu. MCP standaryzuje format połączenia. Host, implementacja serwera, konto, zakres tokenu i zasady zatwierdzania nadal określają, do czego prowadzi wywołanie.

Używaj serwera MCP jako wąskiego adaptera dla Git i Bitbucket Cloud REST API.

Chroń adapter przed przekazywaniem tokenów, server-side request forgery (SSRF) i problemem confused deputy. SSRF pozwala serwerowi wysyłać żądania do niezamierzonych adresów. Problem confused deputy występuje, gdy serwer korzysta z szerszych uprawnień w imieniu wywołującego. Zabezpiecz go też przed złośliwymi serwerami lokalnymi, niebezpiecznymi przekierowaniami OAuth i nadmiernie dużymi wynikami danych źródłowych. Zdefiniuj dozwolone originy Bitbucket i identyfikatory repozytoriów. Uruchamiaj serwery lokalne w sandboxie z osobnym użytkownikiem systemu operacyjnego. Redaguj sekrety w wynikach narzędzi i logach.

Ta sekcja opisuje projekt, a nie przetestowaną konfigurację MCP. Nie przypisano tu klienta, serwera, transportu, wersji ani fixture. Zanim połączysz agenta z repozytorium produkcyjnym, zweryfikuj jeden serwer tylko do odczytu w osobnym profilu testowym.

Przykładowe narzędzia odczytu:

| Narzędzie | Ograniczony wynik |
|---|---|
| **`get_repository_metadata`** | Zwraca metadane jednego repozytorium |
| **`read_source_file`** | Odczytuje jedną ścieżkę w jednej rewizji |
| **`list_branches`** | Wyświetla gałęzie jednego repozytorium |
| **`get_pull_request`** | Zwraca jeden pull request po uzyskaniu zakresu odczytu pull requestów przez token |
| **`get_build_status`** | Zwraca dane statusu jednego commita |

Te nazwy opisują projekt. Nie są poleceniami Atlassian. Nie pozwól serwerowi przyjmować dowolnych adresów URL, poleceń powłoki, surowych tokenów, żądań eksportu klucza prywatnego ani nieograniczonych identyfikatorów repozytoriów.

Ustaw uprawnienia na czterech poziomach:

1. **Bitbucket Cloud:** klucz repozytorium lub projektu tylko do odczytu dla Git oraz najmniejsze zakresy tokenu API do odczytów REST.
2. **1Password:** jeden sejf lub konto usługi dla zadania, bez możliwości eksportu klucza prywatnego.
3. **Serwer MCP:** allowlista narzędzi odczytu, stałe endpointy Bitbucket Cloud, walidacja wejścia, limity czasu i zredagowane logi.
4. **Host MCP:** zgoda użytkownika na serwer i każdą operację umożliwiającą zapis, a narzędzia zapisu wyłączone w profilu domyślnym.

*Lista narzędzi MCP potwierdza ich wykrycie. Nie potwierdza autoryzacji, właściwego zakresu, bezpiecznej obsługi wejścia ani poprawności wyniku.*

## Zaplanuj przepływ pracy agenta

Zachowaj jawny przepływ pracy. Każdy etap dostarcza dowodów dla następnego.

| Etap | Działanie agenta | Uprawnienie | Zatwierdzenie przez człowieka |
|---|---|---|---|
| **Przygotuj** | Odczytaj konfigurację, rejestr klucza hosta, etykietę klucza, zakres tokenu i termin ważności | Odczyt lokalny | Zatwierdź rekord konfiguracji |
| **Sprawdź** | Sklonuj lub pobierz przez Git over SSH i odczytaj metadane REST | Odczyt repozytorium i API | Brak po konfiguracji |
| **Analizuj** | Odczytuj pliki, gałęzie, pull requesty i status kompilacji przez zatwierdzone narzędzia | Narzędzia MCP tylko do odczytu | Brak dla ograniczonych odczytów |
| **Przygotuj zmianę** | Utwórz poprawkę, plan gałęzi lub szkic pull requestu w lokalnym obszarze roboczym | Tylko zapis lokalny | Sprawdź diff i cel |
| **Zatwierdź zapis** | Przedstaw dokładną operację zdalną, zakres i procedurę wycofania | Bez zapisu zdalnego | Zatwierdzenie przez człowieka |
| **Wykonaj zapis** | Wypchnij gałąź, utwórz pull request lub wywołaj endpoint zapisu | Krótkotrwała tożsamość z prawem zapisu | Potwierdź każdą operację |
| **Zweryfikuj** | Odczytaj wynikowy commit, pull request lub status | Ponownie tylko do odczytu | Potwierdź oczekiwany wynik |

Domyślny profil agenta powinien zatrzymać się po etapie **Analizuj** lub **Przygotuj zmianę**. Osobny profil zapisu powinien używać innego tokenu lub klucza, krótkiego terminu ważności, stałego celu i monitu o zatwierdzenie. Klucz dostępu do repozytorium nie umożliwia kroku zapisu, co tworzy przydatną granicę techniczną.

## Wycofanie i usunięcie

Wycofywanie rozpocznij od odebrania dostępu, a następnie wyczyść konfigurację lokalną:

1. Usuń klucz dostępu do repozytorium, projektu lub obszaru roboczego w odpowiedniej sekcji ustawień Bitbucket.
2. Unieważnij token API repozytorium, projektu, obszaru roboczego lub użytkownika na odpowiedniej stronie zabezpieczeń Bitbucket.
3. Usuń zapisane poświadczenie Teamwork Graph zgodnie z udokumentowaną [procedurą uwierzytelniania](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/getting-started/how-authentication-works/) dla zainstalowanej wersji CLI. Poprzednie poświadczenie zachowaj wyłącznie w zatwierdzonym menedżerze sekretów. Potwierdź, że odizolowany profil nie wyświetla już poświadczenia testowego.
4. Po zakończeniu testu usuń plik repozytorium `.gitconfig` i wpis `includeIf`. Nie zmieniaj pozostałej konfiguracji Git.
5. Usuń tylko zweryfikowany wpis klucza hosta Bitbucket dodany na potrzeby testu. Zachowaj inne zatwierdzone klucze hostów.
6. Usuń zewnętrzny plik `agent.env` i pliki tymczasowe. Usuń wpis serwera MCP z konfiguracji hosta, a następnie uruchom hosta ponownie.

Zapisz każde usunięcie, wykonawcę i czas. Wymień klucz lub token, jeśli wartość trafiła do nieoczekiwanego logu, rekordu procesu lub transkrypcji.

## Pętla odczytu zdalnego i aktualizacji lokalnych referencji

Używaj krótkiej pętli do cyklicznej inspekcji repozytorium:

```bash
LOCAL_REPO="<local-directory>"
git -C "$LOCAL_REPO" fetch --no-tags
git -C "$LOCAL_REPO" status --short --branch
git -C "$LOCAL_REPO" log -1 --format='%H %ad %s' --date=iso-strict
```

`HEAD` oznacza aktualnie wybraną referencję repozytorium. Sukces dowodzi, że jedna dozwolona tożsamość SSH dotarła do wskazanego repozytorium. Nie dowodzi, który klucz wybrano ani czy istnieje dostęp do push.

**Oczekiwany wynik:** wynik fetch, status gałęzi i jeden wiersz commita. Przykład nieprzetestowany. `fetch` nie zapisuje danych zdalnie, ale aktualizuje lokalne referencje i `FETCH_HEAD`. Pętla nie wykonuje push ani nie zmienia gałęzi.

Serwer MCP powinien udostępniać tę samą granicę odczytu przez nazwane operacje. Lokalny wrapper powłoki lub narzędzie MCP powinno odrzucić czasownik zapisu przed wysłaniem żądania. Zapisuj nazwę narzędzia, symbol zastępczy repozytorium, rewizję, klasę wyniku i czas trwania. Redaguj tokeny, ciasteczka, ścieżki prywatne i treść plików, chyba że zadanie wymaga odczytu jednego pliku.

## Rozwiązywanie problemów

### `Permission denied (publickey)`

Sprawdź aktywne gniazdo agenta, wybrany klucz publiczny, wpis klucza dostępu do repozytorium i `IdentitiesOnly`. Klucz repozytorium musi być dodany do repozytorium docelowego lub projektu. Klucz osobisty wymaga uprawnień konta. Klucz obszaru roboczego ma inną granicę zapisu.

### Oferowany jest niewłaściwy klucz repozytorium

Użyj jednego klucza na repozytorium przez `core.sshCommand` albo grupuj klony w katalogu kontrolowanym przez `includeIf`. Wyświetl klucze agenta poleceniem `ssh-add -l`. Jeśli dostępnych jest wiele kluczy 1Password, użyj jawnego selektora tożsamości lub zakładki SSH 1Password. [Przewodnik 1Password Agent](https://www.1password.dev/ssh/agent) opisuje kwestie limitu kluczy i zakładek.

### SSH zgłasza zmieniony klucz hosta

Zatrzymaj agenta. Nie usuwaj `known_hosts` jako pierwszej reakcji. Porównaj aktualny rejestr kluczy hosta Bitbucket Cloud z lokalnym wpisem przez niezależny kanał. Usuń lub zastąp wpis dopiero po pomyślnej weryfikacji.

### API zwraca `401` lub `403`

Sprawdź wygaśnięcie tokenu, jego typ, zakres endpointu oraz granicę konta lub obszaru roboczego. Zakres odczytu repozytorium nie obejmuje pull requestów. Endpoint zapisu wymaga zakresu zapisu i zatwierdzonego profilu. Nie rozszerzaj zakresów, dopóki nie wskażesz niedziałającego endpointu.

### API zwraca dane repozytorium, ale nie pull requesty

Dodaj najmniejszy zakres odczytu pull requestów do nowego lub obróconego tokenu. Nie używaj ponownie szerokiego tokenu użytkownika dla serwera MCP tylko do odczytu.

### Serwer MCP wyświetla narzędzia, ale wywołanie nie działa

Rozdziel rejestrację serwera, połączenie, wykrywanie narzędzi, wykonanie i weryfikację wyniku. Sprawdź log serwera bez ujawniania tokenu. Zweryfikuj endpoint i format wejścia. Ponów próbę raz po sprawdzeniu łączności. Oznacz operację jako nieukończoną, jeśli druga próba również się nie powiedzie.

### CLI Bitbucket innej firmy żąda szerokiego dostępu

Zatrzymaj instalację. Porównaj żądany dostęp z opisem zadania. Sprawdź źródło, podpisy lub sumy kontrolne wydań, cele sieciowe, przechowywanie sekretów i operacje zapisu. Oficjalna referencja poleceń Atlassian CLI nie potwierdza obsługi binarnego narzędzia Bitbucket innej firmy.

## Następne kroki

Utwórz krótki rejestr dostępu: zakres repozytorium lub projektu, etykieta klucza, data weryfikacji klucza hosta, zakresy API, termin ważności tokenu, właściciel 1Password, allowlista narzędzi MCP, zasady logowania i osoba zatwierdzająca zapis.

Wykonaj jedno klonowanie tylko do odczytu, jeden odczyt metadanych REST i jeden odczyt narzędziem MCP, używając symboli zastępczych w transkrypcji. Porównaj wyniki. Pozostaw profil agenta tylko do odczytu, dopóki rejestr i logi nie przejdą weryfikacji.

Gdy pojawi się zadanie zapisu, najpierw przygotuj lokalny diff. Przedstaw gałąź docelową, zmienione ścieżki, żądaną metodę API, zakres tokenu i krok wycofania. Użyj osobnej, krótkotrwałej tożsamości z prawem zapisu dopiero po zatwierdzeniu dokładnej operacji przez człowieka.
