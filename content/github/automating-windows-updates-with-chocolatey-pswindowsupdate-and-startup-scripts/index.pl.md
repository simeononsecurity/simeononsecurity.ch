---
title: "Usprawnienie aktualizacji systemu Windows dzięki automatyzacji przy użyciu Chocolatey, PSWindowsUpdate i skryptów startowych"
date: 2020-07-22
---
 Aktualizacje systemu Windows za pomocą Chocolatey, PSWindowsUpdate i skryptów startowych**

W dzisiejszym szybko zmieniającym się środowisku biznesowym czas ma kluczowe znaczenie dla administratorów systemów. Aktualizacja komputerów z systemem Windows, będąca krytycznym aspektem administrowania systemami, może być niezwykle czasochłonnym zadaniem, które może zająć nawet tydzień, biorąc pod uwagę wystarczającą liczbę systemów. Jednak z pomocą Chocolatey, PSWindowsUpdates i Startup Scripts, możliwe jest teraz wdrażanie aktualizacji przy zaledwie jednym ponownym uruchomieniu każdej maszyny, co znacznie skraca czas wymagany do wykonania aktualizacji.

## Usprawnienie aktualizacji systemu Windows dzięki automatyzacji

Aktualizacje systemu Windows mają kluczowe znaczenie dla utrzymania stabilności i bezpieczeństwa maszyn z systemem Windows. Wykonywanie aktualizacji na dużej liczbie maszyn może być czasochłonnym zadaniem, szczególnie dla administratorów systemu z ograniczonymi zasobami. Jednak przy użyciu narzędzi do automatyzacji, takich jak Chocolatey, PSWindowsUpdate i skrypty startowe, proces ten można usprawnić, aby umożliwić administratorom przeprowadzanie aktualizacji przy minimalnym wysiłku.

### Chocolatey

[Chocolatey](https://chocolatey.org/) to menedżer pakietów dla systemu Windows, który może być używany do automatyzacji instalacji oprogramowania na komputerach z systemem Windows. Jest podobny do apt-get na Ubuntu lub homebrew na macOS i może być używany do instalowania i zarządzania szeroką gamą pakietów oprogramowania. Chocolatey może być używany do cichej instalacji pakietów, co oznacza, że mogą one być instalowane bez interwencji użytkownika.

### PSWindowsUpdate

[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) to moduł PowerShell, który może być używany do automatyzacji instalacji aktualizacji systemu Windows. Udostępnia on polecenia cmdlet, które mogą być używane do instalowania, odinstalowywania i wyświetlania aktualizacji systemu Windows. PSWindowsUpdate to potężne narzędzie, które może być używane do zarządzania aktualizacjami systemu Windows na wielu komputerach, dzięki czemu jest idealne dla administratorów systemu, którzy muszą zarządzać dużą liczbą maszyn.

### Skrypty startowe

[Startup Scripts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn789190(v=ws.11)) to skrypty, które mogą być używane do automatyzacji zadań, które muszą być wykonywane podczas uruchamiania lub zamykania komputera. Skrypty te mogą być używane do wykonywania zadań, takich jak instalowanie oprogramowania, konfigurowanie ustawień i zarządzanie aktualizacjami systemu Windows.

## Automatyzacja aktualizacji systemu Windows za pomocą pojedynczego restartu

Aby zautomatyzować aktualizacje systemu Windows za pomocą Chocolatey, PSWindowsUpdate i skryptów startowych, administratorzy mogą postępować zgodnie z poniższym przewodnikiem krok po kroku.

### Konfiguracja skryptu zamykania systemu
Pobierz wszystkie pliki pomocnicze ze strony [GitHub Repository](https://github.com/simeononsecurity/ChocoAutomateWindowsUpdates)

1. Otwórz Edytor lokalnych zasad grupy, naciskając **"Win + R "** i wpisując **"gpedit.msc "**, a następnie **"Ctrl + Shift + Enter "**.
2. Przejdź do Komputer **Konfiguracja\Ustawienia Windows\Skrypty (uruchamianie/wyłączanie)**.
3. W okienku wyników kliknij dwukrotnie Shutdown.
4. Wybierz kartę PowerShell.
5. W oknie dialogowym Shutdown Properties kliknij przycisk Add.
6. W polu Script Name wpisz ścieżkę do skryptu lub kliknij Browse, aby wyszukać "*chocoautomatewindowsupdates.ps1*" w folderze współdzielonym Netlogon na kontrolerze domeny.
7. Uruchom ponownie komputer.

Teraz wszystko, co administrator musi zrobić, to ponownie uruchomić komputer, aby wykonać aktualizacje systemu Windows.

### Zrozumienie skryptu

Skrypt używany do automatyzacji aktualizacji systemu Windows nosi tytuł "*chocoautomatewindowsupdates.ps1*". Wykonuje on następujące zadania:

1. Instaluje menedżera pakietów Chocolatey.
2. Włącza kilka preferowanych zmian w konfiguracji Chocolatey.
3. Aktualizuje wszystkie zainstalowane pakiety Chocolatey.
4. Instaluje moduł PSWindowsUpdate PowerShell.
5. Dodaje menedżera usługi Windows Update.
6. Instaluje wszystkie dostępne aktualizacje systemu Windows.
7. Instaluje wszelkie brakujące sterowniki lub aktualizacje wymagane przez wcześniej zainstalowane aktualizacje.

### Korzyści z automatyzacji aktualizacji systemu Windows

Automatyzacja aktualizacji systemu Windows za pomocą Chocolatey, PSWindowsUpdate i skryptów startowych ma kilka zalet dla administratorów systemu. Korzyści te obejmują:

- **Oszczędność czasu**: Automatyzacja aktualizacji systemu Windows znacznie skraca czas potrzebny na wykonanie aktualizacji. Administratorzy nie muszą już ręcznie instalować aktualizacji na każdym komputerze.
- Spójność**: Automatyzacja aktualizacji systemu Windows zapewnia, że aktualizacje są instalowane spójnie na wszystkich komputerach. Zmniejsza to prawdopodobieństwo wystąpienia błędów i luk w zabezpieczeniach.
- **Centralne zarządzanie**: Automatyzacja aktualizacji systemu Windows pozwala administratorom zarządzać aktualizacjami z centralnej lokalizacji, ułatwiając śledzenie, które aktualizacje zostały zainstalowane i które maszyny wymagają aktualizacji.
- **Zwiększone bezpieczeństwo**: Automatyzacja aktualizacji systemu Windows zapewnia, że komputery są na bieżąco z najnowszymi poprawkami bezpieczeństwa, zmniejszając ryzyko naruszenia bezpieczeństwa.

### Podsumowanie

Automatyzacja aktualizacji systemu Windows za pomocą Chocolatey, PSWindowsUpdate i skryptów startowych to potężne narzędzie, które może zaoszczędzić administratorom systemu wiele czasu i wysiłku. Umożliwia ono instalowanie aktualizacji w sposób spójny i wydajny, zapewniając, że komputery są na bieżąco z najnowszymi poprawkami zabezpieczeń. Postępując zgodnie z krokami opisanymi w tym samouczku, administratorzy mogą zautomatyzować aktualizacje systemu Windows za pomocą pojedynczego restartu, dzięki czemu proces aktualizacji komputerów z systemem Windows jest znacznie szybszy i łatwiejszy.
