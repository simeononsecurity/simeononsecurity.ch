---
title: "Jak działa DNS: główny system DNS, znaczenie i rozwiązywanie problemów"
draft: false
toc: true
date: 2023-07-20
lastmod: 2026-11-13
description: "Poznaj zasady działania DNS i głównego systemu DNS, ich hierarchię, proces rozwiązywania nazw, buforowanie i wskazówki diagnostyczne."
genre: ["Podstawy DNS", "Główny system DNS", "System nazw domenowych", "Rozwiązywanie nazw DNS", "Hierarchia DNS", "Buforowanie DNS", "Diagnostyka DNS", "Rekordy DNS", "Zarządzanie DNS", "Polecenia DNS"]
tags: ["DNS", "Główny system DNS", "System nazw domenowych", "Rozwiązywanie nazw DNS", "Hierarchia DNS", "Buforowanie DNS", "Rekordy DNS", "Zarządzanie DNS", "Diagnostyka DNS", "sieci", "infrastruktura internetowa", "adresy IP", "dostęp do witryn", "zapytanie rekurencyjne", "autorytatywne serwery nazw", "TTL", "mechanizmy buforowania", "czyszczenie pamięci DNS", "serwery główne DNS", "trasowanie anycast", "ICANN", "współpraca DNS", "rekord A", "rekord AAAA", "rekord CNAME", "rekord MX", "rekord TXT", "rekord SRV", "rekord NS", "rekord PTR", "rekord SOA", "polecenia diagnostyczne DNS", "Windows", "macOS", "Linux", "Wiersz polecenia", "terminal systemowy"]
cover: "/img/cover/An_image_depicting_interconnected_computer_ne.webp"
coverAlt: "Ilustracja połączonych sieci komputerowych z nazwami domen i adresami IP, przedstawiająca działanie DNS i głównego systemu DNS."
coverCaption: "Poznaj DNS i opanuj system nazw domenowych"
---

## Jak działają DNS i główny system DNS

### Wprowadzenie

System nazw domenowych (DNS) jest ważną częścią infrastruktury internetu. Umożliwia otwieranie witryn przy użyciu nazw domen zamiast adresów IP. Działa jak książka telefoniczna, która tłumaczy czytelne dla ludzi nazwy domen na adresy IP zrozumiałe dla komputerów. U podstaw DNS leży główny system DNS, hierarchiczny i rozproszony mechanizm rozwiązywania nazw. W tym artykule wyjaśniamy działanie DNS, głównego systemu DNS oraz rekordów przypisanych do domen.

{{< youtube id="mpQZVYPuDGU" >}}

## System nazw domenowych (DNS)

**System nazw domenowych (DNS)** to zdecentralizowany system nazewnictwa, który łączy nazwy domen z adresami IP. Umożliwia otwieranie witryn i innych zasobów internetowych przez wpisanie nazwy domeny w przeglądarce. Dzięki DNS nie musisz zapamiętywać skomplikowanych adresów IP.

### Hierarchia DNS

DNS działa w hierarchicznej strukturze składającej się z kilku poziomów. Na szczycie znajduje się strefa główna, niżej domeny najwyższego poziomu (TLD), domeny drugiego poziomu i subdomeny. Każdy poziom składa się na pełną nazwę domeny. W `www.example.com` „www” jest subdomeną, „example” domeną drugiego poziomu, a „com” domeną TLD.

### Proces rozwiązywania nazw DNS

Gdy wpisujesz nazwę domeny w przeglądarce, rozpoczyna się proces rozwiązywania DNS. Przeglądarka wysyła zapytanie do resolvera DNS, zwykle udostępnianego przez dostawcę internetu (ISP). Resolver wykonuje kolejne kroki, aby ustalić nazwę domeny i znaleźć odpowiadający jej adres IP.

1. **Lokalna pamięć podręczna DNS**: Resolver sprawdza lokalną pamięć podręczną pod kątem żądanej nazwy domeny i adresu IP. Jeśli znajduje dane, od razu zwraca wynik.

