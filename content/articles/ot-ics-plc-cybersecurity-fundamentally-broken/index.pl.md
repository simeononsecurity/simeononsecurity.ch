---
title: "Dlaczego cyberbezpieczeństwo OT, ICS i PLC nadal nie działa"
draft: false
toc: true
date: 2026-06-26
lastmod: 2026-11-22
description: "Sprawdź, dlaczego zabezpieczenia OT nie nadążają za starszą architekturą, ograniczeniami operacyjnymi i rzeczywistymi ścieżkami ataku."
tags: ["bezpieczeństwo OT", "bezpieczeństwo ICS", "bezpieczeństwo PLC", "bezpieczeństwo IoT", "cyberbezpieczeństwo przemysłowe", "bezpieczeństwo SCADA", "NIST 800-82", "IEC 62443", "NERC CIP", "technologia operacyjna", "infrastruktura krytyczna", "czujniki analogowe", "izolacja sieci", "starsze systemy", "opinia o cyberbezpieczeństwie", "przemysłowe systemy sterowania", "SCADA", "Stuxnet", "bezpieczeństwo systemów sterowania", "bezpieczeństwo cyberfizyczne", "bezpieczeństwo łańcucha dostaw", "łańcuch dostaw OT"]
cover: "/img/cover/ot-ics-plc-cybersecurity-fundamentally-broken.webp"
coverAlt: "Ilustracja zestawia stary sterownik PLC z funkcjami analogowymi z nowoczesnym, cyberbezpiecznym sterownikiem z interfejsami cyfrowymi na ciemnym tle."
coverCaption: ""
---

Spędziłem wystarczająco dużo czasu w środowiskach przemysłowych, by powiedzieć wprost: **większość programów cyberbezpieczeństwa OT, ICS i PLC to teatr**. Tworzą dokumentację zgodności. Nie zapewniają bezpieczeństwa. Infrastruktura krytyczna pada ofiarą ataków właśnie w luce między tymi pojęciami.

To nie jest atak na osoby opracowujące standardy. **NIST SP 800-82 Rev 3**, **IEC 62443** i **NERC CIP** to solidne technicznie dokumenty. Problemem nie są zalecenia. *Problem polega na tym, do jakich systemów się je stosuje.*

## Systemy zbudowano tak, by działały, a nie by były zabezpieczone

**Sterowniki PLC, systemy SCADA, rozproszone systemy sterowania (DCS) i starszy przemysłowy sprzęt IoT** zaprojektowano w jednym celu: miały niezawodnie działać przez długi czas. **Dostępność była jedynym celem projektowym wartym omówienia.** Poufność, integralność, uwierzytelnianie i rejestrowanie zdarzeń nie były wymaganiami. W wielu przypadkach nie brano ich nawet pod uwagę podczas projektowania tych systemów.

NIST SP 800-82 Rev 3 (2023) mówi o tym otwarcie. Opisuje środowiska OT jako mające *„szczególne wymagania dotyczące wydajności, niezawodności i bezpieczeństwa”*, w których *„zabezpieczenia nie mogą zakłócać działania systemu”*. Przeczytaj to jeszcze raz. **Główny dokument z wytycznymi bezpieczeństwa dla technologii operacyjnych wyraźnie przyznaje, że bezpieczeństwo jest na drugim miejscu.** To nie wada dokumentu. To trafny opis środowiska.

Nie zastosujesz kontroli dostępu opartej na rolach do PLC, które nie zna pojęcia ról użytkowników. Nie zaktualizujesz oprogramowania sprzętowego urządzenia, którego producent już nie istnieje. **Starsze protokoły szeregowe, w tym Modbus RTU i Profibus DP, nie mają natywnego uwierzytelniania.** Przesyłają polecenia i dane każdemu, kto o nie poprosi. Nie sprawdzają, kto wysyła żądanie.

*Wytyczne są dobre. Systemy często nie potrafią ich spełnić.* To różne problemy.

## Istnieją dwie zupełnie różne kategorie systemów OT

**Starsze sterowniki PLC z lat 80. do początku XXI wieku** projektowano do pracy w izolacji, z dostępem wyłącznie fizycznym. Korzystają z własnościowych systemów operacyjnych. Często zarządza się nimi ze stacji inżynierskich podłączonych także do sieci firmowych. Ich konfiguracje są przechowywane w formatach bez kontroli integralności. Systemy te stanowią znaczną część infrastruktury wodociągowej, energetycznej, produkcyjnej i transportowej.

**Nowoczesne sterowniki z funkcjami zabezpieczeń są inne.** Siemens, Schneider, Rockwell, Beckhoff i Phoenix Contact dostarczają już platformy z bezpiecznym rozruchem, podpisanym oprogramowaniem sprzętowym, kontrolą dostępu opartą na rolach, tożsamością wspieraną przez TPM oraz szyfrowaną komunikacją. EtherNet/IP CIP Security, PROFINET Security Class i OPC UA z uwierzytelnianiem są dostępne w aktualnym sprzęcie.

Nie umniejszam znaczenia nowoczesnej inżynierii bezpieczeństwa OT. Postęp jest realny. **Problem w tym, że większość wdrożonych systemów nie jest nowoczesna.** Gdy ktoś mówi o „cyberbezpieczeństwie OT”, zwykle opisuje próbę zabezpieczenia 20-letniego sterownika programowalnego za pomocą ram bezpieczeństwa cybernetycznego opracowanych w 2023 roku. O tę lukę chodzi.

## Co naprawdę działa

**Bezpieczeństwo fizyczne i izolacja sieci to najpewniejsze zabezpieczenia starszych środowisk OT.** Wszystkie główne standardy bezpieczeństwa ICS mówią to samo. IEC 62443 dzieli środowiska OT na strefy bezpieczeństwa z określonymi kanałami komunikacji. Chodzi o to, by ruch boczny musiał przechodzić przez kontrolowane granice, a nie swobodnie rozchodził się po płaskiej sieci.

Izolacja sieci znacznie ogranicza powierzchnię ataku przez sieć, ale nie eliminuje wszystkich zagrożeń. Nośniki wymienne, dostęp osób wewnątrz organizacji, laptopy serwisowe, tymczasowe połączenia inżynierskie i ataki na łańcuch dostaw to udokumentowane drogi do systemów bez dostępu do sieci. **Stuxnet**, który dotarł do odizolowanych irańskich zakładów z wirówkami za pomocą zainfekowanych pamięci USB, jest klasycznym przykładem. *Izolacja sieci jest konieczna. Nie wystarcza.*

**Nadzór człowieka nad parametrami procesu fizycznego** pozostaje jedną z najpewniejszych metod wykrywania problemów. Wyszkolony operator obserwujący ciśnienie, temperaturę i przepływ w czasie rzeczywistym zauważy rzeczy, których nie wykryje żaden system wykrywania włamań. IDS nie sprawdzi, czy wartość cyfrowa odpowiada rzeczywistości fizycznej.

Zabezpieczenia ograniczające ryzyko w odpowiednich kontekstach:

- **Diody danych** pozwalają wysyłać telemetrię na zewnątrz bez przyjmowania połączeń przychodzących
- **Listy dozwolonych aplikacji** na stacjach HMI ograniczają programy uruchamiane na komputerach z dostępem do systemów sterowania
- **Pasywne platformy wykrywania anomalii** firm Claroty, Dragos i Nozomi analizują ruch bez ingerencji w komunikację płaszczyzny sterowania
- **Segmentacja sieci** między strefami OT spowalnia ruch boczny bez konieczności pełnej izolacji fizycznej
- **Zasady zero trust**, opisane w NIST SP 800-82 Rev 3, wprowadzają weryfikację każdej sesji do niektórych nowoczesnych architektur OT

*Żadne z tych zabezpieczeń nie rozwiązuje podstawowych ograniczeń projektowych. Ograniczają ryzyko na obrzeżach systemów, których nigdy nie projektowano z myślą o takich zabezpieczeniach.*

## Sygnałów analogowych nie da się uwierzytelnić

**Pętle prądowe 4-20 mA, sygnały 0-10 V, wyjścia termopar i odczyty RTD są przesyłane jako zmienne sygnały elektryczne.** Sygnał fizyczny nie ma mechanizmu weryfikacji autentyczności. Kto poda właściwy sygnał na przewód, zostanie uznany za wiarygodne źródło.

