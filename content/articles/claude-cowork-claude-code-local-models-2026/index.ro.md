---
title: "Claude Cowork și Claude Code cu modele locale: ghid de configurare 2026"
date: 2026-09-22
lastmod: 2026-11-14
toc: true
draft: false
description: "Configurează Ollama cu Claude Desktop și Claude Code printr-un API compatibil cu Anthropic. Vezi modelele și funcțiile disponibile doar în cloud în 2026."
genre: ["AI local", "Instrumente AI de programare", "AI găzduit local", "Instrumente pentru dezvoltatori", "Confidențialitate", "Modele open-source", "Automatizare", "Hardware AI"]
tags: ["claude cowork", "claude code", "modele locale claude desktop", "ollama claude code", "anthropic base url", "anthropic_auth_token", "model local claude code", "rulează claude offline", "agent local AI de programare", "ollama launch claude", "claude desktop ollama", "programare llm locală", "programare AI privată", "programare AI offline", "agent AI local", "qwen3.8", "model glm cloud", "modele cu apeluri de instrumente", "configurare claude code", "claude code gratuit", "claude fără cheie API", "fereastră de context pentru model local", "llama.cpp", "ollama cloud", "confidențialitate în programarea AI", "AI izolată de rețea", "instrumente AI pentru devops"]
cover: "/img/cover/claude-cowork-setup-guide-local-models-2026.webp"
coverAlt: "Spațiu de lucru modern cu un computer care afișează o interfață de programare, o tabletă și boxe inteligente pe un fundal albastru închis cu accente luminoase colorate."
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**Instrumentele agentice Claude funcționează acum cu modele de pe propriul hardware, fără cheie API, abonament sau date care părăsesc dispozitivul.** Ollama oferă un API compatibil cu Anthropic, la care Claude Code și Claude Desktop se conectează prin câteva comenzi.

*Multe ghiduri omit un detaliu important. Prezintă Claude Cowork, apoi oferă pași care configurează instrumentul din linia de comandă. Sunt două integrări diferite și doar una oferă Cowork.*

Acest ghid explică separat cele două căi, variabila de mediu omisă de tutorialele populare, modelele potrivite pentru fiecare în septembrie 2026 și funcțiile care rămân exclusiv în cloud indiferent de configurare.

**După ghid:** vei identifica integrarea de care ai nevoie, o vei conecta prin metoda documentată de Ollama și vei verifica endpointul cu un test de apelare a unui instrument. Inferența locală păstrează cererile către model pe dispozitiv doar dacă alegi un model local și eviți funcțiile bazate pe cloud.

## Răspunsul pe scurt

**Ollama se conectează la Claude în două moduri distincte. Alegerea celui greșit este motivul cel mai des întâlnit pentru un terminal funcțional fără Cowork după urmarea unui ghid.**

| Integrare | Ce primești | Metoda de configurare | Platformă |
|---|---|---|---|
| **Claude Desktop** | Cowork, subagenți, căutare web, mod automat | Aplicația Ollama, apoi **Apps** și **Connect Claude** | **Doar macOS** |
| **Claude Code** | Agent de programare CLI cu apeluri de instrumente și editare de fișiere | `ollama launch claude` sau variabile de mediu | macOS, Linux, Windows |

**Dacă vrei Cowork, folosește integrarea Claude Desktop.** Configurarea se face grafic în aplicația Ollama și funcționează doar pe macOS. Suportul pentru Windows este încă listat ca viitor.

**Dacă vrei un agent în terminal, folosește Claude Code.** Este suficientă o comandă.

*Ambele sunt gratuite. Costurile țin doar de hardware și electricitate.*

## Două integrări diferite

Confuzia începe cu denumirile. **Claude Cowork este o funcție din Claude Desktop**, nu o aplicație separată și nici un sinonim pentru Claude Code.

Documentația Ollama le prezintă pe pagini și sub titluri diferite. Claude Desktop apare la **Assistants**, alături de OpenClaw și Hermes. Claude Code apare la **Coding**, alături de OpenCode, Cline și Codex CLI.

Distincția contează deoarece configurarea diferă complet:

- **Claude Desktop** se configurează din interfața aplicației Ollama. Nu modifici profilul shell-ului.
- **Claude Code** se configurează prin variabile de mediu sau o singură comandă de lansare.

