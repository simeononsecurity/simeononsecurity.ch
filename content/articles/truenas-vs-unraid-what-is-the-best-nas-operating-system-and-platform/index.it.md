---
title: "Unraid vs TrueNas: Quale sistema operativo NAS è più adatto a voi?"
date: 2023-02-16
toc: true
draft: false
description: "Un confronto completo tra Unraid e TrueNas, che include la facilità d'uso, le caratteristiche, la documentazione e la comunità, per aiutare gli utenti a decidere con cognizione di causa quale sia il sistema operativo NAS più adatto alle loro esigenze."
tags: ["Senza paura", "VeroNas", "Sistema operativo NAS", "Confronto", "Facilità d'uso", "Caratteristiche", "Documentazione", "Comunità", "Open Source", "Impresa", "Protezione dei dati", "Prestazioni", "Flessibilità", "Facile da usare", "Applicazioni di terze parti"]
cover: "/img/cover/Two_computer_servers_facing_each_other_one_blue_one_green.png"
coverAlt: "Due server uno di fronte all'altro, uno blu e uno verde. Sul lato blu c'è una persona in piedi che indossa un elmetto e un giubbotto di sicurezza. Sul lato verde una persona seduta sul divano."
coverCaption: ""
---

Quando si tratta di **costruire un sistema NAS (Network Attached Storage), due dei sistemi operativi più noti per i computer basati su x86 sono TrueNas e Unraid**. Entrambi offrono potenti funzioni per la gestione di un sistema NAS, ma la loro differenza principale risiede nel metodo di gestione dello storage.

In questo articolo confronteremo TrueNas e Unraid per aiutarvi a prendere la decisione migliore per le vostre esigenze.

## Panoramica di Unraid

**Unraid è un sistema operativo NAS proprietario sviluppato da Lime Technology**, una società di software con sede in California. È stato fondato nel 2005 e funziona su piattaforma Linux. L'obiettivo di Unraid è quello di rendere la tecnologia RAID più accessibile, eliminando le restrizioni su dimensioni, velocità, marca e protocollo del disco. Ciò consente una facile espansione degli array RAID e riduce al minimo il rischio di perdita dei dati.

______

## Introduzione a TrueNas

**TrueNas, precedentemente noto come FreeNas, è un sistema operativo NAS open-source sviluppato da iXsystems**, un'azienda privata con sede a San Jose, California. È stato lanciato nel 2005 ed è basato su FreeBSD e Linux. Gli sviluppatori di TrueNas si concentrano sul mercato aziendale e la scelta del file system predefinito (OpenZFS) riflette questo orientamento.

______

## Costo

**Gli utenti domestici che cercano il miglior sistema operativo NAS spesso si preoccupano del costo**. A questo proposito, TrueNas è un chiaro vincitore in quanto è open-source e completamente gratuito, almeno per TrueNas CORE, la versione destinata agli utenti domestici e alle applicazioni di archiviazione non critiche.

Unraid, invece, non è gratuito ma utilizza un modello di prezzo equo, senza abbonamenti o costi nascosti. È possibile scegliere tra tre piani Unraid, ognuno dei quali si differenzia solo per il numero di dispositivi di archiviazione che possono essere collegati. Il piano Basic costa 59 dollari, il piano Plus 89 dollari e il piano Pro 129 dollari.

______

## Facilità d'uso

**Unraid pone una forte enfasi sulla facilità d'uso e sulla flessibilità**. Dispone di un sistema unico di gestione dello storage che consente agli utenti di combinare diverse dimensioni e tipi di dischi e di aggiungere o rimuovere dischi senza alcuna interruzione. Offre inoltre un'interfaccia utente semplice e diretta, che facilita la configurazione e la gestione di un sistema NAS anche agli utenti non tecnici.

**TrueNas, invece, è orientato al mercato aziendale e richiede conoscenze più avanzate per la configurazione e la gestione**. La scelta del file system OpenZFS offre funzioni avanzate di protezione dei dati, come le istantanee, la compressione dei dati e la checksumming per garantire l'integrità dei dati.

______

## Caratteristiche

**Sia TrueNas che Unraid offrono supporto** per le condivisioni NFS, SMB per Windows e AFP per macOS e iOS. Inoltre, TrueNas offre servizi iSCSI, LDAP, Active Directory e Kerberos. Unraid non offre questi servizi, ma supporta i container Docker, consentendo agli utenti di accedere a un'ampia gamma di applicazioni.

**TrueNas dispone anche di un supporto integrato per i servizi di cloud storage** come Amazon S3, Google Cloud e Microsoft Azure, rendendo semplice lo spostamento dei dati nel cloud. Gli utenti di Unraid possono utilizzare soluzioni di terze parti, che però potrebbero richiedere ulteriori impostazioni e configurazioni.

**La piattaforma Linux di Unraid consente anche la configurazione di macchine virtuali** utilizzando KVM e assegnando dispositivi PCI/USB, come le schede grafiche, alle macchine virtuali. In questo modo è possibile utilizzare lo stesso computer sia per i media center che per i giochi.

**TrueNas include la propria tecnologia di containerizzazione**, Jails, e la propria opzione di virtualizzazione, Bhyve. Sebbene TrueNas offra molte delle applicazioni di terze parti più diffuse, come Plex, la selezione complessiva di software potrebbe essere inferiore rispetto a Unraid.

______

## Documentazione e comunità

TrueNas dispone di una documentazione completa che copre tutto, dalla configurazione alle API e alle piattaforme hardware. Il sito web di Unraid ha una sezione di documentazione meno estesa, ma più facile da navigare. Tuttavia, Unraid non dispone di una pagina di supporto individuale, ma gli utenti sono incoraggiati a porre domande sul forum ufficiale della comunità, descritto come amichevole, informativo e utile.

Anche TrueNas ha il suo forum ufficiale, ma potrebbe non essere così accogliente per i principianti come il forum di Unraid. Questo perché molti utenti di TrueNas sono professionisti IT che si occupano di gestione dello storage aziendale.

______

## Conclusione

Sia TrueNas che Unraid sono sistemi operativi NAS potenti e maturi, ciascuno con i propri punti di forza e di debolezza. TrueNas è ideale per chi ha una conoscenza avanzata della gestione dell'archiviazione e desidera le funzioni avanzate di protezione dei dati di OpenZFS. Unraid, invece, è più adatto agli utenti domestici che desiderano un sistema NAS flessibile e facile da usare.

In sintesi:

**Pro di TrueNas
- Gratuito e open-source
- Protezione avanzata dei dati con OpenZFS
- Ottime prestazioni

**Contro: **TrueNas
- Più difficile da usare
- Comunità poco amichevole

**Pro:** Unraid
- Facile da usare
- Ampia varietà di applicazioni di terze parti
- Comunità amichevole

**Contro di Unraid
- Prestazioni limitate

In definitiva, la scelta tra TrueNas e Unraid dipende dalle vostre esigenze specifiche e dal vostro livello di competenza tecnica. Considerate i vostri requisiti, confrontate le caratteristiche e i vantaggi di ciascuno e prendete una decisione informata.
