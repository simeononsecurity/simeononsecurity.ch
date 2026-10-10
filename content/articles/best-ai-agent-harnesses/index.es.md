---
title: "Los mejores harnesses de agentes de IA en 2026: elige según el flujo de trabajo"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Compara Deep Agents, Claude Agent SDK, OpenAI Agents SDK, Pydantic AI, Pi y LangGraph según la ejecución de herramientas, la memoria, la recuperación y el esfuerzo de integración."
genre: ["Inteligencia artificial", "Desarrollo de software", "Seguridad de IA"]
tags: ["harnesses de agentes de IA", "mejores frameworks de agentes", "Deep Agents", "Claude Agent SDK", "OpenAI Agents SDK", "Pydantic AI", "agente de programación Pi", "LangGraph", "runtime de agentes", "llamadas a herramientas", "memoria de agentes", "gestión del contexto", "ejecución durable", "permisos de agentes", "seguridad de agentes de IA", "agentes de IA locales", "evaluación de agentes", "humano en el circuito", "comparación de SDK de agentes", "agentes de producción"]
cover: "/img/cover/ai-agent-execution-components.webp"
coverAlt: "Componentes metálicos modulares conectados a un procesador central brillante mediante rutas turquesa y naranja sobre una superficie de trabajo oscura"
coverCaption: "Ilustración conceptual de los componentes que rodean un modelo de IA."
---

**Deep Agents es mi primera opción para un agente general con modelos configurables y gestión de contexto integrada.** Claude Agent SDK encaja bien para insertar el comportamiento de ejecución de Claude Code. OpenAI Agents SDK y Pydantic AI merecen una prueba para agentes específicos de una aplicación. Pi prefiere un núcleo pequeño y extensible, mientras LangGraph prefiere un control explícito del flujo de trabajo.

**La mejor opción depende del trabajo que pretendas aceptar.** Un asistente de investigación, un editor de repositorios y un servicio que procese solicitudes de clientes necesitan herramientas y reglas de recuperación distintas. Estas recomendaciones son juicios editoriales basados en documentación oficial revisada el **10 de octubre de 2026**, no resultados de un benchmark práctico de rendimiento.

<!--more-->

## Puntos clave

- **Elige primero la abstracción:** agente ensamblado, SDK de aplicación o runtime de flujo de trabajo.
- **Comprueba los límites de ejecución:** la aprobación de herramientas, el aislamiento del sistema de archivos y la política de red resuelven problemas distintos.
- **Prueba la recuperación:** el historial de conversación por sí solo no evita acciones externas duplicadas.
- **Mide el trabajo aceptado:** incluye fallos, tiempo de revisión e infraestructura en la comparación de costes.
- **Mantén explícito el modelo:** cambiar el modelo y el software del agente prueba el sistema completo, no solo el software.

## Qué proporciona un harness

Un **harness de agente es el software que rodea una llamada al modelo.** Prepara el contexto, expone herramientas, ejecuta acciones aprobadas, devuelve resultados y decide cuándo continuar o detenerse. Según la implementación, también gestiona memoria, delegación, permisos y recuperación.

Un **modelo** propone la siguiente acción. Una **herramienta** realiza una operación. Un **runtime** ejecuta y conserva el flujo de trabajo. Estas responsabilidades se solapan en los productos empaquetados, pero separarlas ayuda a identificar capacidades ausentes.

| Componente | Pregunta que debes hacer |
|---|---|
| **Gestión del contexto** | ¿Qué requisitos sobreviven a una ejecución larga? |
| **Ejecución de herramientas** | ¿Quién valida los argumentos y limita la autoridad? |
| **Almacenamiento del estado** | ¿Qué sobrevive al reinicio del proceso? |
| **Verificación** | ¿Qué evidencia confirma que se completó? |

Considera un **agente de soporte ilustrativo** al que se le pide inspeccionar un pedido y preparar una solicitud de reemplazo. Leer el pedido, proponer el reemplazo y enviarlo deben tener autoridades separadas. Una explicación convincente no demuestra permiso para enviarlo, y una transcripción guardada no demuestra si el envío ya ocurrió.

**Alcance:** esta guía compara software y runtimes integrables. Para interfaces de desarrollo diarias, usa la [comparación de agentes de programación CLI](/articles/cli-coding-agents-comparison/) o la [comparación de agentes de programación GUI](/articles/gui-coding-agents-comparison/). Una comparación de SDK no debe convertirse en silencio en una clasificación de herramientas de terminal frente a extensiones de editor.

## La lista corta práctica

| Requisito inicial | Primera opción que debes evaluar | Responsabilidad principal que conservas |
|---|---|---|
| **Agente general** | Deep Agents | Configurar backend, permisos y modelo |
| **Claude Code en una aplicación** | Claude Agent SDK | Operar y aislar el proceso de ejecución |
| **Flujo de herramientas de una aplicación** | OpenAI Agents SDK | Definir herramientas, aprobaciones y aceptación |
| **Aplicación Python tipada** | Pydantic AI y su paquete Harness | Seleccionar capacidades y espacio de trabajo |
| **Núcleo de programación integrable y mínimo** | Pi SDK | Ensamblar extensiones y política de ejecución |
| **Flujo durable explícito** | LangGraph | Diseñar el estado del grafo y el comportamiento de recuperación |

**Son puntos de partida diferentes.** Deep Agents ya utiliza LangGraph, por lo que elegirlo no es necesariamente una decisión excluyente. Pydantic AI también separa su framework central de agentes de las capacidades ensambladas del harness. Compara la cantidad de código de aplicación que tendrás que mantener, en lugar de tratar cada fila como una biblioteca intercambiable.

**Empieza por la capa más pequeña que cumpla la prueba de aceptación.** Usa un framework de aplicación tipado para llamadas de herramientas acotadas, un agente ensamblado para trabajo abierto con archivos o investigación, y un grafo explícito cuando la recuperación y las transiciones necesiten estados con nombre. Añade memoria, acceso a shell o subagentes solo después de que una prueba muestre por qué falla la capa sencilla.

## Deep Agents: capacidades ensambladas

