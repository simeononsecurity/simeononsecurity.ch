---
title: "Automatice la activación de Windows KMS con el script GLVK"
date: 2020-12-18
toc: true
draft: false
description: "Simplifique el proceso de activación de KMS de Windows 10 y Windows 11 con el script de instalación automática de GLVK de SimeonOnSecurity y obtenga más información sobre KMS y las claves de cliente GLVK en las lecturas recomendadas de Microsoft."
tags: ["Activación de Windows", "Claves de cliente KMS", "GLVK", "Actualizaciones de Windows", "Conformidad", "Script Powershell", "Servicio de gestión de claves", "Licencias por volumen", "Activación de empresas", "Servidor de gestión de claves", "Automatización", "Productos Microsoft", "Sistema operativo", "Software", "Entornos empresariales", "Powershell administrativo", "Repositorio GitHub", "Scripting", "Ciberseguridad", "SimeonOnSecurity", "Activación de KMS", "Script de instalación automática de GLVK", "Productos Windows", "empresa", "gestión centralizada", "para ahorrar tiempo", "Administración informática", "activación simplificada", "sin complicaciones", "productividad", "reducción de errores", "capacidades de supervisión", "eficacia", "activación de software", "clave de licencia por volumen", "automatización de scripts", "Gestión informática", "proceso de activación", "licencias de software", "gestión de licencias", "herramienta de activación", "despliegue de software", "Productividad informática"]
---

**Script de autoinstalaciónGLVK para la activación de KMS**

*Lectura recomendada [Microsoft - KMS Client Keys (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## Introducción

La activación KMS (Key Management Service) es un método utilizado por Microsoft para activar y licenciar sus productos en entornos empresariales. El proceso implica un servidor central que activa los ordenadores cliente asignándoles una clave de licencia por volumen denominada GLVK (Generic Volume License Key).

En este artículo, exploraremos la secuencia de comandos de instalación automática de GLVK, que simplifica el proceso de activación de productos Windows mediante KMS. Proporcionaremos instrucciones paso a paso sobre cómo ejecutar el script y destacaremos sus ventajas para las organizaciones.

## Lectura recomendada

Antes de sumergirse en el script de instalación automática de GLVK, se recomienda familiarizarse con el concepto de KMS y las claves de cliente KMS disponibles proporcionadas por Microsoft. Puede consultar la siguiente documentación de Microsoft para obtener más información:

- [Microsoft - KMS Client Keys (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## Cómo ejecutar el script

### Instalación Manual

Para instalar y ejecutar manualmente el script de autoinstalación GLVK, siga estos pasos:

1. Descargue el script y los archivos relacionados desde la página [GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
2. Inicie una sesión administrativa de PowerShell.
3. Navegue hasta el directorio que contiene todos los archivos descargados.
4. 4. Ejecute los siguientes comandos:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```

Estos comandos establecerán la política de ejecución en RemoteSigned para permitir la ejecución de scripts, desbloquearán cualquier script PowerShell descargado y ejecutarán el script de instalación automática GLVK.

## Ventajas del script de instalación automática de GLVK

El script de instalación automática GLVK ofrece varias ventajas a las organizaciones que desean activar productos Windows mediante KMS:

1. **Activación simplificada**: El script automatiza el proceso de activación de KMS, eliminando la necesidad de configuración manual y reduciendo el error humano.

2. **Ahorro de tiempo y esfuerzo**: Al utilizar el script, los administradores de TI pueden ahorrar un tiempo y un esfuerzo significativos que, de otro modo, se emplearían en procedimientos de activación manual para múltiples máquinas.

3. **Gestión centralizada**: El GLVK Auto Install Script permite la gestión centralizada de la activación de KMS, proporcionando un mejor control y capacidades de supervisión.

## Conclusión

El GLVK Auto Install Script es una herramienta valiosa para las organizaciones que buscan un método eficaz y racionalizado de activación de productos Windows mediante KMS. Al automatizar el proceso de activación, ahorra tiempo, reduce errores y mejora las capacidades de gestión centralizada. Con las instrucciones paso a paso proporcionadas, las organizaciones pueden implementar fácilmente el script y disfrutar de las ventajas de una activación KMS sin complicaciones.

## Referencias

1. [Microsoft - KMS Client Keys (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)
2. [GitHub Repository - GLVK Auto Install Script](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
