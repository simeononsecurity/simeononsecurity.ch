---
title: "Automated Branding for Windows Systems - Easily Control Desktop, Lock Screen, and More"
date: 2020-08-14T14:37:16-05:00
toc: true
draft: false
description: "Control desktop wallpaper, users avatar, lock screen, and OEM logo with ease on Windows 10 and Server systems using a partially automated script."
tags: ["Automation", "Branding", "Windows Branding", "Customization", "Windows Customization", "Windows 10", "Windows Server 2016", "Windows Server 2019", "Powershell", "Script", "Windows System Branding", "Desktop Wallpaper", "Users Avatar", "Windows Lock Screen", "OEM Logo", "Microsoft Security Compliance Toolkit 1.0", "Organization Branding", "System Customization", "IT Automation", "Security Compliance"]
---
```
.\sos-copybranding.ps1
```

  Viele Organisationen müssen das Branding eines Windows-Systems steuern oder es kontrollieren möchten. Dazu gehören das Desktop-Hintergrundbild, der Benutzer-Avatar, der Windows-Sperrbildschirm und manchmal das OEM-Logo. Bei Windows 10, Windows Server 2016 und Windows Server 2019 ist das nicht besonders einfach. Aber mit Hilfe des verlinkten Skripts können wir es teilweise automatisieren und den Prozess viel einfacher machen.  ## Laden Sie die erforderlichen Dateien herunter  **Laden Sie die erforderlichen Dateien aus dem [GitHub-Repository] herunter (https://github.com/simeononsecurity/Windows-Branding-Script)**  ## So richten Sie die Branding-Dateien ein  - [X] Ersetzen Sie alle Bilder durch Ihre Branding-Bilder   - [X] OEM-Logo muss entweder 95 x 95 oder 120 x 20 und im ".bmp"-Format sein   - [X] Generieren Sie das Benutzerbild zusammen mit den Varianten 32x32, 40x40, 48x48, 192x192.   - [X] Benutzerbild für Gastbild erstellen oder kopieren.  ## So führen Sie das Skript aus  ## Dieses Skript verwendet das folgende Tool:  - [Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)