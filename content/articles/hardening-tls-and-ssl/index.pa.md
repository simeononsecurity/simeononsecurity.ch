---
title: "SSL ਅਤੇ TLS 1.1 ਅਤੇ ਇਸ ਤੋਂ ਪੁਰਾਣੇ ਸੰਸਕਰਣ ਬੰਦ ਕਰਕੇ ਕੰਪਿਊਟਰ ਦੀ ਸੁਰੱਖਿਆ ਮਜ਼ਬੂਤ ਕਰੋ"
date: 2023-02-08
lastmod: 2026-11-13
toc: true
draft: false
description: "TLS 1.2 ਜਾਂ ਨਵਾਂ ਸੰਸਕਰਣ ਚਾਲੂ ਰੱਖਦਿਆਂ SSL ਅਤੇ ਪੁਰਾਣੇ TLS ਸੰਸਕਰਣ ਬੰਦ ਕਰੋ। ਇਸ ਵਿੱਚ Windows Schannel, .NET ਅਤੇ Linux ਸੇਵਾਵਾਂ ਸ਼ਾਮਲ ਹਨ।"
tags: ['ਕੰਪਿਊਟਰ ਸੁਰੱਖਿਆ ਮਜ਼ਬੂਤ ਕਰਨਾ', 'SSL ਅਤੇ TLS ਬੰਦ ਕਰਨਾ', 'ਡਾਟਾ ਸੁਰੱਖਿਆ', 'POODLE', 'BEAST', 'Heartbleed', 'Windows ਰਜਿਸਟਰੀ ਸੰਪਾਦਕ', 'Linux OpenSSL ਸੰਰਚਨਾ', 'Apache', 'Nginx']
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.webp"
coverAlt: "ਡਾਟਾ ਸੁਰੱਖਿਆ ਦਰਸਾਉਂਦੇ ਤਾਲੇ ਦੇ ਚਿੰਨ੍ਹ ਵਾਲਾ ਕੰਪਿਊਟਰ"
coverCaption: ""
---

## ਜਾਣ-ਪਛਾਣ:

ਕੰਪਿਊਟਰ ਸਾਡੀ ਰੋਜ਼ਾਨਾ ਜ਼ਿੰਦਗੀ ਦਾ ਅਹਿਮ ਹਿੱਸਾ ਬਣ ਗਏ ਹਨ, ਇਸ ਲਈ ਡਾਟਾ ਸੁਰੱਖਿਆ ਦੀ ਲੋੜ ਵੀ ਵਧੀ ਹੈ। ਆਵਾਜਾਈ ਦੌਰਾਨ ਡਾਟੇ ਦੀ ਰੱਖਿਆ ਲਈ SSL (Secure Socket Layer) ਅਤੇ TLS (Transport Layer Security) ਪ੍ਰੋਟੋਕੋਲ ਵਿਆਪਕ ਤੌਰ ’ਤੇ ਵਰਤੇ ਜਾਂਦੇ ਹਨ। ਤਕਨਾਲੋਜੀ ਦੇ ਵਿਕਾਸ ਨਾਲ ਇਨ੍ਹਾਂ ਦੇ ਪੁਰਾਣੇ ਸੰਸਕਰਣ ਸਾਈਬਰ ਹਮਲਿਆਂ ਲਈ ਕਮਜ਼ੋਰ ਹੋ ਗਏ ਹਨ। ਇਹ ਲੇਖ ਦੱਸਦਾ ਹੈ ਕਿ TLS 1.2 ਜਾਂ TLS 1.3 ਉਪਲਬਧ ਰੱਖਦਿਆਂ SSL ਅਤੇ TLS 1.0 ਤੇ 1.1 ਨੂੰ ਕਿਵੇਂ ਬੰਦ ਕਰਨਾ ਹੈ।

