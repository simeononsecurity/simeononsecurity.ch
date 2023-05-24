---
title: "HackTheBox - Sfide - Cripto - Chiama"
date: 2020-10-07
draft: false
description: "Scopri come decrittografare i toni DTMF utilizzando la crittografia dei numeri primi per risolvere la sfida Crypto - Call su HackTheBox."
tags: ["HackTheBox", "Cripto sfida", "Toni DTMF", "Cifrario di numeri primi", "Decrittazione", "Risolvere enigmi", "Crittografia", "Conversione audio", "Comporre ABC", "Decodifica.fr", "WAV", "Mp3", "Frequenza", "Tratto matematico", "Bandiera", "Audacia", "Visualizzatore sonico", "Numeri", "Menu di cassa automatica", "Telefono a pagamento"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "Un telefono animato con uno schermo verde e un lucchetto, simbolo di sicurezza e crittografia, con toni DTMF raffigurati sullo sfondo"
coverCaption: ""
---

Risolvi la sfida Crypto - Call su HackTheBox decodificando i toni DTMF nel file sound.mp3. Converti il file in .wav e usa DialABC per ottenere il testo cifrato. Separa i numeri e usa la cifratura dei numeri primi su Decode.fr per rivelare la bandiera. Preparati a mettere alla prova le tue abilità nel cifrare i numeri primi in questa entusiasmante sfida su HackTheBox."

______

## File forniti:

Ti viene fornito un file:
- suono.mp3

## Procedura dettagliata:

Riproducendo **sound.mp3**, sentirai un suono familiare. Se non hai familiarità, i suoni che stai ascoltando sono i toni **DTMF** (dual tone multi frequency). Gli stessi toni che si sentivano mentre si componeva un numero su un telefono pubblico o mentre si accedeva ai menu di un cassiere automatico.

Ogni tono ha una frequenza specifica. Potresti ottenere i numeri manualmente, ma chi ha il tempo per farlo? [DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

Porta il file convertito in [DialABC](http://www.dialabc.com/sound/detect/index.html) e otterrai il seguente output:
```
2331434783711923431767372331117714113
```
 
Tieni presente che se ascolti attentamente il file audio o lo apri in **Audacity** o **Sonic Visualizer**, con un'eccezione, i numeri vengono accoppiati in gruppi di due.
Se si separa il numero si ottiene quanto segue:
```
23 31 43 47 83 71 19 23 43 17 67 37 23 31 11 7 71 41 13
```

Organizzato in questo modo, potresti essere confuso e pensare che potrebbe essere HEX. Non lo è.
Fai molta attenzione ai numeri. Quale tratto matematico condivide ogni raggruppamento di numeri?....
Sono tutti numeri primi. Il che dovrebbe portarti a provare il meno noto **cifrario dei numeri primi**.

Useremo [Decode.fr](https://www.dcode.fr/prime-numbers-cipher) per completare questa sfida.
Invia il testo cifrato da prima che lo separassimo e otterrai la bandiera.
```
2331434783711923431767372331117714113
```

______

### Flag Esempio:
```
HTB{xxxxxxxxxxxxxxxxxxx}
```