---
title: "Projekty ChatGPT i Claude: konfiguracja kontekstu AI do ponownego użycia"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Skonfiguruj projekty ChatGPT i Claude z ukierunkowanymi instrukcjami, aktualnymi plikami referencyjnymi i prostym testem ponownie użytego kontekstu."
genre: ["Sztuczna inteligencja", "Produktywność"]
tags: ["Projekty ChatGPT", "Projekty Claude", "instrukcje projektu AI", "kontekst AI", "konfiguracja projektu ChatGPT", "wiedza projektu Claude"]
cover: "/img/cover/effective-ai-chat-projects.webp"
coverAlt: "Dwie uporządkowane przestrzenie projektów AI z opisem projektu, plikami referencyjnymi i oddzielnymi rozmowami"
coverCaption: ""
---

[Wróć do kursu Praktyczny przepływ pracy z AI](/effective-ai-course-start/)

**Utwórz projekt, gdy kilka rozmów ma ten sam cel.** Umieść stałe instrukcje i zatwierdzone pliki referencyjne w jednym miejscu. Każdą rozmowę skup na jednym zadaniu. Ta lekcja wykorzystuje fikcyjny warsztat społecznościowy do ćwiczeń bez prywatnych danych.

**Cel nauki:** utworzysz projekt z dwoma kontrolowanymi źródłami i sprawdzisz zawarte w nich fakty w nowym czacie.

## Najważniejsze informacje

- **Instrukcje projektu** określają zachowanie do ponownego użycia w powiązanych czatach.
- **Źródła projektu** zawierają materiały referencyjne, z których ma korzystać asystent.
- **Historia rozmowy** zapisuje jeden dialog, ale nie zastępuje zatwierdzonego źródła.
- **Test w nowym czacie** pokazuje, czy konfiguracja projektu dostarcza wystarczający kontekst.

## Zanim zaczniesz

**Wymagania wstępne:** konto ChatGPT lub Claude oraz pakiet zadań z [lekcji 1](/articles/effective-ai-workflow-foundations/). Zarezerwuj 35 minut. Poziom jest podstawowy. Przez całe ćwiczenie używaj fikcyjnych nazw, dat i miejsc.

**Utwórz dwa małe pliki** na komputerze. Otwórz edytor zwykłego tekstu, wklej każdy poniższy blok do osobnego pliku i zapisz go pod podaną nazwą `.md`. Pliki Markdown to zwykły tekst. `workshop-brief.md` opisuje odbiorców i styl. `approved-schedule.md` zawiera fikcyjny oficjalny harmonogram.

```text
workshop-brief.md, wersja 1
Odbiorcy: osoby zapisane na warsztaty wprowadzające.
Styl: krótkie zdania, przyjazny i rzeczowy ton.
Nie wymyślaj cen, udogodnień dla osób z niepełnosprawnościami ani informacji o parkingu.
```

```text
approved-schedule.md, wersja 1
Znacznik źródła: WS-2026-11-12-R1
Wydarzenie: Wprowadzenie do bezpieczeństwa cyfrowego
Data: 2026-11-12
Początek: 7 p.m.
Miejsce: Community Room A
```

## Konfiguracja ChatGPT

1. **Otwórz „Projects”** na pasku bocznym ChatGPT i utwórz projekt o nazwie `Workshop Practice`.
2. **Dodaj oba pliki** jako źródła projektu.
3. **Otwórz ustawienia projektu** i dodaj poniższe instrukcje.
4. **Sprawdź ustawienia pamięci i udostępniania** konta oraz obszaru roboczego przed dodaniem rzeczywistych materiałów.

```text
Użyj approved-schedule.md jako źródła informacji o wydarzeniu.
Użyj workshop-brief.md w sprawie odbiorców i stylu.
Jeśli brakuje wymaganej informacji, poproś o źródło lub oznacz ją jako nieznaną.
Twórz wyłącznie wersje robocze. Nie wysyłaj ich ani nie publikuj.
Po każdej poprawionej wersji wypisz zmiany faktograficzne.
```

