---
title: "Fondamenti di rete: cosa sono le sottoreti e le VLAN"
draft: false
toc: true
date: 2023-07-23
lastmod: 2026-11-13
description: "Scopri le basi delle sottoreti e delle VLAN, come suddividere una rete e come migliorarne l’efficienza e la sicurezza."
genre: ["Fondamenti di rete", "Suddivisione in subnet", "VLAN", "Gestione della rete", "Sicurezza della rete", "Indirizzamento IP", "Segmentazione della rete", "Uso efficiente delle risorse", "Prestazioni di rete", "IPv4"]
tags: ["fondamenti di rete", "sottorete", "suddivisione in subnet", "VLAN", "gestione della rete", "sicurezza della rete", "indirizzamento IP", "segmentazione della rete", "uso efficiente delle risorse", "prestazioni di rete", "IPv4", "configurazione sottorete", "maschere di sottorete", "assegnazione indirizzi IP", "comunicazione inter-VLAN", "porte switch", "configurazione VLAN", "interfacce VLAN", "connettività di rete", "sottoreti", "domini di broadcast", "misure di sicurezza", "intervallo indirizzi IP", "esempi di sottorete", "distribuzione VLAN", "amministrazione di rete", "configurazione switch", "configurazione router", "scalabilità di rete", "comunicazione e trasferimento dati", "reti efficienti"]
cover: "/img/cover/A_symbolic_illustration_of_interconnected_comp.webp"
coverAlt: "Illustrazione simbolica di reti di computer interconnesse con sottorete e VLAN"
coverCaption: "Reti efficienti: sottorete e VLAN spiegate in modo semplice."
---

## Fondamenti di rete: cosa sono le sottoreti e le VLAN

### Introduzione

Nel mondo connesso di oggi, le reti informatiche sono essenziali per la comunicazione e il trasferimento dei dati. Conoscere i fondamenti di rete è utile ai professionisti IT e agli utenti. Questo articolo spiega che cosa sono le sottoreti, come suddividere una rete e come funzionano le VLAN.

## Sottoreti: un approfondimento

### Che cos’è una sottorete?

{{< youtube id="nR5xCmXJE5E" >}}

Una **sottorete** è una suddivisione logica di una rete IP. Consente all’amministratore di dividere una rete grande in segmenti più piccoli e gestibili. Ogni sottorete ha un proprio intervallo di indirizzi IP, così gli indirizzi disponibili si usano meglio.

### Perché usare le sottoreti?

Le reti informatiche usano le sottoreti per vari motivi:

1. **Segmentazione della rete:** Le sottoreti dividono una rete grande in reti più piccole. Questo migliora le prestazioni e riduce la congestione.

2. **Maggiore sicurezza:** Separare i dispositivi in sottoreti diverse permette di usare firewall e liste di controllo degli accessi per gestire il traffico e migliorare la sicurezza.

3. **Uso efficiente delle risorse:** La suddivisione in sottoreti distribuisce meglio gli indirizzi IP, una risorsa limitata nello spazio IPv4.

### Come creare sottoreti?

{{< youtube id="LdSAaSHfK3M" >}}

La suddivisione in sottoreti divide una rete in sottoreti più piccole. Segui questi passaggi:

1. **Definisci i requisiti della rete:** Stabilisci quante sottoreti e quanti host servono per ciascuna sottorete.

2. **Scegli uno schema di indirizzamento IP:** Seleziona uno schema adatto al numero richiesto di sottoreti e host.

3. **Calcola le maschere di sottorete:** Determina le maschere in base al numero di sottoreti e host richiesti.

4. **Assegna gli indirizzi IP:** Assegna gli indirizzi a ogni sottorete e verifica che rientrino nell’intervallo corretto.

5. **Testa e verifica:** Prova la connettività e controlla gli indirizzi assegnati.

### Esempi di suddivisione in sottoreti

Consideriamo un semplice esempio di suddivisione in sottoreti:

Supponiamo di avere l’intervallo IP 192.168.0.0/24 e di voler creare quattro sottoreti con lo stesso numero di host. Possiamo suddividere la rete così:

1. **Passaggio 1: Definisci i requisiti della rete:** Servono quattro sottoreti con lo stesso numero di host.

2. **Passaggio 2: Scegli uno schema di indirizzamento IP:** Scegliamo una maschera /26, che consente 64 indirizzi per sottorete.

3. **Passaggio 3: Calcola le maschere di sottorete:** La maschera /26 è 255.255.255.192.

4. **Passaggio 4: Assegna gli indirizzi IP:** Assegniamo questi indirizzi alle sottoreti:

   - sottorete 1: 192.168.0.0/26
   - sottorete 2: 192.168.0.64/26
   - sottorete 3: 192.168.0.128/26
   - sottorete 4: 192.168.0.192/26

5. **Passaggio 5: Testa e verifica:** Verifichiamo la connettività tra i dispositivi di ogni sottorete.

### Tabelle utili per la suddivisione in sottoreti

#### Tabella di riferimento per il calcolo delle sottoreti

| Maschera di sottorete | Notazione CIDR | Indirizzi IP totali | Indirizzi IP utilizzabili |
|-------------|---------------|--------------------|---------------------|
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224 | 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1,024 | 1,022 |
| /21 | 255.255.248.0 | 2,048 | 2,046 |
| /20 | 255.255.240.0 | 4,096 | 4,094 |
| /19 | 255.255.224.0 | 8,192 | 8,190 |
| /18 | 255.255.192.0 | 16,384 | 16,382 |
| /17 | 255.255.128.0 | 32,768 | 32,766 |
| /16 | 255.255.0.0 | 65,536 | 65,534 |
| /15 | 255.254.0.0 | 131,072 | 131,070 |
| /14 | 255.252.0.0 | 262,144 | 262,142 |
| /13 | 255.248.0.0 | 524,288 | 524,286 |
| /12 | 255.240.0.0 | 1,048,576 | 1,048,574 |
| /11 | 255.224.0.0 | 2,097,152 | 2,097,150 |
| /10 | 255.192.0.0 | 4,194,304 | 4,194,302 |
| /9 | 255.128.0.0 | 8,388,608 | 8,388,606 |
| /8 | 255.0.0.0 | 16,777,216 | 16,777,214 |
| /7 | 254.0.0.0 | 33,554,432 | 33,554,430 |
| /6 | 252.0.0.0 | 67,108,864 | 67,108,862 |
| /5 | 248.0.0.0 | 134,217,728 | 134,217,726 |
| /4 | 240.0.0.0 | 268,435,456 | 268,435,454 |
| /3 | 224.0.0.0 | 536,870,912 | 536,870,910 |
| /2 | 192.0.0.0 | 1,073,741,824 | 1,073,741,822 |
| /1 | 128.0.0.0 | 2,147,483,648 | 2,147,483,646 |
| /0 | 0.0.0.0 | 4,294,967,296 | 4,294,967,294 |

#### Tabella delle sottoreti utilizzabili

| Notazione CIDR | Numero di sottoreti utilizzabili |
|---------------|-------------------------|
| /0 | 1 |
| /1 | 2 |
| /2 | 4 |
| /3 | 8 |
| /4 | 16 |
| /5 | 32 |
| /6 | 64 |
| /7 | 128 |
| /8 | 256 |
| /9 | 512 |
| /10 | 1024 |
| /11 | 2048 |
| /12 | 4096 |
| /13 | 8192 |
| /14 | 16384 |
| /15 | 32768 |
| /16 | 65536 |
| /17 | 131072 |
| /18 | 262144 |
| /19 | 524288 |
| /20 | 1048576 |
| /21 | 2097152 |
| /22 | 4194304 |
| /23 | 8388608 |
| /24 | 16777216 |
| /25 | 33554432 |
| /26 | 67108864 |
| /27 | 134217728 |
| /28 | 268435456 |
| /29 | 536870912 |
| /30 | 1073741824 |
| /31 | 2147483648 |
| /32 | 4294967296 |

#### Tabella delle potenze di due

| Potenza di due | Valore |
|--------------|-------|
| 2^32 | 4294967296 |
| 2^31 | 2147483648 |
| 2^30 | 1073741824 |
| 2^29 | 536870912 |
| 2^28 | 268435456 |
| 2^27 | 134217728 |
| 2^26 | 67108864 |
| 2^25 | 33554432 |
| 2^24 | 16777216 |
| 2^23 | 8388608 |
| 2^22 | 4194304 |
| 2^21 | 2097152 |
| 2^20 | 1048576 |
| 2^19 | 524288 |
| 2^18 | 262144 |
| 2^17 | 131072 |
| 2^16 | 65536 |
| 2^15 | 32768 |
| 2^14 | 16384 |
| 2^13 | 8192 |
| 2^12 | 4096 |
| 2^11 | 2048 |
| 2^10 | 1024 |
| 2^9 | 512 |
| 2^8 | 256 |
| 2^7 | 128 |
| 2^6 | 64 |
| 2^5 | 32 |
| 2^4 | 16 |
| 2^3 | 8 |
| 2^2 | 4 |
| 2^1 | 2 |
| 2^0 | 1 |

## VLAN: reti locali virtuali

### Che cos’è una VLAN?

{{< youtube id="jC6MJTh9fRE" >}}

Una **VLAN (Virtual Local Area Network)** è un raggruppamento logico di dispositivi in una rete, indipendentemente dalla posizione fisica. Le VLAN creano domini di broadcast separati e migliorano flessibilità, sicurezza e scalabilità.

### Perché usare le VLAN?

Le VLAN offrono vari vantaggi nella gestione della rete:

1. **Maggiore sicurezza:** Le VLAN isolano i dati sensibili e limitano gli accessi non autorizzati. Il traffico resta in segmenti specifici e protegge le risorse importanti.

2. **Prestazioni migliori:** Le VLAN separano logicamente il traffico, riducono la congestione e migliorano le prestazioni. Il traffico broadcast resta nella VLAN.

3. **Gestione di rete più semplice:** Le VLAN raggruppano i dispositivi per funzione, reparto o altri criteri, semplificando amministrazione e configurazione.

### Configurazione delle VLAN

In genere, la configurazione di una VLAN segue questi passaggi:

1. **Individua i requisiti VLAN:** Definisci scopo e ambito della distribuzione. Identifica i dispositivi e la VLAN a cui assegnarli.

2. **Assegna gli ID VLAN:** Assegna un ID univoco a ogni VLAN. Gli ID sono di solito numeri da 1 a 4094, con alcuni valori riservati.

3. **Configura le porte dello switch:** Assegna le porte alle VLAN appropriate come porte access o trunk.

4. **Configura le interfacce VLAN:** Se serve comunicare tra VLAN, [configura le interfacce VLAN](https://simeononsecurity.com/network-plus/ethernet-switching-vlans-port-configurations-security/) su uno switch di livello 3 o un router.

5. **Testa e verifica:** Verifica la connettività tra i dispositivi di ogni VLAN.

### Tabella delle VLAN riservate

| Tag VLAN | Descrizione |
|-------------------|----------------------------------------------------|
| VLAN 0 | ID VLAN riservato, da non usare |
| VLAN 1 | VLAN predefinita per molti dispositivi di rete |
| VLAN 2 | VLAN predefinita per il traffico di gestione |
| VLAN 3-4 | ID VLAN riservati |
| VLAN 5 | Riservato all’ID VLAN Token Ring |
| VLAN 6-1001 | ID VLAN riservati |
| VLAN 1002-1005 | VLAN predefinite Cisco per scopi specifici |
| VLAN 1006-1024 | ID VLAN riservati |
| VLAN 1025-4094 | Riservato all’intervallo VLAN esteso |
| VLAN 4095 | ID VLAN riservato, da non usare |

## Conclusione

[Capire le sottoreti](https://simeononsecurity.com/articles/networking-basics-what-is-a-switch-router-gateway-subnet-firewall-and-dmz/) e le VLAN è essenziale per progettare e gestire reti informatiche efficienti. Le sottoreti segmentano la rete e migliorano prestazioni e sicurezza. Le VLAN raggruppano logicamente i dispositivi e rendono la rete più flessibile e gestibile. Seguendo i passaggi descritti, gli amministratori possono suddividere le reti e configurare VLAN secondo le esigenze.

I fondamenti di rete sono la base per reti solide e scalabili, adatte alle esigenze della comunicazione e del trasferimento dati moderni.

## Riferimenti

- [Fondamenti di subnetting](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)
- [Comprendere e configurare le VLAN](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst4500/12-2/25ew/configuration/guide/conf/vlans.pdf)
- [Standard IEEE 802.1Q](https://standards.ieee.org/standard/802_1Q-2018.html)
