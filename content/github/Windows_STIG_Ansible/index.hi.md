---
title: "Ansible STIG Playbooks के साथ स्वचालित Windows अनुपालन"
date: 2022-04-26
toc: true
draft: false
description: "विंडोज सिस्टम के लिए Ansible STIG Playbooks के साथ अपने सुरक्षा अनुपालन को व्यवस्थित करें।"
tags: ["स्वचालन", "विंडोज अनुपालन", "Ansible STIG Playbooks", "विंडोज हार्डनिंग", "एसटीआईजी लिपियों", "एसटीआईजी अनुपालन", "अन्सिबल गैलेक्सी", "पावरशेल", "पॉवरशेल स्क्रिप्ट", "विंडोज सर्वर", "विंडोज़ रक्षक", "।जाल", "फ़ायरफ़ॉक्स", "ओरेकल जेआरई 8", "एडोब रीडर डीसी", "इंटरनेट कनेक्टिविटी", "ऑफ़लाइन संगतता", "सुरक्षा सख्त", "विंडोज सुरक्षा"]
---


शिमोनऑनसिक्योरिटी की एसटीआईजी लिपियों के लिए अन्सिबल प्लेबुक

## टिप्पणियाँ:

- वर्तमान में इंटरनेट कनेक्टिविटी की आवश्यकता है। (ऑफ़लाइन अनुकूलता WIP)

## उपयोग:

## स्थापना:

-[Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

```bash
ansible-galaxy collection install simeononsecurity.windows_stigs
```

## पर आधारित:

-[simeononsecurity/STIG-Compliant-Domain-Prep](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep)
-[simeononsecurity/Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[simeononsecurity/Standalone-Windows-Server-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-Server-STIG-Script)
-[simeononsecurity/Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[simeononsecurity/.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[simeononsecurity/FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[simeononsecurity/Oracle-JRE-8-STIG-Script](https://github.com/simeononsecurity/Oracle-JRE-8-STIG-Script)
-[simeononsecurity/Adobe-Reader-DC-STIG-Script](https://github.com/simeononsecurity/Adobe-Reader-DC-STIG-Script)
