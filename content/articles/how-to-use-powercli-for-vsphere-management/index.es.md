---
title: "Domina PowerCLI para administrar vSphere"
date: 2023-08-02
lastmod: 2026-11-14
toc: true
draft: false
description: "Aprende a usar PowerCLI para administrar VMware vSphere, automatizar tareas y mejorar la productividad."
genre: ["Tecnología", "Virtualización", "VMware", "Gestión de TI", "Automatización", "Interfaz de línea de comandos", "Programación de scripts", "Administración de sistemas", "Computación en la nube", "Gestión de centros de datos"]
tags: ["PowerCLI", "VMware PowerCLI", "Instalar PowerCLI", "Instalación de PowerCLI", "Descargar PowerCLI", "Descarga de PowerCLI", "Conectar PowerCLI a vCenter", "Administración de vSphere", "Administración de máquinas virtuales", "Administración de hosts", "Automatización", "Programación de scripts", "Virtualización", "Servidor vCenter", "Hosts ESXi", "Administración de almacenes de datos", "Administración de adaptadores de red", "Creación de máquinas virtuales", "Eliminación de máquinas virtuales", "Configuración de máquinas virtuales", "Administración de recursos del host", "Asignación de CPU", "Asignación de memoria", "Configuración de almacenamiento", "Ejemplos de PowerCLI", "Documentación de PowerCLI", "Gestión de TI", "Administración de sistemas", "Computación en la nube"]
cover: "/img/cover/An_illustrated_cartoon_image_showcasing_a_pers.webp"
coverAlt: "Ilustración de una persona que usa comandos de PowerCLI para administrar máquinas virtuales y hosts en un entorno vSphere."
coverCaption: "Mejora la administración de vSphere con PowerCLI"
---

## Introducción

**PowerCLI** es una herramienta de **interfaz de línea de comandos (CLI)** de **VMware** que permite a los administradores **gestionar y automatizar** entornos **VMware vSphere**. Tanto si empiezas como si tienes experiencia, sus numerosos **cmdlets** simplifican las tareas administrativas y mejoran la productividad. Este artículo explica la instalación, la conexión a vCenter y el uso eficaz de PowerCLI.

______

## Instalar PowerCLI

Para **empezar a usar PowerCLI**, instálalo en tu equipo con estos pasos:

1. **Descarga** el instalador de PowerCLI desde el sitio oficial de VMware. El enlace está en la [documentación de PowerCLI](https://code.vmware.com/web/dp/tool/vmware-powercli). Elige la versión adecuada para tu sistema operativo.

2. **Ejecuta** el instalador y sigue las instrucciones. Elige la ubicación de instalación y las opciones que prefieras.

3. Pulsa «Finish» para completar la instalación. Después podrás empezar a usar PowerCLI.

______

## Conectarse a vCenter con PowerCLI

Después de instalar PowerCLI, conéctate al servidor vCenter para administrar la infraestructura virtual mediante sus cmdlets. Sigue estos pasos:

1. **Abre** PowerCLI desde el menú Inicio o el acceso directo del escritorio.

2. **Conéctate** al servidor vCenter con este comando:

```powershell
Connect-VIServer -Server <vCenter IP or hostname>
```

Sustituye `<vCenter IP or hostname>` por la dirección IP o el nombre de host real de tu servidor vCenter.

3. Cuando se solicite, introduce las **credenciales** de una cuenta con privilegios suficientes para administrar vCenter.

4. **Verifica** la conexión con un comando sencillo, como **Get-VMHost**. Si aparece una lista de hosts ESXi, la conexión se realizó correctamente.

______

## Usar PowerCLI para administrar vSphere

Una vez conectado a vCenter, puedes realizar tareas habituales como estas.

### Obtener información

PowerCLI incluye numerosos cmdlets para consultar el entorno vSphere. Por ejemplo:

- **Get-VM**: obtiene información sobre las máquinas virtuales.
- **Get-VMHost**: obtiene información sobre los hosts ESXi.
- **Get-Datastore**: obtiene información sobre los almacenes de datos.
- **Get-NetworkAdapter**: obtiene información sobre los adaptadores de red.

Usa parámetros con estos cmdlets para filtrar y dar formato a los resultados.

### Automatizar tareas

Una ventaja clave de PowerCLI es la automatización de tareas repetitivas. Con unas pocas líneas puedes ejecutar operaciones complejas en varios objetos a la vez. Por ejemplo:

#### Crear instantáneas de todas las máquinas virtuales de una carpeta

```PowerShell
## Apagar todas las máquinas virtuales de un host específico
Get-VMHost -Name "MyHost" | Get-VM | Stop-VM

## Crear una instantánea de todas las máquinas virtuales de una carpeta específica
Get-Folder -Name "MyFolder" | Get-VM | New-Snapshot -Name "DailySnapshot" -Description "Daily Backup"
```

Este script muestra cómo PowerCLI automatiza tareas como apagar todas las máquinas virtuales de un host y crear instantáneas de las máquinas de una carpeta.

#### Apagar de forma segura todas las máquinas virtuales de una carpeta

```PowerShell
## Obtener la carpeta que contiene las máquinas virtuales que se apagarán
$folder = Get-Folder -Name "MyFolder"

## Obtener todas las máquinas virtuales de la carpeta especificada
$vms = Get-VM -Location $folder

## Apagar todas las máquinas virtuales de forma ordenada
foreach ($vm in $vms) {
    if ($vm.PowerState -eq "PoweredOn") {
        $vm | Shutdown-VMGuest -Confirm:$false
    }
}
```

Este script muestra cómo apagar correctamente todas las máquinas virtuales de una carpeta. Primero, `Get-Folder` busca la carpeta y `Get-VM` obtiene las máquinas que contiene. Después, un bucle `foreach` recorre cada máquina. Si su estado es «PoweredOn», `Shutdown-VMGuest` inicia un apagado ordenado. El parámetro `-Confirm:$false` omite la solicitud de confirmación.

Así puedes garantizar un apagado ordenado de las máquinas virtuales de una carpeta.

Las funciones de scripting de PowerCLI también permiten crear flujos de automatización adaptados a tus necesidades.

### Administrar máquinas virtuales y hosts

PowerCLI permite realizar varias tareas de administración en máquinas virtuales y hosts. Por ejemplo:

- **Crear y quitar máquinas virtuales**: usa cmdlets como **`New-VM`** y **`Remove-VM`** para crear o quitar máquinas mediante programación. El cmdlet **[cmdlet New-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/new-vm/#DefaultParameterSet)** admite parámetros de CPU, memoria, disco y red durante la creación.

- **Modificar la configuración de máquinas virtuales**: cambia valores de CPU, memoria, disco y red. Por ejemplo, **[cmdlet Set-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/set-vm/#DefaultSet)** permite cambiar la asignación de CPU y memoria.

- **Administrar recursos del host**: gestiona la CPU, la memoria, la red y el almacenamiento. El cmdlet **[cmdlet Set-VMHost](https://vdc-repo.vmware.com/vmwb-repository/dcr-public/e7c1a32c-a3c6-4d7c-91bb-18a86a38daf7/12353298-ce6e-4d3f-bd8d-ab9f5ab044cc/doc/Set-VMHost.html)** permite modificar la configuración de red y almacenamiento del host.

Estos son algunos ejemplos de lo que puedes hacer con PowerCLI para administrar vSphere. Su amplio conjunto de cmdlets permite automatizar y simplificar muchas tareas administrativas.

## Conclusión

**PowerCLI** es una herramienta útil para administrar y automatizar entornos VMware vSphere. Sus numerosos cmdlets simplifican las tareas administrativas y mejoran la productividad. Tras instalarlo y conectarte a vCenter, puedes consultar información, automatizar tareas y administrar máquinas virtuales y hosts con eficiencia.

Empieza a explorar PowerCLI y simplifica la administración de vSphere.


## Referencias
- [Documentación de PowerCLI](https://code.vmware.com/web/dp/tool/vmware-powercli)
- [Connect-VIServer: referencia del cmdlet VMware PowerCLI](https://docs.vmware.com/en/VMware-PowerCLI/latest/VMware.VimAutomation.Core/Connect-VIServer.html)
- [Get-VM: referencia del cmdlet VMware PowerCLI](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/get-vm/#Default)
