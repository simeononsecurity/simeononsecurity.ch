---
title: "10 connectors, habilitats i eines MCP de Claude Code: guia pràctica"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Tria extensions de Claude Code per planificar, revisar codi, gestionar coneixement, dissenyar i automatitzar. Compara deu eines, dependències i comprovacions pràctiques."
genre: ["Intel·ligència artificial", "Eines per a desenvolupadors", "Desenvolupament de programari"]
tags: ["connectors de Claude Code", "habilitats de Claude Code", "eines MCP", "Graphify", "grill-me", "grill-with-docs", "grill-me-codex", "Claudex Loop", "connector Codex", "revisió de codi", "claude-obsidian", "Obsidian", "CLAUDE.md", "guies de Karpathy", "Impeccable", "Higgsfield", "NotebookLM", "notebooklm-py", "n8n MCP", "flux de desenvolupament d'IA", "instruccions d'agent", "grafs de coneixement"]
cover: "/img/cover/claude-code-plugins-workflow-management-tools.webp"
coverAlt: "Icones d'eines blaves i morades, carpetes i panells de gràfics abstractes connectats a un eix geomètric central sobre un fons fosc"
coverCaption: "Il·lustració conceptual del flux de treball. Les formes del gràfic no representen resultats mesurats."
---

**Tria una extensió de Claude Code al voltant d'un problema concret del teu flux de treball.** Els requisits poc clars necessiten una conversa de planificació. Els defectes no detectats necessiten revisió i proves. La recerca repetida necessita fonts traçables. Instal·lar més eines només ajuda quan les responsabilitats són clares.

Aquesta guia compara **deu projectes** per a aquestes tasques, amb exemples de configuració i un exercici d'avaluació. L'anàlisi es basa en la documentació actual dels projectes i en el vídeo proporcionat de Chase AI. Les recomanacions són judicis editorials, no mesures de rendiment pràctiques ni proves d'un augment de productivitat de deu vegades.

<!--more-->

## Punts clau

- **Tria segons el resultat:** un pla revisat, un mapa de codi i una imatge generada necessiten eines diferents.
- **Separa les capes d'instal·lació:** les instruccions, els programes executables, els connectors i les connexions de servei tenen dependències diferents.
- **Comprova els noms actuals:** Graphify i grill-me-codex ara tenen ubicacions de repositori canòniques diferents.
- **Verifica més enllà de l'acord:** que dos models acceptin un pla no demostra una implementació correcta.
- **Mesura el treball acceptat:** inclou la configuració, l'ús del servei, els intents fallits i les correccions humanes.

## Abans de començar

**Requisits previs:** una instal·lació funcional de Claude Code, un projecte o branca d'un sol ús i permís per usar els serveis externs seleccionats. Els exemples de CLI assumeixen un terminal i el gestor de paquets indicat. Les integracions al núvol necessiten els seus propis comptes i autenticació.

**Temps estimat:** 15 minuts de lectura i de 30 a 60 minuts per a una prova acotada. **Dificultat:** intermèdia per a la configuració de CLI i la integració de serveis. Llegir les habilitats d'instruccions necessita menys configuració.

**Documentació comprovada el 10 d'octubre de 2026.** Les ordres i les regles d'accés reflecteixen les fonts enllaçades. Torna a comprovar la versió instal·lada abans de seguir un tutorial antic. Aquest article se centra en extensions usades des de Claude Code, amb les diferències de l'amfitrió indicades quan cal.

**Verifica per capes després de la instal·lació.** Comprova per separat els fitxers, la detecció de l'amfitrió, les dependències executables, les credencials i una tasca representativa. Un instal·lador correcte no demostra que funcionin el navegador, el servidor MCP, l'eina multimèdia o el compte extern. Fes la primera prova amb dades sintètiques i registra la revisió aigües amunt.

## Coneix el tipus d'extensió

