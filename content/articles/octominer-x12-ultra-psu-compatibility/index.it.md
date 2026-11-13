---
title: "Compatibilità degli alimentatori Octominer X12 Ultra: prova sul campo Chicony e LiteOn"
date: 2026-11-12
lastmod: 2026-11-12
toc: true
draft: false
description: "Una prova con cinque ventole e tre alimentatori su un Octominer X12 Ultra ha mostrato che un alimentatore Chicony avviava il sistema, mentre le unità LiteOn testate segnalavano l’ambra e non partivano."
genre: ["Hardware per il mining", "Hardware informatico"]
tags: ["Octominer X12 Ultra", "alimentatore server", "compatibilità alimentatori", "Chicony R12-1K6P2A", "LiteOn PS-2142-2L"]
cover: "/img/cover/octominer-x12-ultra-psu-compatibility.webp"
coverAlt: "Illustrazione astratta di tre alimentatori server in uno chassis con indicatori verdi, ambra e grigi"
coverCaption: ""
---

**Il Chicony R12-1K6P2A ha avviato il mio Octominer X12 Ultra con cinque ventole e tre alimentatori.** Gli alimentatori LiteOn PS-2142-2L provati hanno mostrato una luce verde, sono passati all’ambra e non hanno avviato il sistema. Il risultato riguarda la mia unità con una scheda di alimentazione **OCTOMINER (12PIN) 3x DPS1200 rev. 20**. La stessa potenza nominale o una lista per una scheda breakout X12 separata non dimostrano la compatibilità con una scheda Octominer.

