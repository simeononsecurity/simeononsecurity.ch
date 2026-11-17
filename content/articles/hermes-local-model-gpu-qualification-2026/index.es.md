---
title: "Benchmarks de modelos locales de Hermes: las combinaciones de GPU y modelos que elegiría"
date: 2026-10-24
lastmod: 2026-11-15
toc: true
draft: false
description: "Mis recomendaciones de modelos para Hermes se basan en pruebas de contexto largo, herramientas, transmisión y visión en sistemas RTX 5060 Ti, RTX 2000E Ada, RTX 3060 Ti y RTX 3070."
genre: ["Inteligencia artificial", "IA local", "Informática"]
tags: ["Agente Hermes", "modelos de lenguaje locales", "benchmarks de LLM", "inferencia GPU", "RTX 3060 Ti", "RTX 3070", "RTX 2000E Ada", "RTX 5060 Ti", "calificación de modelos", "llamadas a herramientas", "contexto largo", "llama.cpp", "Ollama", "Qwen3.5", "Qwen3.6", "Qwen3.8"]
cover: "/img/cover/hermes-local-model-gpu-benchmarks.webp"
coverAlt: "Ilustración de tarjetas gráficas de dos ventiladores y de perfil bajo junto al título Hermes Model Benchmarks sobre un fondo azul oscuro"
coverCaption: ""
---

Para las tareas de Hermes con contexto largo, empezaría con Qwen3.5 35B en dos tarjetas RTX 5060 Ti de 16 GB. La ruta probada retuvo 239.153 tokens de entrada mediante LiteLLM y superó comprobaciones independientes de herramientas, transmisión, visión, solicitudes en cola y cancelación. Qwen3.6 es mi alternativa con una sola tarjeta. En los sistemas RTX 3060 Ti y RTX 3070, empezaría con Qwen3.5 2B o 4B.

Estas opciones se basan en ejecutar modelos por las rutas de inferencia que usa el agente. Probé la retención de entradas largas, los intercambios con herramientas, las respuestas transmitidas, las preguntas sobre imágenes y la liberación del modelo. También probé los modos y los ajustes de memoria de las rutas, porque cargar un modelo correctamente dice poco sobre su utilidad durante una solicitud larga del agente.

Hermes requiere al menos 64.000 tokens de contexto para usar herramientas con un agente. Fijé el umbral de calificación de contexto largo en 65.536 tokens de entrada reales. El recuento de tokens de entrada importa más que el tamaño de contexto anunciado por el servidor. ([Documentación de proveedores de Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md))

## Qué GPU tiene cada sistema

Las letras de los sistemas identifican las combinaciones de hardware en todos los resultados.

| Sistema | GPU usadas en este benchmark | Modelo que elegiría para empezar |
|---|---|---|
| A | 2 × GeForce RTX 5060 Ti, 16 GB cada una | Qwen3.5 35B entre ambas tarjetas, o Qwen3.6 en una tarjeta |
| B | 1 × RTX 2000E Ada, 16 GB | Qwen3.5 9B si el procesamiento de entradas largas durante varios minutos encaja con la tarea |
| C | 1 × RTX 2000E Ada, 16 GB | Gemma 3 4B para la ruta probada de entrada larga, Qwen3.5 0.8B sin razonamiento para tareas de recuperación acotadas |
| D | 1 × RTX 2000E Ada, 16 GB | Qwen3.5 9B, Gemma 4 12B-IT o GPT-OSS 20B para las cargas probadas con modelos más grandes |
| E | 9 × GeForce RTX 3060 Ti, 8 GB cada una | Qwen3.5 2B o 4B |
| F | 8 × GeForce RTX 3060 Ti, 8 GB cada una | Qwen3.5 2B o 4B |
| G | 3 × GeForce RTX 3070 | Qwen3.5 2B o 4B |

El número de tarjetas instaladas no significa que todas las solicitudes usaran todas las GPU. Las pruebas de Qwen3.5 35B y Flash Next usaron ambas tarjetas del sistema A. Qwen3.6 usó una. La repetición de visión de Qwen3.5 4B que tuvo éxito en el sistema E usó una tarjeta elegida de un grupo de ocho, mientras una novena tarjeta siguió excluida de las tareas de IA.

Interpreta las duraciones como resultados conjuntos del modelo, el entorno de ejecución y el sistema probados. Estas ejecuciones comparan configuraciones útiles. No aíslan la arquitectura de GPU como causa de la diferencia de velocidad.

## Dos RTX 5060 Ti hacen de Qwen3.5 35B mi elección para contexto largo

Qwen3.5 35B produjo el resultado de mayor retención de entrada en estas pruebas. La progresión directa de Ollama retuvo 248.279 tokens de entrada dentro de un contexto de ejecución de 262.144 tokens. Otra solicitud transmitida a través de la pasarela retuvo 239.153 tokens de entrada, devolvió el marcador inicial y terminó con normalidad después de 31 tokens de salida en 148,12 segundos.

El resultado de la pasarela importa para Hermes porque la solicitud pasó por el intermediario y LiteLLM. Otras solicitudes completaron un intercambio con una herramienta, reconocieron una imagen roja y devolvieron dos respuestas correctas al enviarse juntas. El intermediario puso las dos solicitudes en cola. Cerrar una solicitud transmitida liberó el intermediario y descargó el modelo en 60,31 segundos.

| Solicitud de Qwen3.5 35B | Tokens de entrada | Tokens de salida | Duración | Resultado |
|---|---:|---:|---:|---|
| Ollama directo, primera etapa progresiva | 69,429 | 31 | 38.783 s | Marcador inicial exacto |
| Ollama directo, continuación con prefijo compartido | 124,179 | 31 | 28.472 s | Marcador inicial exacto |
| Ollama directo, continuación con prefijo compartido | 182,579 | 31 | 38.974 s | Marcador inicial exacto |
| Ollama directo, continuación con prefijo compartido | 248,279 | 31 | 54.215 s | Marcador inicial exacto |
| Solicitud transmitida por el intermediario | 69,427 | 29 | 38.872 s | Marcador inicial exacto |
| Solicitud transmitida por LiteLLM | 239,153 | 31 | 148.12 s | Marcador inicial exacto, descarga limpia |

Las solicitudes directas progresivas reutilizaron un prefijo cada vez mayor. Sus duraciones describen el comportamiento de continuación con el modelo ya preparado. El resultado de 54,215 segundos no es una medición independiente en frío para procesar una nueva indicación de 248K.

En la etapa directa más larga, el modelo informó unos 27.300 millones de bytes residentes entre las dos GPU. Los picos de memoria por tarjeta llegaron a 14.964 y 12.386 MiB.

Las temperaturas máximas llegaron a 62 y 63 C, y la ejecución no registró fallos OOM ni Xid. La entrada dejó 13.865 tokens dentro del contexto configurado para continuar. La respuesta corta del marcador usó 31 de esos tokens.

Usaría esta ruta cuando importe más retener un conjunto de trabajo grande que obtener la respuesta inicial más rápida. Las comprobaciones de herramientas y visión demuestran comportamientos útiles del agente, mientras la prueba de entrada larga demuestra retención. Son cargas distintas.

## Qwen3.6 es la opción de una sola tarjeta

