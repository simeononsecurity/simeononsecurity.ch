---
title: "Automatyzacja zgodności Oracle JRE 8 STIG za pomocą skryptu Powershell"
date: 2020-08-05
---


STIG Oracle JRE nie są tak proste, wymagając od administratorów zbadania dokumentacji JAVA i wygenerowania plików konfiguracyjnych java, podczas gdy większość administratorów jest przyzwyczajona do STIG-owania wyłącznie za pomocą zasad grupy.

## Pobierz wymagane pliki

Pobierz wymagane pliki ze strony [GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## STIGS/SRGs Applied:
- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Źródła:
- [MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

- [cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## Jak uruchomić skrypt

**Skrypt można uruchomić z wyodrębnionego pliku do pobrania z GitHub w następujący sposób:**

```
.\sos-install-java-config.ps1
```
