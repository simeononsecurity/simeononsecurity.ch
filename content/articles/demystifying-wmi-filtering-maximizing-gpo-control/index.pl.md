---
title: "Zrozumieć filtrowanie WMI"
date: 2023-07-25
lastmod: 2026-11-12
toc: true
draft: false
description: "Dowiedz się, jak filtrowanie WMI pomaga kierować obiekty zasad grupy (GPO) do właściwych komputerów. Poznaj praktyczne przykłady i dobre praktyki."
genre: ["Zarządzanie systemem Windows", "Zasady grupy", "Administracja systemami", "Zarządzanie siecią", "Infrastruktura IT", "Zarządzanie zasadami", "Ład IT", "Automatyzacja IT", "Active Directory", "Zgodność z wymaganiami bezpieczeństwa"]
tags: ["filtrowanie WMI", "GPO", "obiekty zasad grupy", "filtry WMI", "kierowanie zasad", "zapytania WMI", "Windows Management Instrumentation", "kontrola GPO", "Konsola zarządzania zasadami grupy", "język zapytań WMI", "stosowanie zasad", "WQL", "precyzyjne dostrajanie zasad", "zarządzanie zasadami", "zasoby systemowe", "przykłady kierowania zasad", "administracja systemami", "zarządzanie siecią", "zarządzanie infrastrukturą IT", "automatyzacja IT", "zarządzanie Active Directory", "zgodność z wymaganiami bezpieczeństwa", "techniki kontroli zasad", "dobre praktyki zarządzania zasadami", "filtrowanie zasad", "strategie kontroli GPO", "bezpieczeństwo GPO", "zalety filtrowania WMI", "wdrażanie filtrowania WMI", "dobre praktyki dotyczące filtrów WMI"]
cover: "/img/cover/An_illustration_of_a_magnifying_glass_focusing.webp"
coverAlt: "Ilustracja lupy skierowanej na ikonę filtra, symbolizująca wybieranie komputerów docelowych GPO za pomocą filtrowania WMI."
coverCaption: "Użyj filtrowania WMI, aby skutecznie kierować zasady GPO do właściwych celów."
---

## Wprowadzenie

