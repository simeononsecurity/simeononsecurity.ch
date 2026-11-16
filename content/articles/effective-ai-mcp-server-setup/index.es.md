---
title: "Configuración de un servidor MCP: permisos, pruebas de herramientas y eliminación segura"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Conecta un servidor de documentación MCP de solo lectura, inspecciona sus herramientas, realiza una lectura real y elimina la conexión."
genre: ["Inteligencia artificial", "Herramientas para desarrolladores"]
tags: ["Configuración de servidor MCP", "Protocolo de contexto de modelos (MCP)", "Permisos MCP", "MCP en Codex", "MCP en Claude Code", "MCP en OpenCode"]
cover: "/img/cover/effective-ai-mcp-server-setup.webp"
coverAlt: "Un cliente de IA conectado a un servidor de documentación de solo lectura, con una herramienta y un límite de acceso visibles"
coverCaption: ""
---

[Volver al curso de flujo de trabajo práctico con IA](/effective-ai-course-start/)

**Usa un servidor MCP cuando una tarea requiera una herramienta repetible o información actualizada fuera del proyecto.** Model Context Protocol, o MCP, define cómo intercambian información sobre herramientas, recursos y prompts un cliente y un servidor. Una entrada del servidor no demuestra que la herramienta funcione. Esta lección prueba una conexión de documentación de solo lectura.

**Objetivo de aprendizaje:** distinguir la configuración de una lectura MCP real y documentar una eliminación segura.

## Ideas clave

- **Host MCP:** aplicación de IA que coordina usuarios, modelos, permisos y clientes.
- **Cliente MCP:** componente del protocolo que se comunica con un servidor.
- **Servidor MCP:** programa o servicio remoto que ofrece herramientas, recursos o prompts.
- **Descubrimiento de herramientas:** evidencia de una capacidad con nombre en el cliente.
- **Ejecución de herramientas:** evidencia de una llamada real y el contenido devuelto.
- **Alcance de permisos:** acceso concedido por el host, servidor, cuenta y usuario.

## Antes de empezar

