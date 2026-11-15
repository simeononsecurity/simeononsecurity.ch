---
title: "Lokalne modele Hermes w testach: jakie zestawy GPU i modeli bym wybrał"
date: 2026-10-24
lastmod: 2026-11-15
toc: true
draft: false
description: "Moje rekomendacje modeli Hermes wynikają z testów długiego kontekstu, narzędzi, strumieniowania i obrazów na systemach RTX 5060 Ti, RTX 2000E Ada, RTX 3060 Ti oraz RTX 3070."
genre: ["Sztuczna inteligencja", "Lokalna AI", "Sprzęt komputerowy"]
tags: ["Hermes Agent", "lokalne modele językowe", "testy LLM", "inferencja GPU", "RTX 3060 Ti", "RTX 3070", "RTX 2000E Ada", "RTX 5060 Ti", "kwalifikacja modelu", "wywoływanie narzędzi", "długi kontekst", "llama.cpp", "Ollama", "Qwen3.5", "Qwen3.6", "Qwen3.8"]
cover: "/img/cover/hermes-local-model-gpu-benchmarks.webp"
coverAlt: "Ilustracja kart graficznych z dwoma wentylatorami i niskoprofilowych obok tytułu Hermes Model Benchmarks na granatowym tle"
coverCaption: ""
---

Do zadań Hermesa z długim kontekstem zacząłbym od Qwen3.5 35B na dwóch kartach RTX 5060 Ti po 16 GB. Testowana trasa zachowała 239 153 tokeny wejściowe przez LiteLLM i przeszła osobne kontrole narzędzi, strumieniowania, obrazu, kolejki żądań oraz anulowania. Qwen3.6 to moja alternatywa na jednej karcie. W systemach z RTX 3060 Ti i RTX 3070 zacząłbym od Qwen3.5 2B lub 4B.

Te wybory wynikają z uruchamiania modeli na ścieżkach inferencji używanych przez agenta. Sprawdziłem zachowanie długiego wejścia, pełne cykle użycia narzędzi, odpowiedzi strumieniowane, pytania o obrazy i zwalnianie modelu. Przetestowałem też tryby i ustawienia pamięci wykorzystywane przez trasy, bo samo załadowanie modelu niewiele mówi o jego przydatności podczas długiego żądania agenta.

Hermes wymaga co najmniej 64 000 tokenów kontekstu do pracy agenta z narzędziami. Za próg kwalifikacji długiego kontekstu przyjąłem 65 536 rzeczywistych tokenów wejściowych. Liczba tokenów wejściowych jest ważniejsza niż kontekst deklarowany przez serwer. ([Dokumentacja dostawców Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md))

## Karty GPU w poszczególnych systemach

Litery systemów oznaczają poniższe zestawy sprzętu i będą używane przy omawianiu wyników.

| System | GPU używane w tym benchmarku | Mój model startowy |
|---|---|---|
| A | 2 × GeForce RTX 5060 Ti, po 16 GB | Qwen3.5 35B na obu kartach albo Qwen3.6 na jednej karcie |
| B | 1 × RTX 2000E Ada, 16GB | Qwen3.5 9B, jeśli kilkuminutowe przetwarzanie długiego wejścia pasuje do zadania |
| C | 1 × RTX 2000E Ada, 16GB | Gemma 3 4B do testowanej ścieżki długiego wejścia; Qwen3.5 0.8B bez myślenia do ograniczonych zadań przypominania |
| D | 1 × RTX 2000E Ada, 16GB | Qwen3.5 9B, Gemma 4 12B-IT lub GPT-OSS 20B do testowanych zadań z większymi modelami |
| E | 9 × GeForce RTX 3060 Ti, po 8 GB | Qwen3.5 2B lub 4B |
| F | 8 × GeForce RTX 3060 Ti, po 8 GB | Qwen3.5 2B lub 4B |
| G | 3 × GeForce RTX 3070 | Qwen3.5 2B lub 4B |

Liczba zainstalowanych kart nie oznacza, że każde żądanie używało wszystkich GPU. Testy Qwen3.5 35B i Flash Next korzystały z obu kart w systemie A. Qwen3.6 używał jednej karty. Udana powtórka testu obrazu z Qwen3.5 4B w systemie E korzystała z jednej wybranej karty z puli ośmiu, a dziewiąta karta pozostawała wyłączona z zadań AI.

Podane czasy traktuj jako wyniki łącznej konfiguracji testowanego modelu, runtime'u i systemu. Te przebiegi porównują użyteczne konfiguracje. Nie izolują architektury GPU jako przyczyny różnicy prędkości.

## Dwie karty RTX 5060 Ti czynią Qwen3.5 35B moim wyborem do długiego kontekstu

Qwen3.5 35B uzyskał w tych testach największy wynik zachowanego wejścia. Bezpośrednia seria w Ollama zachowała 248 279 tokenów wejściowych przy kontekście runtime'u 262 144 tokenów. Oddzielne strumieniowane żądanie przez bramę zachowało 239 153 tokeny wejściowe, zwróciło znacznik początkowy i zakończyło się normalnie po 31 tokenach wyjściowych w 148,12 s.

Wynik bramy ma znaczenie dla Hermesa, bo żądanie przechodziło przez brokera i LiteLLM. Osobne żądania ukończyły cykl narzędzia, rozpoznały czerwony obraz i zwróciły dwie poprawne odpowiedzi po wysłaniu ich równocześnie. Broker umieścił oba żądania w kolejce. Zamknięcie strumieniowanego żądania zwolniło brokera i wyładowało model w ciągu 60,31 s.

| Żądanie Qwen3.5 35B | Tokeny wejściowe | Tokeny wyjściowe | Czas | Wynik |
|---|---:|---:|---:|---|
| Bezpośrednia Ollama, pierwszy etap progresji | 69,429 | 31 | 38.783 s | Dokładny znacznik początkowy |
| Bezpośrednia Ollama, kontynuacja ze wspólnym prefiksem | 124,179 | 31 | 28.472 s | Dokładny znacznik początkowy |
| Bezpośrednia Ollama, kontynuacja ze wspólnym prefiksem | 182,579 | 31 | 38.974 s | Dokładny znacznik początkowy |
| Bezpośrednia Ollama, kontynuacja ze wspólnym prefiksem | 248,279 | 31 | 54.215 s | Dokładny znacznik początkowy |
| Strumieniowane żądanie brokera | 69,427 | 29 | 38.872 s | Dokładny znacznik początkowy |
| Strumieniowane żądanie LiteLLM | 239,153 | 31 | 148.12 s | Dokładny znacznik początkowy, clean unload |

Kolejne bezpośrednie żądania ponownie wykorzystywały coraz dłuższy wspólny prefiks. Ich czasy opisują kontynuację z ciepłym prefiksem. Wynik 54,215 s nie jest niezależnym, zimnym pomiarem przetwarzania nowego promptu o długości 248K.

W największym bezpośrednim etapie model raportował około 27,3 mld bajtów pamięci zajętej na obu GPU. Szczytowe użycie pamięci na kartach wyniosło 14 964 i 12 386 MiB.

Szczytowe temperatury wyniosły 62 i 63°C. Nie odnotowano błędu OOM ani Xid. W skonfigurowanym kontekście pozostało 13 865 tokenów na kontynuację. Krótka odpowiedź ze znacznikiem zużyła z tego 31 tokenów.

Wybrałbym tę trasę, gdy zachowanie dużego zestawu roboczego jest ważniejsze od najkrótszej pierwszej odpowiedzi. Kontrole narzędzi i obrazu potwierdzają przydatne zachowania agenta, a test długiego wejścia sprawdza jego zachowanie w kontekście. To odrębne zadania.

