---
title: "Kompletny przewodnik: instalacja GrapheneOS na urządzeniu Google Pixel"
draft: false
toc: true
date: 2023-05-21
lastmod: 2026-05-24
description: "Dowiedz się, jak zainstalować GrapheneOS na urządzeniu Google Pixel, aby zwiększyć prywatność i bezpieczeństwo, korzystając z instalatora internetowego lub metody CLI."
tags: ["GrapheneOS", "Google Pixel", "prywatność", "bezpieczeństwo", "Android", "urządzenia mobilne", "system operacyjny", "przewodnik instalacji", "niestandardowy ROM", "ochrona danych", "bezpieczny system", "open source", "fastboot", "bootloader", "zweryfikowane uruchamianie", "Pixel 10", "Pixel 9"]
cover: "/img/cover/how-to-install-graphine-os.webp"
coverAlt: "Abstrakcyjna cyfrowa ilustracja przedstawiająca smartfon Google Pixel podłączony do komputera kablem USB-C, otoczony kolorowymi elementami graficznymi symbolizującymi transfer danych i bezpieczeństwo."
coverCaption: ""
---

**Jak zainstalować GrapheneOS na urządzeniu Google Pixel**

GrapheneOS to otwartoźródłowy, zorientowany na prywatność system operacyjny oparty na Androidzie. Oferuje znacznie ulepszone zabezpieczenia i ochronę prywatności, co czyni go doskonałym wyborem dla każdego, kto dba o prywatność i bezpieczeństwo danych. Jeśli posiadasz obsługiwane urządzenie Google Pixel i chcesz przejść na GrapheneOS, ten przewodnik obejmuje zarówno zalecaną metodę **instalatora internetowego**, jak i tradycyjną metodę **wiersza poleceń (CLI)**.

