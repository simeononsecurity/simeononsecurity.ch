---
title: "2x RTX 5060 Ti kontra GB10: lokalny benchmark AI pięciu modeli przy kontekście 256K"
date: 2026-10-10
lastmod: 2026-11-07
toc: true
draft: false
description: "Porównanie RTX 5060 Ti z GB10 dla pięciu modeli oraz benchmark Qwen3.8 Flash-Next na Strata, wykonany na tym samym hoście przy kontekście do 256K."
genre: ["Sztuczna inteligencja", "Lokalna AI", "Sprzęt GPU", "Benchmarki", "Sprzęt komputerowy"]
tags: ["RTX 5060 Ti", "GB10", "DGX Spark", "Qwen3.8", "Qwen3.8 Flash-Next", "GSQ-RCO", "Qwen4Exp", "Strata", "Qwen3.5", "Qwen3.6", "GPT-OSS", "Nemotron", "lokalne LLM", "lokalne wnioskowanie", "pamięć współdzielona", "VRAM", "benchmark GPU", "długi kontekst", "narzut PCIe", "sprzęt AI", "NVIDIA Blackwell", "wydajność LLM", "pamięć GPU"]
cover: "/img/cover/nvidia-rtx-5060-ti-vs-gb10-memory-performance-comparison.webp"
coverAlt: "Ilustracja przedstawia dwie karty graficzne NVIDIA RTX 5060 Ti po lewej i system NVIDIA GB10 po prawej, wyróżnione żywymi kolorami na ciemnym tle."
coverCaption: "Wydajność lokalnego modelu zależy od architektury pamięci, wyboru modelu i długości kontekstu."
---

**Dwie karty RTX 5060 Ti z 16 GB pamięci zapewniają łącznie 32 GB VRAM.** System NVIDIA GB10 udostępnia 128 GB spójnej pamięci zunifikowanej. Nowy benchmark pięciu modeli daje bardziej zrównoważony obraz niż wcześniejszy test obejmujący wyłącznie Qwen.

Przy ustawieniu 256K system z dwiema kartami osiąga wyższą szybkość generowania dla czterech z pięciu modeli. GB10 wyraźnie wygrywa w przypadku Qwen3.8 27B i zostawia więcej pamięci na modele, kontekst oraz przydziały środowiska uruchomieniowego. Najlepszy wybór zależy od modelu i obciążenia.

Osobny test na tym samym hoście porównał Qwen3.8-Flash-Next IQ2_XS uruchomiony w Strata z gęstym Qwen3.8 27B Q4_K_M w Ollama. Mediana szybkości generowania po rozgrzewce wyniosła 92,8 tokena na sekundę dla Flash-Next przy prompcie o długości 260 446 tokenów. Gęsty Qwen3.8 osiągnął 0,939 tokena na sekundę przy prompcie o długości 260 444 tokenów.

