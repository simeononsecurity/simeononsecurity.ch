---
title: "Windows Defender PowerShell-Befehle für die Systemsicherheit"
date: 2023-07-27
lastmod: 2026-11-20
toc: true
draft: false
description: "Entdecken Sie die Leistungsfähigkeit der Windows Defender PowerShell-Befehle, und erfahren Sie, wie Sie die Sicherheit Ihres Systems mit der Befehlszeilensteuerung verbessern können."
genre: ["Windows Defender", "PowerShell-Befehle", "Systemsicherheit", "Befehlszeilenkontrolle", "Virenschutz", "Windows-Betriebssysteme", "Malwareschutz", "erweiterte Sicherheitseinstellungen", "Automatisierung von Sicherheitsabläufen", "Windows PowerShell"]
tags: ["Technologie", "Cybersicherheit", "Betriebssysteme", "Windows", "Befehlszeilen-Tools", "System-Sicherheit", "PowerShell", "Virenschutz", "Schutz vor Malware", "Skripterstellung"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.webp"
coverAlt: "Eine animierte Illustration, die ein Schild zeigt, das ein Computersystem vor verschiedenen Cyber-Bedrohungen schützt."
coverCaption: "Verbessern Sie die Sicherheit Ihres Systems mit Windows Defender PowerShell-Befehlen."
---

## Einleitung

Windows Defender wurde von Microsoft entwickelt und ist eine integrierte Antiviren- und Sicherheitslösung für Windows-Betriebssysteme. Sie bietet eine benutzerfreundliche Oberfläche zur effektiven Verwaltung von Sicherheitseinstellungen. Für fortgeschrittene Benutzer, die eine Steuerung über die Befehlszeile bevorzugen, bietet Windows Defender jedoch eine Reihe von leistungsstarken PowerShell-Befehlen. In diesem Artikel werden wir in die Welt der **Windows Defender PowerShell-Befehle** eintauchen und untersuchen, wie sie die Systemsicherheit verbessern und eine bessere Kontrolle über Ihre Windows-Umgebung ermöglichen können.

## Die Macht der Windows Defender PowerShell-Befehle

Mit den Windows Defender PowerShell-Befehlen können Benutzer erweiterte Sicherheitsvorgänge über eine Befehlszeilenschnittstelle durchführen. Diese Befehle bieten eine breite Palette von Funktionen, von einfachen Vorgängen wie dem Scannen nach Malware bis hin zu komplexen Aufgaben wie der Konfiguration von erweiterten Sicherheitseinstellungen. Durch die Verwendung von PowerShell können Benutzer Sicherheitsvorgänge automatisieren, benutzerdefinierte Skripts erstellen und Windows Defender nahtlos in ihre bestehenden Arbeitsabläufe integrieren.

## Erste Schritte mit Windows Defender PowerShell

Um auf Windows Defender PowerShell-Befehle zugreifen zu können, müssen Sie eine PowerShell-Sitzung mit Administratorrechten öffnen. Hier erfahren Sie, wie Sie beginnen können:

1. Drücken Sie `Win + X` und wählen Sie **Windows PowerShell (Admin)** (als Administrator) aus dem Menü.
2. Wenn Sie dazu aufgefordert werden, klicken Sie auf **Yes** (Ja), damit die App Änderungen an Ihrem Gerät vornehmen kann.

Sobald Sie eine PowerShell-Sitzung geöffnet haben, können Sie die Windows Defender PowerShell-Befehle verwenden.

## Allgemeine Windows Defender PowerShell-Befehle

### 1. **Get-MpComputerStatus**: Überprüfen des Windows Defender-Status

Der Befehl `Get-MpComputerStatus` gibt einen Überblick über den aktuellen Status von Windows Defender auf Ihrem System. Dazu gehören die Version der Antiviren-Engine, der Zeitpunkt des letzten Scans und der Status des Echtzeitschutzes. Mit diesem Befehl können Sie den Zustand von Windows Defender schnell prüfen und sicherstellen, dass der Schutz ordnungsgemäß funktioniert.

Um den Windows Defender-Status zu überprüfen, öffnen Sie eine PowerShell-Sitzung mit administrativen Rechten und führen Sie den folgenden Befehl aus:

```powershell
Get-MpComputerStatus
```

Dieser Befehl zeigt Informationen wie z.B.:

- **AntivirusEngineVersion**: Die Versionsnummer der von Windows Defender verwendeten Antiviren-Engine.
- **LastFullScanTime**: Datum und Uhrzeit der letzten vollständigen Überprüfung, die von Windows Defender durchgeführt wurde.
- **LastQuickScanTime**: Datum und Uhrzeit der letzten von Windows Defender durchgeführten Schnellüberprüfung.
- **RealTimeProtectionEnabled**: Gibt an, ob der Echtzeitschutz aktiviert oder deaktiviert ist.

Regelmäßige Überwachung des Windows Defender-Status mit `Get-MpComputerStatus` stellt sicher, dass Sie über das Schutzniveau Ihres Systems vor potenziellen Bedrohungen informiert bleiben.

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

Mit dem Befehl `Update-MpSignature` können Sie die von Windows Defender verwendeten Antivirensignaturen manuell aktualisieren. Diese Signaturen enthalten wichtige Informationen zu bekannter Malware und helfen Windows Defender, Bedrohungen zu erkennen und zu blockieren. Wenn Sie den Befehl ausführen, erhält Ihr System die neuesten Signaturen und besseren Schutz vor neuen Bedrohungen.

Um Windows Defender-Signaturen manuell zu aktualisieren, öffnen Sie eine PowerShell-Sitzung mit Administratorrechten und führen Sie den folgenden Befehl aus:

```powershell
Update-MpSignature
```
Dieser Befehl löst den Update-Prozess aus, bei dem **Windows Defender** eine Verbindung zu **Microsoft-Servern** herstellt, um die neuesten **Virensignaturen** herunterzuladen. Sobald das Update abgeschlossen ist, verfügt Windows Defender über die aktuellsten Informationen über bekannte Malware und kann Bedrohungen besser erkennen und beseitigen.

Die Signaturen von Windows Defender auf dem neuesten Stand zu halten, ist unerlässlich, um ein Höchstmaß an Schutz vor der sich ständig weiterentwickelnden Landschaft von **Malware** und **Cyber-Bedrohungen** zu gewährleisten. Durch regelmäßiges Aktualisieren der Signaturen mit `Update-MpSignature` stellen Sie sicher, dass Windows Defender Ihr System wirksam schützen kann.

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

Mit dem Befehl `Set-MpPreference` können Sie verschiedene Einstellungen von **Windows Defender** an Ihre Sicherheitsanforderungen anpassen. Dazu gehören Optionen für **Echtzeitschutz**, **cloudbasierten Schutz** und **Einstellungen des Netzwerkinspektionssystems**.

Sie können den Echtzeitschutz beispielsweise mit `Set-MpPreference` aktivieren oder deaktivieren. Der Echtzeitschutz überwacht Ihr System auf schädliche Aktivitäten und reagiert sofort auf Bedrohungen. Führen Sie zum Aktivieren des Echtzeitschutzes den folgenden Befehl aus:

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

Außerdem können Sie mit diesem Befehl die Einstellungen für den Cloud-basierten Schutz anpassen. Der Cloud-basierte Schutz nutzt Cloud-Ressourcen, um die Erkennung von Bedrohungen zu verbessern und schneller auf neue Bedrohungen reagieren zu können. Um den Cloud-basierten Schutz zu aktivieren, verwenden Sie den folgenden Befehl:

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

Außerdem können Sie mit dem Befehl `Set-MpPreference` die Einstellungen des Netzwerkinspektionssystems anpassen. Dieses System analysiert den Netzwerkverkehr auf verdächtige Aktivitäten und mögliche Bedrohungen. Führen Sie zum Anpassen der Einstellungen den folgenden Befehl aus:

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

Durch Feinabstimmung dieser Einstellungen mit `Set-MpPreference` können Sie **Windows Defender** so optimieren, dass er Ihren spezifischen Sicherheitsanforderungen entspricht und einen zuverlässigen Schutz vor Malware und anderen bösartigen Aktivitäten gewährleistet.

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

Der Befehl `Start-MpScan` startet Malware-Scans auf Ihrem System, damit Sie schädliche Dateien frühzeitig erkennen und entfernen können. Er unterstützt verschiedene Scanarten, darunter **Schnellscans**, **vollständige Scans** und **benutzerdefinierte Scans** bestimmter Pfade.

Führen Sie für einen **Schnellscan** mit `Start-MpScan` den folgenden PowerShell-Befehl aus:

```powershell
Start-MpScan -ScanType QuickScan
```

Ein schneller Scan konzentriert sich auf kritische Bereiche Ihres Systems, in denen Malware häufig gefunden wird, und ermöglicht eine schnelle Bewertung potenzieller Bedrohungen.

Für einen umfassenderen Scan aller Dateien und Verzeichnisse auf Ihrem System können Sie einen **vollständigen Scan** starten. Führen Sie dazu mit `Start-MpScan` den folgenden Befehl aus:

```powershell
Start-MpScan -ScanType FullScan
```

Eine vollständige Überprüfung gewährleistet eine gründliche Erkennung und Entfernung von Malware von Ihrem System, kann aber im Vergleich zu einer Schnellüberprüfung länger dauern.

Neben den vordefinierten Scanarten können Sie mit `Start-MpScan` benutzerdefinierte Scans ausführen und bestimmte Pfade oder Dateien angeben. Mit dem folgenden Befehl können Sie zum Beispiel ein bestimmtes Verzeichnis scannen:

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

Mit diesem Befehl wird ein benutzerdefinierter Scan für das angegebene Verzeichnis initiiert, mit dem Sie gezielt bestimmte Bereiche Ihres Systems auf Malware untersuchen können.

Durch die Nutzung der Vielseitigkeit des `Start-MpScan` können Sie Scans planen, Sicherheitsprozesse automatisieren und die regelmäßige Erkennung und Bekämpfung von Malware auf Ihrem System sicherstellen.

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

Der Befehl `Get-MpThreatCatalog` liefert detaillierte Informationen zu bekannten Bedrohungen und ihren Eigenschaften. Der Katalog enthält unter anderem Angaben zum Schweregrad, zu zugehörigen Dateinamen und zu empfohlenen Maßnahmen zur Eindämmung.

Führen Sie die folgenden Schritte aus, um mit `Get-MpThreatCatalog` Informationen zu bestimmten Bedrohungen abzurufen:

1. Öffnen Sie eine PowerShell-Sitzung mit administrativen Rechten.
2. Führen Sie den folgenden Befehl aus:

```powershell
   Get-MpThreatCatalog
```
Mit diesem Befehl wird eine Liste der bekannten Bedrohungen mit den entsprechenden Details angezeigt.

Die Ausgabe des Befehls `Get-MpThreatCatalog` enthält wichtige Angaben wie:

- **ThreatID**: Eine eindeutige Kennung für die Bedrohung.
- **Severity**: Gibt den Schweregrad der Bedrohung von Low bis Severe an.
- **Name**: Der Name oder die Beschreibung der Bedrohung.
- **Path**: Der Pfad der zugehörigen Datei.
- **RecommendedAction**: Gibt eine empfohlene Maßnahme zur Eindämmung der Bedrohung an.

Mit den Ergebnissen von `Get-MpThreatCatalog` erhalten Sie Einblick in mögliche Bedrohungen und können fundierte Entscheidungen zu ihrer Eindämmung treffen. Dazu gehören etwa das Isolieren, Entfernen oder Überwachen einer Bedrohung. Der Katalog hilft Ihnen, wirksam auf Sicherheitsvorfälle zu reagieren.

Weitere Informationen zur Verwendung von `Get-MpThreatCatalog` und die Interpretation der Ergebnisse finden Sie in der offiziellen Microsoft-Dokumentation.

Nutzen Sie den Befehl `Get-MpThreatCatalog` regelmäßig, um über neue Bedrohungen informiert zu bleiben und die Sicherheit Ihres Systems zu verbessern.

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

Mit dem Befehl `Add-MpPreference` können Sie Ausschlüsse in Windows Defender hinzufügen und so das Scanverhalten und den Echtzeitschutz anpassen. Sie können Dateien, Ordner oder Prozesse angeben, die Windows Defender bei Scans oder beim Echtzeitschutz ignorieren soll.

Wenn Sie mit `Add-MpPreference` einen Ausschluss hinzufügen, geben Sie den Pfad oder Namen der auszuschließenden Datei, des Ordners oder Prozesses an. Das folgende Beispiel fügt einen Ordner als Ausschluss hinzu:

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

Dieser Befehl sorgt dafür, dass Windows Defender die Überprüfung des angegebenen Ordners überspringt, wodurch unnötige Warnungen und mögliche Unterbrechungen Ihres Arbeitsablaufs vermieden werden.

Ausschlüsse können in verschiedenen Szenarien nützlich sein, z. B. beim Ausschluss von vertrauenswürdigen Anwendungen, Entwicklungsumgebungen oder bestimmten Dateien, die Fehlalarme auslösen können. Durch die Nutzung der Flexibilität von `Add-MpPreference` können Sie Windows Defender an Ihre speziellen Sicherheitsanforderungen anpassen und seine Leistung optimieren.

Schützen Sie Ihr System wirksam und vermeiden Sie unnötige Fehlalarme und Scanunterbrechungen mit den Ausschlussfunktionen von `Add-MpPreference`.

## Defender-Befehle 2026 prüfen

Führen Sie Defender-Befehle nur in einer erhöhten Sitzung aus, wenn die Aufgabe Administratorrechte erfordert. Prüfen Sie vor der Verwendung eines Parameters die aktuelle Modulhilfe für die jeweilige Windows-Version. Erfassen Sie die bestehende Konfiguration, ändern Sie jeweils eine Einstellung, prüfen Sie das Ergebnis und notieren Sie den Rücksetzungsbefehl.

Nützliche Prüfschritte sind der Schutzstatus, das Alter der Signaturen, Ausschlüsse, Einstellungen, Scanverlauf und aktuelle Erkennungen. Beschränken Sie den Umfang der Ausschlüsse und dokumentieren Sie die Verantwortlichen sowie das Ablaufdatum. Aktuelle Cmdlets und ihr Verhalten finden Sie in der offiziellen [Dokumentation zum Microsoft Defender PowerShell-Modul](https://learn.microsoft.com/en-us/powershell/module/defender/) und der [Dokumentation zu Microsoft Defender Antivirus](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-windows).

## Schlussfolgerung

Die Windows Defender PowerShell-Befehle bieten einen **robusten Satz von Tools** für die Verwaltung und Verbesserung der Sicherheit Ihres Windows-Systems. Durch die Nutzung dieser Befehle können Sie *Sicherheitsvorgänge automatisieren*, *erweiterte Einstellungen konfigurieren* und Windows Defender nahtlos in Ihre Arbeitsabläufe integrieren. Unabhängig davon, ob Sie ein **Systemadministrator** oder ein **fortgeschrittener Nutzer** sind, können Sie durch die Erkundung der Möglichkeiten der Windows Defender PowerShell-Befehle die Sicherheitslage Ihres Systems erheblich verbessern.

Denken Sie daran, dass mit großer Macht auch große Verantwortung einhergeht. Seien Sie bei der Verwendung von PowerShell-Befehlen vorsichtig und stellen Sie sicher, dass Sie die Auswirkungen der Befehle verstehen, bevor Sie sie ausführen. Wenn Sie Ihr Wissen mit der Leistungsfähigkeit der Windows Defender PowerShell-Befehle kombinieren, können Sie proaktive Maßnahmen ergreifen, um Ihr System vor sich entwickelnden Bedrohungen zu schützen.

## Referenzen

1. Microsoft Docs - [Windows Defender-Cmdlets in Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. Microsoft Docs - [Einführung in Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
