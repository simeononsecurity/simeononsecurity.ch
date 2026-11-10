---
title: "Jakie modele AI działają na Raspberry Pi 4 lub 5?"
date: 2026-09-20
lastmod: 2026-11-07
toc: true
draft: false
description: "Wykorzystaj wyniki pomiarów Raspberry Pi 4 i 5, aby dobrać lokalne modele językowe do dostępnej pamięci, szybkości i zadania, od małych modeli LFM2.5 po większe opcje 3B."
genre: ["Raspberry Pi", "Sztuczna inteligencja", "Samodzielny hosting"]
tags: ["Raspberry Pi 4", "Raspberry Pi 5", "lokalna AI", "małe modele językowe", "Ollama", "GGUF", "LFM2.5", "Qwen2.5", "Gemma 3", "kwantyzacja modeli", "edge AI"]
cover: "/img/cover/raspberry-pi-4-5-local-ai-models.webp"
coverAlt: "Dwa komputery Raspberry Pi na ciemnym biurku, nad nimi niebieskie i bursztynowe ilustracje sieci neuronowych"
coverCaption: "Ilustracja lokalnych modeli AI działających na sprzęcie Raspberry Pi."
---

Raspberry Pi może lokalnie uruchomić użyteczny model językowy, ale model musi zmieścić się w pamięci płytki i odpowiadać w czasie akceptowalnym dla aplikacji. Raspberry Pi 4 z 2 GB najlepiej nadaje się do modeli z mniej więcej miliardem parametrów lub mniej. Raspberry Pi 5 z 8 GB wygodnie obsługuje kompaktowe modele 1B–3B i może załadować niektóre większe modele po kwantyzacji, ale wiąże się to ze znacznymi kompromisami.

