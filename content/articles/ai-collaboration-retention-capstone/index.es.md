---
title: "Capstone de colaboración con IA: GitHub, Confluence y Jira"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Entrega un cambio sintético de retención mediante flujos GitHub-first y Confluence/Jira, con evidencia de fallos y revisión independiente."
genre: ["Inteligencia artificial", "Colaboración de equipos", "Ingeniería de software"]
tags: ["curso de colaboración con IA", "propuesta de retención", "revisión de GitHub", "flujo Confluence Jira", "matriz de fallos", "aceptación independiente"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustración de profesionales que revisan trabajo compartido en un espacio de ciberseguridad"
coverCaption: ""
---

[Volver al curso de colaboración con IA](/ai-collaboration-course-start/)

**Entrega PROP-042 dos veces**, primero mediante GitHub-first y después mediante GitHub con Confluence y Jira. Tú contribuyes, propietarios separados revisan y las personas autorizadas para publicar aplican el cambio. Usa sandboxes sintéticos aislados después de las lecciones anteriores. El capstone prueba el procedimiento completo, incluido el rechazo, la recuperación y la transferencia independiente, no solo la calidad del texto del asistente.

## Ideas principales

- **Un cambio compartido** compara ambos modelos de autoridad.
- **Las pruebas negativas** importan tanto como la entrega correcta.
- **Los paquetes de evidencia** respaldan la revisión independiente.
- **Completar el laboratorio** no autoriza el despliegue en producción.

## Antes de comenzar

**Requisitos:** [módulos anteriores del curso](/ai-collaboration-course-start/), acceso aprobado al sandbox y revisores separados. **Tiempo previsto:** de ocho a doce horas en varias sesiones, más la revisión independiente. El tiempo real depende de la configuración de la cuenta y las reparaciones. **Dificultad:** avanzada.

**Artefactos necesarios:** carta, mapa, política, adaptadores, línea base, manifiesto, propuesta fijada, revisiones de propietarios, libro mayor, registro de recuperación y transferencia. Los permisos dependientes del plan que falten bloquean la finalización. No se convierten en aprobaciones supuestas.

**Prepara un directorio de evidencia por pista antes de probar.** El revisor debe identificar al actor, las revisiones de origen, la acción intentada, el resultado observado y el estado final sin depender de un resumen del chat.

## Establecer dos líneas base

1. **Crea ejecuciones aisladas** llamadas GitHub-first y Mixed. Mantén separadas las revisiones y las comprobaciones.
2. **Restaura la línea base de siete días** con el procedimiento aprobado de cada pista y captura las revisiones resultantes.
3. **Verifica los controles de denegación** con cuentas de contribuyente y de usuario excluido.
4. **Captura el contexto actual** y confirma el acuerdo entre adaptador y política.
5. **Declara el alcance:** retención de treinta días para una exportación sintética, excluyendo datos reales, copias de seguridad y retenciones legales.

**PROP-042 es una etiqueta de correlación, no una aprobación reutilizable.** Cada ejecución necesita su propia revisión congelada y evidencia de origen. Incluye los identificadores de ejecución en los informes.

## Entregar con GitHub-first

**Abre el Issue y el PR candidato** siguiendo las lecciones de GitHub. Cambia juntos el requisito, la configuración, la propuesta y el runbook. Captura la base protegida, ejecuta comprobaciones confiables y obtiene las revisiones de producto y operaciones en el commit final.

```text
Run: GitHub-first
Change: synthetic retention 7 -> 30 days
Requirement: REQ-17 revision 2
Configuration: retention_days 30
Runbook: Retention days: 30
Proposal: base revision 1, from 7, to 30
Manifest: protected pre-change source hashes
Review: product and operations at final proposal revision
Publication: merged commit and read-back
Limit: no running deletion service exercised
```

**Completa las referencias reales desde el sandbox.** El esquema muestra la asignación esperada, no evidencia terminada. La persona mantenedora hace merge solo después de la revisión y luego lee **`main`** de forma independiente. Cierra el Issue después de enlazar los registros finales.

## Entregar la pista mixta

**Lee las versiones de Confluence y congela la propuesta de Jira.** Obtén las dos revisiones de propietarios. Publica el requisito con la entrega pendiente, haz merge de la configuración, publica el runbook y vuelve a leer todos los sistemas antes de marcar Done.

**Registra cada publicación** con evidencia de versión de página, commit o transición. Las copias del requisito en el repositorio son instantáneas. El comprobador local no demuestra la autoridad actual de Confluence.

| Comparación | GitHub-first | Entorno mixto |
|---|---|---|
| **Requisito** | Revisión de repositorio protegido | Publicación revisada por el propietario de Confluence |
| **Coordinación** | Issue/PR | Propuesta fijada de Jira |
| **Unidad de publicación** | Merge del repositorio | Escrituras de páginas separadas y merge |
| **Actualidad** | Commit protegido | Versiones de página más commit |
| **Recuperación** | Revert o compensación revisados | Compensación guiada por el libro mayor |

**Elige el flujo según las necesidades de propiedad.** GitHub-first reduce la coordinación entre sistemas. La pista mixta conserva los espacios de trabajo y añade comprobaciones de publicación y acceso.

## Ejecutar la matriz de fallos

| Caso | Inyección | Evidencia observada requerida |
|---|---|---|
| **Cambio aprobado** | Enviar una propuesta revisada de treinta días | Lectura coherente y revisión |
| **Contexto obsoleto** | Cambiar el origen después de capturarlo | Rechazo, conciliación y nueva aprobación |
| **Escritura no autorizada** | El contribuyente publica | Denegación y revisión sin cambios |
| **Conflicto** | Jira dice sesenta, Confluence siete | Bloqueo y conciliación del propietario |
| **Publicación parcial** | Interrumpir después de una escritura | Libro mayor pendiente y recuperación |
| **Denegación de acceso** | Retirar el acceso de lectura de la tarea | Sin texto protegido ni publicación |
| **Recuperación** | Compleción o backout aprobado | Nuevas revisiones comprobadas |
| **Transferencia** | Una sesión nueva recibe solo mapa y libro mayor | Lectura nueva y siguiente acción correcta |

**El conflicto entre sistemas pertenece a Mixed.** En GitHub-first prueba un conflicto entre la descripción del Issue y el archivo aprobado. Ejecuta los demás casos aplicables en ambas pistas. Un fallo del validador local no sustituye la evidencia de permisos en vivo.

| Caso y archivo de evidencia | Ejecución GitHub-first | Ejecución Mixed |
|---|---|---|
| **Cambio aprobado** `01-approved-change.md` | PR revisado y lectura posterior | Páginas revisadas, merge y libro mayor |
| **Contexto obsoleto** `02-stale-context.md` | Cambiar la base protegida después de capturarla | Cambiar una página de autoridad después de capturarla |
| **Escritura no autorizada** `03-unauthorized-write.md` | Denegación del push directo | Denegación de edición y transición |
| **Conflicto** `04-conflict.md` | El Issue contradice el archivo aprobado | El texto de Jira contradice Confluence |
| **Publicación parcial** `05-partial-publication.md` | Detenerse antes del merge o la lectura | Detenerse después de una página |
| **Denegación de acceso** `06-access-denial.md` | Retener una fuente protegida del repositorio | Excluir a un usuario de una página restringida |
| **Recuperación** `07-recovery.md` | Revert o compleción revisados | Compensación guiada por el libro mayor |
| **Transferencia** `08-handoff.md` | Una sesión nueva lee archivos protegidos | Una sesión nueva lee páginas y libro mayor asignados |

**Crea cada archivo antes de la prueba.** Registra el resultado esperado y observado, el rol del actor, las revisiones inicial y final, la referencia de evidencia nativa y la decisión del revisor. Mantén separadas las carpetas de las dos pistas.

**Separa los resultados esperados de los observados.** Para cada caso registra el ID de ejecución, el rol, las revisiones iniciales, la acción intentada, la expectativa, la observación, las revisiones resultantes y la decisión. Redacta credenciales e identificadores de cuenta de los informes compartidos.

## Evaluar la finalización

**La aprobación requiere evidencia observada para cada fila aplicable** y aceptación independiente. Los revisores comprueban permisos, actualidad del origen, revisión del rol, publicación parcial y reconstrucción de la transferencia.

**Falla de inmediato** ante una publicación no autorizada, texto denegado que llega al modelo o sobrescritura silenciosa de una base modificada. Mantén el trabajo bloqueado hasta que los controles corregidos pasen una repetición. No compenses estas fallas con otros resultados.

**Mide los casos completados y bloqueados, las propuestas obsoletas rechazadas, las escrituras denegadas, las recuperaciones y el tiempo del revisor.** Los resultados propuestos siguen siendo esperados hasta que se observen.

## Planificar las dos ejecuciones

**No reutilices una aprobación entre pistas.** El valor es el mismo, pero cambian los espacios de origen, las revisiones capturadas, los permisos y la secuencia de publicación. Da a cada ejecución su directorio de evidencia y paquete de revisión.

```text
capstone-evidence/
  github-first/
    charter-and-map
    captured-sources
    fixed-proposal
    role-reviews
    consistency-results
    permission-results
    publication-readback
    recovery-and-handoff
  mixed/
    same evidence categories, independently captured
```

**Estos nombres son un ejemplo organizativo**, no archivos de archivo proporcionados. Guarda la evidencia real de forma privada en el sandbox aprobado. Las entregas compartidas deben usar roles y referencias redactadas.

**Asigna un observador antes de ejecutar los fallos.** El contribuyente realiza la acción. El observador registra el estado inicial, el resultado y el estado final. Un revisor posterior decide si la evidencia respalda la afirmación. Declara el solapamiento de roles.

## Ejecutar fallos de forma aislada

**Restablece un estado revisado y verificado entre casos.** Inyectar deriva de origen, revocación de acceso y discrepancia del runbook al mismo tiempo oculta qué control rechazó la propuesta. Un fallo por ejecución ofrece una causa trazable.

1. **Captura el estado inicial:** revisiones de origen, configuración, estado de entrega y rol.
2. **Aplica una inyección sintética:** cambia una condición relevante mediante una ruta de prueba autorizada.
3. **Intenta la acción limitada:** validación, lectura, publicación o transferencia.
4. **Registra la observación:** salida real y estado de origen resultante.
5. **Repara mediante revisión:** conserva la evidencia del fallo antes de restaurar los controles.
6. **Repite el caso positivo:** confirma que el flujo corregido todavía entrega el trabajo permitido.

**Un fallo planificado sigue siendo una observación de fallo.** No llames exitosa a una publicación no autorizada porque querías probarla. La prueba expuso un defecto, pero el límite de publicación falló.

## Interpretar un resultado mixto

**Paquete de evidencia ilustrativo:** la consistencia local pasa, producto y operaciones revisan el paquete fijado, la publicación del requisito funciona y se deniega la edición del runbook. La configuración aún no se ha fusionado. Jira sigue bloqueado.

| Afirmación | Veredicto | Motivo |
|---|---|---|
| **Los registros candidatos coinciden** | Respaldado por la comprobación local | Los registros entregados pasaron las comparaciones |
| **Los propietarios aceptaron la intención y las operaciones** | Requiere revisiones nativas fijadas | Las etiquetas de rol no bastan |
| **Entrega de treinta días completada** | Sin respaldo | Las publicaciones necesarias siguen pendientes |
| **El límite funciona para cada rol** | Sin respaldo | Una denegación tiene alcance limitado |
| **El propietario de recuperación debe actuar** | Respaldado como siguiente paso | La entrega parcial necesita una decisión revisada |

**Razonamiento esperado:** mantén la ejecución incompleta, verifica las fuentes actuales y solicita la decisión del propietario correspondiente. No debilites permisos ni describas la comprobación de instantánea como evidencia de publicación en vivo.

## Revisar con un lector independiente

**Pide al revisor que reconstruya los acontecimientos**, no que lea solo tu conclusión. Debe encontrar la base aprobada, la propuesta fijada, las decisiones, las revisiones resultantes, los fallos, la reparación y las brechas restantes sin tu narración.

```text
Reviewer questions:
Which source governs retention intent in this track?
Which exact package did each owner review?
Did any source change after review?
What was published, and what remains pending?
Which denied action was observed under which role?
Did protected text reach an excluded user's context?
Which repair was reviewed and read back?
Does the fresh handoff reconstruct current state independently?
```

**Puntúa cada requisito por separado.** Usa Supported, Failed, Blocked o Not run con una referencia de evidencia. Consistencia, aprobación, permisos, recuperación y transferencia son requisitos distintos.

```text
Run ID and track:
Reviewer role and review date:
Case 01 approved change: status ___ evidence ___ gap ___
Case 02 stale context: status ___ evidence ___ gap ___
Case 03 unauthorized write: status ___ evidence ___ gap ___
Case 04 conflict: status ___ evidence ___ gap ___
Case 05 partial publication: status ___ evidence ___ gap ___
Case 06 access denial: status ___ evidence ___ gap ___
Case 07 recovery: status ___ evidence ___ gap ___
Case 08 handoff: status ___ evidence ___ gap ___
Overall decision: Supported / Failed / Blocked / Not run
Next accountable role and action:
```

**Supported significa que el revisor encontró evidencia observada para cada caso aplicable.** Registra Failed ante un control fallido, Blocked si falta acceso o control y Not run si no se intentó el caso. Conserva la referencia nativa en su archivo de evidencia.

**Puerta de aprobación del curso:** completa las pistas GitHub-first y Mixed. En cada pista, los ocho casos aplicables deben ser Supported. Un límite Failed o una lectura nativa ausente bloquea la pista. Una pista completa produce un resultado parcial documentado.

**Paquete de modelo redactado, solo ilustrativo:**

```text
Track: github-first | Run: G-01 | Reviewer: separate pilot role
Base: protected commit base-001 | Fixed proposal: PROP-042 r1
Approvals: product review ref P-01, operations review ref O-01
Consistency: local check pass, saved output ref C-01
Permission: contributor direct push denied, native event ref D-01
Publication: merged commit merge-002, fresh clone confirms thirty
Exception: backups and legal holds remain excluded
Recovery: interruption case R-01 read back and resolved through review
Handoff: second reader found current base, exception, and next action
Runtime limit: no production deletion or deployment claim
Decision: Supported for synthetic GitHub-first track only
```

Sustituye cada referencia ilustrativa por un artefacto observado del sandbox. Repite todo el paquete para Mixed con sus propias versiones y revisiones. El revisor debe rechazar una aprobación de GitHub copiada en el paquete Mixed.

## Escribir una decisión limitada

**Una decisión final útil nombra el siguiente piloto**, no un despliegue sin límites. Elige otra configuración de exportación sintética con los mismos roles y una ruta de consulta directa. Mantén los datos reales y la publicación automática fuera del alcance.

| Elemento de decisión | Detalle requerido |
|---|---|
| **Alcance** | Un cambio siguiente y sus exclusiones explícitas |
| **Evidencia** | Casos Supported y fallos sin resolver |
| **Controles** | Requisitos impuestos por la plataforma y de procedimiento por separado |
| **Propietarios** | Rol responsable de cada brecha restante |
| **Brecha de ejecución** | Comportamiento de eliminación o despliegue no probado |
| **Condiciones de parada** | Acceso ausente, autoridad cambiada, publicación no autorizada |

**Comprobación final:** ambos paquetes superan la reconstrucción independiente, los casos aplicables tienen evidencia observada y los controles pendientes siguen visibles. Si solo completas GitHub, informa de finalización parcial.

## Resolución de problemas y backout

**Solo evidencia del camino feliz:** repite las pruebas de denegación e interrupción. **Roles solapados:** decláralo y repite con usuarios separados. **Controles del plan ausentes:** detente y obtén un sandbox aprobado.

**Backout:** restaura la línea base mediante PR revisados y ediciones de Confluence, revoca integraciones temporales, archiva la evidencia de Jira y ejecuta la limpieza sintética aprobada después de conservar la evidencia. Conserva el historial de recuperación.

## Crear la decisión de despliegue

```text
Decision: another synthetic pilot, blocked, or rejected
Evidence: both run packages and failure matrix
Unenforced requirements: procedural controls listed explicitly
Provider review: input scope and retention handling
Owner coverage: product, operations, policy, repository, delivery
Production gaps: runtime tests, secrets, deployment, access review
Next action: one bounded follow-up with accountable role
Review date: assigned by pilot owners
```

**Razonamiento esperado:** el éxito sintético respalda otro piloto limitado. Producción requiere aprobaciones separadas para datos reales, despliegue, gestión del proveedor y comportamiento en ejecución. Una respuesta exitosa del asistente no autoriza el despliegue.

## Referencias principales

- **Controles del repositorio:** [Ramas protegidas](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Acceso del espacio de trabajo:** [Permisos de Confluence](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Controles de entrega:** [Esquemas de permisos de Jira](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).

## Próximos pasos

**Vuelve al [centro del curso](/ai-collaboration-course-start/)** para revisar los controles faltantes. Compara tu implementación con el [artículo del marco](/articles/one-source-many-tools-ai-collaboration-framework/) antes de elegir otro piloto.
