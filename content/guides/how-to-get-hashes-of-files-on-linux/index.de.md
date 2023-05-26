---
title: "Linux-Dateihashes: Ein Leitfaden zur Ermittlung von SHA256-, MD5- und SHA1-Hashes mithilfe integrierter Tools"
draft: false
toc: true
date: 2023-05-25
description: "Erfahren Sie, wie Sie SHA256-, MD5- und SHA1-Hashes von Dateien unter Linux mithilfe integrierter Tools erhalten und dabei die Integrität und Authentizität der Daten sicherstellen."
tags: ["Linux-Datei-Hashes", "SHA256-Hash", "MD5-Hash", "SHA1-Hash", "Linux-Befehlszeile", "Dateiintegrität", "Datenvalidierung", "Linux-Sicherheit", "integrierte Tools", "Dateiprüfung", "Datenauthentizität", "Datei-Hashing-Algorithmen", "Linux-Systemverwaltung", "Befehlszeilentools", "Dateiprüfsummen", "Linux-Utilities", "Datei-Integritätsprüfungen", "Überprüfung der Datenintegrität", "Datei-Hash-Beispiele", "Linux-Hash-Befehle", "Datei-Hashing-Methoden", "Linux-Sicherheitsmaßnahmen", "Linux-Datenschutz", "Linux-Dateimanagement", "Linux-Dateiverifizierung", "Integrität von Linux-Dateien", "Datensicherheit", "Linux-Datenvalidierung", "Sicherheit des Linux-Systems", "Datei-Hashing-Verfahren", "Sicherung der Dateiintegrität", "sichere Dateivalidierung", "Linux-Datenintegrität"]
cover: "/img/cover/A_digital_representation_of_file_hashes_being_calculated.png"
coverAlt: "Eine digitale Darstellung von Datei-Hashes, die auf einem Linux-Terminal-Bildschirm berechnet werden, als Symbol für Datenintegrität und -sicherheit."
coverCaption: ""
---

**Leitfaden: Hashes von Dateien unter Linux mit eingebauten Tools abrufen**

## Einführung

In der Welt der Linux-Systeme ist die Ermittlung von Datei-Hashes unerlässlich, um die Datenintegrität zu gewährleisten und die Authentizität von Dateien zu überprüfen. Datei-Hashes dienen als eindeutige Identifikatoren, die es Benutzern ermöglichen, Manipulationsversuche zu erkennen und die Datenintegrität zu überprüfen. In dieser umfassenden Anleitung erfahren Sie, wie Sie **SHA256**-, **MD5**- und **SHA1**-Hashes von Dateien unter Linux mit Hilfe integrierter Tools erhalten. Folgen Sie den schrittweisen Anweisungen und lernen Sie anhand konkreter Beispiele.

______

## Hashes unter Linux mit eingebauten Tools abrufen

Linux bietet mehrere integrierte Tools, mit denen Benutzer Hashes von Dateien berechnen können, ohne zusätzliche Software installieren zu müssen. Wir werden drei weit verbreitete Hash-Algorithmen untersuchen: **SHA256**, **MD5**, und **SHA1**.

### SHA256-Hash berechnen

Um den **SHA256-Hash** einer Datei unter Linux zu erhalten, können Sie den `sha256sum` Befehl. Öffnen Sie ein Terminal und navigieren Sie zu dem Verzeichnis, in dem sich die Datei befindet. Führen Sie dann den folgenden Befehl aus:

```bash
sha256sum file_path
```
Ersetzen Sie `file_path` mit dem tatsächlichen Pfad zu Ihrer Datei.

### Beziehen der MD5- und SHA1-Hashes
Sie können auch die `MD5` und `SHA1 hashes` einer Datei unter Linux mit ähnlichen Befehlen:

- So erhalten Sie die `MD5 hash`

```bash
md5sum file_path
```

- Um die `SHA1 hash`

```bash
sha1sum file_path
```
Ersetzen Sie `file_path` mit dem Pfad zu Ihrer Datei in beiden Befehlen.

## Beispiele
Schauen wir uns nun konkrete Beispiele an, um den Prozess der Ermittlung von Hashes mit Hilfe von eingebauten Tools unter Linux zu veranschaulichen.

{{< youtube id="3aX9zK88X9M" >}}

### Beispiel 1: SHA256-Hash erhalten
Stellen Sie sich vor, Sie haben eine Datei namens `document.pdf` in dem Verzeichnis `/home/user/docs` Um die `SHA256 hash` dieser Datei unter Linux, führen Sie den folgenden Befehl aus:

```bash
sha256sum /home/user/docs/document.pdf
```

Die Ausgabe zeigt die `SHA256 hash` Wert der Datei.

### Beispiel 2: Abrufen des MD5-Hashes

Angenommen, Sie haben eine Datei mit dem Namen `image.jpg` gespeichert im Verzeichnis `/home/user/pictures` Um die `MD5 hash` dieser Datei unter Linux, führen Sie den folgenden Befehl aus:

```bash
md5sum /home/user/pictures/image.jpg
```

Das Terminal zeigt die `MD5 hash` Wert der Datei.

## Beispiel 3: SHA1-Hash abrufen

Betrachten Sie ein Szenario, in dem Sie eine Datei mit dem Namen `data.txt` in dem Verzeichnis `/home/user/files` Um die `SHA1 hash` dieser Datei unter Linux, führen Sie den folgenden Befehl aus:

```bash
sha1sum /home/user/files/data.txt
```
Die Ausgabe zeigt die `SHA1 hash` Wert der Datei.

## Schlussfolgerung
Die Ermittlung von Datei-Hashes unter Linux mit Hilfe integrierter Tools ist eine einfache, aber wirkungsvolle Methode, um die Datenintegrität zu gewährleisten und die Authentizität von Dateien zu überprüfen. Wenn Sie die Anweisungen in diesem Leitfaden befolgen, können Sie SHA256-, MD5- und SHA1-Hashes Ihrer Dateien auf Linux-Systemen zuverlässig berechnen.

## Referenzen

1. [sha256sum - Linux man page](https://man7.org/linux/man-pages/man1/sha256sum.1.html)
2. [md5sum - Linux man page](https://man7.org/linux/man-pages/man1/md5sum.1.html)
3. [sha1sum - Linux man page](https://man7.org/linux/man-pages/man1/sha1sum.1.html)