| Tipus | Funció | Exemple |
|---|---|---|
| **Fitxer d'instruccions** | Fixa expectatives persistents del projecte | CLAUDE.md |
| **Habilitat** | Proporciona un procediment per a una tasca | grill-me |
| **Connector** | Empaqueta ordres registrades i integracions | Connector Codex |
| **CLI** | Executa ordres des d'un terminal | Graphify |
| **Servidor MCP** | Exposa eines invocables a un client d'agent | Integració n8n |

El **Model Context Protocol (MCP)** connecta una aplicació d'agent amb eines i dades exposades per un servidor. Una **interfície de línia d'ordres (CLI)** executa ordres. Una habilitat sol ensenyar a l'agent a usar una interfície, però la seva presència no demostra una connexió funcional.

**Comença per la capacitat que falta.** Si el teu agent ja té cerca al repositori, un procediment de cerca nou necessita un benefici observable. Si l'agent no té accés a una plataforma d'automatització, un fitxer d'instruccions per si sol no proporciona accés autenticat. La [guia de l'entorn d'agents](/articles/best-ai-agent-harnesses/) explica el programari que envolta les crides al model i l'execució d'eines.

## Tria la primera eina

| Problema | Eina | Primera comprovació d'acceptació |
|---|---|---|
| **Requisits ambigus** | grill-me / grill-with-docs | Decisions i criteris d'acceptació explícits |
| **Deriva d'abast repetida** | CLAUDE.md inspirat en Karpathy | Cada canvi serveix el canvi sol·licitat |
| **Pla d'implementació arriscat** | Claudex Loop | Resultats de revisió resolts amb proves |
| **Canvis de codi sense revisar** | Connector OpenAI Codex | Resultats vinculats al codi i als casos de fallada |
| **Repositori desconegut** | Graphify | Relacions coherents amb els fitxers font |
| **Coneixement dispers del projecte** | claude-obsidian | Reclamacions amb enllaços a l'evidència original |
| **Síntesi repetida de fonts** | notebooklm-py | Respostes amb cites de les fonts previstes |
| **Interfície confusa** | Impeccable | Els usuaris completen la interacció prevista |
| **Recursos visuals absents** | Higgsfield | El resultat encaixa amb el briefing aprovat |
| **Flux de servei repetible** | n8n MCP | L'execució de prova produeix el resultat esperat |

**Inici recomanat:** tria una fila i desa una tasca de referència abans d'instal·lar. Afegeix una segona eina només quan aporti una contribució separada i mesurable.

## Aclareix la feina

### grill-me i grill-with-docs

