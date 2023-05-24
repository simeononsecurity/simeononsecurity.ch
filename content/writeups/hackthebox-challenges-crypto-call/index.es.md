---
title: "HackTheBox - Desafíos - Crypto - Llamada"
date: 2020-10-07
draft: false
description: "Aprenda a descifrar tonos DTMF utilizando el cifrado de números primos para resolver el desafío Crypto - Call en HackTheBox."
tags: ["HackTheBox", "Desafío criptográfico", "Tonos DTMF", "Cifrado de números primos", "Descifrado", "Resolver rompecabezas", "Criptografía", "Conversión de audio", "DialABC", "Decode.fr", "WAV", "MP3", "Frecuencia", "Rasgo matemático", "Bandera", "Audacia", "visualizador sónico", "Números", "Menús de cajero automático", "Teléfono público"]
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

Cada tono tiene una frecuencia específica. Puede obtener los números manualmente, pero ¿quién tiene tiempo para eso? [DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

Lleve el archivo convertido a [DialABC](http://www.dialabc.com/sound/detect/index.html) y obtendrá el siguiente resultado:
```
2331434783711923431767372331117714113
```
 
Tenga en cuenta que si escucha el archivo de audio con atención o lo abre en **Audacity** o **Sonic Visualizer**, con una excepción, los números se emparejan en grupos de dos.
Si separas el número obtienes lo siguiente:
```
23 31 43 47 83 71 19 23 43 17 67 37 23 31 11 7 71 41 13
```

Organizado de esta manera, puede confundirse y pensar que podría ser HEX. no lo es
Presta mucha atención a los números. ¿Qué rasgo matemático comparten cada agrupación de números?....
Todos son números primos. Lo que debería llevarlo a probar el **cifrado de números primos** menos conocido.

usaremos [Decode.fr](https://www.dcode.fr/prime-numbers-cipher) para completar este desafío.
Envíe el texto cifrado antes de que lo separáramos y obtendrá la bandera.
```
2331434783711923431767372331117714113
```

______

### Ejemplo de indicador:
```
HTB{xxxxxxxxxxxxxxxxxxx}
```