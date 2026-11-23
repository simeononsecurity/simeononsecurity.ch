---
title: "Una font, moltes eines: un marc de col·laboració amb IA per a equips mixtos"
date: 2026-10-01
lastmod: 2026-11-23
toc: true
draft: false
description: "Crea un sistema compartit de col·laboració amb IA, amb responsables de les fonts, versions de context, revisió duradora dels canvis i criteris clars per triar entre mapes de projecte i RAG."
genre: ["Intel·ligència artificial", "Gestió del coneixement", "Enginyeria de programari", "Col·laboració d'equip"]
tags: ["marc de col·laboració amb IA", "equips mixtos", "font de veritat", "agents d'IA", "AGENTS.md", "CLAUDE.md", "regles de Cline", "Claude Code", "Codex", "ChatGPT", "Copilot", "Cowork", "generació augmentada amb recuperació", "RAG", "Model Context Protocol", "mapa de projecte", "manifest de context", "gestió del coneixement", "deriva de la documentació", "aprovació humana", "registre de decisions", "relleu entre agents", "versionament de polítiques", "worktrees de Git", "controls per a pull requests"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Il·lustració de professionals que col·laboren en tasques de ciberseguretat"
coverCaption: ""
---

**Dues persones fan la mateixa pregunta a dues eines d'IA:** quant de temps ha de conservar el servei una exportació? En aquest exemple il·lustratiu, l'agent d'IDE del desenvolupador respon set dies basant-se en un README. L'assistent de xat del responsable d'operacions respon trenta dies basant-se en una pàgina wiki. Totes dues respostes semblen segures. Cada eina ha llegit una còpia diferent de la veritat.

**La fallada és de responsabilitat,** no de qualitat del prompt. El requisit del wiki va canviar la setmana passada, però ningú no va actualitzar el README. El desenvolupador demana a l'agent que corregeixi la tasca de retenció. L'agent segueix el document antic i crea un pedaç polit que restaura el comportament incorrecte. Els revisors inspeccionen el codi sense veure la versió del requisit que fonamenta la resposta.

**Assigneu una font a cada fet.** Feu que totes les eines llegeixin d'aquesta font i canalitzeu cada canvi durador a través d'una persona. El repositori, el wiki i el gestor de tasques tenen funcions diferents. Necessiten autoritat explícita, responsables identificats i un procediment compartit per traslladar informació entre ells.

**Aquesta guia ofereix un model que podeu aplicar aquesta setmana,** amb generació augmentada amb recuperació o sense. Comenceu amb un mapa de projecte, instruccions versionades, registres d'evidències i propostes revisades. Afegiu infraestructura de cerca només quan el problema de recuperació ho justifiqui.

**El primer lliurable ha de ser un registre de fonts,** no pas un connector. Enumereu cada tipus de fet, la seva font autoritativa, el responsable, la revisió actual i qui n'aprova els canvis.

## Idees clau

- **Assigneu autoritat segons el tipus d'informació,** sense forçar-ho tot dins d'una aplicació.
- **Tracteu la memòria i els índexs de recuperació com a memòries cau,** mai com a fonts de polítiques independents.
- **Adjunteu les versions de les fonts a les propostes,** perquè els revisors sàpiguen quins fets fonamenten el canvi.
- **Exigiu l'aprovació fora dels prompts,** mitjançant controls d'accés i passos de revisió obligatoris.
- **Compartiu el procediment entre eines,** adaptant-ne la presentació a cada interfície.

## Abans de començar

**Requisits previs:** trieu un projecte pilot amb un repositori, un wiki o un sistema documental, un gestor de tasques i responsables disposats a revisar canvis. Si l'equip no té wiki, pot fer servir un dipòsit de documents versionat. Manteniu el model de responsabilitat.

**Temps estimat:** reserveu de dues a quatre hores per al mapa i les plantilles inicials, seguides d'una setmana de prova. **Dificultat:** moderada. El més difícil és acordar l'autoritat, no pas instal·lar una altra eina d'IA.

**Abast:** aquest és un model operatiu proposat per a equips. Les seves regles d'aprovació i convencions de noms són recomanacions, no comportaments predeterminats garantits per Claude Code, Codex, Cline, Cowork, Copilot o ChatGPT. La taula de continguts automàtica de dalt enllaça cada pas d'implementació.

## Eines mixtes, contextos diferents

**Programadors i no programadors comparteixen un projecte,** però s'hi acosten amb interfícies diferents. Un desenvolupador utilitza un agent d'IDE o de terminal. Un responsable de producte utilitza un projecte de xat. Un responsable d'operacions treballa amb un wiki i un gestor de tasques. Trieu les interfícies segons la tasca, no segons l'accés als fets autoritatius.

**El context és el material disponible per a la resposta actual.** Inspeccioneu cada sessió per trobar fitxers del repositori, documents penjats, historial del xat, memòria desada, resultats de connectors i fragments recuperats. Dues sessions amb evidències diferents no han de coincidir, encara que les preguntes siguin iguals.

| Problema | Què hi veieu |
|---|---|
| **Deriva de la documentació** | Un README repeteix un requisit obsolet |
| **Promoció del resum** | Un resum de sessió esdevé evidència sense la font original |
| **Escriptures solapades** | Dos agents substitueixen la mateixa pàgina des de versions base diferents |
| **Decisions perdudes** | Un acord de reunió no arriba mai al registre de decisions |
| **Manca de procedència** | Una resposta plausible no indica la versió de la pàgina o el commit |

**L'exemple de retenció mostra la diferència.** El wiki descriu el comportament objectiu aprovat. El codi descriu el comportament implementat. Cap dels dos no hauria de reescriure l'altre d'amagat. Registreu el desacord i demaneu al responsable designat si cal revisar la implementació o el requisit.

> **Idea clau:** definiu l'autoritat abans d'escollir una eina d'IA. Comenceu pels termes següents.

### Barra lateral: cinc termes compartits

| Terme | Significat en aquest marc |
|---|---|
| **Font** | Registre autoritatiu designat per a un tipus d'informació |
| **Memòria cau** | Còpia derivada per guanyar velocitat o comoditat |
| **Proposta** | Canvi suggerit que espera l'aprovació del responsable |
| **Mapa de projecte** | Índex de les ubicacions de les fonts, identificadors i responsables |
| **Manifest** | Registre de les evidències exactes utilitzades en una resposta o proposta |

## Assigneu una font a cada fet

**Una sola font vol dir una autoritat per a cada fet,** no una única base de dades per a tota l'organització. Definiu aquesta distribució durant la prova pilot. Substituïu els rols d'exemple pels responsables reals de l'equip.

| Tipus d'informació | Sistema d'origen | Responsable | Qui escriu | Com ho llegeixen els agents |
|---|---|---|---|---|
| **Codi, proves, configuració, esquemes** | Repositori | Mantenidor d'enginyeria | Col·laboradors mitjançant PR revisades | Fitxers d'un commit registrat |
| **Documents publicats i ADR** | Repositori | Responsable tècnic | Col·laboradors mitjançant la mateixa PR | Fitxers versionats |
| **Requisits** | Wiki | Responsable de producte | Responsable o editor autoritzat | ID i revisió de la pàgina |
| **Runbooks** | Wiki | Responsable d'operacions | Editor autoritzat | ID i revisió de la pàgina |
| **Política** | Wiki | Responsable de polítiques | Editor autoritzat després de la revisió | Pàgina canònica i adaptador local |
| **Decisions entre equips** | Registre de decisions del wiki | Responsable de decisió designat | Responsable després de l'aprovació | ID i estat de la decisió |
| **Tasques i troballes** | Gestor de tasques | Responsable de la tasca | Persones o canal d'entrada autoritzat de propostes | Clau i revisió de l'issue |
| **Xats, resums, embeddings** | Només memòria cau | Responsable de sessió o índex | Eines i participants | Només referència, seguida de comprovacions de font |

**Un registre de decisió d'arquitectura (ADR)** pertany al costat del codi quan governa el disseny del repositori. Una decisió entre equips pertany al registre compartit. Enllaceu els dos registres quan una decisió abasti tots dos àmbits. No mantingueu còpies independents de l'estat d'aprovació.

**Les còpies locals de les polítiques estan subordinades a la pàgina canònica.** En canvi, les proves i els esquemes del repositori són fonts dins del seu propi àmbit. La ubicació no determina l'autoritat per si sola. El mapa sí.

**Una memòria cau mai no substitueix una font.** Si un resum diu set dies i el requisit aprovat diu trenta, feu servir el requisit per al comportament objectiu. Conserveu el resum contradictori com a evidència de deriva, no com una regla alternativa. Un cop definida l'autoritat, establiu el flux d'escriptura.

## Primer obteniu evidències, després proposeu

**Els agents incorporen evidències al context de la sessió** i després redacten propostes. No aproven fets duradors pel seu compte. Editar una branca de tasca o enviar un esborrany no equival a publicar una política, fusionar codi o marcar una decisió com a acceptada.

```text
Font -> lectura amb permisos comprovats -> context de sessió
Context de sessió -> proposta + versió base -> revisió del responsable
Aprovació del responsable -> publicació controlada -> registre de canvis
Versió base canviada -> conciliar la proposta -> revisar de nou
```

**Adjunteu la versió base** abans de demanar una revisió. El revisor necessita el valor anterior, el valor proposat, el motiu, les evidències i els sistemes afectats. L'aprovació ha de referir-se a una revisió concreta de la proposta, no a un xat en evolució.

```yaml
proposal_id: PROP-042
target: wiki:REQ-17
base_version: 8
change: "Conserveu les exportacions durant trenta dies en lloc de set."
evidence:
  - "decision:DEC-12 acceptada"
affected_records:
  - "repo:export-service configuració de retenció"
  - "wiki:RUN-04 procediment de neteja"
owner_role: product-owner
status: awaiting-review
```

**Els identificadors anteriors són exemples.** Registreu una fila per a cada canvi lògic aprovat amb l'ID de proposta, registres objectiu, versions anterior i resultant, aprovador, marca temporal i referència de fusió o publicació. Enllaceu-hi els esdeveniments d'auditoria propis dels sistemes sense substituir-ne l'historial natiu.

**Les persones prenen la decisió.** Un editor autoritzat o una automatització limitada aplica la revisió aprovada. Limiteu les credencials d'escriptura en conseqüència. Les instruccions soles no separen la redacció de la publicació. La mateixa distinció s'aplica a la recuperació.

## Context compartit sense RAG

**Un mapa de projecte és el primer índex de recuperació.** Manteniu una pàgina per projecte amb els ID de font, les ubicacions del repositori, les claus del gestor, els àmbits d'autoritat i els responsables. Llegiu primer el mapa i després obteniu el registre pertinent per ID. Cerqueu quan l'ID sigui desconegut.

### Barra lateral: mapa de projecte d'exemple

```yaml
project: export-service
map_id: MAP-01
policy:
  source_id: POL-01
  approved_version: 3
  owner_role: policy-owner
sources:
  requirements: {page_id: REQ-17, owner_role: product-owner}
  runbook: {page_id: RUN-04, owner_role: operations-owner}
  decisions: {register_id: DEC-REGISTER, owner_role: project-lead}
repository:
  key: export-service
  setup: README.md
  terms: CONTEXT.md
  decisions: docs/adr/
tracker:
  project_key: EXP
  active_task: EXP-42
```

**Els connectors directes redueixen la còpia manual.** Model Context Protocol (MCP) és un protocol d'integració per exposar eines i context a aplicacions d'IA. Feu servir connectors aprovats per al wiki, el gestor de tasques i el repositori quan siguin compatibles. Una consulta dirigida limita els resultats irrellevants, però no substitueix l'autorització ni les comprovacions d'actualitat. Seguiu les orientacions de seguretat de MCP enllaçades a les referències en triar els permisos del connector.

**La recuperació exacta requereix poca configuració.** Ofereix evidències citables sense una base de dades vectorial. Els límits també són clars: algú manté el mapa, les preguntes àmplies necessiten cerca addicional i les pàgines grans ocupen espai de sessió. Recupereu la secció pertinent amb les restriccions del voltant en lloc d'enganxar un manual sencer.

**El treball sense connexió fa servir snapshots explícits.** Registreu la revisió exportada i marqueu les respostes com a basades en un snapshot. No publiqueu canvis fins que una persona o un connector autoritzat comprovi la font actual. Després, feu visible la mateixa política a cada interfície.

## Una política, adaptadors diferents

**Manteniu una política compartida** i distribuïu adaptadors breus específics per a cada eina. Poseu la versió aprovada de la política a la primera línia de cada adaptador o conjunt d'instruccions copiat. Incloeu l'ID de la font i un snapshot local revisat per a les sessions sense accés al connector.

**La càrrega varia segons l'eina.** Codex documenta la descoberta per capes de **`AGENTS.md`**. Claude Code documenta **`CLAUDE.md`**, les importacions i la memòria de projecte. Cline documenta **`.clinerules/`** i els controls de regles. Feu servir la documentació oficial enllaçada a les referències. Verifiqueu les instruccions carregades en la versió instal·lada en lloc de suposar que els noms dels fitxers es comporten igual.

### Barra lateral: capçalera d'exemple d'AGENTS.md

```markdown
Versió de la política: v3 | Font: wiki:POL-01 | Estat: aprovada

# Instruccions del projecte

Llegiu el mapa de projecte MAP-01 abans de començar una tasca.
Carregueu docs/policy-snapshot.md i registreu la revisió de la font.
Tracteu la memòria del xat i els fragments de cerca com a memòries cau.
Adjunteu les revisions de les fonts a cada proposta factual.
Feu servir una branca de tasca i un worktree per a cada tasca de programació.
No publiqueu polítiques, no aproveu decisions ni fusioneu la vostra PR.
Atureu-vos davant conflictes de fonts o escriptures solapades no resolts.
Comprovacions obligatòries: proves, revisió de la documentació, actualitat de la política.
Responsables: mantenidor d'enginyeria, responsable de producte i responsable de polítiques.
```

**Les instruccions dels projectes de xat reben la mateixa capçalera i procediment.** Les persones que no programen reben el snapshot de la política i el mapa de projecte mitjançant càrregues o connectors aprovats. Si la interfície no té accés en directe, una persona proporciona l'exportació versionada i en registra la limitació.

**Una etiqueta de versió és una afirmació, no una prova que el contingut sigui idèntic.** Genereu adaptadors des del snapshot aprovat o compareu-ne les parts de política amb un resum criptogràfic emmagatzemat. Reviseu per separat les excepcions específiques de cada adaptador. Comproveu durant el pilot les regles desactivades, les sobreescriptures imbricades i les instruccions personals. Després, registreu les evidències emprades per cada tasca.

## Registreu un manifest de context

**Un manifest de context explica les evidències de la resposta.** Registreu els ID i les revisions de pàgines, les claus d'issues i la seva revisió o hora d'actualització, i els ID complets de commit del repositori. Incloeu l'hora de recuperació i les seccions pertinents. Marqueu els registres no disponibles en lloc de substituir-los per un resum recordat.

```yaml
task: EXP-42
policy: {page_id: POL-01, version: 3}
wiki:
  - {page_id: REQ-17, version: 8, section: export-retention}
tracker:
  - {issue_key: EXP-42, revision: 5}
repository:
  commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  files: [README.md, config/retention.yaml]
limits:
  - "No s'ha recuperat el runbook. No se n'ha proposat cap canvi."
```

**El valor del commit és sintètic.** Substituïu-lo pel commit inspeccionat en un manifest real. Afegiu-hi l'hora de recuperació durant la consulta real. Un registre creat abans de la inspecció és una llista de comprovació, no una evidència.

**Les citacions ajuden a comprovar,** no generen confiança automàtica. Enllaceu cada afirmació important amb el registre i la secció que la fonamenten. Si dues fonts discrepen, conserveu totes dues al manifest i comuniqueu la diferència no resolta. No trieu només pel segell temporal més recent sense comprovar-ne l'àmbit i l'aprovació. Aquesta disciplina també s'aplica a la recuperació semàntica.

## Context compartit amb RAG

**La generació augmentada amb recuperació (RAG)** proporciona al model material recuperat mentre formula una resposta. Un índex semàntic ajuda a trobar fragments pertinents encara que la pregunta faci servir altres paraules. La visió general de RAG de Microsoft descriu la fonamentació, els límits de recuperació i els requisits de control d'accés. Consulteu la font oficial a les referències.

**Feu servir RAG per descobrir contingut en col·leccions grans,** com ara documentació antiga, notes de reunió i transcripcions. Etiqueteu les classes de documents i els estats d'aprovació. Una transcripció indexada des de l'enregistrament original és una font del que van dir els participants, no una autoritat per als requisits aprovats. No convertiu una conversa en política mitjançant la indexació.

| Regla de l'índex | Comportament exigit |
|---|---|
| **Ingeriu fonts, no memòries cau** | Excloeu els resums generats i les còpies locals sense seguiment |
| **Preserveu la procedència** | Deseu per fragment l'ID de font, la revisió, la secció i l'estat del document |
| **Actualitzeu quan hi hagi canvis** | Reindexeu les edicions i invalideu els fragments obsolets |
| **Respecteu els canvis d'accés** | Actualitzeu permisos i elimineu contingut suprimit o revocat |
| **Retorneu citacions** | Mostreu referències dels registres al costat del text recuperat |
| **Comproveu el registre en directe** | Obteniu evidències actuals abans de proposar una acció important |

**En aquest marc, un fragment recuperat és un indicador.** El seu text ajuda a localitzar evidències. La font en directe confirma la redacció actual, l'aprovació, les excepcions properes i l'accés. Si la recuperació en directe falla, marqueu el snapshot i atureu l'acció duradora. És una regla de governança, no una afirmació sobre totes les implementacions de RAG.

**Els embeddings obsolets i el context absent creen riscos diferents.** Un fragment antic no inclou una revisió. Un fragment actual també pot induir a error si una excepció és a la secció següent. Preserveu els títols i recupereu les restriccions adjacents abans d'avaluar un requisit.

**La filtració de permisos mereix una prova pròpia.** Apliqueu l'autorització abans de retornar fragments al model, no després de generar la resposta. Reviseu el contingut sensible abans d'indexar-lo o enviar crides a embeddings externs. Tingueu en compte el text copiat als registres, les peticions al model i les traces de recuperació. Triar un model local no converteix un connector remot en local. Aquestes comprovacions determinen si RAG encaixa en el pilot.

## Trieu mapa, RAG o tots dos

**Adapteu la recuperació a la pregunta.** Un ID de requisit conegut afavoreix l'accés directe. Una pregunta oberta sobre material històric dispers afavoreix la cerca. Comenceu pel mapa tret que la descoberta ja sigui un problema mesurat.

### Barra lateral: RAG o no?

```text
Les tasques solen indicar un projecte, una pàgina, un issue o un fitxer?
  Sí -> La recuperació directa és suficient per al pilot?
           Sí -> NOMÉS MAPA
           No -> HÍBRID: mapa per als ID coneguts, RAG per descobrir
  No -> Les evidències estan disperses en una col·lecció gran?
           No -> NOMÉS MAPA, més la cerca nativa
           Sí -> La feina és exploratòria i només de lectura?
                    Sí -> NOMÉS RAG per descobrir
                    No -> HÍBRID amb comprovacions de fonts en directe

Totes les opcions mantenen responsables, autorització i procedència.
La descoberta amb RAG també comprova les fonts abans d'una acció duradora.
```

**Només RAG descriu la interfície de recuperació,** no un permís per ometre la governança. Feu-lo servir per a una col·lecció exploratòria acotada on continuï sent possible comprovar directament les fonts. És una mala opció per a canvis amb ID conegut que necessiten comprovacions precises de versió.

**El model híbrid separa descoberta i verificació.** El mapa resol les consultes conegudes. RAG localitza registres desconeguts. RAG respon «on». La font respon «què». Per a l'exemple de retenció, obteniu directament **`REQ-17`**. Per a «quines decisions antigues sobre exportacions expliquen aquest límit?», cerqueu al registre i obteniu cada decisió pertinent. Ara apliqueu la part del repositori.

## Informació dins del repositori

**El coneixement del repositori canvia amb la implementació.** Manteniu una estructura compacta perquè els agents i revisors sàpiguen on buscar.

| Fitxer o directori | Responsabilitat |
|---|---|
| **`CONTEXT.md`** | Termes del projecte i enllaços als registres autoritatius |
| **`docs/adr/`** | Decisions d'arquitectura del repositori acceptades |
| **`docs/design/`** | Descripcions aprovades del comportament del sistema |
| **`docs/plans/`** | Plans d'implementació proposats amb estat explícit |
| **`AGENTS.md`** | Controls de revisió, límits i rols responsables |
| **`README.md`** | Configuració i punts d'entrada, no requisits duplicats |

**Apliqueu la regla de la mateixa PR:** canvieu junts el codi i els documents del repositori afectats. Si no cal actualitzar la base de coneixement, exigiu una excepció escrita a la descripció de la PR o al lloc acordat per als trailers del commit.

```text
KB-Update: none (motiu: la refactorització interna conserva el comportament documentat)
```

**La pipeline aplica la declaració.** Una comprovació obligatòria rebutja canvis de comportament sense actualització documental o excepció. Un responsable humà de documentació revisa l'excepció. Una comprovació per camí identifica canvis candidats, però no prova la integritat semàntica. Exigiu la comprovació i la revisió mitjançant protecció de branca o un control de fusió equivalent.

**Una porta absent de la pipeline no és una porta.** Escriure «revisió de la documentació» en un fitxer d'instruccions només dona orientació. Proveu-ne l'aplicació enviant una PR deliberadament incompleta durant el pilot i confirmeu que la fusió queda bloquejada.

**Feu servir una tasca, una branca i un worktree.** La documentació oficial de Git sobre worktrees descriu arbres de treball separats amb el seu propi estat de checkout. Els worktrees separats redueixen col·lisions locals d'edició. No impedeixen que dues branques canviïn el mateix fitxer ni que dos agents actualitzin la mateixa pàgina wiki.

**No feu mai commits directament a la branca predeterminada,** tant si es diu **`main`**, **`master`** com d'una altra manera. Informeu de les diferències entre requisits i codi al gestor de tasques. Adjunteu els registres en conflicte i deixeu que els seus responsables resolguin el comportament desitjat abans d'alinear cap costat. Apliqueu controls equivalents fora de Git.

## Informació fora del repositori

**El wiki necessita un estàndard documental.** Cada pàgina autoritativa indica la finalitat, l'estat, el responsable, la revisió, la data de revisió i els ID de fonts relacionades. Poseu les propostes en una zona d'esborranys clarament no autoritativa. No barregeu redacció proposada en una pàgina de requisits aprovada.

**Les actualitzacions segures segueixen una seqüència fixa:**

1. **Torneu a llegir** la pàgina actual i les restriccions del voltant.
2. **Compareu** la seva versió amb la versió base de la proposta.
3. **Concilieu** les edicions intermèdies i obteniu una nova aprovació per al text canviat.
4. **Escriviu** la revisió aprovada amb una condició sobre la versió esperada.
5. **Verifiqueu** la pàgina desada i afegiu la referència al registre de canvis.

**Tornar a llegir no elimina les curses d'escriptura.** Feu servir el mecanisme d'actualització condicional del sistema si n'hi ha. Si no, serialitzeu la publicació mitjançant un sol responsable i verifiqueu el resultat. Atureu-vos si un altre autor canvia la base durant la revisió.

**La regla de no suprimir s'aplica als fluxos d'agents.** Els agents proposen arxivar o eliminar. Les persones autoritzades apliquen procediments de retenció i eliminació. No interpreteu aquesta regla com un permís per conservar indefinidament informació sensible.

**Les troballes del gestor inclouen evidències,** no només conclusions. Registreu què heu observat, l'ordre exacte o mètode d'inspecció, el commit inspeccionat, el comportament esperat i real i els criteris d'acceptació. Elimineu secrets i sortides sensibles abans d'adjuntar evidències. Marqueu les ordres suggerides com a no executades fins que algú les executi.

```text
Troballa: la implementació de retenció no concorda amb el requisit aprovat
Evidència: REQ-17 v8 i config/retention.yaml inspeccionat
Ordre d'inspecció: git show HEAD:config/retention.yaml
Commit: l'ID complet del commit inspeccionat consta al manifest
Acceptació: la durada aprovada concorda amb codi, proves i runbook
Estat: pendent de revisió dels responsables de producte i enginyeria
```

**L'exemple és una plantilla de troballa,** no un resultat mesurat. Completeu-lo després d'una inspecció real. Enllaceu l'actualització del wiki i les evidències del gestor mitjançant l'ID de proposta.

**El registre de decisions separa regles i raonaments.** Emmagatzemeu la pregunta, opcions, recomanació, compensacions, responsable, estat d'aprovació i referència a la regla resultant. Els agents proposen. Les persones decideixen. Les regles aprovades van a les polítiques i procediments. La justificació queda al registre.

**Recolliu els fets duradors de les reunions i els xats.** Envieu una proposta amb les evidències de la font i demaneu-ne l'aprovació. Fins que es publiqui, marqueu l'acord com a provisional. Després, connecteu el comportament aprovat entre el repositori i el wiki.

## Connecteu els dos sistemes

**La sincronització després de la fusió trasllada els canvis d'implementació cap a fora.** Creeu una tasca d'actualització del wiki enllaçada amb el commit fusionat, el requisit aprovat i el runbook afectat. Un agent redacta l'actualització. El responsable del wiki comprova la pàgina actual i n'aprova la publicació. Manteniu la tasca oberta fins que verifiqueu la revisió desada.

**La vigència de les polítiques és una auditoria separada.** Compareu cada adaptador del repositori i cada còpia de les instruccions del xat amb la versió canònica aprovada. La política **`v3`** és a **`POL-01`**. Cada **`AGENTS.md`** indica **`v3`** a la primera línia. L'auditoria marca **`v2`**, etiquetes absents i diferències de contingut encara que les etiquetes coincideixin.

| Comprovació | Evidència de finalització |
|---|---|
| **Vigència de la política** | Comparació de la versió canònica i el resum de l'adaptador |
| **Conciliació de requisits** | Revisió del requisit comparada amb codi i proves |
| **Sincronització postfusió** | Commit fusionat enllaçat amb la revisió publicada al wiki |
| **Resolució de conflictes** | Decisió aprovada pel responsable enllaçada amb tots dos registres afectats |

**Concilieu segons el calendari o en el moment de la PR.** Una auditoria setmanal és adequada per a un pilot. Una PR que canvia el comportament necessita una comprovació de requisits abans de fusionar-se. Trieu la freqüència segons el cost de la deriva i registreu l'última comprovació satisfactòria.

**El canvi a trenta dies té diversos punts de control:** producte aprova el requisit, enginyeria actualitza la configuració i les proves, els revisors fusionen la PR i operacions publica l'actualització del runbook. Una fila del registre de canvis enllaça els registres resultants. Una sincronització fallida del wiki continua visible en lloc d'amagar-se darrere d'una fusió satisfactòria. Els relleus compartits mantenen aquesta seqüència entre eines.

## Un procediment per a cada eina

**Empaqueteu els passos repetits com a skills o prompts,** amb un ID de procediment versionat. Compartiu el contracte, no un format de fitxer universal suposat. Cada adaptador d'eina proporciona el mecanisme de càrrega o invocació admès.

| Procediment | Resultat obligatori |
|---|---|
| **Iniciar una tasca** | Responsable, àmbit, versió de la política, manifest de fonts, reserva d'escriptura |
| **Revisió de documents** | Metadades absents, autoritat duplicada, referències de font trencades |
| **Comprovació de coneixement** | Diferències entre requisit i codi amb revisions justificatives |
| **Relleu** | Evidències actuals, propostes, comprovacions completes, preguntes no resoltes |

**Els no programadors treballen sense Git.** Recuperen fonts permeses en projectes de xat, omplen la mateixa plantilla de proposta i la presenten al responsable mitjançant una pàgina d'esborrany o una tasca al gestor. No necessiten cap checkout del repositori per demanar una correcció del requisit.

**Els programadors fan servir fitxers del repositori i controls de PR.** Enllacen la proposta aprovada a la PR, registren els commits inspeccionats i executen les comprovacions obligatòries. Tots dos grups transmeten la mateixa estructura d'evidències.

```yaml
handoff:
  task: EXP-42
  policy_version: 3
  manifest: "ID i revisions de fonts, i commit inspeccionat adjunts"
  completed: [requirement-review]
  proposals: [PROP-042]
  pending: [implementation-review, runbook-publication]
  reservations: ["la publicació de RUN-04 s'ha assignat al responsable d'operacions"]
  unresolved: []
  next_owner_role: engineering-maintainer
```

**Un relleu continua sent una memòria cau.** La persona següent torna a llegir les fonts abans d'actuar i n'enregistra les noves revisions. No doneu per provat «completat» sense comprovar l'aprovació o les evidències de prova enllaçades. Apliqueu les proteccions següents abans d'escriure.

## Proteccions abans de cada escriptura

**Examineu les dades abans que surtin del sistema d'origen.** Comproveu la classificació, els permisos dels connectors, les destinacions aprovades, el tractament del proveïdor del model i el registre d'activitat. Envieu el mínim de contingut pertinent. Manteniu els registres restringits fora dels projectes de xat i serveis d'embeddings no autoritzats.

**El text recuperat és una evidència, no un canal d'instruccions.** Una pàgina wiki o resposta d'una eina que digui a un agent que ignori la política no en canvia l'autoritat. Reviseu per separat les instruccions que provenen del contingut i la política operativa aprovada. Limiteu els connectors a només lectura durant la recuperació i separeu les credencials de publicació de l'accés a la sessió.

**Assigneu un responsable actiu per pàgina o fitxer.** Registreu la reserva al gestor de tasques amb l'àmbit i la caducitat. Torneu a llegir abans d'escriure i feu servir comprovacions de versió. Els worktrees separats ajuden aïllant la feina local; les reserves i escriptures condicionals gestionen els registres compartits.

| Motiu per aturar-se i preguntar | Resposta necessària |
|---|---|
| **Les fonts discrepen i no hi ha responsable** | Atureu-vos i demaneu l'assignació d'autoritat |
| **Una altra tasca ha reservat l'objectiu** | Acordeu la responsabilitat abans d'editar |
| **La versió base ha canviat** | Concilieu-la i demaneu una nova aprovació |
| **Una afirmació important no té evidències** | Marqueu-la com a no verificada i demaneu una font |
| **El tractament de dades no és clar** | Manteniu el contingut al sistema d'origen |
| **Falla l'accés a la font en directe** | Registreu els límits del snapshot i atureu l'acció duradora |

**Els prompts no són controls de seguretat.** Comproveu fora del model la denegació de permisos, les branques protegides, el rebuig de bases obsoletes i la responsabilitat d'escriptura. Una demostració conforme no és suficient si el compte encara té drets de publicació sense restriccions. Feu servir aquestes proves per decidir si el pilot està preparat.

## Feu una prova pilot abans de promoure

**Comenceu el marc com un esborrany.** Proveu un projecte amb un programador, un no programador i responsables de fonts identificats. Feu la mateixa pregunta amb un ID conegut en dues eines i després un exercici deliberat de conflicte de fonts. Reviseu els manifestos i les propostes, no la fluïdesa de la prosa.

**Raonament esperat:** tots dos participants identifiquen el requisit aprovat actual i descriuen separadament la implementació inspeccionada. Si discrepen, primer comparen les entrades del manifest. És un exercici proposat, no un benchmark observat.

| Mètrica | Definició |
|---|---|
| **Taxa de citació** | Afirmacions importants amb suport de fonts ÷ afirmacions factuals importants de les mostres |
| **Troballes setmanals de deriva** | Diferències confirmades d'autoritat o versió, agrupades per tipus de font |
| **Temps de resposta de la proposta** | Temps mitjà entre una proposta llesta per revisar i la decisió registrada |
| **Feina refeta per context obsolet** | Tasques reobertes per evidències obsoletes o no verificades |

**Mesureu una línia base abans de fixar objectius.** Més troballes de deriva durant la primera setmana poden indicar una detecció millor, no una documentació pitjor. Seguiu la recurrència i el temps de resolució juntament amb el recompte brut. Reviseu les evidències sensibles sense copiar-les a exportacions analítiques.

**Lliureu un repositori d'exemple durant el desplegament.** Incloeu un mapa sintètic, adaptadors de política, manifests, plantilles de proposta, excepcions documentals i comprovacions de revisió executables. Feu servir registres wiki i del gestor simulats, sense credencials de producció. Demostreu la publicació denegada, el rebuig d'una base canviada, la deriva de versió de política i un relleu satisfactori.

**Un repositori de plantilles és un lliurable del desplegament,** no un recurs subministrat amb aquest article. Promoveu el model operatiu després que la direcció i els responsables de fonts revisin els resultats del pilot. Manteniu les excepcions i els casos de fallada no resolts al registre de decisions. Abans de promoure'l, corregiu els errors previsibles següents.

## Resolució de problemes del context compartit

| Símptoma | Primera reparació |
|---|---|
| **Dues eines responen diferent** | Compareu els ID de font, revisions, àmbit i estat d'aprovació |
| **Les instruccions semblen actuals però el comportament difereix** | Inspeccioneu els adaptadors carregats, els controls de regles i les substitucions locals |
| **RAG retorna requisits antics** | Inspeccioneu l'actualització de l'índex i obteniu la pàgina en directe |
| **Una edició del wiki esborra un altre canvi** | Exigiu escriptures condicionals o publicació serialitzada |
| **Les comprovacions de documents passen amb text obsolet** | Afegiu revisió del responsable i conciliació del requisit |
| **Les decisions queden al xat** | Assigneu el canal d'entrada de propostes i la responsabilitat del registre |

**Repareu el recorregut de les evidències abans de reescriure el prompt.** Torneu a executar el cas pilot fallit i registreu-ne el resultat. Feu servir la llista següent per convertir el procés corregit en una pràctica setmanal repetible.

## Deu passos per a aquesta setmana

1. **Trieu un projecte pilot** i les persones i eines que hi participaran.
2. **Assigneu una font i un responsable** a cada tipus d'informació.
3. **Publiqueu un mapa de projecte** amb ID de font i àmbits d'autoritat.
4. **Redacteu una política compartida** i obteniu la revisió del responsable.
5. **Versioneu cada adaptador d'instruccions a la primera línia** i verifiqueu que es carrega.
6. **Exigiu un manifest de context** per a respostes i propostes factuals importants.
7. **Creeu un canal d'entrada de propostes** amb versions base i aprovador identificat.
8. **Apliqueu controls d'escriptura** i la regla documental de la mateixa PR.
9. **Proveu deriva, conflicte i relleu** amb registres sintètics.
10. **Reviseu les mètriques del pilot** i aproveu l'etapa següent.

**Assigneu una font a cada fet, feu que cada eina hi llegeixi i feu passar cada canvi durador per una persona.**

## Referències i passos següents

**La documentació oficial dona suport als components tècnics,** no a les regles organitzatives del marc. Comproveu el comportament de les eines instal·lades i els permisos dels connectors durant el pilot.

- **Instruccions del Codex:** [Instruccions personalitzades amb AGENTS.md](https://developers.openai.com/codex/guides/agents-md), sobre la descoberta i verificació d'instruccions.
- **Instruccions de Claude Code:** [Com recorda Claude el vostre projecte](https://code.claude.com/docs/en/memory), sobre instruccions de projecte i memòria.
- **Instruccions de Cline:** [Regles](https://docs.cline.bot/customization/cline-rules), sobre regles de l'espai de treball i controls d'activació.
- **Disseny de recuperació:** [Generació augmentada amb recuperació a Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview), sobre fonamentació, límits de recuperació i seguretat.
- **Seguretat dels connectors:** [Bones pràctiques de seguretat de MCP](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices), sobre autorització i riscos dels connectors.
- **Aïllament dels worktrees:** [Documentació de Git worktree](https://git-scm.com/docs/git-worktree), sobre arbres de treball separats i estat compartit del repositori.

**Per planificar la inferència local,** llegiu la [Guia de context GPU d'IA local](/articles/local-ai-model-gpu-context-guide/). La capacitat del maquinari i la governança de fonts compartides resolen problemes diferents. Una finestra de context més gran no corregeix autoritats en conflicte.

{{< centerbutton href="/articles/local-ai-model-gpu-context-guide/" >}}
  Llegiu la Guia de context GPU d'IA local
{{< /centerbutton >}}
