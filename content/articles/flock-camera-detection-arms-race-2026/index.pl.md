---
title: "Wyścig wykrywania kamer Flock: co zmieniło się w 2026 roku"
date: 2026-09-10
lastmod: 2026-11-13
toc: true
draft: false
description: "Poznaj zgłaszane zmiany w wykrywaniu kamer Flock Safety, reakcje społeczności i metody podczerwieni do rozpoznawania systemów kamer."
genre: ["Technologie ochrony prywatności", "Kontrnadzór", "Projekty open source", "Prawa cyfrowe", "Bezpieczeństwo sieci", "Badania bezpieczeństwa", "Modyfikowanie sprzętu", "Narzędzia prywatności"]
tags: ["Flock Safety", "ALPR", "Flock-You", "Wykrywanie OUI", "Żądanie probe z wildcard", "Tryb promiskuitywny WiFi", "Monitorowanie 802.11", "DeFlockJoplin", "NitekryDPaul", "Wykrywanie BLE", "WiFi 5GHz", "Lokalnie administrowany MAC", "Dopasowywanie wzorców SSID", "Sprzęt do kontrnadzoru", "STS Collective", "colonelpanichacks", "Unikanie wykrywania", "ESP32", "Wykrywanie WiFi", "Świadomość nadzoru", "OUI-SPY", "M5 Atom Lite", "Flock Finder", "Śledzenie zgłoszeń GitHub", "Aktualizacja firmware", "Ochrona przed identyfikacją na podstawie cyfrowego odcisku urządzenia", "Losowanie MAC", "Fingerprinting elementów informacji", "Przeskakiwanie kanałów", "Ochrona prywatności", "Bezpieczeństwo open source", "Nadzór masowy", "Firmware wykrywające", "Badanie WiFi podczas jazdy", "Demontaż kamer", "Sprzęt chroniący prywatność", "Wykrywanie podczerwieni", "Oświetlacz IR", "ESP32-CAM", "Seeed Studio XIAO ESP32S3 Sense", "Quectel L76K", "Wykrywanie optyczne", "Valleytech Custom Solutions"]
cover: "/img/cover/flock-camera-detection-techniques-2026.webp"
coverAlt: "Miejska scena z kamerą Flock na latarni i pojazdem z zaawansowanym urządzeniem wykrywającym. Świecące sygnały pokazują bezprzewodową transmisję danych na ciemnym tle."
coverCaption: "Jak zmieniany sprzęt Flock Safety wciąż psuje narzędzia wykrywania open source, a społeczność nadrabia zaległości"
canonical: "https://simeononsecurity.com/articles/flock-camera-detection-arms-race-2026/"
---

**Jeśli twój detektor Flock-You zamilkł na trasie, na której wcześniej zawsze znajdował kamery, nie wyobrażasz sobie tego, a sprzęt prawdopodobnie nie jest uszkodzony.** W ciągu ostatniego roku sprzęt i firmware kamer Flock Safety zmieniono co najmniej dwa razy, przez co przestały działać metody wykrywania społeczności. Badacze open source musieli za każdym razem odtworzyć nową sygnaturę.

