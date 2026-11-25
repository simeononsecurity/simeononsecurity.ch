---
title: "Meshtastic vs MeshCore vs Reticulum"
date: 2026-09-01
lastmod: 2026-11-25
toc: true
draft: false
description: "Confronta Meshtastic, MeshCore e Reticulum in base a routing, tempo di trasmissione, infrastruttura, trasporto e casi d’uso offline."
genre: ["LoRa", "Reti mesh", "Comunicazioni fuori rete", "Comunicazioni di emergenza", "Radioamatori", "Software a codice aperto", "Preparazione alle emergenze", "Reti wireless", "Privacy", "Networking"]
tags: ["meshtastic vs meshcore vs reticulum", "rete Reticulum", "meshtastic", "meshcore", "reticulum", "lxmf", "rete mesh LoRa", "comunicazioni fuori rete", "rnode", "radio a pacchetto", "networking indipendente dal trasporto", "reti mesh", "comunicazioni di emergenza", "rete mesh comunitaria", "tempo di trasmissione LoRa", "flooding gestito", "limite di hop", "nodo ripetitore", "room server", "app Sideband", "nomadnet", "meshchat", "comunicazioni per le emergenze", "radio fuori rete", "protocollo di rete mesh", "rete mesh regionale", "ingegneria RF"]
cover: "/img/cover/meshtastic-meshcore-reticulum-network-comparison.webp"
coverAlt: "Illustrazione che confronta tre sistemi di rete mesh con nodi, antenne e linee di collegamento su uno sfondo scuro e vivace, per rappresentarne le caratteristiche distintive."
coverCaption: ""
ref: ["/articles/meshcore-vs-meshtastic-comparison-guide", "/articles/field-deployable-connectivity-and-data-security-for-edge-nodes"]
---

## La risposta breve

**Questi tre progetti non risolvono tutti lo stesso problema.** Meshtastic e MeshCore sono sistemi di rete mesh LoRa con filosofie di routing diverse. Reticulum ha un ambito più ampio. È un livello di rete indipendente dal trasporto, che funziona contemporaneamente su LoRa, radio a pacchetto, Wi-Fi, Ethernet, collegamenti seriali e Internet.

**La domanda giusta non è «qual è il migliore?».** È «quale architettura si adatta alla rete che voglio costruire?».

*Meshtastic è adatto alle reti ad hoc e agli utenti in movimento.* **MeshCore è adatto a un’infrastruttura fissa costruita intenzionalmente.** **Reticulum è adatto alle reti che devono collegare trasporti diversi o unire reti altrimenti separate.** Chi costruisce una singola rete LoRa regionale di solito ha bisogno solo di una delle prime due opzioni.

______

## Definisci la rete da costruire

Prima di confrontare i protocolli, scrivi cosa deve fare la rete. Per la maggior parte delle implementazioni comunitarie e di comunicazione di emergenza, questi sono obiettivi utili:

- **Funzionamento senza licenza**, così chiunque può partecipare senza una licenza da radioamatore
- **Hardware a basso costo**, accessibile a una comunità che vuole distribuire la rete su larga scala
- **Bassi consumi**, idealmente sostenibili con energia solare o batterie
- **Comunicazioni a lunga distanza** senza dipendere da rete cellulare o Internet
- **Indipendenza dalle infrastrutture**, dalla rete elettrica, dagli ISP e dagli operatori telefonici
- **Configurazione e utilizzo alla portata di chi non è esperto di radio**
- **Adatto a una rete comunitaria**, non soltanto alla cantina di un singolo operatore
- **Possibilità di crescere oltre pochi nodi** senza crollare
- **Utilità durante i guasti alle infrastrutture**, quando torri cellulari e Internet non funzionano
- **Consegna affidabile prima della distanza da record**

Tieni a mente questo elenco mentre prosegui. Valuteremo ogni compromesso architetturale rispetto a questi requisiti.

______

## Meshtastic

**Meshtastic** è l’opzione più matura e diffusa. Offre molti vantaggi per l’utente medio.

- **Ecosistema maturo** con anni di sviluppo attivo
- **Ampia comunità**, Discord attivo e documentazione completa
- **Ampio supporto hardware** per schede LILYGO, Heltec, RAK e Seeed
- **Buone app mobili** per iOS e Android
- **Facile da iniziare**, la prima configurazione richiede meno di 20 minuti
- **Buon supporto agli utenti portatili e in movimento** che entrano ed escono dalla rete in modo imprevedibile
- **Funzioni GPS e di telemetria** con un ecosistema sviluppato attorno a esse
- **Implementazioni esistenti** nella maggior parte delle aree metropolitane, che semplificano l’adozione perché si entra in una rete anziché costruirla da zero

