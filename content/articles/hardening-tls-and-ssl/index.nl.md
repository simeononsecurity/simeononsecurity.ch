---
title: "De beveiliging van uw computer versterken door SSL en TLS 1.2 en lager uit te schakelen"
date: 2023-02-08
toc: true
draft: false
description: "In dit artikel worden de stappen besproken om de gegevensbeveiliging te verbeteren door oudere versies van SSL- en TLS-protocollen, die kwetsbaar zijn voor cyberdreigingen zoals POODLE, BEAST en Heartbleed, uit te schakelen in Windows- en Linux-systemen."
tags: ["Verbetering van de computerbeveiliging", "SSL en TLS uitschakelen", "Gegevensbeveiliging", "POODLE", "BEAST", "Heartbleed", "Windows register editor", "Linux OpenSSL configuratie", "Apache", "Nginx"]
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.png"
coverAlt: "Een computer met een hangslotsymbool voor gegevensbeveiliging"
coverCaption: ""
---

## Introductie:

Computers zijn een cruciaal aspect van ons dagelijks leven geworden, en daarmee is de behoefte aan gegevensbeveiliging aanzienlijk toegenomen. Van de verschillende methoden die worden gebruikt om gegevens te beveiligen, zijn SSL (Secure Socket Layer) en TLS (Transport Layer Security) veelgebruikte protocollen. Naarmate de technologie evolueert, worden oudere versies van deze protocollen echter kwetsbaar voor cyberaanvallen. In dit artikel bespreken we de stappen om computers te harden door SSL en alle TLS-versies 1.2 en lager uit te schakelen om de gegevens veilig te houden.

### Waarom SSL en TLS 1.2 en lager uitschakelen?

Oudere versies van SSL en TLS zijn kwetsbaar voor verschillende veiligheidsbedreigingen zoals POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) en Heartbleed. Deze aanvallen kunnen leiden tot de blootstelling van gevoelige informatie, waardoor het van cruciaal belang is het gebruik van verouderde protocollen uit te schakelen.

### SSL en TLS 1.2 en lager in Windows uitschakelen:

In Windows kan het proces van het uitschakelen van SSL en TLS 1.2 en lager worden bereikt via de register-editor. Hier is een powershell-script om de taak uit te voeren:

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

#### SSL en TLS 1.2 en lager uitschakelen in Linux:

In Linux kan het proces om SSL en TLS 1.2 en lager uit te schakelen worden bereikt door het OpenSSL-configuratiebestand te wijzigen. Dit zijn de te volgen stappen:

1. Open de terminal en log in als root.
2. Navigeer naar het OpenSSL configuratiebestand. Gewoonlijk staat het in /etc/ssl/openssl.cnf.
3. Open het bestand met een tekstverwerker zoals nano of vim.
4. Zoek de richtlijn SSLProtocol en stel de waarde in op -TLSv1.2.
5. Sla het bestand op en sluit de tekstverwerker.
6. Herstart de diensten die OpenSSL gebruiken, zoals Apache of Nginx, zodat de wijzigingen van kracht worden.

## Conclusie:

Door SSL en alle TLS-versies 1.2 en lager uit te schakelen, kunt u de beveiliging van uw computer verharden en gevoelige informatie beschermen tegen potentiële cyberdreigingen. Het is een eenvoudig proces dat met minimale inspanning kan worden uitgevoerd, waardoor het een cruciaal aspect is van het handhaven van de beveiliging van uw computer. Door de in dit artikel beschreven stappen uit te voeren, kunt u uw gegevens veilig houden en cyberaanvallen voorkomen, waardoor het risico dat gevoelige informatie wordt blootgesteld, afneemt.

Het is belangrijk op te merken dat het uitschakelen van deze oudere versies van SSL- en TLS-protocollen de beveiliging van uw computer kan verbeteren, maar ook gevolgen kan hebben voor de compatibiliteit met sommige oudere systemen. Daarom is het essentieel om de aangebrachte wijzigingen grondig te testen en ervoor te zorgen dat er geen nadelige gevolgen zijn voor uw systeem voordat u ze volledig implementeert.

Kortom, het harden van uw computer door het uitschakelen van SSL en alle TLS-versies 1.2 en lager is een essentiële stap in het handhaven van de veiligheid van gevoelige informatie en het voorkomen van cyberaanvallen. De in dit artikel beschreven stappen vormen een eenvoudige gids voor het beveiligen van uw computer, waardoor het voor particulieren en organisaties gemakkelijk is om de nodige beveiligingsmaatregelen te treffen.