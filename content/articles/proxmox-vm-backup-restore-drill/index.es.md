---
title: "Prueba de restauración de una VM Proxmox: demuestra que el sistema invitado funciona"
date: 2026-10-11
lastmod: 2026-11-15
toc: true
draft: false
description: "Prueba una copia de seguridad de una VM Proxmox con una restauración aislada. Comprueba los discos incluidos, el modo de copia, los datos del invitado, el estado del servicio y el tiempo de recuperación sin tocar producción."
genre: ["Virtualización", "Copia de seguridad y recuperación", "Laboratorio doméstico"]
tags: ["prueba de restauración de Proxmox", "copia de seguridad de VM Proxmox", "ejercicio de restauración Proxmox", "qmrestore", "vzdump", "verificación de Proxmox Backup Server", "copia de VM con snapshot Proxmox", "prueba de recuperación de VM", "RPO y RTO de copias de seguridad", "restauración aislada de VM", "modo de copia de seguridad Proxmox", "copia con agente invitado"]
cover: "/img/cover/proxmox-vm-backup-restore-drill.webp"
coverAlt: "Una copia pasa de una VM de producción naranja por un almacén hasta una VM de prueba aislada azul. Se comprueban discos, servicios y tiempos."
coverCaption: "Un trabajo de copia completado es el comienzo de una prueba de recuperación."
---

Una tarea de copia de seguridad en verde indica que Proxmox escribió una copia. La tarea no muestra si el invitado arranca, si sus datos están actualizados o si funciona su servicio principal. **Restaura una copia con un ID de VM nuevo en una red aislada.** El resultado aporta pruebas de recuperación antes de que una interrupción te obligue a hacer la prueba.

<!--more-->

Este ejercicio cubre una **máquina virtual de Proxmox VE**. Los contenedores tienen reglas de copia distintas, sobre todo para montajes enlazados y de dispositivos. La [prueba de copia y restauración del homelab](/articles/homelab-backup-restore-drill/) del sitio cubre una recuperación de archivos más amplia. Aquí probarás una copia de Proxmox de una VM y su carga de trabajo.

Un **invitado** es el sistema operativo que se ejecuta dentro de una máquina virtual. Los **montajes enlazados** y los **montajes de dispositivos** exponen recursos del host al invitado. Prueba esos recursos con un plan de recuperación aparte.

## Puntos clave

- **Define el éxito primero:** elige un dato, una comprobación del servicio y un tiempo de recuperación aceptable.
- **Inspecciona la cobertura:** una copia de VM omite los discos marcados como **No backup** y no recrea servicios externos ni datos excluidos.
- **Restaura por separado:** usa un ID de VM libre y mantén la red restaurada aislada de producción.
- **Registra pruebas:** mide la antigüedad de la copia, el tiempo de restauración, el arranque, la presencia de discos y una comprobación real de la aplicación.

## Antes de empezar

Elige una VM cuya copia sea segura para probar. Necesitas acceso de administrador a Proxmox, una copia completada en almacenamiento de archivos o en Proxmox Backup Server (PBS), espacio suficiente para una segunda VM y un bridge aislado o un dispositivo de red desconectado. Un bridge aislado es una red virtual de Proxmox sin ruta a la LAN de producción. Si no tienes uno, utiliza un adaptador desconectado o una VLAN de pruebas. Mantén encendida la VM de producción. Reserva un ID nuevo para la VM, por ejemplo **920**, tras comprobar si otro invitado ya lo usa. Reserva tiempo suficiente para una restauración completa y una prueba de carga de trabajo.

Escribe las condiciones de aprobación antes de restaurar. Para un servidor de archivos, elige un archivo reciente y su suma de comprobación o contenido esperado. Para una base de datos, elige una consulta de solo lectura segura y un registro escrito antes de la copia. Para un servicio web, elige una comprobación local de estado y una página representativa. Registra la fecha más reciente aceptable de los datos, tu **objetivo de punto de recuperación (RPO)**, y el tiempo permitido para recuperar el servicio, tu **objetivo de tiempo de recuperación (RTO)**. Una pantalla de arranque por sí sola no cumple estas comprobaciones.

