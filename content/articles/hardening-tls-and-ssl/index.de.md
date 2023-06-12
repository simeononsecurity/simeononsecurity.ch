---
title: "Härtung der Sicherheit Ihres Computers durch Deaktivierung von SSL und TLS 1.2 und darunter"
date: 2023-02-08
toc: true
draft: false
description: "Dieser Artikel beschreibt die Schritte zur Verbesserung der Datensicherheit durch die Deaktivierung älterer Versionen von SSL- und TLS-Protokollen, die für Cyber-Bedrohungen wie POODLE, BEAST und Heartbleed anfällig sind, in Windows- und Linux-Systemen."
tags: ["Verstärkung der Computersicherheit", "Deaktivieren von SSL und TLS", "Sicherheit der Daten", "POODLE", "BEAST", "Heartbleed", "Windows-Registrierungs-Editor", "Linux OpenSSL-Konfiguration", "Apache", "Nginx"]
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.png"
coverAlt: "Ein Computer mit einem Vorhängeschloss-Symbol, das für Datensicherheit steht"
coverCaption: ""
---

## Einleitung:

Computer sind zu einem entscheidenden Aspekt unseres täglichen Lebens geworden, und damit ist auch der Bedarf an Datensicherheit erheblich gestiegen. Unter den verschiedenen Methoden zur Sicherung von Daten bei der Übertragung sind SSL (Secure Socket Layer) und TLS (Transport Layer Security) weit verbreitete Protokolle. Da sich die Technologie jedoch weiterentwickelt, werden ältere Versionen dieser Protokolle anfällig für Cyberangriffe. In diesem Artikel besprechen wir, wie man Computer durch Deaktivieren von SSL und allen TLS-Versionen 1.2 und darunter härtet, um die Daten zu schützen.

### Warum SSL und TLS 1.2 und darunter deaktivieren?

Ältere Versionen von SSL und TLS sind anfällig für verschiedene Sicherheitsbedrohungen wie POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) und Heartbleed. Diese Angriffe können zur Preisgabe sensibler Daten führen, weshalb es wichtig ist, die Verwendung veralteter Protokolle zu deaktivieren.

### Deaktivieren von SSL und TLS 1.2 und darunter in Windows:

In Windows kann die Deaktivierung von SSL und TLS 1.2 und darunter über den Registrierungseditor erfolgen. Hier finden Sie ein Powershell-Skript, mit dem Sie diese Aufgabe erledigen können:

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

#### Deaktivierung von SSL und TLS 1.2 und darunter unter Linux:

Unter Linux kann die Deaktivierung von SSL und TLS 1.2 und darunter durch Änderung der OpenSSL-Konfigurationsdatei erreicht werden. Die folgenden Schritte sind zu befolgen:

1. Öffnen Sie das Terminal und melden Sie sich als root an.
2. Navigieren Sie zu der OpenSSL-Konfigurationsdatei. Normalerweise befindet sie sich unter /etc/ssl/openssl.cnf.
3. Öffnen Sie die Datei mit einem Texteditor wie nano oder vim.
4. Suchen Sie die Richtlinie SSLProtocol und setzen Sie ihren Wert auf -TLSv1.2.
5. Speichern Sie die Datei und schließen Sie den Texteditor.
6. Starten Sie die Dienste, die OpenSSL verwenden, wie z. B. Apache oder Nginx, neu, damit die Änderungen wirksam werden.

## Fazit:

Durch die Deaktivierung von SSL und allen TLS-Versionen 1.2 und darunter können Sie die Sicherheit Ihres Computers erhöhen und sensible Informationen vor potenziellen Cyber-Bedrohungen schützen. Es handelt sich dabei um einen einfachen Prozess, der mit minimalem Aufwand durchgeführt werden kann und daher ein wichtiger Aspekt bei der Aufrechterhaltung der Sicherheit Ihres Computers ist. Durch die Umsetzung der in diesem Artikel beschriebenen Schritte können Sie Ihre Daten schützen und Cyberangriffe verhindern, wodurch das Risiko der Preisgabe vertraulicher Informationen verringert wird.

Es ist wichtig zu beachten, dass die Deaktivierung dieser älteren Versionen von SSL- und TLS-Protokollen zwar die Sicherheit Ihres Computers verbessern kann, aber auch die Kompatibilität mit einigen älteren Systemen beeinträchtigen kann. Daher ist es wichtig, die vorgenommenen Änderungen gründlich zu testen und sicherzustellen, dass sie sich nicht negativ auf Ihr System auswirken, bevor Sie sie vollständig implementieren.

Zusammenfassend lässt sich sagen, dass die Härtung Ihres Computers durch die Deaktivierung von SSL und allen TLS-Versionen 1.2 und darunter ein wichtiger Schritt ist, um die Sicherheit sensibler Daten zu gewährleisten und Cyberangriffe zu verhindern. Die in diesem Artikel beschriebenen Schritte bieten eine unkomplizierte Anleitung zur Sicherung Ihres Computers, die es Einzelpersonen und Unternehmen leicht macht, die erforderlichen Sicherheitsmaßnahmen zu ergreifen.