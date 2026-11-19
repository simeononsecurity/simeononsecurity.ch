---
title: 'Rollback da Home Assistant Core 2026.11 a 2026.10.4: correggere la versione 3 dello storage HTTP'
date: 2026-11-15
lastmod: '2026-11-18'
toc: true
draft: false
description: Correggi l'errore della versione 3 dello storage HTTP dopo il rollback di Home Assistant Core 2026.11 a 2026.10.4
  su Yellow. Include comandi protetti e risultati verificati.
genre:
- Domotica
- Risoluzione dei problemi
tags:
- Home Assistant Yellow
- Home Assistant OS
- Rollback di Core 2026.11
- Core 2026.10.4
- Versione 3 dello storage HTTP
- CM4
cover: /img/cover/home-assistant-yellow-core-rollback-http-recovery.webp
coverAlt: Illustrazione di una scheda computer gialla, un collegamento di configurazione interrotto e una dashboard web ripristinata
coverCaption: ''
---

Un aggiornamento non riuscito di Home Assistant Core 2026.11 ha riportato il mio Yellow CM4 alla versione 2026.10.4. Yellow era ancora raggiungibile in rete, ma non mostrava più la dashboard. Il rollback ha lasciato un file delle impostazioni HTTP con versione di storage 3.1, mentre Core 2026.10.4 supporta la versione 2.2. Ho conservato il file, convertito una copia con controlli rigorosi, ripristinato l'accesso HTTP e poi aggiornato Core alla versione 2026.11.1.

<!--more-->

## Punti principali

- **Conferma l'incompatibilità.** Confronta l'errore del log di Core con la versione installata e la versione dello storage HTTP.
- **Conserva il file.** Prima del ripristino, mantieni una copia invariata e un backup fuori dal dispositivo.
- **Verifica il risultato.** Controlla lo stato di Core, la porta di ascolto salvata, la dashboard e la versione installata.

