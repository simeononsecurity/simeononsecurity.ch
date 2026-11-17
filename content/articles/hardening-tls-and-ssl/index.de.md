---
title: "Härten Sie die Computersicherheit, indem Sie SSL und TLS 1.1 und ältere Versionen deaktivieren"
date: 2023-02-08
lastmod: 2026-11-13
toc: true
draft: false
description: "Deaktivieren Sie SSL und alte TLS-Versionen, während TLS 1.2 oder neuer verfügbar bleibt. Der Artikel behandelt Schannel und .NET unter Windows sowie Linux-Dienste."
tags: ['Computersicherheit härten', 'SSL und TLS deaktivieren', 'Datensicherheit', 'POODLE', 'BEAST', 'Heartbleed', 'Windows-Registrierungseditor', 'Linux-OpenSSL-Konfiguration', 'Apache', 'Nginx']
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.webp"
coverAlt: "Ein Computer mit Vorhängeschloss-Symbol als Zeichen für Datensicherheit"
coverCaption: ""
---

## Einleitung:

Computer sind zu einem wichtigen Teil unseres Alltags geworden. Damit ist auch der Bedarf an Datensicherheit gewachsen. SSL (Secure Socket Layer) und TLS (Transport Layer Security) schützen Daten bei der Übertragung. Ältere Versionen sind inzwischen anfällig für Cyberangriffe. Dieser Artikel erklärt, wie Sie SSL und TLS 1.0 sowie 1.1 abschalten und TLS 1.2 oder TLS 1.3 verfügbar halten.

*TLS 1.2 ist kein veraltetes Protokoll. Der aktuelle Mindeststandard ist TLS 1.2 oder neuer. [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) definiert TLS 1.3. [RFC 8996](https://www.rfc-editor.org/rfc/rfc8996) erklärt TLS 1.0 und TLS 1.1 offiziell für veraltet.*

### Warum SSL und TLS 1.1 und ältere Versionen deaktivieren?

Ältere SSL- und TLS-Versionen sind anfällig für Bedrohungen wie POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) und Heartbleed. Diese Angriffe können vertrauliche Informationen offenlegen. Heartbleed betraf anfällige OpenSSL-Implementierungen und war selbst keine Protokollversion. Installieren Sie den Bibliotheks-Patch und ändern Sie offengelegte Zugangsdaten.

Die aktuellen [Microsoft-Hinweise zu Schannel-Registrierungseinstellungen](https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings) führen Protokolleinstellungen für unterstützte Windows-Versionen auf. Microsoft empfiehlt Gruppenrichtlinien oder andere unterstützte Verwaltungstools, sofern verfügbar. Bearbeiten Sie die Registrierung direkt nur, wenn keine bessere Steuerung verfügbar ist.

### Deaktivieren von SSL und TLS 1.1 und älteren Versionen unter Windows:

Unter Windows lassen sich die Protokolle über die Registrierung deaktivieren. Das PowerShell-Skript ändert die Schannel-Einstellungen für Client und Server. Außerdem stellt es .NET so ein, dass die TLS-Standardeinstellungen des Betriebssystems und starke Kryptografie verwendet werden.

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

#### Deaktivieren von SSL und TLS 1.1 und älteren Versionen unter Linux:

Unter Linux hängt das Deaktivieren alter Protokolle von der Anwendung und Bibliothek ab. Eine Änderung an `/etc/ssl/openssl.cnf` überschreibt nicht die Einstellungen jedes Daemons oder jeder mitgelieferten TLS-Bibliothek. Gehen Sie so vor:

1. Öffnen Sie das Terminal und melden Sie sich als root an.
2. Öffnen Sie die OpenSSL-Konfigurationsdatei. Sie liegt meist unter /etc/ssl/openssl.cnf.
3. Öffnen Sie die Datei in einem Texteditor wie nano oder vim.
4. Suchen Sie die Protokollanweisung des Dienstes und setzen Sie die Mindestversion auf TLS 1.2. Die frühere Anweisung `-TLSv1.2` deaktivierte TLS 1.2. Verwenden Sie sie nicht als modernen Mindeststandard.
5. Speichern Sie die Datei und schließen Sie den Editor.
6. Starten Sie OpenSSL-Dienste wie Apache oder Nginx neu, damit die Änderungen greifen.

## Fazit:

Wenn Sie SSL und TLS 1.1 und ältere Versionen deaktivieren, härten Sie den Computer und behalten die Kompatibilität mit modernen TLS-Clients. Die Einstellung gehört zum Dienst, der die TLS-Verbindung aushandelt. Testen Sie jede Anwendung einzeln, statt anzunehmen, dass eine OpenSSL-Datei alle Daemons steuert.

Das Deaktivieren älterer Versionen kann die Kompatibilität mit manchen Altsystemen beeinträchtigen. Testen Sie die Änderungen gründlich und prüfen Sie die Auswirkungen, bevor Sie sie vollständig einführen.

Schützen Sie vertrauliche Informationen und senken Sie das Angriffsrisiko, indem Sie den ausgehandelten Protokollstand jedes Dienstes prüfen und temporäre Ausnahmen dokumentieren.

## Aktuelle Prüfliste

- **Prüfen Sie das ausgehandelte Protokoll.** Testen Sie Client und Server mit einem TLS-Scanner oder einem genehmigten internen Test an beiden Verbindungsenden.
- **Lassen Sie TLS 1.2 aktiviert.** Manche ältere Anwendungen benötigen es weiterhin. TLS 1.3 hängt von Betriebssystem und Bibliothek ab.
- **Prüfen Sie DTLS getrennt.** RFC 8996 erklärt DTLS 1.0 für veraltet. Ein DTLS-1.1-Protokoll definiert er nicht.
- **Starten Sie betroffene Dienste neu.** Schannel- und Anwendungseinstellungen erfordern oft einen Neustart des Dienstes oder Systems.
- **Dokumentieren Sie Ausnahmen.** Halten Sie alte Endpunkte mit vorübergehender Kompatibilitätseinstellung fest und setzen Sie einen Termin für deren Abschaltung.
