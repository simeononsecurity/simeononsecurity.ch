---
title: "Standalone-Windows-STIG-Script: Einen STIG-konformen PC erstellen"
date: 2023-02-02
toc: true
draft: false
description: "Schritt-für-Schritt-Anleitung zur Verwendung des Standalone-Windows-STIG-Script für Windows-Systeme, mit Erläuterungen zu Parametern und Prüfung."
tags: ["STIG-Skript", "Windows-Sicherheit", "STIG-konformes Windows-System", "Systemhärtung", "Windows STIG", "Windows-Sicherheit", "Windows-Compliance", "Manuelle Installation", "Windows-Updates", "Adobe Reader", "Firefox", "Chrome", "Internet Explorer 11", ".NET Framework", "Office", "OneDrive", "Java", "Windows Defender", "Windows-Firewall", "Gegenmaßnahmen", "Nessus PID", "VMware Horizon", "Optionale Härtung"]
cover: "/img/cover/create-compliant-windows-desktop-systems-with-standalone-windows-stig-script.webp"
coverAlt: "Eine Illustration eines Computerbildschirms mit einer Sicherheits-Compliance-Oberfläche, dynamischen Fortschrittsbalken und Datenströmen auf dunkelblauem Hintergrund mit leuchtenden Akzentfarben."
coverCaption: ""
lastmod: 2026-11-09
---

Windows-Systeme sind in Unternehmen, Organisationen und sogar zu Hause weit verbreitet. Angesichts der zunehmenden Zahl von Cyberangriffen ist es von entscheidender Bedeutung, sicherzustellen, dass diese Systeme sicher sind und den Branchenstandards entsprechen. Das Standalone-Windows-STIG-Skript ist ein nützliches Tool, das Ihnen dabei hilft, genau das zu erreichen. In diesem Artikel erfahren Sie, was das Standalone-Windows-STIG-Skript ist, wie es funktioniert und wie Sie es verwenden können, um ein sicheres und konformes Windows-System zu erstellen.

## Was ist Standalone-Windows-STIG-Skript?

**Standalone-Windows-STIG-Script** ist ein von Simeononsecurity entwickeltes Skript, das dazu dient, den Prozess der Erstellung eines sicheren und mit dem Security Technical Implementation Guide (STIG) konformen Windows-Systems zu automatisieren. Das Skript ist Open-Source und auf **GitHub** verfügbar.

## Wie funktioniert es?

Das Standalone-Windows-STIG-Skript implementiert die im STIG enthaltenen Richtlinien zur Sicherung eines Windows-Systems. Das Skript kann auf einem Windows-System ausgeführt werden und nimmt die notwendigen Änderungen am System vor, um die Einhaltung der STIG zu gewährleisten. Das Skript deckt eine breite Palette von Sicherheitsmaßnahmen ab, einschließlich, aber nicht beschränkt auf die folgenden:

- Kontorichtlinien
- Audit-Richtlinien
- Sicherheitsoptionen
- Firewall-Einstellungen
- Service-Einstellungen

## Vorteile der Verwendung von Standalone-Windows-STIG-Script:

- **Automatisierung**: Das Skript automatisiert den Prozess der Sicherung eines Windows-Systems, was Zeit spart und die Möglichkeit menschlicher Fehler ausschließt.

- **Konformität**: Das Skript setzt die Richtlinien der STIG um und stellt sicher, dass das Windows-System mit den Industriestandards übereinstimmt.

- **Sicherheit**: Durch die Verwendung des Standalone-Windows-STIG-Skripts können Sie sich darauf verlassen, dass Ihr Windows-System sicher ist und den Industriestandards entspricht.

_________________________________________________________________________________________________________________________

## So verwenden Sie Standalone-Windows-STIG-Skript:

1. Die Verwendung des Standalone-Windows-STIG-Skripts ist relativ einfach. Im Folgenden werden die Schritte zur Verwendung des Skripts beschrieben:

2. **Downloaden Sie das Skript**: Das Skript ist auf GitHub unter https://github.com/simeononsecurity/Standalone-Windows-STIG-Script verfügbar. Laden Sie das Skript herunter und speichern Sie es auf Ihrem Windows-System.

3. **Öffnen Sie eine erweiterte Eingabeaufforderung**: Klicken Sie mit der rechten Maustaste auf die Windows-Startschaltfläche und wählen Sie "Windows PowerShell (Admin)".

4. **Ausführen des Skripts**: Navigieren Sie zu dem Ort, an dem Sie das Skript gespeichert haben, und führen Sie das Skript aus, indem Sie den folgenden Befehl eingeben:

```powershell
powershell.exe -ExecutionPolicy Bypass -File Standalone-Windows-STIG-Script.ps1
```

5. Überprüfen Sie die Änderungen: Nachdem das Skript ausgeführt wurde, überprüfen Sie die Änderungen, die am System vorgenommen wurden, um sicherzustellen, dass alles korrekt konfiguriert ist.

## Fazit:

Zusammenfassend lässt sich sagen, dass das Standalone-Windows-STIG-Skript ein nützliches Tool ist, das Ihnen helfen kann, Ihr Windows-System zu sichern und die Industriestandards einzuhalten. Mithilfe des Skripts können Sie den Prozess der Sicherung Ihres Windows-Systems automatisieren und sicherstellen, dass es mit der STIG konform ist, so dass Sie die Gewissheit haben, dass Ihr System sicher ist. Wenn Sie also ein konformes und sicheres Windows-System erstellen möchten, sollten Sie die Verwendung des Standalone-Windows-STIG-Skripts in Betracht ziehen.