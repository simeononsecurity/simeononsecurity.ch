---
title: "1Password SSH Agent and CLI: Acceso de solo lectura para agentes de IA"
date: 2026-10-11
lastmod: 2026-10-28
toc: true
draft: false
description: "Diseñe un flujo de trabajo SSH de solo lectura con 1Password CLI, el SSH Agent y MCP. Utilice comandos sintéticos, permisos restringidos y aprobación humana antes de las pruebas en vivo."
genre: ["Administración de sistemas", "Seguridad en la nube", "Automatización"]
tags: ["1Password CLI", "Claves SSH", "1Password SSH Agent", "MCP", "Model Context Protocol", "Administración de agentes", "Administración de sistemas", "Bitbucket Cloud", "Git sobre SSH", "Referencias de secretos", "Cuentas de servicio", "Mínimo privilegio", "Autenticación de clave pública", "Gestión de secretos", "Seguridad de línea de comandos", "Seguridad de automatización"]
cover: "/img/cover/1password-cli-ssh-keys-mcp-agent-administration.webp"
coverAlt: "Diagrama abstracto de un agente que utiliza una referencia de secreto, un agente SSH y herramientas MCP sin mostrar claves privadas."
coverCaption: ""
---

**Un agente de línea de comandos necesita un acceso útil, no una copia de cada credencial.** Esta guía presenta un diseño acotado para 1Password CLI, el Agente SSH de 1Password, el acceso a Git de Bitbucket y el Protocolo de Contexto de Modelo (MCP). El primer flujo de trabajo utiliza nombres sintéticos, acciones de solo lectura y aprobación humana en el límite de SSH.

<!--more-->

La distinción clave es simple. **El SSH interactivo utiliza el consentimiento a través del Agente SSH de 1Password. La automatización no supervisada requiere una identidad separada, un acceso restringido y un ciclo de vida de claves diferente.** No trate una conexión MCP como permiso para ejecutar ninguno de los dos flujos de trabajo.

## Puntos clave

- **Protección de la clave privada:** El Agente SSH de 1Password realiza la autenticación SSH manteniendo las claves privadas dentro de la aplicación de 1Password.
- **Manejo de la clave pública:** Publique solo una clave pública en Bitbucket o en una cuenta remota. Mantenga la mitad privada en un elemento de Clave SSH.
- **Consentimiento interactivo:** Una persona aprueba una sesión de cliente o terminal antes de que el Agente SSH utilice una clave.
- **Separación no supervisada:** Un trabajo programado necesita una cuenta de servicio dedicada y un ámbito de bóveda restringido. Una aprobación del Agente SSH interactivo no satisface esta necesidad.
- **Límites de MCP:** MCP conecta un agente con herramientas y recursos. El cliente, el servidor, el sistema operativo y la política de 1Password siguen controlando el acceso.

## Antes de comenzar

**Prerrequisitos:** Instale 1Password 8 y 1Password CLI 2.20.0 o posterior. Inicie sesión a través de una cuenta de 1Password compatible. Utilice un cliente OpenSSH. Cree un repositorio de prueba de Bitbucket u otro destino no de producción. Mantenga disponible una segunda ruta administrativa para revertir cambios.

**Tiempo:** De 30 a 45 minutos para una revisión de diseño y una demostración sintética.

**Dificultad:** Intermedia. Necesita conocimientos básicos de Git, SSH, shell y control de acceso.

Esta guía cubre el diseño y la planificación. El artículo de Bitbucket enlazado cubre los límites de acceso específicos de Bitbucket. Esta guía no prueba una cuenta en vivo, no crea una clave real, no se conecta a un host real ni registra un servidor MCP real. Todos los identificadores a continuación son sintéticos. **Reemplace los marcadores de posición solo dentro de su propio entorno controlado.**

**Postura de versión:** Utilice 1Password 8 y [1Password CLI 2.20.0 o posterior](https://www.1password.dev/ssh/manage-keys) para este flujo de trabajo. [1Password CLI 1 está deprecado](https://www.1password.dev/cli/upgrade/). [1Password 7 se retirará a principios de 2027](https://support.1password.com/add-account/). La generación, importación y compartición de claves SSH requieren 1Password 8. Confirme las versiones de Git, OpenSSH, host MCP y servidor MCP instalados antes de probar. Los ejemplos a continuación siguen sin probarse.

Un **vault** (bóveda) es una colección protegida de elementos de 1Password. **OpenSSH** es el software de cliente y servidor SSH utilizado por muchos sistemas operativos. **MCP**, o Model Context Protocol, conecta a un agente con herramientas o recursos aprobados.

## Por qué mantener las claves privadas sin leer

Un par de claves SSH tiene una clave pública y una clave privada. Un servicio Git remoto o un servidor almacena la clave pública. El cliente demuestra la posesión de la clave privada durante la autenticación. La clave privada no necesita viajar al servicio remoto.

El [1Password SSH Agent](https://www.1password.dev/ssh/agent) extiende este modelo. Su documentación indica que los clientes SSH y Git se autentican a través del agente mientras la clave privada permanece en la aplicación de 1Password. El cliente recibe un resultado de firma, no un archivo de clave privada.

Esta frontera reduce varias vías de exposición:

- **Control de versiones:** Una clave privada no entra en un repositorio ni en una solicitud de extracción (pull request).
- **Historial de shell:** Un valor de clave privada no aparece en un argumento de comando.
- **Archivos temporales:** Un guion no necesita escribir una clave privada en `~/.ssh/`.
- **Contexto del agente:** Un modelo de lenguaje grande (LLM) no necesita el texto de la clave privada para solicitar una operación SSH.
- **Reutilización accidental:** Una clave copiada no permanece en un espacio de trabajo antiguo después de que termina una tarea.

La frontera no hace que SSH sea inofensivo. Un proceso con permiso para usar el socket del agente podría realizar acciones como la clave aprobada. La verificación de claves de host, los límites de cuentas remotas, los permisos del repositorio, la política de comandos y el aislamiento de procesos siguen siendo importantes.

*La frontera de la clave privada protege el material de la clave. La frontera no aprueba un comando remoto ni demuestra que el host de destino sea de confianza.*

## Consentimiento SSH interactivo

Configure una bóveda dedicada para claves de agente. Use el archivo de configuración del SSH Agent para seleccionar el conjunto de claves más pequeño y una clave específica para el host. No exponga todas las claves elegibles de todas las bóvedas integradas a un proceso de automatización.

El [modelo de seguridad de 1Password SSH Agent](https://www.1password.dev/ssh/agent/security) vincula la aprobación a una clave y a un proceso solicitante. El prompt identifica el proceso y la clave. La persona luego aprueba la solicitud a través del método de autenticación configurado.

1Password documenta varios alcances de aprobación. La aprobación por clave y por aplicación es el valor predeterminado. Un alcance de sesión de terminal limita la aprobación a una pestaña o sesión. La aprobación por solicitud vuelve a preguntar por cada solicitud. Existe una opción de aprobación para todos los procesos, pero esta opción otorga a todos los procesos bajo el usuario del sistema operativo actual acceso para la sesión.

**Utilice el alcance de aprobación más estrecho adecuado para la tarea.** Un agente de administración de sistemas debe ejecutarse en una terminal dedicada o en un entorno aislado (sandbox). No apruebe cada proceso cuando una única sesión de terminal sea suficiente.

La sesión de aprobación no es una concesión permanente. 1Password registra la autorización durante el período configurado o hasta que la aplicación se bloquee o se cierre. Cuando la aplicación está bloqueada, el agente no retiene las claves privadas para su uso posterior. El proceso SSH Agent continúa en segundo plano mientras 1Password está cerrado si la configuración compatible está habilitada, pero una nueva solicitud de firma requiere que 1Password esté desbloqueado.

La [guía de configuración de SSH de 1Password](https://www.1password.dev/ssh/get-started) muestra el flujo general: generar o importar una clave, publicar la clave pública, habilitar el SSH Agent, configurar el cliente SSH, ejecutar un comando SSH o Git y aprobar la solicitud. La ruta exacta del socket varía según el sistema operativo. Utilice las instrucciones de la plataforma actual en lugar de copiar una ruta de otra máquina.

La aplicación 1Password debe estar desbloqueada antes de que una nueva solicitud de firma tenga éxito. El proceso del agente podría continuar en segundo plano mientras la aplicación está cerrada. Una aplicación bloqueada no libera el material de la clave privada para la firma.

## Claves públicas y Bitbucket

La [guía de gestión de claves de 1Password](https://www.1password.dev/ssh/manage-keys) documenta elementos de SSH Key, generación de claves, importación de claves, claves públicas, huellas digitales y claves privadas. El ejemplo de CLI utiliza `op item create --category ssh` para crear un elemento de SSH Key. 1Password CLI genera una clave Ed25519 de forma predeterminada para este ejemplo y oculta la clave privada en su salida.

Bitbucket Cloud utiliza el flujo de trabajo de línea de comandos normal de Git y OpenSSH. Su [guía de línea de comandos](https://support.atlassian.com/bitbucket-cloud/docs/find-the-command-line/) describe las operaciones de Git desde un repositorio local. Su [guía de configuración SSH](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) enumera las formas remotas SSH y los formatos de clave pública admitidos.

**Trate Bitbucket como el consumidor de la clave pública.** Registre la clave pública o la huella digital a través de la cuenta de Bitbucket aprobada o la configuración del repositorio. Mantenga la clave privada en 1Password. El cliente Git solicita al SSH Agent que firme. El cliente no lee un archivo de clave privada.

Para el alcance de la clave de acceso de Bitbucket, la ruta de registro y la prueba de Git de solo lectura, consulte [Bitbucket Cloud SSH Keys and Git CLI: Read-Only Access for AI Agents](/articles/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation/).

La documentación de Bitbucket denomina a esto un flujo de trabajo de Git CLI. Este artículo no asume un servidor MCP de Bitbucket separado ni un producto llamado Bitbucket CLI. Una CLI específica de Bitbucket requiere su propia documentación actual y su propia revisión de permisos.

## El límite entre el Agente y MCP

Utilice la especificación actual de MCP](https://modelcontextprotocol.io/specification/2026-07-28) al revisar un nuevo servidor.

La URL de la especificación del 18-06-2025 en el siguiente párrafo de contexto es una versión histórica. Utilice la especificación del 28-07-2026 para nuevas revisiones.

[MCP](https://modelcontextprotocol.io/specification/2025-06-18) estandariza las conexiones entre una aplicación de LLM, un conector de cliente y un servidor. Un servidor ofrece herramientas, recursos o indicaciones (prompts). La especificación también establece que los hosts deben obtener el consentimiento del usuario antes de exponer datos o invocar herramientas.

**MCP en sí mismo no otorga permisos.** Una herramienta de MCP sigue ejecutándose dentro de los permisos de su proceso de servidor, usuario del sistema operativo, ruta de red, cuenta de nube y credenciales configuradas. Una descripción de herramienta no es una política de autorización.

La [documentación de Seguridad de 1Password para AI](https://www.1password.dev/security-for-ai) describe un Servidor MCP de Entornos y patrones de configuración segura de MCP. La misma página describe la carga en tiempo de ejecución de valores de configuración de MCP desde 1Password. Estas páginas no definen un producto MCP de claves SSH de 1Password genérico ni un flujo de trabajo SSH universal para cada cliente de agente.

Utilice MCP como una superficie de control estrecha:

- **Herramientas de lectura:** Inspeccionar el estado del servicio, metadatos del repositorio o registros aprobados.
- **Herramientas de planificación:** Preparar un comando o registro de cambios sin ejecutar el comando.
- **Herramientas de aprobación:** Solicitar una decisión humana antes de una escritura remota.
- **Herramientas de escritura:** Mantenerlas deshabilitadas hasta que el destino, el comando, el alcance y el plan de reversión sean explícitos.

El agente debe recibir referencias, metadatos y resultados de operaciones. **El agente no debe recibir texto de claves privadas, una volcado de elementos de todo el bóveda o una shell sin restricciones.**

## Una Política Inicial Segura

Comience con una política escrita antes de habilitar un agente. Mantenga la política cerca de la configuración de MCP, pero no coloque credenciales en el archivo.

```yaml
agent_policy:
  purpose: "Read-only repository and system inspection"
  identities:
    interactive_ssh: "1Password SSH Agent with per-terminal consent"
    unattended_jobs: "Dedicated service account with one narrow vault"
  allowed:
    - "Read repository metadata through Git"
    - "Read approved service status and logs"
    - "Run one synthetic SSH connectivity check"
  approval_required:
    - "Any remote write"
    - "Any package, firewall, clock, or service change"
    - "Any new host-key acceptance"
    - "Any private-key export"
  denied:
    - "Read or print private-key fields"
    - "List every vault or every item"
    - "Write tokens or secrets to shell profiles"
    - "Run arbitrary commands from tool output"
  rollback:
    - "Revoke the service account"
    - "Remove the public key from the target"
    - "Disable the MCP server entry"
    - "Lock 1Password and end the agent session"
```

Esta política es un ejemplo, no un formato de configuración de 1Password. Almacene la política real en el plano de control utilizado por su cliente de agente. Revise cada herramienta contra la política antes de habilitar cada herramienta.

## Cuentas de Servicio y Referencias de Secretos

Una **cuenta de servicio** otorga a un proceso automatizado su propia identidad. La [guía de scripts de la CLI de 1Password](https://www.1password.dev/cli/secrets-scripts) recomienda cuentas de servicio para el acceso con privilegios mínimos a bóvedas seleccionadas. Esto separa un trabajo no supervisado del SSO, MFA, inventario de bóvedas y cuenta diaria de una persona.

Una **referencia secreta** nombra un valor sin colocar el valor en el código fuente. La [referencia de la CLI de 1Password](https://www.1password.dev/cli/reference) utiliza la forma `op://vault/item/field`. La referencia es segura de almacenar solo cuando el proceso circundante aún tiene un acceso restringido. Una referencia no elude la política.

Use `op read` cuando un comando necesite un valor. Use `op run` cuando un proceso hijo necesite un conjunto controlado de valores de tiempo de ejecución. Use `op item create` cuando un nuevo elemento de clave SSH deba existir en la bóveda aprobada.

No confunda la inyección en tiempo de ejecución con la protección de claves privadas. Un token de API pasado como variable de entorno sigue siendo visible para el proceso hijo. Una clave privada pasada a través de una variable de entorno es peor porque el valor expande la exposición a la inspección de procesos, informes de errores, salida de depuración, trazado de shell y registro accidental.

**Prefiera una referencia en el código fuente y un valor en tiempo de ejecución en el proceso más pequeño posible.** Mantenga el proceso de vida corta. Desactive el trazado de shell. No imprima el entorno. Elimine los archivos temporales después de una ejecución fallida.

## Flujo de trabajo inicial seguro

La secuencia siguiente separa el registro de la clave pública, SSH interactivo, el descubrimiento de MCP y el diseño no supervisado.

### 1. Definir el objetivo

Anote la clase de objetivo, la cuenta remota, el repositorio o comando previsto, la fuente de la clave del host, el propietario de la aprobación y la acción de reversión. Use un registro sintético durante el primer ejercicio.

```text
target_class: test-repository
remote_account: git
operation: read-only connectivity check
host_key_source: approved administrator record
approval_owner: named operator
rollback: remove public key and revoke test identity
```

**Resultado esperado, sin probar:** El registro identifica un objetivo y una operación. El registro no contiene un nombre de host, dirección IP, token, clave privada o datos personales.

### 2. Crear o seleccionar el elemento de clave SSH

La [guía oficial de claves SSH de 1Password](https://www.1password.dev/ssh/manage-keys) documenta el patrón de creación de la CLI. El comando siguiente utiliza un título sintético y una bóveda de prueba nombrada.

```bash
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
```

**Salida esperada, sin probar:** 1Password crea un elemento de clave SSH en la bóveda de prueba nombrada y oculta la clave privada en la salida de la terminal. El comando cambia el estado de 1Password. La salida legible por humanos exacta depende de la versión de la CLI y del estado de inicio de sesión.

Capture el identificador de elemento devuelto en el registro de prueba sin copiar el campo de la clave privada. Use el identificador o el título exacto del elemento para lecturas específicas de campo posteriores solo después de confirmar el esquema del elemento.

No redirija esta salida a un registro compartido. Capture solo el identificador del elemento, la huella digital de la clave pública y el registro de aprobación cuando el procedimiento local admita una salida estructurada segura.

### 3. Manejar la clave pública

Abra el elemento de clave SSH en 1Password y use su acción Copiar clave pública. Utilice una referencia específica de campo solo después de confirmar la etiqueta del campo de clave pública en su propia cuenta. No descargue el elemento completo.

```bash
PUBLIC_KEY_REF="op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
op read "$PUBLIC_KEY_REF"
```

**Salida esperada, sin probar:** Una línea sintética de clave pública OpenSSH o un valor de clave pública del campo confirmado. El nombre de campo de marcador de posición anterior no es una promesa sobre la etiqueta del campo de su elemento.

Registre la clave pública en la cuenta de Bitbucket aprobada, el repositorio de Bitbucket o la cuenta remota. Nunca pegue la clave privada correspondiente en Bitbucket. La [guía de SSH de Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) también recomienda registrar la clave de host de Bitbucket antes de la primera conexión.

Para Bitbucket, obtenga el registro de clave de host publicado y compare el registro con una copia de confianza independiente antes de agregar una línea a `~/.ssh/known_hosts`. Use la verificación estricta de host después de que la comparación sea exitosa. No acepte una clave de host modificada durante la ejecución de un agente.

### 4. Habilitar SSH interactivo

Active el Agente SSH de 1Password en la aplicación de escritorio. Configure OpenSSH con el valor específico de la plataforma `IdentityAgent` o `SSH_AUTH_SOCK` de la [guía de configuración oficial](https://www.1password.dev/ssh/get-started). Limite la primera prueba a un solo repositorio o a una cuenta no de producción.

En macOS o Linux, configure el socket desde la guía de configuración de la plataforma y ejecute `ssh-add -l`. En Windows, use la configuración de tubería nombrada admitida y verifique las claves disponibles a través de la interfaz del Agente SSH de 1Password o una prueba de SSH de Windows documentada. No presente `ssh-add -l` como un comando de verificación multiplataforma.

Solo en macOS o Linux:

```bash
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**Salida esperada, sin probar:** En macOS o Linux, `ssh-add -l` enumera las huellas dactilares del agente activo. En Windows, use la prueba de tubería nombrada documentada o la interfaz del Agente SSH de 1Password. Una lectura exitosa de Git devuelve una referencia de commit. El marcador de posición del repositorio anterior requiere reemplazo en una prueba controlada.

El comando utiliza un marcador de posición de repositorio. Reemplace el marcador de posición solo en una prueba controlada. **No apruebe un aviso para un destino o proceso que no esperaba.**

### 5. Agregar MCP después de que la ruta SSH funcione

Primero verifique el cliente SSH y el destino sin MCP. Luego agregue un solo servidor MCP de solo lectura o un conector local. Proporcione al agente una herramienta como `read_status` o `prepare_command`. No comience con una herramienta de shell general.

La configuración de MCP debe hacer referencia a los valores de tiempo de ejecución a través del mecanismo de entorno admitido por el cliente. La [guía de seguridad de IA de 1Password](https://www.1password.dev/security-for-ai) describe cómo reemplazar los tokens de configuración de MCP en texto plano con variables de entorno cargadas desde 1Password. **Mantenga la referencia o el nombre de la variable en la configuración. Mantenga el valor resuelto fuera del transcurso del agente.**

Esta sección describe un diseño, no una configuración de MCP probada. Aquí no se fija ningún cliente, servidor, transporte, versión o fixture. Valide un servidor de solo lectura en un perfil de prueba separado antes de conectar un agente a un sistema de producción.

### 6. Registrar el resultado

Registre la clase objetivo, el nombre de la herramienta, la decisión de aprobación, la huella digital de la clave pública, el resultado del comando y el resultado de la limpieza. Omita los valores secretos. Marque cada salida como observada o esperada.

**Resultado esperado, no probado:** El agente lee el estado, propone un comando acotado, recibe aprobación explícita para la solicitud SSH, completa la operación de solo lectura y produce un registro sin texto de clave privada.

## Secuencia de comandos sintética

La siguiente secuencia muestra el orden sin utilizar infraestructura real. Estos comandos son solo ejemplos. No se ejecutaron durante la preparación del artículo.

```bash
op --version
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
op read "op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
# macOS or Linux only
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**Salida esperada, no probada:**

```text
2.x.y
SSH Key item created. Private key: redacted
ssh-ed25519 AAAA<synthetic-public-key> synthetic-key-label
256 SHA256:<synthetic-fingerprint> synthetic-agent-admin-key (ED25519)
<synthetic-commit-id>        HEAD
```

El bloque de salida es ilustrativo. El bloque no representa una ejecución contra una cuenta de 1Password, Bitbucket, un proveedor de Git o un host remoto. Un registro de producción debe almacenar solo metadatos aprobados y un estado de éxito o fallo.

## Acceso interactivo versus no atendido

| Modo de acceso | Identidad | Ruta de la clave privada | Modelo de aprobación |
|---|---|---|---|
| **SSH interactivo** | Cuenta humana a través de 1Password SSH Agent | La clave privada permanece en la aplicación de 1Password | Un humano aprueba un proceso, una sesión de terminal o una solicitud |
| **Lectura programada** | Cuenta de servicio dedicada | `op run` proporciona valores de tiempo de ejecución acotados | Política de trabajo y alcance de la cuenta de servicio |
| **SSH programado** | Identidad de automatización dedicada | La exportación de la clave sigue siendo un diseño de último recurso | Aislamiento del trabajo, vida útil corta, restricción de host y rotación |
| **Escritura del agente** | Identidad humana o específica de la tarea | Depende de la integración aprobada | Aprobación humana antes de cada cambio definido |

*No programe un flujo de trabajo alrededor de un prompt del Agente SSH interactivo. Utilice un diseño de automatización separado o mantenga el paso operado por un humano.*

Para trabajos no supervisados, cree una cuenta de servicio con acceso a un solo bóveda o a un conjunto pequeño de elementos. Asigne al trabajo un único propósito. Utilice un repositorio o una cuenta de servidor dedicada. Agregue la verificación de claves de host. Establezca un tiempo de espera de ejecución. Registre los metadatos de las acciones sin incluir secretos. Rote o revogue la identidad después de la prueba.

Si un trabajo no supervisado realmente necesita una clave privada SSH, utilice una clave de automatización dedicada con una cuenta remota limitada y una fecha de finalización documentada. La obtención de la clave privada mediante `op read` aún exporta el material de la clave a través de un límite de proceso. Este diseño tiene un radio de impacto mayor que el Agente SSH de 1Password. Prefiera una identidad de plataforma, un servicio de despliegue u otra identidad de carga de trabajo cuando el destino lo soporte.

## Por qué las variables de entorno en texto plano aumentan el riesgo

Las variables de entorno mantienen los secretos fuera de los archivos de código fuente, pero no los hacen invisibles. Un proceso hijo lee su entorno. La inspección de procesos, los manejadores de errores, la salida de depuración, la trazabilidad de la shell y los registros de comandos copiados podrían exponer los valores.

1Password documenta `op run` como un método de tiempo de ejecución para cargar referencias en un subproceso. Utilice `op run` para los valores que un proceso realmente necesita. Mantenga el proceso hijo de vida corta y restrinja su comando. No pase una clave privada a través de `SSH_PRIVATE_KEY`, `KEY` o una variable similar cuando el Agente SSH elimine la necesidad de exportación.

El orden más seguro es:

1. **Utilice el Agente SSH** para SSH interactivo.
2. **Utilice el registro de clave pública** para Bitbucket o la cuenta remota.
3. **Utilice `op run`** para un proceso hijo no supervisado limitado.
4. **Utilice `op read`** para un solo valor cuando un proceso hijo no necesite un entorno completo.
5. **Exporte una clave privada** solo después de una excepción por escrito, un alcance limitado, un plan de limpieza y un plan de rotación.

## Tabla de decisiones

| Necesidad | Ruta preferida | Razón para detener o rediseñar |
|---|---|---|
| Un humano ejecuta Git sobre SSH | 1Password SSH Agent | Detener si el mensaje de confirmación menciona un proceso o una clave inesperados |
| Registrar una clave de repositorio | Leer o autocompletar la clave pública | Nunca copiar la clave privada en el servicio de repositorios |
| El agente lee el estado del servicio | Herramienta MCP de solo lectura con alcance a nivel de SO | Detener si la herramienta expone una shell sin restricciones |
| El agente propone un cambio remoto | Herramienta de planificación seguida de aprobación humana | Detener si el destino, el comando o la reversión no están claros |
| Un trabajo lee un token de API | Cuenta de servicio más `op read` o `op run` | Detener si el token entra en el código fuente, los registros o un perfil global |
| Un trabajo necesita acceso SSH | Identidad de carga de trabajo o clave de automatización dedicada | Detener si el trabajo requiere una clave personal o una cuenta amplia |
| La configuración MCP necesita un token | Referencia de tiempo de ejecución cargada por el cliente compatible | Detener si un token en texto plano se commitea en la configuración |

## Manejo de fallos

**Solicitud de consentimiento SSH inesperada:** Denegar la solicitud. Verificar el nombre del proceso, la sesión de terminal, la huella digital de la clave, el destino del repositorio y la clave del host. Revisar la configuración del cliente SSH antes de reintentar.

**No hay socket de SSH Agent:** Confirmar que la aplicación de escritorio de 1Password está instalada mediante un método compatible, que el SSH Agent está habilitado y que el cliente utiliza el socket específico de la plataforma. La [página oficial de SSH Agent](https://www.1password.dev/ssh/agent) enumera los requisitos del sistema operativo y los enlaces de configuración del socket.

**Falla la autenticación de clave pública:** Verificar la clave pública seleccionada, la cuenta remota, el permiso del repositorio, la clave del host y la configuración SSH. Utilizar una comparación de huella digital pública. No resolver el error exportando una clave privada no relacionada.

**`op read` deniega el acceso:** Verificar el alcance del bóveda de la cuenta de servicio, el identificador del elemento, la referencia del campo, el estado de inicio de sesión y el estado del elemento. Reducir la referencia a un único elemento aprobado. No ampliar la concesión de la bóveda como primera respuesta.

**`op run` expone un valor:** Detener el trabajo. Conservar solo el registro mínimo del incidente. Eliminar los registros copiados y los archivos temporales según su procedimiento de retención. Rotar el secreto o la clave afectada. Revisar la trazabilidad de la shell, la inspección de procesos, los informes de errores y la retención de transcripciones MCP.

**La herramienta MCP se comporta de manera inesperada:** Trate la salida de la herramienta como datos no confiables. Deténgase antes de ejecutar comandos sugeridos por la salida. Inspeccione el código fuente del servidor, la configuración, los permisos y el transporte. El host MCP debe obtener el consentimiento del usuario. La especificación también proporciona orientación para los implementadores sobre el consentimiento y los controles de acceso, pero el protocolo no reemplaza su revisión.

## Reversión y eliminación

La reversión comienza con la eliminación del acceso, no con la eliminación de archivos.

1. **Detenga el agente o el trabajo programado.** Desactive la entrada del servidor MCP o desconecte el cliente.
2. **Bloquee 1Password.** Termine la sesión interactiva de autorización SSH.
3. **Elimine la clave pública.** Elimine la clave de prueba de Bitbucket, el repositorio o la cuenta remota.
4. **Revogue la cuenta de servicio.** Elimine su acceso al bóveda e invalide su token.
5. **Elimine el elemento de Clave SSH de prueba** después de confirmar que ningún flujo de trabajo aprobado utiliza el elemento.
6. **Elimine la configuración temporal.** Elimine las referencias de prueba, las sobrescripciones de sockets locales y los registros generados.
7. **Revise las pruebas.** Confirme que el registro de reversión no contenga ninguna clave privada, token o volcado de entorno.

*La eliminación de un archivo local no revoca una clave pública, una cuenta de servicio, un token en caché o una autorización remota. Elimine cada concesión en su origen.*

## Solución de problemas

### El agente solicita una clave en cada comando

Verifique el alcance de autorización seleccionado. La aprobación por solicitud es más restrictiva. Es posible que una sesión de terminal o aplicación haya terminado. 1Password también vuelve a solicitarla después de un evento de bloqueo o salida.

### El agente ve una clave privada en su transcripción

Detenga el flujo de trabajo y rote la clave. Inspeccione la respuesta del servidor MCP, el comando de shell, el registro de depuración y el envoltorio de la herramienta. Reemplace las lecturas de claves privadas con el uso de SSH Agent para tareas interactivas. Para los trabajos, reemplace una clave personal con una identidad dedicada y una excepción documentada.

### Una lista de claves contiene demasiadas identidades

El Agente SSH de 1Password expone las claves elegibles de sus bóvedas configuradas. Use una configuración de agente con alcance limitado o una configuración SSH específica del host. La [documentación del agente](https://www.1password.dev/ssh/agent) también señala el límite de seis claves del servidor OpenSSH.

### Un comando funciona manualmente pero falla en un trabajo

Compare la identidad, el alcance de la bóveda, el entorno, los datos de la clave del host, el directorio de trabajo y los supuestos de aprobación. Una sesión interactiva de 1Password incluye el consentimiento humano. Un trabajo programado no lo incluye. Diseñe el trabajo como un modo de acceso separado.

### El servidor MCP está conectado pero la tarea falla

La conexión no demuestra la autorización. Verifique el descubrimiento de herramientas, las credenciales del servidor, el consentimiento del cliente, los permisos del sistema operativo, el acceso a la red y los permisos del lado del destino en pasos separados. Mantenga la primera prueba solo de lectura.

## Próximos pasos

Utilice la especificación MCP actual del 2026-07-28 para nuevas aprobaciones. Cualquier enlace a la especificación del 2025-06-18 en este artículo es contexto histórico.

Comience con un repositorio sintético y una herramienta MCP solo de lectura. Registre cada resultado esperado como no probado hasta que un entorno controlado produzca evidencia. Luego, repita el flujo de trabajo con un destino no de producción, un operador designado, una clave de host verificada y un registro escrito de reversión.

Lea la [referencia de la CLI de 1Password](https://www.1password.dev/cli/reference) para las opciones de comando actuales. Lea [Cargar secretos en scripts](https://www.1password.dev/cli/secrets-scripts) antes de crear automatización de cuentas de servicio. Lea la [especificación MCP](https://modelcontextprotocol.io/specification/2026-07-28) antes de aprobar herramientas de un servidor nuevo.

**Mantenga SSH interactivo aprobado por humanos. Mantenga el acceso no supervisado separado. Mantenga las claves privadas no legibles siempre que el destino admita autenticación basada en agentes.**
