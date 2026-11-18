---
title: "Podatności kamer Flock Safety: ponad 50 wykrytych luk"
date: 2026-05-24
lastmod: 2026-11-15
toc: true
draft: false
description: "Badanie podatności kamer Flock Safety obejmuje ujawnione dane uwierzytelniające, słabe zabezpieczenia, dostęp fizyczny i ograniczenia procesu ujawniania luk."
genre: ["Badania bezpieczeństwa", "Analiza podatności", "Technologie nadzoru", "Cyberbezpieczeństwo", "Ochrona prywatności", "Bezpieczeństwo IoT", "Bezpieczeństwo fizyczne", "Bezpieczeństwo sieci", "Infrastruktura krytyczna", "Technologie rządowe"]
tags: ["Podatności Flock Safety", "Bezpieczeństwo ALPR", "Hakowanie kamer", "Luki bezpieczeństwa IoT", "Hasła zapisane na stałe", "Podatności Android Things", "Wykorzystanie dostępu fizycznego", "Bezpieczeństwo sieci", "Błędy szyfrowania", "Naruszenia prywatności danych", "Ujawnienia CVE", "Badania bezpieczeństwa", "Badania GainSec", "Dochodzenie Bena Jordana", "Bezpieczeństwo kamer monitoringu", "Luki w technologiach rządowych", "Krytyczne podatności", "Odpowiedzialne ujawnianie", "Analiza cyberbezpieczeństwa", "Technologie organów ścigania", "Bezpieczeństwo publiczne", "Bezprzewodowy punkt dostępowy", "Obejście uwierzytelniania", "Dane uwierzytelniające w postaci jawnej", "Wyciek RF", "Atak TEMPEST", "Ujawnienie informacji", "Dostęp do powłoki root", "Zdalne wykonanie kodu", "Audyt bezpieczeństwa", "Ocena podatności", "Ryzyko dla bezpieczeństwa narodowego", "Dochodzenie Senatu", "Program bug bounty", "Podatność zero-day", "Tworzenie exploitów", "Testy penetracyjne", "Biała księga bezpieczeństwa", "Publikacja 404 Media", "Niezależne badania", "Bezpieczeństwo sprzętu", "Analiza oprogramowania układowego", "Eksploatacja systemu"]
cover: "/img/cover/flock-safety-camera-security-vulnerabilities-research-2026.webp"
coverAlt: "Zaawansowana kamera monitoringu z niebieskimi i zielonymi podświetleniami na ciemnym tle. Otaczające ją abstrakcyjne kształty i linie symbolizują luki w zabezpieczeniach cyfrowych."
coverCaption: "Krytyczne luki narażają ponad 80 000 kamer monitoringu na nieautoryzowany dostęp"
canonical: "https://simeononsecurity.com/articles/flock-safety-camera-security-vulnerabilities-research-2026/"
---

**Ponad 50 krytycznych luk w zabezpieczeniach naraża największą prywatną sieć monitoringu w kraju**

## Wprowadzenie: kryzys bezpieczeństwa narodowego

Pod koniec 2024 roku i przez cały 2025 rok niezależni badacze bezpieczeństwa odkryli coś, co może być **najpoważniejszą porażką w zabezpieczeniach technologii nadzoru stosowanej przez organy ścigania w historii Stanów Zjednoczonych**. W systemach kamer Flock Safety wykryto **ponad 50 krytycznych podatności**. Te same kamery codziennie fotografują i śledzą ponad **150 milionów pojazdów** w ramach ponad **80 000 wdrożeń** w całym kraju.

Artykuł zawiera kompleksową analizę techniczną tych podatności na podstawie:
- **Formalnej białej księgi GainSec** „Examining the Security Posture of an Anti-Crime Ecosystem” (51 ustaleń, 22 przypisane identyfikatory CVE, 8 w toku)
- **Dziennikarskiego śledztwa Bena Jordana** i praktycznych testów bezpieczeństwa
- **Relacji 404 Media** o publicznie dostępnych obrazach z kamer
- **Oficjalnych odpowiedzi** Flock Safety i senatorów USA
- **Opublikowanych ujawnień** w National Vulnerability Database (NVD)
- **Zrzutu systemu plików z września 2026 roku**, opublikowanego przez Distributed Denial of Secrets, wraz ze szczegółową analizą techniczną Micaha Lee oraz wspólnym śledztwem WIRED i 404 Media

Aby poznać **powody wdrażania tych kamer** i **ich wpływ na prywatność**, przeczytaj artykuł: **[Monitoring Flock Safety: rozpowszechnienie, obawy dotyczące prywatności i sposoby ochrony](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**

Informacje o **wykrywaniu tych kamer** znajdziesz w artykule: **[Projekt wykrywania Flock-You: sprzętowy przewodnik po przeciwdziałaniu nadzorowi](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**

______

## Skala problemu

### Skala podatnej infrastruktury

Stan na maj 2026 roku:
- **Ponad 80 000 kamer Flock Safety** wdrożonych w Stanach Zjednoczonych
- **Ponad 5 000 miast i miejscowości** korzystających z usług Flock
- **Ponad 3 500 organów ścigania** z dostępem do systemu
- **Ponad 22 000 użytkowników organów ścigania** korzystających z baz danych
- **Miliardy punktów danych** przechowywanych w przeszukiwalnych bazach

### Oś czasu podatności

- **Koniec 2024 roku**: badacz bezpieczeństwa Jon „GainSec” Gaines odkrywa pierwsze podatności
- **Luty 2025 roku**: rozpoczyna się odpowiedzialne ujawnianie luk firmie Flock Safety
- **Kwiecień 2025 roku**: opublikowane zostają pierwsze przypisane identyfikatory CVE
- **Listopad 2025 roku**: ukazuje się formalna biała księga z 51 ustaleniami
- **Grudzień 2025 roku**: Ben Jordan demonstruje podatności na nagraniu
- **Styczeń 2026 roku**: 404 Media odkrywa ponad 60 publicznie dostępnych obrazów z kamer
- **Luty 2026 roku**: senatorowie USA wnioskują o dochodzenie Federalnej Komisji Handlu (FTC)
- **Maj 2026 roku**: proces ujawniania nadal trwa

### Kategorie podatności

Ponad 50 podatności obejmuje kilka kategorii:
1. **Uwierzytelnianie i autoryzacja** (hasła zapisane na stałe, brak MFA)
2. **Kryptografia i szyfrowanie** (niezaszyfrowane dane w spoczynku i podczas przesyłania)
3. **Bezpieczeństwo sieci** (odsłonięte punkty dostępowe Wi-Fi, dane uwierzytelniające w postaci jawnej)
4. **Bezpieczeństwo fizyczne** (wykorzystanie sekwencji naciśnięć przycisku, odsłonięte porty USB)
5. **Prywatność danych** (nieautoryzowane gromadzenie danych, zbyt długi okres przechowywania)
6. **Projekt systemu** (przestarzałe oprogramowanie, niewystarczająca kontrola dostępu)
7. **Ujawnienie informacji** (odsłonięte klucze API, publiczne obrazy z kamer)

______

## Zrzut systemu plików z września 2026 roku

**We wrześniu 2026 roku organizacja non-profit Distributed Denial of Secrets zajmująca się przejrzystością opublikowała pełne obrazy systemu plików z działającej kamery Flock.** Grupa określająca się jako **stegan0gram** odkręciła urządzenie od słupa, skopiowała pamięć wewnętrzną i opublikowała obrazy. **404 Media** i **WIRED** przeprowadziły wspólne śledztwo, a badacz bezpieczeństwa **Micah Lee** opublikował analizę techniczną zawartości.

Wszystkie wcześniejsze ustalenia w tym artykule pochodziły z urządzeń laboratoryjnych badaczy lub zakupionych egzemplarzy. Ten zbiór danych pochodzi z kamery działającej w służbie miejskiej. To najsilniejszy dotąd opublikowany dowód.

*Kamera nie została zaatakowana przez sieć. Została fizycznie zdjęta.*

### Zawartość zrzutu

Publikacja obejmuje obrazy trzech partycji. Każda przedstawia inny element problemu.

| Partycja | Rozmiar | Znaczenie |
|-----------|---------|-----------|
| **system** | 1,5 GB | Obraz systemu Android zawierający **19 aplikacji Flock**, między innymi `flock-sambuca`, `flock-collins` i `flock-phone-home` |
| **persist** | 32 MB | Dane urządzenia w `flock/auth0/auth0_cred`, na **niezaszyfrowanej partycji, która przetrwa przywrócenie ustawień fabrycznych** |
| **media** | 18 GB | Dzienniki i obrazy w kontenerze, którego **klucz deszyfrujący znajduje się na tej samej partycji** |

### Potwierdzony problem z danymi uwierzytelniającymi

Zrzut rozstrzyga, czy dane uwierzytelniające zapisane na stałe są teorią, czy działają w produkcji. Działają.

**Klucz API zapewniający dostęp do zaplecza Flock znajduje się na stałe w plikach binarnych aplikacji.** Wartość zapisano w klasie `CameraSettings` w `com.flocksafety.android.common.lib`. Flock dołącza tę współdzieloną bibliotekę do wszystkich 19 aplikacji, więc klucz znajduje się w każdej z nich. Aplikacja `flock-sambuca` używa go podczas konfiguracji.

**Proces uwierzytelniania przebiega następująco:**

1. Każda kamera prosi serwer Flock o dane uwierzytelniające i identyfikuje się adresem **MAC**
2. Usługa logowania **Okta Auth0** firmy Flock zwraca krótkotrwały token `FlockAuth0Token`
3. Kamera zapisuje zwrócone dane uwierzytelniające **w postaci jawnej**

Identyfikator klienta i sekret klienta Auth0 znajdują się na **niezaszyfrowanej partycji `/persist`**, w pliku zaprojektowanym tak, by przetrwać przywrócenie ustawień fabrycznych. Napastnik najpierw odzyskuje partycję persist, ponieważ nic jej nie chroni.

Szerszy problem sekretów zapisanych na stałe w platformie opisuje [Krytyczna podatność nr 4](#critical-vulnerability-4-hardcoded-credentials-throughout-system).

### Klucz szyfrujący przechowywany razem z zamkiem

Flock twierdzi, że kamery chroni **szyfrowanie na urządzeniu**. Zrzut pokazuje, jak to rozwiązanie działa w praktyce.

Partycja media o rozmiarze 18 GB znajduje się w zaszyfrowanym kontenerze. Klucz deszyfrujący jest na tej samej partycji, w pliku z rozszerzeniem `.key`. Grupa stegan0gram odzyskała klucz, odblokowała kontener i odczytała jego zawartość. **Obrazy są zaszyfrowane tak, jak zamknięte pudełko jest zabezpieczone, gdy klucz przyklejono do pokrywki.**

Odzyskane dzienniki ujawniły również położenie kamery. Współrzędne GPS występują w nich **155 razy** i skupiają się w promieniu około 100 metrów. To typowy rozrzut odbiornika przytwierdzonego do słupa. Współrzędne wskazują **Wauwatosa w stanie Wisconsin**, przedmieście Milwaukee, gdzie kamerę zamontowano przy N Mayfair Road. Micah Lee porównał dzienniki z Google Street View i zidentyfikował konkretne urządzenie na podstawie numeru seryjnego i adresu MAC.

*Szyfrowanie danych w spoczynku nic nie daje, gdy klucz leży obok zaszyfrowanych danych.*

### Stanowisko Flock

Odpowiedź Flock powtórzyła stanowisko firmy wobec wcześniejszych ustaleń GainSec. Rzecznik oświadczył:

> „Flock poważnie traktuje bezpieczeństwo i prowadzi publiczną politykę ujawniania podatności, która umożliwia badaczom bezpośrednie zgłaszanie potencjalnych luk. Nie otrzymaliśmy zgłoszenia za pośrednictwem tego procesu, a na podstawie ograniczonych informacji nie mamy wystarczających szczegółów, by ocenić przedstawione zarzuty.”

Trudno pogodzić tę odpowiedź z osią czasu. Podatności w systemie operacyjnym kamery zostały publicznie załatane w **2018 i 2021 roku**, a standardy przechowywania danych uwierzytelniających i zarządzania kluczami nie zmieniły się od czasu znacznie wcześniejszego niż wdrożenie kamery. **Przegląd dekady publicznej historii podatności nie wymaga zewnętrznego zgłoszenia.**

Flock określił również zdjęcie i analizę kamery jako nielegalne, co według obecnego prawa jest prawdą. Ustalenia dotyczące bezpieczeństwa pozostają jednak aktualne niezależnie od sposobu pozyskania sprzętu.

### Dlaczego to ważniejsze niż wcześniejsze badania

Biała księga GainSec opisała 51 ustaleń dotyczących legalnie pozyskanych urządzeń. Flock podważył ocenę ich wagi i twierdził, że dostęp wymaga fizycznej bliskości.

Ten zrzut usuwa te zastrzeżenia. Fabryczny stan produkcyjnej kamery, bez modyfikacji jej operatorów, obejmuje dane uwierzytelniające infrastruktury w postaci jawnej, klucze zapisane obok chronionych danych i system operacyjny bez aktualizacji bezpieczeństwa od ośmiu lat. **Nie był potrzebny żaden exploit. Wystarczył klucz.**

______

## Flota urządzeń

Flock sprzedaje całą linię produktów, a właściwości zabezpieczeń różnią się między urządzeniami. Poniższe dane pochodzą z analiz GainSec i analizy oprogramowania układowego opracowanej przez społeczność badającą wykrywanie urządzeń w **[WiFi Mothership](https://wifimothership.com/flock)**.

| Urządzenie | Rola | Platforma | System operacyjny |
|---|---|---|---|
| **Falcon** | Zasilana energią słoneczną kamera ALPR | Qualcomm MSM8953 (Snapdragon 625) / OpenQ 624A SoM | Android 8.1 |
| **Sparrow** | Kamera ALPR z zasilaniem przewodowym | Taka sama jak Falcon | Android 8.1 |
| **Raven** | Wykrywanie wystrzałów i dźwięków alarmowych | ESP32-WROOM-32D z procesorem DSP Syntiant NDP120-B0 | FreeRTOS / ESP-IDF |
| **Bravo** | Moduł obliczeniowy Edge AI | Qualcomm QCS6490 / TurboX QCS6490-U8B | **Android 13, jądro 5.4.180** |
| **Picard** | Starszy moduł obliczeniowy | Wycofany na rzecz Bravo | |
| **Condor** | Kamera PTZ | Nie opisano w pełni | |
| **Alpha** | Autonomiczny dron | Zaprojektowany przez Flock, zgodny z NDAA | Autopilot własnościowy |
| **Aerodome M350** | Starszy dron | DJI Matrice M350 / M300 RTK | Oprogramowanie DJI |
| **Przyczepa LPR (ATS-5)** | Mobilna platforma ALPR | Podwozie All Traffic Solutions z kamerą Flock | Taka sama jak Falcon |
| **Wing** | Most programowy do kamer innych firm | Brak, obsługuje istniejące kamery IP | |

*Na pierwszy rzut oka widać lukę między generacjami. Moduł obliczeniowy działa na Androidzie 13, podczas gdy obsługiwane przez niego kamery korzystają z Androida 8.1, systemu wydanego w 2017 roku.*

**Falcon zasługuje na szczególną uwagę.** Obsługuje ALPR, nadal działa na Androidzie 8.1 i zapisuje dane na **niezaszyfrowanej pamięci eMMC o pojemności 32 GB**. Właśnie na tej pamięci znajdowały się pliki multimedialne i dzienniki odzyskane przez grupę stegan0gram. Sparrow korzysta z tej samej platformy, ale ma zasilanie przewodowe.

**Bravo to przeciwieństwo Falcona.** Nowoczesny moduł obliczeniowy z Androidem 13 i wnioskowaniem AI dla obrazu z kamer pokazuje, że firma potrafi dostarczać aktualne oprogramowanie, gdy się na to zdecyduje.


## Zweryfikowane identyfikatory CVE

Piętnaście CVE przypisano rodzinom Falcon, Sparrow, Raven i Bravo. Każdy identyfikator poniżej zweryfikowano we wrześniu 2026 roku w rejestrze **CVE.org**, a nie przepisano z wtórnego źródła.

### Wykrywanie wystrzałów i urządzenia audio

| CVE | Ustalenie | CVSS |
|-----|-----------|------|
| **CVE-2025-47818** | Hasło do połączenia zapisane na stałe | 2.2 |
| **CVE-2025-47819** | Układany interfejs debugowania bez właściwej kontroli dostępu | 6.4 |
| **CVE-2025-47820** | Kod przechowywany w postaci jawnej | 2.0 |
| **CVE-2025-47821** | Hasło do systemu zapisane na stałe | 2.2 |

Wszystkie cztery dotyczą urządzeń wykrywania wystrzałów w wersjach **wcześniejszych niż 1.3**.

### Czytniki tablic rejestracyjnych

| CVE | Ustalenie | CVSS |
|-----|-----------|------|
| **CVE-2025-47822** | Układany interfejs debugowania bez właściwej kontroli dostępu | 6.4 |
| **CVE-2025-47823** | Hasło do systemu zapisane na stałe | 2.2 |
| **CVE-2025-47824** | Kod przechowywany w postaci jawnej | 2.0 |

Te trzy podatności dotyczą oprogramowania układowego czytników tablic rejestracyjnych **do wersji 2.2 włącznie**.

### Błędy aplikacji w całej flocie

| CVE | Ustalenie | CVSS |
|-----|-----------|------|
| **CVE-2025-59403** | Aplikacja Collins udostępnia punkty administracyjne na **porcie 8080 bez uwierzytelniania**: `/reboot`, `/logs`, `/crashpack` i `/adb/enable`. Ostatni uruchamia ADB przez TCP bez potwierdzenia debugowania, co zapewnia napastnikowi w tej samej sieci dostęp do powłoki | **9.8 KRYTYCZNA** |
| **CVE-2025-59407** | Aplikacja DetectionProcessing zawiera magazyn kluczy Java i jego **hasło zapisane na stałe**; magazyn przechowuje klucz prywatny | **9.8 KRYTYCZNA** |
| **CVE-2025-59405** | Aplikacja Peripheral zawiera klucz API DataDog zapisany w postaci jawnej | 7.5 |
| **CVE-2025-59409** | Produkcyjne oprogramowanie układowe Falcon i Sparrow zawiera **dane dostępowe do deweloperskiej sieci Wi-Fi zapisane w postaci jawnej** | 7.5 |
| **CVE-2025-59406** | Aplikacja Pisco zawiera sekret klienta **Auth0 zapisany w postaci jawnej** | 6.2 |

### Moduł obliczeniowy Bravo

| CVE | Ustalenie | CVSS |
|-----|-----------|------|
| **CVE-2025-59402** | Akceptuje domyślny program ładujący Thundercomm TurboX 6490 Firehose, który umożliwia wgrywanie oprogramowania układowego i zrzucanie partycji | 5.4 |
| **CVE-2025-59404** | Ma odblokowany program rozruchowy, co omija Android Verified Boot | 7.5 |
| **CVE-2025-59408** | Ma wyłączony Secure Boot | 7.3 |

**Cztery podatności mają wektor ataku sieciowego i ocenę co najmniej 7,5, więc żadna nie wymaga dostępu fizycznego.** CVE-2025-59403 to przypisany identyfikator nieuwierzytelnionej ścieżki API. Obejmuje wywołanie `/adb/enable`, którego używa [Krytyczna podatność nr 1](#critical-vulnerability-1-button-press-wireless-access-point), by uzyskać powłokę root.

*Rejestry CVE są ważne z jeszcze jednego powodu. Niezależne rejestry potwierdzają problem sekretów w postaci jawnej, a strona alertów bezpieczeństwa Flock jest wymieniona jako źródło w wpisach Raven i LPR.*

______

## Krytyczna podatność nr 1: bezprzewodowy punkt dostępowy uruchamiany przyciskiem {#critical-vulnerability-1-button-press-wireless-access-point}

### CVE-2025-59403

**Poziom zagrożenia**: KRYTYCZNY (CVSS 9.8)

### Wykorzystanie podatności

Najbardziej alarmująca wykryta luka pozwala **każdej osobie mającej fizyczny dostęp** do kamery Flock Safety przejąć nad nią pełną kontrolę w mniej niż 60 sekund:

**Krok 1**: Naciśnij przycisk z tyłu kamery Falcon/Sparrow **trzy razy**
**Krok 2**: Urządzenie tworzy otwarty bezprzewodowy punkt dostępowy
**Krok 3**: Połącz się z siecią Wi-Fi (hasło zapisane na stałe: opisano je w białej księdze GainSec)
**Krok 4**: Wyślij polecenie włączenia ADB (Android Debug Bridge)
**Krok 5**: Połącz się przez ADB i uzyskaj powłokę root

### Szczegóły techniczne

```
Urządzenie: kamera ALPR Flock Safety Falcon/Sparrow
Sprzęt: Android Things 8.0/8.1 (koniec wsparcia w 2021 r.)
Wektor ataku: sekwencja fizycznych naciśnięć przycisku
Uwierzytelnianie: zakodowane na stałe hasło WiFi (takie samo we wszystkich urządzeniach)
Skutek: pełne przejęcie urządzenia, wykradzenie danych i instalacja złośliwego oprogramowania
```

### Możliwe działania po uzyskaniu dostępu

Po uzyskaniu dostępu do powłoki napastnik może:
- **Wyodrębnić wszystkie zapisane obrazy** (w tym osoby, nie tylko pojazdy)
- **Zmodyfikować lub usunąć dowody** zapisane na urządzeniu
- **Zainstalować trwałe złośliwe oprogramowanie** (przetrwa ponowne uruchomienie)
- **Sklonować tożsamość urządzenia**, by je podszywać
- **Przechwytywać i modyfikować** strumienie wideo
- **Wykorzystać urządzenie jako klienta botnetu** do ataków DDoS
- **Przechwycić dane Wi-Fi** pobliskich urządzeń (atak z użyciem honeypota)
- **Wyłączyć kamerę** lub spowodować odmowę usługi

### Demonstracja

Badacz bezpieczeństwa Ben Jordan zademonstrował ten atak na YouTube. Pokazał:
- Połączenie z punktem dostępowym Wi-Fi w **mniej niż 30 sekund**
- Uzyskanie dostępu do powłoki root w **mniej niż 60 sekund łącznie**
- Pełny dostęp do systemu plików, zapisanych obrazów i pamięci systemu
- Możliwość instalacji dowolnych aplikacji Android

**Cytat z demonstracji**:
> „Hasło do tego punktu dostępowego to [REDACTED], zapisane małymi literami. Każda sprawdzona przez nas kamera ma to samo hasło zapisane na stałe. Potem wysyłasz polecenie włączające ADB... całość trwa pewnie mniej niż 30 sekund, można całkowicie uzyskać powłokę urządzenia i pełny dostęp do niego.”

### Odpowiedź producenta

Flock Safety początkowo twierdził, że podatność dotyczy wyłącznie **urządzeń niepołączonych z chmurą**. Porównał je do **„iPhone'a skradzionego z ciężarówki przed połączeniem z siecią”**.

*To twierdzenie zostało obalone.* Badacze odtworzyli podatność **na urządzeniach połączonych z chmurą**, na wielu modelach kamer wykazujących **identyczną lukę** i na urządzeniach pochodzących z **różnych źródeł**. Wszystkie miały tę samą wadę.

______

## Krytyczna podatność nr 2: przestarzały system Android

### CVE-2025-47822 do CVE-2025-47824

**Poziom zagrożenia**: ŚREDNI do NISKIEGO (CVSS 6.4, 2.2 i 2.0)

### Problem

Kamery Flock Safety działają na **Android Things 8.0 lub 8.1**, który:
- Został **wycofany przez Google w 2021 roku**
- **Nie otrzymuje aktualizacji bezpieczeństwa od 2021 roku**
- Ma **ponad 900 opublikowanych podatności** według stanu na 2026 rok
- Jest **poza wsparciem od ponad pięciu lat**

### Analiza techniczna

**System operacyjny**: Android Things 8.0/8.1
**Koniec wsparcia**: styczeń 2021 roku
**Znane podatności**: ponad 900
**Poprawki bezpieczeństwa**: brak od zakończenia wsparcia
**Urządzenia objęte problemem**: moduły obliczeniowe Falcon, Sparrow, Condor i Bravo

### Co pokazuje zrzut z września 2026 roku

Obrazy systemu plików opublikowane we wrześniu 2026 roku wskazują dokładne wersje z kamery używanej w służbie, a nie z urządzenia laboratoryjnego.

| Komponent | Wersja w kamerze | Stan |
|-----------|------------------|------|
| **Android** | 8.1, kompilacja z 5 czerwca 2025 roku | Poziom poprawek bezpieczeństwa **2018-06-05** |
| **Jądro Linux** | 3.18.71 | Wydane w 2017 roku; seria 3.18 zakończyła się na wersji 3.18.140 w maju 2019 roku |
| **Aktualne wydanie Androida** | Android 17, czerwiec 2026 roku | O dziewięć głównych wersji nowsze |

Sama kompilacja kamery jest nowa. **Jej system operacyjny nie jest**, a poziom poprawek pokazuje, że od **ośmiu lat** urządzenie nie otrzymało aktualizacji bezpieczeństwa Androida. Jądro ma **69 wydań poprawek zaległości** względem końca własnej gałęzi utrzymaniowej, czyli brakuje w nim ponad dziewięciu lat poprawek.

### Dwie podatności obecne w tej kompilacji

Micah Lee wskazał dwie publicznie znane luki dotyczące komponentów obecnych w kamerze. Daty poprawek dowodzą, że urządzenie powstało przed ich wydaniem.

| CVE | Komponent | Skutek | Poprawka |
|-----|-----------|--------|----------|
| **CVE-2021-1905** | Sterownik GPU Qualcomm Adreno | Błąd use-after-free umożliwia **dowolnemu kodowi na urządzeniu, także aplikacjom bez uprawnień, uszkodzenie pamięci jądra i przejęcie pełnej kontroli** | Maj 2021 roku |
| **CVE-2018-9568** „WrongZone” | Obsługa gniazd w jądrze Linux | Pomylenie typów przez IPv6 umożliwia programowi **eskalację uprawnień do root**. Publicznie dostępny jest kod exploita | Grudzień 2018 roku |

Obie podatności załatano na długo przed kompilacją oprogramowania układowego kamery. **Żadna nie wymaga dostępu fizycznego, ponieważ można je wykorzystać za pomocą oprogramowania już działającego na urządzeniu.** Zastrzeżenie o bliskości fizycznej, którego Flock użył, by umniejszyć ustalenia GainSec, nie dotyczy żadnej z nich.

### Porównanie z urządzeniami konsumenckimi

Dla porównania:
- Producenci **smartfonów** przestają je aktualizować po około pięciu latach i **wycofują je ze sprzedaży**
- **Domową kamerę monitoringu** z oprogramowaniem sprzed pięciu lat uznano by za **krytycznie niezabezpieczoną**
- Agencje rządowe wymagają **aktualnego, wspieranego oprogramowania** w systemach wrażliwych

*Mimo to Flock Safety nadal wdraża i sprzedaje kamery z oprogramowaniem bez wsparcia producenta i poprawek bezpieczeństwa, zawierającym setki znanych exploitów i przetwarzającym wrażliwe dane organów ścigania.*

### Dlaczego to ważne

Używanie **oprogramowania po zakończeniu wsparcia** w urządzeniach monitoringu oznacza, że:
- **Każda opublikowana podatność Androida 8.x** działa na tych kamerach
- **Kod exploitów jest publicznie dostępny** dla wielu luk
- **Żadne poprawki nie usuną** nowo odkrytych problemów
- **Nie da się osiągnąć zgodności regulacyjnej** (FISMA, NIST, CMMC)

______

## Krytyczna podatność nr 3: brak szyfrowania podczas działania

### CVE-2025-47824 i CVE-2025-59407

**Poziom zagrożenia**: WYSOKI do KRYTYCZNEGO (CVSS od 2.0 do 9.8)

### Deklaracje Flock Safety a rzeczywistość

**Na stronie Flock Safety czytamy**:
> „Dane i nagrania są szyfrowane przez cały cykl życia”

**Ustalenia niezależnych badaczy** (GainSec i Ben Jordan):
> „W całym naszym badaniu nie odszyfrowaliśmy ani nie złamaliśmy niczego. Wszystko było niezaszyfrowane podczas działania.”

*Rozbieżność między deklaracją marketingową a rzeczywistością techniczną jest całkowita.*

### Dane niezaszyfrowane

Podczas badania urządzeń naukowcy znaleźli dane **niezaszyfrowane**:
1. **Zapisane nagrania wideo i obrazy**
2. **Dane tablic rejestracyjnych i metadane**
3. **Dane Wi-Fi i klucze API**
4. **Pliki baz danych z zapisami wykryć**
5. **Ruch sieciowy** (zob. podatność nr 6)
6. **Dzienniki systemu z poufnymi informacjami**

### Sprzeczność dotycząca przechowywania danych

**Deklaracja Flock Safety**: dane są automatycznie usuwane po siedmiu dniach
**Ustalenia badaczy**: znaleziono obrazy sięgające **daty produkcji urządzenia** (sprzed miesięcy lub lat)

Fragment białej księgi GainSec:
> „Znaleźliśmy obrazy starsze niż siedem dni. Niektóre zapisane zdjęcia zrobiono, gdy kamera została uruchomiona w fabryce, w której ją wyprodukowano.”

*Oznacza to, że deklarowane zasady prywatności nie są egzekwowane na poziomie urządzenia.*

### Konsekwencje dla prywatności

Brak szyfrowania oznacza, że:
- **Kradzież urządzenia fizycznego** powoduje natychmiastowy wyciek danych
- **Przechwycenie sieci** ujawnia dane w postaci jawnej
- **Osoby z dostępem wewnętrznym** mogą łatwo wyprowadzić dane
- **Ochrona nakazem sądowym** może nie obejmować niezaszyfrowanych danych
- Możliwe są **naruszenia wielu przepisów** (HIPAA, CCPA i innych)

______

## Krytyczna podatność nr 4: dane uwierzytelniające zapisane na stałe w całym systemie {#critical-vulnerability-4-hardcoded-credentials-throughout-system}

### CVE-2025-47818, CVE-2025-47821, CVE-2025-47823, CVE-2025-59407 i CVE-2025-59409

**Poziom zagrożenia**: KRYTYCZNY (CVSS 9.8, najwyższy poziom)

### Kategorie sekretów zapisanych na stałe

Badacze bezpieczeństwa wykryli **liczne dane uwierzytelniające zapisane na stałe**:

#### 1. Hasła do punktu dostępowego Wi-Fi
- **Wspólne hasło** dla wszystkich kamer Falcon/Sparrow
- **Użytkownicy i administratorzy nie mogą go zmienić**
- **Znane badaczom** i opublikowane w białej księdze (w ocenzurowanych fragmentach)
- **Potwierdzone przez CVE-2025-59409**: produkcyjne oprogramowanie układowe Falcon i Sparrow (kompilacja `OPM1.171019.026`) zawiera **dane dostępu do deweloperskiej sieci Wi-Fi w postaci jawnej**

#### 2. Klucze i tokeny API
- **Zapisane na stałe w oprogramowaniu układowym** i kodzie aplikacji
- **Zapewniają dostęp do zaplecza** różnych usług
- **Znalezione przez inżynierię wsteczną** plików APK Androida
- **Potwierdzone przez zrzut z września 2026 roku**: klucz API zaplecza zapisany na stałe w `CameraSettings` w `com.flocksafety.android.common.lib`, współdzielonej bibliotece dołączonej do **wszystkich 19 aplikacji Flock** na urządzeniu
- **Identyfikator klienta i sekret Auth0 znajdują się na niezaszyfrowanej partycji `/persist`** pod ścieżką `flock/auth0/auth0_cred`; lokalizacja ta przetrwa przywrócenie ustawień fabrycznych
- **Zwrócone dane uwierzytelniające są zapisywane w postaci jawnej** po uwierzytelnieniu kamery w usłudze Okta Auth0 Flock z użyciem jej adresu MAC

#### 3. Dane uwierzytelniające do baz danych
- **Bazy SQLite** bez ochrony hasłem
- Dane dostępu **MySQL/PostgreSQL** w plikach konfiguracyjnych
- **Bezpośredni dostęp do bazy danych** z lokalnej powłoki

#### 4. Magazyny kluczy kryptograficznych
- **Potwierdzone przez CVE-2025-59407**: aplikacja DetectionProcessing dołącza magazyn kluczy Java i jego hasło zapisane na stałe; magazyn zawiera **klucz prywatny**
- **Poziom zagrożenia**: KRYTYCZNY (CVSS 9.8), ponieważ materiał klucza znajduje się w pliku binarnym, który miał go chronić

#### 5. Nazwy sieci Wi-Fi
- Lista preferowanych sieci **zapisana na stałe w oprogramowaniu układowym**
- Umożliwia ataki z użyciem **fałszywych punktów dostępowych** (zob. podatność nr 6)

#### 6. Dane logowania do usług chmurowych
- **Tokeny AWS/Azure** osadzone w kodzie
- **Klucze API usług zewnętrznych** (ArcGIS, usługi mapowe)
- **Tokeny OAuth**, które nigdy nie są rotowane

### Scenariusz ataku: fałszywa sieć

Korzystając z nazw sieci Wi-Fi zapisanych na stałe, badacze zademonstrowali następujący atak:

1. Napastnik konfiguruje **fałszywą sieć Wi-Fi** z identyfikatorem SSID zapisanym na stałe
2. Kamera **łączy się automatycznie** (preferuje zapisane sieci)
3. Napastnik przechwytuje **cały ruch sieciowy** metodą man-in-the-middle
4. Z ruchu wyodrębnia dane uwierzytelniające w postaci jawnej
5. Uzyskuje **dostęp do systemu zaplecza**

**Nie potrzeba fizycznego dostępu do kamery.** Wystarczy znajdować się w zasięgu Wi-Fi.

______

{{< figure src="flock-safety-hardcoded-credentials-attack-vectors-diagram.webp" alt="Schemat pięciu wektorów ataku z użyciem danych uwierzytelniających zapisanych na stałe w kamerach Flock Safety: hasła Wi-Fi, klucze API, dane do baz danych i tokeny usług chmurowych" >}}

______

## Krytyczna podatność nr 5: brak uwierzytelniania wieloskładnikowego

### Niepowodzenie polityki organizacyjnej

**Poziom zagrożenia**: WYSOKI (organizacyjny)

### Ujawnienie

**Flock Safety nie wymaga 2FA/MFA** od niektórych organów ścigania, *tych samych, które codziennie uzyskują dostęp do danych o lokalizacji 150 milionów pojazdów.*

Cytat badacza bezpieczeństwa:
> „Kiedy pierwszy raz się o tym dowiedziałem, nie mogłem w to uwierzyć. Procedura bezpieczeństwa przy logowaniu do Disney Plus jest zbyt uciążliwa dla niektórych wydziałów policji, gdy uzyskują dostęp do poufnych informacji i lokalizacji praktycznie wszystkich osób.”

### Dlaczego to ważne

Bez MFA/2FA:
- **Jedno przejęte hasło** oznacza pełny dostęp do systemu
- **Ataki phishingowe** są bardzo skuteczne
- Działają ataki **credential stuffing** wykorzystujące dane z innych wycieków
- **Zagrożenia wewnętrzne** łatwiej zrealizować
- **Skradzione urządzenia** zapewniają natychmiastowy dostęp

### Porównanie

Wymagania bezpieczeństwa dla systemów **mniej wrażliwych**:
- **Disney+**: obsługuje 2FA
- **Gmail**: 2FA domyślnie włączone dla nowych kont
- **Bankowość**: 2FA wymagane prawnie
- **Media społecznościowe**: 2FA jest standardem

Wymagania bezpieczeństwa dla systemu **śledzącego codziennie ponad 150 mln pojazdów**:
- **Flock Safety**: 2FA jest opcjonalne (część agencji go nie stosuje)

### Odpowiedź senatora USA

Ustalenie to wyraźnie wskazano w **liście senatora Wydena** z wnioskiem o dochodzenie FTC. Zawarto w nim zarzut, że Flock Safety:
> „niepotrzebnie naraził wrażliwe dane osobowe Amerykanów na kradzież przez hakerów i zagranicznych szpiegów”

### Proste rozwiązanie

**Klucze bezpieczeństwa USB/NFC** kosztują **10–25 USD** i zapewniają:
- Uwierzytelnianie **odporne na phishing**
- **Brak dodatkowych aplikacji** i kodów
- Zgodność ze standardami **FIDO2/WebAuthn**
- **Prostą obsługę** (podłącz klucz lub dotknij urządzeniem)

*Jeśli to „zbyt kłopotliwe” dla funkcjonariuszy organów ścigania, **nie powinni mieć dostępu** do krajowych systemów nadzoru.*

______

## Krytyczna podatność nr 6: ruch sieciowy w postaci jawnej

### Oczekiwanie na przypisanie identyfikatora

**Poziom zagrożenia**: WYSOKI (badacze szacują CVSS 7.8)

**Tej kategorii nie przypisano identyfikatora CVE.** Najbliższy przypisany wpis, CVE-2025-59406, zawiera klasyfikację CWE-319 dotyczącą przesyłania danych w postaci jawnej, ale odnosi się do osadzonego sekretu Auth0, a nie przechwycenia transmisji. Ustalenia w tej sekcji nadal opierają się na opisanych wcześniej publikacjach badaczy.

### Podatność

Kamery podczas połączeń z siecią (LTE lub Wi-Fi) przesyłają dane **bez odpowiedniego szyfrowania**:

**Rodzaje przechwytywanego ruchu**:
- Obrazy i tekst tablic rejestracyjnych
- Metadane wykryć
- Dzienniki systemowe
- Dane konfiguracyjne
- Dane uwierzytelniające (w niektórych przypadkach)

### Wektor ataku nr 1: fałszywa sieć Wi-Fi

Badacze zademonstrowali następujące działanie:
1. Wyjmij kartę SIM z kamery **albo** skonfiguruj fałszywą sieć z zapisanym na stałe identyfikatorem SSID
2. Kamera łączy się z fałszywą siecią Wi-Fi
3. Przechwyć ruch za pomocą **Wireshark** lub podobnego analizatora pakietów
4. Przeanalizuj go narzędziem takim jak **NetworkMiner** lub **Unblo**
5. Wyodrębnij **dane uwierzytelniające w postaci jawnej** oraz wrażliwe dane

Cytat z badań GainSec:
> „Przez pewien czas przechwytywałem dane pcap przesyłane z jednej z tych kamer, a potem analizowałem je w Wireshark i Unblo... i rzeczywiście znalazłem w nich dane uwierzytelniające w postaci jawnej.”

### Wektor ataku nr 2: IMSI catcher / Stingray

Bardziej zaawansowany atak nie wymaga fizycznego dostępu do kamery:
1. Użyj **IMSI catchera** (samodzielnie zbudowanego urządzenia Stingray) lub profesjonalnego SDR
2. **Przejmij połączenie LTE**, podszywając się pod stację bazową
3. Kamera łączy się z **fałszywą stacją bazową**
4. Przechwytuj cały ruch metodą **man-in-the-middle**
5. Wyodrębnij dane uwierzytelniające, obrazy i metadane

**Dostęp fizyczny nie jest potrzebny.** Atak działa z odległości **setek stóp**.

### Możliwość współczesnego ataku typu Tempest

Transmisja danych w postaci jawnej umożliwia również **ataki w stylu Tempest**, w których:
- Można przechwycić emisje RF kamery
- Można **zdalnie odtworzyć strumień wideo**
- Technika przypomina metody CIA z **czasów zimnej wojny**
- Współczesny sprzęt SDR czyni ją **dostępną dla hobbystów**

______

## Krytyczna podatność nr 7: publicznie dostępne strumienie z kamer

### Odkrycie ze stycznia 2026 roku

**Poziom zagrożenia**: KRYTYCZNY (CVSS 10.0 - pełne ujawnienie systemu)

### Odkrycie

W styczniu 2026 roku Ben Jordan i **404 Media** odkryli, że za pomocą **prostych wyszukiwań Google** można znaleźć:
- **Ponad 60 całkowicie odsłoniętych** interfejsów administracyjnych kamer Flock Safety
- **Brak wymogu nazwy użytkownika i hasła**
- **Strumienie wideo na żywo** i 30 dni archiwalnych nagrań
- Dostęp do panelu **pełnej kontroli nad kamerą**

### Dostępne dane

Z poziomu tych odsłoniętych interfejsów każdy mógł:
- **Oglądać obraz na żywo**
- **Przeglądać nagrania z 30 dni**
- **Pobierać pliki wideo**
- **Sterować kamerami PTZ** (obrót, pochylenie, zbliżenie) w urządzeniach Condor
- **Zobaczyć ścieżki i skróty plików** z dowodami
- **Usunąć dowody** jednym kliknięciem
- **Zmienić ustawienia kamery**
- **Wyświetlić numery seryjne i lokalizacje urządzeń**

### Zaobserwowane naruszenia prywatności

Ben Jordan udokumentował obrazy przedstawiające:
- **Rodzinę wkładającą niemowlę do samochodu** na parkingu Lowe's
- **Mężczyznę wychodzącego rano z domu** w Nowym Jorku
- **Kobietę samotnie biegającą** leśnym szlakiem w Georgii
- **Kłócącą się parę** na ulicznym targu w Atlancie (AI automatycznie zbliżyła obraz twarzy)
- **Funkcjonariusza i karetkę** pomagających osobie w kryzysie psychicznym w stanie Iowa
- **Dzieci bawiące się** na placu zabaw w rejonie zatoki San Francisco
- **Mężczyznę na huśtawce** w pustym parku, przeżywającego prywatną chwilę

Cytat Bena Jordana:
> „Samo wypowiadanie tego na głos przyprawia mnie o mdłości. Próbuję jednak pokazać wam choć część informacji, które każdy na świecie, mający dostęp do komercyjnej wyszukiwarki, mógł znaleźć o osobach odwiedzających ten targ lub spacerujących tym szlakiem w ciągu ostatnich 31 dni.”

### Możliwości śledzenia

Kamery Condor PTZ mają funkcje śledzenia oparte na **AI**:
- **Automatycznie przybliżają obraz osób**
- **Śledzą ludzi w ruchu**
- **Wykrywają i przybliżają smartfony** (by odczytać ich ekrany)
- **Jednocześnie śledzą wiele celów**
- **Nagrywają bez przerwy**, bez nadzoru

### Możliwość doxxingu

Ben Jordan pokazał, jak łatwo ujawnione nagrania pozwalają ustalić tożsamość:
> „W ciągu dwóch minut dzięki rozpoznawaniu twarzy w komercyjnym narzędziu OSINT ustaliłem, że jedna z tych osób właśnie ukończyła studia medyczne, a druga zmaga się z przewlekłym zespołem jelita drażliwego. Para miała też w zeszłym roku dziecko... Wiem również, że jechali ponad 45 minut ze swojego podmiejskiego adresu.”

Porównanie z:
- **Usługami rozpoznawania twarzy**
- Profilami w **mediach społecznościowych**
- Bazami **rejestrów publicznych**
- Informacjami z **wycieków danych** (np. Park Mobile)
- **Rejestrami zgłoszeń alarmowych** (wiele miast je publikuje)

Rezultat: **pełne ustalenie tożsamości w kilka minut**

______

{{< figure src="flock-exposed-camera-feed-ptz-ai-tracking-privacy-violation-overview.webp" alt="Schemat pokazuje, jak odsłonięte kamery PTZ Flock Safety ze śledzeniem AI umożliwiały publiczny dostęp do obrazu na żywo osób w parkach, na szlakach i parkingach" >}}

______

## Krytyczna podatność nr 8: nieuprawnione gromadzenie danych

### Sprzeczność z publicznymi deklaracjami

**Poziom zagrożenia**: WYSOKI (konsekwencje dotyczące prywatności i prawa)

### Deklaracje Flock Safety

**Oficjalna deklaracja na stronie**:
> „Flock Safety nie rejestruje ani nie gromadzi danych o ludziach, wyłącznie o pojazdach”

### Ustalenia niezależnych badaczy

**Rzeczywiste działanie kamer**:
1. **Detekcja ruchu** uruchamia kamerę **przy dowolnym ruchu**, nie tylko pojazdu
2. **AI wyszukuje tablicę rejestracyjną** na obrazie
3. **Jeśli nie znajdzie tablicy**, obraz **i tak zostaje zapisany** (nie jest usuwany)
4. Osobny katalog przechowuje obrazy bez tablic
5. **Utrwalane i przechowywane są obrazy** **ludzi, pieszych i rowerzystów**

*Twierdzenie „wyłącznie o pojazdach” jest nieprawdziwe. Kamera zapisuje obrazy każdej osoby, która przed nią przejdzie.*

### Zweryfikowane obserwacje

Badacze udokumentowali kamery rejestrujące:
- **Osobę przechodzącą** przed kamerą (zapisany obraz)
- **Dłoń machającą** przed obiektywem (zapisany obraz)
- **Biurko lub przedmiot przesunięty** w pobliżu kamery (zapisany obraz)
- **Pracowników fabryki** w zakładzie produkcyjnym (przechowywanych przez wiele miesięcy)

Cytat GainSec:
> „Kiedy stanąłem przed kamerą, moduł radarowy uruchomił moduł kamery, by zrobił mi zdjęcie. Następnie lokalna AI szukała tablicy rejestracyjnej, nie znalazła jej, ale mimo to zapisała obraz w oddzielnym katalogu.”

### Konsekwencje prawne

Nieuprawnione gromadzenie tych danych może:
- **Naruszać deklarowane zasady prywatności** (praktyki wprowadzające w błąd)
- **Naruszać umowy zakupowe** (jeżeli miasta wymagały gromadzenia danych „wyłącznie o pojazdach”)
- **Prowadzić do naruszeń GDPR/CCPA** (obywatele UE, mieszkańcy Kalifornii)
- **Unieważniać zgody**
- **Narażać firmę na procesy** z powodu fałszywej reklamy

### Rozszerzenie zakresu nadzoru

Kamery **Condor PTZ** (wdrażane w latach 2025–2026) są **przeznaczone do śledzenia ludzi**:
- **Wykrywanie osób oparte na AI**
- **Automatyczne przybliżanie twarzy**
- **Śledzenie ludzi w ruchu**
- **Brak możliwości rezygnacji**
- **Częste wdrożenia** w parkach, na szlakach i stacjach komunikacji

*To ogromne rozszerzenie zakresu, od „czytników tablic rejestracyjnych” po nadzór nad całą populacją, bez zmiany zasad, nowych umów ani powiadomienia publicznego.*

______

## Krytyczna podatność nr 9: odsłonięte porty USB narażone na ataki Rubber Ducky

### Wykorzystanie dostępu fizycznego

**Poziom zagrożenia**: WYSOKI (wymagany dostęp fizyczny)

### Podatność

**Moduły obliczeniowe Bravo** i niektóre modele kamer mają:
- **Odsłonięte porty USB-C** na obudowie
- **Brak zabezpieczeń fizycznych** (uszczelnień obudowy)
- **Automatyczne uruchamianie** urządzeń USB
- **Brak wymaganego uwierzytelniania**

### Atak Rubber Ducky / BadUSB

**Urządzenie BadUSB** (kosztuje 5–15 USD):
- Udaje **klawiaturę USB**
- **Uruchamia zaprogramowane skrypty** (ładunki)
- **Wykonuje się automatycznie** po podłączeniu
- **Nie wymaga interakcji użytkownika**

### Scenariusz ataku

GainSec zademonstrował następujące działanie:
1. Podejdź do wdrożonego urządzenia Flock
2. Podłącz **urządzenie BadUSB** do odsłoniętego portu
3. Urządzenie wykonuje ładunek (skrypt)
4. Ładunek instaluje **trwałe złośliwe oprogramowanie**
5. Napastnik **odchodzi**
6. Złośliwe oprogramowanie **łączy się z serwerem sterującym** przez LTE/Wi-Fi

**Łączny czas**: poniżej 30 sekund

### Możliwości ładunku

Zautomatyzowane skrypty mogą:
- **Włączyć bezprzewodowy punkt dostępowy** (z pominięciem sekwencji naciśnięć przycisku)
- **Zainstalować tylne wejście** do zdalnego dostępu
- **Wyprowadzić dane** na zdalny serwer
- **Zmodyfikować nagrania** lub dowody
- **Wyłączyć kamerę** albo spowodować odmowę usługi
- **Dołączyć do botnetu** i prowadzić ataki DDoS
- **Przechwycić dane uwierzytelniające** z innych systemów

### Dlaczego to ważne

Ponad **80 000 kamer** często stoi w **półwiejskich lokalizacjach** o **ograniczonej widoczności**:
- **Dostęp fizyczny** jest stosunkowo łatwy
- **Brak ochrony** i stałego nadzoru
- Mocowanie za pomocą **zwykłych opasek zaciskowych do węży**
- Często montaż na wysokości **około 2,1 metra** (dostępnej przy użyciu stołka)

Cytat Bena Jordana:
> „Te kamery nie są nieprzeniknionymi fortecami. To plastikowe kamery z Androidem i moduły obliczeniowe zamontowane na wysokości około 2,1 metra za pomocą opasek zaciskowych do węży.”

______

{{< figure src="badusb-rubber-ducky-flock-camera-usb-exploit-attack-chain.webp" alt="Schemat ataku pokazujący, jak urządzenie BadUSB podłączone do odsłoniętego portu USB kamery Flock Safety może w niecałe 30 sekund zainstalować trwałe złośliwe oprogramowanie" >}}

______

## Krytyczna podatność nr 10: publicznie ujawnione klucze API

### Odkrycie badacza OSINT

**Poziom zagrożenia**: KRYTYCZNY (CVSS 9.5)

### Odkrycie

W 2025 roku **badacz OSINT Joshua Michael** odkrył:
- **Ujawnioną stronę demonstracyjną Flock Safety** znalezioną przez zaawansowane wyszukiwanie Google
- **Widoczny kod źródłowy** liczący 5 000 wierszy
- **Aktywny klucz API** osadzony w kodzie
- **Dostęp do ponad 50 prywatnych warstw** danych geoprzestrzennych

### Zakres dostępu przyznany przez klucz API

Ujawniony **klucz API ArcGIS** zapewniał dostęp do:

**1. Danych rejestracyjnych**
- Nazw klientów
- Adresów e-mail
- Liczby kamer w każdej lokalizacji
- Możliwości dołączania plików

**2. Bieżących lokalizacji radiowozów** (wielu jednostek)
- Śledzenia GPS pojazdów policyjnych w czasie rzeczywistym
- Wdrożenia w Aurora w stanie Kolorado
- Policji w Carrollton
- **Ryzyka dla bezpieczeństwa narodowego**

**3. Danych osobowych funkcjonariuszy**
- Imion i numerów telefonów
- Adresów e-mail
- Planowanych obszarów patrolowania
- Rejonów służbowych

**4. Bazy alertów o poszukiwanych pojazdach** (Dallas w Teksasie)
- **6 000 rekordów** oznaczonych pojazdów
- Tablic rejestracyjnych i przyczyn oznaczenia
- Miejsc i czasu wykrycia
- Identyfikatorów kamer, które zarejestrowały pojazdy
- **Pięciu miesięcy śledzenia przemieszczania się**

Cytat Joshuy Michaela:
> „Każdy mógł znaleźć tę mapę przez Google i śledzić wzorce przemieszczania się tych osób przez pięć miesięcy. Warto też zauważyć, że w kategorii przyczyny ktoś został oznaczony jako »podejrzany«, a wiele innych wpisów nie ma powodu albo pole jest puste.”

### Powierzchnia ataku

Ujawnione klucze API umożliwiają:
- **Śledzenie konkretnych pojazdów**
- **Narażenie bezpieczeństwa funkcjonariuszy** (adresy domowe, trasy patroli)
- **Naruszenie bezpieczeństwa operacyjnego** (miejsca obecności i nieobecności policji)
- **Zastraszanie świadków** (śledzenie osób zgłaszających przestępstwa)
- Gromadzenie **informacji kryminalnych przez zorganizowane grupy przestępcze**

### Kontekst naruszenia: Flax Typhoon

Zaledwie kilka tygodni przed tym odkryciem, według badaczy bezpieczeństwa Alexy Feminin oraz Jamesa Zhanga, **wspierana przez państwo chińskie** grupa hakerska **Flax Typhoon** przejęła ArcGIS.

Cytat z magazynu InfoSecurity:
> „Hakerzy mieli zaatakować legalną, publicznie dostępną aplikację ArcGIS... używaną do odzyskiwania danych po katastrofach, zarządzania kryzysowego i innych krytycznych zadań.”

**Oznacza to, że wrogie państwa mogły uzyskać dostęp do** lokalizacji radiowozów, tożsamości funkcjonariuszy, rozmieszczenia kamer monitoringu i schematów reagowania kryzysowego.

______

## Dodatkowe podatności (podsumowanie ponad 50 luk)

### Podatności 11–51

Biała księga GainSec dokumentuje **41 dodatkowych ustaleń**, w tym:

**Błędy projektowe systemu**:
- Tryb debugowania włączony w produkcyjnym oprogramowaniu układowym
- Niezabezpieczony proces rozruchu pozwala przejąć program ładujący
- Brak bezpiecznego elementu lub TPM do przechowywania kluczy
- Przewidywalny mechanizm aktualizacji oprogramowania układowego

**Problemy z uwierzytelnianiem**:
- Tokeny sesji nigdy nie wygasają
- Brak ograniczeń dostępu według adresu IP
- Wspólne dane uwierzytelniające w całej flocie urządzeń
- Brak przypinania certyfikatów

**Bezpieczeństwo sieci**:
- Otwarte porty z usługami debugowania
- Telnet włączony w części urządzeń
- Serwery FTP ze słabymi danymi uwierzytelniającymi
- Podatności na przekierowanie DNS

**Prywatność i przechowywanie danych**:
- Obrazy przechowywane dłużej, niż zadeklarowano
- Metadane nigdy nie są usuwane
- Gromadzone dane rozpoznawania twarzy
- Śledzenie lokalizacji niezwiązane z pojazdami

**Bezpieczeństwo fizyczne**:
- Łatwy demontaż obudów
- Odsłonięte interfejsy szeregowe
- Dostępne porty debugowania JTAG
- Brak plomb wskazujących na naruszenie

**Błędy kryptograficzne**:
- Słabe generowanie liczb losowych
- Klucze szyfrujące zapisane na stałe
- MD5 nadal używany w łańcuchu skrótów
- Wyłączona walidacja certyfikatów

**Ujawnianie informacji**:
- Szczegółowe komunikaty błędów ujawniają szczegóły wewnętrzne
- Włączone listowanie katalogów na serwerach WWW
- Komentarze w kodzie źródłowym zawierają dane uwierzytelniające
- Kopie konfiguracji są czytelne dla wszystkich

### Stan CVE

Stan na maj 2026 roku:
- **Przypisano i opublikowano 22 CVE**
- **Osiem CVE** oczekuje na przypisanie przez MITRE
- **21 ustaleń** nie zgłoszono do CVE (decyzja badacza)
- **Wszystkie ustalenia** opisano w białej księdze GainSec

Pełne szczegóły techniczne: [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)

______

## Odpowiedź Flock Safety

### Oficjalne oświadczenia

**Wpis na blogu z listopada 2025 roku**:
> „Flock dąży do ciągłego zwiększania bezpieczeństwa... Żadna z podatności opisanych w raporcie nie wpływa na zdolność naszych klientów do realizacji celów związanych z bezpieczeństwem publicznym.”

**Twierdzenie**: podatności wymagają dostępu fizycznego i „szczegółowej wiedzy”

**Dowody przeciwne**:
- Do znalezienia odsłoniętych strumieni z kamer wystarczało **wyszukiwanie w Google**
- Do ataków bezprzewodowych wystarczała **bliskość urządzenia**
- Ujawniony klucz API można było wykorzystać **zdalnie**
- Po ujawnieniu **powszechnie znano hasła zapisane na stałe**

### Podważanie badań na urządzeniach

Flock początkowo twierdził, że urządzenia badawcze:
> „Nie były połączone z chmurą... jak iPhone skradziony z ciężarówki przed pierwszym połączeniem z siecią”

*To twierdzenie okazało się nieprawdziwe.* Badacze przetestowali **urządzenia połączone z chmurą** i uzyskali identyczne wyniki. Kamery dostępne publicznie wykazywały **te same podatności**, a 404 Media znalazło **ponad 60 odsłoniętych kamer produkcyjnych**.

### Odpowiedź wobec badaczy

GainSec poinformował, że próby odpowiedzialnego ujawnienia spotkały się z:
- **Programem bug bounty z umową o zachowaniu poufności**, która uciszała zgłoszenie
- **Brakiem potwierdzenia** wprowadzonych poprawek
- **Oświadczeniem PR** wydanym przed upływem 90-dniowego terminu
- **Brakiem podziękowania** dla badacza w komunikacie prasowym
- **Utratą pracy** przez badacza w ciągu 48 godzin od publikacji nagrania

Ben Jordan zgłosił:
- **Wizyty policji** na swojej posesji
- **Podejrzenie prywatnych detektywów** fotografujących jego dom
- **Nękanie przez sąsiadów**
- **Groźby prawne** ze strony Flock Safety

Cytat Bena:
> „Nie uważam tych zdarzeń za konsekwencje ani karę za badanie podatności bezpieczeństwa. Uważam je za konsekwencje i karę za etyczne i przejrzyste działanie.”

### Dalsze wdrażanie

*Mimo tego wszystkiego* Flock Safety:
- **Nadal sprzedaje** podatne urządzenia
- **Nie udostępnia aktualizacji oprogramowania układowego** usuwających przyczyny problemu
- **Nadal korzysta** z Android Things 8.x (koniec wsparcia w 2021 roku)
- **Nie wymaga MFA** od organów ścigania

______

## Odpowiedź legislacyjna i polityczna

### Wniosek Senatu USA o wszczęcie dochodzenia

**Luty 2026 roku**: senatorowie **Ron Wyden** (Oregon) i **Raja Krishnamoorthi** (Illinois) wysłali do FTC formalny list z wnioskiem o wszczęcie dochodzenia.

**Fragment listu**:
> „Flock niepotrzebnie naraził wrażliwe dane osobowe Amerykanów na kradzież przez hakerów i zagranicznych szpiegów.”

**Wskazane podstawy**:
- Ryzyko dla bezpieczeństwa narodowego
- Wprowadzające w błąd deklaracje dotyczące prywatności
- Niewystarczające praktyki bezpieczeństwa
- Brak obowiązku stosowania MFA

### Działania rad miejskich

**Denver w stanie Kolorado**:
- Rada miasta **zagłosowała przeciwko** przedłużeniu umowy z Flock (grudzień 2025 roku)
- Wskazała na „**lekceważenie uczciwości i odpowiedzialności**” przez Flock
- Burmistrz **uchylił decyzję** w wyniku „zakulisowej umowy” (styczeń 2026 roku)
- Sprzeciw społeczności trwa

**Evanston w stanie Illinois**:
- Odkryto, że **ICE korzystało z kamer** bez zgody
- Zagłosowano za **usunięciem kamer**
- *Flock ponownie zainstalował kamery bez upoważnienia*
- Miasto wydaje środki podatników na **zakrywanie kamer płachtami** i działania prawne

**Oakland w Kalifornii**:
- Odroczono głosowanie nad **rozszerzeniem wartym 2,25 mln USD**
- Zlecono niezależny audyt bezpieczeństwa
- Ustalono, że twierdzenia Flock o skuteczności były **wprowadzające w błąd**

### Wnioski o udostępnienie dokumentów publicznych

Kilka miast prowadzi dochodzenia oparte na:
- Publicznie dostępnych badaniach bezpieczeństwa
- Wnioskach FOIA o umowy z Flock
- Wymogach niezależnego audytu
- Presji społeczności lokalnych

______

## Analiza techniczna: scenariusze ataków w praktyce

### Scenariusz 1: nadzór państwa obcego

**Podmiot zagrażający**: zagraniczna służba wywiadowcza

**Cel**: śledzenie urzędników rządowych

**Metoda**:
1. Użycie urządzenia IMSI catcher do przechwycenia ruchu LTE kamery
2. Wyodrębnienie z transmisji danych uwierzytelniających w postaci jawnej
3. Uzyskanie dostępu do zaplecza przez przejęte klucze API (lub wcześniej ujawnioną warstwę ArcGIS)
4. Wyszukanie w bazie pojazdów zarejestrowanych przy obiektach rządowych
5. Śledzenie przemieszczania się urzędników i personelu wojskowego

**Czas wykonania**: dni (po przygotowaniu infrastruktury)
**Prawdopodobieństwo wykrycia**: niskie (szyfrowane C2 naśladuje prawidłowy ruch)

### Scenariusz 2: kontrnadzór zorganizowanej przestępczości

**Podmiot zagrażający**: organizacja zajmująca się handlem narkotykami

**Cel**: ustalenie tras patroli policyjnych

**Metoda**:
1. Zakup urządzenia BadUSB (15 USD)
2. Dojazd do kamer na terenie działalności
3. Podłączenie BadUSB do odsłoniętego portu USB (30 sekund)
4. Ładunek wyłącza kamerę lub modyfikuje nagrania
5. Alternatywnie: ładunek wyprowadza dane o lokalizacji radiowozów na zdalny serwer

**Czas wykonania**: 30 sekund na kamerę
**Prawdopodobieństwo wykrycia**: niskie (wygląda jak aktywność prawidłowego urządzenia)

### Scenariusz 3: prześladowca lub sprawca przemocy domowej

**Podmiot zagrażający**: agresywny były partner

**Cel**: śledzenie przemieszczania się ofiary

**Metoda**:
1. Zdobycie numeru rejestracyjnego ofiary (informacja publiczna)
2. Wyszukanie w Google odsłoniętego interfejsu kamery Flock (podatność z 2026 roku)
3. Sprawdzenie 30 dni nagrań pod kątem pojawienia się pojazdu
4. Porównanie z publicznymi bazami danych (adres pracy, domu itp.)
5. Ustalenie zwyczajów i harmonogramu ofiary

**Czas wykonania**: od kilku minut do kilku godzin
**Prawdopodobieństwo wykrycia**: zero (brak rejestrowania uwierzytelnienia)

### Scenariusz 4: manipulowanie dowodami

**Podmiot zagrażający**: oskarżony w sprawie karnej

**Cel**: zniszczenie dowodów przed rozprawą

**Metoda**:
1. Poznanie lokalizacji kamery z dokumentów uzyskanych na podstawie nakazu
2. Fizyczny dostęp do kamery (sekwencja naciśnięć przycisku)
3. Uzyskanie powłoki root
4. Przejście do katalogu z dowodami
5. Usunięcie wybranych obrazów lub nagrań albo zmiana znaczników czasu

**Czas wykonania**: poniżej pięciu minut
**Prawdopodobieństwo wykrycia**: niskie (chyba że kamera zostanie poddana analizie kryminalistycznej przed dostępem obrony)

### Scenariusz 5: działacz na rzecz prywatności lub dziennikarz

**Podmiot zagrażający**: rzecznik przejrzystości

**Cel**: udokumentowanie nadużyć w nadzorze

**Metoda**:
1. Użycie urządzeń wykrywających (zob. nasz [sprzętowy przewodnik Flock-You](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))
2. Sporządzenie mapy kamer w społeczności
3. Złożenie wniosków FOIA o zasady przechowywania nagrań
4. Zademonstrowanie podatności radzie miasta
5. Działania na rzecz usunięcia kamer lub wprowadzenia nadzoru

**Czas wykonania**: ciągłe
**Prawdopodobieństwo wykrycia**: wysokie (działania publiczne)

______

{{< figure src="flock-camera-attack-scenario-threat-actor-matrix-nation-state-crime.webp" alt="Macierz porównująca pięć rzeczywistych scenariuszy ataku na kamery Flock Safety: nadzór państwa obcego, kontrnadzór przestępczy, prześladowanie, manipulowanie dowodami i działania na rzecz prywatności" >}}

______

## Jak chronić się przed tymi podatnościami

### Dla organów ścigania

**Natychmiastowe działania**:
1. **Wymagaj MFA/2FA** dla wszystkich użytkowników (klucze bezpieczeństwa USB)
2. **Audytuj dzienniki dostępu** co miesiąc pod kątem nieautoryzowanych zapytań
3. **Ogranicz udostępnianie** do niezbędnych jurysdykcji
4. **Izoluj sieć**: umieść kamery w dedykowanych sieciach VLAN
5. **Zabezpiecz fizycznie**: używaj plomb wskazujących na naruszenie i monitoruj kamery
6. **Przygotuj plan reagowania na incydent** przejęcia

**Wymagania umowne**:
1. **Regularne audyty bezpieczeństwa** niezależnych firm
2. **Obowiązkowe aktualizacje oprogramowania układowego** w ciągu 30 dni od wydania poprawki
3. **Powiadomienie o CVE** w ciągu 24 godzin
4. **Szyfrowanie dowodów w spoczynku** z kluczami zarządzanymi przez klienta
5. **Kary SLA** za naruszenia bezpieczeństwa
6. **Prawo do audytu** zakładów i kodu dostawcy

**Strategia długoterminowa**:
1. **Plan migracji** z systemów operacyjnych po zakończeniu wsparcia
2. **Infrastruktura hostowana samodzielnie** (mniejsza zależność od chmury)
3. **Ocena alternatyw o otwartym kodzie źródłowym**
4. **Przejrzystość wobec społeczności** w sprawie lokalizacji kamer i zasad

### Dla Flock Safety (zalecenia)

**Priorytet krytyczny** (natychmiast):
1. **Wyłącz tworzenie bezprzewodowego punktu dostępowego** po naciśnięciu przycisku
2. **Wymuś MFA** dla wszystkich kont użytkowników, bez wyjątków
3. **Zmień wszystkie dane uwierzytelniające** zapisane na stałe w całym systemie
4. **Pilnie załataj** publicznie dostępne interfejsy
5. **Szyfruj dane w spoczynku** i właściwie zarządzaj kluczami

**Wysoki priorytet** (30 dni):
1. **Przejdź na wspierany system operacyjny** (Android 12+ lub Linux)
2. **Uruchom program bug bounty** bez umów o zachowaniu poufności
3. **Zleć audyt bezpieczeństwa stronie trzeciej** i opublikuj wyniki
4. **Szyfruj ruch sieciowy** od końca do końca
5. **Popraw zabezpieczenia fizyczne** (usuń odsłonięte USB, wzmocnij obudowy)

**Średni priorytet** (90 dni):
1. **Przeprojektuj system uwierzytelniania**
2. **Zabezpiecz rozruch** przy użyciu zweryfikowanego oprogramowania układowego
3. **Zintegruj sprzętowy moduł bezpieczeństwa**
4. **Uzyskaj certyfikaty zgodności** (FedRAMP, SOC 2, ISO 27001)
5. **Udostępnij klientom panel bezpieczeństwa** z powiadomieniami o naruszeniach

**Długoterminowo** (rok):
1. **Udostępnij komponenty bezpieczeństwa jako open source** (by budować zaufanie)
2. **Prowadź program testów adwersarialnych** (red team)
3. **Ustal wymagania dla stanowisk inżynierii bezpieczeństwa**
4. **Włącz praktyki bezpieczeństwa do SDLC** (DevSecOps)
5. **Bierz udział w tworzeniu standardów branżowych** (OWASP, CIS)

### Dla osób prywatnych

**Sposoby ochrony**:
1. **Używaj urządzeń wykrywających** (zob. nasz [sprzętowy przewodnik](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))
2. **Sporządź mapę kamer** w swojej okolicy
3. **Zmieniaj trasy i pory podróży**, by utrudnić analizę wzorców
4. **Domagaj się nadzoru i przejrzystości** na posiedzeniach rady miasta
5. **Składaj wnioski FOIA** o własne dane (gdy pozwala na to prawo)
6. **Wspieraj przepisy dotyczące prywatności** na poziomie stanowym i federalnym

**Środki bezpieczeństwa operacyjnego (OpSec)**:
1. **Unikaj nietypowych pojazdów** (popularna marka, model i kolor)
2. Korzystaj z **innych pojazdów** podczas wrażliwych działań (jeśli to legalne)
3. Wybieraj **alternatywne środki transportu** (rower, komunikacja publiczna, pieszo)
4. Używaj **osłon tablic chroniących prywatność** (tylko jeśli są legalne w danej jurysdykcji)
5. Używaj **toreb Faradaya** do telefonów, gdy istnieje ryzyko korelacji danych

{{< stscollective-ad "flockyou" >}}

______

{{< figure src="flock-safety-security-remediation-priority-roadmap.webp" alt="Priorytetowa mapa drogowa napraw pokazująca poprawki, które Flock Safety powinien wdrożyć natychmiast oraz w ciągu 30 i 90 dni i w dłuższej perspektywie, by usunąć krytyczne podatności" >}}

______

## Zespół badawczy

### GainSec (Jon „GainSec” Gaines)

**Doświadczenie**: specjalista ds. bezpieczeństwa ofensywnego, ponad 10 lat praktyki

**Wkład**:
- Odkrył **47 z 51** podatności
- Opublikował **formalną białą księgę** ze szczegółami technicznymi
- Koordynował z Flock Safety **odpowiedzialne ujawnianie**
- Zarejestrował **30 CVE** (22 opublikowane, 8 oczekujących)
- Opracował **listę kontrolną obrońcy** dla specjalistów bezpieczeństwa

**Kontakt**: whitepaper@gainsecmail.com
**Badania**: [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)
**Blog**: [gainsec.com](https://gainsec.com)

### Ben Jordan (Benn Jordan)

**Doświadczenie**: dziennikarz, muzyk, badacz technologii

**Wkład**:
- **Nagrania wideo** dokumentujące podatności
- **Publiczne demonstracje** dla dziennikarzy (The Guardian, 404 Media)
- Odkrycie przez Google **ponad 60 publicznie dostępnych obrazów z kamer**
- **Działania rzecznicze i edukacja społeczna**
- **Współpraca legislacyjna** z biurami senatorów

**Kontakt**: przez kanał YouTube
**Prace**: YouTube - Benn Jordan

### Joshua Michael (Next AI)

**Doświadczenie**: specjalista OSINT i badacz prywatności

**Wkład**:
- Odkrył **ujawnione klucze API** za pomocą zaawansowanych wyszukiwań Google
- Udokumentował **ujawnione warstwy ArcGIS**
- Opracował **metody OSINT** do śledzenia badań
- **Skorelował dane** z publicznymi wyciekami

**Organizacja**: Next AI - firma zajmująca się analizą informacji ze wszystkich źródeł

### Pozostali współtwórcy

- **404 Media** - dziennikarstwo śledcze i publiczne ujawnianie
- **The Guardian** - zasięg międzynarodowy
- **Lucy Parsons Labs** - wieloletnie działania i badania dotyczące ALPR
- **Sassy South** - organizowanie społeczności
- **DeFlock / Will Freeman** - projekt mapowania lokalizacji kamer
- **Ed Vogel** - analiza prawna i polityczna

______

## Kwestie etyczne

### Harmonogram odpowiedzialnego ujawniania

Społeczność bezpieczeństwa przestrzegała dobrych praktyk **odpowiedzialnego ujawniania**:

**Standardowa procedura**:
1. Odkrycie podatności
2. **Prywatne powiadomienie dostawcy z 90-dniowym wyprzedzeniem**
3. Dostawca opracowuje i wdraża poprawkę
4. **Publiczne ujawnienie** po poprawce lub po 90 dniach (w zależności od tego, co nastąpi wcześniej)
5. Szczegółowy opis pomagający w obronie

**Rzeczywisty przebieg**:
1. GainSec odkrył podatności (koniec 2024 roku)
2. **Wielokrotnie kontaktował się** z Flock Safety (od lutego 2025 roku)
3. Flock zaoferował **bug bounty z umową o zachowaniu poufności** (próbując uciszyć badacza)
4. Flock **przedwcześnie wydał oświadczenie PR**, nie uznając wkładu badacza
5. **Nie potwierdzono**, że wdrożono poprawki
6. GainSec przystąpił do **publicznego ujawnienia** po upływie 90-dniowych terminów
7. Ben Jordan i 404 Media **niezależnie zweryfikowali** podatności w systemach produkcyjnych

### Odwet wobec badaczy

GainSec i Ben Jordan zgłosili:
- **Utratę pracy** lub problemy zawodowe
- **Wizyty policji** w prywatnych domach
- **Podejrzenie obserwacji** domów i posesji
- **Nękanie przez sąsiadów**
- **Groźby prawne**
- **Ataki w mediach społecznościowych** (dyrektor generalny Flock nazwał ich „terrorystami”)

Ten **efekt mrożący** dla badań bezpieczeństwa:
- Zniechęca do ujawniania podatności
- Opóźnia krytyczne poprawki bezpieczeństwa
- Szkodzi bezpieczeństwu publicznemu
- Narusza normy etyczne społeczności bezpieczeństwa

*Odpowiedź Flock Safety wobec badaczy przestrzegających procedur ujawniania tworzy niebezpieczny precedens dla całej społeczności badawczej.*

Cytat Bena Jordana:
> „Nie mam możliwości poświęcić kolejnych miesięcy na jeszcze jedną podatność Flock Safety. Jak widać, ta jest pilna i szczerze mówiąc, obawiam się, że ktoś już ją wykorzystuje.”

### Interes publiczny

Badacze działali **w interesie publicznym**, ponieważ:
- **Przestrzegali procedur odpowiedzialnego ujawniania**
- **Najpierw powiadomili dostawcę**, przed publicznym ujawnieniem
- **Usunęli wrażliwe szczegóły**, które ułatwiałyby wykorzystanie podatności
- **Przekazali wskazówki obronne** specjalistom
- **Zabiegali o zmianę polityki** właściwymi kanałami
- **Podjęli osobiste ryzyko**, by poinformować opinię publiczną

Bez ich pracy:
- **Ponad 80 000 podatnych kamer** pozostałoby bez zmian
- **Ponad 150 mln codziennych skanów pojazdów** nie byłoby chronionych
- **Miliony Amerykanów** pozostawałyby narażone bez swojej wiedzy
- **Bezpieczeństwo narodowe** byłoby zagrożone
- **Nie podjęto by działań legislacyjnych**

______

## Wnioski: dalsze działania

{{< figure src="flock-safety-vulnerability-disclosure-timeline-2026.webp" alt="Schemat osi czasu procesu ujawniania podatności Flock Safety w latach 2024–2026: od pierwszego odkrycia, przez odpowiedzialne ujawnienie, po trwające nienaprawione zagrożenie" >}}

### Obecny stan (maj 2026 roku)

- Udokumentowano i częściowo ujawniono **ponad 50 krytycznych podatności**
- **Ponad 80 000 kamer** nadal działa z nienaprawionymi lukami
- Dostawca nie przeprowadził **kompleksowych napraw**
- **Ograniczone działania regulacyjne** (wniosek o dochodzenie FTC, które jednak się nie rozpoczęło)
- **Utrzymujące się ryzyko wykorzystania** zagrażające bezpieczeństwu narodowemu i prywatności

### Co powinno się wydarzyć

**W całej branży**:
1. **Obowiązkowe audyty bezpieczeństwa** przed wdrożeniem rządowym
2. **Niezależne testy** przeprowadzane przez wykwalifikowane podmioty zewnętrzne
3. **Publiczne ujawnianie** wyników audytów
4. **Odpowiedzialność dostawców** za błędy bezpieczeństwa
5. **Zgodność ze standardami** (NIST, ISO itp.)

**Działania Flock Safety**:
1. **Natychmiastowe poprawki awaryjne** krytycznych podatności
2. **Migracja systemu operacyjnego** na wspieraną platformę
3. **Publiczne potwierdzenie zakresu problemu**
4. **Rekompensata** dla poszkodowanych badaczy
5. **Raportowanie przejrzystości** stanu bezpieczeństwa

**Działania organów ścigania**:
1. **Wymagania bezpieczeństwa** w umowach zakupowych
2. **Regularne audyty** wdrożonych systemów
3. **Obowiązkowe MFA** dla wszystkich użytkowników
4. **Plany reagowania na incydenty**
5. **Przejrzystość wobec społeczności** w sprawie programów nadzoru

**Działania legislacyjne**:
1. **Federalne standardy** dla technologii nadzoru
2. **Wymóg ujawniania podatności** zainteresowanym podmiotom
3. **Ochrona sygnalistów** dla badaczy bezpieczeństwa
4. **Środki cywilnoprawne** w razie naruszeń prywatności
5. **Mechanizmy nadzoru** nad systemami inwigilacji

### Szerszy obraz

To studium przypadku dotyczy **nie tylko Flock Safety**. Pokazuje ono:
- **Branżę nadzoru**, która przedkłada wzrost nad bezpieczeństwo
- **Zakupy rządowe** bez wystarczającej wiedzy technicznej
- **Niezweryfikowane i niepodważane twierdzenia dostawców**
- **Niedopasowane zachęty finansowe** w obszarze bezpieczeństwa publicznego
- **Luki regulacyjne** w nadzorze nad nowymi technologiami

*Każde miasto podpisujące umowę z Flock bez niezależnej weryfikacji bezpieczeństwa akceptuje to ryzyko w imieniu mieszkańców.*

### Wezwanie do działania

**Dla specjalistów bezpieczeństwa**:
- **Wspieraj działania na rzecz odpowiedzialnego ujawniania**
- **Współtwórz narzędzia bezpieczeństwa open source**
- **Zabiegaj o ochronę badaczy**

**Dla organów ścigania**:
- **Wymagaj odpowiedzialności** od dostawców
- **Wymagaj audytów bezpieczeństwa** przed wdrożeniem
- **Natychmiast wprowadź MFA**
- **Konsultuj się ze społecznością bezpieczeństwa**

**Dla decydentów**:
- **Uchwal standardy bezpieczeństwa**
- **Finansuj niezależne audyty** technologii nadzoru
- **Chroń sygnalistów** i badaczy
- **Powołaj organy nadzoru** z wiedzą techniczną

**Dla opinii publicznej**:
- **Dowiedz się więcej o nadzorze** w swojej społeczności
- **Uczestnicz w posiedzeniach rady miasta**, gdy omawiane są umowy
- **Wspieraj organizacje** działające na rzecz przejrzystości
- **Kontaktuj się z przedstawicielami władz** w sprawie swoich obaw
- **Używaj narzędzi wykrywających**, by mapować nadzór (zob. nasz [sprzętowy przewodnik](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))

### Powiązane artykuły

- **[Monitoring Flock Safety: rozpowszechnienie, obawy dotyczące prywatności i sposoby ochrony](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** - poznaj krajobraz nadzoru
- **[Projekt wykrywania Flock-You: sprzętowy przewodnik po przeciwdziałaniu nadzorowi](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** - zbuduj własne urządzenie wykrywające

Oczekiwanie, aż branża naprawi te luki, nie jest strategią ochrony. **[Urządzenia wykrywające FlockYou](https://stscollective.com/collections/flockyou-alpr-flock-safety-awareness-devices)** ze sklepu STS Collective działają już dziś, a kod **SIMEONONSECURITY** daje do 20% zniżki.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Kup wykrywacze FlockYou i oszczędź 20%
{{< /centerbutton >}}

______

## Źródła

1. [Badania GainSec nad ekosystemem przeciwdziałania przestępczości - GitHub](https://github.com/GainSec/anti-crime-ecosystem-research)
2. [Biała księga GainSec - Zenodo DOI: 10.5281/zenodo.17529423](https://zenodo.org/records/17584876)
3. [Blog GainSec - nieformalne analizy techniczne](https://gainsec.com/)
4. [Oficjalna odpowiedź Flock Safety - listopad 2025](https://www.flocksafety.com/blog/response-to-compiled-security-research-on-flock-safety-devices)
5. [404 Media - ujawnione obrazy z kamer Flock](https://www.404media.co/)
6. [YouTube Bena Jordana - demonstracje podatności](https://www.youtube.com/@BennJordan)
7. [National Vulnerability Database](https://nvd.nist.gov/)
8. [Baza danych CVE MITRE](https://cve.mitre.org/)
9. [Electronic Frontier Foundation - nadzór ALPR](https://www.eff.org/issues/automated-license-plate-readers)
10. [List senatora Wydena do FTC](https://www.wyden.senate.gov/)
11. [Lucy Parsons Labs - badania ALPR](https://lucyparsonslabs.com/)
12. [Projekt DeFlock - mapowanie kamer](https://deflockproject.org/)
13. [Distributed Denial of Secrets - obrazy systemu plików kamery ALPR Flock](https://ddosecrets.org/article/flock-alpr-camera)
14. [Micah Lee - kamery Flock są pełne podatności i danych uwierzytelniających zapisanych na stałe](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
15. [WIRED i 404 Media - hakerzy dostali się do wnętrza kamery Flock](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
16. [Hackaday - ten tydzień w bezpieczeństwie: kamery Flock są przestarzałe](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
17. [NVD - CVE-2021-1905, use-after-free w GPU Qualcomm Adreno](https://nvd.nist.gov/vuln/detail/CVE-2021-1905)
18. [NVD - CVE-2018-9568, pomylenie typów gniazd jądra Linux](https://nvd.nist.gov/vuln/detail/CVE-2018-9568)
19. [WiFi Mothership - wykrywanie ALPR Flock Safety i dokumentacja urządzeń](https://wifimothership.com/flock)
20. [CVE.org - wyszukiwarka rekordów programu CVE](https://www.cve.org/)
21. [Alert bezpieczeństwa Flock Safety - wykrywanie wystrzałów i czytniki tablic rejestracyjnych](https://www.flocksafety.com/articles/gunshot-detection-and-license-plate-reader-security-alert)
22. [GainSec - Fly By Device 2: bezprzewodowe RCE Falcon i Sparrow](https://gainsec.com/2025/09/27/fly-by-device-2-the-falcon-sparrow-gated-wireless-rce-camera-feed-dos-information-disclosure-and-more/)
23. [GainSec - Root from the Coop Device 3: powłoka root w module obliczeniowym Bravo Flock Safety](https://gainsec.com/2025/09/19/root-from-the-coop-device-3-root-shell-on-flock-safetys-bravo-compute-box/)
