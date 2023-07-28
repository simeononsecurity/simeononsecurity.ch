---
title: "Análisis de virus eficientes con los módulos PowerShell de VirusTotal"
date: 2020-11-24
toc: true
draft: false
description: "Realice escaneos de virus eficientes con los Módulos PowerShell de VirusTotal automatizando la interacción con la API de VirusTotal y agilizando su flujo de trabajo de seguridad."
tags: ["Módulos PowerShell", "PowerShell", "Automatización", "VirusTotal", "Análisis de virus", "Exploración de dominios", "Clave API", "API de VirusTotal", "Página para desarrolladores de VirusTotal", "Administración del sistema", "Flujo de trabajo de seguridad", "Análisis antivirus eficaces", "Descargar e instalar", "Repositorio GitHub", "Ejemplos de uso de la API"]
---
 Colección de módulos PowerShell para interactuar con la API de VirusTotal

**Notas
- Necesitarás tu clave de la API de VirusTotal, que se puede encontrar en tu [Shodan Account](https://www.virustotal.com/gui/)
- Puede encontrar ejemplos de las API utilizadas en los módulos en la página [VirusTotal Developers Page](https://developers.virustotal.com/reference#getting-started)

## Descarga e instalación
- Descargue los módulos de la página [GitHub Repository](https://github.com/simeononsecurity/VirusTotal-PS)
- Instalar todos los módulos
```ps
Get-ChildItem -Recurse *.ps1 | Import-Module
```