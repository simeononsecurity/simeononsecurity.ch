---
title: "SenseCAP M1 Raspberry Pi Shield: pinout i ponowne użycie w LoRaWAN"
date: 2026-09-12
lastmod: 2026-11-13
toc: true
draft: false
description: "Poznaj shield SenseCAP M1, porównaj sprzeczne mapy GPIO, sprawdź układ ATECC608 i zaplanuj bramę LoRaWAN z nowoczesnym Raspberry Pi OS."
genre: ["Raspberry Pi", "IoT", "Bezpieczeństwo sprzętu"]
tags: ["SenseCAP M1", "SenseCAP M1 shield", "SenseCAP M1 pinout", "Raspberry Pi shield", "Raspberry Pi HAT", "LoRaWAN gateway", "WM1302", "WM1303", "SX1302", "SX1303", "Seeed Studio", "Helium hotspot reuse", "LoRa concentrator", "SPI GPIO", "GPIO17", "GPIO22 LED", "libgpiod", "Raspberry Pi OS", "ATECC608", "CryptoAuthLib", "I2C diagnostics", "STTS751", "LoRa Basics Station", "ChirpStack", "The Things Stack", "hardware reverse engineering"]
cover: "/img/cover/sensecap-wm1302-shield-hardware.webp"
coverAlt: "Shield SenseCAP M1 z modułem Seeed WM1302, złączem Raspberry Pi, przewodem antenowym, portem USB-C i złączem wentylatora"
coverCaption: "Zdjęcie płytki: Clockwork Bird, 2023. Źródło i informacje o autorstwie znajdują się poniżej."
coverCredit: "Clockwork Bird"
coverCreditURL: "https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/"
---

**Shield SenseCAP M1 to użyteczny sprzęt bramy LoRaWAN, ale jego okablowanie wymaga dokładniejszej analizy niż w typowym poradniku o nakładkach Raspberry Pi HAT.** Ten przewodnik rozwija [badanie Clockwork Bird z 2023 roku](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/) o dokumentację producenta, analizę sterowników upstream i aktualne wskazówki dotyczące GPIO. Zidentyfikujesz sprzęt, oddzielisz potwierdzone fakty od niepełnych danych pinoutu i przygotujesz powtarzalny zapis uruchomienia.

> **Zakres:** To przewodnik sprzętowy oparty na dokumentacji. Polecenia i mapowanie pinów nie zostały na potrzeby tego artykułu sprawdzone na fizycznym urządzeniu M1.

## Najważniejsze wnioski

- **Zidentyfikuj obie płytki:** nośnik M1 i wyjmowany koncentrator mają osobne modele i rewizje.
- **Sprawdź skrypty resetu:** domyślne wartości CoreCell są sprzeczne z sygnałami w opublikowanym pinoucie M1.
- **Sprawdź interfejsy systemu:** pliki urządzeń SPI, numeracja GPIO i wersje narzędzi GPIO odpowiadają na różne pytania.
- **Zachowaj konfigurację elementu zabezpieczającego:** odczyt informacji o urządzeniu różni się od konfigurowania i generowania kluczy.
- **Zweryfikuj całą ścieżkę:** wykrycie koncentratora nie potwierdza dostarczenia danych z czujnika.
## Zanim zaczniesz

**Poziom trudności: średni.** Przeznacz około jednej do dwóch godzin na inwentaryzację, przygotowanie systemu i kontrolę dokumentacji. Weryfikacja elektryczna, dostosowanie sterownika i wdrożenie serwera sieciowego wymagają dodatkowego czasu, zwłaszcza przy nieznanej rewizji płytki.

| Element | Cel |
|---|---|
| **Shield M1 i koncentrator** | Odczytaj rewizję nośnika i pełne oznaczenie modułu |
| **Raspberry Pi 4** | Zacznij od hosta z oryginalnego projektu M1 |
| **Zapasowa karta microSD** | Przygotuj osobny system, zachowując pierwotną instalację |
| **Odpowiedni zasilacz i antena** | Dopasuj je do zestawu i pasma RF modułu |
| **SSH lub lokalna konsola** | Zapisuj diagnostykę i edytuj konfigurację |
| **Czujnik LoRaWAN i serwer** | Po uruchomieniu sprzętu zweryfikuj dostarczenie danych aplikacji |
| **Miernik i doświadczenie ze sprzętem** | Sprawdź nieudokumentowane połączenia przed ich wysterowaniem |

Przed demontażem sfotografuj obie strony odłączonego od zasilania zestawu. Zanotuj orientację złączy, śruby, dystanse i przebieg anteny. Zachowaj oryginalną kartę oraz konfigurację do czasu, aż nowa instalacja przejdzie kryteria akceptacji.
## Rozróżnij trzy warstwy sprzętu