*To szybko zmieniająca się sytuacja. Metoda wykrywania i lista OUI poniżej pochodzą z gałęzi `colonelpanichacks/flock-you` `main` z września 2026 roku. Sprawdź [repozytorium GitHub](https://github.com/colonelpanichacks/flock-you), zanim uznasz urządzenie za wadliwe.*

{{< youtube id="cVf-id71BuQ" >}}

*Powyższy film Valleytech Custom Solutions pokazuje dokładnie opisywany objaw: zwykły przejazd wardrivingowy nagle nie wykrywa niczego na kilku wersjach firmware, na trasie, na której wcześniej niezawodnie znajdowano kamery, w hrabstwie, gdzie niektóre wcześniej oznaczone urządzenia fizycznie zniknęły.*

______

## Przejazd wardrivingowy, który nagle niczego nie wykrył

Zgłoszenia zwykle opisują ten sam schemat. Kierowca pokonuje trasę, którą przejechał już dziesiątki razy. Detektor działa na aktualnym firmware i wcześniej wykrywał te same kamery. Podczas jednego przejazdu nie rejestruje niczego: ani sygnału dźwiękowego, ani wpisu w logu, na każdej testowanej wersji niestandardowego firmware.

Film Valleytech opisuje taki przypadek: codzienna droga do poczty zawsze rejestrowała co najmniej jedną kamerę Flock, a teraz nie rejestruje żadnej. Druga trasa obok Micro Center wcześniej oznaczała pięć kamer. Teraz tylko jedna jest aktywna, a pozostałe cztery fizycznie usunięto ze słupów.

**W tym samym czasie działy się dwie rzeczy, które łatwo pomylić:**

- **Kamery są fizycznie usuwane lub przenoszone** w niektórych miejscach, więc jest tam mniej urządzeń do wykrycia.
- **Zmieniła się sygnatura bezprzewodowa kamer**, więc urządzenie nadal stojące na słupie może nie uruchomić detektora ze starym firmware.

Dwa zgłoszenia GitHub w repozytorium `colonelpanichacks/flock-you`, opublikowane w odstępie kilku miesięcy, szczegółowo opisują drugi problem. Razem pokazują, jak społeczność już dwukrotnie musiała zmienić metodę wykrywania.

______

## Zgłoszenie #20: zniknął punkt dostępowy do zarządzania

**[Zgłoszenie #20](https://github.com/colonelpanichacks/flock-you/issues/20)** otwarto w styczniu 2026 roku. Użytkownik sprawdził urządzenie obok znanej kamery Flock oznaczonej w DeFlock, ale nie wykrył niczego. W kolejnych tygodniach podobne wyniki zgłaszali użytkownicy z Florydy, Indiany, Atlanty i Środkowego Zachodu, korzystający z różnego sprzętu i anten.

Jeden z komentujących zadał najważniejsze pytanie: **czy Flock zmienił coś po swojej stronie, co mniej więcej w tym samym czasie przerwało wykrywanie wszystkim?**

Opiekun projektu colonelpanichacks potwierdził to. **Około grudnia 2025 roku Flock wyłączył punkt dostępowy do zarządzania, który nadawały kamery.** Był on pierwotną podstawą wykrywania bezprzewodowego. Po jego zniknięciu społeczność przeszła na sygnały Bluetooth Low Energy (BLE). Do wiosny 2026 roku ta metoda również stała się zawodna.

| Sygnał wykrywania | Stan |
|---|---|
| **Punkt dostępowy WiFi do zarządzania** | Wyłączony przez Flock około grudnia 2025 roku |
| **Nadajniki BLE** | Przestały działać niezawodnie wiosną 2026 roku |
| **Komórkowe łącze LTE** | Nadal używane do wysyłania danych do chmury, ale nie da się go pasywnie wykryć |
| **Żądania probe 802.11 z wildcard** | Obecna podstawa wykrywania, patrz niżej |

*Każdy niestandardowy firmware oparty na starym punkcie dostępowym lub BLE szuka teraz sygnału, którego kamery już nie wysyłają. Dlatego działające wcześniej urządzenie może zamilknąć, mimo że sprzęt jest sprawny.*

______

## Nowa metoda: wildcard probe i fingerprinting ramek

Obecny firmware `flock-you` działa w dedykowanym trybie promiskuitywnym 802.11. Radio niczego nie nadaje i nie dołącza do sieci. Tylko nasłuchuje, przełączając kanały WiFi 11, 6 i 1 co 250 milisekund, aby nadążyć za zmianami kanałów kamer.

**Detekcja następuje dopiero wtedy, gdy jednocześnie spełnione są wszystkie warunki:**

1. Ramka to 802.11 **Management Probe Request** (typ 0, podtyp 4).
2. **Element SSID jest obecny i ma długość 0**, co oznacza wildcard probe bez żądania konkretnej sieci.
3. Adres nadawcy (**addr2**) pasuje do znanego prefiksu OUI Flock.
4. Pozostałe Information Elements odpowiadają wzorcowi fingerprintu opisanemu przez społeczność DeFlockJoplin, na podstawie badań Pintora i Atzoriego z 2022 roku o **[fingerprintingu elementów informacji w żądaniach probe WiFi](https://ieeexplore.ieee.org/document/10001618)**.

Firmware nazywa tę metodę `wifi_wildcard_probe_ie_sig`. W testach terenowych społeczność DeFlockJoplin wykryła **11 z 12 znanych kamer przy zaledwie 2 fałszywych alarmach**. To ta sama zweryfikowana terenowo wartość bazowa, którą opisuje **[przewodnik sprzętowy](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**. OUI dwunastej kamery dodano później do poniższej listy.

{{< figure src="flock-detection-arms-race-timeline-2026.webp" alt="Oś czasu metod wykrywania kamer Flock: od punktu dostępowego WiFi przez nadajniki Bluetooth Low Energy po wildcard probe i fingerprinting elementów informacji, a następnie nowe SSID, 5GHz i unikanie fingerprintingu MAC" >}}

______

## Aktualna lista OUI

Fingerprint wildcard probe działa tylko wtedy, gdy adres MAC nadajnika pasuje do prefiksu OUI potwierdzonego na prawdziwym sprzęcie Flock. Listę prowadzi głównie badacz **@NitekryDPaul**. Społeczność **DeFlockJoplin** dodała 31. prefiks po wykryciu kamery, której nie obejmowała wcześniejsza lista 30 pozycji.

```text
70:c9:4e  3c:91:80  d8:f3:bc  80:30:49  b8:35:32
14:5a:fc  74:4c:a1  08:3a:88  9c:2f:9d  c0:35:32
94:08:53  e4:aa:ea  f4:6a:dd  f8:a2:d6  24:b2:b9
00:f4:8d  d0:39:57  e8:d0:fc  e0:4f:43  b8:1e:a4
70:08:94  58:8e:81  ec:1b:bd  3c:71:bf  58:00:e3
90:35:ea  5c:93:a2  64:6e:69  48:27:ea  a4:cf:12
82:6b:f2
```

**Lista nie jest stała.** W notatkach badawczych opisano prefiksy przetestowane, a potem obniżone w rankingu. Jeden należał do odtwarzacza multimedialnego Sony, inny był wczesną wartością zastępczą, która nigdy do niczego nie pasowała. Dwie pozycje mają niską pewność. Prefiks `82:6b:f2` pozostaje mimo lokalnego zarządzania, ponieważ usunięcie go wyeliminowałoby prawdziwe wykrycie potwierdzone przez DeFlockJoplin.

**Jeden prefiks ma niezależne potwierdzenie ze sprzętu pracującego w terenie.** Obrazy systemu plików kamery Flock opublikowane we wrześniu 2026 roku zawierały MAC **`f4:6a:dd:57:46:fb`**. Prefiks `f4:6a:dd` jest na tej liście pozycją 13. Nie pochodził z laboratorium ani kupionej próbki. Należał do kamery na słupie w Wauwatosa w stanie Wisconsin, fotografującej ruch uliczny. To najmocniejsze dotąd potwierdzenie jednego prefiksu.

*Jeśli utrzymujesz własny fork firmware, pobieraj listę OUI z katalogu upstream `datasets/` zamiast wpisywać kopię na stałe. Lista zmienia się wraz z badaniami, a nieaktualna kopia po cichu zacznie pomijać kamery.*

______

## Ranking sygnałów wykrywania

Dopasowanie OUI jest metodą używaną przez bieżący firmware, ale najsłabszą z pięciu dostępnych sygnałów. Społeczność **[WiFi Mothership](https://wifimothership.com/flock)** szereguje je według pewności, korzystając z badań firmware GainSec.

| Pewność | Sygnał | Uwagi |
|---|---|---|
| **WYSOKA** | **Identyfikator producenta BLE `0x09C8`** (XUNTONG) | Najsilniejszy fingerprint cyfrowy. Występuje w urządzeniach Raven oraz Falcon i Sparrow z podłączonym modułem baterii |
| **WYSOKA** | **UUID usług BLE Raven `0x3100`–`0x3500`** | Usługi GATT Raven dotyczące GPS, zasilania, sieci, wysyłania danych i błędów. Działa tylko ze sprzętem Raven |
| **ŚREDNIA** | **Wzorzec SSID WiFi `^Flock-[A-Z0-9]+$`** | Domyślna nazwa hotspotu konfiguracji. Inne SSID w firmware to `FS Ext Battery`, `Penguin` i `Pigvision` |
| **ŚREDNIA** | **Fragment nazwy urządzenia BLE** | Nazwy takie jak `FS Ext Battery` są w ładunkach reklamowych i nie wymagają analizy danych producenta |
| **NISKA** | **Dopasowanie adresu MAC i prefiksu OUI** | **Najbardziej zaszumiona metoda.** Prefiksy dostawców komponentów występują w tysiącach niezwiązanych produktów |

*Dolny wiersz to metoda, od której obecny firmware najbardziej zależy. To główny problem wykrywania opartego na OUI.*

### Dlaczego lista OUI jest tak zaszumiona

31 prefiksów z powyższej listy nie oznacza 31 identyfikatorów Flock. WiFi Mothership śledzi równolegle **26 prefiksów i klasyfikuje każdy z nich według rzeczywistego właściciela**.

| Klasa | Liczba | Właściciel |
|---|---:|---|
| **Flock Safety** | **1** | `B4:1E:52`, przydział IEEE dla samej firmy |
| **Moduły baterii** | 10 | Układy Silicon Labs w pakietach rozszerzonej baterii |
| **Moduły kamer** | 11 | Moduły kamer WiFi firmy Liteon Technology |
| **Infrastruktura obliczeniowa** | 4 | Raspberry Pi Foundation i Raspberry Pi Trading |

**Dwadzieścia pięć z tych 26 prefiksów należy do dostawców komponentów.** Ich części trafiają do ogromnej liczby niezwiązanych urządzeń. Prefiks pakietu baterii Silicon Labs lub modułu kamery Liteon występuje w produktach bez związku z Flock Safety, a płytki Raspberry Pi są powszechne.

**Dopasowanie to wskazówka, nie identyfikacja.** Dlatego fingerprint wildcard probe ma tak duże znaczenie w obecnym firmware. Połączenie OUI z żądaniem probe o pustym SSID zwiększa poziom pewności z przypuszczenia do 62 w skali projektu.

*Tylko `B4:1E:52` samodzielnie odpowiada na pytanie «czy to urządzenie Flock?». Pozostałe 30 prefiksów traktuj jako dowody pomocnicze.*

### Ile kamer ujawnia hotspot

Dane wardrivingowe wyznaczają dolną granicę liczby urządzeń. WiFi Mothership znalazł **co najmniej 900 punktów dostępowych Flock w WiGLE w 2025 roku**. Punkt AP oznacza tu urządzenie nadające domyślny hotspot SSID `Flock-XXXX`.

Liczba opisuje urządzenia udostępniające hotspot konfiguracji, a nie całą zainstalowaną bazę. Flock deklaruje dziesiątki tysięcy wdrożeń. Większość kamer nie nadaje niczego, co przejeżdżający wardriver zarejestruje. **Mapa to próbka i to niewielka.**

______

## Zgłoszenie #43: nowe SSID, 5GHz i antyfingerprinting MAC

Trzy miesiące po zamknięciu zgłoszenia #20 pojawił się kolejny raport. Opisuje możliwy celowy mechanizm utrudniania wykrywania, a nie przypadkową zmianę firmware. **[Zgłoszenie #43](https://github.com/colonelpanichacks/flock-you/issues/43)**, opublikowane w maju 2026 roku, opiera się na danych WiGLE zebranych przy kamerze już potwierdzonej przez DeFlock. Wskazuje trzy rzeczy, których obecne narzędzia nie uwzględniały.

### Ustalenie 1: inny format SSID

Dotąd hotspoty Flock używały wzorca `Flock-XXXXXX`. Kamera z raportu nadawała **`Flock Camera net.`**, czyli nazwę całkiem innego rodzaju. Badacze szukający w WiGLE przez wildcard `Flock-*` otrzymaliby zero wyników dla tej kamery, choć aktywnie nadawała.

### Ustalenie 2: potwierdzony hotspot 5GHz

Ta sama kamera nadawała jednocześnie na **kanale 1 pasma 2,4GHz** i **kanale 157 pasma 5GHz**, z sąsiednimi adresami MAC w każdym paśmie (`...9f:a2:de` i `...9f:a2:df`). Wskazuje to na jeden moduł WiFi dual-band, który przydzielił sąsiednie adresy każdemu radiu, a nie na dwa niezależne urządzenia. Badacz nsm_barii wcześniej zapisał żądanie probe Flock na kanale 149 pasma 5GHz. To już dwa potwierdzenia, że obsługa 5GHz jest realna.

**Każda wcześniej opisana metoda, także obecny firmware wildcard probe, nasłuchuje wyłącznie pasma 2,4GHz.** Kamera nadająca głównie lub wyłącznie na 5GHz pozostaje dla tego sprzętu niewidoczna, nawet przy dokładnej liście OUI.

### Ustalenie 3: lokalnie administrowane MAC hotspotu

W obu zapisanych adresach MAC ustawiony jest **bit administracji lokalnej**. Nie pochodzą więc z prawdziwego bloku OUI Flock zarejestrowanego w IEEE. Standardowa logika wykrywania `flock-you` pomija lokalnie administrowane adresy, bo tak zwykle odfiltrowuje się losowane adresy telefonów i laptopów.

**Ten filtr ogranicza fałszywe alarmy, ale odrzuci też kamerę Flock używającą lokalnie administrowanego MAC na interfejsie hotspotu.** Kolejne końcowe bajty obu przechwyconych adresów wykluczają losowe generowanie i sugerują celowy, uporządkowany przydział adresów.

| Ustalenie | Co nadal działa |
|---|---|
| **Nowy format SSID** (`Flock Camera net.`) | Dopasowywanie SSID, jeśli rozszerzy się wzorzec |
| **Praca w paśmie 5GHz** | Nic w obecnym firmware WiFi, bo skanuje tylko 2,4GHz |
| **Lokalnie administrowany MAC** | Dopasowanie SSID, które nie zależy od adresu MAC |

*Dopasowanie SSID to jedyna metoda w tabeli, która działa niezależnie od pasma i sposobu przydzielenia MAC. To praktyczny argument za szerszym dopasowaniem SSID zamiast samego OUI.*

______

## Czy Flock celowo utrudnia wykrywanie?

Żadne z dwóch zgłoszeń GitHub nie dowodzi intencji. Autor zgłoszenia #43 sam zadał otwarte pytanie: czy zjawisko występuje we wszystkich wdrożeniach Flock, czy tylko w jednej wersji firmware na jednej kamerze?

Spójrz na oba zgłoszenia razem. Jeden sygnał znika, społeczność znajduje zamiennik, a jego martwe pola (skanowanie tylko 2,4GHz, dopasowanie OUI, odrzucanie lokalnie administrowanych MAC) odpowiadają cechom, które wykorzystałyby nowe SSID, radio 5GHz i lokalnie administrowany adres. **To może być zbieg okoliczności związany z niezależną aktualizacją firmware. Może też wynikać z ograniczenia przez dostawcę własnej obecności bezprzewodowej, które celowo lub nie utrudnia zewnętrzne wykrywanie.**

*Nie musisz rozstrzygać, która interpretacja jest prawdziwa. Buduj wykrywanie, które nie zależy od jednego założenia, bo w dwuletniej historii projektu każde takie założenie miało ograniczony okres przydatności.*

### Potwierdzenie wizualne: kamera działa, ale niczego nie nadaje

**[Trzeci krótki film Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0) sprawdza wyjaśnienie, że kamerę być może usunięto.**

{{< youtube id="sjI8FB0cLk0" >}}

Twórca wrócił nocą do tej samej kamery z pierwszego filmu i wizualnie potwierdził, że **diody IR nadal świeciły**, więc urządzenie było zasilane i oświetlało scenę do nocnego rejestrowania. Jednocześnie **każdy testowany firmware zapisał zero prawidłowych trafień**. Jeden alarm był potwierdzonym fałszywym alarmem. Kamera nie wysyłała niczego po stronie bezprzewodowej.

**To rozdziela dwa możliwe wyjaśnienia.** Usunięcie lub przeniesienie kamery nie tłumaczy urządzenia, które wyraźnie działa i świeci w nocy. Aktywna kamera, której nie widzi żadna metoda WiFi, wskazuje na zanik sygnatury bezprzewodowej, a nie brak sprzętu.

Po rozmowach z innymi twórcami badającymi ten problem autor stwierdził, że nie był to odosobniony wynik. **Wiele osób zaobserwowało podobny schemat w podobnym czasie**, co sugeruje skoordynowaną zmianę po stronie Flock w całym kraju, a nie lokalny przypadek jednej kamery. *To anegdota z nieformalnych rozmów, a nie opublikowany zbiór danych. Pasuje jednak do okresów z grudnia 2025 i wiosny 2026 opisanych w zgłoszeniu #20. Taki raport powinien trafić do nowego zgłoszenia GitHub.*

______

## Co to oznacza dla twojego sprzętu wykrywającego

Jeśli urządzenie zamilkło, przejdź przez tę listę przed uznaniem go za uszkodzone:

1. **Najpierw zaktualizuj firmware.** Jeśli używasz wersji starszej niż bieżąca gałąź `main`, prawdopodobnie nadal szukasz wyłączonego punktu AP lub martwych nadajników BLE. Pobierz najnowszy firmware i wgraj go ponownie.
2. **Sprawdź, czy kamera nadal tam jest.** Niektóre raporty o zerowej liczbie wykryć dotyczyły sprzętu rzeczywiście usuniętego lub przeniesionego. Porównaj dane z **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** albo **[DeFlock](https://deflock.org/)**.
3. **Zwolnij na skrzyżowaniach.** Przeskakiwanie kanałów co 250ms może sprawić, że miniesz okno wykrywania, zanim radio trafi na właściwy kanał. Zatrzymanie na 30–60 sekund wykrywa więcej kamer niż szybki przejazd z większą anteną.
4. **Zgłoś wynik.** Zero wykryć przy wizualnie potwierdzonej kamerze to właśnie rodzaj danych, który doprowadził do zgłoszeń #20 i #43. Otwórz nowe zgłoszenie zamiast zakładać, że ktoś już o tym napisał.
5. **Poznaj ograniczenia.** Firmware obsługujący tylko WiFi 2,4GHz nie zobaczy kamery przeniesionej na 5GHz ani urządzenia milczącego na skanowanych pasmach. To obecna luka, a nie błąd twojej kompilacji.

**Sprzęt nadal ma zastosowanie.** Lista OUI i fingerprint wildcard probe wykrywają dziś większość wdrożonych kamer. Traktuj każdy detektor, własny lub kupiony, jako migawkę trwającego wyścigu, a nie rozwiązanie na zawsze.

{{< stscollective-ad "flockyou" >}}

______

## Równoległe podejście: wykrywanie błysku podczerwieni zamiast WiFi

W tym wyścigu działa także inny front niż detekcja bezprzewodowa. **[Osobny film](https://www.youtube.com/shorts/mzpr6bslsYA) Valleytech Custom Solutions opisuje inne podejście**: obserwowanie oświetlacza podczerwieni kamery zamiast nasłuchiwania sygnatury radiowej.

{{< youtube id="mzpr6bslsYA" >}}

Większość kamer ALPR, w tym Flock, używa **podczerwieni do czytelnego rejestrowania tablic nocą**. To samo pozwala zwykłym kamerom bezpieczeństwa działać w ciemności. IR jest niewidoczne dla człowieka, ale widzi je sensor obrazu bez filtra odcinającego podczerwień. *Brak tego filtra w zwykłym module kamery pozwala przekształcić go w detektor Flock.*

### Jak wygląda prototyp

Podejście przeszło kilka iteracji przed uzyskaniem użytecznej konfiguracji:

- **Pierwsza próba**: dedykowane odbiorniki fotodiodowe IR. Działały technicznie, ale były zbyt drogie do praktycznego projektu DIY.
- **Druga próba**: **Jetson Nano z modułem kamery Raspberry Pi**. Potwierdziła koncepcję, ale koszt i pobór mocy nie pasowały do urządzenia ręcznego ani montowanego w pojeździe.
- **Obecna konstrukcja**: **moduł kamery ESP32 bez soczewki z filtrem IR**. Twórca przetestował **ESP32-CAM** i **M5Stack S3 Cam**, a następnie wybrał **Seeed Studio XIAO ESP32S3 Sense** wraz z modułem GNSS Seeed XIAO opartym na układzie **Quectel L76K** do dodawania lokalizacji GPS. To ten sam schemat wardrivingu GPS, którego używa panel Flask projektu WiFi `flock-you`.

| Wymaganie | Dlaczego ma znaczenie |
|---|---|
| **Brak filtra IR w module kamery** | Filtr poprawiający kolory zwykłych zdjęć blokuje światło potrzebne tej metodzie |
| **Kamera zamiast fotodiody** | Fotodiody zdolne odizolować sygnał były zbyt drogie do praktycznej budowy DIY |
| **Rejestrowanie GPS** | Łączy wykrycia z lokalizacją podobnie jak panel Flask firmware WiFi |

### Wzór migania kamery

Założenie wymaga, by oświetlacz migał w powtarzalnym wzorze zamiast świecić stale. Twórca podał **samodzielnie zmierzony czas około 20ms włączone, 80ms wyłączone, okres 100ms, czyli cykl pracy 20% przy 10Hz**. Podkreślił, że wynik nie został potwierdzony i może być błędny. *Traktuj tę liczbę jako punkt wyjścia do własnego pomiaru, a nie potwierdzoną specyfikację. Flock jej nie opublikował, a twórca nie twierdził, że jest pewien.*

### Stan projektu

**To wczesny prototyp DIY, nie gotowy produkt.** Twórca określa oprogramowanie jako „vibe coded” i nadal rozwijane. Planowany brzęczyk do alertów dźwiękowych nie został jeszcze dodany. Nie ma też gotowej płytki podobnej do OUI-SPY. Obecna wersja nadal wymaga **wizualnego potwierdzenia przez człowieka**, czy alarm dotyczy kamery, a nie innego źródła podczerwieni. To narzędzie przesiewowe, nie w pełni zautomatyzowane.

*Ten sygnał detekcji różni się od pozostałych metod. Nie zależy od WiFi, pasma 2,4 lub 5GHz, OUI ani zachowania adresu MAC. Nie dotyczą go więc metody unikania z Issue #43. Ma własne ograniczenia: widoczność optyczną, wpływ światła dziennego i niepotwierdzony niezależnie cykl pracy.*

______

## Co robi społeczność

Reakcje na oba zgłoszenia powtarzały schemat, który przez dwa lata utrzymywał projekt w użyciu: ktoś opisuje lukę, inna osoba wnosi poprawkę, a zmiana trafia do aktualizacji zamiast do zaległości.

- **Zgłoszenie #20** zakończyło się potwierdzeniem przyczyny i przebudową firmware wokół wildcard probe, na podstawie badań terenowych DeFlockJoplin.
- **Zgłoszenie #43** wciąż jest otwarte, a propozycja dopasowywania wzorca SSID czeka na wdrożenie. *Dodanie wzorca `Flock Camera` to niewielki, dobrze określony wkład dla osoby znającej logikę dopasowań firmware.*
- Zbiór OUI ma wersje i daty. Obniżone oraz niepewne pozycje są opisane, a nie usuwane bez śladu.

*To praktyczna przewaga narzędzi open source nad zamkniętym rozwiązaniem. Osoba, która odkryje lukę w detektorze własnościowym, nie może sama go poprawić. Ten projekt poprawiono już dwa razy.*

______

## Druga reakcja: zabranie sprzętu

Wykrywanie bezprzewodowe to jedna reakcja na kamery. Równoległa inicjatywa zajęła się samym sprzętem i we wrześniu 2026 roku dostarczyła najbardziej szczegółowych publicznych danych o działaniu kamery Flock.

**Kolektyw stegan0gram zdjął kamerę ze słupa, skopiował pamięć wewnętrzną i opublikował obrazy systemu plików przez Distributed Denial of Secrets.** Tak opisali swoją pracę:

> "Po co je tylko niszczyć, skoro można je odtworzyć i znaleźć sekrety tych, którzy nas szpiegują? Uwolniliśmy sprzęt z terenu, rozbroiliśmy go, a następnie poddaliśmy inżynierii wstecznej kamery i powiązane urządzenia solarne."

*To ważne rozróżnienie. Zniszczenie kamery usuwa jeden egzemplarz. Inżynieria wsteczna daje dowody dotyczące wszystkich.*

### Co ujawniło usunięcie

Opublikowany zbiór obejmuje **partycję multimedialną 18GB**, **obraz systemu Android 1,5GB** oraz **partycję poświadczeń 32MB**, a także odzyskany klucz zaszyfrowanego kontenera multimediów. Badacze ustalili wersję systemu operacyjnego i jądra, znaleźli zakodowane na stałe poświadczenia backendu oraz tokeny uwierzytelniania zapisane w postaci jawnej.

Te dane wspierają badania opisane w artykule **[Podatności kamer Flock Safety: znaleziono ponad 50 błędów](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)**, które wcześniej opierały się na sprzęcie laboratoryjnym i kupionych urządzeniach.

### Reakcje na usuwanie kamer

Fizyczna ingerencja ma konsekwencje, a sytuacja jest złożona:

- **W całym kraju aresztowano wiele osób** pod zarzutem manipulowania kamerami Flock lub ich niszczenia.
- **Niektóre miasta zapowiedziały rezygnację z kamer Flock**, czego chcą przeciwnicy systemu.
- **Jeden departament policji stworzył fałszywą obudowę kamery Flock wydrukowaną w 3D**, by zwabić i aresztować potencjalnych wandali.

Noel Pichardo, były funkcjonariusz policji w Pawtucket w stanie Rhode Island, został krytykiem Flock po zakwestionowaniu używania kamer przez swój departament. W rozmowie z WIRED przyznał, że rozumie frustrację, ale obawia się, że samosądy utwierdzą policję i państwo w przekonaniu o konieczności tego narzędzia. «Im dłużej państwo ignoruje sprzeciw mieszkańców wobec tego rodzaju nadzoru, tym częściej będzie do tego dochodzić» – powiedział.

### Gdzie w tym wszystkim mieści się detekcja

Demontaż nie zmienia problemu wykrywania opisanego w tym artykule. Kamera nadal nadaje tak jak wcześniej, firmware nadal potrzebuje listy OUI i sygnatury probe, a dwie udokumentowane przerwy w działaniu pozostają aktualne.

Zrzut danych potwierdza **tożsamość sprzętu**, w tym jeden prefiks OUI zweryfikowany na prawdziwym urządzeniu. Pokazuje też, jaka presja wpływa na wdrożenia. **Kamery znikają z trasy, gdy rada miasta kończy umowę, a nie wtedy, gdy detektor milknie.** Narzędzia bezprzewodowe odpowiadają na osobiste pytanie o otoczenie. Spór o politykę odpowiada na większe pytanie, a zrzut dał mu najmocniejsze dotąd dowody.

______

## Podsumowanie: wykrywanie stale się zmienia

Cichy detektor na trasie, na której wcześniej znajdowano kamery, nie dowodzi awarii sprzętu. To dowód, że zmieniła się sygnatura bezprzewodowa, którą urządzenie ma rozpoznawać, a w ciągu jednego roku powtórzyło się to już dwa razy. **Punkt dostępowy do zarządzania, nadajniki BLE, a teraz być może założenia firmware o paśmie 2,4GHz i samym OUI** miały ograniczony okres przydatności.

**Rozwiązaniem nigdy nie było porzucenie wykrywania WiFi.** Trzeba jawnie dokumentować założenia metody i być gotowym na ich poprawę po kolejnym raporcie takim jak zgłoszenie #20 lub #43. To przewaga firmware open source nad zamkniętym rozwiązaniem: poprawka może trafić do projektu, gdy społeczność znajdzie lukę, a nie według harmonogramu dostawcy.

### Najważniejsze wnioski

- **Zniknęły już dwa sygnały wykrywania**: punkt dostępowy WiFi do zarządzania (wyłączony około grudnia 2025 roku) i nadajniki BLE (zawodne od wiosny 2026 roku).
- **Obecna metoda wildcard probe, dopasowania OUI i fingerprintu IE** wykryła w testach terenowych 11 z 12 kamer, ale działa tylko przez WiFi 2,4GHz.
- **Oczekujące zgłoszenie opisuje nowe SSID, potwierdzony hotspot 5GHz i lokalnie administrowane adresy MAC**, których obecna metoda oparta na OUI i 2,4GHz nie wykryje.
- **Pojawia się odrębna metoda bezprzewodowa**: kamera ESP32 bez filtra IR może wykryć oświetlacz podczerwieni i nie zależy od WiFi.
- **Potwierdzenie wizualne wzmacnia obserwację ciszy radiowej**: kamera świeciła nocą, ale nie zapisała żadnego prawidłowego trafienia WiFi. W tym konkretnym przypadku nie została usunięta.
- **Brak wykryć przy znanej kamerze nie oznacza automatycznie awarii detektora.** Najpierw zaktualizuj firmware i sprawdź, czy kamera nadal stoi.
- **Projekt open source wdraża poprawki, gdy społeczność wykryje luki.** Czytaj zgłoszenia GitHub, nie tylko README.

### Następne kroki

1. **Zaktualizuj firmware** do bieżącej gałęzi `main` przed dalszym rozwiązywaniem problemów: **[github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)**
2. **Przeczytaj pełny przewodnik sprzętowy**, jeśli jeszcze go nie znasz: **[Projekt wykrywania Flock-You: sprzętowy przewodnik po kontrnadzorze](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**
3. **Sprawdź przypuszczalne martwe strefy** w **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)**, zanim uznasz, że urządzenie coś pominęło.
4. **Poznaj system, z którym się mierzysz**: **[Nadzór kamer Flock Safety: skala, obawy o prywatność i strategie ochrony](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**
5. **Połącz wykrywanie WiFi i sieci komórkowych** za pomocą **[Rayhunter](/articles/how-to-flash-rayhunter-devices-complete-guide/)**. Żadna z metod w tym artykule nie wykrywa symulatorów stacji bazowych.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Kup gotowe urządzenia FlockYou i oszczędź 20%
{{< /centerbutton >}}

______

## Powiązane artykuły

| Artykuł | Zakres |
|---|---|
| **[Projekt wykrywania Flock-You: sprzętowy przewodnik po kontrnadzorze](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Trzy platformy sprzętowe, konfiguracja firmware i metoda wykrywania |
| **[Flock Finder: mapa podejrzanych kamer Flock w twojej okolicy](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Porównanie martwej strefy z ponad 40 000 lokalizacji przed diagnostyką urządzenia |
| **[Kamery Flock: narzędzie bezpieczeństwa publicznego czy maszyna do nadzoru bez nakazu?](/articles/flock-cameras-public-safety-or-surveillance-2026/)** | Analiza możliwości bazy Flock i znaczenia pytania o nakaz |
| **[Nadzór kamer Flock Safety: skala, obawy o prywatność i strategie ochrony](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Skala wdrożeń, przypadki nadużyć i zasoby dla społeczności |
| **[Podatności kamer Flock Safety: znaleziono ponad 50 błędów](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)** | Badania sprzętu i oprogramowania kamer |
| **[Jak wgrać firmware do urządzeń Rayhunter: kompletny przewodnik](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Wykrywanie IMSI catcherów i stingrayów, komórkowy odpowiednik luki WiFi |

______

## Źródła

1. [Repozytorium GitHub Flock-You - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [Zgłoszenie GitHub #20 - nie wykrywa kamer Flock, ale wykrywa inne urządzenia](https://github.com/colonelpanichacks/flock-you/issues/20)
3. [Zgłoszenie GitHub #43 - sygnał 5GHz? Nowe filtrowanie OUI i MAC](https://github.com/colonelpanichacks/flock-you/issues/43)
4. [Zbiór badań OUI NitekryDPaul](https://github.com/colonelpanichacks/flock-you/blob/main/datasets/NitekryDPaul_wifi_ouis.md)
5. [nitekry/nite-oui-collection](https://github.com/nitekry/nite-oui-collection)
6. [DeFlock Joplin - społecznościowe badania ALPR](https://deflockjoplin.today)
7. [Pintor, L. i Atzori, L. (2022) - analiza żądań probe WiFi i fingerprinting Information Element, IEEE GLOBECOM](https://ieeexplore.ieee.org/document/10001618)
8. [WIRED i 404 Media - hakerzy dostali się do kamery Flock](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
9. [Micah Lee - kamery Flock mają ponad 50 podatności i zakodowane poświadczenia](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
10. [Distributed Denial of Secrets - obrazy systemu plików kamery ALPR Flock](https://ddosecrets.org/article/flock-alpr-camera)
11. [Hackaday - Tydzień w bezpieczeństwie: stare kamery Flock, poprawki Microsoftu i badania SSH](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
12. [WiFi Mothership - wykrywanie ALPR Flock i informacje o urządzeniach](https://wifimothership.com/flock)
13. [GainSec - badania firmware i komunikaty bezpieczeństwa](https://gainsec.com/)
8. [Polowanie na ukryty probe - zachowanie wildcard probe dla ukrytych SSID](https://goodwi.fi/posts/2023/12/hunt-for-hidden-probe/)
9. [DeFlock - społecznościowa mapa kamer ALPR](https://deflock.org/)
10. [Colonel Panic Tech - OUI-SPY i sprzęt do wykrywania](https://colonelpanic.tech)
11. [STS Collective - urządzenia FlockYou](https://stscollective.com/discount/SIMEONONSECURITY)
12. [Coś dziwnego dzieje się z kamerami Flock - Valleytech Custom Solutions](https://www.youtube.com/shorts/cVf-id71BuQ)
13. [Wardriving podczerwieni dla kamer Flock - Valleytech Custom Solutions](https://www.youtube.com/shorts/mzpr6bslsYA)
14. [Kamery Flock nadal działają, ale nie nadają - Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0)
15. [Automatyczne rozpoznawanie tablic - Wikipedia (podczerwień w systemach ANPR/ALPR)](https://en.wikipedia.org/wiki/Automatic_number-plate_recognition)
16. [Seeed Studio XIAO ESP32S3 Sense](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html)
17. [Moduł GNSS L76K dla Seeed Studio XIAO](https://www.seeedstudio.com/L76K-GNSS-Module-for-Seeed-Studio-XIAO-p-5864.html)

