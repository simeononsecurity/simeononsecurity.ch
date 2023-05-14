---
title: "HackTheBox - Desafio - Criptografia - RSA fraco"
draft: false
description: "Aprenda a usar uma ferramenta automatizada de ataque RSA, RsaCtfTool, para resolver facilmente o desafio HackTheBox Weak RSA Crypto."
tags: ["HackTheBox", "desafios", "Criptografia", "RSA fraco", "RsaCtfToolName", "Criptografia RSA Fraca HTB", "desafio fácil", "cifra RSA", "flag.enc", "key.pub", "pacote OpenSSL", "ferramenta automatizada de ataque RSA", "script python", "RsaCtfToolName", "python3", "chave pública", "uncipherfile", "Exemplo de sinalizador"]
toc: true
cover: "/img/cover/A_cartoon_hacker_wearing_a_cape_and_a_mask_standing.png"
coverAlt: "Um hacker de desenho animado usando uma capa e uma máscara, parado na frente de uma porta de cofre com o logotipo HTB e segurando uma ferramenta (como uma chave inglesa ou chave de fenda) com um fundo verde simbolizando o sucesso e a bandeira em um balão acima a cabeça deles."
coverCaption: ""
---
 o desafio HTB Weak RSA Crypto com facilidade. Com base na cifra RSA, esse desafio fácil requer o uso de uma ferramenta automatizada de ataque RSA como o RsaCtfTool. Obtenha a bandeira com um comando simples e expanda suas habilidades de criptografia com os desafios do HackTheBox.

______

## Arquivos Fornecidos:

**Você recebe os seguintes arquivos:**
- flag.enc
- key.pub

## Passo a passo:

À primeira vista, você pensaria que pode descriptografar o sinalizador com a chave pública.
Para isso, podemos usar o pacote OpenSSL para descriptografar o sinalizador.
Desta vez é um pouco diferente e você descobrirá que o pacote OpenSSL não funcionará para este desafio.

Usaremos uma ferramenta de ataque RSA automatizada. Um script python comum é o[RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

```bash
python3 RsaCtfTool.py --publickey ./key.pub --uncipherfile ./flag.enc 
```
  
Simply put, this tool finds the flag easily for you in an automated fashion.

______

### Flag Example:
```
HTB{XXXXXX_XXXXXXX_XXXXXX}
```
