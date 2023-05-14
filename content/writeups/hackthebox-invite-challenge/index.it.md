---
title: "HackTheBox - Invite Challenge (Windows/Linux)"
draft: false
toc: true
description: "Scopri come generare un codice di invito e unisciti alla piattaforma online HackTheBox per testare e migliorare le tue abilità nei penetration test e nella sicurezza informatica su Windows e Linux."
tags: ["HackTheBox", "Sfida ad inviti", "Test di penetrazione", "Sicurezza informatica", "finestre", "Linux", "Piattaforma online", "POST HTTP", "Codice di invito", "Base64 codificato", "PowerShell", "Bash di Linux", "Decodifica Base64", "Generazione del codice di invito", "Programmazione", "Sviluppo web", "Tecnologia", "Sicurezza informatica", "Formazione informatica"]
cover: "/img/cover/A_cartoon_computer_screen_showing_the_HackTheBox_website.png"
coverAlt: "Lo schermo di un computer a cartone animato che mostra il sito Web di HackTheBox con una porta del caveau che viene sbloccata con una chiave, rivelando un trofeo o una medaglia, con uno sfondo di paesaggio urbano nella combinazione di colori del logo di HackTheBox (blu e bianco)."
coverCaption: ""
---
 istruzioni passo passo per completare la sfida di invito HackTheBox su Windows o Linux. Scopri come generare un codice di invito e unisciti alla piattaforma online per testare e migliorare le tue abilità nei test di penetrazione e nella sicurezza informatica. L'articolo presenta soluzioni sia semplici che avanzate, rendendo facile per gli utenti di tutti i livelli completare la sfida e ottenere l'accesso alla piattaforma.

______

## Che cos'è Hack the Box?

HackTheBox è una piattaforma online per testare e migliorare le tue abilità nei test di penetrazione e nella sicurezza informatica.

## Come ci si iscrive a Hack the box?

Per creare un account su HackTheBox (HTB) devi completare la sfida dell'invito o hackerarti per entrare. Non preoccuparti, anche se non è difficile e questo articolo ti aiuterà a completare la sfida.

Per prima cosa, vai al[HackTheBox Website](https://hackthebox.eu) e fare clic sul pulsante Partecipa.

Ti verrà presentata una casella che richiede chiaramente un codice di invito.

Puoi vedere chiaramente una casella di testo che ci chiede un codice di invito.

Premi ***"F12"*** sulla tastiera o ***"Ctrl + Maiusc + I"*** per aprire gli strumenti di sviluppo del tuo browser.

Nella scheda "Elementi", troverai uno script **[inviteapi.min.js](https://www.hackthebox.eu/js/inviteapi.min.js)

Esaminando il javascript e la funzione makeInviteCode, scoprirai che devi inviare un **HTTP POST** a **/api/invite/generate** per ottenere un codice di invito.

Puoi fare quanto segue per ottenere il codice di invito codificato Base64:

### Soluzione:

#### Semplice:
- **Finestre**:```powershell (Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" ```

Which will generate the following content: ```json {"success":1,"data":{"code":"Tk9ULVRIRS1GTEFHLVlPVSdSRS1MT09LSU5HLUZPUg==","format":"encoded"},"0":200} ```

If you take the encoded invite code to [base64decode.org](https://www.base64decode.org/), you'll get your invite code!

#### Advanced (Instantly print out invite code):
 - **Windows**: ```powershell $base64api=((Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON).Data).Code ; [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($base64api)) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" | jq -r '.data.code' | base64 -d ```
 - **Note**: You'll need to install the [jq](https://stedolan.github.io/jq/download/) package.

______

### Invite Code Ex:
```XXXXX-XXXXX-XXXXX-XXXXX-XXXXX```


