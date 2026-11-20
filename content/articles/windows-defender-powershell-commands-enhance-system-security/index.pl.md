---
title: "Polecenia PowerShell programu Windows Defender dla bezpieczeństwa systemu"
date: 2023-07-27
lastmod: 2026-11-20
toc: true
draft: false
description: "Odkryj moc poleceń Windows Defender PowerShell i dowiedz się, jak zwiększyć bezpieczeństwo systemu za pomocą sterowania z wiersza poleceń."
genre: ["Windows Defender", "Polecenia PowerShell", "bezpieczeństwo systemu", "kontrola wiersza poleceń", "antywirus", "Systemy operacyjne Windows", "ochrona przed złośliwym oprogramowaniem", "zaawansowane ustawienia zabezpieczeń", "automatyzacja operacji bezpieczeństwa", "Windows PowerShell"]
tags: ["Technologia", "Cyberbezpieczeństwo", "Systemy operacyjne", "Windows", "Narzędzia wiersza poleceń", "Bezpieczeństwo systemu", "PowerShell", "Antywirus", "Ochrona przed złośliwym oprogramowaniem", "Skrypty"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.webp"
coverAlt: "Animowana ilustracja przedstawiająca tarczę chroniącą system komputerowy przed różnymi cyberzagrożeniami."
coverCaption: "Zwiększ bezpieczeństwo swojego systemu dzięki poleceniom Windows Defender PowerShell."
---

## Wprowadzenie

Windows Defender, opracowany przez Microsoft, to zintegrowane rozwiązanie antywirusowe i zabezpieczające dla systemów operacyjnych Windows. Oferuje przyjazny dla użytkownika interfejs do efektywnego zarządzania ustawieniami zabezpieczeń. Jednak dla zaawansowanych użytkowników, którzy preferują kontrolę z poziomu wiersza poleceń, Windows Defender zapewnia zestaw potężnych poleceń PowerShell. W tym artykule zagłębimy się w świat **poleceń Windows Defender PowerShell** i zbadamy, w jaki sposób mogą one zwiększyć bezpieczeństwo systemu i zapewnić większą kontrolę nad środowiskiem Windows.

## Potęga poleceń Windows Defender PowerShell

Polecenia Windows Defender PowerShell dają użytkownikom możliwość wykonywania zaawansowanych operacji bezpieczeństwa za pomocą interfejsu wiersza poleceń. Polecenia te zapewniają szeroki zakres funkcji, od prostych operacji, takich jak skanowanie w poszukiwaniu złośliwego oprogramowania, po złożone zadania, takie jak konfigurowanie zaawansowanych ustawień zabezpieczeń. Korzystając z PowerShell, użytkownicy mogą automatyzować operacje bezpieczeństwa, tworzyć niestandardowe skrypty i płynnie integrować Windows Defender z istniejącymi przepływami pracy.

## Pierwsze kroki z Windows Defender PowerShell

Aby uzyskać dostęp do poleceń Windows Defender PowerShell, należy otworzyć sesję PowerShell z uprawnieniami administratora. Oto jak możesz zacząć:

1. Naciśnij przycisk `Win + X` i wybierz **Windows PowerShell (Admin)** (jako administrator) z menu.
2. Jeśli pojawi się monit, kliknij **Yes** (Tak), aby zezwolić aplikacji na wprowadzanie zmian na urządzeniu.

Po otwarciu sesji PowerShell można rozpocząć korzystanie z poleceń Windows Defender PowerShell.

## Typowe polecenia Windows Defender PowerShell

### 1. **Get-MpComputerStatus**: Sprawdza status Windows Defender

Polecenie `Get-MpComputerStatus` przedstawia bieżący stan programu Windows Defender, w tym wersję silnika antywirusowego, czas ostatniego skanowania i stan ochrony w czasie rzeczywistym. Pozwala szybko ocenić działanie programu i sprawdzić, czy działa prawidłowo.

Aby sprawdzić stan Windows Defender, otwórz sesję PowerShell z uprawnieniami administratora i wykonaj następujące polecenie:

```powershell
Get-MpComputerStatus
```

To polecenie wyświetli takie informacje, jak

- **AntivirusEngineVersion**: Numer wersji silnika antywirusowego używanego przez Windows Defender.
- **LastFullScanTime**: Data i godzina ostatniego pełnego skanowania wykonanego przez Windows Defender.
- **LastQuickScanTime**: Data i godzina ostatniego szybkiego skanowania wykonanego przez program Windows Defender.
- **RealTimeProtectionEnabled**: Wskazuje, czy ochrona w czasie rzeczywistym jest włączona czy wyłączona.

Regularne monitorowanie stanu Windows Defender za pomocą `Get-MpComputerStatus` zapewnia, że użytkownik jest na bieżąco informowany o poziomie ochrony systemu przed potencjalnymi zagrożeniami.

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

Polecenie `Update-MpSignature` umożliwia ręczną aktualizację sygnatur antywirusowych używanych przez Windows Defender. Sygnatury zawierają ważne informacje o znanym złośliwym oprogramowaniu i pomagają wykrywać oraz blokować zagrożenia. Uruchomienie polecenia pobiera najnowsze sygnatury i zwiększa ochronę przed nowymi zagrożeniami.

Aby ręcznie zaktualizować sygnatury Windows Defender, otwórz sesję PowerShell z uprawnieniami administratora i wykonaj następujące polecenie:

```powershell
Update-MpSignature
```
To polecenie uruchamia proces aktualizacji, w którym **Windows Defender** łączy się z serwerami **Microsoft** w celu pobrania najnowszych **sygnatur antywirusowych**. Po zakończeniu aktualizacji Windows Defender będzie posiadał najbardziej aktualne informacje o znanym złośliwym oprogramowaniu, zwiększając jego zdolność do identyfikowania i eliminowania zagrożeń.

Aktualizowanie sygnatur Windows Defender jest niezbędne do utrzymania najwyższego poziomu ochrony przed stale ewoluującym krajobrazem **złośliwego oprogramowania** i **zagrożeń cybernetycznych**. Regularne aktualizowanie sygnatur przy użyciu `Update-MpSignature` zapewniasz, że Windows Defender może skutecznie chronić twój system.

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

Polecenie `Set-MpPreference` pozwala dostosować ustawienia **Windows Defender** do konkretnych wymagań bezpieczeństwa. Obejmuje to **ochronę w czasie rzeczywistym**, **ochronę opartą na chmurze** i **ustawienia systemu inspekcji sieci**.

Ochronę w czasie rzeczywistym można włączyć lub wyłączyć za pomocą `Set-MpPreference`. Funkcja ta aktywnie monitoruje system pod kątem złośliwych działań i szybko reaguje na zagrożenia. Aby ją włączyć, wykonaj następujące polecenie:

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

Dodatkowo można wykorzystać polecenie do dostosowania ustawień ochrony opartej na chmurze. Ochrona oparta na chmurze wykorzystuje zasoby chmury w celu poprawy wykrywania zagrożeń i zapewnienia szybszych reakcji na pojawiające się zagrożenia. Aby włączyć ochronę opartą na chmurze, użyj następującego polecenia:

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

Ponadto `Set-MpPreference` umożliwia dostosowanie ustawień systemu inspekcji sieci. System inspekcji sieci analizuje ruch sieciowy pod kątem podejrzanych działań i potencjalnych zagrożeń. Aby dostosować ustawienia systemu inspekcji sieci, wykonaj następujące polecenie:

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

Dostosowanie tych ustawień za pomocą `Set-MpPreference` pozwala zoptymalizować **Windows Defender** zgodnie z wymaganiami bezpieczeństwa i zapewnić solidną ochronę przed złośliwym oprogramowaniem oraz innymi zagrożeniami.

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

Polecenie `Start-MpScan` uruchamia skanowanie systemu w poszukiwaniu złośliwego oprogramowania, pomagając wykrywać i usuwać szkodliwe pliki. Obsługuje **szybkie skanowanie**, **pełne skanowanie** oraz **skanowanie niestandardowe** określonych ścieżek.

Aby wykonać **szybkie skanowanie** za pomocą `Start-MpScan`, uruchom następujące polecenie PowerShell:

```powershell
Start-MpScan -ScanType QuickScan
```

Szybkie skanowanie koncentruje się na krytycznych obszarach systemu, w których często znajduje się złośliwe oprogramowanie, zapewniając szybką ocenę potencjalnych zagrożeń.

Aby dokładniej sprawdzić wszystkie pliki i katalogi systemu, można uruchomić **pełne skanowanie**. Wykonaj następujące polecenie za pomocą `Start-MpScan`:

```powershell
Start-MpScan -ScanType FullScan
```

Pełne skanowanie zapewnia dokładne wykrycie i usunięcie złośliwego oprogramowania z systemu, ale jego ukończenie może potrwać dłużej niż w przypadku szybkiego skanowania.

Oprócz wstępnie zdefiniowanych typów skanowania polecenie `Start-MpScan` pozwala określić ścieżki lub pliki do skanowania niestandardowego. Na przykład poniższe polecenie skanuje wybrany katalog:

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

To polecenie zainicjuje niestandardowe skanowanie w określonym katalogu, umożliwiając ukierunkowanie na określone obszary systemu w celu wykrycia złośliwego oprogramowania.

Funkcje polecenia `Start-MpScan` pozwalają planować skanowanie, automatyzować zadania związane z bezpieczeństwem oraz regularnie wykrywać i ograniczać złośliwe oprogramowanie w systemie.

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

Polecenie `Get-MpThreatCatalog` dostarcza szczegółowych informacji o znanych zagrożeniach i ich atrybutach. Katalog zawiera dane o poziomie zagrożenia, powiązanych nazwach plików i zalecanych działaniach ograniczających ryzyko.

Aby uzyskać informacje o określonych zagrożeniach przy użyciu `Get-MpThreatCatalog` wykonaj następujące kroki:

1. Otwórz sesję PowerShell z uprawnieniami administracyjnymi.
2. Wykonaj następujące polecenie:

```powershell
   Get-MpThreatCatalog
```
To polecenie wyświetli listę znanych zagrożeń wraz z odpowiadającymi im szczegółami.

Wynik polecenia `Get-MpThreatCatalog` zawiera ważne informacje, takie jak:

- **ThreatID**: Unikalny identyfikator zagrożenia.
- **Severity**: Wskazuje poziom dotkliwości zagrożenia, od Low (niski) do Severe (poważny).
- **Name**: Nazwa lub opis zagrożenia.
- **Path**: Ścieżka do pliku powiązanego z zagrożeniem.
- **RecommendedAction**: Zawiera wskazówki dotyczące zalecanych działań, które należy podjąć w celu złagodzenia zagrożenia.

Wykorzystując informacje uzyskane z `Get-MpThreatCatalog` można uzyskać cenny wgląd w potencjalne zagrożenia i podejmować świadome decyzje dotyczące odpowiednich działań w celu ich złagodzenia. Niezależnie od tego, czy chodzi o izolowanie, usuwanie czy monitorowanie określonego zagrożenia, szczegółowy katalog umożliwia skuteczne reagowanie na incydenty związane z bezpieczeństwem.

Aby dowiedzieć się więcej o używaniu `Get-MpThreatCatalog` i interpretowaniu wyników, zapoznaj się z oficjalną dokumentacją Microsoft.

Regularnie korzystaj z `Get-MpThreatCatalog`, aby śledzić zmiany w krajobrazie zagrożeń i zwiększać bezpieczeństwo systemu.

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

Polecenie `Add-MpPreference` pozwala dodawać wykluczenia do Windows Defender i dostosowywać zachowanie skanowania oraz ochrony w czasie rzeczywistym. Można wskazać pliki, foldery lub procesy, które Windows Defender ma pomijać podczas skanowania lub działania ochrony w czasie rzeczywistym.

Aby dodać wykluczenie przy użyciu `Add-MpPreference` musisz podać ścieżkę lub nazwę pliku, folderu lub procesu, który chcesz wykluczyć. Oto przykład dodawania wykluczenia dla folderu:

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

To polecenie zapewnia, że Windows Defender pomija skanowanie określonego folderu, redukując niepotrzebne alerty i potencjalne przerwy w przepływie pracy.

Wykluczenia przydają się między innymi w przypadku zaufanych aplikacji, środowisk programistycznych lub plików powodujących fałszywe alarmy. Za pomocą `Add-MpPreference` można dostosować Windows Defender do wymagań bezpieczeństwa i zoptymalizować jego działanie.

Chroń system, ograniczaj fałszywe alarmy i unikaj zbędnych przerw w skanowaniu, korzystając z funkcji wykluczeń polecenia `Add-MpPreference`.

## Kontrola poleceń Defender w 2026 r.

Uruchamiaj polecenia Defendera z sesji o podwyższonych uprawnieniach tylko wtedy, gdy zadanie wymaga takich uprawnień. Przed użyciem parametru sprawdź aktualną pomoc modułu dla docelowej wersji systemu Windows. Zapisz bieżącą konfigurację, zmieniaj po jednym ustawieniu, sprawdź wynik i zanotuj polecenie przywracające poprzednią wartość.

Przydatne czynności kontrolne obejmują sprawdzenie stanu ochrony, wieku sygnatur, wykluczeń, preferencji, historii skanowania i ostatnich wykryć. Ogranicz zakres wykluczeń oraz zapisz osobę odpowiedzialną i datę wygaśnięcia. Aktualne polecenia cmdlet i ich działanie opisują [dokumentacja modułu PowerShell Microsoft Defender](https://learn.microsoft.com/en-us/powershell/module/defender/) oraz [dokumentacja programu antywirusowego Microsoft Defender](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-windows).

## Wnioski

Polecenia Windows Defender PowerShell zapewniają **bogaty zestaw narzędzi** do zarządzania i zwiększania bezpieczeństwa systemu Windows. Wykorzystując te polecenia, można *automatyzować operacje bezpieczeństwa*, *konfigurować zaawansowane ustawienia* i płynnie włączać Windows Defender do przepływów pracy. Niezależnie od tego, czy jesteś **administratorem systemu**, czy **użytkownikiem zaawansowanym**, odkrywanie możliwości poleceń Windows Defender PowerShell może znacznie poprawić stan bezpieczeństwa twojego systemu.

Pamiętaj, że z wielką mocą wiąże się wielka odpowiedzialność. Korzystając z poleceń PowerShell, zachowaj ostrożność i upewnij się, że rozumiesz wpływ poleceń przed ich wykonaniem. Łącząc swoją wiedzę z mocą poleceń Windows Defender PowerShell, możesz podjąć proaktywne działania w celu ochrony systemu przed ewoluującymi zagrożeniami.

## Referencje

1. Microsoft Docs - [Polecenia cmdlet programu Windows Defender w Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. Microsoft Docs - [Wprowadzenie do Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
