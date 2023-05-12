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

Resuelva el desafío HTB Débil RSA Crypto con facilidad. Basado en el cifrado RSA, este sencillo desafío requiere el uso de una herramienta de ataque RSA automatizada como RsaCtfTool. Obtenga la bandera con un simple comando y amplíe sus habilidades criptográficas con los desafíos de HackTheBox.  ______  ##Archivos provistos:  **Se le garantizaron los siguientes archivos:** - bandera.enc - clave.pub  ## Tutorial:  A primera vista, pensaría que puede descifrar la bandera con la clave pública. Para eso, podemos usar el paquete OpenSSL para descifrar la bandera. Esta vez es un poco diferente y encontrará que el paquete OpenSSL no funcionará para este desafío.  Usaremos una herramienta de ataque RSA automatizada. Una secuencia de comandos de Python común es [RsaCtfTool] (https://github.com/Ganapati/RsaCtfTool)     En pocas palabras, esta herramienta encuentra la bandera fácilmente para usted de forma automática.  ______  ### Ejemplo de indicador: