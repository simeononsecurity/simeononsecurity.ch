---
title: "Aumente la seguridad de su sistema con los comandos PowerShell de Windows Defender"
date: 2023-07-27
toc: true
draft: false
description: "Descubra el poder de los comandos PowerShell de Windows Defender y aprenda a mejorar la seguridad de su sistema con el control de la línea de comandos."
genre: ["Windows Defender", "Comandos PowerShell", "seguridad del sistema", "control por línea de comandos", "antivirus", "Sistemas operativos Windows", "protección antimalware", "configuración de seguridad avanzada", "automatizar las operaciones de seguridad", "Windows PowerShell"]
tags: ["Tecnología", "Ciberseguridad", "Sistemas operativos", "Windows", "Herramientas de línea de comandos", "Seguridad del sistema", "PowerShell", "Antivirus", "Protección contra malware", "Scripting"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.png"
coverAlt: "Ilustración animada que representa un escudo que protege un sistema informático de diversas ciberamenazas."
coverCaption: "Potencie la seguridad de su sistema con los comandos PowerShell de Windows Defender."
---

## Introducción

Windows Defender, desarrollado por Microsoft, es una solución integrada de antivirus y seguridad para sistemas operativos Windows. Ofrece una interfaz fácil de usar para gestionar eficazmente la configuración de seguridad. Sin embargo, para los usuarios avanzados que prefieren el control desde la línea de comandos, Windows Defender proporciona un conjunto de potentes comandos PowerShell. En este artículo, nos adentraremos en el mundo de los **comandos PowerShell de Windows Defender** y exploraremos cómo pueden mejorar la seguridad del sistema y proporcionar un mayor control sobre su entorno Windows.

## El poder de los comandos PowerShell de Windows Defender

Los comandos PowerShell de Windows Defender permiten a los usuarios realizar operaciones de seguridad avanzadas mediante una interfaz de línea de comandos. Estos comandos proporcionan una amplia gama de funcionalidades, desde operaciones sencillas como la búsqueda de malware hasta tareas complejas como la configuración de parámetros de seguridad avanzados. Utilizando PowerShell, los usuarios pueden automatizar operaciones de seguridad, crear scripts personalizados e integrar Windows Defender en sus flujos de trabajo existentes sin problemas.

## Introducción a Windows Defender PowerShell

Para acceder a los comandos de Windows Defender PowerShell, debe abrir una sesión de PowerShell con privilegios administrativos. A continuación se explica cómo empezar:

1. Pulsa `Win + X` y seleccione **Windows PowerShell (Admin)** en el menú.
2. Si se le solicita, haga clic en **Sí** para permitir que la aplicación realice cambios en el dispositivo.

Una vez que tenga abierta una sesión de PowerShell, puede empezar a utilizar los comandos de PowerShell de Windows Defender.

## Comandos comunes de Windows Defender PowerShell

### 1. **Get-MpComputerStatus**: Comprueba el estado de Windows Defender

El `Get-MpComputerStatus` proporciona una descripción general del estado actual de Windows Defender en el sistema, incluida la versión del motor antivirus, la última hora de análisis y el estado de la protección en tiempo real. Al ejecutar este comando, puede evaluar rápidamente el estado general de Windows Defender y asegurarse de que funciona de forma óptima.

Para comprobar el estado de Windows Defender, abra una sesión de PowerShell con privilegios administrativos y ejecute el siguiente comando:

```powershell
Get-MpComputerStatus
```

Este comando mostrará información como:

- **AntivirusEngineVersion**: El número de versión del motor antivirus utilizado por Windows Defender.
- **LastFullScanTime**: La fecha y hora del último análisis completo realizado por Windows Defender.
- **LastQuickScanTime**: La fecha y hora del último análisis rápido realizado por Windows Defender.
- RealTimeProtectionEnabled**: Indica si la protección en tiempo real está activada o desactivada.

Supervisar regularmente el estado de Windows Defender mediante `Get-MpComputerStatus` le garantiza que se mantendrá informado sobre el nivel de protección de su sistema frente a posibles amenazas.

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

En `Update-MpSignature` le permite actualizar manualmente las firmas antivirus utilizadas por Windows Defender. Las firmas antivirus contienen información crucial sobre el malware conocido, lo que permite a Windows Defender detectar y bloquear las amenazas con eficacia. Ejecutando este comando, te aseguras de que tu sistema tiene las firmas más recientes, proporcionando una protección mejorada contra las amenazas emergentes.

Para actualizar manualmente las firmas de Windows Defender, abra una sesión de PowerShell con privilegios administrativos y ejecute el siguiente comando:

```powershell
Update-MpSignature
```
Este comando activa el proceso de actualización, en el que **Windows Defender** se conecta a **servidores de Microsoft** para descargar las **firmas antivirus** más recientes. Una vez completada la actualización, Windows Defender dispondrá de la información más actualizada sobre el malware conocido, lo que reforzará su capacidad para identificar y eliminar amenazas.

Mantener las firmas de Windows Defender actualizadas es esencial para mantener el máximo nivel de protección contra el panorama en constante evolución del **malware** y las **amenazas cibernéticas**. Actualizando regularmente las firmas mediante `Update-MpSignature` se asegura de que Windows Defender pueda proteger eficazmente su sistema.

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

En `Set-MpPreference` le permite personalizar varias opciones de **Windows Defender**, lo que le permite adaptar su comportamiento para satisfacer sus requisitos de seguridad específicos. Este comando proporciona flexibilidad para configurar opciones como **protección en tiempo real**, **protección basada en la nube** y **configuración del sistema de inspección de red**.

Por ejemplo, puede activar o desactivar la protección en tiempo real mediante el comando `Set-MpPreference` comando. La protección en tiempo real supervisa activamente su sistema en busca de actividades maliciosas y proporciona una respuesta inmediata a las amenazas. Para activar la protección en tiempo real, ejecute el siguiente comando:

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

Además, puede aprovechar el comando para ajustar la configuración de la protección basada en la nube. La protección basada en la nube utiliza recursos de la nube para mejorar la detección de amenazas y proporcionar respuestas más rápidas a las amenazas emergentes. Para activar la protección basada en la nube, utilice el siguiente comando:

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

Además, el `Set-MpPreference` permite personalizar la configuración del sistema de inspección de red. El sistema de inspección de red analiza el tráfico de red en busca de actividades sospechosas y amenazas potenciales. Para ajustar la configuración del sistema de inspección de red, ejecute el siguiente comando:

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

Ajustando estos parámetros con `Set-MpPreference` puede optimizar **Windows Defender** para adaptarlo a sus necesidades de seguridad específicas y garantizar una protección sólida contra el malware y otras actividades maliciosas.

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

En `Start-MpScan` es una poderosa herramienta para iniciar escaneos de malware en su sistema, permitiéndole identificar y eliminar proactivamente archivos maliciosos. Este comando proporciona flexibilidad a la hora de realizar diferentes tipos de escaneos, incluyendo **escaneos rápidos**, **escaneos completos** y **escaneos personalizados** con rutas específicas.

Para realizar un **escaneo rápido** utilizando el comando `Start-MpScan` ejecute el siguiente comando PowerShell:

```powershell
Start-MpScan -ScanType QuickScan
```

Un escaneado rápido se centra en las áreas críticas del sistema en las que se suele encontrar malware, proporcionando una evaluación rápida de las amenazas potenciales.

Para un análisis más exhaustivo que examine todos los archivos y directorios del sistema, puede iniciar un **análisis completo**. Ejecute el siguiente comando para realizar un análisis completo utilizando `Start-MpScan`

```powershell
Start-MpScan -ScanType FullScan
```

Un análisis completo garantiza una detección y eliminación exhaustivas del malware del sistema, pero puede tardar más en completarse que un análisis rápido.

Además de los tipos de análisis predefinidos, el `Start-MpScan` le permite realizar escaneos personalizados especificando rutas o archivos específicos a escanear. Por ejemplo, puede escanear un directorio específico de su sistema utilizando el siguiente comando:

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

Este comando iniciará un escaneo personalizado en el directorio especificado, permitiéndole seleccionar áreas específicas de su sistema para la detección de malware.

Aprovechando la versatilidad del comando `Start-MpScan` puede programar análisis, automatizar procesos de seguridad y garantizar la detección y mitigación periódicas de malware en su sistema.

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

En `Get-MpThreatCatalog` es un recurso valioso para obtener información detallada sobre amenazas conocidas y sus atributos. Al ejecutar este comando, puede acceder a un catálogo completo de amenazas, que incluye datos sobre su gravedad, los nombres de los archivos asociados y las acciones recomendadas para mitigarlas.

Para recuperar información sobre amenazas específicas utilizando `Get-MpThreatCatalog` sigue estos pasos:

1. Abra una sesión de PowerShell con privilegios administrativos.
2. Ejecute el siguiente comando:

```powershell
   Get-MpThreatCatalog
```
Este comando mostrará una lista de amenazas conocidas junto con sus correspondientes detalles.

La salida del comando `Get-MpThreatCatalog` comando incluye información esencial como:

- **ThreatID**: Un identificador único para la amenaza.
- Severidad**: Indica el nivel de gravedad de la amenaza, que va de Baja a Grave.
- Nombre**: El nombre o descripción de la amenaza.
- Ruta**: La ruta del fichero asociado a la amenaza.
- Acción recomendada**: Proporciona orientación sobre la acción recomendada para mitigar la amenaza.

Aprovechando la información obtenida de `Get-MpThreatCatalog` puede obtener información valiosa sobre las amenazas potenciales y tomar decisiones informadas sobre las acciones adecuadas para mitigarlas. Ya se trate de aislar, eliminar o supervisar una amenaza concreta, el catálogo detallado le permite responder con eficacia a los incidentes de seguridad.

Para obtener más información sobre el uso de `Get-MpThreatCatalog` e interpretar sus resultados, consulte la documentación oficial de Microsoft.

Manténgase alerta y utilice regularmente el `Get-MpThreatCatalog` para mantenerse informado sobre la evolución del panorama de las amenazas y mejorar la seguridad de su sistema.

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

En `Add-MpPreference` le permite agregar exclusiones a Windows Defender, lo que le permite personalizar el comportamiento del análisis y la protección en tiempo real. Al añadir exclusiones, puede especificar archivos, carpetas o procesos que desea que Windows Defender ignore durante los análisis de seguridad o la protección en tiempo real.

Para añadir una exclusión mediante `Add-MpPreference` debe indicar la ruta o el nombre del archivo, carpeta o proceso que desea excluir. Este es un ejemplo de exclusión de una carpeta:

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

Este comando garantiza que Windows Defender omita el análisis de la carpeta especificada, lo que reduce las alertas innecesarias y las posibles interrupciones de su flujo de trabajo.

Las exclusiones pueden ser útiles en varios escenarios, como la exclusión de aplicaciones de confianza, entornos de desarrollo o archivos específicos que pueden desencadenar falsos positivos. Al aprovechar la flexibilidad de `Add-MpPreference` puede ajustar Windows Defender para adaptarlo a sus necesidades de seguridad específicas y optimizar su rendimiento.

Proteja su sistema de forma eficaz a la vez que minimiza los falsos positivos y las interrupciones innecesarias del análisis utilizando las potentes funciones de exclusión que ofrece `Add-MpPreference`

## Conclusión

Los comandos PowerShell de Windows Defender proporcionan un **sólido conjunto de herramientas** para administrar y mejorar la seguridad de su sistema Windows. Aprovechando estos comandos, puede *automatizar operaciones de seguridad*, *configurar opciones avanzadas* e incorporar Windows Defender sin problemas a sus flujos de trabajo. Tanto si es un **administrador del sistema** como un **usuario avanzado**, explorar las capacidades de los comandos PowerShell de Windows Defender puede mejorar significativamente la postura de seguridad de su sistema.

Recuerde que un gran poder conlleva una gran responsabilidad. Cuando utilice comandos PowerShell, sea precavido y asegúrese de comprender el impacto de los comandos antes de ejecutarlos. Combinando sus conocimientos con la potencia de los comandos PowerShell de Windows Defender, podrá tomar medidas proactivas para proteger su sistema de las amenazas en evolución.

## Referencias

1. Microsoft Docs - [Windows Defender Cmdlets in Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. Microsoft Docs - [Introduction to Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
