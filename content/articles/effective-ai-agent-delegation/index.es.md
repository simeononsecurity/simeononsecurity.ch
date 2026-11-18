---
title: "Delegación de agentes de IA: asigna tareas y revisa resultados"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Aprende cuándo ayuda un segundo agente de IA, cómo asignar tareas acotadas, evitar conflictos de edición e integrar pruebas en la sesión principal."
genre: ["Inteligencia artificial", "Ingeniería de software"]
tags: ["Delegación de agentes de IA", "Subagentes", "Agentes de trabajo", "Contexto del orquestador", "Worktrees de IA", "Tareas paralelas de IA"]
cover: "/img/cover/effective-ai-agent-delegation.webp"
coverAlt: "Un agente principal asigna tareas separadas de investigación y revisión antes de combinar informes breves con pruebas."
coverCaption: ""
---

[Volver al curso de flujos de trabajo prácticos de IA](/effective-ai-course-start/)

**Delega una pregunta independiente cuando requiera suficiente trabajo para justificar una sesión separada.** Un agente de trabajo inspecciona fuentes, revisa pruebas o prepara un cambio acotado desde su propio contexto. El agente principal comprueba e integra el resultado. Esta lección usa una comparación de documentación como ejemplo mientras la sesión principal mantiene la pequeña tarea de laboratorio.

**Objetivo de aprendizaje:** asignarás una revisión independiente a un agente y verificarás su breve informe de pruebas.

## Puntos clave

- **Orquestador:** el agente principal que coordina la tarea y la revisión final.
- **Agente de trabajo:** un agente separado al que se asigna un resultado acotado.
- **Trabajo independiente:** una subtarea cuya respuesta no depende del resultado inconcluso de otro agente.
- **Responsabilidad:** un archivo o pregunta asignado a un único agente.
- **Integración:** la comparación del resultado del agente con las fuentes actuales por parte del agente principal.

## Antes de empezar

**Requisitos previos:** tu [traspaso de contexto](/articles/effective-ai-context-window-management/) y tus registros de [verificación de resultados](/articles/effective-ai-output-verification/). Reserva 40 minutos. La dificultad es intermedia. La ruta conectada requiere un producto compatible con agentes de trabajo. La ruta de estudio usa un chat separado e integración manual.

**Empieza con una copia limpia.** Guarda fuera del laboratorio el diff del filtro editado y el registro de pruebas. Extrae el ZIP original en una carpeta temporal nueva. Ejecuta el comando inicial y sus dos pruebas de referencia. Repite la línea base de Git de la configuración del curso y vuelve a crear las instrucciones breves `AGENTS.md` y `CLAUDE.md` opcional de la lección sobre contexto del repositorio. Haz tú mismo el commit de esos archivos de instrucciones y confirma que `git status --short` no muestra cambios. Conserva la copia del filtro editado como referencia, pero realiza el ejercicio con el proyecto inicial limpio.

## Decide si delegar

**Usa un solo agente** para un cambio pequeño y secuencial. Delegar añade costes de configuración, tokens y revisión. Usa un agente de trabajo cuando una pregunta de solo lectura sea independiente y, de otro modo, llene la sesión principal de archivos o páginas fuente.

| Tarea del laboratorio | ¿Delegar? | Motivo |
|---|---|---|
| **Añadir un filtro con dos valores** | Normalmente no | Un archivo pequeño y pruebas concretas |
| **Buscar casos que faltan en dos pruebas base** | Normalmente no | El agente principal lee antes un archivo corto |
| **Comparar tres documentos actuales de productos** | Sí, en modo de solo lectura | La consulta de fuentes se queda en el contexto del agente |
| **Editar dos veces la misma función** | No | Los cambios simultáneos generan conflictos |

**El agente de trabajo necesita menos contexto que el orquestador,** no una copia de toda la conversación. Dale el objetivo, la ruta de la fuente, los límites de la tarea y el formato de respuesta. Mantén breve el informe de pruebas en la sesión principal. Inspecciona los archivos citados antes de actuar.

## Ejecuta un agente de solo lectura

**Mantén pequeña la tarea principal.** En la sesión principal, lee el `AGENTS.md` local y anota qué archivo contiene el comando de pruebas. Asigna a un agente la siguiente pregunta independiente de investigación. No necesita todo el laboratorio ni el chat anterior.