Qwen3.6-35B-A3B UD-Q4_K_XL retuvo 131.000 tokens de entrada en una sola RTX 5060 Ti. La otra tarjeta permaneció inactiva durante la prueba. Esto ofrece una alternativa útil cuando no conviene dedicar ambas tarjetas a un modelo.

| Solicitud de Qwen3.6 por la pasarela | Tokens de entrada | Tokens de salida | Duración | Resultado |
|---|---:|---:|---:|---|
| Solicitud larga inicial | 66,007 |  | 167.82 s | Marcador inicial retenido |
| Solicitud más larga | 90,000 | 11 | 159.92 s | Marcador inicial retenido, cero entradas en caché |
| Solicitud más larga | 119,999 | 11 | 250.61 s | Marcador inicial retenido, cero entradas en caché |
| Cerca del límite de ejecución | 131,000 | 11 | 287.09 s | Marcador inicial retenido, cero entradas en caché |

La solicitud de 131.000 tokens se acercó al límite de ejecución de 131.072. Para un agente, dejaría más espacio para la respuesta y los mensajes posteriores de las herramientas. Retener cerca del límite aporta evidencia sobre el procesamiento de entradas, pero no es un presupuesto predeterminado razonable.

El uso de herramientas pasó con el razonamiento desactivado. El razonamiento predeterminado consumió los 512 tokens permitidos antes de emitir la llamada a la herramienta. La prueba piloto satisfactoria también pasó las solicitudes rápidas, transmitidas y de visión. Su comprobación inicial de contexto de 65.845 tokens tardó 139,57 segundos.

## Qwen3.8 27B gana la comparación de respuesta equivalente de 66K

Para la misma carga del marcador de 66.007 tokens en el sistema A, Qwen3.8 27B devolvió la respuesta más rápido. Mantendría esta ruta disponible para solicitudes de ese tamaño probado, junto a Qwen3.5 35B para el conjunto de trabajo más grande.

| Ruta del sistema A | Tokens de entrada | Duración | Resultado |
|---|---:|---:|---|
| Qwen3.8 27B | 66,007 | 54.64 s | Marcador inicial retenido |
| Qwen3.6-35B-A3B UD-Q4_K_XL | 66,007 | 167.82 s | Marcador inicial retenido |
| Qwen3.8-Flash-Next UD-IQ4_XS | 66,007 | 164.58 s | Marcador inicial retenido |
| Alias de compatibilidad Flash Next IQ4 | 66,007 | 213.25 s | Marcador retenido |

Qwen3.8 27B tardó aproximadamente un tercio del tiempo de las solicitudes equivalentes de Qwen3.6 y Flash Next. Son observaciones de solicitudes completas con los entornos de ejecución probados, no una comparación exclusiva del hardware.

Las respuestas rápidas, la transmisión y el uso de herramientas también pasaron. El modo sin razonamiento completó toda la secuencia de colores y el intercambio con la herramienta, mientras la prueba con razonamiento devolvió solo parte de la secuencia dentro del límite de 512 tokens.

Flash Next sigue siendo una opción predeterminada menos atractiva en este sistema por la presión de memoria. Su prueba piloto de 65.847 tokens pasó en 201,41 segundos con un contexto de ejecución de 98.304. Dos perfiles anteriores de contexto 131.072 llegaron al límite de memoria antes de estar listos.

La ruta posterior llegó a su límite cgroup de 54 GiB. Para el trabajo desatendido, elegiría una ruta con más margen de memoria.

La ruta con la etiqueta `flash-iq2` sirvió al backend de compatibilidad Flash Next IQ4. Su nombre no identifica un resultado IQ2.

## La RTX 2000E Ada admite entradas largas, pero el modelo cambia la espera

Gemma 3 4B es mi ruta probada preferida para entradas largas en el sistema C. Dos rutas retuvieron más de 84K tokens de entrada en unos 88 segundos. Las rutas con modelos más grandes también pasaron comprobaciones de retención útiles, pero sus solicitudes tardaron varios minutos.

| Sistema | Modelo y ruta | Tokens de entrada | Duración | Resultado |
|---|---|---:|---:|---|
| B | Qwen3.5 9B, pasarela | 72,265 | 263 s | Se retuvieron ambos marcadores y pasó la comprobación posterior de recuperación de minería |
| C | Gemma 3 4B, pasarela | 84,044 | 88.05 s | Marcador inicial retenido |
| C | Gemma 3 4B, Aperture | 84,045 | 87.68 s | Marcador inicial retenido |
| C | Gemma 4 12B-IT, pasarela | 67,254 | 263.07 s | Marcador inicial retenido |
| C | Gemma 4 12B-IT, Aperture sin transmisión | 67,255 | 274.24 s | Marcador inicial retenido |
| C | Gemma 4 12B-IT, transmisión de Aperture | 67,255 | 282.16 s | Marcador inicial retenido |
| C | Qwen3.5 9B, pasarela | 75,648 | 319.36 s | Marcador inicial retenido, modelo descargado |
| C | GPT-OSS 20B, pasarela | 84,099 | 315.83 s | Marcador inicial retenido, modelo descargado |
| D | Qwen3.5 9B, Aperture | 81,051 | 324.07 s | La retención pasó en el artefacto instalado |
| D | Gemma 4 12B-IT, Aperture | 72,057 | 300.67 s | La retención pasó en el artefacto instalado |
| D | GPT-OSS 20B, Aperture | 72,104 | 245.94 s | La retención pasó en el artefacto instalado |

La transmisión no eliminó la larga espera de prellenado de Gemma 4 en el sistema C. El primer contenido transmitido llegó después de 277,49 segundos, más tarde que la respuesta completa de 274,24 segundos sin transmisión. Un intento anterior sin transmisión agotó el tiempo de espera antes del reintento satisfactorio. Reservaría esta ruta para tareas compatibles con varios minutos de procesamiento inicial.

Gemma 3 4B también demuestra por qué limitaría la calificación a cada sistema probado. El sistema D no encontró el marcador inicial en dos intentos de recuperación de 65K, incluida una repetición a temperatura cero con 67.252 tokens de entrada. La solicitud determinista terminó con normalidad en 62,07 segundos con la GPU totalmente ocupada.

Una finalización rápida y una respuesta API normal no garantizaban que la respuesta fuera correcta. Usaría la ruta satisfactoria del sistema C y descartaría la ruta fallida del sistema D para elegir modelos de Hermes.

## El modo de razonamiento determina si Qwen3.5 0.8B resulta útil

Qwen3.5 0.8B se convirtió en una opción útil para recuperación acotada en el sistema C al desactivar el razonamiento. El modelo pequeño Q8_0 retuvo 75.649 tokens de entrada mediante la pasarela en 65,92 segundos. Este resultado corresponde al artefacto Q8_0 probado y a la ruta sin razonamiento, no a las antiguas configuraciones de contexto 16K de otras partes de la tabla.

