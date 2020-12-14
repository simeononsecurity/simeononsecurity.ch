---
title: 'SolarWinds Orion Supply Chain Compromised, C2, and Mitigations'
date: 2020-12-14
toc: true
draft: false
tags: ['Command and Controll', 'SolarWinds', 'SolarWinds C2', 'SolarWinds Orion', 'SolarWinds Supply Chain', 'Supply Chain', 'C2', 'Command and Control', 'Mitigations', 'Guidance', 'Threat Intelligence']
---

For guidance on the solarwinds issue please see [DHS](https://cyber.dhs.gov/ed/21-01/), [SolarWinds](https://www.solarwinds.com/securityadvisory), [FireEYE](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html), [MSRC](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/), and [Microsoft](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Trojan:MSIL/Solorigate.B!dha). 

Advanced users, please see the [FireEYE repo](https://github.com/fireeye/sunburst_countermeasures) on this issue.

SANS has a good video on the topic [here](https://www.youtube.com/watch?v=4tmlZCk2gCg&feature=youtu.be).

## Executables:
The DLL in question is ```SolarWinds.Orion.Core.BusinessLayer.dll``` and was signed as a ligitimate part of the SolarWinds suite, bypassing application control technologies. It is installed as a service.

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
  
## Microsoft Malicious DLL Table:
| SHA256                                                           | File Version      | Date first seen |
|------------------------------------------------------------------|-------------------|-----------------|
| 32519b85c0b422e4656de6e6c41878e95fd95026267daab4215ee59c107d6c77 | 2019.4.5200.9083  | March 2020      |
| dab758bf98d9b36fa057a66cd0284737abf89857b73ca89280267ee7caf62f3b | 2020.2.100.12219  | March 2020      |
| eb6fab5a2964c5817fb239a7a5079cabca0a00464fb3e07155f28b0a57a2c0ed | 2020.2.100.11831  | March 2020      |
| c09040d35630d75dfef0f804f320f8b3d16a481071076918e9b236a321c1ea77 | Not available     | March 2020      |
| ac1b2b89e60707a20e9eb1ca480bc3410ead40643b386d624c5d21b47c02917c | 2020.4.100.478    | April 2020      |
| 019085a76ba7126fff22770d71bd901c325fc68ac55aa743327984e89f4b0134 | 2020.2.5200.12394 | April 2020      |
| ce77d116a074dab7a22a0fd4f2c1ab475f16eec42e1ded3c0b0aa8211fe858d6 | 2020.2.5300.12432 | May 2020        |
| a25cadd48d70f6ea0c4a241d99c5241269e6faccb4054e62d16784640f8e53bc | 2019.4.5200.8890  | October 2019    |
| d3c6785e18fba3749fb785bc313cf8346182f532c59172b69adfb31b96a5d0af | 2019.4.5200.8890  | October 2019    |

## FireEYE Indicator Table:
| SHA256  | SHA1                                                              | MD5                                       | FILENAME                          | MIME                                                             | Malware Family                  | Role                      |                                                    |
|---------|-------------------------------------------------------------------|-------------------------------------------|-----------------------------------|------------------------------------------------------------------|---------------------------------|---------------------------|----------------------------------------------------|
| d0d626deb3f9484e649294a8dfa814c5568f846d5aa02d4cdad5d041a29d5600  | 1b476f58ca366b54f34d714ffce3fd73cc30db1a  | 02af7cec58b9a5da1c542b5a32151ba1  | CORE-2019.4.5220.20574-SolarWinds-Core-v2019.4.5220-Hotfix5.msp  | application/vnd.ms-office       | SUNBURST                  | Installer                                          |
| 53f8dfc65169ccda021b72a62e0c22a4db7c4077f002fa742717d41b3c40f2c7  | 47d92d49e6f7f296260da1af355f941eb25360c4  | 08e35543d6110ed11fdf558bb093d401  | Solarwinds Worldwide, LLC                                        | application/x-x509-server-cert  | Code Signing Certificate  | Legitimate SolarWinds code-signing certificate     |
| 019085a76ba7126fff22770d71bd901c325fc68ac55aa743327984e89f4b0134  | 2f1a5a7411d015d01aaee4535835400191645023  | 2c4a910a1299cdae2a4e55988a2f102e  | SolarWinds.Orion.Core.BusinessLayer.dll                          | application/x-dosexec           | SUNBURST                  | backdoor                                           |
| ce77d116a074dab7a22a0fd4f2c1ab475f16eec42e1ded3c0b0aa8211fe858d6  | d130bd75645c2433f88ac03e73395fba172ef676  | 846e27a652a5e1bfbd0ddd38a16dc865  | SolarWinds.Orion.Core.BusinessLayer.dll                          | application/x-dosexec           | SUNBURST                  | backdoor                                           |
| 32519b85c0b422e4656de6e6c41878e95fd95026267daab4215ee59c107d6c77  | 76640508b1e7759e548771a5359eaed353bf1eec  | b91ce2fa41029f6955bff20079468448  | SolarWinds.Orion.Core.BusinessLayer.dll                          | application/x-dosexec           | SUNBURST                  | backdoor                                           |
| 292327e5c94afa352cc5a02ca273df543f2020d0e76368ff96c84f4e90778712  | c2c30b3a287d82f88753c85cfb11ec9eb1466bad  | 4f2eb62fa529c0283b28d05ddd311fae  | OrionImprovementBusinessLayer.2.cs                               | text/plain                      | SUNBURST                  | Decompiled and corrected source code for SUNBURST  |
| c15abaf51e78ca56c0376522d699c978217bf041a3bd3c71d09193efa5717c71  |                                           |                                   |                                                                  |                                 |                           |                                                    |
