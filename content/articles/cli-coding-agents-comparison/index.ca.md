---
title: "Comparació d'agents de codificació CLI: Claude Code, Codex, Gemini, OpenCode, Copilot i Aider"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Compara sis agents de codificació de terminal segons el flux de treball, l'automatització, l'accés als models, els permisos i l'esforç de revisió. Crea una llista curta amb una prova repetible al repositori."
genre: ["Eines per a desenvolupadors", "Intel·ligència artificial", "Desenvolupament de programari"]
tags: ["agents de codificació CLI", "Claude Code CLI", "Codex CLI", "Gemini CLI", "OpenCode CLI", "GitHub Copilot CLI", "Aider", "agents de terminal", "automatització headless", "agent harness", "proveïdors de models", "fluxos Git", "comparació d'agents de codificació", "eines shell", "assistent de codificació", "permisos de l'agent", "context del repositori", "automatització CI", "revisió de codi", "eines per a desenvolupadors"]
cover: "/img/cover/cli-coding-agents-comparison.webp"
coverAlt: "Sis finestres de terminal abstractes envolten un símbol de repositori en una graella equilibrada sobre un fons fosc"
coverCaption: ""
---

Els **agents de codificació de terminal** comparteixen una interfície familiar, però difereixen en la recopilació de context, l'edició de fitxers, les sol·licituds d'aprovació i la integració amb scripts. Aquesta guia compara Claude Code CLI, Codex CLI, Gemini CLI, OpenCode CLI, GitHub Copilot CLI i Aider. Avalua els seus fluxos de terminal separadament dels productes d'escriptori de cada proveïdor.

**Comença per les teves restriccions.** L'accés al proveïdor, l'automatització repetible i els hàbits de revisió filtren millor que una classificació general. Les recomanacions següents són judicis editorials basats en documentació oficial revisada el 10 d'octubre de 2026, no classificacions de rendiment mesurat.

## Idees principals

- **Claude Code, Codex i Gemini CLI** mereixen una prova si vols els seus fluxos de models propis.
- **OpenCode i Aider** serveixen per experimentar amb diversos proveïdors de models, amb enfocaments diferents d'interacció i edició.
- **Copilot CLI** mereix atenció quan l'accés a GitHub i la política de l'organització ja defineixen el teu flux.
- **Una interfície de terminal no implica inferència local**, elecció il·limitada de models ni execució sense supervisió.

**Requisits previs:** Git, un checkout d'un sol ús, proves funcionals i credencials de models aprovades. La dificultat és intermèdia. Reserva una tarda per comparar dues eines seleccionades en tres tasques petites.

## La llista curta

| Eina de terminal | Motiu per avaluar-la | Decisió pendent |
|---|---|---|
| **Claude Code CLI** | Treball de repositori centrat en Claude | Ruta del compte i política de permisos |
| **Codex CLI** | Treball interactiu i execució amb scripts | Configuració del sandbox i gestió de sortida |
| **Gemini CLI** | Flux de Gemini i sortida estructurada headless | Autenticació, quotes i política d'eines |
| **OpenCode CLI** | Selecció del proveïdor i agents configurables | Compatibilitat del model i de l'endpoint |
| **Copilot CLI** | Accés a Copilot des del shell | Accés de l'organització i aprovació d'eines |
| **Aider** | Programació en parella centrada en Git | Selecció de fitxers i model d'edició |

