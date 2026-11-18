---
title: "MeshCore o Meshtastic: confronto"
date: 2026-06-26
lastmod: 2026-11-12
toc: true
draft: false
description: "Confronta MeshCore e Meshtastic per instradamento, portata, tempo di trasmissione, infrastruttura, dispositivi supportati e impiego ideale."
genre: ["LoRa", "Reti mesh", "Comunicazioni offline", "Comunicazioni di emergenza", "Comunicazioni tattiche", "Radioamatori", "Open source", "Preparazione alle calamità", "Reti wireless", "Privacy"]
tags: ["meshcore contro meshtastic", "meshtastic", "meshcore", "rete mesh lora", "comunicazioni offline", "confronto meshtastic", "confronto meshcore", "radio lora", "reti mesh", "comunicazioni di emergenza", "mesh tattica", "radio offline", "protocollo meshtastic", "protocollo meshcore", "lora meshtastic", "comunicazioni in caso di calamità", "radio mesh", "memorizzazione e inoltro", "flooding lora", "mesh LoRa", "t-beam meshtastic", "heltec lora", "rak wisblock", "messaggistica offline", "protocollo rete mesh", "meshtastic 2.6", "tempo di trasmissione lora", "radio di emergenza"]
cover: "/img/cover/meshcore-vs-meshtastic-comparison-guide.webp"
coverAlt: "Illustrazione di due reti mesh LoRa: Meshtastic a sinistra con nodi che diffondono i pacchetti e MeshCore a destra con instradamento strutturato, su sfondo scuro."
coverCaption: ""
ref: ["/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide"]
---

## La risposta breve

Meshtastic e MeshCore funzionano sullo stesso hardware LoRa economico. Entrambi permettono di inviare messaggi cifrati senza rete cellulare o Internet. **I due protocolli non sono compatibili.**

**La filosofia di instradamento è diversa.** Meshtastic diffonde i pacchetti a tutti i nodi vicini. MeshCore instrada il traffico tramite un’infrastruttura pianificata. I due approcci producono prestazioni diverse quando la rete cresce.

*Meshtastic è adatto alla maggior parte delle persone.* L’app mobile è curata, la community è ampia, la documentazione è solida e la configurazione richiede meno di 20 minuti. MeshCore è più adatto alle implementazioni pianificate in cui l’efficienza del tempo di trasmissione conta più dell’auto-organizzazione spontanea.

**I principi della radiofrequenza contano più del firmware.** Nessun protocollo rimedia a un’antenna posizionata male.

______

## Cosa fa ogni sistema

### Meshtastic

**Meshtastic** è un progetto open source avviato nel 2020 da Kevin Hester. Il firmware trasforma hardware LoRa comune in una rete mesh di messaggistica testuale senza dipendere da Internet o dalla rete cellulare. Le trasmissioni usano il flooding gestito: ogni nodo ritrasmette i pacchetti fino a un limite di hop configurabile. Dalla versione 2.6, **i messaggi diretti usano l’instradamento al next hop** dopo la scoperta del percorso, invece del flooding. Questo riduce il tempo di trasmissione per il traffico punto-punto.

Il firmware funziona su hardware LoRa che molti utenti possiedono già o acquistano a basso costo. **LILYGO T-Beam, Heltec WiFi LoRa 32, RAK WisBlock e Seeed SenseCAP Indicator** supportano Meshtastic senza strumenti specializzati. Le app iOS e Android sono ben mantenute. Gli utenti non tecnici entrano in rete in meno di dieci minuti. L’ecosistema include bridge MQTT, integrazione Home Assistant e plugin ATAK.

### MeshCore

**MeshCore** ha guadagnato popolarità nel 2023-2024. Il firmware funziona su gran parte dello stesso hardware LoRa, ma usa un’**architettura di instradamento ibrida**. Prima avviene la scoperta dei percorsi. Poi il traffico passa tramite ripetitori verso la destinazione invece di essere diffuso a tutti. Non si tratta di puro store-and-forward nel senso delle reti tolleranti ai ritardi.

