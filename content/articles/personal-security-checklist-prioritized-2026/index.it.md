---
title: "Checklist di sicurezza personale 2026: da dove iniziare e cosa saltare"
date: 2026-09-30
lastmod: 2026-11-15
toc: true
draft: false
description: "Dai priorità alle misure di sicurezza personale in base al loro impatto sugli attacchi, dalla protezione degli account ai backup, dalla privacy al recupero degli accessi."
genre: ["Sicurezza personale", "Privacy", "Igiene digitale", "Sicurezza degli account", "Modellazione delle minacce", "Sicurezza dei consumatori", "Gestione delle password", "Protezione dei dati"]
tags: ["checklist di sicurezza personale", "checklist di sicurezza digitale", "checklist privacy 2026", "cybersicurezza personale", "sicurezza degli account", "configurazione passkey", "chiave di sicurezza hardware", "configurazione gestore password", "best practice 2fa", "resistenza al phishing", "monitoraggio delle violazioni", "notifiche sulle violazioni", "blocco del credito", "privacy degli alias e-mail", "compartimentazione", "modello di minaccia", "crittografia completa del disco", "strategia di backup 3-2-1", "protezione del browser", "blocco dei tracker", "DNS tramite HTTPS", "rimozione dei metadati", "rimozione EXIF", "protezione dallo scambio SIM", "recupero dell'account", "codici di backup", "furto dei token di sessione", "malware infostealer", "priorità di sicurezza personale", "errori di igiene della sicurezza", "strumenti per la privacy", "strumenti di sicurezza lato client"]
cover: "/img/cover/personal-security-checklist-2026-tiered-structure.webp"
coverAlt: "Illustrazione digitale su sfondo scuro con blocchi colorati disposti a livelli per rappresentare le misure di sicurezza personale. Ogni blocco simboleggia un'azione, come usare un gestore di password e l'autenticazione a due fattori."
coverCaption: ""
ref: ["/articles/how-to-form-your-own-personal-threat-model-safeguard-online-security", "/articles/bitwarden-and-keepassxc-vs-the-rest", "/checklists/password-security-checklist"]
---

**Ogni guida alla sicurezza personale ti consegna la stessa cosa: un lungo elenco piatto di centinaia di consigli senza un ordine di priorità.** Ti dicono di disattivare WebRTC, falsificare l'impronta canvas e cambiare lo user-agent, nella stessa frase in cui raccomandano un gestore di password e gli aggiornamenti automatici.

*Queste misure non hanno lo stesso valore. Trattarle come equivalenti porta molte persone a fare le cose facili, saltare quelle importanti e restare altrettanto esposte.*

Questo articolo conserva l'argomento ed elimina la falsa equivalenza. Troverai gli stessi consigli, ordinati in base al rischio rimosso rispetto all'impegno richiesto, e una valutazione onesta delle abitudini da abbandonare.

## La risposta breve

| Domanda | Risposta breve |
|---|---|
| **Cosa ferma più attacchi?** | Un gestore di password, fattori aggiuntivi resistenti al phishing e aggiornamenti tempestivi. Queste abitudini affrontano i percorsi comuni di compromissione degli account, non tutte le minacce. |
| **Qual è il miglior aggiornamento disponibile oggi?** | **Passkey o chiave di sicurezza hardware.** Entrambe resistono al phishing durante l'accesso perché la credenziale non lascia il dispositivo. Proteggi anche i metodi di recupero e il dispositivo stesso. |
| **Cosa è sopravvalutato?** | Password complesse da ricordare, rotazione programmata delle password e la maggior parte delle modifiche all'impronta del browser. |
| **Cosa è sottovalutato?** | Backup, configurazione del recupero account e sicurezza fisica dei dispositivi. |
| **L'ordine conta?** | Sì, più della completezza. **Completare oggi il livello 1 è meglio che fare tutti i 300 punti prima o poi.** |
| **Quanto dura il livello 1?** | Circa due ore, una volta sola. |

## Perché l'ordine conta più della completezza

Una checklist completa elenca in genere centinaia di voci e le contrassegna come **Essenziale**, **Facoltativo** o **Avanzato**. L'etichetta è utile per filtrare, ma non sostituisce una graduatoria, perché assegna lo stesso valore a ogni voce indipendentemente dal rischio che riduce.

**La mia tesi: neppure tre livelli offrono sufficiente precisione**, perché «Essenziale» raggruppa elementi con riduzioni del rischio molto diverse. Confronta due voci entrambe essenziali:

