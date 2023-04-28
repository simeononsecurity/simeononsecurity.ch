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

قم بحل تحدي HTB Weak RSA Crypto بكل سهولة. بناء على تشفير RSA ، يصبح الهدف السهل استخدام أداة هجوم RSA ، آلية مثل RsaCtfTool. احصل على العلم بأمر بسيط وقم بتوسيع مهاراتك في التشفير مع تحديات HackTheBox.  ______  ## الملفات المقدمة:  ** تم تزويدك بالملفات التالية: ** - علم. أر - مفتاح  ## جولة تفصيلية:  للوهلة الأولى ، تعتقد أنه يمكنك فك تشفير العلم باستخدام المفتاح العام. ، قد يكون عبارة عن حزمة OpenSSL لفك تشفير العلم. هذه المرة ، المرة القادمة ستعمل في المرة القادمة.  أداة هجوم آلية RSA. أحد نصوص Python الشائعة هو [RsaCtfTool] (https://github.com/Ganapati/RsaCtfTool)     ببساطة ، تجد نفسك في فلسطين العلم بطريقة آلية.  ______  ### مثال العلم: