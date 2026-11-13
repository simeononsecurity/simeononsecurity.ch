---
title: "Realiza un simulacro de restauración de copias de seguridad en tu homelab con Restic"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Comprueba si una copia de seguridad de tu homelab restaura archivos utilizables. Define un objetivo de recuperación, restaura con Restic en otra ubicación, revisa los datos y registra el resultado."
genre: ["Homelab", "Copias de seguridad", "Recuperación ante desastres"]
tags: ["copia de seguridad homelab", "simulacro de restauración", "restauración Restic", "verificación de copias de seguridad", "prueba de recuperación", "recuperación ante desastres", "RPO", "RTO", "repositorio de copias", "comprobación Restic", "copia NAS", "copia de servidor", "recuperación de VM", "restauración de archivos", "cifrado de copias", "supervisión de copias", "plan de recuperación", "prueba de copia", "copia externa", "integridad de datos"]
cover: "/img/cover/homelab-backup-restore-drill.webp"
coverAlt: "Un servidor homelab y un NAS con copia en una unidad separada, una carpeta de restauración verificada en un equipo de prueba aislado y un cronómetro."
coverCaption: "Restaura en un destino separado, revisa los datos y mide el tiempo necesario."
---

Que una tarea de copia indique que terminó correctamente no demuestra que puedas recuperar un archivo utilizable. Un **simulacro de restauración** comprueba el camino desde la copia almacenada hasta los datos funcionales sin reemplazar tus archivos activos. Esta guía usa Restic para mostrar una restauración de archivos y ofrece un registro que puedes repetir después de modificar el laboratorio.

<!--more-->

Restic es un programa de copias de seguridad. Un **repositorio** es el área de almacenamiento protegida que contiene los datos de las copias. Una **instantánea** es un punto guardado de una copia.

## Conclusiones principales

- **Elige un objetivo:** Decide qué archivos o servicio necesitas recuperar y define un punto de recuperación y un tiempo aceptables.
- **Restaura por separado:** Usa un destino de prueba vacío para evitar sobrescribir datos activos.
- **Comprueba el resultado:** Abre los archivos restaurados, verifica los datos de la aplicación cuando sea posible y mide el tiempo transcurrido.
- **Registra los fallos:** Anota el ID de la instantánea, los elementos ausentes, los permisos y las reparaciones junto al plan de recuperación.

## Antes de empezar

