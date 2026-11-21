---
title: "Benchmarki GPU modeli Llama 3.1 8B i Qwen3.8 27B na Vast.ai"
date: 2026-10-02
lastmod: 2026-11-20
toc: true
draft: false
description: "Porównaj zmierzone wyniki Ollama dla Llama 3.1 8B i Qwen3.8 27B na GPU Vast.ai, ich koszty i opcje hostingu."
genre: ["Lokalna sztuczna inteligencja", "Benchmarki GPU", "Samodzielnie hostowana AI", "Chmura obliczeniowa", "Sztuczna inteligencja", "Ekonomia AI"]
tags: ["Llama 3.1 8B", "llama3.1:8b", "Qwen3.8 27B", "Qwen3.8:27b", "Vast.ai", "benchmark GPU", "Ollama", "H100", "RTX PRO 5000", "RTX 6000 Ada", "RTX PRO 6000 Max-Q", "A100", "CMP 170HX", "lokalny LLM", "długi kontekst", "wynajem GPU", "samodzielnie hostowana AI", "modele abliterated", "modele bez cenzury", "kredyty API", "subskrypcja AI", "Q4_K_M", "tokeny na sekundę"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Zaawansowane technologicznie stanowisko z kartą graficzną i ekranami prezentującymi wyniki benchmarków lokalnej AI"
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**H100 SXM był najszybszą kartą w obu testach modeli w Ollama, ale nie oferował najlepszej wartości.** RTX PRO 5000 i RTX 6000 Ada zapewniały lepszą równowagę między szybkością a kosztem wynajmu, a CMP 170HX miał najniższą stawkę godzinową spośród ukończonych testów Qwen3.8 27B.

*Wyniki dotyczą jednego modelu, jednego interfejsu Ollama, domyślnej kwantyzacji i jednego sposobu serwowania. Traktuj je jako dane do doboru sprzętu dla tego obciążenia, a nie uniwersalny ranking GPU.*

Ten artykuł porównuje **Llama 3.1:8b**, kompilację Ollama Q4_K_M z 8,03 mld parametrów, z **Qwen3.8:27b**, kompilacją Ollama Q4_K_M z około 27,3 mld parametrów. Oba modele testowano na instancjach GPU wynajętych przez Vast.ai. Testy mierzyły przepustowość dekodowania przy rzeczywistych długościach promptu aż do obsługiwanego limitu kontekstu.

## Krótka odpowiedź

**Do regularnej pracy jednego użytkownika wynajmij RTX PRO 5000 lub RTX 6000 Ada.** RTX PRO 5000 miał najlepszy stosunek osiągów do ceny przy krótkim i średnim kontekście. RTX 6000 Ada kosztował mniej i utrzymywał przewagę nad kartami A100. Wybierz H100 SXM, gdy szybkość odpowiedzi jest ważniejsza od stawki godzinowej albo gdy używasz długich promptów.

| Cel | Zalecenie | Powód |
|---|---|---|
| **Najniższy koszt testu** | CMP 170HX | 0,420 USD za godzinę i wystarczająca VRAM dla testowanych modeli Q4_K_M |
| **Najlepsza wartość poniżej 1,25 USD/h** | RTX PRO 5000 lub RTX 6000 Ada | Wysoka szybkość dekodowania bez kosztu wynajmu H100 |
| **Najszybsze odpowiedzi** | H100 SXM | Najwyższa szybkość dekodowania w obu testach modeli |
| **Qwen z długim kontekstem** | H100 SXM lub RTX PRO 6000 Max-Q | Obie karty ukończyły test Qwen z około 131 tys. tokenów i dużym zapasem VRAM |
| **Popularny punkt odniesienia 8B** | Llama 3.1:8b | Praktyczne porównanie 8B z limitem kontekstu 128K |
| **Małe, powtarzalne obciążenie** | Kredyty API lub subskrypcja czatu | Brak kosztu bezczynnego GPU, konserwacji i wdrażania |
| **Prywatne i częste obciążenie** | Własna stacja robocza z GPU | Stałe użycie łatwiej uzasadnia koszt sprzętu |
| **Testy modeli abliterated lub bez cenzury** | Najpierw wynajmij, kup dopiero przy regularnym użyciu | Przed zakupem sprzętu osobno sprawdź zachowanie modelu, licencję i ryzyko operacyjne |

## Metodyka testu

**Test wykorzystywał Ollama z domyślną kompilacją modelu Q4_K_M.** Nie dodano specjalnej kwantyzacji, dekodowania spekulatywnego, niestandardowego próbkowania ani innego stosu serwującego. Celem było proste i powtarzalne lokalnie porównanie instancji GPU.

Vast.ai opisuje usługę jako rynek chmurowych GPU łączący dostawców mocy obliczeniowej z użytkownikami. Dokumentacja wymienia wynajem na żądanie, rezerwacje, instancje przerywalne i usługę bezserwerową, a także filtry modelu GPU, pamięci, ceny i dostępności. Podane niżej stawki pochodzą z instancji wybranych podczas tej sesji testowej, a nie ze stałego cennika Vast.ai.

Mierzonym wynikiem była **przepustowość dekodowania**, wyrażona w wygenerowanych tokenach na sekundę. Przepustowość wstępnego przetwarzania promptu podano osobno, ponieważ opisuje jego analizę, a nie tempo pojawiania się odpowiedzi. Długi prompt często wymaga dużo czasu na przetworzenie, nawet gdy szybkość dekodowania pozostaje wysoka.

W każdym kontekście wykonano dwie prawidłowe próby i zapisano medianę wyniku dekodowania. Ukończone poziomy promptu oparto na rzeczywistej liczbie prompt_eval_count:

- **Około 16,4 tys. tokenów promptu**
- **Około 32,8 tys. tokenów promptu**
- **Około 65,5 tys. tokenów promptu**
- **Około 131 tys. tokenów promptu**

Nie ukończono żądanej próby z 256 tys. tokenów. Karty A100 40 GB i kilka mniejszych kart nadal przetwarzały dane albo nie osiągnęły docelowej długości kontekstu.

> **Ograniczenie testu:** Wyniki obejmują dwa obciążenia Ollama Q4_K_M i jeden sposób serwowania. Nie przewidują szybkości trenowania, przepustowości wielu użytkowników, generowania obrazów, wydajności vLLM ani wyników innego modelu.

## Ponowny test Llama 3.1 8B

**Llama 3.1:8b stanowi użyteczny, praktyczny punkt odniesienia dla tej samej puli GPU.** Według Ollama model ma około 120 mln pobrań, więc jego popularność uzasadnia wybór do drugiego testu. [Oficjalna strona modelu Ollama](https://ollama.com/library/llama3.1:8b) podaje kompilację Q4_K_M o rozmiarze 4,9 GB, 8,03 mld parametrów i kontekst do 128K.

Ponowny test używał osobnego programu pomiarowego dla modelu, a generator promptów skalibrowano względem tokenizera Ollama. Poniższe etykiety pokazują rzeczywistą liczbę tokenów promptu, a nie żądane ustawienie kontekstu:

- **Około 32 676 rzeczywistych tokenów promptu** dla celu 32k
- **Około 65 342 rzeczywistych tokenów promptu** dla celu 64k
- **Około 130 671 rzeczywistych tokenów promptu** dla celu 128k

Poziom 256k nie jest obsługiwany przez Llama 3.1 8B, ponieważ podany limit kontekstu modelu wynosi 128K. Program dodał ponawianie prób i wiersze statusu, dzięki czemu przekroczenie limitu czasu pozostaje widoczne w tabeli.

### Wyniki Llama 3.1 8B

| GPU | ~32k tokenów dekodowania/s | ~64k tokenów dekodowania/s | ~128k tokenów dekodowania/s |
|---|---:|---:|---:|
| **H100 SXM** | **163.5** | **124.0** | **82.4** |
| **H100 SXM** | **158.6** | **121.2** | **80.6** |
| **RTX PRO 5000** | 110.1 | 79.8 | 49.9 |
| **CMP 170HX 64GB** | 91.9 | 71.0 | 50.1 |
| **RTX 6000 Ada** | 88.3 | 53.9 | 29.3 |
| **RTX PRO 6000 Max-Q** | 66.7 | 53.0 | 40.3 |
| **RTX PRO 6000 S** | 60.3 | 42.5 | 33.9 |
| **A100 SXM4 40GB** | 2.0 | 40.6 | 38.5 |
| **A100 PCIe 40GB** | 1.2 | 20.3 | 20.3 |
| **2x RTX 5060 Ti** | 1.3 | 26.8 | Przekroczono limit czasu |

Dwa wiersze H100 pochodzą z osobnych, prawidłowych instancji tej samej klasy GPU. Obie wyraźnie wyprzedziły pozostałe karty. Wyniki przy 32k były o 44–48% wyższe niż dla RTX PRO 5000, a przy 128k przewaga wynosiła około 61–65%.

Wyniki A100 i RTX 5060 Ti przy 32k są zbyt niskie, by oznaczały porównywalne wykonanie na GPU w tym obciążeniu. Host RTX 5060 Ti przekroczył też limit czasu podczas drugiej próby 128k. Nie traktuj go jako prawidłowego wyniku rankingu przepustowości GPU.

| Docelowy kontekst | Wynik |
|---|---|
| **32k** | Ukończono na wszystkich 10 hostach |
| **64k** | Ukończono na wszystkich 10 hostach |
| **128k** | Ukończono na 9 hostach. Druga próba na hoście 2x RTX 5060 Ti przekroczyła limit czasu |
| **256k** | Nieobsługiwane, Llama 3.1 8B obsługuje kontekst do 128K |

## Porównanie modeli

**Mniejszy model Llama był szybszy na każdej porównywalnej karcie, ale rozmiar i jakość modelu to różne cechy.** Llama 3.1 8B jest użytecznym, popularnym punktem odniesienia o mniejszym zapotrzebowaniu na pamięć. Qwen3.8 27B wymaga więcej pamięci i oferuje inny profil możliwości, więc wyniki pomagają dobrać sprzęt, lecz nie rozstrzygają, który model jest zawsze lepszy.

| Zastosowanie | Lepszy punkt odniesienia | Dlaczego |
|---|---|---|
| **Szybki asystent 8B** | Llama 3.1:8b | Większa szybkość dekodowania i mniejsze zapotrzebowanie na pamięć |
| **Dobór lokalnego modelu 27B** | Qwen3.8:27b | Lepiej odpowiada większemu obciążeniu na pojedynczym GPU |
| **Limit kontekstu 128K** | Llama 3.1:8b | Model ma jawny limit 128K, więc 256k nie jest prawidłowym celem |
| **Testowanie zapasu VRAM** | Qwen3.8:27b | Większy model szybciej ujawnia limity pamięci i długiego kontekstu |
| **Punkt odniesienia między dostawcami** | Llama 3.1:8b | Popularność i rozmiar modelu ułatwiają odtworzenie wyniku |

Wcześniejszy ponowny test Qwen poprawił też rzeczywistą liczbę tokenów promptu do około **32 770**, **65 538** i **131 074** dla obsługiwanych poziomów kontekstu. Te poprawione etykiety zastępują żądane wartości num_ctx przy porównywaniu testów Qwen.

## Około 16 tys. tokenów

**H100 SXM prowadził w krótkim kontekście z wynikiem 134,4 tokena dekodowania na sekundę.** RTX PRO 5000 osiągnął 113,9 tokena na sekundę, kosztując mniej niż połowę stawki godzinowej.

| Miejsce | GPU | VRAM | Tokeny dekodowania/s | Tokeny przetwarzania promptu/s | Stawka wynajmu |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **134.4** | 89,974 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **113.9** | 68,726 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **89.1** | 95,856 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **84.1** | 72,235 | $1.507/hr |
| 5 | **A100 SXM4** | 40 GB | **60.6** | 53,048 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **51.5** | 51,122 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **49.3** | 52,773 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | **38.4** | 38,886 | $0.565/hr |

Przy tej długości promptu RTX PRO 5000 osiągał około 84,7% szybkości dekodowania H100 przy 37,3% jego stawki godzinowej. RTX 6000 Ada osiągał około 66,3% szybkości H100 przy 30,2% stawki.

## Około 32,8 tys. tokenów

**Ranking pozostał stabilny przy średnim kontekście.** H100 SXM osiągnął 120,0 tokena na sekundę, RTX PRO 5000 uzyskał 105,0, a RTX 6000 Ada 75,7.

| Miejsce | GPU | VRAM | Tokeny dekodowania/s | Tokeny przetwarzania promptu/s | Stawka wynajmu |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **120.0** | 139,748 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **105.0** | 103,707 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **75.7** | 141,678 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **66.9** | 120,537 | $1.507/hr |
| 5 | **RTX PRO 6000 S** | 95.6 GB | **65.9** | 109,280 | $1.756/hr |
| 6 | **A100 SXM4** | 40 GB | **51.1** | 81,929 | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | **46.2** | 77,984 | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | **36.1** | 73,377 | $0.565/hr |

RTX PRO 5000 pozostał najkorzystniejszym wynajmem w tej grupie. Był tylko o 12,5% wolniejszy od H100, a kosztował o 62,7% mniej na godzinę.

## Około 65,5 tys. tokenów

**Dłuższe prompty ujawniły większą różnicę między kartami z dużą pamięcią a kartami z mniejszym zapasem.** H100 utrzymał pierwsze miejsce z wynikiem 112,0 tokena na sekundę. RTX PRO 6000 Max-Q wyprzedził RTX 6000 Ada pod względem szybkości dekodowania.

| Miejsce | GPU | VRAM | Tokeny dekodowania/s | Tokeny przetwarzania promptu/s | Stawka wynajmu |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **112.0** | 195,252 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **96.9** | 148,897 | $1.005/hr |
| 3 | **RTX PRO 6000 Max-Q** | 95.6 GB | **75.7** | 156,443 | $1.507/hr |
| 4 | **RTX 6000 Ada** | 48 GB | **70.8** | 208,400 | $0.813/hr |
| 5 | **A100 SXM4** | 40 GB | **49.3** | 147,699 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **45.9** | 118,657 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **37.0** | 124,927 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | brak | brak | $0.565/hr |

RTX PRO 5000 nadal zapewniał najlepszą równowagę w ukończonej tabeli. RTX 6000 Ada był wolniejszy, ale niższa stawka wynajmu czyniła go atrakcyjnym dla osób, którym bardziej zależy na dostępności niż na maksymalnej szybkości.

## Około 131 tys. tokenów

**Przy tym kontekście tylko H100 przekroczył 100 tokenów dekodowania na sekundę.** RTX PRO 6000 Max-Q ukończył próbę z wynikiem 73,4 tokena na sekundę, a RTX 6000 Ada osiągnął 61,7.

| Miejsce | GPU | VRAM | Tokeny dekodowania/s | Tokeny przetwarzania promptu/s | Stawka wynajmu |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **108.2** | 242,093 | $2.693/hr |
| 2 | **RTX PRO 6000 Max-Q** | 95.6 GB | **73.4** | 197,208 | $1.507/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **61.7** | 278,283 | $0.813/hr |
| 4 | **RTX PRO 6000 S** | 95.6 GB | **39.4** | 124,653 | $1.756/hr |
| 5 | **RTX PRO 5000** | 47.8 GB | brak | brak | $1.005/hr |
| 6 | **A100 SXM4** | 40 GB | brak | brak | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | brak | brak | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | brak | brak | $0.565/hr |

RTX PRO 6000 Max-Q stał się praktyczną alternatywą dla H100 przy długich promptach. Osiągnął 67,8% jego szybkości dekodowania przy 56,0% stawki godzinowej. RTX 6000 Ada kosztował mniej, lecz 48 GB VRAM pozostawiało mniej miejsca na długie prompty, większe partie lub inną konfigurację modelu.

## Zbiorcze porównanie dekodowania

| GPU | ~16 tys. | ~32,8 tys. | ~65,5 tys. | ~131 tys. |
|---|---:|---:|---:|---:|
| **H100 SXM** | **134.4** | **120.0** | **112.0** | **108.2** |
| **RTX PRO 5000** | 113.9 | 105.0 | 96.9 | brak |
| **RTX 6000 Ada** | 89.1 | 75.7 | 70.8 | 61.7 |
| **RTX PRO 6000 Max-Q** | 84.1 | 66.9 | 75.7 | 73.4 |
| **RTX PRO 6000 S** | 49.3 | 65.9 | 37.0 | 39.4 |
| **A100 SXM4** | 60.6 | 51.1 | 49.3 | brak |
| **CMP 170HX** | 51.5 | 46.2 | 45.9 | brak |
| **A100 PCIe** | 38.4 | 36.1 | brak | brak |

**H100 prowadził przy każdej ukończonej długości kontekstu.** Jego przewaga nad RTX PRO 5000 zmalała z 20,5 tokena na sekundę przy około 16k tokenach do 12,0 przy około 32,8k. Najlepsza wartość zależy od tego, czy potrzebujesz najszybszej pierwszej odpowiedzi, czy najniższego kosztu długiej sesji.

## Koszt miliona tokenów dekodowania

**Sama cena godzinowa nie pokazuje pełnego porównania.** Podzielenie stawki godzinowej przez przepustowość dekodowania daje przybliżony koszt wynajmu miliona wygenerowanych tokenów. Obliczenie pomija przetwarzanie promptu, bezczynność, pamięć masową, transfer danych, podatki, rabaty oraz nieudane lub przerwane próby.

| GPU | Stawka dla krótkiego kontekstu | Przybliżony koszt miliona tokenów dekodowania |
|---|---:|---:|
| **CMP 170HX** | $0.420/hr | $2.27 |
| **RTX PRO 5000** | $1.005/hr | $2.45 |
| **RTX 6000 Ada** | $0.813/hr | $2.53 |
| **A100 SXM4** | $0.680/hr | $3.12 |
| **A100 PCIe** | $0.565/hr | $4.09 |
| **RTX PRO 6000 Max-Q** | $1.507/hr | $4.98 |
| **H100 SXM** | $2.693/hr | $5.57 |
| **RTX PRO 6000 S** | $1.756/hr | $9.89 |

**W tym wąskim porównaniu rachunkowym wygrał CMP 170HX.** RTX PRO 5000 i RTX 6000 Ada były tuż za nim, a obie karty zapewniały większą przepustowość. Przy pracy interaktywnej dodatkowy czas oczekiwania często ma większe znaczenie niż najniższy koszt tokena.

## Wynająć GPU, kupić kredyty, wykupić subskrypcję czy kupić sprzęt?

**Właściwy wybór zależy od wykorzystania sprzętu i wymagań dotyczących kontroli.** Wynajem GPU to zmienny koszt obliczeń. Kredyty API to zmienny koszt modelu. Subskrypcja czatu ma stałą cenę i limity użycia. Własny sprzęt wymaga zakupu, a później płacenia za prąd, chłodzenie, konserwację i utratę wartości.

| Miesięczny budżet i obciążenie | Zalecana opcja | Dlaczego | Główny kompromis |
|---|---|---|---|
| **Poniżej 10 USD** | Kup kredyty API lub użyj bezpłatnego modelu lokalnego | Sprawdź sposób pracy bez kosztu bezczynnego GPU | Mniejsza kontrola nad hostowaniem modelu i limitami zapytań |
| **10–30 USD** | Kredyty API do sporadycznej pracy albo subskrypcja czatu do codziennego użycia | Subskrypcja pasuje do rozmów, a kredyty do skryptów i rozliczanych wywołań | Żadna opcja nie zapewnia domyślnie prywatnego punktu końcowego 27B |
| **30–100 USD** | Wynajmuj RTX 6000 Ada lub RTX PRO 5000 tylko na czas aktywnych sesji | Budżet wystarcza na krótkie badania bez kosztu posiadania | Instancję nadal trzeba skonfigurować, monitorować i wyłączać |
| **100–250 USD** | Wynajmij szybką kartę do zaplanowanych zadań albo przetestuj własną stację roboczą | Miesięczne użycie zaczyna pokazywać rzeczywiste wykorzystanie | Dostępność i stawki wynajmu się zmieniają |
| **250–600 USD** | Porównaj miesiąc wynajmu RTX PRO 5000 z używanym lub nowym lokalnym GPU | To punkt decyzji przy częstym, prywatnym wnioskowaniu | Sprzęt oznacza koszt energii, ciepło, obsługę i ryzyko odsprzedaży |
| **Powyżej 600 USD** | Kup sprzęt przy wysokim wykorzystaniu albo rezerwuj wynajem klasy H100 na krótkie skoki obciążenia | Łączone podejście ogranicza zakup sprzętu na sporadyczne potrzeby | Kapitał pozostaje związany z jedną konfiguracją |

Te przedziały pomagają podjąć decyzję, ale nie są ofertami dostawców. Stawki testowe pokazują punkt rentowności: H100 za 2,693 USD na godzinę kosztuje około 64,63 USD za ciągłą dobę i około 1941,00 USD za 30 dni, bez pamięci masowej i innych opłat. RTX PRO 5000 za 1,005 USD na godzinę kosztuje około 24,12 USD dziennie i 723,60 USD za 30 dni ciągłej pracy. Wynajem tylko na aktywne sesje daje inny koszt niż pozostawienie GPU uruchomionego przez cały miesiąc.

### Kiedy opłacają się kredyty API

**Kredyty API opłacają się przy nieregularnym użyciu, automatyzacji i zadaniach, które nie wymagają konkretnego modelu lokalnego.** Pozwalają uniknąć uruchamiania GPU, pobierania modeli, problemów ze sterownikami i kosztu bezczynności. Ułatwiają też porównanie hostowanych modeli przed zakupem sprzętu.

Ceny API zależą od modelu i dostawcy. Katalog modeli OpenRouter służy do porównywania długości kontekstu, dostawców i stawek za tokeny. Przed zestawieniem rachunku API z tym testem użyj aktualnego kalkulatora dostawcy. Lokalna karta generuje tokeny bez opłaty dostawcy za każdy token, ale godzina wynajmu biegnie także podczas oczekiwania instancji.

### Kiedy opłaca się subskrypcja

**Subskrypcja pasuje osobie, która codziennie korzysta z hostowanego asystenta.** Przykładowo aktualne plany indywidualne Claude obejmują bezpłatny dostęp oraz poziomy Pro i Max z różnymi limitami i funkcjami. Subskrypcja to nie to samo co API. Zwykle daje wygodny interfejs i zestaw narzędzi, a kredyty API zapewniają sterowanie programowe.

Wybierz subskrypcję, gdy praca polega głównie na interaktywnym pisaniu, badaniu, programowaniu lub analizie plików. Wybierz kredyty API, gdy skrypt, aplikacja albo agent potrzebuje rozliczanego według użycia punktu końcowego.

### Kiedy opłaca się Vast.ai

**Vast.ai sprawdza się, gdy potrzebujesz otwartego modelu, kontroli nad środowiskiem lub krótkiego skoku przepustowości.** Wybierasz GPU, uruchamiasz instancję i Ollama, testujesz model, a potem wyłączasz instancję. To dobra droga dla Qwen3.8 27B, wariantów abliterated i innych plików modeli, które nie mieszczą się na laptopie konsumenckim.

Koszt obejmuje też pracę operacyjną. Sprawdź, czy model korzysta z GPU, obserwuj VRAM, zabezpiecz wystawioną usługę, zachowaj potrzebne pliki modeli i zatrzymaj instancję po teście. Niska stawka godzinowa nie pomoże, jeśli zapomnisz wyłączyć instancję.

### Kiedy opłaca się zakup GPU

**Zakup sprzętu opłaca się przy dużym i stabilnym wykorzystaniu oraz potrzebie lokalnej kontroli.** Zakup usuwa ryzyko braku instancji na wynajem i zapewnia stałe środowisko. Pozwala też uruchamiać prywatne dane bez wysyłania promptów do hostowanego dostawcy.

Cena zakupu to tylko część kosztu. Uwzględnij komputer, zasilacz, pamięć masową, chłodzenie, energię elektryczną, ryzyko awarii oraz czas konfiguracji. Droga karta będzie bezczynna w okresach, gdy kredyty API lub subskrypcja kosztowałyby mniej.

Specyfikacja referencyjna NVIDIA RTX 4090 podaje 24 GB pamięci, 450 W mocy karty graficznej i zalecane zasilanie systemu o mocy co najmniej 850 W. To użyteczny punkt odniesienia dla lokalnego wnioskowania, ale 24 GB nie wystarcza do konfiguracji Q4_K_M modelu 27B testowanych tutaj. Sprawdź rzeczywiste zużycie pamięci modelu, zamiast zakładać, że karta pasuje na podstawie samej liczby parametrów.

## Modele abliterated i bez cenzury

**Warianty abliterated i uncensored zmieniają decyzję zakupową.** Często kuszą mniejszą liczbą odmów lub ograniczeń. Mogą jednak słabiej przestrzegać zasad bezpieczeństwa, mieć niepewne pochodzenie, niespójne formatowanie promptów, wymagać dokładniejszej kontroli albo podlegać ograniczeniom licencyjnym i zasadom użycia.

Najpierw wynajmij kartę. Jednodniowy test RTX PRO 5000 przy podanej stawce kosztuje około 24,12 USD przed innymi opłatami. Wystarczy, by sprawdzić zgodność modelu, użycie GPU, jakość odpowiedzi i ryzyko operacyjne.

**Nie wystawiaj modelu uncensored bezpośrednio do publicznego internetu.** Zastosuj uwierzytelnianie, limity zapytań, kontrolę logowania i izolację sieci. Nie wysyłaj danych osobowych, poufnych ani regulowanych do źródła modelu, którego nie sprawdziłeś.

Jeśli model stanie się codziennym narzędziem, porównaj miesięczny koszt wynajmu z pełnym kosztem własnej stacji roboczej. Przy okazjonalnym użyciu wynajem łatwiej zakończyć lub zmienić.

## Ograniczenia testu

**Brakujące wyniki też są częścią wyniku.** Wartość N/A oznacza, że próba nie dała prawidłowego pomiaru. Nie oznacza, że GPU jest wolny o różnicę sugerowaną przez wynik innej karty.

- **Druga instancja H100 nie dała prawidłowego zestawu wyników**, ponieważ pobieranie modelu zakończyło się zbyt późno.
- **Pominięto instancję 2x RTX 5060 Ti**, ponieważ Ollama uruchomił model na CPU zamiast na GPU.
- **Nie ukończono promptu Qwen3.8 27B o długości 256k tokenów.** Najwyższy prawidłowy poziom wyniósł około 131k rzeczywistych tokenów promptu. Llama 3.1 8B nie obsługuje 256k, ponieważ limit kontekstu wynosi 128K.
- **Żądanej wartości num_ctx nie użyto jako etykiety rankingu.** Końcowe tabele pokazują rzeczywiste wartości prompt_eval_count.
- **Dwie prawidłowe próby dla każdego kontekstu podsumowano medianą szybkości dekodowania.** Ogranicza to wpływ pojedynczego wolnego testu, ale nie zastępuje większego zestawu prób.
- **Celowo użyto prostego interfejsu.** Dostrojone wdrożenie vLLM lub llama.cpp da inny ranking.

## Końcowa rekomendacja

**Zacznij od wynajmu RTX 6000 Ada lub RTX PRO 5000.** RTX 6000 Ada jest budżetową opcją, gdy dostępna jest stawka 0,813 USD za godzinę. RTX PRO 5000 oferuje większą szybkość poniżej ceny H100. Użyj H100 SXM przy długich promptach, wymagającej interaktywnej latencji lub krótkim oknie testowym, gdy czas jest ważniejszy od kosztu. Przy modelu 8B warto sprawdzić CMP 170HX, jeśli niska stawka godzinowa liczy się bardziej niż szczytowa szybkość.

**Nie kupuj GPU po jednym udanym teście.** Przez miesiąc testuj rzeczywiste zadania, zapisuj aktywne godziny, długości promptów, równoległość i zmiany modeli, a potem porównaj koszt wynajmu z pełnymi kosztami posiadania. Kup sprzęt, gdy obciążenie jest częste i stabilne na tyle, by uzasadniało mniejszą elastyczność.

Przy okazjonalnej pracy prostsze będą kredyty API lub subskrypcja czatu. Do prywatnego lokalnego wnioskowania, eksperymentów z otwartymi modelami lub testów modeli abliterated Vast.ai wymaga mniejszego zaangażowania niż natychmiastowy zakup stacji roboczej. Używaj Llama 3.1 8B jako punktu odniesienia dla mniejszej pamięci, a Qwen3.8 27B wtedy, gdy to większy model ma być wdrożony.

## Następne kroki

Powtórz porównanie z własnymi długościami promptów i szacunkiem aktywnych godzin. Sprawdź użycie GPU, zapisz wersję modelu i środowiska, wyłącz instancję po każdej próbie i porównaj miesięczny koszt wynajmu z pełnym kosztem posiadania przed zakupem sprzętu.

## Źródła

1. [Chmurowy rynek GPU Vast.ai](https://vast.ai/)
2. [Dokumentacja Vast.ai: rynek, instancje, ceny i rodzaje wynajmu](https://docs.vast.ai/)
3. [Biblioteka modeli Qwen3 w Ollama](https://ollama.com/library/qwen3)
4. [Strona modelu Llama 3.1 8B w Ollama](https://ollama.com/library/llama3.1:8b)
5. [Katalog modeli OpenRouter i porównanie cen](https://openrouter.ai/models)
6. [Ceny Claude i plany subskrypcji indywidualnej](https://www.anthropic.com/pricing)
7. [Specyfikacja NVIDIA GeForce RTX 4090](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/)
8. [Lokalna AI w 2026 roku: Qwen3.8 27B i sprzęt do samodzielnego hostowania modeli](/articles/local-ai-2026-build-your-rig-now/)
9. [Testowanie modeli Ollama na sprzęcie Raspberry Pi](/articles/ai-models-raspberry-pi-4-5/)
