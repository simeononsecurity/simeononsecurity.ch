---
title: "Automated Branding for Windows Systems - Easily Control Desktop, Lock Screen, and More"
date: 2020-08-14T14:37:16-05:00
toc: true
draft: false
description: "Control desktop wallpaper, users avatar, lock screen, and OEM logo with ease on Windows 10 and Server systems using a partially automated script."
tags: ["Automation", "Branding", "Windows Branding", "Customization", "Windows Customization", "Windows 10", "Windows Server 2016", "Windows Server 2019", "Powershell", "Script", "Windows System Branding", "Desktop Wallpaper", "Users Avatar", "Windows Lock Screen", "OEM Logo", "Microsoft Security Compliance Toolkit 1.0", "Organization Branding", "System Customization", "IT Automation", "Security Compliance"]
---
```
.\sos-copybranding.ps1
```

  कई प्रयोग विंडोज सिस्टम की ब्रांडिंग को नियंत्रित करने की आवश्यकता होती है या वे इसे नियंत्रित करना चाहते हैं। इसमें डेस्कटॉप वॉलपेपर, उपयोगकर्ता अवतार, विंडोज लॉक स्क्रीन और कभी-कभी ओम लोगो शामिल हैं। विंडोज 10, विंडोज सर्वर 2016 और विंडोज सर्वर 2019 में यह विशेष रूप से आसान नहीं है। लेकिन, लिंक्ड स्क्रिप्ट की सहायता से, हम इसे आंशिक रूप से चालू कर सकते हैं और प्रक्रिया को बहुत आसान बना सकते हैं।  ## आवश्यक फाइल डाउनलोड करें  ** [GitHub रिपॉजिटरी](https://github.com/simeononsecurity/Windows-Branding-Script) से आवश्यक फ़ाइलें डाउनलोड करें**  ## ब्रांडिंग फाइल कैसे सेट करें  - [X] सभी प्रभावितों को अपनी ब्रांडिंग से बदलाव   - [X] OEM लोगो या तो 95x95 या 120x20 और ".bmp" प्रारूप में होना चाहिए   - [X] 32x32, 40x40, 48x48, 192x192 उपयोगकर्ता के साथ इमेजेस करें।   - [एक्स] अतिथि छवि के लिए उपयोगकर्ता छवि या प्रतिलिपि बनाएँ।  ## स्क्रिप्ट कैसे चलाएं  ## यह निम्नलिखित स्क्रिप्ट टूल का उपयोग करता है:  - [Microsoft सुरक्षा पूर्ति टूलकिट 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)