## Qwen3.6 to wariant na jednej karcie

Qwen3.6-35B-A3B UD-Q4_K_XL zachował 131 000 tokenów wejściowych na jednej karcie RTX 5060 Ti. Druga karta pozostawała bezczynna podczas testu. Daje to systemowi przydatną alternatywę, gdy nie chcemy przeznaczać obu kart na jeden model.

| Żądanie Qwen3.6 przez bramę | Tokeny wejściowe | Tokeny wyjściowe | Czas | Wynik |
|---|---:|---:|---:|---|
| początkowe długie żądanie | 66,007 |  | 167.82 s | Zachowano znacznik początkowy |
| dłuższe żądanie | 90,000 | 11 | 159.92 s | Zachowano znacznik początkowy, zero cached input |
| dłuższe żądanie | 119,999 | 11 | 250.61 s | Zachowano znacznik początkowy, zero cached input |
| blisko limitu czasu działania | 131,000 | 11 | 287.09 s | Zachowano znacznik początkowy, zero cached input |

Żądanie o długości 131 000 tokenów zbliżyło się do limitu runtime'u wynoszącego 131 072 tokeny. Agentowi zostawiłbym więcej miejsca na odpowiedź i kolejne komunikaty narzędzi. Wynik zachowania wejścia blisko limitu stanowi przydatny dowód obsługi danych, ale nie rozsądny domyślny budżet wejściowy.

Użycie narzędzia powiodło się przy wyłączonym trybie myślenia. Domyślny tryb zużył limit próby wynoszący 512 tokenów, zanim wywołał narzędzie. Udany test pilotażowy przeszedł także dla szybkich, strumieniowanych i obrazowych żądań. Początkowy test kontekstu o długości 65 845 tokenów trwał 139,57 s.

## Qwen3.8 27B wygrywa porównanie odpowiedzi dla wejścia 66K

Dla tego samego zadania ze znacznikiem o długości 66 007 tokenów w systemie A Qwen3.8 27B zwrócił odpowiedź najszybciej. Zachowałbym tę trasę dla żądań o zbliżonym rozmiarze wejścia, a Qwen3.5 35B dla większego zestawu roboczego.

| Trasa systemu A | Tokeny wejściowe | Czas | Wynik |
|---|---:|---:|---|
| Qwen3.8 27B | 66,007 | 54.64 s | Zachowano znacznik początkowy |
| Qwen3.6-35B-A3B UD-Q4_K_XL | 66,007 | 167.82 s | Zachowano znacznik początkowy |
| Qwen3.8-Flash-Next UD-IQ4_XS | 66,007 | 164.58 s | Zachowano znacznik początkowy |
| Flash Next IQ4 compatibility alias | 66,007 | 213.25 s | Znacznik zachowany |

Qwen3.8 27B potrzebował około jednej trzeciej czasu porównywalnych żądań Qwen3.6 i Flash Next. Są to obserwacje pełnych żądań w testowanych runtime'ach, a nie porównanie samego sprzętu.

Szybkie odpowiedzi, strumieniowanie i użycie narzędzi także zakończyły się powodzeniem. Tryb bez myślenia odtworzył pełną sekwencję kolorów i cykl narzędzia, a test z myśleniem zwrócił tylko część sekwencji w ramach limitu 512 tokenów.

Flash Next jest mniej atrakcyjnym wyborem domyślnym na tym systemie z powodu presji na pamięć. Pilotaż z 65 847 tokenami przeszedł w 201,41 s przy kontekście runtime'u 98 304. Dwa wcześniejsze profile z kontekstem 131 072 osiągnęły limity pamięci, zanim się uruchomiły.

Późniejsza trasa osiągnęła limit cgroup wynoszący 54 GiB. Do pracy bez nadzoru wybrałbym trasę z większym zapasem pamięci.

Trasa o etykiecie `flash-iq2` korzystała z backendu zgodności Flash Next IQ4. Jej nazwa nie wskazuje wyniku IQ2.

## RTX 2000E Ada obsługuje długie wejście, ale wybór modelu zmienia czas oczekiwania

Gemma 3 4B to moja preferowana przetestowana trasa długiego wejścia w systemie C. Dwie ścieżki zachowały ponad 84K tokenów wejściowych w około 88 s. Większe modele również przeszły przydatne kontrole zachowania, ale ich żądania trwały kilka minut.

| System | Model i ścieżka | Tokeny wejściowe | Czas | Wynik |
|---|---|---:|---:|---|
| B | Qwen3.5 9B, brama | 72,265 | 263 s | Oba znaczniki zachowane, późniejsza kontrola wznowienia kopania zaliczona |
| C | Gemma 3 4B, brama | 84,044 | 88.05 s | Zachowano znacznik początkowy |
| C | Gemma 3 4B, Aperture | 84,045 | 87.68 s | Zachowano znacznik początkowy |
| C | Gemma 4 12B-IT, brama | 67,254 | 263.07 s | Zachowano znacznik początkowy |
| C | Gemma 4 12B-IT, Aperture bez strumieniowania | 67,255 | 274.24 s | Zachowano znacznik początkowy |
| C | Gemma 4 12B-IT, Aperture ze strumieniowaniem | 67,255 | 282.16 s | Zachowano znacznik początkowy |
| C | Qwen3.5 9B, brama | 75,648 | 319.36 s | Zachowano znacznik początkowy, model zwolniony z pamięci |
| C | GPT-OSS 20B, brama | 84,099 | 315.83 s | Zachowano znacznik początkowy, model zwolniony z pamięci |
| D | Qwen3.5 9B, Aperture | 81,051 | 324.07 s | Test zachowania zaliczony na zainstalowanym artefakcie |
| D | Gemma 4 12B-IT, Aperture | 72,057 | 300.67 s | Test zachowania zaliczony na zainstalowanym artefakcie |
| D | GPT-OSS 20B, Aperture | 72,104 | 245.94 s | Test zachowania zaliczony na zainstalowanym artefakcie |

Strumieniowanie nie skróciło długiego wstępnego przetwarzania Gemma 4 w systemie C. Pierwsza treść pojawiła się po 277,49 s, później niż pełna odpowiedź bez strumieniowania, która trwała 274,24 s. Wcześniejsza próba bez strumieniowania przekroczyła limit czasu przed udaną powtórką. Wybrałbym tę trasę do zadań, w których kilkuminutowy początkowy czas przetwarzania jest akceptowalny.

Gemma 3 4B pokazuje też, dlaczego kwalifikację należy ograniczać do każdego testowanego systemu. System D nie odnalazł znacznika początkowego w dwóch próbach przypomnienia przy 65K, w tym w powtórce przy temperaturze zero z 67 252 tokenami wejściowymi. Deterministyczne żądanie zakończyło się normalnie po 62,07 s przy pełnym wykorzystaniu GPU.

Szybkie zakończenie i prawidłowa odpowiedź API nie oznaczały poprawności odpowiedzi. Używałbym udanej trasy z systemu C, a nieudaną trasę systemu D wykluczyłbym z wyboru dla Hermesa.

## Tryb myślenia decyduje, czy Qwen3.5 0.8B będzie przydatny

Po wyłączeniu myślenia Qwen3.5 0.8B stał się w systemie C przydatnym kandydatem do wąskich zadań przypominania. Mały model Q8_0 zachował 75 649 tokenów wejściowych przez bramę w 65,92 s. Wynik dotyczy testowanego artefaktu Q8_0 i trasy bez myślenia, a nie starszych konfiguracji z kontekstem 16K pokazanych dalej w tabeli.

