---
title: "Costruisci un home lab in 10 livelli, da Pi-hole all'IA locale"
date: 2026-10-27
lastmod: 2026-11-09
toc: true
draft: false
description: "Costruisci un home lab in dieci fasi pratiche, dal filtraggio DNS dell'intera rete all'IA locale, con hardware, costi, competenze e compromessi per ogni livello."
genre: ["Home lab", "Self-hosting", "IA locale", "Reti domestiche"]
tags: ["home lab", "Pi-hole", "Home Assistant", "Docker", "Jellyfin", "Plex", "NAS", "Proxmox", "Tailscale", "Ollama", "IA locale", "consumo energetico"]
cover: "/img/cover/build-home-lab-10-levels.webp"
coverAlt: "Un home lab cresce da un piccolo Raspberry Pi e un router fino a storage, server, apparecchiature di rete e una workstation per l'IA locale."
coverCaption: ""
---

Costruisci un home lab in 10 livelli, da Pi-hole all'IA locale
==============================================================

Un **home lab** è un insieme di computer e servizi che gestisci per risolvere problemi quotidiani e imparare a usare sistemi reali. Puoi bloccare annunci, automatizzare le luci, archiviare i contenuti multimediali della famiglia o provare macchine virtuali. **Inizia con un'attività utile.** Aggiungi hardware quando emerge un limite concreto.

Questa guida parte da un piccolo Raspberry Pi con Pi-hole e arriva a un server che esegue modelli di IA locali. **Ogni livello aggiunge funzionalità e una nuova responsabilità.** Le stime dei costi usano un consumo illustrativo e una tariffa di esempio pari a $0.15 per kilowattora. Controlla la tariffa locale e misura le apparecchiature prima di acquistare altro hardware.

## Livello 1: Blocca gli annunci in tutta la rete domestica

