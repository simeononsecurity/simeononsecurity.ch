---
title: "Oracle JRE 8 STIG-naleving automatiseren met Powershell-script"
date: 2020-08-05
---


De Oracle JRE STIG's zijn niet zo eenvoudig, en vereisen dat beheerders de JAVA-documentatie onderzoeken en java-configuratiebestanden genereren, terwijl de meeste beheerders gewend zijn alleen STIG's te maken met behulp van groepsbeleid.

## Download de benodigde bestanden

Download de vereiste bestanden van de[GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## STIGS/SRG's toegepast:
-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Bronnen:
-[MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

-[cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## Hoe voer je het script uit

**Het script kan worden gelanceerd vanaf de uitgepakte GitHub download als volgt:**

```
.\sos-install-java-config.ps1
```
