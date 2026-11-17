---
title: "Dimensiona un SAI para tu homelab y prueba el apagado automático"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Mide el consumo de tu homelab, compara los límites en vatios y VA del SAI, comprueba la autonomía con tu carga y prueba un apagado limpio antes de confiar en la batería."
genre: ["Laboratorio doméstico", "Protección eléctrica", "Administración de sistemas"]
tags: ["SAI para homelab", "dimensionamiento de SAI", "autonomía del SAI", "apagado automático", "Network UPS Tools", "vatios del SAI", "VA del SAI", "factor de potencia", "respaldo de batería", "apagado de servidor", "apagado de NAS", "corte eléctrico", "prueba de SAI", "curva de autonomía", "medidor de potencia", "monitorización del SAI", "reemplazo de batería", "protección contra sobretensiones", "apagado ordenado", "alimentación del homelab"]
cover: "/img/cover/ups-runtime-sizing-shutdown-test.webp"
coverAlt: "Un SAI del homelab alimenta un servidor, un NAS, un router y un switch sobre una línea temporal desde el corte eléctrico hasta el apagado."
coverCaption: "Mide la carga, comprueba la autonomía y prueba el apagado antes de un corte eléctrico."
---

Un **SAI**, o sistema de alimentación ininterrumpida, da tiempo al homelab para guardar el trabajo y apagar los sistemas durante un corte eléctrico. Su etiqueta no indica por sí sola cuánto tiempo funcionarán los servidores. Necesitas conocer la carga de los equipos, los límites en vatios y VA del SAI, una estimación de autonomía para esa carga y un procedimiento de apagado probado.

## Puntos clave

- **Mide la carga:** Registra los vatios normales y máximos de cada dispositivo que quieras mantener conectado a la batería.
- **Comprueba ambos valores:** El SAI debe cumplir los requisitos en vatios y VA de los equipos conectados.
- **Consulta la curva de autonomía:** La autonomía depende de la carga y del estado de la batería. Usa una estimación específica del modelo.
- **Prueba el apagado:** Confirma que la señal del SAI llega a cada host y que los hosts se detienen antes de que se agote la batería.

## Antes de empezar

Necesitas un medidor de potencia adecuado para la red eléctrica local, una lista de dispositivos y adaptadores de alimentación, y acceso a las especificaciones y a la curva de autonomía de cada modelo de SAI que estés considerando. Para probar el apagado automático, también necesitas una conexión USB o de gestión de red compatible y software para cada host. Reserva tiempo para medir con carga normal, observar con carga alta y realizar una prueba de mantenimiento planificada. Es una tarea de nivel intermedio para un homelab porque una prueba completa de apagado interrumpe los servicios.

