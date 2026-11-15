---
title: 'Fondamenti di rete: switch, router, firewall e DMZ'
draft: false
toc: true
date: 2023-07-21
lastmod: 2026-11-15
description: Scopri come switch, router, gateway, sottoreti, firewall e DMZ suddividono il traffico di rete e applicano i confini di sicurezza.
genre:
- Reti
- Infrastruttura IT
- Sicurezza di rete
- Architettura di rete
- Sicurezza informatica
- Comunicazione dei dati
- Tecnologia dell'informazione
- Fondamenti IT
- Gestione delle reti
- Connettività Internet
tags:
- fondamenti di rete
- switch
- router
- gateway
- sottoreti
- firewall
- DMZ
- rete locale
- LAN
- connettività di rete
- accesso a Internet
- gestione degli indirizzi IP
- segmentazione di rete
- sicurezza di rete
- suddivisione in sottoreti
- protezione firewall
- prestazioni di rete
- architettura di rete
- comunicazione dei dati
- gestione delle reti
- sicurezza informatica
- infrastruttura di rete
- fondamenti IT
- tecnologia dell'informazione
- gestione del traffico dati
- sicurezza IT
- progettazione di rete
- conformità IT
- protocolli di rete
- risoluzione dei problemi di rete
- amministrazione di rete
cover: /img/cover/A_symbolic_illustration_showing_interconnected.webp
coverAlt: Illustrazione simbolica di dispositivi interconnessi tramite switch, router, gateway e firewall.
coverCaption: I fondamenti di rete aiutano a creare reti sicure e affidabili.
---

## Introduzione

In un mondo tecnologico in rapida evoluzione, le reti collegano i dispositivi e consentono la comunicazione. Comprendere i fondamenti di rete è essenziale per i professionisti IT e per chi desidera ampliare le proprie conoscenze. Questo articolo offre una panoramica dei componenti di rete principali, tra cui switch, router, gateway, sottoreti, firewall e DMZ. Al termine conoscerai questi concetti e la loro importanza nella realizzazione di reti affidabili e sicure.

{{< youtube id="_IOZ8_cPgu8" >}}

## Switch: migliorare le prestazioni della rete locale

{{< youtube id="NDVImep5UBI" >}}

Uno **switch** è un dispositivo di rete che opera al livello di collegamento dati del modello OSI. Collega più dispositivi all'interno di una rete locale (LAN) e inoltra pacchetti di dati tra di essi. A differenza degli hub, che inviano i dati a tutti i dispositivi collegati, gli switch inoltrano i pacchetti solo al destinatario previsto. In questo modo riducono le collisioni e la congestione e migliorano le prestazioni della rete.

Funzioni e vantaggi principali degli switch:

- **Inoltro basato sulla porta**: a ogni porta dello switch viene assegnato un indirizzo univoco Media Access Control (MAC), che consente di recapitare i pacchetti direttamente al dispositivo di destinazione.
- **Reti LAN virtuali (VLAN)**: consentono di segmentare la rete e migliorare la sicurezza isolando il traffico tra gruppi di dispositivi diversi.
- **Qualità del servizio (QoS)**: gli switch possono assegnare priorità a determinati tipi di traffico, così le applicazioni sensibili alla latenza, come voce e video, ricevono larghezza di banda sufficiente.

______

## Router: collegare le reti e consentire l'accesso a Internet

{{< youtube id="lyIUgr9JOLs" >}}

Gli switch operano all'interno di una LAN, mentre i **router** collegano più reti. Funzionano al livello di rete del modello OSI e usano protocolli di routing per determinare il percorso migliore verso la destinazione dei pacchetti. Oltre a interconnettere le reti, consentono ai dispositivi di accedere a Internet.

Funzioni e vantaggi principali dei router:

- **Gestione degli indirizzi IP**: usano gli indirizzi IP per identificare e instradare i pacchetti tra reti diverse.
- **Network Address Translation (NAT)**: trasformano gli indirizzi IP privati usati nella LAN in indirizzi IP pubblici quando comunicano con Internet.
- **Funzioni firewall**: molti router integrano funzioni firewall di base per proteggere la rete dagli accessi non autorizzati.
- **Dynamic Host Configuration Protocol (DHCP)**: possono agire da server DHCP e assegnare automaticamente indirizzi IP ai dispositivi della rete.

______

## Gateway: collegare reti di tipo diverso

{{< youtube id="SXZC6D7TRfM" >}}

Un **gateway** è un dispositivo o componente software che collega reti con protocolli o architetture differenti e ne consente la comunicazione. Agisce da intermediario e converte i pacchetti da un formato di rete a un altro. Per esempio, può collegare una rete locale a Internet.

Funzioni e vantaggi principali dei gateway:

- **Traduzione dei protocolli**: convertono i pacchetti, consentendo a reti che utilizzano protocolli di comunicazione diversi di scambiare informazioni.
- **Integrazione delle reti**: integrano reti con architetture differenti e facilitano la comunicazione.
- **Applicazione delle misure di sicurezza**: spesso implementano misure come il filtraggio dei pacchetti o la crittografia per proteggere la trasmissione tra reti.

______

## Sottoreti: organizzare le reti per comunicare in modo efficiente

{{< youtube id="nR5xCmXJE5E" >}}

Una **sottorete** è una suddivisione logica di una rete IP. Dividere una rete in sottoreti più piccole e semplici da gestire può migliorare le prestazioni e la sicurezza. La maschera di sottorete definisce ogni sottorete e determina l'intervallo di indirizzi IP che le viene assegnato.

Vantaggi delle sottoreti:

- **Prestazioni migliori**: dividere una rete grande localizza il traffico, riduce la congestione complessiva e migliora le prestazioni.
- **Maggiore sicurezza**: le regole di controllo degli accessi possono limitare la comunicazione tra sottoreti e aggiungere un livello di protezione.
- **Gestione semplificata**: raggruppare i dispositivi in modo logico agevola l'assegnazione degli indirizzi IP, il routing e la risoluzione dei problemi.

______

## Firewall: proteggere le reti dagli accessi non autorizzati

{{< youtube id="kDEX1HXybrU" >}}

Un **firewall** è un dispositivo di sicurezza di rete che monitora e controlla il traffico in entrata e in uscita in base a regole di sicurezza predefinite. Agisce da barriera tra le reti interne e quelle esterne, come Internet, per impedire accessi non autorizzati e potenziali minacce.

Funzioni e vantaggi principali dei firewall:

- **Filtraggio dei pacchetti**: ispezionano i pacchetti in entrata e in uscita e filtrano il traffico potenzialmente dannoso secondo regole definite.
- **Sistema di prevenzione delle intrusioni (IPS)**: i firewall con IPS possono rilevare e impedire attacchi di rete, comprese infezioni malware e tentativi di intrusione.
- **Supporto per reti private virtuali (VPN)**: molti firewall supportano le VPN per fornire accesso remoto sicuro tramite Internet.
- **Controllo delle applicazioni**: i firewall avanzati ispezionano il livello applicativo e permettono di controllare nel dettaglio applicazioni specifiche e il loro uso della rete.

______

## DMZ: migliorare la sicurezza della rete

{{< youtube id="dqlzQXo1wqo" >}}

Una **zona demilitarizzata (DMZ)** è un segmento di rete tra una rete interna e reti esterne come Internet. Isola dalla rete interna i servizi accessibili al pubblico, come i server web o di posta elettronica, e aggiunge un livello di sicurezza.

Principali vantaggi e usi delle DMZ:

- **Maggiore sicurezza**: collocare i servizi pubblici in una DMZ riduce il rischio che gli attaccanti raggiungano la rete interna.
- **Superficie di attacco ridotta**: solo i servizi necessari vengono esposti a Internet, limitando i possibili percorsi di attacco.
- **Conformità normativa**: regolamenti come il Payment Card Industry Data Security Standard (PCI DSS) richiedono spesso una DMZ per proteggere i dati sensibili dei clienti.

______

## Sequenza di risoluzione dei problemi per il 2026

Procedi dal client verso l'esterno. Controlla lo stato del collegamento, l'assegnazione dell'indirizzo, il gateway predefinito, la risoluzione DNS, la selezione della route, la policy del firewall e il servizio dell'applicazione. Prima di modificare una regola, registra l'indirizzo sorgente, la destinazione, il protocollo, la porta, l'ora e l'errore osservato.

Acquisisci pacchetti soltanto sulle reti che possiedi o amministri. Mantieni le interfacce di gestione su una rete con accesso limitato, segmenta i dispositivi per ospiti e IoT e controlla il percorso creato da ogni inoltro di porta. Il [glossario di rete NIST](https://csrc.nist.gov/glossary) e gli [avvisi CISA](https://www.cisa.gov/news-events/cybersecurity-advisories) offrono riferimenti utili per la terminologia e i rischi attuali.

## Conclusione

Comprendere i componenti di rete è essenziale per costruire e mantenere reti efficienti, sicure e affidabili. In questo articolo abbiamo esaminato funzioni e vantaggi di switch, router, gateway, sottoreti, firewall e DMZ. Conoscere questi concetti ti aiuterà a progettare e gestire reti che rispondono alle esigenze moderne di connettività.

Considera sempre i requisiti specifici della tua rete e consulta la documentazione e le normative governative pertinenti, come gli standard **Federal Information Processing Standards (FIPS)** e le linee guida del **National Institute of Standards and Technology (NIST)**, per seguire le migliori pratiche e rispettare i requisiti di conformità.

## Riferimenti

- Federal Information Processing Standards (FIPS): [https://www.nist.gov/itl/fips](https://www.nist.gov/itl/fips)
- National Institute of Standards and Technology (NIST): [https://www.nist.gov/](https://www.nist.gov/)
