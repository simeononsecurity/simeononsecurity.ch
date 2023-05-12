---
title: „HackTheBox – Provocări – Crypto – Apel”
date: 2020-10-07
draft: false
description: „Aflați cum să decriptați tonurile DTMF folosind cifrul numerelor prime pentru a rezolva provocarea Crypto - Call pe HackTheBox.”
tags: [„HackTheBox”,„Crypto Challenge”,„Tonuri DTMF”,„Cifrul numărului prim”,„Decriptare”,„Rezolvarea puzzle-urilor”,"Criptografie",„Conversie audio”,„DialABC”,„Decode.fr”,„WAV”,„MP3”,"Frecvență",„Trăsătură matematică”,"Steag","Îndrăzneală",„Sonic Visualizer”,„Numere”,„Meniuri automate pentru casă”,„Telefon cu plată”]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: „Un telefon din desene animate cu un ecran verde și un lacăt pe el, simbolizând securitatea și criptarea, cu tonuri DTMF descrise în fundal”
coverCaption: ""
---

Rezolvați provocarea Crypto - Call pe HackTheBox decodând tonurile DTMF din fișierul sound.mp3. Convertiți fișierul în .wav și utilizați DialABC pentru a obține textul cifrat. Separați numerele și utilizați cifra de numere prime pe Decode.fr pentru a dezvălui steagul. Pregătiți-vă să vă puneți la încercare abilitățile în cifrarea numerelor prime în această provocare interesantă pe HackTheBox.”

______

## Fișiere furnizate:

Vi se oferă un singur fișier:
- sunet.mp3

## Plimbare prin:

Redând **sound.mp3**, veți auzi un sunet familiar. Dacă nu sunteți familiarizat, sunetele pe care le auziți aud tonuri **DTMF** (dual tone multifrecvență). Aceleași tonuri pe care obișnuiți să le auziți când formați de la un telefon public sau când accesați meniurile de la casierul automat.

Fiecare ton are o frecvență specifică. Puteți obține numerele manual, dar cine are timp pentru asta?[DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

Luați fișierul convertit în[DialABC](http://www.dialabc.com/sound/detect/index.html) și veți obține următorul rezultat:
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