---
title: "Mastering Active Directory Administration with PowerShell: Przewodnik instalacji i użytkowania"
date: 2023-07-25
toc: true
draft: false
description: "Dowiedz się, jak skutecznie zainstalować i wykorzystać moduł Active Directory dla PowerShell, aby usprawnić zadania administracyjne Windows Active Directory."
genre: ["Technologia", "Windows", "PowerShell", "Active Directory", "Administracja", "Skrypty", "IT", "Automatyzacja", "Windows Server", "Microsoft"]
tags: ["moduł Active Directory dla PowerShell", "import modułu active directory w PowerShell", "moduł Active Directory dla Windows PowerShell", "active directory PowerShell install", "instalacja usługi Active Directory PowerShell", "PowerShell instaluje moduł katalogu aktywnego Windows 10", "instalacja modułu PowerShell Active Directory Windows 10", "pobierz moduł PowerShell Active Directory", "Administracja AD", "Usługa Windows Active Directory", "Polecenia cmdlet PowerShell", "pobieranie informacji AD", "tworzenie obiektów AD", "modyfikować obiekty AD", "zarządzanie zabezpieczeniami AD", "Zarządzanie użytkownikami AD", "Zarządzanie grupą AD", "Zarządzanie AD OR", "Skrypty PowerShell", "Administracja Windows Server", "Microsoft PowerShell", "automatyzacja zadań AD", "Instalacja modułu PowerShell", "Przewodnik administracyjny AD", "Zarządzanie usługą Active Directory", "Zarządzanie bezpieczeństwem AD", "Automatyzacja PowerShell", "Polecenia PowerShell usługi Active Directory", "Odniesienie do polecenia cmdlet PowerShell"]
cover: "/img/cover/An_image_depicting_a_network_of_interconnected.png"
coverAlt: "Obraz przedstawiający sieć połączonych serwerów i ikon użytkowników, symbolizujący zarządzanie i automatyzację Active Directory."
coverCaption: "Odblokuj moc administracji Active Directory za pomocą PowerShell."
---

## Wprowadzenie

W dzisiejszym cyfrowym krajobrazie zarządzanie i utrzymywanie kont użytkowników, grup zabezpieczeń i innych zasobów w środowisku Windows Active Directory (AD) wymaga wydajnych i usprawnionych procesów. PowerShell, potężny język skryptowy opracowany przez Microsoft, oferuje moduł **Active Directory** ułatwiający zadania administracyjne AD. Moduł ten zapewnia szeroki zakres poleceń cmdlet, które umożliwiają administratorom automatyzację różnych operacji i efektywne zarządzanie usługą AD. W tym artykule omówimy instalację i korzystanie z modułu Active Directory dla PowerShell.

## Instalacja modułu Active Directory dla PowerShell

Aby rozpocząć korzystanie z modułu Active Directory dla PowerShell, należy upewnić się, że jest on zainstalowany w systemie. Proces instalacji może się różnić w zależności od systemu operacyjnego. Oto kroki instalacji modułu w systemach **Windows 10**, **Windows 11** i **Windows Server**:

### Windows 10 i Windows 11 - PowerShell
1. Otwórz **Windows PowerShell** z uprawnieniami administratora.
2. Uruchom następujące polecenie, aby zainstalować moduł:

```powershell
Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0 -Online
```

1. Poczekaj na zakończenie instalacji. Po zakończeniu można rozpocząć korzystanie z modułu Active Directory.

### Windows Server
1. Otwórz **Windows PowerShell** z uprawnieniami administratora.
2. Uruchom następujące polecenie, aby zainstalować moduł:

```powershell
Install-WindowsFeature -Name "RSAT-AD-PowerShell" -IncludeAllSubFeature
```

3. Poczekaj na zakończenie instalacji. Po zakończeniu można rozpocząć korzystanie z modułu Active Directory.

### Systemy offline

Systemy offline są nieco bardziej skomplikowane. Istnieje kilka metod, jednak zalecamy użycie następującego skryptu:
- [Offine-PS-ActiveDirectory-Install](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install)

## Importowanie modułu Active Directory w PowerShell

