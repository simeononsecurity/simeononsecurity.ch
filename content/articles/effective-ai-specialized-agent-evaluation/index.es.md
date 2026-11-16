---
title: "OpenClaw y Hermes Agent: una evaluación práctica"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Evalúa agentes de IA especializados y persistentes con un inventario de accesos, una revisión de activadores, un registro de flujo de datos y una decisión sobre el piloto."
genre: ["Inteligencia artificial", "Ingeniería de software", "Productividad"]
tags: ["agentes de IA especializados", "OpenClaw", "Hermes Agent", "agentes trabajadores", "evaluación de agentes de IA", "agentes de IA persistentes"]
cover: "/img/cover/effective-ai-specialized-agent-evaluation.webp"
coverAlt: "Hoja de trabajo que enumera las herramientas, la memoria almacenada, los activadores, los registros y la decisión de revisión de un agente"
coverCaption: ""
---

[Volver al Curso práctico de flujos de trabajo con IA](/effective-ai-course-start/)

**Elige un agente especializado según la tarea y los accesos que necesita.** Un agente trabajador que revisa un archivo difiere de un sistema persistente que recibe mensajes, guarda memoria y ejecuta acciones programadas. Esta lección opcional usa OpenClaw y Hermes Agent como ejemplos y después ofrece una hoja de evaluación previa a la instalación.

**Objetivo de aprendizaje:** compararás los accesos y activadores de un agente y registrarás una decisión para una prueba piloto limitada.

## Ideas clave

- **Agente trabajador con función acotada:** agente asignado a una pregunta o artefacto concreto.
- **Agente persistente:** servicio o sesión que conserva estado o responde a activadores posteriores.
- **Activador:** evento, mensaje o programación que inicia el trabajo.
- **Inventario de accesos:** lista de herramientas, cuentas, archivos y permisos de escritura que recibe el agente.
- **Decisión sobre el piloto:** rechazar, realizar una prueba limitada o aprobar un uso definido.

## Antes de empezar

**Requisitos previos:** [delegación](/articles/effective-ai-agent-delegation/), [ciclos acotados con objetivos](/articles/effective-ai-bounded-agent-loops/) y un caso de uso ficticio. Reserva 35 minutos. La dificultad es intermedia. Esta lección no requiere instalar un agente persistente.

**Caso de uso:** una persona que coordina un taller quiere que un asistente lea un horario y prepare un borrador de recordatorio. La solicitud no autoriza enviar el recordatorio. Tu evaluación debe respetar este límite.

## Compara las funciones

| Enfoque | Tipo de tarea habitual | Primera pregunta |
|---|---|---|
| **Un chat** | Redactar un recordatorio | ¿Está disponible el horario? |
| **Agente de solo lectura** | Verificar datos del horario de manera independiente | ¿Qué fuente debe leer? |
| **Agente de programación** | Actualizar un programa local de informes | ¿Qué archivos y pruebas corresponden? |
| **Plataforma persistente** | Responder a mensajes o programaciones con el tiempo | ¿Qué activadores, herramientas y estados guardados existen? |

**OpenClaw** es una plataforma de agentes de código abierto con una puerta de enlace, canales de mensajería, herramientas, memoria, conexiones MCP y subagentes. Su [descripción general](https://docs.openclaw.ai/start/why-openclaw), [guía de conexión MCP](https://docs.openclaw.ai/tools/mcp) y [guía de subagentes](https://docs.openclaw.ai/tools/subagents) describen esos componentes. Revisa la configuración activa de canales, herramientas y aislamiento antes de iniciar un piloto.

**Hermes Agent** es la aplicación de agentes de Nous Research. La familia de modelos Hermes es independiente. Su [documentación](https://hermes-agent.nousresearch.com/docs/), [guía de delegación](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation) y [guía de configuración](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/) cubren CLI, mensajería, herramientas, memoria y tareas delegadas. La [guía de memoria](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/) describe almacenes locales y la aprobación de escritura. El valor predeterminado documentado de `memory.write_approval` y `skills.write_approval` es `false`. Activa la aprobación o deshabilita el almacén correspondiente si el piloto requiere revisar las escrituras. Comprueba la configuración en ejecución antes de confiar en cualquiera de esos controles.

| Punto de evaluación | OpenClaw | Hermes Agent |
|---|---|---|
| **Punto de entrada** | Puerta de enlace y canales conectados | CLI o interfaz de mensajería configurada |
| **Trabajo delegado** | Subagentes con reglas de sesión y herramientas específicas de la plataforma | Tareas delegadas con reglas de herramientas específicas de la plataforma |
| **Estado persistente** | Revisar memoria habilitada y almacenamiento de sesiones | Revisar ajustes de memoria y perfiles, además de escrituras de habilidades |
| **Trabajo recurrente** | Revisar activadores y programaciones configurados | Revisar [tareas cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron/) y el estado de la puerta de enlace |
| **Primer piloto** | Una solicitud manual por un canal seleccionado | Una solicitud manual por CLI o mensajería |

La tabla describe puntos de revisión, no valores predeterminados de seguridad equivalentes. Registra la versión instalada y la configuración activa antes de conceder acceso a datos o cuentas reales.

**Los nombres no establecen un modelo común de permisos.** Un «subagente» de un producto puede recibir archivos, herramientas e historial distintos de los de un agente trabajador de otro producto. Consulta la documentación de la versión instalada y los ajustes activos, en vez de trasladar supuestos entre herramientas.

## Completa una hoja de accesos

**Escribe una fila por capacidad** antes de instalar o conectar un sistema. Usa los ajustes reales si tienes disponible el producto. Escribe «desconocido» en lugar de adivinar.

| Pregunta | Respuesta para el piloto del taller |
|---|---|
| **Tarea** | Redactar un recordatorio a partir de un horario sintético |
| **Entrada** | Un archivo de horario aprobado |
| **Archivos** | Leer el archivo de horario, sin permiso de escritura |
| **Herramientas externas** | Ninguna en el primer piloto |
| **Acceso a cuentas** | Ninguna cuenta de correo ni calendario |
| **Activador** | Solo solicitud manual |
| **Escrituras de memoria y habilidades** | Registrar los ajustes activos, deshabilitar los almacenes o exigir aprobación de escritura durante el piloto |
| **Registros** | Anotar la ruta de almacenamiento, regla de retención, instrucción, revisión de la fuente y borrador |
| **Revisión** | Una persona comprueba la fecha, la hora, el lugar y la lista de destinatarios |
| **Reversión** | Descartar el borrador y deshabilitar el piloto |

**El flujo de datos forma parte de la hoja.** Indica dónde salen los datos de tu equipo, qué proveedor los procesa y dónde persisten las transcripciones o la memoria. Si una herramienta se conecta al correo, documenta si lee, redacta o envía. Son permisos distintos.

## Decide sobre el piloto

**Rechazar:** el agente necesita permiso amplio para escribir en un buzón cuando solo debe redactar, o se desconocen sus activadores y registros. No necesitas instalar nada para rechazar una opción inadecuada.

**Piloto:** limita la entrada al horario sintético, usa un activador manual, deshabilita el envío y revisa un borrador. El resultado esperado es una hora correcta de las 19:00 y ningún mensaje enviado. Registra tu propia observación si ejecutas el piloto.

**Aprobar un uso definido:** solo después de que el piloto supere sus verificaciones y la persona responsable acepte los accesos, el activador, la retención y los pasos de revisión exactos. Aprobar la redacción no autoriza el envío ni la automatización posterior.

## Diagnostica un fallo

**Supón que un borrador de recordatorio indica las 18:00.** Comprueba si el agente leyó el horario actual o si la memoria almacenada o un mensaje antiguo proporcionó la hora obsoleta. Sustituye la entrada obsoleta, repite un piloto manual y mantén deshabilitado el envío. Un segundo borrador correcto no elimina el primer fallo del registro.

**Supón que aparece una conexión MCP en los ajustes, pero no hay herramientas disponibles.** Vuelve a [Estados de conexión MCP](/articles/effective-ai-mcp-server-setup/). Una entrada de servidor guardada no demuestra que la lectura haya funcionado.

## Practica y comprueba

**Tu resultado:** una hoja de accesos completada y una decisión: Rechazar, Piloto o Aprobar un uso definido. Indica un activador, un límite de permisos, una pregunta sobre el flujo de datos y una forma de detener al agente.

**Comprobación final:** otra persona debe entender qué acción realiza el agente, qué lee y guarda, cuándo se ejecuta, quién revisa el resultado y cómo deshabilitarlo. Si alguna respuesta se desconoce, elige Rechazar o un Piloto más limitado.

## Comprueba lo aprendido

1. **Pregunta:** ¿Una tarea de recordatorio que solo redacta necesita permiso para enviar correo? **Respuesta:** No. Mantén el envío fuera del alcance del piloto.
2. **Pregunta:** ¿Qué ajustes de Hermes deben revisarse antes de un piloto con escrituras controladas? **Respuesta:** Comprueba los ajustes activos de escritura de memoria y habilidades, incluidos los controles de aprobación.

## Siguientes pasos

**Continúa con el [proyecto final del flujo de trabajo con IA](/articles/effective-ai-capstone/)**. Para una comparación más amplia de entornos de ejecución, consulta la [guía de entornos para agentes](/articles/best-ai-agent-harnesses/).

**Navegación del curso:** [Anterior: Ciclos acotados](/articles/effective-ai-bounded-agent-loops/), [Índice del curso](/effective-ai-course-start/).
