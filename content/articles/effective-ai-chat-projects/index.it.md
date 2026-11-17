---
title: "Progetti ChatGPT e Claude: configura un contesto IA riutilizzabile"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Configura progetti ChatGPT e Claude con istruzioni mirate, file di riferimento aggiornati e un semplice test del contesto riutilizzato."
genre: ["Intelligenza artificiale", "Produttività"]
tags: ["Progetti ChatGPT", "Progetti Claude", "istruzioni per progetti IA", "contesto IA", "configurazione progetti ChatGPT", "conoscenze dei progetti Claude"]
cover: "/img/cover/effective-ai-chat-projects.webp"
coverAlt: "Due spazi di lavoro IA organizzati con un brief di progetto, file di riferimento e conversazioni separate"
coverCaption: ""
---

[Torna al corso sul flusso di lavoro pratico con l’IA](/effective-ai-course-start/)

**Crea un progetto quando più conversazioni hanno lo stesso scopo.** Raccogli in un unico posto le istruzioni stabili e i file di riferimento approvati. Mantieni ogni conversazione concentrata su un’attività. Questa lezione usa un laboratorio comunitario fittizio per esercitarti senza dati privati.

**Obiettivo di apprendimento:** creerai un progetto con due fonti controllate e ne verificherai i fatti in una nuova chat.

## Punti chiave

- **Le istruzioni del progetto** definiscono un comportamento riutilizzabile per chat correlate.
- **Le fonti del progetto** contengono i riferimenti che vuoi far consultare all’assistente.
- **La cronologia della conversazione** documenta uno scambio, ma non sostituisce una fonte approvata.
- **Un test in una nuova chat** mostra se la configurazione fornisce contesto sufficiente.

## Prima di iniziare

**Prerequisiti:** un account ChatGPT o Claude e il pacchetto dell’attività della [lezione 1](/articles/effective-ai-workflow-foundations/). Riserva 35 minuti. La difficoltà è per principianti. Usa nomi, date e luoghi inventati durante tutta l’esercitazione.

**Crea due piccoli file** sul computer. Apri un editor di testo semplice, incolla ciascun blocco in un file separato e salvalo con il nome `.md` mostrato. I file Markdown sono testo semplice. `workshop-brief.md` indica il pubblico e lo stile. `approved-schedule.md` contiene il programma ufficiale fittizio.

```text
workshop-brief.md, revisione 1
Pubblico: persone iscritte a un workshop introduttivo.
Stile: frasi brevi e tono cordiale e concreto.
Non inventare prezzi, funzioni di accessibilità o dettagli sui parcheggi.
```

```text
approved-schedule.md, revisione 1
Marcatore della fonte: WS-2026-11-12-R1
Evento: Introduzione alla sicurezza digitale
Data: 2026-11-12
Inizio: 7 p.m.
Luogo: Community Room A
```

## Configurare ChatGPT

1. **Apri “Projects”** nella barra laterale di ChatGPT e crea un progetto chiamato `Workshop Practice`.
2. **Aggiungi i due file** come fonti del progetto.
3. **Apri le impostazioni del progetto** e inserisci le istruzioni seguenti.
4. **Controlla le impostazioni di memoria e condivisione** del tuo account e spazio di lavoro prima di aggiungere materiale reale.

```text
Usa approved-schedule.md per i fatti dell’evento.
Usa workshop-brief.md per pubblico e stile.
Se manca un dato richiesto, chiedi la fonte o segnalalo come sconosciuto.
Scrivi solo bozze. Non inviarle né pubblicarle.
Elenca le modifiche fattuali dopo ogni bozza rivista.
```

**I progetti ChatGPT raccolgono chat, file e istruzioni correlate.** Le impostazioni e le funzioni disponibili cambiano in base al piano e allo spazio di lavoro. Se la procedura di creazione offre la memoria limitata al progetto, selezionala per una prova di isolamento pulita. Con la memoria predefinita, una chat potrebbe attingere a informazioni esterne ai file caricati. Il marcatore univoco qui sotto ti aiuta a verificare il file senza considerare una risposta proveniente dalla memoria come prova della lettura del file. Consulta la [guida ufficiale ai progetti ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) per controllare le opzioni di memoria attuali.

## Configurare Claude

1. **Apri “Projects”** in Claude e crea un progetto con lo stesso nome di esercitazione.
2. **Aggiungi i due file** alle conoscenze del progetto.
3. **Imposta le stesse cinque righe** come istruzioni del progetto.
4. **Avvia una nuova chat nel progetto** per verificare la configurazione.

