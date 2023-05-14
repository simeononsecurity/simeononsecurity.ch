---
title: "PowerShell Scripting dla początkujących: Przewodnik krok po kroku"
draft: false
toc: true
date: 2023-02-25
description: "Poznaj podstawy skryptów PowerShell i rozpocznij automatyzację, korzystając z tego przewodnika krok po kroku."
tags: ["PowerShell", "skryptowanie", "Windows", "automatyka", "cmdlets", "moduły", "pętle", "oświadczenia warunkowe", "funkcje", "najlepsze praktyki", "debugowanie", "testowanie", "zmienne", "PowerShell ISE", "Zdalne sterowanie w PowerShell", "Technologie Microsoft", "IT", "zarządzanie komputerem", "kodowanie", "zadania administracyjne"]
cover: "/img/cover/A_cartoon_character_holding_a_script_and_standing.png"
coverAlt: "Postać z kreskówki trzymająca skrypt i stojąca przed komputerem z monitem PowerShell, wskazująca na łatwość pisania skryptów PowerShell dla początkujących"
coverCaption: ""
---
 Skryptowanie w PowerShell dla początkujących**

PowerShell jest potężną powłoką wiersza poleceń i językiem skryptowym opracowanym przez Microsoft. Zapewnia on szeroki wachlarz poleceń i funkcji do zarządzania i automatyzacji różnych aspektów systemu operacyjnego Windows i innych technologii Microsoftu. W tym artykule omówimy podstawy skryptów PowerShell dla początkujących i przedstawimy przewodnik krok po kroku, jak zacząć.

## Wprowadzenie do PowerShella

PowerShell jest powłoką wiersza poleceń, która umożliwia użytkownikom automatyzację i zarządzanie systemem operacyjnym Windows oraz innymi technologiami firmy Microsoft. Zapewnia kompleksowy zestaw poleceń i funkcji, które umożliwiają użytkownikom wykonywanie różnych zadań administracyjnych, takich jak zarządzanie plikami i katalogami, konfiguracja sieci oraz zarządzanie systemem. PowerShell obsługuje również język skryptowy, który pozwala użytkownikom tworzyć złożone skrypty i automatyzować różne powtarzalne zadania.

## Rozpoczęcie pracy z PowerShellem

### Instalowanie PowerShella

PowerShell jest preinstalowany w większości wersji systemu operacyjnego Windows. Jeśli jednak używasz starszej wersji systemu Windows lub potrzebujesz nowszej wersji PowerShella, możesz ją pobrać z witryny firmy Microsoft. Aby pobrać i zainstalować PowerShell, wykonaj następujące kroki:

1. Przejdź do.[Microsoft PowerShell website](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2) i wybierz wersję PowerShell, którą chcesz zainstalować.
2. Pobierz plik instalacyjny i uruchom go.
3. Postępuj zgodnie z instrukcjami wyświetlanymi na ekranie, aby zakończyć proces instalacji.

### Uruchomienie PowerShell

Po zainstalowaniu programu PowerShell można go uruchomić, wykonując poniższe kroki:

1. Kliknij menu Start i w pasku wyszukiwania wpisz "PowerShell".
2. Z wyników wyszukiwania wybierz "Windows PowerShell".
3. PowerShell otworzy się w nowym oknie.

### Podstawy PowerShell

PowerShell zapewnia interfejs wiersza poleceń, który pozwala użytkownikom na interakcję z systemem operacyjnym. Polecenia w PowerShell nazywane są cmdletami i są zorganizowane w moduły. Aby wyświetlić listę dostępnych modułów, należy użyć polecenia Get-Module:

```powershell
Get-Module
```

Aby wyświetlić listę dostępnych cmdletów w module, należy użyć polecenia Get-Command:
```powershell
Get-Command -Module <module name>
```

Aby uzyskać pomoc dotyczącą cmdleta, należy użyć polecenia Get-Help:
```powershell
Get-Help <cmdlet name>
```

PowerShell obsługuje również aliasy, które są krótszymi nazwami dla cmdletów. Aby wyświetlić listę dostępnych aliasów, należy użyć polecenia Get-Alias:
```powershell
Get-Alias
```

### Skryptowanie PowerShell
Skryptowanie w PowerShell to potężna funkcja, która pozwala użytkownikom zautomatyzować różne zadania administracyjne. Skrypty PowerShell obsługują zmienne, pętle, instrukcje warunkowe i funkcje, co czyni je potężnym narzędziem do automatyzacji.

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
Pętle są używane do powtarzania bloku kodu określoną liczbę razy. PowerShell obsługuje następujące typy pętli:

- **Pętla for**: powtarza blok kodu przez określoną liczbę razy.
- **Pętla While**: powtarza blok kodu tak długo, jak długo warunek jest prawdziwy.
- **Pętla Do-While**: powtarza blok kodu co najmniej raz, a następnie tak długo, jak warunek jest prawdziwy.
- **PętlaorEach**: powtarza blok kodu dla każdego elementu w kolekcji.
  
Na przykład poniższy kod wykorzystuje pętlę For do wypisania liczb od 1 do 5:
```powershell
for($i=1; $i -le 5; $i++) {
Write-Host $i
}
```

#### Oświadczenia warunkowe

Wypowiedzi warunkowe

Instrukcje warunkowe są używane do wykonania bloku kodu, jeśli pewien warunek jest prawdziwy. PowerShell obsługuje następujące typy instrukcji warunkowych:

- **If statement**: wykonuje blok kodu, jeśli warunek jest prawdziwy.
- **Konstrukcja If-Else**: wykonuje jeden blok kodu, jeśli warunek jest prawdziwy, a drugi blok kodu, jeśli warunek jest fałszywy.
- **Konstrukcja przełączająca**: porównuje wartość z zestawem możliwych dopasowań i wykonuje blok kodu dla pierwszego znalezionego dopasowania.

Na przykład, następujący kod używa instrukcji If do sprawdzenia, czy liczba jest większa niż 5:

```powershell
$number = 10
if ($number -gt 5) {
    Write-Host "The number is greater than 5"
}
```
#### Funkcje
Funkcje są blokami kodu wielokrotnego użytku, które wykonują określone zadanie. Funkcje pobierają parametry wejściowe i zwracają wartości wyjściowe. PowerShell obsługuje następujące typy funkcji:

- **Blok skryptu**: blok kodu, który może zostać wykonany.
- Funkcja zaawansowana**: funkcja, która zawiera metadane i walidację parametrów.

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
PowerShell ISE (Integrated Scripting Environment) jest graficznym interfejsem użytkownika dla skryptów PowerShell. PowerShell ISE zapewnia edytor bogatego tekstu, narzędzia do debugowania i inne funkcje, które ułatwiają pisanie i testowanie skryptów PowerShell. Aby otworzyć PowerShell ISE, wykonaj następujące kroki:

1. Kliknij menu Start i wpisz "PowerShell ISE" w pasku wyszukiwania.
2. Z wyników wyszukiwania wybierz "Windows PowerShell ISE".
3. PowerShell ISE otworzy się w nowym oknie.

### PowerShell Remoting
PowerShell Remoting umożliwia użytkownikom uruchamianie poleceń i skryptów PowerShell na zdalnych komputerach. PowerShell Remoting wymaga, aby usługa WinRM była uruchomiona zarówno na komputerze lokalnym, jak i zdalnym. Aby włączyć usługę PowerShell Remoting, wykonaj następujące kroki:

1. Otwórz monit PowerShell z uprawnieniami administratora.
2. Uruchom następujące polecenie, aby włączyć funkcję PowerShell Remoting:
```powershell
   Enable-PSRemoting -Force
```
3. Uruchom następujące polecenie, aby dodać zdalny komputer do listy TrustedHosts:
```powershell
Set-Item wsman:\localhost\Client\TrustedHosts -Value <computer name> -Force
```
4. Uruchom ponownie usługę WinRM
```powershell
Restart-Service WinRM
```

Aby uruchomić polecenie PowerShell na zdalnym komputerze, należy użyć cmdleta Invoke-Command:
```powershell
Invoke-Command -ComputerName <computer name> -ScriptBlock { <command> }
```
### Moduły PowerShell
Moduły PowerShell to zbiory cmdletów, funkcji i skryptów, które zostały zaprojektowane do wykonywania określonych zadań. Moduły PowerShell mogą być instalowane i zarządzane za pomocą Galerii PowerShell, która jest centralnym repozytorium modułów PowerShell.

Aby zainstalować moduł PowerShell z Galerii PowerShell, należy użyć następującego polecenia:
```powershell
Install-Module <module name>
```

Aby wyświetlić listę zainstalowanych modułów PowerShell, należy użyć polecenia Get-InstalledModule:
```powershell
Get-InstalledModule
```

### Najlepsze praktyki pisania skryptów w PowerShell
Podczas pisania skryptów PowerShell ważne jest przestrzeganie najlepszych praktyk, aby zapewnić, że skrypty są bezpieczne, niezawodne i możliwe do utrzymania. Oto kilka najlepszych praktyk, o których należy pamiętać:

Używaj opisowych nazw zmiennych: Używaj nazw zmiennych, które jasno wskazują na ich cel.
Używaj komentarzy: Używaj komentarzy, aby wyjaśnić cel kodu.
- **Use error handling**: Używaj obsługi błędów, aby z wdziękiem obsługiwać błędy i wyjątki.
- **Dokładnie testuj skrypty**: Dokładnie testuj skrypty, aby upewnić się, że działają zgodnie z oczekiwaniami.
- **Używaj funkcji i modułów**: Używaj funkcji i modułów, aby uporządkować kod i poprawić możliwość ponownego wykorzystania.
- **Unikaj hardcodowania wartości**: Unikaj hardcodowania wartości w skrypcie i zamiast tego używaj parametrów lub zmiennych.
- **Używaj verbose output**: Użyj verbose output, aby dostarczyć dodatkowych informacji o postępach skryptu.

### Opracowanie najlepszych praktyk dla skryptów PowerShell

#### Używaj obsługi błędów
Obsługa błędów jest krytycznym aspektem skryptów PowerShell, ponieważ zapewnia, że skrypt z wdziękiem obsługuje błędy i wyjątki. PowerShell udostępnia kilka sposobów obsługi błędów, w tym instrukcję Try-Catch, instrukcję Trap oraz parametr ErrorAction. Instrukcja Try-Catch służy do łapania i obsługi wyjątków, natomiast instrukcja Trap służy do łapania i obsługi błędów. Parametr ErrorAction służy do kontroli sposobu obsługi błędów przez skrypt.

Oto przykład użycia instrukcji Try-Catch do zgrabnej obsługi błędu:
```powershell
try {
    # some code that might throw an error
}
catch {
    Write-Error "An error occurred: $_"
}
```

#### Skrypty testowe dokładnie

Testowanie skryptów PowerShell jest niezbędne, aby zapewnić, że działają one zgodnie z oczekiwaniami. PowerShell dostarcza kilka narzędzi testujących i frameworków, takich jak Pester, które umożliwiają użytkownikom pisanie i wykonywanie testów dla ich skryptów. Narzędzia te pomagają zidentyfikować i wyizolować problemy w kodzie oraz zapewnić, że skrypt spełnia pożądane wymagania.

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
Funkcje i moduły są niezbędne do organizacji kodu i poprawy możliwości ponownego wykorzystania w skryptach PowerShell. Funkcje umożliwiają grupowanie kodu w bloki wielokrotnego użytku, natomiast moduły pozwalają na pakowanie i dzielenie się kodem z innymi. Używając funkcji i modułów, skrypty PowerShell mogą być bardziej modułowe, wydajne i łatwiejsze w utrzymaniu.

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
Twarde kodowanie wartości w skrypcie PowerShell czyni go mniej elastycznym i trudniejszym do utrzymania. Zamiast twardego kodowania wartości, najlepiej jest używać parametrów lub zmiennych, które umożliwiają użytkownikom przekazywanie wartości do skryptu w czasie wykonywania. Dzięki użyciu parametrów lub zmiennych, skrypt może być bardziej użyteczny i dostosowany do zmieniających się warunków.

