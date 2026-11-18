---
title: "Configurarea AI în Confluence și Jira: permisiuni și autoritate"
date: 2026-10-01
lastmod: 2026-11-12
toc: true
draft: false
description: "Configurați pagini de referință în Confluence și permisiuni Jira administrate de companie pentru colaborarea între echipe cu revizuire."
genre: ["Inteligență artificială", "Colaborare în echipă", "Inginerie software"]
tags: ["curs de colaborare AI", "Confluence Cloud", "Jira Cloud", "pagini de referință", "schemă de permisiuni Jira", "tranziție de flux de lucru", "teste de acces"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustrație cu profesioniști care revizuiesc lucrul comun la un proiect într-un spațiu de lucru pentru securitate cibernetică"
coverCaption: ""
---

[Reveniți la cursul de colaborare AI](/ai-collaboration-course-start/)

**Administratorul stabilește autoritatea la locul de muncă înainte să conecteze instrumentele de chat.** Proprietarii de produs și operațiuni publică cerințe și proceduri în Confluence Cloud. Jira Cloud coordonează livrarea. GitHub gestionează implementarea. Creați medii de testare dedicate după ce pregătiți baza, deoarece o permisiune acordată greșit expune informații indiferent de comportamentul modelului.

## Idei principale

- **Confluence** păstrează formularea aprobată a cerințelor.
- **Jira** gestionează starea livrării, nu politica de păstrare.
- **GitHub** gestionează configurația și politica comună.
- **Testele de permisiuni** necesită planuri potrivite și utilizatori separați.

## Înainte să începeți

**Cerințe preliminare:** [fundamentele](/articles/ai-collaboration-pilot-foundation/), depozitul laboratorului, administrarea spațiilor Confluence și administrarea Jira, plus utilizatori separați cu rolurile de colaborator, proprietar și editor. **Timp estimat:** 90–120 de minute. **Dificultate:** administrare avansată.

**Cerința planului:** Confluence Free nu acceptă restricții de conținut. Jira Free nu oferă scheme de permisiuni configurabile, roluri de spațiu sau scheme de securitate pentru elemente de lucru. Pentru această etapă folosiți medii de testare potrivite, cu Standard sau un plan superior. Înainte de testare, verificați planul și privilegiile reale în sursele de referință.

**Notă privind navigarea:** documentația Jira actuală folosește „space” și „work item”. Unele instanțe încă folosesc „project” și „issue”. Alegeți o configurație administrată de companie. Această procedură nu acoperă comportamentul permisiunilor administrate de echipă. Nu sunt necesare Rovo, aplicații Marketplace, aprobări Jira Service Management sau un conector de chat plătit.

**Rezultatul:** pregătiți o matrice de permisiuni, pagini de referință denumite, un flux de lucru Jira doar pentru laborator și dovezi de acces refuzat pentru utilizatori separați. Notați planul instanței și ipotezele privind rolurile lângă rezultatele testelor.

**Verificați înainte să creați înregistrări:**

| Verificare | Dacă este disponibilă | Dacă lipsește |
|---|---|---|
| Restricții de pagină și administrarea spațiului Confluence | Creați separat pagini aprobate și excluse | Marcați drept Blocate testele de editare a paginii și de refuz al citirii |
| Schemă de permisiuni și editor de flux Jira administrate de companie | Copiați o schemă și un flux doar pentru laborator | Marcați drept Blocate testele tranzițiilor |
| Utilizatori separați pentru colaborator, proprietar, editor și utilizator exclus | Rulați teste pozitive și negative pentru fiecare rol | Marcați drept Blocate rolurile netestate |
| Responsabilul depozitului și ramură protejată | Asociați traseul de implementare revizuit | Finalizați mai întâi traseul GitHub-first, înainte de publicarea mixtă |

În octombrie 2026, folosiți butonul **Share** sau controlul de restricții pentru accesul la pagină, zona de permisiuni **Space settings** din Confluence pentru acordări mai largi și **Settings > Work items > Permission schemes** în Jira pentru schema laboratorului. Editorul fluxului Jira administrat de companie controlează tranzițiile. Etichetele UI și funcțiile planului diferă între instanțe. Înainte de acești pași, înregistrați în dovezi traseul și planul reale. Consultați [permisiunile la nivel de pagină Confluence](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/) și [schemele de permisiuni Jira](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/).

## Creați paginile de referință

1. **Creați un spațiu Confluence** numit **`Export Service Lab`**. Dezactivați accesul anonim și partajarea publică prin controalele disponibile pentru site sau spațiu.
2. **Creați pagini publicate**, nu documente live, cu numele **`REQ-17 Export Retention`**, **`RUN-04 Export Cleanup`** și **`Decision Register`**.
3. Ca proprietar de produs, **publicați cerința inițială** de mai jos. Notați în harta depozitului ID-ul și versiunea reale ale paginii.
4. Ca proprietar de operațiuni, **publicați RUN-04** cu păstrare de șapte zile și mențiunea că în acest laborator nu rulează nicio sarcină de ștergere.
5. Pe fiecare pagină de referință, **deschideți Share**. Setați accesul general doar pentru citire pentru membrii eligibili ai spațiului și acordați separat drepturi specifice de editare proprietarilor și editorilor desemnați. Salvați și verificați cu utilizatorul colaborator.

```text
ID sursă: REQ-17
Rolul proprietarului: product-owner
Stare: bază aprobată
Domeniu: numai fișiere de export sintetice
Perioadă de păstrare: 7 zile
Starea livrării: configurația de bază a laboratorului
Excepții: datele de producție, copiile de rezervă și obligațiile legale de păstrare sunt excluse
Dovada aprobării: revizuirea bazei DEC-12
Referință de implementare: atașează commitul de bază protejat din GitHub
```

**Aplicați restricții fiecărei pagini de referință.** Nu presupuneți că restricția de editare a unei pagini părinte protejează și paginile copil. Moștenirea permisiunilor de citire și editare diferă, iar permisiunile spațiului se aplică în continuare. Un link nu acordă acces. Verificați toate apartenențele dacă un utilizator care ar trebui să aibă doar citire poate totuși edita.

**Folosiți aceste texte inițiale pentru celelalte două pagini.** Înlocuiți câmpurile temporare de revizuire cu dovezi reale din mediul de testare înainte să aprobați o înregistrare.

```text
ID sursă: RUN-04
Rolul proprietarului: operations-owner
Stare: bază aprobată
Domeniu: numai fișiere de export sintetice
Perioadă de păstrare configurată: 7 zile
Procedură: compară REQ-17 cu config.json înainte de o modificare revizuită
Limită de execuție: laboratorul nu are o sarcină de ștergere și nu produce dovezi de ștergere
Recuperare: restabilește configurația aprobată anterioară după revizuire
Limită de recuperare: restabilirea configurației nu recuperează fișierele șterse
Dovada revizuirii: adaugă recenzentul real, versiunea paginii și referința deciziei
```

```text
Pagină: Registrul deciziilor
ID intrare: DEC-12
Decizie: folosește șapte zile ca bază sintetică
Domeniu: numai export-service-lab
Cerință: înregistrează versiunea paginii REQ-17 după publicare
Manual: înregistrează versiunea paginii RUN-04 după publicare
Politică: înregistrează revizia GitHub protejată POL-01 după revizuire
Revizuire produs: în așteptare până când proprietarul desemnat înregistrează o decizie
Revizuire operațiuni: în așteptare până când proprietarul desemnat înregistrează o decizie
Stare: exemplu de ciornă, înlocuiește cu dovezi observate ale revizuirii
```

## Actualizați harta

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

**Adăugați în hartă locațiile private reale ale mediului de testare și ID-urile paginilor.** Șablonul numește sursele cu autoritate fără să pretindă că include adrese active. Eliminați din README formulările care atribuie fișierului JSON copiat autoritatea asupra cerințelor din traseul mixt.

**Păstrați POL-01 în GitHub** pentru ambele trasee. Confluence indică revizia sa verificată. Mutarea sursei de autoritate a politicii în timpul unei sarcini necesită o altă tranziție de autoritate revizuită.

## Setați permisiunile Jira

1. **Creați un spațiu de laborator administrat de companie** și copiați o schemă de permisiuni într-o schemă separată pentru laborator. Nu modificați o schemă de producție comună.
2. **Deschideți Settings, Work items, Permission Schemes**, selectați schema laboratorului și actualizați acordările.
3. **Acordați colaboratorilor permisiuni de vizualizare, creare și comentare.** Restricționați privilegiile administrative. Verificați explicit permisiunile de editare și **Transition work items**.
4. **Asociați schema** spațiului de laborator și verificați că niciun spațiu de producție nu o partajează.
5. **Creați PROP-042** ca element de lucru. Notați cheia generată în hartă și păstrați PROP-042 ca ID logic al propunerii în descriere.

**Lipiți această schiță în PROP-042.** Elementul Jira urmărește livrarea. Textul său nu înlocuiește formularea aprobată în Confluence.

```text
ID propunere: PROP-042
Stare: ciornă
Valoare aprobată curentă: 7 zile, de înregistrat versiunea paginii REQ-17
Valoare propusă: 30 de zile pentru fișiere de export sintetice
Excluderi: date de producție, copii de rezervă și obligații legale de păstrare
Înregistrări afectate: REQ-17, RUN-04, config.json, proposal.json
Atașament fix al propunerii: în așteptare
Revizuirea proprietarului de produs: în așteptare
Revizuirea proprietarului operațional: în așteptare
Registrul publicării: în așteptare
Oprește-te dacă se schimbă versiunea sursei, lipsește revizuirea sau accesul este refuzat
```

| Rol | Confluence | Jira | GitHub |
|---|---|---|---|
| **Colaborator** | Citește paginile aprobate | Creează și comentează schițe | Ramură de propunere sau Issue |
| **Proprietar de produs** | Revizuiește cerința | Înregistrează revizuirea cerinței | Revizuiește dovezile PR |
| **Proprietar de operațiuni** | Revizuiește procedura | Înregistrează revizuirea operațională | Revizuiește impactul operațional |
| **Editor** | Editează pagini aprobate | Înregistrează starea publicării | Fără autoritate automată de îmbinare |
| **Responsabil tehnic** | Citește cerința | Înregistrează implementarea | Revizuiește și integrează PR-ul protejat |

**Permisiunile acordate prin grupuri diferite se adună.** Eliminați acordările prea largi și neintenționate din laborator, în loc să presupuneți că una restrânsă o înlocuiește pe cea largă. Nu adăugați identitățile conectorilor în grupuri administrative.

## Setați stările livrării

**Copiați un flux administrat de companie** într-un flux doar pentru laborator. Adăugați stările Schiță, Revizuire, Aprobat, Publicare, Finalizat și Blocat. Adăugați tranziții pentru trimitere, aprobare, publicare, finalizare, blocare și revenire la revizuire. Asociați-l doar tipului de lucru din laborator.

1. **Selectați tranziția către Aprobat** în editorul fluxului.
2. **Adăugați o condiție sau restricție** care limitează acțiunea la rolul ori grupul desemnat de proprietar/editor. Folosiți controalele documentate și publicați schița fluxului ca administrator.
3. **Verificați manual revizuirile ambilor proprietari** înainte de tranziție. Fiecare revizuire identifică propunerea fixată și versiunile surselor.
4. **Restricționați Finalizat** la rolul responsabil de livrare. Eliminați tranzițiile alternative sau globale care ocolesc această limită.

**O tranziție restricționată nu înseamnă aprobare de către două persoane.** Ea controlează persoana care execută tranziția. În acest pilot, verificarea dovezilor celor două roluri rămâne procedurală. Notați explicit această limită.

**Exemplu de înregistrare a tranziției:** pentru **Revizuire către Aprobat**, permiteți numai grupului desemnat de proprietari/editori să activeze tranziția. Înainte de activare, persoana deschide atașamentul fix PROP-042 și verifică decizia proprietarului de produs și a celui de operațiuni pentru aceeași revizie a propunerii. Dacă lipsește o decizie sau indică o revizie mai veche, lăsați elementul în Revizuire și notați lipsa. Restricția fluxului controlează persoana care execută tranziția. Verificarea dovezilor este un pas uman separat.

## Verificați refuzul

**Ca utilizator colaborator**, citiți REQ-17, încercați să îl editați, creați schița Jira și încercați tranziția la Aprobat. Rezultatele așteptate sunt cerință lizibilă, editare refuzată, propunere creată cu succes și aprobare refuzată. Comparați versiunile sursei înainte și după refuz.

**Ca utilizator exclus**, deschideți o pagină sintetică separată și restricționată. Conținutul nu ar trebui să fie accesibil. Testați paginile copil independent. Nu lipiți text protejat în chatul utilizatorului exclus ca ocolire.

## Adaptați harta depozitului

**Păstrați ID-urile surselor stabile când se schimbă locația lor.** REQ-17 indică în continuare intenția aprobată privind păstrarea, dar în traseul mixt sursa sa este o pagină Confluence. Un instantaneu din depozit ajută verificarea și revizuirea. Nu înlocuiește pagina-sursă autoritativă.

| Înregistrare | Sursă cu autoritate | Tratament în depozit |
|---|---|---|
| **REQ-17** | Pagina de cerințe Confluence indicată în hartă | Instantaneu cu dovada reviziei paginii |
| **RUN-04** | Pagina de procedură Confluence indicată în hartă | Fragment operațional capturat pentru consecvență |
| **POL-01** | Politică protejată în GitHub | Instrucțiunile comune ale agenților fac referire la ea |
| **Configurație** | Înregistrare protejată în GitHub | Diferență de implementare propusă |
| **Livrare** | Element de lucru Jira | Link de corelare, nu copie a politicii |

**Adăugați proveniența lângă instantanee.** În pachetul privat al propunerii, notați ID-ul sursei, referința și versiunea paginii, momentul capturii și rolul persoanei care a capturat-o. Nu includeți identificatori nativi de pagină în lucrările publice ale cursului. Dacă editorul găsește o altă versiune actuală, reconciliați înainte să folosiți instantaneul.

**Nu redenumiți autoritatea pentru a se potrivi instrumentului.** Descrierea editabilă Jira este utilă pentru discuții, dar rămâne o înregistrare de livrare. O mențiune de treizeci de zile în Jira nu înlocuiește o cerință de șapte zile în Confluence.

## Proiectați testele de acces

**Separați citirea, redactarea și publicarea.** Un colaborator are nevoie de acces suficient pentru a înțelege cerința sintetică și a trimite o propunere. Nu are nevoie de drept de editare asupra paginii de referință sau de permisiunea de a-și aproba propria propunere.

```text
Înregistrare de test: PERM-REQ-EDIT
Rol: colaborator
Sursă: REQ-17
Condiție prealabilă: sursa poate fi citită, iar revizia publicată a fost capturată
Încercare: editează cerința autoritativă
Rezultat așteptat: editare refuzată, revizie publicată neschimbată
Observat: completează din sandbox
Dovadă: rezultat nativ și recitire independentă a reviziei
Recenzent: administrator sau revizor independent al permisiunilor
```

**Folosiți o înregistrare separată pentru refuzul citirii.** Cerința lizibilă de către colaborator testează separarea publicării de editare. Pagina inaccesibilă utilizatorului exclus testează confidențialitatea. Combinarea cazurilor într-un singur rând ascunde limita verificată.

**Verificați și accesul permis.** Proprietarii și editorii trebuie să poată folosi traseul alocat. Dacă fiecare utilizator primește refuz, mediul de testare este restrictiv, dar inutilizabil. Păstrați dovada unei editări autorizate reușite pe o pagină de testare temporară, fără să modificați cerința aprobată în timpul diagnosticării permisiunilor.

## Repetați revizuirea Jira

**Tratați numele stărilor ca designul acestui pilot.** Schiță conține o solicitare. Revizuire conține un pachet fixat. Aprobat înseamnă că proprietarii au terminat revizuirea. Publicare indică o livrare incompletă. Finalizat necesită o citire de verificare. Blocat indică lipsa dovezilor sau accesului ori un conflict nerezolvat.

| Tranziție | Pachet necesar | Verificare responsabilă |
|---|---|---|
| **Schiță către Revizuire** | Propunere fixă și versiuni ale surselor | Colaboratorul confirmă completitudinea |
| **Revizuire către Aprobat** | Deciziile de produs și operațiuni | Actorul autorizat verifică ambele roluri |
| **Aprobat către Publicare** | Comparație cu sursele actuale | Editorul confirmă că bazele nu s-au schimbat |
| **Publicare către Finalizat** | Registru complet pentru fiecare sistem | Responsabilul livrării verifică citirea de control |
| **Orice pas acceptat către Blocat** | Eșec și acțiune în așteptare | Responsabil de recuperare desemnat |

**Repetați exercițiul cu un pachet sintetic incomplet.** Trimiteți doar revizuirea produsului și cereți actorului autorizat să evalueze tranziția. Rezultatul așteptat este păstrarea lucrării în Revizuire și solicitarea revizuirii operaționale. Aceasta testează pasul procedural separat de refuzul platformei pentru colaborator.

**Testați intenționat rutele alternative.** În vizualizarea fluxului din mediul de testare, inspectați fiecare rută către Aprobat și Finalizat. O tranziție numită și restricționată nu ajunge dacă o altă rută disponibilă ocolește aceeași limită de revizuire. Notați rutele inspectate și actorul folosit, fără să pretindeți acoperire completă după un singur clic.

## Diagnosticați accesul neașteptat

**Începeți cu identitatea efectivă.** Confirmați că sesiunea browserului aparține rolului de testare vizat. Apoi verificați apartenența la grupuri, permisiunile spațiului, accesul la pagini și asocierea fluxului folosind instrumentele de administrare ale produsului. Nu schimbați mai multe controale simultan, deoarece refuzul își pierde valoarea diagnostică.

1. **Confirmați identitatea:** folosiți sesiuni separate pentru colaborator, editor și utilizator exclus.
2. **Găsiți permisiunea:** identificați apartenența sau setarea care permite acțiunea încercată.
3. **Ajustați controlul de laborator:** păstrați accesul legitim al proprietarilor.
4. **Repetați aceeași încercare:** după refuz, capturați versiunea sursei nemodificată.
5. **Repetați cazul pozitiv:** confirmați că publicarea autorizată încă funcționează.

**Lista finală de dovezi:** înregistrați arborele paginilor Confluence și ID-urile asociate, asocierea schemei Jira de laborator, asocierea fluxului de laborator, apartenența fiecărui rol de testare la grupuri, citirea permisă a cerinței, editarea refuzată cu versiunea neschimbată, crearea permisă a unei schițe, tranziția la Aprobat refuzată fără schimbarea stării, citirea refuzată pentru utilizatorul exclus și responsabilul curățării. Pentru fiecare rând, păstrați rolul actorului, versiunea sau starea inițială și finală, rezultatul nativ și evaluatorul independent. Notați calea de navigare observată în instanță, deoarece etichetele și controalele disponibile variază în funcție de plan.

**Verificarea finalizării:** livrați paginile de referință din hartă, fluxul rezervat laboratorului, matricea de roluri dorită și înregistrările de permisiuni observate. Dacă planul nu oferă un control necesar, lăsați rândul relevant Blocat. Lecția despre publicare presupune că testele au reușit, nu doar că există capturi ale setărilor.

## Depanare și revenire

**Colaboratorul încă poate edita:** verificați accesul paginii, permisiunile spațiului și apartenențele. **Tranziția încă reușește:** verificați asocierea fluxului și rutele de ocolire. **Lipsesc setările:** verificați tipul administrat de companie, ediția și privilegiile de administrator.

**Revenire:** eliminați permisiunile conectorilor și arhivați schițele. Dezasociați schemele și fluxurile rezervate laboratorului după păstrarea dovezilor. Restaurați formularea aprobată a paginii din istoricul revizuit sau printr-o editare corectivă. Nu ștergeți dovezile de audit.

## Exercițiu și autoevaluare

**Jira indică treizeci de zile, iar REQ-17 indică șapte.** Identificați valoarea folosită la implementare și proprietarul responsabil de reconciliere.

**Raționament așteptat:** Confluence stabilește intenția. Jira conține o eroare de propunere sau livrare. Opriți publicarea și cereți proprietarului de produs să reconcilieze, în loc să alegeți cel mai recent marcaj temporal.

## Referințe principale

- **Restricții și plan:** [permisiuni Confluence](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Controale de partajare:** [acces la conținut specific](https://support.atlassian.com/confluence-cloud/docs/add-or-remove-page-restrictions/).
- **Administrarea schemei:** [scheme de permisiuni Jira](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).
- **Condiții de tranziție:** [fluxuri de lucru avansate](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).

## Pașii următori

**După ce testele de acces reușesc, continuați cu [Publicarea între sisteme](/articles/ai-collaboration-confluence-jira-publication/)**.
