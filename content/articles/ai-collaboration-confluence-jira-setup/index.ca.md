---
title: "Configuració d’IA a Confluence i Jira: permisos i autoritat"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Configureu pàgines de referència de Confluence i permisos de Jira gestionats per l’empresa per a una col·laboració entre equips revisada."
genre: ["Intel·ligència artificial", "Col·laboració en equip", "Enginyeria del programari"]
tags: ["curs de col·laboració amb IA", "Confluence Cloud", "Jira Cloud", "pàgines de referència", "esquema de permisos de Jira", "transició del flux de treball", "proves d’accés"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Il·lustració de professionals que revisen el treball compartit d’un projecte en un espai de ciberseguretat"
coverCaption: ""
---

[Torneu al curs de col·laboració amb IA](/ai-collaboration-course-start/)

**L’administrador defineix l’autoritat a la feina abans de connectar les eines de xat.** Els responsables de producte i d’operacions publiquen requisits i manuals a Confluence Cloud. Jira Cloud coordina el lliurament. GitHub gestiona la implementació. Creeu entorns de proves separats després de preparar els fonaments, perquè un permís incorrecte exposa informació independentment del comportament del model.

## Idees clau

- **Confluence** és la font de la redacció aprovada dels requisits.
- **Jira** gestiona l’estat del lliurament, no la política de retenció.
- **GitHub** gestiona la configuració i les polítiques compartides.
- **Les proves de permisos** necessiten plans adequats i usuaris separats.

## Abans de començar

**Requisits previs:** els [fonaments](/articles/ai-collaboration-pilot-foundation/), el repositori del laboratori, l’administració dels espais de Confluence i de Jira, i usuaris separats per als rols de col·laborador, responsable i editor. **Temps estimat:** de 90 a 120 minuts. **Dificultat:** administració avançada.

**Requisit del pla:** Confluence Free no admet restriccions de contingut. Jira Free no inclou esquemes de permisos configurables, rols d’espai ni esquemes de seguretat d’elements de treball. Per a aquest itinerari, feu servir entorns de proves adequats amb Standard o un pla superior. Abans de provar, verifiqueu el pla real i els privilegis a les referències.

**Nota de navegació:** la documentació actual de Jira fa servir “space” i “work item”. Alguns tenants encara conserven “project” i “issue”. Trieu una configuració gestionada per l’empresa. Aquest procediment no cobreix el comportament dels permisos gestionats per l’equip. No cal Rovo, cap aplicació de Marketplace, aprovacions de Jira Service Management ni un connector de xat de pagament.

**Resultat:** prepareu una matriu de permisos, pàgines de referència amb nom, un flux de treball de Jira només per al laboratori i proves de denegació amb usuaris separats. Anoteu el pla del tenant i els supòsits dels rols al costat dels resultats.

**Comprovacions abans de crear registres:**

| Comprovació | Si està disponible | Si no està disponible |
|---|---|---|
| Restriccions de pàgina i administració d’espais de Confluence | Creeu pàgines aprovades i excloses separades | Marqueu com a Bloquejades les proves d’edició i de denegació de lectura |
| Esquema de permisos i editor de fluxos de treball de Jira gestionat per l’empresa | Copieu un esquema i un flux només per al laboratori | Marqueu com a Bloquejades les proves de transició |
| Usuaris separats per als rols de col·laborador, responsable, editor i usuari exclòs | Executeu proves positives i negatives per rol | Marqueu com a Bloquejats els rols no provats |
| Responsable del repositori i branca protegida | Enllaceu la ruta d’implementació revisada | Completeu primer la ruta GitHub-first abans de la publicació mixta |

A l’octubre de 2026, feu servir el botó **Share** o el control de restriccions per gestionar l’accés a les pàgines, l’àrea de permisos de **Space settings** a Confluence per a concessions més àmplies i **Settings > Work items > Permission schemes** a Jira per a l’esquema del laboratori. L’editor de fluxos de treball de Jira gestionat per l’empresa controla les transicions. Les etiquetes de la interfície i les funcions del pla varien segons el tenant. Abans de seguir aquests passos, registreu la ruta real i el pla com a prova. Consulteu els [permisos de pàgina de Confluence](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/) i els [esquemes de permisos de Jira](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/).

## Crear les pàgines de referència

1. **Creeu un espai de Confluence** anomenat **`Export Service Lab`**. Desactiveu l’accés anònim i la compartició pública amb els controls disponibles del lloc o de l’espai.
2. **Creeu pàgines publicades**, no documents en directe, anomenades **`REQ-17 Export Retention`**, **`RUN-04 Export Cleanup`** i **`Decision Register`**.
3. Com a responsable de producte, **publiqueu el requisit inicial** següent. Registreu l’ID i la versió reals de la pàgina al mapa del repositori.
4. Com a responsable d’operacions, **publiqueu RUN-04** amb una retenció de set dies i la indicació que al laboratori no s’executa cap tasca d’eliminació.
5. A cada pàgina de referència, **obriu Share**. Configureu l’accés general com a només lectura per als membres aptes de l’espai i concediu permisos d’edició específics als responsables i editors designats. Deseu i verifiqueu amb l’usuari col·laborador.

```text
Source ID: REQ-17
Owner role: product-owner
Status: Approved baseline
Scope: synthetic export files only
Retention: 7 days
Delivery state: baseline lab configuration
Exceptions: production data, backups, and legal holds excluded
Approval evidence: DEC-12 baseline review
Implementation reference: attach protected GitHub baseline commit
```

**Apliqueu restriccions a cada pàgina de referència.** No suposeu que una restricció d’edició a una pàgina principal protegeix les seves pàgines filles. L’herència de lectura i edició funciona de manera diferent, i els permisos de l’espai també s’apliquen. Un enllaç per si sol no concedeix accés. Reviseu totes les pertinences si un usuari que només hauria de llegir encara pot editar.

**Feu servir aquests textos inicials per a les altres dues pàgines.** Abans d’aprovar un registre, substituïu els camps de revisió provisionals per proves reals del sandbox.

```text
Source ID: RUN-04
Owner role: operations-owner
Status: Approved baseline
Scope: synthetic export files only
Configured retention: 7 days
Procedure: compare REQ-17 with config.json before a reviewed change
Runtime limit: this lab has no deletion job and produces no deletion evidence
Recovery: restore the prior approved configuration through review
Recovery limit: restoring configuration does not restore deleted files
Review evidence: add actual reviewer, page version, and decision reference
```

```text
Page: Decision Register
Entry ID: DEC-12
Decision: use seven days as the synthetic baseline
Scope: export-service-lab only
Requirement: REQ-17 page version, record after publication
Runbook: RUN-04 page version, record after publication
Policy: POL-01 protected GitHub revision, record after review
Product review: pending until the named owner records a decision
Operations review: pending until the named owner records a decision
Status: draft example, replace with observed review evidence
```

## Actualitzar el mapa

```yaml
track: mixed-workplace
policy: {source_id: POL-01, home: GitHub, version: 1}
requirements: {source_id: REQ-17, home: Confluence, owner_role: product-owner}
runbook: {source_id: RUN-04, home: Confluence, owner_role: operations-owner}
decisions: {source_id: DEC-12, home: Confluence, owner_role: project-lead}
implementation: {home: GitHub, file: config.json}
delivery: {home: Jira, proposal_id: PROP-042}
snapshot_rule: repository requirement copies are not authoritative
```

**Afegiu al mapa les ubicacions privades reals del sandbox i els ID de les pàgines.** La plantilla identifica les fonts d’autoritat sense fingir que conté adreces actives. Elimineu del README el text que atribueix autoritat sobre els requisits de la ruta mixta al fitxer JSON copiat.

**Manteniu POL-01 a GitHub** per a les dues rutes. Confluence enllaça a la seva revisió aprovada. Moure l’autoritat de la política durant una tasca requereix un altre canvi d’autoritat revisat.

## Configurar els permisos de Jira

1. **Creeu un espai de laboratori gestionat per l’empresa** i copieu un esquema de permisos en un esquema dedicat al laboratori. No editeu un esquema de producció compartit.
2. **Obriu Settings, Work items, Permission Schemes**, seleccioneu l’esquema del laboratori i actualitzeu les concessions.
3. **Concediu als col·laboradors permisos de consulta, creació i comentari.** Restringiu els privilegis administratius. Reviseu explícitament els permisos d’edició i **Transition work items**.
4. **Associeu l’esquema** a l’espai del laboratori i verifiqueu que cap espai de producció el comparteixi.
5. **Creeu PROP-042** com a element de treball. Registreu la clau generada al mapa i manteniu PROP-042 com a ID lògic de proposta a la descripció.

**Enganxeu aquest esborrany a PROP-042.** L’element de Jira fa el seguiment del lliurament. El seu text no substitueix la redacció aprovada a Confluence.

```text
Proposal ID: PROP-042
Status: Draft
Current approved value: 7 days, REQ-17 page version to record
Proposed value: 30 days for synthetic export files
Exclusions: production data, backups, legal holds
Affected records: REQ-17, RUN-04, config.json, proposal.json
Fixed proposal attachment: pending
Product-owner review: pending
Operations-owner review: pending
Publication ledger: pending
Stop on changed source version, missing review, or denied access
```

| Rol | Confluence | Jira | GitHub |
|---|---|---|---|
| **Col·laborador** | Llegeix pàgines aprovades | Crea esborranys i hi comenta | Branca de proposta o Issue |
| **Responsable de producte** | Revisa el requisit | Registra la revisió del requisit | Revisa les proves de la PR |
| **Responsable d’operacions** | Revisa el manual | Registra la revisió operativa | Revisa l’impacte operatiu |
| **Editor** | Edita pàgines aprovades | Registra l’estat de publicació | Sense autoritat automàtica per fusionar |
| **Mantenidor** | Llegeix el requisit | Registra la implementació | Revisa i fusiona la PR protegida |

**Els permisos de diversos grups se sumen.** Elimineu les concessions àmplies no desitjades al laboratori en lloc de suposar que una concessió limitada les anul·la. No afegiu identitats dels connectors als grups administratius.

## Definir els estats de lliurament

**Copieu un flux de treball gestionat per l’empresa** en un flux exclusiu del laboratori. Afegiu els estats Esborrany, Revisió, Aprovat, Publicació, Fet i Bloquejat. Afegiu transicions per a l’enviament, l’aprovació, la publicació, la finalització, el bloqueig i el retorn a revisió. Associeu-lo només al tipus de treball del laboratori.

1. A l’editor del flux de treball, **seleccioneu la transició cap a Aprovat**.
2. **Afegiu una condició o restricció** que limiti l’acció al rol o grup designat de responsable/editor. Feu servir els controls documentats i publiqueu l’esborrany del flux com a administrador.
3. **Comproveu manualment les revisions dels dos responsables** abans de la transició. Cada revisió identifica la proposta congelada i les versions de les fonts.
4. **Restringiu Fet** al rol responsable del lliurament. Elimineu les transicions alternatives o globals que esquivin aquest límit.

**Una transició restringida no és una aprovació per dues persones.** Controla qui executa la transició. En aquest pilot, la comprovació de les proves dels dos rols continua sent un procediment. Registreu explícitament aquest límit.

**Exemple de registre de transició:** per a **Revisió a Aprovat**, permeteu que només el grup designat de responsables/editors l’activi. Abans d’activar-la, la persona obre el fitxer adjunt fix de PROP-042 i comprova una decisió del responsable de producte i una del responsable d’operacions sobre la mateixa revisió de la proposta. Si falta una decisió o es refereix a una revisió anterior, deixeu l’element a Revisió i registreu la mancança. La restricció del flux controla qui executa la transició. La comprovació de les proves és un pas humà separat.

## Verificar la denegació

**Com a col·laborador**, llegiu REQ-17, proveu d’editar-lo, creeu l’esborrany de Jira i proveu la transició cap a Aprovat. Els resultats esperats són requisit llegible, edició denegada, proposta creada i aprovació denegada. Compareu les versions de la font abans i després de la denegació.

**Com a usuari exclòs**, obriu una pàgina sintètica amb restriccions separades. No hi hauria d’haver accés al contingut. Proveu les pàgines filles per separat. No enganxeu el text protegit al xat de l’usuari exclòs per esquivar el control.

## Adaptar el mapa del repositori

**Manteniu estables els ID de les fonts quan canvia la ubicació.** REQ-17 continua indicant la intenció de retenció aprovada, però en la ruta mixta la seva font és una pàgina Confluence. Una captura del repositori ajuda amb les comprovacions i revisions. No substitueix la pàgina com a font d’autoritat.

| Registre | Font d’autoritat | Tractament al repositori |
|---|---|---|
| **REQ-17** | Pàgina de requisits Confluence associada | Captura amb proves de revisió de la pàgina |
| **RUN-04** | Pàgina de manual Confluence associada | Fragment operatiu capturat per mantenir la coherència |
| **POL-01** | Política protegida a GitHub | Les instruccions compartides dels agents hi fan referència |
| **Configuració** | Registre protegit a GitHub | Diferència d’implementació proposada |
| **Lliurament** | Element de treball de Jira | Enllaç de correlació, no còpia de la política |

**Afegiu la procedència a les captures.** Al paquet privat de la proposta, registreu l’ID de la font, la referència i la versió de la pàgina, l’hora de captura i el rol que l’ha capturada. No inclogueu identificadors natius de pàgina en els treballs públics del curs. Si l’editor troba una altra versió actual, concilieu-la abans d’utilitzar la captura.

**No canvieu el nom de l’autoritat per adaptar-lo a l’eina.** La descripció editable de Jira facilita el debat, però continua sent un registre de lliurament. Una frase de trenta dies a Jira no substitueix un requisit de set dies a Confluence.

## Dissenyar les proves d’accés

**Separeu la lectura, la preparació d’esborranys i la publicació.** Un col·laborador necessita prou accés per entendre el requisit sintètic i enviar una proposta. No necessita permís d’edició a la pàgina de referència ni permís per aprovar la seva pròpia proposta.

```text
Test record: PERM-REQ-EDIT
Role: contributor
Source: REQ-17
Precondition: source is readable, published revision captured
Attempt: edit the authoritative requirement
Expected: edit denied, published revision unchanged
Observed: fill from the sandbox
Evidence: native result and independent revision read-back
Reviewer: administrator or independent permission reviewer
```

**Feu servir un registre separat per a la lectura denegada.** El fet que el col·laborador pugui llegir el requisit comprova la separació entre publicació i edició. Que l’usuari exclòs no pugui obrir la pàgina comprova la confidencialitat. Ajuntar-ho en una fila amaga quin límit s’ha provat.

**Comproveu també els accessos permesos.** Els responsables i editors han de poder seguir la ruta assignada. Si tothom rep una denegació, el sandbox és restrictiu però inutilitzable. Conserveu una edició autoritzada correcta en una pàgina de prova d’un sol ús, sense alterar el requisit aprovat mentre diagnostiqueu els permisos.

## Assajar la revisió de Jira

**Tracteu els noms dels estats com el disseny d’aquest pilot.** Esborrany conté una sol·licitud. Revisió conté un paquet congelat. Aprovat indica que els responsables han acabat la revisió. Publicació indica que el lliurament encara no s’ha completat. Fet requereix una comprovació de lectura. Bloquejat indica manca de proves o d’accés, o un conflicte sense resoldre.

| Transició | Paquet necessari | Comprovació responsable |
|---|---|---|
| **Esborrany a Revisió** | Proposta fixa i versions de les fonts | El col·laborador en confirma la integritat |
| **Revisió a Aprovat** | Decisions de producte i operacions | La persona autoritzada comprova els dos rols |
| **Aprovat a Publicació** | Comparació amb les fonts actuals | L’editor confirma que les bases no han canviat |
| **Publicació a Fet** | Registre complet per sistema | El responsable del lliurament comprova la lectura de retorn |
| **Qualsevol pas admès a Bloquejat** | Error i acció pendent | Responsable de recuperació assignat |

**Assageu-ho amb un paquet sintètic incomplet.** Envieu només una revisió de producte i demaneu a la persona autoritzada que valori la transició. S’espera que deixi la feina a Revisió i demani la revisió d’operacions. Això prova el pas procedimental per separat de la denegació de la plataforma al col·laborador.

**Proveu deliberadament les rutes alternatives.** A la vista del flux de treball del sandbox, inspeccioneu totes les rutes cap a Aprovat i Fet. Una transició restringida i amb nom no és suficient si una altra ruta disponible esquiva el mateix límit de revisió. Registreu les rutes revisades i l’usuari emprat, en lloc d’afirmar que un sol clic n’ha cobert totes.

## Diagnosticar accessos inesperats

**Comenceu per la identitat efectiva.** Confirmeu que la sessió del navegador pertany al rol de prova previst. Després, inspeccioneu membres de grup, permisos d’espai, accés a pàgines i associació del flux amb les eines d’administració del producte. No canvieu diversos controls alhora, perquè la denegació perdrà valor diagnòstic.

1. **Confirmeu la identitat:** feu servir sessions separades per al col·laborador, l’editor i l’usuari exclòs.
2. **Localitzeu la concessió:** identifiqueu la pertinença o el paràmetre que permet l’acció provada.
3. **Ajusteu el control del laboratori:** manteniu l’accés legítim dels responsables.
4. **Repetiu el mateix intent:** després de la denegació, captureu la versió de la font sense canvis.
5. **Repetiu el cas positiu:** confirmeu que la publicació autoritzada encara funciona.

**Llista final de proves:** registreu l’arbre de pàgines Confluence i els ID associats, l’associació de l’esquema Jira del laboratori, l’associació del flux, les pertinences de cada rol de prova als grups, una lectura permesa del requisit, una edició denegada amb la versió sense canvis, la creació permesa d’un esborrany, una transició cap a Aprovat denegada amb l’estat sense canvis, la lectura denegada de l’usuari exclòs i la persona responsable de la neteja. Per a cada fila, conserveu el rol de l’actor, la versió o estat inicial i final, el resultat natiu i la persona revisora independent. Registreu la ruta de navegació observada al tenant, perquè les etiquetes i els controls disponibles varien segons el pla.

**Comprovació final:** lliureu les pàgines de referència mapejades, el flux només per al laboratori, la matriu de rols prevista i els registres de permisos observats. Si el pla no té un control necessari, deixeu la fila corresponent Bloquejada. La lliçó de publicació pressuposa que les proves han tingut èxit, no només que hi ha captures de configuració.

## Resolució de problemes i reversió

**El col·laborador encara pot editar:** reviseu l’accés a la pàgina, els permisos d’espai i les pertinences. **La transició encara funciona:** reviseu l’associació del flux i les rutes alternatives. **Falten opcions:** comproveu el tipus de gestió, l’edició i els permisos d’administració.

**Reversió:** elimineu els permisos dels connectors i archiveu els esborranys. Desconnecteu els esquemes i fluxos només del laboratori després de conservar les proves. Restaureu la redacció aprovada de la pàgina amb l’historial revisat o una correcció compensatòria. No elimineu les proves d’auditoria.

## Exercici i autoavaluació

**Jira diu trenta dies mentre que REQ-17 en diu set.** Identifiqueu l’entrada d’implementació i el responsable de resoldre la diferència.

**Raonament esperat:** Confluence determina la intenció. Jira conté un error de proposta o de lliurament. Atureu la publicació i demaneu al responsable de producte que resolgui la diferència, en lloc d’escollir la marca de temps més recent.

## Referències principals

- **Restriccions i pla:** [permisos de Confluence](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Controls per compartir:** [accés a contingut específic](https://support.atlassian.com/confluence-cloud/docs/add-or-remove-page-restrictions/).
- **Administració d’esquemes:** [esquemes de permisos de Jira](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).
- **Condicions de transició:** [fluxos de treball avançats](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).

## Passos següents

**Quan les proves d’accés hagin tingut èxit, continueu amb [Publicació entre sistemes](/articles/ai-collaboration-confluence-jira-publication/)**.
