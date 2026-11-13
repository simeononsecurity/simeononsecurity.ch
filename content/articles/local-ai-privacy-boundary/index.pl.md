---
title: "Prywatność lokalnej AI: co pozostaje na komputerze, a co nie"
date: 2026-10-10
lastmod: 2026-11-13
toc: true
draft: false
description: "Prześledź prompty, pliki modeli, narzędzia, logi, ekspozycję sieciową i koszty energii przed wyborem lokalnego wnioskowania albo hostowanej usługi AI."
genre: ["Lokalna AI", "Prywatność", "AI hostowana we własnym zakresie", "Cyberbezpieczeństwo", "Ekonomia AI"]
tags: ["prywatność lokalnej AI", "lokalne wnioskowanie", "AI w chmurze", "prywatność danych AI", "AI hostowana we własnym zakresie", "prywatność LLM", "koszt posiadania GPU", "koszt energii AI", "RTX 5070", "Claude Haiku 5.5", "prywatność Ollama", "llama.cpp", "bezpieczeństwo AI", "AI bez połączenia z internetem", "lokalne modele językowe", "prywatność promptów", "model zagrożeń AI", "próg rentowności GPU", "granica danych AI", "prywatna AI"]
cover: "/img/cover/local-ai-vs-chatgpt-comparison-illustration.webp"
coverAlt: "Lokalna stacja robocza AI połączona z usługą chmurową przez widoczne ścieżki danych"
coverCaption: "Ilustracja lokalnych i hostowanych ścieżek danych AI"
---

**Lokalna AI daje mniejszą granicę danych.** Prompt przetworzony przez lokalne środowisko pozostaje na urządzeniu, gdy model, narzędzia, logi i ścieżka sieciowa pozostają lokalne. Lokalny GPU nie zamienia komputera w szczelny system.

Środowiska modeli, wtyczki narzędzi, rozszerzenia przeglądarki, zdalny dostęp, wystawione API i pobieranie modeli nadal kształtują ryzyko. Koszt też ma znaczenie. Energia może kosztować mniej niż hostowany token, a posiadanie sprzętu może odsunąć pełny próg rentowności daleko w przyszłość.

Ten poradnik najpierw mapuje granicę prywatności. Potem sprawdza koszt przy użyciu bieżących cen dostawców, jawnego założenia mocy i zgłoszonych wyników z dostarczonego filmu.

<!--more-->

To porównanie kosztów lokalnych i hostowanych daje kontekst dla poniższych wzorów. Nie kopiuj wyników przepustowości bez przetestowania tego samego pliku modelu i środowiska na swoim sprzęcie.

{{< youtube id="DmkuFpoMYmc" enable="true" title="Is local AI worth it? We did the math vs Claude Haiku 5.5" description="A local-versus-hosted AI cost comparison." >}}

Film podaje czas działania 2 minuty 31 sekund. Zweryfikowałem jego tytuł i czas na stronie filmu. Nie odtworzyłem testu sprzętu, więc zgłoszone prędkości pozostają pomiarami podanymi przez źródło.

## Krótka odpowiedź

- **Wybierz lokalne wnioskowanie dla kontrolowanej ścieżki danych.** Trzymaj serwer modelu na urządzeniu, przypnij go do loopback i ogranicz dostęp narzędzi.
- **Wybierz hostowane wnioskowanie do okazjonalnej pracy.** Unikaj wydatków na sprzęt, gdy obciążenie jest małe albo preferowany model nie mieści się w systemie.
- **Traktuj lokalny koszt jako dwie liczby.** Oddziel energię za aktywną godzinę od posiadania sprzętu.
- **Traktuj prywatność jako cechę systemu.** Prywatny model traci korzyść, gdy wtyczka wysyła pliki albo lokalne API nasłuchuje na każdym interfejsie sieciowym.

