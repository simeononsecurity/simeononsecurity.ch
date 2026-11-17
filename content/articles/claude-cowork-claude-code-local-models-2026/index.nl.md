---
title: "Claude Cowork en Claude Code met lokale modellen: installatiegids 2026"
date: 2026-09-22
lastmod: 2026-11-09
toc: true
draft: false
description: "Configureer Ollama met Claude Desktop en Claude Code via een Anthropic-compatibele API. Bekijk modelkeuzes en cloudfuncties voor 2026."
genre: ["Lokale AI", "AI-programmeertools", "Zelfgehoste AI", "Ontwikkelaarstools", "Privacy", "Open-sourcemodellen", "Automatisering", "AI-hardware"]
tags: ["claude cowork", "claude code", "lokale modellen voor claude desktop", "ollama claude code", "anthropic base url", "anthropic_auth_token", "claude code lokaal model", "claude offline draaien", "lokale AI-codeeragent", "ollama launch claude", "claude desktop ollama", "lokaal llm-programmeren", "privé AI-programmeren", "offline AI-programmeren", "lokale AI-agent", "qwen3.8", "glm-cloudmodel", "tool calling-modellen", "claude code instellen", "gratis claude code", "claude zonder API-sleutel", "contextvenster lokaal model", "llama.cpp", "ollama cloud", "AI-programmeren en privacy", "air-gapped AI", "devops-AI-tools"]
cover: "/img/cover/claude-cowork-setup-guide-local-models-2026.webp"
coverAlt: "Een moderne werkplek met een computer waarop een codeerinterface staat, omringd door een tablet en slimme luidsprekers tegen een donkerblauwe achtergrond met kleurrijke lichteffecten."
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**De agentfuncties van Claude werken nu met modellen op je eigen hardware, zonder API-sleutel, abonnement of gegevens die je machine verlaten.** Ollama biedt een Anthropic-compatibele API, waarop Claude Code en Claude Desktop met enkele opdrachten aansluiten.

*Veel handleidingen missen één belangrijk detail. Ze beschrijven Claude Cowork en geven daarna stappen die de opdrachtregeltool instellen. Dat zijn twee verschillende integraties, en slechts één ervan biedt Cowork.*

Deze gids behandelt beide routes afzonderlijk, de omgevingsvariabele die populaire handleidingen overslaan, geschikte modellen voor elke route in september 2026 en functies die cloudgebonden blijven, ongeacht je configuratie.

**Na deze gids:** bepaal je welke integratie je nodig hebt, verbind je die via de gedocumenteerde Ollama-route en controleer je het endpoint met één test voor toolaanroepen. Lokale inferentie houdt modelverzoeken alleen lokaal als je een lokaal model kiest en cloudfuncties vermijdt.

## Kort antwoord

**Ollama verbindt Claude op twee verschillende manieren. De verkeerde kiezen is de meest voorkomende reden waarom iemand een werkende terminal heeft, maar geen Cowork.**

| Integratie | Wat je krijgt | Installatieroute | Platform |
|---|---|---|---|
| **Claude Desktop** | Cowork, subagenten, zoeken op internet, automatische modus | Ollama-app, daarna **Apps** en **Connect Claude** | **Alleen macOS** |
| **Claude Code** | De CLI-codeeragent met toolaanroepen en bestandsbewerkingen | `ollama launch claude` of omgevingsvariabelen | macOS, Linux, Windows |

**Wil je Cowork, gebruik dan de integratie met Claude Desktop.** Dit is een grafische workflow in de Ollama-app. Die is alleen beschikbaar voor macOS; Windows-ondersteuning staat nog als toekomstig vermeld.

**Wil je een agent in je terminal, gebruik dan Claude Code.** Eén opdracht volstaat.

*Beide zijn gratis. Je betaalt alleen voor hardware en elektriciteit.*

## Twee integraties, niet één

De verwarring begint bij de namen. **Claude Cowork is een functie van Claude Desktop**, geen aparte applicatie en geen andere naam voor Claude Code.

De documentatie van Ollama heeft aparte pagina's voor beide producten. Claude Desktop staat onder **Assistants**, naast OpenClaw en Hermes. Claude Code staat onder **Coding**, naast OpenCode, Cline en Codex CLI.

Het verschil is belangrijk omdat de configuratie volledig uiteenloopt:

- **Claude Desktop** stel je in via de Ollama-app. Je hoeft geen shellprofiel aan te passen.
- **Claude Code** stel je in met omgevingsvariabelen of één startopdracht.