Stuxnet pokazał to w praktyce. Atak zmodyfikował logikę PLC działającą na sterownikach Siemens S7 i jednocześnie odtwarzał na interfejsach operatorów wcześniej nagrane prawidłowe dane procesu. **Operatorzy widzieli na ekranach normalne odczyty, gdy wirówki przekraczały limity pracy.** Oszustwo trwało wystarczająco długo, by spowodować fizyczne uszkodzenia wyglądające na awarię sprzętu, a nie atak.

Zakłócenia elektromagnetyczne od kabli zasilających, napędów o zmiennej częstotliwości, wyładowań atmosferycznych i niewłaściwego uziemienia zniekształcają pomiary analogowe podczas normalnej pracy. IEC 61000 istnieje właśnie z tego powodu. W instalacjach przemysłowych stosuje się ekranowane przewody, prawidłowe uziemienie, filtry i separację fizyczną.

Nowoczesne inteligentne urządzenia polowe wewnętrznie przekształcają pomiary analogowe na postać cyfrową przed ich wysłaniem przez HART-IP, WirelessHART, EtherNet/IP CIP Security lub OPC UA. Nowoczesny sprzęt obsługuje uwierzytelnioną komunikację cyfrową na poziomie urządzenia. **Analogowy przewód 4-20 mA łączący starszy przetwornik ze starszym wejściem PLC nie zapewnia uwierzytelniania i nigdy go nie zapewni.** Znaczna część zainstalowanych przyrządów nadal korzysta z takiego przewodu.

## Walidacja czujników to zabezpieczenie funkcjonalne, a nie cyberbezpieczeństwo

Systemy bezpieczeństwa procesowego stosują **redundantne głosowanie czujników**. Układ 2 z 3, w którym dwa czujniki wskazują 230 PSI, a jeden 14 PSI, oznacza odczyt odstający. Zapewnia to ograniczoną odporność na manipulację pojedynczym czujnikiem. *To zabezpieczenie z zakresu inżynierii bezpieczeństwa funkcjonalnego, a nie cyberbezpieczeństwa.*

Standardowe sterowniki PLC nie weryfikują kryptograficznie wejść analogowych. Generator sygnału podłączony do pętli nie różni się od legalnego przetwornika. PLC odczytuje prąd i reaguje na niego.

**Systemy bezpieczeństwa z oprzyrządowaniem miały być niezależną ostatnią linią obrony.** W 2017 roku **TRITON** (znany także jako **TRISIS**) zaatakował urządzenia SIS Triconex firmy Schneider Electric, by wyłączyć tę warstwę. Atakujący dotarli do systemu bezpieczeństwa przez sieć stacji inżynierskich. *Niezależność tej warstwy zależała od separacji sieci, której nie utrzymano.*

IEC 62443-3-3, IEC 62443-4-2 oraz koordynacja z bezpieczeństwem funkcjonalnym według IEC 61511 uwzględniają tę lekcję. Przez lata różne zespoły traktowały bezpieczeństwo procesowe i cyberbezpieczeństwo jako osobne dziedziny. **TRITON praktycznie potwierdził to, co niezależne analizy wykazywały w teorii:** napastnik, który neutralizuje system bezpieczeństwa przed wywołaniem niebezpiecznego stanu, usuwa ostatnie zabezpieczenie zapobiegające fizycznym skutkom.

## Łańcuch dostaw to wektor, który prawdopodobnie pomijasz

**Większość programów bezpieczeństwa OT skupia się na architekturze sieci. Wiele niedawnych włamań do OT wykorzystywało punkty wejścia, których architektura sieci nie blokuje.**

Ryzyko łańcucha dostaw OT obejmuje:

- **Integralność oprogramowania sprzętowego przed instalacją**, zwłaszcza dostawę sprzętu z niezweryfikowanym oprogramowaniem z fabryki lub od dystrybutora
- **Sesje zdalnego dostępu dostawców**, które pozostają stałym zagrożeniem w zakładach zależnych od wsparcia producenta
- **Stacje inżynierskie** podłączone zarówno do sieci firmowej, jak i OT, często dla wygody operacyjnej
- Brak **zestawień komponentów oprogramowania (SBOM)** w większości starszych wdrożeń OT, co niemal uniemożliwia śledzenie składników oprogramowania
- **Podwykonawców serwisowych**, którzy wnoszą laptopy i pamięci USB do operacyjnie odizolowanych środowisk
- **Obsługę podpisanych aktualizacji oprogramowania sprzętowego**, której brakuje w większości starszych platform

