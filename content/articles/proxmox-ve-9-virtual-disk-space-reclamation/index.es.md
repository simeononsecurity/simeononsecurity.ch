---
title: "Proxmox VE 9: Reduce el uso de discos virtuales y recupera espacio"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Reduce el almacenamiento de VM y contenedores LXC en Proxmox VE 9. Compara formatos y backends, activa discard, ejecuta trim y revisa las instantáneas antes de recuperar espacio."
genre: ["Virtualización", "Administración de Linux", "plataforma Proxmox VE", "Almacenamiento", "Laboratorio doméstico"]
tags: ["espacio de disco Proxmox VE 9", "aprovisionamiento ligero Proxmox", "notificaciones discard Proxmox", "comando TRIM Proxmox", "Windows ReTrim en Proxmox", "Linux fstrim en Proxmox", "uso de disco LXC Proxmox", "aprovisionamiento ligero LVM Proxmox", "zvol disperso ZFS Proxmox", "dispositivos de bloque Ceph RBD Proxmox", "formato qcow2 Proxmox", "disco raw Proxmox", "instantáneas Proxmox", "recuperación de espacio de disco virtual", "tipos de almacenamiento Proxmox", "controlador VirtIO SCSI", "detección de escrituras de cero Proxmox", "almacenamiento de copias de seguridad Proxmox"]
cover: "/img/cover/proxmox-ve-9-virtual-disk-space-reclamation.webp"
coverAlt: "Dos cuadrículas de bloques unidas por una flecha muestran los bloques usados de un disco virtual y la capacidad libre de un grupo de almacenamiento."
coverCaption: "Borrar datos del invitado, enviar discard y recuperar espacio son pasos distintos."
---

**Un sistema de archivos invitado más pequeño no siempre reduce el almacenamiento usado en Proxmox.** Para liberar espacio en el host se necesita un disco compatible con aprovisionamiento ligero, una ruta discard operativa para las VM y un almacenamiento de respaldo sin bloques retenidos por instantáneas. Esta guía cubre los ajustes y comprobaciones para VM y contenedores LXC de Proxmox VE 9.

<!--more-->

## Puntos clave

- **Elige primero el almacenamiento de respaldo.** El tamaño anunciado del disco virtual solo difiere del espacio asignado en el host cuando el formato de imagen o el backend admite aprovisionamiento ligero.
- **Activa discard en la VM y luego ejecuta trim dentro del invitado.** Windows ReTrim y Linux `fstrim` envían solicitudes de bloques sin uso a través del disco virtual.
- **Comprueba las instantáneas y las copias por separado.** Los bloques antiguos siguen asignados mientras una instantánea haga referencia a ellos. Los archivos de copia y los fragmentos de PBS siguen sus propias reglas de retención.
- **Clasifica los montajes LXC por tipo.** Los volúmenes rootfs y puntos de montaje administrados, los montajes bind y los montajes de dispositivos tienen distintos propietarios y comportamientos de copia.

## Antes de empezar

Necesitas **acceso de administrador a Proxmox VE 9**, una copia de seguridad verificada de cada invitado afectado y suficiente espacio libre en el grupo para la operación. Anota el ID del invitado, el bus de disco, el ID del volumen, el ID de almacenamiento, las instantáneas y la asignación actual antes de cambiar ajustes. Usa el [simulacro de restauración de VM](/articles/proxmox-vm-backup-restore-drill/) para probar la recuperación.

**Tiempo estimado:** 20 a 60 minutos por invitado, más cualquier tarea extensa de trim o limpieza. **Dificultad:** Intermedia. Empieza con una VM de bajo riesgo y compara su uso de almacenamiento antes y después.

> **Advertencia:** Un grupo thin lleno produce errores de E/S en los invitados y arriesga daños en el sistema de archivos. No sobreasignes capacidad sin vigilar el espacio libre de datos y metadatos del grupo. [Documentación de almacenamiento de Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Sigue la cadena de asignación

**Borrado**, **discard** y **recuperación** ocurren en capas distintas. El invitado borra un archivo y marca libres sus bloques del sistema de archivos. El sistema de archivos envía TRIM o UNMAP para esos bloques. QEMU reenvía la solicitud si discard está activado en el disco virtual. El backend libera la asignación física si su formato y grupo admiten la operación. [Documentación de discos de VM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Capa | Qué revisar | Evidencia útil |
|---|---|---|
| **Archivos del invitado** | Espacio libre del sistema de archivos | Propiedades del volumen de Windows o `df -h` en Linux |
| **Disco virtual** | Bus, discard, emulación SSD, formato de imagen | Pestaña **Hardware** de la VM o `qm config VMID` |
| **Volumen PVE** | Propietario y tamaño configurado | Pestaña **Contenido** del almacenamiento o `pvesm list STORAGE_ID` |
| **Grupo de almacenamiento** | Datos y metadatos libres, bloques retenidos | `pvesm status` y herramientas específicas del backend |

**Un disco virtual de 100 GiB fija un límite de capacidad, no garantiza 100 GiB asignados.** A la inversa, que el invitado informe 20 GiB en uso no prueba que el host use 20 GiB. Los metadatos, las instantáneas, las copias y los bloques escritos anteriormente cambian la cifra. [Documentación de almacenamiento de Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Compara formatos de disco

**El backend de almacenamiento determina qué formatos de imagen ofrece Proxmox.** Los zvol de ZFS y Ceph RBD usan discos virtuales raw. LVM suele usar raw, con una excepción de cadena de volúmenes de Proxmox VE 9 descrita más adelante. Los backends de archivos como directory y NFS admiten raw o qcow2. Raw no proporciona por sí solo asignación thin ni instantáneas. El almacenamiento subyacente debe ofrecer esas funciones. Qcow2 ofrece asignación por copia en escritura e instantáneas en la capa de imagen. [Documentación de discos de VM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Formato | Mecanismo de asignación | Compensación de espacio |
|---|---|---|
| **qcow2 en almacenamiento de archivos** | Qcow2 asigna clústeres al escribirlos | Los metadatos de la imagen y las cadenas de instantáneas consumen espacio |
| **Archivo raw en almacenamiento de archivos** | Comportamiento de archivo disperso del sistema de archivos, si se admite | Raw por sí solo no ofrece aprovisionamiento thin ni instantáneas |
| **Volumen de bloques raw** | LVM thin, ZFS, Ceph RBD u otro almacenamiento de respaldo | La asignación del grupo y las instantáneas dependen del backend |

**Proxmox VE 9 thick LVM tiene un modo especial de instantáneas.** `snapshot-as-volume-chain` usa relaciones qcow2 de respaldo entre volúmenes lógicos thick LVM. No usa instantáneas internas de qcow2. La opción solo afecta a discos de VM nuevos y sigue siendo una vista previa tecnológica en la documentación actual de Proxmox. PVE muestra cada instantánea como completamente asignada. La asignación real en la SAN solo es menor si el almacenamiento de respaldo admite aprovisionamiento thin y discard. [Documentación de almacenamiento LVM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc)

**No conviertas un disco solo porque su extensión sea `.raw`.** Comprueba primero el complemento de almacenamiento y sus bloques asignados. Un disco raw en `local-lvm` tiene un comportamiento de asignación distinto al de un archivo raw completamente asignado en almacenamiento directory normal.

## Compara tipos de almacenamiento

Proxmox separa el **almacenamiento de archivos** del **almacenamiento de bloques**. El complemento de almacenamiento también controla instantáneas, clones, uso compartido y los tipos de contenido que admite cada grupo. Revisa la entrada de **Datacenter > Storage** antes de confiar en un formato o función. [Tabla de tipos de almacenamiento de Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

| Almacenamiento | Comportamiento del disco de VM | Comprobación de recuperación |
|---|---|---|
| **Directory, ext4, XFS** | Archivos raw o qcow2 | Compara los bytes asignados de `du` con el tamaño virtual de la imagen. Revisa las instantáneas si otra capa las ofrece. |
| **NFS, CIFS** | Archivos raw o qcow2 en almacenamiento compartido | Comprueba el espacio asignado en el servidor. El resultado de trim del invitado no demuestra que el espacio del servidor haya bajado. |
| **LVM con asignación ligera (`local-lvm`)** | Volúmenes lógicos raw thin, solo local | Vigila con `lvs` los porcentajes de datos y metadatos del thin pool. |
| **LVM thick** | LV raw o cadenas de volúmenes qcow2 de VE 9 | El borrado en el invitado no reduce la reserva fija del LV. Comprueba por separado la asignación thin de la SAN. |
| **Almacenamiento ZFS (`local-zfs`)** | zvol raw o subvolúmenes de contenedores | Comprueba `sparse`, las propiedades del conjunto de datos, el uso del grupo y las instantáneas. |
| **Ceph RBD** | Imágenes RBD raw thin en almacenamiento compartido | Comprueba la capacidad del grupo Ceph, el uso de la imagen, sus instantáneas y discard. |
| **Btrfs** | Volúmenes respaldados por archivos con subvolúmenes Btrfs para imágenes raw | Trata el complemento Btrfs de PVE como una vista previa tecnológica y revisa las instantáneas y el uso del sistema de archivos. |

**Otros complementos de almacenamiento cumplen funciones distintas.** CephFS ofrece almacenamiento de archivos compartido. iSCSI y Fibre Channel exponen dispositivos de bloques compartidos, a menudo divididos en volúmenes de VM con LVM. ZFS over iSCSI usa almacenamiento remoto de bloques respaldado por ZFS. Proxmox Backup Server (PBS) guarda copias, no discos de VM activos. Comprueba los tipos de **Contenido** habilitados antes de colocar datos `images`, `rootdir`, `backup` o `iso` allí. [Tabla de tipos de almacenamiento de Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**Los indicadores de asignación del almacenamiento de archivos importan al crear el disco.** El valor `format` del almacenamiento elige `raw`, `qcow2` o `vmdk` cuando se admiten. `preallocation` para archivos raw y qcow2 acepta `off`, `metadata`, `falloc` o `full`. El valor predeterminado es `metadata`, tratado como `off` para raw. `full` reserva el espacio del archivo por adelantado y elimina la huella inicial pequeña habitual. Revisa la configuración antes de crear un disco grande. El indicador `shared` solo declara acceso compartido existente. No convierte el almacenamiento local en compartido. [Propiedades comunes de almacenamiento de Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**`sparse` de ZFS es el ajuste de almacenamiento para crear zvol thin.** Sin zvol sparse, la creación reserva capacidad según el comportamiento configurado del volumen. Inspecciona la configuración y el grupo antes de cambiar una implementación existente. [Documentación de almacenamiento ZFS de Proxmox](https://github.com/proxmox/pve-docs/blob/master/pve-storage-zfspool.adoc)

**El almacenamiento directory requiere una segunda comprobación.** La longitud lógica de un archivo qcow2 no es la capacidad virtual visible para el invitado. `du -h` informa los bloques del sistema de archivos asignados a la imagen. `ls -lh` muestra su longitud lógica. Para una VM detenida, `qemu-img info` informa la capacidad virtual y el tamaño en el host. En NFS, usa la contabilidad del servidor para decidir la capacidad final. [Referencia de QEMU `qemu-img`](https://www.qemu.org/docs/master/tools/qemu-img.html)

**NFS tiene otro límite de asignación.** Que qcow2 reutilice un clúster vacío dentro de su archivo no significa que el servidor NFS libere bloques del archivo. La liberación de huecos necesita compatibilidad del cliente, el protocolo negociado, el servidor y su sistema de archivos. NFSv4.2 define `DEALLOCATE`, pero el número de versión por sí solo no demuestra que el servidor haya devuelto espacio. Inspecciona el montaje NFS negociado y mide la asignación en el servidor. [Especificación NFSv4.2 `DEALLOCATE`](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2)

## Configura los indicadores del disco de VM

En la interfaz de Proxmox, abre **VM > Hardware > Hard Disk > Edit**. Inspecciona el bus del disco y las opciones avanzadas. Estos indicadores afectan la asignación o determinan si una optimización sirve. La [referencia oficial de opciones `qm`](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc) indica la disponibilidad según el bus.

| Bus | Opción relacionada con el espacio |
|---|---|
| **IDE** | Compatibilidad heredada. Úsalo solo si el invitado carece de un controlador más reciente. |
| **SATA** | Emulación ampliamente compatible. Verifica trim y las opciones del disco antes de confiar en la recuperación. |
| **SCSI con VirtIO SCSI** | Ruta moderna preferida para discard y ajustes por disco. Windows necesita el controlador VirtIO. |
| **VirtIO Block** | Disco paravirtualizado. El discard de Linux requiere kernel 5.0 o posterior. No admite emulación SSD. |

| Ajuste | Efecto | Guía |
|---|---|---|
| **Habilita discard (`on`)** | Reenvía TRIM o UNMAP del invitado | Necesario para recuperar espacio desde el invitado en un backend thin compatible. El valor predeterminado `ignore` bloquea el reenvío. |
| **Emulación SSD `ssd=1`** | Presenta el disco al invitado como SSD | Algunos invitados necesitan esta identidad antes de emitir trim. No acelera el almacenamiento físico. VirtIO Block no tiene este indicador. |
| **Detect zeroes `detect_zeroes=1`** | Detecta e intenta optimizar escrituras de ceros | Optimización de E/S opcional. No reemplaza trim del invitado ni garantiza espacio recuperado. |
| **Bus: SCSI / VirtIO SCSI single** | Expone un disco SCSI mediante el controlador VirtIO | Opción práctica para invitados modernos Windows y Linux. Instala los controladores VirtIO de Windows. |
| **Bus: VirtIO Block** | Usa el dispositivo de bloques VirtIO | El discard de Linux requiere kernel 5.0 o posterior. No admite emulación SSD. |
| **Hilo de E/S `iothread=1`** | Asigna la E/S de la unidad a otro hilo | Úsalo con VirtIO Block o SCSI en un controlador VirtIO SCSI single. Es un ajuste de rendimiento, no de recuperación. |
| **Caché y AIO** | Cambian el búfer de E/S y la E/S asíncrona | Ajústalos según la carga de trabajo y el backend. Ninguno reduce el disco. |
| **Copia `backup=0`** | Excluye el disco de las copias de VM | Reduce el alcance de la copia y elimina sus datos de la recuperación de VM. Documenta una copia separada. |
| **Replicación `replicate=0`** | Excluye el disco de la replicación de almacenamiento | Reduce los datos replicados y excluye el disco de la réplica. |

**Otras opciones de unidad describen comportamientos, no recuperación.** `format` se aplica al asignar un disco en un backend con varios formatos de imagen. `size` es capacidad virtual, no bytes asignados. `ro=1` marca el disco como solo lectura. `snapshot=1` activa el modo de instantánea temporal de QEMU, que descarta cambios al apagar la VM. No es el indicador para incluir un disco en las instantáneas de VM de Proxmox. Evítalo con datos persistentes. Comprueba la cobertura de recuperación antes de usar `backup=0` o `replicate=0`. [Opciones de disco de VM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)

**No pegues una cadena `qm set --scsi0` abreviada sobre una unidad existente.** Inspecciona **`qm config VMID`** y conserva el ID completo del volumen y las opciones actuales al editarla. Una asignación abreviada arriesga perder otros ajustes por disco. En la interfaz, verifica las opciones guardadas tras cada cambio.

```bash
qm config 100
pvesm status
```

El `100` es un ID de VM de ejemplo. Para crear un disco SCSI **nuevo** de 64 GiB en una VM existente cuyo controlador sea **VirtIO SCSI single** y cuyo invitado tenga el controlador necesario, este comando muestra la sintaxis de asignación. Sustituye el ID de VM y el ID de almacenamiento por los tuyos.

```bash
qm set 100 --scsi0 local-lvm:64,discard=on,ssd=1,iothread=1
```

**Comprueba si ya existe `scsi0` antes de usar el ejemplo.** El comando cambia la ranura. Para un disco existente, usa la interfaz si resulta más fácil conservar su cadena exacta de opciones. Consulta la [referencia del comando `qm` de Proxmox](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc).

## Limpia los archivos del sistema invitado

**Libera primero archivos del invitado.** Revisa la configuración de Almacenamiento de Windows, archivos temporales, instaladores antiguos, cachés de aplicaciones y la papelera. Usa la interfaz propia de cada aplicación para limpiar bases de datos y entornos de contenedores. Borrar datos activos de una aplicación solo para reducir la asignación arriesga perder datos.

**Confirma que el volumen usa un disco virtual compatible con discard** y ejecuta una sesión elevada de PowerShell dentro de la VM Windows:

```powershell
fsutil behavior query DisableDeleteNotify
Optimize-Volume -DriveLetter C -ReTrim -Verbose
```

`DisableDeleteNotify = 0` indica que Windows tiene activadas las notificaciones de borrado para el sistema de archivos informado. **ReTrim** vuelve a enviar solicitudes trim para las regiones actualmente libres del volumen. Que el comando termine correctamente confirma que el invitado envió la operación, no cuántos bytes recuperó el host. Comprueba el host al terminar la tarea. [Referencia de Microsoft `Optimize-Volume`](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps) y [documentación de discos de VM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

**No confundas QEMU guest agent con TRIM.** El agente admite control del invitado y funciones de consistencia de copias. Las notificaciones de borrado del sistema de archivos viajan por la ruta del disco virtual. Instalar solo el agente no recupera bloques. [Documentación del agente invitado de VM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

## Marca los bloques sin uso del sistema de archivos

**Comprueba la ruta de bloques y el sistema de archivos antes de trim.** Una distribución moderna suele ejecutar periódicamente `fstrim.timer`. Inspecciona su estado y luego aplica trim a los sistemas de archivos montados tras borrar datos innecesarios del invitado.

```bash
lsblk -D
systemctl status fstrim.timer
sudo fstrim -av
```

**`lsblk -D`** informa la granularidad y los límites de discard de los dispositivos visibles. **`fstrim -av`** aplica trim a los sistemas de archivos montados compatibles e informa los rangos enviados. Los bytes enviados no equivalen a los bytes devueltos al grupo. Dispositivos cifrados, LVM, RAID y otras capas apiladas necesitan compatibilidad discard en cada capa. [Guía de Red Hat sobre bloques sin uso](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems)

Usa trim programado o una política deliberada de discard en línea. **No actives `discard` continuo en todos los sistemas de archivos como sustituto de comprobar la ruta de almacenamiento.** Tras aplicar trim en el invitado, inspecciona el volumen y grupo de PVE. Revisa la política de compactación propia de una base de datos o servicio si los registros borrados siguen ocupando sus archivos.

## Revisa por separado el almacenamiento de contenedores

**LXC no tiene un bus de disco emulado para el sistema de archivos root.** Empieza con `pct config CTID` e identifica cada entrada `rootfs` y `mpN`. Proxmox define montajes respaldados por almacenamiento, montajes bind y montajes de dispositivos. Una ruta visible dentro del contenedor no identifica qué volumen del host posee sus bloques. [Puntos de montaje de contenedores Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

```bash
pct config 101
pct exec 101 -- df -h
pvesm status
```

Para un **rootfs o punto de montaje administrado**, elimina archivos desde el contenedor o su aplicación y luego inspecciona en el host el volumen de respaldo y sus instantáneas. **No ejecutes comandos `qm` de discard de VM contra un CT.** En subvolúmenes ZFS, las instantáneas retienen bloques borrados. En almacenamiento directory y LVM thin, revisa la asignación real del respaldo, no el tamaño configurado del CT.

Ejecuta **`pct fstrim` en el host Proxmox** después de limpiar el CT cuando el almacenamiento de respaldo admita discard. Proxmox aplica trim al rootfs del CT y a los puntos de montaje administrados aptos. Omite los montajes bind y los montajes de solo lectura. Usa `--ignore-mountpoints` para aplicar trim solo al rootfs. Compara el uso del almacenamiento antes y después. [Referencia de Proxmox `pct fstrim`](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc)

```bash
pct fstrim 101
pct fstrim 101 --ignore-mountpoints 1
```

Los comandos muestran **alcances alternativos** para el CT de ejemplo con ID `101`. Usa el alcance que corresponda a tu disposición de almacenamiento. Un trim correcto no garantiza los mismos bytes liberados si las instantáneas retienen bloques antiguos.

**Los montajes bind y de dispositivos no los administra Proxmox.** Sus datos de origen permanecen en el host o en un dispositivo externo. Las copias `vzdump` del contenedor excluyen su contenido. Los puntos de montaje adicionales respaldados por almacenamiento también se excluyen por defecto, salvo que su opción `backup` los incluya. Comprueba la política de copia real antes de limpiar. [Documentación de copias de Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

Para Docker anidado, inspecciona las capas de imagen, volúmenes y registros dentro del propietario real del almacenamiento antes de usar comandos de limpieza Docker. La [guía de fiabilidad de Docker en LXC](/articles/docker-in-lxc-proxmox-reliability/) explica los límites de montajes y copias. Borrar una imagen de contenedor no elimina por defecto un volumen persistente.

## Mide correctamente el servidor

**Registra las mismas mediciones antes y después de la limpieza.** El espacio libre del grupo es la señal final de capacidad. Usa cifras por volumen para localizar qué invitado produjo el crecimiento.

```bash
pvesm status
pvesm list local-lvm
qm config 100
pct config 101
```

**`pvesm list`** inventaría los volúmenes administrados y sus tamaños configurados. No mide bytes asignados en almacenamiento thin. Para almacenamiento **directory**, inspecciona la ruta montada exacta y un archivo de imagen conocido. Sustituye las rutas por las de **Datacenter > Storage** y la configuración de la VM.

```bash
df -hT /var/lib/vz
du -h /var/lib/vz/images/100/vm-100-disk-0.qcow2
ls -lh /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

Para una VM **detenida**, compara la capacidad virtual y la asignación en el host de la imagen sin modificar el archivo:

```bash
qemu-img info /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

Para **LVM thin**, vigila los datos y metadatos del grupo:

```bash
lvs -a -o lv_name,vg_name,lv_size,data_percent,metadata_percent,segtype
```

Para **ZFS**, separa los datos activos del conjunto de datos de los retenidos por instantáneas:

```bash
zpool list
zfs list -o name,used,available,referenced,usedbysnapshots -r POOL_OR_DATASET
zfs list -t snapshot -o name,used,referenced,written -r DATASET
```

**`usedbysnapshots`** informa los bloques retenidos entre todas las instantáneas de un conjunto de datos. Los valores `used` de cada instantánea no se suman porque comparten bloques. Un archivo borrado puede no cambiar el uso del grupo hasta que caduque o se elimine, según la política de retención, cada instantánea que haga referencia a sus bloques. [Instantáneas y clones de OpenZFS](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html)

Para **Ceph RBD**, identifica el ID del volumen de Proxmox antes de ejecutar comandos Ceph. **`qm config VMID`** muestra `STORAGE_ID:IMAGE`. Abre la entrada RBD en **Datacenter > Storage** para encontrar su **grupo** y **espacio de nombres** opcional. El ID de almacenamiento no tiene por qué coincidir con el nombre del grupo. Construye `POOL/IMAGE` con los valores del grupo y la imagen. Ejecuta estos comandos en un cliente configurado para el clúster Ceph previsto y con credenciales válidas. [Documentación de almacenamiento RBD de Proxmox](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc)

```bash
ceph df
rbd du POOL/IMAGE
rbd snap ls POOL/IMAGE
```

**`rbd du`** informa el uso aprovisionado y real de la imagen, incluidas sus instantáneas. Sin la función de imagen `fast-diff`, consulta los OSD para buscar objetos y requiere más trabajo. **`ceph df`** muestra la capacidad del grupo y del clúster. La replicación, la codificación de borrado y las instantáneas afectan el uso bruto del clúster, por lo que difieren los bytes de imagen y de grupo. [Referencia de comandos Ceph RBD](https://docs.ceph.com/en/squid/man/8/rbd/) y [guía de uso de grupos Ceph](https://docs.ceph.com/en/squid/rados/operations/monitoring/)

Si el almacenamiento RBD usa un espacio de nombres, añade **`--namespace NAMESPACE`** a cada comando `rbd`. Usa el espacio de nombres configurado en la entrada de almacenamiento de Proxmox, no el ID de almacenamiento de Proxmox.

## Ten en cuenta las instantáneas y las copias

**Las instantáneas conservan versiones anteriores de bloques.** Revisa la pestaña **Snapshots** de la VM o CT y el inventario de instantáneas del backend si el uso no baja después de trim. Inspecciona el propietario y las dependencias antes de borrar una. Una copia es otro archivo y sigue la retención del almacenamiento de copias, no el `df` actual del invitado.

**La deduplicación de PBS cambia la contabilidad.** Su almacén de datos contiene fragmentos compartidos entre copias. La poda elimina metadatos de instantáneas de copia. La recolección de basura elimina después los fragmentos sin referencias, tras un período de espera. Comprueba ambas tareas antes de afirmar que se recuperó capacidad de copia. [Documentación de mantenimiento de PBS](https://pbs.proxmox.com/docs/maintenance.html)

> **Advertencia:** Nunca borres un archivo de volumen administrado por Proxmox, un zvol o una instantánea guiándote solo por su nombre. Identifica primero el invitado y la política de retención. La limpieza del almacenamiento debe conservar la copia y la ruta de reversión.

## Reconstruye el archivo de disco con la VM apagada

**Usa conversión sin conexión solo cuando trim normal del invitado y la ruta del backend no resuelvan un problema de asignación qcow2.** Apaga la VM, verifica la copia, identifica las relaciones de instantáneas y cadenas de respaldo, y escribe una imagen de destino separada. QEMU advierte que no se modifique una imagen que otro proceso esté usando. [Documentación de QEMU `qemu-img`](https://www.qemu.org/docs/master/tools/qemu-img.html)

**Prefiere un traslado administrado por Proxmox o el flujo de copia y restauración** cuando el disco tenga instantáneas o resida en almacenamiento de bloques administrado. Ejecutar `qemu-img convert` por separado sobre una imagen propiedad de PVE no actualiza por sí mismo la configuración de VM, la propiedad del volumen ni las referencias a instantáneas. No uses `qemu-img resize --shrink` para recuperar archivos borrados. Reducir la capacidad visible para el invitado arriesga truncar datos si antes no redujiste particiones y sistemas de archivos.

## Diagnostica una recuperación fallida

| Síntoma | Comprobación probable | Siguiente acción |
|---|---|---|
| **Baja `df` del invitado, pero el host no cambia** | Indicador discard de VM, trim del invitado, instantáneas | Verifica la ruta discard completa y las instantáneas retenidas. |
| **`fstrim` indica que no se admite** | Bus de disco del invitado, dispositivos apilados, backend | Inspecciona `lsblk -D`, el kernel del invitado y cada capa intermedia. |
| **Termina Windows ReTrim, pero el host no cambia** | Asignación del backend, instantáneas, contabilidad del servidor | Compara el volumen y el grupo. Confirma que el disco usa almacenamiento thin. |
| **Difieren `ls -lh` y `du -h`** | Archivo sparse o qcow2 | Usa `du` para los bloques asignados del sistema de archivos. |
| **El thin pool LVM sigue alto** | Datos, metadatos, instantáneas | Revisa `lvs` y las instantáneas PVE antes de eliminar nada. |
| **El grupo ZFS sigue alto** | Bloques retenidos por instantáneas y reservas | Revisa `usedbysnapshots`, los ajustes del zvol y la capacidad del grupo. |
| **No coincide `df` del CT con el grupo** | Montajes bind, puntos de montaje, instantáneas | Asocia `rootfs` y cada `mpN` con su propietario en el host. |

**Vuelve a comprobar cuando termine el trabajo en segundo plano.** La contabilidad del almacenamiento puede tardar tras trim, borrar instantáneas o ejecutar la recolección de basura del backend. Compara el espacio libre medido del grupo con el valor inicial. No infieras el éxito solo por el código de salida de un comando del invitado.

## Próximos pasos

**Crea un registro de almacenamiento para cada invitado:** tamaño virtual, bytes asignados, backend, bus, indicador discard, número de instantáneas, cobertura de copia y espacio libre del grupo. Elige una VM, activa la ruta discard compatible, ejecuta trim dentro del invitado y compara los valores registrados. Repite solo cuando el resultado de la primera VM coincida con el comportamiento esperado del backend.

Para planificar mejor la recuperación, sigue el [simulacro de copia y restauración de Proxmox](/articles/proxmox-vm-backup-restore-drill/) y la [guía de actualización de Proxmox VE 8 a 9](/articles/proxmox-ve-8-to-9-upgrade-guide/).

## Fuentes

- [Administración de almacenamiento de Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc), tipos de almacenamiento, aprovisionamiento thin y riesgos de capacidad.
- [Almacenamiento LVM de Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc), cadenas de volúmenes de instantáneas y asignación de VE 9.
- [Almacenamiento RBD de Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc), configuración de grupos y espacios de nombres.
- [Máquinas virtuales de Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/qm.adoc), buses de disco, formatos, discard y agente invitado.
- [Opciones de disco de VM de Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc), indicadores según el bus.
- [Contenedores de Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), sistemas de archivos root y propiedad de puntos de montaje.
- [Comandos de contenedores de Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc), trim de contenedor desde el host.
- [Copias y restauración de Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc), cobertura de copias de VM y CT.
- [documentación de Microsoft para `Optimize-Volume`](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps), sintaxis de ReTrim en Windows.
- [Guía de Red Hat sobre bloques sin uso](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems), comportamiento de Linux `fstrim`.
- [Instantáneas y clones de OpenZFS](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html), bloques retenidos por instantáneas.
- [Referencia de comandos Ceph RBD](https://docs.ceph.com/en/squid/man/8/rbd/), uso e instantáneas de imagen.
- [Especificación NFSv4.2](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2), liberación de espacio en el servidor.
- [Documentación de mantenimiento de PBS](https://pbs.proxmox.com/docs/maintenance.html), poda y recolección de basura.
- [Utilidad de imágenes de disco QEMU](https://www.qemu.org/docs/master/tools/qemu-img.html), seguridad de conversión de imagen sin conexión.
