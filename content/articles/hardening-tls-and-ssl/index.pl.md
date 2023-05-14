---
title: "Wzmocnienie bezpieczeństwa komputera poprzez wyłączenie SSL i TLS 1.2 i niższych"
date: 2023-02-08
toc: true
draft: false
description: "W artykule omówiono kroki mające na celu zwiększenie bezpieczeństwa danych poprzez wyłączenie w systemach Windows i Linux starszych wersji protokołów SSL i TLS, które są podatne na cyberzagrożenia, takie jak POODLE, BEAST i Heartbleed."
tags: ["Wzmocnienie bezpieczeństwa komputerowego", "Wyłączenie SSL i TLS", "Bezpieczeństwo danych", "POODLE", "BEAST", "Heartbleed", "Edytor rejestru Windows", "Konfiguracja OpenSSL w systemie Linux", "Apache", "Nginx"]
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.png"
coverAlt: "Komputer z symbolem kłódki symbolizującym bezpieczeństwo danych"
coverCaption: ""
---

## Wprowadzenie:

Komputery stały się istotnym aspektem naszego codziennego życia, a wraz z tym znacznie wzrosła potrzeba zapewnienia bezpieczeństwa danych. Wśród różnych metod stosowanych do zabezpieczenia danych w tranzycie, SSL (Secure Socket Layer) i TLS (Transport Layer Security) są powszechnie stosowanymi protokołami. Jednak wraz z rozwojem technologii starsze wersje tych protokołów stają się podatne na cyberataki. W tym artykule omówimy kroki mające na celu utwardzenie komputerów poprzez wyłączenie SSL i wszystkich wersji TLS 1.2 i niższych, aby zachować bezpieczeństwo danych.

### Dlaczego warto wyłączyć SSL i TLS 1.2 i niższe?

Starsze wersje SSL i TLS są podatne na kilka zagrożeń bezpieczeństwa, takich jak POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) i Heartbleed. Ataki te mogą prowadzić do ujawnienia wrażliwych informacji, co sprawia, że kluczowe jest wyłączenie stosowania przestarzałych protokołów.

### Wyłączenie SSL i TLS 1.2 i niższych w systemie Windows:

W systemie Windows proces wyłączenia protokołów SSL i TLS 1.2 i niższych można osiągnąć poprzez edytor rejestru. Poniżej znajduje się skrypt powershell do wykonania zadania:

```powershell
Function Disable-Protocol {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Protocol
    )
    $ServerPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\$Protocol\Server"
    $ClientPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\$Protocol\Client"
    New-Item -Path $ServerPath -Force
    New-Item -Path $ClientPath -Force
    Set-ItemProperty -Path $ServerPath -Force -Name Enabled -Type "DWORD" -Value 0
    Set-ItemProperty -Path $ServerPath -Force -Name DisabledByDefault -Type "DWORD" -Value 1
    Set-ItemProperty -Path $ClientPath -Force -Name Enabled -Type "DWORD" -Value 0
    Set-ItemProperty -Path $ClientPath -Force -Name DisabledByDefault -Type "DWORD" -Value 1
}
# Disable SSL v2
Disable-Protocol -Protocol "SSL 2.0"
# Disable SSL v3
Disable-Protocol -Protocol "SSL 3.0"
# Disable TLS 1.0
Disable-Protocol -Protocol "TLS 1.0"
# Disable DTLS 1.0
Disable-Protocol -Protocol "DTLS 1.0"
# Disable TLS 1.1
Disable-Protocol -Protocol "TLS 1.1"
# Disable DTLS 1.1
Disable-Protocol -Protocol "DTLS 1.1"

function Set-NETStrongAuthentication {
    param(
        [string]$RegistryPath,
        [string]$Name,
        [string]$Type,
        [int]$Value
    )
    Set-ItemProperty -Path $RegistryPath -Force -Name $Name -Type $Type -Value $Value
}

$NETVersions = @("2.0.50727", "3.0", "4.0.30319")

foreach ($version in $NETVersions) {
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\Microsoft\.NETFramework\v$version" -Name SchUseStrongCrypto -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\Microsoft\.NETFramework\v$version" -Name SystemDefaultTlsVersions -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v$version" -Name SchUseStrongCrypto -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v$version" -Name SystemDefaultTlsVersions -Type "DWORD" -Value 0x00000001
}
```

#### Wyłączenie SSL i TLS 1.2 i niższych w systemie Linux:

W systemie Linux proces wyłączenia SSL i TLS 1.2 i poniżej można osiągnąć poprzez modyfikację pliku konfiguracyjnego OpenSSL. Oto kroki, które należy wykonać:

1. Otwórz terminal i zaloguj się jako root.
2. Przejdź do pliku konfiguracyjnego OpenSSL. Zazwyczaj znajduje się on pod adresem /etc/ssl/openssl.cnf.
3. Otwórz plik za pomocą edytora tekstu, takiego jak nano lub vim.
4. Zlokalizuj dyrektywę SSLProtocol i ustaw jej wartość na -TLSv1.2.
5. Zapisz plik i zamknij edytor tekstu.
6. Uruchom ponownie usługi korzystające z OpenSSL, takie jak Apache czy Nginx, aby zmiany zaczęły obowiązywać.

## Wnioski:

Wyłączając SSL i wszystkie TLS w wersji 1.2 i niższej, możesz utwardzić bezpieczeństwo swojego komputera i chronić wrażliwe informacje przed potencjalnymi cyberzagrożeniami. Jest to prosty proces, który można wykonać przy minimalnym wysiłku, co czyni go krytycznym aspektem utrzymania bezpieczeństwa komputera. Wdrażając kroki opisane w tym artykule, możesz zabezpieczyć swoje dane i zapobiec cyberatakom, zmniejszając tym samym ryzyko narażenia wrażliwych informacji.

Należy pamiętać, że chociaż wyłączenie tych starszych wersji protokołów SSL i TLS może poprawić bezpieczeństwo komputera, może również wpłynąć na kompatybilność z niektórymi starszymi systemami. Dlatego przed pełnym wdrożeniem wprowadzonych zmian należy dokładnie przetestować je i upewnić się, że nie mają one negatywnego wpływu na system.

Podsumowując, utwardzenie komputera poprzez wyłączenie protokołu SSL i wszystkich wersji TLS 1.2 i niższych jest krytycznym krokiem w utrzymaniu bezpieczeństwa poufnych informacji i zapobieganiu cyberatakom. Kroki przedstawione w tym artykule stanowią prosty przewodnik po zabezpieczeniu komputera, ułatwiając osobom i organizacjom wdrożenie niezbędnych środków bezpieczeństwa.