- **Attiva la 2FA** e rimuovi un'intera categoria di furti di account.
- **Disattiva WebRTC** e chiudi una divulgazione dell'IP locale che interessa a un piccolo gruppo di utenti.

Entrambe meritano un posto in un elenco completo. Solo una appartiene alla prima ora.

**Il principio corretto per ordinare le azioni è un rapporto.** Classifica ogni azione in base al rischio rimosso diviso per l'impegno richiesto, poi procedi dall'alto. Ecco l'ordine:

| Livello | Scopo | Impegno | Blocca |
|---|---|---|---|
| **1. Ferma l'attacco** | Chiudi i percorsi usati oggi dagli aggressori | ~2 ore | Furto di credenziali, phishing, malware, furto del dispositivo |
| **2. Contieni i danni** | Limita le conseguenze quando qualcosa si guasta | ~1 ora | Singolo punto di errore, blocco dell'account, frode d'identità |
| **3. Riduci l'esposizione** | Riduci la tua impronta digitale | Continuo | Profilazione, tracciamento, ingegneria sociale mirata |
| **4. Sicurezza fisica e umana** | Copri ciò che il software non raggiunge | ~30 minuti | Sequestro dei dispositivi, osservazione dello schermo, phishing vocale |

*Procedi verso il basso. Non saltare al livello 3 solo perché sembra più interessante.*
{{< figure src="personal-security-tiers-ranked-by-impact.webp" alt="Diagramma dei quattro livelli di azioni di sicurezza personale, ordinati per rischio eliminato e impegno richiesto, dal blocco degli attacchi alle misure fisiche e umane" >}}

## Livello 1: Ferma l'attacco

Cinque voci richiedono circa due ore in totale e affrontano i percorsi usati dagli aggressori.

### 1. Un gestore di password e password uniche ovunque

**Il riutilizzo automatizzato delle credenziali (credential stuffing) è il metodo dominante per prendere il controllo degli account**, perché le persone riutilizzano le password. Quando un sito subisce una violazione, gli aggressori riprovano automaticamente e su larga scala quelle credenziali sugli altri siti.

Un gestore di password risolve la causa principale rendendo impossibile riutilizzarle per errore. Genera una password distinta ad alta entropia per ogni account e la inserisce al posto tuo.

Un dettaglio importante che molti consigli omettono: **la password del gestore è ora il singolo punto di errore**. Deve essere lunga e memorizzata. È l'unica password che non devi salvare altrove. Una passphrase di cinque o sei parole casuali è più forte di una stringa breve e complessa, oltre che molto più facile da ricordare.

Esistono due architetture valide:

| Approccio | Vantaggio | Compromesso |
|---|---|---|
| **Sincronizzato nel cloud** (Bitwarden e simili) | Comodo, sincronizza tra i dispositivi, semplice da recuperare | Ti fidi della crittografia e della disponibilità del fornitore |
| **File offline** (KeePassXC e simili) | Pieno controllo, nessuna dipendenza dal fornitore | Sei responsabile di backup e sincronizzazione |

*Scegli uno dei due. La differenza tra loro è molto più piccola di quella tra usare un gestore e non usarlo.*

Consulta il confronto completo **[Migliori gestori di password 2026: Bitwarden contro KeePassXC](/articles/bitwarden-and-keepassxc-vs-the-rest/)** e la guida **[Creare password solide nel 2026](/articles/how-to-create-strong-passwords/)**.

### 2. Fattori aggiuntivi resistenti al phishing

I fattori aggiuntivi non sono intercambiabili. Differiscono molto negli attacchi che riescono a contrastare.

| Metodo | Ferma il credential stuffing | Ferma il phishing | Ferma il furto del token di sessione |
|---|---|---|---|
| **Codici SMS** | Sì | In parte, tramite SIM swap | No |
| **Codici delle app di autenticazione** | Sì | In parte, tramite relay in tempo reale | No |
| **Approvazione push** | Sì | Debolmente, tramite bombardamento di richieste | No |
| **Passkey o chiave hardware** | Sì | **Sì** | Sì |

**Passkey e chiavi hardware FIDO2 sono le uniche opzioni nell'elenco che sconfiggono il phishing.** La ragione è strutturale, non incrementale: la credenziale è associata all'origine, quindi un dominio simile non riceve nulla di utilizzabile. Non c'è un codice che la vittima possa leggere ad alta voce all'aggressore.

