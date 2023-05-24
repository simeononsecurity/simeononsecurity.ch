---
title: "Aggiornamento firmware offline per Ubiquiti Unifi UDM Pro e UDM SE tramite riga di comando SSH"
draft: false
toc: true
date: 2023-05-28
description: "Scopri come aggiornare il firmware di Ubiquiti Unifi UDM Pro e UDM SE offline tramite SSH della riga di comando per prestazioni e sicurezza ottimali."
tags: ["Aggiornamento del firmware Ubiquiti", "UDM Pro", "UDM SE", "aggiornamento del firmware offline", "SSH della riga di comando", "gestione della rete", "sicurezza della rete", "aggiornamento del firmware", "Connessione SSH", "file firmware", "Controller di rete UniFi", "correzioni di bug", "miglioramenti delle prestazioni", "patch di sicurezza", "rete", "dispositivi di rete", "tecnologia", "gestione IT", "processo di aggiornamento del firmware", "ottimizzazione della rete", "Aggiornamento del firmware di Ubiquiti Networks", "Aggiornamento firmware UDM Pro", "Aggiornamento firmware UDM SE", "processo di aggiornamento del firmware offline", "Aggiornamento del firmware SSH", "gestione dei dispositivi di rete", "aggiornamenti di sicurezza della rete", "strategie di aggiornamento del firmware", "gestione del firmware offline", "ottimizzazione delle prestazioni della rete", "gestione delle patch di sicurezza", "aggiornamenti della tecnologia di rete"]
cover: "/img/cover/A_colorful_illustration_depicting_a_computer_connecting.png"
coverAlt: "Un'illustrazione colorata raffigurante un computer connesso a un router tramite SSH che simboleggia il processo di aggiornamento del firmware offline per i dispositivi Ubiquiti Unifi UDM Pro e UDM SE."
coverCaption: ""
---

**Aggiorna Ubiquiti Unifi UDM Pro e UDM SE offline tramite SSH**

Nel mondo del networking, **Ubiquiti Networks** ha ottenuto riconoscimenti per le sue soluzioni innovative. **Ubiquiti Unifi Dream Machine Pro (UDM Pro)** e **Unifi Dream Machine SE (UDM SE)** sono due prodotti popolari che offrono funzionalità complete di gestione della rete. L'aggiornamento del firmware di questi dispositivi è fondamentale per garantire prestazioni e sicurezza ottimali. In questo articolo, esploreremo come aggiornare il firmware di UDM Pro e UDM SE **offline** utilizzando l'SSH della riga di comando.

______

## Perché aggiornare il firmware?

Gli aggiornamenti del firmware sono essenziali per qualsiasi dispositivo di rete, poiché spesso contengono correzioni di bug, miglioramenti delle prestazioni e patch di sicurezza. L'aggiornamento regolare del firmware di UDM Pro e UDM SE è fondamentale per garantire che la rete rimanga sicura e funzioni senza problemi.

______

## Aggiornamento firmware offline

L'aggiornamento del firmware di UDM Pro e UDM SE può essere effettuato tramite **UniFi Dashboard**. Tuttavia, in alcuni scenari, una connessione Internet potrebbe non essere disponibile o desiderabile. In tali casi, un aggiornamento offline tramite SSH della riga di comando fornisce una soluzione alternativa.

______

## Preparazione per l'aggiornamento offline

Prima di procedere con l'aggiornamento offline, assicurati di avere i seguenti prerequisiti:

1. Un computer o dispositivo con un client SSH installato.
2. Il file del firmware più recente per UDM Pro o UDM SE. È possibile ottenere il file del firmware da [Ubiquiti Downloads](https://www.ui.com/download/unifi) for the [UDM Pro](https://www.ui.com/download/unifi/unifi-dream-machine-pro) page. For early access firmwares, you can see them on the [community releases page](https://community.ui.com/releases) once you've signed into your.[**ui.com**](https://account.ui.com/) account

______

## Stabilire una connessione SSH

Per aggiornare UDM Pro o UDM SE tramite SSH della riga di comando, procedi nel seguente modo:

1. Assicurati che il tuo computer o dispositivo sia connesso alla stessa rete di UDM Pro o UDM SE.
2. Apri il tuo client SSH preferito e stabilisci una connessione SSH all'indirizzo IP di **UDM Pro o UDM SE**. Ad esempio, utilizzando il **client OpenSSH** in Linux o macOS, puoi utilizzare il seguente comando:

```bash
ssh root@<UDM_IP_ADDRESS>
```

Sostituire `<UDM_IP_ADDRESS>` con l'indirizzo IP effettivo di UDM Pro o UDM SE.

3. Immettere il **nome utente** e la **password** quando richiesto. Le credenziali predefinite per i dispositivi Ubiquiti sono in genere `ubnt` sia per il nome utente che per la password.

______

## Aggiornamento del firmware

Una volta stabilita la connessione SSH, puoi procedere con l'aggiornamento del firmware:

1. Caricare il file del firmware su UDM Pro o UDM SE utilizzando **SCP (Secure Copy)**. SCP consente il trasferimento sicuro dei file tramite SSH. Supponendo che il file del firmware si trovi sul tuo computer locale, puoi utilizzare il seguente comando:

```bash
scp <FIRMWARE_FILE_PATH> ubnt@<UDM_IP_ADDRESS>:/root/fwupdate.bin
```

Sostituire `<FIRMWARE_FILE_PATH>` con il percorso del file del firmware sul computer locale e `<UDM_IP_ADDRESS>` con l'indirizzo IP di UDM Pro o UDM SE.

2. Una volta caricato il file del firmware, è possibile avviare il processo di aggiornamento del firmware. Esegui il seguente comando:

```bash
ssh ubnt@<UDM_IP_ADDRESS> "ubnt-tools fwupdate /root/fwupdate.bin"
```

3. UDM Pro o UDM SE avvierà il processo di aggiornamento del firmware. Questo potrebbe richiedere vari minuti. **Non interrompere il processo** fino al completamento dell'aggiornamento.

4. Al termine dell'aggiornamento, è possibile verificare la versione del firmware accedendo a UniFi Network Controller o eseguendo il seguente comando:

```bash
ssh ubnt@<UDM_IP_ADDRESS> "show version"
```
Si prega di notare che il processo di cui sopra presuppone che si disponga del file del firmware necessario per UDM Pro o UDM SE. Assicurati di disporre del file del firmware corretto per il modello e la versione del tuo dispositivo specifico.

## Conclusione

L'aggiornamento del firmware dei dispositivi Ubiquiti Unifi UDM Pro e UDM SE è un passaggio cruciale per garantire prestazioni e sicurezza ottimali. Mentre il controller di rete UniFi fornisce un modo conveniente per aggiornare il firmware, l'esecuzione di un aggiornamento offline tramite SSH della riga di comando offre una soluzione praticabile quando una connessione Internet non è disponibile o desiderabile.

Seguendo i passaggi descritti in questo articolo, puoi aggiornare correttamente il firmware dei tuoi dispositivi UDM Pro e UDM SE utilizzando SSH della riga di comando. Ricorda di utilizzare sempre l'ultima versione del firmware fornita da Ubiquiti Networks per sfruttare correzioni di bug, miglioramenti delle prestazioni e patch di sicurezza.

## Riferimenti

- [Ubiquiti Downloads](https://www.ui.com/download/unifi/) - Pagina ufficiale dei download di Ubiquiti per i file del firmware.
- [Unifi Advanced Updating Techniques](https://help.ui.com/hc/en-us/articles/204910064-UniFi-Upgrade-the-Firmware-of-a-UniFi-Device)
