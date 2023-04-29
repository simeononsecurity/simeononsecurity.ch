---
title: "PowerShell Scripting para principiantes: Guía paso a paso"
draft: false
toc: true
date: 2023-02-25
descripción: "Aprende los conceptos básicos de PowerShell scripting y empieza con la automatización usando esta guía paso a paso."
tags: ["PowerShell", "scripting", "Windows", "automatización", "cmdlets", "módulos", "bucles", "sentencias condicionales", "funciones", "buenas prácticas", "depuración", "pruebas", "variables", "PowerShell ISE", "PowerShell Remoting", "tecnologías Microsoft", "informática", "gestión informática", "codificación", "tareas administrativas"].
cover: "/img/cover/A_cartoon_character_holding_a_script_and_standing.png"
coverAlt: "Un personaje de dibujos animados sosteniendo un script y de pie frente a un ordenador con el prompt de PowerShell, indicando facilidad en el scripting de PowerShell para principiantes"
coverCaption: ""
---
```powershell
Get-Module
```
``powershell
Get-Command -Module <nombre del módulo>
```
``powershell
Get-Help <nombre del cmdlet>
```
``powershell
Obtener alias
```
``powershell
$nombre_variable = valor
```
``powershell
$nombre = "Juan"
```
``powershell
for($i=1; $i -le 5; $i++) {
Write-Host $i
}
```
``powershell
$número = 10
if ($número -gt 5) {
    Write-Host "El número es mayor que 5"
}
```
```powershell
function Añadir-Números {
    param (
        [int]$num1,
        [int]$num2
    )
    $resultado = $num1 + $num2
    devolver $resultado
}

$resultado = Suma-Números -num1 5 -num2 10
Write-Host "El resultado es $resultado"
```
```powershell
   Enable-PSRemoting -Force
```
``powershell
Set-Item wsman:\localhost\Client\TrustedHosts -Value <nombredelordenador> -Force
```
``powershell
Reiniciar servicio WinRM
```
``powershell
Invoke-Command -ComputerName <nombre del equipo> -ScriptBlock { <command> }
```
``powershell
Install-Module <nombre del módulo>
```
``powershell
Get-InstalledModule
```
``powershell
try {
    # algún código que pueda dar error
}
catch {
    Write-Error "Se ha producido un error: $_"
}
```
```powershell
Describe "Mi Script PowerShell" {
    "Hace algo" {
        # algo de código que debería devolver el resultado esperado
        $result = Hace-Algo
        $resultado | Debería -Ser "resultado esperado"
    }
}
```
```powershell
function Get-ProcessCount {
    $procesos = Get-Proceso
    $cuenta = $procesos.Cuenta
    return $cuenta
}

$count = Get-ProcessCount
Write-Host "Hay $count procesos en ejecución".
```
```powershell
param (
    [cadena]$nombre
)

Write-Host "¡Hola, $nombre!"
```
```powershell
function Get-ProcessCount {
    Write-Verbose "Obteniendo procesos..."
    $procesos = Obtener-Procesos
    $cuenta = $procesos.Cuenta
    return $cuenta
}

