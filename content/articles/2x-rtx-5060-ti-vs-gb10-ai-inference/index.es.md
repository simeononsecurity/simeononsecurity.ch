---
title: "2x RTX 5060 Ti frente a GB10: benchmark local de IA con cinco modelos y contexto 256K"
date: 2026-10-10
lastmod: 2026-11-07
toc: true
draft: false
description: "Comparación de RTX 5060 Ti y GB10 con cinco modelos, más un benchmark de Qwen3.8 Flash-Next en Strata en el mismo host hasta 256K de contexto."
genre: ["Inteligencia artificial", "IA local", "Hardware GPU", "Benchmarking", "Hardware informático"]
tags: ["RTX 5060 Ti", "GB10", "DGX Spark", "Qwen3.8", "Qwen3.8 Flash-Next", "GSQ-RCO", "Qwen4Exp", "Strata", "Qwen3.5", "Qwen3.6", "GPT-OSS", "Nemotron", "LLM local", "inferencia local", "memoria unificada", "VRAM", "benchmark GPU", "contexto largo", "sobrecarga PCIe", "hardware de IA", "NVIDIA Blackwell", "rendimiento LLM", "memoria GPU"]
cover: "/img/cover/nvidia-rtx-5060-ti-vs-gb10-memory-performance-comparison.webp"
coverAlt: "Ilustración de dos tarjetas gráficas NVIDIA RTX 5060 Ti a la izquierda y un sistema NVIDIA GB10 a la derecha, resaltados con colores vivos sobre un fondo oscuro."
coverCaption: "El rendimiento de los modelos locales depende de la arquitectura de memoria, el modelo elegido y la longitud del contexto."
---

**Dos tarjetas RTX 5060 Ti de 16 GB ofrecen 32 GB de VRAM en total.** Un sistema NVIDIA GB10 ofrece 128 GB de memoria unificada coherente. El nuevo benchmark de cinco modelos presenta un resultado más equilibrado que la prueba anterior, limitada a Qwen.

Con la configuración 256K, el sistema de dos tarjetas genera más rápido en cuatro de los cinco modelos. El GB10 supera claramente al otro sistema con Qwen3.8 27B y conserva más memoria para modelos, contexto y asignaciones del runtime. La mejor opción depende del modelo y la carga de trabajo.

Una prueba separada en el mismo host comparó Qwen3.8-Flash-Next IQ2_XS en Strata con Qwen3.8 27B Q4_K_M denso en Ollama. La mediana de generación tras el calentamiento fue de 92.8 tokens por segundo para Flash-Next, con un prompt de 260,446 tokens. Qwen3.8 denso alcanzó 0.939 tokens por segundo con un prompt de 260,444 tokens.

El NVIDIA GB10 utiliza 128 GB de memoria unificada coherente. NVIDIA indica que la plataforma GB10 tiene 128 GB de memoria unificada LPDDR5x y un TDP de chip de 140 W. Cada RTX 5060 Ti usa 16 GB de GDDR7, una interfaz de memoria de 128 bits y una potencia gráfica total de 180 W. Las [especificaciones de NVIDIA RTX 5060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/) y las [especificaciones de NVIDIA GB10](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) describen la diferencia de hardware.

**Los dos sistemas exponen la memoria de forma distinta.** Dos tarjetas crean dos grupos separados de 16 GB. El GB10 coloca el modelo, los datos de contexto, los búferes del runtime y las asignaciones del sistema operativo en un espacio de direcciones compartido.

## Comparación de memoria

| Sistema | Memoria | Modelo de memoria | Potencia indicada |
|---|---:|---|---:|
| **2x RTX 5060 Ti 16 GB** | 32 GB en total | Dos grupos de memoria GPU separados | 360 W GPU en total |
| **Sistema GB10** | 128 GB | Memoria del sistema unificada coherente | TDP GB10 de 140 W |

El GB10 no gana todas las pruebas de rendimiento, ya que la LPDDR5x no iguala el ancho de banda de las GPU discretas. Su ventaja procede de la capacidad y la ubicación. CPU y GPU comparten el mismo espacio de direcciones, así que el conjunto de trabajo no tiene que caber en dos dispositivos aislados de 16 GB.

