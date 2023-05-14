---
title: "HackTheBox - Wyzwania - Kryptowaluty - Wezwanie"
date: 2020-10-07
draft: false
description: "Dowiedz się, jak odszyfrować tony DTMF za pomocą szyfru liczb pierwszych, aby rozwiązać wyzwanie Crypto - Call na HackTheBox."
tags: ["HackTheBox", "Crypto Challenge", "Sygnały DTMF", "Szyfr liczb pierwszych", "Odszyfrowanie", "Rozwiązywanie zagadek", "Kryptografia", "Konwersja audio", "DialABC", "Decode.fr", "WAV", "MP3", "Częstotliwość", "Cecha matematyczna", "Flaga", "Audacity", "Wizualizer dźwiękowy", "Numery", "Menu automatycznych kasjerów", "Telefon płatny"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "Kreskówkowy telefon z zielonym ekranem i kłódką na nim, symbolizujący bezpieczeństwo i szyfrowanie, z tonami DTMF przedstawionymi w tle"
coverCaption: ""
---

Rozwiąż wyzwanie Crypto - Call na HackTheBox, dekodując tony DTMF w pliku sound.mp3. Przekonwertuj plik do .wav i użyj DialABC, aby uzyskać tekst szyfrujący. Rozdziel liczby i użyj szyfru liczb pierwszych na Decode.fr, aby ujawnić flagę. Przygotuj się do wystawienia na próbę swoich umiejętności w szyfrowaniu liczb pierwszych w tym ekscytującym wyzwaniu na HackTheBox."

______

## Provided Files:

Dostarczany jest jeden plik:
- sound.mp3

## Walk Through:

Odtwarzając plik **sound.mp3**, usłyszysz znajome dźwięki. Jeśli nie jesteś zaznajomiony z dźwiękami, które słyszysz, to są to **DTMF** (dual tone multi frequency) tony. Te same tony, które słyszałeś podczas wybierania numerów w telefonach płatnych lub podczas przechodzenia przez menu kasjera automatycznego.

Każdy ton ma określoną częstotliwość. Możesz uzyskać numery ręcznie, ale kto ma na to czas?[DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

Zabierz przekonwertowany plik do[DialABC](http://www.dialabc.com/sound/detect/index.html) i otrzymasz następujące dane wyjściowe:
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