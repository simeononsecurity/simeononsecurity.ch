---
title: "¿Qué modelos de IA funcionan en una Raspberry Pi 4 o 5?"
date: 2026-09-20
lastmod: 2026-11-07
toc: true
draft: false
description: "Elige modelos de lenguaje locales según memoria, velocidad y carga de trabajo con resultados medidos en Raspberry Pi 4 y 5, desde LFM2.5 compactos hasta opciones 3B y mayores."
genre: ["Raspberry Pi", "Inteligencia artificial", "Autoalojamiento"]
tags: ["Raspberry Pi 4", "Raspberry Pi 5", "IA local", "modelos de lenguaje pequeños", "Ollama", "GGUF", "LFM2.5", "Qwen2.5", "Gemma 3", "cuantización de modelos", "IA en el borde"]
cover: "/img/cover/raspberry-pi-4-5-local-ai-models.webp"
coverAlt: "Dos ordenadores Raspberry Pi sobre un escritorio oscuro, con ilustraciones azules y ámbar de redes neuronales encima"
coverCaption: "Ilustración de modelos de IA locales ejecutándose en hardware Raspberry Pi."
---

Una Raspberry Pi puede ejecutar localmente un modelo de lenguaje útil, siempre que el modelo quepa en la memoria de la placa y responda en un tiempo aceptable para tu aplicación. Una Raspberry Pi 4 con 2 GB se adapta mejor a modelos por debajo de unos mil millones de parámetros. Una Raspberry Pi 5 con 8 GB ejecuta con comodidad modelos compactos de 1B a 3B y puede cargar algunos modelos cuantizados mayores, con compromisos importantes.

