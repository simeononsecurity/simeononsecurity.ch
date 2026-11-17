---
title: "Mastering Wireshark: Kompleksowy przewodnik po analizie sieci dla początkujących"
date: 2023-04-07
lastmod: 2026-11-08
toc: true
draft: false
description: "Odkryj, jak skutecznie używać Wireshark do analizy sieci i rozwiązywania problemów dzięki temu szczegółowemu przewodnikowi dla początkujących."
tags: ["Wireshark", "analiza sieci", "rozwiązywanie problemów", "przewodnik dla początkujących", "monitorowanie sieci", "przechwytywanie pakietów", "protokoły sieciowe", "TCP IP", "wizualizacja danych", "bezpieczeństwo sieci", "filtry przechwytujące", "filtry wyświetlacza", "urządzenia sieciowe", "Ethernet", "topologia sieci", "diagnostyka sieci", "administracja siecią", "wydajność sieci", "Samouczek Wireshark", "pakiety danych"]
cover: "/img/cover/A_cartoon_illustration_of_a_detective_with_a_magnifying_glass.webp"
coverAlt: "Kreskówkowa ilustracja detektywa ze szkłem powiększającym analizującego kable sieciowe, podczas gdy logo Wireshark unosi się nad nimi, symbolizując proces rozwiązywania problemów i analizy sieci za pomocą Wireshark."
coverCaption: ""
---

**Przewodnik dla początkujących dotyczący korzystania z Wireshark do analizy sieci i rozwiązywania problemów**

## Wprowadzenie

**Wireshark** to potężny analizator protokołów sieciowych o otwartym kodzie źródłowym, który umożliwia użytkownikom monitorowanie, przechwytywanie i analizowanie ruchu sieciowego. Jest szeroko stosowany przez administratorów sieci, specjalistów ds. bezpieczeństwa i programistów do rozwiązywania problemów, analizy sieci i celów edukacyjnych. W tym artykule omówimy podstawy korzystania z Wireshark do analizy sieci i rozwiązywania problemów, w tym jego instalację, interfejs, podstawowe funkcje i niektóre typowe przypadki użycia.

______

## Instalacja i konfiguracja

