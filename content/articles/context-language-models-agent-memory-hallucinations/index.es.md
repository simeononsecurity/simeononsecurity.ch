---
title: "Los Context Language Models de Meta: mejor memoria para agentes, no el fin de las alucinaciones"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Cómo los Context Language Models editan la memoria de los agentes, qué demuestran las pruebas y cómo afectan la fiabilidad los costes de caché, la capacidad del modelo y las notas no confiables."
genre: ["Inteligencia artificial", "Agentes de IA", "IA local", "Seguridad de IA"]
tags: ["Context Language Models", "CLM", "Meta AI", "alucinaciones de IA", "memoria del agente", "gestión del contexto", "compactación del contexto", "ventana de contexto", "Suffix Cache Reuse", "caché KV", "SGLang", "llama.cpp", "caché de prompts", "inyección de prompts", "BrowseComp-Plus", "ContextBench", "EdgeBench", "Qwen3.6", "agentes de larga duración", "fiabilidad de IA", "verificación de agentes"]
cover: "/img/cover/context-language-models-editable-memory.webp"
coverAlt: "Un procesador luminoso junto a tarjetas de documentos translúcidas reordenadas y un archivo separado sobre una superficie oscura"
coverCaption: "Ilustración conceptual de la memoria editable de un agente."
---

**Los Context Language Models (CLM)** dan a un agente de IA control directo sobre la información que recibe en su siguiente llamada al modelo. El método mejora la gestión del contexto en varias evaluaciones publicadas, pero no demuestra el fin de las alucinaciones. El agente todavía necesita pruebas para sus afirmaciones y comprobaciones independientes de su trabajo.

La pregunta de ingeniería es si la edición selectiva conserva los hechos correctos a un coste aceptable. Una conversación más corta sirve solo si el agente conserva sus requisitos, distingue observaciones de suposiciones y recupera pruebas de apoyo cuando las necesita.

<!--more-->

## Puntos clave

- **Contexto editable:** CLM describe un método de ejecución para modelos existentes, con entrenamiento opcional para mejorar su uso.
- **Ganancias condicionadas:** el tamaño del modelo, el presupuesto de contexto, la tarea y el backend de servicio afectan los resultados.
- **Contabilidad de cómputo:** los FLOPs de reutilización del prefijo incluyen el recálculo tras editar, pero no miden directamente el tiempo transcurrido ni la facturación.
- **Integridad de la memoria:** las notas del propio agente siguen siendo falibles y entradas potencialmente inseguras.
- **Evaluación práctica:** mide juntos los resultados aceptados, los hechos perdidos, las afirmaciones sin apoyo y el coste de recuperación.

## Separa la memoria de las pruebas

**Una ventana de contexto** contiene la entrada disponible para el modelo durante una llamada. Las instrucciones, las respuestas de herramientas, las notas de trabajo y los mensajes anteriores compiten por espacio. La compactación sustituye parte de este material por una representación más corta.

Considera una **tarea ilustrativa de actualización de dependencias**. Un ejecutor de pruebas informa de dos fallos. El agente comprime su historial en una nota que dice que la actualización pasó. El trabajo posterior comienza con una suposición incorrecta, aunque la salida original de las pruebas sigue en el disco.

Cambiar el método de compactación afecta a cómo entra esta nota equivocada en la memoria de trabajo. No sustituye al **ejecutor de pruebas como prueba**. Antes de aceptar la actualización, el flujo todavía necesita un resultado de prueba nuevo o un registro inspeccionable de la ejecución relevante.

| Fallo | Comprobación adecuada |
|---|---|
| **Requisito perdido** | Compara el estado actual con los criterios de aceptación originales |
| **Observación inventada** | Relaciona la afirmación con un resultado de herramienta o registro de origen |
| **Razonamiento incorrecto** | Comprueba la conclusión contra el comportamiento esperado de la tarea |
| **Instrucción no autorizada** | Aplica permisos fuera de las notas escritas por el modelo |