W obiektach zasad grupy (GPO) [**filtrowanie WMI**](https://simeononsecurity.com/github/wmi-filters/) określa, na których komputerach lub kontach użytkowników zostaną zastosowane zasady. Decydują o tym wyniki zapytań WMI (Windows Management Instrumentation). Administratorzy mogą dzięki temu precyzyjniej wybrać cele i zastosować zasady tylko do odpowiednich systemów. W tym artykule wyjaśniamy filtrowanie WMI, jego działanie w GPO, tworzenie [filtrów WMI](https://simeononsecurity.com/github/wmi-filters/) oraz praktyczne zastosowania.

## [Czym jest filtrowanie WMI?](https://simeononsecurity.com/github/wmi-filters/)

[**Filtrowanie WMI**](https://simeononsecurity.com/github/wmi-filters/) polega na stosowaniu filtrów do GPO na podstawie wyników zapytań WMI. WMI to wbudowana w system Windows infrastruktura zarządzania. Umożliwia administratorom pobieranie danych zarządczych i programową interakcję z zasobami systemu. Dzięki filtrowaniu WMI można dynamicznie kierować GPO na podstawie określonych kryteriów zapytań.

Filtry WMI zapisuje się w języku zapytań WMI (WQL), który stanowi podzbiór SQL (Structured Query Language). Zwykle opierają się na właściwościach i wartościach dostępnych w przestrzeni nazw WMI. Administratorzy mogą łączyć warunki, operatory logiczne i przestrzenie nazw, tworząc zapytania precyzyjnie wybierające komputery lub użytkowników.

## Jak działa filtrowanie WMI w GPO?

{{< figure src="wmi-filtering-gpo-evaluation-flow.webp" alt="Schemat pokazuje filtr WMI powiązany z obiektem zasad grupy, który ocenia zapytanie WQL jako True lub False i decyduje, czy zastosować GPO na komputerze docelowym" >}}

W zasadach grupy **filtrowanie WMI** pozwala selektywnie stosować GPO na podstawie wyników **zapytań WMI**. Po przypisaniu **filtra WMI** do GPO jego wynik **True** lub **False** określa, czy GPO zostanie zastosowane.

Filtry korzystają z **języka zapytań WMI (WQL)**, będącego podzbiorem SQL. WQL umożliwia tworzenie złożonych zapytań opartych na różnych **właściwościach** i **wartościach** dostępnych w **przestrzeni nazw WMI**. Dzięki temu można wskazać konkretne komputery lub użytkowników.

Na przykład organizacja może chcieć zastosować GPO wyłącznie na komputerach z systemem Windows 10. Może utworzyć filtr WMI, który sprawdza właściwość **OperatingSystem** klasy **Win32_OperatingSystem**. Zapytanie może wyglądać tak:

```sql
SELECT * FROM Win32_OperatingSystem WHERE Version LIKE "10.%"
```

Zapytanie sprawdza, czy wersja systemu operacyjnego zaczyna się od „10.”, co wskazuje na Windows 10. Jeśli wynik to **True**, GPO zostanie zastosowane na komputerze docelowym. W przeciwnym razie nie zostanie zastosowane.

Filtrowanie WMI obsługuje też warunki i operatory logiczne, takie jak **AND**, **OR** i **NOT**. Administratorzy mogą łączyć wiele właściwości i wartości, aby precyzyjniej kontrolować stosowanie GPO.

Różne **przestrzenie nazw WMI** zapewniają dostęp do określonych zestawów klas i właściwości WMI. Pozwala to kierować GPO na podstawie konfiguracji sprzętu, zainstalowanego oprogramowania, ustawień sieciowych i innych kryteriów.

Więcej informacji o tworzeniu filtrów i zapytań WMI zawiera dokumentacja Microsoft dotycząca [filtrowania WMI dla zasad grupy](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo).

Filtrowanie WMI umożliwia administratorom dostosowanie stosowania GPO do komputerów lub użytkowników spełniających dynamiczne warunki, co usprawnia zarządzanie środowiskiem IT.

## Tworzenie filtrów WMI dla GPO

Aby utworzyć filtr WMI dla GPO, wykonaj następujące czynności:

1. Otwórz **Konsolę zarządzania zasadami grupy** (GPMC) na komputerze z systemem Windows należącym do domeny.

2. Rozwiń domenę i przejdź do węzła **WMI Filters**.

3. Kliknij prawym przyciskiem myszy **WMI Filters** i wybierz **New**.

4. Nadaj filtrowi opisową nazwę i wpisz zapytanie WMI w polu **Query**. Użyj składni WQL.

5. Kliknij **OK**, aby zapisać filtr WMI.

Utworzony filtr można przypisać do jednej lub kilku GPO. Aby przypisać go do GPO:

1. Kliknij prawym przyciskiem myszy wybraną GPO i wybierz **Properties**.

2. W oknie właściwości GPO otwórz kartę **WMI Filtering**.

3. Wybierz żądany filtr WMI z listy.

4. Kliknij **OK**, aby zapisać zmiany.

Przypisanie filtrów WMI do GPO pozwala precyzyjnie kierować stosowanie zasad na podstawie wyników zapytań WMI.

## Ile filtrów WMI można skonfigurować dla GPO?

Administratorzy mogą skonfigurować **wiele filtrów WMI** dla jednej GPO, aby precyzyjnie określić cele zasad. Nie ma określonego limitu liczby filtrów przypisanych do pojedynczej GPO, więc można tworzyć złożone kombinacje.

Należy jednak uwzględnić wpływ liczby filtrów na czas przetwarzania GPO. Większa liczba filtrów może wydłużyć ocenę i stosowanie GPO. Aby zachować sprawne stosowanie zasad, warto ograniczyć liczbę filtrów do rozsądnej wartości.

Załóżmy, że organizacja chce stosować GPO tylko na komputerach z Windows 10, na których zainstalowano określone oprogramowanie. Może utworzyć dwa osobne filtry WMI: jeden dla **systemu operacyjnego**, a drugi dla **instalacji oprogramowania**. Ich połączenie wybierze właściwe komputery.

Ważne jest zachowanie równowagi między wymaganiami dotyczącymi wyboru celów a czasem przetwarzania. Przed określeniem liczby filtrów administratorzy powinni ocenić złożoność środowiska, liczbę komputerów lub użytkowników oraz możliwy wpływ na wydajność.

Możliwość użycia wielu filtrów WMI pomaga optymalizować wybór celów GPO i utrzymać sprawne przetwarzanie oraz zarządzanie środowiskiem IT.

## Praktyczne przykłady filtrowania WMI w GPO

Filtrowanie WMI umożliwia kierowanie zasad do wybranych celów. Oto kilka przykładów:

1. **Wybór określonych systemów operacyjnych**: aby zastosować GPO wyłącznie na komputerach z **Windows 10**, utwórz filtr sprawdzający wersję systemu, na przykład `"SELECT * FROM Win32_OperatingSystem WHERE Version LIKE '10.%'"`. W ten sposób wybierzesz komputery z Windows 10.

2. **Różne zasady dla komputerów stacjonarnych i laptopów**: jeśli te urządzenia wymagają odmiennych zasad, użyj dwóch filtrów WMI. Jeden może rozpoznawać komputery stacjonarne na podstawie atrybutów sprzętu, np. `"SELECT * FROM Win32_ComputerSystem WHERE Desktop = True"`, a drugi może wskazywać laptopy. Dzięki temu każdy typ urządzenia otrzyma odpowiednie zasady.

3. **Wybór zasad na podstawie wolnego miejsca na dysku**: aby nie stosować wymagających zasobów zasad na komputerach z małą ilością miejsca, utwórz filtr sprawdzający dostępne miejsce. Na przykład zapytanie `"SELECT * FROM Win32_LogicalDisk WHERE FreeSpace > 10737418240"` wyklucza komputery z mniej niż 10 GB wolnego miejsca.

Te przykłady pokazują elastyczność **filtrowania WMI** w GPO. Administratorzy mogą wybierać cele stosowania zasad na podstawie konkretnych kryteriów.

## Podsumowanie

Filtrowanie WMI to przydatna funkcja obiektów zasad grupy. Umożliwia administratorom selektywne stosowanie zasad na podstawie wyników zapytań WMI. Filtry kierują zasady do określonych komputerów lub użytkowników, dzięki czemu zarządzanie staje się wydajniejsze i bardziej kontrolowane. W tym artykule omówiliśmy pojęcie filtrowania WMI, jego działanie w GPO, tworzenie filtrów i praktyczne przykłady.

Włączenie filtrowania WMI do zarządzania GPO zwiększa precyzję stosowania zasad i pomaga kierować je wyłącznie do zamierzonych odbiorców.

## Źródła

- [Microsoft Docs: Tworzenie filtrów WMI dla GPO](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/create-wmi-filters-for-the-gpo)
- [Microsoft Docs: about_WQL](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_wql?view=powershell-5.1)
- [Microsoft Docs: Zasady grupy](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects)
- [Microsoft Docs: Konsola zarządzania zasadami grupy](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn265969(v=ws.11))
