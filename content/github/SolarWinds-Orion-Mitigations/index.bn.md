---
title: "সোলারউইন্ডস ওরিয়ন সাপ্লাই চেইন অ্যাটাক: C2, মিটিগেশন এবং এক্সপার্ট গাইডেন্স"
date: 2020-12-14
toc: true
draft: false
description: "SolarWinds Orion Supply Chain Attack সম্পর্কে জানুন, যার মধ্যে C2 ম্যালওয়্যার, প্রশমন, এবং DHS এবং FireEye-এর মতো প্রতিষ্ঠানের বিশেষজ্ঞ নির্দেশিকা রয়েছে।"
tags: ["সোলার উইন্ডস", "সাপ্লাই চেইন", "C2", "কমান্ড এবং নিয়ন্ত্রণ", "প্রশমন", "নির্দেশনা", "থ্রেট ইন্টেলিজেন্স", "ডিএইচএস", "ফায়ারআই", "এমএসআরসি", "মাইক্রোসফট", "SANS", "SolarWinds.Orion.Core.BusinessLayer.dll", "SolarWinds.BusinessLayerHost.exe", "ConfigurationWizard.exe", "NetflowDatabaseMaintenance.exe", "NetFlowService.exe", "SolarWinds.Administration.exe", "SolarWinds.Collector.Service.exe", "DNS CNAMEs", "আইপি রেঞ্জ", "DNS নাম"]
---

সোলারওয়াইন্ডস ইস্যুতে নির্দেশনার জন্য দয়া করে দেখুন[DHS](https://cyber.dhs.gov/ed/21-01/), [SolarWinds](https://www.solarwinds.com/securityadvisory), [FireEYE](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html), [MSRC](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/), and [Microsoft](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Trojan:MSIL/Solorigate.B!dha) 

উন্নত ব্যবহারকারী, দেখুন[FireEYE Countermeasures Repo](https://github.com/fireeye/sunburst_countermeasures) এই বিষয়ে.

SANS এই বিষয়ে একটি ভাল ভিডিও আছে[here](https://www.youtube.com/watch?v=4tmlZCk2gCg&feature=youtu.be)

## এক্সিকিউটেবল:
প্রশ্নে DLL হল```SolarWinds.Orion.Core.BusinessLayer.dll``` and was signed as a ligitimate part of the SolarWinds suite, bypassing application control technologies. It is installed as a service.

The malicious code was injected into a legitimate DLL and is loaded into memory when the application runs. The code runs before the legitimate code. According to Microsoft, the code is activated when ```SolarWinds.BusinessLayerHost.exe``` executable runs, but may the following may also load it:
- ```ConfigurationWizard.exe```
- ```NetflowDatabaseMaintenance.exe```
- ```NetFlowService.exe```
- ```SolarWinds.Administration.exe```
- ```SolarWinds.BusinessLayerHost.exe```
- ```SolarWinds.Collector.Service.exe```
- ```SolarwindsDiagnostics.exe```

## Network information:

**General Ranges:**
- DNS CNAMEs for C2:
  - ```.appsync-api.eu-west-1[.]avsvmcloud[.]com```
  - ```.appsync-api.us-west-2[.]avsvmcloud[.]com```
  - ```.appsync-api.us-east-1[.]avsvmcloud[.]com```
  - ```.appsync-api.us-east-2[.]avsvmcloud[.]com```
- IP Ranges for C2:
  - ```20.140.0.0/15```
  - ```96.31.172.0/24```
  - ```131.228.12.0/22```
  - ```144.86.226.0/24```

**Specifically Identified:**
- DNS Names associated with C2:
  - ```6a57jk2ba1d9keg15cbg.appsync-api.eu-west-1.avsvmcloud[.]com```
  - ```7sbvaemscs0mc925tb99.appsync-api.us-west-2.avsvmcloud[.]com```
  - ```gq1h856599gqh538acqn.appsync-api.us-west-2.avsvmcloud[.]com```
  - ```ihvpgv9psvq02ffo77et.appsync-api.us-east-2.avsvmcloud[.]com``` 
  - ```k5kcubuassl3alrf7gm3.appsync-api.eu-west-1.avsvmcloud[.]com``` 
  - ```mhdosoksaccf9sni9icp.appsync-api.eu-west-1.avsvmcloud[.]com```
- IPs assosciated with C2:
  - ```13.59.205.66```
  - ```54.193.127.66```
  - ```54.215.192.52```
  - ```34.203.203.23``` 
  - ```139.99.115.204``` 
  - ```5.252.177.25```
  - ```5.252.177.21```
  - ```204.188.205.176```	
  - ```51.89.125.18```
  - ```167.114.213.199```
  
## [DLL Locations](https://gist.github.com/KyleHanslovan/0c8a491104cc55d6e4bd9bff7214a99e):
- ```C:\Program Files (x86)\N-able Technologies\Windows Software Probe\bin\SolarWinds.Orion.Core.BusinessLayer.dll```
- ```C:\Program Files (x86)\Solarwinds\Network Topology Mapper\SolarWinds.Orion.Core.BusinessLayer.dll```
- ```C:\Program Files (x86)\Solarwinds\Network Topology Mapper\Service\SolarWinds.Orion.Core.BusinessLayer.dll```
- ```C:\Program Files (x86)\SolarWinds\Orion\SolarWinds.Orion.Core.BusinessLayer.dll```
- ```C:\Program Files (x86)\SolarWinds\Orion\DPI\SolarWinds.Orion.Core.BusinessLayer.dll```
- ```C:\Program Files (x86)\SolarWinds\Orion\NCM\SolarWinds.Orion.Core.BusinessLayer.dll```
- ```C:\Program Files (x86)\SolarWinds\Orion\Interfaces.Discovery\SolarWinds.Orion.Core.BusinessLayer.dll```
- ```C:\Program Files (x86)\SolarWinds\Orion\DPA\SolarWinds.Orion.Core.BusinessLayer.dll```
- ```C:\Program Files (x86)\SolarWinds\Orion\HardwareHealth\SolarWinds.Orion.Core.BusinessLayer.dll```
- ```C:\Program Files (x86)\SolarWinds\Orion\Interfaces\SolarWinds.Orion.Core.BusinessLayer.dl```
- ```C:\Program Files (x86)\SolarWinds\Orion\NetFlowTrafficAnalysis\SolarWinds.Orion.Core.BusinessLayer.dll```
- ```C:\Program Files (x86)\SolarWinds\Orion\NPM\SolarWinds.Orion.Core.BusinessLayer.dll```
  
##[Microsoft Malicious DLL Table:](https://github.com/simeononsecurity/SolarWinds-SunBurst-Countermeasures)
-[See the GitHub Repository for more info](https://github.com/simeononsecurity/SolarWinds-SunBurst-Countermeasures)

##[FireEYE Indicator Table:](https://github.com/simeononsecurity/SolarWinds-SunBurst-Countermeasures)
-[See the GitHub Repository for more info](https://github.com/simeononsecurity/SolarWinds-SunBurst-Countermeasures)

##[Sites Known to Be Hit By SunBurst/SolarFlare:](https://github.com/simeononsecurity/SolarWinds-SunBurst-Countermeasures)
- https://github.com/RedDrip7/SunBurst_DGA_Decode
- https://pastebin.com/raw/6NukuxBN
