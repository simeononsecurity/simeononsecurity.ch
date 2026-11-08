---
title: "Recuperació de la deriva dels agents d’IA i flux de traspàs"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Detecta fonts i adaptadors de polítiques obsolets, recupera publicacions interrompudes i verifica traspassos independents entre agents."
genre: ["Intel·ligència artificial", "Col·laboració en equip", "Enginyeria de programari"]
tags: ["curs de col·laboració d’IA", "deriva de fonts", "recuperació de publicació", "traspàs entre agents", "verificació de fonts actuals", "compensació"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Il·lustració de professionals que revisen plegats la feina d’un projecte en un espai de ciberseguretat"
coverCaption: ""
---
[Torna al curs de col·laboració d’IA](/ai-collaboration-course-start/)

**Comprova si hi ha deriva abans de les tasques i després d’una publicació interrompuda.** Compara les versions de les fonts, les dels adaptadors i l’estat de lliurament al repositori o a l’entorn de treball aïllat. Fes-ho després de completar un itinerari. Així evites que els resums antics es converteixin en autoritat vigent i conserves un historial de recuperació revisable.

## Punts clau

- **La deriva de les fonts** és diferent de la deriva dels adaptadors.
- **Una publicació parcial** requereix un registre per sistema.
- **La recuperació** conserva l’historial juntament amb els canvis revisats.
- **Els traspassos** exigeixen que una altra persona llegeixi independentment les fonts actuals.

## Abans de començar

**Requisits previs:** el [flux de GitHub al navegador](/articles/ai-collaboration-github-browser-workflow/) o el [flux de publicació mixt](/articles/ai-collaboration-confluence-jira-publication/). **Temps estimat:** de 60 a 90 minuts. **Dificultat:** revisió avançada.

**Seguretat:** fes servir només registres sintètics. Atura la publicació automàtica abans de les proves de recuperació. No s’hi proporciona cap servei d’eliminació en execució.

**Resultat per al lector:** acaba amb un inventari de l’estat, una decisió de la persona responsable, una reparació revisada i un traspàs que una altra persona pugui reconstruir a partir de fonts actuals. Completar l’exercici no autoritza la publicació.

## Classifica la deriva

| Deriva | Senyal | Responsable de la reparació |
|---|---|---|
| **Requisit** | La font difereix del manifest | Responsable del producte |
| **Política** | L’adaptador difereix de POL-01 | Responsable de la política |
| **Implementació** | La configuració contradiu la intenció | Mantenidor |
| **Runbook** | Les instruccions contradiuen el comportament aprovat | Responsable d’operacions |
| **Accés** | Es denega la lectura d’una font abans accessible | Administrador, tasca aturada |
| **Lliurament** | Marcat com a complet sense registre complet | Responsable del lliurament |

**El text més recent no és necessàriament una autoritat aprovada.** Una edició recent no autoritzada requereix una investigació, no una adopció automàtica. Determina l’estat i qui n’és responsable abans de copiar valors.

## Executa la comprovació prèvia

```text
Read MAP-01 and capture its revision.
Read POL-01 and compare active adapter versions.
Read REQ-17 and RUN-04 from mapped homes.
Read config.json at protected main.
Read frozen proposal and current role reviews.
Compare current sources with reviewed bases.
List mismatches, denied reads, and pending publications.
Stop consequential writes until owners resolve each mismatch.
```

**La persona col·laboradora fa la comprovació prèvia abans de redactar. Qui publica la repeteix abans d’escriure.** Desa la comparació de versions amb la proposta. Les comprovacions setmanals complementen aquestes lectures, però no les substitueixen.

**Exemple de deriva de l’adaptador:** POL-01 arriba a la versió 2 mentre CLAUDE.md encara indica la versió 1. Atura’t, llegeix el canvi de política revisat, actualitza l’adaptador mitjançant una PR protegida i inicia una sessió nova. Canviar només el número de versió sense carregar la política no corregeix el context.

**Introdueix una deriva de font al laboratori fora de línia:** extreu una còpia nova del ZIP proporcionat en un directori temporal buit. Des de l’arrel, copia `baseline/` a `candidate/`, executa `python3 check.py capture --base baseline > candidate/context.json` i, tot seguit, `python3 check.py validate --base baseline --candidate candidate`. Anota el primer resultat `PASS`. Obre `baseline/requirement.json` en un editor de text i canvia només `"retention_days": 7` per `"retention_days": 8`. Torna a executar la mateixa ordre validate. S’espera un codi de sortida diferent de zero i el missatge `STALE_CONTEXT: capture the trusted base again`. Anota les dues sortides i el camí de la font modificada. Elimina aquesta extracció temporal després de desar les proves privades i extreu una còpia nova per reiniciar l’entorn. No apliquis el canvi a vuit dies al repositori publicat ni consideris una captura nova com una aprovació de la persona responsable.

**Introdueix una deriva de l’adaptador al repositori temporal:** en una branca nova de proposta, copia a CLAUDE.md el text aprovat de l’adaptador POL-01 versió 1 i etiqueta’l com a versió 1. En una proposta de política separada i revisada, descriu el canvi a la versió 2 amb una condició d’aturada nova i concreta. Deixa l’adaptador a la versió 1. Demana a una persona revisora que compari els dos registres i marqui l’adaptador com a obsolet abans de qualsevol merge o execució de l’agent. Reinicia tancant les propostes de prova o actualitzant l’adaptador en una PR revisada. Després obre una sessió nova i verifica les dues versions i la condició d’aturada nova. Conserva els diff antics i corregits. És una prova de documentació, no una simulació de rebuig de la plataforma.

## Recupera una publicació interrompuda

1. **Atura la publicació de PROP-042** i assigna la responsabilitat de la recuperació.
2. **Llegeix l’estat real** en tots els sistemes participants. Distingeix entre accions completades, fallides i no intentades.
3. **Demana al producte que triï** entre completar, fer una reversió revisada o mantenir-ho en espera.
4. **Prepara una proposta de recuperació** amb bases actuals i conserva l’abast i les excepcions, tret que es revisin explícitament.
5. **Aplica un pas revisat cada vegada**, enregistrant i tornant a llegir cada resultat.
6. **Verifica l’estat final** i els límits pendents abans de reprendre la feina habitual.

```yaml
recovery_id: RECOVERY-042
proposal_id: PROP-042
mode: awaiting-owner-choice
illustrative_state:
  requirement: thirty-days-published
  implementation: seven-days-on-main
  runbook: seven-days
  delivery: blocked
choices:
  forward: finish approved implementation and runbook
  backout: restore baseline through reviewed changes
  hold: wait for evidence or access
```

**Substitueix els estats il·lustratius per revisions i valors observats.** Una entrada antiga del registre o una afirmació de l’assistent no demostra que s’hagi tornat a llegir el resultat.

| Opció | Quan fer-la servir | Límit |
|---|---|---|
| **Completar** | L’aprovació continua vigent i les fonts concorden | Requereix una verificació actualitzada |
| **Revertir** | La persona responsable retira el canvi o falla la implementació | No recupera dades eliminades |
| **Mantenir en espera** | Falten proves o accés | El lliurament continua incomplet |

**Tria l’espera si falten proves.** Els exercicis sintètics no justifiquen sobreescriptures a cegues. Indica el rol següent i les proves que falten.

**La recuperació a GitHub** fa servir un revert o una compensació revisats. **La recuperació a Confluence** compara l’historial i aplica una restauració o compensació revisada. **La recuperació a Jira** conserva l’historial de la proposta i torna a obrir o bloqueja el lliurament. Llegeix les revisions resultants en lloc de suposar que la numeració de l’historial es reinicia.

## Verifica un traspàs independent

```text
Handoff: HANDOFF-042
Task: PROP-042
Map and policy: attach current approved revisions
Evidence: requirement, runbook, configuration references
Ledger: completed, failed, pending
Decision: owner choice and fixed proposal revision
Limits: no runtime deletion test or production data
Next role: accountable role
Next action: one bounded step
Stop: changed base, access denial, conflicting authority
```

**Obre una altra eina o una sessió neta** amb el mapa i el traspàs, no amb la conversa anterior. Exigeix lectures noves de les fonts, un manifest nou i que s’identifiqui l’acció pendent. Les proves manuals del navegador continuen sent vàlides si s’etiqueten com a instantània i es tornen a comprovar abans d’escriure.

**Traspàs negatiu:** denega l’accés a REQ-17. Espera un bloqueig explícit, no un valor deduït ni un fragment privilegiat. Restaura només l’accés aprovat mitjançant l’administració i repeteix la verificació.

## Diagnostica abans de reparar

**Comença amb un inventari de l’estat.** «Els assistents discrepen» descriu un símptoma de la resposta, no el problema subjacent de la font. Llegeix per separat el requisit mapejat, la configuració, el runbook, la política i el registre de lliurament abans de demanar a cap assistent que els repari.

| Observació | Diagnòstic | Primera acció |
|---|---|---|
| **Les dues fonts concorden, la resposta antiga difereix** | Context de resposta obsolet | Reconstrueix a partir de lectures actuals |
| **Requisit trenta, configuració set** | Desajust de lliurament o implementació | Revisa el paquet aprovat i el registre |
| **Adaptador u, política dos** | Desajust de versió de les instruccions | Llegeix el canvi de política i repara l’adaptador |
| **Font abans llegible, ara denegada** | Canvi d’accés | Atura la tasca i demana una revisió autoritzada |
| **Registre complet, runbook set** | Tancament sense una lectura de retorn vàlida | Torna a obrir o bloqueja el lliurament i investiga |

**No tractis cada desajust com un problema del model.** Actualitzar una sessió corregeix el context obsolet de la conversa. No publica un runbook, no restaura un permís absent ni concilia decisions contradictòries entre responsables. Identifica qui farà la reparació abans de triar una acció a l’eina.

## Aplica la compensació

**Interrupció il·lustrativa:** REQ-17 conté la intenció aprovada de trenta dies i el lliurament està pendent. La configuració i el runbook encara indiquen set dies. El mantenidor comunica una fallada d’implementació no resolta. El producte tria restaurar en lloc de continuar.

1. **Registra les versions actuals:** requisit trenta, configuració set, runbook set, lliurament bloquejat.
2. **Congela la proposta pendent:** conserva les revisions i les proves de la publicació fallida.
3. **Prepara una modificació compensatòria del requisit:** restaura set i conserva les exclusions i notes afegides entremig.
4. **Obté la revisió de la persona responsable:** indica la versió actual de la font i el text exacte de restauració.
5. **Publica per la via autoritzada:** torna a llegir la versió resultant del requisit.
6. **Concilia el registre:** tots els valors publicats aplicables són set, el canvi original no s’ha lliurat.

**La compensació no esborra l’historial.** Conserva com a registres separats l’intent d’anar a trenta dies, la fallada i la restauració posterior. La font final indica set i l’historial de lliurament explica per què la proposta aprovada no es va completar.

```text
Recovery decision: illustrative compensation
Original proposal: PROP-042 revision 1
Observed mismatch: requirement 30, configuration/runbook 7
Owner decision: restore approved baseline intent
Review object: fixed compensation against current requirement version
Result: capture resulting revision and seven-day read-back
Original delivery: withdrawn or blocked with explanation
Limit: no runtime deletion or data restoration performed
```

**Conserva explícitament qualsevol excepció que hi hagi afegit un altre autor.** Enganxar a cegues el contingut d’una pàgina antiga pot eliminar un canvi intermedi vàlid. Compara el text actual amb el previst i després revisa una modificació compensatòria mínima respecte de la versió actual.

## Prova un traspàs nou

**Fes servir una sessió neta i una altra persona revisora.** Proporciona el mapa, el paquet fixat, el registre i la decisió de recuperació. No comparteixis el xat anterior. Demana a qui rep el traspàs que indiqui la intenció actual, la configuració, les instruccions operatives i la següent acció autoritzada.

```text
Read the mapped current sources independently.
Distinguish approved intent, committed configuration, and delivery state.
Compare them with the reviewed package and ledger.
List missing reads and changed bases.
Recommend one bounded next action with its accountable role.
Do not treat this handoff as approval or publication permission.
```

**Raonament esperat:** qui rep la tasca verifica el resultat de la compensació abans d’afirmar que s’ha restaurat la base. Si només repeteix «set dies» del traspàs, no s’ha provat la lectura independent. Demana proves de les fonts en lloc d’un altre resum.

**Inventari docent completat, interrupció sintètica:**

| Registre | Estat observat | Proves a conservar | Responsable següent |
|---|---|---|---|
| REQ-17 | v5 indica trenta dies, còpies de seguretat excloses | Historial de la pàgina i lectura actual | Producte |
| Configuració protegida | `main` a `base-001` indica set dies | Lectura del commit i esdeveniment de merge denegat | Mantenidor del repositori |
| RUN-04 | v2 encara indica set dies | Lectura actual de la pàgina | Operacions |
| PROP-042 | r1 aprovada, lliurament bloquejat | Revisions fixades i registre | Responsable de lliurament |

Dona aquest inventari a una segona persona sense el xat anterior. El traspàs només s’aprova si aquesta persona troba independentment els quatre estats, assenyala l’exclusió de les còpies de seguretat, identifica `base-001` com la revisió protegida actual i recomana un pas de recuperació revisat pel responsable. Marca’l com a fallit si hi ha una revisió incorrecta, una excepció omesa o una represa sense justificació. Registra les referències de la persona a les fonts i qualsevol correcció abans d’una nova escriptura.

## Decideix si reprens la feina

| Resultat de la comprovació prèvia | Decisió de represa |
|---|---|
| **Les fonts coincideixen amb l’aprovació fixada** | Continua el pas pendent autoritzat |
| **La font ha canviat fora de l’abast revisat** | Atura’t per comparar i obtenir una nova revisió |
| **Falta accés de lectura** | Mantén en espera amb una persona revisora d’accés assignada |
| **La política ha canviat** | Repara els adaptadors i reavalua el permís de la tasca |
| **Es desconeix el resultat de l’escriptura** | Llegeix la destinació abans de tornar-ho a provar |

**Defineix criteris concrets per acceptar la recuperació.** Exigeix una lectura de retorn coincident, un objecte de revisió actual, un registre conciliat i un traspàs nou. No tanquis la recuperació perquè l’assistent digui que el problema s’ha resolt.

**Comprovació de finalització:** lliura un inventari de l’estat observat, la decisió de la persona responsable, la reparació revisada, la lectura final i una reconstrucció independent. Si l’accés impedeix llegir, documenta el bloqueig. Aplica aquest estàndard de proves al projecte final.

## Resolució de problemes i reversió

**Conflictes de revert:** prepara un canvi compensatori sobre l’estat actual. **La restauració perd excepcions:** compara tota la secció pertinent abans d’escriure. **La memòria antiga controla la resposta:** torna a començar amb fonts aprovades i elimina el context obsolet de l’esborrany.

**Reversió de la recuperació:** atura’t a l’últim estat verificat i afegeix una entrada al registre. No esborris esdeveniments d’auditoria natius ni forcis el reinici de l’historial protegit. Escala al producte les qüestions d’autoritat no resoltes.

## Exercici i autoavaluació

**Introdueix proves obsoletes, un adaptador de política antic i una publicació parcial.** Dona els registres a una altra persona revisora sense explicacions i demana-li que identifiqui qui és responsable de la reparació.

**Raonament esperat:** el producte s’encarrega de conciliar requisits, el responsable de la política d’alinear l’adaptador i la coordinació de recuperació del lliurament coordina les persones responsables implicades. «Actualitza el context» no és una reparació completa per a tots els casos.

## Referències principals

- **Controls de recuperació del repositori:** [Branques protegides](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Historial de pàgines:** [Documentació de Confluence](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Inspecció d’instruccions:** [Memòria de Claude Code](https://code.claude.com/docs/en/memory).

## Passos següents

**Completa el [Retention Capstone](/articles/ai-collaboration-retention-capstone/)** amb els dos itineraris i una segona persona lectora. Mostra lectures actuals de les fonts, diferències de versió, qui decideix, la recuperació revisada, la lectura de retorn i la reconstrucció independent.
