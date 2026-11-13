---
title: "Wiederherstellung einer Homelab-Sicherung mit Restic testen"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Prüfe, ob eine Homelab-Sicherung nutzbare Dateien wiederherstellt. Lege ein Wiederherstellungsziel fest, spiele die Daten mit Restic an einem anderen Ort ein, prüfe sie und protokolliere das Ergebnis."
genre: ["Homelab", "Datensicherung", "Notfallwiederherstellung"]
tags: ["Homelab-Sicherung", "Wiederherstellungstest", "Restic-Wiederherstellung", "Sicherungsprüfung", "Wiederherstellungstest", "Notfallwiederherstellung", "RPO", "RTO", "Sicherungs-Repository", "Restic-Prüfung", "NAS-Sicherung", "Serversicherung", "VM-Wiederherstellung", "Dateiwiederherstellung", "Sicherungsverschlüsselung", "Sicherungsüberwachung", "Wiederherstellungsplan", "Sicherungstest", "externe Sicherung", "Datenintegrität"]
cover: "/img/cover/homelab-backup-restore-drill.webp"
coverAlt: "Ein Homelab-Server und ein NAS sichern Daten auf ein separates Laufwerk. Ein verifizierter Wiederherstellungsordner liegt auf einem isolierten Testcomputer, daneben eine Stoppuhr."
coverCaption: "Stelle Daten an einem separaten Ziel wieder her, prüfe sie und miss die benötigte Zeit."
---

Ein Sicherungsauftrag mit Erfolgsmeldung beweist nicht, dass du eine nutzbare Datei wiederherstellen kannst. Ein **Wiederherstellungstest** prüft den Weg von den gespeicherten Sicherungsdaten zu nutzbaren Daten, ohne deine aktiven Dateien zu ersetzen. Diese Anleitung zeigt eine dateibasierte Wiederherstellung mit Restic und enthält ein Protokoll, das du nach Änderungen am Labor erneut ausfüllen kannst.

<!--more-->

Restic ist ein Sicherungsprogramm. Ein **Repository** ist der geschützte Speicherbereich mit den Sicherungsdaten. Ein **Snapshot** ist ein gespeicherter Sicherungszeitpunkt.

## Wichtigste Erkenntnisse

- **Lege ein Ziel fest:** Bestimme die benötigten Dateien oder Dienste und einen akzeptablen Wiederherstellungszeitpunkt sowie eine akzeptable Dauer.
- **Stelle separat wieder her:** Nutze ein leeres Testziel, damit der Test keine aktiven Daten überschreibt.
- **Prüfe das Ergebnis:** Öffne wiederhergestellte Dateien, prüfe nach Möglichkeit Anwendungsdaten und miss die verstrichene Zeit.
- **Protokolliere Fehler:** Halte Snapshot-ID, fehlende Elemente, Berechtigungen und Reparaturen im Wiederherstellungsplan fest.

## Vor dem Start

