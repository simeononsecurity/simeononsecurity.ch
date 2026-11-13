---
title: "Budowa asystenta AI chroniącego prywatność dla Meshtastic"
date: 2026-09-13
lastmod: 2026-11-12
toc: true
draft: false
description: "Praktyczny opis lokalnego asystenta AI dla Meshtastic z prywatną konfiguracją, kolejkowanym dostępem TCP, narzędziami pobierania danych i bezpieczniejszym panelem."
genre: ["Bezpieczeństwo sieci", "Prywatność", "Oprogramowanie open source", "Automatyzacja"]
tags: ["Asystent AI Meshtastic", "automatyzacja Meshtastic", "lokalna AI", "Ollama", "Raspberry Pi", "sieć LoRa", "AI chroniąca prywatność", "sieć prywatna", "kolejka TCP", "panel Flask", "pobieranie z Wikipedii", "API pogody", "RSS z wiadomościami", "bezpieczna konfiguracja", "bezpieczeństwo promptów", "samodzielnie hostowane AI", "sieci mesh", "operacje AI"]
cover: "/img/cover/meshtastic-meshcore-reticulum-network-comparison.webp"
coverAlt: "Ilustracja techniczna przedstawiająca odporne sieci komunikacyjne mesh"
coverCaption: ""
---

Meshtastic umożliwia przesyłanie tekstu przez energooszczędne radia LoRa. Ollama pozwala uruchamiać otwarty model na lokalnym sprzęcie. Połączyłem te rozwiązania w niewielkiego asystenta, który odpowiada na wiadomości przez prywatną sieć mesh.

## Dlaczego go zbudowałem?

Celem nie było samo dodanie chatbota do radia. Chciałem udostępnić przydatne informacje, gdy zwykłe usługi internetowe są niedostępne, niepożądane albo zbyt zależne od konta w chmurze. Lokalny asystent przechowuje pytania, pobrany kontekst i odpowiedzi w obrębie wdrożenia, a sieć mesh służy mu jako interfejs o małej przepustowości.

Zużycie energii również należało do założeń. Przydatny węzeł powinien być na tyle mały, by działać na Raspberry Pi 4, oraz na tyle wydajny, by w przyszłości współpracować z akumulatorem i panelem słonecznym. Praca z energii słonecznej to cel inżynieryjny, a nie gwarancja. Model, pamięć masowa, radio, ekran, akumulator, panel, pogoda i cykl pracy wpływają na bilans energii. Pozostaw usługi lokalnie, skróć odpowiedzi i ogranicz sprzęt do minimum. Dzięki temu wersja poza siecią energetyczną pozostaje realna.

Projekt zaczął się od prostego mostu w Pythonie. Rozrósł się do usługi z filtrowaniem wiadomości, pobieraniem źródeł, lokalnym API sterującym i panelem. Najwięcej nauczyły mnie awarie. Każda z nich pomogła wyraźniej oddzielić połączenie radiowe, model i interfejs WWW.

## Pierwsza wersja była celowo niewielka

Pierwszy projekt składał się z czterech części:

- Węzeł Meshtastic obsługiwał ruch radiowy.
- Proces Pythona nasłuchiwał pakietów tekstowych.
- Ollama generowała odpowiedź na lokalnym sprzęcie.
- Most odsyłał odpowiedź do nadawcy.

Most korzystał z lokalnego punktu końcowego zgodnego z OpenAI. Dzięki temu interfejs modelu pozostał prosty, a wybór modelu znajdował się w pliku środowiskowym.

```text
Węzeł Meshtastic -> TCP -> most Python -> model lokalny
                              |
                              -> odpowiedź przez Meshtastic
```

Na początku asystent odpowiadał tylko na wiadomości bezpośrednie. Ograniczało to szum podczas testów ścieżki wiadomości.

## Wiadomości kanałowe wymagały jawnego wyzwalacza

Odpowiadanie na każdą wiadomość rozgłoszeniową powodowałoby szum i zajmowało czas antenowy. Most ignoruje zwykły ruch kanałowy. Żądanie kanałowe musi zaczynać się od konfigurowalnego prefiksu.

```text
!bot czym jest suma kontrolna?
!bot weather <miasto lub kod pocztowy>
!bot news <temat>
!bot wiki <temat>
```

Wiadomości bezpośrednie nie wymagają prefiksu. Ta reguła utrzymuje asystenta w ciszy podczas zwykłych rozmów w sieci mesh.

