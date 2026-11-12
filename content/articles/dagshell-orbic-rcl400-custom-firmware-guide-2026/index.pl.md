---
title: "Niestandardowe oprogramowanie układowe DagShell dla Orbic RCL400: przewodnik na 2026 rok"
date: 2026-05-28
lastmod: 2026-11-11
toc: true
draft: false
description: "Techniczny przewodnik po oprogramowaniu DagShell dla Orbic RCL400. Opisuje instalację, narzędzia ochrony prywatności, wardriving i ograniczenia badań."
genre: ["Niestandardowe oprogramowanie układowe", "Bezpieczeństwo urządzeń mobilnych", "Narzędzia ochrony prywatności", "Bezpieczeństwo sieci", "Wardriving", "Testy penetracyjne", "Hakowanie IoT", "Badania bezpieczeństwa", "Hakowanie sprzętu", "Technologie ochrony prywatności"]
tags: ["DagShell", "Orbic RCL400", "Niestandardowe oprogramowanie układowe", "Hakowanie hotspotów", "Narzędzia ochrony prywatności", "Naprawa TTL", "Podszywanie się pod adres MAC", "Wykrywanie IMSI catcherów", "Wardriving", "Śledzenie GPS", "Atak Evil Twin", "Portal przechwytujący", "Sniffer DNS", "Skaner ARP", "Skaner portów", "Dodatek Raspberry Pi", "Bezpieczeństwo Wi-Fi", "Mobilny hotspot", "Monitorowanie sieci", "Testy penetracyjne", "Badania bezpieczeństwa", "Skanowanie Bluetooth", "Atak deautoryzacji", "Skanowanie Wi-Fi", "Wyszukiwanie OUI", "Przesyłanie do Wigle", "Monitorowanie wież komórkowych", "Polecenia AT", "Menedżer zapory", "Blokowanie reklam", "Szyfrowanie TLS", "Integracja z RayHunter", "STS Collective", "Laboratorium bezpieczeństwa mobilnego", "Analiza sieci", "Oprogramowanie układowe chroniące prywatność", "Bezpieczeństwo open source", "Kompilacja skrośna dla ARM", "Wbudowany Linux", "Zestaw narzędzi bezpieczeństwa", "Narzędzia hakerskie", "Red team", "Rozpoznanie sieci"]
canonical: "https://simeononsecurity.com/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/"
cover: "/img/cover/dagshell-orbic-rcl400-custom-firmware-guide-2026.webp"
coverAlt: "Ilustracja mobilnego hotspotu Orbic RCL400 ze świecącym zielonym interfejsem. Wokół niego znajdują się abstrakcyjne symbole narzędzi bezpieczeństwa, takich jak wykresy i mapy, na granatowym tle."
coverCaption: ""
---

**Zmień Orbic RCL400 w mobilne laboratorium badań bezpieczeństwa**

## Wprowadzenie: hotspot dla hakerów

**DagShell** to niestandardowe oprogramowanie układowe open source dla **mobilnego hotspotu Orbic RCL400**. Zmienia zwykłe urządzenie komórkowe w **przenośny zestaw narzędzi do badań bezpieczeństwa i ochrony prywatności**. Badacz bezpieczeństwa znany jako „dag” stworzył to oprogramowanie z interfejsem w stylu terminala. Zawiera ono **narzędzia hakerskie, funkcje ochrony prywatności i funkcje monitorowania sieci**, a jego wygląd nawiązuje do zielonych napisów na czarnym tle.

Ten obszerny przewodnik opisuje:
- **Czym jest DagShell** i jakie funkcje oferuje
- **Instrukcje instalacji krok po kroku**, przez webflasher i metodą ręczną
- **Narzędzia i funkcje** wraz ze szczegółowymi objaśnieniami
- **Konfigurację dodatku Raspberry Pi**, który rozszerza możliwości zestawu
- **Powody, by połączyć DagShell z RayHunterem** w mobilnym laboratorium bezpieczeństwa
- **Praktyczne zastosowania** dla badaczy bezpieczeństwa i osób dbających o prywatność
- **Aspekty prawne i etyczne**

**W skrócie:** DagShell i RayHunter na Orbic RCL400 tworzą **kompletne mobilne laboratorium bezpieczeństwa** do wykrywania IMSI catcherów, wardrivingu, analizy sieci i ochrony prywatności.

**Urządzenia z wgranym oprogramowaniem:** Artykuł powstał we współpracy ze **STS Collective**, które oferuje hotspoty Orbic RCL400 z wcześniej zainstalowanymi RayHunterem i DagShell, gotowe do użycia: [stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)

