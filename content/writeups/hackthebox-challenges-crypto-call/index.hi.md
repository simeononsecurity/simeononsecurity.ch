---
title: "HackTheBox - चुनौतियाँ - क्रिप्टो - कॉल"
date: 2020-10-07
draft: false
description: "हैकदबॉक्स पर क्रिप्टो - कॉल चुनौती को हल करने के लिए प्राइम नंबर सिफर का उपयोग करके डीटीएमएफ टोन को डिक्रिप्ट करना सीखें।"
tags: ["HackTheBox", "क्रिप्टो चुनौती", "डीटीएमएफ टोन", "प्राइम नंबर सिफर", "डिक्रिप्शन", "रहस्यों को सुलझाना", "क्रिप्टोग्राफी", "ऑडियो रूपांतरण", "डायलएबीसी", "डीकोड.एफआर", "WAV", "एमपी 3", "आवृत्ति", "गणितीय विशेषता", "झंडा", "धृष्टता", "सोनिक विज़ुअलाइज़र", "नंबर", "स्वचालित टेलर मेनू", "भुगतान फोन"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "हरे रंग की स्क्रीन वाला एक कार्टून फोन और उस पर एक पैडलॉक, सुरक्षा और एन्क्रिप्शन का प्रतीक, DTMF टोन के साथ पृष्ठभूमि में दर्शाया गया है"
coverCaption: ""
---

Sound.mp3 फ़ाइल में DTMF टोन को डिकोड करके हैकदबॉक्स पर क्रिप्टो - कॉल चुनौती को हल करें। फ़ाइल को .wav में कनवर्ट करें और सिफ़र पाठ प्राप्त करने के लिए DialABC का उपयोग करें। संख्याओं को अलग करें और ध्वज प्रकट करने के लिए Decode.fr पर अभाज्य संख्या सिफर का उपयोग करें। HackTheBox पर इस रोमांचक चुनौती में परीक्षण के लिए अपने कौशल को प्राइम नंबर सिफर में डालने के लिए तैयार हो जाइए।"

______

## प्रदान की गई फ़ाइलें:

आपको एक फ़ाइल प्रदान की जाती है:
- ध्वनि एमपी 3

## के माध्यम से चलो:

**sound.mp3** चलाने पर, आपको एक जानी-पहचानी आवाज़ सुनाई देगी। यदि आप उन ध्वनियों से परिचित नहीं हैं जो आप सुन रहे हैं **DTMF** (डुअल टोन मल्टी फ़्रीक्वेंसी) टोन सुन रहे हैं। वही स्वर जो आप पे फ़ोन पर डायल करते समय या स्वचालित टेलर मेनू के माध्यम से प्राप्त करते समय सुनते थे।

प्रत्येक स्वर की एक विशिष्ट आवृत्ति होती है। आप मैन्युअल रूप से नंबर प्राप्त कर सकते हैं, लेकिन उसके लिए किसके पास समय है?[DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

कनवर्ट की गई फ़ाइल को इसमें ले जाएं[DialABC](http://www.dialabc.com/sound/detect/index.html) और आपको निम्न आउटपुट मिलेगा:
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