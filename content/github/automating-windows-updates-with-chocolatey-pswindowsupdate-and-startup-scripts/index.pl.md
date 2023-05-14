---
title: "Usprawnij aktualizacje systemu Windows dzięki automatyzacji przy użyciu Chocolatey, PSWindowsUpdate i skryptów startowych."
date: 2020-07-22
---
 Aktualizacje systemu Windows za pomocą Chocolatey, PSWindowsUpdate i skryptów startowych**.

W dzisiejszym szybko zmieniającym się środowisku biznesowym, czas ma kluczowe znaczenie dla administratorów systemów. Aktualizowanie maszyn Windows, krytyczny aspekt administracji systemami, może być niezwykle czasochłonnym zadaniem, które może zająć nawet tydzień, biorąc pod uwagę wystarczającą liczbę systemów. Jednak z pomocą Chocolatey, PSWindowsUpdates i Startup Scripts można teraz przeprowadzać aktualizacje po zaledwie jednym restarcie każdej maszyny, co znacznie skraca czas potrzebny na przeprowadzenie aktualizacji.

## Usprawnienie aktualizacji systemu Windows dzięki automatyzacji

Aktualizacje systemu Windows są krytyczne dla utrzymania stabilności i bezpieczeństwa maszyn Windows. Przeprowadzanie aktualizacji na dużej liczbie maszyn może być czasochłonnym zadaniem, zwłaszcza dla administratorów systemów z ograniczonymi zasobami. Jednak przy użyciu narzędzi automatyzacji, takich jak Chocolatey, PSWindowsUpdate i Startup Scripts, proces ten można usprawnić, aby umożliwić administratorom wykonywanie aktualizacji przy minimalnym wysiłku.

### Chocolatey

[Chocolatey](https://chocolatey.org/) to menedżer pakietów dla systemu Windows, który może być używany do automatyzacji instalacji oprogramowania na maszynach z systemem Windows. Jest podobny do apt-get na Ubuntu lub homebrew na macOS, i może być używany do instalowania i zarządzania szeroką gamą pakietów oprogramowania. Chocolatey może być używany do instalowania pakietów po cichu, co oznacza, że mogą one zostać zainstalowane bez interwencji użytkownika.

### PSWindowsUpdate

[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) to moduł PowerShell, który może być użyty do zautomatyzowania instalacji aktualizacji systemu Windows. Dostarcza on cmdletów, które mogą być używane do instalowania, odinstalowywania i listowania aktualizacji systemu Windows. PSWindowsUpdate jest potężnym narzędziem, które może być używane do zarządzania aktualizacjami systemu Windows na wielu maszynach, co czyni go idealnym dla administratorów systemu, którzy muszą zarządzać dużą liczbą maszyn.

### Skrypty startowe

[Startup Scripts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn789190(v=ws.11)) to skrypty, które można wykorzystać do zautomatyzowania zadań, które muszą być wykonane podczas uruchamiania lub wyłączania maszyny. Skrypty te mogą być używane do wykonywania takich zadań, jak instalowanie oprogramowania, konfigurowanie ustawień i zarządzanie aktualizacjami systemu Windows.

## Automatyzacja aktualizacji systemu Windows za pomocą pojedynczego restartu

Aby zautomatyzować aktualizacje systemu Windows przy użyciu skryptów Chocolatey, PSWindowsUpdate i Startup Scripts, administratorzy mogą postępować zgodnie z poniższym przewodnikiem krok po kroku.

### Konfigurowanie skryptu zamykania
Pobierz wszystkie pliki pomocnicze z witryny[GitHub Repository](https://github.com/simeononsecurity/ChocoAutomateWindowsUpdates)

1. Otwórz Lokalny Edytor Zasad Grupy, naciskając **"Win + R "** i wpisując **"gpedit.msc "**, a następnie **"Ctrl + Shift + Enter "**.
2. Przejdź do Komputer **Konfiguracja **Ustawienia systemu Windows **Skrypty (uruchamianie/wyłączanie)**.
3. W okienku wyników kliknij dwukrotnie przycisk Shutdown.
4. Wybierz kartę PowerShell.
5. W oknie dialogowym Właściwości zamykania kliknij przycisk Dodaj.
6. W polu Nazwa skryptu wpisz ścieżkę do skryptu lub kliknij Przeglądaj, aby wyszukać "*chocoautomatewindowsupdates.ps1*" w folderze współdzielonym Netlogon na kontrolerze domeny.
7. Uruchom ponownie komputer.

Teraz wszystko, co administrator musi zrobić, to ponownie uruchomić komputer, aby wykonać aktualizacje systemu Windows.

### Zrozumienie skryptu

Skrypt używany do automatyzacji aktualizacji systemu Windows nosi tytuł "*chocoautomatewindowsupdates.ps1*". Wykonuje on następujące zadania:

1. Instaluje menedżera pakietów Chocolatey.
2. Włącza kilka preferowanych zmian w konfiguracji Chocolatey.
3. Uaktualnia wszystkie zainstalowane pakiety Chocolatey.
4. Instaluje moduł PSWindowsUpdate PowerShell.
5. Dodaje menedżera usługi Windows Update.
6. Instaluje wszystkie dostępne aktualizacje systemu Windows.
7. Instaluje wszelkie brakujące sterowniki lub aktualizacje wymagane przez wcześniej zainstalowane aktualizacje.

### Korzyści z automatyzacji aktualizacji systemu Windows

Automatyzacja aktualizacji systemu Windows przy użyciu Chocolatey, PSWindowsUpdate i Startup Scripts ma kilka korzyści dla administratorów systemu. Korzyści te obejmują:

- **Oszczędność czasu**: Automatyzacja aktualizacji systemu Windows znacznie zmniejsza ilość czasu potrzebną do przeprowadzenia aktualizacji. Administratorzy nie muszą już ręcznie instalować aktualizacji na każdej maszynie.
- **Konsekwencja**: Automatyzacja aktualizacji systemu Windows zapewnia, że aktualizacje są instalowane w sposób spójny na wszystkich maszynach. Zmniejsza to prawdopodobieństwo wystąpienia błędów i luk bezpieczeństwa.
- **Zarządzanie scentralizowane**: Automatyzacja aktualizacji systemu Windows pozwala administratorom zarządzać aktualizacjami z centralnej lokalizacji, ułatwiając śledzenie, które aktualizacje zostały zainstalowane i które maszyny wymagają aktualizacji.
- **Większe bezpieczeństwo**: Automatyzacja aktualizacji systemu Windows zapewnia, że maszyny są na bieżąco aktualizowane o najnowsze poprawki bezpieczeństwa, co zmniejsza ryzyko naruszenia bezpieczeństwa.

### Wnioski.

Automatyzacja aktualizacji systemu Windows za pomocą Chocolatey, PSWindowsUpdate i Startup Scripts to potężne narzędzie, które może zaoszczędzić administratorom systemu wiele czasu i wysiłku. Pozwala ono na konsekwentne i skuteczne instalowanie aktualizacji, zapewniając, że maszyny są na bieżąco z najnowszymi łatami bezpieczeństwa. Wykonując kroki opisane w tym poradniku, administratorzy mogą zautomatyzować aktualizacje systemu Windows za pomocą jednego restartu, dzięki czemu proces aktualizacji maszyn Windows jest znacznie szybszy i łatwiejszy.
