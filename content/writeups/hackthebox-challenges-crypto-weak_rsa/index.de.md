---
title: „HackTheBox – Challenge – Krypto – Schwaches RSA“
draft: false
description: „Erfahren Sie, wie Sie ein automatisiertes RSA-Angriffstool, RsaCtfTool, verwenden, um die HackTheBox Weak RSA Crypto-Herausforderung einfach zu lösen.“
tags: [„HackTheBox“,„Herausforderungen“,„Krypto“,„Schwacher RSA“,„RsaCtfTool“,„HTB Weak RSA Crypto“,„Einfache Herausforderung“,„RSA-Chiffre“,"flag.enc", "key.pub", „OpenSSL-Paket“,„Automatisiertes RSA-Angriffstool“,„Python-Skript“,„RsaCtfTool“,„python3“,"Öffentlicher Schlüssel",„Entschlüsselungsdatei“,„Flaggenbeispiel“]
toc: true
cover: "/img/cover/A_cartoon_hacker_wearing_a_cape_and_a_mask_standing.png"
coverAlt: „Ein Cartoon-Hacker mit Umhang und Maske steht vor einer Tresortür mit dem HTB-Logo darauf und hält ein Werkzeug (z. B. einen Schraubenschlüssel oder einen Schraubenzieher) mit einem grünen Hintergrund, der den Erfolg symbolisiert, und der Flagge in einer Sprechblase über ihrem Kopf.
coverCaption: „“
---
 Bewältigen Sie die HTB Weak RSA Crypto-Herausforderung mit Leichtigkeit. Basierend auf der RSA-Verschlüsselung erfordert diese einfache Herausforderung die Verwendung eines automatisierten RSA-Angriffstools wie RsaCtfTool. Holen Sie sich die Flagge mit einem einfachen Befehl und erweitern Sie Ihre Kryptokenntnisse mit HackTheBox-Herausforderungen.

______

## Bereitgestellte Dateien:

**Sie erhalten die folgenden Dateien:**
- flag.enc
- key.pub

## Komplettlösung:

Auf den ersten Blick könnte man meinen, man könne die Flagge mit dem öffentlichen Schlüssel entschlüsseln.
Dazu könnten wir das OpenSSL-Paket verwenden, um die Flagge zu entschlüsseln.
Diesmal ist es etwas anders und Sie werden feststellen, dass das OpenSSL-Paket für diese Herausforderung nicht funktioniert.

Wir verwenden ein automatisiertes RSA-Angriffstool. Ein gängiges Python-Skript ist das[RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

```bash
python3 RsaCtfTool.py --publickey ./key.pub --uncipherfile ./flag.enc 
```
  
Simply put, this tool finds the flag easily for you in an automated fashion.

______

### Flag Example:
```
HTB{XXXXXX_XXXXXXX_XXXXXX}
```
