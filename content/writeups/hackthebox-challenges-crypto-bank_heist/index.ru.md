---
title: "HackTheBox - Задачи - Криптовалюты - Ограбление банка"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["hackthebox", "криптография", "Шифр T9", "многошаговый шифр", "шифр атбаш", "кибербезопасность", "декодировать", "шифротекст", "вызов", "флаг", "кибербезопасность", "взлом", "изучить", "учебное пособие", "расшифровка шифра", "решение головоломок", "взлом кодов", "криптографическая задача", "навыки в области кибербезопасности", "онлайн-обучение"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "мультяшная дверь хранилища, отпираемая ключом, открывает сундук с сокровищами, и все это на фоне парижского городского пейзажа на закате."
coverCaption: ""
---

Исчерпывающее руководство по решению криптозадачи "Ограбление банка" на HackTheBox. Задача заключается в расшифровке [T9](https://simeononsecurity.com/articles/introduction-to-t9-cipher/) or [Multitap cipher](https://simeononsecurity.com/articles/introduction-to-t9-cipher/) текст с помощью Decode.fr и шифр-текст atbash с помощью CyberChef для раскрытия флага. Обязательно к прочтению для начинающих специалистов по кибербезопасности и всех, кто хочет повысить свою квалификацию в области криптографии.

## Предоставляемые файлы:

Для решения этой задачи вам предоставляется следующий шифротекст:

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## Walk Through:

**Очень ясно, что это либо шифр T9, либо Multitap.
Однако в данном случае шифр Multitap. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) имеет инструмент для декодирования.

Вы получите этот простой текст:
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

**Что это за хлам в конце, спросите вы? На самом деле это шифрованный текст Atbash.**

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


Мы будем использовать [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) расшифровать еще раз. Затем вы получаете свой флаг. Ух ты!

______

### Пример флага:

```
HTB{XXXXXXXXXXXXXXXXX}
```