**Ruta conectada:** abre el laboratorio en Codex, Claude Code u otro producto con agentes. Pide al agente principal que delegue la siguiente tarea de solo lectura. Comprueba en el registro de herramientas que el agente se inició y devolvió un informe. Si el producto no ofrece agentes, usa otra sesión y descríbela como agente separado. Las guías de [subagentes de Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents), [subagentes de Claude Code](https://code.claude.com/docs/en/sub-agents) y [agentes de OpenCode](https://opencode.ai/docs/agents/) describen los controles actuales.

**Ruta de estudio:** abre un chat nuevo para la misma solicitud. Entrégale los tres enlaces oficiales o extractos. Etiquétalo como agente simulado. Un segundo chat tiene un contexto separado, pero no demuestra la ejecución nativa de subagentes.

```text
Usa la documentación oficial vigente de Codex AGENTS.md, Claude Code Memory y OpenCode Rules.
Compara cómo carga cada producto los archivos de instrucciones del repositorio.
No edites archivos.
Devuelve como máximo tres filas: producto, archivo de instrucciones, URL de la fuente
y un comportamiento de carga. Indica las dudas. No pegues páginas completas.
```

**Fuentes:** [Instrucciones de proyecto de Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [memoria de Claude Code](https://code.claude.com/docs/en/memory) y [reglas de OpenCode](https://opencode.ai/docs/rules/). El informe esperado menciona `AGENTS.md` para Codex y OpenCode. Las versiones actuales de Claude Code también cargan `AGENTS.md` directamente cuando ningún `CLAUDE.md` o `CLAUDE.local.md` tiene prioridad. Este laboratorio usa un archivo `CLAUDE.md` con una importación `@AGENTS.md`. Así también funciona con sesiones anteriores o configuradas de otra manera. Comprueba las páginas y la versión activas antes de presentar el ejemplo como un resultado observado de un agente.

## Integra los hallazgos

**Abre las fuentes citadas tú mismo.** Si el agente afirma que Claude Code siempre necesita una importación de `CLAUDE.md`, consulta su guía de memoria y corrige el informe. Compara el informe con tus archivos de instrucciones locales. Escribe una nota breve de integración:

```text
Aceptado: Codex y OpenCode usan AGENTS.md como instrucciones del proyecto.
Las versiones actuales de Claude Code pueden cargar AGENTS.md directamente. Este laboratorio
usa CLAUDE.md con una importación @AGENTS.md para mantener un mapa compartido estable.
Pruebas: anota las tres páginas oficiales actuales y la fecha de revisión.
Decisión: conserva un mapa compartido breve y una importación de Claude.
```

**Esta nota es el resultado útil del agente.** El orquestador necesita hallazgos verificados y rutas de fuentes, no la transcripción de la investigación. Delegar consume más tokens en total. Reduce el contexto principal solo cuando el trabajo separado ahorra atención.

## Asigna la responsabilidad de edición

**Si los agentes modifican archivos,** reparte la responsabilidad por archivo o usa worktrees separados para tareas que se solapan. Un worktree es otra copia de trabajo del mismo repositorio Git, con sus propios archivos. Mantiene separadas las modificaciones simultáneas. Después, el agente principal revisa e integra el resultado mediante un merge, cherry-pick o parche explícito, y vuelve a ejecutar las pruebas en el árbol integrado.

| Agente | Trabajo asignado | Entrega |
|---|---|---|
| **Implementación** | `task_report.py` | Diff y comando de pruebas |
| **Autor de pruebas** | `tests/test_task_report.py` | Casos y resultado observado |
| **Orquestador** | Requisito e integración final | Diff combinado y registro de aceptación |

**El laboratorio pequeño no necesita modificaciones en paralelo.** La tabla enseña un patrón de responsabilidad para proyectos mayores. Las pruebas de un worktree no validan una implementación que aún está aislada en otro. Si dos agentes necesitan la misma función, trabaja en serie o pide a uno que revise sin editar. Los worktrees separados evitan colisiones de archivos, pero no resuelven requisitos contradictorios.

## Comprueba el comportamiento del producto

**Los subagentes varían según el host.** Codex, Claude Code y OpenCode tienen distintas reglas de herencia de contexto, permisos de herramientas y entrega de resultados. Lee las guías de [subagentes de Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents), [subagentes de Claude Code](https://code.claude.com/docs/en/sub-agents) y [agentes de OpenCode](https://opencode.ai/docs/agents/) para tu producto instalado. No des por sentado que el agente recibe todo el contexto principal o un worktree aislado.

## Practica y comprueba

**Tu entrega:** un informe breve del agente de documentación y una nota de integración. En la ruta de estudio, usa un chat nuevo y etiquétalo como agente simulado. No afirmes que se ejecutó un subagente nativo en esta ruta.

**Comprobación de finalización:** el informe menciona tres fuentes oficiales, se limita a la pregunta y respeta su extensión. La nota de integración comprueba las fuentes y nombra los archivos de instrucciones del laboratorio.

## Comprueba lo aprendido

1. **Pregunta:** ¿Cuándo ayuda un agente más que uno solo? **Respuesta:** Cuando trabaja en una pregunta independiente o un resultado propio y entrega un informe útil con pruebas.

2. **Pregunta:** ¿Qué debes hacer después de que dos agentes modifiquen archivos que se solapan? **Respuesta:** Integrar los cambios, inspeccionar el diff combinado y repetir las comprobaciones.

## Solución de problemas

- **El agente devuelve una transcripción larga:** pide una tabla breve con referencias a archivos y pruebas.
- **Los agentes discrepan:** vuelve a leer el archivo autoritativo antes de elegir una respuesta.
- **Dos cambios se solapan:** detén una edición y asigna responsabilidades o worktrees separados.
- **El acceso a las herramientas varía:** inspecciona los permisos del agente en vez de asumir que heredó los del principal.

## Próximos pasos

**Continúa con [Ciclos de objetivos acotados](/articles/effective-ai-bounded-agent-loops/)**. Para gobernanza de equipos más amplia que este pequeño laboratorio, sigue el [Curso de implementación de colaboración con IA](/ai-collaboration-course-start/).

**Navegación del curso:** [Anterior: Verificación de resultados](/articles/effective-ai-output-verification/), [Índice del curso](/effective-ai-course-start/).
