---
title: "Kurs Network Plus: Zrozumienie modelu OSI, topologii i typów sieci"
date: 2023-07-01
toc: true
draft: false
description: "Poznaj znaczenie podstaw sieci, w tym modelu OSI, topologii sieci i różnych typów sieci, dla budowania wydajnych i niezawodnych infrastruktur."
genre: ["Technologia", "Tworzenie sieci", "Infrastruktura IT", "Architektura sieci", "Informatyka", "Transmisja danych", "Technologia informacyjna", "Bezpieczeństwo sieci", "Zarządzanie siecią", "Internet"]
tags: ["podstawy sieci", "Model OSI", "topologie sieci", "typy sieci", "enkapsulacja danych", "warstwy sieci", "Topologia siatki", "topologia gwiazdy", "topologia magistrali", "topologia pierścienia", "topologia hybrydowa", "sieć peer-to-peer", "sieć klient-serwer", "LAN", "MAN", "WAN", "WLAN", "PAN", "CAN", "SAN", "SDWAN", "MPLS", "mGRE", "vSwitch", "vNIC", "NFV", "hiperwizor", "łącza satelitarne", "DSL", "internet kablowy", "linia dzierżawiona", "metro-optyczny"]
cover: "/img/cover/A_symbolic_illustration_of_interconnected_nodes.png"
coverAlt: "Symboliczna ilustracja połączonych węzłów tworzących sieć."
coverCaption: "Uwolnienie mocy podstaw sieci."
---

#### [Click Here to Return To the Network Plus Course Page](/network-plus-start)

Podstawy sieci odgrywają kluczową rolę w dzisiejszym połączonym świecie. Niezależnie od tego, czy chodzi o przeglądanie Internetu, wysyłanie wiadomości e-mail czy strumieniowe przesyłanie filmów, wszystkie te czynności opierają się na solidnej infrastrukturze sieciowej. W tym artykule przedstawimy przegląd **podstaw sieci**, zaczynając od **modelu OSI** i **koncepcji enkapsulacji**. Zbadamy również różne ** topologie sieciowe** i ich charakterystykę.

## Przegląd modelu OSI i koncepcji enkapsulacji

Model **OSI (Open Systems Interconnection)** to ramy koncepcyjne, które definiują funkcje sieci w siedmiu różnych warstwach. Każda warstwa ma określone obowiązki i współdziała z warstwami powyżej i poniżej. Zrozumienie modelu OSI jest niezbędne do zrozumienia, w jaki sposób dane są przesyłane i przetwarzane w sieci.

### Warstwy modelu OSI

{{< youtube id="G7aVKgGUe9c" >}}

1. **Warstwa 1 - Fizyczna**: Warstwa fizyczna zajmuje się faktyczną transmisją i odbiorem nieprzetworzonych strumieni bitów za pośrednictwem mediów fizycznych, takich jak przewody miedziane, kable światłowodowe lub połączenia bezprzewodowe.

2. **Warstwa 2 - Łącza danych**: Warstwa łącza danych jest odpowiedzialna za ustanawianie i kończenie połączeń między urządzeniami sieciowymi. Obsługuje również wykrywanie i korekcję błędów, aby zapewnić niezawodną transmisję danych.

3. **Warstwa 3 - Sieć**: Warstwa sieci ułatwia trasowanie pakietów danych od źródła do miejsca docelowego przez wiele węzłów sieci. Zajmuje się kwestiami związanymi z **przeciążeniem sieci**, **routingiem pakietów** i **adresowaniem IP**.

4. **Warstwa 4 - Transport**: Warstwa transportowa zapewnia **dostarczanie danych od końca do końca** i ustanawia niezawodną komunikację między źródłem a miejscem docelowym. Zarządza **segmentacją danych**, **kontrolą przepływu** i **odzyskiwaniem błędów**.

5. **Warstwa 5 - Sesja**: Warstwa sesji ustanawia, utrzymuje i kończy sesje komunikacyjne między aplikacjami. Zarządza **kontrolą dialogu** i **synchronizacją** między urządzeniami.

6. **Warstwa 6 - Prezentacja**: Warstwa prezentacji skupia się na **składzie** i **semantyce** informacji wymienianych między aplikacjami. Obsługuje **szyfrowanie danych**, **kompresję** i **formatowanie** w celu właściwej interpretacji.

7. **Warstwa 7 - Aplikacja**: Warstwa aplikacji reprezentuje rzeczywiste aplikacje i usługi sieciowe używane przez użytkowników końcowych. Zapewnia usługi takie jak **mail**, **transfer plików**, **przeglądanie stron internetowych** i **zdalny dostęp**.

