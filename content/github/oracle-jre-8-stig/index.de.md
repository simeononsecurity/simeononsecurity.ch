---
title: "Automatisieren der Oracle JRE 8 STIG-Konformität mit Powershell-Skript"
date: 2020-08-05
---


Die Oracle JRE STIGs sind nicht so einfach, da sie von den Administratoren verlangen, die JAVA-Dokumentation zu durchsuchen und Java-Konfigurationsdateien zu erstellen, während die meisten Administratoren daran gewöhnt sind, STIGs ausschließlich über Gruppenrichtlinien zu erstellen.

## Download der erforderlichen Dateien

Laden Sie die erforderlichen Dateien von der Seite [GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## Angewandte STIGS/SRGs:
- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Quellen:
- [MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

- [cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## So führen Sie das Skript aus

**Das Skript kann aus dem extrahierten GitHub-Download wie folgt gestartet werden:**

```
.\sos-install-java-config.ps1
```
