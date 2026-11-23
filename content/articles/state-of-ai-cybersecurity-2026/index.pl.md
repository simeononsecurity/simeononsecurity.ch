---
title: "Cyberbezpieczeństwo AI w 2026 roku: szybkie wdrażanie, późniejsze zabezpieczanie"
draft: false
toc: true
date: 2026-06-26
lastmod: 2026-11-23
description: "Ocena wdrażania AI w cyberbezpieczeństwie, luk operacyjnych, aktualnych wytycznych i praktycznych zabezpieczeń dla organizacji w 2026 roku."
tags: ["bezpieczeństwo AI", "cyberbezpieczeństwo AI 2026", "wstrzykiwanie promptów", "agenci AI", "bezpieczeństwo MCP", "łańcuch dostaw AI", "shadow AI", "red teaming AI", "bezpieczeństwo LLM", "obserwowalność AI", "agentowa AI", "zagrożenia AI", "ataki AI", "bezpieczeństwo modeli", "zarządzanie AI", "NIST AI 600-1", "OWASP LLM", "MITRE ATLAS", "reagowanie na incydenty AI", "bezpieczeństwo AI w przedsiębiorstwie", "tożsamość AI", "zatruwanie kontekstu", "zatruwanie narzędzi", "autoryzacja AI"]
cover: "/img/cover/state-of-ai-cybersecurity-2026.webp"
coverAlt: "Ilustracja połączonych systemów AI przedstawionych jako świecące węzły na ciemnym tle. Jasne linie pokazują połączenia, a cienie wskazują luki w zabezpieczeniach wokół niektórych węzłów."
coverCaption: ""
---

W latach 2023, 2024 i 2025 organizacje wdrażały systemy AI w tempie, za którym nie nadążały wytyczne obronne, narzędzia bezpieczeństwa ani praktyki operacyjne. **W 2026 roku skutkiem jest rozległa, słabo monitorowana powierzchnia ataku połączona z rzeczywistymi systemami biznesowymi, podczas gdy mechanizmy obronne dopiero powstają.**

Chcę precyzyjnie wyjaśnić, co budzi moje obawy i dlaczego. To nie jest ogólne ostrzeżenie przed ryzykiem AI. Opisuję rzeczywistą powierzchnię ataku, udokumentowane luki oraz działania, które powinny podjąć organizacje.

## Dlaczego ta luka istnieje

Bezpieczeństwo tradycyjnego oprogramowania dojrzewało przez około trzy dekady. Dziesięciolecia doświadczeń w reagowaniu na incydenty, badania luk, tworzenia narzędzi i zdobywanej z trudem wiedzy operacyjnej doprowadziły do powstania struktur, produktów i praktyk, na których opierają się współczesne programy bezpieczeństwa.

**Generatywna AI w przedsiębiorstwach osiągnęła miliony wdrożeń produkcyjnych w ciągu mniej więcej dwóch lat.**

Dyscypliny, dzięki którym działa bezpieczeństwo oprogramowania, takie jak modelowanie zagrożeń dla konkretnych architektur, wzorce bezpiecznego wdrażania, dojrzałe procedury reagowania na incydenty oraz sprawdzone praktyki audytu i obserwowalności, nie zdążyły się rozwinąć przed wdrożeniem AI na dużą skalę. *Wytyczne pojawiły się po wdrożeniach. Narzędzia pojawiły się po wytycznych. Wiedza operacyjna wciąż się rozwija.*

Nie chodzi o obwinianie. To wyjaśnia, dlaczego luki mają charakter strukturalny, a nie są dziełem przypadku.

## Cztery warstwy bezpieczeństwa AI

Wiele nieporozumień w dyskusjach o bezpieczeństwie AI wynika z traktowania dokumentów dotyczących zarządzania, taksonomii zagrożeń, wytycznych inżynieryjnych i kontroli operacyjnych jako tego samego. Tak nie jest.

