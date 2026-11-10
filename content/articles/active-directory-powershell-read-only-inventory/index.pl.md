---
title: "Tworzenie inwentaryzacji Active Directory tylko do odczytu w PowerShell"
date: 2026-10-10
lastmod: 2026-11-07
toc: true
draft: false
description: "Inwentaryzuj jednostki OU, użytkowników i komputery Active Directory za pomocą zapytań PowerShell o określonym zakresie. Eksportuj kontrolowane pliki CSV bez zmieniania obiektów katalogowych."
genre: ["Active Directory", "PowerShell", "System Administration"]
tags: ["inwentaryzacja Active Directory", "inwentaryzacja AD w PowerShell", "Get-ADUser", "Get-ADComputer", "Get-ADOrganizationalUnit", "Get-ADDomain", "baza wyszukiwania", "AD tylko do odczytu", "eksport użytkowników AD", "eksport komputerów AD", "eksport jednostek OU", "Export-Csv", "RSAT", "audyt katalogu", "raportowanie AD", "inwentaryzacja OU", "Windows Server", "skrypt PowerShell", "moduł AD", "higiena katalogu"]
cover: "/img/cover/active-directory-powershell-read-only-inventory.webp"
coverAlt: "Drzewo Active Directory z rekordami użytkowników, komputerów i jednostek organizacyjnych eksportowanymi do trzech plików do przeglądu."
coverCaption: "Określ zakres zapytania, a następnie eksportuj tylko potrzebne pola."
---

Porządki w Active Directory warto zacząć od wiarygodnej listy istniejących obiektów. Ta **inwentaryzacja tylko do odczytu** zbiera jednostki organizacyjne, użytkowników i komputery z jednego wybranego zakresu. Eksportuje trzy pliki CSV (z wartościami oddzielonymi przecinkami) do przeglądu, nie zmieniając obiektów katalogowych. Chroń te pliki, ponieważ nazwy i szczegóły urządzeń ujawniają część informacji o Twoim środowisku.

<!--more-->

## Najważniejsze informacje

- **Wybierz zakres:** Zacznij od zapytania o jedną jednostkę organizacyjną, zanim rozszerzysz je na całą domenę.
- **Używaj poleceń odczytu:** `Get-ADOrganizationalUnit`, `Get-ADUser` i `Get-ADComputer` pobierają obiekty.
- **Wybierz pola:** Eksportuj tylko właściwości potrzebne do danego zadania.
- **Sprawdź wynik:** Przed użyciem raportu porównaj liczby obiektów i przykładowe wiersze.

## Zanim zaczniesz

Potrzebujesz hosta administracyjnego Windows z działającym DNS i dostępem sieciowym do kontrolera domeny, modułu PowerShell **ActiveDirectory**, konta zatwierdzonego do odczytu wybranych obiektów oraz chronionego folderu na pliki CSV. Na kliencie Windows moduł pochodzi z narzędzi Active Directory w Remote Server Administration Tools (RSAT). [Przewodnik po module Active Directory](/articles/active-directory-module-powershell-installation-usage-guide/) w tej witrynie opisuje instalację. Microsoft udostępnia [dokumentację poleceń cmdlet](https://learn.microsoft.com/en-us/powershell/module/activedirectory/) modułu oraz [opcje instalacji RSAT](https://learn.microsoft.com/windows-server/remote/remote-server-administration-tools). Ten poradnik używa składni Windows PowerShell i nie zmienia obiektów katalogowych.

Uprawnienia katalogowe nadal obowiązują. Microsoft wyjaśnia w wytycznych dotyczących [kont uprzywilejowanych](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory), że listy kontroli dostępu obiektów często dają uwierzytelnionym użytkownikom dostęp do odczytu ogólnych informacji, a ograniczają dostęp do wrażliwych pól i możliwość wprowadzania zmian. Najpierw użyj zatwierdzonego konta i testowej jednostki OU. Nie podnoś uprawnień do Domain Admin, aby wymusić powodzenie inwentaryzacji.

> **Ostrzeżenie:** Pliki CSV zawierają nazwy kont i komputerów. Zapisuj je w zatwierdzonej lokalizacji, ogranicz dostęp i usuń dodatkowe kopie po przeglądzie. Nie publikuj surowego eksportu ani nie dołączaj go do publicznego zgłoszenia.

## Wybierz bazę wyszukiwania

**Jednostka organizacyjna (OU)** grupuje obiekty katalogowe. Jej **nazwa wyróżniająca (DN)** określa pozycję w drzewie katalogu. Parametr `-SearchBase` ogranicza zapytanie do wybranego DN. Bez określenia zakresu szeroki filtr może zwrócić znacznie więcej obiektów, niż potrzebujesz.

Najpierw załaduj moduł i sprawdź DN bieżącej domeny:

```powershell
Import-Module ActiveDirectory
(Get-ADDomain).DistinguishedName
```

Microsoft opisuje polecenie [Get-ADDomain](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-addomain) i zwracane przez nie informacje o domenie. Zanim ustawisz bazę wyszukiwania, znajdź jednostkę OU, którą chcesz sprawdzić:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase (Get-ADDomain).DistinguishedName |
    Select-Object Name, DistinguishedName
```

Skopiuj dokładny DN z wyniku. W kolejnych przykładach zastąp wartość dokumentacyjną DN swojej jednostki OU:

```powershell
$SearchBase = 'OU=Lab,DC=example,DC=com'
```

`example.com` to domena dokumentacyjna. Nie kopiuj jej DN do aktywnego zapytania. Jeśli celowo potrzebujesz inwentaryzacji całej domeny, ustaw `$SearchBase` na DN domeny i odnotuj szerszy zakres w raporcie. [Dokumentacja Get-ADOrganizationalUnit](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit) firmy Microsoft opisuje parametry `-Filter` i `-SearchBase`.

## Inwentaryzuj jednostki OU, użytkowników i komputery

Zacznij od policzenia obiektów. Dzięki temu szybko wykryjesz niewłaściwą bazę wyszukiwania lub nieoczekiwany pusty wynik:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADUser -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADComputer -Filter * -SearchBase $SearchBase | Measure-Object
```

`-Filter *` oznacza wszystkie pasujące obiekty w obrębie bazy wyszukiwania. Microsoft opisuje polecenia [Get-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser) i [Get-ADComputer](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) jako polecenia pobierające dane. Wynik równy zero może być prawidłowy, ale przed uznaniem inwentaryzacji za kompletną sprawdź DN, uprawnienia i domenę docelową.

Teraz wyświetl kilka wierszy w konsoli. Zapisz wybrane pola, aby podgląd i późniejszy eksport CSV używały tych samych kolumn:

```powershell
$UserFields = 'Name', 'SamAccountName', 'Enabled', 'DistinguishedName'
Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields -First 10
```

W przypadku komputerów pobierz dodatkowe pole systemu operacyjnego tylko wtedy, gdy potrzebujesz go do przeglądu:

```powershell
$ComputerFields = @(
    'Name', 'DNSHostName', 'OperatingSystem',
    'Enabled', 'DistinguishedName'
)
Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields -First 10
```

Parametr `-Properties` pobiera właściwości spoza domyślnego zestawu polecenia cmdlet. Dokumentacja [polecenia dotyczącego komputerów](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) firmy Microsoft opisuje ten parametr. Traktuj nazwy systemów operacyjnych jako dane katalogowe, a nie potwierdzenie aktualnie zainstalowanej wersji. Obiekt komputera może być nieaktualny albo jego atrybut mógł nie zostać zaktualizowany.

## Eksportuj kontrolowany plik CSV

Wybierz zatwierdzony folder wyjściowy z wystarczającą ilością miejsca. Poniższe polecenia zapisują **lokalne pliki CSV** i nie zmieniają obiektów katalogowych. Uruchom je w tym folderze. `-NoClobber` zapobiega nadpisaniu istniejącego pliku. Przy każdym uruchomieniu użyj nowego folderu lub nazwy pliku.

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase |
    Select-Object Name, DistinguishedName |
    Export-Csv -Path .\ad-ous.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields |
    Export-Csv -Path .\ad-users.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields |
    Export-Csv -Path .\ad-computers.csv -NoTypeInformation -Encoding UTF8 -NoClobber
```

[Dokumentacja Export-Csv](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv?view=powershell-5.1) firmy Microsoft wyjaśnia parametry `-NoTypeInformation`, `-Encoding` i `-NoClobber`. Otwórz każdy plik CSV w edytorze tekstu lub zatwierdzonym arkuszu kalkulacyjnym. Sprawdź nagłówek, kilka wierszy i liczbę rekordów w porównaniu z wcześniejszymi wynikami. Nieudane polecenie ani plik o rozmiarze zero bajtów nie potwierdzają kompletności raportu.

> **Oczekiwany wynik:** Masz trzy pliki CSV z rekordami OU, użytkowników i komputerów z wybranego zakresu. Liczba wierszy i przykładowe wpisy odpowiadają temu zakresowi.

## Sprawdzaj bez zmieniania obiektów

Użyj inwentaryzacji, aby odpowiedzieć na konkretne pytania: Która jednostka OU zawiera dany komputer? Którzy użytkownicy są wyłączeni? Które urządzenia wymagają przypisania właściciela? Zapisz ustalenia w oddzielnej notatce z przeglądu. Nie zakładaj, że wartość `Enabled` określa, czy konto jest nadal potrzebne. Nie usuwaj ani nie wyłączaj obiektu na podstawie samego eksportu.

W przypadku raportu cyklicznego zapisuj datę zapytania, domenę, DN jednostki OU, wybrane właściwości, operatora i lokalizację CSV. Porównując dwa eksporty, upewnij się, że użyto tego samego zakresu i pól. W przeciwnym razie różnica może wynikać z zapytania, a nie ze zmiany w katalogu.

To **inwentaryzacja**, a nie audyt kont uprzywilejowanych ani raport aktywności logowania. Microsoft zauważa, że właściwości i uprawnienia Active Directory różnią się zależnie od obiektu i środowiska. Przed podjęciem działania potwierdź u właściciela systemu atrybut systemu operacyjnego lub nazwę wyświetlaną. [Przewodnik po zabezpieczeniach Active Directory](/articles/active-directory-security-best-practices/) w tej witrynie opisuje szersze zabezpieczenia.

## Rozwiązywanie problemów

- **Nie można zaimportować modułu:** Sprawdź, czy na hoście zainstalowano narzędzia Active Directory z RSAT lub narzędzia administracyjne Windows Server. Skorzystaj z [przewodnika instalacji modułu](/articles/active-directory-module-powershell-installation-usage-guide/).
- **Zapytanie nie zwraca obiektów:** Sprawdź dokładny DN, bieżącą domenę, zawartość jednostki OU i uprawnienia do odczytu. Zanim rozszerzysz zakres, wypróbuj znaną, małą jednostkę OU.
- **Właściwość jest pusta:** Potwierdź, że atrybut istnieje i że Twoje konto może go odczytać. Nie uzupełniaj brakujących pól przypuszczeniami.
- **Eksport zgłasza, że plik istnieje:** `-NoClobber` ochronił wcześniejszy raport. Wybierz nową nazwę pliku lub folder i ponów polecenie.
- **Liczby różnią się od oczekiwań:** Sprawdź, czy użytkownicy lub komputery nie znajdują się w innej jednostce OU, czy zakres się nie zmienił oraz czy katalog nie zmienił się podczas zapytania.

## Następne kroki

Przechowuj surowy plik CSV w chronionej lokalizacji przez uzgodniony okres przeglądu. Udostępniaj tylko pola potrzebne osobie weryfikującej. Po potwierdzeniu ustaleń przez właścicieli zaplanuj zmiany zgodnie ze standardowym procesem zatwierdzania i wycofywania. Po zatwierdzonych zmianach ponownie wykonaj tę samą inwentaryzację w tym samym zakresie, aby potwierdzić wynik.