> **Wskazówka:** Jeśli napotkasz problemy podczas instalacji, poproś o pomoc na [oficjalnym kanale czatu GrapheneOS](https://grapheneos.org/contact#community). Przed prośbą o pomoc spróbuj samodzielnie postępować zgodnie z przewodnikiem, a następnie zapytaj o konkretne problemy.

## Wymagania wstępne

### Wymagania sprzętowe i systemowe

- Komputer z co najmniej **2 GB wolnej pamięci RAM** i **32 GB wolnego miejsca na dysku**.
- **Wysokiej jakości kabel USB-C** dołączony do urządzenia (lub kabel USB-C na USB-A, jeśli potrzebny). Unikaj hubów USB — podłącz bezpośrednio do tylnego portu komputera stacjonarnego lub portu laptopa.
- Instalacja z maszyny wirtualnej **nie jest zalecana** ze względu na zawodne przekazywanie USB.

> Dobrą praktyką jest aktualizacja urządzenia Pixel przed instalacją GrapheneOS, aby mieć najnowsze oprogramowanie układowe. W każdym razie GrapheneOS wgrywa najnowsze oprogramowanie układowe na początku procesu instalacji.

### Oficjalnie obsługiwane systemy operacyjne

#### Instalator internetowy

- Windows 10 / Windows 11
- macOS Sonoma (14), macOS Sequoia (15), macOS Tahoe (26)
- Arch Linux
- Debian 12 (bookworm), Debian 13 (trixie)
- Ubuntu 22.04 LTS, Ubuntu 24.04 LTS, Ubuntu 25.04
- Linux Mint 21 (postępuj zgodnie z instrukcjami Ubuntu 22.04 LTS), Linux Mint 22 (postępuj zgodnie z instrukcjami Ubuntu 24.04 LTS)
- Linux Mint Debian Edition 6 (postępuj zgodnie z instrukcjami Debian 12)
- ChromeOS
- GrapheneOS
- Android 13, 14, 15 i 16 z certyfikatem Play Protect

#### Metoda CLI

Wszystkie powyższe oprócz ChromeOS, GrapheneOS i Androida (mogą używać tylko instalatora internetowego).

Można też używać starszych, niewspieranych wersji tych platform, ale nie są one oficjalnie obsługiwane. **Przed kontynuowaniem upewnij się, że system operacyjny jest aktualny.**

### Oficjalnie obsługiwane przeglądarki (tylko instalator internetowy)

- **Chromium** (poza Ubuntu — ich pakiet Snap nie obsługuje WebUSB)
- **Vanadium** (GrapheneOS)
- **Google Chrome**
- **Microsoft Edge**
- **Brave** (z wyłączonymi Brave Shields — ograniczają użycie pamięci, aby uniknąć fingerprintingu)

> - Na Androidzie **wyłącz tryb pulpitu** w przeglądarce. Tryb pulpitu uniemożliwia instalatorowi internetowemu wykrycie Androida i żądanie uprawnienia do ponownego podłączenia po ponownych uruchomieniach. Jest domyślnie włączony na dużych tabletach z 8 GB+ RAM (np. Pixel Tablet).
> - Unikaj wersji przeglądarek Flatpak i Snap — powodują problemy podczas instalacji.
> - **Nie używaj** trybu incognito/przeglądania prywatnego — te tryby ograniczają miejsce na dysku potrzebne do rozpakowania pobranego wydania.

### Obsługiwane urządzenia

Potrzebujesz jednego z [oficjalnie obsługiwanych urządzeń Pixel](https://grapheneos.org/faq#supported-devices). **Unikaj wariantów operatorskich** — Pixele operatorskie mają niezerowe ID operatora zapisane fabrycznie, co wyłącza odblokowanie bootloadera i operatora. Kup urządzenie niezwiązane z operatorem (odblokowane).

---

## Włączanie odblokowywania OEM

Odblokowanie OEM musi być włączone z poziomu systemu operacyjnego przed kontynuowaniem.

1. Przejdź do **Ustawienia → Informacje o telefonie/tablecie** i wielokrotnie stuknij **Numer kompilacji**, aż zostanie włączony tryb programisty.
2. Przejdź do **Ustawienia → System → Opcje programisty** i włącz **Odblokowywanie OEM**. Na niektórych SKU z możliwościami operatorskimi wymaga to aktywnego połączenia internetowego, aby stock OS mógł zweryfikować, że urządzenie nie było sprzedawane jako zablokowane przez operatora.

> **Uwaga dotycząca Pixel 6a:** Odblokowanie OEM nie będzie działać z fabryczną wersją oprogramowania. Zaktualizuj do wydania z **czerwca 2022** lub nowszego przez OTA, a następnie wykonaj reset do ustawień fabrycznych, aby naprawić odblokowanie OEM.

---

## Metoda instalacji 1: instalator internetowy (zalecana)

[Instalator internetowy GrapheneOS](https://grapheneos.org/install/web) jest zalecanym podejściem dla większości użytkowników. Używa WebUSB bezpośrednio w przeglądarce — nie wymaga instalacji żadnego oprogramowania.

### Krok 1: Ominięcie błędów fwupd (tylko Linux)

W systemie Linux wiadomo, że `fwupd` nieprawidłowo łączy się z urządzeniami używającymi protokołu fastboot, blokując instalator. Zatrzymaj go przed podłączeniem urządzenia:

```bash
sudo systemctl stop fwupd.service
```

To nie jest trwałe po ponownym uruchomieniu.

### Krok 2: Konfiguracja reguł udev (tylko Linux)

Na Arch Linux:

```bash
sudo pacman -S android-udev
```

Na Debianie i Ubuntu:

```bash
sudo apt install android-sdk-platform-tools-common
```

### Krok 3: Uruchamianie w interfejsie bootloadera

Przytrzymaj przycisk **zmniejszania głośności** podczas uruchamiania urządzenia (włącz z wyłączonego stanu przytrzymując zmniejszanie głośności lub uruchom ponownie i przytrzymaj). Urządzenie musi wyświetlić **czerwony trójkąt ostrzegawczy** i napis **"Fastboot Mode"** — nie naciskaj przycisku zasilania, aby aktywować "Start."

### Krok 4: Podłącz urządzenie

Podłącz urządzenie do komputera przez USB. W systemie Linux ponownie podłącz kabel, jeśli reguły udev nie były skonfigurowane przed pierwszym podłączeniem.

> **Pixel Tablet:** Odłącz od stacji dokującej przed podłączeniem przez USB — tablet nie może używać obu jednocześnie.

> **Windows:** Aktualne Windows 10/11 zawierają ogólny sterownik fastboot dla Pixel 4a (5G) i nowszych. Dla starszych Pixeli lub przestarzałego systemu Windows zainstaluj sterownik z Windows Update (szukaj w "Wyświetl opcjonalne aktualizacje" → "LeMobile Android Device").

### Krok 5: Odblokowanie bootloadera

Przejdź do [https://grapheneos.org/install/web](https://grapheneos.org/install/web) i kliknij przycisk **Unlock the bootloader**. Potwierdź na urządzeniu przyciskami głośności do zmiany wyboru i przyciskiem zasilania do potwierdzenia. **Spowoduje to wyczyszczenie wszystkich danych.**

### Krok 6: Pobieranie i wgrywanie obrazów fabrycznych

1. Kliknij **Download release**, aby pobrać obrazy fabryczne dla twojego urządzenia.
2. Kliknij **Flash factory images** i poczekaj na zakończenie. Automatycznie wgra oprogramowanie układowe, uruchomi ponownie w interfejsie bootloadera i wgra system operacyjny. **Nie obsługuj urządzenia do czasu zakończenia.**

### Krok 7: Zablokowanie bootloadera

Po wgraniu kliknij **Lock the bootloader** w instalatorze internetowym. Potwierdź na urządzeniu. **Spowoduje to ponowne wyczyszczenie wszystkich danych** — zablokowanie bootloadera włącza pełne zweryfikowane uruchamianie.

---

## Metoda instalacji 2: wiersz poleceń (CLI)

### Krok 1: Otwórz terminal

W systemie Windows otwórz **zwykłe (nie-administratorskie) okno PowerShell**. Usuń starszy alias `curl`:

```powershell
Remove-Item Alias:Curl
```

### Krok 2: Instalacja fastboot

Potrzebujesz fastboot w wersji **≥ 35.0.1**.

**Arch Linux:**

```bash
sudo pacman -S android-tools
```

**Debian / Ubuntu** — ich pakiety są nieaktualne. Użyj samodzielnego wydania:

```bash
# Debian / Ubuntu
sudo apt install libarchive-tools
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-linux.zip
echo 'acfdcccb123a8718c46c46c059b2f621140194e5ec1ac9d81715be3d6ab6cd0a  platform-tools_r35.0.2-linux.zip' | sha256sum -c
bsdtar xvf platform-tools_r35.0.2-linux.zip
export PATH="$PWD/platform-tools:$PATH"
```

**macOS:**

```bash
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-darwin.zip
echo 'SHA256 (platform-tools_r35.0.2-darwin.zip) = 1820078db90bf21628d257ff052528af1c61bb48f754b3555648f5652fa35d78' | shasum -c
tar xvf platform-tools_r35.0.2-darwin.zip
export PATH="$PWD/platform-tools:$PATH"
```

**Windows:**

```powershell
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-win.zip
(Get-FileHash platform-tools_r35.0.2-win.zip).hash -eq "2975a3eac0b19182748d64195375ad056986561d994fffbdc64332a516300bb9"
tar xvf platform-tools_r35.0.2-win.zip
$env:Path = "$pwd\platform-tools;$env:Path"
```

Zweryfikuj wersję:

```bash
fastboot --version
# Oczekiwane: fastboot version 35.0.2-12147458
```

### Krok 3: Konfiguracja reguł udev (tylko Linux)

Arch Linux:

```bash
sudo pacman -S android-udev
```

Debian / Ubuntu:

```bash
sudo apt install android-sdk-platform-tools-common
```

### Krok 4: Ominięcie błędów fwupd (tylko Linux)

```bash
sudo systemctl stop fwupd.service
```

### Krok 5: Uruchamianie w interfejsie bootloadera

Przytrzymaj **zmniejszanie głośności** podczas uruchamiania, aż urządzenie wyświetli **"Fastboot Mode"** z czerwonym trójkątem ostrzegawczym.

### Krok 6: Podłącz i odblokuj bootloader

Podłącz przez USB, a następnie uruchom:

```bash
fastboot flashing unlock
```

Potwierdź na urządzeniu (przyciski głośności do wyboru, przycisk zasilania do potwierdzenia). **Spowoduje to wyczyszczenie wszystkich danych.**

### Krok 7: Instalacja OpenSSH (do weryfikacji obrazów)

macOS i Windows domyślnie zawierają OpenSSH.

Arch Linux:

```bash
sudo pacman -S openssh
```

Debian / Ubuntu:

```bash
sudo apt install openssh-client
```

### Krok 8: Pobieranie i weryfikacja obrazów fabrycznych

Pobierz klucz podpisywania:

```bash
curl -O https://releases.grapheneos.org/allowed_signers
```

Oczekiwana zawartość:

```
contact@grapheneos.org ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIUg/m5CoP83b0rfSCzYSVA4cw4ir49io5GPoxbgxdJE
```

Pobierz obrazy fabryczne (zastąp `DEVICE_NAME` i `VERSION` rzeczywistymi wartościami):

```bash
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip.sig
```

Zweryfikuj podpis (Linux / macOS):

```bash
ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" \
  -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip
```

Windows:

```powershell
cmd /c 'ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip'
```

Oczekiwane wyjście:

```
Good "factory images" signature for contact@grapheneos.org with ED25519 key SHA256:AhgHif0mei+9aNyKLfMZBh2yptHdw/aN7Tlh/j2eFwM
```

### Krok 9: Wgrywanie obrazów fabrycznych

Rozpakuj obrazy:

```bash
# Linux
bsdtar xvf DEVICE_NAME-install-VERSION.zip

# macOS / Windows
tar xvf DEVICE_NAME-install-VERSION.zip
```

Wejdź do katalogu i uruchom skrypt wgrywania:

```bash
cd DEVICE_NAME-install-VERSION

# Linux / macOS
bash flash-all.sh

# Windows
./flash-all.bat
```

Poczekaj na zakończenie procesu. Automatycznie obsługuje wgrywanie oprogramowania układowego, ponowne uruchomienia bootloadera i wgrywanie systemu operacyjnego. **Nie obsługuj urządzenia do czasu zakończenia.**

> **Rozwiązywanie problemów z tmpfs w Linux:** Jeśli `/tmp` nie ma wystarczająco dużo miejsca, użyj:
> ```bash
> mkdir tmp && TMPDIR="$PWD/tmp" ./flash-all.sh
> ```

### Krok 10: Zablokowanie bootloadera

```bash
fastboot flashing lock
```

Potwierdź na urządzeniu. **Spowoduje to ponowne wyczyszczenie wszystkich danych.** Zablokowanie włącza pełne zweryfikowane uruchamianie i uniemożliwia fastboot modyfikowania partycji.

---

## Po instalacji

### Uruchamianie

Naciśnij przycisk zasilania z wybraną domyślną opcją **Start** w interfejsie bootloadera, aby uruchomić GrapheneOS.

### Wyłączanie odblokowywania OEM

Podczas pierwszej konfiguracji, ostatni ekran zawiera przełącznik odblokowywania OEM (zaznaczony domyślnie — pozostawienie go zaznaczonego **wyłącza** odblokowanie OEM). Jest to zalecane. Możesz to zmienić później w **Opcjach programisty**.

### Weryfikacja instalacji

GrapheneOS wykorzystuje zweryfikowane uruchamianie i sprzętowe zaświadczanie. Zweryfikowane uruchamianie sprawdza wszystkie obrazy oprogramowania układowego i systemu operacyjnego przy każdym uruchomieniu w oparciu o klucze zapisane w bezpiecznikach SoC. GrapheneOS wgrywa własny publiczny klucz zweryfikowanego uruchamiania do bezpiecznego elementu — przy każdym uruchomieniu ten klucz weryfikuje system operacyjny.

#### Skróty kluczy zweryfikowanego uruchamiania

Gdy alternatywny system operacyjny jest ładowany, urządzenie wyświetla **żółte powiadomienie** z identyfikatorem systemu operacyjnego (sha256 klucza zweryfikowanego uruchamiania). Pixele 4. i 5. generacji wyświetlają tylko pierwsze 32 bity; **Pixele 6. generacji i nowsze wyświetlają pełny skrót**. Porównaj z oficjalnymi skrótami:

| Urządzenie | Skrót klucza zweryfikowanego uruchamiania |
|------------|------------------------------------------|
| Pixel 10a | `d8f879d10419eddc9fcda6280718be763f6bf12299e1f72df3ea8ad8a8eb7f80` |
| Pixel 10 Pro Fold | `55a2d44103e56d5ec65496399c417987ba77730e6488fc60ba058d09fc3caee3` |
| Pixel 10 Pro XL | `141d7fc32af7958a416f2661b37cf6f27bfb376fb5ce616aeaa27a82c7a04f74` |
| Pixel 10 Pro | `4e8ee8f717754052198ca6d2d3aaa232e2461b4293c0d6f297e519cc778de093` |
| Pixel 10 | `3f7415ea26f5df5b14ea6d153256071a7a1af9ce7b0970b7311cc463c7ea02c7` |
| Pixel 9a | `0508de44ee00bfb49ece32c418af1896391abde0f05b64f41bc9a2dfb589445b` |
| Pixel 9 Pro Fold | `af4d2c6e62be0fec54f0271b9776ff061dd8392d9f51cf6ab1551d346679e24c` |
| Pixel 9 Pro XL | `55d3c2323db91bb91f20d38d015e85112d038f6b6b5738fe352c1a80dba57023` |
| Pixel 9 Pro | `f729cab861da1b83fdfab402fc9480758f2ae78ee0b61c1f2137dd1ab7076e86` |
| Pixel 9 | `9e6a8f3e0d761a780179f93acd5721ba1ab7c8c537c7761073c0a754b0e932de` |
| Pixel 8a | `096b8bd6d44527a24ac1564b308839f67e78202185cbff9cfdcb10e63250bc5e` |
| Pixel 8 Pro | `896db2d09d84e1d6bb747002b8a114950b946e5825772a9d48ba7eb01d118c1c` |
| Pixel 8 | `cd7479653aa88208f9f03034810ef9b7b0af8a9d41e2000e458ac403a2acb233` |
| Pixel Fold | `ee0c9dfef6f55a878538b0dbf7e78e3bc3f1a13c8c44839b095fe26dd5fe2842` |
| Pixel Tablet | `94df136e6c6aa08dc26580af46f36419b5f9baf46039db076f5295b91aaff230` |
| Pixel 7a | `508d75dea10c5cbc3e7632260fc0b59f6055a8a49dd84e693b6d8899edbb01e4` |
| Pixel 7 Pro | `bc1c0dd95664604382bb888412026422742eb333071ea0b2d19036217d49182f` |
| Pixel 7 | `3efe5392be3ac38afb894d13de639e521675e62571a8a9b3ef9fc8c44fd17fa1` |
| Pixel 6a | `08c860350a9600692d10c8512f7b8e80707757468e8fbfeea2a870c0a83d6031` |
| Pixel 6 Pro | `439b76524d94c40652ce1bf0d8243773c634d2f99ba3160d8d02aa5e29ff925c` |
| Pixel 6 | `f0a890375d1405e62ebfd87e8d3f475f948ef031bbf9ddd516d5f600a23677e8` |

#### Sprzętowe zaświadczanie za pomocą aplikacji Auditor

GrapheneOS udostępnia [aplikację Auditor](https://attestation.app/) do weryfikacji integralności sprzętu, oprogramowania układowego i systemu operacyjnego przy użyciu zweryfikowanego uruchamiania i zdalnego zaświadczania. Wyniki są wyświetlane na drugim urządzeniu z Androidem z uruchomionym Auditorem (nie na weryfikowanym urządzeniu) lub za pośrednictwem opcjonalnej [usługi monitorowania integralności urządzenia](https://attestation.app/) dla automatycznych zaplanowanych weryfikacji z alertami e-mail.

---

## Zastąpienie GrapheneOS systemem stock

Instalacja systemu stock za pomocą [narzędzia do flashowania Google](https://flash.android.com/) jest podobna do powyższego procesu. Jednak przed flashowaniem i blokowaniem musisz wymazać klucz zweryfikowanego uruchamiania GrapheneOS, aby w pełni przywrócić system stock:

**Instalator internetowy:** Użyj przycisku "Erase non-stock key" w instalatorze internetowym GrapheneOS.

**CLI:**

```bash
fastboot erase avb_custom_key
```

Następnie wgraj obrazy fabryczne systemu stock i zablokuj bootloader.

---

## Podsumowanie

Instalacja GrapheneOS na urządzeniu Google Pixel zapewnia wiodące w branży funkcje prywatności i bezpieczeństwa. Użyj **instalatora internetowego** na [grapheneos.org/install/web](https://grapheneos.org/install/web) dla najprostszego doświadczenia lub postępuj zgodnie z powyższymi krokami CLI dla tradycyjnego podejścia. Zawsze blokuj bootloader po flashowaniu, aby włączyć pełne zweryfikowane uruchamianie, i opcjonalnie użyj aplikacji Auditor, aby potwierdzić integralność instalacji.

## Odnośniki

1. [Witryna GrapheneOS](https://grapheneos.org/)
2. [Instalator internetowy GrapheneOS](https://grapheneos.org/install/web)
3. [Przewodnik instalacji GrapheneOS CLI](https://grapheneos.org/install/cli)
4. [Wydania GrapheneOS](https://grapheneos.org/releases)
5. [Przewodnik użytkowania GrapheneOS](https://grapheneos.org/usage)
6. [FAQ GrapheneOS](https://grapheneos.org/faq)
7. [Aplikacja Auditor](https://attestation.app/)
8. [Android Platform Tools](https://developer.android.com/studio/releases/platform-tools)