Medimos estos modelos por nuestra cuenta con Ollama en una **Pi 4B de 2 GB** y una **Pi 5 de 8 GB**, ambas con almacenamiento microSD. Las pruebas de las tablas usaron los mismos cinco prompts breves para el asistente, el mismo prompt de sistema, una seed fija y un límite de salida de 140 tokens. Descargamos los otros modelos antes de cada prueba y medimos el tiempo de carga en frío, el tiempo hasta el primer token visible, el tiempo total de respuesta, la velocidad de salida y la memoria residente máxima. Fueron pruebas de una sola pasada para una carga de respuestas breves. Los resultados sirven para estimar recursos, no para establecer una clasificación universal de velocidad o calidad. La [CPU Cortex-A76 y las configuraciones de memoria disponibles de la Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) también difieren de forma importante de la [plataforma Cortex-A72 de la Pi 4](https://pip-assets.raspberrypi.com/categories/545-raspberry-pi-4-model-b/documents/RP-008341-DS-1-raspberry-pi-4-datasheet.pdf).

## Tipos de modelos adecuados

| Tipo de modelo | Ejemplos medidos | Uso práctico |
|---|---|---|
| Modelos de texto pequeños, unos 230M–600M parámetros | LFM2.5-230M, LFM2.5-350M, Qwen2.5-0.5B | Comandos locales breves, resúmenes y preguntas con restricciones; mejor punto de partida para una Pi 4 de 2 GB |
| Modelos de texto compactos, unos 1B–2B | LFM2.5-1.2B, Qwen2.5-1.5B, Gemma 3 1B, MiniCPM5-1B | Más capacidad para seguir instrucciones matizadas en una Pi 5 o una Pi 4 con más memoria, aunque responden más lento que los modelos más pequeños |
| Modelos de texto cuantizados de 3B–4B | Qwen2.5-3B, Llama 3.2 3B, Gemma 3 4B | Candidatos más capaces para una Pi 5 de 8 GB cuando se aceptan varios segundos por respuesta |
| Modelos mayores, dispersos o híbridos | LFM2.5 8B | Funciona técnicamente en la Pi 5 de 8 GB que probamos, pero ocupa mucha memoria y tarda en cargar en frío |

Estos son resultados de **generación de texto**. No demuestran el rendimiento en generación de imágenes, reconocimiento de voz, visión ni entrenamiento. «Funciona» implica más que guardar el archivo del modelo en una tarjeta: el runtime, la caché de contexto, el sistema operativo y otros servicios también necesitan RAM. La cuantización reduce el tamaño de los pesos, pero puede empeorar la calidad de respuesta, sobre todo con ajustes extremos como pesos de 1 bit.

### Qué miden las cifras

El benchmark envió prompts breves sobre hechos, procedimientos de seguridad, contexto recuperado, el clima y ayuda a la API de chat de Ollama. Todos los modelos recibieron el mismo conjunto de prompts y seed. Descargamos cada modelo antes de medirlo para incluir una carga en frío en la siguiente solicitud. El **tiempo total** corresponde a la solicitud completa; los **tokens por segundo** describen solo la generación de salida. También registramos el primer token *visible*, algo importante cuando el modelo razona antes de responder.

Para medir memoria, registramos la RAM y el swap disponibles de la Pi junto con la memoria residente de Ollama y de su proceso de inferencia durante cada solicitud. Las cifras de **RSS** corresponden a memoria residente del proceso, no a la demanda total del host. Las páginas respaldadas por archivos, el sistema operativo, un navegador u otro servicio local todavía pueden provocar swap aunque un modelo parezca caber. Las tablas presentan las primeras pruebas de cinco prompts en una sola pasada. Más tarde ampliamos el banco de pruebas con un prompt de noticias y controles de reglas de respuesta. Esos controles ayudan a saber qué revisar, pero no convierten las mediciones anteriores en resultados de cumplimiento para seis prompts.

Ni los tokens por segundo ni el número de parámetros miden la calidad. Un modelo puede generar texto rápido y omitir una fuente solicitada, superar el límite de palabras o dejar una frase incompleta. Compara modelos con los prompts que piensas usar y revisa sus respuestas antes de elegir uno para una aplicación.

## Raspberry Pi 4: prioriza los modelos más pequeños

La Pi 4 de 2 GB probada tenía poco margen. Los modelos LFM2.5 más pequeños completaron los cinco prompts, igual que `qwen2.5:0.5b`. Son opciones razonables para respuestas breves sin conexión o un pequeño asistente local.

| Modelo | Archivo del modelo | Velocidad de salida medida | Tiempo medio de respuesta | Memoria o resultado observado |
|---|---:|---:|---:|---|
| LFM2.5-230M, GGUF importado | 0.25 GB | 12.8 tokens/s | 7.2 s | 383 MB de memoria residente máxima; 5/5 prompts |
| LFM2.5-350M, GGUF importado | 0.38 GB | 8.6 tokens/s | 8.6 s | 516 MB de memoria residente máxima; 5/5 prompts |
| `qwen2.5:0.5b` | 0.40 GB | 8.0 tokens/s | 9.7 s | 5/5 prompts; disponible directamente en Ollama |
| MiniCPM5-1B, GGUF importado, razonamiento desactivado | 0.69 GB | 5.9 tokens/s | 12.2 s | 883 MB de memoria residente máxima; 5/5 prompts |
| MiniCPM5-1B, GGUF importado, razonamiento predeterminado | 0.69 GB | 5.7 tokens/s | 33.3 s | Solo 1/5 prompts devolvió una respuesta visible útil |
| `qwen3:0.6b`, razonamiento predeterminado | 0.52 GB | 6.4 tokens/s | 40.4 s | Una respuesta vacía; la placa se reinició |
| `granite4:350m` | 0.71 GB | 4.6 tokens/s | 15.5 s | 913 MB RSS, sin swap ni reinicio; lenta, pero estable |
| `gemma3:1b` | 0.82 GB | 4.0 tokens/s | 30.7 s | Mucho swap; la placa se reinició durante la prueba |
| `qwen3.5:0.8b` | 1.04 GB | — | — | No terminó; la placa se reinició |

Los resultados de la Pi 4 dependen especialmente del resto del sistema. Vimos reinicios durante pruebas de modelos mayores, incluida una ejecución de `qwen3.5:0.8b` que no terminó. Esto describe nuestra configuración de 2 GB, no significa que todas las Pi 4 o todos los modelos 1B se reinicien. Una Pi 4 de 4 u 8 GB tiene más memoria, pero su CPU seguirá siendo más lenta que la de la Pi 5 probada. No medimos directamente esas variantes de memoria de Pi 4.

Una primera prueba de la Pi 4 también pareció mucho peor que las mediciones finales: unos 625 MB de archivos GGUF temporales estaban en `/tmp`, respaldado por RAM, dejaron solo 500–600 MB libres y llevaron cientos de megabytes al swap. Tras mover esos archivos a almacenamiento persistente, los resultados de los modelos pequeños reflejaron mejor la memoria de inferencia. En una placa de 2 GB, *la ubicación de la descarga* también puede distorsionar un benchmark.

**Recomendación:** Nuestro modelo predeterminado para esta placa de 2 GB es el LFM2.5-350M importado. Se mantuvo estable con **516 MB RSS**, dejó cerca de **1 GB de RAM disponible** y superó **5/6** controles de reglas de respuesta en la prueba de Pi 4. En pruebas repetidas de Pi 5 a veces omitió el nombre de la fuente; las aplicaciones que requieran atribución deben comprobarlo. Elige LFM2.5-230M si la latencia y el margen de memoria son lo más importante: fue más rápida y ligera, pero una respuesta sobre salud convirtió “nausea or vomiting” en “nausea/ventilator use”. Ese error de contenido la hace una opción predeterminada más débil para respuestas de salud o seguridad, pese a una puntuación mecánica repetida superior. Elige `qwen2.5:0.5b` si necesitas un modelo del [registro de Ollama](https://ollama.com/library/qwen2.5/tags), teniendo presente su menor cumplimiento de instrucciones. `granite4:350m` fue estable, pero tardó más y usó más memoria; MiniCPM5-1B solo es viable si el cliente desactiva el razonamiento. Evita Gemma 3 1B y Qwen3.5 0.8B en esta configuración específica de 2 GB, porque nuestras pruebas provocaron reinicios.

## Raspberry Pi 5: más opciones con un costo en velocidad

La Pi 5 de 8 GB manejó los **25 modelos** de nuestro benchmark de velocidad y memoria. La tabla incluye todas las pruebas, también modelos que no recomendamos para esta carga de respuestas cortas. † identifica un GGUF importado. «Think off» indica el ajuste usado para la prueba de velocidad; la prueba de cumplimiento separada no necesariamente usó el mismo ajuste.

| Modelo | Archivo, GB | Salida, tok/s | Respuesta, s | RSS máximo, MB | Evaluación para respuestas breves |
|---|---:|---:|---:|---:|---|
| `lfm2.5-230m` † | 0.25 | 45.0 | 1.8 | 446 | Menor latencia; 78% de cumplimiento repetido |
| `bonsai-1.7b` †, Q1_0 | 0.25 | 15.3 | 8.2 | 871 | Evitar: pesos de 1 bit y 3/6 en cumplimiento de una pasada |
| `lfm2.5-350m` † | 0.38 | 30.0 | 2.1 | 581 | Rápida, pero omitió la fuente en 5 de 18 repeticiones |
| `qwen2.5:0.5b` | 0.40 | 28.4 | 3.6 | 675 | Opción sencilla del registro; 61% de cumplimiento repetido |
| `qwen3:0.6b`, razonamiento desactivado | 0.52 | 23.0 | 4.3 | 1,069 | Condicional: 4/6; importa el ajuste de razonamiento |
| `bonsai-4b` †, Q1_0 | 0.57 | 6.8 | 18.1 | 1,343 | Modelo experimental de 1 bit; el 6/6 de una pasada no está confirmado |
| `minicpm5-1b` †, razonamiento desactivado | 0.69 | 18.4 | 5.1 | 869 | Condicional: el razonamiento predeterminado daba respuestas vacías |
| `granite4:350m` | 0.71 | 12.1 | 6.6 | 892 | Cabe, pero es más lenta y grande que LFM2.5 pequeño |
| `lfm2.5-1.2b` † | 0.73 | 15.5 | 4.7 | 967 | Mejor para nuestra carga; 89% de cumplimiento repetido |
| `llama3.2:1b-instruct-q4_K_M` | 0.81 | 13.0 | 7.5 | 1,244 | Alternativa del registro; 5/6 en cumplimiento |
| `gemma3:1b` | 0.82 | 11.2 | 10.9 | 1,262 | Mejor cumplimiento repetido entre modelos del registro: 83% |
| `qwen2.5:1.5b-instruct-q4_K_M` | 0.99 | 10.3 | 9.4 | 1,361 | 4/6; Gemma 3 1B siguió mejor las reglas |
| `qwen3.5:0.8b`, razonamiento desactivado | 1.04 | 8.8 | 12.2 | 1,592 | 0/6 con razonamiento predeterminado; evitar sin control de razonamiento |
| `spark-x2.5-1.7b` †, razonamiento desactivado | 1.11 | 9.7 | 9.4 | 1,542 | 0/6 con razonamiento predeterminado; evitar sin control de razonamiento |
| `qwen3:1.7b`, razonamiento desactivado | 1.36 | 8.1 | 12.4 | 1,867 | Condicional; más memoria y demora que opciones menores |
| `minicpm5-2b` †, razonamiento desactivado | 1.56 | 7.7 | 10.9 | 1,787 | Condicional; 5/6 en una pasada, viñetas adicionales |
| `qwen2.5:3b-instruct-q4_K_M` | 1.93 | 5.2 | 14.7 | 2,366 | Opción 3B para probar; 5/6 en una pasada |
| `granite4:micro-h` | 1.94 | 3.9 | 23.7 | 2,486 | Evitar para uso interactivo: decodificación lenta |
| `llama3.2:3b-instruct-q4_K_M` | 2.02 | 5.5 | 18.6 | 2,831 | Alternativa 3B; no se informó prueba de cumplimiento |
| `granite4:micro` | 2.10 | 5.3 | 17.9 | 2,679 | Cabe, pero responde más lento que las alternativas pequeñas |
| `qwen3.5:2b`, razonamiento desactivado | 2.74 | 5.0 | 16.1 | 3,627 | Mucha memoria y demora; no se informó prueba de cumplimiento |
| `gemma3:4b` | 3.34 | 3.9 | 30.3 | 4,267 | Evitar para respuestas rápidas; 14.3 s hasta el primer token |
| `ling-3.0-tiny` †, razonamiento desactivado | 4.82 | 9.9 | 19.4 | 5,071 | Gran consumo; 5/6 en una pasada, con fallo de fundamentación |
| `lfm2.5:8b`, razonamiento desactivado | 5.16 | 8.7 | 54.6 | 5,317 | Cabe justo; carga en frío de 34.4 s y respuestas largas |
| `gemma3n:e2b` | 5.62 | 6.1 | 25.9 | 5,261 | Evitar: swap junto con otros servicios de la Pi |

† GGUF importado. Los tiempos de respuesta y memoria proceden del test de velocidad de Pi 5 con cinco prompts; las cifras de cumplimiento vienen de pruebas separadas con seis prompts. Si un modelo no tiene puntuación, no se demostró que respete las reglas de respuesta.

Los modelos LFM2.5 pequeños fueron los más rápidos *para esta carga de respuestas breves*. La versión 1.2B ofrece un punto medio práctico en la Pi 5 probada. Gemma 3 1B es una alternativa disponible solo en el registro y en pruebas posteriores cumplió las reglas de respuesta mejor que Qwen2.5 1.5B. Un modelo 3B puede compensar la lentitud para prompts que requieren más capacidad, pero estas mediciones no demuestran por sí solas cuál da mejores respuestas.

La demora de carga en frío y del primer token cambia la experiencia. En Pi 5, LFM2.5-230M cargó en unos **0.21 segundos** y produjo un token visible en **0.37 segundos**. Qwen2.5 1.5B tardó **2.59 segundos** en cargar y **3.66 segundos** en mostrar el primer token; Qwen2.5 3B tardó **5.60** y **7.97 segundos**. Para una pregunta ocasional, esas demoras pueden importar más que la velocidad de salida una vez iniciada la generación. Un modelo cargado de forma continua reduce esa espera, pero ocupa memoria entre solicitudes.

Otros candidatos medidos muestran por qué no clasificamos solo por cantidad de parámetros. Con el razonamiento desactivado, `qwen3:0.6b` alcanzó **23.0 tokens/s** con **1,069 MB RSS** en Pi 5, mientras MiniCPM5-1B importado llegó a **18.4 tokens/s** con **869 MB RSS**. `granite4:350m` necesitó una descarga de **0.71 GB** y generó **12.1 tokens/s**, pese a la etiqueta 350M. El empaquetado y la arquitectura cambian la relación entre nombre, tamaño del archivo, memoria y velocidad.

Si tu cliente puede enviar `think: false` de forma fiable, Qwen3 0.6B y MiniCPM5-1B son experimentos razonables como alternativas a LFM2.5. MiniCPM5-2B, Qwen3 1.7B y Spark-X2.5 1.7B también funcionaron en Pi 5, pero no ofrecieron una ventaja clara de velocidad y memoria frente a nuestras opciones principales. La prueba de cumplimiento usó el razonamiento predeterminado para MiniCPM5-1B y Spark-X2.5; sus respuestas vacías no deben presentarse como resultado de las pruebas de velocidad con razonamiento desactivado. A la inversa, una medición rápida con razonamiento desactivado no demuestra que un puente sin esa opción reciba una respuesta útil.

Si la facilidad de instalación importa más que la velocidad pura, Gemma 3 1B y Llama 3.2 1B son opciones plausibles del registro en la Pi 5 de 8 GB. Gemma 3 1B siguió las reglas probadas en **15/18** respuestas repetidas. Llama 3.2 1B aprobó **5/6** en una pasada, así que la estimación es menos segura. Qwen2.5 1.5B cargó y respondió más rápido que Gemma 3 1B en la prueba de tiempo, pero solo pasó **4/6** controles en su única prueba de cumplimiento. Elige según lo que necesiten tus prompts.

Para prompts de texto más largos o difíciles, Qwen2.5 3B y Llama 3.2 3B cuantizados son los candidatos 3B con uso de memoria moderado en nuestra Pi 5 de 8 GB. Medimos velocidad y memoria; Qwen2.5 3B aprobó **5/6** en una prueba de cumplimiento. No se informó una prueba comparable para Llama 3.2 3B. Sus más parámetros son motivo para *probarlos* en tareas donde fallan los modelos pequeños, no una prueba de que resuelvan mejor esas tareas. Granite 4 Micro y Micro-H, Qwen3.5 2B, Gemma 3 4B, Ling-3.0-tiny y Gemma 3n E2B cabían o cargaban en nuestras pruebas Pi 5, pero ofrecieron latencia, margen de memoria o fiabilidad menos atractivos para esta aplicación de respuesta breve.

Los dos modelos Bonsai muestran el costo de una cuantización extrema. Sus archivos Q1_0 eran sorprendentemente pequeños para nombres con 1.7B y 4B parámetros, pero el modelo 1.7B pasó solo **3/6** controles de reglas de respuesta. El modelo 4B pasó una única prueba de seis prompts, pero tardó **18.1 segundos** por respuesta y no tiene confirmación de cumplimiento repetido. Considera ambos experimentales, no recomendaciones predeterminadas, sobre todo cuando importa la calidad.

El resultado de LFM2.5-8B requiere contexto: su arquitectura híbrida usa menos parámetros activos por token, por lo que su velocidad de decodificación superó a los modelos densos 3B medidos. Aun así, la carga en frío desde microSD tardó **34.4 segundos** y usó más de **5.3 GB de memoria residente**. Demuestra lo que cabe, pero no es una opción cómoda para una Pi con otros servicios. El `gemma3n:e2b` medido también usó unos 5.3 GB de memoria residente y provocó swap junto con los otros servicios del host de prueba.

La ejecución de LFM2.5 8B también alcanzó el límite completo de **140 tokens** en lugar de mantener la respuesta breve. Gemma 3 4B tardó **14.3 segundos** hasta el primer token y **30.3 segundos** en completar la respuesta. Ambos se pueden cargar en esta Pi 5, pero no se comportaron como un asistente pequeño y ágil en nuestras pruebas. Un modelo diminuto con una respuesta adecuadamente corta puede servir mejor a una interfaz de radio o comandos que un modelo mayor con una velocidad de decodificación más rápida sobre el papel.

## Memoria, razonamiento y formato del modelo

Una primera estimación basada en nuestras mediciones es **tamaño de descarga del modelo × 1.4** para la memoria residente de inferencia. Es solo una regla práctica: la longitud de contexto, los ajustes del runtime, la arquitectura y otros procesos cambian la necesidad. Comprueba la memoria disponible mientras generas, carga un solo modelo en un host pequeño y deja espacio para el sistema operativo. Una placa de 4 GB puede empezar con modelos pequeños o compactos, pero nuestras recomendaciones para 4 GB son extrapolaciones, no pruebas directas de variantes de 4 GB.

Por ejemplo, el archivo LFM2.5-1.2B de 0.73 GB correspondió a unos **967 MB RSS** en Pi 5, mientras el archivo Qwen2.5 1.5B de 0.99 GB alcanzó **1,361 MB RSS**. La regla funciona razonablemente para esos modelos, pero no es un límite estricto. Reserva más memoria que la medida para el proceso del modelo si la Pi también ejecuta una interfaz, un índice de búsqueda, una biblioteca local u otro servicio en segundo plano. Observa el swap durante una solicitud real; un modelo que carga pero usa swap continuamente no resulta práctico.

Algunos modelos generan un bloque de razonamiento interno antes de la respuesta visible. En nuestras pruebas, `qwen3:0.6b` en la Pi 4 de 2 GB tardó mucho más en producir texto visible. MiniCPM5-1B solo dio una de cinco respuestas útiles con el razonamiento predeterminado, frente a cinco de cinco al desactivarlo. Para un límite breve, configura `think: false` en una solicitud compatible a la API de Ollama o elige un modelo que no razone de forma predeterminada. El ajuste se aplica a modelos y clientes compatibles; no es un interruptor universal de velocidad.

La diferencia importa porque el límite de tokens puede incluir tokens de razonamiento aunque el usuario no vea respuesta. En Pi 4, `qwen3:0.6b` con razonamiento predeterminado tardó **40.4 segundos por solicitud** en promedio y produjo una respuesta visible vacía en un prompt. MiniCPM5-1B promedió **33.3 segundos** con su ajuste predeterminado y **12.2 segundos** con el razonamiento desactivado. En las pruebas de Pi 5 también desactivamos el razonamiento de Qwen3, Qwen3.5, MiniCPM5, Ling-3.0 y Spark-X2.5 cuando los registros lo indicaban. Compara cada modelo con el mismo ajuste que usará tu cliente.

### Comprueba si la respuesta sirve

Para nuestra carga breve de asistente mesh, el contrato de respuesta importa tanto como la velocidad: máximo **90 palabras**, hasta **tres viñetas**, texto plano, una frase completa y uso del contexto recuperado proporcionado con el nombre de su fuente. El puente divide el texto en bloques de **180 caracteres**. Una respuesta larga ocupa más tiempo de radio aunque el modelo la genere rápidamente.

La versión posterior del benchmark revisa respuestas vacías, límites de palabras específicos del prompt, demasiadas viñetas, tablas o bloques de código Markdown, finales incompletos, términos ausentes del contexto suministrado y nombres de fuente omitidos. Al evaluar las respuestas según el prompt del sistema del asistente desplegado, los modelos pequeños incumplieron estas reglas con frecuencia. Los fallos más graves fueron **respuestas vacías** cuando el razonamiento consumió el límite de tokens, seguidas de respuestas que ignoraron el contexto recuperado o no citaron su fuente. Superar el límite de palabras o usar demasiadas viñetas seguía mostrando texto, pero desperdiciaba tiempo de radio. Son controles mecánicos, no sustituyen la lectura de la respuesta: no demuestran exactitud ni que los consejos de seguridad sean adecuados.

#### Resultados repetidos de cumplimiento en Pi 5

Primero ejecutamos seis prompts una vez por modelo con un límite de **220 tokens** y el prompt del sistema desplegado. Después probamos dos veces más los modelos prometedores con una seed distinta: **18 respuestas por modelo**. Una pasada perfecta no garantizó resultados perfectos en las repeticiones. Los resultados repetidos siguientes ofrecen una comparación más sólida para las respuestas mesh breves probadas:

| Modelo | Respuestas que siguieron todas las reglas comprobadas | Fallos principales observados |
|---|---:|---|
| LFM2.5-1.2B importado | 16/18 (89%) | Dos respuestas sin terminar |
| `gemma3:1b` | 15/18 (83%) | Tres respuestas sin terminar |
| LFM2.5-230M importado | 14/18 (78%) | Respuestas incompletas y nombres de fuentes ausentes |
| LFM2.5-350M importado | 13/18 (72%) | Nombres de fuentes ausentes |
| `qwen2.5:0.5b` | 11/18 (61%) | Demasiadas viñetas y palabras, nombres de fuentes ausentes |

En la **Pi 4 de 2 GB**, la prueba separada de seis prompts obtuvo **5/6** para LFM2.5-350M, **4/6** para LFM2.5-230M y **2/6** para Qwen2.5-0.5B. MiniCPM5-1B mejoró de **1/6** con el razonamiento predeterminado a **5/6** al desactivarlo. Esos resultados de Pi 4 son de una sola pasada, así que damos más peso a los resultados repetidos de Pi 5 al hablar del seguimiento general de instrucciones, mientras usamos las pruebas de Pi 4 para juzgar estabilidad y velocidad en esa placa.

Los fallos tienen consecuencias distintas. Una respuesta **vacía** no ayuda; ignorar el material proporcionado puede inducir a error. Si falta el nombre de la fuente, el lector no puede verificar la atribución. Las viñetas o palabras adicionales consumen sobre todo paquetes extra de 180 caracteres. Una frase inconclusa puede indicar truncamiento. El error de LFM2.5-230M con un término médico recuerda que una respuesta puede pasar estas pruebas mecánicas y ser incorrecta. Ninguno de los cinco modelos repetidos siguió todas las reglas en las 18 respuestas. Una aplicación con límites estrictos de longitud o formato también debería aplicarlos tras la generación y revisar aparte el contenido de alto riesgo.

También comprobamos el endpoint real del puente, `/v1/chat/completions` compatible con OpenAI de Ollama, usando contexto recuperado de WikiMed. En Pi 5, LFM2.5-1.2B devolvió una respuesta de 28 palabras con seis términos proporcionados; Qwen2.5-0.5B devolvió 38 palabras con siete. Ambas cabían en dos paquetes de 180 caracteres. Esa comprobación confirma que el modelo LFM2.5 importado funciona a través de la ruta de solicitud del puente, pero un único resultado correcto no garantiza fiabilidad.

Ollama publica muchos modelos listos para descargar, incluidas las [variantes Qwen2.5 de 0.5B, 1.5B y 3B](https://ollama.com/library/qwen2.5/tags). Importamos los modelos LFM2.5 pequeños desde las [versiones GGUF de Liquid AI](https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/tree/main) a Ollama. Comprueba la etiqueta exacta o el nombre de archivo GGUF antes de descargar, porque los registros y repositorios pueden cambiar. Guarda las descargas GGUF en almacenamiento persistente; en nuestras pruebas, `/tmp` respaldado por RAM consumió memoria escasa de la Pi 4.

### Etiquetas del registro e importaciones GGUF

Una etiqueta de Ollama es la ruta más corta para una primera prueba: descarga la etiqueta exacta y ejecútala. Los modelos LFM2.5 pequeños de las tablas eran **importaciones GGUF**, no etiquetas `lfm2.5-230m`, `lfm2.5-350m` o `lfm2.5-1.2b` de la biblioteca pública de Ollama. GGUF es un formato de archivo de modelo; nombres como `Q8_0` y `Q4_K_M` identifican opciones de cuantización. Los archivos LFM2.5 de 230M y 350M usados eran Q8_0; el archivo 1.2B era Q4_K_M. Por tanto, la misma cantidad de parámetros con otra cuantización puede tener distinto tamaño, uso de memoria o calidad.

Para importar la variante 350M probada, descarga el GGUF a un directorio en almacenamiento persistente, crea un Modelfile que apunte al archivo y deja que Ollama lo copie a su almacén de modelos:

```bash
mkdir -p "$HOME/gguf"
cd "$HOME/gguf"
curl -fL -C - --retry 5 --retry-all-errors -O \
  https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/resolve/main/LFM2.5-350M-Q8_0.gguf
printf 'FROM %s/LFM2.5-350M-Q8_0.gguf\n' "$PWD" > Modelfile-lfm2.5-350m
ollama create lfm2.5-350m -f Modelfile-lfm2.5-350m
ollama run lfm2.5-350m
```

La importación necesita temporalmente espacio para el archivo descargado y la copia almacenada por Ollama. Usamos descargas reanudables porque a veces se interrumpían transferencias largas de GGUF. Antes de importar, compara el SHA-256 de la descarga con el hash publicado por su fuente; una transferencia parcial puede parecer un problema del modelo. En nuestra Pi, `/tmp` estaba respaldado por RAM, por lo que guardar allí un GGUF reducía la memoria disponible para inferencia.

## Un punto de partida práctico

| Hardware y objetivo | Primer modelo que probar | Motivo |
|---|---|---|
| Pi 4 de 2 GB, opción predeterminada | LFM2.5-350M importado | Estable con 516 MB RSS y cerca de 1 GB disponible; elegido tras un error de término médico del 230M |
| Pi 4 de 2 GB, menor latencia | LFM2.5-230M importado | 383 MB RSS y respuesta media de 7.2 s; revisa el contenido con atención, en especial en preguntas de salud o seguridad |
| Pi 4 de 2 GB, solo modelos del registro | `qwen2.5:0.5b` | Descarga directa de Ollama y estabilidad en nuestra prueba Pi 4 de cinco prompts; 61% de cumplimiento repetido en Pi 5 |
| Pi 4 de 4 GB o Pi 5 | LFM2.5-1.2B importado y luego probar localmente | 967 MB RSS y 89% de cumplimiento repetido en Pi 5 de 8 GB; no probamos directamente variantes de 4 GB |
| Pi 5 de 8 GB, asistente ágil | LFM2.5-1.2B importado | 15.5 tokens/s, respuesta total de 4.7 s y mayor cumplimiento repetido medido |
| Pi 5 de 8 GB, solo configuración del registro | `gemma3:1b` | 11.2 tokens/s, 1,262 MB RSS y 83% de cumplimiento repetido |
| Pi 5 de 8 GB, probar un modelo de texto mayor | Qwen2.5 3B o Llama 3.2 3B cuantizados | Ambos funcionaron cerca de 5 tokens/s y usaron 2.4–2.8 GB RSS; Qwen2.5 3B aprobó 5/6 en una pasada |

Estas opciones priorizan respuestas breves y útiles en una Pi que quizá ejecute otros servicios. Son puntos de partida, no afirmaciones de que un modelo sea el mejor para todas las tareas. En nuestra prueba de cumplimiento de una pasada en Pi 5, `qwen3.5:0.8b` y Spark-X2.5 con razonamiento predeterminado no dieron respuestas conformes, mientras MiniCPM5-1B logró 1/6. Si tu cliente no puede desactivar el razonamiento, evítalos para esta carga breve. Prueba el modelo final con el prompt real, el contexto, la concurrencia y el límite de respuesta que piensas usar.

Para el modelo del registro, después de [instalar Ollama para Linux](https://ollama.com/download/linux), ejecuta:

```bash
ollama pull qwen2.5:0.5b
ollama run qwen2.5:0.5b
```

Prueba tus propios prompts, la longitud de respuesta deseada y los demás servicios en ejecución. Anota tanto el tiempo total de respuesta como el uso de memoria. Eso indica mejor si el modelo encaja en tu Pi que el número de parámetros por sí solo.

En un nodo con memoria limitada, vigila el swap durante las pruebas. Si un modelo mayor vuelve la placa poco receptiva, usa uno más pequeño y define un límite de memoria apropiado para el servicio Ollama, de modo que una carga excesiva falle antes de agotar la memoria del host. El límite del servicio es una protección, no una manera de hacer caber un modelo demasiado grande. Los reinicios de Pi 4 durante nuestras pruebas muestran por qué la respuesta ágil y el margen de memoria deben acompañar a tokens por segundo entre los criterios de selección.

## Convierte el benchmark en una decisión de despliegue

Antes de instalar un modelo para uso diario, define cuatro límites: **tiempo máximo de respuesta, memoria residente máxima, formato de respuesta y comportamiento ante fallos**. Pruébalos junto con los servicios que compartirán la placa. Un modelo que pasa en solitario pero provoca swap junto a tu puente de radio o panel no cumple el requisito de despliegue.

Mantén instalado un modelo pequeño de respaldo. Cámbiate a él si el modelo principal supera el límite de memoria, devuelve una respuesta vacía o incumple el contrato de respuesta. En cada comparación registra la etiqueta del modelo, la cuantización, la versión de Ollama, el prompt, la longitud del contexto y la seed, para que una actualización posterior del modelo no parezca una mejora del hardware.
