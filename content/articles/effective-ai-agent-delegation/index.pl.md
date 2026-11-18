---
title: "Delegowanie zadań agentom AI: przydzielanie pracy i przegląd wyników"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Ustal, kiedy drugi agent AI pomoże, przydziel każdemu pracownikowi ograniczone zadanie, zapobiegaj konfliktom edycji i integruj dowody w głównej sesji."
genre: ["Sztuczna inteligencja", "Inżynieria oprogramowania"]
tags: ["delegowanie agentów AI", "subagenci", "agenci roboczy", "kontekst orkiestratora", "drzewa robocze AI", "równoległe zadania AI"]
cover: "/img/cover/effective-ai-agent-delegation.webp"
coverAlt: "Agent główny przydziela osobne zadania badawcze i przegląd testów, a następnie łączy krótkie raporty z dowodami"
coverCaption: ""
---

[Wróć do praktycznego kursu przepływu pracy AI](/effective-ai-course-start/)

**Deleguj, gdy niezależne pytanie uzasadnia osobną sesję.** Agent roboczy sprawdza źródła, przegląda testy albo przygotowuje ograniczoną zmianę we własnym kontekście. Agent główny sprawdza i integruje wynik. Ta lekcja porównuje dokumentację, a główna sesja zachowuje małe zadanie laboratoryjne.

**Cel nauki:** przydzielisz niezależny przegląd agentowi roboczemu i zweryfikujesz jego krótki raport dowodów.

## Najważniejsze informacje

- **Orkiestrator:** agent główny koordynujący zadanie i przegląd końcowy.
- **Agent roboczy:** osobny agent odpowiedzialny za jeden ograniczony wynik.
- **Niezależna praca:** podzadanie, którego odpowiedź nie zależy od niedokończonego wyniku innego agenta.
- **Własność:** nazwany plik lub pytanie przydzielone jednemu agentowi.
- **Integracja:** porównanie przez agenta głównego wyniku pracy z aktualnymi źródłami.

## Zanim zaczniesz

**Wymagania wstępne:** Twoje zapisy [przekazania kontekstu](/articles/effective-ai-context-window-management/) i [weryfikacji wyników](/articles/effective-ai-output-verification/). Zarezerwuj 40 minut. Poziom średni. Ścieżka połączona wymaga produktu obsługującego agentów roboczych. Ścieżka nauki korzysta z osobnego czatu i ręcznej integracji.

**Zacznij tę lekcję od czystego startera.** Zapisz poza laboratorium diff edytowanego filtra i rejestr testów. Rozpakuj oryginalny ZIP w nowym katalogu tymczasowym. Uruchom polecenie startowe i dwa testy bazowe. Powtórz bazę Git z lekcji konfiguracji kursu i odtwórz krótkie wskazówki `AGENTS.md` oraz opcjonalne `CLAUDE.md` z lekcji o kontekście repozytorium. Samodzielnie zatwierdź te pliki wskazówek i potwierdź, że `git status --short` jest czysty. Zachowaj edytowaną kopię filtra jako odniesienie, ale ćwiczenie wykonuj na czystym starterze.

## Zdecyduj, czy delegować

**Użyj jednego agenta** do małej, sekwencyjnej edycji. Delegowanie wymaga konfiguracji, tokenów i przeglądu. Przydziel zadanie agentowi roboczemu, gdy niezależne pytanie tylko do odczytu inaczej wypełniłoby główny czat wieloma plikami lub stronami źródłowymi.

| Zadanie laboratoryjne | Delegować? | Powód |
|---|---|---|
| **Dodanie filtra o dwóch wartościach** | Zwykle nie | Jeden mały plik i ukierunkowane testy |
| **Znalezienie brakujących przypadków w dwóch testach bazowych** | Zwykle nie | Główna sesja szybciej przeczyta jeden krótki plik |
| **Porównanie aktualnej dokumentacji trzech produktów** | Tak, tylko do odczytu | Czytanie źródeł pozostaje w kontekście agenta |
| **Dwukrotna edycja tej samej funkcji** | Nie | Równoczesne zmiany powodują konflikty |

