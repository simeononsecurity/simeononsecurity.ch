---
title: "Renforcer la sécurité de votre ordinateur en désactivant SSL et TLS 1.2 et moins"
date: 2023-02-08
toc: true
draft: false
description: "Cet article présente les étapes à suivre pour améliorer la sécurité des données en désactivant les anciennes versions des protocoles SSL et TLS, qui sont vulnérables aux cyber-menaces telles que POODLE, BEAST et Heartbleed, dans les systèmes Windows et Linux."
tags: ["Renforcement de la sécurité informatique", "Désactivation de SSL et TLS", "Sécurité des données", "POODLE", "BÊTE", "Heartbleed", "Editeur de registre Windows", "Linux OpenSSL configuration", "Apache", "Nginx"]
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.png"
coverAlt: "Un ordinateur avec un symbole de cadenas représentant la sécurité des données"
coverCaption: ""
---

## Introduction :

Les ordinateurs sont devenus un aspect crucial de notre vie quotidienne, et avec eux, le besoin de sécurité des données s'est considérablement accru. Parmi les différentes méthodes utilisées pour sécuriser les données en transit, SSL (Secure Socket Layer) et TLS (Transport Layer Security) sont des protocoles largement utilisés. Cependant, avec l'évolution de la technologie, les anciennes versions de ces protocoles deviennent vulnérables aux cyber-attaques. Dans cet article, nous examinerons les étapes à suivre pour renforcer les ordinateurs en désactivant le protocole SSL et toutes les versions TLS 1.2 et inférieures afin de préserver la sécurité des données.

### Pourquoi désactiver SSL et TLS 1.2 et moins ?

Les anciennes versions de SSL et TLS sont vulnérables à plusieurs menaces de sécurité telles que POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) et Heartbleed. Ces attaques peuvent entraîner l'exposition d'informations sensibles, d'où l'importance de désactiver l'utilisation de protocoles obsolètes.

### Désactivation de SSL et TLS 1.2 et inférieurs dans Windows :

Dans Windows, le processus de désactivation de SSL et TLS 1.2 et inférieurs peut être réalisé par l'intermédiaire de l'éditeur de registre. Voici un script powershell pour accomplir cette tâche :

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

#### Désactivation de SSL et TLS 1.2 et moins sous Linux :

Sous Linux, le processus de désactivation de SSL et TLS 1.2 et inférieurs peut être réalisé en modifiant le fichier de configuration d'OpenSSL. Voici les étapes à suivre :

1. Ouvrez le terminal et connectez-vous en tant que root.
2. Naviguez jusqu'au fichier de configuration OpenSSL. En général, il est situé dans /etc/ssl/openssl.cnf.
3. Ouvrez le fichier à l'aide d'un éditeur de texte tel que nano ou vim.
4. Localisez la directive SSLProtocol et définissez sa valeur à -TLSv1.2.
5. Enregistrez le fichier et fermez l'éditeur de texte.
6. Redémarrez les services qui utilisent OpenSSL, comme Apache ou Nginx, pour que les modifications soient prises en compte.

## Conclusion :

En désactivant SSL et toutes les versions TLS 1.2 et inférieures, vous pouvez renforcer la sécurité de votre ordinateur et protéger les informations sensibles contre les cybermenaces potentielles. Il s'agit d'un processus simple qui peut être réalisé avec un minimum d'effort, ce qui en fait un aspect essentiel du maintien de la sécurité de votre ordinateur. En mettant en œuvre les étapes décrites dans cet article, vous pouvez sécuriser vos données et prévenir les cyberattaques, réduisant ainsi le risque d'exposition des informations sensibles.

Il est important de noter que si la désactivation de ces anciennes versions des protocoles SSL et TLS peut améliorer la sécurité de votre ordinateur, elle peut également avoir une incidence sur la compatibilité avec certains systèmes plus anciens. Il est donc essentiel de tester minutieusement les modifications apportées et de s'assurer qu'elles n'ont pas d'impact négatif sur votre système avant de les mettre en œuvre.

En conclusion, le durcissement de votre ordinateur par la désactivation du protocole SSL et de toutes les versions TLS 1.2 et inférieures est une étape essentielle dans le maintien de la sécurité des informations sensibles et la prévention des cyberattaques. Les étapes décrites dans cet article constituent un guide simple pour sécuriser votre ordinateur, ce qui permet aux particuliers et aux organisations de mettre en œuvre facilement les mesures de sécurité nécessaires.