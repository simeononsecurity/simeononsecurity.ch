---
title: "Flock-You Detection: Przewodnik po konfiguracji systemu antynadzorczego"
date: 2026-05-24
toc: true
draft: false
description: "Kompleksowy przewodnik techniczny po projekcie open-source Flock-You do wykrywania kamer ALPR Flock Safety za pomocą sprzętu opartego na ESP32. Zawiera instrukcje konfiguracji, szczegóły oprogramowania i opcje zakupu."
genre: ["Sprzęt zabezpieczający", "Antynadzór", "Technologia prywatności", "Projekty open source", "Programowanie ESP32", "Monitorowanie WiFi", "Narzędzia prywatności", "Prawa cyfrowe", "Modyfikacje sprzętu", "Bezpieczeństwo sieci"]
tags: ["Projekt Flock-You", "Wykrywanie ALPR", "ESP32-S3", "Wykrywanie WiFi OUI", "Sprzęt do antynadzoru", "Wykrywanie Flock Safety", "Bezpieczeństwo open source", "Sprzęt prywatności", "M5 Atom Lite", "OUI-SPY", "mesh-detect v2", "Tryb promiscuous WiFi", "Monitorowanie 802.11", "Colonel Panic Tech", "STS Collective", "Urządzenia prywatności", "Wykrywanie nadzoru", "Skanowanie WiFi", "Projekt GitHub", "colonelpanichacks", "Firmware ESP32", "Przewodnik konfiguracji sprzętu", "Narzędzia DIY do prywatności", "Monitorowanie sieci", "Baza danych OUI", "Wykrywanie sond wieloznacznych", "Analiza ramek", "Wykrywanie kamer ALPR", "Technologia prywatności", "Sprzęt wykrywający", "Arduino ESP32", "Platform.io", "Systemy wbudowane", "Wykrywanie RF", "Przetwarzanie sygnałów", "Inżynieria prywatności", "Technologia antynadzorcza", "Badania bezpieczeństwa", "Rzecznictwo na rzecz prywatności", "Otwarty sprzęt", "Ochrona prywatności", "Firmware wykrywający", "Wykrywanie mobilne", "Projekty prywatności", "Porównanie sprzętu"]
cover: "/img/cover/flock-you-detection-project-counter-surveillance-hardware-guide-2026.webp"
coverAlt: "Ilustracja przedstawiająca urządzenie oparte na ESP32 na pierwszym planie, skanujące sygnały WiFi. Kolorowe fale reprezentują różne poziomy siły sygnału na tle ciemnego tła."
coverCaption: "Rozwiązania sprzętowe open-source do wykrywania kamer nadzorczych ALPR"
canonical: "https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/"
---

**Kompletny przewodnik techniczny dotyczący budowy i użytkowania urządzeń wykrywających Flock-You**

## Wprowadzenie: Antynadzór open source

**Projekt Flock-You** to **inicjatywa open-source, napędzana przez społeczność**, mająca na celu wykrywanie i mapowanie infrastruktury nadzorczej ALPR firmy Flock Safety. Hostowany na GitHub pod adresem **colonelpanichacks/flock-you**, projekt ten wykorzystuje przystępny cenowo sprzęt oparty na ESP32 do identyfikacji kamer Flock za pomocą ich **sygnatur sieci WiFi**.

Ten kompleksowy przewodnik obejmuje wszystko, od **metodologii technicznej** wykrywania Flock po **szczegółowe instrukcje konfiguracji** dla trzech platform sprzętowych, **instalacji oprogramowania** i **informacji o zakupie od autoryzowanych sprzedawców**. Niezależnie od tego, czy jesteś orędownikiem prywatności, badaczem bezpieczeństwa, czy zatroskowanym obywatelem, ten przewodnik umożliwi Ci zbudowanie lub zakup własnego urządzenia wykrywającego.

