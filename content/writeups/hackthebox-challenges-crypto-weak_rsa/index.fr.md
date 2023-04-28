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

Résolvez facilement le défi HTB Weak RSA Crypto. Basé sur le chiffrement RSA, ce défi facile nécessite l'utilisation d'un outil d'attaque RSA automatisé comme le RsaCtfTool. Obtenez le drapeau avec une simple commande et développez vos compétences en cryptographie avec les défis HackTheBox.  ______  ##Fichiers fournis :  **Les fichiers suivants vous sont fournis :** - flag.enc - clé.pub  ## Procédure pas à pas :  À première vue, vous pensez que vous pouvez déchiffrer le drapeau avec la clé publique. Pour cela, nous utiliserons le package OpenSSL pour déchiffrer le drapeau. Cette fois, c'est un peu différent et vous constatez que le package OpenSSL ne fonctionnera pas pour ce défi.  Nous utiliserons un outil d'attaque RSA automatisé. Un script python courant est le [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)     En termes simples, cet outil trouve facilement le drapeau pour vous de manière automatisée.  ______  Exemple d'indicateur ### :