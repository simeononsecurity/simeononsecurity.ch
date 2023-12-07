---
title: "Kurs Network Plus: Protokoły routingu, koncepcje i optymalizacja"
date: 2023-07-07
toc: true
draft: false
description: "Poznaj świat technologii i koncepcji routingu, od dynamicznych protokołów routingu, takich jak RIP, OSPF, EIGRP i BGP, po protokoły stanu łącza, wektora odległości i routingu hybrydowego, a także konfigurację routingu statycznego i tras domyślnych."
genre: ["Technologia", "Tworzenie sieci", "Routing", "Protokoły sieciowe", "Zarządzanie siecią", "Routing dynamiczny", "Routing statyczny", "Zarządzanie przepustowością", "Jakość usług", "Urządzenia sieciowe"]
tags: ["technologie routingu", "protokoły routingu dynamicznego", "RIP", "OSPF", "EIGRP", "BGP", "stan łącza", "wektor odległości", "hybrydowe protokoły routingu", "routing statyczny", "trasy domyślne", "odległość administracyjna", "Routing zewnętrzny", "routing wewnętrzny", "czas na życie", "Zarządzanie przepustowością", "kształtowanie ruchu", "jakość usług", "urządzenia sieciowe", "routery", "przełączniki", "firewalle", "load balancery", "punkty dostępu", "optymalizacja sieci", "wydajność sieci", "bezpieczeństwo sieci", "architektura sieci", "ruch sieciowy"]
cover: "/img/cover/An_illustration_of_interconnected_network_devi.png"
coverAlt: "Ilustracja połączonych urządzeń sieciowych z danymi przepływającymi między nimi."
coverCaption: "Nawigacja po cyfrowej autostradzie: Optymalizacja routingu sieci w celu uzyskania najwyższej wydajności"
---

#### [Click Here to Return To the Network Plus Course Page](/network-plus-start)

## Wprowadzenie

W dzisiejszym połączonym świecie wydajny routing sieciowy jest niezbędny do płynnej transmisji danych i komunikacji. Technologie i koncepcje routingu odgrywają kluczową rolę w kierowaniu ruchem sieciowym i optymalizacji wydajności sieci. W tym artykule omówiono różne protokoły routingu, takie jak RIP, OSPF, EIGRP i BGP, a także protokoły stanu łącza, wektora odległości i routingu hybrydowego. Zagłębimy się również w konfigurację i wykorzystanie routingu statycznego i tras domyślnych. Dodatkowo porównamy i zestawimy ze sobą różne urządzenia i ich rozmieszczenie w sieci.

{{< youtube id="YRzr56cwgCg" >}}

## Protokoły routingu dynamicznego

Dynamiczne protokoły routingu zostały zaprojektowane w celu zautomatyzowania procesu wymiany informacji o routingu między routerami. Dostosowują się one do zmian w sieci, takich jak modyfikacje topologii lub awarie łączy, dynamicznie aktualizując tabele routingu. Przyjrzyjmy się bliżej niektórym powszechnie używanym protokołom routingu dynamicznego:

### Routing Internet Protocol (RIP)

Routing Internet Protocol (RIP) to protokół routingu wektora odległości, który działa w oparciu o liczbę przeskoków między routerami. Wykorzystuje on metrykę liczby przeskoków w celu określenia najlepszej ścieżki do sieci docelowej. Protokół RIP obsługuje zarówno protokół IPv4, jak i IPv6 i jest odpowiedni dla małych i średnich sieci.

### Open Shortest Path First (OSPF)

Open Shortest Path First (OSPF) to protokół routingu stanu łącza, który oblicza najkrótszą ścieżkę do miejsca docelowego przy użyciu algorytmu Dijkstry. Bierze on pod uwagę różne wskaźniki, takie jak przepustowość, opóźnienie i niezawodność, aby określić optymalną trasę. OSPF jest szeroko stosowany w dużych sieciach korporacyjnych ze względu na jego skalowalność i szybką zbieżność.

### Rozszerzony protokół routingu bramy wewnętrznej (EIGRP)

Enhanced Interior Gateway Routing Protocol (EIGRP) to hybrydowy protokół routingu opracowany przez firmę Cisco. Łączy on w sobie najlepsze cechy protokołów wektora odległości i stanu łącza. EIGRP wykorzystuje algorytm DUAL (Diffusing Update Algorithm) do obliczania tras i zapewnia zaawansowane funkcje, takie jak równoważenie obciążenia o nierównych kosztach i podsumowywanie tras.

### Protokół bramy granicznej (BGP)

Border Gateway Protocol (BGP) to protokół bramy zewnętrznej używany do routingu między systemami autonomicznymi (AS) w Internecie. BGP jest wysoce skalowalny i umożliwia systemom autonomicznym wymianę informacji o routingu. Wykorzystuje atrybuty ścieżek i zasady do podejmowania decyzji dotyczących routingu w oparciu o czynniki takie jak zasady sieciowe, długość ścieżki i ścieżka AS.

## Protokoły stanu łącza, wektora odległości i routingu hybrydowego

Protokoły routingu można podzielić na protokoły stanu łącza, wektora odległości i hybrydowe w oparciu o ich działanie i informacje, których używają do określania tras.

### Protokoły routingu stanu łącza

Protokoły routingu stanu łącza, takie jak OSPF, utrzymują szczegółową mapę całej sieci poprzez wymianę informacji o stanie łącza między routerami. Każdy router buduje topologiczną bazę danych, umożliwiając mu obliczenie najlepszej ścieżki do sieci docelowej w oparciu o różne metryki.

### Protokoły routingu wektora odległości

Protokoły routingu wektora odległości, takie jak RIP, wykorzystują prostą metrykę (np. liczbę przeskoków) i wymieniają informacje o routingu z sąsiednimi routerami. Routery okresowo ogłaszają swoje tabele routingu sąsiednim routerom, umożliwiając im zbudowanie obrazu sieci. Protokoły wektora odległości mają ograniczoną wiedzę na temat całej sieci i mogą być podatne na pętle routingu.

### Hybrydowe protokoły routingu

Hybrydowe protokoły routingu, takie jak EIGRP, łączą w sobie cechy zarówno protokołów stanu łącza, jak i wektora odległości. Utrzymują one tabelę topologii podobną do protokołów stanu łącza, ale wykorzystują algorytmy wektora odległości do obliczania tras. Protokoły hybrydowe oferują korzyści w postaci szybszej konwergencji i mniejszego narzutu.

## Routing statyczny i trasy domyślne

Routing statyczny polega na ręcznym konfigurowaniu tablicy routingu na routerach, określając ścieżki dostępu do określonych sieci. Jest on zwykle używany w scenariuszach, w których zmiany topologii sieci są minimalne lub przewidywalne. Trasy statyczne są łatwe w konfiguracji i mogą być przydatne w przypadku małych sieci lub określonych segmentów sieci.

Trasa domyślna, znana również jako brama ostatniej instancji, jest używana, gdy nie istnieje wyraźna trasa dla sieci docelowej. Działa jako trasa przechwytująca i jest skonfigurowana na routerach, aby kierować ruch do bramy domyślnej, gdy router nie ma wiedzy o sieci docelowej.

## Odległość administracyjna, zewnętrzna vs. wewnętrzna i czas życia

{{< youtube id="HR59xk4umWY" >}}

### Odległość administracyjna

Odległość administracyjna (AD) to wartość przypisywana protokołom routingu w celu określenia priorytetu tras, gdy na routerze działa wiele protokołów. Niższe wartości odległości administracyjnej oznaczają wyższy priorytet dla danego protokołu routingu. Na przykład, OSPF ma niższy AD (110) niż RIP (120), więc trasy OSPF będą preferowane w stosunku do tras RIP.

### Routing zewnętrzny a wewnętrzny

Zewnętrzne protokoły routingu, takie jak BGP, są używane do wymiany informacji o routingu między systemami autonomicznymi (AS). Obsługują one routing pomiędzy różnymi organizacjami i dostawcami usług. Z drugiej strony, wewnętrzne protokoły routingu, takie jak RIP, OSPF i EIGRP, są używane do routingu wewnątrz systemu autonomicznego.

### Czas życia (TTL)

Time to Live (TTL) to pole w pakietach IP, które określa maksymalną liczbę przeskoków, które pakiet może pokonać, zanim zostanie odrzucony. Zapobiega to krążeniu pakietów w nieskończoność w sieci w przypadku wystąpienia pętli routingu lub innych problemów. Każdy router zmniejsza wartość TTL, gdy pakiet przechodzi przez sieć.

## Zarządzanie przepustowością

Efektywne zarządzanie przepustowością ma kluczowe znaczenie dla optymalizacji wydajności sieci i zapewnienia płynnego przepływu ruchu. Dwa ważne aspekty zarządzania przepustowością to kształtowanie ruchu i jakość usług (QoS).

