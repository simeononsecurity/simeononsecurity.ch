---
title: "HackTheBox - Desafios - Criptografia - Assalto a Banco"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["hackear a caixa","criptografia","cifra T9","cifra multitap","cifra atbash","cíber segurança","decodificar","texto cifrado","desafio","bandeira","cíber segurança","hacking","aprender","tutorial","decodificação de cifras","resolução de quebra-cabeças","descodificador","desafio da criptografia","habilidades de cibersegurança","aprendizagem online"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "uma porta de cofre de desenho animado sendo destrancada com uma chave revelando um baú de tesouro, tudo tendo como pano de fundo uma paisagem urbana parisiense ao pôr do sol."
coverCaption: ""
---

Um guia completo para resolver o desafio de criptografia "Bank Heist" no HackTheBox. O desafio envolve decodificar um texto cifrado T9 ou Multitap usando Decode.fr e um texto cifrado atbash usando CyberChef para revelar a bandeira. Uma leitura obrigatória para aspirantes a profissionais de segurança cibernética e para qualquer pessoa que queira aprimorar suas habilidades em criptografia.

## Arquivos Fornecidos:

Para este desafio, você recebe o seguinte texto cifrado:

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## Walk Through:

**Very clearly, this is either a T9 or Multitap cipher.**  
Multitap is the cipher in this instance though. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) has a tool to decode this.

You'll get this plain text:
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

**What is that junk at the end you might ask? Well it's actually an atbash cipher text.**

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


We'll use [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) to decipher one more time. Then you have your flag. Whoot!

______

### Flag Example:

```
HTB{XXXXXXXXXXXXXXXXX}
```
