---
title: "Aktualizacja zabezpieczeń Chrome 156: sprawdź październikową poprawkę"
date: 2026-10-28
lastmod: 2026-11-09
toc: true
draft: false
description: "Sprawdź wydanie zabezpieczeń Chrome 156 z 27 października w systemach Windows, macOS, Linux i Android. Porównaj zainstalowaną kompilację, dokończ oczekujący restart i osobno sprawdź urządzenia zarządzane."
genre: ["Przeglądarki", "Bezpieczeństwo", "Zarządzanie poprawkami"]
tags: ["Chrome 156", "aktualizacja zabezpieczeń Chrome", "weryfikacja poprawki Chrome", "sprawdzanie wersji Chrome", "Chrome 156 dla Windows", "Chrome 156 dla macOS", "Chrome 156 dla Linux", "Chrome 156 dla Androida", "CVE-2026-118306", "CVE-2026-118331", "CVE-2026-118348", "CVE-2026-118344", "poprawki przeglądarek", "Chrome Enterprise Core", "zarządzane przeglądarki", "bezpieczeństwo Chromium", "aktualizacje przeglądarek", "restart Chrome", "chrome://version", "chrome://settings/help", "aktualizacja Chrome na Androidzie", "aktualizacje zabezpieczeń Brave", "aktualizacje zabezpieczeń Edge"]
cover: "/img/cover/cybersecurity-padlock-shield.webp"
coverAlt: "Ilustracja kłódki i tarczy symbolizujących aktualizację zabezpieczeń, a nie ekran wersji Chrome"
coverCaption: ""
---