NIST SP 800-82 Rev 3 zawiera osobne sekcje o zależnościach od dostawców i dostępie stron trzecich. *Jeśli wewnętrzna izolacja sieci działa, ale dostawca sprzętu utrzymuje stały portal zdalnego dostępu do sieci inżynierskiej, nie masz izolowanej sieci. Masz lukę z drzwiami kontrolowanymi przez kogoś innego.*

## Zabezpieczanie starszych systemów kosztuje więcej, niż powinno

Każdy program PLC jest pisany na zamówienie dla konkretnego procesu. Logika sterująca układem ograniczania uderzeń ciśnienia w rafinerii różni się całkowicie od logiki sekwencji chlorowania w oczyszczalni wody czy regulatora turbiny. To nie wybór. Procesy fizyczne są różne.

**Zabezpieczanie starszych systemów OT często kosztuje więcej, niż przewidywano** z powodu wymagań walidacji inżynierskiej, koniecznych przestojów, ograniczeń wsparcia dostawców, braków w dokumentacji i cykli testowych dłuższych od pierwotnych szacunków. Gdy producent nie wspiera sprzętu, koszty zabezpieczenia mogą dorównać kosztowi wymiany systemu lub go przekroczyć.

**Zgodność z NERC CIP w przypadku cyberzasobów dużego systemu elektroenergetycznego kosztuje poszczególne przedsiębiorstwa użyteczności publicznej miliony dolarów rocznie.** Badanie American Public Power Association z 2019 roku wykazało duże różnice w kosztach zgodności i nieproporcjonalne obciążenie mniejszych przedsiębiorstw. Wiele systemów wodociągowych i mniejszych przedsiębiorstw nie podlega NERC CIP i nie ma porównywalnych obowiązków.

## Systemy należy wymienić

**Wymiana starszych systemów OT to właściwe rozwiązanie.** W dużych zakładach oznacza dziesiątki milionów dolarów, długie okresy przejściowe i ryzyko błędnego przeniesienia złożonej wiedzy operacyjnej podczas migracji. To realne koszty i ryzyka.

Zalecenia branżowe CISA i ICS-CERT mówią o stosowaniu zabezpieczeń kompensacyjnych podczas planowania wymiany. To racjonalna reakcja na ograniczenia. *Mówią wprost, że pełne zabezpieczenie starszego sprzętu jest niemożliwe. Stosuj dostępne zabezpieczenia i planuj wymianę.*

**W praktyce wiele z tych systemów pozostanie w użyciu przez dziesięciolecia.** To problem finansowania i polityki. Społeczność techniczna jasno wskazała potrzebne działania. Budżety operacyjne i harmonogramy wymiany nie nadążają.

## Podłączanie systemów OT do sieci często pogarsza sytuację

Wiele organizacji dodało zdalny dostęp i monitoring do środowisk OT, które pierwotnie były odizolowane. Argument operacyjny jest prosty: zdalny podgląd skraca czas reakcji, a dostawcy szybciej pomagają przez połączenie zdalne. **Skutek dla bezpieczeństwa jest taki, że odizolowane systemy bez zdalnej powierzchni ataku teraz ją mają.**

**Incydent w oczyszczalni wody w Oldsmar z 2021 roku** nastąpił przez zdalne połączenie TeamViewer. Napastnik zmienił ustawienia dozowania wodorotlenku sodu za pomocą legalnego narzędzia do zdalnego dostępu, dodanego dla wygody. **Incydent Colonial Pipeline z 2021 roku** zaczął się od włamania do sieci IT. Operator prewencyjnie zatrzymał działanie rurociągu OT, ponieważ nie mógł potwierdzić, że sieć OT pozostała nienaruszona. *Atak nie naruszył bezpośrednio sieci OT. Zatrzymanie spowodowała niepewność, czy doszło do włamania.*

Dodanie łączności sieciowej do starszych systemów OT dla korzyści operacyjnych, bez zaprojektowania jej zgodnie z odpowiednimi normami, **często powoduje większe ryzyko, niż uzasadniają korzyści**. Model Purdue pozostaje użyteczną architekturą referencyjną, ale NIST nie uznaje go już za wystarczający samodzielnie. Nowoczesne IIoT, łączność z chmurą, zdalne operacje i architektury hybrydowe wymagają dokładniejszego projektu niż sama segmentacja stref.

