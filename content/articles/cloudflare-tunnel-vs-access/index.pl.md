---
title: "Cloudflare Tunnel a Access: czy potrzebujesz obu usług?"
date: 2026-09-11
lastmod: 2026-11-09
toc: true
draft: false
description: "Poznaj różnice między Cloudflare Tunnel i Access, wybierz ochronę dla domowego panelu i uniknij udostępnienia prywatnej aplikacji bez uwierzytelniania."
genre: ["Bezpieczeństwo sieci", "Samodzielny hosting", "Bezpieczeństwo chmury"]
tags: ["Cloudflare Tunnel", "Cloudflare Access", "Cloudflare Tunnel a Access", "Cloudflare Zero Trust", "cloudflared", "aplikacje hostowane samodzielnie", "bezpieczeństwo homelabu", "zdalny dostęp", "dostawca tożsamości", "zasady dostępu", "uwierzytelnianie aplikacji", "publiczna nazwa hosta", "ochrona origin", "tunel wychodzący", "tokeny usług", "Service Auth", "MFA", "prywatny panel", "reverse proxy", "CGNAT"]
cover: "/img/cover/cloudflare-tunnel-vs-access.webp"
coverAlt: "Domowy serwer łączy się przez przezroczysty kanał z bramą chmurową i oddzielnym punktem weryfikacji tożsamości."
coverCaption: ""
---

**Cloudflare Tunnel** łączy aplikację z Cloudflare. **Cloudflare Access** kontroluje, kto uzyskuje do niej dostęp. W przypadku prywatnego domowego panelu udostępnionego przez publiczną nazwę hosta użyj obu usług. Działający tunel sam w sobie nie wprowadza kontroli tożsamości. [Przewodnik Cloudflare dotyczący publikowania aplikacji](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) wyjaśnia tę różnicę.

## Najważniejsze wnioski

- **Wyjaśnij trasę:** odróżnij łącznik, origin i kontrolę tożsamości.
- **Skonfiguruj zasadę:** zezwól wskazanym osobom na dostęp do jednego prywatnego panelu.
- **Oceń ochronę:** przetestuj dozwolone, odrzucone i alternatywne ścieżki dostępu.
- **Zaplanuj dostęp:** udokumentuj osobne wymagania dla odwiedzających i automatyzacji.

## Zanim zaczniesz

**Odbiorcy:** właściciele domowych serwerów, którzy chcą zabezpieczyć panel w przeglądarce. Przykład zakłada aktywną domenę w Cloudflare, działającą lokalną aplikację internetową i uprawnienia do administrowania obiema usługami. **Szacowany nakład pracy:** 20–30 minut na ćwiczenie z zasadami po skonfigurowaniu łącznika. **Poziom trudności:** od początkującego do średnio zaawansowanego.

**Kolejność lektury:** zacznij od ról produktów, prześledź jedno żądanie, a następnie skonfiguruj i sprawdź prostą zasadę. Na koniec przygotuj specyfikację dostępu dla własnej usługi.

## Co robi każdy produkt

