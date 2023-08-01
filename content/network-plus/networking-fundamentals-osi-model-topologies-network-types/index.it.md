---
title: "Corso Network Plus: Capire il modello OSI, le topologie e i tipi di rete"
date: 2023-07-01
toc: true
draft: false
description: "Esplorare l'importanza dei fondamenti di rete, tra cui il modello OSI, le topologie di rete e i vari tipi di rete, per costruire infrastrutture efficienti e affidabili."
genre: ["Tecnologia", "Collegamento in rete", "Infrastruttura IT", "Architettura di rete", "Informatica", "Comunicazione dati", "Tecnologia dell'informazione", "Sicurezza di rete", "Gestione della rete", "Internet"]
tags: ["fondamenti di rete", "OSI model", "topologie di rete", "Tipi di rete", "incapsulamento dei dati", "Livelli di rete", "topologia di rete", "topologia a stella", "topologia bus", "topologia ad anello", "topologia ibrida", "rete peer-to-peer", "rete client-server", "LAN", "UOMO", "WAN", "WLAN", "PAN", "CAN", "SAN", "SDWAN", "MPLS", "mGRE", "vSwitch", "vNIC", "NFV", "hypervisor", "satellite link", "DSL", "Internet via cavo", "linea affittata", "metro-ottico"]
cover: "/img/cover/A_symbolic_illustration_of_interconnected_nodes.png"
coverAlt: "Illustrazione simbolica dei nodi interconnessi che formano una rete."
coverCaption: "Liberare la potenza dei fondamenti di rete."
---

#### [Click Here to Return To the Network Plus Course Page](/network-plus-start)

I fondamenti della rete svolgono un ruolo cruciale nel mondo interconnesso di oggi. Che si tratti di navigare in Internet, inviare e-mail o trasmettere video in streaming, tutte queste attività si basano su una solida infrastruttura di rete. In questo articolo forniremo una panoramica dei **fondamenti di rete**, a partire dal **modelloOSI** e dai concetti di **incapsulamento**. Esploreremo inoltre le diverse **topologie di rete** e le loro caratteristiche.

## Panoramica del modello OSI e dei concetti di incapsulamento

Il **modello OSI (Open Systems Interconnection)** è un quadro concettuale che definisce le funzioni di una rete in sette diversi livelli. Ogni livello ha responsabilità specifiche e interagisce con i livelli superiori e inferiori. La comprensione del modello OSI è essenziale per capire come i dati vengono trasmessi ed elaborati attraverso una rete.

### Livelli del modello OSI

{{< youtube id="G7aVKgGUe9c" >}}

1. **Livello 1 - Fisico**: Il livello fisico si occupa dell'effettiva trasmissione e ricezione di flussi di bit grezzi su supporti fisici come fili di rame, cavi in fibra ottica o connessioni wireless.

2. 2. **Livello 2 - Collegamento dati**: Il livello di collegamento dati è responsabile della creazione e della terminazione delle connessioni tra i dispositivi di rete. Gestisce inoltre il rilevamento e la correzione degli errori per garantire una trasmissione affidabile dei dati.

3. **Livello 3 - Rete**: Il livello di rete facilita l'instradamento dei pacchetti di dati dalla sorgente alla destinazione attraverso più nodi di rete. Si occupa di problemi legati alla **congestione della rete**, all'instradamento dei pacchetti** e all'**indirizzamento IP**.

4. **Livello 4 - Trasporto**: Il livello di trasporto assicura la **consegna dei dati da un capo all'altro** e stabilisce una comunicazione affidabile tra la sorgente e la destinazione. Gestisce la **segmentazione dei dati**, il **controllo del flusso** e il **recupero degli errori**.

5. 5. **Livello 5 - Sessione**: Il livello di sessione imposta, mantiene e termina le sessioni di comunicazione tra le applicazioni. Gestisce il **controllo del dialogo** e la **sincronizzazione** tra i dispositivi.

6. 6. **Livello 6 - Presentazione**: Il livello di presentazione si concentra sulla **tassi** e sulla **semantica** delle informazioni scambiate tra le applicazioni. Gestisce la **crittografia** dei dati, la **compressione** e la **formattazione** per una corretta interpretazione.

