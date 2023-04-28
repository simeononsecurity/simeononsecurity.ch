---
title: "HackTheBox - Challenges - Crypto - Call"
date: 2020-10-07
draft: false
description: "Learn how to decrypt DTMF tones using prime number cipher to solve the Crypto - Call challenge on HackTheBox."
tags: ["HackTheBox", "Crypto Challenge", "DTMF Tones", "Prime Number Cipher", "Decryption", "Solving Puzzles", "Cryptography", "Audio Conversion", "DialABC", "Decode.fr", "WAV", "MP3", "Frequency", "Mathematical Trait", "Flag", "Audacity", "Sonic Visualizer", "Numbers", "Automated Teller Menus", "Pay Phone"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "A cartoon phone with a green screen and a padlock on it, symbolizing security and encryption, with DTMF tones depicted in the backgroun"
coverCaption: ""
---
```
2331434783711923431767372331117714113
```
```
23 31 43 47 83 71 19 23 43 17 67 37 23 31 11 7 71 41 13
```
```
2331434783711923431767372331117714113
```
```
HTB{xxxxxxxxxxxxxxxxxxx}
```
 Resuelve el desafío Crypto - Call en HackTheBox decodificando los tonos DTMF en el archivo sound.mp3. Convierta el archivo a .wav y use DialABC para obtener el texto grabado. Separe los números y use el cifrado de números primos en Decode.fr para revelar la bandera. Prepárese para poner a prueba sus habilidades en el activador de números primos en este emocionante desafío en HackTheBox".  ______  ##Archivos provistos:  Se le proporciona un archivo: - sonido.mp3  ## Caminar a través de:  Al reproducir **sound.mp3**, escuchará un sonido familiar. Si no está conociendo, los sonidos que están escuchando son tonos **DTMF** (multifrecuencia de doble tono). Los mismos tonos que solían escuchar al marcar en un teléfono público o al pasar por los menús de los cajeros automáticos.  Cada tono tiene una frecuencia específica. Puede obtener los números manualmente, pero ¿quién tiene tiempo para eso? [DialABC](http://www.dialabc.com/sound/detect/index.html) tiene una gran herramienta para esto, pero no admite archivos mp3. Primero, tendrás que convertirlo a .wav con esta [herramienta](https://online-audio-converter.com/)  Lleve el archivo convertido a [DialABC](http://www.dialabc.com/sound/detect/index.html) y obtenga el siguiente resultado:   Tenga en cuenta que si escucha el archivo de audio con atención o lo abre en **Audacity** o **Sonic Visualizer**, con una excepción, los números se emparejan en grupos de dos. Si separas el número obtienes lo siguiente:  Organizado de esta manera, puede confundirse y pensar que podría ser HEX. no lo es Presta mucha atencion a los numeros. ¿Qué rasgo matemático comparte cada agrupación de números?.... Todos son números primos. Lo que debería llevar a probar el **cifrado de números primos** menos conocido.  Usaremos [Decode.fr](https://www.dcode.fr/prime-numbers-cipher) para completar este desafío. Envíe el texto grabado antes de que lo separemos y obtengamos la bandera.  ______  ### Ejemplo de indicador: