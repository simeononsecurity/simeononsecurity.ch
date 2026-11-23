---
title: "Einsteigerleitfaden: Linux-Kommandozeile für die Cybersicherheit"
date: 2023-03-13
lastmod: 2026-11-22
toc: true
draft: false
description: "Lernen Sie grundlegende und fortgeschrittene Linux-Befehle für die Cybersicherheit kennen."
tags: ["Linux", "Kommandozeile", "Cybersicherheit", "Einsteigerleitfaden", "Netzwerkscans", "Schwachstellentests", "Malwareanalyse", "Berechtigungen", "Netzwerkverkehr", "Prozessstatus", "Netzwerkstatistiken", "Dateisuche", "Wireshark", "TCPDump", "Nmap", "Linux-Befehlszeile", "Sicherheit", "Penetrationstests", "Digitale Forensik"]
cover: "/img/cover/a-beginners-guide-to-using-the-linux-command-line.webp"
coverAlt: "Illustration eines Computerbildschirms mit grünen Linux-Befehlen auf dunklem Hintergrund, umgeben von digitalen Schlössern und Netzwerkverbindungen."
coverCaption: ""
---

**Linux** ist ein vielseitiges und sicheres Betriebssystem. Wegen seines offenen Quellcodes wird es häufig in der Cybersicherheit eingesetzt. Für Einsteiger kann die Linux-Kommandozeile (CLI) zur Ausführung von Sicherheitsaufgaben jedoch einschüchternd wirken. Dieser Leitfaden stellt grundlegende und fortgeschrittene Linux-CLI-Befehle für die Cybersicherheit vor.

## Grundlegende Linux-Befehle für die Cybersicherheit

### Arbeitsverzeichnis anzeigen

Der Befehl **pwd** (aktuelles Arbeitsverzeichnis anzeigen) zeigt das aktuelle Arbeitsverzeichnis in der CLI an. Das ist das Verzeichnis, in dem Sie sich gerade im Dateisystem befinden. Der Befehl hilft bei der Navigation und zeigt Ihren Standort im Verhältnis zu anderen Verzeichnissen. Wenn Sie sich beispielsweise im Home-Verzeichnis befinden und zum Dokumentenverzeichnis wechseln möchten, verwenden Sie diese Befehle:

```bash
$ pwd
/home/user
$ cd documents
$ pwd
/home/user/documents
```

Im obigen Beispiel zeigt der erste Befehl das aktuelle Arbeitsverzeichnis an, also das Home-Verzeichnis. Der zweite wechselt zum Dokumentenverzeichnis. Der dritte zeigt das neue Arbeitsverzeichnis an.

### Inhalte auflisten

Der Befehl **ls** listet den Inhalt eines Verzeichnisses in der CLI auf. Er zeigt die Namen der Dateien und Unterverzeichnisse im aktuellen Arbeitsverzeichnis an. So erkennen Sie die Dateien an einem bestimmten Speicherort. Um den Inhalt des Dokumentenverzeichnisses anzuzeigen, verwenden Sie diesen Befehl:

```bash
$ ls documents
file1.txt file2.pdf file3.docx
```

Im obigen Beispiel listet der Befehl den Inhalt des Dokumentenverzeichnisses auf. Es enthält drei Dateien: file1.txt, file2.pdf und file3.docx. Sie können den Befehl auch ohne Argumente ausführen, um den Inhalt des aktuellen Arbeitsverzeichnisses aufzulisten. Beispiel:

```bash
$ ls
Desktop Documents Downloads Music Pictures Public Templates Videos
```

Im obigen Beispiel listet der Befehl den Inhalt des Home-Verzeichnisses auf, darunter Unterverzeichnisse wie Desktop, Documents und Downloads.

### Verzeichnis wechseln

Der Befehl **cd** (Verzeichnis wechseln) wechselt das aktuelle Arbeitsverzeichnis in der CLI. Damit navigieren Sie durch das Dateisystem und greifen auf Dateien an anderen Speicherorten zu. Um zum Dokumentenverzeichnis zu wechseln, verwenden Sie diesen Befehl:

```bash
$ cd documents
```

Im obigen Beispiel wechselt der Befehl zum Dokumentenverzeichnis im aktuellen Arbeitsverzeichnis. Sie können auch einen absoluten oder relativen Pfad angeben, um in ein anderes Verzeichnis zu wechseln. Beispiel:

```bash
$ cd /usr/local/bin
```

Im obigen Beispiel wechselt der Befehl über den absoluten Pfad nach /usr/local/bin. Sie können auch einen relativen Pfad verwenden. Beispiel:

```bash
$ cd ../..
```

Im obigen Beispiel wechselt der Befehl zwei Verzeichnisebenen nach oben. Die Notation ".." steht für das übergeordnete Verzeichnis und führt im Verzeichnisbaum nach oben.

### Dateien anzeigen und verketten

Der Befehl **cat** (concatenate) zeigt den Inhalt einer Datei in der CLI an. Er eignet sich zum Lesen textbasierter Dateien wie Protokollen und Konfigurationsdateien. Um den Inhalt einer Datei namens "file1.txt" anzuzeigen, verwenden Sie diesen Befehl:

```bash
$ cat file1.txt
```

Im obigen Beispiel zeigt der Befehl den Inhalt von "file1.txt" an. Sie können ihn auch verwenden, um mehrere Dateien zu verketten und ihren Inhalt in der CLI anzuzeigen. Beispiel:

```bash
$ cat file1.txt file2.txt file3.txt
```

Im obigen Beispiel zeigt der Befehl den Inhalt von drei Dateien an: file1.txt, file2.pdf und file3.docx. Mit Platzhaltern können Sie auch alle Dateien verketten, die einem Muster entsprechen. Beispiel:

```bash
$ cat *.txt
```

Im obigen Beispiel zeigt der Befehl den Inhalt aller Dateien mit der Erweiterung ".txt" im aktuellen Arbeitsverzeichnis an. So lassen sich mehrere Dateien schnell ansehen, ohne sie einzeln zu öffnen.

### Mit regulären Ausdrücken suchen

Der Befehl **grep** (globale reguläre Ausdrücke ausgeben) sucht in einer oder mehreren Dateien nach bestimmten Zeichenfolgen oder Mustern. Er hilft beim Erkennen von Mustern in Protokollen oder beim Suchen nach Informationen in Konfigurationsdateien. Um alle Vorkommen des Worts "error" in "logfile.txt" zu suchen, verwenden Sie diesen Befehl:

```bash
$ grep "error" logfile.txt
```

Im obigen Beispiel sucht der Befehl in "logfile.txt" nach allen Vorkommen von "error" und zeigt die übereinstimmenden Zeilen an. Mit regulären Ausdrücken können Sie auch komplexere Muster suchen. Um Zeilen mit einem Wort zu finden, das mit "p" beginnt und mit "y" endet, verwenden Sie diesen Befehl:

```bash
$ grep "p.*y" logfile.txt
```

Im obigen Beispiel sucht der Befehl in "logfile.txt" nach Zeilen mit einem Wort, das mit "p" beginnt und mit "y" endet. Der reguläre Ausdruck "p.*y" entspricht jeder Zeichenfolge, die mit "p" beginnt und mit "y" endet, unabhängig von der Anzahl der Zeichen dazwischen. So finden Sie Muster in Protokollen, die auf Sicherheitsbedrohungen oder Leistungsprobleme hinweisen können.

### Berechtigungen ändern

Der Befehl **chmod** (Berechtigungsmodus ändern) ändert die Berechtigungen einer Datei oder eines Verzeichnisses in der CLI. Er ist wichtig, um Dateien und Verzeichnisse zu schützen und den Zugriff darauf zu kontrollieren. Drei Ziffern stehen für die Berechtigungen des Eigentümers, der Gruppe und der anderen Benutzer. Sie werden nach folgender Formel berechnet:

```
4 = Lesen
2 = Schreiben
1 = Ausführen
```

Um beispielsweise dem Eigentümer Lese- und Schreibrechte und der Gruppe sowie anderen Benutzern Leserechte für "file1.txt" zu geben, verwenden Sie diesen Befehl:

