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
**Aprendizaje de secuencias de comandos PowerShell para principiantes**.

PowerShell es un potente shell de línea de comandos y lenguaje de scripting desarrollado por Microsoft. Proporciona una amplia gama de comandos y características para la gestión y automatización de diversos aspectos del sistema operativo Windows y otras tecnologías de Microsoft. En este artículo, cubriremos los conceptos básicos de PowerShell para principiantes y proporcionaremos una guía paso a paso para empezar.

## Introducción a PowerShell

PowerShell es un shell de línea de comandos que permite a los usuarios automatizar y gestionar el sistema operativo Windows y otras tecnologías de Microsoft. Ofrece un amplio conjunto de comandos y funciones que permiten a los usuarios realizar diversas tareas administrativas, como la gestión de archivos y directorios, la configuración de redes y la administración de sistemas. PowerShell también es compatible con un lenguaje de secuencias de comandos que permite a los usuarios crear secuencias de comandos complejas y automatizar diversas tareas repetitivas.

## Introducción a PowerShell

### Instalación de PowerShell

PowerShell viene preinstalado en la mayoría de las versiones del sistema operativo Windows. Sin embargo, si utiliza una versión anterior de Windows o si necesita una versión más reciente de PowerShell, puede descargarla del sitio web de Microsoft. Para descargar e instalar PowerShell, sigue estos pasos:

1. Vaya al [sitio web de Microsoft PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2) y seleccione la versión de PowerShell que desea instalar.
2. Descarga el archivo de instalación y ejecútalo.
3. 3. Siga las instrucciones que aparecen en pantalla para completar el proceso de instalación.

### Inicio de PowerShell

Una vez que haya instalado PowerShell, puede iniciarlo siguiendo estos pasos:

1. 1. Haz clic en el menú Inicio y escribe "PowerShell" en la barra de búsqueda.
2. Selecciona "Windows PowerShell" en los resultados de la búsqueda.
3. PowerShell se abrirá en una nueva ventana.

### Fundamentos de PowerShell

PowerShell proporciona una interfaz de línea de comandos que permite a los usuarios interactuar con el sistema operativo. Los comandos de PowerShell se denominan cmdlets y están organizados en módulos. Para ver una lista de los módulos disponibles, utilice el comando Get-Module:

```powershell
Get-Module
```

Para ver una lista de los cmdlets disponibles en un módulo, utilice el comando Get-Command:
```powershell
Get-Command -Módulo <nombre del módulo>
```

Para obtener ayuda sobre un cmdlet, utilice el comando Get-Help:
```powershell
Get-Help <nombre del cmdlet>
```

PowerShell también admite alias, que son nombres más cortos para los cmdlets. Para ver una lista de los alias disponibles, utilice el comando Get-Alias:
```powershell
Get-Alias
```

### Scripts PowerShell
Los scripts de PowerShell son una potente función que permite a los usuarios automatizar diversas tareas administrativas. Las secuencias de comandos de PowerShell admiten variables, bucles, sentencias condicionales y funciones, lo que las convierte en una potente herramienta de automatización.

#### Variables
Las variables se utilizan para almacenar datos en los scripts de PowerShell. Las variables en PowerShell comienzan con un signo de dólar ($). Para asignar un valor a una variable, utilice la siguiente sintaxis:
``powershell
$nombre_variable = valor
```
Por ejemplo
``powershell
$nombre = "Juan"
```
#### Bucles
Los bucles se utilizan para repetir un bloque de código un cierto número de veces. PowerShell soporta los siguientes tipos de bucles:

- Bucle for**: repite un bloque de código un número determinado de veces.
- Bucle While**: repite un bloque de código mientras se cumpla una condición.
- Bucle Do-While**: repite un bloque de código al menos una vez y después mientras se cumpla una condición.
- Bucle orEach**: repite un bloque de código para cada elemento de una colección.
  
Por ejemplo, el siguiente código utiliza un bucle For para imprimir los números del 1 al 5:
```powershell
for($i=1; $i -le 5; $i++) {
Write-Host $i
}
```

#### Sentencias condicionales

Sentencias condicionales

Las sentencias condicionales se utilizan para ejecutar un bloque de código si una determinada condición es verdadera. PowerShell soporta los siguientes tipos de sentencias condicionales:

- Sentencia If**: ejecuta un bloque de código si una condición es verdadera.
- Sentencia If-Else**: ejecuta un bloque de código si una condición es verdadera, y otro bloque de código si la condición es falsa.
- Sentencia Switch**: compara un valor con un conjunto de posibles coincidencias y ejecuta un bloque de código para la primera coincidencia encontrada.

Por ejemplo, el siguiente código utiliza una sentencia If para comprobar si un número es mayor que 5:

```powershell
$número = 10
if ($número -gt 5) {
    Write-Host "El número es mayor que 5"
}
```
#### Funciones
Las funciones son bloques de código reutilizables que realizan una tarea específica. Las funciones toman parámetros de entrada y devuelven valores de salida. PowerShell soporta los siguientes tipos de funciones:

- **Bloque de script**: un bloque de código que se puede ejecutar.
- **Función avanzada**: una función que incluye metadatos y validación de parámetros.

Por ejemplo, el siguiente código define una función que suma dos números:
```powershell
function Suma-Números {
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
### PowerShell ISE
PowerShell ISE (Integrated Scripting Environment) es una interfaz gráfica de usuario para PowerShell scripting. PowerShell ISE proporciona un editor de texto enriquecido, herramientas de depuración y otras características que facilitan la escritura y prueba de scripts PowerShell. Para abrir PowerShell ISE, siga estos pasos:

1. Haz clic en el menú Inicio y escribe "PowerShell ISE" en la barra de búsqueda.
2. Selecciona "Windows PowerShell ISE" en los resultados de la búsqueda.
3. PowerShell ISE se abrirá en una nueva ventana.

### PowerShell Remoting
PowerShell Remoting permite a los usuarios ejecutar comandos y scripts PowerShell en equipos remotos. PowerShell Remoting requiere que el servicio WinRM se ejecute tanto en el equipo local como en el remoto. Para habilitar PowerShell Remoting, siga estos pasos:

1. 1. Abra una ventana de PowerShell con privilegios de administrador.
2. Ejecute el siguiente comando para habilitar PowerShell Remoting:
```powershell
   Enable-PSRemoting -Force
```
3. 3. Ejecute el siguiente comando para añadir el equipo remoto a la lista TrustedHosts:
``powershell
Set-Item wsman:\localhost\Client\TrustedHosts -Value <nombredelordenador> -Force
```
4. 4. Reinicie el servicio WinRM
``powershell
Reiniciar servicio WinRM
```

Para ejecutar un comando PowerShell en un equipo remoto, utilice el cmdlet Invoke-Command:
```powershell
Invoke-Command -ComputerName <nombre del equipo> -ScriptBlock { <command> }
```
### Módulos PowerShell
Los módulos PowerShell son colecciones de cmdlets, funciones y scripts diseñados para realizar tareas específicas. Los módulos de PowerShell pueden instalarse y administrarse mediante la Galería PowerShell, que es un repositorio central de módulos de PowerShell.

Para instalar un módulo PowerShell desde la Galería PowerShell, utilice el siguiente comando:
```powershell
Install-Module <nombre del módulo>
```

Para ver una lista de los módulos de PowerShell instalados, utilice el comando Get-InstalledModule:
``powershell
Get-InstalledModule
```

### Prácticas recomendadas para la creación de scripts PowerShell
Al escribir scripts PowerShell, es importante seguir las mejores prácticas para garantizar que los scripts sean seguros, fiables y mantenibles. Éstas son algunas de las prácticas recomendadas que debe tener en cuenta:

Utilice nombres de variables descriptivos: Utilice nombres de variables que indiquen claramente su propósito.
Use comments: Utilice comentarios para explicar el propósito del código.
- Utiliza el tratamiento de errores**: Utiliza el tratamiento de errores para gestionar los errores y las excepciones con elegancia.
- Probar a fondo los scripts**: Prueba los scripts a fondo para asegurarte de que funcionan como se espera.
- Utilizar funciones y módulos**: Utilice funciones y módulos para organizar el código y mejorar su reutilización.
- Evitar la codificación rígida de valores**: Evite codificar valores en el script y utilice parámetros o variables en su lugar.
- Utilizar salidas detalladas**: Utiliza la salida detallada para proporcionar información adicional sobre el progreso del script.

### Elaboración de las mejores prácticas para la secuencia de comandos PowerShell

#### Utilizar la gestión de errores
El manejo de errores es un aspecto crítico de los scripts PowerShell, ya que asegura que el script maneja con gracia los errores y excepciones. PowerShell proporciona varias maneras de manejar errores, incluyendo la sentencia Try-Catch, la sentencia Trap y el parámetro ErrorAction. La sentencia Try-Catch se utiliza para capturar y gestionar excepciones, mientras que la sentencia Trap se utiliza para capturar y gestionar errores. El parámetro ErrorAction se utiliza para controlar cómo el script maneja los errores.

Este es un ejemplo del uso de la sentencia Try-Catch para manejar un error:
```powershell
try {
    # algún código que pueda lanzar un error
}
catch {
    Write-Error "Se ha producido un error: $_"
}
```

#### Scripts de prueba a fondo

Probar los scripts de PowerShell es esencial para asegurarse de que funcionan como se espera. PowerShell proporciona varias herramientas y marcos de pruebas, como Pester, que permiten a los usuarios escribir y ejecutar pruebas para sus scripts. Estas herramientas ayudan a identificar y aislar problemas en el código y a garantizar que el script cumple los requisitos deseados.

He aquí un ejemplo de uso de Pester para probar un script PowerShell:
```powershell
Describe "Mi script PowerShell" {
    Hace algo" {
        # algo de código que debería devolver el resultado esperado
        $resultado = Hace-Algo
        $resultado | Debería -Ser "resultado esperado"
    }
}
```

#### Utilizar funciones y módulos
Las funciones y los módulos son esenciales para organizar el código y mejorar su reutilización en los scripts de PowerShell. Las funciones permiten a los usuarios agrupar el código en bloques reutilizables, mientras que los módulos permiten a los usuarios empaquetar y compartir código con otros. Mediante el uso de funciones y módulos, los scripts de PowerShell pueden hacerse más modulares, eficientes y fáciles de mantener.

He aquí un ejemplo de uso de una función en PowerShell:
```powershell
función Get-ProcessCount {
    $procesos = Get-Process
    $cuenta = $procesos.Cuenta
    return $cuenta
}

$cuenta = Get-CuentaProcesos
Write-Host "Hay $cuenta procesos en ejecución".
```

#### Evitar la codificación de valores
La codificación de valores en un script PowerShell lo hace menos flexible y más difícil de mantener. En lugar de codificar valores, es mejor utilizar parámetros o variables, que permiten a los usuarios pasar valores al script en tiempo de ejecución. Mediante el uso de parámetros o variables, el script puede ser más reutilizable y adaptable a las condiciones cambiantes.

He aquí un ejemplo de uso de un parámetro en PowerShell:
```powershell
param (
    [cadena]$nombre
)

Write-Host "¡Hola, $nombre!"
```

#### Utilizar la salida detallada
La salida detallada proporciona información adicional sobre el progreso del script, lo que puede ser útil para depurar y solucionar problemas. PowerShell proporciona el cmdlet Write-Verbose, que permite a los usuarios enviar información detallada a la consola. Al utilizar la salida detallada, los scripts de PowerShell pueden ser más informativos y fáciles de depurar.

A continuación se muestra un ejemplo de uso de la salida detallada en PowerShell:
```powershell
function Get-ProcessCount {
    Write-Verbose "Obteniendo procesos..."
    $procesos = Obtener-Procesos
    $cuenta = $procesos.Cuenta
    return $cuenta
}

$cuenta = Obtener-CuentoDeProcesos -Verbose
Write-Host "Hay $cuenta procesos en ejecución".
```

### Diez ideas de scripts Powershell para principiantes

- Copias de seguridad automatizadas**: Crea un script que automatice el proceso de copia de seguridad de archivos y directorios importantes en un disco duro externo o en un servicio de almacenamiento en la nube.
- Gestión de archivos**: Crear un script que organice archivos y directorios clasificándolos en diferentes carpetas en función del tipo de archivo, tamaño u otros criterios.
- Información del sistema**: Crear un script que recupere información del sistema, como el uso de la CPU y la memoria, el espacio en disco y la configuración de red, y la muestre en un formato fácil de leer.
- Gestión de usuarios**: Crear un script que automatice el proceso de añadir, modificar o eliminar usuarios y grupos en el sistema operativo Windows.
- Instalación de software**: Crear un script que instale y configure software en varios ordenadores a la vez, ahorrando tiempo y esfuerzo.
- Configuración de red**: Crear un script que automatice el proceso de configuración de los parámetros de red, como la dirección IP, la máscara de subred y la puerta de enlace predeterminada.
- Seguridad**: Cree una secuencia de comandos que audite y supervise la configuración de seguridad y avise al usuario si se detecta algún cambio.
- Programación de tareas**: Crear un script que programe y automatice tareas recurrentes, como copias de seguridad, actualizaciones y análisis del sistema.
- Manipulación de registros**: Crear un script que modifique o recupere valores del registro para claves o valores específicos.
- Administración remota**: Crear un script que permita la administración remota de ordenadores Windows, permitiendo a los usuarios ejecutar comandos y scripts en máquinas remotas.

## Conclusión

PowerShell es una potente herramienta para gestionar y automatizar el sistema operativo Windows y otras tecnologías de Microsoft. En este artículo, hemos tratado los aspectos básicos de la creación de scripts de PowerShell para principiantes, incluida la instalación e inicio de PowerShell, el uso de cmdlets, variables, bucles, sentencias condicionales y funciones, y el uso de PowerShell ISE, PowerShell Remoting y módulos de PowerShell. Siguiendo las mejores prácticas, los scripts de PowerShell pueden ser seguros, fiables y fáciles de mantener. Con la práctica, puede llegar a dominar las secuencias de comandos de PowerShell y automatizar varias tareas administrativas con facilidad.