**Warstwa 1 to zarządzanie.** NIST AI RMF, ISO/IEC 42001 i EU AI Act działają na poziomie organizacji i procesów. Opisują zarządzanie ryzykiem AI, strukturę nadzoru i dokumentowanie odpowiedzialności. To struktury zarządzania, a nie kontrole techniczne.

**Warstwa 2 to taksonomia zagrożeń.** MITRE ATLAS dokumentuje taktyki przeciwników wymierzone w systemy AI. OWASP Top 10 for LLMs i OWASP Agentic AI Top 10 wymieniają konkretne klasy ataków. Te dokumenty nazywają ataki. Nie opisują zabezpieczeń.

**Warstwa 3 to wytyczne inżynieryjne.** Google SAIF, Microsoft AI SDL, OWASP AI Exchange i NIST AI 600-1 przedstawiają wskazówki dotyczące bezpiecznego tworzenia i wdrażania AI. NIST AI 600-1 jest znacznie bardziej szczegółowy niż podstawowy AI RMF i obejmuje wstrzykiwanie promptów, zatruwanie danych oraz zagrożenia informacyjne w generatywnych wdrożeniach AI.

**Warstwa 4 to operacje.** Monitorowanie, reagowanie na incydenty, kontrole w czasie działania, rejestrowanie, zasada najmniejszych uprawnień, potoki ewaluacji i zarządzanie dostępem to praktyki operacyjne. Wymagają procesów organizacyjnych, a nie tylko dokumentacji.

*Większość organizacji ma niepełne zabezpieczenia na warstwach 3 i 4. To tam znajduje się prawie całe ryzyko operacyjne.*

## Co działa w środowiskach produkcyjnych

AI w przedsiębiorstwach w 2026 roku to nie tylko chatboty. W środowiskach produkcyjnych działają:

- **Systemy RAG** pobierające dane z wewnętrznych repozytoriów dokumentów, wiki, baz danych i rekordów klientów
- **Agenci obsługi klienta** z dostępem do informacji o kontach i systemów zarządzania sprawami
- **Wewnętrzni asystenci produktywności** zintegrowani z pocztą e-mail, kalendarzami, systemami plików i platformami komunikacyjnymi
- **Narzędzia do przeglądu i generowania kodu** z dostępem do repozytoriów źródłowych
- **Agenci automatyczni** realizujący zaplanowane przepływy pracy z poświadczeniami do wewnętrznych API
- **Systemy przetwarzające dokumenty, umowy i dane finansowe**
- **Modele AI używane w wykrywaniu oszustw, rekrutacji i decyzjach dotyczących kontroli dostępu**

Każdy system ma inną powierzchnię ataku. System RAG korzystający z wewnętrznej bazy wiedzy stanowi jednocześnie ryzyko ujawnienia informacji i cel wstrzykiwania promptów. **Agent z dostępem do poczty e-mail i trwałym poświadczeniem to autonomiczny proces mający realny wpływ na rzeczywiste systemy.**

*Zespoły bezpieczeństwa często nie uczestniczyły w decyzji o wdrożeniu tych systemów. Nierzadko odkrywają istniejące wdrożenia AI podczas audytu zamiast przeglądu projektu.*

## AI działa teraz po obu stronach

**Możliwości AI dostępne zespołowi bezpieczeństwa są również dostępne napastnikom.**

**Rozwój wspomagany przez AI** skraca czas potrzebny na przekształcenie publicznych informacji o lukach w działające proof-of-concepty i narzędzia operacyjne. Każdy używający tych narzędzi, również napastnicy, szybciej przechodzi od lektury CVE do działającego kodu.

**Treści phishingowe generowane przez AI** tworzą e-maile o lepszej gramatyce, bardziej przekonującym kontekście i mniejszej liczbie łatwych do wykrycia błędów niż wiele ataków pisanych przez ludzi. Sygnały formatowania i wzorce językowe, których rozpoznawania uczono użytkowników, są mniej wiarygodne, gdy treść generuje AI.

**Klonowanie głosu na potrzeby kampanii vishingowych** pozwala podszywać się pod kierownictwo i współpracowników podczas rozmów na żywo. Próg wejścia dla ukierunkowanej socjotechniki spadł wraz z poprawą jakości syntezy głosu i obniżeniem kosztów dostępu.

**Deepfake wideo wykorzystywane w oszustwach typu business email compromise** przeszło od teorii do praktyki. Od 2024 roku w wielu sektorach udokumentowano oszustwa finansowe z użyciem wygenerowanych przez AI nagrań wideo, na których kierownictwo autoryzuje transakcje. *Szkolenia z podnoszenia świadomości przygotowano dla innego modelu zagrożeń.*

## Wstrzykiwanie promptów i zatruwanie kontekstu

**Zrozumienie wstrzykiwania promptów to punkt wyjścia do zrozumienia bezpieczeństwa systemów AI.**

Model językowy wykonuje instrukcje umieszczone w jego oknie kontekstowym. Kontekst obejmuje prompt systemowy, historię rozmowy, wyniki narzędzi i pobrane dokumenty. **Model nie potrafi niezawodnie odróżnić instrukcji programisty aplikacji od instrukcji umieszczonych przez napastnika w przetwarzanej treści.** To sedno wstrzykiwania promptów według definicji OWASP.

*Bezpośrednie wstrzykiwanie promptów* atakuje bezpośrednio dane wejściowe modelu. Użytkownik podaje tekst, który ma nadpisać instrukcje systemowe.

*Pośrednie wstrzykiwanie promptów* jest poważniejszym problemem w zastosowaniach korporacyjnych. Agent RAG pobiera dokument z bazy wiedzy. Dokument zawiera instrukcje nakazujące agentowi podjęcie innego działania. Narzędzie do tworzenia podsumowań przetwarza stronę internetową z ukrytymi dyrektywami. Bot pomocy technicznej odczytuje załącznik klienta zawierający instrukcje. Agent przetwarza instrukcje i działa zgodnie z nimi.

**Zatruwanie kontekstu** to szersza kategoria. Napastnik nie musi przejąć kontroli nad modelem, aby skompromitować system AI. Wystarczy umieścić złośliwą treść w kontekście modelu. Może to być zatruty dokument RAG, zatruty wpis pamięci, złośliwie przygotowana wiadomość e-mail przetwarzana przez agenta, wrogi plik PDF albo strona kontrolowana przez napastnika, którą odwiedza agent przeglądający internet. *To coś innego niż zatrucie modelu. Model jest w porządku. Kontekst nie.*

Obrona warstwowa zmniejsza to ryzyko. Filtrowanie danych wejściowych, walidacja wyników, narzędzia z ograniczonymi uprawnieniami, środowiska izolowane i ludzka akceptacja działań o istotnych skutkach pomagają. **Żadne z tych zabezpieczeń nie eliminuje tej klasy ataków.** OWASP, NIST, Anthropic, OpenAI i Microsoft zalecają podejście warstwowe, ponieważ pojedyncza kontrola nie wystarczy.

*Projektuj systemy przy założeniu, że pewien odsetek prób wstrzyknięcia promptów zakończy się powodzeniem. Odpowiednio ograniczaj ich konsekwencje.*

## Agenci AI, granice uprawnień i problem zasięgu kompromitacji

Agenci różnią się od chatbotów w jednym krytycznym z punktu widzenia operacji aspekcie: **podejmują działania.**

Agent połączony z pocztą e-mail, GitHubem, Jira, Slackiem, Salesforce, AWS i wewnętrznymi API to autonomiczny proces z dostępem do tych samych systemów, z których korzystają najbardziej podłączeni pracownicy. **Udane wstrzyknięcie promptu do takiego agenta nie powoduje niechcianej odpowiedzi tekstowej. Powoduje niepożądane działanie w prawdziwym systemie.**

