---
title: "HackTheBox - Invite Challenge (Windows/Linux)"
draft: false
toc: true
description: "Aprèn a generar un codi d'invitació i uneix-te a la plataforma en línia HackTheBox per provar i avançar les teves habilitats en proves de penetració i ciberseguretat tant a Windows com a Linux".
tags: ["HackTheBox","Convida desafiament","Prova de penetració","Seguretat cibernètica","Windows","Linux","Plataforma en línia","HTTP POST","Codi d'invitació","Codificació Base64","Powershell","Linux Bash","Descodificació Base64","Convida a la generació de codi","Programació","Desenvolupament web","Tecnologia","Seguretat informàtica","Formació informàtica"]
cover: "/img/cover/A_cartoon_computer_screen_showing_the_HackTheBox_website.png"
coverAlt: "Una pantalla d'ordinador de dibuixos animats que mostra el lloc web de HackTheBox amb una porta de la volta que s'obre amb una clau, revelant un trofeu o una medalla, amb un fons de paisatge urbà amb l'esquema de colors del logotip de HackTheBox (blau i blanc)."
coverCaption: ""
---
 instruccions pas a pas per completar el repte d'invitació HackTheBox a Windows o Linux. Aprèn a generar un codi d'invitació i uneix-te a la plataforma en línia per provar i avançar les teves habilitats en proves d'penetració i ciberseguretat. L'article presenta solucions tant senzilles com avançades, cosa que facilita als usuaris de tots els nivells completar el repte i accedir a la plataforma.

______

## Què és Hack the Box?

HackTheBox és una plataforma en línia per provar i avançar les teves habilitats en proves de penetració i ciberseguretat.

## Com us uniu a Hack the box?

Per crear un compte a HackTheBox (HTB), heu de completar el repte d'invitació o piratejar-vos per entrar. No us preocupeu, encara que no sigui difícil i aquest article us ajudarà a completar el repte.

Primer, aneu al[HackTheBox Website](https://hackthebox.eu) i feu clic al botó unir-se.

Se us presentarà una casella que us demanarà clarament un codi d'invitació.

Podeu veure clarament un quadre de text que ens demana un codi d'invitació.

Premeu ***"F12"*** al vostre teclat o ***"Ctrl + Maj + I"*** per obrir les eines de desenvolupament del vostre navegador.

A la pestanya "Elements", trobareu un script **[inviteapi.min.js](https://www.hackthebox.eu/js/inviteapi.min.js)

Revisant el javascript i la funció makeInviteCode, descobrireu que heu d'enviar un **HTTP POST** a **/api/invite/generate** per obtenir un codi d'invitació.

Podeu fer el següent per obtenir el codi d'invitació codificat en Base64:

### Solució:

#### Simple:
- **Windows**:```powershell (Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON) ```
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


