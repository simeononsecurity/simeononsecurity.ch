---
title: "Reforceu la seguretat de l’ordinador desactivant SSL i TLS 1.1 i versions anteriors"
date: 2023-02-08
lastmod: 2026-11-14
toc: true
draft: false
description: "Desactiveu SSL i les versions antigues de TLS i manteniu TLS 1.2 o posterior. El text tracta Schannel i .NET a Windows i els serveis Linux."
tags: ['Reforç de la seguretat informàtica', 'Desactivació d’SSL i TLS', 'Seguretat de les dades', 'POODLE', 'BEAST', 'Heartbleed', 'Editor del Registre de Windows', 'Configuració d’OpenSSL a Linux', 'Apache', 'Nginx']
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.webp"
coverAlt: "Un ordinador amb un símbol de cadenat que representa la seguretat de les dades"
coverCaption: ""
---

## Introducció:

Els ordinadors formen part essencial de la vida diària, i també ha crescut la necessitat de protegir les dades. SSL (Secure Socket Layer) i TLS (Transport Layer Security) protegeixen les dades durant la transmissió. Les versions antigues ara són vulnerables als atacs. Aquest article explica com desactivar SSL i TLS 1.0 i 1.1 i mantenir TLS 1.2 o TLS 1.3 disponible.

*TLS 1.2 no és un protocol obsolet. El nivell mínim actual és TLS 1.2 o posterior. [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) defineix TLS 1.3, mentre que [RFC 8996](https://www.rfc-editor.org/rfc/rfc8996) declara obsolets formalment TLS 1.0 i TLS 1.1.*

### Per què desactivar SSL i TLS 1.1 i versions anteriors?

Les versions antigues de SSL i TLS són vulnerables a amenaces com POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) i Heartbleed. Aquests atacs poden exposar informació sensible. Heartbleed va afectar implementacions vulnerables d’OpenSSL, però no era una versió del protocol. Apliqueu el pegat a la biblioteca i canvieu les credencials exposades.

Les [indicacions actuals de Microsoft sobre el Registre de Schannel](https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings) enumeren la configuració de protocols per a les versions compatibles de Windows. Microsoft recomana la Directiva de grup o altres eines d’administració compatibles quan estiguin disponibles. Editeu directament el Registre només quan no hi hagi un control millor.

### Desactivar SSL i TLS 1.1 i versions anteriors a Windows:

A Windows, podeu desactivar aquests protocols mitjançant el Registre. L’script de PowerShell següent canvia la configuració de Schannel per als clients i els servidors. També configura .NET perquè utilitzi els valors TLS predeterminats del sistema operatiu i una criptografia robusta.

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
# Desactiva SSL v2
Disable-Protocol -Protocol "SSL 2.0"
# Desactiva SSL v3
Disable-Protocol -Protocol "SSL 3.0"
# Desactiva TLS 1.0
Disable-Protocol -Protocol "TLS 1.0"
# Desactiva DTLS 1.0
Disable-Protocol -Protocol "DTLS 1.0"
# Desactiva TLS 1.1
Disable-Protocol -Protocol "TLS 1.1"
# No hi ha cap protocol DTLS 1.1. L’RFC 8996 desaconsella DTLS 1.0 i manté DTLS 1.2.

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

#### Desactivar SSL i TLS 1.1 i versions anteriors a Linux:

A Linux, la manera de desactivar els protocols antics depèn de l’aplicació i la biblioteca. Modificar `/etc/ssl/openssl.cnf` no substitueix la configuració de cada dimoni ni de les biblioteques TLS incloses. Seguiu aquests passos:

1. Obriu el terminal i inicieu sessió com a root.
2. Aneu al fitxer de configuració d’OpenSSL. Normalment és a /etc/ssl/openssl.cnf.
3. Obriu el fitxer amb un editor de text com nano o vim.
4. Cerqueu la directiva de protocol del servei i establiu TLS 1.2 com a mínim. La instrucció antiga `-TLSv1.2` desactivava TLS 1.2. No la feu servir com a mínim actual.
5. Deseu el fitxer i tanqueu l’editor.
6. Reinicieu els serveis que utilitzen OpenSSL, com Apache o Nginx, per aplicar els canvis.

## Conclusió:

Desactivar SSL i TLS 1.1 i les versions anteriors reforça la seguretat de l’ordinador i manté la compatibilitat amb els clients TLS moderns. La configuració correcta pertany al servei que negocia la connexió TLS. Proveu cada aplicació en lloc de suposar que un únic fitxer OpenSSL controla tots els dimonis.

Desactivar aquestes versions antigues pot afectar la compatibilitat amb alguns sistemes antics. Proveu bé els canvis i confirmeu que no tinguin efectes adversos abans d’aplicar-los del tot.

Protegiu la informació sensible i reduïu el risc d’atacs. Comproveu quin protocol negocia cada servei i documenteu les excepcions temporals.

## Llista de verificació actual

- **Confirmeu el protocol negociat.** Proveu el client i el servidor amb un escàner TLS o una prova interna aprovada als dos extrems de la connexió.
- **Manteniu TLS 1.2 activat.** Algunes aplicacions antigues encara el necessiten. El suport de TLS 1.3 depèn del sistema operatiu i la biblioteca.
- **Reviseu DTLS per separat.** RFC 8996 declara obsolet DTLS 1.0. No defineix cap protocol DTLS 1.1.
- **Reinicieu els serveis afectats.** La configuració de Schannel i de les aplicacions sovint requereix reiniciar el servei o el sistema.
- **Documenteu les excepcions.** Registreu cada punt final antic que necessiti temporalment una configuració de compatibilitat i assigneu-li una data de retirada.
