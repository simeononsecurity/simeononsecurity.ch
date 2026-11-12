---
title: "Planowanie i testowanie segmentacji VLAN w homelabie"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Przygotuj plan VLAN, który rozdzieli zaufane urządzenia, serwery, IoT i gości w homelabie. Określ dozwolony ruch, skonfiguruj sieć etapami i przetestuj izolację."
genre: ["Homelab", "Bezpieczeństwo sieci", "Sieci"]
tags: ["VLAN homelab", "segmentacja VLAN", "sieć IoT", "sieć dla gości", "firewall homelab", "routing między VLAN", "802.1Q", "izolacja sieci", "test VLAN", "VLAN pfSense", "port dostępowy", "port trunk", "reguły firewall", "bezpieczeństwo homelab", "plan sieci", "podsieć", "DHCP", "DNS", "zarządzalny switch", "bezprzewodowy SSID"]
cover: "/img/cover/homelab-vlan-segmentation-plan.webp"
coverAlt: "Router i switch homelab rozdzielają laptopy, serwery, urządzenia IoT oraz gości na chronione strefy sieci."
coverCaption: "Zaplanuj granice VLAN, a następnie przetestuj każdą dozwoloną i blokowaną ścieżkę."
---

Homelab często łączy laptopy, serwery, kamery i urządzenia gości w jednej sieci. **Segmentacja VLAN** umieszcza te grupy w oddzielnych sieciach. Router, firewall lub switch warstwy 3 kieruje ruch między nimi. Reguły firewalla lub listy kontroli dostępu switcha zarządzają takim ruchem. Ten poradnik pomaga zapisać plan, wprowadzać po jednej zmianie i sprawdzać wyniki.

## Najważniejsze wnioski

- **Grupuj według poziomu zaufania:** umieść urządzenia administracyjne, serwery, IoT i gości w osobnych sieciach, jeśli mają różne potrzeby dostępu.
- **Zapisz dozwolone ścieżki:** odnotuj źródło, cel, usługę i uzasadnienie każdego połączenia między sieciami.
- **Skonfiguruj obie warstwy:** ustawienia VLAN switcha i punktu dostępowego przypisują urządzenia do sieci. Reguły firewalla lub listy kontroli dostępu switcha sterują routowanym ruchem.
- **Sprawdź oba wyniki:** z każdej istotnej sieci przetestuj jedno połączenie dozwolone i jedno blokowane.

## Zanim zaczniesz

Potrzebujesz routera lub firewalla z interfejsami VLAN albo switcha warstwy 3 obsługującego routing VLAN i listy kontroli dostępu. Zarządzalny switch przenosi przewodowe VLAN-y. Jeśli oddzielasz klientów bezprzewodowych, potrzebujesz również punktu dostępowego z sieciami Wi-Fi powiązanymi z VLAN-ami. Podczas zmiany konfiguracji pozostaw urządzenie w obecnej sieci zarządzającej. Najpierw zapisz ustawienia routera, switcha i punktu dostępowego. Poniższe kroki wykorzystują **przykładowy plan**, więc dostosuj adresy i porty do swojego sprzętu.

