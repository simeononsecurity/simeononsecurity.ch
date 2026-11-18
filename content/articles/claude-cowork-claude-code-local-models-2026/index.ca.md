---
title: "Claude Cowork i Claude Code amb models locals: guia de configuració 2026"
date: 2026-09-22
lastmod: 2026-11-12
toc: true
draft: false
description: "Configura Ollama amb Claude Desktop i Claude Code mitjançant una API compatible amb Anthropic. Revisa els models i les funcions exclusives del núvol el 2026."
genre: ["IA local", "Eines de programació amb IA", "IA autoallotjada", "Eines per a desenvolupadors", "Privadesa", "Models de codi obert", "Automatització", "Maquinari per a IA"]
tags: ["claude cowork", "claude code", "models locals claude desktop", "ollama claude code", "anthropic base url", "anthropic_auth_token", "model local claude code", "executar claude fora de línia", "agent local de programació amb IA", "ollama launch claude", "claude desktop ollama", "programació local amb llm", "programació privada amb IA", "programació amb IA fora de línia", "agent local d'IA", "qwen3.8", "model glm al núvol", "models amb crides a eines", "configurar claude code", "claude code gratuït", "claude sense clau API", "finestra de context del model local", "llama.cpp", "ollama cloud", "privadesa en la programació amb IA", "IA aïllada de la xarxa", "eines d'IA per a devops"]
cover: "/img/cover/claude-cowork-setup-guide-local-models-2026.webp"
coverAlt: "Espai de treball modern amb un ordinador que mostra una interfície de programació, una tauleta i altaveus intel·ligents sobre un fons blau fosc amb accents de llum de colors."
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**Les eines d'agent de Claude ja funcionen amb models al teu maquinari, sense clau API, subscripció ni dades que surtin de l'ordinador.** Ollama ofereix una API compatible amb Anthropic a la qual Claude Code i Claude Desktop es connecten amb unes quantes ordres.

*Moltes guies passen per alt un detall important. Parlen de Claude Cowork i després donen passos per configurar l'eina de línia d'ordres. Són dues integracions diferents, i només una ofereix Cowork.*

Aquesta guia explica les dues opcions per separat, la variable d'entorn que ometen molts tutorials, els models adequats per a cadascuna el setembre del 2026 i les funcions que continuen sent exclusives del núvol, sigui quina sigui la configuració.

**En acabar la guia:** identificaràs la integració que necessites, la connectaràs pel procediment documentat d'Ollama i comprovaràs el punt final amb una prova de crida a una eina. La inferència local manté les peticions del model a l'ordinador només si tries un model local i evites les funcions basades en el núvol.

## Resposta breu

**Ollama es connecta amb Claude de dues maneres diferents. Triar la que no toca és el motiu més habitual per acabar una guia amb un terminal que funciona però sense Cowork.**

| Integració | Què ofereix | Procediment de configuració | Plataforma |
|---|---|---|---|
| **Claude Desktop** | Cowork, subagents, cerca web, mode automàtic | Aplicació Ollama, després **Apps** i **Connect Claude** | **Només macOS** |
| **Claude Code** | Agent de programació CLI amb crides a eines i edició de fitxers | `ollama launch claude` o variables d'entorn | macOS, Linux, Windows |

**Si vols Cowork, fes servir la integració de Claude Desktop.** Es configura amb la interfície gràfica de l'aplicació Ollama i només està disponible a macOS. La compatibilitat amb Windows encara figura com a futura.

**Si vols un agent al terminal, fes servir Claude Code.** N'hi ha prou amb una ordre.

*Tots dos són gratuïts. Només pagues el maquinari i l'electricitat.*

## Dues integracions, no una

La confusió comença pels noms. **Claude Cowork és una funció de Claude Desktop**, no una aplicació independent ni un sinònim de Claude Code.

La documentació d'Ollama les mostra en pàgines i apartats diferents. Claude Desktop surt a **Assistants**, al costat d'OpenClaw i Hermes. Claude Code surt a **Coding**, al costat d'OpenCode, Cline i Codex CLI.

La distinció importa perquè la configuració és completament diferent:

