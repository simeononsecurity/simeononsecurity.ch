---
title: "Dobierz zasilacz UPS do homelabu i przetestuj automatyczne wyłączanie"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Zmierz pobór mocy homelabu, porównaj limity W i VA zasilacza UPS, sprawdź czas pracy przy swoim obciążeniu i przetestuj bezpieczne wyłączanie, zanim zaufasz zasilaniu z baterii."
genre: ["Laboratorium domowe", "Ochrona zasilania", "Administracja systemami"]
tags: ["UPS do homelabu", "dobór UPS", "czas pracy UPS", "automatyczne wyłączanie", "Network UPS Tools", "moc UPS w watach", "moc UPS w VA", "współczynnik mocy", "zasilanie awaryjne", "wyłączanie serwera", "wyłączanie NAS", "awaria zasilania", "test UPS", "krzywa czasu pracy", "miernik mocy", "monitorowanie UPS", "wymiana baterii", "ochrona przeciwprzepięciowa", "bezpieczne wyłączanie", "zasilanie homelabu"]
cover: "/img/cover/ups-runtime-sizing-shutdown-test.webp"
coverAlt: "Zasilacz UPS w homelabie podtrzymuje serwer, NAS, router i przełącznik według osi czasu od awarii zasilania do wyłączenia."
coverCaption: "Zmierz obciążenie, sprawdź czas pracy i przetestuj wyłączanie przed awarią zasilania."
---

**UPS**, czyli zasilacz awaryjny, daje homelabowi czas na zapisanie pracy i wyłączenie systemów podczas awarii zasilania. Sama etykieta nie mówi, jak długo serwery będą działać. Potrzebujesz pomiaru obciążenia urządzeń, limitów mocy w watach i VA, szacowanego czasu pracy przy tym obciążeniu oraz sprawdzonej procedury wyłączania.

## Najważniejsze informacje

- **Zmierz obciążenie:** Zapisz normalny i wysoki pobór mocy każdego urządzenia, które ma pozostać zasilane z baterii.
- **Sprawdź oba parametry:** UPS musi spełniać wymagania podłączonych urządzeń dotyczące mocy w W i VA.
- **Odczytaj krzywą czasu pracy:** Czas pracy zależy od obciążenia i stanu baterii. Korzystaj z danych dla konkretnego modelu.
- **Przetestuj procedurę:** Sprawdź, czy sygnał z UPS dociera do każdego hosta i czy hosty zatrzymują się przed wyczerpaniem baterii.

## Zanim zaczniesz

Potrzebujesz miernika mocy zgodnego z lokalną instalacją elektryczną, listy urządzeń i zasilaczy oraz dostępu do specyfikacji i wykresu czasu pracy każdego rozważanego modelu UPS. Do automatycznego testu wyłączania potrzebujesz również obsługiwanego połączenia USB lub interfejsu zarządzania przez sieć oraz oprogramowania dla każdego hosta. Zarezerwuj czas na pomiar przy normalnym obciążeniu, obserwację przy dużym obciążeniu i zaplanowany test serwisowy. To zadanie dla osób mających doświadczenie z homelabem, ponieważ pełny test wyłączania przerywa działanie usług.