| Żądanie Qwen3.5 0.8B w systemie C | Tokeny wejściowe | Tokeny wyjściowe | Czas | Wynik |
|---|---:|---:|---:|---|
| Domyślne myślenie, krótka diagnostyka | 9,050 | 3,391 | 66.56 s | Dokładny znacznik początkowy |
| Myślenie wyłączone, dopasowana diagnostyka | 9,055 | 21 | 7.65 s | Dokładny znacznik początkowy, no reasoning text |
| Domyślne myślenie, długa próba |  |  | Limit czasu 600 s | Brak ukończonej odpowiedzi |
| Myślenie wyłączone, natywna Ollama | 75,656 | 22 | 69.80 s | Dokładny znacznik początkowy |
| Punkt końcowy zgodny z OpenAI bez myślenia | 75,646 | 12 | 69.09 s | Dokładny znacznik początkowy |
| Broker wymusza tryb bez myślenia | 75,647 | 13 | 66.83 s | Dokładny znacznik początkowy |
| LiteLLM z systemu A do systemu C | 75,649 | 15 | 65.92 s | Dokładny znacznik początkowy |

Czas porównywalnej diagnostyki spadł z 66,56 do 7,65 s, czyli był około 8,7 raza krótszy, a wygenerowany tekst zmniejszył się z 3 391 do 21 tokenów. Dlatego jawnie ustawiałbym tryb rozumowania przy prostych zadaniach ekstrakcji i routingu. Domyślny tryb zużył większość pracy na tekst, którego zadanie nie wymagało.

Krótka próba zgodności z OpenAI nie odnalazła znacznika; powtórka przy temperaturze zero już się powiodła. Udane testy tras używały trybu bez myślenia i naturalnego zakończenia bez limitu wyjścia. Trzy inne bramy przeszły krótkie próby ze znacznikiem w 4,22, 4,37 i 3,85 s. Potwierdzają one routing, a żądanie 75 649 tokenów potwierdza zachowanie długiego wejścia przez bramę.

Przetestowałbym tę trasę do ograniczonego przypominania i ekstrakcji. Do otwartego rozumowania agenta wybrałbym większy model. Odzyskanie jednego syntetycznego znacznika jest węższym zadaniem niż planowanie, programowanie lub koordynowanie kilku narzędzi.

## Systemy RTX 3060 Ti i RTX 3070 sprzyjają Qwen3.5 2B i 4B

Qwen3.5 2B i 4B to moje praktyczne modele startowe dla kart 8 GB. Żądania tekstowe z kontekstem w systemach E, F i G przeszły z 65 579 tokenami wejściowymi i trwały od 30,343 do 93,753 s. Testowane trasy 4B przeszły też kontrole narzędzi, strumieniowania i obrazu.

Powtórka testu kontekstu obrazu 4B w systemie E zachowała oba znaczniki i kolejność kolorów na obrazie przy 65 637 tokenach wejściowych w 44,88 s. Przeszły też żądania z kolorami w kolejności normalnej i odwróconej. Powtórka użyła jednej sprawnej karty po tym, jak inna zgłosiła błąd połączenia Xid 79 i system został uruchomiony ponownie.

| System | Kontekst tekstowy Qwen3.5 2B | Kontekst tekstowy Qwen3.5 4B | Kontekst obrazu Qwen3.5 4B |
|---|---|---|---|
| E, RTX 3060 Ti pool | 65,579 tokens, 30.343 s | 65,579 tokens, 53.787 s | 65,637 tokens, 44.88 s |
| F, RTX 3060 Ti pool | 65,579 tokens, 61.282 s | 65,579 tokens, 93.753 s | 65,635 tokens, 84.749 s |
| G, RTX 3070 pool | 65,579 tokens, 76.731 s | 65,579 tokens, 90.807 s | 65,635 tokens, 87.496 s |

Każdy z tych systemów zarejestrował 29 zaliczonych kontroli. Różnice czasów między dwoma systemami RTX 3060 Ti pokazują też, dlaczego wybierałbym testowany profil systemu, zamiast szeregować karty na podstawie czasu tych żądań.

Po oknie inferencji wszystkie siedem systemów wróciło do kopania. Oddzielny test odzyskiwania po zatrzymaniu systemu B przeszedł z nowymi zaakceptowanymi udziałami. Wadliwa karta w systemie E wróciła później do kopania po restarcie i wzmocnieniu łącza PCIe, ale pozostała wykluczona z puli AI. Przywrócenie kopania pod koniec okna testowego to odrębny wynik od automatycznego przekazania po pojedynczym żądaniu inferencji.

## Załadowanie modelu nie oznacza jego kwalifikacji

Wykluczyłbym DeepSeek Coder V2 16B z testowanych wariantów Hermesa dla 65K. Próba z pamięcią podręczną f16 zachowała 50 477 tokenów wejściowych, ale test dla celu 65K osiągnął zabezpieczenie VRAM. Alternatywne pamięci Q4 i Q8 załadowały wagi na GPU, a następnie trafiły na limity pamięci hosta lub słabą przepustowość długich promptów.

| Profil cache DeepSeek Coder V2 | Kontekst runtime'u | Zaobserwowany wynik | Moja ocena |
|---|---:|---|---|
| f16 | 81,920 | odzyskiwanie 50 477 tokenów zakończone powodzeniem, zbyt duże żądanie odrzucone | Przydatny wynik dla krótszego kontekstu |
| f16 | 73,728 | Prefill dla celu 65K zatrzymał się przy użyciu 15 802 MiB GPU | Nie kwalifikuje się do 65K |
| Q4_0 | 98,304 | Długi prefill spadł do 96,72 tokena/s przed kontrolowanym zatrzymaniem | Słabe dopasowanie do tego zadania |
| Q8_0 | 77,824 | Długi prefill spadł do 120,12 tokena/s przed kontrolowanym zatrzymaniem | Słabe dopasowanie do tego zadania |
| Q4_0 / Q8_0, larger profiles | 163,840 / 98,304 | Zabezpieczenia pamięci hosta zatrzymały próby | Dopasowanie pamięci należy oceniać dla całego systemu |

Praktyczna lekcja: testuj żądanie, które zamierzasz wysłać. Zajętość GPU, krótka odpowiedź i duży skonfigurowany kontekst nie potwierdzają zachowania długiego wejścia przy użytecznym opóźnieniu.

Granite 4.2 8B i GPT-OSS 20B poprawiły wyniki po dalszych pracach nad trasą w systemie A. Trasa Granite Q6_K zachowała 66 082 tokeny wejściowe w 88,636 s, bez tokenów z pamięci podręcznej. GPT-OSS ukończył cykl narzędzia po poprawce brokera; wywołanie trwało 9,854 s, a dalsze żądanie 9,849 s. Te udane kontrole tras oddzielam od wcześniejszych niekompletnych prób.

## Pełne wyniki benchmarku

Tabela zawiera 295 kontroli dla 59 kombinacji modeli i systemów. Macierz wykazuje 273 zaliczone kontrole, jeden nieudany test przypomnienia oraz siedem wyników niekompletnych, niespójnych lub niezgodnych. Czternaście kontroli leży poza zakresem kwalifikacji 65K. Każdy wiersz pokazuje zmierzony wynik.

Moje rekomendacje dotyczą tras i zadań, które przeszły testy. Nieudany lub niekompletny wiersz nie kwalifikuje danego zachowania.

Zaliczone testy krótkiego kontekstu i embeddingów dotyczą własnych zadań. Zaliczenie kontekstu 16K lub 32K nie kwalifikuje trasy do zadania Hermesa z 65 536 tokenami wejściowymi. Nazwy modeli są tutaj etykietami tras. Etykieta `flash-iq2` używała backendu zgodności IQ4.

