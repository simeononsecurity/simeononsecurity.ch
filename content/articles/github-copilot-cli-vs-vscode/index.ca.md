---
title: "GitHub Copilot CLI contra VS Code: comparació del flux de treball de 2026"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Compara l’agent de terminal de Copilot amb l’experiència a VS Code, amb el context de l’editor, les diferències visuals, el mode Agent, la integració CLI i les polítiques del compte."
genre: ["Eines per a desenvolupadors", "Intel·ligència artificial", "Desenvolupament de programari"]
tags: ["GitHub Copilot CLI contra VS Code", "Copilot CLI", "GitHub Copilot", "VS Code", "mode Agent", "CLI contra GUI", "context de l’editor", "suggeriments en línia", "diferència visual", "sessions de Copilot", "agent de terminal", "flux de GitHub", "revisió de codi", "integració IDE", "eines MCP", "permisos de l’agent", "AI Credits", "eines de desenvolupament", "assistent de programació", "automatització"]
cover: "/img/cover/github-copilot-cli-vs-vscode.webp"
coverAlt: "Indicació de terminal connectada a una selecció de l’editor i a una diferència visual en un espai de programació blau i verd"
coverCaption: ""
---

**GitHub Copilot CLI i Copilot a VS Code ofereixen punts d’entrada diferents per programar.** CLI comença amb l’intèrpret d’ordres i una tasca. VS Code combina context de l’editor, suggeriments, xat i fluxos d’agent. Avalua’ls amb la mateixa política de compte i repositori.

**L’elecció no és exclusiva.** GitHub documenta una connexió entre Copilot CLI i VS Code. Una tasca de terminal aprofita la selecció de l’editor i la revisió visual quan connectes les dues eines explícitament.

## Idees principals

- **Fes servir Copilot CLI per a tasques de terminal** i invocacions programàtiques admeses.
- **Fes servir Copilot a VS Code per a feina centrada en l’editor**, amb assistència en línia i mode Agent.
- **Connecta CLI amb VS Code** quan necessitis prompts de terminal amb context i diferències de l’editor.
- **Verifica el compte, el model i les polítiques**, encara que pertanyin a la mateixa família de productes.

**Abast i data:** La documentació oficial es va comprovar el 10 d’octubre de 2026. Aquesta comparació tracta el CLI independent `copilot` i Copilot a VS Code, no l’antiga extensió `gh copilot` ni un agent del núvol assignat a una issue de GitHub. Cal un repositori provable i accés autoritzat a Copilot. Reserva una hora per a la prova.

## Tres maneres de treballar

| Flux | Interacció principal | Tasca de prova adequada |
|---|---|---|
| **CLI independent** | Prompt de terminal i sortida d’ordres | Explicar i corregir un error de prova reproduït |
| **Integració amb VS Code** | Selecció de l’editor, xat, suggeriments i diferències | Modificar una funció seleccionada i les seves proves |
| **CLI connectat a VS Code** | Tasca de terminal amb context i revisió de l’editor | Investigar des de l’intèrpret i inspeccionar el pedaç visualment |

**El mode híbrid continua sent una sessió CLI.** Executar-lo en un terminal integrat no el converteix automàticament en una conversa nativa del mode Agent. Comprova la sessió i la connexió actives.

## Què ofereix CLI

```bash
copilot
```

**L’ordre independent actual inicia l’agent de terminal.** La [visió general de Copilot CLI](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-cli) de GitHub descriu l’ús interactiu i programàtic, la planificació i els permisos d’eines.

**Una bona primera tasca té un error concret.** Dona l’ordre que falla, el comportament esperat i una restricció contra refactoritzacions no relacionades. Demana reproduir el problema abans de canviar fitxers i compara l’explicació amb la sortida observada.

**L’automatització necessita límits explícits.** Usa les [guies d’ús de CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli) per a la invocació actual. Defineix eines, temps i tractament de sortida abans d’executar feines sense supervisió.

**El sandbox canvia el límit de la prova.** GitHub documenta l’aïllament local per a fitxers, xarxa i sistema, i sandboxes del núvol. Prova l’entorn, la xarxa i l’escriptura amb una fixture innòcua abans de tocar un repositori real.

## Què afegeix VS Code

**L’experiència de Copilot a l’IDE inclou suggeriments, xat i tasques d’agent.** La [visió general de l’IDE](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-in-ides) separa aquestes funcions. L’assistència en línia encaixa amb feina on tu continues sent l’editor principal. El mode Agent encaixa amb canvis limitats en diversos fitxers.