Lokalne wnioskowanie pomaga, gdy wrażliwy tekst musi pozostać wewnątrz stacji roboczej albo odizolowanej sieci. Pomaga też przy pracy offline, stałej wersji modelu i przewidywalnym dostępie bez limitu dostawcy.

Te korzyści nie dowodzą lepszych odpowiedzi. Model hostowany może lepiej pasować do zadania, kończyć je szybciej albo wymagać mniej utrzymania. Zmierz obciążenie przed zakupem sprzętu.

## Prześledź ścieżkę danych

Zmapuj każdy komponent używany w żądaniu. Sama nazwa modelu nie pokazuje, dokąd płyną dane.

| Komponent | Pytanie o prywatność | Zbierane dowody |
|---|---|---|
| **Lokalny serwer modelu** | Czy prompt pozostaje na hoście? | Konfiguracja procesu, adres nasłuchu i ruch wychodzący |
| **Model chmurowy** | Który tekst, pliki i wyniki narzędzi opuszczają hosta? | Endpoint API, warunki dostawcy, logi żądań i ustawienia konta |
| **Tryb chmurowy w lokalnej aplikacji** | Czy wybrany model działa na urządzeniu? | Identyfikator modelu, etykieta dostawcy i połączenie sieciowe |
| **Wtyczka narzędzia** | Czy model otrzymuje pliki, wynik powłoki albo treść przeglądarki? | Lista narzędzi, uprawnienia i przechwycone dane żądania |
| **Pobranie modelu** | Jaki kod i wagi trafiają na hosta? | Repozytorium źródłowe, licencja, suma kontrolna wydania i ścieżka pobrania |
| **Lokalne logi** | Gdzie utrwalają się prompty i wyniki narzędzi? | Logi środowiska, historia powłoki, raporty awarii i zakres kopii zapasowych |

**Lokalny model usuwa jednego dostawcę ze ścieżki promptu.** Nie usuwa potrzeby sprawdzenia reszty ścieżki.

## Lokalny nie znaczy prywatny domyślnie