**Elige Deep Agents primero para un agente que trabaje con archivos, herramientas y conversaciones largas.** Su [descripción oficial](https://docs.langchain.com/oss/python/deepagents/overview) documenta backends de sistema de archivos, descarga de contexto, resúmenes, subagentes y aprobación humana. Se basa en LangChain y en el runtime de LangGraph, con integraciones para varios proveedores de modelos.

**La configuración sigue determinando el comportamiento.** La documentación actual indica que la planificación de tareas es opt-in desde la versión 0.7. No asumas que un tutorial de una versión anterior describe los valores predeterminados actuales. Registra la versión del paquete y el middleware activado en tu evaluación.

**Inspecciona con cuidado el alcance de los permisos.** Las reglas documentadas del sistema de archivos cubren las herramientas de archivos integradas, pero no comandos shell arbitrarios mediante backends sandbox. Denegar una herramienta de archivos no basta si otra ruta de ejecución llega al mismo archivo. Prueba el backend y el límite del shell juntos.

**Mi recomendación:** inclúyelo en la lista corta para un servicio de análisis de documentos o repositorios cuando quieras capacidades ensambladas y elección de proveedor. Prefiere un punto de partida menor cuando el trabajo consista en dos llamadas API definidas y una respuesta validada. Las herramientas adicionales introducen más comportamiento que evaluar.

## Claude: ejecución integrada

**Elige Claude Agent SDK cuando quieras el agente de Claude Code dentro de tu aplicación.** Anthropic describe una biblioteca de Python y TypeScript que usa el mismo bucle de ejecución, herramientas y gestión de contexto que Claude Code. El SDK ejecuta el binario de Claude Code en un proceso que tú operas. Es distinto del cliente API básico de Anthropic y de los Managed Agents alojados. [Descripción general de Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview).

**El atractivo es reutilizar un sistema de ejecución existente.** Las operaciones de archivos, comandos, hooks, permisos, sesiones y subagentes llegan como capacidades documentadas. Tu integración proporciona el límite de la aplicación y las comprobaciones de aceptación específicas de la tarea.

**El alojamiento sigue siendo una decisión de ingeniería.** La [guía de despliegue de Anthropic](https://code.claude.com/docs/en/agent-sdk/secure-deployment) trata los controles del sistema de archivos, las restricciones de red y el aislamiento. Configúralos alrededor del proceso en lugar de tratar una solicitud de permiso como un límite del sistema operativo.

**Mi recomendación:** evalúalo para automatización de documentos o código centrada en Claude con mucho trabajo de archivos y comandos. Elige una alternativa flexible con el proveedor si comparar modelos locales y varios proveedores alojados es un requisito central del producto.

| Opción ensamblada | Enfoque de integración |
|---|---|
| **Deep Agents** | Selección de modelo, middleware y configuración del backend |
| **Claude Agent SDK** | Ejecución de Claude Code dentro de un proceso de aplicación |

## OpenAI: flujos de herramientas para aplicaciones

**Elige OpenAI Agents SDK para una aplicación organizada alrededor de funciones, tareas delegadas y salidas explícitas.** Su [descripción general](https://openai.github.io/openai-agents-python/) documenta el bucle del agente, los handoffs, los guardrails, el tracing y las capacidades de sandbox-agent. El SDK es una interfaz para desarrolladores, distinta de la aplicación de desarrollo Codex.

**La aprobación es un comportamiento configurable.** La [guía human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/) describe ejecuciones interrumpidas y estado serializado para reanudar después de una decisión. Para herramientas locales de shell y patch, la aprobación es opt-in. Añadir solo un callback de aprobación no activa el requisito de aprobación.

**La compatibilidad de modelos se extiende más allá de OpenAI.** La [documentación de proveedores](https://openai.github.io/openai-agents-python/models/) describe puntos de integración y adaptadores para proveedores externos. Valida las salidas estructuradas, las llamadas a herramientas y el soporte de transporte para tu endpoint. No supongas paridad de funciones.

**Mi recomendación:** inclúyelo en la lista corta para un servicio cuyas acciones útiles ya existan como funciones de aplicación bien definidas. Por ejemplo, recupera un pedido, calcula la elegibilidad con código normal y prepara una solicitud estructurada. Mantén la autorización y las comprobaciones de elegibilidad en la aplicación aunque el modelo seleccione la siguiente herramienta.

## Pydantic AI: aplicaciones tipadas

**Elige Pydantic AI cuando los tipos de Python y las salidas validadas sean centrales para tu aplicación.** Su [documentación principal](https://pydantic.dev/docs/ai/overview/) cubre herramientas tipadas, inyección de dependencias, salidas estructuradas e integraciones de ejecución durable. La validación establece la estructura requerida de la salida. No establece la veracidad de cada campo.

**El paquete Harness separado añade capacidades ensambladas.** Su [documentación](https://pydantic.dev/docs/ai/harness/) incluye las pilas Coder y Researcher, acceso a archivos y shell, memoria e integraciones con espacios de trabajo. Un espacio de trabajo local y un sandbox aislado son opciones de ejecución diferentes. Las capacidades de harness pertinentes requieren un espacio de trabajo en lugar de seleccionar uno en silencio.

**Mi recomendación:** incluye el framework central en la lista corta para un servicio Python que devuelva registros tipados. Añade capacidades de harness cuando la tarea también necesite explorar el espacio de trabajo o realizar investigación abierta. Así, un servicio de extracción acotado no hereda acceso a shell sin una necesidad concreta.

Para un **agente ilustrativo de revisión de facturas**, la validación del esquema comprueba si un total es numérico y si una moneda pertenece a un conjunto permitido. La lógica separada de la aplicación compara el total con las líneas y verifica la evidencia de origen. Ambas comprobaciones deben formar parte de la prueba.

| Aspecto de la aplicación | Prueba de aceptación |
|---|---|
| **Salida estructurada** | Valida los campos y verifica su significado de forma independiente |
| **Pausa de aprobación** | Persiste la acción pendiente exacta y la decisión |
| **Cambio de proveedor** | Repite las pruebas de compatibilidad de llamadas y salidas |

## Pi: núcleo pequeño y extensible

**Elige el SDK de Pi cuando quieras control directo sobre una implementación compacta de un agente de programación.** La [documentación del proyecto](https://github.com/earendil-works/pi/tree/main/packages/coding-agent) describe la integración de SDK y RPC junto con su interfaz interactiva. Su conjunto de herramientas predeterminado incluye lectura, escritura, edición y ejecución shell, con extensiones para comportamiento adicional.

**El minimalismo traslada trabajo al integrador.** Pi omite de forma deliberada las ventanas de permisos integradas y la orquestación de subagentes. Su documentación dirige a los usuarios hacia contenedores o extensiones personalizadas para los flujos de confirmación. Evalúa aquí el SDK integrado, no su interfaz de terminal frente al editor gráfico de otro proveedor.

**Mi recomendación:** incluye Pi en la lista corta para un servicio de programación a medida si estás dispuesto a asumir las restricciones de ejecución, la revisión de extensiones y la política de recuperación. Su núcleo pequeño facilita entender y cambiar el comportamiento. Es un punto de partida menos adecuado cuando el requisito principal es un sistema de aprobación y orquestación ya ensamblado.

## LangGraph: control explícito del flujo

**Elige LangGraph cuando el propio flujo de trabajo necesite estados y transiciones explícitos.** Su [documentación de persistencia](https://docs.langchain.com/oss/python/langgraph/persistence) distingue los checkpoints ligados a un hilo de los stores entre hilos. Un checkpointer persistente permite recuperarse tras reinicios del proceso. Uno en memoria no lo permite.

**LangGraph es una base de runtime.** Tú defines el flujo de trabajo y decides dónde encaja el comportamiento guiado por el modelo. Deep Agents ya utiliza esta base, por lo que pasar a LangGraph tiene sentido cuando necesitas un control más directo sobre las rutas de ejecución.

**Mi recomendación:** inclúyelo en la lista corta para un proceso con etapas con nombre, pausas de revisión y reglas de recuperación distintas. Un flujo de entrada de documentos podría extraer campos, validarlos, solicitar revisión y publicar un registro aprobado. Las transiciones fijas sirven cuando el modelo debe elegir el contenido, pero no inventar el proceso empresarial.

| Etapa del flujo | Evidencia de finalización |
|---|---|
| **Extraer** | Registro candidato vinculado a la fuente |
| **Validar** | Comprobaciones deterministas y excepciones |
| **Revisar** | Decisión adjunta al candidato concreto |
| **Publicar** | Recibo externo registrado contra la operación |

**Los efectos externos necesitan su propio diseño de recuperación.** Guardar el estado del grafo no vuelve atómica una transacción de un servicio remoto con el checkpoint. Usa un identificador de operación y reconcilia el resultado externo antes de repetir un envío.

## Prueba las piezas que faltan

**Una lista de funciones es solo un punto de partida.** Ejecuta cada candidato frente a fallos parecidos a tu carga de trabajo. Usa un espacio de trabajo desechable y prueba los servicios con registros sintéticos.

| Prueba | Evidencia que debes conservar |
|---|---|
| **Envío interrumpido** | Un efecto externo después de la recuperación |
| **Conversación larga** | Los requisitos originales siguen satisfechos |
| **Acción rechazada** | Ningún efecto mediante una herramienta alternativa |
| **Instrucción no fiable en un documento** | El texto del documento no adquiere autoridad |
| **Argumentos de herramienta mal formados** | Rechazo antes de modificar la aplicación |
| **Agotamiento del presupuesto** | Parada limitada con trabajo parcial inspeccionable |

**Define la repetición de forma explícita.** En un servicio de solicitudes de reemplazo, detén el worker después de que el servicio de prueba acepte una solicitud, pero antes de guardar la finalización local. Al reiniciar, el flujo debe buscar el identificador de operación en lugar de enviar de nuevo a ciegas. Es una prueba propuesta, no un resultado observado de los productos mencionados.

**Comprueba la evidencia después de la compactación.** Coloca un requisito importante al principio de la tarea y después proporciona material realista suficiente para activar la estrategia de contexto configurada. Pide al agente el artefacto final y las referencias de las fuentes. Nuestro [análisis de CLM y memoria de agentes](/articles/context-language-models-agent-memory-hallucinations/) explica por qué conservar notas y conservar evidencia exacta son cuestiones distintas.

**Revisa los destinos de la telemetría.** Las trazas de herramientas y los almacenes de memoria suelen contener datos de tareas. Registra qué sistemas los reciben y durante cuánto tiempo permanecen disponibles. La inferencia con un modelo local no implica registro, recuperación o ejecución exclusivamente locales.

## Compara el coste por tarea aceptada

**Usa dos vías de evaluación.** Una comparación controlada mantiene constantes el modelo, las herramientas, el conjunto de tareas y los presupuestos cuando existe soporte. Una comparación de despliegue utiliza la configuración prevista para cada candidato. La primera aísla algunos efectos del software. La segunda responde qué configuración completa sirve mejor a tu trabajo.

**No fuerces configuraciones no compatibles en la vía controlada.** Si dos candidatos no tienen un modelo o interfaz de herramientas común, informa de la comparación como una evaluación del sistema. Mantén en el registro el esfuerzo de configuración y la dirección humana.

```yaml
# Illustrative trial record, not a framework configuration file
candidate: "package and pinned version"
model: "provider and exact model identifier"
workspace: "isolated test environment"
task_set: "frozen fixtures and acceptance checks"
limits:
  elapsed_minutes: 15
  model_calls: 30
  tool_calls: 60
record:
  - accepted_result
  - unsupported_claims
  - duplicate_external_actions
  - inference_cost
  - infrastructure_cost
  - human_review_minutes
  - recovery_outcome
```

**Ejecuta varias pruebas por tarea.** Mantén los intentos fallidos en el denominador e informa de los recuentos brutos junto a los porcentajes. Una prueba pequeña revela patrones de fallo, no una clasificación estable de la industria.

**Cálculo de costes ilustrativo:** supón que la configuración A gasta 12 dólares en diez intentos y produce ocho resultados aceptados. Su coste de inferencia por tarea aceptada es de 1,50 dólares. La configuración B gasta 8 dólares, pero produce cuatro resultados aceptados, por lo que su coste correspondiente es de 2,00 dólares. Ninguna cifra incluye revisión humana o infraestructura. Ambos elementos pertenecen a un total registrado por separado.

**Define los fallos descalificadores antes de probar.** Un envío no autorizado o una filtración de datos entre usuarios no debe desaparecer dentro de una puntuación media de calidad. Después de imponer estos requisitos, compara corrección, recuperación, esfuerzo de revisión y coste.

## Toma una decisión acotada

**Empieza con dos candidatos y un flujo de trabajo real.** Para un agente ensamblado y flexible con el proveedor, compara Deep Agents con una alternativa más limitada adecuada para tu aplicación. Para el comportamiento de Claude Code dentro de un servicio, prueba Claude Agent SDK. Para trabajo de aplicaciones tipadas, compara Pydantic AI con OpenAI Agents SDK. Elige Pi cuando el comportamiento personalizado justifique más trabajo de integración, y LangGraph cuando el control explícito del flujo sea la prioridad.

**Requisitos previos de la prueba:** acceso aprobado al modelo, fixtures sintéticas, un espacio de trabajo aislado cuando sea necesario y criterios de aceptación escritos. Reserva una primera tarde para la configuración y las pruebas básicas de fallos. Después recoge ejecuciones repetidas antes de tomar una decisión de producción. La dificultad es intermedia o avanzada según las acciones externas y los requisitos de recuperación.

**Selecciona el sistema más pequeño que cumpla tus requisitos.** Conserva las fixtures de prueba, las versiones de los paquetes y los registros de fallos. Repítelos cuando cambies el modelo, la estrategia de contexto, las herramientas o el backend de ejecución. Esos cambios modifican el sistema evaluado.

## Referencias

- [LangChain: descripción general de Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview)
- [Anthropic: descripción general de Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)
- [Anthropic: despliegue seguro](https://code.claude.com/docs/en/agent-sdk/secure-deployment)
- [OpenAI: Agents SDK](https://openai.github.io/openai-agents-python/)
- [OpenAI: ejecución human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/)
- [OpenAI: integración de modelos y proveedores](https://openai.github.io/openai-agents-python/models/)
- [Pydantic: descripción general del framework de IA](https://pydantic.dev/docs/ai/overview/)
- [Pydantic: AI Harness](https://pydantic.dev/docs/ai/harness/)
- [Earendil: SDK del agente de programación Pi y modos de integración](https://github.com/earendil-works/pi/tree/main/packages/coding-agent)
- [LangChain: persistencia de LangGraph](https://docs.langchain.com/oss/python/langgraph/persistence)
