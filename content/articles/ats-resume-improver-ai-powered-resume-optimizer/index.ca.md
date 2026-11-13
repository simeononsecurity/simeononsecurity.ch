---
title: "ATS Resume Improver: optimitzador de currículums amb IA gratuït"
date: 2026-07-22
lastmod: 2026-11-13
toc: true
draft: false
description: "ATS Resume Improver és una eina gratuïta, de codi obert i executada al client per analitzar, puntuar, comparar, optimitzar i exportar currículums amb models al núvol o locals."
genre: ["Eines professionals", "Projectes de codi obert", "Intel·ligència artificial", "Tecnologia de privadesa", "Eines per a desenvolupadors", "Cerca de feina", "Productivitat"]
tags: ["ATS Resume Improver", "Optimització per a ATS", "Escàner de currículums", "Currículum amb IA", "Currículum OpenAI", "Currículum Claude", "IA local Ollama", "Autoallotjament", "Privadesa prioritària", "Eines per cercar feina", "Anàlisi de mancances de paraules clau", "Carta de presentació", "Puntuació de currículums", "React", "TypeScript", "Docker", "Vite", "Codi obert", "Exportació PDF", "Exportació DOCX", "Analitzador de currículums", "Eines professionals", "Preparació d'entrevistes", "Estimador salarial", "Detecció del tipus de currículum", "Puntuació ATS", "Eina gratuïta per a currículums", "GitHub", "Sense recollida de dades"]
cover: "/img/cover/ai-resume-optimizer-self-hosted-ats-analysis.webp"
coverAlt: "Un portàtil modern sobre una taula mostra una interfície acolorida d'optimització de currículums amb gràfics, sobre un fons blau marí fosc."
coverCaption: "ATS Resume Improver analitza i optimitza els currículums íntegrament al client, sense recollir dades."
canonical: "https://simeononsecurity.com/articles/ats-resume-improver-ai-powered-resume-optimizer/"
---

**Gratuït, de codi obert i preparat per a l'autoallotjament. El teu currículum no arriba a cap servidor si no fas servir un proveïdor d'IA. Fins i tot en aquest cas, el text va directament al proveïdor, no a nosaltres.**

## Què és ATS Resume Improver?

