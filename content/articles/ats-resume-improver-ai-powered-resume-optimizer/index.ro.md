---
title: "ATS Resume Improver: Optimizator gratuit de CV-uri cu IA"
date: 2026-07-22
lastmod: 2026-11-08
toc: true
draft: false
description: "ATS Resume Improver este un instrument gratuit, open-source și rulat în client pentru analizarea, evaluarea, compararea, optimizarea și exportarea CV-urilor cu modele cloud sau locale."
genre: ["Instrumente pentru carieră", "Proiecte open-source", "Inteligență artificială", "Tehnologie pentru confidențialitate", "Instrumente pentru dezvoltatori", "Căutarea unui loc de muncă", "Productivitate"]
tags: ["ATS Resume Improver", "Optimizare ATS", "Scanner de CV-uri", "CV cu IA", "CV OpenAI", "CV Claude", "IA locală Ollama", "Găzduire proprie", "Confidențialitate pe primul loc", "Instrumente pentru căutarea unui loc de muncă", "Analiza lacunelor de cuvinte-cheie", "Scrisoare de intenție", "Evaluarea CV-ului", "React", "TypeScript", "Docker", "Vite", "Open-source", "Export PDF", "Export DOCX", "Parser de CV-uri", "Instrumente pentru carieră", "Pregătire pentru interviuri", "Estimator salarial", "Detectarea tipului de CV", "Scor ATS", "Instrument gratuit pentru CV", "GitHub", "Fără colectare de date"]
cover: "/img/cover/ai-resume-optimizer-self-hosted-ats-analysis.webp"
coverAlt: "Un laptop modern pe un birou afișează o interfață colorată de optimizare a CV-urilor, cu grafice, pe un fundal albastru închis."
coverCaption: "ATS Resume Improver analizează și optimizează CV-urile în întregime în client, fără colectare de date."
canonical: "https://simeononsecurity.com/articles/ats-resume-improver-ai-powered-resume-optimizer/"
---

**Gratuit, open-source și pregătit pentru găzduire proprie. CV-ul tău nu ajunge pe niciun server dacă nu folosești un furnizor de IA. Chiar și atunci, textul merge direct la furnizor, nu la noi.**

## Ce este ATS Resume Improver?

**[ATS Resume Improver](https://atsresumeimprover.netlify.app/)** este un optimizator de CV-uri care rulează în browser. Îți analizează CV-ul în raport cu descrierea unui loc de muncă și te ajută să reduci diferența dintre experiența ta și criteriile sistemelor de urmărire a candidaților (ATS). Este construit cu React 19, Vite și TypeScript. **Întregul proces de analiză și evaluare se desfășoară în browser**, fără server backend.

Codul sursă se află la **[github.com/simeononsecurity/ats-resume-improver](https://github.com/simeononsecurity/ats-resume-improver)**. Folosește versiunea găzduită, implementează propria copie cu un singur clic pe Vercel, Netlify, Cloudflare sau GitHub Pages ori ruleaz-o local cu Docker.

### Problema de confidențialitate pe care o rezolvă

Majoritatea serviciilor de optimizare a CV-urilor îl încarcă pe serverele lor, îi calculează un scor privat și păstrează datele. ATS Resume Improver folosește o abordare diferită.

| Mod | Date care părăsesc dispozitivul |
|------|------------------------|
| **Fără cheie IA** | Nimic. Totul rulează local în browser. |
| **OpenAI / Anthropic** | Textul CV-ului și descrierea postului ajung direct la API-ul furnizorului de IA, folosind cheia ta. Nu există server intermediar. |
| **Ollama (local)** | Nimic. Modelul rulează pe propriul computer. |

**Cheile API rămân doar în memorie** și dispar când închizi fila. Nu există analize, urmărire sau cookie-uri.

______

## Funcții principale

### Ce funcționează fără o cheie IA

Nu ai nevoie de o cheie API pentru rezultate utile. Modul fără cheie include:

- **Încărcarea CV-ului**: PDF, DOCX, TXT sau Markdown
- **Extragerea textului pentru ATS**: arată exact ce citește un ATS din fișier, inclusiv informațiile pierdute prin formatare
- **Detectarea tipului de CV**: identifică profilul potrivit dintre 7 opțiuni și ajustează ordinea secțiunilor
- **Detectarea secțiunilor și avertismente de formatare**: semnalează secțiunile lipsă și formatele greu de procesat
- **Scor ATS (0–100)** cu o analiză pe 5 dimensiuni
- **Analiza lacunelor de cuvinte-cheie**: comparare bazată pe reguli cu descrierea postului
- **Optimizare ATS deterministă**: restructurare locală bazată pe reguli
- **Vizualizator de diferențe înainte/după**: vezi exact ce s-a schimbat
- **Export profesional în PDF, DOCX, TXT și Markdown**

### Ce adaugă IA

Conectează OpenAI, Anthropic Claude sau Ollama local pentru a activa:

- **Analiza semantică a cuvintelor-cheie**: înțelege contextul, nu doar potrivirile exacte. Afișează puterea potrivirii (puternică/moderată/parțială), locul potrivirii („găsit în Competențe și 3 roluri profesionale”), importanța fiecărui cuvânt-cheie (critică/ridicată/medie/scăzută) și un rezumat narativ IA de 2–3 propoziții
- **Optimizarea CV-ului cu IA**: rescriere completă cu instrucțiuni bazate pe bunele practici ATS
- **Exporturi îmbunătățite cu IA**: PDF/DOCX formatate de IA înainte de descărcare
- **Generarea scrisorilor de intenție**: aplică reguli de exprimare naturală care elimină indiciile textului generat de IA (vezi mai jos)
- **Predicția întrebărilor de interviu**: pe baza descrierii postului
- **Estimarea intervalului salarial**

______

## Detectarea tipului de CV

Aplicația clasifică CV-ul într-unul dintre 7 profiluri și adaptează ordinea secțiunilor la așteptările recrutorilor și ale sistemelor ATS pentru etapa respectivă a carierei:

| Profil | Potrivit pentru | Prioritatea secțiunilor |
|---------|----------|-----------------|
| 🏢 **Profesionist cu experiență** | 5+ ani, carieră liniară | Experiență → Competențe → Studii |
| 🌱 **Nivel mediu** | 2–5 ani | Experiență → Competențe → Studii |
| 🎓 **Începător** | 0–2 ani | Competențe → Studii → Proiecte → Experiență |
| 🎒 **Student / absolvent recent** | Încă studiază | Studii → Proiecte → Competențe → Experiență |
| 🔬 **Cadru universitar / cercetător** | Doctorat, publicații | Studii → Cercetare → Publicații → Experiență |
| 📜 **Axat pe certificări** | Certificările cântăresc mai mult decât diploma | Certificări → Competențe → Experiență → Studii |
| 🔄 **Schimbare de carieră** | Pauză sau schimbare detectată | Rezumat → Competențe transferabile → Studii → Experiență |

*Ordinea secțiunilor rămâne consecventă în optimizare și în exporturile PDF, DOCX, TXT și Markdown, nu doar pe ecran.*

______

## Analiza semantică a cuvintelor-cheie cu IA

Aici se diferențiază instrumentul de contoarele de cuvinte-cheie de bază. Când este configurat un furnizor de IA, analiza lacunelor trece de la potrivirea exactă a textului la raționamentul semantic:

| Dimensiune | Fără IA | Cu IA |
|-----------|-----------|---------|
| **Metoda de potrivire** | Doar potrivire exactă a textului | Înțelegerea semantică a contextului |
| **Puterea potrivirii** | — | Evaluări puternică / moderată / parțială |
| **Contextul potrivirii** | — | „găsit în Competențe și 3 roluri profesionale” |
| **Importanța lacunei** | Toate lacunele au aceeași pondere | Critică / ridicată / medie / scăzută |
| **Sugestii** | Sfaturi generice | Recomandări practice pentru fiecare cuvânt-cheie |
| **Acoperire %** | Bazată pe numărul de cuvinte | Ponderată semantic |
| **Rezumat** | — | Rezumat narativ IA de 2–3 propoziții |

*Analiza locală bazată pe reguli rămâne instantanee. Rezultatele IA se adaugă asincron în timp ce le examinezi.*

______

## Furnizori IA acceptați

Toate apelurile IA includ instrucțiuni privind bunele practici ATS, derivate din ghidurile Harvard OCS și Columbia CCE.

### OpenAI

| Model | Potrivit pentru |
|-------|----------|
| **GPT-4.1 mini** (implicit) | Inteligent, rapid și accesibil. Recomandat. |
| GPT-4o mini | Varianta clasică, rapidă și accesibilă |
| GPT-4.1 | Cel mai nou GPT-4.1, cu respectarea precisă a instrucțiunilor |
| GPT-4o | Model emblematic de înaltă calitate |
| GPT-4 Turbo | Fereastră de context mare |
| GPT-3.5 Turbo | Cel mai rapid și mai ieftin |

**Cost estimat**: aproximativ 0,002–0,05 USD pentru analiza unui CV.

### Anthropic Claude

| Model | Potrivit pentru |
|-------|----------|
| **Claude Sonnet 4.5** (implicit) | Rapid și inteligent. Recomandat. |
| Claude Opus 4.5 | Cel mai capabil, potrivit pentru sarcini complexe |
| Claude Haiku 4.5 | Cel mai rapid și mai ieftin |
| Claude 3.5 Sonnet | Fiabil și testat temeinic |
| Claude 3.5 Haiku | Rapid și accesibil în versiunea 3.5 |

### Ollama (local / găzduit propriu)

Nu este necesară o cheie API. Rulează modelul pe propriul hardware. Setează `OLLAMA_ORIGINS=*` pentru a permite accesul browserului.

| Model | Note |
|-------|-------|
| **Llama 3.3** (implicit) | Cel mai nou model Meta. Recomandat. |
| Llama 3.2 | Model Meta |
| Mistral 7B | Rapid și capabil |
| Mixtral 8x7B | Amestec de experți |
| Qwen 2.5 | Model Alibaba Qwen 2.5 |
| DeepSeek R1 | Raționament puternic |
| Phi-4 | Model Microsoft |
| Gemma 3 | Model Google |

Rularea locală a Ollama pune întregul instrument în modul offline. Nicio informație nu părăsește computerul în niciun moment.

______

## Scrisori de intenție cu exprimare naturală

Generatorul de scrisori de intenție aplică un ghid de stil pentru a elimina semnele tipice ale textului generat de IA. Inspirată de [structura de exprimare naturală a Sabrinei Ramonov](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing), fiecare scrisoare respectă aceste reguli:

- **Fără liniuțe em**: cel mai evident indiciu al textului IA este eliminat complet
- **Peste 50 de cuvinte și expresii interzise**: leverage, utilize, dive deep, delve, embark, game-changer, groundbreaking, cutting-edge, pivotal, tapestry, harness, moreover, in conclusion, it's worth noting, ever-evolving, landscape, testament, not only...but also și altele
- **Fără Markdown în corpul scrisorii**: fără asteriscuri pentru text aldin, hashtaguri sau punct și virgulă
- **Implicit, voce activă**: folosește vocea pasivă doar când agentul acțiunii nu contează
- **Contracții obligatorii**: „I've”, „I'm”, „it's”, niciodată „I have”, „I am”, „it is”
- **Lungimi variate ale propozițiilor**: combină propoziții scurte și directe cu unele mai lungi
- **Fără introduceri de umplutură**: „Este important să reții că X” devine o afirmație directă despre X
- **Detaliu concret din anunț în primul paragraf**: arată că scrisoarea nu provine dintr-un șablon

*Rezultatul sună ca și cum l-ar fi scris o persoană, deoarece regulile obligă modelul să scrie în acest stil.*

______

## Calitatea exporturilor

| Format | Ce primești |
|--------|-------------|
| **PDF** | Tipografie profesională, separatoare de secțiuni, marcatori și antet cu date de contact |
| **DOCX** | Document Word structurat corect (`Packer.toBlob`, compatibil cu browserul) |
| **TXT** | Text simplu cu spațiere consecventă, sigur pentru ATS |
| **Markdown** | Fișier `.md` structurat cu titluri și liste |

Când configurezi un furnizor IA, acesta formatează exporturile înainte de descărcare. Fișierul primește insigna ✨ Îmbunătățit cu IA.

______

## Opțiuni de găzduire proprie

### Versiunea găzduită (fără configurare)

Folosește aplicația activă la **[atsresumeimprover.netlify.app](https://atsresumeimprover.netlify.app/)**. Nu ai nevoie de cont, înregistrare sau card de credit.

### Implementare cloud cu un singur clic

| Platformă | Link |
|----------|------|
| **Vercel** | Implementare din depozit cu un singur clic |
| **Cloudflare Pages** | Implementare cu un singur clic |
| **Netlify** | Implementare cu un singur clic |
| **GitHub Pages** | Fork → Settings → Pages → GitHub Actions → implementare automată |

### Dezvoltare locală

```bash
git clone https://github.com/simeononsecurity/ats-resume-improver
cd ats-resume-improver

make install
make dev           # http://localhost:5173
```

### Docker (recomandat pentru medii reproductibile)

```bash
# Development — hot-reload on http://localhost:5173
make docker-dev

# Production — nginx on http://localhost:8080
make docker-prod

# Dev + Ollama together (full local AI stack)
make docker-dev-with-ollama
```

### Stiva Ollama complet offline

```bash
# Start Ollama container (persists models across restarts)
make ollama

# Pull a model
make ollama-pull MODEL=llama3.2

# Start dev app + Ollama side-by-side
make docker-dev-with-ollama
```

Deschide aplicația, accesează panoul cheii API, selectează **Ollama (Local)**, setează URL-ul la `http://localhost:11434` și alege un model. Nicio informație nu părăsește computerul.

______

## Stiva tehnologică

| Nivel | Tehnologie |
|-------|-----------|
| **Framework** | React 19 + TypeScript |
| **Build** | Vite 8 |
| **Stilizare** | Tailwind CSS v4 |
| **Pictograme** | Lucide React |
| **Analiză PDF** | pdfjs-dist |
| **Analiză DOCX** | mammoth |
| **Export PDF** | jsPDF |
| **Export DOCX** | docx (`Packer.toBlob`) |
| **IA** | OpenAI · Anthropic Claude · Ollama |
| **Container** | Docker + nginx (multi-stage) + serviciul Ollama |

Întregul flux de evaluare și analiză (`atsAnalyzer.ts`, `keywordMatcher.ts`, `resumeTypeDetector.ts`) rulează în browser. Integrările IA din `aiProvider.ts` apelează API-urile furnizorilor direct din client, fără server proxy.

______

## Ghid practic de utilizare

### Pasul 1: încarcă CV-ul

Încarcă un fișier PDF, DOCX, TXT sau Markdown. Deschide fila **„What the ATS Sees”** pentru a verifica dacă parserul a extras corect conținutul. Dacă în această vizualizare lipsesc secțiuni sau textul apare deteriorat, software-ul ATS al recrutorilor va avea aceeași problemă.

### Pasul 2: inserează descrierea postului

Inserează anunțul complet în panoul Job Description. Anunțurile mai complete oferă o analiză mai bună a cuvintelor-cheie. Nu elimina secțiunea de cerințe.

### Pasul 3: examinează scorul ATS

Panoul scorului afișează un scor general de la 0 la 100 și o analiză pe 5 dimensiuni. Aceasta arată unde să te concentrezi. Problemele de formatare scad o dimensiune, cuvintele-cheie lipsă scad alta, iar formulările slabe despre experiența profesională scad o a treia.

### Pasul 4: verifică lacunele de cuvinte-cheie

Vizualizarea Keyword Analysis arată ce cuvinte-cheie din descriere apar în CV și care lipsesc. Cu IA activată, primești potrivire semantică și evaluări de importanță. O lacună „Critical” într-o competență tehnică centrală merită mai multă atenție decât una „Low” într-un clișeu despre abilități interpersonale.

### Pasul 5: optimizează

- **Mod determinist**: aplică restructurarea bazată pe reguli. Este sigur, rapid și nu implică taxe API.
- **Mod IA**: rescriere completă cu un LLM și instrucțiuni bazate pe bunele practici ATS.

Examinează **diferența înainte/după** pentru a înțelege fiecare schimbare înainte de a o accepta.

### Pasul 6: exportă

Exportă în PDF, DOCX, TXT sau Markdown. Cu IA activată, exportul este formatat pentru o prezentare profesională. Șablonul PDF folosește tipografie și aspect potrivite pentru recrutori.

______

## Integrarea sfaturilor pentru CV

Instrumentul include materialul de referință complementar `RESUME_TIPS.md` (disponibil și în depozitul GitHub), care acoperă:

- Cum evaluează sistemele ATS CV-urile
- Regulile de formatare importante și ce strică procesarea
- Redactarea rezumatelor, marcatorilor și secțiunilor de competențe
- Strategia cuvintelor-cheie fără repetare excesivă
- Tonul și structura scrisorii de intenție
- Lista de verificare înainte de trimitere

*Citește materialul înainte de a folosi instrumentul pentru a înțelege ce înseamnă scorurile.*

______

## Întrebări frecvente

### Instrumentul îmi stochează CV-ul?

Nu. Aplicația rulează integral în client. Nimic nu este păstrat pe un server. Datele sesiunii rămân în memoria browserului și dispar când închizi fila.

### CV-ul meu a primit un scor mic. Ar trebui să mă îngrijorez?

Scorurile ATS indică o direcție, nu o decizie de tip admis/respins. Un scor de 60 în instrument nu înseamnă că un ATS îți va respinge CV-ul. Înseamnă că există diferențe măsurabile între CV-ul tău și descrierea postului analizat. Folosește scorul pentru a stabili prioritatea modificărilor, nu ca verdict.

### Îl pot folosi cu mai multe descrieri de post?

Da. Inserează oricând o nouă descriere. Analiza cuvintelor-cheie și optimizarea se vor relua pentru noul anunț. Fiecare analiză este independentă.

### Integrarea Ollama funcționează într-adevăr offline?

Da, dacă Ollama rulează pe computerul tău sau pe unul din rețeaua locală. Aplicația trimite textul instanței Ollama prin HTTP. Nimic nu ajunge la un serviciu extern.

### Cât de precisă este detectarea tipului de CV?

Detectorul folosește euristici bazate pe regulile din conținutul CV-ului. Caută anii de experiență menționați, indicii de educație, secțiuni de publicații sau cercetare și semnale privind pauzele în carieră. Funcționează bine pentru majoritatea CV-urilor, dar poate greși în cazul unor profiluri neobișnuite. Ordinea secțiunilor aplicată poate fi ajustată oricând.

______

## Planul proiectului

Funcții în dezvoltare sau planificate:

- Istoricul versiunilor CV-ului prin IndexedDB
- Optimizator de profil LinkedIn
- Suport pentru furnizorul Google Gemini
- Modele Ollama suplimentare

Proiectul folosește licența MIT și acceptă pull request-uri. Deschide un issue înainte de modificări majore.

______

## Concluzie

**ATS Resume Improver** răspunde unei nevoi reale: oferă o analiză serioasă a CV-ului fără să transmită datele tale altcuiva. Modul fără cheie oferă imediat feedback practic despre formatare și acoperirea cuvintelor-cheie. Adăugarea unei chei IA activează raționamentul semantic, redactarea scrisorilor de intenție și pregătirea pentru interviuri, pentru câțiva cenți per analiză sau gratuit prin Ollama.

Versiunea găzduită este la **[atsresumeimprover.netlify.app](https://atsresumeimprover.netlify.app/)**. Codul sursă complet este la **[github.com/simeononsecurity/ats-resume-improver](https://github.com/simeononsecurity/ats-resume-improver)**.

Dacă îl găzduiești pentru propria căutare de loc de muncă sau vrei să ajustezi ponderile scorurilor și instrucțiunile pentru un anumit domeniu, configurarea Docker și structura clară a proiectului facilitează ramificarea și adaptarea.

______

## Curs de optimizare a CV-urilor

Dacă vrei un ghid structurat, pas cu pas, despre aplicarea elementelor evaluate de acest instrument, citește cursul asociat:

**[Curs de optimizare a CV-urilor: depășește sistemele ATS și obține mai multe interviuri](/resume-optimization-course-start/)**. Include 9 module despre evaluarea ATS, formatare, marcatori, cuvinte-cheie, adaptare, scrisori de intenție și lista de verificare înainte de trimitere. Folosește instrumentul împreună cu acest curs pentru feedback imediat la fiecare etapă.

______

## Referințe

1. [ATS Resume Improver — instrument activ](https://atsresumeimprover.netlify.app/)
2. [ATS Resume Improver — depozitul GitHub](https://github.com/simeononsecurity/ats-resume-improver)
3. [Sfaturi pentru CV — RESUME_TIPS.md](https://github.com/simeononsecurity/ats-resume-improver/blob/main/RESUME_TIPS.md)
4. [Sabrina Ramonov — cel mai bun prompt IA pentru exprimare naturală](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing)
5. [Documentația API OpenAI](https://platform.openai.com/docs/)
6. [Documentația Anthropic Claude](https://docs.anthropic.com/)
7. [Ollama — server LLM local](https://ollama.com/)
