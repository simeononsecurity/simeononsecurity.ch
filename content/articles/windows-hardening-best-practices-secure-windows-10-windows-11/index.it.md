---
title: "Migliori pratiche di base per l'irrobustimento di Windows per la sicurezza di Windows 10 e Windows 11"
date: 2023-07-27
toc: true
draft: false
description: "Scoprite le strategie efficaci per migliorare la sicurezza dei vostri sistemi Windows 10 e Windows 11 attraverso tecniche di hardening complete e best practice."
genre: ["Indurimento delle finestre", "Sicurezza di Windows", "Irrigidimento di Windows 10", "Irrigidimento di Windows 11", "Le migliori pratiche di sicurezza di Windows", "Suggerimenti per la sicurezza di Windows", "Linee guida per la sicurezza di Windows", "Protezione dei sistemi operativi Windows", "Irrigidimento del sistema Windows", "Misure di sicurezza di Windows"]
tags: ["Indurimento delle finestre", "Sicurezza di Windows", "Windows 10", "Windows 11", "sicurezza del sistema operativo", "Windows Defender", "Controllo dell'account utente", "Crittografia BitLocker", "configurazione del firewall", "Politiche di AppLocker", "Aggiornamenti di Windows", "password forti", "backup dei dati", "Windows Hello", "Avvio sicuro", "TPM", "Microsoft Defender Antivirus", "Sandbox di Windows", "Microsoft Defender Application Guard", "Accesso controllato alle cartelle", "Migliori pratiche per la protezione di Windows 10 e Windows 11", "Come rendere più resistenti i sistemi operativi Windows", "Misure di sicurezza di Windows per individui e organizzazioni", "Migliorare la sicurezza del sistema Windows", "Protezione dei dati con la crittografia BitLocker", "Isolamento delle sessioni del browser con Microsoft Defender Application Guard", "Consigli e linee guida per la sicurezza di Windows 10", "Implementazione delle funzioni di sicurezza di Windows", "Protezione di Windows con l'isolamento basato sull'hardware", "Garantire l'integrità del sistema Windows"]
cover: "/img/cover/A_cartoon_illustration_of_a_shield_protecting-windows.png"
coverAlt: "Illustrazione a fumetti di uno scudo che protegge il logo di Windows da varie minacce informatiche."
coverCaption: "Proteggete la vostra fortezza Windows con efficaci tecniche di hardening."
---

## Introduzione

I sistemi operativi Windows sono ampiamente utilizzati da individui e organizzazioni in tutto il mondo. Per garantire la sicurezza e l'integrità di questi sistemi, è essenziale implementare le **migliori pratiche di hardening di Windows**. L'hardening consiste nel mettere in sicurezza il sistema operativo riducendo la sua superficie di attacco e mitigando le potenziali vulnerabilità. Questo articolo esplorerà le best practice per l'hardening dei sistemi operativi **Windows 10** e del più recente **Windows 11**, fornendo indicazioni preziose per migliorare la sicurezza del vostro ambiente Windows.

______

## Capire l'hardening di Windows

L'hardening di Windows è il processo di rafforzamento della sicurezza di un sistema operativo Windows. Comporta la configurazione di varie impostazioni e l'implementazione di misure di sicurezza per proteggere da accessi non autorizzati, malware e altre minacce. L'hardening del sistema Windows consente di ridurre al minimo i rischi associati agli attacchi informatici e di garantire la riservatezza, l'integrità e la disponibilità dei dati.

### [Hardening Windows 10](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

Windows 10 è uno dei sistemi operativi più utilizzati a livello globale. Per rendere più sicuro il vostro ambiente Windows 10, considerate le seguenti best practice:

#### 1. [**Enable Windows Defender**](https://github.com/simeononsecurity/Windows-Defender-Hardening)

Windows Defender è una **soluzione antivirus** robusta inclusa in Windows 10. Offre una serie di funzioni di sicurezza per proteggere il sistema da vari tipi di **malware**, tra cui **virus, spyware e ransomware**. Attivando Windows Defender, è possibile migliorare notevolmente la sicurezza dell'ambiente Windows 10.

Per attivare Windows Defender, procedere come segue:

- Aprire l'applicazione **Windows Security** facendo clic sull'icona Windows Security nella barra delle applicazioni o cercando "Windows Security" nel menu Start.
- Nell'applicazione Windows Security, fare clic su "**Protezione da virus e minacce**" nel riquadro di navigazione a sinistra.
- Fare clic su "**Gestione impostazioni**" nella sezione "Impostazioni di protezione da virus e minacce".
- Assicuratevi che l'interruttore "**Protezione in tempo reale**" sia impostato su "**Acceso**". In questo modo Windows Defender esegue una scansione attiva e protegge il sistema in tempo reale.
- Inoltre, è possibile personalizzare le opzioni di scansione e le esclusioni facendo clic rispettivamente su "**Opzioni di scansione**" e "**Aggiungi o rimuovi esclusioni**".

È fondamentale aggiornare **regolarmente** Windows Defender per assicurarsi che disponga delle più recenti **definizioni di malware** e **miglioramenti della sicurezza**. Microsoft rilascia regolarmente aggiornamenti per affrontare nuove minacce e vulnerabilità. Per aggiornare Windows Defender, è possibile seguire i seguenti passaggi:

- Aprire l'applicazione Sicurezza di Windows.
- Andate su "**Protezione da virus e minacce**" nel riquadro di navigazione a sinistra.
- Fare clic su "**Verifica aggiornamenti**" nella sezione "Aggiornamenti protezione da virus e minacce".
- Windows controllerà gli aggiornamenti disponibili e li scaricherà/installerà se necessario.

Attivando e mantenendo aggiornato Windows Defender, è possibile proteggere in modo proattivo il sistema Windows 10 da malware e altre minacce alla sicurezza. Si consiglia inoltre di eseguire **scansioni regolari del sistema** utilizzando Windows Defender per garantire il rilevamento e la rimozione di qualsiasi potenziale minaccia.

Ricordate che, sebbene Windows Defender fornisca un solido livello di protezione, è essenziale integrarlo con **abitudini di navigazione sicure**, **aggiornamenti software regolari** e altre misure di sicurezza per mantenere un ambiente Windows 10 sicuro.

#### 2. [**Keep Windows 10 Updated**](https://support.microsoft.com/en-us/windows/windows-update-faq-8a903416-6f45-0718-f5c7-375e92dddeb2)
L'installazione regolare degli aggiornamenti di Windows è un aspetto critico del **mantenimento di Windows 10**. Questi aggiornamenti includono **patch di sicurezza**, correzioni di bug e miglioramenti delle prestazioni che aiutano a **coprire le vulnerabilità di sicurezza** e a migliorare la stabilità del sistema.

Microsoft rilascia **aggiornamenti regolari** per Windows 10 per risolvere i problemi di sicurezza appena scoperti e migliorare l'esperienza complessiva dell'utente. Mantenendo il sistema aggiornato, ci si assicura che il sistema operativo disponga degli ultimi **miglioramenti della sicurezza** per difendersi dalle minacce emergenti.

Per mantenere aggiornato Windows 10, è possibile seguire i seguenti passaggi:

1. **Attivare gli aggiornamenti automatici**: Per impostazione predefinita, Windows 10 è configurato per scaricare e installare automaticamente gli aggiornamenti. Ciò garantisce che il sistema riceva gli aggiornamenti necessari senza alcun intervento manuale. Per verificare se gli aggiornamenti automatici sono abilitati, procedere come segue:
   - Accedere a **Impostazioni** facendo clic sul menu Start e selezionando l'icona a forma di ingranaggio.
   - Fare clic su **Aggiornamento e sicurezza**.
   - Nel riquadro di navigazione di sinistra, fare clic su **Windows Update**.
   - Assicurarsi che l'opzione **"Automatico "** sia selezionata in **"Impostazioni di Windows Update "**. Se non è selezionata, fare clic sul link **"Cambia ore attive "** per personalizzare le ore in cui Windows deve evitare di installare gli aggiornamenti.

2. **Installazione manuale degli aggiornamenti**: Se si preferisce avere un maggiore controllo sul processo di aggiornamento, è possibile installare manualmente gli aggiornamenti sul sistema Windows 10. Ecco come fare. Ecco come fare:
   - Andate in **Impostazioni** > **Aggiornamento e sicurezza** > **Windows Update**.
   - Fare clic su **"Verifica aggiornamenti "** per vedere se sono disponibili aggiornamenti per il sistema.
   - Se sono presenti aggiornamenti, fare clic su **"Scarica "** e **"Installa "** per avviare il processo di installazione.

È fondamentale sottolineare l'importanza di **riavviare regolarmente il sistema** dopo l'installazione degli aggiornamenti. Alcuni aggiornamenti possono richiedere il riavvio del sistema per applicare completamente le modifiche e garantirne l'efficacia.

Mantenendo il sistema Windows 10 aggiornato**, non solo si aumenta la sua sicurezza, ma si beneficia anche delle funzioni più recenti, dei miglioramenti delle prestazioni e delle correzioni di compatibilità. Si tratta di una misura proattiva per garantire che il sistema rimanga resistente alle potenziali minacce alla sicurezza.

#### 3. [**Configure User Account Control (UAC)**](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-overview)
Il Controllo dell'account utente (UAC) è una funzione di sicurezza di Windows 10 che aiuta a prevenire modifiche non autorizzate al sistema richiedendo l'approvazione dell'amministratore quando necessario. Agisce come una salvaguardia contro il software dannoso o gli utenti non autorizzati che tentano di apportare modifiche che potrebbero avere un impatto sulla sicurezza o sulla stabilità del sistema.

La configurazione delle impostazioni UAC a un livello appropriato è cruciale per **tutelare Windows 10**. Si tratta di trovare un equilibrio tra sicurezza e usabilità per garantire che l'UAC protegga efficacemente il sistema senza causare interruzioni inutili.

Per configurare le impostazioni UAC in Windows 10, potete seguire i seguenti passaggi:

1. Aprite il **Pannello di controllo** digitando "Pannello di controllo" nella barra di ricerca e selezionandolo dai risultati della ricerca.

2. Nel Pannello di controllo, fare clic su **"Account utente "**.

3. Fare clic su **"Modifica delle impostazioni di controllo dell'account utente "**.

4. Verrà visualizzato un cursore con diversi livelli di impostazioni UAC. Ecco le opzioni disponibili:
   - **"Notifica sempre "**: È il livello più alto di sicurezza UAC, in cui viene richiesto il consenso per qualsiasi modifica al sistema, anche per attività semplici.
   - **"Notifica solo quando le applicazioni cercano di apportare modifiche al computer (impostazione predefinita) "**: È l'impostazione consigliata che offre un equilibrio tra sicurezza e usabilità. Viene richiesto il consenso quando le app apportano modifiche, ma non per le modifiche alle impostazioni di Windows.
   - **"Avvisami solo quando le app cercano di apportare modifiche al computer (non oscurare il desktop) "**: Simile all'opzione precedente, ma il desktop non viene oscurato quando vengono visualizzati i messaggi UAC.
   - **"Non notificare mai "**: Si tratta del livello più basso di sicurezza UAC, in cui non viene richiesta alcuna modifica al sistema.

5. Scegliere il livello di sicurezza UAC più adatto alle proprie esigenze spostando il cursore nella posizione desiderata.

6. Fare clic su **"OK "** per salvare le modifiche.

Si consiglia di mantenere l'UAC abilitato e di impostarlo a un livello che garantisca un equilibrio adeguato tra sicurezza e usabilità. Disattivare completamente l'UAC può rendere il sistema più vulnerabile a modifiche non autorizzate e potenzialmente comprometterne la sicurezza.

Configurando le impostazioni UAC, si migliora la sicurezza del sistema Windows 10 assicurando che i privilegi amministrativi siano richiesti per le modifiche critiche del sistema, riducendo il rischio di accesso non autorizzato e di infezioni da malware.

#### 4. [**Use Strong Passwords**](https://simeononsecurity.com/articles/how-to-create-strong-passwords/)
L'uso di password forti è essenziale per mantenere la sicurezza del sistema Windows 10 e per proteggersi da accessi non autorizzati. Le password deboli o facilmente indovinabili possono rendere il sistema vulnerabile agli attacchi, come gli attacchi brute-force o il cracking delle password.

Per garantire che tutti gli account utente del sistema Windows 10 abbiano password forti, seguite queste best practice per le password:

1. **Complessità**: Incoraggiate gli utenti a creare password complesse e non facilmente indovinabili. Una password forte dovrebbe includere una combinazione di lettere maiuscole e minuscole, numeri e caratteri speciali. Evitate di usare parole comuni o schemi prevedibili.

2. **Lunghezza**: Le password più lunghe sono generalmente più sicure. Incoraggiate gli utenti a creare password di almeno 8 caratteri, ma preferibilmente più lunghe. Più caratteri ci sono in una password, più è difficile da decifrare.

3. **Univocità**: Ogni account utente deve avere una password unica. L'uso della stessa password per più account aumenta il rischio di violazione della sicurezza. Incoraggiate gli utenti a utilizzare password diverse per account diversi.

4. **Evitare le informazioni personali**: Sconsigliate agli utenti di utilizzare informazioni personali come nomi, date di nascita o indirizzi nelle loro password. Queste informazioni possono essere facilmente ottenute o indovinate dagli aggressori.

5. **Gestori di password**: Considerate l'utilizzo di uno strumento di gestione delle password per memorizzarle e gestirle in modo sicuro. I gestori di password possono generare password forti e uniche per ogni account e memorizzarle in un database crittografato.

6. **Cambiare regolarmente le password**: Incoraggiate gli utenti a cambiare periodicamente le password per mantenere la sicurezza. Stabilite una politica di scadenza delle password ed educate gli utenti all'importanza di aggiornarle regolarmente.

L'implementazione di pratiche di password solide migliora significativamente la sicurezza del sistema Windows 10 e riduce il rischio di accesso non autorizzato o di violazione dei dati. Istruite regolarmente gli utenti sulla sicurezza delle password e fornite risorse, come i misuratori di forza delle password o le linee guida per la loro creazione, per aiutarli a creare password forti.