7. **Livello 7 - Applicazione**: Il livello applicativo rappresenta le applicazioni e i servizi di rete utilizzati dagli utenti finali. Fornisce servizi quali **email**, **trasferimento di file**, **navigazione web** e **accesso remoto**.

{{< inarticle-dark >}}

### Incapsulamento e decapsulamento dei dati nel contesto del modello OSI

{{< youtube id="_fPzeQ9PHhA" >}}

L'incapsulamento dei dati è il processo di aggiunta di intestazioni e trailer specifici del protocollo al carico utile a ogni livello del modello OSI. Questo incapsulamento consente ai dati di attraversare la rete e raggiungere la destinazione prevista. Al contrario, la decapsulazione consiste nel rimuovere le intestazioni e i trailer aggiunti a ogni livello del modello OSI per estrarre il carico utile originale.

Nel contesto del modello OSI, i seguenti elementi contribuiscono all'incapsulamento e al decapsulamento dei dati:

- **Intestazione Ethernet**: L'intestazione Ethernet contiene informazioni quali gli indirizzi MAC dei dispositivi di origine e di destinazione, il tipo di protocollo Ethernet e i meccanismi di controllo degli errori.

- **Internet Protocol (IP) Header**: L'intestazione IP comprende gli indirizzi IP di origine e di destinazione, l'identificazione del pacchetto, il time-to-live e altri parametri essenziali per la comunicazione basata su IP.

- **Intestazioni TCP (Transmission Control Protocol)/User Datagram Protocol (UDP)**: Le intestazioni TCP e UDP contengono numeri di porta, numeri di sequenza, checksum e altre informazioni importanti necessarie per la comunicazione a livello di trasporto.

- **Bandiere TCP**: I flag TCP indicano funzioni e opzioni di controllo specifiche durante una sessione TCP. Comprendono flag per stabilire connessioni, riconoscere i dati, terminare le connessioni e altro ancora.

- **Carico utile**: Il payload è il dato effettivo che viene trasmesso, come una pagina web, un messaggio di posta elettronica o un file multimediale.

- **Unità massima di trasmissione (MTU)**: L'MTU rappresenta la dimensione massima di un pacchetto di dati che può essere trasmesso su una rete senza frammentazione.

{{< inarticle-dark >}}

## Esplorazione delle topologie di rete e delle loro caratteristiche

{{< youtube id="zbqrNg4C98U" >}}

Le topologie di rete definiscono la disposizione fisica o logica dei dispositivi di rete e le interconnessioni tra di essi. Ogni topologia ha i suoi punti di forza e di debolezza e la scelta della topologia giusta dipende da vari fattori come la scalabilità, la tolleranza ai guasti e il costo.

Topologia a maglie ###

In una topologia **mesh**, ogni dispositivo è collegato a ogni altro dispositivo, formando una rete completamente interconnessa. Questa ridondanza offre un'elevata tolleranza agli errori, ma può essere costosa e complessa da implementare. Le topologie mesh sono comunemente utilizzate nelle infrastrutture critiche e negli ambienti di calcolo ad alte prestazioni.

### Topologia Star/Hub-and-Spoke

In una topologia **stellare**, tutti i dispositivi sono collegati a un hub o switch centrale. L'hub funge da punto di connessione centrale, facilitando la comunicazione tra i dispositivi. Questa topologia è facile da gestire e fornisce un controllo centralizzato, ma può creare un singolo punto di guasto se l'hub si guasta.

Topologia a bus ###

In una topologia **bus**, tutti i dispositivi sono collegati a un'unica linea di comunicazione, chiamata bus. I dati vengono trasmessi in sequenza lungo il bus e i dispositivi ricevono i dati a loro destinati. Le topologie a bus sono semplici e convenienti, ma possono presentare congestioni di rete e hanno una scalabilità limitata.

### Topologia ad anello

In una **topologia ad anello**, i dispositivi sono collegati in una catena circolare, con ogni dispositivo che si collega al successivo e l'ultimo che si collega al primo. I dati circolano in un'unica direzione attorno all'anello. Le topologie ad anello offrono un accesso equo e possono gestire carichi di traffico elevati, ma possono subire interruzioni della rete in caso di guasto di un dispositivo.