I ripetitori gestiscono la maggior parte dell’inoltro. **I room server sono facoltativi.** Memorizzano i messaggi di gruppo, che i client recuperano alla riconnessione. I client usano una radio LoRa companion e si collegano tramite l’infrastruttura quando presente, oppure comunicano direttamente con i nodi vicini se non ci sono ripetitori.

______

## La differenza tecnica principale

### Come funziona l’instradamento di Meshtastic

Le trasmissioni usano il **flooding gestito**. Ogni nodo ritrasmette i pacchetti fino al limite di hop. Nessun nodo deve conoscere la topologia. I nuovi nodi si uniscono senza configurazione e quelli inattivi vengono aggirati automaticamente. Dalla versione 2.6, **i messaggi diretti usano l’instradamento al next hop** dopo la scoperta del percorso, riducendo il tempo di trasmissione punto-punto.

**Il vincolo effettivo è il tempo di trasmissione, non il numero di nodi.** LoRa opera su bande ISM condivise con limiti regionali del duty cycle, in genere pari all’1% in Europa. Una rete con beacon GPS frequenti, telemetria e traffico attivo satura il tempo di trasmissione prima di raggiungere un limite assoluto di nodi. Dieci nodi attivi che inviano telemetria spesso creano più contesa di cinquanta sensori inattivi. Le mesh dense con diverse decine di utenti attivi spesso subiscono maggiore contesa, ma non esiste un limite fisso. La soglia dipende da spreading factor, preset del tempo di trasmissione, intervalli di telemetria, terreno e posizione dei ripetitori.

Meshtastic genera traffico aggiuntivo con gli annunci informativi dei nodi, la telemetria della batteria, i pacchetti GPS e il rilevamento dei vicini. Le versioni recenti del firmware hanno ridotto questo overhead. *Regolare queste impostazioni spesso risolve i problemi di prestazioni prima che serva cambiare protocollo.*

### Come funziona l’instradamento di MeshCore

MeshCore scopre e apprende i percorsi, poi instrada il traffico verso l’infrastruttura invece di ritrasmetterlo a tutti. **I ripetitori inoltrano il traffico tra i nodi.** I room server possono ospitare conversazioni di gruppo e memorizzare i messaggi per i client che si riconnettono in seguito.

L’occupazione del canale dipende dalle conversazioni attive, non dal numero totale di nodi. Una grande installazione con molti nodi inattivi non perde prestazioni come una rete densa basata sul flooding con molto traffico aggiuntivo. MeshCore punta per progetto a installazioni molto più grandi, anche se le prestazioni effettive dipendono dalla qualità dell’implementazione.

Senza ripetitore, i client comunicano direttamente quando sono nel raggio d’azione. *L’architettura dà il meglio con l’infrastruttura. L’infrastruttura non è un requisito assoluto.*

______

## Hardware

Entrambi i protocolli funzionano sulle stesse schede LoRa più diffuse.

| Scheda | Meshtastic | MeshCore |
|---|---|---|
| LILYGO T-Beam (ESP32 + SX1276/SX1262) | Sì | Sì |
| LILYGO T-Echo (nRF52840 + SX1262) | Sì | Sì |
| Heltec WiFi LoRa 32 V3 | Sì | Sì |
| RAK WisBlock 4631 | Sì | Sì |
| Seeed SenseCAP Indicator | Sì | Parziale |
| Station G2 | Sì | Sì |

**Puoi installare uno dei due firmware sullo stesso dispositivo fisico.** Cambiare protocollo non richiede nuovo hardware. Sperimentare costa solo tempo.

______

## Facilità di configurazione

### Configurare Meshtastic

1. Scarica il firmware da meshtastic.org
2. Installa il firmware con il flasher web flasher.meshtastic.org, senza driver
3. Installa l’app Meshtastic sul telefono
4. Abbina il dispositivo tramite Bluetooth
5. Unisciti a un canale o creane uno con nome e password condivisi

**Tempo totale per un nuovo utente: meno di 20 minuti.** La cifratura del canale usa chiavi precondivise AES-256. Il canale pubblico predefinito ti collega subito a qualsiasi nodo Meshtastic nel raggio d’azione. L’app mostra le posizioni GPS su una mappa se i nodi hanno attivato il GPS.

### Configurare MeshCore

1. Installa il firmware sul nodo infrastrutturale, ripetitore o room server, usando PlatformIO o binari precompilati
2. Installa il firmware sulla radio companion del client
3. Installa l’app MeshCore
4. Configura nell’app l’indirizzo e le credenziali dell’infrastruttura
5. Collega la radio companion tramite Bluetooth

**La configurazione richiede più pianificazione.** Prima di implementare la rete, devi capire i ruoli dei nodi. I room server sono facoltativi ma conservano i messaggi per i client offline. *Due amici che vogliono comunicare rapidamente dovrebbero usare Meshtastic. Un team che installa una stazione base con un ripetitore sul tetto dovrebbe usare MeshCore.*

______

## Il tempo di trasmissione è il vero vincolo

Entrambi i protocolli usano LoRa. **La capacità LoRa dipende dal tempo di trasmissione e dal budget del duty cycle, non dal numero di nodi.**

Le variabili che determinano le prestazioni della rete:

- **Spreading factor.** Valori più alti aumentano la portata, ma riducono la velocità e la capacità totale.
- **Preset del tempo di trasmissione.** I preset a lunga portata consumano più duty cycle per messaggio.
- **Intervallo di telemetria.** GPS, batteria e dati ambientali di Meshtastic aggiungono traffico continuo.
- **Frequenza dei messaggi.** Gli utenti attivi che inviano spesso incidono più dei nodi passivi.
- **Posizione dei ripetitori.** Un ripetitore ben posizionato distribuisce il carico. Uno mal posizionato aumenta la congestione.
- **Terreno.** I nodi che non si ricevono aggiungono traffico senza causare contesa. I nodi simultaneamente nel raggio di molti altri creano contesa.

*Meshtastic riduce la pianificazione e accetta parte dell’overhead di trasmissione in cambio dell’auto-organizzazione. MeshCore richiede pianificazione e la ripaga con un uso più prevedibile del tempo di trasmissione. Passare a MeshCore senza migliorare la pianificazione della rete non garantisce prestazioni migliori.*

______

## Normative

I confronti delle prestazioni variano in base alla regione perché le normative sono diverse:

- **915 MHz (USA):** FCC Part 15 non impone un limite fisso al duty cycle, ma si applicano limiti di potenza.
- **868 MHz (UE):** duty cycle dell’1% secondo ETSI, pari a 36 secondi di trasmissione all’ora per canale.
- **433 MHz (UE/Asia):** in molte regioni ci sono limiti più severi, spesso del 10% su alcune sottobande.

**Il limite di duty cycle dell’1% in Europa è un vincolo normativo rigido.** Le mesh dense Meshtastic nell’UE raggiungono i limiti prima delle installazioni equivalenti negli USA. L’uso più efficiente del tempo di trasmissione di MeshCore offre un vantaggio proporzionalmente maggiore nelle regioni con limiti di duty cycle.

______

## Privacy e sicurezza

### Meshtastic

Meshtastic cifra il traffico dei canali privati con **chiavi precondivise AES-256**. Tutti i messaggi di un canale condividono la stessa chiave. Chi possiede la chiave del canale legge tutti i messaggi, incluse le posizioni GPS. **Il canale pubblico predefinito usa una chiave nota distribuita con il firmware**, quindi il traffico pubblico non è riservato a chi esegue Meshtastic nelle vicinanze.

Le posizioni GPS su un canale privato cifrato sono visibili solo ai nodi con la chiave. Sul canale pubblico sono visibili a chiunque. *Questo conta quando il tracciamento ha conseguenze operative.*

Meshtastic 2.6 ha migliorato l’instradamento diretto. Il traffico di gruppo continua a usare la chiave precondivisa del canale. I messaggi diretti offrono più isolamento, ma non sono cifrati end-to-end nel senso del protocollo Signal.

