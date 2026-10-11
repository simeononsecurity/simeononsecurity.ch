---
title: "Flujo de trabajo de GitHub con IA para personas no programadoras: Issues y Pull Requests"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Usa ediciones desde el navegador, Issues, paquetes de contexto del chat y pull requests revisados sin un entorno de desarrollo local."
genre: ["Inteligencia artificial", "Colaboración de equipos", "Ingeniería de software"]
tags: ["curso de colaboración con IA", "edición de GitHub desde el navegador", "GitHub Issues", "pull request", "colaboradores no programadores", "paquete de contexto", "entrega para revisión"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustración de profesionales revisando trabajo compartido en un espacio de trabajo de ciberseguridad"
coverCaption: ""
---

[Volver al curso de colaboración con IA](/ai-collaboration-course-start/)

**Los colaboradores que no programan usan las mismas reglas de autoridad desde el navegador.** Lees fuentes de GitHub, redactas con una herramienta de chat aprobada y envías un Issue o una edición de rama. El mantenedor ejecuta las comprobaciones y publica después de revisar. Usa este flujo después de activar la protección del repositorio, para que el acceso desde el navegador no omita los controles del agente de código.

## Puntos clave

- **Trabajo desde el navegador** sin terminal local.
- **Paquetes de contexto** que conservan el alcance y la evidencia de revisión.
- **Issues y ramas** que siguen siendo propuestas.
- **Entregas** que identifican el trabajo pendiente y el siguiente rol.

## Antes de empezar

**Requisitos:** la [lección sobre los límites del repositorio](/articles/ai-collaboration-github-repository/), acceso de lectura al laboratorio y una herramienta de chat aprobada si la deseas. **Tiempo estimado:** 45 a 60 minutos. **Dificultad:** introductoria. Quienes solo usan Issues omiten Git local y Actions. Quienes envían un PR coordinan con un mantenedor que terminó la [lección sobre agentes y Actions](/articles/ai-collaboration-github-agents-actions/).

**Base sin conectores:** abre GitHub por tu cuenta y proporciona solo extractos sintéticos. No se supone ninguna función de suscripción de chat. Si un proveedor no está aprobado, redacta manualmente con los mismos registros.

**Resultado:** entregas un Issue o PR con revisiones de origen fijas, texto propuesto, archivos afectados, exclusiones y preguntas sin resolver.

## Leer el paquete de fuentes

1. **Abre MAP-01 en `main`** y localiza después POL-01, REQ-17 y RUN-04.
2. **Lee cada fuente** y registra su revisión de commit desde la vista de commits del navegador.
3. **Copia las secciones sintéticas relevantes** con nombres de archivo, revisiones, alcance y excepciones.
4. **Marca el paquete como basado en una instantánea** hasta que el mantenedor lo compare con las fuentes actuales antes de publicar.

```text
Project: export-service-lab
Task: PROP-042 draft, no publication permission
Authority: requirement.json, REQ-17 revision 1
Baseline: retention_days 7
Policy: POL-01 version 1
Requested proposal: retention_days 30
Evidence: attach browser-verified commit references
Missing evidence: no runtime deletion observations
Output: proposed wording, affected files, questions, rollback
Stop: source unavailable, changed revision, conflicting authority
```

**Adjunta en privado las revisiones reales del sandbox.** La plantilla no contiene evidencia completa. Pide al asistente que identifique los registros ausentes antes de recomendar la publicación.

**Paquete sintético completo antes de leer una fuente activa:**

```text
Project: export-service-lab
Task: draft PROP-042 in an Issue
Approved baseline: REQ-17 revision 1, retention_days 7
Proposal: retention_days 30, synthetic export files only
Affected records: requirement.json, config.json, proposal.json, runbook.md
Exclusions: production data, backups, legal holds
Known evidence: supplied lab baseline files
Missing evidence: current main commit, owner decisions, runtime deletion result
Status: Draft, publication blocked until current revisions and reviews exist
Next role: maintainer supplies verified main commit and runs the consistency check
```

**El paquete es una solicitud de borrador completa.** La línea de evidencia ausente es intencional. Sustituye la base de laboratorio proporcionada por revisiones actuales del sandbox antes de pedir la publicación.

## Abrir un Issue

**Selecciona Issues, New issue** y usa el título **`PROP-042: propose thirty-day synthetic retention`**. Pega esta descripción y adjunta el paquete de fuentes.

```text
Proposal: PROP-042
Status: Draft
Current approved value: 7 days, REQ-17 revision 1
Requested value: 30 days
Reason: fictional pilot requirement, not compliance advice
Scope: synthetic export records only
Affected files: requirement.json, config.json, runbook.md
Evidence: source revisions and policy version attached
Reviewers: product-owner and operations-owner
Implementation reviewer: repository-maintainer
Acceptance: consistent records, denied publication, fresh handoff
Rollback: reviewed restoration of the approved baseline
```

**Pide al chat que compare la propuesta con el paquete**, enumere las suposiciones y redacte preguntas para los responsables. Guarda su borrador en el Issue. No le pidas aprobar el cambio ni trates el hilo del chat como registro de decisiones.

## Enviar ediciones desde el navegador

1. **Abre la pestaña Code del repositorio.** Selecciona el menú de ramas sobre la lista de archivos, confirma **`main`**, escribe **`proposal-042`** y elige **Create branch: proposal-042 from main**. Si no se permite crear la rama, usa un fork aprobado o la ruta de Issue indicada abajo.
2. **Confirma `proposal-042` en el menú de ramas** antes de abrir un archivo. Selecciona el archivo y el icono del lápiz. El editor web de GitHub no edita una rama protegida.
3. **Edita el requisito** a treinta días y revisión 2. Vuelve a abrir el menú de ramas antes de cada edición restante. Edita la configuración y el runbook en la misma rama.
4. **Edita `proposal.json`** con to_days 30, from_days 7 y base_revision 1.
5. **Previsualiza Markdown** y revisa la puntuación JSON. Confirma cada edición del navegador en **`proposal-042`**.
6. **Abre Pull requests y después New pull request.** Compara **`proposal-042`** con **`main`**, revisa los cuatro archivos modificados y crea un PR que cite el Issue. Pide al mantenedor un manifest nuevo de la base protegida y la ejecución del control de coherencia.
7. **Solicita revisiones de los responsables** en la revisión final de la propuesta. Mantén abierta la entrega hasta que la revisión y la lectura posterior tengan éxito.

**Registro de navegación:** anota el nombre del repositorio, número de Issue, rama de propuesta, rutas modificadas, número de PR, nombre del check-run, revisión de revisión y commit final de `main`. Usa las vistas Issues, Code, Pull requests, Actions y PR Checks/Reviews. Si GitHub mueve un control, localiza el registro por su número o ID de commit en vez de adivinar desde una captura. Exporta una nota privada de evidencia con las URL y el estado observado. Antes de compartirla fuera del equipo autorizado, elimina nombres de cuentas, correos, tokens, identificadores de inquilino y datos de repositorios ajenos. Conserva la evidencia sin redactar en el lugar privado aprobado.

**GitHub documenta las rutas de contribución mediante ramas y forks.** Quien no tiene permisos de escritura usa un fork aprobado o la ruta de Issue. Un fork no concede permiso de publicación en el repositorio original.

## Revisar el diff de trabajo

| Archivo | Base | Candidato |
|---|---|---|
| **Requisito** | Revisión 1, siete días | Revisión 2, treinta días |
| **Configuración** | Siete días | Treinta días |
| **Runbook** | `Retention days: 7` | `Retention days: 30` |
| **Propuesta** | De 7, a 7 | De 7, a 30, base 1 |
| **Manifest** | No capturado | Hashes de las fuentes protegidas previas al cambio |

**El manifest describe la base**, no el texto propuesto de treinta días. Hashear el requisito candidato y llamarlo evidencia de base causa una discrepancia con la base confiable.

## Verificar y entregar

**Prueba positiva:** el mantenedor hace merge después de la revisión del responsable y de superar los checks. Abre los archivos resultantes en **`main`** y confirma que coinciden. Adjunta el commit y la lectura posterior al Issue. Esto demuestra la configuración confirmada, no el comportamiento de eliminación en tiempo de ejecución.

**Prueba negativa:** pide al chat aprobar o publicar la propuesta. El comportamiento esperado de la política es una respuesta limitada a un borrador. Intenta por separado publicar directamente como colaborador y registra el rechazo de la plataforma con la revisión de fuente sin cambios. Mantén separadas las pruebas de comportamiento y de control de acceso.

```text
Handoff: HANDOFF-042
Proposal: PROP-042
Policy: POL-01 version 1
Sources: attach current requirement, runbook, and config revisions
Published value: record after reading main
Completed: merged files and check reference
Remaining: runtime deletion service not tested
Next role: operations-owner
Next action: independent source read and runbook verification
Stop: changed source, missing access, conflicting authority
```

**Inicia una sesión nueva solo con el mapa y la entrega.** Exige una lectura nueva de la fuente o una solicitud explícita de evidencia del navegador. Debe reconstruir el valor desde los registros de origen y no repetir el resumen anterior del asistente.

## Redactar sin perder el contexto

**Un colaborador del navegador necesita una pregunta completa.** “Please change retention to thirty days” omite la autoridad actual, el alcance, el estado de revisión y los registros afectados. Da al chat el paquete de fuentes y una instrucción de redacción. Si el registro no está disponible, pide evidencia autorizada al mantenedor en vez de sustituir el texto recordado.

```text
Draft an Issue for PROP-042 from the attached synthetic source packet.
Keep seven days labeled as the approved baseline.
Keep thirty days labeled as proposed intent.
Preserve exclusions for production data, backups, and legal holds.
List requirement, configuration, proposal, and runbook changes.
List missing evidence instead of filling it with guessed revisions.
Do not claim owner approval or delivered behavior.
```

**Inspecciona la respuesta antes de copiarla.** Comprueba si cambió el alcance, inventó un commit o describió la aprobación como terminada. Elimina afirmaciones sin respaldo y conserva las preguntas abiertas en el Issue. El chat ayuda a escribir la propuesta, pero no aporta evidencia de sistemas que no ha leído.

## Elegir la ruta de contribución

| Situación | Ruta | Entregable |
|---|---|---|
| **Solo lectura** | Issue con texto propuesto fijo | Solicitud de cambio lista para el mantenedor |
| **Acceso aprobado a ramas** | Ediciones del navegador en una rama de propuesta | PR con cambios relacionados |
| **Ruta de fork aprobada** | Fork y PR ascendente | Candidato pendiente de revisión ascendente |
| **Sin acceso a fuentes** | Detenerse y pedir evidencia autorizada | Tarea bloqueada de forma explícita |

**La ruta de Issue es una contribución completa**, no un ejercicio de programación fallido. Aportas el cambio previsto, la evidencia, el alcance y las preguntas de revisión. El mantenedor aporta el parche y el manifest. Después inspeccionas el parche para comprobar que coincide con tu solicitud.

| Ruta | Comprobación del colaborador | Entrega al mantenedor |
|---|---|---|
| **Solo Issue** | El Issue tiene un paquete de fuentes verificado, texto propuesto fijo, exclusiones y preguntas abiertas | El mantenedor crea la rama, ejecuta los checks y enlaza el PR |
| **PR** | Una rama contiene todos los archivos afectados, el diff coincide con la propuesta y los revisores reciben la revisión final | El mantenedor ejecuta los checks, obtiene la revisión del responsable, hace merge y registra la lectura posterior |

**Cuando uses ediciones del navegador, permanece en la rama de propuesta.** Después de la primera edición, vuelve a abrir cada archivo restante desde el mismo selector. Revisa el diff del PR al final. Crear cuatro ramas separadas produce cuatro cambios incompletos en vez de un paquete revisable.

## Inspeccionar el texto propuesto

**Ejemplo de redacción débil:** “Exports now remain available for thirty days.” Describe la entrega como completa y omite el alcance sintético. Usa una declaración de propuesta mientras la revisión siga pendiente.

```text
Proposed intent:
Retain synthetic export files for 30 days.
Exclude production data, backups, and legal holds.

Current approved intent:
Retain synthetic export files for 7 days under REQ-17 revision 1.

Delivery:
Not published. No runtime deletion service was tested.
```

**Compara cada archivo afectado con este texto.** La revisión del requisito avanza en el candidato. La configuración llega a treinta. La primera línea del runbook llega a treinta y conserva la limitación de laboratorio. La propuesta sigue nombrando siete como valor anterior y la revisión uno como base.

**Pregunta por las discrepancias en vez de reparar controles desconocidos.** Si el parche del mantenedor también debilita la protección o elimina una política, pide una explicación y una revisión separada. No necesitas entender cada línea del flujo para detectar un cambio fuera del alcance pedido.

## Responder a comentarios de revisión

**Revisión ilustrativa:** operaciones solicita una frase que explique que revertir la configuración no recupera los archivos eliminados. Actualiza el borrador en la misma rama y avisa a los revisores del alcance modificado. La revisión final debe referirse a la propuesta modificada, no a una copia antigua del chat.

| Comentario | Acción del colaborador |
|---|---|
| **Falta una exclusión** | Restaurar el texto y pedir revisión de intención |
| **Revisión de fuente obsoleta** | Obtener un paquete autorizado nuevo y reconciliarlo |
| **Falta el manifest** | Pedir al mantenedor que capture la base protegida |
| **Cambio de control no relacionado** | Separarlo o eliminarlo antes de revisar |
| **Afirmación de ejecución no probada** | Sustituirla por la limitación exacta del laboratorio |

**Mantén visibles las preguntas hasta recibir respuesta.** Resolver un comentario sin arreglar su causa elimina una señal útil. Enlaza la modificación o la evidencia en la respuesta para que otro revisor siga la decisión sin leer toda la conversación.

## Comprobación de finalización del navegador

**Entrega un Issue o PR que otro mantenedor pueda ejecutar sin adivinar.** Incluye el paquete de fuentes, el texto propuesto, los registros afectados, las exclusiones, los roles responsables y las preguntas sin resolver. Después de publicar, captura la lectura posterior y sepárala de la propuesta original.

**Autocomprobación:** entrega el paquete a alguien que no conozca tu chat. Pídele distinguir entre valores solicitados, aprobados y publicados. Si informa de que treinta fue entregado antes del merge, corrige las etiquetas del paquete. Lleva la misma disciplina al itinerario de trabajo.

| Puerta de revisión | Condición de aprobación |
|---|---|
| **Revisiones de fuentes** | Cada commit o versión de página declarada se abre en el sandbox. Las revisiones desconocidas quedan como faltantes. |
| **Exclusiones** | Los datos de producción, copias de seguridad y retenciones legales quedan fuera de la propuesta. |
| **Preguntas** | Las preguntas abiertas del responsable o de la fuente permanecen visibles en el Issue o PR. |
| **Vigencia de la aprobación** | Las revisiones nombran la revisión final de la propuesta. La aprobación anterior no cubre cambios posteriores. |

**Una puerta fallida mantiene la publicación pendiente.** Quienes usan Issue entregan el resultado al mantenedor. Quienes usan PR solicitan otra revisión después de corregir.

## Solución de problemas y reversión

**Sin permiso de edición:** usa un Issue o un fork aprobado. **Referencia de commit inventada:** sustitúyela por evidencia verificada y repite la revisión. **Aprobación anterior a las ediciones:** pide aprobación nueva.

**Reversión:** cierra un PR sin merge y conserva su evidencia. Para contenido ya integrado, pide al mantenedor una propuesta de reversión protegida. No cambies la base para simular una recuperación exitosa.

## Ejercicio y autocomprobación

**Oculta el registro del requisito** al nuevo asistente y pide una recomendación de publicación.

**Razonamiento esperado:** solicita evidencia autorizada o marca la respuesta como basada en una instantánea. La publicación sigue bloqueada hasta que una lectura nueva tenga éxito.

## Referencias principales

- **Pasos del navegador:** [Editar archivos](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).
- **Límite de revisión:** [Ramas protegidas](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Siguientes pasos

**Continúa con [Configuración de Confluence y Jira](/articles/ai-collaboration-confluence-jira-setup/)** para repetir el modelo operativo en sistemas de trabajo.
