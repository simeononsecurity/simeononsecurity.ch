---
title: "Claude Code CLI contra Desktop: comparació del flux de treball de 2026"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Compara Claude Code al terminal i a l'espai de treball Code d'escriptori, amb configuració compartida, traspàs de sessions, scripts, revisió visual i opcions de permisos."
genre: ["Eines per a desenvolupadors", "Intel·ligència artificial", "Desenvolupament de programari"]
tags: ["Claude Code CLI contra desktop", "Claude Code", "Claude Desktop", "pestanya Code", "Anthropic", "CLAUDE.md", "permisos de l'agent", "CLI contra GUI", "traspàs de sessió", "flux de programació", "diff visual", "automatització del terminal", "mode sense interfície", "configuració del projecte", "sessions locals", "sessions al núvol", "eines MCP", "revisió de codi", "eines per a desenvolupadors", "arnès de l'agent"]
cover: "/img/cover/claude-code-cli-vs-desktop.webp"
coverAlt: "Conversa al terminal i espai de treball gràfic de programació units per una fletxa de traspàs de sessió sobre un fons fosc"
coverCaption: ""
---

**Claude Code CLI i Desktop** ofereixen dues maneres de dirigir l'agent de programació d'Anthropic. La CLI afavoreix els fluxos de shell i la invocació programàtica. Desktop afavoreix un espai de treball de projecte visible, amb canvis de fitxers i revisió al costat de la conversa.

