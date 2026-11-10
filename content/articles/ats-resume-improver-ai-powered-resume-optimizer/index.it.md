---
title: "ATS Resume Improver: ottimizzatore CV gratuito con IA"
date: 2026-07-22
lastmod: 2026-11-08
toc: true
draft: false
description: "ATS Resume Improver è uno strumento gratuito e open source per ottimizzare i CV. Senza chiave IA, il testo viene elaborato nel browser. Con OpenAI o Anthropic, CV e descrizione dell'offerta vengono inviati direttamente al provider. Ollama può funzionare in locale."
genre: ["Strumenti per la carriera", "Progetti open source", "Intelligenza artificiale", "Tecnologie per la privacy", "Strumenti per sviluppatori", "Ricerca di lavoro", "Produttività"]
tags: ["ATS Resume Improver", "ottimizzazione ATS", "scanner CV", "CV con IA", "CV OpenAI", "CV Claude", "IA locale Ollama", "self-hosting", "privacy al primo posto", "strumenti per cercare lavoro", "analisi delle lacune di parole chiave", "lettera di presentazione", "punteggio CV", "React", "TypeScript", "Docker", "Vite", "open source", "esportazione PDF", "esportazione DOCX", "parser CV", "strumenti per la carriera", "preparazione colloqui", "stima dello stipendio", "rilevamento tipo di CV", "punteggio ATS", "strumento CV gratuito", "GitHub", "nessuna raccolta dati"]
cover: "/img/cover/ai-resume-optimizer-self-hosted-ats-analysis.webp"
coverAlt: "Un laptop moderno su una scrivania mostra un'interfaccia colorata per ottimizzare il CV con grafici, su uno sfondo blu navy scuro."
coverCaption: "ATS Resume Improver analizza e ottimizza il CV interamente nel browser, senza raccogliere dati."
canonical: "https://simeononsecurity.com/articles/ats-resume-improver-ai-powered-resume-optimizer/"
---

**Gratuito, open source e installabile sul tuo server. Il CV non raggiunge mai un server, a meno che tu non usi un provider di IA. Anche in quel caso, il testo va direttamente al provider di IA, non a noi.**

## Che cos'è ATS Resume Improver?

