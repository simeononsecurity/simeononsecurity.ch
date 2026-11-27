---
title: 'Reversión de Home Assistant Core 2026.11 a 2026.10.4: reparar la versión 3 del almacenamiento HTTP'
date: 2026-11-15
lastmod: 2026-11-27
toc: true
draft: false
description: Corrige el error de la versión 3 del almacenamiento HTTP después de que Home Assistant Core 2026.11 vuelva a
  2026.10.4 en Yellow. Incluye comandos protegidos y resultados verificados.
genre:
- Domótica
- Solución de problemas
tags:
- Home Assistant Yellow
- Home Assistant OS
- Reversión de Core 2026.11
- Core 2026.10.4
- Versión 3 del almacenamiento HTTP
- CM4
cover: /img/cover/home-assistant-yellow-core-rollback-http-recovery.webp
coverAlt: Ilustración de una placa de ordenador amarilla, un enlace de configuración roto y un panel web restaurado
coverCaption: ''
---

Una actualización fallida de Home Assistant Core 2026.11 revirtió mi Yellow CM4 a 2026.10.4. Yellow seguía accesible en la red, pero dejó de mostrar el panel. La reversión dejó un archivo de configuración HTTP con la versión de almacenamiento 3.1, mientras Core 2026.10.4 admite la versión 2.2. Conservé el archivo, convertí una copia con comprobaciones estrictas, recuperé el acceso HTTP y después actualicé Core a 2026.11.1.

<!--more-->

## Puntos clave

- **Confirma la incompatibilidad.** Compara el error del registro de Core con la versión instalada y la versión del almacenamiento HTTP.
- **Conserva el archivo.** Guarda una copia sin modificar y otra copia de seguridad fuera del dispositivo antes de recuperar el sistema.
- **Verifica el resultado.** Comprueba el estado de Core, el puerto de escucha guardado, el panel y la versión instalada.

**Solución para este caso exacto:** [Conserva el archivo HTTP](#preserve-recovery-options), [crea y valida un candidato de la versión 2.2](#apply-the-tested-fix-for-version-31), [instálalo después de detener Core](#apply-the-tested-fix-for-version-31) y [verifica el resultado de la actualización](#verify-the-update-outcome). La conversión comprueba los campos originales y se detiene si no coinciden. No la apliques a un archivo HTTP que no hayas inspeccionado.

## Antes de empezar

Necesitas acceso físico a Yellow CM4, un cable de datos USB-C, una consola serie funcional y una copia de seguridad utilizable o una configuración conservada. El procedimiento manual requiere acceso al shell del host y una inspección cuidadosa de JSON. Reserva al menos 30 minutos para diagnosticar y reparar el problema. El inicio de Core y la restauración de copias de seguridad tardan más en instalaciones grandes.

## Identifica el fallo

El error decisivo apareció en el registro de Core:

```text
Storage file http has version 3 which is newer than the max supported version 2
```

La versión anterior de Core no pudo cargar `http`. También fallaron la interfaz y otros componentes que dependen de HTTP. Una concesión del router y una página Observer en buen estado no demostraban que se pudiera acceder al panel. [El problema #190583 de Home Assistant Core](https://github.com/home-assistant/core/issues/190583) documenta el mismo fallo de reversión en varias instalaciones, incluida Yellow. [Mi comentario en el problema](https://github.com/home-assistant/core/issues/190583#issuecomment-6908185955) registra la recuperación probada en este Yellow y el estado final de Core.

**Causa de la interrupción web:** Core 2026.11 escribió `.storage/http` en formato 3.1. La reversión restauró Core 2026.10.4, pero no un archivo HTTP compatible. Core 2026.10.4 rechaza la versión de almacenamiento 3. El perfil guardado `intermediate_v6` de este Yellow tampoco cumple el esquema anterior. Se desconoce por qué falló la primera actualización y provocó la reversión. A fecha de 2026-11-15, el problema enlazado seguía abierto y el debate no incluía una solución confirmada por los responsables del proyecto.

Comprueba la versión instalada de Core y el almacén HTTP antes de cambiar archivos:

```bash
ha core info --raw-json | jq -r '.data.version'

storage=/mnt/data/supervisor/homeassistant/.storage
jq '{version, minor_version, pending_present: (.data.pending != null), profile: .data.stable.ssl_profile}' "$storage/http"
ha core logs | grep -F 'Storage file http has version 3'
```

La siguiente salida refleja este caso, con las marcas de tiempo y los datos privados eliminados:

```text
2026.10.4
{
  "version": 3,
  "minor_version": 1,
  "pending_present": false,
  "profile": "intermediate_v6"
}
Storage file http has version 3 which is newer than the max supported version 2
```

Los comandos de recuperación comparan el puerto de escucha guardado por Supervisor con el archivo HTTP sin mostrar ninguno de los valores. Si no coinciden, comprueba el puerto de escucha real de Core antes de cambiar archivos.

| Señal | Significado |
| --- | --- |
| Core admite la versión de almacenamiento 2 y el archivo indica la versión 3 | La versión anterior no puede cargar la configuración HTTP guardada |
| El archivo HTTP y la lista de Supervisor muestran puertos de escucha distintos | Comprueba el puerto de escucha real de Core antes de atribuirle el fallo |
| La página principal responde, pero el estado de Core sigue en STARTING | La respuesta de la interfaz no demuestra que el inicio haya terminado |

## Conserva las opciones de recuperación {#preserve-recovery-options}

Guarda una copia de seguridad utilizable fuera de Yellow antes de otra actualización. [La guía de copias de seguridad de Home Assistant](https://www.home-assistant.io/common-tasks/general/backups/) describe ubicaciones en la nube y fuera del dispositivo. Una copia cifrada necesita su clave de recuperación. No borres el disco de datos NVMe mientras diagnosticas esta incompatibilidad de almacenamiento.

Copia el archivo HTTP antes de editarlo:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
test ! -e "$storage/http.before-recovery" &&
  cp -p "$storage/http" "$storage/http.before-recovery" &&
  cmp -s "$storage/http" "$storage/http.before-recovery"
```

Detente si el comando falla. No modifiques una copia de recuperación anterior con el mismo nombre. Elige otro nombre y repite la comprobación antes de continuar.

Si el panel no está disponible, usa la consola serie de Yellow. [La guía de Nabu Casa para Linux y macOS](https://support.nabucasa.com/hc/en-us/articles/25454972435357-Using-the-serial-console-on-Home-Assistant-Yellow-for-debugging-Linux-macOS) muestra la conexión USB-C y la posición del UART JP1. Sigue las instrucciones de CM4 correspondientes a tu hardware.

## Aplica la solución probada para la versión 3.1 {#apply-the-tested-fix-for-version-31}

La opción preferida es usar un archivo HTTP compatible anterior a la actualización. Restaura la copia de seguridad mediante el proceso documentado de Home Assistant cuando convenga realizar una restauración completa. Si extraes un único archivo, confirma su versión de almacenamiento y el puerto de escucha guardado antes de sustituir el archivo activo. Los comandos siguientes son la solución directa probada en este Yellow cuando no había un archivo HTTP compatible.

[La solución provisional original del problema](https://github.com/home-assistant/core/issues/190583) aparta `.storage/http` y deja que la versión anterior de Core cree un archivo nuevo. Un [informe posterior de Yellow](https://github.com/home-assistant/core/issues/190583#issuecomment-6749568119) muestra un puerto de escucha distinto en el archivo regenerado. Comprueba el archivo nuevo y `ha core info` antes de concluir que la interfaz web funciona.

Mi instalación no tenía un bloque YAML `http:`, ni una configuración HTTP pendiente, ni un certificado o una clave TLS en los ajustes estables. El perfil guardado era `intermediate_v6`. En este caso concreto, creé un candidato independiente de la versión 2.2 y conservé el puerto de escucha existente:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage

expected=$(ha core info --raw-json | jq -r '.data.port') &&
stored=$(jq -r '.data.stable.server_port' "$storage/http") &&
test -n "$expected" &&
test "$expected" != null &&
test "$expected" = "$stored" &&
test ! -e "$storage/http.v2-candidate" &&
jq -e '
  if .version == 3 and .minor_version == 1 and
     .data.pending == null and
     .data.stable.ssl_profile == "intermediate_v6" and
     (.data.stable | has("ssl_certificate") | not) and
     (.data.stable | has("ssl_peer_certificate") | not) and
     (.data.stable | has("ssl_key") | not) and
     (.data.stable | has("trusted_proxies") | not) and
     (.data.stable | has("use_x_forwarded_for") | not)
  then .version = 2 | .minor_version = 2 | .data.stable.ssl_profile = "intermediate"
  else error("Unexpected HTTP config. Stop and inspect")
  end
' \
  "$storage/http" > "$storage/http.v2-candidate" &&

jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&

test "$(jq -r '.data.stable.server_port' "$storage/http")" = \
  "$(jq -r '.data.stable.server_port' "$storage/http.v2-candidate")"
```

Todos los comandos anteriores deben completarse correctamente antes de sustituir el archivo activo. Si `jq` falla, inspecciona el candidato antes de eliminarlo y volver a intentarlo. [El código fuente HTTP de Core 2026.10.4](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/http/config.py) define la versión de almacenamiento 2.2 y acepta el perfil `intermediate`. [El código fuente de Core 2026.11.1](https://github.com/home-assistant/core/blob/2026.11.1/homeassistant/components/http/config.py) usa la versión 3.1 y nombres de perfil versionados. También validé el candidato con `HTTP_STORAGE_SCHEMA` de la versión anterior de Core instalada antes de aplicarlo.

Ejecuta la comprobación de esquema de la versión anterior de Core instalada mientras el contenedor siga en marcha:

```bash
docker exec homeassistant python3 -c '
import json
from homeassistant.components.http.config import HTTP_STORAGE_SCHEMA
with open("/config/.storage/http.v2-candidate") as source:
    data = json.load(source)
stable = {
    key: value for key, value in data["data"]["stable"].items()
    if key not in ("created_at", "error", "error_message")
}
HTTP_STORAGE_SCHEMA(stable)
print("Esquema aceptado")
'
```

Detente si el esquema rechaza el candidato. Este paso no valida todas las integraciones ni todas las formas no probadas del almacén HTTP.

La comprobación del esquema imprimió `Esquema aceptado` para este candidato. Cualquier otro resultado detiene este procedimiento de recuperación.

Esta conversión manual se probó con los campos indicados. Un archivo con ajustes TLS, proxies de confianza o una configuración pendiente requiere su propia revisión. Cambiar solo el número de versión principal deja un perfil que la versión anterior de Core no acepta.

Supervisor tenía una tarea activa de Core y rechazó `ha core stop` en mi caso. Detuve el contenedor de Core desde la consola del host, instalé el candidato validado y lo inicié:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&
  docker stop homeassistant &&
  test "$(docker inspect -f '{{.State.Running}}' homeassistant)" = false &&
  cmp -s "$storage/http" "$storage/http.before-recovery" &&
  mv "$storage/http.v2-candidate" "$storage/http" &&
  docker start homeassistant
```

Si un comando falla después de detener Core, inspecciona el archivo HTTP activo antes de ejecutar `docker start homeassistant`. Si el archivo ha cambiado, crea un candidato nuevo a partir del contenido más reciente. La página HTTP volvió después de este paso. Una respuesta HTTP no demostraba por sí sola que Core hubiera terminado de arrancar, así que comprobé el estado de Supervisor antes de considerar recuperado el sistema.

En este Yellow, `docker inspect -f '{{.State.Status}}' homeassistant` mostró después `running`. Comprueba `ha core info` y el panel antes de solicitar otra actualización.

## Verifica el resultado de la actualización {#verify-the-update-outcome}

Cuando volvió el acceso HTTP, actualicé Core a 2026.11.1. Para solicitar esa versión:

```bash
ha core update --version 2026.11.1
```

El comando indicó un fallo después de un inicio prolongado. Después, Supervisor registró Core como RUNNING y `Successfully started Home Assistant 2026.11.1`. Una consulta de estado mostró que la versión instalada era la actual, que el archivo HTTP había migrado de nuevo a la versión 3.1 y que el contenedor no se había reiniciado durante la observación. El panel autenticado se cargó. **Comprueba el estado resultante aunque el comando de actualización indique un fallo.**

En tu sistema, comprueba la versión, el estado de Supervisor y el del contenedor después de una actualización larga:

```bash
ha core info --raw-json | jq '{version: .data.version, update_available: .data.update_available}'
ha supervisor info --raw-json | jq '{healthy: .data.healthy, supported: .data.supported}'
docker inspect -f '{{.State.Status}} restarts={{.RestartCount}}' homeassistant
```

En este caso, el primer y el tercer comando produjeron los siguientes resultados saneados:

```text
{
  "version": "2026.11.1",
  "update_available": false
}
running restarts=0
```

Después, abre el panel mediante tu dirección local habitual y confirma que se cargan los estados en directo. Conserva el archivo HTTP guardado hasta que se complete otra copia de seguridad y se verifique el funcionamiento normal.

Las pruebas de mi Yellow no determinaron la causa del primer fallo de actualización. El mensaje de error de la tarea posterior tampoco identificó ninguna causa. Una versión instalada y un panel operativo son pruebas más sólidas del estado resultante que el mensaje de CLI por sí solo, pero ninguna explica por qué Supervisor marcó la tarea como fallida.

## Pasos siguientes

Si persiste el error de almacenamiento HTTP, inspecciona el archivo conservado y restaura una copia de seguridad compatible o ejecuta una versión de Core que pueda leer su versión de almacenamiento. Restaurar el archivo guardado de versión 3 en la versión anterior de Core repite el fallo. Si Core llega a RUNNING pero algunos dispositivos siguen sin estar disponibles, investiga esas integraciones por separado. Conserva la copia de recuperación y la copia en la nube hasta que termine la siguiente copia de seguridad y el panel siga respondiendo.