**Wydanie zabezpieczeń Chrome z 27 października 2026 r.** zawiera 52 poprawki. Aby sprawdzić instalację, porównaj pełny numer wersji z wydaniem dla swojego systemu operacyjnego, a następnie uruchom ponownie Chrome, aby dokończyć oczekującą aktualizację. Samo ogłoszenie wersji nie dowodzi, że urządzenie otrzymało aktualizację. ([Wydanie Chrome na komputery](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

<!--more-->

## Jaka wersja powinna być widoczna?

27 października 2026 r. Google opublikowało następujące wersje kanału Stable. Wydanie na komputery podaje osobne kompilacje dla systemów Windows i macOS oraz dla Linuxa. W [wydaniu na Androida](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html) podano własną kompilację i informację, że wersje na Androida zawierają te same poprawki zabezpieczeń co odpowiadające im wersje na komputery, „o ile nie zaznaczono inaczej”.

| Platforma | Kompilacja z ogłoszenia Google z 27 października |
|---|---|
| **Windows** | 156.0.8078.73 lub 156.0.8078.74 |
| **macOS** | 156.0.8078.73 lub 156.0.8078.74 |
| **Linux** | 156.0.8078.73 |
| **Android** | 156.0.8078.73 |

*Użyj tej tabeli dla wydania z 27 października, a nie jako stałej wersji docelowej. Kolejne aktualizacje zabezpieczeń sprawdzaj w bieżącym [kanale wydań Chrome](https://chromereleases.googleblog.com/).* Google poinformowało, że wdrażanie wersji na komputery potrwa „kilka dni lub tygodni”, a kompilacja na Androida trafi do Google Play w ciągu kilku następnych dni. Urządzenie z wersją niższą niż podana nadal wymaga sprawdzenia, nawet podczas etapowego wdrażania. ([Komunikat dla komputerów](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html), [komunikat dla Androida](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html))

Na [liście poprawek zabezpieczeń dla komputerów](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html) cztery zgłoszone błędy oznaczono jako **Critical**: uszkodzenie pamięci w FileSystem [CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306), nieprawidłowa walidacja danych wejściowych w FileAPI CVE-2026-118331, nieprawidłowa walidacja danych wejściowych w Skia CVE-2026-118348 oraz use-after-free w Layout CVE-2026-118344. Ten sam komunikat wymienia dalsze CVE o poziomach **High** i **Medium**. Liczba 52 oznacza poprawki zabezpieczeń w wydaniu, a nie 52 niezależnie potwierdzone zgłoszenia wykorzystania luk. Według NVD CVE-2026-118306 dotyczy wersji Chrome starszych niż 156.0.8078.73. ([Rekord NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118306))

**Komunikat o wydaniu nie stwierdza, że wymienione luki są aktywnie wykorzystywane.** Ostrzeżenie dotyczy czasu ujawnienia: „Dostęp do szczegółów błędów i odnośników może być ograniczony do czasu, gdy większość użytkowników otrzyma poprawkę”. Ograniczonego dostępu do szczegółów nie traktuj jako dowodu wykorzystania luki. ([Komunikat dla komputerów](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

## Sprawdź i dokończ aktualizację na komputerze

1. Otwórz **`chrome://version`** w używanej instalacji Chrome. Zapisz pełną wersję i system operacyjny, a nie tylko numer główny 156. Okno Chrome z innego kanału lub innej instalacji wymaga osobnego sprawdzenia.
2. Otwórz **`chrome://settings/help`** albo wybierz **Więcej > Pomoc > Google Chrome — informacje**. Google podaje, że Chrome sprawdza aktualizacje na tej stronie. Poczekaj na zakończenie sprawdzania. ([Instrukcje Google dotyczące aktualizacji na komputerze](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en))
3. Wybierz **Uruchom ponownie**, jeśli strona pokazuje tę opcję. Najpierw zapisz niezakończoną pracę. Zamknij pozostałe okna Chrome, otwórz przeglądarkę ponownie i jeszcze raz sprawdź **`chrome://version`**. Porównaj z tabelą wersję widoczną po restarcie.
4. Jeśli wersja nadal jest niższa od ogłoszonej kompilacji, ponownie sprawdź dostępność aktualizacji. Jeśli przeglądarką zarządza organizacja albo program aktualizacyjny zgłasza błąd, skontaktuj się z administratorem. Pomyślne pobranie nie dowodzi, że zmieniła się wersja uruchomionej przeglądarki.

> **Oczekiwany wynik:** Po restarcie uruchomiona kompilacja Chrome Stable odpowiada wersji dla danej platformy z komunikatu z 27 października lub późniejszej wersji ogłoszonej przez dostawcę. Oczekujący przycisk Uruchom ponownie nie potwierdza zakończenia aktualizacji.

Na **Androidzie** otwórz Sklep Play > ikona profilu > Zarządzaj aplikacjami i urządzeniem, a następnie zaktualizuj Chrome w sekcji Dostępne aktualizacje, jeśli jest dostępna. W Chrome otwórz Więcej > Ustawienia > Informacje o Chrome, aby sprawdzić zainstalowaną wersję. Po zakończeniu aktualizacji aplikacji porównaj ją z wierszem Android. Te ścieżki menu są zgodne z [instrukcjami Google dla Androida](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en).

## Sprawdź zarządzaną flotę

W przypadku zarejestrowanych przeglądarek użyj **raportu wersji Chrome** w konsoli administracyjnej Google, aby znaleźć starsze kompilacje według systemu operacyjnego. Otwórz widok Browser Versions, wybierz odpowiednią jednostkę organizacyjną, sprawdź pełny numer wersji pomocniczej i wyeksportuj plik CSV, jeśli potrzebujesz listy urządzeń do obsługi. Google podaje, że raport obejmuje przeglądarki, które przesłały raporty w ciągu poprzednich 28 dni. Wskazuje też na możliwe opóźnienia, zwłaszcza w dużych flotach. ([Wyświetlanie szczegółów wersji Chrome](https://support.google.com/chrome/a/answer/10025748?hl=en))

**Oddziel zgłoszony wykaz od bieżącej weryfikacji.** Sprawdź czas ostatniego raportu i kanał dla każdego urządzenia, a następnie potwierdź wyjątki bezpośrednio w przeglądarce lub w inwentarzu zarządzanych punktów końcowych. Google liczy osobne instalacje Chrome, takie jak Stable i Beta, oddzielnie. Raportowanie przeglądarek wymaga rejestracji i włączenia [raportowania zarządzanych przeglądarek](https://support.google.com/chrome/a/answer/9301421?hl=en). Brak komputera w raporcie nie dowodzi, że ma on poprawkę.

## Osobno sprawdź przeglądarki pochodne Chromium

**Tabela wersji Chrome dotyczy Google Chrome.** Microsoft Edge, Brave i inne przeglądarki oparte na Chromium mają własne pakiety, numery wydań i harmonogramy aktualizacji. Komunikat Chrome nie potwierdza ich stanu poprawek. Sprawdź wersję każdej przeglądarki oraz jej własny komunikat o zabezpieczeniach lub informacje o wydaniu dotyczące odpowiednich poprawek Chromium. Nie porównuj bezpośrednio wersji Edge lub Brave z numerem Chrome 156.0.8078.73 i nie uznawaj jej na tej podstawie za poprawioną.

Dla każdej pochodnej przeglądarki zapisz nazwę produktu, kanał, zainstalowaną kompilację, adres URL komunikatu dostawcy i wskazaną przez niego naprawioną kompilację. Jeśli dostawca nie potwierdził poprawki, oznacz stan jako **niezweryfikowany** i postępuj zgodnie z jego instrukcjami aktualizacji. Wyniki dla Chrome i przeglądarek pochodnych zapisuj w osobnych wierszach inwentarza.

## Źródła i odnośniki

- [Chrome Releases: aktualizacja Stable Channel na komputery, 27 października 2026 r.](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html). Kompilacje komputerowe, 52 poprawki, CVE i komunikat dostawcy o ujawnieniu.
- [Chrome Releases: aktualizacja Chrome na Androida, 27 października 2026 r.](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html). Kompilacja Android i zastrzeżenie dotyczące odpowiadających jej poprawek na komputery.
- [System zgłoszeń Chromium: zapytanie o poprawki bezpieczeństwa M156](https://issues.chromium.org/issues?q=customfield1223088:1-M156). Odnośnik z komunikatu dla komputerów. Dostęp do szczegółów poszczególnych błędów zależy od ograniczeń ujawniania.
- [NVD: CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306) i [CVE-2026-118331](https://nvd.nist.gov/vuln/detail/CVE-2026-118331). Opisy luk i podatne wersje Chrome. Podane wyżej poziomy ważności pochodzą z komunikatu Google, a nie z oceny NVD CVSS.
- [Pomoc Google Chrome: aktualizowanie Chrome na komputerze](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en) i [na Androidzie](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en). Sprawdzanie aktualizacji i ścieżki menu wersji.
- [Pomoc Chrome Enterprise: wyświetlanie szczegółów wersji Chrome](https://support.google.com/chrome/a/answer/10025748?hl=en) i [włączanie raportowania zarządzanych przeglądarek](https://support.google.com/chrome/a/answer/9301421?hl=en). Wymagania i ograniczenia raportowania floty.