Per un’analisi completa del routing, della compatibilità hardware e della configurazione di Meshtastic rispetto a MeshCore, consulta la **[guida comparativa tra MeshCore e Meshtastic](/articles/meshcore-vs-meshtastic-comparison-guide/)**. Questo articolo si concentra sulla questione architetturale più importante per le implementazioni più grandi: **flooding gestito e limite di hop**.

### Flooding gestito e importanza degli hop

Nella **[diffusione controllata](https://meshtastic.org/docs/overview/mesh-algo/#broadcasts-using-managed-flooding)** di Meshtastic, un client normale annulla una ritrasmissione in attesa se sente prima lo stesso pacchetto ritrasmesso. `ROUTER` e `ROUTER_LATE` possono ritrasmettere comunque. Per `CLIENT_BASE` l’eccezione vale per il traffico da o verso un nodo preferito.

Il contatore dei salti di Meshtastic parte da **3** per impostazione predefinita e arriva al massimo a **7**. Dal firmware 2.7.11, i nodi di infrastruttura idonei possono [conservare il contatore](https://meshtastic.org/blog/zero-cost-hops-favorite-routers/) dopo il primo salto se il ripetitore precedente è un `ROUTER` o `ROUTER_LATE` preferito. Ogni ritrasmissione reale occupa il canale.

Un limite più alto può raggiungere più ripetitori, senza costringere tutti i ricevitori a trasmettere. **Più inoltri** possono comportare:

- **Più tempo di trasmissione** per ogni messaggio
- **Più copie in aria** se più ripetitori idonei inoltrano lo stesso pacchetto
- **Più contesa** sul canale condiviso
- **Più rischio di collisioni** quando più radio trasmettono nella stessa finestra
- **Maggiore consumo della batteria** su ogni nodo che riceve e ritrasmette
- **Minore capacità disponibile sul canale** per il traffico dei messaggi

La capacità LoRa è limitata dal tempo di trasmissione e dai limiti regionali del duty cycle, non dal numero di nodi. Una rete con dieci nodi molto attivi, che trasmettono spesso GPS e telemetria, può saturare un canale che cinquanta sensori tranquilli userebbero a malapena. Per questo una rete mesh densa con un limite di hop elevato degrada più rapidamente della stessa quantità di nodi con un limite inferiore e intervalli di telemetria controllati.

Da Meshtastic 2.6, i **messaggi diretti** usano la diffusione per scoprire il percorso e poi provano il prossimo salto appreso. Se non funziona, possono tornare alla diffusione.

Per una rete piccola o media, come quella di un club escursionistico, raramente è un problema. Per una **rete regionale progettata per coprire una città o più comuni**, diventa il principale vincolo di progettazione.

______

## MeshCore

I **ripetitori dedicati** formano lo strato fisso di inoltro di MeshCore. Le radio client sono terminali.

### Ruoli dei nodi

Le implementazioni MeshCore si basano su ruoli distinti, anziché su una rete piatta di nodi equivalenti:

- **Nodi companion o client** con una radio LoRa associata a un telefono o laptop, che comunicano tramite l’infrastruttura vicina quando è disponibile
- **Ripetitori**, progettati appositamente per inoltrare il traffico tra i client e gli altri elementi dell’infrastruttura. Svolgono gran parte del lavoro di routing
- **Room server** (facoltativi), che ospitano conversazioni di gruppo e consegnano i messaggi archiviati ai client quando si riconnettono

In MeshCore, il primo **messaggio diretto** può essere diffuso per scoprire un percorso. I successivi possono usarlo e, secondo la configurazione, tornare alla diffusione. **[I canali di gruppo pubblici e privati continuano a usare la diffusione](https://docs.meshcore.io/faq/#5-general)** tramite i ripetitori abilitati. Le radio client non inoltrano i pacchetti degli altri nodi.

### Perché si adatta a un’infrastruttura statica

*Questo è l’argomento centrale a favore di MeshCore.* Il modello di flooding Meshtastic offre vantaggi reali per le reti ad hoc e mobili: non richiede pianificazione, non ha infrastrutture da mantenere e gestisce bene i nodi che entrano ed escono. Il modello di routing MeshCore è avvantaggiato quando **gli utenti installano intenzionalmente un’infrastruttura**.

Una rete basata su ripetitori noti e posizionati in alto permette di progettare la copertura in modo intenzionale, invece di dipendere dai nodi che, in un determinato giorno, si trovano casualmente nel raggio gli uni degli altri. Questo conta per:

- **Nodi permanenti sui tetti** con alimentazione affidabile
- **Torri** e infrastrutture di comunicazione esistenti
- **Ripetitori solari** in siti non presidiati
- **Siti relay in montagna o in posizione elevata**
- **Infrastrutture comunitarie** condivise tra più gruppi
- **Reti regionali** che coprono più di un quartiere
- **Comunicazioni di emergenza**, dove una copertura prevedibile conta più della flessibilità

Ricollega questo ai principi RF: **collegamenti affidabili tra infrastrutture posizionate correttamente contano più del massimo guadagno dell’antenna, della potenza di trasmissione o della portata teorica.** **Entrambe le reti beneficiano di ripetitori ben posizionati.** I nodi che ritrasmettono dipendono dai ruoli e dal traffico.

______

## L’argomento dei nodi mobili e il suo costo

Una proposta frequente è: *«Meshtastic è migliore per i nodi mobili, MeshCore per quelli statici, quindi usiamo Meshtastic per gli utenti e MeshCore come dorsale».*

Sulla carta sembra interessante. Nella pratica, combinare i due sistemi non offre automaticamente i vantaggi di entrambi, perché **Meshtastic e MeshCore usano architetture di rete e routing diverse e non si scambiano messaggi.** Collegarli richiede un livello di traduzione tra sistemi incompatibili, non la semplice scelta delle parti migliori.

Una volta collegati, gestisci:

- **Due reti distinte**, ognuna con la propria topologia e il proprio comportamento
- **Due modelli di routing** che non condividono lo stato
- **Un livello di traduzione** da sviluppare e mantenere nel tempo
- **Più infrastruttura** per ospitare il bridge
- **Più configurazione** in due ecosistemi firmware invece che in uno
- **Più punti di guasto**, perché il bridge può guastarsi indipendentemente dalle due reti mesh
- **Diagnosi più difficili**, perché un problema di consegna può trovarsi in una delle reti o nel bridge che le collega

Prima di adottare questo progetto, chiediti direttamente: **la complessità aggiunta risolve un problema che un singolo protocollo mesh ben configurato non riesce a risolvere?** Spesso un’implementazione MeshCore ben configurata con pochi nodi companion adatti agli utenti in movimento, oppure un’implementazione Meshtastic con alcuni relay ben posizionati e un limite di hop più alto, offre gran parte dei vantaggi pratici senza gestire due reti incollate insieme.

______

## Reticulum

Reticulum merita una categoria a parte, non un posto come «terza opzione di rete mesh LoRa», perché non è principalmente un protocollo mesh LoRa. **La sua caratteristica distintiva è l’indipendenza dal trasporto.**

Reticulum è uno stack di rete basato sulla crittografia. Non usa indirizzi sorgente, quindi i pacchetti non contengono informazioni sulla loro origine. Ogni indirizzo è sovrano: una volta generato, diventa raggiungibile globalmente in secondi o minuti e rimane raggiungibile anche se il dispositivo viene spostato fisicamente in un’altra parte della rete. Tutte le comunicazioni sono cifrate per impostazione predefinita con chiavi effimere e forward secrecy. Reticulum scarta i pacchetti non cifrati invece di consegnarli. Non servono driver del kernel. Funziona nello spazio utente su qualsiasi sistema con Python 3, incluso Raspberry Pi Zero.

Le interfacce supportate da Reticulum includono:

- **LoRa**, con hardware compatibile con RNode (un progetto definito e open source di ricetrasmettitore LoRa, realizzabile, installabile su schede comuni o acquistabile già pronto)
- **Radio a pacchetto**, tramite qualsiasi TNC che operi in modalità KISS, adatta alla radioamatoria VHF e UHF
- **Wi-Fi ed Ethernet cablata**, con rilevamento automatico dei peer senza router o server DHCP
- **Collegamenti seriali** per connessioni dirette tra dispositivi
- **TCP e UDP su reti IP esistenti**, compreso Internet
- **La rete I2P** e interfacce personalizzate per altri sistemi collegati tramite bridge Python

Su Reticulum funzionano applicazioni come **LXMF** (un protocollo di messaggistica tollerante ai ritardi) e strumenti per utenti finali come **Sideband**, **NomadNet** e i client comunitari **MeshChat**. Questi strumenti aggiungono alle reti Reticulum un livello di messaggistica e navigazione paragonabile a quello fornito subito da Meshtastic e MeshCore.

{{< figure src="reticulum-transport-independent-heterogeneous-network.webp" alt="Diagramma che mostra Reticulum collegare una rete mesh LoRa, una rete radio a pacchetto e un collegamento Internet in un’unica rete cifrata e indirizzabile" >}}

### Quando Reticulum ha senso

Il valore di Reticulum emerge chiaramente in una configurazione eterogenea, per esempio:

**Rete mesh LoRa → nodo Reticulum → collegamento IP → nodo Reticulum → rete radio**

Qui Reticulum fa ciò che né Meshtastic né MeshCore fanno: collega due sistemi di comunicazione altrimenti distinti in un’unica rete indirizzabile. È un requisito reale e specifico, non un miglioramento generico. È utile per:

- **Collegare reti geograficamente distanti** senza un collegamento radio diretto tra loro
- **Unire trasporti fisici diversi**, come una rete mesh LoRa da un lato e una rete radio a pacchetto dall’altro
- **Gateway radio-IP** che trasferiscono il traffico tra una rete radio sul campo e Internet
- **Reti sperimentali e di ricerca**, dove la possibilità di combinare trasporti conta più della semplicità di implementazione
- **Reti in cui nessun trasporto singolo copre tutti i requisiti**, quindi occorre collegare più parti

### Quando Reticulum aggiunge complessità inutile

Se tutti usano hardware LoRa compatibile e l’obiettivo reale è **una sola rete mesh LoRa regionale**, aggiungere Reticulum porta pochi vantaggi e un costo concreto. Ogni ulteriore livello dello stack di rete comporta più:

- **Configurazione** da impostare correttamente e mantenere coerente su tutti i nodi
- **Software** da installare, aggiornare e risolvere in caso di problemi
- **Hardware** in alcune configurazioni, in base al modo in cui si collegano le interfacce
- **Aspetti da diagnosticare** quando qualcosa non viene consegnato
- **Conoscenze richieste** per operatori che devono capire un terzo modello di rete

*Usa Reticulum quando l’indipendenza dal trasporto risolve un requisito reale, non solo perché supporta più tipi di interfaccia dell’alternativa.* Un problema di limite di hop in una rete mesh LoRa è un problema di configurazione di Meshtastic o MeshCore. Non è un problema di indipendenza dal trasporto, e Reticulum non lo trasforma in tale.

______

## Costruisci prima una rete mesh sana, prima di crearne tre frammentate

Se un protocollo soddisfa già i requisiti, **costruisci una rete sana** invece di diverse reti più piccole unite da bridge. Il principio «prima una mesh» dovrebbe guidare la maggior parte delle decisioni qui sopra.

In una rete comunitaria, **l’interoperabilità tra le persone che la usano già conta spesso più della flessibilità architetturale.** Una rete ampia e funzionante basata su un solo protocollo offre più valore pratico di tre reti interessanti dal punto di vista tecnico ma frammentate, che comunicano solo in parte.

### Le reti Meshtastic esistenti contano

**Non scartare Meshtastic solo perché MeshCore offre vantaggi architetturali per l’infrastruttura fissa.** Se una città ha già decine o centinaia di nodi Meshtastic, questa base installata è infrastruttura reale e una comunità reale. La migrazione ha un costo che un confronto delle specifiche non considera:

- **Hardware installato** da riflashare o sostituire
- **Utenti esistenti** che già sanno usare la rete
- **Conoscenze della comunità** accumulate attorno all’implementazione attuale
- **Ripetitori già distribuiti e posizionati**, a volte su tetti o torri difficili da raggiungere
- **Esperienza di configurazione** accumulata da chi gestisce la rete
- **Canali consolidati** che gli utenti già monitorano
- **Formazione necessaria** per chi deve imparare un secondo sistema

La scelta del protocollo è **in parte un problema ingegneristico e in parte una questione di adozione comunitaria.** L’architettura migliore sulla carta non vince automaticamente se obbliga una comunità attiva a ricominciare da zero.

______

## Il problema della rete regionale

Considera un’implementazione ipotetica tra più città:

**Città A, ripetitore, ripetitore, relay rurale, ripetitore, Città B, ripetitore, Città C**

In questa catena, **prova separatamente i messaggi di gruppo e quelli diretti**. MeshCore può riutilizzare il percorso per i diretti, ma diffonde ancora i messaggi di gruppo. Meshtastic può conservare il contatore sui collegamenti di infrastruttura idonei. Ogni ritrasmissione occupa il canale. Nessun protocollo garantisce la consegna da un capo all’altro.

In questo scenario, **limiti di hop, budget di airtime, comportamento del routing e progettazione dell’infrastruttura smettono di essere teorici** e determinano se la rete funziona da un’estremità all’altra. Alla scala geografica, le differenze architetturali tra Meshtastic e MeshCore non sono più accademiche.

{{< figure src="regional-mesh-network-repeater-chain-scaling.webp" alt="Diagramma di una rete mesh regionale che collega tre città con una serie di ripetitori e un relay rurale, mostrando come aumentano airtime e hop con la distanza" >}}

______

## La RF conta ancora più del protocollo

**Nessun software di routing sofisticato crea un percorso RF dove fisicamente non esiste.** Prima di attribuire un problema di copertura al protocollo, verifica i fondamentali:

- **Altezza dell’antenna** rispetto agli ostacoli
- **Linea di vista** tra le due estremità del collegamento
- **Libertà della zona di Fresnel**, distinta dalla linea di vista visiva
- **Perdite della linea di alimentazione**, dovute a un cavo coassiale economico o troppo lungo
- **Qualità dell’antenna** e compatibilità con la banda usata
- **Rumore di fondo** nel sito di ricezione
- **Terreno** tra i nodi
- **Posizionamento dei nodi**, compresi i margini di miglioramento realistici
- **Margine di collegamento**, la differenza tra il segnale ricevuto e il minimo necessario per decodificarlo

*Un’antenna da 2 dBi ben posizionata su un buon palo spesso supera un’antenna ad alto guadagno collocata male vicino alla finestra di una cantina.* La scelta del protocollo determina come la rete gestisce i collegamenti disponibili. Non crea collegamenti che la fisica non consente.

### Affidabilità prima della portata massima

**Non progettare una rete sulla base della distanza massima che un collegamento raggiunge occasionalmente.** Progettala perché i collegamenti funzionino con regolarità.

Per una rete comunitaria o di comunicazioni di emergenza, **la consegna prevedibile a 15 miglia ha più valore pratico di un collegamento che ogni tanto arriva a 40 miglia ma fallisce il resto del tempo.** Crea una copertura sovrapposta con infrastrutture affidabili invece di inseguire i record di distanza. Il principio vale per ogni protocollo.

______

## Quale scegliere

**Meshtastic ha senso** se dai valore a un ecosistema maturo, facilità di adozione, utenti portatili e in movimento e compatibilità con una comunità Meshtastic esistente. È la scelta predefinita giusta per la maggior parte di chi parte da zero.

I **ripetitori fissi** aiutano a pianificare la copertura, ma non eliminano la diffusione. Prima di scegliere, prova entrambi i protocolli con il traffico di gruppo, le impostazioni radio e la disposizione dei ripetitori previste.

**Reticulum ha senso** quando il problema supera una singola rete mesh LoRa e devi collegare trasporti diversi o reti altrimenti separate in un unico sistema indirizzabile.

Per una **rete infrastrutturale comunitaria senza licenza, a basso consumo e lunga portata, basata soprattutto su ripetitori fissi**, orientati verso MeshCore. **Prova il traffico di gruppo prima di cambiare.** Una rete di ripetitori fissi aiuta con la copertura, ma non offre percorsi diretti ai canali di gruppo. *Se nella tua zona esiste già una rete Meshtastic sana, sostituirla richiede vantaggi sufficienti a giustificare la frammentazione della comunità esistente.* Reticulum entra in gioco quando un solo protocollo mesh o un singolo trasporto fisico non basta più, non semplicemente perché fa più cose.

______

## Riferimenti

1. [Algoritmo di broadcast mesh di Meshtastic](https://meshtastic.org/docs/overview/mesh-algo/)
2. [Configurazione LoRa di Meshtastic (hop_limit)](https://meshtastic.org/docs/configuration/radio/lora/)
3. [Sito ufficiale di MeshCore](https://meshcore.co.uk/)
4. [Stack di rete Reticulum](https://reticulum.network/)
5. [Che cos’è Reticulum?](https://reticulum.network/manual/whatis.html)
6. [Configurazione delle interfacce Reticulum](https://reticulum.network/manual/interfaces.html)
7. [Guida comparativa tra MeshCore e Meshtastic](/articles/meshcore-vs-meshtastic-comparison-guide/)
