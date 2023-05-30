---
title: "Automatice OSINT con los módulos PowerShell de Shodan"
date: 2020-11-14
---

Una colección de módulos PowerShell para interactuar con la API de Shodan

**Notas
- Necesitarás tu clave de la API de Shodan, que puedes encontrar en tu carpeta [Shodan Account](https://account.shodan.io/)
- Puede encontrar ejemplos de las API utilizadas en los módulos en la página [Shodan Developers Page](https://developer.shodan.io/api)
- Algunos módulos pueden utilizar créditos de escaneo o de consulta Los créditos de consulta se utilizan cuando se descargan datos a través del sitio web, CLI o API (lo que hacen estos scripts).
  Dado que estamos utilizando la API es importante tener en cuenta que los créditos de consulta se deducen si:
  1.  1. Se utiliza un filtro de búsqueda
  2.  Se solicita la página 2 o superior
      Los créditos se renuevan a principios de mes y 1 crédito te permite descargar 100 resultados.
      En cuanto a los créditos de escaneado, 1 crédito de escaneado le permite escanear 1 IP, y también se renuevan a principios de mes.
      Consulte el Centro de ayuda Shodan [HERE](https://help.shodan.io/the-basics/credit-types-explained) para más detalles.

## Índice
- [Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
- [Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- **Módulos**
  - [Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo) - Devuelve información sobre el plan API perteneciente a la clave API dada.
  - [Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders) - Muestra las cabeceras HTTP que su cliente envía cuando se conecta a un servidor web.
  - [Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP) - Obtiene tu dirección IP actual vista desde Internet.
  - [Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain) - Obtiene todos los subdominios y otras entradas DNS para el dominio dado
  - [Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  - [Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse) - Busca los nombres de host que se han definido para la lista dada de direcciones IP.
  - [Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount) - Busca exploits pero sólo devuelve información sobre el número total de coincidencias relacionadas con el término de búsqueda y, opcionalmente, el autor, la plataforma, el puerto, la fuente o el tipo de exploit.
  - [Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  - [Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount) - Devuelve el número total de resultados de "/shodan/host/search" proporciona.
  - [Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP) - Busca en Shodan con la dirección IP.
  - [Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch) - Busque en Shodan utilizando la misma sintaxis de consulta que en el sitio web y utilice facetas para obtener información resumida de diferentes propiedades.
  - [Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets) - Este módulo devuelve una lista de filtros de búsqueda que pueden utilizarse en la consulta de búsqueda.
  - [Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters) - Este módulo devuelve una lista de filtros de búsqueda que pueden utilizarse en la consulta de búsqueda.
  - [Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts) - Lista todos los puertos que Shodan está rastreando en Internet.
  - [Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile) - Devuelve información sobre la cuenta Shodan vinculada a esta clave API
  - [Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID) - Comprobar el progreso de una solicitud de exploración enviada previamente
  - [Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols) - Enumere todos los protocolos que pueden utilizarse al realizar exploraciones de Internet a petición a través de Shodan.
  - [Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP) - Utilice este módulo para solicitar a Shodan que rastree una red.

<a name="Descargar"></a>

## Descargar

Necesitarás clonar o descargar los scripts a tu ordenador.

Puede utilizar el menú desplegable Código en esta página repo desplazándose hacia arriba, o simplemente copiar y pegar el siguiente enlace: [https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

¡![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

Para este ejemplo vamos a clonar el repositorio dentro de Git Bash, después de hacer clic en el icono del portapapeles como se ve arriba, podemos escribir git clone y hacer clic derecho en la ventana de Git Bash para seleccionar pegar en el menú desplegable:

```
exampleuser@exampleComputer MINGW64 ~/Documents/Github git clone https://github.com/simeononsecurity/Shodan_PS.git
```

Para obtener instrucciones detalladas sobre la clonación, consulte [the github documentation.](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

Una vez que tenga los archivos, es necesario copiar los archivos a C: Archivos de programa de Windows PowerShell Módulos, haciendo esto se mostrará un diálogo diciendo que el acceso está denegado, haga clic en continuar para terminar de copiar los archivos a esta ubicación y, a continuación, proceder a las instrucciones de instalación [here](#Install)

¡![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

**OR**

Puede utilizar el menú desplegable Código en esta página repo desplazándose hacia arriba, o simplemente haga clic en el siguiente enlace:
[https://github.com/simeononsecurity/Shodan_PS/archive/main.zip](https://github.com/simeononsecurity/Shodan_PS/archive/main.zip)
¡![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select Download Zip option](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/downloadzip.gif?raw=true)

Descomprime main.zip haciendo clic con el botón derecho del ratón sobre el archivo y seleccionando extraer aquí en el menú desplegable.

Una vez que tenga los archivos, es necesario copiar los archivos a C: Archivos de programa de Windows PowerShell Módulos, haciendo esto se mostrará un diálogo diciendo que el acceso está denegado, haga clic en continuar para terminar de copiar los archivos a esta ubicación y, a continuación, proceder a las instrucciones de instalación. [here](#Install)

¡![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

# Instalar

<a name="Instalar"></a>

Para instalar los módulos Deberá ejecutar una ventana de PowerShell como administrador.
Hay dos formas de hacerlo:

La primera forma es haciendo clic derecho en el icono de PowerShell en el Escritorio y seleccionando Ejecutar como Administrador en el menú desplegable.

¡![Right click the powershell icon on the Desktop and select run as administrator from dropdown menu](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/RcRunAsAdmin.gif?raw=true)

**OR**

Escribiendo p (o los caracteres que tarde PowerShell en aparecer) en la barra de búsqueda y haciendo clic en Ejecutar como administrador.

¡![type p in the search bar and when powershell comes up click on run as administrator](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/SearchBarRunAsAdmin.gif?raw=true)

Necesitará estar en el directorio en el que copió los scripts.
Ejecute el siguiente comando para cambiar su directorio de trabajo:

```
PS C:\WINDOWS\system32> cd 'C:\Program Files\WindowsPowerShell\Modules\Shodan_PS'
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS>
```

En los equipos cliente Windows debemos cambiar la política de ejecución de PowerShell, que por defecto es Restringida.

Para más información por favor lea esto [Microsoft documentation.](https:/go.microsoft.com/fwlink/?LinkID=135170)

Ejecute el siguiente comando para establecer la política en RemoteSigned e introduzca y para seleccionar que Sí desea cambiar la política.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ExecutionPolicy RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the
security risks described in the about_Execution_Policies help topic at https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to
change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
```

Una vez modificada la política de ejecución, puede ejecutar el siguiente comando para Importar los módulos.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ChildItem -Recurse *.psm1 | Import-Module
```

Ahora puede ejecutar cualquiera de los scripts como un módulo a través de powershell.
