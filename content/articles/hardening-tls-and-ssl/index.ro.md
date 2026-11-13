---
title: "Întăriți securitatea computerului dezactivând SSL și TLS 1.1 și versiunile anterioare"
date: 2023-02-08
lastmod: 2026-11-13
toc: true
draft: false
description: "Dezactivați SSL și versiunile vechi TLS, păstrând TLS 1.2 sau mai nou. Ghidul acoperă Schannel și .NET în Windows și serviciile Linux."
tags: ['Întărirea securității computerului', 'Dezactivarea SSL și TLS', 'Securitatea datelor', 'POODLE', 'BEAST', 'Heartbleed', 'Editorul de registry Windows', 'Configurația OpenSSL pe Linux', 'Apache', 'Nginx']
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.webp"
coverAlt: "Un computer cu simbolul unui lacăt care reprezintă securitatea datelor"
coverCaption: ""
---

## Introducere:

Computerele au devenit o parte esențială a vieții noastre, iar nevoia de a proteja datele a crescut. SSL (Secure Socket Layer) și TLS (Transport Layer Security) sunt protocoale folosite pe scară largă pentru protejarea datelor în tranzit. Pe măsură ce tehnologia evoluează, versiunile vechi devin vulnerabile la atacuri. Acest articol explică cum să dezactivați SSL și TLS 1.0 și 1.1, păstrând disponibile TLS 1.2 sau TLS 1.3.

*TLS 1.2 nu este un protocol învechit. Nivelul minim actual este TLS 1.2 sau mai nou. [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) definește TLS 1.3, iar [RFC 8996](https://www.rfc-editor.org/rfc/rfc8996) depreciază formal TLS 1.0 și TLS 1.1.*

### De ce să dezactivați SSL și TLS 1.1 și versiunile anterioare?

Versiunile vechi SSL și TLS sunt vulnerabile la amenințări precum POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) și Heartbleed. Aceste atacuri pot expune informații sensibile, de aceea protocoalele vechi trebuie dezactivate. Heartbleed a afectat implementări OpenSSL vulnerabile, nu a fost o versiune de protocol. Aplicați corecția bibliotecii și schimbați datele de autentificare expuse.

[Ghidul actual Microsoft pentru registry Schannel](https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings) listează setările de protocol pentru versiunile Windows acceptate. Microsoft recomandă Group Policy sau alte instrumente de administrare acceptate, când sunt disponibile. Modificați direct registry-ul doar dacă nu există un control mai potrivit.

### Dezactivarea SSL și TLS 1.1 și a versiunilor anterioare în Windows:

În Windows, puteți dezactiva aceste protocoale prin editorul registry. Scriptul PowerShell de mai jos modifică setările Schannel pentru client și server. Configurează și .NET să folosească valorile TLS implicite ale sistemului de operare și criptografie puternică.

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
# There is no DTLS 1.1 protocol. RFC 8996 deprecates DTLS 1.0 and retains DTLS 1.2.

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

#### Dezactivarea SSL și TLS 1.1 și a versiunilor anterioare în Linux:

În Linux, dezactivarea protocoalelor vechi depinde de aplicație și bibliotecă. Modificarea fișierului `/etc/ssl/openssl.cnf` nu suprascrie setările fiecărui daemon sau ale bibliotecilor TLS incluse. Urmați pașii:

1. Deschideți terminalul și conectați-vă ca root.
2. Accesați fișierul de configurare OpenSSL. De obicei, acesta se află în /etc/ssl/openssl.cnf.
3. Deschideți fișierul cu un editor de text, precum nano sau vim.
4. Găsiți directiva de protocol a serviciului și setați versiunea minimă la TLS 1.2. Instrucțiunea veche `-TLSv1.2` dezactiva TLS 1.2, deci nu o folosiți ca nivel minim actual.
5. Salvați fișierul și închideți editorul.
6. Reporniți serviciile care folosesc OpenSSL, precum Apache sau Nginx, pentru ca modificările să se aplice.

## Concluzie:

Dezactivarea SSL și TLS 1.1 și a versiunilor anterioare întărește securitatea computerului, păstrând compatibilitatea cu clienții TLS moderni. Setarea corectă aparține serviciului care negociază conexiunea TLS. Testați fiecare aplicație, fără să presupuneți că un singur fișier OpenSSL controlează toți daemonii.

Dezactivarea acestor versiuni vechi poate afecta compatibilitatea cu unele sisteme mai vechi. Testați atent modificările și confirmați că nu produc efecte nedorite înainte de implementarea completă.

Urmați pașii din articol pentru a proteja informațiile sensibile și a reduce riscul atacurilor. Identificați mai întâi protocolul negociat de fiecare serviciu, apoi documentați excepțiile temporare.

## Listă de verificare actuală

- **Confirmați protocolul negociat.** Testați clientul și serverul cu un scaner TLS sau cu un test intern aprobat, la ambele capete ale conexiunii.
- **Păstrați TLS 1.2 activat.** Unele aplicații vechi încă au nevoie de acesta, iar suportul pentru TLS 1.3 depinde de sistemul de operare și bibliotecă.
- **Verificați DTLS separat.** RFC 8996 depreciază DTLS 1.0. Nu definește un protocol DTLS 1.1.
- **Reporniți serviciile afectate.** Setările Schannel și ale aplicațiilor necesită adesea repornirea serviciului sau a sistemului.
- **Documentați excepțiile.** Înregistrați fiecare endpoint vechi care are nevoie temporar de o setare de compatibilitate și stabiliți data eliminării.
