---
title: "Beveilig uw computer door SSL en TLS 1.1 en ouder uit te schakelen"
date: 2023-02-08
lastmod: 2026-11-14
toc: true
draft: false
description: "Schakel SSL en oude TLS-versies uit en houd TLS 1.2 of nieuwer beschikbaar. Dit artikel behandelt Schannel en .NET op Windows en Linux-services."
tags: ['Computerbeveiliging versterken', 'SSL en TLS uitschakelen', 'Gegevensbeveiliging', 'POODLE', 'BEAST', 'Heartbleed', 'Windows Register-editor', 'OpenSSL-configuratie op Linux', 'Apache', 'Nginx']
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.webp"
coverAlt: "Een computer met een hangslot als symbool voor gegevensbeveiliging"
coverCaption: ""
---

## Inleiding:

Computers zijn een belangrijk onderdeel van ons dagelijks leven geworden. Daardoor is ook de behoefte aan gegevensbeveiliging gegroeid. SSL (Secure Socket Layer) en TLS (Transport Layer Security) beschermen gegevens tijdens transport. Oudere versies zijn kwetsbaar voor aanvallen. Dit artikel legt uit hoe u SSL en TLS 1.0 en 1.1 uitschakelt en TLS 1.2 of TLS 1.3 beschikbaar houdt.

*TLS 1.2 is geen verouderd protocol. De huidige ondergrens is TLS 1.2 of nieuwer. [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) definieert TLS 1.3. [RFC 8996](https://www.rfc-editor.org/rfc/rfc8996) verklaart TLS 1.0 en TLS 1.1 formeel verouderd.*

### Waarom SSL en TLS 1.1 en ouder uitschakelen?

Oudere versies van SSL en TLS zijn kwetsbaar voor bedreigingen zoals POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) en Heartbleed. Deze aanvallen kunnen gevoelige gegevens blootleggen. Heartbleed trof kwetsbare OpenSSL-implementaties en was zelf geen protocolversie. Werk de bibliotheek bij en vervang blootgestelde inloggegevens.

De actuele [Microsoft-richtlijnen voor Schannel-registerinstellingen](https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings) bevatten protocolinstellingen voor ondersteunde Windows-versies. Microsoft adviseert Groepsbeleid of andere ondersteunde beheertools als die beschikbaar zijn. Bewerk het register rechtstreeks alleen als er geen betere beheermethode is.

### SSL en TLS 1.1 en ouder uitschakelen in Windows:

In Windows kunt u deze protocollen uitschakelen via het register. Het PowerShell-script hieronder wijzigt de Schannel-instellingen voor clients en servers. Het stelt .NET ook in op de TLS-standaardwaarden van het besturingssysteem en sterke cryptografie.

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
# SSL v2 uitschakelen
Disable-Protocol -Protocol "SSL 2.0"
# SSL v3 uitschakelen
Disable-Protocol -Protocol "SSL 3.0"
# TLS 1.0 uitschakelen
Disable-Protocol -Protocol "TLS 1.0"
# DTLS 1.0 uitschakelen
Disable-Protocol -Protocol "DTLS 1.0"
# TLS 1.1 uitschakelen
Disable-Protocol -Protocol "TLS 1.1"
# Er bestaat geen DTLS 1.1-protocol. RFC 8996 verklaart DTLS 1.0 verouderd en handhaaft DTLS 1.2.

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

#### SSL en TLS 1.1 en ouder uitschakelen in Linux:

In Linux hangt het uitschakelen van oude protocollen af van de toepassing en bibliotheek. Een wijziging aan `/etc/ssl/openssl.cnf` vervangt niet de instellingen van elke daemon of ingebouwde TLS-bibliotheek. Volg deze stappen:

1. Open de terminal en meld u aan als root.
2. Ga naar het OpenSSL-configuratiebestand. Dit staat meestal in /etc/ssl/openssl.cnf.
3. Open het bestand met een teksteditor zoals nano of vim.
4. Zoek de protocolinstructie van de service en stel TLS 1.2 in als minimum. De oude instructie `-TLSv1.2` schakelde TLS 1.2 uit. Gebruik die daarom niet als moderne ondergrens.
5. Sla het bestand op en sluit de editor.
6. Herstart services die OpenSSL gebruiken, zoals Apache of Nginx, zodat de wijzigingen ingaan.

## Conclusie:

Door SSL en TLS 1.1 en ouder uit te schakelen, beveiligt u uw computer en behoudt u compatibiliteit met moderne TLS-clients. De juiste instelling hoort bij de service die de TLS-verbinding onderhandelt. Test elke toepassing afzonderlijk. Ga er niet van uit dat één OpenSSL-bestand alle daemons beheert.

Het uitschakelen van deze oude versies kan de compatibiliteit met sommige oudere systemen beïnvloeden. Test de wijzigingen grondig en controleer de gevolgen voordat u ze volledig invoert.

Bescherm gevoelige informatie en verlaag het risico op aanvallen. Controleer welk protocol elke service onderhandelt en documenteer tijdelijke uitzonderingen.

## Huidige controlelijst

- **Controleer het onderhandelde protocol.** Test client en server met een TLS-scanner of een goedgekeurde interne test aan beide kanten van de verbinding.
- **Laat TLS 1.2 ingeschakeld.** Sommige oudere toepassingen hebben het nog nodig. Ondersteuning voor TLS 1.3 hangt af van het besturingssysteem en de bibliotheek.
- **Controleer DTLS apart.** RFC 8996 verklaart DTLS 1.0 verouderd. De RFC definieert geen DTLS 1.1-protocol.
- **Herstart getroffen services.** Schannel- en applicatie-instellingen vereisen vaak een herstart van de service of het systeem.
- **Documenteer uitzonderingen.** Noteer oude eindpunten die tijdelijk een compatibiliteitsinstelling nodig hebben en stel een verwijderdatum vast.