**Aquesta és una llista delimitada.** Compara sis fluxos de terminal establerts, no tots els productes amb CLI. Els editors gràfics i les extensions pertanyen a la [comparació d'agents de codificació GUI](/articles/gui-coding-agents-comparison/).

## Claude Code i Codex

**Claude Code CLI** ofereix sessions interactives, converses reprenibles, entrada per pipe i un mode d'impressió per a scripts. La seva [referència CLI](https://code.claude.com/docs/en/cli-reference) documenta aquests punts d'entrada. Prova'l si vols que Claude treballi en canvis del repositori mentre dirigeixes les tasques des del shell.

**Codex CLI** exposa inspecció del repositori, edicions, execució d'ordres i revisió en una interfície de terminal. La [documentació CLI d'OpenAI](https://learn.chatgpt.com/docs/codex/cli) descriu els controls interactius. El [mode no interactiu](https://learn.chatgpt.com/docs/non-interactive-mode) ofereix `codex exec` per a scripts i integració contínua.

**Tria entre aquests segons el treball completat.** Dona a cada eina un error desconegut i una prova existent que falli. Compara l'explicació, l'abast del pedaç, la selecció de proves i la recuperació després d'un enfocament rebutjat. Un missatge final segur no demostra la correcció.

## Gemini CLI i Copilot

**Gemini CLI** documenta el context del projecte, les extensions, l'execució d'eines i l'automatització a la seva [guia oficial](https://geminicli.com/docs/). La seva [referència headless](https://geminicli.com/docs/cli/headless/) especifica la sortida estructurada i els codis de sortida. Això fa que la gestió de sortida sigui una part concreta de la prova, no una suposició basada en la disponibilitat del terminal.

**GitHub Copilot CLI** admet treball interactiu i prompts programàtics mitjançant l'ordre independent actual `copilot`. La seva [documentació del producte](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-cli) cobreix la planificació i els permisos d'eines. Avalua'l amb el compte i les polítiques del teu equip. La marca GitHub no dona accés automàtic a tots els repositoris o serveis.

| Entrada d'automatització | Família d'ordres documentada |
|---|---|
| **Claude Code** | `claude -p` |
| **Codex** | `codex exec` |
| **Gemini CLI** | `gemini -p` |
| **Copilot CLI** | `copilot -p` |

**El mode headless necessita una política d'execució.** Defineix accions permeses, límits de temps, gestió d'errors i recollida d'artefactes abans de posar un agent en una pipeline. Que un procés acabi correctament no demostra que el codi generat compleixi els criteris d'acceptació.

## OpenCode i Aider

**OpenCode CLI** combina una UI de terminal interactiva amb operacions de línia d'ordres. La seva [referència CLI](https://opencode.ai/docs/cli/) documenta `opencode run`, mentre que la [guia de proveïdors](https://opencode.ai/docs/providers/) descriu les connexions de models. Prova'l quan la flexibilitat de proveïdors justifiqui gestionar compatibilitat i facturació.

**Aider** se centra en la programació en parella dins d'un repositori Git. La seva [documentació](https://aider.chat/docs/) cobreix la selecció de fitxers, els mapes del repositori, les connexions de models i la integració lint/test. Prova'l quan prefereixis dirigir una conversa d'edició delimitada i mantenir els canvis a prop d'un flux Git explícit.

**Els estils d'interacció diferents necessiten expectatives diferents.** Un assistent d'edició limitat i un agent que explora un repositori complet no consumeixen el context igual. Registra els fitxers proporcionats, l'exploració permesa i la direcció humana necessària. No atribueixis un guany de productivitat a una eina després d'haver seleccionat tu mateix el seu context sense registrar-ho.

{{< figure src="terminal-agent-evaluation-flow.webp" alt="Sessions de terminal abstractes alimenten una revisió compartida de pedaços, una llista de proves i un registre del cost de la tasca" caption="Fes servir els mateixos criteris d'acceptació a cada flux de terminal" >}}

## Models, accés i cost

**L'agent és el programari que envolta el model.** Construeix sol·licituds, gestiona resultats d'eines, administra l'estat de la conversa i aplica la política d'execució. El model i l'endpoint de servei influeixen en el raonament, la fiabilitat de les crides d'eines, la latència i el context disponible.

**La flexibilitat del proveïdor té costos operatius.** Un endpoint personalitzat afegeix decisions sobre identificadors de models, configuració de context, autenticació i suport d'eines. Un servei integrat redueix algunes opcions de configuració, però vincula l'accés al seu compte i polítiques. Cap opció estableix una classificació universal de qualitat.

| Categoria de cost | Inclou-la a la prova |
|---|---|
| **Assignació del compte** | Accés inclòs, límits de velocitat i comportament en esgotar-se |
| **Inferència mesurada** | Ús de prompt, sortida, cache i reintents |
| **Servei local** | Maquinari, electricitat i manteniment del runtime |
| **Esforç humà** | Configuració, correccions i revisió final |
| **Treball fallit** | Execucions abandonades i pedaços revertits |

**Compara el cost per canvi acceptat.** Separa les quotes de subscripció dels càrrecs API incrementals i del temps del desenvolupador. Un client gratuït amb inferència de pagament difereix d'una subscripció amb una assignació. Revisa les condicions actuals del compte abans de canviar de proveïdor.

**Fixa les entrades de comparació.** Registra cada versió de CLI, identificador del model, proveïdor, revisió inicial, mode de permisos i configuració d'eines. Repeteix una tasca després de qualsevol canvi. Altrament, un resultat millor identifica un sistema canviat, no una interfície de terminal millor.

## Permisos i context del repositori

**L'aprovació i l'aïllament són controls diferents.** Una sol·licitud d'aprovació pregunta si una acció ha de continuar. Un sandbox limita els recursos disponibles per a una acció executada. Comprova tots dos, inclòs l'accés a fitxers, xarxa i ordres iniciades per les eines.

**La documentació de permisos de Codex** separa explícitament les regles del sistema de fitxers i de xarxa, incloses les condicions per aplicar restriccions de destinació. Usa la seva [referència de permisos](https://learn.chatgpt.com/docs/permissions) per inspeccionar la configuració instal·lada. Per a cada eina seleccionada, prova una acció permesa innòcua i una acció prohibida innòcua abans de confiar en la política.

**Les instruccions del projecte necessiten verificació.** Dona a cada eina la mateixa ordre de build, criteris d'acceptació i exclusions mitjançant el seu mecanisme d'instruccions compatible. Demana-li que repeteixi les restriccions actives abans d'editar. Un fitxer d'instruccions absent és un defecte de configuració, no un benchmark del model.

```text
Task: Fix the supplied reproduction without changing the public API.
Scope: Preserve unrelated work and avoid new dependencies.
Evidence: Run the existing regression test and relevant neighboring tests.
Report: Explain the cause, changed files, checks, and remaining uncertainty.
```

**Aquest prompt de prova és delimitat expressament.** Afegeix una reproducció coneguda i comprovacions escrites de manera independent. Usa el mateix commit inicial en checkouts separats. Registra la versió de l'eina, el model, el proveïdor, la política de permisos, el temps transcorregut i les intervencions.

## Tria la teva primera parella

| La teva prioritat | Comença la prova amb |
|---|---|
| **Flux Claude contra OpenAI** | Claude Code CLI i Codex CLI |
| **Flux Google contra OpenAI** | Gemini CLI i Codex CLI |
| **Flexibilitat del proveïdor** | OpenCode CLI i Aider |
| **Desplegament existent de GitHub** | Copilot CLI i una alternativa aprovada |
| **Claude contra proveïdors configurables** | Claude Code CLI i OpenCode CLI |

**Executa tres tasques per eina:** un error reproduït, una funció petita amb proves independents i una refactorització delimitada. Conserva els intents fallits. Revisa els pedaços sense mirar quin agent els ha produït quan sigui pràctic. Guanya el flux que produeix canvis acceptables amb menys esforç total al teu repositori.

## Resolució de problemes i passos següents

**Els resultats inesperats sovint comencen en la configuració.** Eines absents, directoris de treball incorrectes, versions de models diferents o assignacions esgotades distorsionen les comparacions. Verifica-ho abans de reescriure prompts repetidament.

**Continua amb una guia enfocada:** [OpenCode contra Claude Code](/articles/opencode-vs-claude-code/), [Codex CLI contra escriptori](/articles/codex-cli-vs-desktop/), [Claude Code CLI contra escriptori](/articles/claude-code-cli-vs-desktop/), [OpenCode CLI contra escriptori](/articles/opencode-cli-vs-desktop/), o [Copilot CLI contra VS Code](/articles/github-copilot-cli-vs-vscode/). Aquestes comparacions d'interfícies es mantenen dins de cada família de productes.
