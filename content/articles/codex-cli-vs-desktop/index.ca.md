---
title: "Codex CLI contra Desktop: comparació del flux de treball de 2026"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Tria entre Codex al terminal i l'espai de treball de programació d'escriptori d'OpenAI. Compara scripts, worktrees, revisió visual, programacions i entorns d'execució."
genre: ["Eines per a desenvolupadors", "Intel·ligència artificial", "Desenvolupament de programari"]
tags: ["Codex CLI contra desktop", "aplicació Codex", "ChatGPT desktop", "OpenAI Codex", "Codex CLI", "programació al terminal", "agent de programació d'escriptori", "codex exec", "worktrees de Git", "tasques programades", "revisió de codi", "permisos de l'agent", "CLI contra GUI", "execució local", "desenvolupament remot", "flux de programació", "instruccions del projecte", "automatització", "eines per a desenvolupadors", "agent harness"]
cover: "/img/cover/codex-cli-vs-desktop.webp"
coverAlt: "Espais de programació al terminal i a l'escriptori connectats a un símbol de repositori amb accents turquesa i blaus"
coverCaption: ""
---

**Codex CLI** encaixa amb un flux de treball controlat per shell, amb ordres explícites i execucions programables. **Codex a l'escriptori** encaixa amb treball organitzat al voltant de projectes, converses, sortides visuals i panells de revisió. Tria la interfície segons com supervises el treball i mantén constants el model, el repositori i la política d'execució.

**Nota sobre el nom:** la documentació anterior de l'aplicació Codex d'OpenAI ara redirigeix a la [documentació de l'aplicació ChatGPT per a escriptori](https://learn.chatgpt.com/docs/app). Aquesta guia usa “Codex desktop” per al flux de programació dins l'aplicació. No equipara un xat normal sense accés al repositori amb un agent de programació.

## Punts clau

- **Usa la CLI per combinar ordres de shell** i executar tasques programables repetibles.
- **Usa l'escriptori per organitzar projectes**, revisar visualment i gestionar tasques programades.
- **Mantén explícita la ubicació d'execució**, sobretot quan treballes amb connexions remotes.
- **La interfície no garanteix millor codi** ni crea una quota d'inferència independent.

**Abast i data:** documentació oficial revisada el 10 d'octubre de 2026. Les recomanacions tracten del flux de treball, no del rendiment mesurat del model. Els requisits són un repositori, proves funcionals i accés adequat al compte. Reserva una hora per a una prova petita entre interfícies.

## Compara els fluxos de treball

| Necessitat | Codex CLI | Codex desktop |
|---|---|---|
| **Iniciar el treball al repositori** | Llança des d'un directori de shell | Selecciona un projecte i un entorn d'execució |
| **Repetir una tasca amb script** | `codex exec` | Prepara prompts i inspecciona visualment les sortides |
| **Inspeccionar diverses tasques** | Flux de terminal i sessions | Organització de projectes i xats |
| **Revisar canvis** | Ordres de terminal i controls de revisió | Panells de diferències i revisió |
| **Gestionar programacions** | Executor extern al voltant d'un script | Interfície de gestió de tasques programades |
| **Aïllar canvis** | Tria un checkout o worktree separat | Flux de worktree integrat |

**Els fonaments compartits de l'agent importen.** OpenAI descriu la CLI, l'aplicació i l'extensió d'IDE com a interfícies del seu agent runtime a [Codex com a plataforma](https://developers.openai.com/blog/codex-as-a-platform). El runtime gestiona estat, eines i política. Les diferències d'interfície encara afecten el context que aportes i com inspecciones el resultat.

## On encaixa la CLI

```bash
codex
```

**Llança-la des del repositori previst.** La [guia de CLI](https://learn.chatgpt.com/docs/codex/cli) documenta la inspecció interactiva, l'edició, les ordres i la revisió. Usa aquesta via quan el teu flux actual ja gira al voltant de sessions de terminal i sortida d'ordres.

```bash
codex exec "Identify the documented test command. Do not modify files."
```

**Usa `codex exec` per a una tasca amb límits clars.** La [referència del mode no interactiu](https://learn.chatgpt.com/docs/non-interactive-mode) explica com s'emeten el progrés i la sortida final. Aplica una política d'execució només de lectura quan investigues. Una frase que demana no editar és una instrucció, no un límit imposat al sistema de fitxers.

**Un script de producció necessita més que aquest exemple.** Defineix credencials, selecció del repositori, temps d'espera, permisos, emmagatzematge de sortida i gestió d'errors. Fes que el treball produeixi proves per a un revisor abans de considerar canvis automàtics. Mantén el contracte d'execució sota control de versions.

## On encaixa l'escriptori

**L'escriptori organitza el treball relacionat en un sol espai.** La documentació actual de l'aplicació d'OpenAI descriu el canvi de projecte, la inspecció de fitxers, les eines connectades i les tasques llargues. Això permet passar entre implementació, un artefacte renderitzat i revisió sense reconstruir el context des de diverses finestres de terminal.

**La revisió és un diferenciador concret.** La [documentació de revisió de codi](https://learn.chatgpt.com/docs/code-review) descriu la visualització de descripcions, fitxers canviats, comentaris i comprovacions. Usa aquestes vistes per investigar un pedaç i decideix si compleix el requisit. El revisor encara necessita proves independents del comportament fora del diff.

**Prova l'escriptori en una tasca visual.** Demana un petit ajust de disseny amb una captura i requisits explícits de finestra gràfica. Compara l'esforç d'adjuntar el context, inspeccionar el resultat i demanar una correcció. Mesura per separat el temps de revisió humana i el temps de resposta del model.

{{< figure src="codex-terminal-desktop-review.webp" alt="Panells d'automatització del terminal i revisió d'escriptori connectats al mateix repositori i a una llista de validació independent" caption="Mantén constants el repositori i els criteris d'acceptació en comparar interfícies" >}}

## Worktrees i ubicació d'execució

**Un worktree és un altre checkout d'un repositori Git.** La [guia de worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees) d'OpenAI descriu xats paral·lels aïllats i el moviment de treball entre el checkout local i un worktree gestionat. Els fitxers i les ordres romanen a l'ordinador o entorn de desenvolupament que allotja el projecte.

**L'aïllament no fusiona el resultat.** Revisa el diff, executa les comprovacions i decideix com portar els canvis a la branca prevista. Les dependències, els fitxers ignorats i els serveis externs també requereixen atenció en començar des d'un checkout nou.

| Abans d'una tasca | Confirma |
|---|---|
| **Repositori** | Projecte i revisió base correctes |
| **Checkout** | Directori existent o worktree aïllat |
| **Amfitrió d'execució** | Ordinador que conté fitxers i eines |
| **Entorn** | Runtime, dependències i serveis de proves |
| **Permisos** | Escriptures de fitxers i accés de xarxa permesos |

**Usa el mateix entorn en la comparació.** Una tasca d'escriptori en una estació configurada i una tasca CLI en un contenidor mínim proven més que la preferència d'interfície. Registra les diferències ambientals abans d'atribuir els errors al client.

## Programació i permisos

**L'escriptori ofereix gestió de programacions.** La [guia de tasques programades](https://learn.chatgpt.com/docs/automations) d'OpenAI distingeix la interfície de gestió de la CLI. El treball local programat requereix que l'ordinador i l'aplicació corresponents romanguin disponibles. Un programador de shell al voltant de `codex exec` és una disposició operativa separada.

**Els permisos s'apliquen a l'entorn d'execució.** Comprova el perfil efectiu en lloc d'inferir la seguretat d'un prompt de terminal o gràfic. La [referència de permisos](https://learn.chatgpt.com/docs/permissions) d'OpenAI documenta els límits del sistema de fitxers i la xarxa. Una aprovació GUI i una política sandbox resolen problemes diferents.

**L'accés al compte necessita la seva pròpia comprovació.** Confirma l'inici de sessió actiu, el model disponible i la pantalla d'ús a cada interfície. No facis pressupostos com si obrir un segon client creés una altra quota independent. Registra la via de facturació abans de comparar el cost per tasca.

## Una prova d'una hora

1. **Prepara un canvi limitat** amb una prova d'acceptació independent i una base neta.
2. **Executa'l a cada interfície** des de checkouts separats amb paràmetres de model i política coincidents.
3. **Demana una correcció** després d'inspeccionar el primer pedaç.
4. **Revisa el diff final** i executa les mateixes ordres de verificació.
5. **Registra el teu esforç** en aportar context, trobar la sortida i aprovar el resultat.

**Tria la CLI** si la tasca és més fàcil de repetir i inspeccionar amb eines de shell. **Tria l'escriptori** si l'organització del projecte i la revisió visual redueixen el teu esforç de supervisió. Mantenir totes dues instal·lades és raonable quan cadascuna serveix una part diferent del flux.

**Conserva el registre de la prova amb el resultat.** Anota la revisió inicial, el model seleccionat, l'amfitrió d'execució, el perfil de permisos, les ordres executades i la sortida final de verificació. Sense aquests camps, una comparació posterior també compara canvis ambientals ocults.

## Resolució de problemes i passos següents

**Un fitxer absent sol requerir una comprovació de l'entorn.** Verifica projecte, checkout i amfitrió abans de demanar a l'agent que recreï res. Per a resultats de proves diferents, compara la selecció del runtime i la configuració de dependències. Per a una programació local aturada, confirma que l'aplicació i l'ordinador estaven disponibles.

**Compara els proveïdors per separat.** Usa la [comparació principal de CLI](/articles/cli-coding-agents-comparison/) per a alternatives de terminal i la [comparació principal de GUI](/articles/gui-coding-agents-comparison/) per a editors i extensions gràfiques. Conserva el registre del model i la tasca d'aquesta prova per a futures actualitzacions.