El sistema de dos tarjetas afronta un problema de ubicación: el modelo debe repartirse entre ambas y el runtime debe mover datos entre ellas. El tráfico PCIe añade latencia y consume ancho de banda. Según las especificaciones de NVIDIA, la RTX 5060 Ti tampoco admite NVLink.

## Benchmark de cinco modelos

La prueba actualizada utilizó la misma matriz de solicitudes en ambos sistemas. Incluyó cinco modelos de Ollama con contextos de 4K, 16K, 32K, 64K, 128K y 256K. Cada solicitud generó 128 tokens con temperatura 0.

Las etiquetas de los modelos probados fueron:

- **Qwen3.8 27B:** `qwen3.8:27b`
- **GPT-OSS 20B:** `gpt-oss:20b`
- **Qwen3.6 35B-A3B:** `qwen3.6:35b`
- **Qwen3.5 35B-A3B:** `qwen3.5:35b-a3b-q4_K_M`
- **Nemotron 3.5 Lightning 30B-A3B:** `nemotron-3.5-lightning:30b-a3b-q4_K_M`

El sistema de dos tarjetas utilizó dos RTX 5060 Ti de 16 GB. El sistema GB10 utilizó 128 GB de memoria unificada. Las pruebas usaron Ollama, versión 0.34.2 en el sistema de dos tarjetas y versión 0.40.2 en el GB10.

### Velocidad de generación

La velocidad de generación mide los tokens producidos después de procesar el prompt. Esta métrica es especialmente importante durante una conversación interactiva.

Sistema con dos RTX 5060 Ti:

| Contexto | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 91.518 | 162.027 | 117.547 | 156.104 | 55.654 |
| 16K | 87.176 | 161.377 | 112.903 | 140.596 | 51.656 |
| 32K | 82.372 | 157.055 | 106.455 | 144.833 | 47.369 |
| 64K | 74.661 | 135.106 | 95.979 | 125.008 | 38.863 |
| 128K | 62.767 | 130.924 | 79.572 | 115.352 | 26.399 |
| 256K | 67.853 | 106.221 | 58.947 | 67.159 | 1.079 |

GB10:

| Contexto | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 62.199 | 98.648 | 72.405 | 100.906 | 32.985 |
| 16K | 56.764 | 94.366 | 69.782 | 95.448 | 32.939 |
| 32K | 53.257 | 98.175 | 64.055 | 95.025 | 29.772 |
| 64K | 49.201 | 96.132 | 58.428 | 84.528 | 25.625 |
| 128K | 40.637 | 80.238 | 48.108 | 74.579 | 22.294 |
| 256K | 43.688 | 68.043 | 36.649 | 62.115 | 22.371 |

A 256K, el sistema de dos tarjetas generó más rápido con GPT-OSS, Nemotron, Qwen3.5 y Qwen3.6. El GB10 superó ampliamente al otro sistema con Qwen3.8: la velocidad cayó a 1.079 tokens por segundo en el sistema de dos tarjetas, mientras que el GB10 produjo 22.371 tokens por segundo.

El resultado de Qwen3.6 está ajustado: el sistema de dos tarjetas alcanzó 67.159 tokens por segundo y el GB10 llegó a 62.115. El resultado no respalda una afirmación universal de que la memoria unificada siempre gana o que siempre ganan dos GPU discretas.

### Velocidad de procesamiento del prompt

El procesamiento del prompt mide la rapidez con que el runtime lee el contexto de entrada antes de generar. Es importante para documentos largos y para recargar el contexto repetidamente.

Sistema con dos RTX 5060 Ti:

| Contexto | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 4745.9 | 2409.0 | 2701.7 | 464.3 | 783.9 |
| 16K | 7617.0 | 3031.8 | 4175.3 | 2654.0 | 840.1 |
| 32K | 8099.5 | 3074.2 | 4335.8 | 2623.2 | 811.2 |
| 64K | 6809.5 | 2893.0 | 4129.9 | 2400.4 | 727.8 |
| 128K | 5089.9 | 2362.7 | 3084.0 | 1723.6 | 546.1 |
| 256K | 5838.3 | 1813.2 | 2229.1 | 1011.0 | 251.3 |

GB10:

| Contexto | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 3295.5 | 576.0 | 2067.9 | 628.8 | 756.9 |
| 16K | 4675.5 | 3006.7 | 2691.2 | 2556.3 | 812.6 |
| 32K | 4571.4 | 3077.9 | 2691.7 | 2563.9 | 794.1 |
| 64K | 3704.7 | 3066.9 | 2585.3 | 2444.9 | 714.0 |
| 128K | 2857.0 | 2802.9 | 2360.4 | 2229.9 | 655.5 |
| 256K | 3243.4 | 2325.4 | 1938.5 | 1817.6 | 535.1 |

A 256K, el sistema de dos tarjetas procesó mejor los prompts de GPT-OSS y Qwen3.5. El GB10 lideró con Nemotron, Qwen3.6 y Qwen3.8. La arquitectura del modelo y el comportamiento del runtime importan tanto como la interfaz de memoria.

## Benchmarks complementarios de Qwen3.8 Flash-Next

Tres pruebas adicionales midieron paquetes GGUF de Qwen3.8 Flash-Next en el sistema de dos RTX 5060 Ti, con contextos de 4K y 16K. Cada fila indica la referencia exacta del modelo en Hugging Face y su cuantización.

| Modelo exacto | Cuantización | Generación 4K | Generación 16K |
|---|---:|---:|---:|
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS) | IQ2_XS | 31.77 tok/s | 28.20 tok/s |
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ3_S) | IQ3_S | 24.54 tok/s | 22.60 tok/s |
| [`hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M`](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF/tree/main) | Q4_K_M | 17.91 tok/s | 17.02 tok/s |

El paquete IQ2_XS logró el mayor rendimiento del grupo: 31.77 tokens por segundo a 4K, frente a 24.54 de IQ3_S y 17.91 de Q4_K_M. A 16K se mantuvo el mismo orden: 28.20, 22.60 y 17.02 tokens por segundo.

Ejecuta las mismas referencias exactas de modelos con Ollama:

```bash
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S
ollama run hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M
```

Estos resultados complementarios anteriores corresponden a un sistema de dos GPU. Son independientes de la matriz de solicitudes comparables entre RTX 5060 Ti y GB10. El registro proporcionado identifica las referencias exactas de los modelos, las cuantizaciones, los contextos solicitados y la velocidad de generación. No incluye los digest de manifiestos resueltos, el recuento de tokens del prompt procesados, la longitud de salida, el estado térmico, la división entre dispositivos, la CPU, la RAM del sistema, la refrigeración ni la fecha de medición.

## Strata frente a Ollama denso a 256K

**Un segundo benchmark del 14 de octubre de 2026 comparó dos pilas de modelos y runtimes en el mismo host con dos RTX 5060 Ti.** La referencia densa utilizó [`qwen3.8:27b`](https://ollama.com/library/qwen3.8:27b), un modelo Qwen35 de 27.3 mil millones de parámetros en Q4_K_M. La pila Flash utilizó [Qwen3.8-Flash-Next IQ2_XS](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS), un modelo Qwen4Exp mixture-of-experts en un paquete nativo unificado de Strata.

Es una comparación a nivel de pila. La arquitectura del modelo, la cuantización, el empaquetado, el enrutamiento de expertos y el motor de inferencia cambiaron a la vez. Las variantes Flash IQ3_S y Q4_K_M quedaron fuera de esta prueba.

### Sistema y método de prueba

| Componente | Configuración registrada |
|---|---|
| **GPU** | 2x NVIDIA GeForce RTX 5060 Ti, 16 GiB cada una, compute capability 12.0 |
| **Conexión GPU** | PCIe 4.0 x4 por tarjeta, topología PHB, sin NVLink |
| **CPU** | AMD Ryzen 9 5900XT, 32 subprocesos |
| **Memoria del host** | 62 GiB de RAM y 15 GiB de swap |
| **Controlador NVIDIA** | 595.99.02 |

El banco de pruebas generó registros sintéticos numerados. Cada fila seguía el formato `Record 00001: alpha beta gamma delta epsilon zeta eta theta iota kappa.` La instrucción exigía escribir primero `BENCHMARK_OK` y después una síntesis técnica concisa hasta el límite de salida. Los seis prompts contenían 180, 720, 1,500, 3,100, 6,200 y 12,400 registros.

Cada ejecución usó temperatura 0, seed 42 y una longitud máxima de salida de 128 tokens. Para cada contexto, se hizo un calentamiento y luego cinco solicitudes medidas. Las pruebas de Ollama usaron `/api/generate` y las de Strata usaron `/v1/chat/completions`. Todas las solicitudes medidas terminaron sin errores de API.

Los controles de decodificación no estaban igualados. Strata definió explícitamente `reasoning_effort` como `none` y deshabilitó el razonamiento mediante su plantilla de chat. La solicitud densa de Ollama no envió `think: false`, y una comprobación posterior encontró salida densa en los campos de razonamiento y respuesta. El resultado de generación corresponde a estos modos de decodificación concretos.

| Configuración de contexto | Tokens del prompt denso | Tokens del prompt Flash |
|---:|---:|---:|
| **4K** | 3,824 | 3,826 |
| **16K** | 15,164 | 15,166 |
| **32K** | 31,544 | 31,546 |
| **64K** | 65,144 | 65,146 |
| **128K** | 130,244 | 130,246 |
| **256K** | 260,444 | 260,446 |

Los encabezados de ambos modelos declaraban un contexto máximo de 262,144 tokens. Los prompts emparejados diferían en dos tokens en cada punto de control.

### Mediana de velocidad de generación tras el calentamiento

Cada mediana cubre cinco solicitudes medidas después de un calentamiento. Cada solicitud densa reutilizó todos los tokens del prompt salvo cuatro. Cada solicitud Flash reutilizó todos salvo siete. La tabla mide el rendimiento de decodificación en caliente con caché de prefijo, no la latencia de extremo a extremo en frío.

| Contexto | Flash IQ2_XS en Strata | Denso Q4_K_M en Ollama | Ventaja de Flash |
|---:|---:|---:|---:|
| **4K** | 98.4 tok/s | 65.0 tok/s | 1.51x |
| **16K** | 96.8 tok/s | 60.6 tok/s | 1.60x |
| **32K** | 95.3 tok/s | 64.4 tok/s | 1.48x |
| **64K** | 89.6 tok/s | 51.2 tok/s | 1.75x |
| **128K** | 92.9 tok/s | 31.5 tok/s | 2.95x |
| **256K** | 92.8 tok/s | 0.939 tok/s | 98.9x |

La pila Flash se mantuvo cerca de 90 tokens por segundo entre 64K y 256K. Qwen3.8 denso se ralentizó mucho después de 64K y llegó a 0.939 tokens por segundo a 256K. La respuesta Flash de 256K terminó con normalidad tras 67 tokens. La ejecución densa alcanzó el límite de salida de 128 tokens.

### Procesamiento del prompt en la primera solicitud

| Contexto | Primera solicitud Flash | Primera solicitud densa |
|---:|---:|---:|
| **4K** | 1,134 tok/s | 832 tok/s |
| **16K** | 2,013 tok/s | 856 tok/s |
| **32K** | 2,386 tok/s | 799 tok/s |
| **64K** | 2,509 tok/s | 690 tok/s |
| **128K** | 2,538 tok/s | 489 tok/s |
| **256K** | 2,399 tok/s | 214 tok/s |

La primera solicitud densa procesó el prompt completo en cada punto de control. Strata informó que reutilizó 16,384 tokens de prefijo a 64K, 49,152 a 128K y 114,688 a 256K. Considera las velocidades Flash de 64K a 256K como rendimiento de continuación de la primera solicitud, no como prefill completo sin caché.

A 256K, Strata procesó la primera solicitud en 60.8 segundos. Ollama tardó alrededor de 1,215.4 segundos. La reutilización del prefijo impide comparar directamente el prefill en frío en este punto de control.

### La ubicación del runtime explica la diferencia con contexto largo

Ollama 0.34.2 usó llama-server 0.4.1-dev con descarga de capas CUDA, la plantilla ChatML y decodificación especulativa MTP con un ancho máximo de borrador de cuatro. El tamaño de batch y microbatch fue 1,024 a 32K y 512 entre 64K y 256K. Las 66 capas densas permanecieron en las GPU a 32K y 64K. A 128K, 63 de 66 capas permanecieron en las GPU y 1,404 MiB pasaron a memoria asignada a la CPU. A 256K, 42 de 66 capas permanecieron en las GPU y 6,002 MiB pasaron a memoria asignada a la CPU. La tasa de aceptación MTP a 256K fue de aproximadamente 69.4 por ciento.

Strata 0.1.44.1 con CUDA 13.0.3 mantuvo sus 48 capas repartidas entre las dos GPU. La configuración 4K y 16K colocó las capas 0 a 23 en la primera GPU y las capas 24 a 47 en la segunda. Esta pasada utilizó una reserva automática de 700 MiB de VRAM y 16,047 espacios de expertos residentes.

La configuración de 32K a 256K colocó las capas 0 a 24 en la primera GPU y las capas 25 a 47 en la segunda. Esta pasada utilizó prefill automático, una probabilidad mínima especulativa de 0.5, almacenamiento KV INT8, 32,768 celdas KV residentes por capa QSA, una reserva de 832 MiB de VRAM, una caché de expertos de 15,318 espacios y 21,024 MiB, y decodificación especulativa MTP con un ancho máximo de borrador de cuatro.

El digest del blob nativo de Strata y PLE fue `sha256:1473e0664c2017095f9164b6d617d7a71893452c1180c83002c4f28fc8c2b0da`. La ejecución también dependió de un perfil de expertos y un paquete de borrador MTP sin digest inmutables publicados.

La ejecución de Strata usó el modo predeterminado de omisión de la cola de rutas. Este ajuste modifica ligeramente la salida del modelo y limita el resultado a la configuración registrada del runtime. Las respuestas Flash tenían marcadores `BENCHMARK_OK`. Las solicitudes densas no devolvieron errores de API, pero el banco principal no capturó el marcador. Sus filas sin procesar registraron cero caracteres de respuesta. Una comprobación posterior encontró salida en los campos de respuesta y razonamiento, y confirmó `BENCHMARK_OK` en la respuesta.

La configuración 4K y 16K registró una solicitud con 409 MiB libres y recomendó una reserva de 832 MiB. La configuración de contexto largo registró una solicitud con 481 MiB libres y recomendó una reserva de 896 MiB. Ambos valores quedaron por debajo del umbral de paginación del controlador de 512 MiB. Ninguna solicitud falló, pero estos estados de poca memoria afectan la repetibilidad.

**Considera la cifra 98.9x como un resultado de contexto largo para toda la pila, no como prueba de una ventaja de 98.9x del motor por sí solo.** La prueba aísla el host, pero no el modelo, la cuantización ni el runtime.

## La longitud real del prompt importa

El contexto solicitado no equivale al número de tokens del prompt procesados. Con la configuración 256K, las pruebas de Qwen3.5, Qwen3.6, Nemotron y Qwen3.8 procesaron entre 171,359 y 171,365 tokens reales del prompt en ambos sistemas.

GPT-OSS procesó 65,538 tokens reales del prompt en la configuración 256K en ambos sistemas. Por lo tanto, su fila de 256K no representa la misma longitud de entrada que la de los demás modelos.

El resultado de Qwen3.8 a 256K muestra la mayor diferencia. El sistema de dos tarjetas procesó 171,359 tokens del prompt a 251.3 tokens por segundo y generó a 1.079 tokens por segundo. El GB10 procesó el mismo número de tokens a 535.1 por segundo y generó a 22.371 tokens por segundo.

**La configuración del contexto indica el límite solicitado.** El recuento real de tokens del prompt demuestra la carga que completó el runtime.

## Por qué sigue importando la VRAM agregada

### 1. El modelo no ve una sola tarjeta de 32 GB

Dos GPU no combinan su memoria en un único espacio de direcciones local. Un runtime model-parallel reparte capas o tensores entre dispositivos. Cada dispositivo aún necesita espacio para los pesos asignados, los búferes temporales y parte del estado del contexto.

La capacidad utilizable es menor que la suma simple. La sobrecarga exacta depende del formato del modelo, la cuantización, el backend de inferencia, la división de tensores y la longitud del contexto.

### 2. La memoria de contexto crece durante la generación

Los pesos del modelo son solo una parte del presupuesto de memoria. La caché de clave-valor (KV cache) almacena datos de atención de tokens anteriores. Los contextos más largos requieren más memoria de caché. Una prueba 4K no predice un despliegue 128K o 256K.

Los nuevos resultados muestran límites diferentes según el modelo. A 256K, Qwen3.8 sufre una caída grave de generación en el sistema de dos tarjetas. Los otros cuatro modelos mantienen una velocidad útil en ambos sistemas. La capacidad de memoria sigue siendo importante porque determina qué combinaciones de modelo y contexto caben junto con las asignaciones del runtime.

### 3. Las transferencias PCIe tienen un coste

Cuando el runtime mueve activaciones o tensores entre GPU, la transferencia cruza la interconexión del host. Esto crea puntos de sincronización y añade latencia a cada paso. El impacto depende de la ubicación de los tensores, la arquitectura del modelo, la cuantización y la longitud del contexto.

Esto no vuelve inútil un sistema con dos GPU. Significa que la configuración del runtime y el modelo determinan el resultado. Un benchmark que solo informa del procesamiento del prompt a 4K omite este coste.

### 4. La eficiencia energética sigue siendo una ventaja del sistema

El GB10 ofrece más capacidad de memoria con una potencia indicada del chip o GPU menor. Dos RTX 5060 Ti suman 360 W de potencia GPU, sin contar el resto del sistema. NVIDIA indica un TDP de 140 W para el GB10.

**El GB10 cambia el máximo rendimiento de varios modelos por más capacidad, un conjunto de trabajo compartido y una potencia GPU indicada menor.** El sistema de dos tarjetas ofrece más rendimiento medido en varios modelos MoE recientes.

## El sistema 5060ti-x2 cuesta mucho menos

Una estación de trabajo completa con dos RTX 5060 Ti de 16 GB figuraba por **$3,479** el 10 de octubre de 2026. La configuración incluye Intel Ultra 7 265K, placa base Z890, 32 GB de DDR5, almacenamiento de 1 TB, fuente de alimentación de 1,000 W y ambas GPU. [Consulta la oferta completa de la estación con dos GPU](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white).

El marketplace estadounidense de NVIDIA anuncia el DGX Spark de 128 GB por **$6,950**. La oferta incluye 128 GB de memoria unificada coherente y 4 TB de almacenamiento NVMe, pero indica que no hay existencias. [Consulta la oferta actual del DGX Spark de NVIDIA](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/).

La plataforma para desarrolladores AMD Ryzen AI Halo ofrece otro punto de comparación. Micro Center anuncia este sistema Strix Halo por **$3,999.99**, con 128 GB de memoria unificada LPDDR5x y 2 TB de almacenamiento. Strix Halo suele estar en la misma categoría práctica de IA local que los sistemas GB10, aunque las pruebas independientes suelen medir una ventaja del GB10 en rendimiento y madurez del software. [Consulta la oferta actual de Linux en Micro Center](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false) y [lee la reseña de Strix Halo frente a GB10](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4).

| Sistema completo | Precio publicado el 10 de octubre de 2026 | Diferencia de precio |
|---|---:|---:|
| **Estación 5060ti-x2** | $3,479 | Referencia |
| **AMD Ryzen AI Halo, Strix Halo** | $3,999.99 | $520.99 más |
| **128 GB GB10 DGX Spark** | $6,950 | $3,471 más |

El GB10 ofrece un grupo de memoria unificada mayor y una potencia GPU indicada menor. El sistema AMD ofrece la misma clase de memoria de 128 GB por unos $4,000. La estación 5060ti-x2 sigue costando alrededor del **50% del precio publicado del GB10**, antes de impuestos y envío.

Son precios publicados por distintos vendedores, no una cesta minorista controlada. El sistema 5060ti-x2 también tiene menos memoria del sistema y almacenamiento. Las ofertas actuales de RTX 5060 Ti de 16 GB rondan los **$789 a $830 por tarjeta**, muy por encima del precio de lanzamiento de $429. Por eso, la ventaja de precio del sistema de dos tarjetas se mantiene durante la actual subida de precios de GPU. [Consulta los precios actuales de RTX 5060 Ti](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/).

## Qué significa para las cargas de IA local

Una configuración de dos tarjetas de 16 GB ejecuta varios modelos cuantizados de 27B a 35B con contextos largos. El benchmark no señala un único ganador para todos los modelos.

Elige el sistema de dos tarjetas si valoras:

- **Mayor velocidad de generación con GPT-OSS, Nemotron, Qwen3.5 y Qwen3.6** en esta prueba.
- **Mayor rendimiento con contextos cortos** en los cinco modelos.
- **Menor coste de compra** que el sistema GB10 anunciado.
- **Compatibilidad del software con GPU discretas de NVIDIA** y futuras pruebas de modelos.

Elige el GB10 si valoras:

- **Qwen3.8 27B a 256K**, donde el GB10 genera más de 20 veces más rápido.
- **Un único grupo de memoria de 128 GB** con más espacio para pesos del modelo, caché KV y búferes del runtime.
- **Menor potencia indicada de GPU o chip** que dos tarjetas discretas.
- **Menos restricciones de ubicación entre dispositivos** para modelos que exigen la configuración de dos tarjetas.

Esto coincide con las recomendaciones de dimensionamiento de [¿Bastan 16 GB de VRAM para trabajar en serio con LLM locales?](/articles/is-16gb-vram-enough-local-llm/), que trata los pesos, el contexto y las asignaciones del runtime como un solo presupuesto. La [guía de 32 GB de VRAM para Qwen 27B](/articles/32gb-vram-qwen-27b-hardware-guide/) llega a la misma conclusión para sistemas de dos tarjetas. La capacidad agregada no equivale al margen utilizable.

Antes de comprar hardware para cualquier despliegue con contexto largo, hazte cuatro preguntas:

- **¿Cabe la cuantización requerida junto con los búferes del runtime?** Los pesos del modelo por sí solos no determinan la memoria necesaria.
- **¿Cabe el contexto sin presionar demasiado la caché KV?** Los prompts largos cambian el resultado.
- **¿El runtime divide el trabajo entre dispositivos de forma eficiente?** Las transferencias PCIe y la ubicación de tensores afectan a cada token generado.
- **¿El sistema completa el contexto objetivo?** Un resultado rápido a 4K no compensa una carga 256K fallida.

**El nuevo benchmark responde a estas preguntas para cada modelo.** A 256K, Qwen3.8 favorece claramente al GB10. En esta configuración concreta, los otros cuatro modelos generan más rápido en el sistema de dos tarjetas. El grupo de memoria unificada más grande sigue ofreciendo más margen de capacidad, aunque no alcance el mayor rendimiento medido.

El mismo hardware de dos GPU también registró una mediana de 92.8 tokens por segundo tras el calentamiento a 256K con Flash-Next IQ2_XS en Strata. Este resultado separado no cambia la conclusión de Qwen3.8 denso frente a GB10. Flash-Next utiliza otra arquitectura mixture-of-experts, cuantización, paquete, runtime y modo de decodificación. Este conjunto de datos no incluye un resultado equivalente de Flash-Next en GB10.

## Conclusión

**El sistema con dos RTX 5060 Ti genera más rápido para cuatro de los cinco modelos probados a 256K.** También cuesta aproximadamente la mitad que el GB10 anunciado. El GB10 sigue siendo mejor opción para Qwen3.8 27B a 256K, para disponer de más margen de memoria y para cargas que aprovechan un único grupo coherente de memoria.

El resultado anterior, limitado a Qwen, sugería una victoria sencilla del GB10. La prueba actualizada con cinco modelos muestra por qué esa conclusión era demasiado amplia. La arquitectura del modelo, la versión del runtime, la ubicación de los tensores y el comportamiento del contexto afectan al resultado.

Si ejecutas GPT-OSS, Nemotron 3.5 Lightning, Qwen3.5 o Qwen3.6, el sistema de dos tarjetas generó más rápido en este benchmark. Si ejecutas Qwen3.8 27B a 256K, el GB10 mantuvo una velocidad de generación útil mientras el sistema de dos tarjetas casi se detuvo.

**La capacidad de memoria y el rendimiento son criterios de compra distintos.** El GB10 ofrece cuatro veces la memoria agregada y un conjunto de trabajo compartido más sencillo. El sistema de dos tarjetas ofrece mayor rendimiento observado en la mayoría de los modelos probados a un precio anunciado mucho menor.

El resultado de Strata aporta otra lección. La ubicación del runtime, la arquitectura del modelo y el modo de decodificación cambiaron el resultado 256K en el mismo host de dos tarjetas. Flash-Next IQ2_XS mantuvo una mediana cercana a 93 tokens por segundo tras el calentamiento, mientras que Qwen3.8 denso descargó 24 capas y cayó por debajo de un token por segundo.

## Límites del benchmark

El benchmark registra las etiquetas de los modelos, los contextos solicitados, los tokens reales del prompt, las velocidades de procesamiento y generación, las versiones de Ollama y el objetivo de generación de 128 tokens. No registra los digest resueltos de manifiestos, el consumo de la CPU o del sistema, la velocidad de los ventiladores ni la refrigeración.

Las filas GPT-OSS a 256K procesaron 65,538 tokens reales del prompt en ambos sistemas. Las demás filas 256K procesaron unos 171K tokens reales. Considera las cifras una comparación observada de sistemas, no una clasificación universal de todas las parejas RTX 5060 Ti ni de todas las implementaciones GB10.

La prueba de Strata frente al modelo denso registra los recuentos exactos de prompts, cinco solicitudes medidas por contexto, versiones del runtime, ubicación de dispositivos, ajustes de caché y estado de las solicitudes. La comparación cambia a la vez la arquitectura del modelo, la cuantización, el empaquetado, el runtime y el modo de decodificación. Strata también reutilizó prefijos de prompts por encima de 32K. Las solicitudes de generación medidas en ambas pilas reutilizaron casi todo el prompt.

No es posible reproducir exactamente la prueba a partir de este artículo. El banco del benchmark, el diseño del paquete de Strata, el perfil de expertos y el paquete de borrador MTP no se publican con digest inmutables. La advertencia de poca VRAM también añade variabilidad entre ejecuciones. La prueba aísla el host, no el motor de inferencia.

Las especificaciones de hardware anteriores proceden de NVIDIA. Las cifras de rendimiento proceden de la prueba controlada realizada para este artículo.

## Referencias

- [Biblioteca de modelos Qwen3.8 de Ollama](https://ollama.com/library/qwen3.8)
- [Modelos GGUF ISTA-DASLab Qwen3.8 Flash-Next GSQ-RCO](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF)
- [Modelos GGUF orcarouter Qwen3.8 Flash-Next Uncensored](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF)
- [Biblioteca de modelos Qwen3.5 de Ollama](https://ollama.com/library/qwen3.5)
- [Biblioteca de modelos Qwen3.6 de Ollama](https://ollama.com/library/qwen3.6)
- [Biblioteca de modelos Nemotron 3.5 Lightning de Ollama](https://ollama.com/library/nemotron-3.5-lightning)
- [Etiquetas de modelos GPT-OSS de Ollama](https://ollama.com/library/gpt-oss/tags)
- [¿Bastan 16 GB de VRAM para trabajar en serio con LLM locales?](/articles/is-16gb-vram-enough-local-llm/)
- [32 GB de VRAM para Qwen 27B](/articles/32gb-vram-qwen-27b-hardware-guide/)
- [Guía de contexto y GPU para IA local](/articles/local-ai-model-gpu-context-guide/)
- [Benchmarks GPU de Qwen3.8 27B en Vast.ai](/articles/qwen38-27b-vast-ai-gpu-benchmark/)
- [Oferta completa de estación de trabajo con dos RTX 5060 Ti de 16 GB](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white)
- [Oferta de NVIDIA DGX Spark en el marketplace de EE. UU.](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/)
- [Oferta Linux de AMD Ryzen AI Halo con 128 GB](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false)
- [Reseña de Tom's Hardware: Strix Halo frente a GB10](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4)
- [Precios actuales de RTX 5060 Ti](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/)