Aby dowiedzieć się, dlaczego ta technologia jest ważna i poznać szerszy krajobraz nadzoru, przeczytaj nasz artykuł towarzyszący: **[Nadzór kamerami Flock Safety: Powszechność, obawy o prywatność i strategie ochrony](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

Chcesz zobaczyć, gdzie kamery Flock zostały już zmapowane? **[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** to narzędzie open-source, które nanosi na mapę ponad 40 000 podejrzanych kamer Flock Safety na całym świecie, korzystając z danych WiGLE WiFi i odcisków palców OUI, aktualizowanych codziennie. Źródło na **[GitHub](https://github.com/simeononsecurity/flock-finder)**.

______

## Zrozumienie metodologii wykrywania Flock-You

### Podstawy techniczne

Kamery Flock Safety zawierają **wbudowane moduły WiFi** do łączności i zdalnego zarządzania. Moduły te nadają identyfikowalne sygnatury sieciowe wykrywalne przez urządzenia działające w **trybie monitorowania promiscuous WiFi**. Projekt Flock-You wykorzystuje tę właściwość poprzez:

#### 1. Wykrywanie WiFi OUI (Organizationally Unique Identifier)

Każdy interfejs sieciowy ma **adres MAC** składający się z:
- **Pierwsze 3 bajty (24 bity)**: OUI, który identyfikuje producenta
- **Ostatnie 3 bajty**: Identyfikator specyficzny dla urządzenia

Badacze **@NitekryDPaul** i społeczność **DeFlockJoplin** odkryli **31 specyficznych OUI** konsekwentnie obecnych we wdrożeniach kamer Flock Safety:

```
Primary Espressif OUIs (ESP32-based modules):
D4:AD:FC - Espressif Inc. (Common ESP32-S3)
AC:67:B2 - Espressif Inc. (ESP32-WROOM)
84:F3:EB - Espressif Inc. (ESP32-S3 variants)
B4:E6:2D - Espressif Inc. (ESP32-C3)
CC:DB:A7 - Espressif Inc. (ESP32-based)
24:0A:C4 - Espressif Inc. (ESP32-SOLO)
30:AE:A4 - Espressif Inc. (ESP32-WROVER)
94:B9:7E - Espressif Inc. (ESP32-based)
A4:CF:12 - Espressif Inc. (ESP32-S2)
C0:49:EF - Espressif Inc. (ESP32-C6)

Additional OUIs identified in Flock deployments:
[... 21 additional manufacturer OUIs ...]
```

Gdy urządzenie wykrywające skanuje ruch WiFi w trybie promiscuous, **identyfikuje każde urządzenie nadające ramki z tymi OUI**.

#### 2. Wykrywanie żądań sondowania wieloznacznego

Kamery Flock okresowo wysyłają **żądania sondowania wieloznacznego** w poszukiwaniu dostępnych sieci. Mają one charakterystyczne cechy:

- **Ramka zarządzania 802.11**: Typ=0, Podtyp=4
- **Element informacyjny SSID**: Długość=0 (pusta/wieloznaczna)
- **Struktura ramki**: Przewidywalny wzorzec w synchronizacji sond
- **IE specyficzne dla dostawcy**: Dodatkowe wskaźniki w ładunku ramki

Oprogramowanie wykrywające analizuje te **wzorce żądań sondowania**, aby zwiększyć pewność identyfikacji kamery Flock ponad proste dopasowanie OUI.

#### 3. Monitorowanie WiFi w trybie promiscuous

Standardowa operacja WiFi odbiera tylko ramki zaadresowane do Twojego urządzenia. **Tryb promiscuous** przechwytuje wszystkie ramki WiFi w zasięgu:

- **Struktura ramki 802.11**: Analiza pól addr1, addr2, addr3
- **Ramki zarządzania**: Żądania sondowania, ramki beacon, żądania powiązania
- **Ramki danych**: Ujawniają wzorce zachowania sieci
- **Ramki sterowania**: ACK, RTS, CTS dostarczają informacji o synchronizacji

Mikrokontrolery ESP32 obsługują tryb promiscuous poprzez **esp_wifi API**, umożliwiając tworzenie niskokosztowego sprzętu wykrywającego.

#### 4. Analiza siły sygnału

Urządzenia wykrywające mierzą **RSSI (Received Signal Strength Indicator)**, aby:
- **Szacować odległość** do wykrytych kamer
- **Triangulować lokalizacje** za pomocą wielu pomiarów
- **Filtrować fałszywe alarmy** na podstawie oczekiwanych charakterystyk sygnału
- **Tworzyć mapy cieplne** gęstości kamer

### Dokładność wykrywania i fałszywe alarmy

Metodologia Flock-You osiąga wysoką dokładność:

- **Wskaźnik prawdziwych pozytywów**: ~95% dla potwierdzonych kamer Flock w zasięgu
- **Wskaźnik fałszywych pozytywów**: ~5-10% w zależności od środowiska
- **Zasięg wykrywania**: 15-90 metrów w zależności od przeszkód i anteny
- **Ocena pewności**: Analiza wieloczynnikowa zmniejsza liczbę fałszywych alarmów

**Typowe źródła fałszywych pozytywów**:
- **Płytki deweloperskie ESP32** używane w innych urządzeniach IoT
- **Komercyjne produkty oparte na ESP32** (inteligentny dom, czujniki)
- **Inne kamery nadzorcze** używające podobnych komponentów
- **Sprzęt do testowania WiFi** obsługiwany przez techników

**Strategie łagodzenia**:
- **Wykrywanie wielosygnaturowe**: Łączenie OUI + wzorzec sondy + weryfikacja fizyczna
- **Korelacja lokalizacji**: Wzajemne odwołania do znanych lokalizacji kamer
- **Potwierdzenie wizualne**: Inspekcja fizyczna po wykryciu elektronicznym
- **Baza danych społeczności**: Weryfikacja wykryć oparta na zbiorowej mądrości

______

## Porównanie platform sprzętowych

Dostępne są trzy główne platformy do wykrywania Flock-You, każda z wyraźnymi zaletami:

### Tabela przeglądu platform

| Funkcja | DIY ESP32 | M5 Atom Lite (Pre-Flashed) | OUI-SPY |
|---------|-----------|---------------------------|---------|
| **Producent** | DIY / Wielu dostawców | STS Collective | Colonel Panic Tech |
| **Cena** | $5-12 | $39.99 | $85 |
| **Procesor** | ESP32-WROOM | ESP32-PICO | ESP32-S3 |
| **Gotowy do użycia** | Nie (budowa DIY) | Tak (wstępnie wgrane oprogramowanie) | Tak (tryb wielofunkcyjny) |
| **Wyświetlacz** | Opcjonalny | Dioda RGB LED (matryca 5×5) | Brak |
| **Bateria** | Opcjonalna | Zewnętrzna zalecana | Nie dołączona |
| **GPS** | Opcjonalny | Nie | Nie |
| **Alarmy** | Brzęczyk + LED | Dioda RGB LED (niebieski=wykrycie) | Zintegrowany brzęczyk |
| **Rejestrowanie danych** | Opcjonalne | Nie | Nie |
| **Obudowa** | Druk 3D lub brak | Kompaktowy moduł plastikowy | Brak (gołe PCB) |
| **Oprogramowanie** | Ręczne wgrywanie | Wstępnie załadowane FlockYou | Tryb wielofunkcyjny (4 oprogramowania) |
| **Najlepszy dla** | Entuzjastów DIY, nauki | Budżetowe rozwiązanie gotowe do użycia | Wykrywanie wielofunkcyjne |
| **Trudność konfiguracji** | Średnia-zaawansowana | Plug-and-play | Plug-and-play |
| **Waga** | 20-50g (różna) | 18g (gołe) | ~40g |
| **Wymiary** | Różne | 24×24×14mm | Płytka PCB |

### Szczegółowa analiza platform

#### 1. Budowa DIY ESP32 ($5-12)

**Przegląd**: Najbardziej przystępna cenowo opcja wykorzystująca standardowe płytki deweloperskie ESP32 z oprogramowaniem open-source.

**Specyfikacje sprzętowe**:
- **Mikrokontroler**: ESP32-WROOM-32 lub podobny (dwurdzeniowy, 240MHz)
- **WiFi**: 802.11 b/g/n, zdolny do trybu promiscuous
- **Pamięć**: 520KB SRAM, 4MB+ Flash
- **Wyświetlacz**: Opcjonalny (wbudowana dioda LED wystarczy)
- **Zasilanie**: Zasilanie przez USB lub powerbank
- **Brzęczyk**: Opcjonalny pasywny moduł brzęczyka (KY-006)
- **Wskaźniki**: Wbudowana dioda LED + opcjonalny brzęczyk
- **Rozszerzalność**: Przyjazny dla płytki stykowej, łatwe modyfikacje

**Oprogramowanie**: Fork open-source na **simeononsecurity/flock-you-esp32**:
- Zmodyfikowany dla standardowego sprzętu ESP32 (GPIO 25, 2, 17)
- Melodia startowa Super Mario Bros. (potwierdza działanie brzęczyka)
- Dwa szybkie rosnące sygnały dźwiękowe przy nowym wykryciu
- Sygnały bicia serca co 10 sekund podczas aktywnego śledzenia
- Obsługa pulpitu Flask do wardriving GPS
- Eksport do formatów JSON, CSV, KML

**Opcje budowy**:
- **Tylko LED ($5)**: Gołe ESP32 + kabel USB, wyłącznie informacja zwrotna wizualna
- **Płytka stykowa ($9-11)**: Dodaj pasywny brzęczyk + płytkę stykową + kabelki, alarmy dźwiękowe
- **Z obudową ($10-12)**: Dodaj obudowę drukowaną 3D z pokrywą zatrzaskową

**Zalety**:
- ✅ Najtańsza opcja (85-95% oszczędności kosztów w porównaniu z OUI-SPY)
- ✅ Całkowicie open-source i modyfikowalny
- ✅ Używa powszechnie dostępnych płytek ESP32
- ✅ Edukacyjny, uczy systemów wbudowanych
- ✅ Obszerna dokumentacja i przewodniki
- ✅ Dostępne pliki obudowy do druku 3D
- ✅ **Taka sama dokładność wykrywania jak urządzenia premium**

**Wady**:
- ❌ Wymaga montażu DIY (bezlutowa płytka stykowa lub obudowa 3D)
- ❌ Wymagane ręczne wgrywanie oprogramowania
- ❌ Brak zintegrowanej baterii (zasilanie USB lub zewnętrzny powerbank)
- ❌ Tylko podstawowa informacja dźwiękowa (bez wyświetlacza)
- ❌ Potrzeba czasu na pozyskanie komponentów

**Najlepszy dla**: Twórców, studentów, orędowników prywatności z ograniczonym budżetem, osób chcących się dowiedzieć, jak działa wykrywanie, tych, którzy lubią projekty DIY.

**Zakup komponentów**:
- **Amazon**: Wyszukaj "ESP32 DevKit" lub "ESP32 Breadboard Kit"
- **AliExpress/eBay**: Dostępne rabaty przy zakupie hurtowym
- **Adafruit**: Wyselekcjonowane części jakościowe z samouczkami

**Zasoby konfiguracji**:
- **Repozytorium GitHub**: [github.com/simeononsecurity/flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)
- **Przewodnik budowy**: Bezlutowy montaż w 10-15 minut
- **Pliki obudowy**: Projekt parametryczny OpenSCAD + pliki STL

---

#### 2. M5 Atom Lite wstępnie wgrany przez STS Collective ($39.99)

**Przegląd**: Wstępnie wgrane kompaktowe urządzenie wykrywające, gotowe do użycia po wyjęciu z pudełka.

**Specyfikacje sprzętowe**:
- **Mikrokontroler**: ESP32-PICO-D4 (dwurdzeniowy, 240MHz)
- **WiFi**: 802.11 b/g/n, zdolny do trybu promiscuous
- **Pamięć**: 520KB SRAM, 4MB Flash
- **Wyświetlacz**: Matryca diod RGB LED 5×5 (WS2812C NeoPixel)
- **Zasilanie**: 5V przez USB-C lub złącze Grove
- **Bateria**: Nie dołączona (zalecany zewnętrzny powerbank USB)
- **Wskaźnik**: Programowalna dioda RGB LED (niebieski=wykrycie)
- **Przyciski**: 1 programowalny przycisk
- **I/O**: Złącze Grove do rozbudowy
- **Rozmiar**: Ultrakompaktowy 24×24×14mm
- **Obudowa**: Trwały moduł plastikowy

**Oprogramowanie**: Niestandardowy port FlockYou przez STS Collective (zastrzeżony):
- Wstępnie załadowany i gotowy do użycia
- Niebieski alarm LED przy wykryciu kamery Flock
- Oparty na badaniach colonelpanichacks FlockYou
- Nie wymaga konfiguracji ani wgrywania oprogramowania
- Prosta operacja plug-and-play
- Opcjonalna obsługa pulpitu

**Zalety**:
- ✅ Wstępnie wgrane, nie wymaga konfiguracji technicznej
- ✅ Przystępne cenowo rozwiązanie gotowe do użycia
- ✅ Niezwykle kompaktowe i przenośne
- ✅ Sprawdzona platforma sprzętowa
- ✅ Prosta niebieska dioda LED = wykrycie
- ✅ Zasilanie przez USB-C (samochód, powerbank, laptop)
- ✅ Wsparcie techniczne dostawcy
- ✅ Regularna cena $99.99, w sprzedaży $39.99

**Wady**:
- ❌ Brak zintegrowanej baterii (potrzebuje zasilania USB)
- ❌ Ograniczony wyświetlacz (tylko dioda RGB LED, bez ekranu)
- ❌ *Oprogramowanie jest zastrzeżone, chwilowo nie jest open-source*
- ❌ Brak rejestrowania danych bez połączenia z komputerem
- ❌ Pojedynczy przycisk ogranicza funkcjonalność

**Najlepszy dla**: Użytkowników chcących natychmiastowego wykrywania bez pracy DIY, priorytetu przenośności, tych, którzy są zadowoleni z prostej informacji zwrotnej LED, kupujących świadomych budżetu, którzy chcą gotowego rozwiązania.

**Zakup**: [stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)

> 💰 **Ekskluzywny rabat**: Zaoszczędź do 20% na produktach STS Collective — użyj kodu **SIMEONONSECURITY** przy kasie lub [kliknij tutaj, aby kupić z zastosowanym rabatem](https://stscollective.com/discount/SIMEONONSECURITY).

---

#### 3. OUI-SPY firmy Colonel Panic Tech ($85)

**Przegląd**: Wielofunkcyjna płytka wykrywania nadzoru z czterema różnymi trybami oprogramowania wybieranymi przez menu WiFi.

**Specyfikacje sprzętowe**:
- **Mikrokontroler**: ESP32-S3 dwurdzeniowy Xtensa LX7, 8MB flash
- **WiFi**: 802.11 b/g/n, zdolny do trybu promiscuous
- **Pamięć**: 8MB Flash
- **Wyświetlacz**: Brak (gołe PCB ze wskaźnikami LED)
- **Bateria**: Nie dołączona
- **Ładowanie**: Zasilanie i programowanie przez USB-C
- **Pamięć masowa**: Brak (tryby wyłącznie wykrywające)
- **Wskaźniki**: Zintegrowany brzęczyk PWM z melodiami specyficznymi dla trybu
- **Przyciski**: Przycisk boot do przełączania trybów
- **Antena**: **Przełączalna**, wbudowana ceramiczna 2.4GHz LUB zewnętrzna przez złącze MMCX
- **Obudowa**: Brak (gołe PCB ze wzorem artystycznym)
- **Unikalna funkcja**: Randomizacja MAC przy każdym uruchomieniu

**Oprogramowanie**: OUI-SPY Unified Blue z **4 trybami do wyboru**:
1. **Tryb Detector**: Wielozadaniowy skaner BLE z filtrowaniem OUI + portal konfiguracji webowej
2. **Tryb Foxhunter**: Tracker zbliżeniowy RSSI dla pojedynczego celu do radiowego namierzania kierunkowego
3. **Tryb Flock-You**: Wykrywanie kamer Flock Safety i Raven z wardriving GPS, eksport JSON/CSV/KML
4. **Tryb Sky Spy**: Detektor RemoteID dronów (OpenDroneID / ASTM F3411) z śledzeniem wielu dronów

**Wybór trybu**:
- Menu startowe WiFi pod adresem 192.168.4.1
- Przytrzymaj przycisk BOOT przez 2 sekundy, aby powrócić do selektora
- Pamięć ostatniego trybu między cyklami zasilania
- Melodie startowe dla każdego trybu (retro sygnały chipowe)
- Operacja wyłącznie wykrywająca (nic nie jest transmitowane)

**Zalety**:
- ✅ Cztery tryby oprogramowania w jednym urządzeniu
- ✅ Przełączalna antena (wbudowana lub zewnętrzna MMCX)
- ✅ Zintegrowany brzęczyk z niestandardowymi melodiami startowymi
- ✅ Profesjonalny projekt PCB
- ✅ Wielofunkcyjny: ALPR, drony, BLE, radiowe namierzanie kierunkowe
- ✅ Obsługa zewnętrznej anteny dla rozszerzonego zasięgu
- ✅ Od twórcy oryginalnego projektu Flock-You
- ✅ Aktywny rozwój i aktualizacje

**Wady**:
- ❌ Najwyższa cena dla wykrywania jednocelowego Flock
- ❌ Brak dołączonej obudowy (gołe PCB)
- ❌ Brak wbudowanej baterii
- ❌ Brak wyświetlacza (wyłącznie informacja dźwiękowa dla większości trybów)
- ❌ *Złożoność niepotrzebna do podstawowego wykrywania*
- ❌ Zewnętrzny GPS wymagany do funkcji wardriving

**Najlepszy dla**: Wielofunkcyjnego wykrywania nadzoru, użytkowników chcących wykrywania dronów + ALPR + BLE w jednym urządzeniu, zastosowań radiowego namierzania kierunkowego, tych, którzy cenią przełączalne anteny i zaawansowane funkcje.

**Zakup**: [colonelpanic.tech](https://colonelpanic.tech/products/oui-spy)


______

## Instrukcje konfiguracji krok po kroku

### Przewodnik konfiguracji 1: Budowa DIY ESP32

**Aby uzyskać pełne szczegółowe instrukcje**, odwiedź repozytorium GitHub: [github.com/simeononsecurity/flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)

#### Szybki start

1. **Wymagany sprzęt**:
   - Płytka ESP32 DevKit ($5-6)
   - Kabel USB (Micro-USB lub USB-C w zależności od płytki)
   - Opcjonalnie: Moduł pasywnego brzęczyka (KY-006), płytka stykowa, kabelki
   - Opcjonalnie: Obudowa drukowana 3D

2. **Konfiguracja oprogramowania**:
   ```bash
   # Install PlatformIO
   pip install platformio
   
   # Clone repository
   git clone https://github.com/simeononsecurity/flock-you-esp32.git
   cd flock-you-esp32
   
   # Flash firmware
   pio run -t upload
   pio device monitor
   ```

3. **Montaż sprzętu** (jeśli używasz brzęczyka):
   - Plus brzęczyka → GPIO 25
   - Minus brzęczyka → GND
   - Wskaźnik LED → GPIO 2 (wbudowany)
   - Zasilanie przez USB

4. **Potwierdzenie uruchomienia**:
   - Melodia Super Mario Bros. 1-2 odgrywa się (jeśli podłączony brzęczyk)
   - Dioda LED miga wskazując skanowanie
   - Monitor szeregowy pokazuje inicjalizację "Flock-You ESP32"

5. **Alarmy wykrywania**:
   - **Nowe wykrycie**: Dwa szybkie rosnące sygnały dźwiękowe (2000→2800 Hz)
   - **Bicie serca**: Dwa sygnały co 10 sekund podczas śledzenia
   - **LED**: Miga przy każdym wykryciu

6. **Wardriving GPS** (opcjonalnie):
   - Podłącz do komputera przez USB
   - Uruchom pulpit Flask: `cd api && python flockyou.py`
   - Otwórz http://localhost:5000
   - Podłącz urządzenie GPS lub użyj lokalizacji przeglądarki
   - Eksportuj wykrycia do JSON/CSV/KML

**Pełny przewodnik budowy, pliki obudowy i rozwiązywanie problemów**: Zobacz README na GitHub

---

### Przewodnik konfiguracji 2: M5 Atom Lite wstępnie wgrany (STS Collective)

#### Szybki start

1. **Rozpakowywanie**:
   - Urządzenie M5 Atom Lite (wstępnie wgrane z oprogramowaniem FlockYou)
   - Sprawdź listę produktów, czy dołączono kabel USB-C

2. **Włączenie zasilania**:
   - Podłącz do źródła zasilania USB-C (powerbank, USB samochodowy, adapter ścienny, komputer)
   - Urządzenie uruchamia się automatycznie
   - Inicjuje się matryca diod RGB LED

3. **Działanie**:
   - **Bezczynność/Skanowanie**: Dioda LED wyświetla wzorzec skanowania
   - **Wykrycie**: Dioda LED zmienia kolor na **NIEBIESKI** po wykryciu kamery Flock
   - **Przycisk**: Naciśnij, aby ręcznie ponownie zeskanować lub zresetować

4. **Użycie przenośne**:
   - Podłącz do powerbanku USB (5000mAh = ~20 godzin)
   - Umieść w uchwycie na kubek, torbie lub kieszeni
   - Dioda LED widoczna przez półprzezroczystą obudowę

5. **Połączenie z pulpitem** (opcjonalnie):
   - Podłącz urządzenie do komputera przez USB-C
   - Zainstaluj pulpit FlockYou zgodnie z instrukcjami STS Collective
   - Wyświetl wykrycia na żywo w interfejsie przeglądarki

**Ostrzeżenie**: *To jest zastrzeżone oprogramowanie. Ponowne wgranie wersji open-source trwale usunie oprogramowanie STS.*

---

### Przewodnik konfiguracji 3: Wielofunkcyjna płytka OUI-SPY

#### Wstępna konfiguracja

1. **Zawartość opakowania**:
   - Gołe PCB OUI-SPY
   - Kabel USB-C
   - Skrócona instrukcja obsługi

2. **Pierwsze uruchomienie**:
   - Podłącz zasilanie USB-C (komputer, adapter ścienny lub powerbank)
   - Urządzenie nadaje sieć WiFi: `OUISPY-[ID]`
   - Brzęczyk odgrywa melodię startową specyficzną dla trybu

3. **Wybór trybu WiFi**:
   - Podłącz telefon/komputer do sieci WiFi OUI-SPY
   - Otwórz przeglądarkę pod adresem: `http://192.168.4.1`
   - Interfejs webowy wyświetla 4 tryby oprogramowania:
     1. **Detector** - Wielozadaniowy skaner BLE
     2. **Foxhunter** - Radiowe namierzanie kierunkowe
     3. **Flock-You** - Wykrywanie kamery ALPR
     4. **Sky Spy** - Detektor RemoteID dronów
   - Wybierz żądany tryb i kliknij "Activate"

4. **Działanie trybu Flock-You**:
   - Urządzenie uruchamia się ponownie w tryb Flock-You
   - Brzęczyk odgrywa melodię startową Flock-You
   - Rozpoczyna skanowanie w poszukiwaniu 31 znanych OUI
   - **Alarm wykrywania**: Brzęczyk ćwierka z unikalnym wzorcem
   - Ostatni tryb zapamiętywany między cyklami zasilania

5. **Przełączanie trybów**:
   - Przytrzymaj **przycisk BOOT** przez 2 sekundy
   - Urządzenie powraca do selektora trybu WiFi
   - Połącz się ponownie z WiFi i wybierz nowy tryb

#### Zaawansowane: Zewnętrzna antena

6. **Przełączanie anten** (dla rozszerzonego zasięgu):
   - Domyślnie: Używa wbudowanej anteny ceramicznej
   - Podłącz antenę MMCX do złącza MMCX
   - Oprogramowanie automatycznie przełącza się na zewnętrzną antenę
   - Użyj anteny kierunkowej/Yagi dla wykrywania dalekiego zasięgu

#### Montaż

7. **Instalacja w pojeździe/na stałe**:
   - *Bez dołączonej obudowy, gołe PCB wymaga ochrony przed montażem*
   - Opcje:
     - Druk 3D niestandardowej obudowy
     - Mocowanie na rzep do deski rozdzielczej
     - Użyj taśmy dwustronnej
     - Skrzynka projektowa DIY
   - Zachowaj dostępność portu USB-C dla zasilania

#### Eksport danych (tryb Flock-You)

8. **Wardriving GPS**:
   - Podłącz zewnętrzny moduł GPS (nie dołączony)
   - Urządzenie rejestruje wykrycia ze współrzędnymi
   - Pobierz pliki danych przez interfejs webowy
   - Formaty eksportu: JSON, CSV, KML

**Uwaga**: Sprawdź colonelpanic.tech pod kątem aktualizacji oprogramowania i dokumentacji specyficznej dla OUI-SPY Unified Blue.

---



______

## Przewodnik zakupu i informacje o dostawcach

### Autoryzowani dostawcy

#### Colonel Panic Tech (colonelpanic.tech)

**Oferowane produkty**:
- **OUI-SPY** ($85): Gotowe do użycia urządzenie wykrywające Flock
- **Zestawy DIY** ($55): Komponenty + PCB + przewodnik montażu
- **Dodatek modułu GPS** ($18): Kompatybilny moduł GPS-6M
- **Akcesoria**: Anteny, obudowy, ulepszenia baterii

**Dlaczego warto kupować od Colonel Panic**:
- ✅ Bezpośrednio od dewelopera sprzętu OUI-SPY
- ✅ Najnowsze oprogramowanie wstępnie zainstalowane
- ✅ Wsparcie techniczne w zestawie
- ✅ Ethos open-source (dostępne schematy)
- ✅ Aktywne forum społeczności

**Wysyłka**:
- USA: 3-5 dni roboczych
- Zagranica: 7-14 dni roboczych
- Darmowa wysyłka przy zamówieniach >$100

**Gwarancja**: 90-dniowa gwarancja sprzętu, dożywotnie aktualizacje oprogramowania

**Strona internetowa**: [https://colonelpanic.tech](https://colonelpanic.tech)

---

#### STS Collective (stscollective.com)

**Oferowane produkty**:
- **M5 Atom Lite wstępnie wgrany** ($39.99): Gotowe do użycia urządzenie wykrywające Flock
- **Akcesoria**: Kompatybilne z różnymi platformami ESP32

**Dlaczego warto kupować od STS Collective**:
- ✅ Wstępnie wgrane urządzenia gotowe do użycia
- ✅ Zapewnienie jakości i testowanie
- ✅ Przystępne ceny
- ✅ Obsługa klienta

**Wysyłka**:
- USA: 2-4 dni robocze (Poczta priorytetowa)
- Zagranica: 7-21 dni roboczych
- Dostępne opcje ekspresowe

**Gwarancja**: Standardowa gwarancja na sprzęt

**Strona internetowa**: [https://stscollective.com](https://stscollective.com)

> 💰 **Rabat dla czytelników**: Użyj kodu **SIMEONONSECURITY**, aby uzyskać do 20% zniżki na produkty STS Collective — [stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

---

#### Inne źródła M5 Atom Lite

**Oficjalny sklep M5Stack**:
- Strona: [shop.m5stack.com](https://shop.m5stack.com)
- Cena: $9.95 za gołe Atom Lite
- Akcesoria: Moduły baterii, czujniki Grove, obudowy
- Wysyłka: Międzynarodowa, 7-14 dni

**Amazon**: Wyszukaj "M5Stack Atom Lite"
- Cena: ~$12-15 (różna w zależności od sprzedawcy)
- Dostępna wysyłka Prime
- Opcje zestawów z akcesoriami

**Adafruit**: [adafruit.com](https://adafruit.com)
- Wyselekcjonowany sprzedawca elektroniki
- Doskonałe zasoby edukacyjne
- Szybka wysyłka z USA

**Uwaga**: *Przy zakupie gołego M5 Atom Lite oprogramowanie musi być zainstalowane oddzielnie zgodnie z powyższym przewodnikiem DIY. Wstępnie wgrana wersja STS Collective to inny produkt.*

### Podsumowanie porównania cen

| Urządzenie | Cena bazowa | Opcjonalne dodatki | Całkowita inwestycja | Czas konfiguracji |
|--------|------------|------------------|------------------|------------|
| **DIY ESP32** | $5-12 | Obudowa 3D, bateria | $5-20 | 15-30 min |
| **M5 Atom Lite** | $39.99 | Powerbank $10 | $40-50 | Plug-and-play |
| **OUI-SPY** | $85 | Zewnętrzna antena $20, obudowa | $85-115 | Plug-and-play |

______

## Używanie urządzenia wykrywającego: Scenariusze praktyczne

### Scenariusz 1: Mapowanie codziennych dojazdów

**Cel**: Dokumentowanie lokalizacji kamer Flock na regularnych trasach.

**Konfiguracja**:
- Użyj urządzenia z możliwością GPS (DIY ESP32 z modułem GPS lub OUI-SPY z GPS)
- Włącz automatyczne rejestrowanie
- Zamontuj w pojeździe lub noś w kieszeni
- Ustaw czułość na ŚREDNIĄ, aby zmniejszyć liczbę fałszywych alarmów

**Procedura**:
1. Uruchom urządzenie wykrywające przed wyjazdem
2. Jedź swoją normalną trasą
3. Urządzenie alarmuje po wykryciu kamer Flock
4. Automatyczne rejestrowanie współrzędnych GPS
5. Wróć do domu i wyeksportuj dane
6. Zaimportuj GPX/CSV do oprogramowania do mapowania
7. Utwórz osobistą mapę lokalizacji kamer

**Korzyści**:
- Świadomość zasięgu nadzoru na Twoich trasach
- Identyfikacja alternatywnych tras wolnych od kamer
- Wkład w projekty mapowania społecznościowego
- Śledzenie zmian rozmieszczenia w czasie

### Scenariusz 2: Ocena nadzoru w okolicy

**Cel**: Określenie zasięgu kamer Flock w okolicy mieszkalnej.

**Konfiguracja**:
- Użyj przenośnego urządzenia (M5 Atom Lite, DIY ESP32 lub OUI-SPY)
- Badanie pieszo lub rowerem
- Stacjonarne monitorowanie w kluczowych skrzyżowaniach

**Procedura**:
1. Chodź/jedź rowerem po ulicach okolicy
2. Zatrzymaj się na każdym skrzyżowaniu na 30-60 sekund
3. Zanotuj wykrycia na mapie
4. Użyj siły sygnału do szacowania odległości/kierunku
5. Wizualnie potwierdź lokalizacje kamer, gdy to możliwe
6. Dokumentuj odkrycia zdjęciami (z terenów publicznych)

**Wynik**:
- Kompletna mapa lokalnej infrastruktury nadzorczej
- Dowody do organizowania społeczności
- Dane do wniosków o dostęp do informacji publicznej
- Świadomość dla osobistych decyzji dotyczących prywatności

### Scenariusz 3: Ocena prywatności podczas podróży

**Cel**: Zrozumienie ekspozycji na nadzór podczas podróży.

**Konfiguracja**:
- Weź kompaktowe urządzenie (M5 Atom Lite w kieszeni lub DIY ESP32)
- Włącz ciągłe rejestrowanie
- Przejrzyj dane po podróży

**Przypadki użycia**:
- Wizyty lekarskie: Oceń nadzór w pobliżu klinik
- Konsultacje prawne: Sprawdź zasięg obszaru biura adwokackiego
- Nabożeństwa religijne: Zrozumienie monitorowania w pobliżu miejsc kultu
- Działalność polityczna: Oceń nadzór na wydarzeniach/protestach
- Sytuacje domowe: Zidentyfikuj, czy miejsce zamieszkania jest monitorowane

### Scenariusz 4: Rzecznictwo społeczne

**Cel**: Dostarczenie danych do debat politycznych i świadomości publicznej.

**Zastosowania**:
- Prezentacja wyników na posiedzeniach rady miejskiej
- Włączenie do wniosków o dostęp do informacji publicznej
- Udostępnianie organizacjom zajmującym się prywatnością
- Wkład w projekty badawcze
- Informowanie stowarzyszeń sąsiedzkich

**Prezentacja danych**:
- Tworzenie map cieplnych pokazujących gęstość kamer
- Generowanie raportów o dysproporcjach w zasięgu
- Tworzenie osi czasu ekspansji rozmieszczenia
- Korelacja ze statystykami przestępczości (lub ich brakiem)

______

## Szczegółowe omówienie techniczne: Zrozumienie kodu

### Podstawowy algorytm wykrywania (uproszczony)

Dla zainteresowanych implementacją techniczną, oto uproszczony widok logiki wykrywania:

```cpp
// Flock-You Detection Core (Conceptual - not full code)

// OUI Database (31 known Flock-associated OUIs)
const uint8_t FLOCK_OUI_LIST[][3] = {
    {0xD4, 0xAD, 0xFC}, // Espressif ESP32-S3
    {0xAC, 0x67, 0xB2}, // Espressif ESP32-WROOM
    {0x84, 0xF3, 0xEB}, // Espressif ESP32-S3 variant
    // ... 28 more OUIs ...
};

// Promiscuous mode callback
void wifi_sniffer_callback(void* buf, wifi_promiscuous_pkt_type_t type) {
    wifi_promiscuous_pkt_t *pkt = (wifi_promiscuous_pkt_t*)buf;
    
    // Extract MAC address from frame
    uint8_t *mac = pkt->payload + 10; // addr2 field position
    
    // Check against OUI database
    for (int i = 0; i < NUM_OUIS; i++) {
        if (memcmp(mac, FLOCK_OUI_LIST[i], 3) == 0) {
            // OUI match found
            int rssi = pkt->rx_ctrl.rssi;
            
            // Check signal strength threshold
            if (rssi > RSSI_THRESHOLD) {
                // Analyze frame for additional signatures
                if (is_wildcard_probe_request(pkt)) {
                    // High confidence detection
                    trigger_alert(mac, rssi, HIGH_CONFIDENCE);
                } else {
                    // OUI match only
                    trigger_alert(mac, rssi, MEDIUM_CONFIDENCE);
                }
            }
        }
    }
}

// Wildcard probe detection
bool is_wildcard_probe_request(wifi_promiscuous_pkt_t *pkt) {
    // Management frame, subtype probe request
    if ((pkt->payload[0] & 0x0F) != 0x04) return false;
    
    // Check for empty SSID IE (wildcard)
    // Position depends on frame structure
    uint8_t *ie = &pkt->payload[24]; // Start of IEs
    if (ie[0] == 0x00 && ie[1] == 0x00) {
        return true; // Wildcard probe
    }
    return false;
}
```

### Wyjaśnienie kluczowych koncepcji technicznych

**Tryb promiscuous**: Zamiast odbierać tylko ramki zaadresowane do Twojego urządzenia, ESP32 przechwytuje wszystkie ramki WiFi w zasięgu. **Jest to niezbędne do wykrywania pobliskich urządzeń, które nie komunikują się z Twoim detektorem.**

**Struktura adresu MAC**: Każda ramka WiFi zawiera wiele adresów MAC:
- `addr1`: Adres odbiorcy
- `addr2`: Adres nadajnika (zawiera OUI)
- `addr3`: Adres ostatecznego miejsca docelowego/źródła

**RSSI (Received Signal Strength Indicator)**: Siła sygnału w dBm (ujemne decybele względem 1 miliwata). Typowe wartości:
- -30 dBm: Niezwykle silny (bardzo blisko)
- -50 dBm: Silny sygnał
- -70 dBm: Słaby, ale użyteczny
- -90 dBm: Bardzo słaby (granica zasięgu)

**Żądania sondowania**: Urządzenia WiFi wysyłają żądania sondowania, aby odkryć dostępne sieci. *Sondy wieloznaczne (puste SSID) szukają dowolnej sieci, co jest powszechne w urządzeniach IoT takich jak kamery Flock, co czyni je wiarygodnie wykrywalnymi.*

______

## Rozwiązywanie typowych problemów

### Problem: Brak wykryć pomimo pobliskiej, znane kamery

**Możliwe przyczyny**:
1. **Kamera offline/wyłączona**: Kamery Flock są czasami tymczasowo nieaktywne
2. **Zablokowany sygnał**: Materiały budowlane pochłaniają WiFi (metal, beton)
3. **Poza zasięgiem**: Efektywny zasięg ~30-90 metrów w zależności od przeszkód
4. **Problem z oprogramowaniem**: Nieaktualne oprogramowanie pomija nowsze warianty OUI

**Rozwiązania**:
- Potwierdź, że kamera jest widoczna i wydaje się sprawna (panele słoneczne, lampki)
- Zbliż się do podejrzanej lokalizacji kamery
- Wypróbuj różne orientacje anteny
- Zaktualizuj do najnowszego oprogramowania Flock-You
- **Sprawdź, czy urządzenie aktywnie skanuje** (zweryfikuj aktywność LED/wyświetlacza)

### Problem: Nadmierne fałszywe alarmy

**Możliwe przyczyny**:
1. **Wysoka gęstość urządzeń ESP32**: Urządzenia inteligentnego domu i IoT są powszechne
2. **Czułość zbyt wysoka**: Wykrywanie odległych/nieistotnych urządzeń
3. **Inne kamery nadzorcze**: Wiele używa modułów ESP32

**Rozwiązania**:
- Zmniejsz ustawienie czułości
- Włącz wykrywanie sond wieloznacznych (wyższa pewność)
- Fizycznie zweryfikuj wykrycia przed zarejestrowaniem
- Użyj siły sygnału do filtrowania (alarmuj tylko przy silnych sygnałach)
- Zaktualizuj bazę danych OUI, aby skupić się na potwierdzonych OUI Flock

### Problem: Szybkie rozładowywanie baterii

**Możliwe przyczyny**:
1. **Ciągłe skanowanie**: Brak zarządzania uśpieniem/zasilaniem
2. **Wyświetlacz zawsze włączony**: Ekran zużywa znaczną moc
3. **Aktywny GPS**: Moduły GPS są energochłonne
4. **Stara bateria**: Baterie Li-Po degradują się w czasie

**Rozwiązania**:
- Włącz tryb pasywnego skanowania (przerywane vs. ciągłe)
- Ustaw limit czasu wyświetlacza
- Wyłącz GPS, gdy mapowanie nie jest potrzebne
- Wymień baterię (OUI-SPY/mesh-detect v2 mają wymienne baterie)
- Użyj zewnętrznego powerbanku do dłuższych sesji

### Problem: GPS nie może uzyskać blokady

**Możliwe przyczyny**:
1. **Użycie wewnętrzne**: GPS wymaga widoczności nieba
2. **Antena niepodłączona**: mesh-detect v2 potrzebuje podłączonej zewnętrznej anteny
3. **Zimny start**: Pierwsze zablokowanie GPS trwa 5-15 minut
4. **Zakłócenia**: Pobliskie urządzenia elektroniczne zakłócają sygnał

**Rozwiązania**:
- Przesuń się na pozycję z wyraźnym widokiem nieba
- Upewnij się, że antena jest prawidłowo podłączona (złącze SMA)
- Poczekaj na wstępne zablokowanie (kolejne blokowania są szybsze)
- Oddal się od źródeł zakłóceń RF
- Sprawdź, czy GPS jest włączony w ustawieniach

### Problem: Dane nie są rejestrowane na karcie SD

**Możliwe przyczyny**:
1. **Karta SD nieformatowana**: Musi być w formacie FAT32
2. **Karta SD pełna**: Brak wolnego miejsca
3. **Karta niewykryta**: Nie włożona do końca
4. **Uszkodzenie systemu plików**: Karta uszkodzona

**Rozwiązania**:
- **Sformatuj kartę SD jako FAT32** (maksymalnie 32GB dla kompatybilności)
- Usuń stare logi lub użyj większej karty
- Włóż kartę do końca (powinna zaskoczyć)
- Przeformatuj kartę lub wymień, jeśli uszkodzona
- Sprawdź, czy urządzenie rozpoznaje kartę (menu pokaże status SD)

______

## Kwestie prawne i etyczne

### Status prawny urządzeń wykrywających

**Legalność skanowania WiFi**:
- ✅ **Legalne w USA**: Pasywne monitorowanie WiFi (tylko odbiór) jest legalne
- ✅ **Brak przechwytywania**: Urządzenia monitorują tylko publicznie nadawane ramki
- ✅ **Brak deszyfrowania**: Nie próbują deszyfrować danych ani łączyć się z sieciami
- ✅ **Podobne do skanerów radiowych**: Porównywalny status prawny do skanerów policyjnych

**Ważne rozróżnienia**:
- ❌ **Nielegalne**: Aktywne zakłócanie/ingerencja w działanie kamery
- ❌ **Nielegalne**: Próby hackowania lub dostępu do systemów kamer
- ❌ **Nielegalne**: Niszczenie lub manipulowanie przy fizycznych kamerach
- ⚠️ **Szara strefa**: *Niektóre jurysdykcje mają surowsze przepisy dotyczące prywatności. Sprawdź lokalne przepisy przed użyciem.*

**Zalecenie**: **Urządzenia wykrywające służą wyłącznie do zwiększania świadomości. Nie zakłócaj działania kamery.**

### Wytyczne dotyczące etycznego użytkowania

**Odpowiedzialne użytkowanie**:
- ✅ Użyj do osobistej świadomości nadzoru
- ✅ Dokumentuj do celów rzecznictwa i dyskusji politycznych
- ✅ Udostępniaj zagregowane dane organizacjom zajmującym się prywatnością
- ✅ Wnoś wkład do projektów mapowania społeczności
- ✅ Edukuj innych o infrastrukturze nadzorczej

**Unikaj**:
- ❌ Używania danych do ułatwiania nielegalnych działań
- ❌ Nękania właścicieli nieruchomości, którzy zainstalowali kamery
- ❌ Wtargnięcia w celu potwierdzenia lokalizacji kamer
- ❌ Działań samosądowych przeciwko infrastrukturze nadzorczej

### Kwestie prywatności

**Prywatność Twoich danych**:
- **Urządzenia wykrywające rejestrują TWOJĄ lokalizację** (przez GPS)
- Przechowuj te dane bezpiecznie
- **Bądź świadomy ryzyka wezwania do sądu** w przypadku udziału w postępowaniach prawnych
- Rozważ szyfrowanie dla wrażliwych plików logów
- Zrozum polityki prywatności dostawców dla urządzeń podłączonych do chmury

**Szanowanie innych**:
- Bądź uważny przy używaniu urządzeń wykrywających w przestrzeniach prywatnych
- Nie używaj do śledzenia innych osób
- Rozważ etyczne implikacje udostępniania danych

______

## Społeczność i rozwój open source

### Wkład w projekt Flock-You

Projekt Flock-You kwitnie dzięki wkładowi społeczności:

**Repozytorium GitHub**: [github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)

**Sposoby wkładu**:
1. **Odkrycie nowego OUI**: Zgłoś nowo zidentyfikowane OUI kamer Flock
2. **Ulepszenia kodu**: Zgłaszaj pull requesty dla ulepszeń oprogramowania
3. **Projekty sprzętu**: Udostępniaj niestandardowe projekty urządzeń wykrywających
4. **Dokumentacja**: Poprawiaj przewodniki konfiguracji, tłumaczenia
5. **Testowanie**: Zgłaszaj błędy, weryfikuj funkcjonalność na różnych urządzeniach
6. **Mapowanie**: Wnoś wkład do zbiorowych baz danych lokalizacji kamer

### Zasoby społeczności

**Fora i dyskusje**:
- **Reddit**: r/privacy, r/privacytoolsIO, aktywne dyskusje
- **Discord**: Serwer Colonel Panic Tech, czat w czasie rzeczywistym
- **GitHub Issues**: Wsparcie techniczne i prośby o funkcje

**Prace badawcze**:
- Studia akademickie dotyczące nadzoru ALPR
- Oceny wpływu na prywatność
- Analizy prawne legalności urządzeń wykrywających

**Organizacje rzecznicze**:
- **Electronic Frontier Foundation** (EFF): Śledzenie ALPR
- **ACLU**: Nadzór i prawa do prywatności
- **Lokalne grupy**: DeFlockJoplin i podobne inicjatywy społecznościowe

### Mapa drogowa przyszłego rozwoju

**Planowane funkcje** (z GitHub projektu):
- **Uczenie maszynowe**: Rozpoznawanie wzorców dla wyższej dokładności
- **Synchronizacja w chmurze**: Opcjonalna zbiorowa baza danych wykryć
- **Aplikacje mobilne**: Integracja z telefonem komórkowym dla rozszerzonych interfejsów
- **Dodatkowe tryby wykrywania**: Inne technologie nadzorcze
- **Alerty w czasie rzeczywistym**: Powiadomienia push przez komórkę/WiFi

______

## Podsumowanie: Wspieranie prywatności przez technologię

**Projekt wykrywania Flock-You** reprezentuje potężną demokratyzację technologii antynadzorczej. Za mniej niż koszt miesięcznej subskrypcji streamingowej, jednostki zyskują świadomość infrastruktury nadzorczej wokół siebie. Niezależnie od tego, czy wybierzesz **budowę DIY ESP32 ($5-12)**, **gotowy do użycia M5 Atom Lite ($40)**, czy **wielofunkcyjny OUI-SPY ($85)**, inwestujesz w świadomość prywatności i cyfrową autonomię.

### Najważniejsze punkty

✅ **Demokratyzacja open-source**: Rozwój napędzany przez społeczność zapewnia dostępność
✅ **Przystępna technologia**: Sprzęt klasy konsumenckiej (ESP32) czyni wykrywanie dostępnym
✅ **Wiele platform**: Opcje dla różnych budżetów i poziomów umiejętności technicznych
✅ **Aktywny rozwój**: Regularne aktualizacje z nowymi sygnaturami OUI i funkcjami
✅ **Legalne i etyczne**: Pasywne monitorowanie jest zgodne z przepisami dotyczącymi komunikacji
✅ **Korzyść społeczna**: Przyczynia się do publicznej świadomości i dyskusji politycznych

### Następne kroki

1. **Dowiedz się więcej** o tym, dlaczego wykrywanie ma znaczenie: [Nadzór kamerami Flock Safety: Powszechność i obawy o prywatność](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)
2. **Wybierz platformę**: Zdecyduj, które urządzenie odpowiada Twoim potrzebom i budżetowi
3. **Zamów sprzęt**: Kup od autoryzowanych dostawców
4. **Skonfiguruj**: Postępuj zgodnie z szczegółowymi przewodnikami w tym artykule
5. **Dołącz do społeczności**: Angażuj się z innymi użytkownikami, dziel się odkryciami, wnoś ulepszenia
6. **Podejmij działania**: Użyj swoich danych do rzecznictwa, świadomości i świadomych decyzji

Proliferacja nadzoru ALPR reprezentuje znaczące przesunięcie w dynamice prywatności. Technologie antynadzorcze takie jak Flock-You oferują kluczową możliwość: **świadomość**. Kiedy rozumiemy zakres i skalę nadzoru, podejmujemy świadome decyzje dotyczące naszych ruchów, naszego rzecznictwa i naszych oczekiwań dotyczących prywatności w przestrzeniach publicznych.

**Technologia umożliwiła wszechobecny nadzór. Technologia pomaga również tym, którzy cenią prywatność.** Projekt Flock-You jest świadectwem siły współpracy open-source w ochronie wolności obywatelskich.

______

## Powiązane artykuły

| Artykuł | Opis |
|---------|-------------|
| **[Nadzór kamerami Flock Safety: Powszechność, obawy o prywatność i strategie ochrony](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Definitywny przewodnik po sieci ALPR Flock Safety, udokumentowanych nadużyciach, zasobach do organizowania społeczności i o tym, co możesz zrobić, aby się chronić |
| **[Flock Finder: Mapuj każdą podejrzaną kamerę Flock Safety w pobliżu](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Jak korzystać z narzędzia open-source Flock Finder do wizualizacji ponad 40 000 podejrzanych kamer Flock na całym świecie przy użyciu danych WiGLE i odcisków palców OUI |
| **[Jak wgrać Rayhunter na urządzenia do wykrywania łapaczy IMSI](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Przewodnik krok po kroku dotyczący wgrywania oprogramowania Rayhunter do wykrywania łapaczy IMSI i stingrayów, uzupełnienie wykrywania ALPR |
| **[Niestandardowe oprogramowanie DagShell dla Orbic RCL400](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | Pełny przewodnik dotyczący instalowania DagShell na Orbic RCL400 do zaawansowanego monitorowania sieci komórkowej i wykrywania łapaczy IMSI |
| **[Porównanie urządzeń Rayhunter 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Porównanie urządzeń obsługiwanych przez Rayhunter, aby pomóc Ci wybrać odpowiedni sprzęt do zestawu narzędzi antynadzorczych |

______

## Referencje

1. [Repozytorium GitHub Flock-You - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [Flock Finder - Interaktywna mapa kamer ALPR](https://simeononsecurity.github.io/flock-finder/)
3. [Flock Finder - Repozytorium GitHub](https://github.com/simeononsecurity/flock-finder)
4. [Colonel Panic Tech - Oficjalny dostawca](https://colonelpanic.tech)
5. [STS Collective - M5 Atom Lite wstępnie wgrany](https://stscollective.com)
4. [Oficjalna dokumentacja M5Stack](https://docs.m5stack.com/en/core/atom_lite)
5. [Dokumentacja techniczna Espressif ESP32](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
6. [Samouczek trybu promiscuous WiFi](https://esp32developer.com/wifi-promiscuous-mode)
7. [Badania społeczności DeFlockJoplin](https://deflockjoplin.org/)
8. [Electronic Frontier Foundation - ALPR](https://www.eff.org/issues/automated-license-plate-readers)
9. [Oficjalne pobieranie Arduino IDE](https://www.arduino.cc/en/software)
10. [Dokumentacja Platform.io](https://docs.platformio.org/)
11. [Baza danych OUI - Standardy IEEE](https://standards.ieee.org/products-programs/regauth/)
12. [Referencja struktury ramki 802.11](https://mrncciew.com/2014/10/08/802-11-mgmt-beacon-frame/)