2. **Zapytanie rekurencyjne**: Jeśli danych nie ma w pamięci podręcznej, resolver rozpoczyna zapytanie rekurencyjne. Najpierw kontaktuje się z głównymi serwerami DNS, które obsługują strefę „.” (kropkę). Serwery główne zwracają adresy IP serwerów TLD dla żądanej domeny.

3. **Zapytanie do TLD**: Resolver kontaktuje się z serwerami TLD wskazanymi w poprzednim kroku i prosi o adresy IP autorytatywnych serwerów nazw dla domeny.

4. **Zapytanie do autorytatywnego serwera nazw**: Resolver wysyła zapytanie do serwerów nazw otrzymanych od serwerów TLD. Zawierają one autorytatywne rekordy domeny i odpowiadają adresem IP przypisanym do nazwy.

5. **Odpowiedź klientowi**: Resolver odbiera adres IP od autorytatywnych serwerów nazw i zwraca go przeglądarce. Przeglądarka może teraz połączyć się z serwerem WWW pod tym adresem.

### Buforowanie DNS

Resolverzy DNS buforują odpowiedzi, aby przyspieszyć działanie i ograniczyć obciążenie serwerów. Po otrzymaniu odpowiedzi resolver zapisuje lokalnie mapowanie nazwy domeny na adres IP. Kolejne zapytania o tę nazwę mogą otrzymać wynik bez ponownego przechodzenia przez hierarchię DNS.

Buforowanie występuje na wielu poziomach: w lokalnym resolverze, resolverze dostawcy internetu oraz urządzeniach takich jak routery i systemy operacyjne. Wartość Time-to-Live (TTL) w odpowiedzi DNS określa czas przechowywania rekordu. Po wygaśnięciu TTL resolver usuwa rekord i wysyła nowe zapytanie.

#### Czyszczenie lokalnej pamięci DNS

Czyszczenie pamięci podręcznej DNS pomaga rozwiązać niektóre problemy i wymusić pobranie aktualnych rekordów. Oto sposoby dla różnych systemów:

##### Windows

Aby wyczyścić pamięć DNS w systemie Windows:

1. Naciśnij `Win + R`, wpisz `cmd` i naciśnij Enter, aby otworzyć Wiersz polecenia.

2. Wpisz poniższe polecenie i naciśnij Enter:

```bash
ipconfig /flushdns
```

Polecenie czyści pamięć podręczną resolvera DNS w systemie Windows.

##### macOS

Aby wyczyścić pamięć DNS w macOS:

1. Otwórz Terminal z folderu Programy > Narzędzia lub wyszukaj go w Spotlight.

2. Wpisz w Terminalu poniższe polecenie i naciśnij Enter:

```bash
sudo killall -HUP mDNSResponder
```

Polecenie ponownie uruchamia proces mDNSResponder, który odpowiada za rozwiązywanie DNS w macOS.

##### Linux

Sposób czyszczenia pamięci DNS w systemie Linux zależy od dystrybucji i resolvera. Oto dwie popularne metody:

1. **Systemy oparte na systemd (np. Ubuntu, Fedora)**:

Otwórz Terminal i uruchom poniższe polecenie z uprawnieniami administratora:

```bash
sudo systemd-resolve --flush-caches

```

Polecenie czyści pamięć DNS w systemach używających systemd-resolved jako resolvera.

2. **Systemy bez systemd**:

Otwórz Terminal i uruchom poniższe polecenie z uprawnieniami administratora:

```bash
sudo /etc/init.d/nscd restart

```

Polecenie ponownie uruchamia Name Service Cache Daemon (nscd), który buforuje DNS w dystrybucjach bez systemd.

Podane kroki są ogólnymi wskazówkami. Polecenia i metody mogą nieznacznie różnić się zależnie od wersji systemu. Czyszczenie pamięci DNS pomaga przy niektórych problemach, ale nie rozwiązuje każdego problemu z łącznością sieciową.

## Jak działa główny system DNS

