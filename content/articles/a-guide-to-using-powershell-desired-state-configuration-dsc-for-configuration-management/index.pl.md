---
title: "PowerShell DSC: przewodnik dla początkujących"
date: 2023-04-02
toc: true
draft: false
description: "Poznaj możliwości PowerShell Desired State Configuration (DSC), aby zautomatyzować i zarządzać konfiguracjami systemu w celu zapewnienia bezpiecznego i zgodnego środowiska."
tags: ["PowerShell", "DSC", "Zarządzanie konfiguracją", "Automatyzacja", "Windows", "Administracja systemem", "Najlepsze praktyki", "Zgodność", "Bezpieczeństwo", "Infrastruktura", "DevOps", "Konfiguracja serwera", "Testowanie", "Git", "Kontrola źródła", "Przepisy rządowe", "NIST", "CIS", "Dryft konfiguracji", "Zasoby niestandardowe"]
cover: "/img/cover/A_cartoon_image_of_a_confident_system_administrator.png"
coverAlt: "Kreskówkowy obraz pewnego siebie administratora systemu z peleryną superbohatera, stojącego obok dobrze zorganizowanej szafy serwerowej, trzymającego skrypt PowerShell DSC w jednej ręce i tarczę z logo Windows w drugiej, chroniącego serwery przed dryfem konfiguracji i zagrożeniami bezpieczeństwa."
coverCaption: ""
---

**Przewodnik po używaniu PowerShell Desired State Configuration (DSC) do zarządzania konfiguracją**

______

## Wprowadzenie

PowerShell Desired State Configuration (**DSC**) to potężne i **niezbędne narzędzie** dla administratorów IT i specjalistów DevOps, pozwalające im zautomatyzować wdrażanie i konfigurację systemów Windows i Linux. Ten artykuł zawiera kompleksowy przewodnik po używaniu PowerShell DSC do zarządzania konfiguracją, w tym najlepsze praktyki, przepisy rządowe i przydatne odniesienia.

______

## Pierwsze kroki z PowerShell Desired State Configuration

### Czym jest konfiguracja pożądanego stanu PowerShell?

PowerShell Desired State Configuration (**DSC**) to **język deklaratywny** wbudowany w PowerShell, który umożliwia administratorom automatyzację konfiguracji systemów, aplikacji i usług. Zapewnia **znormalizowany i spójny** sposób zarządzania konfiguracjami i zapewnienia, że systemy pozostaną w pożądanym stanie.

### Instalacja PowerShell DSC

Aby rozpocząć pracę z PowerShell DSC, należy zainstalować **Windows Management Framework (WMF)**. WMF to pakiet zawierający PowerShell, DSC i inne niezbędne narzędzia do zarządzania. Najnowszą wersję WMF można pobrać ze strony [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=54616)

______

## Tworzenie i stosowanie konfiguracji DSC

### Zapisywanie konfiguracji DSC

Konfiguracja DSC to **skrypt PowerShell** opisujący pożądany stan systemu. Składa się z jednego lub więcej **zasobów DSC**, które definiują ustawienia i właściwości wymagane dla komponentów systemu. Oto przykład prostej konfiguracji DSC, która instaluje rolę Web Server (IIS) na serwerze Windows:

```powershell
Configuration InstallIIS {
    Import-DscResource -ModuleName PSDesiredStateConfiguration

    Node 'localhost' {
        WindowsFeature IIS {
            Ensure = 'Present'
            Name   = 'Web-Server'
        }
    }
}
```
### Stosowanie konfiguracji DSC
Po napisaniu konfiguracji DSC można zastosować ją do systemu docelowego za pomocą polecenia cmdlet **Start-DscConfiguration**. Najpierw należy skompilować skrypt konfiguracyjny, uruchamiając go w PowerShell:

```powershell
InstallIIS
```

Spowoduje to wygenerowanie pliku **MOF** (Managed Object Format) zawierającego skompilowaną konfigurację. Następnie należy zastosować konfigurację do systemu docelowego za pomocą następującego polecenia:

```powershell
Start-DscConfiguration -Path .\InstallIIS -Wait -Verbose
```

## Najlepsze praktyki korzystania z PowerShell DSC

### Modularyzacja konfiguracji

Twórz **modułowe i wielokrotnego użytku** konfiguracje, rozdzielając różne komponenty swojej infrastruktury na **poszczególne zasoby DSC**. Takie podejście pozwala na łatwe **utrzymanie i skalowanie** konfiguracji w miarę rozwoju środowiska.

### Użyj Kontroli Źródła

Zawsze przechowuj konfiguracje DSC i niestandardowe zasoby w **systemie kontroli źródeł**, takim jak Git. Praktyka ta umożliwia śledzenie zmian, współpracę z zespołem i łatwe przywracanie poprzednich wersji konfiguracji w razie potrzeby.

### Testuj swoje konfiguracje

**Testowanie** jest kluczowym aspektem zarządzania konfiguracją. Przed wdrożeniem konfiguracji DSC należy przetestować ją w **środowisku nieprodukcyjnym**, aby upewnić się, że działa zgodnie z oczekiwaniami i nie wprowadza żadnych niezamierzonych konsekwencji. Możesz również użyć narzędzi takich jak [Pester](https://github.com/pester/Pester) do automatycznego testowania konfiguracji DSC.

______

## Przepisy i wytyczne rządowe

### Wytyczne NIST

Narodowy Instytut Standardów i Technologii (NIST) zapewnia wytyczne dotyczące zarządzania konfiguracją systemu. W szczególności [NIST SP 800-53](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) publication contains a section (CM-2) w sprawie konfiguracji bazowych, które są istotne dla korzystania z DSC. Wytyczne te podkreślają znaczenie utrzymywania, monitorowania i kontrolowania zmian w konfiguracji systemu. PowerShell DSC może pomóc organizacjom w przestrzeganiu tych wytycznych, zapewniając spójny i zautomatyzowany sposób zarządzania konfiguracjami systemu.

### Federalna ustawa o zarządzaniu bezpieczeństwem informacji (FISMA)

Federalna ustawa o zarządzaniu bezpieczeństwem informacji [FISMA](https://www.dhs.gov/cisa/federal-information-security-modernization-act) wymaga od agencji federalnych wdrożenia kompleksowych ram zapewniających skuteczność kontroli bezpieczeństwa informacji. Zarządzanie konfiguracją jest kluczowym elementem zgodności z FISMA, a PowerShell DSC może odgrywać istotną rolę w pomaganiu organizacjom w spełnianiu tych wymagań.
______

## Wnioski

PowerShell Desired State Configuration (DSC) to potężne i elastyczne narzędzie do automatyzacji wdrażania i zarządzania konfiguracjami systemu. Postępując zgodnie z najlepszymi praktykami i przestrzegając przepisów rządowych, możesz zapewnić, że systemy Twojej organizacji pozostaną w pożądanym stanie przy jednoczesnym zachowaniu zgodności. Nie zapomnij skorzystać z zasobów udostępnionych w tym artykule, aby lepiej zrozumieć PowerShell DSC i usprawnić procesy zarządzania konfiguracją.
______

## Referencje

- [PowerShell Desired State Configuration (DSC) official documentation](https://learn.microsoft.com/en-us/powershell/dsc/getting-started/wingettingstarted?view=dsc-1.1)
- [NIST SP 800-53 - Security and Privacy Controls for Federal Information Systems and Organizations](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)
- [Federal Information Security Management Act (FISMA)](https://www.dhs.gov/cisa/federal-information-security-modernization-act)
- [Pester - PowerShell Testing Framework](https://github.com/pester/Pester)
- [A Beginner's Guide to Using Encryption for Data Protection](https://simeononsecurity.com/articles/a-beginners-guide-to-using-encryption-for-data-protection/)
- [Best Practices for Installing Security Patches on Windows](https://simeononsecurity.com/articles/best-practices-for-installing-security-patches-on-windows/)