**El mode Agent edita i executa ordres de manera iterativa.** La [guia del mode Agent](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/use-copilot-agents/use-agent-mode?tool=vscode) descriu seleccionar Agent, revisar canvis i ampliar eines amb MCP. La disponibilitat depèn també de la configuració i l’administració.

**Avalua la transferència de context de forma deliberada.** Selecciona una funció, demana una explicació del tractament d’errors i després un canvi petit amb una prova independent. Registra els fitxers veïns necessaris i les suposicions corregides.

{{< figure src="copilot-terminal-editor-bridge.webp" alt="Indicació de terminal vinculada a una selecció de l’editor i a una diferència de codi costat per costat dins un repositori" caption="Una sessió CLI connectada combina l’entrada del terminal amb la revisió de l’editor" >}}

## Connecta les dues interfícies

```text
/ide
```

**Fes servir `/ide` en una sessió interactiva de Copilot CLI** per inspeccionar o canviar la connexió de VS Code. La [guia de connexió](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/connecting-vs-code) documenta l’espai de treball de confiança, la selecció compartida i els canvis proposats com a diferències.

**La connexió automàtica depèn que coincideixi l’espai de treball.** Un CLI local no connecta amb un Codespace remot només perquè coincideixi el nom del repositori. Executa CLI en l’entorn corresponent. Una autorització àmplia també evita l’aprovació del diff. Revisa els permisos si desapareixen els prompts.

**Les transcripcions CLI apareixen a Sessions de VS Code**, amb continuació mitjançant Resume in Terminal. Això conserva el flux de terminal, però no crea una sessió nativa intercanviable de l’agent de l’editor.

| Abans de connectar | Verifica |
|---|---|
| **Espai de treball** | La carpeta correcta és oberta i fiable |
| **Lloc d’execució** | CLI i editor apunten al mateix entorn |
| **Selecció** | El codi ressaltat correspon a la petició |
| **Permisos** | La revisió dels canvis proposats continua activa si cal |
| **Sessió** | Continua la conversa correcta |

## Models, facturació i política

**Fes servir el mateix model per provar les dues interfícies quan sigui possible.** Si difereix, registra-ho. Un altre model, context o conjunt d’eines canvia l’experiment.

**Verifica el recompte d’ús actual del compte.** La documentació del mode Agent esmenta AI Credits. No apliquis estimacions antigues de sol·licituds premium sense revisar la facturació. Una petició CLI i una tasca de l’editor no són automàticament la mateixa unitat de feina.

**L’accés de l’organització és un requisit.** Si falta una funció, revisa la política abans de reinstal·lar l’extensió. Un inici de sessió del proveïdor no autoritza modificar tots els repositoris ni contactar tots els serveis externs.

## Fes una prova aparellada

**Prepara dues còpies de la mateixa revisió inicial.** Usa instruccions i proves d’acceptació iguals. Prova primer el CLI independent i després el mode Agent de VS Code. Afegeix el CLI connectat si el flux mixt encaixa amb la teva feina.

| Mesura | Motiu per registrar-la |
|---|---|
| **Context proporcionat** | Revela l’esforç manual ocult |
| **Correcció** | Separa codi plausible d’una correcció verificada |
| **Passos d’aprovació** | Mostra la supervisió necessària |
| **Temps de revisió** | Mesura l’esforç per entendre el pedaç |
| **Reparacions manuals** | Captura la feina restant |
| **Ús** | Relaciona el cost amb els resultats acceptats |

**Mantén la recuperació dins la prova.** Rebutja un enfocament i explica el motiu. Observa si el següent intent conserva feina útil i respecta la correcció. Això mostra millor l’ús diari que una demostració única.

## Resolució de problemes i passos següents

**Si CLI connecta amb la finestra equivocada**, inspecciona `/ide` i tria l’espai correcte. Si desapareix l’aprovació visual, revisa els permisos d’edició. Si no hi ha mode Agent, revisa l’extensió i la política de l’organització.

**Tria el CLI independent** quan dominin el shell i les invocacions repetibles. **Tria VS Code** quan dominin el context de selecció, el treball en línia i la revisió gràfica. **Usa el CLI connectat** quan entrada i inspecció funcionin bé juntes.

**Per comparar proveïdors**, llegeix la [comparació principal de CLI](/articles/cli-coding-agents-comparison/) o la [comparació principal de GUI](/articles/gui-coding-agents-comparison/). Mantén-les separades d’aquesta prova dins la mateixa família.
