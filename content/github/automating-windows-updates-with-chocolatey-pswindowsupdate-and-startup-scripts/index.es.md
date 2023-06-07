---
title: "Agilice las actualizaciones de Windows con la automatización mediante Chocolatey, PSWindowsUpdate y secuencias de comandos de inicio"
date: 2020-07-22
---
 Actualizaciones de Windows con Chocolatey, PSWindowsUpdate y secuencias de comandos de inicio**

En el acelerado entorno empresarial actual, el tiempo es esencial para los administradores de sistemas. La actualización de equipos Windows, un aspecto crítico de la administración de sistemas, puede ser una tarea extremadamente lenta que puede llevar hasta una semana, si se dispone de suficientes sistemas. Sin embargo, con la ayuda de Chocolatey, PSWindowsUpdates y Startup Scripts, ahora es posible desplegar actualizaciones con tan sólo reiniciar cada máquina, lo que reduce significativamente el tiempo necesario para realizar las actualizaciones.

## Racionalización de las actualizaciones de Windows con la automatización

Las actualizaciones de Windows son fundamentales para mantener la estabilidad y la seguridad de los equipos Windows. Realizar actualizaciones en un gran número de equipos puede ser una tarea que lleve mucho tiempo, especialmente para los administradores de sistemas con recursos limitados. Sin embargo, con el uso de herramientas de automatización como Chocolatey, PSWindowsUpdate y Startup Scripts, este proceso se puede agilizar para permitir a los administradores realizar actualizaciones con el mínimo esfuerzo.

### Chocolatey

[Chocolatey](https://chocolatey.org/) es un gestor de paquetes para Windows que puede utilizarse para automatizar la instalación de software en máquinas Windows. Es similar a apt-get en Ubuntu u homebrew en macOS, y puede utilizarse para instalar y gestionar una amplia gama de paquetes de software. Chocolatey puede utilizarse para instalar paquetes de forma silenciosa, lo que significa que pueden instalarse sin intervención del usuario.

### PSWindowsUpdate

[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) es un módulo de PowerShell que puede utilizarse para automatizar la instalación de actualizaciones de Windows. Proporciona cmdlets que pueden utilizarse para instalar, desinstalar y listar actualizaciones de Windows. PSWindowsUpdate es una potente herramienta que se puede utilizar para gestionar las actualizaciones de Windows en varios equipos, por lo que es ideal para los administradores de sistemas que necesitan gestionar un gran número de equipos.

### Scripts de Inicio

[Startup Scripts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn789190(v=ws.11)) son secuencias de comandos que pueden utilizarse para automatizar tareas que deben realizarse cuando un equipo se inicia o se apaga. Estos scripts pueden utilizarse para realizar tareas como instalar software, configurar ajustes y gestionar actualizaciones de Windows.

## Automatización de actualizaciones de Windows con un solo reinicio

Para automatizar las actualizaciones de Windows utilizando Chocolatey, PSWindowsUpdate y Startup Scripts, los administradores pueden seguir la siguiente guía paso a paso.

### Configuración del Script de Apagado
Descargue todos los archivos de soporte de la página [GitHub Repository](https://github.com/simeononsecurity/ChocoAutomateWindowsUpdates)

1. Abre el Editor de directivas de grupo locales pulsando **"Win + R "** y escribiendo **"gpedit.msc "** seguido de **"Ctrl + Mayús + Intro "**.
2. 2. Vaya a Equipo **Configuración\Configuración de Windows\Scripts (Inicio/Apagado)**.
3. En el panel de resultados, haz doble clic en Apagar.
4. 4. Seleccione la pestaña PowerShell.
5. En el cuadro de diálogo Propiedades de apagado, haga clic en Agregar.
6. En el cuadro Nombre de script, escriba la ruta al script o haga clic en Examinar para buscar "*chocoautomatewindowsupdates.ps1*" en la carpeta compartida Netlogon del controlador de dominio.
7. 7. Reinicie.

Ahora, todo lo que tiene que hacer un administrador es reiniciar el equipo para realizar las actualizaciones de Windows.

### Entendiendo el Script

El script utilizado para automatizar las actualizaciones de Windows se titula "*chocoautomatewindowsupdates.ps1*". Realiza las siguientes tareas:

1. Instala el gestor de paquetes Chocolatey.
2. Habilita un par de cambios de configuración preferentes de Chocolatey.
3. Actualiza todos los paquetes Chocolatey instalados.
4. Instala el módulo PowerShell PSWindowsUpdate.
5. Añade el administrador de servicios de Windows Update.
6. Instala todas las actualizaciones disponibles de Windows.
7. Instala los controladores que falten o las actualizaciones requeridas por las actualizaciones previamente instaladas.

### Ventajas de automatizar las actualizaciones de Windows

Automatizar las actualizaciones de Windows utilizando Chocolatey, PSWindowsUpdate y Startup Scripts tiene varios beneficios para los administradores de sistemas. Estos beneficios incluyen:

- Ahorro de tiempo**: La automatización de las actualizaciones de Windows reduce significativamente el tiempo necesario para llevarlas a cabo. Los administradores ya no tienen que instalar manualmente las actualizaciones en cada máquina.
- Coherencia**: La automatización de las actualizaciones de Windows garantiza que las actualizaciones se instalen de forma coherente en todos los equipos. Esto reduce la probabilidad de errores y vulnerabilidades de seguridad.
- Gestión centralizada**: La automatización de las actualizaciones de Windows permite a los administradores gestionar las actualizaciones desde una ubicación central, lo que facilita el seguimiento de las actualizaciones que se han instalado y de los equipos que necesitan actualizaciones.
- Mayor seguridad**: La automatización de las actualizaciones de Windows garantiza que los equipos se mantengan al día con los últimos parches de seguridad, lo que reduce el riesgo de brechas de seguridad.

### Conclusión

La automatización de las actualizaciones de Windows mediante Chocolatey, PSWindowsUpdate y Startup Scripts es una potente herramienta que puede ahorrar mucho tiempo y esfuerzo a los administradores de sistemas. Permite que las actualizaciones se instalen de forma consistente y eficiente, asegurando que las máquinas están al día con los últimos parches de seguridad. Siguiendo los pasos descritos en este tutorial, los administradores pueden automatizar las actualizaciones de Windows con un solo reinicio, haciendo que el proceso de actualización de los equipos Windows sea mucho más rápido y sencillo.