Per informazioni più dettagliate sulla creazione di password forti e sulle migliori pratiche, potete consultare questo articolo [article](https://simeononsecurity.com/articles/how-to-create-strong-passwords/) Fornisce una guida completa sulla sicurezza delle password e offre suggerimenti per la creazione di password forti e memorabili.

Ricordate che l'utilizzo di password forti è un aspetto fondamentale della sicurezza del sistema e deve essere considerato prioritario per proteggere i dati sensibili e garantire l'integrità dell'ambiente Windows 10.

#### 5. [**Enable BitLocker Encryption**](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)
Uno dei modi più efficaci per proteggere i dati sensibili sul sistema Windows 10 è attivare la crittografia BitLocker. BitLocker fornisce la crittografia dell'intero disco, garantendo che anche in caso di smarrimento o furto del dispositivo, i dati rimangano al sicuro e inaccessibili a persone non autorizzate.

Per attivare la crittografia BitLocker e salvaguardare i vostri dati sensibili, seguite questi passaggi:

1. **Controllare i requisiti di sistema**: Assicuratevi che la vostra edizione di Windows 10 supporti la crittografia BitLocker. BitLocker è disponibile nelle edizioni Windows 10 Pro, Enterprise e Education.

2. **Abilitare BitLocker**: Aprire il Pannello di controllo e navigare nella categoria "Sistema e sicurezza". Fare clic su "Crittografia unità BitLocker" e selezionare le unità da crittografare. Seguire le istruzioni sullo schermo per avviare il processo di crittografia.

3. **Scegliere le opzioni di crittografia**: Durante la configurazione di BitLocker, è possibile scegliere tra diversi metodi di crittografia, come l'uso di una password, di una smart card o di entrambi. Selezionare il metodo appropriato in base ai requisiti e alle preferenze di sicurezza.

4. **Chiave di ripristino di backup**: È fondamentale eseguire il backup della chiave di ripristino BitLocker. Questa chiave funge da sicurezza in caso di dimenticanza della password o di problemi di accesso all'unità crittografata. Conservare la chiave di ripristino in un luogo sicuro, separato dal dispositivo.

5. **Gestione delle impostazioni di BitLocker**: Dopo aver abilitato BitLocker, è possibile personalizzare altre impostazioni, come lo sblocco automatico per unità specifiche o la configurazione dell'uso di TPM (Trusted Platform Module) per una maggiore sicurezza. Queste impostazioni sono accessibili attraverso l'interfaccia di gestione di BitLocker.

Attivando la crittografia BitLocker, si aggiunge un ulteriore livello di protezione al sistema Windows 10, garantendo che anche se il dispositivo cade nelle mani sbagliate, i dati rimangano al sicuro e inaccessibili. È importante aggiornare e mantenere regolarmente le impostazioni di BitLocker per rimanere al passo con le migliori pratiche di sicurezza.

Per informazioni più dettagliate sull'abilitazione e la gestione della crittografia BitLocker, è possibile consultare il sito ufficiale [Microsoft documentation](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview) Fornisce una guida completa sulla crittografia BitLocker, comprese le funzioni avanzate e le opzioni di configurazione.

Ricordate che l'attivazione della crittografia BitLocker aiuta a salvaguardare i vostri dati sensibili e garantisce la tranquillità di sapere che le vostre informazioni sono al sicuro anche in caso di perdita o furto.

#### 6. **Disabilitazione di servizi e funzioni non necessari**
Per migliorare la sicurezza del sistema Windows 10, è essenziale rivedere e disattivare tutti i servizi e le funzioni non necessari. In questo modo, si riduce la superficie di attacco e il potenziale di sfruttamento da parte di malintenzionati.

Ecco i passaggi per disabilitare i servizi e le funzioni non necessari sul sistema Windows 10:

1. **Identificare i servizi non necessari**: Iniziate identificando i servizi in esecuzione sul vostro sistema. Aprite la console di gestione "Servizi" premendo **Tasto Windows + R**, digitando **services.msc** e premendo **Invio**. Esaminare l'elenco dei servizi e ricercare il loro scopo per determinare quali sono essenziali per la funzionalità del sistema.

2. **Disabilitare i servizi non necessari**: Una volta identificati i servizi non necessari, fate clic con il tasto destro del mouse su ciascun servizio e selezionate **Proprietà**. Nella finestra delle proprietà, modificare il **tipo di avvio** in **Disabilitato**. In questo modo si evita che il servizio si avvii automaticamente all'avvio del sistema. Prestare attenzione e assicurarsi di disabilitare solo i servizi non necessari per il normale funzionamento del sistema.

3. **Disabilita le funzioni non necessarie**: Oltre ai servizi, Windows 10 include anche varie funzioni che potrebbero non essere necessarie per il sistema. Aprire il **Pannello di controllo**, spostarsi su **Programmi** o **Programmi e funzionalità** e fare clic su **Attiva o disattiva funzionalità di Windows**. Deselezionare le funzioni non necessarie. Questo passo contribuisce a ridurre ulteriormente la superficie di attacco e a minimizzare le risorse consumate dalle funzioni non necessarie.

4. **Rivedere e aggiornare regolarmente**: È fondamentale rivedere regolarmente l'elenco dei servizi e delle funzionalità abilitate sul sistema Windows 10. Poiché i requisiti del sistema cambiano nel tempo, potrebbe essere necessario rivalutare i servizi e le funzionalità necessarie. Rimanete vigili e aggiornate la configurazione se necessario.

Disattivando i servizi e le funzioni non necessari, si limitano i potenziali punti di accesso per gli aggressori e si riduce la superficie di attacco complessiva del sistema Windows 10. Questa pratica migliora il sistema. Questa pratica migliora la sicurezza del sistema e riduce il rischio di sfruttamento.

Per ulteriori informazioni sulla gestione dei servizi e delle funzionalità in Windows 10, potete consultare le seguenti informazioni [article](https://www.tweakhound.com/2015/07/27/windows-10-default-services/#:~:text=Windows%2010%20Default%20Services%20%20%20%20Name,%20%20%20%2044%20more%20rows%20) per una guida dettagliata.

È importante prestare attenzione quando si disattivano servizi e funzioni, poiché la disattivazione di componenti essenziali può avere un impatto negativo sulla funzionalità del sistema. Prima di apportare qualsiasi modifica, è necessario informarsi e comprendere lo scopo di un servizio o di una funzione.

#### 7. **Implementare le regole del firewall**
Il firewall integrato in Windows 10 funge da linea di difesa fondamentale contro il traffico di rete non autorizzato. Configurando le regole del firewall, è possibile controllare quali connessioni in entrata e in uscita sono consentite, migliorando così la sicurezza del sistema.

Seguite questi passaggi per implementare le regole del firewall sul vostro sistema Windows 10:

1. **Accedere alle impostazioni del firewall**: Per accedere alle impostazioni del firewall, aprire il **Pannello di controllo**, cercare **Windows Defender Firewall** e fare clic sul risultato corrispondente. In alternativa, è possibile fare clic con il pulsante destro del mouse su **Avvio**, selezionare **Impostazioni** e spostarsi su **Rete e Internet > Windows Firewall**.

2. **Configurare le regole in entrata**: Le regole in entrata controllano le connessioni di rete in entrata al sistema. Fare clic su **Impostazioni avanzate** nella finestra di Windows Defender Firewall. Nella nuova finestra, selezionare **Regole in entrata** e fare clic su **Nuova regola**. Seguite le istruzioni sullo schermo per creare regole che consentano solo le connessioni in entrata necessarie. Considerate i servizi e le applicazioni che richiedono l'accesso alla rete e create le regole di conseguenza.

3. **Configurare le regole in uscita**: Le regole in uscita controllano le connessioni di rete in uscita dal sistema. Seguite la stessa procedura di cui sopra, ma selezionate **Regole in uscita**. Creare regole per consentire le connessioni in uscita per i servizi e le applicazioni essenziali e bloccare quelle sospette o non necessarie.

4. **Rivedere e aggiornare regolarmente**: È importante rivedere e aggiornare regolarmente le regole del firewall per garantire che siano in linea con i requisiti del sistema. Quando l'ambiente di rete e i modelli di utilizzo cambiano, potrebbe essere necessario modificare o creare nuove regole. Rimanete vigili e aggiornate le regole per mantenere una configurazione efficace del firewall.

L'implementazione e la manutenzione delle regole del firewall consentono di ridurre significativamente il rischio di accesso non autorizzato alla rete e di migliorare la sicurezza del sistema Windows 10. Inoltre, considerate la possibilità di attivare l'opzione **Modalità segreta** nelle impostazioni del firewall per rendere il vostro sistema meno visibile ai potenziali aggressori.

Per informazioni più dettagliate sulla configurazione delle regole del firewall in Windows 10, è possibile consultare la guida ufficiale [Microsoft documentation](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/best-practices-configuring) per le istruzioni passo-passo.

Ricordate che un firewall ben configurato è un componente essenziale di una strategia di sicurezza completa, ma deve essere utilizzato insieme ad altre misure di sicurezza per garantire una solida protezione del sistema.

#### 8. [**Use AppLocker**](https://github.com/simeononsecurity/AppLocker)
AppLocker è una potente funzione di Windows 10 che consente di controllare quali applicazioni possono essere eseguite sul sistema. Implementando i criteri di AppLocker, è possibile limitare l'esecuzione di applicazioni non autorizzate o potenzialmente dannose, migliorando la sicurezza del vostro ambiente Windows 10.

Seguite questi passaggi per utilizzare AppLocker sul vostro sistema Windows 10:

1. **Accedere alle impostazioni di AppLocker**: Per accedere alle impostazioni di AppLocker, aprire il **Local Group Policy Editor** premendo **Tasto Windows + R**, digitando **gpedit.msc** e facendo clic su **OK**. In alternativa, è possibile cercare **Group Policy Editor** nel menu **Start**.

2. **Configurare i criteri di AppLocker**: Nell'Editor Criteri di gruppo locali, passare a **Configurazione del computer > Impostazioni di Windows > Impostazioni di sicurezza > Criteri di controllo delle applicazioni > AppLocker**. Qui è possibile configurare vari criteri come **Regole eseguibili**, **Regole del programma di installazione di Windows**, **Regole di script** e **Regole delle app confezionate**.

3. **Creare regole AppLocker**: Per creare una regola AppLocker, fare clic con il pulsante destro del mouse sulla cartella del criterio desiderato (ad esempio, **Regole eseguibili**) e selezionare **Crea nuova regola**. Seguire le istruzioni visualizzate per specificare le condizioni e le eccezioni della regola. È possibile creare regole basate sul percorso del file, sull'editore, sull'hash del file o su altri attributi per consentire o negare l'esecuzione dell'applicazione.

4. **Test e perfezionamento dei criteri**: Dopo aver creato le regole di AppLocker, è importante testarle per assicurarsi che funzionino come previsto. Distribuite i criteri in un gruppo o sistema di prova e verificate che solo le applicazioni autorizzate possano essere eseguite. Apportate i necessari perfezionamenti alle regole in base ai risultati dei test.

5. **Revisione e aggiornamento periodici**: Con l'evolversi del panorama applicativo, è fondamentale rivedere e aggiornare regolarmente i criteri di AppLocker. Nuove applicazioni possono richiedere l'autorizzazione all'esecuzione, mentre altre possono diventare obsolete o presentare rischi per la sicurezza. Rimanete proattivi e aggiornate le vostre politiche per mantenere un efficace meccanismo di controllo delle applicazioni.

AppLocker fornisce un controllo granulare sull'esecuzione delle applicazioni, aiutandovi a prevenire l'esecuzione di software non autorizzato o dannoso sul vostro sistema Windows 10. Utilizzando AppLocker, è possibile ridurre il rischio di infezioni da malware, installazioni di software non autorizzate e altri incidenti di sicurezza.

Per informazioni più dettagliate sull'implementazione dei criteri di AppLocker, è possibile consultare il sito ufficiale di AppLocker. [Microsoft documentation](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/applocker-overview) or visit our [AppLocker GitHub repository](https://github.com/simeononsecurity/AppLocker) per ulteriori risorse ed esempi.

Ricordate di rivedere e aggiornare regolarmente i criteri di AppLocker per adattarli ai mutevoli requisiti delle applicazioni e alle nuove minacce alla sicurezza. AppLocker è uno strumento prezioso per difendersi dalle applicazioni non autorizzate e potenzialmente dannose sul sistema Windows 10.

#### 9. [**Regularly Backup Your Data**](https://simeononsecurity.com/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/)
Eseguire regolarmente il backup dei dati è una pratica essenziale per proteggersi dalla perdita di dati causata da incidenti di sicurezza, guasti hardware o altri eventi imprevisti. Creando backup regolari e verificandone l'integrità, è possibile garantire che i dati importanti rimangano al sicuro e possano essere ripristinati in caso di disastro.

Seguite questi passaggi per eseguire regolarmente il backup dei vostri dati su un sistema Windows 10:

1. **Identificare i dati critici**: Iniziare a identificare i dati critici di cui è necessario eseguire il backup. Questi possono includere documenti importanti, file personali, configurazioni di sistema, impostazioni di applicazioni e qualsiasi altro dato che si ritiene prezioso.

2. **Scegliere una soluzione di backup**: Selezionate una soluzione di backup affidabile che soddisfi i vostri requisiti. Windows 10 offre strumenti di backup integrati come **Cronologia file** e **Windows Backup e ripristino**. In alternativa, si può optare per un software di backup di terze parti che offre ulteriori funzioni e flessibilità.

3. **Definire la frequenza di backup**: Stabilite la frequenza con cui eseguire i backup in base alla criticità dei dati e alla frequenza delle modifiche. Alcuni dati possono richiedere backup giornalieri, mentre altri possono essere sottoposti a backup settimanali o mensili.

4. **Selezione dell'archiviazione di backup**: Scegliere un supporto di memorizzazione adatto per archiviare i backup. Può trattarsi di dischi rigidi esterni, dispositivi NAS (Network Attached Storage), servizi di cloud storage o una combinazione di più opzioni di archiviazione. Assicurarsi che il supporto di archiviazione sia sicuro e affidabile.

5. **Configurazione delle impostazioni di backup**: Impostare la soluzione di backup in base alle proprie preferenze. Specificare i dati di cui eseguire il backup, la destinazione del backup ed eventuali impostazioni aggiuntive come la crittografia o la compressione.

6. **Eseguire ripristini di prova**: Verificate regolarmente il processo di ripristino eseguendo dei ripristini di prova dai vostri backup. Questo assicura che i backup funzionino correttamente e che sia possibile ripristinare i dati in caso di necessità.

7. **Monitoraggio e aggiornamento**: Monitorate regolarmente il processo di backup per assicurarvi che funzioni come previsto. Aggiornare la soluzione di backup e regolare le impostazioni di backup in base alle modifiche dei dati e dei requisiti.

Seguendo questi passaggi e attenendosi a una routine di backup regolare, è possibile ridurre al minimo l'impatto della perdita di dati e mantenere la disponibilità delle informazioni importanti. Ricordate di conservare i backup in modo sicuro, lontano dai dati originali, e prendete in considerazione l'implementazione della regola del **3-2-1 backup**, che prevede almeno tre copie dei vostri dati, archiviate su due diversi supporti di memorizzazione, con una copia conservata fuori sede.

Per informazioni più dettagliate sulle migliori pratiche di backup e sulla regola del **3-2-1 backup**, potete consultare l'articolo su [What is the 3-2-1 Backup Rule and Why You Should Use It](https://simeononsecurity.com/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/) Fornisce indicazioni e raccomandazioni preziose per l'implementazione di una strategia di backup efficace.

Ricordate che i backup regolari sono fondamentali per salvaguardare i vostri dati e garantirne la disponibilità in caso di eventi imprevisti. Fate in modo che il backup dei dati sia parte integrante dei vostri sforzi di hardening di Windows 10 per proteggere le vostre preziose informazioni.

______

{{< inarticle-dark >}}


### [Hardening Windows 11](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

Windows 11 è l'ultima versione del sistema operativo Windows, che offre funzionalità avanzate e una maggiore sicurezza. Per rendere più sicuro il vostro ambiente Windows 11, considerate le seguenti best practice:

#### 1. **Secure Boot e TPM**
Secure Boot e TPM (Trusted Platform Module) sono funzioni di sicurezza essenziali disponibili in Windows 11 che aiutano a proteggere da accessi non autorizzati e a garantire l'integrità del sistema operativo. Abilitando il Secure Boot e il TPM, è possibile migliorare la sicurezza del sistema Windows 11.

Seguite questi passaggi per abilitare Secure Boot e TPM sul vostro dispositivo Windows 11:

1. **Verifica della compatibilità**: Prima di abilitare Secure Boot e TPM, assicuratevi che il vostro dispositivo supporti queste funzionalità. Verificare che l'hardware e il firmware del sistema soddisfino i requisiti per la funzionalità Secure Boot e TPM.

2. **Accesso alle impostazioni UEFI/BIOS**: Riavviare il dispositivo Windows 11 e accedere alle impostazioni UEFI (Unified Extensible Firmware Interface) o BIOS (Basic Input/Output System). Il tasto specifico o la combinazione di tasti per accedere a queste impostazioni può variare a seconda del dispositivo. I tasti più comuni sono Del, F2, F10 o Esc. Per istruzioni dettagliate, consultare la documentazione del dispositivo o il sito Web del produttore.

3. **Abilitare l'avvio sicuro**: Una volta entrati nelle impostazioni UEFI/BIOS, navigare fino alle impostazioni Secure Boot. Abilitare l'avvio sicuro per garantire che solo i sistemi operativi e i componenti affidabili possano essere eseguiti durante il processo di avvio. In questo modo si impedisce il caricamento di software non autorizzato o dannoso che potrebbe compromettere la sicurezza del sistema.

4. **Abilita TPM**: Individuare le impostazioni TPM nell'UEFI/BIOS e abilitare il TPM. Il TPM è un microchip dedicato sulla scheda madre del dispositivo che fornisce funzioni di sicurezza basate sull'hardware. L'abilitazione del TPM consente a Windows 11 di sfruttare le sue capacità per migliorare la sicurezza del sistema.

5. **Configura sicurezza TPM**: Dopo aver abilitato il TPM, è possibile disporre di ulteriori opzioni per configurare le impostazioni di sicurezza. A seconda del dispositivo e del firmware, è possibile impostare una password TPM, abilitare gli aggiornamenti del firmware TPM o regolare altre impostazioni correlate. Esaminare le opzioni disponibili e configurarle in base ai propri requisiti di sicurezza.

6. **Salva ed esci**: Dopo aver abilitato Secure Boot e TPM e aver effettuato le configurazioni necessarie, salvare le modifiche nelle impostazioni UEFI/BIOS e uscire. Il sistema si riavvia e le nuove impostazioni diventano effettive.

L'abilitazione di Secure Boot e TPM in Windows 11 aiuta a proteggere il dispositivo da modifiche non autorizzate, rootkit e altre minacce alla sicurezza. Queste funzioni creano una base di fiducia per il sistema operativo e contribuiscono a un ambiente informatico più sicuro.

Si noti che la disponibilità e i passaggi specifici per abilitare Secure Boot e TPM possono variare a seconda del produttore e della versione del firmware del dispositivo. Si consiglia di consultare la documentazione del dispositivo o il sito web del produttore per ottenere istruzioni precise e adatte al proprio sistema.

Abilitando Secure Boot e TPM sul dispositivo Windows 11, si migliora la sicurezza generale e si rafforza la protezione del sistema operativo e dei dati sensibili.

#### 2. [**Enable Microsoft Defender Antivirus**](https://github.com/simeononsecurity/Windows-Defender-Hardening)
Windows 11 è dotato di una protezione antivirus integrata chiamata **Microsoft Defender Antivirus**. Offre una protezione completa contro vari tipi di **malware**, tra cui virus, ransomware e spyware. Abilitando** e **aggiornando regolarmente** Microsoft Defender Antivirus, è possibile garantire il **rilevamento e la prevenzione** delle minacce in tempo reale sul proprio sistema Windows 11.

Seguire questi passaggi per abilitare e aggiornare Microsoft Defender Antivirus sul dispositivo Windows 11:

1. **Controllo dello stato dell'antivirus**: Innanzitutto, verificare lo stato di Microsoft Defender Antivirus sul sistema. Aprite l'applicazione **Windows Security** facendo clic sul menu Start, cercando "Windows Security" e selezionando l'applicazione dai risultati della ricerca. Una volta aperta l'applicazione, passare alla sezione **"Protezione da virus e minacce "** per verificare lo stato di Microsoft Defender Antivirus. Dovrebbe essere **abilitato** per impostazione predefinita su una nuova installazione di Windows 11.

2. **Attivare la protezione in tempo reale**: Nell'applicazione Sicurezza di Windows, assicuratevi che la **protezione in tempo reale** sia abilitata per Microsoft Defender Antivirus. La protezione in tempo reale monitora continuamente il sistema alla ricerca di malware e altre attività dannose, fornendo una **risposta immediata** e **bloccando le minacce** in tempo reale. Se la protezione in tempo reale non è abilitata, fare clic sull'interruttore a levetta** per attivarla.

3. **Aggiornamento delle definizioni**: L'aggiornamento regolare delle **definizioni del virus** è fondamentale per garantire che Microsoft Defender Antivirus sia in grado di rilevare e proteggere dalle minacce più recenti. Nell'app Sicurezza di Windows, passare alla sezione **"Protezione da virus e minacce "** e fare clic sul pulsante **"Verifica aggiornamenti "** per aggiornare le definizioni antivirus. Questo processo assicura che il sistema sia dotato delle **firme** e delle **capacità di rilevamento** più recenti.

4. **Pianificazione delle scansioni**: Microsoft Defender Antivirus consente di pianificare regolari **scansioni del sistema** per rilevare e rimuovere in modo proattivo qualsiasi potenziale minaccia. Nell'app Sicurezza di Windows, accedere alla sezione **"Protezione da virus e minacce "** e fare clic sull'opzione **"Scansione rapida "** o **"Scansione completa "** per avviare una scansione. È inoltre possibile fare clic sul link **"Opzioni di scansione "** per personalizzare le impostazioni di scansione e pianificare scansioni regolari in base alle proprie preferenze.

5. **Configurazione di impostazioni aggiuntive**: Microsoft Defender Antivirus offre impostazioni e funzioni aggiuntive che possono essere configurate in base alle proprie esigenze di sicurezza. Nell'app Sicurezza di Windows, esplorare le varie sezioni come **"Controllo app e browser", "Sicurezza del dispositivo "** e **"Firewall e protezione di rete "** per personalizzare le impostazioni antivirus e sfruttare le funzioni di protezione avanzate.

L'attivazione e l'aggiornamento regolare di Microsoft Defender Antivirus in Windows 11 sono essenziali per mantenere una solida difesa contro il malware e altre minacce alla sicurezza. Seguendo questi passaggi e mantenendo Microsoft Defender Antivirus aggiornato, è possibile garantire che il sistema Windows 11 sia ben protetto.

Sebbene Microsoft Defender Antivirus fornisca una solida protezione, è sempre consigliabile praticare **abitudini di navigazione sicure**, prestare attenzione durante lo **scarico di file** o l'apertura di allegati di posta elettronica** e mantenere il **sistema operativo e le applicazioni aggiornate** per migliorare ulteriormente la sicurezza generale.

#### 3. **Applicare l'isolamento predefinito basato sull'hardware**
Windows 11 sfrutta funzioni di isolamento basate sull'hardware come **Virtualization-based Security (VBS)** e **Hypervisor-protected Code Integrity (HVCI)** per fornire una maggiore sicurezza e proteggere i componenti critici del sistema.

Abilitando e applicando queste funzioni di isolamento predefinite basate sull'hardware, è possibile stabilire solidi confini di sicurezza e mitigare vari vettori di attacco. Ecco alcuni passaggi chiave per garantire la corretta configurazione:

1. **Abilitare la tecnologia di virtualizzazione**: Innanzitutto, è necessario verificare se il sistema supporta la tecnologia di virtualizzazione e assicurarsi che sia abilitata nelle impostazioni del **BIOS** o del **UEFI** del sistema. I passaggi per accedere e abilitare la tecnologia di virtualizzazione possono variare a seconda del produttore della scheda madre o del firmware. Per istruzioni specifiche, consultare la documentazione del sistema o il sito Web del produttore.

2. **Abilitare la sicurezza basata sulla virtualizzazione (VBS)**: Windows 11 incorpora VBS, che utilizza le funzionalità di virtualizzazione hardware per creare contenitori isolati chiamati **Virtual Secure Mode (VSM)**. La VSM fornisce un ambiente di esecuzione sicuro per i componenti critici del sistema, proteggendoli da potenziali attacchi. Per abilitare la VBS, procedere come segue:

   - Premere il tasto **Windows + R** per aprire la finestra di dialogo Esegui.
   - Digitare "**gpedit.msc**" e premere **Invio** per aprire l'Editor criteri di gruppo locali.
   - Passare a **Configurazione del computer -> Modelli amministrativi -> Sistema -> Device Guard**.
   - Fare doppio clic sul criterio **"Attiva sicurezza basata sulla virtualizzazione "**.
   - Selezionare **"Abilitato "** e fare clic su **OK** per applicare le modifiche.

   L'abilitazione di VBS può richiedere hardware compatibile e alcuni requisiti di sistema. Per ulteriori informazioni, consultare la documentazione ufficiale **Microsoft**.

3. **Abilitare l'integrità del codice protetto dall'hypervisor (HVCI)**: HVCI è una funzione che utilizza l'hypervisor per applicare le politiche di integrità del codice, impedendo l'esecuzione di codice non autorizzato e migliorando la sicurezza generale. Per abilitare HVCI, procedere come segue:

   - Premere il tasto **Windows + R** per aprire la finestra di dialogo Esegui.
   - Digitare "**msconfig**" e premere **Invio** per aprire l'utilità di configurazione del sistema.
   - Passare alla scheda **"Avvio "**.
   - Fare clic su **"Opzioni avanzate "**.
   - Selezionare l'opzione **"Enable Hypervisor-protected Code Integrity "**.
   - Fare clic su **OK** per salvare le modifiche e riavviare il sistema.

   L'abilitazione di HVCI richiede hardware compatibile e determinati requisiti di sistema. Per ulteriori dettagli, consultare la documentazione ufficiale **Microsoft**.

Applicando le funzioni di isolamento basate sull'hardware predefinite, come VBS e HVCI, è possibile migliorare in modo significativo la sicurezza del sistema Windows 11. Queste funzioni contribuiscono a proteggere i componenti critici del sistema da vari tipi di minacce. Queste funzioni aiutano a proteggere i componenti critici del sistema da vari attacchi, compresi quelli che tentano di modificare o sfruttare il codice e le configurazioni del sistema.

Assicuratevi di aggiornare regolarmente il vostro sistema con le patch di sicurezza e gli aggiornamenti del firmware più recenti per beneficiare dei miglioramenti e delle mitigazioni della sicurezza offerti da queste funzioni di isolamento basate sull'hardware.

Si noti che la disponibilità e i requisiti delle funzioni di isolamento basate sull'hardware possono variare a seconda della configurazione del sistema e dell'edizione di Windows 11 in uso. Si consiglia di consultare la documentazione ufficiale **Microsoft** e di eseguire controlli di compatibilità per garantire la corretta implementazione di queste funzioni di sicurezza.

#### 4. [**Use Windows Sandbox**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview)
**Windows Sandbox** è uno strumento prezioso che consente di eseguire applicazioni non attendibili o software di prova in un ambiente isolato, fornendo un ulteriore livello di sicurezza al sistema. Utilizzando Windows Sandbox, è possibile ridurre i rischi potenziali associati all'esecuzione di programmi non attendibili.

Windows Sandbox crea un ambiente desktop leggero e temporaneo, completamente separato dal sistema operativo principale. Tutte le modifiche apportate all'interno della Sandbox vengono eliminate una volta chiusa, garantendo che il sistema principale non ne risenta.

Per utilizzare Windows Sandbox, procedere come segue:

1. **Controllare i requisiti di sistema**: Prima di procedere, assicuratevi che il vostro sistema soddisfi i requisiti per l'esecuzione di Windows Sandbox. In generale, sono necessari Windows 10 Pro o Enterprise e un processore con funzionalità di virtualizzazione abilitate nel firmware BIOS/UEFI. Consultare il sito ufficiale [**Microsoft documentation**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview) per i requisiti specifici del sistema.

2. **Attiva Windows Sandbox**: Windows Sandbox è una funzione integrata nelle edizioni Windows 10 Pro ed Enterprise. Per abilitare Windows Sandbox, procedere come segue:

   - Premere il tasto **Windows + R** per aprire la finestra di dialogo Esegui.
   - Digitare "**appwiz.cpl**" e premere **Invio** per aprire la finestra Programmi e funzionalità.
   - Fare clic su **"Attiva o disattiva le funzioni di Windows "** sul lato sinistro.
   - Scorrere verso il basso e individuare **"Windows Sandbox "** nell'elenco delle funzioni.
   - Selezionate la casella accanto a **"Windows Sandbox "** e fate clic su **OK** per attivarla.
   - Windows installerà i componenti necessari e potrebbe essere necessario riavviare il sistema per rendere effettive le modifiche.

3. **Avviare Windows Sandbox**: Una volta abilitata Windows Sandbox, è possibile avviarla seguendo i seguenti passaggi:

   - Aprire il menu **Avvio** e cercare **"Windows Sandbox "**.
   - Fare clic sull'applicazione **"Windows Sandbox "** per aprirla.
   - La Sandbox viene avviata in una finestra separata e fornisce un ambiente sicuro per eseguire applicazioni non attendibili o software di prova.

Durante l'esecuzione di applicazioni in Windows Sandbox, tenere presente che l'ambiente Sandbox è isolato e progettato per eliminare qualsiasi modifica apportata al suo interno. Pertanto, è fondamentale salvare i file o i dati al di fuori di Sandbox, se è necessario conservarli.

Windows Sandbox è uno strumento efficace per testare software sconosciuti, aprire file sospetti o esplorare siti web potenzialmente rischiosi. Aggiunge un ulteriore livello di protezione assicurando che qualsiasi attività dannosa o modifica indesiderata sia confinata all'interno della Sandbox e non abbia un impatto sul sistema operativo principale.

Incorporando Windows Sandbox nelle vostre pratiche di sicurezza, potrete ridurre significativamente i rischi associati all'esecuzione di applicazioni non attendibili, proteggendo il vostro sistema da potenziali minacce.

Per ulteriori informazioni su Windows Sandbox e il suo utilizzo, consultare il sito ufficiale di Windows Sandbox. [**Microsoft documentation**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview)

#### 5. [**Implement Microsoft Defender Application Guard**](https://github.com/simeononsecurity/Windows-Defender-Application-Guard-Hardening)
Microsoft Defender Application Guard è una potente funzione di sicurezza che isola le sessioni del browser Microsoft Edge dal sistema operativo sottostante. Eseguendo Edge in un ambiente sicuro e isolato, Application Guard aiuta a proteggere il sistema dagli attacchi basati sul browser e dai siti Web dannosi.

Per implementare Microsoft Defender Application Guard e migliorare la sicurezza del browser, procedete come segue:

1. **Verifica della compatibilità**: Prima di procedere, assicuratevi che il vostro sistema soddisfi i requisiti per l'esecuzione di Microsoft Defender Application Guard. In genere, sono necessari Windows 10 Pro o Enterprise, un processore compatibile con funzionalità di virtualizzazione e almeno 8 GB di RAM. Consultare il sito ufficiale [**Microsoft documentation**](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-windows-defender-application-guard) per i requisiti specifici del sistema.

2. **Attiva Application Guard**: Application Guard è disponibile come funzione facoltativa in Windows 10. Per abilitare Microsoft Defender Application Guard, procedere come segue:

   - Premere il tasto **Windows + R** per aprire la finestra di dialogo Esegui.
   - Digitare "**appwiz.cpl**" e premere **Invio** per aprire la finestra Programmi e funzionalità.
   - Fare clic su **"Attiva o disattiva le funzioni di Windows "** sul lato sinistro.
   - Scorrere verso il basso e individuare **"Microsoft Defender Application Guard "** nell'elenco delle funzioni.
   - Selezionate la casella accanto a **"Microsoft Defender Application Guard "** e fate clic su **OK** per attivarla.
   - Windows installerà i componenti necessari e potrebbe essere necessario riavviare il sistema per rendere effettive le modifiche.

3. **Configurazione di Application Guard**: Una volta abilitato Application Guard, è possibile configurare le sue impostazioni in base alle proprie esigenze di sicurezza. Application Guard consente di definire il livello di isolamento e di controllare il modo in cui gestisce i siti web e i file non attendibili. È possibile regolare queste impostazioni tramite l'applicazione **Windows Security** o le impostazioni dei Criteri di gruppo.

4. **Test e verifica**: Dopo aver attivato e configurato Microsoft Defender Application Guard, è essenziale testarne e verificarne la funzionalità. Aprite Microsoft Edge e visitate un sito web noto come dannoso o potenzialmente rischioso per verificare se Application Guard riesce a isolare la sessione del browser e a prevenire eventuali attacchi.

Implementando Microsoft Defender Application Guard, si aggiunge un ulteriore livello di protezione al sistema, isolando le sessioni del browser e contenendo le potenziali minacce all'interno di un ambiente sicuro. Ciò contribuisce a salvaguardare il sistema e i dati da attacchi basati sul browser, come download drive-by, script dannosi ed exploit zero-day.

Per informazioni più dettagliate sulla configurazione e l'utilizzo di Microsoft Defender Application Guard, consultare il sito ufficiale di Microsoft Defender. [**Microsoft documentation**](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-windows-defender-application-guard)

#### 6. [**Controlled Folder Access**](https://github.com/simeononsecurity/Windows-Defender-Hardening)
L'Accesso controllato alle cartelle è una potente funzione di sicurezza disponibile in Windows 11 che aiuta a proteggere le cartelle importanti da modifiche non autorizzate da parte di ransomware e altri software dannosi. Attivando l'Accesso controllato alle cartelle e aggiungendo le cartelle necessarie all'elenco protetto, è possibile migliorare la sicurezza del sistema e prevenire potenziali perdite di dati.

Per implementare l'Accesso controllato alle cartelle e proteggere le cartelle importanti, procedere come segue:

1. **Aprire la sezione Sicurezza di Windows**: Premete il tasto **Windows** sulla tastiera, digitate "**Windows Security**" e selezionate l'applicazione **Windows Security** dai risultati della ricerca.

2. **Navigare fino a Impostazioni di protezione da virus e minacce**: Nell'applicazione Windows Security, fare clic sulla scheda **"Protezione da virus e minacce "** nel menu a sinistra.

3. **Configurare l'accesso controllato alle cartelle**: Nella sezione **"Protezione ransomware "**, fare clic su **"Gestisci protezione ransomware "** per accedere alle impostazioni di Accesso controllato alle cartelle.

4. **Attivare l'accesso controllato alle cartelle**: Nelle impostazioni dell'Accesso controllato alle cartelle, selezionate l'interruttore su **"On "** per abilitare la funzione. Windows visualizzerà un avviso per consentire l'accesso alle cartelle protette solo alle applicazioni affidabili.

5. **Aggiungere cartelle protette**: Per specificare le cartelle da proteggere, fare clic su **"Cartelle protette "** e selezionare **"Aggiungi una cartella protetta "**. Scegliere le cartelle da proteggere e fare clic su **"OK "**.

   - Si consiglia di aggiungere cartelle importanti come Documenti, Immagini, Video e qualsiasi altra directory contenente dati preziosi.

6. **Ammetti o blocca le applicazioni**: Per impostazione predefinita, Accesso controllato alle cartelle consente alle applicazioni affidabili di accedere alle cartelle protette. Tuttavia, è possibile personalizzare questo comportamento facendo clic su **"Consenti un'applicazione tramite Accesso controllato alle cartelle "**. Da qui è possibile consentire o bloccare l'accesso di applicazioni specifiche alle cartelle protette.

7. **Monitoraggio e revisione**: Dopo aver abilitato l'Accesso controllato alle cartelle, Windows monitorerà e registrerà continuamente qualsiasi tentativo di accesso alle cartelle protette da parte di applicazioni non autorizzate. È possibile esaminare questi registri facendo clic su **"Rivedi "** nella sezione **"Applicazioni bloccate di recente "** delle impostazioni di Accesso controllato alle cartelle.

Implementando l'Accesso controllato alle cartelle, si aggiunge un ulteriore livello di protezione alle cartelle importanti, riducendo il rischio di modifiche non autorizzate e la potenziale perdita di dati causata da attacchi ransomware. Rivedete regolarmente le impostazioni di Accesso controllato alle cartelle per assicurarvi che le cartelle protette siano in linea con i vostri requisiti di sicurezza.

Per informazioni più dettagliate sulla configurazione e sull'utilizzo di Accesso controllato alle cartelle, consultare il documento ufficiale [**Microsoft documentation**](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/controlled-folders?view=o365-worldwide)


#### 7. **Attiva la manutenzione automatica di Windows**
Windows 11 include una comoda funzione chiamata Manutenzione automatica che aiuta a mantenere il sistema ottimizzato e protetto eseguendo regolari attività di manutenzione. Abilitando la Manutenzione automatica, si garantisce il funzionamento regolare e la sicurezza del sistema.

Per attivare la Manutenzione automatica di Windows, procedere come segue:

1. Aprire le **Impostazioni di Windows**: Premere il tasto **Windows** sulla tastiera, digitare "**Impostazioni**" e selezionare l'applicazione **Impostazioni** dai risultati della ricerca.

2. **Accedere alle impostazioni di manutenzione**: Nell'applicazione Impostazioni, fare clic sulla categoria **"Sistema "** e quindi selezionare **"Informazioni su "** dal menu a sinistra. Scorrere fino alla fine della pagina e fare clic sul link **"System info "**.

3. **Aprire le impostazioni di manutenzione**: Nella finestra Informazioni sul sistema, fare clic sul link **"Manutenzione "** situato in fondo alla pagina.

4. **Abilita la manutenzione automatica**: Nelle impostazioni di manutenzione, spostare l'interruttore accanto a **"Manutenzione automatica "** sulla posizione **"On "**.

5. **Configurazione delle impostazioni di manutenzione**: Per impostazione predefinita, Windows pianifica automaticamente le attività di manutenzione da eseguire ogni giorno alle 2:00 del mattino. Se si preferisce una pianificazione diversa, fare clic su **"Modifica impostazioni di manutenzione "** e personalizzare le opzioni desiderate, come l'ora di inizio della manutenzione e la frequenza delle attività di manutenzione.

6. **Vedi le impostazioni aggiuntive**: Sotto l'interruttore a levetta della Manutenzione automatica, si trovano altre impostazioni relative alla manutenzione, come **"Consenti alla manutenzione programmata di svegliare il computer all'ora prevista "** e **"Consenti alla manutenzione programmata di funzionare anche quando sono a batteria "**. Regolare queste impostazioni in base alle proprie preferenze ed esigenze.

7. **Monitoraggio delle attività di manutenzione**: Una volta attivata la Manutenzione automatica, Windows eseguirà automaticamente le attività di manutenzione in background all'ora programmata. È possibile monitorare queste attività controllando la sezione **"Manutenzione "** nell'applicazione **"Sicurezza di Windows "** o esaminando i registri **"Manutenzione "** nel Visualizzatore eventi.

L'attivazione della Manutenzione automatica di Windows garantisce che il sistema sia ottimizzato e protetto, eseguendo regolarmente attività di manutenzione essenziali come gli aggiornamenti del software, l'ottimizzazione del disco e le scansioni di sicurezza. Mantenendo il sistema in buona salute, è possibile godere di un'esperienza informatica più fluida e sicura.

Per informazioni più dettagliate sulla Manutenzione automatica di Windows e sulle sue opzioni di configurazione, consultare il sito ufficiale di Windows. [**Microsoft documentation**](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-maintenence)

______

{{< inarticle-dark >}}

## Conclusione

L'implementazione di queste **migliori pratiche di hardening di Windows** è essenziale per garantire la sicurezza dei sistemi Windows. Aggiornando regolarmente il sistema operativo**, è possibile correggere le vulnerabilità di sicurezza e migliorare la stabilità del sistema. L'attivazione di funzioni di sicurezza come **antivirus** e **crittografia** aggiunge un ulteriore livello di protezione ai dati. La configurazione di **controlli di accesso** appropriati aiuta a prevenire modifiche non autorizzate e limita l'accesso alle risorse sensibili.

Rispettando queste best practice, potete migliorare la sicurezza del vostro **ambiente Windows**, proteggere i vostri dati e mantenere l'integrità della vostra **infrastruttura digitale**. È importante rimanere **proattivi** e rivedere e aggiornare regolarmente le misure di sicurezza per essere sempre all'avanguardia rispetto alle potenziali minacce.

Ricordate che l'**indurimento di Windows** è un processo continuo ed è essenziale rimanere informati sugli ultimi aggiornamenti e sulle pratiche di sicurezza. Rimanendo proattivi e implementando queste best practice, è possibile ridurre efficacemente i rischi di sicurezza e garantire la sicurezza dei sistemi Windows.

Per ulteriori informazioni sull'hardening di Windows e sulle best practice, consultare fonti affidabili come la **documentazione Microsoft**, i **forum sulla sicurezza** e i siti web affidabili sulla **cybersecurity**.

______

## Riferimenti:

- [Microsoft Windows Security](https://www.microsoft.com/en-us/security)
- [NIST Special Publication 800-171: Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations](https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final)
- [CIS Microsoft Windows 10 Benchmark](https://www.cisecurity.org/benchmark/microsoft_windows_10/)
- [CIS Microsoft Windows 11 Benchmark](https://www.cisecurity.org/benchmark/microsoft_windows_11/)