*TLS 1.2 ਪੁਰਾਣਾ ਪ੍ਰੋਟੋਕੋਲ ਨਹੀਂ ਹੈ। ਮੌਜੂਦਾ ਘੱਟੋ-ਘੱਟ ਮਿਆਰ TLS 1.2 ਜਾਂ ਨਵਾਂ ਹੈ। [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) TLS 1.3 ਦੀ ਪਰਿਭਾਸ਼ਾ ਦਿੰਦਾ ਹੈ, ਜਦਕਿ [RFC 8996](https://www.rfc-editor.org/rfc/rfc8996) TLS 1.0 ਅਤੇ TLS 1.1 ਨੂੰ ਰਸਮੀ ਤੌਰ ’ਤੇ ਅਪ੍ਰਚਲਿਤ ਕਰਦਾ ਹੈ।*

### SSL ਅਤੇ TLS 1.1 ਅਤੇ ਇਸ ਤੋਂ ਪੁਰਾਣੇ ਸੰਸਕਰਣ ਕਿਉਂ ਬੰਦ ਕਰਨੇ?

SSL ਅਤੇ TLS ਦੇ ਪੁਰਾਣੇ ਸੰਸਕਰਣ POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) ਅਤੇ Heartbleed ਵਰਗੇ ਸੁਰੱਖਿਆ ਖਤਰਿਆਂ ਲਈ ਕਮਜ਼ੋਰ ਹਨ। ਇਨ੍ਹਾਂ ਹਮਲਿਆਂ ਨਾਲ ਸੰਵੇਦਨਸ਼ੀਲ ਜਾਣਕਾਰੀ ਸਾਹਮਣੇ ਆ ਸਕਦੀ ਹੈ, ਇਸ ਲਈ ਪੁਰਾਣੇ ਪ੍ਰੋਟੋਕੋਲ ਬੰਦ ਕਰਨਾ ਜ਼ਰੂਰੀ ਹੈ। Heartbleed ਖੁਦ ਪ੍ਰੋਟੋਕੋਲ ਸੰਸਕਰਣ ਨਹੀਂ ਸੀ, ਸਗੋਂ ਇਸ ਨੇ OpenSSL ਦੇ ਕਮਜ਼ੋਰ ਲਾਗੂਕਰਨਾਂ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕੀਤਾ ਸੀ। ਲਾਇਬ੍ਰੇਰੀ ਨੂੰ ਪੈਚ ਕਰੋ ਅਤੇ ਸਾਹਮਣੇ ਆਏ ਹੋ ਸਕਦੇ ਪ੍ਰਮਾਣ-ਪੱਤਰ ਬਦਲੋ।

Microsoft ਦੀ ਮੌਜੂਦਾ [Schannel ਰਜਿਸਟਰੀ ਹਦਾਇਤ](https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings) ਸਮਰਥਿਤ Windows ਰਿਲੀਜ਼ਾਂ ਲਈ ਪ੍ਰੋਟੋਕੋਲ ਸੈਟਿੰਗਾਂ ਦਿੰਦੀ ਹੈ। ਜਿੱਥੇ ਉਪਲਬਧ ਹੋਵੇ, Microsoft Group Policy ਜਾਂ ਹੋਰ ਸਮਰਥਿਤ ਪ੍ਰਬੰਧਨ ਸਾਧਨਾਂ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕਰਦਾ ਹੈ। ਸਿੱਧੀ ਰਜਿਸਟਰੀ ਸੋਧ ਸਿਰਫ਼ ਉਦੋਂ ਕਰੋ ਜਦੋਂ ਵਧੀਆ ਨਿਯੰਤਰਣ ਉਪਲਬਧ ਨਾ ਹੋਵੇ।

### Windows ਵਿੱਚ SSL ਅਤੇ TLS 1.1 ਅਤੇ ਇਸ ਤੋਂ ਪੁਰਾਣੇ ਸੰਸਕਰਣ ਬੰਦ ਕਰਨਾ:

Windows ਵਿੱਚ ਰਜਿਸਟਰੀ ਸੰਪਾਦਕ ਰਾਹੀਂ SSL ਅਤੇ TLS 1.1 ਅਤੇ ਇਸ ਤੋਂ ਪੁਰਾਣੇ ਸੰਸਕਰਣ ਬੰਦ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ। ਹੇਠਾਂ ਦਿੱਤੀ PowerShell ਸਕ੍ਰਿਪਟ Schannel ਦੀਆਂ ਕਲਾਇੰਟ ਅਤੇ ਸਰਵਰ ਸੈਟਿੰਗਾਂ ਬਦਲਦੀ ਹੈ। ਇਹ .NET ਨੂੰ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਦੇ TLS ਡਿਫ਼ਾਲਟ ਅਤੇ ਮਜ਼ਬੂਤ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫੀ ਵਰਤਣ ਲਈ ਵੀ ਸੈੱਟ ਕਰਦੀ ਹੈ।

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

#### Linux ਵਿੱਚ SSL ਅਤੇ TLS 1.1 ਅਤੇ ਇਸ ਤੋਂ ਪੁਰਾਣੇ ਸੰਸਕਰਣ ਬੰਦ ਕਰਨਾ:

Linux ਵਿੱਚ ਪੁਰਾਣੇ ਪ੍ਰੋਟੋਕੋਲ ਬੰਦ ਕਰਨ ਦਾ ਤਰੀਕਾ ਐਪਲੀਕੇਸ਼ਨ ਅਤੇ ਲਾਇਬ੍ਰੇਰੀ ’ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ। `/etc/ssl/openssl.cnf` ਸੋਧਣ ਨਾਲ ਹਰ ਡੈਮਨ ਜਾਂ ਬੰਡਲ ਕੀਤੀ TLS ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਸੈਟਿੰਗ ਨਹੀਂ ਬਦਲਦੀ। ਇਹ ਕਦਮ ਅਪਣਾਓ:

1. ਟਰਮੀਨਲ ਖੋਲ੍ਹੋ ਅਤੇ root ਵਜੋਂ ਲੌਗ ਇਨ ਕਰੋ।
2. OpenSSL ਸੰਰਚਨਾ ਫ਼ਾਈਲ ’ਤੇ ਜਾਓ। ਇਹ ਆਮ ਤੌਰ ’ਤੇ /etc/ssl/openssl.cnf ਵਿੱਚ ਹੁੰਦੀ ਹੈ।
3. ਫ਼ਾਈਲ ਨੂੰ nano ਜਾਂ vim ਵਰਗੇ ਟੈਕਸਟ ਸੰਪਾਦਕ ਨਾਲ ਖੋਲ੍ਹੋ।
4. ਸੇਵਾ ਦਾ ਪ੍ਰੋਟੋਕੋਲ ਨਿਰਦੇਸ਼ ਲੱਭੋ ਅਤੇ ਘੱਟੋ-ਘੱਟ ਸੰਸਕਰਣ TLS 1.2 ਰੱਖੋ। ਪੁਰਾਣੀ `-TLSv1.2` ਹਦਾਇਤ TLS 1.2 ਨੂੰ ਬੰਦ ਕਰਦੀ ਸੀ, ਇਸ ਲਈ ਇਸ ਨੂੰ ਆਧੁਨਿਕ ਘੱਟੋ-ਘੱਟ ਮਿਆਰ ਵਜੋਂ ਨਾ ਵਰਤੋ।
5. ਫ਼ਾਈਲ ਸੰਭਾਲੋ ਅਤੇ ਟੈਕਸਟ ਸੰਪਾਦਕ ਬੰਦ ਕਰੋ।
6. ਤਬਦੀਲੀਆਂ ਲਾਗੂ ਕਰਨ ਲਈ OpenSSL ਵਰਤਣ ਵਾਲੀਆਂ ਸੇਵਾਵਾਂ, ਜਿਵੇਂ Apache ਜਾਂ Nginx, ਮੁੜ ਚਾਲੂ ਕਰੋ।

## ਸਿੱਟਾ:

SSL ਅਤੇ TLS 1.1 ਅਤੇ ਇਸ ਤੋਂ ਪੁਰਾਣੇ ਸੰਸਕਰਣ ਬੰਦ ਕਰਨ ਨਾਲ ਆਧੁਨਿਕ TLS ਕਲਾਇੰਟਾਂ ਨਾਲ ਅਨੁਕੂਲਤਾ ਰੱਖਦਿਆਂ ਕੰਪਿਊਟਰ ਦੀ ਸੁਰੱਖਿਆ ਮਜ਼ਬੂਤ ਹੁੰਦੀ ਹੈ। ਸਹੀ ਸੈਟਿੰਗ ਉਸ ਸੇਵਾ ਵਿੱਚ ਹੁੰਦੀ ਹੈ ਜੋ TLS ਕੁਨੈਕਸ਼ਨ ’ਤੇ ਗੱਲਬਾਤ ਕਰਦੀ ਹੈ। ਹਰ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਜਾਂਚ ਕਰੋ, ਇਹ ਨਾ ਮੰਨੋ ਕਿ ਇੱਕ OpenSSL ਫ਼ਾਈਲ ਸਾਰੇ ਡੈਮਨ ਚਲਾਉਂਦੀ ਹੈ।

ਇਨ੍ਹਾਂ ਪੁਰਾਣੇ ਸੰਸਕਰਣਾਂ ਨੂੰ ਬੰਦ ਕਰਨ ਨਾਲ ਕੁਝ ਪੁਰਾਣੇ ਸਿਸਟਮਾਂ ਦੀ ਅਨੁਕੂਲਤਾ ਪ੍ਰਭਾਵਿਤ ਹੋ ਸਕਦੀ ਹੈ। ਪੂਰੀ ਤਰ੍ਹਾਂ ਲਾਗੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਤਬਦੀਲੀਆਂ ਚੰਗੀ ਤਰ੍ਹਾਂ ਜਾਂਚੋ ਅਤੇ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਿਸਟਮ ’ਤੇ ਮਾੜਾ ਅਸਰ ਨਹੀਂ ਪੈਂਦਾ।

ਸੰਵੇਦਨਸ਼ੀਲ ਜਾਣਕਾਰੀ ਦੀ ਰੱਖਿਆ ਅਤੇ ਹਮਲਿਆਂ ਦਾ ਖਤਰਾ ਘਟਾਉਣ ਲਈ ਇਸ ਲੇਖ ਦੇ ਕਦਮ ਅਪਣਾਓ। ਪਹਿਲਾਂ ਪਤਾ ਕਰੋ ਕਿ ਹਰ ਸੇਵਾ ਕਿਹੜਾ ਪ੍ਰੋਟੋਕੋਲ ਵਰਤਦੀ ਹੈ, ਫਿਰ ਅਸਥਾਈ ਛੋਟਾਂ ਦਰਜ ਕਰੋ।

## ਮੌਜੂਦਾ ਜਾਂਚ ਸੂਚੀ

- **ਗੱਲਬਾਤ ਵਿੱਚ ਚੁਣਿਆ ਪ੍ਰੋਟੋਕੋਲ ਪੁਸ਼ਟੀ ਕਰੋ।** TLS ਸਕੈਨਰ ਜਾਂ ਮਨਜ਼ੂਰਸ਼ੁਦਾ ਅੰਦਰੂਨੀ ਜਾਂਚ ਰਾਹੀਂ ਕੁਨੈਕਸ਼ਨ ਦੇ ਦੋਵੇਂ ਸਿਰਿਆਂ ’ਤੇ ਕਲਾਇੰਟ ਅਤੇ ਸਰਵਰ ਪਰਖੋ।
- **TLS 1.2 ਚਾਲੂ ਰੱਖੋ।** ਕੁਝ ਪੁਰਾਣੀਆਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਅਜੇ ਵੀ ਇਸ ਦੀ ਲੋੜ ਹੈ, ਜਦਕਿ TLS 1.3 ਦਾ ਸਮਰਥਨ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਅਤੇ ਲਾਇਬ੍ਰੇਰੀ ’ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ।
- **DTLS ਦੀ ਵੱਖਰੇ ਤੌਰ ’ਤੇ ਸਮੀਖਿਆ ਕਰੋ।** RFC 8996 DTLS 1.0 ਨੂੰ ਅਪ੍ਰਚਲਿਤ ਕਰਦਾ ਹੈ। ਇਹ DTLS 1.1 ਪ੍ਰੋਟੋਕੋਲ ਪਰਿਭਾਸ਼ਿਤ ਨਹੀਂ ਕਰਦਾ।
- **ਪ੍ਰਭਾਵਿਤ ਸੇਵਾਵਾਂ ਮੁੜ ਚਾਲੂ ਕਰੋ।** ਨਵੀਂ ਨੀਤੀ ਲਾਗੂ ਕਰਨ ਲਈ Schannel ਅਤੇ ਐਪਲੀਕੇਸ਼ਨ ਸੈਟਿੰਗਾਂ ਵਿੱਚ ਅਕਸਰ ਸੇਵਾ ਜਾਂ ਸਿਸਟਮ ਮੁੜ ਚਾਲੂ ਕਰਨਾ ਪੈਂਦਾ ਹੈ।
- **ਛੋਟਾਂ ਦਰਜ ਕਰੋ।** ਹਰ ਪੁਰਾਣੇ ਐਂਡਪੌਇੰਟ ਨੂੰ ਦਰਜ ਕਰੋ ਜਿਸ ਨੂੰ ਅਸਥਾਈ ਅਨੁਕੂਲਤਾ ਸੈਟਿੰਗ ਦੀ ਲੋੜ ਹੈ ਅਤੇ ਇਸ ਨੂੰ ਹਟਾਉਣ ਦੀ ਤਾਰੀਖ਼ ਦਿਓ।
