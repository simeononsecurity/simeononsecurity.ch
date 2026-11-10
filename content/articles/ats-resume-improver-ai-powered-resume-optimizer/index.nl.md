---
title: "ATS Resume Improver: gratis AI-gestuurde cv-optimalisatie"
date: 2026-07-22
lastmod: 2026-11-08
toc: true
draft: false
description: "ATS Resume Improver is een gratis, open-source cv-optimalisatietool. Zonder AI-sleutel wordt de tekst in je browser verwerkt. Met OpenAI of Anthropic gaan cv- en vacatureteksten rechtstreeks naar de aanbieder. Ollama kan lokaal draaien."
genre: ["Loopbaantools", "Open-sourceprojecten", "Kunstmatige intelligentie", "Privacytechnologie", "Ontwikkelaarstools", "Banen zoeken", "Productiviteit"]
tags: ["ATS Resume Improver", "ATS-optimalisatie", "cv-scanner", "AI-cv", "OpenAI-cv", "Claude-cv", "Ollama lokale AI", "zelf hosten", "privacy eerst", "hulpmiddelen voor zoeken naar werk", "analyse van zoekwoordhiaten", "sollicitatiebrief", "cv-score", "React", "TypeScript", "Docker", "Vite", "open source", "PDF-export", "DOCX-export", "cv-parser", "loopbaantools", "sollicitatiegesprek voorbereiden", "salarisschatting", "cv-type detecteren", "ATS-score", "gratis cv-tool", "GitHub", "geen gegevensverzameling"]
cover: "/img/cover/ai-resume-optimizer-self-hosted-ats-analysis.webp"
coverAlt: "Een moderne laptop op een bureau toont een kleurrijke interface voor cv-optimalisatie met grafieken, tegen een diepblauwe achtergrond."
coverCaption: "ATS Resume Improver analyseert en optimaliseert cv's volledig in de browser, zonder gegevens te verzamelen."
canonical: "https://simeononsecurity.com/articles/ats-resume-improver-ai-powered-resume-optimizer/"
---

**Gratis, open source en zelf te hosten. Je cv komt nooit op een server terecht, tenzij je een AI-provider gebruikt. Ook dan gaat de tekst rechtstreeks naar die provider en niet naar ons.**

## Wat is ATS Resume Improver?