## Zgodność z pisemnymi standardami to nie bezpieczeństwo

NIST SP 800-82 Rev 3, IEC 62443 i NERC CIP opisują odpowiednie zabezpieczenia tych systemów. Nie odrzucam ich. Zwracam uwagę na ich wyraźne stwierdzenie: **nie każdy system OT może wdrożyć każde zabezpieczenie.** Ramy przewidują stopniowane poziomy bezpieczeństwa i środki kompensacyjne, ponieważ systemy często nie mogą spełnić wszystkich wymagań.

Różnica między tym, co opisują standardy, a tym, co może osiągnąć konkretne starsze wdrożenie, nie jest błędem dokumentacji. Systemy nie obsługują tych zabezpieczeń. Wytyczne to przyznają. **Pozytywny wynik audytu zgodności starszego OT nie oznacza, że środowisko jest bezpieczne.** Oznacza, że udokumentowano środki kompensacyjne i audytor je zaakceptował.

Ramy zarządzania ryzykiem NIST jasno stwierdzają, że po zastosowaniu zabezpieczeń pozostaje ryzyko rezydualne. Akceptacja ryzyka jest jednym z czterech wyników ram, obok jego przeniesienia, ograniczenia i uniknięcia. *Uznanie ryzyka rezydualnego jest częścią oficjalnych wytycznych.* **Kto twierdzi, że spełnienie wymogów zgodności zabezpiecza środowisko OT, mówi coś, czego przywoływane standardy nie potwierdzają.**

## Co zrobić ze starszym OT

Jeśli zarządzasz starszym środowiskiem OT:

- **Traktuj izolację sieci jako główne zabezpieczenie** i kontroluj wszystko, co przekracza granicę OT
- **Opracuj osobny plan zabezpieczenia stacji inżynierskich.** Łączą oba środowiska i często są punktem wejścia
- **Kontroluj i rejestruj wszystkie nośniki wymienne** w strefach OT
- **Kontroluj zdalny dostęp dostawców** i zamykaj każdą nieużywaną sesję
- Wdróż redundantny monitoring czujników, jeśli pozwala na to projekt procesu
- **Przygotuj harmonogram wymiany z realnymi szacunkami kosztów**, nawet jeśli wymiana nastąpi dopiero za kilka lat
- **Nie traktuj zakończenia audytu zgodności jako osiągnięcia bezpieczeństwa**

Jeśli kupujesz nowe systemy OT:

- **Uwzględnij wymagania bezpieczeństwa w specyfikacji zakupu** przed odpowiedziami dostawców
- Wybieraj platformy z udokumentowaną obsługą uwierzytelnianej komunikacji, podpisanych aktualizacji firmware i kontroli dostępu opartej na rolach
- **Projektuj granice IT/OT jako jawne kanały według IEC 62443**, a nie jako ogólną zasadę „trzymaj je osobno”
- **Wymagaj SBOM dla komponentów oprogramowania OT** jako elementu umowy

Branża dobrze opisała problem. Standardy są technicznie poprawne. *Systemy w terenie często nie potrafią spełnić zaleceń standardów.* Otwarte uznanie tego faktu to początek podejmowania decyzji o zarządzaniu pozostałym ryzykiem.

## Źródła

- NIST SP 800-82 Rev 3: przewodnik po bezpieczeństwie technologii operacyjnych (OT) (2023)
- IEC 62443: seria standardów bezpieczeństwa systemów automatyki i sterowania przemysłowego
- IEC 62443-3-3: wymagania bezpieczeństwa systemów i poziomy bezpieczeństwa
- IEC 62443-4-2: techniczne wymagania bezpieczeństwa komponentów IACS
- IEC 61511: bezpieczeństwo funkcjonalne systemów oprzyrządowania bezpieczeństwa
- NERC CIP: standardy ochrony infrastruktury krytycznej dużego systemu elektroenergetycznego
- IEC 61000: normy kompatybilności elektromagnetycznej
- Ostrzeżenia i dobre praktyki CISA ICS-CERT
- Ramy MITRE ATT&CK dla ICS
- Analiza techniczna Stuxnet, Langner Communications, 2011
- Analiza techniczna TRITON/TRISIS, Dragos, 2017
- Przegląd incydentu w oczyszczalni Oldsmar, CISA, 2021
- Badanie kosztów zgodności NERC CIP, American Public Power Association, 2019
