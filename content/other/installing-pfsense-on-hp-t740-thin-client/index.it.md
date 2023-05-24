---
title: "Esecuzione di pfSense sul thin client HP t740: suggerimenti e guida alla risoluzione dei problemi"
draft: false
toc: true
date: 2023-04-29
description: "Scopri come configurare pfSense sul thin client HP t740 e come risolvere potenziali problemi come il blocco e i problemi di rilevamento SSD."
tags: ["pfSense", "OPNsense", "HardenedBSD", "HP t740", "cliente sottile", "server domestico", "PPPoE", "FreeBSD", "richiesta di avvio", "loader.conf.local", "editor nano", "Rilevamento SSD", "SSD M.2", "digitale occidentale", "Risoluzione dei problemi", "post installazione", "UART", "ESXi", "Proxmox"]
cover: "/img/cover/A_cartoon_of_a_wizard_casting_a_spell_to_fix_a_frozen_computer.png"
coverAlt: "Un cartone animato di un mago che lancia un incantesimo per riparare un computer bloccato, con un fumetto che dice Problema risolto"
coverCaption: ""
---
 pfSense, OPNsense o HardenedBSD sul thin client HP t740**

Se stai cercando un dispositivo potente per eseguire pfSense, OPNsense o HardenedBSD, il thin client HP t740 potrebbe essere la scelta giusta per te.

## Più potenza e un server domestico compatto

HP t740 Thin Client è un dispositivo compatto che può essere utilizzato come un potente box pfSense o un server domestico compatto. Offre più potenza rispetto al t730 o al t620 Plus, il che lo rende una scelta adatta per l'esecuzione di PPPoE, soprattutto se si dispone di Internet in fibra. Può anche offrire un percorso di aggiornamento alla rete 10 Gigabit.

## PS/2 si blocca

Tuttavia, se prevedi di eseguire FreeBSD o i suoi derivati come pfSense, OPNsense o HardenedBSD sul bare metal (anziché all'interno di ESXi o Proxmox), potresti riscontrare un problema per cui il sistema si blocca all'avvio con il messaggio `atkbd0: [GIANT-LOCKED]` Fortunatamente, questo problema può essere risolto immettendo i seguenti comandi al prompt di avvio:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

*Nota che devi disimpostare entrambi, altrimenti si bloccherà comunque all'avvio.*

Dopo aver installato il sistema operativo, apri una shell di post-installazione ed esegui il seguente comando:

```bash
vi /boot/loader.conf.local
```
Quindi, aggiungi queste due righe:
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

### Mantieni le modifiche usando VI
Per chi non ha familiarità con vi, è possibile aggiungere la riga procedendo come segue:

Aggiunta delle linee `hint.uart.0.disabled="1"` E `hint.uart.1.disabled="1"` al `/boot/loader.conf.local` file utilizzando l'editor vi può essere eseguito con i seguenti passaggi:

1. Apri il terminale sul tuo sistema FreeBSD.

2. Digitare `vi /boot/loader.conf.local` e premi Invio per aprire il file nell'editor vi.

3. Premere il `i` tasto per accedere alla modalità di inserimento.

4. Spostare il cursore in fondo al file utilizzando i tasti freccia.

5. Digitare `hint.uart.0.disabled="1"` senza le virgolette.

6. Premere Invio per iniziare una nuova riga.

7. Digitare `hint.uart.1.disabled="1"` senza le virgolette.

8. Premere il `Esc` tasto per uscire dalla modalità di inserimento.

9. Digitare `:wq` e premi Invio per salvare e uscire dal file.

Questo aggiungerà le due righe al file `/boot/loader.conf.local` file, che disabiliterà gli UART e risolverà il problema di blocco durante l'avvio su alcuni dispositivi HP t740 "Thin Client" durante l'esecuzione di FreeBSD o dei suoi derivati come pfSense, OPNsense o HardenedBSD.

Questo risolverà il problema durante i riavvii e gli aggiornamenti del firmware su pfSense/OPNsense.

##SSD

Se stai utilizzando HP M.2 eMMC, non verrà rilevato su un'installazione di FreeBSD pronta all'uso. In tal caso, avrai bisogno di un SSD M.2 di terze parti. Qualsiasi SSD M.2 può funzionare, SATA o NVMe.

Se stai cercando un SSD M.2 di terze parti per il tuo thin client HP t740, ti consigliamo di considerare il [Western Digital 500GB WD Blue SN570 NVMe](https://amzn.to/44bFCBk) or the [Western Digital 500GB WD Blue SA510 SATA](https://amzn.to/3AEbd0V) Entrambe queste opzioni sono affidabili e dovrebbero funzionare bene con il tuo dispositivo. Se vuoi sfruttare entrambi gli slot, avrai bisogno di entrambi. Sacrificherai le velocità di NVME, ma otterrai una ridondanza che è davvero importante.

Si noti che l'autore di questo articolo ha eseguito correttamente pfSense CE 2.5.2 e OPNsense 22.1 sul proprio t740 senza problemi dopo aver seguito i passaggi precedenti.

## Risoluzione dei problemi e post installazione

Dopo l'installazione, se riscontri problemi con la modifica dei file, puoi installare l'editor nano utilizzando `pkg update` E `pkg install nano` Questo ti aiuterà a modificare facilmente i file di testo.

Per garantire che le modifiche apportate al file `/boot/loader.conf.local` file persiste tra gli aggiornamenti della versione di pfSense, è necessario aggiungere le seguenti righe a `/boot/loader.conf` E `/etc/rc.conf.local` 
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

Tuttavia, a volte la modifica di `/boot/loader.conf.local` file prima del riavvio non risolve il problema. In tali casi, potrebbe essere necessario aggiungere le seguenti righe all'inizio del primo avvio:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

Questi passaggi dovrebbero risolvere la maggior parte dei problemi che possono sorgere durante e dopo il processo di installazione.

### Riferimenti:
- [HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
- [pfSense](https://www.pfsense.org/)
- [OPNsense](https://opnsense.org/)
- [HardenedBSD](https://hardenedbsd.org/)
- [ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
- [FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)