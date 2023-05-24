---
title: "HackTheBox - Invite Challenge (Windows/Linux)"
draft: false
toc: true
description: "Aflați cum să generați un cod de invitație și să vă alăturați platformei online HackTheBox pentru a vă testa și îmbunătăți abilitățile în testarea de penetrare și securitatea cibernetică atât pe Windows, cât și pe Linux."
tags: ["HackTheBox", "Provocare invitați", "Testarea de penetrare", "Securitate cibernetică", "Windows", "Linux", "Platforma online", "HTTP POST", "Cod de invitație", "Codul Base64", "Powershell", "Linux Bash", "Decodare Base64", "Invitați la generarea codului", "Programare", "Dezvoltare web", "Tehnologie", "Securitate IT", "Instruire IT"]
cover: "/img/cover/A_cartoon_computer_screen_showing_the_HackTheBox_website.png"
coverAlt: "Un ecran de computer cu desene animate care arată site-ul web HackTheBox cu o ușă de seif descuiată cu o cheie, dezvăluind un trofeu sau o medalie, cu un fundal peisaj urban în schema de culori a siglei HackTheBox (albastru și alb)."
coverCaption: ""
---
 instrucțiuni pas cu pas pentru a finaliza provocarea de invitare HackTheBox pe Windows sau Linux. Aflați cum să generați un cod de invitație și să vă alăturați platformei online pentru a vă testa și a vă dezvolta abilitățile în testarea de penetrare și securitatea cibernetică. Articolul prezintă atât soluții simple, cât și avansate, facilitând utilizatorilor de toate nivelurile să finalizeze provocarea și să obțină acces la platformă.

______

## Ce este Hack the Box?

HackTheBox este o platformă online pentru a-ți testa și avansa abilitățile în testarea de penetrare și securitatea cibernetică.

## Cum te înscrii în Hack the box?

Pentru a crea un cont pe HackTheBox (HTB), trebuie să finalizați provocarea de invitare sau să vă spargeți drumul. Nu vă faceți griji, deși nu este greu și acest articol vă va ajuta să completați provocarea.

Mai întâi, mergi la [HackTheBox Website](https://hackthebox.eu) și faceți clic pe butonul de alăturare.

Vi se va prezenta o casetă care vă cere în mod clar un cod de invitație.

Puteți vedea clar o casetă de text care ne cere un cod de invitație.

Apăsați fie ***„F12”*** de pe tastatură, fie ***„Ctrl + Shift + I”*** pentru a deschide instrumentele de dezvoltare ale browserului.

În fila „Elemente”, veți găsi un script **[inviteapi.min.js](https://www.hackthebox.eu/js/inviteapi.min.js)

Examinând javascript și funcția makeInviteCode, veți descoperi că trebuie să trimiteți un **HTTP POST** la **/api/invite/generate** pentru a obține un cod de invitație.

Puteți face următoarele pentru a obține codul de invitație codificat Base64:

### Soluție:

#### Simplu:
- **Windows**: ```powershell (Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" ```

Care va genera următorul conținut: ```json {"success":1,"data":{"code":"Tk9ULVRIRS1GTEFHLVlPVSdSRS1MT09LSU5HLUZPUg==","format":"encoded"},"0":200} ```

Dacă luați codul de invitare codificat la [base64decode.org](https://www.base64decode.org/) vei primi codul de invitație!

#### Avansat (tipărește instantaneu codul de invitație):
 - **Windows**: ```powershell $base64api=((Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON).Data).Code ; [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($base64api)) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" | jq -r '.data.code' | base64 -d ```
 - **Notă**: va trebui să instalați [jq](https://stedolan.github.io/jq/download/) pachet.

______

### Cod de invitație Ex:
```XXXXX-XXXXX-XXXXX-XXXXX-XXXXX```


