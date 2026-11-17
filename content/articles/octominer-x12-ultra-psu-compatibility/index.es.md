---
title: "Compatibilidad de fuentes del Octominer X12 Ultra: prueba de campo de Chicony y LiteOn"
date: 2026-11-12
lastmod: 2026-11-12
toc: true
draft: false
description: "Una prueba con cinco ventiladores y tres fuentes en un Octominer X12 Ultra mostró que una fuente Chicony arrancó el equipo, mientras las unidades LiteOn probadas marcaron ámbar y no arrancaron."
genre: ["Hardware de minería", "Hardware informático"]
tags: ["Octominer X12 Ultra", "fuente de alimentación para servidor", "compatibilidad de fuentes", "Chicony R12-1K6P2A", "LiteOn PS-2142-2L"]
cover: "/img/cover/octominer-x12-ultra-psu-compatibility.webp"
coverAlt: "Ilustración abstracta de tres fuentes para servidor dentro de un chasis con indicadores verdes, ámbar y grises"
coverCaption: ""
---

**La Chicony R12-1K6P2A arrancó mi Octominer X12 Ultra de cinco ventiladores y tres fuentes.** Las fuentes LiteOn PS-2142-2L que probé mostraron una luz verde, cambiaron a ámbar y no arrancaron el equipo. Este resultado corresponde a mi unidad con una placa de alimentación **OCTOMINER (12PIN) 3x DPS1200 rev. 20**. La misma potencia nominal o una lista para una placa breakout X12 independiente no demuestra compatibilidad con una placa Octominer.

El chasis se vendió como una **configuración de 3.600 W** con tres bahías para fuentes. [Octominer ofrece una opción de tres fuentes de 1.200 W](https://octominer.eu/product/octominer-x12-ultra-used/) para el X12 Ultra, junto con otras configuraciones. Comprueba la etiqueta y la placa de alimentación de tu equipo antes de aplicar estos resultados.

## Resultados de las pruebas

| Fuente | Resultado en este equipo |
|---|---|
| **Chicony R12-1K6P2A, 1.600 W** | Arrancó el equipo en mi prueba. Este artículo no midió carga sostenida ni funcionamiento en todas las bahías. |
| **LiteOn PS-2142-2L, 1.400 W** | Las unidades probadas se iluminaron en verde y luego en ámbar. El equipo no arrancó. |
| **Dell/Delta D1200E-S0, Dell 0F37X3** | La entrada de CA poco habitual dificultó encontrar un cable compatible. No registré resultados de arranque ni de carga para esta fuente. |
| **HP HSTNS-PD30, 1.200 W** | Probada en el mismo equipo. No arrancó el sistema. |
| **Otras unidades HP Common Slot** | Los kits Platinum Plus de 1.200 W y las unidades HSTNS-PD22B, HSTNS-PL22B y HSTNS-PD18 de 750 W que probé no arrancaron este equipo. No registré los números exactos de modelo de las fuentes de los kits. |

**No interpretes el resultado de LiteOn como un diagnóstico de avería para todos los PS-2142-2L.** La secuencia observada identifica un fallo de arranque en este chasis. La prueba no aisló la señal de habilitación, la comunicación de telemetría, el pinout de la placa ni un defecto de una fuente concreta. Del mismo modo, el resultado de Chicony demuestra un arranque correcto, pero no certifica una potencia de 4.800 W para el chasis ni su fiabilidad a largo plazo.

## ¿Qué Chicony arrancó este equipo?

El modelo que funcionó fue **Chicony R12-1K6P2A**, también indicado como pieza **R1K6A002L** en la [tabla de compatibilidad de Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). Su [informe de prueba 80 PLUS](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/chicony-power-r121k6p2a-5866.pdf) identifica una fuente de 1.600 W con una especificación de **200 a 240 V CA**, 10 A y 50 a 60 Hz. El informe midió una eficiencia del 94,19 % con media carga bajo sus condiciones de prueba de 230 V. Estas cifras describen la fuente probada, no todo el equipo de minería.

La clasificación de **200 a 240 V importa**. No des por sentado que este modelo entrega su potencia nominal desde una toma de 120 V. La fuente probada tiene una entrada C14 estándar, según una [ficha de piezas de servidor del modelo exacto](https://www.itcreations.com/product/142080). Usa cables y equipos de distribución con clasificación adecuada para la tensión y corriente de entrada.

Mi prueba confirmó un arranque correcto con la Chicony en esta placa concreta. No demuestra compatibilidad con todas las revisiones del X12 Ultra. Compara el número de modelo completo y revisa la etiqueta de la fuente antes de pedir más unidades.

## Por qué me confundió la lista de LiteOn

El **LiteOn PS-2142-2L** aparece en la [tabla de compatibilidad de placas breakout X12 de Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). Su [informe 80 PLUS](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/liteon-technology-corporation-ps21422l-6889.pdf) identifica un modelo de 1.400 W. Estas fuentes confirman el modelo y su uso indicado con el **adaptador X12 de Parallel Miner**. Ninguna prueba la placa de alimentación OEM de Octominer.

Mis unidades PS-2142-2L cambiaron de **verde a ámbar** tras insertarlas, y el equipo no arrancó. Que las palas de salida tengan una forma parecida no demuestra que coincidan el arranque, el estado o la comunicación. La secuencia de LED por sí sola no demuestra qué diferencia causó el fallo de arranque.

La misma [tabla de Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/) agrupa **Dell/Delta D1200E-S0**, **LiteOn PS-2142-2L** y **Chicony R12-1K6P2A** en la familia de adaptadores de ocho pines. Sitúa **HP HSTNS-PD30** y varias fuentes HP Common Slot de 750 W en otra familia de adaptadores de seis pines. Ninguna de las unidades HP que probé arrancó este equipo. La tabla describe las placas de Parallel Miner, no una lista de sustitución para la placa **OCTOMINER (12PIN)**.

## Comprueba la alimentación y el cableado

La [guía de solución de problemas del Octominer X12 Ultra](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) indica que el chasis consume hasta **200 W** por sí solo con los ventiladores al máximo. Recomienda al menos un **10 % de margen de potencia** y advierte contra superar el **90 % de la potencia nominal de las fuentes instaladas**. Ten en cuenta la potencia de las GPU, el chasis y la salida real de las fuentes con tu tensión de CA.

**La etiqueta de 1.600 W de cada fuente Chicony no eleva la configuración publicada de 3.600 W del chasis a 4.800 W.** La placa de alimentación, el cableado interno, los conectores, la distribución de CA y la refrigeración también limitan el sistema. No medí esos límites en esta unidad. Mantén el equipo dentro de la configuración documentada hasta que Octominer confirme una potencia superior para la revisión exacta de la placa.

El Dell/Delta **D1200E-S0 / 0F37X3** presentó otro problema: su entrada de CA en el lado de la fuente necesitaba un cable de acoplamiento menos común. En una búsqueda anterior identifiqué la entrada como **LS-25** y el conector del cable como **LS-26**, según la unidad y los listados de cables. Comprueba la forma del conector y las marcas eléctricas antes de comprar un cable. Un enchufe C13 de aspecto familiar no sustituye al conector de acoplamiento correcto.

## Verifica tu propio X12

1. **Registra el hardware exacto.** Fotografía la etiqueta del chasis, la etiqueta de la fuente, la entrada de CA, la pala de salida y la revisión de la placa de alimentación. Cuenta los ventiladores y las bahías para fuentes.
2. **Comprueba la alimentación de CA.** Compara la clasificación de entrada de la fuente con las de la toma, el cable y la PDU. El informe de la Chicony R12-1K6P2A especifica de 200 a 240 V CA.
3. **Prueba una configuración mínima.** Apaga y desconecta todas las entradas de CA antes de cambiar una fuente, una GPU o una conexión PSON. [La guía de Octominer](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) recomienda comprobar que la fuente esté asentada y sus LED, el cable PSON de seis pines entre la placa base y la placa de alimentación, y una fuente con una GPU para aislar un problema de arranque.
4. **Registra lo ocurrido.** Anota el modelo de la fuente, la bahía, la secuencia de LED, si arrancaron la placa y los ventiladores, y si inició el equipo. Repite la prueba en otras bahías solo después de un apagado seguro.
5. **Mide antes de añadir carga.** Comprueba la telemetría de la fuente y el consumo en la toma con la carga prevista de las GPU. La prueba de arranque de este artículo no reemplaza una prueba de carga.

## Conclusión

**Chicony R12-1K6P2A es la única fuente de esta comparación con un arranque correcto registrado en mi X12 Ultra de tres ranuras.** Las unidades LiteOn PS-2142-2L probadas cambiaron de verde a ámbar y no arrancaron. Las unidades HP Common Slot probadas tampoco arrancaron el equipo. Trata otros listados de fuentes como pistas de investigación hasta que el modelo exacto y la placa de alimentación de Octominer superen una prueba controlada de arranque y carga. Empieza por las etiquetas de modelo y la revisión de la placa. Revisa las recomendaciones de alimentación de Octominer antes de aumentar la carga de GPU.
