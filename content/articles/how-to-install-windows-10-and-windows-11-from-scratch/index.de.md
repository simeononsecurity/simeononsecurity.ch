---
title: "So laden Sie eine saubere Windows-ISO herunter und installieren sie von Grund auf neu"
date: 2023-02-20
toc: true
draft: false
description: "In dieser Schritt-für-Schritt-Anleitung erfahren Sie, wie Sie eine saubere Windows-ISO-Datei herunterladen und Windows von Grund auf installieren."
tags: ["Windows 10", "Fenster 11", "ISO-Datei", "Saubere Installation", "Werkzeug zur Medienerstellung", "Bootfähiger USB", "Installationsmedien", "BIOS", "UEFI-Firmware", "Benutzerdefinierte Installation", "Produktschlüssel", "64-Bit-System", "32-Bit-System", "Rufus", "ImgBurn", "CDBurnerXP", "HashCalc", "MD5 & SHA Prüfsummen-Dienstprogramm", "Systemtyp"]
cover: "/img/cover/A_cartoon_image_of_a_person_holding_a_USB_stick.png"
coverAlt: "Ein Cartoon-Bild einer Person, die einen USB-Stick mit einem Windows-Logo und einem Häkchen in der Hand hält und vor einem Computerbildschirm mit einem Windows-Logo steht."
coverCaption: ""
---

**So laden Sie eine saubere Windows 10- oder 11-ISO herunter und installieren Windows von Grund auf neu**

Wenn Sie planen, Windows auf einem neuen Computer zu installieren, oder wenn Sie eine saubere Installation durchführen möchten, um Probleme zu beseitigen, ist der Download einer sauberen Windows-ISO-Datei ein wichtiger erster Schritt. In diesem Artikel beschreiben wir die Schritte zum Herunterladen einer sauberen Windows 10- oder 11-ISO und führen Sie durch den Installationsprozess.

## Teil 1: Herunterladen einer sauberen Windows-ISO-Datei

### Schritt 1: Überprüfen Sie Ihren Systemtyp

Der erste Schritt zum Herunterladen einer sauberen Windows-ISO-Datei ist die Überprüfung Ihres Systemtyps. Sie müssen wissen, ob Sie ein 32-Bit- oder ein 64-Bit-System haben, denn davon hängt ab, welche ISO-Datei Sie herunterladen müssen.

Gehen Sie folgendermaßen vor, um Ihren Systemtyp unter Windows 10 zu überprüfen:

1. Öffnen Sie das Startmenü und klicken Sie auf "Einstellungen".
2. Klicken Sie auf "System".
3. Klicken Sie auf "Info".
4. Prüfen Sie unter "Gerätespezifikationen" den Eintrag "Systemtyp".

Wenn Sie ein 32-Bit-System haben, müssen Sie die 32-Bit-Version von Windows herunterladen. Wenn Sie ein 64-Bit-System haben, können Sie entweder die 32-Bit- oder die 64-Bit-Version herunterladen, wir empfehlen jedoch die 64-Bit-Version, um eine bessere Leistung zu erzielen.

### Schritt 2: Laden Sie das Tool zur Medienerstellung herunter.

Um eine saubere Windows-ISO herunterzuladen, verwenden wir das Media Creation Tool von Microsoft. Sie können es direkt von der Microsoft-Website herunterladen, indem Sie die folgenden Schritte ausführen:

1. Gehen Sie auf die Seite [Microsoft Windows 10 download page](https://www.microsoft.com/en-us/software-download/windows10)
2. Scrollen Sie nach unten zum Abschnitt "Windows 10-Installationsmedien erstellen" und klicken Sie auf "Tool jetzt herunterladen".
3. Speichern Sie die Datei auf Ihrem Computer.

Wenn Sie Windows 11 herunterladen möchten, ist der Vorgang ähnlich. Sie können das Tool zur Erstellung von Installationsmedien von der folgenden Website herunterladen [Microsoft Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) und befolgen Sie die gleichen Schritte.

### Schritt 3: Führen Sie das Tool zur Medienerstellung aus.

Sobald Sie das Media Creation Tool heruntergeladen haben, führen Sie es auf Ihrem Computer aus. Sie werden gefragt, ob Sie Ihren aktuellen PC aktualisieren oder ein Installationsmedium erstellen möchten. Wählen Sie die Option "Installationsmedien erstellen" und klicken Sie auf "Weiter".

### Schritt 4: Wählen Sie Ihre Sprache, Edition und Architektur

Im nächsten Schritt wählen Sie Ihre Sprache, Edition und Architektur. Sie können die Sprachoption auf Ihrer aktuellen Sprache belassen oder eine andere Sprache wählen, wenn Sie dies wünschen.

Als Edition wählen Sie die Version von Windows, die Sie installieren möchten. Sie haben die Wahl zwischen Windows 10 Home und Windows 10 Pro, oder Windows 11 Home und Windows 11 Pro.

Wählen Sie als Architektur den Systemtyp aus, den Sie in Schritt 1 festgelegt haben. Wenn Sie ein 64-Bit-System haben, empfehlen wir Ihnen, die 64-Bit-Version auszuwählen, um eine bessere Leistung zu erzielen.

### Schritt 5: Wählen Sie Ihren Medientyp

Im nächsten Schritt wählen Sie den Medientyp aus. Sie können entweder ein bootfähiges USB-Laufwerk erstellen oder eine ISO-Datei herunterladen.

Wenn Sie sich für die Erstellung eines bootfähigen USB-Laufwerks entscheiden, benötigen Sie ein USB-Laufwerk mit mindestens 8 GB Speicherplatz. Das Media Creation Tool formatiert das Laufwerk automatisch und kopiert die erforderlichen Dateien.

Wenn Sie sich für den Download einer ISO-Datei entscheiden, lädt das Medienerstellungs-Tool die Datei herunter und speichert sie auf Ihrem Computer. Sie können dann ein Tool eines Drittanbieters verwenden, um ein bootfähiges USB-Laufwerk zu erstellen oder die ISO-Datei auf eine DVD zu brennen.

### Schritt 6: Herunterladen der ISO-Datei

Wenn Sie sich für den Download einer ISO-Datei entschieden haben, beginnt das Media Creation Tool mit dem Herunterladen der Datei. Dies kann je nach Geschwindigkeit Ihrer Internetverbindung einige Zeit in Anspruch nehmen.

Sobald der Download abgeschlossen ist, prüft das Tool die Datei, um sicherzustellen, dass es sich um eine saubere ISO-Datei handelt.

### Schritt 7: Überprüfen der ISO-Datei

Die Überprüfung der ISO-Datei ist ein wichtiger Schritt, um sicherzustellen, dass die heruntergeladene Datei sauber ist und nicht verändert wurde. Um die Datei zu überprüfen, können Sie ein Tool wie [HashCalc](https://www.slavasoft.com/hashcalc/) or [MD5 & SHA Checksum Utility](https://raylin.wordpress.com/downloads/md5-sha-1-checksum-utility/)

Sobald Sie das Verifizierungstool heruntergeladen und installiert haben, öffnen Sie es und wählen Sie die heruntergeladene ISO-Datei aus. Das Tool berechnet den Hash-Wert der Datei und vergleicht ihn mit dem von Microsoft auf der Windows-Download-Seite angegebenen Hash-Wert. Wenn die Hash-Werte übereinstimmen, ist die ISO-Datei sauber und kann zur Installation von Windows verwendet werden.

## Teil 2: Installieren von Windows aus einer sauberen ISO-Datei

Sobald Sie eine saubere Windows-ISO-Datei haben, können Sie diese verwenden, um Windows auf Ihrem Computer zu installieren. Gehen Sie dazu wie folgt vor:

### Schritt 1: Installationsmedium erstellen

Bevor Sie Windows aus der ISO-Datei installieren können, müssen Sie ein Installationsmedium erstellen. Dazu können Sie ein bootfähiges USB-Laufwerk oder eine DVD verwenden.

Um ein bootfähiges USB-Laufwerk zu erstellen, können Sie ein Tool wie [Rufus](https://rufus.ie/) or [Windows USB/DVD Download Tool](https://www.microsoft.com/en-us/download/windows-usb-dvd-download-tool) Schließen Sie einfach das USB-Laufwerk an, öffnen Sie das Tool, und folgen Sie den Anweisungen, um das bootfähige Laufwerk zu erstellen.

Wenn Sie lieber eine DVD verwenden möchten, können Sie ein Tool wie [ImgBurn](https://www.imgburn.com/) or [CDBurnerXP](https://cdburnerxp.se/en/home) Legen Sie die DVD ein, öffnen Sie das Programm und folgen Sie den Anweisungen, um die ISO-Datei auf die DVD zu brennen.

### Schritt 2: Booten vom Installationsmedium

Nachdem Sie das Installationsmedium erstellt haben, müssen Sie Ihren Computer von diesem Medium booten. Dazu müssen Sie möglicherweise die Startreihenfolge im BIOS oder in der UEFI-Firmware Ihres Computers ändern.

Um das BIOS oder die UEFI-Firmware aufzurufen, starten Sie Ihren Computer neu und drücken Sie die Taste, die auf dem Bildschirm erscheint. Dies ist normalerweise F2, F10 oder Entf. Sobald Sie sich im BIOS oder in der UEFI-Firmware befinden, suchen Sie das Menü "Booten" und ändern Sie die Boot-Reihenfolge so, dass Ihr Installationsmedium ganz oben in der Liste steht.

### Schritt 3: Windows installieren

Sobald Ihr Computer von dem Installationsmedium gebootet hat, wird der Windows-Setup-Bildschirm angezeigt. Folgen Sie den Anweisungen, um Windows auf Ihrem Computer zu installieren.

Sie werden aufgefordert, Ihre Sprache, die Zeitzone und das Tastaturlayout auszuwählen. Anschließend werden Sie aufgefordert, Ihren Product Key einzugeben. Wenn Sie keinen Product Key haben, können Sie die Option "Ich habe keinen Product Key" wählen und mit der Installation fortfahren. Sie können Windows später aktivieren, sobald es installiert ist.

Als Nächstes werden Sie aufgefordert, die Art der Installation auszuwählen. Wählen Sie die Option "Benutzerdefiniert", um eine saubere Installation durchzuführen.

Sie werden dann aufgefordert, die Partition auszuwählen, auf der Sie Windows installieren möchten. Wenn Sie Windows auf einem neuen Computer oder einem Computer mit einer leeren Festplatte installieren, wird nicht zugewiesener Speicherplatz angezeigt. Wählen Sie den nicht zugewiesenen Speicherplatz aus und klicken Sie auf "Weiter", um eine neue Partition zu erstellen und Windows zu installieren.

Sobald die Installation abgeschlossen ist, wird Windows neu gestartet, und Sie werden aufgefordert, Ihr Benutzerkonto einzurichten.

## Schlussfolgerung

Das Herunterladen eines sauberen Windows-ISOs und die Neuinstallation von Windows mag entmutigend erscheinen, aber es ist ein unkomplizierter Prozess, den jeder durchführen kann. Wenn Sie die Schritte in dieser Anleitung befolgen, können Sie sicherstellen, dass Sie ein sauberes Windows

