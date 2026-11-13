---
title: "Rafforza la sicurezza del computer disattivando SSL e TLS 1.1 e versioni precedenti"
date: 2023-02-08
lastmod: 2026-11-13
toc: true
draft: false
description: "Disattiva SSL e le vecchie versioni di TLS mantenendo TLS 1.2 o successivo. La guida tratta Schannel e .NET su Windows e i servizi Linux."
tags: ['Rafforzamento della sicurezza del computer', 'Disattivazione di SSL e TLS', 'Sicurezza dei dati', 'POODLE', 'BEAST', 'Heartbleed', 'Editor del Registro di Windows', 'Configurazione OpenSSL su Linux', 'Apache', 'Nginx']
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.webp"
coverAlt: "Un computer con un lucchetto che rappresenta la sicurezza dei dati"
coverCaption: ""
---

## Introduzione:

I computer sono diventati una parte essenziale della vita quotidiana e, con loro, è cresciuta la necessità di proteggere i dati. SSL (Secure Socket Layer) e TLS (Transport Layer Security) proteggono i dati in transito. Le versioni precedenti sono ormai vulnerabili agli attacchi. Questo articolo spiega come disattivare SSL e TLS 1.0 e 1.1 mantenendo disponibili TLS 1.2 o TLS 1.3.

*TLS 1.2 non è un protocollo obsoleto. Il livello minimo attuale è TLS 1.2 o successivo. [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) definisce TLS 1.3, mentre [RFC 8996](https://www.rfc-editor.org/rfc/rfc8996) depreca formalmente TLS 1.0 e TLS 1.1.*

### Perché disattivare SSL e TLS 1.1 e versioni precedenti?

Le vecchie versioni di SSL e TLS sono vulnerabili a minacce come POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) e Heartbleed. Questi attacchi possono esporre informazioni riservate. Heartbleed ha colpito implementazioni vulnerabili di OpenSSL, ma non era una versione del protocollo. Applica la patch alla libreria e cambia le credenziali esposte.

Le attuali [indicazioni Microsoft sul Registro Schannel](https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings) elencano le impostazioni dei protocolli per le versioni Windows supportate. Microsoft consiglia Criteri di gruppo o altri strumenti di gestione supportati, se disponibili. Modifica direttamente il Registro solo quando non esiste un controllo migliore.

### Disattivare SSL e TLS 1.1 e versioni precedenti in Windows:

In Windows, puoi disattivare questi protocolli tramite il Registro. Lo script PowerShell seguente modifica le impostazioni Schannel per client e server. Configura anche .NET per usare le impostazioni TLS predefinite del sistema operativo e una crittografia robusta.

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

#### Disattivare SSL e TLS 1.1 e versioni precedenti in Linux:

In Linux, il metodo per disattivare i vecchi protocolli dipende dall’applicazione e dalla libreria. Modificare `/etc/ssl/openssl.cnf` non sovrascrive le impostazioni di ogni daemon o delle librerie TLS incluse. Segui questi passaggi:

1. Apri il terminale e accedi come root.
2. Apri il file di configurazione di OpenSSL, di solito in /etc/ssl/openssl.cnf.
3. Apri il file con un editor di testo come nano o vim.
4. Trova la direttiva del protocollo del servizio e imposta TLS 1.2 come versione minima. La vecchia istruzione `-TLSv1.2` disattivava TLS 1.2, quindi non usarla come minimo moderno.
5. Salva il file e chiudi l’editor.
6. Riavvia i servizi che usano OpenSSL, come Apache o Nginx, per applicare le modifiche.

## Conclusione:

Disattivare SSL e TLS 1.1 e versioni precedenti rafforza la sicurezza del computer e mantiene la compatibilità con i client TLS moderni. L’impostazione corretta appartiene al servizio che negozia la connessione TLS. Prova ogni applicazione, senza presumere che un solo file OpenSSL controlli tutti i daemon.

Disattivare queste versioni obsolete può influire sulla compatibilità con alcuni sistemi meno recenti. Prova attentamente le modifiche e verifica che non causino effetti negativi prima di applicarle del tutto.

Proteggi le informazioni sensibili e riduci il rischio di attacchi. Verifica il protocollo negoziato da ogni servizio e documenta le eccezioni temporanee.

## Elenco di verifica attuale

- **Verifica il protocollo negoziato.** Prova client e server con uno scanner TLS o un test interno approvato da entrambe le estremità della connessione.
- **Mantieni attivo TLS 1.2.** Alcune applicazioni meno recenti ne hanno ancora bisogno. Il supporto per TLS 1.3 dipende dal sistema operativo e dalla libreria.
- **Esamina DTLS separatamente.** RFC 8996 depreca DTLS 1.0 e non definisce un protocollo DTLS 1.1.
- **Riavvia i servizi interessati.** Le impostazioni Schannel e delle applicazioni spesso richiedono il riavvio del servizio o del sistema.
- **Documenta le eccezioni.** Registra ogni endpoint legacy che necessita temporaneamente di un’impostazione di compatibilità e assegna una data di ritiro.
