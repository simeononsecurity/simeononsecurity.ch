---
title: "Skrypty PowerShell: Przewodnik krok po kroku dla początkujących, jak zautomatyzować zadania"
draft: false
toc: true
date: 2023-02-25
description: "Poznaj podstawy skryptów PowerShell i zautomatyzuj zadania dzięki temu przewodnikowi krok po kroku dla początkujących, obejmującemu polecenia cmdlet, pętle, funkcje i nie tylko."
genre: ["Technologia", "Programowanie", "Automatyzacja", "Windows", "Skrypty", "IT", "Zadania administracyjne", "Zarządzanie komputerami", "Rozwój oprogramowania", "Kodowanie"]
tags: ["Skrypty PowerShell", "Automatyzacja PowerShell", "Skrypty Windows", "Polecenia cmdlet PowerShell", "Moduły PowerShell", "Pętle PowerShell", "Instrukcje warunkowe PowerShell", "Funkcje PowerShell", "Najlepsze praktyki PowerShell", "Debugowanie PowerShell", "Testowanie PowerShell", "Zmienne PowerShell", "PowerShell ISE", "Remoting PowerShell", "Technologie Microsoft", "Automatyzacja IT", "zarządzanie komputerem", "Kodowanie dla początkujących", "zadania administracyjne", "Pomysły na skrypty PowerShell", "automatyczne kopie zapasowe", "zarządzanie plikami", "informacje o systemie", "zarządzanie użytkownikami", "instalacja oprogramowania", "konfiguracja sieci", "automatyzacja zabezpieczeń", "planowanie zadań", "manipulacja rejestrem", "zdalna administracja"]
cover: "/img/cover/A_cartoon_character_holding_a_script_and_standing.png"
coverAlt: "Postać z kreskówki trzymająca skrypt i stojąca przed komputerem z monitem PowerShell, wskazująca na łatwość tworzenia skryptów PowerShell dla początkujących"
coverCaption: ""
---
 Skrypty PowerShell dla początkujących**

PowerShell to potężna powłoka wiersza poleceń i język skryptowy opracowany przez firmę Microsoft. Zapewnia on szeroką gamę poleceń i funkcji do zarządzania i automatyzacji różnych aspektów systemu operacyjnego Windows i innych technologii Microsoft. W tym artykule omówimy podstawy skryptów PowerShell dla początkujących i przedstawimy przewodnik krok po kroku, aby rozpocząć.

## Wprowadzenie do PowerShell

**PowerShell** to powłoka wiersza poleceń, która umożliwia użytkownikom automatyzację i zarządzanie systemem operacyjnym Windows i innymi technologiami Microsoft. Zapewnia kompleksowy zestaw poleceń i funkcji, które umożliwiają użytkownikom wykonywanie różnych zadań administracyjnych, takich jak zarządzanie plikami i katalogami, konfiguracja sieci i zarządzanie systemem. PowerShell obsługuje również język skryptowy, który pozwala użytkownikom tworzyć złożone skrypty i automatyzować różne powtarzalne zadania.

## Pierwsze kroki z PowerShell

### Instalacja PowerShell

PowerShell jest preinstalowany w większości wersji systemu operacyjnego Windows. Jeśli jednak używasz starszej wersji Windows lub potrzebujesz nowszej wersji PowerShell, możesz pobrać ją ze strony Microsoft. Aby pobrać i zainstalować PowerShell, wykonaj następujące kroki:

1. Przejdź do strony [Microsoft PowerShell website](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2) i wybierz wersję PowerShell, którą chcesz zainstalować.
2. Pobierz plik instalacyjny i uruchom go.
3. Postępuj zgodnie z instrukcjami wyświetlanymi na ekranie, aby zakończyć proces instalacji.

### Uruchamianie PowerShell

Po zainstalowaniu PowerShell można go uruchomić, wykonując następujące kroki:

1. Kliknij menu Start i wpisz "PowerShell" w pasku wyszukiwania.
2. Wybierz "Windows PowerShell" z wyników wyszukiwania.
3. PowerShell otworzy się w nowym oknie.

### Podstawy PowerShell

PowerShell zapewnia interfejs wiersza poleceń, który pozwala użytkownikom na interakcję z systemem operacyjnym. Polecenia w PowerShell nazywane są cmdletami i są zorganizowane w moduły. Aby wyświetlić listę dostępnych modułów, należy użyć polecenia Get-Module:

```powershell
Get-Module
```

Aby wyświetlić listę dostępnych poleceń cmdlet w module, użyj polecenia Get-Command:
```powershell
Get-Command -Module <module name>
```

Aby uzyskać pomoc dotyczącą polecenia cmdlet, użyj polecenia Get-Help:
```powershell
Get-Help <cmdlet name>
```

PowerShell obsługuje również aliasy, które są krótszymi nazwami poleceń cmdlet. Aby wyświetlić listę dostępnych aliasów, należy użyć polecenia Get-Alias:
```powershell
Get-Alias
```

### Skrypty PowerShell
Skrypty PowerShell to potężna funkcja, która pozwala użytkownikom automatyzować różne zadania administracyjne. Skrypty PowerShell obsługują zmienne, pętle, instrukcje warunkowe i funkcje, co czyni je potężnym narzędziem do automatyzacji.

#### Zmienne
Zmienne są używane do przechowywania danych w skryptach PowerShell. Zmienne w PowerShell zaczynają się od znaku dolara ($). Aby przypisać wartość do zmiennej, należy użyć następującej składni:
```powershell
$variable_name = value
```
Na przykład:
```powershell
$name = "John"
```
#### Pętle
Pętle służą do powtarzania bloku kodu określoną liczbę razy. PowerShell obsługuje następujące typy pętli:

- **For loop**: powtarza blok kodu określoną liczbę razy.
- **Pętla While**: powtarza blok kodu tak długo, jak warunek jest prawdziwy.
- **Pętla Do-While**: powtarza blok kodu co najmniej raz, a następnie tak długo, jak warunek jest prawdziwy.
- **orEach loop**: powtarza blok kodu dla każdego elementu w kolekcji.
  
Na przykład, poniższy kod używa pętli For do wypisania liczb od 1 do 5:
```powershell
for($i=1; $i -le 5; $i++) {
Write-Host $i
}
```

#### Instrukcje warunkowe

Stwierdzenia warunkowe

Instrukcje warunkowe służą do wykonywania bloku kodu, jeśli określony warunek jest prawdziwy. PowerShell obsługuje następujące typy instrukcji warunkowych:

- **If statement**: wykonuje blok kodu, jeśli warunek jest prawdziwy.
- **If-Else statement**: wykonuje jeden blok kodu, jeśli warunek jest prawdziwy i inny blok kodu, jeśli warunek jest fałszywy.
- **Switch statement**: porównuje wartość z zestawem możliwych dopasowań i wykonuje blok kodu dla pierwszego znalezionego dopasowania.

Na przykład poniższy kod używa instrukcji If do sprawdzenia, czy liczba jest większa niż 5:

```powershell
$number = 10
if ($number -gt 5) {
    Write-Host "The number is greater than 5"
}
```
#### Funkcje
Funkcje to bloki kodu wielokrotnego użytku, które wykonują określone zadanie. Funkcje przyjmują parametry wejściowe i zwracają wartości wyjściowe. PowerShell obsługuje następujące typy funkcji:

- **Blok skryptu**: blok kodu, który można wykonać.
- Funkcja zaawansowana**: funkcja zawierająca metadane i walidację parametrów.

Na przykład poniższy kod definiuje funkcję, która dodaje dwie liczby:
```powershell
function Add-Numbers {
    param (
        [int]$num1,
        [int]$num2
    )
    $result = $num1 + $num2
    return $result
}

$result = Add-Numbers -num1 5 -num2 10
Write-Host "The result is $result"
```
### PowerShell ISE
PowerShell ISE (Integrated Scripting Environment) to graficzny interfejs użytkownika dla skryptów PowerShell. PowerShell ISE zapewnia bogaty edytor tekstu, narzędzia do debugowania i inne funkcje, które ułatwiają pisanie i testowanie skryptów PowerShell. Aby otworzyć PowerShell ISE, wykonaj następujące kroki:

1. Kliknij menu Start i wpisz "PowerShell ISE" w pasku wyszukiwania.
2. Wybierz "Windows PowerShell ISE" z wyników wyszukiwania.
3. PowerShell ISE otworzy się w nowym oknie.

