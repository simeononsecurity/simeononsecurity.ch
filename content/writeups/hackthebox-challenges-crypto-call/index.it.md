---
title: "HackTheBox - Sfide - Cripto - Chiamata"
date: 2020-10-07
draft: false
description: "Scopri come decrittografare i toni DTMF utilizzando la crittografia dei numeri primi per risolvere la sfida Crypto - Call su HackTheBox."
tags: ["HackTheBox","Cripto sfida","Toni DTMF","Cifrario di numeri primi","Decrittografia","Risoluzione di enigmi","Crittografia","Conversione audio","ComponiABC","Decode.it","WAV","MP3","Frequenza","Tratto matematico","Bandiera","Audacia","Visualizzatore sonoro","Numeri","Menu cassiere automatico","Telefono pubblico"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "Un telefono animato con uno schermo verde e un lucchetto sopra, simbolo di sicurezza e crittografia, con toni DTMF raffigurati sullo sfondo"
coverCaption: ""
---

Risolvi la sfida Crypto - Call su HackTheBox decodificando i toni DTMF nel file sound.mp3. Converti il file in .wav e usa DialABC per ottenere il testo cifrato. Separa i numeri e usa la cifratura dei numeri primi su Decode.fr per rivelare la bandiera. Preparati a mettere alla prova le tue abilità nel cifrare i numeri primi in questa entusiasmante sfida su HackTheBox."

______

## File forniti:

Ti viene fornito un file:
- suono.mp3

## Procedura dettagliata:

Riproducendo **sound.mp3**, sentirai un suono familiare. Se non hai familiarità, i suoni che stai ascoltando sono i toni **DTMF** (dual tone multi frequency). Gli stessi toni che si sentivano mentre si componeva un numero su un telefono pubblico o mentre si accedeva ai menu di un cassiere automatico.

Ogni tono ha una frequenza specifica. Potresti ottenere i numeri manualmente, ma chi ha il tempo per farlo?[DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

Porta il file convertito in[DialABC](http://www.dialabc.com/sound/detect/index.html) e otterrai il seguente output:
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