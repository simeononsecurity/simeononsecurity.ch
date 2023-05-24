---
title: "Gaming the Helium Network: sfruttare le vulnerabilità con MiddleMan e Chirp Stack Packet Multiplexer"
date: 2023-02-18
toc: true
draft: false
description: "Scopri come giocare alla rete Helium sfruttando le vulnerabilità con MiddleMan e Chirp Stack Packet Multiplexer, nonché i rischi e le conseguenze di ciò."
tags: ["Rete di elio", "Prova di copertura", "Intermediario", "Multiplexer di pacchetti Chirp Stack", "gioco", "sfruttare le vulnerabilità", "Rete LoRaWAN", "criptovaluta", "blockchain", "rete decentrata", "hotspot", "spoofing", "imbrogliare", "attività illegale", "sanzioni", "integrità della rete", "ricompense", "attori malintenzionati", "sicurezza della rete", "host legittimi"]
cover: "/img/cover/A_cartoonish_depiction_of_a_group_of_individuals_exploiting.png"
coverAlt: "Una rappresentazione da cartone animato di un gruppo di individui che sfruttano un palloncino di elio con un'immagine di un gateway LoRaWAN e MiddleMan o Chirp Stack Packet Multiplexer sullo sfondo."
coverCaption: ""
---

**Disclaimer**:
È importante notare che il gioco sulla rete Helium è un'attività illegale e non etica che è fortemente disapprovata dalla comunità Helium e dalla più ampia comunità di criptovalute e blockchain. Giocare sulla rete mina l'integrità della rete e danneggia gli host legittimi che forniscono una copertura preziosa alla rete.

Inoltre, mentre l'uso di MiddleMan e Chirp Stack Packet Multiplexer per sfruttare le vulnerabilità nella rete Helium può essere motivo di preoccupazione, è importante notare che questi problemi possono essere risolti solo da Helium introducendo gateway sicuri. Ciò richiederebbe la sostituzione di tutti gli hotspot sulla rete, che è un'impresa significativa e potrebbe non essere fattibile. Di conseguenza, la comunità di Helium deve rimanere vigile e proattiva nell'affrontare le sfide poste dai giochi in rete.

Vale anche la pena notare che il team di Helium è a conoscenza del problema da tempo e ha adottato misure per risolverlo, ma sono necessarie ulteriori azioni per risolvere il problema. La comunità chiede che vengano intraprese azioni concrete per affrontare queste vulnerabilità e per garantire che la rete possa continuare a scalare e crescere in modo sicuro e affidabile.

Scrivendo questo articolo, speriamo di aumentare la consapevolezza del problema dei giochi sulla rete Helium e dell'uso di MiddleMan e Chirp Stack Packet Multiplexer per sfruttare le vulnerabilità del sistema. Riteniamo che facendo luce su questo problema e portando più pubblicità ad esso, la comunità Helium e la più ampia comunità blockchain e criptovaluta possano unirsi per affrontare il problema e lavorare per una rete più sicura e affidabile.

Inoltre, evidenziando questo problema, speriamo di incoraggiare il team di Helium a intraprendere azioni più decisive per affrontare le vulnerabilità della rete e implementare misure di sicurezza più robuste per prevenire il gioco in futuro. Riteniamo che sia importante per il team di Helium essere trasparenti sui loro sforzi per affrontare questo problema e comunicare con la comunità in merito ai loro progressi nella correzione di queste vulnerabilità.

Infine, portando più pubblicità a questo problema, speriamo di incoraggiare una maggiore consapevolezza e educazione sui rischi e le conseguenze del gioco sulla rete Helium. È importante che gli utenti comprendano l'importanza del comportamento etico sulla rete e il potenziale danno che può essere causato dal gioco. Lavorando insieme per affrontare questi problemi, possiamo contribuire a garantire la continua crescita e il successo della rete Helium.

In sintesi, il gioco sulla rete Helium non è tollerato dalla comunità o da noi e incoraggiamo gli utenti ad agire in modo etico e legale quando partecipano alla rete. Sebbene esistano vulnerabilità nella rete che possono essere sfruttate, è importante rimanere vigili e proattivi nell'affrontare questi problemi e lavorare per una rete più sicura e affidabile per tutti gli utenti.

# Come giocare alla rete Helium con MiddleMan e Chirp Stack Packet Multiplexer
La rete Helium è una rete LoRaWAN® decentralizzata che compensa coloro che ospitano hotspot fisici premiandoli con token Helium, o $HNT. Questo sistema è noto come Proof-of-Coverage (PoC). Man mano che la rete è cresciuta e la consapevolezza di questo progetto è aumentata, c'è stato un numero sempre maggiore di imbroglioni che stanno sfruttando il protocollo e i meccanismi di ricompensa. In questo articolo, discuteremo come giocare alla rete Helium utilizzando MiddleMan e Chirp Stack Packet Multiplexer.

## Comprensione del problema del gioco di rete Helium
La rete Helium si basa su Proof of Coverage per garantire che gli hotspot forniscano copertura dove è necessario. Tuttavia, questo sistema è vulnerabile a giochi, spoofing, hacking e altri tipi di comportamenti scorretti che possono danneggiare la rete. Il problema del gioco sulla rete Helium sta costando agli host legittimi migliaia di $ HNT al mese. Helium, Inc, insieme a DeWi, ha intrapreso un'azione aggressiva all'inizio del 2022 per aiutare a sradicare questo problema.

