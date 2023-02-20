---
title: "Hardening Your Computer's Security by Disabling SSL and TLS 1.2 and Below"
date: 2023-02-08
toc: true
draft: false
description: "This article discusses the steps to improve data security by disabling older versions of SSL and TLS protocols, which are vulnerable to cyber threats such as POODLE, BEAST, and Heartbleed, in Windows and Linux systems."
tags: ["Hardening computer security", "Disabling SSL and TLS", "Data security", "POODLE", "BEAST", "Heartbleed", "Windows registry editor", "Linux OpenSSL configuration", "Apache", "Nginx"]
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.png"
coverAlt: "A computer with a padlock symbol representing data security"
coverCaption: ""
---

## Introduction:

Computers have become a crucial aspect of our daily lives, and with that, the need for data security has grown substantially. Among the various methods used to secure data in transit, SSL (Secure Socket Layer) and TLS (Transport Layer Security) are widely used protocols. However, as technology evolves, older versions of these protocols are becoming vulnerable to cyber-attacks. In this article, we will discuss the steps to harden computers by disabling SSL and all TLS versions 1.2 and below to keep the data secure.

### Why disable SSL and TLS 1.2 and below?

Older versions of SSL and TLS are vulnerable to several security threats such as POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS), and Heartbleed. These attacks can lead to the exposure of sensitive information, making it crucial to disable the use of outdated protocols.

### Disabling SSL and TLS 1.2 and below in Windows:

In Windows, the process of disabling SSL and TLS 1.2 and below can be achieved through the registry editor. Here is a powershell script to accomplish the task:

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

#### Disabling SSL and TLS 1.2 and below in Linux:

In Linux, the process of disabling SSL and TLS 1.2 and below can be achieved through modifying the OpenSSL configuration file. Here are the steps to follow:

1. Open the terminal and log in as root.
2. Navigate to the OpenSSL configuration file. Typically, it is located at /etc/ssl/openssl.cnf.
3. Open the file using a text editor such as nano or vim.
4. Locate the SSLProtocol directive and set its value to -TLSv1.2.
5. Save the file and close the text editor.
6. Restart the services that use OpenSSL, such as Apache or Nginx, for the changes to take effect.

## Conclusion:

By disabling SSL and all TLS versions 1.2 and below, you can harden the security of your computer and protect sensitive information from potential cyber threats. It is a simple process that can be accomplished with minimal effort, making it a critical aspect of maintaining the security of your computer. By implementing the steps outlined in this article, you can keep your data secure and prevent cyber attacks, thereby reducing the risk of sensitive information being exposed.

It's important to note that while disabling these older versions of SSL and TLS protocols can improve the security of your computer, it can also impact the compatibility with some older systems. Therefore, it's essential to thoroughly test the changes made and ensure that there are no adverse impacts on your system before fully implementing them.

In conclusion, hardening your computer by disabling SSL and all TLS versions 1.2 and below is a critical step in maintaining the security of sensitive information and preventing cyber attacks. The steps outlined in this article provide a straightforward guide to securing your computer, making it easy for individuals and organizations to implement the necessary security measures.