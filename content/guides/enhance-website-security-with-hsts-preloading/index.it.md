---
title: "Precarico HSTS Come migliorare la sicurezza di un sito web: Una guida passo dopo passo"
date: 2023-08-20
toc: true
draft: false
description: "Scoprite come migliorare la sicurezza dei siti web e la fiducia degli utenti precaricando le impostazioni HSTS su Chrome e Firefox. Seguite la nostra guida passo passo per un'implementazione perfetta."
cover: "/img/cover/enhanced-website-security.png"
coverAlt: "Un'illustrazione in stile fumetto di un sito web protetto da un lucchetto, che rappresenta una maggiore sicurezza e protezione contro le minacce informatiche."
coverCaption: "Rafforzate la difesa del vostro sito web, adottando il precaricamento HSTS."
---

## **Migliorare la sicurezza del sito web con il precaricamento HSTS: Una guida passo-passo**

HTTP Strict Transport Security (HSTS) è un **meccanismo di sicurezza cruciale** che garantisce che i siti web applichino le connessioni HTTPS per **proteggere gli utenti da potenziali minacce alla sicurezza**. Precaricando le impostazioni HSTS su Chrome e Firefox, è possibile **aumentare la sicurezza dei siti web** e creare **fiducia negli utenti**. In questa guida completa, vi guideremo attraverso i **passi essenziali** per precaricare con successo le impostazioni HSTS e vi forniremo **consigli utili** per ottimizzare la sicurezza.

______

### **Comprendere il precaricamento HSTS**

Il **preloading HSTS** è il processo di **sottoposizione del dominio del vostro sito web** agli elenchi di preload dei principali browser. Una volta aggiunto, questi browser **imporranno automaticamente le connessioni HTTPS** per il vostro dominio e tutti i sottodomini. Questo garantisce che gli utenti accedano sempre al vostro sito web in modo sicuro, riducendo il rischio di **attacchi man-in-the-middle** e di intercettazioni non autorizzate. Per ulteriori dettagli sul precaricamento HSTS, è possibile consultare il documento ufficiale [documentation](https://hstspreload.org/)

______

______

### **Requisiti di presentazione**

Prima di inviare il vostro dominio per il precaricamento HSTS, assicuratevi che il vostro sito web soddisfi i seguenti **requisiti essenziali**:

1. **Certificato valido**: Il vostro sito web deve disporre di un **certificato SSL o TLS valido** per consentire **connessioni HTTPS sicure**.

2. **Ridirezione da HTTP a HTTPS**: Assicuratevi che tutte le **richieste HTTP siano reindirizzate** alle loro **controparti HTTPS** quando il vostro sito web è in ascolto sulla porta 80.

3. **HTTPS per tutti i sottodomini**: Tutti i sottodomini del vostro sito web devono **supportare connessioni HTTPS** per essere idonei al precaricamento HSTS.

4. Intestazione **HSTS sul dominio di base**: Includere un'intestazione **HSTS** sul dominio di base per le richieste HTTPS con le seguenti impostazioni:
   - `max-age` deve essere di **almeno 31536000 secondi** (1 anno).
   - Il `includeSubDomains` deve essere specificata per includere tutti i sottodomini.
   - L'opzione `preload` deve essere specificata per richiedere l'inclusione nell'elenco di precaricamento.

Ecco un esempio di intestazione HSTS valida:

```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

______

### **Come precaricare le impostazioni HSTS**

Se il vostro sito web è **completamente impegnato in HTTPS** e soddisfa i requisiti di cui sopra, seguite questi **passi cruciali** per precaricare con successo le impostazioni HSTS:

1. **Esaminare i sottodomini**: Assicuratevi che tutti i **sottodomini del vostro sito web** funzionino correttamente su HTTPS per fornire agli utenti un'esperienza di navigazione senza interruzioni.

2. **Aumento graduale**: Per verificare e risolvere eventuali problemi, aggiungete l'intestazione **HSTS** alle vostre risposte HTTPS con un **basso livello**. `max-age` (ad esempio, 300 secondi). Aumentare gradualmente il valore `max-age` valore in fasi:
   - 5 minuti: `max-age=300; includeSubDomains`
   - 1 settimana: `max-age=604800; includeSubDomains`
   - 1 mese: `max-age=2592000; includeSubDomains`

3. **Monitorare le metriche**: Durante ogni fase, **monitorate attentamente le metriche del vostro sito web**, compresi il traffico e le entrate, per identificare e risolvere eventuali problemi prima di procedere alla fase successiva.

4. **Aumentare l'età massima a 2 anni**: Una volta **convinti che non ci siano più problemi**, impostate l'età massima a 2 anni**. `max-age` a **2 anni (63072000 secondi)** e aggiungere il valore `preload` all'intestazione HSTS:
```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

5. **Invia il tuo sito**: Dopo aver implementato i 2 anni di `max-age` per l'impostazione, **sottoporre il proprio sito** all'elenco di precaricamento HSTS utilizzando il modulo disponibile su [hstspreload.org](https://hstspreload.org/) Si noti che l'inclusione nell'elenco di precaricamento può richiedere diversi mesi per raggiungere gli utenti con un aggiornamento di Chrome.
______

### **Opt-In per il precaricamento HSTS: Responsabilizzare gli operatori dei siti**

Il supporto del precaricamento HSTS è un'**eccellente pratica di sicurezza** che migliora la protezione dei siti web. Tuttavia, dovrebbe essere una decisione **opt-in** per gli operatori del sito. Se si forniscono **consigli sulla configurazione HTTPS** o si offre un'opzione per abilitare l'HSTS, **evitare di includere l'opzione `preload` per impostazione predefinita**. Questo approccio impedisce l'inclusione involontaria nell'elenco di precaricamento, che può causare difficoltà di accesso a determinati sottodomini.

Per garantire un'esperienza senza problemi, **informate gli operatori del sito** sulle **conseguenze a lungo termine** del precaricamento e sottolineate l'**importanza di soddisfare tutti i requisiti** prima di abilitare l'HSTS per il loro dominio.

______

### **Rimozione dall'elenco di precaricamento: Una decisione deliberata**

L'inclusione nell'elenco di precaricamento è una **decisione permanente** che non può essere facilmente annullata. Tuttavia, se si riscontrano **fortemente ragioni tecniche o di costo** che impediscono il supporto HTTPS per alcuni sottodomini, si ha la possibilità di richiedere la **rimozione dall'elenco di precaricamento di Chrome** tramite la funzione [removal form](https://hstspreload.org/removal/)

Assicuratevi di aver valutato attentamente le implicazioni prima di prendere questa importante decisione.
______

______

### **La navigazione più sicura inizia con il precaricamento HSTS**

In conclusione, precaricare le impostazioni HSTS su Chrome e Firefox è un **passo proattivo** verso un'esperienza di navigazione web più sicura per i vostri utenti. **imponendo le connessioni HTTPS**, si **proteggono i dati sensibili** e si crea **fiducia** tra i visitatori. Seguite le **guide** indicate sopra per **precaricare con successo le impostazioni HSTS** e godere di una **maggiore sicurezza del sito web**.

______

### Riferimenti

1. [Chromium - HTTP Strict Transport Security (HSTS)](https://www.chromium.org/hsts/)
2. [HSTS Preload Submission](https://hstspreload.org/)
3. [Mozilla Web Security Guidelines](https://infosec.mozilla.org/guidelines/web_security)
4. [Google Web Fundamentals - Security](https://developers.google.com/web/fundamentals/security/)