Główny system DNS jest podstawowym elementem infrastruktury DNS. Przyjrzyjmy się jego działaniu:

### 1. Strefa główna i serwery główne

Główny system DNS zaczyna się od **strefy głównej**, czyli szczytu hierarchii DNS. Strefa zawiera informacje o autorytatywnych serwerach nazw wszystkich domen najwyższego poziomu (TLD), takich jak .com, .org, .net oraz domen krajowych, takich jak .us i .uk.

System obejmuje 13 głównych serwerów DNS oznaczonych literami od A do M. Są rozmieszczone geograficznie na całym świecie, co zapewnia redundancję i niezawodność.

### 2. Trasowanie anycast

Aby obsłużyć ogromny ruch DNS, serwery główne używają **trasowania anycast**. W tej metodzie wiele serwerów dzieli jeden adres IP, choć znajdują się w różnych miejscach. Warunki sieciowe kierują zapytanie do odpowiedniego serwera, co pozwala wydajnie rozkładać obciążenie.

Gdy użytkownik wysyła zapytanie DNS, infrastruktura sieciowa kieruje je przez anycast do dostępnego serwera głównego o najkrótszej trasie. Anycast rozkłada obciążenie i pomaga uniknąć wąskich gardeł.

### 3. Rekurencyjne resolvery DNS

Po otrzymaniu zapytania o nazwę domeny resolver DNS rozpoczyna rekurencyjny proces rozwiązywania i kontaktuje się z jednym z serwerów głównych.

Serwer główny odpowiada odesłaniem do adresów IP serwerów nazw TLD odpowiedzialnych za żądane TLD. Serwery TLD zawierają informacje o autorytatywnych serwerach nazw domen w tym TLD.

### 4. Odesłania i autorytatywne serwery nazw

Po otrzymaniu odesłania od serwera głównego resolver kontaktuje się z właściwym serwerem nazw TLD.

Serwer TLD zwraca kolejne odesłanie, tym razem z adresami IP autorytatywnych serwerów nazw dla żądanej domeny.

Następnie resolver prosi autorytatywne serwery nazw o adres IP przypisany do domeny.

### 5. Buforowanie i TTL

Podczas rozwiązywania DNS buforowanie zwiększa wydajność i ogranicza obciążenie serwerów. Resolverzy zapisują mapowania nazw domen na adresy IP.

Rekordy DNS są buforowane przez czas określony wartością Time-to-Live (TTL). TTL określa, jak długo rekord pozostaje ważny. Po tym czasie resolver usuwa rekord i wykonuje nowe zapytanie, aby pobrać aktualny adres IP.

### 6. Współpraca i zarządzanie

Głównym systemem DNS wspólnie zarządzają Internet Corporation for Assigned Names and Numbers (ICANN) oraz operatorzy serwerów głównych.

ICANN nadzoruje ogólne zarządzanie i koordynację DNS, współpracując z operatorami serwerów głównych. Wspólnie utrzymują plik strefy głównej, który zawiera informacje o 13 głównych serwerach DNS i ich adresach IP.

operatorzy serwerów głównych dbają o działanie i dostępność serwerów głównych. Wspierają w ten sposób stabilność i odporność całej infrastruktury DNS.

Główny system DNS jest punktem początkowym rozwiązywania nazw. Umożliwia mapowanie nazw domen na adresy IP i sprawne otwieranie witryn oraz innych zasobów internetowych.

#### 13 głównych serwerów DNS

13 głównych serwerów DNS oznaczono literami od A do M. Każdy serwer działa w wielu fizycznych lokalizacjach, co zapewnia redundancję i odporność na awarie. Serwery obsługują zapytania dotyczące strefy głównej, w tym TLD, takie jak .com, .org, .net oraz domeny krajowe, takie jak .us i .uk.

#### ICANN i zarządzanie głównym systemem DNS