### Remoting PowerShell
PowerShell Remoting pozwala użytkownikom uruchamiać polecenia i skrypty PowerShell na zdalnych komputerach. PowerShell Remoting wymaga, aby usługa WinRM była uruchomiona zarówno na komputerze lokalnym, jak i zdalnym. Aby włączyć PowerShell Remoting, wykonaj następujące kroki:

1. Otwórz wiersz polecenia PowerShell z uprawnieniami administratora.
2. Uruchom następujące polecenie, aby włączyć funkcję PowerShell Remoting:
```powershell
   Enable-PSRemoting -Force
```
3. Uruchom następujące polecenie, aby dodać komputer zdalny do listy TrustedHosts:
```powershell
Set-Item wsman:\localhost\Client\TrustedHosts -Value <computer name> -Force
```
4. Uruchom ponownie usługę WinRM
```powershell
Restart-Service WinRM
```

Aby uruchomić polecenie PowerShell na zdalnym komputerze, użyj polecenia cmdlet Invoke-Command:
```powershell
Invoke-Command -ComputerName <computer name> -ScriptBlock { <command> }
```
### Moduły PowerShell
Moduły PowerShell to zbiory poleceń cmdlet, funkcji i skryptów zaprojektowanych do wykonywania określonych zadań. Moduły PowerShell można instalować i zarządzać nimi za pomocą galerii PowerShell, która jest centralnym repozytorium modułów PowerShell.

Aby zainstalować moduł PowerShell z galerii PowerShell, należy użyć następującego polecenia:
```powershell
Install-Module <module name>
```

Aby wyświetlić listę zainstalowanych modułów PowerShell, użyj polecenia Get-InstalledModule:
```powershell
Get-InstalledModule
```

### Najlepsze praktyki dla skryptów PowerShell

Podczas pisania **skryptów PowerShell** ważne jest, aby przestrzegać najlepszych praktyk w celu zapewnienia, że skrypty są **bezpieczne**, **niezawodne** i **możliwe do utrzymania**. Oto kilka najlepszych praktyk, o których należy pamiętać:

- **Używaj opisowych nazw zmiennych**: Używaj nazw zmiennych, które jasno wskazują ich cel.
- Używaj komentarzy**: Używaj komentarzy, aby wyjaśnić cel kodu.
- **Używaj obsługi błędów**: Używaj obsługi błędów, aby z wdziękiem obsługiwać błędy i wyjątki. The `Try...Catch...Finally` w PowerShell umożliwia obsługę wyjątków i podejmowanie odpowiednich działań. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-try-catch-finally?view=powershell-7.1)
- **Dokładne testowanie skryptów**: Dokładnie testuj skrypty, aby upewnić się, że działają zgodnie z oczekiwaniami. Możesz użyć **Pester**, frameworka testowego dla PowerShell, aby napisać i uruchomić testy jednostkowe dla swoich skryptów. [Pester Documentation](https://pester.dev/)
- **Używaj funkcji i modułów**: Używaj funkcji i modułów do organizowania kodu i poprawy możliwości jego ponownego wykorzystania. Funkcje pozwalają podzielić kod na mniejsze, łatwe w zarządzaniu fragmenty, podczas gdy moduły zapewniają sposób na pakowanie i dystrybucję kodu. [About Functions](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-functions?view=powershell-7.1), [About Modules](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-modules?view=powershell-7.1)
- **Unikaj twardego kodowania wartości**: Unikaj twardego kodowania wartości w skrypcie i zamiast tego używaj parametrów lub zmiennych. Sprawia to, że skrypty są bardziej elastyczne i wielokrotnego użytku. Parametry można przekazywać do skryptów za pomocą funkcji `param` słowo kluczowe. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters?view=powershell-7.1)
- **Użyj pełnych danych wyjściowych**: Użyj pełnego wyjścia, aby dostarczyć dodatkowych informacji o postępie skryptu. Można użyć opcji `Write-Verbose` aby wyświetlać szczegółowe komunikaty podczas wykonywania skryptu. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-verbose?view=powershell-7.1)

Przestrzeganie tych najlepszych praktyk pomoże ci pisać bardziej wydajne i łatwe w utrzymaniu skrypty PowerShell, zwiększając twoją produktywność i zapewniając stabilność zadań automatyzacji.

### Opracowanie najlepszych praktyk dla skryptów PowerShell

