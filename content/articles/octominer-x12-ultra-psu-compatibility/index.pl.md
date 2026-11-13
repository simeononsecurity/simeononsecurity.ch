---
title: "Zgodność zasilaczy Octominer X12 Ultra: test Chicony i LiteOn w praktyce"
date: 2026-11-12
lastmod: 2026-11-12
toc: true
draft: false
description: "Test Octominer X12 Ultra z pięcioma wentylatorami i trzema zasilaczami wykazał, że Chicony uruchomił urządzenie, a testowane LiteOn sygnalizowały bursztynowym światłem i nie uruchomiły systemu."
genre: ["Sprzęt do kopania kryptowalut", "Sprzęt komputerowy"]
tags: ["Octominer X12 Ultra", "zasilacz serwerowy", "zgodność zasilaczy", "Chicony R12-1K6P2A", "LiteOn PS-2142-2L"]
cover: "/img/cover/octominer-x12-ultra-psu-compatibility.webp"
coverAlt: "Abstrakcyjna ilustracja trzech zasilaczy serwerowych w obudowie z zielonymi, bursztynowymi i szarymi kontrolkami"
coverCaption: ""
---

**Chicony R12-1K6P2A uruchomił mój Octominer X12 Ultra z pięcioma wentylatorami i trzema zasilaczami.** Testowane przeze mnie zasilacze LiteOn PS-2142-2L pokazywały zielone światło, zmieniały je na bursztynowe i nie uruchamiały urządzenia. Wynik dotyczy mojego egzemplarza z płytą zasilania **OCTOMINER (12PIN) 3x DPS1200 rev. 20**. Taka sama moc znamionowa ani lista dla osobnej płyty breakout X12 nie potwierdza zgodności z płytą Octominer.

