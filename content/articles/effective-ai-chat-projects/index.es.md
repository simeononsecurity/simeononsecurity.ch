---
title: "Proyectos de ChatGPT y Claude: configura un contexto de IA reutilizable"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Configura proyectos de ChatGPT y Claude con instrucciones claras, archivos de referencia actuales y una prueba sencilla del contexto reutilizado."
genre: ["Inteligencia artificial", "Productividad"]
tags: ["Proyectos de ChatGPT", "Proyectos de Claude", "instrucciones de proyectos de IA", "contexto de IA", "configuración de proyectos de ChatGPT", "conocimiento de proyectos de Claude"]
cover: "/img/cover/effective-ai-chat-projects.webp"
coverAlt: "Dos espacios de trabajo de proyectos de IA organizados con un resumen del proyecto, archivos de referencia y conversaciones separadas"
coverCaption: ""
---

[Volver al curso Flujo de trabajo práctico con IA](/effective-ai-course-start/)

**Crea un proyecto cuando varias conversaciones compartan el mismo propósito.** Guarda en un solo lugar las instrucciones estables y los archivos de referencia aprobados. Mantén cada conversación centrada en una tarea. En esta lección practicarás con un taller comunitario ficticio y sin datos privados.

**Objetivo de aprendizaje:** crearás un proyecto con dos fuentes controladas y comprobarás sus datos en un chat nuevo.

## Ideas clave

- **Las instrucciones del proyecto** definen un comportamiento reutilizable para chats relacionados.
- **Las fuentes del proyecto** contienen el material de referencia que quieres que consulte el asistente.
- **El historial de conversación** registra un intercambio, pero no sustituye una fuente aprobada.
- **Una prueba en un chat nuevo** revela si la configuración aporta suficiente contexto.

## Antes de empezar

**Requisitos previos:** una cuenta de ChatGPT o Claude y el paquete de tareas de la [lección 1](/articles/effective-ai-workflow-foundations/). Reserva 35 minutos. El nivel de dificultad es inicial. Usa nombres, fechas y lugares inventados durante toda la práctica.

**Crea dos archivos pequeños** en tu computadora. Abre un editor de texto plano, pega cada bloque en un archivo separado y guárdalo con el nombre `.md` indicado. Los archivos Markdown son texto plano. `workshop-brief.md` describe la audiencia y el estilo. `approved-schedule.md` contiene el horario oficial ficticio.

```text
workshop-brief.md, revisión 1
Público: personas inscritas en un taller introductorio.
Estilo: frases breves y tono cordial y objetivo.
No inventes precios, funciones de accesibilidad ni detalles de estacionamiento.
```

```text
approved-schedule.md, revisión 1
Marcador de la fuente: WS-2026-11-12-R1
Evento: Introducción a la seguridad digital
Fecha: 2026-11-12
Inicio: 7 p.m.
Lugar: Community Room A
```

## Configura ChatGPT

1. **Abre «Projects»** en la barra lateral de ChatGPT y crea un proyecto llamado `Workshop Practice`.
2. **Añade los dos archivos** como fuentes del proyecto.
3. **Abre la configuración del proyecto** y añade las instrucciones siguientes.
4. **Revisa la memoria y las opciones para compartir** de tu cuenta y espacio de trabajo antes de añadir material real.

```text
Usa approved-schedule.md para los datos del evento.
Usa workshop-brief.md para el público y el estilo.
Si falta un dato solicitado, pide la fuente o indícalo como desconocido.
Redacta borradores solamente. No los envíes ni publiques.
Enumera los cambios factuales después de cada borrador revisado.
```

**Los proyectos de ChatGPT agrupan chats, archivos e instrucciones relacionados.** La configuración y las funciones disponibles varían según el plan y el espacio de trabajo. Si el proceso de creación ofrece memoria exclusiva del proyecto, selecciónala para hacer una prueba de aislamiento limpia. Con la memoria predeterminada, un chat podría usar información ajena a los archivos cargados. El marcador único que aparece abajo te ayuda a probar el archivo sin tratar una respuesta obtenida de la memoria como prueba de lectura. Consulta la [guía oficial de proyectos de ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) para verificar las opciones actuales de memoria.

## Configura Claude

1. **Abre «Projects»** en Claude y crea un proyecto con el mismo nombre de práctica.
2. **Añade los dos archivos** al conocimiento del proyecto.
3. **Establece como instrucciones del proyecto** las mismas cinco líneas.
4. **Inicia un chat nuevo dentro del proyecto** para comprobar la configuración.

