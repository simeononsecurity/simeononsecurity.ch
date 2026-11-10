---
title: "Perché Tailscale usa un relay: connessioni dirette, DERP e peer relay"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Scopri perché Tailscale usa un relay, come leggere l'output di status e netcheck e quando una connessione DERP o peer relay richiede un'indagine."
genre: ["Networking", "Network Security", "Self-Hosted"]
tags: ["Tailscale", "relay Tailscale", "DERP", "peer relay Tailscale", "connessione diretta", "WireGuard", "attraversamento NAT", "NAT difficile", "CGNAT", "UDP", "tailscale status", "tailscale ping", "tailscale netcheck", "MappingVariesByDestIP", "prestazioni VPN", "accesso remoto", "tailnet", "rete homelab", "latenza del relay", "crittografia end-to-end"]
cover: "/img/cover/why-tailscale-uses-a-relay.webp"
coverAlt: "Due portatili su isole separate scambiano pacchetti cifrati attraverso un relay centrale mentre un percorso diretto è interrotto."
coverCaption: ""
---

**Tailscale usa un relay** quando i dispositivi non hanno stabilito una connessione diretta. Una breve connessione DERP durante l'avvio è normale. L'uso persistente di un relay spesso dipende dalle condizioni di traduzione degli indirizzi di rete (NAT) o del firewall che influiscono sul percorso tra i dispositivi. Le connessioni dirette, DERP e peer relay mantengono tutte la crittografia end-to-end di WireGuard. [Tipi di connessione Tailscale](https://tailscale.com/docs/reference/connection-types).

## Punti chiave

- **Riconosci il percorso:** distingui le connessioni dirette, DERP e peer relay.
- **Raccogli prove:** esegui sonde specifiche per il peer e controlli di rete su entrambi i dispositivi.
- **Analizza lo schema:** confronta coppie di dispositivi e condizioni di rete.
- **Scegli una modifica:** giustificala con un carico di lavoro misurato e un nuovo test.

## Prima di iniziare

**Prerequisiti:** due dispositivi registrati e online, e un terminale con l'interfaccia a riga di comando di Tailscale, o **CLI**. L'accesso amministrativo serve solo se l'indagine porta a modifiche della configurazione.

**Tempo stimato:** cinque minuti per i controlli di base, poi 15–20 minuti per l'esercizio di confronto. **Difficoltà:** principiante per l'osservazione, intermedia per le modifiche di rete. Definisci prima il problema, ad esempio un backup lento o una risposta ritardata del terminale.

## Connessioni dirette, DERP e peer relay

Un **tailnet** è la tua rete Tailscale. I dispositivi tentano di stabilire una connettività UDP diretta. Quando il percorso diretto non riesce, sono disponibili i relay. Tailscale ricontrolla periodicamente le opzioni di connessione. [Stabilire una connessione](https://tailscale.com/docs/reference/connection-types).

| Percorso | Itinerario del traffico | Implicazione tipica |
|---|---|---|
| **Diretto** | Tra i due dispositivi | In genere il percorso preferito per le prestazioni |
| **Relay DERP** | Attraverso l'infrastruttura relay di Tailscale | Aggiunge un intermediario quando l'accesso diretto non riesce |
| **Peer relay** | Attraverso un dispositivo configurato nel tailnet | Un relay alternativo sotto la tua amministrazione |

Le **prestazioni DERP** dipendono in parte dal percorso aggiuntivo e dalla capacità condivisa del servizio. Tailscale documenta limiti di throughput per condividere equamente le risorse DERP. Non esiste una velocità universale del relay che permetta di prevedere il tempo di trasferimento dei file. [Risoluzione dei problemi di prestazioni Tailscale](https://tailscale.com/docs/reference/troubleshooting/poor-performance-tailnet).

## Comprendi la negoziazione della connessione

L'**attraversamento NAT** è il processo che stabilisce un percorso utilizzabile attraverso dispositivi che traducono gli indirizzi. Tailscale avvia la comunicazione tramite DERP mentre negozia un percorso diretto. Se la connettività diretta non riesce, un peer relay configurato e disponibile offre un'altra opzione. Tailscale ricontrolla le opzioni nel tempo. [Stabilire una connessione](https://tailscale.com/docs/reference/connection-types).

Il **NAT difficile** descrive un comportamento di mapping che complica l'attraversamento. Le condizioni su entrambe le estremità sono importanti. Due dispositivi dietro router diversi non si comportano necessariamente allo stesso modo, anche se entrambe le reti usano indirizzi privati. [Connettività dei dispositivi](https://tailscale.com/docs/reference/device-connectivity).

Per **un portatile in mobilità**, il percorso verso il server di casa può cambiare quando passi dal Wi-Fi domestico alla rete di un hotel. Registra la rete usata durante l'osservazione. Una connessione diretta di ieri non dimostra quale sia il percorso di oggi.

## Controlla la connessione attuale

Sostituisci **`home-server`** con il nome Tailscale o l'indirizzo del peer:

```bash
tailscale ping home-server
tailscale status
tailscale netcheck
```

**`tailscale ping`** verifica la connettività con il peer indicato. **`tailscale status`** elenca i peer e i dettagli delle connessioni. **`tailscale netcheck`** riporta le condizioni del dispositivo su cui esegui il comando. Il [riferimento CLI di Tailscale](https://tailscale.com/docs/reference/tailscale-cli) documenta questi comandi.

| Indicatore nell'output | Interpretazione |
|---|---|
| **`direct`** | Il traffico verso questo peer usa un percorso diretto |
| **`relay`** | Il traffico verso questo peer passa da DERP |
| **`peer-relay`** | Il traffico usa un peer relay configurato |
| **Un primo pong DERP** | Controlla i risultati successivi prima di concludere che il percorso è rimasto sul relay |

Queste etichette provengono dalla [documentazione sui tipi di connessione](https://tailscale.com/docs/reference/connection-types). **Genera prima traffico**, poi controlla il peer che ti interessa. I comandi sopra sono esempi, non risultati acquisiti da un benchmark.

## Interpreta un cambio di percorso

Questa **sequenza illustrativa** omette indirizzi e tempi per concentrare l'attenzione sul cambio di connessione:

```text
Prima risposta:    tramite DERP
Risposta successiva: tramite un endpoint diretto
Status successivo: diretto
```

**Interpretazione:** durante questa osservazione la negoziazione è riuscita. La prima risposta da sola avrebbe portato a una diagnosi errata. Se le risposte successive e lo status indicano ancora un relay, registra un relay persistente per questa coppia di dispositivi e per il periodo di test.

**Ambito della sonda:** un ping Tailscale riuscito conferma la connettività con il peer per quella sonda. Non dimostra che la dashboard, il servizio file o il demone SSH accettino il traffico applicativo. Prima di dichiarare risolto il problema, prova separatamente l'applicazione che non funziona.

## Cosa indica netcheck

Esegui **`tailscale netcheck` su entrambi i dispositivi**. Confronta questi campi con il [riferimento sulla connettività dei dispositivi](https://tailscale.com/docs/reference/device-connectivity):

| Campo | Interpretazione utile |
|---|---|
| **`UDP`** | Se la sonda ha osservato connettività UDP in uscita |
| **`MappingVariesByDestIP`** | Mapping esterni variabili possono indicare un attraversamento NAT difficile |
| **`IPv6`** | Se questo dispositivo dispone di connettività IPv6 utilizzabile |
| **`PortMapping`** | Se è disponibile un meccanismo di port mapping supportato |

**Un solo campo non dà un verdetto.** La disponibilità di un meccanismo di mapping non prova che il percorso verso uno specifico peer funzioni. Anche l'etichetta relay non identifica il router responsabile. Confronta entrambi gli endpoint e i risultati effettivi dei ping.

Il **NAT dell'operatore** è rilevante quando la traduzione a monte non è sotto il tuo controllo, come spieghiamo nella guida sul [port forwarding di T-Mobile Home Internet](/articles/t-mobile-home-internet-port-forwarding/). Non presumere che ogni connessione dietro il NAT dell'operatore abbia lo stesso comportamento di attraversamento.

## Confronta tre coppie di dispositivi

Se disponibile, usa un **terzo dispositivo registrato** per migliorare le prove. Lo schema seguente è ipotetico, non è un risultato misurato:

| Coppia di dispositivi | Percorso osservato |
|---|---|
| **Portatile verso server di casa** | DERP |
| **Portatile verso un altro server** | Diretto |
| **Server di casa verso un altro server** | DERP |

**Ipotesi di lavoro:** indaga prima la rete del server di casa, perché entrambi i percorsi osservati che lo coinvolgono sono rimasti sul relay. È un indizio, non una prova. Ogni coppia negozia in modo indipendente e il server di confronto ha condizioni di rete proprie.

**Prossima osservazione:** raccogli i risultati di netcheck su tutti e tre i dispositivi e ripeti il test portatile-server di casa da un'altra rete sotto il tuo controllo. Se il percorso cambia, registra esattamente quale rete è cambiata. Non attribuire il risultato a una specifica impostazione del firewall prima di averla provata.

**Esercizio:** la connessione portatile-server di casa è diretta, ma il trasferimento di file resta lento. In base a questa osservazione, il relay non spiega più il problema. Controlla la connessione di upload sottostante, il carico del server, lo spazio di archiviazione e il comportamento dell'applicazione prima di cambiare le impostazioni del relay.

## Scegli una modifica mirata

Inizia con un **test comparativo** su un'altra rete sotto il tuo controllo. Se lo stesso peer diventa diretto, hai prove utili sul percorso della rete originale. Esamina le restrizioni UDP e la configurazione NAT prima di modificare impostazioni DNS o applicative non correlate.

**Modifica una sola variabile**, ripeti i controlli e misura lo stesso carico di lavoro. Registra direzione del trasferimento, dimensione del file, tempo trascorso e tipo di connessione. Così distingui il miglioramento del percorso da un cambiamento indipendente del carico del server o dello spazio di archiviazione.

Le **modifiche al firewall** devono seguire le indicazioni specifiche per la piattaforma e le prove raccolte. Aprire una porta applicativa su Internet pubblico non migliora di per sé il percorso di trasporto di Tailscale. Limita le modifiche al traffico necessario e alla rete che amministri. [Indicazioni firewall di Tailscale](https://tailscale.com/docs/integrations/firewalls).

| Risultato | Modifica da valutare |
|---|---|
| **La sonda UDP fallisce** | Esamina le restrizioni UDP in uscita su questa rete |
| **Il mapping cambia in base alla destinazione** | Esamina il comportamento NAT sulle apparecchiature che gestisci |
| **Percorso diretto, applicazione lenta** | Indaga l'host, la connessione sottostante e il carico di lavoro |
| **Relay funzionante, esperienza accettabile** | Mantieni la configurazione e documenta il valore di riferimento |

*Preferisci un miglioramento misurato alla modifica delle impostazioni eseguita soltanto per rimuovere l'etichetta relay.*

## Valuta un peer relay

Un **peer relay** richiede un host adatto, una porta UDP raggiungibile e una policy di accesso che ne consenta l'uso. Sia il relay sia i client partecipanti richiedono Tailscale 1.86 o versioni successive. Controlla le piattaforme host supportate prima di assegnare un dispositivo. [Requisiti dei peer relay](https://tailscale.com/docs/features/peer-relay).

**La posizione determina l'utilità.** Un dispositivo dietro lo stesso confine di rete non raggiungibile non aiuta gli altri peer finché la porta del relay non è raggiungibile.

**Costo di manutenzione:** qualcuno deve mantenere il relay online, aggiornato e adeguatamente dimensionato. Per l'amministrazione occasionale con latenza accettabile, confronta questo impegno con il beneficio misurato. Per trasferimenti grandi e ripetuti, misura il carico di lavoro attraverso il relay proposto prima di adottarlo.

## Controlla gli effetti del traffico condiviso

Il **traffico aggregato** merita attenzione quando un router di subnet o un exit node trasporta diversi carichi di lavoro tramite DERP. Tailscale documenta casi in cui molto traffico instradato tramite relay ritarda il traffico sensibile alla latenza che condivide la connessione. [Risoluzione dei problemi con NAT difficile](https://tailscale.com/docs/reference/troubleshooting/network-configuration/hard-nat-issues).

**Esercizio di confronto:** osserva la sessione interattiva prima, durante e dopo un backup di grandi dimensioni. Mantieni fissa la coppia di endpoint e registra il percorso ogni volta. I ritardi che compaiono durante il trasferimento giustificano un'indagine sul carico condiviso, ma non ne provano la causa esatta.

**Scegli il test successivo** in base all'osservazione. Controlla la saturazione del collegamento e il carico dell'host, poi valuta un percorso diretto o la separazione dei servizi sensibili alla latenza se la topologia lo permette. Non trattare un sintomo DNS come prova automatica di un errore di configurazione DNS.

## Un relay è un exit node?

Un **exit node** instrada il traffico Internet generale di un client attraverso un dispositivo selezionato del tailnet. Un relay trasporta il traffico tra peer Tailscale. Selezionare un exit node non garantisce un percorso diretto verso di esso. [Documentazione sugli exit node](https://tailscale.com/docs/features/exit-nodes).

## Crea un registro diagnostico

Conserva un **breve registro prima e dopo** per il problema effettivo:

```text
Data e versioni di Tailscale:
Dispositivi di origine e destinazione:
Reti usate da ciascun dispositivo:
Percorsi iniziale e stabilizzato della connessione:
Osservazioni netcheck da entrambi i lati:
Carico di lavoro, direzione e tempo trascorso:
Singola modifica provata:
Risultato del nuovo test:
Decisione di mantenere o annullare la modifica:
```

**Criterio di completamento:** il registro collega un sintomo specifico a osservazioni, un'ipotesi e un nuovo test misurato. “Il relay è scomparso” è incompleto se l'applicazione è ancora lenta. “Il backup rispetta il tempo richiesto tramite DERP” è un risultato valido se il requisito è esplicito.

**Usa `tailscale netcheck` come prova, non come verdetto.** Il comando descrive la rete vista da un singolo dispositivo. Il percorso stabilizzato riguarda una coppia di dispositivi e un carico di lavoro. Prima di modificare le impostazioni firewall o NAT, acquisisci entrambi gli endpoint, l'ultima riga di `tailscale status` e la misurazione dell'applicazione.

## Passaggi successivi

Registra il percorso verso il peer importante e misura il carico di lavoro prima di modificare le impostazioni di rete. Per la domanda separata su chi gestisce l'infrastruttura di coordinamento, leggi [Tailscale e Headscale a confronto](/articles/tailscale-vs-headscale-comparison-guide/).