Du benötigst ein funktionsfähiges Sicherungs-Repository, dessen Passwort oder Schlüssel, ausreichend freien Platz am Ziel sowie Leseberechtigungen für Sicherung und Testort. Das Beispiel setzt voraus, dass Restic installiert ist und das Repository eine aktuelle Dateisicherung enthält. Die [Restic-Schnellstartanleitung](https://restic.readthedocs.io/en/stable/010_introduction.html) erklärt das Anlegen eines Repositorys und die ersten Sicherungen. Der [3-2-1-Sicherungsleitfaden](/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/) der Website behandelt die Ablage der Kopien. Die [Homelab-Übersicht](/articles/what-is-a-homelab-and-should-you-have-one/) enthält eine kurze Prüfliste für Sicherungen.

Dieser Test prüft Dateien in einem Snapshot. Eine Datenbank, virtuelle Maschine oder Anwendung benötigt eigene Wiederherstellungsschritte. Halte das Testsystem isoliert, wenn ein Start des wiederhergestellten Dienstes den aktiven Dienst beeinträchtigen könnte. Eine erfolgreiche Dateikopie beweist nicht, dass alle Dienste starten.

> **Warnung:** Stelle beim ersten Test nicht in einen aktiven Pfad wieder her. Nutze ein leeres Testverzeichnis auf einem separaten Dateisystem oder Testhost. Das Repository-Passwort gehört weder in Screenshots und Tickets noch in den Shell-Verlauf.

## Wiederherstellungsziel festlegen

Notiere, was du nach einem Ausfall benötigst. Das **Wiederherstellungspunktziel (RPO)** bezeichnet den Zeitpunkt, bis zu dem Daten nach einer Unterbrechung wiederhergestellt sein müssen. Es beschreibt den maximal akzeptablen Datenverlust. Das **Wiederherstellungszeitziel (RTO)** gibt an, wie lange ein Dienst ausfallen darf. NIST definiert beide in seinem [Leitfaden zur Notfallplanung](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-34r1.pdf). Deine Ziele sollten berücksichtigen, wie oft sich Daten ändern und wie lange eine Wiederherstellung auf deiner Hardware dauert.

| Element | Beispielziel | Zu protokollieren |
|---|---|---|
| **Familiendokumente** | Letzte nächtliche Sicherung | Zeitpunkt des letzten Snapshots und geöffnete Dateien |
| **Konfiguration eines Heimdienstes** | Letzte bekanntermaßen gute Änderung | Konfigurationsversion und erforderliche Geheimnisse |
| **Medienbibliothek auf einem netzgebundenen Speicher (NAS)** | Wöchentliche Sicherung | Testwiedergabe und Wiederherstellungszeit |

Die Ziele oben sind Beispiele, keine Messwerte. Notiere im Wiederherstellungsplan den Speicherort der Sicherung und wie eine berechtigte Person das Repository-Passwort oder den Verschlüsselungsschlüssel erhält. Trage keine geheimen Werte in Plan oder Testprotokoll ein. Bewahre Geheimnisse über einen geschützten Weg auf, der unabhängig vom ausgefallenen Host funktioniert. Ein überlebendes Repository ohne sein einziges Passwort ist nicht wiederherstellbar.

Wähle für diesen Test einen **kritischen Dateisatz** aus. Füge eine kleine Datei hinzu, die nachweislich im neuesten Snapshot liegen sollte. Liste für einen Dienst zusätzlich Konfiguration, Datenbankexport, Zertifikate und Anwendungsversion auf, die zum Start benötigt werden. Prüfe, ob deine Sicherungsmethode konsistente Anwendungsdaten erfasst, bevor du dich auf eine Dateikopie einer laufenden Datenbank verlässt.

## Snapshot finden

Nutze den für den Wiederherstellungstest freigegebenen Repository-Zugriff. Restic setzt beim Lesen oder Ändern von Sicherungsdaten eine temporäre Repository-Sperre. Die folgenden Befehle setzen voraus, dass das Repository diese Sperre zulässt. Halte aktive Quelle und Testziel getrennt. Ersetze `/path/to/repository` durch den tatsächlichen Restic-Repository-Pfad und liste die Snapshots auf:

```bash
restic -r /path/to/repository snapshots
```

Restic fragt nach dem Repository-Passwort, wenn du es nicht über einen eingerichteten Geheimnisdienst bereitgestellt hast. Die [Snapshot-Liste](https://restic.readthedocs.io/en/stable/010_introduction.html) zeigt ID, Datum, Host und Quellpfade. Notiere ID und Zeitstempel des Snapshots, den du testen willst. Vergleiche den Zeitstempel mit deinem RPO. Ein aktuelles Auftragsprotokoll ersetzt diese Prüfung nicht, denn der benötigte Snapshot ist womöglich älter als gedacht.

Fehlt der erwartete Snapshot, beende den Test und untersuche Sicherungszeitplan, Quellauswahl und Repository-Pfad. Wähle nicht stillschweigend einen älteren Snapshot aus und melde das Wiederherstellungsziel als erfüllt.

## In ein leeres Testziel wiederherstellen

Erstelle auf einem Testdateisystem mit genügend Platz für den Snapshot ein **leeres Zielverzeichnis**. Verwende weder die ursprüngliche Quelle noch eine eingebundene Produktionsfreigabe oder einen vorhandenen Ordner mit zu erhaltenden Daten als Restic-Ziel. Ersetze `SNAPSHOT_ID` und beide Beispielpfade vor dem Befehl:

```bash
restic -r /path/to/repository restore SNAPSHOT_ID \
  --target /path/to/empty-restore-drill
```

Der [Restic-Wiederherstellungsleitfaden](https://restic.readthedocs.io/en/stable/050_restore.html) erläutert Snapshot-ID und `--target`-Pfad. Der wiederhergestellte Verzeichnisbaum behält den Quellpfad unter dem Zielverzeichnis bei. Suche deshalb die tatsächlichen Dateien, bevor du das Ergebnis bewertest. Wenn du nur eine kleine Teilmenge benötigst, verwende die dokumentierten [Einschlussfilter für Wiederherstellungen](https://restic.readthedocs.io/en/stable/050_restore.html) und notiere die ausgeschlossenen Dateien. Nutze `--delete` nicht bei einem Test. Laut Restic entfernt diese Option Dateien am Ziel, die im Snapshot fehlen.

Starte die Zeitmessung mit Beginn der Wiederherstellung. Beende sie erst, wenn die erforderlichen Dateien vorhanden und nutzbar sind, nicht wenn der Befehl erstmals Fortschritt meldet. Notiere Repository-Ort, Netzwerkverbindung, Datenumfang und Testhost, da diese Bedingungen eine spätere Wiederherstellung beeinflussen.

> **Erwartetes Ergebnis:** Der ausgewählte Snapshot wird in ein separates Ziel eingespielt, ohne die aktive Quelle zu verändern.

## Daten und Dienst prüfen

Öffne einige wiederhergestellte Dateien mit der Anwendung, die sie normalerweise liest. Nimm eine aktuelle, eine ältere und eine Datei aus einem verschachtelten Verzeichnis. Vergleiche bekannte Größen oder Prüfsummen, falls du sie vor der Sicherung gespeichert hast. Prüfe unter Linux Eigentümer und Rechte, denn eine für das Testkonto lesbare Datei kann für das Dienstkonto unbrauchbar sein.

Stelle einen Dienst in einer isolierten Testinstanz wieder her. Prüfe Konfiguration, benötigte Geheimnisse, Datenbankkonsistenz, Start und eine typische Benutzeraktion. Eine Dateiwiederherstellung ohne Datenbank oder Geheimnis ist keine vollständige Dienstwiederherstellung. Starte die Testinstanz niemals mit der aktiven Datenbank oder Produktionsadresse, solange kein kontrollierter Umschaltplan besteht.

Führe nach dem Beispiel-Restore die Repository-Prüfung von Restic aus:

```bash
restic -r /path/to/repository check
```

Für einen vollständigen Datenlesetest führe `check --read-data` während eines Wartungsfensters aus. Restic weist darauf hin, dass der Befehl das ganze Repository liest und bei einem entfernten Backend viele Daten herunterladen kann. Der [Restic-Leitfaden zur Fehlerbehebung](https://restic.readthedocs.io/en/stable/077_troubleshooting.html) beschreibt die Prüfung und ihren Aufwand. Eine fehlerfreie Prüfung schafft Vertrauen, ersetzt aber weder das Öffnen wiederhergestellter Dateien noch den Dienststart.

```bash
restic -r /path/to/repository check --read-data
```

Vergleiche das Snapshot-Alter mit deinem RPO und die gemessene Wiederherstellungszeit mit deinem RTO. Wird eines der Ziele verfehlt, ist der Test gescheitert, auch wenn Restic fehlerfrei beendet wurde. Passe Sicherungshäufigkeit, Speicherort, Bandbreite oder Wiederherstellungsverfahren an und teste erneut.

## Wiederherstellung protokollieren

Erstelle nach jedem Test ein kurzes Protokoll. Die [Sicherungskontrolle SP 800-53](https://csrc.nist.gov/CSRC/media/Projects/risk-management/800-53%20Downloads/800-53r5/SP_800-53_v5_1-derived-OSCAL.pdf) von NIST nennt die Wiederherstellung ausgewählter Systemfunktionen als Möglichkeit, eine Wiederherstellung zu testen. Ein wiederholbares Protokoll zeigt, ob sich der Plan verbessert.

| Feld | Einzutragendes Ergebnis |
|---|---|
| **Datum und Bedienperson** | Zeitpunkt des Tests und ausführende Person |
| **Repository und Snapshot** | Speicherort, ID, Zeitstempel und Quellpfade |
| **Wiederherstellungsziel** | Geprüfte Dateien oder Dienste sowie RPO und RTO |
| **Messwerte** | Snapshot-Alter, Restore-Zeit und Datei- oder Dienstprüfungen |
| **Fehler** | Fehlende Daten, Schlüsselzugriff, Rechte, Netzwerk oder Startprobleme |
| **Nächster Schritt** | Zuständige Person, Reparatur und nächster Testtermin |

Trage weder Repository-Passwort noch Wiederherstellungsschlüssel oder sensible Dateiinhalte in das Protokoll ein. Bewahre sie in einem geschützten Geheimnisspeicher auf und dokumentiere, wie eine berechtigte Person während eines Ausfalls darauf zugreift.

## Fehlerbehebung

- **Passwort nicht verfügbar:** Prüfe den unabhängigen Schlüsselverwahrungsweg. Gehe nicht davon aus, dass der ausgefallene Host seinen eigenen Schlüssel bereitstellt.
- **Snapshot zu alt:** Prüfe Zeitplan, fehlgeschlagene Aufträge, Quellpfade und ob der erwartete Host in ein anderes Repository gesichert hat.
- **Wiederherstellung zu langsam:** Miss Lesegeschwindigkeit des Speichers, Netzwerkverbindung und Datenmenge. Teste eine kleinere kritische Teilmenge und überarbeite anschließend RTO oder Wiederherstellungsdesign.
- **Datei vorhanden, Dienst fehlerhaft:** Prüfe Datenbankexporte, Anwendungsversion, Eigentümer, Rechte, Zertifikate und fehlende Geheimnisse.
- **Repository-Prüfung meldet Fehler:** Sichere die Ausgabe und nach Möglichkeit eine Kopie des Repositorys. Folge Restics Anleitung zur [Schadensanalyse](https://restic.readthedocs.io/en/stable/077_troubleshooting.html), bevor du Reparaturen versuchst.
- **Test hat aktive Daten geändert:** Stoppe den Testdienst, prüfe Produktionsdaten und verbessere den Isolationsplan vor dem nächsten Versuch.

## Nächste Schritte

Wiederhole den Test nach Änderungen an Sicherungssoftware, Speicher, Verschlüsselungsschlüsseln oder kritischen Diensten. Wechsle mit der Zeit zwischen verschiedenen Dateisätzen und einer vollständigen Dienstwiederherstellung. Bewahre eine unabhängige Sicherung gemäß deinem [3-2-1-Plan](/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/) auf. Ziel ist eine gemessene Wiederherstellung, die du wiederholen kannst, wenn der ursprüngliche Host ausgefallen ist.