Een gids die je `ANTHROPIC_BASE_URL` laat instellen en daarna `claude` laat uitvoeren, configureert de opdrachtregeltool. Verwachtte je na die stappen de desktopervaring van Cowork, **dan is er niets kapot. Je hebt een ander product ingesteld.**

## Claude Desktop en Cowork instellen

Deze route loopt via de Ollama-app, niet via de terminal.

### Vereisten

- **Ollama geïnstalleerd** op macOS. Windows-ondersteuning staat als toekomstig vermeld.
- **Eerst een model downloaden** als je lokaal wilt werken. Voor een cloudmodel meld je je aan bij Ollama en schakel je cloudmodellen in. Voor sommige cloudmodellen is een betaald abonnement nodig.
- **Claude geïnstalleerd.** Ontbreekt het programma, dan biedt Ollama aan het tijdens de installatie te downloaden.

### Stappen

1. Open Ollama en kies **Apps**.
2. Kies **Connect Claude**.
3. Volg de installatievragen. Installeer Claude als daarom wordt gevraagd en start het programma opnieuw wanneer daarom wordt gevraagd.

Dat is de hele procedure. Wil je later een ander model kiezen, open dan **Ollama Settings**, ga naar **Apps**, kies de modellen en selecteer **Restart Claude**.

### Wat beschikbaar is

De documentatie van Ollama vermeldt vier functies als ondersteund via deze integratie:

- **Cowork**, voor moeilijke taken
- **Subagents**, om grotere taken over agents te verdelen
- **Web search**, standaard geleverd via Ollama
- **Auto mode**, waarbij de agent zelf bepaalt wanneer toestemming voor wijzigingen nodig is

*Cowork staat in deze lijst. Via deze integratie werkt het dus wel, maar via de opdrachtregelroute niet.*

### Verbinding verbreken

Na het verbreken van de verbinding wordt de vorige Claude-configuratie hersteld. De wijziging is dus omkeerbaar.

- Open in de interface **Apps**, verbreek de verbinding met Claude en start Claude opnieuw wanneer daarom wordt gevraagd.
- Voer in een terminal `ollama launch claude-desktop --restore` uit.
- **Als je Ollama afsluit terwijl Claude verbonden is, worden de gebruikelijke instellingen van Claude eveneens hersteld.** Laat Ollama actief als je de lokale configuratie wilt behouden.

{{< figure src="claude-desktop-ollama-integration-flow.webp" alt="Diagram van de Ollama-app die via het Apps-paneel verbinding maakt met Claude Desktop, met modelkeuze in Ollama-instellingen en een herstelroute naar de oorspronkelijke configuratie" >}}

## Claude Code instellen via de CLI

Bijna elke gids behandelt deze route. Voor werk in de terminal is dit de juiste keuze.

### Methode met één opdracht

```bash
ollama launch claude
```

De opdracht stelt de vereiste omgevingsvariabelen in, verwijst Claude Code naar je lokale Ollama-instantie en start het programma. Kies een model en druk op Enter. Voeg de vlag toe om vooraf een model te kiezen:

```bash
ollama launch claude --model qwen3.5
```

*De wrapper verzorgt de omgeving. Lees de volgende sectie toch, want inzicht in die instellingen helpt bij het oplossen van problemen.*

### Omgevingsvariabelen handmatig instellen

```bash
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434

claude --model qwen3.5
```

**De tweede regel ontbreekt in veel populaire handleidingen.** Door `ANTHROPIC_API_KEY` op een lege tekenreeks te zetten, voorkom je dat een bestaande echte sleutel in je omgeving de lokale verbinding verstoort. Als een gepubliceerde handleiding deze regel weglaat, krijgen lezers met een al geëxporteerde sleutel een verwarrende fout.

Gebruik deze opdrachten inline om je shellprofiel ongemoeid te laten:

```bash
ANTHROPIC_AUTH_TOKEN=ollama ANTHROPIC_BASE_URL=http://localhost:11434 ANTHROPIC_API_KEY="" claude --model kimi-k2.7-code:cloud
```

Twee details uit de officiële documentatie:

- **`ANTHROPIC_AUTH_TOKEN` bevat de bearer-authenticatie.** Daarom staat in lokale modus de letterlijke tekst `ollama` in deze variabele.
- **De eigen instellingenbestanden van Claude gaan boven shellvariabelen.** Als een verbinding vreemd reageert nadat je nieuwe waarden hebt geëxporteerd, controleer je die instellingen en voer je daarna `/status` uit in Claude Code om het gebruikte endpoint te zien.

