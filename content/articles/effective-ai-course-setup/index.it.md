---
title: "Configurazione del corso sui flussi di lavoro con IA: terminale, Git e laboratorio pratico"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Prepara uno spazio sicuro per esercitarti con l’IA, impara i termini di terminale e Git del corso e avvia il laboratorio iniziale."
genre: ["Intelligenza artificiale", "Ingegneria del software", "Istruzione"]
tags: ["configurazione corso IA", "basi del terminale", "basi di Git", "prerequisiti per agenti di programmazione", "laboratorio pratico IA", "corso IA per principianti"]
cover: "/img/cover/effective-ai-course-setup.webp"
coverAlt: "Spazio di pratica per principianti con simboli di terminale, Python e Git, cartella di laboratorio contrassegnata e archivio di ripristino"
coverCaption: ""
---

[Torna al corso pratico sui flussi di lavoro IA](/effective-ai-course-start/)

**Prepara uno spazio sicuro prima di usare un agente.** Le lezioni 1 e 2 funzionano nel browser senza questo laboratorio. Torna qui prima della lezione 3 per seguire il corso completo. Le lezioni pratiche di programmazione usano Git, Python 3.10 o successivo e un agente di programmazione. Nel percorso di studio, le azioni dell’agente non disponibili sono sostituite da attività manuali segnalate.

**Risultato di apprendimento:** eseguirai il laboratorio iniziale, salverai una base locale e spiegherai come ripristinare una copia usa e getta.

## Punti chiave

- **Percorso browser:** completa gli esercizi su chat, pianificazione, verifica delle fonti e revisione in ChatGPT o Claude.
- **Percorso locale:** usa un terminale e il laboratorio Python fornito per gli esercizi di programmazione.
- **Percorso di ripristino:** estrai una nuova copia del laboratorio quando un esercizio va storto.
- **Regola di sicurezza:** tieni fuori dal laboratorio file privati, dati dei clienti e credenziali.

## Scegli il percorso

| Percorso | Requisiti | Attività |
|---|---|---|
| **Introduzione nel browser** | Browser aggiornato e account ChatGPT o Claude | Lezioni 1 e 2, più il pacchetto di attività chat della lezione 1 |
| **Pratica locale** | Git, Python 3.10 o successivo, terminale e un agente di programmazione | File, differenze, test e modifiche dell’agente |
| **Corso di studio** | Browser, Python 3.10 o successivo locale e Git | Tutti i controlli del laboratorio; passaggi agente e MCP non disponibili sono contrassegnati come non eseguiti |

**Ogni prodotto definisce i propri piani e limiti.** Prima di affidarti a una funzione, controlla [ChatGPT Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) e [Claude Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects). Il percorso di studio non dimostra esperienza pratica con un agente di programmazione non disponibile. Annota questa distinzione nelle note finali.

**Segui un percorso predefinito:** usa ChatGPT nel browser per gli esercizi di chat, poi un agente di programmazione disponibile con il laboratorio locale. Claude è un’alternativa equivalente per la chat. Per la programmazione puoi scegliere Codex CLI, Claude Code CLI o OpenCode. Non servono account con tutti i fornitori.

**Registra cinque controlli preliminari prima di aprire un agente di programmazione.** Così distingui una verifica del laboratorio locale da un’affermazione su un account o uno spazio di lavoro ospitato.

| Controllo | Registra |
|---|---|
| **Spazio di lavoro** | Cartella esatta del laboratorio estratto che l’agente leggerà |
| **Esecuzione** | Computer locale o spazio remoto selezionato |
| **Fornitore** | Account o fornitore del modello usato per questa attività |
| **Permessi** | Scrittura di file e comandi shell consentiti o soggetti ad approvazione |
| **Base** | Conteggio osservato e due test superati prima delle modifiche |

**Mantieni limitata la radice di pratica.** Uno spazio ospitato richiede una copia propria del laboratorio sintetico. Un’esecuzione locale non dimostra che la copia remota o l’account abbiano gli stessi file e permessi.

## Impara i termini locali

| Termine | Significato semplice |
|---|---|
| **Terminale** | App in cui digiti i comandi |
| **Shell** | Software che interpreta i comandi |
| **CLI** | Interfaccia a riga di comando di un programma |
| **Directory di lavoro** | Cartella usata per impostazione predefinita da un comando |
| **Repository** | Progetto tracciato da Git |
| **Commit** | Istantanea salvata di Git |
| **Branch** | Linea denominata di modifiche Git |
| **Diff** | Visualizzazione delle righe aggiunte o rimosse |
| **Prova** | Controllo ripetibile del comportamento atteso |
| **Codice di uscita** | Numero che indica il successo o il fallimento di un comando |

**Per il laboratorio iniziale non serve GitHub.** Git funziona sul computer. GitHub è un servizio di hosting separato. Un commit locale salva un’istantanea senza inviare altrove i file.

## Prepara il laboratorio

**Scarica il [laboratorio iniziale del corso](/downloads/effective-ai-course-lab.zip)** ed estrailo in una nuova cartella sotto il tuo controllo. Apri un terminale lì. Su macOS o Linux, apri Terminal e usa `cd` per entrare nella cartella estratta. Su Windows usa PowerShell o Windows Terminal e `cd`. Su Windows, spesso il comando Python è `py -3` invece di `python3`.

