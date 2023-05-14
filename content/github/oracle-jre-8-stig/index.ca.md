---
title: "Automatitzeu el compliment d'Oracle JRE 8 STIG amb Powershell Script"
date: 2020-08-05
---


Els STIG JRE d'Oracle no són tan senzills, ja que requereixen que els administradors investiguin documentació JAVA i generin fitxers de configuració java, quan la majoria dels administradors s'acostumen a fer STIG només mitjançant la política de grup.

## Baixeu els fitxers necessaris

Baixeu els fitxers necessaris des del[GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## STIGS/SRG aplicats:
-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Fonts:
-[MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

-[cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## Com executar l'script

**L'script es pot llançar des de la descàrrega de GitHub extreta així:**

```
.\sos-install-java-config.ps1
```