Samodzielnie przetestowaliśmy te modele w Ollama na **Pi 4B z 2 GB** i **Pi 5 z 8 GB**, oba z kartą microSD. Pomiary w tabelach wykorzystują te same pięć krótkich promptów asystenta, prompt systemowy, stały seed i limit wyjścia 140 tokenów. Przed każdym testem wyładowywaliśmy inne modele. Mierzyliśmy czas zimnego ładowania, czas do pierwszego widocznego tokenu, całkowity czas odpowiedzi, szybkość generowania i szczytową pamięć rezydentną. Były to jednorazowe testy zadań wymagających krótkich odpowiedzi, więc wyniki pokazują przykładowe wymagania sprzętowe, a nie uniwersalną szybkość lub jakość odpowiedzi. [Procesor Cortex-A76 i dostępne konfiguracje pamięci Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) różnią się też znacząco od [platformy Cortex-A72 w Pi 4](https://pip-assets.raspberrypi.com/categories/545-raspberry-pi-4-model-b/documents/RP-008341-DS-1-raspberry-pi-4-datasheet.pdf).

## Jakie typy modeli mają sens

| Typ modelu | Przykłady z pomiarów | Praktyczne zastosowanie |
|---|---|---|
| Małe modele tekstowe, około 230M–600M parametrów | LFM2.5-230M, LFM2.5-350M, Qwen2.5-0.5B | Krótkie lokalne polecenia, podsumowania i odpowiadanie na ograniczone pytania; najlepszy punkt wyjścia dla Pi 4 z 2 GB |
| Kompaktowe modele tekstowe, około 1B–2B | LFM2.5-1.2B, Qwen2.5-1.5B, Gemma 3 1B, MiniCPM5-1B | Więcej miejsca na niuanse instrukcji w Pi 5 lub Pi 4 z większą pamięcią, lecz wolniejsze odpowiedzi niż w najmniejszych modelach |
| Kwantyzowane modele tekstowe 3B–4B | Qwen2.5-3B, Llama 3.2 3B, Gemma 3 4B | Bardziej zaawansowani kandydaci dla Pi 5 z 8 GB, jeśli kilka sekund oczekiwania na odpowiedź jest akceptowalne |
| Większe modele rzadkie lub hybrydowe | LFM2.5 8B | Technicznie działa na testowanym Pi 5 z 8 GB, ale zużywa dużo pamięci i długo ładuje się po raz pierwszy |

Są to wyniki **generowania tekstu**. Nie określają wydajności generowania obrazów, rozpoznawania mowy, widzenia komputerowego ani trenowania. „Działa” oznacza więcej niż samo zmieszczenie pliku modelu na karcie: pamięci RAM potrzebują również środowisko uruchomieniowe, pamięć podręczna kontekstu, system operacyjny i inne usługi. Kwantyzacja zmniejsza plik wag, lecz może obniżyć jakość odpowiedzi, szczególnie przy skrajnych ustawieniach, takich jak wagi 1-bitowe.

### Co mierzą nasze wyniki

Benchmark wysyłał do interfejsu czatu Ollama krótkie prompty faktograficzne, dotyczące bezpieczeństwa procedur, kontekstu z wyszukiwania, pogody oraz pomocy. Każdy model otrzymał ten sam zestaw promptów i seed. Przed pomiarem wyładowywaliśmy model, aby kolejne żądanie obejmowało zimne ładowanie. Podany **czas rzeczywisty** obejmuje całe żądanie, natomiast **tokeny na sekundę** opisują tylko generowanie odpowiedzi. Mierzyliśmy też pierwszy *widoczny* token, bo model może przez pewien czas rozumować, zanim pokaże odpowiedź.

Pamięć mierzyliśmy, próbkując dostępną pamięć RAM i swap Pi oraz pamięć rezydentną Ollama i procesu inferencji podczas każdego żądania. Podane wartości **RSS** oznaczają pamięć rezydentną procesu, a nie całkowite zapotrzebowanie hosta. Strony plików, system operacyjny, przeglądarka lub inna lokalna usługa mogą wymusić swap, nawet gdy model nominalnie się mieści. Tabele zawierają wyniki pierwotnego testu z pięcioma promptami, wykonanego raz. Później rozszerzyliśmy test o prompt informacyjny i kontrole reguł odpowiedzi. Te kontrole wyjaśniają, co warto sprawdzić, ale wcześniejsze czasy nie są wynikami testu zgodności z sześcioma promptami.

Liczba tokenów na sekundę i liczba parametrów nie są oceną jakości. Model może szybko tworzyć tekst, a mimo to pominąć żądane źródło, przekroczyć limit słów lub wygenerować niedokończone zdanie. Porównywalibyśmy modele na promptach, których rzeczywiście zamierzamy używać, a przed wyborem sprawdzilibyśmy odpowiedzi.

## Raspberry Pi 4: wybieraj najmniejsze modele

Testowane Pi 4 z 2 GB miało niewielki zapas pamięci. Najmniejsze modele LFM2.5 ukończyły wszystkie pięć promptów, podobnie jak `qwen2.5:0.5b`. To rozsądny wybór do krótkich odpowiedzi offline lub małego lokalnego asystenta.

| Model | Plik modelu | Zmierzona szybkość generowania | Średni czas odpowiedzi | Zaobserwowana pamięć lub wynik |
|---|---:|---:|---:|---|
| LFM2.5-230M, import GGUF | 0.25 GB | 12.8 tokena/s | 7.2 s | Szczyt RSS 383 MB; 5/5 promptów |
| LFM2.5-350M, import GGUF | 0.38 GB | 8.6 tokena/s | 8.6 s | Szczyt RSS 516 MB; 5/5 promptów |
| `qwen2.5:0.5b` | 0.40 GB | 8.0 tokena/s | 9.7 s | 5/5 promptów; dostępny bezpośrednio w Ollama |
| MiniCPM5-1B, import GGUF, rozumowanie wyłączone | 0.69 GB | 5.9 tokena/s | 12.2 s | Szczyt RSS 883 MB; 5/5 promptów |
| MiniCPM5-1B, import GGUF, domyślne rozumowanie | 0.69 GB | 5.7 tokena/s | 33.3 s | Tylko 1/5 promptów dał użyteczną widoczną odpowiedź |
| `qwen3:0.6b`, domyślne rozumowanie | 0.52 GB | 6.4 tokena/s | 40.4 s | Jedna pusta odpowiedź; płytka uruchomiła się ponownie |
| `granite4:350m` | 0.71 GB | 4.6 tokena/s | 15.5 s | 913 MB RSS, bez swapu i restartu; wolny, ale stabilny |
| `gemma3:1b` | 0.82 GB | 4.0 tokena/s | 30.7 s | Intensywne użycie swapu; płytka zrestartowała się podczas testów |
| `qwen3.5:0.8b` | 1.04 GB | — | — | Nie ukończył zadania; płytka zrestartowała się |

Wyniki Pi 4 szczególnie zależą od pozostałego obciążenia systemu. Podczas testów większych modeli zaobserwowaliśmy restarty płytki, w tym nieukończony test `qwen3.5:0.8b`. To wynik naszej konfiguracji 2 GB, a nie stwierdzenie, że każdy Pi 4 lub każdy model 1B spowoduje restart. Pi 4 z 4 GB lub 8 GB ma więcej pamięci, ale jego procesor nadal będzie wykonywał inferencję wolniej niż testowane Pi 5. Nie testowaliśmy bezpośrednio tych wariantów Pi 4 z większą pamięcią.

We wczesnym teście Pi 4 wyniki wyglądały znacznie gorzej niż w końcowych pomiarach: około 625 MB tymczasowych plików GGUF znajdowało się w `/tmp` opartym na RAM, pozostawiając tylko około 500–600 MB wolnej pamięci i przenosząc setki megabajtów do swapu. Po przeniesieniu tych plików na trwały nośnik wyniki małych modeli powyżej lepiej pokazywały użycie pamięci przez inferencję. Na płytce z 2 GB nawet *miejsce pobrania pliku* może zniekształcić benchmark.

**Rekomendacja:** Naszym domyślnym modelem dla tej płytki 2 GB jest importowany LFM2.5-350M. Pozostał stabilny przy **516 MB RSS**, zostawił około **1 GB dostępnego RAM** i spełnił **5/6** reguł odpowiedzi w teście zgodności Pi 4. W powtarzanych testach Pi 5 pomijał nazwy źródeł, więc aplikacje wymagające atrybucji powinny to sprawdzać. Wybierz LFM2.5-230M, jeśli najbardziej liczą się opóźnienia i zapas pamięci: był szybszy i mniejszy, ale w jednej odpowiedzi na temat medyczny błędnie przekształcił „nudności lub wymioty” w „nudności/korzystanie z respiratora”. Ten błąd merytoryczny czyni go słabszym wyborem domyślnym dla odpowiedzi dotyczących bezpieczeństwa lub zdrowia mimo wyższego powtarzanego wyniku mechanicznej zgodności. Wybierz `qwen2.5:0.5b`, jeśli potrzebujesz modelu z [rejestru Ollama](https://ollama.com/library/qwen2.5/tags), ale uwzględnij słabsze wykonywanie instrukcji. `granite4:350m` był stabilny, ale wolniejszy i bardziej pamięciożerny; MiniCPM5-1B nadaje się tylko wtedy, gdy klient wyłącza rozumowanie. Unikaj Gemma 3 1B i Qwen3.5 0.8B na tej konkretnej konfiguracji 2 GB, ponieważ nasze testy wywołały restarty.

## Raspberry Pi 5: większy wybór kosztem szybkości

Pi 5 z 8 GB obsłużyło wszystkie **25 modeli** w naszym benchmarku szybkości i pamięci. Tabela zawiera każdy pomiar, również modele, których nie polecamy do tej pracy z krótkimi odpowiedziami. Znak † oznacza import GGUF. „Think off” określa ustawienie użyte w teście szybkości; osobny test zgodności nie zawsze korzystał z tego ustawienia.

| Model | Plik GB | Wyjście tok/s | Odpowiedź s | Szczyt RSS MB | Ocena krótkich odpowiedzi |
|---|---:|---:|---:|---:|---|
| `lfm2.5-230m` † | 0.25 | 45.0 | 1.8 | 446 | Najmniejsze opóźnienie; 78% powtarzanej zgodności |
| `bonsai-1.7b` †, Q1_0 | 0.25 | 15.3 | 8.2 | 871 | Pomiń: wagi 1-bitowe i 3/6 zgodności w pojedynczym teście |
| `lfm2.5-350m` † | 0.38 | 30.0 | 2.1 | 581 | Szybki, ale pominął źródło w 5/18 powtórzeń |
| `qwen2.5:0.5b` | 0.40 | 28.4 | 3.6 | 675 | Łatwy w użyciu z rejestru; 61% powtarzanej zgodności |
| `qwen3:0.6b`, rozumowanie wyłączone | 0.52 | 23.0 | 4.3 | 1,069 | Warunkowo: 4/6 zgodności, ustawienie rozumowania ma znaczenie |
| `bonsai-4b` †, Q1_0 | 0.57 | 6.8 | 18.1 | 1,343 | Eksperymentalny model 1-bitowy; wynik 6/6 z jednego testu niepotwierdzony |
| `minicpm5-1b` †, rozumowanie wyłączone | 0.69 | 18.4 | 5.1 | 869 | Warunkowo: domyślne rozumowanie dawało puste odpowiedzi |
| `granite4:350m` | 0.71 | 12.1 | 6.6 | 892 | Pasuje, ale jest wolniejszy i większy niż małe LFM2.5 |
| `lfm2.5-1.2b` † | 0.73 | 15.5 | 4.7 | 967 | Najlepszy całościowo dla naszej pracy; 89% powtarzanej zgodności |
| `llama3.2:1b-instruct-q4_K_M` | 0.81 | 13.0 | 7.5 | 1,244 | Alternatywa z rejestru; 5/6 w teście zgodności |
| `gemma3:1b` | 0.82 | 11.2 | 10.9 | 1,262 | Najlepsza powtarzana zgodność wśród modeli z rejestru: 83% |
| `qwen2.5:1.5b-instruct-q4_K_M` | 0.99 | 10.3 | 9.4 | 1,361 | 4/6 zgodności; Gemma 3 1B lepiej przestrzegała reguł |
| `qwen3.5:0.8b`, rozumowanie wyłączone | 1.04 | 8.8 | 12.2 | 1,592 | 0/6 przy domyślnym rozumowaniu; unikaj bez kontroli nad nim |
| `spark-x2.5-1.7b` †, rozumowanie wyłączone | 1.11 | 9.7 | 9.4 | 1,542 | 0/6 przy domyślnym rozumowaniu; unikaj bez kontroli nad nim |
| `qwen3:1.7b`, rozumowanie wyłączone | 1.36 | 8.1 | 12.4 | 1,867 | Warunkowo; więcej pamięci i opóźnienia niż mniejsze opcje |
| `minicpm5-2b` †, rozumowanie wyłączone | 1.56 | 7.7 | 10.9 | 1,787 | Warunkowo; 5/6 w pojedynczym teście, dodatkowe wypunktowania |
| `qwen2.5:3b-instruct-q4_K_M` | 1.93 | 5.2 | 14.7 | 2,366 | Model 3B do próby; 5/6 w pojedynczym teście |
| `granite4:micro-h` | 1.94 | 3.9 | 23.7 | 2,486 | Pomiń przy pracy interaktywnej: powolne dekodowanie |
| `llama3.2:3b-instruct-q4_K_M` | 2.02 | 5.5 | 18.6 | 2,831 | Alternatywa 3B; brak raportu z testu zgodności |
| `granite4:micro` | 2.10 | 5.3 | 17.9 | 2,679 | Pasuje, ale odpowiedzi są wolniejsze niż w mniejszych modelach |
| `qwen3.5:2b`, rozumowanie wyłączone | 2.74 | 5.0 | 16.1 | 3,627 | Wysokie zużycie pamięci i opóźnienie; brak raportu z testu zgodności |
| `gemma3:4b` | 3.34 | 3.9 | 30.3 | 4,267 | Pomiń przy responsywnych odpowiedziach; 14.3 s do pierwszego tokenu |
| `ling-3.0-tiny` †, rozumowanie wyłączone | 4.82 | 9.9 | 19.4 | 5,071 | Duże zużycie pamięci; 5/6 w pojedynczym teście z błędem ugruntowania |
| `lfm2.5:8b`, rozumowanie wyłączone | 5.16 | 8.7 | 54.6 | 5,317 | Mieści się ciasno; zimne ładowanie 34.4 s i za długie odpowiedzi |
| `gemma3n:e2b` | 5.62 | 6.1 | 25.9 | 5,261 | Pomiń: presja swapu równolegle z innymi usługami Pi |

† Import GGUF. Czas odpowiedzi i pamięć pochodzą z testu szybkości z pięcioma promptami na Pi 5; wyniki zgodności pochodzą z osobnych testów z sześcioma promptami. Brak wyniku zgodności oznacza, że nie wykazano przestrzegania reguł odpowiedzi.

Małe modele LFM2.5 były najszybsze dla tej pracy z krótkimi odpowiedziami. Wersja 1.2B jest praktycznym kompromisem na testowanym Pi 5. Gemma 3 1B to alternatywa z rejestru, która w naszych późniejszych testach lepiej przestrzegała reguł niż Qwen2.5 1.5B. Model 3B może być wart wolniejszego generowania w przypadku promptów wymagających większej pojemności, ale same czasy nie dowodzą, który model odpowiada najlepiej.

Czas zimnego ładowania i opóźnienie pierwszego tokenu zmieniają wrażenia z używania. LFM2.5-230M ładował się na Pi 5 około **0.21 sekundy**, a pierwszy widoczny token generował po **0.37 sekundy**. Qwen2.5 1.5B potrzebował **2.59 sekundy** na ładowanie i **3.66 sekundy** do pierwszego widocznego tokenu; Qwen2.5 3B odpowiednio **5.60** i **7.97 sekundy**. Przy okazjonalnym pytaniu te opóźnienia mogą mieć większe znaczenie niż szybkość generowania po jego rozpoczęciu. Dla stale załadowanego modelu mają mniejsze znaczenie, ale model zajmuje pamięć między żądaniami.

Inni zmierzeni kandydaci pokazują, dlaczego nie oceniamy modeli wyłącznie na podstawie liczby parametrów. Przy wyłączonym rozumowaniu `qwen3:0.6b` osiągnął na Pi 5 **23.0 tokena/s** przy **1,069 MB RSS**, a importowany MiniCPM5-1B osiągnął **18.4 tokena/s** przy **869 MB RSS**. `granite4:350m` wymagał pobrania **0.71 GB** i generował **12.1 tokena/s**, mimo oznaczenia 350M. Opakowanie modelu i architektura zmieniają zależność między nazwą, rozmiarem pliku, pamięcią i szybkością.

Jeśli klient potrafi niezawodnie wysyłać `think: false`, Qwen3 0.6B i MiniCPM5-1B warto przetestować jako alternatywy dla LFM2.5. MiniCPM5-2B, Qwen3 1.7B i Spark-X2.5 1.7B również działały na Pi 5, ale nie oferowały wyraźnej przewagi w szybkości i pamięci nad naszymi głównymi wyborami. Test zgodności używał domyślnego rozumowania dla MiniCPM5-1B i Spark-X2.5; ich pustych odpowiedzi nie należy przedstawiać jako wyników testów szybkości z wyłączonym rozumowaniem. Z kolei szybki wynik z wyłączonym rozumowaniem nie dowodzi, że bridge pomijający tę flagę otrzyma użyteczną odpowiedź.

Jeśli prostota instalacji jest ważniejsza niż surowa szybkość, Gemma 3 1B i Llama 3.2 1B to wiarygodne modele z rejestru dla Pi 5 z 8 GB. Gemma 3 1B przestrzegała testowanych reguł odpowiedzi w **15/18** powtórzonych odpowiedzi. Llama 3.2 1B przeszła **5/6** w jednym teście, więc ocena jej zgodności jest mniej pewna. Qwen2.5 1.5B ładował się i odpowiadał szybciej niż Gemma 3 1B w naszym teście czasowym, ale w pojedynczym teście zgodności spełnił tylko **4/6** reguł. Wybierz model na podstawie wymagań, które liczą się w twoich promptach.

Do okazjonalnych, dłuższych lub trudniejszych promptów tekstowych kwantyzowane Qwen2.5 3B i Llama 3.2 3B to modele 3B o umiarkowanym zużyciu pamięci na naszym Pi 5 z 8 GB. Zmierzyliśmy ich szybkość i pamięć; Qwen2.5 3B uzyskał **5/6** w pojedynczym teście zgodności, a porównywalnego testu dla Llama 3.2 3B nie opublikowaliśmy. Więcej parametrów to powód, aby je *sprawdzić* w zadaniach, w których mniejsze modele sobie nie radzą, a nie dowód, że odpowiadają lepiej. Granite 4 Micro i Micro-H, Qwen3.5 2B, Gemma 3 4B, Ling-3.0-tiny oraz Gemma 3n E2B zmieściły się lub załadowały w naszych testach Pi 5, ale przy krótkich odpowiedziach oferowały mniej atrakcyjne opóźnienie, zapas pamięci lub niezawodność.

Dwa modele Bonsai pokazują koszt skrajnej kwantyzacji. Ich pliki Q1_0 były zaskakująco małe jak na nazwy z 1.7B i 4B parametrów, ale model 1.7B spełnił tylko **3/6** reguł odpowiedzi. Model 4B zaliczył pojedynczy test z sześcioma promptami, lecz potrzebował **18.1 sekundy** na odpowiedź i nie został ponownie sprawdzony pod kątem zgodności. Traktujemy oba jako eksperymenty, a nie domyślne zalecenia, zwłaszcza gdy liczy się jakość odpowiedzi.

Wynik LFM2.5 8B wymaga kontekstu: jego hybrydowa konstrukcja wykorzystuje mniej aktywnych parametrów na token, więc szybkość dekodowania przewyższyła wyniki gęstych modeli 3B. Zimne ładowanie z microSD nadal trwało **34.4 sekundy**, a pamięć rezydentna przekroczyła **5.3 GB**. To pokazuje, co się zmieści, ale nie jest wygodnym domyślnym wyborem dla Pi, na którym działają inne usługi. Testowany `gemma3n:e2b` również zużywał około 5.3 GB pamięci rezydentnej i powodował swap równolegle z pozostałymi usługami hosta.

Test LFM2.5 8B wykorzystał też cały limit **140 tokenów**, zamiast udzielić krótkiej odpowiedzi. Test Gemma 3 4B wymagał **14.3 sekundy** do pierwszego tokenu i **30.3 sekundy** na całą odpowiedź. Oba modele można załadować na tym Pi 5, ale w naszych testach żaden nie zachowywał się jak responsywny mały asystent. Mały model z odpowiednio krótką odpowiedzią może lepiej służyć interfejsowi radiowemu lub poleceniowemu niż większy model z szybszym dekodowaniem na papierze.

## Pamięć, rozumowanie i format modelu

Przybliżenie oparte na naszych pomiarach to **rozmiar pobieranego modelu × 1.4** jako oszacowanie rezydentnej pamięci inferencji. To tylko praktyczna wskazówka: długość kontekstu, ustawienia runtime, architektura modelu i inne procesy mogą zmienić zapotrzebowanie. Podczas generowania sprawdzaj dostępną pamięć, na małym hoście ładuj tylko jeden model naraz i zostaw miejsce dla systemu operacyjnego. Płytka z 4 GB może zacząć od małych lub kompaktowych modeli, ale nasze rekomendacje dla 4 GB są ekstrapolacjami, a nie bezpośrednimi testami wariantów 4 GB.

Na przykład plik LFM2.5-1.2B o rozmiarze 0.73 GB odpowiadał około **967 MB RSS** na Pi 5, a plik Qwen2.5 1.5B o rozmiarze 0.99 GB osiągnął **1,361 MB RSS**. Ta reguła sprawdza się dość dobrze dla tych modeli, ale nie jest twardym limitem. Jeśli Pi uruchamia też interfejs, indeks wyszukiwania, lokalną bibliotekę lub inną usługę w tle, uwzględnij więcej pamięci niż zmierzone zużycie samego modelu. Obserwuj swap podczas rzeczywistego żądania; model, który wprawdzie się ładuje, ale stale korzysta ze swapu, nie pasuje praktycznie.

Niektóre modele generują wewnętrzny blok rozumowania przed widoczną odpowiedzią. W naszych testach `qwen3:0.6b` na Pi 4 z 2 GB potrzebował znacznie więcej czasu, zanim pojawił się widoczny tekst. MiniCPM5-1B z domyślnym ustawieniem rozumowania udzielił użytecznej odpowiedzi tylko na jeden z pięciu promptów, a po wyłączeniu rozumowania na pięć z pięciu. Przy krótkim limicie odpowiedzi ustaw `think: false` w zgodnym żądaniu API Ollama albo wybierz model, który domyślnie nie rozumuje. To ustawienie dotyczy obsługiwanych modeli i klientów, nie jest uniwersalnym przełącznikiem szybkości.

To rozróżnienie ma znaczenie, bo limit tokenów może obejmować tokeny przeznaczone na rozumowanie, nawet gdy użytkownik nie widzi odpowiedzi. Na Pi 4 `qwen3:0.6b` ze standardowym rozumowaniem odpowiadał średnio po **40.4 sekundy**, a jeden prompt zwrócił pustą widoczną odpowiedź. MiniCPM5-1B potrzebował średnio **33.3 sekundy** z ustawieniem domyślnym i **12.2 sekundy** po wyłączeniu rozumowania. W testach Pi 5 wyłączyliśmy też rozumowanie dla Qwen3, Qwen3.5, MiniCPM5, Ling-3.0 i Spark-X2.5 tam, gdzie wskazują to nasze dane. Porównuj modele z dokładnie takim ustawieniem rozumowania, jakiego użyje klient.

### Sprawdź, czy odpowiedź jest użyteczna

W naszej pracy z krótkimi odpowiedziami dla asystenta mesh kontrakt odpowiedzi jest równie ważny jak szybkość: najwyżej **90 słów**, maksymalnie **trzy wypunktowania**, zwykły tekst, ukończone zdanie oraz wykorzystanie dostarczonego kontekstu z podaniem źródła. Bridge dzieli tekst na fragmenty po **180 znaków**. Długa odpowiedź zajmuje więcej czasu antenowego, nawet jeśli model wygenerował ją szybko.

Późniejsza wersja benchmarku sprawdza puste odpowiedzi, limit słów zależny od promptu, nadmiar wypunktowań, tabele lub bloki kodu Markdown, niedokończone zakończenie, brak terminów z dostarczonego kontekstu i brak nazwy źródła. Gdy ocenialiśmy odpowiedzi według promptu systemowego wdrożonego asystenta, małe modele regularnie naruszały te reguły. Najpoważniejsze problemy to **puste odpowiedzi**, gdy rozumowanie zużywało limit tokenów, a następnie odpowiedzi ignorujące pobrany kontekst lub pomijające źródło. Przekroczenie limitu słów lub zbyt wiele wypunktowań nadal dawało widoczny tekst, ale marnowało czas antenowy. Są to kontrole mechaniczne, a nie substytut przeczytania odpowiedzi: nie potwierdzają poprawności faktów ani trafności porad dotyczących bezpieczeństwa.

#### Powtarzane wyniki zgodności na Pi 5

Najpierw uruchomiliśmy sześć promptów raz na model z limitem **220 tokenów** i wdrożonym promptem systemowym. Obiecujące modele testowaliśmy potem jeszcze dwa razy z innym seedem, uzyskując **18 odpowiedzi na model**. Idealny wynik pojedynczej próby nie gwarantował idealnego wyniku w powtórzeniach. Poniższe wyniki dają pewniejszą podstawę porównania dla testowanych krótkich odpowiedzi mesh:

| Model | Odpowiedzi zgodne ze wszystkimi sprawdzanymi regułami | Główne zaobserwowane błędy |
|---|---:|---|
| Importowany LFM2.5-1.2B | 16/18 (89%) | Dwie niedokończone odpowiedzi |
| `gemma3:1b` | 15/18 (83%) | Trzy niedokończone odpowiedzi |
| Importowany LFM2.5-230M | 14/18 (78%) | Niedokończone odpowiedzi i brak nazw źródeł |
| Importowany LFM2.5-350M | 13/18 (72%) | Brak nazw źródeł |
| `qwen2.5:0.5b` | 11/18 (61%) | Za dużo wypunktowań, za dużo słów, brak nazw źródeł |

Na **Pi 4 z 2 GB** osobny test zgodności z sześcioma promptami dał **5/6** LFM2.5-350M, **4/6** LFM2.5-230M i **2/6** Qwen2.5-0.5B. MiniCPM5-1B poprawił wynik z **1/6** przy domyślnym rozumowaniu do **5/6** po jego wyłączeniu. Wyniki Pi 4 pochodzą z pojedynczej próby, dlatego przy omawianiu ogólnej zgodności z instrukcjami bardziej ufamy powtarzanym wynikom Pi 5, a testy Pi 4 wykorzystujemy do oceny stabilności i szybkości na tej płytce.

Błędy mają różne skutki. **Pusta** odpowiedź nic nie daje użytkownikowi, a odpowiedź ignorująca dostarczone materiały może wprowadzać w błąd. Brak nazwy źródła uniemożliwia czytelnikom sprawdzenie atrybucji. Nadmiar wypunktowań lub słów zużywa głównie dodatkowe pakiety po 180 znaków. Niedokończone zdanie może wskazywać na ucięcie odpowiedzi. Błąd LFM2.5-230M dotyczący terminu medycznego przypomina, że odpowiedź może przejść kontrole mechaniczne, a mimo to być błędna. Żaden z pięciu wielokrotnie testowanych modeli nie przestrzegał wszystkich reguł w każdym z 18 przypadków. Aplikacja wymagająca ścisłego limitu lub formatu powinna wymuszać je także po generacji i osobno oceniać treści wysokiego ryzyka.

Sprawdziliśmy też rzeczywisty punkt końcowy bridge, `/v1/chat/completions` zgodny z OpenAI API Ollama, korzystając z pobranego kontekstu WikiMed. Na Pi 5 LFM2.5-1.2B zwrócił odpowiedź 28-wyrazową wykorzystującą sześć dostarczonych terminów; Qwen2.5-0.5B zwrócił odpowiedź 38-wyrazową z siedmioma. Obie mieściły się w dwóch pakietach po 180 znaków. Ta kontrola potwierdza, że zaimportowany model LFM2.5 działa przez ścieżkę żądania bridge, ale pojedyncza udana odpowiedź nie gwarantuje niezawodności.

Ollama publikuje wiele gotowych do pobrania modeli, w tym [warianty Qwen2.5 0.5B, 1.5B i 3B](https://ollama.com/library/qwen2.5/tags). Małe modele LFM2.5 zaimportowaliśmy do Ollama z [wydań GGUF Liquid AI](https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/tree/main). Przed pobraniem sprawdź dokładny tag lub nazwę pliku GGUF: rejestry modeli i repozytoria mogą się zmieniać. Trzymaj pobrane pliki GGUF na trwałym nośniku; w naszych testach umieszczenie plików w `/tmp` opartym na RAM zużyło cenną pamięć Pi 4.

### Tagi rejestru i importy GGUF

Tag Ollama to najkrótsza droga do pierwszego testu: pobierz dokładny tag i uruchom model. Małe modele LFM2.5 z tabeli były **importami GGUF**, a nie tagami `lfm2.5-230m`, `lfm2.5-350m` czy `lfm2.5-1.2b` w publicznej bibliotece Ollama. GGUF to format pliku modelu; nazwy takie jak `Q8_0` i `Q4_K_M` określają wybrany wariant kwantyzacji. Użyte przez nas pliki LFM2.5 230M i 350M miały format Q8_0, a plik 1.2B — Q4_K_M. Dlatego taka sama liczba parametrów pobrana w innym wariancie kwantyzacji nie musi oznaczać identycznego rozmiaru pliku, zużycia pamięci ani jakości.

Aby zaimportować testowany wariant 350M, pobierz GGUF do katalogu na trwałym nośniku, utwórz Modelfile, który wskazuje plik, i pozwól Ollama skopiować go do własnego magazynu modeli:

```bash
mkdir -p "$HOME/gguf"
cd "$HOME/gguf"
curl -fL -C - --retry 5 --retry-all-errors -O \
  https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/resolve/main/LFM2.5-350M-Q8_0.gguf
printf 'FROM %s/LFM2.5-350M-Q8_0.gguf\n' "$PWD" > Modelfile-lfm2.5-350m
ollama create lfm2.5-350m -f Modelfile-lfm2.5-350m
ollama run lfm2.5-350m
```

Import tymczasowo wymaga miejsca zarówno na pobrany plik, jak i jego kopię w Ollama. Używaliśmy pobierania z możliwością wznowienia, ponieważ długie transfery GGUF czasem przerywały się w połowie. Przed importem porównaj SHA-256 pobranego GGUF z hashem opublikowanym przez źródło. Niepełny transfer może wyglądać jak problem z modelem. W naszej konfiguracji Pi katalog `/tmp` korzystał z RAM, więc przechowywanie tam pliku GGUF ograniczało pamięć dostępną dla inferencji.

## Praktyczny punkt wyjścia

| Sprzęt i cel | Pierwszy model do wypróbowania | Dlaczego |
|---|---|---|
| Pi 4 z 2 GB, wariant domyślny | Importowany LFM2.5-350M | Stabilny przy 516 MB RSS i około 1 GB dostępnego RAM; wybrany po błędzie medycznym modelu 230M |
| Pi 4 z 2 GB, najniższe opóźnienie | Importowany LFM2.5-230M | 383 MB RSS i średnia odpowiedź 7.2 s; dokładnie sprawdzaj treść, zwłaszcza przy pytaniach o zdrowie lub bezpieczeństwo |
| Pi 4 z 2 GB, tylko rejestr Ollama | `qwen2.5:0.5b` | Bezpośrednie pobranie z Ollama i stabilność w teście pięciu promptów Pi 4; 61% powtarzanej zgodności na Pi 5 |
| Pi 4 z 4 GB lub Pi 5 | Importowany LFM2.5-1.2B, następnie test lokalny | 967 MB RSS i 89% powtarzanej zgodności na naszym Pi 5 z 8 GB; wariantów 4 GB nie testowaliśmy bezpośrednio |
| Pi 5 z 8 GB, responsywny asystent | Importowany LFM2.5-1.2B | 15.5 tokena/s, 4.7 s całkowitego czasu odpowiedzi i najwyższa zmierzona powtarzana zgodność |
| Pi 5 z 8 GB, konfiguracja wyłącznie z rejestru | `gemma3:1b` | 11.2 tokena/s, 1,262 MB RSS i 83% powtarzanej zgodności |
| Pi 5 z 8 GB, test większego modelu tekstowego | Kwantyzowany Qwen2.5 3B lub Llama 3.2 3B | Oba działały z około 5 tokenami/s i używały 2.4–2.8 GB RSS; Qwen2.5 3B uzyskał 5/6 w pojedynczym teście zgodności |

Te wybory stawiają na krótkie, użyteczne odpowiedzi na Pi, który może też obsługiwać inne usługi. To punkty startowe, a nie twierdzenie, że jeden model jest najlepszy do wszystkiego. W pojedynczym teście zgodności Pi 5 `qwen3.5:0.8b` i Spark-X2.5 ze standardowym rozumowaniem nie uzyskały żadnej odpowiedzi spełniającej wszystkie reguły, a MiniCPM5-1B uzyskał 1/6. Jeśli klient nie może wyłączyć rozumowania, unikaj tych modeli w tej pracy z krótkimi odpowiedziami. Przetestuj docelowy model z rzeczywistym promptem, długością kontekstu, współbieżnością i limitem odpowiedzi planowanymi dla wdrożenia.

Aby użyć modelu z rejestru, po [zainstalowaniu Ollama dla Linuksa](https://ollama.com/download/linux) uruchom:

```bash
ollama pull qwen2.5:0.5b
ollama run qwen2.5:0.5b
```

Testuj własne prompty, docelową długość odpowiedzi i pozostałe uruchomione usługi. Zapisuj całkowity czas odpowiedzi i zużycie pamięci. To lepiej pokaże, czy model nadaje się do Pi, niż sama liczba parametrów.

Na hoście z ograniczoną pamięcią obserwuj swap podczas testów. Jeśli większy model sprawia, że płytka przestaje reagować, użyj mniejszego modelu i ustaw limit pamięci usługi Ollama odpowiedni dla danego modelu, aby zbyt duże ładowanie zakończyło się błędem, zanim wyczerpie pamięć hosta. Limit usługi zabezpiecza system, ale nie sprawia, że zbyt duży model zacznie się mieścić. Restarty Pi 4 podczas naszych testów pokazują, dlaczego przy wyborze trzeba uwzględniać szybkość reakcji i zapas pamięci, a nie tylko liczbę tokenów na sekundę.

## Przełóż benchmark na decyzję wdrożeniową

Zanim zaczniesz codziennie używać modelu, zapisz cztery limity: **maksymalny czas odpowiedzi, maksymalną pamięć rezydentną, format odpowiedzi i zachowanie przy błędzie**. Przetestuj je razem z usługami, które będą współdzielić płytkę. Model, który samodzielnie przechodzi test, ale wymusza swap obok bridge'a radiowego lub pulpitu, nie spełnia wymagań wdrożenia.

Pozostaw zainstalowany jeden mały model awaryjny. Przełącz na niego, gdy model główny przekracza limit pamięci, zwraca pustą odpowiedź lub nie spełnia kontraktu odpowiedzi. Przy każdym porównaniu zapisuj tag modelu, kwantyzację, wersję Ollama, prompt, długość kontekstu i seed, aby późniejsza aktualizacja modelu nie wyglądała jak poprawa sprzętu.
