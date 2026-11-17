---
title: "Jak wgrać Rayhunter na urządzenia: kompletny poradnik"
draft: false
toc: true
date: 2026-03-09
lastmod: 2026-11-15
description: "Wgraj i skonfiguruj Rayhunter do wykrywania IMSI-catcherów. Sprawdź obsługiwane urządzenia, zainstaluj oprogramowanie sprzętowe, zweryfikuj działanie i rozwiąż typowe problemy."
tags: ["Rayhunter", "IMSI-catcher", "symulator stacji bazowej", "bezpieczeństwo urządzeń mobilnych", "wykrywanie inwigilacji", "ochrona prywatności", "Orbic RC400L", "TP-Link M7350", "mobilny hotspot", "wgrywanie oprogramowania", "cyberbezpieczeństwo", "bezpieczeństwo sieci bezprzewodowych", "przeciwdziałanie inwigilacji", "EFF", "narzędzia ochrony prywatności", "kup Rayhunter", "poradnik instalacji", "konfiguracja", "obsługiwane urządzenia", "bezpieczeństwo sieci"]
cover: "/img/cover/rayhunter.webp"
coverAlt: "Urządzenie Rayhunter wykrywające sygnały bezprzewodowe i IMSI-catchery, otoczone tarczami ochronnymi"
coverCaption: "System Rayhunter do wykrywania IMSI-catcherów, chroniący komunikację mobilną przed inwigilacją"
---

**Kompletny poradnik wgrywania i konfiguracji Rayhunter, systemu do wykrywania IMSI-catcherów.**

## W skrócie

**Rayhunter** to otwartoźródłowy system wykrywania IMSI-catcherów, działający na zmodyfikowanych mobilnych hotspotach. Powiadamia o próbach przechwycenia komunikacji komórkowej przez sprzęt inwigilacyjny. Ten poradnik opisuje instalację na urządzeniach Orbic RC400L i TP-Link M7350, konfigurację, analizę zagrożeń oraz skuteczność w sieciach 5G. Potrzebujesz zgodnego urządzenia z modemem Qualcomm. System wykrywa inwigilację w sieciach 2G, 3G i 4G za pomocą wielu heurystyk. Pozostaje użyteczny mimo upowszechniania się 5G, ponieważ nadal dochodzi do ataków wymuszających przejście na starszą generację sieci. Zapewnia ochronę dziennikarzom, aktywistom i osobom dbającym o prywatność przed inwigilacją rządową, przestępczą i korporacyjną.

**Rayhunter** to otwartoźródłowe narzędzie do wykrywania IMSI-catcherów (symulatorów stacji bazowych), które mogą przechwytywać komunikację mobilną. Jeśli szukasz **Rayhunter na sprzedaż** albo chcesz dowiedzieć się, jak wgrać i skonfigurować te urządzenia, ten poradnik omawia instalację, konfigurację i korzystanie z systemu **Rayhunter**.

