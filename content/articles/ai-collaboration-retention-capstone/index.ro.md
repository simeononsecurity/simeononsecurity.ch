---
title: "Capstone de colaborare AI: GitHub, Confluence și Jira"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Livrează o modificare sintetică de retenție prin fluxuri GitHub-first și Confluence/Jira, cu dovezi de eșec și evaluare independentă."
genre: ["Inteligență artificială", "Colaborare în echipă", "Inginerie software"]
tags: ["curs de colaborare AI", "propunere de retenție", "evaluare GitHub", "flux Confluence Jira", "matrice de eșecuri", "acceptare independentă"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustrație cu profesioniști care evaluează munca partajată a unui proiect într-un spațiu de securitate cibernetică"
coverCaption: ""
---

[Revino la cursul de colaborare AI](/ai-collaboration-course-start/)

**Livrează PROP-042 de două ori**, prin GitHub-first și prin GitHub cu Confluence/Jira. Tu contribui, proprietari separați evaluează, iar editorii autorizați aplică modificarea. Folosește sandbox-uri sintetice izolate după lecțiile anterioare. Capstone-ul testează procedura completă, inclusiv respingerea, recuperarea și predarea independentă, nu calitatea textului asistentului.

## Idei principale

- **O singură modificare comună** compară ambele modele de autoritate.
- **Testele negative** contează la fel de mult ca livrarea reușită.
- **Pachetele de dovezi** sprijină evaluarea independentă.
- **Finalizarea laboratorului** nu autorizează lansarea în producție.

## Înainte de a începe

**Cerințe:** [modulele anterioare ale cursului](/ai-collaboration-course-start/), acces aprobat la sandbox și evaluatori separați. **Timp pentru planificare:** opt până la douăsprezece ore în mai multe sesiuni, plus evaluare independentă. Timpul real depinde de configurarea contului și de lucrările de reparare. **Dificultate:** avansată.

**Artefacte necesare:** cartă, hartă, politică, adaptoare, baseline, manifest, propunere fixată, evaluări ale proprietarilor, registru, înregistrare de recuperare și handoff. Permisiunile dependente de plan care lipsesc blochează finalizarea. Nu le considera aprobări presupuse.

**Pregătește un director de dovezi pentru fiecare traseu înainte de testare.** Un evaluator trebuie să identifice actorul, reviziile sursei, acțiunea încercată, rezultatul observat și starea finală fără să se bazeze pe un rezumat al chatului.

## Stabilește două baseline-uri

1. **Creează rulări izolate** numite GitHub-first și Mixed. Păstrează reviziile și evaluările separate.
2. **Restabilește baseline-ul de șapte zile** prin procedura aprobată pentru fiecare traseu și capturează reviziile rezultate.
3. **Verifică mecanismele de refuz** cu conturi contributor și excluded-user.
4. **Capturează contextul curent** și confirmă acordul dintre adaptor și politică.
5. **Declară domeniul:** retenție sintetică a exportului timp de treizeci de zile, fără date reale, backup-uri și blocări legale.

**PROP-042 este o etichetă de corelare, nu o aprobare reutilizabilă.** Fiecare rulare are nevoie de propria revizie înghețată și de dovezi ale sursei. Include ID-urile rulărilor în rapoarte.

## Livrează prin GitHub-first

**Deschide Issue-ul și PR-ul candidat** folosind lecțiile GitHub. Modifică împreună cerința, configurația, propunerea și runbook-ul. Capturează baza protejată, rulează verificări de încredere și obține evaluări de la produs și operațiuni la commit-ul final.

```text
Run: GitHub-first
Change: synthetic retention 7 -> 30 days
Requirement: REQ-17 revision 2
Configuration: retention_days 30
Runbook: Retention days: 30
Proposal: base revision 1, from 7, to 30
Manifest: protected pre-change source hashes
Review: product and operations at final proposal revision
Publication: merged commit and read-back
Limit: no running deletion service exercised
```

**Completează referințele reale din sandbox.** Schița arată maparea așteptată, nu dovezi finalizate. Maintainer-ul face merge doar după evaluare, apoi citește independent **`main`**. Închide Issue-ul după ce legi înregistrările finale.

## Livrează traseul Mixed

**Citește versiunile Confluence și îngheață propunerea Jira.** Obține ambele evaluări ale proprietarilor. Publică cerința cu livrarea în așteptare, fă merge la configurație, publică runbook-ul și citește toate sistemele înainte de Done.

**Înregistrează fiecare publicare** cu versiunea paginii, commit-ul sau dovada tranziției. Copiile cerințelor din depozit rămân snapshot-uri. Verificatorul local nu dovedește autoritatea curentă a Confluence.

| Comparație | GitHub-first | Workplace Mixed |
|---|---|---|
| **Cerință** | Evaluarea depozitului protejat | Publicare evaluată de proprietarul Confluence |
| **Coordonare** | Issue/PR | Propunere Jira fixată |
| **Unitate de publicare** | Merge în depozit | Scrieri separate de pagini și merge |
| **Actualitate** | Commit protejat | Versiuni de pagină plus commit |
| **Recuperare** | Revert/compensare evaluat | Compensare ghidată de registru |

**Alege fluxul după nevoile de proprietate.** GitHub-first reduce coordonarea între sisteme. Traseul Mixed păstrează locurile de lucru și adaugă verificări de publicare și acces.

## Rulează matricea de eșecuri

| Caz | Injecție | Dovezi observate necesare |
|---|---|---|
| **Modificare aprobată** | Trimite propunerea evaluată pentru treizeci de zile | Read-back și evaluare consecvente |
| **Context învechit** | Modifică sursa după capturare | Respingere, reconciliere, reaprobare |
| **Scriere neautorizată** | Contributor-ul publică | Refuz și revizie neschimbată |
| **Conflict** | Jira spune șaizeci, Confluence șapte | Blocare și reconciliere a proprietarilor |
| **Publicare parțială** | Întrerupe după o scriere | Registru în așteptare și recuperare |
| **Refuz de acces** | Elimină accesul de citire la sarcină | Fără text protejat sau publicare |
| **Recuperare** | Finalizare/backout aprobat | Revizii noi evaluate |
| **Handoff** | Sesiunea nouă primește doar harta/registrul | Citire proaspătă și acțiune corectă |

**Conflictul între sisteme aparține traseului Mixed.** În GitHub-first testează o descriere Issue care intră în conflict cu fișierul aprobat. Rulează celelalte cazuri aplicabile în ambele trasee. Un eșec al validatorului local nu înlocuiește dovezile live ale permisiunilor.

| Caz și fișier de dovezi | Rulare GitHub-first | Rulare Mixed |
|---|---|---|
| **Modificare aprobată** `01-approved-change.md` | PR evaluat și read-back | Pagini evaluate, merge și registru |
| **Context învechit** `02-stale-context.md` | Modifică baza protejată după capturare | Modifică o pagină de autoritate după capturare |
| **Scriere neautorizată** `03-unauthorized-write.md` | Refuz pentru push direct al contributor-ului | Refuz pentru editarea și tranziția paginii |
| **Conflict** `04-conflict.md` | Issue-ul nu corespunde fișierului aprobat | Textul Jira nu corespunde cu Confluence |
| **Publicare parțială** `05-partial-publication.md` | Oprește înainte de merge sau read-back | Oprește după o scriere de pagină |
| **Refuz de acces** `06-access-denial.md` | Reține sursa protejată a depozitului | Exclude utilizatorul dintr-o pagină restricționată |
| **Recuperare** `07-recovery.md` | Revert sau finalizare evaluate | Compensare ghidată de registru |
| **Handoff** `08-handoff.md` | Sesiunea nouă citește fișiere protejate | Sesiunea nouă citește pagini mapate și registrul |

**Creează fiecare fișier înainte de test.** Înregistrează rezultatul așteptat, rezultatul observat, rolul actorului, reviziile inițiale și finale, referința dovezii native și decizia evaluatorului. Un prompt de rută în browser nu este un refuz de push direct. Păstrează separate directoarele celor două trasee.

**Păstrează separate rezultatele așteptate și observate.** Pentru fiecare caz înregistrează ID-ul rulării, rolul actorului, reviziile inițiale, acțiunea încercată, așteptarea, observația, reviziile rezultate și decizia evaluatorului. Redactează credentialele și identificatorii conturilor din rapoartele comune.

## Evaluează finalizarea

**Trecerea necesită dovezi observate pentru fiecare rând aplicabil** și acceptare independentă. Evaluatorii verifică permisiunile, actualitatea sursei, evaluarea rolurilor, publicarea parțială, reconstruirea handoff-ului și logurile de consistență.

**Eșuează imediat** la publicare neautorizată, la ajungerea textului refuzat în model sau la suprascrierea tăcută a unei baze schimbate. Păstrează lucrul Blocked până când controalele corectate trec un test repetat. Nu transforma aceste eșecuri într-un scor favorabil prin mediere.

**Măsoară cazurile finalizate/blocate, propunerile învechite respinse, scrierile refuzate, recuperările și timpul evaluatorului.** Rezultatele propuse rămân așteptate până la observare. Cele zece teste unitare furnizate acoperă consistența, nu securitatea live a tenantului.

## Planifică cele două rulări

**Nu reutiliza o aprobare între trasee.** Valoarea cerută este aceeași, dar locațiile surselor, reviziile capturate, permisiunile și secvența publicării diferă. Oferă fiecărei rulări propriul director de dovezi și pachet de evaluare.

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
    same evidence categories, independently captured
```

**Aceste nume sunt un exemplu de organizare**, nu fișiere de arhivă furnizate. Păstrează dovezile reale în privat în sandbox-ul aprobat. Trimiterile comune ale cursului trebuie să folosească etichete de rol și referințe redactate, iar evaluatorii păstrează accesul la înregistrările native.

**Atribuie un observator de teste înainte de a rula eșecurile.** Contributor-ul execută acțiunea încercată. Observatorul înregistrează starea inițială, rezultatul și starea rezultată. Un evaluator decide ulterior dacă dovezile susțin afirmația. Dezvăluie suprapunerea rolurilor în loc să sugerezi acceptarea independentă.

## Rulează eșecurile în izolare

**Resetează la o stare verificată și evaluată între cazuri.** Injectarea simultană a derivei sursei, revocării accesului și nepotrivirii runbook-ului ascunde controlul care a respins propunerea. Un singur eșec per rulare îi oferă evaluatorului un motiv trasabil.

1. **Capturează starea inițială:** revizii sursă, configurație, stare de livrare și rolul actorului.
2. **Aplică o injecție sintetică:** schimbă o condiție relevantă printr-o rută de test autorizată.
3. **Încearcă acțiunea limitată:** validare, citire, publicare sau handoff.
4. **Înregistrează observația:** ieșirea reală și starea rezultată a sursei.
5. **Repară prin evaluare:** păstrează dovezile eșecului înainte de a restaura controalele.
6. **Repetă cazul pozitiv:** confirmă că fluxul corectat livrează în continuare lucrul permis.

**Un eșec planificat rămâne o observație de eșec.** Nu redenumi publicarea neautorizată drept test reușit doar fiindcă intenționai să o sondezi. Testul a expus un defect, dar limita publicării a eșuat și necesită reparare.

**Fișa de injecție și reset pentru fiecare caz:** folosește o propunere sintetică nouă sau restaurează un baseline evaluat înainte de următorul rând. Observatorul înregistrează precondiția și confirmă resetarea. Nu șterge niciodată încercarea eșuată din registru.

| Caz | Injecție și verificare GitHub-first | Injecție și verificare Mixed | Reset înaintea următorului caz |
|---|---|---|---|
| Modificare aprobată | Trimite PR-ul fixat, obține ambele evaluări, fă merge și redeschide `main` | Publică REQ-17, fă merge la diff-ul evaluat, publică RUN-04, apoi redeschide toate înregistrările | Capturează reviziile finale ca următoarea bază |
| Context învechit | Capturează un manifest, apoi schimbă baza protejată de test printr-un PR evaluat separat înainte de validarea propunerii vechi | Capturează versiunile paginilor, apoi cere unui editor autorizat să modifice o pagină de test înainte de citirea pre-scriere | Oprește, compară versiunile, capturează surse proaspete și evaluează un pachet fixat nou |
| Scriere neautorizată | Contributor-ul încearcă un push direct inofensiv către `main` protejat și înregistrează refuzul serverului | Contributor-ul încearcă editarea REQ-17 și tranziția Approved | Redeschide commit-ul protejat, versiunea paginii și starea Jira, care ar trebui să rămână neschimbate |
| Conflict | Pune șaizeci de zile în Issue-ul schiță, în timp ce fișierul aprobat spune șapte | Pune șaizeci de zile în schița Jira, în timp ce REQ-17 spune șapte | Proprietarul produsului reconciliază schița și înregistrează decizia înainte de evaluare |
| Publicare parțială | Oprește după aprobare, dar înainte de merge sau read-back final, lăsând Issue-ul deschis | Oprește după read-back REQ-17, în timp ce configurația și RUN-04 încă spun șapte | Păstrează livrarea în așteptare, apoi obține o decizie evaluată de finalizare sau compensare |
| Refuz de acces | Folosește o identitate de test exclusă dintr-o sursă privată și încearcă o citire | Folosește identitatea exclusă pe o pagină sintetică restricționată separat | Restaurează doar accesul de test aprobat și verifică faptul că cititorul normal reușește |
| Recuperare | Întrerupe o modificare de test aprobată, apoi propune finalizare sau revert evaluat | Folosește registrul publicării parțiale pentru a propune finalizare sau compensare evaluată | Citește înapoi fiecare sursă rezultată și reconciliază registrul |
| Handoff | Trimite MAP-01 și registrul unui evaluator nou fără chatul vechi | Trimite ID-urile paginilor mapate și registrul unui evaluator nou fără chatul vechi | Evaluatorul deschide sursele curente și înregistrează pasul autorizat următor |

Pentru fiecare caz refuzat, înregistrează răspunsul platformei și o a doua citire a înregistrării protejate. Pentru cazul utilizatorului exclus, inspectează și contextul sarcinii returnat, astfel încât un fragment din cache să nu pară un refuz sigur. Dacă planul nu oferă controlul sau lipsește o identitate de test aprobată, notează Blocked în loc să simulezi un pass.

## Interpretează un rezultat Mixed

**Pachet de dovezi ilustrativ:** consistența locală trece, produsul și operațiunile evaluează pachetul fixat, publicarea cerinței reușește, iar accesul de editare la runbook este refuzat. Configurația nu a fost încă integrată. Jira rămâne Blocked.

| Afirmație | Verdict | Motiv |
|---|---|---|
| **Înregistrările candidate corespund** | Susținut de verificarea locală | Înregistrările furnizate au trecut comparațiile |
| **Proprietarii au acceptat intenția și operațiunile** | Necesită evaluări native fixate | Etichetele de rol singure sunt insuficiente |
| **Livrarea de treizeci de zile este finalizată** | Fără suport | Pașii necesari de publicare rămân în așteptare |
| **Limita permisiunilor funcționează pentru fiecare rol** | Fără suport | O acțiune refuzată are scop limitat |
| **Proprietarul recuperării trebuie să acționeze** | Susținut ca pas următor | Livrarea parțială necesită o decizie evaluată |

**Raționament așteptat:** păstrează rularea incompletă, verifică sursele curente și cere decizia proprietarului potrivit. Nu finaliza prin slăbirea permisiunilor sau descrierea verificării snapshot-ului drept dovadă de publicare live.

**Pachet didactic completat pentru traseul Mixed, sintetic și nu dovadă de tenant:**

```text
Run: MIXED-042-example
Captured base: REQ-17 v4 = 7 days, RUN-04 v2 = 7 days,
  GitHub main base-001 config.json = {"retention_days": 7}, Jira PROP-042 r1 = In Review
Fixed proposal: REQ-17 v5 wording says synthetic exports 30 days,
  excluding production data, backups, and legal holds.
  GitHub config.json changes retention_days from 7 to 30.
  RUN-04 v3 wording says 30 days, no deletion service runs in this lab,
  and incomplete publication stays pending.
Review: product owner approved the exact requirement wording at PROP-042 r1.
  Operations owner approved the exact config diff and runbook wording at r1.
Publication: publisher reopened REQ-17 v5 and read 30 days.
  Maintainer reopened main at merge-002 and read retention_days 30.
  Publisher reopened RUN-04 v3 and read 30 days.
Denied action: contributor tried an edit to restricted REQ-17 from v5.
  Platform denied the edit, the publisher reread v5 unchanged, and the
  observer saved the native denial. No edit was applied and v5 stayed unchanged.
Recovery: after a separate simulated failed RUN-04 attempt, Jira stayed
  Blocked. Operations approved a retry against the current version.
  Publisher reread v3 after the authorized retry before Jira moved to Done.
Handoff: a new reviewer received MAP-01 and the ledger, reopened the three
  sources and Jira, and named the current 30-day state and remaining runtime gap.
Limit: source publication is shown. Actual deletion timing is Not run.
```

Înlocuiește fiecare versiune, actor, refuz și read-back ilustrativ cu înregistrări native înainte de a marca un rând live ca Supported. Dacă un plan sau un rol nu permite testul, marchează rândul Blocked și păstrează cursul celor două trasee incomplet.

## Evaluează cu un cititor independent

**Cere evaluatorului să reconstruiască evenimentele**, nu doar să citească concluzia ta. El trebuie să găsească baseline-ul aprobat, propunerea fixată, deciziile proprietarilor, reviziile rezultate, încercările eșuate, repararea și lipsurile rămase fără narațiunea ta.

```text
Reviewer questions:
Which source governs retention intent in this track?
Which exact package did each owner review?
Did any source change after review?
What was published, and what remains pending?
Which denied action was observed under which role?
Did protected text reach an excluded user's context?
Which repair was reviewed and read back?
Does the fresh handoff reconstruct current state independently?
```

**Punctează fiecare cerință separat.** Folosește Supported, Failed, Blocked sau Not run împreună cu o referință de dovadă. Consistența, aprobarea, permisiunile, recuperarea și handoff-ul sunt cerințe separate. O colecție de teste locale verzi nu compensează o limită live de publicare eșuată.

```text
Run ID and track:
Reviewer role and review date:
Case 01 approved change: status ___ evidence ___ gap ___
Case 02 stale context: status ___ evidence ___ gap ___
Case 03 unauthorized write: status ___ evidence ___ gap ___
Case 04 conflict: status ___ evidence ___ gap ___
Case 05 partial publication: status ___ evidence ___ gap ___
Case 06 access denial: status ___ evidence ___ gap ___
Case 07 recovery: status ___ evidence ___ gap ___
Case 08 handoff: status ___ evidence ___ gap ___
Overall decision: Supported / Failed / Blocked / Not run
Next accountable role and action:
```

**Supported înseamnă că evaluatorul a găsit dovezi observate pentru fiecare caz aplicabil.** Notează Failed pentru un control eșuat observat, Blocked pentru acces sau control lipsă și Not run pentru un caz neîncercat. Păstrează referința nativă a fiecărui caz în fișierul său de dovezi.

**Pragul de trecere al cursului:** finalizează ambele trasee, GitHub-first și Mixed. În fiecare traseu, toate cele opt cazuri aplicabile au nevoie de dovezi Supported. O limită Failed sau lipsa unui read-back nativ blochează traseul. Un plan plătit sau o identitate de test lipsă produce Blocked, nu o trecere presupusă. Un singur traseu finalizat oferă un rezultat parțial documentat, nu finalizarea cursului.

**Pachet de model redactat, doar ilustrativ:**

```text
Track: github-first | Run: G-01 | Reviewer: separate pilot role
Base: protected commit base-001 | Fixed proposal: PROP-042 r1
Approvals: product review ref P-01, operations review ref O-01
Consistency: local check pass, saved output ref C-01
Permission: contributor direct push denied, native event ref D-01
Publication: merged commit merge-002, fresh clone confirms thirty
Exception: backups and legal holds remain excluded
Recovery: interruption case R-01 read back and resolved through review
Handoff: second reader found current base, exception, and next action
Runtime limit: no production deletion or deployment claim
Decision: Supported for synthetic GitHub-first track only
```

Înlocuiește fiecare referință ilustrativă cu un artefact observat din sandbox. Repetă pachetul complet pentru traseul Mixed cu propriile versiuni de surse și evaluări. Evaluatorul trebuie să respingă o aprobare GitHub copiată în pachetul Mixed.

## Scrie o decizie limitată

**O decizie finală utilă numește următorul pilot**, nu o lansare fără limite. De exemplu, alege o altă configurare de export sintetic cu aceleași roluri și o rută de căutare directă, lăsând datele reale și publicarea automată în afara domeniului.

| Elementul deciziei | Detaliu necesar |
|---|---|
| **Domeniu** | O modificare următoare și excluderile sale explicite |
| **Dovezi** | Cazuri Supported și eșecuri nerezolvate |
| **Controale** | Cerințe impuse de platformă și procedurale, separat |
| **Proprietari** | Rol responsabil pentru fiecare lipsă rămasă |
| **Lipsă de execuție** | Comportament de ștergere/deployment netestat |
| **Condiții de oprire** | Acces lipsă, autoritate schimbată, publicare neautorizată |

**Verificarea finalizării:** ambele pachete de rulare trec reconstrucția independentă, cazurile aplicabile au dovezi observate, iar controalele nerezolvate rămân vizibile. Dacă doar traseul GitHub este finalizat, raportează finalizare parțială a cursului. Nu presupune că traseul Mixed ar funcționa la fel.

## Depanare și backout

**Doar dovezi happy-path:** repetă testele de refuz și întrerupere. **Roluri suprapuse:** declară-le și repetă cu utilizatori separați. **Controale de plan lipsă:** oprește-te și obține un sandbox aprobat.

**Backout:** restabilește baseline-ul prin PR-uri evaluate și editări Confluence, revocă integrările temporare, arhivează dovezile Jira și efectuează curățarea sintetică aprobată de proprietar după retenția dovezilor. Păstrează istoricul recuperării.

## Creează decizia de rollout

```text
Decision: another synthetic pilot, blocked, or rejected
Evidence: both run packages and failure matrix
Unenforced requirements: procedural controls listed explicitly
Provider review: input scope and retention handling
Owner coverage: product, operations, policy, repository, delivery
Production gaps: runtime tests, secrets, deployment, access review
Next action: one bounded follow-up with accountable role
Review date: assigned by pilot owners
```

**Raționament așteptat:** succesul sintetic susține un alt pilot limitat. Producția necesită aprobare separată pentru date reale, deployment, gestionarea de către furnizor și comportamentul la rulare. Un răspuns reușit al asistentului nu este autorizare de deployment.

## Referințe principale

- **Controale ale depozitului:** [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Acces la workplace:** [Confluence permissions](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Controale de livrare:** [Jira permission schemes](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).

## Pașii următori

**Revino la [hub-ul cursului](/ai-collaboration-course-start/)** pentru a revedea controalele lipsă. Compară implementarea cu [articolul despre framework](/articles/one-source-many-tools-ai-collaboration-framework/) înainte de a selecta alt pilot.
