---
title: "HackTheBox - Challenges - Crypto - Call"
date: 2020-10-07
draft: false
description: "Learn how to decrypt DTMF tones using prime number cipher to solve the Crypto - Call challenge on HackTheBox."
tags: ["HackTheBox", "Crypto Challenge", "DTMF Tones", "Prime Number Cipher", "Decryption", "Solving Puzzles", "Cryptography", "Audio Conversion", "DialABC", "Decode.fr", "WAV", "MP3", "Frequency", "Mathematical Trait", "Flag", "Audacity", "Sonic Visualizer", "Numbers", "Automated Teller Menus", "Pay Phone"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "A cartoon phone with a green screen and a padlock on it, symbolizing security and encryption, with DTMF tones depicted in the backgroun"
coverCaption: ""
---
```
2331434783711923431767372331117714113
```
```
23 31 43 47 83 71 19 23 43 17 67 37 23 31 11 7 71 41 13
```
```
2331434783711923431767372331117714113
```
```
HTB{xxxxxxxxxxxxxxxxxxx}
```
 Sound.mp3 फ़ाइल में DTMF टोन को डिकोड करके हैकबॉक्स पर क्रिप्टो - कॉल प्रॉब्लम को हल करें। फ़ाइल को .wav में करें और सरल पाठ प्राप्त करने के लिए DialABC का उपयोग करें। चिह्नों को अलग करें और ध्वज प्रकट करने के लिए Decode.fr पर अभाज्य संख्या सिफर का उपयोग करें। HackTheBox पर इस रोमांचक चुनौती में पेश करने के लिए अपने कौशल को प्राइम नंबर सिफर में डालने के लिए तैयार हो जाइए।"  ______  ## प्रदान की गई फ़ाइलें:  आपको प्रदान किया गया एक नामांकन है: - ध्वनि एमपी 3  ## के माध्यम से नीचे:  **sound.mp3** चलने पर, आपको एक मशहूर-पहचानी आवाज़ सुनाई देगी। यदि आप संभावनाओं से परिचित नहीं हैं जो आप सुन रहे हैं **DTMF** (ड्युअल मल्टी टोन फ्रीक्वेंसी) स्वर सुन रहे हैं। वही स्वर जो आप फोन पर डायल करते समय या स्विच्ड टेलर के माध्यम से कई बार प्राप्त करते थे।  प्रत्येक स्वर की एक विशिष्ट क्रिया होती है। आप छत के रूप से नंबर प्राप्त कर सकते हैं, लेकिन उसके लिए पास टाइम है? [DialABC](http://www.dialabc.com/sound/detect/index.html) के पास इसके लिए एक बेहतरीन टूल है, लेकिन यह एमपी3 अनिवार्य को सपोर्ट नहीं करता। सबसे पहले, आप इसे [टूल](https://online-audio-converter.com/) से .wav में लाभ प्राप्त करेंगे  प्रमाण की गई फ़ाइल को [डायलबीसी](http://www.dialabc.com/sound/detect/index.html) पर ले जायें और आपको एक नया ब्लूम मिलेगा:   ध्यान दें कि यदि आप ऑडियो फ़ाइल को ध्यान में रखते हैं या इसे ** ऑडेसिटी** या ** सोनिक विज़ुअल मेकर ** में झाड़ते हैं, तो एक अपवाद के साथ, नंबर दो के टैग में जुड़ते हैं। यदि आप संख्या को अलग करते हैं तो आपको निम्नलिखित मिलते हैं:  इस तरह आप निकल सकते हैं और सोच सकते हैं कि यह जहर हो सकता है। यह नहीं है। पॉइंट पर दें विशेष ध्यान। विश्वसनीयता का प्रत्येक समूह किस गुण को साझा करता है?... वे सभी अज्य संख्याएँ हैं। जो आपको कम ज्ञात **अभ्य संख्या सिफर** को अवज्ञा करने के लिए देखें।  हम इस चुनौती को पूरा करने के लिए [Decode.fr](https://www.dcode.fr/prime-numbers-cipher) का इस्तेमाल करेंगे। इससे पहले कि हम इसे अलग कर दें, सिफर टेक्स्ट प्रस्ताव दें और आपको जावास्क्रिप्ट मिल जाएगा।  ______  ### ध्वज उदाहरण: