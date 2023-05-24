---
title: "HackTheBox - Défi - Crypto - RSA faible"
draft: false
description: "Apprenez à utiliser un outil d'attaque RSA automatisé, RsaCtfTool, pour résoudre facilement le défi HackTheBox Weak RSA Crypto."
tags: ["HackTheBox", "Défis", "Crypto", "RSA faible", "Outil RsaCtf", "Chiffrement RSA faible HTB", "Défi facile", "chiffrement RSA", "flag.enc", "key.pub", "Paquet OpenSSL", "outil d'attaque RSA automatisé", "script python", "Outil RsaCtf", "python3", "Clé publique", "déchiffrerfichier", "Exemple de drapeau"]
toc: true
cover: "/img/cover/A_cartoon_hacker_wearing_a_cape_and_a_mask_standing.png"
coverAlt: "Un hacker de dessin animé portant une cape et un masque, debout devant une porte de coffre-fort avec le logo HTB dessus et tenant un outil (comme une clé ou un tournevis) avec un fond vert symbolisant le succès et le drapeau dans une bulle au-dessus leur tête."
coverCaption: ""
---
 le défi HTB Weak RSA Crypto en toute simplicité. Basé sur le chiffrement RSA, ce défi facile nécessite l'utilisation d'un outil d'attaque RSA automatisé comme le RsaCtfTool. Obtenez le drapeau avec une simple commande et développez vos compétences en cryptographie avec les défis HackTheBox.

______

## Fichiers fournis :

**Les fichiers suivants vous sont fournis :**
- flag.enc
- clé.pub

## Procédure pas à pas:

À première vue, vous penseriez que vous pouvez déchiffrer le drapeau avec la clé publique.
Pour cela, nous pourrions utiliser le package OpenSSL pour déchiffrer le drapeau.
Cette fois, c'est un peu différent et vous constaterez que le package OpenSSL ne fonctionnera pas pour ce défi.

Nous utiliserons un outil d'attaque RSA automatisé. Un script python courant est le [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

```bash
python3 RsaCtfTool.py --publickey ./key.pub --uncipherfile ./flag.enc 
```
  
En termes simples, cet outil trouve facilement le drapeau pour vous de manière automatisée.

______

Exemple d'indicateur ### :
```
HTB{XXXXXX_XXXXXXX_XXXXXX}
```