Przed użyciem modułu Active Directory w PowerShell należy zaimportować go do bieżącej sesji. Wykonaj poniższe kroki, aby zaimportować moduł:

1. Uruchom **Windows PowerShell** z uprawnieniami administracyjnymi.
2. Wykonaj następujące polecenie, aby zaimportować moduł:

```powershell
Import-Module ActiveDirectory
```

3. Moduł Active Directory zostanie zaimportowany i będzie można uzyskać dostęp do jego poleceń cmdlet i funkcji.

## Korzystanie z modułu Active Directory dla PowerShell

Po zaimportowaniu modułu Active Directory można wykorzystać jego bogaty zestaw poleceń cmdlet do wykonywania różnych zadań administracyjnych. Przyjrzyjmy się kilku często używanym poleceniom cmdlet i ich funkcjom:

### Pobieranie informacji Active Directory

Aby efektywnie zarządzać środowiskiem Active Directory (AD), kluczowe jest pobieranie informacji o różnych obiektach AD, takich jak użytkownicy, grupy i jednostki organizacyjne (OU). PowerShell zapewnia potężne polecenia cmdlet, które upraszczają proces pobierania.

- [**Get-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps) To polecenie cmdlet umożliwia pobieranie szczegółowych informacji o użytkownikach AD. Można uzyskać atrybuty, takie jak nazwa użytkownika, nazwa wyświetlana, adres e-mail i inne. Na przykład, aby pobrać wszystkich użytkowników, których nazwa użytkownika zaczyna się od "johndoe", można uruchomić następujące polecenie:

  ```powershell
  Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
  ```

  To polecenie zwróci listę obiektów użytkownika pasujących do określonego filtra.

- [**Get-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps) Polecenie cmdlet Get-ADGroup umożliwia pobieranie informacji o grupach AD. Zapewnia dostęp do szczegółów, takich jak nazwa grupy, członkowie, opis i inne. Na przykład, aby pobrać wszystkie grupy zabezpieczeń w środowisku AD, można wykonać następujące polecenie:

  ```powershell
  Get-ADGroup -Filter 'GroupCategory -eq "Security"'
  ```

  Spowoduje to wyświetlenie listy grup zabezpieczeń w usłudze Active Directory.

- [**Get-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit?view=windowsserver2022-ps) Polecenie cmdlet Get-ADOrganizationalUnit służy do pobierania informacji o jednostkach organizacyjnych AD. Umożliwia dostęp do właściwości, takich jak nazwa jednostki organizacyjnej, opis, nadrzędna jednostka organizacyjna i inne. Aby pobrać wszystkie jednostki organizacyjne w domenie, można użyć następującego polecenia:

  ```powershell
  Get-ADOrganizationalUnit -Filter *
  ```

  Uruchomienie tego polecenia spowoduje wyświetlenie listy wszystkich jednostek OU w usłudze Active Directory.

Korzystając z tych zaawansowanych poleceń cmdlet, można łatwo pobrać określone informacje o użytkownikach, grupach i jednostkach OU usługi AD, umożliwiając wydajną administrację i zarządzanie środowiskiem Active Directory.

{{< inarticle-dark >}}


Te polecenia cmdlet umożliwiają pobieranie określonych atrybutów, filtrowanie wyników i wykonywanie zaawansowanych zapytań w celu pobrania żądanych informacji.

### Tworzenie i zarządzanie obiektami Active Directory

Podczas pracy z Active Directory (AD), moduł Active Directory w PowerShell oferuje potężne polecenia cmdlet do tworzenia i zarządzania obiektami AD. Zapoznajmy się z kilkoma niezbędnymi poleceniami cmdlet do tworzenia użytkowników, grup i jednostek organizacyjnych (OU) w usłudze AD.

- [**New-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps) To polecenie cmdlet umożliwia utworzenie nowego użytkownika AD. Można określić atrybuty, takie jak nazwa użytkownika, hasło, adres e-mail i inne. Na przykład, aby utworzyć nowego użytkownika z nazwą użytkownika "john.doe" i wyświetlaną nazwą "John Doe", można użyć następującego polecenia:

  ```powershell
  New-ADUser -SamAccountName "john.doe" -Name "John Doe"
  ```

  To polecenie utworzy nowego użytkownika w usłudze Active Directory.

- [**New-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adgroup?view=windowsserver2022-ps) Polecenie cmdlet New-ADGroup umożliwia utworzenie nowej grupy AD. Można ustawić właściwości, takie jak nazwa grupy, opis, zakres grupy i inne. Aby utworzyć nową grupę o nazwie "Marketing" z opisem, można wykonać następujące polecenie:

  ```powershell
  New-ADGroup -Name "Marketing" -Description "Marketing Team"
  ```

  To polecenie utworzy nową grupę w usłudze Active Directory.

- [**New-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adorganizationalunit?view=windowsserver2022-ps) Za pomocą polecenia cmdlet New-ADOrganizationalUnit można utworzyć nową jednostkę organizacyjną AD. Można określić właściwości, takie jak nazwa jednostki organizacyjnej, nadrzędna jednostka organizacyjna i inne. Na przykład, aby utworzyć nową jednostkę organizacyjną o nazwie "Sprzedaż" w ramach jednostki organizacyjnej "Działy", można uruchomić następujące polecenie:

  ```powershell
  New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"
  ```

  To polecenie utworzy nową jednostkę organizacyjną w hierarchii usługi Active Directory.

Korzystając z tych poleceń cmdlet, można łatwo tworzyć nowych użytkowników, grupy i jednostki organizacyjne AD z żądanymi właściwościami i konfiguracjami, umożliwiając wydajne zarządzanie środowiskiem Active Directory.

{{< inarticle-dark >}}


### Modyfikowanie obiektów usługi Active Directory

Jeśli chodzi o modyfikowanie właściwości i atrybutów istniejących obiektów Active Directory (AD), moduł Active Directory w PowerShell udostępnia kilka przydatnych poleceń cmdlet. Przyjrzyjmy się tym poleceniom cmdlet do modyfikowania użytkowników, grup i jednostek organizacyjnych (OU) AD.

- [**Set-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-aduser?view=windowsserver2022-ps) Polecenie cmdlet Set-ADUser umożliwia modyfikowanie właściwości użytkownika AD. Można aktualizować atrybuty, takie jak wyświetlana nazwa, adres e-mail, numer telefonu i inne. Na przykład, aby zmienić numer telefonu użytkownika o nazwie "john.doe", można użyć następującego polecenia:

  ```powershell
  Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
  ```

  To polecenie zmodyfikuje numer telefonu określonego użytkownika w usłudze Active Directory.

- [**Set-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adgroup?view=windowsserver2022-ps) Za pomocą polecenia cmdlet Set-ADGroup można modyfikować właściwości grupy AD. Można aktualizować atrybuty, takie jak opis grupy, członkostwo, zakres grupy i inne. Aby zmienić opis grupy o nazwie "Marketing" na "Marketing Team", można wykonać następujące polecenie:

  ```powershell
  Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
  ```

  To polecenie zaktualizuje opis określonej grupy w usłudze Active Directory.

- [**Set-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adorganizationalunit?view=windowsserver2022-ps) Polecenie cmdlet Set-ADOrganizationalUnit umożliwia modyfikowanie właściwości jednostki organizacyjnej AD. Można zmieniać atrybuty, takie jak nazwa jednostki organizacyjnej, opis i inne. Na przykład, aby zmodyfikować opis jednostki organizacyjnej o nazwie "Sprzedaż" na "Dział sprzedaży", można uruchomić następujące polecenie:

  ```powershell
  Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"
  ```

  To polecenie zaktualizuje opis określonej jednostki organizacyjnej w hierarchii usługi Active Directory.

Korzystając z tych poleceń cmdlet, można łatwo modyfikować właściwości i atrybuty obiektów AD, dokonując niezbędnych aktualizacji i dostosowań w celu spełnienia wymagań organizacji.

{{< inarticle-dark >}}


### Zarządzanie bezpieczeństwem Active Directory

Oprócz zarządzania i administrowania obiektami Active Directory (AD), moduł Active Directory w PowerShell udostępnia polecenia cmdlet zaprojektowane specjalnie do obsługi aspektów związanych z bezpieczeństwem AD. Te polecenia cmdlet umożliwiają administratorom efektywne zarządzanie dostępem użytkowników, członkostwem w grupach i zadaniami związanymi z hasłami w środowisku AD.

Oto kilka często używanych poleceń cmdlet związanych z bezpieczeństwem:

- [**Add-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2022-ps) To polecenie cmdlet umożliwia dodawanie członków do grupy AD. Określając grupę AD i konta użytkowników lub grupy, które chcesz dodać, możesz łatwo zarządzać kontrolą dostępu. Na przykład, aby dodać użytkownika o nazwie "JohnDoe" do grupy "Managers", można użyć następującego polecenia:

  ```powershell
  Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
  ```

- [**Remove-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/remove-adgroupmember?view=windowsserver2022-ps) Za pomocą tego polecenia cmdlet można usuwać członków z grupy AD. Określając grupę AD i konta użytkowników lub grupy, które chcesz usunąć, możesz efektywnie zarządzać członkostwem w grupach. Na przykład, aby usunąć użytkownika o nazwie "JaneSmith" z grupy "Developers", można użyć następującego polecenia:

  ```powershell
  Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
  ```

- [**Set-ADUserPassword**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adaccountpassword?view=windowsserver2022-ps) To polecenie cmdlet umożliwia ustawienie hasła dla użytkownika AD. Określając konto użytkownika i podając nowe hasło, można wymusić zasady dotyczące haseł i zapewnić bezpieczne uwierzytelnianie użytkowników. Oto przykład ustawienia nowego hasła dla użytkownika o nazwie "AmyJohnson":

  ```powershell
  Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
  ```

Korzystając z tych poleceń cmdlet związanych z bezpieczeństwem, administratorzy mogą skutecznie zarządzać dostępem użytkowników, członkostwem w grupach i zasadami haseł w środowisku Active Directory.

## Przykładowy skrypt modułu Active Directory dla PowerShell
```powershell
# Import Active Directory module
Import-Module ActiveDirectory

# Retrieve Active Directory information
Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
Get-ADGroup -Filter 'GroupCategory -eq "Security"'
Get-ADOrganizationalUnit -Filter *

# Create a new Active Directory user
New-ADUser -SamAccountName "john.doe" -Name "John Doe"

# Create a new Active Directory group
New-ADGroup -Name "Marketing" -Description "Marketing Team"

# Create a new Active Directory organizational unit
New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"

# Modify Active Directory objects
Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"

# Manage Active Directory security
Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
```

## Wnioski

Podsumowując, moduł **Active Directory dla PowerShell** jest potężnym narzędziem, które umożliwia wydajne i wygodne zarządzanie usługą Windows Active Directory. Po zainstalowaniu i zaimportowaniu modułu uzyskuje się dostęp do kompleksowego zestawu **polecenia cmdlet**, które upraszczają różne zadania związane z AD.

Za pomocą modułu Active Directory można wykonywać szeroki zakres operacji, takich jak pobieranie informacji o obiektach AD, tworzenie nowych obiektów, modyfikowanie właściwości i zarządzanie zabezpieczeniami. Moduł ten umożliwia administratorom automatyzację zadań administracyjnych, usprawnienie przepływu pracy i zapewnienie sprawnego funkcjonowania środowisk Active Directory.

Wykorzystując **PowerShell** i **moduł Active Directory**, można zwiększyć swoje możliwości administracyjne AD i poprawić wydajność procesów zarządzania AD. Niezależnie od tego, czy jesteś administratorem systemu, specjalistą IT, czy menedżerem Active Directory, moduł Active Directory wyposaża Cię w niezbędne narzędzia do efektywnego zarządzania infrastrukturą AD.

Wykorzystaj moc **PowerShell** i **modułu Active Directory**, aby usprawnić zadania administracyjne AD, zwiększyć produktywność oraz utrzymać bezpieczne i dobrze zorganizowane środowisko Active Directory.

{{< inarticle-dark >}}

## Referencje

- [Install-WindowsFeature cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature)
- [Import-Module cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module)
- [Active Directory cmdlets in PowerShell - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/activedirectory)