$count = Get-ProcessCount -Verbose
Write-Host "Hay $count procesos en ejecución".
```

**Aprendizaje de PowerShell para principiantes**
 
 PowerShell es una herramienta de programación de comandos y scripts muy fácil de usar, desarrollada por Microsoft. Ofrece una gran variedad de funciones y parámetros para controlar y automatizar diferentes aspectos de los sistemas de base de datos de Windows y otras tecnologías de Microsoft. En este artículo se describen los fundamentos de PowerShell-Skripterstellung para principiantes y se ofrece una guía de introducción pormenorizada.
 
 ## Introducción a PowerShell
 
 PowerShell es una utilidad de shell que permite al usuario automatizar y controlar el sistema operativo Windows y otras tecnologías de Microsoft. Ofrece una serie de funciones y características que permiten al usuario llevar a cabo distintas tareas de administración, como la gestión de datos y archivos, la configuración de la red y la administración del sistema. PowerShell también cuenta con una interfaz de programación de scripts, con la que el usuario puede crear scripts complejos y automatizar diferentes tareas.
 
 ## Primeros pasos con PowerShell
 
 ### Instalación de PowerShell
 
 PowerShell se instala en la mayoría de las versiones de los sistemas operativos Windows. Si, por el contrario, utiliza una versión diferente de Windows o una versión nueva de PowerShell, puede obtenerla en el sitio web de Microsoft. Siga los siguientes pasos para descargar e instalar PowerShell:
 
 1. Acceda al [Sitio Web de Microsoft PowerShell] (https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2) y seleccione la versión de PowerShell que desea instalar.
 2. 2. Busque los datos de instalación y ejecútelos.
 3. 3. Siga las instrucciones del cuadro de diálogo para completar el proceso de instalación.
 
 ### Inicio de PowerShell
 
 Una vez que haya instalado PowerShell, puede iniciarlo siguiendo estos pasos:
 
 1. 1. Pulse el botón de inicio y seleccione "PowerShell" en la lista.
 2. Selecciona "Windows PowerShell" de la lista de opciones.
 3. PowerShell se abrirá en una nueva ventana.
 
 ### PowerShell-Grundlagen
 
 PowerShell ofrece un conjunto de herramientas de ejecución que permiten a los usuarios interactuar con el sistema operativo. Las funciones de PowerShell se denominan Cmdlets y están organizadas en módulos. Para obtener una lista de los módulos disponibles, utilice el comando Get-Module:
 
 
 Para ver una lista de los Cmdlets disponibles en un módulo, utilice la opción Obtener Comando:
 
 Para obtener ayuda sobre un comando, seleccione Obtener Ayuda:
 
 PowerShell también dispone de Alias, que permiten encontrar los nombres de los Cmdlets. Para ver una lista de las alias disponibles, utilice la opción Obtener Alias:
 
 ### PowerShell-Skripterstellung
 PowerShell-Skripting es una función sencilla que permite al usuario automatizar diferentes tareas de administración. PowerShell-Skripting incluye variables, comandos, configuraciones y funciones, por lo que es una herramienta de automatización muy fácil de usar.
 
 #### Variables
 Las variables se utilizan para especificar datos en los scripts de PowerShell. Las variables en PowerShell comienzan con un símbolo de dólar ($). Utilice la siguiente sintaxis para asignar un valor a una variable:
 Por ejemplo
 #### Schleifen
 Se utiliza para asignar a un bloque de código un número de caracteres diferente. PowerShell soporta los siguientes tipos de descifrado:
 
 - **Por Código**: Para cambiar un bloque de código por un número determinado de mensajes.
 - Durante el juego**: Guarda un Bloqueo de Código, siempre que la configuración sea correcta.
 - Modo de Espera**: Guarda un bloque de código como máximo una vez y luego tanto tiempo como sea necesario para que se cumpla una condición.
 - oCada bucle**: Guarda un bloque de código para cada elemento de una muestra.
   
 El código utilizado puede ser, por ejemplo, una cadena de caracteres, para ajustar los valores de 1 a 5:
 
 #### Anweisungen Bedingte
 
 Especificaciones
 
 Las instrucciones de configuración se utilizan para bloquear el uso de un código, siempre que sea necesaria una configuración diferente. PowerShell soporta los siguientes tipos de configuraciones:
 
 - **Configuración If**: Ayuda a crear un bloque de código cuando una opción es correcta.
 - Contraseña Si-Elsa**: Activa un Bloque de Código si la respuesta es correcta y un Bloque de Código adicional si la respuesta es falsa.
 - Conmutación**: compara un valor con una serie de posibles interacciones y activa un Bloqueo de Código para la primera interacción obtenida.
 
 El siguiente código utiliza, por ejemplo, un valor If para comprobar si un número es mayor que 5:
 
 #### Funciones
 Las funciones son códigos modificables que permiten realizar una tarea determinada. Las funciones proporcionan parámetros de acceso y envían comandos. PowerShell ofrece los siguientes tipos de funciones:
 
 - Bloque de código**: un bloque de código que puede ser definido.
 - Función avanzada**: Una función que contiene metadatos y validación de parámetros.
 
 El código define, por ejemplo, una función a la que se añaden dos valores:
 ### PowerShell-ISE
 PowerShell ISE (Integrated Scripting Environment) es una interfaz gráfica para PowerShell-Skripting. PowerShell ISE ofrece un editor de texto enriquecido, herramientas de depuración y otras funciones que facilitan la escritura y comprobación de scripts PowerShell. Siga los siguientes pasos para configurar PowerShell ISE:
 
 1. Haga clic en el botón de inicio y seleccione "PowerShell ISE" en la lista.
 2. 2. Seleccione "Windows PowerShell ISE" de la lista de opciones.
 3. PowerShell ISE aparecerá en una nueva ventana.
 
 ### PowerShell-Remoting
 PowerShell Remoting permite a los usuarios utilizar funciones y scripts de PowerShell en equipos remotos. PowerShell Remoting permite que el WinRM-Dienst se ejecute tanto en el ordenador local como en el remoto. Sigue los siguientes pasos para activar PowerShell Remoting:
 
 1. 1. Ejecute una orden de acceso PowerShell con permisos de administrador.
 2. Siga los siguientes pasos para activar PowerShell Remoting:
 3. 3. Seleccione el siguiente campo para añadir el equipo remoto a la lista de servidores de confianza:
 4. Inicia WinRM-Dienst de nuevo
 
 Para obtener un error de PowerShell en un equipo remoto, utilice el comando Invocar comando:
 ### Módulo PowerShell
 Los módulos de PowerShell son conjuntos de Cmdlets, funciones y scripts que se han desarrollado para realizar tareas específicas. Los módulos PowerShell pueden instalarse y administrarse a través de la Galería PowerShell, un repositorio central de módulos PowerShell.
 
 Siga estos pasos para instalar un módulo PowerShell de la Galería PowerShell:
 
 Para ver una lista de los módulos PowerShell instalados, utilice el comando Get-InstalledModule:
 
 ### Best Practices für PowerShell-Skripterstellung
 Cuando se escriben scripts de PowerShell, es importante seguir las mejores prácticas para garantizar que los scripts son seguros, fiables y compatibles. Estas son algunas de las mejores prácticas que debe tener en cuenta:
 
 Utilice Variables de Seguridad SIE: Use SIE Variablennamen, sterben ihren Zweck klar angeben.
 Kommentare verwenden: Use SIE SIE Kommentare, um den Zweck des Codes zu erklären.
 - Utilizar el control de errores**: Utilice la Gestión de Errores Sterben para controlar los errores y las anomalías con regularidad.
 - Comprobar los scripts de forma periódica**: Pruebe los scripts para asegurarse de que funcionan correctamente.
 - Utilización de funciones y módulos**: Utilice funciones y módulos para organizar el código y mejorar la seguridad del servidor.
 - Utilizar código fuente**: Añade los archivos codificados en el script y utiliza parámetros o variables.
 - Utilizar la versión completa**: Utilice la versión completa para obtener información adicional sobre el funcionamiento del script.
 
 ### Aplicación de las mejores prácticas para PowerShell-Scripting
 
 #### Verificación de errores
 La gestión de errores es un aspecto crítico de la solución de scripts de PowerShell, ya que asegura que los errores y las anomalías del script sean manejados correctamente. PowerShell ofrece varias posibilidades para el control de errores, como por ejemplo el ajuste Try-Catch, el ajuste Trap y los parámetros ErrorAction. El parámetro Try-Catch WIRD para la detección y el control de errores se utiliza, mientras que el parámetro Trap para la detección y el control de errores se utiliza WIRD. El parámetro ErrorAction-Parameter WIRD se utiliza para controlar el estado del script con errores.
 
 Este es un ejemplo de cómo usar el parámetro Try-Catch para controlar un error:
 
 #### Skripte gründlich testen
 
 Es imprescindible probar los scripts de PowerShell para garantizar que funcionan correctamente. PowerShell ofrece varias herramientas de prueba y marcos de trabajo como Pester, con los que los usuarios pueden crear y realizar pruebas para sus scripts. Estas herramientas ayudan a identificar y aislar problemas en el código y a garantizar que el script cumple los requisitos deseados.
 
 Este es un ejemplo del uso de Pester para probar un script PowerShell:
 
 #### Funciones y módulos utilizados
 Las funciones y los módulos son imprescindibles para organizar el código y mejorar la capacidad de almacenamiento de los scripts de PowerShell. Las funciones permiten a los usuarios agrupar el código en diferentes bloques, mientras que los módulos permiten a los usuarios empaquetar el código y combinarlo con otros. Mediante el uso de funciones y módulos, los flujos de trabajo de PowerShell pueden ser más modulares, eficaces y prácticos.
 
 Este es un ejemplo del uso de una función en PowerShell:
 
 #### Hartcodierte Werte vermeiden
 La codificación de valores en un script de PowerShell lo hace menos flexible y más difícil de usar. En lugar de codificar las órdenes con facilidad, utilice parámetros o variables, lo que permitirá a los usuarios superar el tiempo de espera de las órdenes en el script. Mediante el uso de Parámetros o Variables se puede mejorar el funcionamiento del Skript y adaptarlo a configuraciones diferentes.
 
 Este es un ejemplo del uso de parámetros en PowerShell:
 
 #### Ver la versión completa
 La versión completa proporciona información adicional sobre la ejecución de los scripts, que puede ser útil para la depuración y la detección de errores. PowerShell proporciona el comando Write-Verbose, con el que el usuario puede obtener información adicional en la consola. Mediante el uso de una versión actualizada, los scripts de PowerShell pueden ser más informativos y fáciles de depurar.
 
 Este es un ejemplo del uso de la versión actualizada de PowerShell:
 
 ### Zehn Powershell-Skript-Ideen für Anfänger
 
 - Seguridad automatizada**: Cree un script que automatice el procesamiento de los datos y las descripciones de seguridad más importantes en una plataforma externa o en un servidor de seguridad en la nube.
 - Gestión de dates**: Elabore una hoja de cálculo para organizar los datos y las fichas, y ordénelos en función de la date, el tamaño u otros criterios.
 - Información del sistema**: Escribe una hoja de cálculo que muestre la información del sistema, como la duración de la CPU y del procesador, la posición del procesador y las conexiones de red, en un formato ligeramente reducido.
 - Gestión de usuarios**: Instale un script para automatizar el acceso, la gestión o el cierre de usuarios y grupos en el sistema de base de datos de Windows.
 - Instalación del software**: Instala y configura el software en varios ordenadores al mismo tiempo, ahorrando tiempo y dinero.
 - Configuración de la red**: Instale un script que automatiza el proceso de configuración de redes tales como direcciones IP, subredes y puertas de enlace estándar.
 - Seguridad**: Cree una hoja de cálculo que compruebe la seguridad y advierta al usuario cuando se realicen cambios.
 - Planificación del trabajo**: Crea un programa que planifica y automatiza tareas como copias de seguridad, actualizaciones y escaneos del sistema.
 - Manipulación de registros**: Cree un script para cambiar o eliminar las respuestas de registro de cualquier tabla o archivo.
 - Gestión de residuos**: Instale un script que permita la administración remota de ordenadores Windows, de forma que se puedan configurar los parámetros de usuario y los permisos en ordenadores remotos.
 
 ## Inicio
 
 PowerShell es una herramienta muy útil para controlar y automatizar los sistemas de base de datos de Windows y otras tecnologías de Microsoft. En este artículo se explican los fundamentos de la programación de PowerShell para principiantes, incluyendo la instalación e inicio de PowerShell, el uso de Cmdlets, variables, comandos, configuraciones básicas y funciones, así como el uso de PowerShell ISE, PowerShell Remoting y módulos de PowerShell. Gracias a los métodos más avanzados, los scripts de PowerShell pueden ser más seguros, fiables y seguros. Con un poco de Übung, puede utilizar PowerShell-Skripting y automatizar diferentes tareas de administración.
