---
title: "ਹੈਕਬੌਕਸ - ਚੁਣੌਤੀਆਂ - ਕ੍ਰਿਪਟੋ - ਬੈਂਕ ਚੋਰੀ"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["hackthebox", "ਕ੍ਰਿਪਟੋਗ੍ਰਾਫੀ", "T9 ਸਿਫਰ", "ਮਲਟੀਟੈਪ ਸਾਈਫਰ", "atbash ਸਿਫਰ", "ਸਾਈਬਰ ਸੁਰੱਖਿਆ", "ਡੀਕੋਡ", "ਸਿਫਰਟੈਕਸਟ", "ਚੁਣੌਤੀ", "ਝੰਡਾ", "ਸਾਈਬਰ ਸੁਰੱਖਿਆ", "ਹੈਕਿੰਗ", "ਸਿੱਖੋ", "ਟਿਊਟੋਰਿਅਲ", "ਸਿਫਰ ਡੀਕੋਡਿੰਗ", "ਬੁਝਾਰਤ ਹੱਲ", "ਕੋਡਬ੍ਰੇਕਿੰਗ", "ਕ੍ਰਿਪਟੋਗ੍ਰਾਫੀ ਚੁਣੌਤੀ", "ਸਾਈਬਰ ਸੁਰੱਖਿਆ ਹੁਨਰ", "ਆਨਲਾਈਨ ਸਿਖਲਾਈ"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "ਇੱਕ ਕਾਰਟੂਨ ਵਾਲਟ ਦਾ ਦਰਵਾਜ਼ਾ ਇੱਕ ਚਾਬੀ ਨਾਲ ਖੋਲ੍ਹਿਆ ਜਾ ਰਿਹਾ ਹੈ ਜੋ ਇੱਕ ਖਜ਼ਾਨੇ ਦੀ ਛਾਤੀ ਨੂੰ ਪ੍ਰਗਟ ਕਰਦਾ ਹੈ, ਜੋ ਸੂਰਜ ਡੁੱਬਣ ਵੇਲੇ ਪੈਰਿਸ ਦੇ ਇੱਕ ਸ਼ਹਿਰ ਦੇ ਦ੍ਰਿਸ਼ ਦੇ ਪਿਛੋਕੜ ਵਿੱਚ ਸੈੱਟ ਕੀਤਾ ਗਿਆ ਹੈ।"
coverCaption: ""
---

HackTheBox 'ਤੇ "ਬੈਂਕ ਹੀਸਟ" ਕ੍ਰਿਪਟੋ ਚੁਣੌਤੀ ਨੂੰ ਹੱਲ ਕਰਨ ਲਈ ਇੱਕ ਵਿਆਪਕ ਗਾਈਡ। ਚੁਣੌਤੀ ਵਿੱਚ Decode.fr ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ T9 ਜਾਂ ਮਲਟੀਟੈਪ ਸਾਈਫਰ ਟੈਕਸਟ ਨੂੰ ਡੀਕੋਡ ਕਰਨਾ ਅਤੇ ਫਲੈਗ ਨੂੰ ਪ੍ਰਗਟ ਕਰਨ ਲਈ CyberChef ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਇੱਕ ਐਟਬਾਸ਼ ਸਾਈਫਰ ਟੈਕਸਟ ਸ਼ਾਮਲ ਹੈ। ਚਾਹਵਾਨ ਸਾਈਬਰ ਸੁਰੱਖਿਆ ਪੇਸ਼ੇਵਰਾਂ ਅਤੇ ਕ੍ਰਿਪਟੋਗ੍ਰਾਫੀ ਵਿੱਚ ਆਪਣੇ ਹੁਨਰ ਨੂੰ ਵਧਾਉਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਨ ਵਾਲੇ ਕਿਸੇ ਵੀ ਵਿਅਕਤੀ ਲਈ ਪੜ੍ਹਨਾ ਲਾਜ਼ਮੀ ਹੈ।

## ਪ੍ਰਦਾਨ ਕੀਤੀਆਂ ਫਾਈਲਾਂ:

ਇਸ ਚੁਣੌਤੀ ਲਈ ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਸਿਫਰ ਟੈਕਸਟ ਨਾਲ ਪ੍ਰਦਾਨ ਕੀਤਾ ਗਿਆ ਹੈ:

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## Walk Through:

**Very clearly, this is either a T9 or Multitap cipher.**  
Multitap is the cipher in this instance though. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) has a tool to decode this.

You'll get this plain text:
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

**What is that junk at the end you might ask? Well it's actually an atbash cipher text.**

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


We'll use [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) to decipher one more time. Then you have your flag. Whoot!

______

### Flag Example:

```
HTB{XXXXXXXXXXXXXXXXX}
```