**Interfejs VLAN** to połączenie bramy z VLAN-em. Bramą może być router, firewall albo switch warstwy 3. **Zakres DHCP** to pula adresów oferowana urządzeniom w danej sieci przez usługę DHCP. **Przekaźnik DHCP** przekazuje żądania adresu z VLAN-u do serwera DHCP w innej sieci. Użyj przekaźnika, gdy brama nie przydziela adresów dla tego VLAN-u, a serwer DHCP znajduje się gdzie indziej. [Przewodnik Juniper po przekaźniku DHCP](https://www.juniper.net/documentation/us/en/software/junos/dhcp/topics/topic-map/dhcp-relay-agent-security-devices.html) opisuje tę ścieżkę. Bezprzewodowy **SSID** to nazwa sieci, z którą łączą się klienci. Jeśli sprzęt nie ma zarządzalnego switcha ani punktu dostępowego obsługującego VLAN, zacznij od wbudowanej sieci gościnnej i sprawdź jej izolację przed zakupem lub zmianą sprzętu.

Jeśli potrzebujesz najpierw poznać podstawowe terminy, przeczytaj [podsiec i VLAN-y](/articles/networking-basics-what-are-subnets-and-vlans/). [Przewodnik po segmentacji sieci](/articles/how-to-perform-network-segmentation-for-improved-security/) w witrynie omawia szersze zagadnienie bezpieczeństwa. CISA opisuje oddzielne sieci domowe dla gości i urządzeń Internetu rzeczy w [wytycznych bezpieczeństwa dla federalnych mobilnych stanowisk pracy](https://www.cisa.gov/sites/default/files/2024-08/Federal-Mobile-Workplace-Security_508_2024-08-14.pdf).

> **Ostrzeżenie:** zmiana VLAN-u na porcie obsługującym połączenie administracyjne może odciąć ci dostęp. Zachowaj fizyczny dostęp i znaną procedurę odzyskiwania do czasu, aż wszystkie sieci przejdą testy.

Przed przeniesieniem kabla wyeksportuj konfigurację każdego urządzenia i zapisz aktualny adres IP zarządzania, port switcha, ustawienie VLAN i login administratora. Pozostaw jeden działający port administracyjny i laptop w pierwotnej sieci. Jeśli zmiana odetnie dostęp, podłącz laptop ponownie do tego portu, przywróć zapisane ustawienie lub konfigurację i sprawdź, czy stara brama odpowiada, zanim spróbujesz ponownie. Jeśli ścieżka administracyjna switcha jest niedostępna, użyj udokumentowanej konsoli lub lokalnej procedury odzyskiwania. Nie resetuj sprzętu, dopóki nie wiesz, co reset usuwa.

## Inwentaryzacja urządzeń i przepływów

Wypisz każde urządzenie, jego bieżący adres, właściciela i potrzebne usługi. Każdy dostęp do innej sieci powinien mieć uzasadnienie. Laptop może na przykład administrować serwerem, a kamera potrzebować dostępu tylko do rejestratora i serwera DNS. Telefon gościa potrzebuje Internetu, ale nie dostępu do serwerów.

| Grupa urządzeń | Przykładowe urządzenia | Wymagany dostęp |
|---|---|---|
| **Administracja** | Laptop administratora, zarządzanie switchem i punktem dostępowym | Router, switch, punkt dostępowy, administracja serwerami |
| **Serwery** | Hypervisor, NAS, cel kopii zapasowych | Aktualizacje, DNS, zatwierdzony ruch aplikacji |
| **IoT** | Kamery, inteligentne gniazdka, urządzenia multimedialne | DNS, usługa czasu, określony kontroler lub rejestrator |
| **Goście** | Telefony i laptopy odwiedzających | Internet, DNS, brak dostępu do prywatnych podsieci |

Zapisz wyjątki przed dodaniem reguł. Lokalne funkcje wykrywania, takie jak przesyłanie obrazu na ekran, często korzystają z multicastu, który domyślnie nie przechodzi przez granicę routingu. Nie otwieraj całego ruchu między VLAN-ami, by rozwiązać jeden problem z wykrywaniem. Ustal protokół i dodaj najmniejszy obsługiwany wyjątek.

## Przypisywanie VLAN-ów i adresów

Przypisz każdej grupie identyfikator VLAN i osobną podsieć IP. Ten **przykładowy plan** używa adresów zarezerwowanych do dokumentacji i zakłada, że router zapewnia DHCP i DNS. Nie kopiuj tabeli do działającej sieci bez sprawdzenia konfliktów adresów.

| Sieć | ID VLAN | Podsieć | Przykładowa brama |
|---|---:|---|---|
| **Administracja** | 10 | `192.0.2.0/27` | `192.0.2.1` |
| **Serwery** | 20 | `198.51.100.0/27` | `198.51.100.1` |
| **IoT** | 30 | `203.0.113.0/27` | `203.0.113.1` |
| **Goście** | 40 | `192.0.2.32/27` | `192.0.2.33` |

Te zakresy zarezerwowane do dokumentacji służą tylko do zilustrowania układu, zgodnie z [RFC 5737](https://www.rfc-editor.org/info/rfc5737). W laboratorium używaj adresów prywatnych z [RFC 1918](https://www.rfc-editor.org/info/rfc1918), z niepokrywającą się podsiecią dla każdego VLAN-u. W planie zapisz rzeczywistą bramę, pulę DHCP, adres DNS i rezerwację urządzenia.

**Porty dostępowe** przenoszą sieć jednego urządzenia bez znacznika VLAN. **Porty trunk** przenoszą wybrane oznaczone VLAN-y między routerem, switchem i punktem dostępowym. Ustaw ten sam identyfikator VLAN oraz tę samą konfigurację native lub bez tagu po obu stronach. [Przewodnik Netgate po switchach VLAN](https://docs.netgate.com/pfsense/en/latest/recipes/switch-vlan-configuration.html) omawia oznaczone trunki, nieoznaczone porty dostępowe i identyfikatory VLAN portów. Nie używaj domyślnego VLAN 1 do zarządzania, jeśli sprzęt pozwala utworzyć osobny VLAN, jak opisano w [wytycznych bezpieczeństwa VLAN Netgate](https://docs.netgate.com/pfsense/en/latest/vlan/security.html).

Ruch **native** lub **bez tagu** na trunku nie ma znacznika VLAN. Obie strony muszą przypisać go do tego samego VLAN-u, w przeciwnym razie urządzenie może trafić do niewłaściwej sieci. Zezwalaj tylko na VLAN-y potrzebne temu łączu. Wyłącz nieużywane porty switcha lub przypisz je do ograniczonej sieci. Netgate odradza też traktowanie VLAN-u jako pełnej granicy bezpieczeństwa, jeśli napastnik kontroluje port switcha. Chroń fizyczne porty i dane logowania urządzeń, a także routowany ruch.

## Tworzenie macierzy ruchu

Sam VLAN oddziela domeny rozgłoszeniowe. **Routing między VLAN-ami** na routerze lub switchu warstwy 3 nadal wymaga reguł dostępu. Ustal, które urządzenie routuje między VLAN-ami. Jeśli switch warstwy 3 routuje lokalnie, ruch między jego VLAN-ami może w ogóle nie dotrzeć do firewalla routera. Zastosuj równoważne listy kontroli dostępu na switchu albo kieruj ruch przez firewall, a następnie testuj w faktycznym punkcie egzekwowania reguł. Sprawdź kierunek ACL switcha i to, czy śledzi stan połączenia. Wiele ACL-i switchy dopasowuje pakiety osobno w każdym kierunku, więc dozwolone połączenie może wymagać wąskiej reguły dla ruchu powrotnego. [Przewodnik Cisco po ACL](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/security/acls/acls-configuration-guide/access-control-lists.html) opisuje kierunek interfejsu i kolejność dopasowania pakietów. Użyj inwentarza urządzeń, by zapisać planowane połączenia. Poniższe wpisy to przykłady, a nie uniwersalny zestaw reguł.

| Źródło | Cel | Usługa | Decyzja |
|---|---|---|---|
| **Administracja** | Interfejs administracyjny serwera | TCP 443 | Zezwalaj zatwierdzonym urządzeniom administracyjnym |
| **Administracja** | Interfejsy administracyjne routera, switcha i punktu dostępowego | Udokumentowane porty zarządzania tych urządzeń | Zezwalaj zatwierdzonym urządzeniom administracyjnym |
| **IoT** | Rejestrator kamer | Udokumentowany port rejestratora | Zezwalaj tylko w razie potrzeby |
| **IoT** | Zatwierdzony DNS i usługa czasu | DNS i NTP | Zezwalaj tylko do wybranych usług |
| **IoT** | Podsieć administracyjna | Dowolny | Blokuj |
| **Goście** | Prywatne podsieci | Dowolny | Blokuj |
| **Goście** | DNS i Internet | DNS, ruch internetowy | Zezwalaj przez zatwierdzony resolver i bramę |

Uwzględnij w planie także własne usługi routera. Reguła blokująca IoT dostęp do innych VLAN-ów może nadal pozostawiać osiągalny interfejs administracyjny routera. Ogranicz usługi zarządzania do sieci administracyjnej. Zacznij od wymaganych reguł zezwalających i domyślnego blokowania pozostałego routowanego ruchu. Sprawdź istniejące szerokie reguły zezwalające, zanim uznasz, że ustawienie domyślne cokolwiek blokuje. [Najlepsze praktyki firewalla Netgate](https://docs.netgate.com/pfsense/en/latest/firewall/best-practices.html) wskazują, że domyślna sieć LAN pfSense ma regułę zezwalającą. [Metodologia reguł pfSense](https://docs.netgate.com/pfsense/en/latest/firewall/rule-methodology.html) wyjaśnia, że reguły interfejsu filtrują ruch wchodzący przez ten interfejs, a dozwolone połączenia tworzą stan dla ruchu powrotnego.

Przykładowa tabela dotyczy IPv4. Jeśli sieć używa IPv6, przypisz każdemu VLAN-owi prefiks i politykę IPv6, sprawdź ogłoszenia routera i przetestuj dozwolone oraz blokowane ścieżki IPv6. Zablokowanie IPv4 nie dowodzi izolacji IPv6. Jeśli nie planujesz routingu IPv6, sprawdź ustawienia IPv6 routera oraz adresy klientów zamiast zakładać, że IPv6 nie występuje. Netgate opisuje [działanie firewalla IPv6](https://docs.netgate.com/pfsense/en/latest/config/advanced-networking.html) i [ogłoszenia routera](https://docs.netgate.com/pfsense/en/latest/services/dhcp/ipv6-ra.html).

## Konfigurowanie jednej sieci naraz

1. Wybierz bramę dla VLAN-u. Jeśli routuje go router lub firewall, utwórz tam interfejs VLAN i przypisz mu adres bramy. Jeśli robi to switch warstwy 3, utwórz interfejs VLAN na switchu. Skonfiguruj zakres DHCP na bramie albo przekaźnik DHCP do istniejącego serwera. Sprawdź, czy zatwierdzony resolver DNS jest osiągalny. [Przewodnik konfiguracji VLAN Netgate](https://docs.netgate.com/pfsense/en/latest/vlan/configuration.html) wymienia kroki interfejsu i usług dla bramy pfSense.
2. Jeśli router jest bramą VLAN-u, dodaj VLAN do trunku router-switch. Jeśli bramą jest switch warstwy 3, przypisz adres bramy VLAN-u do switcha i routuj do routera lub firewalla przez osobną sieć tranzytową albo routowane łącze uplink. Ustaw na switchu trasę domyślną do routera nadrzędnego. Na routerze dodaj przez switch trasę powrotną dla każdego VLAN-u zarządzanego przez switch. Jeśli te podsieci potrzebują Internetu, sprawdź politykę firewalla routera i wychodzący NAT. Nie konfiguruj tego samego adresu bramy ani zakresu DHCP na obu urządzeniach. [Przewodnik Cisco po routingu między VLAN-ami](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41260-189.html) pokazuje bramy VLAN-ów należące do switcha. Netgate opisuje [trasy powrotne](https://docs.netgate.com/pfsense/en/latest/routing/static.html) i [wychodzący NAT](https://docs.netgate.com/pfsense/en/latest/nat/outbound.html) dla sieci za routerem wewnętrznym. Jeśli klienci bezprzewodowi potrzebują tej sieci, dodaj VLAN do właściwego trunku switch-punkt dostępowy.
3. Przypisz do VLAN-u testowy port dostępowy albo bezprzewodowy SSID. Podłącz do tego portu lub SSID niekrytyczne urządzenie testowe.
4. Dodaj planowane reguły firewalla lub listy kontroli dostępu switcha na urządzeniu routującym VLAN. Sprawdź, czy pozostały ruch routowany jest blokowany. Jeśli switch nie śledzi stanu, sprawdź kierunek ACL i ruch powrotny. Przetestuj dostęp do każdej bramy i interfejsu administracyjnego, każdej lokalnej podsieci oraz IPv6, jeśli jest używane. Zezwalaj wyłącznie na ścieżki z macierzy ruchu. Ogranicz zarządzanie do sieci administracyjnej. Sprawdź kolejność reguł i usuwaj lub zawężaj szerokie reguły zezwalające dopiero wtedy, gdy testowa ścieżka administracyjna działa.
5. Sprawdź, czy urządzenie testowe otrzymuje adres, bramę i serwer DNS z planowanej podsieci. Następnie wykonaj poniższe testy połączeń przed przenoszeniem kolejnych urządzeń.

Nie przenoś ostatniego urządzenia administracyjnego, dopóki jego zastępcza ścieżka nie działa. Zapisz działającą konfigurację po przejściu testów przez każdą sieć. Jeśli DHCP, DNS lub dostęp administracyjny przestanie działać, podłącz urządzenie testowe ponownie do pierwotnego portu lub SSID, przywróć ostatnią zmianę switcha albo routera z zapisanej konfiguracji i ponownie sprawdź pierwotną sieć przed kontynuowaniem.

## Testowanie izolacji i dostępu

Użyj usługi, którą kontrolujesz i o której wiesz, że nasłuchuje na celu. Na testowym urządzeniu Windows zastąp przykładowy adres i port prawdziwym serwerem i uruchom:

```powershell
Test-NetConnection -ComputerName 198.51.100.10 -Port 443
```

Pole **`TcpTestSucceeded`** pokazuje, czy połączenie TCP zostało nawiązane. [Dokumentacja Microsoft dotycząca Test-NetConnection](https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection) opisuje parametry `-ComputerName` i `-Port`. Samo nieudane połączenie nie dowodzi, że reguła firewalla zadziałała. Usługa może być wyłączona albo firewall hosta może odrzucać ruch. Przed wnioskiem sprawdź usługę docelową i dziennik firewalla sieciowego.

Testuj z urządzenia faktycznie połączonego z każdym źródłowym VLAN-em. Przed każdym testem zanotuj adres źródłowy, bramę i serwer DNS. Sprawdź dozwolone połączenie do planowanej usługi, blokowane połączenie do wewnętrznej usługi spoza macierzy, zapytanie DNS przez planowany resolver i dostęp do Internetu, jeśli jest przewidziany. Dla VLAN-u z bramą na switchu sprawdź trasę domyślną switcha, trasę powrotną routera i drogę powrotną od celu, jeśli dozwolone połączenie nie działa. Powtórz dozwolone i blokowane testy z adresami IPv6, jeśli IPv6 jest aktywne. W pfSense **Status > System Logs > Firewall** pokazuje zapisane działania zezwalające i blokujące. [Przewodnik Netgate po dzienniku firewalla](https://docs.netgate.com/pfsense/en/latest/monitoring/logs/firewall.html) opisuje ten widok. Porównaj źródło, cel, port i regułę w dzienniku z testem. Jeśli test niespodziewanie się powiedzie, sprawdź szerokie reguły zezwalające i istniejące wpisy stanu. Po zmianie reguł nawiąż nowe połączenie, ponieważ już istniejące może nadal działać z zapisanym stanem.

Aby sprawdzić DNS w Windows, uruchom `nslookup example.com` i porównaj wyświetlony serwer z planowanym resolverem. Następnie spróbuj wyszukać nazwę z klienta gościnnego lub IoT, dla którego DNS jest ograniczony. Udane wyszukiwanie samo nie dowodzi, że klient użył wybranego resolvera. Sprawdź więc wskazany serwer oraz dziennik firewalla lub resolvera. Osobno przetestuj bezpośredni dostęp z urządzenia IoT lub gościa do adresu administracyjnego routera jako przypadek, który powinien być blokowany.

Urządzenia w **tym samym VLAN-ie** mogą wymieniać ruch bez przechodzenia przez firewall routera. Jeśli punkt dostępowy udostępnia lokalną izolację klientów, sprawdź ją osobno, a na serwerach używaj firewalli hosta. Testy firewalla między VLAN-ami nie dowodzą izolacji w ramach jednego VLAN-u.

> **Oczekiwany wynik:** każde urządzenie otrzymuje adres z planowanej podsieci. Dozwolone usługi działają. Blokowane próby odpowiadają blokadzie firewalla albo równoważnemu udokumentowanemu mechanizmowi.

## Rozwiązywanie problemów

- **Brak adresu:** sprawdź VLAN portu dostępowego lub SSID, tagi trunku, zakres DHCP i interfejs bramy.
- **Adres działa, DNS nie:** sprawdź adres resolvera, powiązanie usługi routera i regułę firewalla dla DNS.
- **Urządzenie nieoczekiwanie dociera do innego VLAN-u:** sprawdź reguły routera, szerokie reguły zezwalające i to, czy urządzenia nadal współdzielą nieoznaczoną sieć.
- **Brak wpisu firewalla dla routowanego ruchu:** sprawdź, czy switch warstwy 3 lub alternatywna brama nie routuje połączenia przed firewallem.
- **VLAN z bramą na switchu dociera do sieci lokalnych, ale nie do Internetu:** sprawdź trasę domyślną switcha, trasy powrotne routera, politykę firewalla i wychodzący NAT dla podsieci VLAN.
- **IPv4 jest blokowane, ale połączenie działa:** sprawdź adresy IPv6, ogłoszenia routera, reguły IPv6 i istniejące wpisy stanu.
- **Blokowany test wygasa bez wpisu firewalla:** potwierdź, że usługa docelowa nasłuchuje. Potem sprawdź routing i ustawienia rejestrowania. [Przewodnik Netgate po rozwiązywaniu problemów z firewallem](https://docs.netgate.com/pfsense/en/latest/troubleshooting/firewall.html) opisuje kontrole logów i stanu.
- **Przesyłanie lub wykrywanie przestaje działać:** ustal protokół wykrywania i ścieżkę do kontrolera, zanim dodasz wąski wyjątek.

## Następne kroki

Przechowuj inwentarz urządzeń i macierz ruchu razem z diagramem sieci. Przeglądaj reguły po dodaniu serwera lub urządzenia IoT. Po każdej istotnej zmianie sieci ponownie wykonaj jeden dozwolony i jeden blokowany test połączenia. Szersze zasady projektowania opisuje artykuł o [segmentacji sieci](/articles/how-to-perform-network-segmentation-for-improved-security/).