Va nominata anche una minaccia correlata, perché neutralizza metodi che molti considerano sicuri. **I malware infostealer ora raccolgono direttamente i cookie del browser**, consentendo a un aggressore di riutilizzare una sessione autenticata senza password né secondo fattore. Ecco perché conta l'ultima colonna e perché **il punto 3 del livello 1 non è facoltativo**.

*Ordine di priorità: passkey quando disponibili, chiave hardware per e-mail e finanze, app di autenticazione per il resto, SMS solo quando non esiste un'opzione migliore.*

{{< figure src="phishing-resistant-second-factor-comparison.webp" alt="Diagramma che confronta codici SMS, app di autenticazione, approvazione push e passkey rispetto a credential stuffing, phishing e furto di token di sessione. Le passkey li contrastano tutti." >}}

Genera e verifica localmente codici basati sul tempo con il nostro **[Generatore TOTP e HOTP](/totp-generator/)**, che legge un segreto Base32 o un URI `otpauth://` e funziona interamente nel browser.

### 3. Aggiornamenti automatici ovunque

**La maggior parte delle intrusioni riuscite sfrutta vulnerabilità per cui esiste già una patch.** Gli aggressori fanno affidamento sul ritardo con cui installi gli aggiornamenti.

La soluzione pratica non è diventare più diligenti negli aggiornamenti. Elimina la decisione attivandoli automaticamente a ogni livello:

- **Sistema operativo**: Windows Update, Aggiornamento Software su macOS oppure unattended-upgrades su Linux
- **Browser**: lascia attivi gli aggiornamenti automatici e riavvia quando richiesto. Un riavvio in sospeso significa che il browser non è ancora aggiornato.
- **Telefono**: abilita gli aggiornamenti automatici delle app, non solo quelli del sistema operativo
- **Router**: è il livello che si dimentica più spesso, e può essere raggiunto dall'esterno

**Un browser in attesa del riavvio esegue codice vulnerabile.** Questa sola abitudine riduce l'esposizione più della maggior parte degli elementi del livello 3 messi insieme.

*La nostra analisi dell'evasione dal kernel in **[I container non sono più un confine di sicurezza](/articles/containers-no-longer-security-boundary-2026/)** mostra quanto sia importante la finestra per installare una patch quando si sfrutta un'escalation di privilegi.*

### 4. Crittografia del dispositivo e blocco schermo effettivo

**La crittografia completa del disco trasforma il furto di un dispositivo da violazione dei dati a perdita dell'hardware.** Senza, chiunque abbia il tuo portatile o telefono può leggere ogni dato, inclusi il vault del gestore di password e i token delle sessioni attive.

Ogni piattaforma principale offre la crittografia, ma su alcune non è attiva per impostazione predefinita:

| Piattaforma | Funzione | Verifica |
|---|---|---|
| **Windows** | BitLocker o Device Encryption | Impostazioni, poi Privacy e sicurezza, quindi Crittografia dispositivo |
| **macOS** | FileVault | Impostazioni di Sistema, poi Privacy e sicurezza, quindi FileVault |
| **Linux** | LUKS | Durante l'installazione, conferma che i volumi root e home siano cifrati |
| **iOS e Android** | Attiva per impostazione predefinita dopo aver impostato un codice | Imposta un codice e verifica che la crittografia sia attiva |

Oltre alla crittografia, contano due regole:

- **Usa una passphrase o un PIN lungo, non un codice di quattro cifre.** Gli account e-mail e finanziari meritano il blocco più forte del telefono, perché il codice protegge tutto il resto sul dispositivo.
- **Se rischi coercizione legale, preferisci un PIN alla biometria.** La biometria è comoda e facile da ricordare, ma in alcune giurisdizioni impronte o volti imposti hanno tutele diverse dalla conoscenza forzata.

### 5. Backup, da testare una volta

**Ransomware e guasti hardware hanno lo stesso esito, e il backup è l'unico controllo che resiste a entrambi.** È l'elemento che si salta più spesso e di cui ci si pente di più.

Lo schema standard è **3-2-1**: tre copie su due tipi di supporto, con una copia fuori sede. Per una persona significa:

- **Una copia locale** per ripristinare rapidamente
- **Una copia cifrata fuori sede** per ransomware e incendi
- **Una copia offline o una copia scrivibile** nel caso in cui il ransomware raggiunga lo spazio sincronizzato

*Quest'ultimo punto conta più degli altri ed è quello meno attuato. Lo spazio sincronizzato non è un backup. Ransomware ed eliminazioni accidentali si propagano.*

