---
title: "Open WebUI v0.12.4: checklist per aggiornamento e controllo degli accessi 2026"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "Esegui il backup e aggiorna Open WebUI alla versione v0.12.4. Poi prova la condivisione delle chat, le autorizzazioni di esportazione, le concessioni delle risorse, gli account e l'accesso alla rete."
genre: ["IA self-hosted", "Sicurezza informatica", "Amministrazione di sistema"]
tags: ["Open WebUI", "Open WebUI v0.12.4", "aggiornamento Open WebUI", "sicurezza Open WebUI", "controllo accessi Open WebUI", "IA self-hosted", "aggiornamento Docker", "aggiornamento pip", "backup Open WebUI", "autorizzazioni Open WebUI", "ruoli Open WebUI", "gruppi Open WebUI", "autorizzazione esportazione chat", "chat condivise", "chat archiviate", "accesso alla knowledge base", "accesso ai modelli", "autorizzazioni degli strumenti", "sicurezza chiavi API", "sicurezza account amministratore", "disattivare le registrazioni", "autenticazione proxy inverso", "accesso VPN", "fissare la versione dell'immagine del container"]
---

**Open WebUI v0.12.4 include correzioni di sicurezza che i responsabili non hanno ancora descritto nel dettaglio.** Le note di rilascio raccomandano di aggiornare presto le installazioni e dichiarano che seguiranno avvisi dopo l'assegnazione dei CVE. Le modifiche indicate di seguito alla condivisione delle chat e alle autorizzazioni sono quelle visibili nelle note, non un elenco completo delle correzioni di sicurezza non ancora divulgate. [Note di rilascio Open WebUI v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

<!--more-->

## Punti chiave

- **Esegui prima il backup.** Conserva una copia ripristinabile del volume dati o del database e dei caricamenti prima di modificare l'applicazione.
- **Fissa il rilascio ufficiale.** Usa `ghcr.io/open-webui/open-webui:v0.12.4` per l'immagine Docker standard oppure `open-webui==0.12.4` per pip.
- **Prova le autorizzazioni con ruoli utente reali.** Un pulsante nascosto non dimostra che l'API esegua un controllo di autorizzazione.
- **Mantieni privato l'accesso.** Richiedi l'autenticazione dell'applicazione e limita l'accesso alla rete tramite VPN o proxy inverso autenticato.

## Prima dell'aggiornamento

**Prerequisiti:** identifica il metodo d'installazione attuale, la variante dell'immagine container, la posizione dei dati persistenti, il database esterno, il proxy inverso e il provider di autenticazione. Pianifica una finestra di fermo e conserva la configurazione corrente del container o la definizione del servizio. Dedica tempo a una prova di ripristino su un'istanza separata. I comandi seguenti sono modelli documentati dal fornitore e adattati a questa versione fissata. Non sono il risultato di un aggiornamento reale eseguito per questa guida. [Aggiornare Open WebUI](https://docs.openwebui.com/getting-started/updating/)

1. **Inventaria l'archiviazione.** Nella configurazione Docker standard, `open-webui` monta `/app/backend/data`. Registra i bind mount, il database esterno, lo storage a oggetti e le variabili d'ambiente personalizzate. Con pip, individua la directory dati attiva dell'applicazione e il database prima di modificare l'ambiente. Non presumere che l'esportazione delle chat sia un backup completo.
2. **Esegui il backup dopo aver fermato le scritture.** Arresta l'applicazione o crea uno snapshot coerente del database, poi copia il volume, gli eventuali database esterni e i caricamenti in uno spazio di archiviazione separato. Il fornitore documenta un archivio del volume Docker. Adatta il nome del volume e il percorso di backup alla tua installazione. Verifica che l'archivio si apra e prova un ripristino su un'istanza separata prima di farvi affidamento. [Backup e ripristino](https://docs.openwebui.com/getting-started/updating/#backup--restore)
3. **Leggi le note di rilascio e le indicazioni per la migrazione.** Le note v0.12.4 non elencano le correzioni di sicurezza in attesa e non specificano le versioni interessate. Non attribuire un CVE a tali correzioni e non presumere che ogni versione precedente a v0.12.4 sia vulnerabile a un difetto specifico. La guida di aggiornamento avverte che alcune migrazioni del database sono irreversibili e che le repliche con versioni diverse creano problemi. Se più worker o repliche condividono un database, fermali insieme e segui la [procedura di migrazione per più repliche](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations). Per il rollback potrebbe servire il backup del database precedente all'aggiornamento.

