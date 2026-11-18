---
title: "Testuj wycieki DNS i WebRTC w przeglądarce z VPN"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Sprawdź publiczny adres IP, resolver DNS i adresy WebRTC przeglądarki przed połączeniem VPN i po nim. Zinterpretuj wyniki i zbadaj problemy z trasowaniem."
genre: ["Prywatność", "Przeglądarki", "Sieci"]
tags: ["test wycieku DNS", "test wycieku WebRTC", "test wycieku VPN", "test prywatności przeglądarki", "wyciek adresu IP", "DNS przez HTTPS", "bezpieczny DNS", "DNS Firefox", "bezpieczny DNS Chrome", "kandydaci WebRTC", "tunelowanie dzielone VPN", "wyciek IPv6", "test resolvera", "prywatność przeglądarki", "prywatność sieci", "rozwiązywanie problemów VPN", "resolver DNS", "kandydaci ICE", "prywatny adres IP", "mDNS"]
cover: "/img/cover/privacy-browser-leak-test-dns-webrtc.webp"
coverAlt: "Okno przeglądarki z trzema panelami: publiczny IP, DNS i połączenia równorzędne, obok ciągłego tunelu i kropkowanej alternatywnej trasy do zdalnych serwerów."
coverCaption: "Porównaj każdą trasę sieciową przed połączeniem VPN i po nim."
---

Ikona połączenia wirtualnej sieci prywatnej (VPN) nie dowodzi, że każde żądanie przeglądarki przechodzi tą samą trasą. Osobno sprawdź **publiczny adres IP**, **resolver systemu nazw domenowych (DNS)** i **adresy WebRTC**. Każdy wynik odpowiada na inne pytanie. Ten poradnik przedstawia powtarzalny test i sposób badania nieoczekiwanych wyników.

<!--more-->

## Najważniejsze informacje

- **Porównaj dwa stany:** Zapisz te same wyniki przed połączeniem VPN i po nim.
- **Analizuj każdy wynik osobno:** Zmiana publicznego IP nie wskazuje, dokąd trafiły zapytania DNS.
- **Sprawdź kandydatów WebRTC:** Poszukaj publicznego adresu spoza oczekiwanej trasy. Prywatny adres oznacza coś innego.
- **Zmieniaj jedną opcję naraz:** Po każdej zmianie VPN, przeglądarki lub DNS powtórz test.

## Zanim zaczniesz

Użyj przeglądarki i połączenia sieciowego, które chcesz chronić. Ustal, czy VPN ma obejmować całe urządzenie, czy tylko wybrane aplikacje. Jeśli VPN korzysta z tunelowania dzielonego, zapisz, czy testowana przeglądarka jest w tunelu. Przygotuj politykę DNS klienta VPN do porównania.

**Tunelowanie dzielone** kieruje wybrane aplikacje przez VPN, a pozostałe przez zwykłą sieć.

