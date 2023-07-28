---
title: "SolarWinds Orion Supply Chain Attack : C2, atténuations et conseils d'experts"
date: 2020-12-14
toc: true
draft: false
description: "Découvrez l'attaque de la chaîne d'approvisionnement SolarWinds Orion, y compris le logiciel malveillant C2, les mesures d'atténuation et les conseils d'experts d'organisations telles que le DHS et FireEye."
tags: ["SolarWinds", "Chaîne d'approvisionnement", "C2", "Commandement et contrôle", "Atténuations", "Orientations", "Renseignements sur les menaces", "DHS", "FireEye", "CSEM", "Microsoft", "SANS", "SolarWinds.Orion.Core.BusinessLayer.dll", "SolarWinds.BusinessLayerHost.exe", "ConfigurationWizard.exe", "NetflowDatabaseMaintenance.exe", "NetFlowService.exe", "SolarWinds.Administration.exe", "SolarWinds.Collector.Service.exe", "DNS CNAMEs", "Gammes IP", "Noms DNS"]
---

Pour obtenir des conseils sur le problème de solarwinds, veuillez consulter le site suivant [DHS](https://cyber.dhs.gov/ed/21-01/), [SolarWinds](https://www.solarwinds.com/securityadvisory), [FireEYE](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html), [MSRC](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/), and [Microsoft](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Trojan:MSIL/Solorigate.B!dha) 

Pour les utilisateurs avancés, veuillez consulter la page [FireEYE Countermeasures Repo](https://github.com/fireeye/sunburst_countermeasures) sur cette question.

Le SANS propose une bonne vidéo sur le sujet [here](https://www.youtube.com/watch?v=4tmlZCk2gCg&feature=youtu.be)

## Exécutables :
La DLL en question est ```SolarWinds.Orion.Core.BusinessLayer.dll``` et a été signé comme une partie légitime de la suite SolarWinds, en contournant les technologies de contrôle des applications. Il est installé en tant que service.

Le code malveillant a été injecté dans une DLL légitime et est chargé en mémoire lors de l'exécution de l'application. Le code s'exécute avant le code légitime. Selon Microsoft, le code est activé lorsque ```SolarWinds.BusinessLayerHost.exe``` L'exécutable s'exécute, mais les éléments suivants peuvent également le charger :
- ```ConfigurationWizard.exe```
- ```NetflowDatabaseMaintenance.exe```
- ```NetFlowService.exe```
- ```SolarWinds.Administration.exe```
- ```SolarWinds.BusinessLayerHost.exe```
- ```SolarWinds.Collector.Service.exe```
- ```SolarwindsDiagnostics.exe```

## Informations sur le réseau :

**Gamme générale:**
- DNS CNAMEs pour C2 :
  - ```.appsync-api.eu-west-1[.]avsvmcloud[.]com```
  - ```.appsync-api.us-west-2[.]avsvmcloud[.]com```
  - ```.appsync-api.us-east-1[.]avsvmcloud[.]com```
  - ```.appsync-api.us-east-2[.]avsvmcloud[.]com```
- Plages IP pour C2 :
  - ```20.140.0.0/15```
  - ```96.31.172.0/24```
  - ```131.228.12.0/22```
  - ```144.86.226.0/24```

**Spécifiquement identifié:**
- Noms DNS associés à C2 :
  - ```6a57jk2ba1d9keg15cbg.appsync-api.eu-west-1.avsvmcloud[.]com```
  - ```7sbvaemscs0mc925tb99.appsync-api.us-west-2.avsvmcloud[.]com```
  - ```gq1h856599gqh538acqn.appsync-api.us-west-2.avsvmcloud[.]com```
  - ```ihvpgv9psvq02ffo77et.appsync-api.us-east-2.avsvmcloud[.]com``` 
  - ```k5kcubuassl3alrf7gm3.appsync-api.eu-west-1.avsvmcloud[.]com``` 
  - ```mhdosoksaccf9sni9icp.appsync-api.eu-west-1.avsvmcloud[.]com```
- IPs associés à C2 :
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
  
## [DLL Locations](https://gist.github.com/KyleHanslovan/0c8a491104cc55d6e4bd9bff7214a99e)
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
  
## [Microsoft Malicious DLL Table:](https://github.com/simeononsecurity/SolarWinds-SunBurst-Countermeasures)
- [See the GitHub Repository for more info](https://github.com/simeononsecurity/SolarWinds-SunBurst-Countermeasures)

## [FireEYE Indicator Table:](https://github.com/simeononsecurity/SolarWinds-SunBurst-Countermeasures)
- [See the GitHub Repository for more info](https://github.com/simeononsecurity/SolarWinds-SunBurst-Countermeasures)

## [Sites Known to Be Hit By SunBurst/SolarFlare:](https://github.com/simeononsecurity/SolarWinds-SunBurst-Countermeasures)
- https://github.com/RedDrip7/SunBurst_DGA_Decode
- https://pastebin.com/raw/6NukuxBN