- **Claude Desktop** es configura a la interfície de l'aplicació Ollama. No cal modificar cap perfil de shell.
- **Claude Code** es configura amb variables d'entorn o amb una sola ordre d'inici.

Una guia que et fa exportar `ANTHROPIC_BASE_URL` i després executar `claude` configura l'eina de línia d'ordres. Si t'esperaves l'experiència d'escriptori de Cowork, **la configuració no s'ha espatllat. Has configurat un altre producte.**

## Configurar Claude Desktop i Cowork

Aquest procediment passa per l'aplicació Ollama, no pel terminal.

### Requisits previs

- **Ollama instal·lat** a macOS. La compatibilitat amb Windows figura com a futura.
- **Un model descarregat abans de començar** si vols executar-lo localment. Per a un model al núvol, inicia sessió a Ollama i activa els models cloud. Alguns necessiten un pla de pagament.
- **Claude instal·lat.** Si no hi és, Ollama ofereix descarregar-lo durant la configuració.

### Passos

1. Obre Ollama i selecciona **Apps**.
2. Selecciona **Connect Claude**.
3. Segueix les instruccions. Instal·la Claude si t'ho demanen i reinicia'l quan aparegui l'avís.

Això és tot. Per canviar de model més endavant, obre **Ollama Settings**, ves a **Apps**, tria els models i selecciona **Restart Claude**.

### Funcions disponibles

La documentació d'Ollama enumera quatre funcions compatibles amb aquesta integració:

- **Cowork**, per completar tasques difícils
- **Subagents**, per dividir tasques grans entre agents
- **Web search**, proporcionada per defecte per Ollama
- **Auto mode**, que deixa que l'agent decideixi quan demanar permís abans de fer canvis

*Cowork apareix a la llista. Aquesta integració el proporciona, però la de línia d'ordres no.*

### Desconnectar

Desconnectar restaura la configuració anterior de Claude, de manera que el canvi no és destructiu.

- A la interfície, obre **Apps**, desconnecta Claude i reinicia'l quan t'ho demani.
- Des del terminal, executa `ollama launch claude-desktop --restore`.
- **Tancar Ollama mentre Claude està connectat també restaura la configuració habitual de Claude.** Deixa Ollama en execució si vols conservar la configuració local.

{{< figure src="claude-desktop-ollama-integration-flow.webp" alt="Diagrama de l'aplicació Ollama connectant amb Claude Desktop des del panell Apps, la selecció de models a la configuració d'Ollama i el camí per restaurar la configuració original" >}}

## Configurar Claude Code des de la CLI

Gairebé totes les guies expliquen aquest procediment, que és l'adequat per treballar al terminal.

### Mètode d'una sola ordre

```bash
ollama launch claude
```

L'ordre defineix les variables d'entorn necessàries, apunta Claude Code a la instància local d'Ollama i l'inicia. Tria un model de la llista i prem Enter. Per indicar el model directament, afegeix l'opció:

```bash
ollama launch claude --model qwen3.5
```

*El wrapper prepara l'entorn. Llegeix la secció següent igualment, perquè saber què defineix t'ajudarà a resoldre problemes.*

### Definir manualment les variables d'entorn

```bash
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434

claude --model qwen3.5
```

**La segona línia és la que ometen moltes guies populars.** Assignar una cadena buida a `ANTHROPIC_API_KEY` evita que una clau real ja present a l'entorn interfereixi amb la connexió local. Si una guia publicada se salta aquesta línia, els lectors que ja tinguin una clau exportada rebran un error confús.

Per no modificar el perfil de shell, passa-ho tot directament a l'ordre:

```bash
ANTHROPIC_AUTH_TOKEN=ollama ANTHROPIC_BASE_URL=http://localhost:11434 ANTHROPIC_API_KEY="" claude --model kimi-k2.7-code:cloud
```

Dos detalls de la documentació oficial:

- **`ANTHROPIC_AUTH_TOKEN` porta l'autenticació bearer.** Per això conté el text literal `ollama` en el mode local.
- **Els fitxers de configuració de Claude tenen prioritat sobre les variables de shell.** Si la connexió es comporta de manera estranya després d'exportar valors nous, comprova la configuració i executa `/status` a Claude Code per veure quin punt final utilitza.