Oto przykład użycia parametru w PowerShell:
```powershell
param (
    [string]$name
)

Write-Host "Hello, $name!"
```

#### Użycie wyjścia Verbose
Wyjście weryfikujące dostarcza dodatkowych informacji o postępie skryptu, co może być przydatne podczas debugowania i rozwiązywania problemów. PowerShell udostępnia cmdlet Write-Verbose, który pozwala użytkownikom na wyprowadzenie na konsolę informacji weryfikujących. Używając wyjścia verbose, skrypty PowerShell mogą być bardziej informacyjne i łatwiejsze do debugowania.

Oto przykład użycia wyjścia verbose w PowerShell:
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

### Dziesięć pomysłów na skrypty Powershell dla początkujących

- **Automatyczne kopie zapasowe**: Stwórz skrypt, który zautomatyzuje proces tworzenia kopii zapasowych ważnych plików i katalogów na zewnętrznym dysku twardym lub w usłudze przechowywania danych w chmurze.
- **Zarządzanie plikami**: Utwórz skrypt, który organizuje pliki i katalogi, sortując je do różnych folderów na podstawie typu pliku, rozmiaru lub innych kryteriów.
- **Informacje systemowe**: Utwórz skrypt, który pobiera informacje o systemie, takie jak wykorzystanie procesora i pamięci, miejsce na dysku oraz ustawienia sieciowe, i wyświetla je w łatwym do odczytania formacie.
- **Zarządzanie użytkownikami**: Utwórz skrypt, który automatyzuje proces dodawania, modyfikowania lub usuwania użytkowników i grup w systemie operacyjnym Windows.
- **Instalacja oprogramowania**: Utwórz skrypt, który instaluje i konfiguruje oprogramowanie na wielu komputerach jednocześnie, oszczędzając czas i wysiłek.
- **Konfiguracja sieci**: Utwórz skrypt, który zautomatyzuje proces konfiguracji ustawień sieciowych, takich jak adres IP, maska podsieci i brama domyślna.
- **Bezpieczeństwo**: Stwórz skrypt, który audytuje i monitoruje ustawienia bezpieczeństwa oraz alarmuje użytkownika w przypadku wykrycia jakichkolwiek zmian.
- **Planowanie zadań**: Utwórz skrypt, który planuje i automatyzuje powtarzające się zadania, takie jak kopie zapasowe, aktualizacje i skanowanie systemu.
- **Manipulowanie rejestrami**: Utwórz skrypt, który modyfikuje lub pobiera wartości rejestru dla określonych kluczy lub wartości.
- **Zdalna administracja**: Tworzenie skryptu umożliwiającego zdalną administrację komputerami z systemem Windows, pozwalającego użytkownikom na wykonywanie poleceń i skryptów na zdalnych maszynach.

## Wnioski.

PowerShell to potężne narzędzie do zarządzania i automatyzacji systemu operacyjnego Windows oraz innych technologii firmy Microsoft. W tym artykule omówiliśmy podstawy tworzenia skryptów w PowerShellu dla początkujących, w tym instalację i uruchamianie PowerShella, używanie cmdletów, zmiennych, pętli, wyrażeń warunkowych i funkcji oraz korzystanie z PowerShell ISE, PowerShell Remoting i modułów PowerShella. Stosując najlepsze praktyki, skrypty PowerShell mogą być bezpieczne, niezawodne i łatwe do utrzymania. Dzięki praktyce można stać się biegłym w tworzeniu skryptów PowerShell i z łatwością zautomatyzować różne zadania administracyjne.
