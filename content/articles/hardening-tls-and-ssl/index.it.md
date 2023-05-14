---
title: "Per rafforzare la sicurezza del computer, disabilitate SSL e TLS 1.2 e inferiori."
date: 2023-02-08
toc: true
draft: false
description: "Questo articolo illustra i passaggi per migliorare la sicurezza dei dati disabilitando le vecchie versioni dei protocolli SSL e TLS, vulnerabili alle minacce informatiche come POODLE, BEAST e Heartbleed, nei sistemi Windows e Linux."
tags: ["Rafforzamento della sicurezza informatica", "Disabilitare SSL e TLS", "Sicurezza dei dati", "POODIO", "BESTIA", "Heartbleed", "Editor del registro di Windows", "Configurazione OpenSSL di Linux", "Apache", "Nginx"]
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.png"
coverAlt: "Un computer con il simbolo di un lucchetto che rappresenta la sicurezza dei dati."
coverCaption: ""
---

## Introduzione:

I computer sono diventati un aspetto cruciale della nostra vita quotidiana e, di conseguenza, l'esigenza di sicurezza dei dati è cresciuta in modo sostanziale. Tra i vari metodi utilizzati per proteggere i dati in transito, SSL (Secure Socket Layer) e TLS (Transport Layer Security) sono protocolli ampiamente utilizzati. Tuttavia, con l'evolversi della tecnologia, le versioni più vecchie di questi protocolli stanno diventando vulnerabili agli attacchi informatici. In questo articolo, discuteremo i passaggi per rendere più sicuri i computer disabilitando SSL e tutte le versioni di TLS 1.2 e successive per mantenere i dati al sicuro.

### Perché disabilitare SSL e TLS 1.2 e inferiori?

Le vecchie versioni di SSL e TLS sono vulnerabili a diverse minacce alla sicurezza come POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) e Heartbleed. Questi attacchi possono portare all'esposizione di informazioni sensibili, per cui è fondamentale disabilitare l'uso di protocolli obsoleti.

### Disabilitare SSL e TLS 1.2 e inferiori in Windows:

In Windows, il processo di disabilitazione di SSL e TLS 1.2 e inferiori può essere eseguito attraverso l'editor del registro di sistema. Ecco uno script powershell per eseguire l'operazione:

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

#### Disabilitare SSL e TLS 1.2 e inferiori in Linux:

In Linux, il processo di disabilitazione di SSL e TLS 1.2 e inferiori può essere realizzato modificando il file di configurazione di OpenSSL. Ecco i passi da seguire:

1. Aprite il terminale e accedete come root.
2. Andare al file di configurazione di OpenSSL. In genere si trova in /etc/ssl/openssl.cnf.
3. Aprire il file con un editor di testo come nano o vim.
4. Individuare la direttiva SSLProtocol e impostarne il valore su -TLSv1.2.
5. Salvare il file e chiudere l'editor di testo.
6. Riavviare i servizi che utilizzano OpenSSL, come Apache o Nginx, affinché le modifiche abbiano effetto.

## Conclusione:

Disabilitando SSL e tutte le versioni TLS 1.2 e inferiori, è possibile rafforzare la sicurezza del computer e proteggere le informazioni sensibili da potenziali minacce informatiche. Si tratta di un processo semplice che può essere portato a termine con il minimo sforzo e che rappresenta un aspetto fondamentale per mantenere la sicurezza del computer. Attuando i passaggi descritti in questo articolo, è possibile mantenere i dati al sicuro e prevenire gli attacchi informatici, riducendo così il rischio di esposizione di informazioni sensibili.

È importante notare che la disattivazione di queste vecchie versioni dei protocolli SSL e TLS può migliorare la sicurezza del computer, ma può anche influire sulla compatibilità con alcuni vecchi sistemi. Pertanto, è essenziale testare a fondo le modifiche apportate e assicurarsi che non vi siano impatti negativi sul sistema prima di implementarle completamente.

In conclusione, la protezione del computer mediante la disattivazione di SSL e di tutte le versioni di TLS 1.2 e inferiori è un passo fondamentale per mantenere la sicurezza delle informazioni sensibili e prevenire gli attacchi informatici. I passaggi descritti in questo articolo forniscono una guida semplice per la protezione del computer, facilitando l'implementazione delle misure di sicurezza necessarie da parte di privati e organizzazioni.