Wiersz kontekstu Qwen3.5 35B dla systemu A odpowiada ostatniemu etapowi serii ze wspólnym prefiksem opisanej wyżej. Czasy narzędzi zapisane ze znakiem plus pokazują osobno wywołanie i dalsze żądanie.

Wiersz współbieżności podaje czasy dwóch żądań umieszczonych w kolejce. Wiersz anulowania pokazuje czas zwolnienia po zamknięciu strumienia przez klienta. Dodatkowe serie kontekstu i porównania tras Qwen3.5 0.8B mają własne tabele powyżej.

### System A

| Etykieta trasy modelu | Test | Wynik | Tokeny wejściowe | Czas żądania |
|---|---|---|---:|---:|
| bonsai-2-27b | context | Zaliczone | 65,621 | 88.746 s |
| bonsai-2-27b | quick | Zaliczone | 57 | 6.429 s |
| bonsai-2-27b | stream | Zaliczone |  | 9.371 s |
| bonsai-2-27b | tools | Zaliczone |  | 10.478 s |
| deepseek-coder-v2:16b | context | Niezgodne | 50,477 |  |
| deepseek-coder-v2:16b | quick | Zaliczone | 77 | 43.239 s |
| flash-iq2 | context | Zaliczone | 66,007 | 213.25 s |
| flash-iq2 | quick | Zaliczone |  | 56.03 s |
| flash-iq2 | stream | Zaliczone |  | 1.35 s |
| flash-iq2 | tools | Zaliczone |  | 16.55 s |
| gemma-4-12b-it | context | Zaliczone | 65,590 | 51.225 s |
| gemma-4-12b-it | quick | Zaliczone | 21 | 5.166 s |
| gemma-4-12b-it | stream | Zaliczone |  | 4.653 s |
| gemma-4-12b-it | tools | Zaliczone |  | 18.72 s |
| gemma-4-12b-it | vision | Zaliczone | 115 | 7.222 s |
| gemma-4-12b-it | vision_context | Zaliczone | 65,685 | 56.06 s |
| gemma-4-12b-it | vision_reverse | Zaliczone | 115 | 7.467 s |
| gemma-4-e4b-it | context | Zaliczone | 65,590 | 21.889 s |
| gemma-4-e4b-it | quick | Zaliczone | 21 | 17.919 s |
| gemma-4-e4b-it | stream | Zaliczone |  | 4.25 s |
| gemma-4-e4b-it | tools | Zaliczone |  | 8.734 s |
| gpt-oss-20b | context | Zaliczone | 65,637 | 159.155 s |
| gpt-oss-20b | quick | Zaliczone | 73 | 10.548 s |
| gpt-oss-20b | stream | Zaliczone |  | 20.594 s |
| gpt-oss-20b | tools | Zaliczone |  | 9.854 + 9.849 s |
| granite-4.2-3b | context | Zaliczone | 65,589 | 70.968 s |
| granite-4.2-3b | quick | Zaliczone | 20 | 4.009 s |
| granite-4.2-3b | stream | Zaliczone |  | 5.365 s |
| granite-4.2-3b | tools | Zaliczone |  | 6.086 s |
| granite-4.2-8b | context | Zaliczone | 66,082 | 88.636 s |
| granite-4.2-8b | quick | Zaliczone | 20 | 5.857 s |
| granite-4.2-8b | stream | Zaliczone |  | 11.826 s |
| granite-4.2-8b | tools | Zaliczone |  | 11.852 s |
| qwen27b | context | Zaliczone | 66,007 | 54.64 s |
| qwen27b | quick | Zaliczone | 57 | 31.5 s |
| qwen27b | stream | Zaliczone |  | 0.92 s |
| qwen27b | tools | Zaliczone |  | 4.25 s |
| qwen3-embedding-0.6b | context | Zaliczone | 32,767 | 7.736 s |
| qwen3-embedding-0.6b | quick | Zaliczone | 14 | 2.125 s |
| qwen3.5-0.8b | context | Zaliczone | 16,429 | 10.5 s |
| qwen3.5-0.8b | quick | Zaliczone | 17 | 14.316 s |
| qwen3.5-0.8b | stream | Zaliczone |  | 2.125 s |
| qwen3.5-0.8b | tools | Zaliczone |  | 4.416 s |
| qwen3.5-2b | context | Zaliczone | 65,581 | 11.175 s |
| qwen3.5-2b | quick | Zaliczone | 17 | 4.519 s |
| qwen3.5-2b | stream | Zaliczone |  | 3.736 s |
| qwen3.5-2b | tools | Zaliczone |  | 5.046 s |
| qwen3.5-4b | context | Zaliczone | 65,579 | 36.451 s |
| qwen3.5-4b | quick | Zaliczone | 15 | 19.935 s |
| qwen3.5-4b | stream | Zaliczone |  | 17.496 s |
| qwen3.5-4b | tools | Zaliczone |  | 7.308 s |
| qwen3.5-4b | vision | Zaliczone | 70 | 7.848 s |
| qwen3.5-4b | vision_context | Zaliczone | 65,635 | 28.24 s |
| qwen3.5-4b | vision_reverse | Zaliczone | 70 | 4.386 s |
| qwen3.5-9b | context | Zaliczone | 65,581 | 34.139 s |
| qwen3.5-9b | quick | Zaliczone | 17 | 3.88 s |
| qwen3.5-9b | stream | Zaliczone |  | 3.378 s |
| qwen3.5-9b | tools | Zaliczone |  | 10.204 s |
| qwen3.5-9b | vision | Zaliczone | 72 | 4.441 s |
| qwen3.5-9b | vision_context | Zaliczone | 65,637 | 33.745 s |
| qwen3.5-9b | vision_reverse | Zaliczone | 72 | 3.97 s |
| qwen3.5:35b-a3b-q4_K_M | cancellation | Zaliczone |  | 60.31 s |
| qwen3.5:35b-a3b-q4_K_M | concurrency | Zaliczone |  | 26.23 / 25.33 s |
| qwen3.5:35b-a3b-q4_K_M | context | Zaliczone | 248,279 | 54.215 s |
| qwen3.5:35b-a3b-q4_K_M | gateway | Zaliczone | 239,153 | 148.12 s |
| qwen3.5:35b-a3b-q4_K_M | quick | Zaliczone | 79 | 10.08 s |
| qwen3.5:35b-a3b-q4_K_M | stream | Zaliczone | 69,429 | 38.783 s |
| qwen3.5:35b-a3b-q4_K_M | tools | Zaliczone |  | 15.22 + 14.83 s |
| qwen3.5:35b-a3b-q4_K_M | vision | Zaliczone |  | 18.39 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | context | Zaliczone | 65,845 | 139.57 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | quick | Zaliczone | 15 | 3.97 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | stream | Zaliczone |  | 0.45 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | tools | Zaliczone | 293 | 5.48 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | vision | Zaliczone | 38 | 0.59 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | context | Zaliczone | 65,847 | 201.41 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | quick | Zaliczone | 17 | 54.62 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | stream | Zaliczone |  | 1.2 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | tools | Zaliczone |  | 22.18 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | vision | Zaliczone |  | 3.86 s |

### System B