### Rechtstreeks verbinding maken met Ollama Cloud

Voor deze route hoef je Ollama niet te installeren. Stel een API-sleutel in en verwijs Claude Code naar het gehoste endpoint van Ollama:

```bash
ANTHROPIC_BASE_URL=https://ollama.com \
ANTHROPIC_AUTH_TOKEN="$OLLAMA_API_KEY" \
ANTHROPIC_API_KEY="" \
claude --model glm-5.3-flash
```

**Er geldt één beperking.** Volgens de documentatie van Ollama werken gehost zoeken op internet en geavanceerde bediening van tools via deze route niet volledig. Basischat, bestandsbewerkingen en toolaanroepen werken met compatibele modellen.

## Modellen kiezen voor september 2026

Het modellenaanbod is in 2026 sterk veranderd. Advies uit het voorjaar moet je daarom opnieuw controleren.

| Model | Type | Context | Waarom kiezen |
|---|---|---|---|
| **Qwen3.8 27B** | Lokaal, 18 GB | 256K | De beste lokale allrounder van dit moment, met vision, toolaanroepen en instelbare denkmodus |
| **Qwen3 Coder Next** | Lokaal, MoE 80B totaal / 3B actief | 256K | Gemaakt voor altijd actieve codeeragenten, met een snelle modus zonder denkstappen |
| **Qwen3.6 35B A3B** | Lokaal, MoE 35B / 3B actief | 262K | Apache 2.0 en efficiënt bij beperkt geheugen |
| **kimi-k2.7-code:cloud** | Cloud | Groot | Cloudmodel voor programmeerwerk zonder lokale hardware |
| **glm-5.3-flash** | Cloud | Groot | Het model dat de eigen documentatie van Ollama als eerste noemt |

**Begin met Qwen3.8 27B als je genoeg geheugen hebt.** Het draait lokaal met een contextvenster van 256K, native vision, toolaanroepen en denkstappen die je per verzoek in- of uitschakelt. Op een kaart met ten minste 24 GB is het geschikt voor dagelijks gebruik.

**Begin met een cloudmodel als je dat geheugen niet hebt.** Claude Code verbinden met een gehost model kost niets om te proberen en maakt de hardwarevraag overbodig. Je code verlaat dan wel je machine.

### Waarschuwing voor ternaire modellen

In onze **[gids voor lokale AI](/articles/local-ai-2026-build-your-rig-now/)** lees je dat het ternaire Bonsai 2 27B-model met **5,53 GiB** een volledig 27B-model draait. Dat lijkt hier een aantrekkelijke keuze.

**Deze workflow ondersteunt het niet.** De ternaire kernels zitten in de llama.cpp-fork van Prism ML, en standaard Ollama kan deze bestanden niet laden. Een opdracht als `ollama launch claude --model Ternary-Bonsai-2-27B` stopt voordat inferentie begint. Gebruik voor Claude Code het standaard Qwen3.8 27B-pakket en bewaar de ternaire pakketten voor een runtime die ze ondersteunt.

*Gemak en maximale efficiëntie lopen hier uiteen. De geïntegreerde tools verwachten een standaard-GGUF.*

## Stel een context van 64K in voordat je het model de schuld geeft

De documentatie van Ollama geeft één rechtstreeks advies voor werk in repositories: kies een model en **stel een contextvenster van minstens 64K in**. Verhoog dit verder voor grotere repositories.

Claude Code laadt bestandsinhoud, verschillen en opdrachtuitvoer in het contextvenster. Bij een kleine standaardwaarde raakt het model halverwege de taak vol. De fout lijkt dan op een redeneerprobleem in plaats van een configuratieprobleem.

| Context | Geschikt voor |
|---|---|
| Minder dan 32K | Bewerkingen in één bestand en korte vragen |
| **64K** | Werk met meerdere bestanden in een bescheiden repository |
| 128K | Grotere repositories en lange opdrachtuitvoer |
| 256K | Het volledige venster van Qwen3.8 27B |

*Raakt Claude Code halverwege een taak de draad kwijt, controleer dan de contextinstelling voordat je van model wisselt.*

## Toolaanroepen met één opdracht controleren

Toolaanroepen maken van een agent iets anders dan een tekstgenerator. Controleer dus of ze werken.

Vraag Claude Code nadat het is gestart:

```text
Read the current directory and list all files
```

