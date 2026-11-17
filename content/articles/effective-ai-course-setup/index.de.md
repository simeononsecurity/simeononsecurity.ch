---
title: "Einrichtung des KI-Workflow-Kurses: Terminal, Git und Übungslabor"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Richte einen sicheren Übungsbereich für KI ein, lerne die im Kurs verwendeten Terminal- und Git-Begriffe und starte das Einstiegslabor."
genre: ["Künstliche Intelligenz", "Softwareentwicklung", "Bildung"]
tags: ["KI-Kurseinrichtung", "Terminal-Grundlagen", "Git-Grundlagen", "Voraussetzungen für Coding-Agenten", "KI-Übungslabor", "KI-Kurs für Einsteiger"]
cover: "/img/cover/effective-ai-course-setup.webp"
coverAlt: "Übungsbereich für Einsteiger mit Terminal-, Python- und Git-Symbolen, markiertem Laborordner und Archiv zum Zurücksetzen"
coverCaption: ""
---

[Zurück zum praktischen KI-Workflow-Kurs](/effective-ai-course-start/)

**Richte einen sicheren Übungsbereich ein, bevor du einen Agenten verwendest.** Lektion 1 und 2 funktionieren ohne dieses Labor im Browser. Kehre vor Lektion 3 hierher zurück, wenn du den vollständigen Kurs absolvieren möchtest. Für die praktischen Programmierlektionen brauchst du Git, Python 3.10 oder neuer und einen Coding-Agenten. Im Studienpfad ersetzen gekennzeichnete manuelle Aufgaben nicht verfügbare Agentenaktionen.

**Lernziel:** Du führst das Einstiegslabor aus, speicherst einen lokalen Ausgangsstand und erklärst, wie du eine entbehrliche Kopie zurücksetzt.

## Wichtigste Erkenntnisse

- **Browserpfad:** Bearbeite Chat-, Planungs-, Quellenprüfungs- und Review-Übungen in ChatGPT oder Claude.
- **Lokaler Pfad:** Verwende für Programmierübungen ein Terminal und das bereitgestellte Python-Labor.
- **Zurücksetzen:** Entpacke eine neue Laborkopie, wenn eine Übung schiefgeht.
- **Sicherheitsregel:** Private Dateien, Kundendaten und Zugangsdaten gehören nicht ins Labor.

## Wähle deinen Pfad

| Pfad | Voraussetzungen | Übungen |
|---|---|---|
| **Einführung im Browser** | Aktueller Browser und ChatGPT- oder Claude-Konto | Lektionen 1 und 2 sowie das Chat-Aufgabenpaket aus Lektion 1 |
| **Praktisches Arbeiten lokal** | Git, Python 3.10 oder neuer, Terminal und ein Coding-Agent | Dateien, Diffs, Tests und Änderungen des Agenten |
| **Studienkurs** | Browser, lokales Python 3.10 oder neuer und Git | Vollständige Laborprüfungen; nicht verfügbare Agenten- und MCP-Schritte sind als nicht ausgeführt markiert |

**Angebote und Limits legt jedes Produkt selbst fest.** Prüfe [ChatGPT Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) und [Claude Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects), bevor du dich auf eine Funktion verlässt. Der Studienpfad belegt keine praktische Fähigkeit mit einem nicht verfügbaren Coding-Agenten. Halte diesen Unterschied in deinen Abschlussnotizen fest.

**Nutze einen Standardpfad:** ChatGPT im Browser für Chatübungen, danach einen verfügbaren Coding-Agenten mit dem lokalen Labor. Claude ist eine gleichwertige Chat-Option. Für die Programmierphase stehen Codex CLI, Claude Code CLI und OpenCode zur Wahl. Du brauchst keine Konten bei allen Anbietern.

**Notiere fünf Vorabprüfungen, bevor du einen Coding-Agenten öffnest.** So unterscheidest du eine lokale Laborprüfung von einer Aussage über ein Konto oder einen gehosteten Arbeitsbereich.

| Prüfung | Notiz |
|---|---|
| **Arbeitsbereich** | Exakter entpackter Laborordner, den der Agent lesen soll |
| **Ausführung** | Lokaler Computer oder ausgewählter Remote-Arbeitsbereich |
| **Anbieter** | Für diese Aufgabe verwendetes Konto oder Modellanbieter |
| **Berechtigungen** | Ob Dateischreibzugriffe und Shell-Befehle erlaubt sind oder eine Freigabe brauchen |
| **Ausgangsstand** | Beobachtete Anzahl und zwei bestandene Tests vor Änderungen |