| Solicitud de Qwen3.5 0.8B en el sistema C | Tokens de entrada | Tokens de salida | Duración | Resultado |
|---|---:|---:|---:|---|
| Razonamiento predeterminado, diagnóstico breve | 9,050 | 3,391 | 66.56 s | Marcador inicial exacto |
| Razonamiento desactivado, diagnóstico equivalente | 9,055 | 21 | 7.65 s | Marcador inicial exacto, sin texto de razonamiento |
| Razonamiento predeterminado, intento largo |  |  | tiempo agotado a los 600 s | No se completó la respuesta |
| Razonamiento desactivado, Ollama nativo | 75,656 | 22 | 69.80 s | Marcador inicial exacto |
| Endpoint compatible con OpenAI sin razonamiento | 75,646 | 12 | 69.09 s | Marcador inicial exacto |
| Intermediario con modo sin razonamiento obligatorio | 75,647 | 13 | 66.83 s | Marcador inicial exacto |
| LiteLLM desde el sistema A al C | 75,649 | 15 | 65.92 s | Marcador inicial exacto |

El diagnóstico equivalente bajó de 66,56 a 7,65 segundos, unas 8,7 veces más rápido, mientras la salida generada cayó de 3.391 a 21 tokens. Por eso fijaría explícitamente el modo de razonamiento para tareas sencillas de extracción y enrutamiento. El razonamiento predeterminado dedicó la mayor parte del trabajo a generar una salida que la tarea no necesitaba.

Una prueba breve compatible con OpenAI no encontró el marcador hasta que pasó el reintento con temperatura cero. Las comprobaciones de ruta satisfactorias usaron el modo sin razonamiento y una finalización natural sin límite de salida. Otras tres pasarelas pasaron solicitudes breves con marcador en 4,22, 4,37 y 3,85 segundos. Esas comprobaciones validan el enrutamiento; la solicitud de 75.649 tokens valida la retención de entradas largas mediante la pasarela.

Probaría esta ruta para recuperación y extracción acotadas. Elegiría un modelo mayor para razonamiento abierto de agentes. Recuperar un marcador sintético es una tarea más limitada que planificar, programar o coordinar varias herramientas.

## Los sistemas RTX 3060 Ti y RTX 3070 favorecen Qwen3.5 2B y 4B

Qwen3.5 2B y 4B son mis opciones prácticas para empezar en las tarjetas de 8 GB. Las solicitudes de contexto de texto en los sistemas E, F y G pasaron con 65.579 tokens de entrada y duraciones de 30,343 a 93,753 segundos. Las rutas 4B probadas también superaron las comprobaciones de herramientas, transmisión e imágenes.

La repetición del contexto de visión 4B del sistema E retuvo ambos marcadores y el orden de los colores de imagen con 65.637 tokens de entrada en 44,88 segundos. También pasaron las solicitudes con el orden de colores directo e inverso. La repetición usó una tarjeta sana después de que otra sufriera un fallo de enlace Xid 79 y el sistema se reiniciara.

| Sistema | Contexto de texto Qwen3.5 2B | Contexto de texto Qwen3.5 4B | Contexto de visión Qwen3.5 4B |
|---|---|---|---|
| E, grupo RTX 3060 Ti | 65,579 tokens, 30.343 s | 65,579 tokens, 53.787 s | 65,637 tokens, 44.88 s |
| F, grupo RTX 3060 Ti | 65,579 tokens, 61.282 s | 65,579 tokens, 93.753 s | 65,635 tokens, 84.749 s |
| G, grupo RTX 3070 | 65,579 tokens, 76.731 s | 65,579 tokens, 90.807 s | 65,635 tokens, 87.496 s |

Cada uno de estos sistemas registró 29 comprobaciones satisfactorias. La diferencia de tiempos entre los dos sistemas RTX 3060 Ti también muestra por qué elegiría un perfil de sistema probado en vez de ordenar las tarjetas según estas duraciones de solicitud.

Los siete sistemas reanudaron la minería después de la ventana de inferencia. La comprobación independiente de recuperación tras detener el sistema B pasó con nuevas acciones aceptadas. La tarjeta que falló en el sistema E volvió a minar después de un reinicio y de reforzar el enlace PCIe, pero siguió excluida del grupo de IA. Restaurar la minería al final de la ventana es un resultado distinto de devolver automáticamente el equipo tras una solicitud de inferencia.

## Cargar un modelo no lo califica

Excluiría DeepSeek Coder V2 16B de las opciones Hermes probadas a 65K. La prueba con caché f16 retuvo 50.477 tokens de entrada, pero la prueba objetivo de 65K llegó a la protección de VRAM. Las alternativas de caché Q4 y Q8 cargaron los pesos en las GPU, pero después alcanzaron los límites de memoria del anfitrión o tuvieron un rendimiento bajo con solicitudes largas.

| Perfil de caché de DeepSeek Coder V2 | Contexto de ejecución | Resultado observado | Mi evaluación |
|---|---:|---|---|
| f16 | 81,920 | Recuperación de 50.477 tokens satisfactoria; se rechazó una solicitud demasiado grande | Resultado útil con contexto más corto |
| f16 | 73,728 | El prellenado objetivo de 65K se detuvo con 15.802 MiB de uso de GPU | No califica para 65K |
| Q4_0 | 98,304 | El prellenado largo bajó a 96.72 tokens/s antes de la detención controlada | Poco adecuado para esta carga |
| Q8_0 | 77,824 | El prellenado largo bajó a 120.12 tokens/s antes de la detención controlada | Poco adecuado para esta carga |
| Q4_0 / Q8_0, perfiles más grandes | 163,840 / 98,304 | Las protecciones de memoria del anfitrión detuvieron las pruebas | El ajuste de memoria depende de todo el sistema |

La lección práctica es probar la solicitud que tienes previsto enviar. Que el modelo resida en la GPU, responda brevemente y tenga un contexto configurado grande no demuestra que retenga entradas largas con una latencia útil.

Granite 4.2 8B y GPT-OSS 20B mejoraron tras ajustes específicos de ruta en el sistema A. La ruta Q6_K de Granite retuvo 66.082 tokens de entrada en 88,636 segundos sin entrada en caché. GPT-OSS completó el intercambio con la herramienta tras la reparación del intermediario, en 9,854 segundos para la llamada y 9,849 segundos para el seguimiento. Mantendría estas comprobaciones satisfactorias separadas de los intentos anteriores incompletos.

## Resultados completos de los benchmarks

La tabla contiene 295 comprobaciones en 59 combinaciones de modelos y sistemas. La matriz registra 273 aprobadas, una comprobación de recuperación fallida y siete resultados incompletos, incoherentes o incompatibles. Catorce comprobaciones quedan fuera del alcance de calificación de 65K. Cada fila muestra su resultado medido.

Mis recomendaciones se aplican a las rutas y cargas que pasaron. Una fila fallida o incompleta no califica el comportamiento correspondiente.

Los resultados de contexto corto y de embeddings corresponden a sus propias cargas. Pasar con contexto 16K o 32K no califica una ruta para la carga Hermes de 65.536 tokens de entrada. Los nombres de modelos de aquí son etiquetas de ruta. La etiqueta `flash-iq2` servía al backend de compatibilidad IQ4.

La fila de contexto Qwen3.5 35B del sistema A es la última etapa de prefijo compartido de la progresión anterior. Las duraciones de herramientas con un signo más muestran por separado la llamada y su seguimiento.

La fila de concurrencia muestra las duraciones de las dos solicitudes en cola. La fila de cancelación indica el tiempo de liberación después de que el cliente cerró el flujo. Las progresiones adicionales de contexto y las comparaciones de rutas de Qwen3.5 0.8B aparecen en sus tablas anteriores.


