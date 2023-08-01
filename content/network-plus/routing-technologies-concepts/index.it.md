---
title: "Corso Network Plus: Protocolli di Routing, Concetti e Ottimizzazione"
date: 2023-07-07
toc: true
draft: false
description: "Esplorate il mondo delle tecnologie e dei concetti di routing, dai protocolli di routing dinamico come RIP, OSPF, EIGRP e BGP ai protocolli di routing a stato di collegamento, a vettore di distanza e ibridi, nonché la configurazione del routing statico e delle rotte predefinite."
genre: ["Tecnologia", "Collegamento in rete", "Instradamento", "Protocolli di rete", "Gestione della rete", "Instradamento dinamico", "Instradamento statico", "Gestione della larghezza di banda", "Qualità del servizio", "Dispositivi di rete"]
tags: ["tecnologie di routing", "protocolli di routing dinamico", "RIP", "OSPF", "EIGRP", "BGP", "stato del collegamento", "vettore distanza", "protocolli di routing ibridi", "instradamento statico", "percorsi predefiniti", "distanza amministrativa", "percorso esterno", "instradamento interno", "tempo di vivere", "Gestione della larghezza di banda", "Modellamento del traffico", "qualità del servizio", "dispositivi di rete", "router", "interruttori", "firewall", "bilanciatori di carico", "punti di accesso", "ottimizzazione della rete", "prestazioni della rete", "sicurezza della rete", "architettura di rete", "traffico di rete"]
cover: "/img/cover/An_illustration_of_interconnected_network_devi.png"
coverAlt: "Un'illustrazione di dispositivi di rete interconnessi con dati che scorrono tra loro."
coverCaption: "Navigare sull'autostrada digitale: Ottimizzare l'instradamento della rete per ottenere le massime prestazioni"
---

#### [Click Here to Return To the Network Plus Course Page](/network-plus-start)

## Introduzione

Nel mondo interconnesso di oggi, un instradamento di rete efficiente è essenziale per una trasmissione e una comunicazione fluida dei dati. Le tecnologie e i concetti di instradamento svolgono un ruolo cruciale nell'indirizzare il traffico di rete e nell'ottimizzare le prestazioni della rete. Questo articolo esplora vari protocolli di routing, come RIP, OSPF, EIGRP e BGP, oltre a protocolli di routing a stato di collegamento, a vettore di distanza e ibridi. Approfondiremo anche la configurazione e l'uso del routing statico e delle rotte predefinite. Inoltre, confronteremo e contrapporremo i diversi dispositivi e il loro posizionamento sulla rete.

{{< youtube id="YRzr56cwgCg" >}}

## Protocolli di routing dinamico

I protocolli di routing dinamico sono progettati per automatizzare il processo di scambio di informazioni di routing tra i router. Si adattano ai cambiamenti della rete, come le modifiche alla topologia o i guasti ai collegamenti, aggiornando dinamicamente le tabelle di routing. Vediamo nel dettaglio alcuni protocolli di routing dinamico comunemente utilizzati:

### Protocollo di instradamento Internet (RIP)

Il Routing Internet Protocol (RIP) è un protocollo di routing distance vector che opera in base al numero di hop tra i router. Utilizza la metrica del numero di hop per determinare il percorso migliore verso una rete di destinazione. RIP supporta sia IPv4 che IPv6 ed è adatto a reti di piccole e medie dimensioni.

### Open Shortest Path First (OSPF)

Open Shortest Path First (OSPF) è un protocollo di routing a stato di collegamento che calcola il percorso più breve verso una destinazione utilizzando l'algoritmo di Dijkstra. Prende in considerazione varie metriche, come la larghezza di banda, il ritardo e l'affidabilità, per determinare il percorso ottimale. OSPF è ampiamente utilizzato nelle grandi reti aziendali grazie alla sua scalabilità e alla rapida convergenza.

### Enhanced Interior Gateway Routing Protocol (EIGRP)

Enhanced Interior Gateway Routing Protocol (EIGRP) è un protocollo di routing ibrido sviluppato da Cisco. Combina le migliori caratteristiche dei protocolli distance vector e link state. EIGRP utilizza l'algoritmo di aggiornamento diffuso (Diffusing Update Algorithm, DUAL) per calcolare le rotte e offre funzionalità avanzate come il bilanciamento del carico a costo disuguale e la riepilogo delle rotte.

### Protocollo gateway di confine (BGP)

Il Border Gateway Protocol (BGP) è un protocollo di gateway esterno utilizzato per l'instradamento tra sistemi autonomi (AS) in Internet. BGP è altamente scalabile e consente ai sistemi autonomi di scambiare informazioni di routing. Utilizza gli attributi e le politiche di percorso per prendere decisioni di instradamento basate su fattori quali le politiche di rete, la lunghezza del percorso e il percorso AS.

## Protocolli di instradamento a stato di collegamento, a vettore di distanza e ibridi

I protocolli di routing possono essere classificati in link state, distance vector e ibridi in base al loro funzionamento e alle informazioni che utilizzano per determinare i percorsi.

### Protocolli di instradamento allo stato di collegamento

I protocolli di routing allo stato di collegamento, come OSPF, mantengono una mappa dettagliata dell'intera rete scambiando informazioni sullo stato di collegamento tra i router. Ogni router costruisce un database topologico che gli consente di calcolare il percorso migliore verso una rete di destinazione in base a varie metriche.

### Protocolli di instradamento a vettore di distanza

I protocolli di instradamento a vettore di distanza, come il RIP, utilizzano una metrica semplice (come il conteggio degli hop) e scambiano informazioni di instradamento con i router vicini. I router pubblicizzano periodicamente le loro tabelle di routing ai router vicini, consentendo loro di costruire un quadro della rete. I protocolli vettoriali a distanza hanno una conoscenza limitata della rete complessiva e possono essere soggetti a loop di instradamento.

### Protocolli di instradamento ibridi

I protocolli di routing ibridi, come EIGRP, combinano le caratteristiche di entrambi i protocolli link state e distance vector. Mantengono una tabella topologica simile a quella dei protocolli a stato di collegamento, ma utilizzano algoritmi vettoriali a distanza per calcolare le rotte. I protocolli ibridi offrono i vantaggi di una convergenza più rapida e di un overhead ridotto.

{{< inarticle-dark >}}

## Routing statico e rotte predefinite

Il routing statico prevede la configurazione manuale della tabella di routing sui router, specificando i percorsi per raggiungere reti specifiche. È tipicamente utilizzato in scenari in cui i cambiamenti della topologia di rete sono minimi o prevedibili. Le rotte statiche sono facili da configurare e possono essere utili per piccole reti o segmenti di rete specifici.

Un percorso predefinito, noto anche come gateway di ultima istanza, viene utilizzato quando non esiste un percorso esplicito per una rete di destinazione. Funziona come una rotta di recupero e viene configurata sui router per indirizzare il traffico verso un gateway predefinito quando il router non è a conoscenza della rete di destinazione.

## Distanza amministrativa, esterno vs interno e tempo di vita

{{< youtube id="HR59xk4umWY" >}}

### Distanza amministrativa

La distanza amministrativa (AD) è un valore assegnato ai protocolli di routing per determinare la priorità dei percorsi quando più protocolli sono in esecuzione su un router. Valori più bassi di distanza amministrativa indicano una maggiore priorità per un particolare protocollo di routing. Ad esempio, OSPF ha una AD più bassa (110) rispetto a RIP (120), quindi le rotte OSPF saranno preferite a quelle RIP.

### Routing esterno e interno

I protocolli di routing esterni, come BGP, sono utilizzati per scambiare informazioni di routing tra sistemi autonomi (AS). Gestiscono il routing tra diverse organizzazioni e fornitori di servizi. I protocolli di routing interno, invece, come RIP, OSPF ed EIGRP, sono utilizzati per il routing all'interno di un sistema autonomo.

### Tempo di vita (TTL)

Il Time to Live (TTL) è un campo dei pacchetti IP che specifica il numero massimo di hop che un pacchetto può percorrere prima di essere scartato. Impedisce ai pacchetti di circolare indefinitamente nella rete in caso di loop di routing o altri problemi. Ogni router decrementa il valore TTL man mano che il pacchetto attraversa la rete.

## Gestione della larghezza di banda

Una gestione efficiente della larghezza di banda è fondamentale per ottimizzare le prestazioni della rete e garantire un flusso regolare del traffico. Due aspetti importanti della gestione della larghezza di banda sono il traffic shaping e la qualità del servizio (QoS).

### Modellamento del traffico

Il traffic shaping è una tecnica utilizzata per controllare la velocità di trasmissione dei dati su una rete. Consente agli amministratori di rete di modellare il flusso di traffico definendo limiti di larghezza di banda e dando priorità a determinati tipi di traffico. In questo modo si previene la congestione della rete e si garantisce che le applicazioni critiche ricevano una larghezza di banda sufficiente.

### Qualità del servizio (QoS)

La qualità del servizio (QoS) si riferisce alla capacità di una rete di assegnare priorità e risorse a diversi tipi di traffico in base alla loro importanza e ai loro requisiti. I meccanismi QoS, come la prioritizzazione del traffico, l'allocazione della larghezza di banda e la gestione della congestione, contribuiscono a garantire prestazioni ottimali per le applicazioni in tempo reale come voce e video.

{{< inarticle-dark >}}

## Confronto e posizionamento dei dispositivi

I diversi dispositivi svolgono ruoli specifici in una rete e hanno caratteristiche diverse che li rendono adatti a compiti particolari. Confrontiamo e contrapponiamo alcuni dispositivi di rete comuni e discutiamo la loro collocazione appropriata:

- **Router**: I router sono responsabili dell'indirizzamento del traffico tra reti diverse. Operano a livello di rete (Layer 3) e utilizzano protocolli di routing per determinare il percorso migliore per la trasmissione dei dati.

- Switch**: Gli switch operano a livello di collegamento dati (Layer 2) e facilitano la comunicazione tra i dispositivi di una rete locale (LAN). Utilizzano gli indirizzi MAC per inoltrare i pacchetti di dati al destinatario previsto.

- **Firewall**: I firewall proteggono le reti da accessi non autorizzati e traffico dannoso. Applicano i criteri di sicurezza ispezionando il traffico di rete e consentendo o bloccando connessioni specifiche in base a regole predefinite.

- Bilanciatori di carico**: I bilanciatori di carico distribuiscono il traffico di rete in entrata su più server per ottimizzare l'utilizzo delle risorse, migliorare le prestazioni e garantire un'elevata disponibilità.

- Punti di accesso**: I punti di accesso (AP) forniscono connettività wireless ai dispositivi di una rete. Consentono la comunicazione wireless trasmettendo e ricevendo dati tra i dispositivi wireless e la rete cablata.

La collocazione di questi dispositivi dipende dall'architettura e dai requisiti della rete. I **Router** sono generalmente collocati sul perimetro della rete per gestire il traffico tra le reti. Gli **interruttori** sono distribuiti all'interno delle LAN per collegare i dispositivi e facilitare la comunicazione locale. I **Firewall** sono posizionati tra le reti per proteggere dalle minacce esterne. I **bilanciatori di carico** sono posizionati davanti ai server web per distribuire il traffico in modo efficiente. Gli **Access Point** sono posizionati strategicamente per fornire una copertura wireless nelle aree desiderate.

______

## Conclusione

La comprensione delle **tecnologie e dei concetti di routing** è fondamentale per gli amministratori di rete e i professionisti IT. I **protocolli di routing dinamico** come **RIP, OSPF, EIGRP e BGP** automatizzano il processo di scambio di informazioni di routing e si adattano ai cambiamenti della rete. **I protocolli di routing ibridi, vettori di distanza e allo stato di collegamento** offrono diversi approcci per determinare i percorsi ottimali. **L'instradamento statico e le rotte predefinite** forniscono un controllo manuale sulle decisioni di instradamento. Le tecniche di **gestione della larghezza di banda** come il **traffic shaping e il QoS** garantiscono un utilizzo efficiente della rete. Il confronto e il posizionamento appropriato dei dispositivi di rete migliora le prestazioni e la sicurezza della rete.

Padroneggiando le **tecnologie e i concetti di routing**, gli amministratori di rete possono costruire **reti robuste ed efficienti** che soddisfano le esigenze della connettività moderna.

______