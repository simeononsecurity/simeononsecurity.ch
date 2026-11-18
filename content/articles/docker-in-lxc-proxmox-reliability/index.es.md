---
title: "Docker en LXC sobre Proxmox: fiabilidad, pruebas y migración a VM"
date: 2026-09-16
lastmod: 2026-11-13
toc: true
draft: false
description: "Evalúa Docker dentro de Proxmox LXC con un fallo documentado de AppArmor, un análisis cuidadoso de un informe sobre bloqueos del host, comandos de diagnóstico y un plan de migración a una VM."
genre: ["Virtualización", "Administración de Linux", "laboratorio doméstico"]
tags: ["Docker en LXC", "Docker en Proxmox", "LXC de Proxmox", "máquina virtual para Docker", "fiabilidad del homelab", "bloqueos del host Proxmox", "máquina virtual Debian para Docker", "contenedores sin privilegios", "anidamiento de contenedores", "aislamiento del kernel de Linux", "AppArmor", "runc", "lxc-pve", "Docker Compose", "controladores de almacenamiento de Docker", "almacén de imágenes de containerd", "presión de memoria", "Linux PSI", "diario persistente", "copias de seguridad de Proxmox", "copias de bind mounts", "migración de VM", "dominios de fallo", "paso de GPU", "solución de problemas del servidor doméstico"]
cover: "/img/cover/docker-lxc-vm-homelab-isolation.webp"
coverAlt: "Ilustración isométrica de un servidor doméstico con cargas de trabajo anidadas y un compartimento separado para una máquina virtual conectada al hardware compartido"
coverCaption: "Ilustración conceptual del hardware compartido y distintos límites de aislamiento de cargas"
---
**Docker dentro de Linux Containers (LXC)** reduce parte del coste de infraestructura, pero aumenta las interacciones entre el entorno de ejecución de las aplicaciones y el host Proxmox. Para los servicios Docker de los que depende tu hogar, una **máquina virtual (VM) Debian** es un punto de partida práctico. Separa el kernel invitado y simplifica el entorno que debes reproducir al investigar un problema. Este artículo analiza el vídeo proporcionado, comprueba el informe de incidente relacionado e incorpora fallos documentados y un plan de migración.

<!--more-->

## Puntos clave

- **Distingue los tipos de fallo:** un error al iniciar Docker, una VM bloqueada y un host físico que no responde requieren investigaciones distintas.
- **Evalúa las pruebas:** la estabilidad posterior a una migración respalda una decisión de recuperación, pero no demuestra la causa original.
- **Consulta la documentación vigente:** la compatibilidad nativa con imágenes OCI y Docker anidado en LXC son vías de despliegue distintas.
- **Protege los datos persistentes:** las copias de seguridad de Proxmox y los archivos Compose no cubren automáticamente todas las ubicaciones de datos de las aplicaciones.
- **Prueba el plan de recuperación:** mide la restauración, el comportamiento tras reiniciar y la disponibilidad del servicio antes de retirar el despliegue anterior.

## Antes de empezar

**Dificultad:** Intermedia. **Público:** administradores de Proxmox que eligen entre Docker anidado y Docker en una VM. Antes de seguir los ejemplos de diagnóstico, debes reconocer un proyecto Compose, un montaje de contenedor y un intérprete de comandos de Linux.

**Esfuerzo estimado:** reserva entre 30 y 60 minutos para el inventario y la recopilación de pruebas. El tiempo de migración depende del tamaño de la base de datos, el rendimiento del almacenamiento, el acceso al hardware y la ventana de interrupción elegida. Los ejemplos siguientes son procedimientos documentados y razonamientos ilustrativos, no mediciones de un laboratorio para este artículo.