**Toont het echte bestanden, dan werken toolaanroepen.** Antwoordt het dat het de map zou lezen en beschrijft het wat daar vermoedelijk staat, dan is de functie niet gekoppeld. Je praat dan met een chatmodel waarop een programmeerprompt is toegepast. Geen enkele extra prompt lost dit op.

Voer deze controles in deze volgorde uit:

1. **Kies een model met bevestigde ondersteuning voor toolaanroepen.** Niet elk model ondersteunt dit. Je kunt het verschil niet afleiden uit het aantal parameters.
2. **Controleer of de omgeving naar Ollama verwijst.** Voer `ollama --version` uit en controleer of `ANTHROPIC_BASE_URL` naar je lokale endpoint verwijst.
3. **Voer `/status` uit in Claude Code.** Een basis-URL of inloggegeven in de eigen instellingen van Claude gaat boven de shellvariabelen die je net hebt geëxporteerd.

## Wat alleen in de cloud beschikbaar blijft

Ken deze grens voordat je een workflow rond lokale inferentie bouwt.

| Functie | Met lokale modellen | Cloud |
|---|---|---|
| Chat en bestandsbewerkingen | Ja | Ja |
| Toolaanroepen | Afhankelijk van model | Ja |
| Subagenten | Ja | Ja |
| Zoeken op internet | Via Ollama | Ja |
| **Cowork** | Via de integratie met Claude Desktop | Ja |
| Automatische modus | Via de integratie met Claude Desktop | Ja |
| Geplande prompts | Via `/loop` in Claude Code | Ja |

Voor lokaal gebruik gelden drie kanttekeningen:

- **Redeneren over meerdere bestanden verslechtert eerder dan de snelheid.** Een lokaal model werkt goed met één bestand, redelijk met drie bestanden en slecht met een volledige repository. Stem de omvang van de taak daarop af.
- **Voor sommige cloudmodellen is een betaald Ollama-abonnement nodig.** Je moet ook aangemeld zijn en de cloudmodellen hebben ingeschakeld.
- **De rechtstreekse cloudroute heeft beperkingen.** Gehost zoeken op internet en geavanceerde bediening van tools worden niet volledig ondersteund als je de lokale installatie overslaat.

*Lokale inferentie is sterk in afgebakend werk dat je kunt controleren, en minder geschikt voor grote, onduidelijke taken. Stem je planning af op die grens.*

## Automatiseren

Twee functies maken deze aanpak geschikt voor meer dan interactieve sessies.

### Headless uitvoeren voor scripts en CI

De vlag `--yes` slaat interactieve selecties over en haalt het model op als dat nodig is. Je hebt `--model` nodig. Alles na `--` gaat rechtstreeks naar Claude Code:

```bash
ollama launch claude --model gemma4:cloud --yes -- -p "how does this repository work?"
```

**Let op het machtigingsmodel.** Claude Code vraagt voor de meeste acties om bevestiging. Een headless uitvoering vereist daarom ingestelde machtigingsregels of een geïsoleerde omgeving. Richt een onbeheerde agent niet op een repository die je wilt beschermen.

### Geplande prompts met `/loop`

Binnen een Claude Code-sessie voert `/loop` met een interval een prompt of slashopdracht uit:

```text
/loop 30m Check my open PRs and summarize their status
/loop 1h Research the latest AI news and summarize key developments
/loop 15m Check for new GitHub issues and triage by priority
```

*Dit werkt zolang de sessie open is. Het is geen achtergrondproces en stopt zodra de sessie eindigt.*

## Problemen oplossen

| Symptoom | Waarschijnlijke oorzaak | Oplossing |
|---|---|---|
| **Verbinding geweigerd** | Ollama draait niet | Voer `ollama serve` uit en controleer met `curl http://localhost:11434/api/tags` |
| **Het model beschrijft acties in plaats van ze uit te voeren** | Het gekozen model ondersteunt geen toolaanroepen | Schakel over naar een model met bevestigde ondersteuning voor toolaanroepen |
| **Er wordt een echte API-sleutel gebruikt in plaats van het lokale endpoint** | `ANTHROPIC_API_KEY` is nog geëxporteerd | Stel de variabele in op een lege tekenreeks, zoals hierboven |
| **Cowork ontbreekt na de installatie** | De CLI van Claude Code is ingesteld in plaats van Claude Desktop | Gebruik voor Cowork de Ollama-workflow via **Apps** |
| **Genereren duurt lang** | De context is te groot ingesteld of er is een dicht model gekozen terwijl een dun model volstaat | Verlaag de context en probeer daarna een mixture-of-experts-model |
| **Geëxporteerde variabelen hebben geen effect** | De instellingenbestanden van Claude gaan boven shellvariabelen | Controleer de instellingenbestanden en voer daarna `/status` uit |
| **Verzoeken op de achtergrond mislukken** | Claude Code kiest voor interne taken een klein model | Laat de kleine-modelinstelling naar hetzelfde lokale model verwijzen |