Un ghid care îți cere să exporți `ANTHROPIC_BASE_URL` și apoi să rulezi `claude` configurează instrumentul din linia de comandă. Dacă te așteptai la experiența Cowork de desktop, **configurarea nu este defectă. Ai configurat alt produs.**

## Configurarea Claude Desktop și Cowork

Această cale trece prin aplicația Ollama, nu prin terminal.

### Cerințe

- **Ollama instalat** pe macOS. Suportul Windows este listat ca viitor.
- **Un model descărcat în prealabil** dacă vrei rulare locală. Pentru un model cloud, conectează-te la Ollama și activează modelele cloud. Unele cer un plan cu plată.
- **Claude instalat.** Dacă lipsește, Ollama oferă descărcarea lui în timpul configurării.

### Pașii

1. Deschide Ollama și selectează **Apps**.
2. Selectează **Connect Claude**.
3. Urmează instrucțiunile. Instalează Claude dacă ți se cere și repornește-l când apare solicitarea.

Acesta este întregul proces. Pentru a schimba modelul ulterior, deschide **Ollama Settings**, mergi la **Apps**, alege modelele și selectează **Restart Claude**.

### Funcții disponibile

Documentația Ollama enumeră patru funcții acceptate prin această integrare:

- **Cowork**, pentru sarcini dificile
- **Subagenți**, pentru împărțirea sarcinilor mari între agenți
- **Web search**, oferită implicit prin Ollama
- **Auto mode**, prin care agentul decide când să ceară permisiunea înainte de modificări

*Cowork apare în listă. Funcția este disponibilă prin această integrare, nu și prin cea din linia de comandă.*

### Deconectarea

Deconectarea restaurează configurația anterioară a lui Claude, deci schimbarea nu este distructivă.

- În interfață, deschide **Apps**, deconectează Claude și repornește-l când ți se cere.
- Dintr-un terminal, rulează `ollama launch claude-desktop --restore`.
- **Închiderea Ollama cât timp Claude este conectat restaurează și configurația obișnuită a lui Claude.** Lasă Ollama să ruleze dacă vrei să păstrezi configurarea locală.

{{< figure src="claude-desktop-ollama-integration-flow.webp" alt="Diagramă care arată aplicația Ollama conectându-se la Claude Desktop din panoul Apps, selectarea modelelor în setările Ollama și calea de restaurare a configurației inițiale" >}}

## Configurarea Claude Code din CLI

Aceasta este calea prezentată de aproape toate ghidurile și este cea potrivită pentru lucrul în terminal.

### Metoda cu o singură comandă

```bash
ollama launch claude
```

Comanda setează variabilele de mediu necesare, direcționează Claude Code spre instanța locală Ollama și pornește programul. Alege un model din listă și apasă Enter. Pentru a specifica modelul de la început, adaugă opțiunea:

```bash
ollama launch claude --model qwen3.5
```

*Wrapper-ul pregătește mediul. Citește și secțiunea următoare, deoarece cunoașterea setărilor ajută la depanare.*

### Setarea manuală a variabilelor de mediu

```bash
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434

claude --model qwen3.5
```

**A doua linie lipsește din multe ghiduri populare.** Setarea `ANTHROPIC_API_KEY` la un șir gol împiedică o cheie reală deja prezentă în mediu să afecteze conexiunea locală. Dacă un ghid publicat omite linia, cititorii cu o cheie exportată primesc o eroare greu de înțeles.

Pentru a evita modificarea profilului shell-ului, transmite totul direct în comandă:

```bash
ANTHROPIC_AUTH_TOKEN=ollama ANTHROPIC_BASE_URL=http://localhost:11434 ANTHROPIC_API_KEY="" claude --model kimi-k2.7-code:cloud
```

Două detalii din documentația oficială:

- **`ANTHROPIC_AUTH_TOKEN` conține autentificarea bearer**, de aceea valoarea sa literală în modul local este `ollama`.
- **Fișierele de setări proprii ale lui Claude au prioritate față de variabilele shell-ului.** Dacă o conexiune se comportă ciudat după exportarea unor valori noi, verifică setările și rulează `/status` în Claude Code pentru a vedea endpointul folosit.

