---
title: "Flujo de publicación con IA en GitHub, Confluence y Jira"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Publica una propuesta fija de retención en Confluence, GitHub y Jira con controles de versión y recuperación ante una publicación parcial."
genre: ["Inteligencia artificial", "Colaboración en equipo", "Ingeniería de software"]
tags: ["curso de colaboración con IA", "Confluence Cloud", "Jira Cloud", "publicación entre sistemas", "control de versiones", "registro de publicación", "publicación parcial"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustración de profesionales que revisan trabajo compartido en un espacio de ciberseguridad"
coverCaption: ""
---

[Volver al curso de colaboración con IA](/ai-collaboration-course-start/)

**El colaborador congela PROP-042 antes de que los responsables lo aprueben.** Una persona encargada de publicar actualiza los requisitos en Confluence, un mantenedor de GitHub fusiona la implementación y operaciones publica el runbook. Jira registra cada paso. Hazlo después de verificar los permisos, porque los tres sistemas no forman una transacción atómica. Tu registro de publicación hace visibles las entregas incompletas.

## Puntos clave

- **La intención aprobada** difiere del comportamiento entregado.
- **Las revisiones fijas de la propuesta** vinculan la revisión a una versión.
- **Los registros de publicación** exponen el trabajo incompleto.
- **Las lecturas recientes** protegen ante cambios en las bases.

## Antes de empezar

**Requisitos previos:** la [configuración del entorno de trabajo](/articles/ai-collaboration-confluence-jira-setup/), acceso de publicación, responsables y un mantenedor del repositorio. **Tiempo estimado:** dos horas. **Dificultad:** coordinación avanzada.

**Interfaz de referencia:** lecturas en el navegador, redacción opcional en un chat aprobado y publicación por una persona. No se presupone ninguna suscripción a conectores. Antes de añadir una integración, revisa su disponibilidad en el tenant, los ámbitos, el manejo del proveedor y la correspondencia de identidades. Nunca compartas las credenciales de un responsable con un colaborador.

**Resultado para el lector:** terminarás con una propuesta fija, un registro de publicación por sistema, pruebas de lectura posterior y una decisión de recuperación para el primer paso incompleto. El ejercicio demuestra el procedimiento y el manejo de pruebas, no el comportamiento de retención en producción.

## Registrar las fuentes actuales

1. **Lee MAP-01** y luego abre REQ-17 y RUN-04 mediante los ID de página asignados.
2. **Abre el menú de la página y Page History** y registra las versiones numéricas, el estado, el texto, el responsable y las excepciones.
3. **Lee el elemento de Jira** y adjunta una exportación fija de la propuesta o un commit de GitHub. La clave por sí sola no fija las pruebas de revisión.
4. **Lee POL-01 aprobada** y la configuración base protegida.
5. **Proporciona al chat solo los extractos sintéticos necesarios**, márcalos como instantáneas y mantén deshabilitadas las acciones de escritura.

```text
Task: PROP-042, propose only
Authority: Confluence REQ-17 for intent, GitHub for behavior
Read: mapped current pages, versions, scope, exceptions
Proposal: synthetic export retention from 7 to 30 days
Output: requirement wording, config diff, runbook, ledger
Evidence: source ID and captured revision for each factual claim
Unknowns: missing access and absent runtime observations
Stop: conflict, changed base, or denied access
```

**Los paquetes sin conexión siguen basándose en instantáneas.** La persona encargada de publicar vuelve a leer las fuentes actuales antes de escribir. La denegación de acceso bloquea la publicación. Una exportación antigua no sustituye la autorización actual.

## Fijar la propuesta

```json
{
  "proposal_id": "PROP-042",
  "proposal_revision": 1,
  "requirement_base_version": 1,
  "runbook_base_version": 1,
  "policy_version": 1,
  "from_days": 7,
  "to_days": 30,
  "status": "awaiting-owner-review",
  "publication_order": ["requirement", "implementation", "runbook", "delivery"]
}
```

**Sustituye las versiones ilustrativas de las páginas por las versiones capturadas realmente.** Adjunta el JSON fijo y el texto propuesto a Jira. Cada responsable registra su función, decisión, revisión de la propuesta, versiones de las fuentes y hora de revisión. Cualquier cambio sustancial devuelve el paquete a `Review`.

**Producto revisa la intención y el alcance. Operaciones revisa la limpieza y la recuperación.** El mantenedor revisa el diff. Las reacciones a mensajes de chat mutables no son aprobaciones vinculadas a una revisión.

## Publicar y leer de nuevo

1. **Pasa Jira a `Publishing`** después de que la persona encargada de publicar verifique ambas revisiones de los responsables y que las bases de origen no hayan cambiado.
2. **Publica REQ-17** con treinta días y un campo de entrega pendiente. Registra la versión resultante, el alcance y las excepciones.
3. **Abre la PR de implementación en GitHub**, con referencia a la versión aprobada de la página. Cambia la configuración a treinta días y adjunta una instantánea del requisito sin autoridad.
4. **Fusiona tras la revisión del repositorio** y vuelve a leer **`main`**. Registra por separado el comportamiento guardado en el repositorio y el comportamiento en ejecución.
5. **Publica RUN-04**, vuelve a leerlo por ID y registra su versión resultante. La persona encargada de publicar actualiza las referencias de entrega del requisito.
6. **Completa Jira** solo cuando todos los registros coincidan y se adjunten las pruebas de la lectura final.

**Usa el validador local solo para comprobar la coherencia de las instantáneas.** Copia el requisito de Confluence anterior al cambio en el esquema JSON base del laboratorio, captura una instantánea y edita la propuesta para establecer treinta días. Usa una revisión local de instantánea incrementada y conserva por separado en Jira las versiones reales de Confluence. El flujo que toma GitHub como fuente raíz no valida Confluence en directo. No presentes su estado verde como verificación de una fuente de autoridad externa.

**No despliegues la funcionalidad de eliminación en este ejercicio.** Un servicio real requiere pruebas de despliegue, datos de prueba controlados, un mecanismo para suspender temporalmente la eliminación y pruebas de límites en ejecución. Una fusión demuestra el estado del repositorio, no el comportamiento de retención en producción.

## Registrar la publicación parcial

| Paso | Estado inicial | Prueba de finalización |
|---|---|---|
| **REQ-17** | Pending | Versión resultante de la página |
| **Configuración** | Pending | Commit fusionado y revisión |
| **RUN-04** | Pending | Versión resultante de la página |
| **Cierre de Jira** | Pending | Lectura final y transición |

**Registra cada resultado antes de intentar el paso siguiente.** PROP-042 relaciona los eventos de cada sistema. Una sola fila completada nunca significa que el cambio entero esté completo.

**Fallo ilustrativo:** Confluence publica treinta días, pero GitHub deniega la fusión. Mantén Jira en `Blocked` y el requisito marcado como entrega pendiente. Producto elige completar el cambio o restaurar a siete días tras una revisión. No conviertas una copia de emergencia del README en la fuente autorizada del requisito.

## Gestionar ediciones simultáneas

**Referencia para el navegador:** designa a una sola persona encargada de publicar durante el periodo piloto. Vuelve a abrir Page History inmediatamente antes y después de publicar. Si otra persona cambia la fuente, detente, compara, concilia y renueva la aprobación. Publicar de forma serializada es un procedimiento, no una garantía de transacción atómica.

**Extensión de API:** la documentación de Confluence v2 describe **`GET /wiki/api/v2/pages/{id}?body-format=storage`** y **`PUT /wiki/api/v2/pages/{id}`** con un objeto de versión. Una integración de publicación revisada compara la versión actual con la base aprobada, envía la siguiente versión y vuelve a leerla. Nunca actualices automáticamente una versión fallida ni reintentes un cuerpo antiguo.

**El éxito de la API por sí solo no basta.** Comprueba el contenido resultante, el ID de origen, el alcance y la versión. Este curso no incluye un cliente de API con capacidad de escritura. La publicación manual en el navegador es la referencia ejecutable para personas sin experiencia en programación.

## Verificar casos negativos

| Inyección | Razonamiento esperado |
|---|---|
| **Cambiar la fuente después de la aprobación** | Detenerse y volver a aprobar con la versión nueva |
| **Quitar el acceso de edición de la persona publicadora** | Denegar la actualización y mantener pendiente el registro |
| **Establecer Jira en sesenta días** | Detener el conflicto y conservar la autoridad de Confluence |
| **Falla la publicación del runbook** | Mantener la entrega incompleta y asignar la recuperación |

**Registra los resultados reales del sandbox** con la función del actor y las revisiones anteriores y posteriores. No incluyas el contenido protegido de la página en las pruebas de usuarios sin acceso. Los resultados esperados no son resultados medidos.

## Preparar el paquete de revisión

**Fija el contenido, no solo la etiqueta de la propuesta.** PROP-042 aparece en cada sistema, pero una etiqueta no identifica el contenido que revisó cada responsable. Incluye el texto exacto del requisito, el diff de implementación, el texto del runbook, las versiones de las fuentes y la secuencia de publicación en un único paquete fijo.

```text
Package: PROP-042 revision 1, illustrative
Intent: synthetic export retention changes from 7 to 30 days
Exclusions: production data, backups, legal holds
Requirement amendment: fixed proposed REQ-17 wording
Implementation: fixed candidate diff and protected base reference
Runbook amendment: fixed RUN-04 wording and recovery limits
Review: product and operations decisions for this package
Delivery: requirement -> implementation -> runbook -> closure
Stop: changed source, missing review, denied write, failed read-back
```

**Mantén el paquete legible para ambos responsables.** Producto necesita la intención y las exclusiones. Operaciones necesita el cambio operativo y los límites de recuperación. Ambos deben entender el periodo en que la intención aprobada y la configuración entregada difieren. Un diff de código sin más no basta para un responsable que desconoce los archivos del repositorio.

**Contenido completo del paquete para este ejemplo sintético:**

```text
REQ-17 proposed v5: "Synthetic export files are retained for 30 days from creation. This pilot excludes production data, backups, and legal holds. Delivery remains pending until the GitHub configuration and RUN-04 read-backs match this approved wording."

GitHub config.json, proposed change against base-001:
-  "retention_days": 7
+  "retention_days": 30

RUN-04 proposed v3: "Retention days: 30. Synthetic exports only. No deletion job runs in this lab. If publication fails, keep delivery pending, read back each source, and obtain owner approval before restoring the seven-day configuration or completing the thirty-day publication."
```

Estos textos son propuestas de ejemplo, no registros activos del tenant. Adjunta el commit base y las versiones de página reales antes de la revisión. El paquete fijo debe incluir todos los textos propuestos, no un resumen que obligue a un responsable a deducirlos.

**Separa la instantánea sin conexión de la publicación en directo.** Justo antes de la primera escritura, la persona encargada vuelve a comprobar las páginas asignadas y el mantenedor vuelve a comprobar la base protegida. Si cualquiera cambió, el paquete antiguo se detiene en `Review`.

## Recorrer el registro

**Progresión de estado ilustrativa:** la tabla usa revisiones didácticas, no observaciones. Completa las versiones resultantes y los commits reales después de cada escritura en el sandbox.

| Paso | Estado después de la lectura correcta | Trabajo pendiente |
|---|---|---|
| **Revisión de responsables completa** | Paquete aprobado, todos los valores publicados en siete | Todos los pasos de publicación |
| **REQ-17 publicado** | Intención en treinta, entrega pendiente | Configuración y runbook |
| **Fusión de GitHub leída de nuevo** | Intención/configuración en treinta, runbook en siete | Runbook y conciliación final |
| **RUN-04 publicado** | Todos los registros aplicables en treinta | Lectura final independiente |
| **Entrega cerrada** | Registro completo con pruebas | Las carencias de ejecución declaradas continúan |

**La entrega pendiente es un estado significativo.** Evita describir la implementación antigua como si cumpliera la nueva intención cuando la publicación sigue incompleta. Durante ese periodo, los lectores necesitan ambos valores, no un resumen único que afirme que la retención ya es de treinta días.

**Añade los intentos fallidos como eventos separados.** Si falla la escritura del runbook, conserva los resultados correctos del requisito y de la configuración. Registra la acción intentada, el fallo, la versión que no cambió, la función asignada y el siguiente paso. No restablezcas las filas completadas a Pending ni borres la secuencia observada.

**Ejemplo de rechazo por versión obsoleta:** la persona encargada lee REQ-17 v4, otra persona autorizada publica v5 y luego intenta aplicar PROP-042 r1 sobre v4. La plataforma informa de un conflicto de versión o la lectura previa a la escritura detecta v5. Registra el actor `publisher`, la versión inicial `v4`, el intento `PROP-042 r1`, el conflicto observado o el cambio de versión actual, la versión final `v5` sin cambios por este intento y la persona responsable asignada `product owner`. Mantén Jira en `Review`. Vuelve a leer v5, concilia el texto y solicita la revisión de un nuevo paquete fijo antes de escribir de nuevo. En una prueba real, usa la respuesta de la plataforma y Page History actuales. Esta fila es un ejemplo didáctico.

**Ejemplo didáctico completado, solo con valores sintéticos:**

| Sistema | Fuente inicial | Revisión fija | Escritura y lectura posterior | Estado final |
|---|---|---|---|---|
| Confluence REQ-17 | v4, siete días | PROP-042 r1, producto aprobó v4 a v5 | La persona publicadora escribió v5, el revisor volvió a abrir v5 | Treinta días, copias de seguridad y retenciones legales excluidas |
| Configuración de GitHub | Commit `main` `base-001`, siete días | PROP-042 r1, operaciones aprobó el diff candidato | PR fusionada como `merge-002`, clon independiente leyó treinta | Treinta días en la fuente protegida |
| Confluence RUN-04 | v2, siete días | PROP-042 r1, operaciones aprobó v2 a v3 | La persona publicadora escribió v3, el revisor volvió a abrir v3 | Paso operativo de treinta días con reversión |
| Jira PROP-042 | In Review | Ambas decisiones vinculadas a r1 | El responsable de entrega adjuntó pruebas y pasó a Done | Cierre tras las tres lecturas de verificación |

Las etiquetas anteriores son ilustrativas, no pruebas del tenant. Tu registro necesita enlaces nativos a las versiones de páginas y los ID de commit. Antes de pasar Jira a Done, adjunta la propuesta congelada, las dos revisiones por función, el registro de las bases de origen, cada lectura de publicación, el resultado de las pruebas negativas y las limitaciones de ejecución no resueltas. Si falta un elemento, mantén la entrega abierta o `Blocked`.

**Puerta del paquete:** marca cada una de las cinco comprobaciones como `Supported` o `Blocked`: las revisiones de las fuentes están actualizadas, ambos responsables aprobaron la misma revisión fija, todas las publicaciones necesarias coinciden con la lectura posterior, los límites de ejecución siguen explícitos y el estado de recuperación está conciliado. `Done` requiere cinco comprobaciones `Supported` y ninguna escritura no autorizada.

## Gestionar una escritura incierta

**Un timeout deja el resultado en duda.** No demuestra éxito ni fracaso. En el flujo del navegador, vuelve a abrir la fuente asignada e inspecciona su contenido e historial actuales antes de decidir si reintentas.

1. **Pausa el paso siguiente:** mantén incompleta la entrega.
2. **Lee el destino:** compara el texto actual, la versión y el alcance con el paquete fijo.
3. **Registra la observación:** completado, sin cambios, en conflicto o inaccesible.
4. **Elige el siguiente paso:** continúa desde una finalización verificada, reintenta un paso autorizado sin cambios o eleva el conflicto.
5. **Conserva la incertidumbre:** mantén el intento fallido o desconocido junto a la lectura posterior.

**No repitas toda la secuencia a ciegas.** Repetir un paso ya completado añade revisiones y arriesga sobrescribir ediciones ajenas. Reanuda desde el estado verificado. Si no hay acceso a la fuente, elige `Hold` en vez de deducir su estado a partir del registro antiguo.

## Comparar decisiones de recuperación

| Situación | Decisión que revisar | Motivo |
|---|---|---|
| **Requisito cambiado, fusión denegada** | Completar el cambio o compensar el requisito | La intención y el comportamiento difieren |
| **Configuración cambiada, runbook denegado** | Terminar el runbook o revertir la configuración | Las instrucciones operativas están desactualizadas |
| **Otro responsable cambia el alcance** | Volver a `Review` | La aprobación fija describe otro contenido |
| **Resultado de escritura desconocido** | Leer primero el destino | El reintento depende del estado observado |
| **La persona publicadora pierde el acceso** | Mantener `Hold` y solicitar administración autorizada | La autorización anterior no permite nuevas escrituras |

**Decide según el estado actual y la decisión del responsable.** Completar el cambio requiere aprobaciones actuales y controles viables. La compensación requiere revisar la restauración frente a ediciones intermedias. La recuperación es otra publicación, no una excepción privilegiada al proceso.

## Comprobación de finalización de la publicación

**Entrega un paquete que una persona revisora independiente pueda conciliar.** Debe encontrar la propuesta exacta revisada, sus bases de origen, ambas revisiones por función, cada resultado de escritura, los valores finales y las limitaciones de ejecución restantes. Pídele que identifique el primer paso incompleto tras una interrupción.

**Razonamiento esperado:** el siguiente paso se determina con fuentes recientes y el registro, no con la confianza del asistente anterior. Lleva las referencias asignadas finales a las pruebas de recuperación, donde la búsqueda debe conservar la misma distinción de autoridad.

## Solución de problemas y recuperación

**Versión cambiada:** compara el historial y renueva la revisión. **La comprobación de instantánea pasa, pero la wiki difiere:** vuelve a obtener las fuentes actuales de Confluence. **Se marcó Done demasiado pronto:** reabre el elemento mediante el flujo permitido y registra los pasos que faltan.

**Recuperación:** usa la comparación de Page History y una restauración o edición compensatoria revisada por un responsable. Registra la versión resultante, sin asumir que una restauración restablece la numeración. Revierte la configuración mediante una PR protegida si producto elige cancelar el cambio. Los archivos eliminados quedan fuera del compromiso de reversión.

## Ejercicio y autoevaluación

**Interrumpe el proceso después de publicar REQ-17** y entrega a otra persona encargada solo el mapa y el registro.

**Razonamiento esperado:** esa persona obtiene las fuentes actuales, confirma la aprobación fija y reanuda solo el paso pendiente autorizado. La falta de pruebas devuelve el trabajo a `Review`.

## Referencias principales

- **Historial y restauración:** [documentación técnica de Confluence](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Operaciones de la API con versiones:** [páginas de Confluence REST API v2](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/).
- **Controles del flujo de trabajo:** [flujos de trabajo avanzados de Jira](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).
- **Seguridad de integraciones:** [buenas prácticas de seguridad de MCP](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices).

## Próximos pasos

**Continúa con [Recuperación con prioridad en el mapa](/articles/ai-collaboration-map-first-retrieval/)** después de completar una ejecución de publicación revisada.