La [guía de protectores contra sobretensiones](/articles/protecting-your-tech_-the-best-surge-protectors/) del sitio trata la protección frente a sobretensiones. La [comparativa de modelos de SAI](/articles/best-ups-models-for-uninterrupted-connectivity/) enumera productos. Esta guía se centra en dimensionar y verificar tu propia carga. Tanto la [guía de dimensionamiento de SAI de Eaton](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/ups-sizing-guide.html) como la [guía de compra de Schneider Electric](https://www.se.com/us/en/work/support/product-support/ups-buying-guide-for-selecting-a-battery-backup-system/) distinguen la capacidad de salida de la autonomía de la batería.

> **Advertencia:** Usa solo las tomas y cargas que apruebe el fabricante del SAI. Mantén la prueba dentro de la capacidad nominal del SAI. Una prueba real de apagado detiene el laboratorio conectado.

## Mide lo que debe permanecer encendido

Decide qué dispositivos deben funcionar hasta el apagado. Incluye el hipervisor, el almacenamiento, el switch de red y el router si algún host necesita acceso a la red para recibir la señal de apagado. Deja fuera de las tomas respaldadas por batería los monitores, impresoras y otras cargas opcionales, salvo que tu plan las necesite.

Mide en el enchufe el grupo de dispositivos que quieres mantener con batería. Registra los **vatios normales** y el valor máximo observado durante una actividad representativa, como arrancar hosts o máquinas virtuales. La etiqueta de una fuente de alimentación indica su capacidad, no el consumo medido del sistema. Aun así, revisa las etiquetas de los dispositivos para conocer los límites de entrada y de corriente de arranque. Anota las condiciones de medición en tu hoja de trabajo.

| Dispositivo | Vatios normales | Pico observado en vatios | ¿Toma con batería? |
|---|---:|---:|---|
| **Router y switch** | 30 | 35 | Sí |
| **NAS** | 60 | 90 | Sí |
| **Servidor pequeño** | 90 | 135 | Sí |
| **Total ilustrativo** | **180** | **260** | Tres dispositivos |

Los valores anteriores son **ilustrativos**, no mediciones de un laboratorio concreto. Tu carga cambia según los discos, las GPU, los ajustes de energía y los equipos conectados. Vuelve a medir tras cambios importantes de hardware.

## Compara la potencia activa y la potencia aparente

Los **vatios** describen la potencia real que usan los equipos. Los **voltioamperios (VA)** describen la potencia aparente. La relación depende del **factor de potencia**: los vatios divididos por el factor de potencia equivalen a VA. Eaton explica este cálculo en su [guía de dimensionamiento](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/ups-sizing-guide.html). No interpretes una etiqueta de 1000 VA como 1000 vatios. Comprueba la capacidad independiente en vatios del SAI.

Para la carga máxima ilustrativa de 260 W, un margen de capacidad del 25 % da **325 W**. Schneider Electric recomienda una potencia de salida aproximadamente [entre un 20 % y un 25 % superior a la carga](https://www.se.com/us/en/work/support/product-support/ups-buying-guide-for-selecting-a-battery-backup-system/). Elige un SAI cuya potencia continua en vatios supere el pico previsto más el margen. Si conoces el factor de potencia combinado, divide los vatios máximos por ese factor para estimar los VA máximos y aplica también el margen elegido a los VA. Si no, usa un medidor adecuado o el selector del fabricante para determinar los VA requeridos y el margen. No inventes un factor de potencia que no hayas medido.

El margen de capacidad no determina la autonomía. Un SAI con un límite alto de vatios pero una batería pequeña podría alimentar la carga durante poco tiempo. Antes de elegir un modelo, comprueba las tomas, el tipo de enchufe, la tensión de entrada, la interfaz de comunicaciones y la opción de reemplazo de batería.

## Define un objetivo de autonomía

Anota cuánto tiempo necesita el laboratorio para detenerse de forma segura. Incluye el tiempo para que la alerta de apagado llegue a los hosts, se detengan las máquinas virtuales, el almacenamiento vacíe las escrituras y el SAI corte la salida. Añade margen para un apagado lento y una batería antigua. Un laboratorio pensado para superar cortes breves necesita un objetivo distinto de uno que solo debe apagarse correctamente.

Como **ejemplo**, supón que un apagado probado dura 6 minutos y eliges 5 minutos de reserva. La autonomía necesaria con la carga prevista es de al menos 11 minutos. Es un ejemplo de planificación, no un umbral universal. Compara el objetivo con la curva de autonomía o el selector del modelo candidato usando tu **carga normal y máxima medida**, y revisa el resultado a medida que envejece la batería. El [selector de SAI de Schneider Electric](https://www.se.com/us/en/work/products/tools/ups-selector/) calcula la autonomía según la carga indicada y las especificaciones del modelo. Eaton también remite a los datos de autonomía específicos de cada modelo en su [guía de SAI de escritorio](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/desktop-ups-buying-guide.html).

Copia esta **hoja de trabajo** para tu laboratorio. Completa las filas de dispositivos a partir de las lecturas del medidor. Suma los vatios normales y máximos, añade el margen elegido al total máximo y aplica el mismo margen a los VA máximos medidos o calculados. Compara ambos resultados con un SAI candidato. Si usas el selector de un fabricante, anota su resultado de dimensionamiento VA y el margen. Usa la curva del modelo para estimar la autonomía. Completa las filas de tiempos y recuperación durante la prueba.

| Campo | Tu resultado |
|---|---|
| **Dispositivos y tomas con batería** | Nombres de los dispositivos y toma asignada a cada uno |
| **Vatios normales por dispositivo y total** | Valores medidos y suma |
| **Vatios máximos por dispositivo y total** | Valores máximos observados y suma |
| **Factor de potencia medido o especificado** | Valor y fuente, o «desconocido» |
| **VA máximos medidos o calculados** | Vatios máximos divididos por el factor de potencia combinado, si se conoce |
| **Margen de capacidad** | Porcentaje elegido y vatios/VA después del margen |
| **Valores nominales del SAI candidato** | Modelo, vatios y VA de salida, y límites de las tomas |
| **Objetivo de autonomía y estimación de la curva** | Minutos necesarios y estimación del modelo con tu carga |
| **Tiempos de alerta y apagado** | Hora de la alerta de batería y parada del último host |
| **Resultado de recuperación** | Arranque de hosts, almacenamiento, aplicaciones y monitorización |

Si el factor de potencia es desconocido, usa el selector del fabricante o mide la potencia aparente con un medidor adecuado. No indiques un valor VA calculado a partir de un factor supuesto. La hoja está completa solo cuando el modelo cumple ambos límites de salida y su autonomía estimada supera el objetivo de apagado.

> **Resultado esperado:** La hoja identifica los dispositivos conectados, las cargas medidas, los límites en vatios y VA del SAI, el objetivo de autonomía y una estimación específica del modelo.

## Planifica el apagado automático

Un SAI mantiene los equipos encendidos temporalmente. El host sigue necesitando una **señal de apagado**. Comprueba si el SAI ofrece USB, una tarjeta de gestión de red u otra interfaz compatible. Asegúrate de que cada host que deba detenerse tenga una ruta de monitorización compatible. Eaton indica que muchos modelos admiten comunicaciones USB o de red para un [apagado limpio de NAS o servidores](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/desktop-ups-buying-guide.html).

En un laboratorio Linux con **Network UPS Tools (NUT)**, el controlador lee el SAI, `upsd` comparte su estado y `upsmon` activa el apagado del host cuando la alimentación llega a un nivel crítico. Un host conectado directamente a un SAI USB o serie suele ejecutar el controlador, `upsd` y `upsmon` en modo **Primary**. Otros hosts ejecutan `upsmon` en modo **Secondary** contra ese servidor. Un SAI con gestión de red necesita un controlador compatible y una configuración primaria específica del modelo. La [guía de topología de NUT](https://networkupstools.org/docs/user-manual.chunked/ar01s02.html) explica estos roles. Configura el router y el switch para que los hosts de monitorización sigan conectados con batería. Restringe el comando de apagado y sus permisos a los administradores.

Antes de probar el apagado, comprueba que el controlador informa del estado actual. Sustituye `myupsname` por el nombre del SAI en tu configuración de NUT:

```bash
upsc myupsname@localhost ups.status
```

La [guía de configuración de NUT](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html) espera `OL` con alimentación normal de red y explica `OB` para el funcionamiento con batería. Ejecuta la comprobación de estado desde cada host que monitorice el SAI y usa el nombre correcto del servidor para clientes remotos. Una lectura obsoleta o ausente indica que debes reparar la ruta de señal antes de probar el apagado.

Anota el **orden de apagado**. Por ejemplo, detén primero las VM de aplicaciones, después los clientes de almacenamiento y, por último, el hipervisor y el NAS. Comprueba si cada servicio y sistema de archivos se recupera con normalidad al volver la corriente. Detener el host correctamente sin recuperar las aplicaciones no es un resultado completo.

## Prueba sin hacer suposiciones

Empieza con una **simulación** en el host que tenga configurado el controlador del SAI. NUT documenta `upsdrvctl -t shutdown` como una vista previa de la secuencia de apagado del controlador; no ejecuta los controladores ni corta la alimentación:

```bash
upsdrvctl -t shutdown
```

Esta **simulación del controlador** no demuestra que una alerta de corte llegue a todos los hosts. Comprueba cada servicio de monitorización y sus registros. En una ventana de mantenimiento, la [guía de pruebas de apagado de NUT](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html) describe una prueba forzada con `upsmon -c fsd` en el host NUT principal. Esta **prueba FSD** inicia una secuencia real de apagado. La marca FSD permanece activa hasta que se reinicia `upsd`. Cuando los sistemas vuelvan a estar disponibles, confirma que `upsd` se reinició y que el estado ya no muestra FSD antes de volver a confiar en la monitorización. Lee el [manual actual de upsmon](https://networkupstools.org/docs/man/upsmon.html), prepara una vía de recuperación y ejecuta la prueba solo después de guardar el trabajo y avisar a los usuarios del laboratorio.

Para una **prueba controlada del evento de batería**, sigue primero el procedimiento del fabricante del SAI con cargas no críticas. Esta prueba con poca carga verifica que llega la señal, pero no demuestra la autonomía de tu laboratorio. Más adelante, durante una ventana de mantenimiento, prueba una carga de batería representativa de la prevista. Alguien debe vigilar el SAI y poder restablecer la alimentación de red si se reduce el margen. Registra la carga que indica el SAI, la hora en que informa del funcionamiento con batería, cuándo empieza a apagarse cada host y cuándo se detiene el último. Comprueba que la batería no se agote antes de que se detengan los hosts. Tras volver la corriente, revisa el arranque de los hosts, la salud de las aplicaciones, la integridad del almacenamiento y el estado de la monitorización. NUT considera correcta la secuencia cuando el sistema operativo se detiene antes de agotar la batería y reanuda el funcionamiento al volver la alimentación.

| Comprobación | Qué registrar |
|---|---|
| **Ruta de señal** | Evento del SAI visible en cada host de monitorización |
| **Tiempo de apagado** | Último host detenido antes de agotar la batería |
| **Recuperación** | Hosts, almacenamiento y aplicaciones arrancan correctamente |
| **Capacidad** | La carga del SAI se mantiene dentro de los límites en vatios y VA |

## Solución de problemas

- **Alarma de sobrecarga del SAI:** Retira cargas opcionales. Compara la carga máxima medida con ambos límites del SAI y los límites de sus tomas.
- **Autonomía inferior a la prevista:** Comprueba la carga actual, la antigüedad de la batería, los datos de autonomía del modelo y los últimos resultados de prueba. No extrapoles linealmente solo a partir de VA.
- **Un host no se apaga:** Comprueba su servicio de monitorización, ruta de red, permisos de apagado y registros.
- **Los hosts se detienen pero no vuelven:** Revisa el comportamiento de la salida del SAI al volver la corriente, la opción del firmware para recuperar la alimentación y las [consideraciones de NUT sobre carreras de alimentación](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html).
- **La simulación funciona, pero falla la prueba de corte:** La vista previa del controlador cubre una ruta más limitada. Inspecciona la entrega del evento y el orden real de apagado de los hosts.

## Siguientes pasos

Guarda la hoja con el inventario de tu homelab. Vuelve a medir la carga al añadir hardware y repite la prueba de apagado tras cambiar el SAI, el software de monitorización, la política de arranque del host o la pila de almacenamiento. Revisa por separado tu plan de copia y restauración. La batería protege la ventana de apagado; una [copia de seguridad probada del homelab](/articles/what-is-a-homelab-and-should-you-have-one/) protege tus datos frente a otros fallos.