Zanim zanurzysz się w świat analizy sieci za pomocą Wireshark, musisz pobrać i zainstalować go na swoim komputerze. Wireshark jest dostępny dla systemów Windows, macOS i Linux. Aby pobrać najnowszą wersję, odwiedź stronę [Wireshark official website](https://www.wireshark.org/#download)

Po pobraniu i zainstalowaniu Wireshark może być konieczne zainstalowanie wymaganych sterowników i skonfigurowanie systemu w celu uzyskania optymalnej wydajności. Plik [official Wireshark documentation](https://www.wireshark.org/docs/wsug_html_chunked/) zawiera szczegółowe instrukcje dla określonych systemów operacyjnych.

______

## Interfejs Wireshark

Po pierwszym otwarciu programu Wireshark zobaczysz przyjazny dla użytkownika interfejs z kilkoma panelami, z których każdy służy do określonego celu.

- Lista interfejsów przechwytywania:** Wyświetla dostępne interfejsy sieciowe na komputerze. Aby rozpocząć przechwytywanie pakietów, wystarczy wybrać interfejs i kliknąć przycisk "Start".
- Lista pakietów:** Wyświetla przechwycone pakiety w porządku chronologicznym. Możesz zastosować filtry, aby wyświetlić określone pakiety w oparciu o swoje wymagania.
- Szczegóły pakietu:** Wyświetla szczegółowe informacje o wybranym pakiecie, w tym stos protokołów i poszczególne pola nagłówka.
- **Packet Bytes:** Wyświetla nieprzetworzone dane (szesnastkowo i ASCII) wybranego pakietu.

______

## Przechwytywanie i filtrowanie pakietów

Aby przechwycić pakiety, wystarczy wybrać żądany interfejs sieciowy i kliknąć przycisk "Start". Wireshark rozpocznie monitorowanie ruchu sieciowego i wyświetli przechwycone pakiety w czasie rzeczywistym.

**Filtrowanie pakietów** jest kluczową funkcją Wireshark, ponieważ pozwala skupić się na określonym ruchu w oparciu o różne parametry, takie jak adresy IP, protokoły lub numery portów. Filtry można stosować za pomocą paska "Filtr" znajdującego się nad panelem listy pakietów. Na przykład, aby filtrować pakiety z określonym adresem IP, można użyć następującej składni: `ip.addr == 192.168.1.1` Odwiedź stronę [Wireshark Display Filters reference](https://www.wireshark.org/docs/man-pages/wireshark-filter.html) aby dowiedzieć się więcej o dostępnych filtrach.

______

## Analiza ruchu sieciowego

Po przechwyceniu i przefiltrowaniu pakietów można rozpocząć analizę ruchu sieciowego. Wireshark zapewnia wiele wbudowanych narzędzi, które pomagają w interpretacji danych:

- **Statystyki:** Oferuje kompleksowy widok różnych statystyk sieciowych, takich jak konwersacje, hierarchia protokołów, punkty końcowe i inne. Dostęp do tych statystyk można uzyskać, przechodząc do menu "Statystyki".
- Wykresy:** Wizualizacja danych sieciowych za pomocą wykresów, które mogą pomóc w identyfikacji wzorców, trendów lub anomalii. Możesz tworzyć wykresy dla różnych metryk, takich jak przepustowość, czas podróży w obie strony lub skalowanie okien, przechodząc do menu "Statystyki" i wybierając "Wykresy IO" lub "Wykresy strumienia TCP".
- **Expert Information:** Zapewnia wgląd w potencjalne problemy związane z przechwyconym ruchem, takie jak retransmisje, zduplikowane pakiety lub zniekształcone pakiety. Dostęp do tej funkcji można uzyskać, klikając "Analyze" na pasku menu i wybierając "Expert Information".

______

## Rozwiązywanie problemów sieciowych

Wireshark jest doskonałym narzędziem do rozwiązywania różnych problemów sieciowych, takich jak opóźnienia, utrata pakietów lub problemy z łącznością. Niektóre typowe techniki rozwiązywania problemów obejmują:

- **Analiza retransmisji TCP:** Nadmierna liczba retransmisji TCP może wskazywać na przeciążenie sieci, utratę pakietów lub inne problemy. Użyj filtra wyświetlania `tcp.analysis.retransmission` aby wyizolować retransmitowane pakiety i przeanalizować ich charakterystykę.
- **Identyfikacja powolnych połączeń sieciowych:** Określenie, czy powolne połączenia sieciowe są spowodowane opóźnieniami sieci, czy opóźnieniami aplikacji, poprzez analizę czasu RTT (round-trip time) między pakietami. Użyj funkcji TCP Stream Graph, aby zwizualizować wartości RTT i zidentyfikować możliwe wąskie gardła.
- **Wykrywanie nieautoryzowanego dostępu:** Monitorowanie ruchu sieciowego pod kątem podejrzanych działań lub prób nieautoryzowanego dostępu poprzez filtrowanie pakietów na podstawie adresów IP, portów lub protokołów.

## Plan przechwytywania dla początkujących

Zacznij od pytania i krótkiego przechwytywania. Przechwytuj ruch na interfejsie, który go przenosi, odtwórz jeden problem, a następnie zatrzymaj przechwytywanie. Zapisz plik pcapng ze znacznikiem czasu. Zrzuty często zawierają dane logowania, dane osobowe, nazwy hostów i adresy wewnętrzne. Przechowuj je jako wrażliwe materiały i udostępniaj wyłącznie upoważnionym osobom.

**Filtr przechwytywania** ogranicza pakiety zapisywane podczas przechwytywania. **Filtr wyświetlania** ukrywa pakiety po przechwyceniu, ale nie usuwa ich z pliku. Składnia filtrów jest inna. Podręcznik Wireshark opisuje oba języki.

| Cel | Filtr wyświetlania | Co sprawdzić |
|---|---|---|
| **Błąd DNS** | `dns` | Nazwę zapytania, kod odpowiedzi, adres serwera i opóźnienie odpowiedzi. |
| **Nawiązanie TCP** | `tcp.flags.syn == 1` | SYN, SYN-ACK i końcowy ACK dla wybranego punktu końcowego. |
| **Retransmisje** | `tcp.analysis.retransmission` | Kierunek, czas i powtarzające się straty na jednej trasie. |
| **Jeden host** | `ip.addr == 192.168.1.20` | Ruch do wybranego hosta lub z niego. |
| **Jedna usługa** | `tcp.port == 443` | Wybrany port TCP, bez zakładania, jaka aplikacja go używa. |

W terminalu polecenie `tshark -i <interface> -f "host 192.168.1.20" -w incident.pcapng` zapisuje plik pcapng z filtrem przechwytywania libpcap. `tshark -r incident.pcapng -Y "dns or tcp.analysis.retransmission"` odczytuje plik z filtrem wyświetlania. Zastąp interfejs, adres i nazwę pliku wartościami z autoryzowanego testu.

Wybierz pakiet i użyj **Analyze > Follow**, aby sprawdzić strumień protokołu. Wireshark obsługuje między innymi TCP, UDP, TLS, HTTP, HTTP/2, QUIC, WebSocket i SIP. Śledzenie strumienia samo w sobie nie odszyfrowuje TLS. [Przewodnik Wireshark po strumieniach](https://www.wireshark.org/docs/wsug_html_chunked/ChAdvFollowStreamSection.html) opisuje zakres i ograniczenia tej funkcji.

Traktuj **Expert Information** jako wskazówkę. Zestaw retransmisję, zduplikowany lub nieprawidłowy pakiet z czasem, punktami końcowymi, licznikami interfejsu i dziennikami aplikacji. Dokumentacja Wireshark określa Expert Information jako punkt wyjścia, a nie dowód awarii.

______

## Przestrzeganie przepisów rządowych

Niektóre przepisy rządowe, takie jak [**General Data Protection Regulation (GDPR)**](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679) oraz [**Health Insurance Portability and Accountability Act (HIPAA)**](https://www.hhs.gov/hipaa/index.html) wymagają od organizacji ochrony poufnych informacji i utrzymania bezpieczeństwa sieci. Wireshark może pomóc w przestrzeganiu tych przepisów poprzez monitorowanie ruchu sieciowego pod kątem nieautoryzowanego dostępu lub wycieku danych.

Należy pamiętać, że korzystanie z Wireshark do przechwytywania i analizowania ruchu sieciowego może również podlegać względom prawnym i etycznym. Przed użyciem Wiresharka do analizy sieci należy zawsze upewnić się, że posiada się odpowiednie uprawnienia i przestrzega zasad swojej organizacji oraz lokalnych przepisów.

______

## Wnioski

Wireshark to potężne i wszechstronne narzędzie do analizy sieci i rozwiązywania problemów. Rozumiejąc jego funkcje i ucząc się, jak z nich skutecznie korzystać, można poprawić bezpieczeństwo sieci organizacji, zoptymalizować wydajność sieci i zachować zgodność z przepisami rządowymi.

______

## Referencje

1. [Wireshark - Go Deep.](https://www.wireshark.org/)
2. [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
3. [General Data Protection Regulation (GDPR)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679)
4. [Health Insurance Portability and Accountability Act (HIPAA)](https://www.hhs.gov/hipaa/index.html)
5. [Podręcznik TShark Wireshark](https://www.wireshark.org/docs/man-pages/tshark.html)
6. [Śledzenie strumieni protokołów w Wireshark](https://www.wireshark.org/docs/wsug_html_chunked/ChAdvFollowStreamSection.html)
7. [Expert Information w Wireshark](https://www.wireshark.org/docs/wsug_html_chunked/ChAdvExpert.html)

Pamiętaj, aby ćwiczyć i eksperymentować z Wiresharkiem na własną rękę, aby lepiej zrozumieć jego możliwości. Im częściej będziesz z niego korzystać, tym bardziej będziesz biegły w identyfikowaniu i rozwiązywaniu problemów z siecią.




