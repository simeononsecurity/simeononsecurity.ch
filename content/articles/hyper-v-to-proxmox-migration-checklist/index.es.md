---
title: "Migrar una VM de Hyper-V a Proxmox VE: lista de verificación reversible"
date: 2026-10-11
lastmod: 2026-11-19
toc: true
draft: false
description: "Migre una máquina virtual de Hyper-V a Proxmox VE mediante una exportación con el origen apagado, firmware equivalente, importación de discos, prueba de arranque aislada y un plan de reversión."
genre: ["Virtualización", "Administración de sistemas", "Laboratorio doméstico"]
tags: ["Migración de Hyper-V a Proxmox", "Migración de Hyper-V", "Migración a Proxmox VE", "Importación de VHDX", "qm disk import", "Cambio de VM", "Exportación de Hyper-V", "VM Windows en Proxmox", "VirtIO en Proxmox", "Reversión de VM", "Migración UEFI", "Puntos de control de Hyper-V", "TPM virtual", "Recuperación de BitLocker", "Migración de laboratorio doméstico"]
cover: "/img/cover/hyper-v-to-proxmox-migration-checklist.webp"
coverAlt: "Un disco cruza un puente entre un bastidor de servidores azul y otro naranja, con una ruta de regreso separada y un escudo junto al destino."
coverCaption: "Mantenga disponible la VM de origen hasta que el nuevo huésped supere las comprobaciones del cambio."
---

Una **exportación de Hyper-V** conserva los archivos de una máquina virtual, mientras que Proxmox VE necesita una configuración nueva para el huésped y los archivos de disco virtual VHDX importados. Una copia correcta no demuestra por sí sola que el huésped arrancará ni atenderá a los usuarios. Esta lista lleva una VM por una exportación con el origen apagado, una prueba de arranque controlada y un cambio con una ruta de retorno clara.

<!--more-->

## Puntos clave

- **Registre el origen:** anote la generación del firmware, las rutas de disco, los puntos de control, la red y el cifrado antes de exportar.
- **Detenga las escrituras:** apague la VM de Hyper-V antes de la exportación final y manténgala apagada durante la prueba en Proxmox.
- **Iguale la ruta de arranque:** Hyper-V Generation 1 usa BIOS heredado. Generation 2 usa UEFI.
- **Valide el servicio:** compruebe los datos, el acceso de red, las copias de seguridad y el estado del huésped antes de retirar el origen.

## Antes de comenzar

Programe una ventana de mantenimiento y una prueba con una VM desechable. Necesita acceso de administrador a Hyper-V, Proxmox VE, almacenamiento para la exportación y una copia de seguridad verificada, separada de la copia de migración. Reserve tiempo para transferir todos los discos virtuales y probar la aplicación del huésped. El tamaño del disco y la velocidad de transferencia determinan el tiempo de inactividad.

Este procedimiento cubre una VM convencional con discos virtuales. **Las VM protegidas, los discos de paso directo, los discos compartidos, las cargas de trabajo en clúster y las licencias ligadas al hardware** requieren planes específicos. Anote quién decide el cambio y la hora límite para revertir. No inicie ambas copias en la red de producción con la misma identidad de máquina.

| Dato de origen | Por qué lo necesita |
|---|---|
| **Generación y firmware de la VM** | Elegir SeaBIOS u OVMF en Proxmox |
| **Estado y plantilla de Secure Boot** | Igualar la política de arranque e inscribir claves compatibles |
| **Discos de arranque y datos** | Importar todos los archivos VHDX necesarios en el orden correcto |
| **Puntos de control y archivos AVHDX** | Evitar tratar un disco diferencial como disco base independiente |
| **IP, DNS, MAC y VLAN** | Restaurar la conectividad sin duplicar una identidad |
| **vTPM y BitLocker** | Preparar la recuperación antes de cambiar el hardware virtual |
| **Servicios y comprobaciones de datos** | Definir pruebas de éxito y reversión |

Generation 1 usa BIOS heredado. Generation 2 usa la Interfaz de firmware extensible unificada (UEFI). Un **archivo AVHDX** es un disco diferencial de Hyper-V vinculado a un VHDX base. Un **vTPM** es un Módulo de plataforma segura virtual que usa BitLocker y otras funciones. Una **VLAN** es una red lógica independiente transportada por hardware de red compartido.

**SeaBIOS** proporciona firmware BIOS heredado. **OVMF** proporciona firmware UEFI. **VirtIO** es una interfaz de dispositivo virtual rápida que requiere controladores en el huésped. Un **initramfs** es el sistema de archivos inicial de Linux que carga controladores antes del sistema principal.

## Hacer inventario de la máquina virtual en Hyper-V

