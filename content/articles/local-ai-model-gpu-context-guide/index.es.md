---
title: "¿Qué modelo de IA local deberías ejecutar? Guía de GPU, contexto y programación para octubre de 2026"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Guía práctica de octubre de 2026 para elegir modelos de IA locales para agentes de programación. Compara memoria de GPU, crecimiento de KV-cache, tamaño de contexto, calidad de cuantización, procesamiento de prompts, ajustes de razonamiento y costes de alquiler en la nube."
genre: ["IA local", "Hardware de IA", "IA autohospedada", "Benchmarking de GPU", "Herramientas para desarrolladores", "Economía de la IA"]
tags: ["modelos de IA locales", "agentes de programación", "guía de GPU", "VRAM", "KV cache", "ventana de contexto", "Qwen 27B", "mezcla de expertos", "cuantización", "llama.cpp", "Ollama", "decodificación especulativa", "predicción de varios tokens", "LLM local", "alquiler de GPU", "estación de trabajo de IA", "programación con agentes", "procesamiento de prompts", "velocidad de inferencia"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Una estación de trabajo que muestra opciones de modelos de IA locales, uso de memoria de GPU y ventanas de contexto de agentes de programación"
coverCaption: ""
ref: ["/articles/32gb-vram-qwen-27b-hardware-guide", "/articles/qwen38-27b-vast-ai-gpu-benchmark", "/articles/local-ai-2026-build-your-rig-now"]
---

**El mejor modelo local para programar es el que mantiene suficiente parte de tu proyecto en memoria y lo lee con la rapidez necesaria para seguir siendo útil.** El tamaño del modelo importa, pero un modelo que solo encaja después de pasar datos a la RAM del sistema suele sentirse peor que un modelo más pequeño con una ventana de contexto estable.

*Elige el modelo y el presupuesto de memoria juntos. No elijas un modelo de una lista de niveles y lo fuerces sobre hardware inadecuado.*

Esta guía se centra en agentes de programación, no en prompts cortos de autocompletado. Un agente lee archivos, salidas de herramientas, errores del compilador y resultados de pruebas antes de escribir una solución. Esas entradas consumen contexto y el contexto cambia la decisión de hardware.

## El vídeo sirve como referencia

El siguiente vídeo compara modelos locales en varios niveles de memoria de GPU. Es útil por sus observaciones prácticas sobre la selección de modelos y sus resultados de hardware. Este artículo sigue un camino separado y organiza la decisión en torno al comportamiento de la memoria, el contexto del agente, el procesamiento de prompts y el coste total de propiedad.

{{< youtube id="C9M6iUFtVB4" enable="true" title="I Tested Every Local AI Model So You Don't Have To" description="Comparación práctica de modelos de IA locales en varios niveles de memoria de GPU, con atención a cargas de programación y límites del hardware." >}}

## Por qué fallan las listas de niveles

Una lista de niveles suele relacionar el número de parámetros con una cifra de memoria de GPU. El atajo sirve para una primera estimación. Deja de servir cuando un agente de programación empieza a leer un repositorio real.

Los pesos del modelo son la primera asignación. La **KV cache** es la asignación que crece. Guarda las claves y los valores de atención del contexto activo para que el tiempo de ejecución no tenga que recalcular todo el prompt después de cada token generado.

| Consumidor de memoria | Qué contiene | Por qué importa |
|---|---|---|
| **Pesos del modelo** | Los parámetros cuantizados | Requisito de carga única |
| **KV cache** | Notas del contexto activo | Crece con el prompt y la conversación |
| **Buffers del tiempo de ejecución** | Espacio temporal de cálculo | Varía según el backend y el tamaño del lote |
| **Instrucciones del agente** | Prompts del sistema y definiciones de herramientas | Usa contexto antes de recibir los archivos del proyecto |

**Que el archivo del modelo quepa en la tarjeta no demuestra que el agente sea utilizable.** El tiempo de ejecución necesita espacio para la caché, los buffers temporales, las definiciones de herramientas y la siguiente respuesta.

## El contexto es el presupuesto real

Los agentes de programación gastan contexto en más cosas que los archivos fuente. El presupuesto también incluye instrucciones del sistema, esquemas de herramientas, listados de directorios, salidas del shell, mensajes del compilador, resultados de pruebas y turnos anteriores de conversación.

Tres conexiones MCP con definiciones de herramientas detalladas suelen consumir varios miles de tokens antes de que el agente abra un archivo del proyecto. Un contexto predeterminado pequeño deja poco espacio para el código. El agente responde, pero pierde el conjunto de trabajo necesario para reparaciones de varios pasos.

Las [preguntas frecuentes del tiempo de ejecución de Ollama](https://docs.ollama.com/faq) indican un contexto predeterminado de 4.096 tokens. `OLLAMA_CONTEXT_LENGTH` cambia el valor predeterminado, mientras que `OLLAMA_NUM_PARALLEL` escala la memoria necesaria con el número de solicitudes simultáneas. Registra ambos valores antes de comparar un benchmark local con un resultado de una sola solicitud.

```bash
OLLAMA_CONTEXT_LENGTH=32768 OLLAMA_NUM_PARALLEL=1 ollama serve
```

Este ejemplo establece un valor predeterminado de 32K para una solicitud activa. No reserva 32K tokens para los archivos del proyecto. Las instrucciones, las definiciones de herramientas, la entrada y la salida comparten la ventana.

### Un registro de contexto sencillo

Antes de comparar GPU, registra estos valores:

- **Tamaño del proyecto:** archivos y líneas de código aproximadas en una tarea normal.
- **Sobrecarga de herramientas:** prompt del sistema, esquemas MCP, herramientas del shell e instrucciones del editor.
- **Carga del error:** longitud normal de la salida del compilador y de las pruebas.
- **Contexto objetivo:** el prompt más grande que quieres mantener sin truncarlo.
- **Margen de respuesta:** espacio reservado para el parche y la explicación previstos.

Usa el resultado como especificación de carga de trabajo. Un desarrollador que edita un archivo cada vez tiene una necesidad de memoria diferente de quien pide a un agente rastrear una API por un monorepo.

## La KV Cache cambia la clasificación

Dos modelos con un número de parámetros parecido suelen tener costes de contexto distintos. Un modelo denso con todas las capas contribuyendo a la caché creciente necesita más memoria que un modelo con un diseño de atención híbrido.

Uno de los modelos de programación 27B tratados en el material de referencia usa un conjunto limitado de capas de atención completa, mientras que las demás usan un resumen de tamaño fijo. El coste de contexto 128K indicado queda por debajo de 9GB para la caché. Según el informe, un modelo de tamaño similar con atención completa creciente en todas las capas necesita más de 21GB con la misma longitud de contexto.

Estas cifras describen arquitecturas de modelos y ajustes de tiempo de ejecución específicos. Trátalas como un motivo para inspeccionar la arquitectura, no como una fórmula universal de memoria.

| Comportamiento del modelo | Efecto sobre el contexto | Implicación para el hardware |
|---|---|---|
| **Atención completa en cada capa** | Gran crecimiento de la caché | Necesita más memoria para prompts largos |
| **Atención híbrida o deslizante** | Menor crecimiento de caché en algunas capas | Más margen de contexto con el mismo tamaño de modelo |
| **Mezcla de expertos** | Menos parámetros activos por token | Menos cálculo por token, pero todos los pesos necesitan almacenamiento |
| **Extensión de contexto largo** | Ventana de trabajo mayor | Más memoria de caché y más trabajo de procesamiento del prompt |

**Lee la arquitectura del modelo antes de comprar memoria.** El número de parámetros por sí solo oculta el coste de una sesión larga de programación.

## Elige según el nivel de memoria de GPU

### De cuatro a ocho GB

Los modelos densos pequeños siguen siendo la opción práctica. Caben en la tarjeta, responden rápido y funcionan bien para autocompletado, explicaciones breves y ediciones de archivos concretos.

Un modelo grande con descarga a CPU puede producir texto, pero el tiempo de respuesta suele convertirse en el límite. Un agente de programación necesita lecturas de archivos y llamadas a herramientas repetidas. Una configuración de cuatro tokens por segundo convierte cada reparación en una espera larga, aunque el modelo funcione técnicamente.

Los modelos de mezcla de expertos ofrecen otra vía. Una parte activa pequeña reduce la presión de cálculo, mientras el conjunto completo de pesos vive parcialmente en la memoria del sistema. Este enfoque requiere un sistema con mucha RAM y rutas de transferencia rápidas.

| Carga de trabajo | Dirección sugerida |
|---|---|
| **Autocompletado** | Modelo denso pequeño con prompt corto |
| **Ediciones de un archivo** | Modelo instruct pequeño con soporte de herramientas |
| **Agente para todo el repositorio** | Alquila una GPU mayor o aumenta primero la memoria del sistema |
| **Código privado bajo un NDA** | Usa un modelo local, pero acepta un alcance menor o ejecuciones más lentas |

**En este nivel, compra RAM del sistema antes de perseguir un modelo grande.** Un modelo pequeño estable supera a un modelo grande que pasa la mayor parte del tiempo moviendo datos por el bus.

### De doce a dieciséis GB

Este nivel abre la puerta a un modelo de programación 27B, pero la elección de cuantización se vuelve central. Una compilación estándar de 4 bits cercana a 17GB no cabe en una tarjeta de 16GB cuando se añade la sobrecarga del tiempo de ejecución.

Una compilación de 3 bits cercana a 13GB deja más espacio para el contexto. Una tarjeta de 12GB orienta la elección hacia una compilación de 2 bits o un modelo de mezcla de expertos más pequeño. La calidad depende del cuantizador y del proceso de calibración concretos, por lo que dos cargas con la misma profundidad de bits suelen producir resultados de programación distintos.

Comprueba estos puntos antes de descargar un modelo cuantizado:

- **Autor del cuantizador y notas de la versión**
- **Datos de calibración y resultados de evaluación**
- **Compatibilidad del tokenizador**
- **Pruebas de llamadas a herramientas**
- **Longitud de contexto con la cuantización elegida**
- **Soporte de tiempo de ejecución en Ollama, llama.cpp o el frontend elegido**

**No trates “2-bit” o “3-bit” como una descripción completa de la calidad.** Importan el método de empaquetado y el registro de calibración.

### De veinticuatro a treinta y dos GB

Este es el rango más flexible para un modelo de programación 27B. Una tarjeta de 24GB suele admitir una compilación de 4 bits con un contexto útil, pero una ventana completa de 128K puede superar la memoria restante. Una tarjeta de 32GB da más espacio al tiempo de ejecución para la caché y las asignaciones temporales.

Este rango también facilita justificar la propiedad. Una GPU gestiona la carga sin la complejidad de dividirla entre dos tarjetas. El sistema consume menos energía que una configuración multi-GPU y el soporte de software es más fácil de probar.

| Capacidad | Posición práctica |
|---|---|
| **24GB** | Modelo 4-bit sólido con límites de contexto que debes medir |
| **32GB** | Modelo 4-bit o 6-bit 27B con más margen de contexto |
| **48GB** | Mayor precisión o caché más grande sin cambiar el modelo principal |

**El rango de 24GB a 32GB es la zona lógica para tener hardware propio y trabajar a diario con código privado.** Evita el peor comportamiento de descarga sin obligar a instalar hardware de centro de datos en una caja de escritorio.

### Cuarenta y ocho GB o más

Más memoria no significa automáticamente un modelo nuevo. El mismo modelo 27B podría funcionar con precisión de 8 bits en una tarjeta de 48GB, con una caché mayor y menos compromisos. La mejora está en la consistencia, el espacio de contexto y la calidad de salida, no en un nivel nuevo de razonamiento.

Con 128GB, la decisión cambia. Un modelo de mezcla de expertos mucho mayor se vuelve posible, pero el procesamiento del prompt se convierte en una preocupación seria. Un modelo suele generar rápido mientras tarda en leer un repositorio grande o un resultado de herramienta nuevo.

**Para modelos grandes, mide por separado la velocidad de prellenado y la de decodificación.** Una respuesta rápida después de leer lentamente el prompt sigue sintiéndose lenta en un flujo de trabajo de agente.

## La velocidad de decodificación es solo la mitad de la prueba

La **velocidad de decodificación** mide los tokens generados por segundo. Responde a «¿A qué velocidad escribe el modelo?». La **velocidad de prellenado** mide el procesamiento del prompt. Responde a «¿A qué velocidad lee el modelo?».

Un agente pasa mucho tiempo leyendo. Cada llamada a una herramienta añade texto nuevo. Un archivo fuente largo, un stack trace o un registro de pruebas entra en el prompt antes de que comience la siguiente respuesta.

| Métrica | Experiencia del usuario |
|---|---|
| **Tokens de decodificación por segundo** | Rapidez con que aparece la respuesta tras el procesamiento |
| **Tokens de prompt por segundo** | Tiempo que espera el agente antes de que empiece la respuesta |
| **Tiempo hasta el primer token** | Retraso combinado del procesamiento del prompt y la configuración |
| **Retención del contexto** | Cantidad de estado del proyecto disponible durante la tarea |

**Haz benchmarks con tus tamaños de prompt.** Un prompt sintético corto oculta el coste más importante durante el trabajo con repositorios.

## Primero, los ajustes gratuitos del tiempo de ejecución

Las mejoras de hardware no son el primer paso de rendimiento. Prueba los ajustes del tiempo de ejecución antes de abrir una página de compra.

### Predicción de varios tokens

Algunas combinaciones de modelo y backend permiten predecir varios tokens futuros y verificarlos en una pasada. La función suele aparecer mediante un indicador de tiempo de ejecución o una configuración de borrador compatible.

Las pruebas indicadas en el material de referencia muestran grandes ganancias en algunas tarjetas de gama alta. Los resultados varían según el archivo del modelo, el backend, el controlador y la tarjeta. Las rutas de Apple Metal pueden no conservar la función necesaria durante la conversión.

### Nivel de razonamiento

Un modelo con el razonamiento máximo activado dedica más tiempo al trabajo interno antes de devolver un resultado. El razonamiento medio suele equilibrar mejor la reparación de código, sobre todo cuando la tarea ya incluye un mensaje de error claro y un archivo objetivo concreto.

Usa una matriz de prueba sencilla:

1. Ejecuta la misma tarea de corrección con razonamiento bajo, medio y alto.
2. Registra el tiempo hasta el primer token, el tiempo total, el éxito del parche y el resultado de la prueba.
3. Repite con un prompt corto y otro del tamaño de un repositorio.
4. Conserva el ajuste que produzca la mejor tarea completada, no la mayor tasa de tokens.

**El razonamiento medio con una ruta compatible de varios tokens es un buen punto de partida.** Verifica la calidad con tu propio código antes de convertirlo en el valor predeterminado.

## ¿Hardware local o GPU alquilada?

El cómputo alquilado gana para el trabajo ocasional. Pagas por sesiones activas en vez de comprar, refrigerar, actualizar y alimentar una tarjeta durante todo el año.

El hardware propio gana cuando la carga es frecuente, privada o sin conexión. También elimina las colas y ofrece un entorno estable para pruebas repetibles.

| Situación | Mejor primer paso |
|---|---|
| **Unas pocas sesiones al mes** | Alquila una GPU o usa una API |
| **Programación privada diaria** | Compra un sistema compatible de 24GB a 32GB |
| **Repositorio grande con recargas frecuentes** | Alquila primero y mide la velocidad de prellenado |
| **El código no sale del edificio** | Compra el sistema más pequeño que cumpla el objetivo de contexto |
| **Experimentar con un modelo nuevo** | Alquila antes de comprar hardware |

Calcula el punto de equilibrio con horas activas, no con horas del calendario. Incluye electricidad, almacenamiento, refrigeración, mantenimiento y el tiempo necesario para mantener el tiempo de ejecución operativo.

**Una GPU de gama alta comprada para experimentar de vez en cuando es un gasto de afición.** Un sistema de 24GB a 32GB usado a diario para trabajo privado tiene un argumento económico más sólido.

## Una mejor lista de compra

Usa este orden al comparar un modelo y una GPU:

1. **Define la tarea.** Autocompletado, reparación de un archivo, agente de repositorio o análisis de contexto largo.
2. **Mide el prompt.** Cuenta instrucciones normales del sistema, esquemas de herramientas, archivos y salidas de pruebas.
3. **Inspecciona el comportamiento de la caché.** Busca notas de arquitectura y mediciones de memoria de contexto.
4. **Elige una cuantización.** Comprueba los resultados de calidad de la carga concreta, no solo su cantidad de bits.
5. **Prueba prellenado y decodificación.** Usa prompts de tu propio repositorio.
6. **Ajusta el razonamiento.** Compara el tiempo de tarea completada en varios niveles de razonamiento.
7. **Prueba privacidad y mantenimiento.** Confirma dónde viaja el código fuente y quién mantiene el backend.
8. **Compara el coste de alquiler.** Usa las horas activas previstas e incluye la energía en la estimación del sistema propio.

## Recomendación final

**Por debajo de 12GB, ejecuta un modelo más pequeño o uno de mezcla de expertos con suficiente RAM del sistema.** No fuerces un modelo denso 27B en una configuración que pasa la mayor parte del tiempo descargando datos.

**De 12GB a 16GB, céntrate en la calidad de cuantización y en un objetivo de contexto controlado.** Una compilación 2-bit o 3-bit bien probada con soporte de herramientas es más útil que un archivo 4-bit que nunca encaja bien.

**De 24GB a 32GB, un modelo de programación 27B se convierte en el valor predeterminado práctico para el trabajo privado diario.** Mide el uso de contexto y la velocidad del prompt antes de asumir que está disponible toda la ventana anunciada.

**A partir de 48GB, dedica la memoria adicional a precisión, espacio de caché y sesiones estables antes de pasar a un modelo mayor.** Cuando el modelo supera el territorio de 128GB, la velocidad de lectura del prompt y la economía del alquiler merecen más atención que la capacidad bruta.

El nombre del modelo es solo el punto de partida. La pregunta útil es cuánto contexto del proyecto queda después de que el modelo, el tiempo de ejecución, las herramientas y la caché tomen su parte.

## Lecturas relacionadas

- [32GB de VRAM para Qwen 27B: guía de hardware de IA local](/articles/32gb-vram-qwen-27b-hardware-guide/), centrada en rutas de hardware para una carga 27B.
- [Benchmarks de GPU de Llama 3.1 8B y Qwen3.8 27B en Vast.ai](/articles/qwen38-27b-vast-ai-gpu-benchmark/), resultados medidos de GPU alquiladas y límites de contexto largo.
- [IA local en 2026: un modelo 27B supera a Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/), calidad del modelo, cuantización y economía del hardware local.