NVIDIA GB10 korzysta ze 128 GB spójnej pamięci zunifikowanej. NVIDIA podaje dla platformy GB10 128 GB pamięci zunifikowanej LPDDR5x i TDP układu 140 W. Każda karta RTX 5060 Ti ma 16 GB pamięci GDDR7, 128-bitowy interfejs pamięci i deklarowaną moc graficzną 180 W. Różnicę sprzętową opisują [specyfikacja NVIDIA RTX 5060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/) i [specyfikacja NVIDIA GB10](https://www.nvidia.com/en-us/products/workstations/dgx-spark/).

**Oba systemy udostępniają pamięć w inny sposób.** Dwie karty tworzą dwie oddzielne pule po 16 GB. GB10 umieszcza model, dane kontekstu, bufory środowiska uruchomieniowego i przydziały systemu operacyjnego we wspólnej przestrzeni adresowej.

## Porównanie pamięci

| System | Pamięć | Typ pamięci | Podana moc |
|---|---:|---|---:|
| **2x RTX 5060 Ti 16 GB** | 32 GB łącznie | Dwie oddzielne pule pamięci GPU | Łącznie 360 W GPU |
| **System GB10** | 128 GB | Spójna pamięć systemowa zunifikowana | TDP GB10 140 W |

GB10 nie wygrywa każdego testu przepustowości, ponieważ LPDDR5x nie dorównuje przepustowości pamięci dyskretnych GPU. Jego przewaga wynika z pojemności i rozmieszczenia danych. CPU i GPU współdzielą przestrzeń adresową, więc zestaw roboczy nie musi mieścić się w dwóch odizolowanych urządzeniach po 16 GB.

System z dwiema kartami ma problem z rozmieszczeniem danych. Model trzeba podzielić między obie karty, a środowisko uruchomieniowe musi przenosić między nimi dane. Ruch PCIe zwiększa opóźnienie i zużywa przepustowość. Według specyfikacji NVIDIA RTX 5060 Ti nie obsługuje również NVLink.

## Benchmark pięciu modeli

W zaktualizowanym teście oba systemy otrzymały tę samą macierz żądań. Obejmowała pięć modeli Ollama i ustawienia kontekstu 4K, 16K, 32K, 64K, 128K oraz 256K. Każde żądanie wygenerowało 128 tokenów przy temperaturze 0.

Użyte tagi modeli:

- **Qwen3.8 27B:** `qwen3.8:27b`
- **GPT-OSS 20B:** `gpt-oss:20b`
- **Qwen3.6 35B-A3B:** `qwen3.6:35b`
- **Qwen3.5 35B-A3B:** `qwen3.5:35b-a3b-q4_K_M`
- **Nemotron 3.5 Lightning 30B-A3B:** `nemotron-3.5-lightning:30b-a3b-q4_K_M`

System z dwiema kartami korzystał z dwóch RTX 5060 Ti po 16 GB. System GB10 używał 128 GB pamięci zunifikowanej. Testy uruchomiono w Ollama: wersja 0.34.2 działała w systemie dwukartowym, a wersja 0.40.2 w GB10.

### Szybkość generowania

Szybkość generowania mierzy liczbę tokenów utworzonych po przetworzeniu promptu. Ten wskaźnik ma największe znaczenie podczas interaktywnej rozmowy.

System z dwiema kartami RTX 5060 Ti:

| Kontekst | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 91.518 | 162.027 | 117.547 | 156.104 | 55.654 |
| 16K | 87.176 | 161.377 | 112.903 | 140.596 | 51.656 |
| 32K | 82.372 | 157.055 | 106.455 | 144.833 | 47.369 |
| 64K | 74.661 | 135.106 | 95.979 | 125.008 | 38.863 |
| 128K | 62.767 | 130.924 | 79.572 | 115.352 | 26.399 |
| 256K | 67.853 | 106.221 | 58.947 | 67.159 | 1.079 |

GB10:

| Kontekst | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 62.199 | 98.648 | 72.405 | 100.906 | 32.985 |
| 16K | 56.764 | 94.366 | 69.782 | 95.448 | 32.939 |
| 32K | 53.257 | 98.175 | 64.055 | 95.025 | 29.772 |
| 64K | 49.201 | 96.132 | 58.428 | 84.528 | 25.625 |
| 128K | 40.637 | 80.238 | 48.108 | 74.579 | 22.294 |
| 256K | 43.688 | 68.043 | 36.649 | 62.115 | 22.371 |

Przy 256K system dwukartowy generował szybciej w przypadku GPT-OSS, Nemotron, Qwen3.5 i Qwen3.6. GB10 miał dużą przewagę przy Qwen3.8. W systemie dwukartowym Qwen3.8 spadł do 1,079 tokena na sekundę, podczas gdy GB10 osiągnął 22,371 tokena na sekundę.

Wyniki Qwen3.6 są zbliżone. System dwukartowy osiągnął 67,159 tokena na sekundę, a GB10 62,115. Ten wynik nie uzasadnia ogólnego twierdzenia, że pamięć zunifikowana zawsze wygrywa albo że zawsze wygrywają dwa dyskretne GPU.

### Szybkość przetwarzania promptu

Przetwarzanie promptu mierzy szybkość odczytu kontekstu wejściowego przez środowisko uruchomieniowe przed generowaniem. Ma znaczenie przy długich dokumentach i ponownym wczytywaniu kontekstu.

System z dwiema kartami RTX 5060 Ti:

| Kontekst | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 4745.9 | 2409.0 | 2701.7 | 464.3 | 783.9 |
| 16K | 7617.0 | 3031.8 | 4175.3 | 2654.0 | 840.1 |
| 32K | 8099.5 | 3074.2 | 4335.8 | 2623.2 | 811.2 |
| 64K | 6809.5 | 2893.0 | 4129.9 | 2400.4 | 727.8 |
| 128K | 5089.9 | 2362.7 | 3084.0 | 1723.6 | 546.1 |
| 256K | 5838.3 | 1813.2 | 2229.1 | 1011.0 | 251.3 |

GB10:

| Kontekst | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 3295.5 | 576.0 | 2067.9 | 628.8 | 756.9 |
| 16K | 4675.5 | 3006.7 | 2691.2 | 2556.3 | 812.6 |
| 32K | 4571.4 | 3077.9 | 2691.7 | 2563.9 | 794.1 |
| 64K | 3704.7 | 3066.9 | 2585.3 | 2444.9 | 714.0 |
| 128K | 2857.0 | 2802.9 | 2360.4 | 2229.9 | 655.5 |
| 256K | 3243.4 | 2325.4 | 1938.5 | 1817.6 | 535.1 |

Przy 256K system dwukartowy prowadził w przetwarzaniu promptu dla GPT-OSS i Qwen3.5. GB10 osiągnął lepszy wynik dla Nemotron, Qwen3.6 i Qwen3.8. Architektura modelu i zachowanie środowiska uruchomieniowego są równie ważne jak interfejs pamięci.

## Dodatkowe benchmarki Qwen3.8 Flash-Next

Trzy dodatkowe testy zmierzyły pakiety Qwen3.8 Flash-Next GGUF w systemie z dwiema kartami RTX 5060 Ti przy kontekście 4K i 16K. Każdy wiersz zawiera dokładne oznaczenie modelu w Hugging Face i jego kwantyzację.

| Dokładny model | Kwantyzacja | Generowanie 4K | Generowanie 16K |
|---|---:|---:|---:|
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS) | IQ2_XS | 31.77 tok/s | 28.20 tok/s |
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ3_S) | IQ3_S | 24.54 tok/s | 22.60 tok/s |
| [`hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M`](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF/tree/main) | Q4_K_M | 17.91 tok/s | 17.02 tok/s |