| Etykieta trasy modelu | Test | Wynik | Tokeny wejściowe | Czas żądania |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Zaliczone | 65,590 | 299.163 s |
| gemma-4-12b-it | quick | Zaliczone | 21 | 15.261 s |
| gemma-4-12b-it | stream | Zaliczone |  | 148.792 s |
| gemma-4-12b-it | tools | Zaliczone |  | 34.124 s |
| gemma-4-12b-it | vision | Zaliczone | 120 | 61.455 s |
| gemma-4-12b-it | vision_context | Zaliczone | 65,690 | 295.581 s |
| gemma-4-12b-it | vision_reverse | Zaliczone | 120 | 32.511 s |
| gemma3-4b | context | Zaliczone | 65,584 | 67.382 s |
| gemma3-4b | quick | Zaliczone | 15 | 6.329 s |
| gemma3-4b | stream | Zaliczone |  | 24.138 s |
| gemma3-4b | vision | Zaliczone | 306 | 7.018 s |
| gemma3-4b | vision_context | Zaliczone | 65,876 | 70.912 s |
| gemma3-4b | vision_reverse | Zaliczone | 306 | 5.762 s |
| gpt-oss-20b | context | Zaliczone | 65,637 | 206.767 s |
| gpt-oss-20b | quick | Zaliczone | 72 | 16.583 s |
| gpt-oss-20b | stream | Zaliczone |  | 32.075 s |
| gpt-oss-20b | tools | Zaliczone |  | 28.102 s |
| nomic-embed-text | context | Niekompletne | 2,048 |  |
| nomic-embed-text | quick | Zaliczone |  | 7.117 s |
| qwen3-14b | context | Niekompletne |  | 1800.09 s |
| qwen3-14b | quick | Zaliczone | 15 | 37.199 s |
| qwen3-14b | stream | Zaliczone |  | 35.471 s |
| qwen3-14b | tools | Zaliczone |  | 87.554 s |
| qwen3-8b | context | Poza zakresem 65K, wykluczone |  |  |
| qwen3-8b | quick | Poza zakresem 65K, zaliczone | 15 | 21.059 s |
| qwen3-8b | stream | Poza zakresem 65K, wykluczone |  |  |
| qwen3-8b | tools | Poza zakresem 65K, wykluczone |  |  |
| qwen3.5-9b | context | Zaliczone | 65,579 | 282.796 s |
| qwen3.5-9b | litellm_long_route | Zaliczone | 72,265 | 263 s |
| qwen3.5-9b | post_external_stop_mining | Zaliczone |  |  |
| qwen3.5-9b | quick | Zaliczone | 15 | 25.881 s |
| qwen3.5-9b | stream | Zaliczone |  | 143.44 s |
| qwen3.5-9b | tools | Zaliczone |  | 31.812 s |
| qwen3.5-9b | vision | Zaliczone | 75 | 32.015 s |
| qwen3.5-9b | vision_context | Zaliczone | 65,640 | 396.288 s |
| qwen3.5-9b | vision_reverse | Zaliczone | 75 | 28.626 s |

### System C

| Etykieta trasy modelu | Test | Wynik | Tokeny wejściowe | Czas żądania |
|---|---|---|---:|---:|
| gemma-4-12b-it | aperture_context | Zaliczone | 67,255 | 274.24 s |
| gemma-4-12b-it | aperture_short | Zaliczone | 35 | 39.32 s |
| gemma-4-12b-it | aperture_stream_context | Zaliczone | 67,255 | 282.16 s |
| gemma-4-12b-it | context | Zaliczone | 65,670 | 313.661 s |
| gemma-4-12b-it | gateway_context | Zaliczone | 67,254 | 263.07 s |
| gemma-4-12b-it | gateway_short | Zaliczone | 27 | 20.98 s |
| gemma-4-12b-it | quick | Zaliczone | 21 | 16.447 s |
| gemma-4-12b-it | stream | Zaliczone |  | 15.175 s |
| gemma-4-12b-it | tools | Zaliczone |  | 37.821 s |
| gemma-4-12b-it | vision | Zaliczone | 120 | 58.52 s |
| gemma-4-12b-it | vision_context | Zaliczone | 65,690 | 308.759 s |
| gemma-4-12b-it | vision_reverse | Zaliczone | 120 | 31.25 s |
| gemma3-4b | aperture_context | Zaliczone | 84,045 | 87.68 s |
| gemma3-4b | aperture_after_system_d_route_change | Zaliczone | 24 | 5.42 s |
| gemma3-4b | aperture_short | Zaliczone | 22 | 5.45 s |
| gemma3-4b | aperture_stream | Zaliczone |  | 3.72 s |
| gemma3-4b | context | Zaliczone | 65,664 | 67.543 s |
| gemma3-4b | gateway_context | Zaliczone | 84,044 | 88.05 s |
| gemma3-4b | gateway_short_via_system_a | Zaliczone |  | 3.16 s |
| gemma3-4b | gateway_short_via_system_e | Zaliczone |  |  |
| gemma3-4b | gateway_short_via_system_f | Zaliczone |  | 4.15 s |
| gemma3-4b | gateway_short_via_system_g | Zaliczone |  | 6.06 s |
| gemma3-4b | quick | Zaliczone | 15 | 5.163 s |
| gemma3-4b | stream | Zaliczone |  | 24.691 s |
| gemma3-4b | vision | Zaliczone | 306 | 7.318 s |
| gemma3-4b | vision_context | Zaliczone | 65,876 | 72.476 s |
| gemma3-4b | vision_reverse | Zaliczone | 306 | 5.831 s |
| gpt-oss-20b | context | Zaliczone | 65,716 | 216.594 s |
| gpt-oss-20b | gateway_context | Zaliczone | 84,099 | 315.83 s |
| gpt-oss-20b | gateway_short | Niespójne |  |  |
| gpt-oss-20b | quick | Zaliczone | 72 | 21.603 s |
| gpt-oss-20b | stream | Zaliczone |  | 31.957 s |
| gpt-oss-20b | tools | Zaliczone |  | 26.096 s |
| nomic-embed-text | context | Poza zakresem 65K, niekompletne | 2,048 |  |
| nomic-embed-text | quick | Poza zakresem 65K, zaliczone |  | 4.178 s |
| qwen3-14b | context | Poza zakresem 65K, niekompletne |  | 1800.06 s |
| qwen3-14b | quick | Poza zakresem 65K, zaliczone | 15 | 35.809 s |
| qwen3-14b | stream | Poza zakresem 65K, zaliczone |  | 35.43 s |
| qwen3-14b | tools | Poza zakresem 65K, zaliczone |  | 87.723 s |
| qwen3-8b | context | Poza zakresem 65K, wykluczone |  |  |
| qwen3-8b | quick | Poza zakresem 65K, zaliczone | 15 | 21.293 s |
| qwen3-8b | stream | Poza zakresem 65K, niekompletne |  | 900.01 s |
| qwen3-8b | tools | Poza zakresem 65K, wykluczone |  |  |
| qwen3.5-9b | context | Zaliczone | 65,662 | 287.984 s |
| qwen3.5-9b | gateway_context | Zaliczone | 75,648 | 319.36 s |
| qwen3.5-9b | gateway_short | Zaliczone | 21 | 72.14 s |
| qwen3.5-9b | quick | Zaliczone | 15 | 24.635 s |
| qwen3.5-9b | stream | Zaliczone |  | 143.157 s |
| qwen3.5-9b | tools | Zaliczone |  | 30.395 s |
| qwen3.5-9b | vision | Zaliczone | 75 | 27.756 s |
| qwen3.5-9b | vision_context | Zaliczone | 65,640 | 398.797 s |
| qwen3.5-9b | vision_reverse | Zaliczone | 75 | 28.645 s |

### System D

| Etykieta trasy modelu | Test | Wynik | Tokeny wejściowe | Czas żądania |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Zaliczone | 65,590 | 275.395 s |
| gemma-4-12b-it | exact_digest_aperture_65k | Zaliczone | 72,057 | 300.67 s |
| gemma-4-12b-it | exact_digest_broker_short | Zaliczone | 34 | 30.74 s |
| gemma-4-12b-it | quick | Zaliczone | 21 | 15.05 s |
| gemma-4-12b-it | stream | Zaliczone |  | 14.722 s |
| gemma-4-12b-it | tools | Zaliczone |  | 33.869 s |
| gemma-4-12b-it | vision | Zaliczone | 120 | 56.315 s |
| gemma-4-12b-it | vision_context | Zaliczone | 65,690 | 282.174 s |
| gemma-4-12b-it | vision_reverse | Zaliczone | 120 | 29.978 s |
| gemma3-4b | context | Zaliczone | 65,584 | 63.564 s |
| gemma3-4b | exact_digest_65k_recall | Nieudane | 67,252 | 62.07 s |
| gemma3-4b | quick | Zaliczone | 15 | 5.151 s |
| gemma3-4b | stream | Zaliczone |  | 22.552 s |
| gemma3-4b | vision | Zaliczone | 306 | 8.276 s |
| gemma3-4b | vision_context | Zaliczone | 65,876 | 67.575 s |
| gemma3-4b | vision_reverse | Zaliczone | 306 | 5.651 s |
| gpt-oss-20b | context | Zaliczone | 65,637 | 189.07 s |
| gpt-oss-20b | exact_digest_aperture_65k | Zaliczone | 72,104 | 245.94 s |
| gpt-oss-20b | exact_digest_broker_short | Zaliczone | 84 | 15.96 s |
| gpt-oss-20b | quick | Zaliczone | 72 | 15.431 s |
| gpt-oss-20b | stream | Zaliczone |  | 31.052 s |
| gpt-oss-20b | tools | Zaliczone |  | 23.65 s |
| nomic-embed-text | context | Niekompletne | 2,048 |  |
| nomic-embed-text | quick | Zaliczone |  | 2.798 s |
| qwen3-14b | context | Niekompletne | 40,939 | 872.209 s |
| qwen3-14b | quick | Zaliczone | 15 | 36.021 s |
| qwen3-14b | stream | Zaliczone |  | 33.491 s |
| qwen3-14b | tools | Zaliczone |  | 82.471 s |
| qwen3-8b | context | Niekompletne |  | 1800.07 s |
| qwen3-8b | quick | Zaliczone | 15 | 19.283 s |
| qwen3-8b | stream | Zaliczone |  | 19.401 s |
| qwen3-8b | tools | Zaliczone |  | 65.054 s |
| qwen3.5-9b | context | Zaliczone | 65,579 | 258.048 s |
| qwen3.5-9b | exact_digest_aperture_65k | Zaliczone | 81,051 | 324.07 s |
| qwen3.5-9b | exact_digest_broker_short | Zaliczone | 29 | 94.48 s |
| qwen3.5-9b | quick | Zaliczone | 15 | 27.16 s |
| qwen3.5-9b | stream | Zaliczone |  | 28.62 s |
| qwen3.5-9b | tools | Zaliczone |  | 28.129 s |
| qwen3.5-9b | vision | Zaliczone | 75 | 25.047 s |
| qwen3.5-9b | vision_context | Zaliczone | 65,640 | 369.477 s |
| qwen3.5-9b | vision_reverse | Zaliczone | 75 | 27.602 s |

### System E

| Etykieta trasy modelu | Test | Wynik | Tokeny wejściowe | Czas żądania |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Zaliczone | 65,590 | 49.086 s |
| gemma-4-e4b-it | quick | Zaliczone | 21 | 23.911 s |
| gemma-4-e4b-it | stream | Zaliczone |  | 28.136 s |
| gemma-4-e4b-it | tools | Zaliczone |  | 56.756 s |
| granite-4.0-h-tiny | context | Zaliczone | 65,566 |  |
| granite-4.0-h-tiny | quick | Zaliczone | 35 | 10.408 s |
| granite-4.0-h-tiny | stream | Zaliczone |  | 27.798 s |
| granite-4.0-h-tiny | tools | Zaliczone |  | 43.304 s |
| granite-4.2-3b | context | Zaliczone | 65,589 | 1014.03 s |
| granite-4.2-3b | quick | Zaliczone | 20 | 14.569 s |
| granite-4.2-3b | stream | Zaliczone |  | 6.948 s |
| granite-4.2-3b | tools | Zaliczone |  | 56.376 s |
| qwen3-embedding-0.6b | context | Zaliczone | 32,767 | 20.387 s |
| qwen3-embedding-0.6b | quick | Zaliczone | 14 | 9.592 s |
| qwen3.5-0.8b | context | Zaliczone | 16,429 | 9.128 s |
| qwen3.5-0.8b | quick | Zaliczone | 17 | 452.417 s |
| qwen3.5-0.8b | stream | Zaliczone |  | 11.163 s |
| qwen3.5-0.8b | tools | Zaliczone |  | 39.214 s |
| qwen3.5-2b | context | Zaliczone | 65,579 | 30.343 s |
| qwen3.5-2b | quick | Zaliczone | 15 | 12.509 s |
| qwen3.5-2b | stream | Zaliczone |  | 26.165 s |
| qwen3.5-2b | tools | Zaliczone |  | 42.056 s |
| qwen3.5-4b | context | Zaliczone | 65,579 | 53.787 s |
| qwen3.5-4b | quick | Zaliczone | 15 | 26.736 s |
| qwen3.5-4b | stream | Zaliczone |  | 26.02 s |
| qwen3.5-4b | tools | Zaliczone |  | 57.293 s |
| qwen3.5-4b | vision | Zaliczone | 72 | 10.09 s |
| qwen3.5-4b | vision_context | Zaliczone | 65,637 | 44.88 s |
| qwen3.5-4b | vision_reverse | Zaliczone | 72 | 9.96 s |

### System F

| Etykieta trasy modelu | Test | Wynik | Tokeny wejściowe | Czas żądania |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Zaliczone | 65,590 | 98.443 s |
| gemma-4-e4b-it | quick | Zaliczone | 21 | 27.51 s |
| gemma-4-e4b-it | stream | Zaliczone |  | 28.042 s |
| gemma-4-e4b-it | tools | Zaliczone |  | 73.891 s |
| granite-4.0-h-tiny | context | Zaliczone | 65,599 | 19.692 s |
| granite-4.0-h-tiny | quick | Zaliczone | 35 | 43.818 s |
| granite-4.0-h-tiny | stream | Zaliczone |  | 27.296 s |
| granite-4.0-h-tiny | tools | Zaliczone |  | 75.377 s |
| granite-4.2-3b | context | Zaliczone | 65,589 | 145.179 s |
| granite-4.2-3b | quick | Zaliczone | 20 | 15.703 s |
| granite-4.2-3b | stream | Zaliczone |  | 35.482 s |
| granite-4.2-3b | tools | Zaliczone |  | 52.539 s |
| qwen3-embedding-0.6b | context | Zaliczone | 32,767 | 20.656 s |
| qwen3-embedding-0.6b | quick | Zaliczone | 14 | 8.122 s |
| qwen3.5-0.8b | context | Zaliczone | 16,429 | 13.326 s |
| qwen3.5-0.8b | quick | Zaliczone | 17 | 445.22 s |
| qwen3.5-0.8b | stream | Zaliczone |  | 13.266 s |
| qwen3.5-0.8b | tools | Zaliczone |  | 40.825 s |
| qwen3.5-2b | context | Zaliczone | 65,579 | 61.282 s |
| qwen3.5-2b | quick | Zaliczone | 15 | 16.738 s |
| qwen3.5-2b | stream | Zaliczone |  | 25.29 s |
| qwen3.5-2b | tools | Zaliczone |  | 47.444 s |
| qwen3.5-4b | context | Zaliczone | 65,579 | 93.753 s |
| qwen3.5-4b | quick | Zaliczone | 15 | 33.039 s |
| qwen3.5-4b | stream | Zaliczone |  | 25.658 s |
| qwen3.5-4b | tools | Zaliczone |  | 71.731 s |
| qwen3.5-4b | vision | Zaliczone | 70 | 43.053 s |
| qwen3.5-4b | vision_context | Zaliczone | 65,635 | 84.749 s |
| qwen3.5-4b | vision_reverse | Zaliczone | 70 | 27.518 s |

### System G

| Etykieta trasy modelu | Test | Wynik | Tokeny wejściowe | Czas żądania |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Zaliczone | 65,590 | 92.696 s |
| gemma-4-e4b-it | quick | Zaliczone | 21 | 38.329 s |
| gemma-4-e4b-it | stream | Zaliczone |  | 43.549 s |
| gemma-4-e4b-it | tools | Zaliczone |  | 66.616 s |
| granite-4.0-h-tiny | context | Zaliczone | 65,599 | 69.777 s |
| granite-4.0-h-tiny | quick | Zaliczone | 35 | 33.17 s |
| granite-4.0-h-tiny | stream | Zaliczone |  | 31.751 s |
| granite-4.0-h-tiny | tools | Zaliczone |  | 63.338 s |
| granite-4.2-3b | context | Zaliczone | 65,589 | 100.849 s |
| granite-4.2-3b | quick | Zaliczone | 20 | 23.355 s |
| granite-4.2-3b | stream | Zaliczone |  | 28.75 s |
| granite-4.2-3b | tools | Zaliczone |  | 44.226 s |
| qwen3-embedding-0.6b | context | Zaliczone | 32,767 | 23.055 s |
| qwen3-embedding-0.6b | quick | Zaliczone | 14 | 8.924 s |
| qwen3.5-0.8b | context | Zaliczone | 16,429 | 16.74 s |
| qwen3.5-0.8b | quick | Zaliczone | 17 | 504.813 s |
| qwen3.5-0.8b | stream | Zaliczone |  | 15.095 s |
| qwen3.5-0.8b | tools | Zaliczone |  | 36.672 s |
| qwen3.5-2b | context | Zaliczone | 65,579 | 76.731 s |
| qwen3.5-2b | quick | Zaliczone | 15 | 20.949 s |
| qwen3.5-2b | stream | Zaliczone |  | 25.194 s |
| qwen3.5-2b | tools | Zaliczone |  | 37.552 s |
| qwen3.5-4b | context | Zaliczone | 65,579 | 90.807 s |
| qwen3.5-4b | quick | Zaliczone | 15 | 41.84 s |
| qwen3.5-4b | stream | Zaliczone |  | 40.812 s |
| qwen3.5-4b | tools | Zaliczone |  | 54.999 s |
| qwen3.5-4b | vision | Zaliczone | 70 | 29.619 s |
| qwen3.5-4b | vision_context | Zaliczone | 65,635 | 87.496 s |
| qwen3.5-4b | vision_reverse | Zaliczone | 70 | 26.283 s |

## Jak sprawdzałem przydatność Hermesa

Użyłem syntetycznego znacznika blisko początku długiego promptu i po tekście wypełniającym poprosiłem o jego zwrot. Odpowiedź musiała zawierać oczekiwaną wartość. Rozmiar żądania określały tokeny wejściowe raportowane przez serwer. Model, który po dużym promptcie odpowiadał poprawnie na inne pytania, nadal oblewał test, jeśli pomylił znacznik początkowy.

Seria Qwen3.5 35B używała numerowanych rekordów wypełniających, temperatury 0 i rosnącej liczby rekordów: 3 800, 6 800, 10 000 i 13 600. Etapy zwróciły 69 429, 124 179, 182 579 i 248 279 tokenów promptu. Model pozostawał załadowany między etapami, co pozwoliło ponownie wykorzystać prefiks. Oddzielne testy Qwen3.6 blisko limitu wykazały zero tokenów z pamięci podręcznej.

Długi prompt dla 0.8B powtarzał `river stone lantern orchard circuit velvet compass marble` 8 400 razy między początkowym kluczem odpowiedzi a końcowym pytaniem o przypomnienie. Natywna próba używała `think:false`, `num_ctx:131072`, `stream:false` i `keep_alive:0`. Trasa zgodna z OpenAI używała `reasoning_effort:"none"`. Broker wymuszał tryb bez myślenia, więc klienci bramy nie musieli nadpisywać tej opcji.

### Kontrole narzędzi, obrazu i zwalniania zasobów

Testy narzędzi sprawdzały żądanie oraz odpowiedź po otrzymaniu wyniku narzędzia. W prostym teście użyłem `add_numbers(7, 11)` i oczekiwałem wyniku 18. Test Qwen3.5 35B używał `lookup_square` i oczekiwał 49. GPT-OSS wykonywał zapytanie o stan magazynu i musiał uwzględnić zwrócony wynik.

Testy obrazu używały pytań o czerwony i niebieski obraz, odwróconej kolejności oraz długich promptów z kolorami i znacznikami początkowym i końcowym. Test Qwen3.5 35B użył czerwonego PNG 256 × 256. Przed powodzeniem żądania broker wymagał poprawki konwersji zawartości obrazu. Długi test obrazu 4B w systemie E wymagał zachowania obu znaczników oraz kolejności kolorów wejściowych.

Podczas długich testów sprawdzałem pamięć GPU, rezydencję modelu, temperatury, presję na pamięć hosta, zdarzenia OOM i błędy GPU. Zabezpieczenie Qwen3.5 35B sprawdzało też zwolnienie modelu po kontrolowanym przerwaniu. Późniejsze testy anulowania przez klienta i żądań w kolejce obejmowały trasę przez brokera. Dwa żądania w kolejce potwierdzają ich obsługę przy testowanym obciążeniu, a nie istnienie dwóch niezależnych, równoczesnych backendów GPU.

### Interpretacja wyników wydajności

Czasy żądań obejmują wstępne przetwarzanie długiego wejścia i zwróconą odpowiedź. Nie oznaczają liczby generowanych tokenów na sekundę. Przy strumieniowaniu liczy się czas do pierwszej treści, a serie z pamięcią podręczną prefiksu należy interpretować osobno.

Udane testy większych modeli w systemach A i C korzystały z dedykowanych okien inferencji, podczas których kopanie było wyłączone. Po żądaniu modele zostały wyładowane. Kopanie przywrócono na wszystkich siedmiu systemach pod koniec okna testowego. Wyniki opisują usługę modelu w czasie inferencji, nie jednoczesne kopanie i inferencję.

## Profile backendów użyte w testach

Wybierz profil odpowiadający zadaniu, które chcesz odtworzyć. Kwantyzacja, kontekst runtime'u, rodzaj pamięci podręcznej, tryb rozumowania i rozmieszczenie GPU wpływają na wynik.

