---
title: "Automate Oracle JRE 8 STIG Compliance with Powershell Script"
date: 2020-08-05T21:54:53-05:00
toc: true
draft: false
description: "Simplify the process of configuring Oracle JRE 8 STIG compliance with an automated Powershell script, eliminating the need for manual research and configuration."
tags: ["Oracle JRE 8 STIG", "JAVA STIG", "JRE", "JRE8", "JRE STIG", "Compliance", "Automation", "Powershell", "Script", "JAVA Configuration", "Java Documentation", "Group Policy", "IT Security", "System Administration", "Configuration Management", "Windows", "Cybersecurity", "STIG Compliance", "Information Technology", "Software Configuration"]
---
```
.\sos-install-java-config.ps1
```

  Los STIG de Oracle JRE no son tan sencillos, ya que requieren que los administradores investiguen la documentación de JAVA y generen archivos de configuración de Java, cuando la mayoría de los administradores están acostumbrados a STIG utilizando únicamente la política de grupo.  ## Descarga los archivos requeridos  Descargue los archivos necesarios del [repositorio de GitHub] (https://github.com/simeononsecurity/JAVA-STIG-Script)  ## STIGS/SRG aplicados: - [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)  ## Fuentes: - [MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)  - [cbu.edu - Notas técnicas de Java] (http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)  ##ejecutar cómo el script  **El script se puede iniciar desde la descarga de GitHub extraída de esta manera:** 