## Aggiorna il pacchetto installato

**Docker, procedura del fornitore adattata a un tag fissato:** dopo il backup, scarica l'immagine standard ufficiale e ricrea il container con lo *stesso* volume persistente, la stessa configurazione e lo stesso `WEBUI_SECRET_KEY`. L'esempio presuppone il volume denominato predefinito e un proxy upstream associato localmente. Non incollare la chiave reale nella cronologia della shell. Forniscila tramite il meccanismo protetto di ambiente o di gestione segreti già in uso. Conserva le opzioni GPU, Ollama, rete personalizzata, database e tutte le altre della configurazione attuale. [Aggiornare Open WebUI](https://docs.openwebui.com/getting-started/updating/) · [Tag ufficiali delle immagini](https://docs.openwebui.com/getting-started/quick-start/)

```bash
docker pull ghcr.io/open-webui/open-webui:v0.12.4
docker rm -f open-webui
docker run -d --name open-webui --restart always \
  -p 127.0.0.1:3000:8080 \
  -v open-webui:/app/backend/data \
  --env-file ./open-webui.env \
  ghcr.io/open-webui/open-webui:v0.12.4
```

**Controlla `./open-webui.env` prima di eseguire il comando:** il file deve già esistere, avere permessi restrittivi e contenere il `WEBUI_SECRET_KEY` attuale e la configurazione necessaria. Il binding loopback è adatto a un proxy sullo stesso host, non a un proxy su un'altra macchina. Con Compose, modifica solo l'immagine del servizio impostando il tag fissato, poi esegui `docker compose pull open-webui` e `docker compose up -d open-webui` nel progetto esistente. Mantieni lo stesso volume e la stessa configurazione d'ambiente. Sono comandi suggeriti, non una migrazione collaudata della tua installazione.

**pip, procedura del fornitore per una versione fissa:** nell'ambiente virtuale esistente, arresta il servizio, installa la versione esatta del pacchetto e riavvialo con la stessa directory dati e lo stesso ambiente. Evita un secondo ambiente Python o un nuovo database vuoto. L'istruzione generica del fornitore usa `pip install -U open-webui`. Il vincolo seguente fissa questa checklist a v0.12.4. [Aggiornare Open WebUI](https://docs.openwebui.com/getting-started/updating/) · [Guida rapida](https://docs.openwebui.com/getting-started/quick-start/)

```bash
python -m pip install --upgrade 'open-webui==0.12.4'
python -m pip show open-webui
```

**Verifica il servizio in esecuzione, non solo il pacchetto installato.** Controlla la versione all'avvio in `docker logs open-webui` o nei log del servizio pip e confrontala con quella visualizzata dall'applicazione dopo l'accesso. La guida di aggiornamento del fornitore consiglia di controllare i log del container e aprire la pagina di accesso. Se l'interfaccia mostra risorse obsolete, forza l'aggiornamento del browser. Se l'avvio segnala un errore di migrazione, lascia il servizio fermo finché non hai individuato il problema. Non ripristinare un binario precedente su un database migrato senza verificare i requisiti di ripristino. [Controlli post-aggiornamento](https://docs.openwebui.com/getting-started/updating/)

## Verifica gli accessi dopo il riavvio

**Comportamento dichiarato dal fornitore:** v0.12.4 nasconde le azioni per esportare cartelle, esportare chat archiviate e copiare chat agli utenti senza **Allow Chat Export**. Nasconde anche i controlli di accesso su modelli, prompt, strumenti, conoscenze, skill, note e cartelle agli utenti senza la relativa autorizzazione di condivisione. Chi visualizza una cartella condivisa non riceve più aggiornamenti in tempo reale della chat dopo che il proprietario l'ha archiviata. Chi visualizza un link di condivisione non riceve più aggiornamenti in tempo reale dopo che il proprietario ha annullato la condivisione di tutte le chat. I controlli nascosti descrivono il comportamento dell'interfaccia, non provano una correzione sul server di una vulnerabilità non specificata. [Note di rilascio](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

**Verifica consigliata per l'operatore:** con un account di prova privo delle autorizzazioni di esportazione e condivisione, controlla che le azioni indicate non siano presenti. Con un account autorizzato, conferma che le azioni previste funzionino ancora. Crea una chat di prova non sensibile in una cartella condivisa, visualizzala da un altro account, archiviala come proprietario e verifica che gli aggiornamenti nuovi non arrivino più all'altro utente. Ripeti con un link di condivisione e **Unshare All Chats**. Ricontrolla le concessioni salvate e i vecchi link. Non presumere che i contenuti archiviati o le copie storiche siano stati cancellati.

| Area di verifica | Cosa controllare |
|---|---|
| **Ruoli e gruppi** | Rimuovi membri e assegnazioni di amministratore non più validi. Controlla le autorizzazioni effettive di un nuovo utente approvato e di uno con restrizioni. |
| **Modelli e strumenti** | Verifica le concessioni di accesso per ogni modello, gli strumenti associati, i diritti per creare strumenti e le credenziali del provider. Prova con un account non amministrativo. |
| **Conoscenze e file** | Controlla i collaboratori della knowledge base, le concessioni sulle risorse, gli allegati e le impostazioni di condivisione. Verifica un account a cui è stato revocato l'accesso. |
| **Chat ed esportazioni** | Controlla cartelle condivise, link, chat archiviate e assegnazioni di Allow Chat Export. Revoca i link non più necessari. |

Questi controlli d'inventario sono **raccomandazioni operative**, non nuove garanzie introdotte da v0.12.4. La [guida di hardening](https://docs.openwebui.com/getting-started/advanced-topics/hardening/) del fornitore descrive ruoli a più livelli, gruppi, concessioni per risorsa, autorizzazioni dell'area di lavoro, chiavi API e collocazione in rete.

## Colma le lacune di account e rete

- **Registrazione, impostazione del fornitore:** disattiva la registrazione aperta se un amministratore o un provider d'identità crea gli account. Controlla `ENABLE_SIGNUP` e le impostazioni persistenti dell'amministratore usando la [guida di hardening](https://docs.openwebui.com/getting-started/advanced-topics/hardening/). Mantieni restrittive le regole di approvazione per i nuovi account.
- **Chiavi API, controllo operativo:** inventaria le chiavi emesse, elimina quelle inutilizzate e limita creazione e accesso agli endpoint ai soli ruoli e percorsi necessari. Secondo la guida del fornitore, una chiave opera con le autorizzazioni del suo creatore. Tieni le chiavi fuori dagli esempi e dai log dell'applicazione.
- **Amministratori, controllo operativo:** rimuovi gli account amministratore abbandonati, applica controlli di accesso robusti, verifica la disponibilità di MFA e indaga sulle modifiche inattese degli account. Prova la procedura di recupero dell'account prima di disattivare un amministratore ridondante.
- **Perimetro di rete, indicazioni del fornitore:** colloca il servizio dietro una VPN, un proxy di accesso o un proxy inverso con autenticazione e lista consentita di indirizzi IP. Non esporlo pubblicamente senza autenticazione. Evita `WEBUI_AUTH=False` su un servizio raggiungibile. Un proxy inverso privo di autenticazione propria non sostituisce l'accesso all'applicazione. [Proteggere Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)

**Ambito:** questa checklist riguarda il rilascio ufficiale di Open WebUI e i percorsi d'installazione standard documentati. Non verifica fork, immagini derivate o pacchetti di terze parti. Le note v0.12.4 non dichiarano uno sfruttamento attivo. Consulta gli [avvisi di sicurezza del progetto](https://github.com/open-webui/open-webui/security/advisories) per le divulgazioni successive e per le rispettive versioni interessate e corrette. Non attribuire a v0.12.4 la correzione di un avviso precedente senza leggerne l'intervallo di versioni.

## Fonti e riferimenti

- [Note di rilascio Open WebUI v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)
- [Avvisi di sicurezza Open WebUI](https://github.com/open-webui/open-webui/security/advisories)
- [Aggiornare Open WebUI, inclusi backup, rollback e migrazioni](https://docs.openwebui.com/getting-started/updating/)
- [Guida rapida Open WebUI e tag ufficiali delle immagini](https://docs.openwebui.com/getting-started/quick-start/)
- [Proteggere Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)
- [Aggiornamenti e migrazioni per più repliche](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations)