**Halte das Übungs-Stammverzeichnis eng begrenzt.** Ein gehosteter Arbeitsbereich braucht eine eigene Kopie des synthetischen Labors. Ein lokaler Lauf beweist nicht, dass die Remote-Kopie oder das Konto dieselben Dateien und Berechtigungen besitzt.

## Lokale Begriffe verstehen

| Begriff | Einfache Bedeutung |
|---|---|
| **Terminal** | App, in der du Befehle eingibst |
| **Shell** | Software, die diese Befehle interpretiert |
| **CLI** | Kommandozeilenschnittstelle zu einem Programm |
| **Arbeitsverzeichnis** | Ordner, den ein Befehl standardmäßig verwendet |
| **Repository** | Von Git nachverfolgtes Projekt |
| **Commit** | Gespeicherter Git-Schnappschuss |
| **Branch** | Benannter Entwicklungszweig für Git-Änderungen |
| **Diff** | Anzeige hinzugefügter oder entfernter Zeilen |
| **Prüfung** | Wiederholbare Prüfung des erwarteten Verhaltens |
| **Exit-Code** | Zahl, die Erfolg oder Fehlschlag eines Befehls meldet |

**Für das Einstiegslabor brauchst du GitHub nicht.** Git läuft auf deinem Computer. GitHub ist ein separater Hosting-Dienst. Ein lokaler Commit speichert einen Stand, ohne deine Dateien irgendwohin zu senden.

## Das Labor vorbereiten

**Lade das [Kurs-Einstiegslabor](/downloads/effective-ai-course-lab.zip) herunter** und entpacke es in einen neuen Ordner, den du kontrollierst. Öffne dort ein Terminal. Auf macOS oder Linux öffnest du Terminal und wechselst mit `cd` in den entpackten Ordner. Unter Windows verwendest du PowerShell oder Windows Terminal und ebenfalls `cd`. Unter Windows heißt der Python-Befehl oft `py -3` statt `python3`.

**Installiere bei Bedarf [Python 3.10 oder neuer](https://www.python.org/downloads/) und [Git](https://git-scm.com/downloads).** Prüfe die installierten Werkzeuge vor dem Laborlauf. Die ersten beiden Befehle geben Versionsnummern aus. `cd` wechselt das Arbeitsverzeichnis. `ls` listet Dateien auf. Ersetze den Beispielpfad durch den tatsächlichen Pfad deines entpackten Ordners.

```bash
python3 --version
git --version
cd /path/to/effective-ai-course-lab
ls
```

**In Windows PowerShell** verwendest du `py -3 --version`, `git --version`, `cd C:\path\to\effective-ai-course-lab` und `Get-ChildItem`. Die Liste sollte `task_report.py`, `tasks.json`, `tests` und `docs` enthalten. Schlägt ein Versionsbefehl fehl, schließe erst die Installation ab.

```bash
pwd
python3 task_report.py tasks.json
python3 -m unittest discover -s tests -v
```

**In Windows PowerShell** kannst du `pwd` durch `Get-Location` ersetzen und `python3` durch `py -3`, wenn Python den Launcher verwendet. Der erste Befehl zeigt den Pfad; er sollte auf deinen entpackten Laborordner enden. Prüfe auch die Dateinamen. Eine Datei namens `AGENTS.md.txt` ersetzt keine `AGENTS.md`. Aktiviere im Windows-Explorer die Dateinamenerweiterungen, damit du den vollständigen Namen siehst.

**Erwartete Ausgabe:** Der Bericht nennt `Total tasks: 4`. Der Testbefehl führt zwei Tests auf und endet mit `OK`. Eine Shell liefert bei Erfolg den Exit-Code null. Eine andere Anzahl oder ein Traceback bedeutet, dass du Ordner und Python-Einrichtung prüfen solltest.

**Lies Befehle in ihren Bestandteilen.** In `python3 task_report.py tasks.json` startet `python3` Python, `task_report.py` ist das Programm und `tasks.json` benennt die Eingabedaten. Die ausgegebene Anzahl ist eine Ausgabe, kein weiterer Befehl. Nach einem Fehler zeigen macOS und Linux den Status mit `echo $?`. PowerShell stellt den Status des letzten nativen Programms über `$LASTEXITCODE` bereit.

**Plane nach der Python-Installation etwa zehn Minuten für den ersten Lauf ein:** Entpacke das Labor, führe den Bericht aus und vergleiche die Anzahl mit den vier Einträgen in `tasks.json`. Öffne die JSON-Datei in einem Texteditor und zähle die Einträge selbst.

## Git sicher üben

**Starte Git nur im entpackten Laborordner.** Die Befehle speichern einen lokalen Stand. `git status` zeigt geänderte Dateien. `git diff` zeigt geänderte Zeilen, nachdem du eine nachverfolgte Datei bearbeitet hast.

```bash
git init
git add .
git commit -m "Kurslabor-Basisstand"
git status --short
```

**Erwarteter Status:** Nach dem Commit erscheinen keine Dateinamen. Fragt Git nach Name und E-Mail, richte in diesem Ordner eine nur für das Labor bestimmte Identität ein und wiederhole den Commit. Ersetze die Beispielwerte durch private Werte. Füge Identitäts- oder Zugangsdaten-Ausgaben nicht in einen öffentlichen Chat ein.

```bash
git config --local user.name "Kursteilnehmer"
git config --local user.email "learner@example.invalid"
git commit -m "Kurslabor-Basisstand"
git status --short
```

**Zum Zurücksetzen brauchst du keinen Git-Befehl.** Speichere deine Notizen außerhalb des Labors, lösche die entpackte Übungskopie und entpacke die ursprüngliche ZIP-Datei erneut. Nutze das, wenn eine Änderung aus einer Lektion das Programm in einen unbekannten Zustand versetzt.

## Deinen Übungsbereich schützen

**Verwende synthetische Beispiele.** Lade keine privaten Dokumente in ein Kursprojekt hoch. Füge keine API-Schlüssel in Prompts, Quelldateien, Screenshots oder Commits ein. Der Datei- und Befehlszugriff eines Coding-Agenten hängt von seinen Berechtigungen und dem geöffneten Ordner ab. Prüfe beides, bevor du ihn ausführen lässt.

**Prüfe die Freigabe vor dem Hochladen.** Projektdateien können für Projektmitglieder verfügbar sein. Befolge bei echter Arbeit die Richtlinien deiner Organisation. Der Kurs verwendet fiktive Daten, daher ist für das Labor keine besondere Freigabe nötig.

## Üben und prüfen

**Dein Ergebnis:** Notiere den gewählten Pfad, die fünf Vorabfelder, die Anzahl im Bericht, das Testergebnis und die Zurücksetzmethode. Verwende eine frische Laborkopie, um das Zurücksetzen zu üben.

**Erwartetes Verständnis:** Du weißt, welcher Ordner von Befehlen betroffen ist, unterscheidest lokales Git von Hosting und kennst eine Wiederherstellungsmöglichkeit, bevor ein Agent Dateien ändert.

## Verständnis prüfen

1. **Frage:** Schließt eine reine Browser-Einführung den lokalen Laborpfad ab? **Antwort:** Nein. Der vollständige Pfad setzt eine lokale Python- und Git-Ausgangsbasis voraus.

2. **Frage:** Was solltest du speichern, bevor du das entbehrliche Labor änderst? **Antwort:** Das bestandene Ergebnis des Starttests und einen sauberen Ausgangspunkt zum Zurücksetzen.

## Fehlerbehebung

- **Python-Befehl fehlt:** Installiere Python 3 über den offiziellen Anbieter und öffne das Terminal erneut.
- **Datei nicht gefunden:** Prüfe das Arbeitsverzeichnis und liste die Dateien im entpackten Ordner auf.
- **Tests starten nicht:** Verwende genau den Befehl aus der README-Datei des entpackten Labors.
- **Git verlangt eine Commit-Identität:** Richte Git lokal ein und halte die gewählten Werte aus den Kursnotizen heraus.

## Nächste Schritte

**Fahre mit dem [zuverlässigen KI-Workflow](/articles/effective-ai-workflow-foundations/) fort.** Die erste Übung verwendet dieselbe synthetische Werkstatt, bevor ein Werkzeug echte Dateien erhält.

**Kursnavigation:** [Kursübersicht](/effective-ai-course-start/).