Necesitas un repositorio de copias operativo, su contraseña o clave, un destino con espacio suficiente y permiso para leer tanto la copia como la ubicación de prueba. El ejemplo supone que Restic está instalado y que el repositorio contiene una copia reciente de archivos. La [guía de inicio rápido de Restic](https://restic.readthedocs.io/en/stable/010_introduction.html) explica cómo crear un repositorio y hacer las primeras copias. La [guía 3-2-1 de copias de seguridad](/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/) del sitio trata la ubicación de las copias. El [resumen de homelab](/articles/what-is-a-homelab-and-should-you-have-one/) incluye una breve lista para probarlas.

Este simulacro revisa archivos de una instantánea. Una base de datos, una máquina virtual o una aplicación también necesitan pasos de recuperación propios. Mantén aislado el sistema de prueba si iniciar el servicio restaurado puede interferir con el activo. Una copia de archivos correcta no demuestra que todos los servicios vayan a arrancar.

> **Advertencia:** No restaures sobre una ruta activa en la primera prueba. Usa un directorio de prueba vacío en otro sistema de archivos o equipo. No incluyas la contraseña del repositorio en capturas, tickets ni historial de la shell.

## Define el objetivo de recuperación

Anota qué necesitas después de un fallo. El **objetivo de punto de recuperación (RPO)** es el momento hasta el que deben recuperarse los datos tras una interrupción. Representa la pérdida máxima de datos aceptable. El **objetivo de tiempo de recuperación (RTO)** indica cuánto tiempo puede permanecer el servicio fuera de línea. NIST define ambos en su [guía de planificación de contingencias](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-34r1.pdf). Tus objetivos deben reflejar la frecuencia con que cambian los datos y el tiempo que tarda la restauración en tu hardware.

| Elemento | Objetivo ilustrativo | Qué registrar |
|---|---|---|
| **Documentos familiares** | Última copia nocturna | Hora de la última instantánea y archivos abiertos |
| **Configuración del servicio doméstico** | Último cambio conocido como correcto | Versión de configuración y secretos requeridos |
| **Biblioteca multimedia de almacenamiento conectado a la red (NAS)** | Copia semanal | Reproducción de muestra y tiempo de restauración |

Los objetivos anteriores son ejemplos, no resultados medidos. En el plan de recuperación, anota dónde se almacena la copia y cómo una persona autorizada obtiene la contraseña del repositorio o la clave de cifrado. No incluyas valores secretos en el plan ni en el registro del simulacro. Guarda los secretos en una vía protegida e independiente del equipo que podría fallar. Un repositorio que sobrevive pero pierde su única contraseña no se puede recuperar.

Elige un **conjunto de archivos críticos** para este simulacro. Añade un archivo pequeño que sabes que debería estar en la instantánea más reciente. Para un servicio, enumera también la configuración, la exportación de la base de datos, los certificados y la versión de la aplicación necesarios para iniciarlo. Antes de confiar en una copia a nivel de archivos de una base de datos en ejecución, confirma que el método de copia captura datos coherentes.

## Busca una instantánea

Usa el acceso al repositorio aprobado para el simulacro. Restic usa un bloqueo temporal del repositorio mientras lee o modifica datos de copia. Los comandos siguientes suponen que el repositorio permite esta operación de bloqueo. Mantén separadas la fuente activa y el destino de prueba. Sustituye `/path/to/repository` por la ruta real del repositorio Restic y muestra las instantáneas:

```bash
restic -r /path/to/repository snapshots
```

Restic solicita la contraseña del repositorio si no la has proporcionado mediante un método de secretos configurado. Su [lista de instantáneas](https://restic.readthedocs.io/en/stable/010_introduction.html) muestra el ID, la fecha, el host y las rutas de origen. Anota el ID y la fecha y hora que vas a probar. Compara la fecha con tu RPO. El registro reciente de una tarea no sustituye esta comprobación, porque la instantánea necesaria podría ser más antigua de lo esperado.

Si falta la instantánea esperada, detén el simulacro e investiga la planificación de copias, la selección del origen y la ruta del repositorio. No elijas en silencio una instantánea anterior y declares cumplido el objetivo de recuperación.

## Restaura en un destino vacío

Crea un **directorio de destino vacío** en un sistema de archivos de prueba con espacio suficiente para la instantánea. No indiques a Restic que use la fuente original, un recurso compartido de producción montado o una carpeta existente con datos que quieras conservar. Sustituye `SNAPSHOT_ID` y las dos rutas de ejemplo antes de ejecutar el comando:

```bash
restic -r /path/to/repository restore SNAPSHOT_ID \
  --target /path/to/empty-restore-drill
```

La [guía de restauración de Restic](https://restic.readthedocs.io/en/stable/050_restore.html) describe el ID de instantánea y la ruta `--target`. El árbol restaurado conserva la ruta de origen bajo el directorio de destino, así que localiza los archivos reales antes de evaluar el resultado. Si solo necesitas un subconjunto pequeño, usa los [filtros de inclusión documentados](https://restic.readthedocs.io/en/stable/050_restore.html) y anota qué excluiste. No uses `--delete` en un simulacro. Restic indica que esa opción elimina del destino los archivos que no aparecen en la instantánea.

Inicia un cronómetro cuando comience la restauración. Deténlo cuando estén presentes y utilizables los archivos requeridos, no cuando el comando muestre el primer avance. Anota la ubicación del repositorio, la conexión de red, el tamaño de los datos y el equipo de prueba, porque estas condiciones afectan a una recuperación posterior.

> **Resultado esperado:** La instantánea elegida se restaura en un destino separado sin modificar la fuente activa.

## Verifica los datos y el servicio

Abre algunos archivos restaurados con la aplicación que suele leerlos. Incluye uno reciente, uno antiguo y otro de un directorio anidado. Compara tamaños o sumas de comprobación conocidas si las registraste antes de la copia. En Linux, revisa propietario y permisos, ya que una cuenta de prueba puede leer un archivo que la cuenta del servicio no pueda usar.

Para un servicio, restaura en una instancia de prueba aislada. Comprueba su configuración, los secretos necesarios, la coherencia de la base de datos, el inicio y una acción representativa de un usuario. Una restauración de archivos que omite una base de datos o un secreto no recupera el servicio por completo. Nunca inicies la instancia de prueba contra la base de datos activa o una dirección de producción sin un plan controlado de transición.

Ejecuta la comprobación del repositorio de Restic después de restaurar la muestra:

```bash
restic -r /path/to/repository check
```

Para leer todos los datos del repositorio, ejecuta `check --read-data` durante una ventana de mantenimiento. Restic advierte que lee todo el repositorio y puede descargar muchos datos desde un almacenamiento remoto. La [guía de solución de problemas de Restic](https://restic.readthedocs.io/en/stable/077_troubleshooting.html) describe la comprobación y su coste. Una comprobación limpia aporta confianza, pero no sustituye abrir archivos restaurados ni iniciar el servicio.

```bash
restic -r /path/to/repository check --read-data
```

Compara la antigüedad de la instantánea con tu RPO y el tiempo medido de recuperación con tu RTO. Si no cumples alguno, el simulacro ha fallado aunque Restic no haya mostrado errores. Ajusta la frecuencia de las copias, la ubicación del almacenamiento, el ancho de banda o el procedimiento y vuelve a probar.

## Mantén un registro

Después de cada simulacro, escribe un registro breve. El [control de copias de seguridad SP 800-53](https://csrc.nist.gov/CSRC/media/Projects/risk-management/800-53%20Downloads/800-53r5/SP_800-53_v5_1-derived-OSCAL.pdf) de NIST incluye la restauración de funciones de sistemas de muestra como método para probar la recuperación. Un registro repetible permite comprobar si el plan mejora.

| Campo | Resultado que registrar |
|---|---|
| **Fecha y operador** | Cuándo se hizo el simulacro y quién lo hizo |
| **Repositorio e instantánea** | Ubicación, ID, fecha y hora y rutas de origen |
| **Objetivo de recuperación** | Archivos o servicio probado, además de RPO y RTO |
| **Resultado medido** | Antigüedad de la instantánea, tiempo de restauración y comprobaciones de archivos o servicio |
| **Fallos** | Datos ausentes, acceso a claves, permisos, red o problemas de inicio |
| **Siguiente acción** | Responsable, reparación y fecha de la próxima prueba |

No pongas la contraseña del repositorio, la clave de recuperación ni el contenido de archivos sensibles en el registro. Guárdalos en un almacén protegido de secretos y documenta cómo los obtiene una persona autorizada durante una interrupción.

## Solución de problemas

- **No hay contraseña disponible:** Comprueba la vía independiente de custodia de claves. No des por sentado que el equipo averiado estará disponible para recuperar su propia clave.
- **La instantánea es demasiado antigua:** Revisa la planificación, los errores de tareas, las rutas de origen y si el host esperado hizo la copia en otro repositorio.
- **La restauración tarda demasiado:** Mide la velocidad de lectura del almacenamiento, la conexión de red y el volumen de datos. Prueba un subconjunto crítico menor y revisa el RTO o el diseño de recuperación.
- **El archivo existe, pero el servicio falla:** Revisa exportaciones de bases de datos, versión de la aplicación, propietario, permisos, certificados y secretos ausentes.
- **La comprobación del repositorio informa de errores:** Conserva la salida y, si es posible, una copia del repositorio. Sigue la guía de Restic para [investigar daños](https://restic.readthedocs.io/en/stable/077_troubleshooting.html) antes de intentar reparaciones.
- **La prueba cambió datos activos:** Detén el servicio de prueba, verifica los datos de producción y corrige el plan de aislamiento antes de repetir el simulacro.

## Próximos pasos

Repite este simulacro después de cambiar el software de copia, el almacenamiento, las claves de cifrado o los servicios críticos. Alterna conjuntos de archivos y recuperaciones completas de servicios con el tiempo. Mantén una copia independiente según tu [plan 3-2-1](/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/). El objetivo es medir una restauración que puedas repetir cuando el host original ya no esté.