[Polityka prywatności Ollama](https://ollama.com/privacy) stwierdza, że Ollama nie widzi promptów ani danych, gdy model działa lokalnie. Polityka oddziela też działanie lokalne od modeli hostowanych w chmurze. Model chmurowy nadal tworzy granicę usługi, nawet gdy ta sama aplikacja uruchamia oba tryby.

[Dokumentacja serwera llama.cpp](https://github.com/ggml-org/llama.cpp/tree/master/tools/server) pokazuje, że lokalny serwer domyślnie nasłuchuje na `127.0.0.1:8080`. Przykłady Dockera pokazują też `--host 0.0.0.0`, co wystawia usługę na wszystkie interfejsy. Szerszy adres bindowania zmienia granicę dostępu.

Sprawdź adres nasłuchu przed wysłaniem wrażliwego tekstu:

```bash
lsof -nP -iTCP -sTCP:LISTEN | rg 'ollama|llama|8080|11434'
```

`127.0.0.1` albo `localhost` w zwykłym przypadku ogranicza dostęp do tego samego hosta. Adres LAN albo `0.0.0.0` wymaga reguły zapory i planu uwierzytelniania. Nie wystawiaj endpointu modelu do sieci przed przetestowaniem obu wariantów.

Sprawdź też nazwę wybranego modelu. Dokumentacja chmurowa Ollama opisuje modele chmurowe jako osobną ścieżkę usługi. Lokalny interfejs nie dowodzi lokalnego wykonania.

FAQ Ollama [FAQ](https://docs.ollama.com/faq) opisuje tryb tylko lokalny. Ustaw `disable_ollama_cloud` w `~/.ollama/server.json` albo ustaw `OLLAMA_NO_CLOUD=1` przed ponownym uruchomieniem usługi. Usuwa to modele chmurowe Ollama i wyszukiwanie sieciowe z wybranego środowiska. Nie ogranicza innych aplikacji, narzędzi przeglądarki, wtyczek ani dostępu sieciowego na hoście.

```json
{
  "disable_ollama_cloud": true
}
```

Zweryfikuj ustawienie po restarcie. Środowisko tylko lokalne zawęża jedną ścieżkę. Nie ustanawia prywatnego hosta.


## Mowa Ollama i granica sieci

*Wydanie [Ollama v0.40.11](https://github.com/ollama/ollama/releases/tag/v0.40.11) zapowiada generowanie mowy w macOS. [Dokumentacja API](https://docs.ollama.com/api/openai-compatibility) wskazuje, że `/v1/audio/speech` jest dostępne od v0.40.8, więc v0.40.11 nie jest pierwszą udokumentowaną wersją tego endpointu.* To **synteza mowy**, a nie zamiana mowy na tekst: żądanie wysyła tekst do modelu mowy, takiego jak Phonon, i otrzymuje strumień audio. [Przewodnik po mowie](https://docs.ollama.com/capabilities/speech) pokazuje też, jak `ollama run phonon` odtwarza audio lokalnie albo zapisuje plik WAV po przekierowaniu wyjścia.

**Lokalna ścieżka mowy** wymaga pobranego modelu lokalnego i lokalnego serwera. [FAQ Ollamy](https://docs.ollama.com/faq) podaje, że serwer domyślnie nasłuchuje na `127.0.0.1:11434`, a **`OLLAMA_HOST`** zmienia adres nasłuchiwania. Sprawdź aktywny listener poleceniem `lsof` z wcześniejszego przykładu, zamiast zakładać, że nadal działa wartość domyślna. [Wprowadzenie do API Ollamy](https://docs.ollama.com/api/introduction) informuje, że lokalne żądania nie wymagają klucza API. Zanim wyślesz prywatny tekst, ogranicz szersze nasłuchiwanie zaporą i kontrolą dostępu.

**Nasłuchiwanie na loopback nie wyznacza całej granicy.** Ollama opisuje przekazywanie serwera HTTP przez reverse proxy lub tunel. Sprawdź listener, uwierzytelnianie i rejestrowanie żądań każdego proxy, nawet gdy Ollama nadal nasłuchuje tylko na loopback. Wysłany tekst i odebrane audio przechodzą przez połączenie proxy. [Instrukcja rozwiązywania problemów Ollamy](https://docs.ollama.com/troubleshooting) wskazuje logi serwera, ale dokumentacja mowy nie obiecuje, że audio nie będzie przechowywane. Sprawdź, gdzie klienci zapisują wyjściowe pliki WAV i gdzie pozostają logi proxy lub aplikacji. FAQ Ollamy mówi, że przy lokalnym uruchomieniu Ollama nie widzi promptów ani danych. Pobieranie modeli wymaga sieci, a modele chmurowe korzystają z innej ścieżki. W konfiguracji używającej wyłącznie lokalnych modeli Ollamy opisane wyżej `OLLAMA_NO_CLOUD=1` wyłącza funkcje chmurowe Ollamy. Nie kontroluje innych aplikacji.

## Policz koszt hostowany

Ceny tokenów rozdzielają wejście i wyjście. [Anthropic podaje cenę Claude Haiku 5.5: 0,10 USD za milion tokenów wejściowych i 0,50 USD za milion tokenów wyjściowych dla promptów do 100 000 tokenów](https://www.anthropic.com/claude/haiku). Prompty powyżej 100 000 tokenów używają wyższych stawek z cennika.

[Przewodnik OpenAI o tokenach](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens) wyjaśnia, dlaczego liczba słów nie równa się liczbie tokenów. Rozdziela też tokeny wejściowe, wyjściowe, buforowane i służące do rozumowania. Zamiast szacunku na podstawie liczby słów użyj danych o użyciu od dostawcy.

Do prostego porównania użyj miliona wygenerowanych tokenów i miliona tokenów wejściowych jako oddzielnych obciążeń. Agent kodujący często wysyła powtarzający się kontekst i tworzy krótszą odpowiedź, więc jedna łączna liczba tokenów ukrywa mieszankę kosztów.

## Oblicz lokalną moc

[Zapowiedź premiery NVIDIA RTX 5070](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/) podała cenę początkową $549. [Strona rodziny NVIDIA RTX 5070](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/) podaje 12 GB pamięci i 250 W całkowitej mocy graficznej w referencyjnej konstrukcji Founders Edition. Strona produktu NVIDIA nadal podaje $549, a podczas tej weryfikacji karta była niedostępna.

Wartość mocy GPU nie oznacza mocy całego systemu. Użyj miernika ściennego dla swojego PC. Poniższy przykład zakłada **pobór całego systemu 400 W**, w tym GPU, procesor, pamięć, pamięć masową, wentylatory i straty zasilacza. To założenie do obliczeń, a nie zmierzony wynik.

[Prognoza Amerykańskiej Agencji Informacji Energetycznej](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os) przyjęła 18,2 centa za kilowatogodzinę jako średnią domową cenę energii w 2026 roku. Twoja stawka za prąd zmienia wynik.

Użyj tego wzoru dla wygenerowanego wyjścia:

```text
lokalny koszt na 1M tokenów wyjściowych =
(whole_system_watts / 1,000)
× (1,000,000 / output_tokens_per_second / 3,600)
× electricity_price_per_kWh
```

Przy 400 W i $0.182 za kilowatogodzinę system kosztuje $0.0728 za aktywną godzinę.

| Prędkość wyjścia | Czas dla 1M tokenów | Koszt energii dla 1M tokenów |
|---:|---:|---:|
| **20 tokenów na sekundę** | 13 godzin 53 minuty | **$1.01** |
| **50 tokenów na sekundę** | 5 godzin 33 minuty | **$0.40** |
| **94 tokeny na sekundę** | 2 godziny 57 minut | **$0.22** |

Przy 50 tokenach wyjściowych na sekundę lokalna energia kosztuje mniej niż cena wyjścia Haiku 5.5 wynosząca $0.50. Przy 20 tokenach wyjściowych na sekundę lokalna energia kosztuje więcej. Próg prędkości wyjściowej przy tych założeniach wynosi około 40 tokenów na sekundę.

Obliczenie wejścia używa tego samego wzoru. Przy 2650 tokenach wejściowych na sekundę milion tokenów wejściowych zajmuje około 6 minut 17 sekund i kosztuje około $0.008 energii. Przy 1000 tokenów wejściowych na sekundę ta sama praca kosztuje około $0.020.

Dostarczony transkrypt podaje 94 tokeny wyjściowe na sekundę i 2650 tokenów wejściowych na sekundę dla przykładu RTX 5070. Powyższa arytmetyka zgadza się z tymi liczbami przy założeniu 400 W. Transkrypt nie podaje niezależnego zapisu laboratoryjnego, hasha pliku modelu, kompilacji środowiska, promptu ani odczytu miernika ściennego. Traktuj te prędkości jako wynik odniesienia, a nie gwarancję zakupu.

## Sprzęt zmienia próg rentowności

Oszczędność energii sama nie spłaca sprzętu. Porównaj pełny zakup z różnicą między hostowanym kosztem wyjścia a lokalnym kosztem zmiennym.

Przy 50 tokenach wyjściowych na sekundę:

```text
$0.50 cena hostowanego wyjścia - $0.40 koszt lokalnej energii = $0.10 oszczędności na 1M tokenów wyjściowych
$549 cena GPU / $0.10 = około 5.5 miliarda tokenów wyjściowych
```

Przy 94 tokenach wyjściowych na sekundę zaokrąglona oszczędność rośnie do około $0.28 na milion tokenów. Odzyskanie $549 za GPU wymaga wtedy około 2 miliardów tokenów wyjściowych. Obie liczby pomijają pamięć systemową, pamięć masową, płytę główną, zasilacz, chłodzenie, utrzymanie i wartość odsprzedaży.

Cena premierowa nie jest uniwersalną ofertą zakupu. Aktualna strona NVIDIA pokazywała oficjalną cenę bez dostępnego zapasu. Oferta sprzedawcy za $819 wymaga osobnej weryfikacji przed wprowadzeniem jej do modelu progu rentowności. Użyj prawdziwej faktury i zmierzonej mocy ze ściany.

**Istniejący sprzęt zmienia decyzję.** Jeśli stacja robocza ma już wystarczającą pamięć i odpowiedni GPU, koszt sprzętu jest utopiony dla kolejnego zadania. Porównaj moc, czas, jakość, prywatność i utrzymanie. Jeśli musisz kupić cały system, porównaj pełny system z użyciem hostowanym.

Szczegóły doboru modeli znajdziesz w [poradniku o lokalnych modelach AI i kontekście GPU](/articles/local-ai-model-gpu-context-guide/) oraz [poradniku doboru 16 GB pamięci VRAM](/articles/is-16gb-vram-enough-local-llm/). Opis zgłoszonej konfiguracji lokalnego agenta kodującego znajdziesz w [poradniku Strata i OpenCode](/articles/strata-opencode-local-coding-agent-16gb/).

## Co daje lokalna prywatność

- **Krótsza ścieżka danych:** prompt nie musi docierać do dostawcy modelu, gdy wnioskowanie pozostaje lokalne.
- **Praca offline:** pobrany model i lokalne środowisko nie potrzebują aktywnego połączenia z dostawcą do generowania tekstu.
- **Kontrola wersji:** wybierasz plik modelu i wersję środowiska zamiast otrzymywać automatyczną zmianę dostawcy.
- **Kontrola użycia:** lokalne wnioskowanie unika chmurowego licznika za żądanie po uwzględnieniu posiadania sprzętu i energii.
- **Kontrola polityki sieciowej:** zapora i kontrola hosta określają, kto dociera do endpointu modelu.

Te korzyści mają największe znaczenie dla kodu źródłowego, danych klientów, nieopublikowanych projektów, prywatnych notatek i pracy wykonywanej w odłączonym środowisku. Lokalne wnioskowanie nadal wymaga szyfrowania dysku, aktualizacji hosta, rozdzielenia kont i ograniczonych narzędzi.

## Czego lokalna prywatność nie daje

- **Gwarancji jakości:** mniejsze albo skwantyzowane modele wymagają testów względem prawdziwych kryteriów akceptacji.
- **Gwarancji łańcucha dostaw:** pliki modeli, środowiska, wtyczki i obrazy kontenerów wymagają zaufanych źródeł i kontroli integralności.
- **Czystego hosta:** złośliwe oprogramowanie, rozszerzenia przeglądarki, kopie zapasowe, raportery awarii i zdalna administracja nadal widzą dane hosta.
- **Bezpiecznego endpointu sieciowego:** serwer przypięty do każdego interfejsu tworzy nową usługę do obrony.
- **Darmowego systemu:** energia, pamięć masowa, chłodzenie, zużycie sprzętu i utrzymanie nadal kosztują.

[Poradnik Strata o lokalnym agencie kodującym](/articles/strata-opencode-local-coding-agent-16gb/) pokazuje, dlaczego pamięć systemowa, kontekst, dostęp narzędzi i ustawienia środowiska należą do oceny. Sama pamięć GPU nie określa granicy prywatności ani wydajności.

## Wybierz właściwą granicę

| Sytuacja | Lepszy pierwszy wybór | Powód |
|---|---|---|
| **Wrażliwe dokumenty i istniejący zgodny PC** | Wnioskowanie lokalne | Trzymaj prompty na kontrolowanym hoście i unikaj nowych wydatków na sprzęt |
| **Okazjonalne ogólne redagowanie** | Hostowane API lub usługa czatu | Zapłać za małe obciążenie i unikaj utrzymania |
| **Model frontier albo specjalistyczne narzędzie chmurowe** | Usługa hostowana | Wymagany model albo narzędzie nie jest dostępne na lokalnym hoście |
| **Duży powtarzalny wolumen ze sprawdzonym modelem lokalnym** | Uruchomienie lokalne albo hybrydowe | Porównaj energię, jakość, czas wsparcia i ceny dostawcy |
| **Mieszane obciążenia** | Kierowanie hybrydowe | Trzymaj wrażliwe zadania lokalnie i wysyłaj zatwierdzone ogólne zadania do modelu hostowanego |

**Routing hybrydowy wymaga jawnej reguły klasyfikacji.** Oznacz dane jako tylko lokalne, zatwierdzone do przetwarzania hostowanego albo zabronione do czasu przeglądu. Nie polegaj na nazwie modelu ani ikonie aplikacji przy egzekwowaniu reguły.

## Zweryfikuj przed zaufaniem

1. **Nazwij ścieżkę modelu.** Zapisz identyfikator modelu, środowisko, wersję i źródło pobrania.
2. **Sprawdź adres bindowania.** Potwierdź, że serwer nasłuchuje na loopback, chyba że szersza ścieżka ma udokumentowaną potrzebę.
3. **Wypisz każde narzędzie.** Przejrzyj dostęp do plików, powłoki, przeglądarki, sieci i wtyczek.
4. **Sprawdź trwałość danych.** Znajdź logi promptów, wyniki narzędzi, raporty awarii, kopie zapasowe i współdzielone katalogi modeli.
5. **Przetestuj zachowanie sieci.** Obserwuj połączenia podczas wrażliwego testu z reprezentatywnym promptem.
6. **Zmierz system.** Zapisz moc ze ściany, prędkość wyjścia, prędkość wejścia, długość kontekstu i ponowienia.
7. **Przetestuj zaakceptowaną pracę.** Porównaj ukończone zadania i wysiłek przeglądu, a nie tylko tokeny na sekundę.

[Poradnik porównujący lokalną AI z ChatGPT](/articles/local-ai-vs-chatgpt-how-close-are-we/) omawia kompromisy związane z możliwościami modeli. Użyj tej checklisty prywatności razem z testem jakości.

## Referencje

- [Wideo: Czy lokalna AI się opłaca? Porównanie z Claude Haiku 5.5](https://www.youtube.com/watch?v=DmkuFpoMYmc)
- [Zapowiedź premiery NVIDIA Blackwell GeForce RTX 50 Series](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/)
- [Specyfikacja rodziny NVIDIA GeForce RTX 5070](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/)
- [Strona produktu NVIDIA GeForce RTX 5070](https://marketplace.nvidia.com/en-us/consumer/graphics-cards/geforce-rtx-5070/)
- [Amerykańska Agencja Informacji Energetycznej, krótkoterminowe prognozy energetyczne z października 2026](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os)
- [Informacje o modelu Anthropic Claude Haiku 5.5](https://www.anthropic.com/claude/haiku)
- [Cennik platformy Anthropic](https://platform.claude.com/docs/en/about-claude/pricing)
- [OpenAI, rozumienie i liczenie tokenów](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens)
- [Polityka prywatności Ollama](https://ollama.com/privacy)
- [Informacje o wydaniu Ollama v0.40.11](https://github.com/ollama/ollama/releases/tag/v0.40.11)
- [Przewodnik po mowie Ollama](https://docs.ollama.com/capabilities/speech)
- [Dokumentacja API Ollama zgodnego z OpenAI](https://docs.ollama.com/api/openai-compatibility)
- [Wprowadzenie do API Ollama](https://docs.ollama.com/api/introduction)
- [FAQ Ollama: konfiguracja serwera, ustawienia chmury i reverse proxy](https://docs.ollama.com/faq)
- [Rozwiązywanie problemów Ollama i logi serwera](https://docs.ollama.com/troubleshooting)
- [Dokumentacja serwera llama.cpp](https://github.com/ggml-org/llama.cpp/tree/master/tools/server)
