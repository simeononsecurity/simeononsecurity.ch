---
title: "Automatiser la conformité d'Oracle JRE 8 STIG avec un script Powershell"
date: 2020-08-05
---


Les STIG d'Oracle JRE ne sont pas aussi simples, car ils exigent des administrateurs qu'ils recherchent la documentation JAVA et génèrent des fichiers de configuration Java, alors que la plupart des administrateurs sont habitués à utiliser uniquement les STIG à l'aide de la stratégie de groupe.

## Télécharger les fichiers nécessaires

Téléchargez les fichiers nécessaires à partir du site [GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## STIGS/SRGs appliqués :
- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Sources :
- [MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

- [cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## Comment exécuter le script

**Le script peut être lancé à partir du téléchargement GitHub extrait comme ceci:**

```
.\sos-install-java-config.ps1
```
