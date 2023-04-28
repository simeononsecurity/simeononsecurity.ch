---
title: "Windows 10 System-Wide Ad Blocker Script for Better Privacy and Security"
date: 2021-04-02
toc: true
draft: false
description: "Block ads, trackers, and telemetry on Windows 10 using this powerful PowerShell script that utilizes the hosts file and Windows Firewall for system-wide ad-blocking."
tags: ["Windows 10", "ad-blocker", "telemetry blocking", "PowerShell script", "system-wide ad-blocking", "privacy", "security", "EasyList", "Easy Privacy", "NoCoin Filter List", "AdGuard DNS filter", "YoYo Lists", "Peter Lowe's ad/tracking/malware servers", "Windows Firewall", "domain lists", "block Windows trackers", "block trackers", "block ads", "block tracking"]
---
```powershell
iwr -useb 'https://raw.githubusercontent.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/main/sos-system-wide-windows-ad-block.ps1' | iex
```

 ## विवरण: यह स्क्रिप्ट विंडोज फ़ायरवॉल के माध्यम से होस्ट फ़ाइल और संबंधित आईपी के माध्यम से टेलीमेट्री संबंधित डोमेन को ब्लॉक करता है।  **टिप्पणियाँ:** - इन डोमेन को जोड़कर iTunes या Skype जैसे कुछ ख़राब हो सकते हैं -कामाई से संबंधित धोखाधड़ी को व्यापक डीआरएम के साथ पूर्व का कारण बताया गया है  ### अनुमत सूत्रियां: - [EasyList](https://easylist.to/easylist/easylist.txt) / [JustDomains - EasyList](https://justdomains.github.io/blocklists/lists/easylist-justdomains.txt) - [आसान गोपनीयता](https://easylist.to/easylist/easyprivacy.txt) / [JustDomains - EasyPrivacy](https://justdomains.github.io/blocklists/lists/easyprivacy-justdomains.txt) - [नोकॉइन जमा सूची](https://github.com/hoshsadiq/adblock-nocoin-list/) / [JustDomains - NoCoin सागर सूची](https://justdomains.github.io/blocklists/lists/nocoin-justdomains ।TXT) - [AdGuard DNS ग्रहण](https://github.com/AdguardTeam/AdguardSDNSFilter) / [JustDomains - AdGuard बन्धन डोमेन नाम](https://justdomains.github.io/blocklists/lists/adguarddns-justdomains.txt) - [योयो सूचियां](https://pgl.yoyo.org/adservers/serverlist.php) - [पीटर लोव का विज्ञापन/ट्रैकिंग/मैलवेयर सर्वर](https://pgl.yoyo.org/adservers/policy.php)  ### उदाहरण:  स्क्रिप्ट का नवीनतम संस्करण स्वचालित रूप से चला गया: