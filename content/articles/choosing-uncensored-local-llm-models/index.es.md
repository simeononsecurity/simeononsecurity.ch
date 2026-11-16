---
title: "Cómo elegir un modelo de IA local sin censura"
date: 2026-11-15
lastmod: 2026-11-15
toc: true
draft: false
description: "Compara variantes locales por respuestas completas, capacidades conservadas, uso del contexto, cuantización y memoria VRAM necesaria."
genre: ["IA local", "IA autoalojada", "Seguridad de IA", "Equipo GPU"]
tags: ["IA local sin censura", "abliteración", "LLM local", "VRAM", "longitud de contexto", "cuantización", "Ollama", "Qwen3.8", "Gemma 4"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Una estación de trabajo local de IA con una tarjeta gráfica y monitores que muestran visualizaciones de modelos e inferencia"
coverCaption: ""
ref: ["/articles/local-ai-model-gpu-context-guide", "/articles/qwen38-27b-vast-ai-gpu-benchmark"]
---

**Cómo elegir un modelo:** evalúa cada variante por las respuestas útiles que completa, la calidad que conserva y la memoria que requiere tu carga de trabajo. Un número bajo de rechazos o una ficha de modelo popular no demuestra esos resultados.

La etiqueta **sin censura** no tiene una escala de rendimiento estándar. Quienes publican modelos la usan para distintas modificaciones de pesos, ajustes finos y plantillas de conversación. Compara cada candidato con su modelo original y pruébalo en las tareas que quieras ejecutar.

{{< youtube id="j-VqPVjztJE" enable="true" title="Probé todos los modelos locales de IA sin censura (de 8 GB a 32 GB de VRAM)" description="Comparación de variantes de modelos locales, respuestas completas, ajustes de contexto y niveles de memoria GPU." >}}

## Qué te dice la etiqueta

Un **modelo abliterado** ha recibido cambios en los pesos para modificar cierto comportamiento de rechazo. El artículo de 2024 sobre la dirección del rechazo demostró un método en 13 modelos de conversación abiertos. Las herramientas más recientes ofrecen otros enfoques. Por ejemplo, Heretic 2 documenta ablación de rango arbitrario y ablación direccional. La etiqueta de una ficha de modelo no indica qué comportamiento cambió ni qué efecto tuvo la modificación.

Mantén separadas estas cuatro propiedades al comparar modelos:

| Propiedad | Qué comprobar |
|---|---|
| **Comportamiento de rechazo** | ¿Qué solicitudes reciben un rechazo, una respuesta parcial o una respuesta completa? |
| **Capacidades conservadas** | ¿Cómo se comparan las tareas de conocimiento, razonamiento, programación y formato con el modelo original? |
| **Respuesta completa** | ¿Con qué frecuencia termina la generación antes del límite de tokens o de tiempo? |
| **Compatibilidad con el entorno** | ¿El archivo cuantizado exacto funciona con memoria suficiente para el contexto que necesitas? |

Un modelo modificado sigue siendo probabilístico. **Separa las comprobaciones de calidad:** precisión, fiabilidad y uso seguro. Mantén disponible un modelo normalmente alineado para tareas donde importen sus salvaguardas.

## Por qué el número de rechazos es una clasificación débil

**Una puntuación de rechazo** mide un resultado en un conjunto de indicaciones. Dice poco sobre la precisión factual, la longitud de las respuestas o si el modelo entrega una respuesta final antes de agotar el presupuesto de generación.

**La comparación de Qwen3.8-27B de Sapwell, de septiembre de 2026,** probó el modelo base y ocho variantes con la misma configuración de servicio. Su conjunto de 13 tareas midió conocimientos, matemáticas, programación y veracidad. Un conjunto separado de HarmBench contenía 400 solicitudes dañinas, y un juez LLM revisó las respuestas completas. Estos resultados cubren una familia de modelos, una GPU y un diseño de evaluación.

| Variante de Qwen3.8-27B en el estudio | Rechazos explícitos de 400 | Respuestas con razonamiento sin terminar |
|---|---:|---:|
| **Modelo base** | 381 | 0 % |
| **OrcaRouter** | 2 | 38 % |
| **Trohrbaugh** | 122 | 15 % |

El elevado número de rechazos del modelo base coincidió con menos respuestas sin terminar. El bajo número de rechazos de OrcaRouter coincidió con una tasa mayor de respuestas incompletas. Trohrbaugh conservó más rechazos y produjo menos respuestas incompletas. **Elige según tu tarea y los compromisos que aceptes.**

**Un estudio de 23 variantes de Gemma 4 E4B** encontró pérdidas importantes en algunas medidas de capacidad en la variante más descargada, mientras que una modificación menor se mantuvo cerca del modelo base en sus pruebas. La popularidad y las descargas describen su adopción. No miden la calidad.

No combines estas mediciones en una sola puntuación. **Separa las medidas:** rechazo, finalización, corrección y latencia. Registra también el conjunto de indicaciones, la revisión del modelo, la plantilla de conversación, el entorno, el contexto y el límite de salida. Cambiar cualquiera de esos ajustes altera el significado de la comparación.

## Diagnostica las respuestas vacías antes de sustituir un modelo

**Los tokens de razonamiento** consumen el límite de salida antes de que aparezca texto visible. Si el límite se agota durante el razonamiento interno, algunos entornos devuelven una respuesta vacía o truncada. Este resultado no equivale a un rechazo ni a una respuesta completa pero incorrecta.

**El benchmark Qwen3.6-27B de Sapwell** mostró cómo afecta esto a las puntuaciones principales. Las puntuaciones matemáticas sin procesar variaron mucho porque algunas ejecuciones nunca llegaron a la respuesta final. Entre las respuestas completas, los valores de precisión medidos fueron mucho más parecidos. El benchmark separó la capacidad de responder del agotamiento del presupuesto de razonamiento.

**Comprueba el motivo de detención y los registros del entorno** cuando una respuesta quede en blanco. Registra la longitud de la indicación, la asignación de contexto, el límite de tokens de salida, el tiempo transcurrido y si el modelo produjo un marcador de respuesta final. Luego repite la indicación con un límite de salida mayor si queda memoria en el equipo.

| Resultado | Categoría probable que debes investigar |
|---|---|
| **Texto de rechazo** | El modelo rechazó la solicitud. |
| **Salida vacía al llegar al límite de tokens** | La generación agotó el presupuesto de salida antes de dar una respuesta final. |
| **Salida truncada** | El límite de generación detuvo una respuesta incompleta. |
| **Error del entorno** | Falló el servidor, el archivo del modelo o la asignación de memoria. |
| **Respuesta completa pero incorrecta** | El modelo devolvió texto, pero no superó la comprobación de corrección. |

**Salida vacía:** confirma el resultado del entorno antes de llamar defecto del modelo a cada caso. Una ventana de contexto mayor no corrige automáticamente un límite de salida pequeño, una plantilla mal formada o un tiempo de espera de la aplicación.

## Reserva VRAM para los pesos y el contexto

El archivo del modelo es solo uno de los consumidores de memoria. El entorno también necesita espacio para la **caché KV**, que guarda el estado de atención de la indicación y la respuesta activas, además de los búferes de cálculo y otros procesos cargados. Aumentar la longitud del contexto aumenta el uso de memoria.

**La documentación actual de Ollama** indica ventanas de contexto predeterminadas de 4K con menos de 24 GiB de VRAM, 32K entre 24 y 48 GiB, y 256K con 48 GiB o más. Estos valores describen el comportamiento predeterminado del entorno. Comprueba el contexto asignado y la ubicación del procesador con `ollama ps`.

**Ejemplo en Linux:** este comando establece 16K como valor predeterminado para las nuevas sesiones del servidor Ollama:

```bash
OLLAMA_CONTEXT_LENGTH=16384 ollama serve
```

**Verifica el contexto asignado** frente al tamaño normal de las entradas y respuestas con el modelo cargado:

```bash
ollama ps
```

Las columnas `CONTEXT` y `PROCESSOR` muestran la asignación y si el modelo está en la GPU o parcialmente descargado de ella. **Asignación de contexto:** que aparezca un límite no garantiza que toda la ventana quepa en la VRAM.

### Puntos de partida según la memoria de la GPU

**Candidatos iniciales:** estas familias de modelos aparecieron en comparaciones de variantes de 2026. Los tamaños de archivo corresponden a repositorios de cuantización concretos. Confirma el archivo exacto, la compatibilidad del entorno y la memoria medida antes de considerar que una variante encaja.

| Memoria GPU | Candidato inicial | Restricción principal |
|---|---|---|
| **8 GB** | Gemma 4 E4B, como la variante `coder3101` | Mantiene pequeño el archivo de pesos. Reserva memoria para el contexto y los búferes del entorno. |
| **12 GB** | Gemma 4 12B, como el archivo GGUF Q4 de `TrevorJS` de 7,4 GB | Aporta más capacidad al modelo, pero deja menos espacio para un contexto largo que una variante menor. |
| **16 GB** | Un modelo menor o un archivo Q3 de Qwen3.8-27B | El repositorio de Qwen indica 13,72 GB para Q3_K_S. Quien publica el archivo lo califica como de baja calidad. El margen para contexto será limitado. |
| **24 GB** | Qwen3.8-27B Q4_K_S o Q4_K_M | El repositorio actual indica archivos de 16,71 GB y 17,77 GB. Reserva espacio para la caché y los búferes. |
| **32 GB** | Qwen3.8-27B Q6_K | El repositorio actual indica un archivo de 23,46 GB. Un archivo mayor deja menos memoria para el contexto que una cuantización menor. |

*Usa estas opciones como punto de partida. Los repositorios y las versiones cambian, y el tamaño del archivo por sí solo no predice la asignación del entorno ni la calidad de las respuestas.*

Las etiquetas de cuantización GGUF resumen una opción de codificación. **Diferencias entre repositorios:** los archivos con la misma profundidad de bits nominal no garantizan una calidad equivalente. Un repositorio de Qwen califica Q3_K_S como de baja calidad y Q4_K_M como su opción predeterminada. Antes de descargar, revisa el tamaño exacto, la ficha del modelo, el formato de indicaciones y los resultados de las pruebas.

**Para calcular el tamaño de la caché y comprobar la compatibilidad con una GPU local,** consulta la [guía de GPU y contexto para modelos locales](/articles/local-ai-model-gpu-context-guide/). Sus recomendaciones se centran en tareas de programación. Esta página se centra en el comportamiento de rechazo modificado y la evaluación.

## Inspecciona la plantilla de conversación y el origen del modelo

Una **plantilla de conversación** envuelve los mensajes en los tokens e instrucciones que espera el modelo. A veces, un paquete de modelo incluye una plantilla personalizada o un mensaje del sistema. Esos cambios afectan el comportamiento medido aunque los pesos subyacentes no cambien.

**Efecto de la plantilla:** Sapwell encontró una variante de Qwen3.8 cuyo paquete incluía una personalidad que indicaba al modelo que nunca rechazara ni advirtiera. Su afirmación de pocos rechazos dependía de la plantilla. Su comparación estandarizó las plantillas para que la prueba destacara las diferencias entre los pesos. Este control no demuestra que la plantilla incluida sea maliciosa o inutilizable.

**Antes de instalar:** verifica quién publica el modelo, el modelo base, la licencia, el proceso de conversión, el cuantizador, la plantilla y el historial de revisiones. Compáralo con el modelo original usando la misma plantilla y el mismo entorno. Si la ficha del modelo no indica el método ni la configuración de prueba, registra el origen como desconocido.

## Ejecuta una evaluación pequeña para tu carga de trabajo

**Crea un conjunto repetible de indicaciones** a partir de tareas habituales que te pertenezcan o que tengas permiso para probar. Incluye el trabajo que realizará el modelo, preguntas factuales con respuestas conocidas y solicitudes de formato con condiciones claras de aprobación. Añade algunos casos seguros que definan límites para que el comportamiento de rechazo siga formando parte de la decisión.

**Mantén constantes los ajustes de prueba** entre el modelo original y la variante modificada. No cambies el mensaje del sistema, la plantilla, la cuantización, la versión del entorno, el contexto, el límite de salida ni los ajustes de muestreo. Guarda la revisión del modelo o el hash del archivo con los resultados.

Registra cada resultado por separado:

- **Finalización:** respuesta final, rechazo, salida vacía, truncamiento o error del entorno.
- **Corrección:** aprobado o fallido según la respuesta esperada o una rúbrica.
- **Utilidad:** si la respuesta cumple los requisitos de la tarea.
- **Latencia:** tiempo hasta el primer token y tiempo total de generación.
- **Memoria:** contexto asignado, ubicación en la GPU y VRAM máxima.
- **Comportamiento de seguridad:** rechazo o continuación apropiados en cada caso límite.

Repite el conjunto después de cambiar una sola variable. Si la respuesta se completa al aumentar el límite de salida, el primer fallo se debió al presupuesto. Si las respuestas siguen incompletas, revisa la plantilla, el modo de razonamiento, el entorno y la revisión del modelo. **Conserva la variante solo si mejora tu tarea objetivo sin pérdidas inaceptables de precisión o seguridad.**

## Mantén la implementación aislada

**Privacidad:** la inferencia local depende de toda tu pila. Revisa la interfaz, los registros, las extensiones, la telemetría y las rutas de red. Trata los pesos no confiables y las plantillas personalizadas como código y configuración de terceros.

**Acceso público:** nunca expongas el endpoint del modelo directamente a Internet. Aísla el acceso a herramientas y usa variantes modificadas solo para trabajos autorizados. Para acceder a distancia, coloca el endpoint detrás de una puerta de enlace privada con autenticación, límites de solicitudes y aislamiento de red. El artículo original sobre la dirección del rechazo señala las implicaciones de seguridad de las modificaciones que eliminan rechazos.

## Conclusión

**Regla de decisión:** elige el modelo con los resultados verificados más sólidos en tus propias tareas. Usa los rechazos como una medida y luego comprueba la finalización de las respuestas, la corrección, el comportamiento de la plantilla y el margen de VRAM. Empieza con un archivo adecuado para tu GPU, configura el contexto para tu carga de trabajo y compáralo con el modelo original con los mismos ajustes.

**Para calcular la GPU,** compara estos resultados con el [benchmark de alquiler de GPU para Qwen 27B](/articles/qwen38-27b-vast-ai-gpu-benchmark/). Alquila o pide prestado equipo antes de comprarlo si no tienes claro el archivo exacto o el contexto que necesitas.

## Fuentes

- [Benchmark de abliteración de Qwen3.8-27B](https://nathan.sapwell.net/posts/qwen38-27b-abliteration/), Nathan Sapwell, 6 de septiembre de 2026.
- [Benchmark de abliteración de Qwen3.6-27B](https://nathan.sapwell.net/posts/qwen36-27b-abliteration/), Nathan Sapwell, 2026-05-17.
- [Benchmark de variantes de Gemma 4 E4B](https://nathan.sapwell.net/posts/gemma4-e4b-abliteration/), Nathan Sapwell, 1 de agosto de 2026.
- [Benchmark de variantes de Gemma 4 12B](https://nathan.sapwell.net/posts/gemma4-12b-abliteration/), Nathan Sapwell, 28 de agosto de 2026.
- [El rechazo en los modelos de lenguaje está mediado por una sola dirección](https://arxiv.org/abs/2406.11717), Arditi y otros, 2024.
- [Documentación del proyecto Heretic](https://github.com/p-e-w/heretic/).
- [Ficha oficial del modelo Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B).
- [Documentación de Ollama sobre la longitud del contexto](https://docs.ollama.com/context-length).
- [Ficha del modelo Gemma 4 E4B `coder3101`](https://huggingface.co/coder3101/gemma-4-E4B-it-heretic).
- [Archivos GGUF de Gemma 4 12B de TrevorJS](https://huggingface.co/TrevorJS/gemma-4-12B-it-uncensored-GGUF).
- [Archivos GGUF de OrcaRouter Qwen3.8-27B](https://huggingface.co/bartowski/orcarouter_Qwen3.8-27B-Uncensored-GGUF).
- [Formato GGUF y tipos de cuantización](https://huggingface.co/docs/hub/en/gguf), documentación de Hugging Face.
- [Fuente en vídeo: Probé todos los modelos locales de IA sin censura (de 8 GB a 32 GB de VRAM)](https://www.youtube.com/watch?v=j-VqPVjztJE).