| Registro | Ejemplo de evidencia |
|---|---|
| **Punto de copia** | Hora del snapshot y último dato esperado |
| **Destino de recuperación** | ID de VM libre, almacenamiento de destino y bridge aislado |
| **Prueba de carga** | Inicio de sesión, montaje de volumen y lectura de la aplicación |
| **Límite de tiempo** | Hora de inicio y fin de la restauración y de la comprobación del servicio |

No conectes el invitado restaurado a la red de producción antes de revisar su nombre, dirección IP, dirección MAC, tareas programadas e integraciones externas. Una identidad copiada podría entrar en conflicto con la VM en ejecución o enviar trabajo duplicado.

## Inspecciona qué cubre la copia

**Alcance de versiones:** estos ejemplos no se ejecutaron al preparar el artículo. Registra la salida de `pveversion --verbose` antes de probar. Usa documentación correspondiente a la versión instalada de Proxmox VE. Registra el backend de almacenamiento, el tipo de invitado y la salida de los comandos en la hoja del ejercicio.

En un nodo Proxmox, el siguiente comando de solo lectura muestra la configuración de la VM de origen. Sustituye **120** por el ID de tu VM de origen:

```bash
qm config 120
```

Enumera cada disco virtual y su opción de copia. La [documentación de discos de VM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) indica que la opción **No backup** excluye un disco de la copia de la VM. Comprueba si los datos de la aplicación están en un disco excluido, un montaje del host, hardware conectado directamente o un servicio remoto. Registra su procedimiento de recuperación independiente. Una prueba de arranque de la VM no demuestra que los datos excluidos estén protegidos.

Comprueba la fecha, el tamaño, el registro de tarea y el almacenamiento de la copia más reciente. En la interfaz de Proxmox, abre la vista **Backups** del almacenamiento o la pestaña **Backup** de la VM. Confirma que la tarea terminó sin errores. La [documentación de copias de Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) distingue los archivos de copia normales del almacenamiento PBS, que conserva fragmentos y metadatos deduplicados.

| Modo de copia | Comportamiento de la VM | Decisión para este ejercicio |
|---|---|---|
| **Snapshot** | Copia una VM en ejecución con poca interrupción. Las escrituras del invitado conllevan un pequeño riesgo de inconsistencia. | Adecuado para pruebas rutinarias si la carga de trabajo tolera este punto de recuperación. |
| **Stop** | Apaga el invitado al iniciar la copia y ofrece la mayor consistencia. | Úsalo cuando la carga de trabajo requiera un apagado limpio y la interrupción sea aceptable. |
| **Suspend** | Suspende antes del modo snapshot y añade interrupción sin una mejora general de consistencia. | No elijas suspend como mejora predeterminada frente a snapshot. |

Estas ventajas e inconvenientes proceden de la [referencia de modos de copia de Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). Un **QEMU Guest Agent** es un servicio dentro del invitado que permite a Proxmox solicitar acciones como congelar y reanudar el sistema de archivos. Un invitado en ejecución con su agente habilitado y en buen estado admite esas acciones durante una copia snapshot. Congelar el sistema de archivos mejora la consistencia, pero no sustituye una comprobación de recuperación específica de la base de datos. Registra el modo real y el estado del agente, en vez de suponer que una tarea programada usa tu configuración preferida.

## Crea o selecciona un punto de recuperación

Usa una copia programada reciente y correcta si el ejercicio prueba una recuperación rutinaria. Si necesitas una copia nueva puntual, abre la pestaña **Backup** de la VM, selecciona **Backup now**, elige el almacenamiento de destino y el modo y espera a que el registro de la tarea indique que finalizó correctamente. Desde una shell de Proxmox, este ejemplo copia la VM **120** al almacenamiento con ID **backup-nfs** en modo snapshot:

