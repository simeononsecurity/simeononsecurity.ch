---
title: "HackTheBox - चुनौतियाँ - क्रिप्टो - डिकोड"
date: 2020-10-07
draft: false
description: "HackTheBox क्रिप्टो चुनौती को हल करने और छिपे हुए झंडे को उजागर करने के लिए फ़र्नेट और मालबोगे सिफर को डिकोड करना सीखें।"
tags: ["हैक द बॉक्स","चुनौतियां","क्रिप्टो","डिकोड","सार्वजनिक रूप से लिखना","फर्नेट सिफर","मालबोगे सिफर","सममित एन्क्रिप्शन","साइबर सुरक्षा","क्रिप्टोग्राफी","भेदन परीक्षण","पायथन","सुरक्षा","चुनौती","सीटीएफ","झंडा","कूटलेखन","डिक्रिप्शन","बेस 64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "एक कार्टून हैकर एक बड़े ताले के बगल में खड़ा है जिसके एक हाथ में फर्नेट लोगो की चाबी है और दूसरे हाथ में मालबोग लोगो की चाबी है जबकि ताले के अंदर एक झंडा दिख रहा है"
coverCaption: ""
---

HackTheBox क्रिप्टो डिकोड चुनौती के बारे में विस्तृत जानकारी प्राप्त करें। जानकारी के दो तार दिए गए हैं, यह लेख ध्वज को प्रकट करने के लिए फ़र्नेट साइफर और मालबोगे सिफर को डिकोड करने की प्रक्रिया के माध्यम से आपका मार्गदर्शन करता है। समाधान प्राप्त करने के लिए asecuritysite.com और base64decode.org द्वारा प्रदान किए गए टूल का उपयोग करें।

______

## प्रदान की गई फ़ाइलें:

इस चुनौती में आपको दो प्रकार की जानकारी प्रदान की जाती है।

```
993gmULBNujjrZCDev3W8kAVaLkXiyHhCL3500188bA=
```
and
```
gAAAAABboRUb0FsuiYBk1tsXRDr6KAzU1xrNSUv7grB-G-dAEeyqj99kUebz466I2VcH5xDa5HEc5KkbgTklQ7tm9JCRPlJtRng1Ns3VEvbrk7B835OINfPnRbc-UIOnnCmW3CgMdMtf5wGLN299AZEzxIvuy71WC5d9xJDchyiORycuzCth95-4nTKphlNQQ2ko3DX72RxWeEjwt3mavnFXqcOCkGxUhJYmFltz_6ND56VGTrXZi_CK5xLODOX4sj1GNwN_CrU3sJ0obTdA2wF5OaDZLbA1GBPfK0PDlC9WxoUf85K0tFXKfqbt3c5YqtqfytNG5gTkbDFM2NjE7BveBf1DP9ca8g==
```

## Walk Through:

At first glance it appears this is some sort of key and some cipher text.
After searching around, you'll find that it is a Fernet cypher.
[Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) has a great tool to decode it for you.

The plain text from the above information gives you a base64 encoded string

```
RCdgTl45OFs8O3tGMlZVNTRRPythcUw6bVxJNmlYJmYkMEBSeFBfdSldeHFwdW5tM3Fwb2htZmUrTGJnZl9eXSNhYFleV1Z6VFNyUVZVTnJMUVBPTkdrS0QsSEFlKERDPDtfPz5+fTVZOTg3dzUuUjJyMC8oJyZKKikoJyYlfHtBeX53djx6eXhxWTZ0c1VUcG9oLnk=
```

To decode this, we'll use the tool provided from [base64decode.org](https://www.base64decode.org/)

Decoding again gives you the following:
```
D'`N^98[<;{F2VU54Q?+aqL:m\I6iX&f$0@RxP_u)]xqpunm3qpohmfe+Lbgf_^]#a`Y^WVzTSXQVUNrLQPONGkKD,HAe(DC<;_?>
```

This was a new one for me. But you'll find after some careful research that it is a Malboge cipher.
Decoding it with [this](http://malbolge.doleczek.pl/) tool will give you the flag.

______

### Flag Ex:
```
HTB{x_xxx_xxxx}
```

