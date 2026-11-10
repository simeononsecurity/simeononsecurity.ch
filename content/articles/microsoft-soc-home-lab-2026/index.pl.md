---
title: "Domowe laboratorium SOC Microsoft: zdobądź doświadczenie w cyberbezpieczeństwie w 2026 roku"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Zbuduj domowe laboratorium SOC Microsoft z Sentinel, Defender, Intune i Entra. Ćwicz analizę incydentów, sprawdzaj zasady dotyczące kluczy dostępu i dokumentuj dowody do portfolio."
genre: ["Cyberbezpieczeństwo", "Bezpieczeństwo chmury", "Rozwój kariery"]
tags: ["domowe laboratorium SOC", "Microsoft Sentinel", "Microsoft Defender XDR", "Defender for Endpoint", "Defender for Cloud", "Defender for Servers", "Microsoft Intune", "Microsoft Entra ID", "laboratorium Azure", "doświadczenie w cyberbezpieczeństwie", "analityk SOC", "centrum operacji bezpieczeństwa", "reagowanie na incydenty", "KQL", "Log Analytics", "Conditional Access", "uwierzytelnianie odporne na phishing", "klucze dostępu", "bezpieczeństwo tożsamości", "portfolio cyberbezpieczeństwa", "zarządzanie kosztami chmury", "bezpieczeństwo punktów końcowych"]
cover: "/img/cover/microsoft-soc-home-lab.webp"
coverAlt: "Laptop z osią czasu incydentu bezpieczeństwa na domowym biurku, pod chmurą zawierającą serwery i punkty końcowe."
coverCaption: ""
---

**Domowe laboratorium centrum operacji bezpieczeństwa (SOC)** daje miejsce do analizowania alertów, wyjaśniania dowodów i testowania zmian w zabezpieczeniach. Zbuduj niewielkie środowisko Microsoft, zbieraj telemetrię i opisuj każdą analizę. Najważniejszym rezultatem jest powtarzalne dochodzenie poparte dowodami.

Ten przewodnik rozwija podejście do laboratorium opisane w filmie o karierze w cyberbezpieczeństwie Mad Hat i w dostarczonej instrukcji Cyber Range. Wymagania produktów opiera na dokumentacji Microsoft. Konfigurację, wykrywanie i weryfikację rozdziela na mierzalne zadania.

## Najważniejsze wnioski

- **Zacznij od małego zakresu:** jeden zarządzany klient Windows i jedna testowa tożsamość wystarczą do pierwszych ćwiczeń.
- **Sprawdź telemetrię:** widoczne urządzenie lub podłączony portal nie dowodzą, że dzienniki są odbierane.
- **Dokończ analizę:** zapisz zdarzenie wyzwalające, dowody, reakcję i ponowny test.
- **Kontroluj wydatki:** osobno śledź licencje, przechowywane dane, sieć i moc obliczeniową.
- **Opisuj doświadczenie zgodnie z prawdą:** w CV przedstaw środowisko jako projekt laboratoryjny.

## Zanim zaczniesz

**Wymagania wstępne:** podstawowa administracja Windows, znajomość sieci i maszyn wirtualnych. Użyj dedykowanej dzierżawy Microsoft Entra i subskrypcji Azure przeznaczonej na laboratorium. Nie wykorzystuj w ćwiczeniu tożsamości produkcyjnych, prywatnych plików ani systemów pracodawcy.

**Szacowany nakład pracy:** przeznacz weekend na wstępną konfigurację, a potem zaplanuj krótsze sesje analityczne. To szacunek planistyczny. Zatwierdzenie wersji próbnej, dostępność limitów i udostępnienie usług wpływają na czas realizacji. **Poziom trudności:** średniozaawansowany.

Przygotuj oddzielne konto administracyjne i użytkownika testowego bez uprawnień. Przed testowaniem zasad dostępu skonfiguruj i zweryfikuj konta dostępu awaryjnego. Przydzielaj uprawnienia na czas poszczególnych zadań konfiguracyjnych, a do rutynowej analizy używaj konta o niższych uprawnieniach.

| Składnik | Cel w laboratorium |
|---|---|
| **Sentinel** | Zarządzanie informacjami i zdarzeniami bezpieczeństwa (SIEM) dla podłączonych źródeł dzienników |
| **Defender XDR** | Korelacja i analiza w usługach bezpieczeństwa Microsoft objętych licencją |
| **Defender for Endpoint** | Wykrywanie i reagowanie na zagrożenia na podłączonych urządzeniach |
| **Intune** | Rejestrowanie urządzeń oraz zarządzanie zasadami ich zabezpieczeń |
| **Entra ID** | Tożsamości, rejestry logowania i ocena zasad dostępu |
| **Defender for Servers** | Ochrona serwerów za pośrednictwem Defender for Cloud |

