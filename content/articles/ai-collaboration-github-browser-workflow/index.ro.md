---
title: "Flux de lucru AI pe GitHub pentru cei care nu programează: Issues și pull request-uri"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Folosește editarea în browser, Issues, pachete de context pentru chat și pull request-uri revizuite, fără un mediu local de dezvoltare."
genre: ["Inteligență artificială", "Colaborare în echipă", "Inginerie software"]
tags: ["curs de colaborare AI", "editare GitHub în browser", "GitHub Issues", "pull request", "contribuitori fără cunoștințe de programare", "pachet de context", "predare pentru revizuire"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustrație cu profesioniști care revizuiesc munca comună la un proiect într-un spațiu de securitate cibernetică"
coverCaption: ""
---

[Înapoi la cursul de colaborare AI](/ai-collaboration-course-start/)

**Contribuitorii care nu programează respectă aceleași reguli de autoritate și în browser.** Citești sursele GitHub, redactezi cu un instrument de chat aprobat și trimiți un Issue sau o modificare pe o ramură. Responsabilul de mentenanță execută verificările și publică după revizuire. Folosește acest flux după activarea protecției depozitului, astfel încât accesul din browser să nu ocolească regulile agentului de programare.

## Idei principale

- **Lucrul în browser** nu necesită un terminal local.
- **Pachetele de context** păstrează domeniul și dovezile reviziei.
- **Issues și ramurile** rămân propuneri.
- **Predările** identifică lucrul rămas și următorul rol.

## Înainte să începi

**Cerințe preliminare:** [lecția despre limitele depozitului](/articles/ai-collaboration-github-repository/), acces de citire la laborator și un instrument de chat aprobat, dacă dorești. **Durată estimată:** 45-60 de minute. **Dificultate:** introductivă. Contribuitorii care folosesc doar Issues sar peste Git local și Actions. Contribuitorii care trimit un PR se coordonează cu un responsabil care a parcurs [lecția despre agenți și Actions](/articles/ai-collaboration-github-agents-actions/).

**Flux de bază fără conector:** deschide GitHub personal și furnizează doar fragmente sintetice. Nu se presupune că ai o funcție de chat inclusă într-un abonament. Dacă un furnizor nu este aprobat, redactează manual folosind aceleași înregistrări.

**Rezultatul final:** predai un Issue sau PR cu revizii fixe ale surselor, formularea propusă, fișierele afectate, excluderi și întrebări nerezolvate.

## Citește pachetul de surse

1. **Deschide MAP-01 pe `main`**, apoi găsește POL-01, REQ-17 și RUN-04.
2. **Citește fiecare sursă** și notează revizia commitului din vizualizarea commiturilor din browser.
3. **Copiază secțiunile sintetice relevante** împreună cu numele fișierelor, reviziile, domeniul și excepțiile.
4. **Marchează pachetul ca bazat pe un instantaneu** până când responsabilul îl compară cu sursele actuale înainte de publicare.

```text
Project: export-service-lab
Task: PROP-042 draft, no publication permission
Authority: requirement.json, REQ-17 revision 1
Baseline: retention_days 7
Policy: POL-01 version 1
Requested proposal: retention_days 30
Evidence: attach browser-verified commit references
Missing evidence: no runtime deletion observations
Output: proposed wording, affected files, questions, rollback
Stop: source unavailable, changed revision, conflicting authority
```

**Atașează în privat reviziile reale ale mediului de test.** Modelul nu conține dovezi completate. Cere asistentului să identifice înregistrările lipsă înainte să recomande publicarea.

**Pachet sintetic completat înainte de citirea unei surse live:**

```text
Project: export-service-lab
Task: draft PROP-042 in an Issue
Approved baseline: REQ-17 revision 1, retention_days 7
Proposal: retention_days 30, synthetic export files only
Affected records: requirement.json, config.json, proposal.json, runbook.md
Exclusions: production data, backups, legal holds
Known evidence: supplied lab baseline files
Missing evidence: current main commit, owner decisions, runtime deletion result
Status: Draft, publication blocked until current revisions and reviews exist
Next role: maintainer supplies verified main commit and runs checks
```

**Pachetul este complet ca solicitare de redactare.** Linia despre dovezile lipsă este intenționată. Înlocuiește baza furnizată de laborator cu revizii actuale ale mediului de test înainte să ceri publicarea.

## Deschide un Issue

**Selectează Issues, New issue** și folosește titlul **`PROP-042: propose thirty-day synthetic retention`**. Lipește această descriere și atașează pachetul de surse.

```text
Proposal: PROP-042
Status: Draft
Current approved value: 7 days, REQ-17 revision 1
Requested value: 30 days
Reason: fictional pilot requirement, not compliance advice
Scope: synthetic export records only
Affected files: requirement.json, config.json, runbook.md
Evidence: source revisions and policy version attached
Reviewers: product-owner and operations-owner
Implementation reviewer: repository-maintainer
Acceptance: consistent records, denied publication, fresh handoff
Rollback: reviewed restoration of the approved baseline
```

**Cere chatului să compare propunerea cu pachetul**, să enumere presupunerile și să redacteze întrebări pentru responsabili. Salvează proiectul în Issue. Nu cere chatului să aprobe modificarea și nu trata conversația ca registru de decizii.

## Trimite modificări din browser

1. **Deschide fila Code a depozitului.** Selectează meniul ramurilor deasupra listei de fișiere, confirmă **`main`**, introdu **`proposal-042`** și alege **Create branch: proposal-042 from main**. Dacă nu poți crea o ramură, folosește un fork aprobat sau calea Issue de mai jos.
2. **Confirmă `proposal-042` în meniul ramurilor** înainte să deschizi un fișier. Selectează fișierul și pictograma creionului pentru editare. Editorul web GitHub nu editează o ramură protejată.
3. **Modifică cerința** la treizeci de zile și revizia 2. Redeschide meniul ramurilor înaintea fiecărei modificări rămase. Editează configurarea și manualul pe aceeași ramură.
4. **Editează `proposal.json`** cu to_days 30, from_days 7 și base_revision 1.
5. **Previzualizează Markdown** și verifică punctuația JSON. Creează commit pentru fiecare modificare din browser în **`proposal-042`**.
6. **Deschide Pull requests, apoi New pull request.** Compară **`proposal-042`** cu **`main`**, inspectează modificările din toate cele patru fișiere și creează un PR care face trimitere la Issue. Cere responsabilului să atașeze un manifest nou din baza protejată și să ruleze verificarea de consistență.
7. **Solicită revizuirea responsabililor** pentru revizia finală a propunerii. Păstrează livrarea deschisă până când revizuirea și verificarea prin recitire reușesc.

**Jurnal de navigare:** notează numele depozitului, numărul Issue, ramura propunerii, căile fișierelor modificate, numărul PR, numele verificării, revizia analizată și commitul final din `main`. Folosește vizualizările Issues, Code, Pull requests, Actions și PR Checks/Reviews pentru a le găsi din nou. Dacă GitHub mută un control, găsește aceeași înregistrare după număr sau ID-ul commitului în loc să ghicești dintr-o captură de ecran. Exportă o notă privată de dovezi cu adresele URL ale înregistrărilor și starea observată. Înainte să distribui nota în afara echipei autorizate, elimină numele conturilor, adresele de e-mail, tokenurile, identificatorii de tenant și datele fără legătură din alte depozite. Păstrează dovezile neredactate doar în locul privat aprobat.

**Documentația GitHub descrie căile de contribuție prin ramuri și fork-uri.** Un contribuitor fără acces de scriere la depozit folosește un fork aprobat sau calea Issue. Un fork nu oferă drepturi de publicare în depozitul original.

## Inspectează diff-ul rezultat

| Fișier | Bază | Variantă propusă |
|---|---|---|
| **Cerință** | Revizia 1, șapte zile | Revizia 2, treizeci de zile |
| **Configurare** | Șapte zile | Treizeci de zile |
| **Manual** | `Retention days: 7` | `Retention days: 30` |
| **Propunere** | From 7, to 7 | From 7, to 30, base 1 |
| **Manifest** | Necapturat | Hash-uri ale surselor protejate înainte de modificare |

**Manifestul descrie baza**, nu formularea propusă pentru treizeci de zile. Calcularea hash-ului pentru cerința candidat și prezentarea lui ca dovadă a bazei produce o nepotrivire cu baza de încredere.

## Verifică și predă

**Test pozitiv:** responsabilul face merge după revizuirea proprietarului și trecerea verificărilor. Deschide fișierele rezultate din **`main`** și confirmă că sunt de acord. Atașează commitul rezultat și recitirea în Issue. Acest lucru dovedește configurația salvată, nu comportamentul de ștergere la execuție.

**Test negativ:** cere chatului să aprobe sau să publice propunerea. Comportamentul așteptat conform politicii este un răspuns care oferă doar un proiect de text. Separat, încearcă publicarea directă ca contribuitor și înregistrează refuzul platformei împreună cu revizia sursei neschimbată. Păstrează distincte testele comportamentale și cele de control al accesului.

```text
Handoff: HANDOFF-042
Proposal: PROP-042
Policy: POL-01 version 1
Sources: attach current requirement, runbook, and config revisions
Published value: record after reading main
Completed: merged files and check reference
Remaining: runtime deletion service not tested
Next role: operations-owner
Next action: independent source read and runbook verification
Stop: changed source, missing access, conflicting authority
```

**Începe o sesiune nouă doar cu harta și predarea.** Cere o nouă verificare a sursei sau o solicitare explicită de dovezi din browser. Asistentul ar trebui să reconstruiască valoarea din înregistrările sursă, nu să repete rezumatul anterior.

## Redactează fără să pierzi contextul

**Un contribuitor din browser are nevoie în continuare de o întrebare completă.** „Schimbă retenția la treizeci de zile” omite autoritatea actuală, domeniul, starea revizuirii și înregistrările afectate. Oferă chatului pachetul de surse și o instrucțiune de redactare. Dacă înregistrarea nu este disponibilă, cere responsabilului dovezi autorizate în loc să înlocuiești textul cu ce îți amintești.

```text
Draft an Issue for PROP-042 from the attached synthetic source packet.
Keep seven days labeled as the approved baseline.
Keep thirty days labeled as proposed intent.
Preserve exclusions for production data, backups, and legal holds.
List requirement, configuration, proposal, and runbook changes.
List missing evidence instead of filling it with guessed revisions.
Do not claim owner approval or delivered behavior.
```

**Inspectează răspunsul înainte să-l copiezi.** Verifică dacă a schimbat domeniul, a inventat un commit sau a descris aprobarea ca fiind finalizată. Elimină afirmațiile fără suport și păstrează întrebările nerezolvate în Issue. Chatul te ajută să redactezi propunerea, nu furnizează dovezi din sisteme pe care nu le-a citit.

## Alege calea de contribuție

| Situație | Cale | Livrabil |
|---|---|---|
| **Doar acces de citire** | Issue cu formularea propusă fixată | Cerere de modificare pregătită pentru responsabil |
| **Acces aprobat la ramură** | Editări în browser pe o singură ramură de propunere | PR cu modificări corelate ale fișierelor |
| **Cale de fork aprobată** | Fork și PR către depozitul din amonte | Variantă în așteptarea revizuirii din amonte |
| **Fără acces la sursă** | Oprește-te și cere dovezi autorizate | Sarcină marcată explicit ca blocată |

**Calea Issue este o contribuție completă**, nu un exercițiu de programare eșuat. Furnizezi modificarea dorită, dovezile, domeniul și întrebările de revizuire. Responsabilul pregătește patch-ul și manifestul. Apoi verifici dacă patch-ul corespunde solicitării tale.

| Cale | Verificarea de finalizare a contribuitorului | Predarea către responsabil |
|---|---|---|
| **Doar Issue** | Issue conține un pachet de surse verificat, formularea propusă fixată, excluderi și întrebări deschise | Responsabilul creează ramura, rulează verificările și leagă PR-ul |
| **PR** | O ramură conține toate fișierele afectate, diff-ul corespunde propunerii, iar revizorii primesc revizia finală | Responsabilul rulează verificările, obține revizuirea proprietarului, face merge și înregistrează recitirea |

**Când editezi în browser, rămâi pe ramura propunerii.** După ce prima editare creează ramura, redeschide fiecare fișier rămas din același selector de ramură. Verifică diff-ul PR la final. Patru ramuri separate produc patru modificări incomplete, nu un pachet ușor de revizuit.

## Inspectează formularea propusă

**Formulare slabă, cu titlu ilustrativ:** „Exporturile sunt acum disponibile timp de treizeci de zile.” Descrie livrarea ca finalizată și omite domeniul sintetic. Cât timp revizuirea este în așteptare, folosește o formulare de propunere.

```text
Proposed intent:
Retain synthetic export files for 30 days.
Exclude production data, backups, and legal holds.

Current approved intent:
Retain synthetic export files for 7 days under REQ-17 revision 1.

Delivery:
Not published. No runtime deletion service was tested.
```

**Compară fiecare fișier afectat cu această formulare.** Revizia cerinței avansează în varianta candidat. Configurația ajunge la treizeci. Prima linie din manual ajunge la treizeci, păstrând limitarea laboratorului. Propunerea indică în continuare șapte drept valoare anterioară și revizia unu drept bază.

**Întreabă despre neconcordanțe în loc să repari controale necunoscute.** Dacă patch-ul responsabilului slăbește protecția sau șterge politica, cere o explicație și o revizuire separată. Nu trebuie să înțelegi fiecare linie a fluxului pentru a identifica o modificare în afara domeniului solicitat.

## Răspunde la feedback-ul revizuirii

**Exemplu de revizuire:** echipa de operațiuni cere o propoziție care să explice că revenirea configurației nu restaurează fișierele șterse. Actualizează proiectul pe aceeași ramură și informează revizorii că domeniul s-a schimbat. Revizuirea finală trebuie să se refere la propunerea actualizată, nu la o copie mai veche din chat.

| Comentariu la revizuire | Acțiunea contribuitorului |
|---|---|
| **Excludere lipsă** | Restabilește formularea și cere revizuirea intenției |
| **Revizie sursă învechită** | Obține un pachet autorizat nou și reconciliază-l |
| **Manifest lipsă** | Cere responsabilului să captureze baza protejată |
| **Modificare de control fără legătură** | Separ-o sau elimin-o înainte de revizuire |
| **Afirmație despre execuție netestată** | Înlocuiește-o cu limitarea exactă a laboratorului |

**Păstrează întrebările vizibile până la răspuns.** Rezolvarea unui comentariu fără remedierea problemei subiacente elimină un semnal util. Include în răspuns un link la modificare sau la dovezi, astfel încât alt revizor să urmărească decizia fără să citească întreaga conversație.

## Verificarea finalizării în browser

**Predă un Issue sau PR pe care alt responsabil îl execută fără să ghicească.** Include pachetul de surse, formularea propusă, înregistrările afectate, excluderile, rolurile responsabile și întrebările nerezolvate. După publicare, capturează recitirea separat de propunerea inițială.

**Autoverificare:** oferă pachetul cuiva care nu cunoaște chatul tău. Cere-i să distingă între valorile solicitate, aprobate și publicate. Dacă spune că treizeci este deja livrat înainte de merge, repară etichetele pachetului. Aplică aceeași disciplină pe traseul de lucru în echipă.

| Poartă de revizuire | Condiție de acceptare |
|---|---|
| **Reviziile surselor** | Fiecare commit sau versiune de pagină menționată se deschide în mediul de test. Reviziile necunoscute rămân marcate ca lipsă. |
| **Excluderi** | Datele de producție, copiile de siguranță și păstrările legale rămân în afara propunerii. |
| **Întrebări** | Întrebările nerezolvate despre responsabili sau surse rămân vizibile în Issue sau PR. |
| **Valabilitatea aprobării** | Revizuirile menționează revizia finală a propunerii. Aprobarea anterioară nu acoperă editările ulterioare. |

**Orice poartă eșuată menține publicarea în așteptare.** Contribuitorii care folosesc doar Issue predau rezultatul responsabilului. Contribuitorii cu PR cer o altă revizuire după remedieri.

## Depanare și revenire

**Fără permisiune de editare:** folosește un Issue sau un fork aprobat. **Referință de commit inventată:** înlocuiește-o cu dovezi verificate și revizuiește din nou proiectul. **Aprobare anterioară editărilor:** cere o aprobare nouă.

**Revenire:** închide un PR nemergat, păstrând dovezile. Pentru conținutul mergat, cere responsabilului o propunere de revert protejată prin revizuire. Nu modifica baza pentru a simula o recuperare reușită.

## Exercițiu și autoevaluare

**Ascunde înregistrarea cerinței** față de noul asistent și cere o recomandare de publicare.

**Raționament așteptat:** solicită dovezi autoritative sau marchează răspunsul drept bazat pe instantaneu. Publicarea rămâne blocată până când reușește o citire nouă.

## Referințe principale

- **Pași în browser:** [Editarea fișierelor](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).
- **Limita revizuirii:** [Ramuri protejate](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Pașii următori

**Continuă cu [Configurarea Confluence și Jira](/articles/ai-collaboration-confluence-jira-setup/)** pentru a repeta modelul operațional în sistemele de lucru.