**Agent roboczy powinien dostać mniej kontekstu niż orkiestrator,** a nie kopię całej rozmowy. Podaj cel, ścieżkę źródła, granice zadania i format odpowiedzi. W głównej sesji zachowaj krótki raport dowodów. Przed działaniem samodzielnie sprawdź cytowane pliki.

## Uruchom jednego agenta tylko do odczytu

**Utrzymuj małe zadanie główne.** W głównej sesji przeczytaj lokalny `AGENTS.md` i zanotuj, który plik zawiera polecenie testowe. Przydziel oddzielne pytanie badawcze poniżej jednemu agentowi. Nie potrzebuje całego laboratorium ani poprzedniego czatu.

**Ścieżka połączona:** w Codex, Claude Code lub innym kliencie obsługującym agentów otwórz laboratorium jako projekt i poproś agenta głównego o przydzielenie poniższego żądania tylko do odczytu jednemu agentowi. Sprawdź transkrypcję narzędzi, czy rzeczywisty agent się uruchomił i zwrócił raport. Jeśli produkt nie udostępnia agenta, użyj osobnej sesji i oznacz ją jako oddzielną sesję roboczą. Aktualne przewodniki [subagentów Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents), [subagentów Claude Code](https://code.claude.com/docs/en/sub-agents) i [agentów OpenCode](https://opencode.ai/docs/agents/) opisują bieżące ustawienia.

**Ścieżka nauki:** otwórz nowy czat dla tego samego żądania. Podaj trzy oficjalne linki lub fragmenty źródeł. Oznacz czat jako symulowanego agenta. Drugi czat to osobny kontekst, a nie dowód uruchomienia natywnego subagenta.

```text
Użyj aktualnej oficjalnej dokumentacji Codex AGENTS.md, Claude Code memory i OpenCode rules.
Porównaj, jak każdy produkt ładuje pliki instrukcji repozytorium.
Nie edytuj plików.
Zwróć najwyżej trzy wiersze: produkt, plik instrukcji, URL źródła i jedno zachowanie ładowania.
Zaznacz niepewność. Nie wklejaj całych stron.
```

**Zestaw źródeł:** [instrukcje projektu Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [pamięć Claude Code](https://code.claude.com/docs/en/memory) i [reguły OpenCode](https://opencode.ai/docs/rules/). Oczekiwany raport wskazuje `AGENTS.md` dla Codex i OpenCode. Aktualne wersje Claude Code także ładują bezpośrednio `AGENTS.md`, gdy pierwszeństwa nie ma `CLAUDE.md` ani `CLAUDE.local.md`. To laboratorium używa pliku `CLAUDE.md` z importem `@AGENTS.md`, który obsługuje także starsze lub inaczej skonfigurowane sesje. Sprawdź bieżące strony i aktywną wersję, zanim uznasz przykład za zaobserwowany wynik pracy agenta.

## Integruj ustalenia

**Samodzielnie otwórz cytowane strony źródłowe.** Jeśli agent twierdzi, że Claude Code zawsze wymaga importu `CLAUDE.md`, sprawdź jego przewodnik memory i popraw raport. Porównaj go z lokalnymi plikami wskazówek. Napisz krótką notatkę integracyjną:

```text
Przyjęto: Codex i OpenCode używają AGENTS.md jako instrukcji projektu.
Aktualny Claude Code może ładować AGENTS.md bezpośrednio. To laboratorium używa
CLAUDE.md z importem @AGENTS.md, aby zachować stabilną wspólną mapę.
Dowody: zapisz trzy aktualne oficjalne adresy URL i datę przeglądu.
Decyzja: zachowaj krótką wspólną mapę i import dla Claude.
```

**Ta notatka jest użytecznym wynikiem pracy agenta.** Orkiestrator potrzebuje zweryfikowanych ustaleń i ścieżek źródeł, a nie transkrypcji badań. Delegowanie zwiększa łączną liczbę tokenów, więc ograniczaj główną rozmowę tylko wtedy, gdy osobna sesja oszczędza uwagę.

## Przydziel własność edycji

**Jeśli agenci edytują pliki,** podziel własność według plików lub użyj oddzielnych worktree dla nakładających się zadań repozytorium. Worktree to kolejna kopia tego samego repozytorium Git z własnymi plikami roboczymi. Pozwala oddzielić równoczesne edycje. Agent główny sprawdza zmiany i przenosi je przez jawny merge, cherry-pick lub patch, a następnie ponownie uruchamia testy w zintegrowanym drzewie.

| Agent | Przydzielona praca | Zwróć |
|---|---|---|
| **Implementacja** | `task_report.py` | Diff i polecenie testowe |
| **Autor testów** | `tests/test_task_report.py` | Przypadki testowe i zaobserwowany wynik |
| **Orkiestrator** | Wymagania i integracja końcowa | Połączony diff i kryteria akceptacji |

**Małe laboratorium nie potrzebuje równoległych edycji.** Tabela pokazuje podział własności dla większych prac. Testy w jednym worktree nie sprawdzają implementacji nadal odizolowanej w innym. Jeśli dwóch agentów potrzebuje tej samej funkcji, pracuj sekwencyjnie albo poproś jednego o przegląd bez edycji. Oddzielne worktree zapobiegają kolizjom plików, ale nie rozwiązują sprzecznych wymagań.

## Sprawdź zachowanie produktu

**Subagenci różnią się zależnie od hosta.** Codex, Claude Code i OpenCode inaczej dziedziczą kontekst, obsługują uprawnienia narzędzi i zwracają wyniki. Przeczytaj przewodniki dla [subagentów Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents), [subagentów Claude Code](https://code.claude.com/docs/en/sub-agents) i [agentów OpenCode](https://opencode.ai/docs/agents/) dla zainstalowanego produktu. Nie zakładaj, że agent współdzieli cały kontekst sesji głównej albo działa w odizolowanym worktree.

## Ćwicz i sprawdź

**Wynik:** krótki raport agenta dotyczący dokumentacji oraz notatka integracyjna. Na ścieżce nauki użyj nowego czatu i oznacz go jako symulowanego agenta. Nie twierdź, że na tej ścieżce uruchomiono natywnego subagenta.

**Kontrola ukończenia:** raport wymienia trzy oficjalne źródła, mieści się w zakresie pytania i zachowuje limit długości. Notatka integracyjna sprawdza źródła i nazywa pliki wskazówek używane przez laboratorium.

## Sprawdź zrozumienie

1. **Pytanie:** Kiedy agent roboczy pomaga bardziej niż pojedynczy agent? **Odpowiedź:** Gdy odpowiada za niezależne pytanie lub wynik i dostarcza użyteczny raport dowodów.

2. **Pytanie:** Co zrobić, gdy dwóch agentów zmieni nakładające się pliki? **Odpowiedź:** Zintegruj zmiany, obejrzyj połączony diff i ponownie uruchom kontrole.

## Rozwiązywanie problemów

- **Agent zwraca długi transkrypt:** poproś o krótszą tabelę dowodów z odniesieniami do plików.
- **Agenci się nie zgadzają:** przed wyborem odpowiedzi przeczytaj ponownie wiążący plik.
- **Dwie edycje się nakładają:** zatrzymaj jedną i ustal własność plików albo rozdziel worktree.
- **Dostęp agenta do narzędzi jest inny:** sprawdź jego uprawnienia, zamiast zakładać zgodność z ustawieniami agenta głównego.

## Następne kroki

**Kontynuuj [ograniczone pętle celów](/articles/effective-ai-bounded-agent-loops/).** Do zarządzania zespołem poza tym małym laboratorium użyj [kursu wdrażania współpracy AI](/ai-collaboration-course-start/).

**Nawigacja kursu:** [Wstecz: weryfikacja wyników](/articles/effective-ai-output-verification/), [Plan kursu](/effective-ai-course-start/).
