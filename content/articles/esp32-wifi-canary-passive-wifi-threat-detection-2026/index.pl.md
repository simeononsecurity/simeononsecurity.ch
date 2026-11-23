---
title: "ESP32 WiFi Canary: pasywne wykrywanie zagrożeń w paśmie 2,4 GHz"
date: 2026-06-06
lastmod: 2026-11-22
toc: true
draft: false
description: "Techniczny opis ESP32 WiFi Canary, pasywnego czujnika 2,4 GHz wykrywającego evil twin, deautentykację, obniżenie zabezpieczeń i zalewanie beaconami."
genre: ["Bezpieczeństwo sieci", "Bezpieczeństwo WiFi", "Bezpieczeństwo IoT", "Badania bezpieczeństwa", "Systemy wbudowane", "Narzędzia ochrony prywatności", "Projekty ESP32", "Bezpieczeństwo sprzętu", "Bezpieczeństwo bezprzewodowe", "Bezpieczeństwo open source"]
tags: ["ESP32", "WiFi Canary", "M5Stack Atom Lite", "Wykrywanie deautentykacji", "Wykrywanie evil twin", "Bezpieczeństwo WiFi", "Pasywny monitoring WiFi", "Ramki zarządzające 802.11", "Bezpieczeństwo sieci", "Bezpieczeństwo IoT", "NeoPixel", "SK6812", "PlatformIO", "C++", "Oprogramowanie otwarte", "Czujnik bezpieczeństwa", "Wykrywanie zagrożeń bezprzewodowych", "Monitoring BSSID", "Monitoring SSID", "Wykrywanie obniżenia zabezpieczeń", "Wykrywanie zalewu beaconami", "Monitoring WiFi", "Dioda RGB", "Tryb promiscuous", "Bezpieczeństwo systemów wbudowanych", "Bezpieczeństwo w podróży", "Bezpieczeństwo hotelowego WiFi", "WiFi w kawiarniach", "Świadomość bezpieczeństwa", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/"
cover: "/img/cover/esp32-wifi-canary-passive-wifi-threat-detection-2026.webp"
coverAlt: "Ilustracja małego urządzenia przypominającego ESP32 WiFi Canary podłączonego do portu USB. Dioda RGB świeci różnymi kolorami, symbolizując wykrywanie zagrożeń."
coverCaption: ""
---

**Pasywny czujnik zagrożeń WiFi wielkości kciuka, który nigdy nie odpowiada**

## Problem publicznych sieci WiFi

Gdy łączysz się z hotelowym WiFi, hotspotem w kawiarni lub siecią na lotnisku, zakładasz, że widoczny punkt dostępowy jest prawdziwy. Problem polega na tym, że **ramki zarządzające 802.11**, które ogłaszają sieci, zarządzają połączeniami i koordynują klientów, są w większości wdrożeń *całkowicie nieuwierzytelnione*. Przy prostym sprzęcie każdy może sklonować SSID, wysyłać ramki deautentykacji albo uruchomić otwartą sieć-pułapkę obok prawdziwej sieci WPA2.

[**ESP32 WiFi Canary**](https://github.com/simeononsecurity/esp32-wifi-canary) to pasywny czujnik, który pomaga zauważyć to ryzyko w bardzo małej obudowie. Mieści się na M5Stack Atom Lite, urządzeniu wielkości kostki cukru. Po podłączeniu do USB poznaje otoczenie i zapala diodę RGB, gdy wykryje wzorce wskazujące na zagrożenia bezprzewodowe.

Nie łączy się z sieciami, nie przechwytuje danych logowania i nie wysyła ramek. Obserwuje, nalicza punkty i pokazuje stan kolorem.

To kompletna dokumentacja techniczna projektu: opisuje wykrywane zdarzenia, model pewności, budowanie i wgrywanie oprogramowania oraz ograniczenia w praktyce.

---

## Co ESP32 WiFi Canary robi, a czego nie robi

### Zawsze tylko pasywnie

WiFi Canary korzysta z dwóch trybów radiowych, ale nigdy jednocześnie:

1. **Tryb promiscuous**: odbiera i analizuje ramki zarządzające 802.11, takie jak deautentykacja i rozłączenie, bez łączenia się z siecią.
2. **Tryb skanowania**: aktywnie skanuje WiFi, wykrywa pobliskie punkty dostępowe i porównuje je z nauczoną bazą odniesienia.

Urządzenie nigdy:
- nie łączy się z żadną siecią;
- nie przechwytuje ramek danych ani danych logowania;
- nie wysyła żadnych ramek 802.11;
- nie zapisuje danych w trwałej pamięci flash;
- nie komunikuje się przez Internet.

**Wszystko, czego się nauczy, pozostaje w RAM i znika po ponownym uruchomieniu.** To celowe: canary jest **czujnikiem**, a nie urządzeniem do przechwytywania.

### Dioda LED jest interfejsem

Urządzenie nie ma ekranu, aplikacji ani interfejsu WWW. Całe wyjście stanowi jeden **NeoPixel RGB SK6812** na GPIO 27 M5Stack Atom Lite. Dioda pokazuje cztery stany:

| Stan diody | Znaczenie |
|---|---|
| 🔵 Niebieski (wolne pulsowanie) | Uruchamianie, tworzenie bazy odniesienia |
| 🟢 Zielony (ciągły) | Normalnie, brak problemów o wysokiej pewności |
| 🟡 Żółty (ciągły) | Uwaga, wykryto podejrzany wzorzec |
| 🔴 Czerwony (szybkie pulsowanie) | Alarm, wykryto zagrożenie o wyższej pewności |

Uruchamianie trwa około **24 sekund** (3 skany po 8 sekund). Gdy dioda przestaje świecić na niebiesko, baza jest gotowa i zaczyna się monitoring.

---

## Sprzęt

### Główny cel: M5Stack Atom Lite

Projekt powstał z myślą o M5Stack Atom Lite, kompletnej platformie rozwojowej ESP32 w obudowie 24 × 24 mm.

| Element | Szczegóły |
|---|---|
| MCU | ESP32-PICO-D4 |
| Dioda | Jeden NeoPixel RGB SK6812 (GPIO 27) |
| Przycisk | GPIO 39, aktywny stanem niskim |
| USB | Mostek UART CP2104 |
| Zasilanie | USB-C, ok. 80–120 mA podczas skanowania |

**Bez płytki stykowej, dodatkowych elementów i lutowania.** Podłącz zasilanie USB i urządzenie działa.

### Uniwersalny ESP32 DevKit do rozwoju i testów

Projekt ma drugie środowisko PlatformIO (`esp32dev`) dla standardowych płytek ESP32. W tej konfiguracji:

- wbudowana dioda GPIO 2 zastępuje NeoPixel;
- włączone jest pełne szeregowe wyjście debugowania;
- cała logika wykrywania działa tak samo jak w wersji Atom Lite.

Dzięki temu projekt jest dostępny dla osób z ESP32 DevKit za 5 USD i pozwala testować logikę bez sprzętu docelowego.

---

## Proces uczenia bazy odniesienia

### Dlaczego baza jest ważna

Canary, który alarmuje o każdej otwartej sieci w mieście, byłby bezużyteczny. ESP32 WiFi Canary najpierw poznaje otoczenie, a dopiero potem ocenia zagrożenia. Pierwsza faza tworzy **tabelę referencyjną** punktów dostępowych, które legalnie działają w pobliżu.

### Trzy skany, 24 sekundy

Po uruchomieniu urządzenie wykonuje trzy kolejne skany WiFi z przerwami. Po ich zakończeniu zapisuje jako bazę wykryte punkty dostępowe: SSID, BSSID, typ szyfrowania i siłę sygnału.

Szeregowe wyjście w tej fazie wygląda tak:

```
==============================================
 Travel WiFi Canary v1.0
 Passive 2.4 GHz awareness sensor
==============================================
[canary] setup done - starting baseline learning
[canary] baseline scan start (aps=0 score=0)
[canary] scan found 18 APs
[canary] baseline scan 1/3
[canary] baseline scan start (aps=18 score=0)
[canary] scan found 18 APs
[canary] baseline scan 2/3
[canary] baseline scan start (aps=18 score=0)
[canary] scan found 19 APs
[canary] baseline complete: 19 APs learned
  [00] MyHomeWifi                    aa:bb:cc:dd:ee:ff ch06 WPA2     -52 dBm
  [01] XFINITY                       11:22:33:44:55:66 ch01 WPA2     -71 dBm
  ...
[canary] STARTUP → NORMAL  (score=0  "")
```

Gdy dioda zmienia kolor z niebieskiego na zielony, urządzenie działa w pełni.

---

## Wykrywane zagrożenia

WiFi Canary monitoruje sześć wzorców zagrożeń. Każdy dodaje punkty do **wyniku pewności**, który steruje diodą. *Żaden pojedynczy wskaźnik nie jest uznawany za pewny*: model zbiera potwierdzające się sygnały przed eskalacją.

### 1. Serie deautentykacji i rozłączeń

**Podtypy 10 (rozłączenie) i 12 (deautentykacja) ramek zarządzających 802.11** są podstawowymi narzędziami ataków WiFi. Każde urządzenie może je wysłać, a klienci, którzy je odbiorą, zostaną odłączeni od punktu dostępowego.

W **trybie promiscuous** canary liczy te ramki według źródłowego adresu MAC w przesuwanym oknie **5 sekund**.

| Warunek | Dodane punkty |
|---|---|
| ≥ 8 ramek z jednego źródła w 5 s | +2 |
| ≥ 20 ramek z jednego źródła w 5 s | +4 |
| ≥ 5 rozgłoszeniowych ramek deautentykacji | +1 |

**Progi mają znaczenie**: klient przełączający się między punktami dostępowymi generuje kilka legalnych ramek. Narzędzia ataku potrafią wysyłać setki ramek na sekundę do celu. Okno 5 sekund i próg 8 ramek filtrują typowy szum roamingu, a wykrywają długie serie narzędzi takich jak `aireplay-ng`.

### 2. Otwarty klon znanej szyfrowanej sieci (evil twin)

**To wykrywanie o najwyższej pewności.** Atak evil twin często polega na:

1. Utworzeniu otwartej, niezabezpieczonej hasłem kopii znanego SSID WPA2.
2. Nadawaniu silniejszego sygnału niż prawdziwy punkt, aby klienci łączyli się automatycznie.

Po nauczeniu bazy nowy skan wykrywa SSID, które wcześniej korzystało tylko z WPA/WPA2/WPA3, a teraz jest oznaczone jako **OPEN**:

| Warunek | Dodane punkty |
|---|---|
| Ten sam SSID, wcześniej szyfrowany, teraz otwarty | +3 |
| BSSID nie występował w bazie | +1 |
| Sygnał klonu ≥ 10 dB silniejszy od znanego punktu | +1 |

Otwarty klon hotelowego WiFi, który jest o 10 dB silniejszy od prawdziwego punktu, to podręcznikowy przykład. *Ta kombinacja daje 5 punktów (Uwaga) w jednym cyklu skanowania.*

**Przykład wyjścia szeregowego**:

```
[canary] OPEN CLONE: SSID='MyHomeWifi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'MyHomeWifi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'MyHomeWifi'")
```

### 3. Brak oryginalnego szyfrowanego punktu i obecność otwartego klonu

Bardziej zaawansowany wariant: silniejszy klon przyciąga klientów, a prawdziwy punkt zostaje jednocześnie zablokowany przez deautentykację.

| Warunek | Dodane punkty |
|---|---|
| Zniknął szyfrowany punkt z bazy, pojawiła się pasująca otwarta sieć | +3 |

Obejmuje to sytuację, gdy prawdziwy punkt nadal nadaje, ale przegrywa konkurencję siły sygnału lub jest aktywnie zakłócany.

### 4. Obniżenie zabezpieczeń

Ten sam SSID co w bazie, ale zaobserwowany z szyfrowaniem słabszym niż zapisane.

| Warunek | Dodane punkty |
|---|---|
| WPA3 → WPA2 | +1 |
| WPA2 → WPA | +1 |
| Spadek o co najmniej 2 poziomy szyfrowania | +3 |

*Obniżenie zabezpieczeń do sieci otwartej obsługuje wykrywanie evil twin i przyznaje wyższe wyniki.* Ta kategoria obejmuje częściowe obniżenia, które mogłyby umknąć przy prostym porównaniu sieci otwartych i szyfrowanych.

### 5. Zduplikowany SSID od nieoczekiwanego dostawcy

Ten sam SSID i typ zabezpieczeń co punkt z bazy, lecz BSSID używa **innego OUI dostawcy** (pierwsze 3 bajty adresu MAC).

| Warunek | Dodane punkty |
|---|---|
| Inne OUI niż w punkcie z bazy o tym samym SSID | +1 |
| Klon jest też ≥ 10 dB silniejszy | +2 |

*Wynik jest celowo niski.* Sieci firmowe, systemy mesh i punkty dostępowe ISP często mają legalnie wiele BSSID o tym samym SSID od różnych dostawców. Ten sygnał powinien łączyć się z innymi przesłankami, a nie sam wywoływać alarm.

### 6. Zalewanie beaconami lub SSID

Liczy nowe SSID, których nie ma w bazie, pojawiające się w **przesuwanym oknie 30 sekund**.

| Warunek | Dodane punkty |
|---|---|
| ≥ 15 nowych SSID w 30 s | +2 |
| ≥ 30 nowych SSID w 30 s | +3 |

Ataki **zalewania beaconami** rozgłaszają tysiące fałszywych SSID, aby zmylić tabele skanowania lub zakłócić legalne beacony. Piętnaście nowych, nieznanych SSID w 30 sekund to nietypowe zdarzenie w większości środowisk.

---

## Model wyniku pewności

Wszystkie wykryte sygnały składają się na całkowity **wynik zagrożenia**, który steruje diodą:

| Zakres wyniku | Stan diody |
|---|---|
| 0–2 | Normalnie (zielony) |
| 3–5 | Uwaga (żółty) |
| 6+ | Alarm (czerwony, szybkie pulsowanie) |

### Spadek wyniku

Bez nowych zdarzeń wynik **spada o 1 punkt co 60 sekund**. To jedna z najważniejszych decyzji projektowych:

- Pojedyncza seria deautentykacji podnosi wynik do Uwaga, a po ustaniu ataku samoczynnie wraca do Normalnie w ciągu kilku minut.
- Trwający atak utrzymuje stan Alarm.
- Urządzenie resetuje się bez ingerencji i ponownego uruchamiania.

Oznacza to, że:
- **Krótkie anomalie** (roaming i chwilowe zmiany sieci sąsiadów) znikają same.
- **Trwające ataki** pozostają oznaczone.
- **Brak zmęczenia alarmami** przy pojedynczych, niepowtarzających się zdarzeniach.

### Reset przyciskiem

Przycisk GPIO 39 na Atom Lite wykonuje dwie czynności:

1. Wypisuje pełną aktualną tabelę AP na wyjście szeregowe, aby sprawdzić, co widzi urządzenie.
2. Ustawia wynik zagrożenia na 0 i natychmiast przywraca zielony stan, by obserwować nowy cykl skanowania od początku.

---

## Budowanie i flashowanie

### Wymagania

- **PlatformIO** (CLI lub rozszerzenie VS Code)
- **M5Stack Atom Lite** (lub ESP32 DevKit do testów)
- Kabel USB-C

### Flashowanie M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/esp32-wifi-canary.git
cd esp32-wifi-canary

# Budowanie i flashowanie
pio run -e atom-lite --target upload

# Otwórz monitor szeregowy z prędkością 115200 bodów
pio device monitor -b 115200
```

### Flashowanie uniwersalnego ESP32 DevKit

```bash
pio run -e esp32dev --target upload
```

Wersja DevKit korzysta z GPIO 2 (wbudowana dioda) i wypisuje pełny log szeregowy. Nie steruje NeoPixelem. Logika wykrywania jest identyczna jak dla Atom Lite.

### Struktura projektu

```
esp32-wifi-canary/
├── main.cpp              # Cała logika firmware
├── platformio.ini        # Środowiska kompilacji (atom-lite, esp32dev)
├── partitions_4mb.csv    # Tabela partycji flash 4 MB
└── README.md
```

Całe oprogramowanie układowe mieści się w **jednym pliku źródłowym C++**. Logika wykrywania nie wymaga zewnętrznych bibliotek, tylko frameworka ESP32 Arduino do skanowania WiFi, callbacków trybu promiscuous i sterowania NeoPixelem.

### Środowiska platformio.ini

```ini
[env:atom-lite]
platform = espressif32
board = m5stick-c
framework = arduino

[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
```

Środowisko `atom-lite` używa definicji płytki `m5stick-c` (ten sam układ ESP32-PICO-D4 i zgodne przypisanie pinów NeoPixel na GPIO 27).

---

## Opis wyjścia szeregowego

Urządzenie tworzy szczegółowe logi przy **115200 bodów**. Każda linia ma prefiks `[canary]`, co ułatwia filtrowanie.

### Sekwencja startowa

```
==============================================
 Travel WiFi Canary v1.0
 Passive 2.4 GHz awareness sensor
==============================================
[canary] setup done - starting baseline learning
[canary] baseline scan start (aps=0 score=0)
[canary] scan found 18 APs
[canary] baseline scan 1/3
...
[canary] baseline complete: 19 APs learned
  [00] MyHomeWifi                    aa:bb:cc:dd:ee:ff ch06 WPA2     -52 dBm
  [01] XFINITY                       11:22:33:44:55:66 ch01 WPA2     -71 dBm
[canary] STARTUP → NORMAL  (score=0  "")
```

### Zdarzenia wykrywania

```
[canary] normal scan start (aps=19 score=0)
[canary] scan found 21 APs
[canary] OPEN CLONE: SSID='HotelWiFi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'HotelWiFi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'HotelWiFi'")
```

### Zmiany wyniku

```
[canary] CAUTION → NORMAL  (score=2  "score decay")
[canary] NORMAL → ALERT    (score=6  "sustained deauth burst + open clone")
```

Log szeregowy pokazuje, co urządzenie zobaczyło, kiedy i dlaczego zmienił się wynik. To także **pasywny dziennik audytowy**, nawet gdy nikt nie patrzy na diodę.

---

## Uwagi o wykrywaniu i ograniczenia praktyczne

README otwarcie opisuje, czego urządzenie nie potrafi. Warto wyjaśnić te ograniczenia.

### Możliwe fałszywe alarmy

**Sieci firmowe i mesh** są głównym źródłem fałszywych alarmów. Duża sieć firmowa, hotel lub system mesh, taki jak Eero czy Google WiFi, może legalnie wykazywać:

- Wiele BSSID dla tego samego SSID i różne OUI dostawców.
- Różnice konfiguracji zabezpieczeń między pasmami.
- Znikające i pojawiające się punkty dostępowe podczas zmian w sieci mesh.

**Routery Airbnb i SOHO** z wieloma SSID dla pasm mogą również powodować różnice OUI, jeśli radia 2,4 i 5 GHz korzystają z kolejnych bloków MAC różnych dostawców.

*Chwilowe zmiany sieci sąsiadów*: szyfrowana sieć, która chwilowo znika ze skanu, a potem wraca z innymi parametrami (aktualizacja firmware, restart lub konfiguracja), może krótkotrwale uruchomić wykrywanie.

Wynik i jego spadek mają *ograniczać, a nie eliminować* fałszywe alarmy.

### Możliwe fałszywe wyniki negatywne

Dobrze przygotowany **atak evil twin**, który:

- Podszywa się pod dokładny BSSID prawdziwego punktu, więc OUI się zgadza.
- Używa identycznego typu zabezpieczeń i prawidłowej konfiguracji IE WPA2.
- Nadaje z siłą sygnału różniącą się o mniej niż 10 dB od prawdziwego punktu.

*Może nie zebrać wystarczającej liczby punktów, by osiągnąć próg Uwaga.* Deautentykacja potrzebna do odłączenia klientów dodałaby punkty, ale wyrafinowany atakujący ograniczający liczbę ramek może pozostać poniżej progu.

### Przerwa przy przełączaniu radia

**Radio ESP32 nie może jednocześnie działać w trybie promiscuous i aktywnie skanować punktów dostępowych.** Oprogramowanie przełącza te tryby. Dlatego **ramki deautentykacji podczas około 3-sekundowego skanu nie zostaną odebrane**. Atakujący mógłby zsynchronizować serie z oknem skanowania, ale musiałby znać harmonogram.

### Tylko 2,4 GHz

Radio ESP32 działa w paśmie 2,4 GHz. **Sieci 5 i 6 GHz nie są skanowane ani monitorowane.** Urządzenie nie wykryje evil twin działających tylko w paśmie 5 GHz.

### Pasywny zasięg

Wykrywanie deautentykacji wymaga odbioru ramek przez urządzenie. Daleki lub używający kierunkowej anteny atakujący albo atakujący klienta daleko od canary może nadawać zbyt słabo, by uruchomić liczniki.

---

## Zastosowania

### Podróże z poufną pracą

Canary zaprojektowano głównie z myślą o podróżach. Podłącz go do laptopa, portu USB w hotelu lub powerbanku i pozwól mu poznać otoczenie hotelu albo centrum konferencyjnego. Pojawienie się otwartego klonu hotelowego SSID, najczęstszego scenariusza ataku, wywoła co najmniej stan Uwaga.

### Kawiarnie i publiczne WiFi

Otwarte WiFi to częsty cel konfiguracji evil twin. Baza pozwala po przybyciu poznać legalny punkt kawiarni, a potem obserwować konkurencyjne SSID.

### Świadomość i edukacja bezpieczeństwa

Wyjście szeregowe pokazuje szczegółowy i czytelny zapis tego, co widzi urządzenie. Podczas szkolenia demonstracja serii deautentykacji na żywo i obserwowanie zmiany koloru diody działa lepiej niż prezentacja.

### Pasywny monitoring laboratorium

W domowym laboratorium lub małym biurze canary może działać jako stały monitor otoczenia. Dioda szybko pokazuje stan, a przycisk pozwala na żądanie wyświetlić aktualną tabelę sieci.

---

## Uwagi architektoniczne

### Dlaczego jeden wynik zamiast oddzielnych alarmów

Model łączy różne sygnały w jedną liczbę zamiast wyświetlać osobne kategorie alarmów. To celowy wybór interfejsu: urządzenie ma jedną diodę z trzema stanami. Oddzielne alerty wymagałyby ekranu lub aplikacji. *Wynik przekłada zaszumione, częściowo skorelowane sygnały na jeden użyteczny wskaźnik.*

### Dlaczego wynik spada

Bez spadku pojedynczy fałszywy alarm wymagałby ręcznego resetu przyciskiem. Przy obniżaniu wyniku co 60 sekund krótkie anomalie znikają po kilku minutach. **Dzięki temu canary działa bez nadzoru** w torbie, pokoju hotelowym lub samochodzie i wraca do normy po przejściowych zdarzeniach.

### Dlaczego trzy skany bazy

Jeden skan może pominąć punkt, który akurat nie nadawał, na przykład podczas przerwy albo chwilowego wyłączenia zasilania. *Trzy skany w około 24 sekundy dają pełniejszy obraz stabilnego otoczenia przed rozpoczęciem monitoringu.*

---

## Współtworzenie i status projektu

Projekt jest dostępny na [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary) na licencji do użytku pasywnego. Kod składa się z jednego pliku `main.cpp`, więc łatwo go czytać, audytować i rozwijać.

Osoby pracujące z PlatformIO i ESP32 mogą bez modyfikacji kompilować projekt dla Atom Lite i standardowego DevKit.

---

## Porównanie z innymi metodami monitorowania WiFi

| Metoda | Pasywna? | Bez danych logowania | Jedna dioda LED | Format podróżny |
|---|---|---|---|---|
| ESP32 WiFi Canary | ✅ | ✅ | ✅ | ✅ |
| Kismet (laptop) | ✅ | ✅ | ❌ (wymaga ekranu) | ❌ (ciężki) |
| WiFi Pineapple | ❌ (aktywna) | ❌ | ❌ | Częściowo |
| Bezprzewodowy IDS (firma) | ✅ | ✅ | ❌ (wymaga infrastruktury) | ❌ |
| Ręczne skanowanie (aplikacja telefonu) | Częściowo | ✅ | ❌ | ✅ |

Canary zajmuje określoną niszę: **ciągła świadomość otoczenia bez interakcji i bez sieci**, w formacie mieszczącym się przy kluczach lub w torbie na laptopa.

---

## Podsumowanie

ESP32 WiFi Canary robi jedną rzecz: obserwuje otoczenie 2,4 GHz i zmienia kolor, gdy coś wygląda podejrzanie. Nie jest pełnym bezprzewodowym systemem wykrywania włamań, narzędziem do przechwytywania pakietów ani analizatorem kryminalistycznym. To canary, pasywny czujnik zauważający, gdy otoczenie staje się niebezpieczne.

**Model wyniku pewności**, **spadek wyniku** i **trzyetapowa baza odniesienia** odpowiadają na problem fałszywych alarmów czujników otoczenia. Urządzenie może działać bez nadzoru w hotelu lub centrum konferencyjnym i sygnalizować istotne anomalie bez reagowania na normalne zmiany sieci.

Dla osób budujących przenośny zestaw bezpieczeństwa, pracujących w miejscach z niezaufaną infrastrukturą WiFi albo szukających praktycznego projektu ESP32 WiFi Canary jest wart popołudnia pracy i M5Stack Atom Lite za 15 USD.

**GitHub**: [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary)
