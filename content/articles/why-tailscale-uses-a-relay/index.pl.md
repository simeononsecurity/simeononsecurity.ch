---
title: "Dlaczego Tailscale używa przekaźnika: połączenia bezpośrednie, DERP i przekaźniki równorzędne"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Sprawdź, dlaczego Tailscale używa przekaźnika, jak odczytywać wyniki status i netcheck oraz kiedy połączenie DERP lub przez przekaźnik równorzędny wymaga diagnozy."
genre: ["Networking", "Network Security", "Self-Hosted"]
tags: ["Tailscale", "przekaźnik Tailscale", "DERP", "Tailscale Peer Relay", "połączenie bezpośrednie", "WireGuard", "przechodzenie przez NAT", "trudny NAT", "CGNAT", "UDP", "tailscale status", "tailscale ping", "tailscale netcheck", "MappingVariesByDestIP", "wydajność VPN", "zdalny dostęp", "tailnet", "sieci homelab", "opóźnienie przekaźnika", "szyfrowanie end-to-end"]
cover: "/img/cover/why-tailscale-uses-a-relay.webp"
coverAlt: "Dwa laptopy na oddzielnych wyspach wymieniają zaszyfrowane pakiety przez centralny przekaźnik, gdy bezpośrednia trasa jest przerwana."
coverCaption: ""
---