#### Używaj obsługi błędów
Obsługa błędów jest krytycznym aspektem skryptów PowerShell, ponieważ zapewnia, że skrypt z wdziękiem obsługuje błędy i wyjątki. PowerShell zapewnia kilka sposobów obsługi błędów, w tym instrukcję Try-Catch, instrukcję Trap i parametr ErrorAction. Instrukcja Try-Catch służy do wychwytywania i obsługi wyjątków, natomiast instrukcja Trap służy do wychwytywania i obsługi błędów. Parametr ErrorAction służy do kontrolowania sposobu obsługi błędów przez skrypt.

Oto przykład użycia instrukcji Try-Catch do sprawnej obsługi błędu:
```powershell
try {
    # some code that might throw an error
}
catch {
    Write-Error "An error occurred: $_"
}
```

#### Skrypty testowe dokładnie

Testowanie skryptów PowerShell jest niezbędne, aby upewnić się, że działają one zgodnie z oczekiwaniami. PowerShell udostępnia kilka narzędzi testowych i frameworków, takich jak Pester, które umożliwiają użytkownikom pisanie i wykonywanie testów skryptów. Narzędzia te pomagają zidentyfikować i wyizolować błędy w kodzie oraz upewnić się, że skrypt spełnia pożądane wymagania.

Oto przykład użycia Pester do testowania skryptu PowerShell:
```powershell
Describe "My PowerShell Script" {
    It "Does something" {
        # some code that should return the expected result
        $result = Do-Something
        $result | Should -Be "expected result"
    }
}
```

#### Używanie funkcji i modułów
Funkcje i moduły są niezbędne do organizowania kodu i poprawy możliwości jego ponownego wykorzystania w skryptach PowerShell. Funkcje umożliwiają użytkownikom grupowanie kodu w bloki wielokrotnego użytku, podczas gdy moduły umożliwiają użytkownikom pakowanie i udostępnianie kodu innym. Korzystając z funkcji i modułów, skrypty PowerShell mogą być bardziej modułowe, wydajne i łatwe w utrzymaniu.

Oto przykład użycia funkcji w PowerShell:
```powershell
function Get-ProcessCount {
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount
Write-Host "There are $count processes running."
```

#### Unikaj twardego kodowania wartości
Zakodowane na stałe wartości w skrypcie PowerShell sprawiają, że jest on mniej elastyczny i trudniejszy w utrzymaniu. Zamiast zakodowanych na stałe wartości, najlepiej jest używać parametrów lub zmiennych, które umożliwiają użytkownikom przekazywanie wartości do skryptu w czasie wykonywania. Używając parametrów lub zmiennych, skrypt może być bardziej wielokrotnego użytku i dostosowany do zmieniających się warunków.

Oto przykład użycia parametru w PowerShell:
```powershell
param (
    [string]$name
)

Write-Host "Hello, $name!"
```

#### Korzystanie z pełnych danych wyjściowych
Pełne dane wyjściowe dostarczają dodatkowych informacji o postępie skryptu, co może być przydatne do debugowania i rozwiązywania problemów. PowerShell udostępnia cmdlet Write-Verbose, który umożliwia użytkownikom wysyłanie pełnych informacji do konsoli. Korzystając z pełnych danych wyjściowych, skrypty PowerShell mogą być bardziej pouczające i łatwiejsze do debugowania.

Oto przykład użycia pełnych danych wyjściowych w PowerShell:
```powershell
function Get-ProcessCount {
    Write-Verbose "Getting processes..."
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount -Verbose
Write-Host "There are $count processes running."
```

### Dziesięć pomysłów na skrypty PowerShell dla początkujących

Jeśli jesteś początkującym użytkownikiem skryptów PowerShell, oto dziesięć pomysłów na skrypty, które pomogą ci zacząć:

- **Automatyczne kopie zapasowe**: Utwórz skrypt, który zautomatyzuje proces tworzenia kopii zapasowych ważnych plików i katalogów na zewnętrznym dysku twardym lub w chmurze. Możesz użyć `Copy-Item` cmdlet do kopiowania plików i `Start-Job` aby uruchomić proces tworzenia kopii zapasowej w tle. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.1)

- **Zarządzanie plikami**: Utwórz skrypt, który organizuje pliki i katalogi, sortując je w różnych folderach na podstawie typu pliku, rozmiaru lub innych kryteriów. Można użyć funkcji `Get-ChildItem` cmdlet do pobierania plików i polecenie `Move-Item` cmdlet, aby przenieść je do wybranej lokalizacji. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item?view=powershell-7.1)

