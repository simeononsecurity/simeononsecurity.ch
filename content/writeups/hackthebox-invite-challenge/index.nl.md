---
title: "HackTheBox - Invite Challenge (Windows/Linux)"
draft: false
toc: true
description: "Leer hoe u een uitnodigingscode genereert en deelneemt aan het online platform HackTheBox om uw vaardigheden op het gebied van penetratietests en cyberbeveiliging op zowel Windows als Linux te testen en te verbeteren."
tags: ["HackTheBox", "Uitnodiging uitdaging", "Penetratie testen", "Cyberbeveiliging", "Windows", "Linux", "Online platform", "HTTP POST", "Code uitnodigen", "Base64 gecodeerd", "Powershell", "Linux Bash", "Base64 decoderen", "Codegeneratie uitnodigen", "Programmering", "Web Ontwikkeling", "Technologie", "IT Beveiliging", "IT Opleiding"]
cover: "/img/cover/A_cartoon_computer_screen_showing_the_HackTheBox_website.png"
coverAlt: "Een cartoonachtig computerscherm waarop de HackTheBox-website te zien is met een kluisdeur die wordt ontgrendeld met een sleutel, waarop een trofee of medaille te zien is, met een stadslandschap als achtergrond in het kleurenschema van het logo van HackTheBox (blauw en wit)."
coverCaption: ""
---
 stap voor stap instructies om de HackTheBox-uitdaging op Windows of Linux te voltooien. Leer hoe u een uitnodigingscode genereert en lid wordt van het online platform om uw vaardigheden op het gebied van penetratietests en cyberbeveiliging te testen en te verbeteren. Het artikel presenteert zowel eenvoudige als geavanceerde oplossingen, waardoor het voor gebruikers van alle niveaus gemakkelijk is om de uitdaging te voltooien en toegang te krijgen tot het platform.

______

## Wat is Hack the Box ?

HackTheBox is een online platform om uw vaardigheden in penetratietesten en cyberbeveiliging te testen en te verbeteren.

## Hoe doe je mee aan Hack the box ?

Om een account aan te maken op HackTheBox (HTB) moet je de invite uitdaging voltooien, of jezelf de weg naar binnen hacken. Maar maak je geen zorgen, het is niet moeilijk en dit artikel zal je helpen bij het voltooien van de uitdaging.

Ga eerst naar de [HackTheBox Website](https://hackthebox.eu) en klik op de toetredingsknop.

Je krijgt een vakje te zien waarin duidelijk om een uitnodigingscode wordt gevraagd.

Je ziet duidelijk een tekstvak waarin om een uitnodigingscode wordt gevraagd.

Druk op ***"F12"*** op je toetsenbord of ***"Ctrl + Shift + I"*** om de ontwikkelaarstools van je browser te openen.

Op de tab "Elements" vind je een script **[inviteapi.min.js](https://www.hackthebox.eu/js/inviteapi.min.js)

Als je het javascript en de functie makeInviteCode bekijkt, zul je ontdekken dat je een **HTTP POST** moet sturen naar **/api/invite/generate** om een uitnodigingscode te krijgen.

Je kunt het volgende doen om de Base64 gecodeerde uitnodigingscode te krijgen:

### Oplossing:

#### Eenvoudig:
- **Windows**: ```powershell (Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON) ```
- Linux: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" ```

Wat de volgende inhoud zal genereren: ```json {"success":1,"data":{"code":"Tk9ULVRIRS1GTEFHLVlPVSdSRS1MT09LSU5HLUZPUg==","format":"encoded"},"0":200} ```

Als je de gecodeerde uitnodigingscode naar [base64decode.org](https://www.base64decode.org/) krijg je je uitnodigingscode!

#### Geavanceerd (print direct de uitnodigingscode uit):
 - **Windows**: ```powershell $base64api=((Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON).Data).Code ; [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($base64api)) ```
- Linux: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" | jq -r '.data.code' | base64 -d ```
 - **Noot**: Je moet de [jq](https://stedolan.github.io/jq/download/) pakket.

______

### Invite Code Ex:
```XXXXX-XXXXX-XXXXX-XXXXX-XXXXX```


