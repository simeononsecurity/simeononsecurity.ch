---
title: "HackTheBox - चुनौतियाँ - क्रिप्टो - बैंक डकैती"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["हैकथबॉक्स","क्रिप्टोग्राफी","टी 9 सिफर","मल्टीटैप सिफर","एटबैश सिफर","साइबर सुरक्षा","डिकोड","सिफरटेक्स्ट","चुनौती","झंडा","साइबर सुरक्षा","हैकिंग","सीखना","ट्यूटोरियल","सिफर डिकोडिंग","पहेली सुलझाना","कोडब्रेकिंग","क्रिप्टोग्राफी चुनौती","साइबर सुरक्षा कौशल","ऑनलाइन सीखने"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "एक कार्टून तिजोरी के दरवाजे को एक चाबी से खोला जा रहा है, जो एक खजाने की छाती का खुलासा करता है, जो सूर्यास्त के समय पेरिस के शहर के दृश्य की पृष्ठभूमि के खिलाफ है।"
coverCaption: ""
---

HackTheBox पर "बैंक डकैती" क्रिप्टो चुनौती को हल करने के लिए एक व्यापक गाइड। इस चुनौती में ध्वज को प्रकट करने के लिए Decode.fr का उपयोग करके एक T9 या मल्टीटैप सिफर टेक्स्ट को डिकोड करना और साइबरशेफ का उपयोग करके एक एटबैश सिफर टेक्स्ट शामिल है। आकांक्षी साइबर सुरक्षा पेशेवरों और क्रिप्टोग्राफी में अपने कौशल को बढ़ाने के इच्छुक किसी भी व्यक्ति के लिए अवश्य पढ़ें।

## प्रदान की गई फ़ाइलें:

इस चुनौती के लिए आपको निम्नलिखित सिफर पाठ प्रदान किया गया है:

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