**[ATS Resume Improver](https://atsresumeimprover.netlify.app/)** és un optimitzador de currículums que funciona al navegador. Analitza el teu currículum en relació amb la descripció d'una oferta de feina i t'ajuda a reduir la diferència entre la teva experiència i els criteris dels sistemes de seguiment de candidats (ATS). Està fet amb React 19, Vite i TypeScript. **Tot el procés d'anàlisi i puntuació funciona al navegador**, sense servidor de backend.

El codi font és a **[repositori d’ATS Resume Improver a GitHub](https://github.com/simeononsecurity/ats-resume-improver)**. Fes servir la versió allotjada, desplega la teva còpia amb un sol clic a Vercel, Netlify, Cloudflare o GitHub Pages, o executa-la localment amb Docker.

### Quin problema de privadesa resol

La majoria de serveis d'optimització de currículums els pugen als seus servidors, els puntuen de manera opaca i conserven les dades. ATS Resume Improver fa servir un enfocament diferent.

| Mode | Dades que surten del teu dispositiu |
|------|------------------------|
| **Sense clau d'IA** | Cap. Tot funciona localment al navegador. |
| **OpenAI / Anthropic** | El text del currículum i la descripció de l'oferta van directament a l'API del proveïdor d'IA amb la teva clau. No hi ha cap servidor intermedi. |
| **Ollama (al teu ordinador)** | Cap. El model funciona al teu ordinador. |

**Les claus API només es conserven a la memòria** i desapareixen quan tanques la pestanya. No hi ha analítica, seguiment ni galetes.

______

## Funcions principals

### Què funciona sense clau d'IA

No necessites una clau API per obtenir resultats útils. El mode sense clau inclou:

- **Pujada del currículum**: PDF, DOCX, TXT o Markdown
- **Extracció de text per a ATS**: mostra exactament què llegeix un ATS del fitxer, inclosa la informació que es perd amb el format
- **Detecció del tipus de currículum**: identifica quin dels 7 perfils s'assembla al teu currículum i ajusta l'ordre de les seccions
- **Detecció de seccions i avisos de format**: assenyala seccions que falten i formats difícils per al parser
- **Puntuació ATS (0–100)** amb el detall de 5 dimensions
- **Anàlisi de mancances de paraules clau**: comparació de cadenes basada en regles amb la descripció de l'oferta
- **Optimització ATS determinista**: reestructuració local basada en regles
- **Visualitzador de diferències abans/després**: mostra exactament què ha canviat
- **Exportació professional a PDF, DOCX, TXT i Markdown**

### Què aporta la IA

Connecta OpenAI, Anthropic Claude o Ollama local per activar:

- **Anàlisi semàntica de paraules clau**: entén el context, no només les coincidències de cadenes. Mostra la força de la coincidència (forta/moderada/parcial), on es troba (“a Competències i 3 llocs de treball”), la importància de cada paraula clau (crítica/alta/mitjana/baixa) i un resum narratiu de la IA de 2 o 3 frases
- **Optimització del currículum amb IA**: reescriptura completa amb instruccions basades en les bones pràctiques d'ATS
- **Exportacions millorades amb IA**: PDF/DOCX que la IA ha formatat abans de baixar-los
- **Generació de cartes de presentació**: aplica normes d'escriptura natural que eliminen els indicis de text generat per IA (consulta-ho més avall)
- **Predicció de preguntes d'entrevista**: basada en la descripció de l'oferta
- **Estimació de l'interval salarial**

______

## Detecció del tipus de currículum

L'aplicació classifica el currículum en un dels 7 perfils i n'ajusta l'ordre de les seccions a les expectatives dels reclutadors i dels ATS per a aquella etapa professional:

| Perfil | Adequat per a | Prioritat de les seccions |
|---------|----------|-----------------|
| 🏢 **Professional amb experiència** | 5 anys o més, trajectòria lineal | Experiència → Competències → Formació |
| 🌱 **Nivell intermedi** | 2–5 anys | Experiència → Competències → Formació |
| 🎓 **Nivell inicial** | 0–2 anys | Competències → Formació → Projectes → Experiència |
| 🎒 **Estudiant / recent graduat** | Encara estudia | Formació → Projectes → Competències → Experiència |
| 🔬 **Acadèmic / investigador** | Doctorat, publicacions | Formació → Recerca → Publicacions → Experiència |
| 📜 **Centrat en certificacions** | Certificacions per davant del títol | Certificacions → Competències → Experiència → Formació |
| 🔄 **Canvi de carrera** | Detecta una pausa o un canvi | Resum → Competències transferibles → Formació → Experiència |

*L'ordre de les seccions es manté coherent en l'optimització i en les exportacions PDF, DOCX, TXT i Markdown, no només a la pantalla.*

______

## Anàlisi semàntica de paraules clau amb IA

Aquí és on l'eina es diferencia dels comptadors bàsics de paraules clau. Quan configures un proveïdor d'IA, l'anàlisi de mancances passa de la coincidència literal a raonar sobre el significat:

| Dimensió | Sense IA | Amb IA |
|-----------|-----------|---------|
| **Mètode de coincidència** | Només coincidència exacta de cadenes | Comprensió semàntica del context |
| **Força de la coincidència** | — | Valoracions forta / moderada / parcial |
| **Context de la coincidència** | — | “trobat a Competències i 3 llocs de treball” |
| **Importància de la mancança** | Totes tenen el mateix pes | Crítica / alta / mitjana / baixa |
| **Suggeriments** | Consells genèrics | Suggeriments pràctics per a cada paraula clau |
| **Cobertura %** | Basada en el recompte de cadenes | Ponderada semànticament |
| **Resum** | — | Resum narratiu de la IA de 2 o 3 frases |

*L'anàlisi local basada en regles continua sent immediata. Els resultats de la IA s'afegeixen de manera asíncrona mentre els revises.*

______

## Proveïdors d'IA compatibles

Totes les crides a la IA inclouen instruccions de bones pràctiques d'ATS derivades de les pautes de Harvard OCS i Columbia CCE.

### OpenAI

| Nom del model | Adequat per a |
|-------|----------|
| **GPT-4.1 mini** (per defecte) | Intel·ligent, ràpid i assequible. Recomanat. |
| GPT-4o mini | L'opció clàssica, ràpida i assequible |
| GPT-4.1 | L'últim GPT-4.1, segueix bé les instruccions |
| GPT-4o | Model insígnia d'alta qualitat |
| GPT-4 Turbo | Finestra de context àmplia |
| GPT-3.5 Turbo | El més ràpid i econòmic |

**Cost estimat**: uns 0,002–0,05 USD per anàlisi de currículum.

### Anthropic Claude

| Nom del model | Adequat per a |
|-------|----------|
| **Claude Sonnet 4.5** (per defecte) | Ràpid i intel·ligent. Recomanat. |
| Claude Opus 4.5 | El més capaç, per a tasques complexes |
| Claude Haiku 4.5 | El més ràpid i econòmic |
| Claude 3.5 Sonnet | Fiable i ben provat |
| Claude 3.5 Haiku | Ràpid i assequible de la versió 3.5 |

### Ollama (local / autoallotjat)

No cal cap clau API. Executa el model al teu propi maquinari. Defineix `OLLAMA_ORIGINS=*` per permetre l'accés del navegador.

| Nom del model | Notes |
|-------|-------|
| **Llama 3.3** (per defecte) | L'últim model de Meta. Recomanat. |
| Llama 3.2 | Model de Meta |
| Mistral 7B | Ràpid i capaç |
| Mixtral 8x7B | Barreja d'experts |
| Qwen 2.5 | Model Qwen 2.5 d'Alibaba |
| DeepSeek R1 | Raonament potent |
| Phi-4 | Model de Microsoft |
| Gemma 3 | Model de Google |

Executar Ollama localment deixa tota l'eina fora de línia. No surt cap dada de la teva màquina en cap moment.

______

## Naturalització de les cartes de presentació

El generador de cartes de presentació aplica una guia d'estil per eliminar els senyals típics del text generat per IA. Inspirada en el [marc de naturalització de Sabrina Ramonov](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing), cada carta generada segueix aquestes normes:

- **Sense guions em**: s'elimina completament l'indici més evident d'escriptura amb IA
- **Més de 50 paraules i frases prohibides**: leverage, utilize, dive deep, delve, embark, game-changer, groundbreaking, cutting-edge, pivotal, tapestry, harness, moreover, in conclusion, it's worth noting, ever-evolving, landscape, testament, not only...but also i més
- **Sense Markdown al cos de la carta**: sense asteriscs per a negreta, etiquetes o punt i coma
- **Veu activa per defecte**: veu passiva només quan l'agent no importa
- **Contraccions obligatòries**: “I've”, “I'm”, “it's”, mai “I have”, “I am”, “it is”
- **Longitud variada de les frases**: combina frases breus i contundents amb altres de més llargues
- **Sense introduccions de farciment**: “És important assenyalar que X” passa a ser una afirmació directa sobre X
- **Detall concret de l'oferta al primer paràgraf**: demostra que la carta no és una plantilla

*El resultat sembla escrit per una persona perquè les normes obliguen el model a fer-ho així.*

______

## Qualitat de les exportacions

| Format | Què obtens |
|--------|-------------|
| **PDF** | Tipografia professional, separadors de secció, llistes amb vinyetes i capçalera de contacte |
| **DOCX** | Document Word ben estructurat (`Packer.toBlob`, compatible amb navegador) |
| **TXT** | Text pla i net amb espaiat coherent, segur per a ATS |
| **Markdown** | Fitxer `.md` estructurat amb títols i llistes |

Quan configures un proveïdor d'IA, aquest formata les exportacions abans de baixar-les. El fitxer mostra l'etiqueta ✨ Millorat amb IA.

______

## Opcions d'autoallotjament

### Versió allotjada (sense configuració)

Fes servir l'aplicació activa a **[versió en línia d’ATS Resume Improver](https://atsresumeimprover.netlify.app/)**. No cal cap compte, registre ni targeta de crèdit.

### Desplegament al núvol amb un clic

| Plataforma | Enllaç |
|----------|------|
| **Vercel** | Desplegament des del repositori amb un clic |
| **Cloudflare Pages** | Desplegament amb un clic |
| **Netlify** | Desplegament amb un clic |
| **GitHub Pages** | Fork → Settings → Pages → GitHub Actions → desplegament automàtic |

### Desenvolupament local

```bash
git clone https://github.com/simeononsecurity/ats-resume-improver
cd ats-resume-improver

make install
make dev           # http://localhost:5173
```

### Docker (recomanat per a entorns reproduïbles)

```bash
# Desenvolupament: recàrrega en calent a http://localhost:5173
make docker-dev

# Producció: nginx a http://localhost:8080
make docker-prod

# Desenvolupament i Ollama junts (pila d’IA local completa)
make docker-dev-with-ollama
```

### Pila Ollama completament fora de línia

```bash
# Inicia el contenidor d’Ollama (conserva els models entre reinicis)
make ollama

# Baixa un model
make ollama-pull MODEL=llama3.2

# Inicia l’aplicació de desenvolupament i Ollama alhora
make docker-dev-with-ollama
```

Obre l'aplicació, ves al tauler de la clau API, selecciona **Ollama (Local)**, defineix l'URL `http://localhost:11434` i tria un model. No surt cap dada de la teva màquina.

______

## Pila tecnològica

| Capa | Tecnologia |
|-------|-----------|
| **Framework** | React 19 + TypeScript |
| **Compilació** | Vite 8 |
| **Estils** | Tailwind CSS v4 |
| **Icones** | Lucide React |
| **Anàlisi de PDF** | pdfjs-dist |
| **Anàlisi de DOCX** | mammoth |
| **Exportació PDF** | jsPDF |
| **Exportació DOCX** | docx (`Packer.toBlob`) |
| **IA** | OpenAI · Anthropic Claude · Ollama |
| **Contenidor** | Docker + nginx (multietapa) + servei Ollama |

Tot el procés de puntuació i anàlisi (`atsAnalyzer.ts`, `keywordMatcher.ts`, `resumeTypeDetector.ts`) funciona al navegador. Les integracions d'IA d'`aiProvider.ts` criden directament les API dels proveïdors des del client, sense servidor intermediari.

______

## Guia d'ús pràctica

### Pas 1: puja el currículum

Puja un fitxer PDF, DOCX, TXT o Markdown. Obre la pestanya **“What the ATS Sees”** per comprovar que el parser ha extret bé el contingut. Si hi falten seccions o el text apareix desordenat, el programari ATS dels reclutadors tindrà el mateix problema.

### Pas 2: enganxa la descripció de l'oferta

Enganxa l'anunci complet al panell Job Description. Una descripció més completa proporciona una anàlisi de paraules clau millor. No retallis la secció de requisits.

### Pas 3: revisa la puntuació ATS

El panell mostra una puntuació total de 0 a 100 i un desglossament de 5 dimensions. Aquest desglossament indica on t'has de centrar: els problemes de format redueixen una dimensió, les paraules clau absents en redueixen una altra i les descripcions febles de l'experiència laboral en redueixen una tercera.

### Pas 4: audita les mancances de paraules clau

La vista Keyword Analysis mostra quines paraules clau de l'oferta apareixen al currículum i quines no. Amb la IA activada, obtens una coincidència semàntica i nivells d'importància. Una mancança “Critical” en una competència tècnica essencial mereix més atenció que una “Low” en una frase feta sobre habilitats personals.

### Pas 5: optimitza

- **Mode determinista**: aplica una reestructuració basada en regles. És segur, ràpid i no té cost d'API.
- **Mode IA**: reescriptura completa amb un LLM i instruccions basades en les bones pràctiques d'ATS.

Revisa la **diferència abans/després** per entendre cada canvi abans d'acceptar-lo.

### Pas 6: exporta

Exporta a PDF, DOCX, TXT o Markdown. Amb la IA activada, l'exportació es formata per presentar-la de manera professional. La plantilla PDF utilitza una tipografia i una distribució adequades per als reclutadors.

______

## Integració de consells per a currículums

L'eina inclou una guia complementària a `RESUME_TIPS.md` (també disponible al repositori GitHub), amb informació sobre:

- Com puntuen realment els sistemes ATS els currículums
- Normes de format importants i què trenca els parsers
- Com redactar resums, vinyetes i seccions de competències
- Estratègia de paraules clau sense repetir-les en excés
- To i estructura de les cartes de presentació
- Llista de comprovació abans d'enviar

*Llegeix-la abans d'utilitzar l'eina per entendre què signifiquen les puntuacions.*

______

## Preguntes freqüents

### L'eina desa el meu currículum?

No. L'aplicació funciona íntegrament al client. No es desa res en cap servidor. Les dades de la sessió es queden a la memòria del navegador i desapareixen quan tanques la pestanya.

### El meu currículum ha obtingut una puntuació baixa. M'hauria de preocupar?

Les puntuacions ATS orienten, però no aproven ni suspenen. Una puntuació de 60 a l'eina no vol dir que un ATS rebutgi el currículum. Vol dir que hi ha diferències mesurables entre el teu currículum i la descripció concreta que has analitzat. Fes servir la puntuació per prioritzar els canvis, no com a veredicte.

### Puc utilitzar-la amb diverses descripcions de feina?

Sí. Enganxa una altra descripció quan vulguis. L'anàlisi de paraules clau i l'optimització es tornaran a executar per a la nova oferta. Cada anàlisi és independent.

### La integració d'Ollama funciona realment fora de línia?

Sí, si Ollama funciona al teu ordinador o en una màquina de la xarxa local. L'aplicació envia el text a la instància d'Ollama per HTTP. No es comunica amb cap servei extern.

### Quina precisió té la detecció del tipus de currículum?

El detector aplica heurístiques basades en regles al contingut del currículum: busca els anys d'experiència, indicadors de formació, seccions de publicacions o recerca i senyals de pauses professionals. Funciona bé amb la majoria de currículums, però pot equivocar-se amb perfils poc habituals. L'ordre de les seccions sempre es pot ajustar.

______

## Full de ruta del projecte

Funcions en desenvolupament o previstes:

- Historial de versions del currículum mitjançant IndexedDB
- Optimitzador de perfils de LinkedIn
- Suport del proveïdor Google Gemini
- Més models Ollama

El projecte té llicència MIT i accepta pull requests. Obre un issue abans de fer canvis importants.

______

## Conclusió

**ATS Resume Improver** resol una necessitat real: ofereix una anàlisi completa del currículum sense cedir les teves dades a ningú. El mode sense clau proporciona comentaris immediats i pràctics sobre el format i la cobertura de paraules clau. Si hi afegeixes una clau d'IA, obtens raonament semàntic, redacció de cartes de presentació i preparació d'entrevistes per cèntims per anàlisi, o sense cost amb Ollama.

La versió allotjada és a **[versió en línia d’ATS Resume Improver](https://atsresumeimprover.netlify.app/)**. Tot el codi font és a **[repositori d’ATS Resume Improver a GitHub](https://github.com/simeononsecurity/ats-resume-improver)**.

Si l'allotges per a la teva pròpia cerca de feina o vols personalitzar els pesos de puntuació i les instruccions per a un sector concret, la configuració de Docker i l'estructura clara del projecte faciliten fer-ne un fork i adaptar-lo.

______

## Curs d'optimització de currículums

Si vols una guia estructurada, pas a pas, per aplicar tot el que puntua aquesta eina, consulta el curs complementari:

**[Curs d'optimització de currículums: supera els sistemes ATS i aconsegueix més entrevistes](/resume-optimization-course-start/)**. Inclou 9 mòduls sobre puntuació ATS, format, vinyetes, paraules clau, adaptació, cartes de presentació i la llista de comprovació abans d'enviar. Fes servir l'eina amb el curs per obtenir comentaris immediats a cada pas.

______

## Referències

1. [eina en línia](https://atsresumeimprover.netlify.app/)
2. [repositori del codi font](https://github.com/simeononsecurity/ats-resume-improver)
3. [Consells per a currículums — RESUME_TIPS.md](https://github.com/simeononsecurity/ats-resume-improver/blob/main/RESUME_TIPS.md)
4. [Sabrina Ramonov — millor prompt d'IA per naturalitzar l'escriptura](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing)
5. [documentació de l’API d’OpenAI](https://platform.openai.com/docs/)
6. [documentació de l’API d’Anthropic Claude](https://docs.anthropic.com/)
7. [Ollama — servidor local de LLM](https://ollama.com/)
