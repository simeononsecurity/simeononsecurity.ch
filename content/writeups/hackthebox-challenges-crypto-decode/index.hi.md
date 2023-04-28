---
title: "HackTheBox - Challenges - Crypto - Decode"
date: 2020-10-07
draft: false
description: "Learn how to decode Fernet and Malboge ciphers to solve the HackTheBox Crypto Challenge and uncover the hidden flag."
tags: ["HackTheBox", "Challenges", "Crypto", "Decode", "Writeup", "Fernet Cipher", "Malboge Cipher", "Symmetric Encryption", "Cybersecurity", "Cryptography", "Penetration Testing", "Python", "Security", "Challenge", "CTF", "Flag", "Encryption", "Decryption", "Base64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "A cartoon hacker standing next to a large lock with one hand holding a Fernet logo key and the other hand holding a Malboge logo key while a flag is seen inside the lock"
coverCaption: ""
---
```
993gmULBNujjrZCDev3W8kAVaLkXiyHhCL3500188bA=
```
```
gAAAAABboRUb0FsuiYBk1tsXRDr6KAzU1xrNSUv7grB-G-dAEeyqj99kUebz466I2VcH5xDa5HEc5KkbgTklQ7tm9JCRPlJtRng1Ns3VEvbrk7B835OINfPnRbc-UIOnnCmW3CgMdMtf5wGLN299AZEzxIvuy71WC5d9xJDchyiORycuzCth95-4nTKphlNQQ2ko3DX72RxWeEjwt3mavnFXqcOCkGxUhJYmFltz_6ND56VGTrXZi_CK5xLODOX4sj1GNwN_CrU3sJ0obTdA2wF5OaDZLbA1GBPfK0PDlC9WxoUf85K0tFXKfqbt3c5YqtqfytNG5gTkbDFM2NjE7BveBf1DP9ca8g==
```
```
RCdgTl45OFs8O3tGMlZVNTRRPythcUw6bVxJNmlYJmYkMEBSeFBfdSldeHFwdW5tM3Fwb2htZmUrTGJnZl9eXSNhYFleV1Z6VFNyUVZVTnJMUVBPTkdrS0QsSEFlKERDPDtfPz5+fTVZOTg3dzUuUjJyMC8oJyZKKikoJyYlfHtBeX53djx6eXhxWTZ0c1VUcG9oLnk=
```
```
D'`N^98[<;{F2VU54Q?+aqL:m\I6iX&f$0@RxP_u)]xqpunm3qpohmfe+Lbgf_^]#a`Y^WVzTSXQVUNrLQPONGkKD,HAe(DC<;_?>
```
```
HTB{x_xxx_xxxx}
```

 HackTheBox क्रिप्टो डिकोड चुनौती के बारे में विस्तृत जानकारी प्राप्त करें। जानकारी के दो तार दिए गए हैं, यह लेख ध्वज को प्रकट करने के लिए फ़र्नेट साइफ़र और मालबोगे सीफ़र को प्रक्रिया के माध्यम से विभाजित करने के लिए आपका मार्गदर्शन करता है। समाधान प्राप्त करने के लिए asecuritysite.com और base64decode.org द्वारा प्रदान किए गए टूल का उपयोग करें।  ______  ## प्रदान की गई फ़ाइलें:  इस चुनौती में आपको दो प्रकार की जानकारी प्रदान की जाती है।  और  ## के माध्यम से नीचे:  पहली नजर में ऐसा होता है कि यह किसी भी प्रकार की कुंजी और सरल पाठ है। सैकेरा के चारों ओर, आप इसे एक फर्नेट साइफर देखते हैं। [Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) के पास आपके लिए इसे डीकोड करने के लिए एक बेहतरीन उपाय है।  जानकारी से संदीप पाठ आपको आधार 64 के प्रमुख कलाकार प्रदान करता है   इसे डीकोड करने के लिए, हम [base64decode.org](https://www.base64decode.org/) से मिले टूल का उपयोग करेंगे  डिकोडिंग फिर से आपको निम्नलिखित देता है:  यह मेरे लिए एक नया था। लेकिन आप कुछ उपाय खोजने के बाद यह एक मालबोग सीफर है। इसे [इस](http://malbolge.doleczek.pl/) उपकरण से डिकोड करने से आपको टेक्स्ट मिल जाएगा।  ______  ### ध्वज पूर्व: 