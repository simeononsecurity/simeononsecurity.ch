---
title: "HackTheBox - Desafios - Criptografia - Chamada"
date: 2020-10-07
draft: false
description: "Aprenda como descriptografar tons DTMF usando cifra de número primo para resolver o desafio Crypto - Call no HackTheBox."
tags: ["HackTheBox", "Desafio criptográfico", "Tons DTMF", "Cifra de número primo", "Descriptografia", "Resolvendo quebra-cabeças", "Criptografia", "Conversão de Áudio", "DialABC", "Decode.fr", "WAV", "MP3", "Frequência", "característica matemática", "Bandeira", "Audácia", "Visualizador Sônico", "Números", "Menus de Caixa Automático", "telefone público"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "Um telefone de desenho animado com uma tela verde e um cadeado, simbolizando segurança e criptografia, com tons DTMF representados em segundo plano"
coverCaption: ""
---

Resolva o desafio Crypto - Call no HackTheBox decodificando os tons DTMF no arquivo sound.mp3. Converta o arquivo para .wav e use DialABC para obter o texto cifrado. Separe os números e use a cifra de número primo em Decode.fr para revelar o sinalizador. Prepare-se para testar suas habilidades em cifras de números primos neste emocionante desafio no HackTheBox."

______

## Arquivos Fornecidos:

Você recebe um arquivo:
- som.mp3

## Passeio por:

Tocando o **sound.mp3**, você ouvirá um som familiar. Se você não estiver familiarizado, os sons que você está ouvindo são tons **DTMF** (dual tone multifrequency). Os mesmos tons que você costumava ouvir ao discar em um telefone público ou ao acessar os menus do caixa eletrônico.

Cada tom tem uma frequência específica. Você poderia obter os números manualmente, mas quem tem tempo para isso? [DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

Leve o arquivo convertido para [DialABC](http://www.dialabc.com/sound/detect/index.html) e você obterá a seguinte saída:
```
2331434783711923431767372331117714113
```
 
Observe que, se você ouvir o arquivo de áudio com atenção ou abri-lo no **Audacity** ou **Sonic Visualizer**, com uma exceção, os números são emparelhados em grupos de dois.
Se você separar o número, obterá o seguinte:
```
23 31 43 47 83 71 19 23 43 17 67 37 23 31 11 7 71 41 13
```

Organizado assim, você pode ficar confuso e pensar que pode ser HEX. Não é.
Preste bastante atenção nos números. Que característica matemática cada grupo de números compartilha?....
São todos números primos. O que deve levá-lo a experimentar a **cifra de número primo** menos conhecida.

nós vamos usar [Decode.fr](https://www.dcode.fr/prime-numbers-cipher) para completar este desafio.
Envie o texto cifrado antes de separá-lo e você receberá o sinalizador.
```
2331434783711923431767372331117714113
```

______

### Exemplo de sinalização:
```
HTB{xxxxxxxxxxxxxxxxxxx}
```