**Zasięg kompromitacji zależy od tego, do czego agent ma dostęp.** Większość obecnie wdrożonych agentów ma znacznie większy dostęp, niż wymaga jakiekolwiek pojedyncze zadanie. Agent, który musi odczytać zgłoszenie Jira, nie powinien mieć też dostępu do zapisu w głównej gałęzi GitHuba. Agent przetwarzający zgłoszenia pomocy technicznej nie powinien przechowywać poświadczeń do systemu rozliczeniowego.

**Autoryzacja AI to odrębny problem od autoryzacji użytkownika.** Tradycyjne aplikacje pytają, czy użytkownik ma prawo wykonać daną czynność. Architektury agentowe wymagają ustalenia, czy ten agent ma prawo wykonać tę konkretną czynność dla tego użytkownika, w tym momencie i w oparciu o aktualny kontekst. Większość obecnych wdrożeń agentów tego nie robi.

**Zatruwanie narzędzi** różni się od wstrzykiwania promptów. Złośliwe lub przejęte narzędzie połączone z agentem zwraca opisy lub dane zaprojektowane tak, by zmienić jego zachowanie. Badacze coraz częściej uznają zatruwanie narzędzi za odrębną klasę ataków, zwłaszcza w integracjach opartych na MCP.

*Procedury akceptacji przez człowieka mają być ostatnią linią obrony przy istotnych działaniach agentów. Organizacje odkrywają jednak problem zmęczenia akceptacjami. Gdy agenci regularnie proszą o zgodę na rutynowe czynności, użytkownicy zaczynają automatycznie zatwierdzać prośby bez ich sprawdzania. Ostatnia linia obrony staje się formalnością.*

## Tożsamość AI to problem bezpieczeństwa przedsiębiorstwa

**Agenci mają poświadczenia.** Wdrożenia agentów AI obejmują tokeny OAuth, klucze API, poświadczenia kont usługowych i role cloud IAM. Są to tożsamości nieosobowe z rzeczywistym dostępem.

Konkretne luki we współczesnych wdrożeniach:

- **Poświadczenia agentów często są długotrwałe** i nie są rotowane zgodnie z harmonogramem podobnym do kont usługowych
- **Zakresy tokenów agentów bywają szersze**, niż wymagają zadania wykonywane przez agentów
- Zakres rejestrowania działań wykonanych z użyciem tożsamości agentów znacznie się różni
- **Wyciekanie poświadczeń przez prompty** jest udokumentowanym ryzykiem. Agent, który umieści klucze API w kontekście lub wynikach, ujawnia je każdemu, kto odczyta wynik lub pobierze rozmowę.
- Agenci uzyskujący dodatkowe poświadczenia przez wywołania narzędzi tworzą **łańcuchy tożsamości trudne do audytu**

*Zarządzaj tożsamościami agentów tak samo jak uprzywilejowanymi kontami usługowymi. Wymaga to dziś świadomego wysiłku, ponieważ większość narzędzi do zarządzania tożsamością nie obsługuje natywnie wzorców tożsamości agentów AI.*

## Trwała pamięć agentów tworzy długoterminową powierzchnię ataku

**Agenci z trwałą pamięcią mają powierzchnię ataku nieobecną w systemach bezstanowych.**

Napastnik, który może wstrzyknąć treść do pamięci agenta, tworzy pozycję utrzymującą się między sesjami. *Atak nie musi się powieść w pojedynczej interakcji. Wpływ gromadzony w pamięci przez dni lub tygodnie kształtuje przyszłe zachowanie agenta.* Niekiedy określa się to jako **atak długoterminowy lub atak uśpionym kontekstem**.

Wytycznych operacyjnych dotyczących tego konkretnego ryzyka jest niewiele. Organizacje wdrażające agentów z trwałą pamięcią powinny:

- Traktować **magazyny pamięci jako dane o wysokiej wartości**, wymagające kontroli dostępu
- **Walidować zawartość pamięci**, zanim agent zacznie na jej podstawie działać
- Wbudować w architekturę możliwość **audytu i przywracania wcześniejszego stanu pamięci**

## Łańcuch dostaw modeli nie jest traktowany jak łańcuch dostaw oprogramowania

**Organizacje pobierające wstępnie wytrenowane modele z publicznych repozytoriów przyjmują wykonywalne artefakty AI z zewnętrznych źródeł. Kontrola tych pobrań zazwyczaj nie dorównuje kontroli, którą te same organizacje stosują do pakietów npm, PyPI czy Maven.**

Konkretne zagrożenia w repozytoriach modeli:

- **Pliki modeli w formacie pickle PyTorch** wykonują dowolny kod Python podczas ładowania. Wykorzystywano to w udokumentowanych atakach na łańcuch dostaw. **SafeTensors** to format zaprojektowany specjalnie w celu rozwiązania tego problemu. Wybieraj go, gdy jest dostępny.
- Złośliwe programy ładujące modele, które instalują zależności lub wykonują kod konfiguracyjny wraz z modelem
- Modele wytrenowane na **zatrutych zbiorach danych**, które w określonych kontekstach generują subtelnie błędne wyniki
- Modele z **wbudowanymi tylnymi furtkami** aktywowanymi w określonych warunkach wyzwalających
- **Podszywanie się nazwą repozytorium**, aby publikować złośliwe modele pod znajomymi nazwami

*Niewiele organizacji prowadzi wykaz komponentów oprogramowania dla swoich systemów AI.* Większość nie potrafi wskazać, od którego modelu bazowego rozpoczęto działanie systemu produkcyjnego, jaką wersję danych treningowych wykorzystano do dostrajania ani czy wdrożone wagi odpowiadają wagom z ostatniej ewaluacji. Taka identyfikowalność jest warunkiem sensownego zabezpieczenia łańcucha dostaw. Dziś nie jest powszechna.

## Shadow AI tworzy niekontrolowany przepływ danych

**Prywatne konta konsumenckich usług AI to miejsca, przez które dane przemieszczają się bez kontroli.**

ChatGPT Enterprise, Claude Enterprise i Microsoft Copilot dla M365 zapewniają umowne zabezpieczenia danych klientów. **Prywatne konta ChatGPT, Claude, Gemini i podobnych usług konsumenckich domyślnie nie oferują tych gwarancji.**

Pracownicy używający prywatnych kont do przetwarzania dokumentów służbowych przekazują strategie prawne, rekordy klientów, kod źródłowy, prognozy finansowe, decyzje personalne i wewnętrzną komunikację przez kanały, których organizacja nie kontroluje. *Zespoły bezpieczeństwa często nie wiedzą dokładnie, jaka jest skala tych działań ani jakie kategorie danych są w nie zaangażowane.*

Kontrole DLP nie wykrywają danych przesyłanych przez przeglądarkę do konsumenckiej usługi AI. Zasady przechowywania danych nie obejmują historii rozmów na platformie zewnętrznej. **Obowiązki regulacyjne wynikające z GDPR, HIPAA, SOX i przepisów branżowych nie zmieniają się w zależności od tego, czy dane opuściły organizację przypadkowo, czy przez kartę przeglądarki.**

*Ustalenie rzeczywistego zakresu problemu przed budową zabezpieczeń jest koniecznym pierwszym krokiem. Prawie na pewno skala jest większa, niż zakładasz.*

## Systemy AI ujawniają dane w sposób nieznany tradycyjnym aplikacjom

**Nadmiarowe pobieranie przez RAG** zwraca dokumenty użytkownikom, którzy nie powinni mieć do nich dostępu. Pracownik zadaje pytanie. Komponent wyszukiwania zwraca dokument z ograniczonej części bazy wiedzy. Odpowiedź zawiera informacje z tego dokumentu. *Błąd kontroli dostępu wystąpił w warstwie pobierania, a nie aplikacji.* Wiele wdrożeń RAG powstało bez egzekwowania uprawnień do dokumentów zgodnych z uprawnieniami systemu źródłowego.

**Ujawnienie promptu systemowego** odsłania instrukcje operacyjne wbudowane w produkt AI. Prompty systemowe należy traktować jako poufne. Wyciekanie poświadczeń przez prompty, gdy poświadczenia agenta trafiają do kontekstu modelu lub jego wyników, jest zwykle poważniejszym ujawnieniem niż sama treść promptu systemowego.

**Błędy izolacji w systemach AI obsługujących wielu klientów** występują, gdy modele dostrojone na danych wielu klientów pokazują informacje jednego klienta w kontekście innego. To udokumentowana kategoria ryzyka w wielodostępnych produktach AI w modelu SaaS.

**Zapamiętywanie przez model** powoduje dosłowne odtwarzanie treści ze zbioru treningowego. Ryzyko nie znika, szczególnie w modelach dostrajanych na małych lub niedostatecznie zdeduplikowanych prywatnych zbiorach danych. Organizacje dostrajające modele na poufnych danych wewnętrznych powinny ocenić ryzyko zapamiętywania dla konkretnej metody treningu i wykorzystywanych danych.

## Organizacjom brakuje widoczności podczas inferencji

Tradycyjne programy bezpieczeństwa mają rozbudowane rejestrowanie infrastruktury. **Większość wdrożeń AI nie ma równie dobrego pokrycia swoich komponentów AI.**

Monitorowanie wdrożonego modelu językowego lub agenta wymaga innej telemetrii niż monitorowanie serwera aplikacji. Organizacje powinny zbierać:

- **Treść promptów i wyników** w formacie przydatnym do przeglądu zasad i wykrywania anomalii
- **Logi wywołań narzędzi** przez agentów, obejmujące nazwy narzędzi, argumenty i odpowiedzi
- **Logi pobierania danych** dla systemów RAG, w tym zapytania, zwrócone dokumenty i decyzje o kontroli dostępu
- **Sygnały klasyfikacji** prób jailbreaku i wstrzykiwania promptów
- **Monitorowanie spójności wyników** w celu wykrywania zmian zachowania między wersjami modeli
- **Wzorce opóźnień** mogące wskazywać na próby przepełnienia kontekstu

*Wiele organizacji, które wdrożyły AI w 2023 i 2024 roku, ma kody statusu HTTP i pomiary opóźnień. W tych środowiskach często brakuje telemetrii potrzebnej do wykrycia lub zbadania incydentu bezpieczeństwa AI. Odkrycie tego po incydencie jest za późne.*

## Reagowanie na incydenty AI wymaga osobnych procedur

**Obecne procedury reagowania na incydenty obejmują endpointy, sieci, aplikacje i tożsamość. Nie obejmują scenariuszy specyficznych dla AI.**

Pytania, z którymi zmierzy się zespół reagowania na incydenty, a na które obecne procedury nie odpowiadają:

- Jak ustalić, czy model został zatruty podczas przebiegu dostrajania?
- Jak określić zasięg skutecznego pośredniego wstrzyknięcia promptu do agenta z prawem zapisu w wielu systemach?
- Jak ocenić, czy dane treningowe lub dane dostrajania zostały wykradzione podczas kompromitacji łańcucha dostaw?
- Jak ustalić **bazowe zachowanie modelu**, aby porównać je z zachowaniem po incydencie?
- Jak zareagować, gdy aktualizacja modelu od zewnętrznego dostawcy wprowadza zachowanie wyglądające na celowe, a nie przypadkowe?
- Jak ustalić, czy **pamięć agenta była manipulowana przez dłuższy czas**?

*Te scenariusze wymagają przygotowania, zanim wystąpią. Telemetria musi być dostępna przed incydentem. Bazowe zachowanie modelu trzeba udokumentować przed potrzebą porównania.*

