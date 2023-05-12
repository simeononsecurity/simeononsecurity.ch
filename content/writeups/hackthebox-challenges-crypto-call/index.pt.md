---
title: "HackTheBox - Desafios - Criptografia - Chamada"
date: 2020-10-07
draft: false
description: "Aprenda como descriptografar tons DTMF usando cifra de número primo para resolver o desafio Crypto - Call no HackTheBox."
tags: ["HackTheBox","Desafio Criptográfico","Tons DTMF","Cifra de Número Primário","Desencriptação","Resolvendo quebra-cabeças","Criptografia","Conversão de áudio","DialABC","Decode.fr","WAV","MP3","Frequência","Traço Matemático","Bandeira","Audácia","Visualizador Sônico","Números","Menus de Caixa Automático","Telefone público"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "Um telefone de desenho animado com tela verde e um cadeado, simbolizando segurança e criptografia, com tons DTMF representados no fundo"
coverCaption: ""
---

Resolva o desafio Crypto - Call no HackTheBox decodificando os tons DTMF no arquivo sound.mp3. Converta o arquivo para .wav e use DialABC para obter o texto cifrado. Separe os números e use a cifra de número primo em Decode.fr para revelar o sinalizador. Prepare-se para testar suas habilidades em cifras de números primos neste emocionante desafio no HackTheBox."

______

## Arquivos Fornecidos:

Você recebe um arquivo:
- som.mp3

## Passeio por:

Tocando o **sound.mp3**, você ouvirá um som familiar. Se você não estiver familiarizado, os sons que você está ouvindo são tons **DTMF** (dual tone multifrequency). Os mesmos tons que você costumava ouvir ao discar em um telefone público ou ao acessar os menus do caixa eletrônico.

Cada tom tem uma frequência específica. Você poderia obter os números manualmente, mas quem tem tempo para isso?[DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

Leve o arquivo convertido para[DialABC](http://www.dialabc.com/sound/detect/index.html) e você obterá a seguinte saída:
```
2331434783711923431767372331117714113
```
 
Take notice that if you listen to the audio file carefully or open it in **Audacity** or **Sonic Visualizer** that, with one exception, the numbers are paired in groups of two.
If you separate out the number you get the following:
```
23 31 43 47 83 71 19 23 43 17 67 37 23 31 11 7 71 41 13
```

Organized like this, you might be confused and think that it might be HEX. It isn't.  
Pay close attention to the numbers. What mathematical trait do each grouping of numbers share?....
They are all prime numbers. Which should bring you to try the lesser known **prime number cipher**.

We'll use [Decode.fr](https://www.dcode.fr/prime-numbers-cipher) to complete this challenge.   
Submit the cipher text from before we separated it out and you'll get the flag.
```
2331434783711923431767372331117714113
```

______

### Flag Example:
```
HTB{xxxxxxxxxxxxxxxxxxx}
```