| System i model | Testowany profil backendu |
|---|---|
| A, Qwen3.5 35B-A3B Q4_K_M | Ollama 0.34.2, pamięć KV f16, dwie karty RTX 5060 Ti po 16 GB, 64 GiB pamięci hosta i kontekst runtime 262 144 dla dużej progresji. Żądania natywne używały `think:false`, temperatury 0, strumieniowania i pięciominutowego keep-alive między etapami. Żądania bramy korzystały z brokera i LiteLLM. Bez limitu wyjścia żądania. |
| A, Qwen3.8 27B | llama.cpp na żądanie przez broker i LiteLLM, kontekst runtime 262 144, jedno miejsce inferencji, pamięć podręczna Q4 K/V i obie karty RTX 5060 Ti. Żądanie 66 007 tokenów nie miało limitu wyjścia. |
| A, Qwen3.6-35B-A3B UD-Q4_K_XL | Strata 0.1.48, kontekst 131 072, pamięć KV INT8, jedna wybrana GPU, limit pamięci grupy procesów 55 GiB, limit runtime 30 minut, leniwe ładowanie i wyładowanie po 60 sekundach bezczynności. Długa odpowiedź w pilotażu: 217 tokenów wyjściowych. Odpowiedź bramy blisko limitu: 11 tokenów wyjściowych, bez limitu wyjścia żądania. |
| A, Qwen3.8-Flash-Next UD-IQ4_XS | Strata 0.1.48, kontekst 98 304, pamięć KV Q4, rezydentna pamięć ekspertów 8 GiB i obie karty RTX 5060 Ti. Limit pamięci pilotażu: 52 GiB, późniejszej trasy: 54 GiB. Długa odpowiedź pilotażu: 10 tokenów wyjściowych. Wcześniejsze kombinacje większego kontekstu i pamięci podręcznej zatrzymały się na limitach pamięci. |
| A, Granite 4.2 8B | Wagi GGUF Q6_K, wspólny proces roboczy llama.cpp, kontekst 131 072, pamięć Q4_0 K/V, `--n-predict -1`. Długie żądanie używało temperatury 0, strumieniowania i nie miało limitu wyjścia. |
| A, DeepSeek Coder V2 16B | Wagi GGUF Q4_0, Ollama 0.34.2, dwie karty RTX 5060 Ti i 64 GiB pamięci hosta. Osobne próby pamięci f16, Q4_0 i Q8_0 używały kontekstów runtime pokazanych w tabeli. Bez limitu wyjścia żądania. |
| B, C, D, audytowana usługa Ollama | Ollama 0.34.2, kontekst 131 072, równoległość 1, jeden załadowany model, kolejka 128, keep-alive 0, Flash Attention, pamięć KV Q4_0. |
| B, test pilotażowy bramy Qwen3.5 9B | Limit czasu trasy LiteLLM: 1 800 sekund, zero ponowień, bez limitu kontekstu ani tokenów wyjściowych. Oba znaczniki zachowano przy 72 265 tokenach wejściowych. Osobna kontrola wznowienia kopania zaliczona. |
| C, Qwen3.5 0.8B | Wagi Q8_0 na jednej RTX 2000E Ada z profilem mocy 30 W. Kontekst runtime 131 072. Natywne `think:false`, zgodne z OpenAI `reasoning_effort:"none"`, bez limitu wyjścia. Alias brokera przypiął kontekst runtime i wymusił tryb bez myślenia. |
| C, Gemma 4 12B-IT | Profil Ollama na jednej GPU, kontekst runtime 131 072, strumieniowane i niestrumieniowane żądania Aperture bez limitu wyjścia. Bezpośredni przebieg Aperture osiągnął 75°C i 30,64 W przy skonfigurowanym profilu 30 W, a następnie wyładował model. |
| D, Qwen3.5 9B, Gemma 4 12B-IT, GPT-OSS 20B | Dokładne zainstalowane artefakty przetestowane przez Aperture, kontekst runtime 131 072, pełna rezydencja na jednej GPU i naturalne zakończenie bez limitu wyjścia żądania. |
| E, F, G, procesy obsługi czatu llama.cpp | Build 11669, 99 warstw GPU, równoległość 1, Flash Attention, pamięć Q4_0 K/V, `--n-predict -1`. Kontekst runtime różnił się w zależności od rodziny modelu. |

Zapisane profile usług opisują własne konfiguracje runtime'u. Oddzielnie testowany profil Qwen3.5 35B z pamięcią f16 w systemie A nie dziedziczy ustawień cache Q4_0 z mniejszych systemów Ollama.

### Odciski modeli w nowych testach zachowania wejścia

Te identyfikatory modeli odróżniają testowane artefakty od innych pobrań lub aliasów o podobnych nazwach.

| Artefakt | Kwantyzacja | Zapisany digest lub SHA-256 pliku |
|---|---|---|
| Qwen3.5 35B-A3B Ollama tag | Q4_K_M | `72aac7c28be8ff9b81c2a270eb489c88e6d822a76ec0cb7bf34d965768848567` |
| Qwen3.5 0.8B base Ollama tag | Q8_0 | `de63045f29755d4721c09d54c9b45c2dadb644f4fd7d604d4cac90d96049971c` |
| Granite 4.2 8B GGUF file | Q6_K | `5ad3d67f6fe09a448031029bead7f6a088697ca2787c0c5640bf964c59df1a21` |

Digesty manifestu Ollama i sumy SHA-256 plików wag identyfikują różne obiekty. Dopasuj identyfikator do rodzaju artefaktu w tabeli.

## Moje rekomendacje dla Hermesa

Główną trasą wysokiego kontekstu uczyniłbym Qwen3.5 35B na systemie z dwiema kartami RTX 5060 Ti. Wynik zachowania 239 153 tokenów przez bramę, osobne zaliczone testy narzędzia i obrazu oraz potwierdzone zwalnianie żądania przemawiają za nim mocniej niż za modelem reklamującym duże okno kontekstu. Qwen3.8 27B zachowałbym do szybszych odpowiedzi przy 66K, a Qwen3.6 na wypadek, gdy ważna jest praca na jednej karcie.

W systemach RTX 2000E Ada wybrałbym zweryfikowaną trasę Gemma 3 4B z systemu C do zadań długiego wejścia i odpowiedzi. Trasę Qwen3.5 0.8B bez myślenia przetestowałbym przy wąskich zadaniach przypomnienia i ekstrakcji. Większe trasy Gemma, Qwen i GPT-OSS pasują do zadań, w których akceptujemy pierwszą odpowiedź po czterech lub pięciu minutach. Wykluczyłbym nieudaną trasę Gemma 3 z systemu D.

Na kartach RTX 3060 Ti i RTX 3070 z 8 GB zacząłbym od Qwen3.5 2B lub 4B. Wyniki tekstowe 65K i testy obrazu 4B uzasadniają użyteczną konfigurację początkową bez angażowania dwóch kart 16 GB do każdego żądania. Presja pamięci Flash Next oraz niepełne zachowanie DeepSeek Coder V2 przy 65K czynią je gorszymi ustawieniami domyślnymi w testowanych profilach.

Testy wspierają wybór tych modeli i systemów do konkretnych zadań. Zachowanie wejścia, poprawny cykl narzędzia, rozpoznawanie obrazu i prawidłowe zwalnianie zasobów odpowiadają na różne aspekty przydatności Hermesa. Niezawodna konfiguracja musi obsługiwać zachowania używane przez agenta i pozostawiać dość kontekstu na odpowiedź oraz ruch narzędzi.

## Źródła i powiązane materiały

- [Konfiguracja dostawcy i wymagania kontekstu Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md)
- [Specyfikacja NVIDIA GeForce RTX 3060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3060-3060ti/)
- [Specyfikacja NVIDIA GeForce RTX 5060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/)
- [Omówienie Hermes Agent](/hermes-local-ai-broker-course/01-hermes-agent-overview/)
- [Wybór lokalnego backendu modelu](/hermes-local-ai-broker-course/02-choose-a-backend/)
