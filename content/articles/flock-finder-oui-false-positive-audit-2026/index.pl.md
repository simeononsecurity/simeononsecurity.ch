---
title: "Zmapowaliśmy 146 526 „kamer Flock”. 50 278 z nich to systemy ClickShare"
date: 2026-09-21
lastmod: 2026-11-14
toc: true
draft: false
description: "Audyt Flock Finder wykrywa ClickShare i inne fałszywe alarmy, wyjaśnia dowody i opisuje wprowadzone zmiany."
genre: ["Badania nad bezpieczeństwem", "Technologia prywatności", "Projekty open source", "Dziennikarstwo danych", "Przeciwdziałanie inwigilacji"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "Odcisk OUI", "WiGLE", "Fałszywe alarmy", "Jakość danych", "Barco ClickShare", "Adres MAC", "IEEE OUI", "Odcisk elementów informacyjnych", "ESP32", "Flock-You", "NitekryDPaul", "DeFlockJoplin", "Odpowiedzialność open source", "Mapowanie inwigilacji", "WiFi", "Żądanie sondujące", "Losowanie MAC"]
cover: "/img/cover/flock-finder-oui-false-positive-audit-2026.webp"
coverAlt: "Ciemna mapa miasta pełna czerwonych pinezek, które okazują się biurowymi urządzeniami WiFi, oraz kilku zielonych pinezek oznaczających mocniejsze wykrycia"
coverCaption: "Audyt 146 526 rekordów Flock Finder pokazał, jak użyteczna obserwacja terenowa zmieniła się w zbyt pewne twierdzenie na mapie."
canonical: "https://simeononsecurity.com/articles/flock-finder-oui-false-positive-audit-2026/"
---

**Umieściliśmy 146 526 punktów na mapie kamer monitoringu. Co najmniej 50 278 z nich to systemy prezentacyjne Barco ClickShare. Sprzęt z sal konferencyjnych stanowił ponad jedną trzecią tego, co w nagłówku nazwaliśmy „zmapowanymi kamerami”.**

To był nasz projekt, nasz potok danych i nasz błąd. Flock Finder codziennie odpytuje WiGLE o prefiksy MAC zaobserwowane na kamerach Flock Safety, publikuje wyniki z pełną precyzją współrzędnych i przedstawia je jako równoważne pinezki. W metadanych znajdowało się słowo `suspected`, a dokumentacja wspominała o fałszywych alarmach. Mapa i nagłówek nadal sugerowały pewność.

**Wynik dla czytelnika:** odtwórz audyt, oddziel obserwację od przypisania i pokazuj poziom pewności przy pinezce oraz nagłówku. Zgodność prefiksu jest wskazówką do dalszego badania, a nie dowodem na kamerę.

Gdy wreszcie utworzyliśmy histogram częstości kolumny SSID, zbiór danych ujawnił błąd w kilka minut. ClickShare było tylko największą kategorią. Kolejne 6 099 rekordów miało nazwę `SMARTGATE_*`, 3 801 zaczynało się od ogólnego prefiksu WiFi Direct `DIRECT-`, 314 miało dokładną nazwę `AndroidAP`, 138 wskazywało `Audi HUD`, 133 `MAX-PRINTER`, a 30 zawierało ciąg werdyktu innego detektora. Łącznie **60 793 wiersze, czyli 41,5%, pasowały do znanych reguł nazewnictwa innych urządzeń z pierwotnego audytu.**

Flock Finder publikuje teraz klasę dowodów dla każdego rekordu, domyślnie wyklucza znany inny sprzęt z mapy i nagłówka, udostępnia filtry, oznacza rekordy spoza głównego rynku oraz rozdziela prefiksy o wysokiej pewności od prefiksów producentów kontraktowych. Ten artykuł opisuje błąd, dowody i pozostałe ograniczenia.

______

## Jak działa społecznościowe wykrywanie ALPR

Detektory Flock tworzone przez społeczność zwykle łączą trzy rodzaje dowodów bezprzewodowych:

1. **Prefiksy WiFi MAC/OUI.** Pierwsze bajty globalnie zarządzanego adresu MAC mogą wskazać organizację, której przydzielono blok adresów.
2. **Zachowanie WiFi.** SSID, ogólne żądanie sondujące, adres odbiorcy, wzorzec kanałów lub sekwencja elementów informacyjnych 802.11 mogą zawęzić klasę urządzenia.
3. **Dowody Bluetooth.** Identyfikatory producenta i UUID usług mogą identyfikować radia ujawniane przez produkt albo generację oprogramowania sprzętowego.

Dopasowywanie OUI stało się popularne, bo jest tanie i pasywne. Niedrogi ESP32 może badać pobliskie ramki 802.11 bez łączenia się z siecią. Historyczna baza, taka jak [WiGLE](https://wigle.net/), pozwala też przeszukiwać wcześniejsze obserwacje bez wdrażania własnych skanerów.

Metoda rozwijała się w ramach społeczności: mapowanie i lokalna organizacja [DeFlock](https://deflock.org/), projekt [colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you), forki i projekty towarzyszące, takie jak nasz [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32), a wreszcie [Flock Finder](https://github.com/simeononsecurity/flock-finder), który zastosował listę prefiksów do danych WiGLE w skali globalnej.

Pierwotna praca terenowa zasługuje na wyraźne uznanie. [@NitekryDPaul](https://github.com/NitekryDPaul) zaobserwował 30 prefiksów na prawdziwym sprzęcie Flock w trybie promiscuous. [DeFlockJoplin](https://github.com/DeflockJoplin/flock-you) dodał kolejny podczas testów terenowych. Te obserwacje były prawidłowe. Naszym późniejszym błędem było potraktowanie **„zaobserwowano na kamerze Flock” tak, jakby znaczyło „występuje wyłącznie na kamerach Flock”.**

______

## Błąd strukturalny: OUI opisuje łańcuch dostaw

IEEE opisuje OUI jako 24-bitowy identyfikator przydzielany dostawcy, producentowi lub innej organizacji. W połączeniu z kolejnymi 24 bitami wybranymi przez odbiorcę tworzy adres MAC. Rejestr publikuje [IEEE Registration Authority](https://standards.ieee.org/products-programs/regauth/).

OUI mówi, kto otrzymał blok adresów. Nie musi wskazywać marki gotowego produktu. Producenci kontraktowi budują moduły radiowe dla wielu klientów, więc ten sam dostawca układów może pojawiać się w kamerach, projektorach, drukarkach, pojazdach i płytkach hobbystycznych.

Przydziały w rejestrze powiązane z naszą listą ujawniały ryzyko:

| Rejestrujący | Prefiksy na audytowanej liście |
|---|---|
| Liteon Technology | `74:4C:A1`, `F4:6A:DD`, `9C:2F:9D`, `C0:35:32`, `E4:AA:EA`, `14:5A:FC` i inne |
| Universal Global Scientific Industrial (USI) | `E0:4F:43`, `08:3A:88` |
| Espressif | `A4:CF:12`, `3C:71:BF` |
| Silicon Laboratories | `58:8E:81`, `90:35:EA`, `EC:1B:BD` |
| Flock Safety | `B4:1E:52` |

Wpisy Espressif powinny były nas zaalarmować. Dwa prefiksy z rzekomej listy kamer należały do twórcy jednej z najczęściej używanych platform wbudowanego WiFi na świecie, w tym układów stosowanych przez wiele detektorów społecznościowych.

`B4:1E:52` jest inny, bo został zarejestrowany bezpośrednio na Flock Safety. Dodano go do listy 38 prefiksów w audytowanym commicie, **ale nie został jeszcze odpytany**: `scan_stats.json` podawał 31 odpytanych prefiksów. To samo dotyczyło sześciu nowo dodanych prefiksów pakietów baterii. Migawka nie dowodzi, czy własny prefiks Flock jest częsty czy rzadki. Nie zmienimy „nie odpytano” w „zero wyników”.

Obecne repozytorium zawiera 39 prefiksów po dodaniu `E0:0A:F6` dla zgodności z oprogramowaniem detektora. Zachowane podsumowanie skanowania nadal zawiera dane dla 31 prefiksów. Nowe pozycje czekają więc na pełne ponowne obliczenie, a nie są prefiksami z potwierdzonym zerowym wynikiem.

______

## Zbiór danych skontrolował sam siebie

Wszystkie poniższe historyczne liczby audytu ponownie wygenerowaliśmy z `data/flock_cameras.csv` w commicie Flock Finder [`5551829`](https://github.com/simeononsecurity/flock-finder/tree/5551829), używając modułów `csv` i `collections.Counter` ze standardowej biblioteki Pythona. Nowy przejazd testowy nie był potrzebny. Nazwy, geografia i skład prefiksów już przeczyły nagłówkowi. Dane o poprawionej implementacji pochodzą z zachowanego w bieżącym repozytorium podsumowania `scan_stats.json`.

### Geografia była wczesnym sygnałem ostrzegawczym

Spośród 146 526 wierszy 75 818 dotyczyło Stanów Zjednoczonych, 70 674 było spoza USA, a 34 nie miały kraju. Niemcy miały 13 491 rekordów, następnie Kanada 6 251, Francja 5 839, Wielka Brytania 4 836, Holandia 4 636 i Szwajcaria 4 515.

{{< figure src="flock-finder-us-non-us-split.webp" alt="Wykres skumulowany pokazuje 75 818 rekordów z USA, 70 674 spoza USA i 34 bez wartości kraju" caption="Histogram krajów sumuje się do 146 492, ponieważ 34 wiersze mają pustą wartość kraju." >}}

Geografia jest sygnałem do selekcji, a nie dowodem. Flock opisuje sieć jako „krajową” i mówi o klientach w [49 stanach USA](https://www.flocksafety.com/flock-ecosystem). Ekspansja międzynarodowa może też zmienić granice rynku. Dlatego oznaczamy rekordy spoza rynku do sprawdzenia, zamiast je usuwać albo uznawać wszystkie rekordy spoza USA za fałszywe.

Wystarczy ostrożny wniosek: prawie połowa rekordów leżała poza głównym rynkiem projektu w USA. Bez innego sygnału nie można uznać globalnego dopasowania OUI za równie wiarygodne.

### Ponad 60 000 urządzeń podało własną nazwę

| Rodzina SSID w pierwotnym audycie | Rekordy | Udział | Co wskazuje nazwa |
|---|---:|---:|---|
| Zawiera `ClickShare` | 50 278 | 34,3% | Bezprzewodowy sprzęt prezentacyjny Barco |
| `SMARTGATE_*` | 6 099 | 4,2% | Rodzina bramek lub urządzeń typu OBD |
| `DIRECT-*` | 3 801 | 2,6% | Urządzenia WiFi Direct, np. drukarki, telewizory i adaptery |
| Dokładna nazwa `AndroidAP` | 314 | 0,2% | Hotspoty Androida |
| Dokładna nazwa `Audi HUD` | 138 | 0,1% | WiFi systemu multimedialnego lub wyświetlacza HUD Audi |
| Dokładna nazwa `MAX-PRINTER` | 133 | 0,1% | Drukarki biurowe |
| `Flock ALPR [...]` | 30 | <0,1% | Werdykt innego detektora zapisany jako SSID |
| **Suma pierwotnego audytu** | **60 793** | **41,5%** | Można rozpoznać jako inny sprzęt albo wynik detektora |

Dokumentacja pomocy Barco podaje, że domyślna nazwa sieci jednostki bazowej ClickShare to [`ClickShare-<serial base number>`](https://www.barco.com/en/support/knowledge-base/2675-how-to-connect-to-your-clickshare-base-unit-wifi). To bezpośrednie potwierdzenie rodziny produktu, bez zgadywania na podstawie geografii lub rejestru dostawcy.

Klasyfikator produkcyjny zastąpił dokładne kontrole nazw wyrażeniami regularnymi bez rozróżniania wielkości liter. Obejmuje ClickShare, SmartGate, WiFi Direct, AndroidAP, Audi HUD, MAX-PRINTER i etykiety wyjściowe detektorów. W tych samych 146 526 wierszach wykrywa 629 wariantów AndroidAP, 139 Audi HUD i 134 MAX-PRINTER. Obecne repozytorium raportuje więc **61 110 rekordów `identified_other`**, nieco więcej niż 60 793 z pierwotnego audytu.

### Potwierdzający sygnał wynosił tylko 2,4%

Tylko **3 502 wiersze** miały prawdziwy SSID o wzorcu Flock. Kolejne 24 964 nie miały SSID. Pozostałe wskazywały inny sprzęt albo łączyły OUI z niesklasyfikowaną nazwą.

Potwierdzone 3 502 wiersze zawierały 161 prawdziwych wariantów SSID: 3 342 wystąpienia prostej nazwy `Flock`, 157 unikatowych nazw konfiguracyjnych `Flock-XXXXXX` lub `FLOCK-XXXXXX` oraz trzy inne nazwy ze słowem `flock`. Wcześniejsza liczba 166 wariantów w README obejmowała pięć różnych ciągów adnotacji detektora `Flock ALPR [...]`. Te pięć stanowi dowód działania detektora, nie kamery.

{{< figure src="flock-finder-evidence-class-breakdown.webp" alt="Wykres skumulowany do 100 procent dzieli 146 526 rekordów na 3 502 potwierdzone SSID, 57 267 nazwanych niesklasyfikowanych, 24 964 tylko ukrytych OUI, 60 763 zidentyfikowane jako inne i 30 rekordów sprzężenia zwrotnego detektora" caption="Stary nagłówek sprowadzał pięć zasadniczo różnych klas dowodów do jednej liczby." >}}

### Jakość prefiksów mocno się różniła

Wskaźnik fałszywych alarmów nie był jednolity. Niektóre prefiksy zachowywały przydatny sygnał Flock, inne były zdominowane przez nazwane urządzenia biurowe lub konsumenckie.

{{< figure src="flock-finder-per-oui-composition.webp" alt="Poziome wykresy skumulowane dla 31 prefiksów OUI: SSID Flock zielone, znane inne SSID czerwone, ukryte SSID jasnoszare, niesklasyfikowane rekordy ciemnoszare" caption="Największe prefiksy często zawierały najwięcej znanych innych urządzeń. Dane z migawki audytu obejmującej 146 526 wierszy." >}}

Porównaj dwa prefiksy, które stara mapa oznaczała identycznie:

- `70:C9:4E` miało 495 wierszy: 133 nazwy ze wzorcem Flock i 29 znanych nazw innych urządzeń.
- `74:4C:A1` miało 11 872 wiersze: 211 nazw ze wzorcem Flock i 8 385 znanych nazw innych urządzeń.

{{< figure src="flock-finder-prefix-signal-contrast.webp" alt="Porównanie: prefiks 70 C9 4E ma 26,9% SSID Flock i 5,9% znanych innych, prefiks 74 4C A1 ma 1,8% SSID Flock i 70,6% znanych innych" caption="Jedna etykieta ukrywała przeciwne proporcje sygnału do szumu." >}}

Ten sam wzorzec widać w największych grupach: `F4:6A:DD` miało 8 422 znane nazwy innych urządzeń wobec 327 nazw Flock, `D0:39:57` miało 8 270 wobec 473, a `E0:4F:43` obejmowało 6 238 znanych nazw innych urządzeń wobec 66 nazw Flock. Wielkość prefiksu nie dowodziła jakości.

______

## Pętla sprzężenia zwrotnego ukryta w 30 wierszach

Trzydzieści rekordów z Teksasu miało SSID będące wyraźnie wynikiem innego detektora:

| Etykieta detektora zapisana jako SSID | Pewność podana przez narzędzie | Rekordy |
|---|---:|---:|
| `Flock ALPR [wifi_receiver_oui;low]` | niska | 20 |
| `Flock ALPR [wifi_oui_wildcard_probe;medium]` | średnia | 4 |
| `Flock ALPR [wifi_bssid_oui;low]` | niska | 3 |
| `Flock ALPR [flock_receiver_oui;low]` | niska | 2 |
| `Flock ALPR [wifi_hidden_ssid_oui;low]` | niska | 1 |

Narzędzie, które utworzyło 26 z 30 rekordów, oznaczyło je jako mało pewne. Późniejszy upload do WiGLE zapisał werdykt narzędzia w polu SSID. Nasz potok znalazł słowo `Flock` i mógł potraktować etykietę jako niezależne potwierdzenie.

Trzydzieści wierszy to mało statystycznie. Mechanizm jest jednak istotny: narzędzia współdzielące bazę crowdsourcingową mogą pobierać od siebie wyniki i zamieniać przypuszczenie o niskiej pewności w pozorne potwierdzenie. Poprawka wyklucza cały wzorzec `Flock ALPR [` przed sprawdzeniem potwierdzającego podciągu `flock`.

______

## Gdzie popełniliśmy błąd

Nagłówek README brzmiał **„Kamery na mapie | 146 526”**. Mapa publikowała współrzędne z pełną precyzją i rysowała każdy wynik tym samym rodzajem pinezki. Aktualizacje według harmonogramu GitHub Actions nadawały słabej heurystyce pozór utrzymywanego rejestru.

Dodaliśmy zastrzeżenia. Każdy element miał `match_confidence: "suspected"`. README wspominało ClickShare jako możliwe współistniejące urządzenie, a projekt prowadził osobny zbiór kandydatów odkrytych po SSID. Te zastrzeżenia nie sterowały jednak liczbą, pinezką ani widokiem domyślnym, które widzieli czytelnicy.

W tekście zastrzegaliśmy, a w nagłówku podawaliśmy liczbę. To mapa wysunęła twierdzenie.

Najbardziej możliwy do uniknięcia był fakt, że oprogramowanie [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32) już oddzielało identyfikatory o wysokiej pewności od identyfikatorów producentów kontraktowych i oceniało słabe dowody poniżej progu alarmowego. Pomysł istniał w tej samej organizacji, ale potok mapowania go nie odziedziczył.

Skalę błędu odkryliśmy, tworząc histogram własnej kolumny SSID. Zajęło to kilka minut. Każdego dnia publikowaliśmy 146 526 wierszy dowodów przeczących naszej prezentacji.

______

## Co zmieniliśmy

Poprawka jest wdrożona w modelu danych i interfejsie Flock Finder:

- **Dowód na rekord:** `ssid_confirmed`, `oui_high`, `oui_mfr` lub `identified_other`.
- **Poziomy OUI:** prefiksy rozdzielono na obserwowane w terenie o wysokiej pewności oraz współdzielone poziomy producentów kontraktowych.
- **Wykluczenie znanych innych urządzeń:** ClickShare, SmartGate, WiFi Direct, hotspoty Androida, Audi HUD, MAX-PRINTER i SSID będące wynikiem detektora są domyślnie wykluczone z mapy i nagłówka.
- **Widoczna niepewność:** kolory pinezek, wyskakujące okna, liczniki i filtry pokazują klasę dowodów.
- **Oznaczenie rynku:** rekordy poza głównym rynkiem USA mają `out_of_market: true` i pozostają dostępne do przeglądu.
- **Rozbity nagłówek:** 3 502 potwierdzone przez SSID, 73 691 podejrzanych dopasowań OUI wysokiego poziomu, 8 223 podejrzane dopasowania OUI producentów kontraktowych i 61 110 zidentyfikowanych jako inne.

Poprawiona liczba przydatna w działaniu to **85 416**, w tym nadal 81 914 niepotwierdzonych dopasowań OUI. To uzasadnione zestawienie tego, co przeszło obecne reguły, a nie zweryfikowany wykaz kamer.

`identified_other` jest także klasyfikatorem operacyjnym, a nie wyrocznią. Domyślny SSID ClickShare ma mocne potwierdzenie w dokumentacji źródłowej, natomiast szeroki wzorzec, taki jak `DIRECT-`, opisuje konwencję nazewnictwa WiFi Direct używaną przez wiele klas produktów. Publikacja reguły dopasowania i pola `blocked_reason` pozwala badaczom audytować wykluczenia i zmieniać je, gdy pojawią się lepsze dowody.

### Długoterminowym rozwiązaniem jest odcisk firmware’u

Poziomowanie OUI ogranicza szkody, ale nie czyni wspólnego prefiksu producenta specyficznym dla produktu. Silniejszą drogą jest uporządkowana struktura elementów informacyjnych w żądaniach sondowania 802.11. Wcześniejsze prace dokumentują ten podpis TLV:

```text
2,12,127,221:506f9a16030103,45,191,221:0050f208000000
```

Ta sekwencja opisuje zachowanie konkretnego stosu firmware’u, a nie właściciela bloku MAC. Odcisk żądań sondowania to uznana technika identyfikacji urządzeń. [Opublikowane badania nad odciskami warstwy MAC 802.11](https://doi.org/10.1155/2017/6235484) pokazują, że elementy informacyjne żądań sondowania mogą nadal identyfikować urządzenie, gdy adresy MAC się zmieniają. Opisują też konkretny błąd zgłoszony w [flock-you issue #43](https://github.com/colonelpanichacks/flock-you/issues/43): `Flock Camera net.` pojawia się na kolejnych lokalnie zarządzanych adresach MAC w pasmach 2,4 i 5 GHz.

Podpis nadal wymaga niezależnej walidacji terenowej na różnych urządzeniach i wersjach firmware’u. Błędne przechwycenia wymagają defensywnego parsowania. To jednak właściwy kierunek. Losowanie MAC sprawia, że dopasowywanie wyłącznie po OUI prowadzi do przewidywalnego ślepego zaułka.

______

## Dlaczego to ważne poza jednym repozytorium

Ludzie korzystają z map monitoringu, aby decydować, gdzie jechać, parkować, zgłaszać, prowadzić badania i organizować działania. Błędna pinezka odwraca uwagę. Dziesiątki tysięcy błędnych pinezek mogą podważyć wiarygodność sąsiednich, dokładnych obserwacji.

Występuje też asymetria wiarygodności. Dostawcy lub krytykowi wystarczy jedna możliwa do wykazania błędna pinezka ClickShare, by zakwestionować cały zbiór danych. Dostarczyliśmy ich 50 278. Dziennikarze i organizacje społeczne mogą powtórzyć prosty nagłówek szybciej, niż dotrze późniejsza korekta.

Przejrzystość open source zdobywa zaufanie dzięki metodom możliwym do sprawdzenia i widocznej niepewności. Publikacja surowych danych pomogła ujawnić błąd, ale dostęp do danych nie usprawiedliwiał interfejsu wyolbrzymiającego wnioski. Korekta powinna pojawić się wszędzie tam, gdzie czytelnik widzi twierdzenie: w polu, filtrze, pinezce, legendzie i nagłówku.

### Apel do wszystkich map Flock i ALPR

Inne projekty mapowania Flock i ALPR również powinny audytować swoje zbiory danych. To zaproszenie do porównania metod, a nie zarzut, że każda mapa odziedziczyła nasz błąd.

[WiGLE](https://www.wigle.net/stats/) to najszerszy znany nam publicznie dostępny, globalnie przeszukiwalny zbiór obserwacji WiFi. Ten zasięg sprawił, że Flock Finder był atrakcyjny: jedno API mogło przekształcić listę sygnatur z badań terenowych w mapę świata. Sprawił też, że błąd był wystarczająco duży, by go zmierzyć. Globalna baza zwraca każdy niezwiązany produkt współdzielący przestrzeń adresową dostawcy radiowego, a nie tylko produkt, który uzasadniał zapytanie.

Inne mapy używają odmiennych dowodów. Niektóre opierają się na zdjęciach i obserwacjach wolontariuszy, inne importują znaczniki monitoringu OpenStreetMap, dokumenty publiczne, ujawnienia dostawców lub dane innego projektu społecznościowego. Ich sum nie można bezpośrednio porównywać z wynikami WiGLE, a naszego wskaźnika 2,4% potwierdzeń SSID nie należy przenosić na dane zweryfikowane terenowo. Wspólne ryzyko polega na tym, że klasyfikacja jednego projektu trafia do danych źródłowych drugiego i wygląda potem na niezależne potwierdzenie.

Każda publiczna mapa powinna odpowiadać na krótki audyt:

1. **Co oznacza jedna pinezka?** Sfotografowane urządzenie, dokument rządowy, dopasowanie OUI, zgłoszenie użytkownika czy import z innej mapy?
2. **Ile rekordów ma bezpośrednie dowody dotyczące produktu?** Publikuj liczby według klasy dowodów zamiast jednego łącznego wyniku kamer.
3. **Które źródła są niezależne?** Śledź pochodzenie importów, aby tej samej obserwacji nie liczyć jako kilku potwierdzeń.
4. **Co przeczy klasyfikacji?** Twórz tabele częstotliwości SSID, dostawców, krajów, etykiet współtwórców i innych pól kategorycznych.
5. **Jak pokazujesz niepewność i spory?** Umieszczaj poziom pewności i status korekty przy pinezkach, filtrach, eksportach i nagłówku.
6. **Czy inny badacz może odtworzyć liczbę?** Publikuj zapytanie, migawkę źródłową, reguły klasyfikacji i datę.

Ten audyt nie zmniejsza problemu Flock. Sieć kamer ALPR nadal może rejestrować podróże, wspierać wyszukiwanie między jurysdykcjami i wpływać na osoby, które nigdy nie zgodziły się na gromadzenie danych. Dokładne liczby utrudniają odrzucenie tej krytyki. Jeśli kwestionujemy systemy nadzoru, nasze mapy muszą odróżniać to, co zaobserwowaliśmy, wywnioskowaliśmy i potwierdziliśmy.

Popełniliśmy błąd mimo dobrego rozeznania. Prefiksy pochodziły z legalnych badań terenowych, potok dało się odtworzyć, a zastrzeżenia były prawdziwe. Wniosek i tak wykraczał poza dowody. Dobre intencje i dobre dane wejściowe nie znoszą obowiązku sprawdzania wyników systemu w dużej skali.

______

## Odtwórz audyt

Pobierz commit `5551829` i uruchom poniższe polecenia w katalogu głównym repozytorium. Skrypt korzysta wyłącznie ze standardowej biblioteki Pythona i drukuje sumę, geografię, popularne SSID oraz wybrane rodziny urządzeń nazwanych.

```bash
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder
git checkout 5551829

python3 - <<'PY'
import csv
from collections import Counter

with open("data/flock_cameras.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

ssids = Counter((row["ssid"] or "").strip() for row in rows)
countries = Counter((row["country"] or "").strip() for row in rows)

families = {
    "clickshare": lambda s: "clickshare" in s.lower(),
    "smartgate": lambda s: s.lower().startswith("smartgate_"),
    "direct": lambda s: s.lower().startswith("direct-"),
    "androidap": lambda s: s.lower().startswith("androidap"),
    "detector_output": lambda s: s.lower().startswith("flock alpr ["),
}

print("wiersze", len(rows))
print("USA", countries["US"])
print("poza USA", sum(countries.values()) - countries["US"] - countries[""])
print("brak kraju", countries[""])
print("najpopularniejsze SSID", ssids.most_common(20))
for name, matches in families.items():
    print(name, sum(matches(ssid) for ssid in ssids.elements()))
PY
```

Aby użyć dokładnych danych historycznych, skorzystaj z CSV z tego commita, a nie z aktualnie wygenerowanego zbioru. Po audycie projekt przestał wersjonować duży CSV, GeoJSON i pliki według OUI, ponieważ każde skanowanie przepisywało setki megabajtów i znacznie powiększało repozytorium. Obecnie generowane dane są przywracane i publikowane w ruchomym wydaniu [`data-latest`](https://github.com/simeononsecurity/flock-finder/releases/tag/data-latest), a małe podsumowanie `scan_stats.json` pozostaje w Git. Brak wygenerowanego pliku w bieżącej gałęzi nie oznacza zatem, że usunięto historyczne dowody ani że ich liczba wynosi zero.

______

## Wniosek

**Heurystyka oznaczona w metadanych jako „podejrzana”, ale pokazana na mapie jako pewna pinezka, jest twierdzeniem.** Etykieta musi znajdować się w modelu danych i wizualizacji, nie tylko w dokumentacji.

