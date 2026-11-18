---
title: "Hindsight hostowany samodzielnie: lokalna pamięć agentów i prywatne trasowanie modeli"
date: 2026-11-08
lastmod: 2026-11-12
toc: true
draft: false
description: "Studium przypadku samodzielnie hostowanego Hindsight, zaobserwowanych lokalnych tras Qwen i pracy GPU przypisanej do żądań, bez subskrypcji hostowanego wnioskowania na sprawdzonych ścieżkach."
genre: ["Lokalna AI", "Samodzielnie hostowana AI", "Agenci AI", "Infrastruktura AI", "Prywatność"]
tags: ["Hindsight", "Hindsight hostowany samodzielnie", "pamięć agentów", "lokalna AI", "lokalny LLM", "Qwen3.5", "LiteLLM", "prywatna sieć VPN", "brama modeli", "embeddingi", "reranking", "planowanie GPU", "prywatne wnioskowanie", "Docker", "banki pamięci", "strony wiedzy", "lokalne trasowanie modeli"]
cover: "/img/cover/self-hosted-hindsight-local-model-routing.webp"
coverAlt: "Abstrakcyjna prywatna usługa pamięci kieruje zadania do lokalnych serwerów modeli CPU i GPU"
coverCaption: "Przechowywanie i wyszukiwanie pamięci oraz sprawdzone trasy modeli działają na własnym sprzęcie"
---

**Nasza usługa pamięci Hindsight działa na sprzęcie, nad którym mamy kontrolę.** Silnik pamięci, baza danych, model embeddingów i reranker działają w jednym samodzielnie hostowanym wdrożeniu. Hindsight wysyła żądania generowania do prywatnej bramy. Sprawdzony współdzielony backend Qwen oraz przetestowana trasa odświeżania stron używają lokalnych serwerów modeli bez subskrypcji hostowanego wnioskowania.

To opis jednego działającego wdrożenia. **Samodzielne hostowanie nie oznacza pracy offline.** VPN korzysta z zewnętrznej usługi koordynacyjnej, a obrazy oprogramowania i wagi modeli trzeba pobrać. Opisane tu twierdzenie dotyczy przetwarzania pamięci i wnioskowania modeli, a nie każdego połączenia sieciowego naszych urządzeń ani innych narzędzi agentów.

<!--more-->

## Najważniejsze informacje

- **Hindsight obsługuje cały przepływ pracy z pamięcią.** Kontener Docker udostępnia API, workery i płaszczyznę sterowania, a dane banków przechowuje wolumin trwały.
- **Małe modele wyszukiwania działają lokalnie.** Embeddingi i reranking działają na CPU wewnątrz procesu Hindsight.
- **Qwen generuje tekst.** Retain, Reflect i konsolidacja korzystają z prywatnego aliasu Qwen3.5-4B, z wyłączonym rozumowaniem i ograniczonym rozmiarem odpowiedzi. Sprawdzony backend obsługuje żądania lokalnie.
- **Długie odświeżanie stron otrzymuje GPU.** Osobny alias modelu rezerwuje jedną kartę na żądanie w tle, a po jego obsłużeniu zwalnia kartę.
- **Brama ukrywa fizyczne rozmieszczenie.** Hindsight wybiera alias modelu. Prywatne usługi trasujące wybierają punkt końcowy obsługujący żądanie.

## Określ granicę przed wyborem modeli