- **Informacje systemowe**: Utwórz skrypt, który pobiera informacje systemowe, takie jak użycie procesora i pamięci, miejsce na dysku i ustawienia sieciowe, i wyświetla je w łatwym do odczytania formacie. Możesz użyć `Get-WmiObject` cmdlet do zbierania informacji systemowych i formatowania ich przy użyciu `Format-Table` lub `Out-GridView` [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-7.1)

- **Zarządzanie użytkownikami**: Utwórz skrypt automatyzujący proces dodawania, modyfikowania lub usuwania użytkowników i grup w systemie operacyjnym Windows. Można użyć `New-LocalUser` `Set-LocalUser` oraz `Remove-LocalUser` do zarządzania użytkownikami, oraz `New-LocalGroup` `Add-LocalGroupMember` oraz `Remove-LocalGroup` do zarządzania grupami. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localuser?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localgroup?view=powershell-7.1)

- **Instalacja oprogramowania**: Utwórz skrypt, który instaluje i konfiguruje oprogramowanie na wielu komputerach jednocześnie, oszczędzając czas i wysiłek. Możesz użyć `Invoke-Command` do wykonywania poleceń instalacyjnych na komputerach zdalnych. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

- **Konfiguracja sieci**: Utwórz skrypt automatyzujący proces konfiguracji ustawień sieciowych, takich jak adres IP, maska podsieci i brama domyślna. Można użyć `Set-NetIPAddress` `Set-NetIPInterface` oraz `Set-DnsClientServerAddress` aby skonfigurować ustawienia sieciowe. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipaddress?view=win10-ps), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipinterface?view=win10-ps), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/dnsclient/set-dnsclientserveraddress?view=win10-ps)

- **Bezpieczeństwo**: Utwórz skrypt, który przeprowadza audyt i monitoruje ustawienia zabezpieczeń oraz ostrzega użytkownika w przypadku wykrycia jakichkolwiek zmian. Można użyć funkcji `Get-AuditPolicy` cmdlet w celu pobrania zasad audytu i `Send-MailMessage` cmdlet do wysyłania powiadomień e-mail. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-auditpolicy?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/send-mailmessage?view=powershell-7.1)

- **Planowanie zadań**: Utwórz skrypt, który zaplanuje i zautomatyzuje powtarzające się zadania, takie jak kopie zapasowe, aktualizacje i skanowanie systemu. Możesz użyć funkcji `Register-ScheduledTask` cmdlet do tworzenia zaplanowanych zadań oraz `Start-ScheduledTask` cmdlet, aby je wykonać. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/register-scheduledtask?view=win10-ps), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/start-scheduledtask?view=win10-ps)

- **Manipulacja rejestrem**: Tworzenie skryptu, który modyfikuje lub pobiera wartości rejestru dla określonych kluczy lub wartości. Można użyć funkcji `Get-ItemProperty` i `Set-ItemProperty` do interakcji z rejestrem. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-itemproperty?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-itemproperty?view=powershell-7.1)

- Zdalna administracja**: Utwórz skrypt, który umożliwia zdalną administrację komputerami z systemem Windows, pozwalając użytkownikom na wykonywanie poleceń i skryptów na zdalnych maszynach. Można użyć funkcji `Enter-PSSession` cmdlet lub `Invoke-Command` do uruchamiania poleceń na komputerach zdalnych. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enter-pssession?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

Zacznij odkrywać te pomysły na skrypty, aby zdobyć praktyczne doświadczenie i rozwinąć swoje umiejętności PowerShell.

## Wnioski

PowerShell to potężne narzędzie do zarządzania i automatyzacji systemu operacyjnego Windows i innych technologii Microsoft. W tym artykule omówiliśmy podstawy tworzenia skryptów PowerShell dla początkujących, w tym instalację i uruchamianie PowerShell, korzystanie z poleceń cmdlet, zmiennych, pętli, instrukcji warunkowych i funkcji oraz korzystanie z PowerShell ISE, PowerShell Remoting i modułów PowerShell. Przestrzegając najlepszych praktyk, skrypty PowerShell mogą być bezpieczne, niezawodne i łatwe w utrzymaniu. Dzięki praktyce można stać się biegłym w skryptach PowerShell i z łatwością automatyzować różne zadania administracyjne.