**Prova a ripristinare almeno una volta.** Un backup mai ripristinato è un'ipotesi.

## Livello 2: Contieni i danni

Il livello 1 presume che nulla si guasti. Il livello 2 presume che qualcosa si guasti e limita le conseguenze.

### 6. Smetti di riutilizzare il tuo indirizzo e-mail

**L'indirizzo e-mail è la chiave di collegamento tra tutti i database mai violati.** Usare lo stesso indirizzo ovunque permette di correlare una violazione con le altre e offre agli ingegneri sociali un punto di partenza verificato.

**Gli alias risolvono entrambi i problemi.** Genera un indirizzo unico per ogni servizio, così l'indirizzo diventa un'etichetta:

| Vantaggio | Perché conta |
|---|---|
| **Attribuire una violazione** | Se lo spam arriva a un alias, scopri quale servizio ha divulgato o venduto il tuo indirizzo |
| **Blocco immediato** | Disattiva un solo alias senza toccare la casella reale |
| **Resistenza alla correlazione** | Indirizzi distinti impediscono di unire gli account in un unico profilo |
| **Rilevamento del phishing** | I messaggi a un alias non più usato sono chiaramente fraudolenti |

**Il subaddressing** (`you+service@example.com`) è una versione più debole. Aiuta a capire chi ha divulgato il tuo indirizzo, ma rivela anche l'indirizzo reale, quindi non impedisce la correlazione.

*Se possiedi un dominio, gli alias catch-all offrono questa funzione gratuitamente. Altrimenti, lo stesso compito è svolto da fornitori di alias dedicati.*

### 7. Il vero punto d'attacco è il recupero dell'account

**Gli aggressori saltano sempre più spesso la porta d'ingresso e puntano al recupero.** Il recupero deve funzionare anche dopo la perdita del dispositivo, senza diventare l'anello più debole.

Configura questi elementi nell'ordine:

- **Salva i codici di backup offline.** Stampali o conservali su supporti cifrati e tienili **separati dal gestore di password**, così la compromissione di uno non espone l'altro.
- **Preferisci chiavi di recupero alle domande di sicurezza.** Le risposte su cognome da nubile di tua madre o prima auto sono spesso disponibili negli archivi pubblici.
- **Usa risposte false se un sito impone domande.** Salvale nel gestore insieme all'account.
- **Registra un secondo dispositivo o chiave** dove consentito, così un singolo guasto non ti blocca.
- **Rimuovi contatti e numeri di recupero obsoleti**, perché un vecchio numero ora appartiene a qualcun altro.

> **Avviso: perdere il secondo fattore senza codici di recupero significa spesso perdere l'account per sempre. I team di supporto non ripristineranno l'accesso a un account protetto correttamente.** Configura il recupero quando abiliti il secondo fattore.

{{< figure src="three-two-one-backup-strategy-diagram.webp" alt="Diagramma del modello di backup 3-2-1: tre copie di dati su due tipi di supporto e una copia offline protetta da ransomware ed eliminazioni accidentali" >}}

### 8. Monitora le violazioni per venirne a conoscenza presto

**Il valore di una notifica di violazione dipende interamente dalla tempestività.** Vuoi sapere della fuga mentre la password è ancora valida da qualche parte.

- **Have I Been Pwned** invia avvisi quando il tuo indirizzo compare in un nuovo insieme di dati e offre notifiche per l'intero dominio se lo possiedi e usi alias.
- **Il gestore di password fornisce un segnale migliore**, perché conosce le voci del vault associate al servizio notificato e le segnala direttamente.

*Il flusso utile è breve: arriva un avviso, cambi la password dell'account interessato e la cambi ovunque l'avessi riutilizzata. Ecco il vantaggio del punto 1 del livello 1: le password uniche rendono inutile il secondo passaggio.*

### 9. Blocca il credito prima di averne bisogno

**Il blocco del credito è la protezione più forte disponibile contro la frode d'identità con apertura di nuovi account** ed è gratuito. Impedisce ai creditori di consultare il tuo fascicolo per aprire conti a tuo nome.

Negli Stati Uniti il blocco si può richiedere presso ciascuna delle tre principali agenzie di credito. Lo sblocco per una richiesta legittima è temporaneo e reversibile. Segui questi passaggi:

1. **Blocca il credito in tutte e tre le agenzie**, non in una sola. Ognuna conserva un fascicolo distinto.
2. **Conserva i PIN di sblocco** nel gestore di password.
3. **Sblocca temporaneamente** quando richiedi credito, poi bloccalo di nuovo.

*Fallo prima di averne bisogno. Scoprire la procedura durante una frode, mentre contesti anche gli account, è il momento peggiore per impararla.*

## Livello 3: Riduci l'esposizione

Il livello 3 riduce la tua impronta digitale. È importante, ma viene dopo gli elementi precedenti perché non impedisce la compromissione degli account.

### 10. Proteggi il browser che usi

**La maggior parte dell'esposizione dei dati personali avviene nel browser**, e due modifiche ne affrontano gran parte:

- **Installa un blocco dei contenuti.** Pubblicità e tracker sono i principali strumenti di raccolta sul web. Bloccarli elimina sia il tracciamento sia una parte consistente della superficie d'attacco. Scegli un blocco affidabile invece di installarne diversi.
- **Riduci le estensioni a quelle che usi.** **Le estensioni leggono e modificano i contenuti delle pagine**, quindi un'estensione abbandonata o dannosa può aprire una via diretta alle tue sessioni. Controlla l'elenco ogni trimestre.

*La randomizzazione dell'impronta del browser merita di essere compresa e raramente è una priorità. Non vale zero, ma rende meno dei punti da 1 a 5 e può compromettere i siti.*

Consulta l'analisi completa in **[Migliori browser per la privacy 2026: LibreWolf contro Brave e Tor](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/)**.

### 11. Cifra il DNS

**Il DNS in chiaro non è cifrato ed è osservabile: il gestore di rete e chiunque si trovi lungo il percorso può vedere ogni dominio che risolvi.** DNS-over-HTTPS o DNS-over-TLS cifra le richieste.

Due precisazioni:

- **DoH sposta la fiducia, non la rimuove.** Le richieste vengono viste dal resolver anziché dal provider Internet. Scegline uno con un'informativa sulla privacy pubblica; il solo protocollo non basta.
- **DoH aggira i filtri a livello di rete**, compresi i controlli parentali e aziendali su cui molte persone fanno affidamento.

*Un autentico vantaggio di sicurezza oltre alla privacy: il DNS cifrato elimina lo spoofing DNS come percorso d'attacco pratico nelle reti ostili.*

### 12. Rimuovi i metadati prima di condividere

**Le foto contengono più dei pixel.** La maggior parte delle fotocamere dei telefoni incorpora dati EXIF, tra cui coordinate GPS, timestamp e identificativi del dispositivo.

**Questo conta più per i documenti che per le foto.** Un PDF o un file Office condiviso spesso conserva nomi degli autori, cronologia delle modifiche e percorsi di file interni, rivelando dettagli sull'organizzazione.

Il nostro **[Visualizzatore EXIF](/exif-viewer/)** legge localmente i metadati di un'immagine, così puoi vedere cosa rivela una foto senza caricarla. Il **[Parser URL](/url-parser/)** fa lo stesso per i link, mostrando parametri di tracciamento e credenziali incorporate nell'autorità prima di incollare un URL in chat.

## Livello 4: Sicurezza fisica e umana

Questo livello richiede circa trenta minuti e copre ciò che nessun controllo software raggiunge.

### 13. Controllo fisico dei dispositivi

- **Blocca tutti gli schermi**, con un timeout breve. Un portatile sbloccato equivale alla compromissione completa dell'account.
- **Non lasciare mai i dispositivi in vista in un veicolo.** Questo evita il furto, che comporta anche perdita di dati.
- **Usa uno schermo per la privacy** negli spazi pubblici, per contrastare la maggior parte degli sguardi indiscreti.
- **Controlla le stazioni di ricarica pubbliche** prima di collegarti. Preferisci un cavo solo alimentazione o il tuo alimentatore da muro a una porta USB sconosciuta.

### 14. Verifica le persone, non i messaggi

**Il phishing vocale e video ha ormai superato l'idea che una voce familiare provi l'identità.** Clonare una voce da pochi secondi di audio pubblico è comune, e la richiesta spesso include urgenza e una domanda di pagamento o credenziali.

Usa un canale indipendente per verificare:

1. **Riaggancia e richiama** un numero che conoscevi già, non quello fornito dal chiamante.
2. **Considera l'urgenza un segnale, non un motivo.** La pressione ad agire subito è il meccanismo dell'attacco, non un dettaglio secondario.
3. **Concorda una frase di verifica** con i familiari che potrebbero essere impersonati.
4. **Non trasferire denaro basandoti solo su una chiamata o un messaggio vocale.**