### Conectarea directă la Ollama Cloud

Nu este nevoie să instalezi Ollama pentru această cale. Setează o cheie API și direcționează Claude Code spre endpointul găzduit de Ollama:

```bash
ANTHROPIC_BASE_URL=https://ollama.com \
ANTHROPIC_AUTH_TOKEN="$OLLAMA_API_KEY" \
ANTHROPIC_API_KEY="" \
claude --model glm-5.3-flash
```

**Această cale are o limitare.** Documentația Ollama precizează că web search găzduit și controlul avansat al instrumentelor nu sunt acceptate complet. Chatul de bază, editarea fișierelor și apelurile de instrumente funcționează cu modele compatibile.

## Alegerea modelelor pentru septembrie 2026

Oferta de modele s-a schimbat mult în 2026, așa că recomandările din primăvară merită reverificate.

| Model | Tip | Context | De ce să-l alegi |
|---|---|---|---|
| **Qwen3.8 27B** | Local, 18 GB | 256K | Cel mai bun model local generalist actual, cu viziune, apeluri de instrumente și control al gândirii |
| **Qwen3 Coder Next** | Local, MoE 80B în total / 3B activi | 256K | Creat pentru agenți de programare care rulează continuu, cu un mod rapid fără gândire |
| **Qwen3.6 35B A3B** | Local, MoE 35B / 3B activi | 262K | Apache 2.0 și eficient cu memorie modestă |
| **kimi-k2.7-code:cloud** | Cloud | Mare | Model cloud pentru programare, fără cerințe de hardware local |
| **glm-5.3-flash** | Cloud | Mare | Primul model recomandat de documentația Ollama |

**Începe cu Qwen3.8 27B dacă ai suficientă memorie.** Rulează local cu context 256K, viziune nativă, apeluri de instrumente și gândire comutabilă pentru fiecare solicitare. O placă de cel puțin 24 GB este potrivită pentru utilizarea zilnică.

**Începe cu un model cloud dacă nu ai acea memorie.** Testarea lui Claude Code cu un model găzduit nu costă nimic și elimină cerința de hardware, dar codul părăsește dispozitivul.

### Atenție la modelele ternare

În **[ghidul nostru despre AI local](/articles/local-ai-2026-build-your-rig-now/)**, arătăm că Bonsai 2 27B ternar rulează un model complet de 27B în **5,53 GiB**. Pare tentant și în acest caz.

**Nu funcționează în acest flux de lucru.** Kernelurile ternare sunt în fork-ul llama.cpp de la Prism ML, iar Ollama standard nu poate încărca acele fișiere. O comandă precum `ollama launch claude --model Ternary-Bonsai-2-27B` eșuează înainte de pornirea inferenței. Folosește pachetul standard Qwen3.8 27B pentru Claude Code și păstrează pachetele ternare pentru un runtime compatibil.

*Comoditatea și eficiența maximă cer alegeri diferite. Instrumentele integrate așteaptă un GGUF standard.*

## Setează contextul la 64K înainte să învinuiești modelul

Documentația Ollama oferă o instrucțiune directă pentru lucrul în depozite de cod: alege un model și **setează fereastra de context la cel puțin 64K**, apoi mărește-o pentru depozite mai mari.

Claude Code introduce conținutul fișierelor, diferențele și rezultatele comenzilor în fereastra de context. Cu o valoare implicită mică, spațiul se termină în mijlocul sarcinii. Eșecul pare o problemă de raționare, dar cauza este setarea.

| Context | Ce gestionează |
|---|---|
| Sub 32K | Modificări într-un singur fișier și întrebări rapide |
| **64K** | Lucru cu mai multe fișiere într-un depozit modest |
| 128K | Depozite mai mari și ieșiri lungi ale comenzilor |
| 256K | Fereastra completă a modelului Qwen3.8 27B |

*Dacă Claude Code pierde firul la jumătatea unei sarcini, verifică setarea contextului înainte să schimbi modelul.*

## Verificarea apelurilor de instrumente printr-o comandă

Apelurile de instrumente diferențiază un agent de un generator de text. Verifică dacă funcționează.

După pornirea Claude Code, cere-i:

```text
Citește directorul curent și enumeră toate fișierele
```

