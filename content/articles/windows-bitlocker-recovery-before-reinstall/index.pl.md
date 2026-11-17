---
title: "Znajdź klucz odzyskiwania BitLocker przed ponowną instalacją Windows"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Znajdź i sprawdź właściwy klucz odzyskiwania BitLocker, zabezpiecz oddzielną kopię zapasową i wybierz właściwą metodę odzyskiwania lub ponownej instalacji Windows przed wymazaniem dysku."
genre: ["Zabezpieczenia Windows", "Odzyskiwanie danych", "Administracja systemami"]
tags: ["klucz odzyskiwania BitLocker", "ponowna instalacja Windows 11", "ponowna instalacja Windows 10", "szyfrowanie urządzenia", "identyfikator klucza odzyskiwania", "klucz odzyskiwania konta Microsoft", "klucz odzyskiwania konta służbowego lub szkolnego", "kopia klucza odzyskiwania", "zaszyfrowany dysk", "czysta instalacja", "odzyskiwanie Windows", "kopia BitLocker", "48-cyfrowy klucz odzyskiwania", "nośnik instalacyjny Windows", "kopia zapasowa danych", "szyfrowanie dysku", "lista kontrolna odzyskiwania", "instalacja Windows", "rozwiązywanie problemów BitLocker", "przygotowanie do ponownej instalacji"]
cover: "/img/cover/windows-bitlocker-recovery-before-reinstall.webp"
coverAlt: "Laptop z zablokowanym dyskiem, osobna karta z kluczem odzyskiwania, kopia na USB i zaznaczona lista kontrolna odzyskiwania."
coverCaption: "Sprawdź klucz odzyskiwania przed wymazaniem dysku."
---

Czysta instalacja Windows wymazuje wybrany dysk. Jeśli stary dysk używa funkcji **BitLocker** lub **Szyfrowanie urządzenia**, najpierw znajdź klucz odzyskiwania i skopiuj pliki. Klucz zapewnia dostęp do starych zaszyfrowanych danych. Nowa instalacja Windows nie przywróci plików usuniętych z dysku.

<!--more-->

## Najważniejsze informacje

- **Znajdź właściwy klucz:** porównaj identyfikator klucza odzyskiwania wyświetlany przez Windows z kluczem zapisanym na koncie, wydruku lub kopii USB.
- **Sprawdź dostęp:** obejrzyj kopię zapasową, dopasuj identyfikator i odblokuj zablokowany dysk przed usunięciem partycji.
- **Zabezpiecz kopię:** przechowuj 48-cyfrowy klucz oddzielnie od komputera i nośnika instalacyjnego USB.
- **Wybierz właściwą metodę:** użyj opcji odzyskiwania, jeśli potrzebujesz starej instalacji. Wybierz czystą instalację dopiero po sprawdzeniu oddzielnej kopii plików.

## Zanim zaczniesz

Potrzebujesz dostępu do komputera, drugiego urządzenia do sprawdzenia konta lub kopii zapasowej oraz zewnętrznego dysku albo zaufanej pamięci w chmurze na ważne pliki. **Czas:** wyszukanie klucza zależy od dostępu do konta. Kopiowanie plików zależy od ich ilości. **Poziom trudności:** podstawowy przy sprawdzaniu konta, średni przy użyciu narzędzi odzyskiwania. Ten poradnik opisuje przygotowanie i wybór metod odzyskiwania dla Windows 10 i Windows 11. [Poradnik czystej instalacji Windows](/articles/how-to-install-windows-10-and-windows-11-from-scratch/) opisuje nośniki i konfigurację instalacji.

*Standardowe wsparcie Windows 10 zakończyło się 14 października 2025 r. Jeśli urządzenie spełnia wymagania, zaplanuj instalację obsługiwanego Windows 11. Microsoft opisuje [cykl życia Windows 10 i opcje rozszerzonego wsparcia](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-10-end-of-support).*