*È l'azione con il maggior rendimento del livello 4 e non costa nulla.*

### 15. Documenti e smaltimento

- **Distruggi o oscura** documenti con numeri di conto, identificativi o dati medici.
- **Aggiungi una filigrana ai documenti** condivisi per uno scopo preciso, indicando destinatario e data. Non costa nulla e aiuta a tracciare una fuga.
- **Rinuncia ai siti di ricerca delle persone**, aspettandoti di ripetere la procedura perché gli elenchi ricompaiono.
- **Controlla i registri pubblici** e chiedi la rimozione dei dati dove possibile.

*La nostra **[Checklist di sicurezza fisica](/checklists/physical-security-checklist/)** approfondisce questo livello.*

## Cosa sbaglia la maggior parte delle persone

Otto abitudini da abbandonare, con il motivo per cui persistono e cosa fare al loro posto.

| Abitudine | Perché persiste | Cosa fare invece |
|---|---|---|
| **Memorizzare password brevi e complesse** | Per anni le regole di complessità sono state la guida | Usa un gestore e una passphrase lunga per il vault |
| **Ruotare le password secondo un calendario** | Vecchie regole di conformità | Cambia la password dopo una notifica di violazione o un sospetto di compromissione, non a scadenze fisse |
| **Affidarsi agli SMS per gli account importanti** | È l'opzione predefinita | Passa a passkey o chiave hardware per account e-mail, finanziari e d'identità |
| **Conservare i codici 2FA nello stesso gestore delle password** | Comodità | Tienili separati, così una sola violazione non espone entrambi i fattori |
| **Considerare il cloud sincronizzato un backup** | Sembra esserlo | Aggiungi una copia offline o una copia scrivibile |
| **Inseguire l'impronta perfetta del browser** | È misurabile e quindi sembra utile | Prima completa i punti da 1 a 5 |
| **Rispondere onestamente alle domande di sicurezza** | Sembra obbligatorio | Usa risposte false salvate nel gestore |
| **Supporre che HTTPS significhi sicurezza** | Il lucchetto rassicura | Verifica il dominio, perché la maggior parte dei siti di phishing ha certificati validi |

Il modello ricorrente in tutte e otto: **sono visibili e misurabili, quindi attirano l'attenzione, ma vengono dopo azioni con un rendimento maggiore.** Chi ottimizza l'entropia dell'impronta prima di configurare un gestore di password ha invertito l'ordine.

> **Errore comune: considerare i gestori di password un rischio perché concentrano i segreti.** Concentrano effettivamente il rischio, ma l'alternativa è riutilizzare le password su decine di siti. Concentrare il rischio sotto il tuo controllo è meglio che disperderlo senza controllo.

## Proteggi i dati senza cederli

In tutto questo argomento ricorre un problema pratico. **Gli strumenti che aiutano a proteggere gli account spesso chiedono proprio i segreti che vuoi proteggere.**

Un controllo della robustezza che invia la password a un server è una responsabilità. Un calcolatore di hash che carica il file vanifica lo scopo. Uno strumento per certificati che interroga il tuo hostname comunica a terzi quali siti gestisci.

**Tutti gli strumenti qui sotto funzionano interamente nel browser**, senza caricamenti e senza account. È una politica dichiarata del sito; le eccezioni sono indicate apertamente.

**Verifica tu stesso il confine:** scollega la rete, apri lo strumento e controlla il pannello di rete del browser mentre elabori un valore di prova. La promessa di elaborazione locale descrive il progetto previsto. Valuta anche le estensioni del browser e la versione dello strumento.

