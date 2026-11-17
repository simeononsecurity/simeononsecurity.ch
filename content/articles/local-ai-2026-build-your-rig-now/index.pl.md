---
title: "Lokalna AI w 2026 roku: model 27B pokonuje Sonnet 4.6, a okno na sprzęt się zamyka"
date: 2026-09-22
lastmod: 2026-11-14
toc: true
draft: false
description: "Zaplanuj lokalny zestaw AI na 2026 rok, uwzględniając rozmiar modelu, VRAM, przepustowość pamięci, pobór mocy, koszt i możliwości rozbudowy."
genre: ["Lokalna AI", "Samodzielnie hostowana AI", "Modele z otwartymi wagami", "Sprzęt AI", "Uczenie maszynowe", "Kwantyzacja", "Domowe laboratorium", "Prywatność", "Ekonomia AI", "Sprzęt konsumencki"]
tags: ["lokalna ai", "uruchamianie llm lokalnie", "qwen3.8", "qwen3.8 27b", "bonsai 2 27b", "ternary bonsai", "prism ml", "kwantyzacja trójwartościowa", "kwantyzacja 1.58 bit", "kwantyzacja llm", "claude sonnet 4.6", "sonnet 4.6 kontra model lokalny", "otwarte wagi", "model moe", "mieszanka ekspertów", "ollama", "llama.cpp", "rtx 5090", "vram", "lokalna inferencja", "ceny gpu 2026", "niedobór dram", "ceny pamięci", "budowa komputera ai", "ai w homelabie", "koszt subskrypcji ai", "openrouter", "artificial analysis", "poradnik zakupu gpu", "llm hostowany lokalnie", "ai chroniąca prywatność", "sprzęt ai 2026"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Nowoczesne stanowisko z jedną kartą graficzną i kilkoma świecącymi ekranami pokazującymi benchmarki i wizualizacje AI, na granatowym tle."
coverCaption: ""
ref: ["/articles/ai-models-raspberry-pi-4-5", "/articles/building-a-privacy-preserving-meshtastic-ai-assistant"]
---

**Model do pobrania, który mieści się na jednej konsumenckiej karcie graficznej, uzyskuje teraz wyższy wynik niż model API z czołówki w zbiorczym indeksie inteligencji.** Qwen3.8 27B to model vision-language z otwartymi wagami, wydany w sierpniu 2026 roku. Jego trójwartościowa repakietyzacja, Bonsai 2 27B, zmniejsza te same wagi do 5.53 GiB. Razem wyznaczają moment, w którym lokalna inferencja przestała być kompromisem hobbystycznym i stała się realną alternatywą dla płatnego API.

*Sprzętowa strona tej historii szybko się zamyka. Pamięć nie była tak droga od dwóch dekad, a jej ceny podbijają również ceny kart graficznych.*

Ten artykuł omawia wyniki benchmarków, budowę obu modeli, obszary, w których model open source nadal przegrywa, oraz powody, dla których najbliższe dwanaście miesięcy nie sprzyja czekaniu.

**Wynik dla czytelnika:** wybierz model i poziom pamięci do swojego obciążenia. Przed zakupem porównaj koszt sprzętu, energii, rozmiar kontekstu i zmierzoną przepustowość. Porównanie benchmarków nie przewiduje jakości wyników dla twojego zadania ani przyszłej ceny GPU.

## Krótka odpowiedź

**Różnica w inteligencji między lokalnym modelem 27B a płatnym API zbliżonym do czołówki zniknęła. Pozostałe zalety płatnego modelu są mniejsze, niż sugeruje różnica w cenie.**

Jednocześnie zaszły trzy zmiany:

- **Otwarte modele 27B osiągnęły wyniki zbliżone do czołówki.** Qwen3.8 27B uzyskał 33.7 w Intelligence Index wobec 30.1 dla Sonnet 4.6, w tym samym zestawie testów.
- **Kwantyzacja trójwartościowa zmniejszyła wymagania pamięciowe o około dwie trzecie.** Bonsai 2 27B uruchamia cały model 27B w **5.53 GiB**, co mieści się na kartach kosztujących kilkaset dolarów.
- **Podaż pamięci pogorszyła się.** Ceny kontraktowe standardowego DRAM wzrosły na początku 2026 roku o **90 do 95 procent kwartał do kwartału**. TrendForce nie odnotował wcześniej większego kwartalnego wzrostu. W efekcie kolejna generacja GPU przesunęła się na 2028 rok.

*Zakup lub budowa teraz to tańsza opcja. To nie slogan sprzedażowy, lecz wniosek z danych o podaży.*

## Obejrzyj próbę na jednej karcie GPU

Powyższe twierdzenie zasługuje na demonstrację, a nie tabelę. Bijan Bowen przetestował Bonsai 2 27B na komputerze z jedną kartą GPU i sprawdził, czy jest to obecnie najlepszy model dla jednej karty.

{{< youtube id="OA5cICIzD-c" enable="true" title="Pierwszy test Bonsai 2 27B: czy to NAJLEPSZY model AI na jednej karcie GPU?" description="Pierwsze spojrzenie na uruchomienie trójwartościowego modelu Bonsai 2 27B na jednej konsumenckiej karcie GPU. Omówiono szybkość, jakość i alternatywy." >}}

*Zwróć uwagę na jakość odpowiedzi, a nie liczbę tokenów na sekundę. Szybkość najłatwiej poprawić.*

## Dwie nazwy, te same wagi

Dwa modele, które warto tu poznać, nie konkurują ze sobą. **To te same wagi zapisane z dwiema różnymi precyzjami.**

| | Qwen3.8 27B | Trójwartościowy Bonsai 2 27B |
|---|---|---|
| **Czym jest** | Oryginalny model Qwen z otwartymi wagami | Trójwartościowa repakietyzacja Qwen3.8-27B od Prism ML |
| **Wagi na dysku** | **18 GB** | **5.53 GiB** (PTQ1_0) lub **6.70 GiB** (PQ2_0) |
| **Parametry** | 27B, model gęsty | 26.90B, ta sama architektura |
| **Kontekst** | 256K | 262,144 tokenów |
| **Obraz** | Tak, natywnie | Tak, osobny pakiet projektora CLIP |
| **Wywoływanie narzędzi** | Tak | Tak |
| **Licencja** | Apache 2.0 | Apache 2.0 |
| **Środowisko uruchomieniowe** | Ollama, llama.cpp, MLX | Tylko **fork llama.cpp od Prism ML** |

Strona biblioteki Ollama dla `qwen3.8` podaje model 27B o rozmiarze **18 GB**, kontekst 256K, obsługę obrazu, wywoływanie narzędzi i osobną kompilację MLX dla Apple Silicon. Trójwartościowa repakietyzacja w Ollama jest kopią pakietów GGUF na licencji Apache 2.0 od Prism ML, opublikowaną ponownie ze zgodnymi sumami kontrolnymi.

**Praktyczne pytanie nie brzmi więc, który model wybrać.** Chodzi o to, ile pamięci chcesz przeznaczyć na tę samą inteligencję. Wersja trójwartościowa zużywa mniej więcej jedną trzecią pamięci i niewiele traci.

{{< figure src="local-ai-architecture-comparison.webp" alt="Diagram porównuje pamięć tego samego modelu 27B: 18 GB przy standardowej precyzji i 5.53 GiB przy wagach trójwartościowych, obie wersje mieszczą się na jednej konsumenckiej karcie GPU" >}}

## Porównanie wyników

Artificial Analysis ocenia oba modele w tym samym zestawie testów. Warto czytać wyniki wiersz po wierszu, bo każdy model wygrywa w innych obszarach.

| Pomiar | Qwen3.8 27B | Claude Sonnet 4.6 | Lider |
|---|---|---|---|
| **Intelligence Index** | **33.7** | 30.1 | Otwarty |
| **Coding Index** | **68.1** | 63.0 | Otwarty |
| **Agentic Index** | **45.8** | 31.8 | Otwarty |
| **GPQA Diamond** | **90.5%** | 87.5% | Otwarty |
| **Humanity's Last Exam** | **33.9%** | 33.6% | Otwarty |
| **AA-LCR (długi kontekst)** | **82.0%** | 80.0% | Otwarty |
| **GDPval-AA** | **45.4%** | 36.0% | Otwarty |
| **CritPt (fizyka badawcza)** | **5.4%** | 3.1% | Otwarty |
| **Wskaźnik odpowiedzi bez halucynacji** | **69.7%** | 51.6% | Otwarty |
| **SciCode** | 46.6% | **50.1%** | Sonnet |
| **Dokładność AA-Omniscience** | 15.6% | **40.9%** | Sonnet |

*Model open source prowadzi w dziewięciu z jedenastu porównywalnych pomiarów, w tym we wszystkich zbiorczych indeksach.*

### Gdzie wygrywa model z otwartymi wagami

Najważniejsze są trzy zbiorcze indeksy. **Intelligence 33.7 wobec 30.1, Coding 68.1 wobec 63.0 i Agentic 45.8 wobec 31.8.** Różnica w indeksie agentowym jest największa. Ma to największe znaczenie dla osób uruchamiających zautomatyzowane wieloetapowe przepływy pracy zamiast pojedynczych promptów.

Dla porównania percentylowego Artificial Analysis plasuje Qwen3.8 27B **powyżej 86 procent modeli w indeksie agentowym** i powyżej 76 procent w indeksie programowania. Sonnet 4.6 osiąga odpowiednio 68 i 72 procent. W rozumowaniu naukowym na poziomie studiów magisterskich model open source zdobywa **90.5 procent** w GPQA Diamond.

### Gdzie nadal wygrywa Sonnet 4.6

Dwa pomiary wskazują drugą stronę. Żaden nie jest mało istotny.

**AA-Omniscience sprawdza, czy model od razu poprawnie odpowiada na pytania dotyczące wiedzy. Sonnet 4.6 uzyskuje 40.9 procent wobec 15.6 procent.** To duża różnica w wiarygodności faktów i najmocniejszy pojedynczy argument za płatnym modelem premium.

Wynik dotyczący odpowiedzi bez halucynacji wymaga ostrożności. 69.7 procent dla Qwena wobec 51.6 procent dla Sonneta wygląda na wyraźne zwycięstwo i sam w sobie nim jest. Wskaźnik opisuje jednak udział *niepoprawnych* odpowiedzi, które nie zawierają zmyślonych informacji. Model o niższej dokładności tworzy więcej błędnych odpowiedzi, więc te wartości dotyczą różnych zbiorów i nie są wprost porównywalne. **Najpierw sprawdź wiersz z dokładnością.**

Sonnet uzyskuje też 50.1 procent w SciCode wobec 46.6 procent. Raportuje również wyniki w dwóch testach, których karta otwartego modelu nie wymienia: IFBench i Terminal-Bench Hard. Nie da się ich porównać.

### Dwie uczciwe uwagi

**Daty wydania dzieli sześć miesięcy.** Sonnet 4.6 ukazał się w lutym 2026 roku, a Qwen3.8 27B w sierpniu 2026 roku. Porównanie modelu z czołówki z lutego z otwartym modelem z sierpnia nie jest równorzędnym testem.

**Sonnet 4.6 nie jest już flagowym modelem Anthropic.** Sonnet 5 i Opus 5 znajdują się teraz wyżej w ofercie. Otwarty model 27B dogonił flagowy model z połowy 2026 roku. Nie dogonił obecnego szczytu oferty. Każdy, kto twierdzi inaczej, nadinterpretuje tabelę.

*Benchmarki mierzą wyniki w benchmarkach. Liczy się wyłącznie wynik dla twojego obciążenia.*

## Co zmieniają wagi trójwartościowe

Bonsai 2 nie jest mniejszym modelem. To ten sam model 26.90B zapisany ze znacznie niższą precyzją numeryczną. Opublikowane metadane GGUF jasno pokazują kompromis.

| Właściwość | Wartość |
|---|---|
| **Architektura** | `qwen35`, hybrydowy mechanizm uwagi z pełną uwagą co czwartą warstwę oraz warstwami state-space |
| **Parametry** | 26.90B |
| **Bloki** | 64 |
| **Szerokość osadzeń** | 5120 |
| **Uwaga** | 24 głowy zapytań, 4 głowy KV, długość klucza i wartości 256 |
| **Kontekst** | 262,144 tokenów, baza RoPE 1e7 |
| **Format wag** | Trójwartościowy, rozmiar grupy 128. PQ2_0 przy 2.13 bitach na wagę, PTQ1_0 przy 1.75 |
| **Moduł wizji** | CLIP, 460.73M parametrów, dostarczany jako osobny pakiet projektora |
| **Licencja** | Apache 2.0 |

**Wagi trójwartościowe oznaczają, że każdy parametr przyjmuje jedną z trzech wartości zamiast jednej z szesnastu.** Na tym polega kompresja, która pozwala zmieścić pełny model 27B w 5.53 GiB zamiast 18 GB.

### Zmierzona przepustowość

Test wykonano programem `llama-bench` na RTX 5090 32 GB, z przeniesieniem każdej warstwy na GPU i włączonym flash attention. Tabela podaje średnią z trzech przebiegów:

| Pakiet | Wagi | Prefill (pp512) | Dekodowanie (tg128) |
|---|---|---|---|
| **PQ2_0** | 6.70 GiB | **3802.74 tok/s** | **135.41 tok/s** |
| **PTQ1_0** | 5.53 GiB | 1876.31 tok/s | 131.41 tok/s |

PQ2_0 wykonuje prefill **2.03 raza szybciej** niż PTQ1_0, a różnica w dekodowaniu mieści się w granicach błędu statystycznego. Dlatego PQ2_0 jest rozsądnym wyborem domyślnym. PTQ1_0 przydaje się, gdy liczy się ostatnie 1.2 GiB pamięci. Przy użyciu `llama-server` i kontekstu 65K dekodowanie utrzymywało **136.5 tok/s** przy pojedynczym strumieniowym żądaniu.

**Szybkość dekodowania odczuwasz na co dzień.** 135 tokenów na sekundę znacznie przewyższa tempo czytania. Opóźnienie nie jest powodem, by uruchamiać model lokalnie, bo hostowane API jest wystarczająco szybkie. Powodem są koszt, prywatność i kontrola.

### Pułapka, o której nikt nie wspomina

**Standardowa wersja Ollama nie załaduje tych plików.** Jądra trójwartościowe znajdują się w forku llama.cpp od Prism ML. Test z Ollama 0.34.2 kończy się błędem `unsupported tensor "output.weight" size overflows`. Środowisko rozpoznaje architekturę `qwen35`, ale jego biblioteki nie zawierają `pq2_0` ani `ptq1_0`. Nie ma też środowiska wykonawczego do aktywacji Hadamarda.

Przed poświęceniem na to całego wieczoru warto poznać drugą pułapkę. **Pakiet F16 z tej rodziny wygląda na bezpieczną wersję zastępczą, ale nią nie jest.** Jego tensory mają standardowe formaty F16 i F32, więc plik przechodzi parsowanie i ładuje się bez skarg. Potem generuje niespójny tekst. Wagi leżą w obróconej bazie zapisanej w metadanych `prism.hadamard.*`. Środowisko musi zastosować odpowiedni obrót, inaczej wynik będzie bezsensowny. Pakiet F16 zajmuje 50.1 GiB, więc i tak nie zmieści się w całości na karcie 32 GB.

*Przed pobraniem przeczytaj kartę modelu. Kopia społecznościowa nie jest wspieraną kompilacją, a ta strona mówi o tym wprost.*

## Rozwój modeli MoE

Gęste modele 27B to tylko połowa historii. Modele mixture-of-experts aktywują dla każdego tokena niewielką część parametrów, co ponownie zmienia rachunek kosztów.

| Rodzina modelu | Łącznie / aktywne | Kontekst | Informacja |
|---|---|---|---|
| **Qwen3.8 2.4T A95B** | 2.4T / 95B | 1.0M | Model open source spokrewniony z Qwen3.8 Max |
| **Qwen3.6 35B A3B** | 35B / 3B | 262K | Apache 2.0, hybrydowy sparse MoE |
| **Qwen3 Coder Next** | 80B / 3B | 256K | Otwarte wagi, stworzony dla stale działających agentów kodujących |

**Qwen3 Coder Next to model lokalny, który warto obserwować.** Ma łącznie 80B parametrów, lecz dla każdego tokena aktywuje tylko 3B. Powstał z myślą o stale działających agentach w środowiskach CLI i IDE. Model aktywujący 3B parametrów generuje z szybkością modelu 3B, korzystając z możliwości zapisanych w 80B parametrów. Notatki projektu podają wyniki porównywalne z modelami używającymi od 10 do 20 razy więcej aktywnych obliczeń.

*Gęsty model 27B jest dziś bezpiecznym wyborem. Krzywa wydajności modeli rzadkich nadal się poprawia.*

{{< figure src="local-ai-moe-dense-tradeoff.webp" alt="Wykres porównuje gęsty model 27B aktywujący wszystkie parametry na token z rzadkim modelem mixture-of-experts aktywującym tylko 3 miliardy z 80 miliardów parametrów" >}}

## Okno na sprzęt się zamyka

Ta część historii ma wyznaczony termin.

Lokalna inferencja stała się tania dokładnie wtedy, gdy pamięć potrzebna do jej działania zaczęła drożeć. Te dwa trendy zderzają się, a skutki widać już w cenach detalicznych.

### Co stało się z cenami pamięci

**Kontraktowe ceny standardowego DRAM wzrosły o 90 do 95 procent kwartał do kwartału w pierwszym kwartale 2026 roku.** To najwyższy wzrost kwartalny odnotowany przez TrendForce. W tym samym okresie pamięć NAND flash zdrożała o 55 do 60 procent.

Presja nie osłabła. Według danych TrendForce DRAM podrożał w drugim kwartale o kolejne **58 do 63 procent**, a NAND o 70 do 75 procent. Nawet wyhamowanie w trzecim kwartale, wzrost DRAM o 13 do 18 procent i NAND o 10 do 15 procent, nakłada się na dwa rekordowe kwartały. To nie jest ulga.

Przyczyna ma charakter strukturalny, a nie cykliczny. Rozbudowa centrów danych AI pochłania pamięć, która wcześniej trafiała do telefonów, laptopów i konsol. Producenci pamięci najpierw realizują bardziej marżowe zamówienia. Analitycy śledzący podaż modułów przewidują, że w 2027 roku dostawy układów DRAM do producentów modułów spadną o ponad 70 procent.

**Prezes Intela podał konkretną wartość.** Podczas AI Infrastructure Summit w Santa Clara 15 września 2026 roku Lip-Bu Tan powiedział, że ceny pamięci wzrosły już "pięć, sześć i siedem razy" w porównaniu z wcześniejszym poziomem. Ostrzegł, że pamięć stanowi teraz 70 do 80 procent kosztu materiałów taniego laptopa. W osobnej wypowiedzi stwierdził, że poprawa nie nastąpi przed 2028 rokiem.

*Niezależne doniesienia o porównaniu ceny DRAM i wafli z zaawansowanymi układami logicznymi w przeliczeniu na powierzchnię zawierają ważne zastrzeżenie. Ceny spot nie są cenami kontraktowymi, a rynek spot DDR5 jest na tyle mały, że takie porównanie jest sugestywne, lecz nie rozstrzygające. Kierunek zmian nie budzi wątpliwości.*

{{< figure src="local-ai-memory-price-trend-2026.webp" alt="Wykres kwartalnych wzrostów cen kontraktowych DRAM w 2026 roku: wzrost o 90 do 95 procent w pierwszym kwartale, zwalniający do 13 do 18 procent w trzecim kwartale" >}}

### Wpływ na karty graficzne

Pamięć stanowi dużą część kosztu materiałów karty graficznej, więc ceny DRAM bezpośrednio wpływają na ceny GPU.

| Karta | Początek 2025 | Wrzesień 2026 |
|---|---|---|
| **Nvidia RTX 5090** | $1,999 | **ponad $5,000** |
| **Asus RTX 5080** | $1,199 | $1,595 |
| **AMD RX 9070 XT** | około $830 | **ponad $1,037** |

Te podwyżki następowały falami w 2026 roku, a nie jako pojedyncze skoki. Nvidia podniosła ceny w styczniu, ponownie w maju dla RTX 5090, a potem jeszcze raz pod koniec roku. AMD dołączyło w sierpniu, podnosząc ceny wybranych kart Radeon i zestawów pamięci GDDR6 o co najmniej 10 procent. Firma bezpośrednio wskazała na koszty pamięci.

**Kolejna generacja została przesunięta zamiast trafić do sprzedaży.** Premiera serii RTX 60 od Nvidii jest teraz oczekiwana w 2028 roku, z całkowitym pominięciem 2027 roku. Jako przyczynę podano dostępność pamięci.

*Karta kupowana dziś nie konkuruje z tańszą kartą w przyszłym roku. Konkuruje z droższą wersją samej siebie.*

## Dlaczego czekanie kosztuje więcej

Typowa rada sprzętowa brzmi: poczekaj na następną generację. Na rynku z ograniczoną podażą pamięci ta rada działa na twoją niekorzyść.

Przemawiają za tym trzy argumenty.

**Ceny już wzrosły i nadal idą w górę.** Podwyżka cen kontraktowych DRAM o 90 do 95 procent w jednym kwartale nie jest krótkotrwałym skokiem, który cofnie się w kolejnym kwartale. TrendForce prognozuje dalszy wzrost w trzecim kwartale, a nie spadek. Prezes Intela wskazuje 2028 rok jako termin poprawy.

**W 2027 roku nie pojawi się nowy produkt, na który warto czekać.** Jeśli następna generacja konsumenckich GPU trafi na rynek dopiero w 2028 roku, czekanie obejmuje dwa lata. To większa część cyklu wymiany sprzętu spędzona na bezczynności.

**Modele już są wystarczająco dobre.** To zmieniło się w 2026 roku. Dwa lata temu lokalny sprzęt dawał wyraźnie gorsze wrażenia. Dziś za te same pieniądze możesz uruchomić model 27B z szybkością 135 tokenów na sekundę i kontekstem 262K, który pokonuje płatne API w zbiorczym indeksie inteligencji.

*Jeśli czekałeś, aż lokalne modele staną się dobre, już się doczekałeś. Jeśli czekasz na tańszy sprzęt, dane o podaży wskazują na 2028 rok.*

## Co zbudować

Dobór sprzętu do opisanych modeli jest prosty, bo wagi trójwartościowe obniżyły wymagania pamięciowe.

| Poziom | Pamięć | Co uruchomi wygodnie |
|---|---|---|
| **Podstawowy** | 8 do 12 GB VRAM | Trójwartościowy 27B o rozmiarze 5.53 do 6.70 GiB, z zapasem na kontekst |
| **Praktyczny** | 16 do 24 GB VRAM | Pełny Qwen3.8 27B o rozmiarze 18 GB albo pakiet trójwartościowy z długim kontekstem |
| **Komfortowy** | 32 GB VRAM | Trójwartościowy 27B z pełnym kontekstem 262K albo MoE 80B z 3B aktywnych parametrów |
| **Pamięć współdzielona** | 64 do 128 GB | Większe rzadkie modele MoE na Apple Silicon lub komputerze z pamięcią współdzieloną |

Kilka praktycznych uwag ma większe znaczenie niż tabela poziomów:

- **Kup pamięć, nie flagową kartę GPU.** Pakiet trójwartościowy 5.53 GiB sprawia, że podstawowy poziom jest naprawdę użyteczny. Różnicę wydaj na RAM i dysk zamiast na kartę z najwyższej półki w cenach z 2026 roku.
- **Systemy z pamięcią współdzieloną są opłacalne.** Komputer z co najmniej 64 GB pamięci współdzielonej uruchomi większe rzadkie modele za ułamek ceny osobnej karty o tej samej pojemności.
- **Liczą się zasilanie i chłodzenie.** Komputer wykonujący inferencję przez wiele godzin zachowuje się inaczej niż podczas kilkuminutowego benchmarku.
- **Uruchamiaj pakiet trójwartościowy razem z mniejszym modelem.** Model 3B odpowiada na proste pytania, a model 27B zajmuje się trudniejszymi.

{{< centerbutton href="https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B" >}}
Pobierz Ternary Bonsai 2 27B
{{< /centerbutton >}}

## Kiedy modele z wyższej półki są warte swojej ceny

Argument za poziomem premium jest prawdziwy, ale węższy, niż sugeruje marketing.

**Najuczciwszą odpowiedzią jest wiarygodność faktów.** Dokładność AA-Omniscience wynosi 40.9 procent dla Sonnet 4.6 i 15.6 procent dla otwartego modelu 27B. Jeśli błędna odpowiedź zaszkodzi klientowi, diagnozie lub stanowisku prawnemu, różnica 25 punktów procentowych znaczy więcej niż każdy zbiorczy indeks.

**Drugim powodem są długie łańcuchy działań agentów.** Sonnet 4.6 osiąga 53.0 procent w Terminal-Bench Hard i 75.7 procent w τ²-Bench Telecom. Testy te mierzą długotrwałe korzystanie z narzędzi i zachowanie agenta w wielu turach. Karta modelu open source nie podaje porównywalnych wyników. To niepokojący brak.

**Trzeci powód jest operacyjny.** Hostowane API nie wymaga aktualizowania sterowników, radzenia sobie z osobliwościami kwantyzacji, śledzenia forka llama.cpp ani poprawnego ustawienia obróconej bazy wag. Ktoś inny odpowiada za dostępność usługi i ktoś inny odbiera wezwanie o trzeciej nad ranem.

### Pytanie, które warto zadać

Jak wygląda uzasadnienie dla poziomu premium poza przedsiębiorstwami?

**W pracy wymagającej rzetelnej wiedzy nadal ma sens.** Chodzi o badania, analizę prawną, pytania medyczne, modelowanie finansowe i każde zadanie, w którym pewna siebie, lecz błędna odpowiedź jest kosztowna. To rzeczywista kategoria, a różnica dokładności jest prawdziwym powodem do zapłaty.

**W pracy generatywnej uzasadnienie szybko słabnie.** Pisanie, streszczanie, refaktoryzacja kodu, formatowanie danych, klasyfikowanie dokumentów i automatyczne potoki to zadania, w których sprawdzasz wynik, zanim mu zaufasz. Różnica dokładności niewiele kosztuje, gdy człowiek lub zestaw testów weryfikuje rezultat. W takim zastosowaniu trudno uzasadnić opłatę za token za wynik 30.1, skoro wynik 33.7 działa bezpłatnie na sprzęcie, który już posiadasz.

**Decyzja dotyczy teraz konsekwencji, a nie możliwości.** Dwa lata temu pytanie brzmiało, czy model lokalny w ogóle poradzi sobie z pracą. Dziś chodzi o koszt pomyłki i o to, jak ją wykryć.

*Premia dla przedsiębiorstw kupuje niezawodność, zgodność z przepisami i cudzy dyżur. Pozostali płacą za różnicę, która przestaje mieć znaczenie, gdy wynik sprawdza zestaw testów.*

## Najważniejsze wnioski

- **Lokalny model 27B uzyskuje wyższy wynik niż Claude Sonnet 4.6 w zbiorczym indeksie inteligencji**, 33.7 wobec 30.1. Prowadzi też w programowaniu, zadaniach agentowych, długim kontekście i rozumowaniu naukowym.
- **Sonnet 4.6 nadal wygrywa dokładnością faktów**, 40.9 wobec 15.6 procent w AA-Omniscience. To najmocniejszy argument za poziomem premium.
- **Kwantyzacja trójwartościowa czyni ten wybór praktycznym.** Bonsai 2 27B uruchamia ten sam model 26.90B w 5.53 GiB zamiast 18 GB. Oba mają licencję Apache 2.0.
- **Standardowa wersja Ollama nie uruchomi pakietów trójwartościowych.** Potrzebny jest fork llama.cpp od Prism ML, a wersja F16 po cichu generuje niespójny tekst zamiast zgłosić błąd.
- **Zmierzona szybkość dekodowania to 135 tokenów na sekundę** na RTX 5090, znacznie powyżej tempa czytania.
- **Ceny pamięci są powodem, by działać teraz.** Ceny kontraktowe DRAM wzrosły w jednym kwartale 2026 roku o 90 do 95 procent, a kolejna generacja konsumenckich GPU została przesunięta na 2028 rok.
- **Cena RTX 5090 wzrosła w mniej niż dwa lata z $1,999 do ponad $5,000**, a podwyżki objęły każdy poziom.

## Następne kroki

1. **Pobierz model i przetestuj go na własnym obciążeniu**: **[Ternary Bonsai 2 27B w Ollama](https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B)**
2. **Pobierz oryginalne wagi w pełnej precyzji**, jeśli masz wystarczająco pamięci: **[Qwen3.8 w Ollama](https://ollama.com/library/qwen3.8)**
3. **Wypróbuj model przed budową komputera** przez darmowy hostowany punkt końcowy: **[Qwen3.8 27B za darmo w OpenRouter](https://openrouter.ai/qwen/qwen3.8-27b:free)**
4. **Porównaj z płatnym poziomem na tych samych promptach**: **[Claude Sonnet 4.6 w OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-4.6)**
5. **Dobierz komputer do potrzebnego poziomu** na podstawie tabeli pamięci i kup pamięć przed kartą graficzną.
6. **Jeśli masz nieużywane Raspberry Pi**, sprawdź, czy uruchomi mniejszy model: **[Jakie modele AI działają na Raspberry Pi 4 lub 5?](/articles/ai-models-raspberry-pi-4-5/)**

## Powiązane artykuły

| Artykuł | Tematyka |
|---|---|
| **[Jakie modele AI działają na Raspberry Pi 4 lub 5?](/articles/ai-models-raspberry-pi-4-5/)** | Dolna granica lokalnej inferencji i możliwości małych komputerów |
| **[Budowa asystenta AI chroniącego prywatność dla Meshtastic](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | Lokalny asystent na sprzęcie poza siecią, gdzie prywatność jest koniecznością |
| **[Rola pamięci ECC w ograniczaniu uszkodzeń danych](/articles/the-role-of-ecc-memory-in-mitigating-data-corruption/)** | Dlaczego jakość pamięci ma większe znaczenie, gdy działa w niej duży model |
| **[Czym jest homelab i czy warto go mieć?](/articles/what-is-a-homelab-and-should-you-have-one/)** | Planowanie miejsca, zasilania i chłodzenia dla gorącego sprzętu |

## Źródła

1. [Ternary Bonsai 2 27B - model w Ollama](https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B)
2. [Qwen3.8 - biblioteka modeli Ollama](https://ollama.com/library/qwen3.8)
3. [Qwen3.8 27B (bezpłatny) - benchmarki i ceny OpenRouter](https://openrouter.ai/qwen/qwen3.8-27b:free)
4. [Claude Sonnet 4.6 - benchmarki i ceny OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-4.6)
5. [Pierwszy test Bonsai 2 27B - czy to NAJLEPSZY model AI na jednej karcie GPU? - Bijan Bowen](https://www.youtube.com/watch?v=OA5cICIzD-c)
6. [Artificial Analysis - niezależne oceny modeli](https://artificialanalysis.ai/)
7. [TrendForce - prognozy cen kontraktowych DRAM i NAND](https://www.trendforce.com/)
8. [Układy pamięci są już droższe od układów obliczeniowych w przeliczeniu na powierzchnię - Tom's Hardware](https://www.tomshardware.com/pc-components/dram/dram-is-now-more-expensive-than-compute-chips-on-per-area-basis-ai-demand-drives-memory-die-value-past-leading-edge-silicon)
9. [Ulga na rynku GPU przesunięta na 2028 rok po rekordowym wzroście DRAM o 95% - Tech Insider](https://tech-insider.org/gpu-relief-pushed-2028-dram-price-jump-2026/)
10. [Tan z Intela: pamięć podrożała siedmiokrotnie, ulga dopiero w 2028 roku - shattered.io](https://shattered.io/intel-ceo-memory-shortage-no-relief-until-2028-2026/)
11. [Fork llama.cpp Prism ML - jądra trójwartościowe](https://github.com/PrismML-Eng/llama.cpp)
12. [Ternary-Bonsai-2-27B-gguf - wagi źródłowe](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)
