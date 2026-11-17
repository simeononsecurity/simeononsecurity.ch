---
title: "Crear un inventario de Active Directory de solo lectura con PowerShell"
date: 2026-10-10
lastmod: 2026-11-08
toc: true
draft: false
description: "Inventaría unidades organizativas, usuarios y equipos de Active Directory con consultas de PowerShell delimitadas. Exporta archivos CSV verificables sin cambiar objetos del directorio."
genre: ["Active Directory", "PowerShell", "Administración de sistemas"]
tags: ["Inventario de Active Directory", "Inventario de AD con PowerShell", "Get-ADUser", "Get-ADComputer", "Get-ADOrganizationalUnit", "Get-ADDomain", "SearchBase", "AD de solo lectura", "Exportación de usuarios de AD", "Exportación de equipos de AD", "Exportación de OU de AD", "Export-Csv", "RSAT", "Auditoría de directorio", "Informes de AD", "Inventario de OU", "Windows Server", "Script de PowerShell", "Módulo de AD", "Higiene del directorio"]
cover: "/img/cover/active-directory-powershell-read-only-inventory.webp"
coverAlt: "Un árbol de Active Directory del que salen registros de usuarios, equipos y unidades organizativas hacia tres archivos de revisión."
coverCaption: "Delimita la consulta y exporta solo los campos que necesitas revisar."
---
La limpieza de Active Directory empieza con una lista fiable de los objetos existentes. Este **inventario de solo lectura** reúne unidades organizativas, usuarios y equipos de un ámbito elegido. Exporta tres archivos CSV (valores separados por comas) para revisar sin cambiar objetos del directorio. Aun así, protege esos archivos porque los nombres y los detalles de los dispositivos revelan parte de tu entorno.

<!--more-->

## Puntos clave

- **Elige el ámbito:** consulta una unidad organizativa antes de ampliar la búsqueda a todo el dominio.
- **Usa comandos de lectura:** `Get-ADOrganizationalUnit`, `Get-ADUser` y `Get-ADComputer` recuperan objetos.
- **Selecciona los campos:** exporta solo las propiedades necesarias para la tarea.
- **Revisa el resultado:** compara el recuento y algunas filas de muestra antes de confiar en el informe.

## Antes de empezar