**Tailscale używa przekaźnika**, gdy urządzenia nie nawiązały połączenia bezpośredniego. Krótkie połączenie DERP podczas uruchamiania jest normalne. Długotrwałe korzystanie z przekaźnika często wynika z translacji adresów sieciowych (NAT) lub ustawień zapory wpływających na trasę między urządzeniami. Połączenia bezpośrednie, DERP i przekaźniki równorzędne zachowują szyfrowanie end-to-end WireGuard. [Typy połączeń Tailscale](https://tailscale.com/docs/reference/connection-types).

## Najważniejsze wnioski

- **Rozpoznaj trasę:** odróżnij połączenia bezpośrednie, DERP i przekaźnik równorzędny.
- **Zbierz dowody:** uruchom testy skierowane do konkretnego peera oraz kontrole sieci po obu stronach.
- **Przeanalizuj wzorzec:** porównaj pary urządzeń i warunki sieciowe.
- **Wybierz zmianę:** uzasadnij ją pomiarem obciążenia i ponownym testem.

## Zanim zaczniesz

**Wymagania:** dwa zarejestrowane urządzenia w trybie online oraz terminal z interfejsem wiersza poleceń Tailscale, czyli **CLI**. Uprawnienia administratora są potrzebne tylko wtedy, gdy dochodzenie doprowadzi do zmian konfiguracji.

**Szacowany czas:** pięć minut na podstawowe kontrole, a następnie 15–20 minut na ćwiczenie porównawcze. **Poziom trudności:** początkujący w zakresie obserwacji i średnio zaawansowany przy zmianach sieciowych. Najpierw określ problem, na przykład wolną kopię zapasową lub opóźnioną reakcję terminala.

## Połączenia bezpośrednie, DERP i przekaźnik równorzędny

**Tailnet** to Twoja sieć Tailscale. Jej urządzenia próbują nawiązać bezpośrednią łączność UDP. Gdy bezpośrednia trasa nie działa, dostępne są przekaźniki. Tailscale okresowo ponownie sprawdza dostępne opcje połączenia. [Nawiązywanie połączenia](https://tailscale.com/docs/reference/connection-types).

| Trasa | Przepływ ruchu | Typowe znaczenie |
|---|---|---|
| **Bezpośrednia** | Między dwoma urządzeniami | Zwykle preferowana pod względem wydajności |
| **Przekaźnik DERP** | Przez infrastrukturę przekaźników Tailscale | Dodaje pośrednika, gdy bezpośredni dostęp nie działa |
| **Przekaźnik równorzędny** | Przez skonfigurowane urządzenie w tailnecie | Alternatywny przekaźnik pod Twoją administracją |

**Wydajność DERP** zależy częściowo od dodatkowej trasy i współdzielonej przepustowości usługi. Tailscale opisuje limity przepustowości, które mają sprawiedliwie dzielić zasoby DERP. Nie istnieje uniwersalna prędkość przekaźnika pozwalająca przewidzieć czas transferu plików. [Rozwiązywanie problemów z wydajnością Tailscale](https://tailscale.com/docs/reference/troubleshooting/poor-performance-tailnet).

## Jak przebiega negocjacja połączenia

**Przechodzenie przez NAT** to proces tworzenia użytecznej trasy przez urządzenia translatujące adresy. Tailscale rozpoczyna komunikację przez DERP, jednocześnie negocjując trasę bezpośrednią. Jeśli łączność bezpośrednia nie działa, dostępny skonfigurowany przekaźnik równorzędny zapewnia kolejną możliwość. Tailscale ponownie sprawdza dostępne opcje. [Nawiązywanie połączenia](https://tailscale.com/docs/reference/connection-types).

**Trudny NAT** opisuje sposób mapowania utrudniający przechodzenie przez NAT. Liczą się warunki po obu stronach. Dwa urządzenia za różnymi routerami nie muszą zachowywać się tak samo, nawet jeśli obie sieci używają adresów prywatnych. [Łączność urządzeń](https://tailscale.com/docs/reference/device-connectivity).

W przypadku **laptopa używanego w różnych sieciach** trasa do domowego serwera może się zmienić po przejściu z domowego Wi-Fi do sieci hotelowej. Zapisz, z jakiej sieci korzystasz podczas obserwacji. Wczorajsze połączenie bezpośrednie nie opisuje dzisiejszej trasy.

## Sprawdź bieżące połączenie

Zastąp **`home-server`** nazwą Tailscale lub adresem peera:

```bash
tailscale ping home-server
tailscale status
tailscale netcheck
```

**`tailscale ping`** sprawdza łączność z nazwanym peerem. **`tailscale status`** wyświetla peery i szczegóły połączeń. **`tailscale netcheck`** raportuje warunki sieciowe urządzenia, na którym uruchomiono polecenie. [Dokumentacja CLI Tailscale](https://tailscale.com/docs/reference/tailscale-cli) opisuje te polecenia.

| Wskaźnik w wynikach | Interpretacja |
|---|---|
| **`direct`** | Ruch do tego peera korzysta z trasy bezpośredniej |
| **`relay`** | Ruch do tego peera przechodzi przez DERP |
| **`peer-relay`** | Ruch przechodzi przez skonfigurowany przekaźnik równorzędny |
| **Początkowy pong przez DERP** | Sprawdź kolejne wyniki, zanim uznasz, że trasa pozostała przekaźnikowa |

Etykiety pochodzą z [dokumentacji typów połączeń](https://tailscale.com/docs/reference/connection-types). **Najpierw wygeneruj ruch**, a potem sprawdź wybranego peera. Powyższe polecenia są przykładami, a nie wynikami zarejestrowanego benchmarku.

## Interpretacja zmiany trasy

Ta **przykładowa sekwencja** pomija adresy i czasy, aby skupić uwagę na zmianie połączenia:

```text
Pierwsza odpowiedź: przez DERP
Późniejsza odpowiedź: przez bezpośredni punkt końcowy
Późniejszy status: połączenie bezpośrednie
```

**Interpretacja:** podczas tej obserwacji negocjacja zakończyła się powodzeniem. Sama pierwsza odpowiedź prowadziłaby do błędnej diagnozy. Jeśli kolejne odpowiedzi i status nadal wskazują przekaźnik, zapisz trwałe użycie przekaźnika dla tej pary urządzeń i okresu testowego.

**Zakres testu:** udany ping Tailscale potwierdza łączność z peerem na potrzeby tego testu. Nie dowodzi, że panel, usługa plików ani demon SSH akceptują ruch aplikacji. Przed stwierdzeniem, że problem został rozwiązany, osobno przetestuj niedziałającą aplikację.

## Co pokazuje netcheck

Uruchom **`tailscale netcheck` na obu urządzeniach**. Porównaj te pola z [dokumentacją łączności urządzeń](https://tailscale.com/docs/reference/device-connectivity):

| Pole | Przydatna interpretacja |
|---|---|
| **`UDP`** | Czy test wykrył wychodzącą łączność UDP |
| **`MappingVariesByDestIP`** | Zmienne mapowania zewnętrzne mogą wskazywać trudne przechodzenie przez NAT |
| **`IPv6`** | Czy urządzenie ma użyteczną łączność IPv6 |
| **`PortMapping`** | Czy dostępny jest obsługiwany mechanizm mapowania portów |

**Jedno pole nie daje ostatecznego werdyktu.** Dostępny mechanizm mapowania nie dowodzi, że trasa do konkretnego peera działa. Etykieta przekaźnika nie wskazuje również routera, który wywołał problem. Porównaj oba punkty końcowe i rzeczywiste wyniki pingów.

**NAT operatora** ma znaczenie, gdy translacja po stronie dostawcy znajduje się poza Twoją kontrolą, jak opisano w naszym artykule o [przekierowaniu portów w T-Mobile Home Internet](/articles/t-mobile-home-internet-port-forwarding/). Nie zakładaj, że każde połączenie za NAT-em operatora zachowuje się identycznie.

## Porównaj trzy pary urządzeń

Jeśli to możliwe, użyj **trzeciego zarejestrowanego urządzenia**, aby zebrać więcej dowodów. Poniższy wzorzec jest hipotetyczny, a nie zmierzony:

| Para urządzeń | Zaobserwowana trasa |
|---|---|
| **Laptop do domowego serwera** | DERP |
| **Laptop do innego serwera** | Bezpośrednia |
| **Domowy serwer do innego serwera** | DERP |

**Hipoteza robocza:** w pierwszej kolejności sprawdź sieć domowego serwera, ponieważ obie zaobserwowane trasy z jego udziałem korzystały z przekaźnika. To wskazówka, a nie dowód. Każda para negocjuje połączenie osobno, a serwer porównawczy ma własne warunki sieciowe.

**Następna obserwacja:** zbierz wyniki netcheck na wszystkich trzech urządzeniach i powtórz test laptop–serwer domowy z innej kontrolowanej przez siebie sieci. Jeśli trasa się zmieni, dokładnie zapisz, która sieć uległa zmianie. Nie przypisuj wyniku konkretnej regule zapory przed jej przetestowaniem.

**Ćwiczenie:** połączenie laptop–serwer domowy jest bezpośrednie, ale transfer plików nadal jest wolny. Wyjaśnienie o przekaźniku nie pasuje już do tej obserwacji. Przed zmianą ustawień przekaźnika sprawdź bazowe łącze wysyłające, obciążenie serwera, pamięć masową i działanie aplikacji.

## Wybierz ukierunkowaną zmianę

Zacznij od **testu porównawczego** w innej kontrolowanej przez siebie sieci. Jeśli ten sam peer uzyskuje tam połączenie bezpośrednie, masz przydatny dowód dotyczący pierwotnej trasy sieciowej. Sprawdź ograniczenia UDP i konfigurację NAT, zanim zmienisz niezwiązane ustawienia DNS lub aplikacji.

**Zmień jedną zmienną**, ponownie wykonaj kontrole i zmierz to samo obciążenie. Zapisz kierunek transferu, rozmiar pliku, czas oraz typ połączenia. Dzięki temu odróżnisz poprawę trasy od niezależnej zmiany obciążenia serwera lub pamięci masowej.

**Zmiany zapory** powinny wynikać z zaleceń dla konkretnej platformy i zebranych dowodów. Otwarcie portu aplikacji dla publicznego Internetu samo w sobie nie poprawia trasy transportowej Tailscale. Ogranicz zmiany do wymaganego ruchu i sieci, którą administrujesz. [Zalecenia Tailscale dotyczące zapory](https://tailscale.com/docs/integrations/firewalls).

| Ustalenie | Zmiana warta oceny |
|---|---|
| **Test UDP nie powiódł się** | Sprawdź ograniczenia wychodzącego UDP w tej sieci |
| **Mapowanie różni się zależnie od celu** | Sprawdź NAT na zarządzanym przez Ciebie sprzęcie |
| **Trasa bezpośrednia, wolna aplikacja** | Sprawdź host, łącze bazowe i obciążenie |
| **Działający przekaźnik, akceptowalne działanie** | Zachowaj rozwiązanie i zapisz punkt odniesienia |

*Preferuj zmierzoną poprawę zamiast zmiany ustawień wyłącznie po to, by usunąć etykietę przekaźnika.*

## Oceń przekaźnik równorzędny

**Przekaźnik równorzędny** wymaga odpowiedniego hosta, osiągalnego portu UDP i zasad dostępu zezwalających na użycie. Zarówno przekaźnik, jak i uczestniczące klienty wymagają Tailscale w wersji 1.86 lub nowszej. Przed przeznaczeniem urządzenia sprawdź obsługiwane platformy hosta. [Wymagania przekaźnika równorzędnego](https://tailscale.com/docs/features/peer-relay).

**Lokalizacja decyduje o przydatności.** Urządzenie za tą samą niedostępną granicą sieci nie pomoże innym peerom, dopóki port przekaźnika nie będzie osiągalny.

**Koszt utrzymania:** ktoś musi utrzymywać przekaźnik online, aktualny i odpowiednio wyposażony. Przy sporadycznej administracji i akceptowalnych opóźnieniach porównaj ten obowiązek ze zmierzoną korzyścią. Przy częstych dużych transferach zmierz obciążenie przez proponowany przekaźnik przed jego wdrożeniem.

## Sprawdź wpływ współdzielonego ruchu

**Ruch zagregowany** wymaga uwagi, gdy router podsieci lub węzeł wyjściowy przenosi wiele obciążeń przez DERP. Tailscale opisuje sytuacje, w których duży ruch przez przekaźnik opóźnia ruch wrażliwy na opóźnienia korzystający z tego samego połączenia. [Rozwiązywanie problemów z trudnym NAT-em](https://tailscale.com/docs/reference/troubleshooting/network-configuration/hard-nat-issues).

**Ćwiczenie porównawcze:** obserwuj sesję interaktywną przed dużą kopią zapasową, podczas niej i po niej. Nie zmieniaj pary punktów końcowych i za każdym razem zapisuj trasę. Opóźnienia pojawiające się podczas transferu uzasadniają zbadanie współdzielonego obciążenia, ale nie dowodzą jego dokładnej przyczyny.

**Wybierz następny test** na podstawie obserwacji. Sprawdź nasycenie łącza i obciążenie hosta. Następnie oceń bezpośrednią trasę lub rozdzielenie usług wrażliwych na opóźnienia, jeśli topologia na to pozwala. Nie traktuj objawu DNS jako automatycznego dowodu błędu konfiguracji DNS.

## Czy przekaźnik jest węzłem wyjściowym?

**Węzeł wyjściowy** kieruje ogólny ruch klienta do Internetu przez wybrane urządzenie tailnetu. Przekaźnik przenosi ruch między peerami Tailscale. Wybór węzła wyjściowego nie gwarantuje bezpośredniej trasy do tego urządzenia. [Dokumentacja węzłów wyjściowych](https://tailscale.com/docs/features/exit-nodes).

## Utwórz zapis diagnostyczny

Zapisz **krótki raport przed i po zmianie** dla rzeczywistego problemu:

```text
Data i wersje Tailscale:
Urządzenie źródłowe i docelowe:
Sieci używane przez każde urządzenie:
Początkowa i ustalona trasa połączenia:
Wyniki netcheck z obu stron:
Obciążenie, kierunek i czas:
Pojedyncza przetestowana zmiana:
Wynik ponownego testu:
Decyzja o zachowaniu lub cofnięciu zmiany:
```

**Kryterium ukończenia:** zapis łączy konkretne objawy z obserwacjami, hipotezą i zmierzonym ponownym testem. „Przekaźnik zniknął” to niepełny wynik, jeśli aplikacja nadal działa wolno. „Kopia zapasowa spełnia wymagany czas przez DERP” to prawidłowy wynik, jeśli wymaganie jest jasno określone.

**Traktuj `tailscale netcheck` jako dowód, a nie werdykt.** Polecenie opisuje sieć widzianą przez jedno urządzenie. Ustalona trasa dotyczy pary urządzeń i obciążenia. Przed zmianą ustawień zapory lub NAT zapisz oba punkty końcowe, ostatni wiersz `tailscale status` i pomiar aplikacji.

## Następne kroki

Zapisz trasę do ważnego peera i przetestuj obciążenie przed zmianą ustawień sieciowych. Jeśli osobno chcesz sprawdzić, kto obsługuje infrastrukturę koordynacyjną, przeczytaj [Tailscale a Headscale](/articles/tailscale-vs-headscale-comparison-guide/).