**Informacja o sponsorowaniu:** Artykuł sponsoruje [STS Collective](https://stscollective.com), główny dostawca urządzeń zgodnych z Rayhunter. Mimo sponsorowania wszystkie informacje techniczne, analizy i zalecenia w tym poradniku opierają się na oficjalnej dokumentacji Rayhunter, opiniach społeczności i obiektywnej ocenie technicznej.

> 💰 **Specjalna zniżka dla czytelników:** Oszczędź do 20% na urządzeniach Rayhunter i produktach STS Collective. Podczas zakupu użyj kodu **SIMEONONSECURITY** albo [zrób zakupy z naliczoną zniżką](https://stscollective.com/discount/SIMEONONSECURITY).

## Wprowadzenie do Rayhunter

**Rayhunter** to zaawansowany system wykrywania IMSI-catcherów opracowany przez **Electronic Frontier Foundation (EFF)**, czołową organizację non-profit broniącą swobód obywatelskich w świecie cyfrowym. Od 1990 roku EFF działa na rzecz prywatności cyfrowej, wolności wypowiedzi i innowacji poprzez strategiczne procesy sądowe, analizy polityk, aktywizm społeczny i rozwój technologii.

To narzędzie działa na zgodnych mobilnych hotspotach i stale monitoruje sieci komórkowe pod kątem podejrzanych działań, które mogą wskazywać na obecność symulatorów stacji bazowych lub urządzeń StingRay wykorzystywanych do inwigilacji. **Rayhunter** odzwierciedla zaangażowanie EFF w dostarczanie praktycznych narzędzi ochrony prywatności osobom i organizacjom potrzebującym ochrony przed inwigilacją.

System **Rayhunter** wysyła alerty w czasie rzeczywistym po wykryciu potencjalnie szkodliwego zachowania w sieci komórkowej. To ważne narzędzie ochrony prywatności dla dziennikarzy, aktywistów, specjalistów ds. bezpieczeństwa i osób dbających o prywatność. Zgodne urządzenia **[Rayhunter na sprzedaż](https://stscollective.com/collections/rayhunter)** znajdziesz w STS Collective, głównego dostawcy tego specjalistycznego sprzętu.

### Wspieranie projektu Rayhunter

**Rayhunter** to projekt open source, który korzysta ze wsparcia społeczności. Możesz wspierać jego rozwój na kilka sposobów:

- **Zakup w STS Collective**: STS Collective przekazuje EFF część zysku ze sprzedaży każdego urządzenia Rayhunter, wspierając dalszy rozwój **Rayhunter** i badania nad ochroną prywatności.
- **Bezpośrednia darowizna**: Wesprzyj działania EFF na rzecz prywatności i rozwój **Rayhunter**, przekazując darowiznę pod adresem **[Wesprzyj EFF](https://supporters.eff.org/donate/donate)**.
- **Udział w społeczności**: Bierz udział w dyskusjach, twórz dokumentację i testuj oprogramowanie w oficjalnym repozytorium GitHub.

Twoje wsparcie pomaga utrzymać **Rayhunter** jako bezpłatne oprogramowanie open source, które jest stale rozwijane w odpowiedzi na zmieniające się zagrożenia inwigilacyjne.

## Pomoc, opinie i społeczność

**Rayhunter** jest wspierany przez aktywną społeczność badaczy bezpieczeństwa, obrońców prywatności i zaangażowanych obywateli. Możesz uzyskać pomoc i wspierać projekt przez różne kanały:

- **Oficjalna dokumentacja**: [Dokumentacja Rayhunter](https://efforg.github.io/rayhunter/introduction.html), zawierająca kompletne poradniki instalacji, konfiguracji i obsługi
- **Repozytorium GitHub**: [EFForg/rayhunter](https://github.com/EFForg/rayhunter)
- **Dyskusje społeczności**: Otwórz dyskusję na GitHubie o zgodności urządzeń lub rozwiązywaniu problemów
- **Badania bezpieczeństwa**: Współpracuj z badaczami nad poprawą możliwości wykrywania przez **Rayhunter**

Zgodne urządzenia **[Rayhunter na sprzedaż](https://stscollective.com/collections/rayhunter)** są dostępne w STS Collective.

## Często zadawane pytania

### Czy do korzystania z Rayhunter potrzebuję aktywnej karty SIM?

**Rayhunter** wymaga karty SIM w urządzeniu, ale karta nie musi mieć aktywnego planu usług. Jest potrzebna, aby urządzenie mogło łączyć się z sieciami komórkowymi i monitorować podejrzaną aktywność. Jeśli chcesz korzystać z urządzenia jako hotspotu podczas działania **Rayhunter**, potrzebujesz aktywnego planu.

### Jak sprawdzić, czy moje urządzenie Rayhunter działa?

Włącz heurystykę testową w ustawieniach konfiguracji **Rayhunter**. Urządzenie będzie wysyłać alerty za każdym razem, gdy wykryje stację bazową, co pomoże sprawdzić, czy system działa poprawnie. Ten tryb generuje dużo powiadomień, więc wyłącz go po teście.

### Czy kupić urządzenie z blokadą operatora czy bez niej?

W przypadku **Rayhunter** zazwyczaj lepiej wybrać urządzenie bez blokady, szczególnie jeśli zamierzasz używać kart SIM innych operatorów niż Verizon. Większość urządzeń Orbic marki Verizon w rzeczywistości nie ma blokady, ale przed zakupem sprawdź zgodność. Sprawdzone zgodne urządzenia **[Rayhunter na sprzedaż](https://stscollective.com/collections/rayhunter)** oferuje STS Collective.

{{< stscollective-ad "rayhunter" >}}

## Poradnik instalacji

### Instalacja z najnowszego wydania

Instalację **Rayhunter** przetestowano w systemach macOS i Ubuntu 24.04. Jeśli wystąpią problemy z gotowymi wydaniami, może być konieczna instalacja ze źródeł.

#### Wymagania wstępne

Przed instalacją **Rayhunter** upewnij się, że masz zgodne urządzenie. W przypadku urządzeń TP-Link włóż kartę SD sformatowaną w FAT, aby przechowywać nagrania.

#### Pobieranie i konfiguracja

1. **Pobierz najnowsze wydanie**: pobierz odpowiedni plik `rayhunter-vX.X.X-PLATFORM.zip` z oficjalnej strony wydań:
   - Linux x64: `linux-x64`
   - Linux ARM64: `linux-aarch64`
   - Linux ARM v7/v8: `linux-armv7`
   - macOS Intel: `macos-intel`
   - macOS ARM (M1/M2): `macos-arm`
   - Windows: `windows-x86_64`

2. **Rozpakuj archiwum i przejdź do folderu**:
   ```bash
   unzip ~/Downloads/rayhunter-vX.X.X-PLATFORM.zip
   cd ~/Downloads/rayhunter-vX.X.X-PLATFORM
   ```

3. **Połącz się z urządzeniem**: Włącz urządzenie i połącz się przez WiFi lub tethering USB. Powinien być dostępny adres:
   - Urządzenia Orbic: `http://192.168.1.1`
   - Urządzenia TP-Link: `http://192.168.0.1`

#### Instalacja dla konkretnych urządzeń

**Urządzenia Orbic RC400L** (dostępne **[z Rayhunter](https://stscollective.com)**):

**Rayhunter** obsługuje dwie metody instalacji na urządzeniach Orbic RC400L. Większości użytkowników zalecamy instalację przez WiFi. Instalacja przez USB zapewnia dodatkowe możliwości debugowania.

**Instalacja przez WiFi (zalecana)**:
```bash
# Użytkownicy macOS muszą najpierw wykonać to polecenie:
xattr -d com.apple.quarantine installer

# Dla Verizon RC400L (hasło administratora jest takie samo jak hasło WiFi):
./installer orbic --admin-password 'YourWiFiPassword'

# Dla Kajeet/Smartspot RC400L:
./installer orbic --admin-password='$m@rt$p0tc0nf!g'

# Dla urządzeń Moxee (format hasła: 12$ + ostatnie 3 cyfry hasła WiFi):
./installer orbic --admin-password='12$XXX'
```

**Instalacja przez USB (dla zaawansowanych użytkowników)**:
Metoda USB zapewnia dostęp do ADB (Android Debug Bridge) na potrzeby zaawansowanego debugowania, ale nie jest zalecana do typowej instalacji:

```bash
# OSTRZEŻENIE: instalator USB nie jest zalecany w większości zastosowań
./installer orbic-usb
```

Ta metoda wymusza włączenie trybu debugowania, aby aktywować dostęp ADB, instaluje rootshell i **Rayhunter**, a następnie uruchamia urządzenie ponownie. Używaj jej tylko wtedy, gdy potrzebujesz dostępu ADB w innych celach.

**Urządzenia TP-Link M7350** (dostępne **[z Rayhunter](https://stscollective.com)**):
```bash
./installer tplink
```

Instalator wgra **Rayhunter** i ponownie uruchomi urządzenie. Zielona linia na ekranie wskazuje, że **Rayhunter** działa poprawnie.

### Instalacja ze źródeł

Dla programistów i użytkowników, którzy chcą zbudować **Rayhunter** ze źródeł, projekt zawiera:

- **Frontend**: aplikację SvelteKit w JavaScript (`./daemon/web/`)
- **Backend**: plik binarny Rust `rayhunter-daemon` (`./daemon/`)
- **Instalator**: plik binarny Rust zawierający wszystkie elementy (`./installer`)

#### Zależności do kompilacji

Zainstaluj następujące zależności:
- Język programowania Rust
- Node.js/npm
- Narzędzia kompilacji C (`build-essential` w Linuksie, `xcode-select --install` w macOS)

#### Proces kompilacji

```bash
./scripts/build-dev.sh
./scripts/install-dev.sh orbic  # Zastąp 'orbic' typem swojego urządzenia
```

Aby pracować nad frontendem z automatycznym przeładowywaniem:
```bash
cd daemon/web
npm run dev
# Lub z własnym celem:
API_TARGET=http://192.168.1.1:8080 npm run dev
```

### Aktualizowanie Rayhunter

Aktualizacja **Rayhunter** przebiega tak samo jak instalacja. Powtórz te kroki, korzystając z najnowszego wydania, aby zaktualizować urządzenie do najnowszej wersji **Rayhunter**.

## Konfiguracja

**Rayhunter** można skonfigurować przez interfejs WWW albo bezpośrednio edytując na urządzeniu plik `/data/rayhunter/config.toml`.

### Konfiguracja przez interfejs WWW

Połącz się z siecią urządzenia i otwórz interfejs WWW **Rayhunter** pod adresem:
- Orbic: `http://192.168.1.1:8080`
- TP-Link: `http://192.168.0.1:8080`

{{< figure src="rayhunter-dashboard.webp" alt="Pulpit interfejsu WWW Rayhunter" caption="Interfejs WWW Rayhunter zapewnia rozbudowane opcje monitorowania i konfiguracji" >}}

#### Najważniejsze opcje konfiguracji

**Poziom interfejsu urządzenia**: określa, co **Rayhunter** wyświetla na ekranie:
- **Tryb niewidoczny**: brak informacji na ekranie
- **Tryb subtelny**: kolorowa linia (zielona = bezpiecznie, czerwona = alert, biała = wstrzymano)
- **Tryb demonstracyjny**: grafika orki i linia stanu
- **Logo EFF**: logo EFF i linia stanu
- **Wysoka widoczność**: pełnoekranowy kolorowy obraz

**Tryb przycisku urządzenia**: skonfiguruj działanie przycisku zasilania:
- **Wyłącz sterowanie przyciskiem**: przycisk zasilania nie steruje **Rayhunter**
- **Kliknij dwukrotnie, aby ponownie rozpocząć nagrywanie**: wyzeruj alerty i uruchom monitoring ponownie

**Ustawienia powiadomień**: skonfiguruj URL ntfy dla zdalnych alertów oraz włącz lub wyłącz powiadomienia o ostrzeżeniach i niskim poziomie baterii.

**Heurystyki analizatora**: włączaj lub wyłączaj konkretne algorytmy wykrywania **Rayhunter** zależnie od środowiska i modelu zagrożeń.

## Odinstalowywanie Rayhunter

### Urządzenia Orbic

Aby usunąć **Rayhunter** z urządzenia Orbic, uruchom:

```bash
./installer util orbic-shell --admin-password mypassword
```

W powłoce urządzenia:

> **Ostrzeżenie:** Poniższe polecenia trwale usuwają pliki Rayhunter i jego skrypty startowe. Upewnij się, że korzystasz z powłoki właściwego urządzenia. Skopiuj potrzebne nagrania lub konfigurację i przygotuj instalator oraz zgodne oprogramowanie sprzętowe. Po zakończeniu sprawdź, czy plików nie ma, a urządzenie uruchamia się bez usługi Rayhunter. Aby wycofać zmiany, zainstaluj ponownie odpowiednie wydanie z oficjalnego repozytorium.

```bash
echo 3 > /usrdata/mode.cfg
rm -rf /data/rayhunter /etc/init.d/rayhunter_daemon /bin/rootshell
reboot
```

### Urządzenia TP-Link

Aby odinstalować Rayhunter z urządzenia TP-Link:

> **Ostrzeżenie:** Te polecenia usuwają pliki Rayhunter i jego skrypt startowy z urządzenia TP-Link. Najpierw wyeksportuj nagrania i konfigurację. Uruchom polecenia wyłącznie w powłoce urządzenia, a następnie sprawdź, czy wskazane ścieżki nie istnieją i czy urządzenie normalnie się uruchamia. Aby wycofać zmiany, ponownie zainstaluj odpowiednie wydanie z oficjalnego repozytorium.

```bash
./installer util tplink-shell
rm /data/rayhunter /etc/init.d/rayhunter_daemon
update-rc.d rayhunter_daemon remove
```

Usuń pozostałe reguły przekierowania portów w interfejsie administratora TP-Link: Settings > NAT Settings > Port Triggers.

## Korzystanie z Rayhunter

Po instalacji **Rayhunter** uruchamia się automatycznie i stale monitoruje sieci komórkowe pod kątem podejrzanej aktywności. Podczas normalnego działania ekran pokazuje zieloną linię. Po wykryciu potencjalnego IMSI-catchera linia zmienia się w żółte kropki, pomarańczowe kreski lub ciągłą czerwoną linię.

### Heurystyki wykrywania Rayhunter

**Rayhunter** używa wielu zaawansowanych algorytmów wykrywania potencjalnej aktywności IMSI-catcherów:

#### Wykrywanie żądań IMSI
Ta heurystyka rozpoznaje podejrzane sekwencje, w których stacje bazowe żądają tożsamości urządzenia (IMSI, International Mobile Subscriber Identity) bez prawidłowej procedury uwierzytelniania. **Rayhunter** monitoruje czas i kontekst tych żądań, oznaczając nietypowe wzorce mogące wskazywać na sprzęt inwigilacyjny.

Prawidłowo działające sieci komórkowe stosują standardowe procedury uwierzytelniania, zanim zażądają poufnych identyfikatorów. IMSI-catchery często omijają te procedury, aby szybko zbierać tożsamości urządzeń, co powoduje wykrywalne anomalie w sekwencji uwierzytelniania. Metoda ta jest szczególnie skuteczna wobec prostych „pasywnych” IMSI-catcherów, które tylko zbierają informacje o urządzeniach.

#### Wykrywanie zerwania połączenia i przejścia na 2G
**Rayhunter** stale monitoruje podejrzane próby rozłączania urządzeń mobilnych z bezpiecznych sieci 4G/5G i ponownego łączenia ich z mniej bezpiecznymi sieciami 2G. IMSI-catchery często wykorzystują ten atak, ponieważ sieci 2G mają słabsze szyfrowanie i łatwiej je przechwycić.

System analizuje wzorce zrywania połączeń, zwracając uwagę na nietypową częstotliwość, czas i kontekst wskazujące na złośliwe działanie, a nie zwykłą optymalizację sieci. Prawidłowe sieci czasem proponują przejście na starszą generację z powodu zasięgu lub przepustowości, ale **Rayhunter** potrafi odróżnić normalne działanie sieci od potencjalnej inwigilacji.

#### Wykrywanie przejścia przez LTE SIB6/7
System Information Blocks (SIB) to komunikaty rozgłoszeniowe, za pomocą których sieci komórkowe przesyłają urządzeniom konfigurację. **Rayhunter** monitoruje konkretnie komunikaty SIB6 i SIB7, zawierające informacje o sąsiednich komórkach i przekierowaniu częstotliwości.

Atakujący mogą nadawać fałszywe komunikaty SIB6/7, aby zmusić urządzenia do porzucenia bezpiecznego połączenia 4G i przejścia do kontrolowanej przez nich sieci 2G. **Rayhunter** analizuje te transmisje pod kątem niespójności, nietypowych wzorców przekierowania i innych oznak fałszywych stacji bazowych próbujących wymusić zmianę sieci w celu przechwycenia komunikacji.

#### Wykrywanie szyfru zerowego
Ta ważna metoda wykrywania identyfikuje sytuacje, w których sieć komórkowa proponuje transmisję bez szyfrowania, czyli z użyciem szyfru zerowego. Prawidłowo działające komercyjne sieci komórkowe nie powinny proponować nieszyfrowanych połączeń, ponieważ naruszałoby to standardy bezpieczeństwa i przepisy.

**Rayhunter** oznacza każdą sieć proponującą szyfr zerowy jako wysoce podejrzaną. *Prawidłowa sieć nigdy nie proponuje szyfru zerowego.* To wyraźny sygnał, że sprzęt inwigilacyjny próbuje przechwycić komunikację w postaci jawnego tekstu. Heurystyka ta jest szczególnie skuteczna wobec IMSI-catcherów, które stawiają zbieranie danych ponad zachowanie pozorów prawidłowego działania sieci.

#### Wykrywanie niekompletnych bloków SIB
Prawidłowe stacje bazowe nadają kompletne bloki System Information Blocks z niezbędną konfiguracją sieci. **Rayhunter** wykrywa stacje bazowe wysyłające niekompletne albo brakujące informacje systemowe. Często wskazuje to na pośpiesznie wdrożony lub nieprawidłowo skonfigurowany sprzęt inwigilacyjny.

IMSI-catchery często nie implementują pełnej funkcjonalności sieci komórkowej, skupiając się na minimum potrzebnym do łączenia urządzeń i przechwytywania danych. Wykrywając niekompletne implementacje, **Rayhunter** może wskazać potencjalnie złośliwe stacje bazowe, którym brakuje pełnego zestawu funkcji oczekiwanego od prawidłowej infrastruktury komórkowej.

{{< figure src="rayhunter-heuristics-overview.webp" alt="Diagram pięciu heurystyk wykrywania Rayhunter: żądanie IMSI bez uwierzytelnienia, przejście na 2G, przekierowanie LTE SIB6/7, propozycja szyfru zerowego i niekompletne informacje systemowe" >}}
## Aktorzy zagrożeń i potencjalne cele

Zrozumienie, kto wdraża IMSI-catchery i kogo bierze na cel, pomaga ocenić własny model zagrożeń oraz dobrać konfigurację **Rayhunter**. Poszczególni aktorzy dysponują różnym poziomem zaawansowania, a ich strategie wskazują, jakie rodzaje inwigilacji ma wykrywać **Rayhunter**.

### Agencje rządowe i organy ścigania

**Zaawansowanie zagrożenia**: od zaawansowanego do profesjonalnego
**Główne cele**:
- Podejrzani przestępcy objęci śledztwem
- Osoby interesujące służby w sprawach bezpieczeństwa narodowego
- Demonstranci i aktywiści podczas protestów
- Powszechna inwigilacja w obszarach o wysokim poziomie bezpieczeństwa
- Cudzoziemcy i pracownicy dyplomatyczni

**Wzorce wykrywania**: Rządowe IMSI-catchery często używają zaawansowanego sprzętu, który może omijać podstawowe heurystyki wykrywania. Często jednak stosują **ataki wymuszające przejście na 2G** i **wzorce zrywania połączeń**, aby przenosić urządzenia do mniej bezpiecznych sieci i ułatwiać przechwytywanie. Wykrywanie przejść przez LTE SIB6/7 oraz monitorowanie zerwanych połączeń przez **Rayhunter** jest szczególnie skuteczne przeciw technikom inwigilacji stosowanym przez organy ścigania.

**Typowe scenariusze**:
- Inwigilacja podczas protestów, manifestacji i zgromadzeń publicznych
- Monitorowanie lokalizacji w pobliżu obiektów rządowych lub wrażliwej infrastruktury
- Ukierunkowana inwigilacja konkretnych osób objętych śledztwem
- Operacje inwigilacyjne na granicach i lotniskach

### Krajowe i zagraniczne agencje wywiadowcze

**Zaawansowanie zagrożenia**: od profesjonalnego do wojskowego
**Główne cele**:
- Zagraniczni agenci wywiadu i ich źródła
- Urzędnicy państwowi i pracownicy dyplomatyczni
- Wykonawcy z branży obronnej i badacze
- Kierownictwo firm z branż strategicznych
- Dziennikarze zajmujący się bezpieczeństwem narodowym
- Aktywiści działający w drażliwych politycznie obszarach

**Wzorce wykrywania**: Sprzęt wywiadowczy projektuje się z myślą o skrytym działaniu, ale wykrywanie szyfru zerowego i niekompletnych bloków SIB przez **Rayhunter** może ujawnić nawet zaawansowane operacje inwigilacyjne. W ukierunkowanych operacjach agencje często używają sprzętu żądającego **informacji IMSI**, co uruchamia algorytmy **Rayhunter** wykrywające żądania IMSI.

**Typowe scenariusze**:
- Długotrwała inwigilacja ważnych celów wywiadowczych
- Szpiegostwo przemysłowe w pobliżu siedzib firm
- Monitorowanie dyplomatów i ambasad
- Operacje kontrwywiadowcze
- Zagraniczne służby wywiadowcze biorące na cel krajowe źródła

### Organizacje przestępcze

**Zaawansowanie zagrożenia**: od podstawowego do średniego
**Główne cele**:
- Zamożne osoby, które można porwać lub szantażować
- Konkurenci biznesowi, aby zdobyć informacje o firmie
- Funkcjonariusze badający przestępczość zorganizowaną
- Świadkowie i informatorzy w sprawach karnych
- Osoby nękane, prześladowane lub doświadczające przemocy domowej

**Wzorce wykrywania**: Organizacje przestępcze zwykle korzystają z tańszych, komercyjnie dostępnych IMSI-catcherów, które jednocześnie uruchamiają wiele heurystyk **Rayhunter**. Urządzenia te często stosują **niekompletne implementacje SIB**, używają **szyfrów zerowych**, aby zebrać jak najwięcej danych, i przeprowadzają agresywne **ataki wymuszające przejście na 2G** z powodu ograniczonego zaawansowania technicznego.

**Typowe scenariusze**:
- Śledzenie potencjalnych ofiar porwania lub rabunku
- Monitorowanie komunikacji organów ścigania podczas operacji przestępczych
- Szpiegostwo przemysłowe i zdobywanie informacji o konkurencji
- Kampanie nękania i prześladowania
- Zastraszanie świadków i śledzenie ich lokalizacji

### Szpiegostwo korporacyjne i prywatny wywiad

**Zaawansowanie zagrożenia**: od średniego do zaawansowanego
**Główne cele**:
- Kierownictwo konkurencyjnych firm
- Zespoły badawczo-rozwojowe
- Negocjatorzy fuzji i przejęć
- Właściciele własności intelektualnej
- Opiekunowie tajemnic handlowych
- Sygnaliści i wewnętrzne źródła zagrożeń

**Wzorce wykrywania**: Operacje inwigilacji korporacyjnej często korzystają ze sprzętu ze średniej półki, łączącego koszt z możliwościami. Takie wdrożenia często wywołują **wykrywanie zrywania połączeń** i **alerty o żądaniu IMSI**, gdy celem są konkretne osoby podczas negocjacji biznesowych lub cyklu opracowywania produktu.

**Typowe scenariusze**:
- Inwigilacja podczas negocjacji fuzji i przejęć
- Zbieranie informacji o konkurencji na targach i konferencjach
- Operacje kradzieży własności intelektualnej
- Monitorowanie pracowników i wykrywanie zagrożeń wewnętrznych
- Pozyskiwanie danych klientów w celu uzyskania przewagi nad konkurencją

### Prywatni detektywi i firmy inwigilacyjne

**Zaawansowanie zagrożenia**: od podstawowego do średniego
**Główne cele**:
- Osoby objęte śledztwem dotyczącym oszustwa ubezpieczeniowego
- Małżonkowie w sprawach rozwodowych
- Pracownicy podejrzewani o niewłaściwe postępowanie
- Osoby uczestniczące w sporach prawnych
- Cele znane publicznie i celebryci

**Wzorce wykrywania**: Prywatne operacje inwigilacyjne zwykle wykorzystują sprzęt komercyjny z ograniczonymi możliwościami dostosowania. Z powodu kosztów i ograniczeń technicznych często uruchamia on podstawowe heurystyki **Rayhunter**, zwłaszcza **wykrywanie szyfru zerowego** i **monitorowanie niekompletnych bloków SIB**.

**Typowe scenariusze**:
- Śledztwa w sprawach rozwodowych i opieki nad dziećmi
- Inwigilacja związana z oszustwami ubezpieczeniowymi
- Śledztwa dotyczące niewłaściwego postępowania pracowników
- Prześladowanie celebrytów i działania paparazzi
- Śledztwa w sprawach prawnych i zbieranie dowodów

### Złośliwe osoby i haktywiści

**Zaawansowanie zagrożenia**: od podstawowego do średniego
**Główne cele**:
- Osobisty wróg lub partner romantyczny
- Osoby publiczne i celebryci
- Przypadkowe ofiary w miejscach publicznych
- Uczestnicy określonych wydarzeń lub osoby przebywające w konkretnych lokalizacjach
- Członkowie wybranych społeczności lub grup

**Wzorce wykrywania**: Pojedynczy sprawcy zwykle używają podstawowych, czasem improwizowanych IMSI-catcherów, które jednocześnie uruchamiają wiele algorytmów wykrywania **Rayhunter**. W takich wdrożeniach często występuje **użycie szyfru zerowego**, **niekompletne komunikaty SIB** i prymitywne **próby przejścia na 2G**.

**Typowe scenariusze**:
- Kampanie prześladowania i nękania
- Kradzież tożsamości i oszustwa finansowe
- Zakłócanie aktywizmu politycznego i protestów
- Ogólna działalność cyberprzestępcza
- Okazjonalna inwigilacja podczas wydarzeń publicznych

### Ocena zagrożeń i konfiguracja Rayhunter

**Osoby wysokiego ryzyka** (dziennikarze, aktywiści, urzędnicy i kierownictwo firm) powinny włączyć wszystkie heurystyki **Rayhunter** i wybrać tryb wyświetlania **wysoka widoczność**, aby zwiększyć możliwości wykrywania.

**Osoby umiarkowanego ryzyka** (ogólnie osoby dbające o prywatność) mogą używać **trybu subtelnego** z włączonymi podstawowymi heurystykami wykrywania, aby chronić się na co dzień bez przyciągania uwagi.

**Ochrona podczas wydarzeń** (protestów, wrażliwych spotkań i podróży) uzasadnia tymczasowe włączenie wszystkich metod wykrywania i systemów powiadomień, aby uzyskać pełny wgląd w inwigilację.

Znajomość własnego modelu zagrożeń pomaga zoptymalizować konfigurację **Rayhunter** do konkretnego poziomu ryzyka i zapewnić właściwe wykrywanie aktorów, którzy mogą obrać za cel ciebie lub twoje działania.

{{< figure src="imsi-catcher-threat-actors-surveillance.webp" alt="Diagram przedstawiający aktorów zagrożeń używających IMSI-catcherów, w tym agencje rządowe, organizacje przestępcze i szpiegów korporacyjnych biorących na cel urządzenia mobilne" >}}

## Skuteczność Rayhunter w erze 5G

{{< figure src="rayhunter-5g-downgrade-attack-persistence.webp" alt="Diagram przedstawiający telefon 5G zmuszany atakiem do przejścia do monitorowanej sieci 4G lub 3G, czyli technikę nadal wykrywaną przez Rayhunter w erze 5G" >}}

Wraz z przechodzeniem sieci komórkowych na 5G pojawiają się pytania o dalszą skuteczność **Rayhunter**, który wykrywa inwigilację w sieciach 2G, 3G i 4G/LTE, ale nie natywne metody inwigilacji 5G. Zrozumienie obecnych ograniczeń i dalszej przydatności **Rayhunter** ma kluczowe znaczenie przy planowaniu długoterminowych strategii wykrywania inwigilacji.

### Dlaczego Rayhunter nadal działa w sieciach 5G

#### Utrzymywanie się ataków wymuszających przejście do starszej sieci
Podstawowy rodzaj ataku wykrywany przez **Rayhunter** - zmuszanie urządzeń do łączenia się z mniej bezpiecznymi sieciami - nadal ma duże znaczenie przy wdrażaniu 5G. **IMSI-catchery nadal stosują ataki wymuszające przejście na 2G i 3G**, ponieważ:

- **Niższe koszty wdrożenia**: budowa sprzętu dla starszych protokołów wymaga znacznie mniejszych inwestycji niż opracowanie systemów zgodnych z 5G.
- **Szersza zgodność z urządzeniami**: wykorzystanie 2G/3G pozwala atakować też starsze urządzenia bez obsługi 5G.
- **Sprawdzone metody ataku**: techniki inwigilacji w sieciach 2G/3G są dobrze opisane i przetestowane.
- **Korzyści regulacyjne**: starsze technologie inwigilacji mogą podlegać mniejszym ograniczeniom prawnym niż zaawansowane metody przechwytywania 5G.

#### Wsteczna zgodność sieci
Sieci 5G zachowują **wsteczną zgodność z 4G/LTE**, a większość urządzeń mobilnych obsługuje jednocześnie kilka generacji sieci. Ta zgodność stwarza dalsze możliwości ataków przejścia między sieciami, które wykrywa **Rayhunter**:

- **Automatyczny powrót do starszej sieci**: gdy zasięg 5G jest słaby, urządzenia naturalnie wracają do 4G, co daje sprzętowi inwigilacyjnemu możliwość przechwycenia tej zmiany.
- **Luki w negocjacji protokołów**: zaawansowane IMSI-catchery mogą manipulować uzgadnianiem połączenia pomiędzy różnymi generacjami sieci.
- **Wykorzystywanie luk w zasięgu**: sprzęt inwigilacyjny rozmieszczony w obszarach bez pełnego zasięgu 5G może wymuszać przejście do monitorowanych sieci 4G/LTE.

#### Stopniowe wdrażanie 5G
**Powolne wdrażanie pełnego zasięgu 5G** sprawi, że **Rayhunter** pozostanie przydatny przez kolejne lata:

- **Różnice między miastem a wsią**: wiele regionów nadal korzysta głównie z sieci 4G/LTE, w których możliwości wykrywania **Rayhunter** mają bezpośrednie zastosowanie.
- **Ograniczony zasięg wewnątrz budynków**: sygnały 5G często słabo przenikają przez ściany, więc urządzenia wracają do 4G, które **Rayhunter** może skutecznie monitorować.
- **Podróże międzynarodowe**: wdrażanie 5G znacznie różni się w zależności od kraju, dlatego inwigilacja przez 4G/LTE nadal jest istotnym zagrożeniem dla podróżnych.

#### Opóźnienie technologiczne aktorów zagrożeń
Cykle **pozyskiwania i wdrażania sprzętu inwigilacyjnego** często pozostają w tyle za technologią sieci komercyjnych:

- **Terminy zakupów rządowych**: organy ścigania i agencje wywiadowcze mogą przez kilka lat po wdrożeniu 5G używać istniejącego sprzętu inwigilacyjnego obsługującego 4G.
- **Analiza kosztów i korzyści**: wiele operacji inwigilacyjnych osiąga cele dzięki tańszemu przechwytywaniu 4G/LTE, co zmniejsza motywację do zakupu systemów 5G.
- **Wymagania dotyczące szkolenia i wiedzy**: obsługa sprzętu inwigilacyjnego 5G wymaga specjalistycznej wiedzy, której organizacje inwigilacyjne mogą uczyć się przez dłuższy czas.

### Ograniczenia Rayhunter w prawdziwych środowiskach 5G

#### Martwe pola przy natywnej inwigilacji 5G
*To główne ograniczenie Rayhunter.* **Rayhunter nie wykryje natywnych operacji IMSI-catcherów w sieciach 5G**, które nie opierają się na atakach przejścia do starszej sieci:

- **Samodzielne sieci 5G (SA)**: gdy urządzenie łączy się z czystą siecią 5G bez przejścia na 4G, **Rayhunter** nie może monitorować takiej komunikacji.
- **Zaawansowany sprzęt inwigilacyjny 5G**: zaawansowani aktorzy zagrożeń z dostępem do nowoczesnej technologii mogą potencjalnie przechwytywać komunikację 5G bez uruchamiania heurystyk wykrywania **Rayhunter**.
- **Wykorzystanie segmentacji sieci**: funkcje segmentacji sieci 5G mogą zostać wykorzystane do inwigilacji w sposób niewykrywalny dla **Rayhunter**.

#### Ulepszone funkcje bezpieczeństwa 5G
Sieci 5G zawierają **lepsze zabezpieczenia**, które mogą ograniczać skuteczność tradycyjnych technik inwigilacji:

- **Silniejsze protokoły szyfrowania**: 5G stosuje odporniejsze standardy trudniejsze do złamania niż w poprzednich generacjach.
- **Ulepszone procedury uwierzytelniania**: lepsze uwierzytelnianie urządzeń w sieciach 5G może utrudnić pozyskiwanie IMSI.
- **Monitorowanie bezpieczeństwa sieci**: infrastruktura 5G ma lepsze możliwości wykrywania włamań oraz rozpoznawania i odpierania prób inwigilacji.

#### Zmiany w zachowaniu urządzeń
Wraz z upowszechnianiem się 5G **zachowanie urządzeń mobilnych może się zmienić**, wpływając na możliwości wykrywania przez **Rayhunter**:

- **Mniejsza skłonność do przechodzenia na starsze sieci**: przyszłe aktualizacje oprogramowania mogą zwiększyć odporność na takie ataki wraz z poprawą zasięgu 5G.
- **Preferowanie połączeń 5G**: urządzenia mogą częściej wybierać 5G i podejrzliwiej reagować na żądania użycia starszych protokołów.
- **Większa świadomość bezpieczeństwa**: systemy mobilne mogą lepiej rozpoznawać podejrzane zachowanie sieci.

### Strategiczne kwestie dotyczące wdrażania Rayhunter

#### Obecne zalecenia dotyczące wdrożenia
W przypadku obecnego i najbliższego wdrożenia **Rayhunter** zapewnia **kompleksowe możliwości wykrywania inwigilacji**:

- **Wdrożenia miejskie**: nawet w dużych miastach z szerokim zasięgiem 5G **Rayhunter** wykrywa próby inwigilacji wymierzone w sieci 4G/LTE.
- **Ochrona podczas ważnych wydarzeń**: podczas protestów, poufnych spotkań i działań wysokiego ryzyka **Rayhunter** zapewnia kluczową wykrywalność niezależnie od dostępności 5G.
- **Bezpieczeństwo podczas podróży**: **Rayhunter** nadal skutecznie wykrywa inwigilację w podróży krajowej i zagranicznej.

#### Przygotowanie na przyszłość
Organizacje i osoby planujące długoterminowe wykrywanie inwigilacji powinny rozważyć:

- **Hybrydowe metody wykrywania**: połączenie **Rayhunter** z innymi narzędziami i technikami monitorowania zapewnia pełniejsze pokrycie różnych wektorów zagrożeń.
- **Regularne aktualizowanie oceny zagrożeń**: śledzenie rozwoju technologii inwigilacyjnych pomaga określić, kiedy uzupełnić lub zastąpić możliwości **Rayhunter**.
- **Wsparcie rozwoju społeczności**: wspieranie rozwoju **Rayhunter** jako projektu open source zwiększa szanse dodania wykrywania 5G w przyszłych wydaniach.

#### Śledzenie rozwoju technologii
Społeczność **Rayhunter** i EFF nadal badają **możliwości wykrywania inwigilacji 5G**:

- **Badania analizy protokołów**: trwające badania protokołów 5G mogą wskazać nowe możliwości wykrywania dla przyszłych wersji **Rayhunter**.
- **Badania zgodności sprzętu**: ocena, czy zgodne z **Rayhunter** urządzenia można ulepszyć w celu wykrywania prób inwigilacji 5G.
- **Monitorowanie krajobrazu zagrożeń**: śledzenie rozwoju i wdrażania sprzętu inwigilacyjnego 5G pomaga ustalać priorytety przyszłego rozwoju **Rayhunter**.

**Rayhunter** pozostaje **ważnym narzędziem wykrywania inwigilacji** w obecnym środowisku telekomunikacyjnym. Prawdopodobnie będzie przydatny jeszcze przez kilka lat, gdy 5G będzie wdrażane stopniowo, a aktorzy zagrożeń nadal będą używać sprawdzonych metod wymuszania przejścia na starsze sieci.

### Ponowna analiza nagrań

**Rayhunter** stale ulepsza swoje możliwości wykrywania. Możesz ponownie analizować starsze nagrania z użyciem zaktualizowanych heurystyk. W interfejsie WWW kliknij „N warnings”, a następnie wybierz „re-analyze”.

### Analiza na komputerze

Zaawansowani użytkownicy mogą użyć narzędzia CLI `rayhunter-check`, dołączonego do **Rayhunter**, aby analizować pliki PCAP i QMDL na komputerach:

```bash
rayhunter-check -p ~/Downloads/myfile.qmdl
rayhunter-check -p ~/Downloads/myfile.pcap
rayhunter-check -d -p ~/Downloads/myfile.qmdl  # Tryb debugowania
```

## Obsługiwane urządzenia

**Rayhunter** obsługuje różne mobilne hotspoty z modemami Qualcomm, które udostępniają interfejs `/dev/diag`.

{{< figure src="/img/rayhunter-device-regions.svg" alt="Zgodność urządzeń Rayhunter w poszczególnych regionach" caption="Zgodność urządzeń i zalecenia regionalne dotyczące instalacji Rayhunter" >}}
### Zalecane urządzenia

Te urządzenia zostały gruntownie przetestowane i są powszechnie używane przez społeczność **Rayhunter**:

#### Orbic RC400L (czasami sprzedawany pod marką Kajeet RC400L)
- **Zalecany region**: Ameryki
- **Obsługiwane pasma**:
  - 5G: n260/n261, n77, n2/5/48/66
  - 4G: 2/4/5/12/13/48/66
  - Globalne i roamingowe: n257/n78
- **Dostępność**: dostępne są zgodne urządzenia, w tym **[nowy Orbic RC400L z Rayhunter](https://stscollective.com/products/new-rayhunter-orbic-rc400l-imsi-catcher-detector-premium?variant=51361976811822)** i **[Kajeet RC400L](https://stscollective.com/products/rayhunter-imsi-catcher-detector-kajeet-rc400lx-4g-lte-hotspot?variant=51411271844142)**
- **Zakres cen**: profesjonalne modele można kupić w STS Collective

#### TP-Link M7350
- **Zalecany region**: Afryka, Europa, Bliski Wschód (działa też w Amerykach, ale zwykle jest tam droższy)
- **Wymagania specjalne**: nagrywanie wymaga karty SD sformatowanej w FAT
- **Dostępność**: sprawdzone zgodne modele są dostępne jako **[TP-Link M7350 z Rayhunter](https://stscollective.com/collections/rayhunter)**

### Działające urządzenia

Potwierdzono działanie **Rayhunter** na następujących dodatkowych urządzeniach:

- **Wingtech CT2MHS01** (Ameryki), **[dostępny z Rayhunter](https://stscollective.com/collections/rayhunter)**
- **Tmobile TMOHS1** (Ameryki), **[dostępny z Rayhunter](https://stscollective.com/collections/rayhunter)**
- **TP-Link M7310** (Afryka, Europa, Bliski Wschód), **[dostępny z Rayhunter](https://stscollective.com)**
- **PinePhone i PinePhone Pro** (globalnie), **[dostępne z Rayhunter](https://stscollective.com)**
- **FY UZ801** (Azja, Europa), **[dostępny z Rayhunter](https://stscollective.com)**
- **Hotspot Moxee** (Ameryki), **[Moxee K779HSDL z Rayhunter](https://stscollective.com/products/rayhunter-imsi-catcher-stingray-detector-moxee-k779hsdl-hotspot-professionally-refurbished-pre-installed-4g-lte-cellular-threat-detection-device?variant=51309010420014)**

### Uwagi dotyczące instalacji konkretnych urządzeń

#### Orbic/Kajeet RC400L

Orbic RC400L to pierwsze urządzenie, dla którego opracowano **Rayhunter**. Jest **[dostępne z Rayhunter](https://stscollective.com)** w STS Collective.

**Metody instalacji**:
- **Przez sieć**: `./installer orbic` (zalecana, działa przez WiFi)
- **Przez USB**: `./installer orbic-usb` (zapewnia dostęp ADB i powłokę roota)

**Domyślne hasła**:
- **Verizon RC400L**: hasło administratora jest zawsze takie samo jak hasło WiFi (znajdziesz je w menu urządzenia)
- **Kajeet/Smartspot RC400L**: `$m@rt$p0tc0nf!g`
- **Urządzenia Moxee**: hasło ma format `12$XXX`, gdzie XXX oznacza ostatnie 3 cyfry hasła WiFi (sprawdź hasło pod baterią)

**Dostęp do powłoki**: po instalacji użyj `./installer util orbic-shell`.

#### TP-Link M7350/M7310

Te urządzenia niezawodnie współpracują z **Rayhunter** i są **[dostępne z Rayhunter](https://stscollective.com)**.

**Instalacja**: `./installer tplink` (hasło administratora nie jest wymagane)
**Pamięć**: przed instalacją włóż kartę SD sformatowaną w FAT
**Dostęp do powłoki**: `./installer util tplink-shell`

#### Urządzenia specjalistyczne

**PinePhone i PinePhone Pro**: zgodność globalna, **[dostępne z Rayhunter](https://stscollective.com)**
**UZ801**: popularny w Azji i Europie, **[dostępny z Rayhunter](https://stscollective.com)**
**Wingtech CT2MHS01**: urządzenie przeznaczone dla Ameryk, **[dostępne z Rayhunter](https://stscollective.com)**

### Dodawanie nowych urządzeń

**Rayhunter** może potencjalnie obsługiwać każde urządzenie z modemem Qualcomm udostępniającym interfejs `/dev/diag`. Jeśli chcesz, aby **Rayhunter** obsługiwał twoje urządzenie, rozpocznij dyskusję w oficjalnym repozytorium GitHub.

## Dokumentacja REST API

**Rayhunter** udostępnia rozbudowane REST API do programowego dostępu do stanu urządzenia, nagrań i konfiguracji. API umożliwia integrację z innymi narzędziami bezpieczeństwa i zautomatyzowanymi systemami monitorowania.

### Oficjalna dokumentacja API

Pełny opis API, zawierający szczegółowe specyfikacje punktów końcowych, przykłady żądań i odpowiedzi oraz metody uwierzytelniania, znajdziesz w **[oficjalnej dokumentacji REST API Rayhunter](https://efforg.github.io/rayhunter/api-docs/)**.

### Punkty końcowe API

API **Rayhunter** jest dostępne pod adresem `http://[device-ip]:8080/api/` i udostępnia punkty końcowe do:

- **Stanu systemu**: monitorowania kondycji urządzenia i działania **Rayhunter**
- **Zarządzania nagraniami**: rozpoczynania, zatrzymywania i pobierania nagrań
- **Pobierania alertów**: wyświetlania alertów wykrywania i wyników analizy
- **Konfiguracji**: programowego aktualizowania ustawień **Rayhunter**
- **Sterowania heurystykami**: włączania i wyłączania konkretnych algorytmów wykrywania
- **Informacji o urządzeniu**: pobierania specyfikacji i możliwości sprzętu
- **Monitorowania sieci**: dostępu do bieżących danych sieci komórkowej
- **Rejestrowania zdarzeń**: przeglądania historycznych zdarzeń wykrywania i alertów

### Uwierzytelnianie

Dostęp do API korzysta z takiego samego uwierzytelniania jak interfejs WWW. Zabezpiecz urządzenie **Rayhunter** i udostępniaj je tylko upoważnionym użytkownikom.

### Przykłady integracji

REST API **Rayhunter** można zintegrować z platformami monitorowania bezpieczeństwa, systemami SIEM i własnymi narzędziami automatyzacji. Przykłady implementacji i dobre praktyki znajdziesz w **[oficjalnej dokumentacji API](https://efforg.github.io/rayhunter/api-docs/)**.

## Rozwiązywanie problemów

### Typowe problemy z instalacją

**Problemy z połączeniem USB**: wypróbuj inne kable lub porty USB. Wadliwe połączenia USB często powodują błędy instalacji. *To najczęstsza przyczyna niepowodzenia instalacji.*

**Problemy z zabezpieczeniami macOS**: jeśli pojawi się komunikat "No Orbic device found", tymczasowo zmień ustawienie "Allow accessories to connect" na "Always" w ustawieniach bezpieczeństwa.

**Wykrywanie urządzenia**: po instalacji włącz heurystykę testową, aby sprawdzić, czy **Rayhunter** działa poprawnie.

### Uzyskiwanie pomocy

Pomoc przy instalacji i rozwiązywaniu problemów:
- Sprawdź oficjalną dokumentację **Rayhunter**
- Użyj poleceń `./installer --help` i `./installer util --help`, aby zobaczyć dostępne opcje
- Zadaj pytanie w dyskusjach społeczności w GitHubie
- Skontaktuj się z **[STS Collective](https://stscollective.com)** w sprawie zgodności urządzeń

## Często zadawane pytania (FAQ)

### Pytania ogólne

#### Czym dokładnie jest IMSI-catcher i jak działa?
IMSI-catcher, nazywany też StingRayem, symulatorem stacji bazowej lub fałszywą wieżą komórkową, to sprzęt inwigilacyjny podszywający się pod prawidłowe stacje bazowe w celu przechwytywania komunikacji urządzeń mobilnych. Wymusza na pobliskich urządzeniach połączenie ze złośliwym sprzętem zamiast z prawidłową stacją. Operator może dzięki temu zbierać identyfikatory urządzeń (numery IMSI), dane lokalizacyjne, metadane połączeń, a potencjalnie także przechwytywać komunikację. **Rayhunter** wykrywa takie urządzenia, identyfikując nieprawidłowe zachowanie sieci komórkowej.

#### Czy Rayhunter wykrywa każdy rodzaj sprzętu inwigilacyjnego?
**Rayhunter** wykrywa konkretnie IMSI-catchery i symulatory stacji bazowych w sieciach 2G, 3G i 4G/LTE. Nie wykrywa innych form inwigilacji, takich jak monitorowanie WiFi, lokalizatory GPS, obserwacja fizyczna ani natywna inwigilacja 5G niewykorzystująca ataków przejścia na starszą sieć. **Rayhunter** jest jednym z elementów kompleksowej strategii ochrony prywatności.

#### Czy korzystanie z Rayhunter jest legalne?
W większości jurysdykcji korzystanie z **Rayhunter** jest legalne, ponieważ to pasywne narzędzie monitorujące, które nie zakłóca sieci komórkowych ani innych urządzeń. Analizuje jedynie sygnały komórkowe naturalnie odbierane przez urządzenie. Lokalne przepisy są różne, więc sprawdź regulacje obowiązujące w twoim regionie. EFF opracowała **Rayhunter** jako legalne narzędzie ochrony prywatności.

### Pytania techniczne

#### Dlaczego Rayhunter wymaga karty SIM, jeśli nie potrzebuje aktywnego planu?
Karta SIM zawiera numer International Mobile Subscriber Identity (IMSI), niezbędny do uwierzytelnienia urządzenia w sieciach komórkowych i udziału w wymianie komunikatów protokołu monitorowanej przez **Rayhunter**. Bez karty SIM urządzenie nie połączy się z siecią komórkową, a **Rayhunter** nie będzie mieć aktywności sieciowej do analizy pod kątem podejrzanych wzorców.

#### Ile danych zużywa Rayhunter podczas zwykłej pracy?
**Rayhunter** zużywa niewiele danych podczas podstawowego monitorowania, bo analizuje głównie informacje o protokołach komórkowych, a nie ruch internetowy. Zużycie danych wzrośnie, jeśli włączysz zdalne powiadomienia przez ntfy albo jednocześnie użyjesz urządzenia jako hotspotu. Samo monitorowanie zużywa pomijalnie mało przepustowości.

#### Czy mogę korzystać z Rayhunter, gdy urządzenie działa jako mobilny hotspot?
Tak, **Rayhunter** może działać jednocześnie z funkcją mobilnego hotspotu. Wymaga to aktywnego planu usług komórkowych. Monitorowanie przez **Rayhunter** działa niezależnie od hotspotu, ale jednoczesne używanie obu funkcji zużywa więcej energii baterii.

#### Czym różni się instalacja przez WiFi od instalacji przez USB?
**Metoda WiFi** (zalecana większości użytkowników) instaluje **Rayhunter** przez interfejs bezprzewodowy urządzenia i zapewnia standardowe funkcje. **Metoda USB** zapewnia zaawansowanym użytkownikom dostęp do Android Debug Bridge (ADB) w celu debugowania, ale jest bardziej złożona i niepotrzebna przy typowej instalacji.

### Pytania o urządzenia i zgodność

#### Dlaczego Rayhunter obsługuje tylko niektóre urządzenia?
**Rayhunter** wymaga urządzenia z modemem Qualcomm, który udostępnia interfejs `/dev/diag` umożliwiający dostęp do informacji o protokołach komórkowych. Większość urządzeń konsumenckich nie udostępnia tego interfejsu ze względów bezpieczeństwa. Obsługiwane urządzenia zostały przetestowane i potwierdzono ich zgodność z wymaganiami **Rayhunter**.

#### Czy mogę zainstalować Rayhunter na zwykłym smartfonie?
Nie. **Rayhunter** nie można zainstalować na zwykłych smartfonach. Wymaga specjalistycznych mobilnych hotspotów ze wskazanymi modemami Qualcomm udostępniającymi interfejsy diagnostyczne. Obsługiwane urządzenia to między innymi Orbic RC400L, TP-Link M7350 i kilka innych modeli mobilnych hotspotów.

#### Co się stanie, jeśli spróbuję zainstalować Rayhunter na niezgodnym urządzeniu?
Instalator **Rayhunter** wykrywa urządzenie i zazwyczaj odmówi instalacji na niezgodnym sprzęcie. Próba wymuszenia instalacji na nieobsługiwanym urządzeniu może je uszkodzić lub unieruchomić. Przed instalacją zawsze sprawdź zgodność urządzenia.

#### Czy do różnych regionów potrzebuję innych urządzeń?
Tak. Pasma częstotliwości sieci komórkowych różnią się w zależności od regionu. Orbic RC400L jest dostosowany do sieci w Amerykach, a TP-Link M7350 dobrze działa w Europie, Afryce i na Bliskim Wschodzie. Informacje o zgodności urządzeń **Rayhunter** zawierają zalecenia regionalne, dzięki czemu wybierzesz model odpowiedni dla swojej lokalizacji.

### Pytania o użytkowanie i konfigurację

#### Jak sprawdzić, czy urządzenie Rayhunter działa poprawnie?
Włącz heurystykę testową w ustawieniach konfiguracji **Rayhunter**. Za każdym razem, gdy urządzenie wykryje dowolną stację bazową, pojawi się alert potwierdzający działanie systemu. Podczas normalnej pracy ekran powinien pokazywać zieloną linię. Po teście wyłącz heurystykę, ponieważ generuje wiele alertów.

#### Co zrobić, gdy Rayhunter wysyła ostrzeżenie?
Po wykryciu podejrzanej aktywności przez **Rayhunter** najpierw zapisz swoją lokalizację i okoliczności. Optymalizacja sieci lub problemy ze sprzętem mogą powodować fałszywe alarmy. Jeśli alerty powtarzają się w tym samym miejscu lub podczas wrażliwych działań, rozważ zmianę lokalizacji i sprawdź szczegóły alertu w interfejsie WWW.

#### Jak często aktualizować Rayhunter?
**Aktualizuj Rayhunter co miesiąc.** Sprawdzaj stronę wydań pod kątem nowych heurystyk i ulepszeń zgodności, które są regularnie dodawane. EFF stale poprawia możliwości **Rayhunter** w odpowiedzi na zmieniające się techniki inwigilacji. Aktualizacja przebiega tak samo jak pierwsza instalacja.

#### Czy Rayhunter może jednocześnie chronić kilka osób?
**Rayhunter** wykrywa IMSI-catchery w okolicy, więc może chronić kilka osób w swoim zasięgu, zazwyczaj do kilkuset metrów zależnie od siły sygnału. Osoby poważnie podchodzące do wykrywania inwigilacji powinny jednak rozważyć własne urządzenie **Rayhunter**, aby uzyskać maksymalną ochronę i kontrolę konfiguracji.

### Pytania o bezpieczeństwo i prywatność

#### Czy korzystanie z Rayhunter sprawi, że będę bardziej widoczny dla służb?
**Rayhunter** działa pasywnie i nie nadaje sygnałów, które mogłyby ujawnić jego obecność sprzętowi inwigilacyjnemu. Korzystanie z dowolnego narzędzia bezpieczeństwa wskazuje jednak na dbałość o prywatność. Korzyści z wykrywania zwykle przewyższają ryzyko, zwłaszcza w przypadku osób wysokiego ryzyka, takich jak dziennikarze i aktywiści.

#### Czy sprzęt inwigilacyjny wykryje korzystanie z Rayhunter?
**Rayhunter** to pasywny system monitorowania, który nie transmituje sygnałów identyfikujących. Operatorzy inwigilacyjni nie mogą wykryć korzystania z **Rayhunter** na poziomie protokołu komórkowego. Obserwacja urządzenia lub analiza ruchu sieciowego może jednak ujawnić używanie **Rayhunter**, jeśli włączono zdalne powiadomienia.

#### Jakie informacje Rayhunter zbiera na mój temat?
**Rayhunter** analizuje informacje o protokołach komórkowych i przechowuje alerty lokalnie na urządzeniu. Nie zbiera informacji osobistych, treści komunikacji ani danych lokalizacyjnych poza zakresem niezbędnym dla algorytmów wykrywania. Wszystkie dane pozostają na urządzeniu, chyba że włączysz zdalne powiadomienia.

### Pytania zaawansowane

#### Czy mogę analizować dane Rayhunter na komputerze?
Tak. **Rayhunter** zawiera narzędzie wiersza poleceń `rayhunter-check` do analizy nagranych plików PCAP i QMDL na komputerach stacjonarnych. Dzięki temu zaawansowani użytkownicy mogą szczegółowo analizować zdarzenia wykrywania i badać podejrzaną aktywność, wykorzystując pełne zasoby komputera.

#### Jak Rayhunter działa w gęsto zaludnionych miastach?
W dużych miastach z wieloma prawidłowymi stacjami bazowymi optymalizacja sieci i częste przełączanie urządzeń między stacjami mogą zwiększyć liczbę fałszywych alarmów. Algorytmy **Rayhunter** rozróżniają normalne działanie sieci od inwigilacji, ale użytkownicy w gęsto zaludnionych miejscach mogą potrzebować zmienić poziom czułości.

#### Czy Rayhunter działa podczas podróży zagranicznych?
Skuteczność **Rayhunter** podczas podróży zależy od zgodności urządzenia z lokalnymi pasmami komórkowymi i umowami roamingowymi. Algorytmy wykrywania działają globalnie, ale upewnij się, że urządzenie obsługuje częstotliwości wykorzystywane w miejscu docelowym. Pełne działanie może wymagać roamingu międzynarodowego.

{{< figure src="rayhunter-faq-privacy-protection.webp" alt="Osoba przeglądająca alerty Rayhunter na laptopie i niosąca mobilny hotspot w mieście, w pobliżu widocznych stacji bazowych" >}}

______

**Rayhunter** to ważny postęp w ochronie prywatności i wykrywaniu inwigilacji. Prawidłowo wgrywając i konfigurując **Rayhunter** na zgodnym urządzeniu, zyskujesz możliwość wykrywania IMSI-catcherów i ochrony komunikacji mobilnej przed nieuprawnioną inwigilacją.

Niezależnie od tego, czy jesteś dziennikarzem, aktywistą, specjalistą ds. bezpieczeństwa czy osobą dbającą o prywatność, **Rayhunter** zapewnia narzędzia do ochrony bezpieczeństwa mobilnego w coraz bardziej nadzorowanym świecie. Sprawdzone zgodne urządzenia znajdziesz w ofercie **[Rayhunter na sprzedaż](https://stscollective.com)** u zaufanych dostawców sprzętu bezpieczeństwa.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Kup urządzenia Rayhunter i oszczędź 20%
{{< /centerbutton >}}

## Źródła

- [Oficjalne repozytorium Rayhunter w GitHub](https://github.com/EFForg/rayhunter)
- [Najnowsze wydanie Rayhunter](https://github.com/EFForg/rayhunter/releases/tag/v0.10.2)
- [Electronic Frontier Foundation](https://www.eff.org/)
- [STS Collective, dostawca sprzętu Rayhunter](https://stscollective.com)