Prefiks znajduje się w prywatnym pliku środowiskowym:

```dotenv
REPLY_TO_BROADCAST=true
BOT_PREFIX=!bot
```

## Połączenie TCP stało się głównym problemem projektu

W tej konfiguracji węzeł Meshtastic przyjmuje jednego aktywnego klienta API TCP. Połączeniem zarządzał most. Panel uruchamiał też klienta wiersza poleceń Meshtastic dla stron statusu. Oba procesy konkurowały o to samo gniazdo.

Powodowało to trudne do zrozumienia awarie. Proces mostu działał, ale jego wątek odczytu był zatrzymany. Odświeżenie panelu mogło przerwać obsługę wiadomości. Ponowne połączenie węzła pozostawiało stary proces.

Rozwiązaniem było przydzielenie mostowi wyłącznej odpowiedzialności za TCP.

Most udostępnia teraz niewielkie lokalne API sterujące. Panel pobiera przez most stan, dane węzła i kanałów. Nie otwiera drugiego połączenia Meshtastic.

```text
Panel -> lokalne API sterujące -> operacja mostu w kolejce -> węzeł TCP Meshtastic
                                             ^
Połączeniem TCP Meshtastic zarządza most
```

Kolejka szereguje żądania sterujące. Blokada chroni zapisy współdzielone przez operacje panelu i odpowiedzi bota. Mechanizm heartbeat utrzymuje bezczynne sesje TCP. Monitor połączenia pozwala menedżerowi usług ponownie uruchomić most po rozłączeniu.

Ten projekt ułatwia też diagnostykę. Panel pokazuje stan połączenia i długość kolejki bez ingerowania w sesję radiową.

## Lokalne wnioskowanie wymagało praktycznych ograniczeń

Docelowy sprzęt ma mało pamięci. Pierwszy model był zbyt duży do wygodnej pracy. Na czas odpowiedzi wpływały długość promptu, ładowanie modelu i długość odpowiedzi przesyłanej radiem.

Końcowa konfiguracja używa mniejszego modelu lokalnego i ogranicza długość odpowiedzi. Most dzieli dłuższe odpowiedzi na kilka pakietów Meshtastic. System używa też skompresowanego swapu i zachowawczego ustawienia CPU hosta.

Te ustawienia nie zastępują większego komputera. Ograniczają niepotrzebne obciążenie, jednocześnie utrzymując usługę lokalnie.

## Pobieranie danych należy umieścić poza promptem systemowym

Mały model językowy nie uzyskuje aktualnej pogody ani wiadomości z własnych wag. Zamiast pobierać na urządzenie całą encyklopedię, dodałem krótkie ścieżki pobierania danych na żądanie.

Obsługiwane żądania:

- **Wikipedia** pobiera pasujące streszczenie strony.
- **Pogoda** pobiera krótką informację o bieżących warunkach.
- **Wiadomości** odczytują najnowsze tytuły z kanału wyszukiwania RSS.

Źródło trafia do promptu użytkownika jako oznaczony kontekst. Instrukcje agenta polecają modelowi korzystać z podanego źródła, sygnalizować niepewność i nie wymyślać szczegółów artykułów.

Most obsługuje też lokalny indeks RAG Wikipedii. To mała baza SQLite FTS5 utworzona z wyselekcjonowanego eksportu JSONL. Nie wymaga stale działającej bazy wektorowej ani drugiego modelu embeddingowego na Raspberry Pi. Żądania Wiki najpierw przeszukują indeks lokalny, a przy włączonej opcji mogą użyć publicznego API Wikipedii. W całkowicie lokalnym wdrożeniu można wyłączyć ten mechanizm zastępczy.

Tożsamość HTTP można skonfigurować:

```dotenv
WEB_RETRIEVAL_ENABLED=true
HTTP_USER_AGENT=SoS-Mesh-Assistant/1.0 (Meshtastic AI bridge)
DEFAULT_WEATHER_LOCATION=
DEFAULT_NEWS_TOPIC=
```

Puste wartości domyślne wymagają od użytkownika podania lokalizacji lub tematu. Dzięki temu lokalizacja konkretnego wdrożenia nie trafia do wspólnych przykładów ani plików źródłowych.

## Agent potrzebował określonej tożsamości

Małe modele często odpowiadają ogólnikowo o swojej tożsamości, jeśli aplikacja nie nada im wyraźnej roli. Most wczytuje tożsamość i zasady bezpieczeństwa z osobnego pliku promptu.