| Attività | Strumento | Cosa gestisce |
|---|---|---|
| **Creare una password robusta** | **[Generatore di password](/password-generator/)** | `crypto.getRandomValues` con campionamento per rifiuto per evitare bias modulo, più l'entropia delle impostazioni scelte |
| **Verificare la robustezza della password** | **[Controllo password](/password-checker/)** | Valuta localmente una candidata, inclusa la rilevazione di schemi e riutilizzo |
| **Configurare un secondo fattore** | **[Generatore TOTP e HOTP](/totp-generator/)** | Legge un segreto Base32 o URI `otpauth://` e verifica i codici in finestre temporali |
| **Ispezionare il certificato di un sito** | **[Informazioni sul certificato SSL](/ssl-certificate-info/)** | Soggetto, validità, robustezza della chiave, SAN e segnalazioni di algoritmi deboli |
| **Controllare una catena di certificati** | **[Tester della catena SSL](/ssl-chain-tester/)** | Ordina la catena e verifica ogni firma, rilevando gli intermedi mancanti |
| **Verificare un download o un file** | **[Calcolatore hash](/hash-calculator/)** | Da MD5 a SHA-512 per confermare l'integrità rispetto a un digest pubblicato |
| **Generare identificativi univoci** | **[Generatore UUID](/uuid-generator/)** | Identificativi versione 4 con bit di versione e variante corretti |
| **Ispezionare un link sospetto** | **[Analizzatore URL](/url-parser/)** | Decodifica il percorso, elenca i parametri e segnala credenziali nell'autorità |
| **Controllare i metadati di una foto** | **[Visualizzatore EXIF](/exif-viewer/)** | Mostra posizione GPS, timestamp e dati del dispositivo |
| **Misurare codifica o crittografia** | **[Analizzatore di entropia](/entropy-analyzer/)** | Entropia di Shannon per distinguere dati ripetitivi da dati codificati o cifrati |
| **Neutralizzare un indicatore in sicurezza** | **[Disattiva e riattiva IOC](/ioc-defang-refang/)** | Rende inerti URL e indirizzi quando li condividi |

*Il principio della tabella: se uno strumento ha bisogno del segreto, dovrebbe funzionare dove si trova quel segreto. Consulta **[Tutti gli strumenti](/tools/)** per l'elenco completo, inclusi i pochi che effettuano richieste di rete e il motivo.*

## La domanda sul modello di minaccia

**La checklist corretta dipende da chi vuoi tenere lontano**, e ignorare questa domanda porta a impegnarsi nelle cose sbagliate.

| La tua situazione | Avversario realistico | Priorità |
|---|---|---|
| **La maggior parte delle persone** | Criminali opportunisti, credential stuffing automatizzato e phishing indiscriminato | Livelli 1 e 2, oltre ai dispositivi che porti con te |
| **Persona nota o ruolo pubblico** | Phishing mirato, doxxing, tentativi di compromissione degli account | Aggiungi compartimentazione, alias e valuta il monitoraggio della presenza sui social |
| **Giornalista, attivista o rischio legale** | Avversari statali o ben finanziati, sequestro dei dispositivi | Aggiungi Tor, dispositivi dedicati e disciplina operativa nella separazione delle identità |
| **Titolare di piccola impresa** | Compromissione della posta aziendale, frodi su fatture, deviazione dei pagamenti | Verifica ogni trasferimento tramite un canale indipendente |
| **Professionista tecnico** | Catena di fornitura, furto di credenziali, attacchi tramite dipendenze | Aggiungi chiavi hardware, firma del codice e separazione dell'identità lavorativa da quella personale |

**La lettura onesta della tabella.** Per la maggior parte delle persone, la maggior parte del rischio realistico è nei livelli 1 e 2. Gli elementi avanzati sono molto importanti per chi ne ha bisogno e spesso vengono adottati da chi non ne ha.

*La guida **[Come creare il proprio modello di minaccia personale](/articles/how-to-form-your-own-personal-threat-model-safeguard-online-security/)** illustra come fare questa valutazione.*

## Punti chiave

- **L'ordine conta più della completezza.** I cinque punti del livello 1 rimuovono più rischi realistici di una lista completa di 300 elementi eseguita senza un ordine preciso.
- **Passkey e chiavi hardware sono gli unici fattori aggiuntivi che sconfiggono il phishing**, perché la credenziale è associata all'origine e non lascia il dispositivo.
- **I malware infostealer sottraggono direttamente i cookie di sessione**, quindi il furto dei token di sessione spiega perché il fattore più debole non basta da solo.
- **La crittografia trasforma il dispositivo rubato in una perdita hardware**, non in una violazione dei dati. Verifica che sia attiva, perché non è sempre predefinita.
- **Lo spazio sincronizzato non è un backup.** Aggiungi una copia offline o una copia scrivibile e prova un ripristino.
- **Il recupero dell'account è il nuovo punto d'attacco.** Salva i codici di backup offline e separali dal gestore di password.
- **Gli alias interrompono la correlazione** tra tutti i database violati che contengono il tuo indirizzo.
- **La maggior parte delle ottimizzazioni consigliate ha scarso rendimento.** Modifiche all'impronta e user-agent falsi contano molto meno di un gestore di password e degli aggiornamenti automatici.
- **La checklist giusta dipende dal tuo avversario.** Gli elementi avanzati sono importanti per chi ne ha bisogno e spesso vengono adottati da chi non ne ha.

