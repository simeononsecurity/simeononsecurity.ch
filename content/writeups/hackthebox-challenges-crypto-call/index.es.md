---
title: "HackTheBox - Desafíos - Crypto - Llamada"
date: 2020-10-07
draft: false
description: "Aprenda a descifrar tonos DTMF utilizando el cifrado de números primos para resolver el desafío Crypto - Call en HackTheBox".
tags: ["Hackear la caja","Desafío criptográfico","Tonos DTMF","Cifrado de números primos","Descifrado","Resolviendo rompecabezas","Criptografía","Conversión de audio","Marcar ABC","Decode.fr","WAV","MP3","Frecuencia","Rasgo Matemático","Bandera","Audacia","Visualizador Sónico","Números","Menús de cajero automático","Teléfono público"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "Un teléfono de dibujos animados con una pantalla verde y un candado, que simboliza la seguridad y el cifrado, con tonos DTMF representados en el fondo"
coverCaption: ""
---

Resuelve el desafío Crypto - Call en HackTheBox decodificando los tonos DTMF en el archivo sound.mp3. Convierta el archivo a .wav y use DialABC para obtener el texto cifrado. Separe los números y use el cifrado de números primos en Decode.fr para revelar la bandera. Prepárese para poner a prueba sus habilidades en el cifrado de números primos en este emocionante desafío en HackTheBox".

______

## Archivos proporcionados:

Se le proporciona un archivo:
- sonido.mp3

## Caminar a través de:

Al reproducir **sound.mp3**, escuchará un sonido familiar. Si no está familiarizado, los sonidos que está escuchando son tonos **DTMF** (multifrecuencia de doble tono). Los mismos tonos que solía escuchar al marcar en un teléfono público o al pasar por los menús de los cajeros automáticos.

Cada tono tiene una frecuencia específica. Puede obtener los números manualmente, pero ¿quién tiene tiempo para eso?[DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

Lleve el archivo convertido a[DialABC](http://www.dialabc.com/sound/detect/index.html) y obtendrá el siguiente resultado:
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