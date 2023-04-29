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

**Aprendizaje de scripts PowerShell para principiantes **
 
 PowerShell es un potente shell de línea de comandos y un lenguaje de script desarrollado por Microsoft. Ofrece una amplia gama de comandos y funcionalidades para gestionar y automatizar diversos aspectos del sistema operativo Windows y otras tecnologías de Microsoft. En este artículo, cubrimos las bases de los scripts PowerShell para los principiantes y proporcionamos una guía paso a paso para empezar.
 
 ## Presentación de PowerShell
 
 PowerShell es una shell de línea de comandos que permite a los usuarios automatizar y gestionar el sistema de explotación Windows y otras tecnologías Microsoft. Ofrece un conjunto completo de comandos y funciones que permiten a los usuarios realizar diversas tareas administrativas, como la gestión de archivos y registros, la configuración de redes y la gestión del sistema. PowerShell también incluye un lenguaje de script que permite a los usuarios crear scripts complejos y automatizar diversas tareas repetitivas.
 
 ## Primer paso con PowerShell
 
 ### Instalación de PowerShell
 
 PowerShell está preinstalado en la mayoría de las versiones del sistema operativo Windows. Sin embargo, si utiliza una versión antigua de Windows o si necesita una versión más reciente de PowerShell, puede descargarla desde el sitio web de Microsoft. Para descargar e instalar PowerShell, siga estos pasos :
 
 1. Accede al [sitio web de Microsoft PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2) y selecciona la versión de PowerShell que deseas instalar.
 2. 2. Descarga el archivo de instalación y actualízalo.
 3. Siga las instrucciones de la pantalla para finalizar el proceso de instalación.
 
 ### Despliegue de PowerShell
 
 Una vez que haya instalado PowerShell, puede continuar siguiendo estos pasos:
 
 1. 1. Haga clic en el menú desplegable y seleccione "PowerShell" en la barra de búsqueda.
 2. 2. Selecciona "Windows PowerShell" en los resultados de la búsqueda.
 3. PowerShell se abrirá en una nueva ventana.
 
 ### Principios básicos de PowerShell
 
 PowerShell proporciona una interfaz de línea de comandos que permite a los usuarios interactuar con el sistema de explotación. Los comandos de PowerShell se denominan applets de comando y están organizados en módulos. Para obtener una lista de los módulos disponibles, utilice el comando Get-Module :
 
 
 Para obtener una lista de los applets de comandos disponibles en un módulo, utilice el comando Get-Command :
 
 Para obtener ayuda sobre un applet de comando, utilice el comando Get-Help :
 
 PowerShell también tiene en cuenta los alias, que son los nombres y las rutas de las aplicaciones de comandos. Para ver la lista de alias disponibles, utilice el comando Get-Alias :
 
 ### Script PowerShell
 Los scripts PowerShell son una potente funcionalidad que permite a los usuarios automatizar diversas tareas administrativas. Los scripts PowerShell se encargan de las variables, los campos, las instrucciones condicionales y las funciones, lo que los convierte en una poderosa herramienta de automatización.
 
 #### Variables
 Las variables se utilizan para almacenar datos en los scripts PowerShell. Las variables en PowerShell comienzan con el símbolo dólar ($). Para asignar un valor a una variable, utilice la sintaxis siguiente :
 Por ejemplo
 #### Bolas
 Los bucles se utilizan para repetir un bloque de código un cierto número de veces. PowerShell utiliza los siguientes tipos de bucle:
 
 - Bucle For** : repite un bloque de código un cierto número de veces.
 - Ciclo Mientras**: repite un bloque de código mientras se cumpla una condición.
 - Bucle Do-While** : traduce un bloque de código al menos una vez, después de que se cumpla una condición.
 - Bucle orEach** : traduce un bloque de código para cada elemento de una colección.
   
 Por ejemplo, el siguiente código utiliza un círculo For para imprimir los números del 1 al 5 :
 
 #### Expresiones condicionales
 
 Expresiones condicionales
 
 Las instrucciones condicionales se utilizan para ejecutar un bloque de código si se cumple cierta condición. PowerShell utiliza los siguientes tipos de instrucciones condicionales:
 
 - Instrucción If**: ejecuta un bloque de código si se cumple una condición.
 - Instrucción If-Else**: ejecuta un bloque de código si una condición es verdadera, y otro bloque de código si la condición es falsa.
 - Instrucción Switch** : compara un valor con un conjunto de posibles correspondencias y ejecuta un bloque de código para la primera correspondencia encontrada.
 
 Por ejemplo, el código siguiente utiliza una instrucción If para comprobar si un número es superior a 5 :
 
 #### Las funciones
 Las funciones son bloques de código reutilizables que ejecutan una tarea específica. Las funciones tienen en cuenta los parámetros de entrada y devuelven los valores de salida. PowerShell utiliza los siguientes tipos de funciones:
 
 - Bloque de script**: un bloque de código que se puede ejecutar.
 - **Función avanzada**: una función que incluye la validación de parámetros avanzados.
 
 Por ejemplo, el código siguiente define una función que se añade a dos nombres :
 ### PowerShell ISE
 PowerShell ISE (Integrated Scripting Environment) es una interfaz gráfica de usuario para scripts PowerShell. PowerShell ISE proporciona un editor de texto enriquecido, herramientas de inicio de sesión y otras funciones que modifican la escritura y las pruebas de los scripts PowerShell. Para ejecutar PowerShell ISE, siga estos pasos:
 
 1. Haga clic en el menú desplegable y seleccione "PowerShell ISE" en la barra de búsqueda.
 2. 2. Seleccione "Windows PowerShell ISE" en los resultados de la búsqueda.
 3. PowerShell ISE se abrirá en una nueva ventana.
 
 ### Acceso a distancia PowerShell
 PowerShell Remoting permite a los usuarios ejecutar comandos y scripts PowerShell en ordenadores remotos. PowerShell Remoting requiere que el servicio WinRM se ejecute en ordenadores locales y remotos. Para activar PowerShell Remoting, sigue estos pasos:
 
 1. Abre una invitación PowerShell con privilegios de administrador.
 2. 2. Ejecute el siguiente comando para activar PowerShell Remoting :
 3. 3. Ejecute el siguiente comando para agregar el ordenador remoto a la lista de TrustedHosts :
 4. Restablecer el servicio WinRM
 
 Para ejecutar un comando PowerShell en un equipo remoto, utilice el applet de comando Invoke-Command :
 ###Módulos PowerShell
 Los módulos PowerShell son colecciones de applets de comandos, funciones y scripts diseñados para realizar tareas específicas. Los módulos PowerShell pueden instalarse y ejecutarse con la ayuda de la Galería PowerShell, que es una referencia central para los módulos PowerShell.
 
 Para instalar un módulo PowerShell desde la Galería PowerShell, utilice el siguiente comando :
 
 Para ver la lista de módulos PowerShell activados, utilice el comando Get-InstalledModule :
 
 ### Mejores prácticas para los scripts PowerShell
 Durante la escritura de scripts PowerShell, es importante seguir las mejores prácticas para asegurarse de que los scripts son seguros, fiables y mantenibles. Estas son algunas buenas prácticas que debes tener en cuenta:
 
 Utiliza nombres de variables descriptivos: Utiliza nombres de variables que indiquen claramente su objetivo.
 Utiliza comentarios: Utiliza comentarios para explicar el objetivo del código.
 - ** : Utilizar la gestión de errores** Utiliza la gestión de errores para gestionar correctamente los errores y las excepciones.
 - **Prueba cuidadosamente los scripts**: prueba cuidadosamente los scripts para asegurarte de que funcionan como es debido.
 - Utiliza funciones y módulos**: utiliza funciones y módulos para organizar el código y mejorar su uso.
 - **Evita los valores de codificación en tiempo real**: evita los valores de codificación en tiempo real en el script y utiliza en su lugar parámetros o variables.
 - Utilizar una salida de arranque**: utiliza una salida de arranque para proporcionar información adicional sobre el progreso del script.
 
 ### Élaboration des meilleures pratiques pour les scripts PowerShell
 
 #### Utilizar la gestión de errores
 La gestión de errores es un aspecto esencial de los scripts PowerShell, ya que garantiza que el script gestiona correctamente los errores y las excepciones. PowerShell propone varias formas de gestionar los errores, incluyendo la instrucción Try-Catch, la instrucción Trap y el parámetro ErrorAction. La instrucción Try-Catch se utiliza para interceptar y gestionar las excepciones, mientras que la instrucción Trap se utiliza para interceptar y gestionar los errores. El parámetro ErrorAction se utiliza para controlar la forma en que el script gestiona los errores.
 
 Vea un ejemplo de uso de la instrucción Try-Catch para corregir un error:
 
 #### Compruebe correctamente los scripts
 
 Es esencial probar los scripts PowerShell para asegurarse de que funcionan como se espera. PowerShell proporciona varias herramientas y marcos de pruebas, como Pester, que permiten a los usuarios escribir y ejecutar pruebas para sus scripts. Estas herramientas permiten identificar y aislar los problemas en el código y garantizar que el script responde a las exigencias requeridas.
 
 Vea un ejemplo de uso de Pester para probar un script PowerShell :
 
 #### Utilizar las funciones y los módulos
 Las funciones y los módulos son esenciales para organizar el código y mejorar la usabilidad de los scripts PowerShell. Las funciones permiten a los usuarios agrupar el código en bloques reutilizables, mientras que los módulos permiten a los usuarios acondicionar y compartir el código con otros. Mediante el uso de funciones y módulos, los scripts PowerShell pueden hacerse más modulares, eficaces y duraderos.
 
 Vea un ejemplo de uso de una función en PowerShell :
 
 #### Evitar que los valores de codificación se pierdan
 Los valores de codificación en tiempo real en un script PowerShell son los menos flexibles y los más difíciles de mantener. En lugar de codificar los valores en tiempo real, es preferible utilizar parámetros o variables que permitan a los usuarios transmitir los valores al script durante la ejecución. Al utilizar parámetros o variables, el script puede ser más reutilizable y adaptable a condiciones cambiantes.
 
 Vea un ejemplo de uso de un parámetro en PowerShell :
 
 #### Utilizar una salida eliminada
 La salida finalizada proporciona información adicional sobre el progreso del script, lo que puede ser útil para la desconexión y la desconexión. PowerShell proporciona el applet de comando Write-Verbose, que permite a los usuarios producir información detallada en la consola. Utilizando una salida de descarga, los scripts PowerShell pueden ser más informativos y fáciles de descargar.
 
 Vea un ejemplo de uso de una salida descargada en PowerShell :
 
 ### Dix idées de script Powershell pour les principiants
 
 - Salvaguardas automáticas**: crea un script que automatice el proceso de salvaguarda de archivos y carpetas importantes en un disco duro externo o en un servicio de almacenamiento en la nube.
 - Gestión de archivos**: crea un script que organiza los archivos y las copias de seguridad y los triplica en diferentes carpetas en función del tipo de archivo, su tamaño u otros criterios.
 - Sistema de información**: crea un script que recupere la información del sistema, como el uso del procesador y de la memoria, el espacio de disco y los parámetros de red, y los informes en un formato fácil de leer.
 - Gestión de usuarios**: crea un script que automatiza el proceso de añadir, modificar o eliminar usuarios y grupos en el sistema operativo Windows.
 - Instalación de software**: crea un script que instale y configure el software en varios ordenadores a la vez, lo que te permitirá ahorrar tiempo y esfuerzo.
 - Configuración de red**: crea un script que automatiza el proceso de configuración de los parámetros de red, tales como la dirección IP, la máscara de subred y la contraseña por defecto.
 - Seguridad**: cree un script que audite y vigile los parámetros de seguridad y avise al usuario si se detectan modificaciones.
 - **Planificación de tareas** crea un script que planifica y automatiza las tareas: actuales, como las salvaguardas, las puestas al día y los análisis del sistema.
 - Manipulación del registro**: cree un script que modifique o recupere los valores del registro para claves o valores específicos.
 - Administración a distancia** : crea un script que permite la administración a distancia de ordenadores Windows, permitiendo a los usuarios ejecutar comandos y scripts en máquinas distantes.
 
 ## Conclusión
 
 PowerShell es una potente herramienta para gestionar y automatizar el sistema de explotación de Windows y otras tecnologías Microsoft. En este artículo, hemos descrito las bases de los scripts PowerShell para los principiantes, incluyendo la instalación y configuración de PowerShell, el uso de applets de comando, variables, bucles, instrucciones condicionales y funciones, y el uso de los módulos PowerShell ISE, PowerShell Remoting y PowerShell. Siguiendo las mejores prácticas, los scripts PowerShell pueden ser seguros, fiables y mantenibles. Con la práctica, podrá dominar los scripts PowerShell y automatizar fácilmente diversas tareas administrativas.
