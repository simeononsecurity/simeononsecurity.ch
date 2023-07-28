---
title: "Erhöhen Sie Ihre Systemsicherheit mit Windows Defender PowerShell-Befehlen"
date: 2023-07-27
toc: true
draft: false
description: "Entdecken Sie die Leistungsfähigkeit der Windows Defender PowerShell-Befehle, und erfahren Sie, wie Sie die Sicherheit Ihres Systems mit der Befehlszeilensteuerung verbessern können."
genre: ["Windows Defender", "PowerShell-Befehle", "Systemsicherheit", "Befehlszeilenkontrolle", "Antivirus", "Windows-Betriebssysteme", "Malwareschutz", "erweiterte Sicherheitseinstellungen", "Sicherheitsabläufe zu automatisieren", "Windows PowerShell"]
tags: ["Technologie", "Cybersecurity", "Betriebssysteme", "Windows", "Befehlszeilen-Tools", "System-Sicherheit", "PowerShell", "Antivirus", "Schutz vor Malware", "Skripting"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.png"
coverAlt: "Eine animierte Illustration, die ein Schild zeigt, das ein Computersystem vor verschiedenen Cyber-Bedrohungen schützt."
coverCaption: "Verbessern Sie die Sicherheit Ihres Systems mit Windows Defender PowerShell-Befehlen."
---

## Einleitung

Windows Defender wurde von Microsoft entwickelt und ist eine integrierte Antiviren- und Sicherheitslösung für Windows-Betriebssysteme. Sie bietet eine benutzerfreundliche Oberfläche zur effektiven Verwaltung von Sicherheitseinstellungen. Für fortgeschrittene Benutzer, die eine Steuerung über die Befehlszeile bevorzugen, bietet Windows Defender jedoch eine Reihe von leistungsstarken PowerShell-Befehlen. In diesem Artikel werden wir in die Welt der **Windows Defender PowerShell-Befehle** eintauchen und untersuchen, wie sie die Systemsicherheit verbessern und eine bessere Kontrolle über Ihre Windows-Umgebung ermöglichen können.

## Die Macht der Windows Defender PowerShell-Befehle

Mit den Windows Defender PowerShell-Befehlen können Benutzer erweiterte Sicherheitsvorgänge über eine Befehlszeilenschnittstelle durchführen. Diese Befehle bieten eine breite Palette von Funktionen, von einfachen Vorgängen wie dem Scannen nach Malware bis hin zu komplexen Aufgaben wie der Konfiguration von erweiterten Sicherheitseinstellungen. Durch die Verwendung von PowerShell können Benutzer Sicherheitsvorgänge automatisieren, benutzerdefinierte Skripts erstellen und Windows Defender nahtlos in ihre bestehenden Arbeitsabläufe integrieren.

## Erste Schritte mit Windows Defender PowerShell

Um auf Windows Defender PowerShell-Befehle zugreifen zu können, müssen Sie eine PowerShell-Sitzung mit Administratorrechten öffnen. Hier erfahren Sie, wie Sie beginnen können:

1. Drücken Sie `Win + X` und wählen Sie **Windows PowerShell (Admin)** aus dem Menü.
2. Wenn Sie dazu aufgefordert werden, klicken Sie auf **Ja**, damit die App Änderungen an Ihrem Gerät vornehmen kann.

Sobald Sie eine PowerShell-Sitzung geöffnet haben, können Sie die Windows Defender PowerShell-Befehle verwenden.

## Allgemeine Windows Defender PowerShell-Befehle

### 1. **Get-MpComputerStatus**: Überprüfen des Windows Defender-Status

Die Seite `Get-MpComputerStatus` bietet einen Überblick über den aktuellen Status von Windows Defender auf Ihrem System, einschließlich der Version der Antiviren-Engine, der Zeit der letzten Überprüfung und des Echtzeitschutzstatus. Wenn Sie diesen Befehl ausführen, können Sie den allgemeinen Zustand von Windows Defender schnell beurteilen und sicherstellen, dass er optimal funktioniert.

Um den Windows Defender-Status zu überprüfen, öffnen Sie eine PowerShell-Sitzung mit administrativen Rechten und führen Sie den folgenden Befehl aus:

```powershell
Get-MpComputerStatus
```

Dieser Befehl zeigt Informationen wie z.B.:

- **AntivirusEngineVersion**: Die Versionsnummer der von Windows Defender verwendeten Antiviren-Engine.
- **LastFullScanTime**: Datum und Uhrzeit der letzten vollständigen Überprüfung, die von Windows Defender durchgeführt wurde.
- **LastQuickScanTime**: Datum und Uhrzeit der letzten von Windows Defender durchgeführten Schnellüberprüfung.
- **EchtzeitschutzAktiviert**: Gibt an, ob der Echtzeitschutz aktiviert oder deaktiviert ist.

Regelmäßige Überwachung des Windows Defender-Status mit `Get-MpComputerStatus` stellt sicher, dass Sie über das Schutzniveau Ihres Systems vor potenziellen Bedrohungen informiert bleiben.

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

Die `Update-MpSignature` bietet Ihnen die Möglichkeit, die von Windows Defender verwendeten Antivirensignaturen manuell zu aktualisieren. Antivirensignaturen enthalten wichtige Informationen über bekannte Malware und ermöglichen es Windows Defender, Bedrohungen effektiv zu erkennen und zu blockieren. Durch die Ausführung dieses Befehls stellen Sie sicher, dass Ihr System mit den neuesten Signaturen ausgestattet ist, die einen verbesserten Schutz vor neuen Bedrohungen bieten.

Um Windows Defender-Signaturen manuell zu aktualisieren, öffnen Sie eine PowerShell-Sitzung mit Administratorrechten und führen Sie den folgenden Befehl aus:

```powershell
Update-MpSignature
```
Dieser Befehl löst den Update-Prozess aus, bei dem **Windows Defender** eine Verbindung zu **Microsoft-Servern** herstellt, um die neuesten **Virensignaturen** herunterzuladen. Sobald das Update abgeschlossen ist, verfügt Windows Defender über die aktuellsten Informationen über bekannte Malware und kann Bedrohungen besser erkennen und beseitigen.

Die Signaturen von Windows Defender auf dem neuesten Stand zu halten, ist unerlässlich, um ein Höchstmaß an Schutz vor der sich ständig weiterentwickelnden Landschaft von **Malware** und **Cyber-Bedrohungen** zu gewährleisten. Durch regelmäßiges Aktualisieren der Signaturen mit `Update-MpSignature` stellen Sie sicher, dass Windows Defender Ihr System wirksam schützen kann.

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

Die `Set-MpPreference` ermöglicht es Ihnen, verschiedene Einstellungen von **Windows Defender** anzupassen, so dass Sie das Verhalten des Programms auf Ihre spezifischen Sicherheitsanforderungen abstimmen können. Dieser Befehl bietet Flexibilität bei der Konfiguration von Optionen wie **Echtzeitschutz**, **Cloud-basierter Schutz** und **Systemeinstellungen für die Netzwerkinspektion**.

Sie können zum Beispiel den Echtzeitschutz mit dem Befehl `Set-MpPreference` Befehl. Der Echtzeitschutz überwacht Ihr System aktiv auf bösartige Aktivitäten und reagiert sofort auf Bedrohungen. Um den Echtzeitschutz zu aktivieren, führen Sie den folgenden Befehl aus:

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

Außerdem können Sie mit diesem Befehl die Einstellungen für den Cloud-basierten Schutz anpassen. Der Cloud-basierte Schutz nutzt Cloud-Ressourcen, um die Erkennung von Bedrohungen zu verbessern und schneller auf neue Bedrohungen reagieren zu können. Um den Cloud-basierten Schutz zu aktivieren, verwenden Sie den folgenden Befehl:

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

Außerdem ist die `Set-MpPreference` ermöglicht die Anpassung der Einstellungen des Netzwerkinspektionssystems. Das Netzwerkinspektionssystem analysiert den Netzwerkverkehr auf verdächtige Aktivitäten und potenzielle Bedrohungen. Um die Einstellungen des Netzwerkinspektionssystems anzupassen, führen Sie den folgenden Befehl aus:

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

Durch Feinabstimmung dieser Einstellungen mit `Set-MpPreference` können Sie **Windows Defender** so optimieren, dass er Ihren spezifischen Sicherheitsanforderungen entspricht und einen zuverlässigen Schutz vor Malware und anderen bösartigen Aktivitäten gewährleistet.

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

Die `Start-MpScan` ist ein leistungsfähiges Tool zum Starten von Malware-Scans auf Ihrem System, mit dem Sie proaktiv bösartige Dateien identifizieren und beseitigen können. Dieser Befehl bietet Flexibilität bei der Durchführung verschiedener Arten von Scans, einschließlich **Schnell-Scans**, **Voll-Scans** und **Benutzerdefinierte Scans** mit bestimmten Pfaden.

So führen Sie einen **Schnell-Scan** mit dem Befehl `Start-MpScan` auszuführen, führen Sie den folgenden PowerShell-Befehl aus:

```powershell
Start-MpScan -ScanType QuickScan
```

Ein schneller Scan konzentriert sich auf kritische Bereiche Ihres Systems, in denen Malware häufig gefunden wird, und ermöglicht eine schnelle Bewertung potenzieller Bedrohungen.

Für einen umfassenderen Scan, bei dem alle Dateien und Verzeichnisse auf Ihrem System untersucht werden, können Sie einen **Vollscan** initiieren. Führen Sie den folgenden Befehl aus, um einen vollständigen Scan durchzuführen `Start-MpScan`

```powershell
Start-MpScan -ScanType FullScan
```

Eine vollständige Überprüfung gewährleistet eine gründliche Erkennung und Entfernung von Malware von Ihrem System, kann aber im Vergleich zu einer Schnellüberprüfung länger dauern.

Zusätzlich zu den vordefinierten Scantypen bietet die `Start-MpScan` können Sie benutzerdefinierte Scans durchführen, indem Sie bestimmte Pfade oder Dateien angeben, die gescannt werden sollen. Mit dem folgenden Befehl können Sie zum Beispiel ein bestimmtes Verzeichnis auf Ihrem System scannen:

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

Mit diesem Befehl wird ein benutzerdefinierter Scan für das angegebene Verzeichnis initiiert, mit dem Sie gezielt bestimmte Bereiche Ihres Systems auf Malware untersuchen können.

Durch die Nutzung der Vielseitigkeit des `Start-MpScan` können Sie Scans planen, Sicherheitsprozesse automatisieren und die regelmäßige Erkennung und Bekämpfung von Malware auf Ihrem System sicherstellen.

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

Die `Get-MpThreatCatalog` ist eine wertvolle Ressource, um detaillierte Informationen über bekannte Bedrohungen und ihre Attribute zu erhalten. Durch Ausführen dieses Befehls können Sie auf einen umfassenden Katalog von Bedrohungen zugreifen, einschließlich Daten zu deren Schweregrad, zugehörigen Dateinamen und empfohlenen Maßnahmen zur Schadensbegrenzung.

Um Informationen über bestimmte Bedrohungen abzurufen, verwenden Sie `Get-MpThreatCatalog` folgen Sie diesen Schritten:

1. Öffnen Sie eine PowerShell-Sitzung mit administrativen Rechten.
2. Führen Sie den folgenden Befehl aus:

```powershell
   Get-MpThreatCatalog
```
Mit diesem Befehl wird eine Liste der bekannten Bedrohungen mit den entsprechenden Details angezeigt.

Die Ausgabe des Befehls `Get-MpThreatCatalog` Der Befehl enthält wichtige Informationen wie z. B.:

- **ThreatID**: Eine eindeutige Kennung für die Bedrohung.
- **Schweregrad**: Gibt den Schweregrad der Bedrohung an, der von niedrig bis schwer reicht.
- **Name**: Der Name oder die Beschreibung der Bedrohung.
- **Pfad**: Der Pfad der Datei, die mit der Bedrohung verknüpft ist.
- **Empfohlene Maßnahme**: Enthält Hinweise auf die empfohlene Maßnahme zur Abschwächung der Bedrohung.

Durch die Nutzung der Informationen, die von `Get-MpThreatCatalog` erhalten Sie wertvolle Einblicke in potenzielle Bedrohungen und können fundierte Entscheidungen über die geeigneten Maßnahmen zu deren Eindämmung treffen. Ob es um die Isolierung, Entfernung oder Überwachung einer bestimmten Bedrohung geht, der detaillierte Katalog ermöglicht es Ihnen, effektiv auf Sicherheitsvorfälle zu reagieren.

Weitere Informationen zur Verwendung von `Get-MpThreatCatalog` und die Interpretation der Ergebnisse finden Sie in der offiziellen Microsoft-Dokumentation.

Seien Sie wachsam und nutzen Sie regelmäßig die `Get-MpThreatCatalog` Befehl, um über die sich entwickelnde Bedrohungslandschaft informiert zu bleiben und die Sicherheit Ihres Systems zu verbessern.

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

Die `Add-MpPreference` können Sie Ausnahmen zu Windows Defender hinzufügen und so das Verhalten von Scans und Echtzeitschutz anpassen. Durch das Hinzufügen von Ausnahmen können Sie Dateien, Ordner oder Prozesse angeben, die Windows Defender bei Sicherheitsscans oder Echtzeitschutz ignorieren soll.

Um einen Ausschluss hinzuzufügen, verwenden Sie `Add-MpPreference` müssen Sie den Pfad oder Namen der Datei, des Ordners oder des Prozesses angeben, den Sie ausschließen möchten. Hier ist ein Beispiel für das Hinzufügen eines Ausschlusses für einen Ordner:

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

Dieser Befehl sorgt dafür, dass Windows Defender die Überprüfung des angegebenen Ordners überspringt, wodurch unnötige Warnungen und mögliche Unterbrechungen Ihres Arbeitsablaufs vermieden werden.

Ausschlüsse können in verschiedenen Szenarien nützlich sein, z. B. beim Ausschluss von vertrauenswürdigen Anwendungen, Entwicklungsumgebungen oder bestimmten Dateien, die Fehlalarme auslösen können. Durch die Nutzung der Flexibilität von `Add-MpPreference` können Sie Windows Defender an Ihre speziellen Sicherheitsanforderungen anpassen und seine Leistung optimieren.

Schützen Sie Ihr System effektiv und minimieren Sie Fehlalarme und unnötige Scan-Unterbrechungen, indem Sie die leistungsstarken Ausschlussfunktionen nutzen, die von `Add-MpPreference`

## Schlussfolgerung

Die Windows Defender PowerShell-Befehle bieten einen **robusten Satz von Tools** für die Verwaltung und Verbesserung der Sicherheit Ihres Windows-Systems. Durch die Nutzung dieser Befehle können Sie *Sicherheitsvorgänge automatisieren*, *erweiterte Einstellungen konfigurieren* und Windows Defender nahtlos in Ihre Arbeitsabläufe integrieren. Unabhängig davon, ob Sie ein **Systemadministrator** oder ein **Hauptbenutzer** sind, können Sie durch die Erkundung der Möglichkeiten der Windows Defender PowerShell-Befehle die Sicherheitslage Ihres Systems erheblich verbessern.

Denken Sie daran, dass mit großer Macht auch große Verantwortung einhergeht. Seien Sie bei der Verwendung von PowerShell-Befehlen vorsichtig und stellen Sie sicher, dass Sie die Auswirkungen der Befehle verstehen, bevor Sie sie ausführen. Wenn Sie Ihr Wissen mit der Leistungsfähigkeit der Windows Defender PowerShell-Befehle kombinieren, können Sie proaktive Maßnahmen ergreifen, um Ihr System vor sich entwickelnden Bedrohungen zu schützen.

## Referenzen

1. Microsoft Docs - [Windows Defender Cmdlets in Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2) Microsoft Docs - [Introduction to Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