```bash
vzdump 120 --storage backup-nfs --mode snapshot
```

Sustituye ambos ID por los tuyos. Ejecuta el comando solo después de confirmar que el almacenamiento acepta copias y tiene espacio para la tarea. La [referencia de `vzdump` de Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) documenta las opciones de modo y almacenamiento. Revisa el registro de la tarea cuando termine el comando. No consideres una copia antigua como punto de recuperación actual solo porque el nombre del archivo parezca reciente.

Si el destino es **PBS**, ejecuta o revisa una tarea de verificación para el datastore seleccionado. La [documentación de verificación de PBS](https://pbs.proxmox.com/docs/maintenance.html) explica cómo comprobar la integridad de los datos y programar verificaciones periódicas. La verificación detecta fragmentos de copia dañados. **Una verificación correcta no demuestra que un sistema operativo restaurado, una aplicación o una dependencia externa funcione.** Continúa con el ejercicio de restauración incluso tras un resultado correcto.

## Restaura en una VM aislada

En la interfaz de Proxmox, selecciona la copia en la vista **Backups** del almacenamiento y elige **Restore**. Introduce un ID de VM libre y el almacenamiento de destino previsto. Deja desactivada la opción **Start after restore**. Revisa la opción para generar una dirección MAC nueva. La [sinopsis oficial de `qmrestore`](https://github.com/proxmox/pve-docs/blob/master/generated/qmrestore.1-synopsis.adoc) define un ID de VM único, la selección de almacenamiento, `--unique` para obtener una dirección Ethernet aleatoria y el valor predeterminado de no iniciar la VM restaurada.

Para un archivo `vzdump`, este comando de shell muestra el patrón equivalente. Sustituye la ruta del archivo, el ID de VM nuevo y el ID de almacenamiento por los valores de tu entorno:

```bash
qmrestore /path/to/vzdump-qemu-120-2026_10_11-02_00_00.vma.zst 920 --storage local-lvm --unique 1
```

La [descripción de restauración de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qmrestore.adoc) indica que, sin un almacenamiento de destino, la restauración intenta usar el almacenamiento original. Define **`--storage`** cuando el almacenamiento antiguo no exista en el nodo de prueba. No uses **`--force`** para un ejercicio. La opción permite sobrescribir una VM existente, mientras que este procedimiento requiere un ID libre. Las copias de PBS también se restauran desde la interfaz de Proxmox. Selecciona la entrada de almacenamiento del snapshot de PBS en vez de tratarlo como un archivo `.vma.zst` local.

Antes del primer arranque, inspecciona todas las interfaces de red restauradas, incluidas las secundarias y las conectadas directamente. Una **dirección MAC** identifica una interfaz de red. **DNS** asigna nombres a direcciones. **DHCP** asigna la configuración de red. Una **VLAN** es una red lógica transportada por hardware compartido. Un **TPM virtual** almacena el estado de seguridad de un invitado. Desconecta todas las interfaces o conéctalas solo a un segmento de prueba aislado. Confirma que no se pueda alcanzar ninguna ruta de producción, ruta DNS, servicio DHCP, red de administración o integración externa. Si la carga necesita otro servicio de prueba, prepara una copia de prueba en la red aislada. Compara con el origen las asignaciones de disco, el firmware, los requisitos del TPM virtual y cualquier dispositivo especial. Los discos externos, dispositivos conectados directamente y secretos almacenados fuera de la VM necesitan planes independientes.

## Prueba el invitado y la carga de trabajo

Inicia la VM restaurada y usa primero su consola. Confirma que el sistema operativo arranca, que se montan todos los volúmenes esperados, que el reloj es correcto y que la aplicación se inicia. Después ejecuta la condición de aprobación que escribiste antes. Compara un dato conocido con su valor y fecha anteriores a la copia. Una solicitud de inicio de sesión o un proceso en ejecución no demuestra por sí solo que el servicio contenga los datos correctos.

| Prueba | Condición de aprobación |
|---|---|
| **Arranque** | El invitado llega a un inicio de sesión normal sin modo de reparación ni solicitudes de recuperación repetidas. |
| **Discos** | Todos los discos incluidos en la copia aparecen, se montan y contienen los datos esperados. |
| **Servicio** | Una solicitud local representativa o una lectura se completa correctamente. |
| **Punto de recuperación** | Los datos restaurados cumplen el RPO registrado. |
| **Tiempo de recuperación** | La restauración, el arranque y la validación del servicio cumplen el RTO registrado. |
| **Aislamiento** | Ninguna dirección, tarea o integración de producción recibe tráfico duplicado. |

Mantén aislado el invitado restaurado mientras inspeccionas tareas programadas, hooks de notificación, agentes de copia y credenciales de la aplicación. No ejecutes una prueba que envíe mensajes reales a clientes o escriba en servicios de producción. Si una comprobación falla, registra la etapa exacta. Distingue entre **fallo de integridad de la copia**, **fallo de arranque de la VM**, **datos ausentes** y **fallo de la aplicación**. Cada problema requiere una corrección distinta.

| Clase de fallo | Evidencia de confirmación | Primera corrección | Nueva prueba |
|---|---|---|---|
| **Integridad de la copia** | La verificación o restauración informa de datos dañados | Selecciona otro punto de recuperación verificado e inspecciona el estado del almacenamiento | Repite la verificación y la restauración |
| **Arranque de la VM** | La consola muestra errores de firmware, disco o recuperación | Compara firmware, asignación de disco y orden de arranque con el origen | Arranca la copia aislada y registra el resultado de la consola |
| **Datos ausentes** | Falta un archivo, volumen o registro de base de datos esperado | Comprueba discos excluidos, montajes, snapshots y dependencias externas | Repite la comprobación del dato o archivo indicado |
| **Aplicación** | El invitado arranca, pero falla la comprobación del servicio | Inspecciona los registros, credenciales, dependencias y pasos de recuperación del servicio | Ejecuta la misma comprobación local de estado y carga |

Proxmox ofrece la [restauración de archivos individuales para copias PBS](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). Úsala para probar una recuperación de archivos cuando la carga necesite un archivo. Un archivo recuperado no sustituye el arranque completo de la VM ni la prueba del servicio. Proxmox también ofrece restauración en vivo desde PBS. Su documentación indica que, si falla una restauración en vivo, la VM queda en un estado indefinido. Para este ejercicio planificado, usa una restauración normal completada.

## Registra el resultado y cierra el ejercicio

Registra el ID de la VM de origen, el almacenamiento de la copia, la fecha de la copia, el modo, el nuevo ID de VM, el almacenamiento de destino, el aislamiento de red, las horas de inicio y fin de la restauración, la prueba de la aplicación, la fecha de los datos y cualquier comprobación fallida. Compara el punto y el tiempo de recuperación medidos con tus objetivos. Un fallo solo aporta pruebas útiles si cambias el plan de copia y repites el ejercicio.

Apaga la VM restaurada cuando terminen las pruebas. Elimina su copia de prueba solo después de guardar el resultado y confirma que la VM de producción sigue funcionando como se espera. Conserva la copia según tu política normal de retención. No cambies la retención para que una sola prueba resulte satisfactoria.

Repite la prueba tras cambios importantes en el almacenamiento, el invitado o la configuración de copia. Alterna entre las VM importantes, incluidas las que tengan discos excluidos o dependencias externas. La [guía de migración de Hyper-V a Proxmox](/articles/hyper-v-to-proxmox-migration-checklist/) exige esta prueba de recuperación antes de retirar una VM de origen. **Una copia útil tiene una ruta de restauración conocida, una carga probada y un punto de recuperación medido.**

## Próximos pasos

Repite el ejercicio tras cambiar el almacenamiento, el invitado o la copia. Consulta la [prueba de copia y restauración del homelab](/articles/homelab-backup-restore-drill/) para recuperación de archivos.