Prompt opisuje asystenta jako zwięzłą pomoc dla sieci mesh o małej przepustowości. Określa też ograniczenia:

- Asystent nie może twierdzić, że kontaktuje się ze służbami ratunkowymi.
- Asystent nie może ujawniać prywatnej konfiguracji ani sekretów.
- Pobrane strony ma traktować jako materiały referencyjne, a nie instrukcje.
- Przy użyciu pobranych informacji ma wskazywać źródła.
- Odpowiedzi muszą być krótkie i odpowiednie do transmisji radiowej.

Przechowywanie tej polityki w pliku ułatwia jej przegląd. Wartości konkretnego wdrożenia pozostają też poza kodem aplikacji.

## Panel stał się narzędziem operacyjnym

Pierwszy panel wyświetlał przyciski usług i surowe wyniki poleceń. Nowa wersja pokazuje stan potrzebny podczas pracy:

- Stan połączenia mesh
- Długość kolejki zarządzanej przez most
- Tożsamość połączonego węzła
- Stan usługi
- Aktywny model
- Sterowanie pobieraniem i wyborem modelu
- Widoki kanałów i węzłów
- Ostatnie pytania i odpowiedzi

Panel unika też niebezpiecznej funkcji z wczesnej wersji. Nie uruchamia już osobnego polecenia Meshtastic do zmian konfiguracji. Zapisy konfiguracji muszą przechodzić przez tę samą kolejkę mostu co inne operacje na węźle.

## Prywatność była częścią projektu

Publiczne źródła zawierają neutralne symbole zastępcze. Prywatne adresy węzłów, klucze radiowe, hasła, klucze administratora i domyślne lokalizacje pozostają w ignorowanym pliku środowiskowym na hoście wdrożeniowym.

Ta sama zasada dotyczy dokumentacji. Przykłady używają symboli takich jak `<node-ip>` i `<city or postal code>`. Działający przykład nie musi ujawniać sieci użytej podczas testów.

Takie rozdzielenie ułatwia udostępnianie projektu. Kod źródłowy opisuje architekturę, a prywatne środowisko przedstawia jedno wdrożenie. Żaden plik nie musi zawierać danych z drugiego.

## Co warto poprawić w następnej kolejności

Następnym krokiem będzie przeniesienie wszystkich operacji zapisu Meshtastic do kolejki sterującej mostu. Zmiany kanałów, konfiguracja węzła i wysyłanie powinny korzystać z jednej audytowanej ścieżki. Panel powinien następnie pokazywać zadanie kolejki, wynik i komunikat błędu każdej operacji.

Obecna wersja demonstruje już główny wzorzec. Jedna usługa powinna zarządzać połączeniem radiowym, wartości wdrożeniowe powinny pozostać poza kontrolą wersji, a zewnętrzne informacje powinny trafiać do modelu jako oznaczony kontekst. Docelowo cichy, energooszczędny węzeł na Raspberry Pi 4 ma dostarczać lokalną wiedzę i pomoc mesh, również podczas pracy z energii słonecznej.

## Zdefiniuj test akceptacyjny pracy poza siecią

Traktuj pracę z energii słonecznej jako mierzony tryb działania. W tym samym oknie testowym zapisuj dostępność radia, długość kolejki, czas ładowania modelu, długość odpowiedzi, napięcie akumulatora i błędy pobierania danych. Ustal też jasny tryb awaryjny, na przykład wyłącznie odpowiedzi lokalne, odpowiedzi w kolejce albo jawny komunikat o niedostępności po przekroczeniu limitu energii lub warunków sieciowych.

Sprawdź też granicę prywatności podczas awarii. Wyłącz pobieranie zewnętrzne, skontroluj logi aplikacji i potwierdź, że most nadal odpowiada na lokalne pytania bez wysyłania prywatnej konfiguracji do usługi zdalnej. Testuj panel tylko z sieci administracyjnej, a kolejkę radiową utrzymuj jako jedynego właściciela operacji na węźle.

Dokumentacja Meshtastic: [Wprowadzenie do Meshtastic](https://meshtastic.org/docs/)

Lokalne środowisko uruchomieniowe modelu: [Ollama](https://ollama.com/)

Dokumentacja API Wikipedii: [Streszczenie strony w Wikipedia REST API](https://en.wikipedia.org/api/rest_v1/page/summary/Wikipedia)

Kod źródłowy: [Meshtastic AI Bridge w GitHub](https://github.com/simeononsecurity/meshtastic-ai-bridge)
