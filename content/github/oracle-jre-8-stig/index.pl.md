---
title: "Automatyzacja zgodności z Oracle JRE 8 STIG za pomocą skryptu Powershell"
date: 2020-08-05
---


Oracle JRE STIGs nie są tak proste, wymagają od administratorów badania dokumentacji JAVA i generowania plików konfiguracyjnych java, podczas gdy większość administratorów jest przyzwyczajona do wyłącznego STIG-owania za pomocą polityki grupy.

## Pobierz wymagane pliki

Pobierz wymagane pliki z witryny[GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## STIGS/SRGs Applied:
-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Źródła:
-[MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

-[cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## Jak uruchomić skrypt

**Skrypt można uruchomić z wyodrębnionego pliku do pobrania z GitHuba w następujący sposób:**.

```
.\sos-install-java-config.ps1
```