### Connectar directament amb Ollama Cloud

No cal instal·lar Ollama per a aquest procediment. Defineix una clau API i apunta Claude Code al punt final allotjat d'Ollama:

```bash
ANTHROPIC_BASE_URL=https://ollama.com \
ANTHROPIC_AUTH_TOKEN="$OLLAMA_API_KEY" \
ANTHROPIC_API_KEY="" \
claude --model glm-5.3-flash
```

**Aquest procediment té una limitació.** La documentació d'Ollama indica que la cerca web allotjada i el control avançat de les eines no tenen suport complet. El xat bàsic, l'edició de fitxers i les crides a eines funcionen amb models compatibles.

## Models per al setembre del 2026

L'oferta de models va canviar molt durant el 2026. Val la pena tornar a revisar els consells de primavera.

| Model | Tipus | Context | Per què triar-lo |
|---|---|---|---|
| **Qwen3.8 27B** | Local, 18 GB | 256K | Millor model local polivalent actual, amb visió, crides a eines i control del pensament |
| **Qwen3 Coder Next** | Local, MoE 80B totals / 3B actius | 256K | Creat per a agents de programació sempre actius, amb mode ràpid sense pensament |
| **Qwen3.6 35B A3B** | Local, MoE 35B / 3B actius | 262K | Apache 2.0 i eficient amb poca memòria |
| **kimi-k2.7-code:cloud** | Núvol | Gran | Model cloud de programació que no necessita maquinari local |
| **glm-5.3-flash** | Núvol | Gran | El primer model que recomana la documentació d'Ollama |

**Comença amb Qwen3.8 27B si tens prou memòria.** Funciona localment amb un context de 256K, visió nativa, crides a eines i pensament que pots activar per petició. Una targeta amb 24 GB o més ofereix un bon ús diari.

**Comença amb un model al núvol si no tens aquesta memòria.** Provar Claude Code amb un model allotjat no costa res i elimina la qüestió del maquinari, però el codi surt de l'ordinador.

### Avís sobre els models ternaris