**Dacă afișează fișiere reale, apelurile de instrumente funcționează.** Dacă spune că ar citi directorul și descrie ce se așteaptă să găsească, funcția nu este conectată. Vorbești cu un model de chat cu un prompt de programare, nu cu un agent. Mai multe prompturi nu vor remedia problema.

Verifică posibilele cauze în această ordine:

1. **Treci la un model cu suport confirmat pentru instrumente.** Nu toate modelele îl oferă, iar numărul de parametri nu indică diferența.
2. **Confirmă că mediul indică spre Ollama.** Rulează `ollama --version` și verifică dacă `ANTHROPIC_BASE_URL` indică endpointul local.
3. **Rulează `/status` în Claude Code.** Un URL de bază sau date de autentificare din setările Claude au prioritate față de variabilele shell-ului exportate recent.

## Ce funcții rămân doar în cloud

Cunoaște limita înainte să construiești un flux de lucru în jurul inferenței locale.

| Funcție | Cu modele locale | Cloud |
|---|---|---|
| Chat și editare de fișiere | Da | Da |
| Apeluri de instrumente | Depinde de model | Da |
| Subagenți | Da | Da |
| Căutare web | Oferită prin Ollama | Da |
| **Cowork** | Prin integrarea Claude Desktop | Da |
| Mod automat | Prin integrarea Claude Desktop | Da |
| Prompturi programate | Prin `/loop` în Claude Code | Da |

Utilizarea locală are trei limite:

- **Raționarea cu mai multe fișiere scade înaintea vitezei.** Un model local se descurcă bine cu un fișier, acceptabil cu trei și slab cu un depozit întreg. Planifică sarcinile în consecință.
- **Unele modele cloud necesită un plan Ollama cu plată.** Trebuie și să fii conectat și să le activezi.
- **Calea directă spre cloud limitează unele funcții.** Căutarea web găzduită și controlul avansat al instrumentelor nu sunt acceptate complet dacă omiți instalarea locală.

*Inferența locală este potrivită pentru lucrări limitate și verificabile, dar mai puțin pentru sarcini ample și ambigue. Planifică ținând cont de această limită.*

## Automatizare

Două funcții permit mai mult decât utilizarea interactivă.

### Rulări headless pentru scripturi și CI

Opțiunea `--yes` omite selectorii interactivi și descarcă modelul dacă este necesar. Are nevoie de `--model`, iar tot ce urmează după `--` ajunge direct la Claude Code:

```bash
ollama launch claude --model gemma4:cloud --yes -- -p "how does this repository work?"
```

**Ține cont de modelul de permisiuni.** Claude Code cere confirmare înaintea majorității acțiunilor, așa că o rulare headless are nevoie de reguli de permisiuni configurate sau de un mediu izolat. Nu îndrepta un agent nesupravegheat spre un depozit important pentru tine.

### Prompturi programate cu `/loop`

Într-o sesiune Claude Code, `/loop` execută periodic un prompt sau o comandă slash:

```text
/loop 30m Verifică PR-urile mele deschise și rezumă starea lor
/loop 1h Caută cele mai recente știri despre IA și rezumă evoluțiile importante
/loop 15m Verifică problemele GitHub noi și ordonează-le după prioritate
```

*Funcționează cât timp sesiunea este deschisă. Nu este un daemon în fundal și se oprește odată cu sesiunea.*

## Depanare

| Simptom | Cauză probabilă | Soluție |
|---|---|---|
| **Conexiune refuzată** | Ollama nu rulează | Rulează `ollama serve` și verifică cu `curl http://localhost:11434/api/tags` |
| **Descrie acțiunile în loc să le execute** | Modelul ales nu acceptă apeluri de instrumente | Treci la un model cu suport confirmat |
| **Este folosită o cheie API reală în locul endpointului local** | `ANTHROPIC_API_KEY` este încă exportată | Seteaz-o ca șir gol, după cum este prezentat mai sus |
| **Cowork lipsește după configurare** | A fost configurată CLI Claude Code în loc de Claude Desktop | Folosește ruta **Apps** din Ollama pentru Cowork |
| **Generarea este lentă** | Contextul este prea mare sau ai ales un model dens când ajunge unul rar | Redu contextul, apoi încearcă un model mixture-of-experts |
| **Variabilele exportate nu au efect** | Fișierele de setări Claude au prioritate față de variabilele shell-ului | Verifică fișierele și rulează `/status` |
| **Cereri în fundal eșuate** | Claude Code folosește un model mic pentru sarcini interne | Direcționează suprascrierea modelului mic spre același model local |