## Potoki ewaluacji stają się standardową praktyką inżynieryjną

Bezpieczeństwo AI coraz bardziej opiera się na **ustrukturyzowanej ewaluacji przed wdrożeniem**, a nie wyłącznie na monitorowaniu po wdrożeniu.

Ewaluacja bezpieczeństwa przed wdrożeniem obejmuje:

- **Testy wstrzykiwania promptów** z użyciem sprawdzonych zbiorów testowych i w kontekście konkretnego zastosowania
- **Testy porównawcze jailbreaków** z wykorzystaniem opublikowanych zestawów wrogich promptów
- **Ocenę odporności na ataki** modeli podejmujących decyzje o istotnych skutkach
- **Testy regresji** między wersjami modelu w celu wykrycia zmian jego zachowania
- **Ocenę zgodności z zasadami** na podstawie udokumentowanych wymagań akceptowalnego użycia
- **Ćwiczenia red teamingowe** prowadzone przez osoby próbujące pokonać konkretne zabezpieczenia

NIST, CISA, Anthropic, OpenAI, Microsoft i Google coraz częściej oczekują tego przy wdrożeniach wysokiego ryzyka. *Budowa minimalnych potoków ewaluacji przed wdrożeniami o poważnych konsekwencjach jest bardziej osiągalna, niż zakłada większość organizacji.* OWASP AI Exchange i opublikowane struktury ewaluacyjne głównych dostawców AI to rozsądne punkty wyjścia.

## Inwentarz zasobów AI jest prawdopodobnie niepełny

Tradycyjne zarządzanie zasobami obejmuje serwery, endpointy, aplikacje i urządzenia sieciowe. **Systemy AI wprowadzają kategorie zasobów, których większość inwentarzy jeszcze nie śledzi.**

Inwentarz systemów AI powinien obejmować:

- Każdy **wdrożony model**, w tym modele bazowe, warianty dostrojone i modele osadzające
- Wszystkie **prompty i instrukcje systemowe** działające w środowisku produkcyjnym
- Każdego **agenta** w środowisku i narzędzia, do których ma dostęp
- Wszystkie **indeksy RAG**, w tym źródła danych i egzekwowane podczas pobierania kontrole dostępu
- Wszystkie **wektorowe bazy danych** i ich zawartość
- Każdy **serwer MCP lub równoważny framework integracyjny** połączony z dowolnym agentem
- **Zewnętrzne usługi AI** wywoływane przez aplikacje, w tym dane przekazywane każdej usłudze

*Nie można zarządzać tym, czego się nie zinwentaryzowało. Większość organizacji pracujących nad bezpieczeństwem AI w 2026 roku odkrywa zasoby, o których istnieniu nie wiedziała.*

## Jaki jest rzeczywisty stan obrony

Narzędzia, struktury i praktyki obronne dotyczące bezpieczeństwa AI aktywnie i znacząco się rozwijają. To wczesny etap, ale sytuacja się poprawia.

**NIST AI 600-1** rozszerza podstawowy AI RMF dla generatywnej AI o znacznie bardziej konkretne wskazówki operacyjne. Organizacje utrzymujące zgodność AI powinny czytać AI 600-1, a nie tylko podstawowe ramy.

**MITRE ATLAS** udostępnia dokumentację taktyk, technik i procedur przeciwników dotyczących systemów AI w formacie ATT&CK. Modelowanie zagrożeń przed wdrożeniem na podstawie ATLAS prowadzi do precyzyjniejszych wymagań bezpieczeństwa niż korzystanie wyłącznie ze struktur zarządzania.

**OWASP LLM Top 10** i **OWASP Agentic AI Top 10** oferują obecnie najbardziej konkretne publicznie dostępne wskazówki operacyjne. Oba dokumenty są dla praktyków bardziej użyteczne niż większość formalnych programów nauczania.

