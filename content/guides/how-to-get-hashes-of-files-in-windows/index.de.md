---
title: "Vollständige Anleitung: Datei-Hashes unter Windows mit PowerShell"
draft: false
toc: true
date: 2023-05-25
description: "Erfahren Sie, wie Sie mit PowerShell Dateihashes unter Windows abrufen, einschließlich SHA256, MD5 und SHA1, mit schrittweisen Anweisungen und Beispielen."
tags: ["Datei-Hashes", "PowerShell", "SHA256-Hash", "MD5-Hash", "SHA1-Hash", "Dateiintegrität", "Datenauthentifizierung", "Dateiprüfung", "Hashing-Algorithmen", "Windows-Betriebssystem", "Skriptsprache", "Kommandozeilen-Shell", "Datensicherheit", "digitale Forensik", "Cybersicherheit", "Hash-Berechnung", "Dateimanipulation", "Datenintegrität", "Authentizität der Akten", "Windows-Sicherheit", "Dateikennung", "Cyber-Abwehr", "Dateisicherheit", "datenschutz", "Datenüberprüfung", "Dateivalidierung", "Windows PowerShell", "Hash-Erzeugung", "Hash-Algorithmen", "Hash-Funktionen"]
cover: "/img/cover/A_cartoon_illustration_showing_a_file_with_a_lock_symbol.png"
coverAlt: "Eine Cartoon-Illustration, die eine Datei mit einem Schlosssymbol und einer Lupe zeigt, was für die Überprüfung von Datei-Hashes und Sicherheit steht."
coverCaption: ""
---

**Abrufen von Hashes von Dateien unter Windows mit PowerShell**

Im Bereich der Computersicherheit ist das Abrufen von Datei-Hashes ein wichtiger Schritt, um die Datenintegrität zu gewährleisten und die Authentizität von Dateien zu überprüfen. Hashes sind eindeutige Identifikatoren, die für Dateien generiert werden und es Benutzern ermöglichen, Manipulationsversuche zu erkennen und die Integrität von Daten zu überprüfen. In dieser umfassenden Anleitung wird das Verfahren zum Abrufen von **SHA256**-, **MD5**- und **SHA1**-Hashes von Dateien unter Windows mithilfe der leistungsstarken Skriptsprache **PowerShell** erläutert. Folgen Sie den Schritt-für-Schritt-Anweisungen und tauchen Sie tief in spezifische Beispiele ein. Los geht's!

______

## Abrufen von Hashes unter Windows mit PowerShell

PowerShell, eine vielseitige Skriptsprache und Befehlszeilen-Shell für Windows, bietet das Cmdlet **Get-FileHash**, mit dem Benutzer mühelos den Hash einer Datei berechnen können.

### Abrufen des SHA256-Hashes

Führen Sie die folgenden einfachen Schritte aus, um den **SHA256-Hash** einer Datei mit PowerShell abzurufen:

1. Starten Sie PowerShell, indem Sie das **Startmenü** öffnen, nach **PowerShell** suchen und **Windows PowerShell** auswählen.
2. Navigieren Sie zu dem Verzeichnis, in dem sich die Datei befindet. Verwenden Sie die `cd` gefolgt von dem Pfad zum Verzeichnis.
3. Führen Sie den folgenden Befehl aus, um den SHA256-Hash der Datei zu erhalten:
```powershell
   Get-FileHash -Algorithm SHA256 -Path "file_path"
```
### Beschaffung der MD5- und SHA1-Hashes
Sie können auch die `MD5` und `SHA1` Hashes einer Datei mit PowerShell. Verwenden Sie die folgenden Befehle:

- So erhalten Sie die `MD5 hash`
  
```powershell
Get-FileHash -Algorithm MD5 -Path "file_path"
```

- Um die `SHA1 hash`

```powershell
Get-FileHash -Algorithm SHA1 -Path "file_path"
```

Denken Sie daran, in beiden Befehlen "file_path" durch den Pfad zu Ihrer Datei zu ersetzen.

## Beispiele
Lassen Sie uns anhand konkreter Beispiele den Prozess des Abrufs von Hashes mit PowerShell unter Windows erläutern.

{{< youtube id="UrHhsF1q3rU" >}}

### Beispiel 1: SHA256-Hash erhalten
Stellen Sie sich vor, Sie haben eine Datei mit dem Namen `document.pdf` in dem Verzeichnis `C:\Files` Um die `SHA256 hash` dieser Datei mit PowerShell, führen Sie den folgenden Befehl aus:

```powershell
Get-FileHash -Algorithm SHA256 -Path "C:\Files\document.pdf"
```

In der Ausgabe wird der SHA256-Hashwert der Datei angezeigt.

### Beispiel 2: Abrufen des MD5-Hashwerts

Angenommen, Sie besitzen eine Datei namens `image.jpg` gespeichert im Verzeichnis `C:\Photos` Um die `MD5 hash` dieser Datei mit PowerShell, führen Sie den folgenden Befehl aus:

```powershell
Get-FileHash -Algorithm MD5 -Path "C:\Photos\image.jpg"
```

Auf dem Terminal wird der MD5-Hashwert der Datei angezeigt.

### Beispiel 3: Abrufen des SHA1-Hashwerts

Stellen Sie sich ein Szenario vor, in dem Sie eine Datei mit dem Namen `data.txt` in dem Verzeichnis `C:\Documents` Um die `SHA1 hash` dieser Datei mit PowerShell, führen Sie den folgenden Befehl aus:

```powershell
Get-FileHash -Algorithm SHA1 -Path "C:\Documents\data.txt"
```

In der Ausgabe wird der SHA1-Hash-Wert der Datei angezeigt.