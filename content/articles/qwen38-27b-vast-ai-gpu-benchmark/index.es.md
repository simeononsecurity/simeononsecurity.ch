---
title: "Benchmarks de GPU para Llama 3.1 8B y Qwen3.8 27B en Vast.ai"
date: 2026-10-02
lastmod: 2026-11-20
toc: true
draft: false
description: "Compara resultados medidos de Ollama para Llama 3.1 8B y Qwen3.8 27B en GPU de Vast.ai, sus costos y opciones de alojamiento."
genre: ["IA local", "Pruebas de GPU", "IA autohospedada", "Infraestructura en la nube", "Inteligencia artificial", "Economía de la IA"]
tags: ["Llama 3.1 8B", "llama3.1:8b", "Qwen3.8 27B", "Qwen3.8:27b", "Vast.ai", "benchmark de GPU", "Ollama", "H100", "RTX PRO 5000", "RTX 6000 Ada", "RTX PRO 6000 Max-Q", "A100", "CMP 170HX", "LLM local", "contexto largo", "alquiler de GPU", "IA autohospedada", "modelos abliterated", "modelos sin censura", "créditos de API", "suscripción de IA", "Q4_K_M", "tokens por segundo"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Espacio de trabajo tecnológico con una tarjeta gráfica y pantallas que muestran resultados de benchmarks de IA local"
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**La H100 SXM fue la tarjeta más rápida en las dos pruebas de modelos con Ollama, pero no ofreció el mejor valor.** La RTX PRO 5000 y la RTX 6000 Ada lograron una mejor relación entre velocidad y costo de alquiler. La CMP 170HX tuvo la tarifa por hora más baja entre las ejecuciones completadas de Qwen3.8 27B.

*Estos resultados miden un modelo, un wrapper de Ollama, una cuantización predeterminada y un patrón de servicio. Úsalos para dimensionar esta carga de trabajo, no como una clasificación universal de GPU.*

Este artículo compara **Llama 3.1:8b**, una compilación Q4_K_M de Ollama con 8.03 mil millones de parámetros, con **Qwen3.8:27b**, una compilación Q4_K_M de Ollama con aproximadamente 27.3 mil millones de parámetros. Ambos se probaron en instancias de GPU alquiladas a través de Vast.ai. Las pruebas midieron el rendimiento de decodificación con longitudes reales de prompt hasta el límite de contexto admitido.

## Respuesta breve

**Alquila una RTX PRO 5000 o una RTX 6000 Ada para el trabajo habitual de una sola persona.** La RTX PRO 5000 ofreció el mejor valor con contextos cortos y medianos. La RTX 6000 Ada costó menos y mantuvo una ventaja útil sobre las tarjetas A100. Alquila una H100 SXM cuando la velocidad de respuesta importe más que la tarifa por hora o cuando la carga incluya prompts largos.

| Objetivo | Recomendación | Motivo |
|---|---|---|
| **Menor costo de prueba** | CMP 170HX | $0.420 por hora y suficiente VRAM para los modelos Q4_K_M probados |
| **Mejor valor por menos de $1.25/h** | RTX PRO 5000 o RTX 6000 Ada | Buena velocidad de decodificación sin el costo de alquiler de la H100 |
| **Respuestas más rápidas** | H100 SXM | Mayor velocidad de decodificación en ambas pruebas de modelos |
| **Qwen con contexto largo** | H100 SXM o RTX PRO 6000 Max-Q | Ambas completaron la ejecución de Qwen de aproximadamente 131k tokens con bastante VRAM disponible |
| **Referencia popular de 8B** | Llama 3.1:8b | Comparación práctica de 8B con un límite de contexto de 128K |
| **Carga recurrente pequeña** | Créditos de API o una suscripción de chat | Sin costo de GPU inactiva, mantenimiento ni trabajo de implementación |
| **Carga privada y frecuente** | Estación de trabajo propia con GPU | El costo del hardware se justifica mejor con una utilización sostenida |
| **Pruebas con modelos abliterated o sin censura** | Alquila primero y compra solo después de un uso sostenido | El comportamiento, la licencia y el riesgo operativo del modelo requieren pruebas antes de gastar en hardware |

## Qué se probó

**El benchmark usó Ollama con la compilación predeterminada Q4_K_M del modelo.** No se agregó cuantización especial, decodificación especulativa, sampler personalizado ni otro stack de servicio. El objetivo fue comparar las instancias de GPU de una forma sencilla y reproducible a nivel local.

Vast.ai describe su servicio como un mercado de GPU en la nube que conecta a proveedores de cómputo con usuarios. Su documentación enumera opciones bajo demanda, reservadas, interrumpibles y sin servidor, además de filtros por modelo de GPU, memoria, precio y disponibilidad. Las tarifas por hora siguientes corresponden a las instancias elegidas durante esta sesión, no a una lista de precios permanente de Vast.ai.

La salida medida fue el **rendimiento de decodificación**, expresado en tokens generados por segundo. El rendimiento de prefill aparece aparte porque mide el procesamiento del prompt, no la velocidad con que aparece la respuesta. Un prompt largo suele requerir bastante tiempo de procesamiento aunque la decodificación siga siendo rápida.

El benchmark usó dos pruebas válidas por contexto y registró la mediana del resultado de decodificación. Los niveles completados se basaron en los valores reales de `prompt_eval_count`:

- **Aproximadamente 16.4k tokens de prompt**
- **Aproximadamente 32.8k tokens de prompt**
- **Aproximadamente 65.5k tokens de prompt**
- **Aproximadamente 131k tokens de prompt**

No se completó la ejecución solicitada de 256k tokens. Las tarjetas A100 de 40 GB y varias tarjetas más pequeñas seguían procesando o no terminaron con la longitud de contexto objetivo.

> **Límite del benchmark:** Las cifras describen dos cargas Q4_K_M en Ollama con un patrón de servicio. No predicen la velocidad de entrenamiento, el rendimiento con varios usuarios, la generación de imágenes, el rendimiento de vLLM ni los resultados de otro modelo.

## Nueva prueba de Llama 3.1 8B

**Llama 3.1:8b ofrece una referencia práctica útil para el mismo conjunto de GPU.** Ollama indica que el modelo registra aproximadamente 120 millones de descargas, lo que lo convierte en una segunda referencia razonable por popularidad. La [página oficial del modelo en Ollama](https://ollama.com/library/llama3.1:8b) indica una compilación Q4_K_M de 4.9 GB, 8.03 mil millones de parámetros y una ventana de contexto de 128K.

La nueva prueba usó un ejecutor de benchmark específico para el modelo y calibró el generador de prompts con el tokenizador de Ollama. Las etiquetas siguientes usan recuentos reales de tokens del prompt, no los ajustes de contexto solicitados:

- **Aproximadamente 32,676 tokens reales de prompt** para el objetivo de 32k
- **Aproximadamente 65,342 tokens reales de prompt** para el objetivo de 64k
- **Aproximadamente 130,671 tokens reales de prompt** para el objetivo de 128k

El nivel de 256k no es compatible con Llama 3.1 8B porque su límite de contexto indicado es 128K. El ejecutor agregó reintentos y filas de estado, por lo que un tiempo de espera agotado permanece visible en la tabla.

### Resultados de Llama 3.1 8B

| GPU | Decodificación ~32k tok/s | Decodificación ~64k tok/s | Decodificación ~128k tok/s |
|---|---:|---:|---:|
| **H100 SXM** | **163.5** | **124.0** | **82.4** |
| **H100 SXM** | **158.6** | **121.2** | **80.6** |
| **RTX PRO 5000** | 110.1 | 79.8 | 49.9 |
| **CMP 170HX 64GB** | 91.9 | 71.0 | 50.1 |
| **RTX 6000 Ada** | 88.3 | 53.9 | 29.3 |
| **RTX PRO 6000 Max-Q** | 66.7 | 53.0 | 40.3 |
| **RTX PRO 6000 S** | 60.3 | 42.5 | 33.9 |
| **A100 SXM4 40GB** | 2.0 | 40.6 | 38.5 |
| **A100 PCIe 40GB** | 1.2 | 20.3 | 20.3 |
| **2x RTX 5060 Ti** | 1.3 | 26.8 | Tiempo de espera agotado |

Las dos filas de H100 provienen de instancias válidas distintas de la misma clase de GPU. Ambas superaron claramente a las demás tarjetas. Sus resultados de 32k fueron entre un 44 % y un 48 % más rápidos que los de la RTX PRO 5000. En 128k fueron entre un 61 % y un 65 % más rápidos.

Los resultados de 32k de las tarjetas A100 y RTX 5060 Ti son demasiado bajos para representar una ejecución de GPU comparable en esta carga de trabajo. El host con RTX 5060 Ti también agotó el tiempo de espera durante su segundo intento de 128k. Considera que el host no es apto para comparaciones válidas de rendimiento de GPU, no como un resultado real del ranking.

| Objetivo de contexto | Estado |
|---|---|
| **32k** | Completado en los 10 hosts |
| **64k** | Completado en los 10 hosts |
| **128k** | Completado en 9 hosts. El host con 2x RTX 5060 Ti agotó el tiempo de espera durante su segundo intento |
| **256k** | No compatible con ningún host porque Llama 3.1 8B admite hasta 128K de contexto |

## Comparación de los dos modelos

**El modelo Llama más pequeño fue más rápido en todas las GPU comparables, pero el tamaño y la calidad del modelo no son intercambiables.** Llama 3.1 8B sirve como referencia popular que requiere menos memoria. Qwen3.8 27B necesita más memoria y ofrece un perfil de capacidades distinto. Las cifras deben orientar la elección de hardware, no declarar que un modelo siempre es mejor.

| Caso de uso | Mejor referencia de benchmark | Motivo |
|---|---|---|
| **Asistente rápido de 8B** | Llama 3.1:8b | Mayor velocidad de decodificación y menor demanda de memoria del modelo |
| **Dimensionar un modelo local de 27B** | Qwen3.8:27b | Representa mejor una carga mayor en una sola GPU |
| **Límite de contexto de 128K** | Llama 3.1:8b | El modelo tiene un límite explícito de 128K, por lo que 256k no es un objetivo válido |
| **Probar el margen de VRAM** | Qwen3.8:27b | El modelo más grande revela antes los límites de memoria y contexto largo |
| **Referencia entre proveedores** | Llama 3.1:8b | Su popularidad y tamaño facilitan reproducir el resultado |

La prueba anterior de Qwen también corrigió sus recuentos reales de tokens de prompt a aproximadamente **32,770**, **65,538** y **131,074** en los niveles de contexto compatibles. Estas etiquetas corregidas sustituyen los valores solicitados de `num_ctx` al comparar ejecuciones de Qwen.

## Aproximadamente 16k tokens

**La H100 SXM encabezó la prueba de contexto corto con 134.4 tokens de decodificación por segundo.** La RTX PRO 5000 quedó detrás con 113.9 tokens por segundo y costó menos de la mitad por hora.

| Puesto | GPU | VRAM | Decodificación tok/s | Procesamiento del prompt tok/s | Tarifa de alquiler |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **134.4** | 89,974 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **113.9** | 68,726 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **89.1** | 95,856 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **84.1** | 72,235 | $1.507/hr |
| 5 | **A100 SXM4** | 40 GB | **60.6** | 53,048 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **51.5** | 51,122 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **49.3** | 52,773 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | **38.4** | 38,886 | $0.565/hr |

Con esta longitud de prompt, la RTX PRO 5000 alcanzó aproximadamente el 84.7 % de la velocidad de decodificación de la H100 con el 37.3 % de su tarifa por hora. La RTX 6000 Ada alcanzó aproximadamente el 66.3 % de la velocidad de la H100 con el 30.2 % de la tarifa.

## Aproximadamente 32.8k tokens

**El ranking se mantuvo estable en la prueba de contexto medio.** La H100 SXM bajó a 120.0 tokens por segundo, mientras que la RTX PRO 5000 llegó a 105.0 y la RTX 6000 Ada a 75.7.

| Puesto | GPU | VRAM | Decodificación tok/s | Procesamiento del prompt tok/s | Tarifa de alquiler |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **120.0** | 139,748 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **105.0** | 103,707 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **75.7** | 141,678 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **66.9** | 120,537 | $1.507/hr |
| 5 | **RTX PRO 6000 S** | 95.6 GB | **65.9** | 109,280 | $1.756/hr |
| 6 | **A100 SXM4** | 40 GB | **51.1** | 81,929 | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | **46.2** | 77,984 | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | **36.1** | 73,377 | $0.565/hr |

La RTX PRO 5000 siguió siendo el alquiler más atractivo de este grupo. Fue solo un 12.5 % más lenta que la H100 y costó un 62.7 % menos por hora.

## Aproximadamente 65.5k tokens

**Los prompts más largos ampliaron la diferencia entre las tarjetas con mucha memoria y las que tienen menos margen.** La H100 siguió en primer lugar con 112.0 tokens por segundo. La RTX PRO 6000 Max-Q superó a la RTX 6000 Ada en velocidad de decodificación.

| Puesto | GPU | VRAM | Decodificación tok/s | Procesamiento del prompt tok/s | Tarifa de alquiler |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **112.0** | 195,252 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **96.9** | 148,897 | $1.005/hr |
| 3 | **RTX PRO 6000 Max-Q** | 95.6 GB | **75.7** | 156,443 | $1.507/hr |
| 4 | **RTX 6000 Ada** | 48 GB | **70.8** | 208,400 | $0.813/hr |
| 5 | **A100 SXM4** | 40 GB | **49.3** | 147,699 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **45.9** | 118,657 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **37.0** | 124,927 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | N/D | N/D | $0.565/hr |

La RTX PRO 5000 siguió ofreciendo el mejor equilibrio en la tabla completada. La RTX 6000 Ada fue más lenta, pero su menor tarifa de alquiler la hace atractiva para presupuestos que priorizan la disponibilidad sobre la velocidad máxima.

## Aproximadamente 131k tokens

**Con esta longitud de contexto, solo la H100 superó los 100 tokens de decodificación por segundo.** La RTX PRO 6000 Max-Q completó la prueba con 73.4 tokens por segundo, seguida por la RTX 6000 Ada con 61.7.

| Puesto | GPU | VRAM | Decodificación tok/s | Procesamiento del prompt tok/s | Tarifa de alquiler |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **108.2** | 242,093 | $2.693/hr |
| 2 | **RTX PRO 6000 Max-Q** | 95.6 GB | **73.4** | 197,208 | $1.507/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **61.7** | 278,283 | $0.813/hr |
| 4 | **RTX PRO 6000 S** | 95.6 GB | **39.4** | 124,653 | $1.756/hr |
| 5 | **RTX PRO 5000** | 47.8 GB | N/D | N/D | $1.005/hr |
| 6 | **A100 SXM4** | 40 GB | N/D | N/D | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | N/D | N/D | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | N/D | N/D | $0.565/hr |

La RTX PRO 6000 Max-Q se convirtió en la alternativa práctica a la H100 para prompts largos. Entregó el 67.8 % de la velocidad de decodificación de la H100 con el 56.0 % de su tarifa por hora. La RTX 6000 Ada costó menos, pero sus 48 GB de VRAM dejan menos margen para prompts largos, lotes más grandes u otra configuración del modelo.

## Comparación general de decodificación

| GPU | ~16k | ~32.8k | ~65.5k | ~131k |
|---|---:|---:|---:|---:|
| **H100 SXM** | **134.4** | **120.0** | **112.0** | **108.2** |
| **RTX PRO 5000** | 113.9 | 105.0 | 96.9 | N/D |
| **RTX 6000 Ada** | 89.1 | 75.7 | 70.8 | 61.7 |
| **RTX PRO 6000 Max-Q** | 84.1 | 66.9 | 75.7 | 73.4 |
| **RTX PRO 6000 S** | 49.3 | 65.9 | 37.0 | 39.4 |
| **A100 SXM4** | 60.6 | 51.1 | 49.3 | N/D |
| **CMP 170HX** | 51.5 | 46.2 | 45.9 | N/D |
| **A100 PCIe** | 38.4 | 36.1 | N/D | N/D |

**La H100 lideró todos los niveles de contexto completados.** Su ventaja sobre la RTX PRO 5000 bajó de 20.5 tokens por segundo con unos 16k tokens a 12.0 con unos 32.8k. La clasificación de valor depende de si necesitas la respuesta inicial más rápida o el menor costo durante una sesión larga.

## Costo por millón de tokens de decodificación

**La tarifa por hora por sí sola oculta la comparación útil.** Dividir la tarifa indicada entre el rendimiento de decodificación permite estimar el costo de alquiler de un millón de tokens generados. Esta cifra no incluye el procesamiento del prompt, el tiempo inactivo, el almacenamiento, la transferencia de datos, los impuestos, los descuentos ni las ejecuciones fallidas o interrumpidas.

| GPU | Tarifa con contexto corto | Costo aprox. por 1M de tokens de decodificación |
|---|---:|---:|
| **CMP 170HX** | $0.420/hr | $2.27 |
| **RTX PRO 5000** | $1.005/hr | $2.45 |
| **RTX 6000 Ada** | $0.813/hr | $2.53 |
| **A100 SXM4** | $0.680/hr | $3.12 |
| **A100 PCIe** | $0.565/hr | $4.09 |
| **RTX PRO 6000 Max-Q** | $1.507/hr | $4.98 |
| **H100 SXM** | $2.693/hr | $5.57 |
| **RTX PRO 6000 S** | $1.756/hr | $9.89 |

**La CMP 170HX ganó esta comparación aritmética acotada.** La RTX PRO 5000 y la RTX 6000 Ada quedaron cerca y ambas ofrecieron más rendimiento que la CMP 170HX. Para el uso interactivo, el tiempo de espera adicional suele importar más que el menor costo por token.

## ¿Alquilar, comprar créditos, suscribirse o comprar hardware?

**La opción adecuada depende de la utilización y de los requisitos de control.** Alquilar una GPU genera un costo de cómputo variable. Los créditos de API son un costo variable del modelo. Una suscripción de chat es una tarifa fija de acceso con límites de uso. El hardware propio es una compra de capital seguida de gastos de electricidad, refrigeración, mantenimiento y depreciación.

| Presupuesto mensual y carga | Opción recomendada | Motivo | Principal desventaja |
|---|---|---|---|
| **Menos de $10** | Comprar créditos de API o usar un modelo local gratuito | Permite probar el flujo sin pagar por una GPU inactiva | Menos control sobre el alojamiento del modelo y los límites de solicitudes |
| **$10 a $30** | Créditos de API para uso ocasional o una suscripción de chat para interacción diaria | La suscripción sirve para chatear, los créditos para scripts y llamadas medidas | Ninguna opción ofrece por defecto un endpoint privado de 27B |
| **$30 a $100** | Alquilar una RTX 6000 Ada o RTX PRO 5000 solo durante sesiones activas | Cubre sesiones breves de investigación y evita el costo de propiedad | La instancia aún requiere configuración, almacenamiento, supervisión y apagado cuidadoso |
| **$100 a $250** | Alquilar una tarjeta rápida para trabajo programado o probar una estación de trabajo propia | El uso mensual sostenido empieza a hacer visible la utilización | La disponibilidad y las tarifas por hora cambian |
| **$250 a $600** | Comparar un mes de alquiler de RTX PRO 5000 con una GPU local usada o nueva | Este es el punto de decisión para la inferencia privada frecuente | El hardware agrega consumo eléctrico, calor, soporte y riesgo de reventa |
| **Más de $600** | Comprar hardware solo con alta utilización o reservar alquiler de clase H100 para picos | Una estrategia mixta evita tener una tarjeta de máximo rendimiento para demanda ocasional | El capital queda atado a una sola configuración |

Estos rangos sirven como guías, no como cotizaciones de proveedores. Las tarifas del benchmark muestran el punto de equilibrio: una H100 a $2.693 por hora cuesta unos $64.63 por un día continuo de 24 horas y unos $1,941.00 por 30 días, antes del almacenamiento u otros cargos. Una RTX PRO 5000 a $1.005 por hora cuesta unos $24.12 por día y $723.60 por 30 días de uso continuo. El total de una GPU alquilada solo durante sesiones activas será distinto al de una GPU encendida todo el mes.

### Cuándo convienen los créditos de API

**Los créditos de API convienen cuando el uso es irregular, importa la automatización y la tarea no requiere un modelo local específico.** Evitan aprovisionar GPU, descargar modelos, resolver problemas de controladores y pagar por tiempo inactivo. También permiten comparar varios modelos alojados antes de comprometerse con hardware.

Los precios de API varían según el modelo y el proveedor. El catálogo de modelos de OpenRouter permite comparar tamaños de contexto, proveedores y precios por token. Consulta la calculadora vigente del proveedor antes de comparar una factura de API con este benchmark. Una GPU local genera tokens sin un cargo del proveedor por token, pero la hora de alquiler sigue contando mientras la instancia espera.

### Cuándo conviene una suscripción

**Una suscripción es adecuada para una persona que usa un asistente alojado todos los días.** Por ejemplo, los planes individuales actuales de Claude separan los niveles gratuito, Pro y Max con diferentes límites de uso y funciones. Una suscripción no equivale al acceso por API. Suele ofrecer una interfaz pulida y herramientas incluidas, mientras que los créditos de API permiten control programático.

Elige una suscripción cuando el trabajo sea principalmente escritura interactiva, investigación, programación o revisión de archivos. Elige créditos de API cuando un script, una aplicación o un agente necesite un endpoint medido.

### Cuándo conviene Vast.ai

**Vast.ai conviene cuando necesitas un modelo abierto, control privado del entorno de ejecución o un aumento breve del rendimiento.** Seleccionas una GPU, inicias una instancia, ejecutas Ollama, pruebas un modelo y apagas la instancia al terminar. Es una buena opción para Qwen3.8 27B, variantes abliterated y otros archivos de modelo que no caben en una laptop de consumo.

El costo es trabajo operativo. Debes confirmar que el modelo usa la GPU, vigilar la VRAM, proteger el servicio expuesto, conservar los archivos de modelo necesarios y detener la instancia al terminar. Una tarifa por hora baja no evita que olvides una instancia encendida.

### Cuándo conviene comprar una GPU

**Comprar hardware conviene cuando la utilización es sostenida, los requisitos del modelo son estables y necesitas control local.** La compra elimina el riesgo de disponibilidad del alquiler y ofrece un entorno persistente. También permite ejecutar datos privados sin enviar prompts a un proveedor alojado.

El precio de compra es solo una parte del costo. Suma el sistema anfitrión, la fuente de alimentación, el almacenamiento, la refrigeración, la electricidad, el riesgo de reemplazo y el valor de tu tiempo de configuración. Una tarjeta de gama alta también queda inactiva cuando los créditos de API o una suscripción costarían menos.

Las especificaciones de referencia de NVIDIA para la RTX 4090 indican 24 GB de memoria, una potencia gráfica total de 450 W y una recomendación de potencia mínima del sistema de 850 W. Es una referencia útil para inferencia local, pero sus 24 GB quedan por debajo de la capacidad de las configuraciones Q4_K_M de 27B probadas aquí. Comprueba el uso real de memoria del modelo en vez de asumir que cabe en una tarjeta por el número de parámetros.

## Modelos abliterated y sin censura

**Las variantes de modelos abliterated y sin censura cambian la decisión de compra.** Su atractivo suele ser una menor cantidad de rechazos o menos restricciones integradas. Sus costos incluyen un comportamiento de seguridad más débil, procedencia incierta, formatos de prompt inconsistentes, más necesidad de revisión y posibles límites de licencia o uso aceptable.

Alquila antes de comprar estos modelos. Una prueba de un día con la RTX PRO 5000 a la tarifa indicada cuesta unos $24.12 antes de otros cargos. Esto basta para confirmar la compatibilidad del modelo, el uso de GPU, la calidad de las respuestas y el riesgo operativo.

**No expongas un modelo sin censura directamente a Internet público.** Coloca autenticación, límites de solicitudes, controles de registro y aislamiento de red delante del modelo. No envíes datos personales, confidenciales o regulados a una fuente de modelos que no hayas revisado.

Si el modelo se convierte en una herramienta diaria, compara el alquiler mensual con el costo total de una estación de trabajo propia. Si el uso es ocasional, el alquiler es más fácil de detener y reemplazar.

## Advertencias del benchmark

**Los resultados que faltan también forman parte del resultado.** Un valor `N/A` significa que la ejecución no produjo una medición válida. No significa que la GPU sea lenta en la proporción sugerida por el resultado de otra tarjeta.

- **La segunda instancia H100 no produjo un conjunto válido de resultados** porque la descarga del modelo terminó demasiado tarde.
- **Se excluyó la instancia con 2x RTX 5060 Ti** porque Ollama cargó el modelo en la CPU en vez de usar las GPU.
- **No se completó el prompt de 256k tokens de Qwen3.8 27B.** El nivel válido más alto fue de aproximadamente 131k tokens reales de prompt. Llama 3.1 8B indica que 256k no es compatible porque su límite de contexto es 128K.
- **El `num_ctx` solicitado no se usó como etiqueta del ranking.** Las tablas finales usan los valores reales de `prompt_eval_count`.
- **Se resumieron dos pruebas válidas por contexto con la mediana del resultado de decodificación.** Esto reduce el efecto de una ejecución lenta, pero no reemplaza una serie de pruebas más grande.
- **El wrapper fue sencillo por diseño.** Una implementación ajustada de vLLM o llama.cpp produciría un ranking distinto.

## Recomendación final

**Empieza alquilando una RTX 6000 Ada o una RTX PRO 5000.** La RTX 6000 Ada es la opción económica si está disponible a $0.813 por hora. La RTX PRO 5000 ofrece más velocidad por debajo del precio de la H100. Usa la H100 SXM para prompts largos, baja latencia interactiva exigente o una prueba breve en la que el tiempo importe más que el costo de alquiler. Para un modelo de 8B, vale la pena probar la CMP 170HX cuando importe más su menor tarifa por hora que la velocidad máxima.

**No compres una GPU después de una sola prueba exitosa.** Alquila durante un mes con cargas reales, registra las horas activas, las longitudes de prompt, la concurrencia y los cambios de modelo. Después compara el total de alquiler con el costo completo de propiedad. Compra hardware cuando la carga sea frecuente para mantener ocupada la tarjeta y estable para justificar la pérdida de flexibilidad.

Para el uso ocasional, los créditos de API o una suscripción de chat son más sencillos. Para la inferencia local privada, los experimentos con modelos abiertos o las pruebas de modelos abliterated, Vast.ai ofrece una opción con menos compromiso que comprar de inmediato una estación de trabajo. Usa Llama 3.1 8B como referencia de menor demanda de memoria y Qwen3.8 27B cuando el modelo más grande sea el objetivo real de implementación.

## Próximos pasos

Repite la comparación con tus propias longitudes de prompt y una estimación de horas activas. Verifica el uso de GPU, registra la revisión del modelo y la versión del runtime, detén la instancia después de cada ejecución y compara el alquiler mensual con el costo completo de propiedad antes de comprar hardware.

## Referencias

1. [Mercado de GPU en la nube de Vast.ai](https://vast.ai/)
2. [Documentación de Vast.ai: mercado, instancias, precios y tipos de alquiler](https://docs.vast.ai/)
3. [Biblioteca de modelos Qwen3 de Ollama](https://ollama.com/library/qwen3)
4. [Página del modelo Llama 3.1 8B en Ollama](https://ollama.com/library/llama3.1:8b)
5. [Catálogo de modelos y comparación de precios de OpenRouter](https://openrouter.ai/models)
6. [Precios y planes individuales de Claude](https://www.anthropic.com/pricing)
7. [Especificaciones de NVIDIA GeForce RTX 4090](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/)
8. [IA local en 2026: Qwen3.8 27B y hardware para modelos autohospedados](/articles/local-ai-2026-build-your-rig-now/)
9. [Pruebas de modelos Ollama en hardware Raspberry Pi](/articles/ai-models-raspberry-pi-4-5/)