**Origin** to serwer, na którym działa aplikacja. Łącznik **`cloudflared`** inicjuje połączenia z twojej infrastruktury do Cloudflare, więc origin nie potrzebuje publicznego, routowalnego adresu IP. Żądania i odpowiedzi przemieszczają się następnie przez ustanowione połączenie. [Omówienie Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

| Pytanie | Tunnel | Access |
|---|---|---|
| **Jak Cloudflare łączy się z moim serwerem?** | Ustanawia połączenie | Nie zastępuje łączności z originem |
| **Kto uzyskuje dostęp?** | Samodzielnie nie zapewnia logowania użytkownika | Ocenia skonfigurowane zasady dostępu |
| **Co konfiguruję?** | Łącznik i trasę aplikacji | Aplikację, dostawcę tożsamości i zasady |
| **Co potwierdza powodzenie?** | Origin jest osiągalny przez tę trasę | Żądanie spełniło skonfigurowaną zasadę |

**Dostawca tożsamości (IdP)** uwierzytelnia odwiedzającego. **Zasada Access** określa działanie i kryteria dopasowania. Allow zezwala dopasowanym użytkownikom na dostęp. Bypass wyłącza egzekwowanie zasad Access dla pasującego ruchu. [Dokumentacja zasad Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

## Prześledź jedno żądanie z przeglądarki

Dla **`dashboard.example.com`** logiczna ścieżka żądania wygląda tak:

```text
Browser -> Cloudflare Access -> tunnel connection -> cloudflared -> dashboard
               |
               +-> identity provider when authentication is needed
```

**Łącznik inicjuje połączenie tunelowe na zewnątrz** z twojej sieci. Żądania przeglądarki trafiają później do origina przez to ustanowione połączenie. Połączenie wychodzące, które przenosi przychodzące żądania aplikacji, jest głównym powodem, dla którego Tunnel działa bez tradycyjnego przekierowania portu origina. [Model połączeń Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

**Uprawnienia w aplikacji** wymagają osobnej decyzji. Dostęp do panelu nie określa automatycznie, kto może zmieniać jego ustawienia lub usuwać dane. Jeśli aplikacja ma role obserwatora i administratora, skonfiguruj je i przetestuj niezależnie.

Na przykład **członek rodziny z prawami podglądu** potrzebuje wglądu w stan kopii zapasowych, a ty potrzebujesz uprawnień do zmiany ich lokalizacji. Zapisz te wymagania przed wybraniem tożsamości. Dwie osoby, które przejdą tę samą kontrolę Access, nie powinny automatycznie otrzymać tych samych uprawnień w aplikacji.

## Kiedy potrzebujesz obu usług

**Ochrona zależy od odbiorców.** Przed opublikowaniem trasy porównaj te konfiguracje:

| Docelowi odbiorcy | Sugerowana konfiguracja | Sprawdź przed użyciem |
|---|---|---|
| **Każda osoba czytająca publiczną witrynę** | Tunnel, jeśli jest potrzebny do łączności z originem | Publiczny dostęp jest zamierzony |
| **Ty i kilku członków rodziny** | Tunnel i Access | Zezwól tylko wskazanym tożsamościom |
| **Istniejący publiczny origin** | Access i osobna ochrona origina | Bezpośredni dostęp do origina nie może omijać kontroli |
| **Zaplanowany skrypt** | Tunnel i zasada Service Auth | Klient obsługuje metodę uwierzytelniania |

**Access bez Tunnel** jest obsługiwany w przypadku już osiągalnego origina. Zabezpiecz również alternatywne trasy do serwera. Cloudflare zaleca utworzenie aplikacji Access przed opublikowaniem nowej trasy tunelowej. [Wymagania dotyczące aplikacji hostowanych samodzielnie](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/).

*W przypadku prywatnego domowego panelu osiągalnego przez publiczną nazwę hosta zacznij od Tunnel i Access.*

## Skonfiguruj zasadę dla panelu

Użyj tej **przykładowej konfiguracji** dla dwóch zaplanowanych odwiedzających. Zastąp oba przykładowe adresy tożsamościami, które kontrolujesz. Utwórz aplikację Access przed dodaniem publicznej trasy tunelowej.

1. **Aplikacja:** otwórz Zero Trust → Access controls → Applications i utwórz aplikację hostowaną samodzielnie z publiczną nazwą hosta.
2. **Nazwa hosta:** wpisz osobną nazwę hosta panelu. W tym przykładzie obejmującym całą nazwę hosta pozostaw ścieżkę bez ograniczeń.
3. **Zasada:** utwórz zasadę Allow o nazwie `Dashboard viewers`.
4. **Selektor tożsamości:** dodaj regułę Include opartą na Emails. Zastąp `alice@example.com` i `bob@example.com` adresami dwóch wybranych osób.
5. **Logowanie:** wybierz dostawcę tożsamości używanego przez te osoby i określ odpowiedni czas trwania sesji.
6. **Trasa:** zapisz aplikację, a następnie połącz nazwę hosta z panelem przez tunel.

[Oficjalny przepływ konfiguracji aplikacji](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) opisuje te ustawienia. **Oczekiwany wynik:** nowy odwiedzający uwierzytelnia się przed uzyskaniem dostępu do aplikacji. Zanim zaufasz zasadzie, wykonaj poniższy test dla nieuprawnionej tożsamości.

## Interpretuj logikę zasad

**Include** łączy alternatywy operatorem OR. **Require** dodaje obowiązkowe warunki operatorem AND. **Exclude** usuwa pasujących użytkowników. Dodanie kolejnego warunku Include rozszerza grupę uprawnioną do dostępu. [Semantyka reguł Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

| Fragment zasady | Efekt logiczny |
|---|---|
| **Include Alice or Bob** | Wystarczy jedna z nazwanych tożsamości |
| **Include Alice, Include a country** | Dostęp uzyskują również osoby pasujące do kraju |
| **Include Alice, Require a country** | Alice musi dodatkowo spełniać warunek kraju |

**Ćwiczenie z przeglądu zasady:** wymaganie wskazuje wyłącznie Alice i Boba, ale współpracownik dodaje kraj jako kolejny warunek Include. Odrzuć zmianę, ponieważ dopuszcza kolejną grupę osób. Lokalizacja nie potwierdza przynależności do twojego gospodarstwa domowego.

## Uwierzytelniaj zaplanowane skrypty

**Token usługi** zawiera Client ID i Client Secret do zautomatyzowanych żądań. Skonfiguruj zasadę aplikacji tak, aby akceptowała token przez **Service Auth**. Utworzenie tokenu bez odpowiadającej mu zasady nie zapewnia dostępu do aplikacji. [Tokeny usług Cloudflare](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).

W przypadku skryptu kopii zapasowej lub kontroli monitorującej przechowuj **sekret** w chronionym magazynie poświadczeń narzędzia. Nadaj każdej integracji osobną nazwę tokenu i określ rozsądną datę wygaśnięcia. Gdy wycofasz integrację, wymień lub unieważnij token. Dokumentacja tokenów usług opisuje te operacje w całym cyklu życia.

**Jawnie sprawdź zgodność klienta.** Narzędzie oczekujące odpowiedzi API niekoniecznie obsłuży interaktywne logowanie w przeglądarce. Zanim wybierzesz zasadę, potwierdź obsługę nagłówków żądań lub innej wspieranej metody uwierzytelniania.

## Testuj decyzje o dostępie

Potraktuj te pozycje jako **testy akceptacyjne** wdrożenia:

| Test | Dowód do zapisania |
|---|---|
| **Odwiedzający bez zalogowania** | Access przechwytuje żądanie w nowej sesji przeglądarki |
| **Uprawniona tożsamość** | Zamierzona aplikacja wczytuje się po zalogowaniu |
| **Nieuprawniona tożsamość** | Niewymienione konto nie uzyskuje dostępu do aplikacji |
| **Alternatywna trasa** | Stare nazwy DNS i porty origina nie zapewniają niezamierzonego dostępu |
| **Automatyzacja** | Zatwierdzony klient działa, a żądanie bez poświadczenia kończy się niepowodzeniem |

**Widoczny ekran logowania** dowodzi tylko, że jedna ścieżka wymagała uwierzytelnienia. Przetestuj też przypadek odrzucenia i alternatywne trasy. To sugerowane kontrole, a nie wyniki wdrożonego przykładu.

## Sprawdź granicę origina

**Origin ufający tożsamości z Access** powinien weryfikować podpisany token aplikacji. Cloudflare przekazuje go w nagłówku **`Cf-Access-Jwt-Assertion`**. Sama obecność nagłówka nie potwierdza autentyczności. [Walidacja JWT w Cloudflare](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/).

**JSON Web Token (JWT)** zawiera podpisane twierdzenia. Gdy integrujesz tożsamość Access z originem, używaj udokumentowanej metody walidacji, w tym oczekiwanego wystawcy i odbiorcy aplikacji. Odczytanie adresu e-mail z zdekodowanego tokenu nie jest wystarczającą walidacją.

**Issuer** wskazuje podmiot wydający token. **Audience** określa aplikację, dla której jest przeznaczony. Sprawdzaj ważność tokenu i jego datę wygaśnięcia za pomocą obsługiwanej biblioteki walidacyjnej zamiast samodzielnie implementować kontrole podpisu.

**Wyraźnie określ granicę:** wskaż miejsce weryfikacji i trasy prowadzące do aplikacji. Stare przekierowanie portu lub alternatywna nazwa hosta wymagają osobnego przeglądu, nawet gdy główna nazwa hosta przejdzie wszystkie testy w przeglądarce.

## Rozwiąż rozbieżności w zasadach

| Obserwacja | Następna kontrola |
|---|---|
| **Nieoczekiwany odwiedzający uzyskuje dostęp** | Sprawdź warunki Include, zasady Bypass i zakres nazw hostów |
| **Odmowa dla zamierzonego odwiedzającego** | Porównaj zalogowaną tożsamość z dokładnymi wartościami selektora |
| **Skrypt otrzymuje stronę logowania** | Sprawdź poświadczenie i zasadę Service Auth |
| **Dopuszczony obserwator zmienia ustawienia** | Sprawdź role przypisane w samej aplikacji |

**Zachowanie sesji** wpływa również na ponowne testy. Access oferuje kilka czasów trwania sesji, w tym sesje aplikacji i sesje globalne. Zapisz ustawienie sesji i używaj nowej sesji podczas sprawdzania nowej tożsamości. [Zarządzanie sesjami Access](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/).

## Zapisz specyfikację dostępu

Przygotuj **krótką specyfikację** przed dodaniem kolejnej usługi:

```text
Usługa i nazwa hosta:
Dozwolone tożsamości użytkowników:
Wymagane role w aplikacji:
Poświadczenie automatyzacji i jego wygaśnięcie:
Inne trasy do origina:
Miejsce weryfikacji tokenów Access:
Wynik testu uprawnionej tożsamości:
Wynik testu nieuprawnionej tożsamości:
```

**Kryterium ukończenia:** inny administrator powinien wiedzieć, kto uzyskuje dostęp, jak każdy klient się uwierzytelnia i jakie dowody potwierdzają odmowę. Jeśli później dodasz integrację monitorującą, zaktualizuj jej poświadczenie i powtórz kontrolę żądania bez uwierzytelnienia.

## Następne kroki

Skorzystaj z [przewodnika konfiguracji Cloudflare Tunnel](/guides/how-to-setup-and-use-cloudflare-tunnels/), aby skonfigurować łącznik, a następnie wykonaj [oficjalny proces konfiguracji aplikacji Access](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/). W przypadku połączenia komórkowego przed wyborem zdalnego dostępu sprawdź [ograniczenia przekierowania portów w T-Mobile Home Internet](/articles/t-mobile-home-internet-port-forwarding/).
