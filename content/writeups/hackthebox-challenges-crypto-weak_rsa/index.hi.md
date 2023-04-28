---
title: "HackTheBox - Challenge - Crypto - Weak RSA"
draft: false
description: "Learn how to use an automated RSA attack tool, RsaCtfTool, to easily solve the HackTheBox Weak RSA Crypto challenge."
tags: ["HackTheBox", "Challenges", "Crypto", "Weak RSA", "RsaCtfTool", "HTB Weak RSA Crypto", "Easy challenge", "RSA cipher", "flag.enc", "key.pub", "OpenSSL package", "automated RSA attack tool", "python script", "RsaCtfTool", "python3", "public key", "uncipherfile", "Flag Example"]
toc: true
cover: "/img/cover/A_cartoon_hacker_wearing_a_cape_and_a_mask_standing.png"
coverAlt: "A cartoon hacker wearing a cape and a mask, standing in front of a vault door with the HTB logo on it and holding a tool (such as a wrench or a screwdriver) with a green background symbolizing success and the flag in a speech bubble above their head."
coverCaption: ""
---
```bash
python3 RsaCtfTool.py --publickey ./key.pub --uncipherfile ./flag.enc 
```
```
HTB{XXXXXX_XXXXXXX_XXXXXX}
```

HTB कमजोर RSA क्रिप्टो चुनौती को आसानी से हल करें। RSA सिफर के आधार पर, इस आसान चुनौती के लिए RsaCtfTool जैसे स्वचालित RSA अटैक टूल के उपयोग की आवश्यकता है। एक सामान्य क्रम के साथ ध्वज प्राप्त करें और हैकबॉक्स के साथ अपने क्रिप्टोकरंसी खर्च का विस्तार करें।  ______  ## प्रदान की गई फ़ाइलें:  ** आपकी वे फ़ाइलें प्रदान की जाती हैं:** - आदतन - की.पब  ## पैदल चलना:  पहली नज़र में, आपको लगता है कि आप ध्वज की सार्वजनिक कुंजी से क्रिप्ट कर सकते हैं। उसके लिए, हम फ़्लैग को डिक्रिप्ट करने के लिए OpenSSL पैकेज का उपयोग कर सकते हैं। इस बार यह थोड़ा अलग है और आप OpenSSL पैकेज इस चुनौती के लिए काम नहीं करेंगे।  हम एक आरएसए आक्रमण उपकरण का उपयोग करेंगे। [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool) एक सामान्य ड्रैगन लिप्सा है।     सीधे शब्दों में कहे, तो यह स्वचालित रूप से आपके लिए ध्वज को आसानी से ढूंढ लेता है।  ______  ### ध्वजा उदाहरण: