---
title: "Recuperarea derivei agenților AI și fluxul de predare a sarcinilor"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Detectează surse și adaptoare de politici învechite, recuperează publicări întrerupte și verifică predări independente între agenți."
genre: ["Inteligență artificială", "Colaborare în echipă", "Inginerie software"]
tags: ["curs de colaborare AI", "deriva surselor", "recuperarea publicării", "predarea către agent", "verificarea surselor actuale", "compensare"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustrație cu profesioniști care revizuiesc împreună munca unui proiect într-un spațiu de lucru pentru securitate cibernetică"
coverCaption: ""
---
[Înapoi la cursul de colaborare AI](/ai-collaboration-course-start/)

**Verifică deriva înaintea sarcinilor și după o publicare întreruptă.** Compară versiunile surselor, versiunile adaptoarelor și starea livrării în depozit sau în sandboxul de lucru. Fă acest lucru după finalizarea unei piste. Astfel, rezumatele vechi nu devin autoritate actuală și păstrezi un istoric de recuperare care poate fi revizuit.

## Idei principale

- **Deriva sursei** este diferită de deriva adaptorului.
- **Publicarea parțială** necesită un registru pentru fiecare sistem.
- **Recuperarea** păstrează istoricul și modificările revizuite.
- **Predările** necesită ca un alt revizor să citească independent sursele actuale.

## Înainte de a începe

**Cerințe preliminare:** [fluxul GitHub în browser](/articles/ai-collaboration-github-browser-workflow/) sau [fluxul mixt de publicare](/articles/ai-collaboration-confluence-jira-publication/). **Durată estimată:** 60 până la 90 de minute. **Dificultate:** revizuire avansată.

**Siguranță:** folosește numai înregistrări sintetice. Oprește publicarea automată înaintea testelor de recuperare. Nu este furnizat niciun serviciu de ștergere în execuție.

**Rezultatul pentru cititor:** finalizează un inventar de stare, o decizie a proprietarului, o remediere revizuită și o predare pe care un alt revizor o poate reconstrui din sursele actuale. Finalizarea exercițiului nu reprezintă aprobarea publicării.

## Clasificarea derivei

| Derivă | Semnal | Responsabil pentru remediere |
|---|---|---|
| **Cerință** | Sursa diferă de manifest | Proprietarul produsului |
| **Politică** | Adaptorul diferă de POL-01 | Proprietarul politicii |
| **Implementare** | Configurația contrazice intenția | Responsabil de mentenanță |
| **Runbook** | Instrucțiunile contrazic comportamentul aprobat | Responsabil operațional |
| **Acces** | Citirea unei surse accesibile anterior este refuzată | Administrator, sarcină oprită |
| **Livrare** | Marcată ca finalizată fără registru complet | Responsabil de livrare |

**Cel mai recent text nu este neapărat autoritatea aprobată.** O editare recentă neautorizată necesită investigare, nu adoptare automată. Clarifică starea și proprietarul înainte de a copia valori.

## Efectuarea verificării preliminare

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

**Contribuitorul face verificarea preliminară înainte de redactare. Editorul o repetă înainte de scriere.** Păstrează comparația versiunilor împreună cu propunerea. Verificările săptămânale completează aceste citiri, dar nu le înlocuiesc.

**Exemplu de derivă a adaptorului:** POL-01 ajunge la versiunea 2, în timp ce CLAUDE.md indică încă versiunea 1. Oprește-te, citește schimbarea de politică revizuită, actualizează adaptorul printr-un PR protejat și începe o sesiune nouă. Schimbarea doar a numărului versiunii, fără încărcarea politicii, nu repară contextul.

**Introdu o derivă a sursei în laboratorul offline:** extrage o copie nouă a arhivei ZIP furnizate într-un director temporar gol. Din rădăcină, copiază `baseline/` în `candidate/`, execută `python3 check.py capture --base baseline > candidate/context.json`, apoi execută `python3 check.py validate --base baseline --candidate candidate`. Înregistrează primul rezultat `PASS`. Deschide `baseline/requirement.json` într-un editor de text și schimbă numai `"retention_days": 7` în `"retention_days": 8`. Rulează din nou aceeași comandă validate. Codul de ieșire așteptat este diferit de zero, cu mesajul `STALE_CONTEXT: capture the trusted base again`. Înregistrează ambele rezultate și calea sursei modificate. Șterge extracția temporară după salvarea dovezilor private, apoi extrage o copie nouă pentru resetare. Nu aplica schimbarea la opt zile în depozitul publicat și nu considera o nouă captură drept aprobarea proprietarului.

**Introdu o derivă a adaptorului în depozitul temporar:** pe o ramură nouă de propunere, copiază în CLAUDE.md textul aprobat al adaptorului POL-01 versiunea 1 și etichetează-l versiunea 1. Într-o propunere de politică separată și revizuită, descrie schimbarea la versiunea 2 cu o nouă condiție de oprire specifică. Lasă adaptorul la versiunea 1. Cere unui revizor să compare cele două înregistrări și să marcheze adaptorul ca învechit înainte de orice merge sau rulare a agentului. Resetează prin închiderea propunerilor de test sau prin actualizarea adaptorului într-un PR revizuit. Apoi deschide o sesiune nouă și verifică ambele versiuni și noua condiție de oprire. Păstrează diffurile vechi și corectate. Acesta este un test de documentație, nu o simulare a refuzului platformei.

## Recuperarea unei publicări întrerupte

1. **Oprește publicarea PROP-042** și desemnează responsabilul recuperării.
2. **Citește starea reală** în toate sistemele participante. Distinge între finalizat, eșuat și neatins.
3. **Cere echipei de produs să aleagă** între finalizare, revenire revizuită sau suspendare.
4. **Pregătește o propunere de recuperare** pe baza unor referințe actuale, păstrând neschimbate domeniul și excepțiile, dacă nu au fost revizuite explicit.
5. **Aplică un singur pas revizuit odată**, înregistrând și recitind fiecare rezultat.
6. **Verifică starea finală** și limitele rămase înainte de reluarea activității obișnuite.

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

**Înlocuiește stările ilustrative cu revizii și valori observate.** O intrare anterioară în registru sau o afirmație a asistentului nu dovedește o recitire.

| Alegere | Când se folosește | Limitare |
|---|---|---|
| **Continuare** | Aprobarea rămâne valabilă și sursele se reconciliază | Necesită verificare actuală |
| **Revenire** | Proprietarul retrage schimbarea sau implementarea eșuează | Nu recuperează date șterse |
| **Suspendare** | Dovezile sau accesul lipsesc | Livrarea rămâne incompletă |

**Alege suspendarea când lipsesc dovezile.** Exercițiile sintetice nu justifică suprascrierea oarbă. Numește următorul rol și dovezile care lipsesc.

**Recuperarea GitHub** folosește un revert sau o compensare revizuită. **Recuperarea Confluence** compară istoricul și folosește o restaurare sau compensare revizuită. **Recuperarea Jira** păstrează istoricul propunerii și redeschide sau blochează livrarea. Citește reviziile rezultate în loc să presupui că numerotarea istoricului se reia de la zero.

## Verificarea unei predări independente

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

**Deschide alt instrument sau o sesiune curată** cu harta și predarea, nu conversația anterioară. Cere citiri noi ale surselor, un manifest nou și identificarea acțiunii în așteptare. Dovezile colectate manual în browser rămân valabile dacă sunt etichetate ca instantaneu și reverificate înainte de scriere.

**Predare negativă:** refuză accesul la REQ-17. Așteaptă un blocaj explicit, nu o valoare ghicită sau un fragment privilegiat. Restabilește doar accesul aprobat prin administrare și repetă verificarea.

## Diagnostic înainte de reparare

**Începe cu un inventar de stare.** „Asistenții nu sunt de acord” descrie un simptom al răspunsului, nu problema sursei de bază. Citește separat cerința mapată, configurația, runbookul, politica și înregistrarea livrării înainte de a cere oricărui asistent să le repare.

| Observație | Diagnostic | Prima acțiune |
|---|---|---|
| **Ambele surse se potrivesc, răspunsul vechi diferă** | Context de răspuns învechit | Reconstruiește din citiri actuale |
| **Cerință treizeci, configurație șapte** | Nepotrivire de livrare sau implementare | Inspectează pachetul aprobat și registrul |
| **Adaptor unu, politică doi** | Nepotrivire a versiunii instrucțiunilor | Citește schimbarea politicii și repară adaptorul |
| **Sursa era accesibilă, acum este refuzată** | Modificare de acces | Oprește sarcina și cere o revizuire autorizată |
| **Registru complet, runbook șapte** | Închidere fără recitire validă | Redeschide sau blochează livrarea și investighează |

**Nu trata fiecare nepotrivire ca pe o problemă a modelului.** Reîmprospătarea unei sesiuni repară contextul conversațional învechit. Nu publică un runbook, nu restaurează o permisiune lipsă și nu reconciliază decizii contradictorii ale proprietarilor. Numește responsabilul remedierii înainte de a alege o acțiune în instrument.

## Parcurgerea compensării

**Întrerupere ilustrativă:** REQ-17 conține intenția aprobată de treizeci de zile, iar livrarea este în așteptare. Configurația și runbookul indică încă șapte zile. Responsabilul de mentenanță raportează o eroare de implementare nerezolvată. Produsul alege restaurarea în locul continuării.

1. **Înregistrează versiunile curente:** cerință treizeci, configurație șapte, runbook șapte, livrare blocată.
2. **Îngheață propunerea în așteptare:** păstrează revizuirile și dovezile publicării eșuate.
3. **Pregătește o modificare compensatorie a cerinței:** restaurează șapte, păstrând excluderile și notele intervenite.
4. **Obține revizuirea proprietarului:** identifică versiunea actuală a sursei și formularea exactă a restaurării.
5. **Publică prin ruta autorizată:** recitește versiunea rezultată a cerinței.
6. **Reconciliază registrul:** toate valorile publicate aplicabile sunt șapte, schimbarea inițială nu a fost livrată.

**Compensarea nu șterge istoricul.** Păstrează încercarea de schimbare la treizeci de zile, eșecul ei și restaurarea ulterioară ca înregistrări separate. Sursa finală spune șapte, iar istoricul livrării explică de ce propunerea aprobată nu a fost finalizată.

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

**Păstrează explicit orice excepție adăugată de alt autor.** Lipirea oarbă a corpului unei pagini vechi riscă să elimine o modificare intermediară validă. Compară textul actual cu cel dorit, apoi revizuiește o modificare compensatorie minimă pe baza versiunii curente.

## Testarea unei predări noi

**Folosește o sesiune curată și un alt revizor.** Furnizează harta, pachetul fixat, registrul și decizia de recuperare. Nu oferi conversația anterioară. Cere destinatarului să precizeze intenția actuală, configurația, îndrumarea operațională și următoarea acțiune autorizată.

```text
Read the mapped current sources independently.
Distinguish approved intent, committed configuration, and delivery state.
Compare them with the reviewed package and ledger.
List missing reads and changed bases.
Recommend one bounded next action with its accountable role.
Do not treat this handoff as approval or publication permission.
```

**Raționament așteptat:** destinatarul verifică rezultatul compensării înainte de a descrie baza ca restaurată. Dacă repetă doar „șapte zile” din predare, cerința de citire independentă nu a fost testată. Cere dovezi din surse în locul unui alt rezumat.

**Inventar didactic completat, întrerupere sintetică:**

| Înregistrare | Stare observată | Dovezi de păstrat | Următorul proprietar |
|---|---|---|---|
| REQ-17 | v5 indică treizeci de zile, backupurile sunt excluse | Istoricul paginii și o citire nouă | Produs |
| Configurație protejată | `main` la `base-001` indică șapte zile | Recitirea commitului și evenimentul de merge refuzat | Responsabil de mentenanța depozitului |
| RUN-04 | v2 indică încă șapte zile | Citire nouă a paginii | Operațiuni |
| PROP-042 | r1 aprobată, livrare blocată | Revizuiri fixate și registru | Responsabil de livrare |

Dă acest inventar unui al doilea cititor fără conversația veche. Predarea trece numai dacă cititorul găsește independent toate cele patru stări, numește excluderea backupurilor, identifică `base-001` drept revizia protejată curentă și recomandă un pas de recuperare revizuit de proprietar. Marchează eșec pentru o revizie greșită, o excepție lipsă sau o reluare nejustificată. Înregistrează referințele cititorului la surse și orice corecție înainte de o nouă scriere.

## Decizia de reluare

| Rezultatul verificării preliminare | Decizia de reluare |
|---|---|
| **Sursele corespund aprobării fixate** | Continuă pasul autorizat în așteptare |
| **Sursa s-a schimbat în afara domeniului revizuit** | Oprește-te pentru comparație și o nouă revizuire |
| **Lipsește accesul de citire** | Suspendă cu un revizor de acces desemnat |
| **Politica s-a schimbat** | Repară adaptoarele și reevaluează permisiunea sarcinii |
| **Rezultatul scrierii este necunoscut** | Citește destinația înainte de a reîncerca |

**Definește concret criteriile de acceptare a recuperării.** Cere recitire concordantă, un obiect de revizuire actual, un registru reconciliat și o predare nouă. Nu închide recuperarea doar pentru că asistentul spune că problema s-a rezolvat.

**Verificare de finalizare:** furnizează un inventar al stării observate, decizia proprietarului, remedierea revizuită, recitirea finală și o reconstrucție independentă. Dacă accesul împiedică citirea, documentează blocajul. Aplică acest standard de dovezi proiectului final.

## Depanare și revenire

**Conflicte la revert:** pregătește o modificare compensatorie pe baza stării curente. **Restaurarea pierde excepții:** compară întreaga secțiune relevantă înainte de scriere. **Memoria veche controlează răspunsul:** reîncepe cu surse aprobate și elimină contextul vechi al schiței.

**Revenirea asupra recuperării:** oprește-te la ultima stare verificată și adaugă o intrare în registru. Nu șterge evenimentele native de audit și nu reseta forțat istoricul protejat. Escaladează la produs problemele de autoritate nerezolvate.

## Exercițiu și autoevaluare

**Introdu dovezi învechite, un adaptor de politică depășit și o publicare parțială.** Dă înregistrările unui alt revizor fără narațiune și cere-i să identifice responsabilul remedierii.

**Raționament așteptat:** produsul deține reconcilierea cerințelor, proprietarul politicii deține alinierea adaptorului, iar coordonarea recuperării livrării coordonează proprietarii implicați. „Reîmprospătează contextul” nu este o remediere completă pentru toate cazurile.

## Referințe principale

- **Controale de recuperare a depozitului:** [Ramuri protejate](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Istoricul paginii:** [Documentația Confluence](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Inspectarea instrucțiunilor:** [Memoria Claude Code](https://code.claude.com/docs/en/memory).

## Pașii următori

**Finalizează [Retention Capstone](/articles/ai-collaboration-retention-capstone/)** folosind ambele piste și un al doilea cititor. Arată citiri actuale ale surselor, diferențe de versiune, proprietarul deciziei, recuperarea revizuită, recitirea și reconstrucția independentă.
