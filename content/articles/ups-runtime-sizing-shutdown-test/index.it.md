---
title: "Dimensionare un UPS per l’homelab e testare lo spegnimento automatico"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Misura l’assorbimento dell’homelab, confronta i limiti in watt e VA dell’UPS, verifica l’autonomia con il tuo carico e prova uno spegnimento corretto prima di affidarti alla batteria."
genre: ["Laboratorio domestico", "Protezione dell’alimentazione", "Amministrazione di sistema"]
tags: ["UPS per homelab", "dimensionamento UPS", "autonomia UPS", "spegnimento automatico", "Network UPS Tools", "watt UPS", "VA UPS", "fattore di potenza", "alimentazione di backup", "spegnimento server", "spegnimento NAS", "interruzione di corrente", "test UPS", "curva di autonomia", "misuratore di potenza", "monitoraggio UPS", "sostituzione batteria", "protezione da sovratensioni", "spegnimento ordinato", "alimentazione homelab"]
cover: "/img/cover/ups-runtime-sizing-shutdown-test.webp"
coverAlt: "Un UPS dell’homelab alimenta un server, un NAS, un router e uno switch sopra una sequenza temporale dall’interruzione di corrente allo spegnimento."
coverCaption: "Misura il carico, controlla l’autonomia e prova lo spegnimento prima di un’interruzione."
---

Un **UPS**, o gruppo di continuità, dà all’homelab il tempo di salvare il lavoro e spegnere i sistemi durante un’interruzione di corrente. L’etichetta da sola non indica per quanto tempo i server resteranno accesi. Ti servono il carico delle apparecchiature, i limiti in watt e VA dell’UPS, una stima dell’autonomia con quel carico e una procedura di spegnimento verificata.

## Punti chiave

- **Misura il carico:** Registra i watt normali e quelli di picco di ogni dispositivo che vuoi mantenere alimentato a batteria.
- **Controlla entrambi i valori:** L’UPS deve soddisfare i requisiti in watt e VA delle apparecchiature collegate.
- **Consulta la curva di autonomia:** L’autonomia varia in base al carico e allo stato della batteria. Usa una stima specifica del modello.
- **Verifica lo spegnimento:** Accertati che il segnale dell’UPS raggiunga ogni host e che gli host si arrestino prima che la batteria si esaurisca.

## Prima di iniziare

Ti serve un misuratore di potenza adatto alla rete elettrica locale, un elenco di dispositivi e alimentatori e l’accesso alle specifiche e alla curva di autonomia di ogni modello UPS considerato. Per provare lo spegnimento automatico servono anche una connessione USB o di gestione in rete supportata e il software per ciascun host. Riserva tempo per una misura con carico normale, un’osservazione con carico elevato e una prova di manutenzione pianificata. È un’attività di livello intermedio per l’homelab, perché una prova completa di spegnimento interrompe i servizi.