Obudowę sprzedawano w **konfiguracji 3 600 W** z trzema zatokami zasilaczy. [Octominer wymienia opcję z trzema zasilaczami po 1 200 W](https://octominer.eu/product/octominer-x12-ultra-used/) dla X12 Ultra, obok innych konfiguracji. Przed odniesieniem tych wyników do własnego urządzenia sprawdź jego etykietę i płytę zasilania.

## Wyniki testów

| Zasilacz | Wynik w tym urządzeniu |
|---|---|
| **Chicony R12-1K6P2A, 1 600 W** | Uruchomił urządzenie podczas mojego testu. W artykule nie mierzono pracy przy długotrwałym obciążeniu ani działania we wszystkich zatokach. |
| **LiteOn PS-2142-2L, 1 400 W** | Testowane egzemplarze świeciły na zielono, potem na bursztynowo, a urządzenie nie uruchomiło się. |
| **Dell/Delta D1200E-S0, Dell 0F37X3** | Nietypowe wejście AC utrudniało znalezienie pasującego przewodu. W tym teście nie zarejestrowałem wyniku rozruchu ani obciążenia tego zasilacza. |
| **HP HSTNS-PD30, 1 200 W** | Testowany w tym samym urządzeniu. Nie uruchomił systemu. |
| **Inne zasilacze HP Common Slot** | Testowane zestawy Platinum Plus 1 200 W oraz zasilacze 750 W HSTNS-PD22B, HSTNS-PL22B i HSTNS-PD18 nie uruchomiły tego urządzenia. Dokładnych numerów modeli zasilaczy z zestawów nie zapisano. |

**Nie traktuj wyniku LiteOn jako diagnozy usterki wszystkich zasilaczy PS-2142-2L.** Zaobserwowana sekwencja oznacza nieudany rozruch w tej obudowie. Test nie wyodrębnił sygnału włączania, wymiany telemetrii, pinoutu płyty ani usterki konkretnego zasilacza. Wynik Chicony potwierdza udany rozruch, ale nie certyfikowaną moc obudowy 4 800 W ani długoterminową niezawodność.

## Który Chicony uruchomił urządzenie?

Zadziałał model **Chicony R12-1K6P2A**, wymieniony również jako część **R1K6A002L** w [tabeli zgodności Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). Jego [raport testowy 80 PLUS](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/chicony-power-r121k6p2a-5866.pdf) identyfikuje zasilacz 1 600 W przeznaczony do **200–240 V AC**, 10 A i 50–60 Hz. Raport zmierzył sprawność 94,19% przy połowie obciążenia w warunkach testowych 230 V. Te wartości dotyczą testowanego zasilacza, a nie całej koparki.

Zakres **200–240 V ma znaczenie**. Nie zakładaj, że ten model zapewnia moc znamionową z gniazda 120 V. Według [oferty części serwerowych dla dokładnego modelu](https://www.itcreations.com/product/142080) testowany zasilacz ma standardowe wejście C14. Używaj przewodów i urządzeń dystrybucyjnych przystosowanych do napięcia i prądu wejściowego.

Mój test potwierdził udany rozruch Chicony z tą konkretną płytą. Nie dowodzi zgodności ze wszystkimi wersjami X12 Ultra. Przed zamówieniem kolejnych sztuk sprawdź pełny numer modelu i etykietę zasilacza.

## Dlaczego lista LiteOn wprowadziła mnie w błąd

**LiteOn PS-2142-2L** znajduje się w [tabeli zgodności płyt breakout X12 firmy Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). Jego [raport 80 PLUS](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/liteon-technology-corporation-ps21422l-6889.pdf) podaje model 1 400 W. Źródła potwierdzają model i jego wymienione zastosowanie z **adapterem X12 Parallel Miner**. Żadne nie testuje oryginalnej płyty zasilania Octominer.

Moje zasilacze PS-2142-2L zmieniały kolor z **zielonego na bursztynowy** po włożeniu, a urządzenie nie uruchamiało się. Podobny kształt styków wyjściowych nie potwierdza takiego samego działania podczas rozruchu, sygnalizacji stanu ani komunikacji. Sama sekwencja LED nie wskazuje, która różnica spowodowała nieudany rozruch.

Ta sama [tabela Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/) grupuje **Dell/Delta D1200E-S0**, **LiteOn PS-2142-2L** i **Chicony R12-1K6P2A** w rodzinie adapterów ośmiopinowych. **HP HSTNS-PD30** oraz kilka zasilaczy HP Common Slot 750 W umieszcza w innej rodzinie adapterów sześciopinowych. Żaden z testowanych przeze mnie zasilaczy HP nie uruchomił urządzenia. Tabela opisuje płyty Parallel Miner, a nie listę zamienników dla płyty **OCTOMINER (12PIN)**.

## Sprawdź zasilanie i okablowanie

[Instrukcja rozwiązywania problemów Octominer X12 Ultra](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) podaje, że sama obudowa pobiera do **200 W przy pełnej prędkości wentylatorów**. Zaleca co najmniej **10% zapasu mocy** i odradza przekraczanie **90% mocy znamionowej zainstalowanych zasilaczy**. Uwzględnij pobór GPU, obudowy i rzeczywistą moc wyjściową zasilaczy przy danym napięciu AC.

**Etykieta 1 600 W na każdym zasilaczu Chicony nie podnosi opublikowanej konfiguracji obudowy 3 600 W do 4 800 W.** System ograniczają również płyta zasilania, wewnętrzne przewody, złącza, dystrybucja AC i chłodzenie. Nie mierzyłem tych ograniczeń w tym egzemplarzu. Utrzymuj urządzenie w udokumentowanej konfiguracji, dopóki Octominer nie potwierdzi wyższej mocy dla dokładnej rewizji płyty.

Dell/Delta **D1200E-S0 / 0F37X3** miał inny problem: wejście AC po stronie zasilacza wymagało mniej popularnego przewodu. Wcześniej, na podstawie urządzenia i ofert przewodów, określiłem wejście jako **LS-25**, a złącze przewodu jako **LS-26**. Przed zakupem sprawdź kształt złącza i oznaczenia elektryczne. Podobnie wyglądająca wtyczka C13 nie zastąpi właściwego złącza.

## Sprawdź własny X12

1. **Zapisz dokładny sprzęt.** Zrób zdjęcia etykiety obudowy i zasilacza, wejścia AC, styków wyjściowych oraz rewizji płyty zasilania. Policz wentylatory i zatoki.
2. **Sprawdź zasilanie AC.** Porównaj parametry wejścia zasilacza z parametrami gniazda, przewodu i PDU. Raport Chicony R12-1K6P2A podaje 200–240 V AC.
3. **Przetestuj minimalną konfigurację.** Wyłącz urządzenie i odłącz wszystkie przewody AC przed wymianą zasilacza, GPU lub połączenia PSON. [Instrukcja Octominer](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) zaleca sprawdzenie osadzenia i diod zasilacza, sześciopinowego przewodu PSON między płytą główną a płytą zasilania oraz użycie jednego zasilacza z jedną GPU, aby odizolować problem rozruchu.
4. **Zapisz przebieg.** Zanotuj model zasilacza, zatokę, sekwencję LED, uruchomienie płyty i wentylatorów oraz rozruch urządzenia. Testuj inne zatoki dopiero po bezpiecznym wyłączeniu.
5. **Wykonaj pomiary przed zwiększeniem obciążenia.** Sprawdź telemetrię zasilacza i pobór z gniazda przy planowanym obciążeniu GPU. Rozruch opisany w tym artykule nie zastępuje testu obciążeniowego.

## Wniosek

**Chicony R12-1K6P2A to jedyny zamiennik w tym porównaniu z odnotowanym udanym rozruchem w moim trzyzatokowym X12 Ultra.** Testowane LiteOn PS-2142-2L zmieniały kolor z zielonego na bursztynowy i nie uruchamiały systemu. Testowane zasilacze HP Common Slot również go nie uruchomiły. Traktuj inne listy zasilaczy jako wskazówki do sprawdzenia, dopóki dokładny model i płyta Octominer nie przejdą kontrolowanego testu rozruchu oraz obciążenia. Zacznij od oznaczeń modelu i rewizji płyty. Przed zwiększeniem obciążenia GPU sprawdź zalecenia Octominer dotyczące zasilania.
