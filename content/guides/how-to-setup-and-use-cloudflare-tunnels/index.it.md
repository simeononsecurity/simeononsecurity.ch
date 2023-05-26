---
title: "Impostazione dei tunnel Cloudflare: Semplificare e proteggere il traffico di rete"
draft: false
toc: true
date: 2023-05-26
description: "Imparate a configurare i tunnel Cloudflare per ottimizzare e proteggere il traffico di rete, migliorando le prestazioni e la sicurezza."
tags: ["Tunnel Cloudflare", "Sicurezza di rete", "Prestazioni del sito web", "Server proxy", "Web Traffic", "Configurazione della rete", "Server Ubuntu", "Account Cloudflare", "Autenticazione", "Creazione del tunnel", "Instradamento del traffico", "Registri DNS", "Connessione sicura", "Hosting del sito web", "Servizio Proxy", "Protezione della rete", "Ottimizzazione delle prestazioni", "Integrazione di Cloudflare", "Configurazione del server", "Crittografia del traffico", "Gestione del traffico di rete", "Hosting web sicuro", "Sicurezza del sito web", "Configurazione di Ubuntu", "Tecnologia di tunneling", "Servizi Cloudflare", "Prestazioni di rete", "Sicurezza web", "Sicurezza del server", "Gestione del traffico", "Proxy Cloudflare"]
cover: "/img/cover/An_illustration_showing_a_network_tunnel_connecting_a_local.png"
coverAlt: "Un'illustrazione che mostra un tunnel di rete che collega un server locale al logo Cloudflare, a simboleggiare il traffico di rete sicuro e snello."
coverCaption: ""
---

**Guida all'impostazione dei tunnel Cloudflare**

## Introduzione
I tunnel Cloudflare offrono un modo sicuro per ospitare siti web stabilendo una connessione diretta tra la rete locale e Cloudflare. Questa guida vi guiderà attraverso il processo di impostazione dei tunnel Cloudflare per migliorare la sicurezza e le prestazioni del vostro sito web.

______

## Perché Cloudflare Tunnel?
I tunnel Cloudflare offrono diversi vantaggi, tra cui la riduzione dei vettori di attacco e la semplificazione delle configurazioni di rete. Utilizzando Cloudflare come proxy, è possibile chiudere le porte esterne e garantire che tutto il traffico passi attraverso la rete sicura di Cloudflare. Questo fornisce un ulteriore livello di protezione per il vostro sito web.

______

## Prerequisiti
Prima di configurare Cloudflare Tunnels, assicurarsi di disporre di quanto segue:

1. Un account Cloudflare attivo.
2. Un server con Ubuntu.

______

## Passo 1: Installazione
Per iniziare, è necessario installare il pacchetto Cloudflare Tunnels sul server Ubuntu. Seguite questi passaggi:

1. Aprite il terminale sul vostro server Ubuntu.
2. Scaricate l'ultima versione del pacchetto Cloudflare Tunnels eseguendo il seguente comando:

```shell
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
```

## Passo 2: Autenticazione
Successivamente, è necessario autenticare il proprio account Cloudflare con il servizio Cloudflare Tunnels. Seguire questi passaggi:

1. Eseguite il seguente comando nel terminale:

```shell
cloudflared tunnel login
```

2. Fare clic sul sito che si desidera utilizzare con il tunnel per completare il processo di autenticazione.

## Fase 3: creazione di un tunnel

Ora è il momento di creare il tunnel Cloudflare. Seguite questi passaggi:

1. Eseguite il seguente comando nel terminale per creare un tunnel:

```shell
cloudflared tunnel create name_of_tunnel
```

2. Scegliere un nome per il tunnel che sia memorabile e descrittivo. Si noti che il nome del tunnel non può essere modificato in seguito.

3. Dopo la creazione del tunnel, verranno fornite informazioni importanti, tra cui l'UUID del tunnel. Prendere nota di questo UUID perché sarà necessario per la configurazione successiva.