La [guida alle ciabatte antifulmine](/articles/protecting-your-tech_-the-best-surge-protectors/) del sito tratta la protezione dalle sovratensioni. La [raccolta di modelli UPS](/articles/best-ups-models-for-uninterrupted-connectivity/) elenca i prodotti. Questa guida spiega come dimensionare e verificare il tuo carico. Sia la [guida al dimensionamento UPS di Eaton](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/ups-sizing-guide.html) sia la [guida all’acquisto di Schneider Electric](https://www.se.com/us/en/work/support/product-support/ups-buying-guide-for-selecting-a-battery-backup-system/) distinguono la potenza in uscita dall’autonomia della batteria.

> **Avvertenza:** Usa solo le prese e i carichi approvati dal produttore dell’UPS. Mantieni la prova entro la capacità nominale dell’UPS. Una prova reale di spegnimento arresta il lab collegato.

## Misura ciò che deve restare acceso

Decidi quali dispositivi devono funzionare fino allo spegnimento. Includi hypervisor, dispositivo di archiviazione, switch di rete e router se un host deve raggiungere la rete per ricevere il segnale di spegnimento. Lascia monitor, stampanti e altri carichi facoltativi fuori dalle prese alimentate a batteria, a meno che il piano non li richieda.

Misura alla presa il gruppo di dispositivi previsto per l’alimentazione a batteria. Registra i **watt con carico normale** e il valore massimo osservato durante attività rappresentative, come l’avvio degli host o delle macchine virtuali. L’etichetta di un alimentatore indica la capacità, non l’assorbimento misurato del sistema. Controlla comunque le etichette dei dispositivi per i limiti di corrente in ingresso e di spunto. Annota le condizioni di misura nel foglio di lavoro.

| Dispositivo | Watt normali | Picco osservato in watt | Presa a batteria? |
|---|---:|---:|---|
| **Router e switch** | 30 | 35 | Sì |
| **NAS** | 60 | 90 | Sì |
| **Server piccolo** | 90 | 135 | Sì |
| **Totale indicativo** | **180** | **260** | Tre dispositivi |

I valori sopra sono **indicativi**, non misure di un lab specifico. Il carico varia in base a dischi, GPU, impostazioni di alimentazione e apparecchiature collegate. Ripeti le misure dopo modifiche hardware importanti.

## Confronta watt e VA

I **watt** descrivono la potenza attiva usata dalle apparecchiature. I **voltampere (VA)** descrivono la potenza apparente. Il rapporto dipende dal **fattore di potenza**: i watt divisi per il fattore di potenza equivalgono ai VA. Eaton spiega il calcolo nella [guida al dimensionamento](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/ups-sizing-guide.html). Non interpretare un’etichetta da 1000 VA come 1000 watt. Controlla il valore separato in watt dell’UPS.

Per il picco indicativo di 260 W, un margine di capacità del 25% dà **325 W**. Schneider Electric consiglia una potenza in uscita circa [dal 20% al 25% superiore al carico](https://www.se.com/us/en/work/support/product-support/ups-buying-guide-for-selecting-a-battery-backup-system/). Scegli un UPS con potenza continua in watt superiore al picco previsto più il margine. Se conosci il fattore di potenza combinato, dividi i watt di picco per quel fattore per stimare i VA di picco, poi applica ai VA lo stesso margine scelto. Altrimenti usa un misuratore adatto o il selettore del produttore per determinare requisiti VA e margine. Non inventare un fattore di potenza se non lo hai misurato.

Il margine di capacità non determina l’autonomia. Un UPS con un limite in watt elevato ma una batteria piccola potrebbe sostenere il carico solo per poco tempo. Prima di scegliere un modello, verifica prese, tipo di spina, tensione d’ingresso, interfaccia di comunicazione e modalità di sostituzione della batteria.

## Stabilisci un obiettivo di autonomia

Annota quanto tempo serve al lab per arrestarsi in sicurezza. Considera il tempo necessario perché l’avviso di spegnimento raggiunga gli host, le macchine virtuali si fermino, lo storage completi le scritture e l’UPS interrompa l’uscita. Aggiungi un margine per uno spegnimento lento e una batteria usurata. Un lab che deve superare brevi interruzioni richiede un obiettivo diverso da uno che deve solo spegnersi correttamente.

Come **esempio**, supponi che uno spegnimento verificato richieda 6 minuti e che tu scelga 5 minuti di margine. L’autonomia richiesta al carico previsto è almeno 11 minuti. È un esempio di pianificazione, non una soglia universale. Confronta il valore con la curva di autonomia o con il selettore del modello candidato al tuo **carico normale e di picco misurato**, poi rivalutalo con l’invecchiamento della batteria. Il [selettore UPS di Schneider Electric](https://www.se.com/us/en/work/products/tools/ups-selector/) basa l’autonomia sul carico inserito e sulle specifiche del modello. Eaton rimanda ai dati specifici del modello nella sua [guida agli UPS desktop](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/desktop-ups-buying-guide.html).

Copia questo **foglio di lavoro** per il lab. Compila le righe dei dispositivi con le letture del misuratore. Somma i watt normali e quelli di picco, aggiungi il margine scelto al totale di picco e applica lo stesso margine ai VA di picco misurati o calcolati. Confronta entrambi i risultati con un UPS candidato. Se usi il selettore del produttore, annota il risultato VA e il margine. Usa la curva del modello per stimare l’autonomia. Durante la prova, registra i tempi e i risultati del ripristino.

| Campo | Il tuo risultato |
|---|---|
| **Dispositivi e prese a batteria** | Nomi dei dispositivi e presa assegnata a ciascuno |
| **Watt normali per dispositivo e totali** | Valori misurati e somma |
| **Watt di picco per dispositivo e totali** | Valori massimi osservati e somma |
| **Fattore di potenza misurato o specificato** | Valore e fonte, oppure “sconosciuto” |
| **VA di picco misurati o calcolati** | Watt di picco divisi per il fattore di potenza combinato, se noto |
| **Margine di capacità** | Percentuale scelta e watt/VA dopo il margine |
| **Valori nominali dell’UPS candidato** | Modello, watt e VA in uscita e limiti delle prese |
| **Obiettivo di autonomia e stima della curva** | Minuti richiesti e stima del modello al tuo carico |
| **Tempi di avviso e spegnimento** | Ora dell’avviso batteria e arresto dell’ultimo host |
| **Esito del ripristino** | Avvio host, storage, applicazioni e monitoraggio |

Se il fattore di potenza è sconosciuto, usa lo strumento di selezione del produttore o misura la potenza apparente con un misuratore adatto. Non riportare un valore VA calcolato con un fattore ipotizzato. Il foglio è completo solo quando il modello rispetta entrambi i limiti di uscita e la sua autonomia stimata supera l’obiettivo di spegnimento.

> **Risultato atteso:** Il foglio elenca i dispositivi collegati, i carichi misurati, i limiti in watt e VA dell’UPS, l’obiettivo di autonomia e la stima specifica del modello.

## Pianifica lo spegnimento automatico

Un UPS alimenta temporaneamente le apparecchiature. L’host ha comunque bisogno di un **segnale di spegnimento**. Controlla se l’UPS espone USB, una scheda di gestione di rete o un’altra interfaccia supportata. Verifica che ogni host da arrestare disponga di un percorso di monitoraggio compatibile. Eaton segnala che molti modelli supportano la comunicazione USB o di rete per uno [spegnimento ordinato di NAS o server](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/desktop-ups-buying-guide.html).

In un lab Linux che usa **Network UPS Tools (NUT)**, il driver legge l’UPS, `upsd` ne condivide lo stato e `upsmon` attiva lo spegnimento dell’host quando l’alimentazione diventa critica. Un host collegato direttamente a un UPS USB o seriale esegue normalmente driver, `upsd` e `upsmon` in modalità **Primary**. Gli altri host eseguono `upsmon` in modalità **Secondary** collegandosi a quel server. Un UPS gestito in rete richiede un driver compatibile e una configurazione Primary specifica del modello. La [guida alla topologia NUT](https://networkupstools.org/docs/user-manual.chunked/ar01s02.html) spiega questi ruoli. Configura router e switch affinché gli host di monitoraggio restino collegati durante il funzionamento a batteria. Limita il comando di spegnimento e i relativi permessi agli amministratori.

Prima di una prova di spegnimento, verifica che il driver riporti lo stato aggiornato. Sostituisci `myupsname` con il nome dell’UPS nella configurazione NUT:

```bash
upsc myupsname@localhost ups.status
```

La [guida di configurazione NUT](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html) si aspetta `OL` con la normale alimentazione di rete e descrive `OB` per il funzionamento a batteria. Esegui il controllo dello stato su ogni host che monitora l’UPS e specifica il nome corretto del server per i client remoti. Un dato assente o non aggiornato indica che il percorso del segnale va corretto prima di testare lo spegnimento.

Registra l’**ordine di spegnimento**. Per esempio, ferma prima le VM delle applicazioni, poi i client di storage e infine hypervisor e NAS. Verifica che ogni servizio e filesystem si riprenda normalmente al ritorno della corrente. L’arresto corretto dell’host senza il ripristino delle applicazioni non equivale a una prova completa.

## Verifica senza supposizioni

Inizia con una **prova a secco** sull’host con il driver UPS configurato. NUT documenta `upsdrvctl -t shutdown` come anteprima della sequenza di arresto del driver; il comando non invoca i driver e non interrompe l’alimentazione:

```bash
upsdrvctl -t shutdown
```

Questa **prova a secco del driver** non dimostra che un avviso di interruzione raggiunga ogni host. Controlla ogni servizio di monitoraggio e i relativi log. In una finestra di manutenzione, la [guida NUT ai test di spegnimento](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html) descrive una prova forzata con `upsmon -c fsd` sull’host NUT primario. Questo **test FSD** avvia una sequenza reale di spegnimento. Il flag FSD resta attivo finché `upsd` non viene riavviato. Dopo il riavvio dei sistemi, verifica che `upsd` sia ripartito e che lo stato non mostri più FSD prima di affidarti nuovamente al monitoraggio. Leggi il [manuale aggiornato di upsmon](https://networkupstools.org/docs/man/upsmon.html), prepara un piano di ripristino ed esegui la prova solo dopo aver salvato il lavoro e avvisato gli utenti del lab.

Per un **test controllato dell’evento batteria**, segui prima la procedura del produttore dell’UPS con carichi non critici. La prova a carico ridotto controlla la consegna del segnale, ma non dimostra l’autonomia del lab. In seguito, durante una finestra di manutenzione, prova un carico batteria rappresentativo di quello pianificato. Qualcuno deve sorvegliare l’UPS e poter ripristinare la rete elettrica se il margine si riduce. Registra il carico mostrato dall’UPS, l’ora in cui segnala il funzionamento a batteria, l’inizio dello spegnimento di ogni host e l’ora in cui si arresta l’ultimo. Verifica che la batteria non si esaurisca prima dell’arresto degli host. Dopo il ripristino della corrente, controlla l’avvio degli host, lo stato delle applicazioni, l’integrità dello storage e il monitoraggio. NUT considera corretta una sequenza quando il sistema operativo si arresta prima che termini la batteria e riprende il funzionamento al ritorno dell’alimentazione.

| Verifica | Risultato da registrare |
|---|---|
| **Percorso del segnale** | Evento UPS visibile a ogni host di monitoraggio |
| **Tempistiche di spegnimento** | L’ultimo host si è arrestato prima che la batteria si esaurisse |
| **Ripristino** | Host, storage e applicazioni si avviano correttamente |
| **Capacità** | Il carico UPS resta entro i limiti in watt e VA |

## Risoluzione dei problemi

- **Allarme di sovraccarico UPS:** Rimuovi i carichi facoltativi. Confronta il carico massimo misurato con entrambi i limiti UPS e con i limiti delle prese del modello.
- **Autonomia inferiore al previsto:** Controlla il carico attuale, l’età della batteria, i dati specifici del modello e gli ultimi test della batteria. Non estrapolare linearmente usando solo i VA.
- **Un host resta acceso:** Controlla il servizio di monitoraggio, il percorso di rete, i permessi di spegnimento e i log.
- **Gli host si arrestano ma non ripartono:** Verifica il comportamento dell’uscita UPS al ritorno della corrente, l’impostazione firmware di ripristino dopo un’interruzione e le [considerazioni NUT sulle condizioni di gara dell’alimentazione](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html).
- **La prova a secco riesce ma il test di interruzione no:** L’anteprima del driver verifica un percorso più limitato. Esamina la consegna degli eventi e l’effettivo ordine di spegnimento degli host.

## Passi successivi

Conserva il foglio insieme all’inventario dell’homelab. Ripeti la misura dopo aver aggiunto hardware e ripeti il test di spegnimento dopo modifiche all’UPS, al software di monitoraggio, ai criteri di avvio degli host o allo stack di storage. Verifica separatamente il piano di backup e ripristino. La batteria protegge la finestra di spegnimento, mentre un [backup dell’homelab verificato](/articles/what-is-a-homelab-and-should-you-have-one/) protegge i dati da altri guasti.
