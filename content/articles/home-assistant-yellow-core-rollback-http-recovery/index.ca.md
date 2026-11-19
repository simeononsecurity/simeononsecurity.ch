---
title: 'Retrocés de Home Assistant Core 2026.11 a 2026.10.4: correcció de la versió 3 d''emmagatzematge HTTP'
date: 2026-11-15
lastmod: '2026-11-18'
toc: true
draft: false
description: Corregeix l'error de la versió 3 d'emmagatzematge HTTP després que Home Assistant Core 2026.11 retrocedeixi a
  2026.10.4 a Yellow. Inclou ordres protegides i resultats verificats.
genre:
- Domòtica
- Resolució de problemes
tags:
- Home Assistant Yellow
- Home Assistant OS
- Retrocés de Core 2026.11
- Core 2026.10.4
- Versió 3 d'emmagatzematge HTTP
- CM4
cover: /img/cover/home-assistant-yellow-core-rollback-http-recovery.webp
coverAlt: Il·lustració d'una placa d'ordinador groga, un enllaç de configuració trencat i un tauler web restaurat
coverCaption: ''
---

Una actualització fallida de Home Assistant Core 2026.11 va fer retrocedir el meu Yellow CM4 a 2026.10.4. El Yellow continuava accessible a la xarxa, però va deixar de servir el tauler. El retrocés va deixar un fitxer de configuració HTTP a la versió d'emmagatzematge 3.1, mentre que Core 2026.10.4 admet la versió 2.2. Vaig conservar el fitxer, vaig convertir-ne una còpia amb comprovacions estrictes, vaig recuperar l'accés HTTP i després vaig actualitzar Core a 2026.11.1.

<!--more-->

## Idees clau

- **Confirma el desajust.** Compara l'error del registre de Core amb la versió instal·lada i la versió d'emmagatzematge HTTP.
- **Conserva el fitxer.** Abans de recuperar el sistema, guarda'n una còpia intacta i una còpia de seguretat fora del dispositiu.
- **Verifica el resultat.** Comprova l'estat de Core, el listener desat, el tauler i la versió instal·lada.