Installa [Pi-hole](https://docs.pi-hole.net/) su un Raspberry Pi o un altro piccolo computer Linux. Pi-hole funziona come un **sinkhole DNS**. Quando un dispositivo chiede l'indirizzo di un dominio presente in una blocklist, Pi-hole non restituisce una destinazione utilizzabile. Browser, telefono e smart TV applicano lo stesso filtro quando il router o il server DHCP indirizza i client a Pi-hole.

Il **filtraggio DNS** funziona anche fuori dai browser, inclusi alcuni annunci nelle app e nelle TV connesse. I contenuti incorporati nelle pagine restano fuori dal filtro, quindi gli annunci serviti dallo stesso dominio di un sito o di un'app passano. A volte una blocklist impedisce il caricamento di un accesso, un video o un checkout. Controlla il registro delle query di Pi-hole, autorizza il dominio specifico quando serve e prepara un DNS alternativo per le interruzioni.

Il consumo energetico è contenuto. Per un dispositivo da 8 watt acceso per tutto il mese, la stima è 8 W × 24 ore × 30 giorni ÷ 1.000 × $0.15 = **circa $0.86 al mese**. Misura l'alimentatore completo alla presa. Un secondo computer, un disco USB o un alimentatore inefficiente cambiano il totale.

**Imparerai:** DNS, DHCP, blocklist e manutenzione Linux di base.

## Livello 2: Automatizza i dispositivi smart in locale

Aggiungi [Home Assistant](https://www.home-assistant.io/), che riunisce dispositivi smart compatibili e automazioni in un unico sistema. Programma lo spegnimento delle luci all'ora di andare a letto. Accendi un ventilatore quando un sensore di temperatura supera una soglia. Ricevi una notifica quando un sensore di perdita rileva acqua. **Queste piccole automazioni offrono un vantaggio immediato.**

Il **controllo locale** mantiene attive molte automazioni in casa quando un servizio esterno o la connessione Internet non funzionano. Il comportamento dipende dal dispositivo. Alcuni prodotti richiedono comunque un account del fornitore, un servizio cloud o la connessione Internet per la configurazione e le funzioni remote. Controlla i requisiti dell'integrazione prima di comprare hardware.

**Esegui il backup di Home Assistant** e conserva una copia al di fuori dell'host. Documenta integrazioni e procedure di ripristino. Una scheda SD o un mini PC guasto non dovrebbe cancellare la configurazione.

**Imparerai:** integrazioni dei dispositivi, trigger, condizioni e ripristino dai backup.

## Livello 3: Esegui più servizi su un solo mini PC

Un **mini PC aziendale usato** spesso offre memoria espandibile, storage sostituibile e porte utili a un prezzo dell'usato contenuto. Un mini PC Intel N100 di solito consuma meno e occupa poco spazio. Intel descrive l'N100 come un processore a quattro core e quattro thread, con TDP di 6 watt e supporto fino a 16 GB di memoria. Il valore del processore non equivale al consumo dell'intero sistema misurato alla presa. Confronta il computer specifico, la memoria, lo storage, la garanzia e le porte di rete.

Installa Linux e usa [Docker](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) per eseguire servizi separati come **container**. Un container include un'applicazione e le sue dipendenze, condividendo il kernel del sistema operativo host. Per esempio, esegui un gestore di password come il progetto Vaultwarden mantenuto dalla community e un monitor di disponibilità come Uptime Kuma. **Tratta il gestore di password come un servizio sensibile:** limita l'accesso, usa un'autenticazione robusta, applica gli aggiornamenti e conserva un backup cifrato.

**I container non sostituiscono aggiornamenti o backup.** Assegna a ogni servizio una posizione di storage precisa e documenta le procedure di ripristino. Anche un mini PC ha dei limiti. Più database, conversioni multimediali o applicazioni grandi esauriscono memoria, storage o tempo CPU.

**Imparerai:** amministrazione Linux, container, volumi, aggiornamenti e ripristino dei servizi.

## Livello 4: Crea una libreria multimediale domestica

[Jellyfin](https://jellyfin.org/docs/) è un media server open source. [Plex](https://support.plex.tv/) offre un ecosistema di client rifinito e funzioni opzionali legate a un account. Entrambi organizzano librerie personali e trasmettono contenuti ai client supportati. **Scegli in base ai client**, al modello di accesso remoto, al supporto hardware e alle funzioni necessarie.

**Lo spazio di archiviazione** dipende dalle dimensioni e dalla qualità della raccolta. Inizia con un solo disco soltanto se hai già un piano di backup separato. Usa nomi di cartelle e metadati coerenti affinché il server abbini correttamente film ed episodi.

La **riproduzione diretta** invia un file compatibile al client senza modificare il flusso video. La **transcodifica** converte audio o video quando il client, la connessione, i sottotitoli o la qualità richiedono un formato diverso. La transcodifica aumenta il carico del server. Prova dispositivi e rete prima di comprare una GPU o una CPU più potente. **Evita un server multimediale dedicato** se tutti i client riproducono direttamente i file e un host soddisfa le tue esigenze.

**Imparerai:** formati multimediali, pianificazione dello storage, throughput di rete e test dei carichi di lavoro.

## Livello 5: Aggiungi ridondanza dello storage e un backup separato

Un NAS con due unità e **storage a specchio** scrive i dati su entrambi i dischi. Se un disco si guasta, l'altro conserva una copia aggiornata mentre sostituisci quello guasto e ricostruisci lo specchio. La duplicazione protegge la disponibilità in caso di guasto di un disco. **Uno specchio non ripristina** un file eliminato, non annulla la cifratura ransomware e non protegge da furto, incendio o evento elettrico che danneggi entrambi i dischi.

Conserva un **backup separato** su un altro dispositivo o in un'altra posizione. Includi documenti importanti, foto, esportazioni di configurazione e dati dei servizi. Usa una pianificazione dei backup e conserva versioni, così le modifiche accidentali non sovrascrivono tutte le copie integre.

**Prova un ripristino.** Scegli alcuni file, ripristinali in una cartella separata e aprili. Per un servizio, ripristina i dati in un'istanza di prova oppure documenta i passaggi e verifica ogni file. Un backup mai ripristinato è un'ipotesi, non un piano di ripristino.

**Imparerai:** file system, sostituzione dei dischi, rotazione dei backup e test di ripristino.

## Livello 6: Impara la virtualizzazione con un piccolo cluster Proxmox

[Proxmox VE](https://pve.proxmox.com/pve-docs/) esegue macchine virtuali e container su hardware server. Più mini PC uniti in un **cluster** condividono una vista di gestione e permettono di imparare nodi, storage e migrazione. Un cluster è un gruppo di server configurati per coordinarsi. I membri non sommano la memoria in un unico grande pool. **L'alta disponibilità richiede** ulteriore pianificazione e storage condiviso o replicato adeguato.

Uno **snapshot** registra lo stato di una macchina virtuale in un preciso momento, consentendo di tornare a uno stato precedente dopo una modifica nel lab. Di solito gli snapshot dipendono dallo storage originale. Non sono backup indipendenti. **Copia i dati importanti su una destinazione di backup separata** e prova il ripristino.

Ogni nodo aggiunge consumo energetico, porte di rete, cavi e aggiornamenti. Tre computer piccoli sono anche tre sistemi da aggiornare e diagnosticare. Un solo mini PC con alcune macchine virtuali insegna molte delle stesse basi a un costo inferiore. **Aggiungi nodi quando** gli esperimenti richiedono isolamento o vuoi esercitarti nella gestione dei cluster.

**Imparerai:** macchine virtuali, pool di storage, snapshot, appartenenza al cluster e manutenzione dei nodi.

## Livello 7: Aggiungi accesso remoto privato e separazione di rete

[Tailscale](https://tailscale.com/kb/) collega i dispositivi approvati tramite una rete privata, consentendo di accedere ad alcuni servizi domestici quando sei fuori casa. **Limita l'accesso** ai dispositivi e ai servizi necessari a ciascuna persona. Proteggi gli account con l'autenticazione a più fattori e controlla i vecchi dispositivi e le chiavi.

Uno switch gestito o un router con supporto **VLAN** separa i gruppi di dispositivi. Metti le prese smart e gli altri dispositivi meno affidabili su una rete diversa da quella dei computer con file personali. Colloca lo storage su una rete accessibile solo ai sistemi che ne hanno bisogno. La segmentazione limita le comunicazioni tra dispositivi. Mantieni anche aggiornamenti, password robuste e regole di accesso.

**Evita di esporre direttamente i pannelli di amministrazione su Internet** a meno che tu non conosca i requisiti di autenticazione, aggiornamento e firewall del servizio. Anche uno strumento di accesso privato richiede un controllo accurato degli account e dei dispositivi.

**Imparerai:** accesso privato, autorizzazioni basate sull'identità, VLAN, regole firewall e confini di fiducia dei dispositivi.

## Livello 8: Aggiungi un server enterprise

Passa a un server più grande quando hai misurato la necessità di più core CPU, memoria, alloggiamenti per dischi, slot PCIe o capacità di rete. I vecchi server enterprise spesso costano meno usati, ma le ventole sono rumorose e il **consumo in idle è di circa 100–160 watt**, a seconda del modello e dei componenti installati. Considera questo intervallo una stima, non una specifica.

Calcola una stima annuale dell'energia prima dell'acquisto:

`watt misurati ÷ 1.000 × 24 × 365 × tariffa elettrica per kWh`

Con 120 watt e $0.15 per kWh, la stima è 1.051 kWh all'anno, pari a circa **$158 all'anno**. Misura il server specifico in idle e con il carico abituale. Includi il consumo dei dischi, del raffreddamento e dell'UPS.

Controlla profondità del telaio, compatibilità dei dischi, rumore, controllo delle ventole, alimentatore e schede di espansione. Un server che supera il tuo budget di spazio o energia non è un aggiornamento pratico.

**Imparerai:** hardware server, gestione remota, espansione, raffreddamento e stime dei costi di esercizio.

## Livello 9: Misura l'energia e dimensiona correttamente il lab

Usa un **misuratore di potenza da presa** per misurare ogni computer in idle e durante l'uso normale. Elenca i maggiori consumatori. Controlla le impostazioni di risparmio energetico del BIOS, rimuovi schede e dischi inutilizzati e riporta i servizi quotidiani su mini PC efficienti quando l'hardware enterprise non serve.

Avvia il server grande solo quando un carico di lavoro ne richiede la capacità. Se usi una pianificazione Wake-on-LAN o il controllo remoto dell'alimentazione, documenta il ripristino in caso di guasti di rete o alimentazione. Tieni un **elenco delle dipendenze dei servizi** per evitare che gli spegnimenti interrompano storage o rete necessari ad altri sistemi.

Un rack aiuta a organizzare apparecchiature e flusso d'aria quando l'hardware rack giustifica lo spazio. Un UPS copre brevi interruzioni e dà ai sistemi il tempo di spegnersi correttamente. Entrambi aggiungono costi d'acquisto, spazio e consumo energetico. **Misura il loro consumo** e includi la sostituzione delle batterie nel budget a lungo termine.

**Imparerai:** misurazione energetica, gestione dell'alimentazione, mappatura delle dipendenze e pianificazione della capacità.

## Livello 10: Esegui modelli di IA in locale

[Ollama](https://docs.ollama.com/) scarica ed esegue sul computer i modelli linguistici supportati. L'**inferenza locale** mantiene prompt e risposte su hardware sotto il tuo controllo se usi un modello e un'applicazione locali. Verifica che l'intero percorso software resti locale. Un'app connessa, una funzione di telemetria o un'opzione di modello cloud invia dati fuori dalla rete.

I requisiti hardware dipendono dalle dimensioni del modello, dalla quantizzazione, dalla lunghezza del contesto e dalla velocità desiderata. **La memoria di sistema o quella della GPU deve contenere** i pesi del modello e il contesto di lavoro. I computer piccoli eseguono modelli più piccoli, mentre modelli grandi e contesti lunghi richiedono più memoria e spesso una GPU adeguata. Misura il consumo durante l'inferenza. Un sistema con GPU consuma spesso molta più energia di un mini PC in idle.

I modelli locali sono adatti ad attività come preparare bozze, riassumere note private e classificare contenuti in modo semplice, se la qualità soddisfa le tue esigenze. Producono risposte errate e spesso faticano con ragionamenti complessi o fatti aggiornati. I modelli cloud a volte funzionano meglio per attività specifiche. **Confronta qualità, privacy, latenza, costi e consumo energetico** prima di scegliere dove eseguire un carico di lavoro.

**Imparerai:** memoria dei modelli, quantizzazione, inferenza, confini della privacy e valutazione dei carichi di lavoro.

## Confronta i dieci livelli

**I costi sono stime, non preventivi.** I prezzi hardware variano per regione, condizione e configurazione dello storage. Stima l'elettricità con `watt ÷ 1.000 × ore × giorni × tariffa per kWh`. Quando possibile misura alla presa e includi le ore di idle, perché molti server domestici restano accesi tutto il giorno.

### Funzionalità e hardware

| Livello | Nuova funzionalità | Hardware tipico |
|---|---|---|
| **1** | Filtraggio DNS di rete | Raspberry Pi o piccolo host Linux |
| **2** | Automazione locale dei dispositivi | Pi o mini PC, dispositivi compatibili |
| **3** | Più app self-hosted | Mini PC aziendale usato o sistema N100 |
| **4** | Streaming dei propri contenuti | Mini PC e storage multimediale |
| **5** | Tolleranza ai guasti dei dischi e ripristino | NAS a due dischi e backup separato |
| **6** | Lab di server virtuali | Due o più mini PC |
| **7** | Accesso privato e segmentazione | Tailscale, router o switch gestito |
| **8** | Capacità elevata ed espansione | Server enterprise |
| **9** | Minore consumo energetico del lab | Misuratore di potenza, sistemi ottimizzati |
| **10** | Inferenza locale dei modelli | PC con molta memoria, GPU opzionale |

### Competenze, costi e compromessi

| Livello | Competenze acquisite | Stima dei costi ricorrenti | Compromesso principale |
|---|---|---|---|
| **1** | DNS, DHCP, Linux | Circa $1 al mese a 8 W e $0.15/kWh | Alcuni annunci restano e i falsi blocchi vanno controllati |
| **2** | Integrazioni, trigger, backup | Alimentazione host e costi dei dispositivi | Compatibilità e gestione dei backup |
| **3** | Docker, aggiornamenti, storage | Dipende dal consumo misurato del sistema | Limiti di CPU, memoria e disco |
| **4** | Formati, organizzazione, transcodifica | Storage e alimentazione server | A volte la transcodifica richiede più hardware |
| **5** | Mirroring, conservazione, ripristino | Alimentazione NAS, dischi, destinazione backup | Uno specchio non è un backup |
| **6** | Proxmox, VM, cluster | Ogni nodo aggiunge consumo e manutenzione | Più nodi significano più manutenzione |
| **7** | Regole di accesso, VLAN, firewall | Apparati di rete e costi dei servizi | Regole errate espongono i servizi |
| **8** | Hardware, raffreddamento, gestione remota | Dipende dal server, calcola dal consumo misurato | Rumore, calore e consumo in idle |
| **9** | Misurazione, pianificazione, dimensionamento | Costo una tantum del misuratore, risparmio variabile | La pianificazione aggiunge passaggi operativi |
| **10** | Distribuzione e valutazione dei modelli | Energia di calcolo e storage | Qualità e velocità dipendono dall'hardware |

## Scegli il prossimo aggiornamento utile

**Fermati al livello che soddisfa le tue esigenze attuali.** Pi-hole e un mini PC possono coprire i tuoi servizi. Un NAS è utile se ti serve storage condiviso e un piano di ripristino provato. Aggiungi un cluster o un server enterprise quando lo giustificano un carico di lavoro o un obiettivo di apprendimento.

Annota **dove si trovano i dati di ogni servizio, come aggiornarlo e come ripristinarlo.** Prova i backup prima di aggiungere altre apparecchiature. Lascia che il prossimo limite reale guidi l'acquisto successivo.

## Riferimenti

- [Documentazione Pi-hole](https://docs.pi-hole.net/)
- [Documentazione Home Assistant](https://www.home-assistant.io/docs/)
- [Specifiche del processore Intel N100](https://www.intel.com/content/www/us/en/products/sku/231803/intel-processor-n100-6m-cache-up-to-3-40-ghz/specifications.html)
- [Docker: Che cos'è un container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Documentazione Jellyfin](https://jellyfin.org/docs/)
- [Supporto Plex](https://support.plex.tv/)
- [Documentazione Proxmox VE](https://pve.proxmox.com/pve-docs/)
- [Documentazione Tailscale](https://tailscale.com/kb/)
- [Documentazione Ollama](https://docs.ollama.com/)
