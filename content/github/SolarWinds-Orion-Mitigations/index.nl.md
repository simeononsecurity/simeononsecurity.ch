---
title: "SolarWinds Orion Supply Chain Attack: C2, mitigaties en deskundige begeleiding"
date: 2020-12-14
toc: true
draft: false
description: "Leer meer over de SolarWinds Orion Supply Chain Attack, inclusief de C2-malware, mitigaties en deskundige begeleiding van organisaties als DHS en FireEye."
tags: ["SolarWinds", "Toeleveringsketen", "C2", "Commando en controle", "Mitigaties", "Begeleiding", "Informatie over bedreigingen", "DHS", "FireEye", "MSRC", "Microsoft", "ZONDER", "SolarWinds.Orion.Core.BusinessLayer.dll", "SolarWinds.BusinessLayerHost.exe", "ConfigurationWizard.exe", "NetflowDatabaseMaintenance.exe", "NetFlowService.exe", "SolarWinds.Administration.exe", "SolarWinds.Collector.Service.exe", "DNS CNAME's", "IP-bereiken", "DNS-namen"]
---

Voor advies over de solarwinds-kwestie zie[DHS](https://cyber.dhs.gov/ed/21-01/), [SolarWinds](https://www.solarwinds.com/securityadvisory), [FireEYE](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html), [MSRC](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/), and [Microsoft](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Trojan:MSIL/Solorigate.B!dha) 

Gevorderde gebruikers, zie de[FireEYE Countermeasures Repo](https://github.com/fireeye/sunburst_countermeasures) over deze kwestie.

SANS heeft een goede video over dit onderwerp[here](https://www.youtube.com/watch?v=4tmlZCk2gCg&feature=youtu.be)

## Executables:
De DLL in kwestie is```SolarWinds.Orion.Core.BusinessLayer.dll``` en is ondertekend als een ligitiem onderdeel van de SolarWinds suite, waarbij de technologieën voor toepassingscontrole worden omzeild. Het is geïnstalleerd als een service.

De kwaadaardige code is geïnjecteerd in een legitieme DLL en wordt in het geheugen geladen wanneer de toepassing wordt uitgevoerd. De code draait vóór de legitieme code. Volgens Microsoft wordt de code geactiveerd wanneer```SolarWinds.BusinessLayerHost.exe``` executable draait, maar het volgende kan ook geladen worden:
-```ConfigurationWizard.exe```
-```NetflowDatabaseMaintenance.exe```
-```NetFlowService.exe```
-```SolarWinds.Administration.exe```
-```SolarWinds.BusinessLayerHost.exe```
-```SolarWinds.Collector.Service.exe```
-```SolarwindsDiagnostics.exe```

## Netwerk informatie:

**Algemeen bereik:**
- DNS CNAMEs voor C2:
  -```.appsync-api.eu-west-1[.]avsvmcloud[.]com```
  -```.appsync-api.us-west-2[.]avsvmcloud[.]com```
  -```.appsync-api.us-east-1[.]avsvmcloud[.]com```
  -```.appsync-api.us-east-2[.]avsvmcloud[.]com```
- IP bereiken voor C2:
  -```20.140.0.0/15```
  -```96.31.172.0/24```
  -```131.228.12.0/22```
  -```144.86.226.0/24```

**Specifiek geïdentificeerd:**
- DNS Namen geassocieerd met C2:
  -```6a57jk2ba1d9keg15cbg.appsync-api.eu-west-1.avsvmcloud[.]com```
  -```7sbvaemscs0mc925tb99.appsync-api.us-west-2.avsvmcloud[.]com```
  -```gq1h856599gqh538acqn.appsync-api.us-west-2.avsvmcloud[.]com```
  -```ihvpgv9psvq02ffo77et.appsync-api.us-east-2.avsvmcloud[.]com``` 
  -```k5kcubuassl3alrf7gm3.appsync-api.eu-west-1.avsvmcloud[.]com``` 
  -```mhdosoksaccf9sni9icp.appsync-api.eu-west-1.avsvmcloud[.]com```
- IP's geassocieerd met C2:
  -```13.59.205.66```
  -```54.193.127.66```
  -```54.215.192.52```
  -```34.203.203.23``` 
  -```139.99.115.204``` 
  -```5.252.177.25```
  -```5.252.177.21```
  -```204.188.205.176```	
  -```51.89.125.18```
  -```167.114.213.199```
  
##[DLL Locations](https://gist.github.com/KyleHanslovan/0c8a491104cc55d6e4bd9bff7214a99e)
-```C:\Program Files (x86)\N-able Technologies\Windows Software Probe\bin\SolarWinds.Orion.Core.BusinessLayer.dll```
-```C:\Program Files (x86)\Solarwinds\Network Topology Mapper\SolarWinds.Orion.Core.BusinessLayer.dll```
-```C:\Program Files (x86)\Solarwinds\Network Topology Mapper\Service\SolarWinds.Orion.Core.BusinessLayer.dll```
-```C:\Program Files (x86)\SolarWinds\Orion\SolarWinds.Orion.Core.BusinessLayer.dll```
-```C:\Program Files (x86)\SolarWinds\Orion\DPI\SolarWinds.Orion.Core.BusinessLayer.dll```
-```C:\Program Files (x86)\SolarWinds\Orion\NCM\SolarWinds.Orion.Core.BusinessLayer.dll```
-```C:\Program Files (x86)\SolarWinds\Orion\Interfaces.Discovery\SolarWinds.Orion.Core.BusinessLayer.dll```
-```C:\Program Files (x86)\SolarWinds\Orion\DPA\SolarWinds.Orion.Core.BusinessLayer.dll```
-```C:\Program Files (x86)\SolarWinds\Orion\HardwareHealth\SolarWinds.Orion.Core.BusinessLayer.dll```
-```C:\Program Files (x86)\SolarWinds\Orion\Interfaces\SolarWinds.Orion.Core.BusinessLayer.dl```
-```C:\Program Files (x86)\SolarWinds\Orion\NetFlowTrafficAnalysis\SolarWinds.Orion.Core.BusinessLayer.dll```
-```C:\Program Files (x86)\SolarWinds\Orion\NPM\SolarWinds.Orion.Core.BusinessLayer.dll```
  
##[Microsoft Malicious DLL Table:](https://github.com/simeononsecurity/SolarWinds-SunBurst-Countermeasures)
-[See the GitHub Repository for more info](https://github.com/simeononsecurity/SolarWinds-SunBurst-Countermeasures)

##[FireEYE Indicator Table:](https://github.com/simeononsecurity/SolarWinds-SunBurst-Countermeasures)
-[See the GitHub Repository for more info](https://github.com/simeononsecurity/SolarWinds-SunBurst-Countermeasures)

##[Sites Known to Be Hit By SunBurst/SolarFlare:](https://github.com/simeononsecurity/SolarWinds-SunBurst-Countermeasures)
- https://github.com/RedDrip7/SunBurst_DGA_Decode
- https://pastebin.com/raw/6NukuxBN
