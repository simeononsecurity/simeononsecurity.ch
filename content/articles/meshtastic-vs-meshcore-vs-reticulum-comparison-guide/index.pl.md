---
title: "Meshtastic vs MeshCore vs Reticulum"
date: 2026-09-01
lastmod: 2026-11-12
toc: true
draft: false
description: "Porównaj Meshtastic, MeshCore i Reticulum pod kątem routingu, czasu zajęcia kanału, infrastruktury, transportu i zastosowań poza siecią."
genre: ["LoRa", "Sieci mesh", "Łączność poza siecią", "Łączność awaryjna", "Krótkofalarstwo", "Open source", "Przygotowanie na katastrofy", "Sieci bezprzewodowe", "Prywatność", "Sieci komputerowe"]
tags: ["meshtastic vs meshcore vs reticulum", "sieć Reticulum", "meshtastic", "meshcore", "reticulum", "lxmf", "sieć mesh LoRa", "łączność poza siecią", "rnode", "radio pakietowe", "sieć niezależna od transportu", "sieci mesh", "łączność awaryjna", "społecznościowa sieć mesh", "czas zajęcia kanału LoRa", "kontrolowany flooding", "limit przeskoków", "węzeł przekaźnikowy", "serwer pokojowy", "aplikacja Sideband", "nomadnet", "meshchat", "łączność podczas katastrof", "radio poza siecią", "protokół sieci mesh", "regionalna sieć mesh", "inżynieria RF"]
cover: "/img/cover/meshtastic-meshcore-reticulum-network-comparison.webp"
coverAlt: "Ilustracja porównująca trzy systemy sieci mesh za pomocą węzłów, anten i linii połączeń na ciemnym, kolorowym tle, które przedstawia ich różne funkcje."
coverCaption: ""
ref: ["/articles/meshcore-vs-meshtastic-comparison-guide", "/articles/field-deployable-connectivity-and-data-security-for-edge-nodes"]
---

## Krótka odpowiedź

**Te trzy projekty nie rozwiązują tego samego problemu.** Meshtastic i MeshCore to systemy sieci mesh LoRa o różnych założeniach dotyczących routingu. Reticulum ma szerszy zakres. To niezależna od transportu warstwa sieciowa, która działa jednocześnie przez LoRa, radio pakietowe, Wi-Fi, Ethernet, łącza szeregowe i internet.

**Właściwe pytanie nie brzmi „który jest najlepszy?”.** Brzmi: „która architektura pasuje do sieci, którą chcę zbudować?”.

*Meshtastic pasuje do sieci ad hoc i użytkowników mobilnych.* **MeshCore pasuje do celowo budowanej, stałej infrastruktury.** **Reticulum pasuje do sieci, które muszą łączyć różne transporty lub spinać odrębne sieci.** Większości osób budujących jedną regionalną sieć LoRa wystarczy jedna z dwóch pierwszych opcji.

______

## Określ, jaką sieć budujesz

Zanim porównasz protokoły, zapisz, co ma robić sieć. Dla większości wdrożeń społecznościowych i systemów łączności awaryjnej przydatne cele to:

- **Działanie bez licencji**, aby każdy mógł uczestniczyć bez licencji krótkofalarskiej
- **Niedrogi sprzęt**, na którego wdrożenie społeczność może sobie pozwolić na większą skalę
- **Niskie zużycie energii**, najlepiej zasilanie solarne lub bateryjne
- **Łączność dalekiego zasięgu** bez sieci komórkowej i internetu
- **Niezależność od infrastruktury** energetycznej, dostawców internetu i operatorów
- **Łatwa konfiguracja i obsługa dla osób bez wiedzy radiowej**
- **Przydatność we wdrożeniu społecznościowym**, a nie tylko w piwnicy jednego operatora
- **Możliwość rozwoju poza garść węzłów** bez utraty stabilności
- **Przydatność podczas awarii infrastruktury**, gdy nie działają stacje komórkowe i internet
- **Niezawodne dostarczanie wiadomości ważniejsze od rekordowego zasięgu**

Pamiętaj o tej liście przez resztę artykułu. Każdy kompromis architektoniczny ocenimy według tych wymagań.

______

## Meshtastic

**Meshtastic** to najbardziej dojrzała i najszerzej wdrożona opcja. Dobrze sprawdza się u typowego użytkownika.

- **Dojrzały ekosystem** rozwijany aktywnie od lat
- **Duża społeczność**, aktywny serwer Discord i obszerna dokumentacja
- **Szeroka obsługa sprzętu** LILYGO, Heltec, RAK i Seeed
- **Dobre aplikacje mobilne** na iOS i Androida
- **Łatwy początek**, pierwsza konfiguracja zajmuje mniej niż 20 minut
- **Dobre wsparcie dla urządzeń przenośnych i użytkowników w ruchu**, którzy nieprzewidywalnie dołączają do sieci i ją opuszczają
- **Funkcje GPS i telemetrii** z rozwiniętym ekosystemem
- **Istniejące wdrożenia** w większości obszarów metropolitalnych ułatwiają rozpoczęcie, bo dołączasz do sieci zamiast budować ją od zera

Pełne omówienie routingu Meshtastic, zgodności sprzętu i konfiguracji w porównaniu z MeshCore znajdziesz w **[poradniku porównującym MeshCore i Meshtastic](/articles/meshcore-vs-meshtastic-comparison-guide/)**. Ten artykuł skupia się na najważniejszej kwestii architektonicznej dla większych wdrożeń: **kontrolowanym floodingu i limitach przeskoków**.

### Kontrolowany flooding i znaczenie przeskoków

Meshtastic rozsyła komunikaty za pomocą **kontrolowanego floodingu**. Gdy węzeł wysyła wiadomość, każdy węzeł, który ją odbierze, rozsyła pakiet dalej aż do osiągnięcia ustawionego limitu przeskoków. Żaden węzeł nie musi znać topologii sieci. Nowe węzły dołączają bez konfiguracji, a nieaktywne są automatycznie omijane, bo flooding znajduje inną trasę.

Domyślny limit wynosi **3 przeskoki**. Maksymalny to **7**. Unikaj sformułowania „Meshtastic działa tylko na siedmiu przeskokach”. *Właściwe pytanie brzmi, ile kosztuje zwiększenie tej wartości.*

Każdy dodatkowy przeskok powoduje ponowną transmisję wiadomości przez wszystkie węzły w zasięgu. Więcej przekazywania oznacza:

- **Więcej czasu zajętości kanału** na każdą wiadomość
- **Więcej powtórzonych transmisji**, bo każdy węzeł w zasięgu ponawia komunikat
- **Większą konkurencję** o wspólny kanał
- **Większe ryzyko kolizji**, gdy więcej urządzeń radiowych nadaje w tym samym oknie
- **Większe zużycie baterii** w każdym węźle, który odbiera i przekazuje dalej
- **Mniejszą dostępną przepustowość kanału** dla właściwego ruchu wiadomości

Przepustowość LoRa ogranicza czas zajętości kanału i regionalne limity cyklu pracy, a nie liczba węzłów. Sieć z dziesięcioma aktywnymi węzłami, które często rozgłaszają GPS i telemetrię, może nasycić kanał, którego pięćdziesiąt cichych czujników prawie by nie obciążyło. Dlatego gęsta sieć mesh z wysokim limitem przeskoków pogarsza się szybciej niż taka sama liczba węzłów przy niższym limicie i kontrolowanych odstępach telemetrii. **Meshtastic 2.6 poprawił to dla wiadomości bezpośrednich**, przechodząc po wykryciu trasy na routing przez następny węzeł. Ruch punkt-punkt nie zalewa już całego promienia przeskoków. Rozgłoszenia nadal są rozsyłane floodingiem.

W małej lub średniej sieci, na przykład klubie turystycznym, rzadko ma to znaczenie. W **sieci regionalnej przeznaczonej do pokrycia miasta lub kilku miejscowości** staje się głównym ograniczeniem projektu.

______

## MeshCore

**MeshCore opiera się na innym założeniu architektonicznym:** zamiast traktować każde urządzenie jako równorzędnego uczestnika przekazywania wiadomości, buduje zaplanowaną warstwę infrastruktury i kieruje do niej ruch.

### Role węzłów

Wdrożenia MeshCore opierają się na odrębnych rolach, a nie płaskiej grupie równoważnych węzłów:

- **Węzły towarzyszące lub klienckie** zawierają radio LoRa sparowane z telefonem lub laptopem i, jeśli infrastruktura jest w pobliżu, komunikują się za jej pośrednictwem
- **Repeatery** przekazują ruch między klientami a pozostałą infrastrukturą i wykonują większość pracy związanej z routingiem
- **Serwery pokojowe** (opcjonalne) obsługują rozmowy grupowe i dostarczają przechowywane wiadomości klientom po ich ponownym połączeniu

Najpierw następuje wykrycie trasy. Potem ruch przechodzi ustaloną ścieżką do celu, zamiast rozchodzić się do wszystkich węzłów w zasięgu. Zajętość kanału rośnie wraz z liczbą aktywnych rozmów, a nie całkowitą liczbą węzłów. To zupełnie inna krzywa wzrostu niż model floodingu Meshtastic.

### Dlaczego sprawdza się w stałej infrastrukturze

*To główny argument za MeshCore.* Model floodingu Meshtastic ma realne zalety w sieciach ad hoc i mobilnych: nie wymaga planowania ani utrzymywania infrastruktury i dobrze radzi sobie ze zmienną obecnością węzłów. Routing MeshCore ma przewagę, gdy **użytkownicy celowo wdrażają infrastrukturę**.

Sieć oparta na znanych repeaterach umieszczonych wysoko pozwala celowo zaprojektować zasięg. Nie zależy od tego, które węzły akurat znajdą się w swoim zasięgu danego dnia. Ma to znaczenie dla:

- **Stałych węzłów dachowych** z niezawodnym zasilaniem
- **Wież** i istniejącej infrastruktury komunikacyjnej
- **Solarnych repeaterów** w bezobsługowych lokalizacjach
- **Górskich lub wysoko położonych lokalizacji przekaźnikowych**
- **Infrastruktury należącej do społeczności**, współdzielonej przez kilka grup
- **Sieci regionalnych** obejmujących więcej niż jedną dzielnicę
- **Łączności awaryjnej**, w której przewidywalny zasięg liczy się bardziej niż elastyczność

Odnieś to do podstaw RF: **niezawodne łącza między dobrze rozmieszczonymi elementami infrastruktury są ważniejsze niż maksymalizacja zysku anteny, mocy nadawania czy teoretycznego zasięgu.** Protokół oparty na dedykowanych repeaterach wynagradza pracę inżynierii RF potrzebną do ich dobrego rozmieszczenia. Protokół oparty na floodingu mniej na niej zyskuje, ponieważ każdy węzeł wykonuje w przybliżeniu tę samą pracę, niezależnie od lokalizacji.

______

## Argument za węzłami mobilnymi i jego koszt

Częsta sugestia brzmi: *„Meshtastic jest lepszy dla węzłów mobilnych, a MeshCore dla stałych, więc użyjmy Meshtastic dla użytkowników, a MeshCore jako szkieletu sieci”.*

Na papierze brzmi to atrakcyjnie. W praktyce połączenie obu systemów nie daje automatycznie zalet każdego z nich, ponieważ **Meshtastic i MeshCore używają różnych architektur routingu i sieci i nie wymieniają między sobą wiadomości.** Połączenie ich wymaga warstwy tłumaczącej między niekompatybilnymi systemami, a nie prostego wyboru najlepszych elementów każdego z nich.

Po połączeniu obsługujesz:

- **Dwie osobne sieci**, każdą z własną topologią i zachowaniem
- **Dwa modele routingu**, które nie współdzielą stanu
- **Warstwę tłumaczącą**, wymagającą ciągłego rozwijania i utrzymania
- **Dodatkową infrastrukturę** do hostowania mostu
- **Więcej konfiguracji** w dwóch ekosystemach firmware'u zamiast jednego
- **Więcej punktów awarii**, bo sam most może zepsuć się niezależnie od obu sieci mesh
- **Trudniejsze diagnozowanie**, bo problem z dostarczeniem może dotyczyć jednej z sieci lub mostu między nimi

Przed wyborem takiego projektu zadaj sobie wprost pytanie: **czy dodatkowa złożoność rozwiązuje problem, z którym jeden dobrze dostrojony protokół mesh sobie nie poradzi?** Często poprawnie skonfigurowana sieć MeshCore z kilkoma mobilnymi węzłami towarzyszącymi albo sieć Meshtastic z kilkoma dobrze umieszczonymi przekaźnikami i wyższym limitem przeskoków daje większość praktycznych korzyści bez łączenia dwóch sieci.

______

## Reticulum

Reticulum zasługuje na osobną kategorię zamiast miejsca jako „trzecia opcja sieci mesh LoRa”, ponieważ nie jest przede wszystkim protokołem mesh LoRa. **Jego główną cechą jest niezależność od transportu.**

Reticulum to oparty na kryptografii stos sieciowy. Nie używa adresów źródłowych, więc pakiety nie zawierają informacji o miejscu pochodzenia. Każdy adres jest suwerenny: po wygenerowaniu staje się globalnie osiągalny w ciągu sekund lub minut i pozostaje osiągalny po fizycznym przeniesieniu urządzenia do innej części sieci. Cała komunikacja jest domyślnie szyfrowana kluczami efemerycznymi i z poufnością przekazywania. Reticulum odrzuca nieszyfrowane pakiety zamiast je dostarczać. Nie wymaga sterowników jądra. Działa w przestrzeni użytkownika na każdym systemie z Pythonem 3, również na Raspberry Pi Zero.

Reticulum obsługuje między innymi te interfejsy:

- **LoRa**, z użyciem sprzętu zgodnego z RNode (określony, otwarty projekt transceivera LoRa, który można zbudować, wgrać na popularne płytki lub kupić jako gotowy produkt)
- **Radio pakietowe**, przez dowolny TNC pracujący w trybie KISS, odpowiednie dla krótkofalarstwa VHF i UHF
- **Wi-Fi i przewodowy Ethernet**, z automatycznym wykrywaniem peerów bez routera i serwera DHCP
- **Łącza szeregowe** do bezpośrednich połączeń między urządzeniami
- **TCP i UDP w istniejących sieciach IP**, w tym w internecie
- **Sieć I2P** oraz własne interfejsy dla innych połączeń z mostem w Pythonie

Na Reticulum działają aplikacje takie jak **LXMF** (protokół wiadomości tolerujący opóźnienia) oraz narzędzia dla użytkowników, takie jak **Sideband**, **NomadNet** i społecznościowe klienty **MeshChat**. Zapewniają one sieciom Reticulum warstwę wiadomości i przeglądania, podobną do tej dostępnej domyślnie w Meshtastic i MeshCore.

{{< figure src="reticulum-transport-independent-heterogeneous-network.webp" alt="Diagram przedstawiający Reticulum łączący sieć mesh LoRa, radio pakietowe i łącze internetowe w jedną adresowalną, szyfrowaną sieć" >}}

### Kiedy Reticulum ma sens

Zalety Reticulum widać w heterogenicznej konfiguracji, na przykład:

**Sieć mesh LoRa → węzeł Reticulum → łącze IP → węzeł Reticulum → sieć radiowa**

Reticulum robi tu coś, czego nie robi Meshtastic ani MeshCore: łączy dwa różne systemy komunikacyjne w jedną adresowalną sieć. To konkretna potrzeba, a nie ogólna aktualizacja. Dobre zastosowania to:

- **Łączenie geograficznie oddalonych sieci** bez bezpośredniej drogi radiowej między nimi
- **Mostkowanie różnych fizycznych transportów**, na przykład sieci mesh LoRa z jednej strony i radia pakietowego z drugiej
- **Bramy radio-IP** przekazujące ruch między terenową siecią radiową a internetem
- **Sieci eksperymentalne i badawcze**, gdzie mieszanie transportów jest ważniejsze od prostoty wdrożenia
- **Sieci, w których jeden transport nie spełnia wszystkich wymagań** i trzeba połączyć kilka części

### Kiedy Reticulum dodaje niepotrzebną złożoność

Jeśli wszyscy używają zgodnego sprzętu LoRa, a rzeczywistym celem jest **jedna regionalna sieć mesh LoRa**, dodanie Reticulum daje mało korzyści i pociąga za sobą realny koszt. Każda dodatkowa warstwa stosu sieciowego oznacza więcej:

- **Konfiguracji**, którą trzeba ustawić poprawnie i spójnie na wszystkich węzłach
- **Oprogramowania** do zainstalowania, aktualizowania i diagnozowania
- **Sprzętu** w niektórych konfiguracjach, zależnie od sposobu łączenia interfejsów
- **Możliwości wystąpienia problemów**, gdy wiadomość nie zostanie dostarczona
- **Wymaganej wiedzy**, ponieważ operatorzy muszą poznać trzeci model sieci

*Używaj Reticulum, gdy niezależność transportu rozwiązuje rzeczywistą potrzebę, a nie tylko dlatego, że obsługuje więcej typów interfejsów niż alternatywa.* Problem limitu przeskoków w jednej sieci LoRa to problem strojenia Meshtastic lub MeshCore. Nie jest to problem niezależności transportu i Reticulum go w taki nie zmieni.

______

## Zbuduj jedną zdrową sieć mesh, zanim utworzysz trzy podzielone

Jeśli jeden protokół spełnia wymagania, **zbuduj jedną sprawną sieć** zamiast kilku mniejszych połączonych mostami. Zasada „najpierw jedna sieć mesh” powinna kierować większością powyższych decyzji.

W sieci społecznościowej **współpraca między osobami już z niej korzystającymi zwykle liczy się bardziej niż elastyczność architektury.** Duża, działająca sieć jednego protokołu ma większą praktyczną wartość niż trzy technicznie ciekawe, ale podzielone i tylko częściowo komunikujące się sieci.

### Istniejące sieci Meshtastic mają znaczenie

**Nie odrzucaj Meshtastic tylko dlatego, że MeshCore ma zalety architektoniczne dla stałej infrastruktury.** Jeśli w mieście są już dziesiątki lub setki węzłów Meshtastic, ta baza stanowi prawdziwą infrastrukturę i prawdziwą społeczność. Migracja ma koszt, którego nie uwzględnia porównanie specyfikacji:

- **Zainstalowany sprzęt** wymagający ponownego flashowania lub wymiany
- **Dotychczasowi użytkownicy** znający już sposób obsługi sieci
- **Wiedza społeczności** zgromadzona wokół istniejącego wdrożenia
- **Już rozmieszczone repeatery**, czasem na dachach lub wieżach, do których trudno było uzyskać dostęp
- **Doświadczenie konfiguracji** osób obsługujących sieć
- **Ustanowione kanały**, które użytkownicy już monitorują
- **Szkolenie** osób uczących się drugiego systemu

Wybór protokołu jest **częściowo problemem inżynieryjnym, a częściowo problemem przyjęcia przez społeczność.** Lepsza architektura na papierze nie wygrywa automatycznie, jeśli oznacza prośbę do działającej społeczności o rozpoczęcie od nowa.

______

## Problem sieci regionalnej

Rozważ hipotetyczne wdrożenie w kilku miastach:

**Miasto A, repeater, repeater, przekaźnik na wsi, repeater, Miasto B, repeater, Miasto C**

Zastanów się, jak każda architektura obsługuje tę trasę wraz z rozwojem sieci. Sieć mesh oparta na floodingu z limitem siedmiu przeskoków ma trudności z niezawodnym pokonaniem takiego łańcucha. Każdy przeskok zwiększa koszt czasu zajęcia kanału, a każdy dodatkowy aktywny węzeł po drodze zwiększa konkurencję. Ustrukturyzowana architektura repeaterów, taka jak MeshCore, została zbudowana właśnie dla takiego układu: znane punkty przekaźnikowe, celowe rozmieszczenie i routing skalujący się wraz z aktywnymi rozmowami, a nie całkowitą liczbą węzłów.

W tym scenariuszu **limity przeskoków, budżet czasu zajętości kanału, zachowanie routingu i projekt infrastruktury przestają być teorią** i zaczynają decydować o działaniu całej trasy. Przy skali geograficznej różnice architektoniczne między Meshtastic a MeshCore przestają być akademickie.

{{< figure src="regional-mesh-network-repeater-chain-scaling.webp" alt="Diagram regionalnego łańcucha sieci mesh łączącego trzy miasta repeaterami i wiejskim przekaźnikiem, pokazujący narastanie czasu zajętości kanału i liczby przeskoków wraz z odległością" >}}

______

## RF nadal ma większe znaczenie niż protokół

**Żadne sprytne oprogramowanie routingu nie utworzy drogi radiowej tam, gdzie fizycznie jej nie ma.** Zanim obwinisz protokół o problem z zasięgiem, sprawdź podstawy:

- **Wysokość anteny** nad przeszkodami
- **Widoczność radiowa** między końcami łącza
- **Prześwit strefy Fresnela**, odrębny od optycznej widoczności
- **Straty na linii zasilającej** wynikające z taniego lub zbyt długiego kabla koncentrycznego
- **Jakość anteny** i dopasowanie do używanego pasma
- **Poziom szumów** w miejscu odbioru
- **Ukształtowanie terenu** między węzłami
- **Lokalizacja węzłów** i realne możliwości jej poprawy
- **Zapas łącza**, różnica między odbieranym sygnałem a minimum potrzebnym do dekodowania

*Dobrze umieszczona antena 2 dBi na właściwym maszcie często działa lepiej niż źle umieszczona antena o dużym zysku przy oknie piwnicy.* Wybór protokołu określa, jak sieć obsługuje dostępne łącza. Nie tworzy połączeń tam, gdzie nie pozwala na to fizyka.

### Niezawodność ponad maksymalny zasięg

**Nie projektuj sieci wokół maksymalnego zasięgu, jaki łącze osiąga od czasu do czasu.** Projektuj ją tak, by połączenia działały niezawodnie.

W sieci społecznościowej lub awaryjnej **przewidywalne dostarczenie wiadomości na 15 mil ma większą praktyczną wartość niż łącze, które czasem osiąga 40 mil, a przez resztę czasu zawodzi.** Zbuduj nakładające się zasięgi niezawodnej infrastruktury zamiast gonić za rekordowymi łączami. Ta zasada dotyczy każdego protokołu.

______

## Który wybrać?

**Meshtastic ma sens**, gdy cenisz dojrzały ekosystem, łatwość rozpoczęcia, użytkowników przenośnych i mobilnych oraz zgodność z istniejącą społecznością Meshtastic. Dla większości osób zaczynających od zera to właściwy wybór domyślny.

**MeshCore zyskuje**, gdy celowo budujesz trwałą infrastrukturę LoRa i chcesz, by dedykowane repeatery tworzyły większą, ustrukturyzowaną sieć. Bardziej bezpośrednio niż projekt oparty na floodingu wynagradza planowanie i dobre rozmieszczenie repeaterów.

**Reticulum ma sens**, gdy problem wykracza poza jedną sieć mesh LoRa i trzeba połączyć różne transporty lub odrębne sieci w jeden adresowalny system.

W przypadku **darmowej, energooszczędnej, dalekosiężnej sieci infrastruktury społecznościowej, zbudowanej głównie ze stałych repeaterów**, skłaniaj się ku MeshCore. *Jeśli w twojej okolicy działa już zdrowa sieć Meshtastic, jej zastąpienie wymaga korzyści uzasadniających podział istniejącej społeczności.* Reticulum przydaje się, gdy jeden protokół mesh albo fizyczny transport przestaje spełniać wymagania, a nie tylko dlatego, że ma więcej funkcji.

______

## Źródła

1. [Algorytm rozgłaszania w sieci mesh Meshtastic](https://meshtastic.org/docs/overview/mesh-algo/)
2. [Konfiguracja LoRa w Meshtastic (hop_limit)](https://meshtastic.org/docs/configuration/radio/lora/)
3. [Oficjalna witryna MeshCore](https://meshcore.co.uk/)
4. [Stos sieciowy Reticulum](https://reticulum.network/)
5. [Czym jest Reticulum?](https://reticulum.network/manual/whatis.html)
6. [Konfiguracja interfejsów Reticulum](https://reticulum.network/manual/interfaces.html)
7. [Poradnik porównujący MeshCore i Meshtastic](/articles/meshcore-vs-meshtastic-comparison-guide/)
