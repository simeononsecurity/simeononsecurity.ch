---
title: "Przewodnik dla początkujących: Korzystanie z wiersza poleceń Linux dla cyberbezpieczeństwa"
date: 2023-03-13
toc: true
draft: false
description: "Dowiedz się, jak korzystać z wiersza poleceń systemu Linux w celu zapewnienia cyberbezpieczeństwa za pomocą podstawowych i zaawansowanych poleceń."
tags: ["Linux", "Wiersz poleceń", "Cyberbezpieczeństwo", "Przewodnik dla początkujących", "Skanowanie sieci", "Testowanie podatności", "Analiza złośliwego oprogramowania", "Uprawnienia", "Ruch sieciowy", "Status procesu", "Statystyki sieciowe", "Wyszukiwanie plików", "Wireshark", "TCPDump", "Nmap", "Linux CLI", "Bezpieczeństwo", "Testy penetracyjne", "Kryminalistyka cyfrowa"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_wearing_a_hoodie.png"
coverAlt: "Kreskówkowa ilustracja przedstawiająca osobę ubraną w bluzę z kapturem, siedzącą przed ekranem komputera z widocznym interfejsem wiersza poleceń systemu Linux i trzymającą szkło powiększające w celu przedstawienia aspektu cyberbezpieczeństwa."
coverCaption: ""
---

**Linux** to wszechstronny i bezpieczny system operacyjny, który jest szeroko stosowany w branży cyberbezpieczeństwa ze względu na swój charakter open-source. Jednak dla początkujących korzystanie z interfejsu wiersza poleceń (CLI) systemu Linux do wykonywania zadań związanych z cyberbezpieczeństwem może być zniechęcające. Niniejszy przewodnik ma na celu zapewnienie początkującym przeglądu podstawowych i zaawansowanych poleceń CLI systemu Linux, które są przydatne do celów cyberbezpieczeństwa.

## Podstawowe polecenia Linux dla cyberbezpieczeństwa

### Drukuj katalog roboczy

Polecenie **pwd** (print working directory) służy do wyświetlania bieżącego katalogu roboczego w CLI. Katalog roboczy to katalog, w którym aktualnie znajduje się użytkownik w systemie plików. Polecenie jest przydatne do poruszania się po systemie plików i zrozumienia swojej lokalizacji w stosunku do innych katalogów. Na przykład, jeśli znajdujesz się w katalogu domowym i chcesz przejść do katalogu dokumentów, możesz użyć następujących poleceń:

```bash
$ pwd
/home/user
$ cd documents
$ pwd
/home/user/documents
```

W powyższym przykładzie pierwsze polecenie drukuje bieżący katalog roboczy, który jest katalogiem domowym. Drugie polecenie zmienia katalog na katalog documents, a trzecie polecenie drukuje bieżący katalog roboczy, który jest teraz katalogiem documents.

### Lista

Polecenie **ls** służy do wylistowania zawartości katalogu w CLI. Polecenie wyświetla nazwy plików i katalogów w bieżącym katalogu roboczym. Polecenie jest przydatne do identyfikacji plików i katalogów w określonej lokalizacji. Na przykład, jeśli chcesz zobaczyć zawartość katalogu documents, możesz użyć następującego polecenia:

```bash
$ ls documents
file1.txt file2.pdf file3.docx
```

W powyższym przykładzie polecenie wyświetla zawartość katalogu documents, który zawiera trzy pliki: plik1.txt, plik2.pdf i plik3.docx. Można również użyć polecenia bez żadnych argumentów, aby wyświetlić zawartość bieżącego katalogu roboczego. Na przykład:

```bash
$ ls
Desktop Documents Downloads Music Pictures Public Templates Videos
```

W powyższym przykładzie polecenie wyświetla zawartość katalogu domowego, który zawiera kilka podkatalogów, takich jak Pulpit, Dokumenty, Pobrane itd.

### Zmień katalog

Polecenie **cd** (change directory) służy do zmiany bieżącego katalogu roboczego w CLI. Polecenie to umożliwia nawigację po systemie plików i dostęp do plików w różnych lokalizacjach. Na przykład, jeśli chcesz zmienić bieżący katalog roboczy na katalog dokumentów, możesz użyć następującego polecenia:

```bash
$ cd documents
```

W powyższym przykładzie polecenie zmienia bieżący katalog roboczy na katalog documents, który znajduje się w bieżącym katalogu roboczym. Można również użyć polecenia ze ścieżką bezwzględną lub względną, aby zmienić katalog roboczy na katalog, który nie znajduje się w bieżącym katalogu roboczym. Na przykład:

```bash
$ cd /usr/local/bin
```

W powyższym przykładzie polecenie zmienia bieżący katalog roboczy na katalog /usr/local/bin, który jest ścieżką bezwzględną. Alternatywnie, można użyć względnej ścieżki do zmiany katalogu roboczego. Na przykład:

```bash
$ cd ../..
```


W powyższym przykładzie polecenie zmienia bieżący katalog roboczy o dwa poziomy wyżej od bieżącego katalogu roboczego. Notacja ".." reprezentuje katalog nadrzędny i można jej użyć do nawigacji w górę drzewa katalogów.


### Concatenate

Polecenie **cat** (concatenate) służy do wyświetlania zawartości pliku w CLI. Polecenie to jest przydatne do przeglądania zawartości plików tekstowych, takich jak pliki dziennika lub pliki konfiguracyjne. Na przykład, jeśli chcesz wyświetlić zawartość pliku o nazwie "plik1.txt", możesz użyć następującego polecenia:

```bash
$ cat file1.txt
```

W powyższym przykładzie polecenie wyświetla zawartość pliku "file1.txt". Polecenia można również użyć do połączenia wielu plików i wyświetlenia ich zawartości w interfejsie CLI. Na przykład:

```bash
$ cat file1.txt file2.txt file3.txt
```


W powyższym przykładzie polecenie wyświetla zawartość trzech plików: plik1.txt, plik2.txt i plik3.txt. Można również użyć polecenia z symbolami wieloznacznymi, aby połączyć wszystkie pliki pasujące do określonego wzorca. Na przykład:

```bash
$ cat *.txt
```

W powyższym przykładzie polecenie wyświetla zawartość wszystkich plików z rozszerzeniem ".txt" w bieżącym katalogu roboczym. Polecenie to jest przydatne do szybkiego przeglądania zawartości wielu plików bez otwierania ich pojedynczo.


### Global Regular Expression Print

Polecenie **grep** (global regular expression print) służy do wyszukiwania określonych ciągów lub wzorców w pliku lub zestawie plików w CLI. Polecenie to jest przydatne do identyfikowania wzorców w plikach dziennika lub wyszukiwania określonych informacji w plikach konfiguracyjnych. Na przykład, jeśli chcesz wyszukać wszystkie wystąpienia słowa "error" w pliku o nazwie "logfile.txt", możesz użyć następującego polecenia:

```bash
$ grep "error" logfile.txt
```

W powyższym przykładzie polecenie wyszukuje wszystkie wystąpienia słowa "error" w pliku "logfile.txt" i wyświetla pasujące wiersze w CLI. Można również użyć polecenia z wyrażeniami regularnymi, aby wyszukać bardziej złożone wzorce. Na przykład, jeśli chcesz wyszukać wszystkie wiersze zawierające słowo zaczynające się na "p" i kończące się na "y", możesz użyć następującego polecenia:

```bash
$ grep "p.*y" logfile.txt
```

W powyższym przykładzie polecenie wyszukuje wszystkie wiersze zawierające słowo zaczynające się na "p" i kończące się na "y" w pliku "logfile.txt". Wyrażenie regularne "p.*y" pasuje do każdego ciągu znaków zaczynającego się od "p" i kończącego się na "y", z dowolną liczbą znaków pomiędzy nimi. Polecenie to jest przydatne do znajdowania wzorców w plikach dziennika, które mogą pomóc w identyfikacji zagrożeń bezpieczeństwa lub problemów z wydajnością.


### Zmień tryb

Polecenie **chmod** (change mode) służy do zmiany uprawnień pliku lub katalogu w CLI. Polecenie to jest niezbędne do zabezpieczenia plików i katalogów oraz kontrolowania, kto ma do nich dostęp. Uprawnienia są reprezentowane przez trzy cyfry, które odpowiadają odpowiednio właścicielowi, grupie i innym. Cyfry są obliczane na podstawie następującego wzoru:

```
4 = read
2 = write
1 = execute
```

Na przykład, jeśli chcesz nadać właścicielowi uprawnienia do odczytu i zapisu, a grupie i innym uprawnienia tylko do odczytu do pliku o nazwie "plik1.txt", możesz użyć następującego polecenia:

```bash
$ chmod 644 file1.txt
```

W powyższym przykładzie polecenie ustawia uprawnienia pliku "plik1.txt" na 644. Pierwsza cyfra (6) reprezentuje uprawnienia dla właściciela, które są do odczytu i zapisu (4 + 2 = 6). Druga cyfra (4) reprezentuje uprawnienia dla grupy, czyli tylko do odczytu. Trzecia cyfra (4) reprezentuje uprawnienia dla innych, które również są tylko do odczytu.

Można również użyć polecenia z literami, aby zmienić uprawnienia. Na przykład, jeśli chcesz nadać właścicielowi i grupie uprawnienia do odczytu i zapisu, a innym brak uprawnień do pliku o nazwie "plik2.txt", możesz użyć następującego polecenia:

```bash
$ chmod ug=rw,o= file2.txt
```

W powyższym przykładzie polecenie ustawia uprawnienia pliku "plik2.txt" na ug=rw,o=, gdzie "ug" oznacza właściciela i grupę, "r" oznacza uprawnienia do odczytu, a "w" oznacza uprawnienia do zapisu. Znak "=" oznacza "ustaw uprawnienia do", a "o=" oznacza "usuń wszystkie uprawnienia dla innych". Polecenie to jest przydatne do kontrolowania dostępu do poufnych plików i katalogów oraz zapobiegania nieautoryzowanemu dostępowi.


## Zaawansowane polecenia Linux dla cyberbezpieczeństwa

### Network Mapper

Polecenie **nmap** to potężne narzędzie do skanowania sieci w interfejsie CLI, które może być używane do identyfikacji hostów i usług w sieci, a także potencjalnych luk w zabezpieczeniach. Polecenie może wykonywać szereg technik skanowania, w tym wykrywanie hostów, skanowanie portów i wykrywanie systemu operacyjnego.

Jednym z najbardziej podstawowych zastosowań nmap jest skanowanie pojedynczego adresu IP lub hosta. Na przykład, aby przeskanować pojedynczy adres IP (192.168.1.1) w poszukiwaniu otwartych portów, można użyć następującego polecenia:

```bash
$ nmap 192.168.1.1
```

Powyższe polecenie uruchomi skanowanie TCP SYN dla docelowego adresu IP i zwróci listę otwartych portów. Dane wyjściowe pokażą otwarte porty wraz z usługą uruchomioną na każdym porcie, stan portu (otwarty/zamknięty), a czasem dodatkowe informacje, takie jak system operacyjny uruchomiony na celu.

Nmap może być również używany do skanowania wielu hostów lub adresów IP jednocześnie. Na przykład, aby przeskanować zakres adresów IP (192.168.1.1-255) w poszukiwaniu otwartych portów, można użyć następującego polecenia:

```bash
$ nmap 192.168.1.1-255
```

Powyższe polecenie przeskanuje wszystkie adresy IP w zakresie i zwróci otwarte porty i usługi dla każdego celu.

Oprócz podstawowego wykrywania hostów i skanowania portów, nmap może również wykonywać bardziej zaawansowane skanowanie, takie jak wykrywanie usług i wersji, wykrywanie systemu operacyjnego i skanowanie luk w zabezpieczeniach. Skanowania te mogą być przydatne do identyfikowania potencjalnych luk w zabezpieczeniach sieci i zabezpieczania jej przed potencjalnymi atakami.

### TCP Packet Dumper

Polecenie **tcpdump** służy do przechwytywania i analizowania ruchu sieciowego w interfejsie CLI, dzięki czemu jest przydatne do rozwiązywania problemów z siecią, analizowania zachowania sieci i identyfikowania potencjalnych zagrożeń bezpieczeństwa. Polecenie przechwytuje pakiety w czasie rzeczywistym i może filtrować pakiety na podstawie różnych kryteriów, takich jak źródłowy lub docelowy adres IP, protokół i port.

Jednym z najbardziej podstawowych zastosowań tcpdump jest przechwytywanie całego ruchu sieciowego na określonym interfejsie. Na przykład, aby przechwycić cały ruch na interfejsie eth0, można użyć następującego polecenia:

```bash
$ sudo tcpdump -i eth0
```

Powyższe polecenie przechwyci wszystkie pakiety na interfejsie eth0 i wyświetli je w czasie rzeczywistym w CLI. Dane wyjściowe pokażą źródłowy i docelowy adres IP, protokół i inne informacje o każdym pakiecie.

Tcpdump może być również używany do filtrowania pakietów na podstawie różnych kryteriów. Na przykład, aby przechwycić wszystkie pakiety wysłane do lub z określonego adresu IP, można użyć następującego polecenia:

```bash
$ sudo tcpdump host 192.168.1.1
```

Powyższe polecenie przechwyci wszystkie pakiety wysłane do lub z adresu IP 192.168.1.1 i wyświetli je w czasie rzeczywistym w CLI. Można również filtrować pakiety na podstawie protokołu (np. TCP, UDP), numeru portu lub innych kryteriów.

Oprócz przechwytywania pakietów w czasie rzeczywistym, tcpdump może być również używany do przechwytywania pakietów do pliku w celu późniejszej analizy. Na przykład, aby przechwycić wszystkie pakiety na interfejsie eth0 i zapisać je w pliku o nazwie "capture.pcap", można użyć następującego polecenia:

```bash
$ sudo tcpdump -i eth0 -w capture.pcap
```

Powyższe polecenie przechwyci wszystkie pakiety na interfejsie eth0 i zapisze je do pliku "capture.pcap" w formacie pcap, który można później przeanalizować za pomocą narzędzi takich jak Wireshark. Polecenie to jest przydatne do analizy zachowania sieci i identyfikacji potencjalnych zagrożeń bezpieczeństwa.

### Status procesu

Polecenie **ps** wyświetla informacje o uruchomionych procesach w systemie Linux w interfejsie CLI, co jest przydatne do identyfikacji podejrzanych procesów, które mogą być uruchomione w systemie i potencjalnie zagrażać jego bezpieczeństwu. Polecenie może wyświetlać szeroki zakres informacji o uruchomionych procesach, w tym ich identyfikator procesu (PID), użytkownika, użycie procesora i pamięci oraz nazwę polecenia.

Jednym z najbardziej podstawowych zastosowań ps jest wyświetlenie listy wszystkich uruchomionych procesów w systemie. Na przykład, aby wyświetlić listę wszystkich procesów uruchomionych w systemie, można użyć następującego polecenia:

```bash
$ ps aux
```

Powyższe polecenie wyświetli listę wszystkich uruchomionych procesów w systemie, wraz z ich PID, użytkownikiem, wykorzystaniem procesora i pamięci oraz nazwą polecenia. Polecenie to jest przydatne do uzyskania ogólnego widoku procesów uruchomionych w systemie i identyfikacji wszelkich podejrzanych procesów, które mogą być uruchomione.

Ps może być również używane do wyświetlania informacji o określonym procesie lub zestawie procesów. Na przykład, aby wyświetlić informacje o procesie z określonym PID (np. PID 1234), można użyć następującego polecenia:

```bash
$ ps -p 1234
```

Powyższe polecenie wyświetli informacje o procesie z PID 1234, w tym o jego użytkowniku, wykorzystaniu procesora i pamięci oraz nazwie polecenia. Można również wyświetlić informacje o zestawie procesów, określając wiele PID.

Oprócz wyświetlania informacji o uruchomionych procesach, ps może być również używany do monitorowania stanu procesów w czasie rzeczywistym. Na przykład, aby monitorować użycie procesora i pamięci przez określony proces (np. PID 1234) w czasie rzeczywistym, można użyć następującego polecenia:

```bash
$ ps -p 1234 -o %cpu,%mem
```

Powyższe polecenie wyświetli użycie procesora i pamięci przez proces z PID 1234 w czasie rzeczywistym, aktualizując dane wyjściowe co sekundę. Polecenie to jest przydatne do monitorowania wydajności krytycznych procesów i identyfikowania potencjalnych wąskich gardeł wydajności.

### Statystyki sieciowe

Polecenie **netstat** wyświetla informacje o aktywnych połączeniach sieciowych w systemie Linux w interfejsie CLI, dzięki czemu jest przydatne do identyfikowania nieautoryzowanych połączeń sieciowych i potencjalnych zagrożeń bezpieczeństwa. Polecenie może wyświetlać szeroki zakres informacji o aktywnych połączeniach sieciowych, w tym adresy lokalne i zdalne, używany protokół (np. TCP, UDP) oraz stan połączenia.

Jednym z najbardziej podstawowych zastosowań netstat jest wyświetlenie listy wszystkich aktywnych połączeń sieciowych w systemie. Na przykład, aby wyświetlić listę wszystkich aktywnych połączeń sieciowych, można użyć następującego polecenia:

```bash
$ netstat -a
```


Powyższe polecenie wyświetli listę wszystkich aktywnych połączeń sieciowych w systemie, wraz z ich lokalnymi i zdalnymi adresami, używanym protokołem i stanem połączenia. Polecenie to jest przydatne do uzyskania ogólnego widoku aktywnych połączeń sieciowych w systemie i identyfikacji wszelkich nieautoryzowanych połączeń.

Netstat może być również używany do wyświetlania informacji o połączeniach sieciowych dla określonego protokołu (np. TCP). Na przykład, aby wyświetlić listę wszystkich aktywnych połączeń TCP w systemie, można użyć następującego polecenia:

```bash
$ netstat -at
```

Powyższe polecenie wyświetli listę wszystkich aktywnych połączeń TCP w systemie, wraz z ich lokalnymi i zdalnymi adresami oraz stanem połączenia.

Oprócz wyświetlania informacji o aktywnych połączeniach sieciowych, netstat może być również używany do wyświetlania statystyk sieciowych dla określonego protokołu (np. TCP). Na przykład, aby wyświetlić statystyki dotyczące wszystkich połączeń TCP w systemie, można użyć następującego polecenia:

```bash
$ netstat -st
```

Powyższe polecenie wyświetli statystyki dotyczące wszystkich połączeń TCP w systemie, w tym liczbę aktywnych połączeń, liczbę połączeń w każdym stanie oraz liczbę błędów, które wystąpiły. Polecenie to jest przydatne do monitorowania ogólnej kondycji sieci i identyfikowania potencjalnych problemów z wydajnością.


### Znajdź pliki

Polecenie **find** służy do wyszukiwania plików i katalogów w systemie Linux w interfejsie CLI, dzięki czemu jest przydatne do lokalizowania określonych plików i katalogów, które mogą być ukryte lub trudne do znalezienia. Polecenie wyszukuje pliki i katalogi na podstawie szerokiego zakresu kryteriów, w tym ich nazwy, rozmiaru, czasu modyfikacji i uprawnień.

Jednym z najbardziej podstawowych zastosowań polecenia find jest wyszukiwanie plików i katalogów według nazwy. Na przykład, aby wyszukać wszystkie pliki w bieżącym katalogu i jego podkatalogach, które mają nazwę "example.txt", można użyć następującego polecenia:

```bash
$ find . -name example.txt
```

Powyższe polecenie wyszuka wszystkie pliki w bieżącym katalogu i jego podkatalogach, które mają nazwę "example.txt" i wyświetli ich pełną ścieżkę.

Find może być również używany do wyszukiwania plików i katalogów na podstawie ich rozmiaru. Na przykład, aby wyszukać wszystkie pliki w bieżącym katalogu i jego podkatalogach, które są większe niż 1 MB, można użyć następującego polecenia:

```bash
$ find . -size +1M
```

Powyższe polecenie wyszuka wszystkie pliki w bieżącym katalogu i jego podkatalogach, które są większe niż 1 MB i wyświetli ich pełną ścieżkę.

Oprócz wyszukiwania plików i katalogów według nazwy i rozmiaru, find może być również używany do wyszukiwania plików i katalogów na podstawie ich czasu modyfikacji i uprawnień. Na przykład, aby wyszukać wszystkie pliki w bieżącym katalogu i jego podkatalogach, które zostały zmodyfikowane w ciągu ostatnich 7 dni, można użyć następującego polecenia:

```bash
$ find . -mtime -7
```

Powyższe polecenie wyszuka wszystkie pliki w bieżącym katalogu i jego podkatalogach, które zostały zmodyfikowane w ciągu ostatnich 7 dni i wyświetli ich pełną ścieżkę.

Ogólnie rzecz biorąc, polecenie find jest potężnym narzędziem do wyszukiwania plików i katalogów w systemie Linux w oparciu o szeroki zakres kryteriów, dzięki czemu jest przydatne do różnych zadań, w tym administracji systemem i cyberbezpieczeństwa.

______

Korzystanie z wiersza poleceń systemu Linux do celów cyberbezpieczeństwa może być przytłaczające dla początkujących. Jednak dzięki podstawowym i zaawansowanym poleceniom opisanym w tym przewodniku możesz zacząć wykorzystywać Linux CLI na swoją korzyść w cyberbezpieczeństwie. Pamiętaj, aby zachować ostrożność podczas uruchamiania poleceń i dokładnie zrozumieć, co robi każde polecenie przed jego użyciem.

Aby dowiedzieć się więcej o używaniu Linuksa do cyberbezpieczeństwa, pobierz **[Kali Linux](https://www.kali.org/downloads/) system operacyjny, który został zaprojektowany specjalnie do testów penetracyjnych i kryminalistyki cyfrowej.

## Wnioski

Podsumowując, interfejs wiersza poleceń systemu Linux jest potężnym narzędziem dla specjalistów ds. cyberbezpieczeństwa, ale może być zniechęcający dla początkujących. Ucząc się podstawowych i zaawansowanych poleceń opisanych w tym przewodniku, możesz zacząć używać Linux CLI na swoją korzyść w cyberbezpieczeństwie. Pamiętaj, aby zawsze zachować ostrożność podczas uruchamiania poleceń i dokładnie zrozumieć, co robi każde polecenie przed jego użyciem. Dzięki praktyce i doświadczeniu możesz stać się biegły w korzystaniu z wiersza poleceń systemu Linux i przenieść swoje umiejętności w zakresie cyberbezpieczeństwa na wyższy poziom.