---
title: "Guida Definitiva: Installare GrapheneOS sul tuo Google Pixel"
draft: false
toc: true
date: 2023-05-21
lastmod: 2026-05-24
description: "Scopri come installare GrapheneOS sul tuo Google Pixel per una maggiore privacy e sicurezza usando il programma di installazione web o il metodo da riga di comando."
tags: ["GrapheneOS", "Google Pixel", "privacy", "sicurezza", "Android", "dispositivi mobili", "sistema operativo", "guida all'installazione", "ROM personalizzata", "orientato alla privacy", "protezione dei dati", "OS sicuro", "open source", "sicurezza del dispositivo", "funzionalità di privacy", "dati personali", "privacy mobile", "privacy digitale", "personalizzazione del dispositivo", "tecnologia", "fastboot", "bootloader", "verified boot", "Pixel 10", "Pixel 9"]
cover: "/img/cover/how-to-install-graphine-os.webp"
coverAlt: "Un'illustrazione digitale astratta che mostra uno smartphone Google Pixel collegato a un computer tramite cavo USB-C, circondato da elementi grafici che rappresentano il trasferimento di dati e la sicurezza."
coverCaption: ""
---

**Come installare GrapheneOS sul tuo Google Pixel**

GrapheneOS è un sistema operativo open source incentrato sulla privacy basato su Android. Offre un hardening della sicurezza e protezioni della privacy significativamente migliorati, rendendolo un'eccellente scelta per chiunque sia preoccupato per la privacy e la sicurezza dei dati. Se possiedi un dispositivo Google Pixel supportato e vuoi passare a GrapheneOS, questa guida copre sia il metodo **programma di installazione web** consigliato sia il tradizionale metodo da **riga di comando (CLI)**.

