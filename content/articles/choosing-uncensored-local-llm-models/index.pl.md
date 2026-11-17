---
title: "Jak wybrać nieocenzurowany lokalny model AI"
date: 2026-11-15
lastmod: 2026-11-15
toc: true
draft: false
description: "Porównaj lokalne warianty pod kątem pełnych odpowiedzi, zachowanych możliwości, użycia kontekstu, kwantyzacji i wymagań VRAM."
genre: ["Lokalna AI", "AI hostowana samodzielnie", "Bezpieczeństwo AI", "Sprzęt GPU"]
tags: ["nieocenzurowana lokalna AI", "abliteracja", "lokalny LLM", "VRAM", "długość kontekstu", "kwantyzacja", "Ollama", "Qwen3.8", "Gemma 4"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Lokalna stacja robocza AI z kartą graficzną i monitorami pokazującymi wizualizacje modeli i inferencji"
coverCaption: ""
ref: ["/articles/local-ai-model-gpu-context-guide", "/articles/qwen38-27b-vast-ai-gpu-benchmark"]
---

**Wybór modelu:** oceń każdy wariant na podstawie użytecznych odpowiedzi, które kończy, zachowanej jakości i pamięci wymaganej przez twoje zadania. Mała liczba odmów ani popularna karta modelu nie potwierdzają tych wyników.

Etykieta **nieocenzurowany** nie oznacza standardowego poziomu wydajności. Wydawcy modeli stosują ją do różnych modyfikacji wag, dostrojeń i szablonów czatu. Porównaj każdego kandydata z modelem bazowym i sprawdź go na zadaniach, które chcesz wykonywać.

{{< youtube id="j-VqPVjztJE" enable="true" title="Przetestowałem wszystkie nieocenzurowane lokalne modele AI (od 8 GB do 32 GB VRAM)" description="Porównanie lokalnych wariantów modeli, kończenia odpowiedzi, ustawień kontekstu i poziomów pamięci GPU." >}}

## Co mówi etykieta

**Model po abliteracji** ma zmienione wagi, aby zmodyfikować część zachowań związanych z odmową. Artykuł z 2024 roku o kierunku odmowy pokazał jedną metodę dla 13 otwartych modeli czatu. Nowsze narzędzia oferują dodatkowe podejścia. Na przykład Heretic 2 opisuje ablację o dowolnej randze i ablację kierunkową. Etykieta na karcie modelu nie mówi, jakie zachowanie zmieniono ani na co wpłynęła modyfikacja.

Podczas porównywania modeli rozdziel cztery właściwości:

| Właściwość | Co sprawdzić |
|---|---|
| **Zachowanie przy odmowie** | Które prośby kończą się odmową, częściową odpowiedzią lub pełną odpowiedzią? |
| **Zachowanie możliwości** | Jak zadania dotyczące faktów, rozumowania, kodowania i formatowania wypadają w porównaniu z modelem bazowym? |
| **Ukończenie odpowiedzi** | Jak często generowanie kończy się przed limitem tokenów lub czasu? |
| **Dopasowanie do środowiska wykonawczego** | Czy dokładny skwantyzowany plik działa z pamięcią wystarczającą dla potrzebnego kontekstu? |

Zmodyfikowany model nadal działa probabilistycznie. **Oddziel kontrole jakości:** dokładność, niezawodność i bezpieczne użycie. Do pracy, w której zabezpieczenia mają znaczenie, zachowaj dostęp do normalnie dostrojonego modelu.

## Dlaczego liczba odmów słabo ocenia modele

**Wynik odmów** mierzy jeden rezultat dla jednego zestawu poleceń. Niewiele mówi o poprawności faktów, długości odpowiedzi ani o tym, czy model poda odpowiedź końcową przed wyczerpaniem budżetu generowania.

**Porównanie Qwen3.8-27B Sapwella z września 2026 roku** objęło model bazowy i osiem wariantów w tym samym środowisku serwowania. Zestaw 13 zadań mierzył wiedzę, matematykę, kodowanie i prawdomówność. Oddzielny zestaw HarmBench zawierał 400 szkodliwych próśb, a sędzia LLM analizował pełne odpowiedzi. Wyniki dotyczą jednej rodziny modeli, jednej karty GPU i jednego projektu ewaluacji.

| Wariant Qwen3.8-27B z badania | Jawne odmowy na 400 próśb | Odpowiedzi z niedokończonym rozumowaniem |
|---|---:|---:|
| **Model bazowy** | 381 | 0% |
| **OrcaRouter** | 2 | 38% |
| **Trohrbaugh** | 122 | 15% |

Wysoka liczba odmów modelu bazowego współwystępowała z mniejszą liczbą niedokończonych wyników. Niska liczba odmów OrcaRoutera współwystępowała z wyższym odsetkiem nieukończonych odpowiedzi. Trohrbaugh zachował więcej odmów i miał mniej nieukończonych odpowiedzi. **Dopasuj wybór do zadania i akceptowanych kompromisów.**

**Badanie 23 wariantów Gemma 4 E4B** wykazało znaczne straty w części pomiarów możliwości najczęściej pobieranego wariantu, podczas gdy mniejsza modyfikacja w testach pozostała zbliżona do modelu bazowego. Popularność i liczba pobrań opisują adopcję. Nie mierzą jakości.

Nie łącz tych pomiarów w jeden wynik. **Rozdziel miary:** odmowę, ukończenie, poprawność i opóźnienie. Zapisz też zestaw poleceń, wersję modelu, szablon rozmowy, środowisko wykonawcze, kontekst i limit wyjścia. Zmiana dowolnego ustawienia zmienia znaczenie porównania.

## Zdiagnozuj puste odpowiedzi przed zmianą modelu

**Tokeny rozumowania** zużywają limit wyjścia, zanim pojawi się widoczny tekst. Gdy limit skończy się podczas wewnętrznego rozumowania, niektóre środowiska zwracają pustą lub uciętą odpowiedź. To inny wynik niż odmowa albo ukończona, lecz błędna odpowiedź.

**Benchmark Qwen3.6-27B Sapwella** pokazał wpływ tego problemu na wyniki główne. Surowe wyniki matematyczne bardzo się różniły, ponieważ niektóre przebiegi nie docierały do odpowiedzi końcowej. Wśród ukończonych odpowiedzi zmierzona dokładność była znacznie bardziej zbliżona. Benchmark rozdzielał zdolność udzielenia odpowiedzi od wyczerpania budżetu na rozumowanie.

**Przy pustej odpowiedzi sprawdź powód zatrzymania i logi środowiska.** Zapisz długość polecenia, przydzielony kontekst, limit tokenów wyjściowych, czas działania i informację, czy model utworzył znacznik odpowiedzi końcowej. Następnie powtórz polecenie z większym limitem wyjścia, jeśli sprzęt ma wolną pamięć.

| Wynik | Prawdopodobna kategoria do sprawdzenia |
|---|---|
| **Tekst odmowy** | Model odmówił wykonania prośby. |
| **Puste wyjście po osiągnięciu limitu tokenów** | Budżet wyjścia skończył się przed odpowiedzią końcową. |
| **Ucięte wyjście** | Limit generowania przerwał niepełną odpowiedź. |
| **Błąd środowiska wykonawczego** | Nie zadziałał serwer, plik modelu lub przydział pamięci. |
| **Ukończona, ale błędna odpowiedź** | Model zwrócił tekst, lecz nie przeszedł kontroli poprawności. |

**Puste wyjście:** potwierdź wynik środowiska przed uznaniem każdego przypadku za wadę modelu. Większe okno kontekstu nie naprawi automatycznie niskiego limitu wyjścia, błędnego szablonu ani limitu czasu aplikacji.

## Zaplanuj VRAM na wagi i kontekst

Plik modelu to tylko jeden z odbiorców pamięci. Środowisko potrzebuje też miejsca na **pamięć podręczną KV**, która przechowuje stan uwagi dla aktywnego polecenia i odpowiedzi, a także na bufory obliczeniowe i inne załadowane procesy. Zwiększenie długości kontekstu zwiększa zużycie pamięci.

**Aktualna dokumentacja Ollama** podaje domyślne okna kontekstu: 4K przy mniej niż 24 GiB VRAM, 32K od 24 do 48 GiB i 256K przy co najmniej 48 GiB. Te wartości opisują domyślne zachowanie środowiska. Sprawdź przydzielony kontekst i umiejscowienie procesora poleceniem `ollama ps`.

**Przykład dla Linuxa:** ta komenda ustawia domyślną wartość 16K dla nowych sesji serwera Ollama:

```bash
OLLAMA_CONTEXT_LENGTH=16384 ollama serve
```

**Sprawdź przydzielony kontekst** względem typowej długości wejścia i odpowiedzi z załadowanym modelem:

```bash
ollama ps
```

Kolumny `CONTEXT` i `PROCESSOR` pokazują przydział oraz informację, czy model działa na GPU, czy jest częściowo przeniesiony poza nią. **Przydział kontekstu:** widoczny limit nie gwarantuje, że całe okno zmieści się w VRAM.

### Punkt wyjścia według pamięci GPU

**Kandydaci na początek:** te rodziny modeli pojawiły się w porównaniach wariantów z 2026 roku. Rozmiary plików pochodzą z konkretnych repozytoriów z kwantyzacją. Zanim uznasz wariant za odpowiedni, potwierdź dokładny plik, obsługę środowiska i zmierzone zużycie pamięci.

| Pamięć GPU | Kandydat na początek | Główne ograniczenie |
|---|---|---|
| **8 GB** | Gemma 4 E4B, na przykład wariant `coder3101` | Utrzymuje mały plik wag. Zostaw pamięć na kontekst i bufory środowiska. |
| **12 GB** | Gemma 4 12B, na przykład plik GGUF Q4 `TrevorJS` o rozmiarze 7,4 GB | Zapewnia większe możliwości modelu, ale mniej miejsca na długi kontekst niż mniejszy wariant. |
| **16 GB** | Mniejszy model albo plik Q3 Qwen3.8-27B | Repozytorium Qwen podaje 13,72 GB dla Q3_K_S. Wydawca określa ten plik jako niskiej jakości. Zapas na kontekst będzie ograniczony. |
| **24 GB** | Qwen3.8-27B Q4_K_S lub Q4_K_M | Aktualne repozytorium podaje pliki 16,71 GB i 17,77 GB. Zostaw miejsce na pamięć podręczną i bufory. |
| **32 GB** | Qwen3.8-27B Q6_K | Aktualne repozytorium podaje plik 23,46 GB. Większy plik zostawia mniej pamięci na kontekst niż mniejsza kwantyzacja. |

*Traktuj to jako punkt wyjścia. Repozytoria i wersje się zmieniają, a sam rozmiar pliku nie przewiduje przydziału pamięci przez środowisko ani jakości odpowiedzi.*

Etykiety kwantyzacji GGUF podsumowują sposób kodowania. **Różnice między repozytoriami:** pliki o tej samej nominalnej głębi bitowej nie muszą mieć takiej samej jakości. Jedno repozytorium Qwen określa Q3_K_S jako niskiej jakości, a Q4_K_M jako wariant domyślny. Przed pobraniem sprawdź dokładny rozmiar pliku, kartę modelu, format polecenia i wyniki testów.

**Informacje o rozmiarze pamięci podręcznej i dopasowaniu lokalnej karty GPU** znajdziesz w [przewodniku po lokalnych modelach, GPU i kontekście](/articles/local-ai-model-gpu-context-guide/). Zalecenia skupiają się tam na zadaniach programistycznych. Ta strona dotyczy zmienionego zachowania przy odmowie i ewaluacji.

## Sprawdź szablon rozmowy i źródło modelu

**Szablon czatu** opakowuje wiadomości w tokeny i instrukcje oczekiwane przez model. Pakiet modelu czasem zawiera niestandardowy szablon lub polecenie systemowy. Takie zmiany wpływają na mierzone zachowanie, nawet gdy wagi pozostają bez zmian.

**Wpływ szablonu:** Sapwell znalazł wariant Qwen3.8, którego pakiet zawierał personę nakazującą modelowi nigdy nie odmawiać ani nie ostrzegać. Deklaracja o niskiej liczbie odmów zależała od tego szablonu. W porównaniu Sapwell ujednolicił szablony, aby test skupiał się na różnicach między wagami. Taka kontrola nie dowodzi, że dostarczony szablon jest złośliwy lub bezużyteczny.

**Przed instalacją:** sprawdź wydawcę, model bazowy, licencję, proces konwersji, kwantyzator, szablon i historię wersji. Porównaj model z oryginałem przy tym samym szablonie i środowisku wykonawczym. Jeśli karta modelu nie podaje metody ani konfiguracji testu, oznacz pochodzenie jako nieznane.

## Przeprowadź małą ewaluację dla swoich zadań

**Przygotuj powtarzalny zestaw poleceń** z typowych zadań, które należą do ciebie lub które masz prawo testować. Uwzględnij pracę modelu, pytania faktograficzne ze znanymi odpowiedziami oraz prośby o formatowanie z jasnymi kryteriami zaliczenia. Dodaj kilka bezpiecznych przypadków granicznych, aby zachowanie przy odmowie nadal wpływało na decyzję.

**Utrzymuj te same ustawienia testu** dla modelu oryginalnego i zmodyfikowanego wariantu. Nie zmieniaj polecenia systemowego, szablonu, kwantyzacji, wersji środowiska, kontekstu, limitu wyjścia ani ustawień próbkowania. Zapisz wersję modelu lub sumę kontrolną pliku wraz z wynikami.

Zapisuj osobno każdy wynik:

- **Ukończenie:** odpowiedź końcowa, odmowa, puste wyjście, ucięcie albo błąd środowiska.
- **Poprawność:** zaliczenie lub błąd względem oczekiwanej odpowiedzi albo kryteriów.
- **Użyteczność:** czy odpowiedź spełnia wymagania zadania.
- **Opóźnienie:** czas do pierwszego tokenu i całkowity czas generowania.
- **Pamięć:** przydzielony kontekst, użycie GPU i szczytowe zużycie VRAM.
- **Zachowanie bezpieczeństwa:** właściwa odmowa albo kontynuacja dla każdego przypadku granicznego.

Powtórz zestaw po zmianie jednej zmiennej. Jeśli po zwiększeniu limitu wyjścia odpowiedź zostanie ukończona, pierwsza awaria wynikała z budżetu. Jeśli odpowiedzi nadal są niepełne, sprawdź szablon modelu, tryb rozumowania, środowisko i wersję modelu. **Zachowaj wariant tylko wtedy, gdy poprawia zadanie docelowe bez nieakceptowalnych strat dokładności lub bezpieczeństwa.**

## Ogranicz wdrożenie

**Prywatność:** lokalna inferencja zależy od całego stosu. Sprawdź interfejs, logi, rozszerzenia, telemetrię i trasy sieciowe. Niezaufane wagi i niestandardowe szablony traktuj jak kod i konfigurację stron trzecich.

**Dostęp publiczny:** nigdy nie wystawiaj punktu końcowego modelu bezpośrednio do publicznego internetu. Odizoluj dostęp do narzędzi i używaj zmodyfikowanych wariantów wyłącznie do autoryzowanej pracy. Dostęp zdalny zabezpiecz prywatną bramą z uwierzytelnianiem, limitami żądań i izolacją sieciową. Pierwotny artykuł o kierunku odmowy omawia konsekwencje bezpieczeństwa modyfikacji usuwających odmowy.

## Podsumowanie

**Zasada wyboru:** wybierz model z najlepszymi zweryfikowanymi wynikami dla własnego zestawu zadań. Traktuj liczbę odmów jako jeden pomiar, a następnie sprawdź kończenie odpowiedzi, poprawność, działanie szablonu i zapas VRAM. Zacznij od pliku odpowiedniego dla swojej GPU, ustaw kontekst dla zadań i porównaj go z modelem bazowym przy identycznych ustawieniach.

**Aby dobrać GPU,** porównaj te wyniki z [benchmarkiem wynajmu GPU dla Qwen 27B](/articles/qwen38-27b-vast-ai-gpu-benchmark/). Jeśli nie masz pewności co do dokładnego pliku modelu lub docelowego kontekstu, wynajmij lub pożycz sprzęt przed zakupem.

## Źródła

- [Benchmark abliteracji Qwen3.8-27B](https://nathan.sapwell.net/posts/qwen38-27b-abliteration/), Nathan Sapwell, 6 września 2026.
- [Benchmark abliteracji Qwen3.6-27B](https://nathan.sapwell.net/posts/qwen36-27b-abliteration/), Nathan Sapwell, 2026-05-17.
- [Benchmark wariantów Gemma 4 E4B](https://nathan.sapwell.net/posts/gemma4-e4b-abliteration/), Nathan Sapwell, 1 sierpnia 2026.
- [Benchmark wariantów Gemma 4 12B](https://nathan.sapwell.net/posts/gemma4-12b-abliteration/), Nathan Sapwell, 28 sierpnia 2026.
- [Odmowa w modelach językowych zależy od jednego kierunku](https://arxiv.org/abs/2406.11717), Arditi i in., 2024.
- [Dokumentacja projektu Heretic](https://github.com/p-e-w/heretic/).
- [Oficjalna karta modelu Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B).
- [Dokumentacja Ollama o długości kontekstu](https://docs.ollama.com/context-length).
- [Karta modelu Gemma 4 E4B `coder3101`](https://huggingface.co/coder3101/gemma-4-E4B-it-heretic).
- [Pliki GGUF Gemma 4 12B od TrevorJS](https://huggingface.co/TrevorJS/gemma-4-12B-it-uncensored-GGUF).
- [Pliki GGUF OrcaRouter Qwen3.8-27B](https://huggingface.co/bartowski/orcarouter_Qwen3.8-27B-Uncensored-GGUF).
- [Format GGUF i typy kwantyzacji](https://huggingface.co/docs/hub/en/gguf), dokumentacja Hugging Face.
- [Źródło wideo: Przetestowałem wszystkie nieocenzurowane lokalne modele AI (od 8 GB do 32 GB VRAM)](https://www.youtube.com/watch?v=j-VqPVjztJE).