4. Per visualizzare un elenco di tutti i tunnel attivi, utilizzare il comando:

```shell
cloudflared tunnel list
```

In questo modo verranno visualizzati i nomi e gli UUID dei tunnel.

### Passo 4: Configurazione del tunnel

Per configurare il tunnel e iniziare a instradare il traffico, procedere come segue:

1. Navigare nella directory Cloudflare Tunnels sul proprio server. La posizione predefinita è `/etc/cloudflared`

2. All'interno di questa directory, creare un nuovo file denominato `config.yml` utilizzando un editor di testo di vostra scelta.

3. Popolate il file config.yml con i seguenti contenuti:

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json
```

Assicurarsi di sostituire `<your_tunnels_uuid>` con l'UUID del tunnel e, se necessario, aggiornare il percorso del file delle credenziali.

## Passo 5: Instradamento del traffico

Per specificare i servizi interni che si desidera servire attraverso il tunnel, procedere come segue:

1. `Open the ` di nuovo il file.

2. Aggiungere i parametri di ingresso al file per definire i servizi che si desidera instradare attraverso Cloudflare. Ad esempio:

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json

ingress:
  - hostname: example.com
    service: http://10.10.10.123:1234
  - hostname: subdomain.example.com
    service: http://10.10.10.123:8888
  - service: http_status:404

```

Sostituire `<your_tunnels_uuid>` con l'UUID del tunnel e aggiornare il nome dell'host e i dettagli del servizio in base alla configurazione.

3. Salvare il file config.yml.


## Passo 6: Creare i record DNS

Per creare i record DNS per il nome host e i servizi del tunnel, seguire i passaggi seguenti:

1. Aprire il terminale.

2. Utilizzate il seguente comando per creare un record DNS:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> <hostname>
```
Sostituire `<UUID or NAME of tunnel>` con l'UUID o il nome della galleria e `<hostname>` con il nome host desiderato per il servizio.

3. Ad esempio, per creare un record DNS per example.com, eseguire il comando:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> example.com
```

Si noti che le modifiche si rifletteranno nella sezione DNS della dashboard di Cloudflare.

## Passo 7: Avvio del tunnel

Per testare e avviare il tunnel Cloudflare, seguire i seguenti passaggi:

1. Aprite il terminale.

2. Eseguite il seguente comando per avviare il tunnel:

```shell
cloudflared tunnel run <UUID or NAME of tunnel>
```

Sostituire `<UUID or NAME of tunnel>` con l'UUID o il nome del tunnel.

3. Cloudflared imposterà il tunnel e visualizzerà le informazioni sul suo stato. Una volta che il tunnel è attivo e funzionante, si può passare alla fase successiva.

4. Per evitare che il tunnel si chiuda quando si esce dal terminale, è necessario eseguire Cloudflared come servizio systemd. Utilizzare il seguente comando:

```shell
cloudflared --config /path/to/config.yml service install
```

Sostituire `/path/to/config.yml` con il percorso del vostro file `config.yml` file.

## Conclusione

In questa guida abbiamo illustrato i passaggi per configurare i tunnel di Cloudflare su Ubuntu. Seguendo queste istruzioni, potrete migliorare la sicurezza e le prestazioni del vostro sito web sfruttando la rete di Cloudflare. Ricordate di monitorare regolarmente i tunnel e di regolare la configurazione se necessario.

Se si riscontrano problemi o si ha bisogno di ulteriore assistenza, fare riferimento alla sezione [official Cloudflare Tunnels documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)


## Riferimenti
- [Cloudflare Tunnels Documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)
- [Cloudflare Tunnels GitHub Repository](https://github.com/cloudflare/cloudflared)
- [tcude - How to Set Up Cloudflare Tunnels on Ubuntu](https://tcude.net/creating-cloudflare-tunnels-on-ubuntu/)