---
title: "HackTheBox - Invite Challenge (Windows/Linux)"
draft: false
toc: true
description: "Apprenez à générer un code d'invitation et rejoignez la plateforme en ligne HackTheBox pour tester et faire progresser vos compétences en matière de tests d'intrusion et de cybersécurité sur Windows et Linux."
tags: ["HackTheBox","Inviter le défi","Tests de pénétration","La cyber-sécurité","Les fenêtres","Linux","Plateforme en ligne","HTTP POST","Code d'invitation","Encodé en Base64","Powershell","Bash Linux","Décodage Base64","Inviter la génération de code","La programmation","Développement web","Technologie","Sécurité informatique","Formation informatique"]
cover: "/img/cover/A_cartoon_computer_screen_showing_the_HackTheBox_website.png"
coverAlt: "Un écran d'ordinateur de dessin animé montrant le site Web HackTheBox avec une porte de coffre-fort déverrouillée avec une clé, révélant un trophée ou une médaille, avec un fond de paysage urbain dans la palette de couleurs du logo de HackTheBox (bleu et blanc)."
coverCaption: ""
---
 des instructions étape par étape pour relever le défi d'invitation HackTheBox sous Windows ou Linux. Apprenez à générer un code d'invitation et rejoignez la plateforme en ligne pour tester et faire progresser vos compétences en matière de tests d'intrusion et de cybersécurité. L'article présente à la fois des solutions simples et avancées, permettant aux utilisateurs de tous niveaux de relever facilement le défi et d'accéder à la plateforme.

______

## Qu'est-ce que Hack the Box ?

HackTheBox est une plateforme en ligne pour tester et faire progresser vos compétences en matière de tests d'intrusion et de cybersécurité.

## Comment rejoindre Hack the box ?

Pour créer un compte sur HackTheBox (HTB), vous devez relever le défi d'invitation ou vous pirater pour entrer. Ne vous inquiétez pas, même si ce n'est pas difficile et cet article vous aidera à relever le défi.

D'abord, rendez-vous au[HackTheBox Website](https://hackthebox.eu) et cliquez sur le bouton rejoindre.

Vous serez présenté avec une boîte demandant clairement un code d'invitation.

Vous pouvez clairement voir une zone de texte nous demandant un code d'invitation.

Appuyez sur ***"F12"*** sur votre clavier ou ***"Ctrl + Maj + I"*** pour ouvrir les outils de développement de votre navigateur.

Dans l'onglet "Eléments", vous trouverez un script **[inviteapi.min.js](https://www.hackthebox.eu/js/inviteapi.min.js)

En examinant le javascript et la fonction makeInviteCode, vous découvrirez que vous devez envoyer un **HTTP POST** à **/api/invite/generate** pour obtenir un code d'invitation.

Vous pouvez procéder comme suit pour obtenir le code d'invitation encodé en Base64 :

### Solution:

#### Simple:
- **Les fenêtres**:```powershell (Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON) ```
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