Ejecute estos comandos de solo lectura en una sesión elevada de PowerShell en el host de Hyper-V. Son ejemplos no probados. Confirme cada comando con el módulo Hyper-V instalado y su procedimiento de cambios antes de usarlos. Escriba el nombre de la VM cuando se le solicite:

```powershell
$vmName = Read-Host "Nombre de la VM de Hyper-V"
Get-VM -Name $vmName | Select-Object Name, State, Generation, ProcessorCount, MemoryAssigned
Get-VMHardDiskDrive -VMName $vmName | Select-Object ControllerType, ControllerNumber, ControllerLocation, Path
Get-VMSnapshot -VMName $vmName | Select-Object Name, CreationTime
Get-VMNetworkAdapter -VMName $vmName | Select-Object Name, SwitchName, MacAddress
```

El [módulo PowerShell de Hyper-V](https://learn.microsoft.com/en-us/powershell/module/hyper-v/) documenta estos comandos de inventario. Compare las rutas de disco con la configuración de la VM y anote cualquier ISO, disco de datos, conmutador virtual, dirección estática o reserva DHCP conectados. Registre el sistema operativo y las versiones de la aplicación del huésped. Verifique la copia de seguridad restaurando una copia de prueba o revisando un resultado de restauración documentado reciente. Una copia de archivos sin una prueba de recuperación aporta menos evidencia.

Para una VM **Generation 2**, registre también el firmware y la configuración de seguridad:

```powershell
Get-VMFirmware -VMName $vmName | Format-List *
Get-VMSecurity -VMName $vmName | Format-List *
```

Registre el estado de **Secure Boot**, la plantilla y la opción vTPM. La referencia de Microsoft [**`Get-VMFirmware`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmfirmware) limita el comando a Generation 2. [**`Get-VMSecurity`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmsecurity) muestra la configuración de seguridad de la VM. No ejecute **`Get-VMFirmware`** en un huésped Generation 1. Una **dirección MAC** identifica una interfaz de red. **DNS** asigna nombres a direcciones. **DHCP** asigna la configuración de red. Un **disco EFI** almacena los ajustes de UEFI.

**Resuelva los puntos de control antes de la exportación final.** Microsoft indica que una exportación de Hyper-V recopila tanto los archivos de puntos de control como los discos VHDX. Al eliminar un punto de control desde Hyper-V se combina su disco diferencial. Nunca elimine un archivo **`.avhdx`** desde el sistema de archivos para borrar un punto de control. Si falla una combinación o la cadena de discos parece incompleta, deténgase y siga las [instrucciones de recuperación de puntos de control de Microsoft](https://learn.microsoft.com/en-us/troubleshoot/windows-server/virtualization/hyper-v-snapshots-checkpoints-differencing-disks). La [guía de puntos de control de Microsoft](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/checkpoints) explica la eliminación y combinación normales.

Para un huésped Windows que use **BitLocker** o un **TPM virtual**, obtenga y verifique la clave de recuperación antes de cambiar el hardware virtual. La [documentación de seguridad Generation 2 de Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/generation-2-virtual-machine-security-features) describe el cifrado respaldado por vTPM. Las [preguntas frecuentes de BitLocker de Microsoft](https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-key-management-faq) explican por qué los cambios de arranque activan la recuperación. Un nuevo dispositivo TPM de Proxmox no reproduce el estado TPM anterior. Guarde la clave fuera de la VM exportada.

## Exportar una VM apagada

Apague el huésped de forma ordenada. Confirme que Hyper-V muestre **Off** (apagada), no Saved (guardada). Espere a que termine cualquier combinación de puntos de control y luego exporte la VM a una ubicación con espacio libre suficiente. En Hyper-V Manager, haga clic con el botón derecho en la VM, elija **Export** (exportar) y seleccione el destino. El equivalente de PowerShell es:

```powershell
$vmName = Read-Host "Nombre de la VM de Hyper-V apagada"
$exportPath = Read-Host "Directorio de destino de la exportación"
$vm = Get-VM -Name $vmName -ErrorAction Stop
if ($vm.State -ne 'Off') { throw "Apague la VM y espere a que Hyper-V indique Off (apagada) antes de exportarla." }
Export-VM -Name $vmName -Path $exportPath
```

La [guía de exportación de Microsoft](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/export-and-import-virtual-machines) indica que la exportación incluye discos virtuales, configuración y archivos de puntos de control. La referencia de [**`Export-VM`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/export-vm) define el comando. Confirme los archivos de disco esperados y sus tamaños en el destino. Conserve la VM de origen apagada y su copia de seguridad independiente. **No modifique los archivos exportados durante la importación.**

Transfiera los archivos VHDX a una ruta accesible desde el host Proxmox. Trate la exportación como datos confidenciales del huésped. Use transporte cifrado, limite el acceso a la ubicación de transferencia y al almacenamiento de destino, y elimine las copias temporales después de validarlas. Compruebe la capacidad disponible tanto en el área de transferencia como en el almacenamiento de destino. Conserve una exportación intacta para la reversión. Si la exportación contiene archivos **`.avhdx`**, no elija un **`.vhdx`** base por su nombre suponiendo que incluye las escrituras más recientes. Resuelva la cadena de discos en Hyper-V antes de continuar.

## Crear la máquina virtual de destino en Proxmox

Cree una VM nueva en la interfaz web de Proxmox con el tipo de sistema operativo, la CPU y la memoria registrados antes. Elija un ID de VM nuevo y sin usar. No instale un sistema operativo nuevo. Quite el disco vacío creado por el asistente antes de importar el disco de origen. Mantenga desconectado el adaptador de red del puente de producción durante el primer arranque, o conéctelo a una red de prueba aislada.

| Origen Hyper-V | Destino Proxmox |
|---|---|
| **Generation 1, BIOS heredado** | SeaBIOS |
| **Generation 2, UEFI** | OVMF con disco EFI y política Secure Boot equivalente |
| **Disco de arranque Windows sin controlador de almacenamiento VirtIO** | Conectarlo inicialmente como SATA |
| **Windows con vTPM o BitLocker** | Dispositivo nuevo de estado TPM cuando sea necesario, clave de recuperación lista antes del primer arranque |

La [guía de generación de VM de Microsoft](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/plan/Should-I-create-a-generation-1-or-2-virtual-machine-in-Hyper-V) relaciona Generation 1 con BIOS heredado y Generation 2 con UEFI. La [documentación de VM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) documenta SeaBIOS, OVMF y el disco EFI que conserva los ajustes UEFI. **Iguale el modo de arranque del origen.** Cambiarlo durante la migración crea otro problema de arranque que deberá diagnosticar.

Para un origen Generation 2, iguale si **Secure Boot** estaba habilitado. Compruebe la plantilla del origen y seleccione claves inscritas compatibles con el huésped. Los nombres de plantilla de Hyper-V no se transfieren a Proxmox. El disco EFI de 4 MB de Proxmox y la opción **Pre-Enroll keys** (inscribir previamente las claves) proporcionan claves Secure Boot y habilitan Secure Boot de forma predeterminada. Verifique el arranque del destino antes del cambio. La [referencia de firmware de Microsoft](https://learn.microsoft.com/en-us/powershell/module/hyper-v/set-vmfirmware) describe el requisito de plantilla del origen. La [documentación del disco EFI de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) describe las claves del destino.

Antes de cambiar las claves EFI, verifique que la clave de recuperación esté guardada y anote los ID de protectores actuales. Siga la documentación instalada de Proxmox VE y OVMF para inscribir claves EFI. Vuelva a confirmar la clave de recuperación y verifique `manage-bde -status` antes del primer arranque. No suspenda, deshabilite ni elimine protectores como paso genérico de migración. Registre la versión del paquete de firmware, el estado de Secure Boot y la versión de firmware, y el estado de BitLocker.

Si el origen usa un **vTPM**, agregue **TPM State** (estado del TPM) en el panel Hardware (componentes) de Proxmox antes del primer arranque. Seleccione la **versión 2.0**, salvo que el huésped tenga un requisito documentado para la versión 1.2. Esto crea un estado TPM nuevo, no una copia del vTPM de Hyper-V. Un huésped BitLocker necesita su clave de recuperación verificada en el primer arranque. La [documentación TPM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) describe la acción Hardware (componentes) y las versiones.

Para Windows, comience con un disco de arranque SATA, salvo que el huésped ya tenga el controlador de almacenamiento VirtIO requerido. Tras un arranque correcto, instale los controladores VirtIO compatibles y cambie un dispositivo virtual a la vez. Proxmox recomienda VirtIO SCSI por su rendimiento, pero la falta de un controlador de arranque impide que Windows acceda al disco del sistema. Para Linux, compruebe que initramfs incluya el controlador de almacenamiento de destino antes de cambiar el bus. La [documentación de VM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) describe los controladores de disco.

## Importar y conectar discos

En el host Proxmox, compruebe la ruta VHDX copiada. El siguiente comando muestra una importación para el ID de VM **230** en un almacenamiento con ID **`local-lvm`**. Sustituya los tres valores por los suyos:

```bash
qm disk import 230 /path/to/exported/boot.vhdx local-lvm
```

La referencia [**`qm disk import`** de Proxmox](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc) indica que la imagen de origen se importa como un **disco sin usar**. La [documentación de imágenes de QEMU](https://www.qemu.org/docs/master/system/images) incluye VHDX entre los formatos de conversión compatibles. Importe cada disco de datos adicional por separado. Espere a que termine cada tarea de importación y compare los tamaños importados con el inventario de origen.

En el panel **Hardware** (componentes) de la VM, conecte el disco de arranque sin usar como **SATA** para el primer arranque de Windows. Conecte los discos de datos en el orden documentado. En **Options > Boot Order** (opciones > orden de arranque), seleccione el disco de arranque. Para un huésped Generation 2, verifique **OVMF** y el disco EFI. Mantenga intactos los archivos de importación y la VM de origen hasta superar la validación.

## Probar antes del cambio

Inicie el huésped Proxmox en la red aislada. Use la consola para revisar la pantalla de arranque, el inicio de sesión del sistema operativo, los volúmenes, los datos de la aplicación y los registros del servicio. Una pantalla de inicio de sesión no demuestra que la migración haya tenido éxito. Realice las comprobaciones anotadas antes de exportar, incluida una transacción representativa o la lectura de datos recientes.

Para un huésped BitLocker, desbloquéelo con la clave de recuperación si se le solicita. Después de que inicie Windows, revise el estado de protección del volumen del sistema y sus protectores desde un símbolo del sistema elevado:

```powershell
manage-bde -status C:
manage-bde -protectors -get C:
```

La [guía operativa de BitLocker de Microsoft](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) documenta la inspección de protectores y la copia de seguridad de claves de recuperación. La salida contiene material de recuperación confidencial. No lo pegue en un ticket ni en un registro público. Verifique el protector previsto y guarde un método de recuperación actual según su política. Reinicie el huésped y confirme que arranca sin otra solicitud de recuperación antes del cambio. Una solicitud de recuperación repetida es una comprobación fallida, no una razón para descartar la clave original.

| Prueba | Condición de aprobación |
|---|---|
| **Arranque y discos** | El huésped inicia y monta todos los volúmenes esperados |
| **Secure Boot y BitLocker** | Se mantiene la política de arranque prevista y el huésped cifrado reinicia sin repetir la recuperación |
| **Aplicación** | Una lectura o transacción representativa se completa correctamente |
| **Red** | Los pares necesarios alcanzan el huésped de prueba en los puertos previstos |
| **Recuperación** | La copia de seguridad de Proxmox y una restauración aislada funcionan antes de retirar el origen |
| **Operaciones** | La supervisión, la sincronización horaria, el apagado y el agente del huésped funcionan como se espera |

Cuando pasen las comprobaciones de la aplicación, cambie la ruta o dirección de red de producción durante la ventana de mantenimiento. Mantenga apagado Hyper-V. Una NIC virtual distinta podría requerir una nueva reserva DHCP o corregir una dirección estática en el huésped. Compruebe DNS, reglas de firewall y servicios dependientes desde otro cliente. La [documentación de VM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) cubre las opciones de dispositivos de red y agente de huésped.

## Diagnosticar y revertir

| Síntoma | Primera comprobación |
|---|---|
| **No hay dispositivo de arranque** | Orden de arranque, disco importado, modo BIOS o UEFI y claves Secure Boot |
| **Error de almacenamiento de Windows** | Conexión SATA y controlador de almacenamiento VirtIO ausente |
| **Solicitud de recuperación BitLocker repetida** | Estado TPM nuevo, política Secure Boot, mediciones de arranque y protectores |
| **El huésped inicia sin red** | NIC virtual nueva, puente, VLAN, reserva DHCP y dirección estática |
| **Datos antiguos o ausentes** | VHDX equivocado, exportación incompleta, cadena de puntos de control o disco de datos ausente |

Si una prueba necesaria falla antes del plazo de reversión, detenga la VM Proxmox y desconéctela de la red de producción. Restaure la ruta de red de origen y luego inicie la VM original de Hyper-V. **Nunca ejecute ambas copias con la misma identidad de producción.** Registre las escrituras aceptadas por la copia Proxmox antes de volver a Hyper-V. Esas escrituras requieren recuperación o conciliación por separado, ya que el disco de origen no las recibió.

Conserve la VM de origen y la exportación hasta que el huésped Proxmox supere las comprobaciones del servicio, una copia de seguridad nueva, una restauración aislada y un período de observación acordado. La [comparación de virtualización del sitio](/articles/vmware-esxi-citrix-xenserver-hyper-v-comparison/) ayuda a elegir una plataforma. La [guía de actualización de Proxmox](/articles/proxmox-ve-8-to-9-upgrade-guide/) cubre una tarea de mantenimiento posterior. **La migración termina cuando la carga de trabajo y la ruta de recuperación funcionan en el host nuevo, no cuando acaba la importación del disco.**

## Próximos pasos

Conserve la VM de origen y la exportación hasta que las comprobaciones de la carga de trabajo, de las copias de seguridad y de reversión pasen durante el período de observación acordado. Revise la [prueba de restauración de copias de seguridad de VM en Proxmox](/articles/proxmox-vm-backup-restore-drill/) antes de retirar el origen.