*Două dintre aceste șapte probleme au aceeași cauză. Majoritatea problemelor de configurare țin de un endpoint greșit sau de un model fără apeluri de instrumente.*

## Idei principale

- **Claude Desktop și Claude Code sunt integrări separate.** Cowork este în Claude Desktop și se configurează pe macOS din panoul **Apps** al Ollama. Calea CLI nu oferă Cowork.
- **O singură comandă pornește calea CLI:** `ollama launch claude`. Configurarea manuală are nevoie de trei variabile și **multe ghiduri omit `ANTHROPIC_API_KEY=""`**.
- **Nu ai nevoie de instalare locală.** Direcționează Claude Code spre `https://ollama.com` cu o cheie API.
- **Setează un context de minimum 64K înainte să evaluezi modelul.** O fereastră mică poate imita o problemă de raționare.
- **Verifică apelurile de instrumente cu o solicitare.** Dacă modelul descrie ce ar face, ai un generator de text, nu un agent.
- **Pachetele Bonsai ternare nu funcționează aici.** Au nevoie de fork-ul llama.cpp de la Prism ML, pe care Ollama standard nu îl poate încărca.
- **Deconectarea este sigură.** Închiderea Ollama restaurează setările anterioare ale lui Claude, iar din terminal poți rula `ollama launch claude-desktop --restore`.

## Pașii următori

1. **Instalează Ollama și descarcă un model cu suport confirmat pentru instrumente** înainte să configurezi Claude: **[Biblioteca de modele Ollama](https://ollama.com/library)**
2. **Citește pagina Ollama pentru Claude Code** pentru opțiunile și modelele actuale: **[Integrarea Claude Code](https://docs.ollama.com/integrations/claude-code)**
3. **Folosește pagina Claude Desktop** dacă vrei Cowork: **[Integrarea Claude Desktop](https://docs.ollama.com/integrations/claude-desktop)**
4. **Stabilește hardware-ul înainte de achiziție**, folosind categoriile de memorie din ghidul nostru de inferență locală: **[AI local în 2026: un model 27B depășește Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)**
5. **Vezi ce poate gestiona hardware-ul mai mic** dacă vrei un agent permanent pe un dispozitiv cu consum redus: **[Ce modele AI rulează pe Raspberry Pi 4 sau 5?](/articles/ai-models-raspberry-pi-4-5/)**

## Articole conexe

| Articol | Ce acoperă |
|---|---|
| **[AI local în 2026: un model 27B depășește Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | Benchmark de inferență locală, cuantizare ternară și alegerea hardware-ului |
| **[Ce modele AI rulează pe Raspberry Pi 4 sau 5?](/articles/ai-models-raspberry-pi-4-5/)** | Inferență locală pentru un asistent mic, permanent activ |
| **[Construirea unui asistent AI care protejează confidențialitatea pentru Meshtastic](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | Un model local pentru o stație radio off-grid, cu confidențialitatea în prim-plan |
| **[Cele mai bune extensii VS Code pentru dezvoltarea AI](/articles/best-visual-studio-code-extensions-for-ai/)** | Instrumente pentru editor de folosit cu un agent local de programare |

## Referințe

1. [Integrarea Claude Code - documentația Ollama](https://docs.ollama.com/integrations/claude-code)
2. [Integrarea Claude Desktop - documentația Ollama](https://docs.ollama.com/integrations/claude-desktop)
3. [Biblioteca de modele Ollama](https://ollama.com/library)
4. [Qwen3.8 - biblioteca de modele Ollama](https://ollama.com/library/qwen3.8)
5. [Claude Cowork cu modele locale - PromptSpace](https://www.promptspace.in/blog/how-to-use-claude-cowork-with-local-models-2026-guide)
6. [Fork-ul llama.cpp de la Prism ML - kerneluri ternare](https://github.com/PrismML-Eng/llama.cpp)
