---
title: "Hardening Your Computer's Security by Disabling SSL and TLS 1.1 and Below"
date: 2023-02-08
lastmod: 2026-10-10
toc: true
draft: false
description: "This article explains how to retire SSL and older TLS versions while keeping TLS 1.2 or newer available for modern clients and servers. It covers Windows Schannel, .NET, and Linux service configuration."
tags: ["Hardening computer security", "Disabling SSL and TLS", "Data security", "POODLE", "BEAST", "Heartbleed", "Windows registry editor", "Linux OpenSSL configuration", "Apache", "Nginx"]
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.webp"
coverAlt: "A computer with a padlock symbol representing data security"
coverCaption: ""
---

## Introduction:

Computers have become a crucial aspect of our daily lives, and with that, the need for data security has grown substantially. Among the various methods used to secure data in transit, SSL (Secure Socket Layer) and TLS (Transport Layer Security) are widely used protocols. However, as technology evolves, older versions of these protocols are becoming vulnerable to cyber-attacks. This article explains how to retire SSL and TLS 1.0 and 1.1 while keeping TLS 1.2 or TLS 1.3 available.

*TLS 1.2 is not an obsolete protocol. The current baseline is TLS 1.2 or newer. TLS 1.3 is defined by [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446), while [RFC 8996](https://www.rfc-editor.org/rfc/rfc8996) formally deprecates TLS 1.0 and TLS 1.1.*

### Why disable SSL and TLS 1.1 and below?

Older versions of SSL and TLS are vulnerable to several security threats such as POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS), and Heartbleed. These attacks can lead to the exposure of sensitive information, making it crucial to disable the use of outdated protocols. Heartbleed affected vulnerable OpenSSL implementations rather than serving as a protocol version by itself. Patch the library and rotate exposed credentials as part of remediation.

Microsoft's current [Schannel registry guidance](https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings) lists protocol settings for supported Windows releases. Microsoft recommends Group Policy or other supported management tools where available, with direct registry editing reserved for cases without a better control.

### Disabling SSL and TLS 1.1 and below in Windows:

In Windows, the process of disabling SSL and TLS 1.1 and below can be achieved through the registry editor. Here is a PowerShell script to accomplish the task. The script also sets .NET to use operating-system TLS defaults and strong cryptography.

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

#### Disabling SSL and TLS 1.1 and below in Linux:

In Linux, the process of disabling SSL and TLS 1.1 and below depends on the application and library. Modifying `/etc/ssl/openssl.cnf` does not override every daemon or bundled TLS library. Here are the steps to follow:

1. Open the terminal and log in as root.
2. Navigate to the OpenSSL configuration file. Typically, it is located at /etc/ssl/openssl.cnf.
3. Open the file using a text editor such as nano or vim.
4. Locate the service's protocol directive and set the minimum to TLS 1.2. The old `-TLSv1.2` instruction would disable TLS 1.2, so do not use it as a modern baseline.
5. Save the file and close the text editor.
6. Restart the services that use OpenSSL, such as Apache or Nginx, for the changes to take effect.

## Conclusion:

By disabling SSL and TLS versions 1.1 and below, you harden the security of your computer while keeping modern TLS clients compatible. The exact setting belongs to the service that negotiates TLS, so test each application rather than assuming one OpenSSL file controls every daemon.

Note that while disabling these older versions of SSL and TLS protocols can improve the security of your computer, it can also impact the compatibility with some older systems. Therefore, you need to thoroughly test the changes made and ensure that there are no adverse impacts on your system before fully implementing them.

Wrapping up, hardening your computer by disabling SSL and TLS versions 1.1 and below is a critical step in maintaining the security of sensitive information and preventing cyber attacks. The steps outlined in this article provide a straightforward guide to securing your computer, making it easy for individuals and organizations to implement the necessary security measures.

## Current Validation Checklist

- **Confirm the negotiated protocol.** Test the client and server with a TLS scanner or an approved internal test from both sides of the connection.
- **Keep TLS 1.2 enabled.** Some older applications still require it, while TLS 1.3 support depends on the operating system and library.
- **Review DTLS separately.** RFC 8996 deprecates DTLS 1.0. It does not define a DTLS 1.1 protocol.
- **Restart affected services.** Schannel and application settings often require a service or system restart before the new policy applies.
- **Record exceptions.** Document any legacy endpoint that still needs a temporary compatibility setting and assign a retirement date.
