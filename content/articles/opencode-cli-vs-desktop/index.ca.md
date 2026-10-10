---
title: "OpenCode CLI vs Desktop: comparació del flux de treball de 2026"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Compara els clients de terminal i d'escriptori d'OpenCode mitjançant la seva arquitectura de servidor, la configuració del proveïdor, els scripts, l'estat de sessió i la resolució de problemes."
genre: ["Eines per a desenvolupadors", "Intel·ligència artificial", "Desenvolupament de programari"]
tags: ["OpenCode CLI vs desktop", "OpenCode Desktop", "terminal OpenCode", "servidor OpenCode", "TUI", "CLI vs GUI", "agent de codi", "configuració del proveïdor", "models locals", "inferència allotjada", "automatització sense interfície", "opencode run", "opencode serve", "permisos de l'agent", "regles del projecte", "estat de sessió", "flux del desenvolupador", "autenticació del servidor", "eines de codi amb IA", "arnès de l'agent"]
cover: "/img/cover/opencode-cli-vs-desktop.webp"
coverAlt: "Clients de terminal i d'escriptori connectats a un servidor central amb símbols separats per al repositori i la inferència"
coverCaption: ""
---

**OpenCode CLI i Desktop són clients del mateix producte d'agent de codi.** La interfície de terminal s'adapta al treball amb teclat i als scripts. L'aplicació d'escriptori ofereix un espai de treball gràfic. La comparació important inclou el servidor, el projecte, el proveïdor i la configuració que hi ha darrere de cada client.

**Tria la interfície després d'identificar el backend.** Dues finestres d'OpenCode no necessàriament utilitzen el mateix servidor o sessió. Una aplicació d'escriptori connectada a un altre servidor és un entorn d'execució diferent, encara que l'etiqueta del model sembli familiar.

## Punts clau

- **Utilitza CLI per al treball de terminal** i les ordres no interactives.
- **Utilitza Desktop per a un espai gràfic**, comprovant el servidor seleccionat.
- **La configuració del proveïdor determina la inferència**, independentment de la interfície.
- **La mateixa identitat de producte no garanteix el mateix estat de sessió** entre servidors o versions separats.

**Abast i data:** Documentació oficial comprovada el 6 d'octubre de 2026. Aquesta guia compara interfícies, no la qualitat dels models. Necessites un repositori, una connexió de proveïdor funcional i coneixements bàsics de terminal. Reserva 45 a 60 minuts per a la prova.

## El client i el servidor

**OpenCode separa la interfície del servidor.** La [documentació del servidor](https://opencode.ai/docs/server/) descriu la UI de terminal com un client i `opencode serve` com un servidor independent. Aquesta arquitectura admet diverses maneres d'interactuar amb l'agent.

**Desktop inicia un servidor local per defecte.** La [guia de resolució de problemes](https://opencode.ai/docs/troubleshooting/) identifica el sidecar `opencode-cli` i l'opció de connectar-se a un URL de servidor configurat. Quan els clients es comportin diferent, inspecciona aquesta connexió abans de canviar el prompt.

| Capa | Pregunta que cal respondre |
|---|---|
| **Client** | UI de terminal, aplicació d'escriptori o ordre no interactiva? |
| **Servidor de l'agent** | Quin procés rep la petició? |
| **Repositori** | A quin directori accedeix el servidor? |
| **Proveïdor del model** | Quin servei proporciona la inferència? |
| **Sessió** | Conversa existent o tasca nova? |

**La ubicació del servidor no és la ubicació de la inferència.** Un servidor d'agent al teu ordinador encara envia peticions a un model allotjat configurat. En canvi, un servei local compatible d'inferència és un procés separat amb el seu propi model i requisits de recursos.

La referència oficial del servidor indica `127.0.0.1` com a nom d'amfitrió predeterminat per a `opencode serve`. Mantén el servei al loopback durant una prova local:

```bash
opencode serve --hostname 127.0.0.1
```

Utilitza una adreça d'enllaç més àmplia només després de definir l'autenticació, les regles del tallafoc i els camins del repositori exposats al servidor.

{{< figure src="opencode-clients-server-provider.webp" alt="Clients de terminal i d'escriptori connectats a un servidor d'agent, fitxers del repositori i un servei d'inferència separat" caption="Comprova per separat el servidor de l'agent i el proveïdor d'inferència" >}}

## Interacció de terminal i automatització

```bash
opencode
```

**L'ordre predeterminada obre la UI de terminal.** La [referència CLI](https://opencode.ai/docs/cli/) també documenta ordres programàtiques. Comença al repositori previst i confirma l'agent i el model seleccionats abans de demanar canvis.

```bash
opencode run "Identify this project's test command. Do not modify files."
```

**Utilitza `opencode run` per a una petició no interactiva acotada.** Estableix la política de permisos adequada per separat. Un prompt que demana no fer canvis orienta, però no imposa l'aïllament del sistema de fitxers.

**Tria aquest flux quan importi combinar ordres del shell.** Un embolcall repetible ha de capturar la petició, l'estat de sortida, la sortida rellevant i els fitxers canviats. Fes explícit el tractament dels errors. Un diff buit i un missatge d'èxit requereixen una interpretació diferent d'una correcció verificada.

## Configuració i compatibilitat de Desktop

**Utilitza la pàgina oficial de baixada per a la versió prevista.** La [pàgina de baixada d'OpenCode](https://opencode.ai/download) enumera paquets de terminal i d'escriptori. En aquesta comprovació, la pàgina anuncia paquets de terminal v2, mentre que la documentació general també conté exemples d'instal·lació antics. Registra les versions exactes del client i del backend i no barregis instruccions de canals de versions diferents.

**Avalua la interacció d'escriptori amb una tasca real petita.** Obre un projecte, confirma el servidor, envia una petició acotada, inspecciona els fitxers canviats i demana una correcció. Valora l'esforç necessari per entendre les accions de l'agent. No assumeixis que un client gràfic substitueix completament l'editor i el depurador.

| Prova d'escriptori | Evidència esperada |
|---|---|
| **Selecció del projecte** | L'agent identifica el repositori previst |
| **Selecció del model** | El proveïdor i el model coincideixen amb el registre de prova |
| **Execució d'ordres** | El runtime i les proves necessàries estan disponibles |
| **Inspecció del canvi** | El pedaç complet és fàcil de trobar i revisar |
| **Reinici** | El projecte i la sessió previstos continuen identificables |

## Configuració i accés al model

**OpenCode combina configuració de diverses ubicacions.** La [referència de configuració](https://opencode.ai/docs/config/) explica la precedència i la conservació dels paràmetres no conflictius. Compara el model, l'agent i els permisos efectius, no només un fitxer de projecte.

**L'accés al proveïdor forma part de la configuració d'execució.** La [guia de proveïdors](https://opencode.ai/docs/providers/) descriu serveis admesos i endpoints compatibles. Importen les credencials, l'accessibilitat de l'endpoint i el suport d'eines del model. Un servidor que funciona en un altre lloc necessita el seu propi accés vàlid al proveïdor i al repositori.

**El client no fixa el cost total d'inferència.** Compara l'ús facturat amb models i tasques equivalents. Inclou les execucions repetides causades per errors de configuració. Si utilitzes inferència local, registra la memòria del sistema, el format del model, la mida del context i la configuració del runtime. No presentis una baixada d'escriptori com una substitució gratuïta del càlcul allotjat.

## Sessions i canvi segur

**Verifica la continuïtat en lloc d'assumir-la.** Registra el projecte i la sessió actius abans de canviar de client. Comprova que el destí connecta amb el servidor previst i mostra l'historial previst. Si inicies una sessió nova, dona un traspàs concís amb l'objectiu, la feina completada i les comprovacions pendents.

**Evita canvis simultanis al mateix checkout.** Dues converses amb plans diferents comparteixen fitxers quan apunten al mateix directori. Utilitza worktrees o checkouts separats per a experiments independents. Revisa els canvis abans d'integrar-los.

```text
Handover record
Goal:
Current branch and working directory:
Files changed:
Checks already completed:
Known failures:
Next approved action:
```

**Aquest registre fa que el traspàs sigui inspeccionable.** També ajuda a distingir un problema d'interfície d'una instrucció absent o d'un desajust de l'entorn. Mantén les credencials fora del registre.

## Accés al servidor i permisos

**Tracta el servidor de l'agent com un servei d'execució.** La documentació del servidor descriu l'autenticació opcional mitjançant `OPENCODE_SERVER_PASSWORD`. Configura l'accés intencionadament abans de connectar equips. Un servidor d'agent accessible no equival a un lloc web estàtic inofensiu.

**Revisa els permisos de les eines per separat.** La [guia de permisos](https://opencode.ai/docs/permissions/) defineix el comportament allow, ask i deny. Aplica la mateixa política durant la prova de la interfície. No consideris més segur o capaç un client amb menys avisos sense comprovar les regles efectives.

**Comença amb una prova de política innòcua.** Demana una inspecció permesa i una edició prohibida en un projecte d'un sol ús. Verifica el comportament observat i després passa a una implementació acotada. Això fa que la hipòtesi dels permisos sigui comprovable.

## Resolució de problemes i elecció

| Símptoma | Primera inspecció |
|---|---|
| **Error de connexió de Desktop** | Servidor seleccionat i estat del sidecar local |
| **Falta el model en un client** | Versió del servidor, accés al proveïdor i configuració |
| **Resultat de prova diferent** | Directori del projecte i entorn d'execució |
| **Conversa absent** | Identitat del servidor i de la sessió |
| **Funciona fins que es carrega un connector** | Configuració del connector i compatibilitat de la versió |

**Tria el terminal** si les peticions amb scripts i el context del shell faciliten la feina. **Tria Desktop** si la navegació gràfica del projecte millora la supervisió. Mantén les decisions sobre el proveïdor i la política separades d'aquesta preferència.

**Passos següents:** Compara alternatives de terminal al [resum de CLI](/articles/cli-coding-agents-comparison/). Per als requisits d'inferència local, llegeix la [guia d'OpenCode i Strata](/articles/strata-opencode-local-coding-agent-16gb/). Per a alternatives gràfiques, utilitza el [resum de GUI](/articles/gui-coding-agents-comparison/).