{{< inarticle-dark >}}

### Enkapsulacja i dekapsulacja danych w kontekście modelu OSI

{{< youtube id="_fPzeQ9PHhA" >}}

Enkapsulacja danych to proces dodawania nagłówków i zwiastunów specyficznych dla protokołu do ładunku w każdej warstwie modelu OSI. Ta enkapsulacja umożliwia przesyłanie danych przez sieć i dotarcie do zamierzonego miejsca docelowego. I odwrotnie, dekapsulacja polega na usunięciu dodanych nagłówków i zwiastunów w każdej warstwie modelu OSI w celu wyodrębnienia oryginalnego ładunku.

W kontekście modelu OSI następujące elementy przyczyniają się do enkapsulacji i dekapsulacji danych:

- **Nagłówek Ethernet**: Nagłówek Ethernet zawiera informacje takie jak adresy MAC urządzeń źródłowych i docelowych, typ protokołu Ethernet i mechanizmy sprawdzania błędów.

- **Nagłówek protokołu internetowego (IP)**: Nagłówek IP zawiera źródłowy i docelowy adres IP, identyfikację pakietu, czas życia i inne istotne parametry dla komunikacji opartej na protokole IP.

- Nagłówki **Transmission Control Protocol (TCP)/User Datagram Protocol (UDP)**: Nagłówki TCP i UDP zawierają numery portów, numery sekwencyjne, sumy kontrolne i inne istotne informacje niezbędne do komunikacji w warstwie transportowej.

- Flagi TCP**: Flagi TCP wskazują konkretne funkcje kontrolne i opcje podczas sesji TCP. Obejmują one flagi do nawiązywania połączeń, potwierdzania danych, kończenia połączeń i inne.

- **Ładunek**: Ładunek to rzeczywiste dane, które są przesyłane, takie jak strona internetowa, wiadomość e-mail lub plik multimedialny.

- **Maximum Transmission Unit (MTU)**: MTU reprezentuje maksymalny rozmiar pakietu danych, który może być przesyłany przez sieć bez fragmentacji.

{{< inarticle-dark >}}

## Badanie topologii sieci i ich charakterystyki

{{< youtube id="zbqrNg4C98U" >}}

Topologie sieci definiują fizyczny lub logiczny układ urządzeń sieciowych i połączeń między nimi. Każda topologia ma swoje mocne i słabe strony, a wybór odpowiedniej topologii zależy od różnych czynników, takich jak skalowalność, odporność na błędy i koszty.

### Topologia siatki

W ** topologii siatki** każde urządzenie jest połączone z każdym innym urządzeniem, tworząc w pełni połączoną sieć. Taka redundancja zapewnia wysoką odporność na awarie, ale może być kosztowna i skomplikowana w implementacji. Topologie siatkowe są powszechnie stosowane w infrastrukturze krytycznej i środowiskach obliczeniowych o wysokiej wydajności.

### Topologia gwiazdy/koncentratora i szprychy

W ** topologii gwiazdy** wszystkie urządzenia są podłączone do centralnego koncentratora lub przełącznika. Koncentrator działa jako centralny punkt połączenia, ułatwiając komunikację między urządzeniami. Ta topologia jest łatwa w zarządzaniu i zapewnia scentralizowaną kontrolę, ale może stworzyć pojedynczy punkt awarii, jeśli koncentrator ulegnie awarii.

### Topologia magistrali

W ** topologii magistrali** wszystkie urządzenia są podłączone do pojedynczej linii komunikacyjnej, zwanej magistralą. Dane są przesyłane sekwencyjnie wzdłuż magistrali, a urządzenia odbierają przeznaczone dla nich dane. Topologie magistrali są proste i opłacalne, ale mogą doświadczać przeciążenia sieci i mają ograniczoną skalowalność.

### Topologia pierścienia

W ** topologii pierścienia**, urządzenia są połączone w okrągły łańcuch, z każdym urządzeniem łączącym się z następnym i ostatnim urządzeniem łączącym się z pierwszym. Dane krążą w jednym kierunku wokół pierścienia. Topologie pierścieniowe oferują sprawiedliwy dostęp i mogą obsługiwać duże obciążenia, ale mogą być narażone na zakłócenia sieci w przypadku awarii urządzenia.

### Topologia hybrydowa

Topologia hybrydowa** łączy w sobie wiele topologii, tworząc bardziej elastyczną i skalowalną sieć. Na przykład, połączenie topologii gwiazdy i pierścienia może zapewnić redundancję i odporność na błędy przy jednoczesnym zachowaniu skalowalności.