**Installa [Python 3.10 o successivo](https://www.python.org/downloads/) e [Git](https://git-scm.com/downloads) se servono.** Controlla gli strumenti installati prima di avviare il laboratorio. I primi due comandi mostrano le versioni. `cd` cambia la directory di lavoro. `ls` elenca i file. Sostituisci il percorso di esempio con quello effettivo della cartella estratta.

```bash
python3 --version
git --version
cd /path/to/effective-ai-course-lab
ls
```

**In Windows PowerShell** usa `py -3 --version`, `git --version`, `cd C:\path\to\effective-ai-course-lab` e `Get-ChildItem`. L’elenco dovrebbe includere `task_report.py`, `tasks.json`, `tests` e `docs`. Se un comando di versione fallisce, completa l’installazione prima di proseguire.

```bash
pwd
python3 task_report.py tasks.json
python3 -m unittest discover -s tests -v
```

**In Windows PowerShell** puoi sostituire `pwd` con `Get-Location` e `python3` con `py -3` se Python usa il launcher. Il primo comando mostra il percorso, che deve terminare con la cartella estratta. Controlla anche i nomi dei file: `AGENTS.md.txt` non vale come `AGENTS.md`. In Esplora file attiva le estensioni per vedere il nome completo.

**Risultato previsto:** il rapporto indica `Total tasks: 4`. Il comando dei test mostra due test e termina con `OK`. In caso di successo, la shell restituisce codice zero. Un conteggio diverso o un traceback richiede di controllare la cartella e Python.

**Leggi un comando per parti.** In `python3 task_report.py tasks.json`, `python3` avvia Python, `task_report.py` è il programma e `tasks.json` indica i dati in ingresso. Il conteggio stampato è un risultato, non un altro comando. Dopo un errore, macOS e Linux mostrano lo stato con `echo $?`. PowerShell espone lo stato dell’ultimo programma nativo tramite `$LASTEXITCODE`.

**Calcola circa dieci minuti per la prima esecuzione** dopo aver installato Python: estrai il laboratorio, esegui il rapporto e confronta il totale con le quattro voci in `tasks.json`. Apri il file JSON in un editor e conta le voci a mano.

## Usa Git in sicurezza

**Avvia Git solo nella cartella estratta del laboratorio.** Questi comandi creano un’istantanea locale. `git status` mostra i file modificati. `git diff` mostra le righe cambiate dopo la modifica di un file tracciato.

```bash
git init
git add .
git commit -m "Base del laboratorio del corso"
git status --short
```

**Stato previsto:** dopo il commit non appaiono nomi di file. Se Git richiede nome ed email, configura da questa cartella un’identità dedicata al laboratorio e ripeti il commit. Sostituisci i valori d’esempio con valori privati. Non incollare dati d’identità o credenziali in una chat pubblica.

```bash
git config --local user.name "Studente del corso"
git config --local user.email "learner@example.invalid"
git commit -m "Base del laboratorio del corso"
git status --short
```

**Per ripristinare non serve un comando Git.** Salva le note fuori dal laboratorio, elimina la copia estratta e decomprimi di nuovo lo ZIP originale. Usa questo metodo se una modifica lascia il programma in uno stato sconosciuto.

## Proteggi lo spazio di pratica

**Usa esempi sintetici.** Non caricare documenti privati in un progetto del corso. Non inserire chiavi API nei prompt, file sorgente, schermate o commit. L’accesso dell’agente ai file e ai comandi dipende dai permessi e dalla cartella aperta. Controllali entrambi prima di lasciarlo operare.

**Controlla la condivisione prima del caricamento.** I file del progetto potrebbero essere accessibili ai membri. Per il lavoro reale segui le regole della tua organizzazione. Il corso usa dati fittizi, quindi il laboratorio non richiede un’approvazione speciale.

## Esercitati e verifica

**Il tuo risultato:** registra il percorso scelto, i cinque campi preliminari, il conteggio del rapporto, l’esito dei test e il metodo di ripristino. Usa una nuova copia per verificare di saper ripristinare il laboratorio.

**Ragionamento atteso:** sai quale cartella viene interessata dai comandi, distingui Git locale dall’hosting e conosci un metodo di recupero prima delle modifiche dell’agente.

## Verifica la comprensione

1. **Domanda:** Un’introduzione svolta solo nel browser completa il percorso del laboratorio locale? **Risposta:** No. Il percorso completo richiede una base locale di Python e Git.

2. **Domanda:** Cosa devi salvare prima di modificare il laboratorio usa e getta? **Risposta:** L’esito positivo del test iniziale e un punto pulito da cui ripristinare.

## Risoluzione dei problemi

- **Comando Python mancante:** installa Python 3 dal distributore ufficiale e riapri il terminale.
- **File non trovato:** controlla la directory di lavoro e visualizza i file della cartella estratta.
- **Test non eseguiti:** usa esattamente il comando nel README del laboratorio estratto.
- **Git chiede l’identità per il commit:** configura Git localmente e tieni i valori scelti fuori dagli appunti del corso.

## Prossimi passi

**Continua con il [flusso di lavoro IA affidabile](/articles/effective-ai-workflow-foundations/)**. Il primo esercizio usa lo stesso laboratorio sintetico prima che uno strumento riceva file reali.

**Navigazione del corso:** [Programma del corso](/effective-ai-course-start/).