**Correcció per a aquest cas exacte:** [Conserva el fitxer HTTP](#preserve-recovery-options), [crea i valida un candidat de versió 2.2](#apply-the-tested-fix-for-version-31), [instal·la'l després d'aturar Core](#apply-the-tested-fix-for-version-31) i [verifica el resultat de l'actualització](#verify-the-update-outcome). La conversió comprova els camps originals i s'atura si no coincideixen. No l'apliquis a un fitxer HTTP que no hagis inspeccionat.

## Abans de començar

Necessites accés físic a un Yellow CM4, un cable de dades USB-C, una consola sèrie funcional i una còpia de seguretat utilitzable o una configuració conservada. El procediment manual requereix accés a l'intèrpret d'ordres de l'amfitrió i una inspecció acurada del JSON. Reserva almenys 30 minuts per diagnosticar i reparar el problema. L'inici de Core i la restauració de còpies de seguretat triguen més en instal·lacions grans.

## Reconeix el problema

L'error decisiu apareixia al registre de Core:

```text
Storage file http has version 3 which is newer than the max supported version 2
```

La versió anterior de Core no podia carregar `http`. També van fallar el frontend i els altres components que en depenen. Una concessió d'adreça del router i una pàgina Observer en bon estat no demostren que el tauler sigui accessible. [L'incident núm. 190583 de Home Assistant Core](https://github.com/home-assistant/core/issues/190583) documenta el mateix error de retrocés en diverses instal·lacions, inclosa Yellow. [El meu comentari a l'incident](https://github.com/home-assistant/core/issues/190583#issuecomment-6908185955) registra la recuperació provada en aquest Yellow i l'estat final de Core.

**Causa de la interrupció web:** Core 2026.11 va escriure `.storage/http` en format 3.1. El retrocés va restaurar Core 2026.10.4, però no un fitxer HTTP compatible. Core 2026.10.4 rebutja la versió d'emmagatzematge 3. El perfil `intermediate_v6` desat en aquest Yellow tampoc no s'ajusta a l'esquema anterior. No se sap per què va fallar la primera actualització i va provocar el retrocés. A 2026-11-15, l'incident enllaçat continuava obert i la conversa no contenia cap solució confirmada pels mantenidors.

Comprova la versió instal·lada de Core i el magatzem HTTP abans de canviar fitxers:

```bash
ha core info --raw-json | jq -r '.data.version'

storage=/mnt/data/supervisor/homeassistant/.storage
jq '{version, minor_version, pending_present: (.data.pending != null), profile: .data.stable.ssl_profile}' "$storage/http"
ha core logs | grep -F 'Storage file http has version 3'
```

La sortida següent reflecteix aquest cas amb les marques de temps i les dades privades eliminades:

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

Les ordres de recuperació següents comparen el listener desat de Supervisor amb el fitxer HTTP sense mostrar cap dels dos valors. Si no coincideixen, comprova el listener real de Core abans de canviar fitxers.

| Indicador | Significat |
| --- | --- |
| Core admet la versió 2, però el fitxer indica la versió 3 | La versió anterior no pot carregar la configuració HTTP desada |
| El fitxer HTTP i la llista de Supervisor indiquen listeners diferents | Comprova el listener real de Core abans d'atribuir-hi el problema |
| La pàgina principal respon, però Core continua en estat STARTING | La resposta del frontend no demostra que l'inici hagi acabat |

## Conserva les opcions de recuperació {#preserve-recovery-options}

Abans d'una altra actualització, conserva una còpia de seguretat utilitzable fora de Yellow. [La guia de còpies de seguretat de Home Assistant](https://www.home-assistant.io/common-tasks/general/backups/) descriu ubicacions al núvol i fora del dispositiu. Una còpia xifrada necessita la seva clau de recuperació. No esborris el disc de dades NVMe mentre diagnostiques aquest desajust d'emmagatzematge.

Copia el fitxer HTTP abans d'editar-lo:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
test ! -e "$storage/http.before-recovery" &&
  cp -p "$storage/http" "$storage/http.before-recovery" &&
  cmp -s "$storage/http" "$storage/http.before-recovery"
```

Atura't si l'ordre falla. Deixa intacta qualsevol còpia de recuperació anterior amb el mateix nom. Tria un nom nou i repeteix la comprovació abans de continuar.

Si el tauler no està disponible, utilitza la consola sèrie de Yellow. [La guia de Nabu Casa per a Linux i macOS](https://support.nabucasa.com/hc/en-us/articles/25454972435357-Using-the-serial-console-on-Home-Assistant-Yellow-for-debugging-Linux-macOS) mostra la connexió USB-C i la posició del UART JP1. Segueix les instruccions del CM4 corresponents al teu maquinari.

## Aplica la correcció provada per a la versió 3.1 {#apply-the-tested-fix-for-version-31}

L'opció preferida és utilitzar un fitxer HTTP compatible anterior a l'actualització. Restaura la còpia de seguretat amb el procés documentat de Home Assistant quan convingui fer una restauració completa. Si extreus un sol fitxer, confirma'n la versió d'emmagatzematge i el listener desat abans de substituir el fitxer actiu. Les ordres següents són la correcció directa provada en aquest Yellow quan no hi havia cap fitxer HTTP compatible.

[La solució provisional original de l'incident](https://github.com/home-assistant/core/issues/190583) aparta `.storage/http` i deixa que la versió anterior de Core creï un fitxer nou. Un [informe posterior de Yellow](https://github.com/home-assistant/core/issues/190583#issuecomment-6749568119) mostra un listener diferent al fitxer regenerat. Comprova el fitxer nou i `ha core info` abans de concloure que la interfície web s'ha recuperat.

La meva instal·lació no tenia cap bloc YAML `http:`, cap configuració HTTP pendent ni cap certificat TLS o clau a la configuració estable. El perfil desat era `intermediate_v6`. En aquest cas limitat, vaig crear un candidat separat de versió 2.2 i vaig conservar el listener existent:

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

Totes les ordres anteriors han de tenir èxit abans de substituir el fitxer actiu. Si `jq` falla, inspecciona el candidat abans d'eliminar-lo i tornar-ho a provar. [El codi font HTTP de Core 2026.10.4](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/http/config.py) defineix la versió d'emmagatzematge 2.2 i accepta el perfil `intermediate`. [El codi font de Core 2026.11.1](https://github.com/home-assistant/core/blob/2026.11.1/homeassistant/components/http/config.py) utilitza la versió 3.1 i noms de perfil versionats. També vaig validar el candidat amb `HTTP_STORAGE_SCHEMA` de la versió anterior instal·lada abans d'instal·lar-lo.

Executa la comprovació d'esquema de la versió anterior de Core instal·lada mentre el contenidor encara funciona:

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
print("Schema accepted")
'
```

Atura't si l'esquema rebutja el candidat. Aquest pas no valida totes les integracions ni una forma no provada del magatzem HTTP.

La comprovació de l'esquema va mostrar `Schema accepted` per a aquest candidat. Qualsevol altre resultat atura aquesta via de recuperació.

Aquesta conversió manual es va provar amb els camps indicats. Un fitxer amb paràmetres TLS, proxies de confiança o una configuració pendent necessita una revisió pròpia. Canviar només el número de versió principal deixa un perfil que la versió anterior de Core no admet.

Supervisor tenia una tasca activa de Core i va rebutjar `ha core stop` en el meu cas. Vaig aturar el contenidor de Core des de la consola de l'amfitrió, hi vaig instal·lar el candidat validat i el vaig iniciar:

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

Si falla una ordre després de l'aturada, inspecciona el fitxer HTTP actiu abans d'executar `docker start homeassistant`. Si el fitxer ha canviat, crea un candidat nou a partir del contingut actual. La pàgina HTTP va tornar després d'aquest pas. Una resposta HTTP no demostrava que Core hagués acabat d'iniciar-se, així que vaig comprovar l'estat de Supervisor abans de considerar recuperat el sistema.

En aquest Yellow, `docker inspect -f '{{.State.Status}}' homeassistant` va mostrar `running`. Comprova `ha core info` i el tauler abans de demanar una altra actualització.

## Verifica el resultat de l'actualització {#verify-the-update-outcome}

Després de recuperar l'accés HTTP, vaig actualitzar Core a 2026.11.1. Per sol·licitar aquesta versió:

```bash
ha core update --version 2026.11.1
```

L'ordre va indicar un error després d'un inici llarg. A continuació, Supervisor va registrar Core com a RUNNING i `Successfully started Home Assistant 2026.11.1`. Una consulta d'estat va mostrar que la versió instal·lada era l'actual, que el fitxer HTTP havia tornat a migrar a la versió 3.1 i que el contenidor no s'havia reiniciat durant l'observació. El tauler autenticat es va carregar. **Comprova l'estat final encara que l'ordre d'actualització indiqui un error.**

En el teu sistema, comprova la versió, l'estat de Supervisor i l'estat del contenidor després d'una actualització llarga:

```bash
ha core info --raw-json | jq '{version: .data.version, update_available: .data.update_available}'
ha supervisor info --raw-json | jq '{healthy: .data.healthy, supported: .data.supported}'
docker inspect -f '{{.State.Status}} restarts={{.RestartCount}}' homeassistant
```

En aquest cas, la primera i la tercera ordres van produir els resultats anonimitzats següents:

```text
{
  "version": "2026.11.1",
  "update_available": false
}
running restarts=0
```

Després, obre el tauler a l'adreça local habitual i confirma que es carreguen els estats en directe. Conserva el fitxer HTTP desat fins que es completi una còpia de seguretat posterior i es verifiqui el funcionament normal.

Les proves del meu Yellow no van establir la causa de la primera actualització fallida. El missatge de la tasca posterior tampoc no en va identificar cap. Una versió instal·lada i un tauler funcional són proves més sòlides de l'estat final que el missatge de CLI, però cap de les dues explica per què Supervisor va marcar la tasca com a fallida.

## Passos següents

Si continua l'error d'emmagatzematge HTTP, inspecciona el fitxer conservat i restaura una còpia compatible o executa una versió de Core que pugui llegir aquella versió d'emmagatzematge. Restaurar el fitxer desat de versió 3 amb Core anterior repeteix l'avaria. Si Core arriba a RUNNING però alguns dispositius continuen sense estar disponibles, investiga aquestes integracions per separat. Conserva la còpia de recuperació i la còpia al núvol fins que es completi la següent còpia de seguretat i el tauler continuï responent.
