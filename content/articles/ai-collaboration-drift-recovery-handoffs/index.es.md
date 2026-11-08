---
title: "Recuperación ante la deriva de agentes de IA y flujo de traspaso"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Detecta fuentes y adaptadores de políticas obsoletos, recupera publicaciones interrumpidas y verifica traspasos independientes entre agentes."
genre: ["Inteligencia artificial", "Colaboración en equipo", "Ingeniería de software"]
tags: ["curso de colaboración de IA", "deriva de fuentes", "recuperación de publicaciones", "traspaso entre agentes", "verificación de fuentes actuales", "compensación"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustración de profesionales que revisan juntos el trabajo de un proyecto en un espacio de ciberseguridad"
coverCaption: ""
---
[Volver al curso de colaboración de IA](/ai-collaboration-course-start/)

**Comprueba si hay deriva antes de las tareas y después de una publicación interrumpida.** Compara las versiones de las fuentes, las de los adaptadores y el estado de entrega en el repositorio o en el entorno aislado de trabajo. Hazlo después de completar una línea de trabajo. Así evitas que los resúmenes antiguos se conviertan en autoridad vigente y conservas un historial de recuperación verificable.

## Puntos clave

- **La deriva de fuentes** es distinta de la deriva de adaptadores.
- **Una publicación parcial** requiere un registro por sistema.
- **La recuperación** conserva el historial junto con los cambios revisados.
- **Los traspasos** requieren que otra persona lea de forma independiente las fuentes actuales.

## Antes de empezar

**Requisitos previos:** el [flujo de GitHub en el navegador](/articles/ai-collaboration-github-browser-workflow/) o el [flujo de publicación mixto](/articles/ai-collaboration-confluence-jira-publication/). **Tiempo estimado:** de 60 a 90 minutos. **Dificultad:** revisión avanzada.

**Seguridad:** usa solo registros sintéticos. Pausa la publicación automática antes de las pruebas de recuperación. No se proporciona ningún servicio de eliminación en ejecución.

**Resultado para el lector:** termina con un inventario del estado, una decisión del propietario, una reparación revisada y un traspaso que otra persona pueda reconstruir a partir de fuentes actuales. Completar el ejercicio no equivale a autorizar una publicación.

## Clasifica la deriva

| Deriva | Señal | Responsable de la reparación |
|---|---|---|
| **Requisito** | La fuente difiere del manifiesto | Propietario del producto |
| **Política** | El adaptador difiere de POL-01 | Propietario de la política |
| **Implementación** | La configuración contradice la intención | Mantenedor |
| **Runbook** | Las instrucciones contradicen el comportamiento aprobado | Responsable de operaciones |
| **Acceso** | Se deniega una fuente que antes era legible | Administrador, tarea detenida |
| **Entrega** | Marcada como terminada sin un registro completo | Responsable de entrega |

**El texto más reciente no siempre es la autoridad aprobada.** Una edición reciente no autorizada requiere investigación, no adopción automática. Resuelve el estado y quién es responsable antes de copiar valores.

## Ejecuta la comprobación previa

```text
Read MAP-01 and capture its revision.
Read POL-01 and compare active adapter versions.
Read REQ-17 and RUN-04 from mapped homes.
Read config.json at protected main.
Read frozen proposal and current role reviews.
Compare current sources with reviewed bases.
List mismatches, denied reads, and pending publications.
Stop consequential writes until owners resolve each mismatch.
```

**La persona colaboradora hace la comprobación previa antes de redactar. La persona publicadora la repite antes de escribir.** Conserva la comparación de versiones con la propuesta. Las comprobaciones semanales complementan estas lecturas, pero no las sustituyen.

**Ejemplo de deriva del adaptador:** POL-01 llega a la versión 2 mientras CLAUDE.md todavía indica la versión 1. Detente, lee el cambio de política revisado, actualiza el adaptador mediante una PR protegida e inicia una sesión nueva. Cambiar solo el número de versión sin cargar la política no corrige el contexto.

**Introduce deriva de fuentes en el laboratorio sin conexión:** extrae una copia nueva del ZIP proporcionado en un directorio temporal vacío. Desde la raíz, copia `baseline/` en `candidate/`, ejecuta `python3 check.py capture --base baseline > candidate/context.json` y después `python3 check.py validate --base baseline --candidate candidate`. Registra el primer resultado `PASS`. Abre `baseline/requirement.json` en un editor de texto y cambia únicamente `"retention_days": 7` por `"retention_days": 8`. Vuelve a ejecutar el mismo comando validate. El estado de salida esperado no es cero y el mensaje es `STALE_CONTEXT: capture the trusted base again`. Registra ambas salidas y la ruta de la fuente modificada. Elimina esta extracción temporal después de guardar las pruebas privadas y extrae una copia nueva para restablecerla. No apliques el cambio a ocho días en el repositorio publicado ni consideres la nueva captura como aprobación del propietario.

**Introduce deriva del adaptador en el repositorio temporal:** en una rama de propuesta nueva, copia en CLAUDE.md el texto aprobado del adaptador POL-01 versión 1 y etiquétalo como versión 1. En una propuesta de política independiente y revisada, describe un cambio a la versión 2 con una nueva condición de parada específica. Mantén el adaptador en la versión 1. Pide a una persona revisora que compare ambos registros y marque el adaptador como obsoleto antes de cualquier merge o ejecución del agente. Restablece la prueba cerrando las propuestas de prueba o actualizando el adaptador mediante una PR revisada. Luego abre una sesión nueva y verifica ambas versiones y la nueva condición de parada. Conserva los diff antiguos y corregidos. Esto es una prueba documental, no una simulación de rechazo de la plataforma.

## Recupera una publicación interrumpida

1. **Pausa la publicación de PROP-042** y asigna a la persona responsable de la recuperación.
2. **Lee el estado real** en todos los sistemas participantes. Distingue entre lo completado, lo fallido y lo no intentado.
3. **Pide al equipo de producto que elija** entre completar, revertir con revisión o mantener en espera.
4. **Prepara una propuesta de recuperación** con bases actualizadas y conserva el alcance y las excepciones, salvo que se revisen explícitamente.
5. **Aplica un paso revisado cada vez**, registrando y leyendo de nuevo cada resultado.
6. **Verifica el estado final** y los límites pendientes antes de reanudar el trabajo normal.

```yaml
recovery_id: RECOVERY-042
proposal_id: PROP-042
mode: awaiting-owner-choice
illustrative_state:
  requirement: thirty-days-published
  implementation: seven-days-on-main
  runbook: seven-days
  delivery: blocked
choices:
  forward: finish approved implementation and runbook
  backout: restore baseline through reviewed changes
  hold: wait for evidence or access
```

**Sustituye los estados ilustrativos por revisiones y valores observados.** Una entrada anterior del registro o una afirmación del asistente no demuestra que se haya leído el resultado.

| Opción | Cuándo usarla | Límite |
|---|---|---|
| **Completar** | La aprobación sigue vigente y las fuentes concuerdan | Requiere una verificación actualizada |
| **Revertir** | El propietario retira el cambio o falla la implementación | No recupera datos eliminados |
| **Mantener en espera** | Faltan pruebas o acceso | La entrega sigue incompleta |

**Elige mantener en espera si faltan pruebas.** Los ejercicios sintéticos no justifican sobrescrituras a ciegas. Indica el siguiente rol y las pruebas que faltan.

**La recuperación en GitHub** usa un revert o una compensación revisados. **La recuperación en Confluence** compara el historial y aplica una restauración o compensación revisada. **La recuperación en Jira** conserva el historial de la propuesta y vuelve a abrir o bloquea la entrega. Lee las revisiones resultantes en lugar de asumir que la numeración del historial se reinicia.

## Verifica un traspaso independiente

```text
Handoff: HANDOFF-042
Task: PROP-042
Map and policy: attach current approved revisions
Evidence: requirement, runbook, configuration references
Ledger: completed, failed, pending
Decision: owner choice and fixed proposal revision
Limits: no runtime deletion test or production data
Next role: accountable role
Next action: one bounded step
Stop: changed base, access denial, conflicting authority
```

**Abre otra herramienta o una sesión limpia** con el mapa y el traspaso, no con la conversación anterior. Exige nuevas lecturas de las fuentes, un manifiesto nuevo y la identificación de la acción pendiente. Las pruebas manuales del navegador siguen siendo válidas si se etiquetan como instantánea y se vuelven a comprobar antes de escribir.

**Traspaso negativo:** deniega el acceso a REQ-17. Espera un bloqueo explícito, no un valor adivinado ni un fragmento privilegiado. Restablece solo el acceso aprobado mediante administración y repite la verificación.

## Diagnostica antes de reparar

**Empieza con un inventario del estado.** «Los asistentes discrepan» describe un síntoma de la respuesta, no el problema de la fuente subyacente. Lee por separado el requisito asignado, la configuración, el runbook, la política y el registro de entrega antes de pedir a cualquiera de los asistentes que los repare.

| Observación | Diagnóstico | Primera acción |
|---|---|---|
| **Ambas fuentes coinciden, la respuesta antigua difiere** | Contexto de respuesta obsoleto | Reconstruir a partir de lecturas actuales |
| **Requisito treinta, configuración siete** | Desajuste de entrega o implementación | Revisar el paquete aprobado y el registro |
| **Adaptador uno, política dos** | Desajuste en la versión de las instrucciones | Leer el cambio de política y reparar el adaptador |
| **Fuente antes legible, ahora denegada** | Cambio de acceso | Detener la tarea y pedir una revisión autorizada |
| **Registro completo, runbook siete** | Cierre sin una lectura de retorno válida | Reabrir o bloquear la entrega e investigar |

**No trates cada desajuste como un problema del modelo.** Actualizar una sesión corrige el contexto obsoleto de la conversación. No publica un runbook, no restaura un permiso ausente ni reconcilia decisiones contradictorias de los propietarios. Nombra a la persona responsable de la reparación antes de elegir una acción en una herramienta.

## Recorre la compensación

**Interrupción ilustrativa:** REQ-17 contiene la intención aprobada de treinta días y la entrega está pendiente. La configuración y el runbook todavía indican siete. El mantenedor informa de un fallo de implementación sin resolver. El equipo de producto elige restaurar en vez de completar.

1. **Registra las versiones actuales:** requisito treinta, configuración siete, runbook siete, entrega bloqueada.
2. **Congela la propuesta pendiente:** conserva las revisiones y las pruebas del fallo de publicación.
3. **Prepara una modificación compensatoria del requisito:** restaura siete y conserva las exclusiones y notas intermedias.
4. **Obtén la revisión del propietario:** identifica la versión actual de la fuente y el texto exacto de restauración.
5. **Publica por la vía autorizada:** lee de nuevo la versión resultante del requisito.
6. **Reconcilia el registro:** todos los valores publicados aplicables son siete, el cambio original no se entregó.

**La compensación no borra el historial.** Conserva como registros separados el intento de cambio a treinta días, su fallo y la restauración posterior. La fuente final indica siete, mientras el historial de entrega explica por qué la propuesta aprobada no terminó.

```text
Recovery decision: illustrative compensation
Original proposal: PROP-042 revision 1
Observed mismatch: requirement 30, configuration/runbook 7
Owner decision: restore approved baseline intent
Review object: fixed compensation against current requirement version
Result: capture resulting revision and seven-day read-back
Original delivery: withdrawn or blocked with explanation
Limit: no runtime deletion or data restoration performed
```

**Conserva explícitamente cualquier excepción que haya añadido otra persona.** Pegar a ciegas el contenido de una página antigua puede eliminar un cambio intermedio válido. Compara el texto actual con el previsto y luego revisa una modificación compensatoria mínima respecto de la versión actual.

## Prueba un traspaso nuevo

**Usa una sesión limpia y otra persona revisora.** Proporciona el mapa, el paquete fijado, el registro y la decisión de recuperación. No compartas el chat anterior. Pide a quien recibe el traspaso que indique la intención actual, la configuración, las instrucciones operativas y la próxima acción autorizada.

```text
Read the mapped current sources independently.
Distinguish approved intent, committed configuration, and delivery state.
Compare them with the reviewed package and ledger.
List missing reads and changed bases.
Recommend one bounded next action with its accountable role.
Do not treat this handoff as approval or publication permission.
```

**Razonamiento esperado:** quien recibe verifica el resultado de la compensación antes de afirmar que se restauró la base. Si solo repite «siete días» del traspaso, no se ha probado el requisito de lectura independiente. Pide pruebas de las fuentes en lugar de otro resumen.

**Inventario didáctico completado, interrupción sintética:**

| Registro | Estado observado | Pruebas que conservar | Siguiente propietario |
|---|---|---|---|
| REQ-17 | v5 indica treinta días, excluye las copias de seguridad | Historial de la página y lectura actual | Producto |
| Configuración protegida | `main` en `base-001` indica siete días | Lectura del commit y evento de merge denegado | Mantenedor del repositorio |
| RUN-04 | v2 sigue indicando siete días | Lectura actual de la página | Operaciones |
| PROP-042 | r1 aprobada, entrega bloqueada | Revisiones fijadas y registro | Responsable de entrega |

Entrega este inventario a una segunda persona sin el chat anterior. El traspaso solo se aprueba si encuentra por su cuenta los cuatro estados, señala la exclusión de las copias de seguridad, identifica `base-001` como la revisión protegida actual y recomienda un paso de recuperación revisado por el propietario. Márcalo como fallido si hay una revisión incorrecta, una excepción omitida o una reanudación sin fundamento. Registra las referencias a las fuentes y cualquier corrección antes de escribir de nuevo.

## Decide si reanudar

| Resultado de la comprobación previa | Decisión de reanudación |
|---|---|
| **Las fuentes coinciden con la aprobación fijada** | Continúa el paso pendiente autorizado |
| **La fuente cambió fuera del alcance revisado** | Detente para comparar y solicitar una nueva revisión |
| **Falta acceso de lectura** | Mantén en espera con una persona revisora de acceso asignada |
| **Cambió la política** | Repara los adaptadores y vuelve a evaluar el permiso de la tarea |
| **Se desconoce el resultado de escritura** | Lee el destino antes de reintentar |

**Define criterios concretos para aceptar la recuperación.** Exige una lectura de retorno coincidente, un objeto de revisión vigente, un registro conciliado y un traspaso nuevo. No cierres la recuperación porque el asistente diga que el problema está resuelto.

**Comprobación de finalización:** entrega un inventario del estado observado, la decisión del propietario, la reparación revisada, la lectura final y una reconstrucción independiente. Si el acceso impide leer, documenta el bloqueo. Aplica este estándar de pruebas al proyecto final.

## Solución de problemas y reversión

**Conflictos del revert:** prepara un cambio compensatorio sobre el estado actual. **La restauración pierde excepciones:** compara toda la sección pertinente antes de escribir. **La memoria antigua controla la respuesta:** vuelve a empezar con fuentes aprobadas y elimina el contexto obsoleto del borrador.

**Reversión de la recuperación:** detente en el último estado verificado y añade otra entrada al registro. No borres eventos de auditoría nativos ni fuerces el reinicio del historial protegido. Escala al equipo de producto las cuestiones de autoridad que sigan sin resolver.

## Ejercicio y autoevaluación

**Introduce pruebas obsoletas, un adaptador de política desactualizado y una publicación parcial.** Entrega los registros a otra persona revisora sin narración y pídele que identifique quién debe reparar el problema.

**Razonamiento esperado:** producto se encarga de reconciliar los requisitos, el propietario de la política alinea el adaptador y la coordinación de recuperación de entrega coordina a los propietarios participantes. «Actualizar el contexto» no repara por completo todos los casos.

## Referencias principales

- **Controles de recuperación del repositorio:** [Ramas protegidas](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Historial de páginas:** [Documentación de Confluence](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Inspección de instrucciones:** [Memoria de Claude Code](https://code.claude.com/docs/en/memory).

## Próximos pasos

**Completa el [Retention Capstone](/articles/ai-collaboration-retention-capstone/)** con ambos recorridos y una segunda persona lectora. Muestra lecturas actuales de las fuentes, desajustes de versiones, quién decide, la recuperación revisada, la lectura de retorno y la reconstrucción independiente.