```bash
$ chmod 644 file1.txt
```

Im obigen Beispiel setzt der Befehl die Berechtigungen von "file1.txt" auf 644. Die erste Ziffer (6) steht für Lese- und Schreibrechte des Eigentümers (4 + 2 = 6). Die zweite Ziffer (4) gibt der Gruppe Leserechte. Die dritte Ziffer (4) gibt auch den anderen Benutzern Leserechte.

Sie können Berechtigungen auch mit Buchstaben ändern. Um dem Eigentümer und der Gruppe Lese- und Schreibrechte zu geben und alle Rechte anderer Benutzer für "file2.txt" zu entfernen, verwenden Sie diesen Befehl:

```bash
$ chmod ug=rw,o= file2.txt
```

Im obigen Beispiel setzt der Befehl die Berechtigungen von "file2.txt" auf ug=rw,o=. "ug" steht für Eigentümer und Gruppe, "r" für Lesen und "w" für Schreiben. Das Zeichen "=" setzt die Berechtigungen auf die angegebenen Werte. "o=" entfernt alle Rechte anderer Benutzer. So kontrollieren Sie den Zugriff auf vertrauliche Dateien und Verzeichnisse und verhindern unbefugten Zugriff.

## Erweiterte Linux-Befehle für die Cybersicherheit

{{< figure src="linux-cli-advanced-security-commands-overview.webp" alt="Diagramm eines Linux-Terminals mit nmap, netstat und find für Netzwerkscans, Prozessüberwachung und Dateisuche bei Sicherheitsaufgaben" >}}

### Netzwerkkartierung

Der Befehl **nmap** ist ein leistungsstarkes CLI-Werkzeug zum Scannen von Netzwerken. Er kann Hosts und Dienste in einem Netzwerk sowie mögliche Schwachstellen erkennen. Zu den Verfahren gehören Host-Erkennung, Port-Scans und Betriebssystemerkennung.

Eine einfache Verwendung von nmap ist das Scannen einer einzelnen IP-Adresse oder eines Hosts. Um offene Ports auf der IP-Adresse 192.168.1.1 zu finden, verwenden Sie diesen Befehl:

```bash
$ nmap 192.168.1.1
```

Der obige Befehl führt einen TCP-SYN-Scan gegen die Ziel-IP aus und gibt eine Liste offener Ports zurück. Die Ausgabe zeigt offene Ports, den jeweils ausgeführten Dienst und den Portstatus (offen oder geschlossen). Manchmal enthält sie zusätzliche Angaben, etwa zum Betriebssystem des Ziels.

Nmap kann mehrere Hosts oder IP-Adressen gleichzeitig scannen. Um offene Ports in einem IP-Adressbereich (192.168.1.1-255) zu finden, verwenden Sie diesen Befehl:

```bash
$ nmap 192.168.1.1-255
```

Der obige Befehl scannt alle IP-Adressen im Bereich und zeigt die offenen Ports und Dienste für jedes Ziel an.

Neben Host-Erkennung und Port-Scans kann nmap Dienste und Versionen erkennen, Betriebssysteme identifizieren und nach Schwachstellen suchen. Diese Scans helfen dabei, mögliche Sicherheitslücken im Netzwerk zu finden und es vor Angriffen zu schützen.

### TCP-Paketmitschnitt

Der Befehl **tcpdump** erfasst und analysiert den Netzwerkverkehr in der CLI. Er hilft bei der Fehlerbehebung, der Analyse des Netzwerkverhaltens und der Erkennung möglicher Sicherheitsbedrohungen. Er erfasst Pakete in Echtzeit und kann sie nach Kriterien wie Quell- oder Ziel-IP-Adresse, Protokoll und Port filtern.

Eine einfache Verwendung von tcpdump ist das Erfassen des gesamten Netzwerkverkehrs auf einer bestimmten Schnittstelle. Um den Verkehr auf eth0 mitzuschneiden, verwenden Sie diesen Befehl:

```bash
$ sudo tcpdump -i eth0
```

Der obige Befehl erfasst alle Pakete auf eth0 und zeigt sie in Echtzeit in der CLI an. Die Ausgabe enthält Quell- und Ziel-IP-Adressen, das Protokoll und weitere Informationen zu jedem Paket.

Tcpdump kann Pakete auch nach verschiedenen Kriterien filtern. Um alle Pakete zu erfassen, die an eine bestimmte IP-Adresse gesendet werden oder von ihr kommen, verwenden Sie diesen Befehl:

```bash
$ sudo tcpdump host 192.168.1.1
```

Der obige Befehl erfasst alle Pakete, die an die IP-Adresse 192.168.1.1 gesendet werden oder von ihr kommen, und zeigt sie in Echtzeit an. Sie können auch nach Protokoll (zum Beispiel TCP oder UDP), Portnummer oder anderen Kriterien filtern.

Tcpdump kann Pakete außerdem zur späteren Analyse in einer Datei speichern. Um den gesamten Verkehr auf eth0 zu erfassen und in "capture.pcap" zu speichern, verwenden Sie diesen Befehl:

```bash
$ sudo tcpdump -i eth0 -w capture.pcap
```

Der obige Befehl erfasst alle Pakete auf eth0 und speichert sie im pcap-Format in "capture.pcap". Später lassen sie sich mit Werkzeugen wie Wireshark analysieren. Das hilft, das Netzwerkverhalten zu untersuchen und mögliche Sicherheitsbedrohungen zu erkennen.

### Prozessstatus

Der Befehl **ps** zeigt in der CLI Informationen zu laufenden Prozessen auf einem Linux-System an. So lassen sich verdächtige Prozesse erkennen, die die Systemsicherheit gefährden könnten. Die Ausgabe kann Prozess-ID (PID), Benutzer, CPU- und Speichernutzung sowie den Befehlsnamen enthalten.

Eine einfache Verwendung von ps ist die Anzeige aller laufenden Prozesse. Führen Sie dazu diesen Befehl aus:

```bash
$ ps aux
```

Der obige Befehl zeigt alle laufenden Prozesse mit PID, Benutzer, CPU- und Speichernutzung sowie Befehlsnamen an. Diese Übersicht hilft, verdächtige Prozesse zu finden.

Ps kann auch Informationen zu einem bestimmten Prozess oder einer Gruppe von Prozessen anzeigen. Um Informationen zu einem Prozess mit einer bestimmten PID, zum Beispiel 1234, anzuzeigen, verwenden Sie diesen Befehl:

```bash
$ ps -p 1234
```

Der obige Befehl zeigt Informationen zum Prozess mit PID 1234 an, darunter Benutzer, CPU- und Speichernutzung sowie den Befehlsnamen. Sie können auch mehrere PIDs angeben, um mehrere Prozesse anzuzeigen.

Ps kann den Prozessstatus auch in Echtzeit überwachen. Um die CPU- und Speichernutzung eines Prozesses, zum Beispiel PID 1234, zu verfolgen, verwenden Sie diesen Befehl:

```bash
$ ps -p 1234 -o %cpu,%mem
```

Der obige Befehl zeigt die CPU- und Speichernutzung des Prozesses mit PID 1234 an und aktualisiert die Ausgabe jede Sekunde. So überwachen Sie wichtige Prozesse und erkennen mögliche Leistungsengpässe.

### Netzwerkstatistiken

Der Befehl **netstat** zeigt in der CLI aktive Netzwerkverbindungen eines Linux-Systems an. Er hilft, nicht autorisierte Verbindungen und mögliche Sicherheitsbedrohungen zu erkennen. Die Ausgabe kann lokale und entfernte Adressen, das Protokoll (zum Beispiel TCP oder UDP) und den Verbindungsstatus enthalten.

Eine einfache Verwendung von netstat ist die Anzeige aller aktiven Netzwerkverbindungen. Führen Sie dazu diesen Befehl aus:

```bash
$ netstat -a
```

Der obige Befehl zeigt aktive Verbindungen samt lokalen und entfernten Adressen, Protokoll und Status an. Diese Übersicht hilft, nicht autorisierte Verbindungen zu erkennen.