### MeshCore

L’instradamento ibrido di MeshCore significa che **un ascoltatore passivo non può ricostruire l’intera topologia della rete monitorando il traffico**. I dati sono instradati verso un’infrastruttura specifica invece di essere diffusi a tutti. **I messaggi diretti usano la cifratura per contatto**, non una chiave di canale condivisa. Gli altri nodi della stessa infrastruttura non possono decifrare la tua conversazione diretta anche se usano lo stesso ripetitore.

I nodi infrastrutturali inoltrano traffico cifrato. Per i messaggi diretti con cifratura per contatto, il ripetitore inoltra il testo cifrato senza decifrarlo. Per il traffico delle stanze, i room server vedono il contenuto delle stanze che ospitano. *La domanda importante è se controlli il room server.*

MeshCore non offre una cifratura end-to-end rigorosa come il protocollo Signal. **La cifratura per contatto dei messaggi diretti migliora in modo concreto la protezione rispetto alla chiave condivisa del canale.** Per gli usi operativi ad alto rischio, valuta attentamente i dettagli dell’implementazione.

______

## Consumo energetico

Con le impostazioni predefinite, MeshCore genera meno trasmissioni radio aggiuntive di Meshtastic. **Meno trasmissioni migliorano l’autonomia dei nodi client.** La telemetria, i beacon GPS e il flooding gestito di Meshtastic consumano tempo di trasmissione. Puoi ridurre molto l’overhead regolando gli intervalli di telemetria e disattivando la trasmissione GPS sui nodi senza GPS. A parità di impostazioni predefinite, **MeshCore trasmette meno**.

Una rete Meshtastic ben regolata con telemetria minima ha un’autonomia vicina a MeshCore. Le impostazioni predefinite favoriscono MeshCore.

______

## Resilienza della rete

**Il flooding gestito di Meshtastic è resiliente.** La perdita di un nodo relay spesso ha poco impatto operativo, perché gli altri nodi reindirizzano il traffico in modo naturale. Non serve conoscere in anticipo i nodi disponibili. La rete si ripristina da sola.

**MeshCore dipende maggiormente dalla posizione dei ripetitori.** Una rete MeshCore ben progettata con buona copertura dei ripetitori offre prestazioni prevedibili. Se si perde l’unico ripetitore in un’area, i nodi che dipendono da esso perdono la connettività. *MeshCore premia la pianificazione iniziale. Meshtastic tollera meglio i guasti dei nodi.*

Meshtastic accetta overhead di trasmissione in cambio della resilienza. MeshCore accetta la dipendenza dall’infrastruttura in cambio dell’efficienza.

______

## GPS e tracciamento della posizione

**L’ecosistema GPS di Meshtastic è più sviluppato.** L’app mobile include una mappa. I nodi della community alimentano mappe pubbliche come meshmap.net tramite gateway MQTT. La telemetria GPS è una funzione centrale. La condivisione della posizione per gruppi escursionistici, ricerca e soccorso ed eventi è ben sviluppata.

MeshCore non è orientato al tracciamento della posizione. *Se la consapevolezza GPS è un requisito primario, nel 2026 l’ecosistema di Meshtastic è più sviluppato e maturo.*

______

## Ecosistema e community

Meshtastic ha una **community più ampia**:

- Discord attivo con migliaia di membri
- Subreddit attivo su r/meshtastic
- Documentazione estesa su meshtastic.org
- Integrazioni di terze parti con MQTT, Home Assistant, Node-RED, ATAK e librerie Python
- Aggiornamenti firmware regolari
- Ampia raccolta di guide hardware create dalla community

MeshCore cresce, ma resta più piccolo. *Ci sono meno discussioni nei forum, tutorial e integrazioni di terze parti. Quando qualcosa si rompe, cercherai risposte nel codice sorgente del firmware o nel Discord del progetto invece di trovare soluzioni già pubblicate.*