**Questi passaggi descrivono i progetti Claude classici.** Anthropic sta distribuendo una beta separata di Projects ad alcuni utenti Pro e Max di Claude Code. Nella beta, un progetto è una conversazione con thread cloud paralleli. Consulta [Cosa sono i progetti](https://support.claude.com/en/articles/9517075-what-are-projects) e segui l’interfaccia del tuo account. Le istruzioni dei progetti classici valgono per tutte le chat e le conoscenze del progetto forniscono riferimenti condivisi. Usa i file caricati come fatti controllati. Il funzionamento della memoria del progetto varia in base all’account e alle impostazioni, quindi non considerare i dettagli di un’altra chat come il programma approvato. Consulta la [guida alla configurazione dei progetti Claude](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) per i controlli attuali.

| Modalità del progetto | Materiale condiviso da controllare | Nuovo test |
|---|---|---|
| **Progetto ChatGPT** | File caricati, istruzioni e modalità di memoria selezionata | Una nuova chat del progetto cita il marcatore del programma |
| **Progetto Claude classico** | Conoscenze del progetto e istruzioni condivise tra le chat | Una nuova chat del progetto cita il marcatore del programma |
| **Beta di Claude Projects** | Fonti e contesto nel progetto e nei thread cloud | Un nuovo thread del progetto cita il marcatore del programma |

**Un progetto raccoglie il contesto, ma non approva una fonte.** Il marcatore mostra se il file indicato è arrivato alla chat. Confronta comunque data, ora e sala con il file.

## Verificare una nuova chat

**Apri una nuova conversazione di un progetto ChatGPT o una nuova chat di un progetto Claude classico.** Nella beta di Claude Projects, usa un nuovo thread del progetto. Chiedi un breve annuncio. Ometti il programma dal prompt, così saranno le fonti del progetto a fornire i dati.

```text
Scrivi una bozza di email di 100 parole per il prossimo workshop.
Indica il file fonte e il suo marcatore esatto per ora e luogo.
Elenca i dati mancanti dopo la bozza.
Non inviare il messaggio.
```

| Risultato | Significato | Passaggio successivo |
|---|---|---|
| **Ora, luogo e marcatore corrispondono** | Il file è disponibile in questa chat | Verifica personalmente i dati nel file |
| **Un fatto è inventato** | Le istruzioni o l’uso della fonte non hanno funzionato | Rimuovi il fatto e rendi la richiesta più precisa |
| **La fonte non c’è** | Il riferimento non è arrivato a questa chat | Controlla l’appartenenza al progetto e il caricamento del file |
| **Compare una revisione precedente** | Il progetto contiene materiale non aggiornato | Sostituisci la fonte e ripeti il test |

**Non dedurre l’affidabilità da una sola risposta corretta.** La memoria predefinita del progetto potrebbe fornire un orario familiare senza leggere il file caricato. Richiedi il marcatore esatto `WS-2026-11-12-R1`, poi ripeti il test con questa bozza in conflitto:

```text
Rivedi questa frase usando il calendario approvato del progetto:
«La lezione Introduzione alla sicurezza digitale inizia alle 6 p.m. in Community Room A».
Indica la modifica fattuale, il file fonte e il marcatore. Non inviare il messaggio.
```

**Risposta attesa:** la riga indica le 19 e nomina `approved-schedule.md` con il marcatore `WS-2026-11-12-R1`. Registra ogni errore osservato. Un test superato non richiede un errore inventato.

**Esempio di registrazione del test:** nuova chat, primo prompt, ora 19, luogo Community Room A, fonte `approved-schedule.md`, marcatore `WS-2026-11-12-R1`, superato. Prompt di conflitto, correzione dalle 18 alle 19, superato. Questo è un esempio. Sostituiscilo con le tue osservazioni.

## Gestire il progetto

**Mantieni brevi le istruzioni del progetto.** Inserisci lì le regole stabili. Aggiungi i dettagli specifici dell’attività a ciascun prompt. Sostituisci i file non aggiornati e indica le relative revisioni. Separa le attività non correlate in un altro progetto per evitare conflitti tra fonti.

**Prima di condividere un progetto,** controlla file, chat, istruzioni ed elenco degli accessi. Un progetto è uno spazio di lavoro, non un sistema di approvazione. Anche un file chiamato “approved” richiede un responsabile reale e un registro delle revisioni per le attività importanti.

## Esercitarsi e verificare

**Il tuo risultato:** un progetto con due file di origine sintetici, cinque righe di istruzioni e una breve registrazione del test. Annota ora e luogo osservati, nome della fonte, marcatore ed eventuali fatti inventati. Al termine, elimina il progetto di esercitazione se non ti serve più.

**Ragionamento atteso:** una nuova chat usa le fonti del progetto per i fatti stabili, mentre il prompt definisce il risultato immediato. Verifica la risposta nel file. Se manca una fonte o appare una revisione errata, torna alla configurazione del progetto.

## Verificare la comprensione

1. **Domanda:** una nuova chat di un progetto ChatGPT garantisce l’isolamento con ogni impostazione di memoria? **Risposta:** no. Controlla la modalità di memoria del progetto e provala con un marcatore di fonte univoco.

2. **Domanda:** cosa devi fare se il progetto ripete un programma precedente? **Risposta:** controlla la fonte allegata e l’ambito della memoria, poi sostituisci il materiale non aggiornato.

## Risoluzione dei problemi

- **Controlli del progetto mancanti:** verifica il piano attuale e le impostazioni dello spazio di lavoro nella guida del fornitore.
- **Risposte in conflitto:** rimuovi i file di origine duplicati o non aggiornati, poi avvia una nuova chat.
- **Condivisione imprevista:** controlla i membri del progetto e rimuovi le fonti sensibili prima di proseguire.
- **Deriva dello stile ripetuta:** accorcia le istruzioni e fornisci un esempio breve nel prompt dell’attività.

## Prossimi passi

**Continua con [Contesto del repository in AGENTS.md](/articles/effective-ai-agents-md-context/)**. La lezione successiva passa da un progetto di chat a un repository di codice locale.

**Navigazione del corso:** [Precedente: Fondamenti del flusso di lavoro](/articles/effective-ai-workflow-foundations/), [Indice del corso](/effective-ai-course-start/).