## Najpierw sprawdź licencje

**Microsoft 365 E5** to jeden ze sposobów uzyskania szerokiego zakresu funkcji w laboratorium, ale dostęp zależy od planów usług i licencji przypisanych uczestniczącym użytkownikom. Office 365 E5 i Microsoft 365 E5 to różne pakiety. Licencja jednego administratora nie zapewnia pokrycia dla każdego użytkownika testowego ani obciążenia. Przed wyborem subskrypcji sprawdź [wymagania wstępne Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/prerequisites).

**Sentinel w portalu Defender** działa bez E5 i Defender XDR. Dodanie XDR wiąże się z osobnymi wymaganiami licencyjnymi i konfiguracyjnymi. Pusty widok incydentów nie dowodzi braku licencji E5. Dokumentacja Microsoft dotycząca [wdrażania Sentinel](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard) opisuje obie konfiguracje.

**Ochrona serwerów** ma osobną ścieżkę licencjonowania. Defender for Servers integruje się z Defender for Endpoint w obsługiwanych obciążeniach serwerowych. Systemy klienckie Windows wymagają odpowiedniej licencji klienckiej. Nie zakładaj, że każda maszyna wirtualna Azure ma automatycznie licencję serwerową. Zobacz dokumentację Microsoft dotyczącą [integracji Defender for Endpoint](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

**Planowanie okresu próbnego:** na własnym koncie sprawdź uprawnienia, datę wygaśnięcia, ustawienia odnowienia i zawarte usługi. Nie planuj wydatków w oparciu o obiecaną długość okresu próbnego ani stałą miesięczną kwotę z filmu.

## Zaplanuj wydatki

**Budżety Azure** wysyłają powiadomienia, ale po osiągnięciu progu nie zatrzymują zużycia. Raportowanie kosztów również się opóźnia. Wcześnie skonfiguruj alerty i sprawdzaj wydatki po każdej sesji, korzystając z przewodnika Microsoft dotyczącego [konfiguracji budżetu](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets).

| Kategoria kosztów | Pytanie do planowania |
|---|---|
| **Licencje użytkowników** | Którzy użytkownicy potrzebują konkretnych planów usług i kiedy wygasają wersje próbne? |
| **Moc obliczeniowa** | Ile godzin działania maszyn wirtualnych wymaga każde ćwiczenie? |
| **Pamięć masowa** | Które dyski i migawki pozostają po wyłączeniu? |
| **Zbieranie dzienników** | Które tabele wymagają pozyskiwania danych i jak długo je przechowywać? |
| **Sieć** | Czy projekt obejmuje płatną usługę Bastion, publiczne adresy IP lub ruch wychodzący? |
| **Ochrona serwerów** | Które obciążenia mają włączony płatny plan Defender? |

**Wybór projektowy:** zacznij od jednego klienta. Dodaj serwer, gdy ćwiczenie wymaga telemetrii serwerowej. Cztery klienty i kilka serwerów zwiększają nakład administracyjny i koszty, zanim zapewnią przydatną praktykę analityczną.

## Zbuduj sieć

**Proponowany układ:** umieść zasoby Azure w grupie o czytelnej nazwie, na przykład **`rg-soc-lab`**. Użyj oddzielnych podsieci dla klientów i serwerów, jawnych reguł grup zabezpieczeń sieciowych oraz prywatnego dostępu administracyjnego. Sam podział na podsieci nie blokuje ruchu między obciążeniami.

W przypadku dedykowanego wdrożenia **Azure Bastion** przestrzegaj wymagań SKU, w tym zarezerwowanej nazwy **`AzureBastionSubnet`** i podsieci o rozmiarze **`/26`** lub większej w aktualnych wdrożeniach. SKU Developer korzysta z innego modelu wdrażania. Przed wyborem projektu zapoznaj się z [ustawieniami konfiguracji Bastion](https://learn.microsoft.com/en-us/azure/bastion/configuration-settings).

Nie wystawiaj RDP ani SSH do publicznego internetu. Ogranicz ruch administracyjny do wybranej ścieżki zarządzania. Zezwól na wychodzące połączenia wymagane do rejestracji i przesyłania telemetrii bezpieczeństwa.

**Weryfikacja:** przed instalacją obciążeń skonfiguruj prywatny dostęp administracyjny i sprawdź efektywne reguły sieciowe. Jeśli później dodasz celowo podatną aplikację, pozostaw ją w sieci ćwiczeniowej i ogranicz dostęp do maszyn testowych.

## Połącz Sentinel i dzienniki

**Konfiguracja w portalu:** utwórz obszar roboczy Log Analytics i włącz w nim Sentinel. Jeśli obszaru roboczego nie ma w portalu Defender, otwórz **System > Settings > Microsoft Sentinel > Connect a workspace**. Sprawdź dzierżawę i wymagane role Azure oraz Entra zgodnie z [wymaganiami wstępnymi wdrożenia](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard).

**Zbieranie dzienników to osobny etap.** W Entra skonfiguruj ustawienia diagnostyczne tak, aby wymagane kategorie aktywności trafiały do tego samego obszaru roboczego. Zacznij od interaktywnych logowań i zdarzeń audytowych. Przewodnik Microsoft dotyczący [integracji dzienników Entra](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs) opisuje uprawnienia i konfigurację miejsca docelowego.

Aktualny przepływ pracy Sentinel obsługuje również połączenie za pośrednictwem portalu Microsoft Defender. Sprawdź, czy wybrano właściwy główny obszar roboczy, dzierżawa odpowiada tożsamościom testowym, a konto ma wymagane role, zanim zaczniesz diagnozować pustą tabelę. Sama widoczność w portalu nie dowodzi pozyskiwania danych. [Wdrażanie Sentinel w portalu Defender](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard)

```kusto
SigninLogs
| where TimeGenerated > ago(24h)
| where UserPrincipalName =~ "soc-test@YOUR-TENANT.onmicrosoft.com"
| project TimeGenerated, UserPrincipalName, AppDisplayName,
          IPAddress, ResultType, ConditionalAccessStatus, CorrelationId
| order by TimeGenerated desc
```

Uruchom ten przykład w **języku zapytań Kusto (KQL)** w widoku Logs obszaru roboczego po wygenerowaniu nowego logowania testowego. Zastąp przykładową nazwę UPN użytkownikiem laboratoryjnym. Kolumny odpowiadają [schematowi tabeli SigninLogs](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/signinlogs).

**Oczekiwany wynik:** wiersz odpowiadający kontu testowemu i godzinie logowania. Brak wierszy oznacza konieczność sprawdzenia zakresu czasu, tożsamości, ustawień zbierania, miejsca docelowego i opóźnienia pozyskiwania. Brak tabeli wskazuje najpierw na problem ze zbieraniem danych lub obszarem roboczym, a dopiero później na problem z wykrywaniem.

## Podłącz pierwszy punkt końcowy

**Rejestrowanie urządzenia w Intune i wdrażanie EDR** to osobne etapy. Połącz Intune z Defender for Endpoint, zarejestruj obsługiwany klient Windows, a następnie przypisz do jego grupy laboratoryjnej zasady wdrażania funkcji wykrywania i reagowania na punktach końcowych. Sama rejestracja w Entra nie potwierdza wykonania żadnego z tych etapów.

W Intune sprawdź **Endpoint security > Defender for Endpoint**. Jeśli połączenie jest niedostępne, włącz połączenie Intune w zaawansowanych funkcjach punktów końcowych Defender. Postępuj zgodnie z instrukcjami dla danej platformy w [przewodniku integracji Intune i Defender](https://learn.microsoft.com/en-us/intune/device-security/microsoft-defender/configure-integration).

| Etap kontrolny | Dowody do zebrania |
|---|---|
| **Rejestracja** | Urządzenie widoczne w Intune z niedawnym zameldowaniem |
| **Przypisanie zasad** | Zasady wdrażania obejmują właściwą grupę urządzeń |
| **Raportowanie czujnika** | Defender pokazuje stan wdrożenia i aktualną telemetrię |
| **Test wykrywania** | Udokumentowany test generuje oczekiwany sygnał bezpieczeństwa |

**W przypadku serwerów** włącz wybrany plan Defender for Servers i integrację z punktem końcowym, a następnie zweryfikuj wdrożenie czujnika i raportowanie. Defender for Cloud wykrywa maszyny jeszcze przed zakończeniem wdrażania. Sama obecność zasobu w spisie nie wystarcza, co wyjaśnia przewodnik Microsoft dotyczący [wykrywania zasobów i wdrażania](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

## Przeanalizuj alert testowy

**Zacznij od udokumentowanego przez Microsoft testu wykrywania EDR** na punkcie końcowym laboratorium. Wykonaj aktualne [instrukcje testowe](https://learn.microsoft.com/en-us/defender-endpoint/edr-detection), uwzględniając wymagania platformy i wskazówki dotyczące rozwiązywania problemów. Zapisz czas wykonania przed otwarciem kolejki alertów.

Potraktuj wygenerowany alert jako ćwiczenie analityczne. Nazwa nadana przez produkt jest punktem wyjścia. Twoim zadaniem jest ustalenie, co się stało, i poparcie decyzji dowodami.

1. **Wstępna selekcja:** ustal źródło alertu, urządzenie, konto i czas zdarzenia.
2. **Inspekcja:** sprawdź drzewo procesów, wiersz poleceń, szczegóły pliku i dostępną aktywność sieciową.
3. **Ustalenie zakresu:** wyszukaj powiązane działania na testowanej tożsamości i pozostałych urządzeniach laboratoryjnych.
4. **Ocena:** wyjaśnij, czy dowody odpowiadają zaplanowanemu ćwiczeniu, czy niezwiązanemu zdarzeniu.
5. **Reakcja:** opisz wybraną reakcję, jej wpływ i kroki przywracania. Zastosuj obsługiwaną metodę izolacji tylko wtedy, gdy wymaga tego ćwiczenie.
6. **Ponowny test:** po zmianie zabezpieczenia powtórz odpowiedni test i porównaj dowody.

**Nie wymyślaj brakujących wyników.** Jeśli alert nie dotrze, zachowaj zapis wykonania testu i sprawdź zbieranie danych. Jeśli zabezpieczenie zablokuje test przed oczekiwanym zdarzeniem, udokumentuj wynik zapobiegania.

## Testuj zabezpieczenia tożsamości

**Phishing typu adversary-in-the-middle (AiTM)** wykorzystuje pośrednika kontrolowanego przez atakującego w procesie logowania. Dostarczony podręcznik korzysta z tego scenariusza, aby uzasadnić silniejsze uwierzytelnianie. Pierwsze ćwiczenie dotyczące tożsamości wykonaj bezpośrednio na własnym koncie bez uprawnień.

Zacznij od zapisania prawidłowego logowania i szczegółów uwierzytelniania. Przed interpretacją sygnałów ryzyka zapoznaj się z dokumentacją Microsoft dotyczącą [wykrywania ryzyka w Entra](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks). Wymagania wykrywania i przetwarzanie różnią się zależnie od sygnału. Nowy adres IP lub nieudane logowanie nie gwarantują alertu AiTM.

**Klucze dostępu (FIDO2)** wykorzystują poświadczenia powiązane z prawdziwą usługą, a nie kody wielokrotnego użytku wpisywane na stronie logowania pośredniczącej w uwierzytelnieniu. Włącz odpowiedni profil kluczy dostępu dla grupy pilotażowej i zarejestruj tę metodę przed wymuszeniem zasad. Informacje o obsługiwanych uwierzytelniaczach i ograniczeniach znajdziesz w [przewodniku Microsoft dotyczącym konfiguracji kluczy dostępu](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2).

**Ćwiczenie z Conditional Access:** utwórz zasadę obejmującą tylko laboratoryjną grupę pilotażową, wyklucz konta dostępu awaryjnego i wybierz **Require authentication strength > Phishing-resistant MFA strength**. Najpierw ustaw tryb **Report-only**, sprawdź jego wpływ, a następnie włącz zasadę. Dostosuj do wąskiej grupy testowej [przykładową zasadę administratora Microsoft](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa).

| Test | Dowody do zebrania |
|---|---|
| **Zasada w trybie raportowania** | Rekord logowania pokazujący ocenę proponowanej zasady |
| **Wymuszona zasada, słabsza metoda** | Świeże uwierzytelnienie wymaga silniejszej metody przed udzieleniem dostępu |
| **Wymuszona zasada, zarejestrowany klucz dostępu** | Udane logowanie spełniające wymagany poziom zabezpieczeń |

Przy każdym porównaniu wymuś nowe uwierzytelnienie i sprawdź szczegóły zasady. Istniejące sesje utrudniają porównania. **Zakres dowodu:** ćwiczenie weryfikuje wymaganie dotyczące uwierzytelniania. Nie dowodzi uniwersalnej ochrony przed przejęciem punktu końcowego ani kradzieżą istniejącej sesji.

## Przygotuj dowody do portfolio

**Przydatny wpis w portfolio** wyjaśnia decyzję w sposób umożliwiający innemu analitykowi jej ocenę. Dodaj krótki opis architektury, wymagania wstępne dotyczące zbierania danych, oś czasu zdarzeń i uzasadnienie reakcji.

```text
Exercise:
Date and UTC time window:
Lab scope and prerequisites:
Trigger and expected signal:
Observed alert or prevention:
Evidence and queries:
Affected identities and devices:
Disposition and reasoning:
Response and recovery:
Control change and retest:
Limitations and follow-up:
```

Wypełnij każde pole własnymi obserwacjami. **Przed publikacją oczyść eksporty:** usuń poświadczenia, dane sesji, informacje osobiste i zbędne identyfikatory ze zrzutów ekranu oraz wyników zapytań.

**Przykład do CV:** „Zbudowałem laboratorium bezpieczeństwa Microsoft, połączyłem dzienniki tożsamości z Sentinel, analizowałem alerty z testów punktów końcowych i udokumentowałem weryfikację Conditional Access”. Użyj tego opisu wyłącznie po wykonaniu tych zadań. Umieść go w sekcji projektów lub praktyk z podaniem rzeczywistych dat i zakresu.

Laboratorium pokazuje samodzielną praktykę. **Praca w produkcyjnym SOC** obejmuje także wpływ na działalność firmy, eskalację, zobowiązania dotyczące usług i współpracę z innymi zespołami. Wyjaśnij, które elementy ćwiczyłeś, a które pozostają poza twoim doświadczeniem.

## Rozwiązywanie problemów

| Objaw | Pierwsze sprawdzenie |
|---|---|
| **Obszaru roboczego nie ma w Defender** | Ta sama dzierżawa, włączony Sentinel i wymagane role wdrożeniowe |
| **Brak tabeli SigninLogs lub pusta tabela** | Kategorie diagnostyczne, obszar docelowy, nowe zdarzenia i zakres czasu |
| **Urządzenia nie ma w Intune** | Wymagania rejestracji i jej stan |
| **Urządzenie jest widoczne, ale nie ma telemetrii** | Rzeczywisty stan wdrożenia, kondycja czujnika i łączność wychodząca |
| **Zasada wdrożeniowa nie została zastosowana** | Zakres przypisania, platforma urządzenia i ostatnie zameldowanie |
| **Brak alertu ryzyka tożsamości** | Wymagania sygnału i zarejestrowana aktywność; nie zakładaj deterministycznego wykrywania |
| **Nieoczekiwane przyznanie dostępu** | Tryb raportowania, wykluczenia, zakres zasobów i istniejąca sesja |
| **Koszty po wyłączeniu** | Przydział zasobów i opłaty niezależne od mocy obliczeniowej |

**Kolejność diagnozowania:** potwierdź wystąpienie zdarzenia, następnie sprawdź, czy zbieranie działa, a dopiero potem analizuj logikę wykrywania. Zapisz każdą awarię i poprawkę w notatkach projektu.

## Wstrzymaj lub usuń laboratorium

**Cofnięcie przydziału** zwalnia przydzieloną moc obliczeniową maszyny wirtualnej. Samo zamknięcie systemu gościa nie gwarantuje cofnięcia przydziału. Sprawdź stan zasilania w Azure i zapoznaj się z dokumentacją Microsoft dotyczącą [stanów maszyn wirtualnych i rozliczeń](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing).

**Pozostawione zasoby** również wymagają kontroli. Dyski, migawki, usługi sieciowe, przechowywanie dzienników i subskrypcje użytkowników mają osobne cykle życia. Ustaw przypomnienie przed wygaśnięciem każdej wersji próbnej i sprawdź kolejny raport użycia po sprzątaniu.

Przed usunięciem grupy zasobów laboratorium wyeksportuj dowody, które chcesz zachować, i sprawdź ich zawartość. **Usunięcie grupy zasobów jest destrukcyjne** dla zawartych w niej zasobów. Użytkownicy dzierżawy, zasady Intune, zasady Conditional Access, subskrypcje i ustawienia zabezpieczeń na poziomie subskrypcji mogą wymagać osobnego sprzątania.

## Następne kroki

**Najpierw dokończ jedno udokumentowane dochodzenie**, zanim dodasz kolejne obciążenie. Następnie dodaj serwer, ćwiczenie z tożsamością albo regułę wykrywania z jasno określonym warunkiem testowym. Zapisz, czego uczy nowy składnik i ile kosztuje.

Skorzystaj z [przewodnika po laboratorium IT](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/) do ćwiczeń infrastrukturalnych oraz z [poradnika CV dla IT](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/), aby przedstawić swoją pracę. Kolejny projekt ogranicz do zakresu, który da się wyjaśnić od konfiguracji, przez dowody, po sprzątanie.