Procedura korzysta ze stron [IP BrowserLeaks](https://browserleaks.com/ip), [DNS](https://browserleaks.com/dns) i [WebRTC](https://browserleaks.com/webrtc). Podczas odwiedzin usługa widzi adres twojego połączenia. Według opisu test DNS prosi przeglądarkę o rozwiązanie 50 losowych nazw. Bez zgody nie uruchamiaj zewnętrznego testu w sieci zarządzanej lub z ograniczeniami. Nie wpisuj poświadczeń, wewnętrznych nazw hostów ani prywatnych danych przeglądania w witrynie testowej.

> **Ostrzeżenie:** Nie umieszczaj dokładnych adresów IP na publicznych zrzutach ekranu ani we wpisach do pomocy technicznej. Zapisz, czy adresy pasują do oczekiwanej trasy dostawcy Internetu lub VPN. Rzeczywiste wartości udostępniaj tylko zatwierdzonym kanałem pomocy.

## Co pokazuje każdy test

| Kontrola | Co porównać | Czego wynik nie dowodzi |
|---|---|---|
| **Publiczny IP** | Adres widziany przez zwykłą witrynę | Który resolver obsłużył DNS |
| **Resolver DNS** | Serwery zaobserwowane podczas nowych zapytań o nazwy | Dokąd każda aplikacja wysyła DNS |
| **WebRTC** | Lokalne i publiczne adresy kandydatów połączenia | Którego kandydata użyje późniejsza rozmowa |

Strona publicznego IP podaje adres użyty w żądaniu internetowym. Strona DNS rozpoczyna nowe zapytania i wskazuje obsługujące je resolvery. WebRTC, czyli Web Real-Time Communication, pozwala aplikacjom przeglądarkowym nawiązywać połączenia równorzędne. Strona WebRTC sprawdza adresy ujawniane podczas tych połączeń. **Kandydat ICE** to możliwy adres sieciowy połączenia równorzędnego. **Wyjście VPN** to publiczny adres używany po opuszczeniu VPN przez ruch. [RFC 8828](https://datatracker.ietf.org/doc/html/rfc8828) wyjaśnia, dlaczego kandydaci WebRTC czasem zawierają adresy niewidoczne w zwykłym żądaniu internetowym, zwłaszcza przy tunelowaniu dzielonym lub proxy.

Serwer DNS dostawcy VPN, inny resolver wybrany w VPN albo szyfrowany resolver wybrany w przeglądarce pokazują różne nazwy. Sama nazwa resolvera nie oznacza wycieku. Porównaj ją z zamierzoną polityką.

## Zapisz stan początkowy

Rozłącz VPN tylko wtedy, gdy sytuacja pozwala na pomiar bez tunelu. Otwórz trzy strony testowe w zwykłym profilu przeglądarki. Uruchom test DNS i poczekaj na wynik. Zapisz poniższe informacje bez publikowania dokładnych adresów:

| Pole | Notatka początkowa |
|---|---|
| **Przeglądarka i wersja** | Nazwa, wersja i istotne rozszerzenia prywatności |
| **Sieć** | Domowa sieć Wi-Fi, hotspot mobilny lub inna zatwierdzona sieć |
| **Publiczne IPv4 i IPv6** | Czy każdy adres należy do zwykłego połączenia |
| **Wynik DNS** | Nazwy lub operatorzy wyświetlonych resolverów |
| **Wynik WebRTC** | Publiczne, prywatne lub `.local` adresy kandydatów |

Jeśli nie możesz rozłączyć VPN, zacznij od oczekiwanej trasy VPN i oznacz pomiar bez tunelu jako niedostępny. Nie wyciągaj wniosków o zwykłym adresie dostawcy na podstawie etykiety lokalizacji ani mapy. Bazy lokalizacji czasem różnią się od rzeczywistego operatora sieci.

## Powtórz test z połączonym VPN

Połącz VPN i potwierdź, że klient zgłasza aktywny tunel. Odśwież każdą stronę testową w **tym samym profilu przeglądarki**. Ponownie uruchom test DNS, aby wygenerować nowe zapytania. Zapisz również wyniki IPv4 i IPv6, jeśli usługa je pokazuje.

Porównuj wyniki w tej kolejności:

1. **Publiczny IP:** Żądanie internetowe powinno pokazywać adres zgodny z wyjściem VPN lub celowo skonfigurowaną trasą. Jeśli przeglądarka ma korzystać z tunelu, zwykły adres dostawcy wskazuje problem z trasowaniem.
2. **DNS:** Porównaj każdy resolver z ustawieniami DNS VPN i przeglądarki. Zbadaj resolver dostawcy Internetu poza oczekiwanym tunelem. Nazwany resolver zewnętrzny jest właściwy, jeśli celowo wybrano go w przeglądarce.
3. **WebRTC:** Porównaj publicznego kandydata WebRTC z wyjściem VPN i początkowym publicznym IP. Jeśli cały ruch przeglądarki ma korzystać z VPN, zwykły adres dostawcy widoczny tylko w WebRTC wymaga sprawdzenia.
4. **Adresy prywatne:** Adres z [prywatnych zakresów RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) albo kandydat `.local` różni się od publicznego IP dostawcy. Zapisz wpis lokalny i zdecyduj, czy witryna powinna go znać.

[Standard obsługi IP WebRTC](https://datatracker.ietf.org/doc/html/rfc8828) opisuje, jak aplikacja poznaje dodatkowe adresy publiczne lub prywatne przez wykrywanie kandydatów ICE. Projekt [kandydatów hosta mDNS w Chromium](https://groups.google.com/a/chromium.org/g/blink-dev/c/z5hSy6Rf_aE/m/aGND030cAgAJ) zastępuje część adresów prywatnych nazwami `.local`. Pusty wynik WebRTC jest **nierozstrzygający**, jeśli JavaScript, API lub serwer testowy nie zadziałał. Pusty wynik nie dowodzi pełnej ochrony.

> **Oczekiwany wynik:** Zwykłe żądanie internetowe przeglądarki i publiczni kandydaci WebRTC korzystają z wybranej trasy. Wyniki DNS odpowiadają zapisanej polityce resolvera VPN lub przeglądarki.

## Zbadaj rozbieżność DNS

Najpierw sprawdź, czy przeglądarka wybiera własny resolver. Ustawienia [DNS over HTTPS w Firefoxie](https://support.mozilla.org/en-US/kb/dns-over-https) pokazują aktywny stan i poziom ochrony. Ochrona domyślna w pewnych sytuacjach wraca do resolvera systemowego i uwzględnia sygnały sieci. Poziomy Zwiększona i Niestandardowa korzystają z wybranego dostawcy i mechanizmu zapasowego. Poziom Maksymalna ostrzega o niepowodzeniu bezpiecznego rozwiązywania nazw. Ważne są stan i lista wyjątków, a nie tylko przełącznik.

[Przewodnik Chrome po bezpiecznym DNS](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) opisuje tryb automatyczny i własnego dostawcę. Gdy bezpieczne zapytanie się nie powiedzie, tryb automatyczny przechodzi do zapytania nieszyfrowanego. Własny dostawca domyślnie nie przechodzi na tryb nieszyfrowany. Ustawienie może być ograniczone na zarządzanych urządzeniach i przez kontrolę rodzicielską. Przed zmianą zarządzanej polityki sprawdź bieżący interfejs przeglądarki.

Jeśli resolver przeglądarki nie jest przyczyną, porównaj ustawienie DNS klienta VPN, listę aplikacji tunelowania dzielonego, resolver systemu operacyjnego i trasę IPv6. Zmień jeden element, a potem powtórz test DNS. Test DNS w przeglądarce mierzy ścieżkę zapytań tej przeglądarki. Nie określa, jak nazwy rozwiązuje inna aplikacja. Jeśli sieć używa [filtrowania DNS](/articles/nextdns-vs-adguard-ad-blocker-comparison/), sprawdź domenę celowo blokowaną i dozwoloną. Brak reklamy nie dowodzi, jak przebiega trasa resolvera.

## Zbadaj rozbieżność WebRTC

Sprawdź, czy przeglądarka nie została wyłączona z tunelu VPN albo nie korzysta z proxy poza oczekiwaną trasą. Popraw trasę i wykonaj test ponownie. Nie wyłączaj IPv6 ani WebRTC w reakcji na pojedynczy niejednoznaczny wynik. [Standard WebRTC](https://datatracker.ietf.org/doc/html/rfc8828) opisuje kompromis między ujawnieniem adresu a wydajnością bezpośrednich rozmów. Ograniczenie kandydatów lub wymuszenie proxy wpływa na połączenia wideo i inne połączenia równorzędne.

Jeśli przeglądarka lub VPN oferuje udokumentowaną kontrolę obsługi IP WebRTC, przeczytaj jej aktualny opis i wybierz ustawienie pasujące do sposobu korzystania z rozmów. Ponownie sprawdź publicznego kandydata. Sam adres lokalny nie dowodzi, że publiczny IP dostawcy opuścił VPN. Ujawniony publiczny IP dostawcy, różny od adresu HTTP VPN, jest mocniejszym sygnałem.

## Prowadź rejestr testów

| Pole | Wynik do zapisania |
|---|---|
| **Data i przeglądarka** | Wersja, profil, rozszerzenia i sieć |
| **Oczekiwana trasa** | VPN dla całego urządzenia, tunel dzielony lub proxy przeglądarki |
| **Przed i po** | Operator publicznego IP, operator DNS i publiczny kandydat WebRTC |
| **Rozbieżność** | Który wynik nie pasował do zamierzonej polityki |
| **Jedna zmiana** | Zmienione ustawienie i powód |
| **Ponowny test** | Nowy wynik i pozostała niepewność |

Powtórz test po zmianach konfiguracji przeglądarki, VPN lub sieci. Dobry wynik dotyczy wyłącznie testowanej przeglądarki, profilu, sieci i chwili. Nie dowodzi anonimowości ani nie obejmuje wszystkich aplikacji. Jeśli nadal wybierasz przeglądarkę, sprawdź funkcje w [porównaniu przeglądarek dbających o prywatność](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/), a następnie wykonaj test w swojej konfiguracji.

## Następne kroki

Powtórz test po zmianie przeglądarki, VPN lub sieci. Przy wyborze przeglądarki skorzystaj z [porównania przeglądarek dbających o prywatność](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/).
