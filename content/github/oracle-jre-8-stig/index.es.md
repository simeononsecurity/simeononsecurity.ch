---
title: "Automatice el cumplimiento de las STIG de Oracle JRE 8 con un script de Powershell"
date: 2020-08-05
---


Las STIG de Oracle JRE no son tan sencillas, ya que requieren que los administradores investiguen la documentación de JAVA y generen archivos de configuración de Java, cuando la mayoría de los administradores están acostumbrados a utilizar únicamente las STIG mediante políticas de grupo.

## Descargar los archivos necesarios

Descargue los archivos necesarios de la página [GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## STIGS/SRGs Applied:
- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Fuentes:
- [MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

- [cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## Cómo ejecutar el script

**El script puede ser descargado desde GitHub de la siguiente manera

```
.\sos-install-java-config.ps1
```
