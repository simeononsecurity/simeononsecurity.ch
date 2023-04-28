---
title: "HackTheBox - Challenge - Crypto - Weak RSA"
draft: false
description: "Learn how to use an automated RSA attack tool, RsaCtfTool, to easily solve the HackTheBox Weak RSA Crypto challenge."
tags: ["HackTheBox", "Challenges", "Crypto", "Weak RSA", "RsaCtfTool", "HTB Weak RSA Crypto", "Easy challenge", "RSA cipher", "flag.enc", "key.pub", "OpenSSL package", "automated RSA attack tool", "python script", "RsaCtfTool", "python3", "public key", "uncipherfile", "Flag Example"]
toc: true
cover: "/img/cover/A_cartoon_hacker_wearing_a_cape_and_a_mask_standing.png"
coverAlt: "A cartoon hacker wearing a cape and a mask, standing in front of a vault door with the HTB logo on it and holding a tool (such as a wrench or a screwdriver) with a green background symbolizing success and the flag in a speech bubble above their head."
coverCaption: ""
---
```bash
python3 RsaCtfTool.py --publickey ./key.pub --uncipherfile ./flag.enc 
```
```
HTB{XXXXXX_XXXXXXX_XXXXXX}
```

Lösen Sie sterben HTB-Weak-RSA-Crypto-Herausforderung mit Leichtigkeit. Automatisch auf der RSA-Verschlüsselung erfordert this einfache Herausforderung sterben Verwendung eines automatisierten RSA-Angriffstools wie dem RsaCtfTool. Holen Sie sich die Flagge mit einem einfachen Befehl und erweitern Sie Ihre Krypto-Fähigkeiten mit HackTheBox-Herausforderungen.  ______  ## Bereitgestellte Dateien:  **Sie erhalten folgende Dateien:** - flag.enc - key.pub  ##Durchgang:  Auf den ersten Blick könnte man meinen, man könnte das Flag mit dem öffentlichen Schlüssel entschlüsseln. Dazu can wir das OpenSSL-Paket verwenden, um das Flag zu entschlüsseln. Diesmal ist es ein bisschen anders und Sie werden feststellen, dass das OpenSSL-Paket für diese Herausforderung nicht funktioniert.  Wir verwenden ein automatisiertes RSA-Angriffstool. Ein gängiges Python-Skript ist das [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)     Einfach hören, dieses Tool findet die Flagge automatisch und einfach für Sie.  ______  ### Flag-Beispiel: