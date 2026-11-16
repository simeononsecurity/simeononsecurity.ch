---
title: "Come installare Rayhunter sui dispositivi: guida completa"
draft: false
toc: true
date: 2026-03-09
lastmod: 2026-11-15
description: "Installa e configura Rayhunter per rilevare gli IMSI catcher. Verifica i dispositivi supportati, installa il firmware, controlla il funzionamento e risolvi i problemi più comuni."
tags: ["Rayhunter", "IMSI catcher", "simulatore di stazione cellulare", "sicurezza mobile", "rilevamento della sorveglianza", "protezione della privacy", "Orbic RC400L", "TP-Link M7350", "hotspot mobile", "installazione firmware", "sicurezza informatica", "sicurezza wireless", "contromisure alla sorveglianza", "EFF", "strumenti per la privacy", "acquistare Rayhunter", "guida all'installazione", "configurazione", "dispositivi supportati", "sicurezza di rete"]
cover: "/img/cover/rayhunter.webp"
coverAlt: "Un dispositivo Rayhunter rileva segnali wireless e IMSI catcher, circondato da scudi di sicurezza"
coverCaption: "Sistema Rayhunter per rilevare gli IMSI catcher e proteggere le comunicazioni mobili dalla sorveglianza"
---

**Guida completa all'installazione e alla configurazione di Rayhunter, il sistema per rilevare gli IMSI catcher.**

## In breve

**Rayhunter** è un sistema open source per rilevare gli IMSI catcher che funziona su hotspot mobili modificati. Ti avvisa quando apparecchiature di sorveglianza tentano di intercettare le comunicazioni cellulari. Questa guida descrive l'installazione sui dispositivi Orbic RC400L e TP-Link M7350, le opzioni di configurazione, l'analisi delle minacce e l'efficacia sulle reti 5G. Serve un dispositivo compatibile con un modem Qualcomm. Rileva la sorveglianza sulle reti 2G, 3G e 4G con diverse euristiche. Rimane utile nonostante la diffusione del 5G, perché gli attacchi che costringono i dispositivi a passare a reti meno recenti sono ancora possibili. Offre protezione a giornalisti, attivisti e persone attente alla privacy contro la sorveglianza governativa, criminale e aziendale.

**Rayhunter** è uno strumento open source progettato per rilevare IMSI catcher (simulatori di stazioni cellulari) in grado di intercettare le comunicazioni mobili. Se cerchi **Rayhunter in vendita** o vuoi imparare a installare e configurare questi dispositivi, questa guida completa spiega tutto ciò che serve sapere sui sistemi **Rayhunter**.

**Informativa sulla sponsorizzazione:** Questo articolo è sponsorizzato da [STS Collective](https://stscollective.com), il principale fornitore di dispositivi compatibili con Rayhunter. Nonostante la sponsorizzazione, tutte le informazioni tecniche, le analisi e le raccomandazioni di questa guida si basano sulla documentazione ufficiale di Rayhunter, sui commenti della community e su una valutazione tecnica obiettiva.

> 💰 **Sconto esclusivo per i lettori:** Risparmia fino al 20% sui dispositivi Rayhunter e sui prodotti STS Collective. Usa il codice **SIMEONONSECURITY** al pagamento oppure [acquista direttamente con lo sconto applicato](https://stscollective.com/discount/SIMEONONSECURITY).

## Introduzione a Rayhunter

**Rayhunter** è un sistema avanzato per rilevare gli IMSI catcher, sviluppato dalla **Electronic Frontier Foundation (EFF)**, una delle principali organizzazioni non profit impegnate nella difesa delle libertà civili nel mondo digitale. Dal 1990 EFF promuove la privacy digitale, la libertà di espressione e l'innovazione tramite cause strategiche, analisi delle politiche, attivismo di base e sviluppo tecnologico.

Lo strumento funziona su hotspot mobili compatibili e monitora costantemente le reti cellulari alla ricerca di attività sospette che potrebbero indicare la presenza di simulatori di stazioni cellulari o dispositivi "Stingray" usati per la sorveglianza. **Rayhunter** rappresenta l'impegno di EFF a fornire strumenti pratici di tutela della privacy a persone e organizzazioni che hanno bisogno di proteggersi dalla sorveglianza.

Il sistema **Rayhunter** invia avvisi in tempo reale quando rileva comportamenti potenzialmente dannosi sulle reti cellulari. È uno strumento essenziale per giornalisti, attivisti, professionisti della sicurezza e persone attente alla privacy. Puoi acquistare dispositivi compatibili **[con Rayhunter](https://stscollective.com/collections/rayhunter)** presso STS Collective, il principale fornitore di questi dispositivi specializzati.

### Sostenere il progetto Rayhunter

**Rayhunter** è un progetto open source che beneficia del sostegno della community. Puoi contribuire al suo sviluppo in diversi modi:

- **Acquista tramite STS Collective**: STS Collective dona a EFF una parte dei ricavi di ogni dispositivo Rayhunter venduto, sostenendo lo sviluppo di **Rayhunter** e la ricerca sulla privacy.
- **Fai una donazione diretta**: sostieni le attività più ampie di EFF per la tutela della privacy e lo sviluppo di **Rayhunter** su **[Dona a EFF](https://supporters.eff.org/donate/donate)**.
- **Partecipa alla community**: contribuisci a discussioni, documentazione e test tramite il repository ufficiale su GitHub.

Il tuo sostegno aiuta a mantenere **Rayhunter** gratuito, open source e in costante miglioramento per affrontare le nuove minacce di sorveglianza.

## Assistenza, commenti e comunità

**Rayhunter** è sostenuto da una community attiva di ricercatori nel campo della sicurezza, difensori della privacy e cittadini interessati. Puoi ricevere assistenza e contribuire al progetto tramite diversi canali:

- **Documentazione ufficiale**: [Documentazione di Rayhunter](https://efforg.github.io/rayhunter/introduction.html), con guide complete per installazione, configurazione e uso
- **Repository GitHub**: [EFForg/rayhunter](https://github.com/EFForg/rayhunter)
- **Discussioni della community**: avvia discussioni su GitHub per la compatibilità dei dispositivi e la risoluzione dei problemi
- **Ricerca sulla sicurezza**: collabora con i ricercatori per migliorare le capacità di rilevamento di **Rayhunter**

I dispositivi compatibili **[Rayhunter in vendita](https://stscollective.com/collections/rayhunter)** sono disponibili presso STS Collective.

## Domande frequenti

### Serve una SIM attiva per usare Rayhunter?

**Rayhunter** richiede che il dispositivo contenga una SIM, ma non serve un piano di servizio attivo. La SIM è necessaria perché il dispositivo si connetta alle reti cellulari e controlli la presenza di attività sospette. Se vuoi usare il dispositivo come hotspot mentre esegui **Rayhunter**, serve un piano attivo.

### Come verifico che il mio dispositivo Rayhunter funzioni?

Abilita l'euristica di test nelle impostazioni di **Rayhunter**. Il dispositivo genererà un avviso ogni volta che rileva una stazione cellulare, così potrai verificare che il sistema funzioni correttamente. La modalità di test genera molti avvisi, quindi disabilitala dopo la prova.

### È meglio acquistare un dispositivo bloccato o sbloccato?

Per la compatibilità con **Rayhunter** sono generalmente preferibili i dispositivi sbloccati, soprattutto se vuoi usare SIM diverse da Verizon. La maggior parte dei dispositivi Orbic a marchio Verizon è in realtà sbloccata, ma verifica la compatibilità prima dell'acquisto. STS Collective vende dispositivi compatibili verificati **[con Rayhunter](https://stscollective.com/collections/rayhunter)**.

{{< stscollective-ad "rayhunter" >}}

## Guida per l'installazione

### Installazione dall'ultima versione

L'installazione di **Rayhunter** è stata testata su macOS e Ubuntu 24.04. Se riscontri problemi con le versioni precompilate, potrebbe essere necessario installare dai sorgenti.

#### Prerequisiti

Prima di installare **Rayhunter**, assicurati di avere un dispositivo compatibile. Per i dispositivi TP-Link, inserisci una scheda SD formattata FAT per archiviare le registrazioni.

#### Scaricamento e configurazione

1. **Scarica l'ultima versione**: prendi il file `rayhunter-vX.X.X-PLATFORM.zip` appropriato dalla pagina ufficiale delle release:
   - Linux x64: `linux-x64`
   - Linux ARM64: `linux-aarch64`
   - Linux ARM v7/v8: `linux-armv7`
   - macOS Intel: `macos-intel`
   - macOS ARM (M1/M2): `macos-arm`
   - Windows: `windows-x86_64`

2. **Estrai l'archivio e apri la cartella**:
   ```bash
   unzip ~/Downloads/rayhunter-vX.X.X-PLATFORM.zip
   cd ~/Downloads/rayhunter-vX.X.X-PLATFORM
   ```

3. **Connetti il dispositivo**: accendilo e collegalo tramite WiFi o tethering USB. Dovresti poter accedere a:
   - Dispositivi Orbic: `http://192.168.1.1`
   - Dispositivi TP-Link: `http://192.168.0.1`

#### Installazione per dispositivo

**Per i dispositivi Orbic RC400L** (disponibili **[con Rayhunter](https://stscollective.com)**):

**Rayhunter** supporta due metodi di installazione sui dispositivi Orbic RC400L. Il metodo WiFi è consigliato alla maggior parte degli utenti, mentre quello USB offre ulteriori capacità di debug.

**Installazione tramite WiFi (consigliata)**:
```bash
# Gli utenti macOS devono prima eseguire questo comando:
xattr -d com.apple.quarantine installer

# Per Verizon RC400L (la password amministratore è uguale alla password WiFi):
./installer orbic --admin-password 'YourWiFiPassword'

# Per Kajeet/Smartspot RC400L:
./installer orbic --admin-password='$m@rt$p0tc0nf!g'

# Per i dispositivi Moxee (formato password: 12$ + ultime 3 cifre della password WiFi):
./installer orbic --admin-password='12$XXX'
```

**Installazione tramite USB (utenti esperti)**:
Il metodo USB consente l'accesso ADB (Android Debug Bridge) per il debug avanzato, ma non è consigliato per le installazioni tipiche:

```bash
# ATTENZIONE: l'installer USB non è consigliato per la maggior parte degli utilizzi
./installer orbic-usb
```

Questo metodo forza il dispositivo in modalità debug per abilitare ADB, installa rootshell e **Rayhunter**, quindi riavvia il dispositivo. Usalo solo se ti serve ADB per altri scopi.

**Per i dispositivi TP-Link M7350** (disponibili **[con Rayhunter](https://stscollective.com)**):
```bash
./installer tplink
```

L'installer completerà l'installazione di **Rayhunter** e riavvierà il dispositivo. Una linea verde sul display indica che **Rayhunter** funziona correttamente.

### Installazione dai sorgenti

Per gli sviluppatori o gli utenti che devono compilare **Rayhunter** dai sorgenti, il progetto include:

- **Frontend**: applicazione SvelteKit JavaScript (`./daemon/web/`)
- **Backend**: binario Rust `rayhunter-daemon` (`./daemon/`)
- **Installer**: binario Rust che integra tutti i componenti (`./installer`)

#### Dipendenze di compilazione

Installa le seguenti dipendenze:
- Linguaggio di programmazione Rust
- Node.js/npm
- Strumenti di compilazione C (`build-essential` su Linux, `xcode-select --install` su macOS)

#### Procedura di compilazione

```bash
./scripts/build-dev.sh
./scripts/install-dev.sh orbic  # Sostituisci 'orbic' con il tipo di dispositivo
```

Per lo sviluppo frontend con ricaricamento automatico:
```bash
cd daemon/web
npm run dev
# Oppure specifica una destinazione:
API_TARGET=http://192.168.1.1:8080 npm run dev
```

### Aggiornamento di Rayhunter

L'aggiornamento di **Rayhunter** segue la stessa procedura dell'installazione. Ripeti i passaggi con l'ultima versione per aggiornare il dispositivo alla versione più recente di **Rayhunter**.

## Configurazione

Puoi configurare **Rayhunter** tramite l'interfaccia web oppure modificando direttamente sul dispositivo `/data/rayhunter/config.toml`.

### Configurazione dell'interfaccia online

Per accedere all'interfaccia web di **Rayhunter**, collegati alla rete del dispositivo e visita:
- Orbic: `http://192.168.1.1:8080`
- TP-Link: `http://192.168.0.1:8080`

{{< figure src="rayhunter-dashboard.webp" alt="Dashboard dell'interfaccia web di Rayhunter" caption="L'interfaccia web di Rayhunter offre ampie opzioni di monitoraggio e configurazione" >}}

#### Opzioni di configurazione principali

**Livello UI del dispositivo**: controlla cosa mostra **Rayhunter** sullo schermo:
- **Modalità invisibile**: nessuna visualizzazione
- **Modalità discreta**: linea colorata (verde = sicuro, rossa = avviso, bianca = in pausa)
- **Modalità demo**: mostra la grafica di un'orca con la linea di stato
- **Logo EFF**: mostra il logo EFF con la linea di stato
- **Alta visibilità**: display a colori a schermo intero

**Modalità input del dispositivo**: configura il comportamento del pulsante di accensione:
- **Disabilita il controllo dal pulsante**: il pulsante di accensione non controlla **Rayhunter**
- **Doppio tocco per riavviare la registrazione**: azzera gli avvisi e riavvia il monitoraggio

**Impostazioni notifiche**: configura l'URL ntfy per gli avvisi remoti e abilita o disabilita le notifiche per avvisi e batteria scarica.

**Euristiche dell'analizzatore**: abilita o disabilita specifici algoritmi di rilevamento di **Rayhunter** in base all'ambiente e al modello delle minacce.

## Disinstallazione di Rayhunter

### Dispositivi Orbic

Per rimuovere **Rayhunter** dai dispositivi Orbic, esegui:

```bash
./installer util orbic-shell --admin-password mypassword
```

All'interno della shell:

> **Attenzione:** i seguenti comandi eliminano in modo permanente i file di Rayhunter e i relativi hook di avvio. Verifica di essere nella shell del dispositivo previsto, copia le registrazioni o la configurazione necessarie e tieni a disposizione l'installer e il firmware compatibile prima di procedere. Al termine, verifica che i file siano assenti e che il dispositivo si riavvii senza il servizio Rayhunter. Se devi annullare le modifiche, reinstalla la release corrispondente dal repository ufficiale.

```bash
echo 3 > /usrdata/mode.cfg
rm -rf /data/rayhunter /etc/init.d/rayhunter_daemon /bin/rootshell
reboot
```

### Dispositivi TP-Link

Per disinstallare Rayhunter dai dispositivi TP-Link:

> **Attenzione:** questi comandi rimuovono i file di Rayhunter e il relativo hook di avvio dal dispositivo TP-Link. Esporta prima le registrazioni e la configurazione. Esegui i comandi solo nella shell del dispositivo, poi verifica che i percorsi siano assenti e che il dispositivo si avvii normalmente. Per annullare l'operazione, reinstalla la release corrispondente dal repository ufficiale.

```bash
./installer util tplink-shell
rm /data/rayhunter /etc/init.d/rayhunter_daemon
update-rc.d rayhunter_daemon remove
```

Rimuovi eventuali trigger di porta residui nell'interfaccia amministrativa TP-Link, sotto Settings > NAT Settings > Port Triggers.

## Uso di Rayhunter

Dopo l'installazione, **Rayhunter** si avvia automaticamente e monitora costantemente le reti cellulari per individuare attività sospette. In condizioni normali il display mostra una linea verde, che diventa una serie di puntini gialli, trattini arancioni o una linea rossa continua quando rileva IMSI catcher potenziali.

### Euristiche di rilevamento di Rayhunter

**Rayhunter** impiega diversi algoritmi di rilevamento avanzati per identificare possibili attività di IMSI catcher:

#### Rilevamento delle richieste IMSI
Questa euristica identifica sequenze sospette in cui le stazioni cellulari richiedono l'identità del dispositivo (IMSI, International Mobile Subscriber Identity) senza seguire i protocolli di autenticazione corretti. **Rayhunter** controlla i tempi e il contesto delle richieste, segnalando schemi anomali che indicano possibili apparecchiature di sorveglianza.

Le reti cellulari legittime seguono procedure di autenticazione standardizzate prima di richiedere identificativi sensibili. Gli IMSI catcher spesso aggirano tali procedure per raccogliere rapidamente le identità dei dispositivi, creando anomalie rilevabili nella sequenza di autenticazione. Questo metodo è particolarmente efficace contro gli IMSI catcher "passivi" di base, che si limitano a raccogliere informazioni sui dispositivi.

#### Rilevamento della disconnessione e del passaggio forzato a 2G
**Rayhunter** monitora costantemente i tentativi sospetti di disconnettere i dispositivi mobili dalle reti sicure 4G/5G e riconnetterli alle reti 2G meno sicure. Questo attacco di downgrade è comune perché le reti 2G usano una crittografia più debole e sono più facili da intercettare.

Il sistema analizza gli schemi delle disconnessioni, cercando frequenza, tempi e contesti anomali che suggeriscano intenti malevoli anziché la normale ottimizzazione della rete. Le reti legittime possono talvolta suggerire un downgrade per motivi di copertura o capacità, ma **Rayhunter** può distinguere il normale comportamento di rete da una possibile attività di sorveglianza.

#### Rilevamento del passaggio forzato a reti meno recenti tramite LTE SIB6/7
I System Information Block (SIB) sono messaggi broadcast con cui le reti cellulari inviano informazioni di configurazione ai dispositivi mobili. **Rayhunter** monitora in particolare i messaggi SIB6 e SIB7, che contengono informazioni sulle celle vicine e sul reindirizzamento delle frequenze.

Gli attori malevoli possono trasmettere messaggi SIB6/7 falsi per costringere i dispositivi ad abbandonare connessioni 4G sicure e connettersi a reti 2G sotto il loro controllo. **Rayhunter** analizza queste trasmissioni alla ricerca di incongruenze, reindirizzamenti anomali e altri segnali della presenza di stazioni base fraudolente che tentano di forzare il downgrade delle connessioni per intercettarle.

#### Rilevamento della cifratura nulla
Questo metodo di rilevamento essenziale individua quando una rete cellulare propone di comunicare senza cifratura, usando un cifrario nullo. Le reti cellulari commerciali legittime non dovrebbero mai proporre connessioni non cifrate, perché violerebbero gli standard di sicurezza e i requisiti normativi.

**Rayhunter** segnala come altamente sospetta ogni rete che propone un cifrario nullo. *Una rete legittima non proporrà mai un cifrario nullo.* Questo indica chiaramente apparecchiature di sorveglianza che cercano di intercettare comunicazioni in testo in chiaro. L'euristica è particolarmente efficace contro IMSI catcher che privilegiano la raccolta di dati rispetto all'apparenza di una rete legittima.

#### Rilevamento di SIB incompleti
Le stazioni base cellulari legittime trasmettono System Information Block completi, contenenti i dati essenziali di configurazione della rete. **Rayhunter** monitora le stazioni base che forniscono informazioni di sistema incomplete o mancanti, spesso indice di apparecchiature di sorveglianza installate in fretta o configurate male.

Gli IMSI catcher spesso non implementano tutte le funzioni di una rete cellulare e si limitano a quelle minime necessarie per connettere i dispositivi e intercettare dati. Rilevando queste implementazioni incomplete, **Rayhunter** può individuare stazioni base potenzialmente malevole prive delle funzionalità previste dalla normale infrastruttura cellulare.

{{< figure src="rayhunter-heuristics-overview.webp" alt="Diagramma delle cinque euristiche di rilevamento di Rayhunter: richiesta IMSI senza autenticazione, downgrade a 2G, reindirizzamento LTE SIB6/7, proposta di cifrario nullo e trasmissione di informazioni di sistema incomplete" >}}
## Attori delle minacce e potenziali obiettivi

Capire chi usa gli IMSI catcher e chi prende di mira è essenziale per valutare il proprio modello di minaccia e scegliere la configurazione appropriata di **Rayhunter**. I diversi attori dispongono di livelli di sofisticazione differenti e le loro strategie di targeting indicano quali tipi di sorveglianza **Rayhunter** è progettato per rilevare.

### Agenzie governative e forze dell'ordine

**Livello di sofisticazione della minaccia**: da avanzato a professionale
**Obiettivi principali**:
- Sospetti criminali sotto indagine
- Persone di interesse in casi di sicurezza nazionale
- Manifestanti e attivisti durante le proteste
- Sorveglianza della popolazione in aree ad alta sicurezza
- Cittadini stranieri e personale diplomatico

**Schemi di rilevamento**: gli IMSI catcher governativi usano spesso apparecchiature sofisticate, capaci di evitare le euristiche di rilevamento di base. Tuttavia, ricorrono spesso ad **attacchi di downgrade a 2G** e **schemi di disconnessione** per costringere i dispositivi a usare reti meno sicure, più facili da intercettare. Il rilevamento dei downgrade LTE SIB6/7 e il monitoraggio delle disconnessioni di **Rayhunter** sono particolarmente efficaci contro le tecniche di sorveglianza delle forze dell'ordine.

**Scenari tipici**:
- Sorveglianza durante proteste, manifestazioni o raduni pubblici
- Monitoraggio della posizione vicino a edifici governativi o infrastrutture sensibili
- Sorveglianza mirata di specifiche persone sotto indagine
- Operazioni di sorveglianza a confini e aeroporti

### Agenzie dei servizi segreti nazionali ed esteri

**Livello di sofisticazione della minaccia**: da professionale a militare
**Obiettivi principali**:
- Operativi e risorse dei servizi di intelligence stranieri
- Funzionari governativi e personale diplomatico
- Appaltatori della difesa e ricercatori
- Dirigenti aziendali in settori strategici
- Giornalisti che si occupano di sicurezza nazionale
- Attivisti impegnati su temi politici sensibili

**Schemi di rilevamento**: le apparecchiature dei servizi di intelligence sono progettate per non farsi notare, ma il rilevamento dei cifrari nulli e il monitoraggio degli SIB incompleti di **Rayhunter** possono identificare anche operazioni di sorveglianza sofisticate. Nelle operazioni mirate le agenzie usano spesso apparecchiature che richiedono **informazioni IMSI**, attivando gli algoritmi di **Rayhunter** per il rilevamento delle richieste IMSI.

**Scenari tipici**:
- Sorveglianza a lungo termine di obiettivi di intelligence importanti
- Spionaggio industriale vicino alle sedi aziendali
- Monitoraggio di diplomatici e ambasciate
- Operazioni di controspionaggio
- Servizi di intelligence stranieri che prendono di mira risorse nazionali

### Organizzazioni criminali

**Livello di sofisticazione della minaccia**: da base a intermedio
**Obiettivi principali**:
- Persone facoltose per rapimenti o estorsioni
- Concorrenti per ottenere informazioni aziendali
- Forze dell'ordine che indagano sulla criminalità organizzata
- Testimoni e informatori in procedimenti penali
- Vittime di stalking, molestie o violenza domestica

**Schemi di rilevamento**: le organizzazioni criminali usano in genere IMSI catcher commerciali a basso costo, che attivano più euristiche di **Rayhunter** contemporaneamente. Questi dispositivi presentano spesso **implementazioni SIB incomplete**, usano **cifrari nulli** per massimizzare la raccolta dei dati e adottano **attacchi aggressivi di downgrade a 2G** a causa di competenze tecniche limitate.

**Scenari tipici**:
- Tracciamento di potenziali vittime di rapimento o rapina
- Monitoraggio delle comunicazioni delle forze dell'ordine durante operazioni criminali
- Spionaggio industriale e raccolta di informazioni sui concorrenti
- Campagne di stalking e molestie
- Intimidazione dei testimoni e tracciamento della posizione

### Spionaggio aziendale e servizi informativi privati

**Livello di sofisticazione della minaccia**: da intermedio ad avanzato
**Obiettivi principali**:
- Dirigenti di aziende concorrenti
- Team di ricerca e sviluppo
- Negoziatori di fusioni e acquisizioni
- Titolari di proprietà intellettuale
- Custodi di segreti commerciali
- Segnalanti aziendali e fonti di minacce interne

**Schemi di rilevamento**: le operazioni di sorveglianza aziendale spesso utilizzano apparecchiature di fascia media che bilanciano costo e funzionalità. Queste operazioni attivano frequentemente il **rilevamento delle disconnessioni** e gli **avvisi per richieste IMSI** quando prendono di mira determinate persone durante trattative commerciali o cicli di sviluppo dei prodotti.

**Scenari tipici**:
- Sorveglianza durante negoziazioni di fusioni e acquisizioni
- Raccolta di informazioni sui concorrenti in fiere e conferenze
- Operazioni di furto della proprietà intellettuale
- Monitoraggio dei dipendenti e rilevamento delle minacce interne
- Raccolta di dati sui clienti per ottenere vantaggi competitivi

### Investigatori privati e aziende di sorveglianza

**Livello di sofisticazione della minaccia**: da base a intermedio
**Obiettivi principali**:
- Persone indagate per frode assicurativa
- Coniugi coinvolti in procedimenti di divorzio
- Dipendenti sospettati di comportamenti scorretti
- Persone coinvolte in controversie legali
- Celebrità e obiettivi di alto profilo

**Schemi di rilevamento**: le operazioni di sorveglianza privata utilizzano di solito apparecchiature commerciali con possibilità limitate di personalizzazione. Per i vincoli di costo e le limitazioni tecniche, questi sistemi attivano spesso le euristiche di base di **Rayhunter**, in particolare il **rilevamento dei cifrari nulli** e il **monitoraggio degli SIB incompleti**.

**Scenari tipici**:
- Indagini su divorzi e affidamento dei figli
- Sorveglianza per frodi assicurative
- Indagini sui comportamenti scorretti dei dipendenti
- Stalking di celebrità e attività dei paparazzi
- Indagini legali e raccolta di prove

### Individui malevoli e hacktivisti

**Livello di sofisticazione della minaccia**: da base a intermedio
**Obiettivi principali**:
- Nemici personali o partner sentimentali
- Personaggi pubblici e celebrità
- Vittime casuali in luoghi pubblici
- Partecipanti a specifici eventi o persone in determinate località
- Membri di comunità o gruppi presi di mira

**Schemi di rilevamento**: i singoli attori usano in genere configurazioni di IMSI catcher elementari, spesso improvvisate, che attivano più algoritmi di **Rayhunter** contemporaneamente. Queste installazioni presentano spesso **uso di cifrari nulli**, **trasmissioni SIB incomplete** e rozzi **tentativi di downgrade a 2G**.

**Scenari tipici**:
- Campagne di stalking e molestie
- Furto d'identità e frodi finanziarie
- Interruzione dell'attivismo politico e delle proteste
- Attività criminali informatiche generiche
- Sorveglianza opportunistica durante eventi pubblici

### Valutazione delle minacce e configurazione di Rayhunter

Le **persone ad alto rischio** (giornalisti, attivisti, funzionari governativi e dirigenti) dovrebbero abilitare tutte le euristiche di **Rayhunter** e usare la modalità di visualizzazione **alta visibilità** per ottenere la massima capacità di rilevamento.

Le **persone a rischio moderato** (in generale chi presta attenzione alla privacy) possono usare la modalità **discreta** con le euristiche principali abilitate, per proteggersi ogni giorno senza attirare l'attenzione.

La **protezione durante eventi** (proteste, riunioni riservate, viaggi) giustifica l'attivazione temporanea di tutti i metodi di rilevamento e dei sistemi di notifica per avere una consapevolezza completa della sorveglianza.

Conoscere il proprio modello di minaccia aiuta a ottimizzare la configurazione di **Rayhunter** per il profilo di rischio personale e a garantire una copertura adeguata contro gli attori che potrebbero prendere di mira te o le tue attività.

{{< figure src="imsi-catcher-threat-actors-surveillance.webp" alt="Diagramma dei diversi attori che usano IMSI catcher, tra cui agenzie governative, organizzazioni criminali e operatori di spionaggio aziendale che prendono di mira dispositivi mobili" >}}

## Efficacia di Rayhunter con il 5G

{{< figure src="rayhunter-5g-downgrade-attack-persistence.webp" alt="Diagramma di un telefono 5G costretto da un attacco di downgrade a collegarsi a una rete 4G o 3G monitorata, tecnica che Rayhunter continua a rilevare nell'era 5G" >}}

Con la transizione delle reti cellulari al 5G, ci si chiede quanto **Rayhunter** resti efficace, dato che rileva attività su 2G, 3G e 4G/LTE ma non i metodi di sorveglianza nativi del 5G. Comprendere i limiti attuali e la continua utilità di **Rayhunter** in un mondo 5G è essenziale per pianificare strategie di rilevamento a lungo termine.

### Perché Rayhunter resta efficace sulle reti 5G

#### Persistenza degli attacchi che forzano il passaggio a reti meno recenti
Il vettore di attacco fondamentale rilevato da **Rayhunter**, che forza i dispositivi a collegarsi a reti meno sicure, resta importante nei deployment 5G. **Gli IMSI catcher continuano a usare attacchi di downgrade a 2G e 3G** perché:

- **Costi di implementazione inferiori**: costruire apparecchiature per i protocolli più vecchi richiede un investimento molto minore rispetto allo sviluppo di sistemi compatibili con il 5G.
- **Maggiore compatibilità con i dispositivi**: prendere di mira 2G/3G permette di colpire anche i dispositivi più vecchi che non supportano il 5G.
- **Metodi di attacco consolidati**: le tecniche di sorveglianza sulle reti 2G/3G sono documentate e collaudate.
- **Vantaggi normativi**: alcune tecnologie di sorveglianza più vecchie potrebbero essere soggette a meno restrizioni legali rispetto ai metodi avanzati di intercettazione 5G.

#### Compatibilità retroattiva delle reti
Le reti 5G mantengono la **compatibilità retroattiva con 4G/LTE** e la maggior parte dei dispositivi mobili supporta più generazioni contemporaneamente. Questa compatibilità crea ancora opportunità per gli attacchi di downgrade che **Rayhunter** è specializzato nel rilevare:

- **Ritorno automatico a una rete precedente**: i dispositivi passano naturalmente a 4G quando la copertura 5G è scarsa, creando occasioni per intercettare la transizione.
- **Vulnerabilità nella negoziazione dei protocolli**: IMSI catcher sofisticati possono manipolare la procedura di handshake fra generazioni di rete diverse.
- **Sfruttamento delle lacune di copertura**: apparecchiature di sorveglianza posizionate strategicamente in aree con copertura 5G incompleta possono forzare i dispositivi su reti 4G/LTE monitorate.

#### Gradualità nell'implementazione del 5G
La **lenta diffusione di una copertura 5G completa** manterrà **Rayhunter** utile ancora per anni:

- **Differenze tra aree urbane e rurali**: molte regioni dipendono ancora soprattutto dalle reti 4G/LTE, dove le capacità di rilevamento di **Rayhunter** sono direttamente applicabili.
- **Limiti della copertura indoor**: i segnali 5G spesso attraversano male gli edifici, facendo passare i dispositivi a reti 4G che **Rayhunter** può monitorare efficacemente.
- **Viaggi internazionali**: la diffusione globale del 5G varia molto da paese a paese, quindi la sorveglianza tramite 4G/LTE resta un rischio per i viaggiatori.

#### Ritardo tecnologico degli attori delle minacce
I cicli di **acquisizione e implementazione delle apparecchiature di sorveglianza** spesso sono in ritardo rispetto alla tecnologia delle reti commerciali:

- **Tempi di approvvigionamento governativo**: le forze dell'ordine e i servizi di intelligence potrebbero continuare a usare per anni apparecchiature 4G esistenti dopo l'arrivo del 5G.
- **Analisi costi-benefici**: molte operazioni ottengono i risultati desiderati intercettando reti 4G/LTE a costi inferiori, riducendo l'incentivo a passare a sistemi compatibili con il 5G.
- **Requisiti di formazione e competenza**: l'uso di apparecchiature di sorveglianza 5G richiede conoscenze specialistiche che potrebbero richiedere tempo per essere sviluppate nelle organizzazioni.

### Limiti di Rayhunter nei veri ambienti 5G

#### Punti ciechi nella sorveglianza 5G nativa
*Questo è il limite principale di Rayhunter.* **Rayhunter non può rilevare le operazioni native degli IMSI catcher 5G** che non si basano su attacchi di downgrade:

- **Reti 5G standalone (SA)**: quando i dispositivi si collegano a reti esclusivamente 5G senza ripiegare su 4G, **Rayhunter** non può monitorare queste comunicazioni.
- **Apparecchiature avanzate di sorveglianza 5G**: attori sofisticati con accesso a tecnologie avanzate potrebbero intercettare comunicazioni 5G senza attivare le euristiche di **Rayhunter**.
- **Sfruttamento del network slicing**: le funzionalità di network slicing 5G potrebbero essere usate per la sorveglianza in modi non rilevabili da **Rayhunter**.

#### Funzionalità di sicurezza 5G migliorate
Le reti 5G integrano **misure di sicurezza migliorate**, che potrebbero ridurre l'efficacia delle tecniche di sorveglianza tradizionali:

- **Protocolli di cifratura più robusti**: il 5G implementa standard più resistenti, più difficili da violare rispetto alle generazioni precedenti.
- **Procedure di autenticazione migliorate**: l'autenticazione avanzata dei dispositivi sulle reti 5G potrebbe rendere più difficile raccogliere gli IMSI.
- **Monitoraggio della sicurezza di rete**: l'infrastruttura 5G dispone di funzionalità migliori di rilevamento delle intrusioni, che potrebbero individuare e contrastare i tentativi di sorveglianza.

#### Cambiamenti nel comportamento dei dispositivi
Con la diffusione del 5G, **il comportamento dei dispositivi mobili potrebbe evolvere**, influenzando le capacità di rilevamento di **Rayhunter**:

- **Minore propensione al downgrade**: futuri aggiornamenti software potrebbero rendere i dispositivi più resistenti agli attacchi di downgrade man mano che migliora la copertura 5G.
- **Preferenza per il 5G**: i dispositivi potrebbero dare sempre più priorità alle connessioni 5G e insospettirsi di più quando viene richiesto l'uso di protocolli più vecchi.
- **Maggiore consapevolezza della sicurezza**: i sistemi operativi mobili potrebbero rilevare meglio i comportamenti di rete sospetti.

### Considerazioni strategiche per l'implementazione di Rayhunter

#### Raccomandazioni attuali per l'implementazione
Per l'impiego attuale e nel prossimo futuro, **Rayhunter** offre **funzionalità complete di rilevamento della sorveglianza**:

- **Impiego urbano**: anche nelle grandi città con ampia copertura 5G, **Rayhunter** rileva i tentativi di sorveglianza sulle reti 4G/LTE.
- **Protezione durante eventi critici**: durante proteste, riunioni riservate o attività ad alto rischio, **Rayhunter** offre capacità di rilevamento essenziali indipendentemente dalla disponibilità del 5G.
- **Sicurezza in viaggio**: **Rayhunter** resta molto efficace per rilevare la sorveglianza durante viaggi nazionali e internazionali.

#### Strategie per prepararsi al futuro
Organizzazioni e individui che pianificano il rilevamento a lungo termine dovrebbero considerare:

- **Approcci ibridi di rilevamento**: combinare **Rayhunter** con altri strumenti di sicurezza e tecniche di monitoraggio offre una copertura completa di più vettori di minaccia.
- **Aggiornamenti regolari della valutazione delle minacce**: monitorare l'evoluzione della tecnologia di sorveglianza aiuta a decidere quando integrare o sostituire le capacità di **Rayhunter**.
- **Sostegno allo sviluppo della community**: sostenere lo sviluppo open source di **Rayhunter** aumenta la probabilità che le versioni future aggiungano funzionalità di rilevamento 5G.

#### Monitorare l'evoluzione della tecnologia
La community **Rayhunter** e EFF continuano a ricercare **capacità di rilevamento della sorveglianza 5G**:

- **Ricerca sull'analisi dei protocolli**: la ricerca in corso sui protocolli 5G potrebbe individuare nuove opportunità di rilevamento per le versioni future di **Rayhunter**.
- **Studi sulla compatibilità hardware**: valutare se i dispositivi compatibili con **Rayhunter** possono essere migliorati per rilevare tentativi di sorveglianza 5G.
- **Monitoraggio del panorama delle minacce**: seguire lo sviluppo e la diffusione di apparecchiature di sorveglianza compatibili con il 5G aiuta a stabilire le priorità per l'evoluzione di **Rayhunter**.

**Rayhunter** rimane uno **strumento essenziale per rilevare la sorveglianza** nel panorama attuale delle telecomunicazioni e dovrebbe restare utile per diversi anni, mentre il 5G viene implementato gradualmente e gli attori continuano a usare attacchi di downgrade collaudati.

### Rianalizzare le registrazioni

**Rayhunter** migliora costantemente le proprie capacità di rilevamento. Puoi rianalizzare le vecchie registrazioni con le euristiche aggiornate: fai clic su "N warnings" nell'interfaccia web e seleziona "re-analyze".

### Analisi su computer

Per gli utenti esperti, **Rayhunter** include `rayhunter-check`, uno strumento CLI per analizzare file PCAP e QMDL su sistemi desktop:

```bash
rayhunter-check -p ~/Downloads/myfile.qmdl
rayhunter-check -p ~/Downloads/myfile.pcap
rayhunter-check -d -p ~/Downloads/myfile.qmdl  # Modalità debug
```

## Dispositivi supportati

**Rayhunter** supporta diversi hotspot mobili con modem Qualcomm che espongono l'interfaccia `/dev/diag`.

{{< figure src="/img/rayhunter-device-regions.svg" alt="Compatibilità dei dispositivi Rayhunter per regione" caption="Compatibilità dei dispositivi e raccomandazioni regionali per l'installazione di Rayhunter" >}}
### Dispositivi consigliati

Questi dispositivi sono stati testati a fondo e sono ampiamente usati dalla community **Rayhunter**:

#### Orbic RC400L (a volte venduto con il marchio Kajeet RC400L)
- **Regione consigliata**: Americhe
- **Bande supportate**:
  - 5G: n260/n261, n77, n2/5/48/66
  - 4G: 2/4/5/12/13/48/66
  - Globale e roaming: n257/n78
- **Disponibilità**: sono disponibili dispositivi compatibili, tra cui il **[nuovo Orbic RC400L con Rayhunter](https://stscollective.com/products/new-rayhunter-orbic-rc400l-imsi-catcher-detector-premium?variant=51361976811822)** e il **[Kajeet RC400L](https://stscollective.com/products/rayhunter-imsi-catcher-detector-kajeet-rc400lx-4g-lte-hotspot?variant=51411271844142)**
- **Fascia di prezzo**: i modelli professionali sono disponibili tramite STS Collective

#### TP-Link M7350
- **Regione consigliata**: Africa, Europa, Medio Oriente (funziona anche nelle Americhe, ma in genere costa di più)
- **Requisiti speciali**: per le registrazioni serve una scheda SD formattata in FAT
- **Disponibilità**: modelli compatibili verificati sono disponibili come **[TP-Link M7350 con Rayhunter](https://stscollective.com/collections/rayhunter)**

### Dispositivi funzionanti

È stato confermato che **Rayhunter** funziona anche sui seguenti dispositivi:

- **Wingtech CT2MHS01** (Americhe), **[disponibile con Rayhunter](https://stscollective.com/collections/rayhunter)**
- **Tmobile TMOHS1** (Americhe), **[disponibile con Rayhunter](https://stscollective.com/collections/rayhunter)**
- **TP-Link M7310** (Africa, Europa, Medio Oriente), **[disponibile con Rayhunter](https://stscollective.com)**
- **PinePhone e PinePhone Pro** (globale), **[disponibili con Rayhunter](https://stscollective.com)**
- **FY UZ801** (Asia, Europa), **[disponibile con Rayhunter](https://stscollective.com)**
- **Hotspot Moxee** (Americhe), **[Moxee K779HSDL con Rayhunter](https://stscollective.com/products/rayhunter-imsi-catcher-stingray-detector-moxee-k779hsdl-hotspot-professionally-refurbished-pre-installed-4g-lte-cellular-threat-detection-device?variant=51309010420014)**

### Note di installazione per dispositivo

#### Orbic/Kajeet RC400L

Orbic RC400L è il dispositivo originale per cui è stato sviluppato **Rayhunter**. È **[disponibile con Rayhunter](https://stscollective.com)** tramite STS Collective.

**Metodi di installazione**:
- **Via rete**: `./installer orbic` (consigliato, funziona tramite WiFi)
- **Via USB**: `./installer orbic-usb` (fornisce accesso ADB e una shell root)

**Password predefinite**:
- **Verizon RC400L**: la password amministratore è sempre uguale a quella WiFi (si trova nel menu del dispositivo)
- **Kajeet/Smartspot RC400L**: `$m@rt$p0tc0nf!g`
- **Dispositivi Moxee**: formato password `12$XXX`, dove XXX rappresenta le ultime 3 cifre della password WiFi (controlla sotto la batteria)

**Accesso alla shell**: dopo l'installazione usa `./installer util orbic-shell`.

#### TP-Link M7350/M7310

Questi dispositivi funzionano in modo affidabile con **Rayhunter** e sono **[disponibili con Rayhunter](https://stscollective.com)**.

**Installazione**: `./installer tplink` (non serve una password amministratore)
**Archiviazione**: inserisci una scheda SD formattata in FAT prima dell'installazione
**Accesso alla shell**: `./installer util tplink-shell`

#### Dispositivi specializzati

**PinePhone e PinePhone Pro**: compatibilità globale, **[disponibili con Rayhunter](https://stscollective.com)**
**UZ801**: diffuso nelle aree di Asia ed Europa, **[disponibile con Rayhunter](https://stscollective.com)**
**Wingtech CT2MHS01**: dispositivo per le Americhe, **[disponibile con Rayhunter](https://stscollective.com)**

### Aggiungere nuovi dispositivi

**Rayhunter** potrebbe supportare qualsiasi dispositivo con modem Qualcomm che espone l'interfaccia `/dev/diag`. Se vuoi che **Rayhunter** supporti un dispositivo, apri una discussione nel repository ufficiale su GitHub.

## Documentazione dell'API REST

**Rayhunter** offre una REST API completa per accedere in modo programmatico allo stato del dispositivo, alle registrazioni e alla configurazione. L'API consente l'integrazione con altri strumenti di sicurezza e sistemi di monitoraggio automatizzati.

### Documentazione API ufficiale

Per il riferimento API completo, incluse le specifiche dettagliate degli endpoint, esempi di richieste e risposte e metodi di autenticazione, consulta la **[documentazione ufficiale REST API di Rayhunter](https://efforg.github.io/rayhunter/api-docs/)**.

### Punti di accesso API

L'API di **Rayhunter** è accessibile all'indirizzo `http://[device-ip]:8080/api/` e fornisce endpoint per:

- **Stato del sistema**: monitorare la salute del dispositivo e il funzionamento di **Rayhunter**
- **Gestione delle registrazioni**: avviare, interrompere e scaricare le registrazioni
- **Recupero degli avvisi**: accedere agli avvisi di rilevamento e ai risultati dell'analisi
- **Configurazione**: aggiornare in modo programmatico le impostazioni di **Rayhunter**
- **Controllo delle euristiche**: abilitare o disabilitare specifici algoritmi di rilevamento
- **Informazioni sul dispositivo**: recuperare specifiche e capacità del dispositivo
- **Monitoraggio della rete**: accedere ai dati cellulari in tempo reale
- **Registro eventi**: consultare gli eventi di rilevamento e gli avvisi passati

### Autenticazione

L'accesso all'API usa la stessa autenticazione dell'interfaccia web. Proteggi il dispositivo **Rayhunter** e consenti l'accesso solo agli utenti autorizzati.

### Esempi di integrazione

La REST API di **Rayhunter** può integrarsi con piattaforme di monitoraggio della sicurezza, sistemi SIEM e strumenti di automazione personalizzati. Consulta la **[documentazione API ufficiale](https://efforg.github.io/rayhunter/api-docs/)** per esempi completi di implementazione e buone pratiche.

## Risoluzione dei problemi

### Problemi di installazione comuni

**Problemi di connessione USB**: prova cavi o porte USB diversi. Collegamenti USB difettosi causano spesso errori di installazione. *È la causa più comune delle installazioni non riuscite.*

**Problemi di sicurezza macOS**: se compare "No Orbic device found", cambia temporaneamente "Allow accessories to connect" in "Always" nelle impostazioni di sicurezza.

**Rilevamento del dispositivo**: dopo l'installazione abilita l'euristica di test per verificare che **Rayhunter** funzioni correttamente.

### Ottenere assistenza

Per assistenza con l'installazione e la risoluzione dei problemi:
- Consulta la documentazione ufficiale di **Rayhunter**
- Usa `./installer --help` e `./installer util --help` per le opzioni dei comandi
- Partecipa alle discussioni della community su GitHub
- Contatta **[STS Collective](https://stscollective.com)** per domande sulla compatibilità dei dispositivi

## Domande frequenti (FAQ)

### Domande generali

#### Che cos'è esattamente un IMSI catcher e come funziona?
Un IMSI catcher, chiamato anche StingRay, simulatore di stazione cellulare o falsa torre cellulare, è un'apparecchiatura di sorveglianza che imita le stazioni cellulari legittime per intercettare le comunicazioni mobili. Costringe i dispositivi nelle vicinanze a collegarsi all'apparecchiatura malevola anziché alle stazioni legittime, consentendo agli operatori di raccogliere identificativi dei dispositivi (numeri IMSI), dati sulla posizione, metadati delle chiamate e potenzialmente intercettare le comunicazioni. **Rayhunter** rileva questi dispositivi identificando schemi anomali nel comportamento delle reti cellulari.

#### Rayhunter rileva ogni tipo di apparecchiatura di sorveglianza?
**Rayhunter** rileva specificamente IMSI catcher e simulatori di stazioni cellulari che operano sulle reti 2G, 3G e 4G/LTE. Non rileva altre forme di sorveglianza come il monitoraggio WiFi, i localizzatori GPS, la sorveglianza fisica o la sorveglianza nativa 5G che non usa attacchi di downgrade. **Rayhunter** è un componente di una strategia completa per la protezione della privacy.

#### È legale usare Rayhunter?
L'uso di **Rayhunter** è legale nella maggior parte delle giurisdizioni, perché è uno strumento di monitoraggio passivo che non interferisce con reti cellulari o altri dispositivi. Analizza soltanto i segnali cellulari che il dispositivo riceve normalmente. Le leggi locali variano, quindi verifica le normative applicabili. EFF ha sviluppato **Rayhunter** come strumento legittimo per la protezione della privacy.

### Domande tecniche

#### Perché Rayhunter richiede una SIM se non serve un servizio attivo?
La SIM fornisce l'International Mobile Subscriber Identity (IMSI) necessaria al dispositivo per autenticarsi sulle reti cellulari e partecipare agli scambi di protocollo monitorati da **Rayhunter**. Senza SIM il dispositivo non può collegarsi alle reti cellulari e **Rayhunter** non avrebbe attività di rete da analizzare per individuare schemi sospetti.

#### Quanti dati consuma Rayhunter durante il normale funzionamento?
**Rayhunter** consuma pochi dati per il monitoraggio di base, perché analizza principalmente informazioni sui protocolli cellulari, non il traffico Internet. Il consumo aumenta se abiliti le notifiche remote tramite ntfy o usi contemporaneamente il dispositivo come hotspot. Il monitoraggio da solo usa una larghezza di banda trascurabile.

#### Posso usare Rayhunter mentre il dispositivo funziona da hotspot mobile?
Sì, **Rayhunter** può funzionare contemporaneamente all'hotspot mobile. Serve un piano di servizio cellulare attivo. Il monitoraggio di **Rayhunter** è indipendente dalla funzione hotspot, ma usare entrambe le funzioni consuma più batteria.

#### Qual è la differenza tra installazione WiFi e USB?
Il **metodo WiFi** (consigliato alla maggior parte degli utenti) installa **Rayhunter** tramite l'interfaccia wireless del dispositivo e offre le funzioni standard. Il **metodo USB** fornisce ad utenti esperti l'accesso ad Android Debug Bridge (ADB) per il debug, ma è più complesso e non serve per le installazioni tipiche.

### Domande su dispositivi e compatibilità

#### Perché Rayhunter supporta solo alcuni dispositivi?
**Rayhunter** richiede un dispositivo con modem Qualcomm che espone l'interfaccia `/dev/diag`, che fornisce accesso alle informazioni sui protocolli cellulari. La maggior parte dei dispositivi consumer non espone questa interfaccia per motivi di sicurezza. I dispositivi supportati sono stati testati appositamente e risultano compatibili con i requisiti di **Rayhunter**.

#### Posso installare Rayhunter sul mio normale smartphone?
No. **Rayhunter** non si installa sugli smartphone normali. Richiede hotspot mobili specializzati con specifici modem Qualcomm che espongono interfacce diagnostiche. Tra i dispositivi supportati ci sono Orbic RC400L, TP-Link M7350 e diversi altri modelli di hotspot mobile.

#### Che cosa succede se provo a installare Rayhunter su un dispositivo incompatibile?
L'installer di **Rayhunter** rileva il dispositivo e in genere rifiuta l'installazione su hardware incompatibile. Forzare l'installazione su dispositivi non supportati potrebbe danneggiarli o renderli inutilizzabili. Verifica sempre la compatibilità prima di procedere.

#### Servono dispositivi diversi per regioni diverse?
Sì. Le bande di frequenza cellulari variano a seconda dell'area geografica. Orbic RC400L è ottimizzato per le reti delle Americhe, mentre TP-Link M7350 funziona bene in Europa, Africa e Medio Oriente. Le informazioni sulla compatibilità di **Rayhunter** includono raccomandazioni regionali per scegliere il dispositivo adatto alla propria posizione.

### Domande su uso e configurazione

#### Come verifico che il mio dispositivo Rayhunter funzioni correttamente?
Abilita l'euristica di test nelle impostazioni di **Rayhunter**. Genererà un avviso ogni volta che il dispositivo rileva una stazione cellulare, confermando il funzionamento del sistema. Durante il normale funzionamento il display dovrebbe mostrare una linea verde. Ricordati di disabilitare l'euristica dopo la verifica, perché genera molti avvisi.

#### Cosa devo fare se Rayhunter invia un avviso?
Quando **Rayhunter** rileva attività sospette, annota prima la posizione e le circostanze. L'ottimizzazione di rete o problemi delle apparecchiature possono generare falsi positivi. Se gli avvisi persistono nella stessa posizione o durante attività sensibili, valuta di spostarti e controlla i dettagli nell'interfaccia web.

#### Ogni quanto devo aggiornare Rayhunter?
**Aggiorna Rayhunter ogni mese.** Controlla la pagina delle release per nuove euristiche e miglioramenti di compatibilità, che vengono aggiunti spesso. EFF migliora costantemente le capacità di **Rayhunter** in risposta alle tecniche di sorveglianza in evoluzione. L'aggiornamento segue la stessa procedura dell'installazione iniziale.

#### Rayhunter può proteggere più persone contemporaneamente?
**Rayhunter** rileva IMSI catcher nell'area circostante e può proteggere più persone nel raggio d'azione, in genere alcune centinaia di metri, a seconda dell'intensità del segnale. Tuttavia, chi prende seriamente il rilevamento della sorveglianza dovrebbe considerare un dispositivo **Rayhunter** personale per avere la massima protezione e controllo della configurazione.

### Domande su sicurezza e privacy

#### Usare Rayhunter mi rende più visibile agli occhi della sorveglianza?
**Rayhunter** opera passivamente e non trasmette segnali che lo identifichino alle apparecchiature di sorveglianza. Tuttavia, usare strumenti di sicurezza indica attenzione alla privacy. I vantaggi del rilevamento in genere superano i rischi, soprattutto per persone ad alto rischio come giornalisti e attivisti.

#### Le apparecchiature di sorveglianza possono capire che uso Rayhunter?
**Rayhunter** è un sistema di monitoraggio passivo e non trasmette segnali identificativi. Gli operatori di sorveglianza non possono rilevare l'uso di **Rayhunter** a livello di protocollo cellulare. L'osservazione fisica del dispositivo o l'analisi del traffico di rete potrebbero però rivelare l'uso di **Rayhunter** se sono abilitate le notifiche remote.

#### Quali informazioni raccoglie Rayhunter su di me?
**Rayhunter** analizza informazioni sui protocolli cellulari e conserva localmente gli avvisi di rilevamento sul dispositivo. Non raccoglie informazioni personali, contenuti delle comunicazioni o dati di posizione oltre a quanto necessario per gli algoritmi di rilevamento. Tutti i dati restano sul dispositivo, a meno che tu non abiliti le notifiche remote.

### Domande avanzate

#### Posso analizzare i dati Rayhunter sul computer?
Sì. **Rayhunter** include lo strumento a riga di comando `rayhunter-check` per analizzare file PCAP e QMDL registrati su computer desktop. Gli utenti esperti possono così esaminare in dettaglio gli eventi di rilevamento e indagare sulle attività sospette usando tutte le risorse del computer.

#### Come funziona Rayhunter negli ambienti urbani densamente popolati?
Le numerose stazioni cellulari legittime nelle aree urbane dense possono aumentare i falsi positivi, perché l'ottimizzazione della rete e i passaggi fra celle avvengono più spesso. Gli algoritmi di **Rayhunter** distinguono il comportamento normale della rete dall'attività di sorveglianza, ma in aree dense potrebbe essere necessario regolare la sensibilità.

#### Rayhunter funziona durante i viaggi internazionali?
L'efficacia di **Rayhunter** in viaggio dipende dalla compatibilità del dispositivo con le bande cellulari locali e gli accordi di roaming. Gli algoritmi di rilevamento funzionano globalmente, ma verifica che il dispositivo supporti le frequenze usate nel paese di destinazione. Per la piena funzionalità potrebbe servire il roaming internazionale.

{{< figure src="rayhunter-faq-privacy-protection.webp" alt="Persona che controlla gli avvisi di Rayhunter su un laptop e porta un hotspot mobile in un'area urbana con stazioni cellulari vicine" >}}

______

**Rayhunter** rappresenta un importante progresso nella protezione della privacy personale e nel rilevamento della sorveglianza. Installando e configurando correttamente **Rayhunter** su dispositivi compatibili, potrai rilevare IMSI catcher e proteggere le comunicazioni mobili dalla sorveglianza non autorizzata.

Che tu sia giornalista, attivista, professionista della sicurezza o persona attenta alla privacy, **Rayhunter** offre strumenti per mantenere la sicurezza mobile in un mondo sempre più sorvegliato. Per dispositivi compatibili verificati, consulta le opzioni **[Rayhunter in vendita](https://stscollective.com)** dei fornitori affidabili di apparecchiature di sicurezza.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Acquista dispositivi Rayhunter e risparmia il 20%
{{< /centerbutton >}}

## Riferimenti

- [Repository GitHub ufficiale di Rayhunter](https://github.com/EFForg/rayhunter)
- [Ultima release di Rayhunter](https://github.com/EFForg/rayhunter/releases/tag/v0.10.2)
- [Electronic Frontier Foundation](https://www.eff.org/)
- [STS Collective, fornitore di apparecchiature Rayhunter](https://stscollective.com)