*Twee van deze zeven problemen hebben dezelfde oorzaak. De meeste configuratiefouten komen door een verkeerd endpoint of een model zonder toolaanroepen.*

## Belangrijkste punten

- **Claude Desktop en Claude Code zijn afzonderlijke integraties.** Cowork zit in Claude Desktop en wordt op macOS ingesteld via het paneel **Apps** van Ollama. De CLI-route biedt geen Cowork.
- **Met één opdracht start je de CLI-route:** `ollama launch claude`. Handmatig heb je drie variabelen nodig. **Veel handleidingen vergeten `ANTHROPIC_API_KEY=""`.**
- **Een lokale installatie is niet vereist.** Verwijs Claude Code met een API-sleutel naar `https://ollama.com`.
- **Stel eerst een context van minstens 64K in.** Een klein venster lijkt op een redeneerfout.
- **Controleer toolaanroepen met één verzoek.** Beschrijft het model alleen wat het zou doen, dan gebruik je een tekstgenerator in plaats van een agent.
- **Ternaire Bonsai-pakketten werken hier niet.** Ze vereisen de llama.cpp-fork van Prism ML. Standaard Ollama kan ze niet laden.
- **Verbinding verbreken is veilig.** Als je Ollama afsluit, worden de vorige Claude-instellingen hersteld. In de terminal werkt ook `ollama launch claude-desktop --restore`.

## Volgende stappen

1. **Installeer Ollama en haal een model met bevestigde toolondersteuning op** voordat je Claude configureert: **[Ollama-modellenbibliotheek](https://ollama.com/library)**
2. **Lees de Claude Code-pagina van Ollama** voor actuele vlaggen en modellen: **[Claude Code-integratie](https://docs.ollama.com/integrations/claude-code)**
3. **Gebruik de pagina voor Claude Desktop** als je Cowork wilt: **[Claude Desktop-integratie](https://docs.ollama.com/integrations/claude-desktop)**
4. **Bepaal eerst welke hardware je nodig hebt** aan de hand van de geheugencategorieën in onze gids voor lokale inferentie: **[Lokale AI in 2026: een 27B-model verslaat Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)**
5. **Bekijk wat kleinere hardware aankan** als je een altijd actieve agent op een energiezuinig apparaat wilt: **[Welke AI-modellen draaien op een Raspberry Pi 4 of 5?](/articles/ai-models-raspberry-pi-4-5/)**

## Gerelateerde artikelen

| Artikel | Inhoud |
|---|---|
| **[Lokale AI in 2026: een 27B-model verslaat Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | Benchmark voor lokale inferentie, ternaire kwantisering en hardwarekeuze |
| **[Welke AI-modellen draaien op een Raspberry Pi 4 of 5?](/articles/ai-models-raspberry-pi-4-5/)** | Lokale inferentie voor een kleine assistent die altijd actief is |
| **[Een privacyvriendelijke AI-assistent voor Meshtastic bouwen](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | Een lokaal model voor een radio zonder internetverbinding, met privacy als uitgangspunt |
| **[Beste VS Code-extensies voor AI-ontwikkeling](/articles/best-visual-studio-code-extensions-for-ai/)** | Editortools voor gebruik met een lokale codeeragent |

## Bronnen

1. [Claude Code-integratie - Ollama-documentatie](https://docs.ollama.com/integrations/claude-code)
2. [Claude Desktop-integratie - Ollama-documentatie](https://docs.ollama.com/integrations/claude-desktop)
3. [Ollama-modellenbibliotheek](https://ollama.com/library)
4. [Qwen3.8 - Ollama-modellenbibliotheek](https://ollama.com/library/qwen3.8)
5. [Claude Cowork met lokale modellen - PromptSpace](https://www.promptspace.in/blog/how-to-use-claude-cowork-with-local-models-2026-guide)
6. [Prism ML llama.cpp-fork - ternaire kernels](https://github.com/PrismML-Eng/llama.cpp)