**Hindsight to silnik pamięci, a nie serwer modeli.** Pełny obraz Docker zawiera lokalne modele embeddingów i rerankingu, ale generowanie przez model językowy wymaga punktu końcowego. [Instrukcja instalacji Hindsight](https://hindsight.vectorize.io/developer/installation) opisuje ten podział i wskazuje lokalne serwery llama.cpp, Ollama oraz vLLM jako alternatywy dla dostawców hostowanych.

**API pamięci pozostaje w sieci prywatnej.** Webowa płaszczyzna sterowania działa na lokalnym interfejsie. Wolumin trwały przechowuje osadzoną bazę danych, więc ponowne utworzenie kontenera nie usuwa banków. Uwierzytelnianie chroni API, a osobne banki porządkują kontekst projektów.

**Brama generowania udostępnia stabilne nazwy modeli.** Hindsight wysyła żądania zgodne z OpenAI przez prywatną bramę i VPN. Brama przekazuje je do lokalnych punktów końcowych. Sprawdzona trasa Qwen dociera do wdrożenia LiteLLM mapowanego na lokalny serwer CPU. [Dokumentacja routera LiteLLM](https://docs.litellm.ai/docs/routing) opisuje ten wzorzec aliasów modeli. Równoważny router zgodny z OpenAI pełni taką samą funkcję.

{{< figure src="hindsight-private-request-path.webp" alt="Diagram agentów, prywatnej usługi Hindsight, lokalnych modeli wyszukiwania, prywatnej bramy i lokalnych serwerów Qwen" caption="Diagram pomija nazwy hostów, adresy, klucze dostępu i etykiety fizycznych hostów" >}}

[Otwórz diagram pełnej ścieżki żądania](hindsight-private-request-path.webp).

**Wewnętrzne API nadal istnieje.** Hindsight wywołuje prywatną bramę w formacie zgodnym z OpenAI. Sprawdzone trasy modeli obsługują wnioskowanie lokalnie. Nie przeprowadziliśmy audytu wszystkich reguł awaryjnego wyboru trasy w bramie, dlatego przed uznaniem lokalnego przetwarzania za gwarancję dla każdego żądania trzeba sprawdzić politykę bramy.

## Dopasuj każde zadanie pamięci do właściwych zasobów

Operacje Hindsight wykonują różne zadania. **Retain** wyodrębnia fakty z nowych materiałów. **Recall** wyszukuje trafne wspomnienia. **Reflect** wyszukuje informacje i tworzy odpowiedź syntetyzującą. **Consolidation** łączy powiązane fakty. Tłówne **knowledge-page refresh** ponownie tworzy aktualne podsumowanie banku.

| Operacja | Miejsce działania modelu | Powód |
| --- | --- | --- |
| **Retain** | Qwen3.5-4B przez prywatną bramę | Lokalna ekstrakcja strukturalna z ograniczonym budżetem odpowiedzi |
| **Recall** | Lokalne embeddingi CPU i reranking | Wyszukiwanie nie wymaga wywołania API generowania |
| **Reflect** | Qwen3.5-4B przez prywatną bramę | Synteza wymaga generowania po pobraniu wspomnień |
| **Consolidation** | Qwen3.5-4B przez prywatną bramę | Małe partie ograniczają długość odpowiedzi strukturalnych |
| **Knowledge-page refresh** | Dedykowana lokalna trasa Qwen na GPU | Duża synteza w tle przekroczyła limit czasu trasy CPU |

*Małe zadania wyszukiwania pozostaw na CPU, a wnioskowanie GPU rezerwuj dla zmierzonych zadań długotrwałych.*

Kontener Hindsight ładuje **BAAI/bge-small-en-v1.5** do embeddingów i **hindsight-ai/hs-rerank-1** do rerankingu. Dzienniki startowe potwierdzają, że oba modele działają lokalnie na CPU. [Dokumentacja modeli Hindsight](https://hindsight.vectorize.io/developer/models) opisuje lokalne opcje modeli i opcjonalną ścieżkę modelu decyzyjnego.

Zachowaliśmy dotychczasowy model embeddingów, ponieważ zmiana przestrzeni embeddingów wymaga ponownego utworzenia zapisanych wektorów. Reranker już działa lokalnie, więc hostowana usługa rerankingu stworzyłaby nową granicę przetwarzania danych, nie rozwiązując zaobserwowanego limitu czasu generowania. Lokalny pilotaż **hs-decide-1-flash** dał jedną poprawną odpowiedź Reflect, ale wynik pojawił się blisko testowego limitu czasu. Syntetyczne dane konsolidacji nie sprawdziły ścieżki decyzyjnej. Dlatego model decyzyjny nie należy do routingu produkcyjnego.

## Przydziel GPU wolnym zadaniom w tle

**Zwykła nazwa modelu różni się od nazwy modelu do odświeżania.** Retain, Reflect i konsolidacja korzystają ze współdzielonego aliasu Qwen. Odświeżanie stron w tle korzysta z aliasu GPU przypisanego do węzła, który dopuszcza jedno równoczesne wywołanie modelu językowego. Ogranicza to długie zadanie konserwacyjne do jednego GPU naraz.

**Rezerwacja przypisana do żądania ogranicza użycie GPU.** Pula GPU uruchamia worker modelu po nadejściu żądania. Kontroler rezerwuje jedną kartę, obsługuje żądanie, zatrzymuje workera i zwalnia rezerwację. Diagram pomija wykaz fizycznych hostów.

{{< figure src="hindsight-gpu-lease-cycle.webp" alt="Diagram pokazujący rezerwację jednego GPU na potrzeby odświeżenia strony w tle i jego zwolnienie po zakończeniu żądania" caption="Dzierżawa przypisana do żądania rezerwuje jeden GPU do odświeżenia strony" >}}

[Otwórz diagram pełnego cyklu dzierżawy GPU](hindsight-gpu-lease-cycle.webp).

Ten podział wynika z zaobserwowanej awarii. **Jedno odświeżenie strony w trybie CPU osiągnęło godzinny limit czasu.** Po przekierowaniu odświeżania w tle do lokalnej puli GPU pięć wcześniej nieudanych stron ukończyło się w około dwie do sześciu minut podczas jednego przebiegu odzyskiwania. Te wartości dotyczą tych stron i ustawień. Nie są ogólnym benchmarkiem przepustowości Qwen.

## Popraw domyślne limity i limity czasu

**Poprzednie limity wyjściowe Hindsight nie pasowały do naszego lokalnego routera.** Router akceptuje maksymalnie 8 192 tokeny wyjściowe i stosuje limit 256 tokenów, gdy żądanie nie podaje własnego. Poprzedni limit Retain wynoszący 64 000 tokenów powodował HTTP 400. Partie konsolidacji po osiem faktów kończyły się z powodu limitu długości odpowiedzi, a Reflect wymagał jawnego limitu, aby uniknąć domyślnego limitu routera wynoszącego 256 tokenów.

**Ustawiliśmy jawne limity dla każdego zadania.** Rozumowanie Qwen jest wyłączone dla tych operacji pamięci. Hindsight dopuszcza teraz łącznie cztery równoczesne wywołania LLM, w tym najwyżej jedno wywołanie odświeżania stron w tle. Globalny limit czasu LLM wynosi 1 800 sekund, z jedną ponowną próbą modelu.

| Obciążenie | Limit wyjścia lub partii | Limity wywołań i operacji |
| --- | --- | --- |
| **Retain** | 8 192 tokeny wyjściowe | Globalny limit czasu wywołania 1 800 sekund |
| **Reflect** | 4 096 tokenów wyjściowych | 900 sekund na wywołanie, 3 600 sekund na operację |
| **Consolidation** | 4 096 tokenów wyjściowych, cztery fakty na wywołanie | 900 sekund na wywołanie, 14 400 sekund na operację |
| **Page refresh** | Jedno równoczesne wywołanie modelu | 900 sekund na wywołanie, dedykowana trasa GPU |

*Te wartości opisują naszą lokalną instalację i router z listopada 2026 roku.*

**Limit czasu wywołania i limit czasu całej operacji obejmują różne etapy.** Niektóre prawidłowe wywołania Qwen przekraczały poprzedni limit 300 sekund. Dłuższe limity całych operacji pozwalają na pracę składającą się z wielu wywołań, a limit 900 sekund na wywołanie nadal ogranicza każdą próbę.

Podczas przebiegu odzyskiwania kilka zadań Retain zakończyło się z **1 042 do 2 076 tokenami wyjściowymi**. Dwa przebiegi konsolidacji ukończyły odpowiednio **41 z 41** i **30 z 30** elementów. Późniejsze wygaśnięcie limitu odświeżania strony doprowadziło do opisanej wyżej osobnej trasy GPU. Wyniki odzyskiwania nie dowodzą długoterminowej niezawodności.

## Jakie kompromisy wiążą się z tym projektem?

**Brak rachunku za hostowane modele nie oznacza braku kosztów.** Wdrożenie korzysta z własnego sprzętu, energii elektrycznej, pamięci masowej, czasu na konserwację i czasu GPU podczas odświeżania stron. Każdy wybór miejsca działania równoważy przepustowość z opóźnieniem lub prostotą operacyjną.

| Wybór | Korzyść | Kompromis |
| --- | --- | --- |
| **Generowanie z priorytetem CPU** | Zachowuje dostępność GPU | Przetestowane odświeżenie strony osiągnęło godzinny limit czasu |
| **Odświeżanie stron na GPU** | Pięć stron ukończyło się w około dwie do sześciu minut w jednym przebiegu | Zużywa zasoby GPU i zależy od dedykowanej trasy |
| **Osadzona baza danych** | Utrzymuje niewielkie wdrożenie | Zawęża domenę awarii i wymaga przetestowania kopii zapasowych |

*Użyj trasy GPU do odświeżania, gdy zmierzone opóźnienie CPU przekracza okno konserwacji.*

[Instrukcja instalacji Hindsight](https://hindsight.vectorize.io/developer/installation) zaleca osobny PostgreSQL w większych wdrożeniach produkcyjnych. **Nasza osadzona baza danych wymaga przetestowanej ścieżki kopii zapasowej i odzyskiwania** w miarę wzrostu banku.

**Prywatne wnioskowanie zależy od ścieżki żądania.** Sprawdź wybranego dostawcę Hindsight, mapowanie modeli w bramie, reguły awaryjnego wyboru trasy, lokalny proces modelu, retencję logów i wychodzący ruch sieciowy. Identyfikatory śledzenia Hindsight pomagają korelować żądania, a Docker rotuje logi kontenera. Żaden z tych elementów nie dowodzi, że dalsze żądanie pozostało lokalne. Audyt bramy dostarcza brakujących dowodów od początku do końca.

## Zalecenie

**Zacznij od lokalnych modeli wyszukiwania i jawnych limitów generowania.** Uruchom Hindsight oraz modele embeddingów i rerankingu na własnym sprzęcie. Kieruj generowanie przez prywatną bramę zgodną z OpenAI za pośrednictwem VPN. Zmierz każdą operację przed przydzieleniem zasobów CPU lub GPU, a trasę GPU rezerwuj dla zadań w tle, których opóźnienie CPU przekracza okno konserwacji.

*Sprawdź każdą regułę awaryjną bramy i przetestuj odzyskiwanie banku, zanim uznasz wdrożenie za prywatne i odporne.* [Przewodnik po granicach prywatności lokalnej AI](/articles/local-ai-privacy-boundary/) zawiera listę kontrolną na początek.

## Podsumowanie

**To wdrożenie utrzymuje pamięć Hindsight i sprawdzone ścieżki wnioskowania na własnym sprzęcie, bez subskrypcji hostowanego wnioskowania.** Lokalne wyszukiwanie CPU, ograniczone wywołania Qwen i trasa odświeżania stron na GPU z jednym wywołaniem obsługują różne rodzaje obciążenia. Przebiegi odzyskiwania ukończyły zadania Retain, konsolidację i odświeżanie stron przy tych ustawieniach. Następne kontrole to pełny audyt awaryjnych tras bramy, test kopii zapasowej i dłuższa obserwacja niezawodności.
