---
title: "Automatizza la conformità a Oracle JRE 8 STIG con Powershell Script"
date: 2020-08-05
---


Gli Oracle JRE STIG non sono così semplici, richiedendo agli amministratori di ricercare la documentazione JAVA e generare file di configurazione Java, quando la maggior parte degli amministratori è abituata esclusivamente a STIG utilizzando i criteri di gruppo.

## Scarica i file richiesti

Scarica i file richiesti dal file[GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## STIGS/SRG applicati:
-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Fonti:
-[MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

-[cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## Come eseguire lo script

**Lo script può essere avviato dal download GitHub estratto in questo modo:**

```
.\sos-install-java-config.ps1
```
