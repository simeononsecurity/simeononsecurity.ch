---
title: "SenseCAP M1 Raspberry Pi Shield: pinout e riuso LoRaWAN"
date: 2026-09-12
lastmod: 2026-11-07
toc: true
draft: false
description: "Esamina lo shield SenseCAP M1, confronta le mappature GPIO in conflitto, controlla il chip ATECC608 e pianifica un gateway LoRaWAN con Raspberry Pi OS moderno."
genre: ["Raspberry Pi", "IoT", "Sicurezza hardware"]
tags: ["SenseCAP M1", "SenseCAP M1 shield", "SenseCAP M1 pinout", "Raspberry Pi shield", "Raspberry Pi HAT", "LoRaWAN gateway", "WM1302", "WM1303", "SX1302", "SX1303", "Seeed Studio", "Helium hotspot reuse", "LoRa concentrator", "SPI GPIO", "GPIO17", "GPIO22 LED", "libgpiod", "Raspberry Pi OS", "ATECC608", "CryptoAuthLib", "I2C diagnostics", "STTS751", "LoRa Basics Station", "ChirpStack", "The Things Stack", "hardware reverse engineering"]
cover: "/img/cover/sensecap-wm1302-shield-hardware.webp"
coverAlt: "Shield SenseCAP M1 con modulo Seeed WM1302, header Raspberry Pi, cavo antenna, presa USB-C e connettore della ventola"
coverCaption: "Foto della scheda: Clockwork Bird, 2023. La fonte e i crediti sono indicati sotto."
coverCredit: "Clockwork Bird"
coverCreditURL: "https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/"
---

**Lo shield SenseCAP M1 è un hardware utile per gateway LoRaWAN, ma il cablaggio richiede più verifiche di quelle offerte da una guida generica alle Raspberry Pi HAT.** Questa guida amplia l'indagine del [2023 di Clockwork Bird](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/) con documentazione del produttore, analisi dei driver upstream e indicazioni GPIO aggiornate. Identificherai l'hardware, distinguerai i fatti accertati dalle informazioni incomplete sul pinout e preparerai un registro ripetibile dell'avvio.

> **Ambito:** questa è una guida hardware basata sulla documentazione. Per questo articolo, i comandi e la mappatura della scheda non sono stati testati su un M1 fisico.

## Punti chiave

- **Identifica entrambe le schede:** il carrier M1 e il concentratore rimovibile hanno modelli e revisioni distinti.
- **Verifica gli script di reset:** i valori predefiniti CoreCell sono in conflitto con i segnali del pinout M1 pubblicato.
- **Controlla le interfacce del sistema:** file di dispositivo SPI, numerazione GPIO e versioni degli strumenti GPIO rispondono a domande diverse.
- **Conserva il provisioning dell'elemento sicuro:** leggere le informazioni del dispositivo è diverso dal configurarlo o generare chiavi.
- **Verifica l'intero percorso:** rilevare un concentratore non dimostra che i dati del sensore siano stati consegnati.
## Prima di iniziare

**Difficoltà: intermedia.** Dedica circa una o due ore all'inventario, alla preparazione del sistema operativo e ai controlli della documentazione. La verifica elettrica, l'adattamento del driver e la distribuzione del server di rete richiedono altro tempo, soprattutto con una revisione della scheda sconosciuta.

| Elemento | Scopo |
|---|---|
| **Shield M1 e concentratore** | Leggi la revisione del carrier e l'etichetta completa del modulo |
| **Raspberry Pi 4** | Parti dall'host usato nel progetto originale M1 |
| **Scheda microSD di riserva** | Prepara un sistema separato conservando l'installazione originale |
| **Alimentatore e antenna corretti** | Abbinali all'assemblaggio e alla banda RF del modulo |
| **SSH o console locale** | Registra la diagnostica e modifica la configurazione |
| **Sensore LoRaWAN e server** | Dopo l'avvio hardware, verifica la consegna effettiva dei dati applicativi |
| **Multimetro ed esperienza hardware** | Risolvi i collegamenti non documentati prima di pilotarli |

Fotografa entrambi i lati dell'assemblaggio senza alimentazione prima di rimuovere componenti. Annota l'orientamento dei connettori, le viti, i distanziatori e il percorso dell'antenna. Conserva la scheda e la configurazione originali finché la nuova installazione non supera i criteri di accettazione.
## Identifica i tre livelli hardware

**Il sistema M1 completo, lo shield carrier e il concentratore sono componenti distinti.** Seeed descrive l'hotspot assemblato come un Raspberry Pi 4 con un concentratore WM1302/SX1302 o WM1303/SX1303. Un annuncio intitolato "shield SenseCAP M1" non specifica quale modulo sia montato sul carrier. [Panoramica M1 di Seeed Studio](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

