---
title: "HackTheBox - Invite Challenge (Windows/Linux)"
draft: false
toc: true
description: "Aprenda a generar un código de invitación y únase a la plataforma en línea HackTheBox para probar y mejorar sus habilidades en pruebas de penetración y ciberseguridad tanto en Windows como en Linux."
tags: ["HackTheBox", "Desafío de invitación", "Pruebas de penetración", "La seguridad cibernética", "ventanas", "linux", "Plataforma en línea", "PUBLICACIÓN HTTP", "Codigo de invitacion", "Base64 codificado", "Potencia Shell", "Linux Bash", "Decodificación Base64", "Generación de código de invitación", "Programación", "Desarrollo web", "Tecnología", "Seguridad informatica", "Capacitación en TI"]
cover: "/img/cover/A_cartoon_computer_screen_showing_the_HackTheBox_website.png"
coverAlt: "Una pantalla de computadora de dibujos animados que muestra el sitio web de HackTheBox con una puerta de bóveda que se abre con una llave, revelando un trofeo o medalla, con un fondo de paisaje urbano en el esquema de color del logotipo de HackTheBox (azul y blanco)."
coverCaption: ""
---
 instrucciones paso a paso para completar el desafío de invitación de HackTheBox en Windows o Linux. Aprenda a generar un código de invitación y únase a la plataforma en línea para probar y mejorar sus habilidades en pruebas de penetración y seguridad cibernética. El artículo presenta soluciones simples y avanzadas, lo que facilita a los usuarios de todos los niveles completar el desafío y obtener acceso a la plataforma.

______

## ¿Qué es Hack the Box?

HackTheBox es una plataforma en línea para probar y mejorar sus habilidades en pruebas de penetración y seguridad cibernética.

## ¿Cómo te unes a Hack the box?

Para crear una cuenta en HackTheBox (HTB), debe completar el desafío de invitación o piratearse para ingresar. No se preocupe, aunque no es difícil y este artículo lo ayudará a completar el desafío.

Primero, ve a la[HackTheBox Website](https://hackthebox.eu) y haga clic en el botón unirse.

Se le presentará un cuadro que le pedirá claramente un código de invitación.

Puede ver claramente un cuadro de texto que nos pide un código de invitación.

Presiona ***"F12"*** en tu teclado o ***"Ctrl + Shift + I"*** para abrir las herramientas de desarrollo de tu navegador.

En la pestaña "Elementos", encontrará un script **[inviteapi.min.js](https://www.hackthebox.eu/js/inviteapi.min.js)

Al revisar el javascript y la función makeInviteCode, descubrirá que necesita enviar un **HTTP POST** a **/api/invite/generate** para obtener un código de invitación.

Puede hacer lo siguiente para obtener el código de invitación codificado en Base64:

### Solución:

#### Simple:
- **Ventanas**:```powershell (Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON) ```
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


