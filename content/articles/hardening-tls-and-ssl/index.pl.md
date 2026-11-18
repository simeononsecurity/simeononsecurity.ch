---
title: "Wzmocnij bezpieczeństwo komputera, wyłączając SSL oraz TLS 1.1 i starsze wersje"
date: 2023-02-08
lastmod: 2026-11-14
toc: true
draft: false
description: "Wyłącz SSL i stare wersje TLS, pozostawiając TLS 1.2 lub nowszy. Artykuł omawia Schannel i .NET w Windows oraz usługi Linux."
tags: ['Wzmocnienie bezpieczeństwa komputera', 'Wyłączanie SSL i TLS', 'Bezpieczeństwo danych', 'POODLE', 'BEAST', 'Heartbleed', 'Edytor rejestru Windows', 'Konfiguracja OpenSSL w Linux', 'Apache', 'Nginx']
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.webp"
coverAlt: "Komputer z symbolem kłódki oznaczającym bezpieczeństwo danych"
coverCaption: ""
---

## Wprowadzenie:

Komputery stały się ważną częścią codziennego życia, a wraz z nimi wzrosła potrzeba ochrony danych. SSL (Secure Socket Layer) i TLS (Transport Layer Security) chronią dane przesyłane przez sieć. Starsze wersje są podatne na ataki. Ten artykuł wyjaśnia, jak wyłączyć SSL oraz TLS 1.0 i 1.1, pozostawiając TLS 1.2 lub TLS 1.3.

*TLS 1.2 nie jest przestarzałym protokołem. Obecnym minimum jest TLS 1.2 lub nowszy. [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) definiuje TLS 1.3, a [RFC 8996](https://www.rfc-editor.org/rfc/rfc8996) formalnie uznaje TLS 1.0 i TLS 1.1 za przestarzałe.*

### Dlaczego wyłączyć SSL oraz TLS 1.1 i starsze wersje?

Starsze wersje SSL i TLS są podatne na zagrożenia takie jak POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) i Heartbleed. Ataki te mogą ujawnić poufne dane. Heartbleed dotyczył podatnych implementacji OpenSSL, a nie wersji protokołu. Zainstaluj poprawkę biblioteki i zmień ujawnione dane uwierzytelniające.

Aktualne [wskazówki Microsoft dotyczące ustawień rejestru Schannel](https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings) opisują protokoły dla obsługiwanych wersji Windows. Microsoft zaleca zasady grupy lub inne obsługiwane narzędzia zarządzania, jeśli są dostępne. Edytuj rejestr bezpośrednio tylko wtedy, gdy nie ma lepszej metody kontroli.

### Wyłączanie SSL oraz TLS 1.1 i starszych wersji w Windows:

W Windows można wyłączyć te protokoły w rejestrze. Poniższy skrypt PowerShell zmienia ustawienia Schannel dla klienta i serwera. Konfiguruje również .NET tak, aby używał systemowych ustawień TLS i silnej kryptografii.

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
# Wyłącz SSL v2
Disable-Protocol -Protocol "SSL 2.0"
# Wyłącz SSL v3
Disable-Protocol -Protocol "SSL 3.0"
# Wyłącz TLS 1.0
Disable-Protocol -Protocol "TLS 1.0"
# Wyłącz DTLS 1.0
Disable-Protocol -Protocol "DTLS 1.0"
# Wyłącz TLS 1.1
Disable-Protocol -Protocol "TLS 1.1"
# Protokół DTLS 1.1 nie istnieje. RFC 8996 uznaje DTLS 1.0 za przestarzały i zachowuje DTLS 1.2.

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

#### Wyłączanie SSL oraz TLS 1.1 i starszych wersji w Linux:

W Linux sposób wyłączenia starszych protokołów zależy od aplikacji i biblioteki. Zmiana `/etc/ssl/openssl.cnf` nie zastępuje ustawień każdego demona ani dołączonej biblioteki TLS. Wykonaj następujące kroki:

1. Otwórz terminal i zaloguj się jako root.
2. Przejdź do pliku konfiguracji OpenSSL, zwykle /etc/ssl/openssl.cnf.
3. Otwórz plik w edytorze tekstu, takim jak nano lub vim.
4. Znajdź dyrektywę protokołu usługi i ustaw TLS 1.2 jako wersję minimalną. Stara instrukcja `-TLSv1.2` wyłączała TLS 1.2, więc nie używaj jej jako współczesnego minimum.
5. Zapisz plik i zamknij edytor.
6. Uruchom ponownie usługi korzystające z OpenSSL, takie jak Apache lub Nginx, aby zastosować zmiany.

## Podsumowanie:

Wyłączenie SSL oraz TLS 1.1 i starszych wersji wzmacnia bezpieczeństwo komputera, zachowując zgodność z nowoczesnymi klientami TLS. Właściwe ustawienie należy do usługi negocjującej połączenie TLS. Testuj każdą aplikację osobno i nie zakładaj, że jeden plik OpenSSL kontroluje wszystkie demony.

Wyłączenie starszych wersji może wpłynąć na zgodność z niektórymi starszymi systemami. Dokładnie przetestuj zmiany i sprawdź ich skutki przed pełnym wdrożeniem.

Chroń poufne informacje i ogranicz ryzyko ataków. Sprawdź protokół negocjowany przez każdą usługę i udokumentuj tymczasowe wyjątki.

## Bieżąca lista kontrolna

- **Sprawdź negocjowany protokół.** Przetestuj klienta i serwer skanerem TLS lub zatwierdzonym testem wewnętrznym po obu stronach połączenia.
- **Pozostaw TLS 1.2 włączony.** Niektóre starsze aplikacje nadal go wymagają. Obsługa TLS 1.3 zależy od systemu operacyjnego i biblioteki.
- **Sprawdź DTLS osobno.** RFC 8996 uznaje DTLS 1.0 za przestarzały i nie definiuje protokołu DTLS 1.1.
- **Uruchom ponownie usługi.** Ustawienia Schannel i aplikacji często wymagają ponownego uruchomienia usługi lub systemu.
- **Udokumentuj wyjątki.** Zapisz każdy starszy punkt końcowy wymagający tymczasowych ustawień zgodności i wyznacz termin ich usunięcia.
