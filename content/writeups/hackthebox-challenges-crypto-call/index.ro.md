---
title: "HackTheBox - Provocări - Crypto - Apel"
date: 2020-10-07
draft: false
description: "Aflați cum să decriptați tonurile DTMF utilizând cifra primelor pentru a rezolva provocarea Crypto - Call pe HackTheBox."
tags: ["HackTheBox", "Crypto Challenge", "Tonuri DTMF", "Cifrarea numărului prim", "Decriptare", "Rezolvarea puzzle-urilor", "Criptografie", "Conversie audio", "DialABC", "Decode.fr", "WAV", "MP3", "Frecvență", "Trăsătură matematică", "Steag", "Îndrăzneală", "Vizualizator sonic", "Numerele", "Meniuri automate", "Telefon cu plată"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "Un telefon din desene animate cu un ecran verde și un lacăt pe el, simbolizând securitatea și criptarea, cu tonuri DTMF reprezentate în fundal"
coverCaption: ""
---

Rezolvați provocarea Crypto - Call pe HackTheBox decodând tonurile DTMF din fișierul sound.mp3. Convertiți fișierul în .wav și utilizați DialABC pentru a obține textul cifrat. Separați numerele și folosiți cifra de numere prime pe Decode.fr pentru a dezvălui steagul. Pregătește-te să-ți pui la încercare abilitățile în cifrarea numerelor prime în această provocare interesantă pe HackTheBox.”

______

## Fișiere furnizate:

Vi se oferă un singur fișier:
- sunet.mp3

## Plimbare prin:

Redând **sound.mp3**, veți auzi un sunet familiar. Dacă nu sunteți familiarizat, sunetele pe care le auziți aud tonuri **DTMF** (ton dual multifrecvență). Aceleași tonuri pe care obișnuiam să le auziți când formați de la un telefon public sau când accesați meniurile de la casierul automat.

Fiecare ton are o frecvență specifică. Puteți obține numerele manual, dar cine are timp pentru asta? [DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

Luați fișierul convertit în [DialABC](http://www.dialabc.com/sound/detect/index.html) și veți obține următorul rezultat:
```
2331434783711923431767372331117714113
```
 
Rețineți că, dacă ascultați fișierul audio cu atenție sau îl deschideți în **Audacity** sau **Sonic Visualizer**, cu o singură excepție, numerele sunt împerecheate în grupuri de câte doi.
Dacă separați numărul, obțineți următoarele:
```
23 31 43 47 83 71 19 23 43 17 67 37 23 31 11 7 71 41 13
```

Organizat astfel, s-ar putea să fii confuz și să te gândești că ar putea fi HEX. Nu este.
Acordați o atenție deosebită numerelor. Ce trăsătură matematică are fiecare grupare de numere?...
Toate sunt numere prime. Ceea ce ar trebui să vă aducă să încercați **cifrul numerelor prime** mai puțin cunoscut.

Vom folosi [Decode.fr](https://www.dcode.fr/prime-numbers-cipher) pentru a finaliza această provocare.
Trimiteți textul cifrat de înainte de a-l separa și veți primi steagul.
```
2331434783711923431767372331117714113
```

______

### Exemplu de semnalizare:
```
HTB{xxxxxxxxxxxxxxxxxxx}
```