**Estos pasos describen los proyectos clásicos de Claude.** Anthropic está desplegando una beta de Projects independiente para ciertos usuarios Pro y Max de Claude Code. En la beta, un proyecto equivale a una conversación con hilos paralelos en la nube. Consulta [Qué son los proyectos](https://support.claude.com/en/articles/9517075-what-are-projects) y sigue la interfaz de tu cuenta. Las instrucciones del proyecto clásico se aplican a todos los chats y el conocimiento del proyecto aporta material de referencia compartido. Usa los archivos cargados como datos controlados. El funcionamiento de la memoria del proyecto varía según la cuenta y la configuración, así que no trates los detalles de otro chat como el horario aprobado. Revisa los controles actuales en la [guía de configuración de proyectos de Claude](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

| Modo del proyecto | Material compartido que debes revisar | Prueba nueva |
|---|---|---|
| **Proyecto de ChatGPT** | Archivos cargados, instrucciones y modo de memoria elegido | Un chat nuevo del proyecto cita el marcador del horario |
| **Proyecto clásico de Claude** | Conocimiento e instrucciones compartidos entre chats | Un chat nuevo del proyecto cita el marcador del horario |
| **Beta de Claude Projects** | Fuentes y contexto del proyecto y de sus hilos en la nube | Un hilo nuevo del proyecto cita el marcador del horario |

**Un proyecto reúne contexto, pero no aprueba una fuente.** El marcador muestra si el archivo indicado llegó al chat. Aun así, compara tú la fecha, la hora y la sala con el archivo.

## Prueba un chat nuevo

**Abre una conversación nueva de un proyecto de ChatGPT o un chat nuevo de un proyecto clásico de Claude.** En la beta de Claude Projects, usa un hilo nuevo del proyecto. Pide un anuncio breve. Omite el horario en tu prompt para que las fuentes del proyecto aporten los datos.

```text
Redacta un correo de 100 palabras para el próximo taller.
Indica el archivo fuente y su marcador exacto para la hora y el lugar.
Enumera los datos que falten después del borrador.
No envíes el mensaje.
```

| Resultado | Significado | Próximo paso |
|---|---|---|
| **Coinciden la hora, el lugar y el marcador** | El chat tiene acceso al archivo | Comprueba tú los datos con el archivo |
| **Se inventa un dato** | Fallaron las instrucciones o el uso de la fuente | Elimina el dato y concreta más la solicitud |
| **Falta la fuente** | La referencia no llegó a este chat | Comprueba la pertenencia al proyecto y la carga del archivo |
| **Aparece una revisión antigua** | El proyecto contiene material obsoleto | Sustituye la fuente y repite la prueba |

**Una sola respuesta correcta no demuestra fiabilidad.** La memoria predeterminada del proyecto podría proporcionar una hora conocida sin leer el archivo cargado. Exige el marcador exacto `WS-2026-11-12-R1` y repite la prueba con este borrador contradictorio:

```text
Revisa esta frase según el calendario aprobado del proyecto:
«La clase Introducción a la seguridad digital empieza a las 6 p.m. en Community Room A».
Indica el cambio factual, el archivo fuente y el marcador. No envíes el mensaje.
```

**Respuesta esperada:** la línea indica las 7 p. m. y nombra `approved-schedule.md` con el marcador `WS-2026-11-12-R1`. Registra cualquier fallo que observes. Una prueba aprobada no necesita un fallo inventado.

**Ejemplo de registro de prueba:** chat nuevo, primer prompt, hora 7 p. m., lugar Community Room A, fuente `approved-schedule.md`, marcador `WS-2026-11-12-R1`, aprobado. Prompt de conflicto, cambio de 6 p. m. a 7 p. m., aprobado. Este es un registro de ejemplo. Sustitúyelo por tus propias observaciones.

## Mantén el proyecto

**Mantén breves las instrucciones del proyecto.** Guarda allí las reglas estables. Incluye detalles específicos de cada tarea en su prompt. Sustituye los archivos desactualizados e identifica sus revisiones. Separa el trabajo no relacionado en otro proyecto para evitar conflictos entre fuentes.

**Antes de compartir un proyecto,** revisa sus archivos, chats, instrucciones y lista de acceso. Un proyecto es un espacio de trabajo, no un sistema de aprobación. Incluso un archivo llamado «approved» necesita un responsable real y un registro de revisión para trabajos importantes.

## Practica y comprueba

**Tu resultado:** un proyecto con dos archivos de fuentes sintéticas, cinco líneas de instrucciones y un registro breve de prueba. Anota la hora y el lugar observados, el nombre de la fuente, el marcador y cualquier dato inventado. Cuando termines, elimina el proyecto de práctica si ya no lo necesitas.

**Razonamiento esperado:** un chat nuevo usa las fuentes del proyecto para obtener datos estables, mientras que tu prompt define el resultado inmediato. Verifica la respuesta con el archivo. Si falta una fuente o aparece una revisión incorrecta, vuelve a configurar el proyecto.

## Comprueba lo aprendido

1. **Pregunta:** ¿Un chat nuevo de un proyecto de ChatGPT garantiza el aislamiento con cualquier configuración de memoria? **Respuesta:** No. Comprueba el modo de memoria y haz una prueba con un marcador de fuente único.

2. **Pregunta:** ¿Qué debes hacer si el proyecto repite un horario antiguo? **Respuesta:** Revisa la fuente adjunta y el alcance de la memoria, y sustituye el material obsoleto.

## Solución de problemas

- **Faltan controles del proyecto:** consulta tu plan actual y la configuración del espacio de trabajo en la guía del proveedor.
- **Respuestas incompatibles:** elimina los archivos de fuentes duplicados u obsoletos y abre un chat nuevo.
- **Uso compartido inesperado:** revisa los miembros del proyecto y quita las fuentes sensibles antes de continuar.
- **Se repiten los cambios de estilo:** acorta las instrucciones y ofrece un ejemplo breve en el prompt de la tarea.

## Próximos pasos

**Continúa con [Contexto de repositorio en AGENTS.md](/articles/effective-ai-agents-md-context/)**. La siguiente lección pasa de un proyecto de chat a un repositorio de código local.

**Navegación del curso:** [Anterior: Fundamentos del flujo de trabajo](/articles/effective-ai-workflow-foundations/), [Índice del curso](/effective-ai-course-start/).
