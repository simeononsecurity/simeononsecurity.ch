---
title: "HackTheBox - Invite Challenge (Windows/Linux)"
draft: false
toc: true
description: "Erfahren Sie, wie Sie einen Einladungscode generieren und der Online-Plattform HackTheBox beitreten, um Ihre Fähigkeiten in Penetrationstests und Cybersicherheit unter Windows und Linux zu testen und zu verbessern."
tags: ["HackTheBox", "Herausforderung einladen", "Penetrationstests", "Internet-Sicherheit", "Windows", "Linux", "Online-Plattform", "HTTP-POST", "Einladungscode", "Base64-kodiert", "Power Shell", "Linux-Bash", "Base64-Dekodierung", "Laden Sie die Codegenerierung ein", "Programmierung", "Web Entwicklung", "Technologie", "IT Sicherheit", "IT-Schulung"]
cover: "/img/cover/A_cartoon_computer_screen_showing_the_HackTheBox_website.png"
coverAlt: "Ein Cartoon-Computerbildschirm, der die HackTheBox-Website mit einer Tresortür zeigt, die mit einem Schlüssel aufgeschlossen wird und eine Trophäe oder Medaille zum Vorschein bringt, mit einem Stadtbildhintergrund im Farbschema des HackTheBox-Logos (blau und weiß)."
coverCaption: ""
---
 Schritt-für-Schritt-Anleitung zum Abschließen der HackTheBox-Einladungsherausforderung unter Windows oder Linux. Erfahren Sie, wie Sie einen Einladungscode generieren und der Online-Plattform beitreten, um Ihre Fähigkeiten in Penetrationstests und Cybersicherheit zu testen und zu verbessern. Der Artikel stellt sowohl einfache als auch fortgeschrittene Lösungen vor, die es Benutzern aller Erfahrungsstufen erleichtern, die Herausforderung zu meistern und Zugriff auf die Plattform zu erhalten.

______

## Was ist Hack the Box?

HackTheBox ist eine Online-Plattform zum Testen und Ausbauen Ihrer Fähigkeiten im Bereich Penetrationstests und Cybersicherheit.

## Wie treten Sie Hack the Box bei?

Um ein Konto bei HackTheBox (HTB) zu erstellen, müssen Sie die Einladungsherausforderung abschließen oder sich selbst den Weg hineinhacken. Machen Sie sich keine Sorgen, es ist jedoch nicht schwer und dieser Artikel wird Ihnen dabei helfen, die Herausforderung nicht zu meistern.

Gehen Sie zunächst zu [HackTheBox Website](https://hackthebox.eu) und klicken Sie auf die Schaltfläche „Beitreten“.

Ihnen wird ein Feld angezeigt, in dem Sie deutlich nach einem Einladungscode gefragt werden.

Sie können deutlich ein Textfeld sehen, in dem wir nach einem Einladungscode gefragt werden.

Drücken Sie entweder ***"F12"*** auf Ihrer Tastatur oder ***"Strg + Umschalt + I"***, um die Entwicklertools Ihres Browsers zu öffnen.

Auf der Registerkarte „Elemente“ finden Sie ein Skript **[inviteapi.min.js](https://www.hackthebox.eu/js/inviteapi.min.js)

Wenn Sie sich das Javascript und die makeInviteCode-Funktion ansehen, werden Sie feststellen, dass Sie einen **HTTP-POST** an **/api/invite/generate** senden müssen, um einen Einladungscode zu erhalten.

Sie können Folgendes tun, um den Base64-codierten Einladungscode zu erhalten:

### Lösung:

#### Einfach:
- **Windows**: ```powershell (Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" ```

Dadurch wird der folgende Inhalt generiert: ```json {"success":1,"data":{"code":"Tk9ULVRIRS1GTEFHLVlPVSdSRS1MT09LSU5HLUZPUg==","format":"encoded"},"0":200} ```

Wenn Sie den verschlüsselten Einladungscode annehmen [base64decode.org](https://www.base64decode.org/) Du bekommst deinen Einladungscode!

#### Fortgeschritten (Einladungscode sofort ausdrucken):
 - **Windows**: ```powershell $base64api=((Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON).Data).Code ; [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($base64api)) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" | jq -r '.data.code' | base64 -d ```
 - **Hinweis**: Sie müssen das installieren [jq](https://stedolan.github.io/jq/download/) Paket.

______

### Einladungscode Beispiel:
```XXXXX-XXXXX-XXXXX-XXXXX-XXXXX```