**Projekty ChatGPT łączą powiązane czaty, pliki i instrukcje.** Ustawienia projektu i dostępne funkcje zależą od planu i obszaru roboczego. Jeśli podczas tworzenia dostępna jest pamięć ograniczona do projektu, wybierz ją, aby wykonać czysty test izolacji. Przy domyślnej pamięci czat może korzystać z informacji spoza przesłanych plików. Unikatowy znacznik źródła poniżej pomaga sprawdzić plik bez uznawania odpowiedzi z pamięci za dowód odczytania pliku. Aktualne opcje pamięci sprawdź w [oficjalnym przewodniku po projektach ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt).

## Konfiguracja Claude

1. **Otwórz „Projects”** w Claude i utwórz projekt o tej samej nazwie ćwiczenia.
2. **Dodaj oba pliki** do wiedzy projektu.
3. **Ustaw te same pięć wierszy** jako instrukcje projektu.
4. **Rozpocznij nowy czat w projekcie**, aby przetestować konfigurację.

**Te kroki opisują klasyczne projekty Claude.** Anthropic udostępnia osobną wersję beta Projects wybranym użytkownikom Pro i Max Claude Code. W wersji beta projekt oznacza jedną rozmowę z równoległymi wątkami w chmurze. Sprawdź [Czym są projekty](https://support.claude.com/en/articles/9517075-what-are-projects) i korzystaj z interfejsu dostępnego na Twoim koncie. Instrukcje klasycznego projektu obowiązują we wszystkich czatach, a wiedza projektu udostępnia wspólne materiały referencyjne. Używaj przesłanych plików jako kontrolowanych faktów. Działanie pamięci projektu zależy od konta i ustawień, więc nie traktuj informacji z innego czatu jako zatwierdzonego harmonogramu. Aktualne opcje znajdziesz w [przewodniku konfiguracji projektów Claude](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

| Tryb projektu | Wspólne materiały do sprawdzenia | Nowy test |
|---|---|---|
| **Projekt ChatGPT** | Przesłane pliki, instrukcje i wybrany tryb pamięci | Nowy czat projektu podaje znacznik harmonogramu |
| **Klasyczny projekt Claude** | Wiedza projektu i instrukcje wspólne dla czatów | Nowy czat projektu podaje znacznik harmonogramu |
| **Claude Projects beta** | Źródła i kontekst w projekcie oraz wątkach w chmurze | Nowy wątek projektu podaje znacznik harmonogramu |

**Projekt gromadzi kontekst, ale nie zatwierdza źródła.** Znacznik pokazuje, czy nazwany plik dotarł do czatu. Mimo to samodzielnie porównaj datę, godzinę i salę z plikiem.

## Test nowego czatu

**Otwórz nową rozmowę w projekcie ChatGPT lub nowy czat w klasycznym projekcie Claude.** W wersji beta Claude Projects użyj nowego wątku projektu. Poproś o krótkie ogłoszenie. Nie podawaj harmonogramu w promptcie, aby to źródła projektu dostarczyły potrzebne fakty.

```text
Napisz 100-wyrazowy szkic wiadomości e-mail o nadchodzących warsztatach.
Podaj plik źródłowy i jego dokładny znacznik dla czasu i miejsca.
Po szkicu wypisz brakujące informacje.
Nie wysyłaj wiadomości.
```

| Wynik | Znaczenie | Następny krok |
|---|---|---|
| **Godzina, miejsce i znacznik są zgodne** | Plik jest dostępny w tym czacie | Samodzielnie potwierdź fakty w pliku |
| **Fakt został zmyślony** | Instrukcje lub użycie źródła nie zadziałały | Usuń ten fakt i doprecyzuj prośbę |
| **Brakuje źródła** | Odwołanie nie dotarło do tego czatu | Sprawdź przynależność do projektu i przesłanie pliku |
| **Pojawia się stara wersja** | Projekt zawiera nieaktualne materiały | Zastąp źródło i ponów test |

**Nie oceniaj wiarygodności na podstawie jednej prawidłowej odpowiedzi.** Domyślna pamięć projektu może podać znaną godzinę bez odczytania przesłanego pliku. Wymagaj dokładnego znacznika `WS-2026-11-12-R1`, a następnie powtórz test z poniższym sprzecznym szkicem:

```text
Popraw to zdanie na podstawie zatwierdzonego harmonogramu projektu:
„Zajęcia Wprowadzenie do bezpieczeństwa cyfrowego zaczynają się o 6 p.m. w Community Room A.”
Podaj zmianę faktograficzną, plik źródłowy i znacznik. Nie wysyłaj wiadomości.
```

**Oczekiwana odpowiedź:** wiersz podaje godzinę 19.00 i wskazuje `approved-schedule.md` ze znacznikiem `WS-2026-11-12-R1`. Zapisz każdy zaobserwowany błąd. Zaliczenie testu nie wymaga zmyślonego błędu.

**Przykładowy zapis testu:** nowy czat, pierwszy prompt, godzina 19.00, miejsce Community Room A, źródło `approved-schedule.md`, znacznik `WS-2026-11-12-R1`, zaliczony. Prompt sprzeczny, poprawiono 18.00 na 19.00, zaliczony. To tylko przykład. Zastąp go własnymi obserwacjami.

## Utrzymanie projektu

**Instrukcje projektu powinny być krótkie.** Umieszczaj w nich stałe zasady. Szczegóły konkretnego zadania podawaj w jego promptcie. Zastępuj nieaktualne pliki i oznaczaj ich wersje. Niepowiązane zadania przenieś do innego projektu, aby źródła sobie nie przeczyły.

**Przed udostępnieniem projektu** sprawdź jego pliki, czaty, instrukcje i listę dostępu. Projekt to przestrzeń robocza, a nie system zatwierdzania. Nawet plik o nazwie „approved” wymaga prawdziwego właściciela i rejestru wersji w przypadku ważnych zadań.

## Ćwiczenie i sprawdzenie

**Twój rezultat:** jeden projekt z dwoma syntetycznymi plikami źródłowymi, pięcioma wierszami instrukcji i krótkim zapisem testu. Zapisz zaobserwowaną godzinę i miejsce, nazwę oraz znacznik źródła, a także każdy zmyślony fakt. Po ćwiczeniu usuń projekt, jeśli nie jest już potrzebny.

**Oczekiwane rozumowanie:** nowy czat korzysta ze źródeł projektu w przypadku stałych faktów, a prompt określa bieżący wynik. Sprawdź odpowiedź w pliku. Gdy brakuje źródła albo pojawia się niewłaściwa wersja, wróć do konfiguracji projektu.

## Sprawdź swoją wiedzę

1. **Pytanie:** czy nowy czat projektu ChatGPT gwarantuje izolację przy każdym ustawieniu pamięci? **Odpowiedź:** nie. Sprawdź tryb pamięci projektu i przetestuj go za pomocą unikatowego znacznika źródła.

2. **Pytanie:** co zrobić, gdy projekt powtarza stary harmonogram? **Odpowiedź:** sprawdź dołączone źródło i zakres pamięci, a następnie zastąp nieaktualne materiały.

## Rozwiązywanie problemów

- **Brak ustawień projektu:** sprawdź aktualny plan i ustawienia obszaru roboczego w przewodniku dostawcy.
- **Sprzeczne odpowiedzi:** usuń zduplikowane lub nieaktualne pliki źródłowe, a następnie rozpocznij nowy czat.
- **Nieoczekiwane udostępnianie:** sprawdź członków projektu i usuń wrażliwe źródła przed dalszą pracą.
- **Powtarzające się odchylenia stylu:** skróć instrukcje i dodaj krótki przykład do promptu zadania.

## Następne kroki

**Przejdź do [Kontekstu repozytorium AGENTS.md](/articles/effective-ai-agents-md-context/)**. Następna lekcja przechodzi od projektu czatu do lokalnego repozytorium kodu.

**Nawigacja kursu:** [Wstecz: Podstawy przepływu pracy](/articles/effective-ai-workflow-foundations/), [Plan kursu](/effective-ai-course-start/).