> **Ostrzeżenie:** nie usuwaj partycji, aby rozwiązać monit odzyskiwania BitLocker, jeśli nadal potrzebujesz plików ze starej instalacji. Microsoft informuje, że reset bez klucza odzyskiwania usuwa te pliki. Zobacz [wskazówki Microsoft dotyczące klucza odzyskiwania](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key).

## Sprawdź, czy szyfrowanie jest aktywne

**Szyfrowanie urządzenia** i **BitLocker** szyfrują dysk, aby osoba bez odpowiednich danych uwierzytelniających nie mogła odczytać jego zawartości. Jeśli Windows nadal się uruchamia, w Windows 11 otwórz **Ustawienia > Prywatność i zabezpieczenia > Szyfrowanie urządzenia**. W edycjach z zarządzaniem BitLocker wyszukaj w menu Start **Zarządzaj funkcją BitLocker**. Zapisz literę zaszyfrowanego dysku i konto użyte do konfiguracji urządzenia. W przypadku zarządzanego urządzenia służbowego lub szkolnego klucz często przechowuje organizacja.

Opcjonalnie sprawdź stan w wierszu polecenia. Wyszukaj w menu Start **Wiersz polecenia**, wybierz **Uruchom jako administrator** i wprowadź te polecenia. Zastąp `C:`, jeśli Windows używa innej litery. **Protektor** to metoda używana przez Windows do odblokowania zaszyfrowanego dysku.

```text
manage-bde.exe -status C:
manage-bde.exe -protectors -get C:
```

Pierwsze polecenie pokazuje stan szyfrowania, ochrony i blokady. Drugie wyświetla typy protektorów i ich identyfikatory, a także może ujawnić hasło odzyskiwania. Microsoft opisuje te kontrole w [przewodniku obsługi BitLocker](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) oraz [opisie polecenia sprawdzającego stan](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-status). **Nie wklejaj wyniku do prośby o pomoc ani nie udostępniaj go na zrzucie ekranu.** Jeśli urządzenie jest już zablokowane, użyj identyfikatora z ekranu odzyskiwania. Pierwsze osiem cyfr identyfikatora pomaga wybrać właściwy klucz.

## Gdzie znaleźć klucz odzyskiwania BitLocker

**Identyfikator klucza odzyskiwania** wskazuje zapisany klucz. **Klucz odzyskiwania** to osobna 48-cyfrowa liczba wpisywana w celu odblokowania dysku. Nie wpisuj identyfikatora w polu hasła odzyskiwania.

| Urządzenie lub kopia zapasowa | Gdzie szukać |
|---|---|
| **Osobiste konto Microsoft** | Na drugim urządzeniu zaloguj się przez [stronę Microsoft z kluczami odzyskiwania](https://aka.ms/myrecoverykey). Przed użyciem 48-cyfrowego klucza dopasuj identyfikator. |
| **Urządzenie służbowe lub szkolne** | Sprawdź konto organizacji przez [stronę Microsoft dla kont służbowych lub szkolnych](https://aka.ms/aadrecoverykey) albo skontaktuj się z działem IT. |
| **Wydruk lub kopia USB** | Znajdź wydruk lub plik tekstowy utworzony przy włączaniu szyfrowania. Dopasuj identyfikator klucza do tego z ekranu. |

Microsoft wymienia te lokalizacje w artykule [Znajdź klucz odzyskiwania BitLocker](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key). Zacznij od klucza o identyfikatorze zgodnym z monitem. Klucz z innego urządzenia lub usuniętego protectora może nie odblokować tego woluminu. Jeśli urządzenie skonfigurowała inna osoba, jej konto może zawierać klucz.

## Utwórz osobną kopię klucza

Jeśli Windows nadal uruchamia się w edycji Pro, Enterprise lub Education, wyszukaj **Zarządzaj funkcją BitLocker**. Przy zaszyfrowanym dysku wybierz **Utwórz kopię zapasową klucza odzyskiwania**. Microsoft oferuje zapis na koncie, dysku USB, w pliku tekstowym lub na wydruku. Plik tekstowy albo USB przechowuj wyłącznie na szyfrowanym nośniku z kontrolą dostępu, oddzielnie od komputera. Nie używaj nieszyfrowanej lokalizacji. Aktualny interfejs i opcje opisuje [Tworzenie kopii zapasowej klucza odzyskiwania BitLocker](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key).

W Windows Home nie ma **Zarządzaj funkcją BitLocker**. W Windows 11 sprawdź **Ustawienia > Prywatność i zabezpieczenia > Szyfrowanie urządzenia**, a następnie zweryfikuj klucz na koncie Microsoft użytym podczas konfiguracji. Microsoft wyjaśnia, że [Szyfrowanie urządzenia](https://support.microsoft.com/en-us/windows/security/encryption/device-encryption-in-windows) zapisuje klucz na połączonym koncie Microsoft lub służbowym podczas aktywacji. Jeśli konfiguracja umożliwia eksport, zapisz osobną, chronioną kopię.

Otwórz cyfrową kopię na drugim urządzeniu. Wydruk porównaj z wpisem na koncie lub ekranem odzyskiwania. Dopasuj **identyfikator klucza odzyskiwania** do identyfikatora na ekranie lub liście protektorów. Sprawdź, czy kopia zawiera wszystkie 48 cyfr właściwego klucza. Papierową lub przenośną kopię trzymaj z dala od zaszyfrowanego komputera. Złodziej mający komputer i klucz ominąłby ochronę dysku, ostrzega Microsoft w [instrukcjach tworzenia kopii](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key). Nie dołączaj klucza do zgłoszenia pomocy technicznej.

> **Oczekiwany rezultat:** masz zgodny klucz odzyskiwania dostępny poza komputerem.

## Odblokuj komputer, który się nie uruchamia

Jeśli pojawi się **ekran odzyskiwania BitLocker**, wpisz 48-cyfrowy klucz zgodny z jego identyfikatorem. Po uruchomieniu Windows skopiuj pliki przed zmianą partycji. Jeśli klucz odblokuje dysk, ale Windows nadal się nie uruchomi, otwórz [środowisko odzyskiwania Windows](https://support.microsoft.com/en-us/windows/experience/backup-recovery/windows-recovery-environment) i przed resetem spróbuj użyć **Naprawy podczas uruchamiania**. Niektóre narzędzia odzyskiwania wymagają klucza, gdy dysk pozostaje zaszyfrowany.

Aby skopiować pliki z narzędzi odzyskiwania, w środowisku odzyskiwania Windows otwórz **Rozwiąż problemy > Opcje zaawansowane > Wiersz polecenia**. Użyj `manage-bde -status` i `dir`, aby znaleźć zaszyfrowany wolumin Windows i oddzielny zewnętrzny dysk na kopię. **Litery dysków mogą różnić się od tych używanych w zwykłym Windows.** Nie kopiuj plików na instalacyjny USB ani na zaszyfrowany dysk źródłowy.

```text
manage-bde.exe -status
dir D:\Users
dir E:\
```

Powyższe litery są przykładami. Po zidentyfikowaniu właściwych woluminów odblokuj wolumin Windows odpowiednim kluczem. Zastąp przykładową literę dysku i symbol zastępczy własnymi wartościami. Wpisz prawdziwy 48-cyfrowy klucz lokalnie. Nie publikuj ani nie udostępniaj wyniku polecenia.

```text
manage-bde.exe -unlock D: -recoverypassword <48-digit-key>
```

Opcja `-recoverypassword` przyjmuje 48-cyfrowy klucz jako argument wiersza polecenia. Może to zapisać klucz w historii powłoki, transkrypcjach i danych widocznych przy inspekcji procesów. Użyj ekranu odzyskiwania Windows, jeśli chcesz wpisać klucz bez argumentu polecenia. Jeśli masz osobny plik klucza odzyskiwania `.bek`, opcja `-recoverykey <path-to-external-bek>` pozwala uniknąć wpisywania 48 cyfr. Nie umieszczaj klucza na zrzutach ekranu ani w zgłoszeniach.

Microsoft opisuje [polecenie odblokowania](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-unlock). [Wskazówki dotyczące odzyskiwania](https://learn.microsoft.com/en-us/troubleshoot/windows-client/windows-security/bitlocker-recovery-known-issues) opisują też kopiowanie plików użytkownika na inny dysk po odblokowaniu. Aby przykładowo skopiować folder Dokumenty, najpierw potwierdź nazwę konta Windows i literę dysku zewnętrznego, a następnie zastąp obie ścieżki:

```text
xcopy "D:\Users\Name\Documents" "E:\Backup\Documents" /S /E /I /H /V
```

Opcje **`/S /E`** obejmują podfoldery, także puste. **`/I`** traktuje miejsce docelowe jako folder, **`/H`** uwzględnia pliki ukryte, a **`/V`** sprawdza każdy zapisany plik. Microsoft opisuje je w [dokumentacji xcopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy). Powtórz operację dla pozostałych potrzebnych folderów. Otwórz skopiowane pliki na innym urządzeniu, zanim wymażesz dysk Windows. Jeśli nie możesz rozpoznać woluminów albo kopiowanie się nie powiedzie, zatrzymaj się i skorzystaj z pomocy zaufanego specjalisty odzyskiwania danych.

## Zdecyduj, czy ponownie instalować system

**Kopia klucza nie jest kopią plików.** Przed wyborem metody ponownej instalacji wykonaj te kroki w podanej kolejności:

1. Zidentyfikuj zaszyfrowany dysk i identyfikator klucza odzyskiwania.
2. Pobierz zgodny 48-cyfrowy klucz z konta, wydruku lub kopii USB.
3. Jeśli dysk jest zablokowany, odblokuj go na ekranie odzyskiwania albo w narzędziach odzyskiwania.
4. Skopiuj Pulpit, Dokumenty, Obrazy i inne lokalne foldery na zewnętrzny dysk lub zaufaną pamięć w chmurze. W razie potrzeby uwzględnij eksport przeglądarki, dane aplikacji i informacje o licencjach.
5. Otwórz kilka skopiowanych plików na drugim urządzeniu.
6. Dopiero po sprawdzeniu kopii wybierz naprawę, reset lub ponowną instalację.

> **Oczekiwany rezultat:** odpowiedni klucz i ważne pliki są dostępne poza starą instalacją Windows.

Microsoft opisuje [opcje odzyskiwania Windows](https://support.microsoft.com/en-us/windows/experience/backup-recovery/recovery-options-in-windows), które różnie wpływają na pliki i aplikacje. Wiele opcji środowiska odzyskiwania Windows wymaga klucza, gdy BitLocker chroni dysk. Jeśli wolumin jest tam zablokowany, opcja **Zachowaj moje pliki** nie odblokuje go bez klucza.

**Naprawa podczas uruchamiania** i **Przywracanie systemu** mają naprawić istniejącą instalację. **Resetuj ustawienia komputera do stanu początkowego** oferuje opcję **Zachowaj moje pliki**, ale usuwa aplikacje i ustawienia. Opcja **Usuń wszystko** kasuje pliki osobiste. Uruchomienie **`setup.exe` z działającego Windows** umożliwia ponowną instalację w miejscu i wybór zachowania danych. **Instalacja Windows** uruchomiona z USB rozpoczyna czystą instalację, która usuwa pliki, aplikacje i ustawienia wybranej instalacji Windows. Ten sam nośnik oferuje także naprawę. Przed zatwierdzeniem resetu lub instalacji przeczytaj wybraną opcję i sprawdź dysk docelowy. Obie metody opisują [instrukcje ponownej instalacji Microsoft](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media).

| Sytuacja | Następne działanie |
|---|---|
| **Windows się uruchamia i potrzebujesz plików** | Utwórz kopię plików, sprawdź klucz odzyskiwania, a potem wybierz naprawę lub ponowną instalację. |
| **Windows żąda klucza** | Dopasuj identyfikator na ekranie do zapisanego klucza przed zmianą dysku. |
| **Brak zgodnego klucza i kopii plików** | Zatrzymaj się przed wymazaniem dysku. Sprawdź każde konto, wydruk i kopię USB oraz skontaktuj się z działem IT. |
| **Pliki są skopiowane i chcesz zacząć od nowa** | Postępuj zgodnie z [instrukcjami ponownej instalacji Microsoft](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media) i uważnie wybierz dysk docelowy. |

Microsoft informuje, że pracownicy pomocy technicznej nie mogą odtworzyć utraconego klucza odzyskiwania. Jeśli go nie znajdujesz, nie zmieniaj dalej ustawień oprogramowania układowego i sprawdź wszystkie miejsca przechowywania kopii. W przypadku zarządzanego urządzenia poproś administratora o pomoc. Reset bez potrzebnego klucza usuwa stare pliki. Czysta instalacja usuwa też pliki osobiste, aplikacje, dostosowania urządzenia i ustawienia wybranej instalacji. Podejmij tę decyzję świadomie po sprawdzeniu kopii.

## Rozwiązywanie problemów

- **Klucz nie działa:** ponownie sprawdź identyfikator i konto. Urządzenie może mieć więcej niż jeden zapisany klucz odzyskiwania.
- **Brak funkcji Zarządzaj funkcją BitLocker:** Windows Home używa Szyfrowania urządzenia na zgodnych urządzeniach. Sprawdź Ustawienia i konto Microsoft użyte podczas konfiguracji.
- **Na koncie widzisz kilka kluczy:** dopasuj pierwsze osiem cyfr identyfikatora z ekranu odzyskiwania do zapisanych wpisów. Nie wybieraj klucza tylko na podstawie nazwy urządzenia.
- **Klucz odblokowuje dysk, ale Windows się nie uruchamia:** spróbuj Naprawy podczas uruchamiania w środowisku odzyskiwania Windows. Skopiuj dostępne pliki przed resetem lub czystą instalacją.
- **Klucz przechowuje firma lub szkoła:** przed resetem lub ponowną instalacją skontaktuj się z administratorem urządzenia.
- **Plik klucza znajduje się na zablokowanym komputerze:** poszukaj osobnego konta, wydruku lub kopii wymiennej. Kopia na jedynym zaszyfrowanym dysku nie pomoże, gdy dysk jest zablokowany.
- **Monit odzyskiwania pojawił się po zmianie oprogramowania układowego:** zanotuj zmianę i nie wykonuj kolejnych. Znajdź zgodny klucz lub skontaktuj się z administratorem urządzenia.

## Następne kroki

Po sprawdzeniu klucza i plików użyj [poradnika czystej instalacji Windows](/articles/how-to-install-windows-10-and-windows-11-from-scratch/), jeśli czysta instalacja odpowiada Twojemu celowi. Po uruchomieniu Windows sprawdź **Ustawienia > Prywatność i zabezpieczenia > Szyfrowanie urządzenia** albo wyszukaj **Zarządzaj funkcją BitLocker**. W edycjach Pro, Enterprise i Education wybierz **Utwórz kopię zapasową klucza odzyskiwania** w tej funkcji. W edycji Home sprawdź, czy połączone konto zawiera aktualny klucz, i zapisz osobną kopię, jeśli Windows oferuje eksport. Nie zakładaj, że stary klucz pasuje do nowej zaszyfrowanej instalacji.