## Typy i charakterystyka sieci

{{< youtube id="6a-roIeJ_a4" >}}

Sieć obejmuje różne typy sieci, z których każda zaspokaja określone potrzeby i przypadki użycia. Oto kilka popularnych typów sieci:

### Sieć peer-to-peer (P2P)

W **sieci peer-to-peer (P2P)**, urządzenia łączą się ze sobą bezpośrednio, bez polegania na scentralizowanym serwerze. Sieci P2P są często wykorzystywane do udostępniania plików, aplikacji do współpracy i systemów zdecentralizowanych.

### Sieć klient-serwer

Sieć **klient-serwer** obejmuje klientów, którzy żądają usług lub zasobów, oraz serwery, które dostarczają te usługi lub zasoby. Sieci klient-serwer są szeroko stosowane w środowiskach korporacyjnych, gdzie scentralizowana kontrola i zarządzanie zasobami są niezbędne.

### Sieć lokalna (LAN)

**Sieć lokalna (LAN)** obejmuje niewielki obszar geograficzny, taki jak budynek biurowy lub dom. Umożliwia ona urządzeniom w sieci komunikację i współdzielenie zasobów. Sieci LAN są powszechnie używane do komunikacji wewnętrznej, udostępniania plików i drukarek.

### Sieć metropolitalna (MAN)

**Sieć metropolitalna (MAN)** obejmuje większy obszar geograficzny niż sieć LAN, ale mniejszy niż sieć WAN. Łączy ona wiele sieci LAN w obrębie miasta lub regionu metropolitalnego. Sieci MAN są często używane przez organizacje, które wymagają szybkiej łączności między swoimi oddziałami lub kampusami.

### Sieć rozległa (WAN)

**Sieć rozległa (WAN)** obejmuje duży obszar geograficzny, łącząc wiele sieci LAN lub MAN w różnych miastach, krajach lub kontynentach. Sieci WAN opierają się na różnych technologiach komunikacyjnych, takich jak linie dzierżawione, satelity i sieci optyczne, do przesyłania danych na duże odległości.

### Bezprzewodowa sieć lokalna (WLAN)

**Bezprzewodowa sieć lokalna (WLAN)** zapewnia bezprzewodową łączność na ograniczonym obszarze, zazwyczaj przy użyciu technologii Wi-Fi. Sieci WLAN są powszechnie spotykane w domach, biurach, kawiarniach i miejscach publicznych, umożliwiając użytkownikom podłączanie urządzeń bez fizycznych kabli.

### Sieć osobista (PAN)

**Sieć osobista (PAN)** obejmuje niewielki obszar, zazwyczaj w obrębie miejsca pracy danej osoby lub w jej bezpośrednim otoczeniu. Umożliwia komunikację między urządzeniami osobistymi, takimi jak smartfony, tablety i urządzenia do noszenia.

### Sieć kampusowa (CAN)

Sieć kampusowa (CAN)** to sieć obejmująca kampus uniwersytecki lub duży kampus korporacyjny. Zapewnia ona łączność z różnymi budynkami i obiektami na terenie kampusu, ułatwiając komunikację i współdzielenie zasobów.

### Sieć pamięci masowej (SAN)

Sieć SAN (Storage Area Network) jest wyspecjalizowaną siecią przeznaczoną do przechowywania danych. Umożliwia ona wielu serwerom dostęp do współdzielonych zasobów pamięci masowej, takich jak macierze dyskowe lub biblioteki taśmowe, za pośrednictwem szybkiego połączenia.

### Sieć rozległa definiowana programowo (SDWAN)

**SDWAN (Software-Defined Wide Area Network) to technologia, która upraszcza zarządzanie i konfigurację sieci WAN poprzez oddzielenie płaszczyzny kontroli sieci od sprzętu bazowego. Zapewnia scentralizowaną kontrolę i umożliwia organizacjom dynamiczne zarządzanie infrastrukturą WAN.

### Wieloprotokołowe przełączanie etykiet (MPLS)

**Multiprotocol Label Switching (MPLS)** to technika routingu, która wykorzystuje etykiety do wydajnego przesyłania pakietów danych przez sieć. Zapewnia ona wysoką wydajność, niezawodność i bezpieczeństwo komunikacji, dzięki czemu jest odpowiednia dla dostawców usług i przedsiębiorstw.

### Multipoint Generic Routing Encapsulation (mGRE)