**Kompletny M1, jego płytka nośna i koncentrator to osobne elementy.** Seeed opisuje gotowy hotspot jako Raspberry Pi 4 z koncentratorem WM1302/SX1302 albo WM1303/SX1303. Oferta nazwana „shield SenseCAP M1” nie potwierdza, który moduł znajduje się na nośniku. [Przegląd M1 firmy Seeed Studio](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

**Nośnik** łączy zasilanie i sygnały urządzeń peryferyjnych między Pi a modułem. **Koncentrator** obsługuje odbiór i nadawanie radiowe. **Forwarder pakietów** działa na hoście i wymienia odebrane pakiety radiowe oraz zaplanowane downlinki z serwerem. [Przegląd SX1302 HAL firmy Semtech](https://github.com/Lora-net/sx1302_hal)

Na przykład czujnik temperatury na półce wysyła uplink przez radio. Koncentrator go odbiera, host przekazuje dalej, a usługi sieciowe i aplikacyjne przetwarzają dane. Udany start Linuksa potwierdza wyłącznie działanie części hosta.

Zdjęcie Clockwork Bird przedstawia nośnik M1 v1.1 z modułem oznaczonym `WM1302-SPI-EU868`. Użyj zdjęcia, aby znaleźć oznaczenia na swoim sprzęcie. Numery seryjne identyfikują sfotografowany egzemplarz, a nie wartości konfiguracji innej bramy.

{{< figure src="m1-carrier-wm1302-board.webp" alt="Zielony nośnik M1 z oznaczonym modułem WM1302 SPI EU868 obok USB-C, przycisku, złącza wentylatora i przewodu antenowego" caption="Sprzęt M1 v1.1 sfotografowany przez Clockwork Bird i użyty także jako okładka artykułu" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Zasilanie i połączenia radiowe

**Traktuj złącze USB-C M1 jako wejście zasilania.** Producent określa zasilanie całej bramy jako 5 V DC, 3 A, i wskazuje USB-C jako interfejs zasilania. Określenie „port ładowania” sugeruje funkcję akumulatora, której specyfikacja nie opisuje. [Specyfikacja SenseCAP M1](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

Schemat blokowy dostawcy oddziela zasilanie 5 V od regulowanej szyny 3,3 V modułu. To rozróżnienie ma znaczenie podczas diagnostyki: działające Pi i pozbawiony zasilania koncentrator to dwie osobne możliwości. Nie podawaj 5 V na pin sygnałowy ani nie zakładaj, że dwa wejścia zasilania są od siebie odizolowane.

**Moduły SPI i USB wymagają innych połączeń z hostem.** Dokumentacja WM1302 firmy Seeed opisuje bezpośredni dostęp SPI dla modelu SPI oraz most USB oparty na STM32L4 dla modelu USB. Kształt mini-PCIe opisuje format fizyczny, natomiast udokumentowane interfejsy elektryczne to SPI albo USB. Zgodne gniazdo w laptopie nie potwierdza kompatybilności. [Dokumentacja WM1302 firmy Seeed](https://github.com/seeed-lora/WM1302-doc)

Przed instalacją modułu odłącz zasilanie i podłącz odpowiednią antenę. Dopasuj sprzęt radiowy, antenę i plan sieci. Zmiana nazwy pliku konfiguracyjnego nie zastępuje podzespołów RF modułu. Gniazdo zasilania M1 nie potwierdza też obsługi wariantu koncentratora USB.

{{< figure src="m1-power-spi-system-diagram.webp" alt="Schemat blokowy połączenia Raspberry Pi 4 z shieldem M1 przez zasilanie, SPI, GPIO i I2C" caption="Schemat producenta SenseCAP odtworzony w oryginalnym artykule Clockwork Bird, przedstawiający projekt WM1302" credit="Seeed Studio / SenseCAP, via Clockwork Bird" attr="Seeed Studio / SenseCAP, via Clockwork Bird" attrlink="https://www.sensecapmx.com/docs/sensecap-m1/overview/" >}}

## Dokładnie odczytaj pinout

**Zapisuj numery BCM GPIO i numery fizycznych pinów w osobnych kolumnach.** Na przykład BCM GPIO17 znajduje się na fizycznym pinie 11 złącza Pi. Złącze krawędziowe modułu używa trzeciego systemu numeracji, dlatego numer pinu resetu modułu nie jest numerem GPIO Raspberry Pi.

Poniższa tabela przepisuje połączenia z opisanej ilustracji złącza autorstwa Clockwork Bird. To **materiał społeczności**, a nie pełny schemat producenta ani pomiar każdej rewizji M1. Rysunek używa też oznaczeń `SX1262`, podczas gdy ogólny skrypt resetu Semtech zawiera nazwy `SX1261`.

| Sygnał na rysunku | BCM / pin fizyczny | Interpretacja |
|---|---|---|
| **I2C SDA / SCL** | GPIO2 / 3, GPIO3 / 5 | Wspólna magistrala zarządzania |
| **Reset SX1302** | GPIO17 / 11 | Kandydat na reset koncentratora |
| **Dioda użytkownika** | GPIO22 / 15 | Oznaczenie M1 |
| **SPI MOSI / MISO** | GPIO10 / 19, GPIO9 / 21 | Sygnały danych SPI |
| **Zegar SPI** | GPIO11 / 23 | Sygnał zegara SPI |
| **Chip select SX1302** | GPIO8 / 24 | SPI0 CE0 |
| **Reset SX1262** | GPIO5 / 29 | Kandydat na reset dodatkowego radia |
| **Chip select SX1262** | GPIO6 / 31 | GPIO6, a nie SPI0 CE1 |
| **SX1262 BUSY** | GPIO18 / 12 | Wyjście stanu dodatkowego radia |
| **SX1262 IO1 / IO2** | GPIO23 / 16, GPIO24 / 18 | Dodatkowe sygnały, zweryfikuj przed użyciem |

Przekreślone oznaczenia GPS/UART nie potwierdzają, że M1 ma GPS. Pomiń konfigurację GPS, chyba że twój sprzęt zapewnia tę funkcję. Opublikowany diagram nie rozstrzyga też podłączenia przycisku ani sterowania wentylatorem. [Badanie pinoutu Clockwork Bird](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)

{{< figure src="m1-community-header-pinout.webp" alt="Opisany rysunek złącza Raspberry Pi z diodą M1, resetem koncentratora, sygnałami SPI i przekreślonym GPS" caption="Oznaczenia społeczności nie obejmują potwierdzonej dokumentacji wszystkich rewizji, to nie jest pełny schemat M1" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Rozstrzygnij sprzeczności w skryptach resetu

**Skrypt resetu wybiera wyjścia elektryczne, a nie tylko preferencje programowe.** Plik upstream Semtech `reset_lgw.sh` jest przeznaczony dla projektu referencyjnego CoreCell. Domyślnie używa GPIO23 do resetu koncentratora, GPIO18 do włączenia zasilania, GPIO22 do dodatkowego resetu i GPIO13 do resetu AD5338R. [Kod źródłowy skryptu resetu Semtech](https://github.com/Lora-net/sx1302_hal/blob/master/tools/reset_lgw.sh)

Starsze instrukcje instalacji Seeed zmieniają dwa przypisania resetu na GPIO17 i GPIO5, ale zachowują pozostałe wpisy projektu referencyjnego. Przed użyciem przykładu porównaj wartości z opisanym obrazem M1. [Instrukcje konfiguracji WM1302 od Seeed](https://github.com/seeed-lora/WM1302-doc)

| Przypisanie | Sprzeczne dane | Wymagana decyzja |
|---|---|---|
| **GPIO22 jako dodatkowy reset** | Obraz M1 opisuje go jako diodę użytkownika | Usuń to założenie przed włączeniem diody |
| **GPIO18 jako włączenie zasilania** | Obraz M1 opisuje go jako dodatkowe wyjście BUSY | Sprawdź połączenie i kierunek przed sterowaniem |
| **GPIO13 jako reset DAC** | Ogólny skrypt nazywa inny projekt referencyjny | Ustal, czy układ istnieje |
| **Dodatkowe urządzenie SPI** | Obraz M1 wybiera GPIO6 zamiast CE1 | Potwierdź połączenie chip select i obsługę sterownika |

**Wniosek:** jeśli GPIO18 łączy się z wyjściem dodatkowego radia, jak pokazano na rysunku, ustawienie portu Pi jako wyjścia stwarza ryzyko konfliktu elektrycznego. Ta rozbieżność wymaga weryfikacji, ale nie dowodzi uszkodzenia ani jednego uniwersalnego okablowania M1.

Przy odłączonym zasilaniu prześledź dostępne połączenia między złączem a modułem. Zapisz rewizję płytki i oba końce każdej ścieżki. Pomiar ciągłości potwierdza połączenie, natomiast dokumentacja podzespołu określa kierunek sygnału i limity elektryczne.

Skorzystaj z poniższego schematu producenta, aby nie pomylić pinów złącza krawędziowego z pinami nagłówka Pi. Oznaczenia dodatkowego radia opisują opublikowaną referencję modułu, nie potwierdzają identycznego układu ani obsługiwanych funkcji we wszystkich rewizjach. [Pinout modułu WM1302 od Seeed](https://github.com/seeed-lora/WM1302-doc/blob/master/pinout.jpg)

{{< figure src="wm1302-module-edge-connector.webp" alt="Rysunek Seeed z oznaczeniami obu stron złącza krawędziowego WM1302, zasilaniem, SPI, I2C i sygnałami dodatkowego radia" caption="Numeracja złącza krawędziowego modułu różni się od numeracji złącza Raspberry Pi" credit="Seeed Studio" attr="Seeed Studio, WM1302-doc" attrlink="https://github.com/seeed-lora/WM1302-doc" >}}

## Przygotuj Raspberry Pi OS

Zapisz środowisko hosta na zapasowej instalacji:

```bash
cat /etc/os-release
uname -r
tr -d '\0' < /proc/device-tree/model
```

Wersja systemu, jądro i model Pi stanowią punkt wyjścia do odtwarzalnych testów. Zapisz je przed porównaniem wyników ze starszym poradnikiem.

Zainstaluj narzędzia diagnostyczne i kompilacyjne:

```bash
sudo apt update
sudo apt install git build-essential i2c-tools gpiod
sudo raspi-config
```

W **Interface Options** włącz SPI i I2C, a następnie uruchom ponownie system. SPI obsługuje ścieżkę koncentratora, a I2C urządzenia zarządzające omówione poniżej. Nie kopiuj z poradnika o innym HAT-cie niezwiązanych zmian portu szeregowego GPS.

Sprawdź udostępnione interfejsy:

```bash
ls -l /dev/spidev* /dev/i2c-*
i2cdetect -l
gpiodetect
gpioinfo
gpioset --version
```

Polecenia wyświetlają pliki urządzeń, adaptery, kontrolery GPIO, informacje o liniach i wersję zainstalowanego narzędzia GPIO. **`i2cdetect -l` wyświetla adaptery bez skanowania adresów urządzeń.** Plik `/dev/spidev0.0` potwierdza dostępność interfejsu SPI, a nie komunikację z działającym koncentratorem. [Podręcznik i2c-tools](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), [Wskazówki GPIO Raspberry Pi](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

### Uwzględnij wersje GPIO

**Nie kopiuj globalnych numerów GPIO z innego urządzenia.** Starsze skrypty zapisują przez `/sys/class/gpio`, interfejs oznaczony w dokumentacji jądra jako przestarzały. Nowe integracje użytkowe powinny używać interfejsu urządzeń znakowych GPIO wraz z właściwym kontrolerem i przesunięciem linii. [Dokumentacja GPIO Linuksa](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html)

Przed dostosowaniem skryptu sprawdź też `gpioset --help`. Wersje 1 i 2 różnią się składnią i zachowaniem procesu. Obecne narzędzie domyślnie utrzymuje żądane linie, ale przenośna umowa interfejsu nie gwarantuje ich stanu po zakończeniu procesu. [Dokumentacja gpioset libgpiod](https://libgpiod.readthedocs.io/en/master/gpioset.html)

Raspberry Pi opisuje w jądrze zachowanie utrzymywania stanu wyjścia i opcje jego zmiany. Zapisz faktyczną konfigurację jądra, zamiast zakładać, że każdy system Linux zachowuje się identycznie. Zmiana numeracji ani nowsze narzędzie GPIO nie naprawią błędnego mapowania elektrycznego. [Przewodnik Raspberry Pi o GPIO](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)
## Przetestuj diodę użytkownika

Po potwierdzeniu, że GPIO22 jest połączone z diodą, i usunięciu konfliktujących odbiorców tej linii edytuj konfigurację rozruchową:

```bash
sudoedit /boot/firmware/config.txt
```

Współczesny Raspberry Pi OS montuje konfigurację rozruchową pod **`/boot/firmware/config.txt`**. Starsze obrazy używają `/boot/config.txt`, ścieżki z artykułu z 2023 roku. Przed edycją zrób kopię aktywnego pliku. [Dokumentacja config.txt Raspberry Pi](https://www.raspberrypi.com/documentation/computers/config_txt.html)

Dodaj nakładkę diody w sekcji dotyczącej twojego Pi, na przykład `[all]`:

```ini
dtoverlay=gpio-led,gpio=22,label=lorawan,trigger=heartbeat
```

Parametr **`gpio`** używa numeracji BCM. **`label`** nazywa urządzenie LED w Linuksie, a **`trigger=heartbeat`** przypisuje wyzwalacz sygnału życia jądra. Clockwork Bird podaje takie przypisanie dla M1, a dokumentacja nakładki Raspberry Pi opisuje te parametry. [Pierwotna obserwacja LED](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), [Dokumentacja nakładki gpio-led](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README)

Po ponownym uruchomieniu sprawdź zarejestrowaną diodę:

```bash
ls -l /sys/class/leds/
cat /sys/class/leds/lorawan/trigger
```

Oczekiwany wynik to wpis diody `lorawan` z `heartbeat` w nawiasach kwadratowych. Migająca dioda potwierdza działanie tej ścieżki GPIO i sterownika. Nie informuje o udanej rejestracji LoRaWAN, odbiorze radiowym ani stanie Helium.
## Zbadaj urządzenia I2C

**Adres I2C jest wskazówką, a nie identyfikatorem urządzenia.** Clockwork Bird zaobserwował odpowiedzi pod `0x60` i `0x39`, a następnie odczytał informacje ATECC608 przez bibliotekę kryptograficzną. Identyfikacja czujnika temperatury pozostała niepewna w oryginalnym artykule.

Zacznij od listy adapterów z poprzedniej sekcji. Szerokie skanowanie `i2cdetect` wysyła transakcje sondujące, a nie biernie obserwuje ruch. Podręcznik upstream ostrzega przed zakłóceniami. Nie skanuj rutynowo działającej bramy ani nieznanych podłączonych urządzeń. [Zachowanie sondowania i2c-tools](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8)

| Obserwacja | Wniosek poparty danymi | Nierozstrzygnięte pytanie |
|---|---|---|
| **Odpowiedź pod `0x60`** | Coś potwierdziło sondowanie | Czy to oczekiwany element zabezpieczający? |
| **Odpowiedź pod `0x39`** | Coś potwierdziło sondowanie | Jaki komponent i rewizja odpowiedziały? |
| **`UU` w skanowaniu** | Sterownik używa adresu, więc pominięto sondowanie | Który sterownik go używa? |
| **Brak odpowiedzi** | Sondowanie nie otrzymało potwierdzenia | Zasilanie, magistrala, właściciel czy protokół urządzenia? |

### Mocniejsza przesłanka dotycząca czujnika temperatury

**Źródła wskazują STTS751 jako kandydata dla `0x39`.** Nagłówek sterownika temperatury Semtech jawnie przypisuje `0x39` do `STTS751-0DP3F`. Wzmacnia to pierwotną hipotezę, lecz nie identyfikuje każdego egzemplarza płytki z tym adresem. [Nagłówek sterownika STTS751 Semtech](https://github.com/Lora-net/sx1302_hal/blob/master/libloragw/inc/loragw_stts751.h)

Po zidentyfikowaniu zgodnego elementu i upewnieniu się, że żaden inny proces go nie używa, odczytaj rejestry identyfikacyjne:

```bash
sudo i2cget 1 0x39 0xfd b
sudo i2cget 1 0x39 0xfe b
```

W poleceniach **`1`** wybiera zweryfikowaną magistralę, **`0x39`** urządzenie, a **`b`** żąda odczytu bajtu danych SMBus. Dla STTS751-0 udokumentowany identyfikator produktu pod `0xFD` to `0x00`, a identyfikator producenta pod `0xFE` to `0x53`. Te transakcje wybierają adresy rejestrów, ale nie zapisują wartości konfiguracji. [Nota katalogowa STTS751, mapa rejestrów i rejestry identyfikacyjne](https://www.st.com/resource/en/datasheet/stts751.pdf)

Porównaj wyniki z oznaczeniem układu i dokumentacją. Zgodna para wzmacnia identyfikację. Jeśli wystąpi błąd, przed zmianą konfiguracji sprawdź magistralę i jej właściciela. Czujnik mierzy temperaturę w swoim miejscu, co różni się od temperatury procesora Pi.
## Sprawdź element zabezpieczający

**ATECC608 jest osobnym elementem uwierzytelniającym.** Rozróżniaj konfigurację, numer seryjny, klucz publiczny i chronione dane klucza. Odczyt klucza publicznego nie ujawnia powiązanego klucza prywatnego.

**CryptoAuthLib** firmy Microchip zapewnia interfejs urządzenia. Repozytorium **cryptoauthtools** zawiera przykłady oparte na tej bibliotece. Zgodnie z instrukcjami tych projektów przygotuj natywną bibliotekę i wiązania Pythona dla systemu docelowego przed uruchomieniem przykładu. Instalacja niezwiązanego pakietu Pythona albo skopiowanie jednego skryptu nie potwierdza działania backendu I2C. [CryptoAuthLib firmy Microchip](https://github.com/MicrochipTech/cryptoauthlib), [cryptoauthtools firmy Microchip](https://github.com/MicrochipTech/cryptoauthtools)

W przygotowanym katalogu `cryptoauthtools/python/examples` uruchom polecenie inspekcji z oryginalnego artykułu:

```bash
sudo python3 info.py -i i2c
```

Argument **`-i i2c`** wybiera interfejs. W środowisku wirtualnym użyj jego jawnego interpretera Pythona i upewnij się, że znajduje właściwą bibliotekę natywną. W wielu instalacjach `sudo python3` wybiera interpreter systemowy, co wyjaśnia część błędów importu modułów.

Sprawdzony `info.py` odczytuje rewizję, numer seryjny, konfigurację i stan blokady. Gdy strefa danych jest zablokowana, próbuje pobrać klucz publiczny z gniazda 0. Nie uruchamia przykładowej procedury provisioningu. Sam błąd odczytu klucza publicznego z gniazda 0 nie dowodzi awarii urządzenia. [Kod źródłowy info.py firmy Microchip](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/info.py)

| Wynik lub operacja | Znaczenie |
|---|---|
| **Konfiguracja zablokowana** | Obowiązują ograniczenia konfiguracji |
| **Strefa danych zablokowana** | Interpretuj dostęp według skonfigurowanych zasad gniazd |
| **Wyświetlono klucz publiczny** | Pobrano dane publiczne, nie wyeksportowano klucza prywatnego |
| **Uruchomienie `config.py`** | Przykład provisioningu z operacjami konfiguracji, blokowania i generowania kluczy |

**Nie uruchamiaj `config.py`, aby naprawić błąd inspekcji.** Kod obejmuje zapisy konfiguracji, blokowanie stref i generowanie kluczy. Domyślna ścieżka generowania klucza ma znaczenie również na urządzeniu, które już skonfigurowano. [Kod źródłowy config.py firmy Microchip](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/config.py)

Udokumentowane profile provisioningu Microchip pokazują, dlaczego zablokowana strefa danych nie oznacza identycznych uprawnień dla każdego gniazda. Profile nie potwierdzają dokładnej konfiguracji M1. Zachowaj istniejącą konfigurację urządzenia i przed planowaniem ponownego użycia kluczy sprawdź dokumentację właściwego układu. [Zasady dostępu do pamięci i gniazd Microchip](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html)
## Uwzględnij niewiadome dotyczące wentylatora i przycisku

**Trzypinowe złącze wentylatora nie określa napięcia, polaryzacji ani metody sterowania.** Sfotografuj numerację pinów i odczytaj etykietę wentylatora. Przed podłączeniem zamiennika lub wyborem nakładki GPIO ustal połączenia zasilania i sterowania.

Oryginalne badanie nie ustaliło też GPIO przycisku. Znajdź sterownik lub konfigurację dla swojej rewizji płytki, a następnie przy odłączonym zasilaniu zweryfikuj połączenia. Nie ustawiaj każdej pozornie wolnej linii GPIO jako wyjścia w poszukiwaniu przycisku.

| Urządzenie peryferyjne | Zbierane dane | Kryterium akceptacji |
|---|---|---|
| **Zasilanie wentylatora** | Parametry wentylatora, masa złącza i zasilanie | Zmierzone zasilanie odpowiada specyfikacji wentylatora |
| **Sterowanie wentylatorem** | Sterownik/konfiguracja lub prześledzony obwód sterujący | Określone zachowanie przy uruchomieniu i podwyższonej temperaturze |
| **Przycisk użytkownika** | Okablowanie styków, mapowanie GPIO, polaryzacja wejścia | Jedno celowe naciśnięcie wywołuje oczekiwane zdarzenie |

Nowa instalacja systemu nie odtwarza automatycznie polityki chłodzenia oryginalnego urządzenia. Podczas pierwszego dłuższego testu obserwuj jednocześnie pracę wentylatora i temperatury. Zachowaj przepływ powietrza w obudowie i przerwij test, jeśli zestaw nie ma wymaganego chłodzenia.
## Wybierz stos bramy

**Oddziel obsługę płytki od protokołu serwera.** Zgodny serwer LoRaWAN nie naprawi nieprawidłowej procedury resetu ani kalibracji RF. Najpierw wybierz oprogramowanie obsługujące koncentrator, okablowanie nośnika, system operacyjny i konfigurację regionalną.

| Ścieżka programowa | Zastosowanie | Sprawdź przed wdrożeniem |
|---|---|---|
| **Semtech SX1302 HAL** | Uruchamianie i diagnostyka na poziomie źródła | Procedura resetu płytki i konfiguracja modułu |
| **LoRa Basics Station** | Uwierzytelnione połączenie bramy z serwerem | Działająca integracja płytki i dane dostępowe serwera |
| **ChirpStack Concentratord** | Dedykowana usługa koncentratora | Obsługiwany model, kalibracja i mapowanie GPIO |

ChirpStack wymienia model SPI **`seeed_wm1302`**. To potwierdza obsługę modułu, ale nie gwarantuje kompletnego obrazu M1 ani obsługi każdej rewizji M1. Nie traktuj osobnych instrukcji instalacji SenseCAP M2 jako instrukcji firmware M1. [Obsługa sprzętu w ChirpStack](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html), [Cel instalacji Seeed w ChirpStack](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html)

Dokumentacja The Things Stack zaleca **LoRa Basics Station** zamiast starszego forwardera UDP Semtech. Station oferuje TLS i uwierzytelnianie tokenem oraz funkcje centralnej konfiguracji. Przykłady UDP pomagają zrozumieć przekazywanie pakietów, lecz ustawienia adresu serwera nie zapewniają tych zabezpieczeń. [Wskazówki UDP The Things Stack](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [Dokumentacja LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/)

### Przygotuj narzędzia upstream

Kompiluj na docelowym Pi w nowym katalogu roboczym:

```bash
git clone https://github.com/Lora-net/sx1302_hal.git
cd sx1302_hal
git rev-parse HEAD
make
```

Zapisz identyfikator commitu razem z wynikami kompilacji. Udana kompilacja potwierdza zgodność kompilatora, ale radio nadal wymaga zweryfikowanej implementacji resetu i poprawnej konfiguracji. Dokumentacja Semtech opisuje rolę HAL i narzędzi pomocniczych. [Dokumentacja kompilacji i narzędzi SX1302 HAL](https://github.com/Lora-net/sx1302_hal)

Sprawdź plik resetu przed uruchomieniem narzędzi dostępu do sprzętu:

```bash
sed -n '1,180p' tools/reset_lgw.sh
```

Nie kopiuj tego pliku bez zmian do katalogu środowiska wykonawczego. Semtech opisuje automatyczne użycie skryptu resetu przez programy dostępu do sprzętu, w tym narzędzia identyfikacyjne. Sprawdź każdą przypisaną linię, kierunek sygnału, API GPIO i stan przy uruchamianiu oraz zamykaniu.

Po zweryfikowaniu płytki postępuj zgodnie z instrukcjami wybranego stosu, aby odczytać EUI koncentratora i zarejestrować bramę. Zachowaj kalibrację modułu i ustawienia RF podczas dodawania konfiguracji serwera. W konfiguracji UDP Semtech `gateway_ID` oznacza EUI. Gateway ID w konsoli The Things Stack jest czytelnym identyfikatorem rejestracji. [Konfiguracja bramy w The Things Stack](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/)
## Potwierdź dostarczanie danych z czujnika

**Użyj etapowych danych, by znaleźć pierwszą niedziałającą warstwę.** Brama ze statusem online ma połączenie z serwerem. Test akceptacyjny wymaga też znanego czujnika, zgodnego planu częstotliwości i zdekodowanego ładunku aplikacji.

Poniższa sekwencja to proponowany plan testów, a nie zmierzone wyniki M1:

| Punkt kontrolny | Dowód do zapisania | Znaczenie |
|---|---|---|
| **Host gotowy** | System, jądro, zasilanie i spis interfejsów | Przygotowanie Linuksa zakończone |
| **Koncentrator odpowiada** | EUI i poprawny log inicjalizacji | Komunikacja hosta z koncentratorem działa |
| **Radio odbiera** | Oczekiwany pakiet czujnika i metadane odbioru | Skonfigurowana ścieżka odbioru działa |
| **Serwer przyjmuje** | Zdarzenie bramy powiązane z czujnikiem | Przekazywanie i routing serwera działają |
| **Aplikacja dekoduje** | Oczekiwany pomiar i znacznik czasu | Ścieżka aplikacji działa |
| **Odzyskiwanie po restarcie** | Te same kontrole po ponownym uruchomieniu | Konfiguracja startowa jest powtarzalna |

W przypadku czujnika **OTAA** potwierdź też wymianę aktywacyjną i późniejszy uplink. OTAA oznacza aktywację przez powietrze, czyli procedurę dołączenia ustanawiającą sesję. Sam odebrany wniosek o dołączenie nie potwierdza udanego dołączenia ani ścieżki downlink. [Dokumentacja aktywacji The Things Stack](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/)

**Przykład diagnozy:** brama łączy się z serwerem i podaje EUI, ale czujnik się nie pojawia. Najpierw sprawdź konfigurację nadawania czujnika, wybrane kanały odbioru, ścieżkę anteny i logi radiowe. Ponowne programowanie ATECC608 nie uzupełni brakującego dowodu w tym przypadku.

**Drugi przykład:** pakiet czujnika pojawia się lokalnie, ale nie trafia do aplikacji. Porównaj czas pakietu ze zdarzeniami bramy i serwera, a następnie sprawdź routing, rejestrację urządzenia i dekodowanie. Pakiet RF w logu nie wystarcza, by obwinić dekoder ładunku, zanim serwer zaakceptuje zdarzenie.
## Rozwiąż problemy według objawów

| Objaw | Najpierw sprawdź | Następne działanie |
|---|---|---|
| **Brak pliku urządzenia SPI** | Aktywna konfiguracja rozruchowa i ustawienia interfejsu | Włącz właściwy interfejs i uruchom system ponownie |
| **SPI jest dostępne, radio nie działa** | Zasilanie, osadzenie modułu, sekwencja resetu i chip select | Zweryfikuj ścieżkę elektryczną przed zmianą serwera |
| **Błąd eksportu GPIO** | Założenia o starszym sysfs i zainstalowanym jądrze | Użyj sprawdzonej implementacji dla API GPIO |
| **GPIO jest już zajęte** | Odbiorca widoczny w `gpioinfo` | Rozwiąż konflikt właściciela przed ponowną próbą |
| **Dioda nie działa po konfiguracji** | Zastosowanie nakładki i konflikty GPIO22 | Sprawdź zarejestrowane urządzenia LED i skrypt resetu |
| **Brak urządzenia I2C** | Numer magistrali, zasilanie i istniejący właściciel | Sprawdź problem bez powtarzania szerokich skanów |
| **Błąd importu biblioteki kryptograficznej** | Interpreter, wiązania i ścieżka biblioteki natywnej | Napraw środowisko programowe |
| **Odczyt klucza publicznego nie działa** | Polityka gniazda i wcześniejsze udane odczyty | Sprawdź konfigurację bez provisioningu |
| **Wentylator nie działa** | Zweryfikowane zasilanie i implementację chłodzenia | Przywróć prawidłowe chłodzenie przed dłuższymi testami |
| **Uplinki docierają, dołączenie nie działa** | Ścieżkę downlink i ustawienia regionalne/urządzenia | Prześledź odpowiedź na dołączenie i okna odbioru |

Każdą zmianę traktuj jako osobny eksperyment. Zapisz poprzednią konfigurację, zmień jedną wartość, powtórz tę samą kontrolę i zanotuj, czy pojawił się oczekiwany dowód.
## Utwórz dokumentację sprzętu

Użyj tego szablonu, aby przygotować powtarzalny protokół przekazania:

```text
Wersja nośnika i zdjęcia:
Model koncentratora, interfejs i pasmo RF:
Model hosta / system operacyjny / wersja jądra / wersja narzędzia GPIO:
Zasilanie / antena / układ chłodzenia:
Zweryfikowane mapowanie pinów i dowody:
Nierozpoznane połączenia i wykluczone funkcje:
Repozytorium oprogramowania i commit:
Implementacja resetu i obsługa GPIO:
EUI bramy / serwer / plan częstotliwości:
Aktywacja czujnika i dowody zdekodowanego uplinku:
Wynik odzyskiwania po ponownym uruchomieniu:
Lokalizacja oryginalnej karty i procedura wycofania zmian:
```

**Ćwiczenie decyzyjne:** możesz kupić tani nośnik bez oznaczenia modułu albo droższy zestaw z czytelnymi oznaczeniami i udokumentowanym działaniem. Uwzględnij brakujące Pi, koncentrator, antenę, zasilacz i czas weryfikacji, a następnie zdecyduj, co pasuje do projektu. Lepszy wybór wynika z całkowitego kosztu i wymaganego poziomu dowodów dla planowanej usługi, a nie wyłącznie z reklamowanej ceny nośnika.

**Oczekiwane rozumowanie:** projekt edukacyjny toleruje nierozstrzygnięte połączenia, jeśli masz narzędzia pomiarowe i czas. Brama obsługująca działające czujniki wymaga powtarzalnego startu, chłodzenia, wsparcia programowego i potwierdzonego dostarczania danych. Zapisz, który nierozstrzygnięty warunek zatrzymałby wdrożenie.
## Następne kroki

Zacznij od dokumentacji sprzętu i rozstrzygnięcia rozbieżności w skryptach resetu. Następnie uruchom jeden znany czujnik i zapisz dowód aż do dekodowania w aplikacji, zanim dodasz kolejne urządzenia.

**Protokół akceptacji:** zapisz rewizję płytki, oznaczenie modułu, pasmo radiowe, pomiar zasilania, aktywne urządzenie SPI, nazwy linii GPIO, sekwencję resetu, log koncentratora, połączenie z serwerem i jeden zdekodowany uplink. Oznacz każdą wartość jako zaobserwowaną, udokumentowaną lub nadal założoną. Samo uruchomienie procesu nie potwierdza wydajności RF ani dostarczenia danych do aplikacji.

Jeśli twoim celem jest przesyłanie wiadomości w sieci mesh, najpierw porównaj role protokołów w naszym [przewodniku po Meshtastic, MeshCore i Reticulum](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/). Wspólna technologia radiowa LoRa nie potwierdza zgodności firmware. W przypadku wdrożenia komunikacyjnego sprawdź [dokumentację obsługiwanego sprzętu MeshtasticD](https://meshtastic.org/docs/meshtasticd/), zamiast traktować tę procedurę LoRaWAN jako konwersję do Meshtastic.
## Źródła i autorstwo ilustracji

Badanie sprawdzono 12 września 2026 r. Niedatowane linki do dokumentacji i repozytoriów prowadzą do wersji przejrzanych na potrzeby tego artykułu. Lokalne ilustracje zachowują oryginalne oznaczenia i przypisane pochodzenie.

| Wydawca | Źródło i data |
|---|---|
| **Clockwork Bird** | [SenseCAP M1 Raspberry Pi Shield](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), 2023-05-03. Zdjęcie płytki, opisane złącze i odtworzony schemat blokowy producenta |
| **Seeed Studio / SenseCAP** | [Przegląd i specyfikacja M1](https://www.sensecapmx.com/docs/sensecap-m1/overview/), bez daty. Pierwotne przypisanie autorstwa schematu blokowego |
| **Seeed Studio** | [Dokumentacja WM1302 i pinout modułu](https://github.com/seeed-lora/WM1302-doc), repozytorium |
| **Semtech** | [SX1302/SX1303 HAL](https://github.com/Lora-net/sx1302_hal), w tym powiązane źródła skryptu resetu i sterownika temperatury |
| **Raspberry Pi** | [Konfiguracja rozruchowa](https://www.raspberrypi.com/documentation/computers/config_txt.html), [przewodnik GPIO](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices) i [dokumentacja nakładek](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README) |
| **Linux / libgpiod** | [Przestarzały interfejs GPIO sysfs](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html) oraz [podręcznik gpioset](https://libgpiod.readthedocs.io/en/master/gpioset.html), ten ostatni z sierpnia 2026 r. |
| **i2c-tools** | [Podręcznik i2cdetect](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), kod źródłowy v4.3 |
| **STMicroelectronics** | [Nota katalogowa STTS751](https://www.st.com/resource/en/datasheet/stts751.pdf), rewizja 7 |
| **Microchip** | [CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib), [cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools) i [dokumentacja polityk dostępu do gniazd](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html) |
| **ChirpStack** | [Obsługa sprzętu Concentratord](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html) i [cel instalacyjny Seeed](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html) |
| **The Things Industries** | [Forwarder UDP](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/) i [aktywacja urządzenia](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/) |
| **Meshtastic** | [Dokumentacja MeshtasticD](https://meshtastic.org/docs/meshtasticd/), bez daty |