Il **carrier** instrada alimentazione e segnali periferici tra il Pi e il modulo. Il **concentratore** gestisce la ricezione e la trasmissione radio. Un **packet forwarder** gira sull'host e scambia con un server i pacchetti radio ricevuti e i downlink pianificati. [Panoramica Semtech SX1302 HAL](https://github.com/Lora-net/sx1302_hal)

Per esempio, un sensore di temperatura su uno scaffale invia un uplink via radio. Il concentratore lo riceve, l'host lo inoltra e i servizi di rete e applicazione lo elaborano. Un avvio riuscito di Linux dimostra solo il funzionamento della parte host.

La foto di Clockwork Bird mostra un carrier M1 v1.1 con un modulo etichettato `WM1302-SPI-EU868`. Usa la foto per individuare le etichette sul tuo hardware. I numeri seriali identificano il dispositivo fotografato, non i valori di configurazione di un altro gateway.

{{< figure src="m1-carrier-wm1302-board.webp" alt="Carrier M1 verde con modulo WM1302 SPI EU868 etichettato accanto a USB-C, pulsante, presa della ventola e cavo antenna" caption="Hardware M1 v1.1 fotografato da Clockwork Bird e usato anche come copertina dell'articolo" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Alimentazione e collegamenti radio

**Considera la presa USB-C dell'M1 come ingresso di alimentazione.** Il produttore indica 5 V CC e 3 A per il gateway completo e identifica USB-C come interfaccia di alimentazione. Chiamarla porta di ricarica suggerisce una funzione batteria assente dalle specifiche. [Specifiche SenseCAP M1](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

Lo schema a blocchi del fornitore separa l'alimentazione a 5 V dalla linea regolata a 3,3 V del modulo. La distinzione è utile nella diagnosi: un Pi acceso e un concentratore senza alimentazione sono due possibilità separate. Non applicare 5 V a un pin di segnale e non presumere che due ingressi di alimentazione siano isolati.

**Le varianti SPI e USB del modulo richiedono collegamenti host diversi.** La documentazione WM1302 di Seeed descrive accesso SPI diretto per il modello SPI e un bridge USB STM32L4 per il modello USB. La forma mini-PCIe descrive il fattore di forma, mentre le interfacce elettriche documentate sono SPI o USB. Una presa compatibile in un portatile non dimostra la compatibilità. [Documentazione WM1302 di Seeed](https://github.com/seeed-lora/WM1302-doc)

Prima di inserire il modulo, scollega l'alimentazione e collega un'antenna adatta. Abbina hardware RF, antenna e piano di rete previsto. Cambiare il nome di un file di configurazione non sostituisce i componenti RF del modulo e la presa di alimentazione M1 non dimostra il supporto di una variante USB del concentratore.

{{< figure src="m1-power-spi-system-diagram.webp" alt="Schema a blocchi che collega Raspberry Pi 4 allo shield M1 tramite alimentazione, SPI, GPIO e I2C" caption="Schema del produttore SenseCAP riprodotto nell'articolo originale di Clockwork Bird, con il progetto WM1302" credit="Seeed Studio / SenseCAP, via Clockwork Bird" attr="Seeed Studio / SenseCAP, via Clockwork Bird" attrlink="https://www.sensecapmx.com/docs/sensecap-m1/overview/" >}}

## Leggi con attenzione il pinout

**Annota i numeri BCM GPIO e i numeri dei pin fisici in colonne separate.** Per esempio, BCM GPIO17 corrisponde al pin fisico 11 dell'header Pi. Il connettore edge del modulo usa un terzo sistema di numerazione: il numero del suo pin di reset non è un numero GPIO del Raspberry Pi.

La tabella trascrive i collegamenti dall'immagine annotata dell'header di Clockwork Bird. È un **riferimento della comunità**, non uno schema completo del produttore né una misura di ogni revisione M1. Il disegno usa anche le etichette `SX1262`, mentre lo script reset generico di Semtech usa nomi `SX1261`.

| Segnale nel disegno | BCM / pin fisico | Interpretazione |
|---|---|---|
| **I2C SDA / SCL** | GPIO2 / 3, GPIO3 / 5 | Bus di gestione condiviso |
| **Reset SX1302** | GPIO17 / 11 | Candidato per il reset del concentratore |
| **LED utente** | GPIO22 / 15 | Indicazione M1 |
| **SPI MOSI / MISO** | GPIO10 / 19, GPIO9 / 21 | Segnali dati SPI |
| **Clock SPI** | GPIO11 / 23 | Segnale di clock SPI |
| **Chip select SX1302** | GPIO8 / 24 | SPI0 CE0 |
| **Reset SX1262** | GPIO5 / 29 | Candidato per il reset della radio ausiliaria |
| **Chip select SX1262** | GPIO6 / 31 | GPIO6, distinto da SPI0 CE1 |
| **SX1262 BUSY** | GPIO18 / 12 | Uscita di stato della radio ausiliaria |
| **SX1262 IO1 / IO2** | GPIO23 / 16, GPIO24 / 18 | Segnali ausiliari, da verificare prima dell'uso |

Le annotazioni GPS/UART barrate non dimostrano che un M1 includa il GPS. Escludi la configurazione GPS a meno che il tuo hardware non offra questa funzione. Il diagramma pubblicato non chiarisce nemmeno il pulsante utente e il controllo della ventola. [Indagine sul pinout di Clockwork Bird](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)

{{< figure src="m1-community-header-pinout.webp" alt="Disegno annotato dell'header Raspberry Pi con LED M1, reset del concentratore, segnali SPI e collegamenti GPS barrati" caption="Riferimento della comunità senza copertura verificata di tutte le revisioni, non è uno schema M1 completo" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Risolvi i conflitti negli script di reset

**Uno script di reset seleziona uscite elettriche, non semplici preferenze software.** Il file upstream `reset_lgw.sh` di Semtech è destinato al progetto di riferimento CoreCell. I valori predefiniti includono GPIO23 per il reset del concentratore, GPIO18 per l'abilitazione dell'alimentazione, GPIO22 per un reset ausiliario e GPIO13 per il reset di AD5338R. [Codice dello script reset Semtech](https://github.com/Lora-net/sx1302_hal/blob/master/tools/reset_lgw.sh)

Le istruzioni di installazione meno recenti di Seeed modificano le due assegnazioni di reset in GPIO17 e GPIO5, ma mantengono le altre voci del progetto di riferimento. Prima di seguire l'esempio, confronta quei valori con l'immagine M1 annotata. [Istruzioni di configurazione WM1302 di Seeed](https://github.com/seeed-lora/WM1302-doc)

| Assegnazione | Indicazione in conflitto | Decisione richiesta |
|---|---|---|
| **GPIO22 come reset ausiliario** | L'immagine M1 lo indica come LED utente | Rimuovi questa ipotesi prima di abilitare il LED |
| **GPIO18 come abilitazione alimentazione** | L'immagine M1 lo indica come BUSY ausiliario | Verifica collegamento e direzione prima di pilotarlo |
| **GPIO13 come reset DAC** | Lo script generico nomina un altro progetto di riferimento | Accerta se il circuito è presente |
| **Dispositivo SPI ausiliario** | L'immagine M1 seleziona GPIO6 invece di CE1 | Conferma il cablaggio del chip select e il supporto del driver |

**Deduzione:** se GPIO18 è collegato a un'uscita della radio ausiliaria come nel disegno, configurarlo come uscita sul lato Pi crea un rischio di conflitto elettrico. La divergenza richiede una verifica, ma non dimostra un danno né un cablaggio universale per ogni M1.

Con tutta l'alimentazione scollegata, traccia i collegamenti accessibili tra header e connettore del modulo. Annota la revisione della scheda e i due estremi di ogni collegamento. Una misura di continuità conferma la connessione, mentre la documentazione del componente stabilisce direzione del segnale e limiti elettrici.

Usa lo schema del modulo del produttore riportato sotto per non confondere i pin edge con quelli dell'header Pi. Le etichette della radio ausiliaria descrivono il riferimento pubblicato del modulo e non dimostrano che ogni revisione abbia gli stessi chip o funzioni. [Pinout del modulo WM1302 di Seeed](https://github.com/seeed-lora/WM1302-doc/blob/master/pinout.jpg)

{{< figure src="wm1302-module-edge-connector.webp" alt="Disegno Seeed con entrambi i lati del connettore edge WM1302 e segnali di alimentazione, SPI, I2C e radio ausiliaria" caption="La numerazione del connettore edge del modulo è diversa da quella dell'header Raspberry Pi" credit="Seeed Studio" attr="Seeed Studio, WM1302-doc" attrlink="https://github.com/seeed-lora/WM1302-doc" >}}

## Prepara Raspberry Pi OS

Registra l'ambiente host sull'installazione di riserva:

```bash
cat /etc/os-release
uname -r
tr -d '\0' < /proc/device-tree/model
```

La versione del sistema operativo, il kernel e il modello Pi costituiscono il punto di partenza per la riproducibilità. Annotali prima di confrontare i risultati con una guida più vecchia.

Installa gli strumenti di ispezione e compilazione:

```bash
sudo apt update
sudo apt install git build-essential i2c-tools gpiod
sudo raspi-config
```

In **Interface Options**, abilita SPI e I2C, quindi riavvia. SPI serve il percorso del concentratore, mentre I2C serve i dispositivi di gestione descritti sotto. Evita di copiare da un'altra guida HAT modifiche non pertinenti alle porte seriali GPS.

Ispeziona le interfacce esposte:

```bash
ls -l /dev/spidev* /dev/i2c-*
i2cdetect -l
gpiodetect
gpioinfo
gpioset --version
```

Questi comandi elencano file di dispositivo, adattatori, controller GPIO, informazioni sulle linee e versione dello strumento GPIO installato. **`i2cdetect -l` elenca gli adattatori senza eseguire scansioni degli indirizzi dei dispositivi.** Un file `/dev/spidev0.0` dimostra che è esposta un'interfaccia SPI, non che comunichi con un concentratore funzionante. [Manuale i2c-tools](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), [Indicazioni GPIO Raspberry Pi](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

### Tieni conto delle versioni GPIO

**Non copiare numeri GPIO globali da un'altra macchina.** Gli script vecchi scrivono tramite `/sys/class/gpio`, un'interfaccia che il kernel documenta come deprecata. Le nuove integrazioni userspace dovrebbero usare l'interfaccia dei dispositivi a caratteri GPIO con il controller e l'offset di linea corretti. [Documentazione GPIO Linux](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html)

Controlla anche `gpioset --help` prima di adattare uno script. La versione 1 e la versione 2 differiscono per sintassi e comportamento dei processi. Lo strumento attuale mantiene per impostazione predefinita le linee richieste, ma il contratto portabile non ne garantisce lo stato dopo l'uscita del processo. [Documentazione gpioset libgpiod](https://libgpiod.readthedocs.io/en/master/gpioset.html)

Raspberry Pi documenta un comportamento del kernel che mantiene lo stato delle uscite, con opzioni per modificarlo. Registra la configurazione effettiva del kernel invece di presumere che ogni sistema Linux si comporti allo stesso modo. Una numerazione aggiornata o uno strumento GPIO recente non risolvono una mappatura elettrica errata. [Guida all'uso GPIO Raspberry Pi](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)
## Verifica il LED utente

Dopo aver verificato che GPIO22 appartenga al LED e aver rimosso i dispositivi in conflitto su questa linea, modifica la configurazione di avvio:

```bash
sudoedit /boot/firmware/config.txt
```

Le versioni moderne di Raspberry Pi OS montano la configurazione di avvio in **`/boot/firmware/config.txt`**. Le immagini più vecchie usano `/boot/config.txt`, il percorso dell'articolo del 2023. Prima di modificare il file attivo, fanne una copia. [Documentazione config.txt Raspberry Pi](https://www.raspberrypi.com/documentation/computers/config_txt.html)

Aggiungi l'overlay LED in una sezione valida per il tuo Pi, per esempio `[all]`:

```ini
dtoverlay=gpio-led,gpio=22,label=lorawan,trigger=heartbeat
```

Il parametro **`gpio`** usa la numerazione BCM. **`label`** assegna un nome al dispositivo LED Linux e **`trigger=heartbeat`** imposta il trigger heartbeat del kernel. Clockwork Bird riporta questa assegnazione per l'M1 e il riferimento degli overlay Raspberry Pi documenta i parametri. [Osservazione originale sul LED](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), [Riferimento overlay gpio-led](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README)

Dopo il riavvio, controlla il LED registrato:

```bash
ls -l /sys/class/leds/
cat /sys/class/leds/lorawan/trigger
```

Il risultato previsto è un elemento LED `lorawan` con `heartbeat` tra parentesi quadre. Un LED lampeggiante dimostra questo percorso GPIO/driver. Non indica una registrazione LoRaWAN riuscita, ricezione radio o stato Helium.
## Analizza i dispositivi I2C

**Un indirizzo I2C è un indizio, non l'identità di un dispositivo.** Clockwork Bird ha osservato risposte agli indirizzi `0x60` e `0x39`, poi ha letto informazioni ATECC608 tramite la libreria crittografica. Nell'articolo originale l'identificazione del sensore di temperatura è rimasta incerta.

Inizia dall'elenco degli adattatori della sezione precedente. Le scansioni estese di `i2cdetect` inviano transazioni di probing invece di osservare passivamente il traffico e il manuale upstream avverte del rischio di interruzioni. Evita scansioni di routine su un gateway in funzione o su dispositivi collegati sconosciuti. [Comportamento di probing di i2c-tools](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8)

| Osservazione | Conclusione supportata | Domanda aperta |
|---|---|---|
| **Risposta a `0x60`** | Qualcosa ha riconosciuto il probe | È l'elemento sicuro atteso? |
| **Risposta a `0x39`** | Qualcosa ha riconosciuto il probe | Quale componente e revisione hanno risposto? |
| **`UU` in una scansione** | Un driver possiede l'indirizzo e il probing è stato saltato | Quale driver lo possiede? |
| **Nessuna risposta** | Il probe non ha ricevuto conferma | Alimentazione, bus, proprietario o protocollo del dispositivo? |

### Un indizio più solido per il sensore di temperatura

**Le fonti indicano STTS751 come candidato per `0x39`.** L'header del driver di temperatura Semtech associa esplicitamente `0x39` a `STTS751-0DP3F`. Questo rafforza l'ipotesi originale, ma non identifica ogni scheda popolata su questo indirizzo. [Header del driver STTS751 Semtech](https://github.com/Lora-net/sx1302_hal/blob/master/libloragw/inc/loragw_stts751.h)

Dopo aver identificato un componente compatibile e aver verificato che nessun altro processo lo usi, leggi i suoi registri di identificazione:

```bash
sudo i2cget 1 0x39 0xfd b
sudo i2cget 1 0x39 0xfe b
```

Qui **`1`** seleziona il bus verificato, **`0x39`** il dispositivo e **`b`** richiede una lettura byte-data SMBus. Per un STTS751-0, l'ID prodotto documentato a `0xFD` è `0x00` e l'ID produttore a `0xFE` è `0x53`. Le transazioni selezionano gli indirizzi dei registri ma non scrivono valori di configurazione. [Datasheet STTS751, mappa dei registri e registri identificativi](https://www.st.com/resource/en/datasheet/stts751.pdf)

Confronta le letture con la marcatura del chip e la documentazione. Una coppia corrispondente aggiunge prove a favore dell'identificazione; in caso di errore, controlla bus e proprietà prima di modificare la configurazione hardware. Il sensore misura la temperatura locale, diversa da quella della CPU del Pi.
## Ispeziona l'elemento sicuro

**ATECC608 è un componente di autenticazione separato.** Considera configurazione, numero seriale, chiave pubblica e materiale delle chiavi protette come concetti distinti. La lettura di una chiave pubblica non rivela la chiave privata corrispondente.

**CryptoAuthLib** di Microchip fornisce l'interfaccia del dispositivo. Il repository **cryptoauthtools** contiene esempi basati sulla libreria. Segui le istruzioni dei progetti per preparare la libreria nativa e i binding Python sul sistema di destinazione prima di eseguire un esempio. Installare un pacchetto Python non correlato o copiare un solo script non dimostra che il backend I2C funzioni. [CryptoAuthLib Microchip](https://github.com/MicrochipTech/cryptoauthlib), [cryptoauthtools Microchip](https://github.com/MicrochipTech/cryptoauthtools)

Da una directory `cryptoauthtools/python/examples` preparata, esegui il comando di ispezione dell'articolo originale:

```bash
sudo python3 info.py -i i2c
```

L'argomento **`-i i2c`** seleziona l'interfaccia. In un ambiente virtuale, usa l'interprete Python esplicito dell'ambiente e verifica che trovi la libreria nativa corrispondente. In molte installazioni `sudo python3` seleziona l'interprete di sistema, spiegando alcuni errori di importazione dei moduli.

Il file `info.py` esaminato legge informazioni sulla revisione, numero seriale, configurazione e stato del blocco. Se la zona dati è bloccata, tenta di recuperare la chiave pubblica dallo slot 0. Non esegue la sequenza di provisioning dell'esempio. Un errore di lettura della chiave pubblica dallo slot 0 non dimostra da solo un guasto del dispositivo. [Codice sorgente info.py Microchip](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/info.py)

| Output o operazione | Significato |
|---|---|
| **Configurazione bloccata** | Sono attive restrizioni di configurazione |
| **Zona dati bloccata** | Interpreta l'accesso in base alle policy degli slot configurate |
| **Chiave pubblica visualizzata** | Sono state recuperate informazioni pubbliche, non esportata una chiave privata |
| **Esecuzione di `config.py`** | Esempio di provisioning con operazioni di configurazione, blocco e generazione chiavi |

**Non eseguire `config.py` per correggere un errore di ispezione.** Il codice include scritture di configurazione, chiamate per bloccare le zone e generazione di chiavi. Il percorso predefinito di generazione delle chiavi è importante anche su un dispositivo già configurato. [Codice sorgente config.py Microchip](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/config.py)

I profili di provisioning documentati da Microchip mostrano perché una zona dati bloccata non implica autorizzazioni identiche per ogni slot. Questi profili non stabiliscono la configurazione esatta dell'M1. Conserva la configurazione esistente e consulta la documentazione del componente corretto prima di pianificare il riutilizzo delle chiavi. [Policy di accesso agli slot e alla memoria Microchip](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html)
## Gestisci le incertezze su ventola e pulsante

**Una presa per ventola a tre pin non ne determina tensione, polarità o metodo di controllo.** Fotografa la numerazione dei pin e leggi l'etichetta della ventola. Verifica alimentazione e segnali di controllo prima di collegare un ricambio o scegliere un overlay GPIO.

Anche il GPIO del pulsante resta ignoto nell'indagine originale. Cerca un driver o una configurazione legata alla revisione della tua scheda, poi verifica i collegamenti con l'alimentazione scollegata. Non configurare come uscite tutti i GPIO apparentemente liberi per trovare il pulsante.

| Periferica | Prove da raccogliere | Criterio di accettazione |
|---|---|---|
| **Alimentazione della ventola** | Valori nominali della ventola, massa e alimentazione del connettore | La tensione misurata corrisponde alle specifiche della ventola |
| **Controllo della ventola** | Driver/configurazione o circuito di controllo tracciato | Comportamento definito all'avvio e ad alta temperatura |
| **Pulsante utente** | Cablaggio dei contatti, mappatura GPIO, polarità d'ingresso | Una pressione intenzionale genera l'evento previsto |

Una nuova installazione del sistema operativo non ripristina automaticamente la policy di raffreddamento dell'apparato originale. Durante il primo test prolungato, osserva insieme funzionamento della ventola e temperature. Mantieni il percorso del flusso d'aria del contenitore e interrompi il test se l'assemblaggio perde il raffreddamento necessario.
## Scegli uno stack gateway

**Separa il supporto della scheda dal protocollo del server.** Un server LoRaWAN compatibile non corregge una sequenza di reset errata o una calibrazione RF sbagliata. Scegli prima software compatibile con il concentratore, i collegamenti del carrier, il sistema operativo e la configurazione regionale.

| Percorso software | Ruolo utile | Verifica prima della distribuzione |
|---|---|---|
| **Semtech SX1302 HAL** | Avvio a livello sorgente e strumenti diagnostici | Procedura di reset della scheda e configurazione del modulo |
| **LoRa Basics Station** | Connessione gateway autenticata a un server | Integrazione funzionante della scheda e credenziali del server |
| **ChirpStack Concentratord** | Servizio dedicato al concentratore | Modello supportato, calibrazione e mappatura GPIO |

ChirpStack elenca il modello SPI **`seeed_wm1302`**. Questo prova il supporto del modulo, non garantisce un'immagine M1 completa né il supporto di ogni revisione M1. Non trattare le istruzioni di installazione separate per SenseCAP M2 come istruzioni firmware M1. [Supporto hardware ChirpStack](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html), [Destinazione d'installazione Seeed di ChirpStack](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html)

Per The Things Stack, la documentazione consiglia **LoRa Basics Station** al posto del forwarder UDP legacy di Semtech. Station fornisce TLS e autenticazione basata su token insieme a funzioni di configurazione centralizzata. Gli esempi UDP aiutano a comprendere l'inoltro dei pacchetti, ma le impostazioni dell'indirizzo server non offrono queste protezioni. [Indicazioni UDP di The Things Stack](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [Documentazione LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/)

### Prepara gli strumenti upstream

Compila sul Pi di destinazione in una nuova directory di lavoro:

```bash
git clone https://github.com/Lora-net/sx1302_hal.git
cd sx1302_hal
git rev-parse HEAD
make
```

Salva l'identificatore del commit insieme all'output di compilazione. Una build completata dimostra la compatibilità del compilatore, ma la radio richiede comunque un'implementazione di reset verificata e una configurazione corretta. La documentazione Semtech spiega il ruolo della HAL e dei programmi ausiliari. [Documentazione build e strumenti SX1302 HAL](https://github.com/Lora-net/sx1302_hal)

Esamina il file di reset prima di avviare strumenti che accedono all'hardware:

```bash
sed -n '1,180p' tools/reset_lgw.sh
```

Non copiare questo file senza modifiche nella directory runtime. Semtech documenta l'uso automatico dello script di reset nei programmi di accesso all'hardware, inclusi strumenti di identificazione. Verifica ogni pin assegnato, direzione del segnale, API GPIO e stato all'avvio e all'arresto.

Dopo la verifica della scheda, segui le istruzioni dello stack scelto per leggere l'EUI del concentratore e registrare il gateway. Conserva calibrazione e impostazioni RF del modulo quando aggiungi la configurazione server. Nella configurazione UDP Semtech, `gateway_ID` rappresenta l'EUI, mentre il Gateway ID nella console The Things Stack è l'identificatore leggibile della registrazione. [Configurazione gateway The Things Stack](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/)
## Dimostra la consegna dei dati del sensore

**Usa prove per fasi per individuare il primo livello che non funziona.** Un gateway segnato online dimostra una connessione al server. Il test di accettazione richiede anche un sensore noto, un piano di frequenza compatibile e un payload applicativo decodificato.

La sequenza seguente è un piano di test proposto, non un risultato M1 misurato:

| Punto di controllo | Prova da salvare | Significato |
|---|---|---|
| **Host pronto** | Sistema operativo, kernel, alimentazione e inventario delle interfacce | Preparazione Linux completata |
| **Concentratore risponde** | EUI e log d'inizializzazione riuscito | Comunicazione host-concentratore funzionante |
| **La radio riceve** | Pacchetto del sensore previsto e metadati di ricezione | Percorso di ricezione configurato funzionante |
| **Il server accetta** | Evento gateway associato al sensore | Inoltro e routing del server funzionanti |
| **L'applicazione decodifica** | Misura prevista e timestamp | Percorso applicativo funzionante |
| **Ripristino dopo il riavvio** | Le stesse verifiche dopo il riavvio | Configurazione di avvio ripetibile |

Per un sensore **OTAA**, conferma anche lo scambio di attivazione e l'uplink successivo. OTAA significa attivazione over-the-air, la procedura di join che stabilisce una sessione. La sola ricezione di una richiesta di join non dimostra un join riuscito o un percorso downlink. [Documentazione di attivazione The Things Stack](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/)

**Esempio di diagnosi:** il gateway si connette al server e segnala il suo EUI, ma il sensore non appare. Dai priorità alla configurazione di trasmissione del sensore, ai canali di ricezione selezionati, al percorso dell'antenna e ai log radio. Riprogrammare ATECC608 non colma la mancanza di prove in questo scenario.

**Seconda diagnosi:** un pacchetto sensore appare localmente ma non raggiunge l'applicazione. Correlane l'orario con gli eventi del gateway e del server, poi verifica routing, registrazione del dispositivo e decodifica. Un pacchetto RF nel log non basta per accusare il decoder del payload finché il server non ha accettato l'evento.
## Risolvi i problemi in base al sintomo

| Sintomo | Controlla per primo | Azione successiva |
|---|---|---|
| **File dispositivo SPI assente** | Configurazione di avvio attiva e impostazioni dell'interfaccia | Abilita l'interfaccia prevista e riavvia |
| **SPI presente, radio non funziona** | Alimentazione, inserimento, sequenza di reset e chip select | Verifica il percorso elettrico prima di modificare il server |
| **Errore di esportazione GPIO** | Ipotesi legacy su sysfs e kernel installato | Usa un'implementazione verificata per l'API GPIO |
| **GPIO già in uso** | Processo indicato da `gpioinfo` | Risolvi il conflitto di proprietà prima di riprovare |
| **LED non funziona dopo la configurazione** | Applicazione dell'overlay e conflitti GPIO22 | Esamina LED registrati e script di reset |
| **Dispositivo I2C assente** | Numero del bus, alimentazione e proprietario corrente | Indaga senza ripetere scansioni estese |
| **Import della libreria crittografica fallito** | Interprete, binding e percorso della libreria nativa | Correggi l'ambiente software |
| **Lettura della chiave pubblica fallita** | Policy dello slot e letture precedenti riuscite | Esamina la configurazione senza provisioning |
| **La ventola non gira** | Alimentazione verificata e implementazione del raffreddamento | Ripristina il raffreddamento corretto prima di test prolungati |
| **Uplink ricevuti, join non riuscito** | Percorso downlink e impostazioni regionali/dispositivo | Traccia la risposta al join e le finestre di ricezione |

Considera ogni correzione un singolo esperimento. Salva la configurazione precedente, cambia una variabile, ripeti lo stesso controllo e registra se sono emerse le prove previste.
## Crea un registro dell'hardware

Usa questo modello per rendere ripetibile il passaggio di consegne:

```text
Carrier revision and photographs:
Concentrator model, interface and RF band:
Host model / OS / kernel / GPIO tool version:
Supply / antenna / cooling arrangement:
Verified pin mapping and evidence:
Unresolved nets and excluded features:
Software repository and commit:
Reset implementation and GPIO ownership:
Gateway EUI / server / frequency plan:
Sensor activation and decoded uplink evidence:
Reboot recovery result:
Original-card location and rollback procedure:
```

**Esercizio decisionale:** puoi acquistare un carrier economico senza etichetta del modulo oppure un assemblaggio più costoso con etichette leggibili e funzionamento documentato. Scegli l'opzione adatta al tuo progetto includendo nel confronto Pi, concentratore, antenna, alimentazione e tempo di verifica mancanti. La scelta migliore dipende dal costo totale e dalle prove necessarie per il servizio previsto, non solo dal prezzo pubblicizzato del carrier.

**Ragionamento atteso:** un progetto didattico tollera cablaggi non risolti se hai strumenti di misura e tempo. Un gateway per sensori operativi richiede avvio ripetibile, raffreddamento, supporto software e consegna dimostrata dei dati. Registra quale condizione irrisolta fermerebbe la distribuzione.
## Passi successivi

Inizia completando il registro hardware e risolvendo le discrepanze negli script di reset. Poi avvia un sensore noto e salva le prove fino alla decodifica applicativa prima di aggiungere altri dispositivi.

**Registro di accettazione:** salva revisione della scheda, etichetta del modulo, banda radio, misura dell'alimentazione, dispositivo SPI attivo, nomi delle linee GPIO, sequenza di reset, log del concentratore, connessione al server e un uplink decodificato. Contrassegna ogni valore come osservato, documentato o ancora presunto. L'avvio di un processo non dimostra le prestazioni RF né la consegna all'applicazione.

Se il tuo obiettivo è la messaggistica mesh, confronta prima i ruoli dei protocolli nella nostra [guida a Meshtastic, MeshCore e Reticulum](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/). Condividere la tecnologia radio LoRa non dimostra la compatibilità firmware. Per una distribuzione di messaggistica, consulta la [documentazione sull'hardware supportato da MeshtasticD](https://meshtastic.org/docs/meshtasticd/) invece di considerare questa procedura LoRaWAN una conversione a Meshtastic.
## Fonti e crediti delle immagini

La ricerca è stata verificata il 12 settembre 2026. I collegamenti non datati alla documentazione e ai repository si riferiscono alle versioni consultate per questo articolo. Le figure locali mantengono le etichette originali e la provenienza attribuita.

| Editore | Fonte e data |
|---|---|
| **Clockwork Bird** | [SenseCAP M1 Raspberry Pi Shield](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), 2023-05-03. Foto della scheda, header annotato e schema a blocchi del produttore riprodotto |
| **Seeed Studio / SenseCAP** | [Panoramica e specifiche M1](https://www.sensecapmx.com/docs/sensecap-m1/overview/), senza data. Attribuzione originale dello schema a blocchi |
| **Seeed Studio** | [Documentazione WM1302 e pinout del modulo](https://github.com/seeed-lora/WM1302-doc), repository |
| **Semtech** | [SX1302/SX1303 HAL](https://github.com/Lora-net/sx1302_hal), incluse le fonti collegate per lo script di reset e il driver di temperatura |
| **Raspberry Pi** | [Configurazione di avvio](https://www.raspberrypi.com/documentation/computers/config_txt.html), [guida GPIO](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices) e [riferimento overlay](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README) |
| **Linux / libgpiod** | [Interfaccia GPIO sysfs deprecata](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html) e [manuale gpioset](https://libgpiod.readthedocs.io/en/master/gpioset.html), quest'ultimo datato agosto 2026 |
| **i2c-tools** | [Manuale i2cdetect](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), sorgente v4.3 |
| **STMicroelectronics** | [Datasheet STTS751](https://www.st.com/resource/en/datasheet/stts751.pdf), revisione 7 |
| **Microchip** | [CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib), [cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools) e [documentazione delle policy di accesso agli slot](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html) |
| **ChirpStack** | [Supporto hardware Concentratord](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html) e [destinazione d'installazione Seeed](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html) |
| **The Things Industries** | [Forwarder UDP](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/) e [attivazione dei dispositivi](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/) |
| **Meshtastic** | [Documentazione MeshtasticD](https://meshtastic.org/docs/meshtasticd/), senza data |