### Topologia ibrida

Una **topologia ibrida** combina più topologie per formare una rete più flessibile e scalabile. Ad esempio, una combinazione di topologie a stella e ad anello può fornire ridondanza e tolleranza ai guasti mantenendo la scalabilità.

## Tipi di rete e caratteristiche

{{< youtube id="6a-roIeJ_a4" >}}

Le reti comprendono vari tipi di reti, ognuna delle quali risponde a esigenze e casi d'uso specifici. Ecco alcuni tipi di rete comuni:

### Rete Peer-to-Peer (P2P)

In una rete **peer-to-peer (P2P)**, i dispositivi si connettono direttamente tra loro senza affidarsi a un server centralizzato. Le reti P2P sono spesso utilizzate per la condivisione di file, applicazioni collaborative e sistemi decentralizzati.

### Rete client-server

Una rete **client-server** coinvolge i client, che richiedono servizi o risorse, e i server, che forniscono tali servizi o risorse. Le reti client-server sono ampiamente utilizzate negli ambienti aziendali, dove il controllo centralizzato e la gestione delle risorse sono essenziali.

### Rete locale (LAN)

Una **rete locale (LAN)** si estende su una piccola area geografica, come un edificio o una casa. Consente ai dispositivi all'interno della rete di comunicare e condividere le risorse. Le LAN sono comunemente utilizzate per la comunicazione interna, la condivisione di file e stampanti.

### Rete di area metropolitana (MAN)

Una **rete metropolitana (MAN)** copre un'area geografica più ampia di una LAN ma più piccola di una WAN. Collega più LAN all'interno di una città o di una regione metropolitana. Le MAN sono spesso utilizzate dalle organizzazioni che necessitano di connettività ad alta velocità tra le loro filiali o campus.

### Rete geografica (WAN)

Una **rete di area vasta (WAN)** si estende su un'ampia area geografica, collegando più LAN o MAN in città, paesi o continenti diversi. Le WAN si basano su varie tecnologie di comunicazione, come linee affittate, satelliti e reti ottiche, per trasmettere dati su lunghe distanze.

### Rete locale senza fili (WLAN)

Una **rete locale wireless (WLAN)** fornisce connettività wireless in un'area limitata, in genere utilizzando la tecnologia Wi-Fi. Le WLAN si trovano comunemente nelle case, negli uffici, nelle caffetterie e negli spazi pubblici e consentono agli utenti di collegare i propri dispositivi senza cavi fisici.

### Rete personale (PAN)

Una **rete personale (PAN)** copre una piccola area, in genere all'interno dello spazio di lavoro di una persona o nelle sue immediate vicinanze. Consente la comunicazione tra dispositivi personali, come smartphone, tablet e dispositivi indossabili.

### Rete area campus (CAN)

Una **rete di area campus (CAN)** è una rete che si estende su un campus universitario o su un grande campus aziendale. Fornisce connettività a vari edifici e strutture all'interno dell'area del campus, facilitando la comunicazione e la condivisione delle risorse.

### Rete di area di archiviazione (SAN)

Una **rete di archiviazione (SAN)** è una rete specializzata progettata per scopi di archiviazione. Consente a più server di accedere a risorse di archiviazione condivise, come array di dischi o librerie di nastri, tramite una connessione ad alta velocità.

### Software-Defined Wide Area Network (SDWAN)

La **Software-Defined Wide Area Network (SDWAN)** è una tecnologia che semplifica la gestione e la configurazione delle WAN separando il piano di controllo della rete dall'hardware sottostante. Fornisce un controllo centralizzato e consente alle organizzazioni di gestire dinamicamente la propria infrastruttura WAN.

### Commutazione di etichette multiprotocollo (MPLS)

**Il Multiprotocol Label Switching (MPLS)** è una tecnica di routing che utilizza le etichette per inoltrare in modo efficiente i pacchetti di dati attraverso una rete. Fornisce comunicazioni ad alte prestazioni, affidabili e sicure, rendendole adatte ai service provider e alle aziende.

### Multipoint Generic Routing Encapsulation (mGRE)

