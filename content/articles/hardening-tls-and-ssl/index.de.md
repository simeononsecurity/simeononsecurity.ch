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
 ## Einführung:  Computer sind zu einem wichtigen Aspekt unseres täglichen Lebens geworden, und damit ist das Bedürfnis nach Datensicherheit erheblich gestiegen. Unter den verschiedenen Methoden zur Sicherung von Daten während der Übertragung sind SSL (Secure Socket Layer) und TLS (Transport Layer Security) weit verbreitete Protokolle. Mit der Weiterentwicklung der Technologie werden ältere Versionen dieser Protokolle jedoch anfällig für Cyberangriffe. In diesem Artikel besprechen wir die Schritte zum Härten von Computern durch Deaktivierung von SSL und allen TLS-Versionen 1.2 und darunter, um die Daten sicher zu halten.  ### Warum SSL und TLS 1.2 und darunter deaktivieren?  Ältere Versionen von SSL und TLS sind anfällig für mehrere Sicherheitsbedrohungen wie POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) und Heartbleed. Diese Angriffe können zur Offenlegung sensibler Informationen führen, weshalb es wesentlich ist, die Verwendung veralteter Protokolle zu deaktivieren.  ### Deaktivieren von SSL und TLS 1.2 und darunter in Windows:  In Windows kann der Vorgang zum Deaktivieren von SSL und TLS 1.2 und niedriger über den Registrierungseditor erreicht werden. Hier ist ein Powershell-Skript, um die Aufgabe zu erfüllen:   #### SSL und TLS 1.2 und darunter unter Linux deaktivieren:  Unter Linux kann der Vorgang zum Deaktivieren von SSL und TLS 1.2 und darunter durch Ändern der OpenSSL-Konfigurationsdatei erreicht werden. Hier sind die folgenden Schritte:  1. Öffnen Sie das Terminal und melden Sie sich als root an. 2. Navigieren Sie zur OpenSSL-Konfigurationsdatei. Normalerweise befindet es sich unter /etc/ssl/openssl.cnf. 3. Öffnen Sie die Datei mit einem Texteditor wie nano oder vim. 4. Suchen Sie die Anweisung SSLProtocol und setzen Sie ihren Wert auf -TLSv1.2. 5. Speichern Sie die Datei und schließen Sie den Texteditor. 6. Starten Sie die Dienste, die OpenSSL verwenden, wie Apache oder Nginx, neu, damit die Änderungen wirksam werden.  ## Abschluss:  Indem Sie SSL und alle TLS-Versionen 1.2 und niedriger deaktivieren, können Sie die Sicherheit Ihres Computers erhöhen und vertrauliche Informationen vor potenziellen Cyber-Bedrohungen schützen. Es ist ein einfacher Prozess, der mit minimalem Aufwand durchgeführt werden kann, was ihn zu einem entscheidenden Aspekt für die Aufrechterhaltung der Sicherheit Ihres Computers macht. Durch die Umsetzung der in diesem Artikel beschriebenen Schritte können Sie Ihre Daten schützen und Cyberangriffe verhindern, wodurch das Risiko verringert wird, dass vertrauliche Informationen offengelegt werden.  Es ist wichtig zu beachten, dass das Deaktivieren dieser älteren Versionen von SSL- und TLS-Protokollen zwar die Sicherheit Ihres Computers verbessern kann, aber auch die Kompatibilität mit einigen älteren Systemen beeinträchtigen kann. Daher ist es wichtig, die vorgenommenen Änderungen gründlich zu testen und sicherzustellen, dass es keine nachteiligen Auswirkungen auf Ihr System gibt, bevor Sie sie vollständig implementieren.  Zusammenfassend lässt sich sagen, dass das Härten Ihres Computers durch Deaktivieren von SSL und aller TLS-Versionen 1.2 und niedriger ein entscheidender Schritt ist, um die Sicherheit sensibler Informationen zu gewährleisten und Cyberangriffe zu verhindern. Die in diesem Artikel beschriebenen Schritte bieten eine einfache Anleitung zum Sichern Ihres Computers und erleichtern es Einzelpersonen und Organisationen, die erforderlichen Sicherheitsmaßnahmen zu implementieren.