**Requisitos previos:** [práctica de contexto y traspaso](/articles/effective-ai-context-window-management/) y una instalación actual de Codex CLI para el recorrido guiado. Reserva 35 minutos. Dificultad intermedia. Otros agentes de programación tienen guías de configuración independientes. El [servidor oficial OpenAI Docs MCP](https://learn.chatgpt.com/learn/docs-mcp) ofrece documentación para desarrolladores de solo lectura y no requiere cargar datos del curso.

**Usa el laboratorio sintético del curso.** No conectes un calendario, correo electrónico ni sistema de producción para este ejercicio. Una lectura de documentación basta para aprender los estados de conexión.

## Entiende el límite

| Estado | Lo que demuestra | Lo que no demuestra |
|---|---|---|
| **Configurado** | Existe una entrada de servidor | Accesibilidad |
| **Conectado** | El cliente llegó al servidor | Que existan herramientas útiles |
| **Descubierto** | Aparece una herramienta con nombre | Que su llamada tendrá éxito |
| **Ejecutado** | Una llamada devolvió contenido | Que la tarea final sea correcta |
| **Verificado** | La fuente y el resultado responden a la pregunta | Que futuras llamadas siempre funcionen |

**MCP no concede permisos de cuenta por sí solo.** Importan el host cliente, el servidor, la autenticación, el alcance de la cuenta y los ajustes de aprobación local. La [especificación MCP](https://modelcontextprotocol.io/specification/2026-07-28) define el protocolo, mientras que cada producto controla su propia experiencia.

**Trata la salida del servidor como material de referencia.** Una página recuperada no puede reemplazar tu tarea ni autorizar una escritura de archivos. Cada definición de herramienta también consume contexto, así que conecta solo el servidor necesario para esta lectura y elimínalo al terminar.

## Conecta un servidor de solo lectura

**En Codex CLI,** ejecuta estos comandos en una terminal. El primero agrega el servidor público de documentación. El segundo enumera los servidores configurados.

```bash
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex mcp list
```

**Evidencia de configuración esperada:** la lista contiene `openaiDeveloperDocs`. Esto solo demuestra el registro. Inicia una sesión nueva de Codex en la carpeta del laboratorio extraído e inspecciona la lista de herramientas MCP con `/mcp`. Debes usar los nombres que muestre tu versión instalada.

**Solicita una lectura real:**

```text
Usa el servidor MCP de documentación para desarrolladores de OpenAI para encontrar las instrucciones actuales de AGENTS.md.
Devuelve el título y la URL de la página fuente y dos puntos relevantes para este laboratorio. Indica la herramienta MCP usada.
No edites archivos.
```
**Inspecciona el resultado.** La página devuelta debe describir `AGENTS.md` como instrucciones del repositorio e incluir la URL exacta. Abre la página citada y confirma su tema. Una respuesta sin una llamada MCP en la transcripción es una respuesta normal, no prueba de ejecución de herramientas.

## Diagnostica un fallo

**Si `codex mcp list` muestra el servidor, pero `/mcp` no muestra herramientas,** el registro funcionó y el descubrimiento falló. Reinicia la sesión, revisa los servidores activos con `/mcp` y la configuración guardada con `codex mcp get openaiDeveloperDocs`, y luego comprueba la URL y el acceso a la red. No afirmes que la configuración demuestra que MCP funciona.

**Si aparece una herramienta, pero falla la lectura,** registra el error y vuelve a intentarlo una vez tras comprobar la conectividad. Si vuelve a fallar, usa en el navegador la página oficial citada como fuente alternativa y marca el ejercicio MCP como incompleto. No inventes el resultado de una herramienta.

## Elimina la conexión

**Después de la lectura,** elimina el servidor de práctica de Codex CLI y confirma que la entrada desaparezca.

```bash
codex mcp remove openaiDeveloperDocs
codex mcp list
```

**Evidencia de eliminación esperada:** `openaiDeveloperDocs` no aparece en la nueva lista. Reinicia cualquier sesión activa de Codex antes de comprobar si cambiaron sus herramientas disponibles. Eliminar una definición local no revoca una autorización de cuenta distinta usada por otro servicio.

## Usa otro cliente

**Claude Code y OpenCode también admiten MCP.** Sigue la [guía MCP de Claude Code](https://code.claude.com/docs/en/mcp) o la [guía MCP de OpenCode](https://opencode.ai/docs/mcp-servers/) para la versión instalada. Registra los mismos cinco estados: configurado, conectado, descubierto, ejecutado y verificado. El esquema de configuración y los permisos de agente de OpenCode varían según la versión; usa ejemplos de la guía que corresponda a tu instalación.

**Para una ruta solo con navegador,** lee la [página oficial de AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) y completa el mismo registro de verificación. Marca el descubrimiento y la ejecución de herramientas como «no ejecutado». Esta ruta enseña a revisar fuentes, pero no demuestra que MCP funcione.

## Practica y comprueba

**Tu artefacto:** un registro de conexión de cinco filas con el nombre del servidor, el nombre de la herramienta, la URL de origen, el resultado observado y la evidencia de eliminación. Mantén los tokens y los identificadores de cuenta fuera de capturas y registros.

**Criterio de finalización:** la ruta conectada solo se aprueba después de una lectura real con una herramienta y una eliminación posterior de la configuración. La ruta alternativa aprueba su ejercicio de revisión de fuentes con MCP marcado como no ejecutado.

## Comprueba lo aprendido

1. **Pregunta:** ¿Una entrada MCP guardada demuestra que una herramienta funcionó? **Respuesta:** no. Verifica el descubrimiento, los permisos y una lectura real.
2. **Pregunta:** ¿Qué costo de contexto añade una conexión MCP amplia? **Respuesta:** las descripciones y esquemas de herramientas consumen parte del contexto activo.

## Solución de problemas

- **Comando `codex` desconocido:** instala o actualiza Codex CLI desde la guía oficial enlazada.
- **Servidor listado, sin herramientas:** inspecciona el estado de la sesión y los diagnósticos del servidor.
- **La llamada devuelve contenido ajeno a la consulta:** concreta la búsqueda y verifica la página fuente.
- **La eliminación parece no tener efecto:** inicia una sesión nueva e inspecciona la lista activa de servidores.

## Próximos pasos

**Continúa con [Verificación de salidas de IA](/articles/effective-ai-output-verification/).** Para extensiones más amplias, lee la [guía del sitio sobre complementos y herramientas MCP de Claude Code](/articles/claude-code-plugins-skills-mcp-tools/).

**Navegación del curso:** [Anterior: Gestión del contexto](/articles/effective-ai-context-window-management/), [Índice del curso](/effective-ai-course-start/).
