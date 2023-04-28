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
 ## Introduction:  Les ordinateurs sont devenus un aspect crucial de notre vie quotidienne, et avec cela, le besoin de sécurité des données a considérablement augmenté. Parmi les différentes méthodes utilisées pour sécuriser les données en transit, SSL (Secure Socket Layer) et TLS (Transport Layer Security) sont des protocoles largement utilisés. Cependant, à mesure que la technologie évolue, les anciennes versions de ces protocoles deviennent vulnérables aux cyberattaques. Dans cet article, nous discuterons des étapes à suivre pour réactiver les ordinateurs en désactivant SSL et toutes les versions TLS 1.2 et inférieures pour assurer la sécurité des données.  ### Pourquoi désactiver SSL et TLS 1.2 et inférieur ?  Les anciennes versions de SSL et TLS sont vulnérables à plusieurs menaces de sécurité telles que POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) et Heartbleed. Ces attaques peuvent conduire à l'exposition d'informations sensibles, ce qui rend crucial de désactiver l'utilisation de protocoles obsolètes.  ### Désactivation de SSL et TLS 1.2 et inférieur sous Windows :  Sous Windows, le processus de désactivation de SSL et TLS 1.2 et inférieur peut être réalisé via l'éditeur de registre. Voici un script powershell pour accomplir la tâche :   #### Désactivation de SSL et TLS 1.2 et inférieur sous Linux :  Sous Linux, le processus de désactivation de SSL et TLS 1.2 et inférieur peut être réalisé en modifiant le fichier de configuration OpenSSL. Voici les étapes à suivre :  1. Ouvrez le terminal et connectez-vous en tant que root. 2. Accédez au fichier de configuration OpenSSL. En règle générale, il se trouve dans /etc/ssl/openssl.cnf. 3. Ouvrez le fichier à l'aide d'un éditeur de texte tel que nano ou vim. 4. Localisez la directive SSLProtocol et définissez sa valeur sur -TLSv1.2. 5. Enregistrez le fichier et fermez l'éditeur de texte. 6. Redémarrez les services qui utilisent OpenSSL, tels qu'Apache ou Nginx, pour que les modifications prennent effet.  ## Conclusion:  En désactivant SSL et toutes les versions 1.2 et inférieures de TLS, vous pouvez renforcer la sécurité de votre ordinateur et protéger les informations sensibles contre les cybermenaces potentielles. Il s'agit d'un processus simple qui peut être accompli avec un minimum d'effort, ce qui en fait un aspect essentiel du maintien de la sécurité de votre ordinateur. En mettant en œuvre les étapes décrites dans cet article, vous pouvez sécuriser vos données et prévenir les cyberattaques, réduisant ainsi le risque d'exposition d'informations sensibles.  Il est important de noter que si la désactivation de ces anciennes versions des protocoles SSL et TLS peut améliorer la sécurité de votre ordinateur, cela peut également avoir un impact sur la compatibilité avec certains systèmes plus anciens. Par conséquent, il est essentiel de tester minutieusement les modifications apportées et de s'assurer qu'il n'y a pas d'impact négatif sur votre système avant de les mettre en œuvre complètement.  En conclusion, renforcer votre ordinateur en désactivant SSL et toutes les versions 1.2 et inférieures de TLS est une étape critique pour maintenir la sécurité des informations sensibles et prévenir les cyberattaques. Les étapes décrites dans cet article fournissent un guide simple pour sécuriser votre ordinateur, ce qui permet aux particuliers et aux organisations de mettre en œuvre facilement les mesures de sécurité nécessaires.