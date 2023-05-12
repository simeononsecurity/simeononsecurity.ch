---
title: "HackTheBox - Вызовы - Крипто - Звонок"
date: 2020-10-07
draft: false
description: «Узнайте, как расшифровывать тональные сигналы DTMF с помощью шифра простых чисел, чтобы решить задачу Crypto — Call на HackTheBox».
tags: ["ХакБокс",«Крипто вызов»,«Тоны DTMF»,«Шифр простого числа»,"Расшифровка",«Решение головоломок»,"Криптография",«Аудиопреобразование»,"ДиалАБС","Decode.fr","ВАВ","МП3","Частота",«Математическая черта»,"Флаг","Мужество",«Звуковой визуализатор»,«Числа»,«Меню банкомата»,"Телефон-платник"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: «Мультяшный телефон с зеленым экраном и замком на нем, символизирующим безопасность и шифрование, с тонами DTMF, изображенными на заднем плане»
coverCaption: ""
---

Решите задачу Crypto - Call на HackTheBox, расшифровав тональные сигналы DTMF в файле sound.mp3. Преобразуйте файл в .wav и используйте DialABC, чтобы получить зашифрованный текст. Разделите числа и используйте шифр простых чисел на Decode.fr, чтобы раскрыть флаг. Приготовьтесь испытать свои навыки в шифровании простых чисел в этом захватывающем состязании на HackTheBox».

______

## Предоставленные файлы:

Вам предоставляется один файл:
- звук.mp3

## Прохождение:

Проигрывая **sound.mp3**, вы услышите знакомый звук. Если вы не знакомы, звуки, которые вы слышите, являются тонами **DTMF** (двухтональные многочастотные). Те же звуки, которые вы привыкли слышать при наборе номера в телефоне-автомате или при работе с меню банкомата.

Каждый тон имеет определенную частоту. Можно было получить номера вручную, но у кого есть на это время?[DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

Возьмите преобразованный файл в[DialABC](http://www.dialabc.com/sound/detect/index.html) и вы получите следующий вывод:
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