## Hardware richiesto
- [Dragino LPS8](https://www.ebay.com/sch/i.html?_nkw=dragino+lps8)
- [Other Lorawan Gateways that Use the Semtech Forwarder](https://amzn.to/41bcskb)
- [Raspberry Pi](https://amzn.to/3KjFCYp)
- [Other PC that can run docker images or linux software](https://amzn.to/3YkFhcj)

## Utilizzo di MiddleMan per giocare alla rete Helium
Un modo per giocare alla rete Helium è usare MiddleMan. MiddleMan è uno strumento software che può essere utilizzato per creare un falso hotspot che sembra fornire copertura in una posizione specifica. Utilizzando MiddleMan, un utente può creare un falso hotspot che riceverà ricompense per fornire copertura in una particolare area, anche se l'hotspot non si trova fisicamente in quella zona.

Per utilizzare MiddleMan, un utente deve installare il software e creare un falso hotspot. L'utente può quindi configurare l'hotspot per segnalare la sua posizione alla rete Helium utilizzando uno strumento di spoofing GPS. La rete Helium crederà che l'hotspot falso stia fornendo copertura nella posizione specificata e ricompenserà l'utente con $HNT.

Dovresti impostare il tuo gateway lorawan in modo che punti a questo software e manipola i valori in modo che tutti i PoC ricevuti siano considerati validi. L'utilizzo dello spedizioniere semtech è uno dei vari standard nella comunità LoraWAN. Risolvere il problema della manipolazione richiederebbe di reinventare la ruota e implementare il proprio protocollo da zero. Cose come checksum e crittografia impedirebbero che ciò accada. Ma renderebbe anche più difficile per i fornitori con hardware diverso creare hotspot. Per non parlare del fatto che è un caso d'uso supportato avere un minatore di elio e più gateway lora per una migliore copertura. Anche se questo è più un problema a livello aziendale.

 - [helium-DIY-middleman](https://github.com/curiousfokker/helium-DIY-middleman)

## Utilizzo del multiplexer di pacchetti Chirp Stack per giocare alla rete Helium
Un altro modo per giocare alla rete Helium è utilizzare Chirp Stack Packet Multiplexer. Chirp Stack Packet Multiplexer è uno strumento che può essere utilizzato per creare un hotspot virtuale in grado di ricevere pacchetti da più hotspot fisici. Utilizzando Chirp Stack Packet Multiplexer, un utente può creare un hotspot virtuale che riceve pacchetti da hotspot fisici in più posizioni, il che aumenterà i premi guadagnati.

Per utilizzare Chirp Stack Packet Multiplexer, un utente deve installare il software e configurarlo per ricevere pacchetti da hotspot fisici o gateway lorawan in più posizioni. L'hotspot riceverà i pacchetti e segnalerà la sua posizione alla rete Helium, che ricompenserà l'utente con $ HNT.

Ciò consente l'ingresso di più spedizionieri e l'uscita di più gateway. Esistono casi d'uso legittimi per questo software nella comunità LoraWAN, ma il suo utilizzo nell'elio è nella migliore delle ipotesi un'area grigia. Dipende da come lo usi e anche da quale sia il tuo intento.

L'impostazione di questo richiede alcuni file di configurazione. Ma può essere fatto in 5 minuti o meno.
- [chirpstack-packet-multiplexer](https://github.com/brocaar/chirpstack-packet-multiplexer)


## Rischi e conseguenze del gioco sulla rete Helium
Giocare sulla rete Helium è un'attività rischiosa e illegale che può avere gravi conseguenze. Helium, Inc, insieme a DeWi, sta lavorando attivamente per rilevare e prevenire i giochi sulla rete e gli utenti sorpresi a giocare sulla rete saranno penalizzati.

Le sanzioni per il gioco sulla rete Helium possono includere la perdita dell'accesso alla rete, la messa al bando permanente degli hotspot e la perdita di qualsiasi $ HNT guadagnato attraverso il gioco. Inoltre, il gioco sulla rete Helium compromette l'integrità della rete e danneggia gli host legittimi che forniscono una preziosa copertura alla rete.

## Conclusione
Sebbene la rete Helium offra opportunità agli host di hotspot legittimi di guadagnare ricompense tramite la prova di copertura, rappresenta anche un obiettivo attraente per gli attori malintenzionati che cercano di ingannare il sistema. L'uso di MiddleMan e Chirp Stack Packet Multiplexer, anche se non condonato da Helium Inc. o dalla comunità più ampia, è un esempio di come alcuni malintenzionati stiano sfruttando le vulnerabilità della rete per raccogliere ricompense a spese di altri.

È importante che la comunità di Helium continui a lavorare insieme per identificare e affrontare i giochi sulla rete, poiché minaccia l'integrità del sistema e mina gli sforzi degli host legittimi. Ciò può includere sforzi per sviluppare e implementare misure di rilevamento e prevenzione più sofisticate, nonché aumentare la consapevolezza e l'educazione sui rischi e le conseguenze del gioco in rete.

In definitiva, il successo della rete Helium dipende dalla volontà delle sue parti interessate di lavorare insieme per costruire un sistema sicuro, affidabile e degno di fiducia che fornisca valore reale ai suoi utenti. Rimanendo vigile e proattiva nell'affrontare le sfide poste dai giochi, la comunità può aiutare a garantire che la rete Helium continui a crescere e ad evolversi in una direzione positiva.