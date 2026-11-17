---
title: "Come usare bene l’IA: un flusso di lavoro affidabile per principianti"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Impara un flusso di lavoro ripetibile per l’IA: definisci il compito, fornisci il contesto pertinente, esamina le prove e verifica il risultato prima di usarlo."
genre: ["Intelligenza artificiale", "Produttività", "Ingegneria del software"]
tags: ["come usare bene l’IA", "flusso di lavoro IA", "IA per principianti", "verifica dell’IA", "pianificazione delle attività IA", "agenti di programmazione"]
cover: "/img/cover/effective-ai-workflow-foundations.webp"
coverAlt: "Una persona controlla un piano di lavoro IA accanto a pochi file sorgente e ai risultati dei test"
coverCaption: ""
---

[Torna al corso Flusso di lavoro pratico con l’IA](/effective-ai-course-start/)

**Usa l’IA come un collaboratore il cui risultato va controllato.** Parti dal risultato desiderato, fornisci solo il materiale pertinente e confronta la risposta con la fonte. Questa lezione presenta un flusso di lavoro per chat, ricerca e codice.

**Obiettivo di apprendimento:** preparerai un’email corretta per il laboratorio e un registro di revisione con quattro verifiche.

## Punti chiave

- **Compito:** indica il risultato necessario e i suoi limiti.
- **Contesto:** fornisci file, fatti ed esempi pertinenti.
- **Prove:** chiedi da dove provengono le affermazioni e le modifiche importanti.
- **Verifica:** controlla il risultato finito, non la sicurezza dell’assistente.

## Prima di iniziare

**Prerequisiti:** accesso a un qualsiasi strumento di chat IA e un’attività innocua che già conosci. Non servono codice né un piano a pagamento. Dedica 25 minuti. Difficoltà: principiante.

**Scenario di esercitazione:** gestisci un laboratorio comunitario immaginario. Una bozza di email dice che la prossima lezione inizia alle 18:00. Il programma approvato indica le 19:00. Vuoi un’email corretta e un registro delle modifiche. Non inserire dati reali dei clienti.

## Conoscere gli elementi

| Termine | Significato |
|---|---|
| **Modello** | Software che genera testo o un altro risultato a partire da un input |
| **Chat** | Conversazione con il modello, spesso con file e strumenti |
| **Strumento** | Funzione invocata dall’assistente, per esempio ricerca di file o consultazione di un calendario |
| **Agente** | Assistente che svolge un compito con più passaggi e chiamate agli strumenti |
| **Fonte** | Documento usato per sostenere un fatto o una decisione |
| **Artefatto** | File, messaggio, tabella o modifica al codice che conservi |

**Un testo scorrevole non è una prova.** L’assistente potrebbe scrivere una frase convincente basandosi su un programma vecchio. Considera i documenti sorgente come fatti e l’output dell’assistente come una proposta finché non lo verifichi.

## Scrivere un pacchetto del compito

**Indica prima il risultato.** Poi aggiungi la fonte e un criterio di accettazione. La lezione 4 amplia questo schema con un [pacchetto del compito per un agente di programmazione](/articles/effective-ai-task-packets/). Per ora usa questa breve richiesta in chat:

```text
Risultato: prepara una bozza di email per annunciare il prossimo laboratorio.
Fonte: il programma approvato qui sotto dice che la lezione inizia alle 19:00.
Bozza da correggere: "La lezione Introduzione alla sicurezza digitale inizia alle 18:00 il 12 novembre nella sala comunitaria A."
Destinatari: iscritti.
Vincoli: lascia invariati luogo e data. Scrivi solo una bozza.
Completato quando: la bozza indica le 19:00 e descrive la modifica fattuale.
Programma approvato: Introduzione alla sicurezza digitale, 12 novembre 2026,
19:00, sala comunitaria A.
```

**Il pacchetto separa istruzioni e dati.** Le 18:00 della bozza sono il dato da correggere. L’orario approvato determina l’ora corretta. L’assistente non ha il permesso di inviare il messaggio perché hai chiesto soltanto una bozza.

**Scegli una fonte prima di risolvere un conflitto.** Se un riepilogo della chat ripete le 18:00, fa fede il programma approvato. Se due programmi approvati non concordano, fermati e chiedi al responsabile quale versione vale. Non risolvere una disputa tra fonti affidandoti a un testo scorrevole.

## Seguire il ciclo in quattro passaggi

1. **Specifica:** definisci l’artefatto richiesto e un controllo chiaro di completamento.
2. **Fornisci:** includi la fonte pertinente e indica quale documento prevale in caso di conflitto.
3. **Esamina:** confronta il risultato con la fonte e cerca dettagli inventati.
4. **Verifica:** esegui un controllo diretto, poi accetta, correggi o fermati.