Netstat kann auch Verbindungen eines bestimmten Protokolls, etwa TCP, anzeigen. Um alle aktiven TCP-Verbindungen aufzulisten, verwenden Sie diesen Befehl:

```bash
$ netstat -at
```

Der obige Befehl zeigt alle aktiven TCP-Verbindungen samt lokalen und entfernten Adressen sowie Status an.

Netstat kann außerdem Statistiken zu einem bestimmten Protokoll anzeigen. Um Statistiken aller TCP-Verbindungen abzurufen, verwenden Sie diesen Befehl:

```bash
$ netstat -st
```

Der obige Befehl zeigt Statistiken zu TCP-Verbindungen an, darunter die Zahl aktiver Verbindungen, die Zahl der Verbindungen in jedem Status und die Zahl aufgetretener Fehler. So überwachen Sie den Netzwerkzustand und erkennen mögliche Leistungsprobleme.

### Dateien suchen

Der Befehl **find** sucht über die CLI nach Dateien und Verzeichnissen auf einem Linux-System. Er hilft, versteckte oder schwer auffindbare Elemente zu lokalisieren. Die Suche kann Kriterien wie Name, Größe, Änderungszeit und Berechtigungen verwenden.

Eine einfache Verwendung von find ist die Suche nach dem Namen. Um alle Dateien namens "example.txt" im aktuellen Verzeichnis und seinen Unterverzeichnissen zu finden, verwenden Sie diesen Befehl:

```bash
$ find . -name example.txt
```

Der obige Befehl sucht im aktuellen Verzeichnis und seinen Unterverzeichnissen nach Dateien namens "example.txt" und zeigt ihre vollständigen Pfade an.

Find kann auch nach Dateigröße suchen. Um Dateien größer als 1 MB im aktuellen Verzeichnis und seinen Unterverzeichnissen zu finden, verwenden Sie diesen Befehl:

```bash
$ find . -size +1M
```

Der obige Befehl sucht im aktuellen Verzeichnis und seinen Unterverzeichnissen nach Dateien größer als 1 MB und zeigt ihre vollständigen Pfade an.

Zusätzlich zu Namen und Größe kann find nach Änderungszeit und Berechtigungen suchen. Um Dateien zu finden, die in den letzten sieben Tagen geändert wurden, verwenden Sie diesen Befehl:

```bash
$ find . -mtime -7
```

Der obige Befehl sucht im aktuellen Verzeichnis und seinen Unterverzeichnissen nach Dateien, die in den letzten sieben Tagen geändert wurden, und zeigt ihre vollständigen Pfade an.

Der Befehl find ist ein leistungsfähiges Werkzeug, um Dateien und Verzeichnisse nach vielen Kriterien zu suchen. Er eignet sich für Systemverwaltung und Cybersicherheit.

______

Die Linux-Kommandozeile für die Cybersicherheit zu verwenden, kann für Einsteiger überwältigend wirken. Mit den grundlegenden und erweiterten Befehlen in diesem Leitfaden können Sie die CLI für Sicherheitsaufgaben nutzen. Seien Sie beim Ausführen von Befehlen vorsichtig und verstehen Sie ihre Wirkung, bevor Sie sie verwenden.

Um mehr über Linux für die Cybersicherheit zu erfahren, laden Sie das Betriebssystem **[Kali Linux](https://www.kali.org/downloads/)** herunter. Es wurde speziell für Penetrationstests und digitale Forensik entwickelt.

## Fazit

Die Linux-Kommandozeile ist ein leistungsstarkes Werkzeug für Cybersicherheitsexperten, kann für Einsteiger aber einschüchternd wirken. Wenn Sie die grundlegenden und erweiterten Befehle dieses Leitfadens lernen, können Sie die CLI für die Cybersicherheit nutzen. Seien Sie stets vorsichtig und verstehen Sie jeden Befehl, bevor Sie ihn ausführen. Mit Übung und Erfahrung beherrschen Sie die Linux-Kommandozeile und verbessern Ihre Cybersicherheitskenntnisse.
