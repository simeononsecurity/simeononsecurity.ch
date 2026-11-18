---
title: "Gestión de la ventana de contexto de IA: mantén enfocados los agentes de programación"
description: "Controla el contexto activo de una tarea de IA con archivos seleccionados, traspasos breves y respuestas pequeñas de trabajadores, conservando decisiones y pruebas."
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
genre: ["Inteligencia artificial", "Ingeniería de software"]
tags: ["gestión de contexto de IA", "contexto de agente de programación", "traspaso de IA", "compactación de contexto", "orquestación de agentes", "presupuesto de tokens"]
cover: "/img/cover/effective-ai-context-window-management.webp"
coverAlt: "Una nota breve de traspaso junto a archivos seleccionados del proyecto y una transcripción de chat mucho más extensa descartada"
coverCaption: ""
---

[Volver al Curso práctico de flujos de trabajo con IA](/effective-ai-course-start/)

**La ventana de contexto es el texto y el resto del material que un modelo procesa durante el turno actual.** Los mensajes, instrucciones, definiciones de herramientas, fragmentos de archivos, resultados de herramientas e historial de conversación ocupan espacio. Esta lección explica cómo enfocar la siguiente tarea y dejar un traspaso fiable.

**Objetivo de aprendizaje:** preparar un traspaso breve y probarlo en una sesión nueva.

## Ideas clave

- **Tokens:** unidades que el modelo usa para procesar entradas y salidas.
- **Contexto activo:** material disponible durante un turno, sujeto a los límites del producto.
- **Fuentes duraderas:** archivos o registros del proyecto que están fuera del chat.
- **Compactación:** resume o recorta contexto anterior y puede omitir un detalle necesario.
- **Traspaso:** dirige una sesión nueva a las fuentes actuales y al trabajo verificado.

## Antes de empezar

**Requisitos previos:** el laboratorio editado de la [primera tarea con un agente de programación](/articles/effective-ai-coding-agent-first-task/), su requisito aprobado y la [lección sobre paquetes de tareas](/articles/effective-ai-task-packets/). Si seguiste la ruta de estudio, usa tu laboratorio editado manualmente. Reserva 35 minutos. La dificultad es intermedia. Guarda las notas del curso fuera de la carpeta del laboratorio extraído para que `git status` solo muestre cambios de código.

## Elige el contexto según la tarea

**Para editar el filtro de estado,** el agente necesita `task_report.py`, `docs/requirements.md`, las pruebas pertinentes y una muestra pequeña de `tasks.json`. No necesita todos los chats antiguos, toda la documentación del sitio ni el historial completo de Git. Consulta primero un mapa y luego carga los archivos mínimos para decidir el siguiente paso.

| Tarea | Contexto útil | Contexto sobrante |
|---|---|---|
| **Definir el comportamiento** | Requisito aprobado y una muestra de datos | Conversaciones exploratorias antiguas |
| **Editar el programa** | Programa y pruebas específicas | Directorios de proyectos no relacionados |
| **Revisar el resultado** | Diferencias, salida de pruebas y requisito | Transcripción completa del agente |
| **Retomar más tarde** | Nota de traspaso y rutas de las fuentes | Un chat de varias horas pegado entero |

**Esto es una decisión de recuperación, no una regla para ocultar pruebas.** Si falla una prueba, incluye la salida exacta y el archivo implicado. Quita registros irrelevantes, no los detalles necesarios para diagnosticar el fallo.

**Cuenta el espacio fijo antes de añadir trabajadores.** Las instrucciones del agente y los esquemas de herramientas disponibles podrían ocupar contexto antes de leer un archivo de tarea. Un segundo trabajador repite parte de ese gasto y añade un informe que el agente principal debe revisar. Para editar dos archivos, usa un agente. Para buscar de forma independiente en muchas fuentes, un informe breve de un trabajador podría reducir el contexto de la sesión principal aunque aumente el uso total de tokens.

## Prepara un traspaso breve

**Un traspaso es un registro corto para la siguiente sesión.** Debe distinguir el trabajo terminado del propuesto. Guarda este ejemplo como `course-notes/handoff.md`, fuera del laboratorio, y sustituye las observaciones de ejemplo por las tuyas.

```text
Objetivo: añadir --status open|done al informe de tareas del curso.
Fuente: docs/requirements.md, revisión 1.
Espacio de trabajo: carpeta extraída effective-ai-course-lab.
Estado actual: el filtro de estado está en task_report.py y en las pruebas.
Verificado: registra el resultado observado de las pruebas y los recuentos manuales 4, 2 y 2.
Decisión: tasks.json no cambió.
Pendiente: revisión independiente de diferencias y fuente.
Siguiente comprobación: vuelve a ejecutar las pruebas y el caso de estado no válido.
Detente si: el requisito o el valor de referencia difieren de este registro.
```

**El ejemplo no afirma que hayas ejecutado ese trabajo.** Anota los resultados reales de pruebas y los archivos modificados. Si cambia una revisión de la fuente, actualiza el traspaso después de volver a leerla.

## Prueba una sesión nueva

**Abre un chat o una sesión nueva de agente de programación** en el laboratorio. En un chat, pega el traspaso y el `AGENTS.md` del laboratorio sintético, y nombra los archivos que debe revisar. En un agente de programación, abre la carpeta del laboratorio y pega el traspaso con permiso de lectura para los archivos indicados. Pregunta:

```text
Con esta entrega y los archivos actuales del repositorio, indica los valores de estado aprobados, el recuento de referencia y la siguiente comprobación. No edites.
Si la entrega contradice una fuente actual, informa del conflicto.
```

**Razonamiento esperado:** la sesión nueva encuentra `open` y `done` en `docs/requirements.md`, identifica el recuento inicial de 4 y señala las pruebas y comprobaciones manuales. Si repite el valor antiguo `pending`, vuelve a leer el requisito y corrige el traspaso.

## Mantén pequeño el orquestador

**Un orquestador es el agente principal que coordina trabajadores.** Asigna a cada trabajador una pregunta acotada y archivos de entrada concretos. Pide un resultado breve: hallazgo, ruta de evidencia, confianza y asunto pendiente. Guarda los registros detallados en un archivo o en la sesión del trabajador. Devuelve solo lo que el agente principal necesita para decidir el siguiente paso.

**Ejemplo:** pide a un trabajador de solo lectura que revise las pruebas y responda «caso que falta, archivo y línea, comprobación sugerida». No le pidas que pegue todas las pruebas en el chat principal. Luego el agente principal verifica el hallazgo en el repositorio antes de editar. La [lección sobre delegación](/articles/effective-ai-agent-delegation/) añade una tarea de trabajador independiente cuando el alcance justifica el coste.

**Las sesiones de los trabajadores tienen su propio contexto en muchos productos,** pero la herencia y el aislamiento varían. Consulta las reglas actuales del producto antes de suponer que un trabajador ve las mismas instrucciones, archivos o herramientas que su agente principal. Las guías de [subagentes de Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents) y [subagentes de Claude Code](https://code.claude.com/docs/en/sub-agents) describen el comportamiento de cada producto.

## Usa la compactación con cuidado

**La compactación acorta el historial activo.** Codex, Claude Code y OpenCode difieren en cuándo y cómo compactan. Trata un resumen compactado como ayuda para continuar, no como registro completo del proyecto. Guarda los requisitos y las decisiones en archivos y vuelve a comprobarlos después de compactar. Consulta las guías actuales sobre [buenas prácticas de Codex](https://learn.chatgpt.com/docs/learn/best-practices), [comandos de Claude Code](https://code.claude.com/docs/en/commands) y [compactación de OpenCode 2](https://opencode.ai/v2/docs/compaction). OpenCode 1 y OpenCode 2 usan esquemas de compactación distintos. Comprueba `opencode --version` antes de copiar ajustes.

**Si el asistente pierde una restricción,** detén la edición, vuelve a abrir la fuente y repite el paquete de tareas. Una sesión nueva con un traspaso breve y verificado suele requerir menos atención que corregir una conversación larga que se ha confundido.

## Practica y comprueba

**Tu artefacto:** un traspaso de menos de 180 palabras, guardado fuera del laboratorio. Marca cada línea como fuente, resultado observado, decisión o acción pendiente. Entrégalo a una sesión nueva y registra si identifica los dos valores de estado aceptados y la siguiente comprobación.

**Comprobación final:** la sesión nueva nombra `open`, `done`, el recuento inicial de 4 y un paso de prueba sin depender del chat antiguo. Corrige lo que falte y vuelve a probar con otra sesión nueva.

## Comprueba lo aprendido

1. **Pregunta:** ¿Qué debe incluir un traspaso para una sesión nueva? **Respuesta:** El objetivo, la fuente autorizada, el estado actual, el resultado comprobado y la siguiente acción.

2. **Pregunta:** ¿Por qué conviene que el informe de un trabajador sea breve? **Respuesta:** Un informe conciso con pruebas aporta el resultado necesario al orquestador sin repetir la transcripción del trabajador.

## Solución de problemas

- **El resumen omite una decisión:** añade una línea breve con la decisión y la revisión de su fuente.
- **La respuesta del trabajador es enorme:** pide una tabla de pruebas limitada y referencias a archivos.
- **El traspaso está desactualizado:** vuelve a leer los archivos actuales antes de editar.
- **Sigue faltando contexto:** divide la tarea en sesiones más pequeñas con artefactos separados.

## Próximos pasos

**Continúa con [Configuración del servidor MCP](/articles/effective-ai-mcp-server-setup/)**. Añadirás una herramienta externa de solo lectura y limitarás el alcance de su salida.

**Navegación del curso:** [Anterior: Primera tarea de programación](/articles/effective-ai-coding-agent-first-task/), [Índice del curso](/effective-ai-course-start/).