### Kształtowanie ruchu

Kształtowanie ruchu to technika wykorzystywana do kontrolowania szybkości transmisji danych w sieci. Umożliwia administratorom sieci kształtowanie przepływu ruchu poprzez definiowanie limitów przepustowości i nadawanie priorytetów określonym typom ruchu. Pomaga to zapobiegać przeciążeniom sieci i zapewnia, że krytyczne aplikacje otrzymują wystarczającą przepustowość.

### Jakość usług (QoS)

Quality of Service (QoS) odnosi się do zdolności sieci do nadawania priorytetów i przydzielania zasobów różnym typom ruchu w oparciu o ich znaczenie i wymagania. Mechanizmy QoS, takie jak priorytetyzacja ruchu, alokacja przepustowości i zarządzanie przeciążeniami, pomagają zapewnić optymalną wydajność dla aplikacji działających w czasie rzeczywistym, takich jak głos i wideo.

## Porównanie i rozmieszczenie urządzeń

Różne urządzenia odgrywają określone role w sieci i mają różne funkcje, które sprawiają, że nadają się do określonych zadań. Porównajmy i porównajmy niektóre popularne urządzenia sieciowe i omówmy ich odpowiednie rozmieszczenie:

- **Routery**: Routery są odpowiedzialne za kierowanie ruchem pomiędzy różnymi sieciami. Działają one w warstwie sieciowej (warstwa 3) i wykorzystują protokoły routingu do określenia najlepszej ścieżki transmisji danych.

- Przełączniki**: Przełączniki działają w warstwie łącza danych (warstwa 2) i ułatwiają komunikację między urządzeniami w sieci lokalnej (LAN). Używają adresów MAC do przekazywania pakietów danych do zamierzonego odbiorcy.

- Firewalle**: Firewalle chronią sieci przed nieautoryzowanym dostępem i złośliwym ruchem. Egzekwują one zasady bezpieczeństwa poprzez inspekcję ruchu sieciowego i zezwalanie lub blokowanie określonych połączeń w oparciu o wcześniej zdefiniowane reguły.

- **Balansery obciążenia**: Load balancery rozdzielają przychodzący ruch sieciowy na wiele serwerów w celu optymalizacji wykorzystania zasobów, poprawy wydajności i zapewnienia wysokiej dostępności.

- **Punkty dostępowe**: Punkty dostępowe (AP) zapewniają bezprzewodową łączność z urządzeniami w sieci. Umożliwiają komunikację bezprzewodową poprzez przesyłanie i odbieranie danych między urządzeniami bezprzewodowymi a siecią przewodową.

Umiejscowienie tych urządzeń zależy od architektury sieci i wymagań. **Routery** są zwykle umieszczane na obwodzie sieci, aby obsługiwać ruch między sieciami. **Przełączniki** są wdrażane w sieciach LAN, aby łączyć urządzenia i ułatwiać lokalną komunikację. **Zapory sieciowe** są umieszczane pomiędzy sieciami w celu ochrony przed zagrożeniami zewnętrznymi. **Balancery obciążenia** są umieszczane przed serwerami internetowymi, aby efektywnie rozprowadzać ruch. **Punkty dostępowe** są strategicznie rozmieszczone, aby zapewnić zasięg sieci bezprzewodowej w pożądanych obszarach.

______

## Wnioski

Zrozumienie **technologii i koncepcji routingu** jest kluczowe dla administratorów sieci i specjalistów IT. **Dynamiczne protokoły routingu**, takie jak **RIP, OSPF, EIGRP i BGP** automatyzują proces wymiany informacji o routingu i dostosowują się do zmian w sieci. **Protokoły stanu łącza, wektora odległości i routingu hybrydowego** oferują różne podejścia do określania optymalnych tras. **Routing statyczny i trasy domyślne** zapewniają ręczną kontrolę nad decyzjami dotyczącymi routingu. Techniki **zarządzania przepustowością**, takie jak **kształtowanie ruchu i QoS**, zapewniają efektywne wykorzystanie sieci. Odpowiednie porównanie i rozmieszczenie urządzeń sieciowych zwiększa wydajność i bezpieczeństwo sieci.

Opanowując **technologie i koncepcje routingu**, administratorzy sieci mogą budować **solidne i wydajne sieci**, które spełniają wymagania nowoczesnej łączności.

______