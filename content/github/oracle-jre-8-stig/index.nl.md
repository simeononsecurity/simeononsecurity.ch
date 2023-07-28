---
title: "Oracle JRE 8 STIG-naleving automatiseren met Powershell Script"
date: 2020-08-05
---


De Oracle JRE STIG's zijn niet zo eenvoudig, ze vereisen dat beheerders de JAVA documentatie doorzoeken en java configuratiebestanden genereren, terwijl de meeste beheerders gewend zijn om alleen STIG's te maken met behulp van groepsbeleid.

## Download de benodigde bestanden

Download de benodigde bestanden van de [GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## Toegepaste STIGS/SRG's:
- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Bronnen:
- [MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

- [cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## Het script uitvoeren

**Het script kan als volgt uit de uitgepakte GitHub-download worden gelicht:**

```
.\sos-install-java-config.ps1
```
