---
title: "Renforcez la sécurité de votre ordinateur en désactivant SSL et TLS 1.1 et les versions antérieures"
date: 2023-02-08
lastmod: 2026-11-13
toc: true
draft: false
description: "Désactivez SSL et les anciennes versions de TLS tout en conservant TLS 1.2 ou une version ultérieure. L’article couvre Schannel et .NET sous Windows ainsi que les services Linux."
tags: ['Renforcement de la sécurité informatique', 'Désactivation de SSL et TLS', 'Sécurité des données', 'POODLE', 'BEAST', 'Heartbleed', 'Éditeur du Registre Windows', 'Configuration OpenSSL sous Linux', 'Apache', 'Nginx']
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.webp"
coverAlt: "Un ordinateur avec un cadenas symbolisant la sécurité des données"
coverCaption: ""
---

## Introduction:

Les ordinateurs occupent une place essentielle dans notre quotidien, et le besoin de protéger les données a augmenté. SSL (Secure Socket Layer) et TLS (Transport Layer Security) protègent les données en transit. Leurs anciennes versions sont désormais vulnérables aux attaques. Cet article explique comment désactiver SSL et TLS 1.0 et 1.1 tout en conservant TLS 1.2 ou TLS 1.3.

*TLS 1.2 n’est pas un protocole obsolète. Le niveau minimal actuel est TLS 1.2 ou une version ultérieure. [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) définit TLS 1.3, tandis que [RFC 8996](https://www.rfc-editor.org/rfc/rfc8996) déprécie officiellement TLS 1.0 et TLS 1.1.*

### Pourquoi désactiver SSL et TLS 1.1 et les versions antérieures ?

Les anciennes versions de SSL et TLS sont vulnérables à des menaces telles que POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) et Heartbleed. Ces attaques peuvent exposer des informations sensibles. Heartbleed a touché des implémentations vulnérables d’OpenSSL, ce n’était pas une version du protocole. Appliquez le correctif de la bibliothèque et renouvelez les identifiants exposés.

Les [instructions Microsoft actuelles sur le Registre Schannel](https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings) répertorient les paramètres de protocole des versions Windows prises en charge. Microsoft recommande la stratégie de groupe ou d’autres outils de gestion pris en charge lorsqu’ils existent. Modifiez directement le Registre uniquement en l’absence d’un meilleur contrôle.

### Désactiver SSL et TLS 1.1 et les versions antérieures sous Windows :

Sous Windows, vous pouvez désactiver ces protocoles dans le Registre. Le script PowerShell ci-dessous modifie les paramètres Schannel du client et du serveur. Il configure aussi .NET pour utiliser les paramètres TLS par défaut du système et une cryptographie forte.

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

#### Désactiver SSL et TLS 1.1 et les versions antérieures sous Linux :

Sous Linux, la désactivation des anciens protocoles dépend de l’application et de la bibliothèque. Modifier `/etc/ssl/openssl.cnf` ne remplace pas les paramètres de chaque démon ni ceux des bibliothèques TLS intégrées. Suivez ces étapes :

1. Ouvrez le terminal et connectez-vous en tant que root.
2. Accédez au fichier de configuration OpenSSL. Il se trouve généralement dans /etc/ssl/openssl.cnf.
3. Ouvrez le fichier dans un éditeur de texte tel que nano ou vim.
4. Repérez la directive de protocole du service et définissez TLS 1.2 comme version minimale. L’ancienne instruction `-TLSv1.2` désactivait TLS 1.2. Ne l’utilisez pas comme minimum actuel.
5. Enregistrez le fichier et fermez l’éditeur.
6. Redémarrez les services qui utilisent OpenSSL, comme Apache ou Nginx, pour appliquer les changements.

## Conclusion :

Désactiver SSL et TLS 1.1 et les versions antérieures renforce la sécurité de l’ordinateur tout en préservant la compatibilité avec les clients TLS modernes. Le bon réglage appartient au service qui négocie la connexion TLS. Testez chaque application au lieu de supposer qu’un seul fichier OpenSSL contrôle tous les démons.

La désactivation de ces anciennes versions peut affecter la compatibilité avec certains systèmes anciens. Testez soigneusement les changements et vérifiez leurs effets avant de les appliquer partout.

Protégez les informations sensibles et réduisez le risque d’attaque. Vérifiez le protocole négocié par chaque service et consignez les exceptions temporaires.

## Liste de vérification actuelle

- **Vérifiez le protocole négocié.** Testez le client et le serveur avec un scanner TLS ou un test interne approuvé, aux deux extrémités de la connexion.
- **Laissez TLS 1.2 activé.** Certaines applications anciennes en ont encore besoin. La prise en charge de TLS 1.3 dépend du système d’exploitation et de la bibliothèque.
- **Vérifiez DTLS séparément.** La RFC 8996 déprécie DTLS 1.0. Elle ne définit pas de protocole DTLS 1.1.
- **Redémarrez les services concernés.** Les paramètres Schannel et applicatifs nécessitent souvent un redémarrage du service ou du système.
- **Consignez les exceptions.** Notez chaque point de terminaison ancien qui nécessite temporairement un réglage de compatibilité et fixez une date de retrait.