| Requisito | Por qué importa |
|---|---|
| **Acceso a la consola del host** | Distingue una caída de red de un bloqueo de todo el host |
| **Copias de seguridad recientes** | Ofrece una vía de recuperación antes de cambiar el despliegue |
| **ID de contenedores y VM** | Dirige los comandos del host a la carga prevista |
| **Inventario de datos de la aplicación** | Identifica volúmenes, montajes enlazados, bases de datos y dependencias externas |
| **Entorno de pruebas separado** | Permite ensayar la migración sin duplicar escrituras de producción |

## Mira el vídeo original

{{< youtube id="XyPBHhZg0Ok" enable="true" title="Proxmox: The Hidden Danger of Running Docker Inside LXC" description="Explicación de Docker anidado en Proxmox LXC, bloqueos intermitentes del host y una migración a máquinas virtuales Debian" uploadDate="2026-09-15T17:00:09-07:00" >}}

**Vídeo original:** [Proxmox: The Hidden Danger of Running Docker Inside LXC](https://www.youtube.com/watch?v=XyPBHhZg0Ok), publicado el 15 de septiembre de 2026 por *Proxmox x Kubernetes x Homelab x Backup*. La pregunta central es cuánta incertidumbre operativa acompaña a una arquitectura que ahorra recursos.

**Límite de las pruebas:** el vídeo relata un incidente y propone lecciones. Las secciones siguientes distinguen las observaciones del propietario, el comportamiento documentado del software y las recomendaciones derivadas.

## Qué demuestra el incidente

El informe original describe un **host con Intel Core i3-13100 y BIOSTAR H610MHP**. El propietario comunicó bloqueos intermitentes que afectaban al acceso de administración y a los servicios LXC. Una pantalla conectada dejó de responder, aunque el informe indica expresamente que syslog seguía generando datos. Esto es más preciso que describir el suceso como totalmente carente de registros. [Informe original del foro de Proxmox](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)

Más tarde, el propietario comunicó una **mejora tras la migración**. En una actualización del 3 de agosto describió el traslado de las cargas Docker a máquinas virtuales Debian y la detención de los LXC que ejecutaban Docker. No se habían observado nuevos bloqueos en el momento de la actualización. El vídeo cita un periodo estable de 16 días. Ninguna afirmación aporta una reproducción controlada ni identifica un componente defectuoso concreto. [Actualización del propietario en el mismo hilo](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)

| Observación | Qué respalda | Qué no demuestra |
|---|---|---|
| **Largo tiempo de actividad inicial** | La combinación anterior de carga y software funcionó correctamente | La fiabilidad tras cada actualización posterior |
| **El host y los servicios se bloquean** | La interrupción supera una sola aplicación | Docker como causa raíz |
| **La migración precede a la mejora** | Una solución operativa útil | Qué interacción modificada eliminó el detonante |
| **Dieciséis días estables** | Un periodo de observación limitado | La resolución de todos los fallos que se repiten cada dos o tres semanas |

El **periodo de observación** merece atención. Dieciséis días caen dentro de un intervalo de recurrencia de 14 a 21 días. Una observación más larga, que abarque varios intervalos anteriores de fallo, cargas comparables y mantenimiento habitual, aumenta la confianza, pero no demuestra una relación causal controlada.

**El éxito operativo y la prueba de la causa raíz** son resultados distintos. Restablecer servicios domésticos fiables es un motivo válido para migrar. Describe el resultado como una mejora observada de la fiabilidad hasta que pruebas más sólidas establezcan el mecanismo.

## Ubica el límite del kernel

```text
Docker dentro de LXC:
Aplicación -> Entorno de ejecución de Docker -> espacios de nombres y políticas de LXC
              -> kernel del host Proxmox -> hardware físico

Docker dentro de una máquina virtual:
Aplicación -> Entorno de ejecución de Docker -> kernel Linux invitado
              -> hardware virtual / KVM-QEMU
              -> kernel del host Proxmox -> hardware físico
```

**LXC** utiliza el kernel del host. Los espacios de nombres, grupos de control, capacidades, seccomp y perfiles de seguridad restringen procesos sin proporcionar un kernel independiente. Añadir Docker dentro de LXC crea otra capa de administración de contenedores para cargas que usan el mismo kernel subyacente del host. [Arquitectura y funciones de contención de LXC](https://linuxcontainers.org/lxc/introduction/)

Una **VM** añade un kernel invitado. Un fallo del kernel invitado suele afectar a esa VM, mientras Proxmox sigue administrando los demás invitados. La VM aún depende del host físico, el hipervisor, el almacenamiento y la red. Los fallos de hardware y los defectos del kernel del host siguen siendo dependencias compartidas.

| Límite | Docker dentro de LXC | Docker dentro de una VM |
|---|---|---|
| **Kernel que usan las aplicaciones** | Kernel del host Proxmox | Kernel invitado |
| **Entorno del runtime de Docker** | Restringido por la política del contenedor externo | Instalado en un sistema operativo invitado convencional |
| **Actualizaciones del kernel invitado** | Vinculadas al kernel del host | Administradas dentro del invitado |
| **Caída del host físico** | Detiene las cargas dependientes | Detiene las cargas dependientes |

Una VM limita **parte de la propagación de fallos**, pero no toda. El cierre inesperado de un proceso de aplicación dentro de LXC no bloquea automáticamente Proxmox. Del mismo modo, colocar todos los servicios domésticos en una sola VM Docker los agrupa detrás de un sistema operativo invitado y un calendario de mantenimiento comunes.

Para una **comparación conceptual más amplia**, consulta [Contenedores Docker frente a máquinas virtuales](/articles/docker-vs-vms/). Aquí la decisión trata sobre la ubicación de Docker dentro de Proxmox y los límites de diagnóstico resultantes.

## Define el soporte con precisión

**«No compatible»** requiere nombrar un componente y una versión. Distingue entre un despliegue recomendado por el proveedor, funciones documentadas, mantenimiento de la distribución y un derecho contractual de soporte. Que una pila anidada funcione no demuestra que todas sus combinaciones reciban las mismas pruebas. Una recomendación de usar VM tampoco significa que los mantenedores rechacen todos los errores relacionados con el anidamiento.

**La documentación actual de Proxmox** establece otra distinción importante. El código fuente del conjunto de herramientas de contenedores describe el soporte de imágenes de aplicaciones **Open Container Initiative (OCI)** como una vista previa tecnológica, en la que las imágenes se convierten al marco LXC. Para requisitos que priorizan el aislamiento y la migración en vivo, también recomienda contenedores dentro de una VM QEMU. Importar una imagen OCI a ese marco difiere de instalar Docker Engine y ejecutar Compose dentro de un invitado LXC. [Documentación del conjunto de herramientas de contenedores Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

| Despliegue | Pregunta que comprobar |
|---|---|
| **Invitado LXC tradicional** | ¿Se ajustan su plantilla de sistema operativo y su aplicación a las restricciones documentadas para contenedores? |
| **Docker anidado en LXC** | ¿Qué combinaciones de kernel, runtime, política de seguridad y almacenamiento se han probado? |
| **Importación nativa de imágenes OCI** | ¿La versión instalada de Proxmox ofrece la función documentada y el comportamiento requerido? |
| **Docker dentro de una VM Debian** | ¿La versión del invitado cumple los requisitos de instalación de Docker? |

Docker publica una **vía de instalación para Debian**. Usa la lista de versiones compatibles y las instrucciones del repositorio para el invitado. Registra las versiones instaladas en vez de asumir que una guía antigua sigue vigente. Esto proporciona una base de instalación documentada, no una garantía de disponibilidad ni un contrato automático de soporte de pago. [Docker Engine en Debian](https://docs.docker.com/engine/install/debian/)

## Un fallo de anidamiento confirmado

La **incompatibilidad entre runc y AppArmor de 2025** es un ejemplo verificable. Los mantenedores de runc documentaron un fallo al volver a abrir un descriptor dentro de un contenedor externo con un perfil AppArmor. AppArmor interpretó erróneamente un acceso a **`/proc/sys`** como un acceso a **`/sys`**, por lo que la política lo denegó. [Incidencia runc 4968](https://github.com/opencontainers/runc/issues/4968)

Un **inicio afectado** notificó este fragmento de error:

```text
open sysctl net.ipv4.ip_unprivileged_port_start file: reopen fd 8: permission denied
```

El fallo registrado impidió el **inicio del contenedor**. No explica los bloqueos del host descritos por el propietario en el foro. La incidencia recoge **`lxc-pve 6.0.5-2`** como solución de Proxmox para este problema concreto, y el cambio correspondiente de LXC se integró el 20 de noviembre de 2025. *Son referencias a soluciones históricas, no una recomendación de fijar un paquete en una instalación actual.* [Resumen de la solución por los mantenedores](https://github.com/opencontainers/runc/issues/4968), [cambio de LXC integrado](https://github.com/lxc/lxc/pull/4609)

La lección es la **coordinación de dependencias**. Un cambio de seguridad del runtime interactuó con la política del contenedor externo y la solución requirió trabajo en otra capa. Prefiere la actualización mantenida adecuada para tu versión, en lugar de desactivar AppArmor de forma permanente o conservar un runtime antiguo y vulnerable.

> **Idea clave:** este incidente demuestra un problema real de compatibilidad con contenedores anidados y una respuesta real de los mantenedores. No demuestra una inestabilidad universal de LXC ni la causa de otro bloqueo del host.

## Compara los costes reales

Mide la eficiencia con tu **carga de trabajo real**. En condiciones equivalentes, compara la presión de memoria del host, la demanda de CPU, la latencia del almacenamiento, los tiempos de respuesta de la aplicación y el esfuerzo de recuperación. La RAM asignada a una VM, la memoria libre del invitado y la memoria residente del host son medidas distintas.

| Ahorro afirmado | Medición que recopilar | Coste adicional que registrar |
|---|---|---|
| **Menor sobrecarga de memoria** | Uso y presión de memoria del host con la misma carga | Tiempo de administrar límites anidados y diagnosticar contención |
| **Despliegue más rápido** | Tiempo hasta tener un servicio funcional con los datos restaurados | Tiempo de reconstrucción tras una actualización fallida |
| **Uso compartido del hardware más sencillo** | Dispositivos necesarios, permisos y funcionamiento correcto de la aplicación | Dependencia de controladores del host y restricciones de migración |
| **Copias de seguridad más sencillas** | Restauración satisfactoria de todos los datos necesarios | Montajes externos y consistencia de la aplicación |

Docker permite por defecto un **uso sin restricciones de CPU y memoria**, salvo que se apliquen límites. En LXC, el contenedor externo añade sus propios límites. En una VM, la asignación al invitado crea otro límite de capacidad. El invitado también necesita recursos para el sistema operativo, Docker, las cachés y los picos de demanda de las aplicaciones. [Restricciones de recursos de Docker](https://docs.docker.com/engine/containers/resource_constraints/)

**El acceso al hardware** es un requisito de la carga. Compartir un dispositivo gráfico del host con un contenedor y asignar un dispositivo PCI a una VM implican configuraciones distintas de controladores y aislamiento. Antes de elegir, concreta el dispositivo y la necesidad de la aplicación. Por ejemplo, una carga multimedia que requiera decodificación por hardware debe superar una prueba de decodificación tras la migración, además de las comprobaciones HTTP habituales.

Evita las **cifras universales de sobrecarga**. Este artículo no ofrece un coste fijo de RAM ni un porcentaje de rendimiento, porque esos valores requieren una carga, una configuración y un método de medición controlados. Usa un resultado observado de tu propia comparación en el registro de decisiones que aparece más abajo.

## Recopila pruebas por capas

**Empieza en el host Proxmox** con un shell administrativo. Sustituye **`101`** por el ID del LXC que investigas:

```bash
pveversion -v
uname -r
pct config 101
journalctl --list-boots
journalctl -k -b -1 --no-pager
```

**`pveversion -v`** registra las versiones de los componentes Proxmox instalados. **`pct config`** registra la configuración del contenedor externo. En **`journalctl`**, **`-k`** selecciona los mensajes del kernel, **`-b -1`** el arranque anterior y **`--no-pager`** produce texto normal en el terminal. Los mensajes del arranque anterior requieren datos del diario conservados. [Conjunto de herramientas Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), [referencia de journalctl de systemd](https://github.com/systemd/systemd/blob/main/man/journalctl.xml)

**Después inspecciona el host Docker**, dentro del LXC o VM que ejecuta su daemon:

```bash
docker version
docker info
docker compose version
docker ps -a
docker stats --no-stream
```

Registra **ambos entornos**. La etiqueta de imagen del contenedor por sí sola no indica Docker, containerd, runc, el kernel del host, la política de seguridad ni el backend de almacenamiento. Anota la hora del incidente, las actualizaciones recientes y si respondió la consola local. Elimina credenciales y datos privados de aplicaciones antes de publicar material de diagnóstico.

**Inspecciona una carga específica** y sustituye **`app`** por el nombre de su contenedor:

```bash
docker inspect --format '{{json .State}}' app
docker inspect --format '{{.RestartCount}}' app
docker inspect --format '{{json .Mounts}}' app
```

**`docker inspect`** muestra el estado, el número de reinicios y la información de montajes del contenedor indicado. Trata el recuento de reinicios como una pista que debes correlacionar con los registros, no como prueba de un defecto del host. Un contenedor recreado también empieza un historial nuevo. [Referencia de docker inspect](https://docs.docker.com/reference/cli/docker/inspect/)

## Distingue la presión de los bloqueos

**Captura información de presión de Linux en el host** mientras se desarrolla el problema:

```bash
cat /proc/pressure/cpu
cat /proc/pressure/memory
cat /proc/pressure/io
```

**Pressure Stall Information**, o PSI, informa del tiempo que pierden las tareas mientras esperan recursos. Los campos **`some`** y **`full`** describen condiciones de bloqueo distintas, mientras que **`avg10`**, **`avg60`** y **`avg300`** resumen intervalos recientes. La presión de memoria no equivale a la memoria ocupada: una caché grande por sí sola no demuestra una escasez. [Documentación de PSI de Linux](https://docs.kernel.org/accounting/psi.html)

| Prueba | Interpretación útil | Siguiente comprobación |
|---|---|---|
| **Un contenedor se detiene repetidamente** | Fallo de la aplicación o del runtime del contenedor | Estado de salida, registros del servicio, política de reinicio |
| **SSH falla, la consola funciona** | Fallo de red o de la vía de administración | Estado del enlace, controlador NIC, puente, cortafuegos |
| **La Memory PSI aumenta bajo carga** | Las tareas pierden tiempo por contención de memoria | Límites, actividad de recuperación, registros OOM, crecimiento de la carga |
| **Se bloquean las solicitudes de almacenamiento** | Una dependencia de E/S retrasa el trabajo | Estado del dispositivo, registros de almacenamiento, latencia y colas |
| **Watchdog informa de un lockup** | El detector del kernel observó una condición de bloqueo definida | Traza completa, versión del kernel, detonante reproducible |
| **No hay una última entrada de registro** | La recopilación terminó antes de que llegara información útil | Captura persistente o externa antes de que se repita |

Un **informe de lockup de Linux** tiene un significado técnico. Los watchdogs del kernel distinguen bloqueos suaves y duros. Un tiempo de espera agotado del navegador no demuestra ninguno. La falta de un informe del watchdog tampoco demuestra que el host estuviera sano. [Documentación del detector de lockups de Linux](https://docs.kernel.org/admin-guide/lockup-watchdogs.html)

**Los cambios de firmware y de estados de energía** son experimentos. Registra la configuración anterior, el motivo del cambio y el periodo de observación. Desactivar un estado inactivo de la CPU cambia el consumo y el comportamiento térmico. Un informe sobre otra máquina no basta para recomendar la misma configuración de forma universal.

## Conserva registros útiles

**El registro persistente** aumenta la posibilidad de conservar pruebas tras un reinicio. Un archivo de configuración de journald usa este ajuste:

```ini
[Journal]
Storage=persistent
```

**`Storage=persistent`** solicita almacenar el diario en disco cuando está disponible. Configura la retención y el espacio de disco disponible; después, verifica que los arranques anteriores aparezcan en **`journalctl --list-boots`**. El registro persistente aún depende de que el host complete las escrituras antes del fallo. [Configuración de systemd journald](https://github.com/systemd/systemd/blob/main/man/journald.conf.xml)

**La observación externa** aporta otra perspectiva. Supervisa el servicio desde otro equipo y registra las horas. Un monitor que se ejecuta en el host Proxmox que falla desaparece durante la misma interrupción, por lo que ayuda menos a distinguir una caída de una pérdida de telemetría.

**Prueba ilustrativa:** programa una comprobación HTTP ligera desde otro sistema y compara los fallos con la disponibilidad del host y el comportamiento de la consola local. Un tiempo de espera de la aplicación mientras el host responde exige una investigación distinta de un fallo simultáneo de la aplicación, la administración y la consola. Es un diseño de diagnóstico, no un resultado observado en el incidente original.

## Planifica una migración controlada

Empieza con **un proyecto Compose de bajo riesgo**. Prepara una VM Debian con una versión incluida en la documentación de instalación de Docker, configura copias de seguridad y asigna recursos. Conserva el despliegue original para volver atrás hasta que el reemplazo supere las pruebas. [Instrucciones de instalación de Docker para Debian](https://docs.docker.com/engine/install/debian/)

**Haz un inventario del proyecto Compose** desde su directorio de trabajo:

```bash
docker compose config --quiet
docker compose config --images
docker compose config --volumes
```

**`--quiet`** valida la configuración sin mostrarla. **`--images`** enumera las imágenes mencionadas y **`--volumes`** los volúmenes con nombre. Estos comandos no exportan los datos de la aplicación ni proporcionan un inventario completo de montajes enlazados. Revisa también el archivo Compose y los montajes de cada contenedor. [Referencia de Docker Compose config](https://docs.docker.com/reference/cli/docker/compose/config/)

| Datos o dependencia | Acción de migración |
|---|---|
| **Definiciones Compose** | Transfiere los archivos del proyecto y conserva la configuración probada |
| **Secretos y entorno** | Recrea los valores necesarios mediante el proceso elegido para administrar secretos |
| **Volúmenes con nombre** | Haz copias y restaura su contenido mediante procedimientos coherentes con la aplicación |
| **Rutas con montajes enlazados** | Transfiere o vuelve a conectar los datos de origen y verifica la propiedad |
| **Bases de datos** | Usa el procedimiento de copia/restauración admitido o una copia con las escrituras detenidas |
| **Dispositivos y recursos compartidos** | Restablece el acceso y prueba el comportamiento de la aplicación |
| **Puertos y DNS** | Prepara la dirección de reemplazo y planifica el cambio |

Los **volúmenes** sobreviven a los contenedores, pero no migran por sí solos. Un archivo Compose nombra los recursos y define los servicios. La documentación de volúmenes de Docker describe operaciones separadas de copia y restauración del contenido persistente. No des por hecho que recrear el proyecto restaura los datos. [Ciclo de vida y copias de los volúmenes Docker](https://docs.docker.com/engine/storage/volumes/)

Comprueba por separado la **cobertura de las copias de Proxmox**. La documentación excluye el contenido de dispositivos y montajes enlazados de las copias de contenedores. Por tanto, una copia correcta del sistema de archivos raíz de LXC no demuestra que estén protegidos todos los directorios expuestos dentro. [Documentación de copias de seguridad de Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

### Comprueba el almacenamiento antes de copiar

**Inspecciona la configuración de almacenamiento real de Docker** en cada host Docker:

```bash
docker info
findmnt -T /var/lib/docker
```

**`findmnt`** identifica el sistema de archivos que contiene la ruta indicada. Sustituye **`/var/lib/docker`** si el daemon usa otra raíz de datos y revisa la ruta de almacenamiento de containerd cuando corresponda. Docker documenta la diferencia entre el almacén de imágenes containerd y los controladores de almacenamiento clásicos, con requisitos específicos para cada backend. [Selección del backend de almacenamiento de Docker](https://docs.docker.com/engine/storage/drivers/select-storage-driver/)

**Recrea las imágenes y restaura los datos de la aplicación** mediante los procedimientos documentados del backend elegido. Copiar un directorio de datos Docker activo entre distintas configuraciones de almacenamiento añade supuestos sobre metadatos, estado de montajes y consistencia. No es lo mismo que hacer una copia del volumen de datos de una aplicación detenida.

### Cambia con una opción de vuelta atrás

1. **Ensaya la restauración** en la VM con direcciones independientes y datos de prueba cuando corresponda.
2. **Detén las escrituras de producción** durante la ventana acordada y haz la última copia coherente.
3. **Restaura y valida** los datos de la aplicación, los permisos, las credenciales y el acceso necesario al hardware.
4. **Cambia el enrutamiento del servicio** después de que el reemplazo supere las comprobaciones específicas de la aplicación.
5. **Mantén detenido el despliegue original** y conserva su configuración y datos de recuperación.
6. **Documenta cómo revertir los datos** escritos después del cambio antes de reiniciar el sistema anterior.

Evita **dos procesos de escritura activos** sobre el mismo almacenamiento de base de datos. Volver atrás después de nuevas escrituras de producción requiere un plan para conservarlas o descartarlas de forma deliberada. Reiniciar un contenedor antiguo no reconcilia dos historiales de datos divergentes.

## Prueba algo más que el tiempo activo

Las **pruebas de aceptación** deben responder al propósito del servicio. Un estado correcto del contenedor solo demuestra que hay un proceso en ejecución. Un servicio utilizable también requiere sus datos, acceso a la red, dependencias y capacidad de recuperación.

| Prueba | Evidencia que conservar |
|---|---|
| **Función de la aplicación** | Una transacción, consulta u operación multimedia real satisfactoria |
| **Integridad de los datos** | Registros, archivos, permisos y cambios recientes esperados |
| **Reinicio del invitado** | Los servicios vuelven sin reparación manual |
| **Restauración de una copia** | La copia restaurada supera la misma prueba funcional |
| **Carga representativa** | Latencia, CPU, presión de memoria y comportamiento del almacenamiento |
| **Ensayo de mantenimiento** | Una actualización probada y un procedimiento de recuperación utilizable |
| **Observación prolongada** | Registros de disponibilidad que cubren varios intervalos de fallo anteriores |

**Decisión de ejemplo:** un servicio de cámaras y un descargador experimental comparten una pila anidada. Trasladarlos a una VM mejora la separación de kernel, pero mantiene un límite común de mantenimiento del invitado. Si la prioridad es la disponibilidad de las cámaras, evalúa grupos de mantenimiento y límites de recursos separados, y después prueba que la grabación continúe durante las actualizaciones del descargador.

**Razonamiento esperado:** elige la ubicación según la dependencia del servicio que necesitas aislar. Dos VM en el mismo servidor físico siguen compartiendo energía, almacenamiento y kernel del host. Si el requisito incluye sobrevivir a la caída del servidor, el diseño necesita otro sistema independiente o una alternativa manual aceptable.

## Crea un registro de decisiones

**Usa pruebas medidas** para elegir un despliegue y definir cuándo volver a evaluarlo:

```text
Impacto en el servicio y el hogar:
Versiones actuales de host / kernel / LXC / Docker:
Acceso requerido a GPU, dispositivos y red:
Memoria, CPU, almacenamiento y latencia medidos:
Señal de fallo conocida e intervalo de recurrencia:
Cobertura de copias de seguridad y prueba de restauración satisfactoria:
Arquitectura elegida y motivo:
Ventana de interrupción permitida y objetivo de recuperación:
Procedimiento de cambio y reversión de datos posterior al cambio:
Pruebas de aceptación y periodo de observación:
Condición que exige volver a revisar la arquitectura:
```

**Elige Docker anidado en LXC de forma deliberada** cuando sus ventajas justifiquen el trabajo de integración y hayas probado la recuperación. Elige una VM cuando un entorno Docker invitado convencional y un kernel invitado separado simplifiquen el funcionamiento del servicio. Ninguna decisión sustituye las copias de seguridad, la supervisión ni el mantenimiento del host.

## Revisa el cambio antes de migrar

Trata la migración como un **cambio controlado**, no como prueba de la causa del incidente original. Antes del cambio, registra la configuración actual del contenedor, los resúmenes de las imágenes, las rutas de montajes enlazados, las claves del entorno, las asignaciones de dispositivos y la última restauración satisfactoria. Después, compara las mismas comprobaciones de servicio y mediciones de recursos. Mantén detenida la carga anterior hasta que la nueva supere su periodo de aceptación.

Si el incidente vuelve tras la migración, compara el kernel del host, el almacenamiento, la presión de memoria, el acceso a dispositivos y las versiones de Docker de ambos despliegues. La comparación acota la investigación. Una migración satisfactoria no se convierte en un experimento causal si las variables relevantes no se mantuvieron bajo control.

## Próximos pasos

**Empieza por inventariar un servicio.** Identifica sus datos persistentes, dependencias físicas, síntomas de fallo y objetivo de recuperación. Ensaya una restauración antes de decidir si hace falta migrar.

Para **temas relacionados**, consulta la [guía de actualización de Proxmox VE](/articles/proxmox-ve-8-to-9-upgrade-guide/) para planificar actualizaciones y la [guía de seguridad para Docker y Kubernetes](/articles/how-to-secure-your-docker-and-kubernetes-environment/) para reforzar las cargas. Mantén la selección de arquitectura, la ejecución de actualizaciones y el diagnóstico de incidentes como decisiones separadas, cada una con sus propias pruebas.

## Fuentes y pruebas

**Investigación revisada:** 16 de septiembre de 2026. La transcripción proporcionada orientó el tema. Los metadatos del vídeo, el informe original, la incidencia upstream y la documentación oficial se comprobaron por separado. El texto identifica los ejercicios ilustrativos y los pasos de validación propuestos.

| Fuente | Función |
|---|---|
| **[Vídeo original](https://www.youtube.com/watch?v=XyPBHhZg0Ok)** | Explicación original e intervalo de estabilidad comunicado |
| **[Hilo del incidente de Proxmox](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)** | Observaciones de primera mano y seguimiento de la migración |
| **[Conjunto de herramientas de contenedores Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)** | Arquitectura de contenedores y distinción actual de OCI |
| **[Incidencia runc 4968](https://github.com/opencontainers/runc/issues/4968)** | Fallo de inicio documentado y solución histórica del paquete |
| **[Solicitud de incorporación de LXC 4609](https://github.com/lxc/lxc/pull/4609)** | Cambio upstream de AppArmor incorporado |
| **[Documentación de Docker](https://docs.docker.com/engine/install/debian/)** | Base de instalación del invitado, con referencias específicas al runtime y al almacenamiento |
| **[Documentación de PSI de Linux](https://docs.kernel.org/accounting/psi.html)** | Interpretación de la presión sobre recursos |
| **[Documentación del watchdog de Linux](https://docs.kernel.org/admin-guide/lockup-watchdogs.html)** | Condiciones de bloqueo definidas por el kernel |
| **[Documentación de copias de seguridad de Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)** | Exclusiones de montajes de contenedor y comportamiento de las copias |