**Per l’email del laboratorio,** leggi il risultato riga per riga. Controlla orario, data, luogo e destinatari. Chiedi di rimuovere eventuali numeri di sala o link di iscrizione che non compaiono nel programma. L’elenco delle modifiche deve dire «orario corretto dalle 18:00 alle 19:00».

**Bozza di esempio:**

```text
Oggetto: Introduzione alla sicurezza digitale il 12 novembre

Ciao,

La lezione Introduzione alla sicurezza digitale inizia alle 19:00
il 12 novembre 2026, nella sala comunitaria A.

Ti aspettiamo.

Modifica fattuale: l’orario di inizio è stato corretto dalle 18:00 alle 19:00.
```

**Registro di revisione d’esempio:** orario, superato, le 19:00 corrispondono al programma. Altri fatti, superato, evento, data e sala coincidono. Ambito, superato, è una bozza. Elenco modifiche, superato, è indicata l’unica correzione. Questi controlli riguardano l’esempio sintetico mostrato. La tua esecuzione richiede una verifica distinta.

| Controllo | Condizione di superamento | Se non passa |
|---|---|---|
| **Orario** | La bozza indica le 19:00 | Torna al programma approvato |
| **Altri fatti** | Data e luogo corrispondono alla fonte | Elimina le aggiunte non supportate |
| **Ambito** | Il messaggio è una bozza | Ferma ogni invio |
| **Registro** | L’elenco indica la correzione | Chiedi un confronto dei fatti |

**Un controllo superato è un’osservazione.** La frase dell’assistente «verificato» non è un controllo. Confronta tu il risultato con il programma approvato oppure usa una verifica separata e affidabile.

**Mantieni espliciti i limiti delle azioni.** Preparare un promemoria è reversibile. Inviarlo raggiunge i destinatari. Prima di un invio reale, chiedi un’approvazione separata e attuale e controlla i destinatari.

## Scegliere la quantità giusta di IA

**Usa una risposta in chat** per una breve bozza o spiegazione. Usa un progetto se più conversazioni correlate richiedono le stesse istruzioni e gli stessi file. Usa un agente di programmazione se il compito richiede ricerca nel repository, modifiche e test. Coinvolgi un altro collaboratore se una ricerca o revisione indipendente evita di sovraccaricare la conversazione principale di dettagli.

**Per una sola email del laboratorio, scegli una risposta in chat.** Se prepari promemoria per ogni lezione, aggiungi a un progetto il programma approvato e le indicazioni di stile. Un agente di programmazione non serve per questa email, perché non è richiesta una modifica al repository.

**Non delegare un compito poco chiaro.** Ogni collaboratore aggiuntivo ha bisogno di una domanda delimitata e di un modo per controllare il risultato. Le prossime lezioni mostrano quando il lavoro parallelo vale il costo.

## Esercitarsi e verificare

**Il tuo artefatto:** conserva un pacchetto per un’attività innocua che controlli. Includi il risultato desiderato, una fonte autorevole, due vincoli e un controllo di completamento. Eseguilo una volta nello strumento di chat scelto.

**Ragionamento atteso:** il risultato segue la fonte indicata, resta entro l’ambito richiesto ed esclude fatti non supportati. Registra una correzione fatta durante la verifica. Se non è servita alcuna correzione, annota le righe della fonte controllate.

**Criterio di completamento:** assegna un punto per l’orario corretto, gli altri fatti, il solo ambito di bozza e l’elenco fattuale delle modifiche. Completa la lezione con quattro punti su quattro rispetto al programma sintetico.

## Verificare la comprensione

1. **Domanda:** quale fonte determina l’orario se la cronologia della chat contraddice il programma approvato? **Risposta:** il programma approvato.
2. **Domanda:** quali prove chiudono il compito quando la bozza sembra plausibile? **Risposta:** controllo della fonte, del risultato e dell’accesso, più la registrazione dell’esito.

## Risoluzione dei problemi

- **Risposta vaga:** restringi il risultato richiesto e aggiungi un esempio.
- **Dettaglio inventato:** chiedi una fonte e rimuovi il testo senza supporto.
- **Risposta lunga:** imposta un limite di lunghezza o formato nel pacchetto.
- **Errore ripetuto:** avvia una nuova conversazione con la fonte corretta e un riepilogo breve.

## Passi successivi

**Continua con [Progetti ChatGPT e Claude](/articles/effective-ai-chat-projects/)** per tenere insieme istruzioni e file correlati.

**Navigazione del corso:** [Precedente: Configurazione del corso](/articles/effective-ai-course-setup/), [Indice del corso](/effective-ai-course-start/).
