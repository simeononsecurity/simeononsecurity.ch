---
title: "OpenClaw i Hermes Agent: praktyczna ocena"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Oceń wyspecjalizowanych i działających długotrwale agentów AI za pomocą wykazu dostępu, przeglądu wyzwalaczy, zapisu przepływu danych i decyzji o pilotażu."
genre: ["Sztuczna inteligencja", "Inżynieria oprogramowania", "Produktywność"]
tags: ["wyspecjalizowani agenci AI", "OpenClaw", "Hermes Agent", "agenci roboczy", "ocena agentów AI", "długotrwale działający agenci AI"]
cover: "/img/cover/effective-ai-specialized-agent-evaluation.webp"
coverAlt: "Arkusz z narzędziami agenta, zapisaną pamięcią, wyzwalaczami, dziennikami i decyzją o przeglądzie"
coverCaption: ""
---

[Wróć do praktycznego kursu przepływów pracy z AI](/effective-ai-course-start/)

**Wybierz wyspecjalizowanego agenta na podstawie zadania i wymaganych uprawnień dostępu.** Agent roboczy sprawdzający jeden plik różni się od trwałego systemu, który odbiera wiadomości, zapisuje pamięć i wykonuje zaplanowane działania. Ta opcjonalna lekcja wykorzystuje OpenClaw i Hermes Agent jako przykłady, a następnie przedstawia arkusz oceny przed instalacją.

**Cel nauki:** porównasz dostęp i wyzwalacze agentów, a następnie zapiszesz decyzję o ograniczonym pilotażu.

## Najważniejsze informacje

- **Agent roboczy o określonej roli:** agent przypisany do jednego pytania lub artefaktu.
- **Agent trwały:** usługa lub sesja zachowująca stan albo reagująca na późniejsze wyzwalacze.
- **Wyzwalacz:** zdarzenie, wiadomość lub harmonogram rozpoczynający pracę.
- **Wykaz dostępu:** lista narzędzi, kont, plików i uprawnień zapisu przyznanych agentowi.
- **Decyzja o pilotażu:** odrzucić, przeprowadzić ograniczony test albo zatwierdzić określone zastosowanie.

## Zanim zaczniesz

**Wymagania wstępne:** [delegowanie](/articles/effective-ai-agent-delegation/), [ograniczone pętle agentów](/articles/effective-ai-bounded-agent-loops/) oraz fikcyjny przypadek użycia. Zarezerwuj 35 minut. Poziom trudności jest średni. Ta lekcja nie wymaga instalowania trwałego agenta.

**Przypadek użycia:** koordynator warsztatów chce, aby asystent odczytał harmonogram i przygotował projekt przypomnienia. Prośba nie upoważnia do wysłania przypomnienia. Ocena musi zachować tę granicę.

## Porównaj role

| Podejście | Typowe zadanie | Pierwsze pytanie |
|---|---|---|
| **Jeden czat** | Przygotowanie jednego przypomnienia | Czy harmonogram jest dostępny? |
| **Agent tylko do odczytu** | Niezależne sprawdzenie danych z harmonogramu | Jakie źródło ma odczytać? |
| **Agent programistyczny** | Aktualizacja lokalnego programu raportowego | Które pliki i testy mają zastosowanie? |
| **Trwała platforma** | Reagowanie na wiadomości lub harmonogramy w czasie | Jakie wyzwalacze, narzędzia i zapisane stany istnieją? |

**OpenClaw** to otwartoźródłowa platforma agentów z bramą, kanałami komunikacyjnymi, narzędziami, pamięcią, połączeniami MCP i podagentami. Jej [omówienie](https://docs.openclaw.ai/start/why-openclaw), [przewodnik po połączeniach MCP](https://docs.openclaw.ai/tools/mcp) i [przewodnik po podagentach](https://docs.openclaw.ai/tools/subagents) opisują te elementy. Przed pilotażem sprawdź aktywne ustawienia kanałów, narzędzi i piaskownicy.

**Hermes Agent** to aplikacja agentowa Nous Research. Rodzina modeli Hermes jest odrębna. [Dokumentacja](https://hermes-agent.nousresearch.com/docs/), [przewodnik delegowania](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation) i [przewodnik konfiguracji](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/) opisują CLI, komunikację, narzędzia, pamięć i delegowane zadania. [Przewodnik pamięci](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/) omawia lokalne magazyny i zatwierdzanie zapisów. Udokumentowana wartość domyślna `memory.write_approval` oraz `skills.write_approval` to `false`. W pilotażu wymagającym zatwierdzania zapisów włącz akceptację albo wyłącz odpowiedni magazyn. Zanim polegniesz na którymś zabezpieczeniu, sprawdź działającą konfigurację.

| Punkt oceny | OpenClaw | Hermes Agent |
|---|---|---|
| **Punkt wejścia** | Brama i podłączone kanały | CLI lub skonfigurowany interfejs komunikacyjny |
| **Delegowana praca** | Podagenci z regułami sesji i narzędzi właściwymi dla platformy | Delegowane zadania z regułami narzędzi właściwymi dla platformy |
| **Trwały stan** | Sprawdź włączoną pamięć i zapis sesji | Sprawdź ustawienia pamięci i profilu oraz zapisy umiejętności |
| **Powtarzalna praca** | Sprawdź skonfigurowane wyzwalacze i harmonogramy | Sprawdź [zadania cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron/) i stan bramy |
| **Pierwszy pilotaż** | Jedno ręczne żądanie przez wybrany kanał | Jedno ręczne żądanie przez CLI lub komunikację |

Tabela przedstawia punkty kontroli, a nie równoważne domyślne ustawienia bezpieczeństwa. Zapisz zainstalowaną wersję i aktywną konfigurację, zanim przyznasz dostęp do prawdziwych danych lub kont.

**Nazwy nie określają wspólnego modelu uprawnień.** „Podagent” w jednym produkcie może otrzymywać inne pliki, narzędzia i historię niż agent roboczy w innym. Sprawdź dokumentację zainstalowanej wersji i aktywne ustawienia, zamiast przenosić założenia między narzędziami.

## Wypełnij arkusz dostępu

**Dodaj jeden wiersz dla każdej możliwości** przed zainstalowaniem lub podłączeniem systemu. Jeśli produkt jest dostępny, użyj rzeczywistych ustawień. Wpisz „nieznane”, zamiast zgadywać.

| Pytanie | Odpowiedź dla pilotażu warsztatowego |
|---|---|
| **Zadanie** | Przygotowanie przypomnienia na podstawie syntetycznego harmonogramu |
| **Dane wejściowe** | Jeden zatwierdzony plik harmonogramu |
| **Pliki** | Odczyt pliku harmonogramu, bez uprawnień zapisu |
| **Narzędzia zewnętrzne** | Brak w pierwszym pilotażu |
| **Dostęp do kont** | Brak konta pocztowego i kalendarza |
| **Wyzwalacz** | Tylko ręczne żądanie |
| **Zapisy pamięci i umiejętności** | Zapisz aktywne ustawienia, wyłącz magazyny albo wymagaj zatwierdzania zapisów podczas pilotażu |
| **Dzienniki** | Zapisz ścieżkę przechowywania, regułę retencji, polecenie, wersję źródła i projekt |
| **Przegląd** | Człowiek sprawdza datę, godzinę, miejsce i listę odbiorców |
| **Wycofanie** | Odrzuć projekt i wyłącz pilotaż |

**Przepływ danych należy do arkusza.** Zapisz, gdzie dane wejściowe opuszczają komputer, który dostawca je przetwarza oraz gdzie pozostają transkrypcje lub pamięć. Jeśli narzędzie łączy się z pocztą, określ, czy odczytuje wiadomości, tworzy projekty czy je wysyła. To odrębne uprawnienia.

## Podejmij decyzję o pilotażu

**Odrzuć:** agent wymaga szerokich uprawnień zapisu w skrzynce pocztowej do zadania polegającego tylko na przygotowaniu projektu albo nieznane są jego wyzwalacze i dzienniki. Nie musisz niczego instalować, by odrzucić niedopasowane rozwiązanie.

**Pilotaż:** ogranicz wejście do syntetycznego harmonogramu, użyj ręcznego wyzwalacza, wyłącz wysyłanie i sprawdź jeden projekt. Oczekiwany wynik to poprawna godzina 19:00 i brak wysłanej wiadomości. Jeśli przeprowadzisz pilotaż, zapisz własną obserwację.

**Zatwierdź określone zastosowanie:** dopiero gdy pilotaż przejdzie kontrole, a właściciel zaakceptuje dokładny zakres dostępu, wyzwalacz, retencję i kroki przeglądu. Zatwierdzenie tworzenia projektów nie upoważnia do wysyłania ani późniejszej automatyzacji.

## Zdiagnozuj błąd

**Załóż, że projekt przypomnienia podaje godzinę 18:00.** Sprawdź, czy agent odczytał aktualny harmonogram, czy nieaktualna godzina pochodzi z zapisanej pamięci lub starej wiadomości. Zastąp nieaktualne dane wejściowe, powtórz ręczny pilotaż i pozostaw wysyłanie wyłączone. Poprawny drugi projekt nie usuwa pierwszego błędu z dokumentacji.

**Załóż, że połączenie MCP jest widoczne w ustawieniach, ale nie można użyć żadnego narzędzia.** Wróć do [stanów połączenia MCP](/articles/effective-ai-mcp-server-setup/). Zapisany wpis serwera nie dowodzi, że odczyt się powiódł.

## Ćwicz i sprawdź

**Twój artefakt:** wypełniony arkusz dostępu i jedna decyzja: Odrzuć, Pilotaż albo Zatwierdź określone zastosowanie. Wskaż jeden wyzwalacz, jedną granicę uprawnień, jedno pytanie o przepływ danych i jeden sposób zatrzymania agenta.

**Kontrola ukończenia:** inny czytelnik powinien wiedzieć, jakie działanie wykonuje agent, co odczytuje i zapisuje, kiedy działa, kto sprawdza wynik i jak go wyłączyć. Jeśli którejś odpowiedzi nie znasz, wybierz Odrzuć albo węższy pilotaż.

## Sprawdź swoją wiedzę

1. **Pytanie:** Czy zadanie przygotowania projektu przypomnienia wymaga prawa wysyłania poczty? **Odpowiedź:** Nie. Wysyłanie pozostaje poza zakresem pilotażu.
2. **Pytanie:** Które ustawienia Hermes należy sprawdzić przed pilotażem z kontrolowanymi zapisami? **Odpowiedź:** Sprawdź aktywne ustawienia zapisów pamięci i umiejętności, w tym mechanizmy zatwierdzania.

## Następne kroki

**Przejdź do [projektu końcowego przepływu pracy z AI](/articles/effective-ai-capstone/)**. Szersze porównanie środowisk uruchomieniowych znajdziesz w [przewodniku po środowiskach agentów](/articles/best-ai-agent-harnesses/).

**Nawigacja kursu:** [Wstecz: Ograniczone pętle](/articles/effective-ai-bounded-agent-loops/), [Plan kursu](/effective-ai-course-start/).
