---
title: "Capstone de col·laboració amb IA: GitHub, Confluence i Jira"
date: 2026-10-01
lastmod: 2026-11-13
toc: true
draft: false
description: "Executa un canvi de retenció sintètic amb fluxos de treball GitHub-first i Confluence/Jira, evidència de fallades i revisió independent."
genre: ["Intel·ligència artificial", "Col·laboració d'equips", "Enginyeria de programari"]
tags: ["curs de col·laboració amb IA", "proposta de retenció", "revisió de GitHub", "flux Confluence Jira", "matriu de fallades", "acceptació independent"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Il·lustració de professionals que revisen treball compartit en un espai de ciberseguretat"
coverCaption: ""
---

[Torna al curs de col·laboració amb IA](/ai-collaboration-course-start/)

**Lliura PROP-042 dues vegades**, primer amb GitHub-first i després amb GitHub, Confluence i Jira. Tu contribueixes, propietaris separats revisen i els editors autoritzats apliquen el canvi. Fes servir sandbox sintètics aïllats després de les lliçons anteriors. El capstone prova el procediment complet, incloent-hi el rebuig, la recuperació i el traspàs independent. No prova només la qualitat de la prosa de l’assistent.

## Idees clau

- **Un canvi compartit** compara els dos models d’autoritat.
- **Les proves negatives** importen tant com el lliurament correcte.
- **Els paquets d’evidència** permeten la revisió independent.
- **Completar el laboratori** no autoritza el desplegament en producció.

## Abans de començar

**Prerequisits:** [mòduls anteriors del curs](/ai-collaboration-course-start/), accés aprovat al sandbox i revisors separats. **Temps previst:** de vuit a dotze hores en diverses sessions, més la revisió independent. El temps real depèn de la configuració del compte i de les reparacions. **Dificultat:** avançada.

**Artefactes requerits:** carta, mapa, política, adaptadors, línia base, manifest, proposta fixada, revisions dels propietaris, llibre major, registre de recuperació i traspàs. Les permisos que depenen del pla i no existeixen bloquegen el completament. No es converteixen en aprovacions assumides.

**Prepara un directori d’evidència per pista abans de provar.** El revisor ha d’identificar l’actor, les revisions d’origen, l’acció intentada, el resultat observat i l’estat final sense dependre d’un resum de xat.

## Estableix dues línies base

1. **Crea execucions aïllades** amb els noms GitHub-first i Mixed. Mantén separades les revisions i les ressenyes.
2. **Restaura la línia base de set dies** mitjançant el procediment aprovat de cada pista i captura les revisions resultants.
3. **Verifica els controls de denegació** amb comptes de contribuent i d’usuari exclòs.
4. **Captura el context actual** i confirma l’acord entre adaptador i política.
5. **Declara l’abast:** retenció de trenta dies d’una exportació sintètica, excloent dades reals, còpies de seguretat i retencions legals.

**PROP-042 és una etiqueta de correlació, no una aprovació reutilitzable.** Cada execució necessita la seva revisió congelada i la seva evidència d’origen. Inclou els identificadors d’execució als informes.

## Lliura amb GitHub-first

**Obre l’Issue i el PR candidat** amb les lliçons de GitHub. Canvia alhora el requisit, la configuració, la proposta i el runbook. Captura la base protegida, executa les comprovacions fiables i obtén les revisions de producte i operacions en el commit final.

```text
Execució: GitHub-first
Canvi: retenció sintètica 7 -> 30 dies
Requisit: REQ-17 revisió 2
Configuració: retention_days 30
Runbook: termini de retenció: 30 dies
Proposta: revisió base 1, de 7, a 30
Manifest: hashes de les fonts protegides abans del canvi
Revisió: revisions de producte i operacions sobre la versió final de la proposta
Publicació: commit fusionat i lectura de verificació
Límit: no s’ha provat cap servei d’eliminació en execució
```

**Omple les referències reals des del sandbox.** L’esquema és un mapa esperat, no una evidència completa. El mantenidor només fa merge després de la revisió i després llegeix **`main`** de manera independent. Tanca l’Issue quan hagis enllaçat els registres finals.

## Lliura la pista mixta

**Llegeix les versions de Confluence i congela la proposta de Jira.** Obté les dues revisions dels propietaris. Publica el requisit com a pendent de lliurament, fes merge de la configuració, publica el runbook i torna a llegir tots els sistemes abans de Done.

**Registra cada publicació** amb evidència de versió de pàgina, commit o transició. Les còpies del requisit al repositori són instantànies. El verificador local no demostra l’autoritat actual de Confluence.

| Comparació | GitHub-first | Espai de treball mixt |
|---|---|---|
| **Requisit** | Revisió d’un repositori protegit | Publicació revisada pel propietari de Confluence |
| **Coordinació** | Issue/PR | Proposta de Jira fixada |
| **Unitat de publicació** | Merge del repositori | Escriptures de pàgina separades i merge |
| **Actualitat** | Commit protegit | Versions de pàgina més commit |
| **Recuperació** | Revert o compensació revisats | Compensació guiada pel llibre major |

**Tria el flux segons les necessitats de propietat.** GitHub-first redueix la coordinació entre sistemes. La pista mixta conserva els espais de treball i afegeix controls de publicació i accés.

## Executa la matriu de fallades

| Cas | Injecció | Evidència observada requerida |
|---|---|---|
| **Canvi aprovat** | Envia una proposta de trenta dies revisada | Lectura coherent i revisió |
| **Context obsolet** | Canvia l’origen després de capturar-lo | Rebuig, reconciliació i nova aprovació |
| **Escriptura no autoritzada** | El contribuent publica | Denegació i revisió sense canvis |
| **Conflicte** | Jira diu seixanta, Confluence set | Bloqueig i reconciliació del propietari |
| **Publicació parcial** | Interromp després d’una escriptura | Llibre major pendent i recuperació |
| **Accés denegat** | Retira l’accés de lectura de la tasca | Cap text protegit ni publicació |
| **Recuperació** | Compleció o desfer aprovat | Noves revisions revisades |
| **Traspàs** | Una sessió nova rep només mapa i llibre major | Lectura nova i acció següent correcta |

**El conflicte entre sistemes pertany a Mixed.** A GitHub-first, prova un Issue que contradigui el fitxer aprovat. Executa els altres casos aplicables en les dues pistes. Una fallada del validador local no substitueix l’evidència de permisos en directe.

| Cas i fitxer d’evidència | Execució GitHub-first | Execució Mixed |
|---|---|---|
| **Canvi aprovat** `01-approved-change.md` | PR revisat i lectura posterior | Pàgines revisades, merge i llibre major |
| **Context obsolet** `02-stale-context.md` | Canvia la base protegida després de capturar-la | Canvia una pàgina d’autoritat després de capturar-la |
| **Escriptura no autoritzada** `03-unauthorized-write.md` | Denegació del push directe | Denegació d’edició i transició |
| **Conflicte** `04-conflict.md` | L’Issue contradiu el fitxer | El text de Jira contradiu Confluence |
| **Publicació parcial** `05-partial-publication.md` | Atura abans del merge o la lectura | Atura després d’una pàgina |
| **Accés denegat** `06-access-denial.md` | Retén un origen protegit | Exclou un usuari d’una pàgina restringida |
| **Recuperació** `07-recovery.md` | Revert o compleció revisats | Compensació guiada pel llibre major |
| **Traspàs** `08-handoff.md` | Sessió nova llegeix fitxers protegits | Sessió nova llegeix pàgines i llibre major |

**Crea cada fitxer abans de la prova.** Registra el resultat esperat i observat, el rol de l’actor, les revisions inicial i final, la referència d’evidència nativa i la decisió del revisor. Mantén separats els directoris de les dues pistes.

**Separa els resultats esperats dels observats.** Per a cada cas registra l’ID d’execució, el rol, les revisions inicials, l’acció intentada, l’expectativa, l’observació, les revisions resultants i la decisió. Redacta credencials i identificadors de compte dels informes compartits.

## Avalua la compleció

**L’aprovació requereix evidència observada per a cada fila aplicable** i acceptació independent. Els revisors comproven permisos, actualitat de l’origen, revisió del rol, publicació parcial i reconstrucció del traspàs.

**Falla immediatament** davant una publicació no autoritzada, text denegat que arriba al model o sobreescriptura silenciosa d’una base canviada. Mantén el treball bloquejat fins que els controls corregits passin una repetició. No compensis aquestes fallades amb altres resultats.

**Mesura casos completats i bloquejats, propostes obsoletes rebutjades, escriptures denegades, recuperacions i temps del revisor.** Els resultats proposats continuen sent esperats fins que s’observen.

## Planifica les dues execucions

**No reutilitzis una aprovació entre pistes.** El valor és el mateix, però canvien els espais d’origen, les revisions capturades, els permisos i la seqüència de publicació. Dona a cada execució el seu directori d’evidència i paquet de revisió.

```text
capstone-evidence/
  github-first/
    charter-and-map
    captured-sources
    fixed-proposal
    role-reviews
    consistency-results
    permission-results
    publication-readback
    recovery-and-handoff
  mixed/
    les mateixes categories d’evidència, recollides de manera independent
```

**Aquests noms són un exemple d’organització**, no fitxers d’arxiu subministrats. Desa l’evidència real de manera privada al sandbox aprovat. Els lliuraments compartits han d’usar rols i referències redactades.

**Assigna un observador abans de les fallades.** El contribuent fa l’acció intentada. L’observador registra l’estat inicial, el resultat i l’estat final. Un revisor posterior decideix si l’evidència sosté l’afirmació. Declara el solapament de rols.

## Executa les fallades de manera aïllada

**Restableix un estat revisat i verificat entre casos.** Injectar deriva d’origen, revocació d’accés i desajust del runbook alhora amaga quin control ha rebutjat la proposta. Una fallada per execució dona al revisor una causa traçable.

1. **Captura l’estat inicial:** revisions, configuració, estat de lliurament i rol.
2. **Aplica una injecció sintètica:** canvia una condició mitjançant una ruta de prova autoritzada.
3. **Intenta l’acció limitada:** validació, lectura, publicació o traspàs.
4. **Registra l’observació:** sortida real i estat resultant.
5. **Repara amb revisió:** conserva l’evidència abans de restaurar els controls.
6. **Repeteix el cas positiu:** confirma que el flux corregit encara lliura el treball permès.

**Targeta d’injecció i restabliment per a cada cas:** abans del cas següent, fes servir una proposta sintètica nova o restaura una base revisada. La persona observadora registra la precondició i confirma el restabliment. No esborris mai l’intent fallit del registre.

| Cas | Injecció i comprovació: GitHub-first | Injecció i comprovació: Mixed | Restabliment abans del cas següent |
|---|---|---|---|
| Canvi aprovat | Envia el PR fixat, obtén les dues revisions, fusiona’l i torna a obrir `main` | Publica REQ-17, fusiona el diff revisat, publica RUN-04 i torna a llegir els registres | Desa les revisions finals com a nova base |
| Context obsolet | Captura un manifest i canvia la base de prova amb un PR revisat separat abans de validar la proposta antiga | Captura les versions de les pàgines i fes que un editor autoritzat canviï una pàgina de prova abans de la lectura prèvia a l’escriptura | Atura’t, compara versions, captura fonts noves i revisa un paquet nou |
| Escriptura no autoritzada | Contributor intenta un push directe innocu a `main` protegit i desa la denegació del servidor | Contributor intenta editar REQ-17 i fer la transició a Approved | Torna a llegir el commit, la versió de la pàgina i l’estat de Jira per confirmar que no han canviat |
| Conflicte | L’esborrany de l’Issue diu seixanta dies i el fitxer aprovat en diu set | L’esborrany de Jira diu seixanta dies i REQ-17 en diu set | La persona responsable de producte concilia l’esborrany i registra la decisió |
| Publicació parcial | Atura’t després de l’aprovació i abans de fusionar o rellegir; deixa l’Issue obert | Atura’t després de rellegir REQ-17 mentre la configuració i RUN-04 encara indiquen set | Mantén el lliurament pendent i obtén una decisió revisada per completar o compensar |
| Accés denegat | Una identitat de prova exclosa intenta llegir una font sintètica d’un repositori privat de prova | La identitat exclosa intenta accedir a una pàgina sintètica restringida | Restaura només l’accés de prova aprovat i comprova que el lector habitual encara hi accedeix |
| Recuperació | Interromp un canvi de prova aprovat i proposa completar-lo o revertir-lo amb revisió | Fes servir el registre de publicació parcial per proposar completar-la o compensar-la amb revisió | Torna a llegir cada font i concilia el registre |
| Traspàs | Envia MAP-01 i el registre a una persona revisora nova sense el xat anterior | Envia els ID de les pàgines mapejades i el registre a una persona revisora nova sense el xat anterior | La persona revisora obre les fonts actuals i anota el pas següent autoritzat |

En cada cas denegat, registra la resposta de la plataforma i torna a llegir el registre protegit. Per al cas de l’usuari exclòs, consulta les traces d’eines, els registres de recuperació o les dades d’auditoria del proveïdor per comprovar si el text protegit va arribar a la tasca. Si no hi ha aquestes proves, marca com a Bloquejada la comprovació de seguretat d’accés; una denegació visible no demostra que no s’hagi retornat un fragment en memòria cau. Si el pla no inclou el control o falta una identitat de prova autoritzada, marca Bloquejat en lloc de simular un aprovat.



**Una fallada planificada continua sent una observació de fallada.** No anomenis exitosa una publicació no autoritzada perquè volies provar-la. La prova ha exposat un defecte, però el límit de publicació ha fallat.

## Interpreta un resultat mixt

**Paquet d’evidència il·lustratiu:** la coherència local passa, producte i operacions revisen el paquet fixat, la publicació del requisit passa i l’edició del runbook és denegada. La configuració encara no ha fet merge. Jira continua bloquejat.

| Afirmació | Veredicte | Motiu |
|---|---|---|
| **Els registres candidats coincideixen** | Recolzat per la comprovació local | Els registres han passat les comparacions |
| **Els propietaris han acceptat la intenció i operacions** | Requereix revisions natives fixes | Les etiquetes de rol no són suficients |
| **Lliurament de trenta dies complet** | No recolzat | Les publicacions requerides continuen pendents |
| **El límit funciona per a cada rol** | No recolzat | Una denegació té un abast limitat |
| **El propietari de recuperació ha d’actuar** | Recolzat com a pas següent | El lliurament parcial necessita una decisió revisada |

**Raonament esperat:** mantén l’execució incompleta, verifica les fonts actuals i demana la decisió del propietari corresponent. No afebleixis permisos ni descriguis la comprovació de la instantània com a evidència de publicació en directe.

**Paquet pedagògic de Mixed, sintètic i sense dades d'un client:**

```text
Execució: MIXED-042-example
Base capturada: REQ-17 v4 = 7 dies; RUN-04 v2 = 7 dies.
GitHub main base-001 config.json = {"retention_days": 7}; Jira PROP-042 r1 = In Review.
Proposta fixada: REQ-17 v5 estableix 30 dies per a les exportacions sintètiques. Exclou dades de producció, còpies de seguretat i retencions legals.
GitHub config.json canvia retention_days de 7 a 30. RUN-04 v3 indica 30 dies; al laboratori no s’executa cap servei d’eliminació. La publicació incompleta queda pendent.
Revisió: el responsable de producte aprova el text exacte de REQ-17. Operacions aprova el diff de configuració i el runbook a r1.
Publicació: qui publica rellegeix REQ-17 v5 i RUN-04 v3, tots dos amb 30 dies; manteniment llegeix main a merge-002 amb retention_days 30.
Acció denegada: es denega al col·laborador editar REQ-17 v5. Qui publica confirma que no ha canviat; qui observa desa la prova de la plataforma.
Recuperació: falla un intent de RUN-04 i Jira continua Blocked. Operacions autoritza un altre intent; després de rellegir v3, Jira passa a Done.
Relleu: una persona revisora nova rep MAP-01 i el registre, llegeix les tres fonts i Jira, i anota els 30 dies i la mancança d’execució.
Límit: només es demostra la publicació de les fonts. Temps d’eliminació: no executat.
```

## Revisa amb un lector independent

**Demana al revisor que reconstrueixi els esdeveniments**, no que només llegeixi la conclusió. Ha de trobar la base aprovada, la proposta fixada, les decisions, les revisions resultants, les fallades, la reparació i les mancances sense la teva narració.

```text
Preguntes de revisió independent:
Quina font regeix la intenció de retenció en aquest flux?
Quin paquet exacte ha revisat cada responsable?
Ha canviat cap font després de la revisió?
Què s’ha publicat i què continua pendent?
Quina acció denegada s’ha observat i amb quin rol?
Ha arribat text protegit al context d’un usuari exclòs?
Quina reparació s’ha revisat i rellegit?
El nou relleu reconstrueix l’estat actual de manera independent?
```

**Puntua cada requisit per separat.** Usa Supported, Failed, Blocked o Not run amb una referència d’evidència. Coherència, aprovació, permisos, recuperació i traspàs són requisits diferents.

```text
ID i flux d’execució:
Rol de revisió i data:
Cas 01 canvi aprovat: estat ___ prova ___ mancança ___
Cas 02 context obsolet: estat ___ prova ___ mancança ___
Cas 03 escriptura no autoritzada: estat ___ prova ___ mancança ___
Cas 04 conflicte: estat ___ prova ___ mancança ___
Cas 05 publicació parcial: estat ___ prova ___ mancança ___
Cas 06 accés denegat: estat ___ prova ___ mancança ___
Cas 07 recuperació: estat ___ prova ___ mancança ___
Cas 08 relleu: estat ___ prova ___ mancança ___
Decisió general: Justificada / Fallida / Bloquejada / No executada
Rol responsable següent i acció:
```

**Supported significa que el revisor ha trobat evidència observada per a cada cas aplicable.** Registra Failed davant una fallada observada, Blocked si falta accés o control i Not run si no s’ha intentat.

**Porta de pas del curs:** completa les pistes GitHub-first i Mixed. En cada pista, els vuit casos aplicables han de ser Supported. Una frontera Failed o una lectura nativa absent bloqueja la pista. Una sola pista completa és un resultat parcial documentat.

**Paquet de model redactat, només il·lustratiu:**

```text
Flux: github-first | Execució: G-01 | Revisor: rol pilot independent
Base: commit protegit base-001 | Proposta fixada: PROP-042 r1
Aprovacions: revisió de producte P-01, revisió d’operacions O-01
Coherència: comprovació local superada, resultat C-01 desat
Permís: push directe del col·laborador denegat, esdeveniment D-01
Publicació: commit merge-002; un clon nou confirma 30 dies
Excepció: còpies de seguretat i retencions legals excloses
Recuperació: interrupció R-01 rellegida i resolta amb revisió
Relleu: la segona persona troba la base actual, l’excepció i el pas següent
Límit d’execució: no afirma eliminació ni desplegament en producció
Decisió: justificada només per al flux sintètic GitHub-first
```

Substitueix cada referència il·lustrativa per un artefacte observat del sandbox. Repeteix el paquet complet per a Mixed amb les seves versions i revisions. El revisor ha de rebutjar una aprovació GitHub copiada dins del paquet Mixed.

## Escriu una decisió limitada

**Una decisió final útil anomena el pilot següent**, no un desplegament sense límits. Tria una altra configuració d’exportació sintètica amb els mateixos rols i ruta de consulta directa. Mantén les dades reals i la publicació automàtica fora de l’abast.

| Element de decisió | Detall requerit |
|---|---|
| **Abast** | Un canvi següent i les seves exclusions explícites |
| **Evidència** | Casos Supported i fallades sense resoldre |
| **Controls** | Requisits imposats per la plataforma i procediment separats |
| **Propietaris** | Rol responsable de cada buit pendent |
| **Buit d’execució** | Comportament de supressió o desplegament no provat |
| **Condicions d’aturada** | Accés absent, autoritat canviada, publicació no autoritzada |

**Comprovació de compleció:** els dos paquets superen la reconstrucció independent, els casos aplicables tenen evidència observada i els controls pendents continuen visibles. Si només completes GitHub, informa de compleció parcial.

## Resolució de problemes i backout

**Només evidència del camí feliç:** repeteix les proves de denegació i interrupció. **Rols solapats:** declara-ho i repeteix amb usuaris separats. **Controls de pla absents:** atura’t i obtén un sandbox aprovat.

**Backout:** restaura la línia base amb PR revisats i edicions de Confluence, revoca integracions temporals, arxiva l’evidència Jira i fes la neteja sintètica aprovada després de conservar l’evidència. Preserva l’historial de recuperació.

## Crea la decisió de desplegament

```text
Decisió: un altre pilot sintètic, bloquejat o rebutjat
Proves: els dos paquets d’execució i la matriu de fallades
Requisits no aplicats: enumereu explícitament els controls procedimentals
Revisió del proveïdor: abast de les entrades i retenció
Responsabilitats: producte, operacions, política, repositori, lliurament
Mancances de producció: proves d’execució, secrets, desplegament, revisió d’accés
Pas següent: seguiment acotat amb un rol responsable
Data de revisió: assignada pels responsables del pilot
```

**Raonament esperat:** l’èxit sintètic permet un altre pilot limitat. Producció requereix aprovació separada per a dades reals, desplegament, tractament del proveïdor i comportament d’execució. Una resposta correcta de l’assistent no és autorització de desplegament.

## Referències principals

- **Controls del repositori:** [Branques protegides](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Accés de l’espai de treball:** [Permisos de Confluence](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Controls de lliurament:** [Esquemes de permisos de Jira](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).

## Passos següents

**Torna al [centre del curs](/ai-collaboration-course-start/)** per revisar els controls absents. Compara la teva implementació amb l’[article del marc](/articles/one-source-many-tools-ai-collaboration-framework/) abans de triar un altre pilot.