Lo chassis era venduto come **configurazione da 3.600 W** con tre alloggiamenti per alimentatori. [Octominer propone un’opzione con tre alimentatori da 1.200 W](https://octominer.eu/product/octominer-x12-ultra-used/) per l’X12 Ultra, oltre ad altre configurazioni. Controlla l’etichetta e la scheda di alimentazione del tuo sistema prima di applicare questi risultati.

## Risultati della prova

| Alimentatore | Risultato in questo sistema |
|---|---|
| **Chicony R12-1K6P2A, 1.600 W** | Ha avviato il sistema nella mia prova. L’articolo non ha misurato il carico prolungato né il funzionamento in tutti gli alloggiamenti. |
| **LiteOn PS-2142-2L, 1.400 W** | Le unità provate si sono illuminate di verde, poi di ambra. Il sistema non è partito. |
| **Dell/Delta D1200E-S0, Dell 0F37X3** | L’ingresso CA insolito ha complicato la ricerca di un cavo adatto. Non ho registrato risultati di avvio o carico per questo alimentatore. |
| **HP HSTNS-PD30, 1.200 W** | Provato nello stesso sistema. Non ha avviato il sistema. |
| **Altri modelli HP Common Slot** | I kit Platinum Plus da 1.200 W e le unità da 750 W HSTNS-PD22B, HSTNS-PL22B e HSTNS-PD18 provati non hanno avviato questo sistema. I numeri di modello esatti degli alimentatori nei kit non sono stati registrati. |

**Non interpretare il risultato LiteOn come una diagnosi di guasto per tutti i PS-2142-2L.** La sequenza osservata indica un avvio fallito in questo chassis. La prova non ha isolato il segnale di abilitazione, lo scambio di telemetria, il pinout della scheda o un guasto di un singolo alimentatore. Allo stesso modo, il risultato Chicony dimostra un avvio riuscito, non una potenza certificata dello chassis di 4.800 W né l’affidabilità a lungo termine.

## Quale Chicony ha avviato il sistema?

Il modello che ha funzionato era **Chicony R12-1K6P2A**, indicato anche come parte **R1K6A002L** nella [tabella di compatibilità di Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). Il suo [rapporto di prova 80 PLUS](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/chicony-power-r121k6p2a-5866.pdf) identifica un alimentatore da 1.600 W con tensione nominale di **200-240 V CA**, 10 A e 50-60 Hz. Nelle condizioni di prova a 230 V, il rapporto ha misurato un’efficienza del 94,19% a metà carico. Questi valori descrivono l’alimentatore testato, non l’intero impianto di mining.

La specifica di **200-240 V è importante**. Non presumere che questo modello eroghi la potenza nominale da una presa a 120 V. Secondo una [scheda ricambi server per il modello esatto](https://www.itcreations.com/product/142080), l’alimentatore provato ha un ingresso C14 standard. Usa cavi e apparecchiature di distribuzione adeguati alla tensione e alla corrente d’ingresso.

La mia prova ha confermato un avvio riuscito con il Chicony su questa specifica scheda. Non dimostra la compatibilità con tutte le revisioni dell’X12 Ultra. Verifica il numero di modello completo e l’etichetta prima di ordinare altri alimentatori.

## Perché la lista LiteOn mi ha tratto in inganno

Il **LiteOn PS-2142-2L** compare nella [tabella di compatibilità delle schede breakout X12 di Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). Il suo [rapporto 80 PLUS](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/liteon-technology-corporation-ps21422l-6889.pdf) identifica un modello da 1.400 W. Queste fonti confermano il modello e l’uso indicato con **l’adattatore X12 di Parallel Miner**. Nessuna prova la scheda di alimentazione OEM di Octominer.

Le mie unità PS-2142-2L sono passate dal **verde all’ambra** dopo l’inserimento e il sistema non è partito. Lame di uscita simili non dimostrano un comportamento uguale di avvio, stato o comunicazione. La sequenza dei LED da sola non prova quale differenza abbia causato il mancato avvio.

La stessa [tabella Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/) raggruppa **Dell/Delta D1200E-S0**, **LiteOn PS-2142-2L** e **Chicony R12-1K6P2A** nella famiglia di adattatori a otto pin. Colloca **HP HSTNS-PD30** e diversi alimentatori HP Common Slot da 750 W in un’altra famiglia con adattatori a sei pin. Nessuna unità HP che ho provato ha avviato questo sistema. La tabella descrive le schede Parallel Miner, non un elenco di ricambi per la scheda **OCTOMINER (12PIN)**.

## Controlla alimentazione e cablaggio

La [guida alla risoluzione dei problemi dell’Octominer X12 Ultra](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) indica che lo chassis, da solo, consuma fino a **200 W con le ventole alla massima velocità**. Raccomanda almeno un **10% di margine di potenza** e sconsiglia di superare il **90% della potenza nominale degli alimentatori installati**. Considera il consumo delle GPU, dello chassis e la potenza effettiva degli alimentatori alla tua tensione CA.

**Un’etichetta da 1.600 W su ciascun alimentatore Chicony non trasforma la configurazione pubblicata da 3.600 W dello chassis in una da 4.800 W.** Anche la scheda di alimentazione, il cablaggio interno, i connettori, la distribuzione CA e il raffreddamento limitano il sistema. Non ho misurato questi limiti su questa unità. Mantieni il sistema entro la configurazione documentata finché Octominer non conferma una potenza superiore per la revisione esatta della scheda.

Il Dell/Delta **D1200E-S0 / 0F37X3** presentava un problema diverso: l’ingresso CA sul lato dell’alimentatore richiedeva un cavo di accoppiamento meno comune. In una ricerca precedente ho identificato l’ingresso come **LS-25** e il connettore lato cavo come **LS-26**, in base all’unità e agli annunci dei cavi. Verifica la forma del connettore e i dati elettrici prima di acquistare un cavo. Una spina C13 dall’aspetto familiare non sostituisce il connettore corretto.

## Verifica il tuo X12

1. **Registra l’hardware esatto.** Fotografa l’etichetta dello chassis, quella dell’alimentatore, l’ingresso CA, la lama di uscita e la revisione della scheda di alimentazione. Conta ventole e alloggiamenti.
2. **Controlla l’alimentazione CA.** Confronta i valori d’ingresso dell’alimentatore con quelli della presa, del cavo e della PDU. Il rapporto del Chicony R12-1K6P2A specifica 200-240 V CA.
3. **Prova una configurazione minima.** Spegni e scollega ogni alimentazione CA prima di cambiare alimentatore, GPU o collegamento PSON. [La guida Octominer](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) consiglia di controllare l’inserimento e i LED dell’alimentatore, il cavo PSON a sei pin tra scheda madre e scheda di alimentazione, e un alimentatore con una GPU per isolare un problema di avvio.
4. **Registra il risultato.** Annota modello dell’alimentatore, alloggiamento, sequenza dei LED, avvio della scheda e delle ventole e avvio del sistema. Ripeti la prova in altri alloggiamenti solo dopo uno spegnimento sicuro.
5. **Misura prima di aggiungere carico.** Controlla la telemetria dell’alimentatore e la potenza alla presa con il carico GPU previsto. L’avvio descritto in questo articolo non sostituisce una prova sotto carico.

## Conclusione

**Il Chicony R12-1K6P2A è l’unico ricambio di questo confronto con un avvio riuscito segnalato nel mio X12 Ultra a tre alloggiamenti.** Le unità LiteOn PS-2142-2L testate sono passate dal verde all’ambra e non sono partite. Neppure le unità HP Common Slot provate hanno avviato il sistema. Considera gli altri elenchi di alimentatori come piste di ricerca finché il modello esatto e la scheda Octominer non superano una prova controllata di avvio e carico. Inizia dalle etichette dei modelli e dalla revisione della scheda. Consulta le indicazioni di alimentazione Octominer prima di aumentare il carico delle GPU.
