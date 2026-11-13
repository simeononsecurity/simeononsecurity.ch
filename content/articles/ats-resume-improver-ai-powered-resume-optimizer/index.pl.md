---
title: "ATS Resume Improver: darmowy optymalizator CV oparty na AI"
date: 2026-07-22
lastmod: 2026-11-13
toc: true
draft: false
description: "ATS Resume Improver to darmowe narzędzie open source działające po stronie klienta. Analizuje, ocenia, dopasowuje, optymalizuje i eksportuje CV z użyciem modeli chmurowych lub lokalnych."
genre: ["Narzędzia kariery", "Projekty open source", "Sztuczna inteligencja", "Technologie prywatności", "Narzędzia dla programistów", "Poszukiwanie pracy", "Produktywność"]
tags: ["ATS Resume Improver", "optymalizacja ATS", "skaner CV", "CV AI", "CV OpenAI", "CV Claude", "lokalne AI Ollama", "własny hosting", "prywatność przede wszystkim", "narzędzia do szukania pracy", "analiza luk słów kluczowych", "list motywacyjny", "ocena CV", "React", "TypeScript", "Docker", "Vite", "otwarte oprogramowanie", "eksport PDF", "eksport DOCX", "parser CV", "narzędzia kariery", "przygotowanie do rozmowy", "szacowanie wynagrodzenia", "wykrywanie typu CV", "wynik ATS", "darmowe narzędzie CV", "GitHub", "bez zbierania danych"]
cover: "/img/cover/ai-resume-optimizer-self-hosted-ats-analysis.webp"
coverAlt: "Nowoczesny laptop na biurku wyświetla kolorowy interfejs optymalizacji CV z wykresami, na tle w ciemnym granatowym kolorze."
coverCaption: "ATS Resume Improver analizuje i optymalizuje CV w całości po stronie klienta, bez zbierania danych."
canonical: "https://simeononsecurity.com/articles/ats-resume-improver-ai-powered-resume-optimizer/"
---

**Darmowe, open source i możliwe do samodzielnego hostowania. Twoje CV nie trafia na serwer, chyba że używasz dostawcy AI. Nawet wtedy tekst trafia bezpośrednio do dostawcy AI, a nie do nas.**

## Czym jest ATS Resume Improver?

**[ATS Resume Improver](https://atsresumeimprover.netlify.app/)** to przeglądarkowy optymalizator CV typu open source. Analizuje CV w odniesieniu do oferty pracy i pomaga zmniejszyć różnicę między Twoim doświadczeniem a tym, co oceniają systemy śledzenia kandydatów (ATS). Narzędzie zbudowano w React 19, Vite i TypeScript. Cały **proces parsowania i oceniania działa w przeglądarce**, bez serwera backendowego.

Kod źródłowy znajdziesz pod adresem **[repozytorium ATS Resume Improver w GitHub](https://github.com/simeononsecurity/ats-resume-improver)**. Możesz skorzystać z hostowanej wersji, wdrożyć własną na Vercel/Netlify/Cloudflare/GitHub Pages jednym kliknięciem albo uruchomić ją lokalnie w Dockerze.

### Rozwiązanie problemu prywatności

Większość usług optymalizacji CV przesyła dokument na własny serwer, wykonuje zastrzeżoną ocenę i przechowuje dane. ATS Resume Improver działa inaczej.

| Tryb | Dane opuszczające Twoje urządzenie |
|------|------------------------|
| **Bez klucza AI** | Żadne. Wszystko działa lokalnie w przeglądarce. |
| **OpenAI / Anthropic** | Tekst CV i oferta pracy trafiają bezpośrednio do API dostawcy AI z użyciem Twojego klucza. Bez serwera pośredniczącego. |
| **Ollama (lokalnie)** | Żadne. Model działa na Twoim komputerze. |

**Klucze API są przechowywane tylko w pamięci** i znikają po zamknięciu karty. Bez analityki, śledzenia i plików cookie.

______

## Główne funkcje

### Co działa bez klucza AI

Klucz API nie jest potrzebny, by skorzystać z narzędzia. Tryb bez klucza obejmuje:

- **Przesyłanie CV**: PDF, DOCX, TXT lub Markdown
- **Ekstrakcja tekstu ATS**: pokazuje dokładnie, co system ATS odczytuje z pliku, także utratę formatowania
- **Wykrywanie typu CV**: automatycznie rozpoznaje, który z 7 profili pasuje do Twojego CV, i odpowiednio zmienia kolejność sekcji
- **Wykrywanie sekcji i ostrzeżenia o formatowaniu**: wskazuje brakujące sekcje i formaty utrudniające pracę parserów
- **Wynik ATS (0–100)** z podziałem na 5 wymiarów
- **Analiza luk słów kluczowych**: porównanie oparte na regułach z opisem stanowiska
- **Deterministyczna optymalizacja ATS**: lokalne porządkowanie według reguł
- **Porównanie przed i po zmianach**: dokładny podgląd wprowadzonych zmian
- **Profesjonalny eksport do PDF, DOCX, TXT i Markdown**

### Co daje AI

Połącz OpenAI, Anthropic Claude lub lokalną Ollamę, a narzędzie zyska dodatkowe funkcje:

- **Semantyczna analiza słów kluczowych**: rozumie kontekst, a nie tylko zgodność ciągów znaków. Pokazuje siłę dopasowania (silne/umiarkowane/częściowe), miejsce dopasowania ("znaleziono w umiejętnościach i 3 rolach"), wagę słowa (krytyczne/wysokie/średnie/niskie) oraz 2–3-zdaniowe podsumowanie AI
- **Optymalizacja CV przez AI**: pełne przepisanie przy użyciu promptów zgodnych z dobrymi praktykami ATS
- **Eksport ulepszony przez AI**: AI formatuje plik PDF/DOCX przed pobraniem
- **Generowanie listu motywacyjnego**: reguły językowe usuwają charakterystyczne oznaki tekstu AI (szczegóły poniżej)
- **Przewidywanie pytań na rozmowie**: na podstawie oferty pracy
- **Szacowanie przedziału wynagrodzenia**

______

## Wykrywanie typu CV

Aplikacja automatycznie klasyfikuje CV do jednego z 7 profili i dostosowuje kolejność sekcji do oczekiwań rekruterów i systemów ATS na danym etapie kariery:

| Profil | Odpowiedni dla | Priorytet sekcji |
|---------|----------|-----------------|
| 🏢 **Doświadczony specjalista** | Ponad 5 lat, liniowa ścieżka kariery | Doświadczenie → Umiejętności → Wykształcenie |
| 🌱 **Poziom średni** | 2–5 lat | Doświadczenie → Umiejętności → Wykształcenie |
| 🎓 **Początkujący** | 0–2 lata | Umiejętności → Wykształcenie → Projekty → Doświadczenie |
| 🎒 **Student / świeżo po studiach** | Nadal studiuje | Wykształcenie → Projekty → Umiejętności → Doświadczenie |
| 🔬 **Pracownik naukowy / badacz** | Doktorat, publikacje | Wykształcenie → Badania → Publikacje → Doświadczenie |
| 📜 **Liczne certyfikaty** | Certyfikaty ważniejsze niż dyplom | Certyfikaty → Umiejętności → Doświadczenie → Wykształcenie |
| 🔄 **Zmiana kariery** | Wykryta przerwa lub zmiana ścieżki | Podsumowanie → Umiejętności transferowalne → Wykształcenie → Doświadczenie |

*Kolejność sekcji pozostaje taka sama podczas optymalizacji oraz eksportu do PDF, DOCX, TXT i Markdown, a nie tylko na ekranie.*

______

## Semantyczna analiza słów kluczowych przez AI

To wyróżnia narzędzie na tle prostych liczników słów kluczowych. Po skonfigurowaniu dostawcy AI analiza luk przechodzi od prostego porównywania ciągów znaków do rozumowania semantycznego:

| Wymiar | Bez AI | Z AI |
|-----------|-----------|---------|
| **Metoda dopasowania** | Tylko dokładna zgodność tekstu | Semantyczne rozumienie kontekstu |
| **Siła dopasowania** | — | Ocena silna / umiarkowana / częściowa |
| **Kontekst dopasowania** | — | "znaleziono w umiejętnościach i 3 rolach" |
| **Waga luki** | Wszystkie luki mają taką samą wagę | Krytyczna / wysoka / średnia / niska |
| **Sugestie** | Ogólne wskazówki | Konkretne sugestie dla każdego słowa |
| **Pokrycie %** | Liczba zgodnych ciągów | Waga semantyczna |
| **Podsumowanie** | — | 2–3-zdaniowa narracja AI |

*Lokalna analiza oparta na regułach działa natychmiast. AI uzupełnia ją asynchronicznie, gdy przeglądasz wyniki.*

______

## Obsługiwani dostawcy AI

Każde wywołanie AI zawiera prompty zgodne z dobrymi praktykami ATS, opracowanymi na podstawie wytycznych Harvard OCS i Columbia CCE.

### OpenAI

| Nazwa modelu | Zastosowanie |
|-------|----------|
| **GPT-4.1 mini** (domyślny) | Inteligentny, szybki i przystępny cenowo, zalecany |
| GPT-4o mini | Klasyczna szybka i przystępna opcja |
| GPT-4.1 | Najnowszy GPT-4.1, dobrze wykonuje instrukcje |
| GPT-4o | Wysoka jakość, flagowy model |
| GPT-4 Turbo | Duże okno kontekstu |
| GPT-3.5 Turbo | Najszybszy i najtańszy |

**Szacowany koszt**: około 0,002–0,05 USD za analizę CV.

### Anthropic Claude

| Nazwa modelu | Zastosowanie |
|-------|----------|
| **Claude Sonnet 4.5** (domyślny) | Szybki i inteligentny, zalecany |
| Claude Opus 4.5 | Najbardziej zaawansowany, dobry do złożonych zadań |
| Claude Haiku 4.5 | Najszybszy i najtańszy |
| Claude 3.5 Sonnet | Niezawodny i dobrze sprawdzony |
| Claude 3.5 Haiku | Szybki i przystępny cenowo model v3.5 |

### Ollama (lokalnie / na własnym serwerze)

Klucz API nie jest wymagany. Uruchom model na własnym sprzęcie. Ustaw `OLLAMA_ORIGINS=*`, aby zezwolić przeglądarce na dostęp.

| Nazwa modelu | Uwagi |
|-------|-------|
| **Llama 3.3** (domyślny) | Najnowszy Meta Llama, zalecany |
| Llama 3.2 | Meta Llama 3.2 |
| Mistral 7B | Szybki i wszechstronny |
| Mixtral 8x7B | Model typu mixture of experts |
| Qwen 2.5 | Alibaba Qwen 2.5 |
| DeepSeek R1 | Zaawansowane rozumowanie |
| Phi-4 | Microsoft Phi-4 |
| Gemma 3 | Google Gemma 3 |

Uruchomienie Ollamy lokalnie pozwala używać całego narzędzia offline. Żadne dane nie opuszczają komputera.

______

## Naturalnie brzmiące listy motywacyjne

Generator listów motywacyjnych stosuje celowy poradnik stylu, by usunąć charakterystyczne oznaki tekstu wygenerowanego przez AI. Reguły inspirowane są [ramami humanizacji tekstu AI autorstwa Sabriny Ramonov](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing). Każdy wygenerowany list spełnia następujące zasady:

- **Bez em dashy**: najmocniejszy sygnał AI jest całkowicie usuwany
- **Ponad 50 zakazanych słów i zwrotów**: leverage, utilize, dive deep, delve, embark, game-changer, groundbreaking, cutting-edge, pivotal, tapestry, harness, moreover, in conclusion, it's worth noting, ever-evolving, landscape, testament, not only...but also i inne
- **Bez Markdown w treści listu**: bez pogrubień oznaczonych gwiazdkami, hashtagów i średników
- **Domyślnie strona czynna**: strona bierna tylko wtedy, gdy wykonawca naprawdę nie ma znaczenia
- **Wymagane skrócone formy**: "I've", "I'm", "it's", nigdy "I have", "I am", "it is"
- **Zróżnicowana długość zdań**: krótkie, konkretne zdania przeplatają się z dłuższymi
- **Bez pustych wstępów**: "It's important to note that X" zamienia się na samo "X"
- **Konkretny szczegół z oferty w pierwszym akapicie**: pokazuje, że list nie pochodzi z szablonu

*Wynik brzmi jak tekst człowieka, bo reguły wymuszają taki styl.*

______

## Jakość eksportu

| Format | Zawartość |
|--------|-------------|
| **PDF** | Profesjonalna typografia, linie oddzielające sekcje, wypunktowania i dane kontaktowe |
| **DOCX** | Prawidłowo ułożony dokument Word (Packer.toBlob, zgodny z przeglądarką) |
| **TXT** | Czysty tekst z równymi odstępami, bezpieczny dla ATS |
| **Markdown** | Ustrukturyzowany `.md` z nagłówkami i listami |

Po skonfigurowaniu dostawcy AI eksport jest formatowany przez AI przed pobraniem i oznaczony plakietką ✨ AI-Enhanced.

______

## Własny hosting

### Wersja hostowana (bez konfiguracji)

Użyj aplikacji pod adresem **[wersja online ATS Resume Improver](https://atsresumeimprover.netlify.app/)**. Nie potrzebujesz konta, rejestracji ani karty kredytowej.

### Wdrożenie w chmurze jednym kliknięciem

| Platforma | Link |
|----------|------|
| **Vercel** | Wdrożenie repozytorium jednym kliknięciem |
| **Cloudflare Pages** | Wdrożenie jednym kliknięciem |
| **Netlify** | Wdrożenie jednym kliknięciem |
| **GitHub Pages** | Fork → Settings → Pages → GitHub Actions → automatyczne wdrożenie |

### Programowanie lokalne

```bash
git clone https://github.com/simeononsecurity/ats-resume-improver
cd ats-resume-improver

make install
make dev           # http://localhost:5173
```

### Docker (zalecany dla odtwarzalnych środowisk)

```bash
# Programowanie: automatyczne odświeżanie pod http://localhost:5173
make docker-dev

# Produkcja: nginx pod http://localhost:8080
make docker-prod

# Programowanie i Ollama razem (pełny lokalny stos AI)
make docker-dev-with-ollama
```

### Ollama całkowicie offline

```bash
# Uruchom kontener Ollama (modele pozostają po ponownym uruchomieniu)
make ollama

# Pobierz model
make ollama-pull MODEL=llama3.2

# Uruchom aplikację deweloperską i Ollama równolegle
make docker-dev-with-ollama
```

Otwórz aplikację, przejdź do panelu kluczy API, wybierz **Ollama (Local)**, ustaw adres `http://localhost:11434` i wybierz model. Żadne dane nie opuszczają komputera.

______

## Stos technologiczny

| Warstwa | Technologia |
|-------|-----------|
| **Framework** | React 19 + TypeScript |
| **Kompilacja** | Vite 8 |
| **Stylizacja** | Tailwind CSS v4 |
| **Ikony** | Lucide React |
| **Parser PDF** | pdfjs-dist |
| **Parser DOCX** | mammoth |
| **Eksport PDF** | jsPDF |
| **Eksport DOCX** | docx (Packer.toBlob) |
| **AI** | OpenAI · Anthropic Claude · Ollama |
| **Kontener** | Docker + nginx (multi-stage) + usługa Ollama |

Cały proces analizowania i oceniania (`atsAnalyzer.ts`, `keywordMatcher.ts`, `resumeTypeDetector.ts`) działa w przeglądarce. Integracje AI w `aiProvider.ts` wywołują API dostawców bezpośrednio z klienta. Nie ma serwera proxy.

______

## Praktyczny przewodnik

### Krok 1: Prześlij CV

Prześlij plik PDF, DOCX, TXT lub Markdown. Otwórz kartę **"What the ATS Sees"**, aby sprawdzić, czy parser poprawnie odczytał treść. Jeśli w tym widoku brakuje sekcji albo są uszkodzone, oprogramowanie ATS rekruterów będzie miało ten sam problem.

### Krok 2: Wklej opis stanowiska

Wklej pełną ofertę pracy do panelu Job Description. Pełniejsza oferta daje lepszą analizę słów kluczowych, więc nie skracaj sekcji wymagań.

### Krok 3: Sprawdź wynik ATS

Panel pokazuje wynik 0–100 oraz podział na 5 wymiarów. Podział wskazuje, na czym się skupić: problemy z formatem obniżają jeden wymiar, brakujące słowa kluczowe inny, a słabe opisy obowiązków jeszcze inny.

### Krok 4: Sprawdź luki słów kluczowych

Widok Keyword Analysis pokazuje, które słowa z oferty występują w CV, a których brakuje. Po włączeniu AI otrzymasz dopasowanie semantyczne i ocenę ważności. Luka "Critical" w kluczowej umiejętności technicznej wymaga większej uwagi niż luka "Low" dotycząca ogólnego hasła o umiejętnościach miękkich.

### Krok 5: Zoptymalizuj

- **Tryb deterministyczny**: przebudowuje strukturę według reguł. Jest bezpieczny, szybki i nie powoduje kosztów API.
- **Tryb AI**: pełne przepisanie przez LLM przy użyciu promptów zgodnych z dobrymi praktykami ATS.

Przejrzyj **porównanie przed i po zmianach**, aby zrozumieć każdą zmianę przed jej zaakceptowaniem.

### Krok 6: Eksportuj

Eksportuj do PDF, DOCX, TXT lub Markdown. Po włączeniu AI eksport jest formatowany z myślą o profesjonalnej prezentacji. Szablon PDF używa odpowiedniej typografii i układu znanego rekruterom.

______

## Integracja porad dotyczących CV

Do narzędzia dołączono materiał `RESUME_TIPS.md` (dostępny też w repozytorium GitHub), który opisuje:

- Jak systemy ATS oceniają CV
- Które reguły formatowania mają znaczenie i co psuje parsery
- Jak pisać skuteczne podsumowania, punkty i sekcje umiejętności
- Strategię słów kluczowych bez ich upychania
- Ton i strukturę listu motywacyjnego
- Listę kontrolną przed wysłaniem

*Przeczytaj go przed użyciem narzędzia, aby wiedzieć, co oznaczają wyniki.*

______

## Często zadawane pytania

### Czy narzędzie zapisuje moje CV?

Nie. Aplikacja działa całkowicie po stronie klienta. Żadne dane nie są zapisywane na serwerze. Dane sesji znajdują się w pamięci przeglądarki i znikają po zamknięciu karty.

### Mój wynik jest niski. Czy mam się martwić?

Wyniki ATS wskazują kierunek, a nie zaliczenie lub porażkę. Wynik 60 nie oznacza, że system ATS Cię odrzuci. Pokazuje mierzalne różnice między Twoim CV a konkretną przeanalizowaną ofertą. Użyj wyniku, aby ustalić kolejność zmian, a nie jako werdyktu.

### Czy mogę używać narzędzia z wieloma ofertami pracy?

Tak. W dowolnym momencie wklej nową ofertę. Analiza słów kluczowych i optymalizacja zostaną uruchomione ponownie dla nowego stanowiska. Każda analiza jest niezależna.

### Czy integracja Ollama naprawdę działa offline?

Tak, jeśli Ollama działa na Twoim komputerze lub komputerze w sieci lokalnej. Aplikacja wysyła tekst przez HTTP do Twojej instancji Ollama. Żadne dane nie trafiają do usług zewnętrznych.

### Jak dokładne jest wykrywanie typu CV?

Detektor stosuje heurystyki oparte na regułach i analizuje treść CV: wspomniane lata doświadczenia, oznaki wykształcenia, sekcje publikacji lub badań oraz sygnały przerw w karierze. Dobrze działa dla większości CV, ale może się pomylić w nietypowych przypadkach. Zastosowaną kolejność sekcji zawsze można zmienić.

______

## Plan rozwoju projektu

Funkcje w trakcie tworzenia lub planowane:

- Historia wersji CV przez IndexedDB
- Optymalizator profilu LinkedIn
- Obsługa Google Gemini
- Dodatkowe modele Ollama

Projekt jest objęty licencją MIT i przyjmuje pull requesty. Przed większymi zmianami najpierw otwórz issue.

______

## Podsumowanie

**ATS Resume Improver** wypełnia istotną lukę: oferuje poważną analizę CV bez przekazywania danych pośrednikom. Tryb bez klucza natychmiast daje konkretne wskazówki dotyczące formatowania i pokrycia słów kluczowych. Dodanie klucza AI rozszerza analizę o rozumowanie semantyczne, pisanie listów motywacyjnych i przygotowanie do rozmów. Kosztuje to grosze za analizę albo jest całkowicie darmowe z Ollamą.

Hostowana wersja działa pod adresem **[wersja online ATS Resume Improver](https://atsresumeimprover.netlify.app/)**. Pełny kod źródłowy znajdziesz na **[repozytorium ATS Resume Improver w GitHub](https://github.com/simeononsecurity/ats-resume-improver)**.

Jeśli hostujesz narzędzie na własnym serwerze do szukania pracy albo chcesz dostosować wagi i prompty dla konkretnej branży, konfigurację Dockera i przejrzystą strukturę projektu łatwo rozwidlić i zmodyfikować.

______

## Kurs optymalizacji CV

Jeśli chcesz skorzystać z uporządkowanego przewodnika po tym, co ocenia narzędzie, przeczytaj kurs uzupełniający:

**[Kurs optymalizacji CV: pokonaj systemy ATS i zdobądź więcej rozmów](/resume-optimization-course-start/)** — 9 modułów obejmujących punktację ATS, formatowanie, wypunktowania, słowa kluczowe, dopasowanie CV, listy motywacyjne i checklistę przed wysłaniem. Używaj narzędzia razem z kursem, aby otrzymywać natychmiastową informację zwrotną na każdym etapie.

______

## Źródła

1. [narzędzie online](https://atsresumeimprover.netlify.app/)
2. [repozytorium kodu źródłowego](https://github.com/simeononsecurity/ats-resume-improver)
3. [Porady dotyczące CV — RESUME_TIPS.md](https://github.com/simeononsecurity/ats-resume-improver/blob/main/RESUME_TIPS.md)
4. [Sabrina Ramonov — najlepszy prompt AI do nadawania tekstowi ludzkiego brzmienia](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing)
5. [dokumentacja API OpenAI](https://platform.openai.com/docs/)
6. [dokumentacja API Anthropic Claude](https://docs.anthropic.com/)
7. [Ollama — lokalny serwer LLM](https://ollama.com/)