**Les habilitats de Matt Pocock** ajuden a convertir una idea poc especificada en decisions. El [punt d'entrada actual de grill-me](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) invoca l'habilitat compartida de grilling. [grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) invoca grilling i modelatge de domini. La [documentació de la col·lecció](https://github.com/mattpocock/skills) descriu la terminologia compartida i els registres de decisions d'arquitectura.

**Usa la variant amb documentació** quan els termes de negoci afectin la implementació. En un importador CSV il·lustratiu, decideix si un client existent vol dir el mateix correu, el mateix identificador extern o tots dos. Registra la definició abans d'escriure la detecció de duplicats.

**Mantén l'entrevista proporcional.** Una sessió útil resol incerteses materials. No ha de demanar-te repetir respostes ja presents al repositori. Acaba amb un pla, preguntes obertes i comprovacions observables de finalització.

### CLAUDE.md inspirat en Karpathy

**Les guies mantingudes per Multica** converteixen les observacions de Karpathy en quatre temes: supòsits explícits, solucions senzilles, canvis centrats i objectius verificables. El [repositori](https://github.com/multica-ai/andrej-karpathy-skills) és una implementació comunitària inspirada en les seves observacions. Dir que és un connector mantingut personalment per Karpathy descriuria malament el seu origen.

**Integra les guies útils amb la política actual del projecte.** Conserva les ordres de construcció, les convencions de contingut i les restriccions de desplegament. Un fitxer de substitució que les elimini crea noves fonts d'errors.

**Exemple de regla:** exigeix que un canvi de l'importador conservi el tractament actual de duplicats i expliqui qualsevol canvi intencionat amb un fixture. Això converteix una preferència general per la cautela en una comprovació clara per al revisor. Les instruccions expressen expectatives. Les proves i els controls d'execució aporten evidència separada.

| Artefacte de planificació | Objectiu |
|---|---|
| **Requisit** | Anomena el resultat visible per a l'usuari |
| **Entrada del glossari** | Dona un significat a un terme ambigu |
| **Registre de decisió** | Conserva el motiu d'una elecció important |
| **Comprovació d'acceptació** | Estableix com s'avaluarà la finalització |

## Revisa plans i codi

### grill-me-codex, ara Claudex Loop

**Claudex Loop** és la destinació actual del repositori original grill-me-codex. La seva [documentació](https://github.com/chaseai-yt/claudex-loop) descriu el reconeixement del repositori, els requisits, la revisió de l'altre proveïdor, la implementació i la inspecció independent. El circuit complet necessita les dues CLI i Python 3.10 o posterior.

**Usa Claudex Loop per a plans importants** amb supòsits que cal desafiar abans d'implementar. El flux actual admet començar des de Claude Code o Codex. Registra resultats i disposicions, i separa el permís per revisar del permís per construir. La descripció antiga del vídeo amb cinc rondes no substitueix el pressupost actual del flux instal·lat.

**Demana proves amb cada objecció.** En el CSV, la revisió ha d'identificar un duplicat concret o un cas de reintent i el comportament esperat. L'acord dels models és un resultat de revisió, no una prova. Conserva les troballes obertes quan s'acabi el pressupost.

### Connector OpenAI Codex

```text
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

**El connector Codex d'OpenAI per a Claude Code** afegeix revisió de codi i delegació de tasques dins de Claude Code. Són ordres de Claude Code, no ordres shell. El [repositori oficial](https://github.com/openai/codex-plugin-cc) documenta Node.js 18.18 o posterior i accés autenticat a Codex mitjançant ChatGPT o una clau d'OpenAI API.

```text
/codex:review --background
/codex:status
/codex:result
```

**Usa la revisió normal** per als canvis actuals o una comparació de branca. Usa **`/codex:adversarial-review`** per a un repte focalitzat. Ordres de delegació com **`/codex:rescue`** fan una tasca diferent de la revisió de només lectura, així que especifica l'autoritat prevista.

**Pressuposta l'ús de Codex per separat.** El projecte inclou ChatGPT Free entre els comptes admesos, però els límits d'ús continuen aplicant-se. Instal·lar el connector no crea accés il·limitat.

**Regla de selecció:** usa una revisió acotada del connector per a un pedaç existent. Tria el circuit gran quan els requisits i la revisió del pla necessitin el seu propi procés registrat.

## Conserva el context útil

### Graphify

```bash
uv tool install graphifyy
graphify install --project
graphify extract . --code-only
graphify query "show the authentication flow"
```

**Graphify** converteix les relacions del repositori en un graf de coneixement consultable. El seu [repositori canònic](https://github.com/Graphify-Labs/graphify) ara és sota Graphify-Labs. El nom del paquet és **`graphifyy`**, amb dues y finals. L'executable continua sent **`graphify`**.

**L'extracció code-only** usa parsing local d'arbres de sintaxi abstracta per llegir l'estructura del codi. La interpretació de documents i multimèdia usa un altre camí basat en models. No ampliïs les afirmacions de privacitat o cost local a tots els modes.

**Els hooks opcionals** reconstrueixen el graf després de commits i canvis de branca. Després d'un pull o merge, el flux documentat demana **`graphify update .`**. Els canvis de documentació necessiten una actualització pròpia. L'exportació d'Obsidian ofereix una altra vista del graf.

**Usa Graphify per a preguntes de relacions** i després inspecciona el codi corresponent. El graf ajuda a seleccionar fitxers. La seva estructura no demostra comportament d'execució ni substitueix les proves. Mesura l'estalvi de tokens amb les teves preguntes, incloent-hi construcció i manteniment del graf.

### claude-obsidian

**claude-obsidian** organitza materials font en pàgines d'Obsidian enllaçades i citades. El [repositori](https://github.com/AgriciDaniel/claude-obsidian) descriu ingestió, recuperació, manteniment del coneixement, conservació de fonts i registres de suport o contradicció. El vault continua sent un conjunt normal de fitxers locals.

**Usa claude-obsidian per al coneixement durador del projecte:** decisions de disseny, documents font i notes de recerca que han de sobreviure a converses individuals. El resultat útil és un registre mantenible amb procedència, és a dir, un origen traçable per a cada afirmació important.

**Revisa el vault després de la ingestió.** Tria algunes afirmacions i segueix les cites fins al material original. Conserva les proves contradictòries en lloc d'unificar-les en un resum segur. L'emmagatzematge local per si sol no demostra inferència local. Comprova l'amfitrió i la configuració del model abans de donar documents sensibles.

| Sistema de context | Primera pregunta |
|---|---|
| **Graphify** | Quins components font estan connectats? |
| **claude-obsidian** | Quina evidència conservada recolza aquesta decisió? |
| **notebooklm-py** | Què diuen les fonts de recerca seleccionades? |

### notebooklm-py

```bash
uv tool install "notebooklm-py[browser]"
notebooklm login
notebooklm auth check --test --json
notebooklm skill install
```

**notebooklm-py** ofereix una biblioteca Python, una CLI i una habilitat d'agent per al servei de recerca notebook de Google. El [projecte](https://github.com/teng-lin/notebooklm-py) documenta importació de fonts, preguntes fonamentades, artefactes generats i baixades per lots. L'extra browser admet l'inici de sessió interactiu.

**És una integració no oficial.** La biblioteca depèn d'interfícies de Google no documentades i queda exposada a canvis i límits de taxa. No la presentis com una API pública compatible amb Google.

**Usa notebooklm-py per a un corpus acotat**, com notes de versió i guies de migració d'una dependència. Comprova les cites amb el text font abans d'incorporar els resultats a un pla. Protegeix l'estat d'autenticació desat com a material d'accés al compte.

**Externalitzar recerca canvia on s'executa la feina.** No elimina tokens d'orquestració, quotes del servei, esforç de revisió ni obligacions de tractament de dades. Tracta l'estalvi de tokens com una mesura a recollir, no com una propietat automàtica de la instal·lació.

## Dissenya i genera recursos

### Impeccable

```text
/impeccable critique settings
/impeccable audit settings
/impeccable polish settings
```

**Impeccable** ofereix un vocabulari de disseny per a la feina d'interfícies. La seva [documentació](https://github.com/pbakaus/impeccable) cobreix crítica, disposició, tipografia, accessibilitat, moviment i iteració visual al navegador. Els exemples assumeixen una habilitat instal·lada i un projecte amb una superfície de configuració.

**Comença per un problema d'interacció.** Per a l'importador, pregunta per què els usuaris no veuen errors de validació o entenen malament l'opció de duplicats. Revisa els canvis proposats abans d'aplicar un poliment visual. Un espaiat atractiu no resol una acció ambigua.

**La iteració en directe** ajuda a comparar alternatives al navegador. Verifica la navegació amb teclat, la disposició mòbil, els missatges d'error i el contrast. El nombre d'ordres varia entre versions, així que usa la llista de la versió instal·lada i no el recompte del vídeo.

### Higgsfield

**La integració MCP de Higgsfield** connecta agents al seu servei de generació d'imatges i vídeo. La [pàgina d'integració oficial](https://higgsfield.ai/mcp) llista opcions de connexió de Claude Code i CLI. Usa el flux actual per al teu compte i la interfície triada.

**Tria Higgsfield quan falta un lliurable multimèdia.** Per a una pàgina de producte il·lustrativa, especifica proporció, composició, restriccions de marca i ubicació abans de generar variants. Mantén el briefing visual separat de la implementació de la pàgina.

**Comprova primer l'accés i el consum del servei.** Una llista d'integració no demostra accés a tots els models, generació il·limitada ni un dret d'ús comercial concret. Revisa els termes del compte i el model seleccionat abans d'adoptar un flux de producció.

**Revisa el fitxer final** a la mida prevista. Comprova el text visible, els símbols no desitjats, el retall i la coherència amb el producte. Les pantalles i diagrames generats no són proves d'un test correcte.

| Lliurable de disseny | Evidència de finalització |
|---|---|
| **Revisió d'interfície** | Les accions necessàries funcionen en les finestres objectiu |
| **Recurs d'imatge** | Dimensions, retall i contingut coincideixen amb el briefing |
| **Recurs de vídeo** | Temps, moviment i exportació final coincideixen amb el briefing |

## Connecta fluxos repetibles

### n8n MCP

**El servidor MCP integrat de n8n** exposa operacions de flux a clients connectats. La [documentació de connexió actual](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) cobreix instàncies Cloud i autogestionades. La construcció i edició de fluxos es documenta des de n8n 2.13.0. Aquest article es refereix al servidor propi de n8n, no a un paquet comunitari amb un nom semblant.

**Usa accés a nivell d'instància** per a aquesta integració. El node MCP Server Trigger té un abast diferent: exposa eines d'un únic flux. Comprova la [referència d'eines](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference) amb la teva versió desplegada.

**Activa l'accés deliberadament.** Els fluxos existents necessiten exposició MCP per a accés complet. Les previsualitzacions de cerca tenen més visibilitat dins dels permisos existents de l'usuari. L'exposició no és una llista d'autorització per client, encara que els permisos del client també governen les operacions.

**Inspecciona el mode d'execució.** El **`execute_workflow`** documentat executa per defecte la versió de producció publicada. El mode manual executa la versió actual no publicada. Verifica les entrades i les accions posteriors abans d'executar.

**Primera prova útil:** classifica sol·licituds de suport sintètiques i escriu els resultats en una destinació de prova. Confirma el tractament de camps absents i reintents. L'autogestió encara necessita còmput, manteniment i serveis posteriors de pagament.

## Executa una prova controlada

**Exercici il·lustratiu:** afegeix un importador CSV a una aplicació petita. L'importador previsualitza files, informa de camps de correu invàlids i impedeix duplicats. No calen registres de clients ni destinacions externes actives.

```yaml
# Evaluation worksheet, not a tool configuration file
task: "add CSV import preview"
inputs:
  - "valid rows"
  - "invalid email field"
  - "repeated customer identifier"
  - "same import submitted twice"
acceptance:
  - "preview creates no records"
  - "invalid rows receive useful messages"
  - "duplicate policy matches the written requirement"
  - "repeat submission creates no extra records"
record:
  - "source revision and selected skill version"
  - "model and service configuration"
  - "elapsed time and billed usage"
  - "failed checks and human corrections"
```

**Estableix primer la referència.** Desa la revisió inicial i demana a l'agent que completi la tasca amb el flux existent. Executa comprovacions independents i conserva el resultat. Repeteix des de la mateixa revisió amb una sola extensió i els mateixos requisits.

**Ajusta l'experiment al problema sospitat.** Si els duplicats es malinterpreten sovint, prova una habilitat de requisits. Si l'agent omet un validador existent, prova el mapa del repositori. Si els usuaris no veuen errors, prova la crítica d'interfície. Carregar les deu eines alhora impedeix atribuir cap millora.

**Raonament esperat:** un segon intent correcte és una evidència útil, però una execució no demostra un multiplicador general de productivitat. Les execucions repetides separen el valor de l'eina de la variabilitat del model. Compara resultats acceptats, esforç de revisió i intents fallits.

| Observació | Interpretació |
|---|---|
| **Resposta més ràpida, proves fallides** | Menys temps de resposta sense completar la tasca |
| **Execució més llarga, menys correccions** | Possible benefici en l'esforç total d'entrega |
| **Dos revisors d'acord** | Acord que necessita verificació independent |
| **Menys ús de l'agent, càrrecs nous** | El cost s'ha mogut entre proveïdors |

**Crea un registre de decisió conservat.** Anomena el problema, l'eina triada, el benefici observat, el problema pendent i les condicions per repetir la prova. Conserva una eina quan la seva contribució superi aquesta comprovació. Una gran col·lecció instal·lada no exigeix un gran flux actiu.

## Resolució de problemes

| Símptoma | Comprovació següent |
|---|---|
| **L'habilitat existeix però l'ordre falla** | Instal·lació de l'executable, PATH i fitxers auxiliars |
| **Falten ordres amb noms del tutorial antic** | Versió instal·lada i instruccions canòniques |
| **El graf no inclou canvis recents** | Frescor del graf i actualització documental separada |
| **El revisor repeteix objeccions resoltes** | Revisió exacta del pla, proves i pressupost |
| **Falla l'autenticació de Notebook** | Diagnòstic, validesa de sessió i incidències aigües amunt |
| **La connexió n8n no té operacions previstes** | Versió desplegada, exposició i permisos atorgats |
| **El disseny sembla millor però funciona pitjor** | Criteris d'acceptació originals i comprovacions d'interacció |

**Comprova les capes d'instal·lació en ordre:** fitxers presents, detecció de l'amfitrió, dependències preparades, autenticació i tasca representativa verificada. Un instal·lador correcte només estableix una part de la cadena.

**Inspecciona les habilitats superposades abans d'afegir-ne una altra.** Les entrevistes de requisits, les suites de planificació, les eines de disseny i els paquets de revisió poden tenir valors per defecte en conflicte. Tria un procediment principal i afegeix eines de suport per a contribucions concretes. Conserva la política del repositori i l'abast sol·licitat.

## Vídeo de demostració

{{< youtube id="IShdbDP4Jgg" enable="true" title="The Top 10 Claude Code Plugins to 10x Your Next Project (June '26)" >}}

**El recorregut de Chase AI** presenta els deu projectes tractats. [Mira el vídeo original](https://www.youtube.com/watch?v=IShdbDP4Jgg) per veure les demostracions. Usa la documentació enllaçada per a la instal·lació i el comportament actuals. El títol del vídeo és promocional, no un resultat mesurat establert per aquesta guia.

## Passos següents

**Tria un error recurrent i una prova d'acceptació.** Prova l'extensió corresponent en un projecte d'un sol ús i conserva la combinació més petita que millori el resultat. Afegeix gestió del coneixement, generació multimèdia o automatització només quan la feina necessiti aquests resultats.

**Per a orientació relacionada**, llegeix la [comparació d'agents de codi CLI](/articles/cli-coding-agents-comparison/) en triar l'agent. Usa el [curs de col·laboració amb IA](/ai-collaboration-course-start/) per treballar requisits, proves i responsabilitats de revisió.

{{< centerbutton href="/ai-collaboration-course-start/" >}}
Llegeix el curs de col·laboració amb IA
{{< /centerbutton >}}

## Referències

- [Graphify: gràfics de codi i instal·lació](https://github.com/Graphify-Labs/graphify)
- [Matt Pocock: col·lecció d'habilitats](https://github.com/mattpocock/skills)
- [Claudex Loop: projecte grill-me-codex actual](https://github.com/chaseai-yt/claudex-loop)
- [OpenAI: connector Codex per a Claude Code](https://github.com/openai/codex-plugin-cc)
- [claude-obsidian: gestió de coneixement vinculada a fonts](https://github.com/AgriciDaniel/claude-obsidian)
- [Multica: guies de codi inspirades en Karpathy](https://github.com/multica-ai/andrej-karpathy-skills)
- [Impeccable: ordres de disseny i instal·lació](https://github.com/pbakaus/impeccable)
- [Higgsfield: integració d'agent](https://higgsfield.ai/mcp)
- [notebooklm-py: biblioteca, CLI i habilitat no oficials](https://github.com/teng-lin/notebooklm-py)
- [n8n: guia oficial de connexió MCP](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)
