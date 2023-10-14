---
title: "Automatice el cumplimiento de las STIG de .NET con un script de PowerShell"
date: 2020-08-20
---
 el STIG de .NET Framework

La aplicación de la STIG de .NET no es sencilla. A muchos administradores les puede llevar horas implementarla completamente en un solo sistema. Este script aplica los cambios necesarios en el registro y modifica el archivo machine.config para implementar FIPS y otros controles según sea necesario.

## Notas:

Este script no puede y no conseguirá nunca que el .NET stig cumpla al 100%. Ahora mismo, tal y como está, completa aproximadamente el 75% de las comprobaciones y vuelve atrás y completa las comprobaciones aplicables en todas las versiones anteriores de .NET.

Se requiere intervención manual para cualquier aplicación .NET o sitio IIS.

## Requisitos:
- [X] Windows 7, Windows Server 2008 o posterior
- X] Pruebas en su entorno antes de ejecutar en sistemas de producción.

## STIGS/SRGs Aplicados:

- [Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip)

## Fuentes:

- [Add from one XML data to another existing XML file](http://www.maxtblog.com/2012/11/add-from-one-xml-data-to-another-existing-xml-file/)
- [Caspol.exe (Code Access Security Policy Tool)](https://docs.microsoft.com/en-us/dotnet/framework/tools/caspol-exe-code-access-security-policy-tool)
- [Microsoft .NET Framework Documentation](https://docs.microsoft.com/en-us/dotnet/framework/)
- [PowerShell $PSScriptRoot](https://riptutorial.com/powershell/example/27231/-psscriptroot)
- [PowerShell: Run command from script's directory](https://stackoverflow.com/questions/4724290/powershell-run-command-from-scripts-directory)
- [Powershell XML importnode from different file](https://stackoverflow.com/questions/9944885/powershell-xml-importnode-from-different-file)

## Descargar los archivos necesarios

Puede descargar los archivos necesarios desde [GitHub Repository](https://raw.githubusercontent.com/simeononsecurity/.NET-STIG-Script/)

## Cómo ejecutar el script

**El script puede ejecutarse desde la descarga extraída de GitHub así:**

## Cómo ejecutar el script
### Instalación manual:
Si se descarga manualmente, el script debe lanzarse desde un powershell administrativo en el directorio que contiene todos los archivos de la carpeta [GitHub Repository](https://github.com/simeononsecurity/.NET-STIG-Script)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-.net-4-stig.ps1
```
### Instalación automática:
Utilice esta herramienta para descargar, descomprimir y ejecutar automáticamente la última versión del script.
```
iwr -useb 'https://simeononsecurity.com/scripts/sosdotnet.ps1'|iex
```