**Correzione per questo caso specifico:** [Conserva il file HTTP](#preserve-recovery-options), [crea e convalida un candidato versione 2.2](#apply-the-tested-fix-for-version-31), [installalo dopo aver arrestato Core](#apply-the-tested-fix-for-version-31) e [verifica il risultato dell'aggiornamento](#verify-the-update-outcome). La conversione controlla i campi originali e si interrompe se non corrispondono. Non applicarla a un file HTTP non ispezionato.

## Prima di iniziare

Servono accesso fisico a un Yellow CM4, un cavo dati USB-C, una console seriale funzionante e un backup utilizzabile o una configurazione conservata. La procedura manuale richiede accesso alla shell dell'host e un controllo accurato del JSON. Dedica almeno 30 minuti alla diagnosi e alla riparazione. L'avvio di Core e il ripristino dei backup richiedono più tempo nelle installazioni grandi.

## Riconosci il problema

L'errore decisivo compariva nel log di Core:

```text
Storage file http has version 3 which is newer than the max supported version 2
```

La versione precedente di Core non riusciva a caricare `http`. Anche il frontend e gli altri componenti che dipendono da HTTP non funzionavano. Un lease del router e una pagina Observer operativa non dimostravano che la dashboard fosse accessibile. [Il problema n. 190583 di Home Assistant Core](https://github.com/home-assistant/core/issues/190583) documenta lo stesso errore di rollback in diverse installazioni, compresa Yellow. [Il mio commento al problema](https://github.com/home-assistant/core/issues/190583#issuecomment-6908185955) registra il ripristino testato su questo Yellow e lo stato finale di Core.

**Causa dell'interruzione web:** Core 2026.11 ha scritto `.storage/http` nel formato 3.1. Il rollback ha ripristinato Core 2026.10.4, ma non un file HTTP compatibile. Core 2026.10.4 rifiuta la versione di storage 3. Anche il profilo `intermediate_v6` salvato su questo Yellow non è conforme allo schema precedente. Non si conosce il motivo del primo aggiornamento non riuscito e del conseguente rollback. Al 2026-11-15, il problema collegato era aperto e la discussione non conteneva una soluzione confermata dai manutentori.

Controlla la versione installata di Core e lo storage HTTP prima di modificare i file:

```bash
ha core info --raw-json | jq -r '.data.version'

storage=/mnt/data/supervisor/homeassistant/.storage
jq '{version, minor_version, pending_present: (.data.pending != null), profile: .data.stable.ssl_profile}' "$storage/http"
ha core logs | grep -F 'Storage file http has version 3'
```

L'output seguente mostra questo caso con timestamp e dettagli privati rimossi:

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

I comandi di ripristino confrontano la porta di ascolto salvata da Supervisor con il file HTTP senza visualizzare nessuno dei due valori. Se non corrispondono, controlla la porta effettiva di Core prima di modificare i file.

| Segnale | Significato |
| --- | --- |
| Core supporta la versione di storage 2, il file indica la versione 3 | La versione precedente non può caricare le impostazioni HTTP salvate |
| Il file HTTP e l'elenco di Supervisor indicano porte di ascolto diverse | Controlla la porta effettiva di Core prima di attribuire la causa |
| La pagina iniziale risponde, ma Core è ancora in stato STARTING | La risposta del frontend non dimostra che l'avvio sia terminato |

## Conserva le opzioni di ripristino {#preserve-recovery-options}

Prima di un altro aggiornamento, conserva un backup utilizzabile fuori da Yellow. [La guida ai backup di Home Assistant](https://www.home-assistant.io/common-tasks/general/backups/) descrive posizioni cloud e fuori dal dispositivo. Un backup cifrato richiede la relativa chiave di ripristino. Non cancellare il disco dati NVMe mentre diagnostichi questa incompatibilità dello storage.

Copia il file HTTP prima di modificarlo:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
test ! -e "$storage/http.before-recovery" &&
  cp -p "$storage/http" "$storage/http.before-recovery" &&
  cmp -s "$storage/http" "$storage/http.before-recovery"
```

Interrompi se il comando non riesce. Lascia intatta un'eventuale copia di ripristino precedente con lo stesso nome. Scegli un nuovo nome e ripeti il controllo prima di continuare.

Se la dashboard non è disponibile, usa la console seriale di Yellow. [La guida di Nabu Casa per Linux e macOS](https://support.nabucasa.com/hc/en-us/articles/25454972435357-Using-the-serial-console-on-Home-Assistant-Yellow-for-debugging-Linux-macOS) mostra il collegamento USB-C e la posizione dell'UART JP1. Segui le istruzioni CM4 adatte al tuo hardware.

## Applica la correzione testata per la versione 3.1 {#apply-the-tested-fix-for-version-31}

La soluzione preferita è usare un file HTTP compatibile precedente all'aggiornamento. Ripristina il backup tramite la procedura documentata di Home Assistant quando è appropriato un ripristino completo. Se estrai un singolo file, confermane la versione di storage e la porta di ascolto salvata prima di sostituire il file attivo. I comandi seguenti sono la correzione diretta testata su questo Yellow quando non era disponibile un file HTTP compatibile.

[La soluzione temporanea originale del problema](https://github.com/home-assistant/core/issues/190583) sposta `.storage/http` e lascia che la versione precedente di Core crei un nuovo file. Un [rapporto successivo su Yellow](https://github.com/home-assistant/core/issues/190583#issuecomment-6749568119) mostra una porta di ascolto diversa nel file ricreato. Controlla il nuovo file e `ha core info` prima di concludere che l'interfaccia web sia tornata a funzionare.

La mia installazione non aveva un blocco YAML `http:`, una configurazione HTTP in sospeso o un certificato TLS o una chiave nelle impostazioni stabili. Il profilo salvato era `intermediate_v6`. In questo caso circoscritto, ho creato un candidato separato versione 2.2 e mantenuto la porta di ascolto esistente:

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

Tutti i comandi precedenti devono riuscire prima di sostituire il file attivo. Se `jq` non riesce, ispeziona il candidato prima di eliminarlo e riprovare. [Il codice HTTP di Core 2026.10.4](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/http/config.py) definisce la versione di storage 2.2 e accetta il profilo `intermediate`. [Il codice di Core 2026.11.1](https://github.com/home-assistant/core/blob/2026.11.1/homeassistant/components/http/config.py) usa la versione 3.1 e nomi di profilo versionati. Prima dell'installazione, ho anche convalidato il candidato con `HTTP_STORAGE_SCHEMA` della versione precedente di Core installata.

Esegui il controllo dello schema della versione precedente di Core installata mentre il suo container è ancora in esecuzione:

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

Interrompi se lo schema rifiuta il candidato. Questo passaggio non convalida tutte le integrazioni né tutte le forme non testate dello storage HTTP.

Il controllo dello schema ha stampato `Schema accepted` per questo candidato. Qualsiasi altro risultato interrompe questa procedura di ripristino.

Questa conversione manuale è stata testata con i campi indicati. Un file con impostazioni TLS, proxy attendibili o una configurazione in sospeso richiede una verifica specifica. Modificare solo il numero di versione principale lascia un profilo che la versione precedente di Core non accetta.

Nel mio caso Supervisor aveva un'attività Core attiva e ha rifiutato `ha core stop`. Ho arrestato il container Core dalla console dell'host, installato il candidato convalidato e poi l'ho avviato:

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

Se un comando non riesce dopo l'arresto, controlla il file HTTP attivo prima di eseguire `docker start homeassistant`. Se il file è cambiato, crea un nuovo candidato dai suoi contenuti aggiornati. Dopo questo passaggio la pagina HTTP è tornata. Una risposta HTTP non dimostrava che Core avesse completato l'avvio, quindi ho controllato lo stato di Supervisor prima di considerare ripristinato il sistema.

Su questo Yellow, `docker inspect -f '{{.State.Status}}' homeassistant` ha quindi stampato `running`. Controlla `ha core info` e la dashboard prima di richiedere un altro aggiornamento.

## Verifica il risultato dell'aggiornamento {#verify-the-update-outcome}

Dopo aver recuperato l'accesso HTTP, ho aggiornato Core alla versione 2026.11.1. Per richiedere questa versione:

```bash
ha core update --version 2026.11.1
```

Dopo un avvio lungo, il comando ha segnalato un errore. Supervisor ha poi registrato Core come RUNNING e ha riportato `Successfully started Home Assistant 2026.11.1`. Una verifica dello stato ha mostrato che la versione installata era aggiornata, il file HTTP era migrato di nuovo alla versione 3.1 e il container non si era riavviato durante l'osservazione. La dashboard autenticata si è caricata. **Controlla lo stato finale anche quando il comando di aggiornamento segnala un errore.**

Sul tuo sistema, dopo un aggiornamento lungo controlla la versione, lo stato di Supervisor e quello del container:

```bash
ha core info --raw-json | jq '{version: .data.version, update_available: .data.update_available}'
ha supervisor info --raw-json | jq '{healthy: .data.healthy, supported: .data.supported}'
docker inspect -f '{{.State.Status}} restarts={{.RestartCount}}' homeassistant
```

In questo caso, il primo e il terzo comando hanno prodotto i seguenti risultati ripuliti:

```text
{
  "version": "2026.11.1",
  "update_available": false
}
running restarts=0
```

Poi apri la dashboard all'indirizzo locale abituale e conferma che gli stati aggiornati si carichino. Conserva il file HTTP salvato finché non viene completato un backup successivo e non è verificato il funzionamento normale.

Le prove raccolte sul mio Yellow non hanno stabilito la causa del primo aggiornamento non riuscito. Nemmeno il messaggio di errore dell'attività successiva ne indicava una. Una versione installata e una dashboard funzionante sono prove dello stato finale più solide del solo messaggio CLI, ma nessuna delle due spiega perché Supervisor abbia contrassegnato l'attività come non riuscita.

## Passaggi successivi

Se l'errore dello storage HTTP persiste, ispeziona il file conservato e ripristina un backup compatibile oppure esegui una versione di Core in grado di leggere la sua versione di storage. Ripristinare il file conservato versione 3 sotto la versione precedente di Core ripete il problema. Se Core arriva a RUNNING ma alcuni dispositivi restano indisponibili, esamina separatamente le relative integrazioni. Conserva la copia di ripristino e il backup cloud finché non termina il backup successivo e la dashboard continua a rispondere.