> 💰 **Rabat dla czytelników:** Otrzymaj do 20% zniżki na produkty STS Collective, w tym hotspoty Orbic RCL400 z wgranym oprogramowaniem. Przy płatności użyj kodu **SIMEONONSECURITY** lub [przejdź do sklepu z naliczoną zniżką](https://stscollective.com/discount/SIMEONONSECURITY).

______

## Czym jest DagShell?

### Przegląd

**DagShell** to niestandardowe oprogramowanie układowe open source, które zastępuje standardowy interfejs WWW Orbic RCL400 **rozbudowanym zestawem narzędzi bezpieczeństwa**. Obejmuje on:

- **Interfejs w stylu terminala** z grafiką ASCII i estetyką hakerską
- **Szyfrowany interfejs WWW TLS 1.2+** z certyfikatem samopodpisanym
- **Narzędzia ochrony prywatności**, takie jak maskowanie TTL, podszywanie się pod adres MAC i blokowanie reklam przez DNS
- **Monitorowanie sieci**, w tym aktywne połączenia, tablice routingu i zapytania DNS
- **Narzędzia hakerskie**, takie jak wykrywanie IMSI catcherów, skanowanie portów i wykrywanie urządzeń przez ARP
- **Możliwości ataku**, w tym Evil Twin AP, wyłudzanie danych przez portal przechwytujący i ataki deautoryzacji
- **Śledzenie GPS i wardriving** z eksportem CSV zgodnym z Wigle
- **Dodatek Raspberry Pi** do GPS, skanowania Bluetooth i rozpoznania sieci Wi-Fi
- **Dostęp do systemu plików** przez menedżer plików w przeglądarce
- **Obsługę SMS** przez polecenia AT
- **Trwałość działania**, DagShell uruchamia się automatycznie po starcie urządzenia

### Specyfikacja techniczna

**Platforma:** mobilny hotspot Orbic RCL400\
**Architektura:** ARM Linux (jądro 3.18)\
**Język:** C/C++ (statyczny plik binarny ARM)\
**Szyfrowanie:** TLS 1.2+ z certyfikatami samopodpisanymi (dwupoziomowa infrastruktura PKI)\
**Serwer WWW:** niestandardowy, wbudowany serwer HTTPS (port 8443)\
**Interfejs:** terminalowy interfejs w przeglądarce\
**Licencja:** MIT (open source)\
**GitHub:** [github.com/dagnazty/DagShell](https://github.com/dagnazty/DagShell)

### Wygląd

DagShell ma **retro-hakerski wygląd**:
- **Logo z grafiki ASCII** na każdej stronie
- **Zielona kolorystyka na czarnym tle**, inspirowana filmem Matrix
- **Czcionka o stałej szerokości znaków** (Fira Code)
- **Efekty linii skanowania** i świecący tekst
- **Układ inspirowany terminalem**

{{< figure src="dagshell-orbic-rcl400-hacker-terminal-interface-feature-overview.webp" alt="Niestandardowe oprogramowanie DagShell uruchomione na Orbic RCL400. Widać zielony interfejs terminala z grafiką ASCII i menu narzędzi bezpieczeństwa." >}}

______

## Pełny przegląd funkcji

### 🏠 Panel główny

**Przegląd systemu:**
- **Czas działania** urządzenia
- **Interfejs poleceń AT**, bezpośrednie sterowanie modemem dla zaawansowanych użytkowników
- **Szybki status**, adres IP i stan połączenia

**Polecenia AT** umożliwiają niskopoziomowe sterowanie modemem:
```
Example AT Commands:
AT+CSQ       - Signal quality
AT+COPS?     - Current network operator  
AT+CREG?     - Network registration status
AT+CIMI      - Get IMSI (subscriber identity)
AT+CGSN      - Get IMEI (device identifier)
```

### 🌐 Narzędzia sieciowe

**Bieżące informacje o sieci:**
- **Adres IP i interfejs**
- **Maska podsieci, brama** i adres rozgłoszeniowy
- **Statystyki sieci**, liczba wysłanych i odebranych pakietów

**Podgląd tablicy routingu:**
- Lista wszystkich tras sieciowych
- Informacje o bramie domyślnej
- Przypisanie interfejsów

**Monitor aktywnych połączeń:**
- Lista **wszystkich połączeń TCP/UDP** w czasie rzeczywistym
- Lokalne i zdalne adresy IP
- Numery portów i stany połączeń
- Przydatny do **monitorowania komunikacji urządzenia z siecią**

### Zestaw narzędzi ochrony prywatności

#### Naprawa TTL

**Cel:** ukrycie ruchu hotspotu przed wykryciem przez operatora

**Zasada działania:**
- Zmienia wartość **Time To Live (TTL)** w pakietach IP na **65**
- Operatorzy wykrywają tethering przez zmiany TTL: telefon wysyła wartość 64, a urządzenie podłączone do niego wartość 63
- Ustawienie TTL na 65 sprawia, że **cały ruch wygląda na lokalny**

**Zastosowanie:** omijanie ograniczeń lub ograniczania prędkości tetheringu przez operatora

**Polecenia:**
```bash
# Enable TTL fix
iptables -t mangle -A POSTROUTING -j TTL --ttl-set 65

# Disable TTL fix  
iptables -t mangle -D POSTROUTING -j TTL --ttl-set 65
```

#### Podszywanie się pod adres MAC

**Cel:** losowa zmiana adresu MAC urządzenia w celu ochrony prywatności

**Zasada działania:**
- Zmienia adres MAC interfejsu Wi-Fi **wlan0**
- Generuje **losowy adres MAC** lub pozwala wpisać własny
- Utrudnia **śledzenie urządzenia** między sesjami

**Zastosowanie:** zapobieganie śledzeniu na podstawie adresu MAC przez sieci, z którymi się łączysz

**Przebieg:**
1. Interfejs zostaje wyłączony
2. Zostaje ustawiony nowy adres MAC
3. Interfejs uruchamia się ponownie
4. Połączenie zostaje nawiązane ponownie

#### Blokowanie reklam przez DNS

**Cel:** blokowanie reklam i śledzenia na poziomie DNS

**Zasada działania:**
- Modyfikuje plik `/etc/hosts`, dodając do niego **listę blokowanych domen**
- Domeny z listy kieruje na **127.0.0.1** (localhost)
- Blokuje reklamy **na wszystkich podłączonych urządzeniach**

**Zastosowanie:** blokowanie reklam w całej sieci bez konfiguracji każdego urządzenia z osobna

**Źródło listy:** popularne domeny reklamowe i śledzące. Listę można dostosować.

### 📱 Obsługa SMS

**Wysyłanie SMS-ów:**
- Wysyła wiadomości tekstowe do modemu przez **polecenia AT**
- Przydatne do **zdalnych powiadomień** i testów

**Przeglądanie wiadomości:**
- Otwiera natywną skrzynkę odbiorczą Orbic
- Pozwala czytać odebrane SMS-y

**Używane polecenie AT:**
```
AT+CMGS="PHONE_NUMBER"
Message text here^Z
```

### 🔧 Narzędzia hakerskie

#### Wykrywanie IMSI catcherów

**Cel:** monitorowanie informacji o wieżach komórkowych i wykrywanie anomalii wskazujących na urządzenia typu **IMSI catcher/Stingray**

**Zasada działania:**
- Pobiera z modemu **dane wieży komórkowej**:
  - **Cell ID**, identyfikator wieży
  - **LAC**, kod obszaru lokalizacji
  - **MCC/MNC**, kod kraju i kod sieci komórkowej
  - **Siła sygnału** (RSSI)
  - **Generacja sieci** (2G/3G/4G)
- **Rejestruje zmiany**, by wykrywać podejrzane przełączenia wież
- **Śledzi wartości bazowe**, czyli typowe wieże w danym obszarze

**Wskaźniki wykrycia:**
- **Nagła zmiana wieży komórkowej** podczas postoju
- **Przejście na 2G** *(IMSI catchery często wymuszają 2G, by usunąć szyfrowanie)*
- Pojawienie się **nieznanego Cell ID**
- **Słaby sygnał** z fałszywej wieży
- **Częste ponowne połączenia**

**Współpraca z RayHunterem:** DagShell **monitoruje wieże komórkowe**, a RayHunter zapewnia **dedykowane wykrywanie IMSI catcherów** z bardziej zaawansowaną analizą. Szczegóły znajdziesz w dalszej sekcji.

#### Skaner portów

**Cel:** skanowanie docelowych adresów IP w poszukiwaniu otwartych portów

**Zasada działania:**
- **Skanowanie TCP SYN** wysyła pakiety SYN do portów celu
- **Wykrywanie limitu czasu** pomaga ustalić, czy port jest otwarty, zamknięty lub filtrowany
- **Obsługa zakresów** pozwala skanować jeden port albo ich zakres

**Zastosowania:**
- **Rozpoznanie sieci**
- **Wykrywanie urządzeń IoT**
- **Audyt bezpieczeństwa** lokalnych sieci
- **Identyfikacja usług**

**Polecenie:**
```bash
# Scan ports 1-1000 on target
nc -zv -w 2 TARGET_IP 1-1000 2>&1
```

#### Menedżer zapory

**Cel:** blokowanie lub odblokowywanie adresów IP za pomocą iptables

**Zasada działania:**
- Reguły **iptables** odrzucają pakiety z wybranych adresów IP lub do nich
- **Trwałe reguły** działają po ponownym uruchomieniu, jeśli zostały zapisane
- Obsługa **białej i czarnej listy**

**Zastosowania:**
- **Blokowanie złośliwych adresów IP**
- **Zapobieganie nieautoryzowanemu dostępowi**
- **Kształtowanie lub filtrowanie ruchu**
- **Kontrola rodzicielska**

**Polecenia:**
```bash
# Block IP
iptables -I INPUT -s IP_ADDRESS -j DROP
iptables -I OUTPUT -d IP_ADDRESS -j DROP

# Unblock IP
iptables -D INPUT -s IP_ADDRESS -j DROP
iptables -D OUTPUT -d IP_ADDRESS -j DROP
```

### ⚔️ Narzędzia do ataków

**WAŻNE OSTRZEŻENIE PRAWNE:** Te narzędzia służą **WYŁĄCZNIE do autoryzowanych testów bezpieczeństwa**. Używanie ich przeciwko sieciom, których nie posiadasz lub na których testowanie nie masz wyraźnej pisemnej zgody, jest **NIELEGALNE** w większości jurysdykcji (w USA na mocy Computer Fraud and Abuse Act, w Wielkiej Brytanii Computer Misuse Act itd.). Używaj ich wyłącznie **we własnych sieciach** lub w **kontrolowanych laboratoriach**.

#### Sniffer DNS

**Cel:** rejestrowanie zapytań DNS od podłączonych klientów

**Zasada działania:**
- **Rejestrowanie przez iptables** ruchu na porcie 53 (DNS)
- **Nie wymaga trybu promiscuous**
- Rejestruje wszystkie zapytania DNS klientów hotspotu
- Ujawnia, **jakie witryny i usługi** otwierają klienci

**Zastosowania** (za zgodą):
- **Analiza ruchu sieciowego**
- **Nadzór rodzicielski** we własnej rodzinie
- **Badania bezpieczeństwa** własnych urządzeń
- **Analiza działania złośliwego oprogramowania**

*To narzędzie przechwytuje metadane, czyli odwiedzane domeny, z podłączonych klientów. Wdrażaj je wyłącznie w sieciach, które posiadasz lub administrujesz.*

#### Skaner ARP

**Cel:** wykrywanie urządzeń w sieci lokalnej

**Zasada działania:**
- Wysyła **żądania ARP** do wszystkich adresów IP w podsieci
- Urządzenia odpowiadają swoimi **adresami MAC**
- **Wyszukiwanie OUI** pomaga ustalić producenta (Apple, Samsung itd.)
- Tworzy **mapę aktywnych urządzeń** w sieci

**Zastosowania:**
- **Inwentaryzacja sieci**
- **Wykrywanie nieznanych urządzeń**
- **Analiza sieci BYOD**
- **Wykrywanie urządzeń IoT**

**Przykładowy wynik:**
```
IP: 192.168.1.50
MAC: A4:83:E7:XX:XX:XX
Vendor: Apple, Inc.

IP: 192.168.1.75
MAC: 2C:54:91:XX:XX:XX
Vendor: Samsung Electronics
```

#### Traceroute

**Cel:** wizualizacja trasy sieciowej do miejsca docelowego

**Zasada działania:**
- Wysyła pakiety z **rosnącą wartością TTL**
- Każdy przeskok zmniejsza TTL i zwraca komunikat **ICMP Time Exceeded**
- Ujawnia **routery i trasę** do celu
- Mierzy **czas podróży w obie strony (RTT)** dla każdego przeskoku

**Zastosowania:**
- **Diagnozowanie problemów z siecią**
- **Analiza tras**
- **Diagnozowanie opóźnień**
- **Badanie połączeń między sieciami operatorów**

#### Fałszywy punkt dostępu (Evil Twin AP)

**Cel:** utworzenie fałszywego punktu dostępu Wi-Fi, który kopiuje nazwę istniejącej sieci

**Zasada działania:**
- Korzysta z **wlan1**, drugiego interfejsu Wi-Fi, jeśli jest dostępny przez dodatek Pi
- Kopiuje **SSID i typ szyfrowania** sieci docelowej
- **Przechwytuje klientów**, którzy próbują się połączyć
- Wyświetla **portal przechwytujący**, by pozyskać dane logowania

**Scenariusz ataku** (laboratorium):
1. Wyszukaj legalne sieci Wi-Fi
2. Utwórz **fałszywy punkt dostępu** z tą samą nazwą SSID
3. Użyj **ataku deautoryzacji**, by odłączyć klientów od prawdziwego punktu dostępu
4. Urządzenia automatycznie łączą się ponownie z **fałszywym punktem dostępu**
5. Portal przechwytujący zapisuje dane logowania

*Wykrywanie: jeśli oba punkty dostępu są widoczne jednocześnie, klienci zobaczą **powielone nazwy SSID**.*

#### Portal przechwytujący

**Cel:** szablony stron phishingowych służących do pozyskiwania danych logowania

**Dostępne szablony:**
- **Strona logowania do Wi-Fi** w stylu operatora lub hotelu
- **Strony logowania do mediów społecznościowych**, imitujące Facebooka, Twittera i Instagrama
- **Portale logowania firmowego**
- **Strony dostępu do Wi-Fi** na lotnisku lub w kawiarni

**Zasada działania:**
1. Fałszywy punkt dostępu przekierowuje **cały ruch** do portalu
2. Klient widzi **stronę logowania**
3. Klient wpisuje dane
4. Dane logowania zostają **zapisane do pliku**
5. Klient otrzymuje dostęp do internetu albo widzi komunikat o błędzie

**Cel edukacyjny:** pokazanie zagrożeń związanych z **inżynierią społeczną** i tego, dlaczego użytkownicy powinni sprawdzać adresy URL

### 📍 Lokalizator GPS i wardriving

#### Funkcje GPS

**Źródło GPS:** wyłącznie **dodatek Raspberry Pi**
- *Orbic RCL400 **nie ma wbudowanego GPS**. Bez dodatku Pi urządzenie nie zapisuje danych lokalizacyjnych.*
- Pi podłącza **odbiornik GPS USB** z układem U-Blox 7
- Pi przesyła współrzędne do Orbic przez **współdzielone pliki danych**
- Konwersja **ECEF na szerokość i długość geograficzną** odbywa się automatycznie

**Dane na panelu:**
- **Szerokość i długość geograficzna** w stopniach dziesiętnych
- **Wysokość** nad poziomem morza
- **Stan ustalenia pozycji GPS** i dokładność
- **Automatyczne odświeżanie** co 5 sekund
- **Bez okien z prośbą o geolokalizację w przeglądarce**, funkcja nie korzysta z jej API

**Współdzielony stan GPS:**
- Dane GPS są dostępne dla **wszystkich procesów DagShell**
- Tryb wardrivingu automatycznie korzysta z GPS
- Funkcje nie wchodzą ze sobą w konflikt

#### Tryb wardrivingu

**Cel:** skanowanie sieci Wi-Fi wraz ze współrzędnymi GPS na potrzeby mapowania

**Zasada działania:**
1. Czeka na **prawidłowe ustalenie pozycji GPS**, nie zapisuje współrzędnych 0,0
2. Skanuje sieci Wi-Fi co **5 sekund** w pętli ciągłej
3. Zapisuje dane sieci:
   - **SSID**, nazwę sieci
   - **BSSID**, adres MAC
   - **Typ szyfrowania**, WPA2, WPA3 lub otwarte
   - **Siłę sygnału**, RSSI w dBm
   - **Numer kanału**
   - **Współrzędne GPS**, szerokość i długość geograficzną
   - **Znacznik czasu**
4. Eksportuje dane do **pliku CSV zgodnego z Wigle**

**Integracja z Wigle:**
- **WiGLE** (wigle.net) to globalny projekt mapowania sieci Wi-Fi
- Plik CSV DagShell można **bezpośrednio przesłać** do WiGLE
- **Przesyłanie z przeglądarki** ze strony Pliki nie wymaga dodatkowych narzędzi
- Dane trafiają do **publicznej bazy** lokalizacji sieci Wi-Fi

**Zastosowania:**
- **Mapowanie zasięgu Wi-Fi**
- **Badanie sieci** na potrzeby operatorów internetowych
- **Analiza siły sygnału**
- **Badania bezpieczeństwa**, na przykład otwartych sieci i słabego szyfrowania
- **Analizy lokalizacyjne**

**Przykładowy format CSV:**
```csv
MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,Latitude,Longitude,AltitudeMeters
A1:B2:C3:D4:E5:F6,HomeNetwork,WPA2,2026-05-28 10:30:15,6,-45,40.7128,-74.0060,10
```

{{< figure src="dagshell-wardriving-gps-wifi-network-mapping-wigle-csv-export.webp" alt="Tryb wardrivingu DagShell pokazuje współrzędne GPS i skanowane sieci Wi-Fi wraz z SSID, BSSID, typem szyfrowania i siłą sygnału zapisanymi do pliku CSV zgodnego z Wigle." >}}

### 🥧 Dodatek Raspberry Pi

**Dodatek Raspberry Pi** rozszerza możliwości DagShell o **zewnętrzny sprzęt**:

#### Wymagania sprzętowe
**Minimum:**
- **Raspberry Pi 3B+** lub nowszy *(Pi Zero nie zapewnia portom USB zasilania dla urządzeń peryferyjnych)*
- **Odbiornik GPS USB**, zalecany układ U-Blox 7
- **Zasilacz**, *Pi wymaga osobnego zasilania. Port USB Orbic nie dostarcza go wystarczająco dużo*

**Opcjonalnie:**
- **Adapter Wi-Fi**, drugi interfejs pozwala skanować sieci i utrzymać połączenie
- **Adapter Bluetooth**, jeśli wewnętrzny moduł BT w Pi ma słaby zasięg

#### Moduł GPS (U-Blox 7)

**Połączenie:** odbiornik GPS USB podłączony do Pi\
**Protokół:** zdania NMEA przesyłane przez port szeregowy\
**Konwersja:** Pi automatycznie przelicza ECEF na szerokość i długość geograficzną\
**Udostępnianie danych:** zapisuje współrzędne GPS do **współdzielonego pliku** na Orbic

**Parsowanie zdania NMEA:**
```
$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
       |       |          |           |  |  |   |
       Time    Latitude   Longitude   Fix Sats  Altitude
```

#### Skanowanie Bluetooth (BLE)

**Cel:** wykrywanie pobliskich urządzeń Bluetooth

**Zasada działania:**
- Wyszukuje **rozgłoszenia BLE**
- Przechwytuje **adresy MAC**
- **Wyszukiwanie OUI** pomaga ustalić producenta
- Zapisuje wyniki w **formacie CSV**

**Zdalne sterowanie:**
- Rozpoczynaj i zatrzymuj skanowanie w interfejsie WWW DagShell
- Nie trzeba łączyć się z Pi przez SSH
- Status aktualizuje się na bieżąco

**Zastosowania:**
- **Śledzenie i zliczanie urządzeń**
- **Analiza ruchu pieszego**
- **Wykrywanie urządzeń Bluetooth**
- **Badania bezpieczeństwa IoT**

**Dane wyjściowe CSV:**
```csv
Timestamp,MAC,RSSI,Name,Manufacturer
2026-05-28 10:30:15,AA:BB:CC:DD:EE:FF,-65,Fitbit Charge,Fitbit Inc.
```

#### Skanowanie Wi-Fi

**Cel:** skanowanie sieci Wi-Fi przez Pi i przesyłanie wyników do Orbic

**Zaleta:** osobny interfejs skanuje sieci, podczas gdy **Orbic utrzymuje hotspot**

**Zasada działania:**
- Pi korzysta z **drugiego adaptera Wi-Fi** albo wbudowanego modułu Wi-Fi, jeśli nie jest potrzebny do łączności
- Skanuje **wszystkie kanały**: 1–14 w paśmie 2,4 GHz oraz, jeśli sprzęt obsługuje, 36–165 w paśmie 5 GHz
- Wysyła wyniki do Orbic przez współdzielony magazyn danych
- DagShell zapisuje je w **pliku CSV wardrivingu**

**Koordynacja:**
- Pi i Orbic **synchronizują znaczniki czasu GPS**
- Zapobiega to powielonym wpisom
- Łączy **wyniki obu skanerów** w jednym dzienniku

#### Ataki deautoryzacji

**Cel:** odłączanie klientów od sieci Wi-Fi w testach laboratoryjnych

**Zasada działania:**
- Wysyła **ramki deautoryzacji 802.11**
- Podszywa się pod **adres MAC punktu dostępu**
- Klient otrzymuje od punktu dostępu komunikat o rozłączeniu
- Klient **traci połączenie** i próbuje połączyć się ponownie

**Metody sterowania:**
- **Jednorazowa deautoryzacja:** pojedyncza seria ramek
- **Ciągła deautoryzacja:** blokuje ponowne połączenie i powoduje DoS
- **Zdalne sterowanie:** uruchamiane ze strony skanowania DagShell

**Zastosowania** (za zgodą):
- **Usuwanie nieautoryzowanych urządzeń** z własnej sieci
- **Testy penetracyjne** za zgodą właściciela
- **Ataki Evil Twin** w laboratorium, by skierować klientów do fałszywego punktu dostępu

**⚠️ Ostrzeżenie prawne:** Ataki deautoryzacji są **nielegalne w sieciach, których nie posiadasz**. Mogą skutkować naruszeniem przepisów FCC i zarzutami na podstawie CFAA.

#### Usługa automatycznego uruchamiania

**Usługa systemd:** dodatek Pi uruchamia się automatycznie wraz z systemem

**Plik usługi** (`/etc/systemd/system/pi-companion.service`):
```ini
[Unit]
Description=DagShell Pi Companion
After=network.target

[Service]
ExecStart=/usr/bin/python3 /opt/dagshell/pi_companion.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

**Polecenia:**
```bash
# Enable auto-start
sudo systemctl enable pi-companion

# Start service
sudo systemctl start pi-companion

# Check status
sudo systemctl status pi-companion
```

#### Baza danych OUI

**Cel:** ustalenie producenta na podstawie adresu MAC

**Baza danych:** API oparte na prefiksach [OUI Master Database](https://standards.ieee.org/products-programs/regauth/)

**Zasada działania:**
- Pobiera **pierwsze 3 bajty** adresu MAC, czyli prefiks OUI
- Wysyła zapytanie do API: `api.example.com/oui/A4:83:E7`
- Zwraca **nazwę producenta**

**Przykład:**
```
MAC: A4:83:E7:12:34:56
OUI: A4:83:E7
Vendor: Apple, Inc.
```

**Integracja:** używają jej skaner ARP, skaner BLE i skaner Wi-Fi w trybie wardrivingu

### 📁 Eksplorator plików

**Cel:** przeglądanie plików na urządzeniu i zarządzanie nimi

**Lokalizacja:** katalog `/data/`, zapisywalna partycja

**Możliwości:**
- **Przeglądanie plików** i podkatalogów
- **Pobieranie** plików na komputer
- **Usuwanie** plików po potwierdzeniu
- **Wyświetlanie rozmiarów** i znaczników czasu

**Typowe pliki:**
- `wardrive_log.csv`: dane skanowania Wi-Fi
- `bluetooth_scan.csv`: dane urządzeń BLE
- `gps_track.gpx`: ślady GPS
- `dns_queries.log`: przechwycone zapytania DNS
- `arp_scan.txt`: lista urządzeń sieciowych

**Przesyłanie do Wigle:**
- **Bezpośrednie przesyłanie z przeglądarki** ze strony Pliki
- Logowanie na konto WiGLE
- Wysyłanie pliku CSV bez wcześniejszego pobierania go na komputer

______

{{< stscollective-ad "rayhunter" >}}
+
## Przewodnik instalacji

### Wymagania wstępne

**Sprzęt:**
- **Mobilny hotspot Orbic RCL400**
- **Komputer** z systemem Windows, macOS lub Linux
- **Przewód USB**, jeśli oprogramowanie układowe będzie wgrywane bezpośrednio

**Oprogramowanie:**
- **Python 3** z modułami `requests` i `cryptography`
- **Przeglądarka internetowa**, Chrome, Firefox, Edge lub Safari

**Opcjonalnie:**
- **Raspberry Pi 3B+** lub nowszy do GPS i funkcji dodatkowych
- **Odbiornik GPS USB** z układem U-Blox 7

### Metoda 1: webflasher (zalecana)

**Najprostsza metoda**, nie wymaga wiersza poleceń.

**Krok 1:** Otwórz webflasher DagShell.
- Adres: [dagnazty.github.io/DagShell/orbic.html](https://dagnazty.github.io/DagShell/orbic.html)

**Krok 2:** Wygeneruj certyfikaty PKI.
- Kliknij przycisk **„Generate Certificates”**.
- Przeglądarka wygeneruje **dwupoziomową infrastrukturę PKI**: główny urząd certyfikacji i certyfikat serwera.
- **Pobierz pliki:** `root.der` i `server.der`.

**Krok 3:** Włącz powłokę root w Orbic.
- Połącz się z siecią Wi-Fi Orbic.
- Wpisz **hasło administratora** w formularzu WWW.
- Kliknij **„Enable Shell”**.
- Strona wykorzysta API Orbic, by otworzyć **powłokę root na porcie 24**.

**Krok 4:** Wgraj oprogramowanie układowe.
- Kliknij przycisk **„Deploy DagShell”**.
- Skrypt prześle:
  - `orbic_app`, główny plik binarny oprogramowania
  - `root.der`, certyfikat główny
  - `server.der`, certyfikat serwera TLS
  - `dagshell_boot.sh`, skrypt zapewniający trwałość uruchamiania
- Instalacja trwa **2–3 minuty**.

**Krok 5:** Uruchom ponownie Orbic.
- Wyłącz i włącz urządzenie.
- DagShell uruchomi się automatycznie.

**Krok 6:** Otwórz DagShell.
- Wpisz w przeglądarce adres `https://192.168.1.1:8443/`.
- Zaakceptuj **ostrzeżenie o zabezpieczeniach**. Certyfikat jest samopodpisany, to oczekiwane.
- Jeśli pojawi się monit, zaloguj się domyślnymi danymi.

### Metoda 2: instalacja ręczna

**Dla zaawansowanych użytkowników**, którzy chcą zbudować oprogramowanie ze źródeł.

#### Krok 1: instalacja zależności

**Windows:**
```powershell
# Install Python 3
# Download from python.org

# Install required modules
pip install requests cryptography

# ARM cross-compiler included in gcc_win/ folder
```

**macOS:**
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3
brew install python3

# Install required modules
pip3 install requests cryptography

# ARM toolchain included in gcc_mac/ folder
```

**Linux:**
```bash
# Install Python 3 and pip
sudo apt-get update
sudo apt-get install python3 python3-pip

# Install required modules
pip3 install requests cryptography

# Install ARM cross-compiler
sudo apt-get install gcc-arm-linux-gnueabihf
```

#### Krok 2: sklonowanie repozytorium

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell
```

#### Krok 3: zbudowanie oprogramowania układowego

**Windows:**
```powershell
cd orbic_fw_c
python gen_pki.py          # Generate certificates
.\build.ps1                # Compile firmware
```

**macOS/Linux:**
```bash
cd orbic_fw_c
python3 gen_pki.py         # Generate certificates
./build.sh                 # Compile firmware (auto-builds BearSSL)
```

**Wynik:** `orbic_app`, statyczny plik binarny ARM, oraz pliki certyfikatów DER.

**⚠️ Uwaga dla macOS:** Katalog `gcc_mac/` zawiera niestandardowy zestaw narzędzi ARM zbudowany za pomocą **crosstool-ng**. Korzysta on z nagłówków jądra **Linux 3.2**, by zachować zgodność z jądrem 3.18 w Orbic. *Standardowe kompilatory ARM z Homebrew obsługują nowsze jądra i **nie zadziałają**.*

#### Krok 4: włączenie powłoki root w Orbic

```bash
# Connect to Orbic WiFi
# Replace YOUR_ADMIN_PASSWORD with actual password

python enable_shell.py YOUR_ADMIN_PASSWORD
```

Skrypt wykorzystuje API WWW Orbic, by otworzyć powłokę root na **porcie 24**.

#### Krok 5: wdrożenie oprogramowania

```bash
python deploy_base64.py
```

Skrypt przesyła i instaluje:
- `orbic_app` do `/data/orbic_app`
- Certyfikaty do `/data/root.der` i `/data/server.der`
- Skrypt startowy do `/etc/rc.d/dagshell_boot.sh`

**Trwałość:** oprogramowanie uruchamia się automatycznie po restarcie przez skrypt init.

#### Krok 6: ponowne uruchomienie i dostęp

```bash
# Reboot Orbic (power cycle or via SSH)
reboot

# After reboot, access DagShell
# Browser: https://192.168.1.1:8443/
```

### Ostrzeżenie o certyfikacie bezpieczeństwa

Podczas otwierania DagShell zobaczysz ostrzeżenie **„Not Secure”** lub **„Not Trusted”**.

**Przeglądarki na komputerze:**
- Kliknij **„Advanced”**
- Kliknij **„Proceed to 192.168.1.1 (unsafe)”**

**Przeglądarki mobilne:**
- Kliknij **„Show Details”**
- Kliknij **„visit this website”**

**Przyczyna:**
- Certyfikat jest **samopodpisany**, nie pochodzi od zaufanego urzędu, takiego jak Let's Encrypt
- Urządzenie nie ma certyfikatu głównego w magazynie zaufanych certyfikatów
- *To **oczekiwane zachowanie** niestandardowego oprogramowania układowego, a nie oznaka włamania*

**Czy połączenie jest bezpieczne?**
- **Tak.** Połączenie jest szyfrowane przez **TLS 1.2+**.
- Nie da się przechwycić przesyłanych danych.
- *Certyfikat nie tworzy łańcucha zaufania do publicznego urzędu, ale szyfrowanie działa.*

**Opcjonalnie:** Zainstaluj `root.der` w magazynie zaufanych certyfikatów urządzenia, by usunąć ostrzeżenie.

______

## Konfiguracja dodatku Raspberry Pi
+**Opcjonalne, ale zdecydowanie zalecane**, by uzyskać pełną funkcjonalność.

### Konfiguracja sprzętu

**Krok 1:** Zdobądź podzespoły.
- **Raspberry Pi 3B+** lub nowszy (35–55 USD)
- **Odbiornik GPS USB** z układem U-Blox 7 (15–30 USD)
- **Karta microSD** o pojemności co najmniej 16 GB na system Pi (10 USD)
- **Zasilacz** do Pi (10 USD)

**Krok 2:** Zainstaluj Raspberry Pi OS.
```bash
# Download Raspberry Pi Imager
# https://www.raspberrypi.org/software/

# Flash "Raspberry Pi OS Lite" to SD card
# Boot Pi and complete setup
```

**Krok 3:** Podłącz odbiornik GPS.
- Podłącz odbiornik GPS USB do Pi
- Sprawdź wykrycie urządzenia: `lsusb`, na liście powinno pojawić się urządzenie GPS
- Sprawdź port szeregowy: `ls /dev/ttyUSB*` lub `/dev/ttyACM*`

### Instalacja oprogramowania

**Krok 1:** Sklonuj repozytorium DagShell na Pi.

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell/pi_companion
```

**Krok 2:** Zainstaluj zależności.

```bash
# Update package list
sudo apt-get update

# Install required packages
sudo apt-get install python3-serial python3-requests gpsd gpsd-clients

# Install Python modules
pip3 install pyserial gps3 bluetooth pybluez
```

**Krok 3:** Skonfiguruj demona GPS.

```bash
# Edit gpsd config
sudo nano /etc/default/gpsd

# Set DEVICES line to your GPS serial port
DEVICES="/dev/ttyUSB0"  # Adjust if different

# Restart gpsd
sudo systemctl restart gpsd

# Test GPS
cgps -s  # Should show satellite data after ~30 seconds
```

**Krok 4:** Skonfiguruj dodatek Pi.

```bash
# Edit configuration file
nano pi_companion/config.py

# Set Orbic IP address
ORBIC_IP = "192.168.1.1"
ORBIC_PORT = "8443"

# Set GPS serial port
GPS_DEVICE = "/dev/ttyUSB0"

# Save and exit
```

**Krok 5:** Zainstaluj usługę systemd.

```bash
# Copy service file
sudo cp pi_companion.service /etc/systemd/system/

# Reload systemd
sudo systemctl daemon-reload

# Enable auto-start
sudo systemctl enable pi-companion

# Start service
sudo systemctl start pi-companion

# Check status
sudo systemctl status pi-companion
```

**Krok 6:** Sprawdź komunikację.

```bash
# Check logs
journalctl -u pi-companion -f

# Should see GPS coordinates being sent to Orbic
```

### Konfiguracja sieci

**Opcja A:** połączenie Wi-Fi

```bash
# Pi connects to Orbic hotspot
# Edit wpa_supplicant config
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

# Add network
network={
    ssid="Orbic_SSID"
    psk="PASSWORD"
}

# Restart WiFi
sudo systemctl restart networking
```

**Opcja B:** Ethernet przez USB (zalecane)

- Połącz Pi z Orbic **przewodem USB**, od portu USB Pi do portu USB Orbic
- Włącz **tryb gadżetu USB** na Pi
- Pi działa jako **urządzenie USB Ethernet**
- *To połączenie jest bardziej niezawodne niż Wi-Fi podczas ciągłego przesyłania danych*
- Pi uzyskuje dostęp do internetu przez Orbic

**Konfiguracja gadżetu USB:**
```bash
# Edit config.txt
sudo nano /boot/config.txt

# Add at end
dtoverlay=dwc2

# Edit cmdline.txt
sudo nano /boot/cmdline.txt

# Add after rootwait
modules-load=dwc2,g_ether

# Reboot
sudo reboot
```

______
+
## Dlaczego połączyć DagShell z RayHunterem?

{{< figure src="dagshell-rayhunter-complementary-capabilities.webp" alt="Schemat porównuje wardriving Wi-Fi i narzędzia ataków sieciowych DagShell z wykrywaniem anomalii protokołów komórkowych RayHunter. Oba działają na tym samym hotspotcie Orbic RCL400." >}}

### Uzupełniające się możliwości

**DagShell** i **RayHunter** dobrze się **uzupełniają**. Każde z tych narzędzi obejmuje inne aspekty mobilnych badań bezpieczeństwa:

| Funkcja | DagShell | RayHunter |
|---------|----------|-----------|
| **Wykrywanie IMSI catcherów** | Podstawowe monitorowanie wież komórkowych | Zaawansowana analiza wzorców |
| **Śledzenie GPS** | Tak, przez Pi | Tak, przez modem |
| **Wardriving Wi-Fi** | Tak | Nie |
| **Skanowanie Bluetooth** | Tak, przez Pi | Nie |
| **Narzędzia sieciowe** | Tak, sniffer DNS, skaner ARP i portów | Nie |
| **Narzędzia do ataków** | Tak, Evil Twin, portal przechwytujący i deautoryzacja | Nie |
| **Narzędzia ochrony prywatności** | Tak, naprawa TTL, podszywanie się pod MAC i blokowanie reklam | Ograniczone |
| **Baza wież komórkowych** | Podstawowa | Rozbudowana |
| **Analiza AI/ML** | Nie | Tak, wykrywanie anomalii |
| **Analiza protokołów operatora** | Ograniczona | Zaawansowana, SS7/Diameter |

### Zastosowania łączonych funkcji

#### 1. **Pełna ochrona przed IMSI catcherami**

**Scenariusz:** podróż przez obszar o nasilonym nadzorze

**Rola DagShell:**
- **Monitorowanie zmian wież komórkowych** w czasie rzeczywistym
- **Śledzenie lokalizacji GPS** podczas podejrzanych przełączeń
- **Zapisywanie danych wież** do późniejszej analizy

**Rola RayHuntera:**
- **Wykrywanie anomalii** w protokołach komórkowych za pomocą uczenia maszynowego
- **Inspekcja pakietów SS7/Diameter** w celu wykrywania zaawansowanych ataków
- **Porównanie z bazą znanych, zaufanych wież**

**Efekt połączenia:** DagShell zapewnia **ciągłe monitorowanie**, a RayHunter **szczegółową analizę**.

#### 2. **Wardriving z ochroną**

**Scenariusz:** mapowanie sieci Wi-Fi w mieście

**Rola DagShell:**
- **Skanowanie Wi-Fi** ze współrzędnymi GPS
- Narzędzia **analizy sieci**, siły sygnału i szyfrowania
- **Eksport CSV do Wigle** na potrzeby mapowania

**Rola RayHuntera:**
- **Śledzenie wież komórkowych** podczas wardrivingu
- **Wykrywanie IMSI catcherów** podczas skanowania Wi-Fi
- **Ostrzeganie o naruszeniu bezpieczeństwa komórkowego**

**Efekt połączenia:** wardriving ze świadomością **stanu bezpieczeństwa łączności komórkowej**.

#### 3. **Laboratorium badań bezpieczeństwa**

**Scenariusz:** ćwiczenia red team lub testy penetracyjne

**Rola DagShell:**
- **Evil Twin AP** do testowania zabezpieczeń Wi-Fi
- **Portal przechwytujący** do demonstracji inżynierii społecznej
- **Ataki deautoryzacji** do testowania odporności
- Narzędzia **rozpoznania sieci**

**Rola RayHuntera:**
- **Wykrywanie nadzoru** podczas testów
- Świadomość **bezpieczeństwa wież komórkowych**
- **Ograniczenie ryzyka inwigilacji** podczas testów

**Efekt połączenia:** narzędzia ofensywne ze **świadomością obronną**.

#### 4. **Podróże z naciskiem na prywatność**

**Scenariusz:** dziennikarz lub aktywista w wrażliwym otoczeniu

**Rola DagShell:**
- **Maskowanie TTL** w celu ukrycia tetheringu
- **Podszywanie się pod adres MAC** dla anonimowości
- **Blokowanie reklam** i zapobieganie śledzeniu
- **Monitorowanie IMSI catcherów**

**Rola RayHuntera:**
- **Zaawansowane wykrywanie IMSI catcherów**
- Wykrywanie ataków **na poziomie protokołu**
- **Alerty o bezpieczeństwie komórkowym**

**Efekt połączenia:** większa prywatność dzięki **wielowarstwowej ochronie**.

### Wspólna instalacja

**Urządzenie z wgranym oprogramowaniem** (najprostsza opcja):
- Kup w **STS Collective**: [Orbic RCL400 z RayHunterem i DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
- **Gotowe do użycia** po wyjęciu z pudełka
- Obie wersje oprogramowania **zostały przetestowane i sprawdzone**
- **Bez kłopotów z instalacją**

**Instalacja samodzielna:**
1. Najpierw **wgraj RayHunter**. Zobacz nasz przewodnik [Jak wgrać RayHunter na urządzenia](/articles/how-to-flash-rayhunter-devices-complete-guide/).
2. Następnie **wgraj DagShell**. Oba programy mogą działać jednocześnie.
3. **RayHunter** korzysta z domyślnych portów.
4. **DagShell** działa na porcie 8443.
5. Otwórz oba programy w osobnych kartach przeglądarki.

**Brak konfliktów:**
- RayHunter korzysta z portów **80/443**
- DagShell korzysta z portu **8443**
- Nie zakłócają swojego działania
- Działają **jednocześnie**

Pomijasz instalację samodzielną? **[Orbic RCL400 z RayHunterem i DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)** ze wstępnie wgranym oprogramowaniem jest gotowy do użycia. Kod czytelnika **SIMEONONSECURITY** zapewnia do 20% zniżki w STS Collective.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Kup Orbic RCL400 z wgranym oprogramowaniem. Oszczędź 20%.
{{< /centerbutton >}}

______

## Przykłady praktycznych zastosowań

### Przykład 1: badacz bezpieczeństwa

**Profil:** tester penetracyjny przeprowadzający ocenę bezpieczeństwa Wi-Fi

**Używane narzędzia DagShell:**
- **Wardriving Wi-Fi** do mapowania sieci klienta
- **Skaner ARP** do wykrywania urządzeń
- **Skaner portów** do identyfikacji usług
- **Evil Twin i portal przechwytujący** do testowania odporności na inżynierię społeczną
- **Eksplorator plików** do pobierania wyników

**Przebieg pracy:**
1. Przejdź wokół obiektu klienta
2. Użyj wardrivingu do mapowania zasięgu Wi-Fi
3. Utwórz fałszywy punkt dostępu naśladujący sieć klienta, za jego zgodą
4. Monitoruj próby połączenia klientów
5. Przygotuj raport z zebranych danych

**Integracja z RayHunterem:** pomaga upewnić się, że badacz nie jest obserwowany podczas testów.

### Przykład 2: obrońca prywatności

**Profil:** dziennikarz podróżujący za granicę

**Używane narzędzia DagShell:**
- **Naprawa TTL** do omijania ograniczeń operatora
- **Podszywanie się pod MAC** dla anonimowości urządzenia
- **Wykrywanie IMSI catcherów** dla świadomości zagrożeń nadzoru
- **Sniffer DNS** do sprawdzania, czy urządzenie nie ujawnia danych
- **Blokowanie reklam** i śledzenia

**Przebieg pracy:**
1. Włącz naprawę TTL przed użyciem urządzenia
2. Wylosuj adres MAC
3. Stale monitoruj wykrywanie IMSI catcherów
4. Włącz blokowanie reklam dla wszystkich podłączonych urządzeń
5. Zapisuj podejrzaną aktywność komórkową

**Integracja z RayHunterem:** zapewnia bardziej zaawansowane wykrywanie IMSI catcherów niż podstawowe monitorowanie.

### Przykład 3: administrator sieci

**Profil:** administrator IT zarządzający wieloma lokalizacjami

**Używane narzędzia DagShell:**
- **Wardriving Wi-Fi** do sprawdzania zasięgu
- **Skaner ARP** do inwentaryzacji urządzeń
- **Skaner portów** do audytów bezpieczeństwa
- **Monitor aktywnych połączeń** do wykrywania nieautoryzowanego ruchu
- **Menedżer zapory** do blokowania adresów IP

**Przebieg pracy:**
1. Sprawdź zasięg Wi-Fi w lokalizacji za pomocą wardrivingu
2. Wykryj wszystkie urządzenia sieciowe skanerem ARP
3. Przeskanuj serwery pod kątem dostępnych usług
4. Zablokuj złośliwe adresy IP w zaporze
5. Wyeksportuj raporty do dokumentacji

**Integracja z RayHunterem:** monitoruje bezpieczeństwo komórkowe w lokalizacjach z urządzeniami mobilnymi.

### Przykład 4: badacz bezpieczeństwa IoT

**Profil:** badacz analizujący bezpieczeństwo urządzeń IoT

**Używane narzędzia DagShell:**
- **Skaner ARP z wyszukiwaniem OUI** do identyfikacji urządzeń IoT
- **Skaner portów** do wykrywania otwartych usług
- **Sniffer DNS** do rejestrowania wzorców ruchu IoT
- **Skaner Bluetooth** przez Pi do wykrywania urządzeń BLE IoT
- **Traceroute** do analizy łączności

**Przebieg pracy:**
1. Umieść Orbic i Pi w środowisku testowym
2. Wykryj urządzenia IoT skanerem ARP
3. Wyszukaj podatne usługi za pomocą skanera portów
4. Wykryj urządzenia IoT Bluetooth skanerem BLE
5. Analizuj komunikację „telefon do domu” za pomocą sniffera DNS
6. Udokumentuj podatności

**Integracja z RayHunterem:** wykrywa łączność komórkową urządzeń IoT i monitoruje anomalie.

{{< figure src="dagshell-rayhunter-combined-mobile-security-research-use-cases.webp" alt="Schemat czterech praktycznych zastosowań DagShell i RayHunter: badacz bezpieczeństwa, obrońca prywatności, administrator sieci i badacz IoT." >}}

______

## Kwestie prawne i etyczne

### Ramy prawne

**Narzędzia takie jak DagShell funkcjonują na granicy prawa.**

**Dozwolone zastosowania:**
✅ **Własne sieci**, testuj własne urządzenia i sieci\
✅ **Testy autoryzowane**, uzyskaj pisemną zgodę przed testowaniem cudzych systemów\
✅ **Cele edukacyjne**, ucz się w odizolowanym laboratorium\
✅ **Ochrona prywatności**, używaj naprawy TTL i podszywania się pod MAC na własnym urządzeniu\
✅ **Badania bezpieczeństwa**, odpowiedzialnie zgłaszaj znalezione podatności\

**Niedozwolone zastosowania:**
❌ **Nieautoryzowany dostęp**, atakowanie cudzych sieci może naruszać CFAA\
❌ **Ataki deautoryzacji** na cudze sieci, naruszenie przepisów FCC i ryzyko zarzutów karnych\
❌ Ataki **Evil Twin** na osoby postronne, oszustwa telekomunikacyjne i kradzież tożsamości\
❌ **Podsłuchiwanie DNS** innych osób bez zgody\
❌ **Omijanie zabezpieczeń** w celu popełnienia oszustwa\

### Przepisy, które warto znać

**Stany Zjednoczone:**
- **Computer Fraud and Abuse Act (CFAA)**, nieautoryzowany dostęp do komputerów i sieci
- **Wiretap Act**, przechwytywanie komunikacji elektronicznej
- **Przepisy FCC**, zakłócanie częstotliwości radiowych, w tym ataki deautoryzacji

**Wielka Brytania:**
- **Computer Misuse Act 1990**, przepisy podobne do CFAA
- **Regulation of Investigatory Powers Act (RIPA)**, ograniczenia przechwytywania komunikacji

**Unia Europejska:**
- **RODO**, ochrona danych, w tym identyfikujących danych z Bluetooth i Wi-Fi
- *Przepisy lokalne różnią się między państwami, podobnie jak ich egzekwowanie.*

### Zasady etyczne

**Rób:**
- ✅ Korzystaj z narzędzi na **własnych urządzeniach i w swoich sieciach**
- ✅ Uzyskaj **pisemną zgodę** przed testowaniem cudzych systemów
- ✅ **Odpowiedzialnie zgłaszaj** znalezione podatności
- ✅ Używaj narzędzi **edukacyjnie** w kontrolowanym środowisku
- ✅ Stosuj **ochronę prywatności** dla siebie

**Nie rób:**
- ❌ Nie atakuj cudzych sieci
- ❌ Nie wyłudzaj danych logowania od obcych osób
- ❌ Nie zakłócaj działania infrastruktury krytycznej
- ❌ Nie używaj narzędzi w złośliwych celach
- ❌ Nie rozpowszechniaj przechwyconych danych

### Oświadczenie o odpowiedzialnym użyciu

DagShell to **narzędzie do badań bezpieczeństwa i ochrony prywatności**. Jego możliwości przypominają profesjonalne narzędzia do testów penetracyjnych, takie jak **Kali Linux**, **WiFi Pineapple** i **HackRF**.

**Liczy się zamiar:** tych samych narzędzi używają **złośliwi hakerzy** i **specjaliści ds. bezpieczeństwa**. Różnice dotyczą:
- **Autoryzacji**, czyli zgody na testy
- **Zamiaru**, poprawy bezpieczeństwa lub wyrządzenia szkód
- **Ujawnienia**, zgłoszenia wyników lub wykorzystania ich w ataku

Używaj DagShell **odpowiedzialnie i etycznie**. *Jeśli nie masz pewności, czy dane działanie jest legalne, przerwij je i przed dalszymi krokami skonsultuj się z prawnikiem.*

{{< figure src="dagshell-legal-ethical-security-research-responsible-use.webp" alt="Ramy prawne i etyczne badań bezpieczeństwa z DagShell, dozwolone i niedozwolone zastosowania oraz przepisy." >}}

______

## Rozwiązywanie problemów
+

### Problemy z instalacją

**Problem:** `enable_shell.py` nie łączy się

**Rozwiązania:**
- Sprawdź, czy urządzenie jest połączone z **Wi-Fi Orbic**
- Upewnij się, że adres IP to **192.168.1.1**, wartość domyślna
- Ponownie wpisz hasło administratora, zwracając uwagę na wielkość liter
- Sprawdź dostępność portu 80: `telnet 192.168.1.1 80`

**Problem:** nie udaje się przesłać oprogramowania

**Rozwiązania:**
- Najpierw włącz powłokę root. Polecenie `enable_shell.py` musi zadziałać.
- Sprawdź stabilność sieci. Jeśli możesz, użyj połączenia przewodowego.
- Zamiast `deploy_base64.py` spróbuj polecenia `deploy_net.py`.
- Sprawdź, czy na partycji `/data` jest wolne miejsce: `df -h /data`

**Problem:** ostrzeżenie o certyfikacie nie znika

**Rozwiązania:**
- *To **normalne** przy certyfikatach samopodpisanych. Połączenie pozostaje szyfrowane.*
- Za każdym razem kliknij „Advanced” i wybierz „Proceed anyway”.
- **Opcjonalnie:** zaawansowani użytkownicy mogą zainstalować `root.der` w magazynie zaufanych certyfikatów.

### Problemy podczas działania

**Problem:** DagShell nie uruchamia się po starcie

**Rozwiązania:**
- Sprawdź skrypt startowy: `ls -la /etc/rc.d/dagshell_boot.sh`
- Sprawdź, czy plik jest wykonywalny: `chmod +x /etc/rc.d/dagshell_boot.sh`
- Sprawdź dzienniki: `logread | grep dagshell`
- Uruchom ręcznie: `/data/orbic_app &`

**Problem:** GPS nie działa

**Rozwiązania:**
- Sprawdź, czy **dodatek Pi** działa: `systemctl status pi-companion`
- Sprawdź, czy GPS odbiera sygnał satelitarny: `cgps -s` na Pi
- Upewnij się, że odbiornik GPS jest podłączony: `lsusb`
- *Przy zimnym starcie GPS może potrzebować 5–10 minut na ustalenie pozycji. Pierwsze ustalenie pozycji zwykle trwa dłużej na zewnątrz.*

**Problem:** wardriving nie zapisuje danych

**Rozwiązania:**
- Przed rozpoczęciem sprawdź, czy GPS ustalił pozycję
- Sprawdź uprawnienia zapisu w katalogu `/data`
- Upewnij się, że powstaje plik CSV: `ls -la /data/wardrive_log.csv`
- Sprawdź, czy interfejs Wi-Fi działa: `ifconfig wlan0`

**Problem:** dodatek Pi nie komunikuje się z Orbic

**Rozwiązania:**
- Sprawdź łączność sieciową: `ping 192.168.1.1`
- Sprawdź, czy plik konfiguracyjny zawiera poprawny adres IP
- Sprawdź, czy port 8443 jest otwarty: `telnet 192.168.1.1 8443`
- Sprawdź dzienniki dodatku Pi: `journalctl -u pi-companion`

### Problemy z wydajnością

**Problem:** interfejs WWW działa wolno lub zacina się

**Rozwiązania:**
- Wyczyść pamięć podręczną przeglądarki
- Wyłącz rozszerzenia przeglądarki. Blokery reklam mogą zakłócać działanie.
- Połącz się z Orbic **przewodowo** zamiast przez Wi-Fi
- Uruchom ponownie DagShell: `killall orbic_app && /data/orbic_app &`

**Problem:** skanowanie wardrivingu trwa zbyt długo

**Rozwiązania:**
- W ustawieniach zwiększ odstęp między skanami. Zmniejszy to częstotliwość na rzecz wydajności.
- Ogranicz liczbę skanowanych kanałów.
- *Słaby sygnał GPS spowalnia skanowanie, ponieważ system czeka na prawidłowe współrzędne przed zapisaniem danych.*

{{< figure src="dagshell-troubleshooting-installation-gps-wardriving-common-issues.webp" alt="Schemat rozwiązywania typowych problemów z instalacją, GPS i wardrivingiem w DagShell. Zawiera kolejne kroki naprawy." >}}

______

## Konfiguracja zaawansowana

### Dostosowywanie DagShell

**Modyfikowanie kodu źródłowego:**
- Edytuj pliki w katalogu `orbic_fw_c/`
- Zbuduj oprogramowanie ponownie przez `build.sh` lub `build.ps1`
- Wgraj oprogramowanie ponownie

**Dodawanie własnych stron:**
- DagShell osadza kod HTML w C++
- Edytuj `main.cpp`, by dodać nowe trasy
- Skompiluj i wgraj oprogramowanie ponownie

**Własny certyfikat:**
- Wygeneruj własną infrastrukturę PKI przez `gen_pki.py`
- Możesz też użyć **OpenSSL** do utworzenia certyfikatów
- Zastąp pliki `root.der` i `server.der`

### Integracja z innymi narzędziami

**Eksport danych do Wireshark:**
```bash
# Capture pcap file
tcpdump -i wlan0 -w /data/capture.pcap

# Download via file browser
# Open in Wireshark on PC
```

**Import śladów GPS do QGIS:**
```bash
# Export GPX format
python gps_to_gpx.py /data/gps_coords.txt

# Import to QGIS as vector layer
```

**Synchronizacja z zewnętrzną bazą danych:**
```python
# Custom script to upload wardrive data to MySQL
import mysql.connector
import csv

conn = mysql.connector.connect(
    host="your_server",
    user="username",
    password="password",
    database="wardriving"
)

with open('/data/wardrive_log.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("INSERT INTO networks (ssid, bssid, lat, lon) VALUES (%s, %s, %s, %s)",
                      (row['SSID'], row['MAC'], row['Latitude'], row['Longitude']))
conn.commit()
```

### Dostosowanie wydajności

**Przyspieszanie skanowania:**
```bash
# Edit wardrive scan interval
# In DagShell web UI, change from 5s to 3s for faster scanning
# Trade-off: Higher CPU usage, potential missed networks
```

**Oszczędzanie baterii** (przy zasilaniu z akumulatora):
```bash
# Reduce screen brightness on Orbic
# Disable unused features (BT, GPS when not needed)
# Use sleep mode between wardrive sessions
```

______

## Porównanie z innymi rozwiązaniami

### DagShell a WiFi Pineapple

| Funkcja | DagShell (Orbic RCL400) | WiFi Pineapple |
|---------|-------------------------|----------------|
| **Cena** | 60–80 USD plus urządzenie | 99–299 USD |
| **Łączność komórkowa** | ✅ Wbudowane 4G LTE | ❌ Brak, tylko Wi-Fi |
| **GPS** | ✅ Przez dodatek Pi | ⚠️ Przez odbiornik USB |
| **Evil Twin** | ✅ Tak | ✅ Tak |
| **Portal przechwytujący** | ✅ Tak | ✅ Tak |
| **Deautoryzacja** | ✅ Tak, przez Pi | ✅ Tak |
| **Wardriving** | ✅ Tak | ✅ Tak |
| **Wykrywanie IMSI** | ✅ Podstawowe | ❌ Nie |
| **Przenośność** | ✅ Wysoka | ⚠️ Umiarkowana |
| **Bateria** | ✅ Wbudowana | ⚠️ Wymaga zewnętrznej |
| **Krzywa uczenia** | Umiarkowana | Niska, dopracowany interfejs |

**Wybór:** DagShell do **mobilnego bezpieczeństwa komórkowego**, Pineapple do testów **sieci Wi-Fi** z prostym interfejsem.

### DagShell a Kali Linux na Pi

| Funkcja | DagShell | Kali na Pi |
|---------|----------|-----------|
| **Czas konfiguracji** | 15 minut | 2–3 godziny |
| **Komórkowe LTE** | ✅ Wbudowane | ❌ Wymaga modemu USB |
| **Interfejs WWW** | ✅ Tak | ⚠️ Ograniczony, wymaga VNC/SSH |
| **Liczba narzędzi** | Około 15 | Ponad 600 |
| **Specjalizacja** | Bezpieczeństwo mobilne | Ogólne testy penetracyjne |
| **Przenośność** | ✅ Kieszonkowe | ⚠️ Wymaga ekranu i zasilania |
| **Czas pracy na baterii** | 8–10 godzin | 2–4 godziny |

**Wybór:** DagShell do zadań **mobilnych**, Kali jako **kompleksowy** zestaw narzędzi.

### DagShell a standardowe oprogramowanie Orbic

| Funkcja | DagShell | Standardowe oprogramowanie |
|---------|----------|----------------------------|
| **Narzędzia bezpieczeństwa** | ✅ Rozbudowane | ❌ Brak |
| **Funkcje ochrony prywatności** | ✅ Tak | ❌ Minimalne |
| **Możliwość dostosowania** | ✅ Pełna | ❌ Zablokowane |
| **Wardriving** | ✅ Tak | ❌ Nie |
| **GPS** | ✅ Tak, przez Pi | ❌ Nie |
| **Open source** | ✅ Tak | ❌ Własnościowe |
| **Pomoc techniczna** | ⚠️ Społeczność | ✅ Oficjalna |
| **Stabilność** | ⚠️ Beta | ✅ Produkcyjna |

**Wybór:** DagShell dla **badaczy**, standardowe oprogramowanie dla **zwykłych użytkowników**.

______

## Podsumowanie: kompletne mobilne laboratorium

**DagShell** zmienia niepozorny **hotspot Orbic RCL400** w **wydajne mobilne laboratorium bezpieczeństwa**. Łączy w sobie:

✅ **Ochronę prywatności**, maskowanie TTL, podszywanie się pod MAC i blokowanie reklam\
✅ **Monitorowanie sieci**, połączenia, DNS i routing\
✅ **Narzędzia hakerskie**, wykrywanie IMSI, skanowanie portów i wykrywanie urządzeń przez ARP\
✅ **Możliwości ataku**, Evil Twin, portal przechwytujący i deautoryzację\
✅ **Wardriving GPS** z integracją Wigle\
✅ **Rozszerzenie Raspberry Pi**, BLE, Wi-Fi i GPS\
✅ **Przenośność i zasilanie bateryjne**\
✅ **Otwarte źródła i możliwość dostosowania**

### Połączenie z RayHunterem

**RayHunter i DagShell** tworzą **kompletną mobilną platformę bezpieczeństwa**:
- **RayHunter** zapewnia zaawansowane wykrywanie IMSI catcherów
- **DagShell** dostarcza narzędzia ofensywne i ochrony prywatności
- Oba programy działają **jednocześnie** na jednym urządzeniu
- Ich możliwości **uzupełniają się i nie nakładają**
- Jeden **przenośny zestaw** obsługuje wszystkie mobilne zadania bezpieczeństwa

### Zacznij już dziś

**Opcja 1: urządzenie z wgranym oprogramowaniem** (najprostsza)
- **STS Collective**: [Orbic RCL400 z RayHunterem i DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
- Urządzenie jest **gotowe do użycia**
- Bez problemów z instalacją
- Profesjonalnie skonfigurowane

**Opcja 2: instalacja samodzielna**
- Postępuj zgodnie z tym przewodnikiem
- Instalacja jest **bezpłatna**, jeśli masz Orbic RCL400
- Poznaj proces instalacji
- Dostosuj oprogramowanie do swoich potrzeb

### Powiązane artykuły

- **[Jak wgrać RayHunter na urządzenia: kompletny przewodnik](/articles/how-to-flash-rayhunter-devices-complete-guide/)**, najpierw zainstaluj RayHunter
- **[Porównanie urządzeń RayHunter: pełna recenzja](/articles/rayhunter-device-comparison-2026-complete-review/)**, wybierz platformę
- **[Projekt Flock-You: sprzęt do wykrywania inwigilacji](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**, poznaj więcej narzędzi wykrywania

### Ostatnie uwagi

DagShell zapewnia **przenośną, wydajną i niedrogą** platformę mobilnego bezpieczeństwa dla **badaczy bezpieczeństwa**, **testerów penetracyjnych**, **obrońców prywatności** i **administratorów sieci**.

**Zastrzeżenie:** Korzystaj z narzędzi odpowiedzialnie. Testuj tylko sieci i urządzenia, które posiadasz lub do których oceny masz wyraźną pisemną zgodę. Przestrzegaj prawa i zasad etycznych. Powodzenia w testach! 🚀

{{< figure src="dagshell-orbic-rcl400-mobile-security-lab-conclusion-overview.webp" alt="Hotspot Orbic RCL400 z oprogramowaniem DagShell tworzy kompletne, przenośne laboratorium mobilnych badań bezpieczeństwa." >}}

______

## Źródła

1. [Repozytorium DagShell na GitHubie](https://github.com/dagnazty/DagShell)
2. [Dokumentacja DagShell](https://dagnazty.github.io/DagShell/)
3. [STS Collective, urządzenia z wgranym oprogramowaniem](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
4. [WiGLE, projekt mapowania Wi-Fi](https://wigle.net/)
5. [Computer Fraud and Abuse Act (CFAA)](https://www.law.cornell.edu/uscode/text/18/1030)
6. [Oficjalna dokumentacja Raspberry Pi](https://www.raspberrypi.org/documentation/)
7. [Dokumentacja modułu GPS U-Blox](https://www.u-blox.com/)
8. [Baza OUI, standardy IEEE](https://standards.ieee.org/products-programs/regauth/)
9. [Samouczek iptables](https://www.netfilter.org/documentation/)
10. [Dokumentacja OpenSSL](https://www.openssl.org/docs/)
