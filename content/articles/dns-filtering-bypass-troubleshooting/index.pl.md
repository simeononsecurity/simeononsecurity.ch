---
title: "Dlaczego filtrowanie DNS jest omijane: sprawdź ścieżkę resolvera"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Sprawdź, dlaczego urządzenie lub przeglądarka omija filtr DNS. Porównaj zapytania bezpośrednie i domyślne, przejrzyj logi oraz ustawienia szyfrowanego DNS, VPN, IPv6 i routera."
genre: ["Sieci domowe", "DNS", "Prywatność"]
tags: ["omijanie filtrowania DNS", "omijanie Pi-hole", "dziennik zapytań DNS", "bezpieczny DNS w przeglądarce", "DNS przez HTTPS", "Android Private DNS", "iCloud Private Relay", "DNS VPN", "DNS IPv6", "DHCP routera DNS", "Resolve-DnsName", "rozwiązywanie problemów DNS", "test filtra DNS", "rozwiązywanie problemów NextDNS", "rozwiązywanie problemów AdGuard DNS"]
cover: "/img/cover/dns-filtering-bypass-troubleshooting.webp"
coverAlt: "Niebieska ścieżka DNS laptopa przechodzi przez filtr i kończy się na symbolu blokady, a pomarańczowa ścieżka przeglądarki dociera do innego resolvera."
coverCaption: "Prześledź ścieżkę zapytania przed zmianą reguły filtra."
---

Skonfigurowano resolver filtrujący, ale jedno urządzenie nadal łączy się z domeną blokowaną przez Twoje zasady. Przyczyną może być reguła, przypisanie Domain Name System (DNS) urządzeniu, szyfrowany resolver przeglądarki albo VPN. **Sprawdź ścieżkę przed zmianą ustawień.** Zapytanie wysłane bezpośrednio do filtra odpowiada na inne pytanie niż zwykłe zapytanie urządzenia.

<!--more-->

## Najważniejsze wnioski

- **Najpierw sprawdź regułę:** Potwierdź, że filtr odbiera i blokuje bezpieczną domenę testową.
- **Prześledź każdą warstwę:** Router, system operacyjny, przeglądarka, VPN i ustawienia mobilne wpływają na trasowanie DNS.
- **Używaj świeżych zapytań:** Dopasuj nową nazwę hosta i czas do dziennika zapytań filtra.
- **Określ ograniczenie:** Jedno zaobserwowane zapytanie potwierdza jedną ścieżkę, a nie działanie każdej aplikacji i urządzenia.

## Zanim zaczniesz

Zarezerwuj około 20 minut. Potrzebujesz dostępu do dziennika zapytań resolvera filtrującego, jednego urządzenia z problemem oraz zapisu ustawień DNS routera. Przykłady używają laptopa z Windows i **Pi-hole**, ale to samo porównanie działa z resolverem udostępniającym dzienniki dla poszczególnych klientów. Najpierw ustal dokładny adres filtra. Nie umieszczaj prywatnych adresów klientów, dzienników zapytań ani reguł zasad w publicznym raporcie.

Wybierz **nieszkodliwą domenę testową**, którą Twoje zasady już blokują. Możesz też tymczasowo dodać dokładną regułę odmowy dla domeny, którą kontrolujesz w profilu testowym. Zapisz regułę i usuń ją po teście. Nie używaj działającej domeny malware jako sondy. Zablokowana strona jest przydatnym objawem, ale dziennik resolvera dostarcza mocniejszych dowodów ścieżki.

| Warstwa | Pytanie |
|---|---|
| **Filtr** | Czy bezpośrednie zapytanie trafia do właściwego resolvera i pasuje do reguły? |
| **Urządzenie** | Które serwery DNS przypisuje sieć? |
| **Przeglądarka lub aplikacja** | Czy ten klient korzysta z resolvera urządzenia czy osobnej ścieżki? |
| **VPN lub relay** | Czy aktywny tunel zmienia miejsce, do którego trafiają zapytania? |

## Sprawdź, czy filtr działa

Otwórz dziennik zapytań resolvera. Wyślij zapytanie o wybraną zablokowaną domenę bezpośrednio do filtra. W systemie Windows użyj PowerShell i po wyświetleniu monitu wpisz adres filtra oraz domenę testową:

```powershell
$filterAddress = Read-Host "Filtering DNS server address"
$testDomain = Read-Host "Harmless domain blocked by your test rule"
Resolve-DnsName -Name $testDomain -Server $filterAddress -Type A -DnsOnly
```