Internet Corporation for Assigned Names and Numbers (**ICANN**) odpowiada za zarządzanie i koordynację DNS oraz przydzielanie adresów IP. Współpracuje z operatorzy serwerów głównych, aby zapewnić stabilność i bezpieczeństwo głównego systemu DNS. Razem utrzymują plik strefy głównej z informacjami o 13 serwerach głównych i ich adresach IP.

______

## Rodzaje rekordów DNS i ich przeznaczenie

{{< youtube id="HnUDtycXSNE" >}}

Rekordy DNS to podstawowe elementy systemu nazw domenowych. Zawierają różne informacje związane z nazwą domeny. Poniżej znajdują się popularne typy rekordów i ich zastosowania:

| Typ rekordu | Opis | Przykład |
|-------------|-----------------------------------------------------------------------------|-------------------------------------------|
| A | Mapuje nazwę domeny na adres IPv4. | `example.com     IN A 192.0.2.1` |
| AAAA | Mapuje nazwę domeny na adres IPv6. | `example.com     IN AAAA 2001:db8::1` |
| CNAME | Mapuje alias (nazwę kanoniczną) na rzeczywistą nazwę domeny. | `www.example.com IN CNAME example.com` |
| MX | Wskazuje serwery pocztowe odbierające wiadomości dla domeny. | `example.com     IN MX 10 mail.example.com` |
| TXT | Przechowuje dowolny tekst, często SPF, DKIM lub weryfikację domeny. | `example.com     IN TXT "v=spf1 a mx -all"`|
| NS | Wskazuje autorytatywne serwery nazw domeny. | `example.com     IN NS ns1.example.com` |
| SOA | Określa ogólne właściwości strefy (rekord start of authority). | `example.com     IN SOA ns1.example.com` |
| SRV | Określa lokalizację konkretnej usługi domeny. | `_service._proto.example.com IN SRV 10 20 5060 target.example.com` |
| PTR | Mapuje adres IP na nazwę domeny (odwrotne wyszukiwanie DNS). | `1.2.0.192.in-addr.arpa IN PTR example.com` |

### 1. Rekord A (Rekord adresowy)

**Rekord A** mapuje nazwę domeny na adres IPv4. To najprostszy i najczęściej używany typ rekordu DNS. Gdy wpisujesz nazwę domeny w przeglądarce, rekord A wskazuje adres IP serwera WWW hostującego witrynę.

### 2. Rekord AAAA (Rekord adresowy IPv6)

**Rekord AAAA** pełni tę samą funkcję co rekord A, ale mapuje nazwę domeny na adres IPv6. Wraz z przejściem na IPv6 rekordy AAAA zyskują na znaczeniu dla łączności w sieciach IPv6.

### 3. Rekord CNAME (Rekord nazwy kanonicznej)

**Rekord CNAME** tworzy alias lub nazwę kanoniczną dla domeny. Użyj go, gdy domena lub subdomena ma wskazywać inną domenę albo subdomenę. Na przykład możesz utworzyć rekord CNAME, który kieruje "www" na "mywebsite.com".

### 4. Rekord MX (Rekord wymiany poczty)

**Rekord MX** wskazuje serwer pocztowy odbierający wiadomości dla domeny. Określa, na który serwer należy dostarczać pocztę. Można skonfigurować kilka rekordów MX z priorytetami określającymi kolejność prób, gdy główny serwer jest niedostępny.

### 5. Rekord TXT (Rekord tekstowy)

**Rekord TXT** przechowuje tekst powiązany z domeną. Służy między innymi do weryfikacji domeny, rekordów SPF (Sender Policy Framework) używanych przy uwierzytelnianiu poczty oraz ogólnych informacji.

### 6. Rekord SRV (Rekord usługi)

**Rekord SRV** wskazuje lokalizację konkretnej usługi lub zasobu w domenie. Często służy do lokalizowania usług VoIP, komunikatorów i innych aplikacji.

### 7. Rekord NS (Rekord serwera nazw)

**Rekord NS** wskazuje autorytatywne serwery nazw domeny. To serwery przechowujące jej rekordy DNS. Resolver korzysta z rekordów NS, aby znaleźć autorytatywne serwery dla domeny.