Necesitas un equipo de administración Windows con DNS funcional y acceso de red a un controlador de dominio, el módulo de PowerShell **ActiveDirectory**, una cuenta autorizada para leer los objetos seleccionados y una carpeta protegida para los archivos CSV. En un cliente Windows, el módulo forma parte de las herramientas de Active Directory de Remote Server Administration Tools (RSAT). La [guía del módulo de Active Directory](/articles/active-directory-module-powershell-installation-usage-guide/) explica la instalación. Microsoft publica la [referencia de cmdlets](https://learn.microsoft.com/en-us/powershell/module/activedirectory/) del módulo y las [opciones de instalación de RSAT](https://learn.microsoft.com/windows-server/remote/remote-server-administration-tools). Esta guía usa la sintaxis de Windows PowerShell y no cambia objetos del directorio.

Los permisos del directorio siguen aplicándose. Microsoft explica en su [guía sobre cuentas con privilegios](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory) que las listas de control de acceso suelen permitir que los usuarios autenticados lean información general y restringir los campos confidenciales y los cambios. Empieza con una cuenta aprobada y una OU de prueba. No eleves los permisos a Domain Admin para que el inventario funcione.

> **Advertencia:** los archivos CSV contienen nombres de cuentas y equipos. Guárdalos en una ubicación aprobada, limita el acceso y elimina las copias adicionales después de la revisión. No publiques una exportación sin filtrar ni la adjuntes a un issue público.

## Elegir la base de búsqueda

Una **unidad organizativa (OU)** agrupa objetos del directorio. Su **nombre distinguido (DN)** indica su posición en el árbol del directorio. El parámetro `-SearchBase` limita la consulta a un DN elegido. Sin un ámbito deliberado, un filtro amplio podría devolver muchos más objetos de los que necesitas revisar.

Primero carga el módulo y consulta el DN del dominio actual:

```powershell
Import-Module ActiveDirectory
(Get-ADDomain).DistinguishedName
```

Microsoft documenta [Get-ADDomain](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-addomain) y la información del dominio que devuelve el cmdlet. Busca la OU que quieras revisar antes de establecer la base de búsqueda:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase (Get-ADDomain).DistinguishedName |
    Select-Object Name, DistinguishedName
```

Copia el DN exacto del resultado. En los ejemplos siguientes, sustituye este valor de documentación por el DN de tu OU:

```powershell
$SearchBase = 'OU=Lab,DC=example,DC=com'
```

`example.com` es un dominio de documentación. No copies su DN en una consulta real. Si necesitas inventariar todo el dominio de forma intencionada, asigna el DN del dominio a `$SearchBase` y registra ese ámbito más amplio en el informe. La [referencia de Get-ADOrganizationalUnit](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit) de Microsoft documenta `-Filter` y `-SearchBase`.

## Inventariar OU, usuarios y equipos

Empieza con los recuentos de objetos. Así podrás detectar rápidamente una base de búsqueda incorrecta o un resultado vacío inesperado:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADUser -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADComputer -Filter * -SearchBase $SearchBase | Measure-Object
```

`-Filter *` recupera todos los objetos que coinciden dentro de la base de búsqueda. Microsoft documenta [Get-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser) y [Get-ADComputer](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) como comandos de recuperación. Un recuento de cero podría ser correcto, pero revisa el DN, los permisos y el dominio de destino antes de considerar completo el inventario.

Ahora muestra algunas filas en la consola. Guarda los campos seleccionados para que la vista previa y la exportación CSV posterior usen las mismas columnas:

```powershell
$UserFields = 'Name', 'SamAccountName', 'Enabled', 'DistinguishedName'
Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields -First 10
```

Para los equipos, solicita la propiedad adicional del sistema operativo solo si la necesitas para la revisión:

```powershell
$ComputerFields = @(
    'Name', 'DNSHostName', 'OperatingSystem',
    'Enabled', 'DistinguishedName'
)
Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields -First 10
```

El parámetro `-Properties` solicita propiedades que no forman parte del conjunto predeterminado del cmdlet. Microsoft lo explica en la [referencia del cmdlet de equipos](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer). Trata los nombres de los sistemas operativos como datos del directorio, no como prueba de la versión instalada actualmente. Un objeto de equipo puede estar obsoleto o su atributo puede no haberse actualizado.

## Exportar archivos CSV verificables

Elige una carpeta de salida aprobada con espacio suficiente. Los comandos siguientes escriben **archivos CSV locales** y no cambian objetos del directorio. Ejecútalos en esa carpeta. `-NoClobber` impide sobrescribir archivos existentes. Usa una carpeta o un nombre de archivo nuevo en cada ejecución.

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase |
    Select-Object Name, DistinguishedName |
    Export-Csv -Path .\ad-ous.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields |
    Export-Csv -Path .\ad-users.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields |
    Export-Csv -Path .\ad-computers.csv -NoTypeInformation -Encoding UTF8 -NoClobber
```

La [referencia de Export-Csv](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv?view=powershell-5.1) de Microsoft explica `-NoTypeInformation`, `-Encoding` y `-NoClobber`. Abre cada archivo CSV en un editor de texto o una hoja de cálculo aprobada. Comprueba el encabezado, algunas filas y el número de registros frente al recuento anterior. Un comando fallido o un archivo de cero bytes no demuestra que el informe esté completo.

> **Resultado esperado:** tienes tres archivos CSV con registros de OU, usuarios y equipos del ámbito elegido. El número de filas y los valores de muestra coinciden con el ámbito seleccionado del directorio.

## Revisar sin cambiar objetos

Usa el inventario para responder preguntas concretas: ¿qué OU corresponde a un equipo?, ¿qué cuentas de usuario están deshabilitadas?, ¿qué nombres de dispositivos necesitan un propietario? Anota los hallazgos en una nota de revisión separada. No interpretes el valor `Enabled` como prueba de que una cuenta sigue siendo necesaria. No elimines ni deshabilites objetos basándote solo en una exportación.

En los informes recurrentes, registra la fecha de la consulta, el dominio, el DN de la OU, las propiedades seleccionadas, el operador y la ubicación del CSV. Si comparas dos exportaciones, confirma que ambas usaron el mismo ámbito y los mismos campos. De lo contrario, la diferencia podría deberse a la consulta y no a un cambio real del directorio.

Esto es un **inventario**, no una auditoría de cuentas con privilegios ni un informe de actividad de inicio de sesión. Microsoft señala que las propiedades y los permisos de Active Directory varían según el objeto y el entorno. Verifica con el responsable del sistema un atributo del sistema operativo o un nombre para mostrar antes de actuar. La [guía de seguridad de Active Directory](/articles/active-directory-security-best-practices/) trata controles de seguridad más amplios.

## Solución de problemas

- **El módulo no se importa:** confirma que las herramientas de Active Directory de RSAT o las herramientas de administración de Windows Server estén instaladas en el equipo. Sigue la [guía de configuración del módulo](/articles/active-directory-module-powershell-installation-usage-guide/).
- **La consulta no devuelve objetos:** comprueba el DN exacto, el dominio actual, el contenido de la OU y los permisos de lectura. Prueba primero con una OU pequeña conocida antes de ampliar el ámbito.
- **Una propiedad aparece vacía:** confirma que el atributo existe y que tu cuenta puede leerlo. No rellenes los campos que faltan con suposiciones.
- **La exportación indica que el archivo ya existe:** `-NoClobber` protegió el informe anterior. Elige otro nombre de archivo o carpeta y vuelve a ejecutar el comando.
- **El recuento difiere de lo esperado:** comprueba si los usuarios o equipos están en otra OU, si cambió el ámbito y si el directorio cambió durante la consulta.

## Próximos pasos

Guarda los archivos CSV sin filtrar en una ubicación protegida durante el periodo de revisión acordado. Comparte solo los campos que necesita el revisor. Cuando los responsables confirmen los hallazgos, planifica los cambios según tu proceso habitual de aprobación y reversión. Después de los cambios aprobados, repite el mismo inventario con el mismo ámbito para confirmar el resultado.