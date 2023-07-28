---
title: "Automatizați conformitatea Oracle JRE 8 STIG cu un script Powershell"
date: 2020-08-05
---


STIG-urile Oracle JRE nu sunt atât de simple, necesitând ca administratorii să cerceteze documentația JAVA și să genereze fișiere de configurare Java, în condițiile în care majoritatea administratorilor sunt obișnuiți să utilizeze doar STIG-uri prin intermediul politicii de grup.

## Descărcați fișierele necesare

Descărcați fișierele necesare de pe site-ul [GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## STIGS/SRGs aplicate:
- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Surse:
- [MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

- [cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## Cum se execută scriptul

**Scriptul poate fi lansat din descărcarea extrasă de pe GitHub astfel:**

```
.\sos-install-java-config.ps1
```
