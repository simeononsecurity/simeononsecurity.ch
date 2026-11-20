---
title: "Comandos de PowerShell de Windows Defender para la seguridad del sistema"
date: 2023-07-27
lastmod: 2026-11-20
toc: true
draft: false
description: "Descubra el poder de los comandos PowerShell de Windows Defender y aprenda a mejorar la seguridad de su sistema con el control de la línea de comandos."
genre: ["Windows Defender", "Comandos PowerShell", "seguridad del sistema", "control por línea de comandos", "antivirus", "Sistemas operativos Windows", "protección antimalware", "configuración de seguridad avanzada", "automatizar las operaciones de seguridad", "Windows PowerShell"]
tags: ["Tecnología", "Ciberseguridad", "Sistemas operativos", "Windows", "Herramientas de línea de comandos", "Seguridad del sistema", "PowerShell", "Antivirus", "Protección contra malware", "Creación de scripts"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.webp"
coverAlt: "Ilustración animada que representa un escudo que protege un sistema informático de diversas ciberamenazas."
coverCaption: "Potencie la seguridad de su sistema con los comandos PowerShell de Windows Defender."
---

## Introducción

Windows Defender, desarrollado por Microsoft, es una solución integrada de antivirus y seguridad para sistemas operativos Windows. Ofrece una interfaz fácil de usar para gestionar eficazmente la configuración de seguridad. Sin embargo, para los usuarios avanzados que prefieren el control desde la línea de comandos, Windows Defender proporciona un conjunto de potentes comandos PowerShell. En este artículo, nos adentraremos en el mundo de los **comandos PowerShell de Windows Defender** y exploraremos cómo pueden mejorar la seguridad del sistema y proporcionar un mayor control sobre su entorno Windows.

## El poder de los comandos PowerShell de Windows Defender

Los comandos PowerShell de Windows Defender permiten a los usuarios realizar operaciones de seguridad avanzadas mediante una interfaz de línea de comandos. Estos comandos proporcionan una amplia gama de funcionalidades, desde operaciones sencillas como la búsqueda de malware hasta tareas complejas como la configuración de parámetros de seguridad avanzados. Utilizando PowerShell, los usuarios pueden automatizar operaciones de seguridad, crear scripts personalizados e integrar Windows Defender en sus flujos de trabajo existentes sin problemas.

## Introducción a Windows Defender PowerShell

Para acceder a los comandos de Windows Defender PowerShell, debe abrir una sesión de PowerShell con privilegios administrativos. A continuación se explica cómo empezar:

1. Pulse `Win + X` y seleccione **Windows PowerShell (Admin)** (como administrador) en el menú.
2. Si se le solicita, haga clic en **Yes** (Sí) para permitir que la aplicación realice cambios en el dispositivo.

Una vez que tenga abierta una sesión de PowerShell, puede empezar a utilizar los comandos de PowerShell de Windows Defender.

## Comandos comunes de Windows Defender PowerShell

### 1. **Get-MpComputerStatus**: Comprueba el estado de Windows Defender

El comando `Get-MpComputerStatus` ofrece una descripción general del estado actual de Windows Defender en el sistema, incluida la versión del motor antivirus, la hora del último análisis y el estado de la protección en tiempo real. Al ejecutarlo, puede evaluar rápidamente el estado de Windows Defender y comprobar que funciona correctamente.

Para comprobar el estado de Windows Defender, abra una sesión de PowerShell con privilegios administrativos y ejecute el siguiente comando:

```powershell
Get-MpComputerStatus
```

Este comando mostrará información como:

- **AntivirusEngineVersion**: El número de versión del motor antivirus utilizado por Windows Defender.
- **LastFullScanTime**: La fecha y hora del último análisis completo realizado por Windows Defender.
- **LastQuickScanTime**: La fecha y hora del último análisis rápido realizado por Windows Defender.
- **RealTimeProtectionEnabled**: Indica si la protección en tiempo real está activada o desactivada.

Supervisar regularmente el estado de Windows Defender mediante `Get-MpComputerStatus` le garantiza que se mantendrá informado sobre el nivel de protección de su sistema frente a posibles amenazas.

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

El comando `Update-MpSignature` permite actualizar manualmente las firmas antivirus que utiliza Windows Defender. Estas firmas contienen información importante sobre el malware conocido y ayudan a Windows Defender a detectar y bloquear amenazas. Al ejecutar este comando, el sistema obtiene las firmas más recientes y una mayor protección frente a nuevas amenazas.

Para actualizar manualmente las firmas de Windows Defender, abra una sesión de PowerShell con privilegios administrativos y ejecute el siguiente comando:

```powershell
Update-MpSignature
```
Este comando activa el proceso de actualización, en el que **Windows Defender** se conecta a **servidores de Microsoft** para descargar las **firmas antivirus** más recientes. Una vez completada la actualización, Windows Defender dispondrá de la información más actualizada sobre el malware conocido, lo que reforzará su capacidad para identificar y eliminar amenazas.

Mantener las firmas de Windows Defender actualizadas es esencial para mantener el máximo nivel de protección contra el panorama en constante evolución del **malware** y las **amenazas cibernéticas**. Actualizando regularmente las firmas mediante `Update-MpSignature` se asegura de que Windows Defender pueda proteger eficazmente su sistema.

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

El comando `Set-MpPreference` permite personalizar varios ajustes de **Windows Defender** para adaptarlo a sus requisitos de seguridad. Puede configurar opciones como la **protección en tiempo real**, la **protección basada en la nube** y los **ajustes del sistema de inspección de red**.

Por ejemplo, puede activar o desactivar la protección en tiempo real con `Set-MpPreference`. Esta función supervisa el sistema para detectar actividades maliciosas y responde de inmediato a las amenazas. Para activar la protección en tiempo real, ejecute el siguiente comando:

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

Además, puede aprovechar el comando para ajustar la configuración de la protección basada en la nube. La protección basada en la nube utiliza recursos de la nube para mejorar la detección de amenazas y proporcionar respuestas más rápidas a las amenazas emergentes. Para activar la protección basada en la nube, utilice el siguiente comando:

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

Además, puede usar `Set-MpPreference` para personalizar los ajustes del sistema de inspección de red. Este sistema analiza el tráfico de red en busca de actividades sospechosas y posibles amenazas. Para cambiar sus ajustes, ejecute el siguiente comando:

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

Ajustando estos parámetros con `Set-MpPreference` puede optimizar **Windows Defender** para adaptarlo a sus necesidades de seguridad específicas y garantizar una protección sólida contra el malware y otras actividades maliciosas.

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

El comando `Start-MpScan` inicia análisis de malware en el sistema para ayudarle a detectar y eliminar archivos maliciosos. Permite realizar distintos tipos de análisis, incluidos **análisis rápidos**, **análisis completos** y **análisis personalizados** de rutas concretas.

Para realizar un **análisis rápido** con `Start-MpScan`, ejecute el siguiente comando de PowerShell:

```powershell
Start-MpScan -ScanType QuickScan
```

Un escaneado rápido se centra en las áreas críticas del sistema en las que se suele encontrar malware, proporcionando una evaluación rápida de las amenazas potenciales.

Para examinar todos los archivos y directorios del sistema, puede iniciar un **análisis completo**. Ejecute el siguiente comando con `Start-MpScan`:

```powershell
Start-MpScan -ScanType FullScan
```

Un análisis completo garantiza una detección y eliminación exhaustivas del malware del sistema, pero puede tardar más en completarse que un análisis rápido.

Además de los tipos de análisis predefinidos, `Start-MpScan` permite analizar rutas o archivos concretos. Por ejemplo, puede analizar un directorio específico con el siguiente comando:

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

Este comando iniciará un escaneo personalizado en el directorio especificado, permitiéndole seleccionar áreas específicas de su sistema para la detección de malware.

Aprovechando la versatilidad del comando `Start-MpScan` puede programar análisis, automatizar procesos de seguridad y garantizar la detección y mitigación periódicas de malware en su sistema.

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

El comando `Get-MpThreatCatalog` proporciona información detallada sobre amenazas conocidas y sus atributos. El catálogo incluye datos sobre su gravedad, los nombres de los archivos asociados y las acciones recomendadas para mitigarlas.

Para consultar información sobre amenazas concretas con `Get-MpThreatCatalog`, siga estos pasos:

1. Abra una sesión de PowerShell con privilegios administrativos.
2. Ejecute el siguiente comando:

```powershell
   Get-MpThreatCatalog
```
Este comando mostrará una lista de amenazas conocidas junto con sus correspondientes detalles.

La salida del comando `Get-MpThreatCatalog` incluye información esencial como:

- **ThreatID**: Un identificador único para la amenaza.
- **Severity**: Indica el nivel de gravedad de la amenaza, de Low a Severe.
- **Name**: El nombre o la descripción de la amenaza.
- **Path**: La ruta del archivo asociado a la amenaza.
- **RecommendedAction**: Indica la acción recomendada para mitigar la amenaza.

La información de `Get-MpThreatCatalog` le permite conocer posibles amenazas y decidir cómo responder. Puede aislar, eliminar o supervisar una amenaza. El catálogo detallado le ayuda a responder eficazmente a incidentes de seguridad.

Para obtener más información sobre el uso de `Get-MpThreatCatalog` e interpretar sus resultados, consulte la documentación oficial de Microsoft.

Use `Get-MpThreatCatalog` con regularidad para mantenerse al tanto de las amenazas y mejorar la seguridad del sistema.

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

El comando `Add-MpPreference` permite añadir exclusiones a Windows Defender para personalizar el análisis y la protección en tiempo real. Puede indicar los archivos, carpetas o procesos que Windows Defender debe omitir durante los análisis de seguridad o la protección en tiempo real.

Para añadir una exclusión con `Add-MpPreference`, indique la ruta o el nombre del archivo, carpeta o proceso que desea excluir. Este ejemplo añade una exclusión para una carpeta:

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

Este comando garantiza que Windows Defender omita el análisis de la carpeta especificada, lo que reduce las alertas innecesarias y las posibles interrupciones de su flujo de trabajo.

Las exclusiones pueden ser útiles en varios escenarios, como la exclusión de aplicaciones de confianza, entornos de desarrollo o archivos específicos que pueden desencadenar falsos positivos. Al aprovechar la flexibilidad de `Add-MpPreference` puede ajustar Windows Defender para adaptarlo a sus necesidades de seguridad específicas y optimizar su rendimiento.

Proteja el sistema y reduzca los falsos positivos y las interrupciones innecesarias de los análisis mediante las funciones de exclusión de `Add-MpPreference`.

## Revisión de comandos de Defender en 2026

Ejecute los comandos de Defender desde una sesión con privilegios elevados solo cuando la tarea requiera elevación. Revise la ayuda actual del módulo en la versión de Windows de destino antes de usar un parámetro. Registre la configuración existente, cambie un ajuste cada vez, verifique el resultado y anote el comando para revertirlo.

Entre los pasos de revisión útiles se incluyen comprobar el estado de protección, la antigüedad de las firmas, las exclusiones, las preferencias, el historial de análisis y las detecciones recientes. Mantenga las exclusiones acotadas y documente la persona responsable y la fecha de caducidad. Consulte la [documentación del módulo PowerShell de Microsoft Defender](https://learn.microsoft.com/en-us/powershell/module/defender/) y la [documentación de Microsoft Defender Antivirus](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-windows) para conocer los cmdlets y el comportamiento actuales.

## Conclusión

Los comandos PowerShell de Windows Defender proporcionan un **sólido conjunto de herramientas** para administrar y mejorar la seguridad de su sistema Windows. Aprovechando estos comandos, puede *automatizar operaciones de seguridad*, *configurar opciones avanzadas* e incorporar Windows Defender sin problemas a sus flujos de trabajo. Tanto si es un **administrador del sistema** como un **usuario avanzado**, explorar las capacidades de los comandos PowerShell de Windows Defender puede mejorar significativamente la postura de seguridad de su sistema.

Recuerde que un gran poder conlleva una gran responsabilidad. Cuando utilice comandos PowerShell, sea precavido y asegúrese de comprender el impacto de los comandos antes de ejecutarlos. Combinando sus conocimientos con la potencia de los comandos PowerShell de Windows Defender, podrá tomar medidas proactivas para proteger su sistema de las amenazas en evolución.

## Referencias

1. Microsoft Docs - [Cmdlets de Windows Defender en Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. Microsoft Docs - [Introducción a Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