**Red teaming AI** przed wdrożeniem jest coraz częściej oczekiwany przy wdrożeniach wysokiego ryzyka przez NIST, CISA i największych dostawców AI. Zewnętrzny rynek red teamingu AI już istnieje i rozwija się na potrzeby organizacji bez własnych zespołów.

Produkty bezpieczeństwa specyficzne dla AI, obejmujące monitorowanie, guardrails, autoryzację i egzekwowanie zasad w czasie działania, są na wczesnym etapie komercyjnym. *Ta kategoria jest rzeczywista i warto ją oceniać. Ponieważ rynek jest młody, obietnice marketingowe często przewyższają wykazane możliwości. Oceniaj rozwiązania względem konkretnej architektury wdrożenia, a nie scenariuszy opisywanych przez dostawcę.*

## Co należy zrobić

**Zrób inwentarz wdrożonych systemów.** Ustal, co działa, do jakich danych ma dostęp, jakie poświadczenia posiada, z jakich narzędzi korzysta i jakie działania wykonuje. To warunek wszystkiego innego.

**Traktuj agentów AI jak konta uprzywilejowane.** Stosuj zasadę najmniejszych uprawnień. Ogranicz poświadczenia do minimalnego dostępu wymaganego dla każdego zadania. Sprawdź uprawnienia każdego agenta i usuń zbędne dostępy.

**Wprowadź obserwowalność specyficzną dla AI przed wdrożeniem**, a nie po incydencie. Rejestrowanie promptów i wyników, wywołań narzędzi oraz pobierania danych to minimum telemetrii potrzebnej do analizy bezpieczeństwa.

**Oceń ekspozycję na shadow AI.** Ustal, z których usług AI pracownicy korzystają podczas zadań służbowych. Sprawdź, jakie kategorie danych przechodzą przez prywatne konta. Dostosuj zasady i zabezpieczenia do rzeczywistych ustaleń.

**Egzekwuj kontrolę dostępu na poziomie dokumentów w systemach RAG.** Jeśli warstwa pobierania nie egzekwuje zasad dostępu obowiązujących w systemach źródłowych, napraw ją, zanim ujawni ograniczony dokument nieuprawnionemu użytkownikowi.

**Przeprowadź audyt łańcucha dostaw modeli.** Dokumentuj każdy używany model bazowy. Wybieraj SafeTensors zamiast formatów pickle. Kontroluj artefakty modeli tak samo jak zależności oprogramowania.

**Zarządzaj tożsamościami agentów.** Zarządzaj tokenami OAuth i kluczami API agentów zgodnie z tym samym cyklem życia, przeglądem zakresów i rotacją, które stosujesz w przypadku uprzywilejowanych kont usługowych.

**Już teraz zbuduj procedury reagowania na incydenty AI.** Przed incydentem określ, jak badać scenariusze AI, jakie dowody będą potrzebne i jakie są dostępne działania naprawcze.

**Przeprowadzaj ewaluację przed wdrożeniem AI w zastosowaniach o poważnych konsekwencjach.** Jeśli nie masz własnych narzędzi, zacznij od dostępnych publicznych struktur.

*Nie utożsamiaj zgodności z zarządzaniem z poziomem bezpieczeństwa. Struktury zarządzania opisują proces i zarządzanie ryzykiem. Nie opisują technicznie odpornych systemów. Potrzebne są oba elementy.*

## Źródła

- NIST AI Risk Management Framework (AI RMF 1.0), 2023
- NIST AI 600-1: Generative AI Profile, 2024
- OWASP Top 10 for Large Language Model Applications, 2025
- OWASP Agentic AI Top 10
- OWASP AI Exchange
- MITRE ATLAS: Adversarial Threat Landscape for AI Systems
- Google Secure AI Framework (SAIF)
- Microsoft AI Security SDL
- CISA Guidance on AI Cybersecurity, 2024
- ISO/IEC 42001:2023 Artificial Intelligence Management Systems
- EU AI Act, Regulation (EU) 2024/1689
- SafeTensors format documentation, Hugging Face