**[ATS Resume Improver](https://atsresumeimprover.netlify.app/)** is een open-source cv-optimalisatieprogramma in je browser. Het analyseert je cv aan de hand van een vacature en helpt je de kloof te dichten tussen je huidige cv en wat applicant tracking systems (ATS) beoordelen. Het is gebouwd met React 19, Vite en TypeScript. De volledige **verwerkings- en scoreketen draait in je browser**, zonder backendserver.

De broncode staat op **[github.com/simeononsecurity/ats-resume-improver](https://github.com/simeononsecurity/ats-resume-improver)**. Je kunt de gehoste versie gebruiken, de app met één klik op Vercel/Netlify/Cloudflare/GitHub Pages publiceren of lokaal met Docker starten.

### Het privacyprobleem dat het oplost

De meeste cv-optimalisatiediensten uploaden je cv naar hun servers, voeren een bedrijfseigen score uit en bewaren je gegevens. ATS Resume Improver kiest een andere aanpak.

| Modus | Wat je apparaat verlaat |
|------|------------------------|
| **Geen AI-sleutel** | Niets. Alles blijft lokaal en draait in je browser. |
| **OpenAI / Anthropic** | Cv-tekst en vacature gaan met jouw sleutel rechtstreeks naar de API van de AI-provider. Er is geen tussenliggende server. |
| **Ollama (lokaal)** | Niets. Het model draait op je eigen computer. |

**API-sleutels staan alleen in het geheugen** en verdwijnen zodra je het tabblad sluit. Geen analytics, tracking of cookies.

______

## Belangrijkste functies

### Wat werkt zonder AI-sleutel

Je hebt geen API-sleutel nodig om de tool te gebruiken. De modus zonder sleutel bevat:

- **Cv uploaden**: PDF, DOCX, TXT of Markdown
- **ATS-tekst ophalen**: toont precies wat een ATS uit je bestand leest, inclusief opmaak die verloren gaat
- **Cv-type detecteren**: bepaalt automatisch welk van 7 profielen bij je cv past en past de volgorde van secties daarop aan
- **Secties herkennen en opmaak waarschuwen**: signaleert ontbrekende secties en formaten die parsers lastig verwerken
- **ATS-score (0-100)** met een uitsplitsing in 5 dimensies
- **Analyse van zoekwoordhiaten**: vergelijkt tekenreeksen met de vacature
- **Deterministische ATS-optimalisatie**: past lokaal regels toe om de structuur te verbeteren
- **Voor-en-na-vergelijking**: bekijk precies wat er is veranderd
- **Professionele export naar PDF, DOCX, TXT en Markdown**

### Wat AI mogelijk maakt

Verbind OpenAI, Anthropic Claude of Ollama op je eigen computer. De tool krijgt dan extra functies:

- **Semantische zoekwoordanalyse**: begrijpt de context in plaats van alleen tekst te vergelijken. Toont de sterkte van een overeenkomst (sterk/matig/gedeeltelijk), de vindplaats ("gevonden bij Vaardigheden en 3 functies"), het belang per zoekwoord (kritiek/hoog/middel/laag) en een samenvatting van 2-3 zinnen
- **Cv optimaliseren met AI**: volledige herschrijving met prompts op basis van ATS-aanbevelingen
- **AI-verbeterde export**: AI maakt PDF/DOCX op voordat je het bestand downloadt
- **Sollicitatiebrief schrijven**: met regels die herkenbare AI-formuleringen verwijderen (zie hieronder)
- **Vragen voor sollicitatiegesprekken voorspellen**: op basis van de vacature
- **Salarisbereik schatten**

______

## Cv-type herkennen

De app deelt je cv automatisch in bij een van 7 profielen en past de volgorde van secties aan de verwachtingen van recruiters en ATS-systemen voor die loopbaanfase aan:

| Profiel | Geschikt voor | Prioriteit van secties |
|---------|----------|-------------------|
| 🏢 **Ervaren professional** | 5+ jaar, lineaire loopbaan | Ervaring → Vaardigheden → Opleiding |
| 🌱 **Medior** | 2-5 jaar | Ervaring → Vaardigheden → Opleiding |
| 🎓 **Starter** | 0-2 jaar | Vaardigheden → Opleiding → Projecten → Ervaring |
| 🎒 **Student / pas afgestudeerd** | Studeert nog | Opleiding → Projecten → Vaardigheden → Ervaring |
| 🔬 **Academicus / onderzoeker** | PhD, publicaties | Opleiding → Onderzoek → Publicaties → Ervaring |
| 📜 **Veel certificeringen** | Certificaten wegen zwaarder dan diploma | Certificeringen → Vaardigheden → Ervaring → Opleiding |
| 🔄 **Carrièreswitch** | Gat of koerswijziging herkend | Samenvatting → Overdraagbare vaardigheden → Opleiding → Ervaring |

*Dezelfde volgorde van secties geldt bij optimalisatie en exports naar PDF, DOCX, TXT en Markdown, dus niet alleen op het scherm.*

______

## Semantische analyse van zoekwoorden met AI

Hierin onderscheidt de tool zich van eenvoudige zoekwoordtellers. Als je een AI-provider instelt, vervangt semantisch redeneren de eenvoudige tekenreeksvergelijking in de analyse van zoekwoordhiaten:

| Dimensie | Zonder AI | Met AI |
|-----------|-----------|---------|
| **Vergelijkingsmethode** | Alleen exacte tekstovereenkomst | Begrijpt de semantische context |
| **Sterkte van overeenkomst** | — | Scores sterk / matig / gedeeltelijk |
| **Context van overeenkomst** | — | "gevonden bij Vaardigheden en 3 functies" |
| **Belang van hiaten** | Alle hiaten wegen even zwaar | Kritiek / hoog / middel / laag |
| **Suggesties** | Algemene tips | Actiegerichte suggesties per zoekwoord |
| **Dekking %** | Gebaseerd op aantal tekenreeksmatches | Semantisch gewogen |
| **Samenvatting** | — | AI-samenvatting van 2-3 zinnen |

*De lokale analyse op basis van regels werkt direct. AI-resultaten vullen die asynchroon aan terwijl je ze bekijkt.*

______

## Ondersteunde AI-providers

Alle AI-aanroepen bevatten prompts voor ATS-aanbevelingen op basis van richtlijnen van Harvard OCS en Columbia CCE.

### OpenAI

| Model | Geschikt voor |
|-------|----------|
| **GPT-4.1 mini** (standaard) | Slim en betaalbaar, snelle keuze aanbevolen |
| GPT-4o mini | Klassiek snel en betaalbaar model |
| GPT-4.1 | Nieuwste GPT-4.1, volgt instructies nauwkeurig |
| GPT-4o | Hoogwaardige vlaggenschipversie |
| GPT-4 Turbo | Groot contextvenster |
| GPT-3.5 Turbo | Snelst en goedkoopst |

**Geschatte kosten**: ongeveer $0,002-$0,05 per cv-analyse.

### Anthropic Claude

| Model | Geschikt voor |
|-------|----------|
| **Claude Sonnet 4.5** (standaard) | Snel en intelligent, aanbevolen |
| Claude Opus 4.5 | Meest capabel, goed voor complexe taken |
| Claude Haiku 4.5 | Snelst en goedkoopst |
| Claude 3.5 Sonnet | Betrouwbaar en uitgebreid getest |
| Claude 3.5 Haiku | Snel en betaalbaar v3.5-model |

### Ollama (lokaal / zelf gehost)

Je hebt geen API-sleutel nodig. Voer het model uit op je eigen hardware. Stel `OLLAMA_ORIGINS=*` in om browsertoegang toe te staan.

| Model | Opmerkingen |
|-------|-------|
| **Llama 3.3** (standaard) | Nieuwste Meta Llama, aanbevolen |
| Llama 3.2 | Meta Llama 3.2 |
| Mistral 7B | Snel en capabel |
| Mixtral 8x7B | Mixture of experts |
| Qwen 2.5 | Alibaba Qwen 2.5 |
| DeepSeek R1 | Sterk redeneermodel |
| Phi-4 | Microsoft Phi-4 |
| Gemma 3 | Google Gemma 3 |

Als je Ollama lokaal gebruikt, werkt de hele tool offline. Er verlaat op geen enkel moment informatie je apparaat.

______

## Sollicitatiebrieven menselijk laten klinken

De generator voor sollicitatiebrieven volgt een bewuste stijlgids om herkenbare kenmerken van AI-tekst te verwijderen. De regels zijn geïnspireerd op [het menselijker maken van AI-tekst door Sabrina Ramonov](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing). Elke gegenereerde brief voldoet aan deze regels:

- **Geen em-dashes**: het duidelijkste AI-signaal wordt helemaal verwijderd
- **Meer dan 50 verboden woorden en zinsdelen**: leverage, utilize, dive deep, delve, embark, game-changer, groundbreaking, cutting-edge, pivotal, tapestry, harness, moreover, in conclusion, it's worth noting, ever-evolving, landscape, testament, not only...but also, en meer
- **Geen Markdown in de brieftekst**: geen vetgedrukte asterisken, hashtags of puntkomma's
- **Actieve vorm als standaard**: alleen passief als de uitvoerder er echt niet toe doet
- **Samentrekkingen verplicht**: "I've", "I'm", "it's", nooit "I have", "I am", "it is"
- **Afwisselende zinslengte**: korte, krachtige zinnen met langere zinnen ertussen
- **Geen lege inleidingen**: "It's important to note that X" wordt gewoon "X"
- **Concreet detail uit de vacature in alinea 1**: zo blijkt dat de brief niet uit een sjabloon komt

*Het resultaat leest als mensenwerk, omdat de regels het model dwingen menselijk te schrijven.*

______

## Exportkwaliteit

| Formaat | Wat je krijgt |
|--------|-------------|
| **PDF** | Professionele typografie, scheidingslijnen voor secties, opsommingstekens, contactgegevens bovenaan |
| **DOCX** | Goed gestructureerd Word-document (Packer.toBlob, geschikt voor browsers) |
| **TXT** | Schone tekst met consistente spatiëring, geschikt voor ATS |
| **Markdown** | Gestructureerd `.md`-bestand met koppen en opsommingen |

Als je een AI-provider instelt, wordt de export vóór het downloaden door AI opgemaakt. De export krijgt een badge ✨ AI-verbeterd.

______

## Zelf hosten

### Gehoste versie (geen installatie)

Gebruik de live app op **[atsresumeimprover.netlify.app](https://atsresumeimprover.netlify.app/)**. Je hebt geen account, aanmelding of creditcard nodig.

### Clouddeployment met één klik

| Platform | Link |
|----------|------|
| **Vercel** | Met één klik vanuit de repository deployen |
| **Cloudflare Pages** | Deployment met één klik |
| **Netlify** | Deployment met één klik |
| **GitHub Pages** | Fork → Settings → Pages → GitHub Actions → automatisch deployen |

### Lokale ontwikkeling

```bash
git clone https://github.com/simeononsecurity/ats-resume-improver
cd ats-resume-improver

make install
make dev           # http://localhost:5173
```

### Docker (aanbevolen voor reproduceerbare omgevingen)

```bash
# Development — hot-reload on http://localhost:5173
make docker-dev

# Production — nginx on http://localhost:8080
make docker-prod

# Dev + Ollama together (full local AI stack)
make docker-dev-with-ollama
```

### Volledig offline met Ollama

```bash
# Start Ollama container (persists models across restarts)
make ollama

# Pull a model
make ollama-pull MODEL=llama3.2

# Start dev app + Ollama side-by-side
make docker-dev-with-ollama
```

Open daarna de app, ga naar het paneel voor API-sleutels, kies **Ollama (Local)**, stel de URL in op `http://localhost:11434` en kies een model. Er verlaat geen data je apparaat.

______

## Technische stack

| Laag | Technologie |
|-------|-----------|
| **Framework** | React 19 + TypeScript |
| **Build** | Vite 8 |
| **Styling** | Tailwind CSS v4 |
| **Pictogrammen** | Lucide React |
| **PDF-parser** | pdfjs-dist |
| **DOCX-parser** | mammoth |
| **PDF-export** | jsPDF |
| **DOCX-export** | docx (Packer.toBlob) |
| **AI** | OpenAI · Anthropic Claude · Ollama |
| **Container** | Docker + nginx (multi-stage) + Ollama-service |

De volledige score- en verwerkingsketen (`atsAnalyzer.ts`, `keywordMatcher.ts`, `resumeTypeDetector.ts`) draait in de browser. Alle AI-integraties in `aiProvider.ts` roepen de API's van providers rechtstreeks vanuit de client aan. Er is geen proxyserver.

______

## Praktische handleiding

### Stap 1: Upload je cv

Upload een PDF-, DOCX-, TXT- of Markdown-bestand. Open het tabblad **"What the ATS Sees"** om te controleren of de parser je inhoud correct heeft opgehaald. Als secties ontbreken of door elkaar staan, heeft ATS-software van recruiters hetzelfde probleem.

### Stap 2: Plak de vacaturetekst

Plak de volledige vacature in het paneel Job Description. Volledige vacatures leveren betere zoekwoordanalyse op. Kort de sectie met vereisten dus niet in.

### Stap 3: Bekijk je ATS-score

Het scorepaneel toont een totaalscore van 0-100 en een uitsplitsing in 5 dimensies. Die uitsplitsing helpt je bepalen waar je aan moet werken: opmaakproblemen verlagen één dimensie, ontbrekende zoekwoorden een andere en zwakke beschrijvingen van werkervaring een derde.

### Stap 4: Controleer de zoekwoordhiaten

In Keyword Analysis zie je welke zoekwoorden uit de vacature in je cv staan en welke ontbreken. Met AI krijg je semantische overeenkomsten en beoordelingen van het belang. Een "Critical"-hiaat in een belangrijke technische vaardigheid verdient meer aandacht dan een "Low"-hiaat in een algemene soft-skillterm.

### Stap 5: Optimaliseer

- **Deterministische modus**: past regels toe om de structuur aan te passen. Veilig, snel en zonder API-kosten.
- **AI-modus**: volledige LLM-herschrijving met prompts voor ATS-aanbevelingen.

Bekijk de **voor-en-na-vergelijking** om elke wijziging te begrijpen voordat je die accepteert.

### Stap 6: Exporteer

Exporteer naar PDF, DOCX, TXT of Markdown. Als AI is ingeschakeld, wordt de export opgemaakt voor een professionele presentatie. De PDF-sjabloon gebruikt passende typografie en een indeling die recruiters kennen.

______

## Integratie van cv-tips

De tool bevat de bijbehorende referentie `RESUME_TIPS.md` (ook in de GitHub-repository) met informatie over:

- Hoe ATS-systemen cv's beoordelen
- Welke opmaakregels belangrijk zijn en waardoor parsers vastlopen
- Samenvattingen, opsommingen en vaardighedensecties die werken
- Zoekwoorden gebruiken zonder ze te stapelen
- Toon en structuur van sollicitatiebrieven
- Checklist vóór verzending

*Lees het document voordat je de tool gebruikt, zodat je weet wat de scores betekenen.*

______

## Veelgestelde vragen

### Slaat de tool mijn cv op?

Nee. De app draait volledig in de browser. Er wordt niets op een server bewaard. Sessiegegevens staan in het browsergeheugen en verdwijnen zodra je het tabblad sluit.

### Mijn cv scoort laag. Moet ik me zorgen maken?

ATS-scores geven richting, maar zijn geen geslaagd-of-gezakt-test. Een score van 60 betekent niet dat een ATS je afwijst. De score geeft meetbare verschillen aan tussen je cv en de specifieke vacature die je hebt geanalyseerd. Gebruik de score om wijzigingen te prioriteren, niet als oordeel.

### Kan ik de tool voor meerdere vacatures gebruiken?

Ja. Je kunt op elk moment een nieuwe vacaturetekst plakken. De zoekwoordanalyse en optimalisatie worden opnieuw op die vacature uitgevoerd. Elke analyse staat op zichzelf.

### Werkt de Ollama-integratie echt offline?

Ja, als Ollama op je computer of op een computer in je lokale netwerk draait. De app stuurt tekst via HTTP naar je Ollama-installatie. Er gaat niets naar een externe dienst.

### Hoe nauwkeurig is de cv-typedetectie?

De detector gebruikt heuristieken op basis van regels voor je cv: het aantal genoemde ervaringsjaren, opleidingssignalen, publicaties of onderzoekssecties en aanwijzingen voor loopbaangaten. Voor de meeste cv's werkt dit goed, maar bij ongebruikelijke loopbaanprofielen kan de uitkomst onjuist zijn. Je kunt de volgorde van de secties altijd aanpassen.

______

## Projectroadmap

Functies in ontwikkeling of gepland:

- Versiegeschiedenis van cv's via IndexedDB
- LinkedIn-profiel optimaliseren
- Ondersteuning voor Google Gemini
- Extra Ollama-modellen

Het project gebruikt de MIT-licentie en staat open voor pull requests. Maak voor grote wijzigingen eerst een issue aan.

______

## Conclusie

**ATS Resume Improver** vult een echte leemte: serieuze cv-analyse zonder je gegevens via een tussenpartij te laten lopen. De modus zonder sleutel geeft direct bruikbare feedback over opmaak en zoekwoorddekking. Met een AI-sleutel komen daar semantische analyse, sollicitatiebrieven en voorbereiding op sollicitatiegesprekken bij. Dat kost enkele centen per analyse of is helemaal gratis met Ollama.

De gehoste versie staat op **[atsresumeimprover.netlify.app](https://atsresumeimprover.netlify.app/)**. De volledige broncode staat op **[github.com/simeononsecurity/ats-resume-improver](https://github.com/simeononsecurity/ats-resume-improver)**.

Als je de tool zelf host voor je zoektocht naar werk of de scores en prompts voor een bepaalde sector wilt aanpassen, zijn de Docker-configuratie en heldere projectstructuur eenvoudig aan te passen.

______

## Cursus cv-optimalisatie

Wil je een gestructureerde handleiding om alles toe te passen wat deze tool beoordeelt? Volg dan de bijbehorende cursus:

**[Cursus cv-optimalisatie: omzeil ATS-systemen en krijg meer gesprekken](/resume-optimization-course-start/)**: 9 modules over ATS-scores, opmaak, opsommingen, zoekwoorden, afstemming, sollicitatiebrieven en de checklist vóór verzending. Gebruik de tool samen met de cursus voor directe feedback bij elke stap.

______

## Bronnen

1. [ATS Resume Improver — live tool](https://atsresumeimprover.netlify.app/)
2. [ATS Resume Improver — GitHub-repository](https://github.com/simeononsecurity/ats-resume-improver)
3. [Cv-tips — RESUME_TIPS.md](https://github.com/simeononsecurity/ats-resume-improver/blob/main/RESUME_TIPS.md)
4. [Sabrina Ramonov — beste AI-prompt om AI-tekst menselijker te maken](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing)
5. [OpenAI API-documentatie](https://platform.openai.com/docs/)
6. [Anthropic Claude API-documentatie](https://docs.anthropic.com/)
7. [Ollama — lokale LLM-server](https://ollama.com/)