### 8. Rekord PTR (Rekord wskaźnika)

**Rekord PTR** mapuje adres IP na nazwę domeny w odwrotnym wyszukiwaniu DNS. Często służy do sprawdzania tożsamości serwera pocztowego i ograniczania spamu. Odwrotne wyszukiwanie DNS pomaga potwierdzić autentyczność serwera poczty.

### 9. Rekord SOA (Rekord początku autorytetu)

**Rekord SOA** zawiera informacje administracyjne o domenie. Obejmuje między innymi główny autorytatywny serwer nazw, adres e-mail administratora oraz parametry czasowe rekordów DNS.

To tylko kilka spośród wielu typów rekordów DNS. Każdy z nich ma określone zadanie i wspiera dokładne rozwiązywanie nazw domen na powiązane zasoby.

______

## Polecenia diagnostyczne DNS w różnych systemach operacyjnych

Polecenia diagnostyczne pomagają znaleźć przyczynę problemów DNS. Oto często używane polecenia w różnych systemach:

### Windows

#### 1. `ipconfig /flushdns`

To polecenie czyści pamięć DNS w Windows i może pomóc przy nieaktualnych lub błędnych rekordach. Otwórz Wiersz polecenia i uruchom polecenie.

#### 2. `ipconfig /all`

Polecenie `ipconfig /all` wyświetla szczegółowe informacje o interfejsach sieciowych Windows, w tym skonfigurowane serwery DNS. Pozwala sprawdzić, czy system używa właściwych serwerów.

### macOS

#### 1. `sudo killall -HUP mDNSResponder`

Polecenie ponownie uruchamia mDNSResponder w macOS, proces odpowiedzialny za rozwiązywanie DNS. Może odświeżyć ustawienia DNS i pomóc rozwiązać problemy. Otwórz Terminal i uruchom je z uprawnieniami administratora.

#### 2. `nslookup`

Polecenie `nslookup` służy do wyszukiwania rekordów DNS, testowania rozwiązywania nazw i sprawdzania połączenia z serwerami DNS. W Terminalu uruchom `nslookup`, a następnie podaj badaną nazwę domeny lub adres IP.

### Linux

#### 1. `systemd-resolve --flush-caches`

W systemach Linux używających systemd jako resolvera DNS polecenie `systemd-resolve --flush-caches` czyści pamięć DNS. Może pomóc przy problemach spowodowanych nieaktualnymi wpisami. Otwórz Terminal i uruchom je z uprawnieniami administratora.

#### 2. `dig`

Polecenie `dig` to wszechstronne narzędzie diagnostyczne DNS dostępne w systemie Linux. Pokazuje szczegóły zapytań DNS, odpowiedzi i konfiguracji serwerów. Użyj `dig`, aby pytać o konkretne rekordy, testować rozwiązywanie nazw i badać problemy DNS. W Terminalu uruchom `dig`, a następnie podaj domenę lub adres IP.

Te polecenia pomagają diagnozować i rozwiązywać problemy DNS. Pozwalają sprawdzić konfigurację DNS, ustawienia serwerów i problemy z łącznością.

Polecenia i ich opcje mogą zależeć od wersji systemu operacyjnego i dystrybucji. Szczegółowe informacje znajdziesz w dokumentacji używanej wersji systemu.
______


## Podsumowanie

System nazw domenowych (DNS) i główny system DNS odgrywają ważną rolę w działaniu internetu. DNS pozwala otwierać witryny przy użyciu czytelnych nazw domen, a system główny stanowi podstawę całej hierarchii DNS. Zrozumienie ich działania ułatwia korzystanie z sieci i pomaga docenić infrastrukturę obsługującą usługi online.

______

## Źródła

- [DNS w Wikipedii](https://en.wikipedia.org/wiki/Domain_Name_System)
- [Jak działa DNS według Cloudflare](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [Oficjalna witryna ICANN](https://www.icann.org/)
- [operatorzy serwerów głównych](https://www.root-servers.org/)