### Sistema A

| Etiqueta de ruta del modelo | Comprobación | Resultado | Tokens de entrada | Duración de solicitud |
|---|---|---|---:|---:|
| bonsai-2-27b | context | Aprobado | 65,621 | 88.746 s |
| bonsai-2-27b | quick | Aprobado | 57 | 6.429 s |
| bonsai-2-27b | stream | Aprobado |  | 9.371 s |
| bonsai-2-27b | tools | Aprobado |  | 10.478 s |
| deepseek-coder-v2:16b | context | Incompatible | 50,477 |  |
| deepseek-coder-v2:16b | quick | Aprobado | 77 | 43.239 s |
| flash-iq2 | context | Aprobado | 66,007 | 213.25 s |
| flash-iq2 | quick | Aprobado |  | 56.03 s |
| flash-iq2 | stream | Aprobado |  | 1.35 s |
| flash-iq2 | tools | Aprobado |  | 16.55 s |
| gemma-4-12b-it | context | Aprobado | 65,590 | 51.225 s |
| gemma-4-12b-it | quick | Aprobado | 21 | 5.166 s |
| gemma-4-12b-it | stream | Aprobado |  | 4.653 s |
| gemma-4-12b-it | tools | Aprobado |  | 18.72 s |
| gemma-4-12b-it | vision | Aprobado | 115 | 7.222 s |
| gemma-4-12b-it | vision_context | Aprobado | 65,685 | 56.06 s |
| gemma-4-12b-it | vision_reverse | Aprobado | 115 | 7.467 s |
| gemma-4-e4b-it | context | Aprobado | 65,590 | 21.889 s |
| gemma-4-e4b-it | quick | Aprobado | 21 | 17.919 s |
| gemma-4-e4b-it | stream | Aprobado |  | 4.25 s |
| gemma-4-e4b-it | tools | Aprobado |  | 8.734 s |
| gpt-oss-20b | context | Aprobado | 65,637 | 159.155 s |
| gpt-oss-20b | quick | Aprobado | 73 | 10.548 s |
| gpt-oss-20b | stream | Aprobado |  | 20.594 s |
| gpt-oss-20b | tools | Aprobado |  | 9.854 + 9.849 s |
| granite-4.2-3b | context | Aprobado | 65,589 | 70.968 s |
| granite-4.2-3b | quick | Aprobado | 20 | 4.009 s |
| granite-4.2-3b | stream | Aprobado |  | 5.365 s |
| granite-4.2-3b | tools | Aprobado |  | 6.086 s |
| granite-4.2-8b | context | Aprobado | 66,082 | 88.636 s |
| granite-4.2-8b | quick | Aprobado | 20 | 5.857 s |
| granite-4.2-8b | stream | Aprobado |  | 11.826 s |
| granite-4.2-8b | tools | Aprobado |  | 11.852 s |
| qwen27b | context | Aprobado | 66,007 | 54.64 s |
| qwen27b | quick | Aprobado | 57 | 31.5 s |
| qwen27b | stream | Aprobado |  | 0.92 s |
| qwen27b | tools | Aprobado |  | 4.25 s |
| qwen3-embedding-0.6b | context | Aprobado | 32,767 | 7.736 s |
| qwen3-embedding-0.6b | quick | Aprobado | 14 | 2.125 s |
| qwen3.5-0.8b | context | Aprobado | 16,429 | 10.5 s |
| qwen3.5-0.8b | quick | Aprobado | 17 | 14.316 s |
| qwen3.5-0.8b | stream | Aprobado |  | 2.125 s |
| qwen3.5-0.8b | tools | Aprobado |  | 4.416 s |
| qwen3.5-2b | context | Aprobado | 65,581 | 11.175 s |
| qwen3.5-2b | quick | Aprobado | 17 | 4.519 s |
| qwen3.5-2b | stream | Aprobado |  | 3.736 s |
| qwen3.5-2b | tools | Aprobado |  | 5.046 s |
| qwen3.5-4b | context | Aprobado | 65,579 | 36.451 s |
| qwen3.5-4b | quick | Aprobado | 15 | 19.935 s |
| qwen3.5-4b | stream | Aprobado |  | 17.496 s |
| qwen3.5-4b | tools | Aprobado |  | 7.308 s |
| qwen3.5-4b | vision | Aprobado | 70 | 7.848 s |
| qwen3.5-4b | vision_context | Aprobado | 65,635 | 28.24 s |
| qwen3.5-4b | vision_reverse | Aprobado | 70 | 4.386 s |
| qwen3.5-9b | context | Aprobado | 65,581 | 34.139 s |
| qwen3.5-9b | quick | Aprobado | 17 | 3.88 s |
| qwen3.5-9b | stream | Aprobado |  | 3.378 s |
| qwen3.5-9b | tools | Aprobado |  | 10.204 s |
| qwen3.5-9b | vision | Aprobado | 72 | 4.441 s |
| qwen3.5-9b | vision_context | Aprobado | 65,637 | 33.745 s |
| qwen3.5-9b | vision_reverse | Aprobado | 72 | 3.97 s |
| qwen3.5:35b-a3b-q4_K_M | cancellation | Aprobado |  | 60.31 s |
| qwen3.5:35b-a3b-q4_K_M | concurrency | Aprobado |  | 26.23 / 25.33 s |
| qwen3.5:35b-a3b-q4_K_M | context | Aprobado | 248,279 | 54.215 s |
| qwen3.5:35b-a3b-q4_K_M | gateway | Aprobado | 239,153 | 148.12 s |
| qwen3.5:35b-a3b-q4_K_M | quick | Aprobado | 79 | 10.08 s |
| qwen3.5:35b-a3b-q4_K_M | stream | Aprobado | 69,429 | 38.783 s |
| qwen3.5:35b-a3b-q4_K_M | tools | Aprobado |  | 15.22 + 14.83 s |
| qwen3.5:35b-a3b-q4_K_M | vision | Aprobado |  | 18.39 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | context | Aprobado | 65,845 | 139.57 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | quick | Aprobado | 15 | 3.97 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | stream | Aprobado |  | 0.45 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | tools | Aprobado | 293 | 5.48 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | vision | Aprobado | 38 | 0.59 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | context | Aprobado | 65,847 | 201.41 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | quick | Aprobado | 17 | 54.62 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | stream | Aprobado |  | 1.2 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | tools | Aprobado |  | 22.18 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | vision | Aprobado |  | 3.86 s |

### Sistema B

| Etiqueta de ruta del modelo | Comprobación | Resultado | Tokens de entrada | Duración de solicitud |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Aprobado | 65,590 | 299.163 s |
| gemma-4-12b-it | quick | Aprobado | 21 | 15.261 s |
| gemma-4-12b-it | stream | Aprobado |  | 148.792 s |
| gemma-4-12b-it | tools | Aprobado |  | 34.124 s |
| gemma-4-12b-it | vision | Aprobado | 120 | 61.455 s |
| gemma-4-12b-it | vision_context | Aprobado | 65,690 | 295.581 s |
| gemma-4-12b-it | vision_reverse | Aprobado | 120 | 32.511 s |
| gemma3-4b | context | Aprobado | 65,584 | 67.382 s |
| gemma3-4b | quick | Aprobado | 15 | 6.329 s |
| gemma3-4b | stream | Aprobado |  | 24.138 s |
| gemma3-4b | vision | Aprobado | 306 | 7.018 s |
| gemma3-4b | vision_context | Aprobado | 65,876 | 70.912 s |
| gemma3-4b | vision_reverse | Aprobado | 306 | 5.762 s |
| gpt-oss-20b | context | Aprobado | 65,637 | 206.767 s |
| gpt-oss-20b | quick | Aprobado | 72 | 16.583 s |
| gpt-oss-20b | stream | Aprobado |  | 32.075 s |
| gpt-oss-20b | tools | Aprobado |  | 28.102 s |
| nomic-embed-text | context | Incompleto | 2,048 |  |
| nomic-embed-text | quick | Aprobado |  | 7.117 s |
| qwen3-14b | context | Incompleto |  | 1800.09 s |
| qwen3-14b | quick | Aprobado | 15 | 37.199 s |
| qwen3-14b | stream | Aprobado |  | 35.471 s |
| qwen3-14b | tools | Aprobado |  | 87.554 s |
| qwen3-8b | context | Excluido del alcance bajo 65K |  |  |
| qwen3-8b | quick | Fuera del alcance bajo 65K, aprobado | 15 | 21.059 s |
| qwen3-8b | stream | Excluido del alcance bajo 65K |  |  |
| qwen3-8b | tools | Excluido del alcance bajo 65K |  |  |
| qwen3.5-9b | context | Aprobado | 65,579 | 282.796 s |
| qwen3.5-9b | litellm_long_route | Aprobado | 72,265 | 263 s |
| qwen3.5-9b | post_external_stop_mining | Aprobado |  |  |
| qwen3.5-9b | quick | Aprobado | 15 | 25.881 s |
| qwen3.5-9b | stream | Aprobado |  | 143.44 s |
| qwen3.5-9b | tools | Aprobado |  | 31.812 s |
| qwen3.5-9b | vision | Aprobado | 75 | 32.015 s |
| qwen3.5-9b | vision_context | Aprobado | 65,640 | 396.288 s |
| qwen3.5-9b | vision_reverse | Aprobado | 75 | 28.626 s |

### Sistema C

| Etiqueta de ruta del modelo | Comprobación | Resultado | Tokens de entrada | Duración de solicitud |
|---|---|---|---:|---:|
| gemma-4-12b-it | aperture_context | Aprobado | 67,255 | 274.24 s |
| gemma-4-12b-it | aperture_short | Aprobado | 35 | 39.32 s |
| gemma-4-12b-it | aperture_stream_context | Aprobado | 67,255 | 282.16 s |
| gemma-4-12b-it | context | Aprobado | 65,670 | 313.661 s |
| gemma-4-12b-it | gateway_context | Aprobado | 67,254 | 263.07 s |
| gemma-4-12b-it | gateway_short | Aprobado | 27 | 20.98 s |
| gemma-4-12b-it | quick | Aprobado | 21 | 16.447 s |
| gemma-4-12b-it | stream | Aprobado |  | 15.175 s |
| gemma-4-12b-it | tools | Aprobado |  | 37.821 s |
| gemma-4-12b-it | vision | Aprobado | 120 | 58.52 s |
| gemma-4-12b-it | vision_context | Aprobado | 65,690 | 308.759 s |
| gemma-4-12b-it | vision_reverse | Aprobado | 120 | 31.25 s |
| gemma3-4b | aperture_context | Aprobado | 84,045 | 87.68 s |
| gemma3-4b | aperture_after_system_d_route_change | Aprobado | 24 | 5.42 s |
| gemma3-4b | aperture_short | Aprobado | 22 | 5.45 s |
| gemma3-4b | aperture_stream | Aprobado |  | 3.72 s |
| gemma3-4b | context | Aprobado | 65,664 | 67.543 s |
| gemma3-4b | gateway_context | Aprobado | 84,044 | 88.05 s |
| gemma3-4b | gateway_short_via_system_a | Aprobado |  | 3.16 s |
| gemma3-4b | gateway_short_via_system_e | Aprobado |  |  |
| gemma3-4b | gateway_short_via_system_f | Aprobado |  | 4.15 s |
| gemma3-4b | gateway_short_via_system_g | Aprobado |  | 6.06 s |
| gemma3-4b | quick | Aprobado | 15 | 5.163 s |
| gemma3-4b | stream | Aprobado |  | 24.691 s |
| gemma3-4b | vision | Aprobado | 306 | 7.318 s |
| gemma3-4b | vision_context | Aprobado | 65,876 | 72.476 s |
| gemma3-4b | vision_reverse | Aprobado | 306 | 5.831 s |
| gpt-oss-20b | context | Aprobado | 65,716 | 216.594 s |
| gpt-oss-20b | gateway_context | Aprobado | 84,099 | 315.83 s |
| gpt-oss-20b | gateway_short | Incoherente |  |  |
| gpt-oss-20b | quick | Aprobado | 72 | 21.603 s |
| gpt-oss-20b | stream | Aprobado |  | 31.957 s |
| gpt-oss-20b | tools | Aprobado |  | 26.096 s |
| nomic-embed-text | context | Fuera del alcance bajo 65K, incompleto | 2,048 |  |
| nomic-embed-text | quick | Fuera del alcance bajo 65K, aprobado |  | 4.178 s |
| qwen3-14b | context | Fuera del alcance bajo 65K, incompleto |  | 1800.06 s |
| qwen3-14b | quick | Fuera del alcance bajo 65K, aprobado | 15 | 35.809 s |
| qwen3-14b | stream | Fuera del alcance bajo 65K, aprobado |  | 35.43 s |
| qwen3-14b | tools | Fuera del alcance bajo 65K, aprobado |  | 87.723 s |
| qwen3-8b | context | Excluido del alcance bajo 65K |  |  |
| qwen3-8b | quick | Fuera del alcance bajo 65K, aprobado | 15 | 21.293 s |
| qwen3-8b | stream | Fuera del alcance bajo 65K, incompleto |  | 900.01 s |
| qwen3-8b | tools | Excluido del alcance bajo 65K |  |  |
| qwen3.5-9b | context | Aprobado | 65,662 | 287.984 s |
| qwen3.5-9b | gateway_context | Aprobado | 75,648 | 319.36 s |
| qwen3.5-9b | gateway_short | Aprobado | 21 | 72.14 s |
| qwen3.5-9b | quick | Aprobado | 15 | 24.635 s |
| qwen3.5-9b | stream | Aprobado |  | 143.157 s |
| qwen3.5-9b | tools | Aprobado |  | 30.395 s |
| qwen3.5-9b | vision | Aprobado | 75 | 27.756 s |
| qwen3.5-9b | vision_context | Aprobado | 65,640 | 398.797 s |
| qwen3.5-9b | vision_reverse | Aprobado | 75 | 28.645 s |

### Sistema D

| Etiqueta de ruta del modelo | Comprobación | Resultado | Tokens de entrada | Duración de solicitud |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Aprobado | 65,590 | 275.395 s |
| gemma-4-12b-it | exact_digest_aperture_65k | Aprobado | 72,057 | 300.67 s |
| gemma-4-12b-it | exact_digest_broker_short | Aprobado | 34 | 30.74 s |
| gemma-4-12b-it | quick | Aprobado | 21 | 15.05 s |
| gemma-4-12b-it | stream | Aprobado |  | 14.722 s |
| gemma-4-12b-it | tools | Aprobado |  | 33.869 s |
| gemma-4-12b-it | vision | Aprobado | 120 | 56.315 s |
| gemma-4-12b-it | vision_context | Aprobado | 65,690 | 282.174 s |
| gemma-4-12b-it | vision_reverse | Aprobado | 120 | 29.978 s |
| gemma3-4b | context | Aprobado | 65,584 | 63.564 s |
| gemma3-4b | exact_digest_65k_recall | Fallido | 67,252 | 62.07 s |
| gemma3-4b | quick | Aprobado | 15 | 5.151 s |
| gemma3-4b | stream | Aprobado |  | 22.552 s |
| gemma3-4b | vision | Aprobado | 306 | 8.276 s |
| gemma3-4b | vision_context | Aprobado | 65,876 | 67.575 s |
| gemma3-4b | vision_reverse | Aprobado | 306 | 5.651 s |
| gpt-oss-20b | context | Aprobado | 65,637 | 189.07 s |
| gpt-oss-20b | exact_digest_aperture_65k | Aprobado | 72,104 | 245.94 s |
| gpt-oss-20b | exact_digest_broker_short | Aprobado | 84 | 15.96 s |
| gpt-oss-20b | quick | Aprobado | 72 | 15.431 s |
| gpt-oss-20b | stream | Aprobado |  | 31.052 s |
| gpt-oss-20b | tools | Aprobado |  | 23.65 s |
| nomic-embed-text | context | Incompleto | 2,048 |  |
| nomic-embed-text | quick | Aprobado |  | 2.798 s |
| qwen3-14b | context | Incompleto | 40,939 | 872.209 s |
| qwen3-14b | quick | Aprobado | 15 | 36.021 s |
| qwen3-14b | stream | Aprobado |  | 33.491 s |
| qwen3-14b | tools | Aprobado |  | 82.471 s |
| qwen3-8b | context | Incompleto |  | 1800.07 s |
| qwen3-8b | quick | Aprobado | 15 | 19.283 s |
| qwen3-8b | stream | Aprobado |  | 19.401 s |
| qwen3-8b | tools | Aprobado |  | 65.054 s |
| qwen3.5-9b | context | Aprobado | 65,579 | 258.048 s |
| qwen3.5-9b | exact_digest_aperture_65k | Aprobado | 81,051 | 324.07 s |
| qwen3.5-9b | exact_digest_broker_short | Aprobado | 29 | 94.48 s |
| qwen3.5-9b | quick | Aprobado | 15 | 27.16 s |
| qwen3.5-9b | stream | Aprobado |  | 28.62 s |
| qwen3.5-9b | tools | Aprobado |  | 28.129 s |
| qwen3.5-9b | vision | Aprobado | 75 | 25.047 s |
| qwen3.5-9b | vision_context | Aprobado | 65,640 | 369.477 s |
| qwen3.5-9b | vision_reverse | Aprobado | 75 | 27.602 s |

### Sistema E

| Etiqueta de ruta del modelo | Comprobación | Resultado | Tokens de entrada | Duración de solicitud |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Aprobado | 65,590 | 49.086 s |
| gemma-4-e4b-it | quick | Aprobado | 21 | 23.911 s |
| gemma-4-e4b-it | stream | Aprobado |  | 28.136 s |
| gemma-4-e4b-it | tools | Aprobado |  | 56.756 s |
| granite-4.0-h-tiny | context | Aprobado | 65,566 |  |
| granite-4.0-h-tiny | quick | Aprobado | 35 | 10.408 s |
| granite-4.0-h-tiny | stream | Aprobado |  | 27.798 s |
| granite-4.0-h-tiny | tools | Aprobado |  | 43.304 s |
| granite-4.2-3b | context | Aprobado | 65,589 | 1014.03 s |
| granite-4.2-3b | quick | Aprobado | 20 | 14.569 s |
| granite-4.2-3b | stream | Aprobado |  | 6.948 s |
| granite-4.2-3b | tools | Aprobado |  | 56.376 s |
| qwen3-embedding-0.6b | context | Aprobado | 32,767 | 20.387 s |
| qwen3-embedding-0.6b | quick | Aprobado | 14 | 9.592 s |
| qwen3.5-0.8b | context | Aprobado | 16,429 | 9.128 s |
| qwen3.5-0.8b | quick | Aprobado | 17 | 452.417 s |
| qwen3.5-0.8b | stream | Aprobado |  | 11.163 s |
| qwen3.5-0.8b | tools | Aprobado |  | 39.214 s |
| qwen3.5-2b | context | Aprobado | 65,579 | 30.343 s |
| qwen3.5-2b | quick | Aprobado | 15 | 12.509 s |
| qwen3.5-2b | stream | Aprobado |  | 26.165 s |
| qwen3.5-2b | tools | Aprobado |  | 42.056 s |
| qwen3.5-4b | context | Aprobado | 65,579 | 53.787 s |
| qwen3.5-4b | quick | Aprobado | 15 | 26.736 s |
| qwen3.5-4b | stream | Aprobado |  | 26.02 s |
| qwen3.5-4b | tools | Aprobado |  | 57.293 s |
| qwen3.5-4b | vision | Aprobado | 72 | 10.09 s |
| qwen3.5-4b | vision_context | Aprobado | 65,637 | 44.88 s |
| qwen3.5-4b | vision_reverse | Aprobado | 72 | 9.96 s |

### Sistema F

| Etiqueta de ruta del modelo | Comprobación | Resultado | Tokens de entrada | Duración de solicitud |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Aprobado | 65,590 | 98.443 s |
| gemma-4-e4b-it | quick | Aprobado | 21 | 27.51 s |
| gemma-4-e4b-it | stream | Aprobado |  | 28.042 s |
| gemma-4-e4b-it | tools | Aprobado |  | 73.891 s |
| granite-4.0-h-tiny | context | Aprobado | 65,599 | 19.692 s |
| granite-4.0-h-tiny | quick | Aprobado | 35 | 43.818 s |
| granite-4.0-h-tiny | stream | Aprobado |  | 27.296 s |
| granite-4.0-h-tiny | tools | Aprobado |  | 75.377 s |
| granite-4.2-3b | context | Aprobado | 65,589 | 145.179 s |
| granite-4.2-3b | quick | Aprobado | 20 | 15.703 s |
| granite-4.2-3b | stream | Aprobado |  | 35.482 s |
| granite-4.2-3b | tools | Aprobado |  | 52.539 s |
| qwen3-embedding-0.6b | context | Aprobado | 32,767 | 20.656 s |
| qwen3-embedding-0.6b | quick | Aprobado | 14 | 8.122 s |
| qwen3.5-0.8b | context | Aprobado | 16,429 | 13.326 s |
| qwen3.5-0.8b | quick | Aprobado | 17 | 445.22 s |
| qwen3.5-0.8b | stream | Aprobado |  | 13.266 s |
| qwen3.5-0.8b | tools | Aprobado |  | 40.825 s |
| qwen3.5-2b | context | Aprobado | 65,579 | 61.282 s |
| qwen3.5-2b | quick | Aprobado | 15 | 16.738 s |
| qwen3.5-2b | stream | Aprobado |  | 25.29 s |
| qwen3.5-2b | tools | Aprobado |  | 47.444 s |
| qwen3.5-4b | context | Aprobado | 65,579 | 93.753 s |
| qwen3.5-4b | quick | Aprobado | 15 | 33.039 s |
| qwen3.5-4b | stream | Aprobado |  | 25.658 s |
| qwen3.5-4b | tools | Aprobado |  | 71.731 s |
| qwen3.5-4b | vision | Aprobado | 70 | 43.053 s |
| qwen3.5-4b | vision_context | Aprobado | 65,635 | 84.749 s |
| qwen3.5-4b | vision_reverse | Aprobado | 70 | 27.518 s |

### Sistema G

| Etiqueta de ruta del modelo | Comprobación | Resultado | Tokens de entrada | Duración de solicitud |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Aprobado | 65,590 | 92.696 s |
| gemma-4-e4b-it | quick | Aprobado | 21 | 38.329 s |
| gemma-4-e4b-it | stream | Aprobado |  | 43.549 s |
| gemma-4-e4b-it | tools | Aprobado |  | 66.616 s |
| granite-4.0-h-tiny | context | Aprobado | 65,599 | 69.777 s |
| granite-4.0-h-tiny | quick | Aprobado | 35 | 33.17 s |
| granite-4.0-h-tiny | stream | Aprobado |  | 31.751 s |
| granite-4.0-h-tiny | tools | Aprobado |  | 63.338 s |
| granite-4.2-3b | context | Aprobado | 65,589 | 100.849 s |
| granite-4.2-3b | quick | Aprobado | 20 | 23.355 s |
| granite-4.2-3b | stream | Aprobado |  | 28.75 s |
| granite-4.2-3b | tools | Aprobado |  | 44.226 s |
| qwen3-embedding-0.6b | context | Aprobado | 32,767 | 23.055 s |
| qwen3-embedding-0.6b | quick | Aprobado | 14 | 8.924 s |
| qwen3.5-0.8b | context | Aprobado | 16,429 | 16.74 s |
| qwen3.5-0.8b | quick | Aprobado | 17 | 504.813 s |
| qwen3.5-0.8b | stream | Aprobado |  | 15.095 s |
| qwen3.5-0.8b | tools | Aprobado |  | 36.672 s |
| qwen3.5-2b | context | Aprobado | 65,579 | 76.731 s |
| qwen3.5-2b | quick | Aprobado | 15 | 20.949 s |
| qwen3.5-2b | stream | Aprobado |  | 25.194 s |
| qwen3.5-2b | tools | Aprobado |  | 37.552 s |
| qwen3.5-4b | context | Aprobado | 65,579 | 90.807 s |
| qwen3.5-4b | quick | Aprobado | 15 | 41.84 s |
| qwen3.5-4b | stream | Aprobado |  | 40.812 s |
| qwen3.5-4b | tools | Aprobado |  | 54.999 s |
| qwen3.5-4b | vision | Aprobado | 70 | 29.619 s |
| qwen3.5-4b | vision_context | Aprobado | 65,635 | 87.496 s |
| qwen3.5-4b | vision_reverse | Aprobado | 70 | 26.283 s |

## Cómo probé la viabilidad de Hermes

Usé un marcador sintético cerca del inicio de una solicitud larga y pedí el marcador después del texto de relleno. La respuesta debía devolver el valor esperado. El número de tokens de entrada informado por el servidor determinó el tamaño de la solicitud. Un modelo que respondía normalmente tras una solicitud larga también fallaba si el marcador inicial era incorrecto.

La progresión de Qwen3.5 35B usó registros numerados de relleno, temperatura 0 y longitudes crecientes de 3.800, 6.800, 10.000 y 13.600 registros. Esas etapas devolvieron 69.429, 124.179, 182.579 y 248.279 tokens de solicitud. El modelo permaneció cargado entre etapas, lo que permitió reutilizar el prefijo. Las comprobaciones independientes de Qwen3.6 cerca del límite indicaron cero tokens en caché.

La solicitud larga del modelo 0.8B repitió `river stone lantern orchard circuit velvet compass marble` 8.400 veces entre una clave de respuesta inicial y una pregunta final de recuperación. La ejecución nativa envió `think:false`, `num_ctx:131072`, `stream:false` y `keep_alive:0`. La ruta compatible con OpenAI usó `reasoning_effort:"none"`. El intermediario impuso el modo sin razonamiento para su ruta, por lo que quienes usaban la pasarela no necesitaban cambiar la solicitud.

### Comprobaciones de herramientas, visión y liberación

Las pruebas de herramientas comprobaron tanto la solicitud como la respuesta posterior al resultado devuelto por la herramienta. Una prueba sencilla usó `add_numbers(7, 11)` y esperaba 18. La prueba de Qwen3.5 35B usó `lookup_square` y esperaba 49. GPT-OSS hizo una consulta de inventario y tuvo que incorporar el resultado devuelto.

Las comprobaciones de visión usaron preguntas sobre imágenes rojas y azules, invirtieron el orden de las imágenes e incluyeron colores de imagen y marcadores iniciales y finales en solicitudes largas. La prueba de Qwen3.5 35B usó un PNG rojo de 256 × 256. Fue necesaria una reparación de conversión de contenido de imagen en el intermediario antes de que esta solicitud pasara. La prueba larga de visión 4B del sistema E exigió que sobrevivieran a la entrada ambos marcadores y el orden de colores.

Durante las ejecuciones largas comprobé la memoria GPU, la residencia del modelo, las temperaturas, la presión de memoria del anfitrión, los eventos OOM y los fallos GPU. La protección de Qwen3.5 35B también comprobó la liberación tras una interrupción controlada. Las comprobaciones posteriores de cancelación del cliente y de solicitudes en cola ejercitaron la ruta del intermediario. Dos solicitudes en cola demuestran el manejo de solicitudes bajo la carga probada, no dos backends GPU simultáneos e independientes.

### Cómo interpretar los resultados de rendimiento

Las duraciones de las solicitudes incluyen el prellenado de entradas largas y la respuesta devuelta. No representan tokens generados por segundo. El retraso hasta el primer contenido importa en la transmisión, y las progresiones de prefijos en caché requieren su propia interpretación.

Las ejecuciones posteriores satisfactorias de modelos grandes en los sistemas A y C usaron ventanas de inferencia dedicadas con la minería inactiva. Los modelos se descargaron después de esas solicitudes. La minería se restauró en los siete sistemas al finalizar la ventana de prueba. Estos resultados describen el servicio de modelos durante una ventana de inferencia, no minería e inferencia simultáneas.

## Perfiles de backend usados en las pruebas

Elige el perfil correspondiente a la carga que quieras reproducir. La cuantización, el contexto de ejecución, el tipo de caché, el modo de razonamiento y la ubicación de las GPU afectan el resultado.