[Dokumentacja polecenia **`Resolve-DnsName`** firmy Microsoft](https://learn.microsoft.com/en-us/powershell/module/dnsclient/resolve-dnsname) określa **`-Server`** jako zapytanie do wskazanego resolvera. Znajdź zapytanie w dzienniku filtra i sprawdź odpowiedź oraz pasującą regułę. [Dokumentacja zapytań i rejestrowania Pi-hole](https://docs.pi-hole.net/main/pihole-command/) opisuje lokalne narzędzia zapytań. Jeśli bezpośrednie zapytanie jest dozwolone, popraw regułę lub przypisanie grupy klienta przed badaniem obejścia. Jeśli zapytanie nie dociera do filtra, sprawdź adres, usługę i ścieżkę sieciową.

**Ten bezpośredni test nie potwierdza, że laptop zwykle korzysta z filtra.** Opcja **`-Server`** nadpisuje domyślny resolver dla tego zapytania. To rozróżnienie zapobiega częstemu fałszywemu pozytywnemu wynikowi.

## Prześledź ścieżkę urządzenia

Użyj nowej nazwy hosta, aby uniknąć poprzedniego wpisu w pamięci podręcznej DNS. Poniższy przykład wysyła jedno zapytanie bezpośrednio do filtra, a drugie przez zwykły wybór resolvera laptopa. Nazwy są różne, więc wiadomo, który wpis dziennika odpowiada danej ścieżce. Odpowiedź **NXDOMAIN** oznacza, że serwer DNS zgłasza nieistniejącą nazwę hosta. To normalne, gdy losowa nazwa nie jest używana. Liczy się obecność zapytania w dzienniku filtra.

```powershell
$stamp = [guid]::NewGuid().ToString("N")
Resolve-DnsName -Name "direct-${stamp}.example.com" -Server $filterAddress -Type A -DnsOnly
Resolve-DnsName -Name "default-${stamp}.example.com" -Type A -DnsOnly
```

Wyszukaj w dzienniku filtra obie dokładne nazwy i zanotuj czas oraz zgłoszonego klienta. Jeśli pojawia się **`direct-`**, ale nie **`default-`**, sprawdź serwery DNS przypisane do laptopa. W Windows polecenie **`Get-DnsClientServerAddress`** wyświetla adresy serwerów DNS według interfejsu. Sprawdź aktywną kartę Wi-Fi lub Ethernet, a nie rozłączony interfejs. [Dokumentacja klienta DNS Microsoft](https://learn.microsoft.com/en-us/powershell/module/dnsclient/get-dnsclientserveraddress) opisuje to polecenie tylko do odczytu.

Podczas pierwszego testu pozostaw widoczne błędy. Błąd lub przekroczenie limitu czasu wymaga osobnej diagnostyki i różni się od braku wpisu w dzienniku zapytań.

```powershell
Get-DnsClientServerAddress | Select-Object InterfaceAlias, AddressFamily, ServerAddresses
```

Porównaj wiersze IPv4 i IPv6. **DHCP** przypisuje ustawienia sieciowe, takie jak serwery DNS. **IPv6** to nowsza rodzina adresów Internet Protocol używająca adresów 128-bitowych. Dzierżawa IPv4 może wskazywać filtr, podczas gdy reklamy routera IPv6 przekazują inny serwer DNS. Sprawdź reklamy **DHCP** i **DNS IPv6** routera, a potem odnów dzierżawę sieciową urządzenia po poprawce. [Przewodnik po instalacji Pi-hole](https://docs.pi-hole.net/main/post-install/) opisuje kierowanie klientów do Pi-hole przez DHCP. [Przykład konfiguracji routera](https://docs.pi-hole.net/routers/fritzbox/) omawia reklamy DNS IPv6.

Jeśli dziennik pokazuje **router** jako klienta, router może przekazywać zapytania w imieniu urządzeń. Dziennik filtra potwierdza wtedy, że router dotarł do filtra, a nie które urządzenie rozpoczęło zapytanie. Zanim uznasz brak tożsamości klienta za brak danych, potwierdź sposób przekazywania zapytań przez router.

## Sprawdź DNS przeglądarki

Zapytanie z wiersza poleceń testuje ścieżkę resolvera urządzenia. Przeglądarka może zamiast tego używać **DNS przez HTTPS (DoH)**. Otwórz tę samą zablokowaną domenę testową w przeglądarce i sprawdź, czy w dzienniku filtra pojawia się odpowiadające jej zapytanie. Wyczyść pamięć podręczną DNS przeglądarki lub użyj nowej nazwy hosta objętej regułą testową, gdy zapisane wyniki utrudniają porównanie.

W **Chrome na komputerze** otwórz **Ustawienia > Prywatność i bezpieczeństwo > Bezpieczeństwo > Używaj bezpiecznego DNS**. Według [pomocy Google Chrome](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) tryb automatyczny korzysta z obecnego dostawcy i po awarii wraca do niezaszyfrowanego wyszukiwania. Wybrany niestandardowy dostawca nie przełącza się w ten sam sposób. Przed zmianą zapisz wybrany tryb i dostawcę.

W **Firefoxie** otwórz **Ustawienia > Prywatność i bezpieczeństwo > DNS przez HTTPS**. [Przewodnik poziomów ochrony Mozilli](https://support.mozilla.org/en-US/kb/dns-over-https) rozróżnia tryby Domyślny, Zwiększony, Maksymalny, Niestandardowy i Wyłączony. [Omówienie DoH](https://support.mozilla.org/en-US/kb/firefox-dns-over-https) wyjaśnia, kiedy resolver przeglądarki omija lokalny filtr DNS. Ponów test po jednej kontrolowanej zmianie, a potem przywróć wybrane ustawienie prywatności.

**Nie uznawaj każdego brakującego zapytania przeglądarki za obejście.** Przeglądarka mogła użyć danych z pamięci podręcznej, połączyć się ze znanym już adresem albo skorzystać z proxy. Zanim ustalisz, dokąd trafiło zapytanie, porównaj nową nazwę, właściwe okno czasowe i ustawienie resolvera przeglądarki.

## Sprawdź ścieżki mobilne i VPN

Na **Androidzie** sprawdź **Ustawienia > Sieć i internet > Prywatny DNS**. Nazwa hosta dostawcy wybiera prywatną usługę DNS inną niż DNS reklamowany przez router. [Ustawienia sieciowe Androida Google](https://support.google.com/android/answer/9654714?hl=en) opisują opcje Wyłączony, Automatyczny i Nazwa hosta dostawcy. Aby uzyskać kontrolowany wynik lokalny, testuj przez Wi-Fi przy wyłączonej transmisji komórkowej, a potem przywróć zwykłe ustawienie.

Na **urządzeniach Apple** sprawdź, czy w sieci działa **iCloud Private Relay** i czy Safari korzysta z oczekiwanej ścieżki. Apple podaje, że [Private Relay chroni ruch Safari i informacje DNS](https://support.apple.com/en-gb/102602). [Ustawienia sieciowe](https://support.apple.com/en-ie/102022) opisują obsługę dla poszczególnych sieci, gdy filtrowanie koliduje z Private Relay. Nie przenoś wyniku Safari na każdą aplikację urządzenia.

**VPN** może udostępniać własny resolver DNS lub wysyłać zapytania przez tunel. Zapisz, czy VPN jest połączony, jego ustawienia DNS i politykę tunelowania dzielonego. Porównaj ten sam test przy włączonym i wyłączonym VPN tylko wtedy, gdy zezwalają na to Twoje zasady bezpieczeństwa. Zmieniony wynik wskazuje różnicę ścieżki. Sam wynik nie dowodzi wycieku ani usterki filtra.

## Interpretacja wyników

| Dowód | Prawdopodobna następna kontrola |
|---|---|
| **Brak bezpośredniego zapytania w dzienniku filtra** | Adres filtra, usługa DNS, rejestrowanie lub osiągalność sieciowa |
| **Bezpośrednie zapytanie dozwolone** | Dokładna reguła odmowy, zasady grupy lub priorytet reguł |
| **Bezpośrednie jest w dzienniku, domyślnego brak** | DHCP, statyczny DNS urządzenia, DNS IPv6 lub resolver VPN |
| **Domyślne jest w dzienniku, przeglądarki brak** | DoH przeglądarki, pamięć podręczna, proxy lub relay |
| **Oba zapytania są w dzienniku i zablokowane, a strona nadal działa** | Inna nazwa hosta, pamięć podręczna, bezpośredni adres lub ścieżka aplikacji |

**Brak wpisów w dzienniku jest niejednoznaczny**, gdy rejestrowanie jest wyłączone, router przekazuje zapytania w imieniu klienta albo test wykorzystał zapisane dane. Powtórz go z nową nazwą hosta i sprawdź czas zapytania przed zmianą reguł zapory. Blokowanie zwykłego DNS do zewnętrznych resolverów nie zmusza szyfrowanej przeglądarki ani VPN do korzystania z filtra. [Przewodnik Pi-hole dla OPNsense](https://docs.pi-hole.net/routers/opnsense/) przedstawia blokowanie zewnętrznego DNS jako opcjonalną kontrolę sieciową. Zasady urządzenia i konfiguracja przeglądarki nadal są osobnymi kontrolami.

## Naprawa i ponowny test

Zmieniaj jedną warstwę naraz. Popraw reklamy DHCP lub DNS IPv6, usuń niezamierzony statyczny resolver, wybierz oczekiwanego dostawcę DNS w przeglądarce albo dostosuj zasady DNS VPN. Nie osłabiaj po cichu szyfrowanego DNS ani ochrony relay na wszystkich urządzeniach, aby rozwiązać jeden nieudany test. Zapisz urządzenie źródłowe, interfejs, adres filtra, zapytaną nazwę, czas, odpowiedź, klienta w dzienniku, tryb przeglądarki, stan VPN i wprowadzoną zmianę.

Po każdej zmianie ponów test **bezpośredni**, **domyślny** i **w przeglądarce**. Za każdym razem użyj nowej nazwy hosta. Jeśli urządzenie ma kilka profili sieciowych, przetestuj każdy osobno. [Porównanie resolverów DNS](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) pomoże wybrać usługę. [Test wycieku przeglądarki](/articles/privacy-browser-leak-test-dns-webrtc/) odpowiada na inne pytanie: jakie informacje sieciowe opuszczają konfigurację przeglądarki i VPN. **Wiarygodny wynik filtra wymaga zweryfikowanej reguły i zweryfikowanej ścieżki klienta.**

## Następne kroki

Powtórz test bezpośredni, domyślny i przeglądarkowy po każdej kontrolowanej zmianie. Przejrzyj [porównanie resolverów DNS](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) podczas wyboru usługi filtrującej.
