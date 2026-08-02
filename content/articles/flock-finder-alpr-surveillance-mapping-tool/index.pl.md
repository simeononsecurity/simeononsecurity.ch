---
title: "Flock Finder: Mapa kamer ALPR Flock Safety"
date: 2026-07-22
toc: true
draft: false
description: "Flock Finder to narzędzie open source, które mapuje ponad 40 000 kamer Flock Safety ALPR na całym świecie, korzystając z danych WiFi WiGLE i odcisku palca OUI. Dowiedz się, jak działa, jakie ma ograniczenia i jakie narzędzia sprzętowe służą do wykrywania w czasie rzeczywistym."
genre: ["Technologia prywatności", "Kontrwywiad", "Projekty open source", "Prawa cyfrowe", "Bezpieczeństwo sieci", "Narzędzia prywatności", "Hakowanie sprzętu", "Badania bezpieczeństwa"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "Czytnik tablic rejestracyjnych", "Odcisk palca OUI", "WiGLE", "Inwigilacja WiFi", "Kontrwywiad", "STS Collective", "FlockYou", "ESP32", "Narzędzia prywatności", "NitekryDPaul", "DeFlockJoplin", "Wykrywanie ALPR", "Bezpieczeństwo open source", "Mapowanie inwigilacji", "Masowa inwigilacja", "WiFi OUI", "Ochrona prywatności", "Adres MAC", "Tryb rozgłoszeniowy", "802.11", "Wykrywanie w czasie rzeczywistym", "Wardriving", "Prawa cyfrowe", "Wolności obywatelskie", "Świadomość inwigilacji", "GitHub", "Python"]
cover: "/img/cover/flock-finder-open-source-alpr-camera-map.webp"
coverAlt: "Interaktywna mapa wyświetlająca kolorowe znaczniki wskazujące lokalizacje kamer Flock Safety ALPR, z abstrakcyjnymi sygnałami WiFi emanującymi ze znaczników na ciemnym tle."
coverCaption: "Flock Finder mapuje ponad 40 000 domniemanych kamer Flock Safety ALPR przy użyciu danych WiFi WiGLE i odcisku palca OUI."
canonical: "https://simeononsecurity.com/articles/flock-finder-alpr-surveillance-mapping-tool/"
---

**Narzędzie open source do zwiększania świadomości na temat inwigilacji, które mapuje kamery Flock Safety ALPR przy użyciu crowdsourcingowych danych WiFi.**

## Czym jest Flock Finder?

**[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** to projekt open source, który mapuje **kamery Flock Safety ALPR (Automatyczny Czytnik Tablic Rejestracyjnych)** w Stanach Zjednoczonych i 108 innych krajach. Łączy **31 znanych prefiksów OUI (Organizatorycznie Unikalny Identyfikator) WiFi Flock Safety** z **crowdsourcingową bazą danych WiFi WiGLE**, aby identyfikować i nanosić na mapę interaktywną domniemane lokalizacje kamer.

Projekt znajduje się pod adresem **[github.com/simeononsecurity/flock-finder](https://github.com/simeononsecurity/flock-finder)**, jest automatycznie aktualizowany codziennie za pośrednictwem GitHub Actions i od lipca 2026 roku zmapował **ponad 40 000 domniemanych kamer** w 964 regionach na całym świecie.

| Metryka | Wartość |
|--------|-------|
| **Zmapowane kamery** | 40 026+ |
| **Znane prefiksy OUI** | 31 |
| **Pokryte kraje** | 109 |
| **Pokryte regiony** | 964 |
| **Przechowywanie danych** | 730 dni (2 lata) |
| **Częstotliwość automatycznej aktualizacji** | Codziennie |

*Jest to ogólne narzędzie do zwiększania świadomości, a nie definitywny inwentarz. Przeczytaj sekcję dotyczącą ograniczeń przed wyciąganiem wniosków z danych.*

Aby zapoznać się z tłem dotyczącym tego, dlaczego inwigilacja ALPR Flock Safety jest ważna dla prywatności, przeczytaj **[Inwigilacja kamerami Flock Safety: Rozpowszechnienie, obawy dotyczące prywatności i strategie ochrony](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

______

## Jak to działa: Odcisk palca OUI przez WiGLE

### Kluczowy wgląd

Kamery Flock Safety zawierają **transceivery WiFi**, które okresowo budzą się ze snu, aby przesłać przechwycone dane tablic rejestracyjnych do chmury. Podczas tych krótkich aktywnych okien kamera nadaje ramki WiFi zawierające jej **adres MAC** — a pierwsze trzy bajty każdego adresu MAC identyfikują producenta. To jest **OUI (Organizatorycznie Unikalny Identyfikator)**.

Badacz bezpieczeństwa **@NitekryDPaul** odkrył **30 prefiksów OUI** konsekwentnie powiązanych ze sprzętem kamer Flock Safety poprzez **analizę 2,4 GHz w trybie rozgłoszeniowym**. 31. prefiks (`82:6B:F2`) został wniesiony przez **Michaela / DeFlockJoplin** podczas testów terenowych w Joplin, MO.

Flock Finder bierze te 31 OUI, odpytuje WiGLE o zarejestrowane sieci WiFi pasujące do tych prefiksów i nanosi wyniki na mapę.

### 31 znanych prefiksów OUI Flock Safety

| # | Prefiks OUI | Źródło | # | Prefiks OUI | Źródło |
|---|-----------|--------|---|-----------|--------|
| 1 | **70:C9:4E** | @NitekryDPaul | 17 | **D0:39:57** | @NitekryDPaul |
| 2 | **3C:91:80** | @NitekryDPaul | 18 | **E8:D0:FC** | @NitekryDPaul |
| 3 | **D8:F3:BC** | @NitekryDPaul | 19 | **E0:4F:43** | @NitekryDPaul |
| 4 | **80:30:49** | @NitekryDPaul | 20 | **B8:1E:A4** | @NitekryDPaul |
| 5 | **B8:35:32** | @NitekryDPaul | 21 | **70:08:94** | @NitekryDPaul |
| 6 | **14:5A:FC** | @NitekryDPaul | 22 | **58:8E:81** | @NitekryDPaul |
| 7 | **74:4C:A1** | @NitekryDPaul | 23 | **EC:1B:BD** | @NitekryDPaul |
| 8 | **08:3A:88** | @NitekryDPaul | 24 | **3C:71:BF** | @NitekryDPaul |
| 9 | **9C:2F:9D** | @NitekryDPaul | 25 | **58:00:E3** | @NitekryDPaul |
| 10 | **C0:35:32** | @NitekryDPaul | 26 | **90:35:EA** | @NitekryDPaul |
| 11 | **94:08:53** | @NitekryDPaul | 27 | **5C:93:A2** | @NitekryDPaul |
| 12 | **E4:AA:EA** | @NitekryDPaul | 28 | **64:6E:69** | @NitekryDPaul |
| 13 | **F4:6A:DD** | @NitekryDPaul | 29 | **48:27:EA** | @NitekryDPaul |
| 14 | **F8:A2:D6** | @NitekryDPaul | 30 | **A4:CF:12** | @NitekryDPaul |
| 15 | **24:B2:B9** | @NitekryDPaul | 31 | **82:6B:F2** | DeFlockJoplin |
| 16 | **00:F4:8D** | @NitekryDPaul | | | |

### Technika wykrywania addr1

Kluczowe odkrycie @NitekryDPaul wykracza poza proste dopasowywanie adresu MAC nadajnika. Kamery Flock spędzają większość swojego cyklu pracy **śpiąc**. Gdy pobliski punkt dostępowy wysyła ramkę zaadresowaną *do* kamery, MAC kamery pojawia się jako **addr1 (adres odbiorcy)** w ramkach 802.11 — nawet gdy sama kamera nie nadaje aktywnie.

W połączeniu z **wykrywaniem żądań próbnych z symbolem wieloznacznym** (ramki zarządzania 802.11 typ=0, podtyp=4, puste SSID), daje to bardzo precyzyjny podpis wykrywania. Testy terenowe w Joplin, MO osiągnęły **11 z 12 wykrytych kamer przy zaledwie 2 fałszywych alarmach**.

> ⚠️ **Ważne**: Mapa Flock Finder oparta na WiGLE **nie** implementuje techniki addr1. WiGLE to historyczny, pasywnie zbierany zestaw danych — rejestruje tylko nadajniki, nie odbiorniki. W przypadku wykrywania w czasie rzeczywistym, które faktycznie używa metody @NitekryDPaula, potrzebny jest dedykowany sprzęt działający w terenie.

______

## Korzystanie z mapy na żywo

Interaktywna mapa jest dostępna na **[simeononsecurity.github.io/flock-finder/](https://simeononsecurity.github.io/flock-finder/)**. Wyświetla:

- **Pogrupowane znaczniki kamer** zakodowane kolorami według prefiksu OUI
- **Wyszukiwanie** według miasta, stanu lub BSSID
- **Tabela danych OUI** z liczbami kamer dla każdego prefiksu
- **Panel statystyk** pokazujący całkowitą liczbę kamer, regiony i znacznik czasu ostatniej aktualizacji
- **Strona o ALPR** z udokumentowanymi szkodami dla prywatności, kontekstem prawnym i zasobami społeczności

Eksporty danych mapy są również dostępne bezpośrednio:

- `data/flock_cameras.geojson` — GeoJSON do użytku w QGIS, Leaflet lub innych narzędziach
- `data/flock_cameras.csv` — format przyjazny arkuszom kalkulacyjnym
- `data/scan_stats.json` — statystyki i liczby skanowania

### Kluczowe ograniczenia

**Podchodź do mapy z rezerwą.** WiGLE to crowdsourcingowy, sporadycznie aktualizowany zestaw danych, a nie transmisja na żywo.

- **Kamery Flock nie nadają nieprzerwanie.** Budzą się na krótko, aby przesłać dane, więc rekordy WiGLE zależą całkowicie od tego, że wardiver jest w pobliżu dokładnie we właściwym momencie.
- **Dane mogą mieć wiele miesięcy lub lat.** Kamery, które zostały przeniesione lub usunięte, mogą nadal być widoczne.
- **Dopasowywanie OUI jest heurystyką.** OUI mogą być współdzielone, ponownie przypisywane lub sfałszowane. Każdy wynik to *domniemane* urządzenie Flock, a nie potwierdzone.
- **Pokrycie jest nierównomierne.** Gęste obszary metropolitalne mają więcej danych WiGLE; obszary wiejskie mają ich znacznie mniej.

*Używaj mapy, aby rozwinąć ogólną świadomość gęstości inwigilacji w swoim okolicy. W przypadku wykrywania w czasie rzeczywistym z danymi z terenu, sprawdź poniższe opcje sprzętowe.*

______

## Uruchamianie Flock Finder samodzielnie

### Wymagania wstępne

- Python 3.8+
- Bezpłatne konto [WiGLE](https://wigle.net/account) z danymi uwierzytelniającymi API

### Konfiguracja

```bash
# Clone the repository
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder

# Install dependencies
pip install -r requirements.txt

# Set up your WiGLE API credentials
cp .env.example .env
# Edit .env with your WiGLE API Name and Token
```

### Uruchamianie skanera

```bash
# Full scan — all 31 OUI prefixes, worldwide
python3 scripts/wigle_query.py

# Single OUI test
python3 scripts/wigle_query.py --oui 70:C9:4E

# US only
python3 scripts/wigle_query.py --country US

# Specific bounding box (lat1,lon1,lat2,lon2)
python3 scripts/wigle_query.py --bbox 37,-97,39,-94

# Dry run — verify auth, no API queries
python3 scripts/wigle_query.py --dry-run
```

### Przeglądanie mapy lokalnie

```bash
python3 -m http.server 8080 --directory docs/
# Open http://localhost:8080 in your browser
```

### Automatyczne codzienne aktualizacje przez GitHub Actions

Rozwidl repozytorium i dodaj swoje dane uwierzytelniające WiGLE jako **sekrety repozytorium** (`WIGLE_API_NAME` i `WIGLE_API_TOKEN`). Dołączony przepływ pracy uruchamia się codziennie o 6:00 UTC i automatycznie zatwierdza zaktualizowane pliki danych za każdym razem, gdy znajdowane są nowe kamery.

______

## Wykrywanie w czasie rzeczywistym: Sprzęt STS Collective FlockYou

Mapa WiGLE mówi ci, gdzie kamery *były obserwowane*. Do wykrywania w czasie rzeczywistym podczas jazdy — przy użyciu rzeczywistej metody dopasowywania OUI @NitekryDPaula na żywym ruchu WiFi — potrzebujesz dedykowanego sprzętu.

**[STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** produkuje przenośne detektory oparte na ESP32, które skanują sygnatury Flock OUI i alarmują cię w momencie wykrycia pasującej sygnatury.

### Linia urządzeń FlockYou

| Urządzenie | Opis |
|--------|-------------|
| **[FlockYou — M5 Atom Lite](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)** | Kompaktowy, kieszonkowy detektor Flock. Wstępnie zaprogramowany, plug-and-play. Alarmy LED przy wykryciu. |
| **FlockYou Pro — LED + Audio** | Dodaje alarmy dźwiękowe obok wskaźników LED. Nigdy nie przegap kamery podczas jazdy. |
| **FlockYou Atom VoiceS3R** | Detektor z obsługą głosową z mówionymi alarmami audio dla obsługi bez rąk, z oczami na drodze. |

Wszystkie urządzenia:
- **Wstępnie zaprogramowane**, gotowe do użycia po wyjęciu z pudełka
- Skanują ruch WiFi na żywo w poszukiwaniu wszystkich 31 znanych OUI Flock
- Kompaktowe i przenośne — mieszczą się w uchwycie na kubek lub kieszeni
- Zasilane przez USB-C (adapter samochodowy, powerbank lub laptop)

> 💰 **Ekskluzywne zniżki**: Użyj kodu **FLOCKFINDER**, aby uzyskać **20% zniżki** na wszystkie urządzenia STS Collective FlockYou — lub użyj kodu **SIMEONONSECURITY**, aby uzyskać do 20% zniżki na całe zamówienie. [Kupuj na stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

Aby uzyskać pełną analizę techniczną tych urządzeń i alternatyw DIY, przeczytaj **[Projekt Wykrywania Flock-You: Kompletny przewodnik po sprzęcie do kontrwywiad i konfiguracji](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**.

______

## Struktura projektu

```
flock-finder/
├── scripts/
│   └── wigle_query.py        # WiGLE API query and data pipeline
├── data/
│   ├── flock_ouis.csv         # 31 known Flock Safety OUI prefixes
│   ├── flock_cameras.geojson  # Camera locations (GeoJSON)
│   ├── flock_cameras.csv      # Camera locations (CSV)
│   └── scan_stats.json        # Scan statistics
├── docs/
│   └── index.html             # Interactive Leaflet map
└── .github/workflows/
    └── update-data.yml        # Daily auto-update workflow
```

______

## Często zadawane pytania

### Czy to jest legalne?

Tak. **Flock Finder używa wyłącznie publicznie dostępnych danych** z bazy danych WiGLE, która agreguje dobrowolnie przekazywane dane z ankiet WiFi. Nie jest zaangażowane żadne hakowanie, nieautoryzowany dostęp ani systemy zastrzeżone. Pasywne monitorowanie WiFi pod kątem sygnatur OUI jest legalne w Stanach Zjednoczonych.

### Czy każda zmapowana kamera to na pewno kamera Flock?

Nie. Dopasowywanie OUI to **heurystyka**. Prefiksy OUI mogą być współdzielone między producentami, ponownie przypisywane lub fałszowane. Każdy rekord w bazie danych to *domniemane* urządzenie Flock — niezatwierdzone. Przeczytaj [Politykę danych](https://github.com/simeononsecurity/flock-finder/blob/main/docs/data-policy.md), aby uzyskać szczegółowe informacje na temat sposobu żądania korekty.

### Dlaczego niektóre prefiksy OUI nie wyświetlają żadnych kamer?

Pokrycie WiGLE jest nierównomierne. Jeśli żaden wardiver nie przeskanował danego obszaru z aktywnym tym konkretnym OUI, nie będzie żadnych rekordów. *Brak danych nie oznacza braku kamer.*

### Jak aktualne są dane?

Przepływ pracy GitHub Actions uruchamia się codziennie i pobiera najnowsze wyniki WiGLE. Jednak sam WiGLE może mieć rekordy od kilku dni do kilku lat dla dowolnej lokalizacji. Sprawdź plik `scan_stats.json`, aby zobaczyć znacznik czasu ostatniego skanowania.

### Czy mogę przekazać własne dane z wardriving?

Tak. Prześlij dane z wardriving do [WiGLE](https://wigle.net) — automatycznie zasilają kolejne codzienne skanowanie Flock Finder. Możesz również wnosić prefiksy OUI lub ulepszenia kodu poprzez [Przewodnik po wkładzie](https://github.com/simeononsecurity/flock-finder/blob/main/CONTRIBUTING.md).

______

## Społeczność i powiązane projekty

Flock Finder nie działa w samotności. Rosnący ekosystem narzędzi i organizacji pracuje nad dokumentowaniem i zwalczaniem inwigilacji ALPR:

- **[DeFlock.org](https://deflockjoplin.org/)** — Sterowane przez społeczność śledzenie ALPR, dokumentacja i rzecznictwo
- **[Have I Been Flocked?](https://haveibeenflocked.com/)** — Sprawdź, czy twój numer rejestracyjny był wyszukiwany w systemie Flock
- **[FlockHopper](https://flockhopper.com/)** — Planowanie tras omijających znane kamery ALPR
- **[Atlas of Surveillance (EFF)](https://atlasofsurveillance.org/)** — Baza danych EFF o technologii inwigilacji stosowanej przez organy ścigania
- **[NoALPRs.com](https://noalprs.com/)** — Zasoby dla społeczności walczących z wdrożeniami ALPR
- **[DeFlockJoplin](https://deflockjoplin.org/)** — Oprogramowanie sprzętowe open source i badania terenowe; wniósł 31. prefiks OUI

______

## Podziękowania

- **Badania OUI**: @NitekryDPaul — wszystkie 30 oryginalnych prefiksów OUI i strategia wykrywania addr1/tryb rozgłoszeniowy
- **Testy terenowe**: Michael / DeFlockJoplin — 31. prefiks OUI (`82:6B:F2`) i zaostrzanie sondy z symbolem wieloznacznym
- **Źródło danych**: [WiGLE](https://wigle.net) — crowdsourcingowa baza danych WiFi/sieci komórkowych
- **Zainspirowane przez**: [DeFlock](https://deflockjoplin.org/) i track-openroaming-passpoint
- **Partner sprzętowy**: [STS Collective](https://stscollective.com/discount/SIMEONONSECURITY) — detektory FlockYou ESP32

______

## Podsumowanie

**Flock Finder** daje każdemu szybkie, wizualne pojęcie o tym, jak szeroko rozmieszczono kamery Flock Safety ALPR — ponad 40 000 szacowanych lokalizacji w 109 krajach, automatycznie aktualizowanych każdego dnia na podstawie crowdsourcingowych danych WiFi.

Jest to **narzędzie przejrzystości**, a nie tracker na żywo. Jego dane są historyczne, niekompletne i probabilistyczne. Ale czyni skalę inwigilacji ALPR widoczną w sposób, w jaki streszczenia i raporty nie mogą.

W przypadku prawdziwej ochrony w czasie rzeczywistym podczas poruszania się po nadzorowanych obszarach, połącz mapę z dedykowanym sprzętem. **[Urządzenia FlockYou STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** implementują metodę wykrywania @NitekryDPaula bezpośrednio na ESP32 i alarmują cię w momencie wykrycia sygnatury kamery na żywo — dostępne na **[stscollective.com](https://stscollective.com/discount/SIMEONONSECURITY)** z kodem **FLOCKFINDER** lub **SIMEONONSECURITY** za do 20% zniżki.

### Powiązane artykuły

| Artykuł | Co obejmuje |
|---------|---------------|
| **[Inwigilacja kamerami Flock Safety: Prywatność i ochrona](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Pełny obraz: statystyki rozpowszechnienia, kwestie wolności obywatelskich, zestaw narzędzi ACLU, statystyki DeFlock, przewodnik FOIA i strategie ochrony |
| **[Projekt Wykrywania Flock-You: Przewodnik po sprzęcie do kontrwywiad](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Kompletny przewodnik techniczny po detektorach Flock opartych na ESP32 — OUI-SPY, M5 Atom Lite, budowa DIY, konfiguracja oprogramowania sprzętowego krok po kroku |
| **[Jak zaprogramować urządzenia Rayhunter: Kompletny przewodnik](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Wykrywanie chwytaczy IMSI (symulatorów stacji bazowych komórkowych) obok kamer ALPR dla pełnej świadomości kontrwywiadowczej |
| **[Niestandardowe oprogramowanie sprzętowe DagShell dla Orbic RCL400](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | Przekształcenie mobilnego hotspota w platformę do badań bezpieczeństwa — dobrze współpracuje ze sprzętem do wykrywania Flock |
| **[Porównanie urządzeń Rayhunter 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Porównanie opcji sprzętu do wykrywania w kategoriach zagrożeń ALPR i komórkowym inwigilacji |

______

## Referencje

1. [Repozytorium GitHub Flock Finder](https://github.com/simeononsecurity/flock-finder)
2. [Interaktywna mapa Flock Finder](https://simeononsecurity.github.io/flock-finder/)
3. [STS Collective — Urządzenia FlockYou](https://stscollective.com/discount/SIMEONONSECURITY)
4. [WiGLE — Mapowanie sieci bezprzewodowych](https://wigle.net)
5. [DeFlock — Świadomość ALPR w społeczności](https://deflockjoplin.org/)
6. [DeFlockJoplin — Oprogramowanie sprzętowe do wykrywania open source](https://deflockjoplin.org/)
7. [Electronic Frontier Foundation — ALPR](https://www.eff.org/issues/automated-license-plate-readers)
8. [ACLU — Jesteś śledzony](https://www.aclu.org/issues/privacy-technology/location-tracking/you-are-being-tracked)