Il **Multipoint Generic Routing Encapsulation (mGRE)** è una tecnica utilizzata per creare reti private virtuali (VPN) incapsulando i pacchetti di dati e inviandoli su una rete multipunto. Consente una comunicazione efficiente tra più siti o endpoint.

{{< inarticle-dark >}}

## Concetti di rete virtuale

{{< youtube id="A29g5-Os-u8" >}}

Le tecnologie di virtualizzazione hanno rivoluzionato il modo di progettare e gestire le reti. Ecco alcuni concetti di rete virtuale:

### vSwitch

Un **vSwitch**, o switch virtuale, è uno switch di rete basato su software che opera in un ambiente virtualizzato, come un hypervisor. Consente la comunicazione tra le macchine virtuali (VM) e le collega alla rete fisica.

### Scheda di interfaccia di rete virtuale (vNIC)

Una **scheda di interfaccia di rete virtuale (vNIC)** è una scheda di interfaccia di rete virtualizzata che emula una scheda di rete fisica all'interno di una macchina virtuale. Consente alle macchine virtuali di comunicare con lo switch virtuale e la rete fisica.

### Virtualizzazione delle funzioni di rete (NFV)

La **Virtualizzazione delle funzioni di rete (NFV)** è un approccio che virtualizza le funzioni di rete, come firewall, router e bilanciatori di carico, eseguendole su server standard invece che su dispositivi hardware dedicati. Offre flessibilità, scalabilità e riduzione dei costi dell'infrastruttura di rete.

### Ipervisore

Un **hypervisor** è un livello software che consente la creazione e la gestione di macchine virtuali. Fornisce l'astrazione dell'hardware, consentendo l'esecuzione di più macchine virtuali su un singolo server fisico.

## Link al provider

{{< youtube id="M2cJtZXJrpE" >}}

I link dei provider si riferiscono ai vari tipi di opzioni di connettività offerte dai provider. Ecco alcuni link di provider comuni:

### Satellite

I collegamenti **satellitari** utilizzano i satelliti di comunicazione per trasmettere dati su lunghe distanze. Sono spesso utilizzati in aree remote dove le altre opzioni di connettività sono limitate.

### Linea di abbonamento digitale (DSL)

La **Digital Subscriber Line (DSL)** è una tecnologia che fornisce accesso a Internet ad alta velocità attraverso le linee telefoniche esistenti. Offre velocità maggiori rispetto alle tradizionali connessioni dial-up ed è ampiamente disponibile in ambienti residenziali e aziendali.

### Cavo

**Internet via cavo** utilizza gli stessi cavi coassiali usati per la televisione via cavo per fornire accesso a Internet ad alta velocità. È molto diffuso nelle aree residenziali e offre velocità maggiori rispetto alla DSL.

### Linea affittata

Una **linea affittata** è una connessione dedicata punto-punto tra due sedi. Fornisce una connettività affidabile e sicura, che la rende adatta alle aziende con requisiti di larghezza di banda elevati.

### Metro-ottica

Le reti **metro-ottiche** utilizzano la tecnologia della fibra ottica per fornire connettività ad alta velocità all'interno di un'area metropolitana. Offrono un'elevata larghezza di banda e una bassa latenza, ideali per le applicazioni ad alta intensità di dati.

______

In conclusione, la comprensione dei fondamenti del networking è fondamentale per costruire e mantenere infrastrutture di rete affidabili ed efficienti. Il **modelloOSI** fornisce un quadro di riferimento per comprendere come i dati vengono trasmessi ed elaborati attraverso i diversi livelli di rete. Inoltre, la conoscenza delle **topologie di rete** aiuta a progettare reti che soddisfano requisiti specifici di scalabilità, tolleranza ai guasti ed efficienza dei costi. Familiarizzando con i vari **tipi di rete**, con i **concetti di rete virtuale** e con i **collegamenti di provider**, possiamo prendere decisioni informate quando impostiamo e gestiamo le reti.

Riferimenti:
- [OSI Model - Cisco](https://learningnetwork.cisco.com/s/article/osi-model-reference-chart)
- [How Does the Internet Work? - Stanford University](https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm)