Przewodnik po [listwach przeciwprzepięciowych](/articles/protecting-your-tech_-the-best-surge-protectors/) opisuje ochronę przed przepięciami. Zestawienie [modeli UPS](/articles/best-ups-models-for-uninterrupted-connectivity/) przedstawia produkty. Ten poradnik dotyczy doboru i weryfikacji zasilania dla twojego obciążenia. Zarówno [przewodnik doboru UPS firmy Eaton](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/ups-sizing-guide.html), jak i [poradnik zakupowy Schneider Electric](https://www.se.com/us/en/work/support/product-support/ups-buying-guide-for-selecting-a-battery-backup-system/) rozróżniają moc wyjściową od czasu pracy baterii.

> **Ostrzeżenie:** Używaj tylko gniazd i obciążeń zatwierdzonych przez producenta UPS. Testuj w granicach znamionowej mocy zasilacza. Rzeczywisty test wyłączania zatrzymuje podłączone laboratorium.

## Zmierz urządzenia, które mają pozostać włączone

Zdecyduj, które urządzenia muszą działać aż do wyłączenia. Uwzględnij hypervisor, pamięć masową, przełącznik sieciowy i router, jeśli host potrzebuje dostępu do sieci, aby otrzymać sygnał wyłączenia. Nie podłączaj monitorów, drukarek i innych opcjonalnych urządzeń do gniazd podtrzymywanych przez baterię, chyba że wymagają tego twoje założenia.

Zmierz przy gniazdku grupę urządzeń, które mają korzystać z podtrzymania bateryjnego. Zapisz **normalny pobór w watach** i najwyższą zaobserwowaną wartość podczas typowej pracy, na przykład podczas uruchamiania hostów lub maszyn wirtualnych. Etykieta zasilacza podaje jego wydajność, a nie zmierzony pobór mocy systemu. Mimo to sprawdź etykiety urządzeń pod kątem limitów prądu wejściowego i rozruchowego. Zapisz warunki pomiaru w arkuszu.

| Urządzenie | Normalny pobór w watach | Zaobserwowany szczyt w watach | Gniazdo bateryjne? |
|---|---:|---:|---|
| **Router i przełącznik** | 30 | 35 | Tak |
| **NAS** | 60 | 90 | Tak |
| **Mały serwer** | 90 | 135 | Tak |
| **Przykładowa suma** | **180** | **260** | Trzy urządzenia |

Powyższe wartości są **przykładowe**, a nie zmierzone w konkretnym laboratorium. Obciążenie zależy od dysków, kart GPU, ustawień zasilania i podłączonego sprzętu. Po większych zmianach sprzętowych wykonaj pomiar ponownie.

## Porównaj waty i VA

**Waty** opisują moc czynną pobieraną przez sprzęt. **Woltoampery (VA)** opisują moc pozorną. Zależność między nimi wynika ze **współczynnika mocy**: waty podzielone przez współczynnik mocy dają VA. Eaton wyjaśnia to obliczenie w swoim [przewodniku doboru](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/ups-sizing-guide.html). Nie traktuj oznaczenia 1000 VA jak 1000 W. Sprawdź osobny limit mocy UPS w watach.

Dla przykładowego szczytowego obciążenia 260 W margines 25% daje **325 W**. Schneider Electric zaleca moc wyjściową około [20%–25% większą od obciążenia](https://www.se.com/us/en/work/support/product-support/ups-buying-guide-for-selecting-a-battery-backup-system/). Wybierz UPS, którego ciągła moc w watach przewyższa planowany szczyt wraz z marginesem. Jeśli znasz łączny współczynnik mocy, podziel szczytową moc w watach przez tę wartość, aby oszacować szczytowe VA, a następnie zastosuj do VA wybrany margines. W przeciwnym razie użyj odpowiedniego miernika albo konfiguratora producenta, aby ustalić wymagania VA i zapas. Nie zgaduj współczynnika mocy, jeśli go nie zmierzyłeś.

Margines mocy nie określa czasu pracy. UPS o wysokim limicie mocy, ale małej baterii może zasilać obciążenie tylko przez krótki czas. Przed wyborem sprawdź gniazda, typ wtyczki, napięcie wejściowe, interfejs komunikacyjny i możliwość wymiany baterii.

## Określ docelowy czas pracy

Zapisz, ile czasu potrzebuje laboratorium, aby bezpiecznie się zatrzymać. Uwzględnij czas dostarczenia alertu o wyłączeniu do hostów, zatrzymania maszyn wirtualnych, opróżnienia buforów zapisu pamięci masowej i odłączenia wyjścia UPS. Dodaj zapas na wolniejsze wyłączanie i starszą baterię. Laboratorium, które ma działać podczas krótkich awarii, wymaga innego celu niż takie, które ma jedynie bezpiecznie się wyłączyć.

Dla **przykładu** przyjmijmy, że przetestowane wyłączenie trwa 6 minut, a ty dodajesz 5 minut rezerwy. Wymagany czas pracy przy przewidywanym obciążeniu wynosi co najmniej 11 minut. To przykład planowania, a nie uniwersalny próg. Porównaj cel z wykresem czasu pracy lub konfiguratoreм wybranego modelu przy **zmierzonym normalnym i wysokim obciążeniu**, a następnie powtórz ocenę wraz ze starzeniem się baterii. [Konfigurator UPS Schneider Electric](https://www.se.com/us/en/work/products/tools/ups-selector/) oblicza czas pracy na podstawie podanego obciążenia i specyfikacji modelu. Eaton również odsyła do danych dla konkretnych modeli w swoim [poradniku desktopowych UPS-ów](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/desktop-ups-buying-guide.html).

Skopiuj ten **arkusz** do swojego laboratorium. Wypełnij wiersze urządzeń wynikami pomiaru. Zsumuj normalne i wysokie wartości w watach, dodaj wybrany margines do wysokiej sumy, a taki sam margines zastosuj do zmierzonych lub obliczonych szczytowych VA. Porównaj oba wyniki z wybranym UPS-em. Jeśli korzystasz z konfiguratora producenta, zapisz wynik doboru VA i zapas. Oszacuj czas pracy z wykresu danego modelu. Podczas testu uzupełnij czasy i wyniki przywracania.

| Pole | Twój wynik |
|---|---|
| **Urządzenia i gniazda bateryjne** | Nazwy urządzeń i przypisane gniazda |
| **Normalne waty na urządzenie i łącznie** | Zmierzone wartości i suma |
| **Wysokie waty na urządzenie i łącznie** | Najwyższe zaobserwowane wartości i suma |
| **Zmierzony lub określony współczynnik mocy** | Wartość i źródło albo „nieznany” |
| **Zmierzona lub obliczona szczytowa wartość VA** | Szczytowe waty podzielone przez łączny współczynnik mocy, jeśli jest znany |
| **Margines mocy** | Wybrany procent, waty i VA po dodaniu marginesu |
| **Parametry wybranego UPS-a** | Model, moc wyjściowa w watach i VA oraz limity gniazd |
| **Cel czasu pracy i wynik z wykresu** | Wymagane minuty i oszacowanie modelu dla twojego obciążenia |
| **Czasy alertu i wyłączenia** | Czas alertu o baterii i zatrzymania ostatniego hosta |
| **Wynik przywracania** | Uruchomienie hostów, pamięć masowa, aplikacje i monitoring |

Jeśli współczynnik mocy jest nieznany, skorzystaj z konfiguratora producenta lub zmierz moc pozorną odpowiednim miernikiem. Nie podawaj VA obliczonego przy użyciu zgadywanego współczynnika. Arkusz jest gotowy dopiero wtedy, gdy model spełnia oba limity wyjściowe, a jego szacowany czas pracy przekracza cel wyłączenia.

> **Oczekiwany wynik:** Arkusz wymienia podłączone urządzenia, zmierzone obciążenia, limity UPS w watach i VA, docelowy czas pracy oraz oszacowanie dla konkretnego modelu.

## Zaplanuj automatyczne wyłączanie

UPS tymczasowo podtrzymuje zasilanie sprzętu. Host nadal potrzebuje **sygnału wyłączenia**. Sprawdź, czy UPS udostępnia USB, kartę zarządzania sieciowego lub inny obsługiwany interfejs. Sprawdź, czy każdy host, który ma się zatrzymać, ma zgodną ścieżkę monitorowania. Eaton informuje, że wiele modeli obsługuje komunikację USB lub sieciową potrzebną do [bezpiecznego wyłączenia serwera lub NAS](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/desktop-ups-buying-guide.html).

W laboratorium Linux korzystającym z **Network UPS Tools (NUT)** sterownik odczytuje UPS, `upsd` udostępnia jego stan, a `upsmon` inicjuje wyłączenie hosta, gdy zasilanie staje się krytyczne. Host połączony bezpośrednio z UPS-em przez USB lub port szeregowy zwykle uruchamia sterownik, `upsd` i `upsmon` w trybie **Primary**. Pozostałe hosty uruchamiają `upsmon` w trybie **Secondary** względem tego serwera. Sieciowy UPS wymaga zgodnego sterownika i konfiguracji Primary właściwej dla modelu. [Przewodnik topologii NUT](https://networkupstools.org/docs/user-manual.chunked/ar01s02.html) opisuje te role. Skonfiguruj router i przełącznik tak, aby hosty monitorujące zachowały łączność podczas pracy z baterii. Ogranicz polecenie wyłączenia i jego uprawnienia do administratorów.

Przed testem wyłączenia sprawdź, czy sterownik odczytuje aktualny stan. Zastąp `myupsname` nazwą UPS-a z konfiguracji NUT:

```bash
upsc myupsname@localhost ups.status
```

[Przewodnik konfiguracji NUT](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html) wymaga wartości `OL` przy normalnym zasilaniu sieciowym i opisuje `OB` jako pracę na baterii. Uruchom kontrolę stanu na każdym hoście monitorującym UPS i użyj poprawnej nazwy serwera dla klientów zdalnych. Nieaktualny lub brakujący odczyt oznacza, że przed testem trzeba naprawić ścieżkę sygnału.

Zapisz **kolejność wyłączania**. Na przykład najpierw zatrzymaj maszyny wirtualne z aplikacjami, potem klientów pamięci masowej, a na końcu hypervisor i NAS. Sprawdź, czy każda usługa i system plików odzyskują sprawność po powrocie zasilania. Samo zatrzymanie hosta bez poprawnego przywrócenia aplikacji nie oznacza pełnego sukcesu.

## Testuj bez zgadywania

Zacznij od **próby na sucho** na hoście ze skonfigurowanym sterownikiem UPS. NUT opisuje `upsdrvctl -t shutdown` jako podgląd sekwencji wyłączania sterownika; polecenie nie wywołuje sterowników ani nie odcina zasilania:

```bash
upsdrvctl -t shutdown
```

Ta **próba sterownika** nie dowodzi, że alert o awarii dotrze do każdego hosta. Sprawdź każdą usługę monitorującą i jej dzienniki. W oknie serwisowym [instrukcja testowania wyłączania NUT](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html) opisuje wymuszoną próbę wyłączenia za pomocą `upsmon -c fsd` na głównym hoście NUT. Ten **test FSD** rozpoczyna rzeczywistą sekwencję wyłączania. Flaga FSD pozostaje ustawiona do ponownego uruchomienia `upsd`. Po uruchomieniu systemów potwierdź, że `upsd` uruchomił się ponownie, a stan nie pokazuje już FSD, zanim ponownie zaufasz monitoringowi. Przeczytaj aktualną [instrukcję upsmon](https://networkupstools.org/docs/man/upsmon.html), przygotuj drogę odzyskiwania i rozpocznij test dopiero po zapisaniu pracy oraz powiadomieniu użytkowników laboratorium.

Kontrolowany **test zdarzenia bateryjnego** rozpocznij od procedury producenta UPS-a i niekrytycznych urządzeń. Test przy małym obciążeniu sprawdza dostarczanie sygnału, ale nie potwierdza czasu pracy dla twojego laboratorium. Później, podczas okna serwisowego, przetestuj reprezentatywne planowane obciążenie bateryjne. Ktoś powinien obserwować UPS i móc przywrócić zasilanie sieciowe, gdy zapas zacznie maleć. Zapisz obciążenie widoczne na UPS-ie, czas przejścia w tryb bateryjny, rozpoczęcie wyłączania każdego hosta oraz moment zatrzymania ostatniego hosta. Sprawdź, czy bateria nie wyczerpie się przed zatrzymaniem hostów. Po powrocie zasilania sprawdź uruchamianie hostów, stan aplikacji, integralność pamięci masowej i stan monitoringu. Według NUT sekwencja kończy się poprawnie, gdy system operacyjny zatrzymuje się przed wyczerpaniem baterii, a działanie wraca po przywróceniu zasilania.

| Kontrola | Zapisz |
|---|---|
| **Ścieżka sygnału** | Zdarzenie UPS widoczne na każdym monitorującym hoście |
| **Czas wyłączania** | Ostatni host zatrzymał się przed wyczerpaniem baterii |
| **Przywracanie** | Hosty, pamięć masowa i aplikacje startują poprawnie |
| **Moc** | Obciążenie UPS-a pozostaje w limitach W i VA |

## Rozwiązywanie problemów

- **Alarm przeciążenia UPS-a:** Odłącz opcjonalne urządzenia. Porównaj zmierzone wysokie obciążenie z oboma limitami UPS-a i limitami jego gniazd.
- **Czas pracy krótszy od oczekiwanego:** Sprawdź aktualne obciążenie, wiek baterii, dane czasu pracy dla modelu i wyniki ostatniego testu baterii. Nie wyliczaj liniowo czasu wyłącznie z VA.
- **Jeden host pozostaje włączony:** Sprawdź usługę monitorowania, połączenie sieciowe, uprawnienia do wyłączania i dzienniki.
- **Hosty zatrzymują się, lecz nie wracają:** Sprawdź zachowanie wyjścia UPS-a po powrocie zasilania, ustawienie firmware hosta dotyczące przywracania zasilania oraz opisane w NUT [kwestie wyścigu z zasilaniem](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html).
- **Próba na sucho działa, a test awarii nie:** Podgląd sterownika sprawdza węższą część procedury. Skontroluj dostarczanie zdarzeń i rzeczywistą kolejność wyłączania hostów.

## Następne kroki

Przechowuj arkusz razem z inwentaryzacją homelabu. Zmierz obciążenie ponownie po dodaniu sprzętu i powtórz test wyłączania po zmianie UPS-a, oprogramowania monitorującego, polityki uruchamiania hostów lub stosu pamięci masowej. Osobno sprawdź plan tworzenia kopii i przywracania danych. Bateria chroni czas potrzebny na wyłączenie, a [przetestowana kopia homelabu](/articles/what-is-a-homelab-and-should-you-have-one/) chroni dane przed innymi awariami.
