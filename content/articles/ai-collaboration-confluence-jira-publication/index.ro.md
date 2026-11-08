---
title: "Flux de publicare AI în GitHub, Confluence și Jira"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Publică o propunere fixă de retenție în Confluence, GitHub și Jira, cu verificări de versiune și recuperare după publicarea parțială."
genre: ["Inteligență artificială", "Colaborare în echipă", "Inginerie software"]
tags: ["curs de colaborare AI", "Confluence Cloud", "Jira Cloud", "publicare între sisteme", "verificare versiune", "registru de publicare", "publicare parțială"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustrație cu profesioniști care revizuiesc munca comună la un proiect într-un spațiu de lucru de securitate cibernetică"
coverCaption: ""
---

[Înapoi la cursul de colaborare AI](/ai-collaboration-course-start/)

**Contribuitorul fixează PROP-042 înainte ca responsabilii să îl aprobe.** Un editor Confluence actualizează cerințele, un responsabil GitHub îmbină implementarea, iar echipa de operațiuni publică runbook-ul. Jira înregistrează fiecare pas. Fă acest lucru după ce verifici permisiunile, deoarece cele trei sisteme nu formează o tranzacție atomică. Registrul de publicare face vizibile livrările incomplete.

## Idei principale

- **Intenția aprobată** diferă de comportamentul livrat.
- **Reviziile fixe ale propunerii** leagă revizuirea de o versiune.
- **Registrele de publicare** expun pașii incompleți.
- **Citirile recente** protejează împotriva bazelor schimbate.

## Înainte de a începe

**Cerințe preliminare:** [configurarea spațiului de lucru](/articles/ai-collaboration-confluence-jira-setup/), acces de publicare, responsabili și un responsabil al depozitului. **Durată estimată:** două ore. **Dificultate:** coordonare avansată.

**Interfața de bază:** citire în browser, redactare opțională într-un chat aprobat și publicare de către o persoană. Nu se presupune niciun abonament la conectori. Înainte de a adăuga o integrare, verifică disponibilitatea în tenant, domeniile de acces, gestionarea datelor de către furnizor și maparea identităților. Nu partaja niciodată acreditările unui responsabil cu un contribuitor.

**Rezultatul pentru cititor:** vei termina cu o propunere fixă, un registru de publicare pentru fiecare sistem, dovezi de recitire și o decizie de recuperare pentru primul pas incomplet. Exercițiul demonstrează procedura și gestionarea dovezilor, nu comportamentul de retenție în producție.

## Înregistrează sursele actuale

1. **Citește MAP-01**, apoi deschide REQ-17 și RUN-04 folosind ID-urile de pagină mapate.
2. **Deschide meniul paginii și Page History** și înregistrează versiunile numerice, starea, formularea, responsabilul și excepțiile.
3. **Citește elementul Jira** și atașează un export fix al propunerii sau un commit GitHub. Cheia singură nu fixează dovezile revizuirii.
4. **Citește POL-01 aprobată** și baza de configurație protejată.
5. **Furnizează chatului doar fragmentele sintetice necesare**, marchează-le ca instantanee și dezactivează acțiunile de scriere.

```text
Task: PROP-042, propose only
Authority: Confluence REQ-17 for intent, GitHub for behavior
Read: mapped current pages, versions, scope, exceptions
Proposal: synthetic export retention from 7 to 30 days
Output: requirement wording, config diff, runbook, ledger
Evidence: source ID and captured revision for each factual claim
Unknowns: missing access and absent runtime observations
Stop: conflict, changed base, or denied access
```

**Pachetele offline rămân bazate pe instantanee.** Editorul recitește sursele actuale înainte de a scrie. Refuzul accesului blochează publicarea. Un export vechi nu înlocuiește autorizarea actuală.

## Fixează propunerea

```json
{
  "proposal_id": "PROP-042",
  "proposal_revision": 1,
  "requirement_base_version": 1,
  "runbook_base_version": 1,
  "policy_version": 1,
  "from_days": 7,
  "to_days": 30,
  "status": "awaiting-owner-review",
  "publication_order": ["requirement", "implementation", "runbook", "delivery"]
}
```

**Înlocuiește versiunile ilustrative ale paginilor cu versiunile capturate efectiv.** Atașează JSON-ul fix și formularea propusă în Jira. Fiecare responsabil înregistrează rolul, decizia, revizia propunerii, versiunile surselor și ora revizuirii. Orice modificare substanțială trimite pachetul înapoi la `Review`.

**Echipa de produs revizuiește intenția și domeniul de aplicare. Operațiunile revizuiește curățarea și recuperarea.** Responsabilul depozitului revizuiește diff-ul. Reacțiile la mesaje de chat modificabile nu sunt aprobări legate de o revizie.

## Publică și recitește

1. **Mută Jira în `Publishing`** după ce editorul verifică ambele revizuiri ale responsabililor și faptul că bazele sursă nu s-au schimbat.
2. **Publică REQ-17** cu treizeci de zile și un câmp de livrare în așteptare. Înregistrează versiunea rezultată, domeniul și excepțiile.
3. **Deschide PR-ul de implementare GitHub**, făcând referire la versiunea aprobată a paginii. Schimbă configurația la treizeci de zile și atașează un instantaneu neautoritar al cerinței.
4. **Îmbină după revizuirea depozitului** și recitește **`main`**. Înregistrează separat comportamentul din depozit și comportamentul la execuție.
5. **Publică RUN-04**, recitește-l după ID și înregistrează versiunea rezultată. Editorul actualizează referințele de livrare ale cerinței.
6. **Finalizează Jira** numai când toate înregistrările coincid și este atașată dovada recitirii finale.

**Folosește validatorul local numai pentru a verifica consistența instantaneelor.** Copiază cerința Confluence anterioară modificării în schema JSON de bază a laboratorului, captureaz-o și modifică varianta candidat la treizeci de zile. Incrementează revizia locală a instantaneului și păstrează separat în Jira versiunile reale Confluence. Fluxul cu GitHub ca sursă-rădăcină nu validează Confluence activ. Nu prezenta starea verde drept verificare a unei autorități externe.

**Nu introduce în mediul de execuție funcționalitatea de ștergere în acest exercițiu.** Un serviciu real necesită dovezi de implementare, date de test controlate, un mecanism de suspendare și teste ale limitelor la execuție. O îmbinare dovedește starea depozitului, nu comportamentul de retenție în producție.

## Urmărește publicarea parțială

| Pas | Stare inițială | Dovada finalizării |
|---|---|---|
| **REQ-17** | Pending | Versiunea rezultată a paginii |
| **Configurație** | Pending | Commit îmbinat și revizuire |
| **RUN-04** | Pending | Versiunea rezultată a paginii |
| **Închidere Jira** | Pending | Recitire finală și tranziție |

**Înregistrează fiecare rezultat înainte de a încerca pasul următor.** PROP-042 corelează evenimentele individuale ale sistemelor. Un singur rând finalizat nu înseamnă că întreaga schimbare este completă.

**Eșec ilustrativ:** Confluence publică treizeci de zile, dar GitHub refuză îmbinarea. Menține Jira în `Blocked` și cerința marcată cu livrare în așteptare. Produsul alege finalizarea sau restabilirea la șapte zile după revizuire. Nu transforma o copie de urgență a README-ului în autoritatea cerinței.

## Gestionează modificările concurente

**Bază pentru browser:** desemnează un singur editor în perioada pilotului. Redeschide Page History imediat înainte de editare și după publicare. Dacă alt autor schimbă sursa, oprește-te, compară, reconciliază și reînnoiește aprobarea. Publicarea serializată este o procedură, nu o garanție de tranzacție atomică.

**Extensie API:** documentația Confluence v2 descrie **`GET /wiki/api/v2/pages/{id}?body-format=storage`** și **`PUT /wiki/api/v2/pages/{id}`** cu un obiect de versiune. O integrare de publicare revizuită compară versiunea actuală cu baza aprobată, trimite versiunea următoare și recitește rezultatul. Nu reîmprospăta automat o versiune eșuată și nu reîncerca folosind un corp vechi.

**Succesul API singur nu este suficient.** Verifică textul rezultat, ID-ul sursei, domeniul și versiunea. Acest curs nu include un client API cu drept de scriere. Publicarea manuală în browser este baza executabilă pentru persoanele care nu programează.

## Verifică cazurile negative

| Injecție | Raționament așteptat |
|---|---|
| **Schimbă sursa după aprobare** | Oprește-te și aprobă din nou versiunea nouă |
| **Elimină accesul de editare al editorului** | Refuză actualizarea și păstrează registrul în așteptare |
| **Setează Jira la șaizeci de zile** | Oprește conflictul și păstrează autoritatea Confluence |
| **Publicarea runbook-ului eșuează** | Menține livrarea incompletă și atribuie recuperarea |

**Înregistrează rezultatele reale din sandbox** împreună cu rolul actorului și reviziile de dinainte și de după. Nu include conținutul protejat al paginii în dovezile pentru utilizatori fără acces. Rezultatele așteptate nu sunt rezultate măsurate.

## Asamblează pachetul de revizuire

**Fixează conținutul, nu doar eticheta propunerii.** PROP-042 apare în fiecare sistem, dar o etichetă nu identifică textul revizuit de responsabil. Include textul exact al cerinței, diff-ul de implementare, textul runbook-ului, versiunile surselor și ordinea publicării într-un singur pachet fix.

```text
Package: PROP-042 revision 1, illustrative
Intent: synthetic export retention changes from 7 to 30 days
Exclusions: production data, backups, legal holds
Requirement amendment: fixed proposed REQ-17 wording
Implementation: fixed candidate diff and protected base reference
Runbook amendment: fixed RUN-04 wording and recovery limits
Review: product and operations decisions for this package
Delivery: requirement -> implementation -> runbook -> closure
Stop: changed source, missing review, denied write, failed read-back
```

**Păstrează pachetul lizibil pentru ambii responsabili.** Produsul are nevoie de intenție și excluderi. Operațiunile au nevoie de schimbarea operațională și limitele de recuperare. Ambii trebuie să înțeleagă perioada în care intenția aprobată și configurația livrată diferă. Un simplu diff de cod nu este suficient pentru un responsabil nefamiliarizat cu fișierele depozitului.

**Conținutul completat al pachetului pentru acest exemplu sintetic:**

```text
REQ-17 proposed v5: "Synthetic export files are retained for 30 days from creation. This pilot excludes production data, backups, and legal holds. Delivery remains pending until the GitHub configuration and RUN-04 read-backs match this approved wording."

GitHub config.json, proposed change against base-001:
-  "retention_days": 7
+  "retention_days": 30

RUN-04 proposed v3: "Retention days: 30. Synthetic exports only. No deletion job runs in this lab. If publication fails, keep delivery pending, read back each source, and obtain owner approval before restoring the seven-day configuration or completing the thirty-day publication."
```

Aceste formulări sunt texte propuse pentru exemplu, nu înregistrări active ale tenantului. Atașează commit-ul de bază real și versiunile paginilor înainte de revizuire. Pachetul fix trebuie să includă corpurile propuse complete, nu un rezumat care obligă responsabilul să le deducă.

**Separă instantaneul offline de publicarea activă.** Chiar înainte de prima scriere, editorul verifică din nou paginile mapate, iar responsabilul depozitului verifică din nou baza protejată. Dacă oricare s-a schimbat, pachetul vechi se oprește la `Review`.

## Parcurge registrul

**Progresie ilustrativă a stării:** tabelul folosește revizii didactice, nu observații. Completează versiunile rezultate și commit-urile reale după fiecare scriere în sandbox.

| Pas | Stare după recitire reușită | Lucru rămas |
|---|---|---|
| **Revizuirea responsabililor completă** | Pachet aprobat, toate valorile publicate sunt șapte | Toți pașii de publicare |
| **REQ-17 publicat** | Intenție de treizeci, livrare în așteptare | Configurație și runbook |
| **Îmbinarea GitHub recitită** | Intenție/configurație de treizeci, runbook de șapte | Runbook și reconciliere finală |
| **RUN-04 publicat** | Toate înregistrările aplicabile sunt treizeci | Recitire finală independentă |
| **Livrare închisă** | Registru complet cu dovezi | Limitele la execuție declarate persistă |

**Livrarea în așteptare este o stare relevantă.** Evită să descrii implementarea veche drept conformă cu noua intenție cât timp publicarea este incompletă. În această perioadă, cititorii au nevoie de ambele valori, nu de un singur rezumat care pretinde că retenția este de treizeci de zile.

**Adaugă încercările eșuate ca evenimente separate.** Dacă scrierea runbook-ului eșuează, păstrează rezultatele reușite pentru cerință și configurație. Înregistrează acțiunea încercată, eșecul, versiunea neschimbată, rolul atribuit și pasul următor. Nu reseta rândurile finalizate la Pending și nu șterge secvența observată.

**Exemplu de respingere a unei versiuni vechi:** editorul citește REQ-17 v4, un alt editor autorizat publică v5, apoi editorul încearcă să aplice PROP-042 r1 peste v4. Platforma raportează un conflict de versiune sau citirea prealabilă scrierii detectează v5. Înregistrează actorul `publisher`, versiunea inițială `v4`, încercarea `PROP-042 r1`, conflictul observat sau schimbarea versiunii curente, versiunea finală `v5` nemodificată de această încercare și responsabilul atribuit `product owner`. Menține Jira în `Review`. Recitește v5, reconciliază textul și solicită revizuirea unui nou pachet fix înainte de o altă scriere. Într-un test activ, folosește răspunsul real al platformei și Page History. Acest rând este un exemplu didactic.

**Exemplu didactic completat, numai cu valori sintetice:**

| Sistem | Sursă inițială | Revizuire fixă | Scriere și recitire | Stare finală |
|---|---|---|---|---|
| Confluence REQ-17 | v4, șapte zile | PROP-042 r1, Produs a aprobat schimbarea v4 la v5 | Editorul a scris v5, revizorul a redeschis v5 | Treizeci de zile, backup-urile și reținerile legale excluse |
| Configurație GitHub | Commit-ul `main` `base-001`, șapte zile | PROP-042 r1, Operațiunile au aprobat diff-ul candidat | PR îmbinată ca `merge-002`, o clonă independentă a citit treizeci | Treizeci de zile în sursa protejată |
| Confluence RUN-04 | v2, șapte zile | PROP-042 r1, Operațiunile a aprobat schimbarea v2 la v3 | Editorul a scris v3, revizorul a redeschis v3 | Pas operațional de treizeci de zile cu revenire |
| Jira PROP-042 | In Review | Deciziile ambilor responsabili sunt legate de r1 | Responsabilul livrării a atașat dovezile și a trecut la Done | Închis după cele trei recitiri |

Etichetele de mai sus sunt ilustrative, nu dovezi din tenant. Registrul tău are nevoie de linkuri native către versiunile paginilor și de ID-uri commit. Înainte de a muta Jira la Done, atașează propunerea fixată, ambele revizuiri pe roluri, înregistrarea bazelor sursă, fiecare recitire a publicării, rezultatul testului negativ și limitele nerezolvate la execuție. Dacă lipsește un element, menține livrarea deschisă sau `Blocked`.

**Poarta pachetului:** marchează fiecare dintre cele cinci verificări ca `Supported` sau `Blocked`: reviziile surselor sunt recente, ambii responsabili au aprobat aceeași revizie fixă, toate publicările necesare corespund recitirii, limitele la execuție rămân explicite și starea recuperării este reconciliată. `Done` necesită cinci verificări `Supported` și nicio scriere neautorizată.

## Gestionează o scriere incertă

**Un timeout lasă rezultatul necunoscut.** Nu dovedește nici succesul, nici eșecul. În fluxul din browser, redeschide sursa mapată și inspectează conținutul și istoricul actual înainte de a decide dacă încerci din nou.

1. **Oprește pasul următor:** menține livrarea incompletă.
2. **Citește destinația:** compară textul actual, versiunea și domeniul cu pachetul fix.
3. **Înregistrează observația:** finalizată, neschimbată, în conflict sau inaccesibilă.
4. **Alege pasul următor:** continuă de la o stare de finalizare verificată, reîncearcă un pas autorizat neschimbat sau escaladează conflictul.
5. **Păstrează incertitudinea:** menține încercarea eșuată/necunoscută alături de recitirea ulterioară.

**Nu relua orbește întreaga secvență.** Repetarea unui pas deja finalizat adaugă revizii și riscă să suprascrie modificări fără legătură. Reia dintr-o stare verificată. Dacă nu ai acces la sursă, alege `Hold` în loc să ghicești pe baza registrului vechi.

## Compară deciziile de recuperare

| Situație | Decizia de revizuit | Motiv |
|---|---|---|
| **Cerința s-a schimbat, îmbinarea a fost refuzată** | Finalizează sau compensează cerința | Intenția și comportamentul diferă |
| **Configurația s-a schimbat, runbook-ul a fost refuzat** | Finalizează runbook-ul sau revino asupra configurației | Instrucțiunile operaționale sunt depășite |
| **Alt responsabil schimbă domeniul** | Revino la `Review` | Aprobarea fixă descrie un alt corp |
| **Rezultatul scrierii este necunoscut** | Citește mai întâi destinația | Reîncercarea depinde de starea observată |
| **Editorul pierde accesul** | Menține `Hold` și solicită administrare autorizată | Autorizarea veche nu permite scrieri noi |

**Alege pe baza stării actuale și a deciziei responsabilului.** Finalizarea înainte necesită aprobări actuale și controale funcționale. Compensarea necesită revizuirea restaurării în raport cu modificările intervenite. Recuperarea este o altă publicare, nu o excepție privilegiată de la proces.

## Verificarea finalizării publicării

**Predă un pachet pe care un revizor independent îl poate reconcilia.** Revizorul trebuie să găsească propunerea exactă revizuită, bazele sursă, ambele revizuiri pe roluri, rezultatul fiecărei scrieri, valorile finale și limitările rămase la execuție. Cere-i să identifice primul pas incomplet după o întrerupere.

**Raționament așteptat:** următoarea acțiune vine din surse recente și din registru, nu din încrederea asistentului anterior. Folosește referințele finale mapate în testele de recuperare, unde descoperirea trebuie să păstreze aceeași distincție de autoritate.

## Depanare și recuperare

**Versiunea s-a schimbat:** compară istoricul și reînnoiește revizuirea. **Verificarea instantaneului reușește, dar wiki diferă:** obține din nou sursele Confluence actuale. **Done a fost setat prea devreme:** redeschide prin fluxul permis și înregistrează pașii lipsă.

**Recuperare:** folosește comparația Page History și o restaurare sau o editare compensatorie revizuită de un responsabil. Înregistrează versiunea rezultată în loc să presupui că restaurarea resetează numerotarea. Revino asupra configurației printr-o PR protejată dacă Produsul alege revenirea. Fișierele șterse nu sunt incluse în promisiunea de revenire.

## Exercițiu și autoevaluare

**Întrerupe procesul după publicarea REQ-17** și oferă altui editor doar harta și registrul.

**Raționament așteptat:** acesta obține sursele actuale, confirmă aprobarea fixă și reia doar pasul în așteptare autorizat. Dovezile lipsă trimit lucrarea înapoi la `Review`.

## Referințe principale

- **Istoric și restaurare:** [documentația tehnică Confluence](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Operațiuni API cu versiuni:** [pagini Confluence REST API v2](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/).
- **Controale de flux de lucru:** [fluxuri Jira avansate](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).
- **Securitatea integrării:** [bune practici de securitate MCP](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices).

## Pașii următori

**Continuă cu [Recuperare pornind de la hartă](/articles/ai-collaboration-map-first-retrieval/)** după finalizarea unei runde de publicare revizuite.
