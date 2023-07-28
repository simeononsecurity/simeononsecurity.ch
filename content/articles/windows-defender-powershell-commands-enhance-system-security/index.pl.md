---
title: "Zwiększ bezpieczeństwo swojego systemu dzięki poleceniom Windows Defender PowerShell"
date: 2023-07-27
toc: true
draft: false
description: "Odkryj moc poleceń Windows Defender PowerShell i dowiedz się, jak zwiększyć bezpieczeństwo systemu za pomocą sterowania z wiersza poleceń."
genre: ["Windows Defender", "Polecenia PowerShell", "bezpieczeństwo systemu", "kontrola wiersza poleceń", "antywirus", "Systemy operacyjne Windows", "ochrona przed złośliwym oprogramowaniem", "zaawansowane ustawienia zabezpieczeń", "automatyzacja operacji bezpieczeństwa", "Windows PowerShell"]
tags: ["Technologia", "Cyberbezpieczeństwo", "Systemy operacyjne", "Windows", "Narzędzia wiersza poleceń", "Bezpieczeństwo systemu", "PowerShell", "Antywirus", "Ochrona przed złośliwym oprogramowaniem", "Skrypty"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.png"
coverAlt: "Animowana ilustracja przedstawiająca tarczę chroniącą system komputerowy przed różnymi cyberzagrożeniami."
coverCaption: "Zwiększ bezpieczeństwo swojego systemu dzięki poleceniom Windows Defender PowerShell."
---

## Wprowadzenie

Windows Defender, opracowany przez Microsoft, to zintegrowane rozwiązanie antywirusowe i zabezpieczające dla systemów operacyjnych Windows. Oferuje przyjazny dla użytkownika interfejs do efektywnego zarządzania ustawieniami zabezpieczeń. Jednak dla zaawansowanych użytkowników, którzy preferują kontrolę z poziomu wiersza poleceń, Windows Defender zapewnia zestaw potężnych poleceń PowerShell. W tym artykule zagłębimy się w świat **poleceń Windows Defender PowerShell** i zbadamy, w jaki sposób mogą one zwiększyć bezpieczeństwo systemu i zapewnić większą kontrolę nad środowiskiem Windows.

## Potęga poleceń Windows Defender PowerShell

Polecenia Windows Defender PowerShell dają użytkownikom możliwość wykonywania zaawansowanych operacji bezpieczeństwa za pomocą interfejsu wiersza poleceń. Polecenia te zapewniają szeroki zakres funkcji, od prostych operacji, takich jak skanowanie w poszukiwaniu złośliwego oprogramowania, po złożone zadania, takie jak konfigurowanie zaawansowanych ustawień zabezpieczeń. Korzystając z PowerShell, użytkownicy mogą automatyzować operacje bezpieczeństwa, tworzyć niestandardowe skrypty i płynnie integrować Windows Defender z istniejącymi przepływami pracy.

## Pierwsze kroki z Windows Defender PowerShell

Aby uzyskać dostęp do poleceń Windows Defender PowerShell, należy otworzyć sesję PowerShell z uprawnieniami administratora. Oto jak możesz zacząć:

1. Naciśnij przycisk `Win + X` i wybierz **Windows PowerShell (Admin)** z menu.
2. Jeśli pojawi się monit, kliknij **Tak**, aby zezwolić aplikacji na wprowadzanie zmian na urządzeniu.

Po otwarciu sesji PowerShell można rozpocząć korzystanie z poleceń Windows Defender PowerShell.

## Typowe polecenia Windows Defender PowerShell

### 1. **Get-MpComputerStatus**: Sprawdza status Windows Defender

The `Get-MpComputerStatus` zapewnia przegląd bieżącego stanu programu Windows Defender w systemie, w tym wersję silnika antywirusowego, czas ostatniego skanowania i stan ochrony w czasie rzeczywistym. Uruchamiając to polecenie, można szybko ocenić ogólną kondycję programu Windows Defender i upewnić się, że działa on optymalnie.

Aby sprawdzić stan Windows Defender, otwórz sesję PowerShell z uprawnieniami administratora i wykonaj następujące polecenie:

```powershell
Get-MpComputerStatus
```

To polecenie wyświetli takie informacje, jak

- **AntivirusEngineVersion**: Numer wersji silnika antywirusowego używanego przez Windows Defender.
- **LastFullScanTime**: Data i godzina ostatniego pełnego skanowania wykonanego przez Windows Defender.
- **LastQuickScanTime**: Data i godzina ostatniego szybkiego skanowania wykonanego przez program Windows Defender.
- RealTimeProtectionEnabled**: Wskazuje, czy ochrona w czasie rzeczywistym jest włączona czy wyłączona.

Regularne monitorowanie stanu Windows Defender za pomocą `Get-MpComputerStatus` zapewnia, że użytkownik jest na bieżąco informowany o poziomie ochrony systemu przed potencjalnymi zagrożeniami.

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

The `Update-MpSignature` daje możliwość ręcznej aktualizacji sygnatur antywirusowych używanych przez program Windows Defender. Sygnatury antywirusowe zawierają kluczowe informacje o znanym złośliwym oprogramowaniu, umożliwiając usłudze Windows Defender skuteczne wykrywanie i blokowanie zagrożeń. Uruchamiając to polecenie, upewniasz się, że twój system ma najnowsze sygnatury, zapewniając lepszą ochronę przed pojawiającymi się zagrożeniami.

Aby ręcznie zaktualizować sygnatury Windows Defender, otwórz sesję PowerShell z uprawnieniami administratora i wykonaj następujące polecenie:

```powershell
Update-MpSignature
```
To polecenie uruchamia proces aktualizacji, w którym **Windows Defender** łączy się z serwerami **Microsoft** w celu pobrania najnowszych **sygnatur antywirusowych**. Po zakończeniu aktualizacji Windows Defender będzie posiadał najbardziej aktualne informacje o znanym złośliwym oprogramowaniu, zwiększając jego zdolność do identyfikowania i eliminowania zagrożeń.

Aktualizowanie sygnatur Windows Defender jest niezbędne do utrzymania najwyższego poziomu ochrony przed stale ewoluującym krajobrazem **złośliwego oprogramowania** i **zagrożeń cybernetycznych**. Regularne aktualizowanie sygnatur przy użyciu `Update-MpSignature` zapewniasz, że Windows Defender może skutecznie chronić twój system.

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

The `Set-MpPreference` umożliwia dostosowanie różnych ustawień **Windows Defender**, pozwalając na dostosowanie jego zachowania do konkretnych wymagań bezpieczeństwa. To polecenie zapewnia elastyczność w konfigurowaniu opcji takich jak **ochrona w czasie rzeczywistym**, **ochrona oparta na chmurze** i **ustawienia systemu inspekcji sieci**.

Na przykład, można włączyć lub wyłączyć ochronę w czasie rzeczywistym za pomocą polecenia `Set-MpPreference` polecenie. Ochrona w czasie rzeczywistym aktywnie monitoruje system pod kątem złośliwych działań i zapewnia natychmiastową reakcję na zagrożenia. Aby włączyć ochronę w czasie rzeczywistym, wykonaj następujące polecenie:

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

Dostrajając te ustawienia za pomocą `Set-MpPreference` Możesz zoptymalizować **Windows Defender**, aby dostosować go do swoich konkretnych potrzeb w zakresie bezpieczeństwa i zapewnić solidną ochronę przed złośliwym oprogramowaniem i innymi złośliwymi działaniami.

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

The `Start-MpScan` jest potężnym narzędziem do inicjowania skanowania systemu pod kątem złośliwego oprogramowania, umożliwiając proaktywną identyfikację i eliminację złośliwych plików. To polecenie zapewnia elastyczność w wykonywaniu różnych rodzajów skanowania, w tym **szybkiego skanowania**, **pełnego skanowania** i **niestandardowego skanowania** z określonymi ścieżkami.

Aby wykonać **szybkie skanowanie** przy użyciu polecenia `Start-MpScan` wykonaj następujące polecenie PowerShell:

```powershell
Start-MpScan -ScanType QuickScan
```

Szybkie skanowanie koncentruje się na krytycznych obszarach systemu, w których często znajduje się złośliwe oprogramowanie, zapewniając szybką ocenę potencjalnych zagrożeń.

Aby uzyskać bardziej kompleksowe skanowanie, które sprawdza wszystkie pliki i katalogi w systemie, można zainicjować **pełne skanowanie**. Wykonaj następujące polecenie, aby przeprowadzić pełne skanowanie przy użyciu `Start-MpScan`

```powershell
Start-MpScan -ScanType FullScan
```

Pełne skanowanie zapewnia dokładne wykrycie i usunięcie złośliwego oprogramowania z systemu, ale jego ukończenie może potrwać dłużej niż w przypadku szybkiego skanowania.

Oprócz wstępnie zdefiniowanych typów skanowania, dostępne są następujące opcje `Start-MpScan` umożliwia wykonywanie niestandardowych skanów poprzez określenie określonych ścieżek lub plików do skanowania. Na przykład, można przeskanować określony katalog w systemie za pomocą następującego polecenia:

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

To polecenie zainicjuje niestandardowe skanowanie w określonym katalogu, umożliwiając ukierunkowanie na określone obszary systemu w celu wykrycia złośliwego oprogramowania.

Wykorzystując wszechstronność funkcji `Start-MpScan` Polecenie pozwala zaplanować skanowanie, zautomatyzować procesy bezpieczeństwa i zapewnić regularne wykrywanie i ograniczanie złośliwego oprogramowania w systemie.

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

The `Get-MpThreatCatalog` jest cennym źródłem uzyskiwania szczegółowych informacji o znanych zagrożeniach i ich atrybutach. Wykonując to polecenie, można uzyskać dostęp do kompleksowego katalogu zagrożeń, w tym danych dotyczących ich dotkliwości, powiązanych nazw plików i zalecanych działań w celu złagodzenia skutków.

Aby uzyskać informacje o określonych zagrożeniach przy użyciu `Get-MpThreatCatalog` wykonaj następujące kroki:

1. Otwórz sesję PowerShell z uprawnieniami administracyjnymi.
2. Wykonaj następujące polecenie:

```powershell
   Get-MpThreatCatalog
```
To polecenie wyświetli listę znanych zagrożeń wraz z odpowiadającymi im szczegółami.

Wynik polecenia `Get-MpThreatCatalog` Polecenie zawiera istotne informacje, takie jak

- **ThreatID**: Unikalny identyfikator zagrożenia.
- **Severity**: Wskazuje poziom dotkliwości zagrożenia, od niskiego do poważnego.
- Nazwa**: Nazwa lub opis zagrożenia.
- Ścieżka**: Ścieżka do pliku powiązanego z zagrożeniem.
- **RecommendedAction**: Zawiera wskazówki dotyczące zalecanych działań, które należy podjąć w celu złagodzenia zagrożenia.

Wykorzystując informacje uzyskane z `Get-MpThreatCatalog` można uzyskać cenny wgląd w potencjalne zagrożenia i podejmować świadome decyzje dotyczące odpowiednich działań w celu ich złagodzenia. Niezależnie od tego, czy chodzi o izolowanie, usuwanie czy monitorowanie określonego zagrożenia, szczegółowy katalog umożliwia skuteczne reagowanie na incydenty związane z bezpieczeństwem.

Więcej informacji na temat korzystania z `Get-MpThreatCatalog` i interpretacji wyników, należy zapoznać się z oficjalną dokumentacją Microsoft.

Zachowaj czujność i regularnie korzystaj z aplikacji `Get-MpThreatCatalog` aby być na bieżąco z ewoluującym krajobrazem zagrożeń i zwiększyć bezpieczeństwo swojego systemu.

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

The `Add-MpPreference` umożliwia dodawanie wykluczeń do programu Windows Defender, umożliwiając dostosowanie działania skanowania i ochrony w czasie rzeczywistym. Dodając wykluczenia, można określić pliki, foldery lub procesy, które program Windows Defender ma ignorować podczas skanowania bezpieczeństwa lub ochrony w czasie rzeczywistym.

Aby dodać wykluczenie przy użyciu `Add-MpPreference` musisz podać ścieżkę lub nazwę pliku, folderu lub procesu, który chcesz wykluczyć. Oto przykład dodawania wykluczenia dla folderu:

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

To polecenie zapewnia, że Windows Defender pomija skanowanie określonego folderu, redukując niepotrzebne alerty i potencjalne przerwy w przepływie pracy.

Wykluczenia mogą być przydatne w różnych scenariuszach, takich jak wykluczanie zaufanych aplikacji, środowisk programistycznych lub określonych plików, które mogą powodować fałszywe alarmy. Wykorzystując elastyczność `Add-MpPreference` można dostosować program Windows Defender do konkretnych potrzeb w zakresie bezpieczeństwa i zoptymalizować jego wydajność.

Skuteczna ochrona systemu przy jednoczesnym zminimalizowaniu fałszywych alarmów i niepotrzebnych przerw w skanowaniu dzięki wykorzystaniu potężnych możliwości wykluczania zapewnianych przez `Add-MpPreference`

## Wnioski

Polecenia Windows Defender PowerShell zapewniają **bogaty zestaw narzędzi** do zarządzania i zwiększania bezpieczeństwa systemu Windows. Wykorzystując te polecenia, można *automatyzować operacje bezpieczeństwa*, *konfigurować zaawansowane ustawienia* i płynnie włączać Windows Defender do przepływów pracy. Niezależnie od tego, czy jesteś **administratorem systemu**, czy **użytkownikiem zaawansowanym**, odkrywanie możliwości poleceń Windows Defender PowerShell może znacznie poprawić stan bezpieczeństwa twojego systemu.

Pamiętaj, że z wielką mocą wiąże się wielka odpowiedzialność. Korzystając z poleceń PowerShell, zachowaj ostrożność i upewnij się, że rozumiesz wpływ poleceń przed ich wykonaniem. Łącząc swoją wiedzę z mocą poleceń Windows Defender PowerShell, możesz podjąć proaktywne działania w celu ochrony systemu przed ewoluującymi zagrożeniami.

## Referencje

1. Microsoft Docs - [Windows Defender Cmdlets in Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2) Microsoft Docs - [Introduction to Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
