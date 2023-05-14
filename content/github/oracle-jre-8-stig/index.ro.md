---
title: "Automatizați conformitatea Oracle JRE 8 STIG cu Powershell Script"
date: 2020-08-05
---


STIG-urile Oracle JRE nu sunt atât de simple, solicitând administratorilor să cerceteze documentația JAVA și să genereze fișiere de configurare java, când majoritatea administratorilor sunt obișnuiți să facă STIG numai folosind politica de grup.

## Descărcați fișierele necesare

Descărcați fișierele necesare din[GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## STIGS/SRG aplicate:
-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Surse:
-[MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

-[cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## Cum se rulează scriptul

**Scriptul poate fi lansat din descărcarea GitHub extrasă astfel:**

```
.\sos-install-java-config.ps1
```
