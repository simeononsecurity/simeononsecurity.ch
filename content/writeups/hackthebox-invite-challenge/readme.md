---
title: "HackTheBox Invite Challenge - Windows"
draft: false
toc: true
---

# HackTheBox - Invite Challenge

## What is Hack the Box ?

HackTheBox is an online platform to test and advance your skills in penetration testing and cyber security. 

## How do you join Hack the box ?

To create an account on HackTheBox (HTB) you have to complete the invite challenge, or hack yourself the way in. Don't worry though it isn't hard and this article will aid you incompleting the challenge.

First, go to the [HackTheBox Website](https://hackthebox.eu) and click on the join button. 

You'll be presented with a box clearly asking for an invite code.

You can clearly see a text box asking us for an invite code. 

Hit either "F12" on your keyboard or "Ctrl + Shift + I" to open your browsers developer tools.

On the "Elements" tab, you'll find a script **[inviteapi.min.js](https://www.hackthebox.eu/js/inviteapi.min.js)**.

Reviewing the javascript and the makeInviteCode function, you'll discover that you need to send an **HTTP POST** to **/api/invite/generate** to get an invite code.

In windows you can do the following to get the Base64 encoded invite code:
```ps
Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate"
```

Which will generate the following content:
```
{"success":1,"data":{"code":"Tk9ULVRIRS1GTEFHLVlPVVItTE9PS0lORy1GT1I=","format":"encoded"},"0":200}
```



If you take the encoded invite code to [base64decode.org](https://www.base64decode.org/), you'll get your FLAG the invite code!