**Multipoint Generic Routing Encapsulation (mGRE)** to technika wykorzystywana do tworzenia wirtualnych sieci prywatnych (VPN) poprzez enkapsulację pakietów danych i wysyłanie ich przez sieć wielopunktową. Umożliwia ona wydajną komunikację między wieloma lokalizacjami lub punktami końcowymi.

{{< inarticle-dark >}}

## Koncepcje sieci wirtualnych

{{< youtube id="A29g5-Os-u8" >}}

Technologie wirtualizacji zrewolucjonizowały sposób projektowania i zarządzania sieciami. Oto kilka koncepcji sieci wirtualnych:

### vSwitch

**vSwitch**, czyli wirtualny przełącznik, to oparty na oprogramowaniu przełącznik sieciowy, który działa w zwirtualizowanym środowisku, takim jak hiperwizor. Umożliwia on komunikację między maszynami wirtualnymi (VM) i łączy je z siecią fizyczną.

### Wirtualna karta sieciowa (vNIC)

**Wirtualna karta sieciowa (vNIC)** to zwirtualizowana karta sieciowa, która emuluje fizyczną kartę sieciową w maszynie wirtualnej. Umożliwia ona maszynom wirtualnym komunikację z wirtualnym przełącznikiem i siecią fizyczną.

### Wirtualizacja funkcji sieciowych (NFV)

**Wirtualizacja funkcji sieciowych (NFV)** to podejście, które wirtualizuje funkcje sieciowe, takie jak zapory ogniowe, routery i load balancery, uruchamiając je na standardowych serwerach zamiast na dedykowanych urządzeniach sprzętowych. Oferuje elastyczność, skalowalność i oszczędność kosztów infrastruktury sieciowej.

### Hiperwizor

Hiperwizor** to warstwa oprogramowania, która umożliwia tworzenie i zarządzanie maszynami wirtualnymi. Zapewnia abstrakcję sprzętową, umożliwiając uruchamianie wielu maszyn wirtualnych na jednym serwerze fizycznym.

## Linki do dostawców

{{< youtube id="M2cJtZXJrpE" >}}

Łącza dostawcy odnoszą się do różnych typów opcji łączności oferowanych przez dostawców usług. Oto kilka typowych linków dostawcy:

### Satelita

**Łącza satelitarne** wykorzystują satelity komunikacyjne do przesyłania danych na duże odległości. Są one często używane w odległych obszarach, gdzie inne opcje łączności są ograniczone.

### Cyfrowa linia abonencka (DSL)

**Digital Subscriber Line (DSL)** to technologia zapewniająca szybki dostęp do Internetu za pośrednictwem istniejących linii telefonicznych. Oferuje szybsze prędkości niż tradycyjne połączenia dial-up i jest szeroko dostępna w środowiskach mieszkalnych i biznesowych.

### Kabel

**Internet kablowy** wykorzystuje te same kable koncentryczne, co telewizja kablowa, aby zapewnić szybki dostęp do Internetu. Jest popularny w obszarach mieszkalnych i oferuje szybsze prędkości w porównaniu do DSL.

### Linia dzierżawiona

**Linia dzierżawiona** to dedykowane połączenie punkt-punkt między dwiema lokalizacjami. Zapewnia niezawodną i bezpieczną łączność, dzięki czemu jest odpowiednia dla firm o wysokich wymaganiach dotyczących przepustowości.

### Metro-Optical

Sieci **metro-optyczne** wykorzystują technologię światłowodową do zapewnienia szybkiej łączności na obszarze metropolitalnym. Oferują one wysoką przepustowość i niskie opóźnienia, idealne dla aplikacji intensywnie wykorzystujących dane.

______

Podsumowując, zrozumienie podstaw sieci ma kluczowe znaczenie dla budowania i utrzymywania niezawodnej i wydajnej infrastruktury sieciowej. Model **OSI** zapewnia ramy do zrozumienia, w jaki sposób dane są przesyłane i przetwarzane w różnych warstwach sieci. Dodatkowo, znajomość ** topologii sieci** pomaga w projektowaniu sieci, które spełniają określone wymagania dotyczące skalowalności, odporności na awarie i efektywności kosztowej. Zapoznając się z różnymi **typami sieci**, **koncepcjami sieci wirtualnych** i **łączami dostawców**, możemy podejmować świadome decyzje podczas konfigurowania i zarządzania sieciami.

Odniesienia:
- [OSI Model - Cisco](https://learningnetwork.cisco.com/s/article/osi-model-reference-chart)
- [How Does the Internet Work? - Stanford University](https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm)
