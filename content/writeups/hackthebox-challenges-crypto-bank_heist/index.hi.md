---
title: "HackTheBox - Challenges - Crypto - Bank Heist"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["hackthebox", "cryptography", "T9 cipher", "multitap cipher", "atbash cipher", "cyber security", "decode", "ciphertext", "challenge", "flag", "cybersecurity", "hacking", "learn", "tutorial", "cipher decoding", "puzzle solving", "codebreaking", "cryptography challenge", "cybersecurity skills", "online learning"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "a cartoon vault door being unlocked with a key revealing a treasure chest, all set against a backdrop of a Parisian cityscape at sunset."
coverCaption: ""
---
```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```
```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```
```
HTB{XXXXXXXXXXXXXXXXX}
```

 HackTheBox पर "बैंक धोखाधड़ी" क्रिप्टो चुनौती को हल करने के लिए एक व्यापक गाइड। इस चुनौती में ध्वजा को प्रकट करने के लिए Decode.fr का उपयोग करके एक T9 या मल्टीटैप सिफर टेक्स्ट को डिकोड करना और साइबरशेफ का उपयोग करके एक एटबैश सिफर टेक्स्ट शामिल है। आकाक्षी साइबर सुरक्षा पेशेवर और क्रिप्टोग्राफी में अपना खर्च बढ़ाने के लिए किसी भी व्यक्ति के लिए अनिवार्य रूप से पढ़ें।  ## प्रदान की गई फ़ाइलें:  इस चुनौती के लिए आपको निम्नलिखित सिफर पाठ प्रदान किया गया है:   ______  ## के माध्यम से नीचे:  ** बहुत स्पष्ट रूप से, यह या तो एक टी9 या मल्टी टैप सिफर है।** हालाँकि, इस उदाहरण में मल्टीप्ल सरल है। [Decode.fr](https://www.dcode.fr/multiap-abc-cipher) में इसे डिकोड करने के लिए एक टूल है।  आपको यह संदीप पाठ मिलेगा:  **अंत में वह जंक क्या है जो आप पूछ सकते हैं? वैसे यह वास्तव में एक एथैश सिफर टेक्स्ट है। **    एक बार और समझने के लिए [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) का इस्तेमाल करेंगे। फिर आपके पास अपना झंडा है। वाह!  ______  ### ध्वजा उदाहरण: 