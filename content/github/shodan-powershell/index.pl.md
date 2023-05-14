---
title: "Zautomatyzuj OSINT dzięki modułom Shodan PowerShell"
date: 2020-11-14
---

Kolekcja modułów PowerShell do interakcji z API Shodan

**Uwagi:**
- Będziesz potrzebował klucza API Shodan, który można znaleźć na stronie[Shodan Account](https://account.shodan.io/)
- Przykłady API używanych w modułach można znaleźć na stronie[Shodan Developers Page](https://developer.shodan.io/api)
- Niektóre moduły mogą używać kredytów skanowania lub zapytań Kredyty zapytań są używane, gdy pobierasz dane przez stronę internetową, CLI lub API (co robią te skrypty).
  Ponieważ używamy API, ważne jest, aby zauważyć, że kredyty na zapytania są odejmowane, jeśli:
  1.  Używany jest filtr wyszukiwania
  2.  Żądana jest strona 2 lub więcej
      Kredyty odnawiają się na początku miesiąca, a 1 kredyt pozwala na pobranie 100 wyników.
      Jeśli chodzi o kredyty na skanowanie, 1 kredyt na skanowanie pozwala na skanowanie 1 IP i również odnawia się na początku miesiąca.
      Proszę przejrzeć Centrum Pomocy Shodan[HERE](https://help.shodan.io/the-basics/credit-types-explained) w celu uzyskania pełnych informacji.

## Table of Contents.
-[Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
-[Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- **Moduły**.
  -[Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo) - Zwróć informacje o planie API należącym do podanego klucza API.
  -[Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders) - Pokazuje nagłówki HTTP, które klient wysyła podczas łączenia się z serwerem internetowym.
  -[Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP) - Uzyskuje aktualny adres IP widziany z Internetu.
  -[Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain) - Uzyskuje wszystkie subdomeny i inne wpisy DNS dla podanej domeny
  -[Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  -[Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse) - Wyszukuje nazwy hostów, które zostały zdefiniowane dla podanej listy adresów IP.
  -[Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount) - Wyszukuje exploity, ale zwraca tylko informacje o całkowitej liczbie dopasowań związanych z wyszukiwanym hasłem oraz opcjonalnie autora exploita, platformę, port, źródło lub typ.
  -[Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  -[Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount) - Zwraca całkowitą liczbę wyników "/shodan/host/search" zapewnia.
  -[Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP) - Szukaj Shodan z adresem IP.
  -[Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch) - Przeszukaj Shodan używając tej samej składni zapytania co strona internetowa i użyj faset, aby uzyskać informacje podsumowujące dla różnych właściwości.
  -[Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets) - Moduł ten zwraca listę filtrów wyszukiwania, które mogą być użyte w zapytaniu wyszukiwania.
  -[Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters) - Moduł ten zwraca listę filtrów wyszukiwania, które mogą być użyte w zapytaniu wyszukiwania.
  -[Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts) - Wymień wszystkie porty, które Shodan indeksuje w Internecie.
  -[Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile) - Zwraca informacje o koncie Shodan powiązanym z tym kluczem API
  -[Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID) - Sprawdź postęp wcześniej złożonego żądania skanowania
  -[Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols) - Wymień wszystkie protokoły, które mogą być używane podczas wykonywania skanowania Internetu na żądanie za pomocą Shodana
  -[Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP) - Użyj tego modułu, aby poprosić Shodana o przeszukanie sieci.

<a name="Pobierz"></a>

## Pobierz

Będziesz musiał sklonować lub pobrać skrypty na swój komputer.

Możesz użyć rozwijanego menu Code na tej stronie repo, przewijając w górę, lub po prostu skopiować i wkleić następujący link:[https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

Dla tego przykładu będziemy klonować repo w ramach Git Bash, po kliknięciu na ikonę schowka jak widać powyżej, możemy wpisać git clone i kliknąć prawym przyciskiem myszy na okno Git Bash, aby wybrać paste z rozwijanego menu:

```
exampleuser@exampleComputer MINGW64 ~/Documents/Github git clone https://github.com/simeononsecurity/Shodan_PS.git
```

Szczegółowe instrukcje dotyczące klonowania można znaleźć na stronie[the github documentation.](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

Gdy już masz pliki, musisz skopiować je do C:\Program Files \WindowsPowerShell \Moduły, wykonanie tego spowoduje wyświetlenie okna dialogowego z informacją o odmowie dostępu, kliknij przycisk kontynuuj, aby zakończyć kopiowanie plików do tej lokalizacji, a następnie przejdź do instrukcji instalacji.[here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

**OR**

Możesz użyć menu rozwijanego Code na tej stronie repo, przewijając w górę, lub po prostu kliknij następujący link:
[https://github.com/simeononsecurity/Shodan_PS/archive/main.zip](https://github.com/simeononsecurity/Shodan_PS/archive/main.zip)
![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select Download Zip option](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/downloadzip.gif?raw=true)

Rozpakuj main.zip klikając prawym przyciskiem myszy na plik i wybierając z rozwijanego menu opcję extract here.

Po uzyskaniu plików należy skopiować je do C:\Program Files \WindowsPowerShell \Moduły, wykonanie tej czynności spowoduje wyświetlenie okna dialogowego z informacją o odmowie dostępu, kliknij przycisk kontynuuj, aby zakończyć kopiowanie plików do tej lokalizacji, a następnie przejdź do instrukcji instalacji.[here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

# Install

<a name="Zainstaluj"></a>

Aby zainstalować moduły należy uruchomić okno PowerShell jako administrator.
Można to zrobić na dwa sposoby:

Pierwszy sposób polega na kliknięciu prawym przyciskiem myszy ikony PowerShell na Pulpicie i wybraniu z rozwijanego menu opcji Uruchom jako administrator.

![Right click the powershell icon on the Desktop and select run as administrator from dropdown menu](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/RcRunAsAdmin.gif?raw=true)

**OR**

Wpisując p (lub ilekolwiek znaków potrzeba, aby PowerShell się pokazał) w pasku wyszukiwania i klikając na Uruchom jako administrator.

![type p in the search bar and when powershell comes up click on run as administrator](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/SearchBarRunAsAdmin.gif?raw=true)

Musisz być w katalogu, do którego skopiowałeś skrypty.
Uruchom następujące polecenie, aby zmienić katalog roboczy:

```
PS C:\WINDOWS\system32> cd 'C:\Program Files\WindowsPowerShell\Modules\Shodan_PS'
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS>
```

Na komputerach klienckich Windows musimy zmienić politykę wykonywania PowerShell, która domyślnie jest Restricted.

Aby uzyskać więcej informacji przeczytaj[Microsoft documentation.](https:/go.microsoft.com/fwlink/?LinkID=135170)

Uruchom następujące polecenie, aby ustawić politykę na RemoteSigned i wpisz y, aby wybrać, że Tak chcesz zmienić politykę.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ExecutionPolicy RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the
security risks described in the about_Execution_Policies help topic at https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to
change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
```

Po zmianie polityki wykonania możesz uruchomić następujące polecenie, aby zaimportować moduły.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ChildItem -Recurse *.psm1 | Import-Module
```

Teraz możesz uruchomić dowolny ze skryptów jako moduł poprzez powershell.
