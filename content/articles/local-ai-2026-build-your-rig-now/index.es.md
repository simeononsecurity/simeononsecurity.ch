---
title: "IA local en 2026: un modelo 27B supera a Sonnet 4.6 mientras se cierra la ventana para comprar equipos"
date: 2026-09-22
lastmod: 2026-11-15
toc: true
draft: false
description: "Planifica un equipo de IA local para 2026 según el tamaño del modelo, la VRAM, el ancho de banda de memoria, el consumo, el coste y las opciones de ampliación."
genre: ["IA local", "IA autoalojada", "Modelos de pesos abiertos", "Equipos para IA", "Aprendizaje automático", "Cuantización", "Laboratorio doméstico", "Privacidad", "Economía de la IA", "Equipos de consumo"]
tags: ["ia local", "ejecutar llm localmente", "qwen3.8", "qwen3.8 27b", "bonsai 2 27b", "ternary bonsai", "prism ml", "cuantización ternaria", "cuantización de 1,58 bits", "cuantización llm", "claude sonnet 4.6", "sonnet 4.6 frente a modelo local", "pesos abiertos", "modelo moe", "mezcla de expertos", "ollama", "llama.cpp", "rtx 5090", "vram", "inferencia local", "precios gpu 2026", "escasez de dram", "precios de memoria", "montar un pc para ia", "ia para laboratorio doméstico", "coste de suscripción de ia", "openrouter", "artificial analysis", "guía de compra de gpu", "llm autoalojado", "ia que protege la privacidad", "equipos de ia 2026"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Espacio de trabajo de alta tecnología con una tarjeta gráfica y varias pantallas iluminadas que muestran resultados de IA y visualizaciones sobre un fondo azul oscuro."
coverCaption: ""
ref: ["/articles/ai-models-raspberry-pi-4-5", "/articles/building-a-privacy-preserving-meshtastic-ai-assistant"]
---

**Un modelo descargable que cabe en una sola tarjeta gráfica de consumo ya supera a un modelo de API de primera línea en el índice global de inteligencia.** Qwen3.8 27B es un modelo de visión y lenguaje con pesos abiertos, publicado en agosto de 2026. Su versión reempaquetada en ternario, Bonsai 2 27B, reduce los mismos pesos a 5.53 GiB. En conjunto, marcan el momento en que la inferencia local dejó de ser una concesión para aficionados y se convirtió en una alternativa real a una API de pago.

*La ventana para comprar equipos se está cerrando. La memoria no había sido tan cara en dos décadas, y su precio también está elevando el de las tarjetas gráficas.*

Este artículo presenta los resultados de las pruebas, las diferencias entre los dos modelos, los aspectos en los que el modelo abierto aún pierde y por qué los próximos doce meses no son un buen momento para esperar.

**Qué obtendrás:** elige un modelo y una capacidad de memoria según tu carga de trabajo. Antes de comprar, compara el coste del equipo, la electricidad, la longitud del contexto y el rendimiento medido. La comparación de pruebas no predice la calidad para tus tareas ni el precio futuro de tu GPU.

## Respuesta breve

**La diferencia de inteligencia entre un modelo local 27B y una API de pago cercana a los modelos de primera línea ha desaparecido. Las ventajas restantes del modelo de pago son menores de lo que sugiere la diferencia de precio.**

Se produjeron tres cambios a la vez:

- **Los modelos abiertos 27B alcanzaron puntuaciones cercanas a los líderes.** Qwen3.8 27B obtiene 33.7 en el Intelligence Index frente a 30.1 de Sonnet 4.6, en la misma batería de evaluación.
- **La cuantización ternaria redujo la necesidad de memoria en aproximadamente dos tercios.** Bonsai 2 27B ejecuta el modelo 27B completo en **5.53 GiB**, una capacidad disponible en tarjetas que cuestan unos cientos de dólares.
- **El suministro de memoria empeoró.** Los precios contractuales de la DRAM convencional subieron entre **90 y 95 %** en el primer trimestre de 2026 respecto al anterior. TrendForce no había registrado un aumento trimestral mayor y las GPU de nueva generación se retrasaron hasta 2028.

*Comprar o montar un equipo ahora es la opción más barata. No es un argumento de venta, sino lo que indican los datos de suministro.*

## Mira la prueba con una sola GPU

La afirmación anterior merece una demostración, no una tabla. Bijan Bowen probó Bonsai 2 27B en un equipo con una sola GPU y se preguntó si es el mejor modelo disponible hoy para una tarjeta.

{{< youtube id="OA5cICIzD-c" enable="true" title="Primera prueba de Bonsai 2 27B: ¿es el MEJOR modelo de IA para una sola GPU?" description="Primer análisis del modelo ternario Bonsai 2 27B en una sola GPU de consumo, con atención a la velocidad, la calidad y las alternativas." >}}

*Fíjate en la calidad de la respuesta, no en los tokens por segundo. La velocidad es lo más fácil de mejorar.*

## Dos nombres, un modelo

Los dos modelos de los que hablamos no compiten entre sí. **Son los mismos pesos con dos niveles de precisión distintos.**

| | Qwen3.8 27B | Bonsai 2 27B ternario |
|---|---|---|
| **Qué es** | El modelo original de Qwen con pesos abiertos | Reempaquetado ternario de Qwen3.8-27B por Prism ML |
| **Pesos en disco** | **18 GB** | **5.53 GiB** (PTQ1_0) o **6.70 GiB** (PQ2_0) |
| **Parámetros** | 27B denso | 26.90B, misma arquitectura |
| **Contexto** | 256K | 262,144 tokens |
| **Visión** | Sí, nativa | Sí, proyector CLIP en un paquete aparte |
| **Llamadas a herramientas** | Sí | Sí |
| **Licencia** | Apache 2.0 | Apache 2.0 |
| **Entorno de ejecución** | Ollama, llama.cpp, MLX | Solo **el fork de llama.cpp de Prism ML** |

La página de la biblioteca de Ollama para `qwen3.8` indica que el modelo 27B ocupa **18 GB**, admite un contexto de 256K, visión y llamadas a herramientas, y dispone de una compilación MLX independiente para Apple Silicon. La versión ternaria de Ollama es un espejo de los paquetes GGUF Apache-2.0 de Prism ML, republicados con las mismas sumas de comprobación.

**La pregunta práctica no es qué modelo elegir.** Es cuánta memoria quieres dedicar a la misma inteligencia. La versión ternaria usa aproximadamente un tercio de memoria y pierde poco a cambio.

{{< figure src="local-ai-architecture-comparison.webp" alt="Diagrama que compara la memoria del mismo modelo 27B: 18 GB con precisión estándar y 5.53 GiB con pesos ternarios; ambas versiones caben en una sola GPU de consumo" >}}

## Comparación de resultados

Artificial Analysis evalúa ambos modelos con la misma batería. Conviene leer los resultados fila por fila, no resumirlos, porque cada modelo destaca en áreas distintas.

| Medida | Qwen3.8 27B | Claude Sonnet 4.6 | Líder |
|---|---|---|---|
| **Intelligence Index** | **33.7** | 30.1 | Abierto |
| **Coding Index** | **68.1** | 63.0 | Abierto |
| **Agentic Index** | **45.8** | 31.8 | Abierto |
| **GPQA Diamond** | **90.5%** | 87.5% | Abierto |
| **Humanity's Last Exam** | **33.9%** | 33.6% | Abierto |
| **AA-LCR (contexto largo)** | **82.0%** | 80.0% | Abierto |
| **GDPval-AA** | **45.4%** | 36.0% | Abierto |
| **CritPt (física de investigación)** | **5.4%** | 3.1% | Abierto |
| **Tasa sin alucinaciones** | **69.7%** | 51.6% | Abierto |
| **SciCode** | 46.6% | **50.1%** | Sonnet |
| **Precisión AA-Omniscience** | 15.6% | **40.9%** | Sonnet |

*El modelo abierto lidera en nueve de las once filas comparables, incluidos todos los índices globales.*

### Dónde gana el modelo abierto

Los tres índices globales resumen el resultado. **Intelligence: 33.7 frente a 30.1, Coding: 68.1 frente a 63.0 y Agentic: 45.8 frente a 31.8.** La diferencia es mayor en el índice de agentes. Esto es importante sobre todo para quienes ejecutan flujos automatizados de varios pasos en lugar de consultas individuales.

Como referencia porcentual, Artificial Analysis sitúa a Qwen3.8 27B **por encima del 86 % de modelos en el índice de agentes** y del 76 % en programación. Sonnet 4.6 queda en el 68 % y el 72 %, respectivamente. En razonamiento científico de nivel avanzado, el modelo abierto obtiene **90.5 %** en GPQA Diamond.

### Dónde Sonnet 4.6 sigue ganando

Dos resultados van en la dirección contraria, y ninguno es menor.

**AA-Omniscience mide si un modelo responde correctamente a preguntas de conocimiento a la primera. Sonnet 4.6 obtiene el 40.9 % frente al 15.6 %.** Es una diferencia amplia en fiabilidad factual y el argumento individual más sólido para pagar por un modelo de gama alta.

La tasa sin alucinaciones requiere cautela. El 69.7 % de Qwen frente al 51.6 % de Sonnet parece una victoria clara, y por sí solo lo es. Pero la métrica describe la proporción de respuestas *incorrectas* que no inventan información. Un modelo menos preciso produce más respuestas incorrectas. Por eso, los porcentajes corresponden a conjuntos distintos y no se pueden comparar directamente. **Mira primero la fila de precisión.**

Sonnet también gana SciCode con el 50.1 % frente al 46.6 %, y publica cifras en dos evaluaciones que no aparecen en la ficha del modelo abierto: IFBench y Terminal-Bench Hard. No se pueden comparar.

### Dos salvedades honestas

**Las fechas de lanzamiento están separadas por seis meses.** Sonnet 4.6 salió en febrero de 2026. Qwen3.8 27B salió en agosto de 2026. Comparar un modelo puntero de febrero con uno abierto de agosto no es una comparación equilibrada.

**Sonnet 4.6 ya no es el modelo puntero de Anthropic.** Sonnet 5 y Opus 5 están ahora por encima en la gama. El modelo abierto 27B alcanzó al buque insignia de mediados de 2026, pero no a la cima actual. Afirmar lo contrario es sacar demasiadas conclusiones de la tabla.

*Las pruebas miden el rendimiento en pruebas. Solo importa la puntuación que obtengas con tu propia carga de trabajo.*

## Qué cambian los pesos ternarios

Bonsai 2 no es un modelo más pequeño. Es el mismo modelo de 26.90B con una precisión numérica mucho menor, y los metadatos GGUF publicados dejan claro el intercambio.

| Propiedad | Valor |
|---|---|
| **Arquitectura** | `qwen35`, atención híbrida con atención completa cada cuatro capas y capas state-space |
| **Parámetros** | 26.90B |
| **Bloques** | 64 |
| **Anchura del embedding** | 5120 |
| **Atención** | 24 cabezas de consulta, 4 cabezas KV, longitud clave/valor 256 |
| **Contexto** | 262,144 tokens, base RoPE 1e7 |
| **Formato de pesos** | Ternario, grupo de 128. PQ2_0 a 2.13 bits por peso, PTQ1_0 a 1.75 |
| **Torre de visión** | CLIP, 460.73M parámetros, distribuido en un paquete proyector aparte |
| **Licencia** | Apache 2.0 |

**Los pesos ternarios hacen que cada parámetro tome uno de tres valores en vez de dieciséis.** Esa compresión es el punto central y permite que el modelo 27B completo ocupe 5.53 GiB en lugar de 18 GB.

### Rendimiento medido

Medido con `llama-bench` en una RTX 5090 de 32 GB, todas las capas descargadas en la GPU, flash attention activada, promedio de tres ejecuciones:

| Paquete | Pesos | Prefill (pp512) | Decodificación (tg128) |
|---|---|---|---|
| **PQ2_0** | 6.70 GiB | **3802.74 tok/s** | **135.41 tok/s** |
| **PTQ1_0** | 5.53 GiB | 1876.31 tok/s | 131.41 tok/s |

PQ2_0 realiza el prefill **2.03 veces más rápido** que PTQ1_0, mientras que la decodificación queda estadísticamente igualada. Por eso PQ2_0 es la opción predeterminada razonable. PTQ1_0 sirve cuando esos últimos 1.2 GiB marcan la diferencia. Con `llama-server` y un contexto de 65K, la decodificación mantuvo **136.5 tok/s** en una solicitud de transmisión.

**La velocidad de decodificación se nota en el uso diario.** 135 tokens generados en un segundo superan con creces la velocidad de lectura. La latencia no es motivo para ejecutar inferencia local, porque una API alojada ya es suficientemente rápida. Los motivos son el coste, la privacidad y el control.

### La trampa que nadie menciona

**Ollama estándar no puede cargar estos archivos.** Los núcleos ternarios están en el fork de llama.cpp de Prism ML. En la comprobación con Ollama 0.34.2, la carga falla con `unsupported tensor "output.weight" size overflows`. El entorno reconoce la arquitectura `qwen35`, pero sus bibliotecas no incluyen `pq2_0` ni `ptq1_0` y tampoco tienen un entorno de ejecución para la activación de Hadamard.

Hay otra trampa que conviene conocer antes de perder una tarde. **El paquete F16 de esta familia parece una alternativa segura, pero no lo es.** Sus tensores son F16 y F32 normales, así que el archivo se analiza y carga sin errores, pero después genera texto incoherente. Los pesos están en una base rotada que se declara en los metadatos `prism.hadamard.*`. El entorno debe aplicar la rotación correspondiente o producirá resultados absurdos. Con 50.1 GiB, el paquete F16 tampoco se puede colocar entero en una tarjeta de 32 GB.

*Lee la ficha del modelo antes de descargarlo. Un espejo comunitario no es una compilación compatible, y esta página lo dice claramente.*

## La ola MoE que viene detrás

Los modelos densos 27B son solo la mitad de la historia. Los modelos mixture-of-experts activan una pequeña fracción de sus parámetros en cada token, lo que cambia de nuevo los costes.

| Modelo | Total / activos | Contexto | Nota |
|---|---|---|---|
| **Qwen3.8 2.4T A95B** | 2.4T / 95B | 1.0M | Modelo de pesos abiertos relacionado con Qwen3.8 Max |
| **Qwen3.6 35B A3B** | 35B / 3B | 262K | Apache 2.0, MoE disperso híbrido |
| **Qwen3 Coder Next** | 80B / 3B | 256K | Pesos abiertos, diseñado para agentes de programación siempre activos |

**Qwen3 Coder Next es el modelo local que conviene seguir.** Tiene 80B parámetros en total, pero solo activa 3B en cada token. Está pensado para agentes siempre activos en entornos CLI e IDE. Un modelo que activa 3B parámetros genera a la velocidad de un modelo 3B y aprovecha las capacidades almacenadas en 80B. Las notas del proyecto describen un rendimiento comparable al de modelos con entre 10 y 20 veces más cómputo activo.

*El modelo denso 27B es la opción segura hoy. La eficiencia de los modelos dispersos aún está mejorando.*

{{< figure src="local-ai-moe-dense-tradeoff.webp" alt="Gráfico que compara un modelo denso 27B que activa todos sus parámetros por token con un modelo mixture-of-experts disperso que solo activa 3.000 millones de 80.000 millones de parámetros" >}}

## Se cierra la ventana para comprar equipos

Esta parte de la historia tiene fecha límite.

La inferencia local se abarató justo cuando la memoria que necesita empezó a encarecerse. Las dos tendencias chocan y sus efectos ya se ven en los precios minoristas.

### Qué pasó con los precios de memoria

**Los precios contractuales de la DRAM convencional subieron entre el 90 y el 95 % en el primer trimestre de 2026 respecto al trimestre anterior.** Es el mayor aumento trimestral registrado por TrendForce. La memoria flash NAND subió entre el 55 y el 60 % en el mismo periodo.

La presión no cedió. Según TrendForce, la DRAM subió otro **58–63 %** en el segundo trimestre y la NAND, entre el 70 y el 75 %. Incluso la moderación del tercer trimestre, con aumentos del 13–18 % en DRAM y del 10–15 % en NAND, se suma a dos trimestres récord en lugar de aliviar la situación.

La causa es estructural, no cíclica. Los centros de datos de IA absorben capacidad de memoria que antes se destinaba a teléfonos, portátiles y consolas. Los fabricantes de memoria asignan primero capacidad a los pedidos con márgenes más altos. Los analistas que siguen el suministro de módulos prevén que en 2027 la oferta de chips DRAM para fabricantes de módulos caiga más del 70 %.

**El director ejecutivo de Intel puso una cifra sobre la mesa.** En la cumbre AI Infrastructure Summit en Santa Clara, el 15 de septiembre de 2026, Lip-Bu Tan dijo que la memoria ya costaba "cinco, seis y siete veces" más que antes. Advirtió que ahora representa entre el 70 y el 80 % del coste de materiales de un portátil económico. En otra ocasión dijo que no habría alivio hasta 2028.

*Los artículos independientes que comparan el coste por superficie de las obleas DRAM con las obleas de lógica avanzada incluyen una salvedad importante. Los precios al contado no son los contractuales, y el mercado al contado de DDR5 es demasiado reducido para que la comparación sea concluyente. La dirección general está clara.*

{{< figure src="local-ai-memory-price-trend-2026.webp" alt="Gráfico del aumento trimestral de los precios contractuales de DRAM durante 2026: subida del 90 al 95 % en el primer trimestre, que se modera al 13–18 % en el tercero" >}}

### Efecto en las tarjetas gráficas

La memoria representa una parte importante del coste de materiales de una tarjeta gráfica, así que los precios de la DRAM repercuten directamente en los de las GPU.

| Tarjeta | Principios de 2025 | Septiembre de 2026 |
|---|---|---|
| **Nvidia RTX 5090** | $1,999 | **más de $5,000** |
| **Asus RTX 5080** | $1,199 | $1,595 |
| **AMD RX 9070 XT** | unos $830 | **más de $1,037** |

Las subidas llegaron en oleadas coordinadas durante 2026, no como picos aislados. Nvidia subió los precios en enero, otra vez en mayo para la RTX 5090 y de nuevo más adelante ese año. AMD siguió en agosto con un aumento de al menos el 10 % en algunas tarjetas Radeon y kits de memoria GDDR6, atribuido directamente al coste de la memoria.

**La generación siguiente se retrasó en vez de salir al mercado.** Ahora se espera que la serie RTX 60 de Nvidia llegue en 2028 y se salte por completo 2027. Se cita la disponibilidad de memoria como causa.

*La tarjeta que compras hoy no compite con una más barata el año que viene. Compite con una versión más cara de sí misma.*

## Por qué esperar sale más caro

El consejo habitual sobre hardware es esperar a la próxima generación. En un mercado con memoria limitada, ese consejo te perjudica.

Tres puntos lo explican.

**Los precios ya subieron y siguen aumentando.** Una subida trimestral del 90–95 % en los contratos de DRAM no es un pico que se revierta al trimestre siguiente. TrendForce prevé otra subida en el tercer trimestre, no una bajada, e Intel sitúa el alivio en 2028.

**No habrá un producto de 2027 que merezca la espera.** Si las GPU de consumo de nueva generación no llegan hasta 2028, la espera se extiende a dos años. Gran parte del ciclo de renovación del equipo se pasa esperando sin obtener nada.

**Los modelos ya son suficientemente buenos.** Esto cambió en 2026. Hace dos años, el equipo local ofrecía una experiencia claramente inferior. Hoy, con el mismo dinero, puedes ejecutar un modelo 27B a 135 tokens por segundo y contexto 262K que supera a una API de gama alta en el índice global de inteligencia.

*Si esperabas a que los modelos locales fueran buenos, ya puedes dejar de esperar. Si esperas que baje el precio del equipo, los datos de suministro apuntan a 2028.*

## Qué montar

Adaptar el equipo a los modelos anteriores es sencillo porque los pesos ternarios redujeron los requisitos de memoria.

| Nivel | Memoria | Qué ejecuta con soltura |
|---|---|---|
| **Inicial** | 8–12 GB de VRAM | Modelo ternario 27B de 5.53–6.70 GiB, con margen para el contexto |
| **Práctico** | 16–24 GB de VRAM | Qwen3.8 27B completo de 18 GB o paquete ternario con contexto largo |
| **Cómodo** | 32 GB de VRAM | Modelo ternario 27B con contexto completo 262K o MoE 80B con 3B parámetros activos |
| **Memoria unificada** | 64–128 GB | Modelos MoE dispersos más grandes en Apple Silicon o un ordenador con memoria unificada |

Algunas notas prácticas importan más que la tabla:

- **Compra memoria, no la GPU insignia.** El paquete ternario de 5.53 GiB hace que el nivel inicial sea realmente útil. Invierte la diferencia en RAM del sistema y almacenamiento, no en perseguir una tarjeta de lujo a precios de 2026.
- **Los sistemas de memoria unificada ofrecen buena relación calidad-precio.** Un equipo con 64 GB o más de memoria compartida ejecuta modelos dispersos grandes por una fracción del coste de una tarjeta dedicada de la misma capacidad.
- **La energía y la refrigeración cuentan.** Un equipo que ejecuta inferencia durante horas se comporta de otra forma que uno que realiza pruebas durante unos minutos.
- **Ejecuta el paquete ternario junto a un modelo pequeño.** Un modelo 3B responde a preguntas rápidas y el 27B se ocupa de las difíciles.

{{< centerbutton href="https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B" >}}
Descargar Ternary Bonsai 2 27B
{{< /centerbutton >}}

## Cuándo los modelos de gama alta aún justifican su precio

La gama alta tiene una ventaja real, pero más limitada de lo que sugiere el marketing.

**La respuesta sincera es la fiabilidad factual.** La precisión AA-Omniscience es del 40.9 % para Sonnet 4.6 y del 15.6 % para el modelo abierto 27B. Si una respuesta errónea cuesta un cliente, un diagnóstico o una posición legal, una diferencia de 25 puntos porcentuales importa más que cualquier índice global.

**La segunda razón son las cadenas agénticas largas.** Sonnet 4.6 obtiene el 53.0 % en Terminal-Bench Hard y el 75.7 % en τ²-Bench Telecom. Estas evaluaciones miden el uso sostenido de herramientas y el comportamiento de agentes en varios turnos. La ficha del modelo abierto no ofrece cifras comparables. Esa ausencia no tranquiliza.

**La tercera razón es operativa.** Una API alojada no exige actualizar controladores, resolver particularidades de cuantización, seguir un fork de llama.cpp ni configurar correctamente una base de pesos rotada. Otra persona se ocupa de la disponibilidad y recibe el aviso a las tres de la madrugada.

### La pregunta que conviene hacerse

¿Qué lugar tiene la gama alta fuera de las empresas?

**Sigue teniendo sentido para el trabajo que depende del conocimiento.** Investigación, análisis jurídico, consultas médicas, modelos financieros y cualquier tarea en la que una respuesta segura pero equivocada cueste caro. Es un caso real y la diferencia de precisión es una razón válida para pagar.

**Para el trabajo generativo, la justificación se debilita deprisa.** Redactar, resumir, refactorizar código, cambiar el formato de datos, clasificar documentos y ejecutar procesos automáticos son tareas cuyo resultado se revisa antes de confiar en él. La diferencia de precisión cuesta poco cuando una persona o una batería de pruebas verifica primero el resultado. Para esas cargas, cuesta justificar pagar por token por un índice de 30.1 cuando uno de 33.7 funciona gratis en equipo que ya tienes.

**La decisión ahora depende de las consecuencias, no de las capacidades.** Hace dos años se preguntaba si un modelo local podía hacer el trabajo. Hoy se pregunta cuánto cuesta un error y cómo detectarlo.

*La prima empresarial paga fiabilidad, cumplimiento y el turno de guardia de otra persona. Los demás pagan por una diferencia que deja de importar cuando una batería de pruebas verifica el resultado.*

## Puntos clave

- **Un modelo local 27B supera a Claude Sonnet 4.6 en el índice global de inteligencia**, 33.7 frente a 30.1. También lidera en programación, tareas agénticas, contexto largo y razonamiento científico avanzado.
- **Sonnet 4.6 aún gana en precisión factual**, 40.9 % frente a 15.6 % en AA-Omniscience. Es el argumento más fuerte que queda para la gama alta.
- **La cuantización ternaria vuelve práctico este resultado.** Bonsai 2 27B ejecuta el mismo modelo de 26.90B en 5.53 GiB, en vez de 18 GB. Ambos usan Apache 2.0.
- **Ollama estándar no puede ejecutar los paquetes ternarios.** Necesitan el fork de llama.cpp de Prism ML, y la alternativa F16 produce silenciosamente texto incoherente en vez de fallar.
- **La velocidad de decodificación medida es de 135 tokens por segundo** en una RTX 5090, muy superior a la velocidad de lectura.
- **El precio de la memoria es la razón para actuar ahora.** Los contratos de DRAM subieron entre el 90 y el 95 % en un trimestre de 2026 y las GPU de consumo de nueva generación se retrasaron a 2028.
- **La RTX 5090 pasó de $1,999 a más de $5,000 en menos de dos años**, y todas las gamas subieron.

## Próximos pasos

1. **Descarga el modelo y pruébalo con tu carga de trabajo**: **[Ternary Bonsai 2 27B en Ollama](https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B)**
2. **Consigue los pesos originales a precisión completa** si tienes memoria suficiente: **[Qwen3.8 en Ollama](https://ollama.com/library/qwen3.8)**
3. **Prueba el modelo antes de montar nada** mediante el endpoint alojado gratuito: **[Qwen3.8 27B gratis en OpenRouter](https://openrouter.ai/qwen/qwen3.8-27b:free)**
4. **Compáralo con la gama de pago usando los mismos prompts**: **[Claude Sonnet 4.6 en OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-4.6)**
5. **Dimensiona el equipo según el nivel que necesitas** con la tabla de memoria y compra la memoria antes que la tarjeta gráfica.
6. **Si tienes una Raspberry Pi sin uso**, mira si puede alojar algo más pequeño: **[¿Qué modelos de IA funcionan en Raspberry Pi 4 o 5?](/articles/ai-models-raspberry-pi-4-5/)**

## Artículos relacionados

| Artículo | Contenido |
|---|---|
| **[¿Qué modelos de IA funcionan en Raspberry Pi 4 o 5?](/articles/ai-models-raspberry-pi-4-5/)** | El límite inferior de la inferencia local y lo que realmente pueden manejar las placas pequeñas |
| **[Crear un asistente de IA que proteja la privacidad para Meshtastic](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | Un asistente local en equipo sin conexión, donde la privacidad no es opcional |
| **[El papel de la memoria ECC para evitar la corrupción de datos](/articles/the-role-of-ecc-memory-in-mitigating-data-corruption/)** | Por qué la calidad de la memoria importa más cuando contiene un modelo grande |
| **[Qué es un laboratorio doméstico y si deberías tener uno](/articles/what-is-a-homelab-and-should-you-have-one/)** | Planificar el espacio, la energía y la refrigeración para equipos que generan calor |

## Referencias

1. [Ternary Bonsai 2 27B - espejo del modelo en Ollama](https://ollama.com/tobestyledintro/Ternary-Bonsai-2-27B)
2. [Qwen3.8 - biblioteca de modelos de Ollama](https://ollama.com/library/qwen3.8)
3. [Qwen3.8 27B (gratis) - pruebas y precios de OpenRouter](https://openrouter.ai/qwen/qwen3.8-27b:free)
4. [Claude Sonnet 4.6 - pruebas y precios de OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-4.6)
5. [Primera prueba de Bonsai 2 27B: ¿es el MEJOR modelo de IA para una sola GPU? - Bijan Bowen](https://www.youtube.com/watch?v=OA5cICIzD-c)
6. [Artificial Analysis - evaluaciones independientes de modelos](https://artificialanalysis.ai/)
7. [TrendForce - previsiones de precios contractuales de DRAM y NAND](https://www.trendforce.com/)
8. [Los chips de memoria ya son más caros que los chips de cómputo por superficie - Tom's Hardware](https://www.tomshardware.com/pc-components/dram/dram-is-now-more-expensive-than-compute-chips-on-per-area-basis-ai-demand-drives-memory-die-value-past-leading-edge-silicon)
9. [El alivio para las GPU se retrasa hasta 2028 tras una subida récord del 95 % de la DRAM - Tech Insider](https://tech-insider.org/gpu-relief-pushed-2028-dram-price-jump-2026/)
10. [Tan, de Intel: la memoria cuesta hasta siete veces más, sin alivio hasta 2028 - shattered.io](https://shattered.io/intel-ceo-memory-shortage-no-relief-until-2028-2026/)
11. [Fork de llama.cpp de Prism ML - núcleos ternarios](https://github.com/PrismML-Eng/llama.cpp)
12. [Ternary-Bonsai-2-27B-gguf - pesos originales](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)
