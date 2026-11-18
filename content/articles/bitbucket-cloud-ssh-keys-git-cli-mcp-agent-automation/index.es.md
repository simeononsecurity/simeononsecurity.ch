---
title: "Claves SSH de Bitbucket Cloud: acceso Git de solo lectura para agentes de IA"
date: 2026-10-11
lastmod: 2026-11-13
toc: true
draft: false
description: "Configure claves SSH de Bitbucket Cloud, acceso Git CLI, tokens REST API, 1Password y herramientas MCP para flujos de trabajo de agentes de IA de solo lectura."
genre: ["Seguridad en la nube", "Herramientas para desarrolladores", "Administración de sistemas"]
tags: ["Bitbucket Cloud", "claves SSH de Bitbucket", "claves de acceso al repositorio", "claves de acceso al proyecto", "claves de acceso al espacio de trabajo", "Git CLI", "Bitbucket CLI", "1Password CLI", "1Password SSH Agent", "MCP", "Model Context Protocol", "REST API", "alcances de tokens API", "permisos de agentes", "automatización de solo lectura", "claves de host SSH"]
cover: "/img/cover/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation.webp"
coverAlt: "Flujo de trabajo en terminal que conecta el acceso Git de Bitbucket Cloud, claves SSH con alcance limitado, 1Password, lecturas REST API y herramientas MCP"
coverCaption: ""
---

**Un flujo de trabajo de agente acotado separa la lectura del repositorio, las lecturas de API, el manejo de secretos y las escrituras remotas.** Use Git mediante Secure Shell (SSH) para acceder al código fuente, una clave de acceso de Bitbucket de solo lectura para las descargas automatizadas, REST API para los metadatos y un servidor de Model Context Protocol (MCP) para las herramientas aprobadas. Guarde las claves privadas y los tokens API en 1Password. Exija aprobación humana para las escrituras.

<!--more-->

## Puntos clave

- **Solo lectura por defecto:** use una clave de acceso al repositorio o al proyecto para que el agente obtenga el código. Ninguna permite hacer push.
- **Identidad personal:** use una clave SSH personal para el trabajo interactivo vinculado a una cuenta de usuario.
- **Custodia de secretos:** use 1Password SSH Agent para que Git solicite una firma autorizada sin leer la clave privada.
- **Qué significa CLI:** considere `git`, `curl` y un pequeño wrapper de API auditado como la línea de comandos práctica de Bitbucket.
- **Límite de MCP:** exponga herramientas de lectura con alcance limitado. Desactive las herramientas de escritura o colóquelas tras una aprobación independiente.
- **Control de escritura:** permita que el agente inspeccione, compare y prepare un cambio. Exija que una persona apruebe un push, pull request, merge o cambio de configuración.

## Antes de empezar

**Requisitos previos:** acceso a Bitbucket Cloud, Git, un cliente OpenSSH, 1Password 8, 1Password CLI, una CLI con sesión iniciada o una cuenta de servicio aprobada y un host MCP con controles de aprobación de servidores. Reserve 45 minutos. Nivel intermedio.

Use un repositorio de prueba para la primera ejecución. Sustituya todos los marcadores de posición de los ejemplos. Los comandos siguientes son ejemplos no probados. No representan una cuenta ni un repositorio activo de Bitbucket.

**Versiones:** este artículo ofrece orientación de diseño, no un procedimiento fijado a versiones. Confirme las versiones instaladas de Git, OpenSSH, 1Password CLI, Teamwork Graph CLI, el host MCP y el servidor MCP antes de probar. Configure 1Password SSH Agent para el sistema operativo actual antes de usar `ssh-add -l`.

**Mantenga las credenciales fuera de shells, registros, URL, remotos de Git y archivos fuente.** Use marcadores como `<workspace>`, `<repository>`, `<api-token>` y `<socket-path>`. No pegue una clave privada real en una transcripción de terminal.

## Elegir el límite de acceso

Bitbucket Cloud admite claves de acceso a nivel de repositorio, proyecto y espacio de trabajo. El alcance cambia el impacto de copiar una clave. La [comparación oficial de claves de acceso](https://support.atlassian.com/bitbucket-cloud/kb/difference-between-repository-project-and-workspace-access-keys/) explica directamente las diferencias de permisos.

| Vía de acceso | Alcance | Permite escribir | Uso adecuado |
|---|---|---:|---|
| **Clave de acceso al repositorio** | Un repositorio | No | Descarga estándar para un agente |
| **Clave de acceso al proyecto** | Repositorios de un proyecto | No | Tareas de solo lectura en un grupo pequeño de repositorios |
| **Clave de acceso al espacio de trabajo** | Repositorios de un espacio de trabajo | Sí | Automatización de servicio controlada con un plan de escritura separado |
| **Clave SSH personal** | Repositorios permitidos para un usuario | Sigue la cuenta del usuario | Administración interactiva |
| **Token API** | Alcances API basados en usuario y acceso de la cuenta | Depende de los alcances | Lecturas REST API o una tarea de escritura temporal |

**Empiece por el límite útil más pequeño.** Elija una clave de repositorio si basta con uno. Elija una clave de proyecto si varios repositorios comparten proyecto y el acceso de solo lectura basta. Trate la clave del espacio de trabajo como una identidad de escritura, no como opción predeterminada.

Cree y registre la clave más limitada mediante la ruta correspondiente de configuración de Bitbucket:

1. Abra Repository settings, Access keys y Add key para un repositorio. Pegue la clave pública y mantenga la clave en solo lectura.
2. Abra Project settings, Access keys y Add key si varios repositorios necesitan una identidad de lectura limitada al proyecto.
3. Use una clave de espacio de trabajo solo en un espacio compartido con un diseño de escritura aprobado. Los espacios personales no ofrecen la misma ruta a nivel de espacio de trabajo.
4. Registre la etiqueta de clave, el alcance, la huella de la clave pública, el propietario y la fecha de rotación. Guarde la clave privada en 1Password.

Ejecute una prueba exacta de conexión de solo lectura después del registro:

```bash
git ls-remote git@bitbucket.org:<workspace>/<repository>.git HEAD
```

**Resultado esperado:** una referencia de commit para `HEAD`. Ejemplo no probado. Un resultado correcto demuestra que una identidad SSH permitida llegó al repositorio indicado. No demuestra que se haya seleccionado la clave registrada ni que exista acceso de escritura. Repita la prueba después de configurar una clave por repositorio.

Para la custodia de claves privadas y el consentimiento de 1Password SSH Agent, consulte [1Password CLI y SSH Agent: claves SSH seguras para agentes de IA](/articles/1password-cli-ssh-keys-mcp-agent-administration/).

## Definir correctamente «Bitbucket CLI»

La expresión **Bitbucket CLI** suele mezclar tres interfaces distintas. Manténgalas separadas.

- **Git CLI:** `git clone` y `git fetch` transfieren datos del repositorio por SSH o HTTPS. `git diff` compara archivos locales o revisiones.
- **Cliente REST:** `curl` o un wrapper revisado llama a la API Representational State Transfer (REST) de Bitbucket Cloud. Una API es una interfaz programática para solicitar datos o acciones. La [referencia REST API de Bitbucket Cloud](https://developer.atlassian.com/cloud/bitbucket/rest/) enumera recursos de repositorio, código fuente, ramas, pull requests, pipelines y estados.
- **Atlassian CLI:** `acli` es la línea de comandos oficial de Atlassian. Su [introducción](https://developer.atlassian.com/cloud/acli/guides/introduction/) describe el producto y su [referencia de comandos](https://developer.atlassian.com/cloud/acli/reference/commands/) enumera las interfaces `admin`, `jira`, `feedback` y `rovodev`. La referencia no documenta comandos de Bitbucket Cloud.

**La referencia oficial de comandos `acli` de Atlassian no documenta comandos de Bitbucket Cloud.** No invente un comando como `acli bitbucket clone`. Use Git para las operaciones Git y REST API para los datos de Bitbucket Cloud.

### Teamwork Graph CLI opcional

**Atlassian también publica Teamwork Graph CLI, o `twg`.** Su [descripción general](https://developer.atlassian.com/cloud/twg-cli/) y [catálogo de comandos](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/commands/commands-catalog/) documentan familias de comandos de Bitbucket. El comando de configuración es:

```bash
twg setup
```

El comando de configuración cambia el estado de autenticación local. Siga las indicaciones de la versión instalada para configurar opcionalmente un token de Bitbucket. La ruta del token de Bitbucket en la CLI es independiente de Atlassian OAuth. Ajuste la sintaxis exacta del comando a la versión instalada y al catálogo vigente. Use un perfil independiente, un token restringido, habilidades instaladas revisadas y aprobación humana para comandos que modifican datos.

**Resultado esperado, no probado:** el perfil aislado recibe la configuración de autenticación de Bitbucket. Registre el estado anterior del perfil antes de configurarlo. Para revertir, elimine la credencial guardada mediante el procedimiento documentado de cierre de sesión o eliminación de configuración de la versión instalada.

Si un proyecto de terceros se presenta como Bitbucket CLI, audite su código fuente, proceso de publicación, sumas de comprobación, ruta de actualización, flujo de autenticación, alcances solicitados, destinos de red, manejo de registros y comandos de escritura. Un nombre de binario familiar no demuestra respaldo del proveedor ni permisos seguros.

## Mantener las claves SSH bajo el control de 1Password

[1Password SSH Agent](https://www.1password.dev/ssh/agent) pone las claves SSH guardadas en 1Password a disposición de Git y los clientes SSH. El cliente realiza una solicitud de firma autorizada. La clave privada permanece dentro de la aplicación 1Password, que solicita consentimiento antes de que un cliente aprobado use una clave.

La [referencia de 1Password CLI](https://www.1password.dev/cli/reference) cumple otra función. Use `op` para acceder de forma controlada a elementos, tokens API, cuentas de servicio y configuración de automatización. Use SSH Agent para firmar con SSH. Evite exportar una clave privada a un archivo temporal para facilitar el flujo de trabajo de un agente.

Compruebe el estado local de la CLI y del agente con comandos de solo lectura:

```bash
op --version
ssh-add -l
```

**Resultado esperado:** una versión de 1Password CLI y una o más huellas de claves públicas del agente activo. Ejemplo no probado. Un resultado vacío de `ssh-add -l` significa que el socket de agente seleccionado no tiene ninguna clave disponible.

Para una clave nueva, cree un elemento SSH Key Ed25519 en 1Password o importe una generada mediante un proceso local de confianza. Use una etiqueta basada en el propósito, el alcance y la fecha de rotación. Añada solo la clave pública a Bitbucket Cloud. La [guía Linux de claves de acceso al repositorio](https://support.atlassian.com/bitbucket-cloud/docs/set-up-repository-access-keys-on-linux/) describe la ruta de configuración del repositorio y la limitación de solo lectura.

## Verificar primero la clave de host de Bitbucket

La autenticación SSH del usuario no demuestra la identidad del servidor. El cliente debe verificar la clave de host de Bitbucket Cloud antes de enviar una solicitud de autenticación. La [guía de Atlassian sobre SSH y verificación en dos pasos](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification/) enumera las claves de host públicas y muestra el punto de conexión oficial para obtener entradas known-hosts.

Obtenga los datos de la clave de host pública para compararlos:

```bash
curl --fail --silent --show-error https://bitbucket.org/site/ssh
```

**Resultado esperado:** líneas OpenSSH `known_hosts` para `bitbucket.org`. Ejemplo no probado. Compare la clave o huella devuelta con una copia independiente de confianza antes de añadir la línea a `~/.ssh/known_hosts`.

Use la verificación estricta del host después de que exista la entrada aprobada:

```sshconfig
Host bitbucket.org
    StrictHostKeyChecking yes
    UserKnownHostsFile ~/.ssh/known_hosts
```

**No acepte una clave de host cambiada durante la ejecución de un agente.** Detenga la ejecución, verifique el registro actual de claves de host de Bitbucket Cloud y revise la entrada local de `known_hosts`. La aceptación automática elimina un límite de seguridad basado en claves.

## Seleccionar una clave por repositorio

Un dispositivo suele tener varias claves de Bitbucket. Un agente SSH amplio ofrece varias identidades en una conexión. Un servidor o una política con un límite bajo de intentos de autenticación podría rechazar la clave correcta después de fallar las anteriores.

La [guía de Atlassian sobre varias claves de acceso a repositorios](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) usa `core.sshCommand` en un archivo de configuración Git del repositorio e `includeIf` en la configuración global de Git. Siga el mismo patrón para usar una clave por repositorio.

Ejemplo portable con archivos:

```ini
# .gitconfig dentro de un repositorio local
[core]
    sshCommand = ssh -o IdentitiesOnly=yes -i ~/.ssh/<repository-automation-key>
```

```ini
# ~/.gitconfig
[includeIf "gitdir:~/src/<repository>/"]
    path = ~/src/<repository>/.gitconfig
```

El bloque anterior es una excepción con archivo de clave privada para una identidad de automatización dedicada. No configura 1Password SSH Agent. Para 1Password SSH Agent, configure el valor de `IdentityAgent` o `SSH_AUTH_SOCK` específico de la plataforma según la [guía de configuración de 1Password](https://www.1password.dev/ssh/get-started). Algunas configuraciones OpenSSH usan un archivo `.pub` como selector de identidad del agente. Confirme la compatibilidad de la plataforma antes de usarlo. Una configuración basada en archivo necesita la ruta de la clave privada correspondiente. Nunca pase un archivo `.pub` a un comando que espera material de clave privada ni exporte una clave privada personal.

Use configuración explícita del repositorio cuando un clon local necesite una clave. Use `includeIf` si un directorio contiene varios clones con el mismo límite de acceso. La [guía de varias claves](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) muestra ambas opciones del flujo de Bitbucket.

Clone con Git por SSH:

```bash
git clone git@bitbucket.org:<workspace>/<repository>.git <local-directory>
```

**Resultado esperado:** Git crea `<local-directory>` y obtiene el repositorio mediante `bitbucket.org`. Ejemplo no probado. Una clave de acceso al repositorio solo permite clonar y hacer pull.

## Usar tokens API para lecturas REST limitadas

Use SSH para el transporte Git. Use REST API para metadatos u operaciones fuera del transporte Git. La [guía de permisos de tokens API](https://support.atlassian.com/bitbucket-cloud/docs/api-token-permissions/) enumera alcances del repositorio, como Read, Write, Admin y Delete. Repository Read corresponde a `read:repository:bitbucket` y no incluye acceso a pull requests.

Para automatización de lectura, prefiera un token de acceso de repositorio o proyecto de Bitbucket si el destino admite el endpoint requerido. Un token API de usuario conserva el alcance más amplio de la cuenta. Use un token de espacio de trabajo solo si el registro de la tarea indica ese límite más amplio. Consulte la [guía de tokens de acceso de Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/) antes de elegir el tipo de token.

Para una ruta de lectura de agente, empiece con `read:repository:bitbucket`. Añada `read:pullrequest:bitbucket` solo si el agente necesita datos de pull requests. Añada alcances de espacio de trabajo o pipelines solo cuando el registro de tarea indique el endpoint y el resultado. Los alcances de escritura y administración requieren una aprobación independiente.

Cree cada token API para un propósito, establezca una fecha de caducidad, anótela en el registro de rotación y sustituya el token antes de que caduque. La [guía de creación de tokens API de Atlassian](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/) requiere nombre, caducidad, selección de aplicación y alcances. El token aparece una sola vez tras su creación.

Guarde el valor en 1Password o en un secreto de ejecución administrado. No lo coloque en una URL remota. Envíe un token bearer mediante una variable de entorno solo al proceso que necesite una lectura:

```bash
op run --env-file=/path/to/agent.env -- \
sh -c 'curl --fail --silent --show-error \
  --request GET \
  --url "https://api.bitbucket.org/2.0/repositories/<workspace>/<repository>" \
  --header "Authorization: Bearer ${BITBUCKET_API_TOKEN}" \
  --header "Accept: application/json"'
```

Mantenga `/path/to/agent.env` fuera del repositorio. Guarde en el archivo una referencia como `BITBUCKET_API_TOKEN=op://synthetic-vault/synthetic-api-token/credential`. `op run` resuelve la referencia y expone el valor al proceso hijo de curl durante la vida del subproceso. Esto no impide que el proceso hijo lea el valor de la variable de entorno o lo escriba en un registro. No sustituya el marcador de posición por un token literal.

**Resultado esperado:** metadatos JSON del repositorio seleccionado. Ejemplo no probado. El marcador de posición nunca debe convertirse en un token real en un archivo confirmado o un registro.

Para automatizaciones más largas, permita que 1Password inyecte un secreto en el entorno del proceso mediante el flujo CLI o de cuenta de servicio admitido. Ajuste la duración del token a la tarea. Revoque el token si la tarea termina antes o cambia el propietario del host.

## Dar a MCP una pequeña superficie de lectura

Use la [especificación MCP actual](https://modelcontextprotocol.io/specification/2026-07-28) y sus [reglas de autorización](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) al revisar un servidor nuevo. Los servidores HTTP requieren comprobaciones de audiencia del token y un manejo claro de las respuestas 401 y 403.

El host MCP obtiene el consentimiento del usuario. El cliente mantiene una conexión con un servidor. El servidor expone herramientas, recursos o prompts. Trate cada servidor como código no confiable hasta revisar su origen, transporte, cuenta y permisos.

La URL de la especificación 2025-06-18 del próximo párrafo es una versión histórica. Use la especificación actual 2026-07-28 para revisiones nuevas.

La [especificación MCP](https://modelcontextprotocol.io/specification/2025-06-18) define la comunicación entre un host MCP, un cliente y un servidor. Un servidor expone herramientas, recursos o prompts mediante el protocolo. MCP estandariza el formato de conexión. El host, la implementación del servidor, la cuenta, el alcance del token y la política de aprobación determinan qué alcanza cada llamada.

Use un servidor MCP como adaptador limitado sobre Git y REST API de Bitbucket Cloud.

Proteja el adaptador contra el reenvío de tokens, la falsificación de solicitudes del lado del servidor (SSRF) y el comportamiento de agente confundido. SSRF permite que un servidor envíe solicitudes a destinos no previstos. El comportamiento de agente confundido ocurre cuando un servidor usa privilegios más amplios en nombre de quien llama. Proteja también contra servidores locales maliciosos, redirecciones OAuth inseguras y respuestas de código fuente excesivamente grandes. Fije los orígenes permitidos de Bitbucket y los identificadores de repositorio. Ejecute servidores locales en un entorno aislado bajo un usuario dedicado del sistema operativo. Oculte secretos en los resultados de herramientas y registros.

Esta sección describe un diseño, no una configuración MCP probada. No fija cliente, servidor, transporte, versión ni conjunto de pruebas. Valide un servidor de solo lectura en un perfil de prueba aparte antes de conectar un agente a un repositorio de producción.

Ejemplos de herramientas de lectura:

| Herramienta | Resultado limitado |
|---|---|
| **`get_repository_metadata`** | Devuelve los metadatos de un repositorio |
| **`read_source_file`** | Lee una ruta en una revisión |
| **`list_branches`** | Enumera las ramas de un repositorio |
| **`get_pull_request`** | Devuelve una pull request si el token tiene el alcance de lectura de pull requests |
| **`get_build_status`** | Devuelve datos del estado de un commit |

Estos nombres describen un diseño. No son comandos de Atlassian. Impida que el servidor acepte URL arbitrarias, comandos de shell arbitrarios, tokens sin procesar, solicitudes de exportación de claves privadas o identificadores de repositorio sin restricciones.

Configure permisos en cuatro capas:

1. **Bitbucket Cloud:** clave de lectura de repositorio o proyecto para Git, más los alcances mínimos del token API para lecturas REST.
2. **1Password:** una bóveda o cuenta de servicio para la tarea, sin ruta para exportar claves privadas.
3. **Servidor MCP:** lista permitida de herramientas de lectura, endpoints fijos de Bitbucket Cloud, validación de entradas, límites de tiempo y registros con secretos ocultos.
4. **Host MCP:** aprobación del usuario para el servidor y cada acción con capacidad de escritura, con las herramientas de escritura desactivadas en el perfil predeterminado.

*Una lista de herramientas MCP demuestra que se descubrieron. No demuestra autorización, alcance correcto, manejo seguro de entradas ni un resultado correcto.*

## Organizar el flujo de trabajo del agente

Mantenga explícito el flujo. Cada etapa proporciona evidencia para la siguiente.

| Etapa | Acción del agente | Permiso | Control humano |
|---|---|---|---|
| **Preparar** | Leer configuración, registro de clave de host, etiqueta de clave, alcance del token y caducidad | Lectura local | Aprobar el registro de configuración |
| **Inspeccionar** | Clonar o hacer fetch mediante Git por SSH y consultar metadatos REST | Lectura de repositorio y API | Ninguno después de configurar |
| **Analizar** | Leer archivos, ramas, pull requests y estado de compilación mediante herramientas aprobadas | Herramientas MCP de solo lectura | Ninguno para lecturas limitadas |
| **Preparar cambio** | Crear un parche, plan de rama o borrador de pull request en un espacio de trabajo local | Solo escritura local | Revisar diff y destino |
| **Aprobar escritura** | Presentar la acción remota exacta, el alcance y el plan de reversión | Aún sin escritura remota | Aprobación humana |
| **Ejecutar escritura** | Enviar una rama, crear una pull request o llamar a un endpoint de escritura | Identidad de escritura de corta duración | Confirmar cada acción |
| **Verificar** | Leer el commit, pull request o estado resultante | De nuevo en solo lectura | Confirmar el resultado esperado |

El perfil de agente predeterminado debe detenerse después de **Analizar** o **Preparar cambio**. Un perfil de escritura aparte debe usar otro token o clave, una caducidad breve, un destino fijo y una solicitud de aprobación. Una clave de acceso al repositorio no permite el paso de escritura, lo que establece un límite técnico útil.

## Reversión y eliminación

Empiece la reversión eliminando accesos y después limpie la configuración local:

1. Elimine la clave de acceso al repositorio, proyecto o espacio de trabajo de la página correspondiente de configuración de Bitbucket.
2. Revoque el token API del repositorio, proyecto, espacio de trabajo o usuario en la página de seguridad correspondiente de Bitbucket.
3. Elimine la credencial guardada de Teamwork Graph mediante el [procedimiento de autenticación documentado](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/getting-started/how-authentication-works/) para la versión de CLI instalada. Conserve la credencial previa solo en el gestor de secretos aprobado. Confirme que el perfil aislado ya no muestra la credencial de prueba.
4. Al terminar la prueba, elimine el archivo `.gitconfig` del repositorio y su entrada `includeIf`. Mantenga sin cambios la configuración Git no relacionada.
5. Elimine solo la línea verificada de clave de host de Bitbucket añadida para la prueba. Conserve las demás claves de host aprobadas.
6. Elimine el archivo externo `agent.env` y la salida temporal. Quite la entrada del servidor MCP de la configuración del host y reinicie el host.

Registre cada eliminación, la persona que la realizó y la hora. Rote una clave o token si un valor aparece en un registro, historial de procesos o transcripción inesperados.

## Ciclo de lectura remota con actualizaciones locales de referencias

Use un ciclo pequeño para inspecciones recurrentes del repositorio:

```bash
LOCAL_REPO="<local-directory>"
git -C "$LOCAL_REPO" fetch --no-tags
git -C "$LOCAL_REPO" status --short --branch
git -C "$LOCAL_REPO" log -1 --format='%H %ad %s' --date=iso-strict
```

`HEAD` es la referencia actualmente seleccionada del repositorio. Un resultado correcto demuestra que una identidad SSH permitida llegó al repositorio indicado. No demuestra qué clave se seleccionó ni si existe acceso push.

**Resultado esperado:** resultado de fetch, estado de rama y una línea de commit. Ejemplo no probado. `fetch` no escribe en el remoto, pero actualiza referencias locales y `FETCH_HEAD`. El ciclo no hace push ni cambia de rama.

El servidor MCP debe exponer el mismo límite de lectura mediante operaciones con nombre. Un wrapper local de shell o una herramienta MCP debe rechazar un verbo de escritura antes de enviar la solicitud. Registre el nombre de herramienta, marcador del repositorio, revisión, clase de resultado y duración. Oculte tokens, cookies, rutas privadas y contenido de archivos salvo que la tarea necesite expresamente un archivo.

## Solución de problemas

### `Permission denied (publickey)`

Compruebe el socket del agente activo, la clave pública seleccionada, la entrada de clave de acceso del repositorio y `IdentitiesOnly`. La clave del repositorio debe existir en el repositorio o proyecto de destino. Una clave personal requiere permisos de cuenta. Una clave de espacio de trabajo tiene otro límite de escritura.

### Se ofrece la clave de repositorio incorrecta

Use una clave por repositorio con `core.sshCommand` o agrupe clones en un directorio controlado por `includeIf`. Enumere las claves del agente con `ssh-add -l`. Si hay varias claves 1Password disponibles, use un selector de identidad explícito o un marcador SSH de 1Password. La [guía de 1Password Agent](https://www.1password.dev/ssh/agent) explica el límite de claves y los marcadores.

### SSH informa que cambió la clave de host

Detenga el agente. No elimine `known_hosts` como primera respuesta. Compare el registro actual de claves de host de Bitbucket Cloud con la entrada local mediante un canal independiente. Elimine o sustituya una entrada solo después de confirmar la comparación.

### La API devuelve `401` o `403`

Compruebe la caducidad y tipo de token, el alcance del endpoint y el límite de la cuenta o del espacio de trabajo. El alcance de lectura del repositorio no incluye pull requests. Un endpoint de escritura requiere alcance de escritura y un perfil de escritura aprobado. No amplíe los alcances hasta identificar el endpoint que falló.

### La API devuelve datos del repositorio, pero no pull requests

Añada el alcance mínimo de lectura de pull requests a un token nuevo o rotado. No reutilice un token de usuario amplio para un servidor MCP de solo lectura.

### El servidor MCP enumera herramientas, pero una llamada falla

Distinga el registro del servidor, la conexión, la detección de herramientas, la ejecución y la verificación del resultado. Revise el registro del servidor sin exponer el token. Verifique el endpoint y el formato de entrada. Reintente una vez después de comprobar la conectividad. Marque la operación como incompleta si falla el segundo intento.

### Una CLI de Bitbucket de terceros solicita acceso amplio

Detenga la instalación. Compare el acceso solicitado con el registro de tarea. Revise el código fuente, las firmas o sumas de comprobación de publicaciones, destinos de red, almacenamiento de secretos y comportamiento de escritura. La referencia oficial de comandos Atlassian CLI no demuestra soporte para un binario Bitbucket de terceros.

## Próximos pasos

Cree un registro breve de acceso con el alcance del repositorio o proyecto, etiqueta de clave, fecha de verificación de clave de host, alcances API, caducidad del token, propietario de 1Password, lista permitida de herramientas MCP, política de registros y aprobador de escritura.

Ejecute un clon de solo lectura, una lectura de metadatos REST y una lectura de herramienta MCP con marcadores de posición en la transcripción. Compare los resultados. Mantenga el perfil del agente en solo lectura hasta que se revisen el registro y los logs.

Cuando llegue una tarea de escritura, prepare primero un diff local. Presente la rama de destino, rutas modificadas, método API solicitado, alcance del token y paso de reversión. Use una identidad de escritura separada y de corta duración solo después de que una persona apruebe la acción exacta.