Al nostre **[manual d'IA local](/articles/local-ai-2026-build-your-rig-now/)** expliquem que el Bonsai 2 27B ternari executa un model complet de 27B en **5,53 GiB**. També pot semblar una bona opció aquí.

**No funciona amb aquest flux de treball.** Els nuclis ternaris es troben al fork de llama.cpp de Prism ML, i l'Ollama estàndard no pot carregar aquests fitxers. Una ordre com `ollama launch claude --model Ternary-Bonsai-2-27B` falla abans de començar la inferència. Fes servir el paquet estàndard Qwen3.8 27B amb Claude Code i reserva els paquets ternaris per a un runtime compatible.

*La comoditat i l'eficiència màxima exigeixen opcions diferents. Les eines integrades esperen un GGUF estàndard.*

## Fixa el context a 64K abans de culpar el model

La documentació d'Ollama dona una indicació directa per treballar en repositoris: tria un model i **fixa la finestra de context a 64K o més**. Augmenta-la per als repositoris més grans.

Claude Code carrega el contingut dels fitxers, les diferències i la sortida de les ordres a la finestra de context. Amb un valor per defecte petit, l'espai s'acaba a mitja tasca. Sembla un problema de raonament, però el provoca la configuració.

| Context | Què pot gestionar |
|---|---|
| Menys de 32K | Edicions d'un sol fitxer i preguntes ràpides |
| **64K** | Treball amb diversos fitxers en un repositori modest |
| 128K | Repositoris més grans i sortides d'ordres llargues |
| 256K | La finestra completa de Qwen3.8 27B |

*Si Claude Code perd el fil a mitja tasca, comprova el context abans de canviar de model.*

## Verificar les crides a eines amb una ordre

Les crides a eines distingeixen un agent d'un generador de text. Val la pena verificar que funcionin.

Quan Claude Code estigui en marxa, demana-li:

```text
Llegeix el directori actual i enumera tots els fitxers
```

**Si mostra fitxers reals, les crides a eines funcionen.** Si diu que llegiria el directori i descriu què espera trobar-hi, la funció no està connectada. Parles amb un model de xat amb una instrucció de programació, no amb un agent. Més prompts no ho arreglaran.

Comprova les causes en aquest ordre:

1. **Canvia a un model amb suport confirmat per a eines.** No tots els models el tenen, i el nombre de paràmetres no en mostra la diferència.
2. **Confirma que l'entorn apunta a Ollama.** Executa `ollama --version` i comprova que `ANTHROPIC_BASE_URL` indiqui el punt final local.
3. **Executa `/status` a Claude Code.** Una URL base o una credencial a la configuració de Claude té prioritat sobre les variables de shell que acabes d'exportar.

## Què continua sent exclusiu del núvol

Coneix els límits abans de reconstruir un flux de treball al voltant de la inferència local.

| Funció | Amb models locals | Núvol |
|---|---|---|
| Xat i edició de fitxers | Sí | Sí |
| Crides a eines | Depèn del model | Sí |
| Subagents | Sí | Sí |
| Cerca web | Proporcionada per Ollama | Sí |
| **Cowork** | Amb la integració Claude Desktop | Sí |
| Mode automàtic | Amb la integració Claude Desktop | Sí |
| Prompts programats | Amb `/loop` a Claude Code | Sí |

La configuració local té tres limitacions:

- **El raonament amb diversos fitxers empitjora abans que la velocitat.** Un model local treballa bé amb un fitxer, prou bé amb tres i malament amb tot un repositori. Ajusta la mida de la tasca.
- **Alguns models cloud necessiten un pla de pagament d'Ollama.** També has d'haver iniciat sessió i activar-los.
- **La connexió directa al núvol limita algunes funcions.** La cerca web allotjada i el control avançat d'eines no tenen suport complet si no fas la instal·lació local.

*La inferència local va bé per a tasques acotades i verificables, però pitjor per a treballs amplis i ambigus. Organitza la feina tenint en compte aquesta diferència.*

## Automatitzar

Dues funcions permeten anar més enllà de les sessions interactives.

### Execució sense interfície per a scripts i CI

L'opció `--yes` omet els selectors interactius i baixa el model si cal. Necessita `--model`, i tot el que ve després de `--` es passa directament a Claude Code:

```bash
ollama launch claude --model gemma4:cloud --yes -- -p "how does this repository work?"
```

**Vigila el model de permisos.** Claude Code demana confirmació abans de la majoria d'accions. Per tant, l'execució sense interfície necessita regles de permisos configurades o un entorn aïllat. No dirigeixis un agent sense supervisió a un repositori important.

### Prompts programats amb `/loop`

Dins d'una sessió de Claude Code, `/loop` executa un prompt o una ordre slash amb un interval:

```text
/loop 30m Revisa les meves PR obertes i resumeix-ne l’estat
/loop 1h Investiga les notícies recents d’IA i resumeix-ne els avenços principals
/loop 15m Revisa les incidències noves de GitHub i prioritza-les
```

*Funciona mentre la sessió està oberta. No és un dimoni de fons i s'atura quan acaba la sessió.*

## Resolució de problemes

| Símptoma | Causa probable | Solució |
|---|---|---|
| **Connexió rebutjada** | Ollama no s'està executant | Executa `ollama serve` i comprova-ho amb `curl http://localhost:11434/api/tags` |
| **Descriu les accions en lloc de fer-les** | El model seleccionat no admet crides a eines | Canvia a un model amb suport confirmat |
| **S'utilitza una clau API real en lloc del punt final local** | `ANTHROPIC_API_KEY` encara està exportada | Assigna-hi una cadena buida, com s'ha indicat abans |
| **Cowork no apareix després de configurar-ho** | S'ha configurat la CLI de Claude Code en lloc de Claude Desktop | Per a Cowork, fes servir el flux d'Ollama **Apps** |
| **La generació és lenta** | El context és massa gran o has triat un model dens quan n'hi ha prou amb un d'espars | Redueix el context i prova un model mixture-of-experts |
| **Les variables exportades no fan efecte** | Els fitxers de configuració de Claude tenen prioritat sobre les variables de shell | Comprova els fitxers de configuració i executa `/status` |
| **Fallen les peticions en segon pla** | Claude Code tria un model petit per a tasques internes | Apunta la substitució del model petit al mateix model local |

*Dues d'aquestes set incidències tenen el mateix origen. La majoria dels problemes de configuració provenen d'un punt final incorrecte o d'un model sense crides a eines.*

## Punts clau

- **Claude Desktop i Claude Code són integracions separades.** Cowork és a Claude Desktop i es configura a macOS des del panell **Apps** d'Ollama. La ruta CLI no ofereix Cowork.
- **Una ordre inicia la ruta CLI:** `ollama launch claude`. La configuració manual necessita tres variables, i **moltes guies ometen `ANTHROPIC_API_KEY=""`**.
- **No cal fer una instal·lació local.** Apunta Claude Code a `https://ollama.com` amb una clau API.
- **Fixa el context a 64K o més abans de valorar el model.** Una finestra petita pot semblar un problema de raonament.
- **Verifica les crides a eines amb una petició.** Si el model descriu què faria, tens un generador de text, no un agent.
- **Els paquets Bonsai ternaris no funcionen aquí.** Necessiten el fork de llama.cpp de Prism ML, que l'Ollama estàndard no pot carregar.
- **Desconnectar és segur.** Tancar Ollama restaura la configuració anterior de Claude. També pots executar `ollama launch claude-desktop --restore` des del terminal.

## Passos següents

1. **Instal·la Ollama i baixa un model amb suport confirmat per a eines** abans de tocar la configuració de Claude: **[Biblioteca de models d'Ollama](https://ollama.com/library)**
2. **Llegeix la pàgina d'Ollama sobre Claude Code** per conèixer les opcions i els models actuals: **[Integració de Claude Code](https://docs.ollama.com/integrations/claude-code)**
3. **Fes servir la pàgina de Claude Desktop** si vols Cowork: **[Integració de Claude Desktop](https://docs.ollama.com/integrations/claude-desktop)**
4. **Tria el maquinari abans de comprar-lo**, amb les categories de memòria de la guia d'inferència local: **[IA local el 2026: un model 27B supera Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)**
5. **Comprova què pot fer un equip més petit** si vols un agent sempre actiu en un dispositiu de baix consum: **[Quins models d'IA funcionen en un Raspberry Pi 4 o 5?](/articles/ai-models-raspberry-pi-4-5/)**

## Articles relacionats

| Article | Què inclou |
|---|---|
| **[IA local el 2026: un model 27B supera Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | Referència de rendiment per a inferència local, quantització ternària i selecció de maquinari |
| **[Quins models d'IA funcionen en un Raspberry Pi 4 o 5?](/articles/ai-models-raspberry-pi-4-5/)** | Inferència local per a un assistent petit que sempre està actiu |
| **[Crear un assistent d'IA per a Meshtastic que protegeix la privadesa](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | Un model local que controla una ràdio sense xarxa, amb la privadesa com a prioritat |
| **[Millors extensions de VS Code per al desenvolupament d'IA](/articles/best-visual-studio-code-extensions-for-ai/)** | Eines d'editor per combinar amb un agent local de programació |

## Referències

1. [Integració de Claude Code - documentació d'Ollama](https://docs.ollama.com/integrations/claude-code)
2. [Integració de Claude Desktop - documentació d'Ollama](https://docs.ollama.com/integrations/claude-desktop)
3. [Biblioteca de models d'Ollama](https://ollama.com/library)
4. [Qwen3.8 - biblioteca de models d'Ollama](https://ollama.com/library/qwen3.8)
5. [Claude Cowork amb models locals - PromptSpace](https://www.promptspace.in/blog/how-to-use-claude-cowork-with-local-models-2026-guide)
6. [Fork de llama.cpp de Prism ML - nuclis ternaris](https://github.com/PrismML-Eng/llama.cpp)