Entrambi i progetti sono open source, ma hanno licenze diverse. **Meshtastic usa una licenza di tipo BSD. MeshCore usa GPL.** Alcune organizzazioni ne tengono conto per l’implementazione e la distribuzione.

______

## Quando scegliere Meshtastic

**Piccoli gruppi informali.** Un club di escursionismo che vuole messaggistica offline e condivisione della posizione dovrebbe scegliere Meshtastic. La configurazione è facile, la mappa funziona bene e la rete si organizza da sola.

**Installazioni mobili.** Meshtastic funziona bene con utenti che attraversano il territorio e si uniscono o escono dalla rete in modo imprevedibile. Il flooding auto-organizzato non richiede infrastruttura pianificata per i nodi mobili.

**Installazioni rivolte al pubblico.** Le persone senza competenze tecniche possono configurare i dispositivi senza aiuto. L’avvio con Meshtastic è accessibile.

**Installazione rapida per un evento.** Comunicazioni di un festival, coordinamento di una gara o soccorso installati oggi e smontati la settimana successiva. La configurazione rapida e l’assenza di dipendenze infrastrutturali rendono Meshtastic pratico.

**Tracciamento GPS.** Nel 2026 Meshtastic è la scelta giusta se la posizione è il caso d’uso principale.

______

## Quando scegliere MeshCore

**Installazioni con infrastruttura pianificata.** Hai un ripetitore sul tetto o un room server con alimentazione affidabile. L’instradamento ibrido di MeshCore sfrutta l’infrastruttura fissa.

**Grandi reti con infrastruttura dedicata.** L’efficienza del tempo di trasmissione e le prestazioni prevedibili su larga scala contano più dell’auto-organizzazione spontanea.

**Persistenza dei messaggi con connettività intermittente.** I room server archiviano i messaggi e li consegnano quando i client si riconnettono. **È uno dei vantaggi pratici più concreti di MeshCore rispetto a Meshtastic.**

**Separazione tra nodi fissi e mobili.** Alcuni nodi devono fornire infrastruttura, altri agire da client. Il modello dei ruoli di MeshCore è stato progettato per questa distinzione.

**Regioni con limiti di duty cycle.** Le installazioni europee soggette al limite ETSI dell’1% ottengono più vantaggio dall’uso efficiente del tempo di trasmissione di MeshCore.

**Cifratura per contatto.** Per cifrare i messaggi diretti, il modello di MeshCore è decisamente migliore dell’approccio di Meshtastic basato sulla chiave del canale.

______

## Quando i sistemi cedono

### Punti deboli di Meshtastic

- **Contesa del tempo di trasmissione su larga scala.** Mesh dense con impostazioni predefinite molto attive, frequenti trasmissioni GPS e canali attivi peggiorano. Correggi la configurazione prima di cambiare protocollo.
- **Nessuna persistenza dei messaggi senza infrastruttura.** Senza gateway MQTT, i messaggi persi restano persi.
- **Privacy della posizione sul canale pubblico.** Chiunque ascolti vede tutte le posizioni GPS trasmesse. Va bene per usi casuali, non per requisiti di sicurezza operativa.
- Le versioni firmware principali a volte introducono problemi di compatibilità finché la rete non passa a una versione coerente.

### Punti deboli di MeshCore

- **Configurazione complessa.** Prima di un’installazione significativa devi capire i ruoli dell’infrastruttura.
- **Community più piccola.** Documentazione, tutorial e integrazioni di terze parti di Meshtastic sono più sviluppati.
- **Meno varietà hardware.** MeshCore supporta una gamma più ridotta di dispositivi.
- **App mobile meno mature.** Sono funzionali, ma meno curate delle app Meshtastic per iOS e Android.
- **Dipendenza dall’infrastruttura per prestazioni ottimali.** Senza ripetitori, i client comunicano direttamente ma l’efficienza dell’instradamento scompare. Se il gruppo non si impegna a mantenere un’infrastruttura fissa, il vantaggio architetturale non si concretizza.
- **Ripristino della rete.** La perdita di un ripetitore in un’area interrompe la connettività dei nodi dipendenti. Il flooding di Meshtastic tollera meglio i guasti.
- **Nessuna interoperabilità tra protocolli.** MeshCore e Meshtastic non si scambiano messaggi. Lo stesso hardware può eseguire uno dei due firmware, ma usare entrambi significa gestire due reti separate.

______

## La radiofrequenza conta più del firmware

**Qualità e altezza dell’antenna, perdite della linea di alimentazione, terreno e impostazioni radio influiscono sulle prestazioni più della scelta del firmware.**

Un nodo Meshtastic ben posizionato in cima a una collina con una buona antenna supera un ripetitore MeshCore mal posizionato in un contenitore metallico in cantina. Il confronto presuppone una qualità di installazione fisica simile.

Prima di cambiare protocollo per risolvere un problema di prestazioni, verifica che:

- I collegamenti dell’antenna siano puliti e a bassa perdita.
- I nodi siano più in alto possibile.
- Il preset del tempo di trasmissione corrisponda alla portata desiderata.
- **Gli intervalli di telemetria non saturino il canale.**
- Lo spreading factor sia adatto alla densità dei nodi.

______

## Riepilogo a confronto

| Fattore | Meshtastic | MeshCore |
|---|---|---|
| Modello di rete | Flooding gestito e instradamento al next hop per i messaggi diretti | Scoperta ibrida dei percorsi e inoltro diretto |
| Difficoltà di configurazione | Facile | Da media a difficile |
| Progettazione per la scala | Flessibile, peggiora con la contesa | Progettato per reti pianificate più grandi |
| Qualità app mobile | Eccellente | Funzionale |
| Dimensioni della community | Molto ampia | In crescita |
| GPS e tracciamento | Ecosistema sviluppato | Poca attenzione |
| Persistenza dei messaggi | No, serve un gateway MQTT | Sì, tramite room server facoltativi |
| Cifratura messaggi diretti | PSK del canale | Cifratura per contatto |
| Necessità di infrastruttura | Non richiesta | Ottimizzato per nodi infrastrutturali |
| Ripristino della rete | Resiliente, si ripara da sola | Dipende dai ripetitori |
| Supporto hardware | Ampio | Sottoinsieme mirato |
| Ideale per | Gruppi mobili, ad hoc e piccoli | Installazioni pianificate con infrastruttura fissa |

______

## Quale scegliere

**Inizia con Meshtastic.** Sarai operativo nel giro di un pomeriggio. Troverai persone con cui fare test. L’app funziona e la documentazione è eccellente. L’instradamento al next hop di Meshtastic 2.6 riduce il divario di efficienza per il traffico diretto punto-punto.

**Passa a MeshCore se le impostazioni predefinite di Meshtastic non sono adatte alla tua installazione.** Se hai ripetitori dedicati, hai bisogno di conservare messaggi per utenti intermittenti oppure costruisci una grande rete pianificata dove l’efficienza di trasmissione conta più dell’auto-organizzazione, l’architettura MeshCore è adatta e giustifica l’impegno di configurazione.

Prima di cambiare protocollo, **regola la tua rete Meshtastic**. Riduci gli intervalli di telemetria. Disattiva la trasmissione GPS sui nodi senza GPS. Adatta il preset del tempo di trasmissione alla densità dei nodi. *Molte reti con problemi di prestazioni hanno problemi di configurazione, non di protocollo.*

I protocolli rispondono a esigenze diverse nel compromesso tra pianificazione e spontaneità. Meshtastic riduce la pianificazione e accetta l’overhead dell’auto-organizzazione. MeshCore richiede pianificazione e la premia con prestazioni più prevedibili. **Nessuno dei due sostituirà l’altro, perché gli usi sono diversi.**

*Stai costruendo una rete che deve collegare LoRa a packet radio, Wi-Fi o Internet invece di restare su una singola rete mesh LoRa?* Consulta la **[guida comparativa Meshtastic, MeshCore e Reticulum](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/)** per capire dove si adatta una rete indipendente dal trasporto e dove aggiunge complessità inutile.
