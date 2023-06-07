---
title: "Rationalisierung von Windows-Updates durch Automatisierung mit Chocolatey, PSWindowsUpdate und Startup Scripts"
date: 2020-07-22
---
 Windows-Updates mit Chocolatey, PSWindowsUpdate und Startup-Skripten**

In der schnelllebigen Geschäftswelt von heute ist Zeit für Systemadministratoren von entscheidender Bedeutung. Die Aktualisierung von Windows-Rechnern, ein wichtiger Aspekt der Systemadministration, kann eine extrem zeitaufwändige Aufgabe sein, die bei einer ausreichenden Anzahl von Systemen bis zu einer Woche dauern kann. Mit Hilfe von Chocolatey, PSWindowsUpdates und Startup Scripts ist es nun jedoch möglich, Updates mit nur einem einzigen Neustart jedes Rechners auszuführen, wodurch sich der Zeitaufwand für die Durchführung von Updates erheblich verringert.

## Rationalisierung von Windows-Updates mit Automatisierung

Windows-Updates sind für die Aufrechterhaltung der Stabilität und Sicherheit von Windows-Rechnern von entscheidender Bedeutung. Die Durchführung von Updates auf einer großen Anzahl von Rechnern kann eine zeitraubende Aufgabe sein, insbesondere für Systemadministratoren mit begrenzten Ressourcen. Durch den Einsatz von Automatisierungstools wie Chocolatey, PSWindowsUpdate und Startup Scripts kann dieser Prozess jedoch rationalisiert werden, so dass Administratoren Updates mit minimalem Aufwand durchführen können.

### Chocolatey

[Chocolatey](https://chocolatey.org/) ist ein Paketmanager für Windows, mit dem sich die Installation von Software auf Windows-Rechnern automatisieren lässt. Er ähnelt apt-get auf Ubuntu oder homebrew auf macOS und kann zur Installation und Verwaltung einer Vielzahl von Softwarepaketen verwendet werden. Chocolatey kann verwendet werden, um Pakete im Hintergrund zu installieren, was bedeutet, dass sie ohne Benutzereingriff installiert werden können.

### PSWindowsUpdate

[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) ist ein PowerShell-Modul, das zum Automatisieren der Installation von Windows-Updates verwendet werden kann. Es bietet Cmdlets, die zum Installieren, Deinstallieren und Auflisten von Windows-Updates verwendet werden können. PSWindowsUpdate ist ein leistungsfähiges Tool, das zur Verwaltung von Windows-Updates auf mehreren Computern verwendet werden kann und somit ideal für Systemadministratoren ist, die eine große Anzahl von Computern verwalten müssen.

### Startup-Skripte

[Startup Scripts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn789190(v=ws.11)) sind Skripte, die verwendet werden können, um Aufgaben zu automatisieren, die beim Starten oder Herunterfahren eines Rechners ausgeführt werden müssen. Diese Skripte können für Aufgaben wie die Installation von Software, die Konfiguration von Einstellungen und die Verwaltung von Windows-Updates verwendet werden.

## Automatisieren von Windows-Updates mit einem einzigen Neustart

Um Windows-Updates mithilfe von Chocolatey, PSWindowsUpdate und Startup Scripts zu automatisieren, können Administratoren die folgende Schritt-für-Schritt-Anleitung befolgen.

### Einrichten des Shutdown-Skripts
Laden Sie alle unterstützenden Dateien von der [GitHub Repository](https://github.com/simeononsecurity/ChocoAutomateWindowsUpdates)

1. Öffnen Sie den Editor für lokale Gruppenrichtlinien, indem Sie **"Win + R "** drücken und **"gpedit.msc "** eingeben, gefolgt von **"Strg + Umschalt + Eingabe "**.
2. Navigieren Sie zu Computer **Konfiguration\Windows-Einstellungen\Skripte (Starten/Herunterfahren)**.
3. Doppelklicken Sie im Ergebnisbereich auf Herunterfahren.
4. Wählen Sie die Registerkarte PowerShell.
5. Klicken Sie im Dialogfeld Shutdown-Eigenschaften auf Hinzufügen.
6. Geben Sie im Feld Skriptname den Pfad zum Skript ein, oder klicken Sie auf Durchsuchen, um "*chocoautomatewindowsupdates.ps1*" im freigegebenen Netlogon-Ordner auf dem Domänencontroller zu suchen.
7. Starten Sie neu.

Jetzt muss ein Administrator nur noch den Computer neu starten, um Windows-Updates durchzuführen.

### Das Skript verstehen

Das Skript zur Automatisierung von Windows-Updates trägt den Namen "*chocoautomatewindowsupdates.ps1*". Es führt die folgenden Aufgaben aus:

1. Installiert den Chocolatey-Paketmanager.
2. Ermöglicht eine Reihe von bevorzugten Chocolatey-Konfigurationsänderungen.
3. Aktualisiert alle installierten Chocolatey-Pakete.
4. Installiert das PSWindowsUpdate PowerShell-Modul.
5. Fügt den Windows Update-Dienstmanager hinzu.
6. Installiert alle verfügbaren Windows-Updates.
7. Installiert alle fehlenden Treiber oder Updates, die für zuvor installierte Updates erforderlich sind.

### Vorteile der Automatisierung von Windows-Updates

Die Automatisierung von Windows-Updates mithilfe von Chocolatey, PSWindowsUpdate und Startup Scripts hat für Systemadministratoren mehrere Vorteile. Zu diesen Vorteilen gehören:

- **Zeitersparnis**: Durch die Automatisierung von Windows-Updates wird der Zeitaufwand für die Durchführung von Updates erheblich reduziert. Administratoren müssen Updates nicht mehr manuell auf jedem Rechner installieren.
- **Konsistenz**: Durch die Automatisierung von Windows-Updates wird sichergestellt, dass die Updates auf allen Rechnern einheitlich installiert werden. Dadurch wird die Wahrscheinlichkeit von Fehlern und Sicherheitslücken verringert.
- **Zentrale Verwaltung**: Durch die Automatisierung von Windows-Updates können Administratoren die Updates von einer zentralen Stelle aus verwalten, so dass es einfacher ist, den Überblick darüber zu behalten, welche Updates installiert wurden und welche Computer Updates benötigen.
- **Erhöhte Sicherheit**: Durch die Automatisierung von Windows-Updates wird sichergestellt, dass die Rechner immer mit den neuesten Sicherheits-Patches versorgt werden, wodurch das Risiko von Sicherheitsverletzungen verringert wird.

### Fazit

Die Automatisierung von Windows-Updates mithilfe von Chocolatey, PSWindowsUpdate und Startup Scripts ist ein leistungsfähiges Tool, das Systemadministratoren viel Zeit und Mühe ersparen kann. Es ermöglicht die konsistente und effiziente Installation von Updates und stellt sicher, dass die Rechner mit den neuesten Sicherheitspatches ausgestattet sind. Wenn Sie die in diesem Lernprogramm beschriebenen Schritte befolgen, können Administratoren Windows-Updates mit nur einem einzigen Neustart automatisieren und so den Prozess der Aktualisierung von Windows-Rechnern wesentlich beschleunigen und vereinfachen.
