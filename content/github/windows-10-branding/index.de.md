---
title: "Automatisches Branding für Windows-Systeme - Einfache Steuerung von Desktop, Sperrbildschirm und mehr"
date: 2020-08-14
---


Viele Unternehmen müssen oder wollen das Branding eines Windows-Systems kontrollieren.
Dazu gehören das Desktop-Hintergrundbild, der Avatar des Benutzers, der Windows-Sperrbildschirm und manchmal das OEM-Logo.
In Windows 10, Windows Server 2016 und Windows Server 2019 ist dies nicht besonders einfach.
Aber mit Hilfe des verlinkten Skripts können wir es teilweise automatisieren und den Prozess viel einfacher machen.

## Download der benötigten Dateien

**Downloaden Sie die benötigten Dateien von der [GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)

## Wie man die Branding-Dateien einrichtet

- X] Ersetzen Sie alle Bilder durch Ihre Branding-Bilder
  - X] Das OEM-Logo muss entweder 95x95 oder 120x20 groß sein und im Format ".bmp" vorliegen.
  - X] Generieren Sie das Benutzerbild zusammen mit den Varianten 32x32, 40x40, 48x48, 192x192.
  - X] Erzeugen oder kopieren Sie das Benutzerbild für das Gastbild.

## So führen Sie das Skript aus
```
.\sos-copybranding.ps1
```

## Dieses Skript verwendet das folgende Tool:

- [Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