> **Suggerimento:** Se hai problemi con il processo di installazione, chiedi aiuto sul [canale chat ufficiale di GrapheneOS](https://grapheneos.org/contact#community). Prima di chiedere aiuto, prova a seguire la guida da solo e poi chiedi aiuto per ciò in cui sei bloccato.

## Prerequisiti

### Requisiti hardware e di sistema

- Un computer con almeno **2 GB di memoria libera** e **32 GB di spazio di archiviazione libero**.
- Un **cavo USB-C di alta qualità** incluso con il dispositivo (o un cavo USB-C/USB-A se necessario). Evita gli hub USB — collega direttamente a una porta posteriore del desktop o a una porta del laptop.
- L'installazione da una macchina virtuale **non è consigliata** a causa del passthrough USB inaffidabile.

> È buona pratica aggiornare il tuo dispositivo Pixel prima di installare GrapheneOS per avere il firmware più recente. In ogni caso, GrapheneOS esegue il flash del firmware più recente all'inizio del processo di installazione.

### Sistemi operativi ufficialmente supportati

#### Programma di installazione web

- Windows 10 / Windows 11
- macOS Sonoma (14), macOS Sequoia (15), macOS Tahoe (26)
- Arch Linux
- Debian 12 (bookworm), Debian 13 (trixie)
- Ubuntu 22.04 LTS, Ubuntu 24.04 LTS, Ubuntu 25.04
- Linux Mint 21 (seguire le istruzioni di Ubuntu 22.04 LTS), Linux Mint 22 (seguire le istruzioni di Ubuntu 24.04 LTS)
- Linux Mint Debian Edition 6 (seguire le istruzioni di Debian 12)
- ChromeOS
- GrapheneOS
- Android 13, 14, 15 e 16 con certificazione Play Protect

#### Metodo CLI

Tutti i precedenti eccetto ChromeOS, GrapheneOS e Android (che possono usare solo il programma di installazione web).

Le versioni più vecchie e a fine vita di queste piattaforme possono anche essere usate ma non sono ufficialmente supportate. **Assicurati che il tuo sistema operativo sia aggiornato prima di procedere.**

### Browser ufficialmente supportati (solo programma di installazione web)

- **Chromium** (fuori da Ubuntu — il loro pacchetto Snap manca di WebUSB funzionante)
- **Vanadium** (GrapheneOS)
- **Google Chrome**
- **Microsoft Edge**
- **Brave** (con Brave Shields disabilitato — limita l'uso dello storage per evitare il fingerprinting)

> - Su Android, **disabilita la modalità desktop** nel tuo browser. La modalità desktop impedisce al programma di installazione web di rilevare Android e richiedere il permesso di riconnessione dopo i riavvii. È abilitata per impostazione predefinita su tablet grandi con 8 GB+ di RAM (es. Pixel Tablet).
> - Evita le versioni Flatpak e Snap del browser — causano problemi durante l'installazione.
> - **Non** usare la modalità in incognito/navigazione privata — queste modalità limitano lo spazio di archiviazione necessario per estrarre la versione scaricata.

### Dispositivi supportati

Hai bisogno di uno dei [dispositivi Pixel ufficialmente supportati](https://grapheneos.org/faq#supported-devices). **Evita le varianti degli operatori** — i Pixel degli operatori hanno un carrier ID non zero flashato in fabbrica che disabilita lo sblocco del bootloader e dell'operatore. Procurati un dispositivo indipendente dall'operatore (sbloccato).

---

## Abilitare lo sblocco OEM

Lo sblocco OEM deve essere abilitato dall'interno del sistema operativo prima di poter procedere.

1. Vai su **Impostazioni → Info sul telefono/tablet** e tocca ripetutamente **Numero build** finché la modalità sviluppatore non è abilitata.
2. Vai su **Impostazioni → Sistema → Opzioni sviluppatore** e attiva **Sblocco OEM**. Su alcune SKU compatibili con gli operatori, ciò richiede una connessione internet attiva in modo che l'OS stock possa verificare che il dispositivo non sia stato venduto come bloccato a un operatore.

> **Nota Pixel 6a:** Lo sblocco OEM non funzionerà con la versione OS stock di fabbrica. Aggiorna tramite OTA alla versione di **giugno 2022** o successiva, quindi esegui un ripristino di fabbrica per correggere lo sblocco OEM.

---

## Metodo di installazione 1: Programma di installazione web (Consigliato)

Il [programma di installazione web di GrapheneOS](https://grapheneos.org/install/web) è l'approccio consigliato per la maggior parte degli utenti. Usa WebUSB direttamente nel tuo browser — non è richiesta alcuna installazione software.

### Passaggio 1: Aggirare i bug di fwupd (solo Linux)

Su Linux, `fwupd` si connette in modo errato ai dispositivi usando il protocollo fastboot, bloccando il programma di installazione. Fermalo prima di connettere il dispositivo:

```bash
sudo systemctl stop fwupd.service
```

Questo non persisterà attraverso i riavvii.

### Passaggio 2: Configurare le regole udev (solo Linux)

Su Arch Linux:

```bash
sudo pacman -S android-udev
```

Su Debian e Ubuntu:

```bash
sudo apt install android-sdk-platform-tools-common
```

### Passaggio 3: Avvio nell'interfaccia del bootloader

Tieni premuto il pulsante **volume giù** mentre il dispositivo si avvia (accendilo da spento tenendo premuto volume giù, oppure riavvia e tieni premuto volume giù). Il dispositivo deve mostrare un **triangolo di avviso rosso** e le parole **"Fastboot Mode"** — non premere il pulsante di accensione per attivare "Avvia".

### Passaggio 4: Connettere il dispositivo

Collega il dispositivo al computer tramite USB. Su Linux, ricollega il cavo se le regole udev non erano state configurate prima della prima connessione.

> **Pixel Tablet:** Scollega dallo stand prima di collegare tramite USB — il tablet non può usare entrambi simultaneamente.

> **Windows:** L'attuale Windows 10/11 include un driver fastboot generico per Pixel 4a (5G) e successivi. Per Pixel più vecchi o Windows obsoleto, installa il driver da Windows Update (cerca in "Visualizza aggiornamenti opzionali" → "LeMobile Android Device").

### Passaggio 5: Sbloccare il bootloader

Vai su [https://grapheneos.org/install/web](https://grapheneos.org/install/web) e clicca sul pulsante **Sblocca il bootloader**. Conferma sul dispositivo usando i pulsanti del volume per cambiare la selezione e il pulsante di accensione per confermare. **Questo cancella tutti i dati.**

### Passaggio 6: Scaricare e flashare le immagini di fabbrica

1. Clicca su **Scarica versione** per scaricare le immagini di fabbrica per il tuo dispositivo.
2. Clicca su **Flasha immagini di fabbrica** e attendi che il processo sia completato. Flasherà automaticamente il firmware, riavvierà nell'interfaccia del bootloader e flasherà l'OS. **Non interagire con il dispositivo fino al termine.**

### Passaggio 7: Bloccare il bootloader

Dopo il flash, clicca su **Blocca il bootloader** nel programma di installazione web. Conferma sul dispositivo. **Questo cancella di nuovo tutti i dati** — bloccare il bootloader abilita il verified boot completo.

---

## Metodo di installazione 2: Riga di comando (CLI)

### Passaggio 1: Aprire un terminale

Su Windows, apri una finestra **PowerShell normale (non amministratore)**. Rimuovi il vecchio alias `curl`:

```powershell
Remove-Item Alias:Curl
```

### Passaggio 2: Installare fastboot

Hai bisogno di fastboot versione **≥ 35.0.1**.

**Arch Linux:**

```bash
sudo pacman -S android-tools
```

**Debian / Ubuntu** — i loro pacchetti sono obsoleti. Usa la versione standalone:

```bash
# Debian / Ubuntu
sudo apt install libarchive-tools
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-linux.zip
echo 'acfdcccb123a8718c46c46c059b2f621140194e5ec1ac9d81715be3d6ab6cd0a  platform-tools_r35.0.2-linux.zip' | sha256sum -c
bsdtar xvf platform-tools_r35.0.2-linux.zip
export PATH="$PWD/platform-tools:$PATH"
```

**macOS:**

```bash
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-darwin.zip
echo 'SHA256 (platform-tools_r35.0.2-darwin.zip) = 1820078db90bf21628d257ff052528af1c61bb48f754b3555648f5652fa35d78' | shasum -c
tar xvf platform-tools_r35.0.2-darwin.zip
export PATH="$PWD/platform-tools:$PATH"
```

**Windows:**

```powershell
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-win.zip
(Get-FileHash platform-tools_r35.0.2-win.zip).hash -eq "2975a3eac0b19182748d64195375ad056986561d994fffbdc64332a516300bb9"
tar xvf platform-tools_r35.0.2-win.zip
$env:Path = "$pwd\platform-tools;$env:Path"
```

Verifica la versione:

```bash
fastboot --version
# Atteso: fastboot version 35.0.2-12147458
```

### Passaggio 3: Configurare le regole udev (solo Linux)

Arch Linux:

```bash
sudo pacman -S android-udev
```

Debian / Ubuntu:

```bash
sudo apt install android-sdk-platform-tools-common
```

### Passaggio 4: Aggirare i bug di fwupd (solo Linux)

```bash
sudo systemctl stop fwupd.service
```

### Passaggio 5: Avvio nell'interfaccia del bootloader

Tieni premuto **volume giù** durante l'avvio finché il dispositivo non mostra **"Fastboot Mode"** con il triangolo di avviso rosso.

### Passaggio 6: Connettere e sbloccare il bootloader

Collega tramite USB, poi esegui:

```bash
fastboot flashing unlock
```

Conferma sul dispositivo (pulsanti del volume per la selezione, pulsante di accensione per confermare). **Questo cancella tutti i dati.**

### Passaggio 7: Installare OpenSSH (per la verifica delle immagini)

macOS e Windows includono OpenSSH per impostazione predefinita.

Arch Linux:

```bash
sudo pacman -S openssh
```

Debian / Ubuntu:

```bash
sudo apt install openssh-client
```

### Passaggio 8: Scaricare e verificare le immagini di fabbrica

Scarica la chiave di firma:

```bash
curl -O https://releases.grapheneos.org/allowed_signers
```

Contenuto atteso:

```
contact@grapheneos.org ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIUg/m5CoP83b0rfSCzYSVA4cw4ir49io5GPoxbgxdJE
```

Scarica le immagini di fabbrica (sostituisce `DEVICE_NAME` e `VERSION` con i valori reali):

```bash
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip.sig
```

Verifica la firma (Linux / macOS):

```bash
ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" \
  -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip
```

Windows:

```powershell
cmd /c 'ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip'
```

Output atteso:

```
Good "factory images" signature for contact@grapheneos.org with ED25519 key SHA256:AhgHif0mei+9aNyKLfMZBh2yptHdw/aN7Tlh/j2eFwM
```

### Passaggio 9: Flashare le immagini di fabbrica

Estrai le immagini:

```bash
# Linux
bsdtar xvf DEVICE_NAME-install-VERSION.zip

# macOS / Windows
tar xvf DEVICE_NAME-install-VERSION.zip
```

Entra nella directory ed esegui lo script di flash:

```bash
cd DEVICE_NAME-install-VERSION

# Linux / macOS
bash flash-all.sh

# Windows
./flash-all.bat
```

Attendi che il processo finisca. Gestisce automaticamente il flash del firmware, i riavvii del bootloader e il flash dell'OS. **Non interagire con il dispositivo fino al termine.**

> **Risoluzione problemi tmpfs Linux:** Se `/tmp` non ha abbastanza spazio, usa:
> ```bash
> mkdir tmp && TMPDIR="$PWD/tmp" ./flash-all.sh
> ```

### Passaggio 10: Bloccare il bootloader

```bash
fastboot flashing lock
```

Conferma sul dispositivo. **Questo cancella di nuovo tutti i dati.** Il blocco abilita il verified boot completo e impedisce a fastboot di modificare le partizioni.

---

## Post-installazione

### Avvio

Premi il pulsante di accensione con l'opzione predefinita **Avvia** selezionata nell'interfaccia del bootloader per avviare GrapheneOS.

### Disabilitare lo sblocco OEM

Durante la prima configurazione, l'ultima schermata contiene un interruttore per lo sblocco OEM (spuntato per impostazione predefinita — lasciarlo spuntato **disabilita** lo sblocco OEM). Questo è consigliato. Puoi modificarlo più tardi nelle **Opzioni sviluppatore**.

### Verificare l'installazione

GrapheneOS sfrutta il verified boot e l'attestazione hardware. Il verified boot verifica tutto il firmware e le immagini OS ad ogni avvio rispetto alle chiavi bruciate nei fusibili del SoC. GrapheneOS flasha la propria chiave pubblica di verified boot nell'elemento sicuro — ad ogni avvio, questa chiave verifica l'OS.

#### Hash della chiave Verified Boot

Quando viene caricato un OS alternativo, il dispositivo mostra un **avviso giallo** con l'identificatore dell'OS (sha256 della chiave di verified boot). I Pixel di 4ª e 5ª generazione mostrano solo i primi 32 bit; **i Pixel di 6ª generazione in poi mostrano l'hash completo**. Confronta con gli hash ufficiali:

| Dispositivo | Hash della chiave Verified Boot |
|------------|--------------------------------|
| Pixel 10a | `d8f879d10419eddc9fcda6280718be763f6bf12299e1f72df3ea8ad8a8eb7f80` |
| Pixel 10 Pro Fold | `55a2d44103e56d5ec65496399c417987ba77730e6488fc60ba058d09fc3caee3` |
| Pixel 10 Pro XL | `141d7fc32af7958a416f2661b37cf6f27bfb376fb5ce616aeaa27a82c7a04f74` |
| Pixel 10 Pro | `4e8ee8f717754052198ca6d2d3aaa232e2461b4293c0d6f297e519cc778de093` |
| Pixel 10 | `3f7415ea26f5df5b14ea6d153256071a7a1af9ce7b0970b7311cc463c7ea02c7` |
| Pixel 9a | `0508de44ee00bfb49ece32c418af1896391abde0f05b64f41bc9a2dfb589445b` |
| Pixel 9 Pro Fold | `af4d2c6e62be0fec54f0271b9776ff061dd8392d9f51cf6ab1551d346679e24c` |
| Pixel 9 Pro XL | `55d3c2323db91bb91f20d38d015e85112d038f6b6b5738fe352c1a80dba57023` |
| Pixel 9 Pro | `f729cab861da1b83fdfab402fc9480758f2ae78ee0b61c1f2137dd1ab7076e86` |
| Pixel 9 | `9e6a8f3e0d761a780179f93acd5721ba1ab7c8c537c7761073c0a754b0e932de` |
| Pixel 8a | `096b8bd6d44527a24ac1564b308839f67e78202185cbff9cfdcb10e63250bc5e` |
| Pixel 8 Pro | `896db2d09d84e1d6bb747002b8a114950b946e5825772a9d48ba7eb01d118c1c` |
| Pixel 8 | `cd7479653aa88208f9f03034810ef9b7b0af8a9d41e2000e458ac403a2acb233` |
| Pixel Fold | `ee0c9dfef6f55a878538b0dbf7e78e3bc3f1a13c8c44839b095fe26dd5fe2842` |
| Pixel Tablet | `94df136e6c6aa08dc26580af46f36419b5f9baf46039db076f5295b91aaff230` |
| Pixel 7a | `508d75dea10c5cbc3e7632260fc0b59f6055a8a49dd84e693b6d8899edbb01e4` |
| Pixel 7 Pro | `bc1c0dd95664604382bb888412026422742eb333071ea0b2d19036217d49182f` |
| Pixel 7 | `3efe5392be3ac38afb894d13de639e521675e62571a8a9b3ef9fc8c44fd17fa1` |
| Pixel 6a | `08c860350a9600692d10c8512f7b8e80707757468e8fbfeea2a870c0a83d6031` |
| Pixel 6 Pro | `439b76524d94c40652ce1bf0d8243773c634d2f99ba3160d8d02aa5e29ff925c` |
| Pixel 6 | `f0a890375d1405e62ebfd87e8d3f475f948ef031bbf9ddd516d5f600a23677e8` |

#### Attestazione basata su hardware con Auditor

GrapheneOS fornisce l'[app Auditor](https://attestation.app/) per verificare l'integrità di hardware, firmware e OS usando il verified boot e l'attestazione remota. I risultati vengono mostrati su un secondo dispositivo Android che esegue Auditor (non sul dispositivo in fase di verifica), o tramite il [servizio di monitoraggio dell'integrità dei dispositivi](https://attestation.app/) opzionale per verifiche automatiche programmate con avvisi via email.

---

## Sostituire GrapheneOS con l'OS predefinito

L'installazione dell'OS predefinito tramite lo [strumento di flash web di Google](https://flash.android.com/) è simile al processo precedente. Tuttavia, prima di flashare e bloccare, devi cancellare la chiave di verified boot di GrapheneOS per tornare completamente allo stock:

**Programma di installazione web:** Usa il pulsante "Cancella chiave non-stock" nel programma di installazione web di GrapheneOS.

**CLI:**

```bash
fastboot erase avb_custom_key
```

Poi flasha le immagini di fabbrica stock e blocca il bootloader.

---

## Conclusione

Installare GrapheneOS sul tuo Google Pixel offre funzionalità di privacy e sicurezza leader del settore. Usa il **programma di installazione web** su [grapheneos.org/install/web](https://grapheneos.org/install/web) per l'esperienza più semplice, o segui i passaggi CLI precedenti per un approccio tradizionale. Blocca sempre il bootloader dopo il flash per abilitare il verified boot completo, e usa opzionalmente l'app Auditor per confermare l'integrità della tua installazione.

## Riferimenti

1. [Sito web di GrapheneOS](https://grapheneos.org/)
2. [Programma di installazione web di GrapheneOS](https://grapheneos.org/install/web)
3. [Guida all'installazione CLI di GrapheneOS](https://grapheneos.org/install/cli)
4. [Versioni di GrapheneOS](https://grapheneos.org/releases)
5. [Guida all'uso di GrapheneOS](https://grapheneos.org/usage)
6. [FAQ di GrapheneOS](https://grapheneos.org/faq)
7. [App Auditor](https://attestation.app/)
8. [Android Platform Tools](https://developer.android.com/studio/releases/platform-tools)
