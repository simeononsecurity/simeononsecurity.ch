---
title: "Jedno źródło, wiele narzędzi: framework współpracy AI dla mieszanych zespołów"
date: 2026-10-01
lastmod: 2026-11-23
toc: true
draft: false
description: "Zbuduj wspólny system współpracy z AI, określając **właścicieli źródeł**, wersjonowanie kontekstu, trwały przegląd zmian oraz wybór między mapą projektu a RAG."
genre: ["Sztuczna inteligencja", "Zarządzanie wiedzą", "Inżynieria oprogramowania", "Współpraca zespołowa"]
tags: ["framework współpracy AI", "mieszane zespoły", "źródło prawdy", "agenci AI", "AGENTS.md", "CLAUDE.md", "reguły Cline", "Claude Code", "Codex", "ChatGPT", "Copilot", "Cowork", "generowanie wspomagane wyszukiwaniem", "RAG", "Model Context Protocol", "mapa projektu", "manifest kontekstu", "zarządzanie wiedzą", "dryf dokumentacji", "zatwierdzenie przez człowieka", "rejestr decyzji", "przekazanie agentowi", "wersjonowanie polityk", "Git worktrees", "bramki pull requestów"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustracja przedstawiająca grupę specjalistów współpracujących przy zadaniach z zakresu cyberbezpieczeństwa"
coverCaption: ""
---

**Dwie osoby zadają dwóm narzędziom AI to samo pytanie:** jak długo usługa ma przechowywać eksport? W tym przykładzie agent IDE programisty odpowiada: siedem dni, na podstawie pliku README. Asystent czatu kierownika operacyjnego odpowiada: trzydzieści dni, na podstawie strony wiki. Oba odpowiedzi brzmią pewnie. Każde narzędzie odczytało inną kopię prawdy.

**Problemem jest własność źródła**, a nie jakość promptu. Wymaganie w wiki zmieniło się w zeszłym tygodniu, lecz nikt nie zaktualizował README. Programista prosi agenta o poprawienie zadania usuwającego eksporty. Agent kieruje się starszym dokumentem i przygotowuje schludną poprawkę, która przywraca błędne działanie. Recenzenci analizują kod, nie widząc wersji wymagania, na której oparto odpowiedź.

**Przypisz każdy fakt do jednego miejsca.** Niech każde narzędzie odczytuje to źródło, a każdą trwałą zmianę zatwierdza człowiek. Repozytorium, wiki i tracker nadal mają różne zadania. Określ ich autorytet, właścicieli i **wspólną procedurę** przenoszenia informacji między systemami.

**Ten poradnik przedstawia model do wdrożenia w tym tygodniu**, z RAG lub bez niego. Zacznij od mapy projektu, wersjonowanych instrukcji, rejestrów dowodów i recenzowanych propozycji. Infrastrukturę wyszukiwania dodaj dopiero wtedy, gdy wymaga tego problem z odnajdywaniem informacji.

**Pierwszym rezultatem powinien być rejestr źródeł**, a nie konektor. Dla każdego typu faktów zapisz **autorytatywne źródło**, właściciela, bieżącą rewizję i osobę zatwierdzającą zmiany.

## Najważniejsze wnioski

- **Przypisz autorytet do rodzaju informacji**, zamiast zmuszać wszystko do jednego narzędzia.
- **Traktuj pamięć i indeksy wyszukiwania jako pamięci podręczne**, nigdy jako niezależne źródła polityk.
- **Dołączaj wersje źródeł do propozycji**, aby recenzenci wiedzieli, jakie fakty uzasadniają zmianę.
- **Wymuszaj zatwierdzanie poza promptami**, przez kontrolę dostępu i **wymagane bramki przeglądu**.
- **Udostępniaj procedurę różnym narzędziom**, dopasowując jej realizację do każdego interfejsu.

## Zanim zaczniesz

**Wymagania:** wybierz projekt pilotażowy z repozytorium, wiki lub systemem dokumentów, trackerem i właścicielami gotowymi recenzować zmiany. Jeśli zespół nie ma wiki, użyj wersjonowanego magazynu dokumentów. Model własności pozostaje bez zmian.

**Szacowany czas:** przeznacz od dwóch do czterech godzin na początkową mapę i szablony, a potem tydzień na pilotaż. **Trudność:** umiarkowana. Uzgodnienie autorytetu jest trudniejsze niż instalacja kolejnego narzędzia AI.

**Zakres:** to proponowany model pracy zespołu. Zasady zatwierdzania i konwencje nazewnicze są zaleceniami, a nie domyślnym zachowaniem gwarantowanym przez Claude Code, Codex, Cline, Cowork, Copilot czy ChatGPT. Automatyczny spis treści powyżej prowadzi do każdego etapu wdrożenia.

## Różne narzędzia, rozdzielony kontekst

**Programiści i osoby nieprogramujące pracują nad wspólnym projektem**, ale korzystają z różnych interfejsów. Programista używa agenta w IDE lub terminalu. Właściciel produktu pracuje w projekcie czatu. Zespół operacyjny używa wiki i trackera. Dobieraj interfejs do zadania, a nie do dostępu do autorytatywnych faktów.

**Kontekst to materiał dostępny dla bieżącej odpowiedzi.** W każdej sesji sprawdź pliki repozytorium, przesłane dokumenty, historię czatu, zapisaną pamięć, wyniki konektorów i pobrane fragmenty. Sesje z różnymi dowodami nie muszą dać zgodnych odpowiedzi, nawet przy identycznym pytaniu.

| Problem | Co widzisz |
|---|---|
| **Dryf dokumentacji** | README powtarza nieaktualne wymaganie |
| **Awans podsumowania** | Podsumowanie sesji staje się dowodem bez pierwotnego źródła |
| **Nakładające się zmiany** | Dwa agenty zastępują tę samą stronę na podstawie różnych wersji |
| **Utracone decyzje** | Ustalenie ze spotkania nie trafia do rejestru decyzji |
| **Brak pochodzenia** | Wiarygodna odpowiedź nie podaje wersji strony ani commita |

**Przykład z okresem przechowywania pokazuje różnicę.** Wiki opisuje zatwierdzone zachowanie docelowe. Kod opisuje zachowanie wdrożone. Żadne z nich nie powinno po cichu przepisywać drugiego. Zapisz rozbieżność i zapytaj wskazanego właściciela, czy należy zmienić implementację, czy wymaganie.

> **Najważniejsze:** ustalenie autorytetu poprzedza wybór narzędzia AI. Zacznij od poniższych pojęć.

### Panel boczny: pięć wspólnych pojęć

| Pojęcie | Znaczenie w tym modelu |
|---|---|
| **Źródło** | Wskazany autorytatywny zapis dla typu informacji |
| **Pamięć podręczna** | Pochodna kopia używana dla szybkości lub wygody |
| **Propozycja** | Sugerowana zmiana oczekująca na zatwierdzenie właściciela |
| **Mapa projektu** | Indeks lokalizacji źródeł, identyfikatorów i właścicieli |
| **Manifest** | Zapis dokładnych dowodów wykorzystanych w odpowiedzi lub propozycji |

## Przypisz faktom jedno miejsce

**Jedno źródło oznacza jeden autorytet dla każdego faktu**, a nie **jedną bazę danych dla całej organizacji**. W pilotażu ustal poniższy podział. Zastąp przykładowe role rzeczywistymi właścicielami w zespole.

| Rodzaj informacji | System źródłowy | Właściciel | Kto zapisuje | Jak agenty odczytują |
|---|---|---|---|---|
| **Kod, testy, konfiguracja, schematy** | Repozytorium | Opiekun techniczny | Współtwórcy przez recenzowane PR-y | Pliki ze wskazanego commita |
| **Opublikowana dokumentacja i ADR-y** | Repozytorium | Właściciel techniczny | Współtwórcy przez ten sam PR | Wersjonowane pliki |
| **Wymagania** | Wiki | Właściciel produktu | Właściciel lub zatwierdzony publikujący | ID strony i rewizja |
| **Runbooki** | Wiki | Właściciel operacyjny | Zatwierdzony publikujący | ID strony i rewizja |
| **Polityka** | Wiki | Właściciel polityki | Zatwierdzony publikujący po recenzji | Strona kanoniczna i lokalny adapter |
| **Decyzje między zespołami** | Rejestr decyzji w wiki | Imiennie wskazany właściciel decyzji | Właściciel po zatwierdzeniu | ID decyzji i status |
| **Zadania i ustalenia** | Tracker | Właściciel zadania | Ludzie lub uprawniony kanał propozycji | Klucz i rewizja zgłoszenia |
| **Czaty, podsumowania, embeddingi** | Tylko pamięć podręczna | Opiekun sesji lub indeksu | Narzędzia i uczestnicy | Wyłącznie odnośnik, następnie kontrola źródła |

**Rekord decyzji architektonicznej (ADR)** należy umieścić przy kodzie, jeśli określa architekturę repozytorium. Decyzja między zespołami trafia do wspólnego rejestru. Powiąż rekordy, jeśli decyzja obejmuje oba zakresy. Nie utrzymuj dwóch niezależnych kopii statusu zatwierdzenia.

**Lokalne kopie polityk podlegają stronie kanonicznej.** Testy i schematy repozytorium są natomiast źródłami w ich własnym zakresie. O autorytecie nie decyduje lokalizacja. Decyduje mapa.

**Pamięć podręczna nigdy nie zastępuje źródła.** Jeśli podsumowanie podaje siedem dni, a zatwierdzone wymaganie trzydzieści, użyj wymagania dla zachowania docelowego. Zachowaj sprzeczne podsumowanie jako dowód dryfu, a nie konkurencyjną regułę. Następnie ustal ścieżkę zapisu.

## Z pamięci podręcznej w dół, propozycja w górę

**Agenty pobierają dowody do kontekstu sesji**, a potem przygotowują propozycje. Nie zatwierdzają samodzielnie trwałych faktów. Edycja gałęzi zadania lub złożenie wersji roboczej różni się od publikacji polityki, scalania kodu czy oznaczenia decyzji jako przyjętej.

```text
Źródło -> odczyt z kontrolą uprawnień -> kontekst sesji
Kontekst sesji -> propozycja + wersja bazowa -> przegląd właściciela
Zatwierdzenie właściciela -> kontrolowana publikacja -> rejestr zmian
Zmieniona wersja bazowa -> uzgodnienie propozycji -> ponowny przegląd
```

**Zapisz wersję bazową** przed prośbą o recenzję. Recenzent potrzebuje poprzedniej i proponowanej wartości, uzasadnienia, dowodów oraz dotkniętych systemów. Zatwierdzenie powinno dotyczyć konkretnej rewizji propozycji, a nie zmieniającego się wątku czatu.

```yaml
proposal_id: PROP-042
target: wiki:REQ-17
base_version: 8
change: "Przechowuj eksporty przez trzydzieści dni zamiast siedmiu."
evidence:
  - "decyzja:DEC-12 przyjęta"
affected_records:
  - "repo:export-service retention configuration"
  - "wiki:RUN-04 cleanup procedure"
owner_role: product-owner
status: awaiting-review
```

**Powyższe identyfikatory są przykładowe.** Dla każdej zatwierdzonej logicznej zmiany zapisz **jeden wiersz dziennika** ze wskazaniem ID propozycji, rekordów docelowych, poprzedniej i wynikowej wersji, zatwierdzającego, czasu oraz odnośnika do scalenia lub publikacji. Powiąż z wierszem zdarzenia audytowe systemów zamiast zastępować ich historię.

**Decyzja należy do ludzi.** Uprawniony publikujący lub ograniczona automatyzacja wdraża zatwierdzoną rewizję. Ogranicz uprawnienia zapisu. Same instrukcje nie rozdzielają tworzenia propozycji i publikowania. To samo rozróżnienie dotyczy pobierania informacji.

## Wspólny kontekst bez RAG

**Mapa projektu to pierwszy indeks wyszukiwania.** Prowadź jedną stronę na projekt z ID źródeł, lokalizacjami w repozytorium, kluczami trackera, zakresami autorytetu i właścicielami. Najpierw odczytaj mapę, a potem pobierz odpowiedni rekord po ID. Szukaj, gdy ID nie jest znane.

### Panel boczny: przykładowa mapa projektu

```yaml
project: export-service
map_id: MAP-01
policy:
  source_id: POL-01
  approved_version: 3
  owner_role: policy-owner
sources:
  requirements: {page_id: REQ-17, owner_role: product-owner}
  runbook: {page_id: RUN-04, owner_role: operations-owner}
  decisions: {register_id: DEC-REGISTER, owner_role: project-lead}
repository:
  key: export-service
  setup: README.md
  terms: CONTEXT.md
  decisions: docs/adr/
tracker:
  project_key: EXP
  active_task: EXP-42
```

**Bezpośrednie konektory ograniczają ręczne kopiowanie.** Model Context Protocol (MCP) to protokół integracyjny udostępniający narzędzia i kontekst aplikacjom AI. Korzystaj z zatwierdzonych **konektorów wiki**, trackera i repozytorium, jeśli są dostępne. Precyzyjne pobranie ogranicza nieistotne wyniki, ale nie zastępuje autoryzacji ani kontroli aktualności. Przy wyborze uprawnień konektora zastosuj wskazówki bezpieczeństwa MCP wymienione w referencjach.

**Dokładne pobieranie wymaga niewielkiej konfiguracji.** Zapewnia cytowalne dowody bez bazy wektorowej. Ma też jasne ograniczenia: ktoś musi utrzymywać mapę, szerokie pytania wymagają dodatkowego wyszukiwania, a duże strony zajmują miejsce w sesji. Pobieraj właściwą sekcję wraz z sąsiednimi ograniczeniami zamiast wklejać cały podręcznik.

**Praca offline korzysta z jawnych migawek.** Zapisz wyeksportowaną rewizję i oznacz odpowiedzi jako oparte na migawce. Nie publikuj zmian, dopóki uprawniona osoba lub konektor nie sprawdzi bieżącego źródła. Następnie pokaż tę samą politykę w każdym interfejsie.

## Jedna polityka, różne adaptery

**Utrzymuj jedną wspólną politykę**, a potem udostępniaj krótkie adaptery dla narzędzi. Umieść zatwierdzoną wersję polityki w pierwszym wierszu każdego adaptera lub skopiowanego zestawu instrukcji. Dodaj ID źródła i sprawdzoną **lokalną migawkę** dla sesji bez konektora.

**Każde narzędzie ładuje instrukcje inaczej.** Codex opisuje warstwowe wyszukiwanie `AGENTS.md`. Claude Code opisuje `CLAUDE.md`, importy i pamięć projektu. Cline opisuje `.clinerules/` i sterowanie regułami. Skorzystaj z oficjalnej dokumentacji w referencjach. Sprawdź załadowane instrukcje w swojej wersji narzędzia, zamiast zakładać, że nazwy plików działają identycznie.

### Panel boczny: przykładowy nagłówek AGENTS.md

```markdown
Wersja polityki: v3 | Źródło: wiki:POL-01 | Stan: zatwierdzona

# Instrukcje projektu

Przed rozpoczęciem zadania przeczytaj mapę projektu MAP-01.
Załaduj docs/policy-snapshot.md i zapisz rewizję źródłową.
Traktuj pamięć czatu i fragmenty wyszukiwania jako pamięć podręczną.
Dołącz rewizje źródeł do każdej propozycji faktów.
Używaj jednej gałęzi zadania i jednego worktree na zadanie programistyczne.
Nie publikuj polityki, nie zatwierdzaj decyzji ani nie scalaj własnego PR.
Zatrzymaj pracę przy nierozstrzygniętych konfliktach źródeł lub nakładających się zapisach.
Wymagane kontrole: testy, recenzja dokumentacji i aktualność polityki.
Właściciele: opiekun inżynierii, właściciel produktu, właściciel polityki.
```

**Instrukcje projektu czatu dostają ten sam nagłówek i procedurę.** Osoba nieprogramująca otrzymuje migawkę polityki i mapę projektu przez zatwierdzone przesłane pliki lub konektory. Jeśli interfejs nie ma dostępu na żywo, ktoś dostarcza eksport z wersją i zapisuje to ograniczenie.

**Etykieta wersji to deklaracja, nie dowód identycznej treści.** Twórz adaptery z zatwierdzonej migawki albo porównuj ich fragmenty polityki z zapisanym skrótem. Osobno recenzuj wyjątki specyficzne dla adaptera. Podczas pilota sprawdź wyłączone reguły, zagnieżdżone nadpisania i instrukcje osobiste. Następnie zapisz dowody wykorzystane przez każde zadanie.

## Zapisz manifest kontekstu

**Manifest kontekstu wyjaśnia, jakie dowody wspierają odpowiedź.** Zapisz ID i rewizje stron, klucze zgłoszeń wraz z rewizją lub czasem aktualizacji oraz pełne ID commitów repozytorium. Dodaj **czas pobrania** i odpowiednie sekcje. Oznacz niedostępne rekordy zamiast zastępować je zapamiętanym podsumowaniem.

```yaml
task: EXP-42
policy: {page_id: POL-01, version: 3}
wiki:
  - {page_id: REQ-17, version: 8, section: export-retention}
tracker:
  - {issue_key: EXP-42, revision: 5}
repository:
  commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  files: [README.md, config/retention.yaml]
limits:
  - "Runbook nie został pobrany. Nie zaproponowano jego zmiany."
```

**Wartość commita jest sztuczna.** W prawdziwym manifeście zastąp ją sprawdzonym commitem. Dodaj czas pobrania podczas odczytu. Rekord sporządzony przed inspekcją jest listą kontrolną, a nie dowodem.

**Cytaty wspierają weryfikację**, nie automatyczne zaufanie. Każde ważne twierdzenie połącz z odpowiednim rekordem i sekcją. Jeśli źródła są sprzeczne, zachowaj oba w manifeście i zgłoś nierozstrzygniętą różnicę. Nie wybieraj najnowszego znacznika czasu bez sprawdzenia zakresu i zatwierdzenia. Ta dyscyplina dowodowa dotyczy też wyszukiwania semantycznego.

## Wspólny kontekst z RAG

**Retrieval-augmented generation (RAG)** dostarcza modelowi pobrany materiał podczas tworzenia odpowiedzi. Indeks semantyczny pomaga znaleźć istotne fragmenty, nawet gdy pytanie używa innych słów. Omówienie RAG firmy Microsoft opisuje ugruntowanie, ograniczenia wyszukiwania i kontrolę dostępu. Oficjalne źródło znajduje się w referencjach.

**Używaj RAG do odkrywania informacji w większych zbiorach**, takich jak starsza dokumentacja, notatki ze spotkań i transkrypcje. Oznaczaj klasy dokumentów i statusy zatwierdzenia. Transkrypcja z oryginalnego nagrania jest źródłem tego, co powiedzieli uczestnicy, a nie autorytetem dla zatwierdzonych wymagań. Nie zamieniaj rozmowy w politykę przez indeksowanie.

| Reguła indeksu | Wymagane zachowanie |
|---|---|
| **Pobieraj źródła, nie pamięci podręczne** | Wyklucz generowane podsumowania i nieśledzone kopie lokalne |
| **Zachowuj pochodzenie** | Dla każdego fragmentu przechowuj ID źródła, rewizję, sekcję i status dokumentu |
| **Odświeżaj po zmianach** | Ponownie indeksuj edycje i unieważniaj nieaktualne fragmenty |
| **Uwzględniaj zmiany dostępu** | Aktualizuj uprawnienia i usuwaj treści wycofane lub usunięte |
| **Zwracaj cytaty** | Pokazuj odnośniki do rekordów obok pobranego tekstu |
| **Sprawdzaj bieżący rekord** | Pobierz aktualne dowody przed propozycją ważnego działania |

**Pobrany fragment działa w tym modelu jak wskaźnik.** Jego treść pomaga znaleźć dowody. Bieżące źródło potwierdza aktualne brzmienie, zatwierdzenie, wyjątki i dostęp. Jeśli pobranie na żywo się nie powiedzie, oznacz migawkę i przerwij ważne działanie. To reguła zarządzania, nie twierdzenie o każdej implementacji RAG.

**Nieaktualne embeddingi i brak kontekstu stwarzają odrębne ryzyka.** Stary fragment nie uwzględnia rewizji. Aktualny fragment nadal może wprowadzić w błąd, jeśli wyjątek znajduje się w następnej sekcji. Zachowaj nagłówki i pobieraj sąsiednie ograniczenia przed oceną wymagania.

**Wycieki uprawnień wymagają osobnego testu.** Wymuś autoryzację przed zwróceniem fragmentów modelowi, nie dopiero po wygenerowaniu odpowiedzi. Sprawdzaj poufne treści przed indeksowaniem lub zewnętrznym embeddingiem. Uwzględnij kopie tekstu w logach, żądaniach modelu i śladach wyszukiwania. Lokalny model nie czyni zdalnego konektora lokalnym. Te kontrole pomagają zdecydować, czy RAG należy do pilota.

## Wybierz mapę, RAG albo oba rozwiązania

**Dopasuj wyszukiwanie do pytania.** Znane ID wymagania przemawia za bezpośrednim dostępem. Otwarte pytanie o rozproszone materiały historyczne przemawia za wyszukiwaniem. Zacznij od mapy, chyba że problem z odkrywaniem informacji został już zmierzony.

### Panel boczny: RAG czy nie?

```text
Czy zadania zwykle wskazują projekt, stronę, zgłoszenie lub plik?
  Tak -> Czy bezpośrednie pobieranie wystarczy w pilotażu?
           Tak -> TYLKO MAPA
           Nie -> HYBRYDA: mapa dla znanych ID, RAG do odkrywania
  Nie -> Czy dowody są rozproszone w dużym zbiorze?
           Nie -> TYLKO MAPA oraz wbudowane wyszukiwanie
           Tak -> Czy praca jest eksploracyjna i tylko do odczytu?
                    Tak -> TYLKO RAG do odkrywania
                    Nie -> HYBRYDA z kontrolą źródeł na żywo

Każda opcja zachowuje właścicieli, autoryzację i pochodzenie.
Odkrywanie przez RAG nadal sprawdza źródła przed trwałym działaniem.
```

**RAG-only opisuje interfejs wyszukiwania**, a nie zwolnienie z zasad. Używaj go do ograniczonego zbioru eksploracyjnego, w którym nadal da się sprawdzić bezpośrednie źródło. To słaby wybór przy zmianach opartych na znanym ID i wymagających dokładnej kontroli wersji.

**Model hybrydowy oddziela odkrywanie od weryfikacji.** Mapa obsługuje znane zapytania. RAG lokalizuje nieznane rekordy. RAG odpowiada „gdzie”, źródło odpowiada „co”. W przykładzie retencji pobierz bezpośrednio `REQ-17`. Dla pytania „które starsze decyzje o eksportach wyjaśniają ten limit?” przeszukaj rejestr i pobierz każdą właściwą decyzję. Teraz zastosuj część dotyczącą repozytorium.

## Informacje w repozytorium

**Wiedza repozytorium zmienia się wraz z implementacją.** Utrzymuj zwięzłą strukturę, aby agent i recenzent wiedzieli, gdzie szukać.

| Plik lub katalog | Odpowiedzialność |
|---|---|
| **`CONTEXT.md`** | Pojęcia projektu i linki do autorytatywnych rekordów |
| **`docs/adr/`** | Przyjęte decyzje architektoniczne repozytorium |
| **`docs/design/`** | Zatwierdzone opisy działania systemu |
| **`docs/plans/`** | Proponowane plany implementacji z jawnym statusem |
| **`AGENTS.md`** | Bramki recenzji, granice i role właścicieli |
| **`README.md`** | Konfiguracja i punkty wejścia, nie duplikaty wymagań |

**Stosuj zasadę tego samego PR:** zmieniaj kod i powiązaną dokumentację repozytorium razem. Jeśli aktualizacja bazy wiedzy nie jest potrzebna, wymagaj pisemnego wyjątku w opisie PR albo uzgodnionym miejscu na trailer commita.

```text
KB-Update: none (powód: refaktoryzacja wewnętrzna zachowuje udokumentowane zachowanie)
```

**Pipeline wymusza deklarację.** Wymagana kontrola odrzuca zmiany zachowania bez aktualizacji dokumentacji lub wyjątku. Człowiek odpowiedzialny za dokumentację recenzuje wyjątek. Kontrola oparta na ścieżkach wskazuje kandydackie zmiany, ale nie dowodzi semantycznej kompletności. Wymagaj kontroli i recenzji przez ochronę gałęzi lub równoważny mechanizm scalania.

**Bramka, której nie ma w pipeline, nie jest bramką.** Sama wzmianka o „recenzji dokumentacji” w pliku instrukcji to tylko wskazówka. Podczas pilota prześlij celowo niekompletny PR i sprawdź, czy scalanie pozostaje zablokowane.

**Używaj jednego zadania, jednej gałęzi i jednego worktree.** Oficjalna dokumentacja Git opisuje odrębne katalogi robocze z własnym sprawdzonym stanem. Worktrees ograniczają lokalne kolizje edycji, ale nie zapobiegają zmianom tego samego pliku w dwóch gałęziach ani równoległym edycjom strony wiki przez dwa agenty.

**Nigdy nie commituj bezpośrednio do gałęzi domyślnej**, niezależnie od tego, czy nazywa się `main`, `master` czy inaczej. Zgłoś w trackerze różnice między wymaganiem a kodem. Dołącz sprzeczne rekordy i pozwól ich właścicielom ustalić zamierzone zachowanie przed zmianą którejkolwiek strony. Stosuj równoważne kontrole poza Git.

## Informacje **poza repozytorium**

**Wiki potrzebuje standardu dokumentacji.** Każda autorytatywna strona zawiera cel, status, właściciela, rewizję, termin przeglądu i powiązane ID źródeł. Propozycje umieszczaj w sekcji szkiców z jasną etykietą braku autorytetu. Nie mieszaj proponowanego brzmienia z zatwierdzoną stroną wymagań.

**Bezpieczne aktualizacje przebiegają według stałej sekwencji:**

1. **Odczytaj ponownie** bieżącą stronę i sąsiednie ograniczenia.
2. **Porównaj** jej wersję z wersją bazową propozycji.
3. **Rozstrzygnij** zmiany pośrednie i uzyskaj ponowne zatwierdzenie zmienionego brzmienia.
4. **Zapisz** zatwierdzoną rewizję z warunkiem oczekiwanej wersji.
5. **Zweryfikuj** zapisaną stronę i dodaj odnośnik do dziennika zmian.

**Samo ponowne odczytanie nie eliminuje wyścigów.** Jeśli to możliwe, użyj mechanizmu aktualizacji warunkowej. Bez niego publikację szereguje jeden właściciel, który weryfikuje wynik. Zatrzymaj się, jeśli inny autor zmieni bazę w trakcie przeglądu.

**Zakaz usuwania dotyczy przepływów pracy agentów.** Agenty proponują archiwizację lub usunięcie. Uprawnieni ludzie stosują procedury retencji i kasowania. Nie interpretuj tej reguły jako zgody na bezterminowe przechowywanie poufnych informacji.

**Ustalenia w trackerze zawierają dowody**, nie tylko wnioski. Zapisz obserwację, dokładne polecenie lub metodę inspekcji, sprawdzony commit, oczekiwane i rzeczywiste zachowanie oraz kryteria akceptacji. Usuń sekrety i poufne dane z załączników. Sugerowane polecenia oznacz jako niewykonane, dopóki ktoś ich nie uruchomi.

```text
Ustalenie: implementacja retencji nie zgadza się z zatwierdzonym wymaganiem
Dowody: REQ-17 v8 oraz sprawdzony config/retention.yaml
Polecenie inspekcji: git show HEAD:config/retention.yaml
Commit: pełne sprawdzone ID commita zapisano w manifeście
Akceptacja: zatwierdzony czas odpowiada kodowi, testom i runbookowi
Status: oczekuje na recenzję właścicieli produktu i inżynierii
```

**Przykład to szablon ustalenia**, a nie wynik pomiaru. Uzupełnij go na podstawie rzeczywistej inspekcji. Połącz aktualizację wiki i dowody trackera przez ID propozycji.

**Rejestr decyzji oddziela reguły od uzasadnień.** Zapisz pytanie, opcje, rekomendację, kompromisy, właściciela, **status zatwierdzenia** i odnośnik do wynikowej reguły. Agenty proponują. Ludzie decydują. Zatwierdzone reguły trafiają do polityki i procedur. Uzasadnienie zostaje w rejestrze.

**Utrwalaj ważne fakty ze spotkań i czatów.** Złóż propozycję z dowodami źródłowymi i uzyskaj zatwierdzenie. Do publikacji oznacz ustalenie jako tymczasowe. Następnie połącz zatwierdzone zachowanie w repozytorium i wiki.

## Połącz oba systemy

**Synchronizacja po scaleniu przenosi zmiany implementacji na zewnątrz.** Utwórz zadanie aktualizacji wiki powiązane ze scalonym commitem, zatwierdzonym wymaganiem i dotkniętym runbookiem. Agent przygotowuje szkic. Właściciel wiki sprawdza bieżącą stronę i zatwierdza publikację. Zamknij zadanie dopiero po weryfikacji zapisanej rewizji.

**Aktualność polityki to osobny audyt.** Porównuj każdy adapter repozytorium i kopię instrukcji w czacie z kanoniczną zatwierdzoną wersją. Polityka `v3` znajduje się pod `POL-01`. Każdy `AGENTS.md` wymienia `v3` w pierwszym wierszu. Audyt wykrywa `v2`, brakujące etykiety i różnice treści mimo zgodnych etykiet.

| Kontrola | Dowód ukończenia |
|---|---|
| **Aktualność polityki** | Kanoniczna wersja i porównanie skrótu adaptera |
| **Uzgodnienie wymagań** | Rewizja wymagania porównana z kodem i testami |
| **Synchronizacja po scaleniu** | Scalony commit połączony z opublikowaną rewizją wiki |
| **Rozwiązanie konfliktu** | Decyzja właściciela połączona z oboma rekordami |

**Uzgadniaj na harmonogramie lub przy PR.** Tygodniowy audyt pasuje do pilota. PR zmieniający zachowanie wymaga sprawdzenia wymagania przed scaleniem. Dobierz częstotliwość do kosztu dryfu i zapisuj termin ostatniej udanej kontroli.

**Zmiana z siedmiu na trzydzieści dni ma kilka punktów kontrolnych:** produkt zatwierdza wymaganie, inżynieria aktualizuje konfigurację i testy, recenzenci scalają PR, a zespół operacyjny publikuje zmianę runbooka. Jeden wiersz dziennika łączy wynikowe rekordy. Nieudana synchronizacja wiki pozostaje widoczna i nie ginie za udanym scaleniem. Wspólne przekazania utrzymują ten porządek między narzędziami.

## Jedna procedura, każde narzędzie

**Pakuj powtarzalne kroki jako umiejętności lub prompty** z wersjonowanym ID procedury. Udostępniaj kontrakt, nie zakładaj uniwersalnego formatu pliku. Każdy adapter wykorzystuje obsługiwany mechanizm ładowania lub wywoływania.

| Procedura | Wymagany wynik |
|---|---|
| **Rozpoczęcie zadania** | Właściciel, zakres, wersja polityki, manifest źródeł, rezerwacja zapisu |
| **Lint dokumentacji** | Brakujące metadane, zduplikowany autorytet, uszkodzone odnośniki do źródeł |
| **Kontrola wiedzy** | Różnice między wymaganiem a kodem z potwierdzającymi rewizjami |
| **Przekazanie** | Bieżące dowody, propozycje, ukończone kontrole, nierozstrzygnięte pytania |

**Osoby nieprogramujące pracują bez Git.** Pobierają dozwolone źródła w projektach czatu, wypełniają ten sam szablon propozycji i przesyłają go właścicielowi jako stronę roboczą lub zadanie trackera. Nie potrzebują checkoutu repozytorium, aby poprosić o korektę wymagania.

**Programiści używają plików repozytorium i bramek PR.** Łączą zatwierdzoną propozycję z PR, zapisują sprawdzane commity i uruchamiają wymagane kontrole. Obie grupy przekazują tę samą strukturę dowodów.

```yaml
handoff:
  task: EXP-42
  policy_version: 3
  manifest: "Attached source IDs, revisions, and inspected commit"
  completed: [requirement-review]
  proposals: [PROP-042]
  pending: [implementation-review, runbook-publication]
  reservations: ["RUN-04 publication assigned to operations-owner"]
  unresolved: []
  next_owner_role: engineering-maintainer
```

**Przekazanie nadal jest pamięcią podręczną.** Następna osoba przed działaniem ponownie odczytuje źródła i zapisuje nowe rewizje. Nie uznawaj pozycji „ukończono” za dowód bez sprawdzenia powiązanego zatwierdzenia lub testu. Przed każdym zapisem zastosuj poniższe zabezpieczenia.

## Zabezpieczenia przed każdym zapisem

**Sprawdź dane, zanim opuszczą system źródłowy.** Zweryfikuj klasyfikację, uprawnienia konektora, dozwolone miejsca docelowe, przetwarzanie przez dostawcę modelu i logowanie. Wysyłaj minimum potrzebnej treści. Nie umieszczaj ograniczonych rekordów w nieuprawnionych projektach czatu ani usługach embeddingowych.

**Pobrany tekst jest dowodem, nie kanałem instrukcji.** Strona wiki lub odpowiedź narzędzia nakazująca agentowi zignorowanie polityki nie zmienia jej autorytetu. Oddzielnie oceniaj instrukcje pochodzące z treści i zatwierdzoną politykę operacyjną. Podczas pobierania ogranicz konektory do odczytu i oddziel poświadczenia publikacyjne od dostępu sesji.

**Przypisz każdej stronie lub plikowi jednego aktywnego właściciela.** Zarejestruj rezerwację w trackerze wraz z zakresem i terminem wygaśnięcia. Przed zapisem odczytaj ponownie i użyj kontroli wersji. Osobne worktrees pomagają izolować lokalne zmiany, a rezerwacje i zapisy warunkowe chronią współdzielone rekordy.

| Powód, by zatrzymać się i zapytać | Wymagana reakcja |
|---|---|
| **Źródła są sprzeczne, brak właściciela** | Wstrzymaj pracę i poproś o przypisanie autorytetu |
| **Inne zadanie rezerwuje cel** | Uzgodnij własność przed edycją |
| **Wersja bazowa się zmieniła** | Uzgodnij propozycję i poproś o ponowne zatwierdzenie |
| **Ważne twierdzenie nie ma dowodów** | Oznacz jako niezweryfikowane i poproś o źródło |
| **Niejasne przetwarzanie danych** | Zostaw treść w systemie źródłowym |
| **Brak dostępu do źródła na żywo** | Zapisz ograniczenia migawki i wstrzymaj trwałe działanie |

**Prompty nie są kontrolami bezpieczeństwa.** Testuj odmowę dostępu, chronione gałęzie, odrzucanie nieaktualnej bazy i własność zapisu poza modelem. **Poprawna demonstracja** nie wystarcza, jeśli konto nadal ma nieograniczone uprawnienia publikacji. Na podstawie tych testów zdecyduj, czy pilotaż jest gotowy.

## Najpierw pilotaż

**Rozpocznij od szkicu frameworku.** Uruchom pilotaż dla jednego projektu z programistą, osobą nieprogramującą i wskazanymi właścicielami źródeł. Zadaj dwóm narzędziom to samo pytanie o znanym ID, a następnie przeprowadź ćwiczenie z celowo sprzecznymi źródłami. Oceniaj manifesty i propozycje, nie płynność tekstu.

**Oczekiwane rozumowanie:** obie osoby wskazują bieżące zatwierdzone wymaganie i osobno opisują sprawdzoną implementację. Jeśli się różnią, najpierw porównaj wpisy w manifestach. To proponowane ćwiczenie, a nie zaobserwowany benchmark.

| Metryka | Definicja |
|---|---|
| **Wskaźnik cytowań** | Twierdzenia wspierane przez źródła podzielone przez ważne twierdzenia faktyczne w próbie |
| **Cotygodniowe ustalenia o dryfie** | Potwierdzone rozbieżności autorytetu lub wersji pogrupowane według typu źródła |
| **Czas obsługi propozycji** | Mediana od gotowości propozycji do recenzji do zapisanej decyzji |
| **Poprawki po nieaktualnym kontekście** | Ponownie otwarte zadania wynikające z nieaktualnych lub niezweryfikowanych dowodów |

**Najpierw zmierz punkt odniesienia.** Więcej ustaleń o dryfie w pierwszym tygodniu może oznaczać lepsze wykrywanie, nie gorszą dokumentację. Oprócz liczby śledź powtarzalność i czas rozwiązania. Wrażliwe dowody oceniaj bez kopiowania ich do eksportów analitycznych.

**Podczas wdrożenia przygotuj przykładowe repozytorium.** Dodaj syntetyczną mapę, adaptery polityk, manifesty, szablony propozycji, wyjątki dokumentacyjne i wykonywalne kontrole recenzji. Użyj fikcyjnych rekordów wiki i trackera, bez poświadczeń produkcyjnych. Pokaż odmowę publikacji, odrzucenie zmienionej bazy, dryf wersji polityki i udane przekazanie.

**Repozytorium szablonów jest rezultatem wdrożenia**, a nie zasobem dołączonym do artykułu. Rozszerz model operacyjny po przejrzeniu wyników pilota przez kierownictwo i właścicieli źródeł. Zapisz wyjątki i nierozwiązane awarie w rejestrze decyzji. Przed rozszerzeniem napraw przewidywalne problemy opisane niżej.

## Rozwiązywanie problemów ze wspólnym kontekstem

| Objaw | Pierwsza naprawa |
|---|---|
| **Dwa narzędzia odpowiadają inaczej** | Porównaj ID źródeł, rewizje, zakres i status zatwierdzenia |
| **Instrukcje wydają się aktualne, zachowanie jest inne** | Sprawdź załadowane adaptery, przełączniki reguł i lokalne nadpisania |
| **RAG zwraca stare wymagania** | Sprawdź odświeżanie indeksu i pobierz bieżącą stronę |
| **Edycja wiki kasuje inną zmianę** | Wymagaj zapisów warunkowych lub szeregowania publikacji |
| **Kontrole dokumentacji przechodzą ze starą treścią** | Dodaj recenzję właściciela i uzgadnianie wymagań |
| **Decyzje pozostają w czacie** | Przypisz obsługę propozycji i właściciela rejestru |

**Napraw ścieżkę dowodów, zanim przepiszesz prompt.** Następnie ponownie uruchom nieudany przypadek pilotażowy i zapisz wynik. Skorzystaj z checklisty, aby naprawiony proces powtarzać co tydzień.

## Dziesięć kroków na ten tydzień

1. **Wybierz jeden projekt pilotażowy** oraz uczestniczące osoby i narzędzia.
2. **Przypisz każdemu typowi informacji miejsce i właściciela.**
3. **Opublikuj mapę projektu** z ID źródeł i zakresami autorytetu.
4. **Przygotuj wspólną politykę** i uzyskaj recenzję właściciela.
5. **Wersjonuj każdy adapter instrukcji** w pierwszym wierszu i sprawdź, czy się ładuje.
6. **Wymagaj manifestu kontekstu** dla ważnych odpowiedzi faktycznych i propozycji.
7. **Utwórz ścieżkę przyjmowania propozycji** z wersjami bazowymi i wskazanymi zatwierdzającymi.
8. **Wymuś kontrolę zapisu i regułę dokumentacji w tym samym PR.**
9. **Przetestuj dryf, konflikt i przekazanie** na syntetycznych rekordach.
10. **Przejrzyj metryki pilota** i zatwierdź kolejny etap wdrożenia.

**Przypisz każdy fakt do jednego miejsca, każ narzędziom odczytywać to źródło i przekazuj każdą trwałą zmianę człowiekowi.**

## Źródła i dalsze kroki

**Oficjalna dokumentacja opisuje komponenty techniczne**, nie organizacyjne reguły tego frameworku. Podczas pilota sprawdź działanie zainstalowanych narzędzi i uprawnienia konektorów.

- **Instrukcje Codex:** [Instrukcje niestandardowe z AGENTS.md](https://developers.openai.com/codex/guides/agents-md), o wyszukiwaniu i weryfikowaniu instrukcji.
- **Instrukcje Claude Code:** [Jak Claude zapamiętuje projekt](https://code.claude.com/docs/en/memory), o instrukcjach projektu i pamięci.
- **Instrukcje Cline:** [Reguły](https://docs.cline.bot/customization/cline-rules), o regułach obszaru roboczego i sterowaniu aktywacją.
- **Projekt wyszukiwania:** [RAG w Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview), o ugruntowaniu, ograniczeniach wyszukiwania i bezpieczeństwie.
- **Bezpieczeństwo konektorów:** [Najlepsze praktyki bezpieczeństwa MCP](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices), o autoryzacji i ryzykach konektorów.
- **Izolacja worktrees:** [Dokumentacja Git worktree](https://git-scm.com/docs/git-worktree), o oddzielnych katalogach roboczych i współdzielonym stanie repozytorium.

**Przy planowaniu lokalnego wnioskowania** przeczytaj [Przewodnik po kontekście GPU dla lokalnej AI](/articles/local-ai-model-gpu-context-guide/). Pojemność sprzętu i zarządzanie wspólnymi źródłami rozwiązują różne problemy. Większe okno kontekstu nie naprawi sprzecznego autorytetu.

{{< centerbutton href="/articles/local-ai-model-gpu-context-guide/" >}}
  Przeczytaj przewodnik po kontekście lokalnej AI
{{< /centerbutton >}}