## Prossimi passi

1. **Completa oggi il livello 1**, in circa due ore: gestore di password, secondo fattore resistente al phishing, aggiornamenti automatici, crittografia del dispositivo e un backup verificato.
2. **Approfondisci con una checklist comunitaria** che copre centinaia di elementi in una dozzina di categorie: **[Checklist di sicurezza personale](https://github.com/Lissy93/personal-security-checklist)**.
3. **Usa la versione interattiva** per filtrare per modello di minaccia e monitorare i progressi: **[Difesa digitale](https://digital-defense.io)**.
4. **Applica le checklist organizzative del sito** per gli equivalenti professionali: **[Sicurezza delle password](/checklists/password-security-checklist/)**, **[Consapevolezza del phishing](/checklists/phishing-awareness-checklist/)**, **[Backup e recupero dei dati](/checklists/data-backup-recovery-checklist/)**, **[Sicurezza dei dispositivi mobili](/checklists/mobile-device-security-checklist/)** e **[Sicurezza dei social media](/checklists/social-media-security-checklist/)**.
5. **Scegli il gestore di password** con il confronto architetturale **[Bitwarden contro KeePassXC](/articles/bitwarden-and-keepassxc-vs-the-rest/)**.
6. **Migliora browser** invece di ottimizzarne uno più debole: **[LibreWolf contro Brave e Tor](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/)**.
7. **Proteggi i dati di pagamento** con numeri di carta virtuali: **[Carte virtuali Privacy.com](/articles/privacy-com-virtual-debit-cards-security-privacy/)**.
8. **Usa gli strumenti localmente**, a partire dal **[Generatore di password](/password-generator/)** e dal **[Generatore TOTP](/totp-generator/)**.

## Articoli correlati

| Articolo | Argomento |
|---|---|
| **[Come creare il proprio modello di minaccia personale](/articles/how-to-form-your-own-personal-threat-model-safeguard-online-security/)** | La valutazione che determina il livello adatto a te |
| **[Migliori gestori di password 2026: Bitwarden contro KeePassXC](/articles/bitwarden-and-keepassxc-vs-the-rest/)** | Scelta tra un vault sincronizzato nel cloud e uno offline |
| **[Creare password solide nel 2026](/articles/how-to-create-strong-passwords/)** | Entropia, passphrase e perché la lunghezza conta più della sostituzione dei simboli |
| **[Guida all'autenticazione a più fattori](/articles/what-are-the-diferent-kinds-of-factors-in-mfa/)** | Tassonomia dei fattori alla base del confronto precedente |
| **[Migliori browser per la privacy 2026: LibreWolf contro Brave e Tor](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/)** | Protezione del browser nel livello 3 |
| **[Smartwatch adatti agli appassionati di privacy](/articles/smartwatches-for-privacy-and-security-enthusiasts/)** | Applicare la stessa logica di classificazione ai dispositivi indossabili |
| **[Carte virtuali Privacy.com](/articles/privacy-com-virtual-debit-cards-security-privacy/)** | Limitare l'esposizione dei pagamenti, abbinandola al blocco del credito |

## Riferimenti

1. [Checklist di sicurezza personale, lista comunitaria di Alicia Sykes](https://github.com/Lissy93/personal-security-checklist)
2. [Checklist di sicurezza personale, documento completo](https://github.com/Lissy93/personal-security-checklist/blob/HEAD/CHECKLIST.md)
3. [Difesa digitale, versione interattiva](https://digital-defense.io)
4. [Awesome Privacy, elenco di software rispettoso della privacy](https://github.com/lissy93/awesome-privacy)
5. [Have I Been Pwned, notifiche sulle violazioni](https://haveibeenpwned.com)
6. [FIDO Alliance, specifiche delle passkey e FIDO2](https://fidoalliance.org/passkeys/)
7. [Use Plaintext Email, configurazione dell'e-mail in testo semplice](https://useplaintext.email/)
8. [Consumer Financial Protection Bureau, rapporti e punteggi di credito](https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/)
9. [FTC, consigli per i consumatori sul furto d'identità](https://consumer.ftc.gov/identity-theft-and-online-security)
10. [Passkeys.dev, risorsa comunitaria sull'implementazione delle passkey](https://passkeys.dev/)