Pakiet IQ2_XS osiągnął w tej grupie najwyższą przepustowość. Przy 4K uzyskał 31,77 tokena na sekundę, wobec 24,54 dla IQ3_S i 17,91 dla Q4_K_M. Przy 16K kolejność pozostała taka sama: 28,20, 22,60 i 17,02 tokena na sekundę.

Uruchom te same dokładne oznaczenia modeli w Ollama:

```bash
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S
ollama run hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M
```

Te wcześniejsze dodatkowe wyniki pochodzą z systemu dwuprocesorowego. Nie należą do przedstawionej wyżej macierzy żądań porównującej RTX 5060 Ti z GB10. Dostarczony zapis podaje dokładne oznaczenia modeli, kwantyzacje, wymagane ustawienia kontekstu i szybkość generowania. Brakuje w nim rozstrzygniętych skrótów manifestów, liczby przetworzonych tokenów promptu, długości odpowiedzi, stanu rozgrzania, podziału urządzeń, procesora, pamięci RAM, konfiguracji chłodzenia i daty pomiaru.

## Strata kontra gęsty model w Ollama przy 256K

**Drugi benchmark z 14 października 2026 r. porównał dwa zestawy modeli i środowisk uruchomieniowych na tym samym hoście z dwiema kartami RTX 5060 Ti.** Gęstym modelem bazowym było [`qwen3.8:27b`](https://ollama.com/library/qwen3.8:27b), model Qwen35 z 27,3 mld parametrów w kwantyzacji Q4_K_M. Zestaw Flash używał [Qwen3.8-Flash-Next IQ2_XS](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS), modelu Qwen4Exp typu mixture-of-experts w zunifikowanym natywnym pakiecie Strata.

To porównanie całych stosów. Jednocześnie zmieniły się architektura modelu, kwantyzacja, pakiet, routing ekspertów i silnik wnioskowania. Warianty Flash IQ3_S i Q4_K_M nie wchodziły w zakres tej próby.

### System testowy i metoda

| Komponent | Zapisana konfiguracja |
|---|---|
| **GPU** | 2x NVIDIA GeForce RTX 5060 Ti, po 16 GiB, compute capability 12.0 |
| **Połączenie GPU** | PCIe 4.0 x4 na kartę, topologia PHB, bez NVLink |
| **CPU** | AMD Ryzen 9 5900XT, 32 wątki |
| **Pamięć hosta** | 62 GiB RAM i 15 GiB swap |
| **Sterownik NVIDIA** | 595.99.02 |

Harmonogram testu wygenerował syntetyczne rekordy z numerami. Każdy wiersz miał format `Record 00001: alpha beta gamma delta epsilon zeta eta theta iota kappa.` Instrukcja wymagała umieszczenia `BENCHMARK_OK` na początku, a następnie krótkiej syntezy technicznej do limitu wyjściowego. Sześć promptów zawierało 180, 720, 1 500, 3 100, 6 200 i 12 400 rekordów.

Każdy test używał temperatury 0, ziarna 42 i maksymalnej długości wyjścia 128 tokenów. Przy każdym kontekście po jednej rozgrzewce wykonano pięć mierzonych żądań. Testy Ollama korzystały z `/api/generate`, a testy Strata z `/v1/chat/completions`. Wszystkie mierzone żądania zakończyły się bez błędów API.

Ustawienia dekodowania nie były dopasowane. Strata jawnie ustawiła `reasoning_effort` na `none` i wyłączyła myślenie za pomocą szablonu czatu. Żądanie dla gęstego modelu w Ollama nie zawierało `think: false`, a dodatkowa próba wykazała gęste wyjście w polach myślenia i odpowiedzi. Wynik generowania należy traktować jako właściwy dla tych trybów dekodowania.

| Ustawienie kontekstu | Tokeny promptu, model gęsty | Tokeny promptu, Flash |
|---:|---:|---:|
| **4K** | 3,824 | 3,826 |
| **16K** | 15,164 | 15,166 |
| **32K** | 31,544 | 31,546 |
| **64K** | 65,144 | 65,146 |
| **128K** | 130,244 | 130,246 |
| **256K** | 260,444 | 260,446 |

Nagłówki obu modeli deklarowały maksymalny kontekst 262 144 tokenów. Sparowane prompty różniły się o dwa tokeny w każdym punkcie kontrolnym.

### Mediana szybkości generowania po rozgrzewce

Każda mediana obejmuje pięć mierzonych żądań po jednej rozgrzewce. Każde mierzone żądanie gęstego modelu ponownie wykorzystywało wszystkie tokeny promptu poza czterema. Każde żądanie Flash pomijało w ponownym użyciu siedem tokenów. Tabela przedstawia przepustowość dekodowania po rozgrzaniu i z pamięcią podręczną prefiksu. Nie przedstawia zimnego opóźnienia od początku do końca.

| Kontekst | Flash IQ2_XS w Strata | Gęsty Q4_K_M w Ollama | Przewaga Flash |
|---:|---:|---:|---:|
| **4K** | 98.4 tok/s | 65.0 tok/s | 1.51x |
| **16K** | 96.8 tok/s | 60.6 tok/s | 1.60x |
| **32K** | 95.3 tok/s | 64.4 tok/s | 1.48x |
| **64K** | 89.6 tok/s | 51.2 tok/s | 1.75x |
| **128K** | 92.9 tok/s | 31.5 tok/s | 2.95x |
| **256K** | 92.8 tok/s | 0.939 tok/s | 98.9x |

Zestaw Flash utrzymywał około 90 tokenów na sekundę w zakresie od 64K do 256K. Gęsty Qwen3.8 wyraźnie zwolnił po 64K i przy 256K osiągnął 0,939 tokena na sekundę. Odpowiedź Flash dla 256K zakończyła się normalnie po 67 tokenach. Gęsty model osiągnął limit wyjścia wynoszący 128 tokenów.

### Przetwarzanie promptu w pierwszym żądaniu

| Kontekst | Pierwsze żądanie Flash | Pierwsze żądanie, model gęsty |
|---:|---:|---:|
| **4K** | 1,134 tok/s | 832 tok/s |
| **16K** | 2,013 tok/s | 856 tok/s |
| **32K** | 2,386 tok/s | 799 tok/s |
| **64K** | 2,509 tok/s | 690 tok/s |
| **128K** | 2,538 tok/s | 489 tok/s |
| **256K** | 2,399 tok/s | 214 tok/s |

Pierwsze żądanie gęstego modelu przetwarzało pełny prompt w każdym punkcie kontrolnym. Strata zgłosiła ponowne wykorzystanie 16 384 tokenów prefiksu przy 64K, 49 152 przy 128K i 114 688 przy 256K. Szybkości Flash od 64K do 256K należy traktować jako przepustowość kontynuacji pierwszego żądania, a nie wstępne przetwarzanie bez pamięci podręcznej.

Przy 256K Strata przetworzyła pierwsze żądanie w 60,8 sekundy. Ollama potrzebowała około 1 215,4 sekundy. Ponowne użycie prefiksu uniemożliwia bezpośrednie porównanie zimnego przetwarzania wstępnego w tym punkcie.

### Rozmieszczenie środowiska uruchomieniowego wyjaśnia różnicę przy długim kontekście

Ollama 0.34.2 korzystała z llama-server 0.4.1-dev, przenoszenia warstw CUDA, szablonu ChatML i spekulacyjnego dekodowania MTP z maksymalną szerokością szkicu równą cztery. Rozmiar partii i mikropartii wynosił 1 024 przy 32K oraz 512 w zakresie od 64K do 256K. Przy 32K i 64K wszystkie 66 gęstych warstw działało na GPU. Przy 128K na GPU pozostały 63 z 66 warstw, a 1 404 MiB przeniesiono do pamięci mapowanej na CPU. Przy 256K na GPU pozostały 42 z 66 warstw, a 6 002 MiB przeniesiono do pamięci mapowanej na CPU. Współczynnik akceptacji MTP przy 256K wynosił około 69,4%.

Strata 0.1.44.1 z CUDA 13.0.3 utrzymywała 48 warstw podzielonych między oba GPU. Konfiguracja 4K i 16K umieszczała warstwy od 0 do 23 na pierwszym GPU, a warstwy od 24 do 47 na drugim. Ta próba używała automatycznej rezerwy 700 MiB VRAM i 16 047 rezydentnych miejsc dla ekspertów.

Konfiguracja od 32K do 256K umieszczała warstwy od 0 do 24 na pierwszym GPU, a warstwy od 25 do 47 na drugim. Ta próba używała automatycznego przetwarzania wstępnego, minimalnego prawdopodobieństwa spekulacyjnego 0,5, pamięci KV INT8, 32 768 rezydentnych komórek KV na warstwę QSA, rezerwy 832 MiB VRAM, pamięci podręcznej ekspertów z 15 318 miejscami i pojemnością 21 024 MiB oraz spekulacyjnego dekodowania MTP z maksymalną szerokością szkicu równą cztery.

Skrót bloba natywnego Strata i PLE wynosił `sha256:1473e0664c2017095f9164b6d617d7a71893452c1180c83002c4f28fc8c2b0da`. Test zależał również od profilu ekspertów i pakietu szkiców MTP, dla których nie opublikowano niezmiennych skrótów.

Test Strata używał domyślnego trybu pomijania końcówki routingu. To ustawienie nieznacznie zmienia wyjście modelu i sprawia, że wynik dotyczy konkretnej zapisanej konfiguracji środowiska uruchomieniowego. Odpowiedzi Flash zawierały znacznik `BENCHMARK_OK`. Żądania gęstego modelu nie zwróciły błędów API, ale główny harmonogram nie przechwycił znacznika. Surowe wiersze zapisywały zero znaków odpowiedzi. Dodatkowa próba wykazała wyjście w polach odpowiedzi i myślenia oraz potwierdziła `BENCHMARK_OK` w odpowiedzi.

Konfiguracja 4K i 16K zapisała jedno żądanie przy 409 MiB wolnej pamięci i zaleciła rezerwę 832 MiB. Konfiguracja długiego kontekstu zapisała jedno żądanie przy 481 MiB wolnej pamięci i zaleciła rezerwę 896 MiB. Obie wartości były niższe od progu stronicowania sterownika wynoszącego 512 MiB. Żadne żądanie nie zakończyło się błędem, lecz tak mały zapas pamięci wpływa na powtarzalność.

**Wynik 98,9x traktuj jako rezultat długiego kontekstu dla całego stosu, a nie dowód na 98,9-krotną przewagę samego silnika.** Test odizolowuje host, ale nie model, kwantyzację ani środowisko uruchomieniowe.

## Rzeczywista długość promptu ma znaczenie

Wymagane ustawienie kontekstu nie jest równoznaczne z liczbą przetworzonych tokenów promptu. Przy ustawieniu 256K testy Qwen3.5, Qwen3.6, Nemotron i Qwen3.8 przetworzyły w obu systemach około 171 359 do 171 365 rzeczywistych tokenów promptu.

Przy ustawieniu 256K GPT-OSS przetworzył w obu systemach 65 538 rzeczywistych tokenów promptu. Wiersz 256K dla tego modelu nie odpowiada więc takiej samej długości wejścia jak wyniki pozostałych modeli.

Wynik Qwen3.8 przy 256K pokazuje największą różnicę. System dwukartowy przetworzył 171 359 tokenów promptu z szybkością 251,3 tokena na sekundę, a następnie generował z szybkością 1,079 tokena na sekundę. GB10 przetworzył tyle samo tokenów promptu z szybkością 535,1 tokena na sekundę i generował z szybkością 22,371 tokena na sekundę.

**Ustawienie kontekstu określa wymagany limit.** Rzeczywista liczba tokenów promptu pokazuje obciążenie ukończone przez środowisko uruchomieniowe.

## Dlaczego łączna pojemność VRAM nadal ma znaczenie

### 1. Model nie widzi jednej karty 32 GB

Dwa GPU nie łączą pamięci w jedną lokalną przestrzeń adresową. Środowisko model-parallel dzieli warstwy lub tensory między urządzenia. Każde urządzenie nadal potrzebuje miejsca na przypisane mu wagi, bufory tymczasowe i część stanu kontekstu.

Użyteczna pojemność jest mniejsza, niż sugeruje prosta suma. Dokładny narzut zależy od formatu modelu, kwantyzacji, backendu wnioskowania, podziału tensorów i długości kontekstu.

### 2. Pamięć kontekstu rośnie podczas generowania

Wagi modelu stanowią tylko część budżetu pamięci. Pamięć podręczna klucz-wartość (KV cache) przechowuje dane mechanizmu attention dla wcześniejszych tokenów. Dłuższy kontekst wymaga większej pamięci podręcznej. Test 4K nie przewiduje zachowania wdrożenia 128K ani 256K.

Nowe wyniki pokazują różne punkty załamania zależnie od modelu. Przy 256K szybkość generowania Qwen3.8 drastycznie spada w systemie dwukartowym. Pozostałe cztery modele utrzymują użyteczną szybkość generowania w obu systemach. Pojemność pamięci nadal ma znaczenie, ponieważ określa, które kombinacje modelu i kontekstu mieszczą się wraz z przydziałami środowiska uruchomieniowego.

### 3. Transfery PCIe zwiększają narzut

Gdy środowisko uruchomieniowe przenosi aktywacje lub tensory między GPU, transfer przebiega przez interkonekt hosta. Powoduje to punkty synchronizacji i zwiększa opóźnienie każdego kroku. Kara zależy od rozmieszczenia tensorów, architektury modelu, kwantyzacji i długości kontekstu.

Nie oznacza to, że system z dwoma GPU jest bezużyteczny. Wynik zależy od konfiguracji środowiska uruchomieniowego i modelu. Benchmark podający wyłącznie przetwarzanie promptu przy 4K pomija ten koszt.

### 4. Efektywność energetyczna nadal daje przewagę na poziomie systemu

GB10 ma niższą deklarowaną moc układu lub GPU i zapewnia większą pojemność pamięci. Dwie karty RTX 5060 Ti mają łącznie deklarowaną moc GPU 360 W, bez uwzględnienia reszty systemu. NVIDIA podaje TDP GB10 na poziomie 140 W.

**GB10 poświęca szczytową przepustowość kilku modeli na rzecz większej pojemności, wspólnego zestawu roboczego i niższej deklarowanej mocy GPU.** System dwukartowy osiąga większą zmierzoną przepustowość w przypadku kilku nowszych modeli MoE.

## System 5060ti-x2 kosztuje znacznie mniej

Kompletna stacja robocza z dwiema kartami RTX 5060 Ti 16 GB kosztowała **3 479 USD** według oferty z 10 października 2026 r. Konfiguracja obejmuje Intel Ultra 7 265K, płytę główną Z890, 32 GB DDR5, dysk 1 TB, zasilacz 1 000 W i obie karty GPU. [Zobacz ofertę kompletnej stacji roboczej z dwoma GPU](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white).

Amerykański sklep NVIDIA podaje cenę DGX Spark z 128 GB pamięci jako **6 950 USD**. Oferta obejmuje 128 GB spójnej pamięci zunifikowanej i 4 TB pamięci NVMe, ale system jest oznaczony jako niedostępny. [Sprawdź bieżącą ofertę DGX Spark w NVIDIA](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/).

Platforma deweloperska AMD Ryzen AI Halo stanowi kolejny punkt odniesienia. Ten system Strix Halo kosztuje **3 999,99 USD** w Micro Center i ma 128 GB pamięci zunifikowanej LPDDR5x oraz 2 TB pamięci masowej. Strix Halo często należy do tej samej praktycznej klasy lokalnych systemów AI co GB10, choć niezależne testy często wskazują przewagę GB10 w przepustowości i dojrzałości oprogramowania. [Sprawdź bieżącą ofertę wersji Linux w Micro Center](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false) i [przeczytaj recenzję Strix Halo kontra GB10](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4).

| Kompletny system | Cena w ofercie z 10 października 2026 r. | Różnica ceny |
|---|---:|---:|
| **Stacja robocza 5060ti-x2** | $3,479 | Punkt odniesienia |
| **AMD Ryzen AI Halo, Strix Halo** | $3,999.99 | O $520.99 więcej |
| **128 GB GB10 DGX Spark** | $6,950 | O $3,471 więcej |

GB10 zapewnia większą pulę pamięci zunifikowanej i niższą deklarowaną moc GPU. System AMD oferuje tę samą klasę 128 GB pamięci za około 4 000 USD. Cena stacji 5060ti-x2 nadal wynosi około **50% ceny GB10 podanej w ofercie**, przed podatkiem i wysyłką.

To ceny z ofert różnych sprzedawców, a nie porównanie kontrolowanego koszyka detalicznego. System 5060ti-x2 ma też mniej pamięci systemowej i miejsca na dane. Obecne oferty kart RTX 5060 Ti 16 GB wynoszą około **789–830 USD za sztukę**, znacznie powyżej początkowej ceny katalogowej 429 USD. Przewaga cenowa systemu dwukartowego utrzymuje się więc mimo obecnego skoku cen GPU. [Bieżące ceny RTX 5060 Ti](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/).

## Znaczenie dla lokalnych obciążeń AI

Konfiguracja dwóch kart 16 GB uruchamia kilka skwantyzowanych modeli 27B–35B przy długich ustawieniach kontekstu. Benchmark nie wskazuje jednego zwycięzcy dla wszystkich modeli.

Wybierz system dwukartowy, jeśli zależy Ci na:

- **Większej szybkości generowania GPT-OSS, Nemotron, Qwen3.5 i Qwen3.6** w tym teście.
- **Większej przepustowości przy krótkim kontekście** dla pięciu modeli.
- **Niższym koszcie zakupu** w porównaniu z GB10 z oferty.
- **Kompatybilności oprogramowania z dyskretnymi GPU NVIDIA** i możliwości testowania kolejnych modeli.

Wybierz GB10, jeśli zależy Ci na:

- **Qwen3.8 27B przy 256K**, gdzie GB10 generuje ponad 20 razy szybciej.
- **Jednej puli pamięci 128 GB** z większą ilością miejsca na wagi modelu, pamięć KV i bufory środowiska uruchomieniowego.
- **Niższej deklarowanej mocy GPU lub układu** niż w przypadku dwóch oddzielnych kart.
- **Mniejszych ograniczeniach rozmieszczenia na wielu urządzeniach** dla modeli obciążających konfigurację dwukartową.

Zgadza się to z zaleceniami doboru sprzętu w artykule [Czy 16 GB VRAM wystarczy do poważnej pracy z lokalnymi LLM?](/articles/is-16gb-vram-enough-local-llm/), który traktuje wagi, kontekst i przydziały środowiska uruchomieniowego jako jeden budżet. [Przewodnik po 32 GB VRAM dla Qwen 27B](/articles/32gb-vram-qwen-27b-hardware-guide/) dochodzi do tego samego wniosku dla konfiguracji dwukartowych. Łączna pojemność nie oznacza dostępnego zapasu pamięci.

Przed zakupem sprzętu do wdrożenia z długim kontekstem zadaj cztery pytania:

- **Czy wybrana kwantyzacja mieści się wraz z buforami środowiska uruchomieniowego?** Same wagi modelu nie określają zapotrzebowania na pamięć.
- **Czy kontekst mieści się bez nadmiernego obciążenia pamięci KV?** Długie prompty zmieniają wynik.
- **Czy środowisko uruchomieniowe efektywnie dzieli pracę między urządzenia?** Transfery PCIe i rozmieszczenie tensorów wpływają na każdy wygenerowany token.
- **Czy system obsługuje wymagany kontekst do końca?** Dobry wynik 4K nie rekompensuje nieudanego obciążenia 256K.

**Nowy benchmark odpowiada na te pytania dla każdego modelu.** Przy 256K Qwen3.8 wyraźnie wypada lepiej na GB10. W tej konkretnej konfiguracji pozostałe cztery modele generują szybciej na systemie dwukartowym. Większa pula pamięci zunifikowanej nadal zapewnia większy zapas pojemności, nawet gdy nie daje najwyższej zmierzonej przepustowości.

Ten sam sprzęt z dwoma GPU osiągnął też medianę 92,8 tokena na sekundę po rozgrzewce przy 256K dla Flash-Next IQ2_XS w Strata. Ten osobny wynik nie zmienia wniosku dotyczącego gęstego Qwen3.8 na GB10. Flash-Next korzysta z innej architektury mixture-of-experts, kwantyzacji, pakietu, środowiska uruchomieniowego i trybu dekodowania. Ten zestaw danych nie zawiera dopasowanego wyniku Flash-Next na GB10.

## Werdykt

**System z dwiema kartami RTX 5060 Ti generuje szybciej dla czterech z pięciu testowanych modeli przy 256K.** Kosztuje też około połowę ceny GB10 z oferty. GB10 pozostaje lepszym wyborem dla Qwen3.8 27B przy 256K, gdy liczy się zapas pamięci oraz dla obciążeń korzystających z jednej spójnej puli pamięci.

Wcześniejszy wynik dla samego Qwen sugerował proste zwycięstwo GB10. Zaktualizowany test pięciu modeli pokazuje, dlaczego taki wniosek był zbyt szeroki. Na wynik wpływają architektura modelu, wersja środowiska uruchomieniowego, rozmieszczenie tensorów i zachowanie przy różnym kontekście.

Jeśli korzystasz z GPT-OSS, Nemotron 3.5 Lightning, Qwen3.5 lub Qwen3.6, w tym benchmarku system dwukartowy generował szybciej. Dla Qwen3.8 27B przy 256K GB10 zapewniał użyteczną szybkość generowania, podczas gdy system dwukartowy niemal stanął.

**Pojemność pamięci i przepustowość to osobne kryteria zakupu.** GB10 oferuje czterokrotnie większą łączną pamięć i prostszy, współdzielony zestaw roboczy. System dwukartowy zapewnia wyższą zaobserwowaną przepustowość dla większości testowanych modeli przy znacznie niższej cenie w ofercie.

Wynik Strata pokazuje drugą zależność. Rozmieszczenie w środowisku uruchomieniowym, architektura modelu i tryb dekodowania zmieniły wynik 256K na tym samym hoście dwukartowym. Flash-Next IQ2_XS utrzymał medianę około 93 tokenów na sekundę po rozgrzewce, podczas gdy gęsty Qwen3.8 przeniósł 24 warstwy poza GPU i zwolnił do mniej niż jednego tokena na sekundę.

## Ograniczenia benchmarku

Benchmark zapisuje tagi modeli, wymagane konteksty, rzeczywistą liczbę tokenów promptu, szybkość przetwarzania promptu i generowania, wersje Ollama oraz limit generowania wynoszący 128 tokenów. Nie zapisuje rozstrzygniętych skrótów manifestów, poboru mocy CPU ani całego systemu, prędkości wentylatorów lub konfiguracji chłodzenia.

Wiersze GPT-OSS dla 256K obejmują 65 538 rzeczywistych tokenów promptu w obu systemach. Pozostałe wiersze 256K obejmują około 171 tys. rzeczywistych tokenów promptu. Traktuj te wartości jako porównanie zaobserwowanych systemów, a nie uniwersalny ranking każdej pary RTX 5060 Ti i każdej implementacji GB10.

Test Strata kontra model gęsty zapisuje dokładne liczby promptów, pięć mierzonych żądań na kontekst, wersje środowisk uruchomieniowych, rozmieszczenie urządzeń, ustawienia pamięci podręcznej i status żądań. W porównaniu jednocześnie zmieniono architekturę modelu, kwantyzację, pakiet, środowisko uruchomieniowe i tryb dekodowania. Strata ponownie wykorzystywała też prefiksy promptu powyżej 32K. Mierzone żądania generowania w obu stosach ponownie wykorzystywały niemal cały prompt.

Nie da się dokładnie odtworzyć testu na podstawie tego artykułu. Harmonogram benchmarku, układ pakietu Strata, profil ekspertów i pakiet szkiców MTP nie mają opublikowanych niezmiennych skrótów. Ostrzeżenie o niskim VRAM zwiększa też ryzyko różnic między uruchomieniami. Test izoluje host, a nie silnik wnioskowania.

Powyższe specyfikacje sprzętu pochodzą od NVIDIA. Dane o wydajności pochodzą z kontrolowanego testu benchmarkowego przeprowadzonego na potrzeby tego artykułu.

## Źródła

- [Biblioteka modeli Qwen3.8 w Ollama](https://ollama.com/library/qwen3.8)
- [Modele ISTA-DASLab Qwen3.8 Flash-Next GSQ-RCO GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF)
- [Modele orcarouter Qwen3.8 Flash-Next Uncensored GGUF](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF)
- [Biblioteka modeli Qwen3.5 w Ollama](https://ollama.com/library/qwen3.5)
- [Biblioteka modeli Qwen3.6 w Ollama](https://ollama.com/library/qwen3.6)
- [Biblioteka modeli Nemotron 3.5 Lightning w Ollama](https://ollama.com/library/nemotron-3.5-lightning)
- [Tagi modeli GPT-OSS w Ollama](https://ollama.com/library/gpt-oss/tags)
- [Czy 16 GB VRAM wystarczy do poważnej pracy z lokalnymi LLM?](/articles/is-16gb-vram-enough-local-llm/)
- [32 GB VRAM dla Qwen 27B](/articles/32gb-vram-qwen-27b-hardware-guide/)
- [Przewodnik po kontekście modeli AI i GPU](/articles/local-ai-model-gpu-context-guide/)
- [Benchmarki GPU dla Qwen3.8 27B w Vast.ai](/articles/qwen38-27b-vast-ai-gpu-benchmark/)
- [Oferta kompletnej stacji roboczej z dwiema kartami RTX 5060 Ti 16 GB](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white)
- [Oferta NVIDIA DGX Spark w amerykańskim sklepie](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/)
- [Oferta AMD Ryzen AI Halo 128 GB z Linuxem](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false)
- [Recenzja Tom's Hardware: Strix Halo kontra GB10](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4)
- [Bieżące ceny RTX 5060 Ti](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/)
