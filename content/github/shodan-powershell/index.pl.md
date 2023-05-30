---
title: "Automatyzacja OSINT za pomocą modułów Shodan PowerShell"
date: 2020-11-14
---

Kolekcja modułów PowerShell do interakcji z interfejsem API Shodan

**Uwagi:**
- Będziesz potrzebował klucza API Shodan, który można znaleźć na stronie [Shodan Account](https://account.shodan.io/)
- Przykłady interfejsów API używanych w modułach można znaleźć na stronie [Shodan Developers Page](https://developer.shodan.io/api)
- Niektóre moduły mogą używać kredytów skanowania lub zapytań Kredyty zapytań są używane podczas pobierania danych za pośrednictwem strony internetowej, CLI lub API (co robią te skrypty).
  Ponieważ korzystamy z API, ważne jest, aby pamiętać, że kredyty zapytań są odejmowane, jeśli:
  1.  Używany jest filtr wyszukiwania
  2.  Żądana jest strona 2 lub wyższa
      Kredyty odnawiają się na początku miesiąca, a 1 kredyt pozwala pobrać 100 wyników.
      Jeśli chodzi o kredyty skanowania, 1 kredyt skanowania pozwala zeskanować 1 IP i również odnawia się na początku miesiąca.
      Zobacz Centrum pomocy Shodan [HERE](https://help.shodan.io/the-basics/credit-types-explained) aby uzyskać szczegółowe informacje.

## Spis treści
- [Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
- [Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- **Moduły**
  - [Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo) - Zwraca informacje o planie API należącym do podanego klucza API.
  - [Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders) - Wyświetla nagłówki HTTP wysyłane przez klienta podczas łączenia się z serwerem WWW.
  - [Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP) - Pobiera bieżący adres IP widziany z Internetu.
  - [Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain) - Pobiera wszystkie subdomeny i inne wpisy DNS dla danej domeny
  - [Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  - [Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse) - Wyszukuje nazwy hostów zdefiniowane dla podanej listy adresów IP.
  - [Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount) - Wyszukuje exploity, ale zwraca tylko informacje o całkowitej liczbie dopasowań związanych z wyszukiwanym terminem i opcjonalnie o autorze exploita, platformie, porcie, źródle lub typie.
  - [Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  - [Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount) - Zwraca całkowitą liczbę wyników wyszukiwania "/shodan/host/search".
  - [Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP) - Wyszukaj Shodan za pomocą adresu IP.
  - [Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch) - Przeszukuj Shodan przy użyciu tej samej składni zapytań co na stronie internetowej i używaj aspektów, aby uzyskać podsumowanie informacji dla różnych właściwości.
  - [Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets) - Moduł ten zwraca listę filtrów wyszukiwania, które mogą być użyte w zapytaniu.
  - [Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters) - Moduł ten zwraca listę filtrów wyszukiwania, które mogą być użyte w zapytaniu.
  - [Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts) - Lista wszystkich portów, które Shodan indeksuje w Internecie.
  - [Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile) - Zwraca informacje o koncie Shodan powiązanym z tym kluczem API
  - [Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID) - Sprawdzanie postępu wcześniej przesłanego żądania skanowania
  - [Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols) - Wymień wszystkie protokoły, które mogą być używane podczas skanowania Internetu na żądanie za pomocą aplikacji Shodan
  - [Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP) - Użyj tego modułu, aby poprosić Shodan o przeszukanie sieci.

<a name="Download"></a>

## Download

Będziesz musiał sklonować lub pobrać skrypty na swój komputer.

Możesz użyć rozwijanego menu Kod na tej stronie repozytorium, przewijając w górę, lub po prostu skopiować i wkleić poniższy link: [https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

W tym przykładzie będziemy klonować repozytorium w Git Bash, po kliknięciu ikony schowka, jak pokazano powyżej, możemy wpisać git clone i kliknąć prawym przyciskiem myszy okno Git Bash, aby wybrać wklej z menu rozwijanego:

```
exampleuser@exampleComputer MINGW64 ~/Documents/Github git clone https://github.com/simeononsecurity/Shodan_PS.git
```

Aby uzyskać szczegółowe instrukcje dotyczące klonowania, zobacz [the github documentation.](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

Po uzyskaniu plików należy skopiować je do C:\Program Files\WindowsPowerShell\Modules, co spowoduje wyświetlenie okna dialogowego z informacją o odmowie dostępu, kliknij Kontynuuj, aby zakończyć kopiowanie plików do tej lokalizacji, a następnie przejdź do instrukcji instalacji [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

**OR**

Możesz użyć rozwijanego menu Kod na tej stronie repozytorium, przewijając w górę lub po prostu klikając poniższy link:
[https://github.com/simeononsecurity/Shodan_PS/archive/main.zip](https://github.com/simeononsecurity/Shodan_PS/archive/main.zip)
![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select Download Zip option](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/downloadzip.gif?raw=true)

Rozpakuj plik main.zip, klikając go prawym przyciskiem myszy i wybierając z menu rozwijanego opcję Wypakuj tutaj.

Po uzyskaniu plików należy je skopiować do C:\Program Files\WindowsPowerShell\Modules, co spowoduje wyświetlenie okna dialogowego z informacją o odmowie dostępu, kliknij Kontynuuj, aby zakończyć kopiowanie plików do tej lokalizacji, a następnie przejdź do instrukcji instalacji [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

# Install

<a name="Install"></a>

Aby zainstalować moduły, należy uruchomić okno PowerShell jako administrator.
Można to zrobić na dwa sposoby:

Pierwszym sposobem jest kliknięcie prawym przyciskiem myszy ikony PowerShell na pulpicie i wybranie opcji Uruchom jako administrator z menu rozwijanego.

![Right click the powershell icon on the Desktop and select run as administrator from dropdown menu](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/RcRunAsAdmin.gif?raw=true)

**OR**

Wpisując p (lub dowolną liczbę znaków potrzebną do wyświetlenia PowerShell) w pasku wyszukiwania i klikając Uruchom jako administrator.

![type p in the search bar and when powershell comes up click on run as administrator](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/SearchBarRunAsAdmin.gif?raw=true)

Będziesz musiał znajdować się w katalogu, do którego skopiowałeś skrypty.
Uruchom następujące polecenie, aby zmienić katalog roboczy:

```
PS C:\WINDOWS\system32> cd 'C:\Program Files\WindowsPowerShell\Modules\Shodan_PS'
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS>
```

Na komputerach klienckich z systemem Windows musimy zmienić zasady wykonywania PowerShell, które domyślnie są ograniczone.

Więcej informacji można znaleźć tutaj [Microsoft documentation.](https:/go.microsoft.com/fwlink/?LinkID=135170)

Uruchom następujące polecenie, aby ustawić politykę na RemoteSigned i wpisz y, aby wybrać Tak, aby zmienić politykę.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ExecutionPolicy RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the
security risks described in the about_Execution_Policies help topic at https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to
change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
```

Po zmianie zasad wykonywania można uruchomić następujące polecenie, aby zaimportować moduły.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ChildItem -Recurse *.psm1 | Import-Module
```

Teraz możesz uruchomić dowolny skrypt jako moduł za pomocą powershell.
