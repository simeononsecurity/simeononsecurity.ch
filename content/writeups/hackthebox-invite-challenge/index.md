---
title: "HackTheBox - Invite Challenge (Windows/Linux)"
draft: false
toc: true
description: "Learn how to generate an invite code and join the HackTheBox online platform to test and advance your skills in penetration testing and cybersecurity on both Windows and Linux."
tags: ["HackTheBox", "Invite Challenge", "Penetration Testing", "Cybersecurity", "Windows", "Linux", "Online Platform", "HTTP POST", "Invite Code", "Base64 Encoded", "Powershell", "Linux Bash", "Base64 Decode", "Invite Code Generation", "Programming", "Web Development", "Technology", "IT Security", "IT Training"]
cover: "/img/cover/A_cartoon_computer_screen_showing_the_HackTheBox_website.png"
coverAlt: "A cartoon computer screen showing the HackTheBox website with a vault door being unlocked with a key, revealing a trophy or medal, with a cityscape background in the color scheme of HackTheBox's logo (blue and white)."
coverCaption: ""
---
Get step by step instructions to complete the HackTheBox invite challenge on Windows or Linux. Learn how to generate an invite code and join the online platform to test and advance your skills in penetration testing and cyber security. The article presents both simple and advanced solutions, making it easy for users of all levels to complete the challenge and gain access to the platform.

______

## What is Hack the Box ?

HackTheBox is an online platform to test and advance your skills in penetration testing and cyber security. 

## How do you join Hack the box ?

To create an account on HackTheBox (HTB) you have to complete the invite challenge, or hack yourself the way in. Don't worry though it isn't hard and this article will aid you incompleting the challenge.

First, go to the [HackTheBox Website](https://hackthebox.eu) and click on the join button. 

You'll be presented with a box clearly asking for an invite code.

You can clearly see a text box asking us for an invite code. 

Hit either ***"F12"*** on your keyboard or ***"Ctrl + Shift + I"*** to open your browsers developer tools.

On the "Elements" tab, you'll find a script **[inviteapi.min.js](https://www.hackthebox.eu/js/inviteapi.min.js)**.

Reviewing the javascript and the makeInviteCode function, you'll discover that you need to send an **HTTP POST** to **/api/invite/generate** to get an invite code.

You can do the following to get the Base64 encoded invite code:

### Solution:

#### Simple:
- **Windows**: ```powershell (Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON) ```
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