**Aquesta comparació tracta l'espai de treball de programació d'escriptori**, descrit com la pestanya Code a l'[inici ràpid d'escriptori](https://code.claude.com/docs/en/desktop-quickstart) d'Anthropic. El xat general i altres fluxos d'escriptori queden fora de l'abast. La distinció importa quan comproves l'accés al repositori i la configuració.

## Punts clau

- **Fes servir la CLI per als scripts**, l'entrada canalitzada i el treball centrat en el terminal.
- **Fes servir Desktop per a la supervisió gràfica**, els fitxers adjunts i la revisió de diffs.
- **La configuració compartida redueix la duplicació**, però el comportament de les sessions i els controls disponibles difereixen.
- **Moure una conversa exigeix un traspàs compatible**, no copiar un prompt en un xat nou.

**Abast i data:** documentació oficial comprovada el 10 d'octubre de 2026. És una comparació de funcions i fluxos de treball, no una prova de programació. Necessites un repositori comprovable i una ruta de compte aprovada. Reserva entre 45 i 60 minuts per a una prova petita.

## Mateix motor, controls diferents

**Anthropic descriu Desktop com el mateix motor subjacent amb una GUI.** La seva [referència d'escriptori](https://code.claude.com/docs/en/desktop) documenta la configuració compartida i la memòria del projecte, i diferencia les funcions del client. Les bases compartides no impliquen que cada opció de la CLI tingui un botó a Desktop.

| Activitat | CLI | Espai de treball Code de Desktop |
|---|---|---|
| **Treball interactiu** | Conversa al terminal | Conversa gràfica amb panells del projecte |
| **Invocació amb script** | Mode print i entrada canalitzada | Fes servir la CLI per a aquest flux |
| **Revisió de canvis** | Flux de terminal/editor | Diff visual integrat |
| **Organització de tasques** | Sessions del terminal i controls de la CLI | Barra lateral de sessions i disseny de l'espai de treball |
| **Treball recurrent** | Planificador extern o CI | Tasques programades de Desktop |
| **Regles del projecte** | Configuració del repositori i de l'usuari | Configuració compartida amb comportament específic de la superfície |

**Tria segons l'esforç de supervisió.** Una investigació d'errors centrada en shell i un canvi visual d'una aplicació plantegen demandes diferents a la interfície. Cap dels dos demostra un model més fort.

## Treball al terminal i scripts

```bash
claude -p "Explain the failing test and propose a fix. Do not edit files."
```

**El mode print funciona sense la conversa interactiva normal.** La [referència de la CLI](https://code.claude.com/docs/en/cli-reference) d'Anthropic documenta aquesta família d'ordres, l'entrada canalitzada i les opcions de represa. Ajusta els permisos de les eines a la investigació. El prompt anterior no substitueix una política de només lectura.

**Fes servir un script quan el contracte d'entrada i sortida sigui estable.** Alguns exemples són un informe programat, una inspecció acotada del repositori o un pas de CI que produeixi material de revisió. Defineix què compta com a fallada i desa l'evidència. No aprovis un pegat només perquè el missatge final de l'agent sembli complet.

**Mantén interactiu el treball quan quedin decisions obertes.** Si una tasca exigeix triar un disseny d'API o resoldre requisits contradictoris, una sessió de terminal amb punts de control explícits sovint necessita menys codi d'automatització que un embolcall sense interfície.

## Revisió i programació a Desktop

**Desktop ofereix un espai de treball de programació sense exigir una instal·lació separada de la CLI.** L'inici ràpid descriu la selecció del projecte, la selecció del model i l'acceptació gràfica dels canvis. Avalua'l amb un pegat que inclogui un fitxer font, una prova i un fitxer de configuració perquè la revisió impliqui més d'un panell.

**El treball programat és una funció separada de Desktop.** La [documentació de tasques programades](https://code.claude.com/docs/en/desktop-scheduled-tasks) d'Anthropic explica les tasques recurrents i els requisits d'operació. Comprova on s'executa una tasca i què ha de continuar disponible abans de basar-hi un flux diari.

**Revisa el pegat agregat.** Les aprovacions d'edicions individuals no mostren totes les interaccions entre fitxers modificats. Després de l'execució, inspecciona el diff final i executa la comprovació d'acceptació per separat.

{{< figure src="claude-cli-desktop-session-handoff.webp" alt="Conversa del terminal i revisió gràfica de codi connectades mitjançant un projecte compartit amb un traspàs de sessió controlat" caption="Un motor compartit encara necessita comprovacions explícites de sessió i entorn" >}}

## Configuració i permisos

**La configuració té abast i precedència.** La [referència de configuració](https://code.claude.com/docs/en/settings) d'Anthropic diferencia la configuració gestionada, d'usuari, de projecte i local. Verifica la configuració efectiva abans de diagnosticar una diferència entre clients. Una regla del projecte no anul·la necessàriament la política de l'organització.

**El mode de permisos canvia la interacció.** Compara els clients amb polítiques coincidents i després prova la teva política preferida per separat. No presentis menys sol·licituds d'aprovació com un avantatge incondicional. La pregunta és si les accions permeses coincideixen amb la tasca i l'entorn.

| Comprovació de configuració | Motiu |
|---|---|
| **Carpeta del projecte** | Carrega el codi i les regles de projecte previstos |
| **Ruta del compte** | Determina el context d'accés i facturació |
| **Model seleccionat** | Evita barrejar canvis d'interfície i model |
| **Política de permisos** | Controla quines operacions avancen |
| **Entorn d'execució** | Determina les ordres i proves disponibles |

**Mantén les instruccions canòniques del projecte al repositori.** Documenta les ordres de build, els fitxers exclosos i els criteris d'acceptació. Demana a l'agent que identifiqui aquestes restriccions abans d'editar. Una discrepància indica un problema de configuració a resoldre abans de comparar el comportament.

## Moure una sessió

```text
/desktop
```

**El traspàs documentat de CLI a Desktop desa la sessió i surt de la CLI.** La referència d'escriptori limita aquesta ordre a sessions de subscripció compatibles a macOS i Windows x64. Les sessions amb clau d'API i proveïdors externs no reben el mateix camí. Comprova la versió instal·lada i el compte abans de dependre'n.

**Tracta el traspàs com una transició controlada.** Acaba o atura l'operació activa, identifica la branca actual i inspecciona els canvis pendents. Després d'obrir la interfície de destinació, verifica el repositori i pregunta pel pas següent. No iniciïs una segona implementació als mateixos fitxers mentre la primera continuï executant-se.

**Compartir fitxers és diferent de compartir una conversa.** Dos clients que obren el mateix checkout veuen els canvis del sistema de fitxers, però una conversa nova no té el raonament ni les restriccions de la sessió original. Desa un registre breu de la tasca al repositori quan necessitis un traspàs portable.

## Tria amb una prova petita

**Fes servir un error amb un símptoma visible.** Proporciona la reproducció, el comportament esperat i els fitxers que l'agent ha de conservar. Executa intents separats des de la mateixa revisió base, amb el mateix model i ajustos de permisos.

| Etapa de la prova | Observa |
|---|---|
| **Context** | Esforç per adjuntar registres, fitxers i captures |
| **Implementació** | Interrupcions i necessitats d'aclariment |
| **Revisió** | Facilitat d'inspeccionar cada fitxer modificat |
| **Correcció** | Resposta a un enfocament rebutjat |
| **Finalització** | Resultat de la prova independent i diff net |

**Prefereix la CLI** quan dominin els scripts i el context del terminal. **Prefereix Desktop** quan l'estat visible del projecte i la revisió gràfica redueixin la fricció. Fes servir tots dos deliberadament si alternes aquestes necessitats.

## Resolució de problemes i passos següents

**Si Desktop no té una ordre disponible a la CLI**, consulta la comparació de funcions en lloc d'assumir una fallada d'instal·lació. Si les ordres només funcionen al terminal, compara l'entorn d'execució i el descobriment del runtime. Si el traspàs no està disponible, comprova la plataforma i l'elegibilitat d'autenticació.

Per a una llista més àmplia, llegeix la [comparació de CLI](/articles/cli-coding-agents-comparison/) o la [comparació de GUI](/articles/gui-coding-agents-comparison/). Per a una comparació d'agents de diversos proveïdors, consulta [OpenCode contra Claude Code](/articles/opencode-vs-claude-code/).