**[ATS Resume Improver](https://atsresumeimprover.netlify.app/)** è un ottimizzatore di CV open source basato sul browser. Analizza il CV rispetto a un annuncio di lavoro e aiuta a colmare la distanza tra ciò che hai e ciò che valutano i sistemi di tracciamento delle candidature (ATS). È sviluppato con React 19, Vite e TypeScript. L'intera **pipeline di analisi e valutazione viene eseguita nel browser**, senza un server backend.

Il codice sorgente è disponibile su **[github.com/simeononsecurity/ats-resume-improver](https://github.com/simeononsecurity/ats-resume-improver)**. Puoi usare la versione ospitata, distribuire la tua istanza su Vercel/Netlify/Cloudflare/GitHub Pages con un clic oppure avviarla localmente con Docker.

### Il problema di privacy che risolve

La maggior parte dei servizi di ottimizzazione dei CV carica il documento sui propri server, lo valuta con sistemi proprietari e conserva i dati. ATS Resume Improver adotta un approccio diverso.

| Modalità | Dati che lasciano il dispositivo |
|------|------------------------|
| **Senza chiave IA** | Nulla. Tutto resta locale e funziona nel browser. |
| **OpenAI / Anthropic** | Il testo del CV e la descrizione del lavoro vanno direttamente all'API del provider IA con la tua chiave, senza server intermedi. |
| **Ollama (locale)** | Nulla. Il modello viene eseguito sul tuo computer. |

**Le chiavi API sono conservate solo in memoria** e scompaiono quando chiudi la scheda. Nessuna analisi, tracciamento o cookie.

______

## Funzioni principali

### Cosa funziona senza una chiave IA

Non serve una chiave API per ottenere valore concreto. La modalità senza chiave include:

- **Caricamento CV**: PDF, DOCX, TXT o Markdown
- **Estrazione del testo ATS**: mostra esattamente ciò che l'ATS legge dal file, compreso ciò che si perde con la formattazione
- **Rilevamento del tipo di CV**: identifica automaticamente quale dei 7 profili corrisponde al CV e adatta l'ordine delle sezioni
- **Rilevamento delle sezioni e avvisi di formattazione**: segnala sezioni mancanti e formati difficili per i parser
- **Punteggio ATS (0–100)** con suddivisione in 5 dimensioni
- **Analisi delle lacune di parole chiave**: confronto basato su regole con la descrizione del lavoro
- **Ottimizzazione ATS deterministica**: riorganizzazione locale basata su regole
- **Visualizzatore delle differenze prima/dopo**: mostra esattamente le modifiche
- **Esportazione professionale in PDF, DOCX, TXT e Markdown**

### Cosa aggiunge l'IA

Collega OpenAI, Anthropic Claude o Ollama in locale per aggiungere queste funzioni:

- **Analisi semantica delle parole chiave**: comprende il contesto invece di limitarsi a confrontare stringhe. Mostra la forza della corrispondenza (forte/moderata/parziale), la posizione ("trovata in Competenze e 3 ruoli"), l'importanza della parola chiave (critica/alta/media/bassa) e una sintesi narrativa di 2-3 frasi generata dall'IA
- **Ottimizzazione del CV con IA**: riscrittura completa con prompt basati sulle buone pratiche ATS
- **Esportazione migliorata dall'IA**: l'IA formatta il PDF/DOCX prima del download
- **Generazione di lettere di presentazione**: regole di scrittura che eliminano i segnali tipici dell'IA (vedi sotto)
- **Previsione delle domande di colloquio**: basata sull'annuncio di lavoro
- **Stima della fascia salariale**

______

## Rilevamento del tipo di CV

L'app classifica automaticamente il CV in uno dei 7 profili e adatta l'ordine delle sezioni alle aspettative di recruiter e ATS per la fase professionale corrispondente:

| Profilo | Indicato per | Priorità delle sezioni |
|---------|----------|-----------------|
| 🏢 **Professionista esperto** | Oltre 5 anni, carriera lineare | Esperienza → Competenze → Istruzione |
| 🌱 **Livello intermedio** | 2–5 anni | Esperienza → Competenze → Istruzione |
| 🎓 **Inizio carriera** | 0–2 anni | Competenze → Istruzione → Progetti → Esperienza |
| 🎒 **Studente / neolaureato** | Ancora iscritto | Istruzione → Progetti → Competenze → Esperienza |
| 🔬 **Accademico / ricercatore** | Dottorato, pubblicazioni | Istruzione → Ricerca → Pubblicazioni → Esperienza |
| 📜 **Molte certificazioni** | Le certificazioni pesano più del titolo | Certificazioni → Competenze → Esperienza → Istruzione |
| 🔄 **Cambio di carriera** | Rilevata una pausa o un cambio | Sintesi → Competenze trasferibili → Istruzione → Esperienza |

*L'ordine delle sezioni si applica in modo uniforme all'ottimizzazione e alle esportazioni PDF, DOCX, TXT e Markdown, non solo alla schermata.*

______

## Analisi semantica delle parole chiave con IA

È qui che lo strumento si distingue dai semplici contatori di parole chiave. Quando configuri un provider IA, l'analisi delle lacune passa dal confronto letterale al ragionamento semantico:

| Dimensione | Senza IA | Con IA |
|-----------|-----------|---------|
| **Metodo di confronto** | Solo corrispondenza esatta | Comprensione semantica del contesto |
| **Forza della corrispondenza** | — | Valutazioni forte / moderata / parziale |
| **Contesto della corrispondenza** | — | "trovata in Competenze e 3 ruoli" |
| **Importanza della lacuna** | Tutte le lacune hanno lo stesso peso | Critica / alta / media / bassa |
| **Suggerimenti** | Consigli generici | Suggerimenti pratici per ogni parola chiave |
| **Copertura %** | Basata sul conteggio delle stringhe | Ponderata semanticamente |
| **Sintesi** | — | Narrazione IA di 2–3 frasi |

*L'analisi locale basata su regole funziona subito. L'IA la arricchisce in modo asincrono mentre esamini i risultati.*

______

## Provider IA supportati

Ogni chiamata IA include prompt basati sulle buone pratiche ATS e sulle linee guida di Harvard OCS e Columbia CCE.

### OpenAI

| Modello | Ideale per |
|-------|----------|
| **GPT-4.1 mini** (predefinito) | Intelligente, rapido e conveniente, consigliato |
| GPT-4o mini | Opzione classica, rapida e conveniente |
| GPT-4.1 | Ultimo GPT-4.1, segue le istruzioni con precisione |
| GPT-4o | Modello di punta ad alta qualità |
| GPT-4 Turbo | Ampia finestra di contesto |
| GPT-3.5 Turbo | Il più rapido e meno costoso |

**Costo stimato**: circa $0,002-$0,05 per analisi del CV.

### Anthropic Claude

| Modello | Ideale per |
|-------|----------|
| **Claude Sonnet 4.5** (predefinito) | Rapido e intelligente, consigliato |
| Claude Opus 4.5 | Il più capace, ideale per compiti complessi |
| Claude Haiku 4.5 | Il più rapido e meno costoso |
| Claude 3.5 Sonnet | Affidabile e collaudato |
| Claude 3.5 Haiku | Rapido ed economico, v3.5 |

### Ollama (locale / self-hosted)

Non serve una chiave API. Esegui il modello sul tuo hardware. Imposta `OLLAMA_ORIGINS=*` per consentire l'accesso dal browser.

| Modello | Note |
|-------|-------|
| **Llama 3.3** (predefinito) | Ultimo Meta Llama, consigliato |
| Llama 3.2 | Meta Llama 3.2 |
| Mistral 7B | Rapido e capace |
| Mixtral 8x7B | Mixture of experts |
| Qwen 2.5 | Alibaba Qwen 2.5 |
| DeepSeek R1 | Modello di ragionamento avanzato |
| Phi-4 | Microsoft Phi-4 |
| Gemma 3 | Google Gemma 3 |

Eseguire Ollama in locale rende lo strumento completamente offline. Nessun dato lascia il computer.

______

## Rendere naturali le lettere di presentazione

Il generatore di lettere di presentazione applica una guida di stile precisa per eliminare i segnali tipici del testo generato dall'IA. Ispirato al [framework di umanizzazione di Sabrina Ramonov](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing), ogni lettera rispetta queste regole:

- **Niente em dash**: il segnale più evidente dell'IA viene eliminato del tutto
- **Oltre 50 parole e frasi vietate**: leverage, utilize, dive deep, delve, embark, game-changer, groundbreaking, cutting-edge, pivotal, tapestry, harness, moreover, in conclusion, it's worth noting, ever-evolving, landscape, testament, not only...but also e altre
- **Niente Markdown nel corpo della lettera**: niente asterischi per il grassetto, hashtag o punti e virgola
- **Forma attiva per impostazione predefinita**: forma passiva solo quando il soggetto non conta davvero
- **Contrazioni obbligatorie**: "I've", "I'm", "it's", mai "I have", "I am", "it is"
- **Frasi di lunghezza variabile**: frasi brevi e incisive alternate a frasi più lunghe
- **Niente introduzioni riempitive**: "It's important to note that X" diventa semplicemente "X"
- **Dettaglio concreto dell'annuncio nel primo paragrafo**: dimostra che la lettera non è un modello precompilato

*Il risultato sembra scritto da una persona, perché le regole impongono al modello uno stile naturale.*

______

## Qualità dell'esportazione

| Formato | Contenuto |
|--------|-------------|
| **PDF** | Tipografia professionale, separatori di sezione, elenchi puntati, intestazione con contatti |
| **DOCX** | Documento Word ben strutturato (Packer.toBlob, compatibile con il browser) |
| **TXT** | Testo semplice e pulito, con spaziatura uniforme, adatto agli ATS |
| **Markdown** | File `.md` strutturato con titoli ed elenchi |

Con un provider IA configurato, l'esportazione viene formattata dall'IA prima del download e contrassegnata con il badge ✨ AI-Enhanced.

______

## Hosting autonomo

### Versione ospitata (nessuna configurazione)

Usa l'app disponibile su **[atsresumeimprover.netlify.app](https://atsresumeimprover.netlify.app/)**: non servono account, registrazione o carta di credito.

### Distribuzione cloud con un clic

| Piattaforma | Link |
|----------|------|
| **Vercel** | Distribuzione con un clic dal repository |
| **Cloudflare Pages** | Distribuzione con un clic |
| **Netlify** | Distribuzione con un clic |
| **GitHub Pages** | Fork → Settings → Pages → GitHub Actions → distribuzione automatica |

### Sviluppo locale

```bash
git clone https://github.com/simeononsecurity/ats-resume-improver
cd ats-resume-improver

make install
make dev           # http://localhost:5173
```

### Docker (consigliato per ambienti riproducibili)

```bash
# Development — hot-reload on http://localhost:5173
make docker-dev

# Production — nginx on http://localhost:8080
make docker-prod

# Dev + Ollama together (full local AI stack)
make docker-dev-with-ollama
```

### Stack Ollama completamente offline

```bash
# Start Ollama container (persists models across restarts)
make ollama

# Pull a model
make ollama-pull MODEL=llama3.2

# Start dev app + Ollama side-by-side
make docker-dev-with-ollama
```

Poi apri l'app, vai al pannello della chiave API, seleziona **Ollama (Local)**, imposta l'URL su `http://localhost:11434` e scegli un modello. Nessun dato lascia il computer.

______

## Stack tecnologico

| Livello | Tecnologia |
|-------|-----------|
| **Framework** | React 19 + TypeScript |
| **Build** | Vite 8 |
| **Stile** | Tailwind CSS v4 |
| **Icone** | Lucide React |
| **Parser PDF** | pdfjs-dist |
| **Parser DOCX** | mammoth |
| **Esportazione PDF** | jsPDF |
| **Esportazione DOCX** | docx (Packer.toBlob) |
| **IA** | OpenAI · Anthropic Claude · Ollama |
| **Container** | Docker + nginx (multi-stage) + servizio Ollama |

L'intera pipeline di analisi e valutazione (`atsAnalyzer.ts`, `keywordMatcher.ts`, `resumeTypeDetector.ts`) gira nel browser. Le integrazioni IA in `aiProvider.ts` chiamano le API dei provider direttamente dal client, senza un server proxy.

______

## Guida pratica all'uso

### Passaggio 1: carica il CV

Carica un file PDF, DOCX, TXT o Markdown. Apri la scheda **"What the ATS Sees"** per verificare che il parser abbia estratto correttamente il contenuto. Se mancano sezioni o sono illeggibili in questa vista, il software ATS dei recruiter avrà lo stesso problema.

### Passaggio 2: incolla la descrizione del lavoro

Incolla l'intero annuncio nel pannello Job Description. Gli annunci più completi producono un'analisi delle parole chiave migliore: non tagliare la sezione dei requisiti.

### Passaggio 3: controlla il punteggio ATS

Il pannello mostra un punteggio complessivo da 0 a 100 e la suddivisione in 5 dimensioni. La suddivisione indica dove intervenire: problemi di formato abbassano una dimensione, parole chiave mancanti un'altra e descrizioni deboli dell'esperienza una terza.

### Passaggio 4: verifica le lacune di parole chiave

La vista Keyword Analysis mostra quali parole dell'annuncio compaiono nel CV e quali mancano. Con l'IA attiva, ottieni corrispondenze semantiche e valutazioni di importanza. Una lacuna "Critical" in una competenza tecnica centrale merita più attenzione di una lacuna "Low" in una parola generica sulle competenze trasversali.

### Passaggio 5: ottimizza

- **Modalità deterministica**: riorganizza il CV secondo regole. Sicura, rapida e senza costi API.
- **Modalità IA**: riscrittura completa con un LLM e prompt basati sulle buone pratiche ATS.

Esamina le **differenze prima/dopo** per capire ogni modifica prima di accettarla.

### Passaggio 6: esporta

Esporta in PDF, DOCX, TXT o Markdown. Con l'IA attiva, l'esportazione viene formattata per una presentazione professionale. Il modello PDF usa una tipografia adeguata e un layout familiare ai recruiter.

______

## Integrazione dei consigli per il CV

Lo strumento include il documento di riferimento `RESUME_TIPS.md` (anche nel repository GitHub), che spiega:

- Come valutano davvero i CV i sistemi ATS
- Le regole di formattazione importanti e cosa compromette i parser
- Come scrivere riepiloghi, punti elenco e sezioni delle competenze efficaci
- Strategia per le parole chiave senza accumularle artificialmente
- Tono e struttura di una lettera di presentazione
- Lista di controllo prima dell'invio

*Leggilo prima di usare lo strumento per capire cosa significano i punteggi.*

______

## Domande frequenti

### Lo strumento memorizza il mio CV?

No. L'app funziona interamente lato client. Nessun dato viene salvato su un server. I dati della sessione restano nella memoria del browser e scompaiono quando chiudi la scheda.

### Il mio CV ha un punteggio basso. Devo preoccuparmi?

I punteggi ATS sono indicativi, non determinano un esito positivo o negativo. Un punteggio pari a 60 non significa che un ATS ti rifiuterà: indica differenze misurabili tra il tuo CV e la specifica descrizione del lavoro analizzata. Usa il punteggio per stabilire quali modifiche fare prima, non come verdetto.

### Posso usarlo con più descrizioni di lavoro?

Sì. Incolla una nuova descrizione quando vuoi. L'analisi delle parole chiave e l'ottimizzazione verranno ripetute per il nuovo annuncio. Ogni analisi è indipendente.

### L'integrazione Ollama funziona davvero offline?

Sì, se Ollama gira sul tuo computer o su un computer della rete locale. L'app invia il testo alla tua istanza Ollama tramite HTTP. Nessun dato raggiunge servizi esterni.

### Quanto è preciso il rilevamento del tipo di CV?

Il rilevatore applica euristiche basate su regole al contenuto del CV: anni di esperienza, indicatori di istruzione, sezioni di pubblicazioni o ricerca e segnali di pause lavorative. Funziona bene per la maggior parte dei CV, ma può sbagliare con percorsi insoliti. L'ordine delle sezioni applicato è sempre modificabile.

______

## Tabella di marcia del progetto

Funzioni in sviluppo o pianificate:

- Cronologia delle versioni del CV tramite IndexedDB
- Ottimizzatore del profilo LinkedIn
- Supporto per Google Gemini
- Altri modelli Ollama

Il progetto usa la licenza MIT e accetta pull request. Apri prima un issue per le modifiche importanti.

______

## Conclusione

**ATS Resume Improver** colma una lacuna reale: offre un'analisi seria del CV senza affidare i dati a intermediari. La modalità senza chiave fornisce subito consigli pratici su formattazione e copertura delle parole chiave. Una chiave IA aggiunge ragionamento semantico, scrittura di lettere di presentazione e preparazione ai colloqui, per pochi centesimi a ogni analisi o gratis con Ollama.

La versione ospitata è disponibile su **[atsresumeimprover.netlify.app](https://atsresumeimprover.netlify.app/)**. Il codice completo è su **[github.com/simeononsecurity/ats-resume-improver](https://github.com/simeononsecurity/ats-resume-improver)**.

Se vuoi ospitare lo strumento per cercare lavoro o personalizzare i pesi dei punteggi e i prompt per un settore specifico, la configurazione Docker e la struttura pulita del progetto rendono semplice creare una fork e adattarla.

______

## Corso di ottimizzazione del CV

Per una guida strutturata e passo passo su tutto ciò che valuta lo strumento, segui il corso complementare:

**[Corso di ottimizzazione del CV: supera i sistemi ATS e ottieni più colloqui](/resume-optimization-course-start/)** — 9 moduli su punteggi ATS, formattazione, punti elenco, parole chiave, personalizzazione, lettere di presentazione e lista di controllo prima dell'invio. Usa lo strumento insieme al corso per ricevere feedback immediato a ogni passaggio.

______

## Riferimenti

1. [ATS Resume Improver — strumento online](https://atsresumeimprover.netlify.app/)
2. [ATS Resume Improver — repository GitHub](https://github.com/simeononsecurity/ats-resume-improver)
3. [Consigli per il CV — RESUME_TIPS.md](https://github.com/simeononsecurity/ats-resume-improver/blob/main/RESUME_TIPS.md)
4. [Sabrina Ramonov — il miglior prompt IA per rendere umano un testo generato dall'IA](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing)
5. [Documentazione API OpenAI](https://platform.openai.com/docs/)
6. [Documentazione API Anthropic Claude](https://docs.anthropic.com/)
7. [Ollama — server LLM locale](https://ollama.com/)