| Sistema y modelo | Perfil de backend probado |
|---|---|
| A, Qwen3.5 35B-A3B Q4_K_M | Ollama 0.34.2, caché KV f16, ambas RTX 5060 Ti de 16 GB, 64 GiB de RAM del anfitrión y contexto de ejecución 262.144 para la progresión larga. Las solicitudes nativas usaron `think:false`, temperatura 0, transmisión y cinco minutos de permanencia entre etapas. Las solicitudes de pasarela usaron el intermediario y LiteLLM. Sin límite de salida de solicitud. |
| A, Qwen3.8 27B | llama.cpp bajo demanda mediante el intermediario y LiteLLM, contexto de ejecución 262.144, una ranura de inferencia, caché K/V Q4 y ambas RTX 5060 Ti. La solicitud de 66.007 tokens no tuvo límite de salida. |
| A, Qwen3.6-35B-A3B UD-Q4_K_XL | Strata 0.1.48, contexto 131.072, caché KV INT8, una GPU seleccionada, límite de memoria del grupo de procesos de 55 GiB, límite de ejecución de 30 minutos, carga diferida y descarga tras 60 segundos inactivos. Respuesta larga piloto: 217 tokens de salida. Respuesta de pasarela cerca del límite: 11 tokens de salida, sin límite de salida de solicitud. |
| A, Qwen3.8-Flash-Next UD-IQ4_XS | Strata 0.1.48, contexto 98.304, caché KV Q4, caché de expertos residente de 8 GiB y ambas RTX 5060 Ti. Límite de memoria piloto de 52 GiB y ruta posterior de 54 GiB. Respuesta larga piloto: 10 tokens de salida. Las combinaciones anteriores con contextos y cachés mayores se detuvieron al alcanzar límites de memoria. |
| A, Granite 4.2 8B | Pesos GGUF Q6_K, proceso de trabajo compartido de llama.cpp, contexto 131.072, caché K/V Q4_0, `--n-predict -1`. La solicitud larga usó temperatura 0, transmisión del uso y ningún límite de salida. |
| A, DeepSeek Coder V2 16B | Pesos GGUF Q4_0, Ollama 0.34.2, dos RTX 5060 Ti, 64 GiB de RAM del anfitrión. Las pruebas separadas de caché f16, Q4_0 y Q8_0 usaron los contextos de ejecución mostrados en la tabla comparativa. Sin límite de salida de solicitud. |
| B, C, D, servicio Ollama auditado | Ollama 0.34.2, contexto 131.072, paralelismo 1, un modelo cargado, cola de tamaño 128, permanencia 0, Flash Attention, caché KV Q4_0. |
| B, piloto de pasarela Qwen3.5 9B | Tiempo de espera de ruta LiteLLM de 1.800 segundos, cero reintentos y sin límite de contexto ni de tokens de salida. Ambos marcadores se retuvieron con 72.265 tokens de entrada. La comprobación independiente de recuperación de minería pasó. |
| C, Qwen3.5 0.8B | Pesos Q8_0 en una RTX 2000E Ada con un perfil de potencia de 30 W. Contexto 131.072. `think:false` nativo, `reasoning_effort:"none"` compatible con OpenAI y sin límite de salida. El alias del intermediario fijó el contexto de ejecución e impuso el modo sin razonamiento. |
| C, Gemma 4 12B-IT | Perfil Ollama de una sola GPU, contexto 131.072 y solicitudes de Aperture transmitidas y sin transmisión, sin límite de salida. La ejecución directa de Aperture llegó a 75 C y 30,64 W con el perfil configurado de 30 W y después se descargó. |
| D, Qwen3.5 9B, Gemma 4 12B-IT, GPT-OSS 20B | Artefactos instalados exactos probados mediante Aperture, contexto 131.072, residencia total en una GPU y finalización natural sin límite de salida de solicitud. |
| E, F, G, procesos de chat de llama.cpp | Compilación 11669, 99 capas GPU, paralelismo 1, Flash Attention, caché K/V Q4_0, `--n-predict -1`. El contexto de ejecución variaba según la familia de modelos. |

Los perfiles de servicio registrados describen sus propias configuraciones de ejecución. El perfil Qwen3.5 35B con caché f16 probado por separado en el sistema A no hereda los ajustes de caché Q4_0 de los sistemas Ollama más pequeños.

### Huellas de modelos para las nuevas pruebas de entrada retenida

Estos identificadores distinguen los artefactos probados de otras descargas o alias con nombres similares.

| Artefacto | Cuantización | Huella registrada o SHA-256 del archivo |
|---|---|---|
| Etiqueta Ollama de Qwen3.5 35B-A3B | Q4_K_M | `72aac7c28be8ff9b81c2a270eb489c88e6d822a76ec0cb7bf34d965768848567` |
| Etiqueta Ollama base de Qwen3.5 0.8B | Q8_0 | `de63045f29755d4721c09d54c9b45c2dadb644f4fd7d604d4cac90d96049971c` |
| Archivo GGUF de Granite 4.2 8B | Q6_K | `5ad3d67f6fe09a448031029bead7f6a088697ca2787c0c5640bf964c59df1a21` |

Las huellas de manifiestos Ollama y los valores SHA-256 de archivos de pesos identifican objetos diferentes. Asocia el identificador con el tipo de artefacto de la tabla.

## Qué ejecutaría con Hermes

Usaría Qwen3.5 35B como ruta principal de contexto amplio en el sistema de dos RTX 5060 Ti. Su resultado de retención de 239.153 tokens por la pasarela, las comprobaciones independientes de herramientas y visión y la liberación de solicitudes verificada respaldan mejor esta elección que un modelo anunciado con una gran ventana de contexto. Mantendría Qwen3.8 27B para respuestas más rápidas en solicitudes comparables de 66K y Qwen3.6 cuando importe usar una sola tarjeta.

En los sistemas RTX 2000E Ada, elegiría la ruta Gemma 3 4B verificada del sistema C para la carga probada de respuesta con entrada larga. Probaría la ruta Qwen3.5 0.8B sin razonamiento para recuperación y extracción acotadas. Las rutas mayores Gemma, Qwen y GPT-OSS sirven para tareas que acepten sus respuestas iniciales probadas de cuatro a cinco minutos. Excluiría de la selección la ruta Gemma 3 fallida del sistema D.

Para las tarjetas RTX 3060 Ti y RTX 3070 de 8 GB, empezaría con Qwen3.5 2B o 4B. Sus resultados de texto a 65K y las comprobaciones de imagen 4B respaldan una configuración inicial útil sin dedicar las dos tarjetas de 16 GB a todas las solicitudes. La presión de memoria de Flash Next y el comportamiento incompleto a 65K de DeepSeek Coder V2 hacen que sean opciones predeterminadas menos adecuadas en los perfiles probados.

Las pruebas respaldan estas opciones de modelos y sistemas para flujos de trabajo específicos. La retención de entradas, un intercambio correcto con una herramienta, el reconocimiento de imágenes y la liberación limpia responden a aspectos diferentes de la viabilidad de Hermes. Una configuración fiable necesita los comportamientos que usa tu agente y suficiente contexto para la respuesta y el tráfico de herramientas.

## Fuentes y lecturas relacionadas

- [Configuración de proveedores y requisitos de contexto de Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md)
- [Especificaciones de NVIDIA GeForce RTX 3060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3060-3060ti/)
- [Especificaciones de NVIDIA GeForce RTX 5060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/)
- [Descripción general de Hermes Agent](/hermes-local-ai-broker-course/01-hermes-agent-overview/)
- [Elegir un backend de modelo local](/hermes-local-ai-broker-course/02-choose-a-backend/)
