---
title: "Eye Spy: pasywny wykrywacz nadzoru i trackerów na ESP32"
date: 2026-06-07
lastmod: 2026-11-22
toc: true
draft: false
description: "Techniczne omówienie Eye Spy v1.1, pasywnego wykrywacza BLE i WiFi na ESP32, który wykrywa kamery, trackery, drony i powiązane sygnały."
genre: ["Narzędzia ochrony prywatności", "Kontrnadzór", "Bezpieczeństwo IoT", "Systemy wbudowane", "Badania bezpieczeństwa", "Bezpieczeństwo WiFi", "Bezpieczeństwo Bluetooth", "Projekty ESP32", "Bezpieczeństwo sprzętu", "Bezpieczeństwo open source"]
tags: ["Eye Spy", "ESP32", "M5Stack Atom Lite", "Wykrywanie nadzoru", "Kontrnadzór", "Wykrywanie BLE", "Skanowanie WiFi", "Wykrywanie AirTag", "Wykrywanie ALPR", "Flock Safety", "Wykrywanie kamer nasobnych", "Wykrywanie dronów", "OpenDroneID", "NimBLE", "NeoPixel", "SK6812", "PlatformIO", "C++", "Otwarte oprogramowanie", "Prywatność", "Pasywne BLE", "Tryb monitorowania", "Wykrywanie OUI", "Wykrywanie trackerów", "Kamera nasobna Axon", "Ray-Ban Meta", "Samsung SmartTag", "Tracker Tile", "Ukryta kamera", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/eye-spy-passive-surveillance-detector-esp32-2026/"
cover: "/img/cover/eye-spy-passive-surveillance-detector-esp32-2026.webp"
coverAlt: "Ilustracja małego urządzenia M5Stack Atom Lite otoczonego kolorowymi falami sygnału na ciemnogranatowym tle, symbolizująca wykrywanie nadzoru przez Bluetooth i WiFi."
coverCaption: ""
---

**Pasywny czujnik wielkości kciuka, który informuje, gdy coś cię obserwuje**

## Wprowadzenie: niewidoczny krajobraz nadzoru

W świecie fizycznym jest coraz więcej urządzeń, które obserwują, nagrywają i śledzą: czytniki tablic rejestracyjnych na skrzyżowaniach, kamery nasobne służb porządkowych, kamery w wynajmowanych lokalach, komercyjne trackery podobne do AirTagów ukryte w torbach lub samochodach oraz kamery monitoringu przy wejściach do sklepów. Większość tych urządzeń komunikuje się bezprzewodowo przez **Bluetooth LE** lub **WiFi**. *Większość tych komunikatów jest rozgłaszana w eterze, więc może je wykryć każdy, kto ma odpowiedni odbiornik.*

[**Eye Spy**](https://github.com/simeononsecurity/eye-spy) to narzędzie do pasywnego wykrywania nadzoru, które wykorzystuje właśnie ten fakt. Eye Spy działa na **M5Stack Atom Lite**, płytce deweloperskiej ESP32-PICO-D4 wielkości mniej więcej kostki cukru, i stale monitoruje pasma BLE i WiFi w poszukiwaniu elektronicznych sygnatur urządzeń nagrywających, kamer monitoringu, systemów **ALPR** (automatycznych czytników tablic rejestracyjnych), dronów i trackerów osobistych. Po wykryciu sygnału zmienia kolor diody RGB.

*Nie łączy się z żadnym urządzeniem i niczego nie nadaje.* Obserwuje, przyznaje punkty i świeci.

Ten artykuł to kompletne omówienie techniczne: wyjaśnia, co wykrywa Eye Spy, jak działa model oceny pewności, jak zaprojektowano silniki wykrywania, jak zbudować i wgrać oprogramowanie urządzenia oraz jakie są jego praktyczne ograniczenia.

**Wolisz nie budować urządzenia samodzielnie?** W sklepie STS Collective są dostępne **[detektory Eye Spy](https://stscollective.com/collections/eye-spy-passive-surveillance-detectors)** z wgranym oprogramowaniem, gotowe do użycia. Kod czytelnika **SIMEONONSECURITY** daje do 20% zniżki.

{{< stscollective-ad "eyespy" >}}

---

## Wskaźniki LED: cały interfejs użytkownika

Podobnie jak [ESP32 WiFi Canary: pasywne wykrywanie zagrożeń w paśmie 2,4 GHz](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/), Eye Spy używa tylko jednej diody NeoPixel RGB SK6812 podłączonej do GPIO 27 płytki M5Stack Atom Lite. Dioda stale pokazuje jeden z czterech poziomów zagrożenia:

| Kolor | Znaczenie | Zakres punktów |
|-------|-------------|---------------------|
| 🔵 Niebieski pulsujący | Uruchamianie / pierwszy skan | -- |
| 🟢 Zielony stały | Brak wykrytych urządzeń | 0–2 |
| 🟡 Żółty stały | Uwaga: w pobliżu może być urządzenie nagrywające | 3–5 |
| 🔴 Czerwony migający | Alarm: wykryto urządzenie nadzoru lub śledzące | 6+ |

**Jedno wykrycie o wysokiej pewności (kamera nasobna Axon, kamera Flock Safety, zgodny OUI ALPR lub AirTag) daje dość punktów, by po jednym cyklu wykrywania natychmiast zmienić diodę na czerwoną.** Kilka wykryć o średniej pewności sumuje punkty do poziomu żółtego i może łącznie doprowadzić do czerwonego.

---

## Sprzęt

### Główny wariant: M5Stack Atom Lite

| Element | Szczegóły |
|-----------|--------|
| Płytka | M5Stack Atom Lite |
| MCU | ESP32-PICO-D4 |
| Dioda | NeoPixel SK6812 na GPIO 27 |
| Przycisk | GPIO 39 (tylko wejście) |
| Pamięć flash | 4 MB |

Atom Lite to kompletna, samodzielna platforma. **Nie trzeba lutować, używać płytki stykowej ani dodawać zewnętrznych elementów.** Wystarczy podłączyć urządzenie przez USB.

### Zwykły ESP32 DevKit

Drugi profil kompilacji PlatformIO (`esp32dev`) obsługuje dowolny standardowy ESP32 DevKit ze zintegrowaną diodą na GPIO 2. Cała logika wykrywania działa tak samo. Ten wariant przydaje się podczas prac programistycznych i testowania logiki oraz przy wdrożeniu, gdy obudowa Atom Lite nie jest potrzebna.

---

## System punktacji

Eye Spy wykorzystuje **model oceny pewności**, który łączy sygnały ze wszystkich silników wykrywania w jedną liczbę całkowitą. Wynik określa stan diody (zielony, żółty lub czerwony) i podlega dwóm mechanizmom automatycznego zarządzania:

### Spadek punktacji

Bez nowych wykryć wynik spada o **1 punkt co 60 sekund**. Gdy oddalisz się od wykrytego urządzenia, dioda po kilku minutach wróci do zielonego stanu bez twojej ingerencji.

### Przerwa przed ponownym naliczeniem punktów

Każdy *typ* wykrycia ma **120-sekundową przerwę**, zanim ta sama źródłowa sygnatura będzie mogła ponownie dodać punkty. *Zapobiega to nieograniczonemu zwiększaniu wyniku przez jedno stale obecne urządzenie.* Kamera Flock Safety pozostająca w zasięgu doda +5 raz, a potem będzie mogła ponownie zwiększyć wynik po 120 sekundach.

Oba mechanizmy razem oznaczają, że:

- **Krótkotrwałe wykrycia** (na przykład samochód z AirTagiem, który przejeżdża) samoczynnie znikają.
- **Trwały nadzór** (na przykład stałe użycie kamer nasobnych) utrzymuje stan alarmu, dopóki pozostajesz w zasięgu.
- **Wielokrotne wykrywanie jednego urządzenia** nie powoduje niekontrolowanego wzrostu wyniku.

---

## Silniki wykrywania

{{< figure src="eye-spy-ble-wifi-detection-engines-overview.webp" alt="Diagram równoległych silników BLE i WiFi Eye Spy, które szukają AirTagów, kamer nasobnych, systemów ALPR i dronów, a następnie przekazują wyniki do modelu zagrożeń opartego na ocenie pewności" >}}

Eye Spy stale przełącza się między trzema fazami skanowania:

**Pasywne BLE (9 s) → skan WiFi (~3 s) → nasłuch promiscuous (5 s) → powtórz**

Eye Spy zatrzymuje BLE przed każdą operacją WiFi, aby prawidłowo współdzielić radio ESP32. BLE jest ponownie uruchamiane na początku każdego cyklu.

---

### Silnik 1: BLE, skanowanie pasywne

Skanowanie BLE korzysta z **NimBLE bez wysyłania żądań skanowania**. Urządzenie nasłuchuje pakietów rozgłoszeniowych BLE i nie wysyła odpowiedzi. *Dzięki temu Eye Spy jest elektronicznie niewidoczny dla szukanego sprzętu: urządzenie docelowe nie wykrywa pasywnego skanera.*

Aby ograniczyć fałszywe alarmy w zatłoczonych miejscach, urządzenia o sygnale słabszym niż **−90 dBm** są ignorowane.

#### Tabela wykrywania BLE

| # | Cel | Metoda wykrywania | Punkty |
|---|--------|-----------------|-------|
| 1 | **Kamera nasobna Axon** | OUI MAC BLE `00:25:df` (Axon: kamery nasobne, urządzenia Taser i sprzęt służb) | +5 🔴 |
| 2 | **Inteligentne okulary Ray-Ban Meta** | UUID usługi BLE `0xFD5F` | +5 🔴 |
| 3 | **BLE Flock Safety** | Nazwa urządzenia BLE zawiera `Flock`, `Penguin`, `Pigvision` lub `FS Ext Battery` | +5 🔴 |
| 4 | **Skimmer kart (HC-03/05/06)** | Dokładna nazwa BLE: moduły Bluetooth często spotykane w nakładkach na terminale płatnicze | +5 🔴 |
| 5 | **Apple AirTag** | Dane producenta `0x004C`, podtyp `0x12`/`0x1E` albo surowy ładunek `1E FF 4C 00` / `4C 00 12` | +4 🔴 |
| 6 | **Dron (OpenDroneID BLE)** | UUID usługi BLE `0xFFFA` albo ładunek danych usługi AD z kodem aplikacji `0x0D` | +4 🔴 |
| 7 | **Samsung SmartTag** | UUID usługi BLE `0xFD5A` | +3 🟡 |
| 8 | **Tracker Tile** | UUID usługi BLE `0xFEED` lub `0xFEEC` | +3 🟡 |
| 9 | **Węzeł MeshCore** | Prefiks nazwy BLE `MeshCore-` | +2 🟡 |
| 10 | **iBeacon (śledzenie w sklepach i obiektach)** | Dane producenta `0x004C 0x02 0x15`; używane w sklepach, na lotniskach i stadionach do śledzenia ruchu | +2 🟡 |
| 11 | **Nieznane trwałe urządzenie** | Niesklasyfikowany MAC BLE widziany co najmniej 3 razy w ciągu co najmniej 5 minut (wykrywanie zwiadowców i urządzeń śledzących) | +2 🟡 |

#### Ważne wykrycia BLE w szczegółach

**Kamera nasobna Axon (+5)**: Axon (wcześniej TASER International) produkuje jedne z najczęściej używanych kamer nasobnych dla służb porządkowych w Stanach Zjednoczonych. OUI `00:25:df` jest zarejestrowany na Axon i występuje w jego urządzeniach noszonych przez użytkowników. **Jedno wykrycie natychmiast osiąga próg alarmu.**

**Inteligentne okulary Ray-Ban Meta (+5)**: Współpraca Ray-Ban Meta obejmuje inteligentne okulary konsumenckie umożliwiające nagrywanie wideo i robienie zdjęć. UUID usługi BLE `0xFD5F` to charakterystyczny identyfikator rozgłoszeniowy tych urządzeń. *Są to produkty konsumenckie i mogą pojawiać się w zatłoczonych miejscach publicznych.* Warto zwrócić uwagę na każde wykrycie z tą punktacją, niezależnie od intencji osoby, która je nosi.

**Moduły Bluetooth w skimmerach kart (+5)**: HC-03, HC-05 i HC-06 to tanie moduły szeregowe Bluetooth, często znajdowane w nakładkach na terminale płatnicze i sprzęcie do skimmingu bankomatów. Wykrywanie dokładnie porównuje nazwę urządzenia ze znanymi domyślnymi nazwami oprogramowania tych modułów. **Czerwony alarm uzasadnia fizyczne sprawdzenie pobliskich terminali płatniczych.**

**Apple AirTag (+4)**: AirTagi rozgłaszają dane za pomocą zastrzeżonego protokołu Apple **Nearby Interaction**. Wykrywanie sprawdza nagłówek danych producenta (`0x004C` = Apple) oraz podtypy AirTagów (`0x12` dla zwykłego rozgłoszenia, `0x1E` dla zgłoszenia zagubionego przedmiotu). Wzorce surowego ładunku zapewniają dodatkową, niezależną metodę wykrywania.

**OpenDroneID BLE (+4)**: Standard **ASTM F3411 Remote ID**, przyjęty również przez amerykańską FAA dla dronów komercyjnych, określa sposób rozgłaszania tożsamości i położenia przez drony. Eye Spy szuka UUID usługi GATT `0xFFFA` (wyznaczonej usługi Remote ID) oraz kodu aplikacji `0x0D` w ładunku danych usługi AD. *Każdy pobliski dron komercyjny zgodny ze standardem aktywuje to wykrywanie.*

**Nieznane trwałe urządzenie (+2)**: To silnik **wykrywania urządzeń podążających za użytkownikiem**. Śledzi każdy adres MAC BLE niesklasyfikowany przez opisane wcześniej wykrycia. Punkty są przyznawane, gdy ten sam niesklasyfikowany adres MAC pojawi się co najmniej trzy razy w czasie pięciu minut lub dłużej. Tracker trwałości monitoruje równocześnie do 50 nieznanych adresów MAC, a wpisy usuwa po 30 minutach nieobecności. **Pomaga to wykrywać niestandardowe lub zmodyfikowane trackery, które nie pasują do znanych identyfikatorów UUID usług ani wzorców producentów.**

**iBeacon (+2)**: Sklepy, lotniska i stadiony stosują format iBeacon Apple (`0x4C 0x00 0x02 0x15`) do śledzenia ruchu urządzeń w przestrzeni. Wykrywanie reaguje na standardowy format rozgłoszeniowy bez względu na UUID: identyfikuje typ wdrożenia, a nie konkretny UUID. *Wykrycie oznacza, że prawdopodobnie przebywasz w miejscu, które aktywnie śledzi obecność urządzeń Bluetooth.*

---

### Silnik 2: skan WiFi, aktywne wyszukiwanie kanałów

Silnik skanowania WiFi korzysta ze standardowego interfejsu skanowania punktów dostępu ESP32, aby wykrywać pobliskie punkty dostępu i porównywać ich BSSID oraz SSID ze znanymi sygnaturami urządzeń nadzoru.

#### Tabela wykrywania WiFi

| # | Cel | Metoda wykrywania | Punkty |
|---|--------|-----------------|-------|
| 12 | **Kamera Flock Safety (OUI)** | BSSID pasuje do 22-wpisowej tabeli OUI Flock Safety (`d4:bb:e6`, `3c:61:05` i prefiksy FS-Ext-Battery) | +5 🔴 |
| 13 | **Kamera ALPR / LPR (OUI)** | BSSID pasuje do OUI `00:0e:58` firmy Motorola Solutions / Vigilant Solutions | +5 🔴 |
| 14 | **SSID ze słowami kluczowymi Flock** | SSID zawiera: `flock`, `flocksafety`, `fs ext`, `penguin` lub `pigvision` | +5 🔴 |
| 15 | **SSID ze słowami kluczowymi ALPR** | SSID zawiera: `alpr`, `lpr`, `vigilant`, `plateread`, `licenseplat`, `motorola` lub `automate` | +4 🔴 |
| 16 | **Producent kamer monitoringu (OUI)** | BSSID pasuje do tabeli 31 OUI kamer: Hikvision, Dahua, Axis, Ring, Nest, Arlo, Wyze, Reolink, FLIR, Amcrest, Vivotek, Hanwha, Mobotix lub Ubiquiti UniFi | +3 🟡 |
| 17 | **SSID ze słowami kluczowymi kamer** | SSID zawiera między innymi: `cam`, `ipcam`, `cctv`, `nvr`, `dvr`, `doorbell`, `surv`, `blink`, `lorex`, `protect` lub `genetec` | +2 🟡 |

#### Tabela OUI Flock Safety

Tabela `FLOCK_OUIS` z 22 wpisami to najbardziej szczegółowy wykaz w projekcie. Obejmuje:

- `d4:bb:e6`: OUI Flock Safety zarejestrowane przez IEEE.
- `3c:61:05`: OUI Flock Safety zarejestrowane przez IEEE.
- 20 dodatkowych prefiksów MAC zaobserwowanych w urządzeniach Flock FS-Ext-Battery i kamerach WiFi Flock.

Te 22 wpisy reprezentują zakresy sprzętowych adresów MAC zaobserwowane w działających systemach kamer ALPR Flock Safety. **Wykrywanie OUI jest niezależne od SSID**: kamera Flock z SSID bez słów kluczowych nadal otrzymuje +5 punktów, jeśli jej BSSID ma zgodny OUI.

OUI Flock Safety i Vigilant Solutions znajdują się w osobnych tabelach, dzięki czemu oba mogą niezależnie podnieść wynik podczas tego samego cyklu skanowania. *Lokalizacja, w której występują urządzenia obu producentów, może uzyskać +10 punktów w jednej rundzie skanowania WiFi.*

#### Tabela OUI producentów kamer monitoringu

Tabela z 31 OUI kamer monitoringu obejmuje głównych producentów kamer IP, których sprzęt można spotkać w sklepach, firmach i domach:

- **Firmy i zastosowania komercyjne**: Hikvision, Dahua, Axis, Vivotek, Hanwha (Samsung Techwin), Mobotix i Genetec.
- **Urządzenia konsumenckie i małe biura**: Ring, Nest, Arlo, Wyze, Reolink, Blink, Lorex i Amcrest.
- **Infrastruktura**: Ubiquiti UniFi (punkty dostępowe i kamery korzystają z nakładających się zakresów OUI) oraz FLIR.

Dopasowanie bez potwierdzenia słowem kluczowym daje +3 punkty, czyli poziom uwagi. Jeśli pasuje też SSID ze słowem kluczowym, ta sama sieć kamer otrzymuje +3 za OUI i +2 za SSID, co w jednym cyklu skanowania prowadzi do poziomu alarmu.

---

### Silnik 3: promiscuous WiFi, pasywne przechwytywanie ramek

Silnik promiscuous przełącza radio ESP32 w **tryb monitorowania** i przechwytuje surowe ramki zarządzające 802.11. Umożliwia to wykrywanie urządzeń, które nie rozgłaszają SSID, zwłaszcza dronów używających protokołu **Remote ID** przez **WiFi Neighbor Awareness Networking (NaN)**.

Podczas tej fazy radio **przeskakuje między kanałami** `{1, 6, 11, 3, 8, 13}` co 400 ms, aby zwiększyć zasięg odbioru ramek NaN dronów.

#### Tabela wykrywania promiscuous

| # | Cel | Metoda wykrywania | Punkty |
|---|--------|-----------------|-------|
| 18 | **Dron (OpenDroneID WiFi NaN)** | Ramka zarządzająca 802.11 skierowana do `51:6f:9a:01:00:00`: rozgłoszenie Remote ID ASTM F3411 | +4 🔴 |

**OpenDroneID WiFi NaN (+4)**: Standard ASTM F3411 wyznacza adres multiemisji `51:6f:9a:01:00:00` dla wszystkich ramek Remote ID WiFi NaN. Regulowane drony komercyjne, które transmitują pozycję i tożsamość przez WiFi, wysyłają ramki na ten adres. Eye Spy nasłuchuje ramek zarządzających kierowanych do tego adresu MAC multiemisji. Wykrywanie jest pasywne i niezawodne. *Operator drona musiałby wyłączyć Remote ID, aby je ominąć, co naruszałoby obowiązujące przepisy.*

To wykrywanie uzupełnia silnik OpenDroneID BLE (wykrycie nr 6). *Zależnie od sprzętu i konfiguracji dron może rozgłaszać dane przez BLE, WiFi lub oba protokoły.* Eye Spy obsługuje oba warianty.

---

## Harmonogram faz i zarządzanie radiem

```
Pasywne BLE (9 s) → skan WiFi (~3 s) → nasłuch promiscuous (5 s) → powtórz
```

ESP32-PICO-D4 ma **jedno współdzielone radio 2,4 GHz** obsługujące BLE i WiFi. Eye Spy zarządza nim w następujący sposób:

1. **Faza BLE** (9 sekund): aktywny stos NimBLE i skanowanie pasywne, bez transmisji żądań skanowania.
2. **Zatrzymanie BLE**: stos BLE jest jawnie zatrzymywany przed uruchomieniem WiFi.
3. **Skan WiFi** (~3 sekundy): aktywne skanowanie punktów dostępowych na wszystkich kanałach i dopasowywanie OUI oraz SSID.
4. **Nasłuch promiscuous** (5 sekund): pasywne przechwytywanie ramek 802.11 ze skokami między kanałami.
5. **Zatrzymanie WiFi**: WiFi jest wyłączane, a BLE uruchamiane ponownie na następny cykl.

Takie jawne zarządzanie fazami zapobiega konfliktom radiowym i zapewnia obu silnikom, BLE oraz WiFi, uporządkowany dostęp do radia w każdym cyklu.

---

## Wyjście szeregowe

Wszystkie linie zaczynają się od `[eyespy]`, co ułatwia ich filtrowanie. Monitor szeregowy działa z prędkością **115200 bodów**.

### Uruchamianie

```
[eyespy] Eye Spy v1.1 starting
[eyespy] init OK
```

### Zwykły cykl

```
[eyespy] BLE scan start
[eyespy] WiFi scan
[eyespy] WiFi done  score=0
[eyespy] promisc ON
[eyespy] status  score=0  CLEAR  phase=PROMISC  tracked=3
```

### Zdarzenia wykrywania

```
[eyespy] Flock-cam OUI d4:bb:e6  "Flock_CAM_0032"
[eyespy] +5 (Flock-cam-OUI)  score=5
[eyespy] WiFi done  score=5
[eyespy] promisc ON
[eyespy] status  score=5  CAUTION  phase=PROMISC  tracked=12
[eyespy] Axon-cam  RSSI=-62
[eyespy] +5 (Axon-cam)  score=10
[eyespy] status  score=10  ALERT  phase=BLE  tracked=12
[eyespy] decay  score=9
```

Pole `tracked=N` pokazuje liczbę unikalnych MAC BLE obecnie przechowywanych w trackerze trwałości. Ułatwia ocenę zagęszczenia urządzeń BLE w otoczeniu.

### Pola wyniku

Każda linia stanu zawiera:

- **score**: bieżący wynik zagrożenia.
- **state**: `CLEAR` / `CAUTION` / `ALERT`.
- **phase**: aktywny silnik (`BLE` / `WIFI` / `PROMISC`).
- **tracked**: liczba unikalnych MAC BLE w tabeli trwałości.

---

## Kompilacja i wgrywanie

### Wymagania

- **PlatformIO** (CLI lub rozszerzenie do VS Code).
- **M5Stack Atom Lite** lub dowolny ESP32 DevKit.
- Kabel USB-C.

### Zależności

PlatformIO instaluje je automatycznie:

```ini
lib_deps =
    adafruit/Adafruit NeoPixel @ ^1.15.1
    h2zero/NimBLE-Arduino @ ^1.4.3
```

**Adafruit NeoPixel** steruje diodą RGB SK6812. **NimBLE-Arduino** zapewnia stos pasywnego skanowania BLE. Jest preferowany zamiast domyślnej biblioteki BLE ESP32, ponieważ prawidłowo obsługuje tryb pasywny, nie wysyła żądań skanowania i zużywa mniej pamięci.

### Wgrywanie na M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/eye-spy.git
cd eye-spy

# Skompiluj i wgraj oprogramowanie dla Atom Lite
pio run -e atom-lite -t upload

# Otwórz monitor szeregowy z prędkością 115200 bodów
pio device monitor -b 115200
```

### Wgrywanie na zwykły ESP32 DevKit

```bash
pio run -e esp32dev -t upload
```

### Struktura projektu

```
eye-spy/
├── src/
│   └── main.cpp          # Cała logika oprogramowania urządzenia
├── platformio.ini         # Środowiska kompilacji (atom-lite, esp32dev)
├── partitions_4mb.csv     # Tabela partycji pamięci flash 4 MB
└── README.md
```

### platformio.ini

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

*Środowisko `atom-lite` korzysta z definicji płytki `m5stick-c`, która używa tego samego układu ESP32-PICO-D4 i zgodnego mapowania pinów NeoPixel na GPIO 27.*

---

## Uwagi dotyczące wykrywania i praktyczne ograniczenia

{{< figure src="eye-spy-m5stack-atom-lite-pocket-size.webp" alt="Ilustracja M5Stack Atom Lite Eye Spy w stylu fotografii. Urządzenie wielkości kostki cukru jest trzymane między dwoma palcami, by pokazać jego kompaktowy rozmiar" >}}

### Czego Eye Spy nie potrafi

**WiFi 5 GHz**: ESP32 to urządzenie **wyłącznie 2,4 GHz**. Kamery monitoringu, systemy ALPR i punkty dostępowe działające tylko w paśmie 5 GHz nie będą widoczne dla silników skanowania WiFi ani nasłuchu promiscuous. *Wiele nowoczesnych kamer IP obsługuje także 2,4 GHz, mimo zgodności z 5 GHz. Urządzenia działające wyłącznie w paśmie 5 GHz nie zostaną jednak wykryte.*

**Szyfrowane BLE**: niektóre zaawansowane produkty nadzoru szyfrują lub ukrywają swoje rozgłoszenia BLE. Eye Spy wykrywa urządzenia, które jawnie nadają rozpoznawalne sygnatury: OUI, UUID usług i dane producenta. *Urządzenia zmieniające adresy MAC, co jest coraz popularniejszą funkcją prywatności w trackerach konsumenckich, unikają wykrywania na podstawie MAC.* Tracker trwałości może je wykryć tylko wtedy, gdy zmiana adresu następuje rzadziej niż co pięć minut.

**Kamery przewodowe**: **Kamery IP podłączone przez Ethernet i niekorzystające z radia WiFi nie emitują sygnałów bezprzewodowych, które Eye Spy mógłby wykryć.** Ukryte kamery bez połączenia z siecią, nagrywające wyłącznie lokalnie, również nie mają sygnatur RF.

**Ograniczenia zasięgu**: W pomieszczeniach praktyczny zasięg odbioru silnych sygnałów przez antenę ESP32 wynosi **20–40 metrów**, a słabych lub zasłoniętych sygnałów jest mniejszy. *Urządzenia na granicy zasięgu lub za znaczącym ekranowaniem RF mogą nie uzyskać punktów albo nie przekroczyć progu RSSI −90 dBm.*

### Możliwe fałszywe alarmy

**Kamery konsumenckie w sąsiednich domach**: Kamery Ring, Nest, Wyze, Arlo i Reolink są powszechne na osiedlach, a ich OUI znajdują się w tabeli 31 kamer. *W okolicy mieszkalnej można spodziewać się żółtych wskazań uwagi (+3) z kamer przy dzwonkach sąsiadów.* Nie są to fałszywe alarmy w sensie technicznym, ponieważ urządzenie *rzeczywiście* wykrywa kamerę. Liczy się kontekst.

**Wdrożenia iBeacon w handlu**: duże sieci detaliczne instalują infrastrukturę iBeacon niemal w każdym sklepie. *Wizyta w galerii handlowej lub supermarkecie prawdopodobnie wywoła wykrycie iBeacon (+2).* Urządzenie działa prawidłowo: infrastruktura śledzenia w sklepach naprawdę tam jest.

**Infrastruktura Ubiquiti UniFi**: Punkty dostępowe UniFi znajdują się w tabeli OUI kamer, ponieważ Ubiquiti produkuje sprzęt sieciowy i kamery bezpieczeństwa korzystające z nakładających się zakresów OUI. *Sieć korzystająca z urządzeń UniFi uzyska +3 za dopasowania OUI w silniku skanowania WiFi.*

**Samsung SmartTag i urządzenia konsumenckie**: UUID SmartTag (`0xFD5A`) to usługa zarejestrowana przez firmę Samsung. *SmartTagi są trackerami konsumenckimi mającymi legalne, osobiste zastosowania.* Obecność pobliskiego SmartTaga wywoła to wykrycie.

### Praktyczne znaczenie poziomów punktacji

| Wynik | Prawdopodobna sytuacja w rzeczywistym świecie |
|-------|-----------------------------|
| 6–10 (🔴) | Wiarygodne wykrycie o wysokiej pewności: kamera Axon w odległości około 30 m, kamera Flock Safety ze zgodnym OUI, potwierdzony wzorzec śledzenia przez AirTag albo dron nadający Remote ID |
| 3–5 (🟡) | Kilka trackerów konsumenckich, punkty za kamery sąsiadów, możliwa kamera Flock albo pojedyncze wykrycie OpenDroneID |
| 0–2 (🟢) | Nie wykryto istotnych sygnatur nadzoru; występuje zwykły ruch urządzeń konsumenckich, ale poniżej progu |

---

## Porównanie z podobnymi projektami

Eye Spy koncentruje się na nadzorze fizycznym w otoczeniu, a [ESP32 WiFi Canary: pasywne wykrywanie zagrożeń w paśmie 2,4 GHz](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/) wykrywa ataki WiFi na warstwie sieciowej wymierzone we własne urządzenia. *To uzupełniające się narzędzia obsługujące różne modele zagrożeń.*

| Możliwość | Eye Spy | ESP32 WiFi Canary |
|------------|---------|------------------|
| Wykrywanie AirTagów i trackerów | ✅ | ❌ |
| Wykrywanie kamer ALPR / Flock | ✅ | ❌ |
| Wykrywanie kamer nasobnych | ✅ | ❌ |
| Wykrywanie dronów (Remote ID) | ✅ | ❌ |
| Wykrywanie złośliwych punktów dostępu typu evil twin | ❌ | ✅ |
| Wykrywanie ataków deautoryzacji | ❌ | ✅ |
| Wykrywanie obniżenia poziomu zabezpieczeń | ❌ | ✅ |
| Uczenie się wartości bazowych | ❌ | ✅ |
| Pasywne BLE | ✅ | ❌ |
| Ta sama platforma sprzętowa | ✅ | ✅ |

Oba projekty działają na tym samym sprzęcie M5Stack Atom Lite, korzystają z tych samych wskaźników LED oraz systemu kompilacji PlatformIO. Aby monitorować otoczenie fizyczne i sieciowe, możesz wgrać każdy projekt na osobny moduł Atom Lite i nosić oba urządzenia.

Eye Spy uzupełnia również [projekt wykrywania Flock You](https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/) dla osób szczególnie zainteresowanych infrastrukturą nadzoru ALPR.

---

## Zastosowania

### Świadomość otaczającego nadzoru

Eye Spy jest przeznaczony przede wszystkim dla osób, które chcą wiedzieć o infrastrukturze nadzoru w najbliższym otoczeniu. Podczas spaceru po osiedlu, przejazdu obok skrzyżowania lub udziału w wydarzeniu publicznym Eye Spy zamienia złożoną analizę RF w **jeden stan diody widoczny w czasie rzeczywistym**.

### Wykrywanie śledzenia przez AirTag

Śledzenie za pomocą AirTagów jest udokumentowanym problemem. **Silnik wykrywania urządzeń podążających za użytkownikiem** w Eye Spy (nieznany, trwały adres MAC BLE widziany co najmniej 3 razy w ciągu 5 minut lub dłużej) ma wykrywać zmodyfikowane lub niestandardowe trackery, które nie odpowiadają znanemu formatowi rozgłoszeniowemu Apple. W połączeniu z bezpośrednim wykrywaniem AirTagów zapewnia **dwie niezależne metody wykrycia trackera, który za tobą podąża**.

### Sprawdzanie wynajmowanego lokalu lub pokoju hotelowego

Uruchomienie Eye Spy po wejściu do nowego pokoju hotelowego lub wynajmowanego lokalu pozwala wstępnie wykryć nieoczekiwane urządzenia BLE i WiFi. SSID zawierające słowa kluczowe kamer lub OUI nadzoru znalezione podczas skanowania WiFi dodaje punkty uwagi. *To nie zastępuje dokładnego skanowania RF*, ale dodaje pasywną warstwę kontroli do oględzin pomieszczenia.

### Wdrożenia ALPR i badania prywatności

Badacze dokumentujący infrastrukturę nadzoru, dziennikarze pracujący w obserwowanych miejscach i obrońcy prywatności mogą używać Eye Spy jako niedrogiego, przenośnego urządzenia wykrywającego. Wyjście szeregowe rejestruje każde wykrycie wraz z RSSI, więc urządzenie nadaje się do prostego gromadzenia danych.

### Bezpieczeństwo w podróży

Podobnie jak WiFi Canary, Eye Spy ma format odpowiedni do podróży. Atom Lite mieści się w kieszeni lub można go przypiąć do torby. W czasie podróży przez lotniska, stacje kolejowe lub wydarzenia publiczne z intensywnym nadzorem zapewnia ciągłe, pasywne monitorowanie bez konieczności obsługi.

---

## Uwagi dotyczące architektury

### Dlaczego pasywne BLE ma znaczenie

Wybór pasywnego skanowania BLE bez wysyłania żądań ma istotne konsekwencje dla bezpieczeństwa. Podczas standardowego skanowania BLE skaner nadaje pakiet **SCAN_REQ**, aby poprosić każde urządzenie rozgłaszające o dodatkowe dane. *Aktywne skanowanie BLE jest więc widoczne dla obu urządzeń*: skanowane urządzenie widzi adres skanera w żądaniu.

Tryb pasywny NimBLE nasłuchuje tylko nierozgłaszanych kierunkowo pakietów reklamowych (ADV_IND, ADV_NONCONN_IND, ADV_SCAN_IND) i nigdy nie wysyła SCAN_REQ. **Eye Spy nie nadaje niczego przez BLE podczas skanowania.** Wykryta kamera nasobna Axon, urządzenie Flock lub AirTag nie może zaobserwować skanera ani na niego zareagować.

### Projekt trackera trwałości

Tracker nieznanych urządzeń przechowuje do **50 adresów MAC BLE** wraz z czasem pierwszego i ostatniego wykrycia. Wykrywanie uruchamia się, gdy dany MAC pojawi się co najmniej trzy razy w okresie trwającym minimum pięć minut.

Limit 50 wpisów i usuwanie danych po 30 minutach to decyzje inżynieryjne, które równoważą czułość wykrywania z ograniczoną pamięcią RAM ESP32. *W gęstym środowisku BLE (transporcie publicznym, na konferencji lub w galerii handlowej) tabela może szybko zapełnić się urządzeniami konsumenckimi.* Próg RSSI −90 dBm odfiltrowuje odległe urządzenia i koncentruje tracker na pobliskich, trwałych źródłach.

### Współdziałanie spadku punktacji i przerwy

**120-sekundowa przerwa przed ponownym naliczeniem punktów** zapobiega ciągłemu zwiększaniu wyniku przez urządzenie stale pozostające w zasięgu podczas każdego dziewięciosekundowego cyklu BLE. Bez tej przerwy jedna kamera Flock dodawałaby +5 co 15 sekund i w kilka minut osiągnęłaby setki punktów.

**Spadek wyniku o 1 punkt co 60 sekund** zmniejsza punktację po opuszczeniu zasięgu przez urządzenie, jeśli przerwa minęła i nie doszło do ponownego wykrycia. *Pojedyncze wykrycie za +5 punktów, które się nie powtarza, spadnie do zera w pięć minut.* Urządzenie wraca wtedy do stanu spokoju odpowiedniego dla typowego przemieszczania się.

---

## Współtworzenie i stan projektu

Eye Spy jest dostępny na licencji Apache-2.0 pod adresem [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy).

Możliwe kierunki rozwoju:

- **Dodawanie wpisów OUI**: rozszerzanie tabel OUI Flock Safety i kamer o nowe adresy MAC sprzętu udokumentowane w terenie.
- **Dodawanie UUID usług BLE**: nowe inteligentne okulary, kamery i trackery wprowadzają nowe identyfikatory UUID.
- **Dostosowanie trackera trwałości**: limit 50 wpisów, próg 3 wykryć i okno 5 minut to stałe, które można zmienić.
- **Rejestrowanie danych szeregowych**: format wyjścia szeregowego ułatwia analizę programową. Zewnętrzny rejestrator mógłby agregować zdarzenia z wielu urządzeń Eye Spy.

Oprogramowanie sprzętowe znajduje się w jednym pliku `main.cpp` w katalogu `src/`, więc łatwo je czytać, audytować i modyfikować.

---

## Podsumowanie

Eye Spy rozwiązuje wąski, ale istotny problem: w otoczeniu fizycznym jest coraz więcej urządzeń nadzoru, a większość z nich nadaje wykrywalne sygnatury RF. **M5Stack Atom Lite za 15 USD z oprogramowaniem Eye Spy staje się ciągłym skanerem otoczenia**, który zamienia złożoną analizę pakietów BLE i wyszukiwanie OUI WiFi w pojedynczą diodę RGB.

Model oceny pewności odzwierciedla realistyczną wagę zagrożeń: kamera nasobna Axon w pobliżu działań służb otrzymuje +5 i natychmiast zapala czerwone światło; komercyjny iBeacon otrzymuje +2 i zwiększa świadomość sytuacji bez samodzielnego wywoływania fałszywego alarmu. Spadek punktacji i przerwy przed ponownym naliczeniem ograniczają alarmy z powodu przejściowych lub trwałych sygnałów niskiego poziomu.

Do pracy kontrnadzorczej, ochrony w podróży, wykrywania AirTagów lub po prostu sprawdzania, czy coś w pobliżu cię obserwuje, Eye Spy jest praktycznym, pasywnym narzędziem open source, które warto mieć w wyposażeniu specjalisty ds. bezpieczeństwa.

**GitHub**: [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy)

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Kup detektory Eye Spy i oszczędź 20%
{{< /centerbutton >}}
