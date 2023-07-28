---
title: "Automatizzare la conformità di Oracle JRE 8 STIG con uno script Powershell"
date: 2020-08-05
---


Le STIG di Oracle JRE non sono così semplici, e richiedono agli amministratori di ricercare la documentazione JAVA e di generare file di configurazione java, quando la maggior parte degli amministratori è abituata ad utilizzare esclusivamente STIG con i criteri di gruppo.

## Scaricare i file necessari

Scaricare i file necessari dal sito [GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## STIGS/SRG applicati:
- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Fonti:
- [MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

- [cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## Come eseguire lo script

**Lo script può essere prelevato dal download estratto da GitHub in questo modo:**

```
.\sos-install-java-config.ps1
```