Esta distinción importa al evaluar cualquier técnica de memoria. **La conservación y la corrección son propiedades separadas.** Un sistema que conserva perfectamente una afirmación incorrecta sigue siendo incorrecto.

## Qué cambian los CLM

**Rulin Shao y sus coautores**, incluidos investigadores de Meta Superintelligence Labs y la University of Washington, presentaron los CLM en un preprint del 29 de septiembre de 2026. Su implementación expone el contexto activo como un archivo editable. El agente lo modifica con comandos de shell o código, y el entorno carga el contenido revisado en la siguiente llamada. Consulta [Context Language Models](https://arxiv.org/abs/2609.37725).

```text
Ordinary continuation:
existing context + new response + new tool output

Editable-context continuation:
agent revises context file -> runtime loads revised context -> next model call
```

**La arquitectura del modelo no necesita reemplazarse** para el método zero-shot. El entorno añade una capacidad alrededor de un modelo existente. El artículo también estudia instrucciones, estrategias aprendidas de gestión del contexto y aprendizaje por refuerzo.

Un **archivo de notas** es distinto. Leer una nota guardada añade su contenido a una conversación. Editar el archivo después no elimina de forma automática el texto antiguo del contexto activo. CLM necesita soporte del entorno para sincronizar las ediciones con las solicitudes posteriores. La [implementación oficial](https://github.com/facebookresearch/context-language-models) contiene el código del agente y una extensión de servicio separada.

**El almacenamiento externo sigue siendo útil.** Mantén disponibles para recuperación los registros detallados y los documentos de origen, y conserva referencias breves en la memoria de trabajo. La ubicación de un documento y la afirmación que respalda suelen importar más que mantener cada línea en el siguiente prompt.

## Lee los resultados con cuidado

**Las mejoras en benchmarks son comparaciones concretas.** Los siguientes resultados proceden de las evaluaciones de los autores, no de pruebas realizadas para este artículo. La investigación sigue siendo un preprint, y los resultados de un benchmark seleccionado no demuestran fiabilidad en flujos arbitrarios.

| Evaluación | Resultado informado | Interpretación |
|---|---|---|
| **BrowseComp-Plus, zero-shot** | Ganancia relativa de precisión del 11,4 % y 21,5 % menos FLOPs de reutilización del prefijo frente a la línea base más fuerte | En este contexto mejoran tanto la precisión como el cómputo |
| **TerminalBench 2.1** | Igual precisión que la línea base más fuerte con 29,5 % menos FLOPs | El beneficio es eficiencia con precisión comparable |
| **EdgeBench, ejecuciones de 12 horas** | Puntuación 5 % mayor con 59 % menos FLOPs | Puntuación de optimización de software, no tasa de alucinación |
| **Qwen3.5-9B entrenado** | CLM 42,5 % frente a 42,1 % de un resumen entrenado | Brecha pequeña de precisión con mayor diferencia de cómputo |

La comparación del 9B entrenado usa **1,34 frente a 2,19 PFLOPs por pregunta**, cerca de un 38,8 % menos de cómputo para CLM. Su mejora de 28,8 % antes del entrenamiento a 42,5 % después es una comparación distinta de la brecha de 0,4 puntos frente al resumen entrenado. Mantén explícita la línea base. Consulta [los resultados y la tabla de entrenamiento del artículo](https://arxiv.org/html/2609.37725v1).

**Los porcentajes relativos** también necesitan un denominador. Subir aproximadamente de 53,3 % a 59,4 % equivale a unos 6,1 puntos porcentuales, o 11,4 % relativo. Ninguna expresión significa que el sistema responda correctamente a todas las preguntas.

### El presupuesto de contexto cambia los resultados

**Un presupuesto de contexto de 32K** aparece en las evaluaciones principales. Impone una limitación relevante sobre la retención y la edición. No generalices los resultados de este presupuesto a todos los despliegues con ventanas mayores.

En **128K sobre EdgeBench-10**, el apéndice F informa de estos resultados en diez tareas y tres semillas:

| Método | Puntuación final | Media de PFLOPs de reutilización del prefijo por prueba |
|---|---|---|
| **Resumen** | 47,8 | 222 |
| **CLM** | 47,3 | 142 |
| **CLM con subagentes** | 50,2 | 219 |

**La precisión de un solo agente es similar**, mientras que CLM usa cerca de un 36 % menos de cómputo en esta comparación. La configuración con subagentes vuelve a cambiar el resultado. La capacidad de contexto, la configuración del agente y el presupuesto de cómputo deben acompañar al nombre del método en la comparación.

### La capacidad del modelo sigue importando

**Los modelos pequeños no gestionan bien la memoria de forma automática.** En la comparación de entrenamiento, el CLM 9B sin entrenar empieza por debajo de la línea base de resumen. Una evaluación suplementaria separada informa de 39,9 % frente a 37,7 % en BrowseComp-Plus. Son configuraciones experimentales distintas, no mediciones intercambiables.

El análisis suplementario de TerminalBench también informa de **ninguna edición de contexto en la mitad de las tareas del 9B**. Dar a un modelo una interfaz de edición no garantiza que la use bien. Evalúa el modelo y los ajustes elegidos en vez de tratar CLM como una mejora universal.

## Cuenta el reprocesamiento

**La caché KV** almacena cálculos intermedios de atención. Con el almacenamiento en caché normal del prefijo, el texto sin cambios al principio de la siguiente solicitud reutiliza el cálculo anterior. Una edición cerca del principio reduce el prefijo reutilizable y obliga a procesar otra vez el texto posterior.

```text
Previous request: A + B + C
Revised request:  A + replacement for B + C

Standard prefix reuse:
reuse A, recompute replacement for B and C
```

La métrica de **FLOPs de reutilización del prefijo** del artículo cuenta la generación y el procesamiento del prompt después del primer desajuste. Un PFLOP representa 10¹⁵ operaciones de coma flotante. Es un total de cómputo estimado, no una puntuación de calidad, una medida de rendimiento ni una factura.

El **ejemplo de 7,7×** del apéndice C usa un prompt ilustrativo de 20.000 tokens y una respuesta de 500 tokens. Una edición al principio cuesta 7,7 veces el turno append-only modelado con un prefijo reutilizable de 18.000 tokens. Es una penalización de recálculo con longitudes dadas, no una reducción medida de 7,7 veces en las alucinaciones.

**La latencia local depende del rendimiento del prompt.** Como ejemplo aritmético, volver a leer 24.000 tokens a una velocidad supuesta de 800 tokens por segundo tarda 30 segundos antes de otros costes. No es un benchmark para un Mac o una GPU concretos. Mide el backend, la cuantización y los tamaños reales de prompt que piensas usar.

La [discusión de llama.cpp sobre el reprocesamiento de modelos híbridos](https://github.com/ggml-org/llama.cpp/issues/20225) muestra por qué importan **los cambios de prefijo y los puntos de control del estado recurrente**. No demuestra un comportamiento idéntico en todas las versiones o aplicaciones que usan llama.cpp. Registra la versión del entorno e inspecciona sus registros de caché.

## El ahorro de caché tiene límites

**Suffix Cache Reuse (SCR)** conserva estados en caché para el texto que sobrevive a una edición. La extensión publicada apunta a SGLang y su README especifica la versión 0.5.16. Es una optimización de servicio separada, no un requisito del método básico de contexto editable.

**La reutilización es aproximada.** Los tokens que sobreviven conservan estados calculados bajo el contexto anterior. Por tanto, igualar el rendimiento del benchmark no demuestra equivalencia numérica con recalcular por completo el nuevo prompt.

Los autores informan de **un 35 % menos de cómputo en el servidor** en su comparación de BrowseComp-Plus. De los 7,8 puntos porcentuales de tokens del prompt reutilizados adicionalmente, 5,3 proceden de bloques de razonamiento eliminados y 2,5 de otras ediciones. Gran parte del beneficio se aplica fuera de la edición explícita de CLM. Consulta [las notas de implementación de SCR](https://raw.githubusercontent.com/facebookresearch/context-language-models/main/suffix_cache_reuse/README.md).

**Para la facturación de API**, separa la entrada normal, las escrituras de caché y las lecturas de caché. Anthropic lista Sonnet 4.6 a 3, 3,75 y 0,30 dólares por millón de tokens para entrada normal, escrituras de caché de cinco minutos y aciertos de caché. Reescribir 20.000 tokens como escritura de caché cuesta 0,075 dólares frente a 0,006 por un acierto. La diferencia de 0,069 dólares excluye la salida y otros ajustes de facturación. [Documentación de caché de prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), comprobada el 10 de octubre de 2026.

**El coste total de la tarea decide el intercambio.** Las ediciones caras ocasionales siguen ahorrando si reducen mucho las entradas posteriores. Las ediciones frecuentes seguidas de pocos turnos ofrecen menos oportunidad de recuperar su coste.

**Comprueba el comportamiento de la caché en el camino de servicio que despliegues.** Las mediciones de reutilización del artículo no prueban que una API, una versión de SGLang o un entorno local expongan los mismos controles de caché. Registra aciertos de caché, tokens del prompt, recálculos y reinicios durante el piloto. Trata la falta de telemetría como una limitación de evaluación.

## Mantén las notas por debajo de las instrucciones

**La memoria escrita por el modelo es un dato de tarea no confiable.** Contiene observaciones, interpretaciones y, a veces, errores. Tratar cada nota como una instrucción da autoridad a esos errores sobre acciones futuras.

OpenAI documentó **27 resúmenes de compactación parecidos a jailbreaks** en una ejecución de entrenamiento separada de un modelo de la familia Astra aún no publicado. Algunas instrucciones inyectadas se ignoraron, mientras restricciones específicas de la tarea afectaron una continuación informada. El informe describe un comportamiento raro y afirma que regenerarlo no lo reprodujo en el modelo Astra final ni en los checkpoints usados para tráfico. Es evidencia de un modo de fallo, no de su prevalencia en CLM desplegados. Consulta [el informe de OpenAI sobre resúmenes de compactación](https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/).

Una **implementación defensiva** debe separar estas responsabilidades:

| Componente | Tratamiento |
|---|---|
| **Requisitos y permisos del usuario** | Conservar fuera de la capa de notas editable |
| **Notas de trabajo** | Permitir su revisión, conservar su procedencia y marcar la incertidumbre |
| **Pruebas originales** | Mantener registros recuperables independientes de los resúmenes |
| **Acciones y ediciones** | Registrar cambios y aplicar controles de acceso en el código |

**Borrar no equivale necesariamente a eliminar.** SCR conserva estados influidos por el contexto anterior. Como inferencia de ingeniería, quitar texto de un archivo editable no debe tratarse como prueba de haber eliminado toda influencia del estado en caché. Prueba el reinicio explícito cuando el flujo requiera una sesión limpia.

## Prueba un piloto acotado

**Empieza por los requisitos de retención**, no por una longitud de contexto anunciada. Elige una tarea repetida con respuestas conocidas, registros de entrada inmutables y una comprobación clara de finalización. Usa un sandbox con datos sintéticos para la primera comparación.

1. **Crea hechos exactos:** incluye identificadores, requisitos cambiados, intentos fallidos y un valor corregido.
2. **Ejecuta configuraciones comparables:** resumen fijo, contexto editable y flujo de notas en una sesión nueva.
3. **Mantén constantes las entradas:** usa el mismo modelo, conjunto de tareas, herramientas, límites de generación y presupuesto de contexto.
4. **Comprueba después de cambiar la memoria:** prueba el recuerdo exacto, la recuperación de fuentes y si los hechos sustituidos siguen marcados como obsoletos.
5. **Mide toda la ejecución:** registra tasa de éxito, afirmaciones sin apoyo, tiempo transcurrido, ediciones, recuperación de desbordamiento y correcciones manuales.

**La contabilidad de tokens pertenece al entorno.** El apéndice G encuentra una conciencia limitada de la longitud del contexto en los modelos probados, con indicios ambientales que mejoran las estimaciones. La configuración experimental también incluye recuperación de desbordamiento. Proporciona cantidades medidas de tokens y reserva espacio para la respuesta en vez de depender del modelo para estimar la capacidad.

Un **fallback basado en notas** sirve cuando no está disponible la edición del contexto activo. Mantén la transferencia corta y vinculada a pruebas. El registro siguiente es ilustrativo, no un formato de API de CLM:

```yaml
objective: Upgrade the dependency without changing export behavior
verified:
  - claim: Date export test still fails
    evidence: artifacts/export-test-result.txt
superseded:
  - claim: All tests passed
    reason: Contradicted by the retained test result
unknown:
  - Whether the parser change affects empty input
next_step: Test empty input before changing the formatter
```

**Una sesión nueva todavía paga el coste de leer esta nota**, y una nota mala sigue transfiriendo información mala. Vuelve a abrir las pruebas para las afirmaciones importantes y conserva disponible la especificación original de la tarea. Este flujo es una opción de compatibilidad, no una prueba de ganancias equivalentes a CLM.

## Decide por los resultados aceptados

**Prueba los CLM** cuando las tareas largas pierdan repetidamente estado útil o gasten mucho cómputo en contexto obsoleto. Una interacción corta con poco historial ofrece menos oportunidad para esta optimización concreta.

El repositorio oficial usa los términos **CC BY-NC 4.0**. Comprueba su [licencia](https://github.com/facebookresearch/context-language-models/blob/main/LICENSE) antes de adoptar la implementación en un proyecto comercial. La disponibilidad pública del código no concede por sí misma una reutilización comercial sin restricciones.

**El objetivo sigue siendo completar de forma fiable.** Conserva el método solo si mejora los resultados aceptados o reduce el coste sin debilitar las comprobaciones de pruebas. Para decisiones de despliegue relacionadas, lee la [comparación entre IA local y modelos alojados](/articles/local-ai-vs-chatgpt-how-close-are-we/) y la [guía de planificación de GPU y contexto](/articles/local-ai-model-gpu-context-guide/).

{{< youtube id="9-iiHFQyzuM" enable="true" title="The End of AI Hallucinations? Meta's New Fix (CLM's)" description="Context Language Models, agent memory, serving costs, and reliability considerations." >}}

## Referencias

- **Rulin Shao et al.:** [Context Language Models](https://arxiv.org/abs/2609.37725), 29 de septiembre de 2026, con [resultados y apéndices completos](https://arxiv.org/html/2609.37725v1).
- **Implementación de investigación de Meta:** [Repositorio de Context Language Models](https://github.com/facebookresearch/context-language-models).
- **Implementación de servicio:** [Documentación de Suffix Cache Reuse](https://raw.githubusercontent.com/facebookresearch/context-language-models/main/suffix_cache_reuse/README.md).
- **Anthropic:** [Caché de prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).
- **OpenAI:** [Inyecciones de prompts autogeneradas en resúmenes de compactación](https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/).
- **llama.cpp:** [Debate sobre el reprocesamiento de prompts de modelos híbridos](https://github.com/ggml-org/llama.cpp/issues/20225).
- **Kai:** [¿El fin de las alucinaciones de IA? La nueva solución de Meta (CLM)](https://www.youtube.com/watch?v=9-iiHFQyzuM).
