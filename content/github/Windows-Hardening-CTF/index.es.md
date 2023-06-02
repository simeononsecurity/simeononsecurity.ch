---
title: "Windows Hardening CTF: Refuerce la seguridad de su dispositivo Windows para eventos de Captura de la Bandera"
date: 2020-10-19
toc: true
draft: false
description: "Descubra una potente secuencia de comandos que mejora la seguridad de Windows mediante la aplicación de varias medidas de refuerzo para impedir el compromiso."
tags: ["Endurecimiento de Windows", "Seguridad de Windows", "script", "Dispositivo Windows", "símbolo del sistema", "LLMNR", "PowerShell", "PYME", "Marcas de tiempo TCP", "AppLocker", "Registro de Windows", "DEP", "Configuraciones EMET", "Modo de lenguaje restringido de PowerShell", "Cifrado SMB", "Mitigación de Spectre y Meltdown", "Windows Defender", "Cortafuegos de Windows", "PSWindowsUpdate", "Actualizaciones de Windows", "script de endurecimiento", "Políticas recomendadas por la ANS", "Registro y controles de seguridad de Windows", "Control de aplicaciones de Windows Defender", "Procedimientos de reducción de la superficie de ataque de Windows Defender", "Protecciones basadas en la nube de Windows Defender", "Protecciones contra exploits de Windows Defender", "Instalación de PSWindowsUpdate", "Mejora de la seguridad de los dispositivos Windows", "Medidas de protección de Windows", "reforzar la seguridad de Windows"]
---

**Endurecimiento de Windows-CTF**
Un script de endurecimiento de Windows que hace más difícil y molesto comprometer un dispositivo Windows.

## ¿Qué hace este script?
- Desactiva el Símbolo del sistema
- Desactiva LLMNR
- Desactiva PowerShell v2
- Desactiva SMB Compression
- Desactiva SMB v1
- Desactiva SMB v2
- Desactiva TCP Timestamps
- Desactiva WSMAN y PSRemoting
- Habilita AppLocker con las políticas recomendadas por la NSA
- Habilita las mejores prácticas de registro y controles de seguridad de Windows
- Activa DEP
- Habilita las configuraciones de EMET (sólo se aplica a sistemas con EMET instalado)
- Habilita el Modo de Lenguaje Construido de PowerShell
- Habilita el registro de PowerShell
- Habilita el cifrado SMB
- Habilita las mitigaciones de Spectre y Meltdown
- Habilita el control de aplicaciones de Windows Defender
- Habilita las funciones de reducción de la superficie de ataque de Windows Defender
- Habilita las protecciones basadas en la nube de Windows Defender
- Habilita las protecciones contra exploits de Windows Defender
- Habilita el cortafuegos y el registro de Windows
- Instala PSWindowsUpdate e instala todas las actualizaciones de Windows disponibles

## Descarga los archivos necesarios:

Descarga los archivos necesarios de la [GitHub Repository](https://github.com/simeononsecurity/Windows-Hardening-CTF)

## Cómo ejecutar el script:

**El script puede ser descargado desde GitHub de la siguiente manera:**
```
.\sos-windows-hardening-ctf.ps1
```
